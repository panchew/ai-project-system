---
type: template
status: active
last_updated: 2026-09-02
---

# Merge Authorization Template

A **Merge Authorization** is the **parent's own record of an act it performed itself**:
the merge of a child's branch. It is **not** an instruction issued to a child: the child
never holds merge authorization (PROJECT-SYSTEM-GUIDELINES.md §11.6 — *the parent
performs the merge of a child's branch*). The parent that accepted a delivery performs
the merge of that child's branch — by silence for a clean delivery, or following an
accepting Review Decision on the exception path (PROJECT-SYSTEM-GUIDELINES.md §11.6 /
AI-OPERATING-GUIDELINES.md §12) — and this artifact is the durable record of that act.

Used by: **Phase Chat / Milestone Chat / HQ Chat** — the parent that performed the
merge (recorder) → itself. The child never receives it.
Related artifacts: [Review Decision](review-decision.md) (precedes this only on the
exception path — a clean delivery is accepted by silence),
[Epic Closure Notice](epic-closure-notice.md) (the child's confirmation that the
merge performed by the parent completed), [Delivery Notice](delivery-notice.md) (the
child's own delivery record, produced at execution completion).

---

## Artifact Schema

```yaml
---
type: merge-authorization
epic: <P#-M#-E#.#>
branch: epic/<E#.#>
milestone: <M##>
issued_by: <role and chat name of the parent that performed the merge, e.g., "Milestone Chat (M43)">
issued_to: <the parent chat — the parent records its own act>
date: <YYYY-MM-DD>
status: merged
---
```

| Field | Required | Notes |
|-------|----------|-------|
| `type` | yes | Always `merge-authorization` |
| `epic` | yes | The Epic whose branch was merged |
| `branch` | yes | The branch merged, e.g., `epic/P12-M43-E43.1` — a reference to the branch, not the party addressed |
| `milestone` | yes | Parent milestone (e.g., `M43`) |
| `issued_by` | yes | The parent chat that performed the merge |
| `issued_to` | yes | The parent chat — the parent records its own act |
| `date` | yes | ISO date the merge was performed |
| `status` | yes | `merged` |

---

## Body Sections

```markdown
# Merge Authorization: <P#-M#-E#.#> — <Epic Name>

## Basis
<State that the Definition of Done is met and the delivery is accepted — by silence for
a clean delivery (PSG §11.6 / AOG §12), or, on the exception path, reference the
accepting Review Decision (timestamp / path) that the parent's merge follows.>

## Merge Record
- Source branch: epic/<E#.#>
- Target branch: milestone/<M#>
- PR: #<number> — <url>
- Merge strategy: <squash | rebase | merge>

## Conditions
<Any pre-merge conditions that were satisfied: CI green, conflicts resolved, follow-ups
filed. If none, state "None — merged on acceptance.">

## Post-Merge
<The parent's own follow-through after the merge it performed: delete the merged
branch, confirm the child produced its Delivery Notice, then stop.>
```

---

## Filled Example

```markdown
---
type: merge-authorization
epic: P4-M17-E17.1
branch: epic/P4-M17-E17.1
milestone: M17
issued_by: Phase Chat (P4)
issued_to: Phase Chat (P4)
date: 2026-06-17
status: merged
---

# Merge Authorization: P4-M17-E17.1 — Fix Daemon Orchestrator Path Resolution

## Basis
Follows the accepting Review Decision dated 2026-06-17 (Milestone Agent, P4-M17) —
exception path, accepted with a follow-up Epic. All Definition of Done items verified;
182 tests pass with no regression. PR #73 accepted.

## Merge Record
- Source branch: epic/P4-M17-E17.1
- Target branch: milestone/M17
- PR: #73 — https://github.com/panchew/ai-project-system/pull/73
- Merge strategy: squash

## Conditions
CI was green and the branch mergeable. Merged on acceptance.

## Post-Merge
Deleted the epic/P4-M17-E17.1 branch after the merge, confirmed the child produced its
Delivery Notice, and stopped.
```

---

## Notes

- A Merge Authorization is only valid after **parent acceptance** of the delivery — by
  silence for a clean delivery, or an accepting **Review Decision** on the exception path
  (PSG §11.6 / AOG §12). It does not replace the review — it records the act that acts
  on its outcome.
- Only the parent that performed the merge may record a Merge Authorization. A child
  **never** holds merge authorization and **MUST NOT** merge its own branch — the parent
  performs the merge (PSG §11.6).
- The record is committed to the repository for the audit trail.
</content>