# Milestone Execution Chat Starter — P13-M48

**Milestone:** P13-M48 — Fleet Readiness, Proven by Running It
**Phase:** P13 — Daily Fleet Operation in Drivr
**Project:** ai-project-system
**Repository:** `/home/panchew/soft-dev/ai-project-system` (https://github.com/panchew/ai-project-system)
**Milestone Spec:** `docs/phases/P13__Daily_Fleet_Operation_in_Drivr/P13-M48__milestone-spec.md`
**Branch:** `milestone/M48` (from `phase/P13`)
**Execution Mode:** manual
**Issued:** 2026-09-08

> Cite the Milestone spec by path and branch. Do not stamp a moving spec version or commit SHA into
> child starters; amendments are discovered from the committed branch history.

---

## Governance References

You are operating under the AI Project System governance framework as a **Milestone Chat**.

**Authoritative governance documents:**
- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) v2.9.0 (Effective: 2026-09-03)
- [AI-OPERATING-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/AI-OPERATING-GUIDELINES.md) v2.12.0 (Effective: 2026-09-03)

**Governance hierarchy:** PSG → AOG → this Starter → M48 spec → session decisions → system
references → chat. The P13 opening ruling's four CFO decisions are incorporated into this Starter
and the Phase spec and remain settled; neither this session nor a child may reopen them.

**Critical rules:**

- Documentation is authoritative; chat is ephemeral.
- **Stage 1:** produce Epic specs and Epic Execution Chat Starters, commit them, and open a PR.
  **Stage 2:** oversee delivery, accept a clean delivery only through an in-chat acknowledgment
  naming the party that reviewed and accepted (role + session identity; silence accepts nothing),
  and merge only after all gates and explicit human merge authorization.
- Produce only direct-child planning artifacts. Do not implement code, tests, migrations, registry
  changes, or runs yourself.
- You report to the P13 Phase Chat. Do not reach across to sibling milestones or phases.
- If merge authorization arrives directly in this chat rather than after the parent Phase Chat's
  Stage-2 review, state the bypass and confirm the human intends it before proceeding. A child never
  holds merge authorization. Mode is not authority.
- Rejected delivery rework is limited to three attempts. A written extension grants exactly one
  additional attempt, not a reset. On exhaustion, require an Escalation Notice and hand back to the
  Phase Chat.
- Mid-flight direction changes travel through an amended governing spec with a changelog entry.
  Notify running children to re-read it; do not patch direction through chat alone.

**Context scoping:**

- At start, load this Starter and the full M48 spec. From the P13 Phase spec load the M48 entry,
  success criteria, repository boundary, and risks only.
- Load the PSG/AOG sections required by the template's per-level context-scoping standard. Load
  triggered closure, escalation, review, visual, and error-handling sections before acting on those
  situations.
- Do not load sibling Milestone specs or governance changelogs.

---

## Prerequisite Verification

### Model verification

This instance is manual. Read the harness-reported model identity and compare it with the live
`.ai-project.yml` `models.milestone` value. `model_verification` is `blocking`. If both identities
are present and disagree, stop before planning or review, state the mismatch plainly, and wait for
the Phase Chat/human. Follow `governance/systems/chat-hierarchy.md` "Manual Chat Model
Verification" for absent-key and absent-self-report handling.

### Spec and branch

Before planning, verify the spec is tracked on the expected parent branch:

```bash
git -C /home/panchew/soft-dev/ai-project-system show phase/P13:docs/phases/P13__Daily_Fleet_Operation_in_Drivr/P13-M48__milestone-spec.md >/dev/null
```

If the spec is absent, untracked, incomplete, or ambiguous, stop and report to the P13 Phase Chat.
Do not fill gaps by assumption.

### Re-measure the operational baseline

The M48 spec records planning-time findings, not execution-time truth. Before writing the relevant
Epic spec, re-measure and record repository/ref/date for:

- Drivr's current adapter, scheduler eligibility behavior, and no-code-change boundary;
- `footboard` and `home_finance` fleet-registry status;
- each project's branch/worktree state, governance pin, installed agent, model block, and remote;
- `home_finance`'s exact validator findings;
- source-suite live visual behavior; and
- the raw P12 run-event fields used by the proposed baseline.

Do not inspect credential values. Presence and effective path category are the maximum permitted
credential evidence.

---

## Milestone Context

**Milestone number:** P13-M48
**Milestone name:** Fleet Readiness, Proven by Running It
**Milestone spec:** `docs/phases/P13__Daily_Fleet_Operation_in_Drivr/P13-M48__milestone-spec.md`

**Governance versions:**
- PROJECT-SYSTEM-GUIDELINES.md: v2.9.0
- AI-OPERATING-GUIDELINES.md: v2.12.0
- Released framework: v9.0.0

**Epics:**

- **E48.1 — Operational Evidence and Run Gate**
- **E48.2 — Deterministic Acceptance, Live Qualification Separate**
- **E48.3 — Enrollment Completes the Delivery Substrate**
- **E48.4 — Footboard Readiness and Real Epic Run**
- **E48.5 — Home Finance Disposition and Real Epic Run**
- **E48.6 — Fleet Cost-and-Quality Baseline**

