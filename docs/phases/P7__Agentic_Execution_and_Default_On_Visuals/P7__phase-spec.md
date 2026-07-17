---
phase: P7
name: Agentic Execution and Default-On Visuals
status: completed
start_date: 2026-07-12
planned_end_date: 2026-09-05
version: 1.1.0
---

# Phase P7: Agentic Execution and Default-On Visuals

## Executive Summary

P1–P6 built and hardened the governance machine and gave it a visual comprehension layer.
**In P7 the machine starts doing the work itself.** The adapter epic (P7-AE-1) produces the
first real, non-mocked agentic run — the system executing its own epics through the P3
orchestrator on local models — and SN-17 flips visuals from opt-in to the **default lens**
through which the CFO follows that increasingly autonomous flow. The governance
reconciliations (P7-GH-16, P6-GH-14, P6-GH-15) clean the contradictions that real consumer
projects (`character-factory`, `local-agent-runner`) actually hit during adoption and
execution.

P7 is scoped by **SN-18** (P7 spine), which ratifies the full candidate pool with nothing
deferred and fixes **P7-AE-1 as milestone one**. It builds on the **HQ ruling of 2026-07-11**
(P7-AE-1 unblocks the stalled `local-agent-runner` P2) and **SN-17** (visuals default-on).
All binding decisions in those inputs are settled and are **not** for re-debate.

Three milestones:

1. **M26 — First Real Agentic Run (P7-AE-1)** — build `bin/run-dev-agent`, wire the proven
   `local-agent-runner` engine as the orchestrator's `dev_command`, and complete one live
   Epic non-mocked. Scheduled **first** (binding).
2. **M27 — Visuals Default-On (SN-17)** — flip visuals to default-on/opt-out per SN-17's four
   binding decisions, and resolve Ollama+ComfyUI single-GPU coexistence as a design task
   inside this milestone.
3. **M28 — Governance Reconciliations** — P7-GH-16 (Level-0 handoff + HQ opener template),
   P6-GH-14 (Delivery-Notice ordering), P6-GH-15 (init installs superseded agent file), and
   P7-GH-17 (retire the Delivery Authorization ceremonial block — SN-19).

---

## Vision

By the end of P7:

- ✅ **The system executes its own epics for real** — a live Epic runs through the P3
  orchestrator with `local-agent-runner` wired in as `dev_command` on a local model,
  non-mocked, and is accepted like any other epic
- ✅ **A partner project unblocks** — the same live run is `local-agent-runner`'s P2-M3/E3.2
  evidence, accepted in its Milestone Chat, closing its stalled Phase P2
- ✅ **Visuals are the default lens** — visual production is on by default with an explicit
  opt-out; specs and delivery/closure declarations get a visual as they are created;
  structural-first keeps this free for projects with no endpoint
- ✅ **Local inference coexists** — the Ollama runner and ComfyUI share the single GPU under a
  documented scheduling design, so generative visuals don't starve epic execution
- ✅ **Adoption contradictions are gone** — the Level-0 handoff is defined one coherent way (or
  explicitly two, by scale), an HQ starter template exists, Delivery-Notice ordering is
  reconciled, and `ai-project-init` installs the canonical agent file

---

## Scope

### P7.1: First Real Agentic Run (M26) — P7-AE-1

The flagship. Turn the proven-but-mocked orchestration and the proven standalone runner into
**one real run**. Both halves are ready: `bin/ai-project-orchestrator`'s Agentic Mode passed
all 5 verify-loop scenarios end-to-end (with dev/QA mocked), and `local-agent-runner` v1.0.0
is proven (155 tests) with its P2 runner-side support delivered (`write_file`/`list_dir`/`git`
tools + `--context` on the CLI + the SN-3 final-answer repair nudge). The adapter is the one
remaining variable.

**Execution sequence (from the HQ ruling, binding):**
1. Deliver `bin/run-dev-agent` — the CONTRACT §7 adapter shim. Invoked by the orchestrator as
   `dev_command`; reads `AI_PROJECT_ACTIVE_MODEL` from the env; builds a runner Task
   (`--task` = the epic's Definition of Done, `--context` = the **scoped** epic spec/starter —
   never full governance, `--tools` = the coding set scoped to the repo, `--model` = the active
   tag); invokes the runner; returns its exit code to the orchestrator; writes the transcript
   into the epic's artifacts.
