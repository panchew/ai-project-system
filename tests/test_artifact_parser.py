"""
Unit tests for artifact parsing and validation.

This module contains comprehensive tests for:
- YAML frontmatter parsing
- Schema validation for all artifact types
- Reference format validation
- Error handling and edge cases
- In-memory indexing and lookups
"""

import pytest
from pathlib import Path
from datetime import datetime

from lib.artifact_parser import ArtifactParser, Artifact
from lib.artifact_errors import (
    ArtifactParseError,
    ArtifactSchemaError,
    ArtifactTypeError,
    ArtifactFileError,
)


class TestArtifactParserBasic:
    """Test basic parser functionality."""
    
    def setup_method(self):
        """Initialize parser for each test."""
        self.parser = ArtifactParser()
    
    def test_parse_valid_completion_notice_file(self):
        """Test parsing a valid completion notice from file."""
        fixture_path = Path(__file__).parent / "fixtures" / "valid_completion_notice.md"
        artifact = self.parser.parse_file(fixture_path)
        
        assert artifact.artifact_type == "completion_notice"
        assert artifact.get_epic_id() == "P1-M1-E1.1"
        assert artifact.get_milestone_id() == "P1-M1"
        assert artifact.get_phase_id() == "P1"
        assert artifact.get_status() == "ready_for_review"
        assert artifact.get_timestamp() == "2026-05-29T14:32:00Z"
    
    def test_parse_valid_completion_notice_content(self):
        """Test parsing completion notice from string content."""
        content = """---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: 2026-05-29T14:32:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: test-project
deliverables:
  - name: Test
    path: test.py
    type: implementation
    status: ready
blockers: []
qa_status: passed
pr_details:
  number: 1
  title: "feat: Test"
  target_branch: milestone/M1
  url: "https://github.com/example/project/pull/1"
---

# Test Artifact

This is a test artifact.
"""
        artifact = self.parser.parse_content(content)
        assert artifact.artifact_type == "completion_notice"
        assert "Test Artifact" in artifact.body
    
    def test_parse_valid_review_decision_accept(self):
        """Test parsing a valid accept review decision."""
        fixture_path = Path(__file__).parent / "fixtures" / "valid_review_decision_accept.md"
        artifact = self.parser.parse_file(fixture_path)
        
        assert artifact.artifact_type == "review_decision"
        assert artifact.frontmatter.get("decision") == "accept"
        assert artifact.get_epic_id() == "P1-M1-E1.1"
    
    def test_parse_valid_review_decision_reject(self):
        """Test parsing a valid reject review decision."""
        fixture_path = Path(__file__).parent / "fixtures" / "valid_review_decision_reject.md"
        artifact = self.parser.parse_file(fixture_path)
        
        assert artifact.artifact_type == "review_decision"
        assert artifact.frontmatter.get("decision") == "reject"
    
    def test_parse_valid_delivery_notice(self):
        """Test parsing a valid delivery notice."""
        fixture_path = Path(__file__).parent / "fixtures" / "valid_delivery_notice.md"
        artifact = self.parser.parse_file(fixture_path)
        
        assert artifact.artifact_type == "delivery_notice"
        assert artifact.frontmatter.get("status") == "delivered"
        assert artifact.get_epic_id() == "P1-M1-E1.1"


class TestParseErrors:
    """Test error handling in parser."""
    
    def setup_method(self):
        """Initialize parser for each test."""
        self.parser = ArtifactParser()
    
    def test_file_not_found(self):
        """Test error when file doesn't exist."""
        with pytest.raises(ArtifactFileError):
            self.parser.parse_file("/nonexistent/path/to/file.md")
    
    def test_no_frontmatter(self):
        """Test error when frontmatter is missing."""
        fixture_path = Path(__file__).parent / "fixtures" / "invalid_no_frontmatter.md"
        
        with pytest.raises(ArtifactParseError) as exc_info:
            self.parser.parse_file(fixture_path)
        
        assert "yaml frontmatter" in str(exc_info.value).lower()
    
    def test_malformed_yaml(self):
        """Test error when YAML syntax is invalid."""
        fixture_path = Path(__file__).parent / "fixtures" / "invalid_yaml_syntax.md"
        
        with pytest.raises(ArtifactParseError):
            self.parser.parse_file(fixture_path)
    
    def test_missing_artifact_type(self):
        """Test error when artifact_type field is missing."""
        content = """---
artifact_version: 1.0
timestamp: 2026-05-29T14:32:00Z
---

# Test
"""
        with pytest.raises(ArtifactParseError) as exc_info:
            self.parser.parse_content(content)
        
        assert "artifact_type" in str(exc_info.value).lower()
    
    def test_unknown_artifact_type(self):
        """Test error when artifact_type is not recognized."""
        content = """---
artifact_type: unknown_type
artifact_version: 1.0
timestamp: 2026-05-29T14:32:00Z
---

# Test
"""
        with pytest.raises(ArtifactTypeError):
            self.parser.parse_content(content)


