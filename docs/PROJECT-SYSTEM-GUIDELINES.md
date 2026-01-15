# PROJECT SYSTEM GUIDELINES
*(Authoritative Project Structure, Documentation, and Execution Policy)*

---

## 1. Purpose

This document defines the **authoritative project system rules** used across all projects.

It governs:
- Repository structure
- Documentation organization (`docs/` as a system)
- Branch naming, hierarchy, and promotion
- Markdown conventions
- Execution eligibility, delivery, and closure
- Cross-project consistency

If any structure, document, or practice conflicts with this file, **this file wins**.

---

## 2. Core Principles

- Consistency over optimization
- Markdown is a first-class artifact
- Structure enables scale
- Context must be explicit and derivable
- Done must be explicit
- Delivery follows hierarchy, not convenience
- Execution contracts must be explicit at chat start

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

---

## 4. Mandatory Epic Execution Chat Starter

Every Epic execution chat MUST begin with a **complete Epic Execution Chat Starter**.

The starter is a binding execution contract and MUST include:

- Mandatory Context Packet (project, phase, milestone, epic, spec path)
- Explicit scope and non-goals
- Governance enforcement statement
- Definition of Done reminder
- **Delivery Requirements**, including:
  - Working branch name (`epic/*`)
  - Required PR source and target
  - Explicit statement that delivery is part of completion

Execution chats that do not include delivery requirements are invalid.

---

## 5. Branch Promotion Rules (Reminder)

```
epic/*      → milestone/*
milestone/* → phase/*
phase/*     → develop
```

---

## Closing Statement

Execution must be explicit from first message to final report.
