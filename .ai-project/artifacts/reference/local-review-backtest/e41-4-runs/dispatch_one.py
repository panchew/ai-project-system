#!/usr/bin/env python3
"""Dispatch a single run by opaque ID using runner.py's exact capture logic."""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from runner import RUNS, RAW, BLIND, BACKTEST, extract_prompt, run_opencode, render_blinded
from transport import credential_visibility


def dispatch(runid: str) -> str:
    run = next(r for r in RUNS if r["runid"] == runid)
    rec_path = RAW / f"{run['runid']}__*.json"
    if list(RAW.glob(rec_path.name)):
        return f"skip {runid} (already captured)"
    packet = BACKTEST / "packets" / run["packet"]
    prompt = extract_prompt(str(packet))
    result = run_opencode(run["model"], prompt)
    record = {
        "runid": run["runid"],
        "opaque": True,
        "model_string": run["model"],
        "packet": run["packet"],
        "attempt": run["attempt"],
        "audit_header_transmitted": False,
        "no_tuning_applied": True,
        "sampling": "vendor defaults, seed not fixed",
        "credential_visibility": credential_visibility(),
        "run": result,
    }
    ts = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    (RAW / f"{run['runid']}__{ts}.json").write_text(json.dumps(record, indent=2))
    bp = BLIND / f"{run['runid']}__{run['packet'].replace('packet-', '').replace('.md', '')}.md"
    bp.write_text(render_blinded(run, result))
    return (f"{runid} {run['model']} {run['packet']} a{run['attempt']} "
            f"finish={result['finish_reason']} exit={result['exit']} chars={len(result['response'])}")


if __name__ == "__main__":
    runid = sys.argv[1]
    print(dispatch(runid))
