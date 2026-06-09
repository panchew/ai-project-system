"""
Scenario 4: Manual Mode Test
Verify that artifacts are copy-paste friendly (safe characters, cleanly structured),
and verify that manual copy-pasting of artifacts works interchangeably with agentic routing.
"""

import string
from lib.artifact_parser import ArtifactParser
from lib.daemon_extensions import process_artifacts


def test_manual_mode(tmp_project, make_completion_notice):
    """Test manual mode copy-paste compatibility and coexistence with agentic mode."""
    
    # 1. Simulate a copy-pasted artifact text from a chat (e.g. Slack/Teams/Discord)
    chat_pasted_text = """---
artifact_type: completion_notice
artifact_version: "1.0"
timestamp: 2026-06-01T12:00:00Z
issuer_chat: Epic Agent (P1-M14-E14.1)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P1-M14-E14.1
milestone_id: P1-M14
phase_id: P1
project_name: ai-project-system
deliverables:
  - name: Integration Tests
    path: tests/integration/test_artifact_happy_path.py
    type: implementation
    status: ready
blockers: []
qa_status: passed
pr_details:
  number: 101
  title: "feat: Add integration tests"
  target_branch: milestone/M144
  url: "https://github.com/example/pull/101"
---

# Completion Notice: P1-M14-E14.1 — Integration Tests for Multi-Artifact Workflows

## Summary
This is a manual copy-paste test artifact. No special characters here!
"""

    # 2. Verify characters in the copy-paste string are human-readable and standard printable text
    # No non-printable characters or weird control characters (except tabs and newlines)
    for index, char in enumerate(chat_pasted_text):
        assert char.isprintable() or char in "\n\r\t", f"Non-printable/unfriendly character at index {index}: {repr(char)}"

    # 3. Verify parser can parse this pasted text block directly (content integrity)
    parser = ArtifactParser()
    artifact = parser.parse_content(chat_pasted_text)
    
    assert artifact.artifact_type == "completion_notice"
    assert artifact.get_epic_id() == "P1-M14-E14.1"
    assert artifact.get_milestone_id() == "P1-M14"
    assert artifact.get_status() == "ready_for_review"
    assert "manual copy-paste test artifact" in artifact.body

    # 4. Coexistence Verification:
    # A human copies a Review Decision from a Chat and manually writes it as a file
    # under review-decisions/ (simulating manually moving the artifact between channels)
    manual_review_text = """---
artifact_type: review_decision
artifact_version: "1.0"
timestamp: 2026-06-01T13:00:00Z
issuer_chat: Milestone Agent (P1-M14)
issuer_role: Milestone Agent
decision: accept
epic_id: P1-M14-E14.1
milestone_id: P1-M14
project_name: ai-project-system
completion_notice_timestamp: 2026-06-01T12:00:00Z
feedback: "Manually pasted and reviewed"
authorization:
  action: merge
  merge_instruction: "Manually merge PR"
---
# Accepted Review
Approved via manual override chat.
"""
    
    # Save manually into the project's artifact directory
    rd_dir = tmp_project / ".ai-project" / "artifacts" / "review-decisions"
    rd_dir.mkdir(parents=True, exist_ok=True)
    manual_rd_file = rd_dir / "manual_paste.md"
    manual_rd_file.write_text(manual_review_text, encoding="utf-8")
    
    # Verify file is detected and processed by the daemon (coexistence of manual and agentic)
    process_artifacts(tmp_project)
    
    # File should be successfully moved to processed
    assert not manual_rd_file.exists()
    processed_file = rd_dir / ".processed" / "manual_paste.md"
    assert processed_file.exists()
    
    # And a trigger file is created for routing to the Epic Chat
    trigger_file = tmp_project / ".ai-project" / "queue" / "route_review_P1-M14-E14.1.json"
    assert trigger_file.exists()
