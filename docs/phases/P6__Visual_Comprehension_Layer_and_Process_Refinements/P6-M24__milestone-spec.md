---
milestone: M24
name: Comprehension Behavior and Clips
phase: P6
status: planned
start_date: 2026-06-29
epics:
  - E24.1
  - E24.2
is_final: false
---

# Milestone M24 — Comprehension Behavior and Clips

## Purpose

Make the visual layer **do its job**: turn the governance flow into a continuous visual
narrative the CFO can follow with low cognitive load. M23 delivered the *mechanism* — by-link
storage and the §7 binding convention (link + What / Level / **State** / Description). M24
delivers the *behavior* that uses it:

1. **Proposed-vs-implemented becomes routine at every level (E24.1).** Establish, in AOG §16,
   the expectation that every level produces both tracks — a **proposed** visual before build
   and an **implemented** visual after — generously ("nothing is too much"), **Structural-first**
   because most of it is free text (Mermaid/PlantUML), with per-level examples bound via the
   M23 §7 convention.
2. **Clips become single-parent documentation that doubles as publishable media (E24.2).** A
   **clip** binds to exactly one governance node and tells that node's proposed→implemented
   story, produced on the **verified LTX-Video path** (`ltxv-video.json` → `.webm`), with a
   defined publish path (YouTube/TikTok/IG/FB) where the published asset is the **same hosted
   asset reused**, not a separate production.

> **M24 is governance/behavior, not plumbing and not new schema.** The producer (ComfyUI
> FLUX/SDXL/LTX-Video) and the helper (`bin/ai-project-visual`) are done and verified (SN-16);
> the binding schema and its `State` field are done and merged (M23 / E23.2). M24 directs how
> the framework *uses* them — it does not rebuild them or redefine the binding block.

---

## Binding Design Decisions (SN-16, 2026-06-29 — apply in full, do not re-examine)

Source: `.ai-project/artifacts/steering-notes/2026-06-29__creation-chat__steering-note__P6-contract-delivered.md`.

1. **Storage by link** — generated visual material is referenced by link, never committed to git.
   *(M23 reversal — M24 must not regress it; a clip is hosted and linked, never committed.)*
2. **Link carries metadata** — the §7 binding records What / Level / **State** / Description.
   *(M24 uses this; it does not change it.)*
3. **Clip = one parent** — every clip belongs to exactly **one** governance node (one epic,
   milestone, or phase) and tells that node's proposed→implemented story, using the same §7
   binding as any other visual. **No cross-cutting editorial reel in P6** — a project-spanning
   montage is a separate later capability if ever wanted.

The "nothing is too much" coverage bar and the proposed/implemented two-track are CFO-set and
binding (SN-15/SN-16). They are **not** for re-debate in this milestone.

---

## Problem Statement

P5 shipped the visual framework inert; M23 turned storage by-link and gave every level a §7
home for a link + metadata, with a `State` field that *can* hold `proposed` or `implemented`.
But a mechanism that *can* be used is not the same as a behavior that *is* used. Nothing yet
tells an agent that producing **both** a proposed and an implemented visual is the routine
default at every level, nor how generous to be, nor that the cheap path (Structural text) should
carry most of the coverage. And the most CFO-facing artifact — a **clip** that narrates a
node's proposed→implemented arc and can be published to social channels — has a verified
production path (LTX-Video) and a `What: clip` slot in §7, but no documented convention for how
it is bound (single-parent), produced (from the arc), or reused (publish = same asset). M24
closes both gaps: the routine two-track behavior, and the clip convention.

---

## Goals

By the end of this milestone:

1. **Proposed-vs-implemented is the documented default.** AOG §16 directs every level to track
   **both** a proposed (before build) and an implemented (after) visual when
   `visual_artifacts.enabled: true`, generously, **Structural-first**, recorded via the §7
   binding's `State` field (E24.1).
2. **Per-level proposed/implemented examples exist.** The guide shows, per level, what
   "proposed" and "implemented" look like and how each is bound via §7 (E24.1).
