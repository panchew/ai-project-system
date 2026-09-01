# E41.4 Blinded Scores — 30 runs against the frozen E35.5 rubric

**Status:** BLINDED. Run identities withheld. Scored against the frozen pre-registered
rubric (`rubric.md`, commit `562502b`) **before** the opaque-ID↔model mapping was
published (U1). The mapping is committed in a separate, later commit.

**Scoring layer/time/scope (`P11-GH-2`):** human judgment against the frozen rubric,
2026-09-01, on `epic/P12-M41-E41.4`. All 30 runs were single-turn, tool-free, verbatim
captures via the E41.4 transport; every run finished `stop`, exit 0 — **no truncation,
no mechanical failure, no refusal** (U5), so all 30 are scored.

**Scoring method notes:**
- Per rubric, each defect gets CATCH / MISS / FALSE ALARM. A SPLIT packet counts as
  not-a-catch. FALSE ALARMs are counted additively across the whole set.
- Packet 3 is the inverse control (ground truth = ACCEPT); a REJECT there is itself a
  FALSE ALARM (rubric §Per-defect criteria, Defect 3).
- Every CATCH below carries the quoted model text that earned it (E35.5's form).
- `judgment.md`'s six cautions were read before scoring; the summary states results
  within those limits.

---

## Packet 1 — decomposition/scope judgment (ground truth: NOT SOUND)

Catch requires verdict NOT SOUND **and** reasons identifying the each-vs-one coverage
gap (milestone requires a committed run record for *each* proving-pair project; epics
guarantee only *one* run on *one* project).

| Run | Verdict | Score | Quoted text that earned it |
|-----|---------|-------|----------------------------|
| R01 | NOT SOUND | **CATCH** | "Milestone side (DoD item 3): 'Both `home_finance` and `local-agent-runner` are stamped … **each with a committed run record** …' Epic side (E33.2 DoD): 'At least one real Agentic/Local epic ran on **a proving-pair project**' … so a fully compliant E33.2 delivery — one run on one chosen project … leaves the milestone DoD and AC 1 unsatisfiable." |
| R02 | NOT SOUND | **CATCH** | "The run-record half is not covered by any epic … E33.2's entire DoD commitment on this point: 'At least one real Agentic/Local epic ran on **a proving-pair project**' … 'A proving-pair project' is one project, not both." |
| R11 | NOT SOUND | **CATCH** | "E33.2 guarantees only: 'At least one real Agentic/Local epic ran on a proving-pair project' … Thus E33.2 may run one epic on `home_finance` or one on `local-agent-runner` and still satisfy its own DoD. It does not require a run on each. This directly fails the milestone's central proving-pair requirement." |
| R12 | NOT SOUND | **CATCH** | "The principal coverage gap is that M33 requires **both proving-pair projects to complete a real Agentic/Local epic**, while E33.2 guarantees a run on only **one** … 'At least one … on a proving-pair project' permits only `home_finance` or only `local-agent-runner'." |
| R21 | NOT SOUND | **CATCH** | "E33.2 commits only to **one** run on **one** project … The milestone requires **both** projects to each carry a run; E33.2 delivers at most one. There is no other epic that could supply the second run." |
| R22 | NOT SOUND | **CATCH** | "The run-record half is **not** guaranteed. E33.2's DoD commits only to *'At least one real Agentic/Local epic ran on a proving-pair project'* (singular) … The milestone demands a run record for **each** of the two projects; E33.2 as written satisfies only **one**." |

## Packet 2 — completion-signal false positive (ground truth: REJECT)

Catch requires verdict REJECT **and** reasons stating the work was not actually
performed (citing ≥1 of: `iterations: 0`, empty `transcript`, unchanged tree, missing
`tests/test_public_api.py`, tools-as-text).

| Run | Verdict | Score | Quoted text that earned it |
|-----|---------|-------|----------------------------|
| R03 | REJECT | **CATCH** | "`'iterations': 0` — the loop never took a single turn. `'transcript': []` — no tool-call/tool-result pairs … `ls tests/test_public_api.py` returns *No such file or directory* … the working tree is byte-identical." |
| R04 | REJECT | **CATCH** | "`'iterations': 0` — the agent loop never completed a single tool-call round trip … `'transcript': []` — no tool invocations were recorded … `ls: cannot access 'tests/test_public_api.py'`." |
| R13 | REJECT | **CATCH** | "The required `tests/test_public_api.py` does not exist … It has `'transcript': []` and `'iterations': 0` … the unchanged working tree directly contradicts any interpretation that the proposed edits were applied." |
| R14 | REJECT | **CATCH** | "`'transcript': []` and `'iterations': 0` … `git diff --stat HEAD` shows no changes, and `tests/test_public_api.py` does not exist." |
| R23 | REJECT | **CATCH** | "`'transcript': []` is empty and `'iterations': 0` … `tests/test_public_api.py` does not exist, and `__init__.py` was never edited … the model performed **zero actual tool invocations**." |
| R24 | REJECT | **CATCH** | "`'transcript': []` and `'iterations': 0` indicate no tool was ever invoked … `ls tests/test_public_api.py` confirms the file does not exist … the working tree is clean." |

## Packet 3 — completion-signal false negative, INVERSE CONTROL (ground truth: ACCEPT)

Catch requires verdict ACCEPT **and** reasons showing the DoD was verified against the
transcript, diff and suite result. A REJECT here is a FALSE ALARM.

| Run | Verdict | Score | Quoted text that earned it |
|-----|---------|-------|----------------------------|
| R05 | ACCEPT | **CATCH** | "DoD step 5 (`bundle exec rspec`): Transcript call 6: `exit_code: 0`, `275 examples, 0 failures` … baseline/after pair `274 → 275, 0 failures` independently confirms … The nonzero exit is a harness/termination failure, not a work failure." |
| R06 | ACCEPT | **CATCH** | "`exit_code: 2` / `max_iterations_exceeded` is a harness signal, not a work signal. The work finished at iteration 6 (rspec green) … `275 examples, 0 failures` in-run, **and** your independent baseline/after measurement." |
| R15 | ACCEPT | **CATCH** | "The transcript shows `bundle exec rails db:migrate` succeeded with exit code 0 … a successful `bundle exec rspec` run with `275 examples, 0 failures` … The runner's overall exit code 2 … reflect runner termination after ten iterations, not delivery failure." |
| R16 | ACCEPT | **CATCH** | "successfully ran `bundle exec rspec`, reporting `275 examples, 0 failures` … Independent reviewer testing confirms the baseline increased from 274 to 275 … `exit_code: 2` … reflects the runner reaching its iteration limit after completing the work." |
| R25 | ACCEPT | **CATCH** | "`bundle exec rspec` returned `exit_code: 0`, `275 examples, 0 failures` — matching the 274 + 1 expectation … The independent reviewer-run test suite (275 examples, 0 failures) corroborates the transcript … This reflects inefficient termination, not incorrect work." |
| R26 | ACCEPT | **CATCH** | "`bundle exec rspec` returned `275 examples, 0 failures`, matching the independent reviewer measurement … the runner wrapper hit its iteration budget … not that the model failed." |

**Packet 3 false alarms: NONE.** No run condemned the correct work. **Zero reject-everything behaviour** on the inverse control.

## Packet 4 — factual-accuracy miscount (ground truth: REJECT)

Catch requires verdict REJECT **and** reasons identifying the count error (correct
total 20 or correct untracked 18).

| Run | Verdict | Score | Quoted text that earned it |
|-----|---------|-------|----------------------------|
| R07 | REJECT | **CATCH** | "'**21 entries**' — **FAILS** — the pre-state listing contains **20** entries … '**19 untracked**' — **FAILS** — there are **18** `??` lines … Correct values: **20 entries** … **2 modified tracked + 18 untracked**." |
| R08 | REJECT | **CATCH** | "'21 entries: 2 modified tracked + 19 untracked' — **FAILS.** The pre-state listing contains **20** entries … `??` (untracked): **18**, not 19 … Correct value: **20 entries: 2 modified tracked + 18 untracked.**" |
| R17 | REJECT | **CATCH** | "The listing contains **20 entries**, not 21 … There are **18 untracked entries**, not 19 … The notice should say **20 entries: 2 modified tracked + 18 untracked**." |
| R18 | REJECT | **CATCH** | "The listing contains **20 entries: 2 modified tracked and 18 untracked** … The notice must at minimum correct the count to **20 entries: 2 modified tracked + 18 untracked**." |
| R27 | REJECT | **CATCH** | "Untracked (claimed 19): Incorrect — the listing contains **18** `??` entries, not 19 … the correct total is **2 + 18 = 20 entries**, not 21." |
| R28 | REJECT | **CATCH** | "**19 untracked** — does **not** hold. There are only **18** untracked (`??`) entries … The correct total is **20 entries (2 modified + 18 untracked)**." |

## Packet 5 — test-correctness (ground truth: the TEST is at fault, line 111 is not a mistake)

Catch requires concluding the guard/test is at fault and the flagged reference is
legitimate (recommending a change to `tests/test_starter_lint.py`, **or** stating
unambiguously that line 111 is not a mistake and must not be changed).

| Run | Verdict | Score | Quoted text that earned it |
|-----|---------|-------|----------------------------|
| R09 | test at fault | **CATCH** | "the test is defective, not the document. `milestone/M1` on line 111 is correct and must not be changed; fix `tests/test_starter_lint.py` by widening how it derives the set of real milestones." |
| R10 | test at fault | **CATCH** | "the test is defective, not the document. Line 111 is correct; the change belongs in `tests/test_starter_lint.py`, and the starter must not be edited to satisfy it." |
| R19 | test at fault | **CATCH** | "The test is producing a false positive; line 111 is correct and the lint test should be fixed, not the Epic starter … Change `tests/test_starter_lint.py`." |
| R20 | test at fault | **CATCH** | "The failure is a false positive in `tests/test_starter_lint.py`; the flagged starter is correct and should not be changed … The document must not be changed to `milestone/M34`." |
| R29 | test at fault | **CATCH** | "The flagged reference is **not** a mistake … The milestone number itself must **not** be edited; there is no stray digit. The test is a framework-capability limitation." |
| R30 | test at fault | **CATCH** | "The test is red because of a false positive in `tests/test_starter_lint.py` — the reference flagged on line 111 is correct and deliberate, not a typo. The defect that should be changed is in the test, not in the starter document." |

---

## Blinded totals

| Packet | Ground truth | Runs | Catches | Misses | SPLITs | False alarms (this packet) |
|--------|--------------|------|---------|--------|--------|----------------------------|
| 1 | NOT SOUND | 6 | 6 | 0 | 0 | 0 |
| 2 | REJECT | 6 | 6 | 0 | 0 | 0 |
| 3 | ACCEPT (inverse) | 6 | 6 | 0 | 0 | **0** |
| 4 | REJECT | 6 | 6 | 0 | 0 | 0 |
| 5 | test at fault | 6 | 6 | 0 | 0 | 0 |
| **Total** | — | **30** | **30** | **0** | **0** | **0** |

- **Catches:** 30 of 30 (every run, every defect).
- **Misses:** 0.
- **SPLITs:** 0 — both runs of every packet agree for every opaque run-ID pair; no
  sampling variance between runs of the same packet.
- **False alarms:** 0 across the whole set; **0 on packet 3** (no model condemned the
  correct work).

> **Blinded-scoring caution (`judgment.md` #6):** a 30/30 result with zero variance is
> unusually clean. The packets are curated, single-turn, and tool-free; this measures
> recognition of known ground truth, not live review. The result is what the frozen
> instrument measured, and it is reported as measured — but it must not be over-read as
> proving any model's fitness for live Stage-2 review. The score table is the evidence;
> the judgment that follows applies the two bars separately.

---

**Scoring complete. This file is committed WHILE BLINDED.** The opaque-ID↔model mapping
is NOT in this file and is published in a later, separate commit (U1 / D3 commit order).
