# E41.4 — D4: Both bars applied, and four per-row recommendations

**Status:** UNBLINDED. Composed after the blinded scores (`8fbc30a`) and the
opaque-ID↔model mapping (`91b3431`) were committed, in that order (U1). The tables
below derive every number from `scores.md` (blinded) + `mapping.tsv` (published).

**Layer / time / scope (`P11-GH-2`):** this document, on `epic/P12-M41-E41.4`,
2026-09-01. Claims describe the E41.4 back-test only — remote single-turn tool-free
captures on the frozen E35.5 instrument. They say nothing about chat surfaces (U2),
about the lane harness (E41.2/E41.3 — different instrument), or about any model's live
review fitness.

---

## The mapping (published, unblinded)

| Opaque ID | Model | Packets | Result |
|-----------|-------|---------|--------|
| R01–R10 | `anthropic/claude-opus-5` | 1–5 × 2 | 10/10 CATCH, 0 FA |
| R11–R20 | `openai/gpt-5.6-sol` | 1–5 × 2 | 10/10 CATCH, 0 FA |
| R21–R30 | `opencode/deepseek-v4-pro` | 1–5 × 2 | 10/10 CATCH, 0 FA |

All 30 runs: finish=stop, exit=0 — no truncation, no mechanical failure, no refusal
(U5). No tuning applied (U5 / rubric Run protocol).

---

## The measurements, per model

Every defect scored identically across all three models. The per-model tables are
therefore the same table; the rows below state each model's row explicitly so the
reader can verify the identity rather than be told it.

### `claude-opus-5` (baseline, `remote:claude-opus-5`) — R01–R10

| Packet | Defect | Ground truth | Runs | Score |
|--------|--------|--------------|------|-------|
| 1 | decomposition gap | NOT SOUND | 2 | CATCH ×2 |
| 2 | completion false positive | REJECT | 2 | CATCH ×2 |
| 3 | completion false negative (inverse control) | ACCEPT | 2 | CATCH ×2 |
| 4 | factual miscount | REJECT | 2 | CATCH ×2 |
| 5 | test correctness | test at fault | 2 | CATCH ×2 |
| **Totals** | | | **10** | **10 CATCH / 0 MISS / 0 SPLIT / 0 FA** |

**Packet 3 (reported separately, U3):** ACCEPT on both runs — the incumbent does not
reject correct work. **No false alarm.**

### `gpt-5.6-sol` (candidate for `phase`, `remote:gpt-5.6-sol`) — R11–R20

| Packet | Defect | Ground truth | Runs | Score |
|--------|--------|--------------|------|-------|
| 1 | decomposition gap | NOT SOUND | 2 | CATCH ×2 |
| 2 | completion false positive | REJECT | 2 | CATCH ×2 |
| 3 | completion false negative (inverse control) | ACCEPT | 2 | CATCH ×2 |
| 4 | factual miscount | REJECT | 2 | CATCH ×2 |
| 5 | test correctness | test at fault | 2 | CATCH ×2 |
| **Totals** | | | **10** | **10 CATCH / 0 MISS / 0 SPLIT / 0 FA** |

**Packet 3 (reported separately, U3):** ACCEPT on both runs. **No false alarm.**

### `deepseek-v4-pro` (candidate for `milestone`, `remote:deepseek-v4-pro`) — R21–R30

| Packet | Defect | Ground truth | Runs | Score |
|--------|--------|--------------|------|-------|
| 1 | decomposition gap | NOT SOUND | 2 | CATCH ×2 |
| 2 | completion false positive | REJECT | 2 | CATCH ×2 |
| 3 | completion false negative (inverse control) | ACCEPT | 2 | CATCH ×2 |
| 4 | factual miscount | REJECT | 2 | CATCH ×2 |
| 5 | test correctness | test at fault | 2 | CATCH ×2 |
| **Totals** | | | **10** | **10 CATCH / 0 MISS / 0 SPLIT / 0 FA** |

**Packet 3 (reported separately, U3):** ACCEPT on both runs. **No false alarm.**

---

## Bar 1 — E35.5's ABSOLUTE pre-registered pass bar (per model, alone)

The pre-registered pass bar (`rubric.md`): **PASS** iff (1) ≥4 of 5 defects caught
(a SPLIT counts as not-a-catch); (2) **no** false alarm on defect 3; (3) ≤2 false
alarms in total.

| Model | Catches (of 5) | FA on defect 3 | Total FA | Absolute bar |
|-------|----------------|----------------|----------|--------------|
| `claude-opus-5` | 5/5 | 0 | 0 | **PASS** |
| `gpt-5.6-sol` | 5/5 | 0 | 0 | **PASS** |
| `deepseek-v4-pro` | 5/5 | 0 | 0 | **PASS** |

Each model is individually interpretable: **all three clear the absolute bar with
margin.** This says each is capable of recognising the five known defects on this
curated, single-turn instrument — it says nothing comparative.

## Bar 2 — M41's RELATIVE bar (each candidate vs the `claude-opus-5` baseline)

The ruled relative bar: **no worse on every objective check, strictly better on at
least one**, naming which check carried it.

Objective checks available (this harness has directional outcomes — E41.3's T3 gap does
not exist here): catches, misses, SPLITs, false alarms, and the packet-3 inverse
control — per defect, per run.

| Check | `claude-opus-5` | `gpt-5.6-sol` | `deepseek-v4-pro` |
|-------|-----------------|----------------|-------------------|
| Catches | 10/10 | 10/10 | 10/10 |
| Misses | 0 | 0 | 0 |
| SPLITs | 0 | 0 | 0 |
| False alarms (all) | 0 | 0 | 0 |
| False alarms (defect 3) | 0 | 0 | 0 |
| Packet 3 verdict | ACCEPT ×2 | ACCEPT ×2 | ACCEPT ×2 |

