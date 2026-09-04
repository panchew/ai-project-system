---
type: milestone-closure-declaration
milestone: M46
status: complete
completion_date: 2026-09-04
declared_by: "Milestone Chat (P12-M46 — The Drivr MVP Surface)"
issued_to: "Phase Chat (P12 — Completion: Fail-Closed Defaults and the Drivr MVP)"
is_final: false
---

# MILESTONE CLOSURE DECLARATION — M46

Milestone **P12-M46 — The Drivr MVP Surface** is declared **COMPLETE (awaiting consolidation)**.

**Five epics were planned (one set at a time, Phase-Chat-accepted between sets), delivered, re-measured
by this Milestone Chat at Stage-2 (G2), and merged with explicit human merge authorization for each:**
**E46.1** (#268), **E46.2** (#269), **E46.3** (#270), **E46.4** (#271), **E46.5** (#272). **All five
stand at attempt 1 of 3** — the rework limit was never touched.

---

## ⚠ THE ONE SENTENCE THIS MILESTONE SHOULD BE READ BY

> **A surface that *validates* a governance rule can be argued with; a surface that cannot
> *represent* the rule's violation has nothing to argue about — and M46 moved at least three rules
> from the first category to the second, on a board whose central verdict is now allowed to say
> "I don't know."**

---

## The recursion, discharged — read this before the DoD

**M46's subject is the surface that governs agentic dispatch, and its own execution is `manual` by
construction** — building the surface agentically would have the mechanism under repair reporting on
its own repair (the same circularity M41, M42 and M45 all refuse). All five epics landed code in
**Drivr** (`~/soft-dev/drivr`), a separate repository this project's suite does not cover; each
Delivery Notice states the Drivr repository and ref separately, and this Milestone Chat re-measured
the Drivr suite and read the load-bearing code at Stage-2 rather than accepting the notices on
report.

**Two cross-epic sequencing constraints were honoured by construction.** E46.1 ran first — its
registry is the prerequisite for E46.4's go-to-blocker, not a convenience — and E46.5 committed its
bar as the **first commit on its branch** (`95f7656`), the E45.1 worked precedent. E46.2, E46.3 and
E46.4 are parallel-safe and delivered in sequence against a moving Drivr `main`; each Delivery Notice
re-measured its governing artifacts at its own branch point (G2), which is what made the planning
spec's `4872107` pin stale-safe.

**Per E43.1, the milestone merge `milestone/M46 → phase/P12` is performed by the Phase Chat, not by
this Milestone Chat.** This declaration does not merge itself. See §Required Action.

---

## Completion Verification — the Definition of Done, item by item

| # | DoD item | Disposition |
|---|---|---|
| 1 | All five epics delivered, accepted, and merged to `milestone/M46` | **MET.** E46.1 PR #268 (`102100a`), E46.2 PR #269 (`fa41751`), E46.3 PR #270 (`6abbc94`), E46.4 PR #271 (`9c0691f`), E46.5 PR #272 (`dd13465`) |
| 2 | **A role maps to one session, and a second claimant is caught at claim time** (E46.1) | **MET.** `drivr/registry` — atomic `O_EXCL` claim, cross-process, agreeing-fork refused (`test_a_correct_converging_second_claimant_is_still_refused`), three-valued lookup with `undetermined` never `vacant`. Drivr `main` `4410eda`. |
| 3 | **`undetermined` is rendered as itself**, with a render-side no-fold guard (E46.2) | **MET.** `drivr/board` — pure `board_state(position, conclusion)`; `FINISHED + UNDETERMINED` → `undetermined` and nothing else; render-side guard mirroring E45.4's consumer guard, falsified both directions. Drivr `main` `107457a`. |
| 4 | **Three governance rules are unrepresentable**, each with a constructibility test (E46.3) | **MET.** `drivr/capabilities` — closed domain (`creation`/`hq` → ∅; `phase`/`milestone` → `{run_agentic}`; `epic` → `{run_agentic, dispatch}`), `ast`-scan for rule 3, three tests falsified both directions. Drivr `main` `99392ed`. |
| 5 | **Approval is carried by signed one-time link; escalation is one level** (E46.4) | **MET.** `drivr/controls` — approval wires `Surface.redeem` (one mint site); `parent(level)` one-arg, no skip/broadcast/jump, terminus stated; go-to-blocker refuses to guess on `vacant`/`undetermined`. Drivr `main` `4767cf3`. |
| 6 | **The qualification bar was committed before the suite**, and both historical failures are detected (E46.5) | **MET.** Bar is first commit (`95f7656`, before `f33af95`); E39.3 (counts) and the `llama3.1:8b` overpack (context) both detected, named and cited; no-swap refusal falsified both directions. Drivr `main` `114de1c`. |
| 7 | **Every Drivr deliverable is on Drivr `main`**, not only on an epic branch (BC9) | **MET.** All five merged to Drivr `main` (final `114de1c`); each epic's Delivery Notice flagged BC9 as an open item and this Milestone Chat completed it by the local merge. |
| 8 | Every claim states the layer, repository, ref and date (`P11-GH-2`) | **MET.** Each Delivery Notice carries a `P11-GH-2` table naming layer, repo, ref, date; re-measured at Stage-2. |
| 9 | No deliverable states a coverage count where a list belongs | **MET.** Roles, capabilities, board tokens, controls, and the escalation chain are all itemized; the two historical failures are named, not counted. |
| 10 | Suites green, each named with its repository and invocation | **MET.** Drivr **581 passed / 0 failed / 0 skipped** at `main` `114de1c` (`python3 -m pytest -q`, re-measured at Stage-2). `ai-project-system` is **environment-dependent** (`766+1 skipped` / `767 passed` / `766 passed + 1 failed` are the same suite; the variance is the live-ComfyUI integration test). |
| 11 | Milestone Closure Declaration committed, `is_final: false` | **This document** |

## Acceptance Criteria (Milestone) — verified

- [x] **The surface cannot express a governance violation** for the three named rules — a reader can
      say why the state is unconstructible, not merely rejected. `drivr/capabilities` closes the
      domain over `{run_agentic, dispatch}`; `construct(creation, run_agentic)` raises the same way an
      enum raises for a member it does not define, and `test_no_mode_control_implies_merge_authority`
      (`ast`-scan) asserts no scope in `drivr/` couples `ExecutionMode` with authority.
- [x] **The board tells the truth about not knowing** — `undetermined` is visible, distinct, and never
      rendered as a neighbour. `BoardState.UNDETERMINED` is the render of `Conclusion.UNDETERMINED` and
      nothing else, itemized (not counted), with the no-fold guard falsified in both directions.
- [x] **A role has one holder, and the mechanism works against an agreeing fork.** The atomic `O_EXCL`
      claim refuses a correct, converging second claimant at claim time, outside the state the forks
      write (V2b), with no form resting on implicit `HEAD` (V2c).
- [x] **The qualification bar was set before it graded anything**, and detects successful nothing on
      both recorded cases. Bar is the first commit; E39.3 (zero rounds, `framework_version` claim) and
      the `llama3.1:8b` 4× overpack are both detected, by different mechanisms (E41.2 S4), and
      `COULD_NOT_MEASURE` is distinct from `FAIL`.
- [x] **Nothing this milestone declares complete lives only on an epic branch.** All five Drivr
      deliverables are on Drivr `main` (`114de1c`); no DoD item was ticked against an epic branch
      (the M43/M45 defect, which did not recur).

---

## Findings — recorded honestly, not folded into the tick

**1. The Drivr code remains local-only — no remote, no second copy.** Every epic's Delivery Notice
flagged that Drivr has no configured `origin`, so each Drivr commit exists on this disk and nowhere
else; each merge to `main` was a **local** merge, and no GitHub PR for any Drivr change exists. This is
the M45 carry-forward note (`P12__carry-forward-note__drivr-no-remote-recoverability.md`) recurring on
all five epics, not a new discovery. **The Phase Chat owns the publication-model decision; the CFO has
ruled "Drivr code local-only for now."**

**2. The `ListAgents` self-address token form moved again, and the re-measure caught it.** E46.1's
Delivery Notice re-measured at build time (Hard Constraint 4) and found the harness reports `ses_<id>`,
not the `ai-project-system-<hex>` form V1 recorded on 2026-08-27 — the *capability* survived, the
*token form* moved. The registry is agnostic to the form, so the design did not depend on it; but any
future artifact citing the `ai-project-system-<hex>` literal is now stale. This is V1's lesson firing
correctly — re-measure at the moment of use — and it is recorded rather than left in the delivery.

**3. The milestone spec's `4872107` pin was stale from the first epic on; every epic re-measured (G2)
and none reported a pinned-but-unread ref.** Drivr `main` moved `4872107` → `4410eda` (E46.1) →
`107457a` (E46.2) → `99392ed` (E46.3) → `4767cf3` (E46.4) → `114de1c` (E46.5). Each Delivery Notice
branched from the then-current `main` and re-measured its governing artifacts at its own branch point;
the planning spec's single pin was correct at its date and was not trusted past it.

**4. The "both historical failures" naming was reconciled by the milestone spec, not by the phase
spec.** Milestone V5 names E39.3 + the `llama3.1:8b` overpack; phase P12.6 names E33.2 Run A + E39.3.
This Milestone Chat flagged the discrepancy to the Phase Chat at planning close (E33.2 Run A is a third
successful-nothing case already in E41.2's instrument replay set). E46.5 built against V5's pair
(authoritative for M46) and additionally flags E33.2 Run A's shape through the same counts mechanism.
The two authoritative statements still do not reconcile; this is a Phase-Chat item, recorded here
rather than folded.

**5. The `ai-project-system` baseline is environment-dependent.** All five delivery notices and this
declaration state the Drivr suite (581) as the operative baseline and the `ai-project-system` suite as
`766+1 skipped / 767 / 766+1 failed` — the same suite, the live-ComfyUI integration test being the
variable.

---

## Milestone Summary — what M46 actually produced

**The Drivr MVP surface exists, and it is built so the three rules cannot be clicked away.**

1. **The registry came first (E46.1).** A Drivr-owned role → session-address mapping with an atomic
   `O_EXCL` claim and a three-valued lookup — the prerequisite for auto-open and go-to-blocker, and the
   answer to *"which session holds a role, and that exactly one does."*
2. **The board renders the truth (E46.2).** A pure board-state function and a render-side no-fold
   guard: `undetermined` is first-class on the board, itemized, and never a neighbour.
3. **Three rules became unrepresentable (E46.3).** A closed level-capability model with no way to
   express agentic at Creation/HQ, dispatch at Phase/Milestone, or mode→merge-authority — absence as
   the deliverable, each with a constructibility test.
4. **The present controls were built (E46.4).** Approval carried only by the signed one-time link,
   escalation one level up the SN-25 chain, and go-to-blocker resolving through the registry rather
   than guessing.
5. **SN-37's gate was formalized (E46.5).** The bar committed first, the three-valued result, the
   enforced no-swap refusal, and both historical failures detected.

**Net:** the surface that opens where attention belongs is now backed by a registry that knows who
holds a role, a board that tells the truth about not knowing, three rules that cannot be expressed,
controls that carry authorization by link and escalate by one level, and a gate that blocks a model
swap the evidence cannot support.

---

## Required Action: Consolidation

**To fully close this milestone, consolidation is required — and per E43.1 it is the Phase Chat's act,
not this Milestone Chat's:**

1. **The Phase Chat reviews this declaration** and the five merged epic branches.
2. **The Phase Chat creates and merges** `milestone/M46 → phase/P12` (the consolidation commit).
3. **The Phase Chat flips the milestone spec's `status` from `planned` to `completed`** in the same act
   (the M42–M45 precedent — `planned` through the planning merge, `completed` only at closure).
4. **The Phase Chat reports the merge commit SHA** back to this Milestone Chat.

**Open items the Phase Chat holds, not this Milestone Chat:** the Drivr publication-model decision
(CFO: "local-only for now"); the milestone-V5 vs phase-P12.6 "both historical failures" reconciliation
(Finding 4); and — unchanged from M45 — the escalation-terminus disposition and `model_verification`'s
flip to `blocking`, both of which come due at M47's completion, not here.
