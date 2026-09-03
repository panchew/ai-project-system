---
project: ai-project-system
phase: P9
milestone: M30
epic: E30.2
type: reference
status: active
last_updated: 2026-07-17
---

# Frontier-vs-Local Model Routing Policy (P9-M30-E30.2)

**What this is:** the recorded answer to "when is a paid frontier model the
default, and when does a local model suffice?", derived from the E30.1
measurements — not from pre-existing assumptions (M30 Hard Constraint). Every
row traces to the [audit report](audit-report.md) (which cites the
[dataset](token-burn-dataset.md) cell or gap record).

**Who consumes it:** M31's manual-mode guardrail verifies chats against the
`.ai-project.yml` `models:` block, which implements rows P5–P7 of this policy;
M31's agentic paid-vs-local decision logic applies the defaults below. The
CFO reads this file; the block comment in `.ai-project.yml` links here.

**Domain note:** the `models:` block configures *unattended agentic
execution*. Per the pinned product direction (SN-22), only Phase, Milestone,
and Epic chats ever go agentic; Creation and HQ stay manual at all times.
Manual chats run on whatever the CFO's harness selects (the measured mix —
report §2.3); the policy still records their paid-vs-local answer because the
M30 audit question covers every level.

## Policy rows

Defaults are per chat level; per-task-type splits are gap-recorded where the
dataset cannot separate them (G4–G7), which is Hard-Constraint-compliant.

