# Project Roadmap

## Vision

Build a **formal, repeatable project system** for AI-assisted software development that:
- Treats documentation as a first-class artifact
- Makes execution context explicit and derivable
- Enables parallel work without coordination overhead
- Scales from solo projects to team collaboration

This system eliminates the chaos of ephemeral chats and lost context.

---

## Completed Phases

### P0 – Project Formalization *(Retired)*

**Goal**: Bootstrap the repository and formalize the initial system contract.

**Status**: Retired (Completed 2026-01-25)

**Milestone**:
- **M0.1** – Repository Bootstrap *(Completed)*

---

### P1 – System Foundation & Adoption *(Fully Closed)*

**Goal**: Establish the AI Project System as a stable, adoptable, and self-hosting system.

**Status**: Fully Closed (Started 2026-01-14, Completed 2026-04-18)

**Milestones**:
- **M14** – Genesis & Integration Baseline *(Completed)*
- **M15** – Execution Ergonomics & Validation *(Completed)*
- **M16** – Governance Distribution & Adoption *(Completed)*
- **M17** – Adoption Readiness & Practical Enablement *(Completed)*
- **M5** – System Refinement from Real Usage *(Completed)*

**Key Deliverables**:
- ✅ Repository structure aligned with PROJECT-SYSTEM-GUIDELINES.md
- ✅ Authoritative governance documents published
- ✅ Complete phase/milestone/epic documentation framework
- ✅ Project tracker integration system
- ✅ Human review and acceptance framework
- ✅ Governance propagation model
- ✅ Templates and scaffolding
- ✅ Quick-start guide and visual documentation
- ✅ Example project and walkthrough
- ✅ FAQ, licensing, and community readiness
- ✅ Milestone/epic closure process specification
- ✅ Unplanned progress branch model
- ✅ Epic Execution Chat Starter format

---

### P2 – Adoption, Architecture & Multi-Project Support *(Completed)*

**Goal**: Evolve the governance model for multi-project support, CLI tooling, override boundaries, and adoption readiness.

**Status**: Completed (Consolidated to master 2026-05-22)

**Milestones**:
- **M6** – Governance Folder Restructure *(Completed)*
- **M7** – CLI Initialization Tool *(Completed)*
- **M8** – HQ Agent & End-to-End Validation *(Completed)*
- **M9** – Override Boundaries & System Refinement *(Completed)*
- **M10** – Adoption & Phase P2 Closure *(Completed)*

**Key Deliverables**:
- ✅ Restructured governance directory (`governance/`) with guides and templates
- ✅ `.ai-project.yml` configuration spec (v2.0.0+)
- ✅ Submodule support for multi-project governance distribution
- ✅ Migration guide for legacy users
- ✅ CLI initialization tool (`bin/ai-project-init`)
- ✅ HQ Agent deployment and end-to-end validation
- ✅ Override spec and precedence rules
- ✅ Adoption guides, FAQ, and multi-project onboarding

---

### P3 – Agentic Execution Model Maturity *(Completed)*

**Goal**: Transform the AI Project System from a human-mediated documentation framework into an unattended, 24/7 autonomous development cluster with file-driven state machines, sandboxing, and hybrid model routing.

**Status**: Completed (Consolidated to master 2026-05-24)

**Milestones**:
- **M11** – File-Driven Bus & State Triggers *(Completed)*
- **M12** – Containerized Sandbox & Loop Verification *(Completed)*
- **M13** – Orchestrator CLI Daemon *(Completed)*

**Key Deliverables**:
- ✅ `.ai-project/queue/` — File-driven message bus with JSON trigger schemas
- ✅ `bin/ai-project-orchestrator` — Core orchestration engine with 3-attempt Dev-QA loop
- ✅ `Dockerfile.sandbox` — Isolated container runtime for execution and validation
- ✅ `bin/ai-project-daemon` — Background service for continuous queue monitoring
- ✅ `bin/ai-project-git-merge` — Automated branch promotion and merge utility
- ✅ `bin/verify-loop.sh` — 5-scenario closed-loop verification harness (all passing)
- ✅ `bin/verify-daemon.sh` — Daemon lifecycle and integration test suite
- ✅ `bin/build-sandbox.sh` — Sandbox image builder
- ✅ Hybrid model routing (remote for planning, local for execution)
- ✅ Closed-loop execution with self-healing, 3-attempt ceiling, escalation reports
- ✅ Stale lock recovery and signal-based cleanup
- ✅ PROJECT-SYSTEM-GUIDELINES.md Sections 18A–18D (cluster execution rules)

