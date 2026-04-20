---
project: ai-project-system
phase: P2
milestone: M6
epic: E6.1
type: spec
status: active
last_updated: 2026-04-19
---

# Governance Folder Structure Spec

**Epic:** E6.1 — Define `/governance` Folder Structure
**Produced by:** Coding Agent during E6.1 execution
**Purpose:** Authoritative migration target for E6.2 and all subsequent M6 epics

---

## 1. Overview

This document defines the canonical `/governance` folder layout for the AI Project System. It is the single authoritative reference for:

- **E6.2** — which files to move and where
- **E6.3** — where `.ai-project.yml` will reference governance paths
- **E6.4** — what the git submodule exposes
- **E6.5** — what the migration guide instructs adopters to replicate
- **M7 CLI** — what `ai-project init` scaffolds
- **M8 HQ Agent** — where it finds governance files

No files are created or moved in E6.1. This document describes the target state. E6.2 executes the migration.

---

## 2. Audit: Governance vs. Project Artifact Classification

Before defining the target structure, all files in `docs/` were classified as either **governance** (portable system rules) or **project artifact** (history of this specific project).

### 2.1 Governance Files (→ move to `/governance/`)

These files are the system itself. They are portable and referenceable via submodule.

| Current Path | Classification | Target Path |
|---|---|---|
| `docs/PROJECT-SYSTEM-GUIDELINES.md` | Canonical governance doc (authority L1) | `governance/PROJECT-SYSTEM-GUIDELINES.md` |
| `docs/AI-OPERATING-GUIDELINES.md` | Canonical governance doc (authority L2) | `governance/AI-OPERATING-GUIDELINES.md` |
| `docs/EPIC-EXECUTION-CHAT-STARTER.md` | Canonical format reference (authority L3) | `governance/EPIC-EXECUTION-CHAT-STARTER.md` |
| `docs/FAQ.md` | System FAQ (informational reference) | `governance/guides/FAQ.md` |
| `docs/QUICK-START.md` | Onboarding guide (informational reference) | `governance/guides/QUICK-START.md` |
| `docs/governance-source.md` | Adoption declaration template | `governance/templates/governance-source.md` |
| `docs/templates/README.md` | Templates index | `governance/templates/README.md` |
| `docs/templates/epic-spec.md` | Epic spec template | `governance/templates/epic-spec.md` |
| `docs/templates/epic-completion-report.md` | Completion report template | `governance/templates/epic-completion-report.md` |
| `docs/templates/epic-completion-notice.md` | Delivery notice template | `governance/templates/epic-completion-notice.md` |
| `docs/templates/epic-execution-chat-starter.md` | Chat starter template | `governance/templates/epic-execution-chat-starter.md` |
| `docs/templates/epic-review-seal.md` | Review seal template | `governance/templates/epic-review-seal.md` |
| `docs/templates/milestone-spec.md` | Milestone spec template | `governance/templates/milestone-spec.md` |
| `docs/templates/milestone-closure-declaration.md` | Milestone closure template | `governance/templates/milestone-closure-declaration.md` |
| `docs/templates/phase-spec.md` | Phase spec template | `governance/templates/phase-spec.md` |
| `docs/systems/hq-chat.md` | HQ Chat system reference | `governance/systems/hq-chat.md` |
| `docs/systems/hq-chat-opener.md` | HQ Chat opening protocol | `governance/systems/hq-chat-opener.md` |
| `docs/systems/epic-execution-chat-starter.md` | Chat starter system reference | `governance/systems/epic-execution-chat-starter.md` |
| `docs/systems/governance-propagation.md` | Governance propagation model | `governance/systems/governance-propagation.md` |
| `docs/systems/PROJECT-TRACKER-INTEGRATION-SYSTEM.md` | Tracker integration system | `governance/systems/PROJECT-TRACKER-INTEGRATION-SYSTEM.md` |
| `docs/systems/start-a-project.md` | New project guide | `governance/systems/start-a-project.md` |
| `docs/diagrams/authority-hierarchy.md` | Authority hierarchy diagram | `governance/diagrams/authority-hierarchy.md` |
| `docs/diagrams/epic-lifecycle-flow.md` | Epic lifecycle flow diagram | `governance/diagrams/epic-lifecycle-flow.md` |
| `docs/diagrams/repository-structure.md` | Repository structure diagram | `governance/diagrams/repository-structure.md` |

### 2.2 Project Artifact Files (stay in `docs/`)

These files are the history of this specific project. They are not portable and must remain in `docs/`.

