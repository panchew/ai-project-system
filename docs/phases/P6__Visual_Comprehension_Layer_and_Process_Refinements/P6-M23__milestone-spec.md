---
milestone: M23
name: By-Link Storage Model and Binding Convention
phase: P6
status: planned
start_date: 2026-06-29
epics:
  - E23.1
  - E23.2
is_final: false
---

# Milestone M23 — By-Link Storage Model and Binding Convention

## Purpose

Reverse the v5.0.0 **commit-the-binary** storage model to **by-link**, and define the
**link + metadata binding convention** that becomes load-bearing once the link is the only
thing in git. M23 is the **foundation milestone of P6**: M24 (comprehension behavior and
clips) depends on the binding convention this milestone defines, so M23 executes first.

Two tightly-coupled deliverables:

1. **Reverse the storage model (E23.1).** Shipped v5.0.0 guidance instructs committing the
   generated binary into `.ai-project/visuals/<level>/<id>.<ext>` so it "travels with the
   decision record." The CFO has reversed this (SN-16, ratified 2026-06-29): generated visual
   material is **referenced by link, never committed to git**; the **adopter owns the storage
   backend**. The reversal must touch the four named surfaces and be recorded in the AOG and
   guide changelogs as an explicit reversal of v5.0.0 shipped guidance.
2. **Define the binding convention (E23.2).** Once the link is the only thing in git, the
   **metadata is load-bearing**. Define the binding schema (link + what / level /
   proposed-vs-implemented / short description) and the per-level placement convention, and
   update the guide and the relevant templates so each level knows how to record a binding.

> **This milestone is governance/documentation, not plumbing.** The producer (three ComfyUI
> workflows) and the helper (`bin/ai-project-visual`) are done and verified end-to-end
> (SN-16). M23 changes what the framework *says about storing and binding* the output — not
> how the output is generated.

---

## Binding Design Decisions (SN-16, 2026-06-29 — apply in full, do not re-examine)

Source: `.ai-project/artifacts/steering-notes/2026-06-29__creation-chat__steering-note__P6-contract-delivered.md`.

1. **Storage by link** — generated visual material is referenced by link, never committed to git.
2. **Link carries metadata** — every binding records *what* the visual is, *which level* it
   binds to, *proposed-vs-implemented*, and a *short text description* (so the record survives
   link rot).
3. **Clip = one parent** — every clip belongs to exactly one governance node. *(Carried for
   continuity; the clip convention is M24's concern, not M23's.)*

These three decisions are settled by the CFO and are **not** for re-debate in this milestone.

---

## Problem Statement

P5 (v5.0.0) shipped the visual-artifacts framework with explicit instructions to **commit
generated binaries into the version-controlled project** so each visual "travels with its
decision record." That guidance is now reversed: version control is the wrong home for
generated binary material, and the framework has always been infrastructure-agnostic about
where adopter resources live (endpoints, agents — and now storage). The reversal is not a
tweak; it is the single biggest governance change in P6, and it is named as an explicit,
scoped deliverable so it cannot leak in as an incidental edit.

A reversal alone is not enough. Once the binary is **not** in git, the only thing in git is a
**link** — and a bare link rots. The framework therefore needs a **binding convention**: a
link plus a small, load-bearing block of metadata that records what the visual is, which
level it belongs to, whether it shows the *proposed* or *implemented* state, and a short text
description that outlives the link. M23 delivers both halves: the reversal, then the binding
convention that makes by-link survivable.

---

## Goals

By the end of this milestone:

1. **By-link is the framework default.** All four named surfaces describe referencing visuals
   by link; **no instruction to commit a generated binary remains** anywhere in the guide, the
   AOG, the helper's output guidance, or the integration-test surface (E23.1).
2. **The reversal is recorded as a reversal.** The AOG changelog and a guide changelog both
   record the change explicitly as a **reversal of v5.0.0 shipped guidance** (E23.1).
