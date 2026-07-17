---
phase: P8
name: Visual Artifacts Activation
status: completed
start_date: 2026-07-14
planned_end_date: 2026-07-28
version: 1.0.0
---

# Phase P8: Visual Artifacts Activation

## Executive Summary

P5–P7 built the visual-artifacts framework, flipped it default-on framework-wide (M27), and
proved the generative endpoint works (P6: FLUX-schnell, SDXL, LTX-Video all verified against
`localhost:8188`) — but this source repo has never actually run its own capability. It carries
its own opt-out (`visual_artifacts.enabled: false`) because of a naming collision between the
`.ai-project.yml` schema's `types: diagrams` value and AOG §16.3's endpoint-free "Structural"
mode: the schema value and even the yml-spec's own §3.5 documentation describe `diagrams` as
Mermaid/PlantUML, but `bin/ai-project-visual --type diagrams` is, in the current implementation,
always a ComfyUI generative call. Enabling the capability today doesn't turn on free structural
diagrams — it turns on a generative call with no endpoint reachable in a bare test run, which is
exactly what breaks `test_helper_generates_against_endpoint` with connection-refused. **P8 makes
`visual_artifacts` real**: resolve that collision, flip the switch, and prove generation against
the live local endpoint — closing carry-forward **P7-GH-21**.

