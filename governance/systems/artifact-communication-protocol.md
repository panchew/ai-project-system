---
type: system
status: active
effective_date: 2026-05-29
version: 1.0.0
---

# Artifact Communication Protocol (P4.1)

## Purpose

This document defines the canonical artifact formats and communication rules for structured, predictable handoffs between governance chats in the AI Project System.

**Problem Solved:** Manual mode previously required human copy-paste between chats, creating transcription errors and breaking audit trails. Agentic mode had no standard for parent-child artifact exchange.

**Solution:** Three canonical artifacts with standardized frontmatter (YAML) + markdown body. Every chat produces these when appropriate, and parent chats consume them for decisions.

**Benefit:** 
- Automation-ready: chats can parse YAML frontmatter programmatically
- Human-readable: markdown body explains context
- Audit trail: every handoff is recorded
- No transcription: artifacts flow directly between chats
- CFO-friendly: Layer-8 sees predictable completion/review/delivery artifacts from all projects

---

## Core Principles

1. **Artifact-First Communication** — Every chat-to-chat handoff uses one of the three canonical artifacts
2. **Frontmatter + Body** — YAML frontmatter for machine parsing, markdown body for human context
3. **Reference Integrity** — Every artifact includes parent_id, child_id, epic_id, milestone_id, phase_id as appropriate
4. **One Way Per Direction** — Completion flows up, Review Decision flows down, Delivery closes the cycle
5. **Immutability** — Once an artifact is created, it is archived; modifications create a new versioned artifact
6. **Terminal States** — A chat declares completion via artifact, parent accepts/rejects via artifact, delivery finalizes via artifact

---

## Artifact Types

### 1. Completion Notice (Epic → Milestone, Milestone → Phase, Phase → HQ)

**Trigger:** Epic/Milestone/Phase declares work finished, submits for parent review.

**Direction:** Upward (child → parent)

**Purpose:** Signal readiness for parent acceptance. Parent must explicitly accept or reject.

#### Structure

```markdown
---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: <ISO-8601 UTC>
issuer_chat: <chat_type> (<full_reference>)
issuer_role: Epic|Milestone|Phase Agent
status: ready_for_review
epic_id: <P#-M#-E#.#>
milestone_id: <P#-M#>
phase_id: <P#>
project_name: <name>
deliverables:
  - name: <artifact_name>
    path: <repo_path>
    type: spec|implementation|report|pr
    status: ready
  - name: ...
    ...
blockers: []  # or list of {description, severity: critical|warning}
qa_status: passed|failed|blocked  # final QA loop result
pr_details:
  number: <PR number or "pending">
  title: <PR title>
  target_branch: <target branch>
  url: <GitHub URL or "not_created_yet">
---

# Completion Notice: <P#-M#-E#.#> — <Epic Name>

## Summary
<Brief executive summary of what was delivered (2-3 sentences)>

## Deliverables
<List of what was created/modified, with paths and status>

## Quality Assurance
- Tests: <passed/failed/n/a>
- Code Review: <ready/pending/issues>
- Definition of Done: <✓ all items met / ✗ items pending>

## Blockers or Risks
<Any outstanding issues that may affect acceptance>

## Ready for Parent Review
This Epic is complete and submitted for <Milestone|Phase|HQ> Chat review and acceptance.

**Next Action:** Parent Chat reviews this artifact, then issues either:
- **Review Decision (Accept)** → allows merge
- **Review Decision (Reject)** → requires rework
```

#### Examples

