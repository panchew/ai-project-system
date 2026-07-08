---
type: milestone-closure-declaration
milestone: M25
status: complete
completion_date: 2026-07-03
declared_by: Milestone Chat (P6-M25 — Process Refinements)
issued_to: Phase Chat (P6 — Visual Comprehension Layer and Process Refinements)
is_final_milestone: true
---

# MILESTONE CLOSURE DECLARATION — M25

Milestone **P6-M25 — Process Refinements** is hereby declared **COMPLETE (awaiting consolidation)**.
All epics have been executed by Coding Agents, independently verified by this Milestone Chat,
accepted under SN-13 default-accept, and merged to `milestone/M25` (HEAD `4a995e3`), with the full
test suite green (**260 passed, 1 skipped** — the lone skip is the visual-artifact endpoint
integration test at the repo default `enabled: false`; the count rose from 259 to 260 when E25.3
added `tests/test_init_agent_path.py`). **M25 is the final P6 milestone** (`is_final: true`): on
consolidation, the Phase Chat proceeds to **phase delivery** — and, fittingly, does so by following
the very phase-closure sequence M25 itself codified (E25.1's PSG §5C).

**Scope note (recorded honestly):** the milestone spec named three epics (E25.1/E25.2/E25.3). Two of
its three carry-forwards — default-accept (P6-GH-10) and the init-path alignment (P6-GH-11) — proved
to reach across far more of the framework than the spec's named-surface lists captured. M25 therefore
grew, by **Phase Chat decision at each step**, to **six** epics (E25.1–E25.6) plus **two new
carry-forwards** (P6-GH-14, P6-GH-15). Every addition was authorized, not assumed.

## Completion Verification

✅ **E25.1 — Phase-closure canonical sequence (P6-GH-12, High)** — merged to `milestone/M25`
(PR #103, merge `7571868`). Adds PSG **§5C "Phase Closure"** — an ordered, mandatory **9-step**
sequence mirroring §1A (Epic) and §5B (Milestone) one level up, with **README update (Step 3),
version bump (Step 4), and git tag (Step 8) as mandatory automatic steps** — so **no out-of-band
Steering Note** is needed to close a phase. Adds a "phase complete vs. fully closed (delivered)"
distinction, a Phase Closure Authority subsection, and the phase-closure declaration as the recorded
output — formalized as the new `governance/templates/phase-closure-declaration.md`. Reconciled §5B's
"Phase closure — future work" line to point at §5C. **PSG v2.1.0 → v2.2.0.** Verified: acceptance
recorded by reference to SN-13 only (normative codification left to E25.2 — lane held).

✅ **E25.2 — Codify SN-13 default-accept (P6-GH-10, Medium)** — merged to `milestone/M25`
(PR #104, merge `bab4659`). Adds PSG **§11.6 "Default-Accept (SN-13)"** and an AOG **§12
"Default-Accept (SN-13) — Normative"** block: **happy path** = a clean child delivery (DoD +
acceptance criteria + spec) is accepted **by silence**, no Review Decision artifact, the merge +
in-chat acknowledgment is the acceptance record; **exception path** = a Review Decision (Epic Review
Seal at Epic level) issued only when not clean. The **two-gate framing** is explicit — Layer-8 human
review is **preserved**; only the acceptance-artifact question changes. Reconciled the always-review
language in §11.5 (flow + rules, plus a duplicate rule-numbering bug fixed → 1–10), §12, §13A/§13B,
§1A (gate-scoping note; the human-review steps kept verbatim), AOG §3.6/§3.7 and lines ~728/~817;
wired §5C Step 6's pointer to §11.6. **PSG v2.2.0 → v2.3.0; AOG v2.5.1 → v2.6.0.**

✅ **E25.4 — Reconcile default-accept across reference/protocol/role/diagram docs (P6-GH-10)** —
merged to `milestone/M25` (PR #105, merge `288309c`). E25.2's Stage-2 sweep found the always-review
model woven through the *reference tier*; E25.4 reconciled all seven surfaces to §11.6/§12 (referenced,
not restated): the two `systems/*-execution-chat-starter.md`, `EPIC-EXECUTION-CHAT-STARTER.md`, the
two **hard rules** in `artifact-communication-protocol.md` ("Review Decision (Accept) MUST precede a
Delivery Notice") and `roles-authorization-team-governance.md` ("Cannot merge PR without Review
Decision (Accept)"), `diagrams/artifact-flow.md`, and `start-a-project.md`. The Review Decision
artifact, its template, and the worked **REJECT** examples were preserved (exception path). The
**Bugfix Workflow was kept as a deliberate exception** (its 4-hour Review Decision SLA is intentional
under production urgency) with a documented carve-out. Doc bumps: `artifact-communication-protocol`
**v1.0.0 → v1.1.0**, `roles-authorization` **v1.0.0 → v1.1.0**, `bugfix-epic-workflow` **v1.1.0 →
v1.2.0**; PSG/AOG **not** re-bumped.

✅ **E25.5 — Reconcile default-accept in the artifact templates tier (P6-GH-10)** — merged to
`milestone/M25` (PR #107, merge `902d765`; **human-authorized**). Reconciled the last default-accept
tier: `merge-authorization.md`, `completion-notice-epic.md`, `README.md`, and a one-line exception-path
clarifier in `epic-review-seal.md` — each referencing §11.6/§12. The **Merge Authorization artifact
and its "no merge without this authorization" force were preserved** (it is the human-authorized merge
signal §11.6 keeps; only its coupling to a *mandatory* Review Decision was reconciled). No version
bumps; PSG/AOG not re-bumped. **With E25.2 + E25.4 + E25.5, default-accept is codified and reconciled
framework-wide** (milestone acceptance criterion 4) — the only remaining "Review Decision precedes X"
statements are the **intentional exceptions**: the Bugfix Workflow and the separate CFO production
`deployment-authorization` gate.

✅ **E25.3 — Align `ai-project-init` agent path (P6-GH-11, Low)** — merged to `milestone/M25`
(PR #108, merge `bcbdb89`; **human-authorized**). Changes `bin/ai-project-init` to write the canonical,
tool-neutral **`.ai-project/agents/`** path at all three sites (L133/L327/L408) — **Option A** (no
automatic `.github/agents/` copy; the Copilot copy is a documented manual step). Adds
`tests/test_init_agent_path.py` (an end-to-end test asserting the canonical file is written and
`.github/agents/` is not — none guarded either path before; **suite 259 → 260**). Reconciled
QUICK-START and the GitHub Copilot integration guide. The `hq.agent.md`-vs-`governance.agent.md`
filename mismatch was flagged, not fixed (→ P6-GH-15).

✅ **E25.6 — Reconcile the remaining CLI-path adoption docs (P6-GH-11)** — merged to `milestone/M25`
(PR #109, merge `4a995e3`; **human-authorized**). E25.3's Stage-2 sweep found two more live guides
still claiming the CLI writes `.github/agents/`; E25.6 (documentation only) reconciled
`ADOPTION-GUIDE.md` and `docs/systems/cli-usage-guide.md` to the actual behavior (CLI writes
`.ai-project/agents/`; the Copilot copy is manual), matching E25.3's Option A framing. Grep-verified:
no live guide claims the CLI writes `.github/agents/`; the remaining mentions are Copilot
auto-detection / manual-copy references. `bin/` and `tests/` untouched (P6-GH-15 boundary respected).
**With E25.3 + E25.6, the CLI's documented path matches the script framework-wide.**

Verified on `milestone/M25` (HEAD `4a995e3`): all six epic merge commits present; every Epic spec /
Epic Execution Chat Starter / Delivery Notice committed; PSG at **v2.3.0** (§5C + §11.6), AOG at
**v2.6.0** (§12 default-accept); `bin/ai-project-init` writes `.ai-project/agents/` with a passing
test; full suite green (**260 passed, 1 skipped**). This Milestone Chat re-ran the suite and re-grepped
the reconciled surfaces before each merge rather than trusting the Delivery Notices.

## Milestone Definition of Done — all items satisfied

- ✅ E25.1, E25.2, E25.3 (and the Phase-Chat-added E25.4, E25.5, E25.6) each meet their Definition of
  Done (recorded in their Delivery Notices).
- ✅ All six epic branches merged to `milestone/M25` (PRs #103/#104/#105/#107/#108/#109).
- ✅ PSG defines a mandatory phase-closure sequence — README update, version bump, git tag (§5C, E25.1).
- ✅ AOG + PSG + the phase/milestone Execution Chat Starter templates describe SN-13 default-accept,
  the contradictory always-review language reconciled **framework-wide**, and Layer-8 human review
  preserved (§11.6 + AOG §12, E25.2; reference tier E25.4; templates tier E25.5).
- ✅ `bin/ai-project-init` writes `.ai-project/agents/`, with a test and doc agreement (E25.3 + E25.6).
- ✅ Full test suite passes on `milestone/M25` (260 passed, 1 skipped).
- ✅ This Milestone Closure Declaration produced.

## Milestone Acceptance Criteria — all satisfied

1. ✅ The phase-closure process lists README update, version bump, and git tag as mandatory steps
   (E25.1, PSG §5C).
2. ✅ AOG, PSG, and the Execution Chat Starter templates describe the SN-13 default-accept model; the
   Review Decision is documented as the exception path (E25.2; templates E25.5).
3. ✅ `bin/ai-project-init` writes `.ai-project/agents/`, asserted by a test; docs agree (E25.3 + E25.6).
4. ✅ No codified text contradicts default-accept; Layer-8 human review is preserved where mandated
   (E25.2 + E25.4 + E25.5, framework-wide; the Bugfix Workflow and the CFO production
   `deployment-authorization` gate are documented, deliberate exceptions).

## Milestone Summary

M25 is **process hygiene** — it closes three P5 carry-forwards and, in doing so, makes the written
framework match the framework as operated. **E25.1** gives phase closure the mandatory, canonical
sequence the levels below it already had (§5C), so P6's own delivery can be executed from the text
rather than by a Steering Note. **E25.2/E25.4/E25.5** codify **SN-13 default-accept** — the delivery
model in force since P5 — and reconcile the superseded always-review language everywhere it was
written, across four document tiers (normative, reference/protocol/role/diagram, templates), while
carefully **preserving** Layer-8 human review and keeping the Bugfix Workflow as a deliberate
exception. **E25.3/E25.6** point the initializer at the canonical, tool-neutral `.ai-project/agents/`
path, guard it with the framework's first test of that behavior, and align every live guide.

Two of M25's epics ran materially deeper than scoped, and the milestone's honest lesson is recorded
below: **a spec's named-surface list is a floor, not a ceiling.**

## Process Notes for Phase Chat (non-blocking)

1. **GH-8 adjacency honored.** The Phase Chat produced only the Milestone spec and Milestone Execution
   Chat Starter; this Milestone Chat authored all six Epic specs and Epic Execution Chat Starters.
   **Bookkeeping the Milestone Chat could not do itself:** the Milestone spec's epic list still reads
   E25.1/E25.2/E25.3 — the Phase Chat should **add E25.4, E25.5, E25.6** to it.
2. **Scope growth was authorized at every step.** Each epic beyond the named three (E25.4, E25.5,
   E25.6) was added by an explicit Phase Chat decision (via a scoping question), never assumed. The
   two hard-rule contradictions (protocol ordering; roles merge-gate) and the templates tier were
   surfaced by exhaustive Stage-2 sweeps, not guessed.
3. **Two new carry-forwards to record at phase level:**
   - **P6-GH-14** — the pre-existing **P4.1-vs-PSG §12 Delivery-Notice ordering** inconsistency
     (Completion → review → merge → Delivery Notice, vs. PSG §12's execution → Delivery Notice →
     review). Not a default-accept issue; surfaced during E25.4.
   - **P6-GH-15** — `bin/ai-project-init` installs the **superseded** `governance/agents/hq.agent.md`
     (its own frontmatter reads "(superseded) Use governance.agent.md") instead of the canonical
     unified `governance/agents/governance.agent.md`. A script + test + doc behavior change (also
     resolves the `hq`-vs-`governance` filename mismatch), out of M25's path-only scope. Surfaced
     during E25.6.
4. **SN-13 default-accept throughout, dogfooded.** All six deliveries were clean; no Review Decision
   artifacts were issued. This Milestone Chat accepted each by silence after an independent review.
5. **Epic-PR merges were human-authorized.** Consistent with the §11.6 model this very milestone
   codified (human-authorized merge on an Epic PR is preserved) and with the harness's "Merge Without
   Review" gate, the last three merges (E25.5, E25.3, E25.6) were explicitly authorized by the
   operator before this Milestone Chat performed them; the earlier merges (E25.1, E25.2, E25.4) landed
   under Stage-2 authority before that gate engaged. The merge facts live in the Delivery Notices, the
   merge commits, and this declaration.

None affects milestone acceptance.

## Required Action: Consolidation (and then Phase Delivery)

**To fully close this milestone, consolidation is required — this is the Phase Chat's
(milestone-level) acceptance:**

1. **Pull Request:** `milestone/M25` → `phase/P6` (long-lived **PR #102**, opened and kept current by
   this Milestone Chat).
2. **Phase Chat (P6) reviews** the consolidation PR (all M25 work present — §5C; §11.6 + AOG §12
   default-accept reconciled framework-wide; `bin/ai-project-init` canonical path + test; branch
   hierarchy correct; suite 260/1) and authorizes the milestone-level merge.
3. **Merge PR #102** — M25 lands on `phase/P6` (the milestone closure commit); then issue the Stage-2
   "Milestone Fully Closed — M25" acknowledgment with the merge SHA.
4. **M25 IS the final P6 milestone** (`is_final: true`). After consolidation, **do not branch a new
   milestone** — proceed to **P6 phase delivery** (`phase/P6 → master`, **PR #95**) **following
   E25.1's new PSG §5C sequence**: README update (retire the stale `226/226` banner to the live
   `260 passed / 1 skipped`), version bump, consolidation merge, git tag, and the phase-closure
   declaration (using the new `governance/templates/phase-closure-declaration.md`). This is the
   intended dogfood — P6 closes by the process it just codified.
5. *(Optional cleanup)* the merged epic branches `epic/P6-M25-E25.1 … E25.6` may be deleted
   (local + remote) per project policy.

---

**Declared by the Milestone Chat (P6-M25). Awaiting Phase Chat milestone-level acceptance of the
`milestone/M25 → phase/P6` consolidation PR #102. M25 makes the written framework tell the truth —
a canonical phase closure, default-accept codified and reconciled framework-wide, and a
tool-neutral initializer — and it is the last P6 milestone before phase delivery.**
