"""Tests for ``bin/ai-project-validate`` — the first enforcement of
``governance/ai-project-yml-spec.md`` §4 (P10-GH-5, Epic P11-M38-E38.3).

Three things these tests are deliberately built to hold:

1. **Warnings and errors stay distinguishable.** §4 rules 11, 16 and 22 say unknown
   keys ``MUST produce a validation warning (not an error)``; rules 12, 17 and 23 say
   invalid values ``MUST produce a validation error``. A validator that collapses the
   two has not enforced §4, so the distinction is asserted directly rather than left
   to the error count.

2. **Key identification is structural, not textual.** ``test_key_detection_is_structural_not_textual``
   is the guard that matters most: a config mentioning ``framework_version`` only inside
   a comment and inside a quoted string must not be read as carrying the key. This
   phase has been bitten twice by text-shaped measurement — once by a comment line
   matching a naive ``grep framework_version``, once by bold markup inside a phrase
   making a literal search miss a sentence that was really there (``P11-GH-2``).

3. **No host dependency.** Every case is a fixture under ``tmp_path`` or this repo's
   own committed config. Nothing here reads ``~/soft-dev``; the fleet run is evidence
   recorded in the Delivery Notice, not a test.
"""

import importlib.util
import sys
import json
from importlib.machinery import SourceFileLoader
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
VALIDATOR_PATH = REPO_ROOT / "bin" / "ai-project-validate"


def _load_validator():
    """The script is extensionless, so load it by path — the same spec_from_loader
    approach tests/test_model_config.py and tests/test_visual_artifacts_config.py use
    (``load_module()`` would work but is deprecated and would add a suite warning)."""
    loader = SourceFileLoader("ai_project_validate", str(VALIDATOR_PATH))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
    # Registered before exec_module because the validator uses `from __future__ import
    # annotations` with @dataclass: resolving those deferred annotations makes
    # dataclasses look the module up in sys.modules, which fails if it is not there.
    sys.modules[loader.name] = module
    loader.exec_module(module)
    return module


validator = _load_validator()


MINIMAL_VALID = """\
governance:
  source: https://github.com/panchew/ai-project-system
  version: "7.1.0"
  ref: v7.1.0

project:
  name: my-project
  description: "A project using the AI Project System"
"""


def check(text, path=".ai-project.yml"):
    return validator.validate_text(text, path)


def rules_of(findings):
    return sorted(f.rule for f in findings if f.rule is not None)


def fields_of(findings):
    return sorted(f.field for f in findings)


# ---------------------------------------------------------------------------
# The baseline: a minimal valid config produces nothing at all.
# ---------------------------------------------------------------------------


def test_minimal_valid_config_is_clean():
    report = check(MINIMAL_VALID)
    assert report.valid
    assert report.findings == []


def test_repo_own_config_is_section_4_valid():
    """This repository's own committed config must satisfy the spec it publishes."""
    report = validator.validate_file(REPO_ROOT / ".ai-project.yml")
    assert report.valid, [f.as_dict() for f in report.errors]


# ---------------------------------------------------------------------------
# Rules 1 and 2 — the file itself.
# ---------------------------------------------------------------------------


def test_rule_1_wrong_filename_is_an_error():
    report = check(MINIMAL_VALID, path="/tmp/project.yml")
    assert not report.valid
    assert 1 in rules_of(report.errors)


def test_rule_2_unparseable_yaml_is_a_single_error():
    report = check("governance:\n  source: [unclosed\n")
    assert not report.valid
    assert rules_of(report.errors) == [2]
    # Nothing downstream is checkable, so nothing downstream is claimed.
    assert len(report.findings) == 1


def test_rule_2_empty_file_is_an_error():
    report = check("")
    assert not report.valid
    assert rules_of(report.errors) == [2]


def test_rule_2_non_mapping_top_level_is_an_error():
    report = check("- just\n- a list\n")
    assert not report.valid
    assert rules_of(report.errors) == [2]


# ---------------------------------------------------------------------------
# Rule 3 — the FIVE required fields.
# ---------------------------------------------------------------------------


