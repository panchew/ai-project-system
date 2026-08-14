---
project: ai-project-system
phase: P11
milestone: M38
epic: E38.6
type: reference
status: complete
last_updated: 2026-08-14
---

# Judgment (re-review 01) — Local/Paid Controlled Comparison (E38.6)

## Verdict

**On the one task, on this material, the paid arm (claude-opus-5) produced a CATCH and the
local arm (qwen3-coder:30b) produced a MISS.** Both runs are valid, protocol-conforming,
comparable, and independently re-measured.

## The valid result

| | Local run 2 | Paid run 3 |
|---|---|---|
| Fleet warning total | **10 (wrong; correct is 12)** | **12 (correct)** |
| Raw total | 14 | 14 |
| Excluded contribution | not correctly attributed | 2 (correct) |
| Structural invariant test | absent | present (`raw == fleet + excluded`) |
| Isolation | container (Drivr adapter) | packet-only, no fs/shell/search tools |
| Verdict | **MISS** | **CATCH** |

The paid arm derived the fleet total two independent ways (sum of per-project warnings; sum
of the schema-drift occurrence counts), attributed the 2-warning gap to the two worktree
checkouts of `ai-project-system`, and added **7** tests guarding the split (re-review 02,
Finding 3: seven, not eight — historical commit messages are preserved unedited). Its
proposed changes, applied verbatim, pass the full test file (23/23 = 16 original + 7 new)
against the pre-fix registry.
The local arm separated the totals but computed the fleet total **wrong** (10 instead of 12)
and mis-attributed the gap to the unenrolled projects.

## Why this is now a compliant result

The review's first re-review rejected paid run 2 (programmatic subagent, instructed-not-
sandboxed isolation). Per the second protocol-correction addendum (committed before run 3),
**paid run 3** was run as a **genuinely fresh, human-operated manual session** via Claude
Code CLI: model `claude-opus-5`, in an empty non-repo directory, with **all
filesystem/shell/search tools disallowed**, receiving **only the sealed packet**. The run
record confirms zero tool_use events and no file-access capability. This closes Finding 1.

The timestamp erratum and commit-order corrections required by Finding 2 are recorded in the
Delivery Notice.

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

**The CFO's split-posture question now has a compliant, valid, controlled data point: on
this one code-shaped task, the paid arm's output was correct and complete, and the local
arm's was partial and wrong on the key number.** Both arms ran validly and comparably, and
the paid arm's protocol compliance is now verified. The sample is one. Let the CFO and M39
write the "therefore" on a larger body of evidence.
