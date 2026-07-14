---
type: template
status: active
last_updated: 2026-06-17
---

# Epic Closure Notice Template

An **Epic Closure Notice** is the artifact a Coding Agent issues to its Milestone Chat to
confirm that an authorized Epic branch merge has completed. It closes the loop opened by
the [Merge Authorization](merge-authorization.md): the parent said "merge," and this
notice reports "merged." It is closely related to the [Delivery Notice](delivery-notice.md)
— the Delivery Notice records the merge for the Epic's own audit trail, while the Epic
Closure Notice is the upward confirmation that lets the Milestone Chat mark the Epic done.

Used by: **Coding Agent** (issuer) → **Milestone Chat** (recipient).

---

## Artifact Schema

```yaml
---
type: epic-closure-notice
epic: <P#-M#-E#.#>
milestone: <M##>
issued_by: <role and chat name, e.g., "Coding Agent (E17.1)">
issued_to: <role and chat name, e.g., "Milestone Chat (P4-M17)">
date: <YYYY-MM-DD>
status: complete
---
```

| Field | Required | Notes |
|-------|----------|-------|
| `type` | yes | Always `epic-closure-notice` |
| `epic` | yes | The Epic being closed |
| `milestone` | yes | Parent milestone (e.g., `M17`) |
| `issued_by` | yes | The Coding Agent that merged the branch |
| `issued_to` | yes | The Milestone Chat receiving confirmation |
| `date` | yes | ISO date the merge completed |
| `status` | yes | `complete` |

---

## Body Sections

```markdown
# Epic Closure Notice: <P#-M#-E#.#> — <Epic Name>

## Merge Confirmation
- PR: #<number> — <url>
- Merge commit: <hash>
- Target branch: milestone/<M#>
- Merged at: <YYYY-MM-DD HH:MM UTC>
- Epic branch: deleted | retained

## Authorization Reference
<Reference the Merge Authorization (issuer + date) that permitted this merge.>

## Final State
<Confirm the Definition of Done is satisfied, the Delivery Notice is produced, and the
working tree is clean. List any accepted follow-ups carried forward.>

## Visual Bindings
<Optional. Record links to any generated visuals for this closure, using the binding schema
in governance/guides/visual-artifacts.md §7 (link + What / Level / State / Description).
Bind a hosted LINK, never a committed path. Omit this section if there are no visuals.>

## Chat Closure
This Epic Chat (<P#-M#-E#.#>) is now closed. No further work will be performed here.
```

---

## Filled Example

```markdown
---
type: epic-closure-notice
epic: P4-M17-E17.1
milestone: M17
issued_by: Coding Agent (E17.1)
issued_to: Milestone Chat (P4-M17)
date: 2026-06-17
status: complete
---

# Epic Closure Notice: P4-M17-E17.1 — Fix Daemon Orchestrator Path Resolution

## Merge Confirmation
- PR: #73 — https://github.com/panchew/ai-project-system/pull/73
- Merge commit: f19ca36
- Target branch: milestone/M17
- Merged at: 2026-06-17 00:00 UTC
- Epic branch: deleted

## Authorization Reference
Merged under the Merge Authorization issued by Phase Chat (P4) on 2026-06-17, which
followed the accepting Review Decision of the same date.

## Final State
Definition of Done satisfied; Delivery Notice produced and committed; working tree clean.
No outstanding follow-ups.

## Chat Closure
This Epic Chat (P4-M17-E17.1) is now closed. No further work will be performed here.
```

---

## Notes

- The Epic Closure Notice is issued **only after** the merge actually completes. Do not
  issue it in anticipation of a merge.
- It does not replace the Delivery Notice; both are produced. The Delivery Notice is the
  Epic's record; the Epic Closure Notice is the explicit signal to the Milestone Chat
  that the Epic may be marked closed.
- An Epic with a dirty working tree MUST NOT be closed. Resolve uncommitted changes first.
</content>
