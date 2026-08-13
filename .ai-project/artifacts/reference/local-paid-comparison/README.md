---
project: ai-project-system
phase: P11
milestone: M38
epic: E38.6
type: reference
status: pre-registered
last_updated: 2026-08-12
---

# Local/Paid Controlled Comparison — evidence directory

Evidence for Epic **P11-M38-E38.6**. Runs the same code-shaped task agentic/local through E38.2's adapter (qwen3-coder:30b) and manual/paid at models.epic_manual (remote:claude-opus-5), on blinded material with a pre-registered rubric.

## Method

Adopts E35.5's blinding discipline: blinded packet with audit header, pre-registered rubric committed before any run, every run reported.

The blinding addresses the contamination risk unique to this Epic: a local arm with repository access can find the delivered answer in git. The local arm therefore runs in an **isolated workspace** — a temporary directory containing only the pre-fix files, with no `.git` directory and no post-fix commits. The paid arm receives the same material inline.

## Contents

| Path | What it is |
|---|---|
| `rubric.md` | The **pre-registered** scoring rubric. Committed with the packet, before any run. |
| `packets/packet-1-registry-validation.md` | Blinded comparison packet — fleet registry validation fix. |
| `runs/local/` | Raw outputs from the local arm (agentic, qwen3-coder:30b, through drivr's adapter). |
| `runs/paid/` | Raw outputs from the paid arm (manual, claude-opus-5). |

## The material

**Task:** Fix the fleet registry's validation section to correctly distinguish fleet-only warning totals from raw totals that include non-fleet configs.

**Ground truth:** The fix was delivered in E38.3's Stage-2 rework (commit 927b7fa on milestone/M38). The correct totals are derivable from the pre-fix registry itself.

**Why this material:** It is code-shaped (YAML data + Python test), its ground truth is knowable from a committed fix, and the pre-fix state is reconstructable from git without revealing the answer.

## Commit order proof

| Commit | Time | Contents |
|---|---|---|
| **this commit** | 2026-08-12 | **rubric + packet + README** — before any model run |
| *(subsequent commit)* | 2026-08-12 | run outputs, scores, Delivery Notice |
