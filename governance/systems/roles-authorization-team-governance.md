---
type: system
status: active
effective_date: 2026-09-02
version: 1.2.0
---

# Roles, Authorization & Team Governance (P4.3)

## Purpose

This document defines roles, responsibilities, and authorization boundaries for team-based project execution using the AI Project System.

**Problem Solved:** P1-P3 governance assumed a solo developer (single human + agents). Real teams need role-based access control, delegation of authority, and clear decision boundaries.

**Solution:** Define named roles (CFO, Lead, Contributor, Reviewer, HQ Agent, Milestone Agent, Epic Agent) with explicit authorities and constraints.

**Benefit:**
- Multiple humans can participate without conflicts
- Authority is explicit and delegatable
- Decisions are recorded with decision-maker attribution
- CFO (Layer-8) retains production deployment gate

---

## Core Principle: Layered Authority

The AI Project System uses **layered authority** where decisions are delegated downward, but escalation flows upward:

```
CFO (Layer-8) ← Production Deployment Gate
  ↓
HQ Agent ← Strategic Decisions, Phase Planning
  ↓
Phase Agent ← Milestone Planning & Approval
  ↓
Milestone Agent ← Epic Planning & Acceptance
  ↓
Epic Agent ← Implementation & Delivery
  ↓
Contributors ← Code Implementation
```

**Rule:** Each layer can make decisions independently within its scope, but cannot override decisions from parent layers without documented escalation.

---

## Roles

### 1. CFO (Chief Financial Officer / Layer-8)

**Identity:** You (the human). The single source of strategic authority.

**Responsibilities:**
- ✓ Authorize Phase planning (new projects, budget allocation)
- ✓ Authorize ALL production deployments
- ✓ Escalation review (blocking issues, disputes)
- ✓ Cross-project strategic decisions
- ✓ Team hiring/assignment decisions

**Authority Boundaries:**
- ✓ Can override any decision if justified
- ✓ Can pause/cancel any Phase or Epic
- ✗ Cannot bypass Definition of Done or governance rules
- ✗ Cannot merge PRs directly (must delegate to authorized role)

**Decision Artifacts:**
- Issues **Phase Authorization** (approval to begin Phase planning)
- Issues **Deployment Authorization** (approval for production deployment)
- Issues **Escalation Decision** (resolution to blocked issues)

**Interaction Pattern:**
- Visits HQ Chat for status, decisions, escalations
- Reviews high-level reports and metrics
- Issues 1-2 decisions per project per week (typical)

**Time Commitment:** 30 min - 2 hours per project per week

---

### 2. HQ Agent (Headquarters Agent)

**Identity:** Autonomous agent (acts in HQ Chat mode).

**Responsibilities:**
- ✓ Parse CFO decisions and translate to Phase planning
- ✓ Evaluate Bugfix Epics vs. standard planning
- ✓ Review Completion Notices from Phases
- ✓ Coordinate with Phase Agents
- ✓ Escalate blocking issues to CFO

**Authority Boundaries:**
- ✓ Can approve Phase planning (on CFO authorization)
- ✓ Can create Bugfix Epics (up to SLA)
- ✓ Can reject Phase planning if governance non-compliant
- ✗ Cannot authorize production deployment (CFO only)
- ✗ Cannot override CFO decisions
- ✗ Cannot work on code implementation

**Decision Artifacts:**
- Issues **Phase Completion Notice** (planning complete, ready for CFO review)
- Issues **Phase Review Decision** (exception path only — reject or accept-with-follow-ups; a clean Phase delivery is accepted by an acknowledgment naming the party that reviewed and accepted, PSG §11.6 — silence accepts nothing)
- Issues **Bugfix Epic Approval** (authorization to begin bugfix work)

**Operational Rules:**
- Operates 24/7 in agentic mode (daemon-driven)
- Responds to CFO messages in HQ Chat within 1 hour
- Reviews incoming Completion Notices within 4 hours (SLA)

---

### 3. Phase Lead (Optional, Team Lead Role)

**Identity:** Named human or agent (assigned by CFO).

