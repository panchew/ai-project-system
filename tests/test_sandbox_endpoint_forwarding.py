"""Guards the sandbox → host inference seam (Bugfix B2.1).

``run_in_sandbox()`` forwarded exactly one environment variable, so a sandboxed
agentic/local dispatch met a container-local ``localhost:11434`` that answers
nothing and exited class 5 before doing any work. The gap was documented on
2026-07-12 (P7-M26-E26.3) and worked around per-epic for three weeks because
**nothing asserted the seam** — which is what this file is for. The durable part
of B2.1 is not the ``-e`` flag; it is that removing the flag now fails the suite.

The tests load the extensionless ``bin/ai-project-orchestrator`` as a module,
mirroring tests/test_visual_artifacts_config.py, and inspect the ``docker run``
argv the function builds. No container is started here; the live end-to-end
demonstration is tests/integration/test_sandbox_ollama_reachability.py.
"""

import importlib.util
from importlib.machinery import SourceFileLoader
from pathlib import Path
from unittest.mock import MagicMock

import pytest


REPO_ROOT = Path(__file__).resolve().parent.parent
ORCH_PATH = REPO_ROOT / "bin" / "ai-project-orchestrator"
DOCKERFILE_SANDBOX = REPO_ROOT / "Dockerfile.sandbox"


def _load_orchestrator():
    """Load the extensionless ``bin/ai-project-orchestrator`` script as a module."""
    loader = SourceFileLoader("ai_project_orchestrator_b21", str(ORCH_PATH))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


orch = _load_orchestrator()

# The environment variables that decide what run_in_sandbox() forwards. Every test
# starts from a known-clean slate so a developer's own shell cannot mask a defect.
CONTROLLING_VARS = (
    "AI_PROJECT_OLLAMA_ENDPOINT",
    "LOCAL_AGENT_RUNNER",
    "AI_PROJECT_SANDBOX_GATEWAY",
)


@pytest.fixture
def docker_argv(monkeypatch):
    """Return a callable that runs run_in_sandbox() and hands back the docker argv."""
    for var in CONTROLLING_VARS:
        monkeypatch.delenv(var, raising=False)

    captured = {}

    def fake_run(cmd, *args, **kwargs):
        captured["cmd"] = cmd
        return MagicMock(returncode=0, stdout="", stderr="")

    monkeypatch.setattr(orch.subprocess, "run", fake_run)

    def invoke(image="mock-image", command="test-cmd", active_model="local:mock"):
        orch.run_in_sandbox(image, command, active_model)
        return captured["cmd"]

    return invoke


def _env_values(argv, name):
    """Every ``-e NAME=value`` value present in a docker argv, in order."""
    prefix = f"{name}="
    return [
        argv[i + 1][len(prefix):]
        for i, arg in enumerate(argv[:-1])
        if arg == "-e" and argv[i + 1].startswith(prefix)
    ]


# ---------------------------------------------------------------------------
# The forwarding itself — the regression these tests exist to catch
# ---------------------------------------------------------------------------

class TestEndpointForwarding:
    def test_endpoint_is_forwarded_even_when_unset_in_the_environment(self, docker_argv):
        assert _env_values(docker_argv(), "AI_PROJECT_OLLAMA_ENDPOINT")

    def test_forwarded_endpoint_is_never_the_containers_own_loopback(self, docker_argv):
        """The defect in one assertion: a loopback endpoint inside the container is severed."""
        endpoint = _env_values(docker_argv(), "AI_PROJECT_OLLAMA_ENDPOINT")[0]
        host = orch.urlparse(endpoint).hostname
        assert host is not None
        assert host.lower() not in orch.LOOPBACK_HOSTNAMES

    def test_host_endpoint_is_honoured_and_its_port_preserved(self, docker_argv, monkeypatch):
        monkeypatch.setenv("AI_PROJECT_OLLAMA_ENDPOINT", "http://localhost:9999")
        endpoint = _env_values(docker_argv(), "AI_PROJECT_OLLAMA_ENDPOINT")[0]
        assert orch.urlparse(endpoint).port == 9999

    def test_a_routable_endpoint_is_forwarded_unchanged(self, docker_argv, monkeypatch):
        """An endpoint already naming a reachable host is correct as written."""
        monkeypatch.setenv("AI_PROJECT_OLLAMA_ENDPOINT", "http://inference.internal:11434")
        assert _env_values(docker_argv(), "AI_PROJECT_OLLAMA_ENDPOINT") == [
            "http://inference.internal:11434"
        ]

    def test_active_model_is_still_forwarded(self, docker_argv):
        """B2.1 adds forwarding; it must not displace what was already there."""
        assert _env_values(docker_argv(active_model="local:qwen3-coder:30b"),
                           "AI_PROJECT_ACTIVE_MODEL") == ["local:qwen3-coder:30b"]


