---
project: ai-project-system
phase: P11
milestone: M38
epic: E38.6
type: reference
status: pre-registered
last_updated: 2026-08-12
---

# Packet 1 — fleet registry validation: fleet vs raw warning totals

**Defect (E38.6 comparison material):** The fleet registry's `validation` section reports a single `total_warnings: 14` that conflates warnings from fleet-enrolled projects with warnings from non-fleet configs (git worktrees and/or unenrolled project directories). A reader cannot tell whether `14` is the fleet total, the raw total including non-fleet configs, or something else.

**Ground truth (E38.3 Stage-2 rework, commit 927b7fa):** The fix separates `total_warnings` into `fleet_total_warnings` (12) and `raw_total_warnings` (14), adds `fleet_configs` (13), `raw_configs_checked` (15), and `excluded_worktree_configs` (2), and adds a derived-invariant test.

**Provenance — verbatim `git show` of the pre-fix revision:**

- `git show 9e2feaf:.ai-project/registry/fleet-registry.yml` — the registry as first delivered
- `git show 9e2feaf:tests/test_fleet_registry.py` — the test file as first delivered

**Excised (blinding record) — none of the following appears in the prompt below:**

- The fix commit `927b7fa` and its diff
- E38.3's Delivery Notice (which narrates the fix)
- The post-fix version of the registry or test file
- Any document stating the correct warning totals (12 fleet, 14 raw)
- The test `test_fleet_and_raw_warning_totals_are_distinct_and_derived` that was added

<!-- PROMPT-BEGIN -->

You are given a fleet registry file and its corresponding test file. The registry records the state of 15 project directories, their enrollment status, and the results of a §4 validation run.

## The Problem

The registry's `validation` section currently reports:

```yaml
validation:
  measured: 2026-08-11
  command: bin/ai-project-validate --fleet ~/soft-dev
  invalid_configs: 4
  total_errors: 8
  total_warnings: 14
```

The `enumeration` section reports that the fleet root contains 17 directories, of which 2 are excluded as git worktrees, leaving 15 project directories. Of those, 13 are enrolled and 2 are unenrolled.

The problem: `total_warnings: 14` is an aggregate that does not distinguish between warnings from enrolled fleet projects and warnings from non-fleet configs that the validator checked. A fleet warning total should count only enrolled fleet projects; the raw total should include everything the validator checked. Currently a reader cannot tell which is which.

## Your Task

Fix the registry at `.ai-project/registry/fleet-registry.yml` to:

1. **Separate the totals** — replace `total_warnings` with distinct fields for the fleet-only total and the raw total
2. **Add derived fields** — add the fields that make the relationship between the totals explicit (how many configs were checked in each category, how many were excluded, and why)
3. **Add a test** — add a test in `tests/test_fleet_registry.py` that verifies these derived invariants hold (e.g. that the raw total equals the fleet total plus excluded configs' contributions)

The correct numbers can be derived from the registry itself: each enrolled project lists its `section_4_warnings`, and the difference between the raw total and the fleet total is knowable from the enumeration.

## Files

The relevant files are provided in the workspace:

- `.ai-project/registry/fleet-registry.yml` — the registry (pre-fix version)
- `tests/test_fleet_registry.py` — the test file (pre-fix version)

Do not modify any files outside these two. Do not touch `bin/ai-project-validate` or any governance document.
