---
milestone: M27
name: Visuals Default-On
phase: P7
status: planned
start_date: 2026-07-13
epics:
  - E27.1
  - E27.2
  - E27.3
is_final: false
---

# Milestone M27 — Visuals Default-On (SN-17)

## Purpose

Flip visual-artifact production from an opt-in capability to the **default lens** through
which the CFO follows an increasingly autonomous flow, per SN-17's four binding decisions —
and, because the contention only bites once generative visuals actually run, design the
Ollama+ComfyUI single-GPU coexistence **here**, inside this milestone, not as its own epic.

M26 (First Real Agentic Run) is fully consolidated to `phase/P7` (merge `db4a34f`) and its
cross-repo hand-back to `local-agent-runner` is delivered and resolved. **M27 is milestone two
of P7** — independent of M26's agentic-execution surface; it touches the visual-artifacts
framework built in P5/P6 (`governance/AI-OPERATING-GUIDELINES.md` §16, `governance/
ai-project-yml-spec.md` §3.5, `governance/guides/visual-artifacts.md`).

---

## Binding Context (SN-17 — settled, NOT for re-examination)

SN-17's four decisions carry into M27 unchanged (ratified by SN-18, the P7 spine):

1. **Default-on with an explicit opt-out.** AOG §17.1 flips from opt-in to default-on;
   `visual_artifacts.enabled: false` becomes the opt-out, not the baseline.
2. **Structural-first default.** With no `comfyui_url` configured (or generative otherwise
   unreachable), default-on produces **structural** visuals (Mermaid/PlantUML) only.
   Generative activates when an endpoint is present. Default-on is therefore safe at **zero
   infrastructure** — no project is forced to stand up ComfyUI to get the default behavior.
3. **Trigger set.** Automatic production is limited to **specs + delivery/closure
   declarations**. Every other artifact type (steering note, progress digest, merge
   authorization, …) gets a visual **on demand** — asked for in the proper chat, pointing at
   the artifact file — never automatically.
4. **Enforcement is a setting, not a hard gate.** A defaulted-true config key (e.g.
   `visual_required_for_specs: true`) lives in the `visual_artifacts` block. Opting out is a
   config change, not a per-artifact negotiation.

**Coexistence is inside this milestone** (SN-18 decision 4, not its own epic, not deferred):
the Ollama runner and ComfyUI share one 16 GB GPU on the CFO's host (`~/soft-dev/ai-stack`).
Because the contention only manifests when generative visuals actually run, it is designed
where it bites.

---

## Problem Statement

The visual-artifacts framework (P5/P6) was built and shipped **opt-in and off by default** —
correct for its own milestone, but now the wrong default for the phase's stated goal (visuals
as the CFO's default lens on an increasingly autonomous system). Verified on `phase/P7`:

- **AOG §17.1** states plainly: "Visual artifacts are an **opt-in** capability... **absent
  block or `enabled: false` means the capability is off**."
- **`governance/ai-project-yml-spec.md` §3.5** — the `enabled` field's documented default is
  **`false`**; "When the block is **absent**, the visual-artifacts capability is
  **disabled**... a project must explicitly turn the capability on."
- **`bin/ai-project-orchestrator`** — `DEFAULT_VISUAL_ARTIFACTS = {"enabled": False, ...}`
  (line 31); `resolve_visual_artifacts()` hardcodes `resolved["enabled"] = False` before
  merging any provided block (line 144) — the code path that must flip.
- **`governance/guides/visual-artifacts.md`** opens: "The capability is **opt-in** and **off
  by default**."
- **No enforcement-setting key exists anywhere** (`visual_required_for_specs` or equivalent) —
  grepped across `governance/` and `bin/`, zero hits. This is genuinely new surface, not a
  rename.
