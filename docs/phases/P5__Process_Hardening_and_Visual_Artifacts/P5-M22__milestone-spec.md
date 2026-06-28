---
milestone: M22
name: Visual Artifacts
phase: P5
status: planned
start_date: 2026-06-28
epics:
  - E22.1
  - E22.2
is_final: true
---

# Milestone M22 — Visual Artifacts

## Purpose

Establish visual artifact production as a first-class, opt-in capability so that any
tool-capable agent can produce visuals — when the feature is enabled — at the abstraction
level that matches its chat level. M22 is the **final P5 milestone**: when it consolidates
into `phase/P5`, Phase P5 is ready for delivery to `master`.

Scope is the framework layer **plus** the working integration: the `.ai-project.yml` spec
extension, AOG guidance, the `seed.md` visual-intent elicitation, a ComfyUI API helper
callable by any tool-capable agent, an integration guide, and an integration test that
**skips gracefully when the feature is disabled**. The CFO supplies a reachable ComfyUI
endpoint; the framework delivers everything else.

This milestone ensures:
- Visual artifacts are **opt-in** via `visual_artifacts.enabled` (default `false`),
  mirroring the existing `cfo_review_gate` opt-in philosophy (VA-1 config layer)
- Every chat level has clear guidance on **what visual to produce and how** (VA-1)
- A new adopter is asked **"what does success look like visually?"** at Creation Chat,
  before the Project Brief (SN-11)

---

## Binding Design Decisions (SN-11, 2026-06-21 — apply in full, do not re-examine)

Source: `.ai-project/artifacts/steering-notes/2026-06-21__creation-chat__steering-note.md`.

1. **Opt-in** via `visual_artifacts.enabled` in `.ai-project.yml`; default `false`.
2. **Abstraction mirrors chat level** (table below).
3. **Tool-calling capability is the gate** for visual production — not the chat-level label.
4. **Two visual modes:** *structural* (Mermaid/PlantUML diagrams) and *generative*
   (ComfyUI API imagery/video).
5. **Visual intent originates at the Creation Chat** and propagates down the artifact cascade.
6. **Video output** (ComfyUI video nodes) is in scope.
7. **`seed.md` must elicit** "what does success look like visually?" before the Project Brief.

| Chat level | Visual type |
|------------|-------------|
| Creation Chat | Concept / vision imagery |
| HQ Chat | System architecture |
| Phase Chat | Phase scope diagram |
| Milestone Chat | Component + flow diagrams |
| Epic Chat | UI mockups, before/after, implementation diagrams |

---

## Problem Statement

The governance framework has no notion of visual artifacts. Adopters who want a concept
image, an architecture diagram, or a UI mockup have no configuration to enable it, no
guidance on what each chat level should produce, no helper to call a generative endpoint,
and no prompt at project inception to capture visual intent. SN-11 (binding) decided this is
P5 scope and that the capability must be opt-in, tool-capability-gated, and present at every
chat level. M22 delivers it.

---

## Goals

By the end of this milestone, the system must:

1. Define and validate a `visual_artifacts` block (`enabled`, `comfyui_url`, `types`) in the
   `.ai-project.yml` spec, defaulting to `enabled: false` in this repo (E22.1).
2. Document "Visual Artifact Production" in AOG — what each chat level produces, structural
   vs. generative modes, and what to commit where (E22.2).
3. Elicit visual intent in `seed.md` Rule 4, before the Project Brief (E22.2).
4. Ship a ComfyUI API helper (`bin/ai-project-visual` or equivalent) callable by any
   tool-capable agent, plus an integration guide and a gracefully-skipped integration test
   (E22.2).

---

## Non-Goals

This milestone explicitly does **not** aim to:

- Stand up or host a ComfyUI instance — endpoint availability is the **CFO's** responsibility
  (managed via the ComfyUI project, which adopts governance separately)
- Require a live endpoint for the suite to pass — the integration test MUST skip when
  `enabled: false` so the repo's suite stays green
- Re-examine or revise the SN-11 binding decisions
- Build a UI, a queue, or batch/render orchestration beyond a single prompt→artifact helper
- Touch M20/M21 deliverables

---

## In Scope

- `visual_artifacts` block in `governance/ai-project-yml-spec.md` + validation + tests +
  this repo's `.ai-project.yml` (E22.1)
- AOG "Visual Artifact Production" section; `governance/templates/seed.md` Rule 4;
  `bin/ai-project-visual` helper; `governance/guides/visual-artifacts.md`; integration test
  (E22.2)

## Out of Scope

