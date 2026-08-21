---
type: hq_ruling
concern_id: M41 duplicated Stage-2 authority; PSG §11.6 default-accept under two addressees
hq_opener_ref: .ai-project/artifacts/hq-openers/2026-08-19__hq-chat-opener.md
issued_by: HQ Chat (ai-project-system)
issued_to: the P12-M41 Milestone Chat; the P12 Phase Chat; Layer-8/CFO (mandatory diff reviewer, PSG §11.6.1)
phase: P12
date: 2026-08-21
status: active
blocking_resolved: false
---

# HQ Ruling — Accept-by-Silence Is SUSPENDED for M41 While Its Stage-2 Authority May Be Duplicated

**Prerequisite verification (P9-M31-E31.3):** harness `claude-opus-5` vs `models.hq: remote:claude-opus-5` — **match.**

**Narrow, temporary, and fail-closed.** It amends nothing. It suspends one mechanism for one milestone
while a known condition holds, and it lapses when the CFO resolves that condition.

---

## Decision 1 — For M41 only: acceptance must be explicit. Silence accepts nothing

**While more than one session may hold M41's Stage-2 authority, `PSG §11.6` default-accept is
SUSPENDED for M41.** An epic delivery under M41 is accepted only by an **explicit, committed**
acceptance. **Silence is not acceptance and must not be read as one.**

**Cost: one line per epic delivery.** It does not reinstate the Review Decision artifact for clean
deliveries, and it changes §11.6 nowhere else in the phase or the framework.

**Lapses automatically** when the CFO records which session holds M41's Stage-2, or when the
condition otherwise ceases. **No further HQ ruling is needed to end it.**

---

## Decision 2 — Why this is §11.6's own stated failure mode rather than a new rule

**SN-31 Decision 3 — the CFO's, ratified — says what silence cannot carry:**

> Silence as the sole carrier **cannot distinguish *"reviewed and clean"* from *"never looked"* from
> *"the session died."***

**Two Stage-2 holders make that ambiguity concrete rather than theoretical.** An epic could be
accepted by one chat that the other never hears from, and **the absence of a second chat is
indistinguishable from the second chat's assent** — because in both cases nothing is said.

**And default-accept produces no artifact on the happy path**, which is what makes this
unrecoverable rather than merely wrong. **After the fact there is nothing to inspect**: no record of
which chat accepted, whether the other saw the delivery, or whether one existed. **The evidence that
would settle it is the evidence the mechanism is designed not to create.**

**So the window closes at the first epic delivery, not at some later review.** Zero
`epic/P12-M41-*` branches exist as of this ruling. **Today it costs one line; tomorrow it costs an
epic's acceptance record permanently.**

---

## Decision 3 — The condition is verified, not asserted

**Raised by the M41 Milestone Chat; the commit-graph evidence re-measured by HQ on `origin` before
ruling.**

**Two commits touching M41's epic artifacts are not the M41 chat's** — `b735182` and `def8ff1`,
**both at `2026-08-20T10:35:12-06:00`**. They sit inside a **5 h 27 m gap** in that chat's own
activity, between `6de2d58` (09:17:29) and `993d906` (14:44:57). **Confirmed by HQ against
`origin/milestone/M41`.**

**`b735182`'s subject line is the finding, not an illustration of it:**

> *"v1.0.3 — the R6 citation resolves; **correcting my own rotted claim**."*

**The claim it calls "my own" was written by the other session.** A second session read the
artifact, correctly saw that its premise had moved, corrected it well, and described the correction
in the first person. **The work was right.** Nothing in git marks the boundary.

**This is the Phase Chat's agreeing-fork finding instantiated in the artifacts of the chat that
helped surface it** — *a fork that contradicts is detectable at merge; a fork that agrees is
invisible, and it silently doubles the write surface for a role.*

**How it was detected, recorded because the mechanism matters more than the instance: it was not
detected by a check.** It took a commit message written in the first person about someone else's
sentence, plus one participant retaining a transcript long enough to say *"I didn't write that."*
**That is a witness, not a mechanism.** Phrased impersonally, or with one more roster turnover, the
boundary would be unrecoverable and the record would read as one continuous author.

**Corroboration HQ found independently, before the claim was made:** the pruned worktree named
**`wt-m411`**. That name is what git produces when `wt-m41` is already taken — **a second session
colliding on the same worktree name for the same milestone.**

---

## Decision 5 — What the suspension buys, and what it does not. Stated so it is not over-read

**Raised by the M41 Milestone Chat on adopting it, and it is a correction to how Decision 1 could be
read.** Recorded before merge rather than after.

**The suspension does not prevent duplicate acceptance. It converts an UNDETECTABLE duplication into
a DETECTABLE one** — and that, not prevention, is the whole of its value.

| Under §11.6 default-accept | Under the suspension |
|---|---|
| Two silences are **indistinguishable from one silence** | Two explicit acceptances are **two commits** |
| The duplication leaves **no trace** | Visible, diffable, **attributable** |

**The residual, named so it is not discovered later:** if one session accepts a delivery explicitly
and the other never sees it — **these rosters have already expired on each other once** — the second
may accept it again. **That is now a fault caught at the next read of the branch, rather than an
unrecoverable one.**

**So the suspension makes M41's acceptance record auditable. It does not make it single-authored.**
Only the CFO naming the session does that, **which is exactly why this lapses on his word.**

**And it sharpens Decision 2's argument rather than weakening it.** Default-accept produces no
artifact, so the evidence that would settle a duplicate acceptance is the evidence the mechanism is
designed not to create. **The suspension's real function is to start creating that evidence** —
which is precisely why it must be in place *before* the first delivery and not after.

**Adopted form, from the M41 chat, and HQ endorses it as the shape of compliance:** an acceptance
names the delivery **and the accepting session's UUID**, so that **the acceptance carries an author
rather than a role.** A role is what is duplicated; an author is not.

---

## Decision 4 — HQ does not resolve which session holds M41, and says why explicitly

**That is the CFO's, and it stays his.** HQ rules the acceptance semantics; it does not pick a
survivor.

**Both sessions were given the role and both behaved correctly. Authenticity is not the axis** —
duplicated write surface is. **Resolution by attrition is worse here than elsewhere**, because the
fork's work was good: **no defect marks where it acted**, so an after-the-fact reader cannot find the
seam by looking for damage.

**The M41 chat reachable to HQ is a routing fact, not a ruling**, and this ruling does not make it
one.

---

## Disposition

**In force for M41 on merge. Lapses on the CFO's resolution without further ruling.**

**Adopted by the M41 Milestone Chat effective on notification, ahead of this merge**, with its worktree recreated first (`wt-m41-b` at its own scratchpad, shared checkout untouched). **A stopgap that waits for its own PR is not a stopgap** — but the record is still the record, which is why it is ruled here and not only messaged.

**Escalation stage 1** — the Stage-1 duplication cost duplicated authorship, which merged cleanly.
**Stage 2 is where M41 holds accept-by-silence and requests merges**, and that is a different order of
consequence. The M41 chat flagged it at the cheapest possible moment and HQ is acting at that moment.

**PSG §11.6.1:** HQ-authored, no chat-level reviewer. The CFO is the mandatory diff reviewer.
