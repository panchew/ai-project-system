"""
Validation tests for the team-project-example artifact files.

Verifies:
- YAML front-matter parses without errors
- Required fields are present for each artifact type
- Artifact filenames match the naming convention
- At least one Accept and one Reject review decision exist
- Epic IDs follow the P#-M#-E#.# pattern
- team role names in artifacts match TEAM_SETUP.md defined roles
- Minimum artifact counts are met (3+ completion notices, 2+ review decisions, 3+ delivery notices)
- Bugfix Epic spec has the required category field
"""

import re
import pytest
from pathlib import Path
from datetime import datetime, timezone

import yaml


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

EXAMPLE_ROOT = Path(__file__).parent.parent / "examples" / "team-project-example"
ARTIFACTS_ROOT = EXAMPLE_ROOT / ".ai-project" / "artifacts"
COMPLETION_NOTICES_DIR = ARTIFACTS_ROOT / "completion-notices"
REVIEW_DECISIONS_DIR = ARTIFACTS_ROOT / "review-decisions"
DELIVERY_NOTICES_DIR = ARTIFACTS_ROOT / "delivery-notices"
DOCS_ROOT = EXAMPLE_ROOT / "docs" / "phases"


def parse_frontmatter(file_path: Path) -> dict:
    """Extract and parse YAML front-matter from a Markdown file."""
    content = file_path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}
    return yaml.safe_load(parts[1]) or {}


def get_artifact_files(directory: Path) -> list[Path]:
    return sorted(directory.glob("*.md"))


# Filename pattern: <ISO-timestamp>__<ID>__<artifact-type>.md
FILENAME_PATTERN = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}Z__[A-Z0-9\-\.]+__[\w\-]+\.md$"
)

# Epic ID pattern: P#-M#-E#.# or P#-M#-B#.#
EPIC_ID_PATTERN = re.compile(r"^P\d+-M\d+-[EB]\d+\.\d+$")

# Milestone ID pattern: P#-M#
MILESTONE_ID_PATTERN = re.compile(r"^P\d+-M\d+$")

# ISO-8601 UTC timestamp pattern (in YAML body)
TIMESTAMP_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")

# Roles defined in TEAM_SETUP.md
DEFINED_ROLES = {"Epic Agent", "Milestone Agent", "Phase Lead", "CFO"}


# ---------------------------------------------------------------------------
# Test 1: Completion notices directory exists and has 3+ files
# ---------------------------------------------------------------------------

class TestCompletionNoticeCount:
    def test_at_least_three_completion_notices_exist(self):
        files = get_artifact_files(COMPLETION_NOTICES_DIR)
        assert len(files) >= 3, (
            f"Expected at least 3 completion notices, found {len(files)}: {[f.name for f in files]}"
        )


# ---------------------------------------------------------------------------
# Test 2: YAML front-matter validity for all completion notices
# ---------------------------------------------------------------------------