- ComfyUI instance provisioning/hosting (CFO)
- Non-ComfyUI generative backends
- Any M20/M21 change

---

## Planned Epics

### Confirmed Epics

- **E22.1 — Configuration and spec** (VA-1 config layer)
- **E22.2 — Guidelines, templates, and agent integration** (VA-1 full implementation)

> **Artifact scope (GH-8 adjacency):** the Phase Chat produced only this Milestone spec and
> the Milestone Execution Chat Starter. The Milestone Chat (§3.7) authors both Epic specs and
> both Epic Execution Chat Starters for E22.1 and E22.2. No Phase-level Epic drafts exist.

### Deferred Epics

- None.

---

## Epic Detail

### E22.1 — Configuration and spec (VA-1 config layer)

**Source:** P5 phase spec, P5-VA-1 (config layer); SN-11 decision 1.

**Grounding (verified):** `.ai-project.yml` (repo root) currently opts in to features with a
simple scalar (`cfo_review_gate: enabled`). The spec `governance/ai-project-yml-spec.md` has
§3 Schema (with §3.1 Full Schema Reference) and §4 Validation Rules. `.ai-project.yml` is
parsed/consumed by `bin/ai-project-init` and `bin/ai-project-orchestrator` — **extend the
existing config handling; do not introduce a parallel validator.**

**Deliverables:**

1. **Spec extension** — document the `visual_artifacts` block in
   `governance/ai-project-yml-spec.md` (§3 schema + §3.1 full-schema reference + §4 validation
   rules + an example): a nested, opt-in block —
   ```yaml
   visual_artifacts:
     enabled: false              # opt-in; default false
     comfyui_url: http://localhost:8188
     types:
       - diagrams                # Mermaid/PlantUML structural
       - infographics            # ComfyUI-generated imagery
       - video                   # ComfyUI video (optional)
   ```
2. **Validation** — validate the block in the existing `.ai-project.yml` handling: `enabled`
   is boolean; `types` ∈ {diagrams, infographics, video}; `comfyui_url` is a well-formed URL
   when present; the whole block is optional (absent ⇒ disabled).
3. **Tests** — coverage for valid blocks, invalid values, and the absent/default-false case.
4. **Repo config** — add the block to this repo's `.ai-project.yml` with `enabled: false`.

**Definition of Done:**
- [ ] `visual_artifacts` block documented in `governance/ai-project-yml-spec.md` (schema + validation rules + example)
- [ ] Validation accepts valid blocks and rejects invalid `enabled`/`types`/`comfyui_url`
- [ ] Tests cover valid, invalid, and absent/default cases; full suite passes
- [ ] This repo's `.ai-project.yml` carries the block with `enabled: false`

**Acceptance Criteria:**
- [ ] `governance/ai-project-yml-spec.md` documents the `visual_artifacts` block
- [ ] A `.ai-project.yml` with a malformed `visual_artifacts` block fails validation; a valid one passes
- [ ] Suite green with `enabled: false` default

---

### E22.2 — Guidelines, templates, and agent integration (VA-1 full implementation)

**Source:** P5 phase spec, P5-VA-1 (full implementation); SN-11 decisions 2–7.

**Depends on E22.1** — the helper and integration test read the `visual_artifacts` block
(`comfyui_url`, `enabled`) that E22.1 defines. Execute E22.1 first.

**Deliverables:**

1. **AOG "Visual Artifact Production" section** — when `enabled`: what each chat level
   produces (the SN-11 abstraction table), structural (Mermaid/PlantUML) vs. generative
   (ComfyUI) modes, tool-capability gating, and what files to commit and where.
2. **`seed.md` Rule 4** — update `governance/templates/seed.md` to elicit "What does success
   look like visually?" before the Project Brief (visual intent originates at Creation Chat).
3. **ComfyUI helper** — `bin/ai-project-visual` (or equivalent), callable by any tool-capable
   agent: accepts a prompt, a type, and an output path; reads `comfyui_url` from
   `.ai-project.yml`; calls the ComfyUI API; writes the result to the output path. Fails
   clearly when `enabled: false` or no endpoint is configured.
4. **Integration guide** — `governance/guides/visual-artifacts.md`: endpoint configuration,
   structural-diagram tooling, output formats, and a worked example for each chat level's
   visual (per the abstraction table).
5. **Integration test** — exercises the helper against the ComfyUI endpoint; **skips
   gracefully when `visual_artifacts.enabled` is `false`** (the repo default), so the suite
   stays green without a live endpoint.

