# PROJECT SYSTEM GUIDELINES
*(Authoritative Project Structure, Documentation, and Execution Policy)*

---

## 1. Purpose

This document defines the **authoritative project system rules** used across all projects.

It governs:
- Repository structure
- Documentation organization (`docs/` as a system)
- Branch naming and intent
- Markdown conventions
- Execution eligibility and closure
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

Front-matter defines document identity, scope, lifecycle, and enables deterministic context extraction.

### Required Front-Matter

```
---
project: <project-name>
phase: P<id>
milestone: M<id>
epic: E<id>
type: <spec | decision | system | task | completion | reference>
status: <draft | active | completed | deprecated>
last_updated: YYYY-MM-DD
---
```

Execution context MUST be derivable from front-matter.

---

## 6. File Naming Conventions

Epic-level files:

```
P<phase>-M<milestone>-E<epic>__<type>__<slug>.md
```

Where `<type>` includes:
- `spec`
- `completion`
- `decision`
- `system`
- `task`
- `reference`

Rules:
- Filenames must be meaningful in isolation
- Dates use `YYYY-MM-DD`
- No ambiguous names

---

## 7. Branch Naming Rules

Branches represent **intent**, not individuals.

```
phase/P2
milestone/M2.3
epic/E2.3.1
fix/<slug>
spike/<slug>
```

One epic branch corresponds to one epic spec.

---

## 8. Documentation ↔ Branch Alignment

- Every active epic branch MUST have a corresponding epic spec
- Specs without branches are not in execution
- Execution work without a spec is invalid

---

## 9. Decision Management

- Decisions live under `docs/decisions/`
- Decisions are immutable once accepted
- Changes require a new decision document

---

## 10. Definition of Done (Mandatory)

Every **Epic spec MUST include a Definition of Done**.

The Definition of Done:
- Defines the exit condition for execution chats
- Authorizes Coding Agents to conclude work autonomously
- Prevents ambiguous or open-ended execution

Execution chats MUST:
- Evaluate progress against the Definition of Done
- Declare completion explicitly once all criteria are met
- Produce an Epic Completion Report
- Stop once the Epic is complete

---

## 11. Epic Completion Reports (Mandatory)

Every Epic MUST conclude with an **Epic Completion Report**.

The Epic Completion Report:
- Is created once, at Epic completion
- Is stored alongside the Epic spec under `docs/phases/`
- Records what was delivered, verified, and deferred
- Serves as the durable closure artifact for the Epic

Completion Reports are **append-only** and MUST NOT modify the original Epic spec.

---

## 12. System Installation Tasks

Governance changes that affect structure or conventions require a **System Installation Task**.

Such tasks are:
- One-time
- Explicitly scoped
- Execution-only
- Delegated to a Coding Agent

---

## 13. Canonical Epic Spec Template

All Epic specs MUST follow this structure.

```
---
project: <project-name>
phase: P<id>
milestone: M<id>
epic: E<id>
type: spec
status: active
last_updated: YYYY-MM-DD
---

# Epic: <Epic Name>

## Objective
<Why this epic exists>

## In Scope
<Explicit inclusions>

## Out of Scope
<Explicit exclusions>

## Constraints
- Tech stack:
- Architectural rules:
- Operational constraints:

## Acceptance Criteria
- <What must be true for success>

## Definition of Done
This Epic is complete when:

- [ ] All scoped work is implemented
- [ ] Automated tests are added or updated
- [ ] Code coverage does not regress (if applicable)
- [ ] CI pipeline passes
- [ ] Code is committed to the epic branch
- [ ] A pull request is opened or merged (as appropriate)
- [ ] Documentation is updated if required
- [ ] Epic Completion Report is created

## Authoritative References
- Decisions: <paths>
- Systems: <paths>
```

---

## 14. Adoption & Evolution

- Adopted at project creation
- Enforced forward-only
- Evolution is intentional, not accidental

---

## Closing Statement

This project system exists to:
- Reduce friction
- Preserve clarity
- Enable parallel work
- Support AI-native workflows

Structure is not bureaucracy.  
Structure is leverage.
