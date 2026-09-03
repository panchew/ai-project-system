---
milestone: M26
name: First Real Agentic Run
phase: P7
status: planned
start_date: 2026-07-12
epics:
  - E26.1
  - E26.2
  - E26.3
is_final: false
---

# Milestone M26 — First Real Agentic Run (P7-AE-1)

## Purpose

Deliver `bin/run-dev-agent` and complete the **first real, non-mocked agentic run**: a live
Epic executing through the P3 orchestrator with `local-agent-runner` wired in as `dev_command`
on a local model, then hand the run's transcript to `local-agent-runner`'s P2-M3 Milestone Chat
for acceptance — closing that project's stalled E3.2 → M3 → P2 chain.

Both halves are proven and waiting for the adapter:

- `bin/ai-project-orchestrator` **Agentic Mode** passed all 5 verify-loop scenarios end-to-end —
  but with dev/QA **mocked** (`04_epic.json` trigger + `tests/mocks/mock_{dev,qa}.sh`).
- `local-agent-runner` (sibling repo, `~/soft-dev/local-agent-runner`) is **v1.0.0-proven**
  (155 tests) and its P2 runner-side support is **delivered**: `write_file`/`list_dir`/`git`
  tools + full permission model + `--context` on the CLI + the SN-3 final-answer repair nudge.
  The runner-side gate is **cleared** (HQ ruling 2026-07-11).

The adapter is the one remaining variable. M26 is **milestone one of P7** (binding, SN-18) and
is time-sensitive: a partner project's P2 closure is stalled on it.

---

## Binding Context (settled — NOT for re-examination)

1. **P7-AE-1 is milestone one** (SN-18) — M26 runs first, before M27/M28.
2. **Orchestrator-driven first run** (HQ ruling) — no interim scripted path. The live run goes
   through `bin/ai-project-orchestrator` Agentic Mode, not a hand-rolled script.
3. **The adapter MUST NOT depend on the runner's `final_answer`** (SN-3 / runner P1 audit — it
   is systematically unreliable on Q&A-shaped tasks with `qwen2.5-coder:14b`). Epic success is
   the QA `validation_command` exit code and the transcript, never prose.
4. **Cross-repo exit obligation** (HQ ruling / SN-18): the live-run transcript is also
   `local-agent-runner`'s P2-M3/E3.2 evidence and MUST be surfaced to that project's P2-M3
   Milestone Chat for acceptance. This is an M26 exit criterion, not an optional follow-up.
   The shared Layer-8 (CFO) carries it across; cross-repo coordination is escalated to HQ —
   no chat in this repo reaches across.

**Execution sequence (from the HQ ruling — binding):**

1. Deliver `bin/run-dev-agent` — the CONTRACT §7 adapter shim (E26.1).
2. Switch `.ai-project.yml` `epic_dev` from `llama3:8b` (verified unusable — empty tool-call
   responses) to `qwen2.5-coder:14b` (E26.2).
3. Wire the runner as `dev_command`; drop the `04_epic.json` mock trigger (E26.2).
4. Execute one live Epic end-to-end (E26.3).

---

## Problem Statement

The orchestration layer and the execution engine are each proven in isolation, but the system
has **never executed one of its own epics for real**:

- The orchestrator's Agentic Mode loop (`handle_epic_execution`) already defaults
  `dev_command` to `./bin/run-dev-agent` (`bin/ai-project-orchestrator:317`) — **a file that
  does not exist**. Every proven run substituted mocks.
- `.ai-project.yml:26` still pins `epic_dev: local:llama3:8b`, a model verified unusable for
  tool-calling (empty tool-call responses).
- The runner is proven standalone but has never been invoked by the orchestrator; its P2
  cannot close without a real consumer run (E3.2 evidence).

---

## Goals

By the end of this milestone:

1. **The adapter exists.** `bin/run-dev-agent` implements CONTRACT §7: invoked by the
   orchestrator as `dev_command`; reads `AI_PROJECT_ACTIVE_MODEL`; builds a runner Task
   (`--task` = the epic's Definition of Done, `--context` = the **scoped** epic spec/starter —
   never full governance, `--tools` = the coding set scoped to the repo, `--model` = the active
   tag); invokes the runner; returns its exit code to the orchestrator; writes the transcript
   into the epic's artifacts (E26.1).