| row | level (× task) | default | why (traces to report) | confidence / gaps | revisit trigger |
|---|---|---|---|---|---|
| P1 | creation × all | **Paid frontier, manual** | CFO-facing inception judgment; manual-by-design (SN-22). Measured as level totals only — task split invisible to repo-write signals (report §3; G6). No `models:` key exists or is needed (report §7.2). | Task split gap-recorded (G6) | Creation ever entering agentic scope (no current plan) |
| P2 | hq × all | **Paid frontier, manual** | Scoping/digest/coordination judgment feeding CFO decisions (report §3); manual-by-design (SN-22). Per-task split gap-recorded (G5). | Task split gap-recorded (G5) | HQ ever entering agentic scope (no current plan) |
| P3 | phase × all | **Paid frontier** | Long-horizon governance judgment + review/closure authority; costliest sessions per unit (median $20.84 — report §2.2); errors propagate into merges (report §3). Per-task split inside mixed sessions gap-recorded (G4/G7), so selective offload is untargetable today. | Mixed-bucket attribution (G4, G7) | Within-session task segmentation landing (report §8) |
| P4 | milestone × all | **Paid frontier** | Largest spend share (37% — report §2.2) *and* the level where Stage-2 accept authority lives; same mixed-bucket shape as phase (report §3; G4/G7). **The tier stays paid frontier** — evaluated against local inference 2026-07-31 and not moved (see the P4 note below). **The value is set by CFO allowance decision (SN-41), not by measurement** (mapping row); the one measurement of the configured engine (E41.4, 2026-09-01) is neutral toward the decision (see the P4 note below). | Mixed-bucket attribution (G4, G7); local candidate established but **prescription variance unmeasured, search/absence-detection and tool-using verification untested** (G-P4-a/b/c) | Same as P3, **or** an evaluation clearing G-P4-a, G-P4-b and G-P4-c (HQ Ruling 2026-07-31) |
| P5 | epic × execution | **Paid frontier today; designated local-offload experiment (M31)** | Highest-volume attributed cell, bounded and spec-driven (38 sessions, median $2.92 — report §2.2/§3): the best offload candidate *by shape*. Local capability unproven: one measured local run, 404 output tokens (dataset §5), input unmeasured (G9), no quality measure (G12). Paid remains the default until M31 dual-mode produces run evidence. | Local evidence thin (G9, G12) | M31 dual-mode runs at epic level |
| P6 | epic × dev-agent lane (`epic_dev`) | **`local:qwen3-coder:30b`** — the local lane M31's runner uses when the P5 experiment runs | **Row changed on new cited evidence (P10-M33, applied P10-M34-E34.3).** The prior value `qwen2.5-coder:14b` was *falsified by running it*, not by argument: E33.2 **Run A** dispatched the then-configured `epic_dev`/`epic_qa` model against a real epic and returned **exit 0 having done nothing** — 0 tool rounds, 0 files changed, SN-3 markdown-plan mode. **Run B** — same epic, same Ollama runtime, `qwen3-coder:30b` — produced mergeable work; **E33.4** then ran a second real epic (`home_finance`) on the same model to complete, green work (275 examples, 0 failures). The model was the lever; the runtime was never the problem. Loadability envelope, recorded honestly: Q4_K_M/18.6 GB **exceeds** the proving box's 16 GB VRAM and **partially offloads to RAM** (12.9 GB VRAM / 21.4 GB total), running ~9.4 tok/s against the 14b's 12.2 on the same epic — slower, but it finishes. That is the ratified trade. Cited: `docs/phases/P10__Fleet_Adoption_and_Local_Inference_Proving/P10-M33-E33.2__runtime-decision.md`; `agentic-runs/P10-M33-E33.2/run-record.md`; `agentic-runs/P10-M33-E33.4/run-record.md`. | Two real epics on the new value, one comparative same-runtime pair; **no quality signal captured (G12 still open)**; input-token measurement gap (G9) unchanged. Exit codes proven unreliable in *both* directions on this stack (E33.2 Run A: exit 0, zero work; E33.4: exit 2, complete work) — verification reads the transcript and the target repo, never the exit status | A third real agentic epic on the raised tier disagreeing with these two, the first captured **quality** signal (G12), or a loadability change on the execution host (the partial RAM offload is the standing fragility) |
| P7 | epic × qa-agent lane (`epic_qa`) | **`local:qwen3-coder:30b`** | **Referent updated; the reasoning is unchanged, and that is deliberate.** The QA role still has **zero** captured runs of its own — **G11 remains open**. M33 produced no isolated QA-role run because the runner dispatches dev and QA from one model in practice (E33.2 run record: *"Run A is the configured `epic_dev`/`epic_qa` model"*), so E33.2/E33.4 gave the **dev** lane its evidence, not this one. This row therefore does **not** move on new QA-lane evidence — none exists. It moves on exactly the reasoning it already carried, *gap-grounded interim default: the one local model with any run evidence* (report §7.2 standard), with the referent updated from `qwen2.5-coder:14b` — which E33.2 Run A falsified — to `qwen3-coder:30b`. No QA-lane evidence is claimed here. | Gap-grounded (**G11 open — zero captured QA-role runs**); evidence is dev-lane adjacent only (G9, G12) | The first **isolated QA-role** run — G11's own closure condition, still unfired; a dispatch change that gives the QA lane a separate model would fire it sooner |

### Note on row P4 — Milestone × local inference, evaluated 2026-07-31, row unchanged

P10-M35-E35.5 back-tested `qwen3.6:27b` (Q4_K_M) against five known-ground-truth defects from
this repository's own history — pre-registered rubric, blinded packets, ten scored runs, every
run committed including the ones that did not help. Result: **PASS at 4 of 5 with zero false
alarms**, against a threshold written before any model ran.

**HQ ruled the row unchanged** (`.ai-project/artifacts/rulings/2026-07-31__ai-project-system-hq__ruling__milestone-locality-row-p4.md`).
The evaluation earned **candidacy**, which was the bar the 2026-07-30 SN-25 ruling set for it —
and candidacy is not adoption. The decisive finding is not the miss but its shape: the two runs
on defect 5 produced **identical diagnoses and opposite prescriptions** at the same prompt and
settings. At Milestone the remedy *is* the decision, so a prescription that depends on the
sampling draw cannot hold Stage-2 accept authority. Behind that sit three untested faculties —
measured prescription variance (**G-P4-a**), unassisted search and absence-detection over a real
branch (**G-P4-b**), and tool-using verification of a claim before ruling on it (**G-P4-c**).

