# Documentation System

This directory contains the **project history and execution artifacts** for this project.

Governance files (rules, templates, system references) live in `/governance/`.

All project execution history lives here:
- Plans and phases
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
├─ roadmap/
├─ phases/
├─ decisions/
├─ context/
└─ _legacy/
```

Governance documents are in `/governance/`. See [`/governance/README.md`](../governance/README.md) for the governance structure.

---

## Folder Responsibilities

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

Epic specs are the **primary execution drivers**.

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
- Governance files belong in `/governance/`, not `docs/`
- Execution work requires an Epic spec with valid front-matter
- Meaning is preserved; structure may evolve

---

## Operating Principle

> **Structure enables clarity.  
> Clarity enables scale.**

If documentation placement is unclear, update this file before adding new content.