class TestSchemaValidation:
    """Test schema validation for completion notice."""
    
    def setup_method(self):
        """Initialize parser for each test."""
        self.parser = ArtifactParser()
    
    def test_missing_required_field_deliverables(self):
        """Test error when deliverables field is missing."""
        fixture_path = Path(__file__).parent / "fixtures" / "invalid_missing_field.md"
        
        with pytest.raises(ArtifactSchemaError) as exc_info:
            self.parser.parse_file(fixture_path)
        
        assert "deliverables" in str(exc_info.value).lower()
    
    def test_empty_deliverables_list(self):
        """Test error when deliverables list is empty."""
        content = """---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: 2026-05-29T14:32:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: test
deliverables: []
blockers: []
qa_status: passed
pr_details:
  number: 1
  title: "test"
  target_branch: milestone/M1
  url: "https://example.com/pull/1"
---
"""
        with pytest.raises(ArtifactSchemaError) as exc_info:
            self.parser.parse_content(content)
        
        assert "not be empty" in str(exc_info.value).lower()
    
    def test_invalid_qa_status(self):
        """Test error when qa_status has invalid value."""
        content = """---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: 2026-05-29T14:32:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: test
deliverables:
  - name: Test
    path: test.py
    type: implementation
    status: ready
blockers: []
qa_status: unknown_status
pr_details:
  number: 1
  title: "test"
  target_branch: milestone/M1
  url: "https://example.com/pull/1"
---
"""
        with pytest.raises(ArtifactSchemaError):
            self.parser.parse_content(content)
    
    def test_invalid_status_completion_notice(self):
        """Test error when status is not ready_for_review."""
        content = """---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: 2026-05-29T14:32:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: invalid_status
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: test
deliverables:
  - name: Test
    path: test.py
    type: implementation
    status: ready
blockers: []
qa_status: passed
pr_details:
  number: 1
  title: "test"
  target_branch: milestone/M1
  url: "https://example.com/pull/1"
---
"""
        with pytest.raises(ArtifactSchemaError):
            self.parser.parse_content(content)
    
    def test_invalid_deliverable_structure(self):
        """Test error when deliverable has missing fields."""
        content = """---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: 2026-05-29T14:32:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: test
deliverables:
  - name: Test
    path: test.py
blockers: []
qa_status: passed
pr_details:
  number: 1
  title: "test"
  target_branch: milestone/M1
  url: "https://example.com/pull/1"
---
"""
        with pytest.raises(ArtifactSchemaError):
            self.parser.parse_content(content)
    
    def test_invalid_pr_details_number(self):
        """Test error when pr_details.number is invalid."""
        content = """---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: 2026-05-29T14:32:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: test
deliverables:
  - name: Test
    path: test.py
    type: implementation
    status: ready
blockers: []
qa_status: passed
pr_details:
  number: invalid_number
  title: "test"
  target_branch: milestone/M1
  url: "https://example.com/pull/1"
---
"""
        with pytest.raises(ArtifactSchemaError):
            self.parser.parse_content(content)
    
    def test_valid_pr_details_pending(self):
        """Test that pr_details.number can be 'pending'."""
        content = """---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: 2026-05-29T14:32:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: test
deliverables:
  - name: Test
    path: test.py
    type: implementation
    status: ready
blockers: []
qa_status: passed
pr_details:
  number: pending
  title: "test"
  target_branch: milestone/M1
  url: "not_created_yet"
---
"""
        artifact = self.parser.parse_content(content)
        assert artifact.frontmatter["pr_details"]["number"] == "pending"


class TestReferenceValidation:
    """Test reference ID format validation."""
    
    def setup_method(self):
        """Initialize parser for each test."""
        self.parser = ArtifactParser()
    
    def test_invalid_epic_id_format(self):
        """Test error when epic_id format is invalid."""
        fixture_path = Path(__file__).parent / "fixtures" / "invalid_reference_format.md"
        
        with pytest.raises(ArtifactSchemaError) as exc_info:
            self.parser.parse_file(fixture_path)
        
        assert "epic_id" in str(exc_info.value).lower()
    
    def test_valid_epic_id_formats(self):
        """Test that valid epic_id formats are accepted."""
        # Standard epic format
        content1 = """---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: 2026-05-29T14:32:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: test
deliverables:
  - name: Test
    path: test.py
    type: implementation
    status: ready
blockers: []
qa_status: passed
pr_details:
  number: 1
  title: "test"
  target_branch: milestone/M1
  url: "https://example.com/pull/1"
---
"""
        artifact1 = self.parser.parse_content(content1)
        assert artifact1.get_epic_id() == "P1-M1-E1.1"
        
        # Bugfix format
        content2 = content1.replace("P1-M1-E1.1", "B1.2")
        artifact2 = self.parser.parse_content(content2)
        assert artifact2.get_epic_id() == "B1.2"
    
    def test_valid_milestone_id_format(self):
        """Test that valid milestone_id formats are accepted."""
        content = """---
artifact_type: review_decision
artifact_version: 1.0
timestamp: 2026-05-29T15:00:00Z
issuer_chat: Milestone Agent (P1-M1)
issuer_role: Milestone Agent
decision: accept
milestone_id: P1-M1
phase_id: P1
project_name: test
completion_notice_timestamp: 2026-05-29T14:32:00Z
feedback: "Good"
authorization:
  action: merge
  merge_instruction: "Merge PR"
---
"""
        artifact = self.parser.parse_content(content)
        assert artifact.get_milestone_id() == "P1-M1"
    
    def test_valid_phase_id_format(self):
        """Test that valid phase_id formats are accepted."""
        content = """---
artifact_type: review_decision
artifact_version: 1.0
timestamp: 2026-05-29T15:00:00Z
issuer_chat: Phase Agent (P1)
issuer_role: Phase Agent
decision: accept
phase_id: P1
project_name: test
completion_notice_timestamp: 2026-05-29T14:32:00Z
feedback: "Good"
authorization:
  action: merge
  merge_instruction: "Merge PR"
---
"""
        artifact = self.parser.parse_content(content)
        assert artifact.get_phase_id() == "P1"


