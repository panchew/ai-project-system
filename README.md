# AI Project System

**A formal, governed documentation system for AI-assisted project execution.**

Turn AI coding assistants into reliable project executors through structured specs, clear boundaries, and explicit human review.

---

## 🎉 All Phases Complete — Autonomous Cluster Ready

**The AI Project System was built using its own governance.** All three planned phases (P1, P2, P3) are complete and consolidated to `master`.

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

### Phase P3 — Agentic Execution Model Maturity (Complete)
| Milestone | Epics | Status | Key Deliverables |
|-----------|-------|--------|------------------|
| **M11** — File-Driven Bus & State Triggers | 4 | ✅ Complete | `.ai-project/queue/`, Python orchestrator, queue schemas |
| **M12** — Containerized Sandbox & Loop Verification | 4 | ✅ Complete | `Dockerfile.sandbox`, 3-retry recursion engine, mock harness |
| **M13** — Orchestrator CLI Daemon | 4 | ✅ Complete | `ai-project-daemon`, auto-merge hooks, lifecycle tests |

👉 **[Start using the system — manual or agentic](governance/guides/QUICK-START.md)**

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

Each level is planned by its parent and feeds into the next:

```
HQ Chat ──creates──→ Phase specs + Phase Execution Chat Starter
                        │
                        ▼
                   Phase Chat ──creates──→ Milestone specs + Milestone Execution Chat Starter
                                               │
                                               ▼
                                          Milestone Chat ──creates──→ Epic specs + Epic Execution Chat Starter
                                                                          │
                                                                          ▼
                                                                     Epic mode ──executes──→ Code, PRs, deliverables
```

### 🤖 **AI-First Execution** (Two Modes)
Purpose-built for AI coding assistants:

**Manual Mode** (no infrastructure required):
- Chat Starters provide complete context for each level (Phase, Milestone, Epic)
- You copy-paste starters between sessions — handoffs are explicit and documented

**Agentic Mode** (Docker + daemon):
- File-driven queue (`.ai-project/queue/`) replaces copy-paste handoffs
- `ai-project-orchestrator` detects triggers, dispatches work, runs Dev-QA loops
- `ai-project-daemon` monitors the queue 24/7
- `Dockerfile.sandbox` provides isolated, reproducible runtime
- Auto-merge promotes branches automatically via `ai-project-git-merge`

Both modes use the same specs, same artifacts, same governance. Start manual, graduate to agentic.

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

### **Executing Work (Manual)**
- ⚙️ [Epic Execution Chat Starter System](governance/systems/epic-execution-chat-starter.md) — How to run Epics
- 👔 [HQ Chat Guide](governance/systems/hq-chat.md) — HQ mode responsibilities

### **Executing Work (Agentic/Autonomous)**
- 🤖 [`bin/ai-project-orchestrator`](bin/ai-project-orchestrator) — Core orchestration engine
- 🤖 [`bin/ai-project-daemon`](bin/ai-project-daemon) — Background queue monitor
- 🤖 [`Dockerfile.sandbox`](Dockerfile.sandbox) — Sandbox container runtime
- 🤖 [`bin/verify-loop.sh`](bin/verify-loop.sh) — Dev-QA loop verification (5 scenarios)
- 🤖 [`bin/ai-project-git-merge`](bin/ai-project-git-merge) — Auto-merge utility
- 📋 [PROJECT-SYSTEM-GUIDELINES.md §18](governance/PROJECT-SYSTEM-GUIDELINES.md) — Unattended cluster rules

