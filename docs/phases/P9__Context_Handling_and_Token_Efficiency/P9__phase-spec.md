---
phase: P9
name: Context Handling and Token Efficiency
status: active
start_date: 2026-07-17
planned_end_date: 2026-08-07
version: 1.0.0
---

# Phase P9: Context Handling and Token Efficiency

## Executive Summary

The framework is functionally complete through P8 — every chat level works, visual artifacts
are real, and the governance loop closes phases cleanly. What failed in practice is the **cost
model underneath it**: the original model-tier assumption (local models only at the Epic level,
frontier everywhere else) exhausted the CFO's premium token quota and left them without frontier
reasoning when it mattered. Policies were written before evidence existed.

**P9's spine is context handling / token efficiency: make token use as smart and effective as
possible.** Per SN-22 (Creation Chat, 2026-07-17, all decisions CFO-ratified), three workstreams
flow from the spine:

1. **Measurement-first model-tier audit** — instrument actual token burn per chat level and task
   type, then derive the frontier/paid-vs-local policy from evidence, not assumption.
2. **Dual manual/agentic mode for working levels** — Phase, Milestone, and Epic Chats gain a
   per-instance manual/agentic switch; Creation Chat and HQ Chat remain manual permanently.
   Agentic mode must itself decide paid vs local.
3. **Manual-mode model guardrail** — every manually started chat verifies its model against the
   level→model mapping in `.ai-project.yml` and refuses to proceed on mismatch.

P9 also absorbs, at HQ's triage: **SN-21 canonization** (the system-level participant and its
`system_request`/`system_response` artifact pair, live in the field since 2026-07-16, plus the
CFO's daily System Chat re-instantiation seed) and the **P8-GH-1/P8-GH-3 documentation
reconciliations**. The ComfyUI precision investigation continues as a **non-blocking, CFO-side
track** — explicitly not the spine and not a blocker (SN-22, revising the 2026-07-17 Progress
Digest; see digest v1.1).

Overarching goal (SN-22): get the CFO's system up and running so progress happens in each and
every governed project — token efficiency is what makes running eight governed projects on one
machine and one quota sustainable.

Three milestones:

1. **M30 — Token Measurement & Model-Tier Audit** — evidence before policy.
2. **M31 — Dual-Mode Working Levels & Model Guardrail** — the mode switch, the paid-vs-local
   decision logic, and the manual-mode startup guardrail.
3. **M32 — System Participant Canonization & Governance Hygiene** — SN-21 canonization (schemas,
   hierarchy placement, authority boundary, daily seed) plus P8-GH-1/P8-GH-3 reconciliation.

---

## Vision

By the end of P9:

- ✅ **Token burn is measured, not guessed.** There is a committed measurement report showing
  actual token consumption per chat level and task type, including how much of it is governance
  corpus overhead.
- ✅ **The frontier-vs-local policy is evidence-grounded.** A recorded policy states when paid
  models are worth it and when local models suffice — replacing the failed Epics-only-local
  assumption — and `.ai-project.yml`'s `models:` mapping (currently stale: `remote:gpt-4o`,
  `remote:claude-3-5-sonnet`, `local:qwen2.5-coder`) is refreshed to match it.
- ✅ **Phase, Milestone, and Epic Chats are dual-mode.** Each instance can be started manual or
  agentic, chosen one by one; Creation Chat and HQ Chat are documented as manual-only,
  permanently. Agentic mode carries its own paid-vs-local decision mechanism.
- ✅ **Manual-mode chats refuse to run on the wrong model.** The startup guardrail checks the
  running model against the `.ai-project.yml` level→model mapping and refuses on mismatch.
- ✅ **The system-level participant is canonized.** `system_request`/`system_response` schemas
  are in the Artifact Communication Protocol (or a companion document), the participant's place
  relative to `chat-hierarchy.md` is decided and recorded, the authority boundary (execute, never
  decide; `status: escalated` for review/merge/scope) is normative, and a **System Chat
  re-instantiation seed** exists so the CFO can spawn the System Chat daily.
