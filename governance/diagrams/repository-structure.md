# Repository Structure

This diagram shows the canonical file and folder structure of an AI Project System repository.

---

## Directory Tree

```
ai-project-system/
│
├── README.md                           # Repository front door
├── LICENSE                             # Project license
│
├── governance/                         # All governance files live here
│   │
│   ├── README.md                       # Governance folder overview
│   │
│   ├── PROJECT-SYSTEM-GUIDELINES.md    # Level 1 authority (system structure)
│   ├── AI-OPERATING-GUIDELINES.md      # Level 2 authority (execution procedures)
│   ├── EPIC-EXECUTION-CHAT-STARTER.md  # Level 3 authority (chat starter format)
│   │
│   ├── agents/                         # AI agent definition files
│   │   └── hq.agent.md                 # HQ Chat agent (M8 deliverable)
│   │
│   ├── diagrams/                       # Visual documentation
│   │   ├── epic-lifecycle-flow.md      # How Epics move from idea → closure
│   │   ├── authority-hierarchy.md      # Document precedence rules
│   │   └── repository-structure.md     # This file
│   │
│   ├── guides/                         # Onboarding and FAQ for human adopters
│   │   ├── QUICK-START.md              # 30-minute onboarding walkthrough
│   │   └── FAQ.md                      # Frequently asked questions
│   │
│   ├── systems/                        # System operation guides
│   │   ├── epic-execution-chat-starter.md
│   │   ├── governance-propagation.md
│   │   ├── hq-chat-opener.md
│   │   ├── hq-chat.md
│   │   ├── PROJECT-TRACKER-INTEGRATION-SYSTEM.md
│   │   └── start-a-project.md
│   │
│   └── templates/                      # Reusable spec templates
│       ├── README.md
│       ├── phase-spec.md
│       ├── milestone-spec.md
│       ├── epic-spec.md
│       ├── epic-execution-chat-starter.md
│       ├── epic-completion-report.md
│       ├── epic-completion-notice.md
│       ├── epic-review-seal.md
│       └── governance-source.md
│
├── docs/                               # Project history and execution artifacts
│   │
│   ├── README.md                       # Documentation index
│   │
│   ├── phases/                         # Phase–Milestone–Epic hierarchy
│   │   ├── P0__phase__project-formalization.md
│   │   ├── P0-M0.1__milestone__repository-bootstrap.md
│   │   ├── P0-M0.1-E0.1.1__epic__formalize-system-repository.md
│   │   ├── P0-M0.1-E0.1.1__completion__retired.md
│   │   │
│   │   └── P1__System_Foundation_and_Adoption/
│   │       ├── P1__phase.md
│   │       ├── P1-M1__milestone.md
│   │       ├── P1-M1-E1.1__spec__project-tracker-integration-system.md
│   │       ├── P1-M1-E1.1__completion__project-tracker-integration-system.md
│   │       ├── P1-M2__milestone.md
│   │       ├── P1-M2-E2.1__spec__human-review-and-acceptance.md
│   │       ├── P1-M2-E2.1__completion__human-review-and-acceptance.md
│   │       ├── [... additional Epics ...]
│   │       └── P1-M4-E4.2__spec__quick-start-guide-and-visual-documentation.md
│   │
│   ├── roadmap/                        # Project roadmap and planning
│   │   └── overview.md
│   │
│   ├── context/                        # Project context and tracking
│   │   └── project-tracker.md
│   │
│   ├── decisions/                      # Architectural decision records (future)
│   │   └── [ADRs will live here]
│   │
│   ├── admin/                          # Administrative records
│   │   └── [Administrative corrections and notices]
│   │
│   └── _legacy/                        # Retired or superseded documents
│       └── [Old versions preserved for history]
│
└── [project code would go here]        # For projects that include code
```

---

## Directory Purposes

### **Root Level**

#### `README.md`
- **Purpose:** Repository front door
- **Audience:** First-time visitors, potential adopters
- **Content:** What the system is, why it exists, how to get started
- **Authority:** Informative, not governance
- **Enhanced in:** Epic E4.2

#### `LICENSE`
- **Purpose:** Legal terms for system usage
- **Status:** To be added in E4.4
- **Expected:** MIT or similar permissive license

---

### **`governance/` — Governance Root**

All governance files live under `governance/` to keep them portable and separately referenceable.

#### `governance/README.md`
- **Purpose:** Governance folder overview and navigation hub
- **Content:** Links to governance documents, authority hierarchy, adoption instructions
- **Audience:** Users who have entered the governance folder

#### `governance/PROJECT-SYSTEM-GUIDELINES.md`
- **Authority Level:** 1 (Highest)
- **Purpose:** Defines system structure, governance, core concepts
- **Immutability:** High (changes require governance process)
- **Version:** Tracked and referenced in all Specs
- **Key Content:** Phase-Milestone-Epic model, file conventions, repository structure

#### `governance/AI-OPERATING-GUIDELINES.md`
- **Authority Level:** 2
- **Purpose:** Execution procedures for AI agents
- **Key Content:** Canonical happy path, agent responsibilities, HQ authority
- **Relationship:** Implements PROJECT-SYSTEM-GUIDELINES.md procedures

