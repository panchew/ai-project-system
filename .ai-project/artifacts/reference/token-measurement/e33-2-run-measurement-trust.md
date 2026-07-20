---
project: ai-project-system
phase: P10
milestone: M33
epic: E33.3
type: measurement-trust-record
status: recorded
last_updated: 2026-07-20
derived_from: .ai-project/artifacts/agentic-runs/P10-M33-E33.2/run-record.md
---

# E33.3 — Trustworthy measurement out of E33.2's run

This is Epic P10-M33-E33.3's governance record: the **captured burn/validation data** from
E33.2's real Agentic/Local run, the **validation** of `bin/measure-token-burn` against it, the
**sizing decision** with its basis, and the **explicit honesty judgment** on whether the run's
numbers can be trusted. It closes P9-GH-2 (`measure-token-burn` cannot verify its own claims) **to
the extent trusting E33.2's numbers requires** — no more (Non-Goals; Hard Constraint).

Every number below traces to E33.2's committed run artifacts. Where a number could not be captured,
that is recorded as a gap — no value is backfilled from the banned 24K/157K estimates or any
assumption (Acceptance Criterion 2; E30.1 discipline).

---

## 1. Captured burn/validation data (from E33.2's run)

Two runs of the *same* task on the same Ollama runtime, differing only in model (E33.2 run record
§4). Ground-truth source in parentheses for each cell.

| | Run A — `qwen2.5-coder:14b` | Run B — `qwen3-coder:30b` |
|---|---|---|
| Output tokens | **223** (transcript-A `tokens`; run record §4) | **829** (transcript-B `tokens`; run record §4) |
| Tool rounds (iterations) | **0** (transcript-A `iterations`) | **10** (transcript-B `iterations`) |
| Duration | 18.3 s (transcript 18288 ms / metadata 18370 ms) | 88.6 s (transcript 88565 ms) |
| End-to-end throughput | ~12.2 tok/s (run record §4) | ~9.4 tok/s (run record §4) |
| Runner status | `completed` (transcript-A) | `max_iterations_exceeded` (transcript-B) |
| Exit code | `0` (transcript-A `__run-metadata.json`) | **GAP** — no `__run-metadata.json` for Run B; run record §4 states exit 2 in prose, but it is **not persisted** in the run artifacts |
| Actual work produced | **none** — plan-as-prose, 0 files changed (run record §4; SN-3 mode) | correct, complete, **green** (suite 210/1 at target `4ec1e8f`) |

**Run-status trust reading (the point of the capture):**

- **Run A is a false-positive success.** Exit 0 / `completed`, yet 0 tool rounds and no work — a real
  token count (223) attached to a run-status that did nothing. Machine-flagged
  (`zero_work_completion = true`).
- **Run B is a false-negative failure.** `max_iterations_exceeded` (and exit 2 per the run record),
  yet the work was correct and green. This half is **not machine-decidable** from the transcript —
  it required the human review E33.2 already performed. Recorded as a caveat (gap G11), not asserted
  by the tool.

Aggregated numbers only; no raw paid-session content imported (privacy, carried from E30.1). The
per-model transcripts already live under E33.2's run-record dir; this record cites/derives from them.

---

## 2. Validation of `measure-token-burn` against that data

