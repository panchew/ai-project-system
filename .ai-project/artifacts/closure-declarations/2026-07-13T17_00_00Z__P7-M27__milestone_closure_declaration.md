---
type: milestone-closure-declaration
milestone: M27
status: complete
completion_date: 2026-07-13
declared_by: Milestone Chat (P7-M27 — Visuals Default-On)
issued_to: Phase Chat (P7 — Agentic Execution and Default-On Visuals)
is_final_milestone: false
---

# MILESTONE CLOSURE DECLARATION — M27

Milestone **P7-M27 — Visuals Default-On (SN-17)** is hereby declared **COMPLETE (awaiting
consolidation)**. All three epics have been executed, independently re-verified by this
Milestone Chat, accepted under PSG §11.6 default-accept, and merged to `milestone/M27`; one
real regression (B4.1) found during E27.3's own due diligence has been fixed via the Bugfix
Workflow (CFO Deployment Authorization obtained) and merged. Full test suite is green
(**306 passed, 1 skipped**) on both test surfaces this milestone touches: `pytest tests/` and
`bin/ai-project-orchestrator`'s embedded `--test` suite (**18/18, `OK`**).

**M27 is milestone two of P7.** It flips visual-artifact production from opt-in/off-by-default
to default-on/opt-out per SN-17's four binding decisions, and designs the Ollama+ComfyUI
single-GPU coexistence SN-18 placed inside this milestone.

## Completion Verification

