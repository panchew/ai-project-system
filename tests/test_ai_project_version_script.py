"""Proving-vehicle test for Epic P7-M26-E26.3-PROVE (P7-M26-E26.3).

Validates ``bin/ai-project-version``, the one artifact the real, non-mocked
orchestrator/qwen2.5-coder:14b loop is expected to produce end-to-end. Per the
Milestone Chat's amendment (Escalation Notice
``P7-M26-E26.3__escalation-notice__sandbox-and-tools-json-execution-adequacy.md``,
resolved 2026-07-12): the coding tool set available to the live run
(``write_file``/scoped ``run_command``/scoped ``git``) has no mechanism to set a
file's executable bit, so this test asserts no such thing — the script is invoked
as ``python3 bin/ai-project-version``, never ``./bin/ai-project-version``.

Before the live run, this test fails (the script does not exist yet) — the
validation gate is real, not rigged.
"""

import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT_PATH = REPO_ROOT / "bin" / "ai-project-version"
YML_PATH = REPO_ROOT / ".ai-project.yml"


def _expected_version():
    with open(YML_PATH, "r") as f:
        data = yaml.safe_load(f)
    return str(data["governance"]["version"])


def test_script_exists():
    assert SCRIPT_PATH.exists(), f"{SCRIPT_PATH} does not exist"


def test_script_prints_governance_version_and_exits_zero():
    result = subprocess.run(
        [sys.executable, str(SCRIPT_PATH)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"expected exit 0, got {result.returncode}; stderr={result.stderr!r}"
    )
    assert result.stdout.strip() == _expected_version()
