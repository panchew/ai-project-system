---
phase: P4
name: Team Collaboration and Artifact-Driven Communication
status: active
start_date: 2026-05-29
planned_end_date: 2026-07-31
version: 1.3.0
---

# Phase P4: Team Collaboration and Artifact-Driven Communication

## Executive Summary

Phase P4 transforms the AI Project System from a solo-developer framework (P1-P3) into a **team-capable governance system** with artifact-driven communication, role-based authorization, and explicit production deployment gates.

**Key Achievement:** Multiple humans and agents can work together with clear decision boundaries, no governance divergence, and full audit trails. CFO (Layer-8) remains the single source of strategic authority while teams scale from 2 people to 20+.

---

## Vision

By the end of P4:

✅ **Multiple teams** can use the AI Project System concurrently on different projects
✅ **Multiple contributors** can work on the same project without coordination overhead
✅ **Explicit decisions** are recorded via artifacts (not ephemeral chat)
✅ **CFO oversight** is lightweight (1-3 hours per week) yet maintains strategic control
✅ **Production gate** is never bypassed — CFO always authorizes production deploys
✅ **Audit trail** is complete — every decision, every merge, every deployment is recorded

---

## Scope

### Three Pillars

#### P4.1: Artifact-Driven Communication
Create canonical artifact formats for predictable hand-offs between chats.

**Deliverables:**
- ✅ **Protocol Design:** `governance/systems/artifact-communication-protocol.md` (complete)
- ⏳ **Daemon Integration:** Parse and route artifacts via queue system
- ⏳ **Integration Tests:** Multi-artifact workflow validation (Planning → Completion → Review → Delivery)
- ⏳ **HQ Chat Update:** Reference artifact system in HQ Starter

#### P4.2: Bugfix Epic Workflow
Create expedited path for unplanned production issues.

**Deliverables:**
- ✅ **Workflow Design:** `governance/systems/bugfix-epic-workflow.md` (complete)
- ⏳ **HQ Chat Handler:** Evaluate issue and create Bugfix Epic
- ⏳ **Escalation Handler:** Manage expedited 4-hour SLA reviews
- ⏳ **Post-Mortem Template:** Critical/High severity bugfix analysis

#### P4.3: Roles & Authorization
Define roles, decision authorities, and escalation paths for teams.

**Deliverables:**
- ✅ **Governance Model:** `governance/systems/roles-authorization-team-governance.md` (complete)
- ⏳ **Example Project:** 3-person team, 2-3 concurrent Epics
- ⏳ **Role Playbook:** Decision matrices, when-to-escalate guides

### Out of Scope (P5 or Later)
- System Operations (dashboards, observability, runbooks)
- Public release & community contribution model
- Advanced features (dependency tracking, resource allocation, burn-down charts)

---

## Milestones

### M14: Artifact System Implementation (2-3 Epics)

**Goal:** Implement artifact parsing, routing, and integration in daemon and agents.

**Epics:**
- **E14.1 – Artifact Parsing & Schema Validation**
  - Parse YAML frontmatter from Completion Notice files
  - Validate artifact schema (required fields, types, references)
  - Route artifacts to correct parent chat based on epic_id/milestone_id
  - Test on all three artifact types (Completion Notice, Review Decision, Delivery Notice)

- **E14.2 – Daemon Queue Integration**
  - Extend daemon to detect Completion Notice files in `.ai-project/artifacts/completion-notices/`
  - Route to parent Milestone Chat or HQ Chat
  - Detect Review Decision files, route back to Epic Chat
  - Detect Delivery Notice files, route to parent for acknowledgment
  - Handle race conditions (file written while being read)

- **E14.3 – Integration Tests**
  - Test end-to-end: Epic completes → Completion Notice → Milestone reviews → Review Decision → Epic merges → Delivery Notice
  - Test rework cycle: Rejection → Epic reworks → new Completion Notice (v1.1) → Review Decision Accept
  - Test escalation: Milestone cannot decide → escalate to Phase/HQ
  - Test manual mode: copy-paste artifacts between chats works alongside agentic mode

---

### M15: Cleanup and Salvage (1-2 Epics)

