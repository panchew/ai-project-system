---
type: milestone-closure-declaration
milestone: M36
status: complete
completion_date: 2026-08-04
declared_by: Milestone Chat (P11-M36 — Record Integrity and Documentation Hygiene)
issued_to: Phase Chat (P11 — Drivr: Coordination over Rented Execution)
is_final_milestone: false
---

# MILESTONE CLOSURE DECLARATION — M36

Milestone **P11-M36 — Record Integrity and Documentation Hygiene** is hereby declared **COMPLETE
(awaiting consolidation)**. Five epics — E36.1 through E36.5 — have been executed, **independently
verified by this Milestone Chat**, accepted under PSG §11.6 default-accept, and merged to
`milestone/M36` with explicit human merge authorization for each (SN-19 / §11.6).

**M36 is NOT P11's final milestone.** On consolidation the Phase Chat proceeds to **M37 planning**,
per the binding order M36 → M37 → M38 → M39. `phase/P11` is not merged to master until all four
milestones close.

Full suite green on `milestone/M36` @ `24709ad`: **377 passed, 0 failed, 0 skipped, 0 xfailed.**
See *Suite baseline* below — the figure moved twice during this milestone and the milestone spec's
`375 / 1 xfailed` is stale.

**What "independently verified" meant here.** Not Delivery Notices trusted on faith. Every epic's
central claim was re-checked against the committed diff or re-measured from primary sources: I ran
the Authority Boundary byte check myself rather than reading its output; I recomputed both of
E36.3's `sha256` freezes from scratch; I injected a real third collision into the live steering-note
corpus to confirm E36.2's guard fails and names both claimants; I counted bare `SN-23` occurrences
by two independent methods; and I read the P10-GH-4/5/6 carry-forward notes in full to adjudicate a
classification E36.5 challenged. **That last check found my own spec wrong** — see *Findings*.

---

## Completion Verification

✅ **All five Epics complete and merged to `milestone/M36`:**

| Epic | Name | PR | Merge |
|---|---|---|---|
| **E36.1** | Steering Note ID allocation rule + SN-23 date-qualified citations | #174 | `f1a5e75` |
| **E36.2** | Renumber the misnumbered Layer-8/CFO note (+ B3.1 test obligation) | #176 | `65a512e` |
| **E36.3** | Creation Chat re-instantiation reconciliation (SN-26) | #178 | `d8f4871` |
| **E36.4** | System HQ Routing & Origination codification (`SN-29`, D1–D4) | #179 | `5012dcc` |
| **E36.5** | P10-GH-2 re-diagnosis + bounded artifact-ID audit | #180 | `24709ad` |

✅ **All Epics accepted.** Four accepted by silence (SN-13 / PSG §11.6). **E36.1 received the
milestone's one Review Decision** — `reject / rework`, for an evidence-record miscount — and was
accepted after rework. Every merge carried explicit human authorization.

✅ **The binding internal order held.** E36.1 landed before E36.2 (constraint 2): the allocation
rule was **recorded** before anything was renumbered, so E36.2 applied a rule rather than inventing
one.

---

## Milestone Definition of Done — verified

