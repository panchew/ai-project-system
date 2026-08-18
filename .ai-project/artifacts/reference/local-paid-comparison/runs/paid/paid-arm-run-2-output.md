Read the packet once. Everything below is derived from it; no other tool was used.

The key finding: the per-project `section_4_warnings` lists sum to **12**, not 14, and the missing 2 are attributable to a specific pair of configs the validator opened but the fleet does not contain.

## A. Revised registry

Two changes: the `validation:` section (plus its comment banner), and the `registry_version` line in the provenance block.

```yaml
# --- provenance block, top of file: one line changes ---
registry_version: "1.1.0"     # was "1.0.0" — `validation:` gained scope-qualified counts
created: 2026-08-11
created_by: Epic P11-M38-E38.3 (ai-project-system, P11-M38)
fleet_root: ~/soft-dev
```

```yaml
# ============================================================================
# §4 VALIDATION — as measured, not as remembered
# ============================================================================
#
# Command:  bin/ai-project-validate --fleet ~/soft-dev
# Date:     2026-08-11
# Repo:     ai-project-system @ epic/P11-M38-E38.3
#
# 4 of 13 enrolled configs are §4-INVALID, carrying 8 errors between them.
#
# RECONCILIATION with the two figures already in the record, neither of which is wrong:
#
#   "3 of 6 invalid at P10 close"  (P11-M38 milestone spec) — a DIFFERENT SCOPE: six
#       projects, not thirteen. Not comparable, and not contradicted.
#   "4 of 12 invalid"  (E38.3 spec Finding 3, 2026-08-08) — required-field PRESENCE
#       only, before any format constraint was checked, over twelve enrolled projects.
#
#   This measurement: 4 of 13, over the same four projects, 2026-08-11, full §4.
#
# The spec predicted "your number will be higher than four." The number of invalid
# PROJECTS did not move — it is the same four. The number of VIOLATIONS did: presence-
# only found 5, full §4 found 8. The three additional violations are `home_finance`'s
# `project.name` (rule 7 — `home_finance` contains an underscore, which
# `^[a-z][a-z0-9-]*$` does not admit) and `social-stories-creator`'s
# `governance.version: v7.0.0` (rule 5, twice — unquoted, and not bare semver).
# No project became invalid that was not already invalid on presence alone.
#
# ---------------------------------------------------------------------------
# TWO TOTALS, BECAUSE THE VALIDATOR CHECKED MORE THAN THE FLEET
# ---------------------------------------------------------------------------
#
# This section previously reported `total_warnings: 14` next to prose about 13 enrolled
# projects, and a reader could not tell which population the 14 belonged to. It belonged
# to neither cleanly. `--fleet ~/soft-dev` discovers configs by the immediate-
# subdirectory scan, and that scan opens FIFTEEN `.ai-project.yml` files: the 13 enrolled
# fleet projects, PLUS the two git worktrees the enumeration above excludes by hand.
# Each worktree is a checkout of `ai-project-system` itself, so each presents that
# project's config a second time and earns its one warning (`cfo_review_gate`) again.
#
#   fleet_warnings      12   = Σ `section_4_warnings` over the 13 enrolled projects
#   excluded_warnings  + 2   = 2 worktree checkouts × 1 warning each
#   raw_warnings       = 14  = what the validator printed
#
# The 12 is confirmed a second way, from data already in this file:
# `findings.schema_drift_class` records the three NOT-BLESSED fields in
# 5 (`created_at`) + 5 (`submodule_path`) + 2 (`cfo_review_gate`) = 12 configs, at one
# warning per occurrence. `framework_version` does not appear: it was BLESSED into
# §3.6 / rule 26 and is no longer warned.
#
# THE RAW TOTAL IS KEPT, NOT CORRECTED AWAY. Those 2 extra warnings are the residue of
# the naive `for d in */; do [ -f "$d/.ai-project.yml" ]` discovery — the exact method
# defect this Epic exists to guard against, showing up inside the Epic's own tooling.
# Deleting the raw figure would hide the evidence that `--fleet` has the defect the
# enumeration works around by hand. Recorded, not smoothed. NOT REPAIRED HERE: fixing
# `--fleet`'s discovery is a change to `bin/ai-project-validate`, which is out of scope.
#
# ERRORS AND INVALID COUNTS DO NOT SPLIT, and that is a measured fact rather than an
# omission: the two extra configs are checkouts of a §4-VALID config, so they contribute
# 0 errors and 0 invalid configs and the fleet and raw figures coincide. They are written
# out anyway, so that every count in this section names its category and no reader has to
# infer one from the surrounding prose.
#
# ⚠ COINCIDENCE, FLAGGED RATHER THAN LEFT TO TRIP SOMEONE: `configs_checked: 15` and
# `enumeration.project_directories: 15` are the same number over DIFFERENT SETS. The 15
# directories are 13 enrolled + 2 UNENROLLED (`ai-stack`, `character-factory`), which
# carry no root config and were never opened. The 15 configs are those same 13 + 2
# WORKTREES. The overlap is 13, not 15.

validation:
  measured: 2026-08-11
  command: bin/ai-project-validate --fleet ~/soft-dev

  # WHAT WAS CHECKED — stated so the totals below are attributable.
  configs_checked: 15
  fleet_configs_checked: 13
  excluded_configs: 2
  excluded_as_worktrees: [worktree-epic-E38.2, worktree-epic-E38.3]
  excluded_configs_note: >-
    Checked by the validator, NOT fleet members. Both are git worktrees of
    `ai-project-system` itself and carry a `.ai-project.yml` only because they are
    checkouts of this repository at `epic/P11-M38-E38.3`. `--fleet` discovery does not
    make the worktree exclusion the enumeration makes, so their configs were opened and
    their findings landed in the raw totals. Same list as
    `enumeration.excluded_as_worktrees`, for the same reason.

  # RESULTS — every count names its category. `fleet_*` counts only the 13 enrolled
  # fleet projects and is the figure to quote about the fleet. `raw_*` is what the
  # validator printed over everything it opened. `excluded_*` is the difference, and
  # `raw_* == fleet_* + excluded_*` holds for all three measures by construction.
  fleet_invalid_configs: 4
  raw_invalid_configs: 4
  excluded_invalid_configs: 0
  fleet_errors: 8
  raw_errors: 8
  excluded_errors: 0
  fleet_warnings: 12
  raw_warnings: 14
  excluded_warnings: 2
  totals_note: >-
    The fleet warning total is the sum of the `section_4_warnings` lists on the 13
    enrolled projects below; it is not a separate measurement to be taken on faith, and
    `tests/test_fleet_registry.py` re-adds it. The excluded contribution is 2 worktree
    checkouts of `ai-project-system` × its 1 warning. Errors and invalid counts coincide
    across fleet and raw because that source config is §4-VALID. No re-measurement was
    performed: this is the 2026-08-11 run, re-presented with its scopes named.
```

