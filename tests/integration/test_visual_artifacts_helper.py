"""Integration test for ``bin/ai-project-visual`` (Epic P5-M22-E22.2, VA-1).

Exercises the ComfyUI helper. The endpoint-generation test **skips** when
``visual_artifacts.enabled`` is ``false`` (the repo default) so the suite stays green with
no live ComfyUI instance. Gate/configuration behaviour that needs no endpoint is asserted
deterministically.

The effective config is read through E22.1's single source —
``bin/ai-project-orchestrator``'s ``load_yml_config`` / ``resolve_visual_artifacts`` —
loaded via ``SourceFileLoader``, mirroring tests/test_visual_artifacts_config.py.
"""

import importlib.util
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


@pytest.mark.skipif(
    not REPO_VA.get("enabled"),
    reason="visual_artifacts.enabled is false (repo default); no live ComfyUI endpoint to exercise.",
)
def test_helper_generates_against_endpoint(tmp_path):
    """With the capability enabled, the helper writes a non-empty artifact from the
    configured endpoint. SKIPPED at the repo default (enabled: false)."""
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
