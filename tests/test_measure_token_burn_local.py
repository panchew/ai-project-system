"""Tests for ``bin/measure-token-burn`` Direction C-lite local-run extraction.

Added by Epic P10-M33-E33.3 (trustworthy measurement out of the run). The E33.2
Agentic/Local run landed its transcripts in a *newer per-model layout*
(``transcript-<tag>.json`` + optional ``transcript-<tag>__run-metadata.json``,
one pair per model) rather than the single ``transcript.json`` /
``run-metadata.json`` PROVE layout the tool was originally built against. Before
E33.3's fix the tool silently skipped any run dir lacking ``run-metadata.json``,
so E33.2's real numbers (Run A 223 tok / 0 rounds; Run B 829 tok / 10 rounds)
were invisible to the measurement mechanism.

These tests lock in that (1) the old layout still yields exactly its prior
output-token numbers, and (2) the new per-model layout is captured — including
the run-status each token count is attached to (exit-code-untrust, gap G11):
Run A's ``completed``/0-round false-positive is flagged, and Run B's
metadata-less transcript records an exit-code gap instead of a skipped run.
"""

import importlib.util
import json
from importlib.machinery import SourceFileLoader
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT_PATH = REPO_ROOT / "bin" / "measure-token-burn"

_spec = importlib.util.spec_from_loader(
    "measure_token_burn", SourceFileLoader("measure_token_burn", str(SCRIPT_PATH))
)
mtb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mtb)


def _write(path, obj):
    path.write_text(json.dumps(obj), encoding="utf-8")


def _legacy_run(run_dir, *, model, exit_code, status, iterations, tokens):
    run_dir.mkdir(parents=True, exist_ok=True)
    _write(run_dir / "run-metadata.json", {"model": model, "exit_code": exit_code,
                                            "duration_ms": 20000})
    _write(run_dir / "transcript.json", {"status": status, "iterations": iterations,
                                         "tokens": tokens, "model": model,
                                         "duration_ms": 20000, "transcript": []})


def _collect(tmp_path, monkeypatch):
    monkeypatch.setattr(mtb, "REPO_ROOT", str(tmp_path))
    return {(r["run"], r["variant"]): r for r in mtb.collect_local_runs(None)}


def test_legacy_single_transcript_layout_unchanged(tmp_path, monkeypatch):
    base = tmp_path / ".ai-project" / "artifacts" / "agentic-runs"
    _legacy_run(base / "P7-M26-E26.3-PROVE", model="qwen2.5-coder:14b",
                exit_code=0, status="completed", iterations=7, tokens=404)
    runs = _collect(tmp_path, monkeypatch)
    assert len(runs) == 1
    r = runs[("P7-M26-E26.3-PROVE", None)]
    assert r["output_tokens"] == 404          # unchanged from the 1.0.0 behavior
    assert r["exit_code"] == 0
    assert r["status"] == "completed"
    assert r["iterations"] == 7
    assert r["zero_work_completion"] is False
    assert r["run_metadata_present"] is True


def test_e33_2_per_model_layout_is_captured(tmp_path, monkeypatch):
    base = tmp_path / ".ai-project" / "artifacts" / "agentic-runs"
    run_dir = base / "P10-M33-E33.2"
    run_dir.mkdir(parents=True)
    # Run A: transcript + sibling run-metadata (exit 0 / completed / 0 rounds).
    _write(run_dir / "transcript-A-qwen2.5-coder-14b.json",
           {"status": "completed", "iterations": 0, "tokens": 223,
            "model": "qwen2.5-coder:14b", "duration_ms": 18288, "transcript": []})
    _write(run_dir / "transcript-A-qwen2.5-coder-14b__run-metadata.json",
           {"model": "qwen2.5-coder:14b", "exit_code": 0, "duration_ms": 18370})
    # Run B: transcript ONLY (no metadata sibling) — exit code must become a gap.
    _write(run_dir / "transcript-B-qwen3-coder-30b.json",
           {"status": "max_iterations_exceeded", "iterations": 10, "tokens": 829,
            "model": "qwen3-coder:30b", "duration_ms": 88565,
            "transcript": [{"eval_count": 80}]})

    runs = _collect(tmp_path, monkeypatch)
    assert len(runs) == 2, "both per-model transcripts must be captured, not skipped"

    a = runs[("P10-M33-E33.2", "A-qwen2.5-coder-14b")]
    assert a["output_tokens"] == 223
    assert a["exit_code"] == 0
    assert a["status"] == "completed"
    assert a["iterations"] == 0
    # exit-code-untrust: completed + 0 rounds is a false-positive success.
    assert a["zero_work_completion"] is True

    b = runs[("P10-M33-E33.2", "B-qwen3-coder-30b")]
    assert b["output_tokens"] == 829          # runner's own total, not eval sum
    assert b["exit_code"] is None             # no metadata sibling => recorded gap
    assert b["run_metadata_present"] is False
    assert b["status"] == "max_iterations_exceeded"
    assert b["iterations"] == 10
    assert b["zero_work_completion"] is False
    # falls back to transcript-reported model/duration when metadata is absent
    assert b["model"] == "qwen3-coder:30b"
    assert b["duration_ms"] == 88565


def test_eval_count_fallback_when_no_top_level_tokens(tmp_path, monkeypatch):
    base = tmp_path / ".ai-project" / "artifacts" / "agentic-runs"
    run_dir = base / "P0-M0-E0.0"
    run_dir.mkdir(parents=True)
    _write(run_dir / "transcript-A-m.json",
           {"status": "completed", "iterations": 2, "model": "m",
            "duration_ms": 100,
            "transcript": [{"eval_count": 100}, {"eval_count": 50}, {"noise": 1}]})
    runs = _collect(tmp_path, monkeypatch)
    r = runs[("P0-M0-E0.0", "A-m")]
    assert r["output_tokens"] == 150          # summed per-turn eval_count
