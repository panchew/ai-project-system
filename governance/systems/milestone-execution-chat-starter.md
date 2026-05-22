---
type: system
status: active
effective_date: 2026-04-23
---

# Milestone Execution Chat Starter — System Reference

## Purpose

This document defines the role, responsibilities, and operating rules for a Milestone Execution Chat session in the AI Project System.

A Milestone Execution Chat Starter is the governance artifact that launches a Milestone Chat. It is produced by a Phase Chat (or HQ Chat during bootstrap), delivered to the Milestone Chat session, and constitutes the binding execution contract for the session.

---

## What a Milestone Chat Is

A **Milestone Chat** is a planning session scoped to a single Milestone. It is:

- **Finite in duration** — it opens with a Milestone Execution Chat Starter and closes when all Epic Chat Starters are produced and accepted by the parent Phase Chat (or HQ Chat)
- **Launched from a Phase Chat** — using the Milestone Execution Chat Starter template (`governance/templates/milestone-execution-chat-starter.md`)
- **Scoped to a single Milestone** — it does not span multiple milestones or phases outside its Milestone
- **Read-only with respect to the project** — it does NOT execute work; it plans and produces planning artifacts

A Milestone Chat has read access to:
- The Milestone spec
- All Epic stubs within the Milestone

A Milestone Chat does NOT have write authority over the project repository. All file creation during a Milestone Chat session is performed by the Coding Agent acting on the Milestone Chat's instructions as deliverables committed to the repository.

---

## Responsibilities

The following is the exhaustive list of Milestone Chat responsibilities:

1. **Review the Milestone spec** — confirm it is complete, actionable, and consistent with governance
2. **Produce Epic specs** — create an Epic spec file for every Epic stub within the Milestone; these are deliverables committed by the Coding Agent
3. **Produce Epic Execution Chat Starters** — create a filled-in Epic Execution Chat Starter for each Epic within the Milestone
4. **Return deliverables to the parent chat** — all produced artifacts are returned to the Phase Chat (or HQ Chat) for review and acceptance
5. **Issue Epic Delivery Authorization** — when the parent chat accepts an Epic's deliverables, the Milestone Chat issues an Epic Delivery Authorization artifact authorizing the Coding Agent to proceed with that Epic

A Milestone Chat MUST complete all responsibilities before declaring the session closed.

---

## Communication Scope

Milestone Chat communication is strictly bounded:

| Direction | Permitted | Notes |
|-----------|-----------|-------|
| Upward | Phase Chat (or HQ Chat during bootstrap) only | Reports progress, returns deliverables, requests decisions |
| Downward | Coding Agents only | Issues Epic Execution Chat Starters and Epic Delivery Authorizations |
| Lateral | PROHIBITED | A Milestone Chat MUST NOT reach across to sibling milestones or phases |

**Rule:** A Milestone Chat MUST NOT communicate with or reference work belonging to another Milestone. If cross-milestone dependencies are discovered, the Milestone Chat escalates to the parent chat (Phase Chat or HQ Chat).

---

## What a Milestone Chat Is NOT

- ❌ **Not a Coding Agent** — it does not branch, commit, or open PRs directly
- ❌ **Not a substitute for Phase Chat or HQ Chat authority** — the parent chat owns accept/reject decisions; Milestone Chat produces proposals only
- ❌ **Not a place where branches are created or files are directly modified** — the Coding Agent executes those actions on the Milestone Chat's behalf
- ❌ **Not a persistent session** — it closes when all Epic Chat Starters are produced and accepted by the parent chat
- ❌ **Not an execution chat** — it produces planning artifacts, not code or implementation

---

## Governance Authority Chain

Within a Milestone Chat session, the following hierarchy governs all decisions:

1. `PROJECT-SYSTEM-GUIDELINES.md` (highest authority)
2. `AI-OPERATING-GUIDELINES.md`
3. Milestone Execution Chat Starter (the instance that launched this session)
4. Milestone Spec
5. Decisions made during the session
6. System references
7. Chat messages (lowest authority)

Documentation is authoritative. Chat is ephemeral. Any conflict between a chat statement and a governance document is resolved in favor of the governance document.

---

## Epic Delivery Authorization

When the parent chat (Phase Chat or HQ Chat) accepts an Epic's deliverables, the Milestone Chat issues an **Epic Delivery Authorization** artifact.

The Epic Delivery Authorization is the signal to the Coding Agent that the Epic's planning artifacts are accepted and Epic execution may begin.

### Required Format

The Epic Delivery Authorization is a structured block with the following fields:

```
EPIC DELIVERY AUTHORIZATION

Issuer: Milestone Chat (<P#>-<M#> — <Milestone Name>)
Date: <YYYY-MM-DD>
Epic Reference: <P#>-<M#>-<E#.#> — <Epic Name>
Authorized Action: Proceed with Epic execution
Merge Instruction: Merge epic/<E#.#> to milestone/<M#> upon Epic completion and parent acceptance
```

### Authority Rules

- **Only HQ Chat, Phase Chat, or Milestone Chat may issue Epic Delivery Authorizations.**
- A Coding Agent MUST NOT self-authorize Epic execution.
- The Epic Delivery Authorization MUST be issued before a Coding Agent begins.

---

## Session Lifecycle

A Milestone Chat session follows this sequence:

1. **Open** — receive the Milestone Execution Chat Starter from Phase Chat or HQ Chat
2. **Review** — confirm the Milestone spec exists and is complete
3. **Plan** — produce Epic specs and Epic Execution Chat Starters for all Epics
4. **Return** — deliver all artifacts to parent chat for review
5. **Authorize** — for each accepted Epic, issue an Epic Delivery Authorization
6. **Close** — declare the session closed after all Epics are authorized

**If the Milestone spec is missing or incomplete:** STOP. Report the issue to the parent chat. Do not proceed with planning.

---

## Reference

- **Agent definition:** `governance/agents/governance.agent.md` (Milestone mode)
- **System document:** `governance/systems/milestone-execution-chat-starter.md` (this file)
- **Template:** `governance/templates/milestone-execution-chat-starter.md`
- **Parent mode:** Phase mode (in `governance/agents/governance.agent.md`)
- **Parent system:** `governance/systems/phase-execution-chat-starter.md`
- **Child system:** `governance/systems/epic-execution-chat-starter.md`
- **Hierarchy reference:** `governance/systems/chat-hierarchy.md`
- **Governing guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md` §13B
- **Delivery wrapping rule:** `governance/AI-OPERATING-GUIDELINES.md` §3.1.1