## B. Tests to add

Place after `test_worktrees_are_excluded_and_the_exclusion_is_stated` and before the `Binding Constraint 5` banner. Plus one required edit to an existing assertion, shown first.

```python
# EXISTING TEST, one line changed, because the `validation:` schema changed and a schema
# change under a frozen version number is the same "reader cannot tell" defect in
# another costume.
def test_registry_exists_and_parses(registry):
    """Drivr reads this file (`SN-27` decision 5). A registry Drivr cannot parse has
    missed the point."""
    assert isinstance(registry, dict)
    assert registry["registry_version"] == "1.1.0"


# ---------------------------------------------------------------------------
# §4 totals — fleet vs raw. The validator checked more than the fleet, and the
# section now says so in fields rather than leaving it to prose.
# ---------------------------------------------------------------------------


def test_no_validation_count_is_scope_ambiguous(registry):
    """The defect this replaced: `total_warnings: 14` sat in a section whose prose talks
    about 13 enrolled projects, and belonged to neither population cleanly. Every count
    here now declares its category in its own name, and the ambiguous names must not
    come back — including by someone helpfully "restoring" them for compatibility."""
    validation = registry["validation"]
    for retired in ("total_warnings", "total_errors", "invalid_configs"):
        assert retired not in validation, (
            f"{retired!r} is scope-ambiguous: say fleet_, raw_ or excluded_"
        )
    counts = {k: v for k, v in validation.items() if isinstance(v, int)}
    assert counts, "the validation section records no counts at all"
    for key in counts:
        assert key.startswith(("fleet_", "raw_", "excluded_", "configs_")), (
            f"{key!r} does not name the population it counts"
        )


def test_fleet_totals_are_the_sum_of_the_projects_own_lists(registry):
    """The fleet figures are not a separate measurement to be trusted on faith — they are
    the per-project lists already in this file, added up. If they stop agreeing, one of
    the two is stale and the registry no longer knows which."""
    validation = registry["validation"]
    enrolled = [p for p in registry["projects"] if p["enrolled"]]

    assert len(enrolled) == validation["fleet_configs_checked"]
    assert sum(len(p["section_4_warnings"]) for p in enrolled) == validation["fleet_warnings"]
    assert sum(len(p["section_4_errors"]) for p in enrolled) == validation["fleet_errors"]
    assert sum(1 for p in enrolled if p["section_4"] == "invalid") == (
        validation["fleet_invalid_configs"]
    )


def test_raw_totals_equal_fleet_totals_plus_the_excluded_contribution(registry):
    """The invariant the split exists to make checkable, for every measure and not just
    the one that happened to differ. If these stop reconciling, the section is recording
    a subtraction somebody did in their head."""
    validation = registry["validation"]
    for measure in ("warnings", "errors", "invalid_configs"):
        assert validation[f"raw_{measure}"] == (
            validation[f"fleet_{measure}"] + validation[f"excluded_{measure}"]
        ), f"{measure}: raw != fleet + excluded"


def test_the_checked_configs_reconcile_with_the_enumeration(registry):
    """`--fleet` finds configs by the immediate-subdirectory scan, so it opens the 13
    enrolled projects AND the two worktrees the enumeration excludes by hand. The
    validator does not make that exclusion; this registry does, and states the arithmetic
    so the difference is checkable rather than folkloric."""
    validation = registry["validation"]
    enumeration = registry["enumeration"]

    assert validation["fleet_configs_checked"] == enumeration["enrolled"]
    assert validation["excluded_configs"] == len(validation["excluded_as_worktrees"])
    assert validation["excluded_as_worktrees"] == enumeration["excluded_as_worktrees"]
    assert validation["configs_checked"] == (
        validation["fleet_configs_checked"] + validation["excluded_configs"]
    )


def test_the_checked_configs_are_not_the_project_directories(registry):
    """A coincidence worth a standing guard: `configs_checked` and `project_directories`
    are both 15 and are different sets. The directories are 13 enrolled + 2 UNENROLLED,
    which carry no root config and were never opened. The configs are those 13 + 2
    WORKTREES. Asserting the two decompositions, rather than the equal totals, is what
    stops a later edit from "simplifying" one into the other."""
    validation = registry["validation"]
    enumeration = registry["enumeration"]

    assert validation["configs_checked"] == (
        enumeration["enrolled"] + validation["excluded_configs"]
    )
    assert enumeration["project_directories"] == (
        enumeration["enrolled"] + enumeration["unenrolled"]
    )
    for project in registry["projects"]:
        if not project["enrolled"]:
            assert "section_4_warnings" not in project, (
                f"{project['name']}: unenrolled, so the validator had no config to open"
            )


def test_the_excluded_warnings_are_a_second_reading_of_their_source_project(registry):
    """The gap is attributable, not a remainder. Both excluded configs are checkouts of
    `ai-project-system` at this Epic's branch, so each presents that project's config
    again and earns its warnings again — which is why the excess is exactly 2, and why
    errors and invalid counts show no excess at all: the source config is §4-VALID."""
    validation = registry["validation"]
    source = next(p for p in registry["projects"] if p["name"] == "ai-project-system")

    assert source["section_4"] == "valid"
    assert validation["excluded_warnings"] == (
        validation["excluded_configs"] * len(source["section_4_warnings"])
    )
    assert validation["excluded_errors"] == (
        validation["excluded_configs"] * len(source["section_4_errors"])
    )
    assert validation["excluded_invalid_configs"] == 0

    fleet_names = {p["name"] for p in registry["projects"]}
    for worktree in validation["excluded_as_worktrees"]:
        assert worktree not in fleet_names, f"{worktree} is not a fleet member"


def test_fleet_warnings_reconcile_with_the_schema_drift_finding(registry):
    """A second, independent derivation of the same 12, from a different part of the
    file. Every §4 warning in this measurement is one unknown-key occurrence — the
    validator's documented decision to warn where §4 is silent
    (`findings.schema_drift_class.unknown_key_gap`) — so the NOT-BLESSED fields'
    occurrence counts must sum to the fleet total. `framework_version` is absent from the
    sum because it was BLESSED into §3.6 / rule 26 and is no longer warned.

    The load-bearing assumption, stated rather than buried: ONE WARNING PER OCCURRENCE.
    A field can earn two findings in one config — `governance.version` does exactly that
    for ERRORS under rule 5 in `social-stories-creator` — so if that ever becomes true on
    the warning side, this test is the thing that notices."""
    drift = registry["findings"]["schema_drift_class"]
    warned = [f for f in drift["fields"] if f["disposition"].startswith("NOT BLESSED")]
    assert warned, "no warned fields: the finding and the totals have diverged"

    occurrences = sum(int(str(f["in_configs"]).split()[0]) for f in warned)
    assert occurrences == registry["validation"]["fleet_warnings"]
    assert int(str(drift["scope"]).split()[0]) == (
        registry["validation"]["fleet_configs_checked"]
    ), "the finding and the validation section disagree about how many configs are in scope"


def test_each_warned_field_occurrence_count_matches_the_project_entries(registry):
    """And the finding's per-field counts must match the project entries they summarise,
    or the aggregate agrees by luck. `5 of 13` for `created_at` means five enrolled
    projects list it — those five and no others."""
    drift = registry["findings"]["schema_drift_class"]
    enrolled = [p for p in registry["projects"] if p["enrolled"]]

    for field in (f for f in drift["fields"] if f["disposition"].startswith("NOT BLESSED")):
        expected = int(str(field["in_configs"]).split()[0])
        actual = sum(
            1
            for p in enrolled
            if any(field["field"] in warning for warning in p["section_4_warnings"])
        )
        assert actual == expected, (
            f"{field['field']}: finding says {expected}, project entries say {actual}"
        )
```