3. **The clip convention is documented as single-parent.** A clip binds to exactly one node
   (epic/milestone/phase) via §7 (`What: clip`), tells that node's proposed→implemented story,
   and is hosted-and-linked (by-link, never committed) (E24.2).
4. **Clip production + publish path are documented.** How a clip is produced from the
   proposed→implemented arc on the verified LTX-Video path (`ltxv-video.json` → `.webm`), and
   the publish path (YouTube/TikTok/IG/FB) as the **same hosted asset reused** — not a separate
   production (E24.2).

---

## Non-Goals

This milestone explicitly does **not**:

- **Rebuild the producer or helper, or add plumbing.** ComfyUI and `bin/ai-project-visual` are
  done and verified. M24 changes guidance, not generation. No helper flag, no upload step
  (Open Design Question B stays resolved from M23).
- **Redefine the binding schema or its `State` field.** E23.2 delivered the five-element §7
  block and the proposed/implemented `State`. E24.1 directs its *routine use*; it does not
  restate or alter the schema (documented once, in §7).
- **Regress by-link.** A clip and every generated visual is hosted and linked, never committed.
- **Build a publishing pipeline or stand up hosting.** The publish path is documented as
  *reuse of the same hosted asset*; where it is hosted/published is the adopter's decision
  (infrastructure-agnostic).
- **Produce a cross-cutting / project-spanning editorial reel.** Explicitly deferred — clips
  are single-parent in P6 (SN-16 decision 3).
- **Do M25 process-refinement work** (GH-12 / GH-10 / GH-11), or re-open any M23 surface.

---

## In Scope

- **E24.1** — AOG §16 two-track ("proposed-vs-implemented") expectation as the routine default
  at every level, Structural-first/"nothing is too much", with per-level proposed/implemented
  examples bound via the §7 `State` field.
- **E24.2** — the clip convention: single-parent binding (`What: clip`), production from the
  proposed→implemented arc on the verified LTX-Video path, and the publish path as the same
  hosted asset reused. Resolves Open Design Question A.

## Out of Scope

- Producer/helper/plumbing changes; binding-schema redefinition; by-link regression; a
  publishing pipeline or hosting; the cross-cutting reel; any M25 work; any M23 surface re-open.

---

## Planned Epics

### Confirmed Epics

- **E24.1 — Proposed-vs-implemented comprehension behavior** (P6-VC-3)
- **E24.2 — Clips as documentation + publishable media** (P6-VC-4)

> **Artifact scope (GH-8 adjacency):** the Phase Chat produces only this Milestone spec and the
> Milestone Execution Chat Starter. The **Milestone Chat** owns final epic planning and authors
> both Epic specs and both Epic Execution Chat Starters for E24.1 and E24.2. No Phase-level Epic
> drafts exist; the epic detail below is the indicative decomposition and the verified grounding
> the Milestone Chat plans against — it may adjust epic boundaries **within M24's scope** but may
> not add or drop the named deliverables.

### Deferred Epics

- None.

---

## Epic Detail

### E24.1 — Proposed-vs-implemented comprehension behavior (P6-VC-3)

**Source:** SN-16 (ratified 2026-06-29); phase spec P6-VC-3. The "nothing is too much" coverage
bar and the proposed/implemented two-track are CFO-set and binding.

**Grounding (verified on `phase/P6` — anchors the Milestone Chat plans against):**

- **The mechanism already exists — do not rebuild it.** Guide §7 defines the five-element
  binding and states explicitly that **`State` is a field, not a second schema**: "A level may
  carry both a `proposed` binding (the visual intent, before build) and an `implemented`
  binding (what was actually built) — the same five-element block, distinguished by **State**."
  E24.1 establishes the *expectation to routinely produce both*, not a new schema.
- **AOG §16 is the home for the behavior.** §16 currently runs §16.1 opt-in gating, §16.2
  per-level abstraction (the level→visual-type table), §16.3 two modes (Structural / Generative),
  §16.4 tool-capability gating, §16.5 what-to-commit (now by-link). The two-track expectation is
  a **new subsection** (e.g. §16.6 "Proposed vs. implemented"); §16.2/§16.3 may gain a sentence
  tying the per-level abstraction and Structural-first preference to the two tracks.