### **Team Collaboration**
- 👥 [Team Onboarding Guide](docs/team-collaboration/team-onboarding-guide.md) — All roles, authority matrix, escalation path, your first week
- 👤 [CFO Quick Start](docs/team-collaboration/cfo-quick-start.md) — Strategic authority, typical week, production gate (5 min read)
- 🛠️ [Contributor Guide](docs/team-collaboration/contributor-guide.md) — Full Epic workflow for developers
- 🔎 [Reviewer Guide](docs/team-collaboration/reviewer-guide.md) — Review checklist and process
- 📋 [Phase Lead Guide](docs/team-collaboration/phase-lead-guide.md) — Milestone planning and escalation
- 📊 [Decision Matrices](docs/team-collaboration/decision-matrices.md) — Who decides what, in table format
- 🚶 [Example Walkthrough](docs/team-collaboration/example-walkthrough.md) — Real Epic cycle using Taskflow example project
- ❓ [Team FAQ](docs/team-collaboration/faq.md) — 15 answered questions
- 🔧 [Troubleshooting Guide](docs/team-collaboration/troubleshooting-guide.md) — Common problems with solutions

### **Examples**
- 📚 [Phase P1](docs/phases/P1__System_Foundation_and_Adoption/) — Foundation and adoption artifacts
- 📚 [Phase P2](docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/) — Multi-project adoption artifacts
- 📚 [Phase P3](docs/phases/P3__Agentic_Execution_Model_Maturity/) — Autonomous cluster artifacts
- 👥 [Taskflow Team Example](examples/team-project-example/) — Team project example with real artifacts (E16.1)
- 🔍 See how this system was built using itself

### **Reference**
- 🏛️ [Governance Propagation](governance/systems/governance-propagation.md) — How governance flows
- 🗺️ [Project Tracker Integration](governance/systems/PROJECT-TRACKER-INTEGRATION-SYSTEM.md) — Tracker usage

---

## How It Works (5-Minute Overview)

Work cascades through four governance levels, each planned by the level above and executed by the level below. The system supports **two execution modes**:

---

### Mode 1: Manual (Chat Starter Copy-Paste)

The original governance model. No infrastructure needed beyond Git and an AI chat tool.

```
HQ Chat ──creates──→ Phase specs + Phase Execution Chat Starter
                        │  (copy-paste)
                        ▼
                   Phase Chat ──creates──→ Milestone specs + Milestone Execution Chat Starter
                                               │  (copy-paste)
                                               ▼
                                          Milestone Chat ──creates──→ Epic specs + Epic Execution Chat Starter
                                                                          │  (copy-paste)
                                                                          ▼
                                                                     Epic Mode  ──executes──→ Code, PRs, deliverables
```

**Flow:** Human copy-pastes Chat Starters → AI executes → Human reviews → HQ authorizes merge.

---

### Mode 2: Agentic (File-Driven Autonomous Cluster)

The P3 infrastructure automates handoffs. Requires Docker and the daemon process.

```

                               ┌─────────────────────────┐
                               │   .ai-project/queue/    │
                               │   File-Driven Triggers   │
                               └────┬────────────────────┘
                                    │ poll / write
                                    ▼
┌─────────────────────────────────────────────────────────────┐
│              ai-project-daemon (background)                  │
│  Polls queue → dispatches to orchestrator → monitors result │
└─────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────┐
│           ai-project-orchestrator (per-job)                  │
│  • Reads trigger JSON                                        │
│  • Launches Docker sandbox                                   │
│  • Runs Dev → QA loop (3 attempts max)                       │
│  • Produces completion / escalation report                    │
│  • Writes result back to queue                               │
└─────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────┐
│              Dockerfile.sandbox (ephemeral)                   │
│  • Isolated runtime with Node, Python, Go                     │
│  • Executes work, captures stdout/stderr                      │
│  • Secure filesystem with write-restricted volumes            │
│  • Self-destructs after completion                            │
└─────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                    ai-project-git-merge (auto-promotion)
                    Branch: epic/ → milestone/ → phase/
```

**Flow:** Trigger file appears in queue → daemon detects it → orchestrator runs sandboxed Dev-QA loop → result written → auto-merge promotes accepted work.

---

### The Governance Hierarchy (same for both modes)

### **1. HQ Plans the Phase**
HQ Chat defines the Phase scope, goals, and milestones, then issues the Phase spec.

### **2. Phase Plans the Milestones**
Phase Chat reviews the Phase spec, produces **Milestone specs** for each milestone, then returns them to HQ for acceptance.