- **The source repo's own `.ai-project.yml`** explicitly sets `visual_artifacts.enabled:
  false`, commented as keeping "the suite... green without a live ComfyUI endpoint" — but
  structural visuals need no endpoint (§17.3), so this reasoning does not, on its face,
  justify disabling structural once the default flips. Whether the source repo's own config
  changes is an Epic-level call (see E27.1).
- **The single-GPU contention is real and currently undesigned.** `~/soft-dev/ai-stack/
  docker-compose.yml` runs both `ollama` and `comfyui` services, and **both** request GPU
  reservations with `count: all` and no memory partitioning — Docker's `count: all` does not
  sub-allocate VRAM between them; nothing in the compose file or the codebase coordinates
  concurrent use.

---

## Goals

By the end of this milestone:

1. **Visuals are default-on with an opt-out.** AOG §17.1 reads default-on/opt-out; the
   yml-spec's documented `enabled` default is `true`; `resolve_visual_artifacts()`'s hardcoded
   `False` becomes a default of `True` when the block is absent, while an explicit `enabled:
   false` still disables (E27.1).
2. **An enforcement setting exists, defaulted true.** A new `visual_artifacts` key (naming is
   Open Design Question C) governs whether specs/delivery/closure artifacts are required to
   carry a visual; defaulted `true`; documented in the yml-spec and AOG (E27.1).
3. **Structural-first is codified as the zero-infra safe path.** No project is forced to run
   ComfyUI to get default-on behavior; generative only activates with `comfyui_url` present
   (E27.2).
4. **The automatic trigger set is codified.** Specs and delivery/closure declarations get a
   visual automatically when the capability is on; every other artifact type is on-demand only
   (E27.2).
5. **Ollama+ComfyUI coexistence is designed.** A documented GPU/VRAM scheduling approach (plus
   any config/guardrails) addresses the `count: all`/no-partitioning gap found above, so
   generative visual production does not starve local-model epic execution (E27.3).

---

## Non-Goals

This milestone explicitly does **not**:

- **Touch M26's agentic-execution surface** (`bin/run-dev-agent`, the orchestrator's
  `dev_command` wiring, the runner) — that is closed and out of scope here.
- **Touch M28's governance-reconciliation surfaces** (Level-0 handoff, Delivery-Notice
  ordering, init agent-file path, or the SN-19 Delivery-Authorization retirement) — independent
  work, may run in parallel per the phase spec.
- **Stand up ComfyUI or any storage-backend infrastructure.** E27.3 designs the coexistence
  and scheduling approach; it does not host anything. The CFO owns the infrastructure.
- **Re-debate any of SN-17's four decisions** or the coexistence-placement decision — all are
  ratified and binding.
- **Add per-artifact-type enforcement keys** unless E27.3 — wait, unless the Milestone Chat's
  own resolution of Open Design Question C finds a real need; the recommended default is the
  single `visual_required_for_specs` key.

---

## In Scope

- **E27.1** — the default-on flip in AOG §17.1, the yml-spec §3.5 default change, the
  `bin/ai-project-orchestrator` code flip, the new enforcement setting, and reconciliation of
  every surface that currently asserts opt-in/off-by-default (`governance/guides/
  visual-artifacts.md`, the spec templates' Visual Bindings sections if they assert opt-in
  language, agent definitions if they need updating).
- **E27.2** — codifying structural-first as the zero-infra default behavior and the automatic
  trigger set (specs + delivery/closure only; everything else on-demand) — primarily a
  normative-documentation epic (AOG §17 already has the structural/generative and per-level
  machinery from P5/P6; E27.2 states the *default-on* trigger policy on top of it).
- **E27.3** — a documented GPU/VRAM scheduling design for Ollama+ComfyUI coexistence, grounded
  in the concrete `docker-compose.yml` finding above, plus any config or guardrails the design
  calls for.

## Out of Scope

- Any M26 or M28 surface; ComfyUI/storage hosting; re-debating SN-17 or the coexistence
  placement; per-artifact-type enforcement keys beyond the single recommended default unless
  the Milestone Chat records a reasoned need.

---

## Planned Epics

### Confirmed Epics

- **E27.1 — Default-on flip + enforcement setting** (High)
- **E27.2 — Structural-first + trigger-set behavior** (High, may proceed alongside E27.1 —
  see Dependencies and Sequencing)
- **E27.3 — Ollama+ComfyUI coexistence design** (Medium)

> **Artifact scope (GH-8 adjacency):** the Phase Chat produces only this Milestone spec and
> the Milestone Execution Chat Starter. The **Milestone Chat** owns final epic planning and
> authors every Epic spec and Epic Execution Chat Starter. No Phase-level Epic drafts exist.

### Deferred Epics

- None.

---

## Epic Detail

### E27.1 — Default-on flip + enforcement setting (High)

**Source:** P7 phase spec P7.2 decisions 1 & 4; SN-17.

**Grounding (verified on `phase/P7`):**

- `governance/AI-OPERATING-GUIDELINES.md` §17.1 — the opt-in gating language to flip
  ("Visual artifacts are an **opt-in** capability... absent block or `enabled: false` means
  the capability is off").
- `governance/ai-project-yml-spec.md` §3.5 — the `enabled` field's table row (`Default:
  false`) and prose ("When the block is **absent**, the visual-artifacts capability is
  **disabled**... a project must explicitly turn the capability on").
- `bin/ai-project-orchestrator:30-34` (`DEFAULT_VISUAL_ARTIFACTS`) and `:139-149`
  (`resolve_visual_artifacts`, specifically the hardcoded `resolved["enabled"] = False` at
  line 144, which runs **before** any provided block is merged in) — the exact lines the flip
  touches.
- `tests/` — `test_visual_artifacts_absent_is_disabled` and
  `test_visual_artifacts_absent_block_is_disabled` (in `bin/ai-project-orchestrator`'s test
  module) currently assert the **old** default; these must be rewritten to assert the new
  default-on/structural-first behavior, not merely deleted.
- `governance/guides/visual-artifacts.md:4` — "The capability is **opt-in** and **off by
  default**" — the guide's opening framing to reconcile.
- **No enforcement-setting key exists today** — this is new schema, not a rename. Name it per
  Open Design Question C's resolution (recommended default: single
  `visual_required_for_specs: true`).
- **Epic-level design point:** whether the source repo's own `.ai-project.yml` (currently
  explicit `enabled: false`) changes as part of this epic's dogfooding, given structural
  visuals need no endpoint and are not "generated binaries" in the §17.5 sense. Decide and
  document; do not assume either way without stating the reasoning.

**Deliverables:**

1. AOG §17.1 rewritten: default-on with `enabled: false` as the explicit opt-out.
2. `ai-project-yml-spec.md` §3.5: `enabled`'s documented default → `true`; prose reconciled;
   version bump + changelog row.
3. `bin/ai-project-orchestrator`: `DEFAULT_VISUAL_ARTIFACTS["enabled"]` → `True`;
   `resolve_visual_artifacts()`'s hardcoded override removed/inverted so an absent block
   resolves to enabled (structural-first — E27.2 supplies the structural/generative split;
   this epic only flips the on/off default).
4. The new enforcement-setting key: schema entry in the yml-spec, validation rule, resolution
   logic, default `true`, documented behavior.
5. Existing tests rewritten to assert the new defaults (not merely deleted); new tests for the
   enforcement-setting key.
6. Reconcile `governance/guides/visual-artifacts.md`'s opt-in framing and any spec-template /
   agent-definition surface that asserts the old default (verify each named surface before
   editing — do not assume all need changes; the phase spec names spec templates' Visual
   Bindings sections and agent definitions as candidates, but the current `governance/agents/`
   files contain no opt-in language to reconcile — confirm this remains true and note it if a
   surface needs no change).
7. Decide and document the source-repo `.ai-project.yml` question above.
8. AOG + yml-spec version bumps and changelog rows.

**Definition of Done:**
- [ ] AOG §17.1 describes default-on/opt-out
- [ ] yml-spec §3.5 documents `enabled` defaulting to `true`
- [ ] `resolve_visual_artifacts()` resolves an absent block to enabled (not disabled)
- [ ] The enforcement-setting key exists, is validated, defaults `true`, and is documented
- [ ] All affected tests updated (not deleted) to assert the new behavior
- [ ] `governance/guides/visual-artifacts.md` and any other surface asserting opt-in language
      reconciled (or confirmed unaffected, with that confirmation on record)
- [ ] The source-repo `.ai-project.yml` question is decided and documented
- [ ] Full test suite passes

**Acceptance Criteria:**
- [ ] A fresh project with no `visual_artifacts` block produces structural visuals for a new
      spec by default (verified once E27.2's structural-first behavior is also in place —
      this epic supplies the on/off default; E27.2 supplies the structural/generative split)
- [ ] Setting `visual_artifacts.enabled: false` cleanly opts out
- [ ] The enforcement setting is present, defaulted true, and documented

---

### E27.2 — Structural-first + trigger-set behavior (High)

**Source:** P7 phase spec P7.2 decisions 2 & 3; SN-17.

**Grounding (verified on `phase/P7`):**

- AOG §17.3 ("Two modes") and §17.4 ("Tool-capability gating") **already** define
  Structural/Generative and the capability gate from P5/P6 — this epic does not rebuild that
  machinery. What is missing is the **default-on trigger policy** layered on top: which
  artifact types get a visual *automatically* now that the capability is on by default, versus
  which stay on-demand.
- **No automatic trigger logic exists in code today** — visual production is chat-level
  behavior (an agent decides to produce one), not something `bin/ai-project-orchestrator`
  invokes on artifact creation. This epic's deliverable is primarily **normative**: which
  artifact types the default-on capability applies to, stated clearly enough that any chat
  level can follow it without inventing its own interpretation.
- The phase spec's trigger set is exact: **specs + delivery/closure declarations**, automatic;
  everything else (steering note, progress digest, merge authorization, …), on-demand only.

**Deliverables:**

1. AOG (§16, likely a new subsection alongside §17.1) states: with the capability on
   (default), structural-first governs — no `comfyui_url` ⇒ structural only, generative
   activates only when an endpoint is present (restating/cross-referencing §17.3/§17.4, not
   duplicating them).
2. AOG states the automatic trigger set explicitly: specs + delivery/closure declarations
   automatic; all other artifact types on-demand (asked for in the proper chat, pointing at
   the artifact file).
3. Per-level guidance reconciled if §17.2's existing per-level table needs a note on which
   levels' spec-shaped artifacts are covered by the automatic trigger.
4. `governance/guides/visual-artifacts.md` reconciled to describe the trigger-set behavior
   (which artifacts are automatic vs. on-demand) alongside its existing structural/generative
   content.
5. AOG version bump + changelog row.

**Definition of Done:**
- [ ] AOG codifies structural-first as the zero-infra default behavior for the now-default-on
      capability
- [ ] AOG codifies the automatic trigger set (specs + delivery/closure only) and the on-demand
      path for every other artifact type
- [ ] `governance/guides/visual-artifacts.md` reconciled
- [ ] Full test suite passes

**Acceptance Criteria:**
- [ ] A fresh project with no `visual_artifacts` block still produces structural visuals for a
      new spec (default-on, structural-first) — the milestone-level acceptance criterion,
      jointly satisfied with E27.1
- [ ] The trigger set (specs + delivery/closure automatic; everything else on-demand) is
      stated as a normative rule, not left implicit

---

### E27.3 — Ollama+ComfyUI coexistence design (Medium)

**Source:** P7 phase spec P7.2 coexistence task; SN-18 decision 4.

**Grounding (verified — the concrete contention this epic designs around):**

- `~/soft-dev/ai-stack/docker-compose.yml` runs both `ollama` (port 11434) and `comfyui`
  (port 8188) as separate services, **each** with a `deploy.resources.reservations.devices`
  block requesting `driver: nvidia, count: all, capabilities: [gpu]` — i.e., **both services
  can claim the entire GPU simultaneously**; nothing in the compose file partitions VRAM or
  serializes access. This is the "known RAM contention" the phase spec names, now confirmed at
  the file level.
- The contention is real only when generative visual production actually invokes ComfyUI
  concurrently with a live-model epic execution (M26's `bin/run-dev-agent` path) — hence
  designing it here, where SN-18 places it, rather than as a standalone epic.

**Epic-level design points (the Milestone Chat / Coding Agent resolves these; not prescribed
here):** whether the design is a scheduling policy (e.g., don't run generative visual
production while an agentic epic run is in flight), a VRAM-partitioning config change to
`docker-compose.yml` (e.g., explicit memory limits, `MemoryReservation`, or sequential
`docker-compose` profiles), an advisory guardrail documented for the CFO to apply manually, or
some combination. The deliverable is a **documented design** (+ any config/guardrails it
calls for) — not a mandate to stand up new infrastructure (out of scope per the phase spec).

**Deliverables:**

1. A documented GPU/VRAM coexistence design (where it lives — a new guide, a section of
   `visual-artifacts.md`, or a section of the M27 milestone's own artifacts — is an Epic-level
   call) that names the concrete contention (above) and states the scheduling/guardrail
   approach.
2. Any config or guardrail changes the design calls for (e.g., `docker-compose.yml`
   adjustments, an orchestrator-side check, or a documented manual procedure) — scoped to what
   the design actually requires, not speculative hardening.
3. A clear statement of what remains the CFO's infrastructure responsibility versus what the
   framework encodes.

**Definition of Done:**
- [ ] A documented GPU/VRAM scheduling design for Ollama+ComfyUI coexistence exists
- [ ] The design names the concrete `count: all`/no-partitioning contention found in
      `~/soft-dev/ai-stack/docker-compose.yml`
- [ ] Any config/guardrail changes the design calls for are implemented and documented
- [ ] Full test suite passes (if any config/guardrail change touches tested code)

**Acceptance Criteria:**
- [ ] A documented Ollama+ComfyUI coexistence design is present and addresses the confirmed
      contention

---

## Branch Strategy

```
master
└── phase/P7                    (M26 consolidated — HEAD e0a20c5)
    └── milestone/M27            ← this milestone (Milestone Chat branches from phase/P7)
        ├── epic/P7-M27-E27.1    ← default-on flip + enforcement setting
        ├── epic/P7-M27-E27.2    ← structural-first + trigger-set behavior
        └── epic/P7-M27-E27.3    ← Ollama+ComfyUI coexistence design
