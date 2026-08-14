I have the file contents from your message, but this session exposes no file-read/write/bash tools — I can't edit `.ai-project/registry/fleet-registry.yml` or `tests/test_fleet_registry.py` on disk. Below are the exact replacement blocks to paste in. Nothing else in either file needs to change.

## The numbers, derived from the registry

Summing `section_4_warnings` over the 13 enrolled projects:

| project | warnings |
|---|---|
| ai-project-system | 1 (`cfo_review_gate`) |
| drivr | 2 |
| ai-project-system-mcp | 2 |
| social-stories-creator | 2 |
| home_finance | 2 |
| courtis | 2 |
| fieldledger-assesment | 1 (`cfo_review_gate`) |
| local-agent-runner, panchew-io, footboard, Getawayinsured2023, voicebox, personal-management-system | 0 |
| **fleet total** | **12** |

The gap to 14 is exactly 2, and it is attributable rather than floating: the two excluded directories are git worktrees *of `ai-project-system` itself*, so each carries that project's config verbatim — 1 `cfo_review_gate` warning each.

This is independently confirmed by `findings.schema_drift_class`, which records the three NOT-BLESSED fields at `created_at` 5/13 + `submodule_path` 5/13 + `cfo_review_gate` 2/13 = 12. Two sections of the registry that were written from different measurements agree.

Errors need no split: 1 + 4 + 2 + 1 = 8 across the four invalid enrolled configs, and the worktree configs (copies of a §4-valid project) contribute 0. I kept `total_errors` and made that coincidence explicit rather than silent, since it's a fact about this measurement, not a property of the method.

## Replacement for the `validation:` block (and its preceding comment tail)

Replace the last paragraph of the `§4 VALIDATION` comment header and the `validation:` mapping with:

```yaml
# No project became invalid that was not already invalid on presence alone.
#
# ---------------------------------------------------------------------------
# TWO WARNING TOTALS, BECAUSE THE VALIDATOR CHECKED MORE THAN THE FLEET
# ---------------------------------------------------------------------------
#
# `bin/ai-project-validate --fleet ~/soft-dev` walks immediate subdirectories carrying a
# `.ai-project.yml`. That set is NOT the fleet: it includes `worktree-epic-E38.2` and
# `worktree-epic-E38.3`, which are git worktrees of `ai-project-system` and are excluded
# from the fleet by `enumeration.excluded_as_worktrees` above. So the validator checked
# 15 configs, of which 13 are fleet projects.
#
# The earlier single `total_warnings: 14` was the RAW figure and was not wrong — it was
# unreadable. A reader could not tell whether 14 described the fleet or described what
# the tool happened to walk, and the two differ by exactly the defect this Epic exists
# to guard against. Both are recorded, and the gap between them is attributed:
#
#   fleet_warnings     12   sum of `section_4_warnings` over the 13 enrolled projects
#   excluded_warnings   2   2 worktrees x 1 warning each (`cfo_review_gate`), because a
#                           worktree is a checkout of `ai-project-system` and carries
#                           that project's config verbatim
#   raw_warnings       14   what the validator printed
#
# The 12 is corroborated by `findings.schema_drift_class` from a separate measurement:
# `created_at` 5 + `submodule_path` 5 + `cfo_review_gate` 2 = 12 warned occurrences over
# the same 13 configs. `framework_version` is blessed (§4 rule 26) and is not warned.
#
# ERRORS ARE NOT SPLIT, and that is a fact about this measurement rather than about the
# method: `ai-project-system` is §4-valid, so its two worktrees contribute 0 errors and
# the fleet and raw error totals both read 8. `fleet_errors` and `excluded_errors` are
# recorded anyway so a future measurement where they diverge cannot do so silently.

validation:
  measured: 2026-08-11
  command: bin/ai-project-validate --fleet ~/soft-dev

  # What the command actually walked, split by whether it is fleet or not.
  configs_checked: 15
  fleet_configs_checked: 13
  excluded_configs_checked: 2
  excluded_configs: [worktree-epic-E38.2, worktree-epic-E38.3]
  excluded_reason: >-
    Git worktrees of `ai-project-system` itself, confirmed by `git worktree list` and by
    each holding a `.git` FILE rather than a directory. They carry a `.ai-project.yml`
    only because they are checkouts of this repository. Excluded from the fleet by
    `enumeration.excluded_as_worktrees`; the validator has no such notion and counted
    them, which is the whole reason the raw and fleet totals differ.

  invalid_configs: 4

  total_errors: 8
  fleet_errors: 8
  excluded_errors: 0

  fleet_warnings: 12
  excluded_warnings: 2
  raw_warnings: 14
  excluded_warnings_basis: >-
    Each excluded worktree is a checkout of `ai-project-system` and so reproduces that
    project's single warning (`cfo_review_gate`, top-level, no §4 rule): 2 x 1 = 2. The
    gap is derived from a named source, not asserted as a residual.
```

## Additions to `tests/test_fleet_registry.py`

Append after `test_worktrees_are_excluded_and_the_exclusion_is_stated`, before the Binding Constraint 5 section:

```python
# ---------------------------------------------------------------------------
# §4 totals — the fleet total, the raw total, and the gap between them
# ---------------------------------------------------------------------------
#
# Same rule as everywhere else in this file: nothing here re-measures the fleet. These
# read the committed registry and hold it to its own arithmetic, so that a hand-edited
# total cannot drift away from the per-project evidence it is supposed to summarise.


def _enrolled(registry):
    return [p for p in registry["projects"] if p["enrolled"]]


def test_the_warning_totals_are_separated_not_aggregated(registry):
    """`total_warnings` was one number doing two jobs — a reader could not tell whether
    it described the fleet or described whatever the validator happened to walk. The
    field is gone on purpose; its return would restore the ambiguity."""
    validation = registry["validation"]
    assert "total_warnings" not in validation, (
        "`total_warnings` conflates fleet warnings with warnings from configs that are "
        "not fleet members; use fleet_warnings / raw_warnings"
    )
    for field in ("fleet_warnings", "excluded_warnings", "raw_warnings",
                  "configs_checked", "fleet_configs_checked", "excluded_configs_checked"):
        assert field in validation, f"validation is missing derived field {field!r}"


def test_the_raw_warning_total_is_the_fleet_total_plus_the_excluded_configs(registry):
    """The invariant that makes both numbers safe to quote: they reconcile, and the
    difference is accounted for rather than absorbed."""
    validation = registry["validation"]
    assert validation["raw_warnings"] == (
        validation["fleet_warnings"] + validation["excluded_warnings"]
    )
    assert validation["raw_warnings"] >= validation["fleet_warnings"]


def test_the_fleet_warning_total_is_the_sum_of_the_enrolled_projects(registry):
    """A fleet total counts fleet projects. Not the projects the tool walked."""
    counted = sum(len(p.get("section_4_warnings") or []) for p in _enrolled(registry))
    assert registry["validation"]["fleet_warnings"] == counted

    for project in registry["projects"]:
        if not project["enrolled"]:
            assert not project.get("section_4_warnings"), (
                f"{project['name']}: unenrolled, so §4 does not apply and it cannot "
                f"contribute to a §4 warning total"
            )


def test_the_configs_checked_split_matches_the_enumeration(registry):
    """`validation` and `enumeration` were measured by different means on the same day.
    If they disagree about how many configs exist and how many were excluded, one of
    them is stale and neither can be trusted."""
    validation, enumeration = registry["validation"], registry["enumeration"]

    assert validation["fleet_configs_checked"] == enumeration["enrolled"]
    assert validation["excluded_configs_checked"] == len(enumeration["excluded_as_worktrees"])
    assert validation["configs_checked"] == (
        validation["fleet_configs_checked"] + validation["excluded_configs_checked"]
    )
    assert validation["excluded_configs"] == enumeration["excluded_as_worktrees"]


def test_the_excluded_warnings_are_attributed_not_left_as_a_residual(registry):
    """The gap is not a floating correction term. Each excluded directory is a git
    worktree of `ai-project-system`, so it carries that project's config verbatim and
    contributes exactly that project's warnings — if the source project's warnings
    change, the gap has to change with them."""
    validation = registry["validation"]
    source = next(p for p in registry["projects"] if p["name"] == "ai-project-system")
    per_worktree = len(source["section_4_warnings"])

    assert validation["excluded_warnings"] == (
        validation["excluded_configs_checked"] * per_worktree
    )
    assert validation.get("excluded_reason", "").strip(), "exclusion stated, not silent"
    assert validation.get("excluded_warnings_basis", "").strip()


def test_the_error_totals_reconcile_the_same_way(registry):
    """Errors happen to be unambiguous at this measurement — `ai-project-system` is
    §4-valid, so its worktrees carry none. That is a fact about 2026-08-11, not about
    the method, so the split is recorded and asserted rather than assumed permanent."""
    validation = registry["validation"]
    counted = sum(len(p.get("section_4_errors") or []) for p in _enrolled(registry))

    assert validation["fleet_errors"] == counted
    assert validation["total_errors"] == validation["fleet_errors"] + validation["excluded_errors"]
    assert validation["invalid_configs"] == sum(
        1 for p in _enrolled(registry) if p["section_4"] == "invalid"
    )


def test_the_fleet_warning_total_agrees_with_the_recorded_schema_drift(registry):
    """A cross-check between two sections written from independent measurements: every
    fleet warning is an unblessed field occurrence, so the per-field counts in
    `findings.schema_drift_class` must sum to `fleet_warnings`. `framework_version` is
    blessed (§4 rule 26) and is not warned, so it is excluded here."""
    fields = registry["findings"]["schema_drift_class"]["fields"]
    warned = [f for f in fields if str(f["disposition"]).startswith("NOT BLESSED")]
    assert warned, "no warned fields recorded, so this cross-check proves nothing"

    occurrences = 0
    for field in warned:
        count, _, scope = str(field["in_configs"]).partition(" of ")
        occurrences += int(count)
        assert int(scope) == registry["enumeration"]["enrolled"], (
            f"{field['field']}: drift measured over a different scope than the fleet"
        )

    assert registry["validation"]["fleet_warnings"] == occurrences
```

## Notes

- The blessed `framework_version` (7/13) is deliberately excluded from the drift cross-check — it's an optional §4 field under rule 26 and produces no warning. If it were counted the sum would be 19, not 12.
- I did not touch `bin/ai-project-validate`, the enumeration block, or any governance doc. Worth flagging separately: the validator itself has no concept of worktree exclusion, which is *why* these two totals differ at all. Teaching it that is a change to the tool's contract and belongs to whoever owns it.
- I haven't run the suite (no execution tools here). The new tests read only keys that the replacement `validation:` block defines, plus `enumeration`, `projects`, and `findings.schema_drift_class`, all unchanged.