2. Switch `.ai-project.yml` `epic_dev` from `llama3:8b` (verified unusable — empty tool-call
   responses) to `qwen2.5-coder:14b`.
3. Wire the runner as `dev_command` and **drop the `04_epic.json` mock trigger**.
4. Execute one live Epic end-to-end.

**Binding design constraint (SN-3 / runner P1 audit):** the adapter **MUST NOT depend on the
runner's `final_answer`** — it is systematically unreliable on Q&A-shaped tasks with
`qwen2.5-coder:14b`. Epic success is the QA `validation_command` exit code and the transcript,
never prose.

**Cross-repo exit obligation (from the ruling / SN-18):** the live-run transcript is also
`local-agent-runner`'s P2-M3/E3.2 evidence. It **must be surfaced to that project's P2-M3
Milestone Chat for acceptance**, closing E3.2 → M3 → P2 in sequence. This is an AE-1 exit
criterion, not an optional follow-up.

### P7.2: Visuals Default-On (M27) — SN-17

Flip visual production from opt-in to the default lens, per SN-17's four binding decisions
(carried into P7 unchanged by SN-18):

1. **Default-on with an explicit opt-out.** AOG §16.1 flips from opt-in to default-on;
   `visual_artifacts.enabled: false` is the opt-out. Reconcile `ai-project-yml-spec.md` §3.5,
   `governance/guides/visual-artifacts.md`, the spec templates' Visual Bindings sections, and
   the agent definitions.
2. **Structural-first default.** With no `comfyui_url` configured, default-on produces
   **structural** visuals (Mermaid/PlantUML) only; generative activates when an endpoint is
   present. Default-on is therefore safe at zero infrastructure.
3. **Trigger set.** Automatic production is limited to **specs + delivery/closure
   declarations**. Any other artifact (steering note, progress digest, merge authorization, …)
   gets a visual **on demand** — asked for in the proper chat, pointing to the artifact file.
4. **Enforcement is a setting, not a hard gate.** A defaulted-true config key (e.g.
   `visual_required_for_specs: true`) in the `visual_artifacts` block. Opt-out is a config
   change, not a per-artifact negotiation. (Exact key naming is a scoping-level detail; the
   mechanism is decided.)

**Coexistence design task (SN-18 decision 4 — inside this milestone, not its own epic, not
deferred):** the Ollama runner and ComfyUI contend for one 16 GB GPU on the CFO's host
(`~/soft-dev/ai-stack` runs both, with known RAM contention). Because the contention bites
when generative visuals actually run, it is designed **where it bites** — here. Deliverable: a
documented GPU/VRAM scheduling design (and any config or guardrails) so generative visual
production does not starve local-model epic execution.

### P7.3: Governance Reconciliations (M28)

Three small doc/CLI contradiction fixes surfaced by real adoption. Independent of the agentic
and visual work.

- **P7-GH-16 — Level-0 handoff defined two contradictory ways.** `seed.md` Rule 4 converges on
  Project Brief + HQ Chat Opener → HQ Chat; `genesis.md` / `start-a-project.md` /
  `chat-hierarchy.md` converge on committed `genesis.md` → Phase Chat directly (HQ never
  opened, despite the packet being named "HQ Context Packet"). Decide the canonical Level-0
  output — or codify both as scale-dependent — and reconcile all four docs. **Sub-item (SN-2):**
  promote the existing `governance/systems/hq-chat-opener.md` into `governance/templates/` as
  the missing HQ starter template.
- **P6-GH-14 — Delivery-Notice ordering.** P4.1 has Completion → review → merge → Delivery
  Notice; PSG §12 has execution → Delivery Notice → review. Reconcile to one ordering.
- **P6-GH-15 — init installs superseded agent file.** `bin/ai-project-init` installs the
  superseded `governance/agents/hq.agent.md` instead of the canonical unified
  `governance/agents/governance.agent.md` (also resolves the `hq`-vs-`governance` filename
  mismatch). A script + test + doc behavior change.
- **P7-GH-17 — retire the Delivery Authorization ceremonial block (SN-19).** The Epic /
  Milestone **Delivery Authorization** blocks in the starter tier survived E25.2's SN-13
  default-accept reconciliation. PSG §1A gate-scoping (under §11.6) already demoted delivery
  authorization to an **in-chat act — no artifact** on the happy path, but the artifact-shaped
  blocks persist in both starter templates, the `governance/systems/` mirrors
  (milestone/phase/hq execution-chat-starter), and AOG §1A step 6 + the two §10 enforcement
  bullets. A docs-only reconciliation (E25.6-shaped): **retire the ceremonial block; preserve
  the in-chat merge authorization unchanged** (the CFO still says "merge it"; the harness
  enforces human merge authorization regardless). Fold the load-bearing **merge instruction**
  into each starter's execution instructions. *The live P7 phase-execution starter has already
  been amended by HQ under the GH-9 path at SN-19 acceptance; the live M26 milestone starter's
  block is the Phase Chat's to sweep (adjacency).*

