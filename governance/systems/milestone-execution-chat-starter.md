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

## Issuing Review Decisions — Worked Examples (P4.1)

A Review Decision is the binding accept/reject artifact you issue after reading a
Completion Notice. It is committed to the repository — a decision made only in chat is
not authoritative. Use the template `governance/templates/review-decision.md`.

### Example — Review Decision (ACCEPT)

```markdown
---
artifact_type: review_decision
artifact_version: 1.0
timestamp: 2026-06-17T15:00:00Z
issuer_chat: Milestone Agent (P4-M17)
issuer_role: Milestone Agent
decision: accept
epic_id: P4-M17-E17.1
milestone_id: P4-M17
phase_id: P4
completion_notice_timestamp: 2026-06-17T00:00:00Z
authorization:
  action: merge
  merge_instruction: Merge PR #73 to milestone/M17; delete epic/P4-M17-E17.1 after merge.
---

# Review Decision: P4-M17-E17.1 — Fix Daemon Orchestrator Path Resolution

## Decision: ACCEPT ✓

## Feedback
Spec compliance confirmed and independently verified: 17 new tests, full suite green,
no regression. Root cause analysis correct. Authorized to merge.

## Authorization
Merge PR #73 to milestone/M17 using squash-and-merge, then delete the epic branch.
```

### Example — Review Decision (REJECT)

```markdown
---
artifact_type: review_decision
artifact_version: 1.0
timestamp: 2026-06-17T15:00:00Z
issuer_chat: Milestone Agent (P4-M17)
issuer_role: Milestone Agent
decision: reject
epic_id: P4-M17-E17.9
milestone_id: P4-M17
phase_id: P4
completion_notice_timestamp: 2026-06-17T14:00:00Z
authorization:
  action: rework
  merge_instruction: null
---

# Review Decision: P4-M17-E17.9 — Example Rejected Epic

## Decision: REJECT ✗

## Feedback
Rework required before this can merge:
1. **Test coverage:** 62% — spec requires 80%. Add error-path tests.
2. **CI:** 3 linter checks failing. Fix all before resubmission.
3. **Scope:** PR touches files outside the Epic spec. Remove them or escalate.

## Authorization
Not authorized to merge. Address the items above, create a new Completion Notice
(v1.1), and resubmit. This counts as attempt 1 of 3 (see Rework Cycle below).
```

---

## Rework Cycle (P4.1)

When you issue a **Reject**, the Epic enters the rework cycle:

1. The Epic Agent reads your feedback and addresses every item.
2. It produces a **new Completion Notice** (increment the version: v1.1, v1.2, …) and
   resubmits.
3. You review again and issue a fresh Review Decision.

**Maximum 3 attempts.** If a third Completion Notice is still not acceptable, do **not**
issue a fourth rejection-and-retry. Instead the Epic Agent produces an **Escalation
Notice** and you escalate to the Phase Chat (see [Escalation Path](#escalation-path)).

The 3-attempt limit resets only if you explicitly grant an extension in writing (as an
artifact or a recorded decision). Silent fourth attempts are a governance violation.

```
Reject → Epic reworks → new Completion Notice (vN) → re-review
   (attempt 1) → (attempt 2) → (attempt 3) → STILL failing? → Escalation Notice → Phase Chat
```

---

## Escalation Path (P4.1)

Escalate **upward to the Phase Chat** (never laterally) when you hit something you
cannot resolve within your Milestone authority:

| Trigger | Why it escalates |
|---------|------------------|
| 3 rework attempts exhausted | The Epic cannot complete as specified |
| Out-of-scope finding | The fix requires work beyond this Milestone's scope |
| Missing or contradictory spec | You cannot author a correct Epic spec / review against it |
| Cross-milestone dependency | Resolution belongs above your Milestone (lateral contact is prohibited) |
| Authority conflict | A decision exceeds Milestone authority (e.g., production, Phase scope) |

To escalate, produce an **Escalation Notice** using
`governance/templates/escalation-notice.md`: state the blocker, what you already tried,
the decision you need, and the impact (who/what is blocked). Commit it and submit it to
the Phase Chat. Do not proceed on the blocked path until the Phase Chat responds.

**Reference:** Escalation Notice template `governance/templates/escalation-notice.md`;
[Troubleshooting Guide](../../docs/team-collaboration/troubleshooting-guide.md) for
escalation problems; [Phase Lead Guide](../../docs/team-collaboration/phase-lead-guide.md).

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
  - Merge Authorization template: `governance/templates/merge-authorization.md`
  - Epic Closure Notice template: `governance/templates/epic-closure-notice.md`
  - Escalation Notice template: `governance/templates/escalation-notice.md`
- **Parent system:** `governance/systems/hq-execution-chat-starter.md` (HQ level)
- **P4 entry point:** [P4 Governance System Guide](../../docs/team-collaboration/P4-governance-system-guide.md)
- **Governing guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md` §13B
- **Delivery wrapping rule:** `governance/AI-OPERATING-GUIDELINES.md` §3.1.1
