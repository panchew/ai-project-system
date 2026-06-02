"""
Unit tests for Artifact Routing, File Locking, and Idempotency.

Contains 30+ test cases covering:
- Idempotency Tracker loading, saving, and signature checks
- ArtifactRouter directory initialization
- File locking and write completion waiting
- Routing triggers for Completion Notices, Review Decisions, and Delivery Notices
- Target and parent chat determination logic
- Error handling, invalid formatting, and file moves to .processed/ and .failed/
"""

import json
import logging
import time
import fcntl
import os
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

from lib.artifact_router import ArtifactRouter, IdempotencyTracker
from lib.artifact_parser import Artifact, ArtifactParser
from lib.artifact_errors import ArtifactParseError, ArtifactSchemaError


# -----------------------------------------------------------------------------
# IdempotencyTracker Tests (Test Cases 1-6)
# -----------------------------------------------------------------------------

def test_tracker_get_signature():
    """Test generating artifact signatures."""
    tracker = IdempotencyTracker(Path("dummy_path"))
    
    # 1. Standard completion notice
    art1 = Artifact(
        "completion_notice",
        {"epic_id": "P1-M1-E1.1", "timestamp": "2026-05-29T14:32:00Z"},
        "Body",
    )
    assert tracker.get_signature(art1) == "completion_notice:P1-M1-E1.1:2026-05-29T14:32:00Z"

    # 2. Review decision milestone level
    art2 = Artifact(
        "review_decision",
        {"milestone_id": "P1-M1", "timestamp": "2026-05-29T15:00:00Z"},
        "Body",
    )
    assert tracker.get_signature(art2) == "review_decision:P1-M1:2026-05-29T15:00:00Z"

    # 3. Delivery notice missing timestamp & ids
    art3 = Artifact("delivery_notice", {}, "Body")
    assert tracker.get_signature(art3) == "delivery_notice:unknown:no-timestamp"


def test_tracker_is_and_mark_processed(tmp_path):
    """Test marking artifacts as processed and persists them."""
    track_file = tmp_path / "processed.json"
    tracker = IdempotencyTracker(track_file)
    
    art = Artifact(
        "completion_notice",
        {"epic_id": "P1-M1-E1.1", "timestamp": "2026-05-29T14:32:00Z"},
        "Body",
    )
    
    # 4. Check initial state
    assert not tracker.is_processed(art)
    
    # 5. Mark processed & verify
    tracker.mark_processed(art)
    assert tracker.is_processed(art)
    assert track_file.exists()

    # 6. Re-load tracker and verify persistence
    tracker2 = IdempotencyTracker(track_file)
    assert tracker2.is_processed(art)


# -----------------------------------------------------------------------------
# Directory Setup & General Tests (Test Cases 7-8)
# -----------------------------------------------------------------------------

def test_router_directory_creation(tmp_path):
    """Test that ArtifactRouter correctly creates required directories."""
    # 7. Check directories exist on init
    router = ArtifactRouter(project_root=tmp_path)
    
    assert (tmp_path / ".ai-project" / "queue").exists()
    assert (tmp_path / ".ai-project" / "artifacts" / "completion-notices").exists()
    assert (tmp_path / ".ai-project" / "artifacts" / "completion-notices" / ".processed").exists()
    assert (tmp_path / ".ai-project" / "artifacts" / "completion-notices" / ".failed").exists()
    
    # 8. Tracker file initialized in correct place
    assert router.tracker.tracking_file == tmp_path / ".ai-project" / "processed_artifacts.json"


# -----------------------------------------------------------------------------
# File Locking Tests (Test Cases 9-11)
# -----------------------------------------------------------------------------

def test_wait_for_write_completion_success(tmp_path):
    """Test wait_for_write_completion on a stable, unlocked file."""
    router = ArtifactRouter(project_root=tmp_path)
    file_path = tmp_path / "test.md"
    file_path.write_text("dummy content", encoding="utf-8")
    
    # 9. Verify we can acquire lock
    f = router.wait_for_write_completion(file_path, timeout=0.5)
    assert f is not None
    
    # Try flock to prove we have exclusive lock
    with pytest.raises((IOError, BlockingIOError)):
        f2 = open(file_path, "rb")
        fcntl.flock(f2, fcntl.LOCK_EX | fcntl.LOCK_NB)
        
    f.close()


