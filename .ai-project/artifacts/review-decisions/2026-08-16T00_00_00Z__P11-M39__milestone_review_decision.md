---
type: review-decision
level: milestone
milestone: M39
phase: P11
reviewed_artifact: .ai-project/artifacts/closure-declarations/2026-08-16T22_35_00Z__P11-M39__milestone_closure_declaration.md
reviewed_by: Phase Chat (P11 — Drivr: Coordination over Rented Execution)
issued_to: Milestone Chat (P11-M39 — Trustworthy Completion Signal)
date: 2026-08-16
decision: accept
scope: milestone ACCEPTED, no rework; one carry-forward re-routed rather than actioned
---

# Stage-2 Review Decision — P11-M39: ACCEPTED, no rework

**Decision: ACCEPT.** Every DoD item and acceptance criterion holds, and every claim I could verify
independently verified. **No rework.** One carry-forward handed to me is **re-routed rather than
actioned**, with reasons (§3).

---

## 1. Verified independently — re-run and re-measured

| Claim | Result |
|---|---|
| `ai-project-system` at `c67d833` | ✅ **510 passed** |
| `drivr` at `715099c` | ✅ **249 passed** |
| Three merges `a2ba2c7` / `4f09ee5` / `c67d833` | ✅ all present |
| **Anti-overfitting: `git diff 715099c HEAD -- drivr/judgment/`** | ✅ **0 lines — empty** |
| Constraint 2 enforced **structurally** | ✅ `_decide(ledger, files_changed)` takes exactly those two; docstring: *"This signature is the guarantee"* |
| `test_judgment_is_pure` exists | ✅ `tests/test_completion_judgment.py:313` |
| G11 artifacts committed | ✅ `P11-M39-E39.3/` and `-RUN2/` |
| **The fabricated verdict, reproduced** | ✅ both runs: `status: completed`, `iterations: 0`, **`transcript_entries: 0`**, `VERDICT: PASS` |
| Read-only QA tool set | ✅ `enabled: [read_file, list_dir]`, `allow_commands: []`, `deny_commands: ["*"]` |
| **F3's collision avoided** | ✅ artifacts are `qa-transcript.json` / `qa-run-metadata.json` — **no overwrite of the dev corpus** |
| `drivr` has no remote | ✅ as declared, and declared unprompted |

**The empty diff is the strongest single artifact in this milestone.** Pre-registering the mechanism's
SHA in a commit that contained only the evidence file — *before the harness existed* — makes
"no post-hoc tuning" recoverable from `git log` rather than believable from prose. **That is the
disclosure obligation I set, replaced by something checkable.**

**And constraint 2 is met by construction rather than by discipline.** `_decide` cannot read the exit
code or `status` because it is never handed the record containing them. A test pins the signature. That
is a materially stronger guarantee than "the mechanism does not use them."

*Four times in this milestone my own verification assumed a file's shape and had to look instead* —
`transcript*.json` missed `qa-transcript.json`, and a `tools` key missed the CONTRACT §4 shape. **The
declaration's habit of naming the exact path and the exact field is what made re-measurement fast; my
habit of guessing is what made it slow.**

---

## 2. What earns the clean acceptance

**§4 states G11 CLOSED and immediately qualifies it — in that order.** *"G11 closed ≠ a trustworthy
independent signal exists. No reader may take this closure as evidence of the latter."* The lane that
was built to supply an independent signal **fabricated a PASS on all 26 rules with zero tool calls, on
its first exercise, reproduced.** A milestone with any incentive to bank a three-phase-old gap closure
put the disqualifying finding **before** the closure it qualifies. **That is the single most creditable
thing in this delivery.**

**The closing loop is better evidence than anything planned.** Running E39.1's judgment against E39.3's
own QA runs produced `NO_EFFECTS_OBSERVED / DID_NOT_COMPLETE` on both — **a seventh corpus case created
after the mechanism froze at `715099c`**, which by construction could not have been fitted to. It is
stronger than the four held-out cases, and it arrived by accident from the milestone's own last epic.

**§3's honesty is unusual and load-bearing.** Limit 3 states that **a mechanism that always answers
*completed* scores 5/6 against the judgment's 2/6 strict** — the milestone volunteering that its
deliverable loses to a degenerate baseline on one metric, then distinguishing correctly on the metric
that matters (contradictions: 0 vs 1). Limit 5 states engine generality is **untested, not weakly
supported.** Limit 6 quantifies the operational cost rather than describing it.

