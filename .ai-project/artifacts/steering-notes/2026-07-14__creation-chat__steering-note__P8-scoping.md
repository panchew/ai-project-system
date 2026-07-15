---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-07-14T15:00:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-20
    severity: high
    title: P8 theme — activate real ComfyUI visual artifacts locally; local agentic execution deferred
decisions:
  - "P8 spine: make visual_artifacts real. Enable it in .ai-project.yml, resolve the types: diagrams / AOG §16.3 structural naming collision left open by E27.1, and get generation passing for real against the already-verified P6 local ComfyUI endpoint (localhost:8188) instead of being permanently opted out."
  - "Local-LLM agentic Epic execution (issue #126 — qwen3-coder:30b upgrade, native tool calling, 32k ctx) is explicitly deferred, not part of P8. .ai-project.yml's models.epic_dev/epic_qa mapping stays untouched."
  - "Visual form is chosen by the agent, not prescribed by the CFO: Structural (Mermaid/PlantUML, no ComfyUI) for things like workflow diagrams, Generative (ComfyUI image/video) for concept imagery and short explainer clips. Whether the existing FLUX/SDXL/LTX-Video workflows hit the precision needed for technical explanation is not yet confirmed by the CFO and should be validated as part of P8, not assumed from the P6 verification alone."
  - "ComfyUI stays local for P8 (localhost:8188, same host as everything else) — no cloud migration needed now. This is only viable because local-LLM agentic work is deferred; if that work is picked back up later, the two need to share one GPU exclusively, and a cloud ComfyUI path (Colab + ngrok, CFO has working precedent from another project, 'The Character Factory') becomes relevant again then, not now."
  - "No governance-version bump needed in .ai-project.yml right now — considered and retracted by the CFO. governance.version (6.0.0) and the ai-project-yml-spec version (2.3.0) both already match current state."
---

# Creation Chat Steering Note — P8 Scoping

## Purpose

This note closes the P8 scoping session in the Creation Chat. The CFO opened wanting
to exercise the framework's agentic and visual-artifact capabilities together as a
full chat-to-chat chain, with a larger ambition (multi-project "production line"
orchestration, reviewed by the CFO in open-hours sessions) sitting behind it. Through
the session that scope narrowed to something concrete and immediately actionable:
P8 turns on real ComfyUI visual artifacts using what P6 already built, and defers the
local-agentic-execution half entirely. The larger ambition is real but is not P8 — it
is carried forward below, not scoped in.

---

## Concerns for HQ Triage

### SN-20 — P8 theme and scope boundary [HIGH]

**Detail:** `.ai-project.yml` currently carries `visual_artifacts.enabled: false`
with a comment (left by a past Epic, referenced as E27.1) explaining why: this
schema's `types: diagrams` value is actually a ComfyUI generative txt2img call in
the current implementation, not the endpoint-free Mermaid/PlantUML "structural"
mode AOG §16.3 describes — a naming collision between the two. Enabling it today
breaks `test_helper_generates_against_endpoint` with connection-refused against
`localhost:8188`, so it was left disabled to keep the suite green, and fixing the
collision was explicitly out of that Epic's scope.

Separately, the CFO wanted to also exercise real local-LLM agentic Epic execution
in the same phase (per issue #126: `qwen3-coder:30b` is verified — native tool
calling, 32k context — recommending an `epic_dev` upgrade from the current
`qwen2.5-coder:14b`). Mid-session the CFO chose to defer this: running ComfyUI
locally and running local-LLM agentic execution both want the same GPU (issue
#126 notes the card is fully committed while the 30b model is loaded and that
`comfyui`/`llamacpp` must be stopped during agentic runs), and the CFO would
rather exercise the already-built ComfyUI path cleanly than manage that
contention this phase.

