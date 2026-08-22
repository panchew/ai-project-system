"""Tests for ``bin/successful-nothing-instrument`` (Epic P12-M41-E41.2, D1/D2).

These lock in the instrument's behaviour **in both directions**, which is the whole
point of the epic. The milestone's acceptance criterion names only two positives, and
an instrument that returns FAIL unconditionally satisfies it — and would then fail the
incumbent and every candidate, so M41 would conclude on a number that no model
qualifies. The negative controls are therefore first-class here, not an afterthought.

Every case below replays a **committed, read-only** transcript whose outcome is already
known from the record, so these are regression tests against reality rather than
against a fixture someone wrote to agree with the code.
"""

import importlib.util
import json
import subprocess
from importlib.machinery import SourceFileLoader
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT_PATH = REPO_ROOT / "bin" / "successful-nothing-instrument"
RUNS = REPO_ROOT / ".ai-project" / "artifacts" / "agentic-runs"
REPLAY_SET = (
    REPO_ROOT
    / "docs"
    / "phases"
    / "P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP"
    / "P12-M41-E41.2__replay-set.json"
)

RUN_A = RUNS / "P10-M33-E33.2" / "transcript-A-qwen2.5-coder-14b.json"
RUN_B = RUNS / "P10-M33-E33.2" / "transcript-B-qwen3-coder-30b.json"
RUN_E334 = RUNS / "P10-M33-E33.4" / "transcript-qwen3-coder-30b.json"
RUN_E393 = RUNS / "P11-M39-E39.3" / "qa-transcript.json"
RUN_E393_2 = RUNS / "P11-M39-E39.3-RUN2" / "qa-transcript.json"


def _load_module():
    loader = SourceFileLoader("successful_nothing_instrument", str(SCRIPT_PATH))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def sni():
    return _load_module()


def _evaluate(sni, transcript, lane, **kw):
    case = {"transcript": str(transcript), "lane": lane}
    case.update(kw)
    return sni.evaluate(case, repo_root=str(REPO_ROOT))


# --------------------------------------------------------------- C-A, the round count


def test_tool_rounds_counts_executed_calls_not_intended_ones(sni):
    """E33.2 Run A emitted three well-formed tool calls as prose inside a ```json fence.
    The runner parsed no protocol call. The correct count is ZERO — a scraper over the
    final answer would report 3, and would report it for the run that did nothing."""
    record = _evaluate(sni, RUN_A, "epic_dev")
    assert record["counts"]["tool_rounds"] == 0
    intended = json.loads(RUN_A.read_text())["final_answer"]
    assert intended.count('"name"') == 3, "the three intended calls are still in the fence"


def test_denied_call_is_a_round_but_is_not_evidence(sni):
    """E33.2 Run B spent 3 of its 10 rounds on a `pip install -e .` its allow-list denied.
    Those are real rounds the runner spent (C-A counts them) and they support no claim."""
    record = _evaluate(sni, RUN_B, "epic_dev")
    assert record["counts"]["tool_rounds"] == 10
    denied = [c for c in record["executed_calls"] if c["denied_or_errored"]]
    assert len(denied) == 3
    assert all(c["name"] == "run_command" for c in denied)


# ------------------------------------------------------- the two negative controls


def test_negative_control_run_b_passes_with_its_counts(sni):
    """THE primary negative control. Run B exited 2 with `max_iterations_exceeded` and
    shipped mergeable work. "Run B passed" is not a result; the counts are."""
    record = _evaluate(sni, RUN_B, "epic_dev")
    assert record["verdict"] == "PASS"
    assert record["counts"]["tool_rounds"] == 10
    assert record["counts"]["files_changed"]["count"] == 2
    assert record["counts"]["files_changed"]["paths"] == [
        "local_agent_runner/__init__.py",
        "tests/test_public_api.py",
    ]


