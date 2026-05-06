---
project: ai-project-system
phase: P1
milestone: M1
epic: null
type: system
status: active
last_updated: 2026-01-17
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

## Step 1 — Create the Repository

Create a new Git repository using your preferred tooling.

At minimum, the repository MUST contain:
- A `docs/` directory
- A project-level `README.md`

No code is required at this stage.

---

## Step 2 — Install Governance Documents

Copy the following governance documents into `docs/`:

- `PROJECT-SYSTEM-GUIDELINES.md`
- `AI-OPERATING-GUIDELINES.md`

These documents become **authoritative** for the project.

They MUST NOT be modified unless governance evolution is explicitly intended.

---

## Step 3 — Initialize Documentation Structure

Create the baseline documentation structure:

```
docs/
├─ README.md
├─ context/
├─ systems/
├─ phases/
├─ decisions/
└─ templates/
```


This structure enables all future work.

---

## Step 4 — Declare System Alignment

Create:

```
docs/context/system-alignment.md
```


Declare:
- Governance versions in use
- Date of alignment

This allows drift detection across projects.

---

## Step 5 — Spawn the HQ Chat

Create an **HQ Chat** (Headquarters / Control Room) in your preferred LLM interface.

The HQ Chat becomes the **strategic control plane** for the project.

HQ Chats:
- Define Phases, Milestones, and Epics
- Produce Epic specs
- Produce Epic Execution Chat Starters
- Never execute code

---

## Step 6 — Define Phase 0 or Phase 1

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
