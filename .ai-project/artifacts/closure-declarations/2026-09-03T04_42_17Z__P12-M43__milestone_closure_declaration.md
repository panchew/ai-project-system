---
type: milestone-closure-declaration
milestone: M43
status: complete
completion_date: 2026-09-02
declared_by: "Milestone Chat (P12-M43 — The Acceptance Chain, Made Structural)"
issued_to: "Phase Chat (P12 — Completion: Fail-Closed Defaults and the Drivr MVP)"
is_final: false
---

# MILESTONE CLOSURE DECLARATION — M43

Milestone **P12-M43 — The Acceptance Chain, Made Structural** is declared **COMPLETE (awaiting
consolidation)**.

**Four epics were delivered, re-measured by this Milestone Chat at Stage-2 (G2), and merged with
explicit human merge authorization for each:** **E43.1** (#250), **E43.2** (#251), **E43.3** (#252),
**E43.4** (#253). No rework attempt was consumed on any epic; each stands at attempt 1 of 3.

---

## ⚠ THE ONE SENTENCE THIS MILESTONE SHOULD BE READ BY

> **Every rule in this framework was enforced by an agent reading prose and choosing to comply —
> and M43 replaced that with structure, for *authority* rather than for `bin/`: the parent merges, so
> a child never holds the authorization; acceptance carries a named, attributable signal, so absence
> stops reading as approval; the rework limit exists once, so it cannot be absent from the surface
> that must enforce it; and exhausted rework flips the parent to manual — the system's first
> fail-closed default — performed and recorded by Drivr so the committed starter stays the source of
> truth.**

---

## The recursion, discharged — read this before the DoD

**M43 is the milestone whose subject is the acceptance chain, and its own epics are the boundary
case.** The boxed warning in this milestone's starter held throughout Stage-2: a rule you are
rewriting still binds you while you rewrite it. **Each of M43's four epics was therefore accepted
under the *pre-M43* rules** — E43.1 (the parent-merges rule) did not govern E43.1's own merge; E43.2
(the named-acknowledgment rule) did not govern E43.2's own acceptance. The merge of M43's own epics
was carried by **Layer-8 (the CFO's) explicit authorization** on each of the four, which sits outside
the child/parent merge rule entirely.

**The consequence is that this milestone's consolidation is the first act ever performed under
E43.1's new rule.** E43.1 landed *"the parent performs the merge of a child's branch"* — so the
milestone merge `milestone/M43 → phase/P12` is performed by the **Phase Chat**, not by this Milestone
Chat. This declaration does not merge itself. See §Required Action.

---

## Completion Verification — the Definition of Done, item by item

| # | DoD item | Disposition |
|---|---|---|
| 1 | All four epics delivered, accepted, and merged to `milestone/M43` | **MET.** E43.1 `9b00fd4`, E43.2 `2679c15`, E43.3 `0ef69be`, E43.4 `bd9cda3` |
| 2 | A child never holds merge authorization; `merge-authorization.md` is the parent's record; E40.5's guard survives as a labelled backstop | **MET** (E43.1). PSG §11.6 "The Model" states the parent merges at the Phase→Milestone and Milestone→Epic gates; the template is re-authored (subject, fields, post-conditions all move to the parent); the eight starter surfaces carry the guard **relabelled a backstop**, not deleted |
| 3 | A clean delivery still costs no artifact, and acceptance is distinguishable from absence | **MET** (E43.2). The signal rides the §11.6 acknowledgment that already exists — a named, attributable in-chat act (role + session identity), no new object; *"silence accepts nothing"*; the boundary "review-happened ≠ review-correct" is stated |
| 4 | One statement governs the rework limit and its extension semantics, reached by every surface in an **itemized** list, including all three templates | **MET** (E43.3). The single statement lives in PSG §11.6 "The Rework Limit"; the two extension semantics ("resets" vs. `+1`) are reconciled to one (`+1`, SN-36/37); ten surfaces itemized, two **carry** (the Milestone surfaces), eight **cite**, the three templates in the set. `P12-GH-1` closed |
| 5 | The flip exists, defaults on, is blessed in the yml spec, and produces no validator warning | **MET** (E43.4). `rework_exhaustion_flip: enabled` in `.ai-project.yml`; §3.8 + §4 rule 28 in `ai-project-yml-spec.md`; **and** `cfo_review_gate` blessed in the same change (§3.7 + §4 rule 27). `bin/ai-project-validate` reports **no warning** for either key — re-run, not taken on report |
| 6 | Resume is specified normatively: restores, never promotes; returns the mode, not the budget | **MET** (E43.4). Resume's normative home is `chat-hierarchy.md` "Resume" — it restores the declared mode and never promotes manual → agentic; it returns the mode, not the budget (no counter reset, by construction: the record schema has no counter field) |
| 7 | The committed-starter invariant is intact | **MET** (E43.4). Drivr performs and records the flip **rather than rewriting the committed starter**; a reader determines declared mode from the committed file and the effective mode from the recorded transition |
| 8 | Every new check has been shown to fail when its change is reverted | **MET.** Falsification demonstrated per epic: E43.1 (revert re-authoring → 2 fail; remove backstop relabel → 1 fail), E43.2 (three ways: silent-accept → 2, attendance → 1, attribution → 1), E43.3 (remove a cite → 2, restore "resets" → 2), E43.4 (remove §4 enforcement → warning returns) |
| 9 | No deliverable states a coverage count in place of a list | **MET.** W2 discharged in all four epics — surface sets are itemized lists with per-surface state (E43.1: 18 surfaces; E43.2: 17; E43.3: 10; E43.4: the yml fields); no coverage claim rests on a bare number |
| 10 | Suite green at **549** plus this milestone's additions; the Drivr half's verification stated separately | **MET, with the baseline drift noted.** `549` was the `d98f95d` phase baseline; **M42 landed before M43's epics ran**, so the operative baseline was **582** (E43.1's own measurement at `cf32fc6`). Final: **740 passed / 0 failed** (`PYTHONPATH=. pytest -q`, no skips). **Drivr half stated separately:** `tests/test_modes_flip_resume.py` in Drivr — **469 passed** there, *not* covered by this repo's suite |
| 11 | Milestone Closure Declaration committed, `is_final: false` | **This document** |

---

## Acceptance Criteria (Milestone) — verified

- [x] **The bypass class `P9-GH-1`/`P10-GH-9` describe is structurally unavailable, not merely
      discouraged.** A reader can say why a child *cannot* hold the authorization — the parent merges
      (E43.1), and a child never receives a merge instruction.
- [x] **Every rule this milestone touches exists once, and a reader can find the one place.** The
      parent-merges statement, the rework limit, the flip, and resume each have a single normative
      home; the surfaces reach them by carry or cite rather than restating.
- [x] **No number in a deliverable stands where a list belongs.** The historical "seven/eight/nine"
      surface-set discrepancy is discharged by itemization, not by a cleaner count.
- [x] **The first fail-closed default is itself validated.** `rework_exhaustion_flip` is blessed
      (§3.8/§4-r28) — it is not an unblessed key, and `cfo_review_gate`, the precedent it copied, is
      blessed alongside it (§3.7/§4-r27).
- [x] **Every claim states the layer, time and scope it was verified at, and the two-repository
      boundary is explicit.** Each record carries its `P11-GH-2` block with a pinned ref, and E43.4
      names its repository per deliverable (this repo vs. Drivr).

---

## Carry-forwards — recorded honestly, not folded into the tick

**A — the `model_verification` key is a fresh W1-pattern unblessed key (out of M43's scope).**
`bin/ai-project-validate .ai-project.yml` still reports **one** warning, for `model_verification`
(line 93) — the SN-40 advisory/blocking toggle. It is a *top-level* unblessed key, exactly the class
E43.4 just closed for the two gate keys. **Not M43's scope** (it belongs to the model-lineup/SN-40
track, M41/M47-adjacent), but it is the same schema-drift defect wearing a new key, and it should be
blessed wherever that track is consolidated — otherwise *"it only warns"* becomes the next W1. Raised
at E43.4 acceptance; carried here so it is not orphaned.

**B — the suite baseline the DoD named is stale, and that is not a defect to hide.** The DoD's `549`
predates M42; the real baseline when M43 ran was `582`. The milestone's closure therefore shows
`582 → 740` rather than `549 → 740`. Recorded because a closure that says "green at 549" without the
drift would be the exact derived-claim rot `P12-GH-3` names.

**C — the milestone's own rules are now operative on `milestone/M43`, but not yet on `phase/P12`.**
This is the honest state at Stage-2 completion: M43's changes govern the milestone branch's own
artifacts, but do not bind the phase (or anything downstream) until the consolidation merges. The
recursion (below) is why this is a feature, not an unfinished half.

---

## Milestone Summary — what M43 actually produced

**Four structural changes to how acceptance is authorised, and recorded, in this framework.**

1. **A child never holds merge authorization.** The parent performs the merge (E43.1), so the bypass
   class is unavailable rather than discouraged; E40.5's guard survives as a labelled backstop.
2. **Acceptance is a named, attributable signal, and still costs nothing.** A clean delivery produces
   no artifact — the acknowledgment (role + session identity) rides the existing §11.6 acceptance
   record, so *reviewed-and-clean* is distinguishable from *nobody-looked* from the record alone, and
   a duplicated role leaves evidence (M46's currency half remains out of scope) (E43.2).
3. **The rework limit exists once.** One statement in the normative tier, `+1` extension semantics
   reconciled, ten surfaces reaching it by carry/cite, and a check that fails on omission — the
   generalization of `P12-GH-1` ("no test detects the omission") now has a test (E43.3).
4. **The system's first fail-closed default, and it is itself validated.** Exhausted rework flips the
   receiving parent to manual — opt-out, on by default, blessed in the yml spec, performed and
   recorded by Drivr; resume restores the declared mode and never promotes or resets the budget
   (E43.4).

**Net:** the four changes share one property — each removes a *choice* an agent might refuse to make,
in favour of a *fact* that cannot be refused. M43 gates nothing and nothing gates it, but **P12 cannot
close without it**; on consolidation it delivers the acceptance spine the phase's remaining milestones
(M44's rituals, M47's proof) run against.

---

## Required Action: Consolidation

**To fully close this milestone, consolidation is required — and, per E43.1's now-landed rule, it is
performed by the parent.**

1. **The Phase Chat performs the merge** of `milestone/M43` → `phase/P12` (E43.1: *"the parent
   performs the merge of a child's branch"* — this is the first milestone-level application of it).
2. **The Phase Chat reviews this Declaration and the four epic merges** (G2 — re-measure, do not take
   the executor's word), and accepts the milestone by **an in-chat acknowledgment naming the party
   that reviewed and accepted** (E43.2 — silence accepts nothing).
3. **Merge authorization** follows the Phase Chat's Stage-2 review and **explicit human
   authorization** — acceptance is not authorization, and this Milestone Chat does not merge on its
   own decision.
4. **Flip the milestone spec's `status` from `planned` to `completed`** on consolidation (the M42
   lesson: a stale `status: planned` is load-bearing — a `git show` of this frontmatter returns
   `planned` until it is flipped, and a downstream gate read it as "not done" in M42).
5. **Report the merge commit SHA back** to complete the record.

**No next milestone branches from M43** — M43 gates nothing. **P12's closure, however, requires this
consolidation.**

---

## Stage-2 Review — Phase Chat Decision: **ACCEPTED**

**Reviewed and accepted by:** the **P12 Phase Execution Chat** (this session, `4710216f`), acting as
M43's parent. **Reviewed at:** `origin/milestone/M43` @ `4c1c17a`, on 2026-09-03.

*This acknowledgment is named and attributable because **E43.2 now requires it**. M43's own
consolidation is the first acceptance in this framework's history that could not have been performed
by silence — the rule landed four commits ago and binds the acceptance of the milestone that landed
it. Recorded here rather than sent as a message: the channel is routing, the artifact is the record.*

### Re-measured, not inherited (G2)

| Claim | Re-measured | Result |
|---|---|---|
| Suite **740 passed / 0 failed** | isolated worktree at `origin/milestone/M43` | **740 passed** — exact |
| Validator: no warning for the two gate keys, exactly one for `model_verification` | `bin/ai-project-validate .ai-project.yml` | **0 errors, 1 warning** — `model_verification` (line 93), both gate keys clean |
| `rework_exhaustion_flip` / `cfo_review_gate` blessed | `.ai-project.yml` `:29`/`:19`; `ai-project-yml-spec.md` `:47`/`:44`, §3.7 `:564` | **confirmed** |
| E43.1 landed normatively | `PROJECT-SYSTEM-GUIDELINES.md:589` (and the workflow at `:37`) | *"the merge of a child's branch is performed by the parent"* — **present** |
| E43.2 landed normatively | `PROJECT-SYSTEM-GUIDELINES.md:562` | *"merge + in-chat acknowledgment; no artifact; silence accepts nothing"* — **present** |
| E43.3 single statement | `PROJECT-SYSTEM-GUIDELINES.md:617-619` | *"stated once, here"* — **present** |
| E43.4 flip | `PROJECT-SYSTEM-GUIDELINES.md:632` | *"Exhausted rework flips the receiving parent to manual"* — **present** |
| `P12-GH-1` closed (was: 0 templates) | `governance/templates/` | **7 of 25 templates** now reach the limit, including all three starter templates. Substantively closed |
| Drivr half **469 passed** | `~/soft-dev/drivr`, `PYTHONPATH=. pytest -q` | **469 passed** — exact, **but see Carry-forward D for the ref** |

### Carry-forwards — the three declared are accepted as written; a fourth is added

**A, B and C are accepted as recorded.** A (`model_verification` is an unblessed top-level key) is
**corroborated from a second, independent direction**: the Phase Chat has separately measured that
`model_verification` has **no enforcement mechanism at all** — zero occurrences in `bin/`, `tests/`
or `lib/` under that name or seven synonyms, and the only model check that exists
(`run-dev-agent`'s `check_local_availability`) explicitly exempts `remote:`-prefixed values, which is
what `phase` and `milestone` are. **So the key is neither blessed by the schema nor read by any
code.** E43.4 found the schema half; the Phase Chat found the enforcement half; they are the same
defect. This matters at P12's closure, where the key is scheduled to flip `advisory → blocking`:
**flipping it would change a word that nothing reads.** Held in the Phase Chat's thread by CFO
instruction until M47 completes, then disposed with E41.5's ungated routing rows as one item.

**D — NEW, found at this review: the Drivr half of E43.4 is verified but NOT MERGED.**
The 469-passing suite was measured on **`epic/P12-M43-E43.4`** (`af3904d`), which is **one commit
ahead of Drivr's `main` (`f60164c`) and not merged into it.** The entire deliverable —
`drivr/modes/__init__.py`, `drivr/modes/record.py` (317 lines, the flip/resume implementation) and
its 244-line test file — **exists only on that branch**; `main` contains none of it. Drivr is a
**local-only repository with no remote**, so there is no PR and the merge is a local act.

*The declaration is not inaccurate — it states the Drivr number and scopes it as "not covered by this
repo's suite."* **What it omits is the ref**, and here the ref is the load-bearing part: DoD items 5
and 7 read as *the flip exists and Drivr performs it*, and in Drivr's mainline **it does not yet.**
This is `P11-GH-2` — *state the layer, time, scope **and ref*** — which **M43 itself strengthened into
its own milestone spec during planning**, applied to M43's own closure. A number without a ref is not
a measurement.

**Consequence:** M43's in-repo half is complete and binding on consolidation. **P12 may not claim the
fail-closed flip is operative until Drivr's `epic/P12-M43-E43.4` merges to `main`** — a mechanical
step on written, passing code, not missing work. Carried to the phase record.

### One consistency note, recorded and not blocking

E43.1 versioned its normative addition as a **patch** (PSG `2.4.1`), while E43.2, E43.3 and E43.4
versioned the same class of change — adding a normative statement to §11.6 — as **minor** (`2.5.0`,
`2.6.0`, `2.7.0`). All four are the same kind of act. The content is fully recorded either way, so
this changes nothing substantive; it is noted because versioning is itself a governance surface and
P12's subject is records that say what happened.

### Disposition

**ACCEPTED.** All eleven DoD items verified; the five milestone acceptance criteria hold. No rework
attempt consumed; each epic stands at attempt 1 of 3.

**Consolidation is the Phase Chat's to perform** (E43.1's first milestone-level application), and it
**awaits explicit CFO merge authorization** — acceptance is not authorization. On authorization the
Phase Chat merges `milestone/M43 → phase/P12`, flips this milestone spec's `status` to `completed` in
the same act (the M42 lesson: a stale `planned` is load-bearing), and reports the SHA.
