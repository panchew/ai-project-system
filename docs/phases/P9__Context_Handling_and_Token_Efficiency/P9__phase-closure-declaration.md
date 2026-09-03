---
type: phase-closure-declaration
phase: P9
name: Context Handling and Token Efficiency
status: closed
merge_commit: 8044451
tag: v7.0.0
master_head_at_closure: 8044451
closed_date: 2026-07-20
closed_by: Phase Chat (P9)
acceptance_model: SN-13 default-accept (each milestone's delivery — M30, M31, M32 — independently re-verified by this Phase Chat before consolidation, not accepted on the closure declaration's word alone; no Review Decision artifact issued at any gate); CFO authorized all three milestone-consolidation merges (#135, #144, #145) and the phase-delivery merge (#134), PSG §5C Step 6/7
---

# Phase P9 Closure Declaration

**Phase P9 — Context Handling and Token Efficiency is closed.**

Merge commit `8044451` landed on `master`. Tagged `v7.0.0`.

This is the **fourth phase closed through the canonical PSG §5C sequence** (P6 was first, P7
second, P8 third). P9's spine was context handling / token efficiency: the original
model-tier assumption — local models only at the Epic level, frontier everywhere else —
failed in practice, exhausting the CFO's premium token quota and leaving them without
frontier reasoning when it mattered. P9 replaced that assumption with evidence, gave the
working levels a real dual-mode switch guarded on both sides, and canonized a governance
participant that had already been running in the field for weeks.

---

## Delivery Record

| Milestone | Epics | Scope / gaps closed | PR | Merge commit |
|-----------|-------|---------------------|-----|--------------|
| M30 — Token Measurement & Model-Tier Audit | E30.1–E30.4 (4) | Real per-level/per-task-type token dataset with explicit gap records (G1–G14); frontier-vs-local policy (`model-routing-policy.md`, rows P1–P7); `.ai-project.yml` `models:` refreshed off the measured mix; evidence-sized context-scoping standard; AOG §3.1.1 reference-first handoff rule (SN-23, added mid-flight as E30.4 via phase spec v1.1.0) | #135 | `1711a97` |
| M31 — Dual-Mode Working Levels & Model Guardrail | E31.1–E31.3 (3) | Per-instance Execution Mode in `chat-hierarchy.md`; Creation/HQ manual-only permanently, normatively recorded; agentic paid-vs-local decision logic applying the M30 policy; `DEFAULT_MODELS` falsified-name fix; manual-mode startup guardrail refusing on mismatch at every level; Post-M31 Measurement Recapture (milestone-level, not a fourth epic) | #144 | `e1a81ea` |
| M32 — System Participant Canonization & Governance Hygiene | E32.1–E32.3 (3) | `system_request`/`system_response` schemas + out-of-hierarchy annex (`governance/systems/system-hq.md`, `chat-hierarchy.md`); normative execute-never-decide Authority Boundary (byte-identical across three surfaces); daily System Chat re-instantiation seed (`system-hq-seed.md`); P8-GH-1 (stale opt-out prose) and P8-GH-3 (vestigial phrase) reconciled, grep-clean | #145 | `d136640` |

**10 epics** across 3 milestones. **363 passed, 0 failed, 0 skipped** at closure (up from the
307-passed/0-skipped baseline at phase-open — 56 new tests added across E31.2/E31.3, none
removed, no skip introduced to route around any change).

---

## Process Record

Closure was recorded under the **SN-13 default-accept model** (PSG §11.6 / AOG §14): each
milestone's delivery was independently re-verified by this Phase Chat — live suite re-runs,
grep checks re-run personally rather than trusted from Delivery Notices or Closure
Declarations, direct inspection of the edited governance surfaces — before consolidation, at
every gate. No Review Decision artifact was issued; every milestone delivery held up clean
under independent review.

**Mid-flight amendment (SN-23, 2026-07-18).** A Creation Chat evaluation session raised a
token-economy concern: governance-mandated artifact echo (full-body chat-starter display,
copy-paste artifact transport) was obsolete against committed-file practice and the
IDE-attach workflow, and was itself a cost the M30 measurement work had just quantified. HQ
triaged it into M30 as a follow-up epic (E30.4) via phase spec **v1.1.0** (`e490394`) rather
than into M31 — the evidence requirement bound to E30.1's mechanism, which lives in M30, and
landing it before M31/M32 sessions started stopped the echo cost sooner. The Phase Chat owed
and closed a milestone-spec amendment (A1, `3d15571`) recording E30.4 in M30's own governing
document — not left as a phase-spec-only fact.

**Process gap surfaced and closed within the phase (M31).** Merge authorization for Epic
E31.3's PR (#142) was given directly inside that Epic's own chat session, bypassing the
Milestone Chat's Stage-2 review at the time of merge. The Milestone Chat performed the review
retroactively, found the delivery clean, and added a guard to
`governance/templates/epic-execution-chat-starter.md` (commit `8dbffe0`) so a future Epic
chat confirms before acting on an authorization that bypasses its parent's review. This
process gap and its fix are also recorded in this project's persistent memory
([[feedback-merge-authorization-routing]]). **Not yet extended:** the same guard pattern for
the Milestone/Phase Execution Chat Starter templates — recorded as a proposal for HQ below,
not implemented in P9 (outside this Phase Chat's own artifact-scope adjacency).

**Honest negative finding, reported plainly (M31).** The Post-M31 Measurement Recapture
re-ran `bin/measure-token-burn` unmodified and found **no reduction observed** in billed
per-call context medians — not because the M30/M31 work failed, but because the measurement
mechanism itself cannot currently answer the question cleanly (no `--since` filter against a
non-append-only session directory; E30.3's Direction B pack cells are permanently pinned
pre-reduction by their own design). This is the "no movement yet, window too short" outcome
the M31 milestone spec explicitly named as an acceptable finding, and it was recorded rather
than shaped toward a positive result.

**No scope creep.** All three milestones stayed within their planned epic boundaries except
the one HQ-triaged mid-flight addition (E30.4, above); no epic was added to M31 or M32.

---

## What P9 Delivered to `master`

**Measurement and policy (M30):**
- `bin/measure-token-burn` — real per-level, per-task-type token-burn capture from harness
  session data, with governance-corpus overhead separable and every uncapturable cell an
  explicit gap record (G1–G10) rather than a guess
- `model-routing-policy.md` (rows P1–P7) — the evidence-grounded frontier-vs-local policy
  replacing the failed local-only-at-Epic assumption
- `.ai-project.yml` `models:` refreshed to the measured mix (`remote:claude-opus-4-8` for
  hq/phase/milestone, `local:qwen2.5-coder:14b` for epic_dev/epic_qa) — the falsified
  `gpt-4o`/`claude-3-5-sonnet` entries are gone
- `context-scoping.md` — per-level context-scoping standard; measured pack reduction across
  the three Execution Chat Starter templates (epic −59%, milestone −56%, phase −52% proxy
  tokens)
- AOG §3.1.1 (v2.10.0) — the single normative reference-first artifact-handoff rule,
  replacing mandated full-body echo across 8 governance surfaces; paste retained as the
  documented repo-less fallback

**Dual mode and guardrails (M31):**
- `chat-hierarchy.md` "Execution Mode: Manual vs. Agentic" — per-instance mode declared in
  each concrete instance's own committed Execution Chat Starter; absence means manual;
  Creation Chat and HQ Chat recorded manual-only, permanently, normatively
- Agentic paid-vs-local decision logic in the epic-execution dispatch path, applying the M30
  policy; `DEFAULT_MODELS` aligned with the refreshed `models:` block; consistency-guard
  tests extended from `epic_dev`-only to all five `models:` keys plus a policy↔block
  divergence check
- `EXIT_LOCAL_UNAVAILABLE` (exit 5) preflight in `bin/run-dev-agent`, and a matching
  escalation path in the dispatch handler, for GPU contention with ComfyUI
- Manual-mode startup guardrail: two new manual-only `models:` keys (`creation`,
  `epic_manual`); verify-and-refuse instruction on all five manual-chat template surfaces
  (the three Execution Chat Starters, `hq-chat-opener.md`, `genesis.md`/`seed.md`); real
  mismatch-refusal evidence from this session's own live model

**System participant and hygiene (M32):**
- `governance/systems/system-hq.md` — canonizes System HQ (field-adopted 2026-07-16, SN-21):
  the `system_request`/`system_response` schemas, storage/naming conventions, and status
  vocabulary matching field usage; the normative execute-never-decide Authority Boundary
- `chat-hierarchy.md` — an explicit out-of-hierarchy annex placing System HQ as a
  cross-project, one-desk-per-machine participant, not a fifth per-project level
- `governance/systems/system-hq-seed.md` — the daily System Chat re-instantiation seed,
  analogous to Creation Chat's Genesis/seed pattern
- AOG §17.5 and `governance/guides/visual-artifacts.md` corrected — no governance surface
  describes this repo as opted out of `visual_artifacts` (P8-GH-1 closed)
- Six pre-P9 planning documents purged of the vestigial "Phase Delivery Notice" phrase,
  preserving the P8 closure declaration's own intentional carry-forward record unchanged
  (P8-GH-3 closed)

**Governance versions at delivery:** PSG v2.3.0 (unchanged), AOG v2.10.0, yml-spec v2.5.0,
Artifact Communication Protocol v1.4.0, framework v7.0.0.

---

## Outstanding Carry-Forwards Restated (not this phase's own work)

Per this phase's own acceptance criteria (items 7–8), restated here rather than silently
dropped:

> **P8-GH-2 — Machine-local hosting limitation (Low).** The storage backend provisioned to
> complete E29.3's bindings is local only. **Status unchanged: deferred**, on its recorded
> trigger (revisit only if cloud-reachable hosting is ever actually needed). Source record:
> `docs/phases/P8__Visual_Artifacts_Activation/P8__phase-closure-declaration.md`,
> Carry-Forward row P8-GH-2 — untouched by P9.

> **ComfyUI precision investigation (SN-20 Carry-Over 3).** **Status unchanged: non-blocking,
> CFO-side track** (P9 phase spec, "Out of Scope"). Nothing in P9 touched, blocked on, or
> resolved it. If the investigation lands, its outcome routes through Creation Chat / HQ as
> new input, not into a closed phase.

---

## Visual Bindings

No phase-level visual was generated for P9's closure; each milestone's own Structural
proposed-track diagram is recorded in its respective milestone spec
(`P9-M30__milestone-spec.md`, `P9-M31__milestone-spec.md`, `P9-M32__milestone-spec.md`).

---

## Carry-Forward to P10

| ID | Title | Priority |
|----|-------|----------|
| P9-GH-1 | **Merge-authorization-routing guard is patched at Epic level only.** The E31.3 process gap (merge authorization given directly in a child chat, bypassing the parent's Stage-2 review) was fixed in `governance/templates/epic-execution-chat-starter.md` (`8dbffe0`). The same class of gap could recur at Milestone→Phase or Phase→HQ; the Milestone/Phase Execution Chat Starter templates were not patched. Recorded as a proposal for HQ, not implemented in P9 — extending it is a governance-template edit outside any single Phase/Milestone Chat's own artifact-scope adjacency. | Medium |
| P9-GH-2 | **`bin/measure-token-burn` cannot currently verify its own reduction claims.** The Post-M31 Measurement Recapture found the mechanism has no `--since`/time-window filter (the harness session directory is not append-only — sessions rotate out), and E30.3's Direction B pack cells are permanently pinned to the pre-reduction file set by design, so a rerun can never show that specific reduction. Any future recapture needs either a mechanism fix (a `--since` flag or a stable session-ID ledger) or a fresh, separately committed pack measurement in `context-scoping.md`'s own style. Recorded in `.ai-project/artifacts/reference/token-measurement/post-m31-recapture.md` §7; not fixed in P9 per that epic's own hard constraint (mechanism stays unmodified). | Low |
| P9-GH-3 | **Within-session task segmentation in `bin/measure-token-burn`.** Named in the E30.1 audit report §8 as a measurement-precision improvement (mixed parent-chat sessions currently attribute at the whole-session level, not per task). Unowned future work, not scheduled to any P9 milestone. | Low |
| Issue #126 | **Local-LLM agentic execution GPU-exclusivity / scheduling.** M31's agentic paid-vs-local logic is GPU-contention-*aware* (an `EXIT_LOCAL_UNAVAILABLE` preflight and escalation path exist) but does not *resolve* scheduling between Ollama and ComfyUI — unchanged from its P8 carry-forward status. | — |
| SN-20 Carry-Over 2 | **The spin-off "software factory" project** — unchanged, future Creation Chat item. | — |
| SN-21 carry-overs | **MCP bridge write path** (ai-project-system-mcp roadmap territory) and **scheduled request-sweep/SLA cadence** (future triage if volume grows) — both explicitly out of P9's M32 scope, unchanged. | — |

---

## Sign-Off

Phase P9 is closed. At `v7.0.0`, the AI Project System replaced a policy written before
evidence with a policy derived from real, captured data; gave its own working levels a
genuine manual/agentic switch instead of a hardcoded assumption, guarded on both the paid and
the manual side; and wrote down a governance participant that had already been quietly
running the CFO's machine for a month. Nine phases, 99 epics, 32 milestones — and, as with P8,
the most valuable delivery here is not a clean pass but an honest number: the recapture found
no measured reduction yet, and said so plainly rather than shading the result.
