"""Integration test for ``bin/ai-project-visual`` (Epic P5-M22-E22.2, VA-1).

Exercises the ComfyUI helper. As of Epic P8-M29-E29.2, this repo's own
``visual_artifacts.enabled`` is ``true`` and ``test_helper_generates_against_endpoint`` runs
for real against the live local ComfyUI endpoint by default — it is not skipped unless a
contributor explicitly opts out. A contributor/agent running on a machine without ComfyUI
reachable at ``http://localhost:8188`` should set ``AI_PROJECT_SKIP_LIVE_ENDPOINT_TESTS=1``
to skip that one test; the default (unset) still runs and requires the endpoint, preserving
this repo's suite-green-with-a-real-call bar. Gate/configuration behaviour that needs no
endpoint is asserted deterministically and is unaffected by either flag.

The effective config is read through E22.1's single source —
``bin/ai-project-orchestrator``'s ``load_yml_config`` / ``resolve_visual_artifacts`` —
loaded via ``SourceFileLoader``, mirroring tests/test_visual_artifacts_config.py.
"""

import importlib.util
import os
import subprocess
import sys
from importlib.machinery import SourceFileLoader
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
ORCH_PATH = REPO_ROOT / "bin" / "ai-project-orchestrator"
HELPER_PATH = REPO_ROOT / "bin" / "ai-project-visual"
REPO_YML = REPO_ROOT / ".ai-project.yml"


def _load_orchestrator():
    loader = SourceFileLoader("ai_project_orchestrator_helper_it", str(ORCH_PATH))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


def _effective_repo_config():
    """Effective visual_artifacts config for the repo's .ai-project.yml (cwd-independent)."""
    orch = _load_orchestrator()
    orch.YML_CONFIG = REPO_YML
    return orch.load_yml_config()["visual_artifacts"]


def _run_helper(args, cwd):
    """Run the helper as a subprocess; cwd selects which .ai-project.yml it reads."""
    return subprocess.run(
        [sys.executable, str(HELPER_PATH), *args],
        cwd=str(cwd),
        capture_output=True,
        text=True,
    )


def _write_yml(directory, body):
    (directory / ".ai-project.yml").write_text(body, encoding="utf-8")


# Read once at collection time; drives the skip decision for the endpoint test.
REPO_VA = _effective_repo_config()

# Opt-OUT only (P8-M29-E29.2): a contributor without a reachable ComfyUI endpoint sets this
# to skip test_helper_generates_against_endpoint explicitly. Unset (the default) still runs
# and requires the live endpoint — an opt-in-to-run default would just be the old
# skip-by-default behaviour renamed, which the Hard Constraint forbids.
_SKIP_LIVE_ENDPOINT = os.environ.get("AI_PROJECT_SKIP_LIVE_ENDPOINT_TESTS", "") not in ("", "0")


@pytest.mark.skipif(
    not REPO_VA.get("enabled"),
    reason="visual_artifacts.enabled is false (repo default); no live ComfyUI endpoint to exercise.",
)
@pytest.mark.skipif(
    _SKIP_LIVE_ENDPOINT,
    reason="AI_PROJECT_SKIP_LIVE_ENDPOINT_TESTS is set; contributor opted out of the live "
           "ComfyUI endpoint call (see module docstring).",
)
def test_helper_generates_against_endpoint(tmp_path):
    """With the capability enabled, the helper writes a non-empty artifact from the
    configured endpoint. Runs for real by default; skip explicitly via
    AI_PROJECT_SKIP_LIVE_ENDPOINT_TESTS=1 on a machine without a reachable endpoint."""
    vtype = (REPO_VA.get("types") or ["diagrams"])[0]
    out = tmp_path / "out.png"
    result = _run_helper(
        ["--prompt", "integration smoke test", "--type", vtype,
         "--output", str(out), "--timeout", "180"],
        cwd=REPO_ROOT,
    )
    assert result.returncode == 0, f"helper failed: {result.stderr}"
    assert out.exists() and out.stat().st_size > 0


