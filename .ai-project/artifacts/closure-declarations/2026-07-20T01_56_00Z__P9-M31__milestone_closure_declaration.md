---
type: milestone-closure-declaration
milestone: M31
status: complete
completion_date: 2026-07-20
declared_by: Milestone Chat (P9-M31 — Dual-Mode Working Levels & Model Guardrail)
issued_to: Phase Chat (P9 — Context Handling and Token Efficiency)
is_final_milestone: false
---

# MILESTONE CLOSURE DECLARATION — M31

Milestone **P9-M31 — Dual-Mode Working Levels & Model Guardrail** is hereby declared
**COMPLETE (awaiting consolidation)**. All three planned epics — E31.1, E31.2, E31.3 — plus
the milestone-level Post-M31 Measurement Recapture deliverable have been executed,
independently verified by this Milestone Chat (diff review, live suite re-runs on this
branch after each merge, grep checks for the specific acceptance-criterion strings, direct
inspection of the governance sections and template edits — not Delivery Notices trusted on
faith), accepted under PSG §11.6 default-accept, and merged to `milestone/M31` with
explicit human merge authorization for each (SN-19/§11.6). Full test suite is green on
consolidated `milestone/M31` @ `da7a386`: **363 passed, 0 failed, no new skips** (up from
the 307 baseline via 56 new tests added across E31.2 and E31.3).

**M31 is the second P9 milestone, not the last (`is_final_milestone: false`).** One
milestone remains: **M32 (SN-21 canonization + P8-GH-1/3 hygiene) is independent**,
schedulable by the Phase Chat at its discretion — it has no dependency on M31 in either
direction. This declaration triggers Phase Chat consolidation of `milestone/M31 →
phase/P9`; it does not trigger phase closure.

## Completion Verification

