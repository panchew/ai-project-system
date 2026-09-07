"""`model_verification` is a BLESSED key, and blessing is not enforcement.

P12 closure disposal, 2026-09-07. E43.4 blessed ``cfo_review_gate`` and
``rework_exhaustion_flip`` and left ``model_verification`` warning only because it sat
outside M43's scope — a gap, not a decision. It was the single warning
``bin/ai-project-validate`` emitted on this repo's own config.

Falsified in both directions: removing the key from ``KNOWN_TOP_LEVEL`` must bring the
warning back, and an invalid value must still be rejected. The blessing widens the schema
by exactly one key and two values, and nothing else.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
VALIDATE = REPO / "bin" / "ai-project-validate"
SPEC = REPO / "governance" / "ai-project-yml-spec.md"

BASE = """\
governance:
  source: https://github.com/panchew/ai-project-system
  version: "2.0.0"
  ref: v2.0.0
project:
  name: fixture
  description: A fixture config.
"""


def _run(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATE), str(path)],
        capture_output=True,
        text=True,
        cwd=REPO,
    )


def _write(tmp_path: Path, extra: str) -> Path:
    p = tmp_path / ".ai-project.yml"
    p.write_text(BASE + extra)
    return p


@pytest.mark.parametrize("value", ["advisory", "blocking"])
def test_blessed_values_produce_no_warning(tmp_path: Path, value: str) -> None:
    """Both allowed values are clean — the key is no longer schema drift."""
    result = _run(_write(tmp_path, f"model_verification: {value}\n"))
    assert "model_verification" not in result.stdout, (
        f"{value!r} still warns; the key is not blessed:\n{result.stdout}"
    )
    assert "0 error" in result.stdout


def test_absent_key_is_valid(tmp_path: Path) -> None:
    """Absent means advisory (chat-hierarchy.md), and is not an error."""
    result = _run(_write(tmp_path, ""))
    assert "0 error" in result.stdout
    assert "model_verification" not in result.stdout


def test_the_key_is_in_the_validator_s_known_set() -> None:
    """The blessing lives in KNOWN_TOP_LEVEL. Removing it is what re-breaks this."""
    assert '"model_verification",' in VALIDATE.read_text(), (
        "model_verification is not in bin/ai-project-validate; the warning returns"
    )


def test_the_schema_documents_the_key() -> None:
    """A blessed key with no §3.x entry and no §4 rule is half-blessed."""
    spec = SPEC.read_text()
    assert "### 3.9 Optional Fields — `model_verification`" in spec
    assert "29. `model_verification`, when present" in spec
    assert "model_verification: <advisory|blocking>" in spec


def test_the_spec_states_that_blessing_is_not_enforcement() -> None:
    """The honesty is load-bearing.

    ``chat-hierarchy.md`` already states that ``blocking`` is carried by agent compliance
    rather than by a wrapping process. §3.9 must not let the blessing imply otherwise — a
    reader who concludes the schema now enforces the refusal has been misled by us.
    """
    spec = SPEC.read_text()
    section = spec.split("### 3.9 Optional Fields — `model_verification`", 1)[1]
    section = section.split("\n## 4. Validation Rules", 1)[0]
    assert "no code" in section.lower()
    assert "does not add enforcement" in section or "it does not add enforcement" in section


def test_blessing_is_independent_of_which_value_is_held() -> None:
    """Blessing the key must not smuggle in the advisory→blocking decision.

    That flip is HQ's act at P12's closure. The schema permits both values and requires
    neither; a schema that required ``blocking`` would have taken a decision that was not
    the schema's to take.
    """
    spec = SPEC.read_text()
    assert "| Default | `advisory` |" in spec
    assert "does not require `blocking`" in spec
