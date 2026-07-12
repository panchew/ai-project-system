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

### P6 – Visual Comprehension Layer & Process Refinements *(Completed)*

**Goal**: Build the consumer architecture that turns the governance flow into a continuous
visual narrative — explaining the *proposed solution* and the *actual implementation* at
every level so the CFO can follow along with low cognitive load — plus close the three P5
process carry-forwards.

**Status**: Completed (Consolidated to master 2026-07-08 — **v5.1.0**, 260 passed / 1 skipped
by design). First phase closed through the canonical **PSG §5C** sequence — the very sequence
P6 itself codified. See the
[Phase Closure Declaration](../phases/P6__Visual_Comprehension_Layer_and_Process_Refinements/P6__phase-closure-declaration.md).

**Milestone Status**:

| Milestone | Name | Epics | Status | PR |
|-----------|------|-------|--------|-----|
| **M23** | By-Link Storage Model & Binding Convention | E23.1–E23.2 (2) | ✅ Complete | #96 |
| **M24** | Comprehension Behavior & Clips | E24.1–E24.2 (2) | ✅ Complete | #99 |
| **M25** | Process Refinements | E25.1–E25.6 (6) | ✅ Complete | #102 |

**Key Deliverables**:
- ✅ By-link storage model — generated visual material referenced by link, never committed to git (v5.0.0 commit-the-binary guidance reversed and reconciled everywhere) (P6-VC-1)
- ✅ Binding convention (guide §7) — link + What / Level / State / Description metadata with per-level placement (P6-VC-2)
- ✅ Proposed-vs-implemented visuals as the routine default at every level, Structural-first (AOG §16.6) (P6-VC-3)
- ✅ Single-parent clips as documentation that doubles as publishable media, on the verified LTX-Video path (AOG §16.7, guide §8) (P6-VC-4)
- ✅ Canonical phase closure (PSG §5C) — README update, version bump, tag as mandatory automatic steps (P6-GH-12)
- ✅ SN-13 default-accept codified (PSG §11.6, AOG §12) and reconciled framework-wide, Layer-8 human review preserved (P6-GH-10)
- ✅ `ai-project-init` writes tool-neutral `.ai-project/agents/`, with the framework's first test of that behavior (P6-GH-11)
- ✅ Governance at delivery: **PSG v2.3.0**, **AOG v2.6.0**

---

## In Progress

### P7 – Agentic Execution & Default-On Visuals *(Active)*

**Goal**: The governance machine starts doing the work itself. Build `bin/run-dev-agent` and
complete the first real, non-mocked agentic run — the system executing its own epics through
the P3 orchestrator on local models (P7-AE-1) — flip visuals from opt-in to the default lens
the CFO follows that flow through (SN-17), and reconcile the adoption/execution contradictions
real consumer projects hit (P7-GH-16, P6-GH-14, P6-GH-15).

**Status**: Active — opened 2026-07-12. Scoped via Creation Chat (SN-18 spine) on the HQ
ruling (2026-07-11) and SN-17. Both halves of the first run are ready: orchestration proven
(verify-loop 5/5, mocked) and `local-agent-runner` P2 runner-side support delivered — the
adapter is the one remaining variable. See
[`docs/phases/P7__Agentic_Execution_and_Default_On_Visuals/P7__phase-spec.md`](../phases/P7__Agentic_Execution_and_Default_On_Visuals/P7__phase-spec.md).

**Milestones**:

| Milestone | Name | Candidates |
|-----------|------|------------|
| **M26** | First Real Agentic Run *(scheduled first — binding)* | P7-AE-1 |
| **M27** | Visuals Default-On | P7-VC-1 (SN-17) + Ollama/ComfyUI coexistence design task |
| **M28** | Governance Reconciliations | P7-GH-16, P6-GH-14, P6-GH-15 |

**Candidate → milestone mapping** *(single registry; IDs as named by their source)*:

