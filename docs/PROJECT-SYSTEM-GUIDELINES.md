# PROJECT SYSTEM GUIDELINES
*(Authoritative Project Structure & Naming Policy)*

---

## 1. Purpose

This document defines the **authoritative project system rules** used across all projects.

It governs:
- Repository structure
- Branch naming
- Documentation organization
- Markdown usage as a programming medium
- Cross-project consistency

If any repository structure, branch name, or document conflicts with this file, **this file wins**.

---

## 2. Core Principles

- Consistency over optimization
- Markdown is a first-class artifact
- Structure enables scale

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

---

## 4. The `docs/` Folder as a Markdown Program

The `docs/` directory is a structured, executable knowledge system.

---

## 5. File Naming Conventions

Epic-level files:

```
P<phase>-M<milestone>-E<epic>__<type>__<slug>.md
```

---

## 6. Branch Naming Rules

```
phase/P2
milestone/M2.3
epic/E2.3.1
fix/<slug>
spike/<slug>
```

---

## 7. Documentation ↔ Branch Alignment

- Every active epic branch has a corresponding Epic spec

---

## 8. Decision Management

- Decisions live under `docs/decisions/`

---

## 9. System Installation Tasks

Governance changes that affect structure require a **System Installation Task**.

---

## Closing Statement

Structure is leverage.
