# EPIC EXECUTION CHAT STARTER (CANONICAL TEMPLATE)

MANDATORY CONTEXT PACKET

Project: <project-name>
Phase: P<id> — <phase-name>
Milestone: M<id> — <milestone-name>
Epic: E<id> — <epic-name>
Spec Path: <path-to-epic-spec>
Governance: PROJECT-SYSTEM-GUIDELINES.md and AI-OPERATING-GUIDELINES.md enforced
Execution Mode: Single-epic execution
Scope Rule: Execute this Epic only. No scope expansion.

DELIVERY REQUIREMENTS (MANDATORY)

- Working branch: epic/E<id>
- Pull request:
  epic/E<id> → milestone/M<id>
- Direct PRs to phase/* or develop are invalid
- Delivery is part of the Definition of Done

EXECUTION INSTRUCTIONS

- Treat the Epic spec as the single source of truth
- Implement only what is explicitly defined
- Ask questions only if execution is blocked

COMPLETION REQUIREMENTS

- Definition of Done satisfied
- PR opened against correct milestone branch
- Epic Completion Report produced and committed
- **Completion Notice artifact** produced (see `governance/templates/completion-notice-epic.md`)
- Agent declares Epic complete and stops

## Artifact-Driven Communication (P4.1)

When this Epic is complete, you MUST produce a **Completion Notice** artifact before declaring the work done.

### Completion Notice

The Completion Notice is a structured artifact (YAML frontmatter + markdown) that signals readiness for parent (Milestone) review.

**Template:** `governance/templates/completion-notice-epic.md`

**What to include:**
- Frontmatter with epic_id, milestone_id, phase_id, pr_details, qa_status
- Summary of what was delivered
- List of deliverables (spec, implementation, tests, PR)
- QA status (tests passed, code review ready, DoD met)
- Any blockers or risks

**Example:**
```markdown
---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: 2026-05-29T14:32:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
status: ready_for_review
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: my-project
pr_details:
  number: 428
  title: "feat: Implement Feature Name (E1.1)"
  target_branch: milestone/M1
  url: "https://github.com/user/project/pull/428"
qa_status: passed
---

# Completion Notice: P1-M1-E1.1 — Feature Name

## Summary
Implemented feature XYZ with full test coverage and documentation. All Definition of Done items satisfied.

...
```

### What Happens Next

1. **You (Epic Agent):** Produce Completion Notice in `governance/templates/completion-notice-epic.md`, fill it in, and paste it into the Milestone Chat.
2. **Milestone Agent:** Reviews your Completion Notice, then issues a **Review Decision** artifact (Accept or Reject).
3. **If Accept:** You merge the PR and produce a **Delivery Notice** artifact.
4. **If Reject:** You address feedback, create a new Completion Notice (v1.1), and resubmit.

### Storage

After creating the Completion Notice, store it in: `.ai-project/artifacts/completion-notices/<timestamp>__<epic_id>__completion_notice.md`

This creates an audit trail for the CFO (Layer-8) to track progress across all projects.

---

**Reference:** `governance/systems/artifact-communication-protocol.md` (P4.1)
