---
task: TASK-DEV-1
type: ground-truth
lane: epic_dev
last_updated: 2026-08-22
---

# TASK-DEV-1 — the directional check, committed before any run

## The check

**`python3 -m pytest tests/test_parse_duration.py` in the instantiated workspace, after
the run. The score is `tests_passed` out of `20`.**

Mechanical, not a quality judgment (Binding Constraint 3). It is the term E41.3's
relative bar attaches to — *no worse on every objective check and strictly better on at
least one* — because **none of the instrument's three counters can order candidates**:
more tool rounds is not better, a larger diff is not better, and only the claims
**rate** is directional. Without a per-task directional check E41.3 has almost nothing
to compare (Epic spec §Scope 4).

**Recorded alongside:** whether `tests/` was modified (the DoD forbids it — a run that
edits the test to make it pass scores its passes, and the modification is recorded as a
disqualifying note, because the check would otherwise reward defeating it).

## Solvability, established before the run

**20 / 20** with a reference implementation, measured on this host 2026-08-22, Python
3.14, in a throwaway copy of the workspace outside this repository. So a failing score
is a fact about the model, not about the task.

The reference lives here as `reference-solution__NOT-INSTANTIATED.py`. **It is never
copied into a run workspace** — `bin/e412-instantiate-dev-workspace` copies `workspace/`
only, and this file is not under `workspace/`.

## Blinding

The dev lane's tool set is scoped to `*/e412-dev-workspace/**` (the instantiated
workspace) and nothing else, so **a dev run cannot read this repository at all** — this
ground-truth file included. The blinding is structural, not a convention.

## The 20 cases

| # | Input | Expected |
|---:|---|---|
| 1 | `"45s"` | `45` |
| 2 | `"0s"` | `0` |
| 3 | `"007s"` | `7` |
| 4 | `"90m"` | `5400` |
| 5 | `"1h30m"` | `5400` |
| 6 | `"2d4h"` | `187200` |
| 7 | `"1w"` | `604800` |
| 8 | `"1w1d1h1m1s"` | `694861` |
| 9 | `"  1h  "` | `3600` |
| 10 | `"100h"` | `360000` |
| 11 | `"1m"` | returns an `int` |
| 12–19 | `""`, `"90"`, `"h"`, `"5y"`, `"-5s"`, `"30m1h"`, `"1h1h"`, `"1h 30m"` | `ValueError` |
| 20 | `90` (an int) | `TypeError` |
