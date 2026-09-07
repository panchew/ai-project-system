"""Durable guards for the mechanical-tier defects the external assessment observed
(Epic P12-M44-E44.6, SN-30 Rec 1).

Background
----------
Issue #192 (external assessment, 2026-08-10) Finding 2 observed four defects, all in
the mechanically-checkable tier — rules that existed, were correct, and were violated
anyway, with no detector to notice:

  1. The AOG carried two ``§13``s / two ``§14``s and out-of-order sections — headed by
     a uniqueness + monotonicity check. **Owned by E44.4's D5** (``tests/
     test_aog_section_numbering.py``); E44.6 records the finding and cites that check,
     and builds nothing here — one detector, one check, one falsification.
  2. ``.ai-project.yml`` missing ``framework_version``; ``bin/ai-project-init`` wrote
     neither ``framework_version`` nor ``models:`` — checkable by schema validation.
  3. E36.1 claimed **4** bare ``SN-23`` references; the actual count was **17** —
     checkable by occurrence count.
  4. The count-error tally collided at "nine": E38.3 and E38.5 each incremented from a
     stale base of eight — checkable by identifier uniqueness.

Each guard below is built to **fail when its defect is reintroduced** and to pass on
the current corpus. The falsification is demonstrated by mutating the real artifact
into the defect's shape and observing the guard go red, then restoring it (green).

Two scope notes, so the guards are not over-claimed:

* Defect #2's ``bin/ai-project-init`` side is OUT of scope here (the epic's guards are
  checks, not a fix of the producer; the schema-validation mechanism already exists
  from P10-GH-5 / E38.3). The guard enforces the *schema contract* — the invariant
  that a ``.ai-project.yml`` this repository ships is schema-conformant and carries the
  fields the defect named, so a regression back to an incomplete config fails the
  suite.
* Defects #3 and #4 are historic one-off errors corrected in their own records. The
  guards therefore target the *class* — an un-dated ``SN-23`` citation in the two
  normative documents that get cited by number, and an instance-identifier set that
  uses a shared ordinal (or a duplicate identifier) — not a frozen count.
"""

import re
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
YML_PATH = REPO_ROOT / ".ai-project.yml"
AOG_PATH = REPO_ROOT / "governance" / "AI-OPERATING-GUIDELINES.md"
CHAT_HIERARCHY_PATH = REPO_ROOT / "governance" / "systems" / "chat-hierarchy.md"

# ---------------------------------------------------------------------------
# Defect #2 — .ai-project.yml schema contract
# ---------------------------------------------------------------------------

# The five REQUIRED fields, §4 rule 3 (ai-project-yml-spec.md v2.9.0). Mirrors the
# validator's own list so a contract guard that drifts from the validator is caught
# by the real-corpus test (the guard asserts these plus the validator's pass).
REQUIRED_FIELDS = (
    "governance.source",
    "governance.version",
    "governance.ref",
    "project.name",
    "project.description",
)

# The seven `models:` keys the schema recognizes (§3.4). Defect #2 named a config
# that was missing/partial in exactly this surface, so a present-but-incomplete
# `models:` block is the shape to guard. KNOWN_MODELS in bin/ai-project-validate.
MODEL_KEYS = {
    "hq",
    "phase",
    "milestone",
    "epic_dev",
    "epic_qa",
    "creation",
    "epic_manual",
}

# Rule 26 — framework_version, when present, is a non-empty string matching
# `^v?\d+\.\d+\.\d+$`. Absent is valid (the field is optional by P10-GH-1).
FRAMEWORK_VERSION_RE = re.compile(r"^v?\d+\.\d+\.\d+$")

MODEL_ROUTE_RE = re.compile(r"^(remote|local):[a-zA-Z0-9.:_-]+$")


