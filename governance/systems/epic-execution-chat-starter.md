---
type: template
status: active
last_updated: 2026-07-18
version: 1.0.0
---


# EPIC EXECUTION CHAT STARTER

GOVERNANCE RESOLUTION

- All governance for Epic Execution Chat Starters is resolved **by explicit reference** to the authoritative governance source.
- The authoritative governance model is documented in [governance/systems/governance-propagation.md](governance-propagation.md).
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

When a parent chat produces an Epic Execution Chat Starter, it commits the
filled-in starter as a git-tracked file and hands it off **by reference**:
IDE-attach + one line of intent, or the canonical reference line
(artifact type + id — repo-relative path — status). The starter's body is NOT
echoed into chat output.

Fallback — no repo access? For genuinely repo-less delivery only, use the
four-backtick fenced full-body form defined in the canonical rule's fallback
format.

Canonical rule: AI-OPERATING-GUIDELINES.md §3.1.1 (reference-first artifact
handoff; cited, not restated)

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-08-05 | **Versioning convention adopted** (HQ Ruling 2026-08-04, P10-GH-8; applied by E37.1, P11-M37). This document previously carried neither a `version` field nor a `## Changelog` section. **This is its first recorded row, and no prior history is reconstructed** — for changes before this date, see `git log -- governance/systems/epic-execution-chat-starter.md`. |