- **Structural-first is why generous coverage is cheap.** §16.3 / guide §2 already prefer
  Structural (Mermaid/PlantUML — text, free, no endpoint) for architecture/scope/component/flow
  diagrams; Generative (ComfyUI) is for concept/vision/mockups/clips. E24.1 makes the
  "nothing is too much" bar affordable by leaning on Structural for most of the coverage.
- **Per-level examples attach to the guide.** The guide §5 worked examples currently show **one**
  visual per level; E24.1 extends the per-level guidance to show a **proposed** and an
  **implemented** example per level, each recorded as a §7 binding (distinguished by `State`).

**Deliverables:**

1. AOG §16 guidance (new subsection) establishing the **two-track expectation** — every level
   produces a *proposed* visual before build and an *implemented* visual after, as the routine
   default when the capability is enabled — with the **"nothing is too much"** coverage bar and
   the **Structural-first** preference stated.
2. Per-level worked examples (in `governance/guides/visual-artifacts.md`) showing what
   *proposed* and *implemented* look like at each level (Creation / HQ / Phase / Milestone /
   Epic), each recorded as a §7 binding via the `State` field — reusing, not restating, the §7
   schema.
3. A changelog entry in the AOG (and the guide changelog) recording the added behavior.

**Definition of Done:**
- [ ] AOG §16 has a subsection directing both a *proposed* and an *implemented* visual per level when enabled, with the "nothing is too much" bar and Structural-first preference
- [ ] The guide shows a per-level proposed/implemented example, each bound via §7 (`State`)
- [ ] The §7 schema is referenced, not redefined or restated
- [ ] The behavior is recorded in the AOG and guide changelogs
- [ ] Full test suite passes (no plumbing touched; integration test still skips at `enabled: false`)

**Acceptance Criteria:**
- [ ] AOG §16 directs every level to produce both a proposed and an implemented visual when `enabled: true`
- [ ] Per-level proposed/implemented examples exist, bound via the M23 §7 convention
- [ ] By-link and the §7 schema are unchanged (no regression, no redefinition)

---

### E24.2 — Clips as documentation + publishable media (P6-VC-4)

**Source:** SN-16 (ratified 2026-06-29); phase spec P6-VC-4. Clip = one parent (binding
decision 3).

**Depends on E24.1** — a clip *is* the proposed→implemented arc of one node rendered as video,
so it builds on E24.1's two-track behavior. E24.1 and E24.2 also both touch AOG §16 and the
guide; serialize them (or use a worktree, GH-2) to avoid contention.

**Grounding (verified — anchors the Milestone Chat plans against):**

- **`clip` is already a `What` value in §7** (`image | infographic | mockup | diagram | clip`).
  E24.2 does **not** add it; it documents how a clip binds (single-parent), is produced, and is
  reused. A clip is bound like any visual: a §7 block whose `Level` is the one node it belongs to.
- **The LTX-Video path is verified end-to-end.** The reference bundle
  (`.ai-project/artifacts/reference/comfyui-endpoint/`) documents `ltxv-video.json` → `.webm`
  via `bin/ai-project-visual --type video --workflow workflows/ltxv-video.json`; `VISUAL-ARTIFACTS.md`
  records LTX-Video → valid `.webm` as verified (defaults 768×512, 97 frames @ 25 fps). M24 needs
  **no new plumbing** — it documents production on this existing path.
- **Single-parent (SN-16 decision 3).** A clip binds to exactly **one** node — one epic,
  milestone, or phase — and tells that node's proposed→implemented story. This is naturally
  expressible in §7 (a single `Level`/parent), but the **clip-specific single-parent rule** and
  the **no-cross-cutting-reel** boundary must be stated.
- **By-link applies to clips too.** A clip is hosted and linked via §7, **never committed** — the
  M23 reversal covers video output exactly as it covers images.
