<!-- scoped context: docs/phases/P3__Library_Surface/P3-M4-E4.1__spec__public-run-api.md -->
---
project: local-agent-runner
phase: P3
milestone: M4
epic: E4.1
type: spec
status: in-execution
last_updated: 2026-07-20
proving_vehicle_for: ai-project-system P10-M33-E33.2 (first real Agentic/Local run)
carry_forward: CF-2 (P2 phase-closure — library entry point run(...) -> Result)
---

# Epic E4.1 — Public library entry point (`run` / `Result`)

## Context

This is the first slice of **CF-2** (P2 Phase-Closure carry-forward: "Library entry point
`run(...) -> Result` with pluggable custom tool handlers"). The `run()` function and the `Result`
dataclass already exist in `local_agent_runner/loop.py` and are used by the CLI, but the package's
public surface (`local_agent_runner/__init__.py`) exports **only** the `ollama_client` symbols. A
library consumer who wants to embed the runner must reach into the internal `loop` module. This Epic
promotes the existing loop-level entry point to the package's **public API** so
`from local_agent_runner import run, Result` works — the minimal, genuinely-useful first step of
CF-2. (Pluggable custom tool handlers — the second half of CF-2 — are a later slice, out of scope
here.)

This Epic is also the **real work vehicle** for ai-project-system's Epic P10-M33-E33.2 (the first
real Agentic/Local run on the proving pair). It is genuine local-agent-runner work that advances the
project; the run that executes it produces the runtime evidence E33.2 records.

## Problem Statement

`run` and `Result` are the library's natural entry point but are not exported from the package root,
so embedding the runner as a library requires importing from the private `loop` module. Promote them
(and the two terminal-status constants plus `ToolPermissions`) to the public API, without disturbing
the existing exports.

## Goals

1. `run`, `Result`, `ToolPermissions`, `STATUS_COMPLETED`, and `STATUS_MAX_ITERATIONS_EXCEEDED` are
   importable directly from `local_agent_runner`.
2. The existing `ollama_client` exports remain intact.
3. A test proves the public import path.

## Non-Goals

- No behavior change to `run()` or `Result` — this is an export/surface change only.
- No pluggable custom tool handlers (second CF-2 slice, deferred).
- No CLI change.

## Scope of Work

Edit `local_agent_runner/__init__.py` only, and add one new test file. Do not modify `loop.py`,
`tools.py`, `cli.py`, or any other module.

## Definition of Done

Complete every step below, then stop.

1. Edit the file `local_agent_runner/__init__.py`. Keep the existing imports from
   `local_agent_runner.ollama_client` and their entries in `__all__` exactly as they are. Then add
   these imports:
   - from `local_agent_runner.loop`: import `run`, `Result`, `STATUS_COMPLETED`, and
     `STATUS_MAX_ITERATIONS_EXCEEDED`
   - from `local_agent_runner.tools`: import `ToolPermissions`
2. In that same file, add these five names — `run`, `Result`, `ToolPermissions`, `STATUS_COMPLETED`,
   `STATUS_MAX_ITERATIONS_EXCEEDED` — to the `__all__` list, keeping the existing names in `__all__`.
3. Create a new file `tests/test_public_api.py` containing a test function that runs
   `from local_agent_runner import run, Result, ToolPermissions, STATUS_COMPLETED, STATUS_MAX_ITERATIONS_EXCEEDED`
   and then asserts that `run` is callable and that `Result` is a class (use `import inspect;
   assert inspect.isclass(Result)`). The test must also assert `STATUS_COMPLETED == "completed"`.
4. Run the command `pytest -q` from the repository root and confirm it reports all tests passing.

## Acceptance Criteria

- `from local_agent_runner import run, Result, ToolPermissions, STATUS_COMPLETED, STATUS_MAX_ITERATIONS_EXCEEDED` succeeds.
- The pre-existing `ollama_client` exports still import from `local_agent_runner`.
- `pytest -q` passes (new test included), no new failures.