class TestIndexing:
    """Test artifact indexing and lookup."""
    
    def setup_method(self):
        """Initialize parser for each test."""
        self.parser = ArtifactParser()
    
    def test_index_by_epic_id(self):
        """Test indexing artifacts by epic_id."""
        content = """---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: 2026-05-29T14:32:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: test
deliverables:
  - name: Test
    path: test.py
    type: implementation
    status: ready
blockers: []
qa_status: passed
pr_details:
  number: 1
  title: "test"
  target_branch: milestone/M1
  url: "https://example.com/pull/1"
---
"""
        artifact = self.parser.parse_content(content)
        
        # Look up by epic_id
        found = self.parser.get_artifact_by_epic("P1-M1-E1.1")
        assert found is not None
        assert found.artifact_type == "completion_notice"
    
    def test_get_all_artifacts_by_epic(self):
        """Test getting all artifacts for an epic."""
        fixture_path1 = Path(__file__).parent / "fixtures" / "valid_completion_notice.md"
        fixture_path2 = Path(__file__).parent / "fixtures" / "valid_delivery_notice.md"
        
        self.parser.parse_file(fixture_path1)
        self.parser.parse_file(fixture_path2)
        
        artifacts = self.parser.get_artifacts_by_epic("P1-M1-E1.1")
        assert len(artifacts) == 2
    
    def test_get_artifact_by_milestone(self):
        """Test getting artifact by milestone_id."""
        fixture_path = Path(__file__).parent / "fixtures" / "valid_completion_notice.md"
        self.parser.parse_file(fixture_path)
        
        found = self.parser.get_artifact_by_milestone("P1-M1")
        assert found is not None
        assert found.get_milestone_id() == "P1-M1"
    
    def test_get_artifact_by_phase(self):
        """Test getting artifact by phase_id."""
        fixture_path = Path(__file__).parent / "fixtures" / "valid_completion_notice.md"
        self.parser.parse_file(fixture_path)
        
        found = self.parser.get_artifact_by_phase("P1")
        assert found is not None
        assert found.get_phase_id() == "P1"
    
    def test_artifact_type_filter_in_lookup(self):
        """Test filtering by artifact type in lookups."""
        fixture_path1 = Path(__file__).parent / "fixtures" / "valid_completion_notice.md"
        fixture_path2 = Path(__file__).parent / "fixtures" / "valid_delivery_notice.md"
        
        self.parser.parse_file(fixture_path1)
        self.parser.parse_file(fixture_path2)
        
        # Should get completion_notice (newer timestamp)
        found = self.parser.get_artifact_by_epic("P1-M1-E1.1", artifact_type="completion_notice")
        assert found is not None
        assert found.artifact_type == "completion_notice"
    
    def test_nonexistent_lookup_returns_none(self):
        """Test that looking up nonexistent artifact returns None."""
        found = self.parser.get_artifact_by_epic("NONEXISTENT")
        assert found is None


class TestReviewDecisionValidation:
    """Test review_decision specific validation."""
    
    def setup_method(self):
        """Initialize parser for each test."""
        self.parser = ArtifactParser()
    
    def test_review_decision_accept_valid(self):
        """Test valid accept decision."""
        fixture_path = Path(__file__).parent / "fixtures" / "valid_review_decision_accept.md"
        artifact = self.parser.parse_file(fixture_path)
        assert artifact.frontmatter["decision"] == "accept"
    
    def test_review_decision_reject_valid(self):
        """Test valid reject decision."""
        fixture_path = Path(__file__).parent / "fixtures" / "valid_review_decision_reject.md"
        artifact = self.parser.parse_file(fixture_path)
        assert artifact.frontmatter["decision"] == "reject"
    
    def test_review_decision_missing_decision_field(self):
        """Test error when decision field is missing."""
        content = """---
artifact_type: review_decision
artifact_version: 1.0
timestamp: 2026-05-29T15:00:00Z
issuer_chat: Milestone Agent (P1-M1)
issuer_role: Milestone Agent
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: test
completion_notice_timestamp: 2026-05-29T14:32:00Z
feedback: "Good"
authorization:
  action: merge
  merge_instruction: "Merge PR"
---
"""
        with pytest.raises(ArtifactSchemaError):
            self.parser.parse_content(content)
    
    def test_review_decision_missing_id(self):
        """Test error when no reference ID is present."""
        content = """---
artifact_type: review_decision
artifact_version: 1.0
timestamp: 2026-05-29T15:00:00Z
issuer_chat: Milestone Agent (P1-M1)
issuer_role: Milestone Agent
decision: accept
project_name: test
completion_notice_timestamp: 2026-05-29T14:32:00Z
feedback: "Good"
authorization:
  action: merge
  merge_instruction: "Merge PR"
---
"""
        with pytest.raises(ArtifactSchemaError) as exc_info:
            self.parser.parse_content(content)
        
        assert "epic_id" in str(exc_info.value).lower() or "id" in str(exc_info.value).lower()


