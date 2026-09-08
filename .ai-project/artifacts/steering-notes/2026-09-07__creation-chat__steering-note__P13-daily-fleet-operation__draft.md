---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-09-07T16:23:15Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
framework_version: 9.0.0
status: draft
concerns:
  - id: SN-47
    severity: high
    title: "[PROPOSED — confirm] P13 — Drivr as the daily fleet workspace"
decisions:
  - "Move the human's daily software-development operation into Drivr as the fleet orchestrator and software factory, producing steady, quality progress across projects."
  - "Use agentic execution as much as possible; switch to manual for blockers or when the human chooses to supervise. The human chooses how to continue through Manual and Agentic options."
  - "Show the fleet, each project's status and progress, its exact phase/milestone/epic position, and whether it is working, stopped, or waiting for the human. Selection reveals details and current activity."
  - "Conversations happen inside Drivr. A project waiting for intervention states exactly what it needs from the human to move forward. Continue's relationship to Send message remains open."
  - "Allow repeated model changes from the UI per project and level, updating that project's .ai-project.yml. Reasoning/inference at that same project and level prevents the change; activity elsewhere does not."
  - "Judge token expense against the quality of results. Heavy governance context is acceptable when justified; excessive context is a hypothesis to investigate, not an established finding."
  - "Prevent credentials and other sensitive information from entering future commits, including through .ai-project.yml; consider appropriate .gitignore changes."
  - "Once Drivr can run independently, ai-project-system enters maintenance mode."
  - "Extend Drivr's agentic execution from the proven Epic level through Milestone to Phase, implementing the allowance already present in governance."
  - "Include a lever controlling whether a governance level is allowed to run agentically."
  - "Governance auto-update is important, and Drivr must be prepared to handle it. Required P13 delivery versus nice-to-have priority remains to be settled."
  - "The initial fleet is panchew-io, footboard, and home_finance. Check their models blocks for alignment before execution."
  - "Use the shared ai-project-system lineup for all three initial-fleet projects: Creation GPT-6, HQ Claude Opus 5, Phase GPT-5.6 Sol, Milestone DeepSeek V4 Pro, and Epic Dev/QA/manual DeepSeek V4 Flash."
---

# P13 planning draft — Drivr as the daily fleet workspace

## Purpose

The human has asked to plan P13 after P12 proved that Drivr can perform real work. The destination
is daily software development inside Drivr across the fleet, with steady progress and quality
results at a justified token cost.

**Draft for human review.** The decisions below capture what the human said in this session.
Everything marked **[PROPOSED — confirm]** is planning advice, including the milestone boundaries,
evidence requirements, and transition bar. This draft does not open P13 or authorize execution.
The human carries the accepted direction to HQ through this artifact.

## Decisions Already Made

These are the human's stated requirements; their appearance here does not confer governance
authority on the Creation Chat.

1. **Destination:** move daily software-development work into Drivr, the fleet orchestrator and
   software factory. Its purpose is steady, quality progress across projects.
2. **Operating pattern:** work agentically as much as possible. Turn to manual when blocked or
   when the human elects to supervise. The human chooses **Continue → Manual** or
   **Continue → Agentic**.
3. **First screen:** show which projects belong to the fleet; each project's status and progress;
   its exact phase, milestone, or epic; and whether it is working, stopped, or waiting. Selecting
   a project reveals details and what it is doing, including building or inferring.
4. **Interaction:** chat inside Drivr, as in this conversation. When waiting for the human, state
   exactly what is needed to move forward. The relationship between Continue and Send message is
   undecided.
5. **Models:** selection is per project and per level, repeatable from the UI, and updates the
   corresponding value in `.ai-project.yml`. A change is prevented only while that same project
   and level is reasoning/inferring. Work at other projects or levels does not prevent it.
6. **Token value:** make an informed decision about consumption and result quality. Governance
   may be context-heavy; heavy context is acceptable if its contribution justifies its cost.
   There is no established quality-result baseline yet. The work should produce results others
   can recognize as quality.
