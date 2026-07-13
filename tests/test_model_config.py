"""Consistency guard for the epic_dev model configuration (Epic P7-M26-E26.2).

E26.2's documented decision: the config value (``.ai-project.yml`` ``models.epic_dev``)
and the orchestrator's in-script default (``DEFAULT_MODELS["epic_dev"]``) both move to
``local:qwen2.5-coder:14b`` and must agree, so an absent ``models:`` block can never
silently resurrect a tool-call-incapable model (``llama3:8b`` — local-agent-runner
CONTRACT §1.4). These tests load the extensionless orchestrator script as a module,
mirroring tests/test_visual_artifacts_config.py.
"""

import importlib.util
from importlib.machinery import SourceFileLoader
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
ORCH_PATH = REPO_ROOT / "bin" / "ai-project-orchestrator"
YML_PATH = REPO_ROOT / ".ai-project.yml"
YML_SPEC_PATH = REPO_ROOT / "governance" / "ai-project-yml-spec.md"

EXPECTED_EPIC_DEV = "local:qwen2.5-coder:14b"


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
