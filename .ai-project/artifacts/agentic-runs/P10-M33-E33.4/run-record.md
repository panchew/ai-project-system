---
epic: P10-M33-E33.4
type: agentic-run-record
status: complete
date: 2026-07-20
target_repo: home_finance
target_branch: epic/P2-M1-E1.1-mxn-currency-default
target_commit: 8dfb2bd
target_base: 0ea6924 (chore/framework-v7.0.0-bump, framework_version v7.0.0)
runtime: Ollama 0.30.0
model: qwen3-coder:30b (raised tier — dispatch deviation, see §2)
dispatch: bin/run-dev-agent (governance adapter, CONTRACT §7) direct on host
---

# E33.4 Run Record — `home_finance`'s real Agentic/Local epic (proving-pair completion)

This is the governance run record for Epic P10-M33-E33.4 (framework repo, `epic/P10-M33-E33.4`).
The real code produced by the run lives in the **target repo** `home_finance`
(`epic/P2-M1-E1.1-mxn-currency-default`, commit `8dfb2bd`) — **not** merged onto `phase/P10`
(Cross-Repo split). A reader of *this* repo can verify the target outcome from the cited commit plus
the context and transcript copied alongside this file.

With E33.2's `local-agent-runner` run, this completes the **"each proving-pair project has a
committed run record for at least one real Agentic/Local epic"** bar (Milestone DoD / AC 1; Phase
Success Criterion 1 / Phase AC).

## 1. What was scoped (Manual/Paid framing)

- **Target project:** `home_finance` — the proving pair's remaining un-run half. It was bumped and
  confirmed at `framework_version: v7.0.0` by E33.1 (`0ea6924`) but had carried no real epic.
- **Genuine unit (the Epic Chat's Design Decision):** the **MXN currency-default correction** —
  `financial_events.currency` carried a database-level default of `"USD"`, contradicting the
  MXN-first brief. This is **pre-articulated, deferred, CFO-owned work**, named in three places in
  `home_finance`'s own governance record before this Epic existed:
  - P2 phase doc §Notes — *"Currency default fix: the schema currently defaults
    `financial_events.currency` to `"USD"`; correcting this to MXN is part of M1's money foundation"*
  - P2-M1 milestone §Problem Statement — *"today the schema defaults `financial_events.currency` to
    `"USD"`, contradicting the brief"*
  - P2-M1 milestone **Goal 4** (*"correct the schema's currency default away from USD"*) and
    §In Scope (*"migration to fix the `currency` default"*)

  M1's sequencing rationale explicitly requires it be *"resolved at the foundation, not retrofitted
  later"*, before write flows harden around it. **Why it qualifies:** real, pre-articulated,
  founder-deferred work that advances the project's own roadmap — not a synthetic demo (Hard
  Constraint). It is also small, self-contained and reviewable, mirroring E33.2's slice-selection.
- **Scoped as target epic `home_finance` P2-M1-E1.1**, spec committed at
  `home_finance:docs/phases/P2__Monthly_Loop_and_North_Star/P2-M1-E1.1__spec__mxn-currency-default.md`.
  Its **Definition of Done** is the task text the adapter extracts and hands to the model.

## 2. Dispatch path + model selection (documented Epic-Agent decisions)

Dispatched through the governance-aware adapter **`bin/run-dev-agent`** (CONTRACT §7 shim; carries
the E31.2 dispatch-time model guard and the run-record convention) **directly on the host**, with
the working directory set to the `home_finance` checkout — the same path E33.2 took (and
P7-M26-E26.3-PROVE before it), *not* wrapped in the orchestrator's Docker sandbox. Rationale
unchanged from E33.2: the adapter is the governance-bearing piece, and running it directly keeps
Docker/container-networking failure surface out of the run.

