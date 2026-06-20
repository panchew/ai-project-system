"""
Validation tests for the genesis template and the genesis walkthrough example.

Verifies (Epic P4-M18-E18.1):
- governance/templates/genesis.md has the required YAML front-matter schema
- The template defines all required sections
- The walkthrough example (examples/genesis-walkthrough/genesis.md) is complete
  (status: complete) with a non-empty project and matching schema
"""

import re
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).parent.parent
GENESIS_TEMPLATE = REPO_ROOT / "governance" / "templates" / "genesis.md"
GENESIS_WALKTHROUGH = REPO_ROOT / "examples" / "genesis-walkthrough" / "genesis.md"

REQUIRED_FRONTMATTER_FIELDS = [
    "type",
    "project",
    "created_by",
    "date",
    "phase_1_name",
    "status",
]

REQUIRED_SECTIONS = [
    "## Project Brief",
    "## HQ Context Packet",
    "## Phase 1 Scope",
    "## Creation Chat Decisions",
    "## Next Step",
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
# Genesis template
# ---------------------------------------------------------------------------

class TestGenesisTemplate:
    def test_genesis_template_exists(self):
        assert GENESIS_TEMPLATE.exists(), "governance/templates/genesis.md not found"

    def test_genesis_template_frontmatter_parses(self):
        fm = parse_frontmatter(GENESIS_TEMPLATE)
        assert isinstance(fm, dict) and fm, "genesis template front-matter failed to parse"

    def test_genesis_template_has_required_frontmatter_fields(self):
        fm = parse_frontmatter(GENESIS_TEMPLATE)
        missing = [f for f in REQUIRED_FRONTMATTER_FIELDS if f not in fm]
        assert not missing, f"genesis template missing front-matter fields: {missing}"

    def test_genesis_template_type_is_genesis(self):
        fm = parse_frontmatter(GENESIS_TEMPLATE)
        assert fm.get("type") == "genesis", (
            f"genesis template 'type' must be 'genesis', got: {fm.get('type')}"
        )

    def test_genesis_template_status_is_draft(self):
        fm = parse_frontmatter(GENESIS_TEMPLATE)
        assert fm.get("status") == "draft", (
            f"genesis template 'status' should default to 'draft', got: {fm.get('status')}"
        )

    def test_genesis_template_has_all_required_sections(self):
        content = GENESIS_TEMPLATE.read_text(encoding="utf-8")
        missing = [s for s in REQUIRED_SECTIONS if s not in content]
        assert not missing, f"genesis template missing sections: {missing}"

    def test_genesis_template_is_concise(self):
        # Non-functional requirement: readable in under 5 minutes (kept under 150 lines).
        line_count = len(GENESIS_TEMPLATE.read_text(encoding="utf-8").splitlines())
        assert line_count <= 150, (
            f"genesis template is {line_count} lines; keep it under 150 for readability"
        )


# ---------------------------------------------------------------------------
# Genesis walkthrough example
# ---------------------------------------------------------------------------

class TestGenesisWalkthrough:
    def test_genesis_walkthrough_exists(self):
        assert GENESIS_WALKTHROUGH.exists(), (
            "examples/genesis-walkthrough/genesis.md not found"
        )

    def test_genesis_walkthrough_frontmatter_valid(self):
        fm = parse_frontmatter(GENESIS_WALKTHROUGH)
        missing = [f for f in REQUIRED_FRONTMATTER_FIELDS if f not in fm]
        assert not missing, f"walkthrough genesis missing front-matter fields: {missing}"
        assert fm.get("type") == "genesis"

    def test_genesis_walkthrough_is_complete(self):
        fm = parse_frontmatter(GENESIS_WALKTHROUGH)
        assert fm.get("status") == "complete", (
            "walkthrough genesis must have 'status: complete' (it is finished evidence)"
        )
        assert fm.get("project"), "walkthrough genesis 'project' must not be empty"
        assert fm.get("phase_1_name"), "walkthrough genesis 'phase_1_name' must not be empty"

    def test_genesis_walkthrough_date_is_iso(self):
        fm = parse_frontmatter(GENESIS_WALKTHROUGH)
        assert re.match(r"^\d{4}-\d{2}-\d{2}$", str(fm.get("date"))), (
            f"walkthrough genesis 'date' must be ISO (YYYY-MM-DD), got: {fm.get('date')}"
        )

    def test_genesis_walkthrough_has_all_required_sections(self):
        content = GENESIS_WALKTHROUGH.read_text(encoding="utf-8")
        missing = [s for s in REQUIRED_SECTIONS if s not in content]
        assert not missing, f"walkthrough genesis missing sections: {missing}"

    def test_genesis_walkthrough_has_no_unfilled_placeholders(self):
        # A completed walkthrough must not contain template <placeholders>.
        content = GENESIS_WALKTHROUGH.read_text(encoding="utf-8")
        leftover = re.findall(r"<[a-z][^>]*>", content)
        assert not leftover, (
            f"walkthrough genesis still contains unfilled placeholders: {leftover}"
        )
