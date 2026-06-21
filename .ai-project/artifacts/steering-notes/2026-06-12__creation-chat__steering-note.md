---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-06-12T00:00:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-1
    severity: high
    title: milestone/M14 stranded on wrong git base
  - id: SN-2
    severity: high
    title: Abandoned P4-M1 nomenclature artifacts on master
  - id: SN-3
    severity: medium
    title: Phase and Milestone Chats missing Stage 2 lifecycle definition
  - id: SN-4
    severity: medium
    title: Three generations of completion templates coexist — inconsistent
  - id: SN-5
    severity: medium
    title: start-a-project.md is P1-era, contradicts P2+ submodule model
decisions:
  - Cleanup executes before M14 salvage and before any new feature work
  - M14 salvage strategy is cherry-pick (7 commits onto fresh branch from master), not restart
  - MVP manual mode must be proven before agentic mode is extended further
  - HQ Chat is being re-instantiated cleanly — not continued from prior sessions
  - Creation Chat is now a formalized permanent layer above HQ Chat
  - Genesis artifact approach adopted (formal artifact shipped with framework, not convention)
artifacts_produced:
  - path: governance/templates/genesis.md
    description: Genesis artifact template — bootstraps the Creation Chat
  - path: governance/diagrams/artifact-flow.md
    description: Full artifact flow diagram across all chat levels, with exists/missing status
---

# Steering Note — Creation Chat to HQ Chat

## Purpose

This Steering Note closes the Creation Chat session of 2026-06-12 and provides HQ Chat
with the concerns, decisions, and context it needs to begin planning.

---

## Concerns for HQ Triage

### SN-1 — milestone/M14 stranded on wrong git base [HIGH]

`milestone/M14` contains the complete, executed first milestone of P4 under correct
numbering: E14.1 (artifact parser), E14.2 (daemon queue integration), E14.3 (integration
tests) — with review decisions, delivery notices, and a Milestone Completion Declaration
(2026-06-06). The work is done and governance-compliant.

**The problem:** the branch was rooted on a January 2026 P1-era commit, not master.
A direct merge would destroy five months of history. The branch cannot be merged as-is.

**Recommended resolution:** Cherry-pick the 7 P4 commits onto a fresh branch from
master. Only 3 files overlap with master (P4 phase spec, P4 HQ starter, roadmap) —
conflicts are manageable. Requires HQ authorization to execute.

### SN-2 — Abandoned P4-M1 nomenclature artifacts on master [HIGH]

The agent that planned P4's first milestone used the wrong naming convention (M1 instead
of continuing global numbering to M14). The planning artifacts were corrected and
the work executed correctly under M14, but the abandoned M1-named specs and chat
starters were never removed from master:

- `docs/phases/P4.../P4-M1-E1.1__epic-execution-chat-starter.md`
- `docs/phases/P4.../P4-M1-E1.1__spec__Artifact_Parsing_and_Schema_Validation.md`
- `docs/phases/P4.../P4-M1-E1.2__spec__...`
- `docs/phases/P4.../P4-M1-E1.3__spec__...`
- `docs/phases/P4.../P4-M1__milestone-execution-chat-starter.md`

Master currently presents M14's work as "not yet started." This is actively misleading.

### SN-3 — Phase and Milestone Chats missing Stage 2 lifecycle [MEDIUM]

Phase and Milestone Execution Chat Starters currently define these chats as planning-only.
They explicitly state: "Not a Coding Agent — does not branch, commit, or open PRs."
This is wrong. Both chat types have a Stage 2: aggregate child completions, open their
own PR, merge after parent Review Decision Accept, send Delivery Notice.

In agentic mode this was handled silently by `ai-project-git-merge`. In manual mode
the gap is exposed — the human has no guidance on who opens milestone/* → phase/* PRs.
The starters need a Stage 2 section. The "not an execution chat" language must be corrected.

### SN-4 — Three generations of completion templates coexist [MEDIUM]

- `governance/templates/epic-completion-notice.md` (Jan 2026, plain text, no YAML schema)
- `governance/templates/epic-completion-report.md` (P2-era)
- `governance/templates/completion-notice-epic.md` (P4.1, correct, YAML frontmatter)

An Epic Chat reading governance will find three conflicting templates and no guidance
on which to use. The first two should be deleted; the third should be the sole canonical
template (possibly renamed `completion-notice.md` since it applies at all levels).

### SN-5 — start-a-project.md is outdated [MEDIUM]

`governance/systems/start-a-project.md` (last updated 2026-01-17) instructs copying
governance files into `docs/` — directly contradicting the P2 model (`ai-project init`,
governance-as-submodule, `.ai-project.yml`). A new adopter following the README's
"How to Start a Project" link gets incorrect instructions. This document needs a full
rewrite to reflect the current flow and the new Creation Chat / Genesis layer.

---

## Decisions Already Made

These are not for HQ to re-decide — they come from the CFO (Layer-8) and are binding:

1. **Cleanup executes first** — before M14 salvage, before any new feature work.
2. **M14 salvage strategy is cherry-pick** — not a restart. HQ should authorize execution.
3. **Manual mode MVP before agentic extension** — no new agentic work until the full
   manual artifact lifecycle is validated end-to-end by real usage.
4. **Creation Chat is now a formalized permanent layer above HQ Chat** — the governance
   hierarchy is: Creation → HQ → Phase → Milestone → Epic.
5. **Genesis artifact approach adopted** — a formal artifact (not convention) ships with
   the framework and bootstraps the Creation Chat. Template created this session.

---

## Artifacts Produced This Session

| Path | Description |
|------|-------------|
| `governance/templates/genesis.md` | Genesis artifact template |
| `governance/diagrams/artifact-flow.md` | Full artifact flow diagram (exists/missing status) |
| `.ai-project/artifacts/steering-notes/2026-06-12__creation-chat__steering-note.md` | This document |

---

## Next Action

HQ Chat should read this Steering Note and the current project state, then plan the
work needed to address these concerns — as formal Phases, Milestones, and Epics.

The artifact flow diagram (`governance/diagrams/artifact-flow.md`) provides the
agreed picture of what the full artifact system should look like when complete.