| Path | Classification |
|---|---|
| `docs/README.md` | Docs system index (project-specific) |
| `docs/LICENSE` | Project license |
| `docs/_legacy/` | Legacy project files |
| `docs/admin/` | Administrative correction records |
| `docs/context/` | Runtime project context (project-tracker.md) |
| `docs/decisions/` | Project decisions |
| `docs/phases/` | All phase/milestone/epic execution artifacts |
| `docs/roadmap/` | This project's roadmap |

---

## 3. Canonical `/governance` Folder Layout

The complete target structure after E6.2 migration:

```
/governance/
├── README.md                               # Folder overview, authority hierarchy, submodule usage
├── PROJECT-SYSTEM-GUIDELINES.md            # Authoritative execution rules (Authority Level 1)
├── AI-OPERATING-GUIDELINES.md              # Authoritative AI behavior rules (Authority Level 2)
├── EPIC-EXECUTION-CHAT-STARTER.md          # Canonical chat starter format reference (Authority Level 3)
│
├── agents/
│   └── hq.agent.md                         # HQ Chat agent definition (M8 deliverable — placeholder in E6.2)
│
├── diagrams/
│   ├── authority-hierarchy.md              # Mermaid diagram: authority hierarchy
│   ├── epic-lifecycle-flow.md              # Mermaid diagram: epic lifecycle
│   └── repository-structure.md            # Mermaid diagram: repository structure
│
├── guides/
│   ├── QUICK-START.md                      # Onboarding guide for new adopters
│   └── FAQ.md                              # Frequently asked questions
│
├── systems/
│   ├── hq-chat.md                          # HQ Chat system reference
│   ├── hq-chat-opener.md                   # HQ Chat opening protocol reference
│   ├── epic-execution-chat-starter.md      # Epic Execution Chat Starter system reference
│   ├── governance-propagation.md           # Governance propagation model
│   ├── PROJECT-TRACKER-INTEGRATION-SYSTEM.md  # Project tracker integration system
│   └── start-a-project.md                  # New project guide
│
└── templates/
    ├── README.md                           # Templates index and usage guide
    ├── epic-spec.md                        # Epic specification template
    ├── epic-completion-report.md           # Epic completion report template
    ├── epic-completion-notice.md           # Epic delivery notice template
    ├── epic-execution-chat-starter.md      # Epic execution chat starter template
    ├── epic-review-seal.md                 # Epic review seal template
    ├── milestone-spec.md                   # Milestone specification template
    ├── milestone-closure-declaration.md    # Milestone closure declaration template
    ├── phase-spec.md                       # Phase specification template
    └── governance-source.md               # Governance adoption declaration template
```

---

## 4. Subdirectory Definitions

### `governance/` (root)

The root of the governance folder contains only the three canonical governance documents and the README. All other content is organized into subdirectories.

| File | Purpose | Authority |
|---|---|---|
| `README.md` | Folder orientation — what this folder contains, how to use it, how to reference via submodule | Informational |
| `PROJECT-SYSTEM-GUIDELINES.md` | Authoritative project structure, documentation, and execution policy | Level 1 (highest) |
| `AI-OPERATING-GUIDELINES.md` | Authoritative AI usage and execution policy | Level 2 |
| `EPIC-EXECUTION-CHAT-STARTER.md` | Canonical chat starter format reference | Level 3 |

### `governance/agents/`

Contains AI agent definition files. This subfolder exists so that `ai-project init` (M7) knows exactly where to place agent files, and the HQ Chat agent (M8) has a canonical home.

| File | Purpose | Status |
|---|---|---|
| `hq.agent.md` | VS Code Copilot custom agent for HQ Chat | Placeholder in E6.2; full content delivered in M8 |

### `governance/diagrams/`

Contains Mermaid-rendered diagrams that visually document the governance system. These are explanatory only — they carry no authority.

| File | Purpose |
|---|---|
| `authority-hierarchy.md` | Visualizes the authority hierarchy (which document wins conflicts) |
| `epic-lifecycle-flow.md` | Visualizes the epic lifecycle from spec to closure |
| `repository-structure.md` | Visualizes the canonical repository folder structure |

### `governance/guides/`

Contains informational guides for humans adopting the system. No authority — guides describe and explain, not govern.

| File | Purpose |
|---|---|
| `QUICK-START.md` | End-to-end walkthrough for new adopters; first thing to read after README |
| `FAQ.md` | Answers to common questions about philosophy, usage, and adoption |

### `governance/systems/`

Contains operational system references: documents that describe how specific systems within the governance framework work. These are implementation guidance, not policy authority.

