---
type: system
status: active
effective_date: 2026-05-29
version: 1.1.0
---

# Bugfix Epic Workflow (P4.2)

## Purpose

This document defines the lightweight workflow for unplanned bugfixes that require rapid response without the full Phase → Milestone → Epic ceremony.

**Problem Solved:** The standard governance model is plan-first (Phase Spec → Milestone Spec → Epic Spec → Execution). A critical production bug cannot wait for planning. We need a direct path to fix.

**Solution:** Bugfix Epic variant with minimal planning ceremony, direct HQ Chat approval, expedited merge path.

**Use Case:** Production incidents, security vulnerabilities, critical regressions that require immediate fix.

---

## When to Use Bugfix Epic

Use Bugfix Epic when:

✓ **Issue is unplanned** — discovered after Phase planning is complete
✓ **Issue is time-sensitive** — production impact, security risk, or critical blocker
✓ **Issue is in-scope** — belongs to current Phase's project
✓ **Issue is actionable** — root cause known or investigation time is bounded
✓ **Fix is localized** — does not require architecture changes or cross-team coordination

Do NOT use Bugfix Epic when:

✗ **Issue is planned** — belongs to a Milestone already in progress (use normal Epic flow)
✗ **Issue requires investigation** — root cause unknown, fix scope unclear (escalate to HQ)
✗ **Issue is out-of-scope** — outside current Phase or requires new planning
✗ **Issue requires review board** — security, compliance, or architectural review needed

---

## Bugfix Epic Structure

A Bugfix Epic is a minimal spec variant with these fields:

```markdown
---
epic_id: B#.#  # Special prefix for Bugfixes
phase_id: <P#>
category: bugfix
severity: critical|high|medium|low
discovered_date: <YYYY-MM-DD>
reported_by: <name or team>
status_url: <incident URL if applicable>
---

# Bugfix Epic B#.# — <Brief Issue Title>

## Problem Description

<Clear, concise problem statement (2-3 sentences)>

## Impact

- **Severity:** Critical | High | Medium | Low
- **Affected Component:** <component or feature>
- **Affected Users:** <who is impacted>
- **Business Impact:** <time, revenue, reputation impact if applicable>

## Root Cause

<Root cause analysis, or "Unknown — investigation required">

## Proposed Solution

<Specific fix approach, or "To be determined by developer">

## Definition of Done

- [ ] Root cause identified (if not already known)
- [ ] Fix implemented
- [ ] Tests added or updated
- [ ] No regressions introduced (QA validation)
- [ ] PR merged to production/hotfix branch
- [ ] Deployment complete
- [ ] Monitoring confirmed (if applicable)

## Acceptance Criteria

<Specific acceptance criteria for fix validation>

Example:
- Endpoint returns correct status code
- Error logs stop appearing
- Performance metric returns to baseline
- Feature flags disabled/enabled as expected
```

---

## Bugfix Epic Workflow

```
Production Issue Discovered
  ↓
HQ Chat evaluates issue
  ↓
Decision: Bugfix Epic or Standard Planning?
  ↓
[If Bugfix Epic]
  ↓
HQ Chat creates minimal Bugfix Epic spec
  ↓
HQ Chat issues Epic Delivery Authorization (direct)
  ↓
Epic Execution Chat opens with Bugfix spec
  ↓
Developer implements fix
  ↓
QA validates (same 3-attempt loop as normal Epic)
  ↓
Epic produces Completion Notice
  ↓
HQ Chat reviews (expedited, within 2-4 hours)
  ↓
HQ Chat issues Review Decision (Accept)
  ↓
Epic proceeds to merge to hotfix or production branch
  ↓
Delivery Notice issued
  ↓
HQ Chat acknowledges and closes Bugfix Epic
```

---

## Key Differences from Standard Epic

| Aspect | Standard Epic | Bugfix Epic |
|--------|--------------|-----------|
| **Planning ceremony** | Phase → Milestone → Epic | Direct to HQ Chat |
| **Spec length** | Full specification | Minimal spec (2-3 sections) |
| **Parent review** | Milestone Chat (planning), Phase Chat (acceptance) | HQ Chat (direct) |
| **Branch strategy** | `epic/E#.#` → `milestone/M#` → `phase/P#` | `bugfix/B#.#` → `hotfix` or `master` |
| **Merge authority** | Milestone + Phase approval | HQ approval (expedited) |
| **Dev-QA loop** | 3 attempts | 3 attempts (same rules) |
| **Time to resolution** | Days (planned) | Hours (urgent) |
| **Documentation** | Full epic spec + implementation docs | Minimal spec + implementation notes |
| **Production gate** | Phase merge to production (normal release cycle) | **HQ explicitly authorizes production merge** |

---

## Bugfix Epic ID Scheme

Bugfix Epics use a special ID format: **B#.#** (instead of E#.#)

- **B** = Bugfix (distinguishes from planned Epics)
- **First #** = Phase number (e.g., B2.3 = Bugfix in Phase 2)
- **Second #** = Sequential bugfix counter within phase

