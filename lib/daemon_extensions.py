"""
Daemon Extensions for Artifact Monitoring and Routing.

This module provides the core functions and loops for the background daemon to
monitor and route artifacts without blocking other operations.
"""

import os
import sys
import time
import logging
import signal
from pathlib import Path
from typing import Union, Optional

from lib.artifact_router import ArtifactRouter


def setup_daemon_logger(project_root: Path) -> logging.Logger:
    """Set up loggers for the daemon."""
    log_dir = project_root / ".ai-project" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    
    logger = logging.getLogger("ai_project_daemon")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        # File Handler
        fh = logging.FileHandler(log_dir / "daemon.log", encoding="utf-8")
        fh.setFormatter(
            logging.Formatter(
                "[%(asctime)s] [%(levelname)s] %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
        )
        logger.addHandler(fh)
        
        # Console Handler
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
        logger.addHandler(ch)
        
    return logger


def process_artifacts(project_root: Union[str, Path]) -> None:
    """One-off scan and process of all new artifacts under the project root.
    
    Used for manual triggering, testing, and integration steps.
    """
    root_path = Path(project_root).resolve()
    logger = setup_daemon_logger(root_path)
    router = ArtifactRouter(project_root=root_path, logger=logger)
    
    for a_type, directory in router.artifact_dirs.items():
        if not directory.exists():
            continue
            
        for path in directory.glob("*.md"):
            if ".processed" in path.parts or ".failed" in path.parts:
                continue
            if path.is_dir():
                continue
                
            try:
                router.process_file(path)
            except Exception as e:
                logger.error(
                    f"Unexpected error processing {path.name} "
                    f"in process_artifacts: {e}"
                )


def daemon_artifact_monitoring_loop(
    project_root: Union[str, Path], interval: float = 10.0
) -> None:
    """Continuous background loop for artifact monitoring and routing."""
    root_path = Path(project_root).resolve()
    logger = setup_daemon_logger(root_path)
    router = ArtifactRouter(project_root=root_path, logger=logger)
    
    logger.info(f"[*] Daemon loop started (PID: {os.getpid()})")
    
    running = True
    
    def handle_signal(signum, frame):
        nonlocal running
        logger.info(
            f"[!] Daemon received signal {signum}. Cleaning up and exiting..."
        )
        running = False
        
    try:
        signal.signal(signal.SIGTERM, handle_signal)
        signal.signal(signal.SIGINT, handle_signal)
    except ValueError:
        # Ignore if running in a thread or non-main context where signals are restricted
        pass

    while running:
        try:
            # Ensure directories exist
            router.ensure_directories()
            
            # Scan directories
            for a_type, directory in router.artifact_dirs.items():
                if not directory.exists():
                    continue
                    
                for path in directory.glob("*.md"):
                    if ".processed" in path.parts or ".failed" in path.parts:
                        continue
                    if path.is_dir():
                        continue
                        
                    try:
                        router.process_file(path)
                    except Exception as e:
                        logger.error(
                            f"Unexpected error processing {path.name} in loop: {e}"
                        )
                        
            time.sleep(interval)
        except KeyboardInterrupt:
            logger.info("[!] Daemon loop interrupted by user.")
            break
        except Exception as e:
            logger.error(f"Error in daemon loop iteration: {e}")
            time.sleep(interval)

    logger.info("[✓] Daemon stopped successfully")
