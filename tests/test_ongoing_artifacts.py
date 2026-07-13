"""
Validation tests for the Creation Chat ongoing-artifact templates.

Verifies (Epic P4-M19-E19.2):
- governance/templates/steering-note.md has the required YAML front-matter schema
- governance/templates/progress-digest.md has the required front-matter and the
  four mandated sections
- governance/templates/bouncer-work-log.md has the required minimal front-matter
- The committed reference Steering Note (2026-06-19) validates against the schema
- governance/systems/creation-chat-guide.md documents the re-instantiation ritual
"""

import re
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).parent.parent
TEMPLATES = REPO_ROOT / "governance" / "templates"
STEERING_NOTE_TEMPLATE = TEMPLATES / "steering-note.md"
PROGRESS_DIGEST_TEMPLATE = TEMPLATES / "progress-digest.md"
BOUNCER_WORK_LOG_TEMPLATE = TEMPLATES / "bouncer-work-log.md"
CREATION_CHAT_GUIDE = REPO_ROOT / "governance" / "systems" / "creation-chat-guide.md"
AI_PROJECT_YML = REPO_ROOT / ".ai-project.yml"
REFERENCE_STEERING_NOTE = (
    REPO_ROOT
    / ".ai-project"
    / "artifacts"
    / "steering-notes"
    / "2026-06-19__creation-chat__steering-note.md"
)

STEERING_NOTE_FIELDS = [
    "artifact_type",
    "artifact_version",
    "timestamp",
    "issuer_chat",
    "target",
    "project_name",
    "concerns",
    "decisions",
]

PROGRESS_DIGEST_FIELDS = [
    "artifact_type",
    "artifact_version",
    "timestamp",
    "issuer_chat",
    "target",
    "project_name",
    "period_covered",
]

BOUNCER_WORK_LOG_FIELDS = [
    "artifact_type",
    "timestamp",
    "project",
    "severity",
]

PROGRESS_DIGEST_SECTIONS = [
    "## Phase Status",
    "## Open Decisions",
    "## Next Actions",
    "## Blocking Concerns",
]


def parse_frontmatter(file_path: Path) -> dict:
    """Extract and parse YAML front-matter from a Markdown file."""
    content = file_path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}
    return yaml.safe_load(parts[1]) or {}


# ---------------------------------------------------------------------------
# Steering Note template
# ---------------------------------------------------------------------------

class TestSteeringNoteTemplate:
    def test_exists(self):
        assert STEERING_NOTE_TEMPLATE.exists(), (
            "governance/templates/steering-note.md not found"
        )

    def test_frontmatter_parses(self):
        fm = parse_frontmatter(STEERING_NOTE_TEMPLATE)
        assert isinstance(fm, dict) and fm, (
            "steering-note template front-matter failed to parse"
        )

    def test_has_required_frontmatter_fields(self):
        fm = parse_frontmatter(STEERING_NOTE_TEMPLATE)
        missing = [f for f in STEERING_NOTE_FIELDS if f not in fm]
        assert not missing, f"steering-note template missing fields: {missing}"

    def test_artifact_type(self):
        fm = parse_frontmatter(STEERING_NOTE_TEMPLATE)
        assert fm.get("artifact_type") == "steering_note"

    def test_has_required_sections(self):
        content = STEERING_NOTE_TEMPLATE.read_text(encoding="utf-8")
        for section in (
            "## Purpose",
            "## Concerns for HQ Triage",
            "## Decisions Already Made",
            "## Carry-Over Open Items",
            "## Next Action",
        ):
            assert section in content, f"steering-note template missing {section}"


# ---------------------------------------------------------------------------
# Progress Digest template
# ---------------------------------------------------------------------------

class TestProgressDigestTemplate:
    def test_exists(self):
        assert PROGRESS_DIGEST_TEMPLATE.exists(), (
            "governance/templates/progress-digest.md not found"
        )

    def test_has_required_frontmatter_fields(self):
        fm = parse_frontmatter(PROGRESS_DIGEST_TEMPLATE)
        missing = [f for f in PROGRESS_DIGEST_FIELDS if f not in fm]
        assert not missing, f"progress-digest template missing fields: {missing}"

    def test_artifact_type(self):
        fm = parse_frontmatter(PROGRESS_DIGEST_TEMPLATE)
        assert fm.get("artifact_type") == "progress_digest"

    def test_has_four_required_sections(self):
        content = PROGRESS_DIGEST_TEMPLATE.read_text(encoding="utf-8")
        missing = [s for s in PROGRESS_DIGEST_SECTIONS if s not in content]
        assert not missing, f"progress-digest template missing sections: {missing}"

    def test_has_exactly_four_h2_sections(self):
        # The spec mandates "no more, no fewer" than four sections.
        content = PROGRESS_DIGEST_TEMPLATE.read_text(encoding="utf-8")
        h2 = re.findall(r"^## .+$", content, flags=re.MULTILINE)
        assert len(h2) == 4, f"progress-digest must have exactly 4 sections, found {len(h2)}: {h2}"


# ---------------------------------------------------------------------------
# Bouncer Work Log template
# ---------------------------------------------------------------------------

