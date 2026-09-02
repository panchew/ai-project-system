"""Guards the E42.1 fail-closed sandbox abort.

bin/ai-project-orchestrator ran a dispatched model's command unsandboxed on the
host (``subprocess.run(command, shell=True)``) when the Docker invocation raised
``FileNotFoundError`` -- isolation failing open, with the run record silent about
it. E42.1 removes that path and fails closed (``LOCAL_UNAVAILABLE_EXIT`` +
escalation report + trigger-file archive), and states what "Docker is available"
means so a daemon that is installed-but-not-running is its own fail-closed case
rather than a silent detour.

The guard lives here in ``tests/`` rather than the script's embedded suite,
because the milestone's stated invocation is ``PYTHONPATH=. pytest -q`` -- a
guard pytest does not collect is a guard the reviewer cannot see fail. The tests
load the extensionless ``bin/ai-project-orchestrator`` as a module, mirroring
tests/test_sandbox_endpoint_forwarding.py; no container is started.

Falsification (the milestone's Hard Constraint): replacing the
``raise SandboxUnavailable(...)`` in ``run_in_sandbox`` with the removed host
fallback makes test_host_shell_path_is_never_reached and
test_raises_sandbox_unavailable fail.
"""

import importlib.util
import json
from importlib.machinery import SourceFileLoader
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest


REPO_ROOT = Path(__file__).resolve().parent.parent
ORCH_PATH = REPO_ROOT / "bin" / "ai-project-orchestrator"


def _load_orchestrator():
    loader = SourceFileLoader("ai_project_orchestrator_e421", str(ORCH_PATH))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


orch = _load_orchestrator()


def _docker_only_file_not_found(cmd, *args, **kwargs):
    """subprocess.run replacement: the docker argv (a list) raises FileNotFoundError
    as the real binary does; any other invocation (the removed host fallback) would
    succeed -- so a test that expects no fallback call observes the difference."""
    if isinstance(cmd, list) and "docker" in cmd:
        raise FileNotFoundError(f"[Errno 2] No such file or directory: '{cmd[0]}'")
    return MagicMock(returncode=0, stdout="", stderr="")


class TestDockerBinaryAbsent:
    def test_raises_sandbox_unavailable(self):
        with patch.object(orch.subprocess, "run", side_effect=_docker_only_file_not_found):
            with pytest.raises(orch.SandboxUnavailable) as exc:
                orch.run_in_sandbox("mock-image", "host-cmd", "mock-model")
        assert "Docker binary" in str(exc.value)
        assert "FileNotFoundError" in str(exc.value)

    def test_host_shell_path_is_never_reached(self):
        """The guard: Docker absent must NOT reach subprocess.run(command, shell=True).

        Only the docker argv call happens; no second, shell=True invocation ever
        runs the model's command unsandboxed on the host."""
        calls = []

        def recording_fake(cmd, *args, **kwargs):
            calls.append((cmd, kwargs))
            return _docker_only_file_not_found(cmd, *args, **kwargs)

        with patch.object(orch.subprocess, "run", side_effect=recording_fake):
            with pytest.raises(orch.SandboxUnavailable):
                orch.run_in_sandbox("mock-image", "host-cmd", "mock-model")

        assert len(calls) == 1
        cmd, kwargs = calls[0]
        assert isinstance(cmd, list)
        assert "docker" in cmd
        assert not kwargs.get("shell")


class TestDaemonNotRunning:
    def test_raises_with_distinct_reason(self):
        """A daemon installed but not running is a DIFFERENT failure from a missing
        binary: no FileNotFoundError, so it must be detected and fail closed on its
        own terms, never retried as an ordinary task failure."""
        def fake_run(cmd, *args, **kwargs):
            return MagicMock(
                returncode=1,
                stdout="",
                stderr="Cannot connect to the Docker daemon at "
                       "unix:///var/run/docker.sock. Is the docker daemon running?",
            )

        with patch.object(orch.subprocess, "run", side_effect=fake_run):
            with pytest.raises(orch.SandboxUnavailable) as exc:
                orch.run_in_sandbox("mock-image", "host-cmd", "mock-model")
        assert "daemon is not running" in str(exc.value)

    def test_ordinary_task_failure_is_not_a_daemon_outage(self):
        """Negative control: a genuine in-container command failure (arbitrary
        stderr, non-zero exit) is NOT a daemon outage and must NOT abort -- the
        Dev-QA retry loop owns that case."""
        def fake_run(cmd, *args, **kwargs):
            return MagicMock(
                returncode=1,
                stdout="",
                stderr="make: *** No rule to make target 'lint'.  Stop.",
            )

        with patch.object(orch.subprocess, "run", side_effect=fake_run):
            code, _out, _err = orch.run_in_sandbox("mock-image", "host-cmd", "mock-model")
        assert code == 1


class TestFailClosedDisposition:
    def test_docker_absent_produces_escalation_archive_and_exit5(self, tmp_path, monkeypatch):
        """The full G1 shape at the caller: reason stated, escalation report written,
        trigger file archived so the run is not silently retried, exit
        LOCAL_UNAVAILABLE_EXIT."""
        monkeypatch.setattr(orch, "PROJECT_ROOT", tmp_path)
        monkeypatch.setattr(orch, "QUEUE_DIR", tmp_path / ".ai-project" / "queue")
        orch.QUEUE_DIR.mkdir(parents=True, exist_ok=True)

        trigger = {
            "epic_id": "EPIC-E421-1",
            "sandbox_env": "mock-sandbox",
            "validation_command": "run-validation",
            "dev_command": "run-dev",
            "run_dev_initially": True,
        }
        trigger_file = orch.QUEUE_DIR / "04_epic.json"
        trigger_file.write_text(json.dumps(trigger))

        with patch.object(orch.subprocess, "run", side_effect=_docker_only_file_not_found):
            with patch.object(orch.sys, "exit", side_effect=SystemExit) as mock_exit:
                with pytest.raises(SystemExit):
                    orch.handle_epic_execution(trigger, orch.DEFAULT_MODELS)

        mock_exit.assert_called_once_with(orch.LOCAL_UNAVAILABLE_EXIT)
        assert not trigger_file.exists()
        archived = orch.QUEUE_DIR / "04_epic.json.failed"
        assert archived.exists()

        report = tmp_path / "docs" / "admin" / "escalation-report-EPIC-E421-1.md"
        assert report.exists()
        text = report.read_text()
        assert "status: sandbox-unavailable" in text
        assert "Sandbox Unavailable" in text
        assert "Docker binary" in text