def test_wait_for_write_completion_locked_timeout(tmp_path):
    """Test wait_for_write_completion times out when file is locked."""
    router = ArtifactRouter(project_root=tmp_path)
    file_path = tmp_path / "test.md"
    file_path.write_text("dummy content", encoding="utf-8")
    
    # Lock the file first
    f_lock = open(file_path, "r+b")
    fcntl.flock(f_lock, fcntl.LOCK_EX)
    
    # 10. Verify router times out trying to acquire lock
    f_router = router.wait_for_write_completion(file_path, timeout=0.2)
    assert f_router is None
    
    f_lock.close()


def test_wait_for_write_completion_nonexistent(tmp_path):
    """Test wait_for_write_completion returns None for missing files."""
    router = ArtifactRouter(project_root=tmp_path)
    # 11. Missing file returns None
    assert router.wait_for_write_completion(tmp_path / "missing.md") is None


# -----------------------------------------------------------------------------
# Completion Notice Routing Tests (Test Cases 12-16)
# -----------------------------------------------------------------------------

def test_route_completion_notice_milestone(tmp_path):
    """Test Completion Notice routes to Milestone chat when milestone_id exists."""
    router = ArtifactRouter(project_root=tmp_path)
    art = Artifact(
        "completion_notice",
        {
            "epic_id": "P1-M1-E1.1",
            "milestone_id": "P1-M1",
            "phase_id": "P1",
            "timestamp": "2026-05-29T14:32:00Z",
        },
        "Body",
    )
    
    # 12. Run routing
    assert router.route_completion_notice(art) is True
    
    # 13. Verify trigger payload
    trigger_file = tmp_path / ".ai-project" / "queue" / "route_completion_P1-M1-E1.1.json"
    assert trigger_file.exists()
    
    with open(trigger_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["action"] == "route_artifact"
        assert data["artifact_type"] == "completion_notice"
        assert data["epic_id"] == "P1-M1-E1.1"
        assert data["parent"] == "milestone"
        assert data["parent_ref"] == "P1-M1"


def test_route_completion_notice_phase(tmp_path):
    """Test Completion Notice routes to Phase chat when phase_id only exists."""
    router = ArtifactRouter(project_root=tmp_path)
    art = Artifact(
        "completion_notice",
        {
            "epic_id": "P1-M1-E1.1",
            "phase_id": "P1",
            "timestamp": "2026-05-29T14:32:00Z",
        },
        "Body",
    )
    
    # 14. Run routing
    assert router.route_completion_notice(art) is True
    
    # Verify trigger payload
    trigger_file = tmp_path / ".ai-project" / "queue" / "route_completion_P1-M1-E1.1.json"
    with open(trigger_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["parent"] == "phase"
        assert data["parent_ref"] == "P1"


def test_route_completion_notice_hq(tmp_path):
    """Test Completion Notice routes to HQ when neither milestone nor phase exists."""
    router = ArtifactRouter(project_root=tmp_path)
    art = Artifact(
        "completion_notice",
        {
            "epic_id": "P1-M1-E1.1",
            "timestamp": "2026-05-29T14:32:00Z",
        },
        "Body",
    )
    
    # 15. Run routing
    assert router.route_completion_notice(art) is True
    
    # Verify trigger payload
    trigger_file = tmp_path / ".ai-project" / "queue" / "route_completion_P1-M1-E1.1.json"
    with open(trigger_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["parent"] == "hq"
        assert data["parent_ref"] == "hq"


def test_route_completion_notice_missing_epic_id(tmp_path):
    """Test routing fails if epic_id is missing."""
    router = ArtifactRouter(project_root=tmp_path)
    art = Artifact("completion_notice", {}, "Body")
    
    # 16. Verify failure
    assert router.route_completion_notice(art) is False


# -----------------------------------------------------------------------------
# Review Decision Routing Tests (Test Cases 17-21)
# -----------------------------------------------------------------------------

def test_route_review_decision_epic(tmp_path):
    """Test Review Decision routes back to Epic Chat when epic_id is present."""
    router = ArtifactRouter(project_root=tmp_path)
    art = Artifact(
        "review_decision",
        {
            "decision": "accept",
            "epic_id": "P1-M1-E1.1",
            "milestone_id": "P1-M1",
            "timestamp": "2026-05-29T15:00:00Z",
        },
        "Body",
    )
    
    # 17. Run routing
    assert router.route_review_decision(art) is True
    
    # 18. Verify trigger payload
    trigger_file = tmp_path / ".ai-project" / "queue" / "route_review_P1-M1-E1.1.json"
    assert trigger_file.exists()
    
    with open(trigger_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["action"] == "route_artifact"
        assert data["artifact_type"] == "review_decision"
        assert data["decision"] == "accept"
        assert data["target"] == "epic"
        assert data["target_ref"] == "P1-M1-E1.1"


def test_route_review_decision_milestone(tmp_path):
    """Test Review Decision routes to Milestone Chat when epic_id missing but milestone_id present."""
    router = ArtifactRouter(project_root=tmp_path)
    art = Artifact(
        "review_decision",
        {
            "decision": "reject",
            "milestone_id": "P1-M1",
            "timestamp": "2026-05-29T15:00:00Z",
        },
        "Body",
    )
    
    # 19. Run routing
    assert router.route_review_decision(art) is True
    
    # Verify trigger payload
    trigger_file = tmp_path / ".ai-project" / "queue" / "route_review_P1-M1.json"
    assert trigger_file.exists()
    
    with open(trigger_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["target"] == "milestone"
        assert data["target_ref"] == "P1-M1"


def test_route_review_decision_phase(tmp_path):
    """Test Review Decision routes to Phase Chat when only phase_id present."""
    router = ArtifactRouter(project_root=tmp_path)
    art = Artifact(
        "review_decision",
        {
            "decision": "accept",
            "phase_id": "P1",
        },
        "Body",
    )
    
    # 20. Run routing
    assert router.route_review_decision(art) is True
    
    # Verify trigger payload
    trigger_file = tmp_path / ".ai-project" / "queue" / "route_review_P1.json"
    with open(trigger_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["target"] == "phase"
        assert data["target_ref"] == "P1"


def test_route_review_decision_hq(tmp_path):
    """Test Review Decision routes to HQ Chat when no ID present."""
    router = ArtifactRouter(project_root=tmp_path)
    art = Artifact(
        "review_decision",
        {
            "decision": "accept",
        },
        "Body",
    )
    
    # 21. Run routing
    assert router.route_review_decision(art) is True
    
    # Verify trigger payload
    trigger_file = tmp_path / ".ai-project" / "queue" / "route_review_hq.json"
    with open(trigger_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["target"] == "hq"
        assert data["target_ref"] == "hq"


# -----------------------------------------------------------------------------
# Delivery Notice Routing Tests (Test Cases 22-25)
# -----------------------------------------------------------------------------

def test_route_delivery_notice_milestone(tmp_path):
    """Test Delivery Notice routes to parent Milestone Chat when milestone_id present."""
    router = ArtifactRouter(project_root=tmp_path)
    art = Artifact(
        "delivery_notice",
        {
            "epic_id": "P1-M1-E1.1",
            "milestone_id": "P1-M1",
            "timestamp": "2026-05-29T16:00:00Z",
        },
        "Body",
    )
    
    # 22. Run routing
    assert router.route_delivery_notice(art) is True
    
    # 23. Verify trigger payload
    trigger_file = tmp_path / ".ai-project" / "queue" / "route_delivery_P1-M1-E1.1.json"
    assert trigger_file.exists()
    
    with open(trigger_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["action"] == "route_artifact"
        assert data["artifact_type"] == "delivery_notice"
        assert data["epic_id"] == "P1-M1-E1.1"
        assert data["parent"] == "milestone"
        assert data["parent_ref"] == "P1-M1"


def test_route_delivery_notice_phase(tmp_path):
    """Test Delivery Notice routes to Phase when only phase_id present."""
    router = ArtifactRouter(project_root=tmp_path)
    art = Artifact(
        "delivery_notice",
        {
            "phase_id": "P1",
        },
        "Body",
    )
    
    # 24. Run routing
    assert router.route_delivery_notice(art) is True
    
    # Verify trigger payload
    trigger_file = tmp_path / ".ai-project" / "queue" / "route_delivery_P1.json"
    with open(trigger_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["parent"] == "phase"
        assert data["parent_ref"] == "P1"


def test_route_delivery_notice_hq(tmp_path):
    """Test Delivery Notice routes to HQ when no other IDs are present."""
    router = ArtifactRouter(project_root=tmp_path)
    art = Artifact(
        "delivery_notice",
        {},
        "Body",
    )
    
    # 25. Run routing
    assert router.route_delivery_notice(art) is True
    
    # Verify trigger payload
    trigger_file = tmp_path / ".ai-project" / "queue" / "route_delivery_hq.json"
    with open(trigger_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["parent"] == "hq"
        assert data["parent_ref"] == "hq"


# -----------------------------------------------------------------------------
# Process File & Workflow Tests (Test Cases 26-35)
# -----------------------------------------------------------------------------

def test_process_file_success_completion(tmp_path):
    """Test successful end-to-end processing of a valid Completion Notice."""
    router = ArtifactRouter(project_root=tmp_path)
    
    content = """---
artifact_type: completion_notice
artifact_version: "1.0"
timestamp: 2026-05-29T14:32:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: test-project
deliverables:
  - name: Test
    path: test.py
    type: implementation
    status: ready
blockers: []
qa_status: passed
pr_details:
  number: 1
  title: "feat: Test"
  target_branch: milestone/M1
  url: "https://github.com/example/project/pull/1"
---

# Body Content
"""
    file_path = tmp_path / ".ai-project" / "artifacts" / "completion-notices" / "completion.md"
    file_path.write_text(content, encoding="utf-8")
    
    # 26. Process file
    res = router.process_file(file_path)
    assert res is True
    
    # 27. Verify trigger created
    trigger_file = tmp_path / ".ai-project" / "queue" / "route_completion_P1-M1-E1.1.json"
    assert trigger_file.exists()
    
    # 28. Verify file moved to .processed
    assert not file_path.exists()
    assert (tmp_path / ".ai-project" / "artifacts" / "completion-notices" / ".processed" / "completion.md").exists()
    
    # 29. Verify marked processed in tracker
    sig = "completion_notice:P1-M1-E1.1:2026-05-29T14:32:00Z"
    assert sig in router.tracker.processed_signatures


def test_process_file_idempotency(tmp_path):
    """Test that processing an already processed file skips routing and just archives."""
    router = ArtifactRouter(project_root=tmp_path)
    
    # Pre-mark as processed
    art = Artifact(
        "completion_notice",
        {"epic_id": "P1-M1-E1.1", "timestamp": "2026-05-29T14:32:00Z"},
        "Body",
    )
    router.tracker.mark_processed(art)
    
    # File content to process
    content = """---
artifact_type: completion_notice
artifact_version: "1.0"
timestamp: 2026-05-29T14:32:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: test-project
deliverables:
  - name: Test
    path: test.py
    type: implementation
    status: ready
blockers: []
qa_status: passed
pr_details:
  number: 1
  title: "feat: Test"
  target_branch: milestone/M1
  url: "https://github.com/example/project/pull/1"
---
"""
    file_path = tmp_path / ".ai-project" / "artifacts" / "completion-notices" / "completion.md"
    file_path.write_text(content, encoding="utf-8")
    
    # 30. Process file (should skip trigger creation since it's already processed)
    res = router.process_file(file_path)
    assert res is True
    
    # 31. Verify no trigger created
    trigger_file = tmp_path / ".ai-project" / "queue" / "route_completion_P1-M1-E1.1.json"
    assert not trigger_file.exists()
    
    # 32. Verify file still archived to .processed/
    assert not file_path.exists()
    assert (tmp_path / ".ai-project" / "artifacts" / "completion-notices" / ".processed" / "completion.md").exists()


def test_process_file_parse_error(tmp_path):
    """Test malformed markdown frontmatter moves to .failed/."""
    router = ArtifactRouter(project_root=tmp_path)
    
    bad_content = """---
artifact_type: completion_notice
malformed_yaml: [this, is, bad: yes
---
"""
    file_path = tmp_path / ".ai-project" / "artifacts" / "completion-notices" / "bad.md"
    file_path.write_text(bad_content, encoding="utf-8")
    
    # 33. Process file (should fail)
    res = router.process_file(file_path)
    assert res is False
    
    # 34. Verify file moved to .failed/
    assert not file_path.exists()
    assert (tmp_path / ".ai-project" / "artifacts" / "completion-notices" / ".failed" / "bad.md").exists()


def test_process_file_validation_error(tmp_path):
    """Test schema invalid frontmatter moves to .failed/."""
    router = ArtifactRouter(project_root=tmp_path)
    
    # Missing required deliverables field
    bad_content = """---
artifact_type: completion_notice
artifact_version: "1.0"
timestamp: 2026-05-29T14:32:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: test-project
qa_status: passed
pr_details:
  number: 1
  title: "feat: Test"
  target_branch: milestone/M1
  url: "https://github.com/example/project/pull/1"
---
"""
    file_path = tmp_path / ".ai-project" / "artifacts" / "completion-notices" / "bad_schema.md"
    file_path.write_text(bad_content, encoding="utf-8")
    
    # 35. Process file (should fail validation)
    res = router.process_file(file_path)
    assert res is False
    
    # Verify file moved to .failed/
    assert not file_path.exists()
    assert (tmp_path / ".ai-project" / "artifacts" / "completion-notices" / ".failed" / "bad_schema.md").exists()


# -----------------------------------------------------------------------------
# Extra Coverage Tests (Test Cases 36-45)
# -----------------------------------------------------------------------------

def test_tracker_load_save_failures(tmp_path):
    """Test IdempotencyTracker handling corrupt files or save failures."""
    track_file = tmp_path / "corrupt_processed.json"
    track_file.write_text("{invalid json", encoding="utf-8")
    
    # Tracker should handle corrupt file gracefully and start fresh
    tracker = IdempotencyTracker(track_file)
    assert len(tracker.processed_signatures) == 0
    
    # Save failure should not raise exception (e.g. if target directory is a file)
    bad_dir_file = tmp_path / "bad_dir"
    bad_dir_file.touch()
    tracker_fail = IdempotencyTracker(bad_dir_file / "tracker.json")
    art = Artifact("completion_notice", {"epic_id": "P1-M1-E1.1"}, "Body")
    tracker_fail.mark_processed(art)  # Should fail save internally but not crash


def test_wait_for_write_completion_stat_failure(tmp_path):
    """Test wait_for_write_completion handles stat or permission issues gracefully."""
    router = ArtifactRouter(project_root=tmp_path)
    file_path = tmp_path / "protected.md"
    file_path.write_text("protected content", encoding="utf-8")
    
    # Mock stat to raise OSError
    with patch.object(Path, "stat", side_effect=OSError("Permission Denied")):
        # Should wait and still try to lock
        f = router.wait_for_write_completion(file_path, timeout=0.1)
        if f:
            f.close()


def test_wait_for_write_completion_open_failures(tmp_path):
    """Test wait_for_write_completion handles lock failures and read fallbacks."""
    router = ArtifactRouter(project_root=tmp_path)
    file_path = tmp_path / "fail_open.md"
    file_path.write_text("content", encoding="utf-8")
    
    # Mock open to raise PermissionError on r+b, but succeed on rb
    original_open = open
    def mock_open(path, mode="r", *args, **kwargs):
        if mode == "r+b":
            raise PermissionError("Access denied")
        return original_open(path, mode, *args, **kwargs)
        
    with patch("builtins.open", side_effect=mock_open):
        f = router.wait_for_write_completion(file_path, timeout=0.2)
        assert f is not None
        f.close()


def test_process_file_skip_processed_or_failed_path(tmp_path):
    """Test process_file immediately ignores files in .processed or .failed paths."""
    router = ArtifactRouter(project_root=tmp_path)
    proc_path = tmp_path / ".ai-project" / "artifacts" / "completion-notices" / ".processed" / "skip.md"
    proc_path.parent.mkdir(parents=True, exist_ok=True)
    proc_path.write_text("content", encoding="utf-8")
    
    assert router.process_file(proc_path) is False


def test_process_file_general_exception(tmp_path):
    """Test general exceptions during file reading are handled gracefully."""
    router = ArtifactRouter(project_root=tmp_path)
    file_path = tmp_path / ".ai-project" / "artifacts" / "completion-notices" / "err.md"
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text("content", encoding="utf-8")
    
    # Mock wait_for_write_completion to raise exception
    with patch.object(router, "wait_for_write_completion", side_effect=RuntimeError("Generic IO Error")):
        res = router.process_file(file_path)
        assert res is False
        assert (tmp_path / ".ai-project" / "artifacts" / "completion-notices" / ".failed" / "err.md").exists()


def test_routing_trigger_write_failures(tmp_path):
    """Test route methods handle write or permission failures gracefully."""
    router = ArtifactRouter(project_root=tmp_path)
    art = Artifact("completion_notice", {"epic_id": "P1-M1-E1.1", "timestamp": "123"}, "Body")
    
    # Mock open inside route_completion_notice to fail
    with patch("builtins.open", side_effect=IOError("Write blocked")):
        assert router.route_completion_notice(art) is False
        assert router.route_review_decision(art) is False
        assert router.route_delivery_notice(art) is False


def test_archive_file_failure(tmp_path):
    """Test archive_file handles rename or destination write failures gracefully."""
    router = ArtifactRouter(project_root=tmp_path)
    file_path = tmp_path / "test_arch.md"
    file_path.write_text("content", encoding="utf-8")
    
    # Mock rename to raise OSError
    with patch.object(Path, "rename", side_effect=OSError("Disk full")):
        router.archive_file(file_path, success=True)
        # Should log and survive without crashing


class StopLoopException(BaseException):
    """Custom BaseException to break infinite loops during testing."""
    pass


def test_daemon_extensions_error_branches(tmp_path):
    """Test uncovered error branches in process_artifacts and daemon loop."""
    from lib.daemon_extensions import process_artifacts, daemon_artifact_monitoring_loop
    
    # Initialize a router to ensure directories exist
    router = ArtifactRouter(project_root=tmp_path)
    directory = router.artifact_dirs["completion_notice"]
    
    # Create sub-directory representing processed
    proc_dir = directory / ".processed"
    proc_dir.mkdir(parents=True, exist_ok=True)
    sub_file = proc_dir / "skip_me.md"
    sub_file.write_text("content", encoding="utf-8")
    
    # Create a directory named like a file to hit is_dir() check
    dir_as_file = directory / "is_a_directory.md"
    dir_as_file.mkdir(parents=True, exist_ok=True)
    
    # Create a file that raises error on processing
    bad_file = directory / "fail_proc.md"
    bad_file.write_text("invalid content", encoding="utf-8")
    
    # Mock Path.exists to return False specifically for delivery-notices to cover directory.exists() == False
    original_exists = Path.exists
    def mock_path_exists(self_path):
        if self_path.name == "delivery-notices":
            return False
        return original_exists(self_path)
        
    with patch.object(Path, "exists", side_effect=mock_path_exists, autospec=True):
        # Run process_artifacts (should handle bad_file move to failed, skip dir and sub-file)
        process_artifacts(tmp_path)
        
        # Test missing directories inside daemon_artifact_monitoring_loop
        # Since we can't easily exit an infinite loop without signals or exceptions,
        # we raise StopLoopException to exit loop cleanly.
        with patch("time.sleep", side_effect=StopLoopException):
            try:
                daemon_artifact_monitoring_loop(tmp_path, interval=0.1)
            except StopLoopException:
                pass # Break loop and exit cleanly
    
    assert (directory / ".failed" / "fail_proc.md").exists()
    assert not (directory / ".processed" / "is_a_directory.md").exists()

    # 3. Test unexpected errors in process_artifacts loop
    with patch("lib.artifact_router.ArtifactRouter.process_file", side_effect=ValueError("Unexpected processing crash")):
        bad_file = directory / "fail_proc_2.md"
        bad_file.write_text("invalid content 2", encoding="utf-8")
        process_artifacts(tmp_path) # Should log exception and continue without crashing

    # 4. Test signal handling and general Exception block inside daemon loop
    from lib.daemon_extensions import setup_daemon_logger
    import signal
    logger = setup_daemon_logger(tmp_path)
    
    # We can mock signal function to capture handle_signal
    captured_handler = None
    def mock_signal(sig, handler):
        nonlocal captured_handler
        captured_handler = handler
        
    call_count = 0
    def mock_ensure_dirs():
        nonlocal call_count
        call_count += 1
        if call_count > 1:
            raise RuntimeError("Ensure dir failed")
            
    with patch("lib.daemon_extensions.signal.signal", side_effect=mock_signal):
        # We start loop but raise exception on first check to verify Exception catching & time.sleep call
        with patch("lib.artifact_router.ArtifactRouter.ensure_directories", side_effect=mock_ensure_dirs):
            # Mock sleep to raise StopLoopException to exit loop immediately on sleep
            with patch("time.sleep", side_effect=StopLoopException) as mock_sleep:
                try:
                    daemon_artifact_monitoring_loop(tmp_path, interval=0.1)
                except StopLoopException:
                    pass
                assert mock_sleep.call_count >= 1 # ensured it hit sleep after exception
                
        # Manually invoke captured signal handler to cover signal lines
        if captured_handler:
            captured_handler(signal.SIGTERM, None)


        # Should break loop and exit cleanly

