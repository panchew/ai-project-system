"""The blessing check for E43.4 (P12-M43) — the system's **first fail-closed default**
must not ship as a key nothing validates (finding W1 of the M43 milestone spec).

The switch `rework_exhaustion_flip` follows the `cfo_review_gate` pattern (on by
default, opt-out via `disabled`). W1's defect is that the precedent itself was an
**unblessed** key: `bin/ai-project-validate` warned on `cfo_review_gate` as a
schema-drift unknown key. Copying the pattern verbatim would ship the flip as a second
unvalidated key. E43.4 blesses both — a §3 schema entry and a §4 rule (27 and 28) in
`governance/ai-project-yml-spec.md` — and this file is the check that the blessing
holds.

What it asserts, and how the guard is falsified:

1. `rework_exhaustion_flip` is a **recognised** top-level key (present in the
   validator's `KNOWN_TOP_LEVEL`), so a valid value reports **no warning** for it.
2. A config carrying `rework_exhaustion_flip: enabled` — the on-by-default state — is
   clean for that key.
3. The repository's **own committed config** reports no warning for the key.
4. **Falsification:** with the key dropped from `KNOWN_TOP_LEVEL` (the unblessed state —
   exactly what the validator warned on before this epic), the warning returns. The
   guard is proved by showing it fires when the blessing is removed, not asserted.
5. The `cfo_review_gate` precedent is blessed in the same change (the E43.4 decision),
   so a valid `cfo_review_gate` value no longer warns either — and an **invalid** value
   for either key is an **error** (rules 27/28), not a warning.

Every case is a fixture under this repository — nothing reads `~/soft-dev`; the fleet
run is evidence recorded in the Delivery Notice, not a test dependency.
"""

import importlib.util
import sys
from importlib.machinery import SourceFileLoader
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
VALIDATOR_PATH = REPO_ROOT / "bin" / "ai-project-validate"


def _load_validator():
    loader = SourceFileLoader("ai_project_validate", str(VALIDATOR_PATH))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
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

KEY = "rework_exhaustion_flip"
PRECEDENT = "cfo_review_gate"


def check(text, path=".ai-project.yml"):
    return validator.validate_text(text, path)


def fields_of(findings):
    return sorted(f.field for f in findings)


# ---------------------------------------------------------------------------
# 1–3. The blessing holds: the key is recognised, clean, and the repo's own
#      config proves it.
# ---------------------------------------------------------------------------


def test_the_flip_key_is_a_recognised_top_level_key():
    """The blessing's first half is a schema entry: the validator knows the key."""
    assert KEY in validator.KNOWN_TOP_LEVEL


def test_enabled_flip_produces_no_warning():
    report = check(MINIMAL_VALID + "\nrework_exhaustion_flip: enabled\n")
    assert report.valid
    assert report.findings == []


def test_disabled_flip_produces_no_warning():
    """`disabled` is the explicit opt-out — the key stays blessed either way."""
    report = check(MINIMAL_VALID + "\nrework_exhaustion_flip: disabled\n")
    assert report.valid
    assert report.findings == []


def test_absent_flip_key_is_valid_and_silent():
    """The key is optional: absent means enabled at the default (rule 28)."""
    report = check(MINIMAL_VALID)
    assert report.valid
    assert report.findings == []


def test_repo_own_config_reports_no_warning_for_the_flip_key():
    """This repository's own committed config carries the switch; the validator must
    not warn on it."""
    report = validator.validate_file(REPO_ROOT / ".ai-project.yml")
    assert report.valid, [f.as_dict() for f in report.errors]
    assert KEY not in fields_of(report.warnings)


# ---------------------------------------------------------------------------
# 4. Falsification — the guard fires when the blessing is removed.
# ---------------------------------------------------------------------------


def test_falsification_unblessed_key_warns_again(monkeypatch):
    """Remove the §4 blessing (here: the validator's recognition of the key — the
    mechanism that makes the warning return) and the schema-drift warning returns.

    This is the exact state before E43.4: an unblessed top-level key reported with
    `rule: None` under the schema-drift class."""
    original = validator.KNOWN_TOP_LEVEL
    known = {k for k in original if k != KEY}
    monkeypatch.setattr(validator, "KNOWN_TOP_LEVEL", known)
    report = check(MINIMAL_VALID + "\nrework_exhaustion_flip: enabled\n")
    assert report.valid  # a warning, not an error
    assert KEY in fields_of(report.warnings)
    assert all(f.rule is None for f in report.warnings)
    # And with the blessing restored, it is clean again — the guard is demonstrated
    # to be the blessing, not something else about the config.
    monkeypatch.setattr(validator, "KNOWN_TOP_LEVEL", original)
    report = check(MINIMAL_VALID + "\nrework_exhaustion_flip: enabled\n")
    assert report.findings == []


# ---------------------------------------------------------------------------
# 5. The precedent is blessed in the same change; invalid values are errors.
# ---------------------------------------------------------------------------


def test_cfo_review_gate_precedent_is_blessed_too():
    """E43.4's stated decision: blessing the flip's successor while leaving its
    precedent warned would leave a standing validator warning on this repo's own
    config, so `cfo_review_gate` is blessed in the same change."""
    assert PRECEDENT in validator.KNOWN_TOP_LEVEL
    report = check(MINIMAL_VALID + "\ncfo_review_gate: enabled\n")
    assert report.valid
    assert report.findings == []


def test_invalid_flip_value_is_an_error():
    """Rules 27/28 constrain the value when present: a non-`enabled`/`disabled` value
    is an error, not a warning — the key is blessed, and blessed keys are validated."""
    report = check(MINIMAL_VALID + "\nrework_exhaustion_flip: true\n")
    assert not report.valid
    assert 28 in {f.rule for f in report.errors}
    assert KEY in fields_of(report.errors)


def test_invalid_gate_value_is_an_error():
    report = check(MINIMAL_VALID + "\ncfo_review_gate: maybe\n")
    assert not report.valid
    assert 27 in {f.rule for f in report.errors}
    assert PRECEDENT in fields_of(report.errors)