- **Publish = reuse, not re-produce.** The publish path to YouTube/TikTok/IG/FB is the **same
  hosted asset reused**; the framework documents the path, it does not build a publisher or host
  the asset (infrastructure-agnostic, consistent with by-link).

**Deliverables:**

1. **Clip convention (single-parent).** Document, in AOG §16 and/or the guide, that a clip binds
   to exactly one governance node (epic/milestone/phase) via §7 (`What: clip`), tells that node's
   proposed→implemented story, and is hosted-and-linked (never committed). State the
   no-cross-cutting-reel boundary (deferred in P6).
2. **Production from the arc.** Document how a clip is produced from the proposed→implemented arc
   on the verified LTX-Video path (`ltxv-video.json` → `.webm`, via `bin/ai-project-visual`),
   referencing the existing contract — **no new helper capability**.
3. **Publish path.** Document the publish path (YouTube/TikTok/IG/FB) as the **same hosted asset
   reused**, not a separate production; keep it infrastructure-agnostic (no pipeline, no hosting).
4. **Resolve Open Design Question A** (see below) and record the resolution.
5. A changelog entry recording the clip convention.

**Definition of Done:**
- [ ] The clip convention is documented as single-parent, bound via §7 (`What: clip`), hosted-and-linked
- [ ] Clip production is documented on the verified LTX-Video path, with no new plumbing
- [ ] The publish path is documented as the same hosted asset reused (no pipeline/hosting built)
- [ ] The no-cross-cutting-reel boundary is stated
- [ ] Open Design Question A is resolved and recorded (reference, not vendor — see below)
- [ ] The clip convention is recorded in the AOG and/or guide changelog
- [ ] Full test suite passes (no plumbing touched)

**Acceptance Criteria:**
- [ ] The clip convention is documented as single-parent with a defined publish path
- [ ] Clip production references the verified LTX-Video path; no helper change is introduced
- [ ] By-link holds for clips (hosted + linked, never committed)

---

## Open Design Question A — Resolved (recommended default adopted)

**Question (SN-16, phase spec):** Vendor the workflow JSONs in-repo (e.g. a `workflows/` dir the
helper points at) or reference them on the CFO's ComfyUI host?

**Resolution (binding for M24):** Adopt the recommended default — **reference, not vendor.** The
workflows + models are the **generative request contract** and stay **CFO-side**, consistent with
"the framework does not own the storage backend" and the infrastructure-agnostic stance for
endpoints, agents, and (since M23) storage. The verified contract bundle at
`.ai-project/artifacts/reference/comfyui-endpoint/` (`flux-schnell.json`, `sdxl.json`,
`ltxv-video.json`, `VISUAL-ARTIFACTS.md`) stands as the **documented reference** — a preserved
copy of the CFO's host-side contract, not the vendored runtime. E24.2's clip-production guidance
references this bundle rather than shipping a runnable `workflows/` directory. This resolution is
within milestone authority (the phase starter directs resolving the non-blocking Open Design
Questions within the owning milestone) and removes the ambiguity for the Epic.

