---
type: milestone-closure-declaration
milestone: M45
status: complete
completion_date: 2026-09-04
declared_by: "Milestone Chat (P12-M45 — Trustworthy Completion Signal)"
issued_to: "Phase Chat (P12 — Completion: Fail-Closed Defaults and the Drivr MVP)"
is_final: false
---

# MILESTONE CLOSURE DECLARATION — M45

Milestone **P12-M45 — Trustworthy Completion Signal** is declared **COMPLETE (awaiting
consolidation)**.

**Four epics were planned (one set at a time, Phase-Chair-accepted between sets), delivered, re-measured
by this Milestone Chat at Stage-2 (G2), and merged with explicit human merge authorization for each:**
**E45.1** (#263), **E45.2** (#264), **E45.3** (#265), **E45.4** (#266). **All four stand at attempt 1
of 3** — the rework limit was never touched.

---

## ⚠ THE ONE SENTENCE THIS MILESTONE SHOULD BE READ BY

> **The thing Drivr will use to decide whether agentic work finished is, for the first time, able to
> say "I don't know" — and say it honestly, end to end: `undetermined` is produced by the judgment,
> carried by the consumer contract without being folded, guarded against folding, and named in a
> written contract so M46 builds the board against a supported verdict instead of inventing one.**

---

## The recursion, discharged — read this before the DoD

**M45's subject is the instrument that judges whether agentic work completed, and its first customer is
the milestone's own governance.** The execution was `manual` by construction — dispatching the
judgment-under-repair to build the judgment-itself would have had it reporting on its own repair (the
same circularity M41 refuses for the model line-up and M42 for the execution tier). Three of the four
epics landed code in **Drivr** (`~/soft-dev/drivr`), a separate repository this project's suite does not
cover; each Delivery Notice therefore states the Drivr repository and ref separately, and this Milestone
Chat re-measured the load-bearing code claims at Stage-2 rather than accepting the notices on report.

**The `P11-GH-1` channel stayed quiet** — the M45 milestone spec moved **zero times mid-flight**, and
the backstop (`git log HEAD..origin/milestone/M45`) was run before each delivery and found no amendment.
One cross-epic sequencing constraint was honoured by construction: **E45.4 ran last**, fenced off from
`completion.py` (E45.2's surface) and `outcome.py` (E45.4's), so it reconciled the consumer contract
against a post-E45.2 signal that had stopped moving.

**Per E43.1, the milestone merge `milestone/M45 → phase/P12` is performed by the Phase Chat, not by this
Milestone Chat.** This declaration does not merge itself. See §Required Action.

---

## Completion Verification — the Definition of Done, item by item

| # | DoD item | Disposition |
|---|---|---|
| 1 | All four epics delivered, accepted, and merged to `milestone/M45` | **MET.** E45.1 `03e71c5`, E45.2 `0064603`, E45.3 `9f9e76b`, E45.4 `acbc728` |
| 2 | **A read-only run is no longer reported as `DID_NOT_COMPLETE`** | **MET** (E45.2 + E45.4). `_decide` reads `Role.INSPECTION`; an inspection-only ledger reads `Completion.INSPECTED_NO_EFFECTS` → `Reading.UNDETERMINED`. Verified at Drivr `17aef91` (suite 470) and held through E45.4's re-key (`e9956f2`, suite 471). |
| 3 | The correct verdict for an effects-absent run is **decided and recorded**, with the layer named | **MET** (E45.2 D1). Decision **C3** — a new `Completion.INSPECTED_NO_EFFECTS` (a `Completion`-layer change, projecting to `Reading.UNDETERMINED`). C1 (reuse `INDETERMINATE`) rejected for folding a well-evidenced state into "too thin to judge"; C2 (positive for read-only tasks) **out of scope**, reported not smuggled (BC5). |
| 4 | `_decide` reads inspection evidence and **still reads nothing beyond the ledger** | **MET** (E45.2 D5). `test_judgment_independence.py` unchanged — parameter list still exactly `["ledger", "files_changed"]`; inspection is read *within* the ledger. Exit codes refused in advance, and confirmed refused. |
| 5 | **`P10-GH-7` is closed or re-rated on measured evidence**, both directions addressed, the missing-delivery case defined | **MET** (E45.3). **Re-rated, not closed.** Direction A (blocked-as-running) confirmed as structural absence; Direction B (running-as-blocked) confirmed but re-scoped (exit code already refused). Missing-delivery branch defined: absence → `undetermined`, never "still working"/"blocked". Gap record amended in `chat-hierarchy.md` (changelog `1.7.0`); severity High, owner unassigned, unchanged. |
| 6 | **`undetermined` survives end to end** and no consumer folds it | **MET** (E45.4). Full path traced (judgment → scheduler → journal → gate queue → board); the two-`Disposition` collision resolved by rename (scheduler type → `Conclusion`); a no-fold guard falsified; `undetermined` never folded into `in progress`, `blocked`, `DONE`, or `NOT_DONE`. |
| 7 | **The bar was the first commit on E45.1's branch**, and the judgment beats the degenerate baseline | **MET** (E45.1). Bar is commit `da0c66a`, the first commit on `epic/P12-M45-E45.1`, shown by `git log`. Signal 2/3 beats degenerate baseline 1/3; **post-fix 3/3**. |
| 8 | The `undetermined` rate after the work is **published** | **MET** (E45.4 D4). Post-fix rate **1/3** on E45.1's declared set, published — not improved by redefinition (renaming `undetermined` is expressly prohibited). |
| 9 | Every change names its layer and its repository; Drivr-side verification stated separately | **MET.** Each Delivery Notice's `P11-GH-2` table names layer (`Completion`/`Reading`/`Conclusion`), repository (Drivr vs `ai-project-system`), ref (`f15e239`, `17aef91`, `e9956f2`), date. |
| 10 | Milestone Closure Declaration committed, `is_final: false` | **This document** |

---

## Acceptance Criteria (Milestone) — verified

- [x] **The signal can say "I don't know" and does so when the evidence is absent — and a reader can
      tell that from a run record, not from this spec.** E45.1's live run showed the defect; E45.2's
      `test_e45_1_read_only_case_reads_undetermined` and the inverted pin test assert the fix; E45.4's
      no-fold guard asserts the consumer. Each is a run record, not prose.
- [x] **It beats "always answer completed."** E45.1 measured 2/3 over the degenerate baseline's 1/3;
      post-fix the signal scores 3/3 against a baseline that stays constant. A signal that loses to a
      constant carries no information; this one now carries the read-only class correctly.
- [x] **M46 has a written contract** and does not have to infer the signal's shape. E45.4 wrote
      `docs/m46-completion-signal-contract.md`: layers named, the no-fold rule stated, the board
      vocabulary (`queued`/`in progress`/`undetermined`) fixed, change = a spec amendment.
- [x] **No fix trusted a replay where a live run was required (Y4).** E45.1's discovery was a live run
      (`f15e239`); E45.2/E45.4 moved the measured case (constructed record, falsified guard) and did
      **not** claim live discovery; E45.3 named both directions' methods honestly (code-read/constructed
      for the structural absence; cited for the live exit-code evidence) — no replay presented as
      discovery.
