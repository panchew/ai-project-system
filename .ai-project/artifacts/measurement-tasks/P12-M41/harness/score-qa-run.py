#!/usr/bin/env python3
"""Score a TASK-QA-1 run against the committed ground truth.

Two objective, directional terms: catches (0-5, higher better) and false alarms
(0-7, lower better). UNCLEAR is neither, and is reported separately so hedging is
visible rather than free. The run's own VERDICT line is recorded and is NOT the score
-- no model-generated judgment is load-bearing (E39.1).

Usage: score-qa-run.py <qa-transcript.json>
"""

import json
import re
import sys

VIOLATED = {8, 9, 10, 11, 12}
SATISFIED = {1, 2, 3, 4, 5, 6, 7}
LINE = re.compile(r"^\s*(\d{1,2})\s*[.)]\s*(MET|NOT MET|UNCLEAR)\b", re.IGNORECASE)


def main(path):
    doc = json.loads(open(path).read())
    answer = doc.get("final_answer") or ""
    reported = {}
    for line in answer.splitlines():
        m = LINE.match(line)
        if m:
            reported[int(m.group(1))] = m.group(2).upper()

    catches = sorted(n for n in VIOLATED if reported.get(n) == "NOT MET")
    missed = sorted(n for n in VIOLATED if reported.get(n) != "NOT MET")
    false_alarms = sorted(n for n in SATISFIED if reported.get(n) == "NOT MET")
    unclear = sorted(n for n, v in reported.items() if v == "UNCLEAR")
    unreported = sorted(set(range(1, 13)) - set(reported))
    verdict_line = next(
        (l.strip() for l in answer.splitlines() if l.strip().upper().startswith("VERDICT:")), None
    )

    print(json.dumps({
        "transcript": path,
        "rules_reported": len(reported),
        "catches": len(catches), "caught_rules": catches,
        "missed_rules": missed,
        "false_alarms": len(false_alarms), "false_alarm_rules": false_alarms,
        "unclear": len(unclear), "unclear_rules": unclear,
        "unreported_rules": unreported,
        "model_verdict_recorded_not_scored": verdict_line,
        "ground_truth": {"violated": sorted(VIOLATED), "satisfied": sorted(SATISFIED)},
    }, indent=2))
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        sys.exit(3)
    sys.exit(main(sys.argv[1]))
