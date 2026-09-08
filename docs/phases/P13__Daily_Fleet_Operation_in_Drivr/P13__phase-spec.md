---
phase: P13
name: "Daily Fleet Operation in Drivr"
status: scoping
start_date: 2026-09-07
planned_end_date: 2026-10-31
version: 1.0.0
---

# Phase P13 — Daily Fleet Operation in Drivr

## Executive Summary

**P12 proved the framework can do the thing it was built for, and did it exactly once.** One
epic, one project, one engine: `P1-M1-E1.1` on `panchew-io`, 111 tool rounds, 21 files changed,
instrument verdict `PASS` against a bar committed before the run it judged.

**P13's job is to make that ordinary.** The destination is the CFO's daily software development
happening *inside Drivr* — a fleet orchestrator and software factory producing steady, quality
progress across projects, at a token cost he can see and judge.

That requires four things this phase delivers and one it must not pretend:

- **Repeatability first.** `n=1` becomes `n=3` in the phase's opening milestone, on the existing
  proven path, before a pixel of new surface is built.
- **A surface that tells the truth about work nobody is watching** — where each project is, what
  it is doing, whether it is stopped, and exactly what it needs from the CFO to move.
- **Agentic reach extended from Epic through Milestone to Phase**, gated by a lever that defaults
  to off, with merge and acceptance authority left structurally out of reach.
- **Cost and quality measured together**, so "heavy context" is a funded decision rather than an
  accident.

And the thing it must not pretend: **static alignment is not operational readiness.** A validator
returning zero errors says a file parses. It says nothing about whether a run happens.

**On completion, `ai-project-system` enters maintenance mode** — but only when the CFO judges
that Drivr supports the intended operation. A closed phase does not establish that transition.

---

## Vision

Open one window. See the fleet. Every project shows its status, its progress, its exact
Phase/Milestone/Epic position, and whether it is working, stopped, or waiting. Pick one and land
where the attention belongs — with the conversation already carrying the right artifacts.

Work runs agentically as far as it can. When it cannot, it stops and **says what it needs**, in
words the CFO can act on, and he chooses **Continue → Manual** or **Continue → Agentic**. Models
change per project and per level from the interface, take effect, and survive. What the work
costs is visible next to what the work was worth.

**Visual binding** — carried forward from SN-47, which carried it from SN-36:

- **Link:** https://claude.ai/code/artifact/688a152b-df5d-4882-b48f-26108200b92c
- **What:** mockup
- **Level:** Creation
- **State:** proposed
- **Description:** The Drivr Window — fleet project selection at the left, conversational
  workspace and composer in the centre, project status and current activity at the right.
  Selection brings the human to the work needing attention with its context available.

**Interpretation, ruled:** retain the layout and workflow intent. Apply SN-47's clarifications
about Continue, model switching, and activity visibility. **The artifact's August 19
implementation commentary predates P12 and is not the P12 completion record.** The binding
establishes the experience — not a frontend framework, not a multi-user product, not a
network-hosting requirement.

---

## Governing Decisions

This phase opens under
`.ai-project/artifacts/rulings/2026-09-07__ai-project-system-hq__ruling__p13-opening-and-sn-47-triage.md`,
which consumed SN-47. **Four CFO decisions are binding and may not be reopened by the Phase
Chat:**

1. **`model_verification: blocking` is intentional.** The configured rows describe what those
   chats run on. `P12-CF-1` is closed as discharged. **The P13 Phase Chat runs on
   `remote:gpt-5.6-sol`.**
2. **Drivr receives a private git remote** before any milestone that changes Drivr code opens.
   The work stays unpublished; the acceptance chain becomes operable.
3. **Eight milestones (M48–M55)**, with repeatability proven in M48 and SN-47's M51 split.
4. **Phase/Milestone dispatch becomes representable**, gated by an eligibility lever defaulting
   to **OFF**, scoped **per-project with a fleet-wide default**. **Merge and acceptance authority
   remain unrepresentable by construction**, as does Creation/HQ manual-only (SN-22).

**Four HQ judgements are open to correction** (ruling §4): the governance-updater priority, the
adoption bar, `home_finance`'s schema resolution, and the assignment of the non-deterministic
suite to M48.

---

## Entry Conditions

**No milestone opens until these are met.** They are conditions rather than deliverables because
each one is a state the acceptance machinery depends on, and none can be accepted by that
machinery while it is unmet.

