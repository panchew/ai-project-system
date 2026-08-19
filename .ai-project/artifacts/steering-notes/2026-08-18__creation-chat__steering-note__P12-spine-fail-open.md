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
  - id: SN-34
    severity: medium
    title: governance-propagation.md's Constraints are factually false and its Non-Goals prohibit work now contemplated — an active normative document resting on an expired technical premise
  - id: SN-35
    severity: medium
    title: There is no HQ re-instantiation ritual — HQ can be opened once at inception and has no defined way to be re-opened, though it is re-opened routinely
decisions:
  - "P12's spine, in the CFO's words: completing the CFO's vision of the workflow, using the governance and the MVP of the harness (Drivr). A completion phase, not a redesign."
  - "The three verified execution-tier defects are P12 scope, under a sequencing constraint rather than a date: they land BEFORE the first real agentic integration, not after."
  - "Accept-by-silence is tweaked, not retired. The low-ceremony property is kept; silence as the sole carrier is replaced."
  - "The PARENT performs the merge, not the child. Reverses the CFO's own interview description and structurally closes the P9-GH-1 / P10-GH-9 bypass class."
  - "Exhausted rework flips the receiving parent chat to manual. Opt-out default, switch modelled on cfo_review_gate. Drivr performs the flip and records it, so the committed starter remains the source of truth."
  - "Consolidating the eight starter-shaped surfaces is P12 scope."
  - "Keep unchanged: per-instance Execution Mode in the committed starter; 'Mode is not authority'; PSG §11.6.1 (the CFO is the mandatory diff reviewer)."
  - "The rework limit is 3 attempts maximum, movable only by a written reason. This confirms the built rule rather than amending it."
  - "HOLD RELEASED 2026-08-18. The withheld input was governance auto-update; it is recorded in Carry-Over 9 at 'nice if possible' weight. P12 may be opened."
  - "i18n policy: chat and output in the user's language; documentation remains in the original language; English is authoritative; translation on demand is a view, never the source."
  - "Governance auto-update (nice if possible): opt-in, apply rather than notify, run by the harness at Phase Chat start ONLY, authorized by the CFO and HQ through Drivr's existing gate queue. Fail-open on the CHECK. Pin advances automatically; framework_version is written only after the roll-forward procedure completes. Artifacts under a rolled-back version are marked superseded, never dropped. bin/ai-project-init is fixed so repaired installs do not re-break."
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

### SN-34 — An active normative document rests on an expired premise [MEDIUM]

`governance/systems/governance-propagation.md` (`status: active`, v1.0.0) states as **Constraints**:

> *"HQ chats and related tools **do not** have live access to GitHub repositories."*
> *"No automatic synchronization or polling is **possible**."*

**Both are false as of 2026-08-18.** This repository is operated through `gh` daily; `B2.1`
(P11-M37) gave the sandbox reachability to the host; and **Drivr is a scheduler**. On those
constraints the document builds three prohibitions — *"Governance does not propagate automatically
or implicitly"*, *"Manual Enforcement... not automation"*, and the Non-Goals *"No CLI or automation
tooling. No automatic or live governance syncing."*

**This is filed independently of whether the CFO's governance auto-update idea is ever built.** A
normative document whose stated justification has expired is a defect on its own: any future
proposal in this area will be measured against a rule whose reasoning no longer holds, and will
either be wrongly refused or quietly ignored. Both outcomes are worse than an amendment.

**It is also a known error class in this project.** The P11 phase record lists, among the HQ errors
caught one level down, *"a technical note inherited from an opener and never checked against the
running version."* This is that, at the normative tier, aged across at least four phases. It is the
**time axis** of `P11-GH-2`.

**Required action:** rule on `governance-propagation.md` — amend the Constraints to match reality
and decide deliberately whether the prohibitions survive their justification. The ruling is required
even if Carry-Over 9 is never scoped.

---

### SN-35 — HQ can be born but not re-opened [MEDIUM]

**Found by the CFO, 2026-08-18, by needing the thing and not finding it.** He asked for an HQ Chat
Opener to carry this note to HQ, and observed that he expected not to have had to ask.

Measured the same day: `governance/systems/hq-chat.md`,
`governance/systems/hq-execution-chat-starter.md` and `governance/templates/hq-chat-opener.md`
contain **zero** occurrences of re-instantiation, re-opening, or any equivalent. The only documented
route to an HQ Chat is `start-a-project.md` Step 3 — the **inception** path, in which the opener is
*"produced by the Creation Chat's full-path convergence... filled out per `seed.md` Rule 4"*, paired
with a committed `genesis.md`.

**`ai-project-system` has neither a `genesis.md` nor a Project Brief, both by ruling** (SN-26,
canonized P11-M36-E36.3). So the one documented path to opening HQ is unavailable to this project,
while HQ chats are re-opened here routinely — the CFO opens fresh ones mid-phase by design, which is
the stated reason governance auto-update runs at Phase start and not HQ start (Carry-Over 9).

**This is SN-26's defect, un-generalized.** The Creation Chat had exactly this hole: a continuity
problem served only by a bootstrap artifact. It was found, ruled on, and closed with a
Re-instantiation Ritual naming the committed artifacts a re-opened session receives. **Nobody asked
whether HQ had the same hole.** It does.

**The evidence is the opener itself.** The one produced to carry this note had to be adapted from an
inception template, filling founding-state fields with current state and adding a "read these two
committed artifacts" section modelled on the Creation Chat's ritual Step 3. That adaptation is
stated inside the opener rather than hidden, but an adaptation invented per-occasion is precisely
what a ritual exists to prevent.