**Epic Completion Notice:**
```markdown
---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: 2026-05-29T14:32:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: my-project
deliverables:
  - name: Epic Spec
    path: docs/phases/P1__Phase_Name/M1__Milestone/E1.1__spec__Feature_Name.md
    type: spec
    status: ready
  - name: Implementation
    path: src/features/feature-name.ts
    type: implementation
    status: ready
  - name: Tests
    path: tests/features/feature-name.test.ts
    type: implementation
    status: ready
  - name: Pull Request
    path: pull/428
    type: pr
    status: ready
blockers: []
qa_status: passed
pr_details:
  number: 428
  title: "feat: Implement Feature Name (E1.1)"
  target_branch: milestone/M1
  url: "https://github.com/user/project/pull/428"
---

# Completion Notice: P1-M1-E1.1 — Feature Name

## Summary
Implemented feature XYZ with full test coverage and documentation. All Definition of Done items satisfied.

## Deliverables
- ✓ Epic spec created
- ✓ Implementation code committed
- ✓ Tests written and passing (14/14 tests)
- ✓ PR #428 opened against milestone/M1
- ✓ Code review checklist completed

## Quality Assurance
- Tests: passed (14/14)
- Code Review: ready (self-reviewed against checklist)
- Definition of Done: ✓ all items met

## Blockers or Risks
None. Ready for acceptance.

## Ready for Parent Review
This Epic is complete and submitted for Milestone Chat review and acceptance.
```

---

### 2. Review Decision (Milestone → Epic, Phase → Milestone, HQ → Phase)

**Trigger:** Parent reviews Completion Notice, decides to accept or reject.

**Direction:** Downward (parent → child)

**Purpose:** Grant authority to proceed with merge (Accept) or require rework (Reject).

#### Structure

```markdown
---
artifact_type: review_decision
artifact_version: 1.0
timestamp: <ISO-8601 UTC>
issuer_chat: <chat_type> (<full_reference>)
issuer_role: Milestone|Phase|HQ Agent
decision: accept|reject
epic_id: <P#-M#-E#.#> (or milestone_id for Milestone reviews, phase_id for Phase reviews)
milestone_id: <P#-M#>
phase_id: <P#>
project_name: <name>
completion_notice_timestamp: <timestamp of the Completion Notice being reviewed>
feedback: <feedback or rejection reason>
authorization:
  action: merge|rework
  merge_instruction: <if action=merge: detailed merge instructions>
---

# Review Decision: <P#-M#-E#.#> — <Epic Name>

## Decision: ACCEPT | REJECT

## Reviewer Context
- Reviewed by: <chat_type> Agent
- Review Date: <YYYY-MM-DD HH:MM UTC>
- Completion Notice Date: <YYYY-MM-DD HH:MM UTC>

## Feedback
<Detailed feedback, notes, or rejection reason>

## Authorization
<If ACCEPT:>
You are authorized to merge this work. Follow these steps:
1. <step 1>
2. <step 2>
3. ...

<If REJECT:>
This submission has been rejected. Please address the following before resubmitting:
1. <required change 1>
2. <required change 2>
3. ...
```

#### Examples

**Epic Review Decision (Accept):**
```markdown
---
artifact_type: review_decision
artifact_version: 1.0
timestamp: 2026-05-29T15:00:00Z
issuer_chat: Milestone Agent (P1-M1)
issuer_role: Milestone Agent
decision: accept
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: my-project
completion_notice_timestamp: 2026-05-29T14:32:00Z
feedback: "Excellent work. Spec compliance confirmed, tests comprehensive, PR ready for merge."
authorization:
  action: merge
  merge_instruction: "Merge PR #428 to milestone/M1. After merge, declare Epic complete in Milestone Chat."
---

# Review Decision: P1-M1-E1.1 — Feature Name

## Decision: ACCEPT ✓

## Reviewer Context
- Reviewed by: Milestone Agent (P1-M1)
- Review Date: 2026-05-29 15:00 UTC
- Completion Notice Date: 2026-05-29 14:32 UTC

## Feedback
Excellent work. The implementation is spec-compliant, tests are comprehensive (14/14 passing), and the PR is ready for merge. No issues found.

## Authorization
You are authorized to merge this work. Follow these steps:
1. Ensure PR #428 passes all CI/CD checks
2. Merge PR #428 to milestone/M1 using squash-and-merge strategy
3. Delete the epic/E1.1 branch after merge
4. Declare Epic E1.1 complete in the Milestone Chat
5. Move to the next Epic
```

