#!/usr/bin/env python3
"""E39.2 — run E39.1's completion judgment against the six preserved runs.

Pre-registered mechanism SHA: drivr@715099cb94a9f7c010cde1c22e455d4b41161a14
Pre-registration commit in this repo: bc89db5 (committed BEFORE this file existed).

This script is the EPIC'S INSTRUMENT, not the mechanism. It reads the preserved artifacts
read-only, calls the public API described in drivr/docs/completion-judgment.md §7, and
writes its raw output next to itself. It never edits, normalizes or regenerates a
preserved artifact.

Run from the repository root:

    PYTHONPATH=/home/panchew/soft-dev/drivr \\
      python3 .ai-project/artifacts/validation-runs/P11-M39-E39.2/validate_completion_judgment.py

Ordering is enforced by this file, not by discipline: the binding pair is run and its
verdicts are frozen into the results before any held-out case is loaded (see main()).
"""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from drivr.judgment import from_runner_transcript, judge_completion

REPO = Path(__file__).resolve().parents[4]
RUNS = REPO / ".ai-project/artifacts/agentic-runs"
OUT = Path(__file__).resolve().parent
DRIVR = Path("/home/panchew/soft-dev/drivr")

PREREGISTERED_SHA = "715099cb94a9f7c010cde1c22e455d4b41161a14"

# --- The corpus -----------------------------------------------------------------------
# `sidecar: None` means the run has no run-metadata file. That is an ABSENT input and is
# recorded as absent — never as a negative finding (E39.2 spec F1; Run B).
# `truth_record` is the committed governance record the ground truth was read from.

BINDING = [
    {
        "case": "E33.2-run-A",
        "dir": "P10-M33-E33.2",
        "transcript": "transcript-A-qwen2.5-coder-14b.json",
        "sidecar": "transcript-A-qwen2.5-coder-14b__run-metadata.json",
        "truth": "did-not-complete",
        "truth_record": ".ai-project/artifacts/agentic-runs/P10-M33-E33.2/run-record.md",
        "required_reading": "did-not-complete",
    },
    {
        "case": "E33.4",
        "dir": "P10-M33-E33.4",
        "transcript": "transcript-qwen3-coder-30b.json",
        "sidecar": "run-metadata.json",
        "truth": "completed",
        "truth_record": ".ai-project/artifacts/agentic-runs/P10-M33-E33.4/run-record.md",
        "required_reading": "completed",
    },
]

HELD_OUT = [
    {
        "case": "E33.2-run-B",
        "dir": "P10-M33-E33.2",
        "transcript": "transcript-B-qwen3-coder-30b.json",
        "sidecar": None,  # ABSENT — the only case in the corpus with no sidecar
        "truth": "completed",
        "truth_record": ".ai-project/artifacts/agentic-runs/P10-M33-E33.2/run-record.md",
    },
    {
        "case": "P7-M26-E26.3-PROVE",
        "dir": "P7-M26-E26.3-PROVE",
        "transcript": "transcript.json",
        "sidecar": "run-metadata.json",
        "truth": "completed",
        "truth_record": (
            "docs/phases/P7__Agentic_Execution_and_Default_On_Visuals/"
            "P7-M26-E26.3__delivery-notice.md"
        ),
    },
    {
        "case": "P9-M31-E31.1-PROVE",
        "dir": "P9-M31-E31.1-PROVE",
        "transcript": "transcript.json",
        "sidecar": "run-metadata.json",
        "truth": "completed",
        "truth_record": (
            "docs/phases/P9__Context_Handling_and_Token_Efficiency/"
            "P9-M31-E31.1__demonstration-evidence.md"
        ),
    },
    {
        "case": "P9-M31-E31.2-PROVE",
        "dir": "P9-M31-E31.2-PROVE",
        "transcript": "transcript.json",
        "sidecar": "run-metadata.json",
        "truth": "completed",
        "truth_record": (
            "docs/phases/P9__Context_Handling_and_Token_Efficiency/"
            "P9-M31-E31.2__run-record.md"
        ),
    },
]

# --- Scoring conventions, fixed before any held-out case is read ----------------------
# `Reading` is three-valued by construction (drivr/docs/completion-judgment.md §5), so
# "matches ground truth" needs a declared convention or the score can be chosen after the
# fact. Both are reported; neither is preferred.
#
#   strict     — Reading equals the ground truth. UNDETERMINED counts as a MISS.
#   non-contra — Reading does not assert the opposite of the ground truth.
#                UNDETERMINED makes no claim and so cannot contradict.
#
# This convention is INHERITED, not invented here: E39.1's description, committed at
# 715099c BEFORE this epic began, already states that EFFECTS_UNVERIFIED is the correct
# IN-RUN reading for the four runs whose ground truth was established out-of-run.