- [x] **Every claim states layer, repository, ref and date.** Carried through all four epics and
      re-measured at Stage-2.

---

## Findings — recorded honestly, not folded into the tick

**1. The Drivr code is local-only — no remote, no second copy.** E45.2 (`17aef91` on
`epic/P12-M45-E45.2`) and E45.4 (`e9956f2` on `epic/P12-M45-E45.4`) landed Drivr code that exists on
this disk and nowhere else; Drivr has no `origin`, so no push was possible. `ai-project-system` records
cite the refs; no other machine can fetch them. This is the set-1 lesson ("nothing lives on one disk")
in a new shape, flagged by the E45.2 Epic Chat, confirmed by this Milestone Chat, and filed separately
as `P12__carry-forward-note__drivr-no-remote-recoverability.md`. **The Phase Chat owns the
publication-model decision (own remote / intentionally-local / vendored); the CFO has ruled "Drivr code
local-only for now."**

**2. The two-`Disposition` collision was Y3's warning made concrete.** Drivr genuinely had two enums
named `Disposition` (judgment's *how an input figured* vs scheduler's *what the scheduler concludes*),
confirmed live at `f15e239`. E45.4 resolved it by rename (→ `Conclusion`), not annotation — a consumer
reasoning by name can no longer fold one into the other. This is the exact fold the CFO's ruling and Y3
both warned about, found in the code rather than hypothetical.

