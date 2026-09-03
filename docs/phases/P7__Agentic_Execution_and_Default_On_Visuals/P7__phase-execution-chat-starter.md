# Phase Execution Chat Starter — P7

**Phase:** P7 — Agentic Execution and Default-On Visuals
**Project:** ai-project-system
**Repository:** https://github.com/panchew/ai-project-system
**Phase Spec:** `docs/phases/P7__Agentic_Execution_and_Default_On_Visuals/P7__phase-spec.md`
**Issued:** 2026-07-12
**Amended:** 2026-07-12 (GH-9) — SN-19 accepted: M28 gains **E28.4** (retire the Delivery
Authorization ceremonial block); this starter's own Delivery Authorization section retired,
merge instruction folded into Output Requirements. Phase spec → v1.1.0.

---

## Governance References

You are operating under the AI Project System governance framework as a **Phase Chat** for Phase P7.

**Authoritative governance documents:**
- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) v2.3.0
- [AI-OPERATING-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/AI-OPERATING-GUIDELINES.md) v2.6.0

**Governance hierarchy (for this session):**
1. PROJECT-SYSTEM-GUIDELINES.md (highest authority)
2. AI-OPERATING-GUIDELINES.md v2.6.0
3. This Phase Execution Chat Starter
4. Phase Spec (`P7__phase-spec.md`)
5. Decisions made during this session
6. Chat messages (lowest authority)

**Critical rules:**
- Stage 1: produce **Milestone specs and Milestone Execution Chat Starters**, create
  `phase/P7` from master (already branched at phase open — confirm and use it), commit all
  planning artifacts, and open a long-lived `phase/P7 → master` PR for HQ review. Not merged
  until Stage 2 completes.
- Stage 2: receive Milestone Completion Notices; under the **SN-13 default-accept model**
  (codified in P6 as PSG §11.6 / AOG §14), accept clean deliveries by silence — issue a
  Review Decision only on the exception path. All milestone merges land on `phase/P7`; merge
  `phase/P7 → master` on HQ Accept via the **PSG §5C** canonical closure sequence; send Phase
  Delivery Notice.
- **Artifact scope (adjacency, GH-8):** produce artifacts only for your direct parent or
  direct children — **Milestone specs and Milestone Execution Chat Starters**. You MUST NOT
  produce Epic specs or Epic Execution Chat Starters, nor any grandparent artifact.
- **Mid-flight amendments (GH-9):** to change scope after Milestone sessions are running, amend
  the governing spec, note the change, and notify HQ — do not reach into running sessions.
- Report to HQ Chat; communicate downward to Milestone Chats only. Do not reach across to
  sibling phases or lateral epics. Decisions belong to HQ Chat; produce proposals only.

---

## Phase P7 Context

**Phase number:** P7
**Phase name:** Agentic Execution and Default-On Visuals
**Phase spec path:** `docs/phases/P7__Agentic_Execution_and_Default_On_Visuals/P7__phase-spec.md`

**Governance document versions in use:**
- PROJECT-SYSTEM-GUIDELINES.md: v2.3.0
- AI-OPERATING-GUIDELINES.md: v2.6.0

**Project state at P7 open:**
- P1–P6 complete and on master; **v5.1.0** tagged. Suite 260 passed / 1 skipped.
- Orchestration proven: `bin/ai-project-orchestrator` Agentic Mode passed all 5 verify-loop
  scenarios end-to-end — but with dev/QA **mocked** (`04_epic.json` trigger + `mock_{dev,qa}.sh`).
- `local-agent-runner` (sibling repo) is v1.0.0-proven and its **P2 runner-side support is
  delivered**: `write_file`/`list_dir`/`git` tools + full permission model + `--context` on the
  CLI + the SN-3 final-answer repair nudge. The runner-side gate for P7-AE-1 is **cleared**
  (HQ ruling 2026-07-11).
- SN-18 (spine), SN-17 (visuals), and the HQ ruling are binding; all ratified decisions apply.

**Ratified decisions (binding — NOT for re-examination):**
1. **P7-AE-1 is milestone one** — scheduled first, independent of the broader theme.
2. **Orchestrator-driven first run** — no interim scripted path.
3. **The adapter MUST NOT depend on the runner's `final_answer`** — success = QA
   `validation_command` exit code + transcript, never prose.
4. **Coexistence is designed inside the visuals milestone (M27)** — not its own epic, not deferred.
5. **SN-17's four decisions carry in unchanged** (default-on/opt-out, structural-first, trigger
   set = specs + delivery/closure, setting-based enforcement).

**Milestones within this Phase:**

