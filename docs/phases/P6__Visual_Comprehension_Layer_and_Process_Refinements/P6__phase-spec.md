---
phase: P6
name: Visual Comprehension Layer and Process Refinements
status: active
start_date: 2026-06-29
planned_end_date: 2026-08-15
version: 1.0.0
---

# Phase P6: Visual Comprehension Layer and Process Refinements

## Executive Summary

P5 shipped the visual-artifacts **framework** (the `visual_artifacts` block, AOG §16,
`bin/ai-project-visual`, `governance/guides/visual-artifacts.md`) — inert, `enabled: false`.
The CFO has since delivered and **verified end-to-end** the producer side: three
API-format ComfyUI workflows (FLUX-schnell, SDXL/Juggernaut-XL, LTX-Video 2B) driven
through the existing helper. **The plumbing is done. P6 is not plumbing.**

P6 builds the **consumer architecture that turns the governance flow into a continuous
visual narrative** — explaining the *proposed solution* (before build) and the *actual
implementation* (after) at every level, generously, primarily so the CFO can follow along
with low cognitive load. Publishable clips (YouTube/TikTok/IG/FB) are a **byproduct** of
the same asset, not the driver.

P6 has two parallel objectives:

1. **Visual Comprehension Layer (M23–M24)** — reverse the v5.0.0 binary-storage model to
   **by-link**, define the **link + metadata binding convention**, make
   **proposed-vs-implemented** visuals routine at every level, and define **clips** as
   single-parent documentation that doubles as publishable media.

2. **Process Refinements (M25)** — close the three process carry-forwards from P5
   (GH-12 phase-closure canonical sequence, GH-10 codify SN-13 default-accept, GH-11
   `ai-project-init` agent path).

The governing inputs are **SN-15** (P6 scoping) and **SN-16** (contract delivered, scope
sharpened). All binding decisions in those notes are settled and are **not** for re-debate.

---

## Vision

By the end of P6:

- ✅ **Generated visual material is referenced by link, never committed to git** — the
  v5.0.0 "commit the binary so it travels with the decision record" guidance is reversed,
  reconciled everywhere it appears, and the adopter owns the storage backend
- ✅ **A visual's link carries its own context** — every binding records what the visual is,
  which level it belongs to, proposed-vs-implemented, and a short description, so the record
  survives link rot when the link is the only thing in git
- ✅ **Proposed-vs-implemented coverage is routine at every level** — "nothing is too much";
  Structural (free, text, no endpoint) carries most of it, Generative fills concept/clips
- ✅ **A clip tells one node's proposed→implemented story** — bound to exactly one governance
  node, produced from the verified LTX-Video path, reusable as published media
- ✅ **Phase closure is a canonical automatic sequence** — README update, version bump, and
  tag happen as mandatory steps, not via an out-of-band Steering Note
- ✅ **The default-accept model is written down** — SN-13 is codified in AOG, PSG, and the
  Starter templates, matching the protocol already in force since P5

---

## Scope

### P6.1: By-Link Storage Model and Binding Convention (M23)

The foundation. Two tightly-coupled deliverables: reverse the storage model, then define
the binding convention that becomes load-bearing once the link is the only thing in git.

**P6-VC-1 — By-link storage reconciliation (explicit reversal of v5.0.0 guidance)**

> **This is the single biggest governance change in P6 and is named here as an explicit,
> scoped deliverable so it cannot leak in as an incidental edit.**

Shipped v5.0.0 guidance instructs committing the generated binary into
`.ai-project/visuals/<level>/<id>.<ext>` so it "travels with the decision record." The CFO
has **reversed this** (ratified 2026-06-29, SN-16): generated visual material is **not**
stored in the version-controlled project; it is **referenced by link**; **no binaries in
git**; the **adopter owns the storage backend** (same infrastructure-agnostic stance P5
took for platform/agents). Rationale: version control is the wrong home for generated
binary material.

The reconciliation must touch **all four** of these surfaces, named explicitly:
1. `governance/guides/visual-artifacts.md` — §4 (Output formats: the `.ai-project/visuals/...`
   path and "commit the generated file together with the artifact" instruction) and the §1
   source-repo note
2. `governance/AI-OPERATING-GUIDELINES.md` §16.5 ("What to commit, and where" — the
   "Generated artifacts are written under … and committed" bullet)