#### `governance/EPIC-EXECUTION-CHAT-STARTER.md`
- **Authority Level:** 3
- **Purpose:** Canonical format reference for Epic Execution Chat Starters
- **Audience:** HQ Chat when generating chat starters

---

### **`docs/` — Project History Root**

Project history and execution artifacts live under `docs/`.

#### `docs/README.md`
- **Purpose:** Documentation index
- **Content:** Links to project execution artifacts
- **Audience:** Users navigating project history

---

### **`docs/phases/` — Project Execution Hierarchy**

#### **Structure:**
```
phases/
├── P0__phase__project-formalization.md
├── P0-M0.1__milestone__repository-bootstrap.md
├── P0-M0.1-E0.1.1__epic__formalize-system-repository.md
├── P0-M0.1-E0.1.1__completion__retired.md
│
└── P1__System_Foundation_and_Adoption/
    ├── P1__phase.md
    ├── P1-M1__milestone.md
    ├── P1-M1-E1.1__spec__*.md
    ├── P1-M1-E1.1__completion__*.md
    └── [... more Milestones and Epics ...]
```

#### **File Types in phases/:**

**Phase Specs** (`P1__phase.md`)
- Define high-level project phase
- Contain Milestones
- Example: "P1 — System Foundation & Adoption"

**Milestone Specs** (`P1-M1__milestone.md`)
- Define deliverable increment
- Contain Epics
- Example: "M1 — Genesis & Integration Baseline"

**Epic Specs** (`P1-M1-E1.1__spec__*.md`)
- Define atomic unit of work
- Include goals, deliverables, DoD, acceptance criteria

**Epic Completions** (`P1-M1-E1.1__completion__*.md`)
- Document Epic execution results
- Verify Definition of Done
- Record metrics and deviations

#### **Nested Folders:**
- Some Phases use folder structure: `P1__System_Foundation_and_Adoption/`
- Keeps related Milestones and Epics organized
- Optional (P0 uses flat structure, P1 uses folder)

---

### **`governance/templates/` — Reusable Templates**

Created in Epic E4.1, migrated to `/governance` in E6.2.

#### **Template Files:**
- `phase-spec.md` — Template for creating new Phase specs
- `milestone-spec.md` — Template for creating new Milestone specs
- `epic-spec.md` — Template for creating new Epic specs
- `epic-execution-chat-starter.md` — Template for AI execution instructions
- `epic-completion-report.md` — Template for completion documentation
- `epic-review-seal.md` — Template for human review documentation
- `governance-source.md` — Template for governance adoption declaration
- `README.md` — Template usage guide

#### **Usage:**
1. Copy template to `docs/phases/`
2. Fill in front-matter and sections
3. Use as authoritative specification
4. Templates are **blueprints**, not live documents

---

### **`governance/diagrams/` — Visual Documentation**

Created in Epic E4.2, migrated to `/governance` in E6.2.

#### **Diagram Files:**
- `epic-lifecycle-flow.md` — Visual flowchart of Epic execution
- `authority-hierarchy.md` — Document precedence diagram
- `repository-structure.md` — This file

#### **Format:**
- Mermaid syntax (GitHub-native rendering)
- Markdown files with embedded Mermaid code blocks
- Include explanatory text alongside diagrams

---

### **`governance/systems/` — System Operation Guides**

Procedural guides for operating the system. Migrated to `/governance` in E6.2.

#### **Key Files:**
- `epic-execution-chat-starter.md` — How to use Chat Starters
- `governance-propagation.md` — How governance flows
- `hq-chat.md` — HQ (human) responsibilities
- `PROJECT-TRACKER-INTEGRATION-SYSTEM.md` — Project tracking procedures
- `start-a-project.md` — How to initialize new projects

#### **Purpose:**
- Supplement governance with practical how-tos
- Authority Level 4 (operational guidance)
- Not templates (these are guides, not blueprints)

---

### **`governance/guides/` — Onboarding Guides**

Informational guides for humans adopting the system.

#### **Key Files:**
- `QUICK-START.md` — 30-minute onboarding walkthrough
- `FAQ.md` — Frequently asked questions

#### **Purpose:**
- Help new adopters get started quickly
- No authority — informational only

---

### **`docs/roadmap/` — Project Planning**

High-level roadmap and future planning.

#### **Content:**
- `overview.md` — Project roadmap
- Future Phases (planned but not started)
- Strategic direction

---

### **`docs/context/` — Project Context**

Project-wide context and tracking.

#### **Content:**
- `project-tracker.md` — Current status, active work, blockers
- Living document (updated frequently)

---

### **`docs/decisions/` — Decision Records**

Architectural Decision Records (ADRs).

#### **Status:** Directory exists but not yet used
#### **Future Use:**
- Record significant technical decisions
- Format: ADR template (to be defined)
- Immutable once accepted

---

### **`docs/admin/` — Administrative Records**

Administrative corrections, notices, and records.

