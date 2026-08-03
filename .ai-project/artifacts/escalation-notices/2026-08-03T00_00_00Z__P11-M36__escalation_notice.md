---
type: escalation-notice
milestone: M36
issued_by: Milestone Chat (P11-M36)
issued_to: Phase Chat (P11) — for routing to HQ, which owns the decision
date: 2026-08-03
status: open
---

# Escalation Notice: P10-GH-8's own revisit trigger has fired inside M36

## Trigger

**Out-of-scope finding whose owning decision sits above this chat.** This is not a request to
reconsider a parked item on preference. **P10-GH-8's recorded trigger condition has been met, and
met inside M36.**

The P10-M35 carry-forward note
(`docs/phases/P10__Fleet_Adoption_and_Local_Inference_Proving/P10-M35__carry-forward-note__P10-GH-8-unversioned-system-documents.md`)
states its own revisit condition verbatim:

> **Trigger for revisit:** the next epic that amends a system-tier document and finds itself unable
> to state what changed since a prior known-good state. Whoever takes it should decide the convention
> **once** for all 15 documents rather than per-document under a passing edit.

**E36.1 is that epic.** It added an entire new normative section — *"Steering Note ID Allocation"*,
carrying the allocation rule, the separating rule and the SN-23 non-renumbering statement — to
`governance/systems/creation-chat-guide.md`, a document with **no `version` field and no
`## Changelog`.** It therefore could not record a version bump for its single largest change. E36.1
correctly followed each document as it stands and normalized nothing, per its spec's explicit
instruction; the gap is structural, not a delivery defect.

E36.1's own sweep evidence records it as *"a concrete, freshly-evidenced instance of P10-GH-8's
cost."* This notice escalates that from an observation in an epic's evidence file to a decision
request, because the decision is not mine to make.

## What Was Attempted

Resolution within this chat's authority was attempted and correctly refused at every level:

1. **E35.1 (P10) declined** to retrofit a version and backdated changelog onto `chat-hierarchy.md`
   under cover of a cross-reference edit. The P10-M35 Milestone Chat **upheld that judgment** — it is
   the reason the carry-forward note is well-formed.
2. **The P11 Phase Chat recommended against folding it into M36**, reasoning recorded in the
   milestone spec's §Out of Scope: P10-GH-8 is a corpus-wide convention change, whereas M36's five
   epics are each bounded to a named defect with a named fix.
3. **HQ parked it** (Ruling 2026-08-01): *"the Phase Chat MAY propose folding it in, but HQ does not
   mandate it: M36 already carries four items and the CFO scoped it to those."*
4. **E36.1's spec forbade normalizing it** and instructed that each document be followed as it
   stands. E36.1 complied exactly and noted the cost rather than fixing it.

**Every one of those judgments was correct and none is being contested.** What has changed is only
that the condition the note itself named has now occurred, and it will occur twice more inside M36.

## The verified state, re-measured today

The carry-forward note's figures are from 2026-07-30. Re-measured on `epic/P11-M36-E36.1`:

| | 2026-07-30 (note) | 2026-08-03 (verified) |
|---|---|---|
| Documents in `governance/systems/` | 15 | **17** |
| Carrying `version` + `## Changelog` | 5 | **7** |
| Carrying neither | 10 | **10** |

**The unversioned set has not shrunk by a single document.** The corpus grew by two
(`fleet-operator.md`, `fleet-operator-brief.md`), and both were *created* with the convention. New
documents get it; existing ones never gain it. **The gap is not closing — it is calcifying**, and the
ten unversioned documents include the two most-amended and most-cited in the directory:
`chat-hierarchy.md` and `creation-chat-guide.md`.

**M36 will amend both, three more times, before it closes:**

| Epic | Document | Amendment | Versioned? |
|---|---|---|---|
| E36.1 (delivered) | `creation-chat-guide.md` | **new normative section** (~74 lines) | ❌ cannot |
| E36.3 (planned) | `creation-chat-guide.md` | Re-instantiation Ritual reconciliation — a **normative statement** | ❌ cannot |
| E36.4 (planned) | `chat-hierarchy.md` | Authority Boundary annex, byte-level frozen | ❌ cannot |

The note predicted precisely this: *"It compounds. Each amendment makes the retrofit larger and its
reconstruction less reliable."* M36 is the milestone that makes it compound fastest, because M36's
entire subject is amending the normative corpus.

## Decision Needed

**HQ's decision on one question: does the system-tier versioning convention get decided before M36
closes, and if so, where?** Three shapes, with this chat's recommendation.

**Option A — Fold into M36 (lands in E36.1, per the milestone spec).**
Not recommended. It converts a milestone whose contents the CFO **fixed at four items** into an
open-ended consistency pass, inside the one milestone whose entire value proposition is that cleanup
lands **bounded and governed**. E36.1 is currently in rework for an evidence-accuracy correction;
adding a corpus-wide convention change to it is the wrong direction for that epic specifically.

**Option B — Leave parked, unchanged.**
Acceptable, but it should be an *informed* acceptance rather than a default: it means M36 knowingly
adds three normative amendments — including one entirely new normative section — to documents that
cannot record them, in the milestone dedicated to record integrity. **If HQ chooses this, this chat
asks only that the choice be recorded**, so a future reader sees a decision rather than an oversight.

**Option C — Decide the convention once, outside M36, as a B-series bugfix. ← recommended.**
Direct precedent exists: the CFO gave **B3.1** exactly this treatment — *"small, mechanical,
self-contained, and may land before P11 opens without waiting for the milestone."* The same shape
fits here **if scoped to forward-looking adoption only**:

- Every `governance/systems/` document gains a `version` field and a `## Changelog`.
- Each currently-unversioned document is seeded at a starting version with a **first changelog row
  that says the convention was adopted and points at git for prior history.**
- **No backdated reconstruction.** That is the expensive, unreliable part, and it is what makes the
  full retrofit corpus-wide rather than mechanical. Dropping it makes the change small.

This satisfies the note's instruction to decide the convention **once for all documents rather than
per-document under a passing edit**, keeps M36's five epics bounded exactly as the CFO scoped them,
and stops the compounding. Whether it lands before or after M36 is HQ's call; **this chat does not
need it to land first.**

## Impact

**Nothing is blocked.** M36 proceeds unchanged under any of the three options, and this notice is
explicitly **not** a request to pause E36.1's rework, E36.2's sequencing, or any planning.

The cost of inaction is bounded but real and compounding: three normative amendments landing
unrecordable, in the milestone whose subject is record integrity, with the gap calcifying at a
verified rate of zero documents recovered in five weeks.

**This chat's default if HQ does not respond before M36 closes:** proceed under **Option B**, and
record the unversioned amendments explicitly in the Milestone Closure Declaration so the choice is
legible as a choice.

## Resolution

*(empty — awaiting Phase Chat routing and HQ decision)*
