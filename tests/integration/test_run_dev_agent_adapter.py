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
"""

import json
import os
import stat
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
ADAPTER_PATH = REPO_ROOT / "bin" / "run-dev-agent"
REPO_TOOLS_JSON = REPO_ROOT / ".ai-project" / "agents" / "tools.json"

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


@pytest.fixture
def project(tmp_path):
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
    }


def run_adapter(project, model="local:qwen2.5-coder:14b", exit_code=0, env_extra=None):
    env = os.environ.copy()
    env.pop("AI_PROJECT_ACTIVE_MODEL", None)
    env.pop("AI_PROJECT_OLLAMA_ENDPOINT", None)
    if model is not None:
        env["AI_PROJECT_ACTIVE_MODEL"] = model
    env["LOCAL_AGENT_RUNNER"] = str(project["stub"])
    env["STUB_ARGS_FILE"] = str(project["args_file"])
    env["STUB_EXIT_CODE"] = str(exit_code)
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
    result = run_adapter(
        project, env_extra={"AI_PROJECT_OLLAMA_ENDPOINT": "http://ollama-host:11434"}
    )
    assert result.returncode == 0, result.stderr
    assert flag_value(runner_args(project), "--endpoint") == "http://ollama-host:11434"


def test_endpoint_defaults_to_runner_default(project):
    result = run_adapter(project)
    assert result.returncode == 0, result.stderr
    assert "--endpoint" not in runner_args(project)


# --- exit-code passthrough -------------------------------------------------------


@pytest.mark.parametrize("code", [0, 2, 3, 4])
def test_runner_exit_code_passes_through_unaltered(project, code):
    result = run_adapter(project, exit_code=code)
    assert result.returncode == code


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
