---
type: escalation-notice
milestone: M37
issued_by: Milestone Chat (P11-M37)
issued_to: Phase Chat (P11)
date: 2026-08-05
status: open
routed_to: HQ Chat (ai-project-system)
routed_on: 2026-08-05
routed_by: Phase Chat (P11)
phase_chat_disposition: "Verified in full. Route A declined; landing order NOT reversed (E37.2 proceeds now, merge order unchanged); both E37.1 artifacts confirmed needing no rework. Escalated: Route C for E37.1 with the local-lane comparison moved to M38 (E37.1 agentic has an unrecognized M38 dependency — Route B.2 would invest in the engine A1.2 may retire). Separately recommended: Route B.1 alone as a B-series bugfix."
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

**Phase Chat (P11), 2026-08-05. Partly resolved here; the route decision escalated to HQ with a
recommendation that differs from all three options as written.**

### Verification — every claim re-measured, not forwarded

| Claim | Phase Chat verification |
|---|---|
| Sandbox cannot reach `http://localhost:11434` | ✅ **HTTP 000** |
| Sandbox *can* reach `http://172.17.0.1:11434` | ✅ **HTTP 200** |
| `local-agent-runner` absent from the image | ✅ `ABSENT`; **no reference in `Dockerfile.sandbox`** |
| `run_in_sandbox()` forwards only `AI_PROJECT_ACTIVE_MODEL` + the mount | ✅ confirmed at `bin/ai-project-orchestrator:292` — no network config, no `AI_PROJECT_OLLAMA_ENDPOINT`, no `LOCAL_AGENT_RUNNER` |
| `check_local_availability()` precedes `discover_runner()` → class 5 first | ✅ lines **221** and **252** |
| E26.3 prior art, 2026-07-12, per-epic workaround | ✅ verbatim at lines **425–431** |

**The escalation is correct in every particular.** E37.1 as specified cannot be dispatched, and the
finding is prior art three weeks old that was worked around once and never closed. **Escalating rather
than working around it a second time was the right call**, and re-measuring instead of inheriting the
spec's verification is what found it.

### A Phase Chat error this exposes, corrected rather than absorbed

Milestone spec v1.1.0 §Execution Posture states *"Dispatch mechanics — **verified on this host**"* and
*"**No configuration change is required**."* **Both sentences are true and together they are
misleading.** I verified the three preconditions **at the host layer** and `bin/run-dev-agent` executes
**inside the sandbox**. The verification was real, correctly reported, and **performed at the wrong
layer** — so it certified nothing about the environment the code actually runs in.

