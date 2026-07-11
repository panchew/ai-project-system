---
type: hq_ruling
escalation_ref: local-agent-runner/docs/phases/P2__First_Real_Run/P2__escalation-notice__m3-e3-2-sn-4-blocked.md
issued_by: HQ Chat (ai-project-system)
issued_to: HQ Chat / Phase Chat (P2 — First Real Run) [local-agent-runner]
cross_repo: true
date: 2026-07-11
status: active
blocking_resolved: true
---

# HQ Ruling — P7-AE-1 Adapter Owns the First Real Run; Runner P2 Hold Is Bounded

**Escalation:** local-agent-runner P2-M3 / E3.2 blocked on SN-4 (cross-repo adapter Epic)
**Relayed:** Milestone Chat (P2-M3) → Phase Chat (P2) → HQ Chat, 2026-07-11
**Answering authority:** ai-project-system HQ (the `bin/run-dev-agent` adapter is our work per
CONTRACT §7 / SN-4; only this side can commit its scheduling)

---

## Finding — the boundary held and the gate has cleared

SN-4's split is honored on both sides: the runner delivered **runner-side support only**, and
the adapter Epic stays inside ai-project-system's governance. As of today:

- Runner **P2-M2 is closed** — `write_file` / `list_dir` / `git` + full CONTRACT §4 permission
  model + the SN-3 final-answer repair nudge.
- Runner **P2-M3 / E3.1 is done and merged** — CONTRACT §7 runner-side verification, with
  `--context` now exposed on the CLI.

That is exactly the dependency P7-AE-1 was registered as "gated on." **The gate is cleared.**
P2-M3 / E3.2 ("First Real Run") and ai-project-system's **P7-AE-1** are the *same event seen
from two repos*: neither is blocked on the other technically — both are waiting on ai-project-
system scheduling the adapter Epic. This ruling removes that uncertainty.

---

## Decision 1 — Answers Q1 (hold P2 open? what unblocks P7 scoping? timeline?)

**ai-project-system commits to P7-AE-1 as a flagship, early P7 deliverable.** The runner's P2
holds open (E3.2 unplanned) until it lands — a **bounded** wait, not an indefinite one:

- **What unblocks P7 scoping:** only the Creation Chat setting the P7 spine (per governance, HQ
  does not self-scope a phase). That session **is already in progress with the CFO.** No
  external dependency remains — the runner-side work is done and the orchestrator side is proven
  (verify-loop 5/5, sandbox image built).
- **Commitment independent of the broader P7 theme:** whatever spine the Creation Chat picks,
  **P7-AE-1 is a committed high-priority milestone scheduled first**, because a partner project's
  phase closure is stalled on it and its inputs are all ready.
- **Sequence on execution:** deliver `bin/run-dev-agent` (adapter shim per CONTRACT §7) → switch
  `.ai-project.yml` `epic_dev` from `llama3:8b` to `qwen2.5-coder:14b` → wire the runner as
  `dev_command` and drop the `04_epic.json` mock trigger → execute one live Epic end-to-end.
- **Design constraint carried in (SN-3 / runner P1 audit):** the adapter MUST NOT depend on the
  runner's `final_answer`; epic success is the QA `validation_command` exit code and the
  transcript, never prose.

---

## Decision 2 — Answers Q2 (interim scripted run vs. orchestrator-driven path)

**No interim path. The first real run is the orchestrator-driven path.** CFO-ratified
(2026-07-11).

Rationale: we are a single adapter Epic away from the real thing, and the runner Brief's intent
is a live Epic carried *through the orchestrator* and **accepted in its parent Milestone Chat** —
a scripted bypass would prove strictly less, leave the Brief criterion unmet, and have to be
redone. Spending the effort on the adapter itself is the shorter path to a genuine acceptance.

---

## Coordination — how the run closes both sides

The single end-to-end execution of P7-AE-1 is also the runner's E3.2 evidence. To close cleanly:

1. ai-project-system executes P7-AE-1; the live-run transcript is written into the Epic's
   artifacts on this side.
2. That run is surfaced to the **runner's P2-M3 Milestone Chat** for acceptance (the Brief
   requires acceptance in the runner's parent Milestone Chat). On acceptance, runner E3.2 → M3 →
   P2 close in sequence.
3. The shared Layer-8 (CFO) carries this ruling back to the runner's HQ / Phase Chat, which marks
   its Escalation Notice `status: resolved`, citing this ruling.

---

## Open item flagged for P7 scoping (not resolved here)

The **runner + ComfyUI coexistence** question (SN-17 carry-over) is real infrastructure —
`~/soft-dev/ai-stack` runs both Ollama and ComfyUI on one 16 GB GPU with known RAM contention.
It is **not** a blocker for P7-AE-1 (the first run needs Ollama, not ComfyUI), but P7 scoping
must address GPU/VRAM scheduling between local-model epic execution and generative visuals, per
SN-17 Next Action #3.

---

## No Further Escalation Required

The cross-repo prioritization question is resolved: P7-AE-1 is committed and scheduled first in
P7; the runner's P2 hold is bounded by the in-progress Creation Chat spine session; the first run
is orchestrator-driven. The runner's Phase Chat may mark its escalation resolved on receipt.