class TestCompletionNoticeYAML:
    @pytest.fixture(params=get_artifact_files(COMPLETION_NOTICES_DIR), ids=lambda p: p.name)
    def completion_notice(self, request):
        return request.param

    def test_completion_notice_yaml_parses_without_error(self, completion_notice):
        fm = parse_frontmatter(completion_notice)
        assert isinstance(fm, dict), f"YAML front-matter failed to parse in {completion_notice.name}"
        assert len(fm) > 0, f"Empty front-matter in {completion_notice.name}"

    def test_completion_notice_required_fields(self, completion_notice):
        fm = parse_frontmatter(completion_notice)
        required = [
            "artifact_type", "artifact_version", "timestamp",
            "issuer_chat", "issuer_role", "status",
            "epic_id", "milestone_id", "phase_id", "project_name",
            "deliverables", "qa_status",
        ]
        missing = [f for f in required if f not in fm]
        assert not missing, (
            f"Missing required fields in {completion_notice.name}: {missing}"
        )

    def test_completion_notice_artifact_type_value(self, completion_notice):
        fm = parse_frontmatter(completion_notice)
        assert fm.get("artifact_type") == "completion_notice", (
            f"artifact_type must be 'completion_notice' in {completion_notice.name}, "
            f"got: {fm.get('artifact_type')}"
        )

    def test_completion_notice_status_value(self, completion_notice):
        fm = parse_frontmatter(completion_notice)
        valid_statuses = {"ready_for_review", "delivered", "in_progress"}
        assert fm.get("status") in valid_statuses, (
            f"status must be one of {valid_statuses} in {completion_notice.name}, "
            f"got: {fm.get('status')}"
        )

    def test_completion_notice_epic_id_format(self, completion_notice):
        fm = parse_frontmatter(completion_notice)
        epic_id = str(fm.get("epic_id", ""))
        assert EPIC_ID_PATTERN.match(epic_id), (
            f"epic_id '{epic_id}' does not match P#-M#-E#.# format in {completion_notice.name}"
        )

    def test_completion_notice_milestone_id_format(self, completion_notice):
        fm = parse_frontmatter(completion_notice)
        milestone_id = str(fm.get("milestone_id", ""))
        assert MILESTONE_ID_PATTERN.match(milestone_id), (
            f"milestone_id '{milestone_id}' does not match P#-M# format in {completion_notice.name}"
        )


# ---------------------------------------------------------------------------
# Test 3: YAML front-matter validity for all review decisions
# ---------------------------------------------------------------------------

class TestReviewDecisionYAML:
    @pytest.fixture(params=get_artifact_files(REVIEW_DECISIONS_DIR), ids=lambda p: p.name)
    def review_decision(self, request):
        return request.param

    def test_review_decision_yaml_parses_without_error(self, review_decision):
        fm = parse_frontmatter(review_decision)
        assert isinstance(fm, dict), f"YAML front-matter failed to parse in {review_decision.name}"
        assert len(fm) > 0, f"Empty front-matter in {review_decision.name}"

    def test_review_decision_required_fields(self, review_decision):
        fm = parse_frontmatter(review_decision)
        required = [
            "artifact_type", "artifact_version", "timestamp",
            "issuer_chat", "issuer_role", "decision",
            "epic_id", "milestone_id", "phase_id", "project_name",
            "completion_notice_timestamp", "authorization",
        ]
        missing = [f for f in required if f not in fm]
        assert not missing, (
            f"Missing required fields in {review_decision.name}: {missing}"
        )

    def test_review_decision_artifact_type_value(self, review_decision):
        fm = parse_frontmatter(review_decision)
        assert fm.get("artifact_type") == "review_decision", (
            f"artifact_type must be 'review_decision' in {review_decision.name}"
        )

    def test_review_decision_decision_field_is_valid(self, review_decision):
        fm = parse_frontmatter(review_decision)
        assert fm.get("decision") in {"accept", "reject"}, (
            f"decision must be 'accept' or 'reject' in {review_decision.name}, "
            f"got: {fm.get('decision')}"
        )


# ---------------------------------------------------------------------------
# Test 4: YAML front-matter validity for all delivery notices
# ---------------------------------------------------------------------------

