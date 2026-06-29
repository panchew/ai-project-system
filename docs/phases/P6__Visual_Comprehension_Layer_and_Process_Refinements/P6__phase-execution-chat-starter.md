# Phase Execution Chat Starter — P6

**Phase:** P6 — Visual Comprehension Layer and Process Refinements
**Project:** ai-project-system
**Repository:** https://github.com/panchew/ai-project-system
**Phase Spec:** `docs/phases/P6__Visual_Comprehension_Layer_and_Process_Refinements/P6__phase-spec.md`
**Issued:** 2026-06-29

---

## Governance References

You are operating under the AI Project System governance framework as a **Phase Chat** for Phase P6.

**Authoritative governance documents:**
- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) v2.1.0 (Effective: 2026-06-23)
- [AI-OPERATING-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/AI-OPERATING-GUIDELINES.md) v2.2.0 (Effective: 2026-06-28)

**Governance hierarchy (for this session):**
1. PROJECT-SYSTEM-GUIDELINES.md (highest authority)
2. AI-OPERATING-GUIDELINES.md v2.2.0
3. This Phase Execution Chat Starter
4. Phase Spec (`P6__phase-spec.md`)
5. Decisions made during this session
6. Chat messages (lowest authority)

**Critical rules:**
- Stage 1: produce **Milestone specs and Milestone Execution Chat Starters**, create
  `phase/P6` from master (already branched at phase open — confirm and use it), commit all
  planning artifacts, and open a long-lived `phase/P6 → master` PR for HQ review. The PR is
  **not merged** until Stage 2 completes.
- Stage 2: receive Milestone Completion Notices; under the **SN-13 default-accept model**,
  accept clean deliveries by silence (no Review Decision artifact for the happy path — issue
  a Review Decision only on the exception path). All milestone merges land on `phase/P6`;
  merge `phase/P6 → master` on HQ Accept; send Phase Delivery Notice.
