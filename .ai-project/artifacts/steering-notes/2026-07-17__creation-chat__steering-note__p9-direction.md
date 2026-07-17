---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-07-17T21:00:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-22
    severity: high
    title: P9 direction — context handling and token efficiency as the spine; measurement-driven model-tier policy, dual agentic mode for working levels, manual-mode model guardrail
decisions:
  - "Context handling is the major pillar the project should focus on now: make token use as smart and effective as possible. This is the spine of P9."
  - "The original model-tier assumption — local models only at the Epic level, frontier everywhere else — failed in practice: token burn exhausted premium quota and left the CFO without frontier reasoning. The audit of when to use frontier/paid models vs local resources starts with measurement, so policies are realistic (evidence before policy)."
  - "Agentic mode must cover all working levels: Phase, Milestone, and Epic Chats become dual (manual or agentic). Creation Chat and HQ Chat remain manual at all times. Mode is chosen and set one by one, per instance, as part of the P9 work. Agentic-by-default is the aspiration, but only when everything is ready — there is not yet enough evidence that a full Phase can be carried forward agentically. Agentic mode also needs to decide when to go paid vs when to go local."
  - "Manual-mode startup guardrail: at the start of each manually run chat, verify the right model is being used by the right level as defined in .ai-project.yml. On a mismatch, refuse to proceed. How the mapping is defined/implemented is decided as part of P9."
  - "ComfyUI visual-artifact generation remains relevant but is not a blocker and not the P9 spine. This revises the 2026-07-17 Progress Digest, which recorded the ComfyUI investigation as 'likely P9's spine'."
  - "System-level participant: SN-21 stands as written (executor System HQ, no expansion of authority). The CFO's larger vision of a 'mighty' System Chat governing the local computer above all Creation Chats is pinned as a vision item — it shares the vision of the full working system — but is not scoped here."
  - "System Chat re-instantiation: the CFO will need an artifact to spawn the System Chat over and over — ideally once a day. Analogous to the Creation Chat's Genesis seed; a concrete input for SN-21 canonization triage."
  - "Overarching goal: get the CFO's system up and running so progress happens in each and every governed project, not just this one."
---

# Creation Chat Steering Note — P9 Direction

## Purpose

Direction-setting session held in the Creation Chat on 2026-07-17, CFO present.
The CFO believes the project has matured enough to carry any project forward and
make a meaningful impact in their general system tasks. This note carries the
resulting decisions to HQ so P9 scoping can open on the right spine.

---

## Concern for HQ Triage

### SN-22 — P9 spine: context handling and token efficiency [HIGH]

Severity confirmed by the CFO (2026-07-17); the decisions are the CFO's.

**Detail:** The P9 spine is context handling — making token use as smart as
possible. Three workstreams flow from it, per the CFO's decisions above:

1. **Measurement-first model-tier audit.** Instrument actual token burn per
   level/task so the frontier-vs-local policy is grounded in evidence, not the
   failed Epics-only-local assumption.
2. **Dual agentic mode for working levels.** Phase, Milestone, and Epic Chats
   gain a manual/agentic switch, set per instance during P9. Creation Chat and
   HQ Chat stay manual permanently. Agentic mode must itself decide paid vs
   local. Agentic-by-default is deferred until evidence supports it.
3. **Manual-mode model guardrail.** Each manually started chat verifies its
   model against the level→model mapping in `.ai-project.yml` and refuses to
   proceed on mismatch. Mapping definition and mechanism are P9 design work.

**Required action:** HQ acknowledges SN-22 and opens P9 scoping with this as
the spine. ComfyUI investigation (SN-20 Carry-Over 3 resolution) continues as
a non-blocking track. SN-21 canonization remains at HQ's triage for P9 or a
standalone epic, unchanged — with one added input from the CFO: a
re-instantiation artifact (seed) so the System Chat can be spawned recurrently,
ideally once a day.

---

## Next Action

1. HQ Chat acknowledges SN-22 and records the Progress Digest revision
   (ComfyUI demoted from likely-spine to non-blocking track).
2. P9 scoping session opens with context handling / token efficiency as the
   spine and the three workstreams above as candidate scope.
3. Carry-forwards P8-GH-1/2/3 and SN-21 canonization enter the same scoping
   triage.
