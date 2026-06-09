"""
Artifact parsing and validation library for the AI Project System.

This package provides tools for parsing, validating, and indexing artifacts
used in the artifact-driven communication system.

Main exports:
- ArtifactParser: Main parser class
- Artifact: Parsed artifact representation
- Custom exceptions: ArtifactParseError, ArtifactSchemaError, etc.
"""

from lib.artifact_parser import ArtifactParser, Artifact
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
    SCHEMA_REGISTRY,
)

__all__ = [
    "ArtifactParser",
    "Artifact",
    "ArtifactError",
    "ArtifactParseError",
    "ArtifactSchemaError",
    "ArtifactTypeError",
    "ArtifactNotFoundError",
    "ArtifactFileError",
    "get_schema_for_type",
    "SCHEMA_REGISTRY",
]
