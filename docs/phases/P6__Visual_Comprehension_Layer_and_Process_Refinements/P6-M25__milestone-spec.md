---
milestone: M25
name: Process Refinements
phase: P6
status: complete
start_date: 2026-07-02
epics:
  - E25.1
  - E25.2
  - E25.3
  - E25.4
  - E25.5
  - E25.6
is_final: true
---

# Milestone M25 — Process Refinements

## Purpose

Close the **three P5 carry-forwards** that are pure process hygiene, independent of the visual
work in M23–M24. M25 is the **final P6 milestone** (`is_final: true`): when it consolidates into
`phase/P6`, Phase P6 is ready for delivery to `master`.

Three small, mostly-independent epics:

1. **Phase-closure canonical sequence (E25.1, High).** Make README update + version bump + git
   tag **mandatory automatic steps** of phase closure — the same pattern the Epic happy path
   (PSG §1A) and Milestone Closure (PSG §5B) already use. Today they require an out-of-band
   Steering Note (this is how P5 closed).
2. **Codify SN-13 default-accept (E25.2, Medium).** Write the default-accept delivery model —
   *a parent chat auto-accepts a clean child delivery by silence; a Review Decision is the
   exception path only* — into AOG, PSG, and the Execution Chat Starter templates, **and
   reconcile** the existing always-review language that contradicts it.
3. **Align `ai-project-init` agent path (E25.3, Low).** `bin/ai-project-init` must write the
   canonical, tool-neutral `.ai-project/agents/` path, not `.github/agents/`.

> **Dogfood note (E25.1):** the phase-closure sequence E25.1 defines is the very sequence P6's
> own delivery will follow once M25 closes. E25.1 lands the canonical steps; the P6 phase
> delivery then exercises them (README/version/tag), rather than closing via a one-off Steering
> Note as P5 did.

---

## Binding Context (P5 carry-forwards — settled scope, not for re-debate)

These three items were identified and deferred at P5 closure and are named in the P6 phase spec
(P6-GH-12 / P6-GH-10 / P6-GH-11). Their *existence and intent* are settled; M25 delivers them.
The visual-layer ratified decisions (SN-15/SN-16) do not bear on M25 — this milestone is process
hygiene.

---

## Problem Statement

Three known gaps survived P5:

- **Phase closure is not canonical.** The framework codifies a mandatory Epic-closure happy path
  (PSG §1A) and a Milestone Closure section (PSG §5B), but there is **no phase-closure canonical
  sequence**. README update, version bump, and tag — the steps that make a phase delivery legible
  from `master` — happen today only because a human issues a Steering Note. They should be
  mandatory automatic steps like every other closure gate.
