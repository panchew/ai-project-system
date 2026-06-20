---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-06-19T00:00:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-6
    severity: high
    title: M18 merge pending — PR #77 authorized, not yet executed
  - id: SN-7
    severity: medium
    title: Ongoing Creation Chat role not yet delivered — M18 only covered bootstrap half
  - id: SN-8
    severity: medium
    title: No governance concept for bouncer work (Layer 8 manual interventions)
decisions:
  - M19 scope includes two epics — Bugfix Workflow AND ongoing Creation Chat artifacts
  - Bouncer Work log artifact added to M19 scope alongside Steering Note and Progress Digest schemas
  - Product vision confirmed — Creation Chat is the single visible human interface; all governance runs below it as background agents
  - M19 is the natural next execution step following M18 closure
---

# Steering Note — Creation Chat to HQ Chat

## Purpose

Weekly review session of 2026-06-19. This Steering Note closes the session and
hands off to HQ Chat with updated scope for M19.

---

## Concerns for HQ Triage

### SN-6 — M18 merge pending [HIGH]

PR #77 (`milestone/M18 → phase/P4`) was authorized by Phase Chat on 2026-06-20.
It has not been merged. `phase/P4` is 6 commits behind `milestone/M18`.

**Required action:** Authorize and execute the merge of PR #77. M19 MUST branch
from `phase/P4` after this merge.

### SN-7 — Ongoing Creation Chat role not delivered [MEDIUM]

M18 (Inception Artifacts) delivered the **bootstrap half** of the Creation Chat:
the Genesis template, the Level 0 definition in `chat-hierarchy.md`, and the
updated `start-a-project.md`. What was not delivered — and is needed to complete
the Creation Chat definition — is the **ongoing half**:

- **Steering Note** artifact schema (Creation Chat → HQ direction changes, concerns)
- **Progress Digest** artifact schema (HQ → Creation Chat periodic status)
- **Re-instantiation ritual** (how to reset the Creation Chat session while
  preserving continuity via artifacts)
- **Bouncer Work log** artifact (see SN-8)

These are not optional polish — without them the Creation Chat is a one-shot
bootstrap tool, not the permanent institution it is designed to be.

**Decision:** Add a second epic to M19 covering these artifacts. M19 becomes
the milestone that closes both the last P4 success criterion (Bugfix Workflow)
and the Creation Chat definition.

### SN-8 — No governance concept for bouncer work [MEDIUM]

"Bouncer work" is Layer 8 manual intervention triggered by real-life operation
of a system being built: fixing corrupt or inconsistent data, fulfilling direct
user requests, one-off console operations — the gap between what the system does
and what reality demands. This is distinct from the Bugfix Workflow (which targets
code defects and produces commits).

**The problem:** Bouncer work currently has no home in the governance system.
It happens, it takes real time, and then it disappears. No record, no pattern
detection, no path to formalization.

**The intended flow:**
```
Real-life operation
  → bouncer work happens (manual intervention, no commit)
    → logged in Bouncer Work log (lightweight record)
      → pattern detected (same thing 3+ times?)
        → Steering Note to HQ
          → formal Epic (automate the fix, close the gap)
```

**Decision:** Include a **Bouncer Work log** artifact as part of M19's Creation
Chat ongoing artifacts epic. It is the lightweight record that sits between a
loose chat observation and a formal Steering Note — the first step of the pattern
detection loop.

---

## Decisions Already Made

Binding. Not for HQ to re-debate.

1. **M19 scope = two epics:**
   - E19.1: Bugfix Workflow (SLA tracking, Deployment Authorization artifact,
     post-mortem generation for Critical/High) — the last undelivered P4
     success criterion
   - E19.2: Creation Chat ongoing artifacts (Steering Note schema, Progress
     Digest schema, Bouncer Work log, re-instantiation ritual)

2. **Bouncer Work log is part of M19 scope** — lightweight artifact, not a
   full governance document. Designed to require minimal friction so it actually
   gets used during real-life operation.

3. **Product vision: Creation Chat is the single visible human interface.**
   All governance (HQ, Phase, Milestone, Epic) runs as background agents
   communicating via artifacts. Design decisions at every level should optimize
   for this: complexity invisible to the user, only decisions and outcomes surface.
   The Progress Digest in particular must be high-signal, low-noise — the user
   should not need to dig into phase/milestone artifacts to understand project state.

4. **M19 is the natural next execution step** — no new milestones or phases
   needed before it. The cascade is: this Steering Note → HQ authorizes M18
   merge + opens M19 → Phase Chat plans → Milestone Chat plans → Epic execution.

---

## Carry-Over Open Items (not blocking M19)

From prior milestones, for Phase Chat triage:
1. Stale P4 roadmap status (`docs/roadmap/overview.md`)
2. Stale `Next Steps` in `P4__phase-spec.md`
3. `pytest` not in project dependencies
4. CFO Dashboard deferred by design

---

## Next Action

HQ Chat should:
1. Authorize and execute PR #77 merge (SN-6)
2. Instruct Phase Chat to open M19 with the two-epic scope defined above
3. Pass the product vision (decision 3) to Phase Chat as a design constraint
   so it propagates into Epic specs
