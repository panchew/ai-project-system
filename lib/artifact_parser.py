"""
Main artifact parser module for parsing and validating artifact files.

This module provides the ArtifactParser class which handles:
- Reading artifact files
- Parsing YAML frontmatter
- Separating frontmatter from markdown body
- Validating against schemas
- Creating in-memory index for quick lookups
"""

import re
from pathlib import Path
from typing import Dict, Any, List, Optional, Union
from datetime import datetime, date, timezone
import yaml

from lib.artifact_errors import (
    ArtifactError,
    ArtifactParseError,
    ArtifactSchemaError,
    ArtifactTypeError,
    ArtifactNotFoundError,
    ArtifactFileError,
)
from lib.artifact_schemas import (
    get_schema_for_type,
    CompletionNoticeSchema,
    ReviewDecisionSchema,
    DeliveryNoticeSchema,
)


class Artifact:
    """Represents a parsed and validated artifact."""
    
    def __init__(
        self,
        artifact_type: str,
        frontmatter: Dict[str, Any],
        body: str,
        filepath: Optional[Path] = None,
    ):
        """Initialize an Artifact instance.
        
        Args:
            artifact_type: Type of artifact (completion_notice, review_decision, delivery_notice)
            frontmatter: Parsed YAML frontmatter as dictionary
            body: Markdown body content
            filepath: Path to the artifact file (optional)
        """
        self.artifact_type = artifact_type
        self.frontmatter = frontmatter
        self.body = body
        self.filepath = filepath
    
    def get_epic_id(self) -> Optional[str]:
        """Get the epic_id from frontmatter if present."""
        return self.frontmatter.get("epic_id")
    
    def get_milestone_id(self) -> Optional[str]:
        """Get the milestone_id from frontmatter if present."""
        return self.frontmatter.get("milestone_id")
    
    def get_phase_id(self) -> Optional[str]:
        """Get the phase_id from frontmatter if present."""
        return self.frontmatter.get("phase_id")
    
    def get_timestamp(self) -> Optional[str]:
        """Get the timestamp from frontmatter if present."""
        return self.frontmatter.get("timestamp")
    
    def get_status(self) -> Optional[str]:
        """Get the status from frontmatter if present."""
        return self.frontmatter.get("status")
    
    def __repr__(self) -> str:
        return f"Artifact(type={self.artifact_type}, epic_id={self.get_epic_id()})"