def test_required_fields_are_exactly_five_and_named():
    """§4 rule 3 read 'All four required fields' while listing five, from spec v1.0.0
    until v2.8.0 corrected it (Epic P11-M38-E38.3). Five is right: §3.1 marks five
    REQUIRED and §3.2 documents five. This asserts the validator's own list, so the
    four-versus-five defect cannot re-enter through this side."""
    assert len(validator.REQUIRED_FIELDS) == 5
    assert set(validator.REQUIRED_FIELDS) == {
        "governance.source",
        "governance.version",
        "governance.ref",
        "project.name",
        "project.description",
    }


def test_framework_version_is_not_a_required_field():
    """P10-GH-1 blessed `framework_version` as OPTIONAL (rule 26), which is precisely
    why rule 3's corrected count is five and not six — it never belonged in that list.
    6 of 13 enrolled configs carried no stamp at 2026-08-11; requiring one would have
    invalidated all six."""
    assert "framework_version" not in validator.REQUIRED_FIELDS
    report = check(MINIMAL_VALID)
    assert report.valid
    assert not any(f.field == "framework_version" for f in report.findings)


@pytest.mark.parametrize(
    "missing",
    ["governance.source", "governance.version", "governance.ref", "project.name", "project.description"],
)
def test_rule_3_each_missing_required_field_is_an_error(missing):
    block, key = missing.split(".")
    lines = [ln for ln in MINIMAL_VALID.splitlines() if not ln.strip().startswith(f"{key}:")]
    report = check("\n".join(lines) + "\n")
    assert not report.valid
    assert missing in fields_of(report.errors)
    assert 3 in rules_of(report.errors)


def test_rule_3_absent_blocks_report_every_missing_field():
    report = check("framework_version: v7.1.0\n")
    assert not report.valid
    assert set(fields_of(report.errors)) == set(validator.REQUIRED_FIELDS)


# ---------------------------------------------------------------------------
# Rules 4-8 — the format constraints. Presence is not validity.
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "source",
    ["https://github.com/panchew/ai-project-system", "./governance", "./.governance", "../shared/governance"],
)
def test_rule_4_accepts_https_and_relative_sources(source):
    report = check(MINIMAL_VALID.replace("https://github.com/panchew/ai-project-system", source))
    assert report.valid, [f.as_dict() for f in report.errors]


@pytest.mark.parametrize(
    "source",
    [
        "/absolute/path",
        "git@github.com:panchew/ai-project-system.git",
        "http://github.com/panchew/ai-project-system",
        "governance",
    ],
)
def test_rule_4_rejects_absolute_ssh_http_and_bare_paths(source):
    report = check(MINIMAL_VALID.replace("https://github.com/panchew/ai-project-system", source))
    assert not report.valid
    assert 4 in rules_of(report.errors)


def test_rule_5_unquoted_version_is_an_error():
    """The whole point of rule 5's 'quoted': `version: 2.0` loads as a float. The
    quoting is a fact about the document that a parsed value has already discarded,
    which is why the validator reads the YAML node's scalar style."""
    report = check(MINIMAL_VALID.replace('version: "7.1.0"', "version: 7.1.0"))
    assert not report.valid
    assert 5 in rules_of(report.errors)
    assert any("quoted" in f.message for f in report.errors)


def test_rule_5_v_prefixed_version_is_an_error():
    report = check(MINIMAL_VALID.replace('version: "7.1.0"', 'version: "v7.1.0"'))
    assert not report.valid
    assert 5 in rules_of(report.errors)


@pytest.mark.parametrize("bad", ['"latest"', '"^2.0.0"', '"7.1"'])
def test_rule_5_rejects_non_semver_versions(bad):
    report = check(MINIMAL_VALID.replace('version: "7.1.0"', f"version: {bad}"))
    assert not report.valid
    assert 5 in rules_of(report.errors)


def test_rule_6_empty_ref_is_an_error():
    report = check(MINIMAL_VALID.replace("ref: v7.1.0", 'ref: ""'))
    assert not report.valid
    assert 6 in rules_of(report.errors)


@pytest.mark.parametrize("name", ["home_finance", "MyProject", "9lives", "my project", "-leading"])
def test_rule_7_rejects_non_slug_names(name):
    report = check(MINIMAL_VALID.replace("name: my-project", f"name: {name!r}"))
    assert not report.valid
    assert 7 in rules_of(report.errors)


@pytest.mark.parametrize("name", ["my-project", "ai-project-system", "voicebox", "getawayinsured2023"])
def test_rule_7_accepts_slug_names(name):
    report = check(MINIMAL_VALID.replace("name: my-project", f"name: {name}"))
    assert report.valid, [f.as_dict() for f in report.errors]


