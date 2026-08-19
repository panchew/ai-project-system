---
artifact_type: hq_opener
artifact_version: 1.0
timestamp: 2026-08-19T00:00:00Z
issued_by: Creation Chat
project_name: ai-project-system
repo: https://github.com/panchew/ai-project-system
governance_version: PROJECT-SYSTEM-GUIDELINES.md v2.4.0
operating_version: AI-OPERATING-GUIDELINES.md v2.10.1
framework_version: v8.0.0
active_phase: none — P11 closed 2026-08-17 at v8.0.0; P12 not yet opened
instantiation: p12-scoping
supersedes: .ai-project/artifacts/hq-openers/2026-08-01__hq-chat-opener.md
provenance: >
  Authored by the Creation Chat to instantiate an HQ Chat that opens P12. This is a
  SCOPING instantiation: the 2026-08-17 Progress Digest stated that HQ does not scope a
  phase and that P12 waits on the Creation Chat for a spine. That spine is now filed
  (SN-31), together with six further concerns and twenty-three binding decisions across
  two Steering Notes. This opener carries them. To be filed verbatim by the HQ Chat
  session it instantiates, for the artifact record.
---

# HQ Chat Opener — Project Control Room

## ⚠ Prerequisite Verification — READ BEFORE ANYTHING ELSE

Per this template and `governance/systems/chat-hierarchy.md` "Manual Chat Model Verification"
(P9-M31-E31.3): read your own harness-reported model identity and compare it to `.ai-project.yml`'s
`models.hq`. If both are present and disagree, **STOP — state the mismatch plainly and wait for
human resolution.** HQ Chat is manual-only, permanently (SN-22); it never takes an Execution Mode
declaration and never runs agentically.

- `.ai-project.yml` `models.hq` = `remote:claude-opus-5`
- **No mismatch is expected.** The Creation Chat session that authored this opener verified cleanly
  against `models.creation` on the same value on 2026-08-18.

If a mismatch nonetheless appears, it is not pre-diagnosed and is not this chat's agenda. Halt per
the rule.

## Read these first

Two committed artifacts, and nothing else is required. **You are not being asked to re-derive the
spine — it is set. You are being asked to open a phase from it.**

1. `.ai-project/artifacts/steering-notes/2026-08-18__creation-chat__steering-note__P12-spine-fail-open.md`
   — **SN-31…SN-35.** P12's spine, the fail-open finding, eleven binding decisions, ten carry-overs,
   seven Next Actions. Master `7af49f7`. **Your primary input.**
2. `.ai-project/artifacts/steering-notes/2026-08-19__creation-chat__steering-note__drivr-ux-and-model-qualification.md`
   — **SN-36/SN-37.** Drivr's MVP surface as a §7 visual binding, the model-qualification gate,
   twelve further decisions including a same-day amendment. Master `8149bce`. Discharges the first
   note's Next Action 7.

Supporting, for context rather than action:
`.ai-project/artifacts/progress-digests/2026-08-17__hq__progress-digest.md` — the outgoing HQ's P11
close-out and scoping handoff.

## Project Context

- **Project:** `ai-project-system` — the governance framework, applied to itself
- **Repository:** https://github.com/panchew/ai-project-system, branch `master`, pushed
- **Stack:** Markdown-normative corpus + Python (`bin/` tooling, `pytest`)
- **Ecosystem:** four projects — AI Project System (governance), Local Agent Runner (execution),
  AI Project System MCP (the seam), Drivr (coordination daemon, `~/soft-dev/drivr`)

## Governance

- `PROJECT-SYSTEM-GUIDELINES.md` — **v2.4.0** (effective 2026-07-31)
- `AI-OPERATING-GUIDELINES.md` — **v2.10.1** (effective 2026-08-03)
- `.ai-project.yml` → `governance.version: 8.0.0`, `ref: master`
- Released framework version: **v8.0.0** (tag)

## Current State

| | |
|---|---|
| **Phase** | none open. **P11 FULLY CLOSED** 2026-08-17 at v8.0.0 (merge `bd198c2`, closure `0408e66`) |
| **Milestone** | none |
| **Active Epics** | none |
| **Open PRs** | none |
| **Suite** | **549 passed / 0 failed**, measured on `master` 2026-08-19 |
| **Blocking concerns** | none |
| **Phases complete** | eleven |

## Objectives — P12

**The spine, in the CFO's own words:**

> *Completing what I think is my vision of the workflow, using the governance and the MVP of the
> harness (Drivr).*

**A completion phase, not a redesign** — established by evidence rather than assertion. The CFO
described his intended workflow to a chat held deliberately ignorant of this implementation; the
result was then diffed against what is built. Five levels, Stage 1 / Stage 2 epic-set authoring,
one-level escalation, per-level acceptance gates, default-accept, phase-scoped artifact lifetimes,
agentic confined to Phase/Milestone/Epic — **all matched.**

**What success looks like:** the gap between the intended workflow and the built one is closed, and
the system's default on missing evidence is no longer *proceed*.

### The organizing evidence — four verified instances of one disposition