7. **Secret prevention:** protect future commits from credentials and sensitive information,
   including accidental entries in `.ai-project.yml`. Consider `.gitignore` changes. The human
   clarified that the concern is preventive, rather than a request to investigate Git history.
8. **Transition:** once Drivr runs independently, `ai-project-system` enters maintenance mode.
9. **Agentic coverage:** extend the working Epic execution path through Milestone to Phase in
   P13. The human confirmed this direction as the next extension of the modes governance
   already permits.
10. **Agentic eligibility lever:** provide a control over whether a governance level is allowed
    to run agentically. Whether each setting applies to a single project or the fleet is still
    being clarified.
11. **Governance auto-update:** the human raised this as another important requirement/nice-to-have
    and said Drivr must be ready when it takes effect. Its final P13 completion priority remains
    open.
12. **Initial fleet:** `panchew-io`, `footboard`, and `home_finance`, selected by the human. The
    human also requested checking their model blocks for alignment before execution.
13. **Initial model lineup:** the human accepted the shared lineup below for all three projects
    and authorized applying it through this harness.

### [PROPOSED — confirm] Initial-fleet configuration check and alignment

Initial read-only snapshot of the selected projects on 2026-09-07, before model alignment.
Both the working configuration and `HEAD:.ai-project.yml` were checked; none of these
configuration files had uncommitted changes at that point. The table records the pre-change
state; the application result below records what changed afterward.

| Project | Checkout inspected | `models:` in working file and HEAD | Declared governance | `framework_version` |
|---|---|---|---|---|
| `panchew-io` | `milestone/M1` at `e892b69` | Absent | `7.1.0`, ref `v7.1.0` | Absent |
| `footboard` | `chore/framework-v7.0.0-bump` at `b00bb16` | Absent | `7.0.0`, ref `v7.0.0` | `v7.0.0` |
| `home_finance` | `epic/E1.1` at `2d316d5` | Absent | `7.0.0`, ref `v7.0.0` | `v7.0.0` |

All three configurations also omitted `model_verification`. Absence of a model block establishes
that no explicit project lineup is recorded; it does not by itself prove that no harness could
run using defaults. No provider authentication or inference was exercised in this check.

**Human-selected common starting lineup**, copied from the current `ai-project-system` working
configuration and applied to all three initial-fleet projects. Availability and quality are
not established by the configuration change:

```yaml
models:
  creation: remote:gpt-6
  hq: remote:claude-opus-5
  phase: remote:gpt-5.6-sol
  milestone: remote:deepseek-v4-pro
  epic_dev: remote:deepseek-v4-flash
  epic_qa: remote:deepseek-v4-flash
  epic_manual: remote:deepseek-v4-flash
```

**Application and verification result:** all seven entries were added to each project's
`.ai-project.yml` on its existing branch. Byte comparisons against staged candidates and parsed
comparisons verified that unrelated fields and comments were preserved. These are uncommitted
working-file changes. Existing `footboard` planning changes were preserved. No governance pin,
adoption stamp, provider credential, or `model_verification` setting was changed.

The source repository's `bin/ai-project-validate` reported:

| Project | Full-config result after the model addition | Comparison with before |
|---|---|---|
| `panchew-io` | 0 errors, 0 warnings | No new findings |
| `footboard` | 0 errors, 0 warnings | No new findings |
| `home_finance` | 2 errors, 2 warnings | All four findings pre-existed; no model findings |

`home_finance`'s errors are the missing `project.description` and the underscore in
`project.name` (the schema requires a hyphenated/lowercase slug). Its warnings concern
`governance.submodule_path` and `project.created_at`. Resolve its identity/schema mismatch
explicitly during readiness work rather than silently renaming the project during model
alignment. The installed governance checkouts are still `bb727a5` for `panchew-io` and
`8044451` for the other two, matching the old pins recorded above.

