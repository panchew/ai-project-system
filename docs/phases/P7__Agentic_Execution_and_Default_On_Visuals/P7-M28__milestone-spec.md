---
milestone: M28
name: Governance Reconciliations
phase: P7
status: planned
start_date: 2026-07-13
epics:
  - E28.1
  - E28.2
  - E28.3
  - E28.4
is_final: true
---

# Milestone M28 — Governance Reconciliations

## Purpose

Fix four independent doc/CLI contradictions surfaced by real adoption and by SN-19's own
missed-reconciliation finding. Unlike M26/M27, M28 is **pure process hygiene** — no new
capability, no design task, four small, mostly-independent reconciliation epics.

**M26 (First Real Agentic Run) and M27 (Visuals Default-On) are both fully closed and
consolidated to `phase/P7`.** M28 is the **third and final planned P7 milestone**
(`is_final: true`): on its consolidation, the Phase Chat proceeds to **phase delivery**
(`phase/P7 → master`, the long-lived PR #112) via the PSG §5C canonical closure sequence
(README update + version bump + tag + phase-closure declaration), established at P6 and
already exercised once (P6's own delivery).

---

## Binding Context (settled scope — NOT for re-debate)

Four carry-forwards, each already scoped by name in the P7 phase spec (v1.1.0):

1. **P7-GH-16 — Level-0 handoff contradiction** (+ SN-2 sub-item: promote
   `hq-chat-opener.md` into `templates/`).
2. **P6-GH-14 — Delivery-Notice ordering** (P4.1 vs. PSG §12).
3. **P6-GH-15 — init installs the superseded agent file** (`hq.agent.md` vs.
   `governance.agent.md`).
4. **P7-GH-17 — retire the Delivery Authorization ceremonial block** (SN-19; added to M28 by
   HQ's GH-9 mid-flight amendment, commit `c1646a1`, phase spec v1.1.0).

Their *existence and intent* are settled; M28 delivers them. **Independent of M26/M27's
surfaces** — no epic here touches the orchestrator, the runner adapter, or the visual-artifacts
framework.

---

## Problem Statement

Four real contradictions, each verified directly against the current repository state (not
assumed from the phase spec's own description):

- **Level-0 handoff is defined two incompatible ways, and one of the four named docs is
  internally self-contradictory.** `governance/templates/seed.md` (Rule 3: "Decisions formed
  here are proposals until the human carries them into the **HQ Chat** via an artifact"; Rule
  4: produces a **Project Brief + HQ Chat Opener** pair) converges on Creation Chat → HQ Chat.
  `governance/templates/genesis.md` and `governance/systems/chat-hierarchy.md` (§"Level 0":
  "exists to turn a project brief into the single artifact that lets a **Phase Chat** open") **do not
  open an HQ Chat at all** — genesis.md's own embedded "HQ Context Packet" section feeds a
  Phase Chat directly. **`governance/systems/start-a-project.md` embeds both flows in
  sequence and directly contradicts itself:** Step 3 says "with `genesis.md` committed, open a
  Phase Chat" (bypassing HQ) as its own "Next step," then Step 5 says "Spawn the HQ Chat" and
  Step 6 says "Using the HQ Chat: Define the first Phase" — a Phase Chat was already told to
  open two steps earlier. **A further, undocumented wrinkle: two files share the name
  `start-a-project.md`** — `governance/systems/start-a-project.md` (P4-era, `last_updated:
  2026-06-13`, 179 lines) and `docs/systems/start-a-project.md` (P1-era, `last_updated:
  2026-01-17`, 124 lines) — with materially different content. P7-GH-16 names a single
  `start-a-project.md`; E28.1 must determine whether the second file is a stale duplicate to
  reconcile or remove, not silently ignore it.
- **No HQ Chat Opener template exists in `governance/templates/`** — `governance/systems/
  hq-chat-opener.md` (39 lines, `last_updated: 2026-01-17`) is the only copy, sitting in
  `systems/` rather than the `templates/` tier every other fillable chat-starter artifact
  lives in.
- **PSG §12 and the P4.1 artifact-communication protocol assign the name "Delivery Notice" to
  two different points in the Epic lifecycle — not just a reordering, a terminology
  collision.** PSG §12 ("Delivery Notice (Mandatory)"): "produced by the Coding Agent
  **immediately upon execution completion**... a prerequisite for review and closure — no
  Epic may proceed to review or closure without one." `governance/systems/
  artifact-communication-protocol.md`'s flow diagram and Creation Rules: **Completion Notice**
  is what's produced at completion (prerequisite to review); **Delivery Notice** is created
  by the child chat only **after the PR is merged** — i.e., post-acceptance. AOG line 716
  independently repeats PSG §12's pre-review framing ("a prerequisite for human review and
  Epic Delivery Authorization decision"). **The framework's actual operating practice already
  follows the P4.1 two-artifact model** — every Epic/Milestone/Bugfix delivery in this
  project's own history (including M26, M27, and B4.1, executed this same session) produces a
  Completion Notice pre-review and a separate Delivery Notice post-merge. The reconciliation
  question is which document's terminology yields, not which ordering is correct in practice.
- **`bin/ai-project-init` installs a file its own content declares superseded.**
  `bin/ai-project-init:328-329` sources `governance/agents/hq.agent.md` and installs it as
  `.ai-project/agents/hq.agent.md` (the *path* was already fixed to the canonical
  `.ai-project/agents/` location by E25.3 — this is a **filename**, not a path, defect).
  `governance/agents/hq.agent.md` itself opens: "**This agent has been superseded by
  `governance/agents/governance.agent.md`**... The single `governance.agent.md` replaces all
  separate agent files... with one unified agent." The init script ships the literal stub
  that tells the reader to go copy a different file.
- **The Delivery Authorization ceremonial block survives in more surfaces than a single
  section per file.** Confirmed directly: `governance/templates/milestone-execution-chat-
  starter.md:157-191` and `governance/templates/phase-execution-chat-starter.md:156-190` each
  carry one contained "Epic/Milestone Delivery Authorization" section (already the shape M26's
  and M27's own starters had swept, per SN-19). But the `governance/systems/` mirrors are
  **more deeply embedded, not a single block**: `governance/systems/milestone-execution-chat-
  starter.md` and `governance/systems/phase-execution-chat-starter.md` each reference
  "Delivery Authorization" in their Stage-2 responsibilities list (a numbered step), their
  Communication Protocol table, and a full dedicated section — three touch points, not one.
  `governance/systems/hq-execution-chat-starter.md` has the block scattered across a
  **diagram** (line 117: "Epic Delivery Authorization ▼"), an instruction ("issue an Epic
  Delivery Authorization directly," line 241), and a Phase-level mention (line 350) — no
  single contained section to delete. **AOG itself carries the language in three places, not
  two:** §1A step 6 (line 35: "Only after explicit Epic Delivery Authorization may a PR be
  created and merged"), line 716 (Delivery Notice's own definition names "Epic Delivery
  Authorization decision" as what it's a prerequisite for — entangled with E28.2's finding
  above), and line 756 ("HQ Chat MUST issue explicit Epic Delivery Authorization before
  PR/merge").

---

## Goals

By the end of this milestone:

1. **Level-0 handoff is coherent.** The canonical output is decided — or both flows are
   explicitly codified as scale-dependent (Open Design Question B's recommended default) —
   and `seed.md`, `genesis.md`, `start-a-project.md`, and `chat-hierarchy.md` agree with each
   other and with themselves (E28.1).
2. **An HQ Chat Opener template exists in `governance/templates/`** (E28.1, SN-2 sub-item).
3. **Delivery-Notice ordering is reconciled to one terminology**, matching the framework's
   actual practiced model (E28.2).
4. **`bin/ai-project-init` installs the canonical `governance.agent.md`**, not the superseded
   stub, with a test (E28.3).
5. **The Delivery Authorization ceremonial block is retired everywhere it survives** —
   templates, `governance/systems/` mirrors (including the non-block-shaped references in
   `hq-execution-chat-starter.md`), and all three AOG touch points — while the in-chat merge
   authorization is preserved unchanged (E28.4).

---

## Non-Goals

This milestone explicitly does **not**:

- **Touch M26 or M27's surfaces** — the orchestrator, `bin/run-dev-agent`, the runner adapter,
  or the visual-artifacts framework (AOG §16, yml-spec §3.5, `gpu-coexistence.md`).
- **Re-debate any of the four carry-forwards' existence or intent** — only their reconciled
  wording is open.
- **Resolve Open Design Question B by fiat here** — the recommended default (codify both
  flows as scale-dependent) is non-blocking; E28.1 resolves it, this spec does not pre-decide
  the final wording.
- **Delete `docs/systems/start-a-project.md` or otherwise resolve the duplicate-filename
  finding by assumption** — E28.1 investigates and decides; this spec only surfaces the
  finding.
- **Change AOG's numbering scheme or PSG's section structure beyond what each epic's specific
  reconciliation requires.**

---

## In Scope

- **E28.1** — `seed.md`, `genesis.md`, `governance/systems/start-a-project.md` (and the
  `docs/systems/start-a-project.md` duplicate-filename question), `chat-hierarchy.md`'s Level-0
  section, and promoting `hq-chat-opener.md` into `governance/templates/`.
- **E28.2** — PSG §12, `governance/systems/artifact-communication-protocol.md`, and AOG's
  entangled line-716 reference — reconciled to one Delivery-Notice ordering/terminology.
- **E28.3** — `bin/ai-project-init` (lines 328-329, 408), a new test, and any doc that names
  the installed filename.
- **E28.4** — `governance/templates/{milestone,phase}-execution-chat-starter.md`,
  `governance/systems/{milestone,phase,hq}-execution-chat-starter.md`, and AOG §1A step 6 +
  lines 716 (shared with E28.2) + 756.

## Out of Scope

- Any M26/M27 surface; re-debating carry-forward intent; resolving Question B's wording by
  spec fiat; AOG/PSG structural changes beyond each epic's named reconciliation.

---

## Planned Epics

### Confirmed Epics

- **E28.1 — Level-0 handoff reconciliation + HQ starter template** (P7-GH-16 + SN-2, Medium)
- **E28.2 — Delivery-Notice ordering reconciliation** (P6-GH-14, Medium)
- **E28.3 — init canonical agent file** (P6-GH-15, Low)
- **E28.4 — Retire the Delivery Authorization ceremonial block** (P7-GH-17 / SN-19, Medium)

> **Artifact scope (GH-8 adjacency):** the Phase Chat produces only this Milestone spec and
> the Milestone Execution Chat Starter. The **Milestone Chat** owns final epic planning and
> authors every Epic spec and Epic Execution Chat Starter. No Phase-level Epic drafts exist.

### Deferred Epics

- None.

---

## Epic Detail

### E28.1 — Level-0 handoff reconciliation + HQ starter template (P7-GH-16 + SN-2, Medium)

**Source:** P7 phase spec P7.3 (P7-GH-16); Open Design Question B.

**Grounding:** see "Problem Statement" above — the seed.md-vs-genesis.md contradiction, the
internal self-contradiction inside `governance/systems/start-a-project.md` (Step 3 sends the
reader to a Phase Chat directly; Steps 5-6 then send the same reader to an HQ Chat to define
that same first Phase), and the duplicate-filename finding
(`docs/systems/start-a-project.md`, P1-era, vs. `governance/systems/start-a-project.md`,
P4-era).

**Open Design Question A resolution recommended:** *(Question B)* codify **both flows as
scale-dependent** — lightweight `genesis.md` → Phase Chat directly for small bootstraps; full
`seed.md` → Project Brief + HQ Opener → HQ Chat for ongoing projects — stated explicitly in
all four docs, replacing `start-a-project.md`'s current unlabeled hybrid.

**Deliverables:**
1. Decide (or confirm Question B's default) and state the canonical Level-0 model(s) clearly
   in `seed.md`, `genesis.md`, `governance/systems/start-a-project.md`, and
   `chat-hierarchy.md`'s Level-0 section — eliminating the self-contradiction found above.
2. Resolve the `docs/systems/start-a-project.md` duplicate: reconcile it to agree with the
   canonical version, or determine it is stale and remove it — document the decision either
   way.
3. Promote `governance/systems/hq-chat-opener.md` into `governance/templates/` (move or copy —
   Epic's call; if moved, fix any reference to the old path).

**Definition of Done:**
- [ ] `seed.md`, `genesis.md`, `start-a-project.md`, and `chat-hierarchy.md` no longer
      contradict each other or (in `start-a-project.md`'s case) themselves
- [ ] The `docs/systems/start-a-project.md` duplicate is resolved (reconciled or removed), not
      left silently divergent
- [ ] An HQ Chat Opener template exists in `governance/templates/`
- [ ] Full test suite passes

**Acceptance Criteria:**
- [ ] The four named docs agree on the Level-0 handoff (single canonical output, or both flows
      explicitly scale-dependent)
- [ ] An HQ starter template is in `governance/templates/`

---

### E28.2 — Delivery-Notice ordering reconciliation (P6-GH-14, Medium)

**Source:** P7 phase spec P7.3 (P6-GH-14).

**Grounding:** PSG §12 (lines 609-625) names "Delivery Notice" the pre-review,
completion-time artifact; `artifact-communication-protocol.md`'s flow diagram and Creation
Rules (lines 315-330, 520-563) name that same pre-review artifact "Completion Notice" and
reserve "Delivery Notice" for the **post-merge** artifact; AOG line 716 independently repeats
PSG §12's framing. **The framework's own practiced model already matches
`artifact-communication-protocol.md`'s two-artifact convention** — confirmed directly by this
Phase Chat's own M26/M27/B4.1 execution this session (Completion Notice issued pre-review;
separate Delivery Notice issued post-merge, every time).

**Deliverables:**
1. Reconcile PSG §12 to name the pre-review artifact "Completion Notice" (matching actual
   practice and `artifact-communication-protocol.md`), reserving "Delivery Notice" for the
   post-merge artifact — or, if the Milestone/Epic Chat finds a reason to reconcile the other
   direction, state that reasoning explicitly rather than leaving the terminology collision
   unresolved.
2. Fix AOG line 716's entangled reference to match whichever direction is chosen (**shared
   surface with E28.4** — sequence or coordinate to avoid two epics editing the same line
   inconsistently).
3. PSG (and AOG, if touched) version bump + changelog row.

**Definition of Done:**
- [ ] PSG §12 and `artifact-communication-protocol.md` use one consistent Delivery-Notice
      ordering/terminology
- [ ] AOG line 716's entangled reference is reconciled to match
- [ ] The reconciliation matches the framework's actual practiced model, or states explicitly
      why it diverges
- [ ] Full test suite passes

**Acceptance Criteria:**
- [ ] PSG §12 and P4.1 no longer assign "Delivery Notice" to two different lifecycle points

---

### E28.3 — init canonical agent file (P6-GH-15, Low)

**Source:** P7 phase spec P7.3 (P6-GH-15).

**Grounding:** `bin/ai-project-init:328-329` — `src_file="$project_dir/governance/agents/
hq.agent.md"`, `dest_file="$agents_dir/hq.agent.md"`; line 408 stages
`.ai-project/agents/hq.agent.md`. `governance/agents/hq.agent.md`'s own content: "**This agent
has been superseded by `governance/agents/governance.agent.md`**." The path itself
(`.ai-project/agents/`) was already fixed by E25.3 (P6-M25) — this is the **filename** only.

**Deliverables:**
1. Change `bin/ai-project-init` to source and install `governance/agents/governance.agent.md`
   as `.ai-project/agents/governance.agent.md` (lines 328-329, 408).
2. Add a test asserting the initializer writes `.ai-project/agents/governance.agent.md` (the
   existing `tests/test_init_agent_path.py`, per E25.3, asserts the *path* with `hq.agent.md`
   as the filename — extend or add a case for the filename).
3. Reconcile any doc naming the installed filename as `hq.agent.md`.

**Definition of Done:**
- [ ] `bin/ai-project-init` writes `.ai-project/agents/governance.agent.md`
- [ ] A test asserts the canonical filename
- [ ] Docs naming the installed file agree
- [ ] Full test suite passes

**Acceptance Criteria:**
- [ ] `bin/ai-project-init` installs `governance.agent.md`

---

### E28.4 — Retire the Delivery Authorization ceremonial block (P7-GH-17 / SN-19, Medium)

**Source:** SN-19 (`.ai-project/artifacts/steering-notes/2026-07-12__creation-chat__steering-
note__delivery-authorization-retirement.md`); HQ's acceptance (commit `c1646a1`); phase spec
v1.1.0.

**Grounding:** confirmed directly — the templates carry one contained section each
(`governance/templates/milestone-execution-chat-starter.md:157-191`,
`governance/templates/phase-execution-chat-starter.md:156-190`, already the shape M26's/M27's
own starters were swept to under GH-9 pre-open amendments). The `governance/systems/` mirrors
are **more deeply embedded**: `milestone-execution-chat-starter.md` and
`phase-execution-chat-starter.md` each reference Delivery Authorization in a Stage-2
responsibilities step, a Communication Protocol table row, *and* a dedicated section (three
touch points each); `hq-execution-chat-starter.md` has no single block at all — a diagram
label (line 117), an instruction (line 241), and a Phase-level mention (line 350). AOG carries
it in three places: §1A step 6 (line 35), line 716 (**shared with E28.2** — the same line also
carries the Delivery-Notice terminology collision), and line 756.

**Deliverables:**
1. Retire the Delivery Authorization sections and their Completion-Requirements checklist
   lines from both templates (already the pattern the M26/M27 starters demonstrate) — fold the
   load-bearing **merge instruction** into each template's execution instructions.
2. Retire or rewrite every touch point in the three `governance/systems/` mirrors — not just a
   deleted section; the responsibilities-list steps, Communication Protocol table rows, and
   (for `hq-execution-chat-starter.md`) the diagram/instruction/mention all need addressing
   individually, since they are not one contained block.
3. Reword AOG §1A step 6 and line 756 to in-chat authorization language; **coordinate line 716
   with E28.2** (sequence the two epics or use a worktree, since both touch the same line for
   different reasons — Delivery-Notice terminology vs. Delivery-Authorization retirement).
4. Preserve the in-chat merge authorization unchanged everywhere the block is retired.
5. AOG version bump + changelog row.

**Definition of Done:**
- [ ] No Delivery Authorization ceremonial block/section remains in either template
- [ ] All touch points in the three `governance/systems/` mirrors are addressed (not just a
      block deletion where no single block exists)
- [ ] AOG §1A step 6 and line 756 read in-chat authorization language; line 716 reconciled in
      coordination with E28.2
- [ ] The in-chat merge authorization is preserved, unchanged, everywhere
- [ ] Full test suite passes

**Acceptance Criteria:**
- [ ] No codified text asserts the ceremonial Delivery Authorization artifact as required on
      the happy path
- [ ] The in-chat merge authorization requirement is intact everywhere

---

## Branch Strategy

```
master
└── phase/P7                    (M26 + M27 consolidated — HEAD e982085)
    └── milestone/M28            ← this milestone (Milestone Chat branches from phase/P7)
        ├── epic/P7-M28-E28.1    ← Level-0 handoff + HQ starter template
        ├── epic/P7-M28-E28.2    ← Delivery-Notice ordering reconciliation
        ├── epic/P7-M28-E28.3    ← init canonical agent file
        └── epic/P7-M28-E28.4    ← retire Delivery Authorization ceremonial block
```

Epic PRs target `milestone/M28`. Consolidation PR: `milestone/M28 → phase/P7`.
**M28 is the final P7 milestone** (`is_final: true`). On its consolidation, the Phase Chat
proceeds to **phase delivery** (`phase/P7 → master`, PR #112) via the PSG §5C canonical
closure sequence + the P7 Phase Delivery Notice.

---

## Prerequisites

- This Milestone spec and its Milestone Execution Chat Starter are git-tracked on `phase/P7`
  (verify with `git ls-files --error-unmatch <path>` — the GH-1 convention).
- M28 targets present and git-tracked on `phase/P7`:
  - `governance/templates/seed.md`, `genesis.md`, `hq-chat-opener.md` (in `systems/`, to be
    promoted)
  - `governance/systems/start-a-project.md`, `docs/systems/start-a-project.md`,
    `chat-hierarchy.md`
  - `governance/PROJECT-SYSTEM-GUIDELINES.md` (§12), `governance/systems/
    artifact-communication-protocol.md`
  - `bin/ai-project-init`, `tests/test_init_agent_path.py`, `governance/agents/{hq,governance}.agent.md`
  - `governance/templates/{milestone,phase}-execution-chat-starter.md`,
    `governance/systems/{milestone,phase,hq}-execution-chat-starter.md`,
    `governance/AI-OPERATING-GUIDELINES.md`
- **No external dependency.** M28 is process hygiene; it needs no endpoint, no host
  prerequisite, and no cross-repo coordination.

---

## Dependencies and Sequencing

- **E28.1 and E28.3 are fully independent** of every other epic (disjoint files) and may run
  in parallel.
- **E28.2 and E28.4 both touch AOG line 716** — for different reasons (Delivery-Notice
  terminology vs. Delivery-Authorization retirement). Serialize them (or use a worktree, GH-2)
  and have whichever runs second explicitly reconcile with the first's edit rather than
  clobbering it.
- **Priority order:** no hard priority beyond the E28.2/E28.4 file-contention pairing; E28.1
  and E28.3 may proceed alongside either.
- No dependency on M26 or M27 — both are closed.

---

## Definition of Done (Milestone)

- [ ] E28.1, E28.2, E28.3, and E28.4 each meet their Definition of Done above
- [ ] All four epic branches merged to `milestone/M28`
- [ ] Level-0 handoff is coherent across all four named docs (+ the duplicate-filename
      finding resolved)
- [ ] An HQ Chat Opener template exists in `governance/templates/`
- [ ] Delivery-Notice terminology is consistent between PSG §12 and P4.1
- [ ] `bin/ai-project-init` installs `governance.agent.md`, with a test
- [ ] The Delivery Authorization ceremonial block is retired everywhere it survived (templates
      + all three `governance/systems/` mirrors + AOG's three touch points), with in-chat
      merge authorization preserved
- [ ] Full test suite passes on `milestone/M28`
- [ ] Milestone Closure Declaration produced (`is_final_milestone: true`)

---

## Acceptance Criteria (Milestone)

1. `seed.md`, `genesis.md`, `start-a-project.md`, and `chat-hierarchy.md` no longer
   contradict each other on the Level-0 handoff; an HQ starter template is in `templates/`
   (E28.1).
2. PSG §12 and P4.1 no longer assign "Delivery Notice" to two different lifecycle points
   (E28.2).
3. `bin/ai-project-init` installs `governance.agent.md` (E28.3).
4. No codified text asserts the ceremonial Delivery Authorization artifact as required on the
   happy path, across templates, systems mirrors, and AOG; in-chat merge authorization is
   preserved (E28.4).

---

## Timeline

**Target Start:** 2026-07-13
**Target Completion:** 2026-07-19 (4-6 days per Phase spec estimate; 4 small epics, 2
serialized)
**Actual Start:** Not started
**Actual Completion:** Not started

---

## Notes

- **M28 is the final P7 milestone** (`is_final: true`). On consolidation, the Phase Chat
  proceeds to **phase delivery** (`phase/P7 → master`, the already-open long-lived PR #112) +
  Phase Delivery Notice, following the PSG §5C canonical closure sequence (README update +
  version bump + tag + phase-closure declaration) that P6 itself introduced and exercised.
- **E28.1's grounding surfaced two findings beyond the phase spec's own description**: the
  internal self-contradiction inside `governance/systems/start-a-project.md` itself (not just
  a cross-document mismatch), and a duplicate `start-a-project.md` filename
  (`docs/systems/` vs. `governance/systems/`) that P7-GH-16 did not name. Both are now on
  record for the Milestone/Epic Chat to resolve — not silently absorbed or ignored.
- **E28.2's finding is sharper than "two orderings disagree"**: it is a **terminology
  collision** — PSG §12 and P4.1 both use the name "Delivery Notice" for different points in
  the lifecycle. The framework's own practiced model (confirmed directly this session across
  M26, M27, and B4.1) already matches P4.1's two-artifact convention; the reconciliation's
  most defensible direction is to bring PSG §12 in line with what is actually practiced,
  though the Epic may find and state a different reason if warranted.
- **E28.2 and E28.4 share one file line (AOG :716)** — this is a real file-contention point
  the Milestone Chat must plan around, not an incidental overlap.
- **E28.4's `governance/systems/` mirrors are not shaped like a single deletable block** —
  `hq-execution-chat-starter.md` especially has the language scattered across a diagram and
  prose references. The Epic needs to address each touch point on its own terms, not assume a
  uniform "delete this section" edit works everywhere.
- Exact wording for each reconciliation, whether `hq-chat-opener.md` is moved or copied into
  `templates/`, and how each epic phrases its specific fix are **Epic-level design calls
  within M28's scope** — the milestone fixes the contract (coherent Level-0 docs; one
  Delivery-Notice terminology; canonical agent filename; ceremonial-block retirement
  everywhere it survives), not the wording.
- Default-accept (PSG §11.6 / AOG §12) governs M28's own delivery: clean Epic/Milestone
  deliveries are auto-accepted by silence; Review Decisions are the exception path only. Per
  SN-19 (which E28.4 itself will finish propagating), Epic/Milestone acceptance and the merge
  instruction are in-chat acts — no Delivery Authorization artifact, even for this milestone's
  own deliveries.