def yml_contract_errors(text):
    """Itemized contract defects in ``text`` (``.ai-project.yml``), or ``[]``.

    Reports the §4-required-field presence, the ``models:`` block's completeness and
    well-formedness (present-with-required-keys), and ``framework_version`` per rule
    26 (absent allowed; present must be a pinned semver). Each defect is a line,
    never a count.
    """
    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        return [f"unparseable YAML: {exc}"]

    if not isinstance(data, dict):
        return ["top level is not a mapping"]

    errors = []
    for field in REQUIRED_FIELDS:
        block, key = field.split(".")
        value = data.get(block, {}).get(key) if isinstance(data.get(block), dict) else None
        if value in (None, ""):
            errors.append(f"required field '{field}' absent or empty")

    models = data.get("models")
    if models is not None:
        if not isinstance(models, dict):
            errors.append("'models:' block is not a mapping")
        else:
            missing = sorted(MODEL_KEYS - set(models.keys()))
            if missing:
                errors.append(
                    "'models:' block incomplete — missing keys: " + ", ".join(missing)
                )
            for key in sorted(set(models.keys()) & MODEL_KEYS):
                route = models[key]
                if not isinstance(route, str) or not MODEL_ROUTE_RE.match(route):
                    errors.append(
                        f"models.{key} is not a well-formed route: {route!r}"
                    )

    if "framework_version" in data:
        fv = data["framework_version"]
        if not isinstance(fv, str) or not FRAMEWORK_VERSION_RE.match(fv):
            errors.append(f"framework_version is not a pinned semver: {fv!r}")
    # Absent framework_version is valid (§3.6, rule 26) — deliberately not an error.

    return errors


def test_repo_project_yml_satisfies_the_schema_contract():
    """The repository's own ``.ai-project.yml`` is schema-conformant: the five
    required fields present, the ``models:`` block complete and well-formed, and
    ``framework_version`` (absent or well-formed) per rule 26."""
    errors = yml_contract_errors(YML_PATH.read_text(encoding="utf-8"))
    assert not errors, "\n".join(f"  - {e}" for e in errors)


def test_project_yml_is_accepted_by_the_schema_validator():
    """The contract guard agrees with the real validator: a passing contract must
    also be accepted by ``bin/ai-project-validate`` (its own independent §4 pass)."""
    import importlib.util
    import sys
    from importlib.machinery import SourceFileLoader

    loader = SourceFileLoader(
        "ai_project_validate_e446", str(REPO_ROOT / "bin" / "ai-project-validate")
    )
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
    # Registered before exec_module (as in test_ai_project_validate): the validator
    # uses `from __future__ import annotations` with @dataclass, and resolving those
    # deferred annotations looks the module up in sys.modules.
    sys.modules[loader.name] = module
    loader.exec_module(module)
    report = module.validate_file(YML_PATH)
    assert report.valid, [f.as_dict() for f in report.errors]


def _mutation_of_yml(transform):
    text = YML_PATH.read_text(encoding="utf-8")
    out = transform(text)
    assert out != text, "mutation made no change — falsification would be vacuous"
    return out


def test_falsified_missing_models_key_fails():
    """Reintroduce defect #2's shape — a ``models:`` block missing a key — and the
    contract guard fails, naming the missing key."""
    mut = _mutation_of_yml(lambda t: t.replace(
        "  epic_qa: remote:deepseek-v4-flash\n",
        "",
        1,
    ))
    errors = yml_contract_errors(mut)
    assert any("epic_qa" in e and "incomplete" in e for e in errors)


def test_falsified_malformed_framework_version_fails():
    """Reintroduce a non-pinned ``framework_version`` (the v-prefix/semver contract of
    rule 26) and the guard fails."""
    mut = _mutation_of_yml(lambda t: t + "framework_version: latest\n")
    errors = yml_contract_errors(mut)
    assert any("framework_version" in e and "latest" in e for e in errors)


def test_falsified_missing_required_field_fails():
    """Reintroduce a missing REQUIRED field and the guard fails, naming the field."""
    mut = _mutation_of_yml(lambda t: t.replace("  ref: master\n", "", 1))
    errors = yml_contract_errors(mut)
    assert any("governance.ref" in e for e in errors)


# ---------------------------------------------------------------------------
# Defect #3 — occurrence count: no un-dated SN-23 citation in the citation-bearing
# normative documents (AOG + chat-hierarchy.md)
# ---------------------------------------------------------------------------

# The two Steering Notes that both hold `id: SN-23` (the ratified B3.1 collision),
# cited by the E36.1 date-qualification. A bare (un-dated) `SN-23` citation — the
# "SN-23 Decision N" form a reader follows — in these two documents is the exact
# ambiguity defect E36.1 closed. Prose/changelog mentions of the *identifier* (e.g.
# "id: SN-23", "the surviving SN-23 collision") are NOT citations and are exempt
# per E36.1's recorded three-class distinction (sweep-evidence §4).
SN23_DATED = r"SN-23 \(2026-07-(?:18|20)\)"
# An un-dated SN-23 that forms a citable "SN-23 Decision N"/"SN-23 … Decision #N"
# reference (the reader-follows-by-number form). Dated forms and bare-identifier
# prose mentions are excluded.
UNDATED_SN23_CITATION_RE = re.compile(
    r"SN-23(?!\s*\(2026-07-(?:18|20)\))(?=[^\n]*\bDecision\b)"
)