**Method:** point the tool's Direction C-lite path (`collect_local_runs`) at E33.2's committed run
artifacts and compare its output to the ground truth in §1 (spec §Execution Notes: "start by
pointing the tool at E33.2's artifacts").

### Finding — before any change: the run was silently dropped

`collect_local_runs` globbed each run dir for exactly `transcript.json` + `run-metadata.json` and
**`continue`d past any dir without `run-metadata.json`**. E33.2's dir uses a newer per-model layout
(`transcript-A-<model>.json`, `transcript-A-<model>__run-metadata.json`, `transcript-B-<model>.json`)
— none named `run-metadata.json`. Result, verified on `milestone/M33` before the fix:

```
collect_local_runs() -> 3 runs   # only the OLD PROVE runs
  P7-M26-E26.3-PROVE, P9-M31-E31.1-PROVE, P9-M31-E31.2-PROVE
  (P10-M33-E33.2 absent — silently skipped, no warning)
```

So the tool captured **zero** of E33.2's numbers. This is not a wrong number; it is a **missing**
number with no signal that anything was dropped — the worst failure mode for a run-first measurement
discipline (a run's numbers never reach the dataset, and nothing says so). It also never recorded the
run-status a token count is attached to, so even the runs it *did* capture carried no
exit-code-untrust signal.

### After the proportionate fix: captured, with run-status attached

The tool now recognizes the per-model layout and records exit/status/rounds. Verified output
(`bin/measure-token-burn` §5, regenerated to a scratch location — the committed dataset is not
rewritten here, see §3):

| run | variant | model | output tokens | exit | status | rounds | zero-work? |
|---|---|---|---|---|---|---|---|
| P10-M33-E33.2 | A-qwen2.5-coder-14b | qwen2.5-coder:14b | **223** | 0 | completed | 0 | **⚠ yes** |
| P10-M33-E33.2 | B-qwen3-coder-30b | qwen3-coder:30b | **829** | GAP → G11 | max_iterations_exceeded | 10 | no |
| P7-M26-E26.3-PROVE | — | qwen2.5-coder:14b | 404 | 0 | completed | 7 | no |
| P9-M31-E31.1-PROVE | — | qwen2.5-coder:14b | 759 | 0 | completed | 8 | no |
| P9-M31-E31.2-PROVE | — | qwen2.5-coder:14b | 837 | 2 | max_iterations_exceeded | 10 | no |

**Match check vs. §1 ground truth:** Run A 223 tok / 0 rounds ✅; Run B 829 tok / 10 rounds ✅. The
old three PROVE runs are **unchanged** (404 / 759 / 837) — backward-compatible; they additionally
gain run-status fields (note P9-M31-E31.2's exit 2 / `max_iterations_exceeded` was in the data all
along but never surfaced). Run A's false-positive is now flagged; Run B's exit code is honestly a
gap (no metadata file), with its `max_iterations_exceeded` status still captured from the transcript.

---

## 3. Sizing decision (with its basis)

**Decision: proportionate fix to `bin/measure-token-burn` (not validation-only).**

**Basis — what in the run's numbers drove it:** validation-only would have been correct had the tool
already reproduced E33.2's numbers. It did not — it reproduced **none** of them (silent zero
coverage, §2). For the run's numbers to be trustworthy at all they must first be *captured*, so the
minimal work that makes them trustworthy is the layout fix, plus attaching the run-status that E33.2
explicitly fed forward as a first-class trust case (exit-code-untrust). That is exactly the extent
delivered; nothing beyond it.

**Bounded to the run's trust requirement (what was deliberately NOT done):**

- **No prompt/input-token measurement (blind spot G9).** The runner still records output `eval_count`
  only; that is a runner-side gap, not something trusting *this run's output numbers* requires.
  Left as the standing G9 gap.
- **No automated work-correctness / false-negative detector.** Run B's "failure exit but good work"
  needed human review; the tool records exit/status/rounds but does not guess correctness (gap G11).
- **The committed `token-burn-dataset.json/.md` is not regenerated here.** A full regen re-parses
  today's paid sessions and would rewrite the E30.1 corpus/paid numbers — forbidden by Non-Goals
  ("does not revise the P9 corpus"). The fix ensures the *next* authorized full run folds E33.2 in;
  this epic captures E33.2's numbers in *this* record instead. Deliberate boundary, recorded here.
- No `.ai-project.yml` `models:` change, no `governance/` change, no runner change, no edit to
  E33.1/E33.2 surfaces (read-only inputs).

**Change surface:** `bin/measure-token-burn` (Direction C-lite: `collect_local_runs` generalized +
new `_build_run_entry`/`_load_json` helpers; run-status fields; new gap record G11; §5 renderer;
`SCRIPT_VERSION` 1.0.0 → 1.1.0) and its new test `tests/test_measure_token_burn_local.py`. Behavior
contract preserved: reads the run artifacts **read-only**, writes only its dataset files.

---

## 4. Explicit honesty judgment (non-negotiable — never skipped)

> **`measure-token-burn`'s numbers for E33.2's run CAN now be trusted — the token magnitudes (Run A
> 223, Run B 829) and their tool-round counts (0 / 10), each captured directly from the run's own
> transcripts and matching the run record's ground truth — but ONLY when read together with the
> run-status each is attached to, which the tool now records and, for Run A, flags. They could NOT
> be trusted before this epic: the tool silently dropped the entire run.**

Because:

1. **The magnitudes are real and now captured, not estimated.** 223 and 829 come straight from the
   runner's own reported `tokens`, cross-checked against the run record (§1–§2). No 24K/157K
   backfill anywhere.
2. **A bare magnitude was the untrustworthy part, and that is now fixed.** Run A's 223 tokens looks
   like a normal small run until you see it did **0 rounds under a false-positive `completed`** — the
   number is real but represents a plan emitted as prose, not epic work. The tool now attaches and
   flags that status (`zero_work_completion`), so the number can no longer be read as "an epic's
   worth of work for 223 tokens."
3. **What still cannot be fully trusted is explicitly bounded, not hidden.** Run B's exit code is a
   recorded **gap** (no metadata file persisted for it), and its "failure status but good work"
   false-negative is a human-review fact the tool does not and cannot derive (gap G11). These are
   recorded as gaps, not papered with guesses.

**Net:** P9-GH-2 is closed for E33.2's run to the extent M33 needs — the run's numbers are captured
and carry their trust context. Residual measurement-trust work beyond this run's requirement (G9
local input tokens; a general self-verification harness for the paid dataset) is **recorded here as
remaining, not silently completed or dropped** (spec Notes).

---

## 5. Traceability index

| Claim | Source (on `milestone/M33`) |
|---|---|
| Run A 223 tok / 0 rounds / completed / exit 0 | `.ai-project/artifacts/agentic-runs/P10-M33-E33.2/transcript-A-qwen2.5-coder-14b.json` (+ `__run-metadata.json`); run record §4 |
| Run B 829 tok / 10 rounds / max_iterations_exceeded | `.ai-project/artifacts/agentic-runs/P10-M33-E33.2/transcript-B-qwen3-coder-30b.json`; run record §4 |
| Run B exit 2 (prose only, not in artifacts) | `P10-M33-E33.2/run-record.md` §4; `P10-M33-E33.2__runtime-decision.md` §Review burden |
| exit-code-untrust feed-forward | `P10-M33-E33.2__runtime-decision.md` §Feed-forward to E33.3 |
| Tool pre-fix skipped E33.2 / post-fix captures it | this record §2; `bin/measure-token-burn` `collect_local_runs`; `tests/test_measure_token_burn_local.py` |
| Suite green (363 → 366, no new skips) | `tests/` (`pytest -q`) |
