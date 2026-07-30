---
type: escalation-notice
milestone: M34
issued_by: Milestone Chat (P10-M34)
issued_to: Phase Chat (P10)
date: 2026-07-29
status: resolved
resolved_by: direct CFO instruction to Phase Chat (in-session, 2026-07-29)
resolved_date: 2026-07-29
---

# Escalation Notice: the M34 fleet set changed — `fieldledger-assesment` out, `social-stories-creator` in, and a higher-priority project inbound

## Trigger

The CFO informed the Milestone Chat, in session on 2026-07-29, that the fleet has changed:

1. **`fieldledger-assesment` is out.**
2. **`social-stories-builder` is in.**
3. **A "personal platform" will be in soon and will take highest priority.**

E34.1 and E34.3 are merged and unaffected. **E34.2 is the only unplanned epic, and all three items
land on it.** I stopped before authoring its spec.

## Why this is not mine to absorb

The project set is not a Milestone-Chat variable. `fieldledger-assesment` is named **normatively**
in artifacts above my adjacency (PSG §1A — I may not produce or amend the Milestone spec, still less
the Phase spec):

| Document | Location | What it says |
|---|---|---|
| **P10 phase spec** | §Acceptance Criteria | *"courtis, **fieldledger-assesment**, and Getawayinsured2023 each have a recorded roll-forward path with demonstrable movement"* — **a CFO acceptance criterion for the whole phase** |
| **P10 phase spec** | §P10.2, §Milestones→M34 Goal | names it in the dormant set |
| **M34 milestone spec** | §Acceptance Criteria (E34.2), §Definition of Done | names it in both |
| **M34 milestone spec** | Problem Statement, Goals, In Scope, Epic Detail | names it throughout |

Dropping it silently would leave a phase acceptance criterion unmeetable and unremarked. My starter
is explicit: *"If the Milestone spec is silent on a topic, escalate to the Phase Chat rather than
assuming"* and *"do not expand scope beyond this Milestone's Epics."* The precedent is SN-24, where
a comparable form-only change to M35 still required the Phase Chat to amend the phase spec (v1.1.0)
under an HQ Ruling.

## Findings the decision should rest on (verified 2026-07-29, not assumed)

### 1. The named project does not exist; a similarly-named one does

There is **no `social-stories-builder`** anywhere in `~/soft-dev`. There **is
`social-stories-creator`** — and it is the name carried in `ai-project-system-mcp`'s `registry.yml`
(line 10). I have assumed these refer to the same project but have **not** acted on that assumption.
**Please confirm the name**, or confirm a rename is intended.

### 2. It is not a like-for-like swap — it inverts E34.2's premise

E34.2 exists to roll **dormant, stale** projects forward. `social-stories-creator` is the opposite
shape of work:

| | `fieldledger-assesment` (out) | `social-stories-creator` (in) |
|---|---|---|
| Governance version | `"5.1.0"` — two majors behind | **v7.0.0 already** (submodule at `8044451`) |
| Canonical agent | **none at all** | **present** (`governance.agent.md`) |
| Status | dormant | **active inception** — created 2026-07-21, `genesis.md` `status: complete` 2026-07-23, Phase 1 "Prototype", carries a `seed.md` (full HQ path) |
| M34 lift | agent install + multi-version corpus bump + stamp | **`framework_version` stamp only** |

Swapping them **reduces** E34.2's work and weakens what the milestone demonstrates: the epic's thesis
is that E33.1's procedure moves stale legacy installs, and `social-stories-creator` would exercise
almost none of it. That is a defensible outcome, but it is a **scope decision**, not a list edit —
which is exactly why it is escalated rather than absorbed.

There is also a live question the Phase Chat should settle: a project mid-inception with a completed
genesis is arguably **not a "dormant enrolled project" at all**, and may belong outside M34's frame
entirely rather than inside E34.2's list.

### 3. It is a third instance of P10-GH-5

`social-stories-creator`'s `.ai-project.yml` carries `version: v7.0.0` — **unquoted and v-prefixed**,
failing yml-spec rule 5 (`\d+\.\d+\.\d+`) — and has **no `ref:` key**, failing rule 3. So the count
in the P10-GH-5 note rises to **3 of 6** enrolled projects schema-invalid. The note is filed as
`docs/phases/P10__.../P10-M34__carry-forward-note__P10-GH-5-unenforced-yml-validation.md`; I have not
edited it, since its audit is timestamped to the pre-change fleet.

