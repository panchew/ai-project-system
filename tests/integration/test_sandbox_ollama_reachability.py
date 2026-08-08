"""End-to-end proof of the B2.1 seam: the sandbox reaches the host's Ollama.

tests/test_sandbox_endpoint_forwarding.py asserts the argv ``run_in_sandbox()``
builds. That is the durable guard, and it runs everywhere. This file starts a real
container and asks the real endpoint, because the argv being right is not the same
claim as the packet arriving — B2.1 exists because a verification was performed at
the host layer for code that executes inside the sandbox (P11-GH-2).

Both requirements — a Docker daemon with the sandbox image, and a host Ollama that
answers — are genuine environment facts, so this module skips where they are absent
rather than asserting something it cannot observe. It is **not** a route-around for
the forwarding guard: the unit tests above cover that unconditionally.
"""

import importlib.util
import shutil
import subprocess
import urllib.error
import urllib.request
from importlib.machinery import SourceFileLoader
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[2]
ORCH_PATH = REPO_ROOT / "bin" / "ai-project-orchestrator"
SANDBOX_IMAGE = "ai-project-sandbox:latest"

PROBE = 'curl -s -o /dev/null -w "%{http_code}" "$AI_PROJECT_OLLAMA_ENDPOINT/api/tags"'


def _load_orchestrator():
    loader = SourceFileLoader("ai_project_orchestrator_b21_live", str(ORCH_PATH))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


orch = _load_orchestrator()


def _docker_image_present():
    if shutil.which("docker") is None:
        return False
    try:
        result = subprocess.run(
            ["docker", "image", "inspect", SANDBOX_IMAGE],
            capture_output=True, timeout=30,
        )
    except (OSError, subprocess.SubprocessError):
        return False
    return result.returncode == 0


def _host_ollama_answers():
    endpoint = orch.DEFAULT_OLLAMA_ENDPOINT
    try:
        with urllib.request.urlopen(f"{endpoint}/api/tags", timeout=5) as response:
            return response.status == 200
    except (urllib.error.URLError, OSError):
        return False


pytestmark = [
    pytest.mark.skipif(not _docker_image_present(),
                       reason=f"no Docker daemon or {SANDBOX_IMAGE} not built"),
    pytest.mark.skipif(not _host_ollama_answers(),
                       reason="no Ollama answering on the host's default endpoint"),
]


def test_sandboxed_dispatch_reaches_the_hosts_ollama():
    """The DoD line: from inside the sandbox, the forwarded endpoint returns HTTP 200."""
    code, stdout, stderr = orch.run_in_sandbox(
        SANDBOX_IMAGE, PROBE, active_model="local:qwen3-coder:30b"
    )
    assert code == 0, stderr
    assert stdout.strip() == "200", (
        f"sandbox got HTTP {stdout.strip()!r} from the forwarded endpoint; "
        "000 means the container is severed from the host again"
    )


def test_the_container_still_cannot_reach_its_own_loopback(monkeypatch):
    """Negative control: the 000 this bugfix was filed for is still 000 unforwarded.

    Without it, a green test above proves only that *something* answered — it could
    equally mean an engine had been installed into the image, which Decision 5
    declines. This pins the improvement to the forwarding.
    """
    # curl exits 7 (could not connect) here rather than 0 — that, with the 000, is
    # the failure signal itself, so neither is asserted as success.
    _, stdout, _ = orch.run_in_sandbox(
        SANDBOX_IMAGE,
        'curl -s -o /dev/null -w "%{http_code}" "http://localhost:11434/api/tags"',
        active_model="local:qwen3-coder:30b",
    )
    assert stdout.strip() == "000"
