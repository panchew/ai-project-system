---
project: ai-project-system
phase: P10
milestone: M35
type: note
status: active
issuer_chat: Epic Execution Chat (P10-M35-E35.5)
issued_to: Milestone Chat (P10-M35) → Phase Chat (P10)
last_updated: 2026-07-31
---

# Carry-Forward Note — P10-GH-10: a flaky suite test makes "full suite green" weaker evidence than it reads

**Recorded, not fixed.** Changing `tests/test_artifact_router.py` is a framework *capability* change,
which the bump procedure's Failure Mode 4 and E34.2's handling of P10-GH-6 both establish as out of
scope for an epic whose deliverable is evidence. E35.5 measured it, reported it, and filed this.

> **Identifier caveat:** this Epic assigned **P10-GH-10** because P10-GH-9 was the highest previously
> recorded. **Gap numbering belongs to the Milestone Chat** — renumber if it collides.

---

## The finding

During E35.5's closing verification, one full-suite run failed:

```
FAILED tests/test_artifact_router.py::test_daemon_extensions_error_branches
1 failed, 365 passed in 23.88s
```

Nothing in that run's diff could plausibly have caused it: the only change since the immediately
preceding clean 366/0/0 run was the addition of one Markdown delivery notice.

## What was measured

| Check | Result |
|---|---|
| The failing test, in isolation | **passes** — `1 passed in 0.11s` |
| Full suite, immediately before the failure | **366 / 0 / 0** (twice) |
| Full suite, immediately after the failure | **366 / 0 / 0** (six consecutive runs) |
| Observed rate | **1 failure in 10 full-suite runs** |

The failing run was the one executed directly after `docker start comfyui` and an Ollama model unload
— i.e. under transient system load. That is a correlation observed once, not a demonstrated cause.

## Why the test is a plausible candidate for load sensitivity

`test_daemon_extensions_error_branches` (`tests/test_artifact_router.py:687`):

- patches **`time.sleep` globally** and exits a daemon loop by raising `StopLoopException` from the
  patched `sleep`;
- patches **`Path.exists` globally** with `autospec=True`, discriminating on `self_path.name`;
- drives `daemon_artifact_monitoring_loop(...)` with `interval=0.1`;
- asserts against filesystem state under `tmp_path` (`.failed/fail_proc.md` present,
  `.processed/is_a_directory.md` absent).

A test that globally patches the clock and the filesystem predicate, runs a loop, and then asserts on
files is a familiar shape for an intermittent failure under load. **This is a hypothesis. E35.5 did
not root-cause it**, did not capture the failing assertion's detail, and did not modify the test.

## Why it matters beyond one red run

**Every epic in this phase asserts "full suite green — no regressions, no new skips" as a Definition
of Done item.** That assertion is only as good as the suite's determinism. At roughly 1-in-10:

- an epic that measures **once** can report a green it did not reliably have, or attribute a
  pre-existing flake to its own change and go hunting for a defect it did not introduce;
- the failure mode is **asymmetric and silent** — a spurious red costs investigation time, but a green
  measured once simply looks fine;
- it is the **same class of problem this milestone has been circling**: exit-code untrust (M33, where
  exit 0 meant zero work and exit 2 meant complete work) and the two-sided block-detection failure
  recorded as **P10-GH-7**. A signal treated as authoritative that does not always mean what it says.

There is a small irony worth naming: E35.5 spent its execution establishing that a reviewer must read
the evidence rather than trust the status code, and then hit a status code that did not mean what it
said, in its own suite.

## Candidate directions (not decided here)

1. **Root-cause it.** Capture the failing assertion under `-p no:randomly`, repeated runs, and load.
   Cheapest path to knowing whether it is the global `time.sleep`/`Path.exists` patching, test-order
   dependence, or genuine timing.
2. **Narrow the patching.** Patch `lib.daemon_extensions.time.sleep` rather than `time.sleep`
   globally, and scope the `Path.exists` patch to the module under test. Likely removes the class of
   interference without weakening coverage.
3. **Make the loop exit deterministic.** Exit `daemon_artifact_monitoring_loop` via an explicit
   iteration bound or injected stop condition instead of raising from a patched clock.
4. **Quarantine and track.** Mark it `flaky`/`xfail(strict=False)` so it stops polluting the green
   signal, and carry the defect separately. Cheapest, but it hides the very signal this note is about.

**No recommendation from this level.** Option 1 must precede 2–4 on the evidence; whether the suite's
determinism is worth the work is a framework judgment above an Epic.

## Explicitly not done here

- `tests/test_artifact_router.py` **not modified** — empty diff on this branch.
- **Not root-caused.** One observation, nine clean runs, and a code-shape hypothesis. No repeated
  stress run, no captured assertion detail.
- **No other test audited** for the same pattern. Other tests may patch globals similarly; no sweep
  was performed.
- **E35.5's own suite claims stand** and were not softened: 366/0/0 baseline and 366/0/0 after, each
  measured, with this transient reported alongside rather than in place of them.