def normative_body(text):
    """The documented body, before ``## Changelog`` — a changelog row is history, not
    a citation-bearing normative statement (E36.1's exempt class: it names the change
    class or quotes the historical defective text, so a date there is a category
    error). Mirrors test_model_config.py's exclusion of the yml-spec Changelog."""
    return text.split("## Changelog", 1)[0]


def undated_sn23_citation_lines(text):
    """Line numbers of un-dated ``SN-23`` CITATIONS (a ``SN-23 … Decision`` form) in
    the document body (before ``## Changelog``).

    Occurrence-oriented, not line-oriented: each line holding a bare citation is
    reported once, so the E36.1 undercount (line-oriented counting dropping a line
    that also held a dated form) cannot recur silently. A line whose only ``SN-23``
    are date-qualified, or that merely names the identifier, is not a citation line.
    """
    # Strip the dated forms first, so a line holding both a dated and a bare form
    # cannot have its bare form hidden.
    lines = []
    for lineno, line in enumerate(normative_body(text).splitlines(), 1):
        remainder = re.sub(SN23_DATED, "", line)
        if UNDATED_SN23_CITATION_RE.search(remainder):
            lines.append(lineno)
    return lines


def test_no_undated_sn23_citation_in_the_aog():
    """Defect #3's class: the AOG's normative body (before ``## Changelog``) carries no
    un-dated ``SN-23`` CITATION — every citable ``SN-23 … Decision`` reference is
    date-qualified (2026-07-18). Changelog rows (history) are exempt."""
    bare = undated_sn23_citation_lines(AOG_PATH.read_text(encoding="utf-8"))
    assert not bare, (
        "AI-OPERATING-GUIDELINES.md carries un-dated SN-23 citation(s) at line(s): "
        + ", ".join(str(n) for n in bare)
    )


def test_no_undated_sn23_citation_in_chat_hierarchy():
    """chat-hierarchy.md's normative body (date-qualified to SN-23 (2026-07-20))
    carries no un-dated ``SN-23`` citation."""
    bare = undated_sn23_citation_lines(CHAT_HIERARCHY_PATH.read_text(encoding="utf-8"))
    assert not bare, (
        "chat-hierarchy.md carries un-dated SN-23 citation(s) at line(s): "
        + ", ".join(str(n) for n in bare)
    )


def test_occurrence_oriented_detection_handles_both_forms_on_one_line():
    """The E36.1 lesson, pinned: a line holding both a dated and a bare form must not
    lose the bare form. Line-oriented counting dropped all thirteen such occurrences
    (E36.1 v1.0)."""
    text = "SN-23 (2026-07-18) Decision 2 and SN-23 Decision 2\n"
    assert undated_sn23_citation_lines(text) == [1]


def test_falsified_undated_sn23_citation_fails():
    """Reintroduce a bare ``SN-23 … Decision`` citation into a copy of the AOG and the
    guard fails, naming the line."""
    text = AOG_PATH.read_text(encoding="utf-8")
    mutated = text.replace("SN-23 (2026-07-18) Decision 2, ratified", "SN-23 Decision 2, ratified", 1)
    assert mutated != text, "mutation made no change — falsification would be vacuous"
    bare = undated_sn23_citation_lines(mutated)
    assert bare, "bare SN-23 citation reintroduced into the AOG was not detected"


def test_dated_sn23_citations_and_identifier_mentions_are_not_flagged():
    """A date-qualified SN-23 citation is not a violation, and neither is a bare
    mention of the identifier (E36.1's exempt classes). This is what makes the two
    real-corpus tests green and the falsification above red."""
    dated = "SN-23 (2026-07-18) Decision 2, ratified; SN-23 (2026-07-20) superseded.\n"
    assert undated_sn23_citation_lines(dated) == []
    mention = "Both notes hold id: SN-23 — the surviving SN-23 collision.\n"
    assert undated_sn23_citation_lines(mention) == [], (
        "a bare identifier mention is not a citation and must not be flagged"
    )


