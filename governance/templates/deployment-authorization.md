---
type: template
status: active
last_updated: 2026-06-20
---

# Deployment Authorization Template

A **Deployment Authorization** is the artifact that records the CFO's explicit approval
(or rejection) to deploy an accepted Epic or Bugfix Epic to a target environment. It is
the production gate's paper trail: **no code reaches production without one**, and a
deployment approved only in chat did not happen.

Used by: **CFO** (issuer, via HQ Chat) → **Coding Agent / release operator** (recipient).
Related artifacts: [Delivery Notice](delivery-notice.md) (must precede a production
authorization), [Post-Mortem](post-mortem.md) (follows a Critical/High bugfix deploy).

> The Deployment Authorization is a **governance artifact, not a CI/CD gate**. It proves
> the CFO approved the deploy; enforcement is cultural, not automated. See
> [`../systems/bugfix-epic-workflow.md`](../systems/bugfix-epic-workflow.md) and the
> [HQ Chat Production Deployment Gate](../systems/hq-execution-chat-starter.md#production-deployment-gate).

---

## Artifact Schema

```yaml
---
type: deployment-authorization
epic: <B#.# or P#-M#-E#.#>      # the Bugfix Epic or planned Epic being deployed
project: <project-slug>          # kebab-case project identifier
issued_by: <role name>           # the authorizing role, e.g., "CFO"
date: <YYYY-MM-DD>               # ISO date the authorization is issued
environment: <production | staging>
decision: <authorized | rejected>
---
```

| Field | Required | Notes |
|-------|----------|-------|
| `type` | yes | Always `deployment-authorization` |
| `epic` | yes | Bugfix Epic (`B#.#`) or planned Epic (`P#-M#-E#.#`) being deployed |
| `project` | yes | Project slug (kebab-case) |
| `issued_by` | yes | Authorizing role — only the **CFO** may authorize production |
| `date` | yes | ISO date the decision is issued |
| `environment` | yes | `production` or `staging` |
| `decision` | yes | `authorized` or `rejected` |

---

## Body Sections

```markdown
# Deployment Authorization: <epic> — <brief title>

## What Is Being Deployed
<The commit SHA or release tag, and a one-line description of the change. Reference the
accepting Review Decision / Delivery Notice that makes this deployable.>

## Risk Assessment
<Brief: what could go wrong, blast radius, and how each risk was mitigated. State the
rollback path.>

## Authorization Statement
<For `authorized`: an explicit statement that the named role authorizes deployment of the
named build to the named environment. For `rejected`: the reason and what must change
before re-submission.>

## Conditions
<Any conditions attached to the authorization — e.g., "deploy only during the
maintenance window", "monitor error rate for 30 minutes", "backport to develop after".
If none, state "None.">
```

---

## Filled Example

```markdown
---
type: deployment-authorization
epic: B1.1
project: ai-project-system
issued_by: CFO
date: 2026-06-20
environment: production
decision: authorized
---

# Deployment Authorization: B1.1 — Auth Session Expiry Hotfix

## What Is Being Deployed
Commit `9f3c1ab` (tag `hotfix-B1.1`): corrects the session-token TTL calculation that
was logging users out after 60 seconds instead of 24 hours. Follows the accepting Review
Decision dated 2026-06-20 and the Delivery Notice for the `bugfix/B1.1` merge to the
hotfix branch. Tests green (204 passing); QA confirmed sessions persist for the full TTL.

## Risk Assessment
- **What could go wrong:** an incorrect TTL could over-extend sessions (security risk) or
  re-introduce premature expiry (the original defect).
- **Blast radius:** auth service only; no schema or data migration.
- **Mitigation:** fix is a single arithmetic correction with a regression test pinning the
  24-hour TTL; deploy is to a single service behind a load balancer.
- **Rollback:** revert to the prior release tag `release-2026-06-18` (one-command rollback,
  ~2 minutes; no state to unwind).

## Authorization Statement
As CFO, I authorize deployment of build `9f3c1ab` (`hotfix-B1.1`) to **production**. The
production deployment gate is satisfied: review accepted, tests green, Delivery Notice on
record.

## Conditions
- Deploy during the 22:00–23:00 UTC low-traffic window.
- Monitor the auth error rate for 30 minutes post-deploy; roll back if it exceeds baseline.
- Backport the fix to `develop` within 24 hours.
- Produce the required Critical-severity post-mortem (see
  [post-mortem.md](post-mortem.md)) before closing B1.1.
```

---

## Notes

- **Only the CFO may authorize a production deployment.** The HQ Agent may *prepare* the
  authorization but cannot self-authorize. Staging authorizations may be delegated per the
  team's decision matrix.
- A production authorization is only valid after an accepting **Review Decision** and a
  **Delivery Notice** — the merge must already have happened.
- The authorization is committed to the repository for the audit trail. Store under
  `.ai-project/artifacts/deployment-authorizations/`.
- Urgency never waives the gate. A missed bugfix SLA escalates to the CFO; it does not
  permit an unauthorized deploy.
</content>
