---
type: template
status: active
last_updated: 2026-09-03
---

# Context-Exhaustion Handoff Template

<!--
  CONTEXT-EXHAUSTION HANDOFF TEMPLATE

  Purpose: Define the artifact type and template for a chat that departs — by context
  exhaustion, by deliberate hand-over, or by a departure it does not even know it made.
  Designed by P12-M44-E44.1 (zero templates existed before it). The Drivr boundary is
  stated in this document, not assumed.

  The two faces of this artifact:
  1. WRITTEN face — a session that can feel the end coming writes this artifact and
     commits it before it departs.
  2. RECONSTRUCTIBLE face — the case that actually occurred (the 2026-08-20 departure
     specimens: a session that forked and did not know it had departed). Nobody wrote
     anything. The arriving session must be able to reconstruct the handoff from
     committed state ALONE. The artifact must therefore never be required for a successor
     to continue — committed state is the floor, never the hope.

  Usage:
  1. A departing session writes this artifact when it can feel the end coming or is
     deliberately handing over, and commits it.
  2. An arriving session that finds a handoff reads it; one that finds none reconstructs
     the handoff from committed state (see the Reconstruction section below).
  3. Commit as .ai-project/artifacts/handoffs/<ISO-date>__<chat-id>__context-handoff.md
-->

---

## Artifact Type Definition

- **Artifact type:** `context_handoff`
- **Purpose:** Carry the state a departing chat holds — its scope, its in-flight
  obligations, its open decisions, its next action — to the session that succeeds it.
- **Trigger:** context exhaustion (the session can feel the end coming), a deliberate
  hand-over, or any other departure. **A missing handoff is not a defect in the successor**
  — the reconstructible face covers it.
- **Storage:** `.ai-project/artifacts/handoffs/`
- **Naming:** `<ISO-date>__<chat-id>__context-handoff.md`
- **Direction:** horizontal/self — a session's own successor, not a parent/child gate
  artifact (it is not a Delivery Notice, and it does not substitute for one).

### The Drivr boundary (stated)

- **Harness context tracking is Drivr's — this artifact must not assume it.** Writing and
  reading this artifact requires nothing from Drivr: no token counts, no context-usage
  reports, no live session registry. A session writes it from what it holds; a successor
  reads it from committed state. **If Drivr exists and reports context usage, that is a
  trigger signal for the WRITTEN face — never a requirement of it.**
- **The role registry is M46's, not this artifact's.** Nothing here makes a successor
  *findable* — E44.1 states what a departing session *leaves behind*; the registry that
  maps a session to its governance role is Drivr's (M46). This artifact and that registry
  do not collide.

### The reconstructibility requirement

Something must be **reconstructible by the arriving session from committed state alone**,
because the case that actually occurred is the one where nobody was there to perform the
act. The written handoff is the ideal; the committed state is the floor.

---

## The Handoff

Use this format when a session departs:

```markdown
---
artifact_type: context_handoff
artifact_version: 1.0
timestamp: <ISO-8601 UTC>
departing_chat: <chat_type> (<full_reference>)
departure_reason: context-exhaustion | deliberate-handover | unknown
replacement_chat: <chat_type> (<full_reference>)  # if known
branch: <branch>  # the branch the session was working on
last_commit: <sha>  # the last commit the session made
---

# Context-Exhaustion Handoff: <chat_type> (<full_reference>)

## What this session was doing
<the session's role, level and scope — the artifact it was executing, by reference>

## What this session holds
- <open decision 1, with its committed artifact>
- <open decision 2>
- <deferred correction / obligation, with its owner and trigger>
- <unresolved concern, with the action it requires>
[List everything that must not be lost when this session ends]

## What this session was reading
<the artifacts attached to this session — spec, starter, opener — by reference>

## Where this session stopped
<exactly what the next session should do first — the next action>

## What this session committed
- <artifact/change 1, with its ref>
- <artifact/change 2, with its ref>
```

---

## Reconstruction — when no handoff was written

When a successor arrives and no handoff exists, it reconstructs one **from committed state
alone**:

1. **`git log` of the branch** the predecessor worked on — the last commits, with their
   messages, are the predecessor's own close-out.
2. **The committed execution artifacts** it was executing — the Epic spec, Execution Chat
   Starter, or (for HQ) the most recent opener — which state its scope and next actions.
3. **The artifact streams** — Steering Notes, Progress Digests, openers, escalation
   notices, rulings, delivery notices — which record the decisions and obligations the
   predecessor held.
4. **The `supersedes:` / reference chains** — which link each artifact to the one before it.

If the reconstruction is incomplete, the gap is a defect in the departing session's
commit discipline — recorded, not silently filled in. **Committed state is the floor,
never the hope.**

---

## Notes

- A session that departs **without knowing it has departed** (a fork) can write nothing;
  the reconstructible face is what covers it. A ritual that assumes the departing session
  knows it is leaving covers only the deliberate face.
- This artifact is **not** a Delivery Notice and does not authorize, accept, or close
  anything — it is a continuity record, and it never substitutes for the parent-chat gate
  (PSG §11.6).
- Template follows governance style (prescriptive, structured, explicit).