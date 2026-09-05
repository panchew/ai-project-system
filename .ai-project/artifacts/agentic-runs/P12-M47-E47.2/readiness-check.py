#!/usr/bin/env python3
"""E47.2 readiness check — run against the live selected project (G2 re-measurement).

Mechanism (delegated design decision, E47.2 spec): parse the selected project's
.ai-project.yml, confirm a `models:` block exists, and resolve the epic lanes
(epic_dev / epic_qa) against the proof's route as established by E47.1.

The proof's route (E47.1): remote agentic dispatch through Drivr's OpenCode
adapter on a `remote:`-resolvable engine. Local inference is PARKED (SN-43) —
a `local:`-prefixed lane is not a dispatchable engine for the remote route.

This is a check that RUNS and RECORDS a verdict, never an exit-status assert.
Exit status is recorded for convenience; the verdict is the record.
"""

import json
import sys
from pathlib import Path


def parse_models(yml_path: Path) -> dict:
    raw = yml_path.read_text()
    models = {}
    in_models = False
    for line in raw.splitlines():
        stripped = line.strip()
        if not in_models:
            if stripped == "models:":
                in_models = True
            continue
        if stripped and not line.startswith(" ") and not line.startswith("\t"):
            break
        if not stripped or stripped.startswith("#"):
            continue
        if ":" in stripped:
            key, _, value = stripped.partition(":")
            models[key.strip()] = value.strip()
    return models


def classify_lane(value: str) -> str:
    if not value:
        return "MISSING"
    if value.startswith("local:"):
        return "PARKED_LOCAL"
    if value.startswith("remote:"):
        return "REMOTE_DISPATCHABLE"
    if "/" in value:
        return "BARE_RESOLVABLE"
    return "UNKNOWN"


def main() -> int:
    project_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    yml_path = project_root / ".ai-project.yml"
    result = {
        "check": "E47.2 readiness check",
        "mechanism": "parse .ai-project.yml models block; classify epic lanes against the E47.1 remote-dispatch route (SN-43: local inference PARKED)",
        "project": str(project_root),
        "yml_path": str(yml_path),
        "yml_exists": yml_path.exists(),
        "models_block_present": False,
        "epic_lanes": {},
        "verdict": None,
        "exit_status": 0,
    }
    if not result["yml_exists"]:
        result["verdict"] = "FAIL — no .ai-project.yml"
        result["exit_status"] = 2
        print(json.dumps(result, indent=2))
        return result["exit_status"]

    models = parse_models(yml_path)
    result["models_block_present"] = bool(models)
    if not models:
        result["verdict"] = "FAIL — no models block"
        result["exit_status"] = 2
        print(json.dumps(result, indent=2))
        return result["exit_status"]

    for lane in ("epic_dev", "epic_qa"):
        value = models.get(lane)
        result["epic_lanes"][lane] = {
            "value": value,
            "classification": classify_lane(value) if value else "MISSING",
        }

    classifications = {
        lane: v["classification"] for lane, v in result["epic_lanes"].items()
    }
    if not classifications:
        result["verdict"] = "FAIL — no epic lanes present"
        result["exit_status"] = 2
    elif any(c in ("PARKED_LOCAL", "MISSING", "UNKNOWN") for c in classifications.values()):
        parked = [l for l, c in classifications.items() if c == "PARKED_LOCAL"]
        result["verdict"] = (
            f"FAIL — epic lanes not dispatchable for the remote route "
            f"(parked local: {', '.join(parked)} — SN-43: local inference PARKED)"
        )
        result["exit_status"] = 1
    else:
        result["verdict"] = "PASS — epic lanes resolve to a remote-dispatchable engine for the proof's route"
        result["exit_status"] = 0

    print(json.dumps(result, indent=2))
    return result["exit_status"]


if __name__ == "__main__":
    sys.exit(main())