- **Artifact scope (adjacency, GH-8):** You produce artifacts only for your direct parent or
  direct children — **Milestone specs and Milestone Execution Chat Starters**. You MUST NOT
  produce Epic specs or Epic Execution Chat Starters (a grandchild artifact that bypasses the
  Milestone Chat's review gate), nor any grandparent artifact. See the "Artifact Scope
  Adjacency" section of `governance/systems/chat-hierarchy.md`.
- **Mid-flight amendments (GH-9):** To change scope after Milestone sessions are running, do
  NOT reach into them — amend the governing spec, note the change, and notify HQ Chat,
  escalating up if blocking. The spec file is the downward channel (one write, many readers).
- Report to HQ Chat; communicate downward to Milestone Chats only.
- Do not reach across to sibling phases or lateral epics.
- Decisions belong to HQ Chat; produce proposals only.

---

## Phase P6 Context

**Phase number:** P6
**Phase name:** Visual Comprehension Layer and Process Refinements
**Phase spec path:** `docs/phases/P6__Visual_Comprehension_Layer_and_Process_Refinements/P6__phase-spec.md`

**Governance document versions in use:**
- PROJECT-SYSTEM-GUIDELINES.md: v2.1.0
- AI-OPERATING-GUIDELINES.md: v2.2.0

**Project state at P6 open:**
- P1–P5 complete and on master; **v5.0.0** tagged (`69c1446`)
- Visual-artifacts **framework** shipped in P5 M22 but inert (`enabled: false`)
- **Producer + helper are DONE and verified (SN-16):** three API-format ComfyUI workflows
  (FLUX-schnell, SDXL/Juggernaut-XL, LTX-Video 2B) driven through `bin/ai-project-visual`,
  verified end-to-end for PNG and WEBM. Contract preserved at
  `.ai-project/artifacts/reference/comfyui-endpoint/`. **P6 is NOT plumbing.**
- SN-15 + SN-16 are binding; all three ratified decisions apply in full (see below)

**Ratified decisions (binding — NOT for re-examination):**
1. **Storage by link** — generated visual material is referenced, never committed to git.
2. **Link carries metadata** — what / level / proposed-vs-implemented / short description.
3. **Clip = one parent** — every clip belongs to exactly one governance node.

**Milestones within this Phase:**

| # | Milestone | Indicative Epics | Priority |
|---|---|---|---|
| M23 | By-Link Storage Model & Binding Convention | E23.1, E23.2 | Highest — execute first (foundation) |
| M24 | Comprehension Behavior & Clips | E24.1, E24.2 | Second — depends on M23 |
| M25 | Process Refinements | E25.1, E25.2, E25.3 | Independent — lowest priority |

> Epic identifiers above are **indicative decomposition** from the phase spec. Final epic
> planning is the Milestone Chat's authority; you produce Milestone specs and Milestone
> Execution Chat Starters, and may adjust epic boundaries within a milestone's scope.

---

## Session Objective

Plan **Milestone M23 — By-Link Storage Model & Binding Convention** first.

Do not plan M24 until HQ has accepted M23's deliverables.

---

## M23 — By-Link Storage Model & Binding Convention

**Goal:** Reverse the v5.0.0 commit-the-binary storage model to **by-link**, and define the
**link + metadata binding convention** that becomes load-bearing once the link is the only
thing in git.

**Branch:** `milestone/M23` from `phase/P6` (which branches from master)

**Indicative Epics (2):**

### E23.1 — By-link storage reconciliation (P6-VC-1)

**Source:** SN-16 (ratified 2026-06-29) — the single biggest governance change in P6.

**Binding context:** Generated visual material is **not** stored in the version-controlled
project; it is **referenced by link**. No binaries in git. The adopter owns the storage
backend. This **reverses** shipped v5.0.0 guidance that instructs committing the binary into
`.ai-project/visuals/<level>/<id>.<ext>` so it "travels with the decision record."

**Deliverables (the reversal must touch all four named surfaces — do not let it leak in as
an incidental edit):**
1. `governance/guides/visual-artifacts.md` — rewrite §4 (Output formats: the
   `.ai-project/visuals/...` path and the "commit the generated file together with the
   artifact" instruction) and the §1 source-repo note to the by-link model
2. `governance/AI-OPERATING-GUIDELINES.md` §16.5 ("What to commit, and where") — rewrite the
   "Generated artifacts are written under … and committed" bullet to by-link
3. `bin/ai-project-visual` output guidance — clarify `--output` writes a **local working
   file** to be hosted and linked, not committed (resolve Open Design Question B below)
4. The integration-test expectations — update any assertion that expects a committed binary
   under `.ai-project/visuals/` to the by-link model
5. Record the change as a **reversal of v5.0.0 shipped guidance** in the AOG and guide changelogs

**Note:** Structural diagrams (Mermaid/PlantUML text) are unaffected — text belongs in git;
generated binaries do not. Do not change structural-diagram guidance.

**Acceptance criteria:**
- All four surfaces describe by-link; no instruction to commit generated binaries remains
- The reversal is recorded in the AOG and guide changelogs

### E23.2 — Link + metadata binding convention (P6-VC-2)

**Source:** SN-16 (ratified 2026-06-29) — load-bearing under by-link.

**Deliverables:**
- Define the binding schema: a visual's **link** plus context **metadata** recording, at
  minimum, **what** the visual is, **which level** it binds to, **proposed-vs-implemented**,
  and a **short text description** (so the record survives link rot)
- Define the per-level **placement convention** — which governance artifact a binding
  attaches to, and how the link gets there, at each level
- Update `governance/guides/visual-artifacts.md` and the relevant templates so each level
  knows how to record a binding

**Acceptance criteria:**
- The binding schema is documented with all four metadata fields
- A placement convention is defined per level (Creation / HQ / Phase / Milestone / Epic)

**Resolve in M23 — Open Design Question B (non-blocking):** Does `bin/ai-project-visual` gain
a link-emitting/upload step, or is hosting + linking the agent's responsibility outside the
helper? *Recommended default:* hosting + linking is the agent's responsibility — keep the
helper a minimal one-shot `prompt → local file` tool (its current verified design).

---

## M24 Preview (plan after M23 accepted)

**M24 — Comprehension Behavior & Clips** (depends on M23's binding convention)

- **E24.1 — Proposed-vs-implemented comprehension behavior (P6-VC-3):** AOG §16 guidance
  establishing the two-track expectation (proposed before build, implemented after) as the
  routine default at every level — "nothing is too much"; Structural-first generous coverage;
  per-level examples of proposed vs. implemented, bound via the M23 convention.
- **E24.2 — Clips as documentation + publishable media (P6-VC-4):** single-parent clip
  binding (one epic/milestone/phase), production from the proposed→implemented arc on the
  verified LTX-Video path (`ltxv-video.json` → `.webm`), and the publish path to
  YouTube/TikTok/IG/FB as the **same asset reused**.
  - **Resolve in M24 — Open Design Question A (non-blocking):** vendor the workflow JSONs
    in-repo vs. reference them on the CFO's host. *Recommended default:* reference, not
    vendor — workflows + models are the generative request contract and stay CFO-side
    (`.ai-project/artifacts/reference/comfyui-endpoint/` is the documented reference).

---

## M25 Preview (plan after M24 accepted; independent — lowest priority)

**M25 — Process Refinements** (the three P5 carry-forwards)

- **E25.1 — Phase-closure canonical sequence (P6-GH-12, High):** make README update, version
  bump, and tag **mandatory automatic steps** in the phase-closure process (same pattern as
  the Epic happy path); today they require an out-of-band Steering Note.
- **E25.2 — Codify SN-13 default-accept (P6-GH-10, Medium):** write the default-accept model
  (parent auto-accepts clean deliveries; Review Decision is the exception path only) into
  `governance/AI-OPERATING-GUIDELINES.md`, `governance/PROJECT-SYSTEM-GUIDELINES.md`, and the
  Execution Chat Starter templates.
- **E25.3 — Align `ai-project-init` agent path (P6-GH-11, Low):** `bin/ai-project-init` writes
  `.ai-project/agents/`, not `.github/agents/`.

---

## Output Requirements

For M23, produce in order:

1. **Milestone spec** —
   `docs/phases/P6__Visual_Comprehension_Layer_and_Process_Refinements/P6-M23__milestone-spec.md`
   covering:
   - Milestone goals and scope
   - Epic list with detailed deliverables and acceptance criteria
   - Prerequisites and dependencies
   - Definition of Done
   - Acceptance criteria

2. **Milestone Execution Chat Starter** —
   `docs/phases/P6__Visual_Comprehension_Layer_and_Process_Refinements/P6-M23__milestone-execution-chat-starter.md`,
   using `governance/templates/milestone-execution-chat-starter.md`

Wrap the Milestone Execution Chat Starter in a four-backtick fence (per AOG §3.1.1):

    ````markdown name=P6-M23__milestone-execution-chat-starter.md
    [content here]
    ````

Deliver the Milestone spec first, then the Milestone Execution Chat Starter. After both,
request HQ review. Under SN-13, HQ accepts a clean delivery by silence; do not wait for a
Review Decision artifact on the happy path.

> **Do NOT produce Epic specs or Epic Execution Chat Starters.** Epic planning belongs to the
> Milestone Chat (adjacency rule, GH-8). Your deliverables are the Milestone spec and the
> Milestone Execution Chat Starter only.

---

## Milestone Delivery Authorization Format

When HQ accepts M23's deliverables:

```
MILESTONE DELIVERY AUTHORIZATION

Issuer: Phase Chat (P6 — Visual Comprehension Layer and Process Refinements)
Date: <YYYY-MM-DD>
Milestone Reference: P6-M23 — By-Link Storage Model & Binding Convention
Authorized Action: Proceed with Milestone execution
Merge Instruction: Merge epic branches to milestone/M23 upon Epic acceptance
```

Do NOT issue without explicit HQ Chat acceptance.

---

## Completion Requirements

This Phase Chat session is complete when HQ Chat has accepted all milestone deliverables
through M25 and declared Phase P6 planning complete. In this instantiation, begin with M23
only. Additional milestones will be requested by HQ after each acceptance.

After M23 acceptance: "M23 deliverables accepted. Awaiting HQ direction on M24."

---

## Question Policy

- Ask only blocking questions.
- Do not propose scope changes, add epics, or modify milestone boundaries.
- Do not ask for information already present in this Starter or the phase spec.
- The three ratified decisions (storage-by-link, link-metadata, clip-single-parent) apply in
  full — do not re-examine them.
- The two Open Design Questions (A: vendor vs. reference workflows; B: helper link-emitting
  step) are **non-blocking** and carry recommended defaults — resolve them within the owning
  milestone, do not escalate them as blockers.
- Escalate to HQ Chat for any gap not covered here.

---

Copy the entire chat starter above and paste into your Phase Chat to begin planning.
