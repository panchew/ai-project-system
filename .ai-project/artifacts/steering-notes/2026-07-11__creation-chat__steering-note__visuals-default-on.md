---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-07-11T00:00:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-17
    severity: high
    title: Visual artifact production should be enabled by default (opt-out), produced whenever a governing artifact is created
decisions:
  - Visual artifacts flip from opt-in to default-on with an explicit opt-out switch.
  - Structural-first default — with no endpoint configured, default-on means structural (Mermaid/PlantUML) only; generative activates when comfyui_url is present.
  - Automatic production is limited to specs and delivery/closure declarations; any other artifact gets a visual on demand by asking in the proper chat, pointing to the artifact file.
  - Enforcement is a config setting (e.g. `visual_required_for_specs: true`, default true), not an unconditional hard gate.
---

# Steering Note — Creation Chat to HQ Chat

## Purpose

This note hands off a CFO direction change on visual artifacts, formed while the CFO
was reading a Milestone spec in a consumer project (local-agent-runner) under
governance v5.1.0. It registers one high concern for P7 scoping and four binding
decisions. It does not close the Creation Chat session.

---

## Concerns for HQ Triage

### SN-17 — Visual production should be default-on and tied to artifact creation [HIGH]

**Detail:** The current model (AOG §16.1) is opt-in and off by default: nothing is
generated unless a project enables `visual_artifacts` in `.ai-project.yml`, and even
then production is available-and-encouraged rather than tied to artifact creation.
The CFO's direction: whenever a spec, delivery notice, or closure declaration is
created, the producing chat should also produce the visual(s) for it, by default.

CFO rationale, verbatim in substance:
- Humans struggle with reading volume; visual artifacts are needed to understand
  concepts — this is the CFO's own experience reading a Milestone spec.
- Business perspective: the CFO needs to understand what the framework is delivering,
  and needs presentable material when collaborating in distributed teams.

Technical reality check (verified against v5.1.0): the production machinery already
exists and is verified — `bin/ai-project-visual` (including the LTX-Video clip path),
the §7 binding schema, by-link storage, the proposed/implemented two-track, and
Visual Bindings sections in the spec templates all shipped in P5-M22/P6. What is
missing to use it is CFO-side infrastructure (reachable ComfyUI endpoint + storage
backend for by-link hosting) plus `enabled: true` per project. Structural visuals
(Mermaid/PlantUML) require no infrastructure at all.

**Required action:** Register as a P7 candidate alongside P7-AE-1, P7-GH-16,
P6-GH-14, P6-GH-15. The design is settled by the four binding decisions below;
scoping should turn them into epics:
1. Flip AOG §16.1 from opt-in to default-on with an explicit opt-out
   (`visual_artifacts.enabled: false`), and reconcile `ai-project-yml-spec.md` §3.5,
   `governance/guides/visual-artifacts.md`, templates, and agent definitions.
2. Codify the structural-first default (decision 2).
3. Codify the trigger set (decision 3) and the on-demand path for all other
   artifact types.
4. Add the enforcement setting (decision 4) to the `visual_artifacts` config block —
   exact key naming (`visual_required_for_specs` vs. per-artifact-type keys) is a
   scoping-level detail; the mechanism (a defaulted-true setting) is decided.

---

## Decisions Already Made

1. Visual artifact production flips from opt-in (off by default) to **enabled by
   default with an opt-out switch**. This system is built for the CFO; the default
   should serve the CFO's comprehension needs.
2. **Structural-first default.** With no ComfyUI endpoint configured, default-on
   produces structural visuals (Mermaid/PlantUML) only; generative production
   activates when `comfyui_url` is present. Default-on is therefore safe for
   projects with zero infrastructure.
3. **Trigger set: specs and delivery/closure declarations.** Automatic production is
   limited to these artifact types. Any other artifact (steering note, progress
   digest, merge authorization, …) gets a visual **on demand** — the CFO asks in the
   proper chat, pointing to the artifact file.
4. **Enforcement is a setting, not an unconditional gate:** e.g.
   `visual_required_for_specs: true` (default true) in the `visual_artifacts` block.
   Opt-out is a config change, not a per-artifact negotiation.

---

## Carry-Over Open Items

1. **Local Agent Runner + ComfyUI coexistence.** The two local-inference systems —
   the Local Agent Runner (Ollama, local LLM execution) and ComfyUI (local visual
   generation) — must live together; both are important to the CFO's platform. How
   they share the local machine (GPU/VRAM, scheduling, whether one orchestrates the
   other) is unresolved. Adjacent to P7-AE-1 (first real agentic run, gated on
   runner P2) — scoping should consider them together.
2. Whether to stand up the visual-production infrastructure (ComfyUI + storage
   hosting) as its own small governed project. Optional — not required to use the
   feature — CFO's call.
3. Immediate, no-framework-change option available today: enable structural-first
   visual production in local-agent-runner now (Mermaid needs no infrastructure),
   ahead of the framework default flip.

---

## Next Action

HQ Chat should:
1. Register SN-17 in the P7 candidate pool in `docs/roadmap/overview.md`, alongside
   the four existing candidates.
2. At P7 scoping, turn the four binding decisions into epics (default flip,
   structural-first, trigger set, enforcement setting) — the decisions themselves
   are not for re-debate.
3. Address the Local Agent Runner + ComfyUI coexistence question (carry-over item 1)
   together with P7-AE-1, since both concern the local-inference platform.
4. Consider adjacency with P7-GH-16 (Level-0 handoff) — both touch the artifact
   cascade and templates; scoping them in the same milestone may reduce
   reconciliation churn.
