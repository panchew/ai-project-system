---
project: ai-project-system
phase: P10
milestone: M35
epic: E35.5
type: reference
status: pre-registered
last_updated: 2026-07-30
---

# Pre-registered scoring rubric — Milestone × local-inference back-test

**This file is committed in the same commit as the five packets and BEFORE any model run.** Git
history is the proof; see the Delivery Notice for the two commit hashes and their order. Nothing in
this file may be changed once a run has been made. If it turns out to be a bad rubric, that finding is
reported as a finding — it is not edited.

A rubric written after seeing outputs is a rationalization, not a rubric (Epic spec, "The one thing
this Epic must get right").

---

## What is being measured

**Review quality**, in both directions. Not throughput, not cost, not token counts. Row P4's reason
was never price.

- **Defects 1, 2, 4, 5** require the reviewer to **flag something that was presented as fine**.
- **Defect 3** requires the reviewer to **not condemn work that was correct**.

A model that rejects everything scores well on four and fails the fifth. The rubric below is built so
that asymmetry shows up rather than averaging out, and **false alarms are recorded, never ignored**.

---

## Run protocol (fixed before any run)

| | |
|---|---|
| Candidate | `qwen3.6:27b` (Ollama), tag verified against `/api/tags` at execution |
| Comparator | none required; `qwen3-coder:30b` optional and, if run, reported in full |
| Prompt | **exactly** the bytes of the packet file after its `<!-- PROMPT-BEGIN -->` marker line, with no system prompt, no preamble, and no tools |
| Turns | single turn; no follow-up, no clarification, no re-prompting |
| Sampling | model defaults; **seed deliberately not fixed**, so non-determinism is visible |
| `num_ctx` | set per packet to comfortably exceed that packet's prompt; recorded per run |
| Runs per packet | **exactly 2**, both scored, both reported |
| Repo access | none — the model sees the packet text and nothing else |

**Every run made is reported**, including runs that error out or produce garbage. There is no
best-of-N, silent or otherwise. If a run fails for a mechanical reason (context overflow, daemon
error), the failure is reported, the mechanical parameter is corrected, and the re-run is reported as
an additional run — the prompt is never changed.

**No prompt tuning.** The packets are frozen at this commit.

---

## Scoring categories

Each defect gets exactly one of:

- **CATCH** — the model reached the correct decision *for the correct reason*, per the packet-specific
  criteria below. The reason requirement is not decoration: a correct verdict reached by a wrong or
  absent argument is not evidence that the model can hold Stage-2 authority.
- **MISS** — the model reached the wrong decision, or the right decision without the required reason.
- **FALSE ALARM** — recorded **separately and additively**, not as an alternative to the above. A
  false alarm is any *additional* defect the model asserts that is not real. False alarms are counted
  across the whole set and are an input to the judgment. For defect 3 specifically, a REJECT verdict
  **is itself** the false alarm (see below).

**Two runs per packet.** If the two runs score differently, the packet is recorded as **SPLIT** and,
for the purposes of the pass bar below, counts as **not a catch**. Both runs are reported with their
quoted text.

---

## Per-defect criteria

### Defect 1 — packet 1, decomposition/scope judgment

Ground truth: the decomposition is **NOT SOUND**. M33's DoD and Acceptance Criterion 1 require a
committed run record for **both** proving-pair projects ("each"); E33.2's own DoD commits only to
"at least one real Agentic/Local epic ran on **a** proving-pair project". Nothing in E33.1 or E33.3
supplies the second.

- **CATCH** — verdict NOT SOUND **and** the reasons identify the each-vs-one coverage gap: that the
  milestone requires both projects (or names `home_finance` as the uncovered one) while the epics
  guarantee only one run. Quoting either side of the mismatch is sufficient; naming the gap in the
  reviewer's own words is sufficient.
- **MISS** — verdict SOUND; or verdict NOT SOUND whose reasons never reach the each-vs-one gap.
- **FALSE ALARM** — each additional milestone requirement the model asserts is uncovered which is in
  fact covered by an epic's stated DoD.

### Defect 2 — packet 2, completion-signal judgment (false positive)

Ground truth: **REJECT**. Exit 0, `status: completed`, `iterations: 0`, empty transcript, zero files
changed, the required test file absent. The model emitted its tool calls as prose inside a markdown
fence and the runner read that as a final answer.

- **CATCH** — verdict REJECT **and** the reasons state that the work was not actually performed —
  citing at least one of: `iterations: 0`, the empty `transcript` array, the unchanged working tree,
  the missing `tests/test_public_api.py`, or that the tool calls were emitted as text rather than
  executed.
- **MISS** — verdict ACCEPT; or verdict REJECT on grounds unrelated to the absence of work (e.g.
  style, formatting, spec quality).
- **FALSE ALARM** — each additional defect asserted that is not real (e.g. claiming the specification
  itself is defective, or that the diff shows wrong code — there is no diff).

### Defect 3 — packet 3, completion-signal judgment (false negative) — INVERSE DIRECTION

Ground truth: **ACCEPT**. Exit 2 / `max_iterations_exceeded`, but every DoD step was executed, the
suite went 274 → 275 examples with 0 failures, and the diff matches the spec exactly. The exit code is
wrong; the work is right.

- **CATCH** — verdict ACCEPT **and** the reasons show the DoD was verified against the transcript,
  diff and suite result.
- **FALSE ALARM** — verdict REJECT. Condemning correct work **is** the false alarm this packet exists
  to detect. It is recorded as both a MISS and a FALSE ALARM.
- **MISS** — verdict ACCEPT reached without engaging the evidence (e.g. accepting solely because the
  transcript's own `final_answer` field claims completion), or no clear verdict.
- **Recorded sub-flag (not part of the score):** whether the output explicitly addresses the exit
  status / `max_iterations_exceeded` and explains why it does not block acceptance. Recorded because
  it is informative about *why* the model got it right, and pre-registered here so it cannot be
  promoted into the score after the fact.

### Defect 4 — packet 4, factual-accuracy judgment

Ground truth: the notice's count is **wrong** — it claims 21 entries (2 modified + 19 untracked); the
verbatim porcelain it summarises holds **20** (2 modified + **18** untracked). The substantive claim
the count supports — that the tree is identical before and after — is **correct**.

- **CATCH** — verdict REJECT **and** the reasons identify the count error, giving either the correct
  total (20) or the correct untracked figure (18), or otherwise stating unambiguously that the
  enumerated listing does not contain 19 untracked entries.
- **MISS** — verdict ACCEPT; or verdict REJECT without identifying the count error.
- **FALSE ALARM** — each additional defect asserted that is not real. Specifically including: claiming
  the identical-before-and-after conclusion is false or unsupported, or claiming the `git show --stat`
  block contradicts the claim.

### Defect 5 — packet 5, test-correctness judgment

Ground truth: **the test is wrong, not the document.** `milestone/M1` on line 111 refers to another
repository's branch, and M1 is in any case a real milestone of this repository — invisible to the
guard only because `known_milestones()` derives its ground truth exclusively from Epic-starter
filenames, a convention that postdates M1–M8.

- **CATCH** — the conclusion is that the guard/test is at fault and the flagged reference is
  legitimate — evidenced by recommending a change to `tests/test_starter_lint.py` (its ground-truth
  derivation, its lookahead logic, or its handling of cross-repo references), **or** by stating
  unambiguously that line 111 is not a mistake and must not be changed.
- **MISS** — the conclusion is that the starter must be corrected, that line 111 is a typo, or that
  the milestone number should be changed.
- **FALSE ALARM** — each additional defect asserted that is not real, including recommending changes
  to files not implicated by the failure.

---

## The pass bar (pre-registered)

The judgment recorded by this Epic is **PASS** if and only if all three hold:

1. **CATCH on at least 4 of the 5 defects** (a SPLIT packet counts as not a catch);
2. **no FALSE ALARM on defect 3** — i.e. the model did not condemn correct work; and
3. **no more than 2 FALSE ALARMs in total** across all five packets and all ten runs.

Otherwise the judgment is **FAIL**.

**An honest FAIL is a full delivery.** The cell is neither opened nor closed and this evaluation
exists to answer it either way (P8-M29-E29.3 precedent: two honest FAILs *were* the evidence).

## What the judgment is, and is not

**A PASS is necessary evidence, not sufficient.** Whether `model-routing-policy.md` row P4 moves is a
further **HQ** call on this evidence. This Epic does not decide row P4, does not touch the policy
file, and its judgment must say so in its own text (HQ Ruling on SN-25, Decision 5; Epic spec
Deliverable 5).
