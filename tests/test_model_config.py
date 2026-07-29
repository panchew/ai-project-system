"""Consistency guard for the `.ai-project.yml` `models:` block (Epic P7-M26-E26.2,
extended P9-M31-E31.2 to all five keys + a policy<->block divergence check).

E26.2's documented decision: the config value (``.ai-project.yml`` ``models.epic_dev``)
and the orchestrator's in-script default (``DEFAULT_MODELS["epic_dev"]``) both move to
``local:qwen2.5-coder:14b`` and must agree, so an absent ``models:`` block can never
silently resurrect a tool-call-incapable model (``llama3:8b`` — local-agent-runner
CONTRACT §1.4). These tests load the extensionless orchestrator script as a module,
mirroring tests/test_visual_artifacts_config.py.

P9-M31-E31.2 (Hard Constraint 3, "policy consumed, not re-authored"; Deliverable 3)
generalizes this guard to all five ``models:`` keys — a stale ``DEFAULT_MODELS["hq"]``
is a real defect even though no dispatch mechanism reads it yet — and adds a
policy<->block divergence check: the recorded policy
(``.ai-project/artifacts/reference/token-measurement/model-routing-policy.md``)'s own
"Mapping to `.ai-project.yml`" table is parsed with a narrow, documented method (five
known key rows, not a general markdown parser) and compared against both the config
file and the in-script default. A mismatch fails the suite — never a silent divergence.

P9-M31-E31.3 (Deliverable 4) adds two more `models:` keys, ``creation`` and
``epic_manual`` — manual-chat-only verification targets with no agentic dispatch
surface (Creation never dispatches; a manual Epic chat is neither the `epic_dev` nor
`epic_qa` lane). Because neither key has a dispatch role, they deliberately sit outside
`bin/ai-project-orchestrator`'s ``DEFAULT_MODELS`` (out of scope to touch, per this
Epic's Technical Constraints) and outside `model-routing-policy.md`'s "Mapping to
`.ai-project.yml`" table (out of scope to edit). Their recorded source of truth is
instead `governance/systems/chat-hierarchy.md`'s "Manual Chat Model Verification"
section, "The mapping" table — parsed below with the same narrow, documented-row method
as the policy table, and checked against `.ai-project.yml` for divergence.
"""

import importlib.util
import re
from importlib.machinery import SourceFileLoader
from pathlib import Path

import pytest
import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
ORCH_PATH = REPO_ROOT / "bin" / "ai-project-orchestrator"
YML_PATH = REPO_ROOT / ".ai-project.yml"
YML_SPEC_PATH = REPO_ROOT / "governance" / "ai-project-yml-spec.md"
POLICY_PATH = (
    REPO_ROOT
    / ".ai-project"
    / "artifacts"
    / "reference"
    / "token-measurement"
    / "model-routing-policy.md"
)
CHAT_HIERARCHY_PATH = REPO_ROOT / "governance" / "systems" / "chat-hierarchy.md"

EXPECTED_EPIC_DEV = "local:qwen2.5-coder:14b"

# The five `models:` keys, per the policy's "Mapping to .ai-project.yml" table
# (model-routing-policy.md) — the guard target this file enforces.
MODEL_KEYS = ("hq", "phase", "milestone", "epic_dev", "epic_qa")

# The two manual-chat-only keys added P9-M31-E31.3 — no agentic dispatch surface, so
# deliberately outside MODEL_KEYS, DEFAULT_MODELS, and model-routing-policy.md's own
# mapping table (see this file's module docstring).
MANUAL_ONLY_KEYS = ("creation", "epic_manual")
EXPECTED_MANUAL_ONLY_VALUE = "remote:claude-opus-5"

FALSIFIED_NAMES = ("gpt-4o", "claude-3-5-sonnet", "qwen2.5-coder:7b", "llama3:8b")

# Narrow, documented parse of the policy file's own mapping table (P9-M31-E31.2
# Design Decision 3): rows shaped like "| `key` | `value` | P<n> ... |" between the
# "## Mapping to `.ai-project.yml`" heading and the next `##` heading. Deliberately
# not a general markdown-table parser — five known keys, one known section.
_MAPPING_ROW = re.compile(r"^\|\s*`(\w+)`\s*\|\s*`([^`]+)`\s*\|")


def _load_orchestrator():
    """Load the extensionless ``bin/ai-project-orchestrator`` script as a module."""
    loader = SourceFileLoader("ai_project_orchestrator_model_config_test", str(ORCH_PATH))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