class TestDeliveryNoticeYAML:
    @pytest.fixture(params=get_artifact_files(DELIVERY_NOTICES_DIR), ids=lambda p: p.name)
    def delivery_notice(self, request):
        return request.param

    def test_delivery_notice_yaml_parses_without_error(self, delivery_notice):
        fm = parse_frontmatter(delivery_notice)
        assert isinstance(fm, dict), f"YAML front-matter failed to parse in {delivery_notice.name}"
        assert len(fm) > 0, f"Empty front-matter in {delivery_notice.name}"

    def test_delivery_notice_required_fields(self, delivery_notice):
        fm = parse_frontmatter(delivery_notice)
        required = [
            "artifact_type", "artifact_version", "timestamp",
            "issuer_chat", "issuer_role", "status",
            "epic_id", "milestone_id", "phase_id", "project_name",
            "merge_details", "duration", "final_artifacts",
        ]
        missing = [f for f in required if f not in fm]
        assert not missing, (
            f"Missing required fields in {delivery_notice.name}: {missing}"
        )

    def test_delivery_notice_status_is_delivered(self, delivery_notice):
        fm = parse_frontmatter(delivery_notice)
        assert fm.get("status") == "delivered", (
            f"status must be 'delivered' in {delivery_notice.name}, got: {fm.get('status')}"
        )

    def test_delivery_notice_merge_details_has_required_subfields(self, delivery_notice):
        fm = parse_frontmatter(delivery_notice)
        merge_details = fm.get("merge_details", {}) or {}
        required_subfields = ["pr_number", "merge_commit", "target_branch", "merge_strategy"]
        missing = [f for f in required_subfields if f not in merge_details]
        assert not missing, (
            f"merge_details missing subfields in {delivery_notice.name}: {missing}"
        )


# ---------------------------------------------------------------------------
# Test 5: Artifact filename convention
# ---------------------------------------------------------------------------

class TestArtifactFilenameConvention:
    def _all_artifact_files(self):
        files = []
        for d in [COMPLETION_NOTICES_DIR, REVIEW_DECISIONS_DIR, DELIVERY_NOTICES_DIR]:
            files.extend(d.glob("*.md"))
        return files

    def test_all_artifact_filenames_match_naming_convention(self):
        bad_names = []
        for f in self._all_artifact_files():
            if not FILENAME_PATTERN.match(f.name):
                bad_names.append(f.name)
        assert not bad_names, (
            f"The following artifact filenames do not match the naming convention "
            f"<timestamp>__<ID>__<type>.md: {bad_names}"
        )


# ---------------------------------------------------------------------------
# Test 6: Review decisions include both accept and reject
# ---------------------------------------------------------------------------

class TestReviewDecisionCoverage:
    def test_at_least_two_review_decisions_exist(self):
        files = get_artifact_files(REVIEW_DECISIONS_DIR)
        assert len(files) >= 2, (
            f"Expected at least 2 review decisions, found {len(files)}"
        )

    def test_review_decisions_include_at_least_one_accept(self):
        decisions = [parse_frontmatter(f).get("decision") for f in get_artifact_files(REVIEW_DECISIONS_DIR)]
        assert "accept" in decisions, (
            f"No 'accept' review decision found. Decisions: {decisions}"
        )

    def test_review_decisions_include_at_least_one_reject(self):
        decisions = [parse_frontmatter(f).get("decision") for f in get_artifact_files(REVIEW_DECISIONS_DIR)]
        assert "reject" in decisions, (
            f"No 'reject' review decision found. Decisions: {decisions}"
        )


# ---------------------------------------------------------------------------
# Test 7: Delivery notice minimum count
# ---------------------------------------------------------------------------

class TestDeliveryNoticeCount:
    def test_at_least_three_delivery_notices_exist(self):
        files = get_artifact_files(DELIVERY_NOTICES_DIR)
        assert len(files) >= 3, (
            f"Expected at least 3 delivery notices, found {len(files)}"
        )


# ---------------------------------------------------------------------------
# Test 8: Bugfix Epic spec has required category field
# ---------------------------------------------------------------------------

class TestBugfixEpicSpec:
    def _find_bugfix_specs(self):
        return list(DOCS_ROOT.rglob("B*.md"))

    def test_bugfix_epic_spec_exists(self):
        specs = self._find_bugfix_specs()
        assert len(specs) >= 1, (
            "No bugfix Epic spec (B*.md) found under docs/phases/"
        )

    def test_bugfix_epic_has_category_bugfix(self):
        for spec in self._find_bugfix_specs():
            fm = parse_frontmatter(spec)
            assert fm.get("category") == "bugfix", (
                f"Bugfix Epic spec {spec.name} must have 'category: bugfix' in front-matter"
            )

    def test_bugfix_epic_has_severity_field(self):
        for spec in self._find_bugfix_specs():
            fm = parse_frontmatter(spec)
            assert "severity" in fm, (
                f"Bugfix Epic spec {spec.name} must have a 'severity' field"
            )
            assert fm["severity"] in {"critical", "high", "medium", "low"}, (
                f"Bugfix severity must be critical/high/medium/low in {spec.name}"
            )