| ID | Title | Priority | Milestone | Source |
|----|-------|----------|-----------|--------|
| P7-AE-1 | **`bin/run-dev-agent` adapter — first real agentic run.** Wire `local-agent-runner` (v1.0.0 proven) as the P3 orchestrator's `dev_command`: task = epic DoD, context = scoped spec/starter (never full governance), tools = coding set scoped to the repo, model from `AI_PROJECT_ACTIVE_MODEL`. Must not depend on the runner's `final_answer` (unreliable); switch `epic_dev` `llama3:8b` → `qwen2.5-coder:14b`; drop the `04_epic.json` mock trigger; exit = a live Epic completes non-mocked **and** its transcript is accepted in the runner's P2-M3 Milestone Chat. Runner-side gate **cleared** (HQ ruling 2026-07-11). | High | **M26** | [GH #111](https://github.com/panchew/ai-project-system/issues/111) |
| P7-VC-1 | **Visual production default-on (opt-out).** Flip `visual_artifacts` opt-in → **default-on with explicit opt-out** (`enabled: false`); reconcile AOG §16.1, spec §3.5, guide, templates, agent defs. **Structural-first** (generative only when `comfyui_url` present — safe at zero infra). **Trigger set:** automatic for **specs + delivery/closure declarations**; all else on demand. **Enforcement is a setting** (`visual_required_for_specs`-style, default true), not a hard gate. Four decisions settled — turn into epics, not re-debate. | High | **M27** | [SN-17](../../.ai-project/artifacts/steering-notes/2026-07-11__creation-chat__steering-note__visuals-default-on.md) |
| P7-GH-16 | **Level-0 handoff defined two contradictory ways.** `seed.md` Rule 4 → Brief + HQ Opener → HQ Chat; `genesis.md` / `start-a-project.md` / `chat-hierarchy.md` → committed `genesis.md` → Phase Chat directly (HQ never opened). Decide the canonical output (or codify both as scale-dependent) and reconcile all four docs. Sub-item (SN-2): promote `systems/hq-chat-opener.md` into `templates/`. | Medium | **M28** | [GH #110](https://github.com/panchew/ai-project-system/issues/110) |
| P6-GH-14 | P4.1-vs-PSG §12 Delivery-Notice ordering inconsistency; surfaced during E25.4 | Medium | **M28** | P6 Closure Declaration |
| P6-GH-15 | `bin/ai-project-init` installs the superseded `hq.agent.md` instead of the canonical `governance.agent.md`; surfaced during E25.6 | Low | **M28** | P6 Closure Declaration |

**Coexistence (SN-18 decision 4):** the Ollama runner + ComfyUI single-GPU contention
(`~/soft-dev/ai-stack`) is resolved as a **design task inside M27** — designed where it bites
(when generative visuals run), not its own epic, not deferred.

---

## Guiding Principles

1. **Document before execute**
2. **Chats are ephemeral, Markdown is authoritative**
3. **Structure enables intelligence**
4. **Explicit is better than implicit**
5. **Consistency over optimization**

---

## Current Focus

Phases P1–P6 are **completed and consolidated to master** at **v5.1.0**.

**P7 — Agentic Execution & Default-On Visuals is active** (opened 2026-07-12). The phase spec
is open and the Phase Chat plans **M26 — First Real Agentic Run** first (binding), the
milestone that makes the system execute its own epics for real and unblocks the stalled
`local-agent-runner` P2. M27 (visuals default-on) and M28 (governance reconciliations) follow.

See individual phase directories for detailed specs:
- [`docs/phases/P1__System_Foundation_and_Adoption/`](../phases/P1__System_Foundation_and_Adoption/)
- [`docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/`](../phases/P2__Adoption_Architecture_and_Multi_Project_Support/)
- [`docs/phases/P3__Agentic_Execution_Model_Maturity/`](../phases/P3__Agentic_Execution_Model_Maturity/)
- [`docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/`](../phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/)
- [`docs/phases/P5__Process_Hardening_and_Visual_Artifacts/`](../phases/P5__Process_Hardening_and_Visual_Artifacts/)
- [`docs/phases/P6__Visual_Comprehension_Layer_and_Process_Refinements/`](../phases/P6__Visual_Comprehension_Layer_and_Process_Refinements/)
- [`docs/phases/P7__Agentic_Execution_and_Default_On_Visuals/`](../phases/P7__Agentic_Execution_and_Default_On_Visuals/)