**Model deviation (documented, no routing edit).** `.ai-project.yml` `models.epic_dev`/`epic_qa` are
still `local:qwen2.5-coder:14b`. That model was **proven unusable** for agentic epic work in E33.2
(Run A: false-positive completion, zero work), and the Phase Chat / CFO disposition on
`P10-M33-E33.2__runtime-decision.md` is **"Ollama stands; raise the model tier."** This run therefore
dispatched with `AI_PROJECT_ACTIVE_MODEL=local:qwen3-coder:30b`. Per the spec's Non-Goals and the
starter's do-not-touch list, the **`models:` routing edit is a separate authorized act and was not
performed here** — the raised-tier selection is recorded as a dispatch deviation, exactly as E33.2
did. **No runtime decision is recorded by this Epic; the runtime is settled and was applied, not
re-opened.**

**E31.2 guard honored.** `check_local_availability()` probed `http://localhost:11434/api/tags` before
the runner was invoked and confirmed `qwen3-coder:30b` was actually pulled; no local model was
assumed. The first dispatch attempt exited **3** (config error: the `.ai-project/queue/04_epic.json`
trigger was not yet in place) — the adapter refused loudly rather than inventing a fallback, and the
run proceeded only after the trigger was written. The guard never had to fire exit 5.

**Runner discovery.** `local-agent-runner` is not pip-installed on this host, so `LOCAL_AGENT_RUNNER`
pointed at a two-line wrapper invoking `python3 -m local_agent_runner.cli` from the repo checkout —
the same shim shape E33.2 used.

## 3. Hardware / substrate (loadability)

| | |
|---|---|
| CPU | AMD Ryzen 5 9600X, 6C/12T |
| RAM | 30 GiB total |
| GPU | NVIDIA RTX 5060 Ti, **16 GB VRAM** |
| Runtime | Ollama 0.30.0 (container `ollama`), `http://localhost:11434` |
| Model | `qwen3-coder:30b` — 30.5B params, Q4_K_M, 18.6 GB on disk |

Loaded-model footprint (from `/api/ps` during the run): **12.9 GB VRAM + 21.4 GB total** — a
30B/Q4_K_M exceeds 16 GB VRAM and **partially offloads to system RAM**, yet loads and runs. This
reproduces E33.2's measurement exactly on a second project, confirming the raised tier is loadable on
this substrate rather than borderline.

**Target-repo substrate prepared before dispatch (not part of the run):** `home_finance` requires
PostgreSQL (docker-compose `postgres:16` on port 5435). It was brought up and `db:prepare` run for
both `development` and `test` so the run's own `db:migrate` and `rspec` steps had a working database.
Pre-run baseline established here: **274 examples, 0 failures**.

## 4. The run

One run, one model. **No comparative model trial** — E33.2 already settled the runtime; a second
trial would be re-opening a closed question (spec Non-Goals).

### `qwen3-coder:30b` (raised tier, Ollama 0.30.0)

- **Exit 2, `status: max_iterations_exceeded`, `iterations: 10`, 3,875 tok, 139.8 s.**
- **Produced correct, complete, green work.** Every one of the Definition of Done's five steps was
  executed correctly, and **the work was finished and verified green by iteration 6**:

  | iter | tool | outcome |
  |---|---|---|
  | 0 | `write_file` | migration `20260720120000_change_financial_events_currency_default_to_mxn.rb` — exactly as specified |
  | 1 | `run_command` | `bundle exec rails db:migrate` → exit 0, migration applied, `db/schema.rb` regenerated |
  | 2 | `read_file` | `spec/factories/financial_events.rb` |
  | 3 | `edit_file` | factory `currency { 'USD' }` → `{ 'MXN' }` |
  | 4 | `read_file` | `spec/models/financial_event_spec.rb` |
  | 5 | `edit_file` | added the `'currency default'` describe block |
  | 6 | `run_command` | `bundle exec rspec` → **exit 0, 275 examples, 0 failures** |
  | 7 | `read_file` | `db/schema.rb` 1–50 (self-verification, post-completion) |
  | 8 | `run_command` | `grep -n "financial_events" db/schema.rb` — **denied** by `allow_commands` |
  | 9 | `read_file` | `db/schema.rb` 50–100 (self-verification, post-completion) |