**Required action:** define an HQ re-instantiation ritual, in one normative place, naming the
committed artifacts a re-opened HQ session receives and where an instance of the opener lives. The
Creation Chat's ritual is the model and the precedent for its shape; this is not novel design work.

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

9. **Governance auto-update — "nice if possible", and fully specified at that weight.** The input
   the hold was placed for. **It does not change the spine**, and the CFO assigned it explicitly
   opportunistic priority. Recorded here in full so it is neither lost nor inflated:

   | Question | The CFO's answer |
   |---|---|
   | What it does | **Applies**, not merely notifies |
   | When | **Phase Chat start only** — deliberately *not* HQ start, because a new HQ chat may be opened mid-phase, mid-milestone or mid-epic |
   | Who runs it | The harness (Drivr) |
   | Who authorizes | The CFO **and** HQ, routed through **Drivr's existing derived gate queue and signed one-time-link approval** — the mechanism is already built and is to be pointed at this, not rebuilt |
   | Which version moves | The **pin** (`governance.version` / `ref`) automatically; **`framework_version` only once the roll-forward procedure has actually completed**, so the field keeps meaning what `ai-project-yml-spec.md` §3.6 says it means |
   | On failure to determine | **Fail-open, for the *check*.** Correct here and not an instance of SN-31: fail-open is a defect when the fallback *does something*, and safe when the fallback is *no change*. An undetected update leaves the project exactly where it was. |
   | Rollback | Artifacts written under a rolled-back version are **marked superseded, never dropped** — using the `supersedes:` frontmatter mechanism the Progress Digests already use. The record of what happened is not revised by a version being un-pinned. |
   | Already-broken installs | **Fixed** — and `bin/ai-project-init` is fixed with them, since it hard-codes the path that produced FM 12's placeholder agents and the three non-`.governance` projects. Repairing installs without repairing init re-breaks them on the next install. |

   **The invariant this creates, stated because it is the reason for the schedule and not merely a
   consequence of it: one phase, one governance version.** A phase runs start to finish under a
   single ruleset. This sidesteps `P11-GH-1` at this tier by construction, and it makes rollback
   scoping tractable — "artifacts written under version X" maps onto phase boundaries.

   **Two sub-questions remain open and are the CFO's to close:** (a) what happens when an **apply**
   fails *partway* — fail-open was answered for the check, and a half-applied governance is a state
   neither version defines; (b) whether "mark superseded" should be narrowed further for artifacts
   that are explicitly immutable (a Review Decision, once issued, cannot be revised — but it can be
   annotated).

   **Scope warning for HQ:** *"fix already-broken installs"* turns this from an updater into a
   **reconciler**, which is materially larger than the rest of the item and larger than "nice if
   possible" implies. It should be split rather than carried as one unit.

10. **i18n policy — decided, and it costs almost nothing to state.** Chat and output in the user's
    language; **documentation remains in the original language**; **English is authoritative**;
    translation available on demand as a *view*, never as the source. This is one paragraph of
    normative text, not a project. It also resolves the tension Carry-Over 6 raised: propagating
    English normative text to a Spanish-speaking adopter is **correct** under this policy, because
    the English is the authority and any translation is derived from it.

## Next Action

### HOLD — PLACED AND RELEASED, both on 2026-08-18

**The hold is released. All five items below are actionable.**

The record of it is kept rather than deleted, because the hold and its release are both governance
events. When this note was first committed (`8071eeb`), the CFO had stated there was a further input
P12 could not be entered without, which he had not yet recalled. Next Actions 1 and 2 were blocked
pending written release; 3, 4 and 5 were not.

**The withheld input was governance auto-update.** It is recorded in **Carry-Over 9** below, at the
weight the CFO assigned it — *"nice if possible"* — and it does **not** alter the spine. Its
independently-filed defect is **SN-34**.

The hold was written into the artifact rather than left in chat on purpose. SN-33 records a Steering
Note that reached its target and was acted on by nobody; a note acted on *further than its author
intended* is the same defect with the sign flipped. A hold that lives only in a chat window does not
survive the chat.

---

HQ Chat should:

1. **Open P12 on SN-31's spine** — completion of the workflow vision on governance plus the Drivr
   MVP — and carry `P11-GH-3` into its opening, per the digest's own Next Action 5: the phase
   closure gate needs a pre-merge completion artifact, and P12's opening is its own first customer.

2. **Treat the four fail-open behaviours as the phase's organizing evidence**, with the sequencing
   constraint in Decision 2 recorded as binding: the three execution-tier defects land before the
   first real agentic integration.

3. **File SN-32** as a gap record in HQ's numbering, separately from the consolidation work that
   fixes it.

4. **Action or explicitly defer SN-30's four items** (SN-33). Silence is not an acceptable
   disposition for a Steering Note that has already been dropped once.

5. **Place the two build items** — the handoff artifact, and Drivr's recorded mode-flip from
   Decision 5 — into milestones with room.

6. **Rule on `governance-propagation.md` (SN-34)** — amend its false Constraints and decide
   deliberately whether its prohibitions survive the justification that has expired. Required
   independently of Carry-Over 9's priority.

7. **Note a known gap in the spine's own definition before scoping:** the CFO's **Drivr UX vision**
   (Carry-Over 7) has not yet been described. Drivr is the MVP half of the spine. The CFO has
   authorized opening the phase with this outstanding — it is a milestone-level input, not a
   blocker — but P12 should not be scoped as though Drivr's surface were settled.
