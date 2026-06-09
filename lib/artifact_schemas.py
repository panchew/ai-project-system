"""
Schema definitions for artifact validation.

This module defines the validation schemas for all three artifact types:
- completion_notice
- review_decision
- delivery_notice
"""

from typing import Dict, Any, List, Union
from datetime import datetime


class ArtifactSchema:
    """Base schema class for artifact validation."""
    
    # Schema definition: field_name -> (type, required, validator_func)
    # validator_func is optional and receives the field value
    schema: Dict[str, tuple] = {}
    
    @classmethod
    def get_schema(cls) -> Dict[str, tuple]:
        """Get the schema definition for this artifact type."""
        return cls.schema
    
    @classmethod
    def get_required_fields(cls) -> List[str]:
        """Get list of required field names."""
        return [field for field, (_, required, _) in cls.schema.items() if required]
    
    @classmethod
    def validate_field_type(cls, field_name: str, value: Any) -> bool:
        """Validate that field value matches expected type."""
        if field_name not in cls.schema:
            return False
        
        expected_type, _, _ = cls.schema[field_name]
        
        if expected_type == "string":
            return isinstance(value, str)
        elif expected_type == "int":
            return isinstance(value, int)
        elif expected_type == "float":
            return isinstance(value, (int, float))
        elif expected_type == "bool":
            return isinstance(value, bool)
        elif expected_type == "list":
            return isinstance(value, list)
        elif expected_type == "dict":
            return isinstance(value, dict)
        elif expected_type == "iso8601":
            if not isinstance(value, str):
                return False
            try:
                datetime.fromisoformat(value.replace('Z', '+00:00'))
                return True
            except (ValueError, AttributeError):
                return False
        elif expected_type == "url":
            if not isinstance(value, str):
                return False
            return value.startswith(('http://', 'https://'))
        elif isinstance(expected_type, (list, tuple)):
            return value in expected_type
        
        return False
    
    @classmethod
    def validate_reference_format(cls, reference: str, ref_type: str) -> bool:
        """Validate reference ID format.
        
        Args:
            reference: The reference ID string (e.g., 'P1-M1-E1.1')
            ref_type: Type of reference ('epic_id', 'milestone_id', 'phase_id')
        
        Returns:
            True if reference matches expected format
        """
        if not isinstance(reference, str):
            return False
        
        if ref_type == "epic_id":
            # Format: P#-M#-E#.# or B#.#
            import re
            return bool(re.match(r'^(P\d+-M\d+-E\d+\.\d+|B\d+\.\d+)$', reference))
        elif ref_type == "milestone_id":
            # Format: P#-M#
            import re
            return bool(re.match(r'^P\d+-M\d+$', reference))
        elif ref_type == "phase_id":
            # Format: P#
            import re
            return bool(re.match(r'^P\d+$', reference))
        
        return False


class CompletionNoticeSchema(ArtifactSchema):
    """Schema for completion_notice artifacts."""
    
    schema = {
        "artifact_type": ("string", True, None),  # Must be "completion_notice"
        "artifact_version": ("string", True, None),  # e.g., "1.0"
        "timestamp": ("iso8601", True, None),  # ISO-8601 UTC datetime
        "issuer_chat": ("string", True, None),  # e.g., "Epic Agent (P1-M1-E1.1)"
        "issuer_role": ("string", True, None),  # e.g., "Epic Agent"
        "status": (["ready_for_review"], True, None),  # Fixed value
        "epic_id": ("string", True, None),  # P#-M#-E#.# format
        "milestone_id": ("string", True, None),  # P#-M# format
        "phase_id": ("string", True, None),  # P# format
        "project_name": ("string", True, None),
        "deliverables": ("list", True, None),  # Array of deliverable objects
        "blockers": ("list", False, None),  # Optional, array of blocker objects
        "qa_status": (["passed", "failed", "blocked"], True, None),
        "pr_details": ("dict", True, None),  # Object with number, title, target_branch, url
    }
    
    @classmethod
    def validate_deliverable(cls, deliverable: Any) -> bool:
        """Validate deliverable object structure."""
        if not isinstance(deliverable, dict):
            return False
        
        required_fields = {"name", "path", "type", "status"}
        if not all(field in deliverable for field in required_fields):
            return False
        
        if not isinstance(deliverable.get("name"), str):
            return False
        if not isinstance(deliverable.get("path"), str):
            return False
        if deliverable.get("type") not in ["spec", "implementation", "report", "pr"]:
            return False
        if deliverable.get("status") not in ["ready", "pending", "failed"]:
            return False
        
        return True
    
    @classmethod
    def validate_pr_details(cls, pr_details: Any) -> bool:
        """Validate PR details object structure."""
        if not isinstance(pr_details, dict):
            return False
        
        required_fields = {"number", "title", "target_branch", "url"}
        if not all(field in pr_details for field in required_fields):
            return False
        
        number = pr_details.get("number")
        if not (isinstance(number, int) or number == "pending"):
            return False
        
        if not isinstance(pr_details.get("title"), str):
            return False
        if not isinstance(pr_details.get("target_branch"), str):
            return False
        
        url = pr_details.get("url")
        if not (isinstance(url, str) and (url.startswith("http") or url == "not_created_yet")):
            return False
        
        return True


