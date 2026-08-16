"""Contract tests for ``bin/run-qa-agent`` — the QA-role dispatch built in Epic P11-M39-E39.3.

These tests are the mechanical half of the epic's five-criterion genuineness bar. The
point of that bar is that a reviewer should be able to rule out *"a dev-lane run
relabelled"* **from committed artifacts rather than from the epic's account of itself**,
so each criterion that can be pinned by a test is pinned here:

- **Criterion 1 (role: assesses, does not produce)** — the task text the adapter hands the
  runner is an assessment with a verdict, and is **not** the standard's Definition of Done
  re-served as an instruction, which is exactly what ``bin/run-dev-agent`` does
  (``task_text = extract_dod(...)``). Changing the model does not change the role.
- **Criterion 2 (tools: cannot mutate the tree)** — the **committed** QA tool set enables
  no mutating tool, and the adapter refuses to dispatch under one that does, so the
  guarantee does not depend on that file staying read-only after this epic ends.
- **Criterion 3 (routing: provably from config)** — the model comes from
  ``.ai-project.yml``'s ``models.epic_qa``; there is no flag or environment variable that
  can substitute a different one, and a disagreeing ``AI_PROJECT_ACTIVE_MODEL`` is refused
  rather than preferred.
- **Criterion 4 (capture: distinct paths, overwrite nothing)** — the ``qa-`` prefixed
  filenames are written, the dev adapter's plain ``transcript.json`` /
  ``run-metadata.json`` are **not** created, the four preserved ``epic_id`` values of
  Epic spec §F3 are refused unconditionally, and any pre-existing artifact aborts the run.
- **Criterion 5 (non-authority)** — the metadata declares the verdict advisory.

The runner is **stubbed** throughout (via the adapter's ``LOCAL_AGENT_RUNNER`` discovery
override, the same technique ``test_run_dev_agent_adapter.py`` uses); the one live run
against ``local:qwen3-coder:30b`` is captured as a committed artifact under
``.ai-project/artifacts/agentic-runs/P11-M39-E39.3/``, not re-executed here. The suite
must not depend on a reachable Ollama endpoint or on a ``local-agent-runner`` checkout
existing beside this repository.
"""

import http.server
import json
import os
import stat
import subprocess
import sys
import threading
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
ADAPTER_PATH = REPO_ROOT / "bin" / "run-qa-agent"
REPO_QA_TOOLS_JSON = REPO_ROOT / ".ai-project" / "agents" / "qa-tools.json"
REPO_TOOLS_JSON = REPO_ROOT / ".ai-project" / "agents" / "tools.json"

EXIT_CONFIG = 3
QA_MODEL = "local:qwen3-coder:30b"  # this repo's configured models.epic_qa
QA_TAG = "qwen3-coder:30b"
EPIC_ID = "P11-M99-E99.9"

# Epic spec §F3 (sharpened at v1.0.1): the four directories holding the plain filenames
# the dev adapter writes. E33.4's run-metadata.json is the only surviving copy of that
# binding case's exit code; the three *-PROVE dirs are held-out cases.
FORBIDDEN_EPIC_IDS = [
    "P10-M33-E33.4",
    "P7-M26-E26.3-PROVE",
    "P9-M31-E31.1-PROVE",
    "P9-M31-E31.2-PROVE",
]

MUTATING_TOOLS = {"write_file", "edit_file", "git", "run_command"}

STANDARD_NAME = "standard.md"
STANDARD_BODY = """\
# A fixture standard

## Context

Context prose that must NOT become the task.

## Definition of Done

- [ ] the fixture DoD line one
- [ ] the fixture DoD line two

## Acceptance Criteria

Acceptance prose that must NOT become the task.
"""