What the evidence *does* establish, and what makes the candidacy real: the model reasoned
correctly in **both** directions on exit-code untrust — rejecting exit 0 with zero work,
accepting exit 2 with complete green work — from transcript, diff and suite result rather than
the status code. That is the judgment **P10-GH-7** records as measured-broken in automated
detection.

Not evidence in either direction: `Getawayinsured2023` routes `milestone:` to **`remote:`**
`qwen3.6:27b`. The "natural experiment" this policy's readers were once told existed does not
exist on the locality axis (phase spec corrected at v1.3.1).

### Note on row P4 — reconciled with the SN-41 baseline lineup and E41.4's back-test, 2026-09-01 (P12-M41-E41.5)

**Recorded beside the row, per the file's own convention above — nothing in row P4's `default` or
`why` cells is edited by this note.**

Three separate facts about this one cell are now visible together for the first time, and holding
them apart is the point of this note (`decision made` ≠ `value configured` ≠ `measured`):

1. **DECISION MADE, 2026-08-19.** HQ Ruling, Decision 15
   (`.ai-project/artifacts/rulings/2026-08-19__ai-project-system-hq__ruling__p12-opening-and-sn-30-37-triage.md`):
   row P4 **CLOSED** by CFO decision, a **policy-row change** (Change discipline satisfied by
   decision, not by new cited evidence) — decided value `milestone → Deepseek V4 Flash`.
2. **VALUE CONFIGURED, 2026-08-27.** HQ Ruling on SN-40..46
   (`.ai-project/artifacts/rulings/2026-08-27__ai-project-system-hq__ruling__sn40-46-baseline-lineup-and-the-switching-ratchet.md`),
   landed via PR #236 (`master` `3222f50`, outside P12's milestone machinery per SN-40..46 Decision
   6): the mapping row below now reads `milestone → remote:deepseek-v4-pro` — **`pro`, not
   `flash`** — attributed honestly as *"value set by CFO allowance decision (SN-41), not by
   measurement."* **This is a different engine than the one row P4 was closed on**, landed by a
   second, later, and separate CFO decision, not by the G-P4 evidential path above.
3. **MEASURED, 2026-09-01.** E41.4 (PR #239, merged to `milestone/M41` at `9f50e39`;
   `.ai-project/artifacts/reference/local-review-backtest/e41-4-runs/d4-bars-and-recommendations.md`)
   back-tested the **now-configured** `deepseek-v4-pro` against the unchanged `claude-opus-5`
   incumbent on E35.5's frozen instrument: **absolute bar PASS for both** (10/10 CATCH, 0 false
   alarms each); **relative bar cleared by neither** — identical on every check. Escalated to the
   CFO as a **neutral** result
   (`.ai-project/artifacts/escalation-notices/2026-09-01T00_00_00Z__P12-M41-E41.4__escalation_notice.md`),
   not landed and not dropped.

**The reconciliation, stated plainly.** Row P4's `why` cell above still justifies **"Paid
frontier"** by spend share, Stage-2 accept authority, and *"evaluated against local inference
2026-07-31 and not moved"* — a sentence that names only the **first** evaluation and predates the
second. Read together with the mapping row's honest attribution, the two no longer describe one
process: **the configured value was set by allowance, not by measurement, and the one measurement
this project holds of that configured engine (E41.4) neither supports nor contradicts the
decision** — it found `deepseek-v4-pro` indistinguishable from the incumbent on the frozen
instrument, which is silence, not endorsement, and it says nothing at all about `Deepseek V4
Flash`, the engine the 2026-08-19 closure actually named. **Neither statement above is false; they
now require this note to be read as one.**

