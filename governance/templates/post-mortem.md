---
type: template
status: active
last_updated: 2026-06-20
---

# Post-Mortem Template

A **Post-Mortem** is the blameless incident analysis produced after a Bugfix Epic
resolves a **Critical or High** severity production issue. It records what happened, why,
how it was fixed, and what changes prevent recurrence. It is **required for Critical and
High** severity bugfixes and **optional for Medium and Low**.

Used by: **Coding Agent / on-call author** (author) → **HQ Chat & CFO** (audience).
Related artifacts: [Deployment Authorization](deployment-authorization.md),
[Delivery Notice](delivery-notice.md). Workflow:
[`../systems/bugfix-epic-workflow.md`](../systems/bugfix-epic-workflow.md).

---

## Artifact Schema

```yaml
---
type: post-mortem
epic: <B#.#>                     # the Bugfix Epic this post-mortem covers
severity: <critical | high>      # post-mortems are required for these only
incident_date: <YYYY-MM-DD>     # when the incident began / was discovered
resolved_date: <YYYY-MM-DD>     # when the fix was deployed and confirmed
authored_by: <role>              # role of the author, e.g., "Coding Agent (B1.1)"
---
```

| Field | Required | Notes |
|-------|----------|-------|
| `type` | yes | Always `post-mortem` |
| `epic` | yes | The Bugfix Epic ID (`B#.#`) |
| `severity` | yes | `critical` or `high` |
| `incident_date` | yes | ISO date the incident began or was discovered |
| `resolved_date` | yes | ISO date the fix was deployed and confirmed |
| `authored_by` | yes | Role of the author |

---

## Body Sections

```markdown
# Post-Mortem: <B#.#> — <Incident Title>

## Incident Summary
<One paragraph: what happened, when, and the impact (users affected, duration, data or
revenue impact).>

## Timeline
<Ordered list of key events with timestamps (UTC). Discovery → diagnosis → fix → deploy
→ confirmation.>

## Root Cause
<The actual underlying cause — not just the symptom. What allowed the defect to reach
production?>

## Resolution
<What fixed it: the change made, the commit/tag, and how the fix was verified.>

## Prevention
<Concrete changes that prevent recurrence — tests, guardrails, monitoring, process
changes.>

## Action Items
<Numbered list. Each item has an owner and a due date.>
```

---

## Filled Example

```markdown
---
type: post-mortem
epic: B1.1
severity: critical
incident_date: 2026-06-20
resolved_date: 2026-06-20
authored_by: Coding Agent (B1.1)
---

# Post-Mortem: B1.1 — Auth Session Expiry

## Incident Summary
On 2026-06-20, authenticated users were logged out roughly 60 seconds after signing in
instead of after the intended 24 hours. The defect affected 100% of active sessions for
approximately 3 hours 40 minutes (08:05–11:45 UTC) before the hotfix was deployed. No data
was lost; the impact was loss of access and a spike in re-authentication load.

## Timeline
1. **08:05 UTC** — First user reports of immediate logout; support escalates to HQ Chat.
2. **08:20 UTC** — HQ evaluates: unplanned, production-affecting, urgent → Bugfix Epic
   B1.1 (Critical) created and committed to `docs/bugfixes/`.
3. **08:30 UTC** — Coding Agent reproduces; isolates the session-TTL calculation.
4. **09:10 UTC** — Root cause found: TTL computed in seconds but compared against a
   millisecond timestamp.
5. **09:40 UTC** — Fix implemented on `bugfix/B1.1` with a regression test; tests green.
6. **10:15 UTC** — Completion Notice issued; HQ reviews within the 4-hour SLA and accepts.
7. **10:30 UTC** — CFO Deployment Authorization issued (commit `9f3c1ab`).
8. **11:45 UTC** — Hotfix deployed to production; sessions confirmed stable for the full
   TTL. Incident resolved.

## Root Cause
The session-expiry check compared a TTL expressed in **seconds** (`86400`) against a
timestamp in **milliseconds**, so every session appeared expired after ~86 seconds. The
unit mismatch was introduced in a refactor that changed the clock source without updating
the TTL constant, and no test pinned the actual expiry duration.

## Resolution
Commit `9f3c1ab` (tag `hotfix-B1.1`) normalizes both sides of the comparison to
milliseconds and adds a regression test asserting a 24-hour effective TTL. Verified in QA
and by post-deploy monitoring of the auth error rate.

## Prevention
- Regression test pins the 24-hour session TTL so the unit mismatch cannot recur silently.
- Added a lint rule flagging mixed second/millisecond arithmetic on timestamp values.
- Added an alert on abnormal re-authentication rate to shorten time-to-detection.

## Action Items
1. Backport `9f3c1ab` to `develop`. — Owner: Coding Agent — Due: 2026-06-21
2. Audit other TTL/timeout calculations for unit consistency. — Owner: Phase Lead — Due: 2026-06-27
3. Add the re-auth-rate alert to the standard service dashboard. — Owner: Reviewer — Due: 2026-06-24
```

---

## Notes

- Post-mortems are **blameless**: they analyze systems and process, not individuals.
- Required for **Critical (`B1.x`)** and **High (`B2.x`)** bugfixes; optional for Medium
  and Low. A Critical/High Bugfix Epic does not close until its post-mortem is committed.
- Commit alongside the bugfix audit trail under `.ai-project/artifacts/bugfixes/` (or
  `docs/bugfixes/`), so the CFO can review it via git history.
</content>
