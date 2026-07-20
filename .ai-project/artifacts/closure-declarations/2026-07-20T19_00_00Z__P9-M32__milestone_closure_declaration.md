---
type: milestone-closure-declaration
milestone: M32
status: complete
completion_date: 2026-07-20
declared_by: Milestone Chat (P9-M32 — System Participant Canonization & Governance Hygiene)
issued_to: Phase Chat (P9 — Context Handling and Token Efficiency)
is_final_milestone: true
---

# MILESTONE CLOSURE DECLARATION — M32

Milestone **P9-M32 — System Participant Canonization & Governance Hygiene** is hereby
declared **COMPLETE (awaiting consolidation)**. All three planned epics — E32.1, E32.2,
E32.3 — have been executed, independently verified by this Milestone Chat (diff review
against the exact claimed scope, live suite re-runs on this branch after each merge, the
grep checks re-run personally rather than trusted from the Delivery Notices, direct byte-
diff of the Authority Boundary text across all three surfaces that carry it, direct
inspection of the edited governance sections) — accepted under PSG §11.6 default-accept,
and merged to `milestone/M32` with explicit human merge authorization for each (SN-19/
§11.6). Full test suite is green on consolidated `milestone/M32` @ `1a9e781`: **363 passed,
0 failed, no new skips** (unchanged from the M31-closing baseline — this milestone's work
is documentation/schema only).

**M32 is the third and final planned P9 milestone (`is_final_milestone: true`).** This
declaration triggers the Phase Chat's next action directly: `phase/P9 → master` via the PSG
§5C canonical closure sequence. There is no further P9 milestone to plan or schedule.

## Completion Verification