**Epic Review Decision (Reject):**
```markdown
---
artifact_type: review_decision
artifact_version: 1.0
timestamp: 2026-05-29T15:30:00Z
issuer_chat: Milestone Agent (P1-M1)
issuer_role: Milestone Agent
decision: reject
epic_id: P1-M1-E1.2
milestone_id: P1-M1
phase_id: P1
project_name: my-project
completion_notice_timestamp: 2026-05-29T15:15:00Z
feedback: "Test coverage insufficient. Missing tests for error handling. PR CI checks failing."
authorization:
  action: rework
  merge_instruction: null
---

# Review Decision: P1-M1-E1.2 — Another Feature

## Decision: REJECT ✗

## Reviewer Context
- Reviewed by: Milestone Agent (P1-M1)
- Review Date: 2026-05-29 15:30 UTC
- Completion Notice Date: 2026-05-29 15:15 UTC

## Feedback
This submission is rejected. The following issues must be resolved:

1. **Test Coverage:** Only 60% coverage. Epic spec requires 80% minimum. Add tests for error handling paths.
2. **CI Failures:** 3 linter checks failing. Fix before resubmission.
3. **Documentation:** Missing API documentation in spec. Update before resubmission.

## Authorization
Rework required. Address all items above and resubmit a new Completion Notice when ready.
```

---

### 3. Delivery Notice (Merged PR → Archived Chat)

**Trigger:** PR is merged to parent branch. Epic/Milestone Chat declares itself closed.

**Direction:** Final handoff (child → parent, then to archives)

**Purpose:** Record final state, close the Epic/Milestone Chat, provide CFO audit trail.

#### Structure

```markdown
---
artifact_type: delivery_notice
artifact_version: 1.0
timestamp: <ISO-8601 UTC>
issuer_chat: <chat_type> (<full_reference>)
issuer_role: Epic|Milestone|Phase Agent
status: delivered
epic_id: <P#-M#-E#.#> (or milestone_id for Milestone delivery)
milestone_id: <P#-M#>
phase_id: <P#>
project_name: <name>
merge_details:
  pr_number: <PR number>
  pr_url: <GitHub URL>
  merge_commit: <commit hash>
  merge_timestamp: <ISO-8601 UTC>
  merge_strategy: squash|rebase|merge
  target_branch: <target branch>
duration:
  start_date: <YYYY-MM-DD>
  end_date: <YYYY-MM-DD>
  elapsed_days: <number>
final_artifacts:
  - name: <artifact_name>
    path: <repo_path>
    type: spec|implementation|report
completion_notice_timestamp: <timestamp of associated Completion Notice>
review_decision_timestamp: <timestamp of associated Review Decision>
---

# Delivery Notice: <P#-M#-E#.#> — <Epic Name>

## Summary
Work successfully delivered. PR merged to parent branch. Chat closed.

## Merge Details
- PR Number: <#>
- Merge Commit: <hash>
- Target Branch: <branch>
- Merge Strategy: <squash/rebase/merge>
- Merge Time: <YYYY-MM-DD HH:MM UTC>

## Duration
- Started: <YYYY-MM-DD>
- Completed: <YYYY-MM-DD>
- Total Time: <X days, Y hours>

## Final Artifacts
<List all deliverables committed to the repository>

## Chat Closure
This <Epic|Milestone> Chat is now closed. All work is delivered and merged.

**Next Step:** Parent Chat acknowledges delivery and moves forward.
```

#### Examples