class ReviewDecisionSchema(ArtifactSchema):
    """Schema for review_decision artifacts."""
    
    schema = {
        "artifact_type": ("string", True, None),  # Must be "review_decision"
        "artifact_version": ("string", True, None),  # e.g., "1.0"
        "timestamp": ("iso8601", True, None),  # ISO-8601 UTC datetime
        "issuer_chat": ("string", True, None),  # e.g., "Milestone Agent (P1-M1)"
        "issuer_role": ("string", True, None),  # e.g., "Milestone Agent"
        "decision": (["accept", "reject"], True, None),  # Fixed values
        "epic_id": ("string", False, None),  # Optional for milestone-level decisions
        "milestone_id": ("string", False, None),  # P#-M# format
        "phase_id": ("string", False, None),  # P# format
        "project_name": ("string", True, None),
        "completion_notice_timestamp": ("iso8601", True, None),
        "feedback": ("string", True, None),
        "authorization": ("dict", True, None),  # Object with action and merge_instruction
    }
    
    @classmethod
    def validate_authorization(cls, authorization: Any) -> bool:
        """Validate authorization object structure."""
        if not isinstance(authorization, dict):
            return False
        
        if "action" not in authorization:
            return False
        
        action = authorization.get("action")
        if action not in ["merge", "rework"]:
            return False
        
        if action == "merge" and not isinstance(authorization.get("merge_instruction"), str):
            return False
        
        return True


class DeliveryNoticeSchema(ArtifactSchema):
    """Schema for delivery_notice artifacts."""
    
    schema = {
        "artifact_type": ("string", True, None),  # Must be "delivery_notice"
        "artifact_version": ("string", True, None),  # e.g., "1.0"
        "timestamp": ("iso8601", True, None),  # ISO-8601 UTC datetime
        "issuer_chat": ("string", True, None),  # e.g., "Epic Agent (P1-M1-E1.1)"
        "issuer_role": ("string", True, None),  # e.g., "Epic Agent"
        "status": (["delivered"], True, None),  # Fixed value
        "epic_id": ("string", False, None),  # Optional for milestone-level delivery
        "milestone_id": ("string", False, None),  # P#-M# format
        "phase_id": ("string", False, None),  # P# format
        "project_name": ("string", True, None),
        "merge_details": ("dict", True, None),  # Object with merge information
        "duration": ("dict", True, None),  # Object with start_date, end_date, elapsed_days
        "final_artifacts": ("list", True, None),  # Array of artifact objects
        "completion_notice_timestamp": ("iso8601", True, None),
        "review_decision_timestamp": ("iso8601", True, None),
    }
    
    @classmethod
    def validate_merge_details(cls, merge_details: Any) -> bool:
        """Validate merge_details object structure."""
        if not isinstance(merge_details, dict):
            return False
        
        required_fields = {"pr_number", "pr_url", "merge_commit", "merge_timestamp", 
                          "merge_strategy", "target_branch"}
        if not all(field in merge_details for field in required_fields):
            return False
        
        if not isinstance(merge_details.get("pr_number"), (int, str)):
            return False
        if not isinstance(merge_details.get("pr_url"), str):
            return False
        if not isinstance(merge_details.get("merge_commit"), str):
            return False
        
        merge_strategy = merge_details.get("merge_strategy")
        if merge_strategy not in ["squash", "rebase", "merge"]:
            return False
        
        return True
    
    @classmethod
    def validate_duration(cls, duration: Any) -> bool:
        """Validate duration object structure."""
        if not isinstance(duration, dict):
            return False
        
        required_fields = {"start_date", "end_date", "elapsed_days"}
        if not all(field in duration for field in required_fields):
            return False
        
        # Validate dates are in YYYY-MM-DD format
        import re
        date_pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(date_pattern, duration.get("start_date", "")):
            return False
        if not re.match(date_pattern, duration.get("end_date", "")):
            return False
        
        if not isinstance(duration.get("elapsed_days"), int):
            return False
        
        return True
    
    @classmethod
    def validate_final_artifact(cls, artifact: Any) -> bool:
        """Validate final artifact object structure."""
        if not isinstance(artifact, dict):
            return False
        
        required_fields = {"name", "path", "type"}
        if not all(field in artifact for field in required_fields):
            return False
        
        if not isinstance(artifact.get("name"), str):
            return False
        if not isinstance(artifact.get("path"), str):
            return False
        if artifact.get("type") not in ["spec", "implementation", "report"]:
            return False
        
        return True


# Schema registry for easy lookup
SCHEMA_REGISTRY = {
    "completion_notice": CompletionNoticeSchema,
    "review_decision": ReviewDecisionSchema,
    "delivery_notice": DeliveryNoticeSchema,
}


def get_schema_for_type(artifact_type: str) -> ArtifactSchema:
    """Get the schema class for a given artifact type.
    
    Args:
        artifact_type: The artifact type string (e.g., 'completion_notice')
    
    Returns:
        The schema class for the artifact type
    
    Raises:
        KeyError: If artifact type is not registered
    """
    if artifact_type not in SCHEMA_REGISTRY:
        raise KeyError(f"Unknown artifact type: {artifact_type}")
    
    return SCHEMA_REGISTRY[artifact_type]