- ✅ **The P8 documentation debt is paid.** P8-GH-1 (stale opt-out prose) and P8-GH-3 (vestigial
  "Phase Delivery Notice" phrasing) are reconciled; P9's own planning documents never contained
  the vestigial phrase in the first place.

---

## Scope

### P9.1: Token Measurement & Model-Tier Audit (M30)

**Measurement first (evidence before policy — CFO-ratified).** Instrument and record actual
token consumption across the governance workflow: per chat level (Phase / Milestone / Epic, plus
HQ and Creation for the record), per task type (planning, execution, review, closure), and
governance-corpus overhead (how many tokens the loaded governance context itself costs each
chat). The mechanism is a design decision for the Milestone/Epic Chats — candidates include
harness/API usage logs, transcript token counting, or instrumentation in the orchestrator path —
HQ scopes the problem, not the resolution.

**Audit and policy derivation.** From the measurements, produce the model-tier audit: where do
frontier/paid tokens actually go, which of those expenditures needed frontier reasoning, and
which could a local model have carried? Output is a recorded frontier-vs-local policy (where it
lives — governance doc, yml-spec section, or both — is design work within the milestone) and a
refreshed `models:` mapping in this repo's `.ai-project.yml`.

**Evidence-driven context-load reduction.** If measurement shows the governance corpus is a
dominant per-chat cost (prior local-model work suggested the full corpus is roughly an order of
magnitude larger than the AOG+PSG core), scope reduction work — tighter per-level context
scoping, retrieval instead of full loading, caching — sized by what the evidence shows. This
epic is conditional in extent: measurement decides how much of it P9 needs.

### P9.2: Dual-Mode Working Levels & Model Guardrail (M31)

**The mode switch.** Phase, Milestone, and Epic Chats become dual: manual (a human-driven chat
session, as today) or agentic (driven by the orchestrator/runner path). Mode is chosen and set
**per instance, one by one** — agentic-by-default is explicitly deferred until evidence supports
it (SN-22: "there is not yet enough evidence that a full Phase can be carried forward
agentically"). Where the mode is declared (`.ai-project.yml`, the Execution Chat Starter, or
both) is design work. Creation Chat and HQ Chat are manual at all times — this is permanent
policy to be recorded normatively, not a deferral.

**Agentic paid-vs-local decision.** Agentic mode must itself decide when to spend paid/frontier
tokens and when to run local, consuming M30's evidence-grounded policy. This is the direct fix
for the failed static assumption: the decision moves from a hardcoded level→tier mapping to a
policy the agentic path applies per task.

**Manual-mode startup guardrail.** At the start of each manually run chat, verify the right
model is being used for the level as defined in `.ai-project.yml`; on mismatch, **refuse to
proceed**. How the level→model mapping is defined and how a chat can verify its own model are P9
design decisions (SN-22 leaves both open). The guardrail applies to all manually run chats,
including HQ and Creation.

**GPU-contention awareness.** Local execution (Ollama-served models) and ComfyUI contend for the
same 16 GB GPU (issue #126 context, P8 deferral reason). M31 does not resolve the scheduling
problem, but the paid-vs-local decision logic must not assume a local model is always loadable.

### P9.3: System Participant Canonization & Governance Hygiene (M32)

**SN-21 canonization (HQ triage decision: canonize now, in P9 — not observe-and-wait).**
Rationale: the pattern is live across all 8 governed projects on the CFO's machine, the CFO has
asked for a recurring re-instantiation seed, and SN-22's overarching goal (every governed
project makes progress) makes the system-level participant load-bearing. Work items, per SN-21's
required actions:
1. Add `system_request` / `system_response` schemas to the Artifact Communication Protocol or a
   companion system-participant document, with SN-21's storage and naming conventions.
2. Decide and record where the system-level participant sits relative to
   `governance/systems/chat-hierarchy.md` — new level, annex, or explicitly out-of-hierarchy
   with a pointer.
3. Record the authority boundary normatively: system agents execute within tool authority;
   review decisions, merge authorizations, and scope changes escalate to the human
   (`status: escalated` is mandatory for those).
