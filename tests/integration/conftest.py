import pytest
from pathlib import Path
import yaml
import re
import logging
from typing import Dict, Any, Optional, List
from lib.artifact_router import ArtifactRouter

@pytest.fixture(autouse=True)
def clean_loggers():
    """Clear handlers on global loggers to prevent state leakage between tests."""
    for name in ["ai_project_daemon", "ai_project_daemon.router"]:
        logger = logging.getLogger(name)
        for handler in list(logger.handlers):
            try:
                handler.close()
            except Exception:
                pass
            logger.removeHandler(handler)

@pytest.fixture
def tmp_project(tmp_path):
    """Create a temporary test project structure and return its Path."""
    project_dir = tmp_path / "test_project"
    project_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize the router to ensure all standard folders are created
    router = ArtifactRouter(project_root=project_dir)
    router.ensure_directories()
    
    return project_dir

def dict_to_frontmatter_markdown(frontmatter: Dict[str, Any], body: str) -> str:
    """Format dictionary to YAML frontmatter and append body."""
    yaml_str = yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)
    return f"---\n{yaml_str}---\n{body}"

@pytest.fixture
def make_completion_notice():
    """Returns a helper function to create a valid completion notice."""
    def _create(
        project: Path,
        epic_id: str,
        milestone_id: str,
        phase_id: str,
        qa_status: str = "passed",
        status: str = "ready_for_review",
        version: str = "1.0",
        timestamp: str = "2026-06-01T12:00:00Z",
        filename: Optional[str] = None,
        deliverables: Optional[List[Dict[str, Any]]] = None,
        pr_details: Optional[Dict[str, Any]] = None,
        body: str = "# Completion Notice\nThis is a test completion notice."
    ) -> Path:
        if deliverables is None:
            deliverables = [
                {
                    "name": "Integration Tests",
                    "path": "tests/integration/test_artifact_happy_path.py",
                    "type": "implementation",
                    "status": "ready"
                }
            ]
        if pr_details is None:
            pr_details = {
                "number": 101,
                "title": f"feat: Add integration tests for {epic_id}",
                "target_branch": "milestone/M144",
                "url": f"https://github.com/example/pull/101"
            }
            
        frontmatter = {
            "artifact_type": "completion_notice",
            "artifact_version": version,
            "timestamp": timestamp,
            "issuer_chat": f"Epic Agent ({epic_id})",
            "issuer_role": "Epic Agent",
            "status": status,
            "epic_id": epic_id,
            "milestone_id": milestone_id,
            "phase_id": phase_id,
            "project_name": "ai-project-system",
            "deliverables": deliverables,
            "blockers": [],
            "qa_status": qa_status,
            "pr_details": pr_details
        }
        
        content = dict_to_frontmatter_markdown(frontmatter, body)
        
        name = filename or f"{epic_id}.md"
        cn_dir = project / ".ai-project" / "artifacts" / "completion-notices"
        cn_dir.mkdir(parents=True, exist_ok=True)
        file_path = cn_dir / name
        file_path.write_text(content, encoding="utf-8")
        return file_path
        
    return _create

