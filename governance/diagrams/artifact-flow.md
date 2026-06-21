# Artifact Flow Diagram

This diagram shows every artifact that crosses a chat boundary in the AI Project System —
what opens each chat, what closes it, and what travels between levels.

**Legend**
- `✅ exists` — template or schema already defined in governance
- `⬜ missing` — identified as needed, not yet defined

---

## Chat Lifecycle Model

Every chat except the two extremes has two stages:

```
Stage 1 — Planning
  Opens with:  Execution Chat Starter (from parent)
  Does:        Produces specs and child Starters
  Closes when: All child Starters are produced and accepted by parent

Stage 2 — Oversight
  Does:        Receives Completion Notices from direct children
               Issues Review Decisions (accept / reject)
               Opens own PR to parent branch
               Merges own PR after parent Review Decision Accept
               Sends Delivery Notice
  Closes when: Own PR is merged and Delivery Notice is sent
```

**HQ Chat** has Stage 1 only — master is the final branch, no PR to open.
**Epic Chat** has Stage 2 only — no children to plan, goes straight to execution.
**Phase Chat and Milestone Chat** have both stages.

---

## Full Hierarchy

```
+-------------------------------------------------------------+
|  Governance Framework                                       |
|  (ships the Genesis artifact — one per framework install)   |
+---------------------------+---------------------------------+
                            |  ⬜ Genesis
                            v
+-------------------------------------------------------------+
|  Creation Chat                                              |
|  Permanent · Authority-free · Vision / concerns / brainstorm|
+------+--------------------------------------+---------------+
       |  ⬜ Project Brief                    |
       |  (inception stage closes here;       |  ⬜ Steering Note
       |   governance enabled on acceptance)  |  (ongoing — concern,
       v                                      |   direction change)
+---------------------------------------------v---------------+
|  HQ Chat                                                    |
|  Stage 1 only · Strategic control · No PR (master is final) |
+------+--------------------------------------+---------------+
       |  ✅ Phase Execution Chat Starter     |
       v                                      |  ✅ Review Decision
+---------------------------------------------v---------------+
|  Phase Chat                                                 |
|  Stage 1: Produces Milestone Starters                       |
|  Stage 2: Aggregates Milestone completions                  |
|           Opens PR (phase/* → master)                       |
|           Merges on HQ Accept                               |
+------+--------------------------------------+---------------+
       |  ✅ Milestone Execution Chat Starter |
       v                                      |  ✅ Review Decision
+---------------------------------------------v---------------+
|  Milestone Chat                                             |
|  Stage 1: Produces Epic Starters                            |
|  Stage 2: Aggregates Epic completions                       |
|           Opens PR (milestone/* → phase/*)                  |
|           Merges on Phase Accept                            |
+------+--------------------------------------+---------------+
       |  ✅ Epic Execution Chat Starter      |
       v                                      |  ✅ Review Decision
+---------------------------------------------v---------------+
|  Epic Chat                                                  |
|  Stage 2 only · Execution · Code                            |
|  Opens PR (epic/* → milestone/*)                            |
|  Merges on Milestone Accept                                 |
+-------------------------------------------------------------+
```

---

## Upward Flow (child → parent)

Every chat signals completion by sending a Completion Notice to its parent.
The parent reviews and responds with a Review Decision.
After a positive decision and PR merge, the child sends a Delivery Notice.

```
Epic Chat        ---> ✅ Completion Notice ---> Milestone Chat
Milestone Chat   ---> ✅ Completion Notice ---> Phase Chat
Phase Chat       ---> ✅ Completion Notice ---> HQ Chat

Epic Chat        ---> ✅ Delivery Notice   ---> Milestone Chat
Milestone Chat   ---> ✅ Delivery Notice   ---> Phase Chat
Phase Chat       ---> ✅ Delivery Notice   ---> HQ Chat
```

---

## Downward Flow (parent → child)

A parent opens a child chat by sending it an Execution Chat Starter.
After reviewing a Completion Notice, the parent sends a Review Decision back.

```
HQ Chat         ---> ✅ Phase Execution Chat Starter      ---> Phase Chat (opens it)
Phase Chat      ---> ✅ Milestone Execution Chat Starter  ---> Milestone Chat (opens it)
Milestone Chat  ---> ✅ Epic Execution Chat Starter       ---> Epic Chat (opens it)

HQ Chat         ---> ✅ Review Decision ---> Phase Chat
Phase Chat      ---> ✅ Review Decision ---> Milestone Chat
Milestone Chat  ---> ✅ Review Decision ---> Epic Chat
```

---

## Cross-Hierarchy Flow (Creation <-> HQ)

These artifacts operate outside the execution cycle.
They have no fixed frequency — triggered by events or human judgment.

```
Creation Chat  ---> ⬜ Project Brief    ---> HQ Chat   (once at inception; amended on major pivots)
Creation Chat  ---> ⬜ Steering Note    ---> HQ Chat   (any time: concern, direction change)
HQ Chat        ---> ⬜ Progress Digest  ---> Creation  (periodic: aggregated milestone/epic status)
```

---

## Summary Table

| Artifact | Direction | Sender | Receiver | Status |
|---|---|---|---|---|
| Genesis | Framework → Creation | Governance framework | Creation Chat | ⬜ missing |
| Project Brief | Creation → HQ | Creation Chat | HQ Chat | ⬜ missing |
| Steering Note | Creation → HQ | Creation Chat | HQ Chat | ⬜ missing |
| Progress Digest | HQ → Creation | HQ Chat | Creation Chat | ⬜ missing |
| Phase Execution Chat Starter | HQ → Phase | HQ Chat | Phase Chat | ✅ exists |
| Milestone Execution Chat Starter | Phase → Milestone | Phase Chat | Milestone Chat | ✅ exists |
| Epic Execution Chat Starter | Milestone → Epic | Milestone Chat | Epic Chat | ✅ exists |
| Completion Notice | Child → Parent | Any child chat | Parent chat | ✅ exists |
| Review Decision | Parent → Child | Any parent chat | Child chat | ✅ exists |
| Delivery Notice | Child → Parent | Any child chat | Parent chat | ✅ exists |

**4 artifacts missing. 6 artifacts exist.**

---

## What This Exposes

**The two-stage lifecycle is not documented.** Phase and Milestone Execution Chat Starters
currently define these chats as planning-only and explicitly state they do not open PRs
or merge. This is wrong — they manage their own branch lifecycle in Stage 2.
The starters need a Stage 2 section added: Completion Notice intake, Review Decision
issuance, PR creation, and merge instructions.

**The missing artifacts are all at the top of the hierarchy** — no bootstrap (Genesis),
no inception-to-governance handoff (Project Brief), no ongoing steering channel
(Steering Note), no upward visibility feed (Progress Digest). These are the M15 scope.
