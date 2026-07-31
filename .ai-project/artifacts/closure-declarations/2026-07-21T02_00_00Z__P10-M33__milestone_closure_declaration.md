---
type: milestone-closure-declaration
milestone: M33
status: complete
completion_date: 2026-07-21
declared_by: Milestone Chat (P10-M33 — Proving Pair: v7.0.0 + First Real Agentic/Local Epic)
issued_to: Phase Chat (P10 — Fleet Adoption and Local-Inference Proving)
is_final_milestone: false
---

# MILESTONE CLOSURE DECLARATION — M33

Milestone **P10-M33 — Proving Pair: v7.0.0 + First Real Agentic/Local Epic** is hereby declared
**COMPLETE (awaiting consolidation)**. **Four** epics — E33.1, E33.2, E33.3, and E33.4 (a
decomposition addition, see below) — have been executed, **independently verified by this Milestone
Chat** (diff review, live suite re-runs on this branch after each merge, direct read-only
verification of both target repos' commits and stamps, and confirmation of the "not a demo"
provenance claims against pre-existing target-repo documents — **not Delivery Notices trusted on
faith**), accepted under PSG §11.6 default-accept, and merged to `milestone/M33` with explicit
human merge authorization for each (SN-19 / §11.6). Full test suite is green on consolidated
`milestone/M33` @ `a0bb077`: **366 passed, 0 failed, no skips** (up from the 363 baseline via 3 new
tests added by E33.3's sanctioned fix — an increase from new coverage, not a regression).

**M33 is the first P10 milestone and not the last (`is_final_milestone: false`).** Two remain:
**M34 (Fleet Roll-forward)** — binding order, it consumes this milestone's bump procedure (E33.1)
and settled runtime choice (E33.2) — and **M35 (System-Operator Canonization)**, independent and
schedulable at the Phase Chat's discretion. This declaration triggers Phase Chat consolidation of
`milestone/M33 → phase/P10`; it does **not** trigger phase closure.

**On the epic count — a completion gap found and closed.** M33 was planned with three epics. At
closure review this Milestone Chat verified the Milestone DoD line-by-line and found that
**Milestone DoD, Milestone AC 1, Phase Success Criterion 1, and the Phase Acceptance Criteria all
require *each* proving-pair project to have a committed run record**, while the Milestone spec's
E33.2 epic detail was written in the singular ("running **a** genuine epic of **a** target
project's own work"). E33.2 therefore correctly ran on `local-agent-runner` only, and the
three-epic decomposition never gave the `home_finance` run a home — the milestone was **not**
complete as specified. Rather than declare closure on an unmet DoD item, this was escalated to the
Phase Chat, which disposed: **add E33.4**. E33.4 was authored under the decomposition authority the
Milestone spec grants (§Planned Epics), executed, and merged. The bar is now met.

---

## Completion Verification

✅ **E33.1 — Enrolled-project v7.0.0 bump procedure + apply to the pair (merged PR #150, `d877b6b`).**
Delivered a repeatable bump procedure (`.ai-project/artifacts/reference/v7-bump-procedure/README.md`)
choosing **Direction B (targeted governance-file sync)** over re-running `ai-project-init` — which is
a project-*creation* tool that aborts on an existing `.governance` submodule or clobbers a hand-tuned
`.ai-project.yml` — with preconditions, 5 ordered steps, **7 documented failure modes**, and a
stamp+confirm method. Applied to both proving-pair projects. *Independently verified at Stage-2:* I
ran the procedure's own confirmation commands against both target clones — `home_finance` @ `0ea6924`
and `local-agent-runner` @ `231a2cf`, each with `framework_version: v7.0.0`, submodule pinned to
`8044451` (v7.0.0), canonical agent sha `66404389…`, and no superseded `hq.agent.md`. Every claim
matched. Failure Mode 3 is load-bearing for M34: the installed `governance.agent.md` is an
out-of-band **copy** that re-pinning the submodule does **not** refresh — both projects carried the
stale v6.0.0 agent before this bump. P6-GH-15 was checked and found **not applicable** to the pair,
with a per-project check retained for legacy installs (M34/E34.1's case).

✅ **E33.2 — First real Agentic/Local epic on the pair + runtime decision (merged PR #151, `f059941`).**
A genuine epic of `local-agent-runner`'s own work (CF-2 slice: public `run`/`Result` library API) ran
through the local path via `bin/run-dev-agent` on Ollama, advancing the target at **`4ec1e8f`**
(suite 210/1). Two runs of the same task on the same runtime, differing only in model, produced the
runtime evidence: **Run A (`qwen2.5-coder:14b`, the configured `epic_dev`/`epic_qa`)** returned exit
0/`completed` having produced **zero work** (the SN-3 failure mode — a JSON plan emitted as prose);
**Run B (`qwen3-coder:30b`)** returned exit 2/`max_iterations_exceeded` having produced **correct,
green work**. The decision is recorded across all four required dimensions with the run's own
observations. *Independently verified at Stage-2:* target commit `4ec1e8f` exists, descends from the
v7.0.0 bump `231a2cf`, and lands the public-API export plus its test.

✅ **E33.3 — Trustworthy measurement out of the run / P9-GH-2 (merged PR #152, `775404e`).**
Pointing `measure-token-burn` at E33.2's artifacts revealed the tool **silently dropped the entire
run** — its Direction C-lite path required the old `transcript.json`/`run-metadata.json` filenames
and skipped E33.2's per-model layout, so none of the run's numbers reached the dataset and nothing
signalled the omission. Sized (with recorded basis) as a **proportionate fix**: `bin/measure-token-burn`
1.0.0 → 1.1.0 now recognizes the per-model layout and records the **run-status each token count is
attached to**, folding in E33.2's exit-code-untrust finding; Run A's false-positive is machine-flagged
(`zero_work_completion`), Run B's absent exit code is an honest **gap** (G11), not a guess. Old PROVE
runs preserved unchanged (404/759/837). *Independently verified at Stage-2:* suite 363 → **366**,
new local-extraction tests pass, extent confined to the sanctioned surface.

✅ **E33.4 — home_finance real Agentic/Local epic, proving-pair completion (merged PR #153, `a0bb077`).**
The decomposition addition that closed the completion gap. A genuine epic of `home_finance`'s own
work — the **MXN currency-default correction** — ran on Ollama with `qwen3-coder:30b`, advancing the
target at **`8dfb2bd`** (migration `change_column_default` USD→MXN, regenerated `db/schema.rb`,
de-hardcoded factory, new spec; suite 275/0). No runtime decision and no measurement were produced —
those legs were already closed, and the settled runtime was **applied, not re-opened**. *Independently
verified at Stage-2:* commit `8dfb2bd` exists, descends from E33.1's bump `0ea6924`, and the
"genuine, not a demo" claim holds — the MXN correction is named in `home_finance`'s **pre-existing**
`PROJECT_BRIEF.md`, `P2__phase.md`, and `P2-M1__milestone.md`, while the commit itself added only the
new epic spec. The run exited **2 with complete work** and this was reported as a **false-negative**
rather than smoothed over — corroborating E33.2's exit-code-untrust finding from the opposite
direction.

✅ **All four epics accepted** under PSG §11.6 default-accept (no Review Decision was required — every
delivery was clean), each merged with explicit in-chat human merge authorization (SN-19).

---

## Milestone Definition of Done — verified

- ✅ **E33.1, E33.2, E33.3 (and E33.4) each meet their Definition of Done** — verified per epic at
  Stage-2, above.
- ✅ **All epic branches merged to `milestone/M33`** — `d877b6b`, `f059941`, `775404e`, `a0bb077`.
- ✅ **Both `home_finance` and `local-agent-runner` stamped `framework_version: v7.0.0` (confirmable),
  each with a committed run record for at least one real Agentic/Local epic under the fixed posture**
  — stamps verified directly in both clones; run records at
  `.ai-project/artifacts/agentic-runs/P10-M33-E33.2/` (`local-agent-runner` @ `4ec1e8f`) and
  `.../P10-M33-E33.4/` (`home_finance` @ `8dfb2bd`). **This is the item E33.4 was added to satisfy.**
- ✅ **A documented, repeatable v7.0.0 bump procedure exists with evidence of application to the pair**
  — procedure + cross-repo confirmation evidence, both committed.
- ✅ **The Ollama-vs-llama.cpp+Qwen3.6 runtime decision is recorded with the run's own reasons** —
  `P10-M33-E33.2__runtime-decision.md`, four dimensions, plus the Phase Chat/CFO disposition.
- ✅ **Real burn/validation data from the run exists with an explicit, evidence-backed honesty
  judgment on `measure-token-burn`'s numbers (P9-GH-2 to the extent M33 needs)** —
  `e33-2-run-measurement-trust.md` §1–§4; the judgment is stated verbatim, with no skipped-check
  third state.
- ✅ **Full suite green on `milestone/M33` for changes touching this repo** — **366 passed, no
  failures, no skips**. The 363 → 366 movement is E33.3's three new tests (new coverage, not a
  regression); no test was skipped to route around a change.
- ✅ **Milestone Closure Declaration produced (`is_final: false`)** — this document.

---

## Milestone Acceptance Criteria — verified

1. ✅ **v7.0.0 stamped and confirmable in both proving-pair projects, each with a committed run record
   for a real Agentic/Local epic under the fixed posture** — verified in both target clones and both
   run records.
2. ✅ **The runtime decision is recorded in the run evidence with the run's own reasons — not an
   abstract memo** — every reason traces to Run A/B observations (quality, throughput, loadability,
   review burden), with the un-observable part explicitly *not* decided.
3. ✅ **Real burn/validation data exists with a stated, evidence-backed judgment that
   `measure-token-burn`'s numbers for that run can be trusted** — the judgment is affirmative *with a
   stated condition* (the numbers can be trusted **only when read with the run-status now attached**),
   and records that they could **not** be trusted before this epic.
4. ✅ **A documented, repeatable v7.0.0 bump procedure exists and has been applied to the pair** —
   with preconditions and failure modes sufficient for a third project (M34's lever).
5. ✅ **Every decision traces to a real run — none to an un-run abstraction; where a run could not
   complete, an explicit blocker-and-escalation stands in its place** — the llama.cpp + Qwen3.6-27B-**Q8_0**
   comparison could not be trialed on the proving host (llama.cpp absent; ~42 GB Q8_0 not loadable on
   16 GB VRAM / 30 GB RAM) and was **recorded as a partial blocker and escalated**, not papered over.
   The Phase Chat/CFO disposed it: **"Ollama stands; raise the model tier"**, with the Q8_0 trial
   **parked pending Mac-class ~42 GB hardware** (recorded at `ad6ea9b` in the runtime-decision doc).
6. ✅ **Full suite green at milestone delivery — no regressions, no new skips** — 366 passed, 0 skips.

---

## Handed to the Phase Chat

**Consolidation (PSG §5B Steps 3–5; AOG §3.4 Step 4 — the PR is the human's to own, not
auto-created):**
- Source: `milestone/M33` @ `a0bb077` → Target: `phase/P10`
- Suggested title: `Milestone M33: Proving Pair — v7.0.0 + First Real Agentic/Local Epic`
- Description should carry the four-epic list and this declaration's summary.

**Outstanding Phase Chat action (adjacency — the Milestone Chat must not edit its parent's spec):**
- ⚠️ **Amend the Milestone spec's epic list** to add **E33.4** — front-matter `epics:` (currently
  `E33.1, E33.2, E33.3`) and §Planned Epics — recording the completion-gap disposition that added it.
  The spec currently under-reports the delivered decomposition.

**Carry-forwards / open items for P10:**
- **P10-GH-1 (candidate, from E33.1):** `framework_version` is a **convention-only** top-level key —
  it is not defined in `governance/ai-project-yml-spec.md`. Schema-blessing it is a framework
  *capability* change, correctly deferred out of these adoption epics. Recommend recording it as a
  GH item.
- **The `models:` routing edit is NOT done.** The settled runtime choice is "Ollama + a raised model
  tier," but `.ai-project.yml` `models.epic_dev`/`epic_qa` remain `local:qwen2.5-coder:14b` — the
  model E33.2 proved **unusable** for agentic epic work. Both real runs selected `qwen3-coder:30b` as
  a *documented dispatch deviation*. **M34 should make the routing change**, or the next agentic
  dispatch will again default to a model known to produce false-positive empty completions.
- **Parked:** the llama.cpp + Qwen3.6-27B-Q8_0 trial, pending Mac-class ~42 GB hardware.
- **Residual P9-GH-2 work**, recorded not dropped: blind spot **G9** (local *input* tokens unmeasured
  — a runner-side gap) and a general self-verification harness for the paid dataset. Neither was
  required to trust this run's numbers.
- **Exit-code untrust is now a two-sided, corroborated finding** (E33.2: exit 0 / zero work; E33.4:
  exit 2 / complete work). On this stack the exit status is not a reliable completion signal — review
  must read the transcript and target repo. Worth carrying into M34's fleet runs.

**Cross-repo note:** the target-repo branches (`home_finance` and `local-agent-runner`
`chore/framework-v7.0.0-bump`, and the two run branches) are committed **locally and not pushed** —
publishing them is the CFO's outward action, outside these epics' scope. Verification from this repo
does not depend on it: every claim is confirmable from the committed evidence plus the cited commits.

**M33 → M34 is binding.** M34 consumes E33.1's bump procedure and E33.2's settled runtime choice;
both now exist. M35 remains independent.
