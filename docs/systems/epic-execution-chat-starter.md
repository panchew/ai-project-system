---
type: template
status: active
last_updated: 2026-01-17
---


# EPIC EXECUTION CHAT STARTER

GOVERNANCE RESOLUTION

- All governance for Epic Execution Chat Starters is resolved **by explicit reference** to the authoritative governance source.
- The authoritative governance model is documented in [docs/systems/governance-propagation.md](governance-propagation.md).
- Projects adopting this governance must include a `governance-source.md` file referencing the authoritative source.
- **No live GitHub access or automatic governance syncing is available.** All governance enforcement is by reference and manual review.
- If no `governance-source.md` is present, governance is not adopted for the project.

MANDATORY CONTEXT PACKET

Project:
Phase:
Milestone:
Epic:
Spec Path:
Governance Versions:
Execution Mode:
Scope Rule:


SPEC EXISTENCE REQUIREMENT

- The Epic spec MUST exist at the specified path.
- If the spec is not found, STOP and report the issue.
- Do NOT create or redefine the Epic spec.

DELIVERY REQUIREMENTS (MANDATORY)

- Working branch:
- Pull request target:
- Branch creation authorization:
- Delivery is part of the Definition of Done.


EXECUTION INSTRUCTIONS

- Treat the Epic spec as the single source of truth.
- Execute only what is defined.
- All governance is enforced by reference to the authoritative source (see GOVERNANCE RESOLUTION above).
- Ask questions only if blocked.
- Do not expand scope.

COMPLETION REQUIREMENTS

- All DoD items satisfied
- Completion report produced and committed
- PR created (or manual handoff provided)
- Explicit completion declaration

QUESTION POLICY

- Ask only blocking questions.
- Do not propose new features.

DELIVERY FORMAT (MANDATORY)

When HQ Chat produces an Epic Execution Chat Starter, the entire content MUST be
wrapped in a fenced markdown code block using four backticks:

    ````markdown name=<E#.#>-epic-execution-chat-starter.md
    [starter content here]
    ````

This preserves markdown formatting when copy-pasted into a Coding Agent chat.
After the code block, include:
"Copy the entire chat starter above and paste into your Coding Agent chat to begin execution."

Canonical rule: AI-OPERATING-GUIDELINES.md §3.1.1
