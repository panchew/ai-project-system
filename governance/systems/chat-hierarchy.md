---
type: system
status: active
effective_date: 2026-09-02
version: 1.3.0
---

# Chat Hierarchy — System Reference

## Purpose

This document provides the single authoritative end-to-end reference for the complete AI Project System chat hierarchy. Readers can understand the full four-level chain, artifact responsibilities, and authorization flow without reading all four individual system documents.

---

## The Four-Level Chat Hierarchy

The AI Project System organizes governance and execution across four levels, each with distinct roles and responsibilities. All four levels are served by a single **Governance Agent** (`governance/agents/governance.agent.md`) that self-configures its mode based on the Chat Starter delivered.

> **Note — these four levels are defined *within a single project*.** A separate,
> machine-wide participant, **System HQ**, sits *above and across* every project's HQ Chat
> and is **not** one of these levels (not a "Level 5"). It is documented in the
> out-of-hierarchy annex "System HQ — Out-of-Hierarchy, Cross-Project Participant" near the
> end of this document; its schemas and authority boundary live in
> `governance/systems/system-hq.md`.

```
┌─────────────────────────────────────────────────────┐
│              Governance Agent                       │
│  (single agent, mode selected by Chat Starter)      │
├──────────┬──────────────────────────────────────────┤
│    Mode   │ Role                                     │
├──────────┼──────────────────────────────────────────┤
│  HQ      │ Project-level governance & Phase planning│
│  Phase   │ Milestone planning within a Phase        │
│  Milestone│ Epic planning within a Milestone        │
│  Epic    │ Code execution & delivery                │
└──────────┴──────────────────────────────────────────┘

HQ mode
 │
 ├─ produces → Phase Execution Chat Starter
 │
 └─ Phase mode (plans milestones)
     │
     ├─ produces → Milestone Execution Chat Starter
     │
     └─ Milestone mode (plans epics)
         │
         ├─ produces → Epic Execution Chat Starter
         │
         └─ Epic mode (executes epic work)
             │
             └─ produces → PR, commit, deliverables
```

---

## Hierarchy Summary Table

| Level | Mode | Launched By | Consumes | Produces | Issues | Scope |
|-------|------|-------------|----------|----------|--------|-------|
| **1 — Project** | HQ | (bootstrap) | Phase Spec stubs | Phase Execution Chat Starters | Phase Delivery Authorization | All Phases |
| **2 — Phase** | Phase | HQ | Phase Execution Chat Starter | Milestone Specs, Milestone Execution Chat Starters | Milestone Delivery Authorization | Single Phase |
| **3 — Milestone** | Milestone | Phase (or HQ) | Milestone Execution Chat Starter | Epic Specs, Epic Execution Chat Starters | Epic Delivery Authorization | Single Milestone |
| **4 — Epic** | Epic | Milestone | Epic Execution Chat Starter | Code, commits, PR | (Deliverables for review) | Single Epic |

---

