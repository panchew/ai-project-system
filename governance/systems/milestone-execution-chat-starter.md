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

## Handling Completion Notices from Epics (P4.1)

**New in P4.1:** When Epic Execution Chats finish their work, they produce **Completion Notices** (structured YAML + markdown artifacts) and submit them to you for review and decision.

### What a Completion Notice Is

A Completion Notice is a structured artifact that signals an Epic has finished and is ready for parent (Milestone) review. It includes:
- Deliverables (spec, implementation, tests, PR)
- QA status (tests passed, code review ready, Definition of Done met)
- PR details (number, URL, target branch)
- Any blockers or risks

**Reference:** `governance/systems/artifact-communication-protocol.md` (P4.1)

### Your Responsibilities

1. **Receive** Completion Notices from Epic Agents as they finish work
2. **Review** each Completion Notice for spec compliance, QA status, and PR readiness
3. **Decide** whether to Accept or Reject by issuing a **Review Decision** artifact
4. **Aggregate** all Epic Completion Notices into a **Milestone Completion Notice** when all Epics are done

### Workflow

```
Epic Agent finishes
  ↓
Epic produces Completion Notice
  ↓
Milestone Chat receives it
  ↓
You review Completion Notice
  ↓
Issue Review Decision (Accept or Reject)
  ↓
If Accept: Epic proceeds to merge, produces Delivery Notice
If Reject: Epic reworks, resubmits new Completion Notice
```

### Review Criteria (Accept or Reject)

**Accept if:**
- ✓ Spec compliance confirmed (implementation matches Epic spec)
- ✓ Tests passing (all tests pass, coverage meets DoD requirements)
- ✓ Code review ready (linting, style, documentation complete)
- ✓ PR is against the correct target branch (milestone/M#)
- ✓ All Definition of Done items are satisfied

**Reject if:**
- ✗ Spec mismatch (implementation deviates from Epic spec)
- ✗ Tests failing or insufficient coverage
- ✗ Code review issues (linting, documentation, style problems)
- ✗ PR against wrong branch or not created yet
- ✗ Missing Definition of Done items

### Issuing a Review Decision

When you review a Completion Notice, issue a **Review Decision** artifact using this template:

**Template:** `governance/templates/review-decision.md`

**Format:**
```markdown
---
artifact_type: review_decision
artifact_version: 1.0
timestamp: 2026-05-29T15:00:00Z
issuer_chat: Milestone Agent (P#-M#)
decision: accept  # or "reject"
epic_id: P#-M#-E#.#
...
---

# Review Decision: P#-M#-E#.# — Epic Name

## Decision: ACCEPT ✓

## Feedback
<Your review notes>

## Authorization
If Accept: Authorize the Epic to merge.
If Reject: Explain required changes.
```

### Aggregating into Milestone Completion Notice

When **all Epics** in the Milestone are complete (have received Accept decisions), you produce a **Milestone Completion Notice** to report the entire Milestone's completion to the parent Phase Chat.

**Same artifact type, but scoped to Milestone level:**
```markdown
---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: 2026-05-29T17:00:00Z
issuer_chat: Milestone Agent (P#-M#)
status: ready_for_review
milestone_id: P#-M#
phase_id: P#
deliverables:
  - name: Milestone Spec
    path: docs/phases/.../M#__spec__Milestone_Name.md
  - name: 3 Epic Specs
    path: docs/phases/.../M#__Milestone/
  - name: All Epic Implementations
    path: src/
---

# Completion Notice: P#-M# — Milestone Name

## Summary
Milestone M# is complete. All 3 Epics delivered and merged.

## Deliverables
- Milestone spec
- 3 Epic specs
- All Epic implementations
- All Epic tests passing

## Quality Assurance
- Tests: passed (all Epics)
- Code Review: ready (all Epics)
- Definition of Done: ✓ all items met

...
```

Then the parent Phase Chat reviews and issues a Review Decision at the Milestone level.

---

## Session Lifecycle

A Milestone Chat session follows this sequence:

1. **Open** — receive the Milestone Execution Chat Starter from Phase Chat or HQ Chat
2. **Review** — confirm the Milestone spec exists and is complete
3. **Plan** — produce Epic specs and Epic Execution Chat Starters for all Epics
4. **Return** — deliver all artifacts to parent chat for review
5. **Authorize** — for each accepted Epic, issue an Epic Delivery Authorization
6. **Execute** — receive Completion Notices from Epic Agents as they finish work
7. **Review** — issue Review Decisions (Accept or Reject) for each Completion Notice
8. **Aggregate** — when all Epics complete, produce Milestone Completion Notice
9. **Close** — declare the session closed after parent Phase Chat accepts Milestone Completion Notice

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
- **Artifact Protocol (P4.1):** `governance/systems/artifact-communication-protocol.md`
  - Completion Notice template: `governance/templates/completion-notice-epic.md`
  - Review Decision template: `governance/templates/review-decision.md`
  - Delivery Notice template: `governance/templates/delivery-notice.md`
- **Governing guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md` §13B
- **Delivery wrapping rule:** `governance/AI-OPERATING-GUIDELINES.md` §3.1.1