**3. The milestone spec's `f60164c` pin was stale; every epic re-measured (G2) and none reported a
pinned-but-unread ref.** Drivr moved `f60164c` → `f15e239` → `17aef91` (E45.2) → `e9956f2` (E45.4); the
judgment modules were `git diff`-verified unchanged across the first jump, and each epic stated the ref
it actually measured against.

**4. The `ai-project-system` baseline is environment-dependent, and was corrected mid-planning.** The
Phase Chat's `767` was pinned into four M45 artifacts before being discovered unreliable (the
live-ComfyUI integration test runs or skips or fails by machine); all four were retro-corrected to state
`766+1 skipped / 767 / 766+1 failed` as the same suite. Final suite re-measured at Stage-2: **767
passed** on this box (one of the three accepted states).

**5. M46 is gated, and the gate was honoured by construction.** E45.4 ran last precisely so M46's
contract reconciles a settled signal; the M46 contract is the thing M46 builds its board against, and
building the board first would have produced a window confidently displaying a verdict the pre-E45.2
signal could not support. That is why M45 gates M46, and it held.

---

## Milestone Summary — what M45 actually produced

**The completion signal now can tell the truth, and M46 can trust the shape of what it will receive.**

1. **The bar came first.** E45.1 committed, as the first commit on its branch, a stated bar with four
   pass conditions — honest read-only, can-say-no, can-say-yes, **beat the degenerate baseline** — and
   measured the signal against it: 2/3, beating the baseline but wrong about the read-only class.
2. **The judgment was made honest.** E45.2 taught `_decide` to read `Role.INSPECTION` (the gap
   `projections.py:45` had documented against itself), so a read-only run reads `undetermined` instead
   of `DID_NOT_COMPLETE` — with the decision (C3) and its rejected alternatives recorded.
3. **`P10-GH-7` got its first measurement-and-adjudication since M35.** E45.3 re-rated it on evidence
   (structurally absent, not merely untrustworthy), defined the missing-Delivery-Notice branch as
   `undetermined`, and stated the detector's required signal for M46/later.
4. **`undetermined` survives end to end.** E45.4 inherited E45.3's D4, re-keyed the consumer contract,
   resolved the two-`Disposition` collision, landed a falsified no-fold guard, and wrote the M46
   contract.

**Net:** the window that opens where the attention belongs now has, beneath it, a signal that says
"I don't know" honestly instead of "it failed" wrongly — and M46 has the written contract that makes it
safe to build that window.

---

## Required Action: Consolidation

**To fully close this milestone, consolidation is required — and per E43.1 it is the Phase Chat's act,
not this Milestone Chat's:**

1. **The Phase Chat reviews this declaration** and the four merged epic branches.
2. **The Phase Chat creates and merges** `milestone/M45 → phase/P12` (the consolidation commit).
3. **The Phase Chat flips the milestone spec's `status` from `planned` to `completed`** in the same act
   (the M42–M44 precedent — `planned` through the planning merge, `completed` only at closure).
4. **The Phase Chat reports the merge commit SHA** back to this Milestone Chat.

**`milestone/M46` depends on this milestone** — M45 gates M46 by construction, and M46 must not be
planned ahead of the contract M45 just handed over. The Drivr publication decision (the CFO's
"local-only for now") is the Phase Chat's to hold, with the carry-forward note as its record.
