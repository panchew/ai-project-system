---
type: system
status: active
effective_date: 2026-07-20
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
| `phase` | `remote:claude-opus-5` | Phase | Existing key. Policy row P3. |
| `milestone` | `remote:claude-opus-5` | Milestone | Existing key. Policy row P4. |
| `epic_manual` | `remote:claude-opus-5` | Epic (manual) | New key (this Epic), distinct from the `epic_dev`/`epic_qa` agentic-dispatch lanes those keys serve. Policy row P5's general "epic × execution: paid frontier" default — P6/P7's local-offload values apply only when the agentic Dev/QA dispatch lanes are actually in use, which a manual Epic chat, by definition, is not. |

**Values are versions; the decision behind them is a tier.** These five cells named
`remote:claude-opus-4-8` until 2026-07-28, when that version stopped being offered in the
harness surface in use and this guardrail — correctly — halted every manual chat at once
(P10-M34 Escalation Notice). HQ refreshed all five to `remote:claude-opus-5`, the same
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

#### Mismatch: refuse, unconditionally

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
Merge Instruction: Merge epic/<E#.#> to milestone/<M#> upon Epic completion and parent acceptance
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
| Code merge | Epic mode | Epic mode (proposes), HQ mode (approves) | Pull Request + explicit authorization |

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
