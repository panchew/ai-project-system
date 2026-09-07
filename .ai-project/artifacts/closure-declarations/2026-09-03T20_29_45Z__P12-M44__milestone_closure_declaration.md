---
type: milestone-closure-declaration
milestone: M44
status: complete
completion_date: 2026-09-03
declared_by: "Milestone Chat (P12-M44 — Rituals, Records, and the Normative Repairs)"
issued_to: "Phase Chat (P12 — Completion: Fail-Closed Defaults and the Drivr MVP)"
is_final: false
---

# MILESTONE CLOSURE DECLARATION — M44

Milestone **P12-M44 — Rituals, Records, and the Normative Repairs** is declared **COMPLETE
(awaiting consolidation)**.

**Six epics were delivered, re-measured by this Milestone Chat at Stage-2 (G2), and merged with
explicit human merge authorization for each:** **E44.2** (#256), **E44.1** (#257), **E44.3** (#258),
**E44.4** (#259), **E44.5** (#260), **E44.6** (#261). **One rework attempt was consumed** — E44.4's
cross-reference sweep required one bounded re-sweep (see §Findings); the other five stand at attempt 1
of 3.

---

## ⚠ THE ONE SENTENCE THIS MILESTONE SHOULD BE READ BY

> **Every item here was SN-33's shape — a thing that should be recorded is not, and no mechanism
> notices — and M44 wrote the records: the phase now hands its successor a defined artifact instead of
> a PR comment; the record now distinguishes *decided* from *configured* from *evidenced* without
> inference; the AOG can finally be cited unambiguously; and the normative tier says only what is
> true, with each surviving rule carrying its own reason.**

---

## The recursion, discharged — read this before the DoD

**M44's subject is the records other work depends on, and its own execution is the first customer.**
Three of its epics amended the normative tier while the milestone itself was governed by that tier's
pre-amendment text; the milestone spec moved **three times mid-flight** (v1.2.0 — E44.2 re-scoped from
*specify* to *execute* after E41.5 landed first and handed over the row-P4 rewrite; v1.2.1 — the spent
deadline and the `549` baseline corrected across four surfaces; plus the set-6 monotonicity ruling
folding `16-before-15` into E44.4's D5). **The `P11-GH-1` channel fired on all three and carried** —
each amendment reached this branch with a changelog row and a re-read obligation, which this Milestone
Chat stated in each subsequent delivery.

**The consequence, stated because it is the point:** this milestone is the first to close under the
amended §11.6 (E43.2's named-acknowledgment, *silence accepts nothing*), and its own six epics were the
first deliveries accepted under it. Per **E43.1**, the milestone merge `milestone/M44 → phase/P12` is
performed by the **Phase Chat**, not by this Milestone Chat. This declaration does not merge itself.
See §Required Action.

---

## Completion Verification — the Definition of Done, item by item

| # | DoD item | Disposition |
|---|---|---|
| 1 | All six epics delivered, accepted, and merged to `milestone/M44` | **MET.** E44.2 `0413caf`, E44.1 `09e4451`, E44.3 `97afdd6`, E44.4 `52380f4`, E44.5 `9fff3da`, E44.6 `9ae72e4` |
| 2 | A Phase Completion Declaration template exists and §5C Step 2 names it; **Step 9 unchanged** | **MET** (E44.1). `phase-completion-declaration.md` (marked `COMPLETE (awaiting consolidation)`); PSG §5C Step 2 names it, Step 6 reviews it, **Step 9 and `phase-closure-declaration.md` untouched** — additional, not a relocation. PSG 2.7.0 → 2.8.0 |
| 3 | HQ re-instantiation is documented in one normative place and **matches the nine instances** | **MET** (E44.1). `hq-re-instantiation.md` records the ritual from the nine openers, covers departure **and** arrival, reports three divergences (7/9 `supersedes:`, 3/9 E31.3, 4-vs-5 body form) rather than normalizing them; `hq-chat.md` and the opener template cite it |
| 4 | A handoff artifact type and template exist | **MET** (E44.1). `context-handoff.md` — type `context_handoff`, two faces (written + reconstructible-from-committed-state), **Drivr boundary stated**, M46 role-registry held apart |
| 5 | The decided-but-unconfigured convention exists, and E41.5 has not had to improvise | **MET** (E44.2). The convention lives in `model-routing-policy.md`, covers both faces (decision-ahead-of-configuration, configuration-ahead-of-evidence); row P4's `why` cell rewritten to an allowance-decided account, E41.5's handoff discharged, **no CFO-enumerated value moved** |
| 6 | The fourth state is defined; silence is never a path through it | **MET** (E44.3). `chat-hierarchy.md` defines config-present + self-report-absent (refuse by default, recorded declaration, silence never); the inter-chat paragraph (`P12-GH-4` narrow half) landed restating SN-36, inbound-as-threat-model, channel not designed |
| 7 | AOG sections are `1..n`, unique by number and title; cross-references updated; **no quoted example rewritten**; version bumped | **MET** (E44.4). Renumbered `1..18` monotonic, `1A` folded to `1.1`, title collision resolved (`Error Handling (Duplicate)` + `Error Handling`); corpus-wide sweep (one re-sweep); the nine fenced example headings **byte-identical**; AOG 2.11.0 → 2.12.0 |
| 8 | `governance-propagation.md` states only true constraints, each surviving prohibition with its own reason; the i18n paragraph is in the normative tier | **MET** (E44.5). Both false Constraints struck for a dated capability statement + re-check-on-versioning rule; each survivor carries its reason; the i18n paragraph is one paragraph resolving the English-to-Spanish tension. 1.0.0 → 1.1.0 |
| 9 | SN-30 Rec 1's checks exist; G1 and G2 are in a core document | **MET** (E44.6). Checks for defects #2/#3/#4 each falsified (defect #1 is E44.4's D5, cited not rebuilt); G1/G2 promoted into PSG §2 Core Principles, verbatim-in-substance. PSG 2.8.0 → 2.9.0 |
| 10 | `P11-GH-1`'s note carries P12's instance, **no ordinal**, gap still open and unscoped | **MET** (E44.6). Three instances recorded by artifact + defect (out-of-chain Creation-Chat catch, upward branch staleness, derived-claim rot); no ordinal; evidence only, fix not reopened; gap open and unscoped |
| 11 | **No deliverable states a coverage count where a list belongs** | **MET.** The four defects, the nine instances, the nineteen handoff-mention documents, and the four states are all itemized, never counted |
| 12 | **`P12-GH-3` was not absorbed** — it remains filed, unowned, with its trigger | **MET.** No epic reached for it; the convention E44.2 built is about *decided/configured/evidenced* on named rows, not derived-claim marking — the excluded defect stays excluded |
| 13 | Suite green at **740** plus this milestone's additions | **MET.** 740 (v1.2.1-corrected baseline) + 11 (E44.4) + 15 (E44.6) = **766 passed / 1 skipped**, re-measured at each stage. The one skip is the pre-existing live-ComfyUI integration test (environmental — no endpoint on this box). **No skip introduced** |
| 14 | Milestone Closure Declaration committed, `is_final: false` | **This document** |

---

## Acceptance Criteria (Milestone) — verified

- [x] **A successor at any level can name the artifact it receives, and find its template.** Phase →
      the Phase Completion Declaration (`phase-completion-declaration.md`); HQ re-open → the ritual
      (`hq-re-instantiation.md`); context exhaustion → `context-handoff.md`. Each has a template and a
      named path.
- [x] **The record distinguishes "decided" from "configured" wherever both apply.** E44.2's convention
      makes the three facts readable from the row alone, without inference.
- [x] **Every normative statement this milestone touches is true on its stated date, with its reason.**
      `governance-propagation.md`'s constraints are dated and re-checked-on-versioning; each surviving
      prohibition carries its own reason.
- [x] **No finding this milestone touches still lives only in an epic-tier artifact.** G1/G2 promoted
      out of epic specs into PSG §2; the four observed defects have checks; the `P11-GH-1` instance is
      in the carry-forward note — not in a delivery notice.
- [x] **No pass over a normative document rewrote a quoted example — demonstrated.** E44.4's nine
      fenced example headings are byte-identical; the fence-aware inventory and the `:134` parity
      self-test are the shown evidence, not an assertion.
- [x] **Every claim states the layer, time and scope it was verified at.** Carried through every epic's
      record (`P11-GH-2`), re-measured at Stage-2 (G2) rather than taken on report.

---

## Findings — recorded honestly, not folded into the tick

**1. E44.4 consumed the milestone's one rework attempt — and the failure was the useful half.** The
first sweep over-applied "inside-a-fence = don't touch" and missed three live cross-references
(`ai-project-yml-spec.md` §16.3, `artifact-flow.md` and `merge-authorization.md` AOG §12). The
re-sweep fixed all three under the corrected distinction — *sweep a document's own cross-references
even inside its own worked examples; preserve only quoted external artifact bodies* — and re-scanned
with no further occurrence. The finding is the fence-detector hazard (`:134`'s indented four-backtick
marker) that breaks toggle-based detectors, now carried in E44.4's D1/D5 with a parity self-test.

**2. Duplicate `Error Handling` content remains, marked not removed.** The AOG carries the same
Error-Handling rule twice; E44.4 resolved the *title* collision by titling the first
`Error Handling (Duplicate)` (in-scope: no content deletion), which makes the citation unambiguous but
leaves the duplicated content for a future dedup. **No owner.** Flagged for the phase record.

**3. The Delivery Notice location split.** E44.2 filed its Delivery Notice in
`.ai-project/artifacts/delivery-notices/` (matching M42/M43 practice); E44.1/E44.3/E44.4/E44.5/E44.6
filed in `docs/phases/…` (matching the `epic-execution-chat-starter` template's stated path). The
template and the established practice disagree, and this milestone reproduced both sides. No test
catches it (both notices exist and are findable), but it is a live two-place inconsistency of exactly
the shape this milestone is about. **No owner.** Flagged for the phase record.

**4. Historical documents were correctly left un-swept.** E44.4's corpus-wide sweep updated live
cross-references but left closed-phase (P6/P7/P8) documents' `§16.x` references untouched — correct
(a closed-phase record describes what *was*), but the "does 'corpus-wide' include the closed record"
question is worth a ruling if a future sweep asks. Flagged for the phase record.

**5. Amendment history, for the phase record.** The milestone spec moved mid-flight three times
(v1.2.0 re-scope, v1.2.1 deadline/baseline correction, set-6 monotonicity ruling), each delivered
through the `P11-GH-1` channel to a running child and acknowledged. The governing spec is at v1.2.1 on
this branch; its Changelog is the version statement.

---

## Milestone Summary — what M44 actually produced

**The continuity and normative tiers were the thinnest in the framework; M44 thickened them.**

1. **A successor at any level now has a named artifact.** The Phase Completion Declaration (`P11-GH-3`,
   §5C Step 2, Step 9 unmoved), the recorded HQ re-instantiation ritual (departure *and* arrival, from
   nine instances), and the context-exhaustion handoff (reconstructible from committed state alone).
2. **The record holds *decided* apart from *configured* apart from *evidenced*.** E44.2's convention,
   applied to row P4, so a reader no longer infers one from the other.
3. **The AOG is citable unambiguously** — by number and title — with a fence-aware check that fails on
   duplicate *or* out-of-order, and a cross-reference sweep that never rewrote a quoted example.
4. **The normative tier says only what is true.** `governance-propagation.md`'s false constraints are
   struck for a dated capability statement; the fourth verification state is defined (refuse by default,
   silence never); the inter-chat channel is governed (routing-not-record, restating SN-36); G1/G2 are
   promoted into the constitution; and P12's own `P11-GH-1` instance is on the record, no ordinal.

**Net:** P12's own closure is now `P11-GH-3`'s first customer with an artifact that exists — the
defect this milestone exists to fix is discharged before the phase needs it.

---

## Required Action: Consolidation

**To fully close this milestone, consolidation is required — and per E43.1 it is the Phase Chat's
act, not this Milestone Chat's:**

1. **The Phase Chat reviews this declaration** and the six merged epic branches.
2. **The Phase Chat creates and merges** `milestone/M44 → phase/P12` (the consolidation commit).
3. **The Phase Chat flips the milestone spec's `status` from `planned` to `completed`** in the same act
   (per the M42/M43 precedent — `planned` through the planning merge, `completed` only at closure).
4. **The Phase Chat reports the merge commit SHA** back to this Milestone Chat.

**No `milestone/M45` or `milestone/M47` depends on this milestone** (M44 is independent of both), and
M44 completes before P12 closes — a hard constraint, since **P12's own closure is `P11-GH-3`'s first
customer.**
