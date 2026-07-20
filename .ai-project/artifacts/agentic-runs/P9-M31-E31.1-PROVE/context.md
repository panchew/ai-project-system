<!-- scoped context: docs/phases/P9__Context_Handling_and_Token_Efficiency/P9-M31-E31.1-PROVE__spec__agentic-dispatch-demo.md -->
---
project: ai-project-system
phase: P9
milestone: M31
epic: E31.1-PROVE
type: spec
status: proving-vehicle
last_updated: 2026-07-19
---

# P9-M31-E31.1-PROVE — Agentic-dispatch demonstration (proving vehicle, not a real epic)

**Not a scoped deliverable epic.** This is a minimal proving vehicle, in the tradition of
`P7-M26-E26.3-PROVE`, whose sole purpose is to be dispatched for real through
`bin/ai-project-orchestrator`'s existing, unmodified Dev-QA loop so that E31.1's
"both-modes demonstration evidence" deliverable is a real, non-mocked run rather than a
described hypothetical (per the Epic spec's Execution Notes and Technical Constraints).

Its own Epic Execution Chat Starter
(`P9-M31-E31.1-PROVE__epic-execution-chat-starter.md`) carries `Execution Mode: agentic`
— the concrete instance this run demonstrates.

## Definition of Done

- [ ] Create a file at
      `docs/phases/P9__Context_Handling_and_Token_Efficiency/P9-M31-E31.1-PROVE__output.md`
      whose content is exactly one line: `agentic-dispatch-demo-E31.1: mode model verified`


<!-- scoped context: docs/phases/P9__Context_Handling_and_Token_Efficiency/P9-M31-E31.1-PROVE__epic-execution-chat-starter.md -->
# Epic Execution Chat Starter — E31.1-PROVE

**Epic:** E31.1-PROVE — Agentic-dispatch demonstration (proving vehicle, not a real epic)
**Phase:** P9 — Context Handling and Token Efficiency
**Milestone:** M31 — Dual-Mode Working Levels & Model Guardrail
**Repository:** panchew/ai-project-system
**Branch Strategy:** `epic/P9-M31-E31.1` (committed alongside E31.1 itself — this proving
vehicle is not a separate branch/PR)
**Execution Mode:** agentic — this instance is declared agentic per
`governance/systems/chat-hierarchy.md`'s "Execution Mode" section (P9-M31-E31.1); it is
dispatched, unattended, via `bin/ai-project-orchestrator` → `bin/run-dev-agent` against
`local:qwen2.5-coder:14b` (dev) / `local:qwen2.5-coder:7b` (QA), exactly as recorded there.

---

> **Provenance:** authored by the Epic Chat executing P9-M31-E31.1, solely to produce real
> (not simulated) agentic-side demonstration evidence for that Epic's Deliverable 4 — in
> the tradition of `P7-M26-E26.3-PROVE`. This is not a scoped deliverable epic and has no
> Definition of Done beyond its own proving-vehicle spec
> (`P9-M31-E31.1-PROVE__spec__agentic-dispatch-demo.md`).

## What this instance demonstrates

Per the mode model recorded in `governance/systems/chat-hierarchy.md` ("Execution Mode:
Manual vs. Agentic"), a reader determines any instance's Execution Mode from its own
starter's `Execution Mode` field. This starter declares `agentic` — the run dispatched
from this declaration is recorded in
`docs/phases/P9__Context_Handling_and_Token_Efficiency/P9-M31-E31.1__demonstration-evidence.md`,
alongside the real run artifacts committed at
`.ai-project/artifacts/agentic-runs/P9-M31-E31.1-PROVE/`.

## Begin Execution

Dispatch via `bin/ai-project-orchestrator` against the trigger naming
`epic_spec_path: docs/phases/P9__Context_Handling_and_Token_Efficiency/P9-M31-E31.1-PROVE__spec__agentic-dispatch-demo.md`.
No human-chat execution occurs for this instance — its Execution Mode is agentic, per the
declaration above.
