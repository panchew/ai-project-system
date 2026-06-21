---
artifact_type: steering_note
artifact_version: 1.0
timestamp: <ISO-8601 UTC, e.g. 2026-06-19T00:00:00Z>
issuer_chat: <issuing chat name, e.g. Creation Chat>
target: <recipient chat name, e.g. HQ Chat>
project_name: <project-slug>
concerns:
  - id: <SN-number, e.g. SN-9>
    severity: <critical | high | medium | low>
    title: <one-line summary>
  # Add one entry per concern. Omit the list (or leave empty) if there are none.
decisions:
  - <binding decision text>
  # Add one entry per binding decision. Omit if there are none.
---

<!--
  STEERING NOTE TEMPLATE — Creation Chat → HQ (or any chat → its parent).

  Purpose: a Steering Note hands off concerns and binding decisions between
  sessions so the next session (or HQ) can act without reconstructing context.
  It is the durable record that survives a chat reset — see
  governance/systems/creation-chat-guide.md (Re-instantiation Ritual).

  When to write one:
  - At the end of every session, before a chat reset.
  - When a blocking concern arises mid-session.
  - After 3+ Bouncer Work log entries of the same type (pattern detected).

  Naming convention: <ISO-date>__<issuer-chat-slug>__steering-note.md
    e.g. 2026-06-19__creation-chat__steering-note.md
  Storage: .ai-project/artifacts/steering-notes/

  Front-matter fields:
  - artifact_type:    always `steering_note`
  - artifact_version: schema version (currently 1.0)
  - timestamp:        ISO-8601 UTC the note was issued
  - issuer_chat:      the chat producing the note (e.g. Creation Chat)
  - target:           the chat receiving it (e.g. HQ Chat)
  - project_name:     project slug (kebab-case)
  - concerns:         list of {id, severity, title} — mirrors the Concerns section
  - decisions:        list of binding decision strings — mirrors Decisions Already Made

  Fill every <placeholder>, delete these comments, then commit.
  A filled reference instance lives at
  .ai-project/artifacts/steering-notes/2026-06-19__creation-chat__steering-note.md
-->

# Steering Note — <Issuer Chat> to <Target Chat>

## Purpose

<!-- One paragraph: which session this closes and what it hands off. No narrative
     history — state the situation and the handoff in two or three sentences. -->

<What session this Steering Note closes, and what it hands off to the target chat.>

---

## Concerns for HQ Triage

<!-- One sub-section per concern. The id/severity/title must match a front-matter
     concerns entry. Detail and required action must be self-contained: a reader
     should not need to open another document to understand or act on the concern.
     If there are no concerns, write "None." and delete the sub-sections. -->

### <SN-number> — <one-line title> [<SEVERITY>]

**Detail:** <What the concern is, stated completely. Include the facts needed to
act — branch names, PR numbers, file paths, dates — inline.>

**Required action:** <The specific action the target chat should take.>

---

## Decisions Already Made

<!-- Binding decisions from this session. NOT for the target chat to re-debate —
     these are settled. Numbered list; one decision per item. Write "None." if
     there are none. Each item here should correspond to a front-matter
     decisions entry. -->

1. <Binding decision text.>
2. <Binding decision text.>

---

## Carry-Over Open Items

<!-- Non-blocking items passed forward for later triage. These do NOT block the
     target chat's next action. Numbered list; write "None." if there are none. -->

1. <Non-blocking item carried forward.>

---

## Next Action

<!-- Exactly what the target chat should do next, in order. Prescriptive, not
     descriptive — a checklist the target chat can execute. -->

<Target Chat> should:
1. <First action.>
2. <Second action.>
