"""Contract tests for ``bin/run-dev-agent`` (Epic P7-M26-E26.1, CONTRACT §7 shim).

The runner is **stubbed** (a fake executable the tests control via the adapter's
``LOCAL_AGENT_RUNNER`` discovery override) — the live invocation is E26.3's job.
Covered here, per the Epic spec:

- ``local:`` prefix mapping, bare-tag passthrough, missing/empty env → config error
- Task construction: ``--task-text`` = the spec's Definition of Done, ``--context`` =
  the scoped spec (+ starter when present) and **never the governance corpus**,
  ``--tools`` = the coding set, ``--transcript`` = the epic's artifact path
- Exit-code passthrough for 0 / 2 / 3 / 4
- Transcript written under the documented artifact convention
- Absence guard: the adapter source never references the runner's terminating-text
  field (SN-3 binding constraint)

P9-M31-E31.2 adds the local-availability preflight (Hard Constraint 4): every
``local:``-prefixed model is checked against a real ``/api/tags`` endpoint before the
runner is invoked. ``ollama_stub`` below is a real, minimal Ollama stand-in (a loopback
HTTP server) so those tests are deterministic and hermetic — no dependency on a real
Ollama install. ``run_adapter`` points ``AI_PROJECT_OLLAMA_ENDPOINT`` at it by default;
tests exercising the local-unavailable path override that explicitly.
"""

import http.server
import json
import os
import socket
import stat
import subprocess
import sys
import threading
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
ADAPTER_PATH = REPO_ROOT / "bin" / "run-dev-agent"
REPO_TOOLS_JSON = REPO_ROOT / ".ai-project" / "agents" / "tools.json"

EXIT_LOCAL_UNAVAILABLE = 5  # bin/run-dev-agent's EXIT_LOCAL_UNAVAILABLE (CONTRACT-adjacent)
STUB_MODEL_TAG = "qwen2.5-coder:14b"  # the suite's default local model tag

EPIC_ID = "P9-M99-E99.9"
SPEC_DIR = "docs/phases/P9__Fixture_Phase"
SPEC_NAME = f"{EPIC_ID}__spec__fixture.md"

SPEC_BODY = """---
epic: E99.9
type: spec
---

# Epic E99.9 — Fixture spec

## Context

Context prose that must NOT become the task.

## Definition of Done

- [ ] the fixture DoD line one
- [ ] the fixture DoD line two

## Acceptance Criteria

Acceptance prose that must NOT become the task.
"""

STARTER_BODY = "# Epic Execution Chat Starter — fixture\n\nScoped starter material.\n"

GOVERNANCE_MARKER = "GOVERNANCE-CORPUS-MARKER: this text must never reach --context"

STUB_RUNNER = """#!/usr/bin/env python3
import json, os, sys

with open(os.environ["STUB_ARGS_FILE"], "w") as f:
    json.dump(sys.argv[1:], f)
if "--transcript" in sys.argv:
    path = sys.argv[sys.argv.index("--transcript") + 1]
    with open(path, "w") as f:
        json.dump({"status": "completed", "transcript": [], "tokens": 0}, f)
sys.exit(int(os.environ.get("STUB_EXIT_CODE", "0")))
"""


class _TagsHandler(http.server.BaseHTTPRequestHandler):
    """Serves ``/api/tags`` with whatever tags ``self.server.tags`` carries (set by
    the ``ollama_stub`` fixture) — enough of the real Ollama API surface for the
    adapter's preflight check."""

    def do_GET(self):
        if self.path == "/api/tags":
            body = json.dumps(
                {"models": [{"name": t} for t in self.server.tags]}
            ).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, *_args):
        pass


@pytest.fixture
def ollama_stub():
    """A real loopback HTTP server standing in for Ollama's ``/api/tags``, reachable
    by the adapter's subprocess. Reports ``STUB_MODEL_TAG`` as pulled by default."""
    server = http.server.HTTPServer(("127.0.0.1", 0), _TagsHandler)
    server.tags = [STUB_MODEL_TAG]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield server
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


