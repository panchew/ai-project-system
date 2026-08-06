---
type: escalation-notice
milestone: M37
issued_by: Milestone Chat (P11-M37)
issued_to: Phase Chat (P11)
date: 2026-08-05
status: open
---

# Escalation Notice: E37.1's agentic/local posture is not executable as specified (sandbox lacks both the ollama route and the runner)

## Trigger

**Out-of-scope finding + a spec claim contradicted by measurement.**

Milestone spec v1.1.0 §Execution Posture → *Dispatch mechanics — verified on this host, 2026-08-05*
states **"No configuration change is required"** and records three preconditions as verified. **All
three are host-level facts and all three hold. But `bin/run-dev-agent` executes inside the Docker
sandbox, not on the host, and two further preconditions fail there.**

**As configured today, E37.1 dispatched through `bin/ai-project-orchestrator` fails with exit class 5
before performing any work.** The CFO's split-posture decision is not in question; the enabling work
to execute it has not been scoped, and it is outside both this chat's authority (the M37 Starter
forbids this Milestone Chat from modifying infrastructure) and M37's Hard Constraint (documents only,
no mechanism).

## What Was Attempted

The Milestone Chat re-measured rather than inheriting the spec's verification, per the Starter's
*"Verify, do not inherit."*

**Confirmed holding (host level — the spec's three rows):**

| Precondition | Result |
|---|---|
| `.ai-project.yml` `models.epic_dev: local:qwen3-coder:30b` | present, no change needed |
| Ollama endpoint `http://localhost:11434` reachable from the host | reachable |
| `qwen3-coder:30b` pulled | present |
| Sandbox image `ai-project-sandbox:latest` | present, carries python3 3.11.12 and node |

**Confirmed failing (sandbox level — not covered by the spec's verification):**

| # | Precondition | Result | Evidence |
|---|---|---|---|
| 4 | Ollama reachable **from inside the sandbox** | **FAILS** | `docker run --rm ai-project-sandbox:latest` cannot reach `http://localhost:11434`. It *can* reach `http://172.17.0.1:11434` (the bridge gateway) |
| 5 | `local-agent-runner` on PATH **inside the sandbox** | **FAILS** | not present in the image; `Dockerfile.sandbox` contains no install step |

**Mechanism, traced in code:**

- `run_in_sandbox()` (`bin/ai-project-orchestrator:292`) passes only `AI_PROJECT_ACTIVE_MODEL` and the
  project mount. **It forwards no network configuration, no `AI_PROJECT_OLLAMA_ENDPOINT`, and no
  `LOCAL_AGENT_RUNNER`.**
- `main()` (`bin/run-dev-agent:217`) runs `check_local_availability()` **before** `discover_runner()`.
  So precondition 4 fails first with **exit class 5**; fixing only that surfaces precondition 5 as
  **exit 3**.
- The runner exists on this machine at `/home/panchew/soft-dev/local-agent-runner` — **outside the
  mounted project root**, therefore invisible to the container. A working built binary was found and
  verified runnable at `/home/panchew/soft-dev/Getawayinsured2023/.venv/bin/local-agent-runner`.

**This is prior art, not a new discovery.**
`docs/phases/P7__Agentic_Execution_and_Default_On_Visuals/P7-M26-E26.3__spec__first-real-run-and-cross-repo-acceptance.md:427`
records the same two failures on **2026-07-12** and authorizes a workaround for that Epic: force the
**local-execution fallback** by curating `PATH` so `docker` is absent, causing `run_in_sandbox()`'s own
`FileNotFoundError` handler to run the command on the host. **The gap has been known for three weeks
and was never closed** — it was worked around once, per-epic.

**Not attempted, deliberately:** no fix was applied. Both routes below modify infrastructure, which
this chat may not do.

## Decision Needed

**Choose the route, and assign the enabling work to an owner that is not this Milestone Chat.**

**Route A — local-execution fallback (the E26.3 precedent; no code change).** Curate `PATH` to omit
`docker`; `LOCAL_AGENT_RUNNER` and `AI_PROJECT_OLLAMA_ENDPOINT` propagate because the fallback path
does `os.environ.copy()`. Available today.

> **The cost, stated plainly: this is not sandboxed.** It gives an unsupervised local model
> unrestricted write access to the working tree, on the epic that amends **ten governance documents**
> — and **G2 exists precisely because the exit code will not tell us if that went wrong.** The
> Milestone Chat does not recommend it.

**Route B — close the gap (recommended).** Two independent parts:
1. **The endpoint** needs no code change: prefixing the trigger's `dev_command` with
   `AI_PROJECT_OLLAMA_ENDPOINT=http://172.17.0.1:11434` works, because `dev_command` is executed
   through `sh -c` inside the container. (A `--network host` change in `run_in_sandbox()` is the
   tidier variant and *is* a code change.)
2. **The runner** requires installing `local-agent-runner` into `Dockerfile.sandbox` and rebuilding via
   `bin/build-sandbox.sh`. **There is no trigger-level workaround** — the binary must exist inside the
   image.

**Route C — revert E37.1 to manual/paid.** Available, but it discards the controlled comparison the
CFO chose the split posture to obtain, and the Milestone Chat raises it only for completeness.

**A secondary decision, if the answer is not immediate:** the Milestone Chat's binding landing order
(E37.1 first, E37.2 second) makes a blocked E37.1 block **all of M37**. The order can be reversed so
E37.2 proceeds in parallel — at the cost recorded in E37.1's spec §Dependencies: `creation-chat-guide.md`
would then carry a second irregularity among ten deliberately-uniform rows. **The Milestone Chat does
not reverse it unilaterally.**

## Impact

- **E37.1 cannot be dispatched.** Any attempt exits class 5 having done nothing.
- **M37 is blocked in full**, via the landing order, unless that order is reversed.
- **E37.2 is unaffected in substance** — it is manual/paid and needs none of this.
- **Both E37.1 artifacts are complete and correct as written**; they need no rework for this. The
  blocker is environmental, not specificational.
- **Wider than M37:** the same two failures will block **every** agentic/local epic dispatched through
  the sandbox, including M38's code-shaped local-lane test. Closing this once serves P11 generally;
  working around it per-epic, as E26.3 did, does not.
- **No governance record is at risk.** Nothing has been executed, and the milestone's substance is
  fully recoverable via manual execution under Route C.

## Resolution

(empty — awaiting Phase Chat decision)