**Epic Delivery Notice:**
```markdown
---
artifact_type: delivery_notice
artifact_version: 1.0
timestamp: 2026-05-29T16:00:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: delivered
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: my-project
merge_details:
  pr_number: 428
  pr_url: "https://github.com/user/project/pull/428"
  merge_commit: "abc1234567890def"
  merge_timestamp: 2026-05-29T16:00:00Z
  merge_strategy: squash
  target_branch: milestone/M1
duration:
  start_date: 2026-05-28
  end_date: 2026-05-29
  elapsed_days: 1
final_artifacts:
  - name: Epic Spec
    path: docs/phases/P1__Phase_Name/M1__Milestone/E1.1__spec__Feature_Name.md
    type: spec
  - name: Implementation
    path: src/features/feature-name.ts
    type: implementation
  - name: Tests
    path: tests/features/feature-name.test.ts
    type: implementation
completion_notice_timestamp: 2026-05-29T14:32:00Z
review_decision_timestamp: 2026-05-29T15:00:00Z
---

# Delivery Notice: P1-M1-E1.1 — Feature Name

## Summary
Work successfully delivered. PR #428 merged to milestone/M1. Epic Chat closed.

## Merge Details
- PR Number: #428
- Merge Commit: abc1234567890def
- Target Branch: milestone/M1
- Merge Strategy: squash
- Merge Time: 2026-05-29 16:00 UTC

## Duration
- Started: 2026-05-28
- Completed: 2026-05-29
- Total Time: 1 day, 2 hours

## Final Artifacts
- docs/phases/P1__Phase_Name/M1__Milestone/E1.1__spec__Feature_Name.md
- src/features/feature-name.ts
- tests/features/feature-name.test.ts

## Chat Closure
This Epic Chat (P1-M1-E1.1) is now closed. All work is delivered and merged to milestone/M1.

**Next Step:** Milestone Chat acknowledges and moves to next Epic.
```

**Milestone Delivery Notice:**
```markdown
---
artifact_type: delivery_notice
artifact_version: 1.0
timestamp: 2026-05-29T18:00:00Z
issuer_chat: Milestone Agent (P1-M1)
issuer_role: Milestone Agent
status: delivered
milestone_id: P1-M1
phase_id: P1
project_name: my-project
merge_details:
  pr_number: 450
  pr_url: "https://github.com/user/project/pull/450"
  merge_commit: "def4567890abcdef"
  merge_timestamp: 2026-05-29T18:00:00Z
  merge_strategy: merge
  target_branch: phase/P1
duration:
  start_date: 2026-05-15
  end_date: 2026-05-29
  elapsed_days: 14
final_artifacts:
  - name: Milestone Spec
    path: docs/phases/P1__Phase_Name/M1__Milestone_Spec.md
    type: spec
  - name: 3 Epic Specs
    path: docs/phases/P1__Phase_Name/M1__Milestone/
    type: spec
  - name: All Epic Implementations
    path: src/
    type: implementation
  - name: Milestone Report
    path: docs/phases/P1__Phase_Name/M1__milestone-report.md
    type: report
completion_notice_timestamp: 2026-05-29T17:00:00Z
review_decision_timestamp: 2026-05-29T17:30:00Z
---

# Delivery Notice: P1-M1 — Foundation Setup

## Summary
Milestone M1 successfully completed. All 3 Epics delivered. Milestone branch merged to Phase P1.

## Merge Details
- PR Number: #450
- Merge Commit: def4567890abcdef
- Target Branch: phase/P1
- Merge Strategy: merge
- Merge Time: 2026-05-29 18:00 UTC

## Duration
- Started: 2026-05-15
- Completed: 2026-05-29
- Total Time: 14 days

## Final Artifacts
- docs/phases/P1__Phase_Name/M1__Milestone_Spec.md
- 3 Epic Specs (all complete)
- All Epic implementations (src/)
- Milestone Report (docs/phases/P1__Phase_Name/M1__milestone-report.md)

## Chat Closure
This Milestone Chat (P1-M1) is now closed. All work is delivered and merged to phase/P1.

**Next Step:** Phase Chat acknowledges and moves to M2.
```

---

## Communication Flow Diagram