**Goal:** Make master honest, canonical, and coherent before any P4 feature work begins.
Remove stale artifacts, correct governance documentation, and recover the complete M14
implementation from its stranded branch.

**Epics:**
- **E15.1 – Master Cleanup**
  - Delete M1-nomenclature planning artifacts that misrepresent M14 as "not yet started"
  - Remove obsolete completion templates; identify canonical template
  - Rewrite `start-a-project.md` to reflect current `ai-project init` + submodule flow
  - Update P4 phase spec to global M15–M20 milestone numbering

- **E15.2 – M14 Salvage**
  - Recover M14 artifact system implementation from stranded branch
  - Merge complete M14 work (E14.1, E14.2, E14.3) to master
  - Verify integration tests pass on master

---

### M16: Team Collaboration Example & Documentation (2 Epics) ✅ COMPLETE

**Goal:** Create a working example project and role-based documentation to make the P4
team collaboration model tangible for new adopters.

**Epics (delivered 2026-06-16, merged to phase/P4):**
- **E16.1 – Example Project Setup & Walkthrough**
  - `examples/team-project-example/` with Phase P1, 3 Milestones, 9 Epic specs
  - 5-role TEAM_SETUP; 10 sample artifacts; WALKTHROUGH.md
  - Validation test suite: `tests/test_example_project_artifacts.py`
- **E16.2 – Team Collaboration Documentation**
  - 10 role guides in `docs/team-collaboration/`
  - CFO Quick Start, Team Onboarding, Contributor, Reviewer, Phase Lead guides
  - Decision Matrices, FAQ, Troubleshooting Guide

---

### M17: Bug Fixes & Polish (2 Epics) ✅ COMPLETE

**Goal:** Fix the daemon orchestrator path issue blocking submodule users; bring all
starters, templates, and governance documents current with P4.

**Epics (delivered 2026-06-18, merged to phase/P4):**
- **E17.1 – Fix Daemon Orchestrator Path Resolution**
  - Root cause: path derived from PROJECT_ROOT rather than daemon's own directory
  - Ordered cached fallback search; `--check` flag; 17 new unit tests
- **E17.2 – Update Starters and Documentation**
  - HQ Execution Chat Starter created (completes the four-level starter set)
  - Three governance templates: merge-authorization, epic-closure-notice, escalation-notice
  - P4 Governance System Guide; FAQ (23 questions); Troubleshooting (16 entries)
  - Starter branch-name lint check; "Epic Completion Report" term fully retired
  - Two-Stage Lifecycle flow documented in starters (partial delivery of original M17 scope)

> **Deferred:** The Two-Stage Lifecycle *lifecycle diagram* planned in the original M17
> scope was not delivered. M17 (executed) provided documentation coverage of the flow in
> the starters; the diagram remains **deferred** to a future phase.

---

### M18: Inception Artifacts (1 Epic)

**Goal:** Define and implement the Creation Chat / Genesis layer for new project
onboarding — the foundational entry point that tells a new user (or agent) exactly how
to begin a project under the governance system.

**Epics:**
- **E18.1 – Genesis Template and Creation Chat**
  - Create `governance/templates/genesis.md` — canonical entry point for new project setup
  - Define Creation Chat role: what context it receives, what it produces
    (HQ context packet, Phase 1 scope, first milestone plan)
  - Update `start-a-project.md` to reference the Creation Chat flow end-to-end
  - Validate with a real new-project walkthrough (run the flow, confirm outputs)

---

### M19: Creation Chat Completion and Bugfix Workflow (2 Epics) — **Final P4 milestone**

**Goal:** Close the two remaining P4 success criteria — the Creation Chat onboarding
surface and the end-to-end Bugfix Workflow — in a single final milestone. M19 consolidates
the previously separate M19 (Two-Stage Lifecycle) and M20 (Bugfix Workflow) plans; the
original M19 lifecycle *diagram* is deferred (see the note under M17).

**Epics:**
- **E19.1 – Bugfix Workflow**
  - `docs/bugfixes/` with the B#.# naming convention
  - HQ Chat "Handling Production Issues" handler (evaluate → spec → authorize → SLA →
    escalate)
  - Deployment Authorization and Post-Mortem templates
  - SLA tracking (4-hour window) and escalation documented in the bugfix workflow
  - Carry-overs: roadmap update, pytest dependency, this phase-spec update to v1.3.0