def test_helper_exits_clearly_when_disabled(tmp_path):
    """Disabled capability ⇒ exit 2 and a clear message; never a crash. Needs no endpoint."""
    _write_yml(tmp_path, "visual_artifacts:\n  enabled: false\n")
    result = _run_helper(
        ["--prompt", "x", "--type", "diagrams", "--output", str(tmp_path / "o.png")],
        cwd=tmp_path,
    )
    assert result.returncode == 2
    assert "disabled" in result.stderr.lower()


def test_helper_rejects_unconfigured_type(tmp_path):
    """A --type outside the configured types ⇒ configuration error (exit 3). Needs no endpoint."""
    _write_yml(
        tmp_path,
        "visual_artifacts:\n"
        "  enabled: true\n"
        "  comfyui_url: http://localhost:8188\n"
        "  types:\n"
        "    - diagrams\n",
    )
    result = _run_helper(
        ["--prompt", "x", "--type", "video", "--output", str(tmp_path / "o.mp4")],
        cwd=tmp_path,
    )
    assert result.returncode == 3
    assert "video" in result.stderr


# --- Execution-lock guardrail (E27.3, GPU coexistence) -----------------------------
#
# `--comfyui-url` deliberately points at a closed port (127.0.0.1:1, TCPMUX — never
# bound by ComfyUI or anything else) rather than 8188: this host's own ai-stack may
# have a real ComfyUI listening on 8188 (the exact contention this Epic documents), and
# these tests must stay deterministic without depending on whether that stack happens
# to be running. A closed port gives a fast, reliable "connection refused" (exit 4)
# once the guardrail lets a call through, distinguishing "not locked" from "locked".

_UNREACHABLE_YML = (
    "visual_artifacts:\n"
    "  enabled: true\n"
    "  comfyui_url: http://127.0.0.1:1\n"
    "  types:\n"
    "    - diagrams\n"
)


def _write_lock(directory, pid):
    lock_dir = directory / ".ai-project" / "locks"
    lock_dir.mkdir(parents=True, exist_ok=True)
    (lock_dir / "execution.lock").write_text(str(pid), encoding="utf-8")


def _dead_pid():
    """Spawn and reap a short-lived subprocess; its PID is dead by the time it's used."""
    proc = subprocess.Popen([sys.executable, "-c", "pass"])
    proc.wait()
    return proc.pid


def test_helper_refused_when_execution_lock_live(tmp_path):
    """A live PID in .ai-project/locks/execution.lock ⇒ refused before any generative
    call: exit 5, clear message. Uses this test process's own (necessarily live) PID."""
    _write_yml(tmp_path, _UNREACHABLE_YML)
    _write_lock(tmp_path, os.getpid())
    result = _run_helper(
        ["--prompt", "x", "--type", "diagrams", "--output", str(tmp_path / "o.png"),
         "--timeout", "2"],
        cwd=tmp_path,
    )
    assert result.returncode == 5
    assert "locked" in result.stderr.lower() or "execution" in result.stderr.lower()


def test_helper_proceeds_when_execution_lock_stale(tmp_path):
    """A dead PID in the lock file ⇒ stale-lock handling matches the orchestrator's own:
    not falsely blocked, proceeds to attempt generation (exit 4, unreachable endpoint)."""
    _write_yml(tmp_path, _UNREACHABLE_YML)
    _write_lock(tmp_path, _dead_pid())
    result = _run_helper(
        ["--prompt", "x", "--type", "diagrams", "--output", str(tmp_path / "o.png"),
         "--timeout", "2"],
        cwd=tmp_path,
    )
    assert result.returncode != 5
    assert result.returncode == 4


def test_helper_proceeds_when_execution_lock_absent(tmp_path):
    """No lock file at all ⇒ not blocked; proceeds to attempt generation (exit 4,
    unreachable endpoint)."""
    _write_yml(tmp_path, _UNREACHABLE_YML)
    result = _run_helper(
        ["--prompt", "x", "--type", "diagrams", "--output", str(tmp_path / "o.png"),
         "--timeout", "2"],
        cwd=tmp_path,
    )
    assert result.returncode != 5
    assert result.returncode == 4
