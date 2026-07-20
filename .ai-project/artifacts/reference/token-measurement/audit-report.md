---
project: ai-project-system
phase: P9
milestone: M30
epic: E30.2
type: reference
status: active
last_updated: 2026-07-17
---

# Token-Burn Audit Report — E30.2 (P9-M30)

**Evidence base (sole source):** the committed E30.1 dataset —
[`token-burn-dataset.json`](token-burn-dataset.json) /
[`token-burn-dataset.md`](token-burn-dataset.md) + mechanism
[`README.md`](README.md). 72 paid sessions, window 2026-06-12 → 2026-07-17,
plus one local (ollama) run. No session parsing, raw transcripts, or external
benchmarks were used. Every claim below cites a dataset section/row (of the
`.md` twin, mirrored in the JSON) or a gap record (G-id). Judgments are labeled
as judgments.

**Companion artifacts:** the derived frontier-vs-local policy lives in
[`model-routing-policy.md`](model-routing-policy.md) (Design Decision 1, §7
below); the refreshed `models:` block lives in `.ai-project.yml` and points
back here.

---

## 1. Price weighting (documented per the Hard Constraint)

Raw token counts misstate where the money goes — cache reads are 94.8% of raw
volume (§2 below) but bill at ~0.1× base input. All cost figures in this report
apply the following weighting to the dataset's four usage components, which the
dataset keeps separate for exactly this purpose (dataset §1 note; README "What
the measured numbers mean"):

| component | weight | rate basis |
|---|---|---|
| `input` | 1.0× base input | per-model list price |
| `cache_creation` | 1.25× base input | 5-minute-TTL cache-write premium |
| `cache_read` | 0.10× base input | cache-read discount |
| `output` | per-model output price | — |

**Rates used** (per MTok, Anthropic list pricing, source:
platform.claude.com/docs/en/pricing via the Claude API reference, cached
2026-06-24): claude-fable-5 $10 in / $50 out; claude-opus-4-8 $5 / $25;
claude-sonnet-5 $3 / $15; claude-sonnet-4-6 $3 / $15. These are the four (and
only four) models in the dataset's §2 frontier mix.

**Exactness and caveats:**

- Costs are computed per session **per model** from the dataset JSON's
  `paid_sessions.sessions[].by_model` component splits — no blended-rate
  approximation is involved. The arithmetic is reproducible from the committed
  JSON alone.
- **Cache-write TTL is not recorded in the dataset.** The 1.25× weight assumes
  5-minute-TTL writes (the weighting the dataset README states). If some or
  all writes were 1-hour-TTL (2× base input), cache-creation cost is
  underestimated by up to 1.6×, bounding the window total at **$623–$735**.
  Component *ordering* is unaffected (cache-read remains the largest cost
  component at either bound).
- **Sonnet 5 introductory pricing** ($2/$10 through 2026-08-31) would lower
  claude-sonnet-5's share slightly for the measured window; the standard rates
  are used because the policy is forward-looking. Ordering is unaffected.
- Every model's output/input price ratio in this mix is exactly 5×, so
  relative comparisons between cells are insensitive to rate-table revisions
  that preserve that ratio.

---

## 2. Where the paid tokens (and dollars) go

**Window total: ≈ $623** across 72 sessions / 35 days (≈ $18/day average).
(Dataset §7 rows aggregated; weighting per §1.)

### 2.1 By usage component (dataset §1 components, aggregated over all sessions)

| component | raw tokens | raw share | cost | cost share |
|---|---:|---:|---:|---:|
| cache_read | 705,993,054 | 94.8% | $302.28 | **48.5%** |
| cache_creation | 32,415,570 | 4.4% | $186.05 | **29.8%** |
| output | 5,589,219 | 0.8% | $133.11 | **21.4%** |
| input (uncached) | 365,970 | 0.05% | $1.91 | 0.3% |

Finding: after honest weighting, **context re-reads are still the single
largest cost component (≈half)**, but cache-creation and output — 5.2% of raw
volume combined — carry the other half. An audit summing raw counts would have
attributed ~95% of spend to cache reads; that is the misstatement the Hard
Constraint's price-weighting requirement exists to prevent.

### 2.2 By level × task-type cell (dataset §1 matrix + mixed buckets, weighted)

| level | task | sessions | cost | share | per-session median |
|---|---|---:|---:|---:|---:|
| milestone | mixed (G7) | 13 | $205.58 | 33.0% | $11.71 |
| epic | execution | 38 | $144.20 | 23.1% | $2.92 |
| phase | mixed (G7) | 5 | $97.36 | 15.6% | $20.84 |
| creation | unattributed (G6) | 5 | $62.77 | 10.1% | $4.89 |
| hq | planning | 3 | $30.89 | 5.0% | $4.75 |
| unattributed | mixed (§7 row `4735e1dc`) | 1 | $26.72 | 4.3% | — |
| epic | mixed (§7 row `aaa16d82`, branch-fallback — lower confidence) | 1 | $18.94 | 3.0% | — |
| milestone | planning | 2 | $13.49 | 2.2% | $6.75 |
| hq | mixed (G5) | 1 | $8.64 | 1.4% | — |
| milestone | review | 1 | $7.51 | 1.2% | — |
| milestone | unattributed (§7 row `b1444f31`, branch-fallback) | 1 | $4.03 | 0.6% | — |
| phase | planning | 1 | $3.23 | 0.5% | — |

Level totals: **milestone $230.61 (37.0%) > epic $163.14 (26.2%) > phase
$100.60 (16.1%) > creation $62.77 (10.1%) > hq $39.53 (6.3%)**.

Findings:

1. **The parent chats, not the epic executors, are the biggest paid sink.**
   Milestone + phase together are 53.1% of spend, dominated by long
   mixed-purpose sessions (planning+review+closure in one session — split is
   G7). A median milestone mixed session costs 4× a median epic execution
   ($11.71 vs $2.92); a median phase mixed session costs 7× ($20.84).
2. **Epic execution is the highest-volume attributed cell** (38 sessions,
   first-message-attributed, highest confidence) but is cheap per session —
   the framework's scoped, spec-driven epics keep individual executions
   bounded.
3. Confidence flags: the two `branch-fallback` rows and the mixed buckets are
   lower-confidence attributions by the mechanism's own documentation (README
   "Attribution rules"; dataset §7 rule columns); they total ~8% of spend and
   do not change any ordering above.

