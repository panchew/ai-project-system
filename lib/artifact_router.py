"""
Artifact router module for daemon integration.

This module provides the ArtifactRouter class which handles:
- Monitoring artifact directories
- Acquiring locks and reading safely
- Parsing and validating schema via ArtifactParser
- Idempotency tracking
- Writing JSON triggers to .ai-project/queue/
- Moving processed files to .processed/ or .failed/
"""

import json
import logging
import time
import fcntl
from pathlib import Path
from typing import Dict, Any, List, Optional, Union

from lib.artifact_parser import ArtifactParser, Artifact
from lib.artifact_errors import ArtifactError


class IdempotencyTracker:
    """Tracks processed artifacts to prevent duplicate routing."""

    def __init__(self, tracking_file: Path):
        self.tracking_file = Path(tracking_file)
        self.processed_signatures = set()
        self._load()

    def _load(self) -> None:
        if self.tracking_file.exists():
            try:
                with open(self.tracking_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        self.processed_signatures = set(data)
            except Exception:
                # Fallback on corrupt files
                self.processed_signatures = set()

    def _save(self) -> None:
        try:
            self.tracking_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.tracking_file, "w", encoding="utf-8") as f:
                json.dump(list(self.processed_signatures), f, indent=2)
        except Exception:
            pass

    def get_signature(self, artifact: Artifact) -> str:
        """Create a unique string signature for the artifact."""
        a_type = artifact.artifact_type
        ref_id = (
            artifact.get_epic_id()
            or artifact.get_milestone_id()
            or artifact.get_phase_id()
            or "unknown"
        )
        ts = artifact.get_timestamp() or "no-timestamp"
        return f"{a_type}:{ref_id}:{ts}"

    def is_processed(self, artifact: Artifact) -> bool:
        """Check if artifact has already been processed."""
        sig = self.get_signature(artifact)
        return sig in self.processed_signatures

    def mark_processed(self, artifact: Artifact) -> None:
        """Mark artifact as processed and save state."""
        sig = self.get_signature(artifact)
        self.processed_signatures.add(sig)
        self._save()