```

Epic PRs target `milestone/M27`. Consolidation PR: `milestone/M27 → phase/P7`.
M27 is **not** the final P7 milestone (`is_final: false`) — M28 follows (may run in parallel
per the phase spec's "Independent — may parallel M27" note).

---

## Prerequisites

- This Milestone spec and its Milestone Execution Chat Starter are git-tracked on `phase/P7`
  (verify with `git ls-files --error-unmatch <path>` — the GH-1 convention).
- M27 targets present and git-tracked on `phase/P7`:
  - `governance/AI-OPERATING-GUIDELINES.md` (v2.6.0; §16 in full)
  - `governance/ai-project-yml-spec.md` (§3.5)
  - `governance/guides/visual-artifacts.md`
  - `bin/ai-project-orchestrator` (`DEFAULT_VISUAL_ARTIFACTS`, `resolve_visual_artifacts`,
    `validate_visual_artifacts`, and their existing tests)
  - `.ai-project.yml` (the source repo's own `visual_artifacts` block)
- **Host-side (CFO, read-only reference for E27.3):** `~/soft-dev/ai-stack/docker-compose.yml`
  — outside this repo; E27.3 documents a design against it but does not modify that repository
  unless the CFO directs otherwise.

---

## Dependencies and Sequencing

- **E27.1 and E27.2 both edit AOG §17** (E27.1: §17.1's on/off default + the new enforcement
  key; E27.2: the structural-first/trigger-set subsection). Serialize them or use a worktree
  (GH-2) to avoid file contention — same discipline P6-M25 used for its own PSG-editing pair.
- **E27.1 and E27.2 are logically coupled at the acceptance-criteria level**: "a fresh project
  with no `visual_artifacts` block produces structural visuals for a new spec" requires both
  the on/off flip (E27.1) and the structural-first/trigger-set policy (E27.2). They may be
  planned and executed in either order within the serialization above, but the milestone-level
  acceptance criterion is not satisfied until both are merged.
- **E27.3 is independent** — it touches a different repo's config (read-only reference) and
  documentation; it may run in parallel with E27.1/E27.2.
- No dependency on M26 or M28.

---

## Definition of Done (Milestone)

- [ ] E27.1, E27.2, and E27.3 each meet their Definition of Done above
- [ ] All three epic branches merged to `milestone/M27`
- [ ] AOG §17.1 describes default-on/opt-out; the enforcement setting exists and defaults true
- [ ] `resolve_visual_artifacts()` resolves an absent block to enabled, structural-first
- [ ] The automatic trigger set (specs + delivery/closure) and on-demand path are codified
- [ ] A documented Ollama+ComfyUI coexistence design addresses the confirmed GPU contention
- [ ] A fresh project with no `visual_artifacts` block produces structural visuals for a new
      spec; `visual_artifacts.enabled: false` cleanly opts out
- [ ] Full test suite passes on `milestone/M27`
- [ ] Milestone Closure Declaration produced

---

## Acceptance Criteria (Milestone)

1. A fresh project with no `visual_artifacts` block still produces structural visuals for a
   new spec (default-on, structural-first) (E27.1 + E27.2, jointly).
2. Setting `visual_artifacts.enabled: false` cleanly opts out (E27.1).
3. The enforcement setting is present, defaulted true, and documented (E27.1).
4. The automatic trigger set (specs + delivery/closure only; everything else on-demand) is
   codified as a normative rule (E27.2).
5. A documented Ollama+ComfyUI coexistence design is present and addresses the confirmed
   `count: all`/no-partitioning contention (E27.3).

---

## Timeline

**Target Start:** 2026-07-13
**Target Completion:** 2026-07-20 (5–7 days per Phase spec estimate; 3 epics, 2 serialized)
**Actual Start:** Not started
**Actual Completion:** Not started

---

## Notes

- **The default-on flip is a behavior change for every downstream consumer project**, not
  just this repo — an absent `visual_artifacts` block now means structural-visuals-on instead
  of off. This is the intended SN-17 outcome, not a side effect to soften.
- **Structural-first is what makes the flip safe.** No project is forced to stand up ComfyUI
  to get the new default; only generative production needs the endpoint. E27.1 and E27.2
  together carry this — do not let either land without the other, per the coupled acceptance
  criterion above.
- **The enforcement-setting key is new schema**, confirmed by grep — name it per Open Design
  Question C's resolution (recommended default: single `visual_required_for_specs: true`);
  add per-type keys only if a real need surfaces during execution.
- **E27.3's contention is now a confirmed file-level finding**, not a general worry: both
  `ollama` and `comfyui` in `~/soft-dev/ai-stack/docker-compose.yml` request `count: all` GPU
  devices with no partitioning. The design should speak to this specific configuration, not a
  hypothetical one.
- **This milestone does not touch M26 or M28 surfaces.** M28 (now 4 epics per SN-19's E28.4
  amendment) may proceed in parallel per the phase spec's own note.
- Exact AOG section numbering, the enforcement-key's final name (Question C), where the
  coexistence design document lives, and whether the source repo's own `.ai-project.yml`
  changes are **Epic-level design calls within M27's scope** — the milestone fixes the
  contract (default-on/opt-out; structural-first at zero infra; specs+delivery/closure
  automatic, everything else on-demand; enforcement setting defaulted true; coexistence
  designed against the confirmed contention), not the wording.
- Default-accept (PSG §11.6 / AOG §14) governs M27's own delivery: clean Epic/Milestone
  deliveries are auto-accepted by silence; Review Decisions are the exception path only. Per
  SN-19, Epic/Milestone acceptance and the merge instruction are in-chat acts — no Delivery
  Authorization artifact.