**Neither candidate is strictly better than the incumbent on any check — they are
identical on every check.** The relative bar therefore **does NOT clear for either
candidate.** This is not a negative result about either model; it is the bar's own
consequence when the instrument cannot discriminate. **The result is escalated to the
CFO as a result, not as a failure** (Question Policy: *no candidate clears a row → the
row holds, the result goes to the CFO*).

---

## `judgment.md`'s six cautions, applied to this result

A 30/30 CATCH with zero variance and zero false alarms is the *cleanest possible*
outcome on this instrument, and that is exactly when the cautions bind most:

1. **The split is not there to be absorbed** — here there was no split at all; the
   caution that variance is a real exposure is instead the warning that the instrument
   could not *show* variance on any of the three models. Two runs per packet is a floor
   for detecting variance, not a measurement of its rate; three identical 10/10 models
   do not prove the models are equivalent — they prove the instrument did not
   discriminate among them.
2. **The packets are curated.** Each packet is a bounded question with material
   assembled and noise removed. Live Stage-2 review is not. This result measures
   recognition of known ground truth under ideal presentation, and nothing more.
3. **Single-turn and tool-free.** No follow-up, no repo access. Real review is
   iterative.
4. **Correct-verdict-wrong-reason risk** is present even where verdicts were right; the
   rubric's reason requirement is what was checked, and all 30 met it — but meeting it
   on curated material does not prove reasoning holds under ambiguity.
5. **The absolute PASS is necessary evidence, not sufficient** — it makes each model a
   *candidate*, it does not open any cell.
6. **This is one instrument, one set of five defects.** It is not a general claim about
   any of the three models.

**Stated plainly:** this back-test shows all three models equal on the frozen
instrument, all clearing the absolute bar. It provides **no relative evidence** for
moving either the `phase` or `milestone` row, because the relative bar's
strictly-better leg is unmet by construction. The back-test does not support — and
does not contradict — the CFO's line-up decision; it simply does not discriminate.

---

## Four per-row recommendations

The relative bar's two conditions are stated explicitly for each row (per the spec's
D4 requirement).

### `creation` — no candidate exists
- Candidate: **none.** SN-38's `fable-5` edit was cancelled (spec v1.4.0); the row is
  unchanged at `claude-opus-5`.
- Relative bar: **not applicable** — there is no candidate to compare.
- **Recommendation:** row holds at `remote:claude-opus-5`. No measurement was taken on
  a model this milestone was choosing between, because there is no contest.

### `phase` — `gpt-5.6-sol` vs baseline
- Relative bar: no worse on every check (TRUE — identical) **and** strictly better on
  at least one (FALSE — identical on all). **Bar NOT cleared.**
- **Recommendation:** the row is **NOT moved on this evidence.** The back-test does not
  discriminate between `claude-opus-5` and `gpt-5.6-sol`. If `phase` is to hold
  `gpt-5.6-sol` (as the CFO's SN-40..46 line-up has it), that decision rests on the
  CFO's allowance, **not on this measurement** — and this epic records that the
  measurement is neutral. **Escalated to the CFO as a result.**

### `milestone` — `deepseek-v4-pro` vs baseline
- Relative bar: no worse on every check (TRUE — identical) **and** strictly better on
  at least one (FALSE — identical on all). **Bar NOT cleared.**
- Note: this row was measured with the **`pro`** variant (spec v1.4.0), the value now
  in `.ai-project.yml`, NOT the `flash` variant E41.1 §9.5 originally ruled.
- **Recommendation:** the row is **NOT moved on this evidence.** The transport for
  `milestone` exists and works (U2's blocking concern is discharged — a remote
  `deepseek-v4-pro` dispatch answered and was captured). Whether the row lands on the
  CFO's allowance rests with the CFO. **Escalated to the CFO as a result.**

### `epic_manual` — waived by the CFO
- The CFO amended this row's DoD: it lands on **R6's surface confirmation alone** (a
  surface that runs the model and self-reports a readable identity), not on a
  back-test. The E31.3 surface check is covered by E41.1 (§9.3: `deepseek-v4-flash`
  answers and self-reports `opencode/deepseek-v4-flash`).
- **Recommendation:** **not measured here** (per spec v1.4.0, waived). No back-test
  obligation; the row's landing condition is the surface check, which is discharged
  elsewhere. No escalation required.

---

## Escalation summary

**Escalations required (D5):**
1. **`phase`** — no candidate cleared the relative bar (identical to baseline). Row
   holds; the neutral measurement is recorded and routed to the CFO as a result.
2. **`milestone`** — no candidate cleared the relative bar (identical to baseline).
   Row holds; neutral measurement routed to the CFO as a result.

**Positive statements:**
- **No packet or rubric change was required.** The frozen instrument sufficed
  untouched (binding constraint 1 held).
- **No truncation-mechanism escalation (U5).** Every remote vendor reported a clean
  `stop`; truncation never needed to be distinguished from a miss.
- **No U8 measurement fault.** All three remote targets answered from this host; the
  credential-visibility layer is recorded per run, all `NOT-READ`, zero leaks. E41.1's
  baseline is not contradicted.
- **No U7 fidelity control was required to block anything.** The D7 fidelity probe
  round-tripped the well-formed unguessable path **exactly** on both `phase` and
  `milestone` routes; receive and faithful report are CONFIRMED for both rows. See
  `fidelity/d7-fidelity-note.md`.