**Definition of Done:**
- [ ] AOG has a "Visual Artifact Production" section with per-level guidance and both modes
- [ ] `seed.md` Rule 4 elicits visual intent before the Project Brief
- [ ] `bin/ai-project-visual` runs, reads `comfyui_url`, calls ComfyUI, writes output (manually verifiable against a live endpoint)
- [ ] `governance/guides/visual-artifacts.md` exists with a worked example per chat level
- [ ] Integration test present and **skipped when `enabled: false`**; full suite passes
      (skips, no failures) at the repo default

**Acceptance Criteria:**
- [ ] AOG directs an agent to produce the correct visual for its chat level when `enabled: true`
- [ ] `bin/ai-project-visual` (or equivalent) is callable by a tool-capable agent, reads the configured endpoint, and writes a visual artifact
- [ ] The integration test skips cleanly at `enabled: false`; the suite is green

---

## Branch Strategy

```
master
└── phase/P5            (M20 + M21 already consolidated here)
    └── milestone/M22        ← this milestone (final P5 milestone; branch from phase/P5)
        ├── epic/P5-M22-E22.1   ← Configuration and spec
        └── epic/P5-M22-E22.2   ← Guidelines, templates, and agent integration
```

Epic PRs target `milestone/M22`. Consolidation PR: `milestone/M22 → phase/P5`.
**Phase closure:** after M22 consolidates, `phase/P5 → master` (PR #82) is delivered (Stage 2).

---

## Prerequisites

- `phase/P5` carries the merged M20 + M21 work
- These targets are present and git-tracked on `phase/P5` (verify with
  `git ls-files --error-unmatch <path>` — the GH-1 convention):
  - `governance/ai-project-yml-spec.md`
  - `.ai-project.yml`
  - `governance/AI-OPERATING-GUIDELINES.md`
  - `governance/templates/seed.md`
  - `bin/` (helper home; `bin/ai-project-init` shows the config-handling pattern)
- **External (CFO):** a reachable ComfyUI endpoint is the CFO's responsibility and is **not
  required** for M22 to pass — the integration test skips at `enabled: false`.

---

## Dependencies and Sequencing

- **E22.1 → E22.2** (hard dependency): E22.2's helper and integration test consume the
  `visual_artifacts` block E22.1 defines. Execute E22.1, accept/merge it, then branch E22.2
  from the merged `milestone/M22`.
- Shared-file contention is low (E22.1: yml-spec + `.ai-project.yml` + config loader + tests;
  E22.2: AOG + seed.md + new helper + new guide + integration test), so the dependency — not
  file conflict — sets the order. Use a worktree if any overlap arises (GH-2).

**External:** ComfyUI endpoint (CFO) — optional, integration-test-only, skipped when disabled.

---

## Definition of Done (Milestone)

- [ ] E22.1 and E22.2 each meet their Definition of Done above
- [ ] Both epic branches merged to `milestone/M22`
- [ ] Full test suite passes on `milestone/M22` (integration test skipped at `enabled: false`)
- [ ] Milestone Closure Declaration produced

---

## Acceptance Criteria (Milestone)

1. `governance/ai-project-yml-spec.md` documents a validated `visual_artifacts` block; this
   repo's `.ai-project.yml` sets `enabled: false` (E22.1).
2. AOG directs an agent to produce the right visual for its chat level when
   `visual_artifacts.enabled: true` (E22.2).
3. `seed.md` elicits visual intent before the Project Brief (E22.2).
4. `bin/ai-project-visual` is callable by a tool-capable agent, calls the configured ComfyUI
   endpoint, and writes a visual artifact; `governance/guides/visual-artifacts.md` documents
   it with a per-level worked example (E22.2).
5. The integration test skips cleanly at `enabled: false`; the full suite is green.

---

## Timeline

**Target Start:** 2026-06-28
**Target Completion:** 2026-07-05 (5–7 days per Phase spec estimate)
**Actual Start:** Not started
**Actual Completion:** In progress

---

## Notes

- M22 is the **final P5 milestone** (`is_final: true`). On its consolidation into `phase/P5`,
  the Phase Chat proceeds to **Phase delivery** — `phase/P5 → master` (PR #82) — and the
  P5 Phase Delivery Notice.
- The framework/CFO split is binding (SN-11): M22 delivers a working integration; the CFO
  delivers a reachable endpoint. Keep the suite green without one (skip-on-disabled).
- The exact helper name/location (`bin/ai-project-visual` vs. equivalent) and the structural
  diagram tooling choice are Epic-level decisions for E22.2; the milestone fixes the
  capability and its contract, not the implementation details.
- Default-accept (SN-13) governs delivery: clean Epic/Milestone deliveries are auto-accepted;
  Review Decisions are the exception path.