**Corrected in milestone spec v1.1.2, with the original claim left visible.** This is the **third**
time in P11 that a verification has been performed at a plausible-but-wrong level: the phase spec's
Ollama context note (v1.0.0, HQ's), constraint 2a's xfail mechanism (the starter's), and now this one
(mine). **The pattern is worth more than the three fixes** — *"verify, do not inherit"* is satisfied by
measuring something, and says nothing about whether you measured the right thing.

### The strategic problem none of the three routes accounts for

**Route B.2 would install `local-agent-runner` into the sandbox image — the engine P11 has already
decided against.**

- **SN-27 Amendment A1.1:** the execution roster is **one tool, OpenCode**, covering local and cloud.
- **A1.2:** `local-agent-runner`'s retention is a **directed assessment with a real possibility of
  retirement**, and that assessment is **M38/E38.4** — *after* M37 in binding order.
- **Verified now: OpenCode 1.18.10 is already installed on this host** (`/home/panchew/.opencode/bin/opencode`).
- **`bin/run-dev-agent`'s `discover_runner()` hard-codes `local-agent-runner`** (line 203) as the only
  binary it will find, via `LOCAL_AGENT_RUNNER` or `PATH`.

So the dispatch chain is pinned to the engine the phase is considering retiring, and teaching it to use
OpenCode instead **is M38/E38.2's execution adapter surface** — the milestone that binding order places
*after* this one.

> **The finding, larger than the blocker:** **E37.1's agentic/local posture has an unrecognized
> dependency on M38.** It cannot be executed as specified without either building throwaway scaffolding
> around a possibly-retired engine, or pulling M38's adapter surface forward into M37 — which would
> breach both the fixed-contents fence and the binding milestone order.

### Decisions taken here (Phase Chat authority)

**1. The landing order is NOT reversed, and M37 is NOT blocked in full.** The Milestone Chat framed
this as a landing-order question; **the contention is on merge order only.** This spec's §Dependencies
already says the two epics *"may run in parallel"* and that *"whichever epic lands second owns
reconciling the changelog."*

**So: E37.2 proceeds to planning and execution immediately, and merge order stays E37.1 first.** That
recovers the milestone's throughput without paying the cost the reversal would incur — and that cost is
real: if E37.2 merged first, `creation-chat-guide.md` would gain a **second** non-uniform seeding row,
and **G1's entire premise is that there is exactly one.** Reversing would double the flattening risk on
the very run G1 exists to protect. **The order and the posture are coupled, so reversing now would
pre-commit the risk profile before HQ has decided the posture.** The Milestone Chat was right not to do
it unilaterally.

**2. Route A is declined.** Unsandboxed execution gives an unsupervised local model unrestricted write
access to the working tree, on the epic that amends **ten governance documents**, with **G2 existing
precisely because the exit code will not reveal that it went wrong.** The Milestone Chat does not
recommend it; neither do I. E26.3's authorization was for one epic in a different risk class and is not
precedent for this one.

**3. Both E37.1 artifacts are confirmed as needing no rework for this.** The blocker is environmental,
not specificational, exactly as the escalation states.

### Escalated to HQ, with the Phase Chat's recommendation

**Route C for E37.1 now — and the local-lane comparison moves to M38, not away.** Not mine to decide:
the CFO chose the split posture, so unwinding it is the CFO's call.

**Why this is preserving the CFO's intent rather than discarding it.** The decision's purpose was an
early, low-risk local data point with a cheap ground truth. Getting it here now costs: scaffolding for
an engine under retirement assessment, an unsandboxed run on ten governance documents, or M38 work
pulled forward. **In M38 the same comparison is native** — the adapter surface exists by then, OpenCode
is the engine, and the run is code-shaped work that the phase spec always reserved as the local lane's
real test. The evidence arrives one milestone later and **better**, against the engine that will still
be there.

**Separately, and recommended for authorization now: Route B.1 as a B-series bugfix.**

The endpoint gap is **engine-agnostic, mechanical, and blocks every future agentic/local epic through
the sandbox — including M38's.** Either forward `AI_PROJECT_OLLAMA_ENDPOINT` / add `--network host` in
`run_in_sandbox()`, or document the `dev_command` prefix. **It edits no governance document**, which is
precisely the boundary HQ drew on 2026-08-01 (Decision 5) and held on 2026-08-04 (Decision 3) and
2026-08-05 (Decision 5) — and unlike P10-GH-8, where HQ noted *"nothing here is urgent"* and *"the
escalation says twice nothing is blocked,"* **here something is demonstrably blocked.** Both of HQ's
stated reasons for declining the B-series vehicle are absent.

**B.2 is explicitly NOT recommended** — it is the part that invests in the possibly-retired engine, and
it should wait for M38's adapter surface to make it unnecessary.

**Placement is HQ's**, per SN-28: the hotfix classification is *"HQ's to authorize and execute or
delegate."* A Phase Chat does not open B-series bugfixes.

### Impact of this resolution

- **M37 is not blocked in full.** E37.2 proceeds now; merge order unchanged.
- **E37.1 waits on one HQ decision**, not on enabling work being scoped.
- **Nothing has been executed and no governance record is at risk**, as the escalation states.
- **The wider gap is escalated with an owner recommendation**, so it is closed once for P11 rather than
  worked around per-epic a second time — which was the escalation's own central point, and it is
  correct.