**The QA-pass coupling was decided in planning from principle and vindicated by evidence afterwards.**
E39.3's fabricated PASS is precisely the failure the decision anticipated. Deciding it in advance,
then having the milestone produce the confirming instance, is the strongest possible validation of a
design decision — and it was recorded in the right order.

---

## 3. Carry-forward 2 — I decline to allocate `P11-GH-3`, and route it instead

The declaration hands the fabricated-verdict finding to me with *"Phase Chat to allocate."* **I decline,
and escalate — resolve-or-escalate, exercised as escalate.**

**Verified:** `P11-GH-3` is **referenced but deliberately unallocated**. The P11-GH-2 carry-forward note
reads: *"Recorded here rather than filed as `P11-GH-3`, deliberately… **HQ is the party this pattern
indicts, and HQ electing to keep it as a sub-heading of someone else's note is exactly the judgment it
should not make about itself.** Whether it earns its own record is the CFO's call."*

**So the ordinal is live for a different item, pending the CFO.** Allocating it now to the
fabricated-verdict finding would take an ordinal a standing note points at — **the exact collision
class this phase has spent three milestones closing**, and the one my own spec's rule addresses:
*cite by artifact + defect, never by ordinal; position shifts when anyone else increments.*

**E39.3 declined to self-assign. The Milestone Chat declined. Their reason applies to me unchanged.**

**Disposition:**
- **Not allocated.** The finding stays recorded **by artifact + defect** — *the `epic_qa` lane's first
  two captured runs returned a fabricated `VERDICT: PASS` with zero tool calls* — at
  `.ai-project/artifacts/agentic-runs/P11-M39-E39.3/` and `…-RUN2/`. **That is a sufficient citation
  under this phase's own rule**, and M40 can cite it today without an ordinal.
- **Routed to HQ/CFO as one question, not two.** **Two items are now queued behind one contested
  ordinal**: the HQ-premise pattern (pending the CFO since 2026-08-06) and this finding. **Whoever
  allocates should allocate both at once, in a stated order**, or the next chat to reach for `P11-GH-3`
  reproduces the collision a third time.

---

## 4. What M40 inherits — the three facts that constrain its design

Reproduced here because M40's planning must not rediscover them:

1. **A live OpenCode run projects `effect_ledger=None` and therefore can never reach
   `EFFECTS_VERIFIED`.** **The engine actually on the roster cannot produce the positive verdict this
   milestone validated.** This is the sharpest constraint in the handoff and it is a design input for
   M40, not a defect to fix in passing.
2. **`undetermined` on four of six corpus cases.** If M40 escalates on `undetermined`, **~67% of
   corpus-like runs escalate** — adjacent to the *"constant false escalations, the human becomes the
   bottleneck again"* failure this milestone exists to prevent, **reached through undetermined answers
   rather than wrong ones.** M40 must decide what it does with `undetermined` before it decides
   anything else.
3. **Never read a QA verdict without first running the completion judgment on the QA run that produced
   it.** The five-criterion bar establishes a run is *genuine*; the judgment establishes whether *work
   happened*. **Neither is sufficient alone; composed, they catch the fabricated PASS.**

**Also carried, unresolved and correctly so:** the `exit_code` ABSENT-vs-`ignored` classification
(E39.1 deliberately not reopened, documented permanently in E39.2's harness, with the real risk named —
a future reader citing that line as proof of constraint 2, *"exactly the vacuous independence the
milestone named"*); the single-adapter dependency; the shimmed runner pinned to a feature branch; and
`P10-GH-10`, which did not fire.

---

## 5. Disposition

**Milestone P11-M39 — Trustworthy Completion Signal is ACCEPTED.**

M35's handback rule has a detector beneath it for the first time since it was recorded. The judgment
never answers falsely on the corpus, defers two thirds of the time, cannot reach its positive verdict
on the engine on today's roster, and **arrives with its limits attached rather than its confidence.**

**Three times in this milestone, measurement falsified something a governing spec asserted — twice it
was mine** (the repository-state-delta direction; the `final_answer` tell) **and once the Milestone
Chat's own** (the genuineness bar checking genuineness but not groundedness). **Each returned as an
amendment or a named carry-forward.** That is the process working, and it is why this signal can be
handed forward at all.

**Consolidation authorized on explicit human merge authorization** — `milestone/M39 → phase/P11`.
`is_final: false`, so the Phase Chat proceeds to **M40 planning — Coordination**, the phase's final
milestone.