- **The delivery model in force is not the one written down.** SN-13 default-accept (parent
  auto-accepts clean child deliveries; Review Decision is the exception path only) has governed
  every delivery since P5 — including all of M23 and M24 — but the codified text still describes
  an **always-review** model: PSG §11.5 ("Acceptance Recorded in Review Decision"), PSG §1A
  (mandatory human review + explicit authorization per epic), PSG §13A/§13B and AOG Stage-2
  descriptions ("issues Review Decisions"), and the Execution Chat Starter templates ("Stage 2:
  … issue Review Decisions"). The written model and the operating model disagree; M25 reconciles
  them.
- **The initializer writes a tool-specific agent path.** P5 established `.ai-project/agents/` as
  the canonical, tool-neutral agent location (documented in QUICK-START and the integration
  guides), but `bin/ai-project-init` still writes `.github/agents/`. Docs and script disagree.

---

## Goals

By the end of this milestone:

1. **Phase closure is canonical.** PSG lists README update, version bump, and tag as **mandatory
   automatic** phase-closure steps, mirroring the §1A / §5B pattern; no Steering Note is required
   to close a phase (E25.1).
2. **Default-accept is codified and consistent.** AOG, PSG, and the Execution Chat Starter
   templates describe the SN-13 default-accept model, and no remaining text asserts the
   contradictory always-review / Review-Decision-recorded-acceptance happy path (E25.2).
3. **The initializer writes the agnostic path.** `bin/ai-project-init` writes
   `.ai-project/agents/`; a test asserts it; docs and script agree (E25.3).

---

## Non-Goals

This milestone explicitly does **not**:

- **Change the visual layer.** M23/M24 surfaces (by-link, §7 binding, §16.6/§16.7, guide §5/§8)
  are done and out of scope here.
- **Remove Layer-8 human review.** E25.2 codifies *default-accept at the parent-chat→child gate*;
  it must **not** delete the human-review requirement the framework mandates. It scopes which
  gate default-accept governs and preserves human review where required (see E25.2 detail).
- **Redesign the closure artifacts.** E25.1 adds the *phase-closure* sequence; it does not
  rework the Epic/Milestone closure gates that already exist.
- **Rewrite the initializer.** E25.3 is a path change plus test/doc reconcile, not a refactor.
- Re-debate the P5 carry-forwards' intent, or re-open any M23/M24 decision.

---

## In Scope

- **E25.1** — a canonical phase-closure sequence in `governance/PROJECT-SYSTEM-GUIDELINES.md`
  (README update + version bump + tag as mandatory automatic steps), optionally a phase-closure
  template, and any AOG phase-delivery text that must agree.
- **E25.2** — a normative default-accept definition in AOG + PSG, reconciliation of the existing
  always-review language, and updates to the phase + milestone Execution Chat Starter templates.
- **E25.3** — `bin/ai-project-init` agent path → `.ai-project/agents/`, a test, and doc reconcile.

## Out of Scope

- Any M23/M24 visual surface; any change to the Epic/Milestone closure gates beyond adding the
  phase-level one; removal of human review; an initializer refactor; new features.

---

## Planned Epics

### Confirmed Epics

- **E25.1 — Phase-closure canonical sequence** (P6-GH-12, High)
- **E25.2 — Codify SN-13 default-accept** (P6-GH-10, Medium)
- **E25.3 — Align `ai-project-init` agent path** (P6-GH-11, Low)
- **E25.4 — Reconcile default-accept across reference/protocol/role/diagram docs** (P6-GH-10) — *added during execution*
- **E25.5 — Reconcile default-accept in the artifact templates tier** (P6-GH-10) — *added during execution*
- **E25.6 — Reconcile the remaining CLI-path adoption docs** (P6-GH-11) — *added during execution*

> **Amendment (Phase Chat, 2026-07-03 — milestone-level bookkeeping, GH-8):** M25 was planned with
> three epics; two carry-forwards (P6-GH-10 default-accept; P6-GH-11 init-path) reached across far
> more of the framework than the named-surface lists captured. E25.4/E25.5/E25.6 were added **by
> explicit Phase Chat decision at each step during execution** (never assumed) to reconcile
> default-accept across the reference/protocol/role/diagram and templates tiers (E25.4/E25.5) and
> the remaining CLI-path adoption docs (E25.6). The Milestone Chat, bound by adjacency, could not
> edit this (its parent's) spec; the Phase Chat records the final six-epic list here. Two new
> carry-forwards surfaced and are recorded at phase level: **P6-GH-14** (P4.1-vs-PSG §12
> Delivery-Notice ordering) and **P6-GH-15** (`ai-project-init` installs the superseded
> `hq.agent.md`). Lesson recorded: *a spec's named-surface list is a floor, not a ceiling.*

> **Artifact scope (GH-8 adjacency):** the Phase Chat produces only this Milestone spec and the
> Milestone Execution Chat Starter. The **Milestone Chat** owns final epic planning and authors
> every Epic spec and Epic Execution Chat Starter. No Phase-level Epic drafts exist.

### Deferred Epics

- None.

---

## Epic Detail

### E25.1 — Phase-closure canonical sequence (P6-GH-12, High)

**Source:** P6 phase spec P6-GH-12; P5 carry-forward.

**Grounding (verified on `phase/P6`):**

- PSG **§1A "Canonical Happy Path for Epic Closure (Mandatory)"** is the pattern to mirror — an
  ordered, mandatory, "no step may be skipped" sequence. PSG **§5B "Milestone Closure"** exists.
  There is **no phase-closure canonical sequence** in PSG.
- **No phase-closure template** exists in `governance/templates/` (only `epic-closure-notice.md`
  and `milestone-closure-declaration.md`). P5 produced a one-off
  `docs/phases/P5__.../P5__phase-closure-declaration.md` by hand — evidence of the missing
  canonical step.
- **Stale-artifact evidence the sequence would catch:** the repo README still shows a stale test
  banner ("226/226", a P4 number; current is 259 passed / 1 skipped) — exactly the drift a
  mandatory README-update step prevents.

**Deliverables:**

1. Add a **canonical phase-closure sequence** to PSG (e.g. a "§5C Phase Closure" mirroring §5B,
   or a phase entry in the §1A closure family) that lists **README update, version bump, and git
   tag as mandatory automatic steps** — no out-of-band Steering Note required.
2. Optionally add a **phase-closure-declaration template** to `governance/templates/` mirroring
   `milestone-closure-declaration.md`, so phase closure has a canonical artifact like the levels
   below it.
3. Reconcile any AOG phase Stage-2 / delivery text so it agrees with the new canonical sequence.
4. PSG version bump + changelog row recording the added phase-closure sequence.

**Definition of Done:**
- [ ] PSG defines a mandatory phase-closure sequence including README update, version bump, and tag
- [ ] No Steering Note is required to close a phase (the steps are mandatory/automatic)
- [ ] (If added) a phase-closure template mirrors the milestone-closure template
- [ ] PSG changelog + version bump record the change
- [ ] Full test suite passes

**Acceptance Criteria:**
- [ ] The phase-closure process lists README update, version bump, and tag as mandatory steps
- [ ] The sequence mirrors the §1A / §5B pattern (ordered, mandatory, no step skipped)

---

### E25.2 — Codify SN-13 default-accept (P6-GH-10, Medium)

**Source:** P6 phase spec P6-GH-10; P5 carry-forward. The model has governed every delivery
since P5 (including all of M23/M24) but is not written down.

**The model to codify:** A **parent chat auto-accepts a clean child delivery by silence** —
no Review Decision artifact on the happy path. A **Review Decision is the exception path only**
(issued when a delivery is *not* clean). This governs the **parent-chat → child** acceptance gate
(Phase accepts a clean Milestone; Milestone accepts a clean Epic).

**Grounding (verified — the always-review language E25.2 must reconcile):**

- PSG **§11.5** — the flow ends "Acceptance Recorded in Review Decision"; key rule 5 says
  "Acceptance decisions are recorded in the Review Decision." (Describes always-review.)
- PSG **§1A** — mandates human review + an explicit HQ delivery authorization *per epic*.
- PSG **§13A / §13B** and AOG **Stage-2 descriptions** (AOG ~lines 486, 505) — "oversees … issues
  Review Decisions, and merges when all … are accepted."
- **Execution Chat Starter templates** — `phase-execution-chat-starter.md` and
  `milestone-execution-chat-starter.md` both say "Stage 2: … **issue Review Decisions**, and
  merge when all … are accepted."
- AOG ~lines 728, 817 — "record them in the Review Decision" / "Acceptance is documented in the
  Review Decision and becomes immutable."

**Load-bearing nuance (the epic must get this right):** default-accept applies to the
**parent-chat acceptance of a clean child delivery** — it does **not** abolish Layer-8 human
review where the framework requires it. Codify the default-accept happy path (silence = accept,
no artifact) and the exception path (Review Decision when not clean) **without** contradicting
the human-review requirement; where the two could read as conflicting (e.g. §1A's mandatory human
review vs. auto-accept), the epic must state precisely which gate each governs. This is a
reconciliation, not a blanket delete — same "name the surfaces, don't let it leak" discipline as
the M23 by-link reversal.

**Deliverables:**

1. A **normative definition** of the default-accept model in **AOG** and **PSG** (a new
   subsection — e.g. PSG §11.6 or an extension of §11.5; and the corresponding AOG
   review/acceptance guidance): happy path = parent accepts a clean child delivery by silence,
   no Review Decision; exception path = Review Decision issued when not clean.
2. **Reconcile** the existing always-review language named above (PSG §11.5/§12/§1A/§13A-B; AOG
   Stage-2 descriptions and lines 728/817) so no text asserts the contradictory happy path, while
   preserving the human-review requirement where it applies.
3. Update the **phase + milestone Execution Chat Starter templates** Stage-2 language to describe
   default-accept (issue a Review Decision only on the exception path).
4. AOG (**v2.5.0 → v2.6.0**) and PSG version bumps + changelog rows recording the codification.

**Definition of Done:**
- [ ] AOG and PSG define the default-accept model (happy path = silence; exception = Review Decision)
- [ ] The existing always-review language is reconciled; no text asserts the contradictory happy path
- [ ] Layer-8 human review remains required where the framework mandates it (not deleted)
- [ ] The phase + milestone Execution Chat Starter templates describe default-accept
- [ ] AOG + PSG changelog/version bumps record the change
- [ ] Full test suite passes

**Acceptance Criteria:**
- [ ] AOG, PSG, and the Execution Chat Starter templates describe the SN-13 default-accept model
- [ ] The Review Decision is documented as the exception path, not the happy-path artifact
- [ ] No remaining codified text contradicts default-accept

---

### E25.3 — Align `ai-project-init` agent path (P6-GH-11, Low)

**Source:** P6 phase spec P6-GH-11; P5 carry-forward.

**Grounding (verified):**

- `bin/ai-project-init` writes `.github/agents/`: `mkdir -p "$project_dir/.github/agents"`
  (line 133), `local agents_dir="$project_dir/.github/agents"` (line 327, which drives `mkdir`
  line 331 and `dest_file` line 329), and `git add .github/agents/hq.agent.md` (line 408).
- **`.ai-project/agents/` is the documented canonical, tool-neutral path** — QUICK-START.md
  (`.ai-project/agents/governance.agent.md`, line 92, 166, 735) and the integration guides.
  QUICK-START.md:92 notes "(The CLI also writes a copy to `.github/agents/` …)" — so the doc and
  script must be reconciled together, not just the script changed.
- **No test references either agent path today** (grep of `tests/` finds neither
  `.github/agents` nor `.ai-project/agents`) — E25.3 must **add** coverage.

**Deliverables:**

1. Change `bin/ai-project-init` to write the canonical **`.ai-project/agents/`** path (the
   `agents_dir` at line 327 and the `git add` path at line 408; the `mkdir` at line 133).
2. **Add a test** asserting the initializer writes `.ai-project/agents/hq.agent.md` (none exists).
3. **Reconcile the docs** that describe the CLI writing `.github/agents/` (QUICK-START.md:92 and
   any sibling) so docs and script agree. *(Whether to also keep a `.github/agents/` tool-specific
   copy is an Epic-level call; the phase spec directs the canonical write to `.ai-project/agents/`,
   "not `.github/agents/`.")*

**Definition of Done:**
- [ ] `bin/ai-project-init` writes `.ai-project/agents/hq.agent.md`
- [ ] A test asserts the `.ai-project/agents/` path
- [ ] QUICK-START (and any doc) describing the init agent path agrees with the script
- [ ] Full test suite passes

**Acceptance Criteria:**
- [ ] `bin/ai-project-init` writes `.ai-project/agents/`
- [ ] Test coverage asserts it; docs and script agree

---

## Branch Strategy

```
master
└── phase/P6                  (M23 + M24 consolidated — HEAD 7177e04)
    └── milestone/M25          ← this milestone (Milestone Chat branches from phase/P6)
        ├── epic/P6-M25-E25.1   ← Phase-closure canonical sequence
        ├── epic/P6-M25-E25.2   ← Codify SN-13 default-accept
        └── epic/P6-M25-E25.3   ← Align ai-project-init agent path
```

Epic PRs target `milestone/M25`. Consolidation PR: `milestone/M25 → phase/P6`.
**M25 is the final P6 milestone** (`is_final: true`). On its consolidation, the Phase Chat
proceeds to **phase delivery** — `phase/P6 → master` (PR #95) — following E25.1's new canonical
phase-closure sequence, plus the P6 Phase Delivery Notice.

---

## Prerequisites

- `phase/P6` carries the consolidated M23 + M24 work — verify the M25 targets are present and
  git-tracked (`git ls-files --error-unmatch <path>`, the GH-1 convention):
  - `governance/PROJECT-SYSTEM-GUIDELINES.md` (v2.1.0; §1A, §5B, §11.5, §12, §13A/§13B)
  - `governance/AI-OPERATING-GUIDELINES.md` (v2.5.0; Stage-2 review/acceptance text)
  - `governance/templates/phase-execution-chat-starter.md`,
    `governance/templates/milestone-execution-chat-starter.md`
  - `bin/ai-project-init`
  - `governance/guides/QUICK-START.md`
- This Milestone spec and its Milestone Execution Chat Starter are git-tracked on `phase/P6`.
- **No external dependency.** M25 is process hygiene; it needs no endpoint and no visual work.

---

## Dependencies and Sequencing

- **No hard cross-epic dependency** — the three epics touch mostly different surfaces.
- **E25.1 and E25.2 both edit PSG** (different sections: E25.1 adds a phase-closure sequence;
  E25.2 reconciles §11.5/§12/§1A/§13). Serialize them (or use a worktree, GH-2) to avoid
  file contention.
- **E25.3 is fully independent** (`bin/ai-project-init` + a test + a doc) and may run in parallel.
- **Priority order:** E25.1 (High) → E25.2 (Medium) → E25.3 (Low). E25.1 first because it is
  higher priority *and* its output is exercised by P6's own phase delivery after M25 closes.

---

## Definition of Done (Milestone)

- [ ] E25.1, E25.2, and E25.3 each meet their Definition of Done above
- [ ] All three epic branches merged to `milestone/M25`
- [ ] PSG defines a mandatory phase-closure sequence (README/version/tag)
- [ ] AOG + PSG + the phase/milestone starter templates describe SN-13 default-accept, with the
      contradictory always-review language reconciled and human review preserved
- [ ] `bin/ai-project-init` writes `.ai-project/agents/`, with a test and doc agreement
- [ ] Full test suite passes on `milestone/M25`
- [ ] Milestone Closure Declaration produced

---

## Acceptance Criteria (Milestone)

1. The phase-closure process lists README update, version bump, and tag as mandatory steps (E25.1).
2. AOG, PSG, and the Execution Chat Starter templates describe the SN-13 default-accept model;
   the Review Decision is documented as the exception path (E25.2).
3. `bin/ai-project-init` writes `.ai-project/agents/`, asserted by a test; docs agree (E25.3).
4. No codified text contradicts default-accept; Layer-8 human review is preserved where mandated.

---

## Timeline

**Target Start:** 2026-07-02
**Target Completion:** 2026-07-07 (3–5 days per Phase spec estimate; 3 small epics)
**Actual Start:** Not started
**Actual Completion:** Not started

---

## Notes

- **M25 is the final P6 milestone** (`is_final: true`). On consolidation, the Phase Chat proceeds
  to **phase delivery** (`phase/P6 → master`, PR #95) + Phase Delivery Notice — following the
  canonical phase-closure sequence E25.1 introduces (README update / version bump / tag). This
  is the intended dogfood: P6 closes by the process it just codified, not by a Steering Note.
- **E25.2 is the subtle one.** It is a reconciliation, not an append: the codified always-review
  language (PSG §11.5/§12/§1A/§13; AOG Stage-2 text; the starter templates) contradicts the
  operating default-accept model. The epic must codify default-accept **and** remove the
  contradiction **without** deleting the Layer-8 human-review requirement — scoping precisely
  which gate each governs.
- **E25.3 is genuinely small** but has a doc half: QUICK-START (and siblings) currently describe
  the CLI writing `.github/agents/`; script and docs must be reconciled together, and a test must
  be added (none exists today).
- The stale README banner ("226/226") is a good first target for E25.1's mandatory README-update
  step, or for the P6 phase-delivery README update that follows.
- Default-accept (SN-13) governs M25's own delivery: clean Epic/Milestone deliveries are
  auto-accepted; Review Decisions are the exception path only.
- Exact section numbers, whether a phase-closure template is added, and whether a `.github/agents/`
  tool copy is retained are Epic-level design calls **within M25's scope**; the milestone fixes
  the contract (mandatory phase-closure steps; default-accept codified + reconciled; init writes
  the agnostic path with a test), not the wording.
