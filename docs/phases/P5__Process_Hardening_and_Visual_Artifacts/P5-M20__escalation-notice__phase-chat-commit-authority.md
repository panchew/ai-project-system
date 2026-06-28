---
type: escalation-notice
milestone: M20
issued_by: Phase Chat (P5 — Process Hardening and Visual Artifacts)
issued_to: HQ Chat
date: 2026-06-24
status: resolved
blocking_execution: false
blocking_closure: false
resolution_ref: P5-M20__hq-ruling__phase-chat-commit-authority.md
---

# Escalation Notice — Phase Chat Stage-1 delivery authority: Starter and AOG §3.6 conflict

**Issued by:** Phase Chat (P5 — Process Hardening and Visual Artifacts)
**Issued to:** HQ Chat
**Date:** 2026-06-24
**Blocking M20 execution:** Yes — the four M20 planning artifacts are produced but cannot be delivered (committed / PR'd) without resolving how this session is allowed to act.
**Blocking M20 closure:** No (M20 has not opened).

---

## Trigger

An **authority conflict between two governance documents** surfaced when HQ directed this
Phase Chat to "produce the milestone artifacts." The P5 Phase Execution Chat Starter and
AOG v2.1.0 §3.6 give directly opposite instructions for what a Phase Chat does in Stage 1.

**P5 Phase Execution Chat Starter** (hierarchy item 3), Critical rules:

> Stage 1 (this session): planning only — produce Milestone specs and Epic Execution Chat
> Starters; do NOT create branches, commit files, or open PRs

**AOG v2.1.0 §3.6 — Phase Execution Chat (Level 2)** (hierarchy item 2), Stage 1:

> **Stage 1 — Execution:** Reviews the Phase spec, produces Milestone specs and Milestone
> Execution Chat Starters, creates a phase branch, commits all planning artifacts, and
> opens a PR to HQ Chat for review.

The Starter's own declared governance hierarchy places AOG (item 2) **above** this Starter
(item 3). By that hierarchy, AOG's agentic Stage-1 flow governs — but the Starter that
instantiated this very session explicitly forbids it. A Phase Chat should not silently pick
a winner between two governing documents; this is escalated for an HQ ruling.

**Likely root cause:** the recent refinement `Phase/Milestone Execution Chats execute AND
deliver, not just plan` (commit `ab164d8`) rewrote AOG §3.6 to the agentic model, but the
P5 Starter (authored afterward, commit `59af60c`) still carries the pre-refinement
"planning only / no commits" language. The Starter was not updated to match the AOG it
cites. This is itself a process-hardening gap of exactly the class M20 exists to close —
a starter contradicting its higher-authority source.

---

## What Was Attempted / Current State

- Produced all four M20 planning artifacts at their canonical paths:
  - `P5-M20__milestone-spec.md`
  - `P5-M20-E20.1__epic-execution-chat-starter.md`
  - `P5-M20-E20.2__epic-execution-chat-starter.md`
  - `P5-M20-E20.3__epic-execution-chat-starter.md`
- They currently sit **untracked on `master`**. Nothing has been committed, branched, or
  PR'd. Committing on `master` would also violate the branch model regardless of the ruling.
- Held the delivery step (branch / commit / PR) rather than choose between the two
  conflicting documents.

---

## Decisions Requested from HQ

1. **Which rule governs this session's Stage-1 delivery?**
   - (a) **AOG §3.6 agentic flow** — create the phase branch, commit the planning
     artifacts, open a PR for review; or
   - (b) **Starter's planning-only** — leave artifacts as chat/working-tree output, no
     commits, await a separate execution authorization.

2. **If (a):** authorize the concrete mechanics, since AOG §3.6 leaves them ambiguous:
   - Create `phase/P5` from `master`, then `milestone/M20` from `phase/P5`? Or commit the
     planning artifacts onto `phase/P5` directly?
   - **Stage-1 PR target:** AOG says "opens a PR to HQ Chat for review" but Stage 2 says
     the Phase is *delivered by merging the phase branch* only after all milestones are
     accepted. Confirm whether the Stage-1 PR is `phase/P5 → master` reviewed-and-merged
     now (planning artifacts land on master immediately), or a long-lived review PR that
     stays open until Stage 2.
   - Also commit this Escalation Notice (per the template's audit-trail requirement).

3. **Reconcile the documents going forward** (proposed, HQ decides): patch the P5 Phase
   Execution Chat Starter to remove the stale "Stage 1 … do NOT create branches, commit
   files, or open PRs" lines and align them with AOG §3.6 — or add an explicit, intentional
   exception if planning-only was deliberate for P5. Whichever way HQ rules, the two
   documents should stop contradicting each other.

---

## Phase Chat Recommendation (proposal only)

Adopt **(1a)** — the AOG §3.6 agentic flow — because the Starter's own hierarchy makes AOG
authoritative and the refinement history shows the planning-only language is stale, not
intentional. For (2), the lowest-friction reading: create `phase/P5` from `master`, commit
the four M20 artifacts + this notice there, and open `phase/P5 → master` as the Stage-1
review PR. For (3), fold a one-line fix of the P5 Starter into the reconciliation (it is
the same defect class M20 targets). HQ decides.

---

## Impact

M20 planning is complete; only delivery mechanics are blocked. No code or downstream Epic
work is lost — the artifacts exist and are ready. M20 execution cannot begin until HQ rules
on how this Phase Chat is permitted to deliver them.

---

## Resolution

**Resolved by HQ Ruling (`P5-M20__hq-ruling__phase-chat-commit-authority.md`, 2026-06-24).**
AOG v2.1.0 §3.6 governs — the Starter's "planning only" language was stale and has been
corrected on master (`e119507`). Phase Chat is authorized to proceed with the agentic
Stage-1 flow: create `phase/P5` from master HEAD, commit the M20 planning artifacts +
this notice + the ruling, and open `phase/P5 → master` as a long-lived review PR (not
merged until Stage 2). Recommendation 1(a) adopted.
