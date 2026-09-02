"""Guards the E42.2 epic-scoped staging.

bin/ai-project-orchestrator's handle_epic_execution staged the ENTIRE worktree with
``git add .`` and committed it under the epic's message — so "the agent touched
something it should not have" had no representation: an out-of-scope modification was
silently absorbed into a commit claiming to be the epic's deliverables. E42.2 replaces
that with staging scoped to the epic's files (per the committed design decision in
P12-M42-E42.2's record artifact) and records the out-of-scope remainder instead of
absorbing it.

The definition of "the epic's files" (D1 Part A, candidate 3): the paths the epic's own
run recorded as touched — the write/edit/create tool-call paths in the run's transcript
at ``.ai-project/artifacts/agentic-runs/<epic_id>/transcript.json`` — intersected with
the actual working-tree diff, plus the epic's own run-record artifacts under that same
artifact root. Everything else dirty is out-of-scope and recorded, never staged.

The tests load the extensionless ``bin/ai-project-orchestrator`` as a module, mirroring
tests/test_sandbox_endpoint_forwarding.py, and capture the ``git add`` argv exactly as
that file captures the ``docker run`` argv. No repository is modified; the git
subprocess is faked.

Falsification (the milestone's Hard Constraint — prove the guard by deleting it):
restoring the removed ``subprocess.run(["git", "add", "."], ...)`` at the staging site
makes test_in_scope_only_stages_the_epics_files fail (the argv is ``["git", "add", "."]``
again) and test_out_of_scope_is_recorded_not_staged fail (no out-of-scope record is
written — the case becomes invisible again).
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
    loader = SourceFileLoader("ai_project_orchestrator_e422", str(ORCH_PATH))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


orch = _load_orchestrator()


def _write_transcript(tmp_path, epic_id, tool_calls):
    """Create a run transcript under the epic's artifact root recording tool calls."""
    tp = (
        tmp_path / ".ai-project" / "artifacts" / "agentic-runs"
        / epic_id / "transcript.json"
    )
    tp.parent.mkdir(parents=True, exist_ok=True)
    transcript = {
        "status": "completed",
        "transcript": [
            {"tool_call": {"name": name, "args": {"path": path}}}
            for name, path in tool_calls
        ],
    }
    tp.write_text(json.dumps(transcript))
    return tp


def _fake_git_runs(captured, status_stdout):
    """subprocess.run replacement: answer ``git status`` with porcelain, record every
    command, and let add/commit appear to succeed."""
    def fake_run(cmd, *args, **kwargs):
        captured.append(cmd)
        if cmd[:2] == ["git", "status"]:
            return MagicMock(returncode=0, stdout=status_stdout, stderr="")
        return MagicMock(returncode=0, stdout="", stderr="")
    return fake_run


# ---------------------------------------------------------------------------
# In-scope-only branch — the epic's files are staged, the whole tree is not
# ---------------------------------------------------------------------------

class TestInScopeOnlyBranch:
    def test_in_scope_only_stages_the_epics_files(self, tmp_path, monkeypatch):
        """The guard: a clean, in-scope-only run stages exactly the epic's files and
        commits them — the git add argv is the scoped set, never ["git", "add", "."]."""
        epic_id = "EPIC-E422-1"
        monkeypatch.setattr(orch, "PROJECT_ROOT", tmp_path)

        _write_transcript(tmp_path, epic_id, [
            ("write_file", "bin/foo.py"),
            ("write_file", "tests/test_foo.py"),
        ])

        captured = []
        status_stdout = " M bin/foo.py\n M tests/test_foo.py\n"
        with patch.object(orch.subprocess, "run", side_effect=_fake_git_runs(captured, status_stdout)):
            result = orch._stage_and_commit_epic(epic_id, "dev-model", "qa-model")

        assert result == "committed"

        add_args = [c for c in captured if c[:2] == ["git", "add"]]
        assert add_args, "git add must be invoked"
        assert add_args[0] == ["git", "add", "--", "bin/foo.py", "tests/test_foo.py"]
        assert add_args[0] != ["git", "add", "."]

        # The :477-style claim names what is actually staged — true of the commit.
        commit_args = [c for c in captured if c[:2] == ["git", "commit"]]
        assert commit_args
        assert "Staged files: bin/foo.py, tests/test_foo.py" in commit_args[0][-1]

        # No out-of-scope remainder -> no record.
        rec = tmp_path / ".ai-project" / "artifacts" / "agentic-runs" / epic_id / "out-of-scope.json"
        assert not rec.exists()


