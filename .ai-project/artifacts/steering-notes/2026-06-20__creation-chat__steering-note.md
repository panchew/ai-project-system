---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-06-20T16:00:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-9
    severity: medium
    title: CFO scope direction entered E19.2 out-of-band (pasted starter edit, no Steering Note)
decisions:
  - The CFO PR review gate is adopted into E19.2 scope (Constraint 2 + Functional Requirement 5). Layer 8 must be able to see PR changes before a merge; configurable, ON by default.
---

# Steering Note — Creation Chat to HQ Chat

## Purpose

Closes the 2026-06-20 Creation Chat working session. It records a binding CFO decision —
adopt the CFO PR review gate into Epic E19.2 — and flags the irregular channel through
which that decision first reached the Epic, so HQ can confirm the formalization and harden
the process.

---

## Concerns for HQ Triage

### SN-9 — CFO scope direction entered E19.2 out-of-band [MEDIUM]

**Detail:** During E19.2 execution the CFO (Layer 8, operating Creation Chat) wanted a
"CFO PR review gate" — Layer 8 sees a PR's changes before it merges. Rather than cascading
this as a Steering Note (Creation Chat → HQ → Phase → Milestone spec amendment), Creation
Chat produced a *revised Epic Execution Chat Starter* with a new "Constraint 2," and the
CFO pasted it into the already-running E19.2 Epic chat. The Epic Agent implemented it
correctly: `cfo_review_gate` in `.ai-project.yml`, merge-ready PRs surfaced in the Progress
Digest "Open Decisions" section, a "CFO PR Review Gate" section in
`governance/systems/creation-chat-guide.md`, and tests in
`tests/test_ongoing_artifacts.py`. The work is sound and the directive is legitimate
top-level authority — but it bypassed the Milestone Chat (which owns epic starters) and
left no audit trail, so on first review it was indistinguishable from an Epic Agent
self-authorizing scope.

**Required action:** Confirm the formalization path the Milestone Chat has taken (Steering
Note → E19.2 spec v1.1 amendment → Accept), and ratify, at the system level, the rule that
scope direction from Creation Chat/CFO must flow as a Steering Note + spec amendment, never
as a pasted starter edit. The process-hardening ask is also carried in the M19 Escalation
Notice for Phase Chat.

---

## Decisions Already Made

Binding. Not for HQ to re-debate.

1. **The CFO PR review gate is part of E19.2 scope.** Layer 8 must be able to see a PR's
   changes before merge. It is a configurable gate (`cfo_review_gate: enabled | disabled`
   in `.ai-project.yml`), ON by default, additive to — not a redesign of — the existing
   merge-authorization authority model. Captured as E19.2 Constraint 2 + Functional
   Requirement 5 in spec v1.1.

---

## Carry-Over Open Items

1. System-level rule that Creation Chat/CFO scope direction must cascade as a Steering
   Note + spec amendment (not a pasted starter edit) — being raised to Phase/HQ via the
   M19 Escalation Notice; no action blocking M19.

---

## Next Action

HQ Chat should:
1. Acknowledge SN-9 and the SN-9 decision (CFO PR review gate adopted into E19.2).
2. Confirm the Milestone Chat's formalization (E19.2 spec v1.1 → Accept) is the correct
   remedy rather than a rejection of the as-built work.
3. Forward the procedural rule (Steering-Note-not-pasted-starter) to Phase Chat for
   incorporation into the operating guidelines, per the M19 Escalation Notice.