**Responsibilities:**
- ✓ Own Phase planning and milestone strategy
- ✓ Coordinate milestone priorities and sequencing
- ✓ Act as escalation point for Milestone Agents
- ✓ Report Phase progress to CFO

**Authority Boundaries:**
- ✓ Can delegate Milestone planning to Milestone Agents
- ✓ Can reorder milestones within Phase scope
- ✓ Can escalate milestone blockers to CFO
- ✗ Cannot redefine Phase scope without CFO approval
- ✗ Cannot cancel Phase (CFO only)

**Decision Artifacts:**
- Issues **Phase Strategy Document** (goals, milestones, dependencies)
- Issues **Milestone Priority** (sequencing decision)
- Issues **Escalation Request** (unblocking issue for CFO)

---

### 4. Milestone Agent (Milestone Planning Agent)

**Identity:** Autonomous agent (acts in Milestone mode).

**Responsibilities:**
- ✓ Create Epic stubs from Milestone spec
- ✓ Produce Epic specs and Epic Execution Chat Starters
- ✓ Review Epic Completion Notices
- ✓ Accept clean Epic deliveries by an acknowledgment naming the party that reviewed and accepted; issue a Review Decision only on the exception path (PSG §11.6; silence accepts nothing)
- ✓ Aggregate Epic deliverables into Milestone Completion Notice

**Authority Boundaries:**
- ✓ Can reject Epic Completion Notices if non-compliant
- ✓ Can request rework on incomplete Epics
- ✗ Cannot modify Epic specs without Epic Agent input
- ✗ Cannot approve Phase-level decisions (delegated to Phase Lead/HQ)

**Decision Artifacts:**
- Issues **Epic Review Decision** (exception path only — reject or accept-with-follow-ups; PSG §11.6)
- Issues **Milestone Completion Notice** (all Epics complete)
- Issues **Escalation to Phase** (unresolvable milestone issue)

---

### 5. Epic Agent (Epic Execution Agent)

**Identity:** Autonomous agent (acts in Epic mode, in sandbox).

**Responsibilities:**
- ✓ Receive Epic Delivery Authorization
- ✓ Execute Epic implementation in sandbox
- ✓ Run Dev-QA recursion loop (max 3 attempts)
- ✓ Create Completion Notice when done
- ✓ Merge PR upon parent acceptance — silence on a clean delivery, or an exception-path Review Decision (PSG §11.6)
- ✓ Create Delivery Notice after merge

**Authority Boundaries:**
- ✓ Can implement Epic according to spec
- ✓ Can fail and retry (up to 3 times)
- ✗ Cannot modify Epic spec without escalation
- ✗ Cannot merge PR without parent acceptance — an acknowledgment naming the party that reviewed and accepted for a clean delivery per PSG §11.6 (silence accepts nothing), or an exception-path Review Decision (Accept); a rejected delivery MUST NOT merge
- ✗ Cannot deploy to production

**Decision Artifacts:**
- Issues **Completion Notice** (ready for parent review)
- Issues **Escalation Notice** (max retries exhausted; template `governance/templates/escalation-notice.md`)

---

### 6. Reviewer (Code Review Role)

**Identity:** Named human or agent (optional, assigned per Epic).

**Responsibilities:**
- ✓ Review PR code quality, tests, documentation
- ✓ Approve or request changes before Milestone accept
- ✓ Validate specification compliance
- ✓ Check Definition of Done completeness

**Authority Boundaries:**
- ✓ Can block merge if issues found
- ✓ Can request rework (maps to Epic rejection)
- ✗ Cannot approve merge without Milestone accept
- ✗ Cannot change Epic scope

**Decision Artifacts:**
- Issues **Code Review Comment** (via GitHub PR)
- Issues **Review Blockers** (escalates to Milestone Agent if critical)

---

### 7. Contributors (Implementation Team)

**Identity:** Human developers or agents in Epic Execution Chat.

**Responsibilities:**
- ✓ Implement Epic code according to spec
- ✓ Write tests
- ✓ Create PR with proper description
- ✓ Address code review feedback

