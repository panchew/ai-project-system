---
type: milestone-closure-declaration
milestone: M39
status: complete
completion_date: 2026-08-16
declared_by: Milestone Chat (P11-M39 — Trustworthy Completion Signal)
issued_to: Phase Chat (P11 — Drivr: Coordination over Rented Execution)
is_final_milestone: false
---

# MILESTONE CLOSURE DECLARATION — M39

Milestone **P11-M39 — Trustworthy Completion Signal (P10-GH-7)** is hereby declared **COMPLETE
(awaiting consolidation)**. Three epics — **E39.1, E39.2, E39.3** — were executed, independently
re-measured by this Milestone Chat, and merged to `milestone/M39` with explicit human merge
authorization for each (SN-19 / PSG §11.6, and §11.6.1's CFO diff review satisfied on all three).

**M39 is NOT P11's final milestone.** After Phase Chat review and consolidation into `phase/P11`, the
Phase Chat proceeds to **M40 planning — Coordination**. `phase/P11` is not merged to `master` at this
closure.

Final verification on `milestone/M39` @ `c67d8332d0f29a6edf250c6912cd4333c9ad7c3a`:

```text
ai-project-system: PYTHONPATH=. pytest -q      (bare `pytest` fails collection)
                   510 passed in 34.22s        (baseline 489 + 21 from E39.3)

drivr @ 715099cb94a9f7c010cde1c22e455d4b41161a14:
                   249 passed in 1.11s         (baseline 47 at 31dad51 + 202 from E39.1)
```

**`P10-GH-10` did not fire** in any full-suite run performed during this milestone. Nothing is being
withheld under its both-results obligation. Clean runs do not disprove its ~3-in-10 rate.

**Cross-repo access, stated because a reviewer needs it:** **drivr has no git remote.** *"Verify the
push at `origin`"* is performable for `ai-project-system` and **not performable for drivr**. A G2
reviewer must re-measure drivr on this machine at `715099c`.

---

## 1. The judgment's mechanism, and what it reads

**The mechanism is ordering.**

> **A verification is evidence about the state a run left behind only if no effect follows it.**

That single rule separates the two runs in the corpus that agree on every signal the fleet had ever
read — same `status`, same exit code, same iteration count, same prose shape:

| Case | last effect | last verification | Verdict |
|---|---|---|---|
| E33.2 Run B | **#9** `edit_file` | #5 `pytest -q` → exit 2 | `EFFECTS_UNVERIFIED` — the test is **stale** |
| E33.4 | #5 `edit_file` | **#6** `bundle exec rspec` → exit 0 | `EFFECTS_VERIFIED` |

**What it reads:** an ordered effect ledger projected from the run's own tool-call/tool-result stream,
and `files_changed` — a before/after snapshot delta — when one exists.

**What it does not read, each disqualified by measurement during this milestone:**

| Signal | Why it is out |
|---|---|
| **exit code** | wrong in both directions (P10, restated) |
| **`status`** | wrong in both directions — Run A reports `completed` on zero work |
| **`final_answer`** | wrong in both directions — `P7-M26-E26.3-PROVE` returns a flat refusal on a run that converged attempt 1/3 |
| **naive repository-state delta** | **fails Run A**: `local-agent-runner` gained `4ec1e8f` 4 min 58 s *after* Run A ended, carrying Run B's work |
| **any model-generated judgment** | binding decision, E39.1 — see §5 |

**Every signal in the milestone spec's original table is disqualified standalone.** That is the true
shape of the problem and it was not visible when the milestone opened; three of the four were
falsified by measurement during planning and execution, and each falsification amended the governing
spec rather than being worked around.

**Constraint 2 is enforced structurally, not by intention.** The rules live in
`_decide(ledger, files_changed)`, whose entire parameter list is those two values. It is never handed
an `EvidenceRecord`, so the annotations mapping carrying the exit code and `status` is **unreachable
from inside it**. A test asserts the parameter list. Verified independently by this chat.

**Vocabulary:** five `Completion` members and a three-valued `Reading`, which **structurally cannot
collapse to a boolean**. `None` ≠ `()` is load-bearing: an observed-empty ledger (Run A) reaches
`NO_EFFECTS_OBSERVED`; no ledger observed reaches `INDETERMINATE`.

---

## 2. Both known-case verdicts, and the tuning disclosure

| Case | Verdict | `Reading` | Rule | Required | Result |
|---|---|---|---|---|---|
| **E33.2 Run A** | `no-effects-observed` | `did-not-complete` | `no-effects` | *did not complete* | **PASS** |
| **E33.4** | `effects-verified` | `completed` | `covering-verification` | *completed* | **PASS** |

**Constraint 1 is discharged.** *A design that cannot be shown against both is not delivered* — it was
shown against both, from the committed artifacts, through the real mechanism.

**Post-hoc tuning: NONE, and this is checkable rather than asserted.** E39.2 pre-registered the
mechanism's SHA in **its own commit (`bc89db5`), which contains only the evidence artifact — the
harness did not yet exist**, so the ordering is recoverable from `git log` rather than from prose. The
pre-registered and final SHAs are identical:

```
git -C /home/panchew/soft-dev/drivr diff 715099cb94a9f7c010cde1c22e455d4b41161a14 HEAD -- drivr/judgment/
```

**Empty output is the whole proof.** Re-verified by this Milestone Chat at closure: still empty.

**E33.4's covering verification is iteration #6 — the same iteration E33.4's own run-record
independently names as where the work went green**, reached by the mechanism without being pointed at
it.

---

## 3. The limits — reproduced in full, because M40 inherits them with the verdicts

1. **Two cases falsify and do not generalize.** The pair shows the judgment is not wrong where every
   prior signal was. It does not show it is right in general.
2. **The corpus is imbalanced five to one** — five *completed*, one *did not complete*.
3. **A mechanism that always answers *completed* scores 5/6 and 1/2 on the binding pair.** The
   judgment scores **2/6 strict** and **2/2 on the binding pair**. **On strict scoring it loses to
   the degenerate baseline**; on contradictions it beats it (**0 vs 1**). Always-*undetermined* scores
   0/6 with 0 contradictions. **Neither degenerate strategy dominates the judgment and it dominates
   neither.**
4. **There is exactly one negative case in the whole corpus.** One case is not a false-positive rate.
5. **Every case comes from one runner (`local-agent-runner`); none from OpenCode. Engine generality is
   untested — not weakly supported, untested.** Worse for M40: a live OpenCode run projects
   `effect_ledger=None`, so **it can never reach `EFFECTS_VERIFIED`.** The engine on today's roster
   cannot produce the positive verdict this milestone validated.
6. **`undetermined` on four of six is a real operational limit.** A coordinator wanting yes-or-no gets
   neither, two thirds of the time on corpus-like runs. **If M40 escalates on `undetermined`, ~67% of
   corpus-like runs escalate** — adjacent to the *"constant false escalations, the human becomes the
   bottleneck again"* failure this milestone exists to prevent, reached through undetermined answers
   rather than wrong ones.
7. **Result-string matching is one runner's vocabulary.** A wording change degrades the ledger to
   `UNCLASSIFIED` — visible, not silent.
8. **E39.2's validation is historical** — six stored transcripts, no new runs.

**A seventh case arrived after the mechanism froze** — see §4. It is the only evidence in this
milestone that could not have been overfitted to, because it did not exist when the mechanism was
written.

---

## 4. G11 — unambiguous status

> **G11 is CLOSED**, on the run captured at `.ai-project/artifacts/agentic-runs/P11-M39-E39.3/`,
> dispatched on the host on 2026-08-16 under `.ai-project.yml`'s `models.epic_qa`
> (`local:qwen3-coder:30b`), with the read-only tool set `.ai-project/agents/qa-tools.json`
> (`sha256 83ff08e7…`), via `bin/run-qa-agent` — a QA-role dispatch **built in E39.3**, because E39.1
> built none by its binding decision.

It is **not** claimed by inference, **not** by a relabelled dev-lane run, and **not** from E39.2's
validation. This Milestone Chat verified the relabelling prohibition from committed artifacts rather
than from the epic's account: the task text is `QA_TASK_TEMPLATE`, **not** `extract_dod`
(`extract_dod` is imported only to read *the standard being judged*), and the committed tool set
enables `read_file` and `list_dir` only.

**The three-phase-old gap is closed. What G11 stood for is not delivered, and the two must be read
together.**

### The finding, stated before the closure it qualifies

**The first `epic_qa` run ever captured returned `VERDICT: PASS` on all 26 rules of its standard
having made zero tool calls.** It cited `read_file('.ai-project.yml')` on every line — including a
line about a `framework_version` field **that file does not contain**, and four lines asserting
*validation behaviour* that reading a config file cannot show at all. **Reproduced on a second
identical dispatch.** Both runs: `iterations: 0`, `status: completed`, exit 0.

**This is Run A's failure mode, in the QA role.** The lane that was supposed to supply an independent
trustworthy signal reproduced, on its first exercise, the exact false positive that opened P10-GH-7 in
the dev role.

> **G11 closed ≠ a trustworthy independent signal exists.** The lane now runs. Its output, on the
> only evidence available, cannot be trusted on its own. **No reader may take this closure as
> evidence of the latter.**

**Narrow evidence, stated as such:** one QA task shape, two runs. Not a claim about
`qwen3-coder:30b` in `epic_dev`, where E33.2 Run B and E33.4 recorded real tool use.

### The closing loop — and the design rule M40 should inherit

This Milestone Chat ran **E39.1's completion judgment against E39.3's own QA runs**:

```
P11-M39-E39.3       -> NO_EFFECTS_OBSERVED   DID_NOT_COMPLETE   rule=no-effects
P11-M39-E39.3-RUN2  -> NO_EFFECTS_OBSERVED   DID_NOT_COMPLETE   rule=no-effects
```

**M39's own mechanism catches M39's own fabricated QA verdict** — the same verdict Run A receives.
This is a **seventh corpus case, created after the mechanism froze at `715099c`**, and it is stronger
anti-overfitting evidence than the four held-out cases, which already existed when the mechanism was
written.

> **Design rule for M40: never read a QA verdict without first running the completion judgment on the
> QA run that produced it.** The five-criterion bar establishes that a run is *genuine*; the
> completion judgment establishes whether any *work happened*. **Neither is sufficient alone.
> Composed, they catch this case.**

---

## 5. The QA-pass coupling — decided in planning, consumed in execution

Settled by this Milestone Chat at planning time under the Starter's Question Policy, and **binding**:

> **The verdict MUST NOT be load-bearing on any model-generated judgment.**

**Rationale, which the milestone then proved by measurement:** this milestone exists *because* model
self-report is untrustworthy in both directions. A QA-role second pass is another model reading prose.
**E39.3's fabricated PASS is that reasoning confirmed on the first real QA run ever captured** — the
decision was made from principle in advance and vindicated by evidence afterwards.

E39.1 therefore built **no** QA-role dispatch path; E39.3 built one **on its own terms**, consuming
the decision rather than discovering it. `model-generated judgment` appears on every verdict in the
`ignored` list with its reason, so a reader can see it was considered and excluded. **No speculative
seam was built.**

**The coupling was decided in planning and consumed in execution — not discovered at execution.**
That was the milestone spec's explicit requirement and it held.

---

## 6. Nothing from M40 was built

**No scheduler. No derived gate queue. No thin surface. No signed one-time-link approval. No
competing-model review.**

`judge_completion` is a **pure function** — a record in, a verdict out. No I/O, no state, no
filesystem writes, no network, no notification, no queue; pinned by `test_judgment_is_pure`. E39.3's
QA verdict **triggered nothing**: it is recorded `"authority": "advisory"` and nothing reads it.

**The Hard Constraint held. M39 judged and did not act.** The M40 gate is intact: a judgment exists
and nothing consumes it yet.

**Also untouched:** `model-routing-policy.md` **row P4** (M38's evidence findings used as inputs, not
promoted — constraint 5); the four §4-invalid enrolled configs; the two open `bin/ai-project-init`
defects; `P10-GH-10`; the orchestrator's retry/feedback/escalation behaviour. **Drivr still rents** —
nothing added owns inference, a model loop, or an agent client.

**Constraint 7 — no Structural diagram is owed by any of the three deliveries.** None amended a
normative document in this repository. Each epic stated this explicitly, as the constraint directs.
The epic specs' own proposed-track diagrams remain the governing visuals.

---

## 7. Carry-forwards to the Phase Chat

**1. `exit_code` is classified `ignored` when for a transcript it is `absent`** *(drivr, from E39.2's
Finding 2; this chat ruled it slightly larger than reported)*. The transcript projection has **no
channel** for the exit code — injecting `exit_code: 999` leaves `annotations` byte-identical on all
six cases — so the verdict's `[ignored] exit_code … verbatim: 'None'` line **records absence and
reads as rejection**. drivr already has an ABSENT disposition and applies it correctly to
`files_changed` and `environment`. **The fix is to use it on the transcript path.** Brushes E39.1's
AC4. **E39.1 was deliberately not reopened** — the verdicts are correct, E39.2's evidence artifact and
harness (`exit_code_channel_absent=True`) document it permanently, E39.3 was forbidden from touching
drivr, and this chat may not implement code. **The risk this carries is a future reader citing that
line as proof of constraint 2 — which would be exactly the vacuous independence the milestone named.**

**2. ID allocation for the fabricated-verdict finding — ESCALATED, not allocated.** `P11-GH-3` is
**genuinely contested**: `P11__carry-forward-note__P11-GH-2-….md` declines to file a different pattern
under that ordinal and refers the call to the CFO. E39.3 correctly declined to self-assign; this chat
declines equally. **Recorded by artifact + defect meanwhile** — *the `epic_qa` lane's first two
captured runs returned a fabricated `VERDICT: PASS` with zero tool calls*, artifacts at
`.ai-project/artifacts/agentic-runs/P11-M39-E39.3/` and `…-RUN2/`. **Phase Chat to allocate.**

**3. The five-criterion bar checks genuineness, not groundedness** — **this Milestone Chat's own
spec limitation**, not the epic's. The criteria were optimized for checkability ("was `write_file`
enabled?" is a question about a committed file); groundedness is a different property and the gap was
not named. E39.3 found it and reported it rather than resting on a clean close. **Mitigation already
identified: compose the bar with the completion judgment (§4).**

**4. Single-adapter dependency.** The ordered ledger exists only for `local-agent-runner` transcripts.
**A live OpenCode run can never reach `EFFECTS_VERIFIED`.** Closing this means an adapter that
projects an ordered ledger — OpenCode's `--format json` stream is the obvious candidate. **It was not
built**, deliberately; nothing in this milestone needed it.

**5. Runner availability is shimmed, not installed.** A durable install is blocked on this host under
**PEP 668**; `--break-system-packages` was declined as out of scope. `bin/local-agent-runner-shim` is
committed and a reader can open it — an improvement on five preserved runs naming scratchpad wrappers
that no longer exist. **Limitation: the runner checkout is on a feature branch
(`local-agent-runner` `4ec1e8f`, `epic/cf-2-public-run-api`), and the shim pins the invocation, not
the runner's version.**

**6. Corpus inventory is now a floor of seven directories / six runs with ground truth**, re-counted
by **three different chats** across this milestone (2 → 6 → the §F3 exposure table → 7 directories).
The milestone spec opened with two.

**7. `P10-GH-10` remains open and unfixed.** It did not fire during this milestone. Not M39's.

---

## 8. Definition of Done — milestone level

- [x] E39.1–E39.3 each meet their own DoD, verified by independent re-measurement (G2)
- [x] All three epic branches merged to `milestone/M39` (`a2ba2c7`, `4f09ee5`, `c67d833`)
- [x] A completion judgment exists resting on **neither the exit code nor `status` alone** — and, as
      measured here, on neither `final_answer` nor a naive repository-state delta either
- [x] **Validated against both known cases** — Run A → *did not complete*, E33.4 → *completed* — with
      evidence committed and **no post-hoc tuning**, checkable by one empty diff
- [x] **The two-case limit is stated**, with six further limits (§3)
- [x] **G11's status is unambiguous — CLOSED**, on a named run, with the finding that qualifies it
      stated first (§4). **Never claimed by inference.**
- [x] The QA-pass coupling was decided in E39.1's planning and consumed by E39.3 (§5)
- [x] **Nothing from M40 was built** (§6)
- [x] Row P4 untouched; M38's evidence findings used but not promoted
- [x] Structural diagram — **none owed**; no delivery amended a normative document
- [x] Suites green with baselines named per repo; `P10-GH-10` did not fire
- [x] **Milestone Closure Declaration produced AND COMMITTED** — M38's was authored and left untracked
      until the Phase Chat caught it at consolidation

---

## 9. Acceptance Criteria — milestone level

1. **A run's completion can be judged without the exit code or `status` alone**, and the judgment
   carries its evidence — **met**, and the disqualified set is larger than the milestone anticipated.
2. **Both known cases read correctly**, from the committed transcripts, through the real mechanism —
   **met**, with no tuning, provably.
3. **The signal's limits are stated** — **met**, eight items, including that the judgment loses to the
   trivial baseline on strict scoring.
4. **G11's status is unambiguous** — **met: CLOSED**, with the finding that the lane's output cannot be
   trusted stated adjacently and first.
5. **The M40 gate is intact** — **met**: a judgment exists and nothing consumes it.
6. **Suites green, baselines named per repository** — **met**.

---

## 10. What this milestone actually established

**M35's handback rule had no detector beneath it from the day it was recorded. It has one now.**

But the more useful result is the one nobody planned: **the milestone's own QA lane fabricated a
verdict on its first exercise, and the milestone's own mechanism caught it.** The completion judgment
was validated against six historical runs it might have been fitted to, and then against a seventh
that did not exist when it was written — produced, by accident, by this milestone's last epic.

**Three times during M39, measurement falsified something a governing spec asserted** — the Phase
Chat's repository-state-delta direction, the `final_answer` tell, and this chat's own genuineness bar.
**Each time it returned as an amendment or a named carry-forward rather than a quiet fix.** That is
the process working as designed, and it is why the signal handed to M40 comes with its limits attached
rather than with confidence attached.

**M40 inherits a judgment that never answers falsely, defers two thirds of the time, cannot reach its
positive verdict on the engine actually on the roster, and must not be built over without reading §3
and §4 together.**

---

**Declared by:** Milestone Chat (P11-M39 — Trustworthy Completion Signal)
**Issued to:** Phase Chat (P11 — Drivr: Coordination over Rented Execution)
**Date:** 2026-08-16
**Branch:** `milestone/M39` @ `c67d8332d0f29a6edf250c6912cd4333c9ad7c3a`
**Next:** Phase Chat review and consolidation into `phase/P11`, then **M40 planning — Coordination**.
