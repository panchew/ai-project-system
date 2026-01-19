# AI Project System

A formal, governed documentation system for AI-assisted project execution.

---

## What This Is

This repository contains the **canonical AI Project System** used to structure, document, and execute software projects with AI assistance.

It defines:
- Authoritative governance documents
- A Phase–Milestone–Epic execution model
- A documentation-first workflow
- Explicit context management for AI agents

This is **not an application**.  
It is a **system for managing projects**.

---

## Who This Is For

This system is designed for:
- Engineers using AI tools (ChatGPT, Copilot, Coding Agents)
- Projects where context, scope, and delivery matter
- People who want repeatability, not improvisation

It assumes:
- Git
- Markdown
- Willingness to trade speed for correctness (at first)

---

## Getting Started (Recommended Path)

If you want to **use this system in a project**:

1. Start with **governance**
   - Read [`docs/PROJECT-SYSTEM-GUIDELINES.md`](docs/PROJECT-SYSTEM-GUIDELINES.md)
   - Read [`docs/AI-OPERATING-GUIDELINES.md`](docs/AI-OPERATING-GUIDELINES.md)

2. Understand how projects are started
   - Read [`docs/systems/start-a-project.md`](docs/systems/start-a-project.md)
   - Read [`docs/systems/hq-chat.md`](docs/systems/hq-chat.md)

3. Explore the documentation structure
   - [`docs/README.md`](docs/README.md)
   - [`docs/phases/`](docs/phases/)

You do **not** need to read everything to begin.  
The system is designed to be learned incrementally.

---

## Current Project Status

This repository is **dogfooding its own system**.

- **Phase:** P1 — System Foundation & Adoption
- **Milestones:**
  - ✅ M1 — Genesis & Integration Baseline (completed)
  - ⏳ M2 — (planned, not yet active)

Governance is considered **stable and usable**.
Future work is intentionally paced.

---

## How Progress Is Tracked

Progress is reflected in **three complementary ways**:

1. **Documentation (authoritative)**
   - Phase, Milestone, and Epic state lives in `docs/`
   - Completion reports are explicit and versioned

2. **Git history**
   - Branch hierarchy reflects execution flow
   - Commits and PRs correspond to closed Epics

3. **Project Tracker (assistive)**
   - GitHub Projects is used for planning and visibility
   - Tracker state does **not** override documentation

If there is ever a conflict, **documentation wins**.

---

## Where to Look for Truth

- Governance rules → `docs/PROJECT-SYSTEM-GUIDELINES.md`
- AI behavior rules → `docs/AI-OPERATING-GUIDELINES.md`
- How to operate the system → `docs/systems/`
- What’s active → `docs/phases/`

Chats are ephemeral.  
Markdown is authoritative.

---

## Status of the System

The system is:
- ✔ Validated through real execution
- ✔ In active use for other projects
- ✔ Evolving deliberately, not continuously

New capabilities (CLI, web UI) are **intentionally deferred** until real usage demands them.

---

## License

This is a personal project system.
No license is currently specified.