**Authority Boundaries:**
- ✓ Can implement according to Epic spec
- ✓ Can ask questions if spec is ambiguous
- ✗ Cannot modify Epic scope
- ✗ Cannot merge PR independently
- ✗ Cannot deploy

**Decision Artifacts:**
- Issues **Code Commits** (implementation work)
- Issues **Pull Requests** (work delivery)

---

## Decision Types & Who Decides

| Decision | CFO | HQ Agent | Phase Lead | Milestone Agent | Epic Agent | Reviewer | Contributor |
|----------|-----|----------|-----------|-----------------|-----------|----------|-------------|
| Phase scope | ✓ | - | ✗ propose | - | - | - | - |
| Phase authorization | ✓ | - | - | - | - | - | - |
| Milestone planning | - | - | ✓ (or HQ) | ✓ | - | - | - |
| Epic spec | - | - | - | ✓ | ✓ feedback | - | - |
| Epic implementation | - | - | - | - | ✓ | ✓ feedback | ✓ |
| Epic acceptance | - | - | - | ✓ | - | ✓ input | - |
| Production deploy | ✓ | - | - | - | - | - | - |
| Bugfix creation | - | ✓ | - | - | - | - | - |
| Escalation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

---

## Authorization: Who Can Do What

### Creating Artifacts

| Artifact | Created By | Authority |
|----------|-----------|-----------|
| Phase Spec | HQ Agent or Phase Lead (on CFO authorization) | HQ authorizes after CFO Phase Authorization |
| Milestone Spec | Milestone Agent (on Phase Lead delegation) | Milestone Agent per Milestone planning |
| Epic Spec | Milestone Agent (with Epic Agent input) | Milestone Agent during planning |
| Epic Execution Chat Starter | Milestone Agent | Milestone Agent issues delivery authorization |
| Completion Notice | Epic/Milestone Agent | Agent issues after work complete |
| Review Decision | Milestone Agent / HQ Agent | Exception path only — parent chat issues when a delivery is not clean (PSG §11.6) |
| Delivery Notice | Epic/Milestone Agent | Agent issues after merge |
| Deployment Authorization | CFO | CFO authorizes production deploy |

### Merging to Branches

| Target Branch | Who Can Merge | Authority |
|---------------|--------------|-----------|
| epic/E#.# | Epic Agent (on parent acceptance) | Milestone Agent — acceptance by an acknowledgment naming the party that reviewed and accepted for a clean delivery (silence accepts nothing), or exception-path Review Decision (PSG §11.6) |
| milestone/M# | Milestone Agent (on Phase approval) | Phase Lead/HQ approved |
| phase/P# | Phase Agent (on CFO approval) | CFO approves Phase delivery |
| develop | Release Agent (on deployment cycle) | Release process |
| master | CFO authorized (hotfix or release) | CFO explicitly authorizes |

### Production Deployments

**RULE:** ALL production deployments require **explicit CFO authorization**.

Process:
1. Delivery is merged to develop/staging
2. Epic/Milestone Agent creates **Deployment Authorization Request**
3. CFO reviews Deployment Authorization Request
4. CFO issues **Deployment Authorization** (approved/rejected)
5. On approval, deployment proceeds
6. On rejection, work is paused with CFO feedback

Example Deployment Authorization Request:
```markdown
---
artifact_type: deployment_authorization_request
episode_id: P1-M2-E2.1
timestamp: 2026-05-30T10:00:00Z
requestor: Epic Agent (P1-M2-E2.1)
target_environment: production
---

# Deployment Authorization Request: P1-M2-E2.1

## What's Deploying
Feature XYZ implementation, fully tested, merged to phase/P1.

## Risks
- None identified. Standard feature, no breaking changes.

## Rollback Plan
- Feature flag disabled to deactivate feature.
- Estimated rollback time: 5 minutes.

## CFO Decision Requested
Approve or reject production deployment.
```

---

## Escalation Path

When a decision cannot be made at the current level, escalate upward:

```
Contributor ← (blocked/unclear)
  ↓ Escalate
Epic Agent ← (spec ambiguous)
  ↓ Escalate
Milestone Agent ← (scope unclear)
  ↓ Escalate
Phase Lead / HQ Agent ← (impacts multiple milestones)
  ↓ Escalate
CFO (Layer-8) ← (strategic decision)
  ↓ Decision
HQ Agent ← (announces decision)
  ↓ Cascade Down
```

