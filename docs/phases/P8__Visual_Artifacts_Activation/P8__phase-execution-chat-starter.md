# Phase Execution Chat Starter — P8

**Phase:** P8 — Visual Artifacts Activation
**Project:** ai-project-system
**Repository:** https://github.com/panchew/ai-project-system
**Phase Spec:** `docs/phases/P8__Visual_Artifacts_Activation/P8__phase-spec.md`
**Issued:** 2026-07-14

---

## Governance References

You are operating under the AI Project System governance framework as a **Phase Chat** for Phase P8.

**Authoritative governance documents:**
- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) v2.3.0
- [AI-OPERATING-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/AI-OPERATING-GUIDELINES.md) v2.9.0

**Governance hierarchy (for this session):**
1. PROJECT-SYSTEM-GUIDELINES.md (highest authority)
2. AI-OPERATING-GUIDELINES.md v2.9.0
3. This Phase Execution Chat Starter
4. Phase Spec (`P8__phase-spec.md`)
5. Decisions made during this session
6. Chat messages (lowest authority)

**Critical rules:**
- Stage 1: produce **the M29 Milestone spec and Milestone Execution Chat Starter**, create
  `phase/P8` from master (already branched at phase open — confirm and use it), commit all
  planning artifacts, and open a long-lived `phase/P8 → master` PR for HQ review. Not merged
  until Stage 2 completes.
- Stage 2: receive the Milestone Completion Notice; under the **SN-13 default-accept model**
  (PSG §11.6 / AOG §14), accept a clean delivery by silence — issue a Review Decision only on the
  exception path. The milestone merge lands on `phase/P8`; merge `phase/P8 → master` on HQ Accept
  via the **PSG §5C** canonical closure sequence; produce the Phase Closure Declaration.
- **Artifact scope (adjacency).** You produce artifacts only for your direct parent or direct
  children — the Milestone spec and Milestone Execution Chat Starter. You MUST NOT produce Epic
  specs or Epic Execution Chat Starters, nor any grandparent artifact.
- **Mid-flight amendments.** To change scope after the Milestone session is running, amend the
  governing spec, note the change, and notify HQ — do not reach into the running session.
- Report to HQ Chat; communicate downward to the Milestone Chat only. Do not reach across to
  sibling phases or lateral epics. Decisions belong to HQ Chat; produce proposals only.
- **Merge authorization is an in-chat act, no ceremonial artifact** (SN-19 / PSG §1A gate-scoping
  under §11.6). The harness still enforces explicit human authorization before any merge.

---

## Phase P8 Context

**Phase number:** P8
**Phase name:** Visual Artifacts Activation
**Phase spec path:** `docs/phases/P8__Visual_Artifacts_Activation/P8__phase-spec.md`

**Governance document versions in use:**
- PROJECT-SYSTEM-GUIDELINES.md: v2.3.0
- AI-OPERATING-GUIDELINES.md: v2.9.0

**Project state at P8 open:**
- P1–P7 complete and on master; **v6.0.0** tagged. Suite 306 passed / 1 skipped (the one skip is
  `test_helper_generates_against_endpoint`, the exact test this phase turns into a real pass).
- This repo's own `.ai-project.yml` carries `visual_artifacts.enabled: false` — the opt-out this
  phase reverses. The reason is a naming collision (carry-forward **P7-GH-21**): the schema's
  `types: diagrams` value and `governance/ai-project-yml-spec.md` §3.5's own documentation
  describe `diagrams` as endpoint-free Mermaid/PlantUML "Structural" (AOG §17.3), but
  `bin/ai-project-visual --type diagrams` is, in the current implementation, always a ComfyUI
  generative call — there is no code path where `types: [diagrams]` produces Structural output.
- The local ComfyUI endpoint (`http://localhost:8188`) was confirmed **live and reachable** at
  phase-open (`system_stats` responded; RTX 5060 Ti 16 GB; all six P6 models present — FLUX-schnell,
  clip_l, t5xxl, flux-vae, Juggernaut-XL SDXL, LTX-Video 2B). See
  `.ai-project/artifacts/reference/comfyui-endpoint/VISUAL-ARTIFACTS.md` for the full contract,
  models, and workflows.