3. `bin/ai-project-visual` output guidance — clarify that `--output` writes a **local
   working file** to be hosted and linked, not committed (see Open Design Question B)
4. The integration-test expectations — any assertion that expects a committed binary under
   `.ai-project/visuals/` updates to the by-link model

Structural diagrams (Mermaid/PlantUML text) are unaffected and continue to live inline /
as sibling `.mmd`/`.puml` files — text belongs in git; generated binaries do not.

**P6-VC-2 — Link + metadata binding convention**

Define how a visual's *link* plus context **metadata** attaches to the correct governance
artifact at the correct level. The metadata is **load-bearing** under by-link because the
link is the only thing in git (ratified 2026-06-29, SN-16). Each binding records, at
minimum:
- **what** the visual is (image / infographic / mockup / diagram / clip)
- **which level** it binds to (Creation / HQ / Phase / Milestone / Epic)
- **proposed vs. implemented** (the two-track state)
- a **short text description** (so the record survives link rot)

Deliverable surfaces: a documented binding schema in `governance/guides/visual-artifacts.md`,
the per-level placement convention (which artifact a binding attaches to and how), and
template/guide updates so each level knows how to record a binding.

### P6.2: Comprehension Behavior and Clips (M24)

Builds on the M23 binding convention.

**P6-VC-3 — Proposed-vs-implemented comprehension behavior ("nothing is too much")**

Make proposed-vs-implemented visuals **routinely happen** at every level. The framework
already splits **Structural** (Mermaid/PlantUML — text, free, no endpoint; carries most
architecture/scope/component/flow diagrams) from **Generative** (ComfyUI — concept/vision
imagery, infographics, mockups, clips). Generous coverage is cheap precisely because most
of it is Structural. Deliverables: AOG §16 guidance establishing the two-track expectation
as the default at every level, per-level examples of what "proposed" and "implemented"
look like, tied to the M23 binding convention.

**P6-VC-4 — Clips as documentation + publishable media**

A clip binds to **exactly one** governance node (one epic, milestone, or phase) and tells
that node's proposed→implemented story, using the same binding convention as any other
visual (ratified 2026-06-29, SN-16 — no cross-cutting editorial reel in P6; a
project-spanning montage is a separate later capability if ever wanted). The LTX-Video path
(`ltxv-video.json` → `.webm`) is verified. Deliverables: how a clip is produced from the
proposed→implemented arc, and the publish path to YouTube/TikTok/IG/FB as the *same asset
reused* — not a separate production.

### P6.3: Process Refinements (M25)

Close the three carry-forwards. Independent of the visual work; lower priority.

**P6-GH-12 — Phase-closure canonical sequence** *(High)*

Today, README update + version bump + tag at phase closure require an out-of-band Steering
Note (this is how P5 closed). Make them **mandatory automatic steps** in the phase-closure
process — the same pattern the Epic happy path already uses. Touches the phase-closure
documentation in `governance/` and any closure template/checklist.

**P6-GH-10 — Codify SN-13 default-accept model** *(Medium)*

The default-accept delivery model (parent auto-accepts clean deliveries; Review Decision is
the exception path only) operated correctly through P5 but is **not yet written down**.
Codify it into `governance/AI-OPERATING-GUIDELINES.md`, `governance/PROJECT-SYSTEM-GUIDELINES.md`,
and the Execution Chat Starter templates.

**P6-GH-11 — Align `bin/ai-project-init` to `.ai-project/agents/`** *(Low)*

P5 established the platform-agnostic `.ai-project/agents/` convention, but
`bin/ai-project-init` still writes `.github/agents/`. Align the initializer to the agnostic
path.

---

## Out of Scope

- **Re-building the producer or the helper.** ComfyUI (FLUX/SDXL/LTX-Video) and
  `bin/ai-project-visual` are complete and verified end-to-end. P6 builds the
  governance/comprehension layer **above** them, not the API call.
- **Re-debating the ratified binding decisions** (storage-by-link, link-carries-metadata,
  clip-single-parent). All three are settled by the CFO.
- **A cross-cutting / project-spanning editorial reel.** Explicitly deferred — clips are
  single-parent in P6.