**Escalation Rules:**
1. **Document the blocker** — create an Escalation artifact explaining the issue
2. **Request decision** — clearly state what decision is needed
3. **Time SLA** — expect response within:
   - Epic/Contributor escalation: 4 hours
   - Milestone escalation: 8 hours
   - Phase escalation: 24 hours
   - CFO escalation: 2 business days (or URGENT if blocking)
4. **No re-escalation** — once a decision is made, accept it and proceed

---

## Governance Artifact Attribution

Every artifact MUST include **decision-maker attribution**:

```markdown
---
artifact_type: review_decision
issuer_chat: Milestone Agent (P1-M1)
issuer_role: Milestone Agent
decision_maker: Milestone Agent  # Role that made the decision
decision_maker_id: milestone_agent_01  # Optional identifier
timestamp: 2026-05-30T14:32:00Z
---
```

This allows CFO to trace all decisions back to the role (and potentially human/agent identity) that made them.

---

## Team Communication Norms

### Chat Communication

- **Decisions:** Always document in artifacts, not just chat messages
- **Status:** Daily standup in phase/milestone chats (optional but recommended)
- **Escalations:** Use Escalation artifacts, not vague "help needed" messages
- **Disputes:** Escalate to parent chat, never argue in sibling chats

### Chat Starter References

- **HQ Chat Starter:** Used by CFO and HQ Agent; defines Phase planning scope
- **Phase Chat Starter:** (Optional) Used by Phase Lead if delegating
- **Milestone Chat Starter:** Used by Milestone Agent; defines Milestone planning
- **Epic Chat Starter:** Used by Epic Agent; defines Epic execution

### Async-First Workflow

The system is designed for **async-first** work:

1. **CFO** writes decision in HQ Chat (async)
2. **HQ Agent** processes decision, creates Phase planning artifacts (async)
3. **Milestone Agent** reviews Phase artifacts, creates Milestone spec (async)
4. **Epic Agent** executes Epic in sandbox (async, 24/7)
5. **Reviewer** reviews PR when available (async)
6. **Milestone Agent** accepts a clean delivery by an acknowledgment naming the party that reviewed and accepted, or issues an exception-path Review Decision (async; PSG §11.6)

No required real-time meetings. Team can be fully distributed.

---

## Team Size Flexibility

### Solo Developer (Original Model)

```
CFO (you) ← One human
  ↓
HQ Agent ← All planning decisions
  ↓
Epic Agent ← All execution
```

- CFO reviews once per day
- 1-2 decisions per day
- Time commitment: 30 min/day

### Small Team (2-5 developers)

```
CFO (you) ← One human (strategic)
  ↓
HQ Agent ← Phase planning (autonomic or delegated to Lead)
  ↓
Phase Lead ← Milestone coordination (optional human or agent)
  ↓
Milestone Agent ← Planning
  ↓
Epic Agents ← Multiple Epics in parallel
  ↓
Contributors ← Team members on each Epic
```

- CFO reviews 2-3x per week
- 3-5 decisions per week
- Time commitment: 2-4 hours/week

### Larger Team (6-20+ developers)

```
CFO (you) ← Strategic oversight
  ↓
HQ Agent ← Phase planning
  ↓
Phase Leads ← Per-phase coordination (2-3 humans)
  ↓
Milestone Agents ← Multiple milestones in parallel
  ↓
Epic Agents ← Many Epics concurrently
  ↓
Contributors ← Team members assigned per Epic
```

- CFO reviews 1-2x per week
- 2-3 strategic decisions per week
- Phase Leads handle day-to-day
- Time commitment: 2-3 hours/week for CFO

---

## New Team Member Onboarding

When a new contributor joins:

1. **Assign role** — Contributor, Reviewer, or Milestone Lead
2. **Provide role guide** — This document filtered to relevant sections
3. **Assign first Epic** — Start with a small, well-defined Epic
4. **Designate reviewer** — Assign a peer reviewer for first PR
5. **Monitor first cycle** — CFO (or Phase Lead) reviews first Epic delivery
6. **Grant authority** — After successful first Epic, expand role if needed

