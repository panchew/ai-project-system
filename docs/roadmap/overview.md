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

### P7 – Agentic Execution & Default-On Visuals *(Completed)*

**Goal**: The governance machine starts doing the work itself. Build `bin/run-dev-agent` and
complete the first real, non-mocked agentic run — the system executing its own epics through
the P3 orchestrator on local models (P7-AE-1) — flip visuals from opt-in to the default lens
the CFO follows that flow through (SN-17), and reconcile the adoption/execution contradictions
real consumer projects hit (P7-GH-16, P6-GH-14, P6-GH-15, P7-GH-17).

**Status**: Completed (Consolidated to master 2026-07-14 — **v6.0.0**, 306 passed / 1 skipped
by design). Second phase closed through the canonical **PSG §5C** sequence. See the
[Phase Closure Declaration](../phases/P7__Agentic_Execution_and_Default_On_Visuals/P7__phase-closure-declaration.md).

**Milestone Status**:

| Milestone | Name | Epics | Status | PR |
|-----------|------|-------|--------|-----|
| **M26** | First Real Agentic Run | E26.1–E26.3 (3) | ✅ Complete | #113 |
| **M27** | Visuals Default-On | E27.1–E27.3 (3) + B4.1 bugfix | ✅ Complete | #117 |
| **M28** | Governance Reconciliations | E28.1–E28.4 (4) | ✅ Complete | #125 |

**Key Deliverables**:
- ✅ First genuine non-mocked agentic run — `bin/run-dev-agent` wired as the orchestrator's
  `dev_command` on `qwen2.5-coder`, `04_epic.json` mock trigger retired, transcript accepted in
  `local-agent-runner`'s P2-M3 Milestone Chat (P7-AE-1)
- ✅ Visual artifacts default-on/opt-out framework-wide (AOG §16.1, §16.8 trigger policy,
  `visual_required_for_specs` enforcement key, structural-first zero-infra default) (P7-VC-1)
- ✅ Documented Ollama+ComfyUI single-GPU coexistence design (`governance/guides/
  gpu-coexistence.md`, orchestrator execution-lock reuse, exit code 5)
- ✅ Level-0 handoff coherent — scale-dependent fork (lightweight `genesis.md`→Phase Chat vs.
  full `seed.md`→HQ Chat) codified across all four docs; HQ Chat Opener template promoted to
  `governance/templates/` (P7-GH-16)
- ✅ Delivery-Notice terminology reconciled — PSG §12/AOG's practiced single-artifact model
  confirmed as canonical; `artifact-communication-protocol.md` rewritten to match (P6-GH-14)
- ✅ `ai-project-init` installs the canonical `governance.agent.md`, not the superseded
  `hq.agent.md` (P6-GH-15)
- ✅ Delivery Authorization ceremonial block retired everywhere it survived — both starter
  templates, all three `governance/systems/` mirrors, and AOG §1A/§10 — in-chat merge
  authorization preserved (P7-GH-17)
- ✅ Governance at delivery: **PSG v2.3.0**, **AOG v2.9.0**

---

### P8 – Visual Artifacts Activation *(Completed)*

**Goal**: Make `visual_artifacts` real in this source repo. Resolve the `types: diagrams` /
Structural naming collision (P7-GH-21), flip `visual_artifacts.enabled: true` for real against
the local ComfyUI endpoint, and validate whether the P6-verified workflows produce artifacts
precise enough for technical explanation — not merely "renders successfully" (SN-20).

**Status**: Completed (Consolidated to master 2026-07-17 — **v6.0.1**, 307 passed / 0 skipped).
Third phase closed through the canonical **PSG §5C** sequence. See the
[Phase Closure Declaration](../phases/P8__Visual_Artifacts_Activation/P8__phase-closure-declaration.md).

**Milestone Status**:

| Milestone | Name | Epics | Status | PR |
|-----------|------|-------|--------|-----|
| **M29** | Visual Artifacts Activation | E29.1–E29.3 (3) | ✅ Complete | #133 |

**Key Deliverables**:
- ✅ `visual_artifacts.types` reframed as Generative-only categories across all four named
  surfaces (yml-spec §3.5, `.ai-project.yml`, `bin/ai-project-visual` docstring,
  `VISUAL-ARTIFACTS.md`) — Structural mode documented as needing no `visual_artifacts` config
  at all. **P7-GH-21 closed** (E29.1)
- ✅ `visual_artifacts.enabled: true` in this repo for the first time — the trade every prior
  milestone (P5-M22, P7-M27) deferred. `test_helper_generates_against_endpoint` now a real pass
  against the live endpoint, not a skip; two genuine helper bugs found and fixed in the process
  (stale default checkpoint, fixed-seed empty-output caching) (E29.2)
- ✅ First real generated-and-hosted artifacts from this repo, judged against the
  technical-explanation bar: a diagram-style case (FLUX-schnell) and a clip-style case
  (LTX-Video) — **both judged FAIL**, honest evidence handed to the CFO for SN-20 Carry-Over
  item 3 (E29.3)
- ✅ First machine-level `system_request`/`system_response` round-trip, provisioning a local
  storage backend to complete E29.3's by-link hosting