class TestBouncerWorkLogTemplate:
    def test_exists(self):
        assert BOUNCER_WORK_LOG_TEMPLATE.exists(), (
            "governance/templates/bouncer-work-log.md not found"
        )

    def test_has_required_frontmatter_fields(self):
        fm = parse_frontmatter(BOUNCER_WORK_LOG_TEMPLATE)
        missing = [f for f in BOUNCER_WORK_LOG_FIELDS if f not in fm]
        assert not missing, f"bouncer-work-log template missing fields: {missing}"

    def test_artifact_type(self):
        fm = parse_frontmatter(BOUNCER_WORK_LOG_TEMPLATE)
        assert fm.get("artifact_type") == "bouncer_work_log"

    def test_has_four_body_fields(self):
        content = BOUNCER_WORK_LOG_TEMPLATE.read_text(encoding="utf-8")
        for field in (
            "**What happened:**",
            "**What I did:**",
            "**Side effects:**",
            "**Pattern flag:**",
        ):
            assert field in content, f"bouncer-work-log template missing {field}"


# ---------------------------------------------------------------------------
# Reference Steering Note validates against the schema
# ---------------------------------------------------------------------------

class TestReferenceSteeringNote:
    def test_exists(self):
        assert REFERENCE_STEERING_NOTE.exists(), (
            "reference Steering Note 2026-06-19 not found"
        )

    def test_validates_against_schema(self):
        fm = parse_frontmatter(REFERENCE_STEERING_NOTE)
        missing = [f for f in STEERING_NOTE_FIELDS if f not in fm]
        assert not missing, f"reference Steering Note missing fields: {missing}"
        assert fm.get("artifact_type") == "steering_note"

    def test_concerns_have_required_keys(self):
        fm = parse_frontmatter(REFERENCE_STEERING_NOTE)
        assert isinstance(fm.get("concerns"), list) and fm["concerns"]
        valid_severities = {"critical", "high", "medium", "low"}
        for concern in fm["concerns"]:
            assert {"id", "severity", "title"} <= set(concern.keys()), (
                f"concern missing required keys: {concern}"
            )
            assert concern["severity"] in valid_severities, (
                f"invalid severity: {concern['severity']}"
            )

    def test_decisions_is_nonempty_list(self):
        fm = parse_frontmatter(REFERENCE_STEERING_NOTE)
        assert isinstance(fm.get("decisions"), list) and fm["decisions"]


# ---------------------------------------------------------------------------
# Creation Chat guide
# ---------------------------------------------------------------------------

class TestCreationChatGuide:
    def test_exists(self):
        assert CREATION_CHAT_GUIDE.exists(), (
            "governance/systems/creation-chat-guide.md not found"
        )

    def test_documents_reinstantiation_ritual(self):
        content = CREATION_CHAT_GUIDE.read_text(encoding="utf-8")
        assert "Re-instantiation Ritual" in content
        # Four ritual steps must be present.
        for step in ("Step 1", "Step 2", "Step 3", "Step 4"):
            assert step in content, f"creation-chat-guide missing {step}"

    def test_documents_guidance_sections(self):
        content = CREATION_CHAT_GUIDE.read_text(encoding="utf-8")
        assert "When to Write a Steering Note" in content
        assert "When to Expect a Progress Digest" in content
        assert "Bouncer Work Log" in content

    def test_documents_cfo_review_gate(self):
        content = CREATION_CHAT_GUIDE.read_text(encoding="utf-8")
        assert "CFO PR Review Gate" in content
        assert "cfo_review_gate" in content
        # Both gate states must be documented.
        assert "enabled" in content and "disabled" in content


# ---------------------------------------------------------------------------
# CFO PR review gate (Constraint 2)
# ---------------------------------------------------------------------------

class TestCfoReviewGate:
    def test_progress_digest_surfaces_merge_ready_prs(self):
        # Open Decisions must surface merge-ready PRs awaiting CFO review.
        content = PROGRESS_DIGEST_TEMPLATE.read_text(encoding="utf-8")
        assert "cfo_review_gate" in content or "CFO" in content
        assert "merge-ready" in content.lower() or "merge review" in content.lower()

    def test_ai_project_yml_has_gate_setting(self):
        config = yaml.safe_load(AI_PROJECT_YML.read_text(encoding="utf-8"))
        assert config.get("cfo_review_gate") in {"enabled", "disabled"}, (
            f".ai-project.yml cfo_review_gate must be enabled|disabled, "
            f"got: {config.get('cfo_review_gate')}"
        )


# ---------------------------------------------------------------------------
# Visual artifacts config layer (Epic P5-M22-E22.1, VA-1; default-on flip P7-M27-E27.1)
# ---------------------------------------------------------------------------

class TestVisualArtifactsRepoConfig:
    def test_ai_project_yml_carries_visual_artifacts_disabled(self):
        # This repo opts the capability OFF via the explicit enabled: false opt-out
        # (default-on flip, E27.1). Kept disabled because bin/ai-project-visual's
        # --type diagrams is a ComfyUI-generative call, not an endpoint-free
        # structural diagram, so enabling here would require a live endpoint the
        # suite doesn't have (verified: un-skips test_helper_generates_against_endpoint).
        config = yaml.safe_load(AI_PROJECT_YML.read_text(encoding="utf-8"))
        va = config.get("visual_artifacts")
        assert isinstance(va, dict), (
            f".ai-project.yml must carry a visual_artifacts block, got: {va!r}"
        )
        assert va.get("enabled") is False, (
            f".ai-project.yml visual_artifacts.enabled must be false, got: {va.get('enabled')!r}"
        )