**Required action:** HQ opens the P8 phase spec scoped to the visual-artifacts
activation only:
1. Resolve the `types: diagrams` / AOG §16.3 naming collision (design decision:
   split the schema value, rename, or otherwise disambiguate the schema's
   generative `diagrams` type from AOG's endpoint-free structural mode).
2. Flip `visual_artifacts.enabled: true` and get real generation passing against
   the local endpoint — replace the currently-skipped connection-refused test
   with a real, passing one.
3. Validate precision: confirm the existing FLUX-schnell / SDXL / LTX-Video
   workflows actually produce artifacts good enough for technical explanation
   (not just "renders successfully"), for both a workflow-diagram-style case and
   a short-explainer-clip case, with the agent choosing the form.
4. Leave issue #126 and the `epic_dev`/`epic_qa` mapping untouched — that work is
   deferred, not dropped (see Carry-Over below).

---

## Decisions Already Made

These are the CFO's decisions from this session. Not for HQ to re-debate.

1. **P8 spine.** Make `visual_artifacts` real: enable it, fix the naming
   collision, generate for real against the P6 local endpoint.
2. **Local-agentic execution deferred.** Issue #126's `epic_dev` upgrade and any
   "test agentic mode in the open" work is explicitly out of P8.
3. **Visual form is agent-chosen, precision is unconfirmed.** Structural vs.
   Generative selection happens contextually; whether the P6 workflows meet the
   bar for technical precision is an open question P8 must answer, not an
   assumption it can carry in.
4. **ComfyUI stays local for P8.** No cloud (Colab + ngrok) migration this phase;
   that option exists and is proven elsewhere if the GPU-contention tradeoff
   needs revisiting once local-agentic work resumes.
5. **No `.ai-project.yml` governance-version bump needed right now.** Raised and
   retracted by the CFO this session.

---

## Carry-Over Open Items

Non-blocking. Do not scope into P8. For HQ awareness and later triage.

1. **Local-LLM agentic Epic execution (issue #126).** `qwen3-coder:30b` is
   verified and ready (native tool calling, 32k context). The recommended
   `epic_dev` upgrade and a live-epic proof run are queued for whenever this
   work is picked back up — likely its own phase, given the GPU-exclusivity
   constraint with ComfyUI.
2. **Spin-off "software factory" project (candidate, tentative).** The CFO's
   longer-term ambition: a separate project, a *consumer* of ai-project-system
   governance (configurable to local or cloud models, same arm's-length
   relationship local-agent-runner already has with this repo) providing a
   dashboard/orchestration layer across multiple parallel projects — a daily
   "open hours" briefing (event-driven, not scheduled: brief on whatever
   changed since the CFO last checked in), reviewed via visuals and PRs, with
   the CFO chatting mostly at each project's top-level Creation Chat and
   dropping into lower-level chats only when needed. Mobile dispatch is a named
   nice-to-have. The CFO used "maybe P9" as a placeholder, not a commitment —
   this is not scoped, and structurally would need its own Creation Chat/Project
   Brief as its own project, not a phase of ai-project-system.
3. **ComfyUI-as-a-governed-project thread — status unclear, needs the CFO's
   call.** Earlier in the session the CFO proposed installing ai-project-system
   governance into their own ComfyUI copy to develop/validate a workflow for
   technical precision. The CFO then recalled P6 already delivered working
   workflows and wants to use those for P8 instead. Whether the separate
   governed-ComfyUI-project effort is still wanted (e.g., if P8's precision
   validation in item 3 above finds the P6 workflows insufficient) or fully
   superseded was not resolved — carry forward, do not assume either way.

---

## Next Action

HQ Chat should:

1. Open the P8 phase spec with SN-20's spine as the phase goal: activate real
   ComfyUI visual artifacts against the local P6 endpoint, resolve the naming
   collision, validate precision.
2. Explicitly record issue #126 and the local-agentic-execution track as
   deferred/out-of-scope for P8, not silently dropped.
3. Scope the naming-collision fix and the enable/test work into milestones/epics.
4. Surface Carry-Over items 2 and 3 to the CFO for a future scoping session
   rather than resolving them unilaterally.