@pytest.fixture
def make_review_decision():
    """Returns a helper function to create a valid review decision."""
    def _create(
        project: Path,
        decision: str,
        epic_id: Optional[str] = None,
        milestone_id: Optional[str] = None,
        phase_id: Optional[str] = None,
        feedback: str = "Looks great!",
        version: str = "1.0",
        timestamp: str = "2026-06-01T13:00:00Z",
        cn_timestamp: str = "2026-06-01T12:00:00Z",
        filename: Optional[str] = None,
        authorization: Optional[Dict[str, Any]] = None,
        body: str = "# Review Decision\nThis is a test review decision."
    ) -> Path:
        
        ref_id = epic_id or milestone_id or phase_id or "unknown"
        issuer_ref = milestone_id or phase_id or "HQ"
        
        if authorization is None:
            authorization = {
                "action": "merge" if decision == "accept" else "rework"
            }
            if decision == "accept":
                authorization["merge_instruction"] = "Merge pull request via squash"
                
        frontmatter = {
            "artifact_type": "review_decision",
            "artifact_version": version,
            "timestamp": timestamp,
            "issuer_chat": f"Milestone Agent ({issuer_ref})",
            "issuer_role": "Milestone Agent" if milestone_id else "Phase Agent" if phase_id else "HQ Agent",
            "decision": decision,
            "project_name": "ai-project-system",
            "completion_notice_timestamp": cn_timestamp,
            "feedback": feedback,
            "authorization": authorization
        }
        
        if epic_id:
            frontmatter["epic_id"] = epic_id
        if milestone_id:
            frontmatter["milestone_id"] = milestone_id
        if phase_id:
            frontmatter["phase_id"] = phase_id
            
        content = dict_to_frontmatter_markdown(frontmatter, body)
        
        name = filename or f"review_{ref_id}.md"
        rd_dir = project / ".ai-project" / "artifacts" / "review-decisions"
        rd_dir.mkdir(parents=True, exist_ok=True)
        file_path = rd_dir / name
        file_path.write_text(content, encoding="utf-8")
        return file_path
        
    return _create

@pytest.fixture
def make_delivery_notice():
    """Returns a helper function to create a valid delivery notice."""
    def _create(
        project: Path,
        epic_id: Optional[str] = None,
        milestone_id: Optional[str] = None,
        phase_id: Optional[str] = None,
        status: str = "delivered",
        version: str = "1.0",
        timestamp: str = "2026-06-01T13:15:00Z",
        cn_timestamp: str = "2026-06-01T12:00:00Z",
        rd_timestamp: str = "2026-06-01T13:00:00Z",
        filename: Optional[str] = None,
        merge_details: Optional[Dict[str, Any]] = None,
        duration: Optional[Dict[str, Any]] = None,
        final_artifacts: Optional[List[Dict[str, Any]]] = None,
        body: str = "# Delivery Notice\nThis is a test delivery notice."
    ) -> Path:
        
        ref_id = epic_id or milestone_id or phase_id or "unknown"
        issuer_ref = epic_id or milestone_id or phase_id or "unknown"
        
        if merge_details is None:
            merge_details = {
                "pr_number": 101,
                "pr_url": "https://github.com/example/pull/101",
                "merge_commit": "abc12345abcdef67890",
                "merge_timestamp": "2026-06-01T13:10:00Z",
                "merge_strategy": "squash",
                "target_branch": "milestone/M144"
            }
        if duration is None:
            duration = {
                "start_date": "2026-05-30",
                "end_date": "2026-06-01",
                "elapsed_days": 2
            }
        if final_artifacts is None:
            final_artifacts = [
                {
                    "name": "Integration Tests",
                    "path": "tests/integration/test_artifact_happy_path.py",
                    "type": "implementation"
                }
            ]
            
        frontmatter = {
            "artifact_type": "delivery_notice",
            "artifact_version": version,
            "timestamp": timestamp,
            "issuer_chat": f"Epic Agent ({issuer_ref})",
            "issuer_role": "Epic Agent",
            "status": status,
            "project_name": "ai-project-system",
            "merge_details": merge_details,
            "duration": duration,
            "final_artifacts": final_artifacts,
            "completion_notice_timestamp": cn_timestamp,
            "review_decision_timestamp": rd_timestamp
        }
        
        if epic_id:
            frontmatter["epic_id"] = epic_id
        if milestone_id:
            frontmatter["milestone_id"] = milestone_id
        if phase_id:
            frontmatter["phase_id"] = phase_id
            
        content = dict_to_frontmatter_markdown(frontmatter, body)
        
        name = filename or f"delivery_{ref_id}.md"
        dn_dir = project / ".ai-project" / "artifacts" / "delivery-notices"
        dn_dir.mkdir(parents=True, exist_ok=True)
        file_path = dn_dir / name
        file_path.write_text(content, encoding="utf-8")
        return file_path
        
    return _create
