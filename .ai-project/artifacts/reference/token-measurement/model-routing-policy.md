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
| P4 | milestone × all | **Paid frontier** | Largest spend share (37% — report §2.2) *and* the level where Stage-2 accept authority lives; same mixed-bucket shape as phase (report §3; G4/G7). | Mixed-bucket attribution (G4, G7) | Same as P3 |
| P5 | epic × execution | **Paid frontier today; designated local-offload experiment (M31)** | Highest-volume attributed cell, bounded and spec-driven (38 sessions, median $2.92 — report §2.2/§3): the best offload candidate *by shape*. Local capability unproven: one measured local run, 404 output tokens (dataset §5), input unmeasured (G9), no quality measure (G12). Paid remains the default until M31 dual-mode produces run evidence. | Local evidence thin (G9, G12) | M31 dual-mode runs at epic level |
| P6 | epic × dev-agent lane (`epic_dev`) | **`local:qwen3-coder:30b`** — the local lane M31's runner uses when the P5 experiment runs | **Row changed on new cited evidence (P10-M33, applied P10-M34-E34.3).** The prior value `qwen2.5-coder:14b` was *falsified by running it*, not by argument: E33.2 **Run A** dispatched the then-configured `epic_dev`/`epic_qa` model against a real epic and returned **exit 0 having done nothing** — 0 tool rounds, 0 files changed, SN-3 markdown-plan mode. **Run B** — same epic, same Ollama runtime, `qwen3-coder:30b` — produced mergeable work; **E33.4** then ran a second real epic (`home_finance`) on the same model to complete, green work (275 examples, 0 failures). The model was the lever; the runtime was never the problem. Loadability envelope, recorded honestly: Q4_K_M/18.6 GB **exceeds** the proving box's 16 GB VRAM and **partially offloads to RAM** (12.9 GB VRAM / 21.4 GB total), running ~9.4 tok/s against the 14b's 12.2 on the same epic — slower, but it finishes. That is the ratified trade. Cited: `docs/phases/P10__Fleet_Adoption_and_Local_Inference_Proving/P10-M33-E33.2__runtime-decision.md`; `agentic-runs/P10-M33-E33.2/run-record.md`; `agentic-runs/P10-M33-E33.4/run-record.md`. | Two real epics on the new value, one comparative same-runtime pair; **no quality signal captured (G12 still open)**; input-token measurement gap (G9) unchanged. Exit codes proven unreliable in *both* directions on this stack (E33.2 Run A: exit 0, zero work; E33.4: exit 2, complete work) — verification reads the transcript and the target repo, never the exit status | A third real agentic epic on the raised tier disagreeing with these two, the first captured **quality** signal (G12), or a loadability change on the execution host (the partial RAM offload is the standing fragility) |
| P7 | epic × qa-agent lane (`epic_qa`) | **`local:qwen3-coder:30b`** | **Referent updated; the reasoning is unchanged, and that is deliberate.** The QA role still has **zero** captured runs of its own — **G11 remains open**. M33 produced no isolated QA-role run because the runner dispatches dev and QA from one model in practice (E33.2 run record: *"Run A is the configured `epic_dev`/`epic_qa` model"*), so E33.2/E33.4 gave the **dev** lane its evidence, not this one. This row therefore does **not** move on new QA-lane evidence — none exists. It moves on exactly the reasoning it already carried, *gap-grounded interim default: the one local model with any run evidence* (report §7.2 standard), with the referent updated from `qwen2.5-coder:14b` — which E33.2 Run A falsified — to `qwen3-coder:30b`. No QA-lane evidence is claimed here. | Gap-grounded (**G11 open — zero captured QA-role runs**); evidence is dev-lane adjacent only (G9, G12) | The first **isolated QA-role** run — G11's own closure condition, still unfired; a dispatch change that gives the QA lane a separate model would fire it sooner |

## Mapping to `.ai-project.yml` `models:` (the M31 guardrail target)

| key | value | policy row |
|---|---|---|
| `hq` | `remote:claude-opus-5` | P2 (paid frontier; value = measured workhorse at hq — report §2.3) |
| `phase` | `remote:claude-opus-5` | P3 (value = measured workhorse at phase — report §2.3) |
| `milestone` | `remote:claude-opus-5` | P4 (value = measured workhorse at milestone — report §2.3) |
| `epic_dev` | `local:qwen3-coder:30b` | P6 |
| `epic_qa` | `local:qwen3-coder:30b` | P7 |

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
