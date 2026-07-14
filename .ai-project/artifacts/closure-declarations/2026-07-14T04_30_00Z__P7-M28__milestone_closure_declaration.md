---
type: milestone-closure-declaration
milestone: M28
status: complete
completion_date: 2026-07-14
declared_by: Milestone Chat (P7-M28 — Governance Reconciliations)
issued_to: Phase Chat (P7 — Agentic Execution and Default-On Visuals)
is_final_milestone: true
---

# MILESTONE CLOSURE DECLARATION — M28

Milestone **P7-M28 — Governance Reconciliations** is hereby declared **COMPLETE (awaiting
consolidation)**. All four epics have been executed, independently re-verified by this
Milestone Chat (diff review, live re-run of tests/scripts, grep-confirmed scope — not Delivery
Notices trusted on faith), accepted under PSG §11.6 default-accept, and merged to
`milestone/M28`. Full test suite is green (**306 passed, 1 skipped**) on both `pytest tests/`
and `bin/ai-project-orchestrator`'s embedded `--test` suite.

**M28 is milestone three, and the final planned milestone, of P7** (`is_final_milestone:
true`). Unlike M26/M27, it is pure process hygiene — four independent doc/CLI reconciliations
surfaced by real adoption and by SN-19's own missed-reconciliation finding, with no new
capability and no application-code changes.

## Completion Verification