3. **The binding schema is documented.** A visual binding records a **link** plus the four
   metadata fields (what / level / proposed-vs-implemented / short description), with a defined
   representation in `governance/guides/visual-artifacts.md` (E23.2).
4. **A placement convention exists per level.** The convention states which governance artifact
   a binding attaches to — and how the link gets there — at each of Creation / HQ / Phase /
   Milestone / Epic, with the relevant templates updated so each level can record a binding
   (E23.2).

---

## Non-Goals

This milestone explicitly does **not**:

- **Rebuild the producer or the helper.** ComfyUI (FLUX/SDXL/LTX-Video) and
  `bin/ai-project-visual` are complete and verified. M23 changes storage/binding guidance, not
  the generation path. The helper's *behaviour* is unchanged; only its **output guidance**
  (docstring/help text framing of `--output`) is clarified.
- **Add an upload or link-emitting step to the helper.** See *Open Design Question B —
  Resolved* below: the helper stays a minimal one-shot `prompt → local file` tool.
- **Touch structural-diagram guidance.** Mermaid/PlantUML are **text** and continue to live in
  git, inline or as sibling `.mmd` / `.puml` files. Only **generated binaries** move to by-link.
- **Design the comprehension behavior or the clip convention.** Proposed-vs-implemented routine
  behavior (P6-VC-3) and clips (P6-VC-4) are **M24**. M23 defines the binding mechanism that
  M24 will use; it does not define M24's behavior.
- **Stand up or host a storage backend.** Where binaries live is the adopting team's decision.
- Re-examine the three SN-16 ratified decisions.

---

## In Scope

- **E23.1** — by-link reconciliation across the four named surfaces (guide §4 + §1 note; AOG
  §17.5; `bin/ai-project-visual` output guidance; the integration-test surface) and the
  reversal records in the AOG and guide changelogs.
- **E23.2** — the binding schema (link + four metadata fields), the per-level placement
  convention, and the guide/template updates that let each level record a binding.

## Out of Scope

- Producer/helper rebuild; structural-diagram guidance; M24 comprehension behavior; the clip
  convention; storage-backend hosting; any M25 process-refinement work.

---

## Planned Epics

### Confirmed Epics

- **E23.1 — By-link storage reconciliation** (P6-VC-1)
- **E23.2 — Link + metadata binding convention** (P6-VC-2)

> **Artifact scope (GH-8 adjacency):** the Phase Chat produces only this Milestone spec and
> the Milestone Execution Chat Starter. The **Milestone Chat** owns final epic planning and
> authors both Epic specs and both Epic Execution Chat Starters for E23.1 and E23.2. No
> Phase-level Epic drafts exist; the epic detail below is the indicative decomposition and the
> verified grounding the Milestone Chat plans against — it may adjust epic boundaries **within
> M23's scope** but may not add or drop the named deliverables.

### Deferred Epics

- None.

---

## Epic Detail

### E23.1 — By-link storage reconciliation (P6-VC-1)

**Source:** SN-16 (ratified 2026-06-29) — the single biggest governance change in P6, named as
an explicit scoped deliverable so it cannot enter as an incidental edit.

**Binding context:** Generated visual material is **referenced by link**, not committed to the
version-controlled project. **No binaries in git.** The adopter owns the storage backend. This
**reverses** shipped v5.0.0 guidance.

**Grounding (verified on this branch — anchors the Milestone Chat plans against):**

