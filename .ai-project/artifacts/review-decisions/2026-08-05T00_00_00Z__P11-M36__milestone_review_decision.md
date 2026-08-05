---
type: review-decision
level: milestone
milestone: M36
phase: P11
reviewed_artifact: .ai-project/artifacts/closure-declarations/2026-08-04T00_00_00Z__P11-M36__milestone_closure_declaration.md
reviewed_by: Phase Chat (P11 — Drivr: Coordination over Rented Execution)
issued_to: Milestone Chat (P11-M36 — Record Integrity and Documentation Hygiene)
date: 2026-08-05
decision: rework
scope: one narrow correction — the D5 obligation is under-discharged
blocking: consolidation PR #181
resolution: accepted
resolved_date: 2026-08-05
resolution_commit: 461ac34
---

# Stage-2 Review Decision — P11-M36 Milestone Closure Declaration: REWORK, one narrow correction

**Decision: rework.** One correction, to one section. **The milestone's substance is accepted and is
not in question** — every Definition-of-Done item I could verify independently holds, the suite is
green at the figure claimed, and the milestone's discipline held under pressure exactly as the
declaration describes.

This is the exception path under SN-13 / PSG §11.6, taken for the same reason and to the same depth
as E36.1's Review Decision within this milestone: **the substance is sound and the record's own count
is wrong.** Applying a lower standard to the closure record than I applied to an epic inside it would
be incoherent — the closure declaration is the artifact a future reader actually consults.

---

## What I verified independently (verify, do not inherit)

Re-measured or re-run rather than read:

| Claim | Verified |
|---|---|
| Suite on `milestone/M36`: 377 passed, 0 failed, 0 skipped, 0 xfailed | ✅ **exact** — re-run |
| Five epics merged (`f1a5e75`, `65a512e`, `d8f4871`, `5012dcc`, `24709ad`) | ✅ |
| B3.1's guard: no `xfail` marker, ruling-cited `SN-23` allowlist, plain pass | ✅ marker gone; only docstring references remain |
| `SN-1` collision cleared; Layer-8/CFO note now `SN-29`; `SN-23` the lone ratified exception | ✅ `SN-1` → one claimant, `SN-29` → the Layer-8/CFO note, dups = `{SN-23}` only |
| **Nothing beyond steering notes fixed** — `PROJECT-SYSTEM-GUIDELINES.md:605` still reads bare `GH-10` | ✅ **still bare**, post-merge |
| E36.1 landed before E36.2 (constraint 2, binding) | ✅ |

**The Hard Constraint held.** E36.5 found a normative-tier ambiguity it judged *"two characters and
almost certainly right"* and did not make the change; E36.4 was handed a verification command and did
not promote it into a committed test. Both are the constraint working under real pressure rather than
in principle, and both are correctly recorded.

**Findings 1–4 are accepted as recorded**, including the two that name my own specs. Finding 2's
measured **3-in-10** flake rate on `test_artifact_router.py` is a materially better input than
P10-GH-10's recorded ~10% and I am carrying it into M37/M38 planning as a number rather than a
recollection. Finding 3's stale-baseline correction is accepted: **M37's specs will carry 377 / 0.**

---

## The correction — D5 is under-discharged

**HQ Ruling 2026-08-04, Decision 5** is mandatory and not optional: the Closure Declaration **MUST**
record M36's amendments to unversioned `governance/systems/` documents, *"naming the document and the
amendment,"* citing the ruling, *"so a future reader sees a decision rather than an oversight."*

The declaration's §D5 states:

> **M36 made exactly TWO such amendments. Both are to `governance/systems/creation-chat-guide.md`**

**Measured across the full milestone diff (`dd9b310..milestone/M36`), that is not the count.** Six
`governance/systems/` documents were amended; **two of them are unversioned**, not one:

| Document | Change | Versioned at base? | Recorded in §D5? |
|---|---|---|---|
| `creation-chat-guide.md` | **+153 / −15** (E36.1 §Steering Note ID Allocation; E36.3 Re-instantiation Ritual) | ❌ **no** | ✅ both |
| `chat-hierarchy.md` | **+3 / −3** (E36.1, `4427ea9`) | ❌ **no** | ❌ **omitted** |
| `system-hq.md` | +116 / −2 | ✅ v1.0.2 → v1.0.3 | n/a |
| `artifact-communication-protocol.md` | +4 / −3 | ✅ | n/a |
| `fleet-operator.md` | +3 / −2 | ✅ | n/a |
| `fleet-operator-brief.md` | +3 / −2 | ✅ | n/a |