def _unused_port():
    """A port nothing is listening on (bind-then-close), for the unreachable-endpoint
    tests — standard idiom, negligible flakiness risk in a short test window."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


@pytest.fixture
def project(tmp_path, ollama_stub):
    """A minimal project the adapter can run against, plus a stubbed runner."""
    root = tmp_path / "project"
    spec_dir = root / SPEC_DIR
    spec_dir.mkdir(parents=True)
    (spec_dir / SPEC_NAME).write_text(SPEC_BODY)

    queue = root / ".ai-project" / "queue"
    queue.mkdir(parents=True)
    (queue / "04_epic.json").write_text(json.dumps({
        "epic_id": EPIC_ID,
        "epic_spec_path": f"{SPEC_DIR}/{SPEC_NAME}",
        "validation_command": "pytest",
    }))

    agents = root / ".ai-project" / "agents"
    agents.mkdir(parents=True)
    (agents / "tools.json").write_text(REPO_TOOLS_JSON.read_text())

    # Governance corpus present in the project — must never be picked up as context.
    governance = root / "governance"
    governance.mkdir()
    (governance / "PROJECT-SYSTEM-GUIDELINES.md").write_text(GOVERNANCE_MARKER)

    stub = tmp_path / "stub-runner"
    stub.write_text(STUB_RUNNER)
    stub.chmod(stub.stat().st_mode | stat.S_IXUSR)

    return {
        "root": root,
        "stub": stub,
        "args_file": tmp_path / "stub-args.json",
        "spec_dir": spec_dir,
        "ollama_stub": ollama_stub,
        "ollama_url": f"http://127.0.0.1:{ollama_stub.server_port}",
    }


_DEFAULT_ENDPOINT = object()  # sentinel: "use project's working ollama_stub"


def run_adapter(
    project, model="local:qwen2.5-coder:14b", exit_code=0, env_extra=None,
    ollama_endpoint=_DEFAULT_ENDPOINT,
):
    """``ollama_endpoint`` defaults to the project's real, reachable stub (so every
    existing local-model test passes the P9-M31-E31.2 preflight check silently);
    pass an explicit URL/``None`` to exercise endpoint-forwarding or the
    local-unavailable path instead."""
    env = os.environ.copy()
    env.pop("AI_PROJECT_ACTIVE_MODEL", None)
    env.pop("AI_PROJECT_OLLAMA_ENDPOINT", None)
    if model is not None:
        env["AI_PROJECT_ACTIVE_MODEL"] = model
    env["LOCAL_AGENT_RUNNER"] = str(project["stub"])
    env["STUB_ARGS_FILE"] = str(project["args_file"])
    env["STUB_EXIT_CODE"] = str(exit_code)
    resolved_endpoint = (
        project["ollama_url"] if ollama_endpoint is _DEFAULT_ENDPOINT else ollama_endpoint
    )
    if resolved_endpoint is not None:
        env["AI_PROJECT_OLLAMA_ENDPOINT"] = resolved_endpoint
    env.update(env_extra or {})
    return subprocess.run(
        [sys.executable, str(ADAPTER_PATH)],
        cwd=str(project["root"]),
        env=env,
        capture_output=True,
        text=True,
    )


def runner_args(project):
    with open(project["args_file"]) as f:
        return json.load(f)


def flag_value(args, flag):
    assert flag in args, f"{flag} not passed to the runner: {args}"
    return args[args.index(flag) + 1]


def context_text(project):
    """The context file content — paths the adapter passes are project-root-relative."""
    return (project["root"] / flag_value(runner_args(project), "--context")).read_text()


def artifact_dir(project):
    return project["root"] / ".ai-project" / "artifacts" / "agentic-runs" / EPIC_ID


# --- model mapping -------------------------------------------------------------


def test_local_prefix_maps_to_bare_tag(project):
    result = run_adapter(project, model="local:qwen2.5-coder:14b")
    assert result.returncode == 0, result.stderr
    assert flag_value(runner_args(project), "--model") == "qwen2.5-coder:14b"


def test_bare_tag_passes_through(project):
    result = run_adapter(project, model="qwen2.5-coder:14b")
    assert result.returncode == 0, result.stderr
    assert flag_value(runner_args(project), "--model") == "qwen2.5-coder:14b"


@pytest.mark.parametrize("model", [None, "", "   ", "local:"])
def test_missing_or_empty_model_is_config_error(project, model):
    result = run_adapter(project, model=model)
    assert result.returncode == 3
    assert result.stderr.strip(), "expected a one-line reason on stderr"
    assert not project["args_file"].exists(), "runner must not be invoked"


# --- task construction ----------------------------------------------------------


def test_task_is_the_dod_section(project):
    result = run_adapter(project)
    assert result.returncode == 0, result.stderr
    task = flag_value(runner_args(project), "--task-text")
    assert "the fixture DoD line one" in task
    assert "the fixture DoD line two" in task
    assert "must NOT become the task" not in task


def test_context_is_the_scoped_spec_never_governance(project):
    result = run_adapter(project)
    assert result.returncode == 0, result.stderr
    context = context_text(project)
    assert "the fixture DoD line one" in context, "scoped spec expected in context"
    assert GOVERNANCE_MARKER not in context
    assert "PROJECT-SYSTEM-GUIDELINES" not in context
    assert "AI-OPERATING-GUIDELINES" not in context


def test_context_includes_starter_when_present(project):
    (project["spec_dir"] / f"{EPIC_ID}__epic-execution-chat-starter.md").write_text(
        STARTER_BODY
    )
    result = run_adapter(project)
    assert result.returncode == 0, result.stderr
    context = context_text(project)
    assert "Scoped starter material." in context
    assert GOVERNANCE_MARKER not in context


def test_tools_flag_is_the_coding_set(project):
    result = run_adapter(project)
    assert result.returncode == 0, result.stderr
    tools = flag_value(runner_args(project), "--tools")
    assert tools == str(Path(".ai-project") / "agents" / "tools.json")


def test_endpoint_env_is_forwarded(project):
    # A real, reachable endpoint (not a fake hostname): P9-M31-E31.2's preflight
    # check would otherwise reject an unreachable AI_PROJECT_OLLAMA_ENDPOINT before
    # the flag-forwarding behavior under test ever gets exercised.
    result = run_adapter(project, ollama_endpoint=project["ollama_url"])
    assert result.returncode == 0, result.stderr
    assert flag_value(runner_args(project), "--endpoint") == project["ollama_url"]


def test_endpoint_defaults_to_runner_default(project):
    # A non-local model: the preflight check (and its dependency on a reachable
    # default endpoint) only applies to local: models, so this isolates the
    # flag-omission behavior under test from that check entirely.
    result = run_adapter(project, model="qwen2.5-coder:14b", ollama_endpoint=None)
    assert result.returncode == 0, result.stderr
    assert "--endpoint" not in runner_args(project)


# --- exit-code passthrough -------------------------------------------------------


@pytest.mark.parametrize("code", [0, 2, 3, 4])
def test_runner_exit_code_passes_through_unaltered(project, code):
    result = run_adapter(project, exit_code=code)
    assert result.returncode == code


# --- local-availability preflight (P9-M31-E31.2, Hard Constraint 4) --------------


def test_local_unavailable_when_endpoint_unreachable(project):
    unreachable = f"http://127.0.0.1:{_unused_port()}"
    result = run_adapter(project, ollama_endpoint=unreachable)
    assert result.returncode == EXIT_LOCAL_UNAVAILABLE
    assert "unreachable" in result.stderr
    assert not project["args_file"].exists(), "runner must not be invoked"


def test_local_unavailable_when_model_not_pulled(project):
    result = run_adapter(project, model="local:some-unpulled-tag:latest")
    assert result.returncode == EXIT_LOCAL_UNAVAILABLE
    assert "not found" in result.stderr or "not pulled" in result.stderr
    assert not project["args_file"].exists(), "runner must not be invoked"


def test_local_unavailable_distinct_from_config_error_and_runner_codes():
    """The distinguished exit must not collide with the config-error class (3) or
    any value in the runner's own 0/2/3/4 contract."""
    assert EXIT_LOCAL_UNAVAILABLE not in {0, 2, 3, 4}