def test_negative_control_e334_passes_with_its_counts(sni):
    """The second real agentic epic. Ten rounds against another repository, migration
    written, factory and spec edited, rspec green."""
    record = _evaluate(sni, RUN_E334, "epic_dev")
    assert record["verdict"] == "PASS"
    assert record["counts"]["tool_rounds"] == 10
    assert record["counts"]["files_changed"]["count"] == 3
    assert record["counts"]["claims"]["asserted"] == 4
    assert record["counts"]["claims"]["unresolved"] == 0


def test_cross_repository_run_yields_no_uncheckable_key_claims(sni):
    """E33.4 ran against home_finance. A key claim that cannot be checked here must be
    recorded as NOT ASSERTED, never as asserted-and-unresolved — a claim that cannot be
    checked is not a claim that failed (check list §1 C-C, limit 3). Without this the
    instrument would flag a run that produced committed, green work."""
    record = _evaluate(sni, RUN_E334, "epic_dev")
    assert not [c for c in record["all_claims"] if c["class"] == "C-C3"]


# ------------------------------------------------------------ the three positives


def test_run_a_fails_the_dev_floor(sni):
    record = _evaluate(sni, RUN_A, "epic_dev")
    assert record["verdict"] == "FAIL"
    assert record["counts"]["tool_rounds"] == 0
    assert record["counts"]["files_changed"]["count"] == 0


@pytest.mark.parametrize("transcript", [RUN_E393, RUN_E393_2])
def test_e393_fails_both_qa_floor_terms_independently(sni, transcript):
    """The ruling's own reasoning: nothing is lost against the record, because E39.3's
    fabrication fails `rounds > 0` AND `claims resolve` independently. That is checked
    here rather than taken on the ruling's word."""
    record = _evaluate(sni, transcript, "epic_qa")
    assert record["verdict"] == "FAIL"
    assert record["counts"]["tool_rounds"] == 0
    assert record["counts"]["claims"]["unresolved"] > 0
    fabricated = [c["claim"] for c in record["unresolved_claims"] if c["class"] == "C-C3"]
    assert any("framework_version" in c for c in fabricated)


# ------------------------------------------------------------------- the floor shape


def test_qa_floor_records_files_changed_but_does_not_score_it(sni):
    """`bin/run-qa-agent` refuses to dispatch under a mutating tool set, so
    `files changed > 0` was a constant false on this lane — zero discriminating power,
    not a strict bar. Ruled per-lane by the CFO 2026-08-20."""
    record = _evaluate(sni, RUN_E393, "epic_qa")
    files_term = [t for t in record["floor_terms"] if t["check"].startswith("C-B")][0]
    assert files_term["scored"] is False
    assert record["counts"]["files_changed"]["count"] == 0


def test_every_verdict_stamps_the_floor_version(sni):
    """A run judged against the pre-ruling absolute floor and one judged against the
    ruled per-lane floor are not comparable results. The instrument says which it used."""
    for transcript, lane in ((RUN_A, "epic_dev"), (RUN_E393, "epic_qa")):
        assert _evaluate(sni, transcript, lane)["floor_version"] == "per-lane-ruled-2026-08-20"


def test_exit_code_is_recorded_and_never_scored(sni):
    """The anti-correlation, locked in. Run A exits 0 and FAILS; Run B exits 2 and
    PASSES. Any change that lets exit status reach the verdict breaks this test."""
    a = _evaluate(sni, RUN_A, "epic_dev", metadata=str(RUNS / "P10-M33-E33.2" / "transcript-A-qwen2.5-coder-14b__run-metadata.json"))
    b = _evaluate(sni, RUN_B, "epic_dev")
    assert a["recorded_never_scored"]["exit_code"] == 0 and a["verdict"] == "FAIL"
    assert b["verdict"] == "PASS"
    assert not any("exit" in t["check"].lower() for t in b["floor_terms"])