def test_rule_8_empty_description_is_an_error():
    report = check(MINIMAL_VALID.replace('description: "A project using the AI Project System"', 'description: "   "'))
    assert not report.valid
    assert 8 in rules_of(report.errors)


# ---------------------------------------------------------------------------
# The normative warning/error split — rules 11/16/22 against 12/17/23.
# ---------------------------------------------------------------------------


def test_rule_11_unknown_override_key_warns_and_stays_valid():
    report = check(MINIMAL_VALID + "\noverrides:\n  branch_strategy: gitflow\n  future_key: whatever\n")
    assert report.valid
    assert rules_of(report.warnings) == [11]
    assert report.errors == []


@pytest.mark.parametrize(
    "block",
    [
        "overrides:\n  branch_strategy: octopus\n",
        "overrides:\n  merge_strategy: cherry-pick\n",
        "overrides:\n  epic_prefix: feature\n",
        'overrides:\n  epic_prefix: ""\n',
    ],
)
def test_rule_12_invalid_override_values_are_errors(block):
    report = check(MINIMAL_VALID + "\n" + block)
    assert not report.valid
    assert 12 in rules_of(report.errors)


def test_rule_16_unknown_models_key_warns_and_stays_valid():
    report = check(MINIMAL_VALID + "\nmodels:\n  hq: remote:claude-opus-5\n  epic_reviewer: remote:claude-opus-5\n")
    assert report.valid
    assert rules_of(report.warnings) == [16]


@pytest.mark.parametrize("route", ["claude-opus-5", "cloud:claude-opus-5", "remote:", "remote:model/with/slashes"])
def test_rule_17_invalid_model_routes_are_errors(route):
    report = check(MINIMAL_VALID + f"\nmodels:\n  hq: {route!r}\n")
    assert not report.valid
    assert 17 in rules_of(report.errors)


@pytest.mark.parametrize("route", ["remote:claude-opus-5", "local:qwen3-coder:30b", "remote:qwen3.6:27b", "remote:kimi-k3"])
def test_rule_15_accepts_well_formed_model_routes(route):
    report = check(MINIMAL_VALID + f"\nmodels:\n  hq: {route}\n")
    assert report.valid, [f.as_dict() for f in report.errors]


def test_rule_22_unknown_visual_artifacts_key_warns_and_stays_valid():
    report = check(MINIMAL_VALID + "\nvisual_artifacts:\n  enabled: true\n  render_farm: somewhere\n")
    assert report.valid
    assert rules_of(report.warnings) == [22]


@pytest.mark.parametrize(
    "block",
    [
        "visual_artifacts:\n  enabled: yes-please\n",  # rules 19 + 23
        "visual_artifacts:\n  types:\n    - screenshots\n",  # rules 20 + 23
        "visual_artifacts:\n  comfyui_url: not-a-url\n",  # rules 21 + 23
        "visual_artifacts:\n  comfyui_url: ftp://host/x\n",  # rules 21 + 23
        "visual_artifacts:\n  visual_required_for_specs: sometimes\n",  # rules 25 + 23
    ],
)
def test_rule_23_invalid_visual_artifacts_values_are_errors(block):
    report = check(MINIMAL_VALID + "\n" + block)
    assert not report.valid
    assert 23 in rules_of(report.errors)


def test_rule_24_absent_visual_artifacts_block_is_valid_and_silent():
    """§4 rule 24 is explicit that an absent block is valid at documented defaults —
    no error AND no warning."""
    report = check(MINIMAL_VALID)
    assert report.valid
    assert not any("visual_artifacts" in f.field for f in report.findings)


def test_warnings_alone_never_make_a_config_invalid():
    """The single most important behaviour to hold: §4's warnings are forward-
    compatibility signals, not validity judgments."""
    report = check(
        MINIMAL_VALID
        + "\noverrides:\n  unknown_a: 1\n"
        + "\nmodels:\n  unknown_b: 2\n"
        + "\nvisual_artifacts:\n  unknown_c: 3\n"
        + "\ncreated_at: 2026-08-11T00:00:00Z\n"
    )
    assert report.valid
    assert report.errors == []
    assert len(report.warnings) == 4


