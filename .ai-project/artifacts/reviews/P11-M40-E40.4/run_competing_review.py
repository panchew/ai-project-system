#!/usr/bin/env python3
"""Competing-model PR reviewer — P11-M40-E40.4.

Drives a LOCAL model (Ollama) over the shipped executable code added by a PR and
captures its findings verbatim.

AUTHORITY CEILING (Epic spec P11-M40-E40.4 §The Authority Ceiling). This script:

  * reads the repository and writes ONE findings file. It modifies no reviewed file.
  * never calls the GitHub API. It cannot post, approve, request changes, resolve a
    conversation, apply a suggestion, or set a status check.
  * emits no pass/fail, score, vote, or verdict, and exits 0 whenever the model
    answered at all. Its exit status is therefore NOT usable as a gate — there is
    nothing for a required check to key on.
  * is INVOKED, never triggered. Nothing in this repository runs it automatically.

Findings are inputs to the CFO's PSG §11.6.1 diff review. They feed it. They do not
substitute for it.

Verification note (P11-GH-2 — state the layer): Ollama's runtime context window
defaults to 4096 tokens regardless of what the model advertises, so an oversized
prompt is truncated SILENTLY. This script sets num_ctx explicitly and records
`prompt_eval_count` per call so truncation is visible in the record rather than
inferred from a plausible-looking answer.
"""

import json
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone

ENDPOINT = "http://localhost:11434/api/chat"
MODEL = "qwen3-coder:30b"
NUM_CTX = 32768

TARGETS = [
    "bin/ai-project-validate",
    "bin/run-qa-agent",
    "bin/local-agent-runner-shim",
]

PROMPT = """You are reviewing code newly added by a pull request. Review it for exactly \
three concerns, in this order of attention:

1. PERFORMANCE
2. SECURITY
3. SCALABILITY

The file is `{path}`, added by the PR under review.

Report only concrete, specific findings you can point at a line or construct for. For \
each finding give: the concern (performance/security/scalability), the location, what \
is wrong, and why it matters. If you find nothing real in a category, say so plainly \
rather than inventing something.

You have no authority here. You are not approving or rejecting anything, and nobody is \
obliged to act on what you say. Do not recommend that the PR be blocked or merged.

--- BEGIN {path} ---
{body}
--- END {path} ---
"""


def utcnow():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def file_at(ref, path):
    return subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        capture_output=True, text=True, check=True,
    ).stdout


def review(path, body):
    payload = {
        "model": MODEL,
        "stream": False,
        "options": {"num_ctx": NUM_CTX, "temperature": 0.2},
        "messages": [{"role": "user", "content": PROMPT.format(path=path, body=body)}],
    }
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    started = utcnow()
    with urllib.request.urlopen(req, timeout=1800) as resp:
        data = json.loads(resp.read())
    return {
        "target": path,
        "target_lines": body.count("\n"),
        "started_utc": started,
        "finished_utc": utcnow(),
        "prompt_eval_count": data.get("prompt_eval_count"),
        "eval_count": data.get("eval_count"),
        "num_ctx_requested": NUM_CTX,
        "truncation_suspected": (data.get("prompt_eval_count") or 0) >= NUM_CTX,
        "verbatim_response": data["message"]["content"],
    }


def main():
    ref = sys.argv[1] if len(sys.argv) > 1 else "origin/phase/P11"
    out = sys.argv[2] if len(sys.argv) > 2 else "local-model-findings.json"
    sha = subprocess.run(
        ["git", "rev-parse", ref], capture_output=True, text=True, check=True
    ).stdout.strip()

    record = {
        "epic": "P11-M40-E40.4",
        "reviewer": {"kind": "local", "engine": "ollama", "endpoint": ENDPOINT, "model": MODEL},
        "authority": "none — findings only; feeds PSG 11.6.1, substitutes for nothing",
        "reviewed_ref": ref,
        "reviewed_sha": sha,
        "invocation": "manual — not triggered by any hook, workflow, or scheduler",
        "run_started_utc": utcnow(),
        "reviews": [],
    }

    for path in TARGETS:
        sys.stderr.write(f"[{utcnow()}] reviewing {path} ...\n")
        record["reviews"].append(review(path, file_at(ref, path)))

    record["run_finished_utc"] = utcnow()
    with open(out, "w") as fh:
        json.dump(record, fh, indent=2)
    sys.stderr.write(f"[{utcnow()}] wrote {out}\n")


if __name__ == "__main__":
    main()