---

## Out of Scope

- **Rebuilding the runner.** `local-agent-runner` is a proven standalone engine (v1.0.0) with
  its P2 runner-side support delivered. P7 builds the **adapter** (`bin/run-dev-agent`) inside
  ai-project-system per CONTRACT §7 / SN-4 — not the engine.
- **Runner CF-2 (library entry point)** — deferred by the runner's own P2 CFO decision.
- **Broad runner hardening** — multi-model validation, retry/backoff, concurrency, packaging.
- **Re-debating the settled decisions** — AE-1-first, orchestrator-driven first run (no interim
  scripted path), and SN-17's four visual decisions are all ratified.
- **Standing up ComfyUI / storage-backend infrastructure** — CFO-side; P7 designs the
  coexistence and the by-link convention, not the hosting.
- **A cross-cutting / project-spanning visual reel** — still deferred (P6 boundary).

---

## Open Design Questions (resolve within the named milestone — non-blocking)

**A. The first real-run target Epic (M26).** What epic does the first live run execute? Options:
a purpose-built minimal epic as a proving vehicle, or a real small P7 epic (e.g. an M28
reconciliation) as dogfooding.
- *Recommended default:* a **purpose-built minimal, self-contained epic** as the proving
  vehicle — it isolates the run from unrelated scope and keeps M26 independent of M28 ordering.

**B. Canonical Level-0 output (M28 / P7-GH-16).** `genesis.md`-only, or `genesis.md` + HQ Chat
Opener, or both flows codified as scale-dependent?
- *Recommended default:* **codify both as scale-dependent** — lightweight `genesis.md` → Phase
  Chat for small bootstraps; full seed → Project Brief + HQ Opener → HQ Chat for ongoing
  projects — and say so explicitly in all four docs. (The governance source project itself
  operates the seed flow; consumer docs teach the genesis flow — both are real.)

**C. Enforcement key naming (M27).** `visual_required_for_specs` vs. per-artifact-type keys.
- *Recommended default:* start with the single `visual_required_for_specs` (default true); add
  per-type keys only if a real need appears. The mechanism (a defaulted-true setting) is
  decided; only the surface is open.

---

## Milestones

### M26: First Real Agentic Run (P7-AE-1) — scheduled first (binding)

**Goal:** Deliver `bin/run-dev-agent` and complete the first real, non-mocked agentic run
through the orchestrator, then hand the transcript to `local-agent-runner`'s P2-M3 for
acceptance.

**Indicative Epics** (the Milestone Chat owns final decomposition):
- **E26.1 — The `run-dev-agent` adapter** — CONTRACT §7 shim: orchestrator `dev_command`,
  env-driven model, Task-building (scoped context only), invocation, exit-code passthrough,
  transcript capture. Honors the no-`final_answer` constraint.
- **E26.2 — Real-model wiring + mock retirement** — switch `epic_dev` → `qwen2.5-coder:14b`,
  wire the runner as `dev_command`, drop the `04_epic.json` mock trigger, update config/tests.
- **E26.3 — First real run + cross-repo acceptance** — execute one live Epic end-to-end
  (Open Design Question A), capture the transcript, and surface it to `local-agent-runner`'s
  P2-M3 Milestone Chat for acceptance (closes E3.2 → M3 → P2).

### M27: Visuals Default-On (SN-17)

**Goal:** Flip visual production to default-on/opt-out per SN-17's four decisions, and resolve
Ollama+ComfyUI coexistence as a design task within.

**Indicative Epics:**
- **E27.1 — Default-on flip + enforcement setting** (decisions 1 & 4) — AOG §16.1 opt-in →
  default-on with opt-out; add the defaulted-true enforcement setting to the `visual_artifacts`
  block; reconcile spec §3.5, guide, templates, agent definitions.
- **E27.2 — Structural-first + trigger-set behavior** (decisions 2 & 3) — codify structural-first
  default (generative only when `comfyui_url` present), the automatic trigger set (specs +
  delivery/closure), and the on-demand path for all other artifact types.
