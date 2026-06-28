---
type: milestone-closure-declaration
milestone: M22
status: complete
completion_date: 2026-06-28
declared_by: Milestone Chat (P5-M22 — Visual Artifacts)
issued_to: Phase Chat (P5 — Process Hardening and Visual Artifacts)
is_final_milestone: true
---

# MILESTONE CLOSURE DECLARATION — M22

Milestone **P5-M22 — Visual Artifacts** is hereby declared **COMPLETE**. Both epics (E22.1, E22.2),
delivering the VA-1 visual-artifact capability, have been executed, independently verified, accepted
under SN-13 default-accept, and merged to `milestone/M22` (HEAD `cb195eb`), with the full test suite
green (**259 passed, 1 skipped** — the lone skip is the visual-artifact endpoint test at the repo
default `enabled: false`). **M22 is the final P5 milestone** (`is_final: true`).

## Completion Verification

✅ **E22.1 — Configuration and spec (VA-1 config layer)** — merged to `milestone/M22` (PR #92, merge
`b002ac4`). Accepted under SN-13 default-accept; Epic Closure Notice `2026-06-28T15:00Z`. The
opt-in `visual_artifacts` block (`enabled` / `comfyui_url` / `types`) is documented in
`governance/ai-project-yml-spec.md` (§3.1, §3.5, §4 rules 18–24, §11; v2.0.0 → 2.1.0 + Changelog) and
validated **single-source** in the existing Python config handler (`bin/ai-project-orchestrator`),
with tests for valid / invalid / absent cases. This repo's `.ai-project.yml` carries the block with
`enabled: false`.

✅ **E22.2 — Guidelines, templates, and agent integration (VA-1 full)** — merged (PR #93, merge
`cb195eb`). Accepted under SN-13 default-accept; Epic Closure Notice `2026-06-28T16:30Z`. AOG §16
"Visual Artifact Production" (v2.1.0 → 2.2.0) carries the SN-11 per-level abstraction table, both
modes, tool-capability gating, and commit guidance; `seed.md` Rule 4 elicits visual intent before the
Project Brief (additive, no renumber); `bin/ai-project-visual` is a callable prompt→artifact ComfyUI
helper reading E22.1's config source; `governance/guides/visual-artifacts.md` documents it with a
per-level worked example; and an integration test **skips gracefully when `enabled: false`**.

Verified on `milestone/M22` (HEAD `cb195eb`): both epic merge commits present (`--no-ff`); every Epic
spec / Epic Execution Chat Starter / Delivery Notice / Epic Closure Notice committed; full suite green
(259 passed, 1 skipped, no failures); both epic branches deleted (local + remote).

## Milestone Definition of Done — all items satisfied

- ✅ E22.1 and E22.2 each meet their Definition of Done (recorded in their Delivery Notices and Epic
  Closure Notices).
- ✅ Both epic branches merged to `milestone/M22` (`--no-ff`).
- ✅ Full test suite passes on `milestone/M22` (259 passed, 1 skipped — the integration endpoint test
  skipped at `enabled: false`, by design).
- ✅ This Milestone Closure Declaration produced.

## Milestone Acceptance Criteria — all satisfied

1. ✅ `governance/ai-project-yml-spec.md` documents a validated `visual_artifacts` block; this repo's
   `.ai-project.yml` sets `enabled: false` (E22.1).
2. ✅ AOG (§16) directs an agent to produce the right visual for its chat level when
   `visual_artifacts.enabled: true` (E22.2).
3. ✅ `seed.md` elicits visual intent before the Project Brief (E22.2).
4. ✅ `bin/ai-project-visual` is callable by a tool-capable agent, calls the configured ComfyUI
   endpoint, and writes a visual artifact; `governance/guides/visual-artifacts.md` documents it with a
   per-level worked example (E22.2).
5. ✅ The integration test skips cleanly at `enabled: false`; the full suite is green.

## Milestone Summary

M22 makes visual artifacts a first-class, **opt-in** capability across the governance framework,
delivering SN-11 in full. The config layer (E22.1) adds and validates the `visual_artifacts` block;
the full implementation (E22.2) adds the per-level operating guidance (AOG §16), inception-time visual
elicitation (`seed.md` Rule 4), a callable ComfyUI helper (`bin/ai-project-visual`), an integration
guide, and a skip-on-disabled integration test. The framework/CFO split is honored: the framework
ships a working integration and keeps its own suite green at `enabled: false`; a reachable ComfyUI
endpoint remains the CFO's responsibility.

**M22 dogfooded the M20 hardening + the M21/SN-13 model:** prerequisites were verified with
`git ls-files --error-unmatch` (GH-1); both Epic specs and Epic Execution Chat Starters were authored
by the Milestone Chat under its own authority with no Phase-level drafts (GH-8 adjacency); the hard
E22.1 → E22.2 dependency was respected (E22.2 branched from the merged E22.1, consuming its config
contract read-only); and both clean deliveries were accepted under SN-13 default-accept with no Review
Decision artifacts (exception path never triggered), each merge passing through the CFO PR-review gate.

## Process Notes for Phase Chat (non-blocking)

1. **SN-13 default-accept throughout.** No Review Decision artifacts were issued for either epic —
   both deliveries were clean. Delivery Notices + Epic Closure Notices are present for both.
2. **CFO PR-review gate honored.** `cfo_review_gate: enabled` routed each merge-ready epic PR (#92,
   #93) to CFO diff review before merge rather than auto-merging; the Milestone Chat independently
   re-ran the suite before each.
3. **Manual endpoint verification deferred by design.** The visual helper is exercised against a live
   ComfyUI endpoint only when `enabled: true`; the source repo stays at `enabled: false`, so the
   integration test skips and the suite stays green. Endpoint availability is the CFO's responsibility
   (SN-11 framework/CFO split). Helper failure modes were verified directly (exits 2/3/4).

None affects milestone acceptance.

## Required Action: Consolidation — then Phase Delivery

M22 **is** the final P5 milestone. Its consolidation closes Phase P5.

1. Pull Request: `milestone/M22` → `phase/P5` (opened and kept current by this Milestone Chat).
2. Phase Chat (P5) reviews and authorizes the milestone-level merge (CFO PR-review gate applies).
3. Merge the consolidation PR — M22 lands on `phase/P5`.
4. **Phase delivery:** with M20 + M21 + M22 all consolidated, the Phase Chat proceeds to deliver
   Phase P5 to `master` (`phase/P5 → master`, PR #82) and issues the **P5 Phase Delivery Notice**.

---

**Declared by the Milestone Chat (P5-M22). Awaiting Phase Chat milestone-level acceptance of the
`milestone/M22 → phase/P5` consolidation PR. This is the final P5 milestone — its consolidation
clears the path to P5 phase delivery (PR #82).**