| # | Where | Behaviour when evidence is missing |
|---|---|---|
| 1 | `bin/ai-project-orchestrator:397` | Docker absent → runs the agent's command **unsandboxed on the host** (`shell=True`) |
| 2 | `bin/ai-project-orchestrator:472` | `git add .` — stages the whole tree, not the epic's files |
| 3 | `bin/ai-project-git-merge:269-281` | Approval fails → merges anyway; ladder includes **`--admin` override**, with a test asserting it succeeds against a protected branch |
| 4 | M39's completion judgment | On absent effect evidence, **loses to a degenerate baseline that always answers "completed"** |

**Do not scope these as a defect backlog appended to the phase. They are what the phase is about.**
The CFO confirmed this reading explicitly; it is not an inference the Creation Chat is advancing
alone.

## Constraints

**Technical**

- **Agentic mode has never been integrated in any project.** The CFO: *"just doing some testing and
  measuring does not count as being using it already."* Eleven phases have built machinery for a
  mode that has not yet carried real work.
- **Sequencing constraint, binding:** the three execution-tier defects land **before the first real
  agentic integration**, not by any date. Exposure is low today *because* nothing runs agentically;
  all three go live simultaneously the moment one project does.
- Agentic dispatch is implemented at **Epic level only.** No mechanism consumes a Phase or Milestone
  agentic declaration.
- Drivr exists and coordinates: scheduler, derived gate queue, headless surface, signed
  one-time-link approval. It implements no inference of its own.

**Organizational**

- **The CFO (Layer-8) is the mandatory diff reviewer for every HQ-authored delivery** — PSG §11.6.1.
  Authorization is not review. HQ must not merge its own PR on authorization alone, and must state
  in the PR that no chat-level reviewer exists for it.
- Creation Chat and HQ Chat are manual-only, permanently (SN-22).
- **The twenty-three decisions across the two Steering Notes are inputs, not proposals.** Do not
  re-decide them.

**Explicit non-goals**

- llama.cpp and any non-Ollama local runtime — **CLOSED by CFO decision**, not parked.
- Push / WhatsApp notification — deferred.
- Sidekick-for-external-projects — a **Brief-level identity question**; no phase inherits it as an
  unstated pivot.

## Operating Rules

- HQ Chat is declarative only
- Coding Agents execute Epics
- Epic Execution Chat Starters are mandatory
- Documentation is authoritative

## Immediate Next Actions

From the Steering Notes, consolidated.

1. **Open P12 on the spine above**, carrying **`P11-GH-3`** into its opening — phase closure has no
   pre-merge completion artifact where Epic and Milestone both do, and *P12's opening is its own
   first customer.*
2. **Scope the four fail-open behaviours as the phase's organizing evidence**, with the sequencing
   constraint recorded as binding.
3. **File SN-32** (the 3-attempt rework limit reaches 1 of 8 starter surfaces and 0 templates; PSG
   has it 0 times) as a gap record in HQ's numbering, **separately** from the consolidation that
   fixes it.
4. **Action or explicitly defer SN-30's four items** (issue #192, filed 2026-08-11, actioned
   nowhere). Silence is not an acceptable disposition for a note already dropped once. **These are
   HQ's by construction — the Creation Chat holds no authority to close them.**
5. **Place the build items** — the context-exhaustion handoff artifact, Drivr's recorded mode-flip,
   and SN-37's qualification gate (with its PASS bar set as part of the work, not deferred to first
   use) — into milestones with room.
6. **Rule on `governance-propagation.md` (SN-34)** — its Constraints are factually false and three
   prohibitions rest on them. Required independently of whether governance auto-update is scoped.
7. **Scope Drivr's MVP surface from SN-36's visual binding**, with the completion-signal work as its
   prerequisite rather than a parallel track.
8. **Reconcile the two rework-limit statements** — the existing rule says the 3-attempt limit
   *"resets"* on written extension; SN-36/37's amendment grants **+1**. Two statements about one
   mechanism is the drift condition this framework exists to prevent.
9. **Correct SN-35** on the record — see below.

## Correction to SN-35, recorded here because this artifact is its evidence

SN-35 (2026-08-18) claimed that *"the framework knows how to open HQ once, at birth, and has no
defined way to be re-opened."* **That overstates the defect and is corrected here.**

**What holds:** `governance/systems/hq-chat.md`, `governance/systems/hq-execution-chat-starter.md`
and `governance/templates/hq-chat-opener.md` contain **zero** occurrences of re-instantiation or
re-opening. The normative tier is silent, as measured.

**What does not hold:** there is an established practice with **eight prior instances** in
`.ai-project/artifacts/hq-openers/`, running from 2026-06-12 to 2026-08-01, carrying a stable
`artifact_type: hq_opener`, a stable `<ISO-date>__hq-chat-opener.md` filename convention, a stable
front-matter schema, and `supersedes:` chaining each opener to the one before. **This file is the
ninth and follows it.**

**So the defect is narrower and cheaper than filed:** the practice exists and is **undocumented**,
not absent. The required action is to *record the ritual that is already being followed* — naming
the committed artifacts a re-opened HQ session receives and pointing at this directory — rather than
to design one.

**The finding survives, at lower severity, and this correction is its best evidence.** A reader
competent in the corpus searched the normative tier, found nothing, and concluded the practice did
not exist — while eight instances sat in the artifact record. An undocumented convention is one
re-instantiation away from being lost, and that is precisely the failure mode it just produced.

**The error class is `P11-GH-2`'s layer axis** — a claim verified in one tier and asserted about
another. The Creation Chat made it; the CFO caught it by expecting the file to be where it in fact
already was.