def test_transcript_derived_files_changed_is_declared_a_lower_bound(sni):
    """It credits no run_command side effect — E33.4's `rails db:migrate` really did
    rewrite db/schema.rb and this counter does not see it. The number can only be too
    low, so a PASS on it is sound and a FAIL on it must be named rather than reported
    flat."""
    record = _evaluate(sni, RUN_E334, "epic_dev")
    assert record["counts"]["files_changed"]["provenance"] == "transcript-derived"
    assert record["counts"]["files_changed"]["lower_bound"] is True


def test_vacuous_claims_are_recorded_not_hidden(sni):
    """Run B's final answer is one honest sentence asserting nothing. C-C passes
    vacuously and the vacuity is visible in the record instead of hiding inside a
    boolean — a short, honest final answer is not a fabrication."""
    record = _evaluate(sni, RUN_B, "epic_dev")
    assert record["counts"]["claims"]["asserted"] == 0
    assert record["counts"]["claims"]["vacuous"] is True
    assert record["counts"]["claims"]["rate"] is None


# --------------------------------------------------------------- the declared set


def test_declared_replay_set_is_five_cases_three_fail_two_pass(sni):
    declared = json.loads(REPLAY_SET.read_text())["cases"]
    assert len(declared) == 5
    assert sum(1 for c in declared if c["expected_verdict"] == "FAIL") == 3
    assert sum(1 for c in declared if c["expected_verdict"] == "PASS") == 2


def test_replay_set_verdicts_match_the_declaration(sni):
    """The whole of D2 in one assertion: every declared case is evaluated and every
    verdict is the declared one. An instrument that only flagged the positives would
    fail here on Run B and E33.4."""
    declared = json.loads(REPLAY_SET.read_text())["cases"]
    for case in declared:
        record = _evaluate(
            sni,
            REPO_ROOT / case["transcript"],
            case["lane"],
            metadata=str(REPO_ROOT / case["metadata"]) if case.get("metadata") else None,
            label=case["label"],
        )
        assert record["verdict"] == case["expected_verdict"], case["label"]


def test_unloadable_case_is_a_loud_error_never_a_skip(sni):
    """S3's defect, reproduced deliberately: a case that cannot be loaded is named and
    counted. The reported list is never shorter than the declared set."""
    with pytest.raises(sni.CaseError):
        _evaluate(sni, RUNS / "DOES-NOT-EXIST" / "transcript.json", "epic_dev")


def test_run_b_has_no_run_metadata_and_the_absence_is_recorded(sni):
    """The asymmetry S3 found: the primary negative control has a transcript and no
    run-metadata file, so a metadata-requiring harness drops it silently. Here the
    consequence surfaces as an explicit non-recoverable provenance instead."""
    assert not (RUNS / "P10-M33-E33.2" / "transcript-B-qwen3-coder-30b__run-metadata.json").exists()
    record = _evaluate(sni, RUN_B, "epic_dev")
    assert "NOT RECOVERABLE" in record["advertised_tools"]["provenance"]


def test_a_files_content_mentioning_denial_is_not_a_refusal(sni):
    """REGRESSION — the instrument was wrong here before it was right.

    The first denial pattern matched `is denied` anywhere in a tool result. E33.2 Run B
    reads `local_agent_runner/tools.py`, which is the runner's *permissions module* and
    whose content contains the denial message templates. The call was therefore scored
    as denied, and would have supported no claim citing that file.

    It changed none of the five replay verdicts — Run B asserts no claims — so the
    replay alone would never have surfaced it. It would have produced a false unresolved
    claim on any live run that reads a file discussing permissions and then cites it.
    A pattern was trusted without being falsified; that is the trap by name.
    """
    record = _evaluate(sni, RUN_B, "epic_dev")
    reads = [c for c in record["executed_calls"] if c["name"] == "read_file"]
    assert len(reads) == 3
    assert not any(c["denied_or_errored"] for c in reads)
    tools_py = [c for c in reads if c["args"].get("path", "").endswith("tools.py")]
    assert len(tools_py) == 1 and tools_py[0]["denied_or_errored"] is False


