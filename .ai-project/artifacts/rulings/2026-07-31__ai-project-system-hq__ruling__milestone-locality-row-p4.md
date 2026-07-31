---
type: hq_ruling
evidence_ref: .ai-project/artifacts/reference/local-review-backtest/judgment.md
policy_ref: .ai-project/artifacts/reference/token-measurement/model-routing-policy.md
prior_ruling_ref: .ai-project/artifacts/rulings/2026-07-30__ai-project-system-hq__ruling__sn-25-handback-and-execution-matrix.md
issued_by: HQ Chat (ai-project-system)
issued_to: Creation Chat (P11 scoping), future Phase Chats
phase: P10
date: 2026-07-31
status: active
row_changed: false
---

# HQ Ruling — Row P4 Stands: Milestone Is a Candidate for Local Inference, Not an Adopter

**Evidence:** E35.5's blinded back-test of `qwen3.6:27b` (Q4_K_M) against five known-ground-truth
defects — `judgment.md`, `scores.md`, `rubric.md`, ten committed run records
**Bar it was measured against:** HQ Ruling on SN-25, Decision 5 (2026-07-30)
**Decision:** `model-routing-policy.md` **row P4 is unchanged — Milestone remains paid frontier.**

---

## Decision 1 — The cell does not open. Row P4's decision column is untouched.

Milestone × local inference is **not adopted**. Row P4 continues to read **Paid frontier**, on
the reasoning it has always carried: Milestone is where Stage-2 accept authority lives and where
errors propagate into merges.

**This is a decision, not a deferral.** The evidence I asked for in the SN-25 ruling was
produced, in full, to a higher standard than I specified. The question is answerable now, and
the answer on this evidence is no.

---

## Decision 2 — What was earned: candidacy, and it is real

The SN-25 ruling set back-testing against known ground truth as the bar for a local model to
become a **candidate** for this cell. **That bar is met.** E35.5 earned it, and the finding
should not be flattened into "local review failed," because it did not.

What the evidence genuinely supports:

- **Exit-code untrust generalises to a local reviewer.** The model rejected the exit-0-zero-work
  run and accepted the exit-2-complete-and-green run, reasoning from transcript, diff and suite
  result rather than the status code. That is precisely the two-sided judgment **P10-GH-7**
  records as measured-broken in automated detection — reached correctly, from a local model,
  in both directions. This is the most valuable single result in the artifact.
- **Zero false alarms across five packets and ten runs**, including both deliberate traps. The
  rubric was built to be able to disconfirm this and did not.
- **Citation discipline held under a 25,195-token prompt** — every quotation verified verbatim,
  no fabrications.

---

## Decision 3 — Why candidacy does not become adoption

Four reasons, in descending weight. The first is on its own sufficient.

**1. The defect-5 split is disqualifying at this level.** Two runs of the same prompt at the same
settings produced **identical diagnoses and opposite prescriptions** — one prescribing the real
fix, the other the documentation workaround that would have left P10-GH-6 armed for the next
cross-repo epic. At Milestone, **the remedy is the decision**: Stage-2 acceptance is not "was
something wrong" but "is this disposition correct." A level whose remedy depends on the sampling
draw cannot hold accept authority. The judgment is right that the headline "4 of 5" hides this,
and right to lead with it.

**2. The evaluation tests recognition; Stage-2 review is mostly search.** Each packet arrived
with the relevant material assembled and the noise removed. A live Milestone Chat must decide
*what to examine* across a branch and — the hard part — **notice what is absent**. This phase's
own best catches were absence-catches: M33's decomposition gap was a DoD bar with no epic behind
it, and E33.4 exists because someone noticed a hole rather than misread a page. Packet 1 handed
the model that gap pre-assembled. Nothing here tests the faculty that produced the original
catch.

**3. Real Stage-2 review verifies; this evaluation could not.** Single-turn, tool-free, no repo
access, no follow-up. The decisive counter-example is in this same phase: **E35.5 itself caught
the `Getawayinsured2023` false premise by going and checking it** — an act no single-turn
reviewer can perform, and the single most valuable correction P10 produced. A reviewer that
cannot verify a claim is not doing the job that makes row P4 read paid frontier.