✅ **E31.1 — Mode model + declaration mechanism (merged PR #140, `31eff27`).** Recorded the
manual/agentic mode model in `governance/systems/chat-hierarchy.md`, a new "Execution
Mode: Manual vs. Agentic" section immediately after the existing Hierarchy Summary Table.
The naming collision with that table's pre-existing "Mode" column (level selection) was
resolved up front — the new axis is always spelled "Execution Mode," never bare "mode."
Declaration mechanism: an `Execution Mode` field in each concrete instance's own committed
Execution Chat Starter (`.ai-project.yml` was deliberately not used — rejected as
project-wide and drift-prone against the "per instance" requirement); absence of the field
means manual, stated in the same section that defines the levels. Creation Chat and HQ
Chat recorded manual-only, permanently, normatively, in the same section (SN-22). G7
(one-task-one-session) adopted as labeled, measured-evidence-based guidance (53% mixed
milestone/phase spend vs. 23% epic execution, audit-report.md §2.2) — recommendation, not
a gate. **Demonstration evidence is real, not simulated**: the manual side is that Epic
Chat's own starter (no Execution Mode field → manual, real in-session execution); the
agentic side is a real dispatch of a proving vehicle (`P9-M31-E31.1-PROVE`) through the
unmodified `bin/ai-project-orchestrator` → `bin/run-dev-agent` path against a real local
Ollama endpoint — converged, run artifacts committed. Verified independently: the
"Execution Mode" section exists at the stated location; Creation/HQ manual-permanence
text is present; suite was 307/0 at merge.

✅ **E31.2 — Agentic paid-vs-local decision logic (merged PR #141, `ec85826`).** Fixed the
four gaps M30's closure handoff identified in the one dispatch surface that actually runs
today (`handle_epic_execution` → `run-dev-agent`, epic-level only — the spec was explicit
that HQ/Phase/Milestone have no dispatch mechanism to apply "per task" logic to, and none
was built). `DEFAULT_MODELS` aligned with the refreshed `models:` block — verified by grep,
no falsified name (`gpt-4o`, `claude-3-5-sonnet`, `qwen2.5-coder:7b`) anywhere in `bin/`.
`dev_model`/`qa_model` resolution now cites policy rows P6/P7 in-code (traceability-only,
by design decision — the CI-time guard test already catches drift, a runtime divergence
assertion was judged redundant cost). Consistency-guard tests extended from `epic_dev`-only
(4 tests) to all five `models:` keys plus a policy↔block divergence check (verified live
with a deliberately introduced mismatch that was confirmed to fail, then reverted).
Local-unavailable handling implemented and tested in two layers: `bin/run-dev-agent` gains
a documented `EXIT_LOCAL_UNAVAILABLE` (= 5, deliberately reusing `bin/ai-project-visual`'s
existing GPU-contention exit-5 convention) via an Ollama-reachability preflight;
`handle_epic_execution` short-circuits on that exact signal with a distinguished escalation
record instead of burning retries against a dead endpoint. Row-P5 run evidence: a real
proving-vehicle dispatch (`P9-M31-E31.2-PROVE`) converged with dev/QA both correctly
resolved to `local:qwen2.5-coder:14b`. Verified independently: suite was 349/0 at merge
(307 baseline + 42 new); grep over `bin/` clean; the honest scope-limiting note (per-task
decision logic covers epic×execution only) is stated plainly in the delivered code
comments and Delivery Notice, not overclaimed.

✅ **E31.3 — Manual-mode startup guardrail (merged PR #142, `d985538`).** Closed the manual
half of the founding failure. Level→model mapping (Design Decision: reuse existing
`hq`/`phase`/`milestone` keys; add two new manual-only keys, `creation` and
`epic_manual`, both `remote:claude-opus-4-8`, sourced from policy rows P1/P5 without
editing the policy file; yml-spec bumped 2.4.0 → 2.5.0). Self-verification method
documented: the harness's own `# Environment` system-context self-report is the only
mechanism observed to exist in this environment, with its limit stated plainly
(harness-trust-dependent, not independently verifiable). Verify-and-refuse instruction
added to all five manual-chat template surfaces — the three Execution Chat Starters plus
`hq-chat-opener.md` and `genesis.md`/`seed.md` (the Creation/HQ gap the epic spec flagged
as easy to miss, since those two templates are outside the three E31.1 touched); absent
block/key is a documented permissive default, a present mismatch is an unconditional stop;
E30.3's scoping blocks and E30.4's reference-first wording preserved verbatim on every
edited template. Policy↔block divergence extended (new, self-contained check against
`chat-hierarchy.md`'s own mapping table, since the two new manual-only keys have no
agentic dispatch surface and don't belong in `model-routing-policy.md`'s table). Refusal
evidence is this session's own real, live facts, not a synthetic scenario: the same
continuous session ran first as the Milestone Chat (`claude-sonnet-5` vs. configured
`remote:claude-opus-4-8` for `milestone`) then as the E31.3 Epic Chat (same mismatch
against the new `epic_manual` key) — both genuine mismatches under the mapping this epic
defines. **Process note, recorded for completeness:** this PR's merge was authorized by
the human directly inside the Epic Execution Chat, bypassing this Milestone Chat's Stage-2
review at the time of merge. The Milestone Chat performed the review retroactively
(documented below) and found the delivery clean; the process gap itself is recorded as
[[feedback-merge-authorization-routing]] (Milestone Chat's persistent memory) and a guard
was added to `governance/templates/epic-execution-chat-starter.md` (commit `8dbffe0`, this
milestone) so a future Epic chat confirms before acting on an in-chat authorization that
bypasses parent-chat review. Verified independently (retroactively): suite was 363/0 at
merge; the new `chat-hierarchy.md` section, the two new `.ai-project.yml` keys, the
yml-spec bump, the refusal-evidence file, and E30.3/E30.4 preservation across all five
edited templates were each directly inspected.

✅ **Post-M31 Measurement Recapture (merged PR #143, `da7a386`) — milestone-level
deliverable, not a fourth epic.** `bin/measure-token-burn` rerun unmodified into a
separate `--out` directory, verified to leave the M30 baseline dataset frozen and
untouched. **Honest verdict: no reduction observed.** E30.3's Direction B pack-reduction
claim is structurally untestable by this recapture — the mechanism's pack cells are
permanently pinned to the pre-E30.3 file set by E30.3's own design decision, so a rerun
can never show that reduction by construction; re-verifying it needs a new artifact in
`context-scoping.md`'s own style, not a mechanism rerun. Direction A billed per-call
context medians moved the wrong direction — phase flat (169,003 → 169,003), milestone
+11.2% (129,135 → 143,575), epic +6.4% (76,135 → 81,017) — but the recapture's own §1
finding shows this is not cleanly attributable to anything: the harness session directory
is not append-only (5 sessions rotated out, 9 new ones in between the two runs), and the
true M31-only measurable population is 4 sessions (3 complete) — too small to compute a
defensible median against a 17–72-session baseline. E30.4's echo-vs-reference claim has no
mechanism signal to test it against; recorded as a gap, not inferred from a proxy,
consistent with `echo-cost-note.md`'s own G14. TTL caveat (±18% bound) stated wherever a
dollar conversion would apply. Three new mechanism findings recorded (a missing `--since`
filter, the permanently-pinned Direction B packs, the absent echo-vs-reference signal) —
none fixed here, per the Hard Constraint that `bin/measure-token-burn` stays unmodified.
This is the "no movement yet, window too short" outcome the Milestone spec explicitly
named as an acceptable finding. Verified independently: the M30 baseline dataset's last
git-touching commit remains its original E30.1 commit (confirming it was never
overwritten); `bin/measure-token-burn` diff against the pre-recapture tree is empty; suite
363/0 at merge; scope was exactly three files added, nothing else touched.

## Milestone Definition of Done — verified

- ✅ E31.1, E31.2, and E31.3 each meet their Definition of Done (verified per-epic above)
- ✅ All three epic branches merged to `milestone/M31` (PRs #140–#142, each human-authorized;
  #142's authorization routing gap is recorded above and in memory, not hidden)
- ✅ Phase success criteria 3–5 evidenced: dual start demonstrable + mode recorded per
  instance (E31.1, real dispatch evidence); agentic paid-vs-local mechanism applying the
  recorded policy (E31.2, policy-row-cited code + real run evidence); manual mismatch
  refusal demonstrated (E31.3, this session's own live mismatch)
- ✅ Creation/HQ manual-permanence recorded normatively (E31.1, `chat-hierarchy.md`
  "Creation Chat and HQ Chat: Manual-Only, Permanently")
- ✅ No falsified model name remains in the runtime path (grep-verified clean over `bin/`);
  guard tests cover all `models:` keys (`tests/test_model_config.py`, extended through
  E31.2 and E31.3 to 15 test functions)
- ✅ The post-M31 recapture is committed with its honest comparison (PR #143, merged)
- ✅ Full suite green on `milestone/M31` @ `da7a386`: 363/0, no regressions, no new skips
- ✅ This Milestone Closure Declaration produced (`is_final: false` — M32 remains)

## Milestone Acceptance Criteria — verified

1. ✅ A working-level chat can demonstrably be started in either mode, mode recorded per
   instance; no declaration means manual (E31.1, real demonstration evidence committed)
2. ✅ Agentic mode decides paid-vs-local by applying policy rows P5–P7 (the only rows with
   a real dispatch surface, stated honestly rather than overclaiming P1–P4 coverage) — run
   evidence committed (`P9-M31-E31.2-PROVE`); `DEFAULT_MODELS` aligned; guard tests cover
   every key (E31.2)
3. ✅ A manual chat started on a mismatched model demonstrably refuses, evidence in the
   delivery; the check's instruction is present on all manual-chat template surfaces
   including HQ and Creation (E31.3) — with the honest caveat, stated in the delivery
   itself, that this is documented-instruction enforcement (agent compliance), not a
   code-level impossibility-to-proceed, since manual chats have no process wrapper to gate
4. ✅ Creation Chat and HQ Chat are normatively recorded manual-only permanent (E31.1)
5. ✅ The recapture comparison exists with the TTL caveat noted, claims checked honestly —
   "no reduction observed" reported plainly rather than shaped toward a positive result
   (milestone-level, PR #143)
6. ✅ Suite green at delivery; no regressions; no new skips (all epics + recapture; 307 →
   363 across the milestone)

## Handed to the Phase Chat

- **Consolidation:** `milestone/M31 → phase/P9` is ready for Phase Chat acceptance and
  human-authorized merge (no PR opened yet for this consolidation — the Phase Chat's own
  session should open it, per the M30 precedent's pattern of the *receiving* chat driving
  consolidation).
- **Process gap, recorded not just noted:** merge authorization for PR #142 (E31.3) was
  given directly inside the Epic Execution Chat, bypassing this Milestone Chat's Stage-2
  review at the time. The delivery held up on retroactive review, but the safety net
  didn't fire. A guard was added to the Epic Execution Chat Starter template (`8dbffe0`,
  this milestone) so a future Epic chat confirms before acting on an authorization that
  bypasses its parent's review; the same class of gap could in principle recur at
  Milestone→Phase or Phase→HQ and has not been guarded there yet — the Phase Chat may want
  to consider the same pattern for its own template.
- **M31 handoffs — measured, not left as unowned recommendations:** the post-M31
  recapture found no reduction yet in billed per-call context medians, but also found the
  *measurement itself* is not currently capable of cleanly answering the question:
  `bin/measure-token-burn` has no `--since`/time-window filter (the harness session
  directory is not append-only — sessions rotate out), and its Direction B pack cells are
  permanently pinned to the pre-E30.3 file set by E30.3's own design choice, so they can
  never show that reduction by construction. **Any future recapture attempt needs either a
  mechanism fix (a `--since` flag or a stable session-ID ledger) or a fresh, separately
  committed pack measurement in `context-scoping.md`'s own style** — rerunning the
  mechanism as-is again will not produce a cleaner answer than this one did.
- **Open gap register carried forward:** G1–G14 from M30, plus the three recapture
  findings (no `--since` filter; pinned Direction B packs; no echo-vs-reference signal) —
  none are epic-numbered gaps, all are recorded in
  `.ai-project/artifacts/reference/token-measurement/post-m31-recapture.md` §7.
- **M32 remains independent**, schedulable by the Phase Chat at its discretion, no
  dependency on M31 in either direction.
- **Unowned future work:** the mechanism fix named above (`--since` filter / stable
  session-ID ledger for `bin/measure-token-burn`) is recorded but not scheduled to any
  milestone.

---

**Milestone P9-M31 planning and delivery complete. All three Epic specs, Chat Starters,
and Epic deliveries accepted; all epic branches merged; the milestone-level Post-M31
Measurement Recapture delivered with an honest "no reduction observed" finding. M31 is not
the final P9 milestone — M32 remains, scheduled independently by the Phase Chat. Session
closes on Phase Chat consolidation of `milestone/M31 → phase/P9`.**
