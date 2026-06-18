---
type: template
status: active
last_updated: 2026-06-17
---

# Merge Authorization Template

A **Merge Authorization** is the artifact a Phase Chat (or HQ Chat) issues to a Coding
Agent to authorize merging an accepted Epic branch into its parent branch. It is the
explicit "you may now merge" signal that follows an accepting Review Decision — no merge
may happen without it.

Used by: **Phase Chat / HQ Chat** (issuer) → **Coding Agent** (recipient).
Related artifacts: [Review Decision](review-decision.md) (must precede this),
[Epic Closure Notice](epic-closure-notice.md) (the Coding Agent's reply after merge),
[Delivery Notice](delivery-notice.md).

---

## Artifact Schema

```yaml
---
type: merge-authorization
epic: <P#-M#-E#.#>
milestone: <M##>
issued_by: <role and chat name, e.g., "Phase Chat (P4)">
issued_to: <role and chat name, e.g., "Coding Agent (E17.2)">
date: <YYYY-MM-DD>
status: authorized
---
```

| Field | Required | Notes |
|-------|----------|-------|
| `type` | yes | Always `merge-authorization` |
| `epic` | yes | The Epic whose branch is authorized to merge |
| `milestone` | yes | Parent milestone (e.g., `M17`) |
| `issued_by` | yes | Authorizing chat and role |
| `issued_to` | yes | The Coding Agent receiving authorization |
| `date` | yes | ISO date the authorization is issued |
| `status` | yes | `authorized` |

---

## Body Sections

```markdown
# Merge Authorization: <P#-M#-E#.#> — <Epic Name>

## Basis
<Reference the accepting Review Decision (timestamp / path) that this authorization
follows. State that the Definition of Done is met and the PR is accepted.>

## Authorized Merge
- Source branch: epic/<E#.#>
- Target branch: milestone/<M#>
- PR: #<number> — <url>
- Merge strategy: <squash | rebase | merge>

## Conditions
<Any pre-merge conditions: CI green, conflicts resolved, follow-ups filed. If none,
state "None — merge immediately.">

## Post-Merge Instruction
<What the Coding Agent must do after merging: delete the epic branch, produce a Delivery
Notice and an Epic Closure Notice, then stop.>
```

---

## Filled Example

```markdown
---
type: merge-authorization
epic: P4-M17-E17.1
milestone: M17
issued_by: Phase Chat (P4)
issued_to: Coding Agent (E17.1)
date: 2026-06-17
status: authorized
---

# Merge Authorization: P4-M17-E17.1 — Fix Daemon Orchestrator Path Resolution

## Basis
Follows the accepting Review Decision dated 2026-06-17 (Milestone Agent, P4-M17). All
Definition of Done items verified; 182 tests pass with no regression. PR #73 accepted.

## Authorized Merge
- Source branch: epic/P4-M17-E17.1
- Target branch: milestone/M17
- PR: #73 — https://github.com/panchew/ai-project-system/pull/73
- Merge strategy: squash

## Conditions
None — CI is green and the branch is mergeable. Merge immediately.

## Post-Merge Instruction
After merging, delete the epic/P4-M17-E17.1 branch, produce a Delivery Notice and an
Epic Closure Notice confirming the merge commit, then stop.
```

---

## Notes

- A Merge Authorization is only valid after an accepting **Review Decision**. It does not
  replace the review — it acts on its outcome.
- Only HQ Chat, Phase Chat, or Milestone Chat may issue a Merge Authorization. A Coding
  Agent MUST NOT self-authorize a merge.
- The authorization is committed to the repository for the audit trail.
</content>
