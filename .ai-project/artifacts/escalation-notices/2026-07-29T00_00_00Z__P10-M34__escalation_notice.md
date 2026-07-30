---
type: escalation-notice
milestone: M34
issued_by: Milestone Chat (P10-M34)
issued_to: Phase Chat (P10)
date: 2026-07-29
status: open
blocks: E34.2 planning
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
