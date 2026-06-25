"""Guard: the starter templates verify prerequisites via git-tracking, not disk.

Epic P5-M20-E20.1 — Prerequisite git-tracking verification (GH-1).

Background
----------
During M19 a prerequisite artifact was declared "✅ committed" in a spec but was
in fact untracked in git. The Stage 1 prerequisite check verified only that the
file existed on the working-tree disk; a fresh worktree clone would have lacked
the artifact entirely. Disk presence is not proof of commit.

To close that gap, the Milestone and Epic Execution Chat Starter templates must
instruct the reader to verify a prerequisite with ``git ls-files
--error-unmatch <path>`` on the expected branch, not a disk-existence check.
This test asserts that the literal verification command is present in both
templates so the hardened wording cannot silently regress.

If this test fails: open the named template and restore the prerequisite
git-tracking verification instruction (the literal ``git ls-files
--error-unmatch`` command) in the section noted below.
"""

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = REPO_ROOT / "governance" / "templates"

VERIFICATION_COMMAND = "git ls-files --error-unmatch"

# Each starter template that gates a downstream chat on a prerequisite artifact.
PREREQUISITE_TEMPLATES = (
    TEMPLATES / "milestone-execution-chat-starter.md",
    TEMPLATES / "epic-execution-chat-starter.md",
)


@pytest.mark.parametrize(
    "template", PREREQUISITE_TEMPLATES, ids=lambda p: p.name
)
def test_template_exists(template):
    """Sanity: the template file is present (guards against a path slip)."""
    assert template.is_file(), f"Expected starter template at {template}"


@pytest.mark.parametrize(
    "template", PREREQUISITE_TEMPLATES, ids=lambda p: p.name
)
def test_template_uses_git_tracking_verification(template):
    """Each starter must instruct the literal git-tracking verification command."""
    text = template.read_text()
    assert VERIFICATION_COMMAND in text, (
        f"{template.relative_to(REPO_ROOT)} is missing the prerequisite "
        f"git-tracking verification command '{VERIFICATION_COMMAND}'. "
        "Disk presence is not proof of commit — restore the git ls-files check."
    )