| DoD item | Status | Verification |
|---|---|---|
| E36.1–E36.5 each meet their own DoD | ✅ | Per-epic Stage-2 review |
| All five epic branches merged to `milestone/M36` | ✅ | Table above |
| Allocation rule + separating rule recorded normatively | ✅ | `creation-chat-guide.md` §"Steering Note ID Allocation" (lines 97–170); `templates/steering-note.md` |
| **No un-dated SN-23 citation remains in the normative tier** | ✅ | 39 occurrences, 22 date-qualified, 17 bare — **none a citation**, all enumerated by justification class |
| Layer-8/CFO note carries a non-colliding ID; prior citations footnoted | ✅ | `SN-1` → **`SN-29`**; **seven** citing artifacts amended, not the spec's two |
| **B3.1's guard is a plain passing test with a ruling-cited `SN-23` allowlist; no `xfail`; a new duplicate fails** | ✅ | **Verified by injecting a real collision** — suite went red and named both claimants; corpus restored, 377 clean |
| One normative statement governs re-instantiation; E31.3 check on the path; `genesis.md`/Brief decided; Seed still verifies | ✅ | `creation-chat-guide.md` Steps 3–5; `seed.md` PV frozen at `f29ef0eb…` |
| `system-hq.md` carries Routing & Origination, D1–D3, no new authority; Authority Boundary shown byte-identical; issuer-vs-scribe explicit | ✅ | **Byte check re-run by this chat**: `baecaad4dbc2146c` × 3 |
| P10-GH-2's carry-forward text amended everywhere it is recorded, original legible | ✅ | **Seven** locations |
| Bounded artifact-ID audit recorded; **nothing beyond steering notes fixed** | ✅ | `PROJECT-SYSTEM-GUIDELINES.md:605` **still reads bare `GH-10`** — verified post-merge |
| Every normative amendment carries a Structural diagram | ✅ | E36.1, E36.3, E36.4 fired and delivered; E36.2 and E36.5 **stated** the obligation did not fire |
| Every Epic Starter declares `manual` + `models.epic_manual` | ✅ | All five; **no M36 epic routed to `local:`** |
| Full suite green, no regressions, no new skips | ✅ | **377 / 0 xfailed** |
| Milestone Closure Declaration produced (`is_final: false`) | ✅ | This document |

---

## Acceptance Criteria — verified

1. ✅ **The SN-23 citation trap is closed.** `AI-OPERATING-GUIDELINES.md:124` reads
   `SN-23 (2026-07-18) Decision 2, ratified`; `chat-hierarchy.md:165` reads
   `SN-23 (2026-07-20) Ratified Decision #2 is superseded…`. **A reader can no longer conflate them**,
   and cannot reach "platform agnosticism was superseded" by following a citation.
2. ✅ **A steering-note ID allocation rule exists**, with the separating rule recorded and an explicit
   statement of why SN-23 is not renumbered.
3. ✅ **The Layer-8/CFO note carries a non-colliding ID**, prior citations footnoted, and **the suite
   fails on a new duplicate while passing on the ratified `SN-23` exception — demonstrated by this
   chat, not asserted.**
4. ✅ **One normative statement governs re-instantiation**, the canonized path carries the E31.3
   check, the `genesis.md` question is decided, and the Seed's verification behaviour is preserved.
5. ✅ **System HQ's routing and origination are codified with zero new authority.** The §Out of Scope
   pin and SN-21/SN-22 pin stand byte-identical.
6. ✅ **P10-GH-2 points at the ritual, not at `seed.md`**, and the audit is recorded with its
   finding — **reported and escalated, not remediated inside M36.**
7. ✅ **Every normative amendment carries a Structural diagram.**
8. ✅ **The full suite is green at milestone delivery** — 377 / 0 xfailed.

---

## D5 obligation — unversioned amendments, recorded

**HQ Ruling 2026-08-04 (P10-GH-8), Decision 5** requires this declaration to record M36's amendments
to unversioned `governance/systems/` documents, naming document and amendment and citing the ruling,
*"so a future reader sees a decision rather than an oversight."*

> **Corrected 2026-08-05 following the Phase Chat's Stage-2 review of this declaration**
> (`.ai-project/artifacts/review-decisions/2026-08-05T00_00_00Z__P11-M36__milestone_review_decision.md`).
> This section previously read *"M36 made exactly TWO such amendments. Both are to
> `governance/systems/creation-chat-guide.md`."* **The verified count is THREE amendments across TWO
> unversioned documents** — `chat-hierarchy.md` was omitted. The original claim is left visible here
> because the record's honesty is this milestone's subject.
>
> **HQ Ruling 2026-08-04's own Decision 5 text undercounts**, stating *"the forward-looking count is
> **two**, not three,"* and naming both as `creation-chat-guide.md`. **This declaration corrects it
> upward.** The correction is not new information to HQ: the P11 Phase Chat's routing of the
> 2026-08-03 escalation (2026-08-04) stated it explicitly — *"E36.1 amended **two** unversioned
> system-tier documents, not one — `chat-hierarchy.md` (+3/−3, SN-23 date-qualification) as well"* —
> and the ruling absorbed the Phase Chat's other correction while dropping this one. **HQ is notified
> via this declaration and via the Phase Chat's review.**