def test_non_local_model_skips_local_availability_check(project):
    """A bare/remote-tagged model has no local endpoint to check -- the preflight
    is scoped to local: models only (Non-Goals: never treat a remote dispatch as
    a local-availability question)."""
    unreachable = f"http://127.0.0.1:{_unused_port()}"
    result = run_adapter(project, model="qwen2.5-coder:14b", ollama_endpoint=unreachable)
    assert result.returncode == 0, result.stderr
    assert project["args_file"].exists(), "runner should have been invoked normally"


def test_local_available_and_model_present_proceeds_normally(project):
    """Sanity check: a reachable endpoint reporting the requested tag as pulled
    must not be mistaken for unavailable -- the check must not false-positive."""
    result = run_adapter(project, model=f"local:{STUB_MODEL_TAG}")
    assert result.returncode == 0, result.stderr
    assert flag_value(runner_args(project), "--model") == STUB_MODEL_TAG


# --- transcript + artifacts ------------------------------------------------------


def test_transcript_written_to_documented_convention(project):
    result = run_adapter(project)
    assert result.returncode == 0, result.stderr
    transcript = artifact_dir(project) / "transcript.json"
    assert flag_value(runner_args(project), "--transcript") == str(
        Path(".ai-project") / "artifacts" / "agentic-runs" / EPIC_ID / "transcript.json"
    )
    assert transcript.exists(), "runner-written transcript expected at the artifact path"


