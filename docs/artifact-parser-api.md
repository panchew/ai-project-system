# Artifact Parser API Reference

This document provides a comprehensive API reference for the main artifact parser module in `lib/artifact_parser.py`.

The Artifact Parser handles:
- Reading and separating YAML frontmatter from markdown body in artifact files.
- Validating the extracted data against type-specific schemas.
- In-memory indexing of valid artifacts by reference keys (e.g., `epic_id`, `milestone_id`, `phase_id`) for quick retrieval.

---

## Classes

### `Artifact`

Represents a parsed and fully validated artifact.

#### Constructor

```python
def __init__(self, artifact_type: str, frontmatter: dict, body: str, filepath: Optional[Path] = None)
```
Initializes a new `Artifact` instance.

#### Properties / Methods

- **`artifact_type`**: `str`
  Type of artifact (`completion_notice`, `review_decision`, or `delivery_notice`).
- **`frontmatter`**: `dict`
  The parsed and validated YAML frontmatter.
- **`body`**: `str`
  The markdown body following the frontmatter section.
- **`filepath`**: `Optional[Path]`
  The path to the source file, if read from the filesystem.

- **`get_epic_id() -> Optional[str]`**
  Returns the `epic_id` from the frontmatter, or `None` if not present.
- **`get_milestone_id() -> Optional[str]`**
  Returns the `milestone_id` from the frontmatter, or `None` if not present.
- **`get_phase_id() -> Optional[str]`**
  Returns the `phase_id` from the frontmatter, or `None` if not present.
- **`get_timestamp() -> Optional[str]`**
  Returns the `timestamp` as an ISO-8601 UTC string.
- **`get_status() -> Optional[str]`**
  Returns the `status` from the frontmatter, or `None` if not present.

---

### `ArtifactParser`

Main class for parsing, validating, and indexing artifacts.

#### Constructor

```python
def __init__()
```
Initializes an `ArtifactParser` instance with empty in-memory indices.

#### Key Methods

- **`parse_file(filepath: Union[str, Path]) -> Artifact`**
  Parses and validates an artifact file.
  - **Parameters:** `filepath` - Absolute or relative path to the artifact file.
  - **Returns:** An `Artifact` instance.
  - **Raises:**
    - `ArtifactFileError`: If the file cannot be accessed.
    - `ArtifactParseError`: If the frontmatter is missing or malformed YAML.
    - `ArtifactSchemaError`: If the frontmatter fails schema validation.

- **`parse_content(content: str, filepath: Optional[Path] = None) -> Artifact`**
  Parses and validates artifact content from a string.
  - **Parameters:**
    - `content` - Full artifact file contents (including frontmatter).
    - `filepath` - Optional path for reference in error messages.
  - **Returns:** An `Artifact` instance.
  - **Raises:**
    - `ArtifactParseError` or `ArtifactSchemaError` as above.

- **`get_artifact_by_epic(epic_id: str, artifact_type: Optional[str] = None) -> Optional[Artifact]`**
  Retrieves the latest parsed artifact for a specific epic ID.
  - **Parameters:**
    - `epic_id` - Target epic reference (e.g., `P4-M14-E14.1` or `B1.1`).
    - `artifact_type` - Optional filter for artifact type.
  - **Returns:** The latest matching `Artifact`, or `None` if not found.
 
- **`get_artifacts_by_epic(epic_id: str) -> List[Artifact]`**
  Retrieves all parsed artifacts for a specific epic ID, sorted with newest first.
 
- **`get_artifact_by_milestone(milestone_id: str, artifact_type: Optional[str] = None) -> Optional[Artifact]`**
  Retrieves the latest parsed artifact for a specific milestone ID (e.g., `P4-M14`).

- **`get_artifacts_by_milestone(milestone_id: str) -> List[Artifact]`**
  Retrieves all parsed artifacts for a specific milestone ID, sorted with newest first.

- **`get_artifact_by_phase(phase_id: str, artifact_type: Optional[str] = None) -> Optional[Artifact]`**
  Retrieves the latest parsed artifact for a specific phase ID (e.g., `P4`).

- **`get_artifacts_by_phase(phase_id: str) -> List[Artifact]`**
  Retrieves all parsed artifacts for a specific phase ID, sorted with newest first.

---

## Error Handling

All custom exceptions are defined in `lib/artifact_errors.py` and derive from `ArtifactError`.

- **`ArtifactFileError`**: File cannot be read or accessed.
- **`ArtifactParseError`**: Frontmatter is missing, malformed, or doesn't start/end with standard delimiters (`---`).
- **`ArtifactSchemaError`**: Validation fails. Provides exact field and type details (e.g., `"Invalid type for field 'artifact_version': expected string, got float"`).
- **`ArtifactTypeError`**: `artifact_type` is unrecognized or unsupported.

---

## Example Usage

```python
from pathlib import Path
from lib.artifact_parser import ArtifactParser
from lib.artifact_errors import ArtifactError

parser = ArtifactParser()

try:
    # Parse a single artifact file
    artifact = parser.parse_file("/path/to/artifacts/completion-notices/2026-05-29__P4-M14-E14.1__completion_notice.md")
    print(f"Parsed {artifact.artifact_type} for {artifact.get_epic_id()}")
    
    # Retrieve using index
    latest_cn = parser.get_artifact_by_epic("P4-M14-E14.1", artifact_type="completion_notice")
    if latest_cn:
        print(f"Latest status: {latest_cn.get_status()}")
        
except ArtifactError as e:
    print(f"Error parsing artifact: {e}")
```
