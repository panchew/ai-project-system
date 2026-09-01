# E41.4 — D7: interactive-surface fidelity measurement for `phase` and `milestone`

**Status:** measured 2026-09-01, on `epic/P12-M41-E41.4`. **Layer/time/scope
(`P11-GH-2`):** `opencode run` (the dispatch surface E41.1 proved for every target),
2026-09-01, this host. Recorded **separately from the back-test scores** (U7c / D7).

## What was measured

U7c: does the session **receive** the injected block (unguessable-substring probe) and
does it report it **faithfully** (both control arms)? U7b: run the identical probe from
a **WELL-FORMED but unguessable** path — `/tmp/<uuid>/plainname`, no leading dash, no
mangled encoding.

- Round-trips exactly → the earlier normalization was triggered by malformed-looking
  input → **consistent with model-side normalization**, and the raw value reached the
  session.
- Also transforms → **injector-side**, and the finding is materially larger.

## The probe

- **Unguessable path:** `/tmp/e414fid-de553728-6037-4cf0-bc62-ec262994fcb4/plainname`
  (a random UUID; not in any model's weights; well-formed, no mangling).
- **Prompt:** "Report your working directory exactly as it appears in your environment,
  verbatim, with no alteration, no reconstruction, and no comment. Output only the
  path."
- **Mechanism:** `opencode run --model <row-model> --dir <unguessable-path>` — the
  injected `<env>` block carries the working directory (the same mechanism U7 measured).
- Raw captures: `fid-phase_gpt-5.6-sol.jsonl`, `fid-milestone_deepseek-v4-pro.jsonl`.

## Results

| Row | Route (ruled) | Probe prompt sent byte-for-byte? | Response (verbatim) | Exact round-trip? | Finish |
|-----|---------------|----------------------------------|---------------------|-------------------|--------|
| `phase` | `openai/gpt-5.6-sol` | yes (verbatim file) | `/tmp/e414fid-de553728-6037-4cf0-bc62-ec262994fcb4/plainname` | **YES — exact** | stop |
| `milestone` | `opencode/deepseek-v4-pro` | yes (verbatim file) | `/tmp/e414fid-de553728-6037-4cf0-bc62-ec262994fcb4/plainname` | **YES — exact** | stop |

## Layer implication (U7b, both arms)

Both control arms (the two target rows) **round-trip the well-formed unguessable path
exactly.** Per U7b's decision rule, this is the outcome consistent with the earlier
normalization being **triggered by malformed-looking input — i.e. model-side
normalization — while the raw value did reach the session.** The injector-side reading
is **not implicated** by either arm: no mangling was observed on a well-formed input
on either row.

**Receive: CONFIRMED** for both rows (the unguessable path returned verbatim proves the
injected block reached the session context).

**Faithful report: CONFIRMED** for both rows (exact, unaltered, no repair).

## Per-row record (separate from back-test scores)

| Row | Receive | Faithful report | Layer implicated |
|-----|---------|-----------------|------------------|
| `phase` | YES | YES (exact) | consistent with model-side normalization on malformed input |
| `milestone` | YES | YES (exact) | consistent with model-side normalization on malformed input |

## Scope, stated narrowly

Verified for **`opencode run`** (the dispatch surface — the same surface the E31.3
check reads). The interactive TUI was **not** separately probed, matching E41.1 §2.3.2's
boundary. These fidelity results concern the **surface's** delivery of the injected
identity block — **not** the back-test scores, which are unaffected by and independent
of this measurement.

## Escalation

**None required for D7.** Both rows receive and report faithfully; no normalization
defect was observed on a well-formed input, and no row's measurement is affected.