# ---------------------------------------------------------------------------
# Defect #4 — identifier uniqueness: the count-error tally ordinal collision
# ---------------------------------------------------------------------------

# The remedy M38 recorded (v1.1.4): _cite instances by artifact + defect, never by
# ordinal_. The guard below enforces identifier uniqueness over a set of instance
# records — the shape the defect's own mechanism (a shared number incremented from a
# stale base) would violate. It is deliberately general (like B3.1's steering-note
# uniqueness guard): it does not know what the instances are, only that two distinct
# records must not share an ordinal identifier.
def instance_identifier_issues(records):
    """Itemized problems with ``records`` (each an (id, ordinal) pair; ordinal may be
    None for an artifact+defect identifier), or ``[]``.

    Reports duplicates — two records sharing a non-None ordinal, and two records
    sharing the same id — never a bare count. ``ordinal`` is the shared counter value
    the defect's mechanism used (e.g. both E38.3 and E38.5 recorded ordinal ``9``).
    """
    issues = []
    seen_ordinals = {}
    seen_ids = {}
    for rec_id, ordinal in records:
        if ordinal is not None:
            if ordinal in seen_ordinals:
                issues.append(
                    f"duplicate ordinal {ordinal!r}: {seen_ordinals[ordinal]!r} and {rec_id!r}"
                )
            else:
                seen_ordinals[ordinal] = rec_id
        if rec_id in seen_ids:
            issues.append(f"duplicate instance id {rec_id!r}")
        else:
            seen_ids[rec_id] = ordinal
    return issues


def test_distinct_ordinals_do_not_collide():
    records = [("E38.3", 8), ("E38.5", 9)]
    assert instance_identifier_issues(records) == []


def test_falsified_stale_base_collision_detected():
    """Reintroduce defect #4's exact shape: two distinct instances each recorded as
    ordinal ``9`` (each correctly added one to the same base of eight, neither aware
    of the other). The guard flags the collision."""
    records = [("E38.3 (ai-project-yml-spec.md rule 3)", 9), ("E38.5 (ceiling row)", 9)]
    issues = instance_identifier_issues(records)
    assert any("duplicate ordinal" in issue for issue in issues)
    assert "9" in issues[0]


def test_artifact_defect_identifiers_are_unique():
    """The recorded remedy (cite by artifact+defect, never by ordinal) yields a unique
    set — no ordinal, so no collision and no ordinal to count."""
    records = [
        ("E38.3: ai-project-yml-spec.md §4 rule 3", None),
        ("E38.5: Finding 1 ceiling row", None),
        ("E36.1: bare SN-23 count", None),
    ]
    assert instance_identifier_issues(records) == []


def test_duplicate_artifact_defect_id_detected():
    """Two records identifying the same artifact+defect id is a collision even with
    no ordinal."""
    records = [("E38.3: §4 rule 3", None), ("E38.3: §4 rule 3", None)]
    assert any("duplicate instance id" in i for i in instance_identifier_issues(records))


def test_guard_reads_the_carry_forward_note_without_ordinals():
    """Defect #4's class, applied where E44.6 records it: the P11-GH-1 carry-forward
    note's instance list must not cite an instance by ordinal (it is ruled unusable),
    and must not duplicate an instance id. Guards the note D3 edits, so a future
    editor writing 'the Nth instance' (which reproduces the filed defect) fails the
    suite."""
    note = (
        REPO_ROOT
        / "docs"
        / "phases"
        / "P11__Drivr_Coordination_Over_Rented_Execution"
        / "P11__carry-forward-note__P11-GH-1-mid-flight-amendments-do-not-reach-working-branches.md"
    )
    text = note.read_text(encoding="utf-8")
    # The note must not cite any P11-GH-1 instance by a bare ordinal ("the Nth
    # instance", "instance five", …). The defect's own remedy forbids it.
    ordinal = re.compile(r"\bthe\s+(?:ninth|tenth|eleventh|twelfth|fifth|sixth|seventh|eighth)"
                         r"(?:\s+(?:instance|instance's|one|error|count-error))\b", re.IGNORECASE)
    hits = [ln for ln, line in enumerate(text.splitlines(), 1) if ordinal.search(line)]
    assert not hits, (
        "P11-GH-1 carry-forward note cites an instance by ordinal at line(s): "
        + ", ".join(str(n) for n in hits)
    )
