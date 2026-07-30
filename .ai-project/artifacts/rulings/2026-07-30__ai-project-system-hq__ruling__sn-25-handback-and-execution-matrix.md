---
type: hq_ruling
steering_note_ref: .ai-project/artifacts/steering-notes/2026-07-30__creation-chat__steering-note__escalation-handback-and-execution-matrix.md
concern_id: SN-25
issued_by: HQ Chat (ai-project-system)
issued_to: Phase Chat (P10)
phase: P10
milestone: M35
date: 2026-07-30
status: active
blocking_resolved: true
supersedes_in_part: .ai-project/artifacts/rulings/2026-07-28__ai-project-system-hq__ruling__sn-24-m35-operator-form.md
---

# HQ Ruling — SN-25 Accepted: Handback Is a Role Obligation; Escalation Terminates at a Manual Level; Mode Is Not Authority

**Steering Note:** SN-25 (Creation Chat, 2026-07-30, CFO present) — *Autonomy must be able to
hand back* [HIGH]
**Prior rulings this ruling builds on:** SN-24 operator-form ruling and the paid-frontier
model-mapping ruling, both 2026-07-28.

SN-25 is written in role-and-rule language throughout, naming no implementations. The discipline
from the SN-24 ruling took, unprompted. Noted with appreciation, because it is what makes this
note rulable in one pass.

---

## Decision 1 — The handback rule is accepted. Its destination is the **parent**, not "a human."

**Accepted:** an autonomous execution instance that becomes **blocked** — it has encountered
something requiring judgment it cannot supply — **must be able to surface that block**, with
enough context for the receiving level to act, and **the resulting intervention is
authority-bearing**. An autonomy that cannot hand back is not autonomy; it is an unattended
process that fails silently. The handback travels as an **escalation notice** — an existing
artifact type, exercised by hand twice in M34. No new artifact type and no new authority model.

