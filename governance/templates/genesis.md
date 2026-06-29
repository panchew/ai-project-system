---
type: genesis
project: <project-slug>
created_by: <Creation Chat role or person>
date: <YYYY-MM-DD>
phase_1_name: <Phase 1 short name>
status: draft
---

<!--
  GENESIS TEMPLATE — the single artifact that must exist before a Phase Chat opens.

  Purpose: A Creation Chat (or a human acting as one) fills this out to bootstrap a
  new project. It scopes only project identity, Phase 1 boundaries, and team
  composition. It does NOT define milestone specs, epics, or execution detail —
  those belong to the Phase Chat and below.

  How to use:
  1. Run `ai-project init <project-name>` first (see governance/systems/start-a-project.md).
  2. Copy this file to the project root (or fill it where init placed it).
  3. Replace every <placeholder>. Delete guidance comments as you go.
  4. Set `status: complete` in the front-matter when every section is filled.
  5. Commit the completed genesis.md, then open a Phase Chat using the Next Step section.

  A reader with no prior knowledge of this system should be able to fill this in,
  in one focused session, without opening any other document. See
  examples/genesis-walkthrough/genesis.md for a completed example.

  Front-matter fields:
  - type:         always `genesis`
  - project:      project name as a kebab-case slug (e.g. taskflow)
  - created_by:   the role or person acting as Creation Chat
  - date:         ISO date the genesis was completed (YYYY-MM-DD)
  - phase_1_name: short human name of Phase 1 (e.g. "Core Task CRUD")
  - status:       `draft` while filling in; `complete` when ready to hand off
-->

# Genesis — <Project Name>

## Project Brief

<!-- The one-paragraph "why" of the project. Enough for a stranger to understand intent. -->

**Goal:** <What success looks like in one or two sentences.>

**Problem:** <The problem this project solves and for whom.>

**Initial Team:**

<!-- The people (or roles) who will govern and build Phase 1. Authority = what they decide. -->

| Role | Person | Authority |
|------|--------|-----------|
| CFO | <name> | Phase scope, production authorization |
| Phase Lead | <name> | Milestone planning, Epic acceptance |
| Contributor | <name> | Epic implementation |

## HQ Context Packet

<!--
  This section is the handoff to the Phase Chat. If a Phase Chat can open using ONLY
  this packet — with no follow-up questions — the genesis is correct. Keep it tight.
-->

- **Project:** <project-slug>
- **Governance path:** `.governance/` (sourced as a submodule; see start-a-project.md)
- **Phase 1 scope summary:** <One or two sentences naming what Phase 1 will and will not cover.>
- **Key constraints:** <Hard limits: deadlines, tech mandates, compliance, budget, exclusions.>
- **Architecture visual:** <optional — hosted link to the HQ system-architecture visual>
  <!-- Record as a visual binding (link + What/Level/State/Description) per
       governance/guides/visual-artifacts.md §7. Bind a link, never a committed path. Omit if none. -->

## Phase 1 Scope

<!-- Name and shape Phase 1. Milestone stubs are one-liners only — the Phase Chat expands them. -->

**Name:** <Phase 1 short name>

**Goal:** <The outcome Phase 1 must deliver.>

**Milestone stubs:**

- M1: <one-line description>
- M2: <one-line description>
- M3: <one-line description>

## Creation Chat Decisions

<!-- A record of what the Creation Chat actually settled. Confirms the work above is final. -->

- Project name confirmed: <project-slug>
- Phase 1 scope accepted: <yes / summary of what was agreed>
- Team roles assigned: <who holds CFO, Phase Lead, and contributor roles>

## Next Step

Open a Phase Chat using
[`governance/templates/phase-execution-chat-starter.md`](phase-execution-chat-starter.md),
passing this committed `genesis.md` as the mandatory context packet. The Phase Chat
consumes the HQ Context Packet and Phase 1 Scope above to plan milestones. Do not begin
any execution until the Phase Chat has produced and authorized Milestone work.
