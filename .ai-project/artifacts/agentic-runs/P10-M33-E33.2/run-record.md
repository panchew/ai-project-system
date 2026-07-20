---
epic: P10-M33-E33.2
type: agentic-run-record
status: complete
date: 2026-07-20
target_repo: local-agent-runner
target_branch: epic/cf-2-public-run-api
target_commit: 4ec1e8f
target_base: 231a2cf (chore/framework-v7.0.0-bump, framework_version v7.0.0)
runtime: Ollama 0.30.0
dispatch: bin/run-dev-agent (governance adapter, CONTRACT §7) direct on host
---

# E33.2 Run Record — First real Agentic/Local epic on the pair

This is the governance run record for Epic P10-M33-E33.2 (framework repo, `epic/P10-M33-E33.2`).
The real code produced by the run lives in the **target repo** `local-agent-runner`
(`epic/cf-2-public-run-api`, commit `4ec1e8f`) — **not** merged onto `phase/P10` (Cross-Repo split).
A reader of *this* repo can verify the target outcome from the cited commit + the transcripts copied
alongside this file.

## 1. What was scoped (Manual/Paid framing)

- **Target project:** `local-agent-runner` (Design Decision 1). Chosen because it *is* the local
  inference substrate — running its own epic exercises the Ollama coding stack most directly — and
  it offered the cleanest small, self-contained, reviewable unit of genuine work.
- **Genuine unit:** the first slice of **CF-2** (its own P2 phase-closure carry-forward: "Library
  entry point `run(...) -> Result`"). `run()`/`Result` already existed in `local_agent_runner/loop.py`
  but were **not** exported from the package root. The scoped epic (local-agent-runner
  `P3-M4-E4.1`) promotes them (plus `ToolPermissions`, `STATUS_COMPLETED`,
  `STATUS_MAX_ITERATIONS_EXCEEDED`) to the public API, with a test. Real, pre-articulated,
  CFO-deferred work — not a synthetic demo (Hard Constraint).

## 2. Dispatch path (documented Epic-Agent decision)

Dispatched through the governance-aware adapter **`bin/run-dev-agent`** (CONTRACT §7 shim; carries
the E31.2 dispatch-time model guard and the run-record convention) **directly on the host**, as the
P7-M26-E26.3-PROVE precedent did — *not* wrapped in the orchestrator's Docker sandbox. Rationale:
the runtime evidence (the point of E33.2) is produced by the runner↔Ollama inference and is
identical either way; running the adapter directly keeps Docker/container-networking failure surface
out of the runtime signal for this first run. The M31 dual-mode routing (`epic_dev`/`epic_qa` =
`local:qwen2.5-coder:14b`) and the E31.2 guard (endpoint reachable + model pulled, else exit 5) were
honored — the guard passed (substrate confirmed up before dispatch; no local model assumed).

## 3. Hardware / substrate (loadability)

| | |
|---|---|
| CPU | AMD Ryzen 5 9600X, 6C/12T |
| RAM | 30 GiB total (~3.9 GiB free at run time) |
| GPU | NVIDIA RTX 5060 Ti, **16 GB VRAM** |
| Runtime | Ollama 0.30.0, `http://localhost:11434` |

Loaded-model footprint (from `/api/ps`): `qwen3-coder:30b` = **12.9 GB VRAM + 21.4 GB total** — a
30B/Q4_K_M already exceeds 16 GB VRAM and **partially offloads to system RAM**, yet loaded and ran.

## 4. The runs

Two runs of the **same** task (the spec's Definition of Done), same context, same tools.json, same
Ollama runtime — differing only in model. Run A is the configured `epic_dev`/`epic_qa` model; Run B
is a within-run comparative model trial (sanctioned by spec §Design Decision 2; **no `models:` edit**).

### Run A — `qwen2.5-coder:14b` (the configured model)
- **Exit 0, `status: completed`, `iterations: 0`, 223 tok, 18.3 s (~12.2 tok/s end-to-end).**
- **Produced zero real work.** The model emitted the three intended tool calls **inside a ```json
  markdown fence as prose**; the runner's parser saw no protocol tool call, so the message was
  treated as a *final answer* → false-positive "completed" with **0 tool rounds**. `__init__.py`
  unchanged; test never created.
- This is precisely the **SN-3 failure mode local-agent-runner itself documented** ("final-answer
  turn systematically unreliable on Q&A-shaped tasks with qwen2.5-coder:14b"). The SN-3 repair nudge
  did not fire — the final answer was plausible-looking (a JSON plan), not an obviously-unusable blob.
- Evidence: `transcript-A-qwen2.5-coder-14b.json`, `...__run-metadata.json`.

### Run B — `qwen3-coder:30b` (comparative trial, same Ollama runtime)
- **Exit 2, `status: max_iterations_exceeded`, `iterations: 10`, 829 tok, 88.6 s (~9.4 tok/s end-to-end).**
- **Produced correct, complete, green work.** 10 real tool rounds (3× read_file, 2× write_file, 1×
  edit_file, 3× run_command). Final code: `__init__.py` cleanly adds both imports and extends
  `__all__`; `tests/test_public_api.py` valid. `from local_agent_runner import run, Result` works;
  the package imports cleanly; **suite 210 passed / 1 skipped** (baseline 209/1 + the new test).
- **Why exit 2 despite good work:** it wasted **3 of 10 iterations** trying `pip install -e .`
  (denied by allow_commands, which only permits pytest) and then ran out of the iteration budget
  before a final green `pytest` — so it terminated `max_iterations_exceeded` even though the work was
  essentially done. A **false-negative exit code** (mirror image of Run A's false positive).
- Evidence: `transcript-B-qwen3-coder-30b.json`; committed at target `4ec1e8f`.

## 5. Target-repo outcome (the run advanced the project)

`local-agent-runner` `epic/cf-2-public-run-api` @ **`4ec1e8f`** (base `231a2cf`, v7.0.0): CF-2 slice
landed — public `run`/`Result`/`ToolPermissions`/status-constant API + `tests/test_public_api.py`,
**210 passed / 1 skipped**. Committed as-produced by Run B's model (minor warts noted in the runtime
decision under review burden). This is real work advancing the project, not a demo — Hard Constraint
satisfied.

## 6. Pointers
- Runtime decision (four-dimension): `docs/phases/P10__Fleet_Adoption_and_Local_Inference_Proving/P10-M33-E33.2__runtime-decision.md`
- Scoped target epic: `local-agent-runner:docs/phases/P3__Library_Surface/P3-M4-E4.1__spec__public-run-api.md`
- Transcripts + context handed to the runner: this directory.