**HQ amends one thing in the framing.** SN-25 states the rule twice, in two different shapes: as
*"must be able to summon a human"* (the CFO's *"I get my chat opened ready for me to
intervene"*) and as *"escalation travels exactly one level, to the immediate parent."* Those are
not the same rule, and shipping both into M35 unreconciled would put a contradiction into a
normative record.

**The normative rule is the parent one.** A blocked instance hands back **to its immediate
parent** — not to "a human," which it has no way to identify and no standing to select. The
human is reached because the chain **terminates at a manual level by construction**: Creation
and HQ are manual-only, permanently (SN-22), so every escalation chain that keeps escalating
arrives at a human in a bounded number of hops. **Termination is guaranteed, and it is
guaranteed by SN-22 rather than by hope.** That is worth stating in M35, because it is the
property that makes the handback rule well-founded rather than aspirational.

The CFO's *"my chat opens ready for me to intervene"* is then correctly placed: it is the
**surface behavior** of a level that is manual receiving an escalation — how that surfacing is
presented is coordination, and coordination is P11's. Governance's part is that the notice must
be emitted, must reach the parent, and must carry enough context to act on.

---

## Decision 2 — The one-level rule is recorded normatively. It does **not** close P9-GH-1.

**Recorded:** an escalation notice targets the issuing instance's **immediate parent and nowhere
else**. The parent then decides the next step's direction — **resolve and return** to the child,
or **issue its own notice** one level up. No instance names a target above its parent; no level
is skipped. The child's job is to describe the blocker fully — nature, what was attempted, what
it could not resolve; **judgment about the problem stays nearest the problem, judgment about
where it goes stays with the level holding authority over it.**

HQ affirms the CFO's rejection of instance-judged routing, and adds the reason in its sharpest
form: instance-judged routing lets **a child choose its own judge.** An Epic routing straight to
HQ steps around the Milestone Chat's Stage-2 authority, and the parent may never learn its own
epic is blocked. M34 is the worked counter-example — the Milestone Chat could not open, its
parent Phase Chat diagnosed and issued **its own** notice to HQ, and HQ ruled. Two hops, no
level bypassed, and the reach was *reached* rather than guessed at from below.

**Stated so it cannot be misread: this does not close P9-GH-1.** SN-25 correctly identifies the
one-level rule as protecting the same authority class, and it is genuinely adjacent protection —
but P9-GH-1 is a **merge-authorization** hole in the Milestone and Phase starter templates, and
recording an escalation-routing rule patches no template. P9-GH-1 remains open, carried forward,
and unowned. A future reader must not find "escalation travels one level" and conclude the hole
was closed.

**A live instance of the adjacent question, flagged to HQ and answered here.** The 2026-07-29
M34 escalation was resolved by **direct CFO instruction to the Phase Chat** rather than a round
trip to HQ, and the Phase Chat flagged that as a real routing choice worth HQ's attention rather
than normalizing it silently. That was the right call to flag, and the resolution was correct:
**the CFO is not a level in the chain.** The chain is Epic → Milestone → Phase → HQ → Creation;
the CFO is the authority all of it serves and may answer at any point without that being a
bypass. The one-level rule constrains **instances**, not the human whose keys the gates exist to
hold. The obligation the CFO's direct answer creates is **recording**: the decision must land
where the level that would otherwise have ruled can see it. That happened here — the escalation
notice carries the resolution, the phase spec carries the amendment at v1.2.0. That is the
standard; the discipline of flagging it rather than absorbing it is exactly right and should
continue.

---

## Decision 3 — Creation Chat awareness is visibility only

**Recorded:** the Creation Chat is aware of all escalation notices wherever they arise. This is
a **retrieval** property over committed artifacts — a re-instantiated Creation Chat reads the
directory — never a subscription, and never a seat. **Seed Rule 3 stands: the Creation Chat
holds no governance authority.** Awareness must never make it a decision point or a resolution
path.

**One addition, because a right with no outlet decays into an improvised one.** Awareness does
have a legitimate channel: what the Creation Chat may do with what it sees is **issue a steering
note to HQ** — direction-setting, not resolution. That is how SN-23, SN-24 and SN-25 themselves
arrived. Naming the outlet explicitly is what keeps awareness from drifting into "the Creation
Chat unblocked it," which is the failure SN-25 is right to fear.

---

## Decision 4 — The execution matrix is ratified. **Mode is not authority.**

**Ratified as written**, and it **supersedes SN-23 Ratified Decision #2 on the Execution Mode
axis only**. The locality half stands, with Milestone under evaluation per Decision 5. Recording
the supersession explicitly makes this a decision rather than drift.

| Level | Execution Mode | Inference locality |
|---|---|---|
| Creation | Manual only (permanent, SN-22) | Remote |
| HQ | Manual only (permanent, SN-22) | Remote |
| Phase | Agentic or manual | Remote |
| Milestone | Agentic or manual | Remote — **local under evaluation** |
| Epic | Agentic or manual | Local or remote (in force, E34.3) |

SN-25 is right that at Phase and Milestone **the ask is dispatch, not permission** — E31.1
already made Execution Mode normative at those levels and recorded that no dispatch mechanism
consumes the declaration. SN-23 narrowed it for P10; this restores E31.1's baseline.

**HQ adds the constraint that makes the restoration safe: mode is not authority.**

Restoring agentic mode at Milestone says an instance at that level **may run unattended**. It
does **not** widen what that instance may *authorize*. Milestone is where **Stage-2 accept
authority** lives — the level whose errors propagate into merges, and the reason row P4 reads
paid frontier. Nothing in SN-25 asks to hand accept-and-merge authority to an unattended
process, and nothing in this ratification grants it. **Until ruled otherwise, authority-bearing
acts — Stage-2 acceptance and merge authorization — still require the human's key, whatever mode
the instance is running in.** This is the direct application of SN-25's own retained principle,
that per-level **gates** remain a requirement and stay revisitable: mode is *what may run*, gates
are *what may be decided without a key*. Conflating them would let a mode restoration silently
widen authority, which is precisely the class of drift the framework exists to prevent.

Also carried unchanged: **technical possibility is not sufficient reason.** The matrix is a
bounded position, not a removal of limits.

---

## Decision 5 — The Milestone × local evaluation is directed, with a concrete bar

**The cell is neither opened nor closed. It opens or closes on evidence** — run-first, per
SN-23 #4.

**What must be measured — review quality, not throughput or cost.** Affirmed exactly as SN-25
states it. Row P4's reason for paid frontier is not price; it is that Milestone holds Stage-2
accept authority and its errors propagate into merges. Evidence that a local model is fast or
cheap at Milestone answers a question nobody asked.

**The sufficiency bar, stated concretely so the evaluation cannot end in an argument about what
counts.** This repository has a rare asset: a documented history of review misses and catches
with known ground truth. The evaluation must **back-test a local-model Stage-2 review against
defects whose outcome is already known**, at minimum:

- **M33's decomposition gap** — the "each proving-pair project" bar with no home in the 3-epic
  split, caught only at closure (E33.4).
- **E33.2 Run A's false-positive completion** — exit 0, zero work.
- **E33.4's false-negative** — exit 2, complete and green work.
- **M34's footboard dirty-entry miscount** — caught and corrected in-flight.
- **P10-GH-6** — the starter-lint false positive on real milestones.

A local model's review is a candidate for the cell if it **catches what was caught and flags what
was missed**, on material it has not been told the answer to. This bar is cheap, needs no new
capability, is ungameable by speed, and produces a defensible yes *or* no. A pass is not by
itself sufficient to move row P4 — it is the necessary evidence that makes the question
answerable at all.

**On harvesting `Getawayinsured2023`.** Yes, as an evidence source — and HQ records something
that must not be "fixed" by a well-meaning future reader: that project's `.ai-project.yml`
pointing `phase` and `milestone` at a local model **is not a policy violation.** The yml-spec's
own defaults-provenance note says adopting repositories may override any value per their own
evidence, and `model-routing-policy.md` binds this repository. It is a **legitimate override and
a live natural experiment.** Two limits: its evidence is *that project's* until corroborated,
and harvesting it must not retroactively convert an override into a fleet standard.

**May the result amend row P4 independently of its unfired trigger?** **Yes.** A revisit trigger
is a **prompt to revisit, not a precondition for revisiting.** The Change-discipline rule binds
rows to *new cited evidence* — it does not require that the evidence arrive through a
pre-registered door. The precedent is two days old and in this same file: the 2026-07-28 ruling
**added** a trigger that did not previously exist, which is only coherent if the trigger list is
non-exhaustive. So a completed evaluation meeting the bar above is a valid basis to amend P4,
and **P4 does not wait on P9-GH-3** (within-session task segmentation), which remains carried
forward and unowned. Stated rather than assumed, as SN-25 asked.

---

## Decision 6 — M35 is **re-scoped once when it opens**, not amended a second time

SN-25's observation is adopted. M35 has already been amended once (phase spec **v1.1.0**, per
the SN-24 ruling) and has still not opened. Patching an unopened milestone a second time
produces a spec that is a sediment of amendments rather than a statement of current
understanding.