WORK_NAME = "work.txt"
WORK_BODY = "the work under assessment\n"

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
    """Enough of Ollama's ``/api/tags`` surface for the inherited preflight check."""

    def do_GET(self):
        if self.path == "/api/tags":
            body = json.dumps({"models": [{"name": QA_TAG}]}).encode()
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
    server = http.server.HTTPServer(("127.0.0.1", 0), _TagsHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield server
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


@pytest.fixture
def project(tmp_path, ollama_stub):
    """A minimal project the QA adapter can run against, plus a stubbed runner."""
    root = tmp_path / "project"
    root.mkdir()
    (root / ".ai-project.yml").write_text(
        "project:\n"
        "  name: fixture\n"
        "  description: fixture project\n"
        "models:\n"
        f"  epic_dev: local:some-dev-model\n"
        f"  epic_qa: {QA_MODEL}\n"
    )
    agents = root / ".ai-project" / "agents"
    agents.mkdir(parents=True)
    (agents / "qa-tools.json").write_text(REPO_QA_TOOLS_JSON.read_text())

    (root / STANDARD_NAME).write_text(STANDARD_BODY)
    (root / WORK_NAME).write_text(WORK_BODY)

    stub = tmp_path / "stub-runner"
    stub.write_text(STUB_RUNNER)
    stub.chmod(stub.stat().st_mode | stat.S_IXUSR)

    return {
        "root": root,
        "stub": stub,
        "args_file": tmp_path / "stub-args.json",
        "ollama_url": f"http://127.0.0.1:{ollama_stub.server_port}",
    }


def run_qa(project, epic_id=EPIC_ID, extra_args=(), env_extra=None):
    env = os.environ.copy()
    env.pop("AI_PROJECT_ACTIVE_MODEL", None)
    env["LOCAL_AGENT_RUNNER"] = str(project["stub"])
    env["STUB_ARGS_FILE"] = str(project["args_file"])
    env.setdefault("STUB_EXIT_CODE", "0")
    env.update(env_extra or {})
    argv = [
        sys.executable, str(ADAPTER_PATH),
        "--epic-id", epic_id,
        "--standard", STANDARD_NAME,
        "--work", WORK_NAME,
        "--endpoint", project["ollama_url"],
        *extra_args,
    ]
    return subprocess.run(
        argv, cwd=str(project["root"]), env=env, capture_output=True, text=True
    )


def runner_args(project):
    with open(project["args_file"]) as f:
        return json.load(f)


def flag_value(args, flag):
    assert flag in args, f"{flag} not passed to the runner: {args}"
    return args[args.index(flag) + 1]


def artifact_dir(project, epic_id=EPIC_ID):
    return project["root"] / ".ai-project" / "artifacts" / "agentic-runs" / epic_id


# --- criterion 2: the committed tool set cannot mutate the working tree ----------


def test_committed_qa_tool_set_enables_no_mutating_tool():
    """The evidence a reviewer actually checks: a committed file, not an intention."""
    data = json.loads(REPO_QA_TOOLS_JSON.read_text())
    assert set(data["enabled"]) & MUTATING_TOOLS == set(), data["enabled"]
    assert set(data["enabled"]) <= {"read_file", "list_dir"}, data["enabled"]


def test_committed_qa_tool_set_denies_commands_and_subcommands():
    """Belt and braces at the handler layer: empty allow lists deny by default, so
    ``run_command`` and ``git`` can execute nothing even if they were ever advertised."""
    data = json.loads(REPO_QA_TOOLS_JSON.read_text())
    assert data["allow_commands"] == []
    assert data["allow_subcommands"] == []
    assert data["deny_commands"] == ["*"]


def test_the_dev_tool_set_is_the_one_that_mutates():
    """The contrast criterion 2 exists to draw — and a guard against the QA set being
    quietly swapped for the coding set."""
    dev = json.loads(REPO_TOOLS_JSON.read_text())
    assert MUTATING_TOOLS & set(dev["enabled"]), dev["enabled"]
    assert "commit" in dev["allow_subcommands"]


def test_adapter_refuses_a_mutating_tool_set(project):
    tools = project["root"] / ".ai-project" / "agents" / "qa-tools.json"
    data = json.loads(tools.read_text())
    data["enabled"] = ["read_file", "write_file"]
    tools.write_text(json.dumps(data))

    result = run_qa(project)
    assert result.returncode == EXIT_CONFIG, result.stdout
    assert "write_file" in result.stderr
    assert not artifact_dir(project).exists()


# --- criterion 1: the task assesses, it does not produce ------------------------


def test_task_text_is_an_assessment_not_the_definition_of_done(project):
    result = run_qa(project)
    assert result.returncode == 0, result.stderr
    task = flag_value(runner_args(project), "--task-text")
    assert "VERDICT: PASS" in task and "VERDICT: FAIL" in task
    assert "QA reviewer" in task
    assert "the fixture DoD line one" not in task, (
        "the DoD leaked into the task text — that is the dev adapter's behaviour"
    )


def test_the_standard_reaches_the_runner_as_context_not_as_the_task(project):
    result = run_qa(project)
    assert result.returncode == 0, result.stderr
    context = (project["root"] / flag_value(runner_args(project), "--context")).read_text()
    assert "## STANDARD" in context and "## WORK" in context
    assert "the fixture DoD line one" in context
    assert WORK_NAME in context
    # The work is named for the agent to read with read_file, never inlined — that is
    # what makes the read-only tool set load-bearing rather than decorative.
    assert WORK_BODY.strip() not in context


def test_non_dod_standard_sections_are_supported(project):
    result = run_qa(project, extra_args=("--standard-section", "Acceptance Criteria"))
    assert result.returncode == 0, result.stderr
    context = (project["root"] / flag_value(runner_args(project), "--context")).read_text()
    assert "Acceptance prose" in context
    assert "the fixture DoD line one" not in context


def test_missing_standard_section_is_a_config_error(project):
    result = run_qa(project, extra_args=("--standard-section", "No Such Section"))
    assert result.returncode == EXIT_CONFIG
    assert "No Such Section" in result.stderr


# --- criterion 3: routing comes from .ai-project.yml, not from a hand ------------


def test_model_is_resolved_from_config_models_epic_qa(project):
    result = run_qa(project)
    assert result.returncode == 0, result.stderr
    assert flag_value(runner_args(project), "--model") == QA_TAG
    meta = json.loads((artifact_dir(project) / "qa-run-metadata.json").read_text())
    provenance = meta["model_provenance"]
    assert provenance["source"] == ".ai-project.yml:models.epic_qa"
    assert provenance["configured_value"] == QA_MODEL
    assert len(provenance["config_sha256"]) == 64


def test_disagreeing_active_model_env_is_refused(project):
    result = run_qa(project, env_extra={"AI_PROJECT_ACTIVE_MODEL": "local:something-else"})
    assert result.returncode == EXIT_CONFIG
    assert "hand-picked" in result.stderr
    assert not artifact_dir(project).exists()


def test_agreeing_active_model_env_is_recorded_as_corroboration(project):
    result = run_qa(project, env_extra={"AI_PROJECT_ACTIVE_MODEL": QA_MODEL})
    assert result.returncode == 0, result.stderr
    meta = json.loads((artifact_dir(project) / "qa-run-metadata.json").read_text())
    assert meta["model_provenance"]["env_agrees_with_config"] is True


def test_missing_models_epic_qa_is_a_config_error(project):
    (project["root"] / ".ai-project.yml").write_text("project:\n  name: fixture\n")
    result = run_qa(project)
    assert result.returncode == EXIT_CONFIG
    assert "models.epic_qa" in result.stderr


# --- criterion 4: capture at distinct paths that overwrite nothing ---------------


def test_writes_qa_prefixed_artifacts_and_never_the_dev_filenames(project):
    result = run_qa(project)
    assert result.returncode == 0, result.stderr
    directory = artifact_dir(project)
    assert (directory / "qa-transcript.json").exists()
    assert (directory / "qa-context.md").exists()
    assert (directory / "qa-run-metadata.json").exists()
    # The two filenames whose collision would destroy preserved evidence (§F3).
    assert not (directory / "transcript.json").exists()
    assert not (directory / "run-metadata.json").exists()
    assert not (directory / "context.md").exists()


@pytest.mark.parametrize("epic_id", FORBIDDEN_EPIC_IDS)
def test_preserved_epic_ids_are_refused_unconditionally(project, epic_id):
    result = run_qa(project, epic_id=epic_id)
    assert result.returncode == EXIT_CONFIG
    assert "preserved run directory" in result.stderr
    assert not artifact_dir(project, epic_id).exists()


def test_refuses_to_overwrite_an_existing_artifact(project):
    directory = artifact_dir(project)
    directory.mkdir(parents=True)
    (directory / "qa-transcript.json").write_text("PRESERVED")

    result = run_qa(project)
    assert result.returncode == EXIT_CONFIG
    assert "refusing to overwrite" in result.stderr
    assert (directory / "qa-transcript.json").read_text() == "PRESERVED"


def test_runner_exit_code_passes_through(project):
    result = run_qa(project, env_extra={"STUB_EXIT_CODE": "2"})
    assert result.returncode == 2
    meta = json.loads((artifact_dir(project) / "qa-run-metadata.json").read_text())
    assert meta["exit_code"] == 2


# --- criterion 5: the verdict is advisory ---------------------------------------


def test_metadata_declares_the_verdict_advisory(project):
    result = run_qa(project)
    assert result.returncode == 0, result.stderr
    meta = json.loads((artifact_dir(project) / "qa-run-metadata.json").read_text())
    assert meta["authority"] == "advisory"
    assert meta["role"] == "qa"
    assert meta["lane"] == "epic_qa"
    assert "never whether the assessed work passed" in meta["exit_code_note"]


def test_metadata_binds_the_tool_set_it_actually_dispatched_under(project):
    """The reviewer's check for criterion 2 is only as good as the artifact's binding to
    the file — so the hash and the enabled list are recorded, not just the path."""
    result = run_qa(project)
    assert result.returncode == 0, result.stderr
    meta = json.loads((artifact_dir(project) / "qa-run-metadata.json").read_text())
    assert set(meta["tools_enabled"]) & MUTATING_TOOLS == set()
    assert len(meta["tools_sha256"]) == 64
    assert flag_value(runner_args(project), "--tools").endswith("qa-tools.json")