def test_worktree_count_excludes_the_runs_own_exhaust(sni, tmp_path):
    """REGRESSION — found by running a real dispatch, 2026-08-22.

    ``bin/run-dev-agent`` writes the run's transcript, context and metadata into
    ``.ai-project/artifacts/agentic-runs/<epic_id>/`` INSIDE the workspace. Git reports
    that directory as changed, so a run that produced nothing at all measured **one file
    changed**, and any run with at least one tool round would have cleared the
    ``epic_dev`` floor's C-B term without doing any work.

    Same family as the ``__pycache__`` contaminant found on the degenerate baseline: the
    harness's own exhaust counted as the model's output. The exclusion is explicit at the
    call site and every excluded path is echoed into the record, so nothing is dropped
    silently.
    """
    ws = tmp_path / "e412-dev-workspace"
    # Mirror the real fixture: .ai-project/agents/ and .ai-project/queue/ are COMMITTED,
    # which is what makes git report the new path as `.ai-project/artifacts/` rather than
    # collapsing it all the way up to `.ai-project/`. The exclusion prefix is chosen to
    # match what git actually prints for this fixture, not what it might print for
    # another one.
    (ws / ".ai-project" / "agents").mkdir(parents=True)
    (ws / ".ai-project" / "queue").mkdir(parents=True)
    (ws / ".ai-project" / "agents" / "tools.json").write_text("{}")
    (ws / ".ai-project" / "queue" / "04_epic.json").write_text("{}")
    (ws / "keep.txt").write_text("committed\n")
    for args in (["init", "-q"], ["add", "-A"]):
        subprocess.run(["git", *args], cwd=ws, check=True)
    subprocess.run(
        ["git", "-c", "user.email=t@e", "-c", "user.name=t", "commit", "-q", "-m", "base"],
        cwd=ws, check=True,
    )
    run_dir = ws / ".ai-project" / "artifacts" / "agentic-runs" / "TASK-DEV-1"
    run_dir.mkdir(parents=True)
    (run_dir / "transcript.json").write_text("{}")

    kept, dropped = sni.worktree_changed_paths(ws)
    assert kept == [".ai-project/artifacts/"] and dropped == []

    kept, dropped = sni.worktree_changed_paths(ws, exclude=(".ai-project/artifacts",))
    assert kept == [] and dropped == [".ai-project/artifacts/"]


def test_a_bare_slash_is_not_a_cited_repository_path(sni, tmp_path):
    """REGRESSION — the instrument was wrong in the DANGEROUS direction, and the first
    live epic_qa run found it.

    The run reported, correctly and from a file it had actually read, that
    `healthcheck.path` "does not start with `/`". C-C2's first filter accepted any
    backticked token containing a '/' with no whitespace, so it extracted the bare `/`
    as a cited repository path, failed to resolve it, and returned FAIL on a grounded,
    read-only, one-round run.

    That is the mirror of `return FAIL` and the same shape as M40's F5 one level up:
    a run that did the work correctly scored worse for saying so.
    """
    transcript = tmp_path / "t.json"
    transcript.write_text(json.dumps({
        "status": "completed",
        "final_answer": "8. NOT MET -- `healthcheck.path` does not start with `/`.",
        "transcript": [{"tool_call": {"name": "read_file", "args": {"path": "servicecard.yml"}},
                        "tool_result": "name: x\n"}],
        "iterations": 1, "tokens": 10, "model": "m", "duration_ms": 1,
    }))
    record = _evaluate(sni, transcript, "epic_qa")
    assert record["counts"]["claims"]["asserted"] == 0, record["all_claims"]
    assert record["verdict"] == "PASS"


def test_real_repository_paths_are_still_extracted(sni):
    """The fix must not blind C-C2. E33.4 cites four real paths in backticks and all
    four still resolve — a narrower filter that extracted nothing would 'fix' the false
    alarm by removing the check."""
    record = _evaluate(sni, RUN_E334, "epic_dev")
    c_c2 = [c for c in record["all_claims"] if c["class"] == "C-C2"]
    assert len(c_c2) == 4 and all(c["resolved"] for c in c_c2)
