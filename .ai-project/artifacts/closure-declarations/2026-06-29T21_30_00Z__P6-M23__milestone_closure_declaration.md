---
type: milestone-closure-declaration
milestone: M23
status: complete
completion_date: 2026-06-29
declared_by: Milestone Chat (P6-M23 — By-Link Storage Model and Binding Convention)
issued_to: Phase Chat (P6 — Visual Comprehension Layer and Process Refinements)
is_final_milestone: false
---

# MILESTONE CLOSURE DECLARATION — M23

Milestone **P6-M23 — By-Link Storage Model and Binding Convention** is hereby declared **COMPLETE
(awaiting consolidation)**. Both epics (E23.1, E23.2) have been executed by Coding Agents,
independently verified by this Milestone Chat, accepted under SN-13 default-accept, and merged to
`milestone/M23` (HEAD `651d55d`), with the full test suite green (**259 passed, 1 skipped** — the
lone skip is the visual-artifact endpoint integration test at the repo default `enabled: false`).
**M23 is not the final P6 milestone** (`is_final: false`); M24 and M25 follow on `phase/P6`.

## Completion Verification

✅ **E23.1 — By-link storage reconciliation (P6-VC-1)** — merged to `milestone/M23` (PR #97, merge
`84d6355`). Accepted under SN-13 default-accept; Delivery Notice committed
(`P6-M23-E23.1__delivery-notice.md`). The v5.0.0 commit-the-binary guidance is reversed to **by-link**
across the four named surfaces: `governance/AI-OPERATING-GUIDELINES.md` §16.5 (v2.2.0 → **2.3.0** +
reversal Changelog row); `governance/guides/visual-artifacts.md` §4 prose, §1 source-repo note, §3 +
§5 `--output` examples, and the related-documents row, plus a **new dated Changelog** recording the
reversal; `bin/ai-project-visual` output guidance (docstring + `--output` help) reframed as a local
working file (**no runtime change, no upload step** — Open Design Question B stays resolved); and the
integration test **verified already by-link-consistent and recorded with no make-work edit**.
Grep-confirmed: **zero** `.ai-project/visuals/` commit paths remain in the four surfaces.

✅ **E23.2 — Link + metadata binding convention (P6-VC-2)** — merged to `milestone/M23` (PR #98, merge
`651d55d`). Accepted under SN-13 default-accept; Delivery Notice committed
(`P6-M23-E23.2__delivery-notice.md`). `governance/guides/visual-artifacts.md` gains **§7 "Binding a
visual to an artifact"**: a five-element **binding schema** (Link + What / Level / State /
Description) that records a hosted **link, never a committed path**, and a **per-level placement
convention** for all five levels (Creation → `seed.md` Rule 4 *Visual success*; HQ → `genesis.md` HQ
Context Packet; Phase / Milestone / Epic → a *Visual Bindings* section in each spec template). The
five per-level templates each carry a defined binding placement, and the guide Changelog gains an
E23.2 row. `State` is a single field carrying the proposed/implemented two-track. Clip behaviour and
the proposed-vs-implemented routine behaviour are correctly **deferred to M24**.

Verified on `milestone/M23` (HEAD `651d55d`): both epic merge commits present; every Epic spec / Epic
Execution Chat Starter / Delivery Notice committed; full suite green (259 passed, 1 skipped, no
failures); E23.1's by-link reversal and all structural-diagram (Mermaid/PlantUML) guidance intact
after the E23.2 merge.

## Milestone Definition of Done — all items satisfied

