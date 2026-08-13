---
project: ai-project-system
phase: P11
milestone: M38
epic: E38.6
type: reference
status: pre-registered
last_updated: 2026-08-12
---

# Pre-registered scoring rubric — Local/Paid Controlled Comparison (E38.6)

**This file is committed in the same commit as the comparison packet and BEFORE any model run.** Git history is the proof. Nothing in this file may be changed once a run has been made. If it turns out to be a bad rubric, that finding is reported as a finding — it is not edited.

A rubric written after seeing outputs is a rationalization, not a rubric (E35.5 discipline).

---

## What is being measured

**Quality of a code-shaped data-integrity fix**, run both ways: agentic/local through E38.2's adapter (qwen3-coder:30b) and manual/paid at models.epic_manual (remote:claude-opus-5). Not throughput, not cost, not token counts. The comparison's value is in its method, not in any single result.

---

## Run protocol (fixed before any run)

| | |
|---|---|
| Local arm | OpenCode v1.18.10 through drivr's OpenCodeAdapter, ContainerEnvironment (debian:12-slim), model `ollama/qwen3-coder:30b` |
| Paid arm | Manual chat at `models.epic_manual` (`remote:claude-opus-5`) |
| Prompt | The task description from the blinded packet, with the pre-fix files provided in the workspace (local) or inline (paid) |
| Turns | Single session per arm; no re-prompting, no follow-up clarification from the evaluator |
| Repo access | Local: the isolated workspace only (no `.git`, no post-fix commits). Paid: the blinded packet content only |
| Runs per arm | **exactly 1** (see note on scale below) |

**Every run is reported.** There is no best-of-N, silent or otherwise.

**No prompt tuning.** The packet is frozen at this commit.

### Note on scale

This comparison compares one task run two ways. The sample size (n=1 per arm) is stated honestly. A single task does not support a general claim about either tier — that limitation is the point of the §What this does NOT establish section. The comparison is reusable: someone could run it again on new material from the method as recorded (E38.6 Acceptance Criterion 4).

---

## Scoring categories

Each arm gets exactly one verdict per category:

### Registry fix correctness

- **CATCH** — the registry's `validation` section correctly separates fleet-only totals from raw totals, with all three of:
  1. A fleet-only warning total distinct from the raw total
  2. Derived fields that make the relationship explicit (config counts per category, excluded count)
  3. A test that verifies the derived invariants

- **MISS** — any of: the fix is incomplete (e.g. separates totals but adds no test, or adds a test but doesn't fix the registry); the numbers are wrong (the fleet total does not match the sum of enrolled projects' `section_4_warnings`); the fix introduces a structural error (e.g. removes existing fields, breaks YAML parsing)

- **FALSE ALARM** — each additional defect the arm asserts or introduces that is not real. Including: modifying files outside the two scoped files; changing unrelated parts of the registry (project classifications, state definitions, transitions); altering `bin/ai-project-validate` or governance documents; asserting that the registry's enumeration counts are wrong when they are correct

### G1 compliance

- **PASS** — the non-uniform input (the single `total_warnings` field that needs to be replaced) is quoted verbatim where described, not paraphrased or summarised in a way that loses information
- **FAIL** — the original field name or value is described rather than quoted verbatim when it is the unique non-uniform element

### G2 compliance

- **PASS** — completion is verifiable from the committed artifacts (registry diff + test file) rather than from the arm's own prose about what it did
- **FAIL** — the arm's prose is the only evidence of what was changed

---

## The pass bar (pre-registered)

The comparison records a meaningful result if:

1. At least one arm achieves **CATCH** on registry fix correctness (proving the task is solvable by at least one tier on this material)
2. Both arms' results are recorded honestly, whichever way they fall — a poor local result is evidence, not failure
3. **G1 and G2 compliance** are recorded for both arms, regardless of the fix result
4. **No routing policy changed** — `model-routing-policy.md` is unmodified

---

## What the judgment is, and is not

**A CATCH by either arm is evidence about this task on this material only.** It does not imply that tier is generally superior. **A MISS by either arm is evidence about this task on this material only.** It does not imply that tier is generally unsuitable.

**This comparison does not decide any routing policy.** `model-routing-policy.md` row P4, P6, P7, or any other row is untouched. A further HQ call owns those decisions.

**G11 is not claimed by this comparison.** Running real agentic work through a real adapter is not an `epic_qa` run (Constraint 8).