**Catalog and launch-environment check:** the local OpenCode model catalog cache contains
`opencode/claude-opus-5`, `openai/gpt-5.6-sol`, and both `opencode/` and `opencode-go/` routes
for `deepseek-v4-pro` and `deepseek-v4-flash`. It has no exact `gpt-6` model entry. The latter
is the human-selected Creation identity matching this harness's self-report; it must not be
silently replaced with a differently named model or passed to OpenCode as a proven route.
Creation remains manual. Catalog membership is not evidence of authenticated access.

The inherited `XDG_DATA_HOME` does not point at the normal host data directory: an OpenCode
credential file is absent at that inherited location and present at the normal host location.
Only existence was checked; credential values were not read. This matches the environment
hazard documented in E47.1. No inference or authenticated provider test was run by this check.

Keep model identity and provider routing distinct. Drivr's adapter at `114de1c` passes the
request's model directly to OpenCode. [E47.1's recorded route](../../../docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12-M47-E47.1__record__remote-agentic-dispatch.md)
was `opencode/deepseek-v4-flash`; the project value `remote:deepseek-v4-flash` does not select
that provider route by itself. Readiness must resolve the chosen model to the actual execution
route and check it in the intended launch environment. The record's inherited credential-store
resolution issue also belongs in that check, without printing credential values.

The lineup selection, application, and static validation are complete. Remaining readiness
work includes actual provider/launch resolution and the existing `home_finance` schema issues.
Treat governance-version alignment as an explicit migration: inspect the installed agent and
current work boundary before moving the pin. The current checkouts are an active milestone,
a governance-bump branch with uncommitted planning work, and an epic branch respectively.
Prepare isolated upgrade changes against the appropriate integration baselines; do not achieve
apparent adoption by editing only version strings or overwrite that work.

## Visual Success

The human selected **The Drivr Window** as the UI reference for moving daily work into Drivr.

**Visual binding**
- **Link:** https://claude.ai/code/artifact/688a152b-df5d-4882-b48f-26108200b92c
- **What:** mockup
- **Level:** Creation
- **State:** proposed
- **Description:** Fleet project selection on the left; conversational work and composer in the
  center; project status and current activity on the right. Selection brings the human to the
  work needing attention with its context available.

**[PROPOSED — confirm] Reference interpretation:** retain the layout and workflow intent, and
apply this session's clarifications about Continue, model switching, and activity visibility.
The artifact's August 19 implementation commentary predates P12; use the current records below
for implementation status. Propagate the hosted binding into the phase and relevant UI specs.

## Concerns for HQ Triage

### SN-47 — P13: Drivr as the daily fleet workspace [HIGH — PROPOSED — confirm]

**Detail:** the human wants to move daily development across the fleet into Drivr. The required
experience includes an informative fleet overview, conversational work, agentic execution,
human intervention and explicit continuation, free model selection when the affected level is
idle, justified token expense, and prevention of sensitive-data commits.

**[PROPOSED — confirm] Required action:** scope P13 around delivering and using this experience.
Use the candidate milestones below to prepare the HQ handoff and Phase Chat work. Give each
requirement an observable completion criterion and identify the repository that owns its change.

### [PROPOSED — confirm] Planning baseline and remaining gaps

This is a source-grounded planning interpretation, not a new acceptance of the underlying work.

