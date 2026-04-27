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

The AI Project System organizes governance and execution across four levels, each with distinct roles and responsibilities:

```
HQ Chat
 │
 ├─ produces → Phase Execution Chat Starter
 │
 └─ Phase Chat (plans milestones)
     │
     ├─ produces → Milestone Execution Chat Starter
     │
     └─ Milestone Chat (plans epics)
         │
         ├─ produces → Epic Execution Chat Starter
         │
         └─ Coding Agent (executes epic work)
             │
             └─ produces → PR, commit, deliverables
```

---

## Hierarchy Summary Table

| Level | Chat/Agent | Launched By | Consumes | Produces | Issues | Scope |
|-------|-----------|-------------|----------|----------|--------|-------|
| **1 — Project** | HQ Chat | (bootstrap) | Phase Spec stubs | Phase Execution Chat Starters | Phase Delivery Authorization | All Phases |
| **2 — Phase** | Phase Chat | HQ Chat | Phase Execution Chat Starter | Milestone Specs, Milestone Execution Chat Starters | Milestone Delivery Authorization | Single Phase |
| **3 — Milestone** | Milestone Chat | Phase Chat (or HQ) | Milestone Execution Chat Starter | Epic Specs, Epic Execution Chat Starters | Epic Delivery Authorization | Single Milestone |
| **4 — Epic** | Coding Agent | Milestone Chat | Epic Execution Chat Starter | Code, commits, PR | (Deliverables for review) | Single Epic |

---

## Level 1: HQ Chat

### Role

HQ Chat is the project-level governance and planning session. It:
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

- **System reference:** `governance/systems/hq-chat.md`
- **Governing guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md` §12

---

## Level 2: Phase Chat

### Role

Phase Chat is a planning session scoped to a single Phase. It:
- Opens with a Phase Execution Chat Starter from HQ Chat
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

- **System reference:** `governance/systems/phase-execution-chat-starter.md`
- **Template:** `governance/templates/phase-execution-chat-starter.md`
- **Governing guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md` §13A

---

## Level 3: Milestone Chat

### Role

Milestone Chat is a planning session scoped to a single Milestone. It:
- Opens with a Milestone Execution Chat Starter from Phase Chat (or HQ Chat)
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

- **System reference:** `governance/systems/milestone-execution-chat-starter.md`
- **Template:** `governance/templates/milestone-execution-chat-starter.md`
- **Governing guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md` §13B

---

## Level 4: Coding Agent

### Role

Coding Agent is an execution session scoped to a single Epic. It:
- Opens with an Epic Execution Chat Starter from Milestone Chat
- Executes all Definition of Done items
- Produces code, commits, and pull requests
- Creates a Completion Report
- Requests human review
- Responds to HQ Chat (either directly or via Phase/Milestone Chat per bootstrap mode)

### What It Consumes

- Epic Execution Chat Starter (from Milestone Chat)
- Epic spec
- Existing codebase and project context

### What It Produces

- **Code and commits** — implementation of all DoD items
- **Pull request** — proposed merge to the target branch
- **Completion Report** — structured summary of deliverables
- **Epic Review Seal** (structured) — findings for human review

### What It Issues

- (No authorization artifacts — Coding Agents execute on received authorization)

### Communication Rules

- Reports to Milestone Chat (or Phase Chat / HQ Chat per bootstrap)
- Does NOT communicate laterally or upward to other chats
- Awaits explicit authorization before beginning work

### Documentation

- **System reference:** `governance/systems/epic-execution-chat-starter.md`
- **Template:** `governance/templates/epic-execution-chat-starter.md`
- **Governing guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md` §13

---

## Authorization Artifacts

All execution transitions are gated by structured authorization artifacts. Only these three authorization types exist:

### Phase Delivery Authorization

**Issued by:** HQ Chat  
**To:** Phase Chat  
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

**Issued by:** Phase Chat (or HQ Chat during bootstrap)  
**To:** Milestone Chat  
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

**Issued by:** Milestone Chat (or Phase Chat / HQ Chat during bootstrap)  
**To:** Coding Agent  
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

During P2 bootstrap (M6), HQ Chat performs Phase Chat and Milestone Chat duties directly. The authorization flow still applies:

1. HQ Chat issues a Phase Execution Chat Starter (to itself)
2. HQ Chat produces Milestone specs and Milestone Execution Chat Starters
3. HQ Chat issues Milestone Delivery Authorizations (to itself)
4. HQ Chat produces Epic specs and Epic Execution Chat Starters
5. HQ Chat issues Epic Delivery Authorizations to Coding Agents

After bootstrap, the full four-level hierarchy is adopted.

---

## Communication Flow Rules

All chats and agents operate under these strict rules:

### Upward Communication

- **HQ Chat:** Reports to humans and stakeholders
- **Phase Chat:** Reports to HQ Chat ONLY
- **Milestone Chat:** Reports to Phase Chat (or HQ Chat during bootstrap) ONLY
- **Coding Agent:** Reports to Milestone Chat (or Phase/HQ per bootstrap) ONLY

### Downward Communication

- **HQ Chat:** Launches Phase Chats (issues Phase Execution Chat Starters)
- **Phase Chat:** Launches Milestone Chats (issues Milestone Execution Chat Starters)
- **Milestone Chat:** Launches Coding Agents (issues Epic Execution Chat Starters)
- **Coding Agent:** Produces code and pull requests (no downward launch)

### Lateral Communication

- **PROHIBITED ALWAYS**
- A Phase Chat MUST NOT communicate with other Phases
- A Milestone Chat MUST NOT communicate with other Milestones
- A Coding Agent MUST NOT communicate with other Epics

---

## Hierarchy Decision Authority

Each level has well-defined decision authority:

| Decision | Authority | Who Decides | How Signaled |
|----------|-----------|-------------|--------------|
| Which Phases exist | HQ Chat | Project leadership | Phase Spec stubs in roadmap |
| Which Milestones exist within Phase | Phase Chat | Phase Chat (proposes), HQ Chat (approves) | Phase Execution Chat Starter |
| Which Epics exist within Milestone | Milestone Chat | Milestone Chat (proposes), Phase Chat (approves) | Milestone Execution Chat Starter |
| Epic acceptance | Milestone Chat | Milestone Chat (proposes), Phase Chat (accepts) | Epic Delivery Authorization |
| Code merge | Coding Agent | Coding Agent (proposes), HQ Chat (approves) | Pull Request + explicit authorization |

---

## Reference

- **HQ Chat:** `governance/systems/hq-chat.md`
- **Phase Execution Chat Starter:** `governance/systems/phase-execution-chat-starter.md`
- **Phase Template:** `governance/templates/phase-execution-chat-starter.md`
- **Milestone Execution Chat Starter:** `governance/systems/milestone-execution-chat-starter.md`
- **Milestone Template:** `governance/templates/milestone-execution-chat-starter.md`
- **Epic Execution Chat Starter:** `governance/systems/epic-execution-chat-starter.md`
- **Epic Template:** `governance/templates/epic-execution-chat-starter.md`
- **Project System Guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md`
- **AI Operating Guidelines:** `governance/AI-OPERATING-GUIDELINES.md`
