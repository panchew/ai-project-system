# Documentation System

This directory is the **canonical, authoritative knowledge system** for this project.

All durable project knowledge lives here:
- Governance
- Plans
- Specifications
- Decisions
- Context

Chats are **not** a source of truth.  
Code does **not** replace documentation.

---

## Canonical Structure

```
docs/
├─ README.md
├─ PROJECT-SYSTEM-GUIDELINES.md
├─ AI-OPERATING-GUIDELINES.md
├─ roadmap/
├─ phases/
├─ decisions/
├─ context/
└─ _legacy/
```

This structure is intentional and enforced going forward.

---

## Folder Responsibilities

### `PROJECT-SYSTEM-GUIDELINES.md`
Authoritative rules for:
- Repository structure
- Naming conventions
- Branching strategy
- Documentation organization

### `AI-OPERATING-GUIDELINES.md`
Authoritative rules for:
- HQ chats
- Execution chats
- Coding agents
- Context handling

---

### `roadmap/`
High-level planning and forward-looking documents.
- Vision
- Phases overview
- Long-term sequencing

No implementation details.

---

### `phases/`
Execution-aligned documentation.
- Phase specs
- Milestone specs
- Epic specs

Epic files are the **primary execution drivers**.

---

### `decisions/`
Immutable records of important decisions.
- Architecture
- Trade-offs
- Constraints

Decisions are never edited once accepted.
Changes require a new decision.

---

### `context/`
Supporting and reference material.
- System reference architectures
- Background research
- Proven patterns
- External references

Context informs decisions but is not automatically binding.

---

### `_legacy/`
Historical documentation retained for reference.
- Pre-system documents
- Unaligned or deprecated material

**No new files** should be added here.

---

## Enforcement Rules

- New documentation **must** be placed in the correct folder
- Files at the root of `docs/` are limited to governance and indexes
- Meaning is preserved; structure may evolve
- Execution work requires an Epic spec

---

## Operating Principle

> **Structure enables clarity.  
> Clarity enables scale.**

If documentation placement is unclear, update this file before adding new content.