| File | Purpose |
|---|---|
| `hq-chat.md` | How to operate the HQ Chat; scope, responsibilities, constraints |
| `hq-chat-opener.md` | The opening protocol for HQ Chat sessions |
| `epic-execution-chat-starter.md` | How HQ Chat generates Epic Execution Chat Starters |
| `governance-propagation.md` | How governance propagates to adopting projects; the reference model |
| `PROJECT-TRACKER-INTEGRATION-SYSTEM.md` | How to declare and integrate a project tracker |
| `start-a-project.md` | Step-by-step guide for starting a new project under governance |

### `governance/templates/`

Contains fillable templates for all governance artifact types. Templates carry no authority — they are structure, not policy.

| File | Purpose |
|---|---|
| `README.md` | Templates index: lists all templates with usage notes |
| `epic-spec.md` | Template for writing an Epic specification |
| `epic-completion-report.md` | Template for the Epic completion report |
| `epic-completion-notice.md` | Template for the Epic delivery notice |
| `epic-execution-chat-starter.md` | Template for generating an Epic Execution Chat Starter |
| `epic-review-seal.md` | Template for the Epic Review Seal |
| `milestone-spec.md` | Template for writing a Milestone specification |
| `milestone-closure-declaration.md` | Template for the Milestone Closure Declaration |
| `phase-spec.md` | Template for writing a Phase specification |
| `governance-source.md` | Template for a project's governance adoption declaration |

---

## 5. Authority Hierarchy Within `/governance`

The authority hierarchy applies when two documents appear to conflict. Higher-level documents always win.

| Level | Document(s) | Type |
|---|---|---|
| 1 (highest) | `PROJECT-SYSTEM-GUIDELINES.md` | Canonical policy |
| 2 | `AI-OPERATING-GUIDELINES.md` | Canonical policy |
| 3 | `EPIC-EXECUTION-CHAT-STARTER.md` | Canonical format reference |
| 4 | `systems/` files | Operational guidance |
| 5 | `templates/` files | Structure only (no authority) |
| 6 | `guides/` files | Informational only (no authority) |
| 7 | `diagrams/` files | Visual documentation (no authority) |
| 8 | `agents/` files | Agent definitions (executed as instructed by Level 1–2) |

**Resolution rule:** When any conflict arises, escalate to the highest applicable authority level. If the conflict cannot be resolved by reference to an existing document, it must be resolved explicitly by a new decision (documented in `docs/decisions/` of the adopting project).

---

## 6. Naming Conventions

### 6.1 Root-Level Governance Documents

Canonical governance documents at the root of `/governance/` use **ALL-CAPS-WITH-HYPHENS** naming. This signals highest authority and makes them visually distinct.

Examples:
- `PROJECT-SYSTEM-GUIDELINES.md` ✓
- `AI-OPERATING-GUIDELINES.md` ✓
- `EPIC-EXECUTION-CHAT-STARTER.md` ✓

### 6.2 Subdirectory Files

All files within subdirectories use **kebab-case** (lowercase, hyphen-separated) naming.

Examples:
- `epic-spec.md` ✓
- `hq-chat.md` ✓
- `governance-source.md` ✓

Exception: `PROJECT-TRACKER-INTEGRATION-SYSTEM.md` retains its ALL-CAPS naming in `systems/` because it predates this convention and changing it would break existing references. E6.2 will retain the original name.

### 6.3 Subdirectory Names

All subdirectory names use **lowercase single-word** naming.

- `agents/` ✓
- `diagrams/` ✓
- `guides/` ✓
- `systems/` ✓
- `templates/` ✓

### 6.4 Agent Files

Agent files use the `<name>.agent.md` convention, matching the VS Code Copilot custom agent file format.

- `hq.agent.md` ✓

---

## 7. Draft: `/governance/README.md`

The following is the content to be created as `governance/README.md` in E6.2:

---

```markdown
# AI Project System — Governance

This folder contains all governance files for the AI Project System.

**Governance files are portable.** External projects may reference this folder as a git submodule to adopt the AI Project System governance without copying files manually.

---

## What Is In This Folder

| Item | Purpose |
|---|---|
| `PROJECT-SYSTEM-GUIDELINES.md` | Authoritative project structure and execution rules |
| `AI-OPERATING-GUIDELINES.md` | Authoritative AI agent behavior rules |
| `EPIC-EXECUTION-CHAT-STARTER.md` | Canonical Epic Execution Chat Starter format reference |
| `agents/` | AI agent definition files (VS Code Copilot custom agents) |
| `diagrams/` | Visual documentation of the governance system |
| `guides/` | Onboarding and FAQ for human adopters |
| `systems/` | Operational system reference documents |
| `templates/` | Fillable templates for all governance artifact types |

---

## Authority Hierarchy

When documents conflict, higher levels win:

1. `PROJECT-SYSTEM-GUIDELINES.md` — highest authority
2. `AI-OPERATING-GUIDELINES.md`
3. `EPIC-EXECUTION-CHAT-STARTER.md`
4. `systems/` — operational guidance
5. `templates/`, `guides/`, `diagrams/` — no authority (structure and information only)

---

## How to Adopt This Governance (Git Submodule)

To reference this governance folder from an external project:

```sh
# Add as a submodule
git submodule add https://github.com/panchew/ai-project-system.git governance

