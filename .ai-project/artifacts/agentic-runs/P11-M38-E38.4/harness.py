"""E38.4's measurement instrument.

One job: invoke a command as a subprocess and report what came back, without
losing the exit code on the way.

This exists because of a recorded measurement error (B3.1 field evidence, final
note): a wrapper invoked ``main()`` in-process and discarded its return value,
where ``local_agent_runner/cli.py:229`` uses ``sys.exit(main())``. The false
reading was one step from being filed as "both engines share the false-zero
bug" -- the exact opposite of the truth, in this Epic's own subject matter.

So this module reads ``CompletedProcess.returncode`` and nothing else. It draws
no conclusion about whether a run "succeeded": that is M39's, and building it
here would be the Hard Constraint's drift.

Verified by ``m2_verify.py`` against a case whose exit code is known non-zero
BEFORE any exit code it reports is treated as evidence (M2).
"""

from __future__ import annotations

import json
import subprocess
import time
from typing import Dict, List, Optional


def invoke(
    argv: List[str],
    *,
    cwd: Optional[str] = None,
    env: Optional[Dict[str, str]] = None,
    timeout_s: Optional[float] = None,
    stdin_text: Optional[str] = None,
) -> Dict[str, object]:
    """Run ``argv`` and return what came back. No interpretation.

    ``exit_code`` is ``CompletedProcess.returncode`` verbatim. ``timed_out``
    is reported separately rather than folded into the exit code, because
    collapsing them would destroy the distinction this Epic is assessing.
    """
    started = time.monotonic()
    timed_out = False
    try:
        proc = subprocess.run(
            argv,
            cwd=cwd,
            env=env,
            input=stdin_text,
            capture_output=True,
            text=True,
            timeout=timeout_s,
        )
        exit_code = proc.returncode
        stdout, stderr = proc.stdout, proc.stderr
    except subprocess.TimeoutExpired as exc:
        timed_out = True
        exit_code = None
        stdout = exc.stdout or ""
        stderr = exc.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode("utf-8", "replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode("utf-8", "replace")
    duration_ms = int((time.monotonic() - started) * 1000)

    return {
        "command": argv,
        "exit_code": exit_code,
        "timed_out": timed_out,
        "stdout": stdout,
        "stderr": stderr,
        "duration_ms": duration_ms,
    }


def record(path: str, payload: object) -> None:
    """Write a measurement to disk verbatim, so the raw form outlives the prose."""
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")
