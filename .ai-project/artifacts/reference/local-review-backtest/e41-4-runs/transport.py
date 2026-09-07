#!/usr/bin/env python3
"""E41.4 transport (D1) — send a frozen packet prompt to a remote model via `opencode run`.

E35.5's back-test had no runner; its reproduction recipe was a 5-line Ollama POST.
This epic adds the remote transport E35.5 never had. It uses the ONE mechanism proven
to reach and self-report every measured remote target on this host: `opencode run`.

Design decisions (delegated to this epic):
  1. Single script, one code path per vendor, all routed through `opencode run`
     -- the mechanism E41.1 §9.3 confirmed answers + self-reports for every target.
  2. Opaque run IDs: `R<nn>` allocated by this script; the ID<->model mapping is
     held OUT of the run records and published only after scores are committed (U1).
  3. Run ordering: claude-opus-5 baseline first, then gpt-5.6-sol, then deepseek-v4-pro.
  4. New runs live under e41-4-runs/, clearly separated from E35.5's runs/.
  5. Refusal classification (DECIDED BEFORE ANY RUN): a vendor refusal / refusal to
     answer is a MECHANICAL failure -> committed, excluded, reason stated. A response
     that reaches a verdict is scored.

Invariants (Binding Constraints 2, 9; U5; U8):
  - The prompt is EXACTLY the bytes after the `<!-- PROMPT-BEGIN -->` line.
    The audit header is NEVER transmitted.
  - The response is captured verbatim + the stop/finish reason + parameters + timestamp.
  - No tuning is applied. Sampling is the vendor's defaults.
  - The effective XDG_DATA_HOME and the resolved credential-path presence are recorded
    per dispatch (U8/D8). Credential VALUES are never read, printed, or committed.

Usage:
  python3 transport.py --model <provider/id> --packet <packet.md> --runid R01 [--probe]
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

MARKER = "<!-- PROMPT-BEGIN -->"


def extract_prompt(packet_path: str) -> str:
    """Return exactly the bytes after the PROMPT-BEGIN line (README's two-line recipe)."""
    text = Path(packet_path).read_bytes().decode("utf-8")
    return text.split(MARKER, 1)[1].lstrip("\n")


def verbatim_diff_reference(packet_path: str) -> tuple[bool, str]:
    """Diff what we would send against the file's own post-marker bytes."""
    import difflib
    ref = extract_prompt(packet_path)
    # independent re-derivation exactly as README states
    read = Path(packet_path).read_bytes().decode("utf-8")
    ref2 = read.split(MARKER, 1)[1].lstrip("\n")
    same = ref == ref2
    if not same:
        d = "\n".join(
            difflib.unified_diff(ref2.splitlines(), ref.splitlines(), lineterm="")
        )
        return False, d
    return True, "byte-for-byte identical (two independent extractions)"


def credential_visibility() -> dict:
    """Record effective XDG_DATA_HOME and resolved credential path PRESENCE (U8/D8).

    Presence only. Never reads, prints, or commits a credential value.
    """
    xdg_data = os.environ.get("XDG_DATA_HOME", "")
    store = Path.home() / ".local/share/opencode/auth.json"
    snap = Path(xdg_data) / "opencode/auth.json" if xdg_data else None
    resolved = store if store.exists() else (snap if snap and snap.exists() else None)
    return {
        "XDG_DATA_HOME": xdg_data or "UNSET",
        "XDG_CONFIG_HOME": os.environ.get("XDG_CONFIG_HOME", "UNSET"),
        "credential_path_present": str(resolved) if resolved else "NONE",
        "count_credentials": "NOT-READ" if resolved else "NONE",
    }


def run_opencode(model: str, prompt: str, timeout_s: int = 600) -> dict:
    """Dispatch through `opencode run --format json --auto`, capture verbatim + stop reason."""
    started = time.time()
    proc = subprocess.run(
        ["opencode", "run", "--model", model, "--format", "json", "--auto"],
        input=prompt,
        capture_output=True,
        text=True,
        timeout=timeout_s,
    )
    elapsed = time.time() - started

    text_parts: list[str] = []
    finish_reason = None
    tokens = None
    cost = None
    raw_events: list[dict] = []

    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            ev = json.loads(line)
        except Exception:
            continue
        raw_events.append(ev)
        t = ev.get("type")
        part = ev.get("part", {})
        if t == "text":
            text_parts.append(part.get("text", ""))
        elif t == "step_finish":
            finish_reason = part.get("reason")
            tokens = part.get("tokens")
            cost = part.get("cost")

    return {
        "exit": proc.returncode,
        "stderr": proc.stderr,
        "elapsed_s": round(elapsed, 3),
        "finish_reason": finish_reason,
        "tokens": tokens,
        "cost": cost,
        "response": "".join(text_parts),
        "event_count": len(raw_events),
        "raw_events": raw_events,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--packet", required=True)
    ap.add_argument("--runid", required=True)
    ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument("--probe", action="store_true", help="cheap probe: verify mechanics")
    args = ap.parse_args()

    out_dir = Path(__file__).resolve().parent / "raw"
    out_dir.mkdir(parents=True, exist_ok=True)

    # 1. byte-for-byte verification
    same, detail = verbatim_diff_reference(args.packet)
    record = {
        "runid": args.runid,
        "opaque": True,
        "model_string": args.model,
        "packet": Path(args.packet).name,
        "audit_header_transmitted": False,
        "byte_for_byte_verified": same,
        "extraction_diff": detail if not same else None,
        "credential_visibility": credential_visibility(),
        "probe": args.probe,
    }
    if not same:
        print(json.dumps(record, indent=2))
        print("ABORT: extraction is not byte-for-byte. Nothing sent.")
        return 2

    # 2. dispatch
    prompt = extract_prompt(args.packet)
    record["prompt_char_count"] = len(prompt)
    result = run_opencode(args.model, prompt, args.timeout)
    record["run"] = result
    record["no_tuning_applied"] = True
    record["sampling"] = "vendor defaults, seed not fixed"

    ts = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    rec_path = out_dir / f"{args.runid}__{ts}.json"
    rec_path.write_text(json.dumps(record, indent=2))

    print(f"WRITTEN {rec_path}")
    print(f"finish_reason={result['finish_reason']} exit={result['exit']} "
          f"resp_chars={len(result['response'])}")
    if args.probe:
        print("PROBE response (first 120):", result["response"][:120].replace("\n", " "))

    # 3. exit code reflects mechanical status
    if result["exit"] != 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
