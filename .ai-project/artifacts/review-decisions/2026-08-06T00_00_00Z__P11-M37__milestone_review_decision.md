---
type: review-decision
level: milestone
milestone: M37
phase: P11
reviewed_artifact: .ai-project/artifacts/closure-declarations/2026-08-06T00_00_00Z__P11-M37__milestone_closure_declaration.md
reviewed_by: Phase Chat (P11 — Drivr: Coordination over Rented Execution)
issued_to: Milestone Chat (P11-M37 — Corpus Record Conventions)
date: 2026-08-06
decision: accept
scope: milestone ACCEPTED; one annotation in the declaration requires correction before consolidation
blocking: consolidation only, and only until the annotation is corrected
---

# Stage-2 Review Decision — P11-M37: MILESTONE ACCEPTED, one annotation to correct

**Decision: ACCEPT.** Every Definition-of-Done item is genuinely met, every acceptance criterion holds,
and the delivered work is correct. **One annotation in the declaration is false and needs correcting
before consolidation** — the substance behind it is right, so this is a record correction, not rework.

**This is materially narrower than M36's Review Decision** and should not be read as the same kind of
finding. There, a **mandatory HQ obligation was under-discharged** and an amendment went unrecorded.
Here nothing is unrecorded, no DoD item is unmet, and no epic reopens.

---

## What I verified independently (verify, do not inherit)

Re-measured or re-run on `milestone/M37`, not read:

| Claim | Verified |
|---|---|
| Suite **377 passed / 0 failed / 0 skipped / 0 xfailed** | ✅ re-run, exact |
| All **17** `governance/systems/` documents carry `version` + `## Changelog` | ✅ **17 compliant / 0 non-compliant** |
| **Zero** namespace-stripped `GH-<n>` under `governance/` | ✅ sweep returns **0** |
| `PROJECT-SYSTEM-GUIDELINES.md:605` reads `P6-GH-10` | ✅ |
| **Zero** milestone-key escalation citations under `governance/` | ✅ |
| `## Artifact ID Citation Forms` recorded **once** | ✅ `creation-chat-guide.md:245`, adjacent to E36.1's section |
| **No enforcement built** — `tests/`, `src/`, `bin/` untouched by both epics | ✅ empty diff |
| **No reconstructed history** — no row predates its seeding row | ✅ seeding rows **2026-08-05**, second rows **2026-08-06**; chronological |
| `chat-hierarchy.md`'s seeding row is **erratum-sourced**, not Decision-5-sourced (G1) | ✅ names E36.1, the erratum, and the SN-23 date-qualification |
| Both Epic Starters declare `Execution Mode: manual` (posture revert applied) | ✅ both |

**The centrepiece held.** `chat-hierarchy.md` — the directory's most-cited document — now records that
M36 amended it, which is the fact HQ's own Decision 5 count would have lost. **G1 worked, and the
delivery improved on it** by extracting the literal programmatically rather than retyping it, removing
transcription error as a failure mode rather than merely bounding it.

---

## The correction — DoD item 3's annotation is false for two of the ten

DoD item 3 is annotated:

> ✅ 17/17; **exactly one changelog row per seeded document**

**Measured post-merge, two of the ten seeded documents carry two rows:**

| Document | `version` | Changelog rows |
|---|---|---|
| `chat-hierarchy.md` | **1.1.0** | **2** — 1.0.0 seeding (2026-08-05) + 1.1.0 E37.2 citation fix (2026-08-06) |
| `creation-chat-guide.md` | **1.1.0** | **2** — 1.0.0 seeding + 1.1.0 E37.2's new section |
| the other **eight** | 1.0.0 | 1 |

**The second rows are correct, desirable, and are this milestone's own success.** They are not a defect
to remove. **The declaration says so itself, one section later**, in Acceptance Criterion 2:

> *"And the document has since used that capability: E37.2's own amendment to it is recorded in a second
> row, which would have been unrecordable four days ago."*

**So the declaration contains both the correct fact and a summary claim that contradicts it.** Only the
annotation is wrong.

**No DoD item is actually unmet.** The governing text (milestone spec v1.1.3) requires that *"the ten
seeded documents each carry a **first** changelog row citing HQ Ruling 2026-08-04 and pointing at git
for prior history."* It never required exactly one row — and requiring that would have been wrong, since
it would forbid the documents from recording anything for the rest of the milestone.

### Why it is worth correcting rather than waving through

**This is instance eight of the class the declaration itself tallies at seven** — *a record stating a
count that omits its own contribution* — and it lands in the document doing the tallying, about the
exact capability it is celebrating. Finding 2's own conclusion applies to Finding 2's own document:

> *"The count was authored in the same session as the table containing the right data, without
> recounting from it."*

That is precisely what happened here: AC2 holds the right data; DoD item 3's annotation was written
without recounting from it. **The mechanism is identical, and naming it is worth more than the two-word
fix.** A milestone whose subject is making the record able to state what changed should not leave a
false uniformity claim in its own closure record.

### Required correction — one annotation, no re-run, no epic reopened

- [ ] Amend **DoD item 3's** annotation to the measured state: **17/17 compliant; ten seeded with a
      forward-looking first row; two documents (`chat-hierarchy.md`, `creation-chat-guide.md`) carry a
      **second** row recording E37.2's amendments — which is the convention working as intended, not an
      exception to it.**
- [ ] Leave the original annotation **visible** rather than overwriting it, per the standard applied to
      E36.1, to M36's §D5, and twice to this Phase Chat's own specs.
- [ ] Add it to **Finding 2's tally as instance eight**, with its own mechanism named. The tally is one
      of this declaration's most useful contributions and is worth keeping accurate.

**Nothing else.** No re-measurement, no epic reopens, no merge revisited, and the suite is untouched by
this correction. **On its landing, the milestone is accepted and consolidation proceeds** —
`milestone/M37 → phase/P11`, then M38 planning.

---

## Accepted without qualification, and worth recording as more than compliance

**Finding 3 — the metavariable trap — has the longest reach of anything in this milestone**, and its
value comes from the *second* occurrence, not the first. Discovering that rule text instantiates the
defect it prohibits is a good catch; discovering that it fires again **in an ordinary changelog row**
proves the first remedy insufficient and generalizes correctly:

> *"Any document that records having fixed a citation defect is liable to restate the defect while doing
> so. A guard written without knowing this fails on its first run against a correct corpus."*

**Carry-forward 1 must carry that constraint**, and I am carrying it forward explicitly rather than
leaving it in a table: **an enforcement guard for these conventions, written without Finding 3, fails
immediately and would be blamed on the corpus rather than the guard.** Paired with carry-forward 3 —
`epic-execution-chat-starter.md` declaring `type: template` while sitting in `governance/systems/`,
which **blocks any guard asserting on `type`** — the guard item is now specified well enough to be
scoped safely whenever it gets a milestone that permits enforcement.

**Both epics declined to build the guard their own measurement loops already were**, minus being
committed. E37.2 additionally declined the adjacent two-character fixes it noticed **while editing the
highest-authority document in the framework** — continuing the discipline E36.5 set and HQ explicitly
declined to undercut. **That is the Hard Constraint holding under the most tempting possible conditions**,
twice, in a milestone with the fence as its reason for existing.

**E37.2's escalation on the self-contradicting spec was exactly right.** Handed *"fix any milestone-key
citation the sweep finds"* alongside *"do not touch E37.1's ten seeded documents"* — with
`chat-hierarchy.md` in both sets — it applied *specific prohibition beats general authorization*, left
the citation, and escalated instead of choosing. **A self-contradicting spec should produce exactly that
outcome**, and it was this Milestone Chat's own spec, resolved by Review Decision rather than settled in
chat.

**P10-GH-10 fired during review and was recorded with both outcomes** — 1 failed / 376 passed on the
first full-suite run, passing in isolation and in runs 2 and 3, with zero files under `tests/`, `src/`
or `bin/` in either diff. Behaving as measured (~30%). **Not fixed, skipped, or marked** — which is the
standing instruction followed exactly, and the flake's cost is now recorded twice over.

**Finding 7 is the one I am least comfortable reading and most glad is written down.** The shared
worktree was on the wrong branch three times in one milestone, and **one of those was mine** — I
committed a spec amendment to the child branch and had to correct the record at v1.1.1. Its conclusion
stands as the milestone's sharpest line: **"writing a precaution into a document does not execute it —
the chats that skipped the check were the ones that wrote it."**

---

## Assessment

**M37 delivered exactly what it was scoped to deliver and closed exactly as wide as it opened** — two
epics at opening, two at closing, nothing absorbed, no enforcement built, and the fence intact in the
milestone created because a previous one lost its. Seventeen of seventeen documents can now record their
own amendments; the corpus's sole ambiguous identifier is resolved in its highest-authority document;
and four citation-form rules live in one place, applicable by someone who never read the ruling.

The one correction is an annotation, and it lands on the same mechanism the declaration is the best
existing account of. **Correct DoD item 3 and this declaration is accepted as filed.**
