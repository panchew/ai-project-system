---
project: ai-project-system
phase: P11
milestone: M38
epic: E38.6
type: reference
status: complete
last_updated: 2026-08-14
---

# Local/Paid Controlled Comparison — evidence directory

Evidence for Epic **P11-M38-E38.6**. Runs the same code-shaped task agentic/local through E38.2's adapter (qwen3-coder:30b) and manual/paid at models.epic_manual (remote:claude-opus-5), on blinded material with a pre-registered rubric.

## Method

Adopts E35.5's blinding discipline: blinded packet with audit header, pre-registered rubric committed before any run, every run reported.

The blinding addresses the contamination risk unique to this Epic: a local arm with repository access can find the delivered answer in git. The local arm therefore runs in an **isolated workspace** — a temporary directory containing only the pre-fix files, with no `.git` directory and no post-fix commits. The paid arm is intended to receive **the packet content only** — no repository, no git, no search.

## Contents

| Path | What it is |
|---|---|
| `rubric.md` | The **pre-registered** scoring rubric. Committed with the packet, before any run. |
| `packets/packet-1-registry-validation.md` | Blinded comparison packet — fleet registry validation fix. |
| `protocol-correction-addendum.md` | **Pre-registered** authorization for replacement runs (Review Decision Findings 1/2). |
| `runs/local/` | Local arm runs: run 1 (invalid: host, not container), run 2 (valid: Drivr adapter, container). |
| `runs/paid/` | Paid arm runs: run 1 (invalid: repo access), run 2 (valid: packet-only). |
| `scores.md` | Scored valid pair (local run 2 = MISS, paid run 2 = CATCH). |
| `judgment.md` | Recomputed judgment from the valid pair. |

## The material

**Task:** Fix the fleet registry's validation section to correctly distinguish fleet-only warning totals from raw totals that include non-fleet configs.

**Ground truth:** The fix was delivered in E38.3's Stage-2 rework (commit 927b7fa on milestone/M38). The correct totals are derivable from the pre-fix registry itself.

**Why this material:** It is code-shaped (YAML data + Python test), its ground truth is knowable from a committed fix, and the pre-fix state is reconstructable from git without revealing the answer.

## Protocol history and the resubmission

The original submission had two invalid runs. The Milestone Chat rejected it (Review Decision
2026-08-14T19:06:56Z, REJECT/action: rework):

- **Paid run 1** violated the packet-only condition: it had repository access and read the
  committed answer. **INVALID — retrieval, not capability.**
- **Local run 1** ran directly on the host, not through the registered ContainerEnvironment.
  **INVALID (environment mismatch).**

The `protocol-correction-addendum.md` (committed **before** any replacement run) authorized
exactly one replacement for each, froze the replacement conditions, and required both
original runs be preserved as invalid trials.

**Valid pair (scored):** local run 2 (Drivr OpenCodeAdapter, ContainerEnvironment) = MISS;
paid run 2 (fresh packet-only session, non-contaminated) = CATCH. See `scores.md` and
`judgment.md`.

## Commit order proof

| Commit | Time | Contents |
|---|---|---|
| `fc8d008` | 2026-08-12 | **rubric + packet + README** — before any run |
| `8f0edd9` | 2026-08-12 | run 1 outputs + original scoring + original Delivery Notice |
| `0acf32b` | 2026-08-14 | **protocol-correction-addendum** — before any replacement run |
| `f251b0d` | 2026-08-14 | run 2 outputs + resubmission scoring/judgment |
