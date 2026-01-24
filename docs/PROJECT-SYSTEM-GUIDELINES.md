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

Only Coding Agents (and humans) are permitted to mutate the repository, including creating branches, committing files, and opening pull requests. HQ chats are declarative only and MUST NOT be assumed to have filesystem or CLI access.

Coding Agents MAY create Epic, Milestone, or Phase branches when required to fulfill an explicit execution contract. Branch creation MUST be intentional and traceable to an Epic Execution Chat Starter or a system installation task.

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

Delivery readiness includes verified commits and an explicit pull request handoff when automated PR creation is unavailable.

---

## 11.5. Human Review, Acceptance vs. Execution Completion

**Critical lifecycle distinction:** An Epic can be **execution-complete** while still requiring **human acceptance**.

### Definitions

- **Execution Completion:** All Definition of Done items are verified, code is delivered, tests pass, and the Coding Agent reports completion. This is technical correctness and delivery completeness.

- **Human Review:** After execution completion, a human (Layer 8) conducts an independent review—testing functionality, evaluating correctness against intent, identifying design issues, or uncovering unexpected behavior.

- **Acceptance:** An explicit decision made by HQ Chat (human) regarding whether to accept, accept-with-follow-ups, or reject the completed Epic based on human review findings.

### Flow

```
Coding Agent Executes
  ↓
Coding Agent Reports: "Execution Complete"
  ↓
Human Reviews (Layer 8) in natural language
  ↓
AI Structures review into Epic Review Seal (human approval, no markdown authoring required)
  ↓
HQ Chat Makes Decision: Accept | Accept-with-Followups | Reject
  ↓
Acceptance Recorded in Completion Report
```

### Key Rules

1. **Coding Agents MUST stop after reporting execution completion.** They do NOT infer acceptance.
2. **Humans OWN review.** Human judgment is a first-class input, not a rubber stamp.
3. **HQ Chat OWNS acceptance decisions.** Acceptance is recorded explicitly and becomes immutable.
4. **Follow-up work requires new Epics.** If human review identifies issues, new Epic(s) must be created; iteration without a new contract is prohibited.
5. **Acceptance decisions are recorded in the Epic Completion Report.** The report captures human findings, the decision, and any follow-up actions.
6. **Structured review artifacts are AI-generated.** Humans provide plain-language findings; Coding Agents or HQ Chat produce the Epic Review Seal from that input. Humans may approve or correct AI-structured text but are not required to author or edit markdown.

---

## 12. Epic Completion Reports (Mandatory)

Every Epic MUST conclude with an **Epic Completion Report**.

The Epic Completion Report:
- Is created once, at Epic completion
- Is stored alongside the Epic spec under `docs/phases/`
- Records what was delivered, verified, and deferred
- Serves as the durable closure artifact for the Epic
- **Includes the acceptance decision and human review findings** (if applicable)

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

Tracker integrations MUST be declared via a system reference under `docs/systems/` and MUST NOT be inferred from external tools or naming conventions.

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