✅ **E27.1 — Default-on flip + enforcement setting (High)** — merged to `milestone/M27`
(PR #118, merge `dcfc9b6`). Flipped AOG §16 intro + §16.1, `ai-project-yml-spec.md` §3.5's
`enabled` default, and `bin/ai-project-orchestrator`'s `DEFAULT_VISUAL_ARTIFACTS`/
`resolve_visual_artifacts()` from opt-in to default-on; added the enforcement-setting key
`visual_required_for_specs` (defaulted `true`) end-to-end — schema, validation, resolution,
docs, tests. Confirmed by direct re-read: `DEFAULT_VISUAL_ARTIFACTS = {"enabled": True, ...,
"visual_required_for_specs": True}` (`bin/ai-project-orchestrator:30-35`); yml-spec's `enabled`
row now reads `Default: true`; AOG §16 opens "Visual artifacts are a **default-on** capability
(SN-17)". Confirmed `governance/agents/` and `governance/templates/` carried no opt-in language
needing reconciliation (re-verified at execution time, zero hits). **Real, load-bearing
finding recorded rather than assumed away:** the source repo's own `.ai-project.yml` keeps
`enabled: false` — not oversight, but a verified fact that `bin/ai-project-visual --type
diagrams` is itself ComfyUI-generative (not endpoint-free as the milestone spec's own framing
assumed), so flipping the source repo's config would break
`tests/integration/test_visual_artifacts_helper.py`'s skip-on-disabled behavior against a real
(absent) endpoint. Flagged as a genuine naming-collision finding for follow-up, not silently
worked around.

✅ **E27.2 — Structural-first + trigger-set behavior (High)** — merged to `milestone/M27`
(PR #119, merge `e1ccd13`). Added **AOG §16.8** "Default-on trigger policy" (confirmed present
at `governance/AI-OPERATING-GUIDELINES.md:989`): structural-first cross-referencing the
existing §16.3/§16.4 machinery, and the automatic trigger set stated verbatim — specs +
delivery/closure declarations automatic, everything else on-demand. Added a `guide` §9
restatement and, on independent audit during execution, found and closed a real gap the
milestone spec had not named: **Visual Bindings sections were missing from all four
delivery/closure templates** — added to `delivery-notice.md`, `epic-closure-notice.md`,
`milestone-closure-declaration.md`, and `phase-closure-declaration.md`, plus the guide §7
placement table extended. Confirmed via grep: no AOG/guide renumbering occurred. Together with
E27.1, the milestone-level joint acceptance criterion (fresh project, no `visual_artifacts`
block, produces structural visuals for a new spec by default) is satisfied.

✅ **E27.3 — Ollama+ComfyUI coexistence design (Medium)** — merged to `milestone/M27`
(PR #120, merge `6d04c08`). Delivered `governance/guides/gpu-coexistence.md` (confirmed
present, 8275 bytes), naming the exact contention this Milestone Chat's own audit of
`~/soft-dev/ai-stack/docker-compose.yml` confirmed (`count: all` GPU reservations on both
`ollama` and `comfyui`, plus a further detail beyond the milestone spec's own grounding: both
services are `restart: unless-stopped`, so the contention window persists across host reboots
rather than being opt-in per session). The chosen mitigation reuses existing,
already-implemented machinery rather than adding new infrastructure: `bin/ai-project-visual`
now checks the orchestrator's own PID-based execution lock (via `bin/ai-project-daemon`'s
pre-existing `check_execution_locked()`/`check_pid_alive()`, re-pointed at the orchestrator's
own `LOCK_FILE` to avoid a latent path-mismatch) and refuses a generative ComfyUI call cleanly
with a new **exit code 5** when a live agentic epic run holds the lock. Confirmed present:
`EXIT_LOCKED = 5` at `bin/ai-project-visual:55`. Neither the orchestrator nor the daemon was
modified — a reuse, not a new subsystem. 3 new tests (locked/live, locked/stale, unlocked)
against a deliberately unreachable port so the tests never flake against a real `ai-stack`
ComfyUI instance. **Flagged, not fixed (correctly, out of E27.3's own file scope): the
orchestrator's embedded `--test` suite had 2 pre-existing failures from E27.1's default-on
flip** — this became B4.1 (below), not silently absorbed into E27.3's own scope.

## B4.1 — Bugfix found during E27.3, resolved via the Bugfix Workflow

E27.3's own due-diligence run of `python3 bin/ai-project-orchestrator --test` (a second,
embedded unittest suite distinct from `pytest tests/`) surfaced 2 failures —
`test_visual_artifacts_absent_is_disabled` / `test_visual_artifacts_absent_block_is_disabled`
— still asserting E27.1's **pre-flip** default. Root cause: an undiscoverable-by-`tests/`-grep
duplicate of the equivalent `tests/test_visual_artifacts_config.py` assertions, which E27.1 had
correctly rewritten — the embedded copy was invisible to both E27.1's own grounding and this
Milestone Chat's own merge verification (both used the same `tests/`-scoped grep). CFO chose
the Bugfix Workflow over a new E27.4 or an escalation. **B4.1 spec authored** (severity `low`,
target branch `milestone/M27` per the defect's own location — a documented deviation from the
workflow's default `master`-based shape), then **dispatched, fixed, reviewed (explicit Review
Decision — bugfixes are never silence-accepted, per the workflow's deliberate carve-out from
default-accept), CFO Deployment-Authorized, and merged** (`bugfix/B4.1 → milestone/M27`, merge
`b46d7be`). Both suites re-verified green post-merge by this Milestone Chat directly:
`pytest tests/` (306 passed, 1 skipped) and `python3 bin/ai-project-orchestrator --test`
(18/18, `OK`). B4.1 is closed (`docs/bugfixes/B4.1__spec__orchestrator-embedded-test-suite-stale-default.md`,
`status: closed`).

Verified on `milestone/M27` (HEAD `e4d20d3`): all three epic merge commits present
(`dcfc9b6`/`e1ccd13`/`6d04c08`, confirmed via `git merge-base --is-ancestor`); the B4.1 merge
(`b46d7be`) present; every Epic spec / Epic Execution Chat Starter / Delivery Notice, the
bugfix spec, and the Completion Notice / Review Decision / Deployment Authorization / Delivery
Notice chain for B4.1 all committed; `governance/guides/gpu-coexistence.md` present; AOG §16.1
and §16.8 both present and correctly worded; `visual_required_for_specs` present in schema,
validation, and resolution; full suite green on both test surfaces. This Milestone Chat
independently re-ran both suites and re-read the affected source files directly (not trusting
Delivery Notices alone) before this declaration.

## Milestone Definition of Done — all items satisfied

- ✅ E27.1, E27.2, and E27.3 each meet their Definition of Done (recorded in their Delivery
  Notices and independently re-verified above).