| Evidence read | Implication for P13 |
|---|---|
| [P12 Closure Declaration](../../../docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12__phase-closure-declaration.md) and [September 7 Progress Digest](../progress-digests/2026-09-07__hq__progress-digest.md): closed at v9.0.0; one real epic on `panchew-io`, 111 tool rounds, 21 changed files, instrument `PASS`. | Reuse the working dispatch path. One run establishes a starting point; recurring daily operation across the fleet still needs demonstration. |
| [E46.2 delivery](../../../docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12-M46-E46.2__delivery-notice.md): board-state computation and Markdown rendering. [E46.4 delivery](../../../docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12-M46-E46.4__delivery-notice.md): control models. | These are components to integrate into the requested interactive UI. Their delivery alone does not demonstrate that UI. |
| Local Drivr inspected at `114de1c`, clean working tree: `drivr/surface/app.py` exposes approval GET/POST routes; `drivr/capabilities/model.py` permits dispatch only at Epic. | The conversational fleet client and wider unattended execution require explicit work. Creation and HQ remain manual-only under the Seed. |
| At the same Drivr ref, `drivr/scheduling/scheduler.py` documents that an `UNDETERMINED` outcome is journalled without escalation. The digest carries the narrower missing-block-detector gap as `P10-GH-7`. | Build trustworthy activity and intervention handling. A claimed queue item alone must not become evidence that reasoning is currently happening; uncertainty needs its own visible state. |
| [P9 token audit](../reference/token-measurement/audit-report.md): historical consumption data and cache-sensitive cost analysis exist. The human's two screenshots show large contexts and allowance pressure on later sessions. | Reuse the measurement work, refresh it for today's providers and workflow, and add result-quality evidence. Do not reuse historical prices as current prices or equate gross token count with spend. |
| Working `.ai-project.yml` currently has `creation: remote:gpt-6` and `model_verification: blocking`; the digest describes an earlier deferral of blocking verification. | Preserve the human's current edit. Reconcile current configuration, actual runtime identity, and UI selection rather than applying the digest's historical state as a configuration change. |

### [PROPOSED — confirm] Candidate milestones

The numbers **M48–M54 are provisional planning labels**, following P12's M47. HQ and the Phase
Chat should finalize ownership and decomposition after human acceptance. No dates or effort
estimates are claimed before the integration gaps are assessed.

| Candidate | Outcome and scope | Demonstration required |
|---|---|---|
| **M48 — Fleet readiness and cost/quality baseline** | Verify readiness of the selected initial fleet: panchew-io, footboard, and home_finance. Use the applied model lineup, resolve actual provider/launch routing and home_finance's existing schema findings, and reconcile governance adoption. Measure context composition, token use, and available cost data for representative work; agree task-specific quality criteria before comparisons. | A readiness record for every selected project and a reproducible baseline tying usage to a task, project, level, model/provider, reviewed result, and rework. Missing data is named. |
| **M49 — Prevent sensitive-data commits** | Audit current configuration and files likely to be committed, starting with `.ai-project.yml`. Separate versioned non-secret configuration from credentials; make targeted ignore changes and add detection before commits, covering human, agent, and UI-generated changes. | Synthetic credential fixtures are caught before a commit; ordinary model updates pass; diagnostics do not print secret values. The normal commit paths used by this operation are exercised. |
| **M50 — Fleet overview and project detail** | Implement the referenced window around the existing board/registry data. Show all fleet projects, status, progress, exact work position, and current activity; selecting a project opens its detail and conversation context. | The human opens Drivr and identifies active, stopped, and waiting work without reconstructing status from repository files. Multiple active work items remain individually discoverable. Unknown or stale activity is visible. |
| **M51 — Conversational execution and human intervention** | Integrate in-app chat with the rented execution/chat engines, carry the appropriate artifacts into the conversation, detect cases needing intervention, and support deliberate supervision and Continue choices. Extend agentic dispatch and progression from Epic through Milestone to Phase, as confirmed by the human. Include the lever controlling whether each level may run agentically. | Real work demonstrates execution at Epic, Milestone, and Phase, reaches an intervention, states what the human must provide, continues in the human's chosen mode, and reaches a reviewed delivery. A level with agentic eligibility disabled cannot begin agentic work; enabled eligible levels can. Completion uncertainty is preserved. |
| **M52 — Model selection that takes effect** | Provide per-project, per-level model controls; write the selected key in `.ai-project.yml`; keep actual subsequent inference consistent with it. Enforce the inference-time restriction in the backend as well as the UI, scoped to the selected project and level. | Repeated idle switches take effect; a switch racing inference at that same project/level is prevented; unrelated projects/levels remain usable; a failed write cannot appear successful; unrelated config edits survive. |
| **M53 — Improve token value with evidence** | Use M48's baseline and instrumented UI work to identify avoidable context and repeated work. Compare targeted changes against equivalent tasks using the agreed quality criteria. Retain expensive context where its benefit is demonstrated. | Report input, output, cache use where exposed, available cost/allowance evidence, completion, review findings, rework, and human intervention. Each retained change has evidence supporting its quality/cost tradeoff. No arbitrary token-reduction percentage is imposed. |
| **M54 — Daily fleet adoption and maintenance handoff** | Use Drivr for recurring real development across the agreed fleet roster, complete the rollout, fix adoption blockers, and document starting, stopping, recovery, and the remaining maintenance responsibilities. | The human can use Drivr as the normal development workspace over the agreed observation period. Every fleet project is visible and its operational readiness is explicit. The human reviews the evidence and decides whether independent operation has been reached. |