**Ordering:** E48.1, E48.2, and E48.3 may be planned independently. E48.4 and E48.5 require
E48.1's accepted evidence/quality contracts, E48.2's accepted deterministic gate, explicit fleet
eligibility, and a real parent-governed project Epic. E48.6 requires both attempts and independent
reviews.

**Session objective:** produce one complete Epic spec and one Epic Execution Chat Starter for each
Epic, one set at a time, and return each committed set to the P13 Phase Chat for named review and
acceptance before proceeding.

---

## Findings Every Epic Spec Must Preserve

Carry only the findings relevant to that Epic, but do not lose these boundaries across the set:

1. Static validation is not operational proof. M48 exists to run the path.
2. `remote:deepseek-v4-flash` is a model identity, not the executable OpenCode provider route.
3. Credential-store diagnostics are presence-only. Never load or print credential values.
4. Both required targets were benched at planning time. Eligibility requires explicit authority;
   neither this Starter nor enrollment grants it.
5. The proven path invokes Drivr's `OpenCodeAdapter.execute`; raw `opencode run` alone is not the
   required proof.
6. M48 authorizes no Drivr implementation. If new machinery is required, escalate.
7. `footboard` has dirty in-flight planning work. Use an isolated worktree and preserve it.
8. `home_finance` may not be silently renamed. Every validator finding needs a disposition.
9. Usage must be paired with independently reviewed quality. Missing telemetry is unavailable,
   never estimated or zero-filled.
10. `undetermined`, missing evidence, credential absence, provider unavailability, authenticated
    resource refusal, and a confirmed blocker remain distinct.
11. A named, understood failure can satisfy the attempt requirement; it cannot be hidden as `n=3`
    or automatically open M50.
12. `panchew-io`'s P12 run is retained as the first run. M48 verifies its model block and normalizes
    only what its raw evidence supports.

---

## Epic Planning Requirements

### E48.1 exhaustion ruling and one final attempt

The P13 Phase Chat resolved E48.1's exhausted-rework Escalation Notice on 2026-09-08 by amending
the M48 spec at `## Phase Ruling on E48.1 Rework Exhaustion`. **Read that section in full before
touching E48.1.** Its five decisions are fixed: source-repository bar ownership; source-graph
dispatch-manifest ancestry plus runtime dispatch time; exact source-side OpenCode tool mapping and
authoritative `files_changed`; immutable commit-permalink proposed visual; and bounded quarantine
hardening under the fixed XDG state root.

The same ruling grants a written PSG §11.6 **`+1` extension: exactly one final E48.1 planning
attempt, not a reset.** Reissue the E48.1 spec and Starter from the amended parent contract and
return only that set. E48.2/E48.3 remain paused until E48.1 receives named acceptance. This grant
does not authorize E48.1 execution or any merge. If the final delivery is not acceptable, stop and
escalate; no further rework attempt exists.

### E48.1 — Operational Evidence and Run Gate

- Commit the normalized record contract and task-specific quality bars before either run.
- Test complete, partial, and missing telemetry without double-counting provider totals.
- Specify an adapter-level replay/invocation, executable route selection per attempt, presence-only
  credential check, raw-event retention, and independent work/quality review.
- Specify how explicit fleet eligibility authority is recorded; do not grant it.
- Re-measure `panchew-io` model persistence and extract only supported P12 baseline fields.

### E48.2 — Deterministic Acceptance, Live Qualification Separate

- Separate deterministic acceptance from live ComfyUI qualification without silently deleting,
  mocking, or skipping the live check.
- Require explicit pass/fail/skip semantics and endpoint available/unavailable/opt-out coverage.
- Make every delivery report deterministic suite totals and live qualification independently.

### E48.3 — Enrollment Completes the Delivery Substrate

- Close SN-45 in the supported initialization path with remote present, absent, failure, and
  intentional local-only coverage.
- Keep remote enrollment distinct from fleet activation and dispatch.
- Never create, store, or print credentials.

### E48.4 — Footboard Readiness and Real Epic Run

- Make this an `ai-project-system` proof-and-coordination Epic, not a parent of `footboard` work.
  Its record and Delivery Notice land on `epic/E48.4`; all project changes and the selected real
  Epic remain under `footboard`'s own hierarchy.
- Route cross-project direction through a System HQ request/response and, when routed onward, a
  steering note to `footboard` HQ. Routing never commands and never accepts project work.
- Name the owning repository and branch boundaries. Start from an explicitly selected integration
  baseline in an isolated worktree; do not touch the dirty checkout.
- Plan a real v7.0.0-to-v9.0.0 governance migration, not a version-string edit.
- Select an Epic already present in `footboard`'s accepted Milestone plan. Require its current spec,
  Starter, and parent acceptance before dispatch.
- Require explicit human authority for the benched-to-eligible transition.
- The run subject is agentic, but its governing Epic Chat is manual. Preserve raw run evidence and
  obtain independent project review.

### E48.5 — Home Finance Disposition and Real Epic Run

