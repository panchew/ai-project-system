---
project: ai-project-system
phase: P9
milestone: M30
epic: E30.1
type: reference
status: active
last_updated: 2026-07-17
---

# Token-Burn Measurement Mechanism — E30.1

This directory is the **stable home of the M30 token-burn dataset** (Milestone spec
requirement; E30.2's audit input). It contains:

| file | role |
|---|---|
| `README.md` | this mechanism doc — design decision, attribution rules, blind spots |
| `token-burn-dataset.json` | the dataset, machine-readable (E30.2 cites cells from here) |
| `token-burn-dataset.md` | the same dataset, human-readable, incl. the gap records |
| `audit-report.md` | E30.2's audit — price-weighted findings over the dataset |
| `model-routing-policy.md` | E30.2's derived frontier-vs-local policy (`models:` grounding) |
| `context-scoping.md` | E30.3's per-level context-scoping standard + before/after pack evidence + bounded-scope finding |

The dataset is **generated, not hand-written**: both files are emitted by
[`bin/measure-token-burn`](../../../../bin/measure-token-burn). The committed copies are a
dated snapshot (see `generated_utc` inside); rerunning the script on the CFO's machine
regenerates them from current session data.

---

## Mechanism decision (the Epic's design point)

**Chosen: hybrid A + B + C-lite.** All three candidate directions from the Epic spec are
used, each for the slice it can measure honestly:

- **(A) Harness usage logs — paid spend.** Claude Code persists every session as JSONL
  under `~/.claude/projects/-home-panchew-soft-dev-ai-project-system/` with a
  provider-reported `usage` block per API message (`input_tokens`,
  `cache_creation_input_tokens`, `cache_read_input_tokens`, `output_tokens`). This is
  real billed data covering every governance chat run on this machine since 2026-06-12,
  at zero new spend. The mechanism parses, deduplicates, attributes, and aggregates it.
  *Why:* it is the only source of actual paid counts, and it already exists — the
  CFO-pacing constraint never triggers.
- **(B) Corpus tokenization — governance overhead.** The governance corpus (PSG, AOG,
  yml-spec), the current per-level starters/specs, and directory totals are tokenized
  with a local tokenizer, yielding the corpus-overhead figure separable from task spend.
  *Why:* session usage blocks cannot say which of their input tokens are governance
  corpus; tokenizing the corpus files directly is the honest way to get that split.
- **(C-lite) Local-run extraction — local spend.** The one existing agentic run
  (`.ai-project/artifacts/agentic-runs/P7-M26-E26.3-PROVE/`) already carries ollama
  `eval_count` per turn in `transcript.json`; the mechanism extracts it and
  proxy-tokenizes the run's `context.md`. **`bin/run-dev-agent` was deliberately not
  modified**: forward instrumentation (recording `prompt_eval_count`/`eval_count` into
  `run-metadata.json`) is a real option but touches the runner's behavior contract for
  zero backward gain (only one historical run exists) — noted as future work for the
  E30.3-era, recorded here rather than silently skipped.

## Reproducing a capture

```
python3 -m venv /tmp/tokenv && /tmp/tokenv/bin/pip install tiktoken
/tmp/tokenv/bin/python bin/measure-token-burn          # full capture (A+B+C)
python3 bin/measure-token-burn --no-corpus             # without tiktoken (A+C only)
```

The script is stdlib-only except for optional `tiktoken` (Direction B). It reads the
session directory read-only and writes only the two dataset files in this directory.

## Attribution rules (Direction A)

Sessions are unlabeled; attribution is rule-based and every row in the dataset records
*which rule fired* (`level_rule`, `task_rule`) so E30.2 can weigh confidence.

**Chat level** — first non-sidechain user message (harness wrappers stripped), in order:
`Epic Execution Chat Starter` paste or `Phase Pn Milestone Mn [Epic] En.m` /
`Epic En.m` opener → **epic**; `Milestone Execution Chat Starter` or `Phase Pn
Milestone Mn` → **milestone**; `Phase Execution Chat Starter` or bare `Phase Pn` →
**phase**; an `hq_opener` artifact or `HQ Chat Opener` template → **hq**; a `seed`
artifact → **creation**. Fallback: git branch prefix (`epic/`, `milestone/`, `phase/`),
flagged `branch-fallback` (lower confidence). Otherwise **unattributed**.

**Task type** — role- and signal-based:

1. A `Review …` opener → **review** (the parent chat reviewing a delivery).
2. Epic-level sessions (first-message-attributed only) → **execution** — the Epic
   chat's defined role; includes Delivery Notice authoring (gap G2 covers the bundling).
3. Otherwise, from artifact-write signals (`Write`/`Edit` tool calls to spec/starter,
   review-decision, closure-declaration, delivery-notice paths): only-planning-signals →
   **planning**; several task types in one session → **mixed** (own bucket, split
   gap-recorded, never guessed); no signals → **unattributed**.

**Deduplication (correctness-critical):** Claude Code writes one JSONL line per content
block; every line of a message repeats the same message id and `usage`. Usage is counted
once per unique message id (verified: 43 lines → 17 messages in a sample session, no
id with divergent usage). Tool-use signals are scanned on *every* line. `<synthetic>`
model entries (harness placeholders) are excluded.

## What the measured numbers mean

- **Matrix cells** (dataset §1): whole-session totals summed per level × task type.
  The four usage components are kept separate — E30.2 applies its own price weighting
  (cache reads bill ≈0.1×, cache creation ≈1.25× of base input).
- **First-turn context** (§3): the first API call's `input + cache_creation +
  cache_read` — the real billed cost of booting a chat at that level (system prompt +
  memory + opener) before any work happens.
- **Per-call context** (§3): session context total ÷ API calls — what an average call
  at that level re-reads (dominated by cached context; this is the number the
  premium-quota exhaustion is made of).
- **Corpus packs** (§4): starter + required specs + PSG + AOG per level, proxy-tokenized
  — the governance-corpus share of a level's context load, separable from task spend.
- **Paid vs local**: paid spend lives in §§1–3 (`spend_kind: paid`), local ollama spend
  in §5 (`spend_kind: local`); they are never merged.

## Blind spots (read before citing)

- **Attribution is inferred, not labeled at source.** Rules above are deterministic and
  recorded per row, but a session that opened unconventionally can land in
  `unattributed`/`branch-fallback` buckets (all such rows are visible in dataset §7).
- **No within-session segmentation** — a session is the attribution atom. Mixed
  sessions are a separate bucket (G7); closure inside epic executions is G2.
- **This machine only** — other surfaces/machines and deleted sessions are invisible
  (G8). Notably, any Creation/HQ work done on claude.ai web is not captured.
- **Tokenizer proxy** — Direction B uses tiktoken `o200k_base`, not the Claude
  tokenizer; treat corpus numbers as ±10–15% and use them for proportions (G10).
  Paid-side numbers in §§1–3 are exact provider-billed counts.
- **Local input tokens unmeasured** — the runner transcript records output
  `eval_count` only (G9); local coverage is a single run.
- **Self-measurement** — the capture includes the live E30.1 session itself (session
  `e92a5427`), whose totals are current only up to the moment of capture; harness
  files append while sessions run, so a rerun moves recent rows slightly.
- **Prior estimates are absent by design.** No cell derives from the 24K/157K
  estimates (Hard Constraint). Where measured values happen to land near them, that is
  measurement, not import.

## Contract with E30.2

Every M30 audit question maps to committed cells: *where frontier tokens go* → §1
matrix + §2 by-model split + §7 per-session rows; *which spends needed frontier
reasoning vs local-capable* → §1/§7 level-task attribution + §2 model mix (judgment is
E30.2's; the evidence rows are here); *corpus-overhead findings* → §3 billed context
medians + §4 corpus packs; *paid vs local* → §§1–3 vs §5. Anything not answerable from
those cells is covered by a numbered gap record (§6) — E30.2 cites gaps as gaps and
never needs the raw transcripts.