**[PROPOSED — confirm] Sequence:** start M48 and M49 first. M50 can proceed once the initial
readiness and data-contract findings are available. Build M51 on that usable overview. M52 needs
M49's configuration boundary and M51's inference/activity contract. Start M53's analysis with
M48 and compare changes as real UI work becomes available. Complete M54 after the integrated
workflow is usable; do not defer the first real UI-driven task to the end of the phase.

**[PROPOSED — confirm] Repository boundary:** Drivr owns its client, runtime integration,
activity/intervention handling, controls, and usage display. `ai-project-system` owns the
framework rules/templates and repository protections that need amendment. Readiness changes in
fleet projects remain explicit changes in those projects. Record and verify delivery in the
repository that contains the implementation.

### [PROPOSED — confirm] Governance auto-update readiness

Treat readiness for governance updates as part of the P13 integration work, with delivery of
the complete automatic updater an important nice-to-have pending the human's priority decision.
Readiness requires demonstrated behavior at the phase-start integration boundary; it does not
establish that an updater has shipped.

**Existing direction to carry forward:** [the August 18 Steering Note, Carry-Over 9](2026-08-18__creation-chat__steering-note__P12-spine-fail-open.md)
records opt-in updates run by Drivr at **Phase Chat start only**, authorized by the human and HQ
through the existing gate queue and signed-link mechanism. It describes applying an approved
update, moving the governance pin, and advancing `framework_version` only once roll-forward
completes. An unsuccessful update check leaves the existing version in use. One phase runs under
one governance version. The [P12 phase spec](../../../docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12__phase-spec.md)
separates the updater from the larger installation reconciler and leaves partial-apply failure
and treatment of immutable artifacts unresolved. This planning pass has located that direction;
it has not demonstrated an operational auto-update path.

**Proposed placement within the seven milestones:**

- **M48:** identify each pilot project's installed governance version/pin, verify the existing
  update mechanism and compatibility expectations, and record which parts are implemented.
- **M51:** integrate the update lifecycle with Phase startup and the existing authorization
  controls. Make pending human input, an update in progress, its result, and recovery needs
  understandable in the UI. Do not change a running phase's governance version.
- **M52:** make governance-update and model-setting writes coexist. Preserve the human's model
  selections, agentic-eligibility settings once defined, and unrelated project configuration;
  do not let an update or install silently restore old defaults.
- **M54:** demonstrate the integration boundary for opt-out, no update, update-check failure,
  and a pending authorization. If the updater is delivered, also demonstrate authorized apply,
  successful startup under the new version, and recovery from an interrupted/failed apply on a
  controlled copy before using it on pilot work.

**Proposed failure behavior to resolve with HQ and the human:** distinguish a failed *check*
from a partially completed *apply*. A failed check keeps the existing version. An apply that
leaves inconsistent state pauses phase startup and presents the recovery action needed; startup
resumes only from a verified consistent version. Preserve historical artifacts, using separate
supersession/annotation records for immutable decisions rather than rewriting or deleting them.
These recovery semantics are proposals addressing the prior open questions.