- ✅ E23.1 and E23.2 each meet their Definition of Done (recorded in their Delivery Notices).
- ✅ Both epic branches merged to `milestone/M23` (PR #97 `84d6355`; PR #98 `651d55d`).
- ✅ No instruction to commit a generated binary remains anywhere in the four named surfaces
  (grep-verified; the only `.ai-project/visuals/` mention is §7's *prohibition*).
- ✅ The binding schema and per-level placement convention are documented (guide §7 + five templates).
- ✅ The reversal is recorded in the AOG changelog (2.3.0) **and** the guide changelog **as a reversal
  of v5.0.0**.
- ✅ Full test suite passes on `milestone/M23` (259 passed, 1 skipped — integration endpoint test
  skipped at `enabled: false`, by design).
- ✅ This Milestone Closure Declaration produced.

## Milestone Acceptance Criteria — all satisfied

1. ✅ `governance/guides/visual-artifacts.md` and AOG §16.5 instruct referencing visuals by link and
   explicitly state no generated binaries are committed to git (E23.1).
2. ✅ `bin/ai-project-visual` output guidance frames `--output` as a local working file to host and
   link, with no behaviour change and no upload step (E23.1).
3. ✅ The integration-test surface no longer implies a committed binary under `.ai-project/visuals/`
   (verified by-link-consistent) (E23.1).
4. ✅ The reversal is recorded as a reversal of v5.0.0 in the AOG and guide changelogs (E23.1).
5. ✅ A documented binding schema shows how a link + the four metadata fields attach to an artifact,
   with a defined placement per level (E23.2).
6. ✅ Structural-diagram guidance is unchanged (E23.1 / E23.2).

## Milestone Summary

M23 is the **foundation milestone of P6**. It reverses the single biggest governance change in the
phase — the v5.0.0 commit-the-binary storage model — to **by-link** (E23.1), and then defines the
**link + metadata binding convention** that makes by-link survivable once the link is the only thing
in git (E23.2). The reversal is recorded *as a reversal* in two changelogs so its provenance is
legible; the binding convention gives every governance level a defined home for a link plus the four
load-bearing metadata fields, with `State` carrying the proposed/implemented two-track. M23 changes
what the framework *says about storing and binding* visual output — not how the output is generated;
the producer (ComfyUI) and the helper (`bin/ai-project-visual`) were already done and verified
(SN-16). M24 (comprehension behaviour + clips) depends on the binding mechanism delivered here.

## Process Notes for Phase Chat (non-blocking)

1. **GH-8 adjacency honored.** The Phase Chat produced only the Milestone spec and Milestone
   Execution Chat Starter; this Milestone Chat authored both Epic specs and both Epic Execution Chat
   Starters under its own authority — no Phase-level epic drafts.
2. **Hard E23.1 → E23.2 dependency respected.** E23.2 was authored and executed against the *merged*
   by-link `milestone/M23`; the binding convention binds a link, never a committed path, and did not
   disturb E23.1's reversal (verified post-merge).
3. **SN-13 default-accept throughout.** Both deliveries were clean; no Review Decision artifacts were
   issued. Each epic's Delivery Notice is committed; this Milestone Chat re-ran the full suite and
   re-grepped the surfaces before each merge rather than trusting the notice.
4. **Merges performed by the Milestone Chat under Stage-2 authority.** The Coding Agents stopped at
   PR creation (canonical happy path) and did not self-merge; this Milestone Chat reviewed and merged
   PRs #97 and #98 to `milestone/M23`. The E23.2 merge was additionally **human-authorized** at the
   operator's console (the harness requires explicit human approval to merge an epic PR; Stage-2
   authority alone is not treated as human review). No separate Coding-Agent Epic Closure Notices
   were issued because the Coding Agents did not perform the merges; the merge facts live in the
   Delivery Notices, the merge commits, and this declaration.
5. **Open Design Question B remained resolved.** No upload/link-emitting step was added to the helper;
   hosting + linking is the agent's responsibility, now formalized by the E23.2 binding convention.

None affects milestone acceptance.

## Required Action: Consolidation

**To fully close this milestone, consolidation is required — this is the Phase Chat's
(milestone-level) acceptance:**

1. **Pull Request:** `milestone/M23` → `phase/P6` (long-lived **PR #96**, opened and kept current by
   this Milestone Chat).
2. **Phase Chat (P6) reviews** the consolidation PR (all M23 work present; branch hierarchy correct;
   suite green) and authorizes the milestone-level merge.
3. **Merge PR #96** — M23 lands on `phase/P6` (this becomes the milestone closure commit); then issue
   the **Stage-2 "Milestone Fully Closed — M23"** declaration with the merge SHA.
4. **M23 is not final.** After consolidation, **`milestone/M24` MUST branch from `phase/P6`**. Do
   **not** proceed to phase delivery (`phase/P6 → master`, PR #95) — M24 and M25 remain.
5. *(Optional cleanup)* the merged epic branches `epic/P6-M23-E23.1` and `epic/P6-M23-E23.2` may be
   deleted (local + remote) per project policy.

---

**Declared by the Milestone Chat (P6-M23). Awaiting Phase Chat milestone-level acceptance of the
`milestone/M23 → phase/P6` consolidation PR #96. M23 is the foundation milestone of P6 — its binding
convention is the prerequisite for M24 (comprehension behaviour + clips).**