- **E27.3 — Ollama+ComfyUI coexistence design** — documented GPU/VRAM scheduling design (+ any
  config/guardrails) so generative visuals don't starve local-model epic execution.

### M28: Governance Reconciliations

**Goal:** Fix the four doc/CLI contradictions surfaced by real adoption. Independent; may run
in parallel with M27 at the Phase Chat's discretion.

**Indicative Epics:**
- **E28.1 — Level-0 handoff reconciliation + HQ starter template** (P7-GH-16 + SN-2) — resolve
  Open Design Question B; reconcile `seed.md`, `genesis.md`, `start-a-project.md`,
  `chat-hierarchy.md`; promote `systems/hq-chat-opener.md` into `templates/`.
- **E28.2 — Delivery-Notice ordering reconciliation** (P6-GH-14).
- **E28.3 — init canonical agent file** (P6-GH-15) — install `governance.agent.md`, resolve the
  filename mismatch, with a test.
- **E28.4 — Retire the Delivery Authorization ceremonial block** (P7-GH-17 / SN-19) — docs-only,
  E25.6-shaped. Remove the Delivery Authorization sections and their Completion-Requirements
  checklist lines from both starter **templates** (`governance/templates/{milestone,phase}-execution-chat-starter.md`)
  and the `governance/systems/` **mirrors** (milestone/phase/hq execution-chat-starter); fold
  the load-bearing merge instruction into each starter's execution instructions. Reword AOG §1A
  step 6 and the two §10 enforcement bullets to the in-chat authorization language PSG §1A
  gate-scoping already uses (authorization preserved; artifact retired). The live P7 phase
  starter is already amended (HQ, GH-9); the M26 milestone starter is the Phase Chat's to sweep.

---

## Success Criteria

### P7 is Complete When:

1. ✅ **A live Epic completes non-mocked** through the orchestrator with `local-agent-runner`
   wired in as `dev_command` on `qwen2.5-coder:14b`; success is the QA `validation_command`
   exit code + transcript, not `final_answer`
2. ✅ **The `04_epic.json` mock trigger is retired** and `epic_dev` is off `llama3:8b`
3. ✅ **The cross-repo hand-back is complete** — the run's transcript is accepted in
   `local-agent-runner`'s P2-M3 Milestone Chat (AE-1 exit criterion)
4. ✅ **Visuals are default-on with an opt-out** — AOG §16.1 flipped; structural-first at zero
   infra; automatic for specs + delivery/closure declarations; enforcement setting present and
   defaulted true; spec §3.5 / guide / templates / agent defs reconciled
5. ✅ **Coexistence is designed** — a documented GPU/VRAM scheduling design for Ollama+ComfyUI
   on one host
6. ✅ **Level-0 handoff is coherent** — canonical output decided (or both flows codified as
   scale-dependent) and all four docs agree; an HQ starter template exists in `templates/`
7. ✅ **Delivery-Notice ordering reconciled** (P6-GH-14) and **`ai-project-init` installs the
   canonical agent file** (P6-GH-15)
8. ✅ **Delivery Authorization ceremonial block retired** (P7-GH-17) — gone from the starter
   templates, the `governance/systems/` mirrors, and AOG §1A/§10; the in-chat merge
   authorization preserved unchanged

---

## Acceptance Criteria

The CFO (Layer 8) will accept P7 complete when:

- [ ] `bin/run-dev-agent` exists, is invoked by the orchestrator as `dev_command`, and passes
  scoped context (not full governance) to the runner
- [ ] A recorded live-run transcript shows a real Epic completing through the orchestrator on a
  local model, non-mocked
- [ ] That transcript is accepted in `local-agent-runner`'s P2-M3 Milestone Chat
- [ ] A fresh project with no `visual_artifacts` block still produces structural visuals for a
  new spec (default-on, structural-first)
- [ ] Setting `visual_artifacts.enabled: false` cleanly opts out
- [ ] A documented Ollama+ComfyUI coexistence design is present
- [ ] `seed.md`, `genesis.md`, `start-a-project.md`, and `chat-hierarchy.md` no longer
  contradict each other on the Level-0 handoff; an HQ starter template is in `templates/`
- [ ] `bin/ai-project-init` installs `governance.agent.md`
- [ ] No Delivery Authorization ceremonial block remains in the starter templates,
  `governance/systems/` mirrors, or AOG §1A/§10; each starter still carries the merge
  instruction as an in-chat act

