#!/usr/bin/env python3
"""Score a TASK-DEV-1 run: how many of the 20 pre-written test cases pass.

Mechanical, not a quality judgment. Also records whether `tests/` was modified -- the
DoD forbids it, and a run that edits the test to make it pass would otherwise be
rewarded for defeating the check.

Usage: score-dev-run.py <instantiated-workspace-dir>
"""

import json
import re
import subprocess
import sys
from pathlib import Path

TOTAL = 20


def main(workspace):
    ws = Path(workspace)
    if not ws.is_dir():
        print(f"workspace not found: {workspace}", file=sys.stderr)
        return 3

    # git status BEFORE pytest: the tree is measured as the run left it, never as the
    # scorer left it. The workspace also carries a .gitignore for __pycache__ -- without
    # it, running the tests alone reports three changed paths for a workspace where
    # nothing was done, and a successful-nothing run would clear `files changed > 0`.
    status = subprocess.run(
        ["git", "status", "--porcelain"], cwd=str(ws), capture_output=True, text=True, check=False
    )
    all_changed = [l[3:].strip() for l in status.stdout.splitlines() if l.strip()]
    # The dev adapter writes the run's own transcript/context/metadata into
    # .ai-project/artifacts/ INSIDE the workspace, so git reports it as changed even for
    # a run that produced nothing. The harness's exhaust is not the model's output.
    excluded = [p for p in all_changed if p.startswith(".ai-project/artifacts")]
    changed = [p for p in all_changed if p not in excluded]
    tests_touched = [p for p in changed if p.startswith("tests/")]

    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/test_parse_duration.py", "-q", "--no-header",
         "-p", "no:cacheprovider"],
        cwd=str(ws), capture_output=True, text=True, check=False,
    )
    tail = proc.stdout.strip().splitlines()[-1] if proc.stdout.strip() else ""
    m = re.search(r"(\d+) passed", proc.stdout)
    passed = int(m.group(1)) if m else 0
    m = re.search(r"(\d+) failed", proc.stdout)
    failed = int(m.group(1)) if m else 0
    m = re.search(r"(\d+) error", proc.stdout)
    errors = int(m.group(1)) if m else 0

    print(json.dumps({
        "workspace": str(ws),
        "directional_check": {"tests_passed": passed, "tests_total": TOTAL},
        "tests_failed": failed,
        "collection_errors": errors,
        "pytest_summary": tail,
        "pytest_exit_code_recorded_not_scored": proc.returncode,
        "files_changed_worktree": changed,
        "files_changed_count": len(changed),
        "files_changed_excluded_run_exhaust": excluded,
        "tests_modified": tests_touched,
        "disqualified_for_editing_tests": bool(tests_touched),
    }, indent=2))
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        sys.exit(3)
    sys.exit(main(sys.argv[1]))