class TestDeliveryNoticeValidation:
    """Test delivery_notice specific validation."""
    
    def setup_method(self):
        """Initialize parser for each test."""
        self.parser = ArtifactParser()
    
    def test_delivery_notice_valid(self):
        """Test valid delivery notice."""
        fixture_path = Path(__file__).parent / "fixtures" / "valid_delivery_notice.md"
        artifact = self.parser.parse_file(fixture_path)
        assert artifact.frontmatter["status"] == "delivered"
    
    def test_delivery_notice_invalid_status(self):
        """Test error when status is not 'delivered'."""
        content = """---
artifact_type: delivery_notice
artifact_version: 1.0
timestamp: 2026-05-29T16:00:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: invalid
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: test
merge_details:
  pr_number: 1
  pr_url: "https://example.com/pull/1"
  merge_commit: "abc123"
  merge_timestamp: 2026-05-29T16:00:00Z
  merge_strategy: squash
  target_branch: milestone/M1
duration:
  start_date: "2026-05-28"
  end_date: "2026-05-29"
  elapsed_days: 1
final_artifacts:
  - name: Test
    path: test.py
    type: implementation
completion_notice_timestamp: 2026-05-29T14:32:00Z
review_decision_timestamp: 2026-05-29T15:00:00Z
---
"""
        with pytest.raises(ArtifactSchemaError):
            self.parser.parse_content(content)
    
    def test_delivery_notice_invalid_merge_strategy(self):
        """Test error when merge_strategy is invalid."""
        content = """---
artifact_type: delivery_notice
artifact_version: 1.0
timestamp: 2026-05-29T16:00:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: delivered
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: test
merge_details:
  pr_number: 1
  pr_url: "https://example.com/pull/1"
  merge_commit: "abc123"
  merge_timestamp: 2026-05-29T16:00:00Z
  merge_strategy: invalid_strategy
  target_branch: milestone/M1
duration:
  start_date: "2026-05-28"
  end_date: "2026-05-29"
  elapsed_days: 1
final_artifacts:
  - name: Test
    path: test.py
    type: implementation
completion_notice_timestamp: 2026-05-29T14:32:00Z
review_decision_timestamp: 2026-05-29T15:00:00Z
---
"""
        with pytest.raises(ArtifactSchemaError):
            self.parser.parse_content(content)


class TestEdgeCases:
    """Test edge cases and special scenarios."""
    
    def setup_method(self):
        """Initialize parser for each test."""
        self.parser = ArtifactParser()
    
    def test_timestamp_with_z_suffix(self):
        """Test that ISO-8601 timestamps with Z suffix are valid."""
        content = """---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: 2026-05-29T14:32:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: test
deliverables:
  - name: Test
    path: test.py
    type: implementation
    status: ready
blockers: []
qa_status: passed
pr_details:
  number: 1
  title: "test"
  target_branch: milestone/M1
  url: "https://example.com/pull/1"
---
"""
        artifact = self.parser.parse_content(content)
        assert artifact.get_timestamp() == "2026-05-29T14:32:00Z"
    
    def test_empty_blockers_list(self):
        """Test that empty blockers list is valid."""
        content = """---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: 2026-05-29T14:32:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: test
deliverables:
  - name: Test
    path: test.py
    type: implementation
    status: ready
blockers: []
qa_status: passed
pr_details:
  number: 1
  title: "test"
  target_branch: milestone/M1
  url: "https://example.com/pull/1"
---
"""
        artifact = self.parser.parse_content(content)
        assert artifact.frontmatter["blockers"] == []
    
    def test_url_without_protocol_fails(self):
        """Test that URLs without http/https protocol fail validation."""
        content = """---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: 2026-05-29T14:32:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: test
deliverables:
  - name: Test
    path: test.py
    type: implementation
    status: ready
blockers: []
qa_status: passed
pr_details:
  number: 1
  title: "test"
  target_branch: milestone/M1
  url: "example.com/pull/1"
---
"""
        with pytest.raises(ArtifactSchemaError):
            self.parser.parse_content(content)
    
    def test_multiple_artifacts_timestamp_sorting(self):
        """Test that artifacts are sorted by timestamp (newest first)."""
        content1 = """---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: 2026-05-29T14:00:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: test
deliverables:
  - name: Test
    path: test.py
    type: implementation
    status: ready
blockers: []
qa_status: passed
pr_details:
  number: 1
  title: "test"
  target_branch: milestone/M1
  url: "https://example.com/pull/1"
---
"""
        content2 = content1.replace("2026-05-29T14:00:00Z", "2026-05-29T15:00:00Z")
        
        # Parse older first
        artifact1 = self.parser.parse_content(content1)
        # Then parse newer
        artifact2 = self.parser.parse_content(content2)
        
        # Get latest should return the newer one (artifact2)
        latest = self.parser.get_artifact_by_epic("P1-M1-E1.1")
        assert latest.get_timestamp() == "2026-05-29T15:00:00Z"
    
    def test_frontmatter_only_yaml_object(self):
        """Test that non-dict YAML frontmatter fails."""
        content = """---
- item1
- item2
- item3
---

Body
"""
        with pytest.raises(ArtifactParseError) as exc_info:
            self.parser.parse_content(content)
        
        assert "mapping" in str(exc_info.value).lower() or "dictionary" in str(exc_info.value).lower()


