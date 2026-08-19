---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-08-18T00:00:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-31
    severity: high
    title: P12 spine set — completion of the workflow vision on governance + the Drivr MVP; the system's default on missing evidence is PROCEED, confirmed across four verified instances
  - id: SN-32
    severity: medium
    title: The 3-attempt rework limit reaches one of eight starter surfaces and none of the templates — same shape as P9-GH-1, different rule, unfiled
  - id: SN-33
    severity: medium
    title: SN-30 (external assessment, issue #192) was issued 2026-08-11 and appears in no ruling, spec or declaration; P11 closed without it
decisions:
  - "P12's spine, in the CFO's words: completing the CFO's vision of the workflow, using the governance and the MVP of the harness (Drivr). A completion phase, not a redesign."
  - "The three verified execution-tier defects are P12 scope, under a sequencing constraint rather than a date: they land BEFORE the first real agentic integration, not after."
  - "Accept-by-silence is tweaked, not retired. The low-ceremony property is kept; silence as the sole carrier is replaced."
  - "The PARENT performs the merge, not the child. Reverses the CFO's own interview description and structurally closes the P9-GH-1 / P10-GH-9 bypass class."
  - "Exhausted rework flips the receiving parent chat to manual. Opt-out default, switch modelled on cfo_review_gate. Drivr performs the flip and records it, so the committed starter remains the source of truth."
  - "Consolidating the eight starter-shaped surfaces is P12 scope."
  - "Keep unchanged: per-instance Execution Mode in the committed starter; 'Mode is not authority'; PSG §11.6.1 (the CFO is the mandatory diff reviewer)."
  - "The rework limit is 3 attempts maximum, movable only by a written reason. This confirms the built rule rather than amending it."
references:
  - "https://github.com/panchew/ai-project-system/issues/192 — external assessment, routed by SN-30, still unactioned."
  - ".ai-project/artifacts/progress-digests/2026-08-17__hq__progress-digest.md — the P12 scoping handoff this note answers."
---

# Steering Note — Creation Chat to HQ Chat

## Purpose

The 2026-08-17 Progress Digest asked the Creation Chat for one thing: **P12's spine.** This note
carries it, together with the evidence the spine rests on and the decisions ratified while setting
it.

It also files two concerns found while doing the work, and re-raises one that HQ has not acted on.

---

## Concerns for HQ Triage

### SN-31 — P12 spine, and the finding underneath it [HIGH]

**The spine, in the CFO's words:** *completing what I think is my vision of the workflow using the
governance and the MVP of the harness (Drivr).*

**How it was set, because the method matters.** The CFO described his intended workflow to a
separate chat held **deliberately ignorant** of this repository, Drivr, and every name in either.
That session produced a Mermaid sequence diagram, a hop table, and a list of unresolved questions
quoted verbatim. Only then was the description compared against what is built. The ignorance was
the point: an interviewer who knows the implementation resolves every ambiguity toward it, and the
comparison becomes a mirror.

**The comparison result: the described workflow and the built system agree substantially.** Five
levels, Stage 1 / Stage 2 epic-set authoring, one-level escalation, per-level acceptance gates,
default-accept, phase-scoped artifact lifetimes, agentic confined to Phase/Milestone/Epic — all
matched. This is why the spine is **completion, not redesign**, and HQ should scope it that way.

**What did not match, and is now decided, is recorded in Decisions Already Made below.**

#### The finding: the system's default on missing evidence is PROCEED

Four instances, each independently verified on master at `bd198c2`, 2026-08-18:

| # | Where | Behaviour on missing evidence |
|---|---|---|
| 1 | `bin/ai-project-orchestrator:397` | Docker unavailable → prints a warning and runs the agent's command **unsandboxed on the host**, via `subprocess.run(..., shell=True)`. Isolation fails **open**. |
| 2 | `bin/ai-project-orchestrator:472` | On success, runs `git add .` — stages the entire tree, not the epic's files. |
| 3 | `bin/ai-project-git-merge:269-281` | PR approval fails → prints `Warning ... Proceeding to merge`, then attempts standard merge → **`--admin` override** → auto-merge. **A test at :452 asserts the admin override succeeds against a protected branch.** |
| 4 | M39's completion judgment | On absent effect evidence it returns `undetermined`, and on strict scoring **loses to a degenerate baseline that always answers "completed."** |

**These are not four unrelated bugs. They are one disposition**: when the evidence that should
gate an action is absent, the action proceeds. **The CFO confirmed this reading explicitly**; it is
not an inference this chat is advancing alone.

**Why it gates everything else.** Agentic mode is *defined* by no human being present to notice an
absence. A system that proceeds on missing evidence is therefore precisely as safe as its
supervision — which under agentic operation is zero. This is the technical content of the CFO's own
statement that he cannot move forward without at least one level agentic, and cannot go agentic
without tightening the foundations first.

**Also on the record, and load-bearing for how P12 is scoped:** *agentic mode has never been
integrated in any project.* The CFO's words — *"just doing some testing and measuring does not
count as being using it already."* Eleven phases have built machinery for a mode that has not yet
carried real work. P12 is not more governance; it is the first time this governance is used in
anger.

**Required action:** open P12 on this spine and treat the four fail-open behaviours as its spine
evidence, not as a defect backlog appended to it.

---

### SN-32 — The rework limit reaches one surface of eight [MEDIUM]

Measured 2026-08-18 across all eight starter-shaped surfaces plus PSG:

- `governance/systems/milestone-execution-chat-starter.md` — **8** occurrences of "rework",
  **2** of the 3-attempt rule. Line 329: *"Maximum 3 attempts... Silent fourth attempts are a
  governance violation."*
- `governance/templates/milestone-execution-chat-starter.md` — **0** occurrences. **This is the
  file a Milestone Chat is instantiated from.**
- The other six starter surfaces — **0**.
- `PROJECT-SYSTEM-GUIDELINES.md` — **0**. The rule is not in the normative tier at all.

**So the only mechanism bounding rework loops is not delivered to the chat that must enforce it.**

**This is `P9-GH-1`'s shape exactly** — a rule present in one starter surface and absent from the
rest, invisible because no surface is authoritative — applied to a different rule, three phases
later, and still open. `P9-GH-1` was closed on 2026-08-17 by sweeping all eight surfaces (E40.5).
That sweep fixed one rule; it did not fix the fragmentation that produced it.

**Required action:** file this as a gap record in HQ's own numbering, and place the eight-surface
consolidation in P12 per the CFO's decision below. Filing it separately from the consolidation work
matters: the consolidation is the fix, but the defect must exist as a record in case the
consolidation is deferred.

---

### SN-33 — SN-30 was never actioned, and P11 closed without it [MEDIUM]

SN-30 (2026-08-11) routed the external assessment at issue #192 into governance with four required
HQ actions: place Rec 1 (build checks for the four observed defects), place Rec 2 (promote G1 and
G2 into the core documents), record Recs 3–5 as deferred with reasoning, and decide whether the AOG
section-numbering fix clears SN-28's hotfix boundary.

**A search of the corpus on 2026-08-18 finds `SN-30` in exactly one file: its own.** No ruling, no
milestone spec, no closure declaration. The 2026-08-17 Progress Digest does not mention it. P11
closed six days after it was filed.

The AOG section-numbering defect it reported is still live: two sections both titled
"Error Handling" (`## 13.` at L701, `## 14.` at L861), in the order `1, 1A, 2–9, 13, 14, 10, 11,
12, 13, 14, 16, 15`. Ten phases without detection.

**This is a delivery failure in the Steering Note path itself**, and it is worth HQ noticing as
such: a note reached its target and left no mark. If the mechanism that carries concerns upward can
drop one silently, that is the same fail-open disposition as SN-31, one tier up — in governance
rather than in code.

**Required action:** action SN-30's four items, or record them as deliberately deferred with
reasoning. Either is acceptable; silence is not.

---

## Decisions Already Made

Ratified by the CFO in the Creation Chat, 2026-08-18. **These are not open for HQ to re-decide** —
they are inputs to P12's scoping.

1. **P12's spine** is completion of the workflow vision on governance plus the Drivr MVP.

2. **The three execution-tier defects (SN-31 rows 1–3) are P12 scope**, under a **sequencing
   constraint rather than a date**: they land **before the first real agentic integration**, not
   after. Exposure today is genuinely low precisely because nothing runs agentically; all three go
   live simultaneously the moment one project does.

3. **Accept-by-silence is tweaked, not retired.** Its cheapness is worth keeping — it is what stops
   a parent producing an artifact on every happy path, and it keeps every artifact in the corpus a
   real decision. What is replaced is **silence as the sole carrier**, which cannot distinguish
   *"reviewed and clean"* from *"never looked"* from *"the session died"*. Note that §11.6 already
   makes *"the merge plus the in-chat acknowledgment"* the acceptance record, so the gap is narrower
   than "no record": the merge proves **something was accepted**, not that **a review happened**.

4. **The parent performs the merge, not the child.** This reverses the CFO's own interview
   description on review of the evidence. Its value is structural: `P9-GH-1` and `P10-GH-9` both
   describe a child taking merge authorization directly and bypassing its parent's Stage-2 review,
   and E40.5 patched that **behaviourally** by teaching eight starter surfaces to push back. **If
   the parent merges, the child never holds the authorization at all** — the bypass class becomes
   unavailable rather than merely discouraged, and the E40.5 guard demotes to a backstop.
   *Known consequence:* `governance/templates/merge-authorization.md` is addressed to the child
   (`epic` field: *"The Epic whose branch is authorized to merge"*) and becomes the parent's own
   record instead. One template edit.

5. **Exhausted rework flips the receiving parent chat to manual — opt-out default.** The CFO raised
   this himself; it is **the first fail-closed default in the system**, and the direct counterweight
   to SN-31.
   *Known conflict and its resolution:* `chat-hierarchy.md` holds that *"a reader determines any
   instance's Execution Mode by reading its committed starter file."* A runtime flip would leave the
   committed file saying `agentic` while the instance runs manual, silently breaking the invariant
   that makes mode per-instance rather than a project-wide switch. **Resolution: Drivr performs the
   flip and records it**, so the committed record remains the source of truth rather than being
   contradicted by it. This is pure coordination with no inference, squarely within Drivr's charter,
   and M38 already built fleet-state transitions as append-only recorded actions. The opt-out switch
   itself should follow `cfo_review_gate: enabled` in `.ai-project.yml` — the existing precedent for
   a governance gate that is on by default and disabled deliberately.

6. **Consolidating the eight starter-shaped surfaces is P12 scope** (see SN-32).

7. **Unchanged, confirmed deliberately:** per-instance Execution Mode declared in the committed
   starter; **"Mode is not authority"**; **PSG §11.6.1** (the CFO is the mandatory diff reviewer for
   HQ-authored deliveries, and authorization is not review).
   *Note on "Mode is not authority":* under the CFO's stated near-term posture — Epic agentic,
   every level above manual — this rule never fires, because the only agentic level accepts nothing.
   It becomes load-bearing the moment the agentic bar moves up, which is the stated goal. It is kept
   for that reason, not because it currently binds.

8. **The rework limit is 3 attempts maximum, movable only by a written reason.** This **confirms**
   the built rule rather than amending it.

---

## Carry-Over Open Items

1. **Phase and Milestone agentic dispatch do not exist.** `chat-hierarchy.md` states that no
   dispatch mechanism consumes a Phase or Milestone agentic declaration; the path is implemented at
   **Epic only**. The CFO is aware and places this in the roadmap. Recorded here so P12 scoping does
   not assume two hops that are absent.

2. **No handoff artifact exists for context exhaustion.** "Handoff" appears as prose in ten
   documents; there is no template and no artifact type. The CFO marks this *to build*. Ideally
   semi-automated, supported by harness context tracking — which is Drivr's side of the boundary.

3. **`P10-GH-7` is the correct home for the missing-Delivery-Notice branch.** The CFO independently
   arrived at this gap when asked what happens if a child's delivery never arrives, and left it
   unresolved. It is already filed, severity High, open since M35. Marked *to address*.

4. **The artifact-type inventory (Digest Open Decision 5) is unresolved and this note is adjacent to
   it.** The interview instrument used to set this spine was deliberately **not** minted as a
   governance artifact type, because the digest indicts HQ for minting `field-evidence` without a
   template or an authorizing ruling. If the instrument proves reusable it should be templated
   properly, through a ruling. It is not being smuggled in.

5. **Digest Open Decisions 3, 4 and 6 are untouched by this note** — the four returned proposals,
   the `P11-GH-2` sibling pattern, and `model-routing-policy.md` row P4. The CFO has not ruled on
   them and this note does not.

6. **First external adopter, and they are working in Spanish.** As of 2026-08-18 a person other
   than the CFO has begun using this governance system for their own project, in Spanish. This is
   the first recorded adoption outside the CFO's own fleet — notable on its own, given that the
   external assessment at issue #192 flagged public traction as unproven and adoption friction as
   brutal. It raises **i18n** as a live question the framework has never faced: the corpus is
   English-only, and every artifact, template, starter and normative rule is written in it. The CFO
   raised this as *"one tiny detail"* and it is recorded at that weight — **as an observation, not a
   scoped concern**. No i18n work is proposed here. What is proposed is that the fact be on the
   record before P12 is scoped, because a first outside user is evidence of a kind this project has
   never had.

7. **The Drivr UX vision has not been captured.** The CFO has stated he has a vision for Drivr's
   UX that he has not yet described, and intends to. Drivr is the MVP half of P12's spine, so this
   is a known gap in the spine's own definition — recorded so it is not mistaken for a settled area.

8. **A per-level model and mode mapping is planned, not instructed.** The CFO has a target mapping
   spanning multiple providers and harnesses. It is explicitly *"a plan, not an indication that you
   have to configure everything right now"*, intended as a template for new projects, and **to be
   assessed and measured before it is adopted**. No configuration change is authorized by this note.

---

## Next Action

### HOLD — P12 MUST NOT BE OPENED ON THIS NOTE ALONE

**The CFO has stated that there is a further input P12 cannot be entered without, and that he has
not yet recalled it.** This note is therefore **complete as a record and incomplete as an
authorization**. Everything in it stands — the spine, the decisions, the three concerns — and none
of it is retracted by this hold.

**HQ may act on items 3, 4 and 5 below immediately.** Items 1 and 2 wait for the CFO to release the
hold in writing.

This is recorded in the artifact rather than left in chat deliberately: SN-33 below documents a
Steering Note that reached its target and was acted on by nobody. The inverse failure — a note
acted on *further than its author intended* — is the same defect with the sign flipped, and a hold
that lives only in a chat window is a hold that does not survive the chat.

---

HQ Chat should:

1. **[HELD]** **Open P12 on SN-31's spine** — completion of the workflow vision on governance plus the Drivr
   MVP — and carry `P11-GH-3` into its opening, per the digest's own Next Action 5: the phase
   closure gate needs a pre-merge completion artifact, and P12's opening is its own first customer.

2. **[HELD]** **Treat the four fail-open behaviours as the phase's organizing evidence**, with the sequencing
   constraint in Decision 2 recorded as binding: the three execution-tier defects land before the
   first real agentic integration.

3. **File SN-32** as a gap record in HQ's numbering, separately from the consolidation work that
   fixes it.

4. **Action or explicitly defer SN-30's four items** (SN-33). Silence is not an acceptable
   disposition for a Steering Note that has already been dropped once.

5. **Place the two build items** — the handoff artifact, and Drivr's recorded mode-flip from
   Decision 5 — into milestones with room.
