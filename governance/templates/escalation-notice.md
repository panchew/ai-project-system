---
type: template
status: active
last_updated: 2026-07-30
---

# Escalation Notice Template

An **Escalation Notice** is the artifact any chat issues to its **parent** chat when it
hits a blocking or out-of-scope finding it cannot resolve within its own authority.
Escalation is always upward (Epic → Milestone → Phase → HQ); lateral escalation between
siblings is prohibited.

**It is also the carrier for a handback from an instance that is not a chat.** *(Added
P10-M35-E35.3, 2026-07-30.)* An instance running unattended (Execution Mode `agentic` —
[`../systems/chat-hierarchy.md`](../systems/chat-hierarchy.md)) has no chat in which a human
notices a block and no human present to write the notice, and is **nonetheless subject to
the same obligation**: a blocked agentic instance **MUST** surface the block to its
**immediate parent** via this artifact. Read *"any chat"* throughout this template as **any
instance of any level, attended or unattended.** The handback rule — its destination, the
authority-bearing character of the parent's resolution, and the one-level routing it inherits
— is normative in `../systems/chat-hierarchy.md` ("Handback: what a blocked agentic instance
owes") and is not restated here. **This template's schema is unchanged by it**; a handback
needs no new field.

Used by: **any instance of any level** (Epic / Milestone / Phase), manual or agentic → its
**parent chat**.
Related: the [Rework Cycle](milestone-execution-chat-starter.md) (3 exhausted attempts is
a common trigger) and the [Troubleshooting Guide](../../docs/team-collaboration/troubleshooting-guide.md).

---

## Artifact Schema

```yaml
---
type: escalation-notice
milestone: <M##>
issued_by: <role and chat name, e.g., "Milestone Chat (P4-M17)">
issued_to: <role and chat name, e.g., "Phase Chat (P4)">
date: <YYYY-MM-DD>
status: open
---
```

> **Note:** Per the schema, `epic` is **omitted** for an Escalation Notice — escalation
> is a chat-to-chat signal, not an Epic deliverable. Name the affected Epic(s) in the
> body instead. (If escalating from an Epic chat, you may include `epic:` for context,
> but it is not required.)

| Field | Required | Notes |
|-------|----------|-------|
| `type` | yes | Always `escalation-notice` |
| `milestone` | yes | Milestone context (e.g., `M17`) |
| `issued_by` | yes | The escalating chat and role |
| `issued_to` | yes | The parent chat receiving the escalation |
| `date` | yes | ISO date the escalation is raised |
| `status` | yes | `open` → `resolved` once the parent responds |

---

## Body Sections

```markdown
# Escalation Notice: <short title> (<affected Epic / area>)

## Trigger
<Why this is being escalated: 3 rework attempts exhausted, out-of-scope finding,
missing/contradictory spec, cross-milestone dependency, authority conflict, or an
agentic instance blocked on judgment it cannot supply (handback — see
`../systems/chat-hierarchy.md`).>

## What Was Attempted
<Concrete steps already taken to resolve it without escalating. For a rework
exhaustion, summarize each of the 3 attempts.>

## Decision Needed
<The specific decision or input required from the parent chat to unblock.>

## Impact
<Who/what is blocked and the cost of inaction — e.g., "blocks 2 developers and delays
M17 closure.">

## Resolution
<Left empty when status: open. The parent chat records its decision here and sets
status: resolved.>
```

---

## Filled Example

```markdown
---
type: escalation-notice
milestone: M17
issued_by: Milestone Chat (P4-M17)
issued_to: Phase Chat (P4)
date: 2026-06-17
status: open
---

# Escalation Notice: E17.9 cannot complete as specified (3 attempts exhausted)

## Trigger
Rework attempts exhausted. E17.9 has received three Reject decisions; the third
Completion Notice still fails the Definition of Done.

## What Was Attempted
- Attempt 1: Rejected for 62% test coverage (spec requires 80%).
- Attempt 2: Coverage met, but the change required touching files outside the Epic
  spec's scope to pass integration tests.
- Attempt 3: Scope-limited fix submitted, but the integration tests cannot pass without
  the out-of-scope change. The spec and the dependency are in conflict.

## Decision Needed
Either (a) amend the E17.9 spec to include the dependent module and reset the attempt
counter, or (b) split the dependency into a new Epic and re-scope E17.9.

## Impact
Blocks the developer assigned to E17.9 and delays M17 closure. No other Epic depends on
E17.9, so the rest of M17 can proceed in parallel.

## Resolution
(empty — awaiting Phase Chat decision)
```

---

## Notes

- Escalate **upward only**. A Milestone Chat MUST NOT escalate to a sibling Milestone;
  it escalates to its Phase Chat.
- Do not proceed on the blocked path until the parent chat responds and sets the notice
  to `status: resolved`.
- The Escalation Notice is committed to the repository — an escalation raised only in
  chat is not authoritative and leaves no audit trail.
</content>
