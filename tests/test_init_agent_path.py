"""Tests for the HQ agent install path written by `bin/ai-project-init`.

Epic P6-M25-E25.3 — Align `ai-project-init` agent path (P6-GH-11).

P5 established `.ai-project/agents/` as the canonical, tool-neutral agent
location. `bin/ai-project-init` previously wrote `.github/agents/` instead,
disagreeing with the framework's own docs. This test guards the fix: the
initializer must write the HQ agent to the canonical path.
"""

import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INIT_SCRIPT = REPO_ROOT / "bin" / "ai-project-init"


def test_init_writes_canonical_agent_path(tmp_path):
    """`ai-project-init` installs the HQ agent at `.ai-project/agents/hq.agent.md`."""
    result = subprocess.run(
        ["bash", str(INIT_SCRIPT), "test-proj",
         "--dir", str(tmp_path), "--skip-git", "--skip-submodule"],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stderr

    project_dir = tmp_path / "test-proj"
    canonical_agent = project_dir / ".ai-project" / "agents" / "hq.agent.md"
    assert canonical_agent.is_file()
    assert canonical_agent.stat().st_size > 0

    # The old GitHub-specific path must not be written (Option A: canonical-only).
    assert not (project_dir / ".github" / "agents").exists()
