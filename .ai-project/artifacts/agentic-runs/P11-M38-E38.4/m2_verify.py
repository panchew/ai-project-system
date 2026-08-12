"""M2 -- verify E38.4's harness against a known-nonzero case, before trusting it.

BINDING (Epic spec §M2): before any exit code this Epic reports is treated as
evidence, run the harness against a case whose exit code is known non-zero and
show it reports non-zero.

Four cases, and the fourth is the point:

  A  known-nonzero  -- runner CLI, malformed invocation -> EXIT_CONFIG_ERROR = 3
  B  known-zero     -- /bin/true -> 0   (an instrument that always cried "3"
                       would pass case A and be useless)
  C  known-nonzero  -- /bin/false -> 1  (independent of the subject under test)
  D  FALSIFICATION  -- reproduce the recorded defect in-process: call main()
                       and discard its return value. The truth is 3. A wrapper
                       that drops the return reports 0.

Case D is the one that makes A meaningful. Without it, "the harness reported 3"
is only a claim that the harness works; with it, the exact mistake that nearly
inverted this Epic's conclusion is shown to be caught rather than merely
avoided. It is run here against the same binary, in the same session, so the
two readings differ only in how the value was collected.

No GPU, no model, no network. `local-agent-runner` is NOT modified: case D
imports its `main` and calls it, which is what the original faulty wrapper did.
"""

from __future__ import annotations

import io
import os
import sys
from contextlib import redirect_stderr, redirect_stdout

from harness import invoke, record

RUNNER_DIR = "/home/panchew/soft-dev/local-agent-runner"
HERE = os.path.dirname(os.path.abspath(__file__))

# A deliberately malformed invocation: --tools names a file that does not
# exist, so the CLI fails in _load_permissions before the loop starts and
# before anything touches Ollama. cli.py:37 -> EXIT_CONFIG_ERROR = 3.
MALFORMED = [
    sys.executable,
    "-m",
    "local_agent_runner.cli",
    "--task-text",
    "this invocation is deliberately malformed and must never reach the loop",
    "--tools",
    "/nonexistent/definitely-not-a-tools-file.json",
]


def main() -> int:
    results = {}
    failures = []

    # --- Case A: known-nonzero, the subject under test -------------------
    a = invoke(MALFORMED, cwd=RUNNER_DIR)
    results["A_known_nonzero_runner_config_error"] = a
    if a["exit_code"] != 3:
        failures.append(f"A: expected exit 3, harness reported {a['exit_code']}")

    # --- Case B: known-zero ----------------------------------------------
    b = invoke(["/bin/true"])
    results["B_known_zero"] = b
    if b["exit_code"] != 0:
        failures.append(f"B: expected exit 0, harness reported {b['exit_code']}")

    # --- Case C: known-nonzero, independent of the subject ---------------
    c = invoke(["/bin/false"])
    results["C_known_nonzero_independent"] = c
    if c["exit_code"] != 1:
        failures.append(f"C: expected exit 1, harness reported {c['exit_code']}")

    # --- Case D: falsification -- reproduce the recorded defect ----------
    # The faulty wrapper called main() and threw the return value away.
    sys.path.insert(0, RUNNER_DIR)
    from local_agent_runner.cli import main as runner_main  # noqa: E402

    argv = MALFORMED[3:]  # drop python -m module
    buf_out, buf_err = io.StringIO(), io.StringIO()
    with redirect_stdout(buf_out), redirect_stderr(buf_err):
        true_return = runner_main(argv)

    def faulty_wrapper() -> int:
        """What the recorded error did: invoke main(), discard the return."""
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            runner_main(argv)  # return value discarded -- the defect
        return 0  # the process would exit 0 having fallen off the end

    faulty_reading = faulty_wrapper()

    results["D_falsification_discarded_return"] = {
        "true_return_of_main": true_return,
        "faulty_wrapper_reading": faulty_reading,
        "harness_reading_case_A": a["exit_code"],
        "runner_stderr": buf_err.getvalue().strip(),
        "defect_reproduced": faulty_reading == 0 and true_return != 0,
        "harness_agrees_with_truth": a["exit_code"] == true_return,
    }
    d = results["D_falsification_discarded_return"]
    if not d["defect_reproduced"]:
        failures.append("D: failed to reproduce the discarded-return defect")
    if not d["harness_agrees_with_truth"]:
        failures.append("D: harness disagrees with main()'s true return")

    record(os.path.join(HERE, "m2-verification.json"), results)

    print("M2 harness verification")
    print("=" * 60)
    print(f"A  runner, malformed invocation  -> exit {a['exit_code']}  (known-nonzero: 3)")
    print(f"   stderr: {a['stderr'].strip()}")
    print(f"B  /bin/true                     -> exit {b['exit_code']}  (known-zero: 0)")
    print(f"C  /bin/false                    -> exit {c['exit_code']}  (known-nonzero: 1)")
    print("D  falsification -- the recorded defect, reproduced:")
    print(f"   main()'s true return            = {d['true_return_of_main']}")
    print(f"   wrapper discarding the return   = {d['faulty_wrapper_reading']}   <-- the false zero")
    print(f"   THIS harness (subprocess)       = {d['harness_reading_case_A']}   <-- agrees with truth")
    print("=" * 60)
    if failures:
        for line in failures:
            print("FAIL: " + line)
        return 1
    print("VERIFIED: the harness reports non-zero for known-nonzero cases,")
    print("          zero for known-zero, and does not lose the value the")
    print("          recorded defect lost. Exit codes it reports may now be")
    print("          treated as evidence.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