### **3. Milestone Plans the Epics**
Milestone Chat reviews the Milestone spec, produces **Epic specs** for each epic, then returns them to Phase for acceptance.

### **4. Epic Executes**
Epic mode receives an Epic Execution Chat Starter (manual) or a trigger file (agentic) and executes:
- Creates branch
- Builds deliverables
- Self-validates against Definition of Done
- Produces Delivery Notice and **stops** (manual) or writes completion to queue (agentic)

### **5. Review (Human)**
Human evaluates deliverables:
- Does it meet acceptance criteria?
- Does it solve the stated problem?
- Is quality acceptable?

### **6. Close**
HQ makes decision:
- **Accept:** Authorize merge → branch promoted → Epic closed
- **Reject:** Document rationale → create new Epic or abandon
- **Request Changes:** Define iteration → Epic mode updates

---

## Choosing an Execution Mode

### How It Works

You don't "set" a mode at the project level. **Each Epic picks its delivery mechanism** at launch time. They share the same planning (Phase → Milestone → Epic specs), same branch strategy, same review gates, and same merge process.

```
                         Epic E2.1 ──manual──→ Chat Starter → AI session
                        /
Milestone M2 spec ─────┤
                        \
                         Epic E2.2 ──agentic──→ trigger JSON → daemon + sandbox
```

### When to Use Manual Mode

| Situation | Why |
|-----------|-----|
| **First Epic in a project** | No queue infrastructure set up yet; planning is still fluid |
| **Exploratory / ambiguous work** | Tight human feedback loop is more efficient than automated retries |
| **Debugging a complex issue** | You want to watch each step in the AI session |
| **No Docker available** | Only Git is required |

**How to launch:** Create an Epic Execution Chat Starter → copy-paste into an AI session → Epic mode executes → delivers notice as chat message.

### When to Use Agentic Mode

| Situation | Why |
|-----------|-----|
| **Repetitive Dev-QA cycles** | 3-attempt self-healing loop runs unattended |
| **Standardized work** (docs, refactors, tests) | Clear DoD, low ambiguity, high automation value |
| **24/7 execution** | Daemon polls queue continuously — drop a trigger file and walk away |
| **Multi-project scale** | Each project runs its own daemon independently |

**How to launch:** Write a JSON trigger file into `.ai-project/queue/` → daemon detects it → orchestrator runs Dev-QA loop → result written back to queue.

### Switching Mid-Project

There is no switch. Both mechanisms work simultaneously:

```bash
# Project structure — both modes coexist
my-project/
├── .ai-project/queue/
│   ├── 04_epic.json          ← agentic trigger (daemon processes this)
│   └── readme.txt            ← ignored (not .json)
├── .ai-project/queue/06_epic.json   ← another agentic trigger
├── docs/phases/
│   └── P1-M2-E2.3__spec__...       ← also launched manually via Chat Starter
└── governance/bin/ai-project-daemon --project-root . start   ← daemon running
```

- Daemon **on** → agentic triggers get processed; manual Chat Starters still work.
- Daemon **off** → agentic triggers sit in queue (processed when daemon restarts); manual mode unaffected.
- You can even launch the **same Epic both ways** — but don't. Pick one per Epic.

### Decision Flow

```
Is Docker available and configured?
├── NO  → Use manual mode (Chat Starter)
└── YES → Is the Epic's work well-defined with clear DoD?
          ├── NO  → Use manual mode (tighter feedback)
          └── YES → Consider agentic mode (trigger file + daemon)
```

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

**Option 1: Jump Right In (30 minutes) — Manual Mode**
- 👉 **[Quick Start Guide](governance/guides/QUICK-START.md)** — Learn the governance model by hand

**Option 2: Go Autonomous — Agentic Mode**

Requires Docker. Each project runs its own daemon to watch its `.ai-project/queue/`:

```bash
# From the ai-project-system repo itself (no flag needed):
bin/ai-project-daemon start

# From a project that has governance as a submodule:
cd ~/MyProject
governance/bin/ai-project-daemon --project-root . start

# Check status, stop:
ai-project-daemon status
ai-project-daemon stop
```