- `governance/guides/visual-artifacts.md`
  - **§4 "Output formats"** — the format table is fine (it lists `.png` / `.webp` / `.mp4`).
    The **prose under it** is the reversal target: it instructs "Commit generated artifacts
    under the consuming project's `.ai-project/` namespace … `.ai-project/visuals/<level>/<artifact-id>.<ext>`
    … Commit the generated file **together with** the artifact … so the visual travels with its
    decision record."
  - **§1 source-repo note** — "The governance **source** repository keeps `enabled: false`. It
    ships the guidance, the helper, and the test — **not generated output**." Under by-link this
    generalizes: **no** project commits generated binaries, not only the source repo.
  - **§5 worked examples** — every example writes `--output .ai-project/visuals/<level>/<id>.png`.
    These example paths imply commit and **must be reconciled** so they do not contradict the
    §4 rewrite (the acceptance criterion is "no instruction to commit generated binaries
    remains" — residual example paths count).
- `governance/AI-OPERATING-GUIDELINES.md` **§17.5 "What to commit, and where"** — the bullet
  "**Generated** artifacts are written under … `.ai-project/visuals/<level>/<artifact-id>.<ext>`
  … Commit the generated file together with the artifact that references it, so the visual
  travels with its decision record." Rewrite to by-link. The §17.5 source-repo bullet
  generalizes the same way as the guide's §1 note. AOG is at **v2.2.0**.
- `bin/ai-project-visual` **output guidance** — the docstring usage example (`--output
  .ai-project/visuals/hq/architecture.png`) and the `--output` help text frame `--output` as a
  committed project path. Clarify that `--output` writes a **local working file** to be hosted
  and linked, **not** committed. **The helper's runtime behaviour does not change** — only the
  guidance/framing. (Resolves Open Design Question B; see below.)
- **Integration-test surface** — `tests/integration/test_visual_artifacts_helper.py` **already
  writes to a `tmp_path` and asserts bytes > 0; it does NOT assert a committed binary under
  `.ai-project/visuals/`.** The epic must **verify** this and, finding no committed-binary
  assertion, **record that the test is already consistent with by-link** rather than make a
  cosmetic edit. If any residual example path inside the test implies commit, reconcile it; do
  not invent a test change the by-link model does not require.

**Deliverables:**

1. Rewrite the guide §4 prose and the §1 source-repo note to the by-link model; reconcile the
   §5 worked-example `--output` paths so none implies committing a generated binary.
2. Rewrite the AOG §17.5 "Generated artifacts … and committed" bullet (and the §17.5
   source-repo bullet) to the by-link model.
3. Clarify the `bin/ai-project-visual` output guidance (docstring + `--output` help) that
   `--output` writes a local working file to host and link, not commit — **no behaviour change,
   no upload step**.
4. Verify the integration-test surface; record that it is already by-link-consistent (or
   reconcile a residual example path) — no make-work assertion edit.
5. Record the change as an explicit **reversal of v5.0.0 shipped guidance** in **both** the AOG
   changelog and a guide changelog. *(Note: the guide has no changelog section today; adding
   one — or recording the reversal via an equivalent dated note in the guide — is part of this
   deliverable.)*

**Definition of Done:**
- [ ] Guide §4, §1 note, and §5 example paths describe by-link; no commit-the-binary instruction remains
- [ ] AOG §17.5 describes by-link; no commit-the-binary instruction remains
- [ ] `bin/ai-project-visual` output guidance frames `--output` as a local working file (behaviour unchanged)
- [ ] The integration-test surface is verified by-link-consistent (recorded), with no make-work edit
- [ ] The reversal is recorded as a reversal of v5.0.0 guidance in the AOG changelog and a guide changelog
- [ ] Full test suite passes (integration test still skips at `enabled: false`)

**Acceptance Criteria:**
- [ ] All four named surfaces describe by-link; no instruction to commit generated binaries remains anywhere
- [ ] The reversal is recorded in the AOG and guide changelogs, explicitly as a reversal of v5.0.0
- [ ] Structural-diagram guidance is unchanged

---

### E23.2 — Link + metadata binding convention (P6-VC-2)

**Source:** SN-16 (ratified 2026-06-29) — load-bearing under by-link because the link is the
only thing in git.

**Depends on E23.1** — the binding convention documents how a **link** (not a committed path)
attaches to an artifact, so it must be written against the by-link model E23.1 establishes.
E23.1 and E23.2 also both edit `governance/guides/visual-artifacts.md`; serialize them (or use
a worktree, GH-2) to avoid contention.

**Grounding (verified — candidate placement surfaces per level):**

| Level | Governing artifact a binding plausibly attaches to | Note |
|-------|----------------------------------------------------|------|
| Creation | `governance/templates/seed.md` / Project Brief | Visual intent is **already elicited** here (seed.md Rule 4, "What does success look like visually?") — the natural home to also record the binding |
| HQ | HQ-level governing artifact (e.g., HQ chat opener / architecture record) | HQ produces system architecture |
| Phase | `governance/templates/phase-spec.md` | |
| Milestone | `governance/templates/milestone-spec.md` | |
| Epic | `governance/templates/epic-spec.md` | |

> The exact per-level placement (which artifact, and the precise location within it) is
> **E23.2's design call within M23's scope**. The table above names verified candidate surfaces;
> the milestone fixes the requirement — *a defined placement per level* — not the final choice.

**Deliverables:**

1. **Binding schema** — define a documented representation of a visual binding: a **link** plus
   the four load-bearing metadata fields:
   - **what** the visual is (image / infographic / mockup / diagram / clip)
   - **which level** it binds to (Creation / HQ / Phase / Milestone / Epic)
   - **proposed vs. implemented** (the two-track state)
   - a **short text description** (so the record survives link rot)
2. **Per-level placement convention** — for each of the five levels, state which governance
   artifact a binding attaches to and how the link gets there.
3. **Guide + template updates** — document the schema and placement convention in
   `governance/guides/visual-artifacts.md`, and update the relevant per-level templates (the
   verified candidates above) so each level has a defined place to record a binding.

**Definition of Done:**
- [ ] The binding schema is documented with a concrete representation and all four metadata fields plus the link
- [ ] A placement convention is defined for every level (Creation / HQ / Phase / Milestone / Epic)
- [ ] `governance/guides/visual-artifacts.md` documents the schema and the per-level convention
- [ ] The relevant per-level templates carry a defined place to record a binding
- [ ] Full test suite passes

**Acceptance Criteria:**
- [ ] The binding schema documents the link + all four metadata fields
- [ ] A placement convention is defined per level
- [ ] The convention is consistent with the by-link model from E23.1 (binds a link, never a committed path)

---

## Open Design Question B — Resolved (recommended default adopted)

**Question (SN-16, phase spec):** Does `bin/ai-project-visual` gain a link-emitting/upload
step, or is hosting + linking the agent's responsibility outside the helper?

**Resolution (binding for M23):** Adopt the recommended default. The helper **stays a minimal
one-shot `prompt → local file` tool** (its current, verified design). **No upload or
link-emitting step is added.** Hosting the local working file and recording its link is the
**agent's responsibility**, carried out via the E23.2 binding convention. E23.1's helper-output
guidance reflects this: `--output` writes a local working file to host and link, not a
committed path. This resolution is within milestone authority (the phase starter directs
resolving the non-blocking Open Design Questions within the owning milestone) and removes the
ambiguity for the Epic, which implements guidance only — not a behaviour change.

*(Open Design Question A — vendor vs. reference the workflow JSONs — belongs to M24 and is not
resolved here.)*

---

## Branch Strategy

```
master
└── phase/P6                  (branched at phase open; this milestone plans here)
    └── milestone/M23          ← this milestone (Milestone Chat branches from phase/P6)
        ├── epic/P6-M23-E23.1   ← By-link storage reconciliation
        └── epic/P6-M23-E23.2   ← Link + metadata binding convention
```

Epic PRs target `milestone/M23`. Consolidation PR: `milestone/M23 → phase/P6`.
M23 is **not** the final P6 milestone (`is_final: false`); M24 and M25 follow on `phase/P6`.

---

## Prerequisites

- `phase/P6` carries the committed P6 phase spec and Phase Execution Chat Starter, plus **this
  Milestone spec and its Milestone Execution Chat Starter** (git-tracked — verify with
  `git ls-files --error-unmatch <path>`, the GH-1 convention).
- These reversal/binding targets are present and git-tracked on `phase/P6`:
  - `governance/guides/visual-artifacts.md`
  - `governance/AI-OPERATING-GUIDELINES.md`
  - `bin/ai-project-visual`
  - `tests/integration/test_visual_artifacts_helper.py`
  - `governance/templates/seed.md`, `phase-spec.md`, `milestone-spec.md`, `epic-spec.md`
- **No external dependency.** SN-16 confirms the ComfyUI contract is delivered and verified;
  the reference bundle stands at `.ai-project/artifacts/reference/comfyui-endpoint/`. M23 needs
  no live endpoint (the integration test skips at `enabled: false`).

---

## Dependencies and Sequencing

- **E23.1 → E23.2** (soft dependency): the binding convention is written against the by-link
  model, and both epics edit `governance/guides/visual-artifacts.md`. Execute E23.1 first,
  accept/merge it, then branch E23.2 from the merged `milestone/M23`. Use a worktree (GH-2) if
  any overlap arises before merge.
- No cross-milestone dependency: M24 depends on M23's output, not the reverse; M25 is independent.

---

## Definition of Done (Milestone)

- [ ] E23.1 and E23.2 each meet their Definition of Done above
- [ ] Both epic branches merged to `milestone/M23`
- [ ] No instruction to commit a generated binary remains anywhere in the four named surfaces
- [ ] The binding schema and per-level placement convention are documented
- [ ] The reversal is recorded in the AOG and guide changelogs as a reversal of v5.0.0
- [ ] Full test suite passes on `milestone/M23` (integration test skipped at `enabled: false`)
- [ ] Milestone Closure Declaration produced

---

## Acceptance Criteria (Milestone)

1. `governance/guides/visual-artifacts.md` and AOG §17.5 instruct referencing visuals by link
   and explicitly state no generated binaries are committed to git (E23.1).
2. `bin/ai-project-visual` output guidance frames `--output` as a local working file to host
   and link, with no behaviour change and no upload step (E23.1).
3. The integration-test surface no longer implies a committed binary under `.ai-project/visuals/`
   (verified by-link-consistent) (E23.1).
4. The reversal is recorded as a reversal of v5.0.0 in the AOG and guide changelogs (E23.1).
5. A documented binding schema shows how a link + the four metadata fields attach to an
   artifact, with a defined placement per level (E23.2).
6. Structural-diagram guidance is unchanged (E23.1/E23.2).

---

## Timeline

**Target Start:** 2026-06-29
**Target Completion:** 2026-07-06 (5–7 days per Phase spec estimate; 2 epics)
**Actual Start:** Not started
**Actual Completion:** Not started

---

## Notes

- M23 is the **foundation of P6**: M24 (comprehension behavior + clips) depends on the binding
  convention defined here. Plan and execute M23 before M24.
- The reversal (P6-VC-1) is the **single biggest governance change in P6**. It is named as an
  explicit, scoped deliverable across four surfaces precisely so it cannot enter as an
  incidental edit and so its "reversal of v5.0.0" nature is recorded in the changelogs.
- The verified facts in the Epic Detail (the integration test already writes to a tmp path; the
  guide has no changelog today; the §5 examples carry committing paths) are grounding for the
  Milestone Chat — they keep the epics from either missing a surface or making a make-work edit.
- Default-accept (SN-13) governs delivery: clean Epic/Milestone deliveries are auto-accepted;
  Review Decisions are the exception path only.
- The exact representation of the binding block and the final per-level placement are
  Epic-level design calls **within M23's scope**; the milestone fixes the contract (four
  surfaces by-link; link + four metadata fields; a placement per level), not the wording.
