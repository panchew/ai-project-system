---
type: system
status: active
effective_date: 2026-04-23
version: 1.0.0
---

# Phase Execution Chat Starter — System Reference

## Purpose

This document defines the role, responsibilities, and operating rules for a Phase Execution Chat session in the AI Project System.

A Phase Execution Chat Starter is the governance artifact that launches a Phase Chat. It is produced by HQ Chat, delivered to the Phase Chat session, and constitutes the binding execution contract for the session.

---

## What a Phase Chat Is

A **Phase Chat** is a planning session scoped to a single Phase. It is:

- **Finite in duration** — it opens with a Phase Execution Chat Starter and closes when all Milestone Chat Starters are produced and accepted by HQ
- **Launched from HQ Chat** — using the Phase Execution Chat Starter template (`governance/templates/phase-execution-chat-starter.md`)
- **Scoped to a single Phase** — it does not span multiple phases or milestones outside its Phase
- **Read-only with respect to the project** — it does NOT execute work; it plans and produces planning artifacts

A Phase Chat has read access to:
- The Phase spec
- All Milestone stubs within the Phase

A Phase Chat does NOT have write authority over the project repository. All file creation during a Phase Chat session is performed by the Coding Agent acting on the Phase Chat's instructions as deliverables committed to the repository.

---

## Responsibilities

The following is the exhaustive list of Phase Chat responsibilities:

1. **Review the Phase spec** — confirm it is complete, actionable, and consistent with governance
2. **Produce Milestone specs** — create a Milestone spec file for every Milestone stub within the Phase; these are deliverables committed by the Coding Agent
3. **Produce Milestone Execution Chat Starters** — create a filled-in Milestone Execution Chat Starter for each Milestone within the Phase
4. **Return deliverables to HQ Chat** — all produced artifacts are returned to HQ Chat for review and acceptance
5. **Acknowledge Milestone acceptance in-chat** — when HQ Chat accepts a Milestone's deliverables (by silence on the happy path, per SN-19), the Phase Chat acknowledges the acceptance in-chat and applies the standing merge instruction authorizing the Milestone Chat to proceed with that Milestone

A Phase Chat MUST complete all responsibilities before declaring the session closed.

---

## Communication Scope

Phase Chat communication is strictly bounded:

| Direction | Permitted | Notes |
|-----------|-----------|-------|
| Upward | HQ Chat only | Reports progress, returns deliverables, requests decisions |
| Downward | Milestone Chats only | Issues Milestone Execution Chat Starters; acknowledges Milestone acceptance in-chat (SN-19 — no artifact) |
| Lateral | PROHIBITED | A Phase Chat MUST NOT reach across to sibling phases or lateral epics |

**Rule:** A Phase Chat MUST NOT communicate with or reference work belonging to another Phase. If cross-phase dependencies are discovered, the Phase Chat escalates to HQ Chat.

---

## What a Phase Chat Is NOT

- ❌ **Not a Coding Agent** — it does not branch, commit, or open PRs directly
- ❌ **Not a substitute for HQ Chat's authority** — HQ Chat owns accept/reject decisions; Phase Chat produces proposals only
- ❌ **Not a place where branches are created or files are directly modified** — the Coding Agent executes those actions on the Phase Chat's behalf
- ❌ **Not a persistent session** — it closes when all Milestone Chat Starters are produced and accepted by HQ
- ❌ **Not an execution chat** — it produces planning artifacts, not code or implementation

---

## Governance Authority Chain

Within a Phase Chat session, the following hierarchy governs all decisions:

1. `PROJECT-SYSTEM-GUIDELINES.md` (highest authority)
2. `AI-OPERATING-GUIDELINES.md`
3. Phase Execution Chat Starter (the instance that launched this session)
4. Phase Spec
5. Decisions made during the session
6. System references
7. Chat messages (lowest authority)

Documentation is authoritative. Chat is ephemeral. Any conflict between a chat statement and a governance document is resolved in favor of the governance document.

---

## Milestone Acceptance and Merge Instruction (SN-19 — in-chat, no artifact)

Per SN-19 and PSG §1A gate scoping / §11.6, there is **no Milestone Delivery Authorization
artifact or ceremonial block**. When HQ Chat accepts a Milestone's deliverables (by silence on
the happy path), the Phase Chat (or HQ Chat, during bootstrap) acknowledges the acceptance
**in-chat**. This acknowledgment is the signal to the Coding Agent that the Milestone's
planning artifacts are accepted and the Milestone Chat may begin execution.

The standing merge instruction is: **merge epic branches to `milestone/<M#>` upon Epic
acceptance** — the merge itself still requires explicit human authorization, which the harness
enforces.

### Authority Rules

- **Only HQ Chat or Phase Chat may acknowledge Milestone acceptance.**
- A Coding Agent MUST NOT self-authorize Milestone execution.
- HQ Chat acceptance MUST be acknowledged before a Milestone Chat begins.

---

## Session Lifecycle

A Phase Chat session follows this sequence:

1. **Open** — receive the Phase Execution Chat Starter from HQ Chat
2. **Review** — confirm the Phase spec exists and is complete
3. **Plan** — produce Milestone specs and Milestone Execution Chat Starters for all Milestones
4. **Return** — deliver all artifacts to HQ Chat for review
5. **Authorize** — for each accepted Milestone, acknowledge acceptance in-chat and apply the standing merge instruction (SN-19 — no artifact)
6. **Close** — declare the session closed after all Milestones are authorized

**If the Phase spec is missing or incomplete:** STOP. Report the issue to HQ Chat. Do not proceed with planning.

---

## Reference

- **Agent definition:** `governance/agents/governance.agent.md` (Phase mode)
- **System document:** `governance/systems/phase-execution-chat-starter.md` (this file)
- **Template:** `governance/templates/phase-execution-chat-starter.md`
- **Parent mode:** HQ mode (in `governance/agents/governance.agent.md`)
- **Child mode:** Milestone mode (in `governance/agents/governance.agent.md`)
- **Governing guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md` §13A
- **Delivery wrapping rule:** `governance/AI-OPERATING-GUIDELINES.md` §3.1.1

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-08-05 | **Versioning convention adopted** (HQ Ruling 2026-08-04, P10-GH-8; applied by E37.1, P11-M37). This document previously carried neither a `version` field nor a `## Changelog` section. **This is its first recorded row, and no prior history is reconstructed** — for changes before this date, see `git log -- governance/systems/phase-execution-chat-starter.md`. |