**M36 made THREE such amendments, across TWO of the ten `governance/systems/` documents carrying
neither a `version` field nor a `## Changelog`** — `creation-chat-guide.md` (twice) and
`chat-hierarchy.md` (once). Measured across the full milestone diff `dd9b310..milestone/M36`, in
which **six** `governance/systems/` documents were amended; the other four are versioned and recorded
themselves normally.

**Amendment 1 of 3 — E36.1 (`f1a5e75`, 2026-08-03).** A new normative section, **"Steering Note ID
Allocation"** (~74 lines, now at lines 97–170), recording: the allocation rule (highest existing ID
in the directory plus one, regardless of issuing entity) with its reason; the separating rule
*a bookkeeping defect never rewrites a citation in a normative document*; and the explicit statement
that **SN-23 is not renumbered, and why**, with the two-meaning disambiguation table.

**Amendment 2 of 3 — E36.3 (`d8f4871`, 2026-08-04).** The **Re-instantiation Ritual** section
(lines 28–84) rewritten to become the **single normative statement** governing Creation Chat
re-instantiation. Step 3 opens a re-instantiated session with `seed.md` plus the latest Steering Note
plus the latest Progress Digest — **SN-26 Carry-Over 1 canonized unchanged**, discharging HQ Ruling
2026-08-01 Decision 9 — with a committed `genesis.md` as the single permitted optional addition
rather than the required artifact #1. A new **Step 4** places the P9-M31-E31.3 model check **on the
canonized path itself**. A new subsection, *"Why the Seed opens the session, and `genesis.md` may not
exist,"* records the bootstrap-vs-continuity diagnosis.

**Amendment 3 of 3 — E36.1 (`4427ea9`, merged `f1a5e75`, 2026-08-03), `governance/systems/chat-hierarchy.md`.**
**+3 / −3.** Two SN-23 citations date-qualified in **normative text**: the §Execution Mode
ratification note (line ~117) and the **Ratified-Decision-#2 supersession statement** (lines
~165–168), each `SN-23` → `SN-23 (2026-07-20)`.

> **This is the smallest amendment in the milestone and the least skippable.** Line 165 reads
> *"**SN-23 (2026-07-20) Ratified Decision #2 is superseded on the Execution Mode axis only**"* — and
> **that sentence is one half of the High-severity citation trap M36 exists to close.** It is the
> supersession notice a reader following `AI-OPERATING-GUIDELINES.md`'s citation used to land on
> before wrongly concluding platform agnosticism had been superseded. **Acceptance Criterion 1 cites
> this exact line.** M36 cannot claim that fix as its headline achievement and simultaneously treat
> the amendment that delivered it as too small to record here.
>
> `chat-hierarchy.md` is also, per P10-GH-8's own carry-forward note, *"cited by more artifacts than
> any other document in the directory."* It carries no `version` and no `## Changelog`, so **this
> amendment is recorded nowhere else** — which is exactly the oversight D5 exists to prevent.

**No `version` field and no `## Changelog` were added to any of the three amendments** — P10-GH-8 is
ruled to **M37/E37.6**. Each document's existing inline-dated-note precedent was used instead.

**Consequence for E37.6, stated so it is not discovered late:** the ten unversioned documents E37.6
will seed carry **one more in-flight amendment than HQ's ruling records** — `chat-hierarchy.md`'s.
E37.6's seeding row for that document should not be written from Decision 5's count.

**E36.4 added no fourth**, as HQ verified independently: its `chat-hierarchy.md` annex is byte-frozen
and *shown* identical rather than amended, and its substantive edit landed in `system-hq.md`, which
**is** versioned (bumped v1.0.2 → v1.0.3 with a changelog row). **E36.5 added none** — no
`governance/` file appears in its diff.

**Citation:** `.ai-project/artifacts/rulings/2026-08-04__ai-project-system-hq__ruling__p10-gh-8-versioning-convention.md`,
Decision 5.

---

## Milestone Summary

M36 landed four self-contained documentation items **governed** — with a spec, a Definition of Done,
a Stage-2 review and a closure record — **before any Drivr code exists**, which was the whole content
of the CFO's ruling placing it first.