*(Open Design Question B — helper link-emitting step — was resolved in M23 and stays resolved:
no upload step; hosting + linking is the agent's responsibility.)*

---

## Branch Strategy

```
master
└── phase/P6                  (M23 consolidated here — merge 24a36f6)
    └── milestone/M24          ← this milestone (Milestone Chat branches from phase/P6)
        ├── epic/P6-M24-E24.1   ← Proposed-vs-implemented comprehension behavior
        └── epic/P6-M24-E24.2   ← Clips as documentation + publishable media
```

Epic PRs target `milestone/M24`. Consolidation PR: `milestone/M24 → phase/P6`.
M24 is **not** the final P6 milestone (`is_final: false`); M25 follows on `phase/P6`.

---

## Prerequisites

- `phase/P6` carries the consolidated M23 work — verify the M23 surfaces are present and
  git-tracked (`git ls-files --error-unmatch <path>`, the GH-1 convention):
  - `governance/AI-OPERATING-GUIDELINES.md` (§16, by-link §16.5, v2.3.0)
  - `governance/guides/visual-artifacts.md` (the §7 binding convention + `State` field)
  - `governance/templates/seed.md`, `genesis.md`, `phase-spec.md`, `milestone-spec.md`,
    `epic-spec.md` (each carrying its §7 binding home)
  - `.ai-project/artifacts/reference/comfyui-endpoint/` (the verified LTX-Video contract)
- This Milestone spec and its Milestone Execution Chat Starter are git-tracked on `phase/P6`.
- **No external dependency.** SN-16 confirms the ComfyUI contract (incl. LTX-Video → `.webm`) is
  delivered and verified. M24 is guidance — it needs **no** live endpoint (the integration test
  stays skipped at `enabled: false`).

---

## Dependencies and Sequencing

- **E24.1 → E24.2** (soft dependency): a clip is the proposed→implemented arc rendered as video,
  so E24.2 builds on E24.1's two-track behavior; both also edit AOG §16 and the guide. Execute
  E24.1 first, accept/merge it, then branch E24.2 from the merged `milestone/M24`. Use a worktree
  (GH-2) if overlap arises before merge.
- **Cross-milestone:** M24 depends on **M23's** §7 binding convention (now merged on `phase/P6`);
  M25 is independent of M24.

---

## Definition of Done (Milestone)

- [ ] E24.1 and E24.2 each meet their Definition of Done above
- [ ] Both epic branches merged to `milestone/M24`
- [ ] AOG §16 directs proposed + implemented at every level (Structural-first, "nothing is too much")
- [ ] The clip convention is documented (single-parent, LTX-Video production, publish-as-reuse)
- [ ] Open Design Question A is resolved (reference, not vendor) and recorded
- [ ] By-link and the §7 schema are unchanged (no regression, no redefinition)
- [ ] Full test suite passes on `milestone/M24` (integration test skipped at `enabled: false`)
- [ ] Milestone Closure Declaration produced

---

## Acceptance Criteria (Milestone)

1. AOG §16 directs an agent to produce both a *proposed* and an *implemented* visual for its
   level when `visual_artifacts.enabled: true`, generously and Structural-first (E24.1).
2. Per-level proposed/implemented examples exist, each bound via the M23 §7 convention (E24.1).
3. The clip convention is documented as single-parent with a defined publish path (E24.2).
4. Clip production references the verified LTX-Video path; no helper change is introduced (E24.2).
5. By-link holds for clips and the §7 schema is unchanged (E24.1 / E24.2).

---

## Timeline

**Target Start:** 2026-06-29
**Target Completion:** 2026-07-06 (5–7 days per Phase spec estimate; 2 epics)
**Actual Start:** Not started
**Actual Completion:** Not started

---

## Notes

- M24 is where the visual layer **earns its keep**: it converts M23's mechanism into routine
  proposed-vs-implemented coverage and the single most CFO-facing artifact — the clip.
- **Behavior, not schema.** The recurring risk for both epics is restating or redefining what M23
  already shipped (the §7 block, the `State` field). The Milestone Chat must keep E24.1/E24.2 as
  *guidance that uses §7*, referencing the schema documented once in the guide.
- **No plumbing.** Both epics are documentation; the helper and the LTX-Video path are unchanged.
  The verified contract bundle is the reference E24.2 points at — Open Design Question A resolves
  to *reference, not vendor*.
- **Publishable clips are a byproduct, not the driver** (phase spec): the clip exists to help the
  CFO follow the flow; the publish path reuses the same hosted asset.
- Default-accept (SN-13) governs delivery: clean Epic/Milestone deliveries are auto-accepted;
  Review Decisions are the exception path only.
- The exact AOG subsection number, the wording of the per-level examples, and where the clip
  convention sits (AOG §16 vs. a guide section) are Epic-level design calls **within M24's
  scope**; the milestone fixes the contract (two-track default at every level; single-parent
  clip with LTX-Video production and publish-as-reuse; ODQ A = reference), not the wording.
