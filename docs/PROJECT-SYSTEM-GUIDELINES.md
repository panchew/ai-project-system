# PROJECT SYSTEM GUIDELINES
*(Authoritative Project Structure, Documentation, and Execution Policy)*

**Version:** 1.3.0  
**Effective Date:** 2026-01-17  
**Status:** Current  

---

## 1. Purpose

This document defines the **authoritative project system rules** used across all projects.

It governs:
- Repository structure
- Documentation organization (`docs/` as a system)
- Branch naming, hierarchy, and promotion
- Markdown conventions and front-matter
- Execution eligibility, delivery, and closure
- AI-assisted execution behavior
- Cross-project consistency

If any structure, document, or practice conflicts with this file, **this file wins**.

---

## 2. Core Principles

- **Consistency over optimization**  
  Predictability is more valuable than local perfection.

- **Markdown is a first-class artifact**  
  Durable knowledge lives in versioned Markdown files.

- **Structure enables scale**  
  Clear structure allows parallel work without coordination overhead.

- **Context must be explicit and derivable**  
  Execution context must be mechanically extractable, not remembered.

- **Done must be explicit**  
  Execution units must define and record their own completion.

- **Delivery follows hierarchy, not convenience**  
  Branch promotion is governed, not inferred.

---

## 3. Canonical Repository Structure

```
/
├─ docs/
│  ├─ README.md
│  ├─ PROJECT-SYSTEM-GUIDELINES.md
│  ├─ AI-OPERATING-GUIDELINES.md
│  ├─ roadmap/
│  ├─ phases/
│  ├─ decisions/
│  ├─ context/
│  ├─ systems/
│  ├─ templates/
│  └─ _legacy/
├─ src/
├─ tests/
└─ README.md
```

All durable project knowledge lives under `docs/`.

---

## 4. The `docs/` Folder as a System

The `docs/` directory is a **structured, executable knowledge system**, not passive documentation.

Rules:
- Documentation precedes execution
- Specs drive implementation
- Decisions are explicit and immutable
- Context is preserved independently of chats

Chats are ephemeral.  
Markdown is authoritative.

Local enforcement is defined in `docs/README.md`.

---

## 5. Mandatory Document Front-Matter

All **execution-relevant Markdown documents** MUST begin with a YAML front-matter block.

### Required Front-Matter

```
---
project: <project-name>
phase: P<id>
milestone: M<id>
epic: E<id> | null
type: <spec | decision | system | task | completion | reference>
status: <draft | active | completed | deprecated>
last_updated: YYYY-MM-DD
---
```

Front-matter is mandatory for:
- Phase, milestone, and epic specs
- Decisions
- System installation tasks
- Operational system references
- Epic completion reports

Front-matter is not required for:
- Governance documents
- Index files (README)
- Templates

Execution context MUST be derivable from front-matter.

---

## 6. File Naming Conventions

Epic-level files:

```
P<phase>-M<milestone>-E<epic>__<type>__<slug>.md
```

Rules:
- Filenames must be meaningful in isolation
- Dates use `YYYY-MM-DD`
- No ambiguous names

---

## 7. Branch Naming Rules

Branches represent **intent**, not individuals.

```
phase/P<id>
milestone/M<id>
epic/E<id>
fix/<slug>
spike/<slug>
```

One epic branch corresponds to one epic spec.

---

## 8. Branch Promotion Rules (Mandatory)

Branch merges MUST follow the project hierarchy.

### Promotion Path

```
epic/*      → milestone/*
milestone/* → phase/*
phase/*     → develop
```

### Rules

- Epic branches MUST only open PRs against their parent milestone branch
- Milestone branches MUST only open PRs against their parent phase branch
- Phase branches are promoted to `develop` only once all milestones are integrated
- Direct PRs that skip hierarchy levels are invalid
- If the correct target branch does not exist, execution MUST pause for clarification

These rules override conventional Git workflows.

---

## 9. Documentation ↔ Branch Alignment

- Every active epic branch MUST have a corresponding epic spec
- Specs without branches are not in execution
- Execution work without a spec is invalid

---

## 10. Decision Management

- Decisions live under `docs/decisions/`
- Decisions are immutable once accepted
- Changes require a new decision document

---

## 11. Definition of Done (Mandatory)

Every **Epic spec MUST include a Definition of Done**.

The Definition of Done:
- Defines the exit condition for execution chats
- Authorizes Coding Agents to conclude work autonomously
- Prevents ambiguous or open-ended execution

Execution chats MUST:
- Validate all Definition of Done items
- Open a PR against the **correct milestone branch**
- Produce an Epic Completion Report
- Declare completion explicitly and stop

---

## 12. Epic Completion Reports (Mandatory)

Every Epic MUST conclude with an **Epic Completion Report**.

The Epic Completion Report:
- Is created once, at Epic completion
- Is stored alongside the Epic spec under `docs/phases/`
- Records what was delivered, verified, and deferred
- Serves as the durable closure artifact for the Epic

Completion Reports are append-only and MUST NOT modify the original Epic spec.

---

## 13. Epic Execution Chat Starter (Mandatory)

Every Epic execution chat MUST begin with a **complete Epic Execution Chat Starter**.

The starter is a binding execution contract and MUST include:
- Mandatory Context Packet
- Explicit scope and non-goals
- Governance enforcement statement
- Definition of Done reminder
- Delivery Requirements (branch + PR target)

Execution chats that omit delivery requirements are invalid.

A canonical template is provided under:

```
docs/templates/epic-execution-chat-starter.md
```

---

## 14. Project Tracker Integration (Optional, Declarative)

Projects **may declare integrations with external project trackers** (e.g. Jira, Azure DevOps, GitHub Projects, Pivotal Tracker) via **system references**.

Such integrations:
- Are optional
- Must be explicitly declared
- Must not replace the canonical project structure

Details are defined in the Project Tracker Integration System reference.

---

## 15. Canonical Epic Spec Template

All Epic specs MUST follow the canonical structure defined in:

```
docs/templates/epic-spec.md
```

---

## 16. System Installation Tasks

Governance changes that affect structure or conventions require a **System Installation Task**.

Such tasks are:
- One-time
- Explicitly scoped
- Execution-only
- Delegated to a Coding Agent

---

## 17. Adoption & Evolution

- Adopted at project creation
- Enforced forward-only
- Evolution is intentional, additive, and versioned

---

## Closing Statement

This project system exists to:
- Reduce friction
- Preserve clarity
- Enable parallel work
- Support AI-native workflows

Structure is not bureaucracy.  
Structure is leverage.
