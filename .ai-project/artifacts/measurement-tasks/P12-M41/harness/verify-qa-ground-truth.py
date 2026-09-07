#!/usr/bin/env python3
"""Mechanically verify TASK-QA-1's ground truth against the work file.

The ground truth is a claim about which of the standard's twelve rules the artifact
violates. That claim is checked here rather than asserted, so the scoring baseline is
itself measured. Run from the repository root.
"""

import re
import sys

import yaml

WORK = ".ai-project/artifacts/measurement-tasks/P12-M41/qa-task/work/servicecard.yml"
NAME_RE = re.compile(r"^[a-z][a-z0-9-]*$")
TOP_LEVEL = {"name", "owner", "tier", "replicas", "port", "healthcheck", "dependencies", "region"}


def rules(d):
    hc = d.get("healthcheck") if isinstance(d.get("healthcheck"), dict) else {}
    deps = d.get("dependencies")
    yield 1, isinstance(d, dict), "top level is a mapping"
    yield 2, isinstance(d.get("name"), str) and bool(NAME_RE.match(d.get("name", ""))), "name pattern"
    yield 3, isinstance(d.get("owner"), str) and d.get("owner", "").count("@") == 1, "owner has exactly one @"
    yield 4, d.get("tier") in ("gold", "silver", "bronze"), "tier enum"
    yield 5, isinstance(d.get("replicas"), int) and not isinstance(d.get("replicas"), bool) and d["replicas"] >= 1, "replicas >= 1"
    yield 6, isinstance(d.get("port"), int) and 1024 <= d.get("port", 0) <= 65535, "port range"
    yield 7, isinstance(d.get("healthcheck"), dict) and "path" in hc and "timeout_s" in hc, "healthcheck shape"
    yield 8, isinstance(hc.get("path"), str) and hc.get("path", "").startswith("/"), "healthcheck.path starts with /"
    yield 9, isinstance(hc.get("timeout_s"), int) and 1 <= hc.get("timeout_s", 0) <= 30, "healthcheck.timeout_s range"
    yield 10, deps is None or (isinstance(deps, list) and all(isinstance(x, str) and NAME_RE.match(x) for x in deps)), "dependencies pattern"
    yield 11, d.get("region") in ("us-east", "us-west", "eu-central"), "region enum"
    yield 12, isinstance(d, dict) and not (set(d) - TOP_LEVEL), "no unlisted top-level keys"


def main():
    with open(WORK) as f:
        doc = yaml.safe_load(f)
    violated, met = [], []
    for n, ok, label in rules(doc):
        (met if ok else violated).append((n, label))
    print(f"rules: 12    MET: {len(met)}    VIOLATED: {len(violated)}")
    print("violated:", ", ".join(f"{n} ({l})" for n, l in violated))
    print("met:     ", ", ".join(str(n) for n, _ in met))
    expected = [8, 9, 10, 11, 12]
    actual = [n for n, _ in violated]
    if actual != expected:
        print(f"GROUND TRUTH DISAGREES: expected {expected}, measured {actual}", file=sys.stderr)
        return 1
    print("ground truth CONFIRMED: rules 8, 9, 10, 11, 12 are the five violations")
    return 0


if __name__ == "__main__":
    sys.exit(main())