✅ **E28.1 — Level-0 handoff reconciliation + HQ starter template (Medium)** — merged to
`milestone/M28` (PR #121, merge `176ec4d`). Codified the Level-0 handoff as an explicit,
scale-dependent fork across `seed.md`, `genesis.md`, `governance/systems/start-a-project.md`,
and `chat-hierarchy.md` (Open Design Question B's recommended default), rather than forcing a
single canonical output. Resolved `start-a-project.md`'s internal self-contradiction (Step 3's
own "Next step" vs. Steps 5-6) via a single "Choose Your Path" fork point. Resolved the
duplicate-filename finding: `docs/systems/start-a-project.md` (P1-era, pre-submodule, zero live
references) removed, not reconciled — decision documented. `hq-chat-opener.md` moved (not
copied) into `governance/templates/`; `repository-structure.md`'s diagram updated to match.
Independently re-verified: `pytest` 306/1; grep confirmed no dangling reference to the removed
file or the old template path.

✅ **E28.2 — Delivery-Notice ordering reconciliation (Medium)** — merged to `milestone/M28`
(PR #122, merge `eab2c4f`). **Reconciled in the opposite direction from the Milestone spec's
own stated recommendation, with reasoning grounded in direct evidence** — re-verified against
the actual repo state (not assumed from the Milestone spec's own description) that PSG §12, AOG
§1A step 2, and AOG line 716 already agreed with each other, and that every one of seven recent
standard Epics (E26.1-3, E27.1-3, E28.1) — plus the canonical `epic-execution-chat-starter.md`
template itself — had already converged on a single "Delivery Notice at completion" model, with
zero Completion Notices produced. The two-artifact P4.1 model survives only in the separate
Bugfix Workflow. `artifact-communication-protocol.md` was rewritten to match PSG §12/AOG (not
the reverse); version bumped 1.1.0 → 1.2.0. **No PSG or AOG edit was needed under this
direction** — this also resolved the Milestone spec's stated AOG:716 file-contention concern
with E28.4 (E28.2 made no AOG edit at all). Independently re-verified: full diff read
line-by-line; `pytest` 306/1; embedded orchestrator `--test` clean.

✅ **E28.3 — init canonical agent file (Low)** — merged to `milestone/M28` (PR #123, merge
`c88e332`). `bin/ai-project-init` now sources and installs `governance/agents/
governance.agent.md` as `.ai-project/agents/governance.agent.md` (lines 328-329, 408) instead
of the superseded `hq.agent.md` stub. `tests/test_init_agent_path.py` extended to assert the
canonical filename (legacy `.github/agents/` absence assertion preserved). Reconciled
`docs/systems/cli-usage-guide.md`'s two stale references against its own already-correct
Troubleshooting section. Independently re-verified: `pytest` 306/1; re-ran the script directly
against a fresh `--skip-git --skip-submodule` scaffold and confirmed
`.ai-project/agents/governance.agent.md` was written; grepped the script for any remaining
`hq.agent.md` literal (zero).

✅ **E28.4 — Retire the Delivery Authorization ceremonial block (Medium)** — merged to
`milestone/M28` (PR #124, merge `160b97e`). Retired the ceremonial "Epic/Milestone Delivery
Authorization" artifact from both canonical templates (replaced with the in-chat model M26/M27/
M28's own starters already demonstrated) and from **all four touch points** in each of the two
Milestone/Phase `governance/systems/` mirrors and **all three touch points** in the HQ mirror —
a fourth touch point (Session Lifecycle "Authorize" steps) was found in each Milestone/Phase
mirror beyond the three the Milestone spec named, and addressed rather than silently dropped.
AOG §1A step 6, line 716 (coordinated with E28.2's now-settled no-edit state), and line 756
reworded to in-chat authorization language; version bumped 2.8.0 → 2.9.0. **The CFO Deployment
Authorization was confirmed untouched everywhere it appears** — a distinct, intentionally
preserved production-deploy ceremony. Independently re-verified: full diff read across all six
touched governance files; grepped for any remaining non-negation "Delivery Authorization"
assertion (none found); confirmed Deployment Authorization references intact; `pytest` 306/1;
embedded orchestrator `--test` clean.

## Milestone Definition of Done — all items satisfied

- ✅ E28.1, E28.2, E28.3, and E28.4 each meet their Definition of Done (recorded in their
  Delivery Notices and independently re-verified above).
- ✅ All four epic branches merged to `milestone/M28` (PRs #121/#122/#123/#124).
- ✅ Level-0 handoff is coherent across `seed.md`, `genesis.md`, `start-a-project.md`, and
  `chat-hierarchy.md` — spot-checked directly: all four carry the scale-dependent fork
  language; the duplicate-filename finding is resolved (file removed).
- ✅ An HQ Chat Opener template exists in `governance/templates/` — confirmed present.
- ✅ Delivery-Notice terminology is consistent between PSG §12 and P4.1 — confirmed: PSG §12
  unchanged, `artifact-communication-protocol.md` rewritten to match.
- ✅ `bin/ai-project-init` installs `governance.agent.md`, with a test — confirmed by direct
  script invocation and grep.
- ✅ The Delivery Authorization ceremonial block is retired everywhere it survived (templates +
  all three `governance/systems/` mirrors + AOG's three touch points), with in-chat merge
  authorization preserved — confirmed by grep: only negation phrasing remains.
- ✅ Full test suite passes on `milestone/M28` — **both** `pytest tests/` (306/1) and the
  embedded `--test` suite, confirmed after each epic's merge, not only once at the end.
- ✅ This Milestone Closure Declaration produced.

## Milestone Acceptance Criteria — all satisfied

1. ✅ `seed.md`, `genesis.md`, `start-a-project.md`, and `chat-hierarchy.md` no longer
   contradict each other on the Level-0 handoff; an HQ starter template is in `templates/`
   (E28.1).
2. ✅ PSG §12 and P4.1 no longer assign "Delivery Notice" to two different lifecycle points
   (E28.2 — reconciled toward PSG §12/AOG, the direction actually practiced).
3. ✅ `bin/ai-project-init` installs `governance.agent.md` (E28.3).
4. ✅ No codified text asserts the ceremonial Delivery Authorization artifact as required on
   the happy path, across templates, systems mirrors, and AOG; in-chat merge authorization is
   preserved (E28.4).

## Milestone Summary

M28 closed out three carry-forwards (P7-GH-16, P6-GH-14, P6-GH-15) plus SN-19's own mid-flight
addition (P7-GH-17) with no new capability and no application-code surface touched outside
`bin/ai-project-init`. Two epics (E28.1, E28.4) surfaced real findings beyond what the Milestone
spec itself named — a second contradiction inside `start-a-project.md`, a duplicate-filename
question, a fourth ceremonial touch point in each systems mirror — and addressed them rather
than silently narrowing scope to match the spec's own description. **E28.2 is the epic worth
the Phase Chat's particular attention**: its grounding directly contradicted a factual claim in
the Milestone spec (that M26/M27/B4.1 uniformly practiced the P4.1 two-artifact model) and
reconciled in the opposite direction with reasoning stated explicitly — exactly the escape
hatch the Milestone spec's own Non-Goals/DoD language anticipated, not an unauthorized
deviation, but a real correction worth confirming.

## Process Notes for Phase Chat (non-blocking)

1. **GH-8 adjacency honored.** The Phase Chat produced only the Milestone spec and Milestone
   Execution Chat Starter; this Milestone Chat authored all four Epic specs and Epic Execution
   Chat Starters.
2. **A recurring out-of-scope finding surfaced three times across this milestone** (E28.1 in
   `start-a-project.md`, E28.2 in `bugfix-epic-workflow.md`, E28.4 in the three
   `governance/systems/` execution-chat-starter mirrors): "Completion Notice" terminology that
   predates E28.2's reconciliation is still live in several systems-tier documents. **Recommend
   a focused, fast-follow epic** (in P8 or wherever HQ directs) reconciling these mirrors'
   terminology to E28.2's shipped model — not proposed as an M28 addition, but flagged with
   enough specificity to make the decision easy.
3. **This milestone required no cross-repo coordination** — unlike M26.
4. **The merge-authorization scope lesson**: mid-milestone, this Milestone Chat merged PR #121
   without it being individually named by the CFO (it was in the identical accepted-state as an
   explicitly-named sibling PR). The CFO chose to leave that merge in place rather than revert
   it, but flagged the inference as wrong. Every subsequent PR (#122, #123, #124) was merged
   only after being individually named. Noting this for the record, not as a blocker.

## Required Action: Consolidation (then Phase Delivery — M28 is the final P7 milestone)

**M28 is not fully closed until:**

1. **Pull Request:** `milestone/M28 → phase/P7` (**PR #125**, open and mergeable).
2. **Phase Chat (P7) reviews** the consolidation PR (all four epics present; suite 306/1 on
   both test surfaces) and authorizes the milestone-level merge.
3. **Merge PR #125** — M28 lands on `phase/P7`; then issue the Stage-2 "Milestone Fully
   Closed — M28" acknowledgment with the merge SHA.
4. **M28 is the final planned P7 milestone** (`is_final_milestone: true`). Its consolidation is
   what triggers the Phase Chat's own **phase-delivery sequence**: `phase/P7 → master` via the
   long-lived **PR #112**, executing the PSG §5C canonical closure sequence (README update,
   version bump, git tag, phase-closure declaration) — established at P6 and already exercised
   once.
5. *(Optional cleanup)* the merged epic branches `epic/P7-M28-E28.1 … E28.4` may be cleaned up
   per project policy.

---

**Declared by the Milestone Chat (P7-M28). Awaiting Phase Chat review and milestone-level
acceptance of the `milestone/M28 → phase/P7` consolidation PR #125.**