2. **The live path is real.** `epic_dev` is `qwen2.5-coder:14b`; the runner is the
   `dev_command`; the `04_epic.json` mock trigger is retired from the live path (E26.2).
3. **A live Epic completes non-mocked** through the orchestrator, with success determined by
   the QA `validation_command` exit code + transcript — never `final_answer` (E26.3).
4. **The cross-repo hand-back is arranged.** The transcript is surfaced (via HQ → CFO) to
   `local-agent-runner`'s P2-M3 Milestone Chat for acceptance (E26.3).

---

## Non-Goals

This milestone explicitly does **not**:

- **Rebuild or harden the runner.** `local-agent-runner` is a proven standalone engine; M26
  builds the **adapter** inside ai-project-system per CONTRACT §7 — not the engine. No CF-2
  (library entry point), no multi-model validation, no retry/backoff/concurrency/packaging.
- **Touch the visual layer or the governance reconciliations** — those are M27/M28.
- **Build an interim scripted path** — the first run is orchestrator-driven (binding).
- **Parse or depend on `final_answer`** anywhere in the adapter or acceptance logic (binding).
- Re-debate any ratified decision (AE-1-first, orchestrator-driven, no-`final_answer`).

---

## In Scope

- **E26.1** — `bin/run-dev-agent` (CONTRACT §7 shim) + its tests.
- **E26.2** — `.ai-project.yml` `epic_dev` switch, runner wired as the live `dev_command`,
  mock-trigger retirement from the live path, config/test updates.
- **E26.3** — the first live Epic run (including resolving Open Design Question A and
  authoring the proving-vehicle epic if the default is taken), transcript capture, and the
  cross-repo hand-back escalation.

## Out of Scope

- Runner engine changes (any file in `~/soft-dev/local-agent-runner` — cross-repo; escalate
  to HQ if a runner-side defect blocks the run); M27/M28 surfaces; ComfyUI/visuals; broad
  orchestrator refactors beyond what wiring the real `dev_command` requires.

---

## Planned Epics

### Confirmed Epics

- **E26.1 — The `run-dev-agent` adapter** (High)
- **E26.2 — Real-model wiring + mock retirement** (High, after E26.1)
- **E26.3 — First real run + cross-repo acceptance** (High, after E26.2)

> **Artifact scope (GH-8 adjacency):** the Phase Chat produces only this Milestone spec and the
> Milestone Execution Chat Starter. The **Milestone Chat** owns final epic planning and authors
> every Epic spec and Epic Execution Chat Starter. No Phase-level Epic drafts exist.

### Deferred Epics

- None.

---

## Epic Detail

### E26.1 — The `run-dev-agent` adapter (High)

**Source:** P7 phase spec P7.1 step 1; HQ ruling 2026-07-11; `local-agent-runner/CONTRACT.md`
§7; GH issue #111.

**Grounding (verified on `phase/P7`):**

- `bin/ai-project-orchestrator:317` — `dev_cmd = trigger.get("dev_command", "./bin/run-dev-agent")`.
  The orchestrator already names the adapter as its default `dev_command`; the file does not
  exist. The trigger also carries `epic_id`, `epic_spec_path`, `sandbox_env`, and
  `validation_command` (lines 313–317) — the adapter's inputs are reachable from the trigger
  plus the environment.
- `run_in_sandbox` (orchestrator ~line 270) executes the `dev_command` inside a Docker sandbox:
  `-e AI_PROJECT_ACTIVE_MODEL={active_model}`, repo mounted at `/workspace`, with a
  **local-execution fallback** (env-injected) when Docker is unavailable.
- `.ai-project.yml:26` model values carry a **`local:` prefix** (`local:llama3:8b`) — the
  adapter must map `AI_PROJECT_ACTIVE_MODEL=local:<tag>` to the bare ollama tag the runner's
  `--model` expects.
- Runner CLI (CONTRACT §2): `--model / --task / --tools / --context / --transcript`,
  exit codes `0` completed · `2` did-not-converge · `3` config/tool error · `4` runtime error.
  Tool permissions via `tools.json` (CONTRACT §4: `enabled`, `allow_paths`, `allow_commands`,
  `timeout`).

**Epic-level design points (the Epic resolves these within scope; escalate only if blocked):**

