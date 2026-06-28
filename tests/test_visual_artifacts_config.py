"""Tests for the visual_artifacts config layer (Epic P5-M22-E22.1, VA-1).

The validation locus is the existing Python config handler
``bin/ai-project-orchestrator`` (``load_yml_config`` / ``validate_visual_artifacts``),
not a parallel validator. These tests load that extensionless script as a module —
mirroring tests/test_daemon_path_resolution.py — and exercise the §4 rules (18–24)
documented in governance/ai-project-yml-spec.md §3.5.
"""

import importlib.util
from importlib.machinery import SourceFileLoader
from pathlib import Path

import pytest
import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
ORCH_PATH = REPO_ROOT / "bin" / "ai-project-orchestrator"


def _load_orchestrator():
    """Load the extensionless ``bin/ai-project-orchestrator`` script as a module."""
    loader = SourceFileLoader("ai_project_orchestrator_under_test", str(ORCH_PATH))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


orch = _load_orchestrator()


# ---------------------------------------------------------------------------
# validate_visual_artifacts — §4 rules 18–24
# ---------------------------------------------------------------------------

class TestValidateVisualArtifacts:
    def test_absent_block_is_valid(self):
        # Rule 24: an absent block (None) is valid — no error, no warning.
        assert orch.validate_visual_artifacts(None) is None

    def test_valid_block_passes(self):
        orch.validate_visual_artifacts({
            "enabled": True,
            "comfyui_url": "http://localhost:8188",
            "types": ["diagrams", "infographics", "video"],
        })

    def test_enabled_false_passes(self):
        orch.validate_visual_artifacts({"enabled": False})

    @pytest.mark.parametrize("bad", ["yes", "true", 1, 0, None])
    def test_invalid_enabled_raises(self, bad):
        # Rule 19: enabled must be a boolean. (None is a no-op skip, so test only non-None.)
        if bad is None:
            return
        with pytest.raises(ValueError, match="visual_artifacts.enabled"):
            orch.validate_visual_artifacts({"enabled": bad})

    def test_invalid_types_member_raises(self):
        # Rule 20: each types entry must be one of the allowed set.
        with pytest.raises(ValueError, match="visual_artifacts.types"):
            orch.validate_visual_artifacts({"types": ["diagrams", "bogus"]})

    def test_types_not_a_list_raises(self):
        with pytest.raises(ValueError, match="visual_artifacts.types"):
            orch.validate_visual_artifacts({"types": "diagrams"})

    @pytest.mark.parametrize("bad_url", ["not a url", "ftp://host/x", "localhost:8188", "/just/a/path"])
    def test_malformed_comfyui_url_raises(self, bad_url):
        # Rule 21: comfyui_url must be a well-formed http(s) URL when present.
        with pytest.raises(ValueError, match="visual_artifacts.comfyui_url"):
            orch.validate_visual_artifacts({"comfyui_url": bad_url})

    @pytest.mark.parametrize("good_url", ["http://localhost:8188", "https://comfy.example.com/api"])
    def test_well_formed_url_passes(self, good_url):
        orch.validate_visual_artifacts({"comfyui_url": good_url})

    def test_unknown_key_warns_not_raises(self, capsys):
        # Rule 22: unknown keys produce a warning, not an error.
        orch.validate_visual_artifacts({"enabled": False, "frame_rate": 30})
        captured = capsys.readouterr()
        assert "Unknown key" in captured.err
        assert "frame_rate" in captured.err


# ---------------------------------------------------------------------------
# resolve_visual_artifacts — absent ⇒ disabled, present ⇒ merged
# ---------------------------------------------------------------------------

class TestResolveVisualArtifacts:
    def test_absent_resolves_disabled(self):
        resolved = orch.resolve_visual_artifacts(None)
        assert resolved["enabled"] is False

    def test_present_block_without_enabled_defaults_disabled(self):
        # Opt-in: a block that omits enabled is still disabled.
        resolved = orch.resolve_visual_artifacts({"comfyui_url": "http://localhost:8188"})
        assert resolved["enabled"] is False

    def test_enabled_true_resolves_enabled(self):
        resolved = orch.resolve_visual_artifacts({"enabled": True})
        assert resolved["enabled"] is True


# ---------------------------------------------------------------------------
# load_yml_config — end-to-end through the real loader
# ---------------------------------------------------------------------------

class TestLoadYmlConfig:
    def _write_and_load(self, tmp_path, monkeypatch, data):
        cfg = tmp_path / ".ai-project.yml"
        cfg.write_text(yaml.dump(data), encoding="utf-8")
        monkeypatch.setattr(orch, "YML_CONFIG", cfg)
        return orch.load_yml_config()

    def test_missing_file_disabled(self, tmp_path, monkeypatch):
        monkeypatch.setattr(orch, "YML_CONFIG", tmp_path / "nope.yml")
        config = orch.load_yml_config()
        assert config["visual_artifacts"]["enabled"] is False

    def test_absent_block_disabled(self, tmp_path, monkeypatch):
        config = self._write_and_load(tmp_path, monkeypatch, {"models": {"epic_dev": "x"}})
        assert config["visual_artifacts"]["enabled"] is False
        # models handling is unaffected
        assert config["models"]["epic_dev"] == "x"

    def test_valid_block_loads(self, tmp_path, monkeypatch):
        config = self._write_and_load(tmp_path, monkeypatch, {
            "visual_artifacts": {"enabled": True, "types": ["diagrams"]},
        })
        assert config["visual_artifacts"]["enabled"] is True
        assert config["visual_artifacts"]["types"] == ["diagrams"]

    def test_invalid_block_raises_through_loader(self, tmp_path, monkeypatch):
        with pytest.raises(ValueError):
            self._write_and_load(tmp_path, monkeypatch, {
                "visual_artifacts": {"enabled": "definitely-not-a-bool"},
            })