def score(reading: str, truth: str) -> tuple[str, str]:
    strict = "hit" if reading == truth else "miss"
    if reading == "undetermined":
        non_contra = "no-claim"
    elif reading == truth:
        non_contra = "agrees"
    else:
        non_contra = "CONTRADICTS"
    return strict, non_contra


def sha_of(path: Path) -> str:
    return subprocess.run(
        ["git", "-C", str(DRIVR), "rev-parse", "HEAD"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()


def read_sidecar(spec: dict) -> dict | None:
    """Read the run-metadata sidecar. This is where exit_code lives, and NOWHERE ELSE.

    The harness reads it so the evidence record can show the exit code was AVAILABLE at
    validation time and was still not used. A transcript-only validation would satisfy
    'does not rest on the exit code' by accident (E39.2 spec F2, Trap 2).
    """
    if spec["sidecar"] is None:
        return None
    return json.loads((RUNS / spec["dir"] / spec["sidecar"]).read_text())


def items(verdict, attr):
    return [
        {"name": i.name, "detail": i.detail, "verbatim": i.verbatim}
        for i in getattr(verdict, attr)
    ]


def run_case(spec: dict) -> dict:
    payload = json.loads((RUNS / spec["dir"] / spec["transcript"]).read_text())
    sidecar = read_sidecar(spec)

    record = from_runner_transcript(payload, origin=spec["case"])
    verdict = judge_completion(record)
    reading = verdict.reading().value

    strict, non_contra = score(reading, spec["truth"])

    result = {
        "case": spec["case"],
        "transcript": f"{spec['dir']}/{spec['transcript']}",
        "sidecar": f"{spec['dir']}/{spec['sidecar']}" if spec["sidecar"] else None,
        "verdict": verdict.completion.value,
        "reading": reading,
        "rule": verdict.rule,
        "source": verdict.source,
        "ground_truth": spec["truth"],
        "ground_truth_record": spec["truth_record"],
        "score_strict": strict,
        "score_non_contradiction": non_contra,
        # --- what the mechanism did with each input ---
        "inputs_used": items(verdict, "inputs_used"),
        "inputs_ignored": items(verdict, "inputs_ignored"),
        "inputs_absent": items(verdict, "inputs_absent"),
        "notes": items(verdict, "notes"),
        # --- the two ruled-out signals, shown AVAILABLE ---
        "available_and_ignored": {
            "exit_code": {
                "value": sidecar.get("exit_code") if sidecar else None,
                "authoritative_file": (
                    f"{spec['dir']}/{spec['sidecar']}" if spec["sidecar"] else None
                ),
                "availability": "read from the sidecar by this harness"
                if sidecar
                else "ABSENT — this run has no sidecar; the exit code does not exist "
                     "anywhere in the corpus for this case",
            },
            "status": {
                "value": payload.get("status"),
                "authoritative_file": f"{spec['dir']}/{spec['transcript']}",
                "availability": "read from the transcript by this harness",
            },
        },
        # --- F3: the fields the two files disagree on ---
        "duration_ms": {
            "transcript": payload.get("duration_ms"),
            "sidecar": sidecar.get("duration_ms") if sidecar else None,
            "delta_ms": (
                sidecar["duration_ms"] - payload["duration_ms"]
                if sidecar and "duration_ms" in sidecar
                else None
            ),
            "authoritative_for_this_validation": "transcript",
        },
        "target_epic_id": sidecar.get("epic_id") if sidecar else None,
        "iterations": payload.get("iterations"),
        "transcript_entries": len(payload.get("transcript") or []),
        "explain": verdict.explain(),
    }
    if spec.get("required_reading"):
        result["required_reading"] = spec["required_reading"]
        result["binding_result"] = (
            "PASS" if reading == spec["required_reading"] else "FAIL"
        )
    return result


def independence_probe(spec: dict) -> dict:
    """Demonstrate — not assert — that `status` is not read.

    The transcript projection has NO channel for the exit code (proven separately below),
    so the exit code cannot be demonstrated by injection. `status` can: it is a real field
    of the transcript, it IS projected into `annotations`, and rewriting it to every value
    observed anywhere in the corpus must leave the verdict where it is.
    """
    payload = json.loads((RUNS / spec["dir"] / spec["transcript"]).read_text())
    baseline = judge_completion(from_runner_transcript(payload, origin=spec["case"]))

    observed_statuses = ["completed", "max_iterations_exceeded"]
    observed_final_answers = [
        "I'm sorry, but I can't assist with that request.",
        "I have completed the task successfully.",
        '{"tool": "write_file", "args": {}}',
        None,
    ]

    moved = []
    trials = 0
    for st in observed_statuses:
        for fa in observed_final_answers:
            mutated = dict(payload)
            mutated["status"] = st
            if fa is None:
                mutated.pop("final_answer", None)
            else:
                mutated["final_answer"] = fa
            # exit_code injected too — see exit_code_has_no_channel below
            mutated["exit_code"] = 0 if trials % 2 == 0 else 2
            v = judge_completion(from_runner_transcript(mutated, origin=spec["case"]))
            trials += 1
            if (v.completion, v.rule) != (baseline.completion, baseline.rule):
                moved.append(
                    {"status": st, "final_answer": fa,
                     "verdict": v.completion.value, "rule": v.rule}
                )

    # Does the transcript projection read an injected exit_code at all?
    injected = dict(payload)
    injected["exit_code"] = 999
    channel = "exit_code" in from_runner_transcript(injected, origin="probe").annotations

    return {
        "case": spec["case"],
        "baseline_verdict": baseline.completion.value,
        "baseline_rule": baseline.rule,
        "mutation_trials": trials,
        "verdict_moved_on": moved,
        "verdict_invariant": not moved,
        "exit_code_has_no_channel_in_transcript_projection": not channel,
    }


def main() -> int:
    started = datetime.now(timezone.utc).isoformat(timespec="seconds")
    final_sha = sha_of(DRIVR)

    out: dict = {
        "epic": "P11-M39-E39.2",
        "run_started_utc": started,
        "preregistered_sha": PREREGISTERED_SHA,
        "final_sha": final_sha,
        "sha_identical": final_sha == PREREGISTERED_SHA,
        "mechanism": "drivr.judgment.judge_completion(from_runner_transcript(...))",
        "python": sys.version.split()[0],
    }

    # STEP 1 — BINDING PAIR. Run and frozen before any held-out case is loaded.
    out["binding"] = [run_case(s) for s in BINDING]
    out["binding_gate"] = (
        "PASS" if all(c["binding_result"] == "PASS" for c in out["binding"]) else "FAIL"
    )
    print(f"[step 1] binding pair: {out['binding_gate']}")
    for c in out["binding"]:
        print(f"         {c['case']:<22} {c['reading']:<18} "
              f"(required {c['required_reading']}) -> {c['binding_result']}")

    # STEP 2 — HELD OUT. Only now, and never tuned against.
    out["held_out"] = [run_case(s) for s in HELD_OUT]
    print("[step 2] held out:")
    for c in out["held_out"]:
        print(f"         {c['case']:<22} {c['reading']:<18} truth={c['ground_truth']:<14} "
              f"strict={c['score_strict']:<5} non-contra={c['score_non_contradiction']}")

    # STEP 3 — constraint-2 demonstration, on all six.
    out["independence"] = [independence_probe(s) for s in BINDING + HELD_OUT]
    print("[step 3] independence probe:")
    for p in out["independence"]:
        print(f"         {p['case']:<22} trials={p['mutation_trials']:<3} "
              f"invariant={p['verdict_invariant']} "
              f"exit_code_channel_absent={p['exit_code_has_no_channel_in_transcript_projection']}")

    # Scores, against the declared conventions.
    every = out["binding"] + out["held_out"]
    out["scores"] = {
        "strict_hits": sum(c["score_strict"] == "hit" for c in every),
        "strict_total": len(every),
        "contradictions": sum(
            c["score_non_contradiction"] == "CONTRADICTS" for c in every
        ),
        "no_claim": sum(c["score_non_contradiction"] == "no-claim" for c in every),
        "always_completed_baseline_strict": "5/6",
        "always_completed_baseline_binding": "1/2",
    }
    print(f"[scores] strict {out['scores']['strict_hits']}/{out['scores']['strict_total']} "
          f"| contradictions {out['scores']['contradictions']} "
          f"| no-claim {out['scores']['no_claim']} "
          f"| always-completed baseline 5/6 and 1/2")

    out["final_sha_after_all_cases"] = sha_of(DRIVR)
    out["mechanism_unchanged_across_the_whole_validation"] = (
        out["final_sha_after_all_cases"] == PREREGISTERED_SHA
    )

    (OUT / "verdicts.json").write_text(json.dumps(out, indent=2) + "\n")
    (OUT / "verdicts-explain.txt").write_text(
        "\n\n".join(
            f"===== {c['case']} ({'BINDING' if 'binding_result' in c else 'HELD OUT'}) =====\n"
            + c["explain"]
            for c in every
        )
        + "\n"
    )
    print(f"[done] wrote verdicts.json and verdicts-explain.txt; "
          f"final SHA {out['final_sha_after_all_cases']}")
    return 0 if out["binding_gate"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
