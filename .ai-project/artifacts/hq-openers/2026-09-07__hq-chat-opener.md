---
artifact_type: hq_opener
artifact_version: 1.0
timestamp: 2026-09-08T05:01:10Z
issued_by: Creation Chat
project_name: ai-project-system
repo: https://github.com/panchew/ai-project-system
governance_version: PROJECT-SYSTEM-GUIDELINES.md v2.9.0
operating_version: AI-OPERATING-GUIDELINES.md v2.12.0
framework_version: v9.0.0
active_phase: none — P12 closed at v9.0.0; P13 not yet opened
instantiation: p13-scoping
supersedes: .ai-project/artifacts/hq-openers/2026-08-19__hq-chat-opener.md
provenance: >
  Authored and filed by the Creation Chat at the human's request for an HQ handoff.
  Carries the human's P13 direction in SN-47, with its unaccepted planning proposals
  explicitly preserved, and the latest HQ Progress Digest. This opener instantiates
  an HQ discussion; it does not authorize phase execution or ratify draft proposals.
---

# HQ Chat Opener — Project Control Room

## Prerequisite Verification — before any HQ work

HQ Chat is manual-only, permanently (SN-22). It never takes an Execution Mode declaration
and never runs agentically. Read your own harness-reported model identity and compare it
with the current `.ai-project.yml` value of `models.hq`. If both are present and disagree,
**STOP, state the mismatch plainly, and wait for human resolution.**

Use [Manual Chat Model Verification](../../../governance/systems/chat-hierarchy.md) for the
mapping, self-report limits, and absent-block/absent-key permissive default. Do not infer an
exact model identity from the application name or from the identity of the authoring chat.
At preparation, the configured HQ expectation is `remote:claude-opus-5`; read the current
file before proceeding.

This opener follows the [HQ Chat Re-instantiation Ritual](../../../governance/systems/hq-re-instantiation.md).

## Read these first

1. **Unconsumed agenda:** [SN-47 — P13 daily fleet operation](../steering-notes/2026-09-07__creation-chat__steering-note__P13-daily-fleet-operation__draft.md).
   The human's requirements are distinguished from **[PROPOSED — confirm]** planning advice.
   The note retains `status: draft`; committing it preserves the record, not acceptance of
   its proposed milestones, thresholds, or unresolved choices. Read it by reference; the
   human need not paste it separately.
2. **Latest close-out:** [September 7 HQ Progress Digest](../progress-digests/2026-09-07__hq__progress-digest.md).
   P12 is closed. Its open decisions and carry-forwards remain input to this session.

The human has supplied P13's central objective below. Do not ask HQ to invent a new one or
reconstruct this discussion from a transcript. Use the notes' linked evidence only as needed
for the decision being made; the opener does not require loading the entire artifact corpus.

## Project Context

- **Project:** `ai-project-system`, the governance framework applied to itself.
- **Repository:** https://github.com/panchew/ai-project-system; local checkout
  `/home/panchew/soft-dev/ai-project-system`.
- **Existing stack (repository record):** Markdown governance and Python tooling/tests.
  Drivr implementation is in `/home/panchew/soft-dev/drivr`; a UI stack has not been selected
  by this Creation Chat.
- **Human-selected initial fleet:** `panchew-io`, `footboard`, `home_finance`.

## Governance

- [PROJECT-SYSTEM-GUIDELINES.md](../../../governance/PROJECT-SYSTEM-GUIDELINES.md): **v2.9.0**.
- [AI-OPERATING-GUIDELINES.md](../../../governance/AI-OPERATING-GUIDELINES.md): **v2.12.0**.
- Source `.ai-project.yml`: `governance.version: 9.0.0`, `ref: master`.
- Released framework: **v9.0.0**. Initial-fleet projects still declare older versions;
  adding models did not upgrade their governance.

## Current State

**Recorded baseline:** the digest and [P12 Closure Declaration](../../../docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12__phase-closure-declaration.md)
record P12 fully closed, seven milestones M41–M47 and thirty-two epics delivered, and
**774 passing tests** at close-out. That is historical validation, not a test run by this
opener's author. No P13 phase, milestone, or epic is opened by this handoff.

P12 proved one real Drivr Epic run on `panchew-io`. It does not establish repeated daily use
across the fleet or agentic progression through Milestone and Phase. SN-47 records the
implementation inspection and its limits.