- **How the adapter locates the epic's DoD and scoped spec** — the trigger's `epic_spec_path`
  is the natural source; extraction of the DoD section vs. passing the whole (scoped) spec as
  `--context` is the adapter's call. **Never full governance** — the scoped spec/starter is the
  token-discipline lever (CONTRACT §6; the [[local-model-epic-execution]] audit: scoped ≈ 24K
  tok vs. full governance ≈ 157K tok).
- **Runner + endpoint reachability from the execution context** — the `dev_command` runs inside
  the Docker sandbox (or the local fallback). The runner binary must be invocable there, and the
  Ollama endpoint (`http://localhost:11434` default) must be reachable from wherever the
  adapter runs. How (sandbox image contents, `--endpoint` override, host networking, or relying
  on the documented local fallback) is an Epic design decision — document the choice in the
  adapter or its spec.
- **Transcript destination** — "into the epic's artifacts": exact path convention
  (e.g. under `.ai-project/artifacts/`) is the Epic's call; it must be git-visible and stable,
  because it is also the cross-repo E3.2 evidence (E26.3).

**Deliverables:**

1. `bin/run-dev-agent` — the CONTRACT §7 shim: reads `AI_PROJECT_ACTIVE_MODEL` (mapping the
   `local:` prefix), builds the Task (`--task` = epic DoD, `--context` = scoped spec/starter,
   `--tools` = coding set scoped to the repo, `--model` = active tag), invokes the runner,
   returns the runner's exit code to the orchestrator, writes the transcript into the epic's
   artifacts.
2. The `tools.json` coding-set definition scoped to the repo (per CONTRACT §4).
3. Tests covering the adapter's contract (model mapping, Task construction, exit-code
   passthrough, transcript write) — runner invocation may be stubbed in tests; the **live**
   invocation is E26.3's job.
4. **No `final_answer` parsing anywhere in the adapter** (binding).

**Definition of Done:**
- [ ] `bin/run-dev-agent` exists, is executable, and implements CONTRACT §7 as specified above
- [ ] `AI_PROJECT_ACTIVE_MODEL` (including the `local:` prefix form) drives `--model`
- [ ] `--context` receives scoped epic material only — never full governance
- [ ] The runner's exit code is returned unaltered to the orchestrator
- [ ] The transcript is written into the epic's artifacts
- [ ] The adapter contains no dependency on `final_answer`
- [ ] Tests cover the adapter contract; full test suite passes

**Acceptance Criteria:**
- [ ] The orchestrator can invoke `./bin/run-dev-agent` as `dev_command` without modification
      to the orchestrator's `handle_epic_execution` contract
- [ ] Adapter behavior matches CONTRACT §7 point-for-point; no `final_answer` dependency

---

### E26.2 — Real-model wiring + mock retirement (High)

**Source:** P7 phase spec P7.1 steps 2–3; HQ ruling execution sequence.

**Grounding (verified on `phase/P7`):**

- `.ai-project.yml:26` — `epic_dev: local:llama3:8b` (llama3:8b verified unusable: empty
  tool-call responses). `epic_qa: local:qwen2.5-coder:7b` is **not** in M26's directed scope.
- `bin/ai-project-orchestrator:21` — `DEFAULT_MODELS` also hardcodes
  `"epic_dev": "local:llama3:8b"`; whether the in-script default moves with the config is an
  Epic-level consistency call (recommended: yes, they should agree).
- The mock harness lives at `tests/mocks/mock_dev.sh` / `tests/mocks/mock_qa.sh` and is
  exercised by `tests/integration/test_agentic_mode.py`; the verify-loop scenarios drove
  `handle_epic_execution` via a `04_epic.json` trigger pointing at the mocks.

**Load-bearing nuance:** "drop the `04_epic.json` mock trigger" retires the **mock-driven
path as the live flow** — the trigger *mechanism* (`04_epic.json` in the queue) is how the
orchestrator receives epic work and is what E26.3 uses with real values. CI may retain the
mock scripts for regression coverage of the loop logic; the Epic decides and documents that
boundary. What must be true afterward: no live/documented flow routes an epic through
`mock_dev.sh`/`mock_qa.sh`, and `epic_dev` is off `llama3:8b`.

**Deliverables:**

1. `.ai-project.yml` `epic_dev` → `local:qwen2.5-coder:14b` (and the orchestrator
   `DEFAULT_MODELS` consistency call, decided and documented).
2. The runner (via `bin/run-dev-agent`) wired as the live `dev_command` — real trigger
   documentation/config updated so the live path names the adapter, not a mock.
