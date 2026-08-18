---
project: ai-project-system
phase: P11
milestone: null
type: note
status: active
issuer_chat: HQ Chat (ai-project-system)
issued_to: Phase Chat (P11) → P11 Closure Declaration
last_updated: 2026-08-17
severity: medium
---

# Carry-Forward Note — P11-GH-3: phase closure has no pre-merge completion artifact, where every level below it does

**Origin: the CFO, 2026-08-17**, reviewing P11's delivery and expecting the pattern that holds at
every other level. **The expectation was correct and the framework does not meet it.**

**Recorded, not fixed. P11's own closure proceeds under §5C exactly as written** — the P11 Phase Chat
followed the procedure correctly and this note is not a finding against it.

---

## The pattern, and where it breaks

| Level | Closure artifact | Timing | Mandated by |
|---|---|---|---|
| **Epic** | Delivery Notice | **before** review — *"a prerequisite for review and closure; no Epic may proceed to review or closure without one"* | PSG §12 |
| **Milestone** | Milestone Closure Declaration | **before** consolidation — its own format line reads *"Status: COMPLETE (awaiting consolidation)"* | AOG §"Milestone Closure Declaration Format" (*"HQ Chat MUST use this structured format"*) |
| **Phase** | — **nothing** — | — | — |
| *(Phase)* | *Phase-Closure Declaration* | **Step 9, after merge and tag** — *"the record post-dates the closure commit it describes"* | PSG §5C |

**At Epic and Milestone, a closure artifact exists before the parent's gate and is what the parent
reviews. At Phase, the parent's gate (§5C Step 6, "Delivery Reviewed") has no closure artifact to
review at all.**

§5C **Step 2** says *"'Phase P<id> complete' declared with a verification checklist and phase
summary"* — and **names no artifact, no path, and no template** to record that declaration in. So the
verification checklist and phase summary land wherever the Phase Chat puts them, which for P11 was a
**PR comment**.

---

## What this is NOT

**It is not that P11's Phase-Closure Declaration is missing or late.** Step 9's placement is correct
and should not move: the declaration records the **merge commit, the tag, and `master`'s head at
closure**, none of which exist before the merge. A declaration written earlier could not contain its
own defining fields. **Moving Step 9 earlier would break what it records.**

The gap is the *absence of a second artifact*, not the placement of the existing one.

---

## Why it matters more than it looks

**The phase gate is the highest-stakes acceptance in the framework** — it is the one that puts work on
`master`, bumps the version, and cuts a tag. It is the only gate in the hierarchy where the reviewing
level receives no governed artifact.

**Three consequences, all observed in P11:**

1. **The review package is not durable.** PR #173's comment carried P11's verification checklist,
   milestone table and phase summary. A PR comment is not in `docs/`, is not versioned, is not
   discoverable from the repository, and is not what any future reader of the phase record will find.
2. **It makes the human the transport.** The CFO raised this independently on 2026-08-17 as
   copy/paste friction between chats. This is its sharpest instance: HQ's acceptance at Step 6 depends
   on content that exists only in a PR comment, so it reaches HQ because a person carried it.
3. **§11.6 default-accept compounds it.** A clean phase delivery is accepted by silence, producing no
   Review Decision either. So on the happy path the phase gate can produce **no artifact on either
   side** — nothing reviewed, nothing recording the acceptance.

---

## Severity: Medium

Not High: nothing was lost, P11's evidence is complete and correct, and the procedure was followed.
Not Low: it is structural, it recurs at every phase closure, and it sits at the framework's most
consequential gate. **Eleven phases have closed this way**, which is also the reason it has gone
unnoticed — the Phase Chat has always been present to answer for its own delivery.

---

## Candidate direction — one, and it is the obvious one

**A Phase Completion Declaration at §5C Step 2**, mirroring the Milestone Closure Declaration's shape
and timing:

- issued when the phase is declared complete, **before** the consolidation PR;
- carrying the verification checklist, the milestone table and the phase summary that currently live
  in a PR comment;
- marked `COMPLETE (awaiting consolidation)`, exactly as the Milestone declaration is;
- **it is what HQ reviews at Step 6.**

Step 9's Phase-Closure Declaration stays exactly where it is and keeps its job — recording the merge
commit, tag and head **after** they exist. The two are different artifacts doing different jobs, which
is precisely the arrangement Milestone level already has and Phase level lacks.

**Not placed here.** It amends PSG §5C and AOG, needs a template, and belongs in a scoped epic — the
same reasoning that kept P10-GH-8 out of M36. **P12's opening should carry it.**

---

## A note on how this was found

**The CFO found it by expecting consistency and checking whether the framework delivered it.** No
measurement, no failure, no escalation — an argument from symmetry against the corpus. Recorded
because it is the first defect this phase that no amount of verification discipline would have
surfaced: every level was internally correct, and the gap is only visible when the three are laid
side by side.
