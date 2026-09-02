---
type: milestone-closure-declaration
milestone: M42
status: complete
completion_date: 2026-09-02
declared_by: "Milestone Chat (P12-M42 — Fail-Closed Execution Tier)"
issued_to: "Phase Chat (P12 — Completion: Fail-Closed Defaults and the Drivr MVP)"
is_final: false
---

# MILESTONE CLOSURE DECLARATION — M42

Milestone **P12-M42 — Fail-Closed Execution Tier** is declared **COMPLETE (awaiting consolidation)**.

**Five epics were delivered, re-measured by this Milestone Chat at Stage-2 (G2), and merged with
explicit human merge authorization for each:** **E42.1** (#243), **E42.2** (#244), **E42.3** (#245),
**E42.4** (#246), **E42.5** (#247).

**Accept-by-silence was NOT suspended for M42** (unlike M41). Each epic was accepted by default-accept
(PSG §11.6) with the acceptance acknowledged **in-chat** (SN-19 — no artifact), after an independent
Stage-2 re-measurement of the delivery against its own report. **No rework attempt was consumed on any
epic; each stands at attempt 1 of 3.**

---

## ⚠ THE ONE SENTENCE THIS MILESTONE SHOULD BE READ BY

> **Four defects, one disposition — *when the evidence that should gate an action is absent, the
> action proceeds* — and every one of the four now stops and says so, with a test that proves it, and
> the blast radius is now known rather than assumed.**

M42 was the milestone with **zero dependency on anything else in the phase** and the one **two other
milestones wait on.** On closure it releases **both** M47 (the phase's proof) and **E41.5** (M41's
terminal epic). Its Definition of Done is **met** — with two findings carried forward honestly rather
than folded into a clean tick.

---

## Completion Verification — the Definition of Done, item by item

| # | DoD item | Disposition |
|---|---|---|
| 1 | All five epics delivered, accepted, and merged to `milestone/M42` | **MET.** E42.1 `3583815`, E42.2 `cd27fe1`, E42.3 `f215188`, E42.4 `16ed4ea`, E42.5 `f80fb1d` |
| 2 | No path in `bin/` proceeds on absent gating evidence | **MET, with one caveat (see §Carry-forward A).** Sandbox absence **aborts** (E42.1, `LOCAL_UNAVAILABLE_EXIT`); staging is **epic-scoped** (E42.2, `git add .` gone); approval failure **aborts** and the `--admin` rung is **removed** (E42.3); `ai-project-init` **never manufactures** an agent (E42.4, stub branch deleted). *The caveat: a default init now **fails closed** because the default ref is stale — correct disposition, but "finds the real one" holds only when the ref carries the agent.* |
| 3 | The suite asserts the guard rather than the defect — `:447-460` and `test_init_agent_path.py` inverted, plus a new approval-abort test | **MET.** E42.3 inverted `test_promote_branch_fallback_merge` **and** wrote `test_promote_branch_approval_failure_aborts` (G2 — the `:269` path had no coverage); E42.4 inverted `test_init_agent_path.py` with `P6-GH-11` preserved |
| 4 | Every new guard has been shown to fail when removed | **MET.** Falsification demonstrated per epic: E42.1 (3/5), E42.2 (4/4 both branches), E42.3 (both), E42.4 (both) |
| 5 | The end-to-end `ai-project-init` was run, and its result stated | **MET — and confirming.** E42.4's Obligation 1 ran **four** real inits (no `--skip-submodule`); the `P12-GH-2` inference is **CONFIRMED**, with two findings beyond the note recorded (see §Carry-forward B) |
| 6 | The fleet is swept; every placeholder repaired or recorded | **MET.** E42.5 enumerated **12** enrolled projects by **content** (not size); the one victim (`social-stories-creator`) was **repaired**, not merely recorded (real agent restored from its submodule, `c419fb5`) |
| 7 | Blast radius recorded as a call graph, every caller, Drivr included, liveness stated | **MET.** E42.5 produced the call graph; Drivr inspected directly. Outcome corrects the milestone's framing (see §Carry-forward C) |
| 8 | Defect 2's design decision and E42.1's opt-in shape recorded | **MET.** E42.2 recorded candidate 3 (the run's own recorded footprint) with all five candidates weighed; E42.1 recorded **REMOVAL** (no host path survives) |
| 9 | Suite green — no regressions, no skips | **MET, with the baseline drift noted.** `549` (the 2026-08-19 baseline) is **two epics old**: M41 added `+20`, E42.1 `+5`, E42.2 `+4`, E42.4 `+4`; E42.3 and E42.5 add no pytest-collected tests. Present count **582 passed / 0 failed**, re-measured at each stage. **No skips introduced.** |
| 10 | Milestone Closure Declaration committed, `is_final: false` | **This document** |

---

## Acceptance Criteria (Milestone) — verified

- [x] **A reader can determine, for each of the four defects, what it did, what it now does, and which
      test proves it — from committed artifacts alone.** Each epic's record documents before/after/test.
- [x] **No fix substitutes a louder log for an abort.** Warning-and-continue appears as the disposition
      of none of the four — sandbox aborts, staging scopes, approval aborts, init fails closed.
- [x] **No fix manufactures a substitute for missing evidence.** The `P12-GH-2` stub branch is removed,
      not improved; a placeholder is not installable at all.
- [x] **Every claim states layer, time and scope; read-versus-run honoured.** Each record carries its
      `P11-GH-2` block, and Obligation 1 (the real run) was the load-bearing instance of the distinction.
- [x] **M47's precondition is satisfiable.** A Phase Chat can point at this closure and say the
      execution tier no longer fails open **and** who runs it is now known.

---

## Carry-forwards — recorded honestly, not folded into the tick

**A — the stale `DEFAULT_GOVERNANCE_VERSION="v2.0.0"` (E42.4).** The default ref predates the canonical
agent file, so a **default** `ai-project-init` now **fails closed** — the correct disposition, but it
means the initializer refuses a default run until the ref is bumped. Not E42.4's scope (bumping the ref
is a separate decision), but **owned here, not orphaned**: surfaced to the Phase Chat for a
bump-or-declare decision. *This is fail-closed working, not the milestone failing — but a reader must
be able to see that a default enroll is non-functional until the ref moves.*

**B — the CWD-drift nesting (E42.4, run A1).** The end-to-end run exposed a third layer beneath the
`P12-GH-2` note: the placeholder did not even land at the canonical path, because `cd` bookkeeping
drifted the write into a nested `<project>/<project>/` directory. **Fixed and proven** by run B1.

**C — Drivr executes none of the three scripts (E42.5).** The milestone's risk framing — *"a defect
Drivr is about to invoke nightly"* — is **not realized**. Drivr's dispatch path is `opencode run`
(`execution/opencode.py`); its references to the three scripts are anti-pattern quotes, the
execution-environment decision's Direction B (deliberately *not* routing through the orchestrator's
sandbox), and enrollment history. **The orchestrator's actual live-capable executor is
`bin/ai-project-daemon`, which is currently stopped**; `ai-project-git-merge` has **no execution caller
at all** — a dead path today. This corrects the milestone spec's stated risk and should reach the
phase's record, not just this one.

---

## Milestone Summary — what M42 actually produced

**Four fail-open defects closed, each with falsified guard tests, plus an evidence tail that answered
"who runs this?" instead of assuming it.**

1. **The execution tier no longer fails open.** Sandbox absence aborts with the file's own
   `LOCAL_UNAVAILABLE_EXIT` convention (E42.1); staging is scoped to the epic's own recorded footprint
   with the out-of-scope case made visible (E42.2); approval failure aborts and the privilege-escalating
   `--admin` rung is gone (E42.3); the initializer stops manufacturing a governance agent and its two
   path defects are fixed together (E42.4).
2. **The suite asserts the guard, not the defect.** Two self-protecting tests inverted, plus a new
   approval-abort test for a path that had no coverage at all (G2).
3. **Obligation 1 was actually run, not inferred.** Four real end-to-end inits confirmed the `P12-GH-2`
   mechanism and exposed a third defect (CWD nesting) the note had not named.
4. **The blast radius is a call graph, not a name sweep.** Every caller named, Drivr inspected
   directly, liveness stated per path — with the honest correction that Drivr executes none of the
   three scripts and `git-merge` is currently dead.

**Net:** M47's precondition — *the execution tier no longer fails open* — is discharged, and E41.5's
gate is open.

---

## Required Action: Consolidation

**To fully close this milestone, consolidation is required:**

1. **Create Pull Request** from `milestone/M42` → `phase/P12` (title: "Milestone M42: Fail-Closed
   Execution Tier").
2. **Human reviews the consolidation PR** (all five epics present, no conflicts, branch hierarchy
   correct).
3. **Merge PR** — becomes the milestone closure commit.
4. **Report the merge commit SHA back** to the Phase Chat.

**The next milestone (`milestone/M47` — First Real Agentic Integration, the phase's proof) is released
by this closure**, as is **E41.5** (M41's terminal epic, gated on M42 since 2026-08-19).