## C. Derivation

**`fleet_warnings: 12`** — sum of `section_4_warnings` over the 13 enrolled projects:

| project | warnings listed | n |
|---|---|---|
| ai-project-system | `cfo_review_gate` | 1 |
| drivr | `governance.submodule_path`, `project.created_at` | 2 |
| local-agent-runner | — | 0 |
| ai-project-system-mcp | `submodule_path`, `created_at` | 2 |
| panchew-io | — | 0 |
| social-stories-creator | `submodule_path`, `created_at` | 2 |
| home_finance | `submodule_path`, `created_at` | 2 |
| courtis | `submodule_path`, `created_at` | 2 |
| footboard | — | 0 |
| Getawayinsured2023 | — | 0 |
| voicebox | — | 0 |
| personal-management-system | — | 0 |
| fieldledger-assesment | `cfo_review_gate` | 1 |
| | **total** | **12** |

**Independent confirmation of the 12** — `findings.schema_drift_class` records occurrence counts for the fields the validator warns on: `created_at` 5 + `submodule_path` 5 + `cfo_review_gate` 2 = 12, at one warning per occurrence. `framework_version` (7 of 13) is excluded because its disposition is BLESSED. The two derivations use disjoint parts of the file and agree.

**`raw_warnings: 14`** — the recorded validator output, unchanged.