It closed a **High-severity citation trap** in which following `AI-OPERATING-GUIDELINES.md`'s SN-23
citation by number led a reader to a supersession notice about an unrelated decision, and thence to
the false conclusion that platform agnosticism had been superseded. It gave steering-note IDs an
allocation rule and a separating principle so the defect cannot recur by attention lapse, renumbered
the one collision that could be cleared, and converted B3.1's guard from a blanket `xfail` — which
could never have passed, by decision — into a plain passing test with one ruling-cited exception that
**still fails on a genuinely new collision**. It made Creation Chat re-instantiation executable as
written, from three disagreeing surfaces to one normative statement carrying the model check on the
path itself. It codified System HQ's routing and origination with **zero new authority**, shown
rather than asserted. And it audited three never-checked artifact families, found two normative-tier
ambiguities, and **escalated both rather than fixing either.**

**Nothing was delayed except the ungoverned-ness.**

---

## Findings

### 1. The count-omission pattern — six instances, one root shape, two distinct causes

M36 produced **six** instances of the same defect: *a record stating a count that omits part of its
subject.* Recorded as one finding rather than six corrections, because the shape is the point.

> **Instance 6 was added 2026-08-05, after the Phase Chat's Stage-2 review of this declaration found
> §D5 undercounting** — see the corrected §D5 above. It is recorded here rather than only there
> because it is the **most instructive** of the six and because leaving the finding at five, once the
> sixth is known, would be the very defect the finding describes.

| # | Record | Stated | Actual |
|---|---|---|---|
| 1 | E36.1's sweep evidence §4 | 4 bare `SN-23`, "all in the allocation section" | **17**, 13 in the epic's own new changelog rows |
| 2 | HQ Ruling 2026-08-01:124 | `SN-1` "cited in two non-normative artifacts" | **three** — the ruling did not count itself |
| 3 | E36.2's spec (mine) | 3 citing artifacts / 10 occurrences | **seven** / 21 |
| 4 | E36.2's spec (mine) | suite would be **376** | **377** — omitted the test constraint 2a mandates |
| 5 | E36.5's spec (mine) | 4 P10-GH-2 restatements | **seven** |
| 6 | **§D5 of this declaration (mine)** | **2 unversioned amendments, 1 document** | **three across two** |

**Instances 1–5 share one cause: an author omitting their own contribution**, and every one was
caught by the same control — **re-measuring rather than inheriting.**

**Instance 6 has the opposite cause, and that is why it matters most.** §D5's count was not invented;
it was **inherited from HQ Ruling 2026-08-04's own Decision 5 text** (*"the forward-looking count is
two, not three"*), which reads as canon because it is a merged ruling. I had both primary facts in
hand — I verified E36.1's `chat-hierarchy.md` hunks myself during its Stage-2 review, and I verified
`chat-hierarchy.md` as unversioned myself when raising the P10-GH-8 escalation — **and used the
inherited number anyway.** This is the one place in the milestone where the control that caught the
other five was not applied.

**The lesson generalizes, and is the finding's real content: a count in a ruling is a floor too.**
Authority makes a number harder to question, not more likely to be right. The correction had even
survived one hop — the Phase Chat's routing stated it explicitly on 2026-08-04 — and died at the
next when the ruling absorbed one half of it. **A correction that survives one hop and dies at the
next is worse than one never made**, because everyone downstream then has a ratified number to point
at.

**Four of the six are mine.** Instance 5 was caught by the epic I had specified — E36.5 correctly
applied my stated **rule** over my worked **example** and flagged the departure instead of absorbing
it. Instance 6 was caught by my parent applying to my closure record exactly the standard I had
applied to an epic inside it. **Both are the behaviour the milestone was built to produce**, working
in both directions of the chain.

### 2. P10-GH-10 is worse than recorded — measured, not estimated

`tests/test_artifact_router.py::test_daemon_extensions_error_branches` fails intermittently in
**full-suite runs only**; it passes 5/5 in isolation. Measured across this milestone's reviews, on
multiple branches, never touched by any M36 epic:

**3 failures in 10 full-suite runs ≈ 30%, against a recorded ~10%.**

