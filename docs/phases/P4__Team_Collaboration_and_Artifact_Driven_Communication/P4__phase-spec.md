---
phase: P4
name: Team Collaboration and Artifact-Driven Communication
status: active
start_date: 2026-05-29
planned_end_date: 2026-07-31
version: 1.0.0
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

### M1: Artifact System Implementation (2-3 Epics)

**Goal:** Implement artifact parsing, routing, and integration in daemon and agents.

**Epics:**
- **E1.1 – Artifact Parsing & Schema Validation**
  - Parse YAML frontmatter from Completion Notice files
  - Validate artifact schema (required fields, types, references)
  - Route artifacts to correct parent chat based on epic_id/milestone_id
  - Test on all three artifact types (Completion Notice, Review Decision, Delivery Notice)

- **E1.2 – Daemon Queue Integration**
  - Extend daemon to detect Completion Notice files in `.ai-project/artifacts/completion-notices/`
  - Route to parent Milestone Chat or HQ Chat
  - Detect Review Decision files, route back to Epic Chat
  - Detect Delivery Notice files, route to parent for acknowledgment
  - Handle race conditions (file written while being read)

- **E1.3 – Integration Tests**
  - Test end-to-end: Epic completes → Completion Notice → Milestone reviews → Review Decision → Epic merges → Delivery Notice
  - Test rework cycle: Rejection → Epic reworks → new Completion Notice (v1.1) → Review Decision Accept
  - Test escalation: Milestone cannot decide → escalate to Phase/HQ
  - Test manual mode: copy-paste artifacts between chats works alongside agentic mode

---

### M2: Bugfix Epic Implementation (2-3 Epics)

**Goal:** Implement bugfix workflow with expedited SLA and production gate.

**Epics:**
- **E2.1 – Bugfix Epic Creation in HQ Chat**
  - HQ Agent detects issue report in HQ Chat
  - Decision: "Bugfix Epic" vs "Defer to next Phase"
  - Create minimal Bugfix Epic spec (B#.#)
  - Commit spec and issue Epic Delivery Authorization
  - Assign Bugfix ID and severity level

- **E2.2 – Expedited Review SLA & Production Gate**
  - HQ Agent tracks Completion Notice arrival time (SLA clock starts)
  - 4-hour SLA timer: review and issue Review Decision
  - If SLA missed, escalate to CFO (urgency indicator)
  - Require Deployment Authorization artifact before prod deploy
  - CFO explicitly approves/rejects production deployment

- **E2.3 – Post-Mortem for Critical/High**
  - Auto-generate post-mortem template on Bugfix Epic completion
  - Require root cause analysis, resolution, prevention steps
  - Commit post-mortem to `docs/bugfixes/` for audit trail
  - Report Critical/High to CFO dashboard

---

### M3: Team Collaboration Example (1-2 Epics)

**Goal:** Create and document a real-world 3-person team scenario with concurrent Epics.

**Epics:**
- **E3.1 – Example Project Setup & Walkthrough**
  - Create example project: `examples/team-project-example/`
  - Phase P1 with 3 Milestones
  - Each Milestone has 2-3 Epics
  - Assign roles: CFO, Phase Lead, 2 Contributors, 1 Reviewer
  - Document decision flow: who decides what
  - Show how artifacts flow between chats

- **E3.2 – Team Collaboration Documentation**
  - Create "Team Onboarding Guide" (role assignment, authority matrix, when-to-escalate)
  - Create "CFO Quick Start" (1-3 decisions per week, reviewing Completion Notices)
  - Create "Contributor Guide" (implement Epic, ask if blocked, await Review Decision)
  - Create "Example Run-Through" (walkthrough one full Epic from start to delivery)

---

### M4: Bug Fixes & Polish (1-2 Epics)

**Goal:** Fix known issues, polish documentation, prepare for team adoption.

**Epics:**
- **E4.1 – Fix Daemon Orchestrator Path Resolution**
  - Issue: v2.0.0 submodules don't have orchestrator binary
  - Solution: Make daemon search in `governance/bin/` as fallback
  - Or: Update submodule version to v3.0.0+ (includes orchestrator)
  - Test on fresh submodule checkout

- **E4.2 – Update Starters & Documentation**
  - Update HQ Chat Starter to reference artifact system
  - Update Milestone Chat Starter to reference bugfix handling
  - Create "CFO Dashboard" view (aggregated progress from multiple projects)
  - Polish all P4 governance documents

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
│   ├── 2026-05-30T14-32-00Z__P1-M1-E1.1__completion_notice.md
│   ├── 2026-05-30T14-35-00Z__P1-M1-E1.2__completion_notice.md
│   └── ...
├── review-decisions/
│   ├── 2026-05-30T15-00-00Z__P1-M1-E1.1__review_decision.md
│   └── ...
├── delivery-notices/
│   ├── 2026-05-30T16-00-00Z__P1-M1-E1.1__delivery_notice.md
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
| **Artifact parsing bugs** | Medium | Comprehensive unit tests (E1.3), manual review of artifacts |
| **Race conditions in queue** | Medium | File locking mechanism, atomic writes, idempotent re-processing |
| **4-hour SLA missed** | Medium | Escalation alert to CFO, re-route to Phase Lead if available |
| **Team gets confused by roles** | Medium | Example project (M3), role playbook, clear decision matrix |
| **Daemon path bug blocks submodule users** | High | Fix immediately (E4.1), blocking all team adoption |

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

### Estimate: 6-8 Epics, 3-4 weeks (solo), 2-3 weeks (2-person team)

**Solo Developer Path:**
- M1 (Artifact system): 2-3 weeks
- M2 (Bugfix workflow): 1-2 weeks
- M3 (Team example): 3-5 days
- M4 (Polish & bug fixes): 2-3 days
- **Total: 4-5 weeks**

**Team Path (2-3 people):**
- M1: 1.5 weeks (parallel work on E1.1 & E1.2)
- M2: 1 week (E2.1 & E2.2 in parallel)
- M3: 3 days (E3.1 & E3.2 in parallel)
- M4: 2 days (E4.1 & E4.2 in parallel)
- **Total: 2-3 weeks**

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

1. **Create Milestone M1 Specs** — detailed Epic specs for E1.1, E1.2, E1.3
2. **Begin M1.E1.1** — artifact parsing & schema validation
3. **Establish daily standup** — sync on artifact parsing design
4. **Plan M2** — bugfix handling once M1 artifacts are flowing

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-05-29 | Phase P4 specification. Design complete (P4.1, P4.2, P4.3). 4 milestones, 6-8 estimated Epics. |