3. Mock-trigger retirement from the live path, with the CI-retention boundary decided and
   documented; config/tests updated accordingly.

**Definition of Done:**
- [ ] `.ai-project.yml` `epic_dev` is `local:qwen2.5-coder:14b`
- [ ] The live epic-execution path invokes `bin/run-dev-agent` (no mock in the live flow)
- [ ] The `04_epic.json` mock trigger is retired from the live path; CI boundary documented
- [ ] Config and tests updated; full test suite passes

**Acceptance Criteria:**
- [ ] `epic_dev` is off `llama3:8b` everywhere it is defined
- [ ] No live or documented flow routes epic execution through the mock scripts

---

### E26.3 — First real run + cross-repo acceptance (High)

**Source:** P7 phase spec P7.1 step 4 + cross-repo exit obligation; HQ ruling; SN-18.

**Open Design Question A (resolve in this Epic — non-blocking, recommended default binding
unless the Milestone Chat records a reasoned alternative):** what Epic does the first live run
execute? *Recommended default:* a **purpose-built minimal, self-contained epic** as the proving
vehicle — it isolates the run from unrelated scope and keeps M26 independent of M28 ordering.
If the default is taken, the proving-vehicle epic must be genuinely minimal (small file-scoped
change + a real `validation_command` that can fail), authored within M26.

**Grounding:**

- Success semantics are already correct in the orchestrator: `handle_epic_execution` treats the
  QA `validation_command` exit code as the verdict (dev failures are warnings; validation
  passing ends the loop, commits, and clears the trigger). The run must be accepted on exactly
  those semantics — exit code + transcript, never `final_answer` (binding).
- The run is **orchestrator-driven** (binding): a real `04_epic.json`-mechanism trigger naming
  the target epic, its spec path, the real `validation_command`, and `./bin/run-dev-agent`.

**Deliverables:**

1. One live Epic executed end-to-end through `bin/ai-project-orchestrator` Agentic Mode on
   `qwen2.5-coder:14b`, non-mocked.
2. The run's transcript captured in the epic's artifacts (git-tracked), plus a short run record
   (what ran, trigger contents, validation outcome, iterations/tokens from the transcript).