**`excluded_warnings: 2`** — 14 − 12, and it is attributable rather than residual. The enumeration states that `worktree-epic-E38.2` and `worktree-epic-E38.3` carry a `.ai-project.yml` because they are checkouts of `ai-project-system` at this branch, and that a naive depth-1 config scan counts them. `bin/ai-project-validate --fleet` performs that scan. Each therefore re-presents `ai-project-system`'s config, which carries exactly 1 warning. 2 × 1 = 2. Exact fit, no free parameter.

**Alternative rejected:** `ai-stack/comfyui/.ai-project.yml`. It sits at depth 2, and the enumeration is explicit that fleet-level discovery is immediate subdirectories only. It also cannot compete: if the scan reached the worktrees (and the 2-warning excess is the evidence it did), they already account for the full gap, leaving nothing for comfyui to contribute.

**`configs_checked: 15`** = 13 enrolled + 2 worktrees. Numerically equal to `project_directories: 15` but a different set — the overlap is 13. Flagged in the file and guarded by a test, since this is the single most likely thing for a future reader to misread.

**Errors and invalid configs** — per-project error lists sum to 1 (`mcp`) + 4 (`social-stories-creator`) + 2 (`home_finance`) + 1 (`courtis`) = 8, matching the existing `total_errors: 8` and the prose "4 of 13 ... carrying 8 errors". The worktrees clone a §4-VALID config, so `excluded_errors: 0` and `excluded_invalid_configs: 0`, and raw equals fleet for both. Written out anyway so the section has no scope-ambiguous count left.

