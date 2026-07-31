---
project: ai-project-system
phase: P10
milestone: M35
epic: E35.5
type: reference
status: complete
last_updated: 2026-07-31
---

# Scored results — Milestone × local-inference back-test

Scored strictly against `rubric.md` as committed in **`562502b`**, before any model was run. Where a
result was close, the rubric was applied **as written** rather than reinterpreted — see defect 5,
where that discipline changed the outcome.

**Candidate:** `qwen3.6:27b` (Ollama 0.30.0), tag verified against `/api/tags` at execution —
27.8B, Q4_K_M, 17.4 GB. **Comparator:** none run (optional; its absence is not a shortfall).

---

## Summary

| # | Defect | Kind | Run 1 | Run 2 | Result | False alarms |
|---|---|---|---|---|---|---|
| 1 | M33 decomposition gap | decomposition/scope | CATCH | CATCH | **CATCH** | 0 |
| 2 | E33.2 Run A false-positive completion | completion-signal | CATCH | CATCH | **CATCH** | 0 |
| 3 | E33.4 false-negative completion | completion-signal (**inverse**) | CATCH | CATCH | **CATCH** | 0 |
| 4 | M34 footboard dirty-entry miscount | factual accuracy | CATCH | CATCH | **CATCH** | 0 |
| 5 | P10-GH-6 starter-lint false positive | test correctness | **MISS** | CATCH | **SPLIT** → not a catch | 0 |

**Catches: 4 of 5. False alarms: 0. Splits: 1.**

Against the pre-registered bar — catch on ≥4 of 5; no false alarm on defect 3; ≤2 false alarms total
— all three conditions hold. **The recorded judgment is PASS.** See `judgment.md`, including what a
PASS does and does not license.

---

## Run inventory — every run made

Nothing here was selected on content. The two aborts and the ENOSPC failure produced **no model
output at all**; the truncated run and the two superseded runs are committed in full under
`runs/truncated/` and `runs/superseded/`.

| # | Packet | Outcome | Scored? | Why |
|---|---|---|---|---|
| A1 | 4 | Aborted — 10-min shell timeout, zero output | no | infrastructure |
| A2 | 4 | Aborted — SIGTERM from the Epic Chat's own `pkill`, zero output | no | infrastructure |
| S1 | 4 | Completed, REJECT + correct count | **no** | capture incomplete — `thinking` field discarded |
| S2 | 4 | Completed | **no** | same |
| P | — | Infrastructure probe (`"Reply with the single word: ok"`) | no | established that Ollama returns a separate `thinking` field |
| T1 | 5 | `done_reason=length` — truncated mid-sentence at `num_ctx` 8192 | **no** | mechanical truncation (rubric Run protocol) |
| F1 | 5 | `OSError: [Errno 28] No space left on device`, zero output | no | host disk exhausted by an unrelated `update-notifier-crash` loop that had grown `/var/log/syslog` to 327 GB |
| 1–10 | 1–5 | Completed, `done_reason=stop` | **yes** | the scored set |

**Disclosure on T1.** The truncated packet-5 run was discarded for truncation, not for its answer —
but its visible portion concluded *"false positive … the starter file must be updated"*, which under
the rubric would have scored **MISS**. Discarding it therefore did **not** favour the candidate, and
the re-run's run 1 scored MISS anyway. The full truncated output is committed.

**Mechanical parameters were corrected twice, never tuned toward an answer:** `num_ctx` was raised
after T1 truncated, and `num_gpu` was capped after a CUDA OOM at `num_ctx 32768` (Ollama tried to
place 56 layers on a 16 GB card, requesting 16,782 MiB against 15,849 available). Both are recorded
in each run file's `Options:` line. **No prompt was ever changed.**

### Timings and token counts (context only — not inputs to the judgment)

| Packet | Run | `done_reason` | prompt tok | eval tok | wall clock | `num_ctx`/`num_gpu` |
|---|---|---|---|---|---|---|
| 1 | 1 | stop | 25,195 | 5,665 | 1496.6s | 49152 / 42 |
| 1 | 2 | stop | 4 * | 6,348 | 1603.0s | 49152 / 42 |
| 2 | 1 | stop | 4 * | 1,690 | 129.8s | 8192 |
| 2 | 2 | stop | 4 * | 2,204 | 169.3s | 8192 |
| 3 | 1 | stop | 11,194 | 2,221 | 372.8s | 32768 / 46 |
| 3 | 2 | stop | 4 * | 2,632 | 418.9s | 32768 / 46 |
| 4 | 1 | stop | 1,060 | 5,529 | 426.8s | 8192 |
| 4 | 2 | stop | 4 * | 4,587 | 351.7s | 8192 |
| 5 | 1 | stop | 3,934 | 4,132 | 622.0s | 32768 / 46 |
| 5 | 2 | stop | 3,934 | 4,411 | 645.8s | 32768 / 46 |

