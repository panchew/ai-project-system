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
| P6 | epic × dev-agent lane (`epic_dev`) | **`local:qwen2.5-coder:14b`** — the local lane M31's runner uses when the P5 experiment runs | The only local model with any captured run evidence (dataset §5: completed run, 404 output tokens); tool-calling-capable per the E26.2 finding that moved this default (yml-spec changelog 2.2.0 — operational history, labeled as such). | Single-run evidence (G9, G12) | Additional M31 local runs |
| P7 | epic × qa-agent lane (`epic_qa`) | **`local:qwen2.5-coder:14b`** | The QA role has *zero* captured runs in either spend kind (**G11** — report §6); the prior `7b` value was as unmeasured as the falsified remote names. Gap-grounded interim default: the one local model with any run evidence, per the report §7.2 standard. | Gap-grounded (G11); single-run adjacent evidence (G9) | First M31 QA-role run |

## Mapping to `.ai-project.yml` `models:` (the M31 guardrail target)

| key | value | policy row |
|---|---|---|
| `hq` | `remote:claude-opus-4-8` | P2 (paid frontier; value = measured workhorse at hq — report §2.3) |
| `phase` | `remote:claude-opus-4-8` | P3 (value = measured workhorse at phase — report §2.3) |
| `milestone` | `remote:claude-opus-4-8` | P4 (value = measured workhorse at milestone — report §2.3) |
| `epic_dev` | `local:qwen2.5-coder:14b` | P6 |
| `epic_qa` | `local:qwen2.5-coder:14b` | P7 |

**Why claude-opus-4-8 for the remote keys:** it carried 49.6% of all measured
spend and the plurality of spend at each of hq, phase, and milestone (report
§2.3, findings 4–5) — it is the model that demonstrably did this governance
work in the window. Choosing among the four measured models involves judgment
(no quality measure was captured — G12); choosing a model *outside* the
measured mix would repeat the original fiction. Neither `gpt-4o` nor
`claude-3-5-sonnet` ran once in 72 sessions (dataset §2).

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