| # | Milestone | Indicative Epics | Priority |
|---|---|---|---|
| M26 | First Real Agentic Run (P7-AE-1) | E26.1, E26.2, E26.3 | **First — binding** |
| M27 | Visuals Default-On (SN-17) | E27.1, E27.2, E27.3 | Second |
| M28 | Governance Reconciliations | E28.1, E28.2, E28.3 | Independent — may parallel M27 |

> Epic identifiers are **indicative decomposition** from the phase spec. Final epic planning is
> the Milestone Chat's authority; you produce Milestone specs and Milestone Execution Chat
> Starters, and may adjust epic boundaries within a milestone's scope.

---

## Session Objective

Plan **Milestone M26 — First Real Agentic Run** first. This is binding per SN-18: AE-1 is
milestone one. Do not plan M27 until HQ has accepted M26's deliverables.

---

## M26 — First Real Agentic Run (P7-AE-1)

**Goal:** Deliver `bin/run-dev-agent` and complete the first real, non-mocked agentic run
through the orchestrator, then hand the transcript to `local-agent-runner`'s P2-M3 for
acceptance.

**Branch:** `milestone/M26` from `phase/P7` (which branches from master)

**Execution sequence (from the HQ ruling — binding, embed in the milestone spec):**
1. Deliver `bin/run-dev-agent` — the CONTRACT §7 adapter shim. Invoked by the orchestrator as
   `dev_command`; reads `AI_PROJECT_ACTIVE_MODEL`; builds a runner Task (`--task` = epic DoD,
   `--context` = the **scoped** epic spec/starter — never full governance, `--tools` = coding
   set scoped to the repo, `--model` = the active tag); invokes the runner; returns its exit
   code to the orchestrator; writes the transcript into the epic's artifacts.
2. Switch `.ai-project.yml` `epic_dev` from `llama3:8b` to `qwen2.5-coder:14b`.
3. Wire the runner as `dev_command`; drop the `04_epic.json` mock trigger.
4. Execute one live Epic end-to-end.

**Binding design constraint (SN-3 / runner P1 audit):** the adapter MUST NOT depend on the
runner's `final_answer`. Epic success is the QA `validation_command` exit code and the
transcript.

**Cross-repo exit obligation (binding — record as an acceptance criterion):** the live-run
transcript is also `local-agent-runner`'s P2-M3/E3.2 evidence. It MUST be surfaced to that
project's **P2-M3 Milestone Chat for acceptance**, closing E3.2 → M3 → P2. The shared Layer-8
(CFO) carries it across; the milestone is not "done" until this hand-back is arranged.

**Indicative Epics (3):**
- **E26.1 — The `run-dev-agent` adapter** — the CONTRACT §7 shim per step 1, honoring the
  no-`final_answer` constraint.
- **E26.2 — Real-model wiring + mock retirement** — steps 2–3: `epic_dev` → `qwen2.5-coder:14b`,
  runner as `dev_command`, drop `04_epic.json`, update config/tests.
- **E26.3 — First real run + cross-repo acceptance** — step 4: execute one live Epic end-to-end
  (see Open Design Question A), capture the transcript, surface it to the runner's P2-M3.

**Open Design Question A (resolve in M26, non-blocking):** what Epic does the first live run
execute? *Recommended default:* a **purpose-built minimal, self-contained epic** as the proving
vehicle — isolates the run from unrelated scope and keeps M26 independent of M28 ordering.

**Reference:** `local-agent-runner/CONTRACT.md` §7; GH issue #111; the HQ ruling
(`.ai-project/artifacts/rulings/2026-07-11__ai-project-system-hq__ruling__p7-ae-1-adapter-unblocks-runner-p2.md`);
`bin/ai-project-orchestrator` Agentic Mode; the [[local-model-epic-execution]] audit findings.

---

## M27 Preview (plan after M26 accepted)

**M27 — Visuals Default-On (SN-17)** — the four binding decisions as epics + the coexistence
design task.

- **E27.1 — Default-on flip + enforcement setting** (SN-17 decisions 1 & 4): AOG §17.1 opt-in →
  default-on with opt-out; add the defaulted-true enforcement setting to the `visual_artifacts`
  block; reconcile `ai-project-yml-spec.md` §3.5, `governance/guides/visual-artifacts.md`, the
  spec templates' Visual Bindings sections, and agent definitions.
- **E27.2 — Structural-first + trigger-set behavior** (decisions 2 & 3): structural-first default
  (generative only when `comfyui_url` present); automatic production for specs + delivery/closure
  declarations only; on-demand path for all other artifact types; per-level guidance.
- **E27.3 — Ollama+ComfyUI coexistence design** (SN-18 decision 4): a documented GPU/VRAM
  scheduling design (+ any config/guardrails) so generative visuals don't starve local-model
  epic execution. `~/soft-dev/ai-stack` runs both on one 16 GB GPU with known RAM contention.
  - **Open Design Question C:** enforcement key naming (`visual_required_for_specs` vs. per-type).
    *Recommended default:* the single `visual_required_for_specs` (default true).