P8 is scoped by **SN-20** (Creation Chat, 2026-07-14), which narrowed a larger ambition (exercise
agentic execution and visual artifacts together as one chat-to-chat chain) down to the visual half
only. Local-LLM agentic execution (issue #126) is explicitly deferred — not because it isn't
ready, but because ComfyUI and a loaded local LLM contend for the same 16 GB GPU, and the CFO
would rather exercise the visual-artifacts path cleanly this phase than manage that contention.
All decisions in SN-20 are settled and are **not** for re-debate.

One milestone:

1. **M29 — Visual Artifacts Activation** — resolve the naming collision, enable the capability in
   this repo, get a real passing generation test against the local endpoint, and validate that the
   verified P6 workflows actually produce artifacts precise enough for technical explanation.

---

## Vision

By the end of P8:

- ✅ **The naming collision is gone.** The `.ai-project.yml` schema's generative `types` values
  and AOG §16.3's Structural/Generative mode split no longer share a confusable name; the
  yml-spec §3.5 documentation table (currently wrong — it describes `diagrams` as
  "Mermaid/PlantUML structural") matches what the code actually does.
- ✅ **This repo dogfoods its own default-on flip.** `visual_artifacts.enabled: true` in this
  repo's `.ai-project.yml`, generating for real against `http://localhost:8188`.
- ✅ **The suite is green with a real test, not a skip.** `test_helper_generates_against_endpoint`
  passes against the live endpoint; it is not re-disabled or re-skipped to get there.
- ✅ **Precision is confirmed, not assumed.** A workflow-diagram-style case and a short
  explainer-clip case (agent-chosen form) are produced and judged against the bar of "good enough
  for technical explanation" — the open question P6/P7 left unanswered.
- ✅ **Issue #126 stays visible, not dropped.** The local-agentic-execution track is recorded as
  deferred with its own reason, so it surfaces cleanly whenever GPU exclusivity next gets
  revisited.

---

## Scope

### P8.1: Visual Artifacts Activation (M29)

**The naming-collision fix (P7-GH-21).** Two things are tangled under one schema value:
- AOG §16.3's **Structural** mode — an agent writing Mermaid/PlantUML text directly, no endpoint,
  no `bin/ai-project-visual` call at all.
- The `.ai-project.yml` `visual_artifacts.types` schema's `diagrams` value — which, in
  `bin/ai-project-visual`'s actual implementation, selects a ComfyUI txt2img workflow. There is no
  code path today where `types: [diagrams]` yields Structural output; the yml-spec §3.5 table row
  claiming `diagrams: Mermaid/PlantUML structural` is inaccurate as written.

The fix is a **design decision for the Milestone/Epic Chat**, not fixed here — HQ scopes the
problem, not the resolution. Candidate directions (non-exhaustive, for the Epic Chat to weigh):
rename the schema's generative `diagrams` value to something that can't be read as Structural
(e.g. a name that signals "diagram-style generated image"); or reframe `types` entirely as
generative-only categories with documentation that Structural mode needs no `visual_artifacts`
config at all, since it never touches the helper. Whichever direction, the fix MUST touch every
place the collision is documented: `governance/ai-project-yml-spec.md` §3.5, this repo's
`.ai-project.yml` comment, `bin/ai-project-visual`'s own docstring/help text, and the CFO's
`.ai-project/artifacts/reference/comfyui-endpoint/VISUAL-ARTIFACTS.md` (which carries the same
wrong `diagrams: Mermaid/PlantUML structural` framing in its own config example).

**Enable + real generation.** Flip `visual_artifacts.enabled: true` in this repo's
`.ai-project.yml`. Replace `test_helper_generates_against_endpoint`'s current
skip-when-disabled behavior with a real, passing assertion against `http://localhost:8188` (live
and verified reachable as of phase-open — `system_stats` responds, RTX 5060 Ti 16 GB, all six P6
models present). The suite MUST stay green through this change with a real network call, not by
re-disabling or re-skipping the test — this is a hard constraint, not a preference (see
Constraints below). The Epic Chat should consider what happens for a contributor/CI environment
without a live ComfyUI endpoint reachable — whether that's an accepted local-only test, a marker,
or something else is an implementation decision within this epic's scope.

**Precision validation.** Confirm, empirically, that the P6-verified workflows produce artifacts
good enough for **technical explanation** — not merely "renders successfully" (the P6/P7 bar,
explicitly left unconfirmed at P7 closure). Two cases, agent-chosen form per AOG §16.3:
1. A **workflow-diagram-style case** — e.g. a generated visual explaining a governance or code
   flow.
2. A **short explainer-clip case** — e.g. an LTX-Video clip narrating a proposed→implemented arc
   (AOG §16.6/§16.7).

Judge both against whether a reader unfamiliar with the underlying flow could follow it from the
artifact alone. Document the finding (pass, partial, or fail per case) — this is the evidence the
CFO needs to close Carry-Over item 3 (whether a separate governed ComfyUI-workflow project is
still wanted).

---

## Out of Scope

- **Local-LLM agentic execution (issue #126).** `qwen3-coder:30b` is verified-ready
  (native tool calling, 32k context) and an `epic_dev` upgrade is recommended in that issue — but
  it is **deferred, not dropped**. Reason (CFO, SN-20): ComfyUI and a loaded local LLM both want
  the RTX 5060 Ti 16 GB exclusively; running P8's visual-activation work cleanly this phase means
  not also contending for the GPU with agentic execution. `.ai-project.yml`'s
  `models.epic_dev`/`epic_qa` mapping stays untouched. Revisit in a future phase.
- **The spin-off "software factory" project.** The CFO's longer-term ambition — a separate project
  consuming this governance to orchestrate/dashboard across multiple parallel projects — is real
  but not a phase of this repo. Not scoped in; stays a future Creation Chat item (SN-20
  Carry-Over 2).
- **Whether a separate governed ComfyUI-workflow project is still needed.** Raised and left open
  in SN-20 (Carry-Over 3) pending exactly the precision validation this phase performs. P8
  produces the evidence; it does not decide the question. Surface the finding to the CFO, do not
  resolve unilaterally.
- **Cloud ComfyUI migration (Colab + ngrok).** Proven elsewhere (the CFO's "The Character Factory"
  project) and stays available if GPU contention needs revisiting once local-agentic work resumes
  — not needed for P8, which runs entirely against the local endpoint.
- **A `.ai-project.yml` `governance.version` bump.** Raised and retracted by the CFO in the
  scoping session; `governance.version` (6.0.0) already matches current state.
- **Building new ComfyUI workflows.** The verified P6 workflows (FLUX-schnell, SDXL,
  LTX-Video) are the baseline this phase tests. New workflow engineering is only in scope if the
  precision validation finds the existing ones insufficient, and even then only to the extent
  needed to complete that validation — not a general workflow-development effort.

---

## Milestones

### M29: Visual Artifacts Activation

**Goal:** Resolve the diagrams/structural naming collision (P7-GH-21), enable
`visual_artifacts` for real in this repo against the local ComfyUI endpoint, and validate that the
verified P6 workflows meet the bar for technical-explanation precision.

**Indicative Epics** (the Milestone Chat owns final decomposition):
- **E29.1 — Naming-collision resolution (P7-GH-21).** Disambiguate the schema's generative
  `types` values from AOG §16.3's Structural mode; reconcile `ai-project-yml-spec.md` §3.5,
  `bin/ai-project-visual`'s docstring, `.ai-project.yml`'s comment, and
  `VISUAL-ARTIFACTS.md`'s config example. Land before E29.2 so the enable step isn't undone by a
  documentation/schema change immediately after.
- **E29.2 — Enable + real endpoint test.** Flip `visual_artifacts.enabled: true` in this repo;
  replace `test_helper_generates_against_endpoint`'s skip with a real passing run against
  `http://localhost:8188`; suite stays green.
- **E29.3 — Precision validation.** Produce and judge a diagram-style case and a clip-style case
  against the technical-explanation bar; document the finding for the CFO (feeds Carry-Over
  item 3).

**Sequencing note:** E29.1 before E29.2 is a strong recommendation, not a hard gate the Milestone
Chat must preserve as written — but enabling the capability against a still-colliding schema risks
doing the enable work twice.

---

## Success Criteria

### P8 is Complete When:

1. ✅ **The naming collision is resolved** — the schema, the helper's own documentation, this
   repo's `.ai-project.yml` comment, and `VISUAL-ARTIFACTS.md` all agree on what `types` values
   mean, with no claim that a generative call is Structural output
2. ✅ **This repo's `visual_artifacts.enabled` is `true`**, generating for real against
   `http://localhost:8188`
3. ✅ **`test_helper_generates_against_endpoint` passes for real** — not skipped, not disabled
4. ✅ **A diagram-style and a clip-style artifact are produced and judged** against the
   technical-explanation precision bar, with the finding documented
5. ✅ **Issue #126 / local-agentic execution is recorded as deferred**, with its GPU-exclusivity
   reason, not silently dropped
6. ✅ **Carry-Over items 2 and 3 (SN-20) are surfaced to the CFO**, not resolved unilaterally by
   this phase

---

## Acceptance Criteria

The CFO (Layer 8) will accept P8 complete when:

- [ ] `governance/ai-project-yml-spec.md` §3.5 no longer describes a ComfyUI-generative `types`
  value as "Mermaid/PlantUML structural"
- [ ] This repo's `.ai-project.yml` has `visual_artifacts.enabled: true` with no stale
  opt-out comment
- [ ] `pytest` runs `test_helper_generates_against_endpoint` (or its renamed/replacement
  equivalent) as a real pass against a live endpoint, not a skip
- [ ] The full suite is green at delivery (no regressions, no new skips introduced to route
  around the change)
- [ ] A diagram-style generated artifact and a clip-style generated artifact both exist (by link,
  per AOG §16.5 — not committed as binaries) with a documented precision judgment for each
- [ ] The phase closure declaration records issue #126 as deferred-not-dropped and restates
  SN-20 Carry-Over items 2 and 3 as open items for the CFO

---

## Dependencies

### Internal
- P7's default-on visuals framework (AOG §16, `ai-project-yml-spec.md` §3.5, `bin/ai-project-visual`) —
  complete, on master at v6.0.0
- P6's verified ComfyUI endpoint contract
  (`.ai-project/artifacts/reference/comfyui-endpoint/VISUAL-ARTIFACTS.md`) — complete; all three
  workflows (FLUX-schnell, SDXL, LTX-Video) verified against `localhost:8188`

### External / CFO-side
- **Live ComfyUI endpoint at `http://localhost:8188`** — confirmed reachable at phase-open
  (`system_stats` responded; RTX 5060 Ti 16 GB, all six P6 models present). Availability during
  Epic execution is the CFO's responsibility, as with any generative-mode work (AOG §16.5).
- **GPU exclusivity is real but moot for P8.** Local ComfyUI and local-LLM agentic execution
  cannot run concurrently on this hardware; moot here only because agentic execution is deferred
  for the whole phase.

---

## Timeline

**Estimate:** 1 Milestone, 3 Epics
- M29 (Visual Artifacts Activation): 4–6 days (3 epics, E29.1 recommended before E29.2)
- **Total: ~1–1.5 weeks**

---

## Reference

### Governing Steering Note
- **SN-20:** `.ai-project/artifacts/steering-notes/2026-07-14__creation-chat__steering-note__P8-scoping.md`
  — P8 spine, scope boundary, five ratified decisions, Carry-Over items (binding)

### Key Reference Documents
- `governance/AI-OPERATING-GUIDELINES.md` §16.1–§16.8 — Structural vs. Generative policy,
  default-on trigger policy
- `governance/ai-project-yml-spec.md` §3.5 — `visual_artifacts` schema (contains the collision
  this phase resolves)
- `bin/ai-project-visual` — the generative helper (source of truth for what `--type` actually does)
- `tests/integration/test_visual_artifacts_helper.py` — the currently-skipped endpoint test this
  phase replaces with a real pass
- `.ai-project/artifacts/reference/comfyui-endpoint/VISUAL-ARTIFACTS.md` — CFO's verified P6
  endpoint contract (models, workflows, config example — also carries the collision)
- `docs/phases/P7__Agentic_Execution_and_Default_On_Visuals/P7__phase-closure-declaration.md` —
  carry-forward **P7-GH-21**
- GitHub issue #126 — local-LLM readiness report (`qwen3-coder:30b`); deferred, reference only

### Ratified Decisions (settled — NOT for re-debate)
1. **P8 spine.** Make `visual_artifacts` real: enable it, fix the naming collision, generate for
   real against the P6 local endpoint.
2. **Local-agentic execution deferred.** Issue #126's `epic_dev` upgrade and any "test agentic
   mode in the open" work is explicitly out of P8.
3. **Visual form is agent-chosen; precision is unconfirmed.** Structural vs. Generative selection
   happens contextually; whether the P6 workflows meet the technical-precision bar is an open
   question this phase must answer, not assume.
4. **ComfyUI stays local for P8.** No cloud (Colab + ngrok) migration this phase.
5. **No `.ai-project.yml` governance-version bump needed right now.**

### Items Excluded from P8
- Local-LLM agentic execution (issue #126) — deferred, own future phase
- Spin-off software-factory project — future Creation Chat item, not a phase of this repo
- ComfyUI-as-a-governed-project question — open, pending this phase's own precision finding
- Cloud ComfyUI migration — proven elsewhere, not needed now

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-07-14 | Initial P8 phase spec. One milestone (M29), 3 epics. Resolves P7-GH-21 (diagrams/structural naming collision), enables `visual_artifacts` for real against the local P6 ComfyUI endpoint, and validates technical-explanation precision for a diagram-style and a clip-style case. Scoped by SN-20; local-agentic execution (issue #126) and the two SN-20 Carry-Over items explicitly excluded. |
