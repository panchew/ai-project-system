# AI Project System

**A formal, governed documentation system for AI-assisted project execution.**

Turn AI coding assistants into reliable project executors through structured specs, clear boundaries, and explicit human review.

---

## 🎉 Both Phases Complete — Production Ready

**The AI Project System is fully built using its own governance.** Both Phase P1 (foundation) and Phase P2 (multi-project infrastructure) are complete and production-ready.

### Phase P1 — System Foundation (Complete)
✅ **5 Milestones** (M1-M5), **12 Epics** — Closed 2026-02-23 — [#21](https://github.com/panchew/ai-project-system/pull/21)

### Phase P2 — Adoption Architecture (Complete)
| Milestone | Epics | Status | Key Deliverables |
|-----------|-------|--------|------------------|
| **M6** — Governance Separation | E6.1–E6.7 | ✅ Complete | `/governance` folder, `.ai-project.yml` spec, submodule setup |
| **M7** — CLI Initialization Tool | E7.1–E7.4 | ✅ Complete | `ai-project init` command, hierarchical docs scaffolding |
| **M8** — HQ Chat Agent | E8.1–E8.4 | ✅ Complete | `hq.agent.md`, project onboarding, governance upgrade workflow |
| **M9** — Configuration & Override System | E9.1–E9.4 | ✅ Complete | Override spec, precedence rules, HQ agent integration |
| **M10** — Adoption Validation & Documentation | E10.1–E10.4 | ✅ Complete | Adoption guide, FAQ, onboarded projects, P2 closure |

👉 **[Start using the system now](governance/guides/QUICK-START.md)**

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
- **Engineers using AI tools** (ChatGPT, Claude, Cursor, etc.)
- **Projects where context, scope, and delivery matter** (not throwaway prototypes)
- **People who want repeatability, not improvisation** (structure over chaos)

**Prerequisites:**
- Git (basic familiarity)
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
- Chat Starters provide complete context for each level (Phase, Milestone, Epic)
- Governance Agent self-configures its mode from the Chat Starter
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
1. Milestone Chat creates Epic Spec and Execution Chat Starter
2. AI executes the Epic
3. AI produces Delivery Notice and stops
4. Human reviews deliverables
5. Parent chat (Milestone/Phase/HQ) accepts/rejects/requests changes
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

👉 **[Read the Quick Start Guide](governance/guides/QUICK-START.md)**

The guide walks you through:
1. Initializing repository structure
2. Starting HQ Mode to create a Phase
3. Launching Phase/Milestone/Epic modes via Chat Starters
4. Reviewing and closing your first Epic

**Time:** 30 minutes  
**Outcome:** Complete understanding through practice

---

## Visual Documentation

**Understand the system visually:**

- 🔄 **[Epic Lifecycle Flow](governance/diagrams/epic-lifecycle-flow.md)** — How Epics move from idea to closure
- 📊 **[Authority Hierarchy](governance/diagrams/authority-hierarchy.md)** — Which documents have precedence
- 📁 **[Repository Structure](governance/diagrams/repository-structure.md)** — Where everything lives

---

## Documentation Map

### **New Users**
- 🚀 [Quick Start Guide](governance/guides/QUICK-START.md) — 30-minute walkthrough
- 📖 [PROJECT-SYSTEM-GUIDELINES.md](governance/PROJECT-SYSTEM-GUIDELINES.md) — System structure and governance
- 🤖 [AI-OPERATING-GUIDELINES.md](governance/AI-OPERATING-GUIDELINES.md) — Execution procedures
- 🎨 [Visual Diagrams](governance/diagrams/) — Epic lifecycle, authority, structure

### **Adopting the System**
- 🏗️ [How to Start a Project](governance/systems/start-a-project.md) — Initialize new projects
- 📖 [Adoption Guide](governance/guides/ADOPTION-GUIDE.md) — Step-by-step from zero to HQ Chat live
- ❓ [Adoption FAQ](governance/guides/ADOPTION-FAQ.md) — Troubleshooting common issues
- 🔄 [Governance Sync Guide](governance/guides/GOVERNANCE-SYNC-GUIDE.md) — Updating governance across projects

### **Creating Projects**
- 📝 [Templates](governance/templates/) — Phase, Milestone, Epic templates
- 📋 [Template Usage Guide](governance/templates/README.md) — How to use templates
- ⚙️ [Override Boundaries](governance/override-boundaries.md) — What can be customized vs. immutable

### **Executing Work**
- ⚙️ [Epic Execution Chat Starter System](governance/systems/epic-execution-chat-starter.md) — How to run Epics
- 👔 [HQ Chat Guide](governance/systems/hq-chat.md) — HQ mode responsibilities

### **Examples**
- 📚 [Phase P1 Examples](docs/phases/P1__System_Foundation_and_Adoption/) — Real Epic specs and completions
- 📚 [Phase P2 Examples](docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/) — Multi-project adoption artifacts
- 🔍 See how this system was built using itself

### **Reference**
- 🏛️ [Governance Propagation](governance/systems/governance-propagation.md) — How governance flows
- 🗺️ [Project Tracker Integration](governance/systems/PROJECT-TRACKER-INTEGRATION-SYSTEM.md) — Tracker usage

---

## How It Works (5-Minute Overview)

### **1. Plan (Human + Milestone Chat)**
Milestone Chat creates an Epic Spec and Epic Execution Chat Starter defining:
- Problem statement
- Goals and deliverables
- Definition of Done
- Acceptance criteria

### **2. Execute (Epic Mode)**
Epic mode receives the Chat Starter and executes:
- Creates branch
- Builds deliverables
- Self-validates against DoD
- Produces Delivery Notice and **stops**

### **3. Review (Human)**
Evaluate deliverables:
- Does it meet acceptance criteria?
- Does it solve the stated problem?
- Is quality acceptable?

### **4. Close (Human + AI)**
Make decision:
- **Accept:** HQ authorizes merge → Epic mode merges → Epic closed
- **Reject:** Document rationale → create new Epic or abandon
- **Request Changes:** Define iteration → Epic mode updates

---

## System vs Traditional PM

| Traditional Project Management | AI Project System |
|-------------------------------|-------------------|
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

## Value Proposition

**What you get:**
- ✅ **Structure** — Clear boundaries for AI execution (no scope creep)
- ✅ **Repeatability** — Same process for every Epic, predictable outcomes
- ✅ **Context preservation** — Documentation survives session boundaries
- ✅ **Quality control** — Explicit review and acceptance gates
- ✅ **AI speed** — Autonomous execution once spec is clear

**What you give up:**
- ❌ **Improvisation** — Must plan before executing
- ❌ **Verbal context** — Everything must be written down
- ❌ **Continuous iteration** — Changes require spec updates

**Who should use this:**
- Engineers building production systems with AI assistance
- Projects where context loss has caused rework
- Teams wanting predictable AI execution
- People who value structure over chaos

**Who should NOT use this:**
- Pure exploratory coding (no clear deliverables)
- Throwaway prototypes (overhead not worth it)
- Single-file scripts (too much process)
- Projects without AI assistance (system assumes AI execution)

---

## Getting Started (Recommended Path)

**Option 1: Jump Right In (30 minutes)**
- 👉 **[Quick Start Guide](governance/guides/QUICK-START.md)** — Learn by doing

**Option 2: Understand First, Then Practice**
1. **Read governance**
   - [PROJECT-SYSTEM-GUIDELINES.md](governance/PROJECT-SYSTEM-GUIDELINES.md) — System structure (15 min)
   - [AI-OPERATING-GUIDELINES.md](governance/AI-OPERATING-GUIDELINES.md) — Execution procedures (10 min)
2. **See visual overview**
   - [Epic Lifecycle Flow](governance/diagrams/epic-lifecycle-flow.md) — How Epics work (5 min)
   - [Authority Hierarchy](governance/diagrams/authority-hierarchy.md) — Document precedence (5 min)
3. **Start a project**
   - [How to Start a Project](governance/systems/start-a-project.md) — Step-by-step initialization

**You don't need to read everything to begin.**  
The system is designed to be learned incrementally.

---

## Current Project Status

This repository **dogfooded its own system** — the AI Project System was built using the AI Project System.

### Phase P1 — Complete (closed 2026-02-23)
✅ **5 Milestones:** M1 (Genesis), M2 (Execution Ergonomics), M3 (Governance Distribution), M4 (Adoption Readiness), M5 (System Refinement)
✅ **12 Epics delivered and merged**
✅ **Production-ready baseline**

### Phase P2 — Complete (closed 2026-05-21)
✅ **23 Epics** across 5 milestones — Closed via [#51](https://github.com/panchew/ai-project-system/pull/51)
✅ **M6** — Governance Separation & `.ai-project.yml` (7 Epics)
✅ **M7** — CLI Initialization Tool (4 Epics)
✅ **M8** — HQ Chat Agent (4 Epics)
✅ **M9** — Configuration & Override System (4 Epics)
✅ **M10** — Adoption Validation & Documentation (4 Epics)

### Totals (P1 + P2)
✅ **35 Epics** delivered across **10 milestones** over **2 phases**

### Governance
- PROJECT-SYSTEM-GUIDELINES.md v2.0.0 (effective 2026-04-20)
- AI-OPERATING-GUIDELINES.md v2.0.0 (effective 2026-04-20)

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

1. **[PROJECT-SYSTEM-GUIDELINES.md](governance/PROJECT-SYSTEM-GUIDELINES.md)** — System structure, file conventions, core concepts
2. **[AI-OPERATING-GUIDELINES.md](governance/AI-OPERATING-GUIDELINES.md)** — Execution procedures, agent responsibilities
3. **Epic Execution Chat Starter** — Epic-specific instructions
4. **Epic Spec** — Problem statement, goals, deliverables
5. **Execution Decisions** — Real-time implementation choices
6. **System References** — How-to guides, examples
7. **Chat Messages** — Ephemeral communication (lowest authority)

**Golden Rule:** Documentation is authoritative. Chat is ephemeral. If there's conflict, **higher-level docs win**.

See [Authority Hierarchy Diagram](governance/diagrams/authority-hierarchy.md) for visual explanation.

---

## Status of the System

**Current State:**
- ✅ **Phase P1 Complete** — System Foundation & Adoption (5 milestones, 12 Epics)
- ✅ **Phase P2 Complete** — Adoption Architecture & Multi-Project Support (5 milestones, 23 Epics)
- ✅ **35 total Epics** delivered across 10 milestones, 2 phases
- ✅ **Production-ready** — Stable baseline for adoption in other projects
- ✅ **Battle-tested** — Built using itself (dogfooding validated)
- ✅ **Governance stable** — v2.0.0 (effective 2026-04-20)
- ✅ **Complete documentation** — Quick-start, templates, examples, diagrams, FAQ
- ✅ **CLI tool** — `ai-project init` for one-command project setup
- ✅ **Governance Agent** — Single unified agent with HQ/Phase/Milestone/Epic modes
- ✅ **Override system** — Customizable branching, naming, and merge conventions
- ✅ **Adoption guide** — Step-by-step path from zero to HQ Chat live
- ✅ **Licensed for adoption** — MIT + CC BY-SA 4.0 dual license

**What's Next (Future Phases):**
- **P3** — Execution Model Maturity (Phase/Milestone chat agents, full handoff chain, automated PR merge)
- **Future** — Team collaboration, external integrations, observability, automation tooling

**Intentional Characteristics:**
- Evolving deliberately based on real usage, not speculatively
- No web UI (not needed yet)
- No automation tooling beyond CLI (intentionally deferred)
- Single-user focus (team/org features deferred to future phases)

---

## Licensing

This repository uses **dual licensing**:

- **Code & Templates:** [MIT License](LICENSE)  
  Freely use, modify, and distribute code, templates, and configuration files.

- **Documentation:** [Creative Commons BY-SA 4.0](docs/LICENSE)  
  Documentation must be attributed and shared under the same license.

**Why dual licensing?**
- **MIT** allows unrestricted reuse of templates and code (maximum adoption)
- **CC BY-SA 4.0** ensures documentation improvements flow back to the community

See [LICENSE](LICENSE) and [docs/LICENSE](docs/LICENSE) for full license texts.

---

## Contributing

**Contributions are welcome!** 

This system is designed to improve through real usage experience. We especially value:
- Bug reports (governance conflicts, unclear procedures)
- Documentation improvements (clarifications, examples)
- Real-world usage feedback ("I tried X and encountered Y")

**Before contributing:**
- Read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
- Open an issue to discuss significant changes
- Follow existing documentation style and conventions

**Not accepting (without discussion):**
- Speculative features (no real usage motivation)
- Major redesigns (prove concepts first)
- Tooling/automation (intentionally deferred)

👉 **[Read the full contributing guide](CONTRIBUTING.md)**

---

## Questions?

- 📖 **Start here:** [Quick Start Guide](governance/guides/QUICK-START.md)
- ❓ **FAQ:** [Frequently Asked Questions](governance/guides/FAQ.md)
- 🎨 **Visualize:** [Diagrams](governance/diagrams/)
- 🔍 **Examples:** [Phase P1](docs/phases/P1__System_Foundation_and_Adoption/) | [Phase P2](docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/)
- 📖 **Adoption Guide:** [Step-by-step walkthrough](governance/guides/ADOPTION-GUIDE.md)
- 💬 **Ask:** [Open an issue](https://github.com/panchew/ai-project-system/issues)
