---
project: ai-project-system
phase: P11
milestone: M38
epic: E38.6
type: reference
status: complete
last_updated: 2026-08-12
---

# Judgment — Local/Paid Controlled Comparison (E38.6)

## Verdict

**No tier comparison was produced. The comparison failed on its blinding, and that failure is the finding.**

## Why

The comparison was designed to run the same work two ways on blinded material. It ran the
work two ways, but **only the local arm was blinded**. The paid arm had repository access
and read the committed answer (`927b7fa`) from git — producing a "perfect" result that was
**retrieval, not capability**. The local arm, properly blinded in an isolated git-free
workspace, had to derive the fix and produced a partial result.

**Neither result supports any conclusion about which tier is better at this work.** The
asymmetry (Finding 3, B3.1's confound reproduced one level up) is unstated nowhere in this
record — it is stated plainly in `scores.md`.

## What this comparison demonstrates

1. **The contamination risk the Epic warned about is real, not theoretical.** The spec said:
   *"an arm that reads the answer is not being measured on the work — and it would look like
   an excellent result."* That is precisely what happened. A paid frontier model with
   repository access, given a task whose answer is committed, returns the committed answer
   and looks perfect. **This is the most misleading possible outcome for a routing decision
   — and it is exactly why the blinding discipline exists.**

2. **The blinding worked when enforced.** The local arm, with no git and no answer, derived
   the two headline numbers correctly (12 fleet / 14 raw) and separated the totals. It did
   not complete the task to the pre-registered bar (derived fields incomplete, test weak) —
   but it was genuinely measured on the work.

3. **The method is reusable.** The material, packet, rubric, and run outputs are committed
   and auditable. Someone could run it again with **both** arms blinded — or, more
   honestly, choose material whose answer is **not** in git at all, so the blinding is
   structural rather than environmental.

## What this does NOT establish

- **It does NOT establish that the local tier is better than the paid tier**, or the
  reverse. The two arms ran under non-comparable conditions.
- **It does NOT establish that either tier is unsuitable for code-shaped work.** The local
  arm showed partial ability; the paid arm showed no ability *because it was not measured*.
- **It does NOT move any routing policy.** `model-routing-policy.md` is unmodified. Row P4,
  P6, P7 untouched.
- **It does NOT close G11.** This ran real agentic work through a real adapter but was not
  an `epic_qa` run (Constraint 8).
- **It does NOT recommend re-running B3.1's engine comparison.** This was a tier comparison
  attempt; it failed on blinding, not on engine.

## The honest sentence

**The value of this Epic is in its method, which worked: it caught the contamination it was
designed to catch, before a misleading result could be cited.** The CFO's split-posture
question remains unanswered on this evidence — and recording that honestly is a success
outcome, not a failure. Let someone else write the "therefore."