---

## Dependencies

### Internal
- P3 orchestrator Agentic Mode proven (verify-loop 5/5, sandbox image built) — complete
- P5/P6 visual-artifacts framework on master at v5.1.0 — complete

### External / cross-repo
- **`local-agent-runner` P2 runner-side support — DELIVERED.** P2-M2 closed
  (`write_file`/`list_dir`/`git` + permission model + SN-3 repair nudge); P2-M3/E3.1 merged
  (CONTRACT §7 runner-side verification + `--context` on CLI). The runner-side gate for
  P7-AE-1 is cleared (HQ ruling 2026-07-11).
- **`local-agent-runner` P2-M3 Milestone Chat** must accept the AE-1 live-run transcript to
  close E3.2 → M3 → P2 (cross-repo hand-back; CFO relays as shared Layer-8).
- CFO-side ComfyUI endpoint + storage backend remain optional for using generative visuals;
  structural-first default needs none.

---

## Timeline

**Estimate:** 3 Milestones, ~8–9 Epics
- M26 (First Real Agentic Run): 5–8 days (3 epics) — **first**, time-sensitive (a partner
  project's P2 closure is stalled on it)
- M27 (Visuals Default-On): 5–7 days (3 epics) — includes the coexistence design task
- M28 (Governance Reconciliations): 4–6 days (4 small epics) — independent
- **Total: ~2.5–3 weeks**

---

## Reference

### Governing Steering Notes & Ruling
- **SN-18:** `.ai-project/artifacts/steering-notes/2026-07-12__creation-chat__steering-note__P7-spine.md`
  — P7 spine; full pool, AE-1 first, coexistence placement (binding)
- **SN-17:** `.ai-project/artifacts/steering-notes/2026-07-11__creation-chat__steering-note__visuals-default-on.md`
  — visuals default-on, four binding decisions (binding)
- **HQ Ruling (2026-07-11):** `.ai-project/artifacts/rulings/2026-07-11__ai-project-system-hq__ruling__p7-ae-1-adapter-unblocks-runner-p2.md`
  — AE-1 unblocks runner P2; orchestrator-driven first run; cross-repo hand-back

### Key Reference Documents
- `local-agent-runner/CONTRACT.md` §7 — the adapter contract (task-building, exit codes, transcript)
- GitHub issues [#111](https://github.com/panchew/ai-project-system/issues/111) (P7-AE-1),
  [#110](https://github.com/panchew/ai-project-system/issues/110) (P7-GH-16)
- `bin/ai-project-orchestrator` — Agentic Mode (proven, dev/QA previously mocked)
- `governance/AI-OPERATING-GUIDELINES.md` §16.1 — opt-in policy to flip to default-on
- `governance/guides/visual-artifacts.md`, `governance/ai-project-yml-spec.md` §3.5

### Ratified Decisions (settled — NOT for re-debate)
1. **AE-1 is milestone one** — scheduled first, independent of the broader theme.
2. **Orchestrator-driven first run** — no interim scripted path.
3. **Adapter must not depend on `final_answer`** — success = QA exit code + transcript.
4. **Coexistence is designed inside the visuals milestone** — not its own epic, not deferred.
5. **SN-17's four decisions carry in unchanged.**

### Items Excluded from P7
- Runner engine rebuild / CF-2 / broad hardening — runner's own scope
- ComfyUI + storage hosting — CFO-side infrastructure
- Cross-cutting visual reel — deferred (P6 boundary)

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-07-12 | Initial P7 phase spec. Three milestones (M26–M28), ~8–9 Epics. Agentic execution (first real run, P7-AE-1) + default-on visuals (SN-17) + governance reconciliations (P7-GH-16, P6-GH-14, P6-GH-15). Scoped by SN-18 on the HQ ruling (2026-07-11) and SN-17; AE-1 fixed as milestone one with a cross-repo E3.2 acceptance exit criterion. |
| 1.1.0 | 2026-07-12 | Mid-flight amendment (GH-9) accepting **SN-19**: added **E28.4 (P7-GH-17)** to M28 — retire the Delivery Authorization ceremonial block (SN-13 missed reconciliation) across starter templates, `governance/systems/` mirrors, and AOG §1A/§10, preserving the in-chat merge authorization. Live P7 phase-execution starter amended at the same time (HQ, GH-9). M28 now 4 epics. |
