---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-07-12T00:00:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-19
    severity: medium
    title: Delivery Authorization blocks survived the SN-13 reconciliation in the template/systems tier — retire them on the happy path
decisions:
  - "The Delivery Authorization ceremonial block is noise in the CFO's flow and is to be retired on the happy path; the in-chat merge authorization (PSG §1A gate scoping / §11.6) is preserved unchanged."
---

# Steering Note — Creation Chat to HQ Chat

## Purpose

This note hands HQ a CFO friction report with a verified root cause: the Epic /
Milestone **Delivery Authorization** blocks still mandated by the starter templates
contradict the SN-13 default-accept model the normative tier already codified in P6.
The CFO wants them removed; verification shows removal is a docs-only reconciliation,
the same shape as E25.6. Proposed vehicle: a fourth epic in M28.

---

## Concerns for HQ Triage

### SN-19 — Delivery Authorization blocks missed the SN-13 reconciliation [MEDIUM]

**Detail:** The CFO reports the "Epic Delivery Authorization" artifact causes noise
and friction in his flow (surfaced reading the P7 Phase Execution Chat Starter,
which carries a "Milestone Delivery Authorization Format" section inherited from
the template).

Verified against v5.1.0 (PSG v2.3.0 / AOG v2.6.0):

- **The normative tier already demoted it.** PSG §1A's gate-scoping note (under
  §11.6 Default-Accept) states that for a clean Epic the review acknowledgment, HQ
  decision, and delivery authorization are **in-chat acts — no artifact is
  produced**; explicit authorization before merge still applies but "is an in-chat
  act, not an artifact."
- **The template/systems tier was never reconciled.**
  `governance/templates/milestone-execution-chat-starter.md` (§"Epic Delivery
  Authorization", ~line 157) still mandates a formal `EPIC DELIVERY AUTHORIZATION`
  block per accepted Epic and requires it in Completion Requirements;
  `governance/templates/phase-execution-chat-starter.md` (~line 156) does the same
  at Milestone level. Mirrors exist in `governance/systems/`
  (milestone-execution-chat-starter.md, phase-execution-chat-starter.md,
  hq-execution-chat-starter.md).
- **AOG residue:** AOG §1A step 6 and two §10 enforcement bullets still read "MUST
  issue explicit Epic Delivery Authorization before PR/merge" — artifact-shaped
  wording that PSG's gate-scoping note already superseded in substance.
- **Live instance:** the issued P7 starter
  (`docs/phases/P7__Agentic_Execution_and_Default_On_Visuals/P7__phase-execution-chat-starter.md`,
  §"Milestone Delivery Authorization Format") reproduces the stale template section.

E25.2's framework-wide default-accept reconciliation caught the Review Decision and
Epic Review Seal but not the Delivery Authorization blocks in the template tier.
This is a missed-reconciliation defect, not a new design question.

**Required action:** Schedule a docs-only reconciliation epic (E25.6-shaped):

1. Remove the Delivery Authorization sections and their Completion Requirements
   checklist lines from both starter templates and the `governance/systems/`
   mirrors; fold the load-bearing **merge instruction** into each starter's
   execution instructions.
2. Reword AOG §1A step 6 and the §10 enforcement bullets to the in-chat
   authorization language PSG §1A gate scoping already uses (authorization
   preserved; artifact retired).
3. Amend the live P7 starter via the GH-9 mid-flight amendment path (amend the
   governing artifact, note the change, notify running sessions' parents).

**Proposed vehicle:** a fourth epic in **M28 — Governance Reconciliations**
(same size and shape as E28.1–E28.3). HQ owns the scope decision; adding it to
M28 requires an amendment to the P7 phase spec's M28 scope before the M28
Milestone Chat opens.

---

## Decisions Already Made

1. **Retire the ceremonial block; keep the gate.** The Delivery Authorization
   block is noise in the CFO's flow and goes away on the happy path. The
   **in-chat merge authorization is preserved unchanged** — the CFO still says
   "merge it" before any PR merges (PSG §1A gate scoping / §11.6; the harness
   enforces human merge authorization regardless). Removal of the artifact, not
   of the authorization.

---

## Carry-Over Open Items

None.

---

## Next Action

HQ Chat should:

1. Accept SN-19 and decide the vehicle — recommended: add a fourth reconciliation
   epic to M28's scope in the P7 phase spec (amendment, since P7 is open).
2. Ensure the epic covers all three surfaces: templates + systems mirrors, AOG
   §1A/§10 wording, and the live P7 starter amendment (GH-9 path).
3. Register the concern in the roadmap under the P7 entry so the registry stays
   the single source of truth.