def test_run_metadata_and_context_are_persisted(project):
    result = run_adapter(project, exit_code=2)
    assert result.returncode == 2
    metadata = json.loads((artifact_dir(project) / "run-metadata.json").read_text())
    assert metadata["epic_id"] == EPIC_ID
    assert metadata["model"] == "qwen2.5-coder:14b"
    assert metadata["exit_code"] == 2
    assert (artifact_dir(project) / "context.md").exists()


# --- config errors ---------------------------------------------------------------


def test_missing_trigger_is_config_error(project):
    (project["root"] / ".ai-project" / "queue" / "04_epic.json").unlink()
    result = run_adapter(project)
    assert result.returncode == 3
    assert "trigger" in result.stderr


def test_missing_spec_is_config_error(project):
    (project["spec_dir"] / SPEC_NAME).unlink()
    result = run_adapter(project)
    assert result.returncode == 3
    assert "spec" in result.stderr


def test_spec_without_dod_section_is_config_error(project):
    (project["spec_dir"] / SPEC_NAME).write_text("# Fixture\n\n## Context\n\nNo DoD here.\n")
    result = run_adapter(project)
    assert result.returncode == 3
    assert "Definition of Done" in result.stderr


def test_missing_tools_json_is_config_error(project):
    (project["root"] / ".ai-project" / "agents" / "tools.json").unlink()
    result = run_adapter(project)
    assert result.returncode == 3
    assert "tool" in result.stderr


def test_missing_runner_is_config_error(project, tmp_path):
    empty_path = tmp_path / "empty-path"
    empty_path.mkdir()
    result = run_adapter(
        project, env_extra={"LOCAL_AGENT_RUNNER": "", "PATH": str(empty_path)}
    )
    assert result.returncode == 3
    assert "local-agent-runner" in result.stderr


# --- binding guards ---------------------------------------------------------------


def test_adapter_never_references_the_terminating_text_field():
    """SN-3 binding: no dependency on the runner's prose result — not even for logging."""
    source = ADAPTER_PATH.read_text()
    assert "final" + "_answer" not in source


def test_adapter_is_executable():
    assert os.access(ADAPTER_PATH, os.X_OK)


def test_repo_tools_json_is_the_scoped_coding_set():
    tools = json.loads(REPO_TOOLS_JSON.read_text())
    assert set(tools["enabled"]) == {
        "read_file", "write_file", "edit_file", "list_dir", "run_command", "git",
    }
    assert any("pytest" in c for c in tools["allow_commands"])
    assert tools["allow_paths"], "paths must be scoped, not absent"
    assert tools["timeout"] > 0