4. **System Chat re-instantiation seed** — an artifact the CFO uses to spawn the System Chat
   recurrently, ideally daily; analogous to the Creation Chat's Genesis seed (CFO input via
   SN-22). SN-21's carry-over items (MCP write path, volume/sweep cadence) stay out of scope —
   they belong to ai-project-system-mcp's roadmap and future triage respectively.

**P8-GH-1 — stale opt-out prose (Medium).** AOG §16.5's source-repo sentence,
`governance/guides/visual-artifacts.md` §1 note and §6, and any sibling remnant still describe
this repo as opted out — contradicting the actual state since E29.2 (`enabled: true`, real
passing endpoint test, opt-out env var for the no-endpoint case). Reconcile all of it.

**P8-GH-3 — vestigial "Phase Delivery Notice" phrasing (Low).** PSG §5C's nine steps name no
such artifact — the Phase Closure Declaration is the delivery record — yet the phrase keeps
getting copy-pasted into planning docs (P8's phase spec, milestone spec, and both Execution
Chat Starters all carried it). Purge it from the templates and living documents it propagates
from. P9's own planning documents are written without it.

---

## Out of Scope

- **ComfyUI precision investigation / workflow building (SN-20 Carry-Over 3 resolution).**
  Continues as a **non-blocking, CFO-side track** (SN-22, demoting the Progress Digest v1.0
  projection). Not a P9 milestone; nothing in P9 blocks on it. If the investigation lands
  during P9, its outcome routes through Creation Chat / HQ as new input, not into a running
  milestone.
- **The "mighty" governing System Chat.** The CFO's larger vision of a System Chat governing
  the local machine above all Creation Chats is a **pinned vision item** (SN-22). SN-21's
  executor System HQ stands as written — no expansion of authority in P9.
- **Agentic-by-default.** Aspiration only; deferred until evidence supports carrying a full
  phase agentically (SN-22). P9 delivers the switch, not the default.
- **P8-GH-2 — machine-local visual-artifact hosting (Low).** Stays deferred on its recorded
  trigger: revisit only if cloud-reachable hosting is ever actually needed for this project.
  Not scoped into P9.
- **GPU scheduling between local LLMs and ComfyUI.** M31 must be aware of the contention
  (see P9.2) but resolving it is not P9 work.
- **The spin-off "software factory" project (SN-20 Carry-Over 2).** Future Creation Chat item,
  unchanged.
- **SN-21 carry-over items** — the MCP bridge write path (ai-project-system-mcp roadmap
  territory) and scheduled request sweeps/SLAs (future triage if volume grows).

---

## Milestones

### M30: Token Measurement & Model-Tier Audit

**Goal:** Measure actual token consumption per chat level and task type, audit where
frontier/paid tokens go versus where local models would have sufficed, and derive an
evidence-grounded frontier-vs-local policy plus a refreshed `models:` mapping.

**Indicative Epics** (the Milestone Chat owns final decomposition):
- **E30.1 — Token-burn instrumentation.** Build/choose the measurement mechanism and capture
  real per-level, per-task-type token data, including governance-corpus overhead per chat.
- **E30.2 — Audit report + policy derivation.** The committed measurement report, the
  frontier-vs-local policy, and the `.ai-project.yml` `models:` refresh.
- **E30.3 — Evidence-driven context-load reduction.** Conditional in extent — sized by what
  E30.2's evidence shows about governance-corpus overhead (scoping/retrieval/caching).

**Sequencing:** M30 first — M31's paid-vs-local decision logic consumes its policy output
(evidence before policy is CFO-ratified, not a preference).

### M31: Dual-Mode Working Levels & Model Guardrail

**Goal:** Give Phase, Milestone, and Epic Chats a per-instance manual/agentic mode switch;
give agentic mode a paid-vs-local decision mechanism grounded in M30's policy; make every
manually started chat verify its model against `.ai-project.yml` and refuse on mismatch.

**Indicative Epics:**
- **E31.1 — Mode model + declaration mechanism.** Where mode is declared, what each mode means
  per level, Creation/HQ recorded as manual-only permanently.
- **E31.2 — Agentic paid-vs-local decision logic.** Applies M30's policy in the agentic path.
- **E31.3 — Manual-mode startup guardrail.** Level→model mapping definition + the verify-and-
  refuse startup check for manual chats.