Example:
- B1.1 — First bugfix in Phase P1
- B1.2 — Second bugfix in Phase P1
- B2.1 — First bugfix in Phase P2

---

## Creating a Bugfix Epic

### HQ Chat Workflow

**When to create:**
1. Production issue reported to HQ Chat
2. HQ Agent evaluates severity and scope
3. Decision: "This is a Bugfix Epic"

**What to do:**
1. Create minimal Bugfix Epic spec (2-3 sections, template below)
2. Commit spec to repository: `docs/bugfixes/B#.#__spec__Brief_Title.md`
3. Issue Epic Delivery Authorization (direct to developer or Epic Chat)
4. Assign Epic ID (B#.#) and severity

### Bugfix Epic Spec Template

```markdown
---
epic_id: B#.#
phase_id: <P#>
category: bugfix
severity: critical|high|medium|low
discovered_date: <YYYY-MM-DD>
status: open
---

# Bugfix Epic B#.# — <Brief Issue Title>

## Problem
<What is broken? 2-3 sentences max>

## Impact
- Severity: <Critical|High|Medium|Low>
- Affected: <component or feature>

## Root Cause
<Why did it break? Or "TBD — investigate">

## Fix
<How to fix it? Or "TBD — implement during execution">

## Definition of Done
- [ ] Root cause identified
- [ ] Fix implemented and tested
- [ ] No regressions
- [ ] Merged and deployed
```

### Expedited Review Process

**Normal Epic:** 24-48 hours for review
**Bugfix Epic:** 2-4 hours for review (SLA)

HQ Chat MUST review Completion Notice within 4 hours of receipt. If unable to decide within 4 hours, escalate decision to product/engineering leadership.

See [SLA Tracking and Escalation](#sla-tracking-and-escalation) below for the precise
measurement and escalation rules.

---

## SLA Tracking and Escalation

The Bugfix Epic review SLA is a **4-hour window**, measured precisely as follows:

- **Clock start:** the `timestamp` recorded in the **Completion Notice** artifact when the
  Coding Agent signals the fix is ready for review. The clock measures HQ's review
  latency, *not* the developer's fix time.
- **Clock target:** HQ Chat issues a Review Decision (Accept or Reject) within 4 hours of
  that timestamp.
- **Tracking:** the SLA due time is recorded in the Open Bugfixes dashboard (`SLA Due`
  column) so its status is visible at a glance.

### On SLA Miss

If HQ Chat has not issued a Review Decision within the 4-hour window:

1. **HQ Chat issues an urgent flag to the CFO** — the bugfix is surfaced as overdue, with
   its current state and the reason review is blocked.
2. **The review is still required** — a missed SLA never permits skipping review or
   self-merging. Escalation expedites a decision; it does not waive one.
3. **The production gate still holds** — deployment continues to require a CFO
   [Deployment Authorization](../templates/deployment-authorization.md). Urgency never
   waives the gate.

### Deployment Authorization Is Mandatory

**Every Bugfix Epic that touches production requires a CFO Deployment Authorization**
before the production push — see the [Production Deployment Gate](#production-deployment-gate)
section and the canonical
[Deployment Authorization template](../templates/deployment-authorization.md). This holds
on the expedited path exactly as it does for a normal Epic; the bugfix workflow shortens
*review*, never the *production gate*.

---

## Merge Strategy

### Branching

- **Standard:** `bugfix/B#.#` (from `develop` or `master`)
- **Hotfix:** `hotfix/B#.#` (from `master` if production emergency)

### Merge Target

- **Normal cases:** Merge to `develop`, then coordinate with next Phase merge
- **Production emergencies:** Merge to `master` (hotfix), then backport to `develop`
- **Critical security:** Direct to `master` with post-merge verification

### Production Deployment Gate

**IMPORTANT:** All production deployments MUST be authorized by Layer-8 (CFO).

The CFO produces a **Deployment Authorization** artifact using the canonical
[Deployment Authorization template](../templates/deployment-authorization.md) (the HQ
Agent may prepare it but cannot self-authorize production). Minimal inline form:

```markdown
---
artifact_type: deployment_authorization
bugfix_id: B#.#
timestamp: <ISO-8601 UTC>
issuer: HQ Agent
decision: approved|rejected
target_environment: production|staging|dev
---

# Deployment Authorization: B#.#

## Approved for: <environment>
## Reason: <brief justification>
## Rollback Plan: <if applicable>
```

---

## Communication Path

### Reporting a Potential Bugfix

Any team member can report a potential bugfix to the HQ Chat:

```
**HQ Chat Message**

🔴 **Potential Bugfix**
- Title: <issue title>
- Severity: <critical|high|medium|low>
- Status Page: <link if applicable>
- Reported by: <name>
- Scope estimate: <1-2 hours | half-day | full-day | unknown>

Action needed: Evaluate and decide on Bugfix Epic.
```

### HQ Response

HQ Agent responds with one of:

**Option 1: Approve Bugfix Epic**
```
✓ **Bugfix Epic Approved**
- Epic ID: B#.#
- Severity: <Critical|High|Medium|Low>
- Spec created: docs/bugfixes/B#.#__spec__...md
- Developer assigned: <name>
- SLA: Review by <time>

Proceed with Epic Execution Chat.
```

**Option 2: Defer to Next Phase**
```
⏱ **Deferring to Next Phase**
This issue is not critical enough for expedited bugfix workflow. Will be planned in next Phase.
- Tracked as: <issue tracker reference>
```

**Option 3: Escalate**
```
⚠ **Escalating for Decision**
This issue requires leadership review:
- Security impact assessment needed
- Architectural review required
- Customer impact analysis pending

Action: Escalate to <committee or individual>.
```

---

## Bugfix Epic Execution

Bugfix Epic Execution Chats follow the same Dev-QA loop as standard Epics:

1. **Receive Epic Delivery Authorization** from HQ Chat
2. **Create working branch:** `bugfix/B#.#`
3. **Implement fix** based on Bugfix Epic spec
4. **Run tests** (3-attempt validation loop)
5. **Create PR** against target branch
6. **Produce Completion Notice** (same artifact as standard Epic)
7. **Receive Review Decision** from HQ Chat
8. **Merge PR** upon acceptance
9. **Produce Delivery Notice**
10. **Close Epic Chat**

**Key difference:** All parent approval comes from HQ Chat, not Milestone Chat.

---

## Tracking & Reporting

### Bugfix Dashboard

HQ Chat should maintain visibility of open bugfixes:

```markdown
# Open Bugfixes (Phase P#)

| Epic ID | Title | Severity | Status | SLA Due |
|---------|-------|----------|--------|---------|
| B#.# | ... | Critical | In Progress | 2026-05-30 08:00 UTC |
| B#.# | ... | High | Review | 2026-05-30 14:00 UTC |
| ... | ... | ... | ... | ... |
```

### Post-Mortem (Critical/High Only)

For **Critical and High** severity bugfixes, produce a post-mortem using the canonical
[Post-Mortem template](../templates/post-mortem.md). It is **required** for Critical/High
and **optional** for Medium/Low. A Critical/High Bugfix Epic does not close until its
post-mortem is committed.

The template covers Incident Summary, Timeline, Root Cause, Resolution, Prevention, and
Action Items (with owners and due dates), and carries this front-matter:

```yaml
---
type: post-mortem
epic: <B#.#>
severity: <critical | high>
incident_date: <YYYY-MM-DD>
resolved_date: <YYYY-MM-DD>
authored_by: <role>
---
```

---

## Rules & Constraints

1. **Phase Scoping:** Bugfix Epics MUST belong to the current Phase (or most recent open Phase). Cross-Phase bugfixes require escalation.

2. **Definition of Done:** Bugfix Epics MUST satisfy the same Definition of Done as standard Epics (tests, code review, documentation).

3. **No Scope Expansion:** Bugfix Epics address the specific issue only. If fix uncovers related issues, create separate bugfixes.

4. **Production Authorization:** ALL production deployments require explicit Layer-8 (CFO) approval via Deployment Authorization artifact.

5. **SLA Compliance:** HQ Chat MUST review Completion Notices within 4 hours (SLA). If SLA missed, escalate to leadership.

6. **Backport Requirement:** If merged to hotfix/master, MUST be backported to develop branch to prevent regression.

7. **Audit Trail:** All bugfixes are recorded in `.ai-project/artifacts/bugfixes/` for CFO and audit trail.

---

## Reference

- **Bugfix Epic specs location:** `docs/bugfixes/` (see [`docs/bugfixes/README.md`](../../docs/bugfixes/README.md) for the B#.# naming convention)
- **Deployment Authorization template:** [`governance/templates/deployment-authorization.md`](../templates/deployment-authorization.md)
- **Post-Mortem template:** [`governance/templates/post-mortem.md`](../templates/post-mortem.md)
- **Artifact Protocol (P4.1):** `governance/systems/artifact-communication-protocol.md`
- **Epic Execution Chat Starter:** `governance/EPIC-EXECUTION-CHAT-STARTER.md`
- **HQ Chat Starter:** `governance/systems/hq-execution-chat-starter.md`
- **Production Deployment Guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md` §6 (Authorization & Approval)
- **AI Operating Guidelines:** `governance/AI-OPERATING-GUIDELINES.md`

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-05-29 | Initial release. Defines lightweight Bugfix Epic workflow for unplanned, time-sensitive issues. Includes minimal spec template, expedited review SLA, and production deployment gate requiring CFO authorization. |
| 1.1.0 | 2026-06-20 | Added the SLA Tracking and Escalation section (4-hour window measured from the Completion Notice timestamp; miss → urgent flag to CFO, review never skipped). Referenced the canonical Deployment Authorization and Post-Mortem templates, and the `docs/bugfixes/` location. (P4-M19-E19.1) |
