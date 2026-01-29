# AI Project System

**A formal, governed documentation system for AI-assisted project execution.**

Turn AI coding assistants into reliable project executors through structured specs, clear boundaries, and explicit human review.

---

## The Problem

AI coding assistants are powerful but chaotic:

❌ **Context is lost** across conversations  
❌ **Scope creeps** without clear boundaries  
❌ **Quality varies** without standards  
❌ **Handoffs fail** between humans and AI  
❌ **Decisions disappear** into chat history  

Traditional project management assumes human-to-human communication. AI needs a different approach.

---

## The Solution

The AI Project System provides **structure without rigidity**:

✅ **Structured specs** preserve context across sessions (Phase → Milestone → Epic)  
✅ **Authoritative documentation** replaces ephemeral chat history  
✅ **Clear execution boundaries** define when AI starts, delivers, and stops  
✅ **Explicit human review** ensures quality and alignment  
✅ **Version-controlled decisions** document intent and rationale  

You get **AI speed with human governance**.

---

## What This Is

This repository contains the **canonical AI Project System** used to structure, document, and execute software projects with AI assistance.

It defines:
- Authoritative governance documents
- A Phase–Milestone–Epic execution model
- A documentation-first workflow
- Explicit context management for AI agents

This is **not an application**.  
It is a **system for managing projects**.

---

## Who This Is For

This system is designed for:
- **Engineers using AI tools** (ChatGPT, GitHub Copilot, Cursor, Claude, etc.)
- **Projects where context, scope, and delivery matter** (not throwaway prototypes)
- **People who want repeatability, not improvisation** (structure over chaos)

**Prerequisites:**
- Git and GitHub (basic familiarity)
- Markdown editing
- AI chat tool access
- Willingness to trade upfront planning for execution clarity

**Not for:**
- Pure exploratory coding
- Single-file scripts
- Projects without AI assistance

---

## Key Features

### 📋 **Phase–Milestone–Epic Model**
Hierarchical structure that breaks work into manageable, deliverable units:
- **Phases:** Major segments (e.g., "Foundation", "Feature Development")
- **Milestones:** Cohesive increments (collection of related Epics)
- **Epics:** Atomic deliverable work (complete, reviewable, mergeable)

### 🤖 **AI-First Execution**
Purpose-built for AI coding assistants:
- Epic Execution Chat Starters provide complete context
- AI agents execute autonomously within guardrails
- Documentation preserves context across sessions

### 👤 **Human Governance**
Clear separation of responsibilities:
- **Humans (HQ):** Define goals, review work, make accept/reject decisions
- **AI (Coding Agents):** Execute work, produce deliverables, document completion
- Explicit authorization required for merging

### 📄 **Documentation as Authority**
Version-controlled, authoritative specs:
- Chat is ephemeral, Markdown is truth
- Governance documents define rules and procedures
- Specs define goals, deliverables, and success criteria

### 🔄 **Canonical Happy Path**
Defined Epic lifecycle prevents chaos:
1. HQ creates Epic Spec
2. AI executes Epic
3. AI produces Delivery Notice and stops
4. Human reviews deliverables
5. HQ accepts/rejects/requests changes
6. HQ authorizes merge (if accepted)
7. AI merges and stops

### 🎯 **Definition of Done**
Every Epic has explicit completion criteria:
- Deliverables checklist
- Acceptance criteria for human review
- Success metrics

---

## Quick Start

**New to the system?** Get started in 30 minutes:

👉 **[Read the Quick Start Guide](docs/QUICK-START.md)**

The guide walks you through:
1. Initializing repository structure
2. Creating your first Phase, Milestone, and Epic
3. Executing an Epic with AI assistance
4. Reviewing and closing your first Epic

**Time:** 30 minutes  
**Outcome:** Complete understanding through practice

---

## Visual Documentation

**Understand the system visually:**

- 🔄 **[Epic Lifecycle Flow](docs/diagrams/epic-lifecycle-flow.md)** — How Epics move from idea to closure
- 📊 **[Authority Hierarchy](docs/diagrams/authority-hierarchy.md)** — Which documents have precedence
- 📁 **[Repository Structure](docs/diagrams/repository-structure.md)** — Where everything lives

