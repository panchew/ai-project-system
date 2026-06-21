"""
Scenario 3: Escalation Path E2E Test
Workflow: Epic Completion Notice -> Milestone escalates to Phase -> Phase reviews -> Milestone -> Epic.
"""

import json
from pathlib import Path
from lib.daemon_extensions import process_artifacts


def test_artifact_escalation_path(
    tmp_project,
    make_completion_notice,
    make_review_decision
):
    """Test the escalation path up to Phase Chat and back down."""
    
    # 1. Epic produces Completion Notice
    cn_file = make_completion_notice(
        project=tmp_project,
        epic_id="P1-M14-E14.1",
        milestone_id="P1-M14",
        phase_id="P1",
        timestamp="2026-06-01T12:00:00Z"
    )
    assert cn_file.exists()
    
    # 2. Daemon routes Completion Notice to Milestone Chat
    process_artifacts(tmp_project)
    
    assert not cn_file.exists()
    assert (tmp_project / ".ai-project" / "artifacts" / "completion-notices" / ".processed" / cn_file.name).exists()
    
    cn_trigger = tmp_project / ".ai-project" / "queue" / "route_completion_P1-M14-E14.1.json"
    assert cn_trigger.exists()
    cn_trigger.unlink() # clear trigger for next steps
    
    # 3. Milestone reviews and cannot decide (ambiguous requirement). Escalates to Phase Chat.
    # We do this by issuing a review decision targeting Phase P1
    rd_escalate_file = make_review_decision(
        project=tmp_project,
        decision="reject", # feedback indicates escalation
        phase_id="P1", # Omit epic_id and milestone_id to target phase
        feedback="Requirements for P1-M14-E14.1 are ambiguous. Escalating to Phase Chat for clarification.",
        timestamp="2026-06-01T13:00:00Z",
        cn_timestamp="2026-06-01T12:00:00Z",
        filename="review_escalate_to_phase.md"
    )
    assert rd_escalate_file.exists()
    
    # 4. Daemon routes escalation to Phase Chat
    process_artifacts(tmp_project)
    
    assert not rd_escalate_file.exists()
    assert (tmp_project / ".ai-project" / "artifacts" / "review-decisions" / ".processed" / "review_escalate_to_phase.md").exists()
    
    phase_trigger = tmp_project / ".ai-project" / "queue" / "route_review_P1.json"
    assert phase_trigger.exists()
    with open(phase_trigger, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["target"] == "phase"
        assert data["target_ref"] == "P1"
    phase_trigger.unlink()
    
    # 5. Phase Chat reviews the escalated issue and sends decision back to Milestone Chat
    rd_phase_dec_file = make_review_decision(
        project=tmp_project,
        decision="accept",
        milestone_id="P1-M14", # Target milestone for routing down
        feedback="Phase Board has approved the requirement clarification. Milestone may accept completion.",
        timestamp="2026-06-01T14:00:00Z",
        cn_timestamp="2026-06-01T12:00:00Z",
        filename="review_phase_decision.md"
    )
    assert rd_phase_dec_file.exists()
    
    # 6. Daemon routes Phase decision to Milestone Chat
    process_artifacts(tmp_project)
    
    assert not rd_phase_dec_file.exists()
    assert (tmp_project / ".ai-project" / "artifacts" / "review-decisions" / ".processed" / "review_phase_decision.md").exists()
    
    milestone_trigger = tmp_project / ".ai-project" / "queue" / "route_review_P1-M14.json"
    assert milestone_trigger.exists()
    with open(milestone_trigger, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["target"] == "milestone"
        assert data["target_ref"] == "P1-M14"
    milestone_trigger.unlink()
    
    # 7. Milestone receives Phase approval and issues the final Accept Review Decision to Epic Chat
    rd_final_file = make_review_decision(
        project=tmp_project,
        decision="accept",
        epic_id="P1-M14-E14.1",
        milestone_id="P1-M14",
        feedback="Approved based on Phase Board clarification.",
        timestamp="2026-06-01T15:00:00Z",
        cn_timestamp="2026-06-01T12:00:00Z",
        filename="review_final_accept.md"
    )
    assert rd_final_file.exists()
    
    # 8. Daemon routes final decision to Epic Chat
    process_artifacts(tmp_project)
    
    assert not rd_final_file.exists()
    assert (tmp_project / ".ai-project" / "artifacts" / "review-decisions" / ".processed" / "review_final_accept.md").exists()
    
    epic_trigger = tmp_project / ".ai-project" / "queue" / "route_review_P1-M14-E14.1.json"
    assert epic_trigger.exists()
    with open(epic_trigger, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["target"] == "epic"
        assert data["target_ref"] == "P1-M14-E14.1"
        assert data["decision"] == "accept"
