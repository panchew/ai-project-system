---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-06-27T00:00:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-13
    severity: medium
    title: Default-accept delivery model — Review Decision is the exception path, not the happy path
decisions:
  - On delivery, the parent chat auto-accepts and proceeds if DoD, acceptance criteria, and spec alignment are met. No explicit acceptance artifact is required on the happy path.
  - The Review Decision artifact is reserved for the exception path only — when DoD is not fully met, acceptance criteria are off, scope drifted, or quality does not pass.
  - Silence is acceptance. The absence of a raised Review Decision means the parent chat accepted the delivery and authorized the next step.
  - The Execution Authorization concept collapses into this model — no objection raised within review equals authorized to proceed. An explicit authorization artifact is not needed for the happy path.
  - This applies at every level: Milestone Chat auto-accepts Epic deliveries; Phase Chat auto-accepts Milestone deliveries; HQ Chat auto-accepts Phase deliveries. The exception path is the same at every level.
---

# Creation Chat Steering Note — Default-Accept Delivery Model

## Purpose

M20 execution revealed that the governance's implicit model required explicit
back-and-forth acceptance on every delivery, creating unnecessary round-trips
between parent and child chats. The correct model, confirmed by CFO during
M20 debrief, flips the default: proceed unless there is a reason not to.
This note captures the binding decisions for HQ to use when planning the
Delivery Notice receipt protocol (P5-GH-10).

---

## Concerns for HQ Triage

### SN-13 — Default-accept delivery model

**Severity:** Medium

**Observation:**

During M20, the Milestone Execution Chat received Epic Delivery Notices and
proceeded to auto-accept, merge the Epic branch, and declare closure without
escalating to the parent chat for explicit acceptance. This was initially
flagged as out-of-governance. On reflection, it is correct behavior — and
more efficient. The governance simply did not specify it.

The current implicit model requires an explicit acceptance artifact on every
delivery, which creates mandatory back-and-forth even when everything is
in order. This burns tokens and adds friction to the happy path.

**Binding decisions:**

1. **Default is accept.** When a Delivery Notice arrives, the parent chat
   reviews the deliverables against DoD, acceptance criteria, and the governing
   spec. If everything is in order, the parent proceeds immediately — merges,
   closes, authorizes the next step. No artifact is produced on the happy path.

2. **Review Decision is the exception path only.** A Review Decision artifact
   is issued only when the parent chat finds a valid reason to not accept:
   - Definition of Done not fully met
   - Acceptance criteria not satisfied
   - Scope drifted beyond the spec
   - Quality does not pass
   - Conflicts or blockers discovered
   In all other cases, no Review Decision is issued — the happy path is silent.

3. **Silence is acceptance.** The absence of a raised Review Decision within
   the parent chat's review window means the delivery is accepted and the
   next step is authorized. No explicit sign-off artifact is required.

4. **Execution Authorization collapses into this model.** On the happy path
   there is nothing to authorize — the auto-accept IS the authorization.
   An explicit "Execution Authorization" artifact is only meaningful when
   a prior exception was raised and then resolved. HQ should plan the
   authorization artifact as an exception-path resolution artifact, not as
   a standard happy-path handshake.

5. **Applies at every level uniformly:**
   - Milestone Chat auto-accepts Epic deliveries when criteria are met
   - Phase Chat auto-accepts Milestone deliveries when criteria are met
   - HQ Chat auto-accepts Phase deliveries when criteria are met
   The exception path (Review Decision → revision → re-delivery) is identical
   at every level.

**Analogy:** A CI/CD pipeline. Green means proceed — no human sign-off needed.
Red means stop — a Review Decision is required. You do not sign off on every
green build; you act only when it is red.

**Required action from HQ:**

1. Refine P5-GH-10 scope: the Delivery Notice receipt protocol should specify
   the default-accept model explicitly, so parent chats know they are authorized
   to proceed without asking.
2. Reframe the "Execution Authorization" artifact: it is an exception-path
   resolution artifact (issued after a Review Decision is resolved), not a
   standard handshake on every delivery.
3. Ensure the Phase and Milestone Execution Chat Starter templates reflect this
   in their Stage 2 protocol sections.

---

## Decisions Already Made

- Default-accept: parent chat proceeds on delivery unless a reason to reject exists.
- Review Decision: exception path only — DoD, acceptance criteria, scope, or quality failure.
- Silence is acceptance: no artifact needed on the happy path.
- Execution Authorization: exception-path resolution artifact, not a happy-path handshake.
- Model applies uniformly at all levels (Milestone, Phase, HQ).

---

## Carry-Over Open Items

None beyond SN-13.

---

## Next Action

HQ Chat refines P5-GH-10 during M21 planning to reflect the default-accept
model, and reframes the Execution Authorization artifact accordingly.