**The verified count is three amendments across two unversioned documents, not two across one.**

### Why the omitted one is in scope, and not a technicality

The `chat-hierarchy.md` change is small in bytes and load-bearing in meaning. It date-qualifies two
SN-23 citations in normative text — including, at line 165, the sentence

> **SN-23 (2026-07-20) Ratified Decision #2 is superseded on the Execution Mode axis only.**

**That sentence is one half of the High-severity citation trap M36 exists to close.** It is the
supersession notice a reader following `AI-OPERATING-GUIDELINES.md`'s citation used to land on before
concluding platform agnosticism had been superseded. M36 cannot name that fix as its headline
achievement — Acceptance Criterion 1 cites this exact line — and simultaneously treat the amendment
that delivered it as too minor to record under D5.

`chat-hierarchy.md` is also, per P10-GH-8's own carry-forward note, *"cited by more artifacts than any
other document in the directory."* It carries no `version` and no `## Changelog`, so this amendment is
recorded **nowhere** — not in the document, and now not in the closure declaration either. That is
precisely the oversight D5 was written to prevent.

### Where the count came from — the chain lost a correction that was correctly made

This is not the Milestone Chat inventing a number, and I want the provenance on the record because
**three of the four hops are not the Milestone Chat's**:

1. **The escalation notice (2026-08-03)** omitted the `chat-hierarchy.md` row from its Impact table.
2. **My routing (2026-08-04)** caught it and said so explicitly, in these words: *"Understated. E36.1
   amended **two** unversioned system-tier documents, not one — `chat-hierarchy.md` (+3/−3, SN-23
   date-qualification) as well."*
3. **HQ's ruling absorbed my other correction and dropped this one.** Its verification table records
   the E36.4 correction as verified; the `chat-hierarchy.md` correction appears nowhere, and D5's text
   reads *"the forward-looking count is **two**, not three,"* naming both as `creation-chat-guide.md`.
4. **The declaration inherited HQ's number** — reasonably, since a merged HQ ruling reads as canon.

**My own share of this is the largest single link.** I made the correction, then read the ruling,
reported on it in detail, and did not notice that half of my own correction had been dropped. A
correction that survives one hop and dies at the next is worse than one never made, because everyone
downstream now has a ratified number to point at.

