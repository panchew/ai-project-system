---
task: TASK-QA-1
type: ground-truth
lane: epic_qa
last_updated: 2026-08-22
---

# TASK-QA-1 — the directional check, committed before any run

## The artifact and its planted defects

`work/servicecard.yml` assessed against `standard/TASK-QA-1__standard__servicecard-spec.md`
§ *Validation Rules* (twelve numbered rules).

**Five of the twelve rules are violated. Seven are satisfied.** Machine-verified by
`harness/verify-qa-ground-truth.py`, run on this host 2026-08-22 — the ground truth is
**measured**, not asserted:

```
rules: 12    MET: 7    VIOLATED: 5
violated: 8, 9, 10, 11, 12
met:      1, 2, 3, 4, 5, 6, 7
```

| Rule | Verdict | Why |
|---:|---|---|
| 8 | **VIOLATED** | `healthcheck.path` is `healthz` — it does not start with `/` |
| 9 | **VIOLATED** | `healthcheck.timeout_s` is `45`, outside `1`–`30` |
| 10 | **VIOLATED** | `dependencies` contains `Redis-Cache`, which has uppercase letters |
| 11 | **VIOLATED** | `region` is `us-central`, not one of `us-east`/`us-west`/`eu-central` |
| 12 | **VIOLATED** | `retries` is a top-level key the standard does not list |
| 1–7 | satisfied | valid mapping; `name`, `owner`, `tier`, `replicas`, `port` and the `healthcheck` shape all conform |

**The five are deliberately of different kinds** — a missing prefix, a range, a pattern
inside a list element, an enum, and an extra key — so a run that catches one shape and
misses the rest is distinguishable from one that reads the file properly.

## The check — two objective, directional terms

| Term | Range | Direction | Definition |
|---|---|---|---|
| **catches** | 0–5 | higher is better | violated rules the run reports `NOT MET` |
| **false alarms** | 0–7 | lower is better | satisfied rules the run reports `NOT MET` |

`UNCLEAR` is neither a catch nor a false alarm and is recorded separately, so a run
cannot buy a clean false-alarm count by hedging every line — the hedges are visible.

**This is not the back-test.** Same shape of scoring, different instrument, different
task: E41.4's back-test is a separate measurement on a separate transport.

**The verdict line (`VERDICT: PASS`/`FAIL`) is recorded and is NOT the score.** No
model-generated judgment is load-bearing (E39.1). A run that reports the right verdict
for no reason scores exactly what its per-rule lines score.

## Blinding — measured, not merely intended

The QA tool set's `allow_paths` is `*/ai-project-system/**`, so **this repository is
structurally readable by a QA run** and blinding cannot rest on path scoping the way the
dev lane's does. Two measures instead, and both are recorded:

1. **This ground-truth file is moved out of the working tree for the duration of each
   dispatch** and restored afterwards. It stays committed — "the bar is committed before
   the run it judges" is satisfied by the commit, not by the file being on disk while the
   model runs.
2. **The auditable control:** the instrument records **every executed tool call** with its
   arguments. If a run read anything outside the standard and the work file, it is in the
   transcript, and the run is disqualified with its reason stated.

## The scorer

`harness/score-qa-run.py` — parses the run's per-rule lines and scores them against the
table above. Committed with the task so **E41.3 runs the identical task and the identical
scoring**, not a paraphrase of either.