3. **Cross-repo hand-back arranged:** the transcript surfaced to HQ with an explicit request
   that the CFO (shared Layer-8) carry it to `local-agent-runner`'s P2-M3 Milestone Chat for
   E3.2 acceptance. **M26 is not done until this hand-back is arranged** (arranged = escalated
   to HQ with the evidence attached; the acceptance itself happens in the other repo's chat).

**Definition of Done:**
- [ ] A live Epic completed through the orchestrator, non-mocked, on `qwen2.5-coder:14b`
- [ ] Success was determined by the QA `validation_command` exit code + transcript
- [ ] The transcript is git-tracked in the epic's artifacts
- [ ] The hand-back to `local-agent-runner` P2-M3 is escalated to HQ with the evidence
- [ ] Full test suite passes

**Acceptance Criteria:**
- [ ] A recorded live-run transcript shows a real Epic completing through the orchestrator on
      a local model, non-mocked
- [ ] Open Design Question A is resolved and recorded in the Epic spec
- [ ] The cross-repo hand-back request is on record with HQ

---

## Branch Strategy

```
master
└── phase/P7                    (phase open — HEAD 2bd76ff)
    └── milestone/M26            ← this milestone (Milestone Chat branches from phase/P7)
        ├── epic/P7-M26-E26.1    ← run-dev-agent adapter
        ├── epic/P7-M26-E26.2    ← real-model wiring + mock retirement
        └── epic/P7-M26-E26.3    ← first real run + cross-repo acceptance
```

Epic PRs target `milestone/M26`. Consolidation PR: `milestone/M26 → phase/P7`.
M26 is **not** the final P7 milestone (`is_final: false`) — M27 and M28 follow after HQ
accepts M26's deliverables.

---

## Prerequisites

- This Milestone spec and its Milestone Execution Chat Starter are git-tracked on `phase/P7`
  (verify with `git ls-files --error-unmatch <path>` — the GH-1 convention).
- M26 targets present and git-tracked on `phase/P7`:
  - `bin/ai-project-orchestrator` (Agentic Mode; `handle_epic_execution`, `run_in_sandbox`)
  - `.ai-project.yml` (the `models:` block)
  - `tests/mocks/mock_dev.sh`, `tests/mocks/mock_qa.sh`, `tests/integration/test_agentic_mode.py`
- **Cross-repo (read-only reference):** `~/soft-dev/local-agent-runner` at v1.0.0 with P2
  runner-side support delivered (CONTRACT §7 verified runner-side; `--context` on the CLI).
  The runner-side gate is cleared (HQ ruling 2026-07-11). Any runner-side change needed →
  escalate to HQ; do not reach across.
- **Host-side (CFO):** a reachable Ollama endpoint with `qwen2.5-coder:14b` pulled, for E26.3's
  live run. Not needed for E26.1/E26.2 development and tests.

---

## Dependencies and Sequencing

- **Strictly sequential:** E26.1 → E26.2 → E26.3. This is the HQ ruling's execution sequence
  (binding): the adapter must exist before the wiring switches to it, and the live run needs
  both. No parallelization within M26.
- E26.3 additionally depends on the host-side Ollama endpoint (above) and, for its hand-back,
  on HQ availability to relay cross-repo — neither blocks E26.1/E26.2.

---

## Definition of Done (Milestone)

- [ ] E26.1, E26.2, and E26.3 each meet their Definition of Done above
- [ ] All three epic branches merged to `milestone/M26`
- [ ] `bin/run-dev-agent` exists and implements CONTRACT §7 with no `final_answer` dependency
- [ ] `epic_dev` is `qwen2.5-coder:14b`; the mock trigger is retired from the live path
- [ ] A live Epic completed non-mocked through the orchestrator; transcript git-tracked
- [ ] The cross-repo hand-back to `local-agent-runner` P2-M3 is escalated to HQ with evidence
- [ ] Full test suite passes on `milestone/M26`
- [ ] Milestone Closure Declaration produced

---

## Acceptance Criteria (Milestone)

1. `bin/run-dev-agent` exists, is invoked by the orchestrator as `dev_command`, and passes
   scoped context (not full governance) to the runner (E26.1).
2. A recorded live-run transcript shows a real Epic completing through the orchestrator on a
   local model, non-mocked; success = QA `validation_command` exit code + transcript, never
   `final_answer` (E26.3).
3. The `04_epic.json` mock trigger is retired from the live path and `epic_dev` is off
   `llama3:8b` (E26.2).
4. The transcript hand-back to `local-agent-runner`'s P2-M3 Milestone Chat is arranged via HQ
   (E26.3) — the AE-1 exit criterion.

---

## Timeline

**Target Start:** 2026-07-12
**Target Completion:** 2026-07-20 (5–8 days per Phase spec estimate; 3 sequential epics)
**Actual Start:** Not started
**Actual Completion:** Not started

---

## Notes

- **Sequencing is binding, not advisory** — the HQ ruling fixes adapter → wiring → live run.
- **The no-`final_answer` constraint is architectural**, not stylistic: the adapter, the trigger,
  the run record, and the acceptance argument must all rest on the QA exit code + transcript.
- **The cross-repo hand-back is an exit criterion.** M26 closes that loop by *arranging* the
  hand-back (escalation to HQ with evidence); the acceptance itself is `local-agent-runner`
  P2-M3's decision in its own chat. No chat in this repo communicates with that repo directly.
- **Token discipline is a design requirement** (CONTRACT §6; the [[local-model-epic-execution]]
  audit): `--context` carries the scoped epic spec/starter only. Full-governance context
  (~157K tok) is a defect, not a convenience.
- **Sandbox reachability is the likely first real-world snag** (runner binary + Ollama endpoint
  from inside the Docker sandbox vs. the documented local fallback). It is an E26.1 design
  point with several valid answers — decide, document, and move; escalate only if genuinely
  blocked.
- Exact transcript path conventions, DoD-extraction mechanics, the `DEFAULT_MODELS` consistency
  call, and the CI-retention boundary for the mock scripts are **Epic-level design calls within
  M26's scope**; the milestone fixes the contract (CONTRACT §7 adapter; real model; no mocks in
  the live path; live run accepted on exit code + transcript; hand-back arranged), not the
  wording.
- Default-accept (PSG §11.6 / AOG §14) governs M26's own delivery: clean Epic/Milestone
  deliveries are auto-accepted by silence; Review Decisions are the exception path only.
