# GPU/VRAM Coexistence — Ollama + ComfyUI

Live agentic epic execution (Ollama inference, via `bin/run-dev-agent`/`local-agent-runner`) and
generative visual production (ComfyUI, via [`bin/ai-project-visual`](../../bin/ai-project-visual))
are both GPU-hungry workloads that can run on the same host. This guide names the confirmed
contention, states the framework's mitigation, and draws the line between what the framework
encodes and what remains the CFO's infrastructure responsibility.

| | |
|---|---|
| **Audience** | Adopters running Ollama + ComfyUI on shared GPU hardware; CFOs deciding infra-level partitioning |
| **Related** | [`visual-artifacts.md`](visual-artifacts.md) §3 (exit codes), [`../../bin/ai-project-visual`](../../bin/ai-project-visual), [`../../bin/ai-project-orchestrator`](../../bin/ai-project-orchestrator) (the execution lock), [`../../bin/ai-project-daemon`](../../bin/ai-project-daemon) (the lock-liveness check reused here) |

---

## 1. The confirmed contention

`~/soft-dev/ai-stack/docker-compose.yml` runs both services with no coordination:

```yaml
services:
  ollama:
    restart: unless-stopped
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
  comfyui:
    restart: unless-stopped
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
```

- **`count: all`** on both services makes the entire GPU visible to both containers — Docker does
  not sub-allocate VRAM between them.
- **No `deploy.resources.limits`**, no `NVIDIA_VISIBLE_DEVICES` restriction, and no MPS/MIG
  partitioning on either service.
- **Both services are `restart: unless-stopped`** — they come up together on host boot and stay up.
  The contention window is not something the CFO opts into per session; it exists by default
  whenever both happen to receive concurrent requests.

Left undesigned, a generative visual-production call could compete with a live agentic epic
execution for VRAM, risking an OOM or degraded inference on whichever workload loses the race —
exactly when the framework most needs both to be reliable (an Epic Chat's live run and a
Milestone/Phase Chat producing its default-on spec visual could, in principle, overlap).

---

## 2. The chosen approach: a software-side guardrail

The framework's mitigation is a narrow, in-repo guardrail — not an infrastructure change:

**`bin/ai-project-visual` checks whether a live agentic epic execution is in flight before issuing
a generative (ComfyUI) request, and refuses cleanly if so.**

A live execution is detected via `bin/ai-project-orchestrator`'s own execution lock
(`.ai-project/locks/execution.lock`) — the same PID file the orchestrator writes immediately before
`handle_epic_execution(...)` runs and removes once it returns. Its existence, with a live PID, is a
reliable signal that live Ollama inference is currently in flight, for the exact duration GPU
contention would matter.

**Reuse mechanism.** The orchestrator's own PID-liveness check
(`bin/ai-project-orchestrator:713-733`) is inline in its `main()` and has a deletion side effect
(stale-lock recovery) that belongs to the orchestrator's own startup, not to a read-only guardrail
elsewhere — and the orchestrator's execution-lock logic is out of scope to modify (Technical
Constraints, E27.3 spec). `bin/ai-project-daemon` already has exactly the read-only primitive
needed: `check_pid_alive(pid)` and `check_execution_locked()` (`bin/ai-project-daemon:93-106,
204-218`), factored out there for the daemon's own "defer queue processing while an epic is
running" behavior. Both files reuse identical `os.kill(pid, 0)` semantics (EPERM ⇒ alive, ESRCH ⇒
dead) — they are not divergent implementations, just two existing call sites.

The guardrail loads `bin/ai-project-daemon` the same way the helper already loads
`bin/ai-project-orchestrator` (`load_orchestrator()` / a new `load_daemon()`, both via
`SourceFileLoader`), then points the daemon module's `EXECUTION_LOCK` at the orchestrator module's
`LOCK_FILE` before calling `check_execution_locked()`. This one-line override
(`daemon.EXECUTION_LOCK = orch.LOCK_FILE`) matters: the orchestrator resolves its lock path from
the **current working directory** (the project actually being executed against), while the daemon
module resolves its own default from **its own file location** (correct for its default
self-referential deployment, but not guaranteed to coincide with the invoking project's cwd in a
vendored layout). Pointing the daemon's check at the orchestrator's own resolved path is what makes
this a true reuse rather than a check against a different — possibly wrong — file. No new
PID-liveness implementation is introduced anywhere.

**Stale-lock handling matches the orchestrator's own:** `check_execution_locked()` returns `False`
for a dead PID (via `check_pid_alive`'s `ESRCH` branch), exactly like the orchestrator's own
recovery path — a dead PID never blocks generation.

When locked, the helper exits with a new code (`5`) and a one-line stderr message naming the
contention. See [`visual-artifacts.md` §3](visual-artifacts.md#3-the-bin-ai-project-visual-helper)
for the full exit-code table.

---

## 3. What the framework encodes vs. what remains the CFO's responsibility

| | Owner |
|---|---|
| The execution-lock guardrail in `bin/ai-project-visual` (this design) | **Framework** — ships as code, covered by tests, no live GPU required |
| Reusing, not duplicating, PID-liveness detection | **Framework** |
| Standing up the GPU host, `~/soft-dev/ai-stack` itself, and any container orchestration | **CFO** |
| Infra-level partitioning (MPS/MIG, `deploy.resources.limits`, running the services on a schedule) | **CFO** — documented as options below, not implemented here |
| Deciding whether the guardrail alone is sufficient mitigation, or whether an infra change is also warranted | **CFO** |

The framework's guardrail is a **zero-infrastructure-change** mitigation: it requires no edit to
`~/soft-dev/ai-stack/docker-compose.yml` and works the instant this repo's code ships. It does not
eliminate GPU contention at the hardware level — it only prevents the framework's own generative
calls from firing *while it knows* a live epic execution is using the GPU. A generative call made
by any means outside `bin/ai-project-visual` (e.g. a human driving ComfyUI's own UI directly) is
outside the guardrail's reach, same as any workload the framework doesn't mediate.

### Infra-level options (CFO-owned, not implemented here)

If the guardrail alone proves insufficient in practice, these are the CFO's options — documented
for reference, not mandated or built by this Epic:

- **MPS (Multi-Process Service)** or **MIG (Multi-Instance GPU)** partitioning — sub-allocate the
  GPU so each service gets a bounded share instead of `count: all`.
- **`deploy.resources.limits`** — cap VRAM/compute per container (requires a partitioning-capable
  runtime; plain `count: all` reservations do not enforce limits).
- **Manual sequencing** — stop `restart: unless-stopped` on one service and start it on demand,
  trading availability for guaranteed non-overlap.

Any of these would require editing `~/soft-dev/ai-stack/docker-compose.yml`, a different repository
outside this repo's scope — a CFO decision and action, not a framework change.

---

## 4. Exit code reference

See the authoritative table in [`visual-artifacts.md` §3](visual-artifacts.md#3-the-bin-ai-project-visual-helper).
Code `5` ("execution locked") is this guide's guardrail; codes `0`/`2`/`3`/`4` predate it and are
unchanged.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-07-13 | Guide created. Documents the confirmed `count: all` + `restart: unless-stopped` + no-partitioning contention between Ollama and ComfyUI, the software-side execution-lock guardrail as primary mitigation (exit code `5`, reusing `bin/ai-project-daemon`'s `check_execution_locked()`/`check_pid_alive()` pointed at the orchestrator's own `LOCK_FILE`), and the framework-encodes-vs-CFO-owned split. Per SN-18; E27.3 (P7-M27). |
