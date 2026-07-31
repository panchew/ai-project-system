---
project: ai-project-system
phase: P10
milestone: M35
epic: E35.5
type: reference
status: in-execution
last_updated: 2026-07-30
---

# Milestone × local-inference back-test — evidence directory

Evidence for Epic **P10-M35-E35.5**. `model-routing-policy.md` row **P4** routes the Milestone level
to paid frontier because Milestone holds Stage-2 accept authority and its errors propagate into
merges. E35.4 recorded that cell as *"Remote — local under evaluation."* **This directory is that
evaluation.**

Location follows the `.ai-project/artifacts/reference/token-measurement/` convention (Epic spec,
Deliverables → Suggested home). **This is not a tool.** There is no harness, framework or CLI here —
one-off packets, a frozen rubric, and captured outputs, committed as evidence (Epic spec, Hard
Constraint → "Nothing built").

## Contents

| Path | What it is |
|---|---|
| `rubric.md` | The **pre-registered** scoring rubric. Committed with the packets, before any run. |
| `packets/` | Five blinded review packets, one per defect. |
| `runs/` | Raw model outputs, verbatim and unedited — every run made. |
| `scores.md` | Catch / miss / false-alarm per defect, with the quoted model text that earned each. |
| `judgment.md` | The recorded pass/fail judgment and its reasons. |

## The method

The five defects are ones this phase already adjudicated, so ground truth is known independently of
the model. Every one of them is documented **in this repository**, usually with the finding and its
fix stated plainly — so a local model pointed at the repo would read the answer rather than derive it,
and the result would look like a pass while measuring nothing.

Hence:

1. **Each packet is built from the material as it stood at the moment of the decision** — what a
   Stage-2 reviewer actually had in hand — reconstructed with `git show <pre-fix-commit>:<path>` where
   the material has since been corrected.
2. **Every document that states the finding is excised.** Each packet's audit header names exactly
   what was excluded and why.
3. **The rubric was committed before any run**, in the same commit as the packets.
4. **Every run is reported.** Two runs per packet, both scored. No best-of-N.

## Packet file format — and how to reproduce a run

Each packet file has two parts separated by a single marker line:

```
<!-- ===== audit header: provenance + blinding record ===== -->
   ... read by humans; NEVER sent to the model ...
<!-- PROMPT-BEGIN -->
   ... the prompt, verbatim, byte for byte ...
```

The prompt is **exactly** the bytes after the `<!-- PROMPT-BEGIN -->` line. The audit header is held
out because it names what was excised, which would itself leak the answer.

To reproduce a run:

```bash
PKT=packets/packet-2-completion-signal-false-positive.md
python3 - "$PKT" <<'PY' > /tmp/prompt.txt
import sys; print(open(sys.argv[1]).read().split('<!-- PROMPT-BEGIN -->',1)[1].lstrip('\n'), end='')
PY
python3 - <<'PY'
import json, urllib.request
body = {"model": "qwen3.6:27b", "prompt": open('/tmp/prompt.txt').read(),
        "stream": False, "options": {"num_ctx": 16384}}
req = urllib.request.Request("http://localhost:11434/api/generate",
        data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
print(json.load(urllib.request.urlopen(req))["response"])
PY
```

`num_ctx` per packet is recorded with each run in `runs/`. It is set to comfortably exceed that
packet's prompt; it is not a tuning knob and was never varied to change an answer.

## How to verify the blinding yourself

Do not take this Epic's word for it. Two independent checks:

**1. Read the prompts.** Everything the model saw is in the packet files, after the marker. If a
finding is stated there, the blinding failed.

**2. Run the mechanical check.** Each packet's audit header names the documents excised; this asserts
their tell-tale strings are absent from the prompt:

```bash
cd .ai-project/artifacts/reference/local-review-backtest/packets
python3 - <<'PY'
FORBIDDEN = {
 'packet-1-decomposition-gap.md': ['E33.4', 'amendment A1'],
 'packet-2-completion-signal-false-positive.md':
     ['Run B', 'run-record', 'runtime-decision', 'false-positive', 'false positive',
      'zero real work', 'qwen3-coder', 'SN-3'],
 'packet-3-completion-signal-false-negative.md':
     ['false-negative', 'false negative', 'run-record', 'P10-GH', 'E34.3',
      'Closure Declaration', 'exit-code untrust'],
 'packet-4-factual-accuracy-miscount.md':
     ['c64ebe7', '20 entries', '18 untracked', 'actual is 20', 'miscount'],
 'packet-5-test-correctness.md':
     ['P10-GH-6', 'carry-forward', 'the guard is wrong'],
}
ok = True
for f, words in FORBIDDEN.items():
    prompt = open(f).read().split('<!-- PROMPT-BEGIN -->', 1)[1]
    hits = [w for w in words if w.lower() in prompt.lower()]
    print(('LEAK  ' if hits else 'CLEAN ') + f, hits or '')
    ok &= not hits
print('\nALL CLEAN' if ok else '\nLEAKS PRESENT')
PY
```

**Two strings are deliberately not in that list, and the reason matters:**

- `"Closure Declaration"` occurs in **packet 1's prompt** — but only inside the M33 milestone spec's
  own text ("Milestone Closure Declaration produced (`is_final: false`…)" and the §5C phase-closure
  sentence). That is original source material a planning reviewer had; the *M33 Closure Declaration
  document*, which narrates the gap, is excised.
- `"not a typo"` occurs in **packet 5's prompt** — inside the docstring of
  `tests/test_starter_lint.py` itself, which is the material under review. Removing it would mean
  showing the model a doctored version of the very file it is being asked to judge.

Both are checked by reading, above. Neither states any finding.

## Deliberate design points, so they are not mistaken for sloppiness

- **The candidate model's name is retained in packets 2 and 3.** `qwen2.5-coder:14b` and
  `qwen3-coder:30b` appear in the raw run metadata a Stage-2 reviewer had. Neither name states the
  finding, and stripping them would have meant editing evidence.
- **Packet 3 is the inverse control.** Its correct answer is ACCEPT. A model that rejects everything
  passes packets 1, 2, 4 and 5 and fails this one — which is why it is in the set.
- **The `home_finance` commit message is stripped from packet 3's diff.** It was written after the
  review and asserts the outcome ("Suite: 275 examples, 0 failures").
- **Packet 1 is reconstructed from pre-amendment commits.** The milestone spec is shown at `1c50040`,
  not at `5d820dc` which adds the fourth epic to the decomposition.
