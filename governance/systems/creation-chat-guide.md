# Creation Chat Guide — Ongoing Operation

**Status:** Active
**Applies to:** Creation Chat (Level 0 — see [`chat-hierarchy.md`](chat-hierarchy.md))
**Companion to:** [`start-a-project.md`](start-a-project.md) (the bootstrap half)

---

## Why this guide exists

[`start-a-project.md`](start-a-project.md) covers the **bootstrap half** of the
Creation Chat: producing the committed `genesis.md` that lets a Phase Chat open.
This guide covers the **ongoing half**: how the Creation Chat operates as a
permanent institution across many sessions — handing off state, staying informed,
recording manual work, and resetting without losing continuity.

The governing design constraint:

> Creation Chat is the single visible human interface. All governance (HQ, Phase,
> Milestone, Epic) runs as background agents communicating via artifacts. Complexity
> stays invisible to the user; only decisions and outcomes surface.

Everything below exists to make that continuity survive a chat reset using nothing
but committed artifacts.

---

## Re-instantiation Ritual

A Creation Chat session does not live forever. Context fills, sessions end, chats
get reset. The ritual preserves continuity across a reset using three committed
artifacts and no session memory.

### Step 1 — Before reset: produce and commit a Steering Note

Before ending a session or resetting the chat, produce a Steering Note using
[`../templates/steering-note.md`](../templates/steering-note.md) and commit it to:

```
.ai-project/artifacts/steering-notes/<ISO-date>__creation-chat__steering-note.md
```

This is the durable record of where the project stands. If it is not committed,
the reset loses state. Committing is part of the ritual, not an afterthought.

### Step 2 — What to include in the pre-reset Steering Note

Structured state, not a narrative. Capture exactly:

- **Open concerns** — anything unresolved, each with id, severity, and the action
  it requires (front-matter `concerns` + the Concerns section).
- **Binding decisions** — decisions made this session that must not be re-debated
  (front-matter `decisions` + the Decisions Already Made section).
- **Carry-over items** — non-blocking items passed forward.
- **Next action** — exactly what the next session (or HQ) should do first.

If the next session would have to guess at any of these, the note is incomplete.

### Step 3 — How to re-open: pass exactly three artifacts to the new session

Open the new session with these three committed artifacts and nothing else:

1. The project's committed **`genesis.md`** (project root or governance root).
2. The **most recent Steering Note** from
   `.ai-project/artifacts/steering-notes/` (latest by ISO-date in the filename).
3. The **most recent Progress Digest**, if one exists, from
   `.ai-project/artifacts/progress-digests/` (latest by ISO-date).

No chat transcript, no memory export — only these files.

### Step 4 — What the new session receives

A complete picture of project state with no session memory required:

- `genesis.md` gives project identity and Phase 1 boundaries.
- The latest Steering Note gives open concerns, binding decisions, carry-overs,
  and the next action.
- The latest Progress Digest (if present) gives current phase/milestone status.

The new session opens as if continuing uninterrupted. If it cannot, the gap is a
defect in the pre-reset Steering Note (Step 2) — fix the note, not the ritual.

---

## When to Write a Steering Note

Write one:

- **At the end of every session**, before a chat reset (the ritual above).
- **When a blocking concern arises mid-session** — do not wait for session end;
  commit a Steering Note so the concern reaches HQ immediately.
- **After 3+ Bouncer Work log entries of the same type** — a detected pattern is
  a concern worth formalizing (see the loop below).

---

## When to Expect a Progress Digest

The Creation Chat receives a Progress Digest (HQ → Creation Chat) using
[`../templates/progress-digest.md`](../templates/progress-digest.md):

- **At the start of each new phase or milestone** — HQ sends one unprompted.
- **On request** — the Creation Chat can ask HQ Chat for a fresh digest at any time.

The Progress Digest is the primary self-contained summary of project state. The
user should never need to open a phase or milestone artifact to understand where
the project stands — if they do, the digest has failed its purpose.

---

## CFO PR Review Gate

Layer 8 (the CFO / human operator) must be able to see PR changes before a merge
happens. This is a **configurable gate** — ON by default, disableable per project
when the CFO trusts the process to merge automatically. The gate is additive: it
does not replace or rename the existing merge-authorization artifacts, it adds a
human review step ahead of them.

### Configuration

The toggle is a project-level setting in `.ai-project.yml`:

```yaml
cfo_review_gate: enabled   # or: disabled
```

- **`enabled`** (default) — every merge-ready PR must be surfaced for CFO diff
  review before it merges.
- **`disabled`** — merges proceed automatically (agentic auto-merge); behavior is
  unchanged from a system with no gate.

A project that omits the key is treated as `enabled` (gate ON by default).

### Behavior when the gate is ON

```
PR becomes merge-ready
  → surfaced in the Progress Digest "Open Decisions" section
    (PR number, source → target branch, one-line change summary)
      → CFO reviews the diff
        → CFO approves
          → merge proceeds (existing merge-authorization flow)
```

The Progress Digest is the single visible surface, so the merge-ready PR appears
there — showing **what will merge**, not merely that something is ready. This keeps
the gate consistent with the single-visible-interface constraint: the CFO never has
to leave the Creation Chat surface to know a merge is pending.

### Behavior when the gate is OFF

The current automated merge behavior is unchanged. Merge-ready PRs do **not** appear
in the Progress Digest's Open Decisions section, and merges complete without a human
review step.

---

## Bouncer Work Log → Steering Note Loop

Bouncer work is Layer-8 manual intervention triggered by operating a live system:
data fixes, direct user requests, one-off console operations — the gap between what
the system does and what reality demands. It is distinct from the Bugfix Workflow,
which targets code defects and produces commits.

Each intervention gets a lightweight Bouncer Work log entry
([`../templates/bouncer-work-log.md`](../templates/bouncer-work-log.md)) — under two
minutes to fill. The flow:

```
real-life operation
  → bouncer work happens (manual intervention, no commit)
    → logged in Bouncer Work log (lightweight record)
      → pattern detected (3+ of the same type?)
        → Steering Note to HQ
          → formal Epic (automate the fix, close the gap)
```

**What counts as a pattern:** the **same severity** and the **same type** of
intervention occurring **3 or more times**. When the third matching entry lands,
set the Pattern flag on that Bouncer Work log entry and write a Steering Note to HQ
proposing formalization. The Steering Note is how a repeated manual workaround
becomes a funded Epic that removes the manual work.

---

## Related Documentation

- [`start-a-project.md`](start-a-project.md) — bootstrap half (producing genesis.md)
- [`chat-hierarchy.md`](chat-hierarchy.md) — Creation Chat as Level 0
- [`../templates/steering-note.md`](../templates/steering-note.md)
- [`../templates/progress-digest.md`](../templates/progress-digest.md)
- [`../templates/bouncer-work-log.md`](../templates/bouncer-work-log.md)