---

## Documentation Map

### **New Users**
- 🚀 [Quick Start Guide](docs/QUICK-START.md) — 30-minute walkthrough
- 📖 [PROJECT-SYSTEM-GUIDELINES.md](docs/PROJECT-SYSTEM-GUIDELINES.md) — System structure and governance
- 🤖 [AI-OPERATING-GUIDELINES.md](docs/AI-OPERATING-GUIDELINES.md) — Execution procedures
- 🎨 [Visual Diagrams](docs/diagrams/) — Epic lifecycle, authority, structure

### **Creating Projects**
- 🏗️ [How to Start a Project](docs/systems/start-a-project.md) — Initialize new projects
- 📝 [Templates](docs/templates/) — Phase, Milestone, Epic templates
- 📋 [Template Usage Guide](docs/templates/README.md) — How to use templates

### **Executing Work**
- ⚙️ [Epic Execution Chat Starter System](docs/systems/epic-execution-chat-starter.md) — How to run Epics
- 👔 [HQ Chat Guide](docs/systems/hq-chat.md) — Human responsibilities

### **Examples**
- 📚 [Phase P1 Examples](docs/phases/P1__System_Foundation_and_Adoption/) — Real Epic specs and completions
- 🔍 See how this system was built using itself

### **Reference**
- 🏛️ [Governance Propagation](docs/systems/governance-propagation.md) — How governance flows
- 🗺️ [Project Tracker Integration](docs/systems/PROJECT-TRACKER-INTEGRATION-SYSTEM.md) — Tracker usage

---

## How It Works (5-Minute Overview)

### **1. Plan (Human)**
Create an Epic Spec defining:
- Problem statement
- Goals and deliverables
- Definition of Done
- Acceptance criteria

### **2. Execute (AI)**
Launch AI Coding Agent with Epic Execution Chat Starter:
- Agent creates branch
- Agent builds deliverables
- Agent self-validates against DoD
- Agent produces Delivery Notice and **stops**

### **3. Review (Human)**
Evaluate deliverables:
- Does it meet acceptance criteria?
- Does it solve the stated problem?
- Is quality acceptable?

### **4. Close (Human + AI)**
Make decision:
- **Accept:** HQ authorizes merge → AI merges → Epic closed
- **Reject:** Document rationale → create new Epic or abandon
- **Request Changes:** Define iteration → AI updates

---

## System vs Traditional PM

| Traditional PM | AI Project System |
|----------------|-------------------|
| Jira tickets | Epic Specs (Markdown) |
| Standup meetings | Epic Delivery Notices |
| Verbal context | Documentation (version-controlled) |
| Manager assigns work | Human creates spec, AI executes |
| Code reviews | Human reviews + Epic Review Seals |
| "Done when merged" | "Done when DoD verified + accepted + merged" |
| Continuous communication | Async, documented handoffs |
| Human assumes context | AI reads authoritative docs |

**Key difference:** Traditional PM assumes humans retain context. AI Project System assumes context must be **explicitly documented**.

---

## Getting Started (Recommended Path)

**Option 1: Jump Right In (30 minutes)**
- 👉 **[Quick Start Guide](docs/QUICK-START.md)** — Learn by doing

**Option 2: Understand First, Then Practice**
1. **Read governance**
   - [PROJECT-SYSTEM-GUIDELINES.md](docs/PROJECT-SYSTEM-GUIDELINES.md) — System structure (15 min)
   - [AI-OPERATING-GUIDELINES.md](docs/AI-OPERATING-GUIDELINES.md) — Execution procedures (10 min)
2. **See visual overview**
   - [Epic Lifecycle Flow](docs/diagrams/epic-lifecycle-flow.md) — How Epics work (5 min)
   - [Authority Hierarchy](docs/diagrams/authority-hierarchy.md) — Document precedence (5 min)
3. **Start a project**
   - [How to Start a Project](docs/systems/start-a-project.md) — Step-by-step initialization