- ✅ All three epic branches merged to `milestone/M27` (PRs #118/#119/#120).
- ✅ AOG §16.1 describes default-on/opt-out; the enforcement setting (`visual_required_for_specs`)
  exists and defaults true.
- ✅ `resolve_visual_artifacts()` resolves an absent block to enabled, structural-first.
- ✅ The automatic trigger set (specs + delivery/closure) and on-demand path are codified
  (AOG §16.8).
- ✅ A documented Ollama+ComfyUI coexistence design (`governance/guides/gpu-coexistence.md`)
  addresses the confirmed GPU contention.
- ✅ A fresh project with no `visual_artifacts` block produces structural visuals for a new
  spec; `visual_artifacts.enabled: false` cleanly opts out.
- ✅ Full test suite passes on `milestone/M27` — **both** `pytest tests/` (306/1) and the
  embedded `--test` suite (18/18), the latter only green because of B4.1's fix.
- ✅ This Milestone Closure Declaration produced.

## Milestone Acceptance Criteria — all satisfied

1. ✅ A fresh project with no `visual_artifacts` block still produces structural visuals for a
   new spec (default-on, structural-first) — jointly satisfied by E27.1 + E27.2.
2. ✅ Setting `visual_artifacts.enabled: false` cleanly opts out (E27.1) — and the source repo's
   own use of this exact opt-out, for a real documented reason (the generative-helper
   naming-collision finding), is itself a live proof of the opt-out path working correctly.
3. ✅ The enforcement setting is present, defaulted true, and documented (E27.1).
4. ✅ The automatic trigger set (specs + delivery/closure only; everything else on-demand) is
   codified as a normative rule (E27.2, AOG §16.8).
5. ✅ A documented Ollama+ComfyUI coexistence design is present and addresses the confirmed
   `count: all`/no-partitioning/`restart: unless-stopped` contention (E27.3).

## Milestone Summary

M27 turned SN-17's four ratified decisions into the framework's actual default behavior, and
did it with real findings surfacing along the way rather than a clean pass papered over:
E27.1 discovered the source repo's own config couldn't simply flip (a genuine naming
collision between a documentation-time assumption and the generative helper's actual
behavior), E27.2 found and closed a real template gap the milestone spec hadn't named, E27.3
found a reuse path that avoided new infrastructure entirely, and E27.3's own due diligence
caught a real regression (B4.1) that both E27.1's delivery and this Milestone Chat's own merge
verification had missed the first time — because both used the same blind spot (a
`tests/`-scoped grep that cannot see an embedded duplicate suite). That regression is now
fixed, reviewed, CFO-authorized, and merged.

## Process Notes for Phase Chat (non-blocking)

1. **GH-8 adjacency honored.** The Phase Chat produced only the Milestone spec and Milestone
   Execution Chat Starter; this Milestone Chat authored all three Epic specs and Epic
   Execution Chat Starters.
2. **B4.1 is a real instance of the "same blind spot in two places" failure mode** — worth
   the Phase Chat/CFO's attention: any surface with a `tests/`-external duplicate test suite
   (are there others?) is invisible to grep-based grounding *and* to merge verification that
   only runs `pytest`. Not fixed here beyond B4.1 itself — flagging the pattern, not claiming
   to have swept for more instances.
3. **The source-repo `.ai-project.yml` `enabled: false` decision is a live acceptance-criterion
   proof, not a loose end** — it demonstrates the opt-out path works, for a genuine reason
   (the generative-helper naming collision), and is documented in the file itself.
4. **This milestone required no cross-repo coordination** — unlike M26, there was no
   escalation-to-HQ path exercised.

## Required Action: Consolidation (then M28 or further HQ direction)

**M27 is not fully closed until:**

1. **Pull Request:** `milestone/M27 → phase/P7` (long-lived **PR #117**, open and mergeable).
2. **Phase Chat (P7) reviews** the consolidation PR (all three epics + B4.1 present; suite
   306/1 on both test surfaces) and authorizes the milestone-level merge.
3. **Merge PR #117** — M27 lands on `phase/P7`; then issue the Stage-2 "Milestone Fully
   Closed — M27" acknowledgment with the merge SHA.
4. **M27 is not the final P7 milestone** (`is_final: false`). M28 (4 epics, per SN-19's E28.4
   amendment) may proceed per the phase spec's own "may parallel M27" note — now unblocked
   either way, since M27 is closing.
5. *(Optional cleanup)* the merged epic branches `epic/P7-M27-E27.1 … E27.3` and
   `bugfix/B4.1` (already deleted locally) may be cleaned up per project policy.

---

**Declared by the Milestone Chat (P7-M27). Awaiting Phase Chat review and milestone-level
acceptance of the `milestone/M27 → phase/P7` consolidation PR #117.**
