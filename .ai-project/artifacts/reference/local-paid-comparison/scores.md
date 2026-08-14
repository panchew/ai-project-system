---
project: ai-project-system
phase: P11
milestone: M38
epic: E38.6
type: reference
status: complete
last_updated: 2026-08-12
---

# Scored comparison — Local/Paid Controlled Comparison (E38.6)

Scored against the **pre-registered rubric** (`rubric.md`). Both runs reported in full; no
best-of-N. The reviewer re-measured each arm's output (G2) rather than trusting its prose.

## Summary of results

| | Local arm (qwen3-coder:30b, blinded) | Paid arm (claude-opus-5, UNBLINDED) |
|---|---|---|
| Conditions | Isolated workspace, no git, had to derive | Repository access, read committed answer |
| Registry fix | **MISS (partial)** — correct numbers, incomplete | **INVALID / not scorable** — retrieved answer, did no work |
| G1 | PASS | N/A |
| G2 | PASS (re-measured) | N/A (report matched git, but retrieval not derivation) |
| **Comparable?** | **No** — see the asymmetry finding below | **No** |

---

## Local arm — MISS (partial), the derived fields and test are incomplete

**Conditions:** OpenCode v1.18.10 through E38.2's adapter, model `ollama/qwen3-coder:30b`,
isolated workspace with the two pre-fix files and **no git history**. Exit code **0**.

**What it did (re-measured from the files, not its prose):**

1. `validation:` section — replaced `total_warnings: 14` with:
   ```yaml
   fleet_warnings: 12
   raw_total_warnings: 14
   ```
   **The two key numbers are correct** (12 fleet, 14 raw — matches the sum of enrolled
   `section_4_warnings` and the committed ground truth).
2. `enumeration:` section — added `fleet_configs_checked: 13` and `excluded_configs: 2`.
3. Added a test `test_validation_warnings_separated_correctly` that checks field presence
   and `raw_total_warnings >= fleet_warnings`.

**Why not a CATCH (rubric requires all three):**

- **Criterion 1 (fleet total distinct from raw total):** ✅ met.
- **Criterion 2 (derived fields making the relationship explicit):** ⚠ PARTIAL. It added
  config counts (13, 2) but **omitted `raw_configs_checked`** and placed the counts in the
  `enumeration` section rather than alongside the totals. The structural identity
  `raw(15) == fleet(13) + excluded(2)` is **not** explicitly stated.
- **Criterion 3 (test verifies the derived invariants):** ⚠ PARTIAL. The test checks
  `>=` and field presence, but **does not verify the structural sum** `raw == fleet +
  excluded_contribution`, and does not sum `section_4_warnings`. Its assertions would pass
  even if the invariant were broken.

**Verdict:** MISS. The concept and the two headline numbers are right, but the deliverable
is incomplete against the pre-registered bar. Recorded honestly — a partial fix is evidence,
not failure.

**G1:** PASS — the non-uniform element (`total_warnings: 14`) was quoted verbatim in its
reasoning and replaced with the exact value preserved (`raw_total_warnings: 14`).

**G2:** PASS — I verified completion from the file diffs and a re-run of the test suite
(17 passed), **not** from the arm's prose and **not** from its exit code (recorded 0, not
relied on).

---

## Paid arm — INVALID as a capability measurement (contaminated by repo access)

**Conditions:** Manual chat at `models.epic_manual` (`remote:claude-opus-5`). **The run had
repository access to the live `milestone/M38` state, including commit `927b7fa` — which
contains the answer.**

**What it did:** It did **not** derive the fix. It located the committed answer
(`927b7fa`), reported the four derived fields verbatim, verified the numbers by reading the
committed registry, and concluded "This task is already done — and merged. No changes were
needed."

**This is the epic's central finding, demonstrated empirically rather than asserted:**

> An unblinded arm with repository access produces an **excellent-looking result that is
> retrieval, not capability.** The paid arm "scored" perfectly on every number — because it
> read the answer. This is exactly the contamination E35.5's method and this Epic's
> blinding exist to prevent (spec §Finding 2).

**Scoring:** Not scorable as a capability measurement. It produced no work product and made
no derivation. Reporting its "perfect" result as evidence of paid-tier capability would be
the most misleading possible outcome for a routing decision — which is the exact warning
the Epic carries.

**One genuine, non-retrieved observation:** The committed fix (E38.3's) asserts the warning
invariant as **literals** (`raw_total_warnings == 14`, `fleet_total_warnings == 12`), not
structurally (`raw == fleet + excluded_contribution`), because the registry does not record
the excluded configs' contribution. This is real analysis of the delivered artifact. It is
a noticed-and-left observation (the arm correctly declined to edit E38.3's artifact).

---

## ⚠ The asymmetry finding (Finding 3, reproduced one level up)

**The two arms did not operate under comparable conditions.**

| | Local | Paid |
|---|---|---|
| Repository access | **None** (isolated workspace, no git) | **Full** (live milestone/M38) |
| Could see the answer | No | **Yes** |
| What was measured | Derivation | Retrieval |

**This is B3.1's confound, one level up, stated plainly rather than smoothed.** A comparison
with an unstated asymmetry is worse than none because it will be cited — so this asymmetry
is stated here in the open. **No tier conclusion can be drawn from this comparison as run.**

**Why the local arm was blinded and the paid arm was not:** the local arm runs through
E38.2's adapter against a working directory the Epic controls, so it was given a clean,
git-free workspace. The paid arm is a manual chat the operator runs; in this instance the
operator's chat had repository access and the model used it. This is a property of the
execution environment, not a judgement about either tier.

---

## Pass bar — assessed

The pre-registered pass bar required "at least one arm achieves CATCH." **Neither arm
achieved CATCH** — the local arm was a partial MISS, the paid arm was not a valid capability
measurement. **The comparison did not produce a usable tier result, and that finding is the
deliverable.** Both arms' results are recorded honestly (§G1, §G2 both honored on the local
arm). No routing policy changed.
