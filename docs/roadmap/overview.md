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

### P5 – Process Hardening & Visual Artifacts *(Completed)*

**Goal**: Harden the governance process model, close communication gaps surfaced during P4 execution, and lay the framework foundation for visual artifact delivery.

**Status**: Completed (Consolidated to master 2026-06-28 — **v5.0.0**, 259/259 tests passing)

**Milestone Status**:

| Milestone | Name | Status | Completed |
|-----------|------|--------|-----------|
| **M20** | Governance Process Hardening | ✅ Complete | 2026-06-28 |
| **M21** | Adoption Clarity & Platform Agnosticism | ✅ Complete | 2026-06-28 |
| **M22** | Visual Artifacts | ✅ Complete | 2026-06-28 |

**Key Deliverables**:
- ✅ Git-tracking verification in starters (`git ls-files --error-unmatch`) — closes false-green "committed" gap (GH-1)
- ✅ Working-tree isolation convention for concurrent chats (GH-2)
- ✅ Scope routing rule — CFO direction flows through artifact cascade (GH-3)
- ✅ Platform agnosticism — governance delivery decoupled from `.github/agents/` (GH-5)
- ✅ Documentation clarity — `governance/` vs `.governance/` distinction explicit in adoption guides (GH-6)
- ✅ Phase/Milestone/Creation Chat roles defined in AOG §3.5–§3.7 and PSG §13A–§13B (GH-7, fixed early in v4.0.1)
- ✅ Artifact scope adjacency rule — chats produce artifacts for direct parent or direct children only (GH-8, SN-12a)
- ✅ Hierarchical communication protocol — escalations up one level; directives down via spec amendment (GH-9, SN-12b)
- ✅ Default-accept delivery model — parent auto-accepts clean deliveries; Review Decision is exception path only (SN-13)
- ✅ `visual_artifacts` spec in `.ai-project.yml` — opt-in toggle, ComfyUI URL, artifact type list (VA-1)
- ✅ Visual intent cascade — visual expectations propagate through Phase → Milestone → Epic artifact hierarchy
- ✅ Mermaid/PlantUML and ComfyUI integration guidelines in AOG and templates

---

## In Progress

### P6 – Visual Comprehension Layer & Process Refinements *(Active)*

**Goal**: Build the consumer architecture that turns the governance flow into a continuous
visual narrative — explaining the *proposed solution* and the *actual implementation* at
every level so the CFO can follow along with low cognitive load. Reverse the v5.0.0
binary-storage model to by-link, define the link + metadata binding convention, make
proposed-vs-implemented coverage routine, and define clips as single-parent documentation
that doubles as publishable media. Plus close the three P5 process carry-forwards.

**Status**: Active — opened 2026-06-29. Scoped via Creation Chat (SN-15 + SN-16); producer
(ComfyUI) and helper (`bin/ai-project-visual`) are done and verified, so P6 is the
governance/comprehension layer above them, not plumbing. See
[`docs/phases/P6__Visual_Comprehension_Layer_and_Process_Refinements/P6__phase-spec.md`](../phases/P6__Visual_Comprehension_Layer_and_Process_Refinements/P6__phase-spec.md).

**Milestones**:

| Milestone | Name | Scope |
|-----------|------|-------|
| **M23** | By-Link Storage Model & Binding Convention | P6-VC-1 (by-link reversal), P6-VC-2 (binding + metadata) |
| **M24** | Comprehension Behavior & Clips | P6-VC-3 (proposed-vs-implemented), P6-VC-4 (clips) |
| **M25** | Process Refinements | P6-GH-12, P6-GH-10, P6-GH-11 |

**Candidate Pool** *(single consolidated registry — folds GH-10/11 from the P5 Closure
Declaration and GH-12/13 from earlier roadmap drafts)*:

| ID | Title | Priority | Disposition |
|----|-------|----------|-------------|
| P6-VC-1 | By-link storage reconciliation — reverse the v5.0.0 commit-the-binary model; reconcile guide §4/§1, AOG §16.5, helper output guidance, and the integration test to by-link (explicit, named deliverable) | Highest | M23 |
| P6-VC-2 | Link + metadata binding convention — link carries what / level / proposed-vs-implemented / short description; load-bearing under by-link | High | M23 |
| P6-VC-3 | Proposed-vs-implemented comprehension behavior — routine two-track coverage at every level ("nothing is too much"), Structural-first | High | M24 |
| P6-VC-4 | Clips as documentation + publishable media — single-parent binding, verified LTX-Video path, publish path as same asset reused | High | M24 |
| P6-GH-12 | Phase-closure canonical sequence — README update, version bump, and tag as mandatory automatic steps (today needs a Steering Note) | High | M25 |
| P6-GH-13 | ComfyUI working integration | High | **Subsumed** — producer + helper delivered and verified (SN-16); the real work is the consumer/comprehension layer (P6-VC-1…4) |
| P6-GH-10 | Formally codify SN-13 default-accept model into AOG, PSG, and Starter templates | Medium | M25 |
| P6-GH-11 | Align `bin/ai-project-init` to write `.ai-project/agents/` (not `.github/agents/`) | Low | M25 |

---

## Guiding Principles

1. **Document before execute**
2. **Chats are ephemeral, Markdown is authoritative**
3. **Structure enables intelligence**
4. **Explicit is better than implicit**
5. **Consistency over optimization**

---

## Current Focus

Phases P1–P5 are **completed and consolidated to master** at **v5.0.0**.

**P6 — Visual Comprehension Layer & Process Refinements is active** (opened 2026-06-29).
The phase spec is open and `phase/P6` is branched; the Phase Chat is planning Milestones
M23–M25.

See individual phase directories for detailed specs:
- [`docs/phases/P1__System_Foundation_and_Adoption/`](../phases/P1__System_Foundation_and_Adoption/)
- [`docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/`](../phases/P2__Adoption_Architecture_and_Multi_Project_Support/)
- [`docs/phases/P3__Agentic_Execution_Model_Maturity/`](../phases/P3__Agentic_Execution_Model_Maturity/)
- [`docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/`](../phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/)
- [`docs/phases/P5__Process_Hardening_and_Visual_Artifacts/`](../phases/P5__Process_Hardening_and_Visual_Artifacts/)
- [`docs/phases/P6__Visual_Comprehension_Layer_and_Process_Refinements/`](../phases/P6__Visual_Comprehension_Layer_and_Process_Refinements/)
