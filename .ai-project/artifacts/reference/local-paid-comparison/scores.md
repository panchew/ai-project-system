---
project: ai-project-system
phase: P11
milestone: M38
epic: E38.6
type: reference
status: complete
last_updated: 2026-08-14
---

# Scored comparison (resubmission) — Local/Paid Controlled Comparison (E38.6)

Scored against the **original pre-registered rubric** (`rubric.md`), unchanged. Per the
protocol-correction addendum (`protocol-correction-addendum.md`), the **valid** comparison
pair is **local run 2** and **paid run 2**. Run 1 of each arm is a protocol-invalid trial,
preserved and not scored.

## Valid pair — results

| | Local run 2 (qwen3-coder:30b) | Paid run 2 (claude-opus-5) |
|---|---|---|
| Conditions | Drivr OpenCodeAdapter, ContainerEnvironment (debian:12-slim), isolated git-free workspace | fresh packet-only session, no repo/git/search access |
| Registry fix | **MISS** — `fleet_warnings: 10`, **wrong** (correct 12) | **CATCH** — `fleet_warnings: 12`, `raw_warnings: 14`, `excluded_warnings: 2`, all correct |
| G1 | PASS | PASS |
| G2 | PASS (re-measured) | PASS (values re-verified, non-contamination confirmed) |
| Comparable? | Yes — both valid, protocol-conforming | Yes |

---

## Local run 2 — MISS (numbers wrong)

**Conditions:** Drivr's `OpenCodeAdapter`, `ContainerEnvironment` (`debian:12-slim`), model
`ollama/qwen3-coder:30b`, isolated git-free workspace. Exit code **0**; wall-clock 276.9 s;
adapter duration 237,200 ms.

**What it did (re-measured from files):** separated `total_warnings: 14` into
`fleet_warnings: 10` and `raw_total_warnings: 14`; added `excluded_configs` to the
`enumeration` section; added 4 duplicated test functions.

**Why MISS:** the fleet total is **`10`, but the ground truth is `12`** (sum of the 13
enrolled projects' `section_4_warnings`, verified independently). The arm mis-attributed the
excess — it reasoned the 2-warning gap came from 2 unenrolled projects, but those carry no
warnings; the gap is actually the 2 worktree checkouts of `ai-project-system`. It also
omitted the structural invariant (`raw == fleet + excluded`) and duplicated test functions.

**G1:** PASS — the non-uniform element (`total_warnings: 14`) quoted verbatim; no derivation
step.

**G2:** PASS — scored from the file diffs and a test re-run, not from prose or exit code.

---

## Paid run 2 — CATCH (correct, structurally divergent, non-contaminated)

**Conditions:** fresh claude-opus-5 session, packet content only (one `Read` of the sealed
packet, verified), no repository/git/search access. Wall-clock 538 s (operator-inflated);
**execution duration 299,019 ms** — the figure comparable to the local arm's 237,200 ms.

**What it did (re-measured/verified):** produced a proposed registry rewrite splitting
`total_warnings: 14` into `fleet_warnings: 12`, `raw_warnings: 14`, `excluded_warnings: 2`,
plus scope-named error/invalid counts and checked/excluded config counts, and 8 tests
including the structural invariant `raw == fleet + excluded` for all three measures.

**Why CATCH (rubric requires all three):**
1. **Fleet total distinct from raw total:** ✅ `fleet_warnings: 12` vs `raw_warnings: 14`.
2. **Derived fields making the relationship explicit:** ✅ `configs_checked: 15`,
   `fleet_configs_checked: 13`, `excluded_configs: 2`, with `raw == fleet + excluded`.
3. **Test verifying the derived invariants:** ✅ 8 tests including the sum invariant for all
   measures, an independent second derivation of 12, and a guard against the ambiguous
   `total_warnings` returning.

**Values verified (G2):** `fleet_warnings=12`, `fleet_errors=8`, `invalid=4`, `enrolled=13`
all re-derived correctly from the pre-fix registry.

**Non-contamination evidence (from the run metadata):**
- Field-name overlap with the committed answer (`927b7fa`): **0**.
- Test-name overlap with the committed answer's test: **0**.
- **Structural divergence:** run 2 retires `invalid_configs`/`total_errors` and adds a test
  forbidding their return; the committed answer **keeps** both. A contaminated run would not
  delete fields the answer preserves.
- Values agree (12/14/15/13/8/4) because they are **derivable from the pre-fix registry** —
  which is the task — not because the answer was read.

**G1:** PASS.

**G2:** PASS — scored from the proposed artifact and verified numbers, not from prose; the
arm itself stated "no other tool was used" and the transcript confirms a single `Read`.

---

## The comparison, finally valid

**The valid pair is now scorable and comparable:** both arms ran under their registered
conditions. Local run 2 = **MISS** (wrong fleet number). Paid run 2 = **CATCH** (correct,
complete, non-contaminated). **This is a genuine local/paid result on this task on this
material.**

**But the sample size is n=1 per arm.** This single task does not support a general claim
about either tier. It is recorded here with that limitation, and it is offered as evidence
for a further HQ call — not as a decision.

---

## Invalid trials (preserved, not scored)

- **Paid run 1:** had repository access, read the committed answer (`927b7fa`). INVALID —
  retrieval, not capability. Preserved at `runs/paid/paid-arm-run-1.md`.
- **Local run 1:** ran directly on the host, not through the registered
  ContainerEnvironment. INVALID (environment mismatch). Preserved at `runs/local/`.

## Pass bar — assessed

The pre-registered pass bar required "at least one arm achieves CATCH." **Paid run 2
achieved CATCH.** Both arms ran validly and were scored. The judgment is recomputed from the
valid pair only, with the n=1 limitation retained.
