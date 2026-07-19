---
project: ai-project-system
phase: P9
milestone: M30
epic: E30.4
type: reference
status: active
last_updated: 2026-07-18
---

# Echo-Cost Note — E30.4 before/after evidence (P9-M30)

**What this is:** the mechanism-produced before/after evidence for E30.4's
reference-don't-display reconciliation (SN-23). "Before" is the token cost of the
artifact bodies governance **mandated** into parent-chat context (full-starter
fenced echo per pre-E30.4 AOG §3.1.1; Delivery-Notice paste per the pre-E30.4
artifact-communication-protocol §Manual Mode), measured from the real committed
M30 artifacts. "After" is the canonical §3.1.1 reference line that replaces each
of them.

**Tokenizer:** tiktoken `o200k_base` — the same proxy as the E30.1 mechanism's
Direction B (`bin/measure-token-burn`). **All numbers are proxy tokens with
±10–15% error bars (G10) — suitable for proportions and ordering, never billed
counts.** SN-23's original ≈2.2–2.8K/≈1.0–1.3K figures were word counts; the
tokenizer-based figures below supersede them for this record and land in the same
order of magnitude.

---

## 1. Before/after, per real M30 handoff artifact

Starter "before" = body + the mandated four-backtick fence header + copy
instruction (34 proxy tokens of overhead). Notice "before" = body as pasted.
"After" = the canonical reference line (§3.1.1 format: artifact type + id —
repo-relative path — status).

| artifact (committed file) | before (echo, proxy tok) | after (reference line) | eliminated per handoff | factor |
|---|---:|---:|---:|---:|
| E30.1 epic starter | 3,031 | 50 | 2,981 | 61× |
| E30.2 epic starter | 3,420 | 50 | 3,370 | 68× |
| E30.3 epic starter | 3,386 | 50 | 3,336 | 68× |
| E30.4 epic starter | 2,691 | 50 | 2,641 | 54× |
| M30 milestone starter | 3,627 | 47 | 3,580 | 77× |
| P9 phase starter | 2,721 | 41 | 2,680 | 66× |
| E30.1 Delivery Notice | 1,401 | 44 | 1,357 | 32× |
| E30.2 Delivery Notice | 1,975 | 44 | 1,931 | 45× |
| E30.3 Delivery Notice | 1,862 | 47 | 1,815 | 40× |

**Medians:** starter echo eliminates ≈3,160 proxy tokens per handoff (range
2,641–3,580); Delivery-Notice paste eliminates ≈1,815 (range 1,357–1,931).

**Persistence multiplier (why per-handoff numbers understate the cost):** an
echoed body lands in the parent session's history and is re-read at cache rates
on **every subsequent call** of that session (audit report §2.1–2.2: cache
re-reads are 48.5% of weighted window cost; parent mixed sessions 53%). The M30
Milestone-Chat session's history holds three full-starter echoes ≈ 9,700 proxy
tokens of pure duplication carried on each of its calls — this epic's "before" is
sitting inside E30.2's measured window.

---

## 2. Honest bound (SN-23, stated verbatim in substance)

Reference-first does **not** make ingestion free. The consumer still reads the
referenced file **once, selectively** (frontmatter + Summary + DoD/QA suffices
under PSG §11.6 default-accept). What the reconciliation eliminates is the
**duplication**: the producer's echo of a body it just wrote to file, the
parent's full-body display of a committed starter, and the second ingestion of a
pasted Delivery Notice. The claim is "each artifact body ingested once, where
needed" — not "never ingested." The table's "eliminated" column is therefore an
upper bound on the per-handoff saving; the realized saving per handoff is
(eliminated − the consumer's one selective read of whatever sections it needs).

**Billed effects are forward-looking only.** These are proxy measurements of
committed files, not billed deltas; per the M30 discipline, no billed-median
improvement is claimed as achieved. Future E30.1-mechanism captures over
post-E30.4 sessions are the verification path.

---

## 3. Gap record (continuing the G-series)

- **G14 — echo share of the historical billed window is not isolable.** The
  E30.1 dataset records billed per-call totals, not which input tokens were
  governance-mandated echo; the historical sessions' exact billed echo cost
  cannot be re-measured retroactively. Recorded as a gap, not estimated. The
  per-artifact proxy numbers above plus the report's cache-re-read shares are the
  honest available evidence.

---

## 4. Reproduction

From the repo root, with tiktoken installed (same setup as
`bin/measure-token-burn` Direction B):

```python
import tiktoken
enc = tiktoken.get_encoding("o200k_base")
base = "docs/phases/P9__Context_Handling_and_Token_Efficiency/"
FENCE = len(enc.encode("````markdown name=x-epic-execution-chat-starter.md\n")) + \
        len(enc.encode("````\nCopy the entire chat starter above and paste into "
                       "your Coding Agent chat to begin execution.\n"))  # 34
for f, is_starter in [
    ("P9-M30-E30.1__epic-execution-chat-starter.md", True),
    ("P9-M30-E30.2__epic-execution-chat-starter.md", True),
    ("P9-M30-E30.3__epic-execution-chat-starter.md", True),
    ("P9-M30-E30.4__epic-execution-chat-starter.md", True),
    ("P9-M30__milestone-execution-chat-starter.md", True),
    ("P9__phase-execution-chat-starter.md", True),
    ("P9-M30-E30.1__delivery-notice.md", False),
    ("P9-M30-E30.2__delivery-notice.md", False),
    ("P9-M30-E30.3__delivery-notice.md", False),
]:
    body = len(enc.encode(open(base + f, encoding="utf-8").read()))
    print(f, body + (FENCE if is_starter else 0))
```

"After" values tokenize the canonical reference line for each artifact in the
AOG §3.1.1 format; line lengths vary 41–50 proxy tokens with the P9 paths (a
short-pathed repo will sit lower — the order of magnitude is what matters).

---

## Related

- SN-23: `.ai-project/artifacts/steering-notes/2026-07-18__creation-chat__steering-note__reference-dont-display.md` (master)
- The rule this evidences: `governance/AI-OPERATING-GUIDELINES.md` §3.1.1 (v2.10.0)
- Cost frame: [`audit-report.md`](audit-report.md) §2.1–2.2; [`README.md`](README.md) (G10)
- Sibling lever: [`context-scoping.md`](context-scoping.md) (E30.3 — what a chat *loads*; this note — what governance mandated into *history*)