✅ **E32.1 — SN-21 canonization (merged PR #146, `5c649a7`).** Canonized System HQ — the
cross-project, one-desk-per-machine participant field-adopted 2026-07-16 (SN-21) — into
governance. Design Decision 1 (schema home): **(B) companion document**
(`governance/systems/system-hq.md`, new), reasoned because the protocol's existing types are
all intra-project and its Core Principles/Communication Flow Diagram assume a single-project
chain — a cross-project pair would sit in tension with that document rather than extend it
cleanly; the protocol gained one `## Reference` line + a changelog row (v1.3.0 → v1.4.0),
nothing else. Design Decision 2 (hierarchy placement): an **out-of-hierarchy annex** in
`chat-hierarchy.md`, deliberately placed away from the four-level material, with an early
pointer note plus a structural contrast table stating "not a fifth level" — not a single
prose disclaimer. The `system_request`/`system_response` schemas, storage paths
(`.ai-project/artifacts/system-{requests,responses}/`), naming convention, and status
vocabulary (`pending | in_progress | done | declined | escalated`) all match SN-21's field
usage verbatim — documented, not invented. The normative Authority Boundary
(execute-never-decide; `status: escalated` mandatory for review/merge/scope) is canonical in
`system-hq.md` and reproduced verbatim in the `chat-hierarchy.md` annex. **Verified
independently:** diff scope was exactly the three claimed files (`system-hq.md` new,
`+2/-2` in the protocol, additive-only in `chat-hierarchy.md`); the two Authority Boundary
blocks were byte-diffed and are identical; every pre-existing `chat-hierarchy.md` section
(Execution Mode, Manual Chat Model Verification, Working-Tree Isolation, Communication
Protocol, Authorization Artifacts) confirmed unreworked; suite 363/0.

✅ **E32.2 — System Chat re-instantiation seed (merged PR #147, `762d287`).** Built
`governance/systems/system-hq-seed.md` — a self-contained, paste-into-a-fresh-session daily
re-instantiation prompt, mechanically analogous to `seed.md`'s "Rule 5 — Re-instantiation"
but scoped to System HQ's cross-project, execute-never-decide identity. Design Decision 1
(form/home): **a system-tier document** at `governance/systems/system-hq-seed.md`, sited
next to E32.1's `system-hq.md` rather than inside `governance/templates/` (which the Epic
Chat correctly judged would have structurally implied the opposite of what E32.1 had just
established — that System HQ is not per-project scaffolding). The Authority Boundary is
reproduced verbatim (self-containment requirement — the seed must work alone); the
artifact schemas, storage paths, naming, and status vocabulary are referenced, never
restated, avoiding the exact divergence risk the Epic existed to prevent. E32.1 had already
merged when this Epic ran, so its cross-references point at what E32.1 actually shipped —
no advance-citation reconciliation was owed. Two non-blocking notes surfaced by the Epic
Chat and left as-is by this Milestone Chat: a cosmetic grounding-count drift in the spec (23
vs. the actual 25 files in `governance/templates/`, immaterial to the design reasoning), and
a one-way-only cross-reference (`system-hq.md` has no back-pointer to the seed — correctly
left unedited by the Epic Chat, since editing an already-merged E32.1 surface was outside its
bounds; a one-line follow-up at the Phase Chat's discretion, not required by any acceptance
criterion). **Verified independently:** diff scope was exactly one new file; the seed's
Authority Boundary block was byte-diffed against `system-hq.md`'s canonical block and is
identical; suite 363/0.

✅ **E32.3 — Governance hygiene reconciliation (merged PR #148, `1a9e781`).** P8-GH-1: the
"stays opted out because…" framing removed from AOG §16.5 and the matching stale callout in
`governance/guides/visual-artifacts.md` corrected; §6 "Testing without a live endpoint"
reframed (not deleted) into the two skip paths that genuinely exist in
`tests/integration/test_visual_artifacts_helper.py` — the `enabled: false` path (other
projects) and `AI_PROJECT_SKIP_LIVE_ENDPOINT_TESTS=1` (contributors/CI on a project that has
it on) — with this repo's own `enabled: true` (since E29.2) state stated plainly. P8-GH-3:
all six pre-P9 documents purged of the vestigial "Phase Delivery Notice" phrase, with one
document (`P5-M22__milestone-spec.md`) handled differently on purpose — P5 genuinely produced
a separate `P5__phase-delivery-notice.md` file, still in the repo, so the Epic Chat cited it
by its real path instead of rewriting a true historical statement into a false one. The P8
phase closure declaration's own carry-forward record was left untouched — confirmed by an
empty `git diff` against that file. One self-flagged nuance, judged correctly: a historical
AOG changelog entry (the v2.7.0 row) still restates the old opt-out rationale as *what that
version said at the time* — left alone as a dated historical record, matching the same
principle the P8 closure declaration's own carry-forward table relies on, and independently
placed out of scope by the Epic spec's own Technical Constraints (§16.5 only). **Verified
independently:** both acceptance-criterion greps re-run personally (`stays opted out` →
nothing repo-wide; `Phase Delivery Notice` → only P9's own quoted-discussion docs and the P8
closure declaration); the `AI_PROJECT_SKIP_LIVE_ENDPOINT_TESTS` claim checked against actual
test source, not assumed; diff scope was exactly the six named files + AOG + the guide; suite
363/0.

## Milestone Definition of Done — verified

- ✅ E32.1, E32.2, and E32.3 each meet their Definition of Done (verified per-epic above)
- ✅ All three epic branches merged to `milestone/M32` (PRs #146–#148, each independently
  Stage-2 reviewed by this Milestone Chat before human merge authorization — no delivery
  accepted on the notice's word alone)
- ✅ `system_request`/`system_response` schemas, hierarchy placement, and the normative
  authority boundary all exist and agree with each other (E32.1; Authority Boundary
  byte-identical across `system-hq.md` and the `chat-hierarchy.md` annex)
- ✅ The System Chat re-instantiation seed exists and is usable, and agrees with E32.1's
  canonized material rather than restating it divergently (E32.2; Authority Boundary
  byte-identical to `system-hq.md`'s canonical block)
- ✅ Both P8-GH-1 and P8-GH-3 grep checks pass cleanly; P8-GH-2's deferred status is
  restated, not silently dropped (E32.3 — see restatement below)
- ✅ Full test suite passes on `milestone/M32` @ `1a9e781`: **363/0**, no regressions, no
  new skips
- ✅ This Milestone Closure Declaration produced (`is_final: true` — triggers phase delivery)

## Milestone Acceptance Criteria — verified

1. ✅ `system_request`/`system_response` schemas are in the companion document
   (`governance/systems/system-hq.md`), the hierarchy placement is recorded as an explicit
   out-of-hierarchy annex, and the System Chat re-instantiation seed
   (`governance/systems/system-hq-seed.md`) is usable daily (E32.1, E32.2 — phase
   acceptance criterion, verbatim)
2. ✅ Grep-level checks show no remaining stale opt-out prose (P8-GH-1) and no remaining
   "Phase Delivery Notice" phrasing in templates/living docs outside the intentional
   carry-forward record (P8-GH-3 — phase acceptance criterion, verbatim; re-run personally
   by this Milestone Chat, not trusted from the Delivery Notice)
3. ✅ No authority expansion anywhere in the delivered material — execute-never-decide is
   explicit at every surface that describes System HQ, and is byte-identical across all
   three surfaces that carry it (`system-hq.md`, the `chat-hierarchy.md` annex, the seed) —
   Hard Constraint 1
4. ✅ P8-GH-2 remains recorded as deferred with its trigger, not silently dropped (Hard
   Constraint 3 — restated explicitly below, per this milestone's own Notes requirement)
5. ✅ The full suite is green at milestone delivery with no regressions and no new skips

## P8-GH-2 and the ComfyUI track — restated per this milestone's own instruction

This milestone's own Notes required its closure declaration to restate two items that are
not its own work, because M32's closure is what the Phase Chat's `phase/P9 → master`
sequence depends on finding (phase acceptance criteria items 7–8, verbatim below).

> **P8-GH-2 — Machine-local hosting limitation (Low).** The storage backend provisioned to
> complete E29.3's bindings is local only — `file://` links resolve on this machine and
> nowhere else (dead on GitHub, dead for any other reader). **Accepted by CFO ruling for
> this phase; revisit only if cloud-reachable hosting is ever actually needed for this
> project.** Status confirmed **unchanged: deferred**, on its recorded trigger. Source
> record (`docs/phases/P8__Visual_Artifacts_Activation/P8__phase-closure-declaration.md`,
> Carry-Forward row P8-GH-2) is untouched — confirmed by empty diff during E32.3's review.
> No hosting work was scoped into P9 at any point.

> **ComfyUI precision investigation (SN-20 Carry-Over 3).** Confirmed **unchanged:
> non-blocking, CFO-side track** (P9 phase spec, "Out of Scope"). Nothing in P9 — including
> this milestone — touched, blocked on, or resolved it. If the investigation lands during or
> after P9, its outcome routes through Creation Chat / HQ as new input, not into a closed
> milestone or phase.

Phase acceptance criteria 7 ("P8-GH-1 and P8-GH-3 are reconciled; P8-GH-2 remains recorded as
deferred with its trigger, not silently dropped") and 8 ("The ComfyUI track is surfaced, not
resolved — its status at phase close is reported to the CFO as the non-blocking track it is")
are both satisfied by this milestone's delivery, ready for the Phase Chat to carry directly
into the Phase Closure Declaration.

## Handed to the Phase Chat

- **Consolidation:** `milestone/M32 → phase/P9` is ready for Phase Chat acceptance and
  human-authorized merge (no PR opened yet for this consolidation — per the M30/M31
  precedent, the *receiving* chat drives consolidation).
- **This is the final P9 milestone.** On consolidation, the Phase Chat proceeds directly to
  phase delivery — `phase/P9 → master` via PSG §5C (README update retiring the stale test
  count, version bump, git tag, Phase Closure Declaration) — no further milestone to plan.
- **P8-GH-2 and the ComfyUI track restatement above** is written so the Phase Chat can carry
  it directly into the Phase Closure Declaration without re-deriving it.
- **One non-blocking follow-up, at the Phase Chat's discretion, not required by any
  acceptance criterion:** `governance/systems/system-hq.md` has no back-reference to
  `governance/systems/system-hq-seed.md` (the cross-reference is one-way, seed → doc). A
  one-line `## Reference` addition would close the loop; E32.2's Epic Chat correctly declined
  to make this edit unilaterally since it falls on E32.1's already-merged surface.
- **No open gap register items from this milestone** — E32.1–E32.3 all closed clean, with
  every judgment call (Design Decisions, the AOG changelog preservation, the P5-M22 special
  handling) documented and independently verified rather than accepted on trust.
- **No dependency carried to any future P9 work** — there is none; M32 was the last
  milestone.

---

**Milestone P9-M32 planning and delivery complete. All three Epic specs, Chat Starters, and
Epic deliveries accepted; all epic branches merged; P8-GH-2 and the ComfyUI track's status
both restated for the Phase Chat. M32 is the final P9 milestone — its consolidation is the
direct trigger for `phase/P9 → master` phase delivery. Session closes on Phase Chat
consolidation of `milestone/M32 → phase/P9`.**