# Pin to a specific governance version
cd governance && git checkout v2.0.0
```

Then create a `governance-source.md` at your project root declaring the adoption (use `governance/templates/governance-source.md` as the template).

See `guides/QUICK-START.md` for the full onboarding walkthrough.

---

## Governance Version

This governance folder will be versioned at `v2.0.0` upon completion of Milestone M6 (the migration that creates this folder).
```

---

## 8. E6.2 Migration Checklist

The following actions are required in E6.2. This list is the complete migration target derived from this spec.

**Files to create:**
- [ ] `governance/README.md` (content defined in Section 7 above)
- [ ] `governance/agents/hq.agent.md` (placeholder — full content in M8)

**Files to move from `docs/` to `governance/`:**
- [ ] `docs/PROJECT-SYSTEM-GUIDELINES.md` → `governance/PROJECT-SYSTEM-GUIDELINES.md`
- [ ] `docs/AI-OPERATING-GUIDELINES.md` → `governance/AI-OPERATING-GUIDELINES.md`
- [ ] `docs/EPIC-EXECUTION-CHAT-STARTER.md` → `governance/EPIC-EXECUTION-CHAT-STARTER.md`
- [ ] `docs/FAQ.md` → `governance/guides/FAQ.md`
- [ ] `docs/QUICK-START.md` → `governance/guides/QUICK-START.md`
- [ ] `docs/governance-source.md` → `governance/templates/governance-source.md`
- [ ] `docs/templates/README.md` → `governance/templates/README.md`
- [ ] `docs/templates/epic-spec.md` → `governance/templates/epic-spec.md`
- [ ] `docs/templates/epic-completion-report.md` → `governance/templates/epic-completion-report.md`
- [ ] `docs/templates/epic-completion-notice.md` → `governance/templates/epic-completion-notice.md`
- [ ] `docs/templates/epic-execution-chat-starter.md` → `governance/templates/epic-execution-chat-starter.md`
- [ ] `docs/templates/epic-review-seal.md` → `governance/templates/epic-review-seal.md`
- [ ] `docs/templates/milestone-spec.md` → `governance/templates/milestone-spec.md`
- [ ] `docs/templates/milestone-closure-declaration.md` → `governance/templates/milestone-closure-declaration.md`
- [ ] `docs/templates/phase-spec.md` → `governance/templates/phase-spec.md`
- [ ] `docs/systems/hq-chat.md` → `governance/systems/hq-chat.md`
- [ ] `docs/systems/hq-chat-opener.md` → `governance/systems/hq-chat-opener.md`
- [ ] `docs/systems/epic-execution-chat-starter.md` → `governance/systems/epic-execution-chat-starter.md`
- [ ] `docs/systems/governance-propagation.md` → `governance/systems/governance-propagation.md`
- [ ] `docs/systems/PROJECT-TRACKER-INTEGRATION-SYSTEM.md` → `governance/systems/PROJECT-TRACKER-INTEGRATION-SYSTEM.md`
- [ ] `docs/systems/start-a-project.md` → `governance/systems/start-a-project.md`
- [ ] `docs/diagrams/authority-hierarchy.md` → `governance/diagrams/authority-hierarchy.md`
- [ ] `docs/diagrams/epic-lifecycle-flow.md` → `governance/diagrams/epic-lifecycle-flow.md`
- [ ] `docs/diagrams/repository-structure.md` → `governance/diagrams/repository-structure.md`

**Files to update (internal reference paths):**
- [ ] All internal links in moved files pointing to `docs/` governance paths must be updated to `governance/` paths
- [ ] `docs/README.md` — update structure diagram to reference `/governance/` instead of embedded governance files
- [ ] `PROJECT-SYSTEM-GUIDELINES.md` (after move) — update canonical repository structure in Section 3
- [ ] Version bump: governance version to `v2.0.0` in both canonical governance documents

**Files that remain in `docs/`:**
- `docs/README.md`, `docs/LICENSE`, `docs/_legacy/`, `docs/admin/`, `docs/context/`, `docs/decisions/`, `docs/phases/`, `docs/roadmap/`
