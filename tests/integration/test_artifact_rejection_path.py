"""
Scenario 2: Rejection and Rework Path E2E Test
Complete workflow: Completion Notice (v1.0) -> Reject Review Decision -> Rework -> Completion Notice (v1.1) -> Accept Review Decision.
"""

import json
from pathlib import Path
from lib.daemon_extensions import process_artifacts
from lib.artifact_parser import ArtifactParser


def test_artifact_rejection_path(
    tmp_project,
    make_completion_notice,
    make_review_decision
):
    """Test the rejection and rework loop in artifact flows."""
    
    # 1. Epic produces initial Completion Notice (v1.0)
    cn_v10_file = make_completion_notice(
        project=tmp_project,
        epic_id="P1-M14-E14.1",
        milestone_id="P1-M14",
        phase_id="P1",
        version="1.0",
        timestamp="2026-06-01T12:00:00Z",
        filename="completion_v1.0.md"
    )
    assert cn_v10_file.exists()
    
    # 2. Daemon processes and routes to Milestone Chat
    process_artifacts(tmp_project)
    
    # Verify cn_v10 archived and trigger created
    assert not cn_v10_file.exists()
    cn_v10_processed = tmp_project / ".ai-project" / "artifacts" / "completion-notices" / ".processed" / "completion_v1.0.md"
    assert cn_v10_processed.exists()
    
    cn_v10_trigger = tmp_project / ".ai-project" / "queue" / "route_completion_P1-M14-E14.1.json"
    assert cn_v10_trigger.exists()
    
    # Clean up the trigger to test the next trigger easily (though router overwrites or appends)
    cn_v10_trigger.unlink()
    
    # 3. Milestone reviews and rejects with specific feedback
    rd_reject_file = make_review_decision(
        project=tmp_project,
        decision="reject",
        epic_id="P1-M14-E14.1",
        milestone_id="P1-M14",
        feedback="Code coverage is only 89%. Please increase it to 95% per specifications.",
        version="1.0",
        timestamp="2026-06-01T13:00:00Z",
        cn_timestamp="2026-06-01T12:00:00Z",
        filename="review_reject.md"
    )
    assert rd_reject_file.exists()
    
    # 4. Daemon processes and routes back to Epic Chat
    process_artifacts(tmp_project)
    
    assert not rd_reject_file.exists()
    rd_reject_processed = tmp_project / ".ai-project" / "artifacts" / "review-decisions" / ".processed" / "review_reject.md"
    assert rd_reject_processed.exists()
    
    rd_reject_trigger = tmp_project / ".ai-project" / "queue" / "route_review_P1-M14-E14.1.json"
    assert rd_reject_trigger.exists()
    with open(rd_reject_trigger, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["decision"] == "reject"
        assert data["target_ref"] == "P1-M14-E14.1"
        
    rd_reject_trigger.unlink()
    
    # 5. Epic Agent performs rework and submits a new Completion Notice (v1.1)
    cn_v11_file = make_completion_notice(
        project=tmp_project,
        epic_id="P1-M14-E14.1",
        milestone_id="P1-M14",
        phase_id="P1",
        version="1.1",
        timestamp="2026-06-01T14:00:00Z",
        filename="completion_v1.1.md"
    )
    assert cn_v11_file.exists()
    
    # 6. Daemon processes and routes back to Milestone Chat
    process_artifacts(tmp_project)
    
    assert not cn_v11_file.exists()
    cn_v11_processed = tmp_project / ".ai-project" / "artifacts" / "completion-notices" / ".processed" / "completion_v1.1.md"
    assert cn_v11_processed.exists()
    
    cn_v11_trigger = tmp_project / ".ai-project" / "queue" / "route_completion_P1-M14-E14.1.json"
    assert cn_v11_trigger.exists()
    cn_v11_trigger.unlink()
    
    # 7. Milestone Agent reviews reworked artifact and accepts
    rd_accept_file = make_review_decision(
        project=tmp_project,
        decision="accept",
        epic_id="P1-M14-E14.1",
        milestone_id="P1-M14",
        feedback="Code coverage is now 98%. Approved!",
        version="1.0",
        timestamp="2026-06-01T15:00:00Z",
        cn_timestamp="2026-06-01T14:00:00Z",
        filename="review_accept.md"
    )
    assert rd_accept_file.exists()
    
    # 8. Daemon processes and routes back to Epic Chat
    process_artifacts(tmp_project)
    
    assert not rd_accept_file.exists()
    rd_accept_processed = tmp_project / ".ai-project" / "artifacts" / "review-decisions" / ".processed" / "review_accept.md"
    assert rd_accept_processed.exists()
    
    rd_accept_trigger = tmp_project / ".ai-project" / "queue" / "route_review_P1-M14-E14.1.json"
    assert rd_accept_trigger.exists()
    with open(rd_accept_trigger, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["decision"] == "accept"
        assert data["target_ref"] == "P1-M14-E14.1"

    # 9. Load the processed files using ArtifactParser to verify index state
    parser = ArtifactParser()
    
    parsed_v10 = parser.parse_file(cn_v10_processed)
    parsed_v11 = parser.parse_file(cn_v11_processed)
    parsed_reject = parser.parse_file(rd_reject_processed)
    parsed_accept = parser.parse_file(rd_accept_processed)
    
    # Verify that we can query the artifacts correctly from indices
    epic_artifacts = parser.get_artifacts_by_epic("P1-M14-E14.1")
    assert len(epic_artifacts) == 4
    
    # They should be sorted newest first (timestamp wise)
    # Timestamps: Accept (15:00), CN v1.1 (14:00), Reject (13:00), CN v1.0 (12:00)
    assert epic_artifacts[0].frontmatter["timestamp"] == "2026-06-01T15:00:00Z"
    assert epic_artifacts[0].artifact_type == "review_decision"
    assert epic_artifacts[1].frontmatter["timestamp"] == "2026-06-01T14:00:00Z"
    assert epic_artifacts[1].artifact_type == "completion_notice"
    assert epic_artifacts[1].frontmatter["artifact_version"] == "1.1"
    assert epic_artifacts[2].frontmatter["timestamp"] == "2026-06-01T13:00:00Z"
    assert epic_artifacts[2].artifact_type == "review_decision"
    assert epic_artifacts[3].frontmatter["timestamp"] == "2026-06-01T12:00:00Z"
    assert epic_artifacts[3].artifact_type == "completion_notice"
    assert epic_artifacts[3].frontmatter["artifact_version"] == "1.0"
    
    # Latest completion notice is v1.1
    latest_cn = parser.get_artifact_by_epic("P1-M14-E14.1", "completion_notice")
    assert latest_cn.frontmatter["artifact_version"] == "1.1"
    
    # Latest review decision is accept
    latest_rd = parser.get_artifact_by_epic("P1-M14-E14.1", "review_decision")
    assert latest_rd.frontmatter["decision"] == "accept"
