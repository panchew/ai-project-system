"""Invariant guard for `.ai-project/registry/fleet-registry.yml` (Epic P11-M38-E38.3).

**What this file does NOT do:** it does not re-measure the fleet. Every assertion reads
only the committed registry. A test that walked `~/soft-dev` would pass or fail on the
state of one developer's machine, which is not a property of this repository — and the
registry is a **record**, so its correctness at a date is established by the evidence in
the Delivery Notice, not by re-deriving it on every suite run.

**What it does do** is hold the things that must not drift regardless of what the fleet
looks like: the CFO's three state definitions are verbatim, every project carries a
classification, proposals are marked as proposals, and — the one that matters most —
**nothing automatic exists**. Binding Constraint 5 (`P11-M38`) makes fleet-state
transitions a recorded human action, on a returned CFO proposal rather than a settled
question, and the registry is one convenience away from being the input to a scheduler
(`M40`) it is explicitly not allowed to become.
"""

from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = REPO_ROOT / ".ai-project" / "registry" / "fleet-registry.yml"

# The CFO's definitions. Reproduced here verbatim from the Epic Spec's §Scope-1 table so
# that a reword in either place fails loudly instead of drifting quietly.
CFO_STATE_DEFINITIONS = {
    "active": "Enrolled in the registry. Receives time and attention.",
    "benched": "Not currently receiving attention. May return.",
    "archived": "Not planned to ever be touched again — though it can be brought back to life.",
}

VALID_STATES = set(CFO_STATE_DEFINITIONS)
VALID_BASES = {"recorded", "proposed"}


@pytest.fixture(scope="module")
def registry():
    return yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))


def test_registry_exists_and_parses(registry):
    """Drivr reads this file (`SN-27` decision 5). A registry Drivr cannot parse has
    missed the point."""
    assert isinstance(registry, dict)
    assert registry["registry_version"] == "1.0.0"


def test_the_three_state_definitions_are_the_cfos_verbatim(registry):
    states = registry["states"]
    assert set(states) == VALID_STATES
    for name, expected in CFO_STATE_DEFINITIONS.items():
        assert states[name]["definition"] == expected, f"{name} definition is not verbatim"


def test_there_are_exactly_three_states(registry):
    """Three, not two and not four. A fourth state would be a redefinition of the
    fleet's vocabulary, which is not an epic's to make."""
    assert len(registry["states"]) == 3


def test_every_project_carries_a_classification(registry):
    for project in registry["projects"]:
        assert project["state"] in VALID_STATES, f"{project['name']}: bad state"
        assert project["state_basis"] in VALID_BASES, f"{project['name']}: bad basis"
        assert project.get("rationale", "").strip(), f"{project['name']}: no rationale"


def test_every_project_names_its_enrollment_and_section_4_status(registry):
    """Enrollment and §4 validity are different axes and the registry carries both."""
    for project in registry["projects"]:
        assert isinstance(project["enrolled"], bool), project["name"]
        assert project["section_4"] in {"valid", "invalid", "not_applicable"}, project["name"]
        if project["section_4"] == "invalid":
            assert project["section_4_errors"], f"{project['name']}: invalid but no errors listed"
        if project["section_4"] == "valid":
            assert project["section_4_errors"] == [], f"{project['name']}: valid but errors listed"


def test_unenrolled_projects_are_still_classified(registry):
    """`ai-stack` and `character-factory` resolve as a side effect of classification,
    not as a separate decision. Enrollment is not a registry state."""
    unenrolled = [p for p in registry["projects"] if not p["enrolled"]]
    assert {p["name"] for p in unenrolled} == {"ai-stack", "character-factory"}
    for project in unenrolled:
        assert project["state"] in VALID_STATES
        assert project["section_4"] == "not_applicable"


@pytest.mark.parametrize("name", ["panchew-io", "fieldledger-assesment", "drivr"])
def test_the_three_projects_named_explicitly_are_present(name):
    """Named in the Epic's DoD because each was missed by an earlier fleet list:
    `panchew-io` appeared in no phase artifact until M38's planning; `drivr` was created
    during this milestone; `fieldledger-assesment` was dropped from P10's scope, and
    dropping from a phase's scope is explicitly not a registry state."""
    data = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    assert name in {p["name"] for p in data["projects"]}


def test_project_names_are_unique(registry):
    names = [p["name"] for p in registry["projects"]]
    assert len(names) == len(set(names))