orch = _load_orchestrator()


def _config_models():
    with YML_PATH.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)["models"]


def _policy_mapping_table():
    """The policy file's "Mapping to `.ai-project.yml`" table as a ``{key: value}``
    dict — the five rows the M31 guardrail enforces."""
    text = POLICY_PATH.read_text(encoding="utf-8")
    marker = "## Mapping to `.ai-project.yml`"
    start = text.index(marker)
    rest = text[start + len(marker):]
    next_heading = re.search(r"^##\s", rest, re.MULTILINE)
    section = rest[: next_heading.start()] if next_heading else rest
    mapping = {}
    for line in section.splitlines():
        match = _MAPPING_ROW.match(line.strip())
        if match:
            mapping[match.group(1)] = match.group(2)
    return mapping


def _chat_hierarchy_manual_mapping():
    """`chat-hierarchy.md`'s "Manual Chat Model Verification" → "The mapping" table as a
    ``{key: value}`` dict — the recorded source of truth for the two manual-only keys
    (P9-M31-E31.3), parsed with the same narrow, documented method as
    ``_policy_mapping_table`` (five known key rows, not a general markdown parser)."""
    text = CHAT_HIERARCHY_PATH.read_text(encoding="utf-8")
    marker = "#### The mapping"
    start = text.index(marker)
    rest = text[start + len(marker):]
    next_heading = re.search(r"^####\s", rest, re.MULTILINE)
    section = rest[: next_heading.start()] if next_heading else rest
    mapping = {}
    for line in section.splitlines():
        match = _MAPPING_ROW.match(line.strip())
        if match:
            mapping[match.group(1)] = match.group(2)
    return mapping


# --- epic_dev (original E26.2 coverage, preserved verbatim) ----------------------


def test_config_epic_dev_is_qwen_coder_14b():
    assert _config_models()["epic_dev"] == EXPECTED_EPIC_DEV


def test_default_models_epic_dev_agrees_with_config():
    """Documented E26.2 decision: in-script default and config value agree."""
    assert orch.DEFAULT_MODELS["epic_dev"] == _config_models()["epic_dev"]


def test_epic_dev_is_off_llama3_8b_everywhere_defined():
    """Neither definition of epic_dev may drift back to the tool-call-incapable model."""
    assert "llama3:8b" not in _config_models()["epic_dev"]
    assert "llama3:8b" not in orch.DEFAULT_MODELS["epic_dev"]


def test_yml_spec_does_not_document_llama3_8b_as_epic_dev_default():
    """The reference doc's default rows define the default for adopters (E26.2
    acceptance: off llama3:8b everywhere it is defined, including docs). The
    Changelog section is history, not a definition, and is excluded."""
    body = YML_SPEC_PATH.read_text(encoding="utf-8").split("## Changelog")[0]
    for line in body.splitlines():
        if "epic_dev" in line:
            assert "llama3:8b" not in line, f"epic_dev still defined as llama3:8b: {line!r}"


# --- all five keys (P9-M31-E31.2) -------------------------------------------------


@pytest.mark.parametrize("key", MODEL_KEYS)
def test_default_models_agrees_with_config_for_every_key(key):
    """A stale DEFAULT_MODELS entry is a real defect even for keys with no dispatch
    mechanism yet (hq/phase/milestone) — it's the runtime fallback the moment the
    yml is absent or fails to parse (load_yml_config())."""
    assert orch.DEFAULT_MODELS[key] == _config_models()[key], (
        f"DEFAULT_MODELS[{key!r}] ({orch.DEFAULT_MODELS[key]!r}) diverges from "
        f".ai-project.yml's models.{key} ({_config_models()[key]!r})"
    )


@pytest.mark.parametrize("key", MODEL_KEYS)
@pytest.mark.parametrize("falsified", FALSIFIED_NAMES)
def test_no_falsified_name_in_config_or_default_for_any_key(key, falsified):
    assert falsified not in _config_models()[key]
    assert falsified not in orch.DEFAULT_MODELS[key]


def test_default_models_has_exactly_the_five_documented_keys():
    assert set(orch.DEFAULT_MODELS.keys()) == set(MODEL_KEYS)


# --- policy <-> block divergence (Hard Constraint 3 / Deliverable 3) -------------