### 4. The inbound "personal platform" is above M34

It has no name, no repository, and no enrollment. **"Highest priority" is a phase-or-above
prioritization statement**, not an epic input — P10's scope and ordering were fixed by SN-23, and
a new top-priority project plausibly implies a Steering Note or Creation Chat rather than an M34
amendment. M34 should not hold a slot for it, and E34.2 should not be sized around it. Flagged so it
is routed, not absorbed.

## What I need to proceed

A Phase Chat decision on E34.2's project set, and — because a phase acceptance criterion is
affected — a view on whether this needs HQ.

Specifically:

1. **Is `fieldledger-assesment` removed from the phase acceptance criteria**, or merely deprioritized
   within M34? These have different blast radii: removal requires a **phase spec amendment**;
   deprioritization can be handled inside E34.2 as a recorded, non-blocking deferral with the project
   still named.
2. **Confirm the incoming project's name** (`social-stories-creator`?).
3. **Is it in M34 at all**, given it is current-and-active rather than dormant-and-stale? If yes,
   E34.2's Goals/DoD/Acceptance Criteria need amending to describe a stamp-only project.
4. **Where does the personal platform get routed** — Steering Note, Creation Chat, or a later phase?
   M34 assumes nothing about it absent an answer.

## What I have not done

- Not authored the E34.2 spec or starter.
- Not amended the Milestone spec, the Phase spec, or the P10-GH-5 note.
- Not touched `social-stories-creator` or any target repository.
- Not assumed `social-stories-builder` and `social-stories-creator` are the same project.

## Not blocked by this

E34.1 (merged `bf70841`, P6-GH-15 closed) and E34.3 (merged `aa6cf12`) are complete and unaffected.
Nothing about this escalation reopens them. M34 can still close on two of three epics if the Phase
Chat elects to descope E34.2, though that would leave the phase acceptance criterion open.

## Resolution

**Resolved 2026-07-29 by direct CFO instruction to the Phase Chat**, in-session: *"the only thing
I need is to drop `fieldledger-assesment` as that was a screening project."*

Answering the four numbered questions:

1. **Removed, not deprioritized — and yes, a phase spec amendment.** `fieldledger-assesment` is
   dropped entirely: no roll-forward path is owed for it, and it is not carried as a recorded,
   non-blocking deferral. The phase spec is bumped to **v1.2.0**, removing it from Executive
   Summary item 2, §P10.2, §Milestones→M34 (Goal + E34.2), and the phase Acceptance Criteria. The
   Milestone spec carries the matching amendment (**Amendment A1**).
2. **Not confirmed, and not acted on.** The CFO's instruction addressed only the removal — your
   observation that `social-stories-builder` doesn't exist while `social-stories-creator` does was
   correct to flag and correct not to resolve unilaterally. It is not added to E34.2's scope by
   this resolution.
3. **Not in M34** — unanswered by design, not by oversight. Whether a mid-inception,
   already-v7.0.0 project belongs in a "dormant enrolled projects" epic at all is exactly the kind
   of premise question you were right to escalate rather than absorb; it stays open.
4. **Not routed.** No Steering Note, Creation Chat session, or later-phase placement is decided
   here. M34 assumes nothing about the "personal platform," per your own recommendation.

**This was resolved as a Phase Chat decision, not escalated further to HQ**, despite touching a
phase Acceptance Criterion: the CFO — the authority HQ Chat's process ultimately serves — gave the
instruction directly, in-session, to the Phase Chat, on a narrow, unambiguous, scope-*reducing*
question (drop one named project; add nothing). This is treated as equivalent in kind to the
CFO-ratified decisions Creation Chat sessions record directly (SN-23, SN-24) rather than requiring
a separate HQ round-trip to ratify what the CFO already stated plainly. Flagged here rather than
silently normalized — this is a real routing choice, not the only correct one, and it is
consistent with the framework's open carry-forward **P9-GH-1** (the merge-authorization/routing
hole at Milestone→Phase and Phase→HQ), which this moment is arguably an instance of. Worth HQ's
attention if this pattern recurs.

**E34.2 is unblocked** — proceed to author its spec and starter against the amended Milestone
spec's project set (`courtis`, `Getawayinsured2023`, `footboard`). Your escalation was the correct
call: the project set is not a Milestone-Chat variable, and you were right not to absorb any of
its four questions unilaterally.