- ✅ Governance at delivery: **PSG v2.3.0**, **AOG v2.9.0**, yml-spec **v2.3.1**

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

### P9 – Context Handling and Token Efficiency *(Completed)*

**Goal**: Make token use as smart and effective as possible. The original model-tier
assumption (local models only at the Epic level, frontier everywhere else) failed in
practice — premium quota exhausted, no frontier reasoning left when it mattered. P9 replaced
assumption with evidence-grounded policy, gave the working levels a real dual-mode switch
with a guardrail on both sides, and canonized the system-level participant already running
in the field.

**Status**: Completed (Consolidated to master 2026-07-20 — **v7.0.0**, 363 passed / 0
skipped). Fourth phase closed through the canonical **PSG §5C** sequence. See the
[Phase Closure Declaration](../phases/P9__Context_Handling_and_Token_Efficiency/P9__phase-closure-declaration.md).

**Milestone Status**:

| Milestone | Name | Epics | Status | PR |
|-----------|------|-------|--------|-----|
| **M30** | Token Measurement & Model-Tier Audit | E30.1–E30.4 (4) | ✅ Complete | #135 |
| **M31** | Dual-Mode Working Levels & Model Guardrail | E31.1–E31.3 (3) | ✅ Complete | #144 |
| **M32** | System Participant Canonization & Governance Hygiene | E32.1–E32.3 (3) | ✅ Complete | #145 |

**Key Deliverables**:
- ✅ Real captured token-burn data per chat level and task type, including governance-corpus
  overhead, with every uncapturable cell recorded as an explicit gap rather than a guess
  (`bin/measure-token-burn`) (M30)
- ✅ Evidence-grounded frontier-vs-local policy (`model-routing-policy.md`, rows P1–P7)
  replacing the falsified `.ai-project.yml` `models:` mapping (M30)
- ✅ Evidence-sized context-load reduction (pack reduction across the three starter
  templates) and the reference-first artifact-handoff rule (AOG §3.1.1, SN-23) replacing
  mandated body-echo (M30)
- ✅ Per-instance manual/agentic Execution Mode for Phase/Milestone/Epic Chats
  (`chat-hierarchy.md`); Creation and HQ Chat recorded manual-only, permanently (M31)
- ✅ Agentic paid-vs-local decision logic applying the M30 policy; `DEFAULT_MODELS`
  falsified-name fix; local-unavailable handling for GPU contention with ComfyUI (M31)
- ✅ Manual-mode startup guardrail — a chat on a mismatched model refuses, at every manual
  level including HQ and Creation (M31)
- ✅ System HQ canonized: `system_request`/`system_response` schemas, an explicit
  out-of-hierarchy annex in `chat-hierarchy.md`, a normative execute-never-decide authority
  boundary, and a daily System Chat re-instantiation seed (M32)
- ✅ P8-GH-1 (stale opt-out prose) and P8-GH-3 (vestigial "Phase Delivery Notice" phrasing)
  reconciled, grep-clean; P8-GH-2 restated as deferred, not dropped (M32)
- ✅ Governance at delivery: **PSG v2.3.0**, **AOG v2.10.0**, yml-spec **v2.5.0**, protocol
  **v1.4.0**

---

## In Progress

No active phase. P10 is not yet scoped.

---

## Guiding Principles

1. **Document before execute**
2. **Chats are ephemeral, Markdown is authoritative**
3. **Structure enables intelligence**
4. **Explicit is better than implicit**
5. **Consistency over optimization**

---

## Current Focus

Phases P1–P9 are **completed and consolidated to master** at **v7.0.0**.

**P10 is not yet scoped.** P9 closed 2026-07-20 having replaced the failed model-tier
assumption with evidence-grounded policy, given the working levels a real dual-mode switch
with a guardrail on both sides, and canonized the system-level participant field-adopted
since 2026-07-16. Next-phase scoping is HQ/Creation Chat's call.

See individual phase directories for detailed specs:
- [`docs/phases/P1__System_Foundation_and_Adoption/`](../phases/P1__System_Foundation_and_Adoption/)
- [`docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/`](../phases/P2__Adoption_Architecture_and_Multi_Project_Support/)
- [`docs/phases/P3__Agentic_Execution_Model_Maturity/`](../phases/P3__Agentic_Execution_Model_Maturity/)
- [`docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/`](../phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/)
- [`docs/phases/P5__Process_Hardening_and_Visual_Artifacts/`](../phases/P5__Process_Hardening_and_Visual_Artifacts/)
- [`docs/phases/P6__Visual_Comprehension_Layer_and_Process_Refinements/`](../phases/P6__Visual_Comprehension_Layer_and_Process_Refinements/)
- [`docs/phases/P7__Agentic_Execution_and_Default_On_Visuals/`](../phases/P7__Agentic_Execution_and_Default_On_Visuals/)
- [`docs/phases/P8__Visual_Artifacts_Activation/`](../phases/P8__Visual_Artifacts_Activation/)
- [`docs/phases/P9__Context_Handling_and_Token_Efficiency/`](../phases/P9__Context_Handling_and_Token_Efficiency/)
