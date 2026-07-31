---
project: ai-project-system
phase: P10
milestone: M35
epic: E35.5
type: reference
status: complete
last_updated: 2026-07-31
---

# Judgment — Milestone × local-inference back-test

## The judgment

**PASS**, against the bar pre-registered in `rubric.md` (`562502b`), before any model was run:

| Pre-registered condition | Required | Measured | Met |
|---|---|---|---|
| Catches | ≥ 4 of 5 | **4** (defects 1, 2, 3, 4) | ✅ |
| False alarm on defect 3 | none | **none** | ✅ |
| False alarms in total | ≤ 2 | **0** across 5 packets and 10 runs | ✅ |

`qwen3.6:27b`, reviewing blinded material it had never been told the answer to, caught the M33
decomposition gap, the exit-0-with-zero-work false positive, and the arithmetic error in a delivery
notice — and **accepted** the exit-2 run whose work was actually complete and green. It split on the
starter-lint defect: both runs diagnosed the guard correctly, one prescribed the real fix, the other
prescribed the documentation workaround.

## What this PASS does NOT do

**It does not move, decide, or recommend a change to `model-routing-policy.md` row P4.** That call
belongs to **HQ**, on this evidence. This Epic did not touch the policy file — an empty diff is
recorded in the Delivery Notice — and takes no position on the outcome.

**A pass is necessary evidence, not sufficient.** The HQ Ruling on SN-25 (Decision 5) set
back-testing against known ground truth as the bar for a local model to be a **candidate** for the
Milestone-locality cell. Being a candidate is what was earned here. It does not follow that the cell
should open, and this Epic must not be read as arguing that it should.

**It does not settle the cell in either direction.** E35.4 recorded Milestone × locality as
"Remote — local under evaluation." That is still what it says. Only HQ can change it.

**It is one model, one machine, five defects, ten runs.** It is not a general claim about local
inference, about other local models, or about `qwen3.6:27b` at other quantisations. The parked
llama.cpp + Qwen3.6 **Q8_0** stack was not touched and remains parked; the candidate here is
**Q4_K_M**, a different artifact.

## What HQ should weigh against the PASS

Recorded here because a judgment that reports only its supporting evidence is not a judgment.

**1. The split is the most consequential result, and the bar absorbs it.** Defect 5 produced
identical diagnoses and **opposite prescriptions** across two runs of the same prompt at the same
settings. One would have left P10-GH-6 armed for the next cross-repo epic. The 4-of-5 bar permits
exactly one such failure, and this run used it. Milestone holds Stage-2 accept authority; a level
whose remedy for a defect depends on the sampling draw is a real exposure, and it is not visible in
the headline "4 of 5".

**2. Two runs per packet is a floor for detecting variance, not a measurement of it.** The protocol
can show that variance exists — it did — but cannot estimate its rate. One split in five packets is
consistent with anything from a rare divergence to a coin flip. Deciding row P4 on this evidence
means deciding without knowing which.

**3. The packets are curated, and real Stage-2 review is not.** Each packet was a bounded question
with the relevant material assembled and the noise removed. A live Milestone Chat must *find* what to
examine across a branch, decide what is even in scope, and notice absences. Nothing here tests that,
and it is a large part of the job.

**4. The evaluation is single-turn and tool-free.** No follow-up, no repo access, no ability to check
a claim. Real Stage-2 review is iterative.

**5. Reasoning quality was not uniformly reliable even where verdicts were right.** Defect 2 run 1
reached the correct REJECT via an incorrect causal hypothesis. The verdict survived; the reasoning
would not have, had the review needed to act on the cause.

**6. The natural experiment does not corroborate locality.** `Getawayinsured2023` routes `milestone:`
to **`remote:`**`qwen3.6:27b` — the same model at a remote endpoint. It supports the model choice and
says nothing about running the Milestone level locally (`scores.md`, final section).

## What the PASS is genuinely good evidence for

**Exit-code untrust generalises to the reviewer.** The strongest result is defects 2 and 3 together:
the model rejected exit 0 with zero work and accepted exit 2 with complete, green work, addressing
the exit status explicitly in both directions. That is exactly the two-sided judgment **P10-GH-7**
records as measured-broken in automated block detection, and it was reached from the transcript,
diff and suite result rather than the status code.

**Citation discipline held under load.** Every quotation across both packet-1 runs — a
25,195-token prompt — was verified verbatim against the committed specs. No fabricated citations.

**Both trap directions were avoided.** The model neither condemned the correct work in packet 3 nor
the correct identity claim in packet 4. Zero false alarms across ten runs is the result the rubric
was built to be able to disconfirm, and it did not.

## Method note — why this evidence is admissible

The blinding and the pre-registration are the load-bearing parts, and both are auditable rather than
asserted:

- **The rubric predates every result.** `562502b` contains the rubric and all five packets; the first
  scored run landed after it. `git log` shows the order.
- **The blinding is checkable.** Each packet's audit header names what was excised; `README.md` gives
  a mechanical check a reader can re-run, and states the two deliberate exemptions and why they are
  original source text rather than leaks.
- **Every run is reported**, including two aborts, two superseded runs, one truncation, one ENOSPC
  failure and an infrastructure probe — all committed, none selected on content. The discarded
  truncated run would have scored **MISS**, so discarding it did not favour the candidate.
- **No prompt was ever changed.** Only `num_ctx` and `num_gpu` were corrected, both mechanical, both
  recorded per run.

Had the bar been "catch on all five", this would read **FAIL**. It was set at 4 of 5 before any
result existed, and it is reported as it was written.