**Fleet preparation already performed with human authorization:** all seven selected model
keys were added to the three fleet configurations. Those sibling changes are uncommitted.
SN-47 records the exact lineup, validation, branches, and preservation of existing work.
Remaining readiness findings include:

- `home_finance` has pre-existing schema errors (missing description and an underscore in
  its project-name slug), plus two pre-existing warnings. No rename was authorized.
- Governance pins remain at 7.1.0 for `panchew-io` and 7.0.0 for the other two projects.
- Provider routing and authenticated operation in the intended launch environment remain
  unverified; cached catalog entries do not establish access. The credential-directory
  mismatch needs resolution without printing credentials.

The source repository also has a human's uncommitted configuration edit. Preserve it and
read current values; the digest's earlier model-verification state is historical.

## Objectives — P13

The human's central objective is **to move daily software development into Drivr**, a fleet
orchestrator and software factory that produces steady, quality progress.

Confirmed requirements in SN-47 cover:

- A fleet overview showing status, progress, exact work location and activity, with project
  detail and an explicit statement of what the human must supply when work is waiting.
- Conversation inside Drivr; agentic execution as much as possible, extending through
  Milestone to Phase; manual supervision and **Continue → Manual / Agentic** choices.
- A lever controlling whether a level may run agentically.
- Repeated per-project/per-level model changes from the UI, persisted to `.ai-project.yml`,
  prevented during inference at the same project and level.
- Token expense evaluated alongside output quality, and prevention of future sensitive-data
  commits. Heavy context is acceptable when its contribution justifies the cost.
- Readiness for governance auto-update. Once Drivr runs independently, `ai-project-system`
  enters maintenance mode.

**Visual success:** carry SN-47's hosted visual binding into the Phase artifact cascade:

- **Link:** https://claude.ai/code/artifact/688a152b-df5d-4882-b48f-26108200b92c
- **What:** mockup
- **Level:** Creation
- **State:** proposed
- **Description:** The Drivr Window: fleet selection, conversational workspace/composer,
  project status and current activity. Interpret it alongside the human's newer requirements;
  its August implementation commentary is not the P12 completion record.

## Constraints

- Creation and HQ remain manual-only. Extending execution mode does not extend authority.
- Confirmed requirements are human input; marked proposals are not accepted by transmission.
  In particular, M48–M54 and the two-work-items/five-working-days bar are provisional.
- The human has not selected a frontend stack, hosting model, or a multi-user product scope.
- Preserve chosen models and unrelated changes when preparing fleet governance migrations.
- The requested sensitive-data work concerns future commits, not Git-history investigation
  or rewriting. This planning pass has not established an exposure.
- The digest records Drivr as local-only by human decision and local inference as parked.
  Carry those dispositions forward; resolve any needed publication/recovery change explicitly.
- Enter maintenance only after the human judges that Drivr supports the intended operation.

## Operating Rules

- HQ is declarative; coding agents execute Epics under mandatory Epic Execution Chat Starters.
- Documentation is authoritative; acceptance and unresolved choices remain explicit.
- Prior rulings carried by the digest are constraints, not fresh unconsumed agenda. Consult
  their cited records where necessary; do not revive superseded opener assumptions.
- A Phase Execution Chat Starter must reference an existing Phase spec. Creation's planning
  draft is not a substitute for either artifact or an execution authorization.

## Immediate Next Actions

**[PROPOSED — confirm] Receiving-session agenda:**

1. After model verification, acknowledge the supplied P13 objective and triage SN-47 against
   the P12 digest. Record the distinction between confirmed requirements and proposed scope.
2. Resolve with the human the lever's project/fleet scope, full updater's completion priority,
   candidate milestone boundaries, and adoption evidence threshold. Record further design
   choices from SN-47's opening-decisions section at the appropriate planning level.
3. Give the digest's carry-forwards explicit dispositions. Place fleet/schema/governance and
   provider readiness findings into the agreed work, without representing static alignment
   as operational readiness.
4. Once scope is accepted, produce the P13 Phase spec and Phase Execution Chat Starter under
   the normal HQ process. Preserve the hosted visual binding and identify repository owners.
   Let the Phase Chat finalize milestone planning within that contract.

This artifact is the HQ session opener. It does not itself open P13, approve the candidate
milestones, authorize a merge, or start agentic work.