# ---------------------------------------------------------------------------
# Out-of-scope-present branch — recorded, distinguishable, never absorbed
# ---------------------------------------------------------------------------

class TestOutOfScopeBranch:
    def test_out_of_scope_is_recorded_not_staged(self, tmp_path, monkeypatch):
        """The guard: a dirty file the epic's run did NOT report touching is never
        staged and never folded into the epic commit — it is named in a record."""
        epic_id = "EPIC-E422-2"
        monkeypatch.setattr(orch, "PROJECT_ROOT", tmp_path)

        _write_transcript(tmp_path, epic_id, [
            ("write_file", "bin/foo.py"),
        ])

        captured = []
        # docs/stray.md is dirty but the epic's run never reported touching it.
        status_stdout = " M bin/foo.py\n?? docs/stray.md\n"
        with patch.object(orch.subprocess, "run", side_effect=_fake_git_runs(captured, status_stdout)):
            result = orch._stage_and_commit_epic(epic_id, "dev-model", "qa-model")

        assert result == "committed"

        add_args = [c for c in captured if c[:2] == ["git", "add"]]
        assert add_args
        # The out-of-scope path must NOT appear in any git add argv...
        assert all("docs/stray.md" not in c for c in add_args)
        # ...and the record IS staged so the case travels with the epic.
        assert any(c.endswith("out-of-scope.json") for c in add_args[0])

        rec = tmp_path / ".ai-project" / "artifacts" / "agentic-runs" / epic_id / "out-of-scope.json"
        assert rec.exists()
        payload = json.loads(rec.read_text())
        assert "docs/stray.md" in payload["out_of_scope_paths"]
        assert payload["disposition"] == "recorded; NOT staged or committed with the epic"

        # The commit message states the remainder was recorded, not absorbed.
        commit_args = [c for c in captured if c[:2] == ["git", "commit"]]
        assert commit_args
        assert "docs/stray.md" in commit_args[0][-1]
        assert "Out-of-scope paths recorded" in commit_args[0][-1]

    def test_no_footprint_and_dirty_tree_fails_closed(self, tmp_path, monkeypatch):
        """A run that left no attributable footprint on a dirty tree cannot claim a
        scoped commit: it records the remainder and escalates — it never stages."""
        epic_id = "EPIC-E422-3"
        monkeypatch.setattr(orch, "PROJECT_ROOT", tmp_path)

        # No transcript written at all.
        captured = []
        status_stdout = "?? docs/stray.md\n"
        with patch.object(orch.subprocess, "run", side_effect=_fake_git_runs(captured, status_stdout)):
            result = orch._stage_and_commit_epic(epic_id, "dev-model", "qa-model")

        assert result == "escalate"
        assert not [c for c in captured if c[:2] == ["git", "add"]]
        assert not [c for c in captured if c[:2] == ["git", "commit"]]

        rec = tmp_path / ".ai-project" / "artifacts" / "agentic-runs" / epic_id / "out-of-scope.json"
        assert rec.exists()
        payload = json.loads(rec.read_text())
        assert "docs/stray.md" in payload["out_of_scope_paths"]


# ---------------------------------------------------------------------------
# The definition itself — transcript paths must be project-relative / mapped
# ---------------------------------------------------------------------------

class TestTranscriptFootprint:
    def test_transcript_absolute_path_outside_project_is_ignored(self, tmp_path, monkeypatch):
        """A tool-call path that cannot be mapped into PROJECT_ROOT (a harness
        scratchpad) must not fabricate an in-scope file."""
        epic_id = "EPIC-E422-4"
        monkeypatch.setattr(orch, "PROJECT_ROOT", tmp_path)

        _write_transcript(tmp_path, epic_id, [
            ("write_file", "/tmp/harness-scratchpad/workspace/out.py"),
            ("write_file", "bin/foo.py"),
        ])

        captured = []
        status_stdout = " M bin/foo.py\n M out.py\n"
        with patch.object(orch.subprocess, "run", side_effect=_fake_git_runs(captured, status_stdout)):
            result = orch._stage_and_commit_epic(epic_id, "dev-model", "qa-model")

        assert result == "committed"
        add_args = [c for c in captured if c[:2] == ["git", "add"]]
        # bin/foo.py is in-scope; the harness-scratchpad path is not; the unmappable
        # path was never a file in this tree.
        assert "bin/foo.py" in add_args[0]