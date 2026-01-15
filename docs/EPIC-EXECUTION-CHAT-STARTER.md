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
- Agent declares Epic complete and stops