- Make this an `ai-project-system` proof-and-coordination Epic, not a parent of `home_finance`
  work. Its schema-disposition record, run record, and Delivery Notice land on `epic/E48.5`; project
  changes and the selected real Epic remain under `home_finance`'s own hierarchy.
- Route cross-project direction through System HQ and into `home_finance` HQ for triage. Routing
  never commands and never accepts project work.
- Require explicit disposition of the missing description, underscore/name rule, and two warnings.
  A rename requires separate human authorization and recorded supersession. The alternative is a
  filed schema finding against the rule; M48 does not amend the source schema.
- Name the integration baseline and preserve active project work during the v7.0.0-to-v9.0.0
  migration.
- E1.1 is already delivered and may not be replayed. Select a remaining Epic already listed in the
  accepted M1 plan, and require its own current spec, Starter, and parent acceptance before dispatch.
- Require explicit human authority for the benched-to-eligible transition.
- The run subject is agentic, but its governing Epic Chat is manual. Preserve raw run evidence and
  obtain independent project review.

### E48.6 — Fleet Cost-and-Quality Baseline

- Recompute normalized evidence from raw events and project commits; do not trust executor prose.
- Report context/usage/economic dimensions beside review result, defects, rework, elapsed time, and
  intervention for every project.
- Make task/model/provider/context differences and all unavailable fields visible.
- End with a bounded `n=3` or named-failure conclusion and state whether the evidence supports
  opening M50. The P13 Phase Chat makes the gate decision.

---

## Repository and Delivery Boundaries

M48 spans repositories. Each Epic spec and Starter must state where implementation, evidence,
branch, PR, tests, and Delivery Notice live.

- `ai-project-system`: all six M48 Epic specs, records, and Delivery Notices; implementation for
  E48.1, E48.2, and E48.3; consolidated baseline for E48.6.
- `footboard`: project-side migration and real project Epic only, under `footboard`'s hierarchy;
  raw evidence may be referenced from the M48 record but project delivery remains there.
- `home_finance`: project-side migration/configuration and real project Epic only, under
  `home_finance`'s hierarchy; raw evidence may be referenced from the M48 record but project
  delivery remains there.
- Drivr: execution dependency only. M48 makes no Drivr code change.

Do not claim one repository's suite covers another. E48.4 and E48.5 commit only their M48 records
and Delivery Notices to `ai-project-system`; they do not merge target-project branches. Project-side
changes and product Epics use each target's own canonical review, PR, and parent-merge chain.
Cross-project direction uses the System HQ request/response and routed steering-note channel. If
that chain is unavailable or cannot represent the required work safely, escalate before dispatch.

---

## Output Requirements

For each Epic, in order of acceptance rather than bulk production:

1. A complete Epic spec covering goals/scope, Definition of Done, deliverables, dependencies,
   repository/branch boundary, verification, and acceptance criteria.
2. A filled Epic Execution Chat Starter using the current template, with `Execution Mode: manual`
   for the supervising chat and an explicit distinction where the run subject is agentic.

Write each Starter after its Epic spec is committed. Cite the spec by path and branch, not version
or SHA. Commit each set to `milestone/M48`, hand it off by reference under AOG §3.1.1, and request
P13 Phase Chat review. Do not echo artifact bodies into chat.

Every child Starter must carry the relevant secret boundary, independent-evidence rule, repository
boundary, rework limit, and no-Drivr-code escalation trigger. E48.4/E48.5 must also carry the dirty
work/integration-baseline rule and explicit eligibility prerequisite.

---

## Epic Acceptance and Merge Instruction

There is no ceremonial Delivery Authorization artifact on the clean path. The P13 Phase Chat
accepts an Epic planning set through an in-chat acknowledgment naming the party that reviewed and
accepted; silence accepts nothing. A Review Decision is the exception path only.

Standing merge instruction: merge each accepted `epic/E48.#` branch to `milestone/M48` only after
Epic completion, parent acceptance, and explicit human merge authorization. The parent performs the
merge. For project-side work, preserve the owning project's hierarchy and do not redirect a project
Epic branch into this repository.

Do not proceed to execution or merge without parent acceptance.

---

## Completion Requirements

- [ ] Epic spec and Starter accepted for all six Epics
- [ ] Each acceptance acknowledged in chat with the reviewing party named
- [ ] Cross-repository branch, PR, test, and evidence destinations are explicit
- [ ] The Phase Chat has declared M48 planning complete

Then declare: "Milestone P13-M48 planning complete. All Epic specs and Chat Starters accepted.
Session closed."

---

## Question Policy

- Ask only blocking questions.
- Do not add Epics, widen M48 into UI/dispatch-extension work, or absorb unowned carry-forwards.
- Escalate before: granting project eligibility; renaming `home_finance`; selecting a synthetic
  proving task; modifying Drivr; reading credential values; inventing missing telemetry; or
  treating a named failure as permission to open M50.
- Resolve other ambiguities against the M48 spec first, then the P13 Phase spec. The incorporated
  CFO decisions from the P13 opening ruling remain settled and may not be reopened.
