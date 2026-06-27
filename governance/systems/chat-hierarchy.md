---
type: system
status: active
effective_date: 2026-04-23
---

# Chat Hierarchy — System Reference

## Purpose

This document provides the single authoritative end-to-end reference for the complete AI Project System chat hierarchy. Readers can understand the full four-level chain, artifact responsibilities, and authorization flow without reading all four individual system documents.

---

## The Four-Level Chat Hierarchy

The AI Project System organizes governance and execution across four levels, each with distinct roles and responsibilities. All four levels are served by a single **Governance Agent** (`governance/agents/governance.agent.md`) that self-configures its mode based on the Chat Starter delivered.

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

## Level 0: Creation Chat (Project Bootstrap)

The Creation Chat is the **entry point** for a new project — the step before the four-level hierarchy begins. It runs once per project, immediately after `ai-project init`, and exists to turn a project brief into the single artifact that lets a Phase Chat open: a committed `genesis.md`. It is not one of the Governance Agent's four execution modes; it is a one-time bootstrap session (a human or an AI agent acting as Creation Chat).

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

- **Template:** `governance/templates/genesis.md`
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

## Reference

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
