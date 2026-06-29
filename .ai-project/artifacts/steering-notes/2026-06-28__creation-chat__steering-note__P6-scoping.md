---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-06-28T20:00:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-15
    severity: high
    title: P6 theme — visual comprehension layer; consumer architecture for ComfyUI
decisions:
  - "P6 spine: build the consumer architecture that turns the governance flow into a continuous visual narrative — explaining the proposed solution and the actual implementation at every level, generously, primarily so the CFO can follow along with low cognitive load."
  - "Primary purpose of P6 visuals is CFO comprehension / cognitive-load reduction. Publishable social media material (YouTube, TikTok, Instagram, Facebook) is a byproduct of the same asset, not the driver."
  - "Visuals track two things at all times: the proposed solution (before build) and the actual implementation (after). Coverage bar is generous — 'nothing is too much' when explaining proposed vs. actual."
  - "Storage is by link. The framework owns the request-building and the link-based binding convention; it does NOT own the storage backend. Where binaries live is each adopting project's engineering team's decision. No binaries committed to git."
  - "The ComfyUI workflow(s) and models stay on the CFO's side. The CFO will share the workflow(s) into the Creation Chat; the shared workflow definition becomes the request contract. Request-building work is dependency-blocked until that share."
  - "Numbering reconciliation: roadmap candidates P6-GH-1 → P6-GH-12 and P6-GH-2 → P6-GH-13 (applied to docs/roadmap/overview.md). Full P6 candidate pool is GH-10, GH-11, GH-12, GH-13 under one sequence."
---

# Creation Chat Steering Note — P6 Scoping

## Purpose

This note closes the P6 scoping session in the Creation Chat. It hands HQ the
established theme, the binding decisions the CFO made, the open items still to
ratify, and the external dependency (the ComfyUI workflow share) so HQ can open
the P6 phase spec. It continues the thread opened in SN-11 (visual artifacts as
a first-class deliverable at every chat level): P5 built the framework, P6 builds
the consumer.

---

## Concerns for HQ Triage

### SN-15 — P6 theme and consumer architecture [HIGH]

**Detail:** P5 delivered the *framework* for visual artifacts (the
`visual_artifacts` block in `.ai-project.yml`, AOG §16 per-level guidance,
`bin/ai-project-visual`) but it is inert — `enabled: false`, no live ComfyUI
wiring. P6 makes visuals real by building the **consumer side of the wire**.

The CFO has solved the producer side: ComfyUI is set up with the proper models
and a workflow ready to process requests. P6 is therefore not "get ComfyUI
running" — it is the *structure* by which the governance flow consumes that
workflow:

1. **Request side (consumer → ComfyUI).** Build requests from the CFO's shared
   workflow(s); integrate the workflow definition into the docs. Blocked on the
   workflow share (see dependency below).
2. **Retrieval + binding side (ComfyUI → project).** A visual can bind at any
   level — epic, milestone, phase, or HQ. This is a placement convention that
   says which artifact a given visual belongs to and how the link gets there.
3. **Publishing side (project → audience).** Clips that are simultaneously
   documentation and publishable media. The real audience is the CFO; the
   social-media version is the same asset reused.

The through-line: visuals are a **comprehension layer over the agentic flow**.
As governance increasingly runs as background agents, the CFO cannot follow by
reading every markdown artifact — that *is* the cognitive load. Visuals are how
the founder's office stays legible. P6 is the first concrete step toward the
single-visible-surface product vision.

**Required action:** HQ opens the P6 phase spec with this spine, sequences the
candidate pool into milestones, and treats the workflow share as a gating
dependency on the request-building work (while the binding/storage convention,
which does not depend on the workflow, proceeds in parallel).

---

## Decisions Already Made

These are the CFO's decisions from this session. Not for HQ to re-debate.

1. **Spine.** P6 builds the consumer architecture that turns the governance flow
   into a continuous visual narrative — explaining the proposed solution and the
   actual implementation at every level, generously, primarily so the CFO can
   follow along with low cognitive load.
2. **Audience.** Primary purpose is CFO comprehension / cognitive-load reduction.
   Publishable social material is a byproduct of the same asset, not the driver.
3. **Two tracks, generous coverage.** Visuals explain the *proposed solution*
   (before build) and the *actual implementation* (after) at all times. The bar
   is "nothing is too much."
4. **Storage by link, framework stays infrastructure-agnostic.** Artifacts
   reference visuals by link; binaries are never committed to git. The framework
   owns the request-building and the link-based binding convention, not the
   storage backend — each adopting project's engineering team decides where files
   live. (Same agnosticism stance P5 took for platform/agents.)
5. **Workflow stays CFO-side and becomes the contract.** The CFO will share the
   ComfyUI workflow(s) into the Creation Chat; the shared definition is the
   request contract. No guessing the input/output shape before the share.
6. **Numbering reconciled.** P6-GH-1 → P6-GH-12, P6-GH-2 → P6-GH-13 (applied to
   the roadmap). Candidate pool is one sequence: GH-10, GH-11, GH-12, GH-13.

---

## Carry-Over Open Items

Non-blocking. To ratify or resolve during phase-spec authoring.

1. **RATIFIED 2026-06-29 (see SN-16).** The link binding should carry context
   metadata — what the visual is, which level it binds to, proposed-vs-implemented,
   a short text description — so the artifact stays self-explanatory and survives
   link rot.
2. **RATIFIED 2026-06-29 (see SN-16).** A publishable clip anchors to the
   proposed→implemented arc with a single parent in the hierarchy (same binding
   convention as a diagram, richer medium), rather than floating as free editorial
   pulling from many artifacts.
3. **Single registry.** GH-10 and GH-11 currently live only in the P5 Phase
   Closure Declaration; GH-12 and GH-13 live only in the roadmap. Consolidate all
   four into the roadmap candidate table so there is one source of truth.
4. **Process carry-forwards vs. visual core.** GH-12 (phase-closure automation),
   GH-10 (codify SN-13 default-accept), GH-11 (`ai-project-init` writes
   `.ai-project/agents/`) are lower priority than the visual consumer work. HQ
   decides whether they ride in P6 or split to a later phase.

---

## Dependency

**ComfyUI workflow share (external, CFO-owned).** Request-building cannot be
finalized until the CFO shares the workflow(s) into the Creation Chat. This gates
the request-side milestone only. The link-based binding/storage convention and
the metadata schema do not depend on it and can be designed in parallel.

---

## Next Action

HQ Chat should:

1. Open the P6 phase spec with SN-15's spine as the phase goal.
2. Update the roadmap P6 entry (`docs/roadmap/overview.md`) to reflect the
   established theme and consolidate GH-10/11/12/13 into a single candidate table.
3. Sequence the pool into milestones — the visual consumer architecture
   (request-building, link binding, retrieval) as the core; GH-12/GH-10/GH-11 as
   process refinements, scoped in or deferred per HQ's call.
4. Mark the ComfyUI workflow share as a gating dependency on the request-building
   milestone; schedule the binding/storage convention work in parallel since it
   is independent of the share.
5. Surface the two `[PROPOSED — confirm]` items to the CFO for ratification when
   the phase spec is authored.