class ArtifactParser:
    """Parser for artifact files with schema validation and indexing."""
    
    # Regex pattern for YAML frontmatter
    FRONTMATTER_PATTERN = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
    
    def __init__(self):
        """Initialize the parser with empty indices."""
        self._artifacts_by_epic: Dict[str, List[Artifact]] = {}
        self._artifacts_by_milestone: Dict[str, List[Artifact]] = {}
        self._artifacts_by_phase: Dict[str, List[Artifact]] = {}
    
    def parse_file(self, filepath: Union[str, Path]) -> Artifact:
        """Parse and validate an artifact file.
        
        Args:
            filepath: Path to the artifact file
        
        Returns:
            Artifact: Parsed and validated artifact object
        
        Raises:
            ArtifactFileError: If file cannot be read
            ArtifactParseError: If YAML parsing fails
            ArtifactSchemaError: If validation fails
        """
        filepath = Path(filepath)
        
        try:
            content = filepath.read_text(encoding='utf-8')
        except (IOError, OSError) as e:
            raise ArtifactFileError(f"Failed to read artifact file: {filepath}") from e
        
        return self.parse_content(content, filepath)
    
    def parse_content(self, content: str, filepath: Optional[Path] = None) -> Artifact:
        """Parse artifact content (string) and validate.
        
        Args:
            content: Full artifact content including YAML frontmatter and markdown body
            filepath: Optional path for reference
        
        Returns:
            Artifact: Parsed and validated artifact object
        
        Raises:
            ArtifactParseError: If YAML parsing or structure is invalid
            ArtifactSchemaError: If validation fails
        """
        # Split frontmatter from body
        frontmatter_str, body = self._split_frontmatter(content)
        
        # Parse YAML frontmatter
        try:
            frontmatter = yaml.safe_load(frontmatter_str) or {}
        except yaml.YAMLError as e:
            raise ArtifactParseError(
                f"Failed to parse YAML frontmatter: {str(e)}"
            ) from e
        
        if not isinstance(frontmatter, dict):
            raise ArtifactParseError("YAML frontmatter must be a mapping (dictionary)")
        
        # Normalize types
        frontmatter = self._normalize_frontmatter(frontmatter)
        
        # Get artifact type
        artifact_type = frontmatter.get("artifact_type")
        if not artifact_type:
            raise ArtifactParseError("Missing required field: artifact_type")
        
        # Validate schema
        self._validate_schema(frontmatter, artifact_type)
        
        # Create and return Artifact object
        artifact = Artifact(artifact_type, frontmatter, body, filepath)
        
        # Index the artifact
        self._index_artifact(artifact)
        
        return artifact
    
    def _split_frontmatter(self, content: str) -> tuple:
        """Split artifact content into frontmatter and body.
        
        Args:
            content: Full artifact content
        
        Returns:
            Tuple of (frontmatter_str, body_str)
        
        Raises:
            ArtifactParseError: If frontmatter is malformed
        """
        match = self.FRONTMATTER_PATTERN.match(content)
        if not match:
            raise ArtifactParseError(
                "Artifact must start with YAML frontmatter enclosed in --- delimiters"
            )
        
        frontmatter_str = match.group(1).strip()
        body = content[match.end():].strip()
        
        return frontmatter_str, body
    
    def _validate_schema(self, data: Dict[str, Any], artifact_type: str) -> None:
        """Validate data against schema for artifact_type.
        
        Args:
            data: Dictionary to validate
            artifact_type: Type of artifact
        
        Raises:
            ArtifactTypeError: If artifact type is unknown
            ArtifactSchemaError: If validation fails
        """
        # Get schema for artifact type
        try:
            schema_class = get_schema_for_type(artifact_type)
        except KeyError as e:
            raise ArtifactTypeError(f"Unknown artifact type: {artifact_type}") from e
        
        # Check artifact_type matches
        if data.get("artifact_type") != artifact_type:
            raise ArtifactSchemaError(
                f"artifact_type mismatch: expected '{artifact_type}', "
                f"got '{data.get('artifact_type')}'"
            )
        
        # Check all required fields present
        required_fields = schema_class.get_required_fields()
        for field in required_fields:
            if field not in data:
                raise ArtifactSchemaError(f"Missing required field: {field}")
        
        # Validate field types and values
        for field, value in data.items():
            if field not in schema_class.schema:
                # Unknown field - allow it (forward compatibility)
                continue
            
            expected_type, _, _ = schema_class.schema[field]
            
            # Validate type
            if not schema_class.validate_field_type(field, value):
                raise ArtifactSchemaError(
                    f"Invalid type for field '{field}': expected {expected_type}, "
                    f"got {type(value).__name__}"
                )
        
        # Type-specific validation
        if artifact_type == "completion_notice":
            self._validate_completion_notice(data, schema_class)
        elif artifact_type == "review_decision":
            self._validate_review_decision(data, schema_class)
        elif artifact_type == "delivery_notice":
            self._validate_delivery_notice(data, schema_class)
    
    def _validate_completion_notice(
        self,
        data: Dict[str, Any],
        schema: type,
    ) -> None:
        """Validate completion_notice specific requirements."""
        # Validate artifact_type value
        if data.get("artifact_type") != "completion_notice":
            raise ArtifactSchemaError("artifact_type must be 'completion_notice'")
        
        # Validate status value
        if data.get("status") != "ready_for_review":
            raise ArtifactSchemaError("status must be 'ready_for_review'")
        
        # Validate qa_status value
        if data.get("qa_status") not in ["passed", "failed", "blocked"]:
            raise ArtifactSchemaError(
                f"qa_status must be one of: passed, failed, blocked"
            )
        
        # Validate reference formats
        if not schema.validate_reference_format(data.get("epic_id", ""), "epic_id"):
            raise ArtifactSchemaError(
                f"Invalid epic_id format: {data.get('epic_id')}"
            )
        if not schema.validate_reference_format(data.get("milestone_id", ""), "milestone_id"):
            raise ArtifactSchemaError(
                f"Invalid milestone_id format: {data.get('milestone_id')}"
            )
        if not schema.validate_reference_format(data.get("phase_id", ""), "phase_id"):
            raise ArtifactSchemaError(
                f"Invalid phase_id format: {data.get('phase_id')}"
            )
        
        # Validate deliverables
        deliverables = data.get("deliverables", [])
        if not isinstance(deliverables, list):
            raise ArtifactSchemaError("deliverables must be a list")
        if not deliverables:
            raise ArtifactSchemaError("deliverables must not be empty")
        
        for i, deliverable in enumerate(deliverables):
            if not schema.validate_deliverable(deliverable):
                raise ArtifactSchemaError(
                    f"Invalid deliverable at index {i}: {deliverable}"
                )
        
        # Validate blockers if present
        blockers = data.get("blockers", [])
        if blockers and not isinstance(blockers, list):
            raise ArtifactSchemaError("blockers must be a list")
        
        # Validate pr_details
        pr_details = data.get("pr_details")
        if not schema.validate_pr_details(pr_details):
            raise ArtifactSchemaError(f"Invalid pr_details structure: {pr_details}")
    
    def _validate_review_decision(
        self,
        data: Dict[str, Any],
        schema: type,
    ) -> None:
        """Validate review_decision specific requirements."""
        # Validate artifact_type value
        if data.get("artifact_type") != "review_decision":
            raise ArtifactSchemaError("artifact_type must be 'review_decision'")
        
        # Validate decision value
        if data.get("decision") not in ["accept", "reject"]:
            raise ArtifactSchemaError("decision must be 'accept' or 'reject'")
        
        # Validate at least one ID is present and valid
        epic_id = data.get("epic_id")
        milestone_id = data.get("milestone_id")
        phase_id = data.get("phase_id")
        
        if not (epic_id or milestone_id or phase_id):
            raise ArtifactSchemaError(
                "Must have at least one of: epic_id, milestone_id, phase_id"
            )
        
        # Validate reference formats if present
        if epic_id and not schema.validate_reference_format(epic_id, "epic_id"):
            raise ArtifactSchemaError(f"Invalid epic_id format: {epic_id}")
        if milestone_id and not schema.validate_reference_format(milestone_id, "milestone_id"):
            raise ArtifactSchemaError(f"Invalid milestone_id format: {milestone_id}")
        if phase_id and not schema.validate_reference_format(phase_id, "phase_id"):
            raise ArtifactSchemaError(f"Invalid phase_id format: {phase_id}")
        
        # Validate authorization
        authorization = data.get("authorization")
        if not schema.validate_authorization(authorization):
            raise ArtifactSchemaError(f"Invalid authorization structure: {authorization}")
    
    def _validate_delivery_notice(
        self,
        data: Dict[str, Any],
        schema: type,
    ) -> None:
        """Validate delivery_notice specific requirements."""
        # Validate artifact_type value
        if data.get("artifact_type") != "delivery_notice":
            raise ArtifactSchemaError("artifact_type must be 'delivery_notice'")
        
        # Validate status value
        if data.get("status") != "delivered":
            raise ArtifactSchemaError("status must be 'delivered'")
        
        # Validate at least one ID is present and valid
        epic_id = data.get("epic_id")
        milestone_id = data.get("milestone_id")
        phase_id = data.get("phase_id")
        
        if not (epic_id or milestone_id or phase_id):
            raise ArtifactSchemaError(
                "Must have at least one of: epic_id, milestone_id, phase_id"
            )
        
        # Validate reference formats if present
        if epic_id and not schema.validate_reference_format(epic_id, "epic_id"):
            raise ArtifactSchemaError(f"Invalid epic_id format: {epic_id}")
        if milestone_id and not schema.validate_reference_format(milestone_id, "milestone_id"):
            raise ArtifactSchemaError(f"Invalid milestone_id format: {milestone_id}")
        if phase_id and not schema.validate_reference_format(phase_id, "phase_id"):
            raise ArtifactSchemaError(f"Invalid phase_id format: {phase_id}")
        
        # Validate merge_details
        merge_details = data.get("merge_details")
        if not schema.validate_merge_details(merge_details):
            raise ArtifactSchemaError(f"Invalid merge_details structure: {merge_details}")
        
        # Validate duration
        duration = data.get("duration")
        if not schema.validate_duration(duration):
            raise ArtifactSchemaError(f"Invalid duration structure: {duration}")
        
        # Validate final_artifacts
        final_artifacts = data.get("final_artifacts", [])
        if not isinstance(final_artifacts, list):
            raise ArtifactSchemaError("final_artifacts must be a list")
        
        for i, artifact in enumerate(final_artifacts):
            if not schema.validate_final_artifact(artifact):
                raise ArtifactSchemaError(
                    f"Invalid artifact at index {i}: {artifact}"
                )
    
    def _index_artifact(self, artifact: Artifact) -> None:
        """Add artifact to indices for quick lookup.
        
        Args:
            artifact: The artifact to index
        """
        epic_id = artifact.get_epic_id()
        milestone_id = artifact.get_milestone_id()
        phase_id = artifact.get_phase_id()
        
        if epic_id:
            if epic_id not in self._artifacts_by_epic:
                self._artifacts_by_epic[epic_id] = []
            self._artifacts_by_epic[epic_id].append(artifact)
            # Keep sorted by timestamp (newest first)
            self._artifacts_by_epic[epic_id].sort(
                key=lambda a: a.get_timestamp() or "",
                reverse=True
            )
        
        if milestone_id:
            if milestone_id not in self._artifacts_by_milestone:
                self._artifacts_by_milestone[milestone_id] = []
            self._artifacts_by_milestone[milestone_id].append(artifact)
            self._artifacts_by_milestone[milestone_id].sort(
                key=lambda a: a.get_timestamp() or "",
                reverse=True
            )
        
        if phase_id:
            if phase_id not in self._artifacts_by_phase:
                self._artifacts_by_phase[phase_id] = []
            self._artifacts_by_phase[phase_id].append(artifact)
            self._artifacts_by_phase[phase_id].sort(
                key=lambda a: a.get_timestamp() or "",
                reverse=True
            )
    
    def get_artifact_by_epic(self, epic_id: str, artifact_type: Optional[str] = None) -> Optional[Artifact]:
        """Get the latest artifact for an epic_id.
        
        Args:
            epic_id: The epic ID to look up
            artifact_type: Optional artifact type filter (e.g., 'completion_notice')
        
        Returns:
            The latest Artifact for the epic, or None if not found
        """
        artifacts = self._artifacts_by_epic.get(epic_id, [])
        
        if artifact_type:
            artifacts = [a for a in artifacts if a.artifact_type == artifact_type]
        
        return artifacts[0] if artifacts else None
    
    def get_artifacts_by_epic(self, epic_id: str) -> List[Artifact]:
        """Get all artifacts for an epic_id (sorted by timestamp, newest first).
        
        Args:
            epic_id: The epic ID to look up
        
        Returns:
            List of artifacts for the epic
        """
        return self._artifacts_by_epic.get(epic_id, [])
    
    def get_artifact_by_milestone(self, milestone_id: str, artifact_type: Optional[str] = None) -> Optional[Artifact]:
        """Get the latest artifact for a milestone_id.
        
        Args:
            milestone_id: The milestone ID to look up (e.g., 'P1-M1')
            artifact_type: Optional artifact type filter
        
        Returns:
            The latest Artifact for the milestone, or None if not found
        """
        artifacts = self._artifacts_by_milestone.get(milestone_id, [])
        
        if artifact_type:
            artifacts = [a for a in artifacts if a.artifact_type == artifact_type]
        
        return artifacts[0] if artifacts else None
    
    def get_artifacts_by_milestone(self, milestone_id: str) -> List[Artifact]:
        """Get all artifacts for a milestone_id (sorted by timestamp, newest first).
        
        Args:
            milestone_id: The milestone ID to look up
        
        Returns:
            List of artifacts for the milestone
        """
        return self._artifacts_by_milestone.get(milestone_id, [])
    
    def get_artifact_by_phase(self, phase_id: str, artifact_type: Optional[str] = None) -> Optional[Artifact]:
        """Get the latest artifact for a phase_id.
        
        Args:
            phase_id: The phase ID to look up (e.g., 'P1')
            artifact_type: Optional artifact type filter
        
        Returns:
            The latest Artifact for the phase, or None if not found
        """
        artifacts = self._artifacts_by_phase.get(phase_id, [])
        
        if artifact_type:
            artifacts = [a for a in artifacts if a.artifact_type == artifact_type]
        
        return artifacts[0] if artifacts else None
    
    def get_artifacts_by_phase(self, phase_id: str) -> List[Artifact]:
        """Get all artifacts for a phase_id (sorted by timestamp, newest first).
        
        Args:
            phase_id: The phase ID to look up
        
        Returns:
            List of artifacts for the phase
        """
        return self._artifacts_by_phase.get(phase_id, [])

    def _normalize_frontmatter(self, data: Any) -> Any:
        """Normalize frontmatter types to strings where necessary."""
        if isinstance(data, dict):
            normalized = {}
            for k, v in data.items():
                if k == "artifact_version" and isinstance(v, (int, float)):
                    normalized[k] = str(v)
                elif k in ("timestamp", "completion_notice_timestamp", "review_decision_timestamp", "merge_timestamp") and isinstance(v, datetime):
                    if v.tzinfo:
                        v_utc = v.astimezone(timezone.utc)
                        normalized[k] = v_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
                    else:
                        normalized[k] = v.strftime("%Y-%m-%dT%H:%M:%SZ")
                elif k in ("start_date", "end_date") and isinstance(v, (datetime, date)):
                    normalized[k] = v.strftime("%Y-%m-%d")
                else:
                    normalized[k] = self._normalize_frontmatter(v)
            return normalized
        elif isinstance(data, list):
            return [self._normalize_frontmatter(item) for item in data]
        else:
            return data