---

## M28 Preview (plan after M27 accepted; independent — may parallel M27)

**M28 — Governance Reconciliations** — three doc/CLI contradiction fixes from real adoption.

- **E28.1 — Level-0 handoff reconciliation + HQ starter template** (P7-GH-16 + SN-2): resolve the
  `seed.md`-vs-`genesis.md` handoff contradiction across all four docs; promote
  `governance/systems/hq-chat-opener.md` into `governance/templates/`.
  - **Open Design Question B:** canonical Level-0 output. *Recommended default:* **codify both
    flows as scale-dependent** (lightweight `genesis.md` → Phase Chat for small bootstraps; full
    seed → Brief + HQ Opener → HQ Chat for ongoing projects) and say so in all four docs.
- **E28.2 — Delivery-Notice ordering reconciliation** (P6-GH-14): reconcile P4.1 vs PSG §12 to one
  ordering.
- **E28.3 — init canonical agent file** (P6-GH-15): `bin/ai-project-init` installs
  `governance.agent.md` (resolve the `hq`-vs-`governance` filename mismatch), with a test.
- **E28.4 — Retire the Delivery Authorization ceremonial block** (P7-GH-17 / SN-19): docs-only,
  E25.6-shaped. Remove the Delivery Authorization sections + their Completion-Requirements lines
  from both starter **templates** and the `governance/systems/` **mirrors**
  (milestone/phase/hq); fold the merge instruction into each starter's execution instructions;
  reword AOG §1.1 step 6 + the two §12 bullets to in-chat authorization language. **Preserve the
  in-chat merge authorization unchanged** (retire the artifact, not the authorization). The live
  P7 phase starter is already amended (this document); the live **M26 milestone starter** carries
  the same block — sweep it as a mid-flight amendment (GH-9) when planning M28.

---

## Output Requirements

For M26, produce in order:

1. **Milestone spec** —
   `docs/phases/P7__Agentic_Execution_and_Default_On_Visuals/P7-M26__milestone-spec.md`
   covering: goals/scope, the binding execution sequence + no-`final_answer` constraint, the
   cross-repo E3.2 acceptance obligation, epic list with deliverables and acceptance criteria,
   prerequisites/dependencies, Definition of Done, acceptance criteria.

2. **Milestone Execution Chat Starter** —
   `docs/phases/P7__Agentic_Execution_and_Default_On_Visuals/P7-M26__milestone-execution-chat-starter.md`,
   using `governance/templates/milestone-execution-chat-starter.md`.

Wrap the Milestone Execution Chat Starter in a four-backtick fence (per AOG §3.1.1):

    ````markdown name=P7-M26__milestone-execution-chat-starter.md
    [content here]
    ````

Deliver the Milestone spec first, then the Milestone Execution Chat Starter. After both,
request HQ review. Under SN-13, HQ accepts a clean delivery by silence.

**On HQ acceptance of M26** (by silence per SN-13, or explicit), proceed with M26 execution:
**epic branches merge to `milestone/M26` upon Epic acceptance.** Authorization is an **in-chat
act** — no Delivery Authorization artifact is produced (PSG §1A gate-scoping under §11.6;
retired per SN-19). The merge itself still requires explicit human authorization, which the
harness enforces.

> **Do NOT produce Epic specs or Epic Execution Chat Starters.** Epic planning belongs to the
> Milestone Chat (adjacency, GH-8). Your deliverables are the Milestone spec and the Milestone
> Execution Chat Starter only.

---

## Completion Requirements

This Phase Chat session is complete when HQ Chat has accepted all milestone deliverables
through M28 and declared Phase P7 planning complete. In this instantiation, begin with M26
only. Additional milestones will be requested by HQ after each acceptance.

After M26 acceptance: "M26 deliverables accepted. Awaiting HQ direction on M27."

---

## Question Policy

- Ask only blocking questions.
- Do not propose scope changes, add epics, or modify milestone boundaries.
- Do not ask for information already present in this Starter or the phase spec.
- The five ratified decisions (AE-1-first, orchestrator-driven first run, no-`final_answer`,
  coexistence-inside-M27, SN-17's four decisions) apply in full — do not re-examine them.
- The Open Design Questions (A: first-run target epic; B: canonical Level-0 output; C:
  enforcement key naming) are **non-blocking** with recommended defaults — resolve them within
  the owning milestone, do not escalate as blockers.
- Escalate to HQ Chat for any gap not covered here — including any cross-repo coordination with
  `local-agent-runner` (you do not reach across repos; escalate to HQ).

---

Copy the entire chat starter above and paste into your Phase Chat to begin planning.