Twice it produced a red suite on a delivery that changed no test file, and **once it came within one
unrepeated run of costing a clean epic a false rejection.** HQ named this risk against **M38**
specifically — *"'full suite green' is weaker evidence while a ~10%-flaky test sits in it."* At 30%,
an M38 evidence run has roughly a **one-in-three chance of a spurious red**, and "just re-run" is
precisely what makes suite-shaped evidence unfalsifiable. **Recorded as a measurement so M38 inherits
a number rather than a recollection.** Not scoped into M36; recommended as an amendment to
P10-GH-10's severity input rather than new scope.

### 3. Suite baseline moved twice

`375 passed / 1 xfailed` at milestone open → **`377 passed / 0 xfailed`** at close. E36.2 converted
B3.1's `xfail` to a pass (+1) and added the synthetic-third-collision test constraint 2a mandates
(+1). **The milestone spec's `375 / 1 xfailed` is stale in its DoD and Acceptance Criteria.** M37's
specs should carry **377 / 0**.

### 4. The shared worktree hazard recurred

This repository is worked by multiple sessions and was left on another branch mid-task during this
milestone, producing a false "content is missing" alarm during E36.3's clearance check. Caught by a
file-length comparison. **Every subsequent Epic Starter carried a branch check as its first
prerequisite.** Recommended as standing practice for M37.

---

## Carry-forwards

| Item | Status | Owner |
|---|---|---|
| **E36.5's escalation** — two normative-tier citation ambiguities: bare `GH-10` at `PROJECT-SYSTEM-GUIDELINES.md:605` (ambiguous between `P5-GH-10` and `P6-GH-10`), and *"P10-M34 Escalation Notice"* resolving to two documents, cited at `chat-hierarchy.md:271` and `ai-project-yml-spec.md:660` | **OPEN** — issued to this chat, **routed to the Phase Chat for HQ** | HQ |
| **P10-GH-8** — `governance/systems/` versioning convention | **Ruled and scheduled** → **M37/E37.6** | M37 |
| **P10-GH-10** — flaky `test_artifact_router.py` | **Open**, now with a measured ~30% rate (Finding 2) | Unowned; named in M38's context |
| Convention inconsistencies found by the audit — non-uniform `GH-` allocation across phases; 3 of 8 rulings carry no `concern_id` | **Reported, not fixed** — characterized in the audit artifact | Unowned |
| `rulings/` date ambiguity (2026-07-28 ×2, 2026-07-31 ×2) | **Reported and left** — project-internal only; every normative citation resolves | Unowned |

**Nothing beyond steering notes was remediated. M36 closes exactly as wide as it opened.**

---

## Required Action: Consolidation

1. **Create Pull Request:**
   - Source: `milestone/M36`
   - Target: `phase/P11`
   - Title: `Milestone M36: Record Integrity and Documentation Hygiene`
   - Description: this declaration's summary and Epic list

2. **Human reviews the consolidation PR** — per PSG §11.6.1 the CFO is the mandatory diff reviewer.

3. **Merge PR** (becomes the milestone closure commit).

4. **Report merge commit SHA back to the Phase Chat.**

**M36 is NOT P11's final milestone (`is_final: false`).** After consolidation the Phase Chat proceeds
to **M37 planning** — Drivr inception, registry and adapter, plus **E37.6** (the P10-GH-8 versioning
convention, ruled 2026-08-04). **`milestone/M37` MUST branch from `phase/P11` after this merge.**
Phase closure does not begin until all four milestones close.

---

## Notes

- **M36 executed rulings; it made none.** Every epic traced to a CFO decision or an HQ ruling already
  on the record. Where genuine design decisions remained they were named as such and assigned — and
  **all four of E36.3's were decided by the epic, none escalated.**
- **The milestone's discipline was tested twice and held twice.** E36.5 found a normative-tier
  ambiguity whose fix it judged *"two characters and almost certainly right"* — and did not make it,
  naming that asymmetry as the reason. E36.4 was handed a verification command and did not promote it
  into a committed test. Both are the Hard Constraint working under real pressure rather than in
  principle.
- **One correction of the record, stated plainly:** the P11 starter's constraint 2a mechanism was
  wrong — SN-23's collision is permanent by decision, so B3.1's strict `xfail` could never XPASS and
  removing it would have left a failing test. The corrected obligation was recorded in the milestone
  spec before execution and discharged by E36.2. **HQ is notified via this declaration**, as the
  milestone spec undertook.
