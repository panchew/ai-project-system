---
artifact_type: progress_digest
artifact_version: 1.0
timestamp: 2026-07-20T20:30:00Z
issuer_chat: HQ Chat
target: Creation Chat
project_name: ai-project-system
period_covered: 2026-07-17 to 2026-07-20
---

# Progress Digest — ai-project-system (2026-07-17 to 2026-07-20)

## Phase Status

| Milestone | Status | Blocking issue |
|-----------|--------|----------------|
| P9-M30 — Token Measurement & Model-Tier Audit | ✅ | |
| P9-M31 — Dual-Mode Working Levels & Model Guardrail | ✅ | |
| P9-M32 — System Participant Canonization & Governance Hygiene | ✅ | |

**Phase P9 is closed** (merge `8044451`, tag `v7.0.0`, master `97ed5a3`, suite 363/0/0). 10 epics
across 3 milestones. All nine phases complete; no active phase. HQ independently re-verified the
closure against the repo — suite, tag, all claimed merge commits, governance versions, and both
hygiene carry-forwards (P8-GH-1, P8-GH-3) check out with no discrepancies.

## Open Decisions

1. **P10 spine — the only thing gating further work.** HQ cannot self-scope a phase; the Creation
   Chat sets the spine. Nothing else in the project is waiting on anything else. — before any P10
   work begins.
2. **Did the token-efficiency spine actually pay off, and does P10 keep pushing it?** The Post-M31
   recapture found **no measured reduction**: phase per-call median flat (169K), milestone **+11.2%**
   (129K→144K), epic **+6.4%** (76K→81K) — the wrong direction, though not attributably (sample
   churn, too few M31-scoped sessions). The design-level reduction *is* real and measured by hand
   (starter packs: epic −59%, milestone −56%, phase −52%), but `bin/measure-token-burn` **cannot
   currently verify its own reduction claims** (P9-GH-2) — no `--since` filter, and E30.3's pack
   cells are frozen pre-reduction by design. Choose: (a) P10 continues the spine and fixes the
   measurement so the claim can be proven or falsified, or (b) accept the design-level numbers and
   move the spine elsewhere. — at P10 scoping.
3. **Who owns P9-GH-1 (the merge-authorization gap)?** The E31.3 process gap — merge authorization
   given inside a child chat, bypassing the parent's Stage-2 review — was patched only in the Epic
   starter template. The same gap can still recur at Milestone→Phase and Phase→HQ. It is a
   governance-template edit outside any Phase or Milestone Chat's own adjacency, so it needs HQ to
   own it: P10 scope, or a standalone epic. — at P10 scoping.
4. **Is the ComfyUI precision investigation still wanted?** Untouched by P9 and unreported since
   2026-07-17; still a non-blocking CFO-side track. Confirm it is live, parked, or dropped. — at
   P10 scoping.

**Merge review (CFO gate):** none — no open PRs. The gate is `enabled`; nothing awaits review.

## Next Actions

1. Set the P10 spine (or confirm a deliberate pause) — Creation Chat / CFO — next session.
2. Report the ComfyUI investigation's status so it stops carrying forward unresolved — CFO — with (1).
3. Open P10 scoping and triage P9-GH-1/2/3 plus the restated deferrals into scope or explicit
   defer — HQ — after (1).

## Blocking Concerns

None. P9 closed clean: no open PRs, no pending merge-gate items, no failing tests, no unresolved
escalations. The measurement gap in Decision 2 constrains what P10 can *prove*, but blocks nothing.