Repair of arbitrary broken installations remains a separately scoped reconciler concern. If
the complete updater is deferred, record the supported manual update path and the integration
work delivered; do not report auto-update completion from UI readiness alone.

### [PROPOSED — confirm] Decisions to resolve during phase opening

These are gaps in the plan, not requests to repeat requirements already supplied by the human.

1. **Implement the confirmed agentic coverage.** The human has accepted execution through
   Milestone and Phase; coverage itself is settled. Wire the dispatch/progression mechanisms
   for the modes governance already permits, and reconcile Drivr's current capability model
   and tests with those mechanisms. Creation/HQ stay manual-only; execution mode does not grant
   review or merge authority. Finalize the implementation boundaries and evidence per level.
   The new lever controls eligibility within that permitted range. Define its project/fleet
   scope, persistence, defaults, and handling of a change while work is running. Enforce it on
   dispatch and Continue paths; enabling eligibility alone should not start or resume work.
2. **Mode transitions.** Define the target instance of Continue and voluntary supervision.
   Specify what happens when the human requests manual control during a running tool action.
   Existing resume restores a declared mode and preserves the rework counter; a newly requested
   mode change must be represented explicitly rather than disguised as that resume. Positioning
   Continue beside or apart from Send message remains a UI decision.
3. **Free model choice and existing gates.** The human has settled when model switching is
   allowed. Preserve that freedom. Reconcile qualification and identity-verification rules so
   they cannot add an unintended approval or qualification prerequisite to each valid idle
   change. Keep qualification evidence useful for choice and quality measurement. Define how
   an existing conversation continues under its new model and how model IDs resolve to a
   provider route, without exposing credentials in versioned configuration.
4. **Daily-use environment.** Settle the supported launch/client environment and verify readiness
   of the selected initial fleet (`panchew-io`, `footboard`, `home_finance`). The roster is settled.
   The UI reference establishes the experience, not a frontend framework, multi-user product,
   or network-hosting requirement.
5. **Publication/recovery.** The digest records Drivr as local-only by a prior human decision.
   Resolve how the daily workspace is recovered and how implementation changes are reviewed;
   do not silently create a remote or treat local-only as an accidental defect.
6. **Governance auto-update priority and recovery.** Confirm whether the complete updater is
   required for P13 completion or remains an important nice-to-have alongside demonstrated
   integration readiness. Resolve partial-apply failure handling and immutable-artifact
   annotation before enabling automatic application.

### [PROPOSED — confirm] Cost and quality measurement

Measure the context actually supplied: governance, task/artifact context, conversation history,
tool responses, and harness/skill overhead where attribution is possible. Report both raw
counts and economic evidence, keeping uncached input, cache creation/reads, output, and separately
reported reasoning usage distinct. Avoid double-counting provider totals. Subscription allowance
pressure and cash/API cost are separate measurements; use provider records where available and
date any rate assumptions.

Associate those measurements with reviewed results: whether task-specific acceptance criteria
were met, defects found, rework required, elapsed time, and human intervention. File counts and
tool rounds establish activity, not sufficient evidence of quality. Compare similar work and
record model/provider changes so a task or engine change is not presented as a context-saving
effect. Report uncertainty where the provider does not expose enough attribution.

Use the historical P9 mechanism as an input. Establish this phase's baseline before claiming a
benefit from trimming governance. Numeric cost targets can be chosen after that measurement,
consistent with the human's willingness to fund context that earns its cost.

### [PROPOSED — confirm] Phase completion and maintenance transition

Use the human-selected initial fleet: **panchew-io, footboard, and home_finance**. Require
**two reviewed work items per pilot project** and **five working days** of daily use after
integration. The project selection is confirmed; these evidence thresholds remain proposals.
Record readiness for each project and extend rollout beyond the initial fleet as agreed with
the human.

For the demonstration, cover:

- Fleet overview and accurate work/activity locations, including stopped/waiting/unknown cases.
- Real chat-led work, a genuine human intervention, voluntary supervision, and explicit
  continuation in each supported mode. Recovery does not silently reset rework limits.
- Agentic eligibility off/on at each supported level: disabled levels cannot start agentic
  execution through dispatch or Continue; enabling eligibility alone does not initiate work.
- Model switching while idle, rejection during inference at the same project/level, concurrent
  unrelated work, and persistence of the chosen configuration and effective model.
- Prevention of synthetic secret commits through the paths actually used by humans and agents.
- Reviewed outputs and token/cost evidence sufficient for the human to judge the tradeoff.
- Relaunch/recovery without losing the place of work, outstanding human requests, or selected
  models; any work still requiring an external tool is documented and assessed with the human.
- Governance-update readiness at Phase startup, with its implemented coverage stated. If the
  updater ships, verify consistent version transitions, recorded authorization, preservation of
  project model settings, and the agreed failure/recovery behavior.

Enter maintenance only when the human confirms Drivr supports the intended daily operation.
Proposed maintenance scope for `ai-project-system`: defects, security, compatibility, and
governance changes needed by real use. A closed phase alone does not establish that transition.

## Carry-Over Open Items

**Agentic eligibility lever:** its purpose is confirmed: control whether a level may run
agentically. Its project/fleet scope is awaiting the human's clarification; defaults, persistence,
and treatment of already-running work remain design details to settle explicitly.

**[PROPOSED — confirm]** Triage the digest's carry-forwards against the daily-use objective:

- Address `P10-GH-7` through M51's activity/intervention work, preserving the distinction between
  missing evidence and a confirmed blocker. Connect the relevant remainder of `P12-GH-4` to
  the conversational handoff without making chat text an authorization channel.
- Handle SN-45's enrollment gap and the reported `panchew-io` model-config reversion in M48/M52;
  onboarding or restructuring must not silently replace a chosen model mapping.
- Reconcile `P12-CF-1` with the current configuration and the new selection workflow. Preserve
  this session's intentional local model/verification edits.
- Address live-visual test nondeterminism where it undermines credible P13 acceptance evidence.
  Name the environment and any intentionally skipped live integration separately.
- Give an explicit disposition to `P12-GH-3`, the untemplated `rulings` artifact class, the
  `P11-GH-2` sibling-pattern question, the Delivery Notice location split, duplicate AOG content,
  and closed-phase sweep scope. Do not silently absorb a general corpus cleanup into the UI work.
- Keep local inference parked, including `P12-GH-5`'s recorded disposition, and preserve the
  previously closed non-Ollama runtime direction unless the human changes it. Token measurement
  here examines the current workflow; it does not reopen that runtime decision.
- Git-history investigation or rewriting is outside this proposed phase scope. The requested
  repository work protects future commits. No exposure has been established by this planning pass.

## Next Action

The human requested the framework's HQ Chat Opener for this handoff. Use the
[P13 HQ Chat Opener](../hq-openers/2026-09-07__hq-chat-opener.md), which carries this note as
unconsumed agenda and the latest Progress Digest as the P12 baseline. This note remains a
draft: recording and handing it off does not accept the marked proposals or open P13.

**[PROPOSED — confirm]** Resolve the lever's project/fleet scope, governance auto-update's
completion priority, candidate milestones, and adoption bar with the human in the receiving
HQ session before authorizing the affected scope. The initial fleet, its applied model lineup,
and agentic execution through Milestone and Phase are already confirmed. Carry the remaining
readiness findings above into the phase-opening work.

HQ should then:

1. Record the accepted P13 direction and resolve the opening decisions above, including any
   changes to existing rules needed to implement the human's confirmed choices.
2. Produce the Phase Execution Chat Starter using this direction, the P12 closure/digest,
   and the hosted UI binding. Keep the implementation status distinct from the August 19 vision.
3. Have the Phase Chat verify the current baseline, finalize milestone scope/owners, and begin
   readiness, token measurement, and future-commit protection before the adoption run.
