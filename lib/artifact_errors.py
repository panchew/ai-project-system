"""
Custom exceptions for artifact parsing and validation.

This module defines all custom exception types used by the artifact parsing system.
"""


class ArtifactError(Exception):
    """Base exception for all artifact-related errors."""
    pass


class ArtifactParseError(ArtifactError):
    """Raised when YAML frontmatter parsing fails.
    
    This occurs when the artifact file has malformed YAML, missing frontmatter,
    or invalid syntax in the YAML section.
    """
    pass


class ArtifactSchemaError(ArtifactError):
    """Raised when artifact data fails schema validation.
    
    This occurs when:
    - Required fields are missing
    - Field types don't match schema
    - Reference formats are invalid (epic_id, milestone_id, etc.)
    - Field values are invalid or out of expected range
    """
    pass


class ArtifactTypeError(ArtifactError):
    """Raised when artifact type is unknown or unsupported."""
    pass


class ArtifactNotFoundError(ArtifactError):
    """Raised when an artifact is not found in the index."""
    pass


class ArtifactFileError(ArtifactError):
    """Raised when artifact file cannot be read or accessed."""
    pass
