# MILESTONE EXECUTION CHAT STARTER — P4-M15: Bugfix Epic Workflow

MANDATORY CONTEXT PACKET

Project: ai-project-system
Phase: P4 — Team Collaboration and Artifact-Driven Communication
Milestone: M15 — Bugfix Epic Implementation
Status: Planning Milestone
Governance: PROJECT-SYSTEM-GUIDELINES.md and AI-OPERATING-GUIDELINES.md enforced
Execution Mode: Milestone planning (produces Epic Execution Chat Starters)
Scope Rule: Create 3 Epic Execution Chat Starters for E15.1, E15.2, E15.3 only.

MILESTONE OVERVIEW

**Goal:** Implement expedited bugfix workflow with production deployment gate, 4-hour SLA for review, and post-mortem generation.

**Deliverables:**
- HQ Chat handler for bugfix issue detection and Epic creation
- Escalation handler for SLA management
- Post-mortem template and automation
- Deployment Authorization artifact support
- Integration with M14 artifact system

**Dependencies:**
- M14 (Artifact System) must be complete and integrated
- Daemon and queue system from P3 (existing)
- Artifact communication protocol (P4.1 design)

**Duration:** 1-2 weeks

EPIC STUBS (3 EPICS)

### E15.1 – Bugfix Epic Creation in HQ Chat

**Status:** Spec Complete (ready to execute)

**Description:** Extend HQ Chat to evaluate production issues and create minimal Bugfix Epic specs with expedited authorization.

**Key Requirements:**
- Detect issue reports in HQ Chat messages
- Evaluate severity (critical, high, medium, low)
- Decide: Bugfix Epic vs. defer to next Phase
- Create minimal Bugfix Epic spec (B#.# format)
- Commit spec to `docs/bugfixes/B#.#__spec__...md`
- Issue Epic Delivery Authorization directly (no Milestone intermediary)
- Assign Bugfix ID and severity level

**Deliverables:**
- HQ Chat Handler for issue detection and evaluation
- Bugfix Epic Creation Logic
- Epic Delivery Authorization template
- Documentation: HQ Agent decision flowchart

**Spec:** `P4-M15-E15.1__spec__Bugfix_Epic_Creation_in_HQ_Chat.md`

---

### E15.2 – Expedited Review SLA & Production Gate

**Status:** Spec Complete (ready to execute)

**Description:** Track Completion Notices from bugfixes, enforce 4-hour SLA for review, and require CFO authorization before production deployment.

**Key Requirements:**
- HQ Agent tracks Completion Notice arrival time
- SLA clock: 4 hours from receipt to Review Decision
- If SLA missed: escalate to CFO with urgency flag
- Require Deployment Authorization artifact before prod deploy
- CFO must explicitly approve/reject production deployment
- No automatic merge-to-production without CFO authorization
- Log all SLA decisions to audit trail

**Deliverables:**
- SLA Tracker class in HQ Agent
- Escalation handler for missed SLAs
- Production Deployment Gate enforcement
- Deployment Authorization artifact support
- SLA monitoring dashboard (optional)

**Spec:** `P4-M15-E15.2__spec__Expedited_Review_SLA_and_Production_Gate.md`

**Depends On:** E15.1 (must identify bugfixes first)

---

### E15.3 – Post-Mortem for Critical/High

**Status:** Spec Complete (ready to execute)

**Description:** Auto-generate post-mortem templates for Critical and High severity bugfixes, require root cause analysis, and commit to audit trail.

**Key Requirements:**
- Detect bugfix completion (Delivery Notice received)
- Check severity level (Critical or High)
- Auto-generate post-mortem template
- Require: root cause analysis, resolution steps, prevention measures
- Store post-mortem in `.ai-project/artifacts/bugfixes/`
- Commit post-mortem to repository for audit trail
- Report post-mortem completion to CFO dashboard

**Deliverables:**
- Post-Mortem Generator class
- Post-Mortem artifact template
- Storage and retrieval logic
- Reporting to CFO dashboard

**Spec:** `P4-M15-E15.3__spec__Post_Mortem_for_Critical_and_High_Bugfixes.md`

**Depends On:** E15.1 (must know severity level)

---

## ACCEPTANCE CRITERIA (MILESTONE LEVEL)

✅ **Bugfix Epic creation works end-to-end:**
- Issue reported to HQ Chat
- Bugfix Epic created (B#.#) with minimal spec
- Epic Delivery Authorization issued directly

✅ **SLA enforcement works:**
- Completion Notice arrival triggers SLA clock
- HQ Agent reviews within 4 hours
- If SLA missed, escalation to CFO

✅ **Production gate works:**
- Deployment Authorization artifact required before prod deploy
- CFO explicitly approves/rejects production deployment
- No automatic deployment without CFO authorization

✅ **Post-mortems generated:**
- Critical/High bugfixes auto-generate post-mortem template
- Post-mortem commits to repository
- CFO can view post-mortem reports

✅ **All artifacts flow through M14 system:**
- Completion Notices, Review Decisions, Delivery Notices use M14 format
- Daemon routes all artifacts correctly
- Manual mode (copy-paste) also works

---

## KEY DECISIONS

1. **Minimal spec vs. full spec:** Bugfix Epics use minimal 2-3 section specs, not full specs. Root cause and solution can be TBD.

2. **Direct parent (HQ vs. Milestone):** Bugfix Epics report directly to HQ Chat, not Milestone Chat. This is expedited path.

3. **4-hour SLA:** Bugfix Completion Notices must receive Review Decision within 4 hours or escalate to CFO. Standard Epics have 24-48 hour reviews.

4. **CFO deployment gate:** ALL production deployments require CFO (Layer-8) authorization. This is non-negotiable.

5. **Post-mortem only for C/H:** Only Critical and High severity bugfixes require post-mortem. Low/Medium are documented but not analyzed.

---

## INTEGRATION WITH M14

M15 Epics depend on M14 completion:
- M14 provides artifact parsing and daemon routing
- M15 uses Completion Notice, Review Decision, Delivery Notice formats from M14
- M15 adds Deployment Authorization artifact (new artifact type)
- M15 also adds Post-Mortem artifact (new artifact type)

M14 and M15 must be integrated before team adoption.

---

## DEPENDENCIES & BLOCKERS

- ✅ M14 (Artifact System) must be complete
- ✅ P4.2 Design (Bugfix Workflow) is complete
- ✅ P4.1 Design (Artifact Communication) is complete
- ✅ HQ Chat Starter exists and can be extended
- ⏳ Daemon path resolution (E17.1) — may need fixing on fresh project init

---

## NEXT STEPS

1. **Accept Milestone M15** — CFO approves milestone scope
2. **Execute E15.1** — Create HQ Chat handler for bugfix creation
3. **Execute E15.2** — Implement SLA enforcement and production gate
4. **Execute E15.3** — Implement post-mortem automation
5. **Integrate with M14** — Ensure artifact flow works end-to-end
6. **Begin M16** — Team collaboration example project

---

## REFERENCE

- **Phase Spec:** `docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4__phase-spec.md`
- **Bugfix Workflow Design:** `governance/systems/bugfix-epic-workflow.md`
- **Artifact Protocol (M14):** `governance/systems/artifact-communication-protocol.md`
- **Roles & Authorization (P4.3):** `governance/systems/roles-authorization-team-governance.md`
- **M14 Milestone Starter:** `docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4-M14__milestone-execution-chat-starter.md`
