"""Unit and integration tests for daemon orchestrator path resolution.

Epic P4-M17-E17.1 — Fix Daemon Orchestrator Path Resolution.

Root cause under test: the daemon previously resolved the orchestrator binary
strictly at ``<PROJECT_ROOT>/bin/ai-project-orchestrator``. When the daemon runs
from a governance submodule with ``--project-root .`` pointing at the *consuming*
project, the orchestrator is not under the consuming project's ``bin/`` — it
ships inside the governance package next to the daemon. The daemon therefore
failed with "orchestrator not found".

The fix introduces an ordered, cached search over conventional locations plus
the daemon's own directory (which always contains the orchestrator).
"""

import io
import os
import sys
import stat
import subprocess
import importlib.util
from importlib.machinery import SourceFileLoader
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
DAEMON_PATH = REPO_ROOT / "bin" / "ai-project-daemon"
ORCH_NAME = "ai-project-orchestrator"


def _load_daemon_module():
    """Load the extensionless ``bin/ai-project-daemon`` script as a module."""
    loader = SourceFileLoader("ai_project_daemon_under_test", str(DAEMON_PATH))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


@pytest.fixture
def daemon(tmp_path, monkeypatch):
    """Daemon module with PROJECT_ROOT / DAEMON_DIR redirected into tmp_path.

    Layout:
      tmp_path/project/        -> PROJECT_ROOT (consuming project)
      tmp_path/daemon_dir/     -> DAEMON_DIR (where the daemon script "lives")

    Both start empty; individual tests place an orchestrator where needed.
    """
    mod = _load_daemon_module()

    project_root = tmp_path / "project"
    daemon_dir = tmp_path / "daemon_dir"
    project_root.mkdir(parents=True, exist_ok=True)
    daemon_dir.mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr(mod, "PROJECT_ROOT", project_root)
    monkeypatch.setattr(mod, "DAEMON_DIR", daemon_dir)
    monkeypatch.setattr(mod, "ORCHESTRATOR_BIN", project_root / "bin" / ORCH_NAME)
    mod.reset_orchestrator_cache()

    # Expose helper paths on the module object for convenience in tests.
    mod._t_project_root = project_root
    mod._t_daemon_dir = daemon_dir
    return mod


def _make_orchestrator(directory: Path) -> Path:
    """Create an executable stub orchestrator inside ``directory``."""
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / ORCH_NAME
    path.write_text("#!/usr/bin/env python3\n")
    path.chmod(path.stat().st_mode | stat.S_IXUSR)
    return path


# ---------------------------------------------------------------------------
# 1. Candidate enumeration
# ---------------------------------------------------------------------------

def test_search_paths_contains_four_distinct_candidates(daemon):
    paths = [str(p) for p in daemon.orchestrator_search_paths()]
    pr = daemon._t_project_root
    dd = daemon._t_daemon_dir
    assert str(pr / "bin" / ORCH_NAME) in paths
    assert str(pr / "governance" / "bin" / ORCH_NAME) in paths
    assert str(pr / ".governance" / "bin" / ORCH_NAME) in paths
    assert str(dd / ORCH_NAME) in paths
    assert len(paths) == 4


def test_search_paths_dedupe_self_referential(daemon, monkeypatch):
    """When DAEMON_DIR == PROJECT_ROOT/bin the duplicate is collapsed."""
    pr = daemon._t_project_root
    monkeypatch.setattr(daemon, "DAEMON_DIR", pr / "bin")
    monkeypatch.setattr(daemon, "ORCHESTRATOR_BIN", pr / "bin" / ORCH_NAME)
    paths = [str(p) for p in daemon.orchestrator_search_paths()]
    assert len(paths) == len(set(paths))  # no duplicates
    assert str(pr / "bin" / ORCH_NAME) in paths


# ---------------------------------------------------------------------------
# 2. Resolution per location
# ---------------------------------------------------------------------------

def test_resolve_primary_bin(daemon):
    expected = _make_orchestrator(daemon._t_project_root / "bin")
    assert daemon.resolve_orchestrator_bin() == expected


def test_resolve_governance_bin(daemon):
    expected = _make_orchestrator(daemon._t_project_root / "governance" / "bin")
    assert daemon.resolve_orchestrator_bin() == expected


def test_resolve_dot_governance_bin(daemon):
    expected = _make_orchestrator(daemon._t_project_root / ".governance" / "bin")
    assert daemon.resolve_orchestrator_bin() == expected


def test_resolve_daemon_dir_fallback(daemon):
    """The submodule case: orchestrator ships next to the daemon only."""
    expected = _make_orchestrator(daemon._t_daemon_dir)
    # The consuming project's own bin/ has no orchestrator.
    assert not (daemon._t_project_root / "bin" / ORCH_NAME).exists()
    assert daemon.resolve_orchestrator_bin() == expected


def test_resolve_returns_none_when_absent(daemon):
    assert daemon.resolve_orchestrator_bin() is None


# ---------------------------------------------------------------------------
# 3. Search order / precedence
# ---------------------------------------------------------------------------

def test_primary_bin_preferred_over_governance(daemon):
    primary = _make_orchestrator(daemon._t_project_root / "bin")
    _make_orchestrator(daemon._t_project_root / "governance" / "bin")
    assert daemon.resolve_orchestrator_bin() == primary


