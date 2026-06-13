---
project: ai-project-system
phase: P4
milestone: M15
epic: E15.1
type: system
status: active
last_updated: 2026-06-13
---

# Starting a New Project Under the AI Project System

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
repository. The Genesis / Creation Chat is the entry point for defining the project's intent
before any execution begins.

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
- Installs the HQ agent file
- Creates the baseline documentation structure under `docs/`

The submodule model means governance documents are always sourced from `.governance/`, keeping
every project aligned to a versioned, auditable governance source. See
[`governance/submodule-setup.md`](../submodule-setup.md) for submodule details.

---

## Step 3 — Open the Genesis / Creation Chat

Open [`governance/templates/genesis.md`](../templates/genesis.md) and use it as the prompt for
a new Creation Chat session. The Genesis template collects:

- Project name and purpose
- Stakeholders and roles (CFO, Phase Leads, Contributors)
- Initial phase and milestone intent
- Governance alignment declaration

The Creation Chat produces the first structured artifacts — the project's initial HQ Chat
context and Phase 1 scope — before any code or execution begins.

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

Create an **HQ Chat** (Headquarters / Control Room) in your preferred LLM interface, using
the HQ Execution Chat Starter produced by the Creation Chat.

The HQ Chat becomes the **strategic control plane** for the project:
- Defines Phases, Milestones, and Epics
- Produces Epic specs and Epic Execution Chat Starters
- Issues Review Decisions and Delivery Authorizations
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