class ArtifactRouter:
    """Routes artifacts to target chats by creating triggers in the queue."""

    def __init__(
        self,
        project_root: Optional[Union[str, Path]] = None,
        logger: Optional[logging.Logger] = None,
    ):
        self.project_root = Path(project_root or ".").resolve()
        self.queue_dir = self.project_root / ".ai-project" / "queue"
        
        self.artifact_dirs = {
            "completion_notice": self.project_root / ".ai-project" / "artifacts" / "completion-notices",
            "review_decision": self.project_root / ".ai-project" / "artifacts" / "review-decisions",
            "delivery_notice": self.project_root / ".ai-project" / "artifacts" / "delivery-notices",
        }

        # Set up logger
        if logger is None:
            self.logger = logging.getLogger("ai_project_daemon.router")
            # If logger has no handlers, configure default logging to console/file
            if not self.logger.handlers:
                self.logger.setLevel(logging.INFO)
                log_dir = self.project_root / ".ai-project" / "logs"
                log_dir.mkdir(parents=True, exist_ok=True)
                
                # File handler
                fh = logging.FileHandler(log_dir / "daemon.log", encoding="utf-8")
                fh.setFormatter(
                    logging.Formatter(
                        "[%(asctime)s] [%(levelname)s] %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",
                    )
                )
                self.logger.addHandler(fh)
                
                # Console handler
                ch = logging.StreamHandler()
                ch.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
                self.logger.addHandler(ch)
        else:
            self.logger = logger

        self.parser = ArtifactParser()
        self.tracker = IdempotencyTracker(
            self.project_root / ".ai-project" / "processed_artifacts.json"
        )
        self.ensure_directories()

    def ensure_directories(self) -> None:
        """Ensure all queue and artifact directories exist, including subfolders."""
        self.queue_dir.mkdir(parents=True, exist_ok=True)
        for _, directory in self.artifact_dirs.items():
            directory.mkdir(parents=True, exist_ok=True)
            (directory / ".processed").mkdir(parents=True, exist_ok=True)
            (directory / ".failed").mkdir(parents=True, exist_ok=True)

    def wait_for_write_completion(self, filepath: Path, timeout: float = 2.0) -> Optional[Any]:
        """Wait for write completion using file size stability and flock.
        
        Returns open file object if lock acquired, or None if timeout.
        """
        try:
            if not filepath.exists():
                return None
        except OSError:
            return None

        start_time = time.time()
        last_size = -1

        # Wait until file size is stable
        while time.time() - start_time < (timeout / 2.0):
            try:
                current_size = filepath.stat().st_size
            except OSError:
                current_size = -1

            if current_size == last_size and current_size > 0:
                break
            last_size = current_size
            time.sleep(0.1)

        # Try to acquire flock exclusive lock
        try:
            f = open(filepath, "r+b")
        except (OSError, IOError):
            try:
                f = open(filepath, "rb")
            except (OSError, IOError):
                return None

        lock_acquired = False
        while time.time() - start_time < timeout:
            try:
                fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                lock_acquired = True
                break
            except (IOError, BlockingIOError):
                time.sleep(0.1)

        if lock_acquired:
            return f
        else:
            try:
                f.close()
            except OSError:
                pass
            return None

    def process_file(self, filepath: Path) -> bool:
        """Safely locks, parses, routes, and archives a single artifact file."""
        filepath = Path(filepath).resolve()
        
        # Skip if already in .processed or .failed
        if ".processed" in filepath.parts or ".failed" in filepath.parts:
            return False

        self.logger.info(f"Detected new artifact file: {filepath.name}")

        try:
            f = self.wait_for_write_completion(filepath)
            if f is None:
                self.logger.error(f"Timeout waiting for file lock on {filepath.name}")
                return False

            # Read file contents while lock is held
            f.seek(0)
            content = f.read().decode("utf-8")
            # Close file to release flock
            f.close()
            
            # Parse & validate schema
            artifact = self.parser.parse_content(content, filepath=filepath)
            
            # Idempotency check
            if self.tracker.is_processed(artifact):
                self.logger.info(
                    f"Skipping already processed artifact: {filepath.name} "
                    f"({self.tracker.get_signature(artifact)})"
                )
                self.archive_file(filepath, success=True)
                return True

            # Route based on artifact type
            routed = False
            if artifact.artifact_type == "completion_notice":
                routed = self.route_completion_notice(artifact)
            elif artifact.artifact_type == "review_decision":
                routed = self.route_review_decision(artifact)
            elif artifact.artifact_type == "delivery_notice":
                routed = self.route_delivery_notice(artifact)
            else:
                self.logger.error(f"Unknown artifact type: {artifact.artifact_type}")

            if routed:
                self.tracker.mark_processed(artifact)
                self.archive_file(filepath, success=True)
                return True
            else:
                self.logger.error(f"Failed to route artifact: {filepath.name}")
                self.archive_file(filepath, success=False)
                return False

        except Exception as e:
            self.logger.error(f"Error processing artifact {filepath.name}: {e}")
            # Ensure file is closed
            try:
                f.close()
            except Exception:
                pass
            self.archive_file(filepath, success=False)
            return False

    def route_completion_notice(self, artifact: Artifact) -> bool:
        """Route Completion Notice to parent chat (Milestone or HQ)."""
        epic_id = artifact.get_epic_id()
        milestone_id = artifact.get_milestone_id()
        phase_id = artifact.get_phase_id()

        if not epic_id:
            self.logger.error("Completion Notice missing epic_id")
            return False

        # Determine parent
        if milestone_id:
            parent = "milestone"
            parent_ref = milestone_id
        elif phase_id:
            parent = "phase"
            parent_ref = phase_id
        else:
            parent = "hq"
            parent_ref = "hq"

        # Create trigger payload
        trigger = {
            "action": "route_artifact",
            "artifact_type": "completion_notice",
            "artifact_path": str(artifact.filepath),
            "epic_id": epic_id,
            "parent": parent,
            "parent_ref": parent_ref,
            "timestamp": artifact.get_timestamp() or "",
        }

        # Write trigger to queue
        trigger_path = self.queue_dir / f"route_completion_{epic_id}.json"
        try:
            with open(trigger_path, "w", encoding="utf-8") as out:
                json.dump(trigger, out, indent=2)
            self.logger.info(
                f"[✓] Routed Completion Notice {epic_id} to {parent} Chat ({parent_ref})"
            )
            return True
        except Exception as e:
            self.logger.error(f"Failed to write Completion Notice trigger: {e}")
            return False

    def route_review_decision(self, artifact: Artifact) -> bool:
        """Route Review Decision back to Epic Chat or child level."""
        epic_id = artifact.get_epic_id()
        milestone_id = artifact.get_milestone_id()
        phase_id = artifact.get_phase_id()
        decision = artifact.frontmatter.get("decision")

        # Determine target channel
        if epic_id:
            target = "epic"
            target_ref = epic_id
        elif milestone_id:
            target = "milestone"
            target_ref = milestone_id
        elif phase_id:
            target = "phase"
            target_ref = phase_id
        else:
            target = "hq"
            target_ref = "hq"

        trigger = {
            "action": "route_artifact",
            "artifact_type": "review_decision",
            "artifact_path": str(artifact.filepath),
            "decision": decision,
            "target": target,
            "target_ref": target_ref,
            "timestamp": artifact.get_timestamp() or "",
        }

        # Write trigger to queue
        trigger_path = self.queue_dir / f"route_review_{target_ref}.json"
        try:
            with open(trigger_path, "w", encoding="utf-8") as out:
                json.dump(trigger, out, indent=2)
            self.logger.info(
                f"[✓] Routed Review Decision ({decision}) for {target_ref} to {target} Chat"
            )
            return True
        except Exception as e:
            self.logger.error(f"Failed to write Review Decision trigger: {e}")
            return False

    def route_delivery_notice(self, artifact: Artifact) -> bool:
        """Route Delivery Notice to parent chat for acknowledgment."""
        epic_id = artifact.get_epic_id()
        milestone_id = artifact.get_milestone_id()
        phase_id = artifact.get_phase_id()

        # Determine parent
        if milestone_id:
            parent = "milestone"
            parent_ref = milestone_id
        elif phase_id:
            parent = "phase"
            parent_ref = phase_id
        else:
            parent = "hq"
            parent_ref = "hq"

        trigger = {
            "action": "route_artifact",
            "artifact_type": "delivery_notice",
            "artifact_path": str(artifact.filepath),
            "epic_id": epic_id,
            "parent": parent,
            "parent_ref": parent_ref,
            "timestamp": artifact.get_timestamp() or "",
        }

        ref_key = epic_id or parent_ref
        trigger_path = self.queue_dir / f"route_delivery_{ref_key}.json"
        try:
            with open(trigger_path, "w", encoding="utf-8") as out:
                json.dump(trigger, out, indent=2)
            self.logger.info(
                f"[✓] Routed Delivery Notice for {ref_key} to {parent} Chat ({parent_ref})"
            )
            return True
        except Exception as e:
            self.logger.error(f"Failed to write Delivery Notice trigger: {e}")
            return False

    def archive_file(self, filepath: Path, success: bool = True) -> None:
        """Move artifact file to either .processed/ or .failed/."""
        try:
            subdir = ".processed" if success else ".failed"
            dest_dir = filepath.parent / subdir
            dest_dir.mkdir(parents=True, exist_ok=True)
            dest_path = dest_dir / filepath.name
            
            # If destination already exists, delete it first to avoid rename issues
            if dest_path.exists():
                dest_path.unlink()
                
            filepath.rename(dest_path)
            status_str = "processed" if success else "failed"
            self.logger.info(f"Moved {filepath.name} to {subdir}/")
        except Exception as e:
            self.logger.error(f"Failed to archive file {filepath.name}: {e}")
