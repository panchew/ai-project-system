---
project: ai-project-system
phase: P4
milestone: M15
epic: E15.1
type: system
status: active
last_updated: 2026-06-13
version: 1.0.0
---

# Starting a New Project Under the AI Project System

> **Self-referential vs. submodule: how to read this guide**
>
> - `governance/` is the **framework SOURCE repo** (this repository) — used when dogfooding the
>   framework on itself.
> - `.governance/` is the **submodule path inside a consumer project** — where your governance lives
>   after `ai-project init`.
> - In a consumer project, read bare `governance/...` paths below as `.governance/governance/...`.
>   If your project *is* the framework source, use `governance/...` as written.

## Purpose

This document defines the **canonical process** for starting a new project governed by the AI Project System.

Its goal is to ensure:
- Governance consistency
- Correct role separation
- No execution without structure
- No reliance on tribal knowledge

---

## Overview

Projects are initialized using the `ai-project init` CLI command. Governance documents live in
a dedicated governance submodule (`.governance/`) — they are **not** copied into the project
repository.

The **Creation Chat** is the entry point that turns a project brief into the first structured
artifact: a committed `genesis.md`. It runs once, right after `ai-project init`, and scopes
only project identity, Phase 1 boundaries, and team composition. It does not plan milestones
or epics and does not execute work — that begins with the Phase Chat. The full Creation Chat
role (inputs, authority, outputs, stopping condition) is defined in
[`chat-hierarchy.md`](chat-hierarchy.md#level-0-creation-chat-project-bootstrap).

---

## Step 0 — Open the Creation Chat

Before anything else, open the **Creation Chat** — the session that produces your first
`genesis.md`. Paste [`governance/templates/seed.md`](../templates/seed.md) into a Claude session to
open it (load the Governance Agent first — see the
[integration guides](../guides/integrations/README.md) for your tool: Claude Code, Cursor, Windsurf,
or GitHub Copilot). The Creation Chat you open here is the same one you use in **Step 3** to produce
and commit `genesis.md`.

---

## Step 1 — Create the Repository

Create a new Git repository using your preferred tooling.

The repository needs only a project-level `README.md` to begin — `ai-project init` will
create all required structure.

---

## Step 2 — Run `ai-project init`

Run the project scaffolding command from the repository root:

```bash
ai-project init <project-name>
```

This command:
- Adds the `ai-project-system` governance repository as a Git submodule at `.governance/`
- Creates `.ai-project.yml` declaring the governance source and pinned ref
- Installs the Governance Agent file (canonical, tool-neutral path:
  `.ai-project/agents/governance.agent.md`)
- Creates the baseline documentation structure under `docs/`

The Governance Agent is tool-neutral: to open it in your AI tool (Claude Code, Cursor, Windsurf,
or GitHub Copilot), follow the matching guide in
[`governance/guides/integrations/`](../guides/integrations/README.md). No tool-specific path is
required.

The submodule model means governance documents are always sourced from `.governance/`, keeping
every project aligned to a versioned, auditable governance source. See
[`governance/submodule-setup.md`](../submodule-setup.md) for submodule details.

---

## Step 3 — Run the Creation Chat (produce and commit `genesis.md`)

Copy [`governance/templates/genesis.md`](../templates/genesis.md) into the project and fill it
out in a Creation Chat session. The genesis template collects:

- Project name and purpose (Project Brief)
- Stakeholders and roles — CFO, Phase Lead, Contributors (Initial Team)
- The HQ Context Packet that opens the next chat
- Phase 1 name, goal, and milestone stubs (Phase 1 Scope)
- The decisions the Creation Chat settled (Creation Chat Decisions)

When every section is filled, set `status: complete` in the front-matter and **commit
`genesis.md` to the repository**. A committed `genesis.md` is the single artifact required
before a Phase Chat can open.

There are **no manual governance file-copy steps** — governance is sourced from the
`.governance/` submodule, and `genesis.md` is the only artifact you author by hand at this
stage. For a completed reference, see
[`examples/genesis-walkthrough/genesis.md`](../../examples/genesis-walkthrough/genesis.md).

**Next step:** with `genesis.md` committed, choose your path below — **once** — before
proceeding further.

---

## Choose Your Path

This is the single fork point for the Level-0 handoff. Pick one:

- **Small, single-phase bootstrap:** stop here and open a Phase Chat directly, using
  [`governance/templates/phase-execution-chat-starter.md`](../templates/phase-execution-chat-starter.md)
  and passing the committed `genesis.md` (its HQ Context Packet and Phase 1 Scope) as the
  mandatory context packet. Steps 4-7 below do not apply — a Phase Chat is your ongoing
  control plane. This is the **lightweight path** described in `governance/templates/
  genesis.md`.
- **Ongoing, multi-phase project that needs a persistent control plane:** continue to Step 4
  onward. This **full path** additionally converges the Creation Chat on a Project Brief and
  HQ Chat Opener (`governance/templates/seed.md` Rule 4) and spawns an HQ Chat that governs
  every Phase, not just the first.

Steps 4-7 are the full-flow continuation of the ongoing-project path only — they are not a
second, mandatory pass over the same ground the lightweight path already covered in Step 3.

---

## Step 4 — Declare System Alignment

The `ai-project init` command creates `.ai-project.yml` with the governance source and ref.
Verify that `governance.ref` in `.ai-project.yml` matches the pinned submodule commit.

For manual verification:

```bash
git -C .governance rev-parse HEAD
```

This allows drift detection across projects and ensures every team member is working from
the same governance version.

---

## Step 5 — Spawn the HQ Chat

*(Full path only — see "Choose Your Path" above.)*

Create an **HQ Chat** (Headquarters / Control Room) in your preferred LLM interface, opened
from the HQ Chat Opener produced by the Creation Chat's full-path convergence
([`governance/templates/hq-chat-opener.md`](../templates/hq-chat-opener.md), filled out per
`seed.md` Rule 4), together with the HQ Context Packet and Phase 1 Scope recorded in the
committed `genesis.md`. To load the Governance Agent in
your tool, follow the matching guide in
[`governance/guides/integrations/`](../guides/integrations/README.md) (Claude Code, Cursor,
Windsurf, or GitHub Copilot).

The HQ Chat becomes the **strategic control plane** for the project:
- Defines Phases, Milestones, and Epics
- Produces Epic specs and Epic Execution Chat Starters
- Accepts clean deliveries by an acknowledgment that names the party that reviewed and accepted (a Review Decision is the exception path only — PSG §11.6; silence accepts nothing) and issues Delivery Authorizations
- Never executes code

---

## Step 6 — Define Phase 1

Using the HQ Chat:
- Define the first Phase
- Define at least one Milestone
- Define at least one Epic

No Coding Agent execution may begin before this step is complete.

---

## Step 7 — Execute via Coding Agents

Once an Epic is fully specified:
- An HQ Chat produces the Epic Execution Chat Starter
- A Coding Agent executes the Epic
- Delivery and completion are mandatory

---

## Closing Statement

A project is not started when code is written.

A project is started when **intent, structure, and governance are explicit**.

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.1.0 | 2026-09-02 | **Acceptance distinguishable from absence (E43.2, P12-M43).** The HQ Chat duties list's accept-clean-deliveries line reconciled to the amended PSG §11.6: acceptance is by an **in-chat acknowledgment that names the party that reviewed and accepted** — silence accepts nothing. |
| 1.0.0 | 2026-08-05 | **Versioning convention adopted** (HQ Ruling 2026-08-04, P10-GH-8; applied by E37.1, P11-M37). This document previously carried neither a `version` field nor a `## Changelog` section. **This is its first recorded row, and no prior history is reconstructed** — for changes before this date, see `git log -- governance/systems/start-a-project.md`. |