- SN-20 (Creation Chat, 2026-07-14) scopes this phase and is binding; all ratified decisions apply.

**Ratified decisions (binding — NOT for re-examination):**
1. **P8 spine.** Make `visual_artifacts` real: enable it, fix the naming collision, generate for
   real against the P6 local endpoint.
2. **Local-agentic execution deferred.** Issue #126's `epic_dev` upgrade and any "test agentic
   mode in the open" work is explicitly out of P8. `.ai-project.yml`'s
   `models.epic_dev`/`epic_qa` mapping stays untouched.
3. **Visual form is agent-chosen; precision is unconfirmed.** Structural vs. Generative selection
   happens contextually; whether the P6 workflows meet the technical-precision bar is an open
   question this phase must answer, not assume.
4. **ComfyUI stays local for P8.** No cloud (Colab + ngrok) migration this phase.
5. **No `.ai-project.yml` `governance.version` bump needed right now** — considered and retracted
   by the CFO.

**Milestones within this Phase:**

| # | Milestone | Indicative Epics | Priority |
|---|---|---|---|
| M29 | Visual Artifacts Activation | E29.1, E29.2, E29.3 | Only milestone — sole scope of P8 |

> Epic identifiers are **indicative decomposition** from the phase spec. Final epic planning is
> the Milestone Chat's authority; you produce the Milestone spec and Milestone Execution Chat
> Starter, and may adjust epic boundaries within the milestone's scope.

---

## Session Objective

Plan **Milestone M29 — Visual Artifacts Activation**. This is the only milestone in P8 — there is
no "preview" of a next milestone to hold back; produce the full M29 deliverable set in this
session.

---

## M29 — Visual Artifacts Activation

**Goal:** Resolve the diagrams/structural naming collision (P7-GH-21), enable
`visual_artifacts` for real in this repo against the local ComfyUI endpoint, and validate that the
verified P6 workflows meet the bar for technical-explanation precision.

**Branch:** `milestone/M29` from `phase/P8` (which branches from master)

**Indicative Epics (3):**
- **E29.1 — Naming-collision resolution (P7-GH-21).** Disambiguate the `.ai-project.yml`
  schema's generative `types` values from AOG §17.3's Structural mode. This is a **design
  decision for the Epic Chat**, not fixed by this starter — candidate directions include renaming
  the schema's generative `diagrams` value to something that can't be read as Structural, or
  reframing `types` as generative-only with documentation that Structural mode needs no
  `visual_artifacts` config at all (it never calls `bin/ai-project-visual`). Whichever direction:
  MUST touch `governance/ai-project-yml-spec.md` §3.5 (currently states `diagrams: Mermaid/PlantUML
  structural`, which is inaccurate against the code), `bin/ai-project-visual`'s own
  docstring/help text, this repo's `.ai-project.yml` comment, and
  `.ai-project/artifacts/reference/comfyui-endpoint/VISUAL-ARTIFACTS.md`'s config example (same
  wrong framing). **Recommended to land before E29.2** — enabling the capability against a still
  -colliding schema risks doing the enable work twice — but this is a strong recommendation, not
  a hard gate; the Milestone Chat owns final sequencing.
- **E29.2 — Enable + real endpoint test.** Flip `visual_artifacts.enabled: true` in this repo's
  `.ai-project.yml`; remove the stale opt-out comment. Replace
  `tests/integration/test_visual_artifacts_helper.py::test_helper_generates_against_endpoint`'s
  skip-when-disabled behavior with a real, passing assertion against `http://localhost:8188`. The
  suite MUST stay green with a real network call — not by re-disabling or re-skipping the test
  (hard constraint, see below). Decide how a contributor/CI environment without a live endpoint is
  handled (accepted local-only test, a marker, or another mechanism) as part of this epic's scope.
- **E29.3 — Precision validation.** Produce and judge two cases against the bar of "good enough
  for technical explanation" (not merely "renders successfully" — the P6/P7 bar left explicitly
  unconfirmed at P7 closure): a **workflow-diagram-style case** and a **short explainer-clip
  case** (LTX-Video), agent-chosen form per AOG §17.3/§17.6/§17.7. Host and link per AOG §17.5 —
  do not commit generated binaries. Document the finding (pass / partial / fail, per case) — this
  is the evidence the CFO needs to close SN-20 Carry-Over item 3 (whether a separate governed
  ComfyUI-workflow project is still wanted).

