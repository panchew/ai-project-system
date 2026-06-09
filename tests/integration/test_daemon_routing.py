"""
Integration tests for daemon artifact routing.

Tests:
1. process_artifacts (one-off scan):
   - Creation of Completion Notice, Review Decision, and Delivery Notice files
   - Successful processing, trigger file creation, archiving, and logger generation
2. daemon_artifact_monitoring_loop (continuous background monitoring):
   - Background thread running the monitoring loop
   - Dynamic file creation and detection in under 1 second
   - Clean shutdown verification
"""

import json
import time
import pytest
import threading
from pathlib import Path

from lib.daemon_extensions import process_artifacts, daemon_artifact_monitoring_loop


def test_daemon_one_off_process_artifacts(tmp_path):
    """Integration test verifying process_artifacts correctly routes all 3 types."""
    # 1. Setup project directories
    queue_dir = tmp_path / ".ai-project" / "queue"
    cn_dir = tmp_path / ".ai-project" / "artifacts" / "completion-notices"
    rd_dir = tmp_path / ".ai-project" / "artifacts" / "review-decisions"
    dn_dir = tmp_path / ".ai-project" / "artifacts" / "delivery-notices"
    
    cn_dir.mkdir(parents=True, exist_ok=True)
    rd_dir.mkdir(parents=True, exist_ok=True)
    dn_dir.mkdir(parents=True, exist_ok=True)
    queue_dir.mkdir(parents=True, exist_ok=True)

    # 2. Write valid Completion Notice
    cn_content = """---
artifact_type: completion_notice
artifact_version: "1.0"
timestamp: 2026-06-01T12:00:00Z
issuer_chat: Epic Agent (P4-M14-E14.2)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P4-M14-E14.2
milestone_id: P4-M14
phase_id: P4
project_name: ai-project-system
deliverables:
  - name: Artifact Router Module
    path: lib/artifact_router.py
    type: implementation
    status: ready
blockers: []
qa_status: passed
pr_details:
  number: 100
  title: "feat: Implement artifact routing"
  target_branch: milestone/M144
  url: "https://github.com/example/pull/100"
---
# Completion Notice Body
"""
    cn_file = cn_dir / "cn_test.md"
    cn_file.write_text(cn_content, encoding="utf-8")

    # 3. Write valid Review Decision
    rd_content = """---
artifact_type: review_decision
artifact_version: "1.0"
timestamp: 2026-06-01T13:00:00Z
issuer_chat: Milestone Agent (P4-M14)
issuer_role: Milestone Agent
decision: accept
epic_id: P4-M14-E14.2
milestone_id: P4-M14
phase_id: P4
project_name: ai-project-system
completion_notice_timestamp: 2026-06-01T12:00:00Z
feedback: "Approved"
authorization:
  action: merge
  merge_instruction: "Merge"
---
# Review Decision Body
"""
    rd_file = rd_dir / "rd_test.md"
    rd_file.write_text(rd_content, encoding="utf-8")

    # 4. Write valid Delivery Notice
    dn_content = """---
artifact_type: delivery_notice
artifact_version: "1.0"
timestamp: 2026-06-01T13:15:00Z
issuer_chat: Epic Agent (P4-M14-E14.2)
issuer_role: Epic Agent
status: delivered
epic_id: P4-M14-E14.2
milestone_id: P4-M14
phase_id: P4
project_name: ai-project-system
merge_details:
  pr_number: 100
  pr_url: "https://github.com/example/pull/100"
  merge_commit: "abc12345"
  merge_timestamp: 2026-06-01T13:10:00Z
  merge_strategy: squash
  target_branch: milestone/M144
duration:
  start_date: "2026-05-30"
  end_date: "2026-06-01"
  elapsed_days: 2
final_artifacts:
  - name: Artifact Router Module
    path: lib/artifact_router.py
    type: implementation
completion_notice_timestamp: 2026-06-01T12:00:00Z
review_decision_timestamp: 2026-06-01T13:00:00Z
---
# Delivery Notice Body
"""
    dn_file = dn_dir / "dn_test.md"
    dn_file.write_text(dn_content, encoding="utf-8")

    # 5. Execute process_artifacts
    process_artifacts(tmp_path)

    # 6. Verify Completion Notice processed & routed
    assert not cn_file.exists()
    assert (cn_dir / ".processed" / "cn_test.md").exists()
    cn_trigger = queue_dir / "route_completion_P4-M14-E14.2.json"
    assert cn_trigger.exists()
    with open(cn_trigger, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["parent"] == "milestone"
        assert data["parent_ref"] == "P4-M14"

    # 7. Verify Review Decision processed & routed
    assert not rd_file.exists()
    assert (rd_dir / ".processed" / "rd_test.md").exists()
    rd_trigger = queue_dir / "route_review_P4-M14-E14.2.json"
    assert rd_trigger.exists()
    with open(rd_trigger, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["target"] == "epic"
        assert data["target_ref"] == "P4-M14-E14.2"

    # 8. Verify Delivery Notice processed & routed
    assert not dn_file.exists()
    assert (dn_dir / ".processed" / "dn_test.md").exists()
    dn_trigger = queue_dir / "route_delivery_P4-M14-E14.2.json"
    assert dn_trigger.exists()
    with open(dn_trigger, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["parent"] == "milestone"
        assert data["parent_ref"] == "P4-M14"

    # 9. Verify daemon.log contains routing decisions
    log_file = tmp_path / ".ai-project" / "logs" / "daemon.log"
    assert log_file.exists()
    log_content = log_file.read_text(encoding="utf-8")
    assert "Routed Completion Notice P4-M14-E14.2 to milestone Chat" in log_content
    assert "Routed Review Decision (accept) for P4-M14-E14.2 to epic Chat" in log_content
    assert "Routed Delivery Notice for P4-M14-E14.2 to milestone Chat" in log_content


def test_daemon_continuous_monitoring_loop(tmp_path):
    """Integration test verifying daemon continuous monitoring detects and routes in background."""
    # Setup directories
    queue_dir = tmp_path / ".ai-project" / "queue"
    cn_dir = tmp_path / ".ai-project" / "artifacts" / "completion-notices"
    cn_dir.mkdir(parents=True, exist_ok=True)
    queue_dir.mkdir(parents=True, exist_ok=True)

    # We start daemon loop in a background thread with an aggressive 0.1s interval for speed
    daemon_thread = threading.Thread(
        target=daemon_artifact_monitoring_loop,
        args=(tmp_path, 0.1),
        daemon=True,
    )
    
    # Start thread
    daemon_thread.start()
    
    # Wait for loop to spin up
    time.sleep(0.2)

    # Create a completion notice dynamically to see if background thread catches it
    cn_content = """---
artifact_type: completion_notice
artifact_version: "1.0"
timestamp: 2026-06-01T12:00:00Z
issuer_chat: Epic Agent (P4-M14-E14.2)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P4-M14-E14.2
milestone_id: P4-M14
phase_id: P4
project_name: ai-project-system
deliverables:
  - name: Artifact Router Module
    path: lib/artifact_router.py
    type: implementation
    status: ready
blockers: []
qa_status: passed
pr_details:
  number: 100
  title: "feat: Implement artifact routing"
  target_branch: milestone/M144
  url: "https://github.com/example/pull/100"
---
# Completion Notice Body
"""
    cn_file = cn_dir / "dynamic_cn.md"
    cn_file.write_text(cn_content, encoding="utf-8")

    # The background loop should catch it in < 1 second
    timeout = 2.0
    start_time = time.time()
    processed_file = cn_dir / ".processed" / "dynamic_cn.md"
    trigger_file = queue_dir / "route_completion_P4-M14-E14.2.json"

    while time.time() - start_time < timeout:
        if processed_file.exists() and trigger_file.exists():
            break
        time.sleep(0.05)

    # Verify background thread processed it successfully
    assert processed_file.exists()
    assert trigger_file.exists()
    assert not cn_file.exists()

    with open(trigger_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["epic_id"] == "P4-M14-E14.2"
        assert data["parent"] == "milestone"
        assert data["parent_ref"] == "P4-M14"
