---
project: ai-project-system
phase: P11
milestone: M38
epic: E38.6
type: reference
status: complete
last_updated: 2026-08-14
---

# Judgment (resubmission) — Local/Paid Controlled Comparison (E38.6)

## Verdict

**On the one task, on this material, the paid arm (claude-opus-5) produced a CATCH and the
local arm (qwen3-coder:30b) produced a MISS.** Both runs are valid, protocol-conforming, and
comparable.

## The valid result

| | Local run 2 | Paid run 2 |
|---|---|---|
| Fleet warning total | **10 (wrong; correct is 12)** | **12 (correct)** |
| Raw total | 14 | 14 |
| Excluded contribution | not correctly attributed | 2 (correct) |
| Structural invariant test | absent | present (`raw == fleet + excluded`) |
| Verdict | **MISS** | **CATCH** |

The paid arm derived the fleet total two independent ways (sum of per-project warnings; sum
of the schema-drift occurrence counts), attributed the 2-warning gap to the two worktree
checkouts of `ai-project-system`, and added 8 tests guarding the split. The local arm
separated the totals but computed the fleet total **wrong** (10 instead of 12) and
mis-attributed the gap to the unenrolled projects.

## Why this is now a real result (and what changed)

The original submission's paid run was contaminated (read the committed answer from git).
Per the review decision, it was preserved as an INVALID trial and **one replacement paid run
was authorized** under frozen packet-only conditions. The replacement is non-contaminated:
field-name and test-name overlap with the committed answer are both **zero**, and its
structure **diverges** from the committed answer (it retires `invalid_configs`/`total_errors`
that the answer keeps). Its numbers agree with the answer only because they are derivable
from the pre-fix registry — which is the task.

The local arm was also rerun under the registered Drivr adapter + ContainerEnvironment (run
1 had run on the host). Both run-2 arms are valid and comparable.

## What this does NOT establish

- **It does NOT establish that the paid tier is generally better than the local tier.** This
  is **one task, n=1 per arm**. A single data point cannot carry a general claim, and it is
  offered as evidence, not as a decision.
- **It does NOT establish that the local tier is unsuitable for code-shaped work.** Local run
  2 got the concept right (separate the totals) and only the fleet number wrong. Local run 1
  got both headline numbers right. A poor or partial single result is evidence, not a verdict.
- **It does NOT move any routing policy.** `model-routing-policy.md` is unmodified. Row P4,
  P6, P7 untouched. The "do not write the therefore" is honoured.
- **It does NOT close G11** (Constraint 8). This ran real agentic work through a real adapter
  but was not an `epic_qa` run.
- **It does NOT re-run B3.1's engine comparison.** This is a tier comparison on one task.
- **It does NOT decide row P4.** That is a further HQ call using all four axes together.

## The honest sentence

**The CFO's split-posture question now has a first, valid, controlled data point: on this
one code-shaped task, the paid arm's output was correct and complete, and the local arm's was
partial and wrong on the key number.** Both arms ran validly and comparably. The sample is
one. Let the CFO and M39 write the "therefore" on a larger body of evidence.