**What this note does not do.** It does not move row P4's `default` cell, rewrite its `why` cell,
or touch the mapping table's `milestone` cell (which stays at what #236 landed) — all three stay
put for the same reason the 2026-07-31 note above left them: `test_policy_mapping_agrees_with_yml_block`
forces the mapping table to agree with `.ai-project.yml`, and the tier cells sit **outside** that
guard's parse, where a divergence no test can catch is worse than one that fails a build. It does
not re-close or re-open row P4 — that decision stands as HQ recorded it. **Actually rewriting the
row's language to describe an allowance-decided value is M44's E44.2 to execute** (M41 spec
v1.6.0, changelog 2.0.0); this note is the record that the gap exists and is bounded, filed by
P12-M41-E41.5 per its spec v2.0.0 deliverable D-A.

## The decided-vs-evidenced convention (P12-M44-E44.2)

A row in this file records three facts about its value, and the convention is that a reader can
tell them apart **from the row alone, without inference**:

- **DECIDED** — a decision named the value (or the tier). Written form: a dated decision citation
  (a ruling ref) beside the row or in the row's own note — e.g. row P4's 2026-08-19 closure and
  the SN-40..46 lineup.
- **CONFIGURED** — the value has landed. Written form: the value's presence in the mapping table
  below, which `test_policy_mapping_agrees_with_yml_block` forces to agree with `.ai-project.yml`.
- **EVIDENCED** — a measurement supports the value, or the record says plainly it was not measured.
  Written form: the provenance clause in the row's `why` cell — *"value set by CFO allowance
  decision (SN-41), not by measurement"* for an allowance-decided value, or a cited measurement
  for an evidenced one.

**Both faces are covered:**

1. **decision-ahead-of-configuration** (the R6 case, now historical): a decision is recorded while
   its value is still pending. Written form: the decision named beside the row with the state
   *"value not configured"*, and no value in the mapping table until it lands. The three carried
   rows — `phase`, `milestone`, `epic_manual` — are the historical instance: decided under R6,
   configured since SN-41, retained as the case that forced the convention, **not as a pending
   edit**.
2. **configuration-ahead-of-evidence** (the SN-41 case, live): a value is configured by allowance,
   not by measurement. Written form: the mapping row carries the allowance attribution *"value set
   by CFO allowance decision (SN-41), not by measurement"*, and the tier row's `why` cell says the
   same — it must not describe an evidential derivation that never produced the value. **Row P4 is
   the worked case**: its `why` cell now reads *"The value is set by CFO allowance decision
   (SN-41), not by measurement … the one measurement of the configured engine (E41.4) is neutral
   toward the decision."*

**Why one place rather than several:** a decision and its evidence attach to the **same row**, and a
reader who must read a second document to reconcile them has already lost. Stating the convention
here — in the file that owns the rows — means a reader meets the rule at the row it governs.

**Distinguishability without inference:** the three facts are distinguishable from the record alone
because each has a stated written form in a named place — a decision is a dated citation, a
configuration is a value present in the mapping table, an evidence claim is a provenance clause in
the `why` cell. None is inferred from another: a mapping value present is configured even if its
`why` cell is silent; a `why` cell that says "not by measurement" is an allowance-decided value even
if no ruling is quoted in the same cell.

## Mapping to `.ai-project.yml` `models:` (the M31 guardrail target)

| key | value | policy row |
|---|---|---|
| `hq` | `remote:claude-opus-5` | P2 (paid frontier; value = measured workhorse at hq — report §2.3) |
| `phase` | `remote:gpt-5.6-sol` | P3 — **value set by CFO allowance decision (SN-41), not by measurement** |
| `milestone` | `remote:deepseek-v4-pro` | P4 — **value set by CFO allowance decision (SN-41), not by measurement** |
| `epic_dev` | `remote:deepseek-v4-flash` | P6 — **value set by CFO allowance decision (SN-41), not by measurement** |
| `epic_qa` | `remote:deepseek-v4-flash` | P7 — **value set by CFO allowance decision (SN-41), not by measurement** |

