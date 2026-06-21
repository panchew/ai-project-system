"""
Scenario 6: Error Scenario Tests
Verify that malformed YAML, missing fields, invalid reference formats,
and lock timeout issues are handled gracefully without losing or incorrectly processing files.
"""

import fcntl
import time
import pytest
from pathlib import Path
from lib.daemon_extensions import process_artifacts


def test_corrupted_yaml_moved_to_failed(tmp_project):
    """Verify that an artifact with malformed/corrupted YAML is moved to .failed/."""
    cn_dir = tmp_project / ".ai-project" / "artifacts" / "completion-notices"
    cn_dir.mkdir(parents=True, exist_ok=True)
    
    # Write file with malformed YAML delimiters/keys
    corrupt_file = cn_dir / "corrupted.md"
    corrupt_file.write_text("""---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: 2026-06-01T12:00:00Z
issuer_chat: Epic Agent (P1-M14-E14.1)
*invalid_yaml_here*
---
Malformed YAML body
""", encoding="utf-8")
    
    # Process
    process_artifacts(tmp_project)
    
    # Verify file is moved to .failed/
    assert not corrupt_file.exists()
    failed_file = cn_dir / ".failed" / "corrupted.md"
    assert failed_file.exists()
    
    # Verify no routing triggers are created in the queue
    queue_dir = tmp_project / ".ai-project" / "queue"
    assert not list(queue_dir.glob("*"))


def test_missing_fields_moved_to_failed(tmp_project):
    """Verify that an artifact with missing required fields is moved to .failed/."""
    cn_dir = tmp_project / ".ai-project" / "artifacts" / "completion-notices"
    cn_dir.mkdir(parents=True, exist_ok=True)
    
    # Write file missing required 'issuer_role' and 'deliverables'
    missing_fields_file = cn_dir / "missing_fields.md"
    missing_fields_file.write_text("""---
artifact_type: completion_notice
artifact_version: "1.0"
timestamp: 2026-06-01T12:00:00Z
issuer_chat: Epic Agent (P1-M14-E14.1)
status: ready_for_review
epic_id: P1-M14-E14.1
milestone_id: P1-M14
phase_id: P1
project_name: ai-project-system
qa_status: passed
pr_details:
  number: 101
  title: "Missing fields"
  target_branch: milestone/M144
  url: "https://github.com/example/pull/101"
---
Missing required field (issuer_role, deliverables) body
""", encoding="utf-8")
    
    # Process
    process_artifacts(tmp_project)
    
    # Verify file is moved to .failed/
    assert not missing_fields_file.exists()
    failed_file = cn_dir / ".failed" / "missing_fields.md"
    assert failed_file.exists()


def test_invalid_reference_format_moved_to_failed(tmp_project):
    """Verify that an artifact with an invalid epic_id format is moved to .failed/."""
    cn_dir = tmp_project / ".ai-project" / "artifacts" / "completion-notices"
    cn_dir.mkdir(parents=True, exist_ok=True)
    
    # Write file with invalid reference epic_id format "E14-1" instead of "P1-M14-E14.1"
    invalid_ref_file = cn_dir / "invalid_ref.md"
    invalid_ref_file.write_text("""---
artifact_type: completion_notice
artifact_version: "1.0"
timestamp: 2026-06-01T12:00:00Z
issuer_chat: Epic Agent (E14.1)
issuer_role: Epic Agent
status: ready_for_review
epic_id: "E14-1"
milestone_id: P1-M14
phase_id: P1
project_name: ai-project-system
deliverables:
  - name: Integration Tests
    path: tests/integration/test_artifact_happy_path.py
    type: implementation
    status: ready
qa_status: passed
pr_details:
  number: 101
  title: "Invalid Ref"
  target_branch: milestone/M144
  url: "https://github.com/example/pull/101"
---
Invalid reference format body
""", encoding="utf-8")
    
    # Process
    process_artifacts(tmp_project)
    
    # Verify file is moved to .failed/
    assert not invalid_ref_file.exists()
    failed_file = cn_dir / ".failed" / "invalid_ref.md"
    assert failed_file.exists()


def test_router_lock_timeout_handling(tmp_project, make_completion_notice):
    """Verify that if a file is exclusively locked by another process, router times out and leaves the file alone."""
    cn_file = make_completion_notice(
        project=tmp_project,
        epic_id="P1-M14-E14.3",
        milestone_id="P1-M14",
        phase_id="P1",
        timestamp="2026-06-01T12:00:00Z"
    )
    assert cn_file.exists()
    
    # Acquire an exclusive flock on this file inside the test process
    with open(cn_file, "r+b") as lock_f:
        fcntl.flock(lock_f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        
        # Now run process_artifacts in the same process
        # Since wait_for_write_completion has a lock timeout of 2.0s, let's process
        # to verify it gracefully handles/logs timeout and returns False (no archiving).
        # To make the test run fast, we don't want to wait 2 seconds. But wait!
        # wait_for_write_completion's timeout is fixed to 2.0s in code.
        # 2 seconds is very fast anyway, so let's run it.
        process_artifacts(tmp_project)
        
        # Verify the file remains in the original directory (was not moved to .processed/ or .failed/)
        assert cn_file.exists()
        assert not (tmp_project / ".ai-project" / "artifacts" / "completion-notices" / ".processed" / cn_file.name).exists()
        assert not (tmp_project / ".ai-project" / "artifacts" / "completion-notices" / ".failed" / cn_file.name).exists()
        
        # Release the lock
        fcntl.flock(lock_f, fcntl.LOCK_UN)
        
    # Once the lock is released, processing should successfully run and process the file!
    process_artifacts(tmp_project)
    assert not cn_file.exists()
    assert (tmp_project / ".ai-project" / "artifacts" / "completion-notices" / ".processed" / cn_file.name).exists()