# ---------------------------------------------------------------------------
# Rule 26 — framework_version, blessed by P10-GH-1 at spec v2.8.0.
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("stamp", ["v7.1.0", "v7.0.0", "7.1.0"])
def test_rule_26_accepts_the_fleet_stamp_forms(stamp):
    """The `v?` in the pattern is load-bearing. Every stamp on the machine at
    2026-08-11 was v-prefixed (`v7.0.0` x6, `v7.1.0` x1); requiring a bare semver
    would have invalidated all seven — a fleet-wide reconciliation this Epic was
    explicitly forbidden to perform."""
    report = check(MINIMAL_VALID + f"\nframework_version: {stamp}\n")
    assert report.valid, [f.as_dict() for f in report.errors]


@pytest.mark.parametrize("stamp", ["latest", "v7", "''", "7.1.0-rc1"])
def test_rule_26_rejects_non_version_stamps(stamp):
    report = check(MINIMAL_VALID + f"\nframework_version: {stamp}\n")
    assert not report.valid
    assert 26 in rules_of(report.errors)


def test_framework_version_is_no_longer_an_unknown_key():
    """Before P10-GH-1 it appeared zero times in the spec and would have warned as
    schema drift. After the fold-in it is a recognised optional field."""
    report = check(MINIMAL_VALID + "\nframework_version: v7.1.0\n")
    assert report.findings == []
    assert "framework_version" in validator.KNOWN_TOP_LEVEL


# ---------------------------------------------------------------------------
# Unknown keys where §4 is SILENT — the schema-drift class (Finding 4).
# ---------------------------------------------------------------------------


def test_unknown_keys_outside_the_three_blocks_warn_with_no_rule_number():
    """§4's unknown-key rules (11, 16, 22) cover only `overrides`, `models` and
    `visual_artifacts`. Top level, `governance:` and `project:` have no rule at all.
    The validator warns by its own documented decision, and reports `rule: None` so
    the treatment is never mistaken for §4 enforcement."""
    report = check(
        MINIMAL_VALID.replace("  ref: v7.1.0", "  ref: v7.1.0\n  submodule_path: .governance/")
        .replace("  name: my-project", "  name: my-project\n  created_at: 2026-08-11T00:00:00Z")
        + "\ncfo_review_gate: enabled\n"
    )
    assert report.valid
    assert len(report.warnings) == 3
    assert all(f.rule is None for f in report.warnings)
    assert fields_of(report.warnings) == ["cfo_review_gate", "governance.submodule_path", "project.created_at"]


def test_the_three_unblessed_drift_fields_are_not_silently_accepted():
    """`created_at`, `submodule_path` and `cfo_review_gate` were NOT schema-blessed by
    this Epic (recommend-and-escalate, not act). They must remain visible as warnings
    rather than being normalised away."""
    for key in ("created_at", "submodule_path", "cfo_review_gate"):
        assert key not in validator.KNOWN_TOP_LEVEL
        assert key not in validator.KNOWN_GOVERNANCE
        assert key not in validator.KNOWN_PROJECT


# ---------------------------------------------------------------------------
# The anti-grep guard — P11-GH-2's lesson where it costs something.
# ---------------------------------------------------------------------------


def test_key_detection_is_structural_not_textual():
    """A naive substring or even a line-anchored grep gets this wrong three ways:
    a commented-out key, a key name inside a quoted value, and a key name appearing
    at the start of a line inside a block scalar. None of them are keys."""
    text = """\
# framework_version: v7.1.0   <- a comment, not a key
governance:
  source: https://github.com/panchew/ai-project-system
  version: "7.1.0"
  ref: v7.1.0

project:
  name: my-project
  description: "Mentions framework_version and created_at in prose"
"""
    report = check(text)
    assert report.valid
    # No warnings: neither the comment nor the prose introduced an unknown key.
    assert report.findings == []


def test_a_key_is_scoped_to_its_own_block():
    """`version:` under `project:` is not `governance.version`. A line-anchored grep
    for `^\\s*version\\s*:` cannot tell them apart; the node tree can."""
    text = MINIMAL_VALID.replace("  name: my-project", "  name: my-project\n  version: whatever")
    report = check(text)
    # governance.version is still the valid quoted semver; the stray project.version
    # is unknown-key drift, warned, not an error.
    assert report.valid
    assert fields_of(report.warnings) == ["project.version"]


# ---------------------------------------------------------------------------
# The demonstration required by the Acceptance Criteria: shown, not asserted.
# ---------------------------------------------------------------------------