> **Baseline lineup, 2026-08-27 (SN-41).** Four of these five values changed by **CFO
> allowance decision**, and the Change discipline is satisfied **by decision rather than by
> cited evidence — said so rather than manufacturing a citation**, the same honest form used
> for row P4's closure. **No measurement supports them.** The paragraphs below describe how
> the *previous* values were derived and are retained as history; **they do not describe
> these.** `epic_dev`/`epic_qa` leave `local:qwen3-coder:30b` because **local inference is
> PARKED, re-enterable (SN-43)** — that value's E33.2/E33.4 evidence is not retracted, only
> off the baseline. **`epic_manual` is `remote:deepseek-v4-flash`** (CFO, 2026-08-27, "all
> three"); it is a manual verification target and carries no policy row.

**Why the Opus line for the remote keys:** `claude-opus-4-8` carried 49.6% of
all measured spend and the plurality of spend at each of hq, phase, and
milestone (report §2.3, findings 4–5) — it is the model that demonstrably did
this governance work in the window. Choosing among the four measured models
involves judgment (no quality measure was captured — G12); choosing a model
*outside* the measured mix would repeat the original fiction. Neither `gpt-4o`
nor `claude-3-5-sonnet` ran once in 72 sessions (dataset §2).

**Version refresh, 2026-07-28 (`claude-opus-4-8` → `claude-opus-5`):** the
measured version stopped being offered in the harness surface in use, halting
every manual chat under the M31 guardrail (P10-M34 Escalation Notice). HQ
refreshed this table to the same line's successor version. This is a **mapping
change, not a row change**: rows P1–P4 decide a *tier* ("Paid frontier"), and
`claude-opus-5` is paid frontier, so the Change-discipline rule below — which
binds *rows* to new cited evidence — is not engaged and no re-run of the M30
evidence process is required. The evidence above still says what it said: it
justifies the Opus line over the measured alternatives, and a same-tier
successor inherits that justification. See
`.ai-project/artifacts/rulings/2026-07-28__ai-project-system-hq__ruling__paid-frontier-model-mapping-refresh.md`.

**Mapping revisit trigger — model unavailability.** This table (not rows
P1–P7) is revisited whenever a mapped model becomes unavailable, is
deprecated, or is superseded within its tier. Recorded here rather than in the
rows' *revisit trigger* column deliberately: a **tier is never deprecated —
only a version is**, so unavailability can only ever falsify a mapping, never
a policy row. Same-tier refreshes are applied under this trigger without new
evidence; anything that would change the *tier* remains a row change and takes
the Change-discipline path.

**Two changes on 2026-07-28 are not one change.** This file was edited twice
that day and the edits are different in kind — keeping them distinct is the
point of the rule above:

| | Paid-frontier refresh (HQ Ruling) | Epic-lane change (Epic P10-M34-E34.3) |
|---|---|---|
| Keys | `hq`, `phase`, `milestone`, `creation`, `epic_manual` | `epic_dev`, `epic_qa` |
| What moved | the **mapping table only** (`claude-opus-4-8` → `claude-opus-5`) | **rows P6 and P7**, plus their mapping rows |
| Why the difference | rows P1–P4 decide a *tier*; a same-tier successor inherits the row's justification | rows P6/P7 name the **model itself** in their Decision column, so changing it *is* a row change |
| Gate | Mapping revisit trigger (unavailability) — no new evidence required | **Change discipline** — new cited evidence required, and supplied (E33.2 Run A/B, E33.4) |

They share a file and a date and nothing else. Rows P1–P5 were untouched by
both.

## Standing findings the policy rests on

- Cost is dominated by context re-reads (48.5% weighted — report §2.1);
  parent-chat mixed sessions, not epic executions, are the largest sink
  (report §2.2). **Context-load reduction (E30.3) outranks model downgrade as
  a cost lever**; this policy deliberately does not chase savings by moving
  judgment-bearing levels off frontier models (report §3).
- Coverage caveat: this machine's harness only (G8); price weighting and its
  TTL caveat documented in report §1.

## Change discipline

Policy rows change only with new cited evidence (a new dataset capture, M31
run records, or a quality signal per G12) — never by assumption. Update this
file and `.ai-project.yml`'s `models:` block together; M31's guardrail treats
divergence between them as an error.