- **Why exit 2 despite finished work:** iterations 7–9 were the model **self-verifying work it had
  already completed and proven green**. It never spent a turn emitting a final answer, so the loop
  hit the iteration ceiling. The transcript's `final_answer` field is nonetheless populated and
  **accurate** ("All steps in the Definition of Done have been completed successfully…"). This is a
  **false-negative exit code** — the same class E33.2 Run B hit, but from a different cause (E33.2
  Run B ran out of budget with work still in flight after 3 iterations lost to a denied
  `pip install -e .`; here the work was done at iteration 6 and 4 iterations went to redundant
  verification).
- **Corroborates E33.2's central caution:** on this stack the **exit code alone is not a reliable
  completion signal** — in E33.2 exit 0 meant zero work, and here exit 2 means complete, green work.
  Verification must read the transcript and the target repo, not the exit status.
- **One denied command, one iteration lost** (`grep`). E33.2's lesson was applied — the allowlist was
  scoped to exactly the two commands the DoD names — which cut denial waste from 3 iterations
  (E33.2 Run B) to 1, but did not eliminate the model's reach for general shell utilities.
- **Throughput:** 27.7 tok/s end-to-end including a ~38 s cold model load on iteration 0; ~41 tok/s
  excluding it. Iteration 5 alone consumed 3,266 of the 3,660 generated tokens, because the runner's
  `edit_file` requires reproducing the exact `old` text and the model regenerated a large block of
  the spec file to anchor a small insertion — a concrete efficiency observation about the tool
  surface, recorded as an observation only (no measurement deliverable here; that leg closed with
  E33.3).
- Evidence: `transcript-qwen3-coder-30b.json`, `run-metadata.json`, `context.md` (the exact scoped
  context handed to the runner — spec only, no governance corpus, CONTRACT §6 token discipline).

## 5. Target-repo outcome (the run advanced the project)

`home_finance` `epic/P2-M1-E1.1-mxn-currency-default` @ **`8dfb2bd`** (base `0ea6924`, the E33.1
v7.0.0 bump commit). The MXN currency-default correction landed:

- `db/migrate/20260720120000_change_financial_events_currency_default_to_mxn.rb` —
  `change_column_default :financial_events, :currency, from: "USD", to: "MXN"`
- `db/schema.rb` — now `t.string "currency", default: "MXN", null: false`; schema version
  `2026_07_20_120000`
- `spec/factories/financial_events.rb` — no longer hardcodes `'USD'`
- `spec/models/financial_event_spec.rb` — new example asserting `FinancialEvent.new.currency == "MXN"`
- `app/models/financial_event.rb` **unchanged**, as the spec required

**Suite: 275 examples, 0 failures** (274 baseline + 1 new), independently re-run by this Epic Chat
after the run. This closes a correction `home_finance`'s own P2/M1 documents had been carrying
since 2026-06-24. **Real work advancing the project, not a demo — Hard Constraint satisfied.**

Code was committed **as-produced by the model**, following E33.2's precedent of preserving the
run's evidentiary value. One cosmetic wart is noted rather than silently fixed: the generated
migration file has **no trailing newline**.

**Distribution boundary:** the target branch is committed **locally and has not been pushed** to
`home_finance`'s remote. `home_finance` is CFO-controlled; publishing the branch is the CFO's call,
not this Epic's. Verification from this repo does not depend on the push — the transcript and
context are copied here, and the commit is reproducible from the cited base.

## 6. Pointers

- Scoped target epic spec:
  `home_finance:docs/phases/P2__Monthly_Loop_and_North_Star/P2-M1-E1.1__spec__mxn-currency-default.md`
- Target-repo run artifacts (adapter-written, committed in `home_finance` at `8dfb2bd`):
  `home_finance:.ai-project/artifacts/agentic-runs/P2-M1-E1.1/`
- Settled runtime this run applied:
  `docs/phases/P10__Fleet_Adoption_and_Local_Inference_Proving/P10-M33-E33.2__runtime-decision.md`
  §Phase Chat / CFO disposition
- E33.2's run record (execution pattern mirrored):
  `.ai-project/artifacts/agentic-runs/P10-M33-E33.2/run-record.md`
- E33.1 `home_finance` bump this run depended on:
  `docs/phases/P10__Fleet_Adoption_and_Local_Inference_Proving/P10-M33-E33.1__confirmation-evidence.md`
- Transcript + exact context handed to the runner: this directory.
