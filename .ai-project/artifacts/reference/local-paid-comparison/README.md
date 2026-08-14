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
| `protocol-correction-addendum.md` | **Pre-registered** v1 addendum — authorizes local run 2 + paid run 2 (Review Decision Findings 1/2). |
| `protocol-correction-addendum-v2.md` | **Pre-registered** v2 addendum — authorizes paid run 3 (Re-review 01 Finding 1). |
| `erratum-addendum-v1-timestamp.md` | Records the addendum v1 front-matter timestamp error (Re-review 01 Finding 2). |
| `runs/local/` | Local arm runs: run 1 (invalid: host, not container), run 2 (valid: Drivr adapter, container). |
| `runs/paid/` | Paid arm runs: run 1 (invalid: repo access), run 2 (invalid: programmatic subagent), run 3 (valid: Claude Code CLI packet-only), sealed input. |
| `scores.md` | Scored valid pair (local run 2 = MISS, paid run 3 = CATCH). |
| `judgment.md` | Recomputed judgment from the valid pair. |

## The material

**Task:** Fix the fleet registry's validation section to correctly distinguish fleet-only warning totals from raw totals that include non-fleet configs.

**Ground truth:** The fix was delivered in E38.3's Stage-2 rework (commit 927b7fa on milestone/M38). The correct totals are derivable from the pre-fix registry itself.

**Why this material:** It is code-shaped (YAML data + Python test), its ground truth is knowable from a committed fix, and the pre-fix state is reconstructable from git without revealing the answer.

## Protocol history and the resubmissions

### Original submission
- **Paid run 1** violated the packet-only condition: it had repository access and read the
  committed answer. **INVALID — retrieval, not capability.**
- **Local run 1** ran directly on the host, not through the registered ContainerEnvironment.
  **INVALID (environment mismatch).**

### Re-review 01 (Review Decision 2026-08-14T19:06:56Z)
The first correction addendum (v1) authorized one replacement per invalid arm. Valid pair
was local run 2 (Drivr adapter, container) = MISS and paid run 2 (programmatic subagent,
packet-only) = CATCH. **Paid run 2 was rejected** by Re-review 01 (Review Decision
2026-08-14T20:22:53Z) as a programmatic subagent with instructed-not-sandboxed isolation.

### Re-review 02 (current — Review Decision 2026-08-14T20:22:53Z)
The second correction addendum (v2) classified paid run 2 INVALID, authorized exactly one
**paid run 3** as a genuinely fresh, human-operated manual packet-only session, and committed
the sealed input before the run.

**Valid pair (scored):** local run 2 (Drivr OpenCodeAdapter, ContainerEnvironment) = MISS;
paid run 3 (Claude Code CLI, model claude-opus-5, packet-only, no filesystem/shell/search
tools) = CATCH. See `scores.md` and `judgment.md`.

## Commit order proof

**Current branch IDs** (post-rebase; the pre-rebase IDs are labelled in parentheses where
they carry the original timestamp proof):

| Commit | Time (commit) | Contents |
|---|---|---|
| `628594b` (was `fc8d008`) | 2026-08-12 | **rubric + packet + README** — before any run |
| `1b5c2e1` (was `8f0edd9`) | 2026-08-12 | run 1 outputs + original scoring + original Delivery Notice |
| `c418efd` (was `0acf32b`) | 2026-08-14 13:14:32 -0600 | **protocol-correction-addendum v1** — before run 2 (timestamp erratum: front matter said 19:30:00Z) |
| `e567293` (was `f251b0d`) | 2026-08-14 | run 2 outputs + resubmission scoring/judgment |
| `2b0e884` | 2026-08-14 14:35:35 -0600 | **protocol-correction-addendum v2 + sealed input** — before paid run 3 |
| `0e736f0` | 2026-08-14 | paid run 3 outputs + re-review-01 scoring/judgment + erratum |

The sealed input (`runs/paid/sealed-input-run-3.txt`) is 42,875 bytes, MD5
`450dcfb78800f13ff39cabf4bcf1907f`, byte-for-byte identical to the input the reviewer
independently recovered for run 2.