1. **Drivr has a private remote**, `master` pushed, branch protection configured to match this
   framework's expectations. Until then no Drivr epic can produce a PR, and no Stage-2 review,
   merge authorization, or CFO diff gate can operate on Drivr work. *(Blocks M50 onward; M48 and
   M49 do not change Drivr code and may proceed.)*
2. **The three fleet projects' uncommitted `.ai-project.yml` model additions are committed on
   purpose**, on their existing branches, preserving unrelated work. All three currently sit
   uncommitted on non-default branches — the precise state that produced the `panchew-io` silent
   reversion.
3. **`models.creation: gpt-6` is committed and the suite is green at 774.** *(Discharged by the
   opening ruling's own PR — verify the merge, do not redo the work.)* The opening ruling declares
   the model rows true; the committed record must agree. Verifying this uncovered that **`master`
   was red from `2ed2a48` (2026-09-07 08:44)**: the `creation` divergence guard between
   `chat-hierarchy.md`'s mapping table and `.ai-project.yml` failed, 773 passed / 1 failed against
   the 774 the P12 Progress Digest reports. The PR reconciles the table (`chat-hierarchy.md`
   v1.7.0), corrects the false provenance comment, and restores 774.

---

## Scope

### In Scope

- Operational fleet readiness for `panchew-io`, `footboard`, `home_finance`, **proven by real
  runs**, including provider-route resolution, credential-store resolution in the intended launch
  environment, governance-pin reconciliation, and `home_finance`'s schema findings.
- A cost-and-quality baseline derived **from those runs**, not synthesized.
- Prevention of credentials and sensitive information entering **future** commits.
- The Drivr Window: fleet overview, project detail, current activity.
- In-app conversational execution, intervention detection, and explicit continuation in the
  CFO's chosen mode.
- Extension of agentic dispatch from Epic through Milestone to Phase, with the eligibility lever.
- Per-project, per-level model selection from the UI that persists and takes effect.
- Token-value work grounded in the M48 baseline.
- Governance auto-update **readiness**; the complete updater as an important nice-to-have.
- Daily fleet adoption and the maintenance handoff.

### Out of Scope

- **Git-history investigation or rewriting.** The sensitive-data work protects future commits.
  No exposure has been established by any pass to date.
- **Local inference.** Parked, re-enterable. M48's measurement may generate the re-entry evidence
  without re-entering. **llama.cpp and any non-Ollama local runtime remains CLOSED**, not parked.
- **Publishing Drivr.** Decision 2 gives it a private remote and nothing more.
- **Multi-user product scope, a selected frontend framework, or network hosting.**
- **A general corpus cleanup.** The unowned carry-forwards (`P12-GH-3`, the Delivery Notice
  location split, duplicate AOG `Error Handling` content, closed-phase sweep scope,
  `P11-GH-2`, the untemplated `rulings` class) are **explicitly not absorbed** into this phase.
- **Widening authority.** "Mode is not authority" is unamended. No milestone here lets an
  unattended instance accept, merge, or authorize anything its level could not before.

---

## Milestones

**Two binding constraints:** **M48 gates M50** — no surface is built before the dispatch path is
shown to generalize; and **M50 gates M51 and M52** — the read surface exists before conversation
and dispatch extension are hung on it. **M49 is independent** of all of them and may run in
parallel from the start. M53 needs M49's configuration boundary and M51's inference/activity
contract. M54's analysis starts with M48 and compares against real UI work as it lands.

### M48 — Fleet Readiness, Proven by Running It

Static readiness *and* the run that tests it. Resolve provider routes for the configured models
in the intended launch environment, resolve the credential-store mismatch without printing
credential values, reconcile governance pins as explicit migrations against appropriate
integration baselines, and settle `home_finance`'s schema findings explicitly.

**Then dispatch a real Epic, headless, on `footboard` and on `home_finance`, through the
already-proven P12 path.** No new surface. The deliverable is the run records — including what
the framework got wrong — and `n=1` becomes `n=3`, or a named failure explains why not.

Capture the **cost-and-quality baseline from those runs**: context composition, uncached input,
cache creation and reads, output, separately reported reasoning usage, against reviewed results,
defects, rework, elapsed time, and human intervention. Missing data is named, not estimated.

**Also owned here:** SN-45's enrollment gap; verification that `panchew-io`'s `models:` block has
not reverted again; and **the non-deterministic suite where `visual_artifacts.enabled: true`** —
"suite green" is the gate every acceptance in this phase reports against.

### M49 — Future Commits Protected

Separate versioned non-secret configuration from credentials, starting with `.ai-project.yml`.
Targeted ignore changes plus detection **before** a commit, covering the human, agent, and
UI-generated change paths actually used by this operation. Synthetic credential fixtures are
caught; ordinary model updates pass; diagnostics never print secret values.

### M50 — Fleet Overview and Project Detail

The Drivr Window's read surface, built on the existing board-state and registry work (E46.2,
E46.4). All fleet projects, status, progress, exact work position, current activity; selection
opens detail and conversation context.