#### **Examples:**
- Governance amendments
- Retrospective corrections
- Administrative clarifications

---

### **`docs/_legacy/` — Retired Documents**

Superseded or retired documents preserved for history.

#### **Purpose:**
- Preserve context for future reference
- Show evolution of system
- Don't delete; retire here instead

---

## File Naming Conventions

### **Phase Files**
```
P<number>__phase__<slug>.md
P<number>__<Phase_Name>/
```
- Example: `P1__phase.md`
- Example: `P1__System_Foundation_and_Adoption/`

### **Milestone Files**
```
P<number>-M<number>__milestone__<slug>.md
P<number>-M<number>__milestone.md
```
- Example: `P1-M4__milestone.md`

### **Epic Files**
```
P<number>-M<number>-E<number>.<number>__<type>__<slug>.md
```
- Types: `spec`, `completion`, `delivery-notice`, `review-seal`
- Example: `P1-M4-E4.2__spec__quick-start-guide-and-visual-documentation.md`
- Example: `P1-M4-E4.2__completion__quick-start-guide-and-visual-documentation.md`

### **Template Files**
```
<resource-type>-<artifact-type>.md
```
- Example: `epic-spec.md`
- Example: `epic-execution-chat-starter.md`

### **System Files**
```
<kebab-case-name>.md
```
- Example: `start-a-project.md`
- Example: `governance-propagation.md`

---

## Branch Strategy

Branches mirror the Phase–Milestone–Epic hierarchy:

### **Branch Naming**
```
phase/P<number>
milestone/M<number>
epic/E<number>.<number>
```

### **Branch Hierarchy**
```
master (production)
  └── phase/P1 (long-lived)
      └── milestone/M4 (long-lived)
          └── epic/E4.2 (short-lived)
```

### **Merge Flow**
```
epic/E4.2 → milestone/M4 → phase/P1 → master
```

### **Key Rules**
1. Epic branches created FROM Milestone branches (not master)
2. Milestone branches created FROM Phase branches (not master)
3. Phase branches created FROM master
4. Merges flow upward through hierarchy

---

## How to Navigate This Structure

### **If you want to...**

#### **Understand the system quickly**
1. Read `README.md`
2. Read `governance/guides/QUICK-START.md`
3. Skim diagrams in `governance/diagrams/`

#### **Learn the governance rules**
1. Read `governance/PROJECT-SYSTEM-GUIDELINES.md`
2. Read `governance/AI-OPERATING-GUIDELINES.md`

#### **Start a new project**
1. Read `governance/systems/start-a-project.md`
2. Copy templates from `governance/templates/`
3. Follow `governance/guides/QUICK-START.md`

#### **See an example Epic**
1. Browse `docs/phases/P1__System_Foundation_and_Adoption/`
2. Read any `__spec__` file
3. Read corresponding `__completion__` file

#### **Understand a specific concept**
1. Check `governance/diagrams/` for visual explanation
2. Reference `governance/PROJECT-SYSTEM-GUIDELINES.md` for authoritative definition
3. Check `governance/systems/` for practical guides

---

## What Goes Where?

| Content Type | Location | Example |
|--------------|----------|---------|
| Governance rules | `governance/` root | `PROJECT-SYSTEM-GUIDELINES.md` |
| Quick Start | `governance/guides/` | `QUICK-START.md` |
| Phases | `docs/phases/` | `P1__phase.md` |
| Milestones | `docs/phases/` | `P1-M4__milestone.md` |
| Epics | `docs/phases/` | `P1-M4-E4.2__spec__*.md` |
| Templates | `governance/templates/` | `epic-spec.md` |
| Diagrams | `governance/diagrams/` | `epic-lifecycle-flow.md` |
| System Guides | `governance/systems/` | `hq-chat.md` |
| Onboarding | `governance/guides/` | `QUICK-START.md` |
| Roadmap | `docs/roadmap/` | `overview.md` |
| Context | `docs/context/` | `project-tracker.md` |
| Decisions | `docs/decisions/` | (future ADRs) |
| Admin Records | `docs/admin/` | Amendments, corrections |
| Retired Docs | `docs/_legacy/` | Superseded content |

---

## Evolution of This Structure

This structure was formalized through:
- **P0 (Formalization):** Bootstrapped repository, established core governance
- **P1-M1 (Genesis):** Integrated project tracker, established baseline
- **P1-M2 (Validation):** Added review processes, closure validation
- **P1-M3 (Governance):** Propagated governance, established authority
- **P1-M4 (Adoption):** Added templates (E4.1), documentation (E4.2)

Future Milestones may add:
- Example projects
- Troubleshooting guides
- Team/org guides

The structure grows **intentionally**, not ad-hoc. New directories are added through Epics, not improvised.

---

## References

- [PROJECT-SYSTEM-GUIDELINES.md](../PROJECT-SYSTEM-GUIDELINES.md) — Authoritative structure definition
- [Quick Start Guide](../QUICK-START.md) — Practical walkthrough
- [Templates README](../templates/README.md) — Template usage guide