`*` **`prompt_eval_count: 4` is an Ollama accounting artifact, not a short prompt.** It reports only
newly-evaluated tokens after a prefix-cache hit. Verified by content: packet 2 run 1 reported
`prompt_tok 4` yet its answer discusses `local_agent_runner/__init__.py`, `tests/test_public_api.py`
and `exit_code: 0` — material that appears nowhere except packet 2.

**Throughput is not comparable to M33's figures.** E33.2/E33.4 measured `qwen3-coder:30b` while
ComfyUI held 2.3 GB of VRAM; these runs were made after stopping that container, with 15.3 GB
resident on GPU instead of 11.0 GB. Row P4's reason was never price, and the rubric excludes
throughput from the judgment.

---

## Defect 1 — M33 decomposition gap → **CATCH**

Ground truth: NOT SOUND. M33 DoD 3 / AC 1 require a run record for **each** proving-pair project;
E33.2's DoD commits only to "**a** proving-pair project".

**Run 1** — verdict `NOT SOUND`, gap located and both sides quoted:

> "❌ **NOT GUARANTEED.** E33.1 guarantees the stamping of both projects, but E33.2 only commits to
> running an epic and producing a run record for *at least one* project, leaving the second project
> without a guaranteed run record."

and, in its conclusion, it independently proposed the remedy this milestone actually adopted:

> "To restore soundness, E33.2 must either be expanded to guarantee runs on both projects, split into
> two separate epics (one per project), or **a follow-up epic added under M33 to cover the second
> project's run**."

That third option is what E33.4 was — reached without ever seeing it.

**Run 2** — verdict `NOT SOUND`, same gap, proved by elimination across all three epics:

> "**Guaranteed by:** **NONE**. This is a hard decomposition gap."

