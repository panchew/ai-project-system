"""
Scenario 1: Happy Path E2E Test
Complete workflow: Completion Notice -> Accept Review Decision -> Delivery Notice.
"""

import json
from pathlib import Path
from lib.daemon_extensions import process_artifacts


def test_artifact_happy_path(
    tmp_project,
    make_completion_notice,
    make_review_decision,
    make_delivery_notice
):
    """Test the standard end-to-end multi-artifact flow."""
    # 1. Epic completes work and produces Completion Notice
    cn_file = make_completion_notice(
        project=tmp_project,
        epic_id="P1-M14-E14.1",
        milestone_id="P1-M14",
        phase_id="P1",
        timestamp="2026-06-01T12:00:00Z"
    )
    
    # Verify file is in the right place
    assert cn_file.exists()
    
    # 2. Run daemon artifact routing (simulated one-off run)
    process_artifacts(tmp_project)
    
    # 3. Verify Completion Notice is routed and archived
    assert not cn_file.exists()
    assert (tmp_project / ".ai-project" / "artifacts" / "completion-notices" / ".processed" / cn_file.name).exists()
    
    cn_trigger = tmp_project / ".ai-project" / "queue" / "route_completion_P1-M14-E14.1.json"
    assert cn_trigger.exists()
    with open(cn_trigger, "r", encoding="utf-8") as f:
        cn_data = json.load(f)
        assert cn_data["action"] == "route_artifact"
        assert cn_data["artifact_type"] == "completion_notice"
        assert cn_data["epic_id"] == "P1-M14-E14.1"
        assert cn_data["parent"] == "milestone"
        assert cn_data["parent_ref"] == "P1-M14"

    # 4. Simulate Milestone Chat reviewing and issuing Review Decision (ACCEPT)
    rd_file = make_review_decision(
        project=tmp_project,
        decision="accept",
        epic_id="P1-M14-E14.1",
        milestone_id="P1-M14",
        feedback="All integration tests passed. Excellent work!",
        timestamp="2026-06-01T13:00:00Z",
        cn_timestamp="2026-06-01T12:00:00Z"
    )
    assert rd_file.exists()
    
    # 5. Run daemon routing again
    process_artifacts(tmp_project)
    
    # 6. Verify Review Decision is routed back to Epic and archived
    assert not rd_file.exists()
    assert (tmp_project / ".ai-project" / "artifacts" / "review-decisions" / ".processed" / rd_file.name).exists()
    
    rd_trigger = tmp_project / ".ai-project" / "queue" / "route_review_P1-M14-E14.1.json"
    assert rd_trigger.exists()
    with open(rd_trigger, "r", encoding="utf-8") as f:
        rd_data = json.load(f)
        assert rd_data["action"] == "route_artifact"
        assert rd_data["artifact_type"] == "review_decision"
        assert rd_data["decision"] == "accept"
        assert rd_data["target"] == "epic"
        assert rd_data["target_ref"] == "P1-M14-E14.1"

    # 7. Simulate Epic Agent processing Accept decision, merging PR, and producing Delivery Notice
    dn_file = make_delivery_notice(
        project=tmp_project,
        epic_id="P1-M14-E14.1",
        milestone_id="P1-M14",
        timestamp="2026-06-01T13:15:00Z",
        cn_timestamp="2026-06-01T12:00:00Z",
        rd_timestamp="2026-06-01T13:00:00Z"
    )
    assert dn_file.exists()
    
    # 8. Run daemon routing
    process_artifacts(tmp_project)
    
    # 9. Verify Delivery Notice routed to Milestone and archived
    assert not dn_file.exists()
    assert (tmp_project / ".ai-project" / "artifacts" / "delivery-notices" / ".processed" / dn_file.name).exists()
    
    dn_trigger = tmp_project / ".ai-project" / "queue" / "route_delivery_P1-M14-E14.1.json"
    assert dn_trigger.exists()
    with open(dn_trigger, "r", encoding="utf-8") as f:
        dn_data = json.load(f)
        assert dn_data["action"] == "route_artifact"
        assert dn_data["artifact_type"] == "delivery_notice"
        assert dn_data["epic_id"] == "P1-M14-E14.1"
        assert dn_data["parent"] == "milestone"
        assert dn_data["parent_ref"] == "P1-M14"

    # 10. Verify audit logs
    log_file = tmp_project / ".ai-project" / "logs" / "daemon.log"
    assert log_file.exists()
    log_content = log_file.read_text(encoding="utf-8")
    assert "Routed Completion Notice P1-M14-E14.1 to milestone Chat (P1-M14)" in log_content
    assert "Routed Review Decision (accept) for P1-M14-E14.1 to epic Chat" in log_content
    assert "Routed Delivery Notice for P1-M14-E14.1 to milestone Chat (P1-M14)" in log_content
