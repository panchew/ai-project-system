---
type: hq_ruling
escalation_notice_ref: .ai-project/artifacts/escalation-notices/2026-08-05T00_00_00Z__P11-M37__escalation_notice.md
concern_id: E37.1 agentic/local posture non-executable; sandbox endpoint gap (E26.3 prior art)
issued_by: HQ Chat (ai-project-system)
issued_to: Layer-8/CFO (mandatory diff reviewer, PSG §11.6.1); the P11 Phase Chat; the P11-M37 Milestone Chat
phase: P11
date: 2026-08-06
status: active
blocking_resolved: true
---

# HQ Ruling — E37.1 reverts to manual/paid; the local comparison moves to M38; the sandbox endpoint gap is Bugfix B2.1

**Escalation:** Epic-level finding → M37 Milestone Chat → Phase Chat → HQ, verified at each hop.

---

## Verification — re-measured by HQ, at the layer that matters

Every claim independently reproduced, and one measurement added that the escalation implies but does
not state:

| Claim | HQ verification |
|---|---|
| Sandbox cannot reach `localhost:11434` | ✅ **HTTP 000** |
| Sandbox *can* reach `172.17.0.1:11434` | ✅ **HTTP 200** |
| `local-agent-runner` absent from the image | ✅ **ABSENT**; no install step in `Dockerfile.sandbox` |
| `run_in_sandbox()` forwards only `AI_PROJECT_ACTIVE_MODEL` | ✅ a single `-e`; no endpoint, no `LOCAL_AGENT_RUNNER`, no network config |
| `check_local_availability` (221) precedes `discover_runner` (252) | ✅ — class 5 fires first |
| `discover_runner()` hard-codes `local-agent-runner` | ✅ `bin/run-dev-agent:203`, via `shutil.which` |
| E26.3 prior art, 2026-07-12 | ✅ verbatim — *"cannot reach the real Ollama endpoint or the runner binary… forwards no network config or `LOCAL_AGENT_RUNNER`/`AI_PROJECT_OLLAMA_ENDPOINT`"* |
| **NEW — with the endpoint fixed, is the runner then found?** | ❌ **STILL ABSENT** |

**That last line decides the ruling.** Route B.1 fixes the endpoint; it does **not** make E37.1
dispatchable, because `discover_runner()` looks for a binary the image does not contain. E37.1's
agentic/local posture therefore needs **either** B.2 — installing an engine under directed retirement
assessment — **or** M38/E38.2's adapter surface, pulled forward across a binding order.

**The Milestone Chat's finding that E37.1 carries an unrecognized dependency on M38 is upheld, and it
is stronger than stated: the dependency is not optional under any route that keeps the posture.**

---

## Decision 1 — Route A stays declined. Affirmed, not re-decided.

Unsandboxed write access for an unsupervised local model across ten governance documents, with **G2
existing precisely because the exit code will not reveal failure** (P10-GH-7, measured two-sided).
The Phase Chat's reasoning is correct and E26.3's authorization — one epic, different risk class — is
correctly refused as precedent.

## Decision 2 — Route C: E37.1 reverts to **manual / paid frontier**

E37.1 as specified cannot be dispatched. Reverting the posture is the only route that neither
invests in a possibly-retired engine nor breaches the binding order.

**The posture split was the CFO's decision, and this ruling does not overrule it — it records that
the premise it rested on is false.** The split was chosen on the understanding that dispatch worked;
it does not, and has not since 2026-07-12. **Decision 3 preserves the intent rather than discarding
it.** The CFO may override this ruling on either point.

**E37.1's two artifacts need no rework** — the blocker is environmental, as the escalation says.

## Decision 3 — The local/paid controlled comparison **moves to M38**. Not dropped.

The CFO's goal was an early, low-risk local data point with cheap ground truth. In M37 that costs
scaffolding around an engine under retirement assessment, or an unsandboxed run on ten governance
documents, or M38 work pulled forward. **In M38 the same comparison is native**: the adapter surface
exists (E38.2), OpenCode is the engine (A1.1), and the work is code-shaped.

**This also restores HQ's own advice rather than departing from it.** On 2026-08-05 HQ recommended
running M36 manual/paid because its epics were dense-prose governance amendments — *"save the local
lane for M37's code-shaped epics."* **The restructure moved the code-shaped work to M38.** M37 is now
prose work of exactly the shape the B3.1 engine comparison measured `qwen3-coder:30b` at its weakest
on. The phase spec's *"M37's code-shaped epics test the local lane"* is stale twice over, as the
Phase Chat noted; this ruling fixes it in the spec.

