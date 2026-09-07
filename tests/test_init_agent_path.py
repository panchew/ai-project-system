"""Tests for the HQ agent install path written by `bin/ai-project-init`.

Epic P6-M25-E25.3 — Align `ai-project-init` agent path (P6-GH-11).
Inverted by Epic P12-M42-E42.4 — `ai-project-init` stops manufacturing an agent
(P12-GH-2, severity High).

P5 established `.ai-project/agents/` as the canonical, tool-neutral agent
location, and P6-GH-11 moved `bin/ai-project-init`'s write there from
`.github/agents/`. That coverage survives this inversion.

The pre-E42.4 test invoked the script with `--skip-submodule` and asserted the
resulting file exists, is non-empty, and begins with `#` — the same three
properties the 230-byte "Milestone M8" placeholder the script manufactured
trivially satisfied. The branch that would fail was unreachable under its own
invocation. After the inversion the suite must fail if a placeholder agent is
installable at all (P12-GH-2), and must still fail if the `.github/agents/` path
regresses (P6-GH-11).
"""

import shlex
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INIT_SCRIPT = REPO_ROOT / "bin" / "ai-project-init"

# The historical placeholder the script manufactured (P12-GH-2): readable,
# non-empty, header-shaped — the properties a substitute trivially has, but it is
# NOT the governance agent.
M8_PLACEHOLDER = """\
# HQ Chat Agent

This agent is under development in Milestone M8.

For now, use this as a placeholder for the governance-aware HQ Chat agent.

When M8 is complete, this file will be replaced with the full HQ agent implementation.
"""


def _init_run(tmp_path):
    return subprocess.run(
        ["bash", str(INIT_SCRIPT), "test-proj",
         "--dir", str(tmp_path), "--skip-git", "--skip-submodule"],
        capture_output=True, text=True,
    )


def test_init_aborts_when_governance_agent_absent(tmp_path):
    """Inversion of the pre-E42.4 assertions: an init with no governance agent must
    FAIL with a stated reason. The placeholder is not installable — the old test's
    three assertions (exists, non-empty, starts with '#') recorded the defect as
    correct."""
    result = _init_run(tmp_path)
    assert result.returncode != 0, (
        "an init without a governance agent must fail (fail-closed), got rc=0 with "
        f"stdout={result.stdout!r}"
    )
    assert "governance agent" in result.stderr.lower(), result.stderr

    project_dir = tmp_path / "test-proj"
    # No placeholder may exist at the canonical agents path.
    assert not (project_dir / ".ai-project" / "agents" / "governance.agent.md").exists()
    # P6-GH-11: the old GitHub-specific path must not be created either.
    assert not (project_dir / ".github" / "agents").exists()


def test_install_hq_agent_located_real_agent(tmp_path):
    """The corrected source path (D1) resolves the real agent from a real submodule
    layout and installs it at the canonical `.ai-project/agents/` path (P6-GH-11).
    Seeding `.governance/governance/agents/governance.agent.md` mirrors what the
    submodule clone produces — the whole repository cloned under `.governance/`."""
    project_dir = tmp_path / "test-proj"
    seeded_agent = (
        project_dir / ".governance" / "governance" / "agents" / "governance.agent.md"
    )
    seeded_agent.parent.mkdir(parents=True)
    real_agent = (REPO_ROOT / "governance" / "agents" / "governance.agent.md").read_text()
    seeded_agent.write_text(real_agent)

    result = subprocess.run(
        ["bash", "-c",
         f"source {shlex.quote(str(INIT_SCRIPT))} && "
         f"install_hq_agent {shlex.quote(str(project_dir))}"],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stderr

    dest = project_dir / ".ai-project" / "agents" / "governance.agent.md"
    assert dest.is_file()
    assert dest.read_text() == real_agent
    # P6-GH-11: the old GitHub-specific path must not be written.
    assert not (project_dir / ".github" / "agents").exists()


def test_install_hq_agent_rejects_placeholder(tmp_path):
    """The strengthened validator (D3) rejects the historical placeholder: a file
    that is readable, non-empty and header-shaped but is not the governance agent
    must not be installable."""
    project_dir = tmp_path / "test-proj"
    seeded = project_dir / ".governance" / "governance" / "agents" / "governance.agent.md"
    seeded.parent.mkdir(parents=True)
    seeded.write_text(M8_PLACEHOLDER)

    result = subprocess.run(
        ["bash", "-c",
         f"source {shlex.quote(str(INIT_SCRIPT))} && "
         f"install_hq_agent {shlex.quote(str(project_dir))}"],
        capture_output=True, text=True,
    )
    assert result.returncode != 0
    assert "governance agent" in result.stderr.lower(), result.stderr
    # Nothing is installed.
    assert not (project_dir / ".ai-project" / "agents" / "governance.agent.md").exists()


def test_no_placeholder_branch_in_script():
    """The stub branch is unreachable because it does not exist: the script source
    no longer carries the placeholder's distinctive body marker (the anchor the
    P12-GH-2 note cites)."""
    source = (REPO_ROOT / "bin" / "ai-project-init").read_text()
    assert "This agent is under development in Milestone M8" not in source


def test_agent_source_path_matches_submodule_layout():
    """The source path and the submodule path are one coupled decision (D1+D4):
    the agent resolves at <project>/.governance/governance/agents/, and the
    submodule_path written to .ai-project.yml matches the fleet's `.governance`
    convention — never the one-governance-level-short path."""
    source = (REPO_ROOT / "bin" / "ai-project-init").read_text()
    assert 'GOVERNANCE_SUBMODULE_PATH=".governance"' in source
    assert "$GOVERNANCE_SUBMODULE_PATH/governance/agents/governance.agent.md" in source
    assert "submodule_path: $GOVERNANCE_SUBMODULE_PATH/" in source
    assert "submodule_path: governance/" not in source
    # The old one-level-short read must be gone.
    assert "$project_dir/governance/agents/governance.agent.md" not in source