**Directed:** when the Phase Chat opens M35, it **re-scopes M35 in one pass from current
understanding**, folding in SN-24 *and* SN-25 together. **This supersedes, in mechanism only, the
SN-24 ruling's instruction that the amendment land before M35 planning opens.** That
instruction's *intent* — M35 must never be planned from a superseded spec — is better served by
a single clean re-scope than by a second patch, and is hereby discharged that way. The re-scope
is recorded as a normal amendment with history and a version bump; it is not a silent rewrite.

**One cheap safety step now, because the gap between today and M35's opening is where a stale
read happens.** The Phase Chat adds a short **supersession marker** to §P10.3 and §Milestones→M35
— pointing at SN-24, SN-25, and the two rulings, and stating the text is pending re-scope. A
pointer, not a rewrite; minutes of work, and it removes the only real risk of leaving the full
job until M35 opens.

**What SN-25 adds to M35's content**, in role-level language: the operator role **includes
handing back on a block**; the handback is **authority-bearing**; **escalation travels exactly
one level** and terminates at a manual level by construction; **Creation Chat awareness is
visibility only**.

---

## Decision 7 — Block detection is the load-bearing risk. Recorded as **P10-GH-7**.

SN-25 is right that this is the dependency the whole idea rests on, and right to call it risk
rather than scope. **You cannot escalate on a block you cannot detect**, and detection is
measured broken in both directions:

**P10-GH-7 — the completion signal is untrustworthy two-sided, and the lane that would fix it
has never run.** E33.2 Run A returned exit 0 having done zero work (the validation command would
have passed on the unchanged repo); E33.4 returned exit 2 having produced complete, green work.
Corroborated across two projects on this stack: **the exit code is not a completion signal.**
Compounding it, **G11 stands — zero captured QA-role runs.** `epic_qa` has a config key and a
policy row and no evidence behind it, so the capability that would answer *"is this instance
stuck, finished, or confidently wrong"* is the one never exercised. Any handback mechanism built
over this signal yields **constant false escalations** — the human becomes the bottleneck again,
worse than before — **or silent no-ops that read as success.** Severity: **High.** Owner:
unassigned; a prerequisite for the P11 mechanism, not for M35's record. Carries forward to the
P10 closure declaration alongside P10-GH-1 … P10-GH-6.

The rule can be recorded now precisely because recording it costs nothing and building on it
costs everything — which is Decision 8.

---

## Decision 8 — Nothing here is built in P10. Confirmed.

**M35 records the rules; P11 builds the mechanisms.** No block detector, no mode switch, no
runner→chat channel, no dispatch wiring for Phase/Milestone agentic declarations, and no
push-notification work (deferred under the SN-24 ruling, Decision 6) is scoped in P10.

The domain split SN-25 states is affirmed: **executing larger units and being invocable from a
manual chat is EXECUTION** (Local Agent Runner); **deciding when to run, detecting the block,
switching mode and surfacing the intervention is COORDINATION** (Drivr, P11); **the rule that
autonomy must hand back, that escalation travels one level, and that the human's intervention is
authority-bearing is GOVERNANCE** (this repo). SN-23 Ratified Decision #1 — no third spin-off in
P10 — stands unamended for the third consecutive ruling.

---

## Disposition

**SN-25 — accepted, amended in framing by Decision 1, triaged closed at HQ.** All eight requested
actions are answered: #1 ruled with the destination corrected (Decision 1), #2 recorded with
P9-GH-1 held explicitly open (Decision 2), #3 recorded with its outlet named (Decision 3), #4
ratified with *mode is not authority* attached (Decision 4), #5 directed with a concrete
back-test bar and the trigger question answered (Decision 5), #6 directed as a single re-scope
plus an interim marker (Decision 6), #7 registered as P10-GH-7 (Decision 7), #8 confirmed
(Decision 8).

**The Phase Chat owes two things:** the supersession marker on §P10.3 / §Milestones→M35 now, and
the single M35 re-scope when M35 opens. Nothing else in P10 is gated on this ruling.