### M32: System Participant Canonization & Governance Hygiene

**Goal:** Canonize the system-level participant (SN-21) including the daily System Chat
re-instantiation seed, and pay down P8-GH-1/P8-GH-3.

**Indicative Epics:**
- **E32.1 — SN-21 canonization.** Schemas into the protocol (or companion doc), hierarchy
  placement, normative authority boundary.
- **E32.2 — System Chat re-instantiation seed.** The daily-spawn artifact, Genesis-seed
  analogue.
- **E32.3 — Governance hygiene reconciliation.** P8-GH-1 (stale opt-out prose) + P8-GH-3
  (vestigial "Phase Delivery Notice" phrasing purge).

**Sequencing note:** M32 is independent of M30/M31 and may be scheduled by the Phase Chat
wherever it fits best; M30 → M31 ordering is binding.

---

## Success Criteria

### P9 is Complete When:

1. ✅ **A token-burn measurement report is committed** covering chat levels and task types,
   including governance-corpus overhead, from real captured data
2. ✅ **An evidence-grounded frontier-vs-local policy is recorded** and `.ai-project.yml`'s
   `models:` mapping matches it (stale `gpt-4o`/`claude-3-5-sonnet` entries gone)
3. ✅ **Phase, Milestone, and Epic Chats have a working per-instance manual/agentic mode
   switch**; Creation Chat and HQ Chat are normatively recorded as manual-only
4. ✅ **Agentic mode carries a paid-vs-local decision mechanism** applying the recorded policy
5. ✅ **The manual-mode guardrail works** — a manually started chat on the wrong model refuses
   to proceed, per the `.ai-project.yml` mapping
6. ✅ **SN-21 is canonized** — schemas, hierarchy placement, authority boundary, and the daily
   System Chat re-instantiation seed all exist in governance
7. ✅ **P8-GH-1 and P8-GH-3 are reconciled**; P8-GH-2 remains recorded as deferred with its
   trigger, not silently dropped
8. ✅ **The ComfyUI track is surfaced, not resolved** — its status at phase close is reported
   to the CFO as the non-blocking track it is

---

## Acceptance Criteria

The CFO (Layer 8) will accept P9 complete when:

- [ ] The measurement report exists in the repo with real (not estimated) token data per level
  and task type
- [ ] The frontier-vs-local policy is written into governance and `.ai-project.yml`'s `models:`
  block reflects it
- [ ] A working-level chat can demonstrably be started in either mode, and the mode is recorded
  per instance
- [ ] A manual chat started on a mismatched model demonstrably refuses (evidence in the epic's
  delivery)
- [ ] `system_request`/`system_response` schemas are in the protocol (or companion doc), the
  hierarchy placement is recorded, and the System Chat re-instantiation seed is usable daily
- [ ] Grep-level checks show no remaining stale opt-out prose (P8-GH-1) and no remaining
  "Phase Delivery Notice" phrasing in templates/living docs (P8-GH-3)
- [ ] The full suite is green at delivery (307 baseline, no regressions, no skips introduced to
  route around changes)
- [ ] The phase closure declaration restates P8-GH-2 (deferred, with trigger) and the ComfyUI
  non-blocking track's status

---

## Dependencies

### Internal
- P7's orchestrator + `bin/run-dev-agent` adapter path (agentic execution exists; M31 builds
  the mode switch and decision logic around it) — on master at v6.0.1
- P8's closure evidence (precision FAILs) — context for the non-blocking ComfyUI track only
- `governance/ai-project-yml-spec.md` — extended by M30 (`models:` refresh) and M31 (mode +
  mapping design)

### External / CFO-side
- **Premium/frontier quota status** — measurement (M30) spends some paid tokens to measure
  paid-token burn; the CFO controls pacing
- **Local model availability (Ollama)** for any M31 agentic verification runs; GPU contention
  with ComfyUI acknowledged (see P9.2)
- **ComfyUI investigation** — CFO-side, non-blocking, no P9 dependency on it

---

## Timeline