---

### P4 – Team Collaboration & Artifact-Driven Communication *(Completed)*

**Goal**: Extend the AI Project System from solo developer execution to full team collaboration, with artifact-driven communication, role-based authorization, and explicit production deployment gates.

**Status**: Completed (Consolidated to master 2026-06-20 — **v4.0.0**, 226/226 tests passing)

**Milestone Status**:

| Milestone | Name | Status | Completed |
|-----------|------|--------|-----------|
| **M14** | Artifact System Implementation | ✅ Complete | 2026-06-09 |
| **M15** | Cleanup and Salvage | ✅ Complete | 2026-06-13 |
| **M16** | Team Collaboration Example & Documentation | ✅ Complete | 2026-06-16 |
| **M17** | Bug Fixes & Polish | ✅ Complete | 2026-06-18 |
| **M18** | Inception Artifacts | ✅ Complete | 2026-06-19 |
| **M19** | Creation Chat Completion and Bugfix Workflow | ✅ Complete | 2026-06-20 |

**Key Deliverables**:
- ✅ `governance/systems/artifact-communication-protocol.md` — Canonical artifact schemas & workflows
- ✅ `governance/templates/completion-notice-epic.md` — Completion Notice template
- ✅ `governance/templates/review-decision.md` — Review Decision template
- ✅ `governance/templates/delivery-notice.md` — Delivery Notice template
- ✅ `governance/systems/bugfix-epic-workflow.md` — Bugfix Epic workflow with expedited SLA & production gate
- ✅ `governance/systems/roles-authorization-team-governance.md` — Role definitions, decision matrices, authorization rules, escalation paths
- ✅ `governance/templates/genesis.md` — Project bootstrap form (fill-in-the-blank)
- ✅ `governance/templates/seed.md` — Creation Chat session opener (AI role definition)
- ✅ `governance/systems/chat-hierarchy.md` — Level 0 (Creation Chat) through Level 4 (Epic)
- ✅ `governance/templates/steering-note.md` — Creation Chat → HQ artifact
- ✅ `governance/templates/progress-digest.md` — HQ → Creation Chat status artifact
- ✅ `governance/templates/bouncer-work-log.md` — Layer 8 manual intervention log
- ✅ `governance/systems/creation-chat-guide.md` — Re-instantiation ritual and ongoing usage
- ✅ CFO PR review gate (`cfo_review_gate` in `.ai-project.yml`)

---

## Upcoming

### P5 – Governance Hardening & Platform Agnosticism *(Planned)*

**Goal**: Address process gaps surfaced during P4 execution and decouple the governance framework from GitHub/Copilot-specific conventions.

**Status**: Candidates identified — scoping via Creation Chat before phase spec is opened.

**Registered Candidates**:

| ID | Title | Priority |
|----|-------|----------|
| P5-GH-1 | Prerequisite git-tracking verification in starters (false-green "✅ committed") | Medium |
| P5-GH-2 | Working-tree isolation convention for concurrent chats | High |
| P5-GH-3 | Scope routing rule — CFO direction must flow through artifact cascade | Medium |
| P5-GH-4 | Add Creation Chat session opener step to `start-a-project.md` | Low |
| P5-GH-5 | Platform agnosticism — decouple `.github/agents/` path from governance delivery | Medium |
| P5-GH-6 | Documentation clarity — `governance/` vs `.governance/` distinction not surfaced upfront in sync and adoption guides | Medium-High |
| — | README/roadmap staleness (P4 now shown as complete — this update) | Done |
| — | CFO Dashboard | Deferred by design |

---

## Guiding Principles

1. **Document before execute**
2. **Chats are ephemeral, Markdown is authoritative**
3. **Structure enables intelligence**
4. **Explicit is better than implicit**
5. **Consistency over optimization**

---

## Current Focus

All phases (P1–P4) are **completed and consolidated to master** at **v4.0.0**.

**P5** is in pre-scoping — candidates are registered above. The phase spec will open
after a Creation Chat session establishes the theme and priorities.

See individual phase directories for detailed specs:
- [`docs/phases/P1__System_Foundation_and_Adoption/`](../phases/P1__System_Foundation_and_Adoption/)
- [`docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/`](../phases/P2__Adoption_Architecture_and_Multi_Project_Support/)
- [`docs/phases/P3__Agentic_Execution_Model_Maturity/`](../phases/P3__Agentic_Execution_Model_Maturity/)
- [`docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/`](../phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/)