> "**E33.1** explicitly excludes running epics (`Non-Goals: Run the first real Agentic/Local epic or
> make the runtime decision — that is E33.2.`). **E33.3** only consumes E33.2's data and does not
> execute additional runs (`Non-Goals: Re-run or re-scope E33.2... No new Agentic/Local run`)."

**Quotation accuracy checked.** Every epic quotation in both runs was verified verbatim against the
committed specs (`4b4851b`, `fc9043f`, `612fbaa`), including E33.2's AC "across the four dimensions",
E33.1's AC "third enrolled project", both Non-Goals blocks above, and the suite clause "(363
baseline, no new skips)". **No fabricated citations** — notable from a 25,195-token packet.

**False alarms: 0.** Both runs marked the remaining seven DoD items and five ACs as guaranteed, which
is correct; neither asserted a covered requirement to be uncovered.

## Defect 2 — E33.2 Run A false-positive completion → **CATCH**

Ground truth: REJECT. Exit 0, `status: completed`, `iterations: 0`, empty transcript, zero files
changed, required test file absent.

**Run 1** — verdict `REJECT`:

> "The repository inspection shows `git status --porcelain` produces no output, `git diff` is empty…
> The file was not modified." … "**Step 3 (Create test file):** … the inspection explicitly reports
> `ls: cannot access 'tests/test_public_api.py': No such file or directory`."

> "**Misleading Exit Code:** The metadata shows `"exit_code": 0`. This suggests the runner process
> itself terminated normally, but it does not guarantee the tool calls succeeded."

**Run 2** — verdict `REJECT`, citing the two sharpest signals directly:

> "the metadata shows `"iterations": 0` and an empty `"transcript": []`. This confirms the agent
> never entered an execution loop or invoked the tools against the filesystem."

> "It appears the model generated a static response containing planned tool calls, but the runner
> either lacked a tool-execution step, failed to serialize the calls into actions, or operated in a
> read-only/ephemeral context that discarded changes before persistence."

**Recorded inaccuracy (not a false alarm).** Run 1 hypothesised the empty `"old": ""` argument caused
the failure — *"It is highly likely the runner's wrapper rejected this malformed edit command"*. The
actual cause was the runner reading fenced-JSON prose as a final answer (the SN-3 failure mode). This
is a hedged causal guess about a mechanism, not an asserted defect in the material under review, so
it does not meet the rubric's false-alarm definition. Recorded because it bears on how far such
reasoning should be trusted. Run 2's parallel hypothesis was correctly disjunctive and included the
true cause among its alternatives.

## Defect 3 — E33.4 false-negative completion → **CATCH** (inverse direction held)

Ground truth: ACCEPT. Exit 2 / `max_iterations_exceeded`, but every DoD step executed, suite
274 → 275 with 0 failures, diff exactly as specified.

**Run 1** — verdict `ACCEPT`:

> "The metadata shows `exit_code: 2` with `"status": "max_iterations_exceeded"`, which is a standard
> runner artifact indicating the agent consumed its iteration budget but explicitly reported
> successful completion before stopping. Since all objectives were met, verified, and tested, this
> non-zero exit code does not indicate task failure."

**Run 2** — verdict `ACCEPT`:

> "the non-zero runner exit code is an infrastructure limit artifact that does not invalidate the
> correctly delivered and tested code."

> "The denied `grep` command was gracefully handled via fallback `read_file` calls, and the large
> context replacement in the spec file's `edit_file` call, while verbose, achieved the precise
> structural change requested."

**Pre-registered sub-flag — did it address the exit status?** **Yes, both runs**, explicitly, and
explained why it does not block acceptance. Recorded as pre-registered, and deliberately **not**
promoted into the score.

**False alarms: 0** — and specifically **no REJECT**, which for this packet would have been the false
alarm the inverse control exists to detect. Both runs also confirmed the out-of-scope file
`app/models/financial_event.rb` was untouched, which the spec required.

## Defect 4 — M34 footboard dirty-entry miscount → **CATCH**

Ground truth: the notice claims 21 entries (2 modified + 19 untracked); the porcelain it summarises
holds 20 (2 + 18). The identity claim it supports is **correct** — condemning that would be a false
alarm.

**Run 1** — verdict `REJECT`:

> "**Status:** Does not hold. A direct count of the provided pre-state `git status --porcelain` output
> shows exactly **20 lines**, comprising **2 modified tracked** files … and **18 untracked** items …
> **Correct value:** 20 entries: 2 modified tracked + 18 untracked."

**Run 2** — verdict `REJECT`:

> "Counting the lines in the provided pre-state evidence yields exactly **20 entries**: `2` modified
> (` M`) and `18` untracked (`??`). The notice incorrectly inflates both the untracked count and the
> total by one."

**False alarms: 0.** Both runs explicitly affirmed the claim the count supports rather than
condemning it — run 1: *"'identical to the pre-state, line for line' → **Holds.**"*; run 2:
*"All other claims are accurate and properly supported by the evidence."* This was the trap built
into the packet, and both runs avoided it.

## Defect 5 — P10-GH-6 starter-lint false positive → **SPLIT** (counts as not a catch)

Ground truth: the **test** is wrong, not the document. Rubric CATCH requires recommending a change to
`tests/test_starter_lint.py`, **or** stating line 111 is not a mistake *and must not be changed*.

**Run 1 — MISS.** It diagnosed the mechanism correctly and answered the mistake question correctly:

> "**Is it a mistake?**: No. Line 111 correctly points to the `milestone/M1` branch in the external
> `footboard` repository … The linter's regex matches the syntax literally and lacks repository
> scoping."

But its prescription was to edit the document, not the test:

> "**What should be changed & why**: Update line 111 of
> `docs/phases/P10__…/P10-M34-E34.2__epic-execution-chat-starter.md` to disambiguate the cross-project
> reference. Change ``milestone/M1`` to a namespaced form like ``footboard/milestone/M1``…"

That is the MISS clause verbatim ("the conclusion is that the starter must be corrected"). It is also
precisely the workaround E34.2 applied and which its own carry-forward note calls *"a workaround in
one document, not a fix."*

**Run 2 — CATCH.** Same prompt, same settings, opposite prescription:

> "**What should be changed & why:** The fix should be applied to **`tests/test_starter_lint.py`**,
> not the starter document. The `BRANCH_RE` regex and `find_branch_typos()` function blindly match any
> `milestone/M\d+` token regardless of surrounding context, causing false positives when external
> projects or legacy examples are described in prose."

It offered the namespacing workaround only as a conditional stopgap and explicitly subordinated it:
*"the architectural fix remains refining the linter's context awareness."*

**Scored SPLIT → not a catch**, per the rubric's pre-registered disagreement rule. **False alarms: 0.**

**Why this is the most informative result in the set.** Both runs reached the same *diagnosis* and
diverged on the *remedy* — one prescribing a documentation edit that leaves the defect armed for the
next cross-repo epic, the other prescribing the real fix. A single run of this packet would have
reported a clean catch or a clean miss with equal confidence. The seed was deliberately left unfixed
and two runs pre-registered precisely so this would be visible rather than averaged away.

---

## Observation — `Getawayinsured2023`, and what it does not show

Harvested **read-only**; that project was **not modified** (working tree clean, unchanged by this
Epic). **This evidence is that project's alone until corroborated**, and harvesting an override never
retroactively converts it into a fleet standard. Its `.ai-project.yml` is a **legitimate override**
per the yml-spec's defaults-provenance note — not a defect, and not to be "fixed".

Its `models:` block, verbatim as observed on branch `chore/framework-v7.0.0-bump` @ `c282475`:

```yaml
models:
  creation: remote:kimi-k3
  hq: remote:kimi-k3
  phase: remote:qwen3.6:27b
  milestone: remote:qwen3.6:27b
  epic_dev: local:qwen3-coder:30b
  epic_qa: local:qwen3-coder:30b
  epic_manual: local:qwen3-coder:30b
```

**A correction to the framing this Epic inherited.** The E35.5 spec motivates the candidate by noting
`qwen3.6:27b` is "the model `Getawayinsured2023` actually routes its `milestone` key to, which is the
whole reason a natural experiment exists." That is true of the **model** — and the locality prefix is
**`remote:`**, not `local:`. So this configuration corroborates the *model* selection; it is **not**
evidence that a *local* model holds the Milestone level anywhere in the fleet. The back-test above,
run against a genuinely local endpoint, is the only local-inference evidence this Epic produces.