See [`bin/ai-project-daemon`](bin/ai-project-daemon) (daemon), [`Dockerfile.sandbox`](Dockerfile.sandbox) (sandbox), and [`bin/verify-loop.sh`](bin/verify-loop.sh) (test harness).  
Read Section 18 of [PROJECT-SYSTEM-GUIDELINES.md](governance/PROJECT-SYSTEM-GUIDELINES.md) for cluster execution rules.

**Option 3: Understand First, Then Practice**
1. **Read governance**
   - [PROJECT-SYSTEM-GUIDELINES.md](governance/PROJECT-SYSTEM-GUIDELINES.md) — System structure (15 min)
   - [AI-OPERATING-GUIDELINES.md](governance/AI-OPERATING-GUIDELINES.md) — Execution procedures (10 min)
2. **See visual overview**
   - [Epic Lifecycle Flow](governance/diagrams/epic-lifecycle-flow.md) — How Epics work (5 min)
   - [Authority Hierarchy](governance/diagrams/authority-hierarchy.md) — Document precedence (5 min)
3. **Start a project**
   - [How to Start a Project](governance/systems/start-a-project.md) — Step-by-step initialization

**You don't need to read everything to begin.**  
The system is designed to be learned incrementally. Start manual, graduate to agentic.

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

### Totals (P1 + P2 + P3)
✅ **47 Epics** delivered across **13 milestones** over **3 phases**

### Governance
- PROJECT-SYSTEM-GUIDELINES.md v3.0.0 (effective 2026-05-22)
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
- ✅ **Phase P3 Complete** — Agentic Execution Model Maturity (3 milestones, 12 Epics)
- ✅ **47 total Epics** delivered across 13 milestones, 3 phases
- ✅ **Production-ready** — Stable baseline for adoption and autonomous operation
- ✅ **Battle-tested** — Built using itself (dogfooding validated)
- ✅ **Governance stable** — v3.0.0 (effective 2026-05-22)
- ✅ **Complete documentation** — Quick-start, templates, examples, diagrams, FAQ
- ✅ **CLI tool** — `ai-project init` for one-command project setup
- ✅ **Governance Agent** — Single unified agent with HQ/Phase/Milestone/Epic modes
- ✅ **Override system** — Customizable branching, naming, and merge conventions
- ✅ **Adoption guide** — Step-by-step path from zero to HQ Chat live
- ✅ **Autonomous cluster** — File-driven queue, orchestrator, daemon, sandbox, auto-merge
- ✅ **Self-healing Dev-QA loops** — 3-attempt recursion with escalation on exhaustion
- ✅ **Hybrid model routing** — Remote for planning, local for execution
- ✅ **Licensed for adoption** — MIT + CC BY-SA 4.0 dual license

**What's Next (Future Phases):**
- **P4** — Unplanned. Options: System Operations & Observability, Public Release, Team Collaboration, or as directed.

**Intentional Characteristics:**
- Evolving deliberately based on real usage, not speculatively
- No web UI (not needed yet)
- Supports both manual and agentic execution — meet users where they are
- Hybrid model routing reduces token spend on repetitive Dev-QA loops

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

👉 **[Read the full contributing guide](CONTRIBUTING.md)**

---

## Questions?

- 📖 **Start here:** [Quick Start Guide](governance/guides/QUICK-START.md)
- ❓ **FAQ:** [Frequently Asked Questions](governance/guides/FAQ.md)
- 🎨 **Visualize:** [Diagrams](governance/diagrams/)
- 🔍 **Examples:** [Phase P1](docs/phases/P1__System_Foundation_and_Adoption/) | [Phase P2](docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/) | [Phase P3](docs/phases/P3__Agentic_Execution_Model_Maturity/)
- 📖 **Adoption Guide:** [Step-by-step walkthrough](governance/guides/ADOPTION-GUIDE.md)
- 💬 **Ask:** [Open an issue](https://github.com/panchew/ai-project-system/issues)