### 2.3 Frontier mix — which models actually ran (dataset §2 + per-session `by_model`)

| model | cost | share |
|---|---:|---:|
| claude-opus-4-8 | $309.08 | 49.6% |
| claude-sonnet-5 | $145.08 | 23.3% |
| claude-fable-5 | $116.33 | 18.7% |
| claude-sonnet-4-6 | $52.87 | 8.5% |

Per-level cost mix (aggregated from `paid_sessions.sessions[].by_model` in the
dataset JSON, keyed by each session's attributed level):

| level | top model | per-level model split |
|---|---|---|
| milestone | claude-opus-4-8 | opus-4-8 $138.09, sonnet-5 $50.49, fable-5 $37.64, sonnet-4-6 $4.40 |
| epic | claude-opus-4-8 (narrowly) | opus-4-8 $65.88, sonnet-5 $63.93, fable-5 $30.45, sonnet-4-6 $2.88 |
| phase | claude-opus-4-8 | opus-4-8 $54.36, sonnet-5 $22.40, sonnet-4-6 $14.32, fable-5 $9.52 |
| creation | claude-fable-5 (narrowly) | fable-5 $29.88, opus-4-8 $27.23, sonnet-5 $5.66 |
| hq | claude-opus-4-8 | opus-4-8 $23.53, sonnet-4-6 $8.64, fable-5 $4.75, sonnet-5 $2.61 |

Findings:

4. **The `models:` block's remote entries were fiction.** Neither
   `remote:gpt-4o` nor `remote:claude-3-5-sonnet` appears in a single one of
   the 72 sessions (dataset §2) — the stale names never ran in the measured
   window. The refresh (§7) replaces falsified entries with the measured
   reality; this is P9's founding evidence in one line.
5. **claude-opus-4-8 is the measured workhorse**: half of all spend, and the
   top model at hq, phase, and milestone — the three levels the `models:`
   remote keys govern.
6. *Interpretation caveat (judgment):* the mix reflects the CFO's Claude Code
   model selection over the window, not a deliberate per-level routing
   experiment. The dataset records spend, not per-model output quality (new
   gap **G12**, §6).

---

## 3. Needed-frontier vs local-capable (the report's central judgment)

**This section is judgment, grounded in the cited rows; it is not a
measurement.** The measured local evidence is a single run — 404 output
tokens, qwen2.5-coder:14b, input tokens unmeasured (dataset §5, G9) — so no
cell can be *proven* local-capable from this dataset. What the paid rows do
support:

| level × task | verdict (judgment) | grounding |
|---|---|---|
| epic × execution | **Paid today; the designated local-offload experiment.** Best candidate *by shape*: highest-volume attributed cell (38 sessions, §2.2), cheapest and most bounded per session (median $2.92, median ~46 calls — §7 rows), spec-driven with test-verifiable outputs. But local capability is unproven: one measured local run (§5), no input-token measurement (G9), no measured QA-role run at all (**G11**, §6), no quality measures (**G12**). | dataset §§1, 5, 7; G9, G11, G12 |
| milestone × all | **Needs frontier.** Largest spend share (37%, §2.2); sessions bundle planning, Stage-2 review, and closure authority (mixed, G7) — long-horizon governance judgment where an error propagates into merges. Offload here is also *untargetable* today: the per-task split inside these sessions is gap-recorded (G7/G4). | §2.2; G4, G7 |
| phase × all | **Needs frontier.** Same shape as milestone at the next altitude; costliest sessions per unit (median $20.84, §2.2); mixed split gap-recorded (G4/G7). | §2.2; G4, G7 |
| hq × all | **Needs frontier; manual by design.** CFO-facing scoping/digest judgment (per-task split G5). HQ and Creation remain manual at all times per the pinned product direction (SN-22) — the paid-vs-local question at these levels is not an automation question. | §2.2; G5; SN-22 |
| creation × all | **Needs frontier; manual by design.** Level totals measured, task split invisible to repo-write signals (G6); no `models:` key exists for creation (schema fact, see §7.2). | §2.2; G6; SN-22 |

Supporting judgment from the numbers: **model-downgrade at the epic level is
not the biggest available lever.** Epic execution is 23% of spend; the
milestone/phase parent sessions are 49% and their cost is dominated by context
re-reads (§2.1) — which E30.3's context-load reduction targets directly,
independent of model choice. Local offload at epic remains worthwhile (it is
M31's dual-mode experiment) but should be sized against a $144/35-days cell,
not against the total.

---

## 4. Governance-corpus overhead (E30.3's evidence frame — dataset §§3–4)

All §4 corpus figures are o200k-proxy tokenizations with ±10–15% error bars
(G10); billed context medians in §3 are exact provider-billed numbers.

- **Per-level governance packs** (starter + required specs + PSG + AOG,
  dataset §4): phase 30,478 / milestone 36,614 / epic 29,336 proxy tokens.
- **Billed first-turn context medians** (dataset §3): 19,356 (milestone) to
  29,749 (creation). Note the first turn bills the harness system prompt +
  memory + opener — the governance *specs* mostly enter later, as
  tool-read results that land in cache-creation (G10 note in dataset §6).
- **Billed per-call context medians** (dataset §3): epic 76,135 / hq 101,163 /
  creation 102,515 / milestone 129,135 / phase 169,003. This is what every API
  call re-reads, and it is what §2.1's dominant cache-read cost is made of.
- **Corpus totals** (dataset §4): `governance/` = 157,287 proxy tokens over 69
  files; PSG + AOG + yml-spec alone = 29,663.

Findings for E30.3:

7. **The governance pack is a minority — but material — share of context
   load.** A ~30–37K pack against per-call context medians of 76–169K means
   roughly 20–40% of what a call re-reads is at most governance corpus
   (upper bound: packs assume the whole pack stays in context); the rest is
   conversation history, tool results, and harness overhead. Context-load
   reduction must therefore target *total* per-call context, not only
   governance documents.
8. **The prior 24K/157K estimates are history only.** The measured per-level
   packs (29–37K) supersede the 24K working-set estimate; the 157,287-token
   `governance/` total (dataset §4) supersedes the 157K full-corpus estimate.
   No conclusion in this report derives from the prior estimates (Hard
   Constraint; README "Blind spots").
9. Cost framing for reduction work: halving per-call re-read context across
   the parent-chat levels would address a share of the ~$302 cache-read
   component (§2.1) an order of magnitude larger than eliminating the entire
   epic-execution output spend.

---

## 5. Paid vs local

Paid spend: §§1–3 of the dataset, ≈$623 for the window (this report §2).
Local spend: dataset §5 — one run, 404 output tokens, ~20.6s, model
qwen2.5-coder:14b, input tokens unmeasured (G9), electricity/hardware cost not
modeled. The two are never merged (README). There is no measured basis for a
paid-vs-local cost *ratio* yet; producing one is M31 dual-mode territory.

---

## 6. Gap records

**Carried forward unchanged from the dataset (§6): G1–G10.** In brief: G1/G3
structural (epic planning/review live in parent chats; only epic chats
execute); G2 epic closure bundled into execution; G4 milestone/phase
review+closure inside mixed sessions; G5 HQ task split; G6 creation task
split; G7 mixed-session splits unattributable; G8 this-machine-only coverage
(claude.ai-web work invisible); G9 local input tokens unmeasured; G10
tokenizer proxy error bars.

**New gaps recorded by this audit (continuing the G-series):**

- **G11 (gap; epic_qa role):** No captured run exists for the QA-agent role in
  either spend kind — the sole local run (dataset §5) exercised the dev role
  only, and no paid session maps to it. The `epic_qa` mapping in `models:`
  therefore rests on adjacent evidence (the one local model with any measured
  run) rather than role-specific measurement. Revisit when M31's dual-mode
  runner produces QA-role runs.
- **G12 (gap; cross-cutting):** The dataset measures *spend*, not *output
  quality*: no per-model or per-level quality/outcome measure was captured.
  Judgments about which model a level *needs* (report §3; policy rows) are
  grounded in measured spend distribution, session shapes, and operational
  history — not in measured capability comparisons. Revisit if/when a quality
  signal (e.g. M31 run outcomes, review rejection rates) is instrumented.

---

## 7. Decisions (Design Decisions 1–4, resolved and recorded)

### 7.1 Policy home (Design Decision 1)

**Chosen: a sibling reference artifact —
[`model-routing-policy.md`](model-routing-policy.md) in this directory.**
Reasoning: (a) the policy is derived from *this repo's* measurements, and
rolling it out to other governed projects is an explicit E30.2 non-goal — so
it does not belong in the `governance/` corpus that ships to adopting repos;
(b) it sits beside its evidence (dataset + this report), giving M31 and the
CFO one stable directory for the whole chain policy → report → dataset;
(c) it versions cleanly in git and is linkable from `.ai-project.yml`.
Cross-links: the `models:` block comment points at the policy and this report;
the policy's rows cite this report's sections; this report cites the dataset.

### 7.2 Refresh shape (Design Decision 2)

**Chosen: pure value refresh — same five keys, new values; no yml-spec
semantics change.** The evidence does not force new semantics: the dataset's
wider level set (creation has no key) does not need a key because Creation is
manual-by-design and outside the block's domain — the `models:` block
configures *unattended agentic execution* (its own header comment), which per
SN-22 only Phase/Milestone/Epic will ever enter. Per-task routing and fallback
entries likewise have no measured basis (G7 blocks per-task targeting).
Validation rules 14–17 are untouched; the new values match rule 15's format
regex. No test changes required (the E26.2 guard tests pin `epic_dev`, which
is unchanged).

The refreshed mapping and its per-key grounding are recorded in the policy
(rows P1–P7). Summary: `hq`/`phase`/`milestone` → `remote:claude-opus-4-8`
(the measured workhorse at each of those levels, §2.3 findings 4–5, caveat
G12); `epic_dev` → `local:qwen2.5-coder:14b` (unchanged; the only local model
with any measured run, dataset §5); `epic_qa` → `local:qwen2.5-coder:14b`
(replacing the never-measured 7b with the only locally-evidenced model —
gap-grounded, G11).

### 7.3 yml-spec §3.4 stale defaults (Design Decision 3)

**Chosen: update the spec's documented defaults to the refreshed mapping**
(schema-documentation change → version bump v2.3.1 → **v2.4.0** + changelog
row), rather than leaving them with a rationale. Reasoning: the §3.4 defaults
table and §3.1 schema comments *define the defaults for adopters*; leaving
`remote:gpt-4o` / `remote:claude-3-5-sonnet` there would keep the falsified
names normative for every new adoption while this repo's config moved on —
the same divergence E26.2 closed for `epic_dev` (and E26.2's default change
took a minor bump: 2.1.0 → 2.2.0, the precedent followed here). Updated
consistently: §3.1 schema comments, §3.4 defaults + Allowed-Formats examples,
format-constraint examples. Validation rules unchanged. (The milestone
acceptance grep covers `.ai-project.yml` only; this decision is about honesty,
not the grep.)

### 7.4 Report location (Design Decision 4)

**Chosen: the spec's recommendation** —
`.ai-project/artifacts/reference/token-measurement/audit-report.md` (this
file), beside its evidence, stable and linkable by E30.3 and M31.

---

## 8. Observations carried to the parent chats (out of E30.2 scope)

- **`bin/ai-project-orchestrator` `DEFAULT_MODELS` (lines 17–23) still
  hardcodes the falsified names** (`remote:gpt-4o`, `remote:claude-3-5-sonnet`)
  and `epic_qa: local:qwen2.5-coder:7b` as in-script fallbacks for when the
  `models:` block is absent. Runtime-inert for this repo (the block is
  present), and orchestrator changes are outside E30.2's in-scope list — but
  M31 should align `DEFAULT_MODELS` with the refreshed mapping when it builds
  the guardrail/decision machinery, extending the E26.2 consistency-guard
  pattern (tests/test_model_config.py) beyond `epic_dev`.
- The mixed-bucket dominance (G7) means **future measurement precision at the
  parent-chat levels requires within-session task segmentation** — noted for
  whoever next touches `bin/measure-token-burn` (E30.3-era candidate, per the
  E30.1 README's future-work note).