- **Standing up or hosting the storage backend.** The framework owns the request-building
  and the link-based binding convention only; where binaries live is each adopting team's
  decision.

---

## Open Design Questions (resolve within the named milestone — non-blocking)

These are HQ-/phase-level design choices flagged in SN-16. They do **not** block phase open.
Each carries a recommended default consistent with the ratified infrastructure-agnostic
stance; the owning milestone makes the final call.

**A. Vendor vs. reference the workflow JSONs.** Ship the workflow JSONs in-repo (e.g. a
`workflows/` dir the helper points at) or reference them on the CFO's ComfyUI host?
- *Resolve in:* M24 (the generative/clips milestone).
- *Recommended default:* **reference, not vendor** — the workflows + models are the
  generative request contract and stay CFO-side, consistent with "the framework does not own
  the storage backend." The verified contract bundle at
  `.ai-project/artifacts/reference/comfyui-endpoint/` stands as the documented reference.

**B. Does the helper gain a link-emitting step?** Does `bin/ai-project-visual` gain an
upload/return-link capability, or is hosting + linking the agent's responsibility outside the
helper?
- *Resolve in:* M23, P6-VC-1 (it determines the helper's output guidance).
- *Recommended default:* **hosting + linking is the agent's responsibility** — keep the
  helper a minimal one-shot `prompt → local file` tool (its current, verified design); the
  agent hosts the file and records the link via the binding convention.

---

## Milestones

### M23: By-Link Storage Model and Binding Convention (2 Epics)

**Goal:** Reverse the v5.0.0 commit-the-binary model to by-link, and define the
link + metadata binding convention that becomes load-bearing under by-link.

**Indicative Epics** (the Milestone Chat owns final epic planning):
- **E23.1 — By-link storage reconciliation** (P6-VC-1) — the explicit reversal across all
  four named surfaces (guide §4/§1, AOG §16.5, helper output guidance, integration test);
  flagged in changelogs as a reversal of v5.0.0 shipped guidance. Resolves Open Design
  Question B.
- **E23.2 — Link + metadata binding convention** (P6-VC-2) — binding schema (link + what /
  level / proposed-vs-implemented / description), per-level placement convention, and
  template/guide updates.

### M24: Comprehension Behavior and Clips (2 Epics)

**Goal:** Make proposed-vs-implemented visuals routine at every level, and define clips as
single-parent documentation that doubles as publishable media. Depends on M23's binding
convention.

**Indicative Epics:**
- **E24.1 — Proposed-vs-implemented comprehension behavior** (P6-VC-3) — AOG §16 two-track
  expectation as default; Structural-first generous coverage; per-level proposed/implemented
  examples bound via the M23 convention.
- **E24.2 — Clips as documentation + publishable media** (P6-VC-4) — single-parent clip
  binding, production from the proposed→implemented arc on the verified LTX-Video path, and
  the publish path (same asset reused). Resolves Open Design Question A.

### M25: Process Refinements (3 Epics)

**Goal:** Close the three P5 carry-forwards. Independent of the visual work; lowest priority
— schedule after M23/M24 or in parallel at the Phase Chat's discretion.

**Indicative Epics:**
- **E25.1 — Phase-closure canonical sequence** (P6-GH-12, High) — README update + version
  bump + tag as mandatory automatic phase-closure steps.
- **E25.2 — Codify SN-13 default-accept** (P6-GH-10, Medium) — into AOG, PSG, and Starter
  templates.
- **E25.3 — Align `ai-project-init` agent path** (P6-GH-11, Low) — write `.ai-project/agents/`,
  not `.github/agents/`.

---

## Success Criteria

### P6 is Complete When:

1. ✅ **By-link storage is the framework default** — the four named surfaces (guide §4/§1,
   AOG §16.5, helper output guidance, integration test) all describe by-link; no instruction
   to commit generated binaries remains; the reversal is recorded in the AOG and guide
   changelogs
2. ✅ **The binding convention is documented and load-bearing** — a visual binding records
   what / level / proposed-vs-implemented / description, with a defined placement per level
3. ✅ **Proposed-vs-implemented coverage is the documented default** — AOG §16 directs every
   level to track both tracks, Structural-first, "nothing is too much"
4. ✅ **A clip is single-parent and reusable** — the clip convention binds one node, produces
   from the verified LTX-Video path, and defines the publish path as the same asset reused
5. ✅ **Phase closure is canonical** — README update, version bump, and tag are mandatory
   automatic steps, no Steering Note required
6. ✅ **SN-13 is codified** — default-accept written into AOG, PSG, and Starter templates
7. ✅ **`ai-project-init` writes the agnostic agent path** — `.ai-project/agents/`

---

## Acceptance Criteria

The CFO (Layer 8) will accept P6 complete when:

- [ ] `governance/guides/visual-artifacts.md` and AOG §16.5 instruct referencing visuals by
  link and explicitly state no generated binaries are committed to git
- [ ] The integration test no longer expects a committed binary under `.ai-project/visuals/`
- [ ] A documented binding schema shows how a link + metadata attaches to an artifact at each
  level
- [ ] AOG §16 directs an agent to produce both a *proposed* and an *implemented* visual for
  its level when `visual_artifacts.enabled: true`
- [ ] The clip convention is documented as single-parent with a defined publish path
- [ ] The phase-closure process lists README update, version bump, and tag as mandatory steps
- [ ] AOG, PSG, and the Execution Chat Starter templates describe the SN-13 default-accept model
- [ ] `bin/ai-project-init` writes `.ai-project/agents/`

---

## Dependencies

### Internal
- P5 visual-artifacts framework on master at v5.0.0 (complete)
- `bin/ai-project-visual` helper shipped and verified (complete — P5 M22)

### External
- **RESOLVED (SN-16).** The ComfyUI workflow share that SN-15 flagged as gating is delivered
  and verified. The contract bundle is preserved at
  `.ai-project/artifacts/reference/comfyui-endpoint/` (`flux-schnell.json`, `sdxl.json`,
  `ltxv-video.json`, `VISUAL-ARTIFACTS.md`). No external dependency remains open for P6.

---

## Timeline

**Estimate:** 7 Epics across 3 Milestones
- M23 (By-Link Storage + Binding): 5–7 days (2 epics) — execute first (foundation)
- M24 (Comprehension + Clips): 5–7 days (2 epics) — depends on M23
- M25 (Process Refinements): 3–5 days (3 small epics) — independent, lowest priority
- **Total: ~2.5–3 weeks**

---

## Reference

### Governing Steering Notes
- **SN-16:** `.ai-project/artifacts/steering-notes/2026-06-29__creation-chat__steering-note__P6-contract-delivered.md`
  — contract delivered + verified; scope sharpened; three ratified decisions (binding)
- **SN-15:** `.ai-project/artifacts/steering-notes/2026-06-28__creation-chat__steering-note__P6-scoping.md`
  — P6 theme/spine; candidate renumber (binding)

### Key Reference Documents
- `.ai-project/artifacts/reference/comfyui-endpoint/` — verified ComfyUI contract (3 workflows + endpoint doc)
- `docs/phases/P5__Process_Hardening_and_Visual_Artifacts/P5__phase-closure-declaration.md` — carry-forwards GH-10, GH-11
- `governance/guides/visual-artifacts.md` — §4 / §1 storage guidance to RECONCILE to by-link
- `governance/AI-OPERATING-GUIDELINES.md` §16.5 — commit guidance to RECONCILE to by-link
- `bin/ai-project-visual` — the verified ComfyUI helper (plumbing — already done)
- `governance/systems/chat-hierarchy.md` — Level 0–4 definition

### Ratified Decisions (settled by the CFO — NOT for re-debate)
1. **Storage by link** — generated visual material is referenced, never committed to git.
2. **Link carries metadata** — what / level / proposed-vs-implemented / short description.
3. **Clip = one parent** — every clip belongs to exactly one governance node.

### Items Excluded from P6
- Producer + helper rebuild — done and verified (SN-16)
- Cross-cutting editorial reel — deferred (clips are single-parent in P6)
- Storage-backend hosting — adopter's responsibility (framework stays infrastructure-agnostic)

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-06-29 | Initial P6 phase spec. Three milestones (M23–M25), 7 Epics. Visual comprehension layer (by-link reversal, binding convention, proposed-vs-implemented behavior, clips) + process carry-forwards (GH-12, GH-10, GH-11). Scope authorized by SN-15 + SN-16; by-link reconciliation named as an explicit deliverable (P6-VC-1). |