**`undetermined` keeps its own visible state.** Rendering it as *in progress* would be the
fail-open disposition drawn on a card — the interface asserting knowledge the system does not
have. Unknown and stale activity are visible as such. Multiple active work items stay
individually discoverable.

### M51 — Conversational Execution and Human Intervention

In-app chat against the rented execution and chat engines, with the appropriate artifacts carried
into the conversation. Intervention detection; deliberate supervision; **Continue → Manual /
Agentic** as an explicit, represented choice.

A project waiting on the CFO **states exactly what it needs to move forward**. Resume restores a
declared mode and preserves the rework counter; a newly requested mode change is represented
explicitly rather than disguised as a resume.

**Owns `P10-GH-7`** — preserving the distinction between missing evidence and a confirmed
blocker — and the remainder of **`P12-GH-4`**, narrowly: **chat text may not become an
authorization channel.**

### M52 — Level Extension and the Eligibility Lever

Make dispatch representable at Phase and Milestone, gated by the lever, **default OFF**, scoped
per-project with a fleet-wide default. Enforce it on both the dispatch and Continue paths:
enabling eligibility alone must not start or resume work. Reconcile Drivr's capability model and
its tests with the change.

**This milestone reopens a closed capability domain and must say so.** Phase/Milestone dispatch
is currently unrepresentable by construction and is a named SN-36 exemplar of *"a rule that
cannot be clicked outranks a rule that is merely written."* M52 **must re-derive and re-state
what remains closed** — merge and acceptance authority, Creation/HQ manual-only — because a
domain reopened without restating its remaining closures loses them by drift rather than by
decision.

### M53 — Model Selection That Takes Effect

Per-project, per-level model controls that write `.ai-project.yml` and keep subsequent inference
consistent with what was written. The inference-time restriction is enforced **in the backend as
well as the UI**, scoped to the selected project and level: work elsewhere does not block a
change. A failed write cannot appear successful. Unrelated config edits survive.

**Owns the `panchew-io` silent-reversion class**: onboarding, restructuring, or a governance
update must not silently replace a chosen model mapping. Make the class impossible, not merely
unrepeated.

### M54 — Token Value, on Evidence

Use M48's baseline and instrumented UI work to find avoidable context and repeated work. Compare
targeted changes against equivalent tasks under agreed, task-specific quality criteria. **Retain
expensive context where its benefit is demonstrated.**

Report raw counts and economic evidence separately; keep subscription-allowance pressure distinct
from cash cost; date any rate assumptions; avoid double-counting provider totals; record
model/provider changes so an engine change is not presented as a context saving. **No arbitrary
reduction percentage is imposed.** Does not reopen `P12-GH-5` or the parked local-inference
direction.

### M55 — Daily Fleet Adoption and the Maintenance Handoff

Recurring real development through Drivr across the fleet. Fix adoption blockers. Document
starting, stopping, recovery, and the remaining maintenance responsibilities. Verify SN-45's
enrollment gap is closed in practice.

Demonstrate governance-update readiness at the Phase-startup boundary for opt-out, no update,
update-check failure, and pending authorization. If the updater ships, also demonstrate
authorized apply, successful startup under the new version, preservation of project model
settings, and recovery from an interrupted apply **on a controlled copy first**.

---

## Success Criteria

**P13 is complete when:**

1. **Repeatability is established.** A real Epic has run agentically end to end on each of
   `panchew-io`, `footboard`, and `home_finance`, with run records, or a named and understood
   failure explains any that did not.
2. **The CFO opens Drivr and identifies active, stopped, and waiting work** without reconstructing
   status from repository files. Unknown and stale activity are visible as unknown and stale.
3. **Real chat-led work reaches an intervention, states what it needs, continues in the chosen
   mode, and reaches a reviewed delivery.** Recovery does not silently reset rework limits.
4. **Agentic eligibility off/on behaves at every supported level.** A disabled level cannot begin
   agentic work through dispatch or Continue. Enabling eligibility alone starts nothing.
5. **Model switching works repeatedly while idle**, is prevented during inference at that same
   project and level, leaves unrelated projects and levels usable, and persists — with the
   effective model matching the written one.