---

## Conflict Resolution

If two roles dispute a decision:

1. **Escalate to parent role** — dispute goes up the authority chain
2. **Document positions** — both roles explain their stance in artifacts
3. **Parent decides** — parent role makes final call
4. **Accept & continue** — both roles accept parent decision and proceed

**Example:**
- Epic Agent says Epic is done (Completion Notice)
- Milestone Agent rejects (Review Decision: Reject — exception path)
- Epic Agent disputes rejection in Milestone Chat
- **Parent:** Phase Lead or HQ Agent reviews and makes final decision
- **Resolution:** Phase Lead issues binding decision; Epic Agent reworks or accepts

---

## Rules & Constraints

1. **Single CFO Authority** — Only one person is CFO. Authority cannot be delegated away.

2. **No Peer Override** — Two roles at the same level cannot override each other; escalate.

3. **No Self-Authorization** — A role cannot authorize its own decisions (e.g., Epic Agent cannot approve own PR).

4. **Production Gate** — CFO MUST approve all production deployments, no exceptions.

5. **Audit Trail** — All decisions are recorded in artifacts and committed to repository.

6. **Role Clarity** — Each artifact must clearly state the issuer role (HQ Agent, Milestone Agent, Epic Agent, etc.).

7. **Escalation SLA** — Escalations MUST be responded to within the defined SLA or escalate further.

---

## Delegation & Gradual Autonomy

The system supports **gradually increasing autonomy** as the team matures:

**Phase 0 (Manual, Solo):**
- CFO uses manual mode (Chat Starters, copy-paste)
- HQ Agent provides guidance
- Time: weeks 1-4

**Phase 1 (Manual, Team):**
- CFO adds team members
- Phase Lead or human Reviewer joins
- Manual mode continues
- Time: weeks 5-8

**Phase 2 (Agentic, Team):**
- Daemon starts for Epic execution
- HQ Agent, Milestone Agent, Epic Agent all autonomous
- CFO makes fewer decisions
- Phase Lead handles escalations
- Time: weeks 9-12+

**Phase 3 (Full Autonomy):**
- All agents autonomous
- CFO reviews once per week (or less)
- Phase Lead can delegate further
- System is self-governing

---

## Reference

- **Project System Guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md` §13 (Chat Hierarchy)
- **AI Operating Guidelines:** `governance/AI-OPERATING-GUIDELINES.md` §3 (Agent Responsibilities)
- **Artifact Communication Protocol (P4.1):** `governance/systems/artifact-communication-protocol.md`
- **Bugfix Epic Workflow (P4.2):** `governance/systems/bugfix-epic-workflow.md`
- **HQ Chat Starter:** `governance/systems/hq-execution-chat-starter.md`
- **Governance Agent Definition:** `governance/agents/governance.agent.md`

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.2.0 | 2026-09-02 | **Acceptance distinguishable from absence (E43.2, P12-M43).** Every "by silence / silence-accept" statement reconciled to the amended PSG §11.6: acceptance of a clean delivery is by an **acknowledgment naming the party that reviewed and accepted**; **silence accepts nothing**. Amended: the Phase Review Decision artifact line, the Milestone Agent responsibility, the Epic Agent authority boundary, the merge-authority table's epic row, and the async flow step. No role, authority, or gate changed. Backed by `tests/test_acceptance_distinguishable_from_absence.py`. |
| 1.0.0 | 2026-05-29 | Initial release. Defines 7 roles, decision authorities, authorization matrix, team communication norms, and production deployment gate requiring CFO approval. |
| 1.1.0 | 2026-07-03 | Reconciled to default-accept (SN-13, PSG §11.6 / AOG §14): role duties and authorization rules reframed — a clean delivery is accepted by silence; a Review Decision is the exception path. Merge gate "Cannot merge PR without Review Decision (Accept)" reconciled to "without parent acceptance". Artifact and merge tables annotated. (P6-M25-E25.4) |
