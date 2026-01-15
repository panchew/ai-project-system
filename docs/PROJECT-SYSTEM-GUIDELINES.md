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
- Execution eligibility
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

Front-matter defines document identity, scope, and lifecycle and enables deterministic context extraction.

### Required Front-Matter

```
---
project: <project-name>
phase: P<id>
milestone: M<id>
epic: E<id> | null
type: <spec | decision | system | task | reference>
status: <draft | active | completed | deprecated>
last_updated: YYYY-MM-DD
---
```

### Applicability

Front-matter is **mandatory** for:
- Phase, milestone, and epic specs
- Decisions
- System installation tasks
- Operational system references

Front-matter is **not required** for:
- Governance documents
- Index files (README)
- Transitional notices

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
- No ambiguous names (`notes.md`, `temp.md`)

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

## 10. System Installation Tasks

Governance changes that affect structure or conventions require a **System Installation Task**.

Such tasks are:
- One-time
- Explicitly scoped
- Execution-only
- Delegated to a Coding Agent

---

## 11. Adoption & Evolution

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