```
Epic Execution Chat
    ↓
    [Complete]
    ↓ ARTIFACT: Completion Notice
    ↓
Milestone Chat
    ↓
    [Review]
    ↓ ARTIFACT: Review Decision (Accept)
    ↓ ARTIFACT: Review Decision (Reject ← rework required)
    ↓
Epic Execution Chat (if Reject: rework and resubmit)
    ↓
    [Rework] → Completion Notice
    ↓ ARTIFACT: Review Decision (Accept)
    ↓
Epic Execution Chat
    ↓
    [Merge PR]
    ↓ ARTIFACT: Delivery Notice
    ↓
Milestone Chat
    ↓
    [Acknowledge] → Next Epic or Milestone Complete
    ↓ ARTIFACT: Completion Notice (Milestone)
    ↓
Phase Chat
    ↓
    [Review] → Repeat flow at Milestone level
```

---

## Rules

### Creation Rules

1. **Completion Notice** is created by the child chat when work is finished (all Definition of Done items met, PR open/merged).
2. **Review Decision** is created by the parent chat after reviewing the Completion Notice (accept within 24 hours or escalate).
3. **Delivery Notice** is created by the child chat after the PR is merged to the parent branch.

### Formatting Rules

1. All artifacts MUST have valid YAML frontmatter (no syntax errors).
2. Frontmatter MUST include: `artifact_type`, `artifact_version`, `timestamp`, `issuer_chat`, `decision/status`.
3. Reference IDs MUST match the naming convention: `P#-M#-E#.#` (for Epics), `P#-M#` (for Milestones), `P#` (for Phases).
4. Timestamps MUST be ISO-8601 UTC format.
5. Markdown body MUST be human-readable; no machine-only formats allowed.

### Workflow Rules

1. A Completion Notice MUST precede a Review Decision.
2. A Review Decision (Accept) MUST precede a Delivery Notice.
3. A Delivery Notice MUST be created within 24 hours of PR merge (or escalate if delayed).
4. If a Review Decision rejects, the child chat creates a new Completion Notice (v1.1) after rework.
5. Artifacts are immutable once created; modifications create new versions (v1.1, v1.2, etc.).

### Storage & Archival Rules

1. **Completion Notices** are stored in `.ai-project/artifacts/completion-notices/` (one file per Epic/Milestone).
2. **Review Decisions** are stored in `.ai-project/artifacts/review-decisions/` (one file per decision).
3. **Delivery Notices** are stored in `.ai-project/artifacts/delivery-notices/` (one file per delivery).
4. File naming: `<timestamp>__<epic_id_or_milestone_id>__<artifact_type>.md`
5. Artifacts are committed to the repository for audit trail.

---

## Integration with Manual Mode

In manual mode (no daemon), chats produce these artifacts and paste them into parent chats via copy-paste. The parent chat reviews and copies the Review Decision back.

**CFO Benefit:** Layer-8 can visit any HQ Chat and see the latest Completion Notices, Review Decisions, and Delivery Notices in a structured format, making progress tracking across multiple projects trivial.

---

## Integration with Agentic Mode

In agentic mode (daemon running), these artifacts flow through the queue system:

1. Epic Chat completes → writes Completion Notice to `.ai-project/artifacts/completion-notices/`
2. Daemon detects Completion Notice → routes to parent (Milestone Chat or HQ Chat)
3. Parent Chat reads and processes → writes Review Decision to `.ai-project/artifacts/review-decisions/`
4. Daemon detects Review Decision → routes back to child (Epic Chat or Milestone Chat)
5. Child Chat reads Accept decision → proceeds to merge → writes Delivery Notice

---

## Reference

- **Chat Hierarchy:** `governance/systems/chat-hierarchy.md`
- **Epic Execution Chat Starter:** `governance/EPIC-EXECUTION-CHAT-STARTER.md`
- **Milestone Execution Chat Starter:** `governance/systems/milestone-execution-chat-starter.md`
- **Phase Execution Chat Starter:** `governance/systems/phase-execution-chat-starter.md`
- **Project System Guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md`
- **AI Operating Guidelines:** `governance/AI-OPERATING-GUIDELINES.md`

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-05-29 | Initial release. Defines Completion Notice, Review Decision, Delivery Notice schemas and integration with manual & agentic modes. |