class TestRunnerOverrideForwarding:
    def test_forwarded_when_set(self, docker_argv, monkeypatch):
        monkeypatch.setenv("LOCAL_AGENT_RUNNER", "/opt/bin/local-agent-runner")
        assert _env_values(docker_argv(), "LOCAL_AGENT_RUNNER") == ["/opt/bin/local-agent-runner"]

    def test_absent_when_unset(self, docker_argv):
        assert _env_values(docker_argv(), "LOCAL_AGENT_RUNNER") == []

    def test_absent_when_set_but_empty(self, docker_argv, monkeypatch):
        """bin/run-dev-agent reads an empty override as unset; the argv must agree."""
        monkeypatch.setenv("LOCAL_AGENT_RUNNER", "   ")
        assert _env_values(docker_argv(), "LOCAL_AGENT_RUNNER") == []


# ---------------------------------------------------------------------------
# The gateway is derived or configured — never written down
# ---------------------------------------------------------------------------

class TestGatewayIsNotHardCoded:
    def test_source_contains_no_literal_bridge_address(self):
        """172.17.0.1 is this host's measurement, not a fact about Docker."""
        assert "172.17.0.1" not in ORCH_PATH.read_text()

    def test_default_gateway_is_resolved_by_docker_not_by_us(self, docker_argv):
        argv = docker_argv()
        assert "--add-host" in argv
        assert argv[argv.index("--add-host") + 1] == f"{orch.DEFAULT_SANDBOX_GATEWAY}:host-gateway"

    def test_gateway_is_configurable(self, docker_argv, monkeypatch):
        monkeypatch.setenv("AI_PROJECT_SANDBOX_GATEWAY", "docker-host.example")
        endpoint = _env_values(docker_argv(), "AI_PROJECT_OLLAMA_ENDPOINT")[0]
        assert orch.urlparse(endpoint).hostname == "docker-host.example"

    def test_a_literal_gateway_address_emits_no_add_host(self, docker_argv, monkeypatch):
        """``--add-host 172.17.0.1:host-gateway`` is not a thing docker accepts."""
        monkeypatch.setenv("AI_PROJECT_SANDBOX_GATEWAY", "172.17.0.1")
        argv = docker_argv()
        assert "--add-host" not in argv
        assert _env_values(argv, "AI_PROJECT_OLLAMA_ENDPOINT") == ["http://172.17.0.1:11434"]

    def test_every_flag_precedes_the_image(self, docker_argv, monkeypatch):
        """docker treats anything after the image as the command, silently."""
        monkeypatch.setenv("LOCAL_AGENT_RUNNER", "/opt/bin/local-agent-runner")
        argv = docker_argv(image="mock-image")
        image_at = argv.index("mock-image")
        for flag in ("--add-host", "-e", "-v", "-w"):
            assert argv.index(flag) < image_at


# ---------------------------------------------------------------------------
# Route B.2 stays out — HQ Ruling 2026-08-06, Decision 5
# ---------------------------------------------------------------------------

class TestNoEngineInTheImage:
    def test_dockerfile_installs_no_inference_engine(self):
        text = DOCKERFILE_SANDBOX.read_text().lower()
        for engine in ("local-agent-runner", "ollama", "opencode", "llama.cpp", "llama-cpp"):
            assert engine not in text, f"Dockerfile.sandbox installs {engine} — Route B.2 is declined"