REAL_SHAPE_INVALID = """\
project:
  name: social-stories-creator
  created_at: 2026-07-21T23:23:04Z

governance:
  source: https://github.com/panchew/ai-project-system
  version: v7.0.0
  submodule_path: governance/
"""


def test_validator_fails_on_a_genuinely_invalid_config(tmp_path):
    """This fixture reproduces the shape of a config that really exists on the machine
    (`social-stories-creator`, measured 2026-08-11): missing `governance.ref` and
    `project.description`, with an unquoted v-prefixed `governance.version`.

    It is a fixture, not a copy of the live file — the live file is NOT modified by
    this Epic, and a test that read it would make the suite depend on the host."""
    path = tmp_path / ".ai-project.yml"
    path.write_text(REAL_SHAPE_INVALID, encoding="utf-8")
    report = validator.validate_file(path)

    assert not report.valid
    assert sorted(set(rules_of(report.errors))) == [3, 5]
    assert "governance.ref" in fields_of(report.errors)
    assert "project.description" in fields_of(report.errors)
    # And the two schema-drift keys are surfaced as warnings, not swept up as errors.
    assert fields_of(report.warnings) == ["governance.submodule_path", "project.created_at"]


def test_presence_alone_understates_invalidity(tmp_path):
    """Planning measured required-field *presence* only and found 5 violations across
    4 configs. Enforcing the format constraints too (rules 4, 5, 7) found 8 violations
    across the same 4 configs — no new project became invalid, but the existing ones
    were more invalid than presence-only measurement could show."""
    path = tmp_path / ".ai-project.yml"
    path.write_text(REAL_SHAPE_INVALID, encoding="utf-8")
    report = validator.validate_file(path)
    presence_only = [f for f in report.errors if f.rule == 3]
    assert len(presence_only) == 2
    assert len(report.errors) == 4  # presence (2) + rule 5 twice (unquoted, and non-semver)


# ---------------------------------------------------------------------------
# CLI surface — the JSON output is the authority, the exit code a convenience (G2).
# ---------------------------------------------------------------------------


def test_cli_json_output_is_the_authority(tmp_path, capsys):
    (tmp_path / ".ai-project.yml").write_text(REAL_SHAPE_INVALID, encoding="utf-8")
    code = validator.main(["--json", str(tmp_path / ".ai-project.yml")])
    payload = json.loads(capsys.readouterr().out)

    assert code == 1
    assert payload["spec_version"] == validator.SPEC_VERSION
    report = payload["reports"][0]
    assert report["valid"] is False
    assert report["error_count"] == 4
    assert report["warning_count"] == 2
    # Every finding carries its severity and its rule, so a consumer never has to
    # infer the warning/error split from a count or a exit status.
    assert {f["severity"] for f in report["findings"]} == {"error", "warning"}
    # Rules the implementation does not check are declared, not silently omitted.
    assert set(payload["rules_not_checked"]) == {"9", "13", "14", "18", "24"}


def test_cli_exit_zero_when_only_warnings(tmp_path, capsys):
    (tmp_path / ".ai-project.yml").write_text(MINIMAL_VALID + "\ncfo_review_gate: enabled\n", encoding="utf-8")
    code = validator.main([str(tmp_path / ".ai-project.yml")])
    out = capsys.readouterr().out
    assert code == 0
    assert "VALID" in out
    assert "warning" in out


def test_cli_directory_argument_finds_the_config(tmp_path, capsys):
    (tmp_path / ".ai-project.yml").write_text(MINIMAL_VALID, encoding="utf-8")
    code = validator.main([str(tmp_path)])
    capsys.readouterr()
    assert code == 0


def test_cli_fleet_mode_reports_unenrolled_directories_as_skipped(tmp_path, capsys):
    (tmp_path / "enrolled").mkdir()
    (tmp_path / "enrolled" / ".ai-project.yml").write_text(MINIMAL_VALID, encoding="utf-8")
    (tmp_path / "unenrolled").mkdir()

    code = validator.main(["--json", "--fleet", str(tmp_path)])
    payload = json.loads(capsys.readouterr().out)

    assert code == 0
    assert len(payload["reports"]) == 1
    assert any("unenrolled" in s for s in payload["skipped"])


def test_cli_returns_2_when_nothing_was_validated(tmp_path, capsys):
    code = validator.main([str(tmp_path / "nope")])
    capsys.readouterr()
    assert code == 2