def test_project_count_matches_the_stated_enumeration(registry):
    """The enumeration block states its method and its counts; the project list must
    agree with it, or one of the two is stale."""
    enumeration = registry["enumeration"]
    projects = registry["projects"]

    assert len(projects) == enumeration["project_directories"]
    assert sum(1 for p in projects if p["enrolled"]) == enumeration["enrolled"]
    assert sum(1 for p in projects if not p["enrolled"]) == enumeration["unenrolled"]
    assert sum(1 for p in projects if p["section_4"] == "valid") == enumeration["section_4_valid"]
    assert sum(1 for p in projects if p["section_4"] == "invalid") == enumeration["section_4_invalid"]


def test_worktrees_are_excluded_and_the_exclusion_is_stated(registry):
    """Two of the 17 directories under the fleet root are git worktrees of this very
    repository. A naive `for d in */; do [ -f "$d/.ai-project.yml" ]` counts them as
    fleet members. The exclusion is recorded, not silent."""
    excluded = registry["enumeration"]["excluded_as_worktrees"]
    assert len(excluded) == 2
    assert registry["enumeration"]["directories_found"] == len(registry["projects"]) + len(excluded)
    names = {p["name"] for p in registry["projects"]}
    for worktree in excluded:
        assert worktree not in names


def test_fleet_and_raw_warning_totals_are_distinct_and_derived(registry):
    """The raw ``--fleet`` run included two worktree configs. Its warning total must
    not be presented as the total for the 13 enrolled fleet projects."""
    validation = registry["validation"]
    projects = registry["projects"]
    enrolled = [project for project in projects if project["enrolled"]]

    assert validation["fleet_configs"] == len(enrolled)
    assert validation["fleet_total_warnings"] == sum(
        len(project["section_4_warnings"]) for project in enrolled
    )
    assert validation["excluded_worktree_configs"] == len(
        registry["enumeration"]["excluded_as_worktrees"]
    )
    assert validation["raw_configs_checked"] == (
        validation["fleet_configs"] + validation["excluded_worktree_configs"]
    )
    assert validation["raw_total_warnings"] == 14
    assert validation["fleet_total_warnings"] == 12
    assert validation["raw_total_warnings"] != validation["fleet_total_warnings"]


# ---------------------------------------------------------------------------
# Binding Constraint 5 — nothing automatic. The guard that matters most.
# ---------------------------------------------------------------------------


def test_transitions_are_recorded_not_derived(registry):
    """A transition is a human decision appended by hand. The list starts empty because
    the initial classifications are the registry's first state, not transitions — and
    the `proposed` ones are not decisions at all."""
    assert registry["transitions"] == []


def test_no_automation_field_exists_anywhere_in_the_registry(registry):
    """The registry RECORDS state; it does not ACT on state. This asserts the absence of
    the shape a scheduler would need — no trigger, no schedule, no rule that would let
    something move a project without a human recording it."""
    forbidden = {"auto_transition", "auto_archive", "schedule", "cron", "trigger",
                 "on_inactivity", "inactivity_threshold", "watch", "poll", "queue", "priority"}

    def walk(node, path="root"):
        if isinstance(node, dict):
            for key, value in node.items():
                assert key not in forbidden, f"automation-shaped key {key!r} at {path}"
                walk(value, f"{path}.{key}")
        elif isinstance(node, list):
            for i, value in enumerate(node):
                walk(value, f"{path}[{i}]")

    walk(registry)


def test_proposed_classifications_are_marked_as_proposals(registry):
    """Where the record is silent the registry proposes rather than asserts — the CFO
    owns the fleet's attention. A registry that quietly guesses is worse than one with a
    stated unknown, so every proposal says so in its own rationale too."""
    proposed = [p for p in registry["projects"] if p["state_basis"] == "proposed"]
    assert proposed, "a registry with no proposals has almost certainly asserted something"
    for project in proposed:
        assert "PROPOSED" in project["rationale"], f"{project['name']}: proposal not flagged in its rationale"


def test_archived_is_never_asserted_without_a_recorded_intent(registry):
    """`archived` claims an intent — 'not planned to ever be touched again' — that only
    the CFO can hold. It may never be applied on a `proposed` basis; if the record does
    not contain the intent, the weaker claim (`benched`) is the honest one."""
    for project in registry["projects"]:
        if project["state"] == "archived":
            assert project["state_basis"] == "recorded", (
                f"{project['name']}: archived on a proposed basis asserts an intent the record does not hold"
            )