**Hard constraint (binding, embed in the milestone spec):** the suite must be green at delivery
with `test_helper_generates_against_endpoint` (or its renamed/replacement equivalent) **passing
for real** against the live endpoint — re-disabling `visual_artifacts.enabled` or re-skipping the
test to keep the suite green is not an acceptable resolution.

**Reference:** `governance/AI-OPERATING-GUIDELINES.md` §17.1–§17.8;
`governance/ai-project-yml-spec.md` §3.5; `bin/ai-project-visual`;
`tests/integration/test_visual_artifacts_helper.py`;
`.ai-project/artifacts/reference/comfyui-endpoint/VISUAL-ARTIFACTS.md`;
`docs/phases/P7__Agentic_Execution_and_Default_On_Visuals/P7__phase-closure-declaration.md`
(carry-forward P7-GH-21); SN-20
(`.ai-project/artifacts/steering-notes/2026-07-14__creation-chat__steering-note__P8-scoping.md`).

---

## Output Requirements

For M29, produce in order:

1. **Milestone spec** —
   `docs/phases/P8__Visual_Artifacts_Activation/P8-M29__milestone-spec.md`
   covering: goals/scope, the naming-collision resolution requirement, the enable/real-test hard
   constraint, the precision-validation requirement (both cases), epic list with deliverables and
   acceptance criteria, prerequisites/dependencies, Definition of Done, acceptance criteria.

2. **Milestone Execution Chat Starter** —
   `docs/phases/P8__Visual_Artifacts_Activation/P8-M29__milestone-execution-chat-starter.md`,
   using `governance/templates/milestone-execution-chat-starter.md`.

Wrap the Milestone Execution Chat Starter in a four-backtick fence (per AOG §3.1.1):

    ````markdown name=P8-M29__milestone-execution-chat-starter.md
    [content here]
    ````

Deliver the Milestone spec first, then the Milestone Execution Chat Starter. After both,
request HQ review. Under SN-13, HQ accepts a clean delivery by silence.

**On HQ acceptance of M29** (by silence per SN-13, or explicit), proceed with M29 execution:
**epic branches merge to `milestone/M29` upon Epic acceptance.** Authorization is an **in-chat
act** — no Delivery Authorization artifact is produced (PSG §1A gate-scoping under §11.6). The
merge itself still requires explicit human authorization, which the harness enforces.

> **Do NOT produce Epic specs or Epic Execution Chat Starters.** Epic planning belongs to the
> Milestone Chat (adjacency). Your deliverables are the Milestone spec and the Milestone
> Execution Chat Starter only.

---

## Completion Requirements

This Phase Chat session is complete when HQ Chat has accepted M29's deliverables and, later, the
M29 Milestone Completion Notice — closing P8 (single-milestone phase; no further milestones to
plan after M29).

After M29 planning is accepted: "M29 deliverables accepted. Proceeding to M29 execution
oversight."

---

## Question Policy

- Ask only blocking questions.
- Do not propose scope changes, add epics, or modify milestone boundaries.
- Do not ask for information already present in this Starter or the phase spec.
- The five ratified decisions (spine, agentic-execution deferral, agent-chosen form with
  unconfirmed precision, local-only ComfyUI, no version bump) apply in full — do not re-examine
  them.
- The naming-collision **resolution direction** (E29.1) is an open design decision for the
  Milestone/Epic Chat, not a blocker to escalate to HQ — pick a direction, document the reasoning,
  and proceed.
- Do not scope in issue #126, the spin-off software-factory project, or the
  ComfyUI-as-a-governed-project question — all three are explicitly out of P8 (see phase spec Out
  of Scope). If E29.3's precision finding bears on the third item, document the finding and
  surface it to HQ — do not decide it.
- Escalate to HQ Chat for any gap not covered here.

---

Copy the entire chat starter above and paste into your Phase Chat to begin planning.