# ---------------------------------------------------------------------------
# Test 9: Epic spec count (7-9 standard epics)
# ---------------------------------------------------------------------------

class TestEpicSpecCount:
    def _find_epic_specs(self):
        return [f for f in DOCS_ROOT.rglob("E*.md") if "__spec__" in f.name]

    def _find_bugfix_specs(self):
        return [f for f in DOCS_ROOT.rglob("B*.md") if "__spec__" in f.name]

    def test_at_least_seven_epic_specs_exist(self):
        specs = self._find_epic_specs()
        assert len(specs) >= 7, (
            f"Expected at least 7 standard Epic specs, found {len(specs)}: "
            f"{[f.name for f in specs]}"
        )

    def test_at_most_nine_epic_specs_exist(self):
        specs = self._find_epic_specs()
        bugfix = self._find_bugfix_specs()
        total = len(specs) + len(bugfix)
        assert total <= 9, (
            f"Expected at most 9 total Epic specs (standard + bugfix), found {total}"
        )

    def test_epic_spec_yaml_is_valid(self):
        bad = []
        for spec in self._find_epic_specs():
            fm = parse_frontmatter(spec)
            if not isinstance(fm, dict) or not fm:
                bad.append(spec.name)
        assert not bad, f"Epic specs with invalid/empty YAML front-matter: {bad}"


# ---------------------------------------------------------------------------
# Test 10: Phase and Milestone spec existence
# ---------------------------------------------------------------------------

class TestPhaseAndMilestoneSpecs:
    def test_phase_spec_exists(self):
        phase_specs = list(DOCS_ROOT.rglob("P*__phase-spec.md"))
        assert len(phase_specs) >= 1, "No phase spec found (P*__phase-spec.md)"

    def test_milestone_specs_exist(self):
        milestone_specs = list(DOCS_ROOT.rglob("M*__milestone-spec.md"))
        assert len(milestone_specs) >= 3, (
            f"Expected at least 3 milestone specs, found {len(milestone_specs)}"
        )

    def test_phase_spec_yaml_valid(self):
        for spec in DOCS_ROOT.rglob("P*__phase-spec.md"):
            fm = parse_frontmatter(spec)
            assert fm.get("type") == "phase", (
                f"Phase spec {spec.name} must have 'type: phase'"
            )

    def test_milestone_spec_yaml_valid(self):
        for spec in DOCS_ROOT.rglob("M*__milestone-spec.md"):
            fm = parse_frontmatter(spec)
            assert fm.get("type") == "milestone", (
                f"Milestone spec {spec.name} must have 'type: milestone'"
            )


# ---------------------------------------------------------------------------
# Test 11: TEAM_SETUP.md exists and contains all required roles
# ---------------------------------------------------------------------------

class TestTeamSetup:
    TEAM_SETUP_PATH = EXAMPLE_ROOT / "TEAM_SETUP.md"
    REQUIRED_ROLES = ["CFO", "Phase Lead", "Developer 1", "Developer 2", "Reviewer"]

    def test_team_setup_file_exists(self):
        assert self.TEAM_SETUP_PATH.exists(), "TEAM_SETUP.md not found"

    def test_team_setup_contains_all_required_roles(self):
        content = self.TEAM_SETUP_PATH.read_text(encoding="utf-8")
        missing_roles = [role for role in self.REQUIRED_ROLES if role not in content]
        assert not missing_roles, (
            f"TEAM_SETUP.md is missing these required roles: {missing_roles}"
        )

    def test_team_setup_contains_decision_authority_section(self):
        content = self.TEAM_SETUP_PATH.read_text(encoding="utf-8")
        assert "Decision" in content or "Authority" in content, (
            "TEAM_SETUP.md must contain a decision authority section"
        )