**You don't need to read everything to begin.**  
The system is designed to be learned incrementally.

---

## Current Project Status

This repository is **dogfooding its own system** (the AI Project System was built using the AI Project System).

**Current State:**
- **Phase:** P1 — System Foundation & Adoption
- **Milestone:** M4 — Adoption Readiness & Practical Enablement (active)
- **Recent Completions:**
  - ✅ M1 — Genesis & Integration Baseline
  - ✅ M2 — Validation & Quality Gates
  - ✅ M3 — Governance Propagation & Authority Declaration
  - ✅ E4.1 — Templates & Scaffolding
  - ⏳ E4.2 — Quick Start Guide & Visual Documentation (in progress)

**Governance:** Stable and usable (v1.3.0)  
**Future Work:** Intentionally paced, driven by real usage needs

---

## How Progress Is Tracked

Progress is reflected in **three complementary ways**:

1. **Documentation (authoritative)**
   - Phase, Milestone, and Epic state lives in `docs/`
   - Completion reports are explicit and versioned

2. **Git history**
   - Branch hierarchy reflects execution flow
   - Commits and PRs correspond to closed Epics

3. **Project Tracker (assistive)**
   - GitHub Projects is used for planning and visibility
   - Tracker state does **not** override documentation

If there is ever a conflict, **documentation wins**.

---

## Where to Look for Truth

**Authority Hierarchy (highest to lowest):**

1. **[PROJECT-SYSTEM-GUIDELINES.md](docs/PROJECT-SYSTEM-GUIDELINES.md)** — System structure, file conventions, core concepts
2. **[AI-OPERATING-GUIDELINES.md](docs/AI-OPERATING-GUIDELINES.md)** — Execution procedures, agent responsibilities
3. **Epic Execution Chat Starter** — Epic-specific instructions
4. **Epic Spec** — Problem statement, goals, deliverables
5. **Execution Decisions** — Real-time implementation choices
6. **System References** — How-to guides, examples
7. **Chat Messages** — Ephemeral communication (lowest authority)

**Golden Rule:** Documentation is authoritative. Chat is ephemeral. If there's conflict, **higher-level docs win**.

See [Authority Hierarchy Diagram](docs/diagrams/authority-hierarchy.md) for visual explanation.

---

## Status of the System

**Current State:**
- ✅ **Validated** through real execution (20+ Epics closed)
- ✅ **In active use** for multiple projects
- ✅ **Evolving deliberately**, not continuously
- ✅ **Governance stable** (v1.3.0, effective 2026-01-17)
- ✅ **Templates available** (E4.1, effective 2026-01-28)
- 🏗️ **Documentation expanding** (E4.2, in progress)

**Intentional Limitations:**
- No CLI (not needed yet)
- No web UI (not needed yet)
- No automation tooling (manual process validates concepts)
- No team/org features (single-user focus)

New capabilities will be added **when real usage demands them**, not speculatively.

---

## Contributing

This is a personal project system currently optimized for individual use.

**Want to contribute?**
- File issues for bugs or clarifications
- Share your usage experiences
- Suggest improvements based on real usage (not theory)

**Not accepting:**
- Speculative features
- Team/org features (out of scope for now)
- Tooling/automation (intentionally deferred)

---

## Roadmap

See [docs/roadmap/overview.md](docs/roadmap/overview.md) for planned future work.

**Upcoming:**
- E4.3 — Example Projects & Case Studies
- E4.4 — FAQ & Troubleshooting Guide
- Future phases TBD based on adoption needs

---

## License

No license currently specified. This is a personal project system.

Future licensing decisions will be documented through the governance process.

---

## Questions?

- 📖 **Read:** [Quick Start Guide](docs/QUICK-START.md)
- 🎨 **Visualize:** [Diagrams](docs/diagrams/)
- 🔍 **Explore:** [Example Epics](docs/phases/P1__System_Foundation_and_Adoption/)
- ❓ **Ask:** File an issue in this repository

**The best way to understand the system is to use it.** Start with the [Quick Start Guide](docs/QUICK-START.md).
