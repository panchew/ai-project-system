# Bugfix Epics (`docs/bugfixes/`)

This directory is the canonical home for **Bugfix Epic specs** — the minimal specs HQ
Chat produces when an unplanned, production-affecting issue cannot wait for the next
planned Epic cycle.

A Bugfix Epic is the expedited variant of a normal Epic: direct from HQ Chat, minimal
spec, a 4-hour review SLA, and a mandatory CFO Deployment Authorization before any
production push. The full workflow lives in
[`governance/systems/bugfix-epic-workflow.md`](../../governance/systems/bugfix-epic-workflow.md);
the HQ Chat handler lives in
[`governance/systems/hq-execution-chat-starter.md`](../../governance/systems/hq-execution-chat-starter.md).

---

## B#.# Naming Convention

Bugfix Epics use a **`B#.#`** identifier instead of the planned-Epic `E#.#` form, so
they are visibly distinct in branch names, specs, and the audit trail.

```
B<severity-number>.<sequence>
```

- **`B`** — marks this as a Bugfix Epic (not a planned `E#.#` Epic).
- **First number — severity class:**

  | Severity number | Severity | Meaning |
  |-----------------|----------|---------|
  | `B1.x` | Critical | Production down, data loss, or active security exploit. Post-mortem required. |
  | `B2.x` | High | Major feature broken or degraded for many users. Post-mortem required. |
  | `B3.x` | Medium | Limited-impact defect with a workaround. Post-mortem optional. |
  | `B4.x` | Low | Cosmetic or minor defect, no material impact. Post-mortem optional. |

- **Second number — sequence:** a monotonically increasing counter within that severity
  class (`B1.1`, `B1.2`, `B1.3`, …). Numbers are never reused.

> **Note on the historical scheme.** `bugfix-epic-workflow.md` originally described
> `B<phase>.<sequence>` (the first digit being the phase). This README supersedes that
> for new bugfixes: the first digit now encodes **severity**, which is the dimension HQ
> and the CFO act on. The phase is recorded in the spec front-matter (`phase_id`), so no
> information is lost.

### Filename Format

```
docs/bugfixes/B<severity>.<sequence>__spec__<slug>.md
```

- `<slug>` is a short kebab-case description of the issue.

**Examples:**

```
docs/bugfixes/B1.1__spec__auth-session-expiry.md      # Critical
docs/bugfixes/B2.1__spec__export-csv-truncation.md    # High
docs/bugfixes/B3.2__spec__avatar-cache-stale.md       # Medium
```

---

## Required Spec Fields

A Bugfix Epic spec is intentionally minimal. It MUST carry the following front-matter and
body sections (the canonical template is in
[`governance/systems/bugfix-epic-workflow.md`](../../governance/systems/bugfix-epic-workflow.md)):

```yaml
---
epic_id: B#.#               # e.g., B1.1
phase_id: <P#>              # owning phase (records context the B# no longer encodes)
category: bugfix
severity: critical|high|medium|low
discovered_date: <YYYY-MM-DD>
status: open
---
```

Required body sections:

1. **Problem** — what is broken (2–3 sentences).
2. **Impact** — severity, affected component, affected users.
3. **Root Cause** — known cause, or `TBD — investigate`.
4. **Fix** — proposed direction, or `TBD — implement during execution`.
5. **Definition of Done** — root cause identified, fix implemented and tested, no
   regressions, merged and deployed.

---

## Lifecycle at a Glance

1. Issue reported to HQ Chat → HQ evaluates severity and scope.
2. HQ writes the `B#.#` spec here and issues an Epic Delivery Authorization.
3. Coding Agent fixes on a `bugfix/B#.#` branch.
4. HQ reviews the Completion Notice **within 4 hours** (SLA); a miss escalates to the CFO.
5. Production deploy requires a **CFO Deployment Authorization**
   ([template](../../governance/templates/deployment-authorization.md)).
6. Critical / High severity bugfixes require a **post-mortem**
   ([template](../../governance/templates/post-mortem.md)).

---

## Related Documentation

- [Bugfix Epic Workflow](../../governance/systems/bugfix-epic-workflow.md) — full design,
  SLA, escalation, merge strategy.
- [HQ Execution Chat Starter](../../governance/systems/hq-execution-chat-starter.md) —
  the "Handling Production Issues" handler.
- [Deployment Authorization template](../../governance/templates/deployment-authorization.md)
- [Post-Mortem template](../../governance/templates/post-mortem.md)
</content>
</invoke>
