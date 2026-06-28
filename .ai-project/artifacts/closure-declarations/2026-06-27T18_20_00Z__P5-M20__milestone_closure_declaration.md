---
type: milestone-closure-declaration
milestone: M20
status: complete
completion_date: 2026-06-27
declared_by: Milestone Chat (P5-M20 — Governance Process Hardening)
issued_to: Phase Chat (P5 — Process Hardening and Visual Artifacts)
is_final_milestone: false
---

# MILESTONE CLOSURE DECLARATION — M20

Milestone **P5-M20 — Governance Process Hardening** is hereby declared **COMPLETE**. All five
epics (E20.1–E20.5) closing governance gaps GH-1, GH-2, GH-3, GH-8, and GH-9 have been executed,
independently reviewed, accepted, and merged to `milestone/M20` (HEAD `86f4cad`), with the full
test suite green (**232 passed**).

## Completion Verification

✅ **E20.1 — Prerequisite git-tracking verification (GH-1)** — merged to `milestone/M20`
(PR #83, merge `9808885`). Review Decision `2026-06-25T20:00Z`, Merge Authorization `20:05Z`.

✅ **E20.2 — Working-tree isolation convention (GH-2)** — merged (PR #84, merge `4e1279a`).
Review Decision `2026-06-25T20:30Z`, Merge Authorization `20:35Z`. Cleared the E20.1 lint
carry-over (suite returned to green).

✅ **E20.3 — Scope direction protocol (GH-3)** — merged (PR #85, merge `cd3490a`). Review
Decision `2026-06-27T15:00Z`, Merge Authorization `15:05Z`. Ratified rule verified verbatim.

✅ **E20.4 — Artifact scope adjacency (GH-8)** — merged (PR #86, merge `5b61260`). Review
Decision `2026-06-27T17:00Z`, Merge Authorization `17:05Z`. SN-12a table transcribed verbatim.

✅ **E20.5 — Hierarchical communication protocol (GH-9)** — merged (PR #87, merge `051b8c2`).
Review Decision `2026-06-27T18:00Z`, Merge Authorization `18:05Z`. Four SN-12b decisions stated.

Verified on `milestone/M20` (HEAD `86f4cad`): all five epic merge commits present, every Epic
spec / re-issued (or freshly authored) starter / Delivery Notice committed, full suite green
(232 passed, no regression).

## Milestone Definition of Done — all items satisfied

- ✅ E20.1, E20.2, E20.3, E20.4, E20.5 each meet their Definition of Done (recorded in their
  Review Decisions and Epic Closure Notices).
- ✅ All five epic branches merged to `milestone/M20` (`--no-ff`).
- ✅ Full test suite passes on `milestone/M20` (232/232).
- ✅ This Milestone Closure Declaration produced.

## Milestone Acceptance Criteria — all satisfied

1. ✅ **(GH-1)** Both starter templates mandate `git ls-files --error-unmatch <path>`
   verification, with inline rationale, asserted by a passing test
   (`tests/test_template_prerequisite_wording.py`).
2. ✅ **(GH-2)** `chat-hierarchy.md` has a "Working-Tree Isolation" section and AOG §3.8
   references it. (The dogfooded lint false-positive on the planned `milestone/M21` example was
   fixed via `PLANNED_MILESTONE_LOOKAHEAD` in `tests/test_starter_lint.py`.)
3. ✅ **(GH-3)** `chat-hierarchy.md` has a "Scope Direction Protocol" section with the
   HQ-ratified rule **verbatim**, the P0 exception, and a rationale; AOG §3.9 references it.
4. ✅ **(GH-8)** The adjacency rule is in both starter templates' Critical Rules, in AOG §3.6
   and §3.7, and as the SN-12a table in `chat-hierarchy.md` ("Artifact Scope Adjacency").
5. ✅ **(GH-9)** The hierarchical communication protocol is in `chat-hierarchy.md`
   ("Communication Protocol"), AOG §3.10, and PSG §13D, with amendment-issuing guidance in both
   starter templates.
6. ✅ Full test suite passes (232/232).

## Milestone Summary

M20 hardens the governance **process itself** before further P5 feature work (M21 adoption
clarity, M22 visual artifacts). Five latent defects that produced silent, hard-to-detect
failures are now closed as surgical documentation/wording changes plus one guard test:
git-tracked prerequisite verification (GH-1), one-worktree-per-active-chat isolation (GH-2), a
mandatory auditable scope-direction channel (GH-3), artifact scope adjacency (GH-8), and a
defined hierarchical communication protocol (GH-9).

**M20 dogfooded its own fixes:** every M20 prerequisite was verified with
`git ls-files --error-unmatch` (GH-1); a live shared-working-tree collision recurred during
E20.1 review and is cited as E20.2's worked example (GH-2); the Stage-1 authority conflict was
escalated up rather than self-resolved (GH-3); and the Milestone Chat authored E20.4/E20.5
fresh (no Phase drafts), the GH-8 adjacency rule in action.

## Process Notes for Phase Chat (non-blocking)

1. **Retained remote epic branches.** `origin/epic/P5-M20-E20.1` … `…E20.5` were kept after
   merge — the auto-mode policy blocked remote-branch deletion as not explicitly authorized.
   They can be deleted on owner go-ahead; none affects milestone acceptance.
2. **E20.2 scope addition (already ratified).** The lint false-positive fix folded into E20.2
   was authorized by the Phase Chat on 2026-06-25; the milestone spec's E20.2 detail may
   optionally be amended (a parent-owned artifact) to record it.
3. **Three E20.1–E20.3 starters were Phase-provided drafts** (the original GH-8 instance),
   retained per HQ Option B and re-issued by the Milestone Chat under its own authority.

None affects milestone acceptance.

## Required Action: Consolidation

M20 is **not** the final P5 milestone (M21, M22 follow).

1. Pull Request: `milestone/M20` → `phase/P5` (opened by this Milestone Chat).
2. Phase Chat (P5) reviews and authorizes the milestone-level merge.
3. Merge PR (milestone consolidation commit) — M20 lands on `phase/P5`.
4. Phase Chat proceeds with the next P5 milestone (M21).

---

**Declared by the Milestone Chat (P5-M20). Awaiting Phase Chat milestone-level acceptance of the
`milestone/M20 → phase/P5` consolidation PR.**