## Decision 4 — The sandbox endpoint gap is authorized as **Bugfix B2.1** (High)

Route B.1 alone, engine-agnostic: forward the Ollama endpoint (and the runner override) into the
sandbox so `run_in_sandbox()` stops severing the container from the host it must reach.

**This is consistent with HQ's B-series boundary, not an exception to it — and saying so matters,
because the boundary is only worth having if it can also say yes.** The 2026-08-04 refusal for
P10-GH-8 rested on two limbs, and the escalation is right that **both are absent here**:

| 2026-08-04 limb | Here |
|---|---|
| *"it would edit ten governance documents"* | **Edits none.** `bin/ai-project-orchestrator`, and `Dockerfile.sandbox` if needed — infrastructure, not the normative corpus. |
| *"nothing here is urgent… the escalation says twice nothing is blocked"* | **E37.1 is blocked now**, and every future agentic/local epic dispatched through the sandbox is blocked — including M38's and M39's. |

**Severity High → `B2.1`.** The documented workaround (E26.3's local-execution fallback, omitting
`docker` from `PATH`) is not equivalent: it works by **discarding sandbox isolation**, trading away a
safety property to obtain the capability. A workaround that removes a guarantee does not reduce
severity.

**Post-mortem required** (High severity, `docs/bugfixes/README.md`) — and it is the genuinely
valuable part here, so it is scoped rather than ceremonial: **the finding is not the missing `-e`
flag. It is that a gap documented in E26.3 on 2026-07-12 was worked around per-epic for three weeks
rather than filed.** The post-mortem addresses that and may follow the fix rather than block it.

**Delegated to an Epic-mode Coding Agent. HQ authorizes and does not execute.** The B3.1 authorship
exception was granted for a specific reason on a specific day; it is not a standing practice and HQ
will not repeat it absent its own explicit authorization.

## Decision 5 — Route B.2 declined, with a revisit trigger

Installing `local-agent-runner` into the sandbox image invests in the engine under **directed
retirement assessment** (A1.2, at M38/E38.4), and M38/E38.2's adapter surface should make it
unnecessary. **Trigger for revisit: if E38.4's assessment retains the runner and the adapter surface
does not cover sandboxed dispatch.** Declined now, not forever.

## Decision 6 — The "split M37" permission is SPENT. Confirmed.

The 2026-08-05 ruling recommended splitting M37 when it carried **seven** epics — the condition the
restructure removed. **New M37 has two fixed epics; there is nothing to split.** The recommendation
now attaches to **M38**, which inherited the accumulation. Confirmed as the Phase Chat recorded it.

---

## On the pattern — three verifications at the wrong layer, and the first was HQ's

The Phase Chat's own erratum names the class precisely:

> *"'verify, do not inherit' is satisfied by measuring something, and says nothing about whether you
> measured the right thing."*

Three P11 instances: the phase spec's Ollama context note (v1.0.0, **HQ's** — a 4,096-token claim
inherited from an opener and never checked against the running version); the starter's constraint 2a
xfail mechanism (**HQ's** — a claim contradicted by HQ's own Decision 4 in the same document set); and
the M37 milestone spec's dispatch preconditions (checked at the **host** layer for code that runs
**inside the sandbox**).

**Two of the three are HQ's**, and the Phase Chat's is the one that was caught fastest and corrected
most cleanly. **Filed as `P11-GH-2`** — recorded, not fixed, and deliberately not placed in a
milestone; a third instance of a class is a record, not yet a remedy.

**Ratified as practice in the interim:** a verification states the **layer it was performed at**, and
the layer the verified thing executes at. Where those differ, the verification is not evidence.

---

## Disposition

Route A declined (affirmed). **Route C adopted** — E37.1 manual/paid, artifacts unchanged. **The
local/paid comparison moves to M38**, intent preserved. **Route B.1 authorized as B2.1**, High,
post-mortem scoped to the three-week workaround pattern, delegated. **Route B.2 declined** with a
recorded trigger. **Split-M37 permission confirmed spent.** Phase spec amended to **v1.1.1**;
`P11-GH-2` filed.

**M37 is not blocked. E37.2 proceeds; merge order stays E37.1 first**, as the Phase Chat decided —
that call is upheld and its reasoning (a second non-uniform seeding row would double the flattening
risk G1 exists to bound) is correct.

**This ruling is an HQ-authored delivery. PSG §11.6.1 applies — the CFO is the mandatory diff
reviewer, default-accept does not apply, silence is not acceptance.**