class TestIntegration:
    """Integration tests for complete parsing workflows."""
    
    def setup_method(self):
        """Initialize parser for each test."""
        self.parser = ArtifactParser()
    
    def test_parse_all_fixture_types(self):
        """Test parsing all three artifact types from fixtures."""
        fixtures_dir = Path(__file__).parent / "fixtures"
        
        # Parse all valid fixtures
        valid_files = [
            "valid_completion_notice.md",
            "valid_review_decision_accept.md",
            "valid_delivery_notice.md",
        ]
        
        for filename in valid_files:
            filepath = fixtures_dir / filename
            artifact = self.parser.parse_file(filepath)
            assert artifact is not None
            assert artifact.frontmatter.get("artifact_version") == "1.0"
    
    def test_complete_workflow_simulation(self):
        """Simulate a complete artifact workflow (completion → review → delivery)."""
        # 1. Parse completion notice
        content_completion = """---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: 2026-05-29T14:32:00Z
issuer_chat: Epic Agent (P2-M1-E1.1)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P2-M1-E1.1
milestone_id: P2-M1
phase_id: P2
project_name: test-project
deliverables:
  - name: Feature
    path: src/feature.py
    type: implementation
    status: ready
blockers: []
qa_status: passed
pr_details:
  number: 100
  title: "feat: Complete feature"
  target_branch: milestone/M1
  url: "https://github.com/project/pull/100"
---
"""
        artifact_completion = self.parser.parse_content(content_completion)
        assert artifact_completion.artifact_type == "completion_notice"
        
        # 2. Parse review decision (accept)
        content_review = """---
artifact_type: review_decision
artifact_version: 1.0
timestamp: 2026-05-29T15:00:00Z
issuer_chat: Milestone Agent (P2-M1)
issuer_role: Milestone Agent
decision: accept
epic_id: P2-M1-E1.1
milestone_id: P2-M1
phase_id: P2
project_name: test-project
completion_notice_timestamp: 2026-05-29T14:32:00Z
feedback: "Looks good!"
authorization:
  action: merge
  merge_instruction: "Merge PR #100"
---
"""
        artifact_review = self.parser.parse_content(content_review)
        assert artifact_review.frontmatter["decision"] == "accept"
        
        # 3. Parse delivery notice
        content_delivery = """---
artifact_type: delivery_notice
artifact_version: 1.0
timestamp: 2026-05-29T16:00:00Z
issuer_chat: Epic Agent (P2-M1-E1.1)
issuer_role: Epic Agent
status: delivered
epic_id: P2-M1-E1.1
milestone_id: P2-M1
phase_id: P2
project_name: test-project
merge_details:
  pr_number: 100
  pr_url: "https://github.com/project/pull/100"
  merge_commit: "abc123"
  merge_timestamp: 2026-05-29T16:00:00Z
  merge_strategy: squash
  target_branch: milestone/M1
duration:
  start_date: "2026-05-29"
  end_date: "2026-05-29"
  elapsed_days: 0
final_artifacts:
  - name: Feature
    path: src/feature.py
    type: implementation
completion_notice_timestamp: 2026-05-29T14:32:00Z
review_decision_timestamp: 2026-05-29T15:00:00Z
---
"""
        artifact_delivery = self.parser.parse_content(content_delivery)
        assert artifact_delivery.frontmatter["status"] == "delivered"
        
        # Verify all three are indexed
        assert self.parser.get_artifact_by_epic("P2-M1-E1.1") is not None
        assert len(self.parser.get_artifacts_by_epic("P2-M1-E1.1")) == 3