def test_policy_mapping_table_documents_all_five_keys():
    """Sanity check on the parser itself: if the policy file's table shape drifts
    (heading renamed, rows reformatted), fail loudly here rather than the divergence
    tests below silently passing on an empty mapping."""
    mapping = _policy_mapping_table()
    assert set(mapping.keys()) == set(MODEL_KEYS), (
        f"parsed policy mapping table keys {sorted(mapping.keys())} != "
        f"expected {sorted(MODEL_KEYS)} — model-routing-policy.md's table shape "
        "may have changed; update _MAPPING_ROW/_policy_mapping_table()"
    )


@pytest.mark.parametrize("key", MODEL_KEYS)
def test_policy_mapping_agrees_with_yml_block(key):
    """Hard Constraint 3: 'policy consumed, not re-authored' — guard logic treats
    policy<->block divergence as an error. A genuine policy defect routes through
    the Change Discipline via the Milestone Chat (update both files together);
    this test never edits either file, it only refuses to pass on a silent
    mismatch."""
    policy_value = _policy_mapping_table()[key]
    config_value = _config_models()[key]
    assert policy_value == config_value, (
        f"policy<->block divergence on {key!r}: model-routing-policy.md's mapping "
        f"table says {policy_value!r}, .ai-project.yml's models.{key} says "
        f"{config_value!r}. Per Hard Constraint 3, update both files together via "
        "the Change Discipline — never edit one silently."
    )


@pytest.mark.parametrize("key", MODEL_KEYS)
def test_policy_mapping_agrees_with_default_models(key):
    """Same divergence check against the in-script fallback, so a DEFAULT_MODELS
    edit that drifts from the policy is caught even if `.ai-project.yml` itself
    stays correct."""
    policy_value = _policy_mapping_table()[key]
    default_value = orch.DEFAULT_MODELS[key]
    assert policy_value == default_value, (
        f"policy<->DEFAULT_MODELS divergence on {key!r}: policy says "
        f"{policy_value!r}, DEFAULT_MODELS[{key!r}] says {default_value!r}."
    )


# --- manual-chat-only keys: creation / epic_manual (P9-M31-E31.3) ----------------


def test_config_has_both_manual_only_keys():
    """The two keys this Epic adds must actually exist in `.ai-project.yml` — a
    guardrail whose documented mapping names a key the config never defines would be
    an empty promise."""
    config = _config_models()
    for key in MANUAL_ONLY_KEYS:
        assert key in config, f"models.{key} missing from .ai-project.yml"


@pytest.mark.parametrize("key", MANUAL_ONLY_KEYS)
def test_config_manual_only_key_matches_expected_value(key):
    assert _config_models()[key] == EXPECTED_MANUAL_ONLY_VALUE


@pytest.mark.parametrize("key", MANUAL_ONLY_KEYS)
@pytest.mark.parametrize("falsified", FALSIFIED_NAMES)
def test_no_falsified_name_in_config_for_manual_only_key(key, falsified):
    assert falsified not in _config_models()[key]


def test_chat_hierarchy_manual_mapping_documents_all_five_keys():
    """Sanity check on the parser: if chat-hierarchy.md's table shape drifts, fail
    loudly here rather than the divergence test below silently passing on an empty or
    partial mapping."""
    mapping = _chat_hierarchy_manual_mapping()
    expected_keys = set(MODEL_KEYS[:3]) | set(MANUAL_ONLY_KEYS)  # hq, phase, milestone + 2
    assert expected_keys <= set(mapping.keys()), (
        f"parsed chat-hierarchy.md mapping keys {sorted(mapping.keys())} do not cover "
        f"expected {sorted(expected_keys)} — 'The mapping' table's shape may have "
        "changed; update _MAPPING_ROW/_chat_hierarchy_manual_mapping()"
    )


@pytest.mark.parametrize("key", MANUAL_ONLY_KEYS)
def test_chat_hierarchy_manual_mapping_agrees_with_yml_block(key):
    """Deliverable 4's divergence check for the two manual-only keys: chat-hierarchy.md
    "The mapping" table is these keys' recorded source of truth (they have no
    agentic-dispatch surface, so model-routing-policy.md's own table and
    DEFAULT_MODELS deliberately do not cover them — see module docstring). A mismatch
    here is a real defect; this test never edits either file, it only refuses to pass
    on a silent divergence, consistent with E31.2's enforcement of the same principle
    for the other five keys."""
    documented_value = _chat_hierarchy_manual_mapping()[key]
    config_value = _config_models()[key]
    assert documented_value == config_value, (
        f"chat-hierarchy.md<->.ai-project.yml divergence on {key!r}: 'The mapping' "
        f"table says {documented_value!r}, .ai-project.yml's models.{key} says "
        f"{config_value!r}. Update both together."
    )
