---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-06-25T00:00:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-12a
    severity: medium
    title: Artifact scope adjacency — chats produce only for adjacent levels
  - id: SN-12b
    severity: medium
    title: Hierarchical communication — information travels one level at a time; spec file is the downward channel
decisions:
  - Each chat level produces artifacts only for its direct parent or direct children. No grandchild artifacts (e.g. Phase Chat must not produce Epic Execution Chat Starters). No grandparent artifacts.
  - Upward communication is always 1-to-1. Any level has exactly one parent. Escalations and completion notices travel up one level; the receiving level decides whether to absorb or escalate further.
  - Downward communication is 1-to-many but solved by the spec file, not by broadcasting. A parent amends its own spec; all children read from that same source at any time, including mid-execution.
  - Mid-flight updates — if children are already running when a directive changes, the parent escalates UP rather than reaching into running sessions it does not control.
  - The level spec file has a dual role — planning artifact (what was planned) and live contract (what governs execution including amendments). It is the canonical downward communication channel.
---

# Creation Chat Steering Note — Hierarchical Communication and Artifact Scope

## Purpose

Two governance principles emerged from observing live Phase and Milestone Execution Chat
behavior and from a Creation Chat session on 2026-06-25. Both are binding design decisions
that must inform how HQ scopes the P5 milestones addressing GH-8 and GH-9.

---

## Concerns for HQ Triage

### SN-12a — Artifact scope adjacency

**Severity:** Medium

**Observation:**

In practice, Phase Execution Chats have been producing Epic Execution Chat Starters —
skipping the Milestone Chat layer entirely. This collapses the hierarchy, removes a review
gate, and gives Phase Chat authority over artifacts that belong to Milestone Chat's scope.

**Binding decision:**

Each chat level produces artifacts only for its **direct parent** or **direct children**.

| Chat | May produce | Must NOT produce |
|------|-------------|-----------------|
| Phase Execution Chat | Milestone Specs, Milestone Execution Chat Starters | Epic Specs, Epic Execution Chat Starters |
| Milestone Execution Chat | Epic Specs, Epic Execution Chat Starters | Milestone Specs (parent's job), code (grandchildren's job) |
| Epic Execution Chat | Code, tests, PRs | Epic Specs (parent's job), Milestone Specs (grandparent's job) |

Violation of this rule means a chat is either bypassing a review gate (grandchild production)
or overreaching into its parent's authority (grandparent production). Both are process failures.

**Required action from HQ:**

Register P5-GH-8 and plan a milestone that adds an explicit scope adjacency rule to the
critical rules section of both the Phase and Milestone Execution Chat Starter templates,
and to AOG §3.6 and §3.7.

---

### SN-12b — Hierarchical communication and the spec file as downward channel

**Severity:** Medium

**Observation:**

The governance model defines artifact types for upward communication (Escalation Notices,
Completion Notices) but does not define how downward communication propagates — particularly
when one parent needs to reach multiple concurrent children (e.g. a Milestone Chat with
three running Epic Chats).

**Binding decisions:**

1. **Upward communication is always 1-to-1.** Every level has exactly one parent. An Epic
   Chat escalates to its Milestone Chat. A Milestone Chat escalates to its Phase Chat. The
   receiving level decides whether to absorb the issue or escalate further. No level skips
   its parent to reach a grandparent directly.

2. **Downward communication is solved by the spec file, not by broadcasting.** When a
   parent needs to communicate a directive, amendment, or correction to its children, it
   amends its own spec file. Children — including those already mid-execution — read from
   that spec at any time. One write, many readers. No separate message per child.

3. **The level spec file has a dual role:**
   - *Planning artifact* — what was planned at the start of the session
   - *Live contract* — the authoritative state of scope, constraints, and directives,
     including any amendments issued after child sessions began

4. **Mid-flight updates:** If a directive changes after child sessions are already running,
   the parent does not attempt to reach into those sessions. It amends the spec and, if the
   change is blocking, escalates UP to the parent chat to decide whether to pause or cancel
   the affected children. Downward reach into running sessions is not permitted.

**Required action from HQ:**

Register P5-GH-9 and plan a milestone that:
- Adds the 1-to-1 upward / spec-as-channel downward rule to AOG and PSG
- Defines when a mid-flight spec amendment requires child session pause vs. continue
- Adds guidance to Phase and Milestone Execution Chat Starter templates on how to
  issue amendments (amend the spec, note the change, notify parent chat)

---

## Decisions Already Made

- Artifact production is bounded by adjacency — no grandchild or grandparent artifacts.
- Upward communication: 1-to-1, one level at a time.
- Downward communication: spec file is the channel; no broadcasting.
- Mid-flight updates escalate UP, not into running sessions.
- The level spec file is both a planning artifact and a live contract.

---

## Carry-Over Open Items

None beyond SN-12a and SN-12b.

---

## Next Action

HQ Chat registers P5-GH-8 (artifact scope adjacency) and P5-GH-9 (hierarchical
communication) and folds them into P5 milestone planning. Both are process-hardening
items in Bucket A and are executable once the phase spec is open.