class TestCoverageEnrichment:
    """Extra test cases specifically written to cover 100% of code paths in lib."""
    
    def setup_method(self):
        self.parser = ArtifactParser()

    def test_artifact_repr_and_lookups(self):
        """Test Artifact __repr__ and additional lookup filter paths."""
        artifact = Artifact("completion_notice", {"epic_id": "P1-M1-E1.1"}, "Body")
        assert "Artifact(type=completion_notice" in repr(artifact)
        
        # Additional lookups with and without filters
        self.parser._index_artifact(artifact)
        
        # Test get_artifact_by_milestone with type filter
        assert self.parser.get_artifact_by_milestone("P1-M1", "review_decision") is None
        
        # Test get_artifact_by_phase with type filter
        assert self.parser.get_artifact_by_phase("P1", "review_decision") is None
        
        # Test empty lookup collections
        assert self.parser.get_artifacts_by_milestone("NONEXISTENT") == []
        assert self.parser.get_artifacts_by_phase("NONEXISTENT") == []

    def test_schema_registry_mismatch_and_unknown_fields(self):
        """Test mismatch on validate_schema and forward compatibility with unknown fields."""
        # 1. Unknown field in schema should be ignored/allowed (line 220)
        content_with_unknown_field = """---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: 2026-05-29T14:32:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: test
extra_unknown_field: "some_value"
deliverables:
  - name: Test
    path: test.py
    type: implementation
    status: ready
blockers: []
qa_status: passed
pr_details:
  number: 1
  title: "test"
  target_branch: milestone/M1
  url: "https://example.com/pull/1"
---
"""
        artifact = self.parser.parse_content(content_with_with_unknown_field := content_with_unknown_field)
        assert artifact.frontmatter["extra_unknown_field"] == "some_value"

        # 2. Check artifact_type mismatch (line 205)
        with pytest.raises(ArtifactSchemaError) as exc_info:
            self.parser._validate_schema({"artifact_type": "review_decision"}, "completion_notice")
        assert "mismatch" in str(exc_info.value)

    def test_invalid_types_for_fields_in_schemas(self):
        """Test validate_field_type for float, bool, invalid iso8601, and invalid urls."""
        from lib.artifact_schemas import CompletionNoticeSchema
        
        # Define mock schemas for testing field type validation
        class MockSchema(CompletionNoticeSchema):
            schema = {
                "float_field": ("float", True, None),
                "bool_field": ("bool", True, None),
                "iso_field": ("iso8601", True, None),
                "url_field": ("url", True, None),
                "any_field": ("any_type", True, None),
            }
        
        # Test float type checks
        assert MockSchema.validate_field_type("float_field", 1.5) is True
        assert MockSchema.validate_field_type("float_field", 1) is True
        assert MockSchema.validate_field_type("float_field", "not_a_float") is False
        
        # Test bool type checks
        assert MockSchema.validate_field_type("bool_field", True) is True
        assert MockSchema.validate_field_type("bool_field", "not_a_bool") is False
        
        # Test iso8601 type checks with non-str
        assert MockSchema.validate_field_type("iso_field", 123) is False
        # Test iso8601 invalid string formats
        assert MockSchema.validate_field_type("iso_field", "invalid-date-string") is False
        
        # Test url type checks with non-str
        assert MockSchema.validate_field_type("url_field", 123) is False
        # Test url type checks with invalid prefix
        assert MockSchema.validate_field_type("url_field", "ftp://invalid-url.com") is False
        
        # Test unknown schema field
        assert MockSchema.validate_field_type("nonexistent_field", "val") is False
        # Test unknown expected_type field
        assert MockSchema.validate_field_type("any_field", "val") is False

        # Test invalid reference format check inputs
        assert MockSchema.validate_reference_format(123, "epic_id") is False
        assert MockSchema.validate_reference_format("P1-M1-E1.1", "unknown_ref_type") is False

    def test_deliverable_validation_errors(self):
        """Test CompletionNoticeSchema.validate_deliverable negative cases."""
        from lib.artifact_schemas import CompletionNoticeSchema
        
        # Non-dict
        assert CompletionNoticeSchema.validate_deliverable("not_a_dict") is False
        
        # Missing required fields
        assert CompletionNoticeSchema.validate_deliverable({"name": "only_name"}) is False
        
        # Wrong type for name
        assert CompletionNoticeSchema.validate_deliverable({"name": 123, "path": "p", "type": "implementation", "status": "ready"}) is False
        # Wrong type for path
        assert CompletionNoticeSchema.validate_deliverable({"name": "n", "path": 123, "type": "implementation", "status": "ready"}) is False
        # Invalid type option
        assert CompletionNoticeSchema.validate_deliverable({"name": "n", "path": "p", "type": "invalid_type", "status": "ready"}) is False
        # Invalid status option
        assert CompletionNoticeSchema.validate_deliverable({"name": "n", "path": "p", "type": "implementation", "status": "invalid_status"}) is False

    def test_pr_details_validation_errors(self):
        """Test CompletionNoticeSchema.validate_pr_details negative cases."""
        from lib.artifact_schemas import CompletionNoticeSchema
        
        # Non-dict
        assert CompletionNoticeSchema.validate_pr_details("not_a_dict") is False
        
        # Missing required fields
        assert CompletionNoticeSchema.validate_pr_details({"number": 1}) is False
        
        # Wrong title type
        base = {"number": 1, "title": "t", "target_branch": "b", "url": "https://url.com"}
        bad_title = base.copy(); bad_title["title"] = 123
        assert CompletionNoticeSchema.validate_pr_details(bad_title) is False
        
        # Wrong target_branch type
        bad_branch = base.copy(); bad_branch["target_branch"] = 123
        assert CompletionNoticeSchema.validate_pr_details(bad_branch) is False
        
        # Wrong url type or format
        bad_url1 = base.copy(); bad_url1["url"] = 123
        bad_url2 = base.copy(); bad_url2["url"] = "not_a_url_prefix"
        assert CompletionNoticeSchema.validate_pr_details(bad_url1) is False
        assert CompletionNoticeSchema.validate_pr_details(bad_url2) is False

    def test_authorization_validation_errors(self):
        """Test ReviewDecisionSchema.validate_authorization negative cases."""
        from lib.artifact_schemas import ReviewDecisionSchema
        
        # Non-dict
        assert ReviewDecisionSchema.validate_authorization("not_a_dict") is False
        
        # Missing action
        assert ReviewDecisionSchema.validate_authorization({"merge_instruction": "inst"}) is False
        
        # Invalid action
        assert ReviewDecisionSchema.validate_authorization({"action": "invalid"}) is False
        
        # Action is merge but merge_instruction missing or wrong type
        assert ReviewDecisionSchema.validate_authorization({"action": "merge"}) is False
        assert ReviewDecisionSchema.validate_authorization({"action": "merge", "merge_instruction": 123}) is False

    def test_merge_details_validation_errors(self):
        """Test DeliveryNoticeSchema.validate_merge_details negative cases."""
        from lib.artifact_schemas import DeliveryNoticeSchema
        
        # Non-dict
        assert DeliveryNoticeSchema.validate_merge_details("not_a_dict") is False
        
        # Missing fields
        assert DeliveryNoticeSchema.validate_merge_details({"pr_number": 1}) is False
        
        # Wrong type fields
        base = {
            "pr_number": 1, "pr_url": "url", "merge_commit": "commit", 
            "merge_timestamp": "2026-05-29T16:00:00Z", "merge_strategy": "squash", 
            "target_branch": "branch"
        }
        
        bad_pr_number = base.copy(); bad_pr_number["pr_number"] = [1] # not int or str
        bad_pr_url = base.copy(); bad_pr_url["pr_url"] = 123
        bad_merge_commit = base.copy(); bad_merge_commit["merge_commit"] = 123
        bad_strategy = base.copy(); bad_strategy["merge_strategy"] = "invalid_strategy"
        
        assert DeliveryNoticeSchema.validate_merge_details(bad_pr_number) is False
        assert DeliveryNoticeSchema.validate_merge_details(bad_pr_url) is False
        assert DeliveryNoticeSchema.validate_merge_details(bad_merge_commit) is False
        assert DeliveryNoticeSchema.validate_merge_details(bad_strategy) is False

    def test_duration_validation_errors(self):
        """Test DeliveryNoticeSchema.validate_duration negative cases."""
        from lib.artifact_schemas import DeliveryNoticeSchema
        
        # Non-dict
        assert DeliveryNoticeSchema.validate_duration("not_a_dict") is False
        
        # Missing fields
        assert DeliveryNoticeSchema.validate_duration({"start_date": "2026-05-28"}) is False
        
        # Wrong formats
        base = {"start_date": "2026-05-28", "end_date": "2026-05-29", "elapsed_days": 1}
        
        bad_start = base.copy(); bad_start["start_date"] = "28-05-2026"
        bad_end = base.copy(); bad_end["end_date"] = "29-05-2026"
        bad_days = base.copy(); bad_days["elapsed_days"] = "one"
        
        assert DeliveryNoticeSchema.validate_duration(bad_start) is False
        assert DeliveryNoticeSchema.validate_duration(bad_end) is False
        assert DeliveryNoticeSchema.validate_duration(bad_days) is False

    def test_final_artifact_validation_errors(self):
        """Test DeliveryNoticeSchema.validate_final_artifact negative cases."""
        from lib.artifact_schemas import DeliveryNoticeSchema
        
        # Non-dict
        assert DeliveryNoticeSchema.validate_final_artifact("not_a_dict") is False
        
        # Missing fields
        assert DeliveryNoticeSchema.validate_final_artifact({"name": "n"}) is False
        
        # Wrong types
        base = {"name": "n", "path": "p", "type": "implementation"}
        
        bad_name = base.copy(); bad_name["name"] = 123
        bad_path = base.copy(); bad_path["path"] = 123
        bad_type = base.copy(); bad_type["type"] = "invalid_type"
        
        assert DeliveryNoticeSchema.validate_final_artifact(bad_name) is False
        assert DeliveryNoticeSchema.validate_final_artifact(bad_path) is False
        assert DeliveryNoticeSchema.validate_final_artifact(bad_type) is False

    def test_parser_specific_validation_coverage(self):
        """Test validation error branches in ArtifactParser for specific artifact types."""
        from lib.artifact_schemas import CompletionNoticeSchema, ReviewDecisionSchema, DeliveryNoticeSchema
        from datetime import datetime, date
        
        # Test naive datetime normalization
        naive_dt = datetime(2026, 5, 29, 14, 32, 0)
        res = self.parser._normalize_frontmatter({"timestamp": naive_dt})
        assert res["timestamp"] == "2026-05-29T14:32:00Z"
        
        # Test date normalization
        some_date = date(2026, 5, 29)
        res_date = self.parser._normalize_frontmatter({"start_date": some_date})
        assert res_date["start_date"] == "2026-05-29"

        # 1. Completion notice validations
        # Deliverables not a list
        with pytest.raises(ArtifactSchemaError) as exc_info:
            self.parser._validate_completion_notice({
                "artifact_type": "completion_notice", "status": "ready_for_review", "qa_status": "passed",
                "epic_id": "P1-M1-E1.1", "milestone_id": "P1-M1", "phase_id": "P1",
                "deliverables": "not_a_list"
            }, CompletionNoticeSchema)
        assert "deliverables must be a list" in str(exc_info.value)

        # Blockers not a list
        with pytest.raises(ArtifactSchemaError) as exc_info:
            self.parser._validate_completion_notice({
                "artifact_type": "completion_notice", "status": "ready_for_review", "qa_status": "passed",
                "epic_id": "P1-M1-E1.1", "milestone_id": "P1-M1", "phase_id": "P1",
                "deliverables": [{"name": "n", "path": "p", "type": "implementation", "status": "ready"}],
                "blockers": "not_a_list"
            }, CompletionNoticeSchema)
        assert "blockers must be a list" in str(exc_info.value)

        # Wrong artifact_type
        with pytest.raises(ArtifactSchemaError):
            self.parser._validate_completion_notice({
                "artifact_type": "wrong_type", "status": "ready_for_review", "qa_status": "passed",
                "epic_id": "P1-M1-E1.1", "milestone_id": "P1-M1", "phase_id": "P1",
            }, CompletionNoticeSchema)

        # Wrong status
        with pytest.raises(ArtifactSchemaError):
            self.parser._validate_completion_notice({
                "artifact_type": "completion_notice", "status": "wrong_status", "qa_status": "passed",
                "epic_id": "P1-M1-E1.1", "milestone_id": "P1-M1", "phase_id": "P1",
            }, CompletionNoticeSchema)

        # Wrong qa_status
        with pytest.raises(ArtifactSchemaError):
            self.parser._validate_completion_notice({
                "artifact_type": "completion_notice", "status": "ready_for_review", "qa_status": "wrong_qa",
                "epic_id": "P1-M1-E1.1", "milestone_id": "P1-M1", "phase_id": "P1",
            }, CompletionNoticeSchema)

        # Wrong milestone_id format
        with pytest.raises(ArtifactSchemaError):
            self.parser._validate_completion_notice({
                "artifact_type": "completion_notice", "status": "ready_for_review", "qa_status": "passed",
                "epic_id": "P1-M1-E1.1", "milestone_id": "invalid_ms", "phase_id": "P1",
            }, CompletionNoticeSchema)

        # Wrong phase_id format
        with pytest.raises(ArtifactSchemaError):
            self.parser._validate_completion_notice({
                "artifact_type": "completion_notice", "status": "ready_for_review", "qa_status": "passed",
                "epic_id": "P1-M1-E1.1", "milestone_id": "P1-M1", "phase_id": "invalid_ph",
            }, CompletionNoticeSchema)

        # 2. Review decision validations
        # Wrong type validation check
        with pytest.raises(ArtifactSchemaError):
            self.parser._validate_review_decision({"artifact_type": "wrong_type"}, ReviewDecisionSchema)
            
        # Wrong decision value
        with pytest.raises(ArtifactSchemaError):
            self.parser._validate_review_decision({"artifact_type": "review_decision", "decision": "invalid"}, ReviewDecisionSchema)

        # Invalid epic_id
        with pytest.raises(ArtifactSchemaError):
            self.parser._validate_review_decision({
                "artifact_type": "review_decision", "decision": "accept",
                "epic_id": "invalid_epic", "milestone_id": "P1-M1", "phase_id": "P1",
                "authorization": {"action": "merge", "merge_instruction": "Merge"}
            }, ReviewDecisionSchema)

        # Invalid milestone_id
        with pytest.raises(ArtifactSchemaError):
            self.parser._validate_review_decision({
                "artifact_type": "review_decision", "decision": "accept",
                "epic_id": "P1-M1-E1.1", "milestone_id": "invalid_ms", "phase_id": "P1",
                "authorization": {"action": "merge", "merge_instruction": "Merge"}
            }, ReviewDecisionSchema)

        # Invalid phase_id
        with pytest.raises(ArtifactSchemaError):
            self.parser._validate_review_decision({
                "artifact_type": "review_decision", "decision": "accept",
                "epic_id": "P1-M1-E1.1", "milestone_id": "P1-M1", "phase_id": "invalid_ph",
                "authorization": {"action": "merge", "merge_instruction": "Merge"}
            }, ReviewDecisionSchema)

        # Invalid authorization
        with pytest.raises(ArtifactSchemaError):
            self.parser._validate_review_decision({
                "artifact_type": "review_decision", "decision": "accept",
                "epic_id": "P1-M1-E1.1", "milestone_id": "P1-M1", "phase_id": "P1",
                "authorization": "not_a_dict"
            }, ReviewDecisionSchema)

        # 3. Delivery notice validations
        # Wrong type validation check
        with pytest.raises(ArtifactSchemaError):
            self.parser._validate_delivery_notice({"artifact_type": "wrong_type"}, DeliveryNoticeSchema)
            
        # Wrong status value
        with pytest.raises(ArtifactSchemaError):
            self.parser._validate_delivery_notice({"artifact_type": "delivery_notice", "status": "invalid"}, DeliveryNoticeSchema)

        # Missing any id
        with pytest.raises(ArtifactSchemaError):
            self.parser._validate_delivery_notice({
                "artifact_type": "delivery_notice", "status": "delivered",
                "merge_details": {"pr_number": 1, "pr_url": "url", "merge_commit": "c", "merge_timestamp": "t", "merge_strategy": "squash", "target_branch": "b"},
                "duration": {"start_date": "2026-05-28", "end_date": "2026-05-29", "elapsed_days": 1},
                "final_artifacts": []
            }, DeliveryNoticeSchema)

        # Invalid epic_id
        with pytest.raises(ArtifactSchemaError):
            self.parser._validate_delivery_notice({
                "artifact_type": "delivery_notice", "status": "delivered",
                "epic_id": "invalid_epic", "milestone_id": "P1-M1", "phase_id": "P1",
                "merge_details": {"pr_number": 1, "pr_url": "url", "merge_commit": "c", "merge_timestamp": "t", "merge_strategy": "squash", "target_branch": "b"},
                "duration": {"start_date": "2026-05-28", "end_date": "2026-05-29", "elapsed_days": 1},
                "final_artifacts": []
            }, DeliveryNoticeSchema)

        # Invalid milestone_id
        with pytest.raises(ArtifactSchemaError):
            self.parser._validate_delivery_notice({
                "artifact_type": "delivery_notice", "status": "delivered",
                "epic_id": "P1-M1-E1.1", "milestone_id": "invalid_ms", "phase_id": "P1",
                "merge_details": {"pr_number": 1, "pr_url": "url", "merge_commit": "c", "merge_timestamp": "t", "merge_strategy": "squash", "target_branch": "b"},
                "duration": {"start_date": "2026-05-28", "end_date": "2026-05-29", "elapsed_days": 1},
                "final_artifacts": []
            }, DeliveryNoticeSchema)

        # Invalid phase_id
        with pytest.raises(ArtifactSchemaError):
            self.parser._validate_delivery_notice({
                "artifact_type": "delivery_notice", "status": "delivered",
                "epic_id": "P1-M1-E1.1", "milestone_id": "P1-M1", "phase_id": "invalid_ph",
                "merge_details": {"pr_number": 1, "pr_url": "url", "merge_commit": "c", "merge_timestamp": "t", "merge_strategy": "squash", "target_branch": "b"},
                "duration": {"start_date": "2026-05-28", "end_date": "2026-05-29", "elapsed_days": 1},
                "final_artifacts": []
            }, DeliveryNoticeSchema)

        # Invalid duration structure
        with pytest.raises(ArtifactSchemaError):
            self.parser._validate_delivery_notice({
                "artifact_type": "delivery_notice", "status": "delivered",
                "epic_id": "P1-M1-E1.1", "milestone_id": "P1-M1", "phase_id": "P1",
                "merge_details": {"pr_number": 1, "pr_url": "url", "merge_commit": "c", "merge_timestamp": "t", "merge_strategy": "squash", "target_branch": "b"},
                "duration": "not_a_dict",
                "final_artifacts": []
            }, DeliveryNoticeSchema)

        # Final_artifacts not a list
        with pytest.raises(ArtifactSchemaError) as exc_info:
            self.parser._validate_delivery_notice({
                "artifact_type": "delivery_notice", "status": "delivered",
                "epic_id": "P1-M1-E1.1", "milestone_id": "P1-M1", "phase_id": "P1",
                "merge_details": {"pr_number": 1, "pr_url": "url", "merge_commit": "c", "merge_timestamp": "t", "merge_strategy": "squash", "target_branch": "b"},
                "duration": {"start_date": "2026-05-28", "end_date": "2026-05-29", "elapsed_days": 1},
                "final_artifacts": "not_a_list"
            }, DeliveryNoticeSchema)
        assert "final_artifacts must be a list" in str(exc_info.value)

        # Invalid final_artifact structure
        with pytest.raises(ArtifactSchemaError):
            self.parser._validate_delivery_notice({
                "artifact_type": "delivery_notice", "status": "delivered",
                "epic_id": "P1-M1-E1.1", "milestone_id": "P1-M1", "phase_id": "P1",
                "merge_details": {"pr_number": 1, "pr_url": "url", "merge_commit": "c", "merge_timestamp": "t", "merge_strategy": "squash", "target_branch": "b"},
                "duration": {"start_date": "2026-05-28", "end_date": "2026-05-29", "elapsed_days": 1},
                "final_artifacts": ["invalid_artifact"]
            }, DeliveryNoticeSchema)