**4. Two runs per packet detects variance but cannot measure it.** One split in five packets is
consistent with a rare divergence or a coin flip. Opening the cell on this evidence means
deciding without knowing which, at the level where being wrong propagates into merges.

**Not a reason, and recorded so it is not later mistaken for one:** the
`Getawayinsured2023` "natural experiment" does not weigh against local Milestone inference — it
simply does not exist on the locality axis, since that project routes `milestone:` to
**`remote:`**`qwen3.6:27b`. It was never evidence either way, and the phase spec claim that it
was has already been corrected (v1.3.1).

---

## Decision 4 — The bar was set honestly, and that is credited

E35.5 pre-registered **4 of 5** before any model ran, and states plainly that at a 5-of-5 bar the
result would read FAIL. My SN-25 ruling's plain language — *"catches what was caught and flags
what was missed"* — reads closer to 5 of 5 than to 4 of 5.

**HQ does not treat that gap as a defect in the epic.** Pre-registering a threshold before seeing
results is the property that makes the evidence admissible at all, and a bar chosen after the
fact to match my phrasing would have been worth less, not more. The epic reported its result
against the bar it actually wrote down, disclosed the discrepancy itself, and committed every run
including the truncated one that would have scored MISS. That is the behaviour the framework
wants, and it is why this ruling can be made in one pass on the artifact rather than requiring a
re-run.

The gap is resolved not by re-scoring but by Decision 3: even at 4 of 5 with zero false alarms,
the *shape* of the failure — split prescriptions on the one it missed — is what decides the cell,
and that would be true at 5 of 5 as well.

---

## Decision 5 — What would decide it: three named gates, so this is not permanent limbo

Row P4's cell stays open as a question. It is **not** open-ended. A future evaluation moves it by
addressing these three, and HQ will rule on evidence that does:

- **G-P4-a — Prescription variance, measured.** Enough repetitions to put a *rate* on divergence
  in the **remedy**, not merely the verdict. A candidate whose prescriptions diverge materially is
  disqualified regardless of catch rate.
- **G-P4-b — Unassisted search over a real branch.** Review that must locate what to examine and
  detect an **absence** — a missing epic against a stated DoD bar, a deliverable named in a spec
  and never produced — without the material pre-assembled.
- **G-P4-c — Iterative, tool-using review.** At minimum the ability to check a claim against the
  repository before ruling on it, as E35.5's own premise-verification did.

**Scope limits carried forward unchanged:** one model, one machine, five defects, ten runs, at
**Q4_K_M**. The parked llama.cpp + Qwen3.6 **Q8_0** stack is a different artifact and remains
parked; nothing here touches that trigger.

---

## Decision 6 — Recording, and what is not being changed

Per `model-routing-policy.md`'s **Change discipline**, rows change only with new cited evidence.
There *is* new cited evidence here, and it changes **no decision** — so row P4's decision column
is untouched. What the evidence does change is the row's *confidence/gaps* and *revisit trigger*
columns, which now cite this evaluation and name the three gates above. That edit is applied with
this ruling.

The ratified execution matrix in `chat-hierarchy.md` is **left byte-intact** — the SN-25 ruling
reproduced it "exactly as ratified," and its Milestone cell (*"Remote — local under
evaluation"*) remains accurate: evaluated once, candidate established, not adopted, still under
evaluation against named gates. A dated pointer to this ruling is added beneath it rather than
editing the ratified table, consistent with that document's own statement that the locality
column is **a pointer, not an authority**, and that the policy rows win on divergence.

**P9-GH-3 remains irrelevant to this row**, as ruled on 2026-07-30: row P4 does not wait on its
recorded trigger and may be amended by other evidence. That held — this ruling is made on
evidence that arrived through a door P4 never pre-registered.

---

## Disposition

**Row P4 stands: Milestone remains paid frontier.** `qwen3.6:27b` (Q4_K_M) is an established
**candidate** for the cell on genuine, well-made evidence, and is not adopted. Three gates are
named. No re-run of E35.5 is asked for or needed; its artifact is sufficient for this decision
and is the reason the decision could be made at all.

Carried to P11 scoping as a recorded HQ position, not an open question.