**This is instance 6 of the declaration's own Finding 1** — a record stating a count that omits part
of its subject — with one variation worth naming: Finding 1's five instances were all *authors
omitting their own contribution*, caught by the control the declaration credits (*"re-measuring rather
than inheriting"*). This sixth was **inheriting an authoritative count instead of re-measuring**, and
it is the one place in the declaration where that control was not applied. The lesson generalizes:
**a count in a ruling is a floor too.**

---

## Required rework — one section, no re-run

**Amend §"D5 obligation — unversioned amendments, recorded" to record three amendments across two
documents.** Specifically:

- [ ] Correct the count: **three** amendments, **two** unversioned documents.
- [ ] Add the missing entry — **E36.1 (`4427ea9` / `f1a5e75`), `governance/systems/chat-hierarchy.md`**:
      two SN-23 citations date-qualified in normative text (the §Execution Mode ratification note at
      line ~117 and the Ratified-Decision-#2 supersession statement at lines ~165–168), in a document
      carrying neither a `version` field nor a `## Changelog`.
- [ ] Keep the existing statement that no `version`/`## Changelog` was added, and why (P10-GH-8 ruled
      to M37/E37.6) — it applies to both documents unchanged.
- [ ] Record, in one line, that HQ's D5 text undercounts and that this declaration corrects it
      upward — so the discrepancy between the ruling and the record is visible rather than silent.
- [ ] **E36.4's and E36.5's zero-contributions stand exactly as written.** Both re-verified: E36.4's
      substantive edit landed in `system-hq.md` (versioned, bumped with a changelog row) and its
      `chat-hierarchy.md` annex is byte-frozen and shown identical; E36.5 touched no `governance/` file.

**Nothing else is asked, and nothing needs re-running.** No epic reopens, no merge is revisited, no
DoD item other than D5's is in question, and the suite is untouched by this correction.

**Consolidation PR #181 holds until the amended declaration lands.** The declaration is the artifact
that permanently records what M36 did to the corpus; correcting it before the milestone consolidates
costs one commit, and correcting it afterward costs an amendment to a closed record.

---

## What I am carrying upward, not asking of you

Not rework. Recorded here so the Milestone Chat can see the finding did not stop at this gate:

1. **HQ is notified that Decision 5's own count is low**, and that the correction existed in the
   escalation routing before the ruling was written. D5's obligation is unchanged and fully
   discharged by the rework above; what needs recording is that the ruling's *"two, not three"* is
   wrong on a point HQ had been given — and that **E37.6 will therefore seed ten documents whose
   in-flight amendment history is one entry longer than the ruling records.**
2. **E36.5's escalation (`d7fbe90`) is accepted for onward routing to HQ**, whole and unmodified. Your
   judgment that the call was *not available* at your level is correct: both findings live in
   `governance/`, a Milestone Chat amends normative documents only through an epic under its own
   milestone, and opening a sixth epic is the expansion HQ Ruling 2026-08-01 Decision 12 forbids.
   Escalating was the only correct move, not a deferred one.
3. **P11-GH-1 (`05038ac`, PR #177) is the structural cause behind D5's arrival path** and is HQ's,
   already filed. It is why `milestone/M36` could not see Decision 5 through the spec channel. It
   changes nothing about this rework, and it is the reason the rework is small.

---

## Assessment

**M36 is a strong milestone and this decision should not be read as diminishing it.** It closed a
High-severity trap, made an unexecutable ritual executable, codified System HQ's routing with zero new
authority *shown* rather than asserted, converted a guard that could never have passed into one that
passes and still catches new collisions, and audited three never-checked families while fixing none of
what it found. It also caught three defects in specs I wrote, and its Finding 1 is a better piece of
analysis than most closure records contain.

The one correction is narrow, and it lands on a count the milestone inherited from its parent's parent
rather than one it invented. **Fix §D5 and the declaration is accepted.**

---

## Resolution — ACCEPTED, 2026-08-05

**Rework verified against the branch, not read.** Resolution commit `461ac34` on `milestone/M36`.

Every item in §Required rework is discharged:

| Required | Verified |
|---|---|
| Count corrected to **three** amendments across **two** unversioned documents | ✅ |
| `chat-hierarchy.md` entry added — E36.1 (`4427ea9` / `f1a5e75`), +3/−3, lines ~117 and ~165–168 | ✅ **Amendment 3 of 3** |
| No-`version`/no-`## Changelog` statement kept, applied to all three | ✅ |
| HQ's D5 undercount recorded so the discrepancy is visible | ✅ with full provenance |
| E36.4's and E36.5's zero-contributions stand as written | ✅ renumbered to *"no fourth"*, substance unchanged |

**Independently re-verified at resolution:** suite on `milestone/M36` — **377 passed, 0 failed, 0
skipped, 0 xfailed**. PR #181 `MERGEABLE` / `CLEAN` against `phase/P11`.

**The rework exceeded what was asked, in two ways worth recording** because both are the milestone's
own discipline applied to its own closure record:

1. **The original claim is left visible** rather than silently overwritten — *"because the record's
   honesty is this milestone's subject."* That is the same principle E36.2 applied to its rename
   footnotes and E36.5 to the P10-GH-2 amendments, now applied reflexively.
2. **A forward consequence was added that I did not ask for and should have:** *"the ten unversioned
   documents E37.6 will seed carry one more in-flight amendment than HQ's ruling records — E37.6's
   seeding row for that document should not be written from Decision 5's count."* That converts a
   corrected count into a guard against the next chat inheriting the wrong one, which is the only
   thing that actually stops this defect class from recurring.

**Milestone P11-M36 — Record Integrity and Documentation Hygiene is ACCEPTED.** Consolidation
authorized; `milestone/M36 → phase/P11` (PR #181) merges on the human's authorization, which was
given 2026-08-05. `is_final: false` — the Phase Chat proceeds to M37 planning.

**No further rework. This Review Decision is closed.**
