"""
Scenario 7: Parallel Execution Test
Concurrently write 15+ artifacts (5 Completion Notices, 5 Review Decisions, 5 Delivery Notices)
representing 5 concurrent Epics under the same milestone to ensure zero race conditions or lost artifacts.
"""

import json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from lib.daemon_extensions import process_artifacts


def test_parallel_artifacts(
    tmp_project,
    make_completion_notice,
    make_review_decision,
    make_delivery_notice
):
    """Test processing of 15+ artifacts for 5 concurrent Epics completing simultaneously."""
    epics = [f"P1-M14-E14.{i}" for i in range(1, 6)]
    
    # ------------------ STEP 1: CONCURRENT COMPLETION NOTICES ------------------
    # Write 5 Completion Notices simultaneously (simulating 5 Epics finishing within 100ms)
    def write_cn(epic_id):
        return make_completion_notice(
            project=tmp_project,
            epic_id=epic_id,
            milestone_id="P1-M14",
            phase_id="P1",
            timestamp=f"2026-06-01T12:00:0{epics.index(epic_id)}Z",
            filename=f"cn_{epic_id}.md"
        )

    with ThreadPoolExecutor(max_workers=5) as writer_executor:
        cn_futures = [writer_executor.submit(write_cn, epic) for epic in epics]
        cn_files = [f.result() for f in as_completed(cn_futures)]

    # A single daemon process runs to handle all incoming files
    process_artifacts(tmp_project)

    # Verify all 5 Completion Notices processed successfully
    for cn_file in cn_files:
        assert not cn_file.exists(), f"{cn_file.name} was not processed"
        processed_file = tmp_project / ".ai-project" / "artifacts" / "completion-notices" / ".processed" / cn_file.name
        assert processed_file.exists(), f"{cn_file.name} was not moved to .processed"

    # Verify 5 routing triggers created in queue
    queue_dir = tmp_project / ".ai-project" / "queue"
    for epic in epics:
        trigger_file = queue_dir / f"route_completion_{epic}.json"
        assert trigger_file.exists(), f"Trigger missing for completion of {epic}"
        with open(trigger_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            assert data["epic_id"] == epic
            assert data["parent_ref"] == "P1-M14"
        trigger_file.unlink() # Clean up

    # ------------------ STEP 2: CONCURRENT REVIEW DECISIONS ------------------
    # Write 5 Review Decisions simultaneously
    def write_rd(epic_id):
        return make_review_decision(
            project=tmp_project,
            decision="accept",
            epic_id=epic_id,
            milestone_id="P1-M14",
            feedback=f"Parallel accept for {epic_id}",
            timestamp=f"2026-06-01T13:00:0{epics.index(epic_id)}Z",
            cn_timestamp=f"2026-06-01T12:00:0{epics.index(epic_id)}Z",
            filename=f"rd_{epic_id}.md"
        )

    with ThreadPoolExecutor(max_workers=5) as writer_executor:
        rd_futures = [writer_executor.submit(write_rd, epic) for epic in epics]
        rd_files = [f.result() for f in as_completed(rd_futures)]

    # Daemon processes all 5 Review Decisions
    process_artifacts(tmp_project)

    # Verify all 5 Review Decisions processed successfully
    for rd_file in rd_files:
        assert not rd_file.exists(), f"{rd_file.name} was not processed"
        processed_file = tmp_project / ".ai-project" / "artifacts" / "review-decisions" / ".processed" / rd_file.name
        assert processed_file.exists(), f"{rd_file.name} was not moved to .processed"

    # Verify 5 review triggers created in queue
    for epic in epics:
        trigger_file = queue_dir / f"route_review_{epic}.json"
        assert trigger_file.exists(), f"Trigger missing for review of {epic}"
        with open(trigger_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            assert data["target_ref"] == epic
            assert data["decision"] == "accept"
        trigger_file.unlink() # Clean up

    # ------------------ STEP 3: CONCURRENT DELIVERY NOTICES ------------------
    # Write 5 Delivery Notices simultaneously
    def write_dn(epic_id):
        return make_delivery_notice(
            project=tmp_project,
            epic_id=epic_id,
            milestone_id="P1-M14",
            timestamp=f"2026-06-01T13:15:0{epics.index(epic_id)}Z",
            cn_timestamp=f"2026-06-01T12:00:0{epics.index(epic_id)}Z",
            rd_timestamp=f"2026-06-01T13:00:0{epics.index(epic_id)}Z",
            filename=f"dn_{epic_id}.md"
        )

    with ThreadPoolExecutor(max_workers=5) as writer_executor:
        dn_futures = [writer_executor.submit(write_dn, epic) for epic in epics]
        dn_files = [f.result() for f in as_completed(dn_futures)]

    # Daemon processes all 5 Delivery Notices
    process_artifacts(tmp_project)

    # Verify all 5 Delivery Notices processed successfully
    for dn_file in dn_files:
        assert not dn_file.exists(), f"{dn_file.name} was not processed"
        processed_file = tmp_project / ".ai-project" / "artifacts" / "delivery-notices" / ".processed" / dn_file.name
        assert processed_file.exists(), f"{dn_file.name} was not moved to .processed"

    # Verify 5 delivery triggers created in queue
    for epic in epics:
        trigger_file = queue_dir / f"route_delivery_{epic}.json"
        assert trigger_file.exists(), f"Trigger missing for delivery of {epic}"
        with open(trigger_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            assert data["epic_id"] == epic
            assert data["parent_ref"] == "P1-M14"