def test_governance_preferred_over_dot_governance(daemon):
    gov = _make_orchestrator(daemon._t_project_root / "governance" / "bin")
    _make_orchestrator(daemon._t_project_root / ".governance" / "bin")
    assert daemon.resolve_orchestrator_bin() == gov


def test_dot_governance_preferred_over_daemon_dir(daemon):
    dotgov = _make_orchestrator(daemon._t_project_root / ".governance" / "bin")
    _make_orchestrator(daemon._t_daemon_dir)
    assert daemon.resolve_orchestrator_bin() == dotgov


# ---------------------------------------------------------------------------
# 4. Caching behaviour (NFR: resolve once)
# ---------------------------------------------------------------------------

def test_resolution_is_cached(daemon):
    target = _make_orchestrator(daemon._t_project_root / "bin")
    first = daemon.resolve_orchestrator_bin()
    assert first == target
    # Remove the file; cached value must still be returned.
    target.unlink()
    assert daemon.resolve_orchestrator_bin() == target


def test_reset_cache_forces_reresolution(daemon):
    target = _make_orchestrator(daemon._t_project_root / "bin")
    assert daemon.resolve_orchestrator_bin() == target
    target.unlink()
    daemon.reset_orchestrator_cache()
    assert daemon.resolve_orchestrator_bin() is None


def test_use_cache_false_bypasses_cache(daemon):
    target = _make_orchestrator(daemon._t_project_root / "bin")
    assert daemon.resolve_orchestrator_bin() == target
    target.unlink()
    assert daemon.resolve_orchestrator_bin(use_cache=False) is None


# ---------------------------------------------------------------------------
# 5. process_queue integration with the resolver
# ---------------------------------------------------------------------------

def test_process_queue_defers_when_orchestrator_missing(daemon, monkeypatch):
    queue = daemon._t_project_root / ".ai-project" / "queue"
    queue.mkdir(parents=True, exist_ok=True)
    (queue / "01_a.json").touch()
    monkeypatch.setattr(daemon, "QUEUE_DIR", queue)

    captured = io.StringIO()
    with patch("subprocess.Popen") as mock_popen, patch.object(sys, "stdout", captured):
        daemon.process_queue()
    mock_popen.assert_not_called()
    output = captured.getvalue()
    assert "Orchestrator not found" in output
    # Clean failure must name the paths it tried.
    assert str(daemon._t_daemon_dir / ORCH_NAME) in output


def test_process_queue_invokes_resolved_orchestrator(daemon, monkeypatch):
    queue = daemon._t_project_root / ".ai-project" / "queue"
    queue.mkdir(parents=True, exist_ok=True)
    (queue / "01_a.json").touch()
    monkeypatch.setattr(daemon, "QUEUE_DIR", queue)
    # Orchestrator only in the daemon dir (submodule layout).
    orch = _make_orchestrator(daemon._t_daemon_dir)

    mock_process = MagicMock()
    mock_process.stdout = io.StringIO("done\n")
    mock_process.returncode = 0
    with patch("subprocess.Popen", return_value=mock_process) as mock_popen, \
            patch.object(sys, "stdout", io.StringIO()):
        daemon.process_queue()

    mock_popen.assert_called_once()
    args, _ = mock_popen.call_args
    assert str(orch) in args[0]
    assert "01_a.json" in args[0]


# ---------------------------------------------------------------------------
# 6. --check CLI and --project-root override (end-to-end subprocess)
# ---------------------------------------------------------------------------

def _make_submodule_project(tmp_path: Path) -> Path:
    """Build a consuming project whose governance submodule carries the daemon."""
    project = tmp_path / "consuming-project"
    gov_bin = project / "governance" / "bin"
    gov_bin.mkdir(parents=True, exist_ok=True)
    # Copy the real daemon script into the simulated submodule.
    daemon_dst = gov_bin / "ai-project-daemon"
    daemon_dst.write_text(DAEMON_PATH.read_text())
    daemon_dst.chmod(daemon_dst.stat().st_mode | stat.S_IXUSR)
    # Ship the orchestrator beside the daemon (as the governance package does).
    _make_orchestrator(gov_bin)
    return project


def test_check_command_found_in_submodule_layout(tmp_path):
    """Fresh-checkout simulation: daemon in submodule, run with --project-root."""
    project = _make_submodule_project(tmp_path)
    result = subprocess.run(
        [sys.executable, "governance/bin/ai-project-daemon",
         "--project-root", ".", "--check"],
        cwd=str(project), capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "Orchestrator found at" in result.stdout
    assert ORCH_NAME in result.stdout
    # Prove the fix: the consuming project's own bin/ has no orchestrator.
    assert not (project / "bin" / ORCH_NAME).exists()


def test_check_command_not_found(tmp_path):
    """No orchestrator anywhere → clean non-zero failure naming paths."""
    project = tmp_path / "broken-project"
    gov_bin = project / "governance" / "bin"
    gov_bin.mkdir(parents=True, exist_ok=True)
    daemon_dst = gov_bin / "ai-project-daemon"
    daemon_dst.write_text(DAEMON_PATH.read_text())
    daemon_dst.chmod(daemon_dst.stat().st_mode | stat.S_IXUSR)
    # Intentionally do NOT create an orchestrator.
    result = subprocess.run(
        [sys.executable, "governance/bin/ai-project-daemon",
         "--project-root", ".", "--check"],
        cwd=str(project), capture_output=True, text=True,
    )
    assert result.returncode == 1
    assert "Orchestrator not found" in result.stderr
