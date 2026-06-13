# Taskflow — Team Setup

This document defines the roles, team members, and decision authorities for the Taskflow project (Phase P1).

---

## Team Composition

| Role | Person | Email | Decision Authority |
|------|--------|-------|-------------------|
| **CFO** | Morgan Chen | morgan@taskflow-example.com | Phase scope, production deployment authorization, budget |
| **Phase Lead** | Alex Rivera | alex@taskflow-example.com | Milestone planning, Epic acceptance, Review Decisions |
| **Developer 1** | Jamie Park | jamie@taskflow-example.com | E1.1, E1.2, E2.1, E2.3 implementation |
| **Developer 2** | Sam Torres | sam@taskflow-example.com | E1.3, E2.2, E3.1, E3.2 implementation |
| **Reviewer** | Casey Kim | casey@taskflow-example.com | Code review approval, Definition of Done gate |

> **Note:** All team member names and emails are fictional and used for illustration purposes only.

---

## Role Definitions and Decision Authorities

### CFO — Morgan Chen

**Strategic authority:** Highest decision-maker for the Taskflow project.

**Can decide:**
- ✓ Authorize new Phases (scope, budget, timeline)
- ✓ Authorize production deployments (required for any deploy to production)
- ✓ Override any decision if justified with documented rationale
- ✓ Pause or cancel any Phase or Epic
- ✓ Assign or reassign team members

**Cannot decide:**
- ✗ Bypass Definition of Done or governance rules
- ✗ Merge PRs directly (must delegate to Phase Lead)

**How CFO participates:**
- Reviews HQ Chat weekly (or as needed for escalations)
- Issues Phase Authorization before Phase P1 begins
- Issues Production Deployment Authorization before production launch
- Time commitment: ~2 hours/week

---

### Phase Lead — Alex Rivera

**Tactical authority:** Owns Phase P1 planning and Milestone coordination.

**Can decide:**
- ✓ Accept or reject Epic Completion Notices (issues Review Decisions)
- ✓ Reorder Milestones and Epics within Phase P1 scope
- ✓ Delegate Epic review to Reviewer (Casey Kim) for technical assessment
- ✓ Escalate blockers to CFO (Morgan Chen)

**Cannot decide:**
- ✗ Change Phase P1 scope without CFO approval
- ✗ Authorize production deployment (CFO only)
- ✗ Cancel Phase P1 (CFO only)

**How Phase Lead participates:**
- Opens Milestone Chat for M1, M2, M3
- Reviews Epic Completion Notices within 24 hours
- Issues Review Decision artifacts (Accept or Reject)
- Produces Milestone Completion Notices when all Epics close

---

### Developer 1 — Jamie Park

**Implementation authority:** Executes assigned Epics end-to-end.

**Assigned Epics:**
- E1.1 — User Authentication (M1)
- E1.2 — Task CRUD API (M1)
- E2.1 — Login UI (M2)
- E2.3 — Search and Filter (M2)

**Can decide:**
- ✓ Implementation approach within Epic spec
- ✓ Ask questions if spec is ambiguous (escalate to Phase Lead)
- ✓ Create PR and request review

**Cannot decide:**
- ✗ Change Epic scope
- ✗ Merge PR without Review Decision (Accept)
- ✗ Deploy to any environment

---

### Developer 2 — Sam Torres

**Implementation authority:** Executes assigned Epics end-to-end.

**Assigned Epics:**
- E1.3 — Database Schema (M1)
- E2.2 — Task Dashboard (M2)
- E3.1 — Performance Optimization (M3)
- E3.2 — CI/CD Pipeline (M3)

**Can decide:**
- ✓ Implementation approach within Epic spec
- ✓ Schema design decisions (within E1.3 spec constraints)
- ✓ Create PR and request review

**Cannot decide:**
- ✗ Change Epic scope
- ✗ Merge PR without Review Decision (Accept)

---

### Reviewer — Casey Kim

**Quality gate authority:** Reviews all PRs before Phase Lead issues a Review Decision.

**Review scope covers all Epics in P1.**

**Can decide:**
- ✓ Block a PR merge if code review issues are unresolved
- ✓ Approve PR code quality (required before Phase Lead issues Accept)
- ✓ Escalate critical issues to Phase Lead as Review Blockers

**Cannot decide:**
- ✗ Issue Review Decision artifacts (Phase Lead does this)
- ✗ Change Epic scope
- ✗ Authorize merge independently

---

## Decision Flow Summary

```
Production Deploy Request
  → CFO (Morgan Chen) — Authorization Required

Phase P1 Scope Change
  → CFO (Morgan Chen) — Approval Required

Epic Completion Notice (from Developer)
  → Reviewer (Casey Kim) — Code Review
  → Phase Lead (Alex Rivera) — Review Decision (Accept/Reject)

Bugfix Epic Creation (B1.1)
  → HQ Agent — Expedited Approval (within 4 hours)
  → Developer assigned by Phase Lead
```

---

## Escalation Path

```
Developer (Jamie Park / Sam Torres)
  ↓ (blocked, spec unclear)
Phase Lead (Alex Rivera)
  ↓ (scope dispute, milestone blocker)
CFO (Morgan Chen)
  ↓ (strategic decision)
```

When escalating:
1. Document the blocker in a message or artifact
2. State what decision is needed
3. Tag the next role in the escalation path
4. Expect response within 4 hours (Developers → Phase Lead) or 2 business days (Phase Lead → CFO)

---

## Artifact Responsibility

| Artifact | Produced By |
|----------|-------------|
| Epic Completion Notice | Developer (after implementation + tests passing) |
| Review Decision (Accept/Reject) | Phase Lead (Alex Rivera) |
| Delivery Notice | Developer (after PR merge) |
| Milestone Completion Notice | Phase Lead (Alex Rivera) |
| Phase Completion Notice | Phase Lead (Alex Rivera) |
| Production Deployment Authorization | CFO (Morgan Chen) |

---

## First Epic Guidance for New Team Members

If this is your first Epic on Taskflow:
1. Read the Epic spec completely before writing any code
2. Ask Phase Lead (Alex Rivera) if anything is unclear — don't guess
3. Tag Casey Kim for PR review as soon as the PR is open
4. Produce a Completion Notice using the template in `governance/systems/artifact-communication-protocol.md`
5. Your first Epic will be reviewed more carefully — this is normal

---

## Reference

- [AI Project System Governance](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md)
- [Roles and Authorization Guide](https://github.com/panchew/ai-project-system/blob/master/governance/systems/roles-authorization-team-governance.md)
- [Artifact Communication Protocol](https://github.com/panchew/ai-project-system/blob/master/governance/systems/artifact-communication-protocol.md)
