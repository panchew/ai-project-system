---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-07-12T00:00:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-18
    severity: high
    title: P7 spine — the system executes its own epics for real, and visuals become the default lens
decisions:
  - "P7 candidate pool is the full registry: P7-AE-1, SN-17, P7-GH-16, P6-GH-14, P6-GH-15 — nothing deferred."
  - "P7-AE-1 is milestone one, committed and scheduled first (CFO-ratified via HQ ruling 2026-07-11)."
  - "The first real run is orchestrator-driven; no interim scripted path (CFO-ratified 2026-07-11)."
  - "Ollama+ComfyUI coexistence is resolved as a design task inside the SN-17 visuals milestone — not its own epic, not deferred."
  - "SN-17's four binding decisions (default-on/opt-out, structural-first, specs+delivery/closure trigger set, setting-based enforcement) carry into P7 unchanged."
---

# Creation Chat Steering Note — P7 Spine

## Purpose

This note hands HQ the P7 spine so the phase spec and starter can be drafted, per
the HQ ruling of 2026-07-11 ("P7 opens when the Creation Chat hands me the spine").
It closes the P7 scoping thread in the Creation Chat: candidate selection, milestone-
one commitment, and the coexistence placement are all settled below. The runner's
P2 hold is bounded by this handoff — HQ should treat drafting the phase spec as
time-sensitive.

---

## Concerns for HQ Triage

### SN-18 — P7 spine [HIGH]

**Detail:** P1–P6 built and hardened the governance machine; P6 gave it a visual
comprehension layer. In P7 the machine starts doing the work itself: the adapter
epic (P7-AE-1) produces the first real, non-mocked agentic run — the system
executing its own epics through the orchestrator on local models — and SN-17
flips visuals from opt-in to the default lens through which the CFO follows that
increasingly autonomous flow. The governance reconciliations (P7-GH-16,
P6-GH-14, P6-GH-15) clean the contradictions that real consumer projects
(character-factory, local-agent-runner) actually hit during adoption and
execution. [PROPOSED — confirm] this spine phrasing.

[PROPOSED — confirm] **Phase name:** "P7 — Agentic Execution & Default-On
Visuals" (HQ may refine the slug at spec authoring).

**Required action:** Draft the P7 phase spec + phase-execution chat starter with
P7-AE-1 as milestone one, per the ruling and the sequencing input below.

---

## Decisions Already Made

These are the CFO's decisions. Not for HQ to re-debate.

1. **Full pool, nothing deferred.** P7 scope is all five registered candidates:
   P7-AE-1 (adapter / first real run), SN-17 (visuals default-on), P7-GH-16
   (Level-0 handoff reconciliation + HQ opener template promotion), P6-GH-14
   (DN ordering), P6-GH-15 (init installs superseded hq.agent.md). Selected by
   the CFO 2026-07-12.
2. **P7-AE-1 is milestone one** — committed, scheduled first, independent of the
   broader theme (CFO-ratified via the HQ ruling 2026-07-11; a partner project's
   phase closure is stalled on it and all inputs are ready). Execution sequence
   per the ruling: deliver `bin/run-dev-agent` (CONTRACT §7 shim) → switch
   `epic_dev` to `qwen2.5-coder:14b` → wire runner as `dev_command`, drop the
   `04_epic.json` mock trigger → one live Epic end-to-end. Design constraint:
   the adapter MUST NOT depend on the runner's `final_answer`; success is the QA
   `validation_command` exit code and the transcript.
3. **Orchestrator-driven first run, no interim scripted path** (CFO-ratified
   2026-07-11, recorded in the ruling).
4. **Coexistence placement.** The Ollama+ComfyUI single-GPU contention question
   (SN-17 carry-over, flagged in the ruling) is resolved **as a design task
   inside the SN-17 visuals milestone** — it bites when generative visuals
   actually run, so it is designed where it bites. Not its own epic; not
   deferred to a later phase.
5. **SN-17 decisions carry in unchanged:** default-on with opt-out,
   structural-first (generative only when `comfyui_url` is present), automatic
   production for specs + delivery/closure declarations only (everything else
   on demand), enforcement via a defaulted-true setting
   (`visual_required_for_specs`-style; exact key naming is scoping-level).

---

## Sequencing Input (for HQ to shape into milestones)

[PROPOSED — confirm] Three milestones, continuing from M25:

- **M26 — First Real Agentic Run (P7-AE-1).** Fixed first per the ruling.
- **M27 — Visuals Default-On (SN-17).** The four binding decisions as epics +
  the Ollama/ComfyUI coexistence design task (per decision 4).
- **M28 — Governance Reconciliations (P7-GH-16 + P6-GH-14 + P6-GH-15).** Bundled:
  all three are small doc/CLI contradiction fixes surfaced by real adoption.

HQ owns the final milestone shape; only "AE-1 first" is binding.

---

## Carry-Over Open Items

1. **HQ still owes SN-17's roadmap registration** (SN-17 Next Action #1) — folding
   it into the P7 phase-spec authoring pass satisfies it.
2. **Cross-repo closure choreography** (from the ruling): the P7-AE-1 live-run
   transcript is also runner E3.2's evidence; it must be surfaced to the runner's
   P2-M3 Milestone Chat for acceptance, closing E3.2 → M3 → P2 in sequence. The
   phase spec should record this as an AE-1 exit obligation.
3. The CFO carries the 2026-07-11 ruling to local-agent-runner's HQ/Phase Chat to
   mark its Escalation Notice resolved (Layer-8 relay; may already be done by the
   time HQ reads this).

---

## Next Action

HQ Chat should:

1. Confirm the two [PROPOSED — confirm] items (spine phrasing, phase name) and the
   proposed milestone grouping with the CFO.
2. Draft the P7 phase spec with P7-AE-1 as milestone one and the ruling's execution
   sequence + design constraint embedded in the AE-1 milestone.
3. Register SN-17 in the roadmap and update the P7 entry from "candidate pool" to
   the scoped phase (one registry, per the P6 precedent).
4. Record the cross-repo E3.2 acceptance obligation as an AE-1 exit criterion.
5. Issue the P7 phase-execution chat starter.