All levels are served by a single **Governance Agent** (`governance/agents/governance.agent.md`). The Chat Starter header determines which mode activates — see [Mode Detection Logic](governance.agent.md#mode-detection-logic) in the agent definition.

---

## Execution Mode: Manual vs. Agentic (Per-Instance Declaration)

*(Added P9-M31-E31.1, 2026-07-19.)*

The table above uses **"Mode"** for a different axis entirely: which of the four levels
(HQ/Phase/Milestone/Epic) a chat instance is. This section introduces a second,
orthogonal axis — whether a *given instance* of a Phase, Milestone, or Epic chat runs
under direct human control or is dispatched to run unattended. To keep the two axes from
reading as one ("Milestone mode in agentic mode" is exactly the ambiguity being avoided),
this document keeps calling the level axis **"Mode"** (as in the table above) and always
spells out **"Execution Mode"** for this new axis — never bare "mode" where either
meaning is possible.

Execution Mode applies to **Phase, Milestone, and Epic instances only** (Levels 2–4).
Creation Chat and HQ Chat never take an Execution Mode — see "Creation Chat and HQ Chat:
Manual-Only, Permanently" below.

### The two Execution Modes

- **Manual** — the instance runs as a human-driven chat session, one decision at a time,
  exactly as every chat has run to date. **This is the default** (see Declaration below).
- **Agentic** — the instance is dispatched to run unattended against the model
  `.ai-project.yml`'s `models:` block assigns to its level, via the orchestrator/runner
  path (`bin/ai-project-orchestrator` → `bin/run-dev-agent`). The paid-vs-local choice
  *within* "agentic" is governed by the recorded model-routing policy
  (`.ai-project/artifacts/reference/token-measurement/model-routing-policy.md`) — this
  section only records that agentic instances exist and consume that policy; it does not
  restate or implement the policy's rows (that logic is a separate, later concern).

  **What exists mechanically today:** the dispatch path is implemented for the **Epic**
  level only (`bin/ai-project-orchestrator`'s epic-trigger handling, which calls
  `bin/run-dev-agent`). Declaring a Phase or Milestone instance agentic is a valid
  declaration under this mode model — the semantics above are level-agnostic — but no
  dispatch mechanism yet consumes a Phase/Milestone agentic declaration; wiring the
  orchestrator to those levels is future implementation work, not a defect in this
  declaration mechanism. No agentic instance, at any level, may assume a local model is
  always loadable — GPU-contention handling belongs to the routing policy, not to this
  section.

### The execution matrix (ratified)

*(Added P10-M35-E35.4, 2026-07-30.)*

HQ ratified the execution matrix on 2026-07-30 (**HQ Ruling on SN-25, Decision 4**), restoring the
E31.1 baseline recorded above at Phase and Milestone after SN-23 (2026-07-20) had narrowed P10's opening posture
to Manual/Paid from Creation through Milestone. The table is reproduced here exactly as ratified:

| Level | Execution Mode | Inference locality |
|---|---|---|
| Creation | Manual only (permanent, SN-22) | Remote |
| HQ | Manual only (permanent, SN-22) | Remote |
| Phase | Agentic or manual | Remote |
| Milestone | Agentic or manual | Remote — **local under evaluation** |
| Epic | Agentic or manual | Local or remote (in force, E34.3) |

> **Status of the Milestone locality cell (HQ Ruling, 2026-07-31).** The table above is left as
> ratified; this note records where its one open cell now stands. P10-M35-E35.5 back-tested a
> local model's Stage-2 review against five known-ground-truth defects and passed 4 of 5 with
> zero false alarms. HQ ruled **`model-routing-policy.md` row P4 unchanged — Milestone remains
> remote/paid frontier.** The evaluation established a *candidate*, not an adoption; the
> decisive finding was that the two runs on the missed defect gave identical diagnoses and
> **opposite prescriptions**, and at Milestone the remedy is the decision. Three gates now name
> what would move the cell (G-P4-a/b/c). "Local under evaluation" therefore remains accurate —
> evaluated once, candidate established, not adopted. See
> `.ai-project/artifacts/rulings/2026-07-31__ai-project-system-hq__ruling__milestone-locality-row-p4.md`.

Three things this table does not say — each of which it would be read as saying if left to stand
alone:

**The Creation and HQ rows describe how those levels run; they are not a declaration those levels
accept.** "Manual only" in those two cells means: manually, always, with no per-instance override
possible. It does **not** mean Creation or HQ carries a manual Execution Mode declaration. Neither
level's opener gains an Execution Mode field, then or now — see "Creation Chat and HQ Chat:
Manual-Only, Permanently" below, whose effect these two rows restate and do not amend.

**The locality column is a pointer, not an authority.** Inference locality is decided by
`.ai-project/artifacts/reference/token-measurement/model-routing-policy.md` rows P1–P7, under that
file's own **§Change discipline** (*"Policy rows change only with new cited evidence … never by
assumption"*). That file is authoritative on locality and **wins on any divergence** with this
column — the same relationship this document's "Manual Chat Model Verification" section below
already has with it. A reader asking which locality applies at a level is answered by the policy
rows, not finally by this table, which summarises them as of the ratification date.

**Restoring the mode is not building the dispatcher.** At Phase and Milestone the ask was dispatch,
not permission: this section already made Execution Mode normative at those levels, and the "What
exists mechanically today" paragraph above — that the dispatch path is implemented for the **Epic**
level only, and that *"no dispatch mechanism yet consumes a Phase/Milestone agentic declaration;
wiring the orchestrator to those levels is future implementation work"* — **remains true after this
ratification and is unmodified by it.** The matrix restores a *possibility*, not a default. No Phase
or Milestone agentic run can be dispatched today, and nothing in this repository runs differently
because the matrix was recorded.

**SN-23 (2026-07-20) Ratified Decision #2 is superseded on the Execution Mode axis only.** Decision 2's own text
is preserved verbatim in the P10 phase spec's Ratified Decisions and is **not reopened**. Its
**Execution Mode axis is superseded** — Phase and Milestone may now run agentically or manually,
restoring the P9-M31-E31.1 baseline that SN-23 (2026-07-20) had narrowed for P10's start. Its **locality axis
stands**, with Milestone × local inference now under a directed evidence evaluation (P10-M35-E35.5)
rather than settled either way: that cell is neither opened nor closed, and "under evaluation"
records that the question is live and directed, not that it is unanswered by neglect. The
supersession is recorded explicitly so that it is a decision rather than drift. This record agrees
with the phase spec's **Ratified Decisions → Note on Decision 2** footnote; see also
`.ai-project/artifacts/rulings/2026-07-30__ai-project-system-hq__ruling__sn-25-handback-and-execution-matrix.md`.

### Mode is not authority

*(Added P10-M35-E35.4, 2026-07-30. **This is the normative home of this rule.** Other sections of
this document cite it rather than restating it, so the corpus holds one statement that cannot drift
against a second.)*

Restoring agentic Execution Mode at Phase and Milestone says an instance at those levels **may run
unattended.** It does **not** widen what that instance may **authorize.** An instance running
unattended holds exactly the authority its level always held.

**Until ruled otherwise, authority-bearing acts — Stage-2 acceptance and merge authorization —
still require the human's key, whatever Execution Mode the instance is running in.**

**Mode is what may run; gates are what may be decided without a key.** Conflating the two would let
a mode restoration silently widen authority, which is precisely the class of drift this framework
exists to prevent. Per-level gates remain a requirement and stay revisitable (SN-24), and technical
possibility remains not sufficient reason (HQ Ruling on SN-25, Decision 4) — the matrix is a bounded
position, not a removal of limits.

**Why this binds hardest at Milestone.** Milestone is where **Stage-2 accept authority** lives — the
level whose errors propagate into merges, and the reason `model-routing-policy.md` row P4 reads paid
frontier. A Milestone instance declared agentic may run its review work unattended; it may not
accept a delivery or authorize a merge on its own signature.

**Corollary, for the reader who knows the default-accept model.** PSG §11.6's accept-by-silence
turns a parent's *silence* into acceptance. That model presumes a manual instance, where the human's
key is present at the session by construction; the matrix does not extend it to an unattended one.
An agentic instance's silence is not the silence §11.6 speaks of, and does not by itself accept a
delivery. This follows from the rule above rather than adding to it — no new gate is created here,
and none is removed.

### Declaration mechanism

Execution Mode is declared **per instance**, not project-wide. A single project-wide
switch cannot express "this Milestone Chat session is agentic, the next one is manual"
without becoming a constantly-edited, drift-prone value — so the declaration lives in the
concrete instance's own committed **Execution Chat Starter**
(`governance/templates/{phase,milestone,epic}-execution-chat-starter.md`), in an
**Execution Mode** field near the header, filled in by the parent chat at the moment it
produces the starter — the same natural author, at the same natural moment, as every
other starter field.

- `Execution Mode: manual` — the instance is declared manual.
- `Execution Mode: agentic` — the instance is declared agentic.
- **No field present means manual.** A starter that omits the Execution Mode field —
  including every starter produced before this section existed — is a manual instance.
  No instance is agentic without an explicit, git-tracked declaration in its own starter.

A reader determines any instance's Execution Mode by reading its committed starter file —
no new artifact type, lifecycle, or `.ai-project.yml` field is introduced; the mechanism
piggybacks on the artifact every instance already receives.

### Creation Chat and HQ Chat: Manual-Only, Permanently

Creation Chat (Level 0) and HQ Chat (Level 1) **never take an Execution Mode declaration
and never run agentically.** This is normative, permanent policy (SN-22), not a deferral
pending future work. Neither level's opener gains an Execution Mode field; both levels
are manual at all times, unconditionally, with no per-instance override possible.

### Session-discipline guidance: one task, one session (G7)

*(Adopted 2026-07-19, per the M30 Milestone Closure Declaration's G7 recommendation.)*
M30's token-burn audit found that milestone- and phase-level sessions mixing several
unrelated tasks in one session (planning, Stage-2 review, and closure authority together)
accounted for 53% of measured spend, versus 23% for single-task epic execution sessions
(`.ai-project/artifacts/reference/token-measurement/audit-report.md` §2.2). Based on that
measured evidence, this document records, as **guidance, not a requirement**: start a new
chat instance per discrete task rather than continuing one instance across unrelated
tasks. This recommendation applies uniformly to manual and agentic instances alike; it is
not gated by, and does not affect, any instance's Execution Mode declaration.

### Manual Chat Model Verification (P9-M31-E31.3)

*(Added P9-M31-E31.3, 2026-07-19 — the manual-mode counterpart to the Execution Mode
declaration above and to E31.2's agentic decision logic: neither gives a manual chat any
way to know, or refuse on, a model mismatch. This section closes that gap.)*

This section defines, for every manually-startable chat level, which model it is expected
to run on, how it checks its own identity against that expectation, and what it must do on
a mismatch. It governs **manual** instances only — agentic dispatch's model selection is
E31.2's surface, untouched here.

#### The mapping

| `.ai-project.yml` key | Value | Level | Basis |
|---|---|---|---|
| `creation` | `remote:claude-opus-5` | Creation | New key (this Epic). Policy row P1 (`model-routing-policy.md`): paid frontier, manual. |
| `hq` | `remote:claude-opus-5` | HQ | Existing key (P9-M30-E30.2). Policy row P2. |
| `phase` | `remote:gpt-5.6-sol` | Phase | Existing key. Policy row P3. |
| `milestone` | `remote:deepseek-v4-pro` | Milestone | Existing key. Policy row P4. |
| `epic_manual` | `remote:deepseek-v4-flash` | Epic (manual) | New key (this Epic), distinct from the `epic_dev`/`epic_qa` agentic-dispatch lanes those keys serve. Policy row P5's general "epic × execution: paid frontier" default — P6/P7's local-offload values apply only when the agentic Dev/QA dispatch lanes are actually in use, which a manual Epic chat, by definition, is not. |

**Values are versions; the decision behind them is a tier.** These five cells named
`remote:claude-opus-4-8` until 2026-07-28, when that version stopped being offered in the
harness surface in use and this guardrail — correctly — halted every manual chat at once
(`.ai-project/artifacts/escalation-notices/2026-07-28T20_00_00Z__P10-M34__escalation_notice.md`).
HQ refreshed all five to `remote:claude-opus-5`, the same
line's successor. What the policy actually decides is *paid frontier* (rows P1–P4); only
this table and `model-routing-policy.md`'s mapping table name a version, and a version can
be deprecated where a tier cannot. Expect this refresh to recur at every future
deprecation, and treat it as a mapping change rather than a policy change — see
`model-routing-policy.md`'s **Mapping revisit trigger — model unavailability**. Deciding
which model fills the tier *per level per project* is routing, and routing is Drivr's
domain from P11 onward; the framework does not build a relocation of these values in the
interim. See `.ai-project/artifacts/rulings/2026-07-28__ai-project-system-hq__ruling__paid-frontier-model-mapping-refresh.md`.

(This table records all five manual-verification keys for completeness; `tests/test_model_config.py`'s divergence guard applies it only to the two keys with no pre-existing coverage — `creation` and `epic_manual` — since `hq`/`phase`/`milestone` are already fully guarded via `model-routing-policy.md`'s own mapping table, unchanged by this Epic.)

`creation` and `epic_manual` are new keys, added by this Epic because the pre-existing
five-key `models:` set (`hq`, `phase`, `milestone`, `epic_dev`, `epic_qa`) was built for
agentic dispatch and does not reach Creation (which never dispatches) or a manually-run
Epic chat (which is neither the `epic_dev` nor the `epic_qa` agentic lane). See
`governance/ai-project-yml-spec.md` §3.4 for the field definitions and
`.ai-project.yml`'s `models:` block for this repository's live values. Both new keys are
**consumed from, not re-derived against,** `model-routing-policy.md`'s policy rows — this
section cites those rows' reasoning; it does not add new rows to that file, which is out
of scope for this Epic.

#### Self-model verification method

The only observed mechanism by which a chat can know what model it is currently running
on is the **harness's own self-report**: this repository's harness (Claude Code) injects
an `# Environment` block into every session's system context naming the running model
(e.g. *"You are powered by the model named Sonnet 5. The exact model ID is
claude-sonnet-5."*). A manual chat verifies itself by reading that self-report and
comparing it to the level's expected value above.

**Known limit, stated plainly:** this is a harness-provided self-report, not an
independently, cryptographically verifiable fact. The chat has no mechanism to confirm the
string the harness gave it is accurate — it can only act honestly on what it was told. No
stronger claim is made here.

#### Absent block, or absent key

A freshly initialized project's `.ai-project.yml` has no `models:` block at all
(`bin/ai-project-init` writes only `project:` and `governance:`); an existing project's
`models:` block may predate this Epic and lack the `creation` or `epic_manual` keys. Both
cases are the same condition: **there is no configured expectation for this level to
verify against.** The documented behavior is an explicit **permissive default**: the chat
proceeds, but must state plainly, in its first substantive response, that no
model-mapping expectation is configured for its level and no verification was performed.
This is deliberately different from refusing outright on an absent block — a fresh project
with no `models:` block must still be able to open its first chat — and deliberately
different from silence — an unstated skip would be as dishonest as a false refusal claim.
"Cannot verify, therefore refuse" was the other legitimate option considered; this
document's answer is the permissive default, stated explicitly, not silently assumed.

#### Mismatch: ADVISORY by default, blocking by opt-in

> **AMENDED 2026-08-27 (SN-40, CFO Decision 3).** This section previously read *"Mismatch:
> refuse, unconditionally."* **The reasoning behind that refusal stands and is preserved
> below** — it was written after a Creation Chat ran `claude-opus-5` against a configured
> `remote:claude-opus-4-8` and opened anyway. **What it did not anticipate is a CFO
> deliberately moving the lineup**, for whom an unconditional refusal makes a *mistaken*
> switch stop the next chat from opening at all. That is a ratchet, and the CFO hit it in
> the wild on `panchew-io`.
>
> **The default is now `advisory`.** Governed by `model_verification` in `.ai-project.yml`:
>
> | Value | Behaviour |
> |---|---|
> | **`advisory`** (default) | The chat **states the mismatch plainly in its first substantive response** — self-reported model vs configured value — **and proceeds.** |
> | `blocking` | The unconditional refusal below, restored verbatim. |
>
> **The honesty requirement is unchanged and is not weakened by this amendment:** an
> unstated skip would be as dishonest as a false refusal claim. **Advisory means *say it and
> continue*, never *say nothing*.**
>
> **Absent key → `advisory`.** A missing `model_verification` is not an error; the
> permissive default already governs an absent `models:` block and this is consistent with
> it.
>
> **This lapses on the CFO's declaration**, not on a phase boundary: it defaults off *until
> he declares it is OK to enforce the switching gates.* Until that declaration **no gate
> blocks a lineup change, including SN-37's model-qualification gate** — **suspended for
> lineup changes, not reversed.**

#### The blocking behaviour, retained verbatim for `model_verification: blocking`

If the harness-reported model and the configured expected value for this level are both
present and disagree, the chat **MUST stop** before doing any further planning, review, or
execution work in that session, and state the mismatch plainly (self-reported model vs.
configured value). This is a refusal, not an advisory — no continuation, no "proceeding
with caution," no deferring the check to later in the session. A mismatch never resolves
to switching to agentic mode (no agentic default — this section does not touch Execution
Mode). Policy↔block divergence (the recorded policy disagreeing with `.ai-project.yml`
itself, independent of any chat's own model) is likewise treated as an error, consistent
with E31.2's `tests/test_model_config.py` guard.

**What "refuse" technically means here:** there is no code process wrapping a manual chat
session the way `bin/ai-project-orchestrator` wraps agentic dispatch. This refusal is a
**documented instruction the agent must follow**, enforced the same way every other
AOG/PSG "MUST" in this framework is enforced — by the agent's compliance with governing
documentation — not a technical impossibility-to-proceed. Stating this honestly is itself
part of what this section requires of anything built on top of it.

### Handback: what a blocked agentic instance owes

*(Added P10-M35-E35.3, 2026-07-30, recording the HQ Ruling on SN-25, Decisions 1–2 and 7.)*

The Execution Mode declaration above says an instance **may** run unattended. Until this
section, nothing said what that instance owes anyone when it cannot finish. This section
closes that gap.

It records an **obligation only**. No mechanism in this repository implements, detects, or
carries it — see "The signal this rule depends on is measured broken (P10-GH-7)" below,
which a reader of this rule must not skip.

#### The obligation

An **agentic instance that becomes blocked** — one that has encountered something requiring
judgment it cannot supply — **MUST surface the block.**

Stopping without surfacing is non-compliant. Finishing anyway, on a guess about what the
missing judgment would have been, is non-compliant. There is no third quiet exit: an
autonomy that cannot hand back is not autonomy, it is an unattended process that fails
silently (SN-25).

The handback travels as an **escalation notice**
(`governance/templates/escalation-notice.md`) — the artifact type that already exists for
exactly this purpose. **No new artifact type and no new authority model** is created by this
rule (HQ Ruling on SN-25, Decision 1).

It MUST carry enough for the receiving level to act without re-deriving the situation:

- **the nature of the blocker** — what judgment is missing, and why the instance cannot
  supply it;
- **what was attempted** — the concrete steps already taken before surfacing;
- **what could not be resolved** — the specific decision or input needed to proceed.

Those are the template's existing `## Trigger`, `## What Was Attempted`, and
`## Decision Needed` sections. This rule adds **no field** to its schema.

#### This rule binds instances that are not chats

`PROJECT-SYSTEM-GUIDELINES.md` §13D speaks of *levels*; the escalation-notice template
speaks of *"any chat."* An unattended agentic run is neither, in the ordinary reading — it
has no chat in which a human notices a block, and no human present to write the notice.

**It is nonetheless subject to this rule.** An agentic Phase, Milestone, or Epic instance is
a level of the hierarchy for every purpose of the "Communication Protocol" below, and the
absence of a human in the loop is the **reason the obligation binds**, not an exemption from
it. The escalation-notice template carries the matching applicability statement at its own
end of the cross-reference.

#### The destination is the immediate parent — not "a human"

The handback goes to the blocked instance's **immediate parent, and nowhere else.**

It does **not** go to "a human." An instance has no way to identify a human and no standing
to select one; a rule written that way would be a rule no instance could execute. (HQ Ruling
on SN-25, Decision 1, amending SN-25's own first framing, which read *"summon a human."*)

**The human is still reached — by construction, not by hope.** Each hop travels up exactly
one level, and the chain Epic → Milestone → Phase → HQ → Creation is finite. Its top two
rungs, **Creation Chat and HQ Chat, never take an Execution Mode declaration and never run
agentically**: they are manual at all times, permanently, with no per-instance override
possible (SN-22 — see "Creation Chat and HQ Chat: Manual-Only, Permanently" above). An
escalation therefore **cannot escalate past a manual level**; it arrives at one in **at most
three hops** from the deepest agentic level (Epic → Milestone → Phase → HQ), and at a manual
level there is a human by definition. Termination is a **structural property of the
hierarchy, guaranteed by SN-22** — not a hope that someone happens to be watching.

That reasoning is written out here deliberately. A reader who sees only "immediate parent"
will eventually re-derive *"but then the human never hears about it"*; the SN-22 termination
argument is the answer, and it only works if it is on the page.

The CFO's *"my chat opens ready for me to intervene"* is then correctly placed: it is the
**surface behaviour** of a manual level receiving an escalation. How the arrival is
presented is coordination, and coordination is P11's. Governance's part is that the notice
must be emitted, must reach the parent, and must carry enough context to act on.

#### The resolving intervention is authority-bearing

When the parent resolves a handback, its resolution **carries authority.** It is not
advisory input the blocked instance may weigh, discount, or proceed against. The blocked
path stays blocked until the parent responds and sets the notice to `status: resolved` —
the escalation-notice template's existing rule, which this section does not modify but does
make load-bearing for unattended runs.

**This does not widen what the parent may authorize.** *Mode is not authority* — **cited here, not
restated:** see "Mode is not authority" above, which is that rule's normative home (HQ Ruling on
SN-25, Decision 4). Applied to handback: an instance running unattended holds exactly the authority
its level always held, so a handback resolution is a **direction to the child**, not a new power for
the resolver. *(Citation form adopted P10-M35-E35.4, 2026-07-30; the rule this section states was
unchanged by that Epic.)*

#### Routing: exactly one level, per the protocol that already governs it

Handback routing introduces **no new rule.** It is the framework's existing
upward-communication rule applied to a new subject. That rule is normative in three surfaces
that already agree, and is **cited here rather than restated** — a fourth copy is a fourth
thing that can drift:

| Surface | What it carries |
|---|---|
| `governance/PROJECT-SYSTEM-GUIDELINES.md` **§13D** (Mandatory) | Upward communication is 1-to-1; escalations travel up one level; no level skips its parent to reach a grandparent (SN-12b, 2026-06-25) |
| `governance/AI-OPERATING-GUIDELINES.md` **§3.10** | The same rule for the operating tier |
| **"Communication Protocol" → "Upward — 1-to-1, one level at a time"**, below in this document | The full protocol §13D defers to |

Read those for the rule itself. What this section adds is only its **application to a
handback**:

- **The parent decides direction** — *resolve and return* to the child, or *issue its own
  notice* one level up. That choice belongs to the parent, never to the child.
- **No instance names a target above its parent.** Judgment about the problem stays nearest
  the problem; judgment about *where it goes* stays with the level holding authority over it.
- **Instance-judged routing was considered and rejected**, and the reason belongs in the
  record: it lets **a child choose its own judge.** An Epic routing straight to HQ steps
  around its Milestone Chat's Stage-2 authority, and the parent may never learn its own epic
  is blocked.

#### P9-GH-1 is not closed by this section

**Nothing in this section closes P9-GH-1, softens it, or partly addresses it.** That remains true
and is the point of this subsection.

> **Status update (2026-08-17, Epic P11-M40-E40.5).** `P9-GH-1` was **closed** by a separate,
> later change — the guard was extended to **eight** starter surfaces (three `governance/templates/`
> starters, four `governance/systems/` starter surfaces, and `governance/EPIC-EXECUTION-CHAT-STARTER.md`),
> level-aware per level, backed by `tests/test_merge_authorization_routing_guard.py`. It was **not**
> closed here. The sentence below described the state of the world when this section was written and
> is retained for that reason: at the time, P9-GH-1 was open, carried forward, and unowned.

The two are adjacent, and a future reader will conflate them unless the record refuses to.
**P9-GH-1 is a merge-authorization hole** in the Milestone and Phase Execution Chat Starter
templates — the guard that routes merge authorization to the parent was never extended past
the Epic templates. **This section is about where an escalation is addressed.** Both concern
authority travelling between the same levels, and that is the whole of the resemblance:
recording an escalation-routing rule patches no template, and no template was patched here.
(HQ Ruling on SN-25, Decision 2.)

#### The CFO is not a level in the chain

The chain is Epic → Milestone → Phase → HQ → Creation. The **CFO (Layer 8) is not one of its
rungs.** The CFO is the authority the whole chain serves and **may answer at any point
without that being a bypass.** The one-level rule constrains **instances**; it does not
constrain the human whose keys the gates exist to hold.

**The obligation a direct answer creates is recording.** The decision must land where the
level that would otherwise have ruled can see it — in the escalation notice's
`## Resolution`, and in whatever spec the decision amends. An **unrecorded** direct answer is
the failure mode here; the directness is not.

Both halves have committed worked examples from P10-M34:

- **Two hops, no level skipped.**
  `.ai-project/artifacts/escalation-notices/2026-07-28T20_00_00Z__P10-M34__escalation_notice.md`
  — the M34 Milestone Chat could not open (it refused on a model mismatch, correctly, per
  "Manual Chat Model Verification" above); its parent Phase Chat diagnosed the cause and
  issued **its own** notice one level up to HQ; HQ ruled. The reach to HQ was *reached*, one
  hop at a time, rather than guessed at from below.
- **A direct CFO resolution, recorded.**
  `.ai-project/artifacts/escalation-notices/2026-07-29T00_00_00Z__P10-M34__escalation_notice.md`
  — resolved by direct CFO instruction to the Phase Chat rather than a round trip to HQ, on a
  narrow, scope-*reducing* question. The notice carries the resolution in its `## Resolution`
  section and the phase spec carries the matching amendment at v1.2.0. The Phase Chat flagged
  the routing choice rather than normalizing it silently — that flagging is the standard, and
  it should continue.

#### Declining to act and surfacing the block are both required

`governance/systems/fleet-operator.md` states that where an authority-shaped request cannot
proceed, *"declining to act is a successful outcome for this role, not a failure to
perform."* That is correct in its own frame: refusing a fleet-wide write on a spoken word is
a success.

**It is not a licence to stop silently.** Declining to act and surfacing the block are
**both** required, and they are one sequence rather than two options: decline, **then**
surface. An instance that stops without handing back has performed half the obligation — and
the half it skipped is the one this section exists to impose. `fleet-operator.md` carries the
matching statement at its own end of this cross-reference.

#### Creation Chat awareness is visibility only

The Creation Chat is aware of escalation notices wherever they arise, and that awareness is
**never a resolution path**. It is recorded in
`governance/systems/creation-chat-guide.md` ("Escalation Awareness — Visibility Only") and is
not restated here.

#### The signal this rule depends on is measured broken (P10-GH-7)

This section records an obligation whose trigger **no working mechanism reliably detects.** A
reader of the handback rule must meet that dependency in the same reading, not two documents
away.

**You cannot escalate on a block you cannot detect** — and detection is measured broken in
**both** directions:

- **False success.** P10-M33-**E33.2 Run A returned exit 0 having done zero work** — the
  validation command would have passed on the unchanged repository.
- **False failure.** P10-M33-**E33.4 returned exit 2 having produced complete, green work.**

Corroborated across two projects on this stack: **the exit code is not a completion signal.**
Compounding it, **G11 stands — `epic_qa` has zero captured runs.** The lane that would answer
*"is this instance stuck, finished, or confidently wrong"* has a config key and a policy row
and no evidence behind it, so the capability best placed to supply a trustworthy signal is
the one never exercised.

A handback mechanism built naively over this signal yields **constant false escalations** —
the human becomes the bottleneck again, worse than before — **or silent no-ops that read as
success.**

This is **P10-GH-7** (HQ Ruling on SN-25, Decision 7; severity **High**, owner
**unassigned**). It is **recorded here, not solved here.** Solving it is a prerequisite for
the mechanism, not for this rule: the rule is written now precisely because recording it
costs nothing and building on it costs everything. **P11 (Drivr) builds the detector, the
channel, the mode switch, and the surfacing against these rules; none of them exists in this
repository today** (HQ Ruling on SN-25, Decision 8).

---

## Level 0: Creation Chat (Project Bootstrap)

The Creation Chat is the **entry point** for a new project — the step before the four-level hierarchy begins. It runs once per project, immediately after `ai-project init`. It is not one of the Governance Agent's four execution modes; it is a one-time bootstrap session (a human or an AI agent acting as Creation Chat).

The Level-0 handoff is **scale-dependent** — this section describes its **lightweight path**: a project brief converges on the single artifact that lets a Phase Chat open directly: a committed `genesis.md`. An ongoing, multi-phase project that needs a persistent control plane instead takes the **full path** — `seed.md` Rule 4's Project Brief + HQ Chat Opener convergence, handing off to an HQ Chat rather than a Phase Chat directly. See `governance/systems/start-a-project.md`'s "Choose Your Path" fork for the full comparison; both paths are legitimate Level-0 outcomes, not competing models.

### Role

Creation Chat scopes only **project identity, Phase 1 boundaries, and team composition**. It produces `genesis.md` from the genesis template, then hands off to the first Phase Chat. It never plans milestones or epics and never executes work.

### What It Consumes

- A **project brief** — goal, problem, rough Phase 1 scope, and the initial team (roles)
- The **governance repo path** (`.governance/`, established by `ai-project init`)

### What It Produces

- A completed **`genesis.md`** (`status: complete`), committed to the repository
- A **ready-to-open Phase Chat context** — the HQ Context Packet and Phase 1 Scope inside `genesis.md` are sufficient to open a Phase Chat with no further questions

### Authority

- **May** define and name Phase 1 scope
- **May** assign initial team roles (CFO, Phase Lead, Contributors)
- **May NOT** authorize execution, plan milestones/epics, or create branches, commits, or PRs — those belong to the Phase Chat and below

### Stopping Condition

Creation Chat is complete when `genesis.md` is committed (`status: complete`) and the user has been handed the Phase Chat starter to open next.

### Documentation

- **Template (lightweight path):** `governance/templates/genesis.md`
- **Template (full path):** `governance/templates/seed.md`
- **Walkthrough example:** `examples/genesis-walkthrough/genesis.md`
- **Process guide:** `governance/systems/start-a-project.md`

---

## Level 1: HQ Mode

### Role

HQ mode is the project-level governance and planning session. It:
- Opens with Phase specs
- Plans and authorizes all Phases
- Launches Phase Chats by issuing Phase Execution Chat Starters
- Accepts or rejects Phase deliverables
- Issues Phase Delivery Authorizations

### What It Consumes

- Phase spec stubs (defined in the project roadmap)
- Human input on project scope and strategy

### What It Produces

- **Phase Execution Chat Starters** — one for each Phase
- Structured governance decisions

### What It Issues

- **Phase Delivery Authorization** — signals to Phase Chat that planning may begin

### Communication Rules

- Reports to humans and stakeholders
- Communicates downward to Phase Chats only
- MUST NOT reach across phases

### Documentation

- **Agent definition:** `governance/agents/governance.agent.md` (HQ mode)
- **System reference:** `governance/systems/hq-chat.md`
- **Governing guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md` §12

---

## Level 2: Phase Mode

### Role

Phase mode is a planning session scoped to a single Phase. It:
- Opens with a Phase Execution Chat Starter from HQ mode
- Reviews the Phase spec
- Plans and authorizes all Milestones within the Phase
- Launches Milestone Chats by issuing Milestone Execution Chat Starters
- Accepts or rejects Milestone deliverables
- Issues Milestone Delivery Authorizations

### What It Consumes

- Phase Execution Chat Starter (from HQ Chat)
- Phase spec
- Milestone stubs within the Phase

### What It Produces

- **Milestone specs** — one for each Milestone
- **Milestone Execution Chat Starters** — one for each Milestone

### What It Issues

- **Milestone Delivery Authorization** — signals to Milestone Chat that planning may begin

### Communication Rules

- Reports upward to HQ Chat only
- Communicates downward to Milestone Chats only
- MUST NOT reach across phases or lateral epics

### Documentation

- **Agent definition:** `governance/agents/governance.agent.md` (Phase mode)
- **System reference:** `governance/systems/phase-execution-chat-starter.md`
- **Template:** `governance/templates/phase-execution-chat-starter.md`
- **Governing guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md` §13A

---

## Level 3: Milestone Mode

### Role

Milestone mode is a planning session scoped to a single Milestone. It:
- Opens with a Milestone Execution Chat Starter from Phase mode (or HQ mode)
- Reviews the Milestone spec
- Plans and authorizes all Epics within the Milestone
- Launches Coding Agents by issuing Epic Execution Chat Starters
- Accepts or rejects Epic deliverables
- Issues Epic Delivery Authorizations

### What It Consumes

- Milestone Execution Chat Starter (from Phase Chat or HQ Chat)
- Milestone spec
- Epic stubs within the Milestone

### What It Produces

- **Epic specs** — one for each Epic
- **Epic Execution Chat Starters** — one for each Epic

### What It Issues

- **Epic Delivery Authorization** — signals to Coding Agent that execution may begin

### Communication Rules

- Reports upward to Phase Chat (or HQ Chat during bootstrap) only
- Communicates downward to Coding Agents only
- MUST NOT reach across milestones or lateral phases

### Documentation

- **Agent definition:** `governance/agents/governance.agent.md` (Milestone mode)
- **System reference:** `governance/systems/milestone-execution-chat-starter.md`
- **Template:** `governance/templates/milestone-execution-chat-starter.md`
- **Governing guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md` §13B

---

## Level 4: Epic Mode

### Role

Epic mode is an execution session scoped to a single Epic. It:
- Opens with an Epic Execution Chat Starter from Milestone mode
- Executes all Definition of Done items
- Produces code, commits, and pull requests
- Creates a Delivery Notice
- Requests human review
- Responds to HQ Chat (either directly or via Phase/Milestone Chat per bootstrap mode)

### What It Consumes

- Epic Execution Chat Starter (from Milestone Chat)
- Epic spec
- Existing codebase and project context

### What It Produces

- **Code and commits** — implementation of all DoD items
- **Pull request** — proposed merge to the target branch
- **Delivery Notice** — structured summary of deliverables
- **Epic Review Seal** (structured) — findings for human review

### What It Issues

- (No authorization artifacts — Coding Agents execute on received authorization)

### Communication Rules

- Reports to Milestone Chat (or Phase Chat / HQ Chat per bootstrap)
- Does NOT communicate laterally or upward to other chats
- Awaits explicit authorization before beginning work

### Documentation

- **Agent definition:** `governance/agents/governance.agent.md` (Epic mode)
- **System reference:** `governance/systems/epic-execution-chat-starter.md`
- **Template:** `governance/templates/epic-execution-chat-starter.md`
- **Governing guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md` §13

---

## Authorization Artifacts

All execution transitions are gated by structured authorization artifacts. Only these three authorization types exist:

### Phase Delivery Authorization

**Issued by:** HQ mode  
**To:** Phase mode  
**Signals:** Phase planning may begin

**Format:**
```
PHASE DELIVERY AUTHORIZATION

Issuer: HQ Chat
Date: <YYYY-MM-DD>
Phase Reference: <P#> — <Phase Name>
Authorized Action: Proceed with Phase planning
Instruction: Produce Milestone specs and Milestone Execution Chat Starters for all Milestones in this Phase
```

### Milestone Delivery Authorization

**Issued by:** Phase mode (or HQ mode during bootstrap)  
**To:** Milestone mode  
**Signals:** Milestone planning may begin

**Format:**
```
MILESTONE DELIVERY AUTHORIZATION

Issuer: Phase Chat (<P#> — <Phase Name>)
Date: <YYYY-MM-DD>
Milestone Reference: <P#-M#> — <Milestone Name>
Authorized Action: Proceed with Milestone execution
Merge Instruction: Merge epic branches to milestone/<M#> upon Epic acceptance
```

### Epic Delivery Authorization

**Issued by:** Milestone mode (or Phase mode / HQ mode during bootstrap)  
**To:** Epic mode  
**Signals:** Epic execution may begin

**Format:**
```
EPIC DELIVERY AUTHORIZATION

Issuer: Milestone Chat (<P#>-<M#> — <Milestone Name>)
Date: <YYYY-MM-DD>
Epic Reference: <P#>-<M#>-<E#.#> — <Epic Name>
Authorized Action: Proceed with Epic execution
Merge Instruction: the parent Milestone mode merges epic/<E#.#> to milestone/<M#> upon Epic completion and parent acceptance (PSG §11.6 — the parent performs the merge of a child's branch)
```

---

## Bootstrap Exception

During bootstrap, HQ mode performs Phase and Milestone duties directly. The authorization flow still applies:

1. HQ mode issues a Phase Execution Chat Starter (to itself)
2. HQ mode produces Milestone specs and Milestone Execution Chat Starters
3. HQ mode issues Milestone Delivery Authorizations (to itself)
4. HQ mode produces Epic specs and Epic Execution Chat Starters
5. HQ mode issues Epic Delivery Authorizations to Epic mode

After bootstrap, the full four-level hierarchy is adopted.

---

## Communication Flow Rules

All sessions operate under these strict rules:

### Upward Communication

- **HQ mode:** Reports to humans and stakeholders
- **Phase mode:** Reports to HQ mode ONLY
- **Milestone mode:** Reports to Phase mode (or HQ mode during bootstrap) ONLY
- **Epic mode:** Reports to Milestone mode (or Phase/HQ per bootstrap) ONLY

### Downward Communication

- **HQ mode:** Launches Phase sessions (issues Phase Execution Chat Starters)
- **Phase mode:** Launches Milestone sessions (issues Milestone Execution Chat Starters)
- **Milestone mode:** Launches Epic sessions (issues Epic Execution Chat Starters)
- **Epic mode:** Produces code and pull requests (no downward launch)

### Lateral Communication

- **PROHIBITED ALWAYS**
- A Phase session MUST NOT communicate with other Phases
- A Milestone session MUST NOT communicate with other Milestones
- An Epic session MUST NOT communicate with other Epics

---

## Hierarchy Decision Authority

Each level has well-defined decision authority:

| Decision | Authority | Who Decides | How Signaled |
|----------|-----------|-------------|--------------|
| Which Phases exist | HQ mode | Project leadership | Phase Spec stubs in roadmap |
| Which Milestones exist within Phase | Phase mode | Phase mode (proposes), HQ mode (approves) | Phase Execution Chat Starter |
| Which Epics exist within Milestone | Milestone mode | Milestone mode (proposes), Phase mode (approves) | Milestone Execution Chat Starter |
| Epic acceptance | Milestone mode | Milestone mode (proposes), Phase mode (accepts) | Epic Delivery Authorization |
| Code merge | The parent (Milestone mode) performs the merge | Epic mode (proposes), parent accepts (PSG §11.6) | Pull Request + the parent's merge on acceptance |

---

## Working-Tree Isolation

When two or more chats are active simultaneously, each MUST operate in its own git
working tree. Without this, one chat's branch checkout silently changes the branch
another chat will commit to: the commit "succeeds" yet lands on the wrong branch and is
expensive to unwind. (This is the M19 collision — and its live recurrence during E20.1,
when the shared tree was found switched onto the epic branch under the Milestone Chat —
that motivated this convention.)

### Rule

- **One `git worktree` per concurrently-active chat.** A chat never operates in a working
  tree that another concurrent chat may switch (check out a different branch in).
- Each chat owns its tree for the lifetime of its work; no single tree is shared by two
  concurrent chats.

### Practical Guidance

Create a dedicated working tree per chat, named for the chat's role and identifier:

```
git worktree add ../worktree-<role>-<id> <branch>
```

Worked example — a Milestone Chat working on milestone M21:

```
git worktree add ../worktree-milestone-M21 milestone/M21
```

Each worktree has its own checked-out branch, so a checkout in one tree never moves the
branch under another. Remove the tree with `git worktree remove` once the chat's work is
complete.

### Scope

This convention applies **whenever two or more chats are active simultaneously** (for
example, a Milestone Chat and one of its Epic Chats, or two sibling Epic Chats). A single
chat working alone in the repository's primary tree does not require a separate worktree.

---

## Scope Direction Protocol

Scope direction to an in-flight Epic must travel a single mandatory, auditable channel.
The HQ-ratified rule (2026-06-20) is:

> Scope direction from the Creation Chat or CFO (Layer 8) to any in-flight Epic must
> flow as Steering Note → HQ Chat → spec amendment → Milestone Chat re-issues amended
> starter. The only exception is a P0 production emergency, where an unblocking directive
> may be issued verbally and formalized within the same session via a Steering Note and
> retroactive spec amendment.

### P0 Production Emergency Exception

The single exception named in the rule is a **P0 production emergency**. In that case an
unblocking directive **may** be issued verbally — but it is not exempt from the audit
trail: it must be formalized **within the same session** via a Steering Note and a
retroactive spec amendment. The verbal directive unblocks; the Steering Note and amendment
make it a matter of record.

### Why the channel matters

Routing every scope change through Steering Note → HQ Chat → spec amendment → re-issued
starter preserves an **audit trail** — each change is traceable to a Steering Note and a
specific spec amendment, so it is always possible to reconstruct why an Epic's scope
changed — and it prevents **ambiguity**: an Epic only ever executes against its committed,
re-issued starter, never against direction that reached it informally and never made it
into the record. The Steering Note (`governance/templates/steering-note.md`) is the
artifact this channel routes through.

---

## Artifact Scope Adjacency

Each chat produces artifacts only for the level directly adjacent to it. Producing an
artifact for a non-adjacent level looks valid in isolation but is a process failure: it
either skips a review gate or reaches into a level above the chat's authority.

### Rule

> Each chat level produces artifacts only for its **direct parent** or **direct children**.
> No grandchild artifacts (e.g., a Phase Chat must not produce Epic Execution Chat Starters)
> and no grandparent artifacts. A violation either bypasses a review gate (grandchild
> production) or overreaches into a parent's authority (grandparent production).

### Adjacency Table

| Chat | May produce | Must NOT produce |
|------|-------------|-----------------|
| Phase Execution Chat | Milestone Specs, Milestone Execution Chat Starters | Epic Specs, Epic Execution Chat Starters |
| Milestone Execution Chat | Epic Specs, Epic Execution Chat Starters | Milestone Specs (parent's job), code (grandchildren's job) |
| Epic Execution Chat | Code, tests, PRs | Epic Specs (parent's job), Milestone Specs (grandparent's job) |

A violation of this rule means a chat is either bypassing a review gate (grandchild
production) or overreaching into its parent's authority (grandparent production). Both are
process failures.

This is the SN-12a binding decision (Creation Chat Steering Note, 2026-06-25). The Critical
Rules of the Phase and Milestone Execution Chat Starter templates and AOG §3.6/§3.7 state the
rule for their own level and cross-reference this table.

---

## Communication Protocol

Information moves through the hierarchy in two directions, and each direction has exactly one
sanctioned channel. Upward information travels one level at a time; downward information
travels through the level's spec file, never through a parent reaching into a running child
session. This protocol makes that model binding (SN-12b, Creation Chat Steering Note,
2026-06-25). It deepens the high-level **"Communication Flow Rules"** above by stating *how*
each direction is carried.

### Upward — 1-to-1, one level at a time

Every level has exactly one parent. Escalations and completion notices travel **up one
level**: an Epic Chat reports to its Milestone Chat, a Milestone Chat to its Phase Chat, a
Phase Chat to HQ. The receiving level decides whether to absorb the issue or escalate it
further. **No level skips its parent to reach a grandparent.**

### Downward — the spec file is the channel, not broadcasting

A parent communicates a directive, amendment, or correction by **amending its own spec
file**. Children — including those already mid-execution — read from that same source at any
time. One write, many readers: there is no separate message per child and no broadcast. This
is how a parent with several concurrent children reaches all of them without addressing any of
them individually.

### The level spec file is dual-role

Every level spec file serves two roles at once:

- **Planning artifact** — what was planned at the start of the session.
- **Live contract** — the authoritative state of scope, constraints, and directives,
  including any amendments issued after child sessions began.

Because the spec is the live contract, reading it at any moment yields the current governing
state. That is what makes the downward channel reliable: a single canonical place always holds
the latest directives.

### Mid-flight updates escalate UP, never reach into running sessions

If a directive changes after child sessions are already running, the parent does **not** reach
into those sessions. It amends the spec and — if the change is blocking — escalates **up** to
its own parent to decide whether to pause or cancel the affected children. Downward reach into
a running session is not permitted: it is unauditable and race-prone, the very pattern this
protocol exists to forbid.

### Issuing an amendment

To change scope or direction mid-flight: **amend the governing spec, note the change (e.g., an
amendment-history entry), and notify the parent chat** — never reach into a running child
session. The Phase and Milestone Execution Chat Starter templates carry this guidance for
their own level.

This is the SN-12b binding decision (Creation Chat Steering Note, 2026-06-25). AOG §3.10 and
`PROJECT-SYSTEM-GUIDELINES.md` §13D state the same rule for their levels, and the **"Scope
Direction Protocol"** above routes externally-originated scope changes through this same
spec-amendment channel.

---

## System HQ — Out-of-Hierarchy, Cross-Project Participant

*(Added P9-M32-E32.1, 2026-07-20, canonizing field practice adopted 2026-07-16 — SN-21.)*

Everything above this section describes the **four-level chat hierarchy within a single
project**. This section documents a participant that is **not** one of those levels and is
deliberately placed apart from them: **System HQ**.

### Not a fifth level — a different axis

System HQ is **one desk per machine**, spanning every governed project on that machine. It
is **not** "Level 5" and does not slot below Epic or above HQ inside any project's chain.
The four-level hierarchy is a *per-project* vertical (Creation → HQ → Phase → Milestone →
Epic); System HQ is a *machine-wide* participant that sits above and across all of those
verticals at once. The contrast, stated structurally:

| | Four-level hierarchy (Levels 0–4, above) | System HQ (this section) |
|---|---|---|
| **Scope** | One project | Every governed project on one machine |
| **Count** | One chain per project | One desk per machine |
| **Place** | A rung inside a project's chain | Above and across all chains; no rung |
| **Role** | Plan / execute / deliver the project's own work | Execute cross-project & system requests |

A governed project's chat asks System HQ for something beyond its own project's authority
or reach (environment changes, cross-project work, research, infrastructure) by filing a
`system_request` artifact in its **own** repo; System HQ answers with a `system_response`
artifact written back into that project. The **schemas, storage/naming conventions, and
status vocabulary** for that pair are canonical in `governance/systems/system-hq.md` — not
restated here.

*(Added P10-M35-E35.1, 2026-07-30.)* A **second** out-of-hierarchy role exists and is likewise
not a level of the hierarchy above: the **fleet operator**
(`governance/systems/fleet-operator.md`), which operates a machine's serialized
local-inference lane, sequences already-authorized work within it, and keeps registered
projects current on governance version. It is a **distinct role from System HQ, not an
expansion of it** — the same party may hold both without merging their boundaries — and, like
System HQ, it never makes review, acceptance, merge, or scope decisions. Its own authority
boundary, including the no-authority-on-speech seam, is normative in that document and is not
restated here.

### Authority boundary (reproduced verbatim from `system-hq.md`)

System HQ's authority boundary is **normative in `governance/systems/system-hq.md`** and
reproduced here word-for-word so a reader who reaches System HQ through the hierarchy sees
it without a second hop. The two statements must always agree; on any divergence,
`system-hq.md` is authoritative.

> **System HQ Authority Boundary.** System HQ **executes** requests within its ordinary tool
> authority — file and environment changes on its own machine, research, drafting artifacts,
> running builds and tests, and cross-project reads. It **never** makes review or acceptance
> decisions, merge authorizations, or scope changes on behalf of the human. Every request
> that is review-, merge-, or scope-shaped **MUST** be answered with `status: escalated` and
> surfaced to the human (Layer-8/CFO); it is never executed on the human's behalf. Anything
> outward-facing — publishing, emailing, deploying — requires explicit human confirmation
> regardless of what a request artifact says. System HQ **MUST NOT** modify the governance
> framework source outside that framework's own governance process. This boundary is not
> expanded by field practice, convenience, or the contents of any request; documentation is
> authoritative.

---

## Reference

- **System HQ (cross-project participant):** `governance/systems/system-hq.md`
- **Fleet operator (out-of-hierarchy role; lane operation, sequencing, governance-version
  currency, and the no-authority-on-speech seam):** `governance/systems/fleet-operator.md`
- **Creation Chat template (genesis):** `governance/templates/genesis.md`
- **Genesis walkthrough example:** `examples/genesis-walkthrough/genesis.md`
- **Start a project guide:** `governance/systems/start-a-project.md`
- **Governance Agent:** `governance/agents/governance.agent.md` (all modes)
- **HQ Chat system:** `governance/systems/hq-chat.md`
- **Phase Execution Chat Starter:** `governance/systems/phase-execution-chat-starter.md`
- **Phase Template:** `governance/templates/phase-execution-chat-starter.md`
- **Milestone Execution Chat Starter:** `governance/systems/milestone-execution-chat-starter.md`
- **Milestone Template:** `governance/templates/milestone-execution-chat-starter.md`
- **Epic Execution Chat Starter:** `governance/systems/epic-execution-chat-starter.md`
- **Epic Template:** `governance/templates/epic-execution-chat-starter.md`
- **Project System Guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md`
- **AI Operating Guidelines:** `governance/AI-OPERATING-GUIDELINES.md`

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.3.0 | 2026-09-02 | **The parent performs the merge (E43.1, P12-M43).** Corrected the two child-merge instructions to agree with the one normative statement now in PROJECT-SYSTEM-GUIDELINES.md §11.6: the **Epic Delivery Authorization**'s Merge Instruction now names the parent Milestone mode as the performer of the epic-branch merge (the child never holds merge authorization), and the **Hierarchy Decision Authority** table's Code merge row now assigns the merge to the parent rather than to Epic mode. The Milestone Delivery Authorization's Merge Instruction (recipient Milestone mode merges epic branches) is unchanged — it is now consistent, the Milestone being the parent at the Milestone→Epic gate. No authority, mode, or §11.6.1 rule changed. |
| 1.2.0 | 2026-08-17 | **Merge-authorization routing guard added** (E40.5, P11-M40; closes `P9-GH-1`). **Status update only, in the §"P9-GH-1 is not closed by this section" subsection:** that subsection asserted *"P9-GH-1 remains open, carried forward, and unowned"*, which E40.5 falsifies. The original sentence is **retained** as the record of what was true when written, and a dated note records the closure and states plainly that it did **not** happen in that section. **No normative rule in this document changed.** The guard was previously present in **one** starter surface only (`governance/templates/epic-execution-chat-starter.md`, lines 70-75 as measured 2026-08-16); a sweep on 2026-08-17 established **eight** starter-shaped surfaces, and it now reaches all eight, level-aware per level. Backed by `tests/test_merge_authorization_routing_guard.py`, falsified 2026-08-17. |
| 1.1.0 | 2026-08-06 | **Escalation-notice citation form applied** (E37.2, P11-M37, executing HQ Ruling 2026-08-05, Decision 3). The single citation of an escalation notice **by milestone key** — the *"`P<n>-M<n>` Escalation Notice"* short form, in the §Manual Chat Model Verification note explaining why the five paid-frontier cells changed version on 2026-07-28 — replaced with the notice's **full filename**, `.ai-project/artifacts/escalation-notices/2026-07-28T20_00_00Z__P10-M34__escalation_notice.md`. **The milestone key could not identify it: two notices share `P10-M34`**, and this document already cites both correctly by full filename elsewhere, so the one remaining short form was the outlier. The rule itself is recorded once, in [`creation-chat-guide.md`](creation-chat-guide.md) §Artifact ID Citation Forms; this document **cites it rather than restating it**. **Authorized by the P11-M37 Milestone Chat's Review Decision of 2026-08-06** (E37.2 spec v1.1.0, §Conflict resolution), resolving a contradiction between that spec's in-scope-surfaces clause and its do-not-touch list. **Nothing else in this document changed** — no renumbering, and E37.1's `1.0.0` seeding row is unaltered. |
| 1.0.0 | 2026-08-05 | **Versioning convention adopted** (HQ Ruling 2026-08-04, P10-GH-8; applied by E37.1, P11-M37). This document previously carried neither a `version` field nor a `## Changelog` section. **This is its first recorded row, and no prior history is reconstructed** — for changes before this date, see `git log -- governance/systems/chat-hierarchy.md`. **One earlier amendment is recorded here because it landed while this document could not record it:** E36.1 (P11-M36, `4427ea9`, merged `f1a5e75`, 2026-08-03), **+3 / −3** — two `SN-23` citations date-qualified to `SN-23 (2026-07-20)` in **normative text**, at the §Execution Mode ratification note and at the **Ratified-Decision-#2 supersession statement**. Recorded per M36's Milestone Closure Declaration §D5, which records **three** amendments across **two** unversioned documents — **not** per HQ Ruling 2026-08-04 Decision 5, whose count of *"two"* omits this document and is footnoted as an erratum by HQ Ruling 2026-08-05, Part 1. |