6. **Synthetic secret fixtures are caught before a commit** on the paths humans, agents, and the
   UI actually use; ordinary model updates pass.
7. **Token and cost evidence is sufficient for the CFO to judge the tradeoff**, tied to reviewed
   results rather than to file counts and tool rounds.
8. **Relaunch and recovery lose neither the place of work, outstanding human requests, nor
   selected models.** Any work still requiring an external tool is documented and assessed.
9. **Governance-update readiness is demonstrated at the Phase-startup boundary**, with its
   implemented coverage stated honestly. UI readiness alone is not reported as auto-update
   completion.
10. **The adoption bar is met:** two reviewed work items per pilot project and five working days
    of daily use after integration. *(HQ-adopted from SN-47's proposal; correctable.)*
11. **The CFO confirms** that Drivr supports the intended daily operation. Only then does
    `ai-project-system` enter maintenance mode: defects, security, compatibility, and governance
    changes required by real use.

---

## Repository Boundary

**Drivr owns** its client, runtime integration, activity and intervention handling, controls, and
usage display. **`ai-project-system` owns** framework rules, templates, and repository
protections needing amendment. **Fleet projects own** their own readiness changes, as explicit
changes in those repositories.

**Record and verify each delivery in the repository that contains the implementation.** This is
why Entry Condition 1 exists: five of eight milestones land primarily in Drivr, and until Drivr
has a remote, that repository cannot carry a Delivery Notice through a gate.

---

## Risks

| Risk | Disposition |
|---|---|
| **The proven path does not generalize past `panchew-io`.** | This is the phase's opening question by design (M48), not its closing one. A failure there re-scopes P13 while seven milestones of surface work are still unspent. |
| **Reopening the capability domain (M52) weakens P12's strongest guarantee.** | Ruled and bounded: lever default OFF, per-project scope, authority untouched, remaining closures re-stated as a milestone obligation. |
| **A flaky suite makes every acceptance in this phase unfalsifiable.** | Assigned to M48 rather than carried unowned. It gates everything downstream of it. |
| **The Phase Chat runs on a different model than this HQ session.** | The Phase Execution Chat Starter is written self-contained and harness-neutral. It may assume no tooling and no context beyond what it states. |
| **`undetermined` gets rendered as progress.** | Named in M50 as a fail-open drawn on a card. The completion signal P12 built is the thing the surface must not paper over. |
| **The phase absorbs a corpus cleanup by accident.** | Six unowned carry-forwards are listed in Out of Scope by name. |

---

## Reference

### Governing Rulings
- `.ai-project/artifacts/rulings/2026-09-07__ai-project-system-hq__ruling__p13-opening-and-sn-47-triage.md`
  — this phase's opening ruling
- `.ai-project/artifacts/rulings/2026-08-05__ai-project-system-hq__ruling__artifact-id-citation-forms.md`
  — the `GH-` prefix names **the phase that filed it, permanently**

### Steering Notes
| Note | Date | Carries |
|---|---|---|
| **SN-47** | 2026-09-07 | P13's direction: Drivr as the daily fleet workspace. Thirteen confirmed CFO requirements; consumed by the opening ruling |
| **SN-36** | 2026-08-19 | The Drivr Window, bound as a §7 visual; *"a rule that cannot be clicked outranks a rule that is merely written"* |
| **SN-40…SN-46** | 2026-08-27 | The baseline line-up; the switching ratchet; local inference parked, re-enterable |

### Key Reference Documents
- `.ai-project/artifacts/progress-digests/2026-09-07__hq__progress-digest.md` — P12 close-out
- `docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12__phase-closure-declaration.md`
- `governance/systems/chat-hierarchy.md` — Execution Mode; "Mode is not authority"; Manual Chat
  Model Verification
- `governance/systems/hq-re-instantiation.md` — the ritual this session opened under
- `/home/panchew/soft-dev/drivr/drivr/capabilities/model.py` — the closed capability domain M52
  reopens

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-09-07 | Initial P13 phase spec, from SN-47 and the 2026-09-07 opening ruling. **Eight milestones (M48–M55)**, amending SN-47's seven: repeatability proven in M48 rather than M54, and SN-47's M51 split into M51 (surface) and M52 (capability domain). **Three entry conditions** — Drivr's private remote, the fleet projects' uncommitted model additions, and the `models.creation` record consistency — elevated from SN-47's phase-opening agenda because the acceptance machinery depends on each. Six unowned carry-forwards named in Out of Scope so they are not absorbed. |