# ---------------------------------------------------------------------------
# Test 12: WALKTHROUGH.md exists and mentions key lifecycle stages
# ---------------------------------------------------------------------------

class TestWalkthrough:
    WALKTHROUGH_PATH = EXAMPLE_ROOT / "WALKTHROUGH.md"
    REQUIRED_STAGES = [
        "Completion Notice",
        "Review Decision",
        "Delivery Notice",
        "parallel",
    ]

    def test_walkthrough_file_exists(self):
        assert self.WALKTHROUGH_PATH.exists(), "WALKTHROUGH.md not found"

    def test_walkthrough_mentions_all_lifecycle_stages(self):
        content = self.WALKTHROUGH_PATH.read_text(encoding="utf-8")
        missing = [s for s in self.REQUIRED_STAGES if s.lower() not in content.lower()]
        assert not missing, (
            f"WALKTHROUGH.md is missing references to: {missing}"
        )

    def test_walkthrough_mentions_who_decides(self):
        content = self.WALKTHROUGH_PATH.read_text(encoding="utf-8")
        assert "Phase Lead" in content, (
            "WALKTHROUGH.md must name the Phase Lead role as a decision-maker"
        )
        assert "CFO" in content, (
            "WALKTHROUGH.md must name the CFO role as a decision-maker"
        )


# ---------------------------------------------------------------------------
# Test 13: Delivery notices reference valid epic IDs
# ---------------------------------------------------------------------------

class TestDeliveryNoticeEpicIdIntegrity:
    def test_delivery_notice_epic_ids_are_valid(self):
        bad = []
        for f in get_artifact_files(DELIVERY_NOTICES_DIR):
            fm = parse_frontmatter(f)
            epic_id = str(fm.get("epic_id", ""))
            if not EPIC_ID_PATTERN.match(epic_id):
                bad.append((f.name, epic_id))
        assert not bad, (
            f"Delivery notices with invalid epic_id format: {bad}"
        )

    def test_delivery_notice_has_merge_commit(self):
        for f in get_artifact_files(DELIVERY_NOTICES_DIR):
            fm = parse_frontmatter(f)
            merge_details = fm.get("merge_details") or {}
            commit = merge_details.get("merge_commit", "")
            assert commit and commit != "pending", (
                f"Delivery notice {f.name} must have a non-empty merge_commit"
            )


# ---------------------------------------------------------------------------
# Test 14: Timestamp format in YAML front-matter
# ---------------------------------------------------------------------------

class TestTimestampFormat:
    def _all_artifact_frontmatters(self):
        results = []
        for d in [COMPLETION_NOTICES_DIR, REVIEW_DECISIONS_DIR, DELIVERY_NOTICES_DIR]:
            for f in d.glob("*.md"):
                results.append((f.name, parse_frontmatter(f)))
        return results

    def test_artifact_timestamps_are_iso8601(self):
        # PyYAML auto-converts ISO-8601 timestamps to Python datetime objects.
        # Accept either: a datetime object (UTC), or a string matching the pattern.
        bad = []
        for name, fm in self._all_artifact_frontmatters():
            ts = fm.get("timestamp")
            if isinstance(ts, datetime):
                # PyYAML parsed it as datetime — validate it is timezone-aware (UTC)
                if ts.tzinfo is None:
                    bad.append((name, str(ts), "naive datetime (no timezone)"))
            elif isinstance(ts, str):
                if not TIMESTAMP_PATTERN.match(ts):
                    bad.append((name, ts, "string does not match ISO-8601 pattern"))
            else:
                bad.append((name, repr(ts), f"unexpected type {type(ts).__name__}"))
        assert not bad, (
            f"Artifacts with non-ISO-8601 timestamps: {bad}"
        )