**Assumptions, stated inline as required:** (1) one warning per unknown-key occurrence — supported by both derivations agreeing; (2) `--fleet` uses depth-1 config discovery — supported by the 2-warning excess and by the enumeration's description of the defect; (3) the worktree configs are identical to their source, since they are checkouts of the same branch; (4) `measured: 2026-08-11` stays — this re-presents the existing run's numbers, it does not re-measure, and re-dating it would falsify the record; (5) `registry_version` tracks the schema, hence `1.1.0`. On (5) I cannot inspect Drivr from this packet: if Drivr keys directly on `validation.total_warnings`, the removal is a breaking read and the bump should be `2.0.0` instead — same one-line edit, and worth a Milestone Chat question rather than a unilateral call.

Sanity check performed: re-read the task's three numbered requirements against the deliverable (totals separated; checked/excluded/why fields added; invariant test added), re-added the warning column twice, verified the two derivations of 12 are independent, verified none of the new YAML keys collide with the forbidden set in `test_no_automation_field_exists_anywhere_in_the_registry`, and verified the two YAML plain scalars the new tests parse (`in_configs: 5 of 13`, `scope: 13 enrolled projects`) are strings and are handled as such.

result: Registry `validation:` section rewritten to split `total_warnings: 14` into `fleet_warnings: 12` / `raw_warnings: 14` / `excluded_warnings: 2` (plus scope-named error and invalid-config counts and checked/excluded config counts), with the 12 derived twice independently from the registry and the 2-warning gap attributed to the two git-worktree checkouts of `ai-project-system`, and eight new pytest invariant tests supplied.

TOOLS USED: Read (once, on /tmp/claude-1000/-home-panchew/41aa5209-0deb-4db9-942b-c02f03ef59ba/scratchpad/e38.6-paid-run2-sealed/PACKET.txt)