#!/usr/bin/env python3
"""E41.4 run orchestration (D2) — dispatch all 30 runs and render BLINDED records.

Workflow (U1 blind discipline):
  * Each run gets an opaque ID (R01..R30) and a held-out mapping entry.
  * The raw transport JSON (with model identity) is written to raw/ — GIT-IGNORED,
    never scored from, and never committed until the mapping is published.
  * A BLINDED markdown record (opaque ID + packet + verbatim response + stop reason,
    NO model identity) is written to blinded/ — this is the scoring material.
  * mapping.tsv (git-ignored) holds ID <-> (model, packet, attempt). It is committed
    ONLY AFTER the scores are committed (U1).
  * Ordering decision (delegated): claude-opus-5 baseline first, then gpt-5.6-sol,
    then deepseek-v4-pro.
  * Every run is reported; a mechanical failure (nonzero exit, refusal) is committed
    with its reason and excluded from scoring.

Usage: python3 runner.py            # run all configured runs (skip ones already captured)
"""
from __future__ import annotations

import csv
import json
import re
import sys
import time
from pathlib import Path

from transport import extract_prompt, run_opencode, credential_visibility

HERE = Path(__file__).resolve().parent
BACKTEST = HERE.parent
PACKETS = BACKTEST / "packets"
RAW = HERE / "raw"
BLIND = HERE / "blinded"
RAW.mkdir(exist_ok=True)
BLIND.mkdir(exist_ok=True)

# Model order: baseline first, then candidates (delegated decision 3).
RUNS = []
_runid = 1
for model in ["anthropic/claude-opus-5", "openai/gpt-5.6-sol", "opencode/deepseek-v4-pro"]:
    for pkt in sorted(PACKETS.glob("packet-*.md")):
        for attempt in (1, 2):
            RUNS.append(
                {
                    "runid": f"R{_runid:02d}",
                    "model": model,
                    "packet": pkt.name,
                    "attempt": attempt,
                }
            )
            _runid += 1

assert len(RUNS) == 30, f"expected 30 runs, got {len(RUNS)}"


def already_done(run: dict) -> bool:
    rec = RAW / f"{run['runid']}__*.json"
    return bool(list(RAW.glob(rec.name)))


def render_blinded(run: dict, result: dict) -> str:
    """Blinded markdown record — NO model identity, only opaque ID + packet + response."""
    # record packet 3 clearly; the response is the verbatim model text.
    return f"""# Blinded run record — {run['runid']}

**Packet:** `{run['packet']}` | **Attempt:** {run['attempt']} | **Opaque run ID:** `{run['runid']}`

**Stop/finish reason:** `{result.get('finish_reason') or 'UNKNOWN'}` | **exit:** {result['exit']}
**Elapsed (s):** {result['elapsed_s']} | **No tuning applied:** true | **Sampling:** vendor defaults

**Model response (verbatim, unedited):**

````text
{result['response']}
````
"""


def write_mapping():
    with open(HERE / "mapping.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["runid", "model", "packet", "attempt", "finish_reason", "status"])
        for run in RUNS:
            rec = list(RAW.glob(f"{run['runid']}__*.json"))
            status = "captured" if rec else "not-run"
            finish = ""
            if rec:
                r = json.loads(rec[0].read_text())
                finish = (r.get("run", {}).get("finish_reason") or "UNKNOWN")
            w.writerow([run["runid"], run["model"], run["packet"], run["attempt"], finish, status])


def main():
    done = 0
    for run in RUNS:
        rec_path = RAW / f"{run['runid']}__*.json"
        if list(RAW.glob(rec_path.name)):
            done += 1
            print(f"skip {run['runid']} (already captured)")
            continue
        print(f"\n=== {run['runid']} {run['model']} {run['packet']} attempt {run['attempt']} ===")
        prompt = extract_prompt(str(PACKETS / run["packet"]))
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
        # blinded scoring material
        blind_path = BLIND / f"{run['runid']}__{run['packet'].replace('packet-','').replace('.md','')}.md"
        blind_path.write_text(render_blinded(run, result))
        # mechanical failure: still committed (blinded) + excluded from scoring
        if result["exit"] != 0:
            print(f"  MECHANICAL FAILURE exit={result['exit']}: {result['stderr'][:200]}")
        else:
            print(f"  finish={result['finish_reason']} resp_chars={len(result['response'])}")
        done += 1

    write_mapping()
    print(f"\nTotal captured: {done}/30")
    print(f"Raw (held out): {RAW}")
    print(f"Blinded records: {BLIND}")
    print("Mapping written to mapping.tsv (git-ignored until scores commit).")


if __name__ == "__main__":
    main()