**Estimate:** 3 Milestones, ~9 Epics
- M30 (Token Measurement & Model-Tier Audit): ~1 week (3 epics)
- M31 (Dual-Mode Working Levels & Model Guardrail): ~1 week (3 epics, consumes M30 output)
- M32 (System Participant Canonization & Governance Hygiene): ~3–5 days (3 epics, schedulable
  in parallel by the Phase Chat)
- **Total: ~2–3 weeks**

---

## Reference

### Governing Steering Notes
- **SN-22:** `.ai-project/artifacts/steering-notes/2026-07-17__creation-chat__steering-note__p9-direction.md`
  — P9 spine, three workstreams, ComfyUI demotion, manual-permanence for Creation/HQ, System
  Chat daily-seed input (binding; all decisions CFO-ratified)
- **SN-21:** `.ai-project/artifacts/steering-notes/2026-07-16__creation-chat__steering-note__system-hq-adoption.md`
  — system-level participant field adoption, schemas, authority boundary, canonize-vs-observe
  triage (triage resolved by this spec: canonize, in M32)

### Key Reference Documents
- `.ai-project/artifacts/progress-digests/2026-07-17__hq__progress-digest__v1.1.md` — the
  recorded ComfyUI demotion (revises v1.0's "likely P9's spine")
- `docs/phases/P8__Visual_Artifacts_Activation/P8__phase-closure-declaration.md` —
  carry-forwards P8-GH-1/2/3 (verbatim definitions)
- `.ai-project.yml` — current (stale) `models:` mapping; the object of M30's refresh and M31's
  mapping/guardrail design
- `governance/systems/artifact-communication-protocol.md` — receives (or references) the
  `system_request`/`system_response` schemas
- `governance/systems/chat-hierarchy.md` — receives the system-participant placement decision
- GitHub issue #126 — local-LLM readiness + GPU-exclusivity context for M31 (reference only;
  the scheduling problem stays out of scope)

### Ratified Decisions (settled — NOT for re-debate; SN-22 unless noted)
1. **P9 spine.** Context handling / token efficiency: make token use as smart and effective as
   possible.
2. **Measurement before policy.** The model-tier audit starts with measurement so policies are
   realistic; the Epics-only-local assumption is dead.
3. **Dual mode for working levels only.** Phase/Milestone/Epic Chats become manual-or-agentic,
   set per instance; Creation Chat and HQ Chat are manual permanently. Agentic mode decides
   paid vs local itself. Agentic-by-default is deferred.
4. **Manual-mode guardrail.** Manually started chats verify model-per-level against
   `.ai-project.yml` and refuse on mismatch; mapping design is P9 work.
5. **ComfyUI demoted.** Relevant, non-blocking, not the spine (revises Progress Digest v1.0).
6. **SN-21 stands as written.** Executor System HQ, no authority expansion; the "mighty"
   governing System Chat is pinned vision, not scope.
7. **Daily re-instantiation seed.** The CFO needs a recurring System Chat spawn artifact —
   concrete SN-21 canonization input.
8. **Overarching goal.** The system running so every governed project makes progress.

### HQ Triage Decisions (this scoping session, 2026-07-17)
| Item | Decision | Where |
|------|----------|-------|
| SN-21 canonization | **Canonize now, in P9** (not observe-and-wait) — live across 8 projects, daily seed requested, load-bearing for SN-22's overarching goal | M32 (E32.1, E32.2) |
| P8-GH-1 (stale opt-out prose, Medium) | Into P9 | M32 (E32.3) |
| P8-GH-3 (vestigial "Phase Delivery Notice", Low) | Into P9; P9 planning docs written without the phrase | M32 (E32.3) |
| P8-GH-2 (machine-local hosting, Low) | **Deferred, not scoped** — revisit only on its recorded trigger | Out of Scope |
| ComfyUI investigation (SN-20 CO-3 resolution) | Non-blocking CFO-side track | Out of Scope |

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-07-17 | Initial P9 phase spec. Three milestones (M30 measurement/audit, M31 dual-mode + guardrail, M32 SN-21 canonization + hygiene), ~9 epics. Scoped by SN-22 (spine: context handling / token efficiency); SN-21 triaged canonize-in-P9; P8-GH-1/3 absorbed, P8-GH-2 deferred; ComfyUI track non-blocking. |