- **E19.2 – Creation Chat Completion**
  - Complete the Creation Chat ongoing-artifacts surface begun in M18

This is the **final P4 milestone**; P4 closes when M19 is delivered.

---

## Success Criteria

### P4 is Complete When:

1. ✅ **Artifact System Works End-to-End**
   - Epic completes → produces Completion Notice
   - Milestone reviews Completion Notice → issues Review Decision
   - Epic receives Accept → merges PR → produces Delivery Notice
   - All artifacts stored in `.ai-project/artifacts/` and committed to repo

2. ✅ **Bugfix Workflow Works**
   - Issue reported to HQ Chat
   - HQ creates Bugfix Epic (B#.#)
   - Epic executes in sandbox
   - HQ reviews within 4-hour SLA
   - Deployment requires CFO authorization
   - Post-mortem generated for Critical/High

3. ✅ **Team Example Project Runs Successfully**
   - 3-person team onboarded (CFO, Phase Lead, 2 Contributors)
   - 2-3 Epics run concurrently
   - All artifacts flow correctly between chats
   - Team can execute end-to-end without governance confusion

4. ✅ **Documentation Complete**
   - Role playbooks created
   - CFO guide created
   - Team onboarding guide created
   - All "how-to" scenarios documented with examples

5. ✅ **Known Bug Fixed**
   - Daemon orchestrator path resolution works on fresh project init

---

## Acceptance Criteria

The CFO (Layer-8) will accept P4 complete when:

- [ ] Can visit HQ Chat and see structured Completion Notices from Epics (not informal messages)
- [ ] Can issue Review Decision (Accept/Reject) that flows back to child chat
- [ ] Can authorize production deployment via Deployment Authorization artifact
- [ ] Can create a Bugfix Epic in <5 minutes for urgent production issue
- [ ] Can read "Team Collaboration Example" and onboard new 2-person team in <1 hour
- [ ] Can review progress across 3 projects via aggregated Completion Notices (CFO Dashboard)
- [ ] Can delegate Phase Lead role to team member without losing visibility
- [ ] All decisions recorded in artifacts and accessible in git history

---

## Technical Architecture

### Artifact Storage

```
.ai-project/artifacts/
├── completion-notices/
│   ├── 2026-05-30T14-32-00Z__P1-M14-E1.1__completion_notice.md
│   ├── 2026-05-30T14-35-00Z__P1-M14-E1.2__completion_notice.md
│   └── ...
├── review-decisions/
│   ├── 2026-05-30T15-00-00Z__P1-M14-E1.1__review_decision.md
│   └── ...
├── delivery-notices/
│   ├── 2026-05-30T16-00-00Z__P1-M14-E1.1__delivery_notice.md
│   └── ...
└── bugfixes/
    ├── 2026-05-31T09-00-00Z__B1.1__bugfix_postmortem.md
    └── ...
```

All committed to git. CFO can browse history via `git log --all -- .ai-project/artifacts/`.

### Daemon Extensions

**Current (P3):**
- Daemon monitors `.ai-project/queue/` for trigger files (04_epic.json)
- Spawns orchestrator for Epic execution
- Stores results in `.ai-project/` directory

**New (P4):**
- Daemon monitors `.ai-project/artifacts/completion-notices/` for Completion Notice files
- Parses YAML frontmatter to extract epic_id, milestone_id, phase_id
- Routes to parent chat (Milestone Chat or HQ Chat) via trigger mechanism
- Parent chat reads artifact, issues Review Decision, stores in review-decisions/
- Daemon detects Review Decision, routes back to Epic Chat
- Completes the bidirectional workflow

### Integration Points

| Component | Change | Impact |
|-----------|--------|--------|
| **bin/ai-project-daemon** | Extend queue monitoring to include artifacts/ | Non-breaking (new feature) |
| **governance/agents/governance.agent.md** | Add artifact handling rules (parse, validate, route) | Documentation only |
| **Epic Execution Chat Starter** | Add Completion Notice requirement | Already updated |
| **Milestone Chat Starter** | Add Completion Notice handling section | Already updated |
| **HQ Chat Starter** | Add artifact handling (Bugfix creation, Review Decisions) | To be done |

---

## Risk & Mitigation

| Risk | Likelihood | Mitigation |
|------|------------|-----------|
| **Artifact parsing bugs** | Medium | Comprehensive unit tests (E14.3), manual review of artifacts |
| **Race conditions in queue** | Medium | File locking mechanism, atomic writes, idempotent re-processing |
| **4-hour SLA missed** | Medium | Escalation alert to CFO, re-route to Phase Lead if available |
| **Team gets confused by roles** | Medium | Example project (M16), role playbook, clear decision matrix |
| **Daemon path bug blocks submodule users** | High | Fix immediately (E17.1), blocking all team adoption |

---

## Dependencies

### External
- Git (existing)
- Docker (existing)
- Python 3 (existing)

### Internal
- P1-P3 governance fully operational
- Daemon and orchestrator from P3 working
- Artifact templates (P4 design phase, already created)

---

## Timeline & Staffing

### Estimate: 10-14 Epics, 5-7 weeks (solo), 3-4 weeks (2-person team)

**Delivered:**
- M14 (Artifact system): ✅ complete
- M15 (Cleanup and Salvage): ✅ complete
- M16 (Team Collaboration Example & Documentation): ✅ complete
- M17 (Bug Fixes & Polish): ✅ complete
- M18 (Inception Artifacts): ✅ complete

**Remaining:**
- M19 (Creation Chat Completion and Bugfix Workflow) — final P4 milestone: 3-5 days

---

## Reference

### Design Documents (Complete)
- `governance/systems/artifact-communication-protocol.md` (P4.1 design)
- `governance/systems/bugfix-epic-workflow.md` (P4.2 design)
- `governance/systems/roles-authorization-team-governance.md` (P4.3 design)

### Templates (Complete)
- `governance/templates/completion-notice-epic.md`
- `governance/templates/review-decision.md`
- `governance/templates/delivery-notice.md`

### Updated Documents
- `governance/EPIC-EXECUTION-CHAT-STARTER.md` (Completion Notice requirement)
- `governance/systems/milestone-execution-chat-starter.md` (Completion Notice handling)
- `docs/roadmap/overview.md` (P4 scope added)

### Parent Phase Documents
- P1 Spec: `docs/phases/P1__System_Foundation_and_Adoption/P1__phase-spec.md`
- P2 Spec: `docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/P2__phase-spec.md`
- P3 Spec: `docs/phases/P3__Agentic_Execution_Model_Maturity/P3__phase-spec.md`

---

## Next Steps (Execution Phase)

1. **Create Milestone M14 Specs** — detailed Epic specs for E14.1, E14.2, E14.3
2. **Begin M14.E14.1** — artifact parsing & schema validation
3. **Establish daily standup** — sync on artifact parsing design
4. **Plan M15** — bugfix handling once M14 artifacts are flowing

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-05-29 | Phase P4 specification. Design complete (P4.1, P4.2, P4.3). 4 milestones, 6-8 estimated Epics. |
| 1.1.0 | 2026-06-13 | Updated milestone numbering to global M15–M20. Added M16 (Inception Artifacts), M17 (Two-Stage Lifecycle), M18 (Bugfix Workflow). Renamed former M15/M16/M17 to M15/M19/M20 with authoritative names. (E15.1 — Master Cleanup) |
| 1.2.0 | 2026-06-18 | Reconciled executed milestone plan with original spec. M16 and M17 were delivered with different scopes than planned (team example and bug fixes / polish vs. inception artifacts and two-stage lifecycle). M18–M20 renumbered to preserve the undelivered original M16–M18 work: M18 = Inception Artifacts, M19 = Two-Stage Lifecycle, M20 = Bugfix Workflow. Phase continues. |
| 1.3.0 | 2026-06-20 | M19 and M20 consolidated into single final milestone M19 (Creation Chat Completion and Bugfix Workflow). Original M19 Two-Stage Lifecycle diagram deferred. M19 marked as final P4 milestone. |
