# MILESTONE EXECUTION CHAT STARTER — P4-M19: Creation Chat Completion and Bugfix Workflow

MANDATORY CONTEXT PACKET

Project: ai-project-system
Phase: P4 — Team Collaboration and Artifact-Driven Communication
Milestone: M19 — Creation Chat Completion and Bugfix Workflow
Governance: PROJECT-SYSTEM-GUIDELINES.md and AI-OPERATING-GUIDELINES.md enforced
Base branch: `milestone/M19` (branched from `phase/P4` at commit `16aa8f7`)
This is the FINAL milestone of Phase P4.

MILESTONE OVERVIEW

**Goal:** Close Phase P4 by delivering the two remaining success criteria:
1. **E19.1 — Bugfix Workflow:** HQ Chat bugfix handler, Deployment Authorization artifact,
   SLA tracking, post-mortem template, phase spec update to v1.3.0
2. **E19.2 — Creation Chat Ongoing Artifacts:** Steering Note schema, Progress Digest
   schema, Bouncer Work log, re-instantiation ritual

When both epics merge to `milestone/M19` and the consolidation PR merges to `phase/P4`,
Phase Chat opens the `phase/P4 → master` PR and Phase P4 closes.

**Dependencies:** M18 ✅ (`governance/templates/genesis.md` present, Creation Chat Level 0
defined in `chat-hierarchy.md`)

BRANCH HIERARCHY

```
phase/P4  (HEAD: 16aa8f7)
└── milestone/M19           ← this branch
    ├── epic/P4-M19-E19.1   ← Bugfix Workflow (dispatch first)
    └── epic/P4-M19-E19.2   ← Creation Chat Ongoing Artifacts (may run in parallel)
```

---

## STAGE 1 — Verify Planning Artifacts and Authorize Execution

Before dispatching either Epic, confirm the following are present on `milestone/M19`:

```bash
ls docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4-M19*
```

Expected files:
- [ ] `P4-M19__milestone-spec.md`
- [ ] `P4-M19-E19.1__spec__Bugfix_Workflow.md`
- [ ] `P4-M19-E19.2__spec__Creation_Chat_Ongoing_Artifacts.md`
- [ ] `P4-M19-E19.1__epic-execution-chat-starter.md`
- [ ] `P4-M19-E19.2__epic-execution-chat-starter.md`
- [ ] `P4-M19__milestone-execution-chat-starter.md` (this file)

If any planning artifact is missing: **do not dispatch** — escalate to Phase Chat.

If all present: proceed to Stage 2.

---

## STAGE 2 — Oversee Epic Execution

### Dispatch Order

1. **Dispatch E19.1 first** (phase spec update must land before M19 closes)
2. **Dispatch E19.2** — may run in parallel once E19.1 is underway; no hard dependency

### Dispatching E19.1

Open a new Epic Execution Chat using:
```
docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4-M19-E19.1__epic-execution-chat-starter.md
```

Agent works on `epic/P4-M19-E19.1` and opens a PR to `milestone/M19` when done.

### E19.1 Review Checklist

When E19.1 Completion Notice arrives:

- [ ] `docs/bugfixes/README.md` present with B#.# naming convention
- [ ] HQ Execution Chat Starter has "Handling Production Issues" section with all six
  steps (evaluate → spec → commit → authorize → SLA → escalate)
- [ ] `governance/templates/deployment-authorization.md` has correct YAML schema and
  filled example
- [ ] `governance/templates/post-mortem.md` present and referenced in
  `governance/systems/bugfix-epic-workflow.md`
- [ ] SLA (4-hour window, escalation on miss) documented in bugfix workflow
- [ ] `docs/roadmap/overview.md` P4 milestones M14–M18 marked complete
- [ ] `pytest` present in project dependencies
- [ ] `P4__phase-spec.md` version is 1.3.0; M19 consolidated; M20 removed;
  Two-Stage Lifecycle deferred note present; M19 marked as final P4 milestone
- [ ] `governance/templates/README.md` updated with new templates
- [ ] All existing tests pass

### Dispatching E19.2

Open a new Epic Execution Chat using:
```
docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4-M19-E19.2__epic-execution-chat-starter.md
```

Agent works on `epic/P4-M19-E19.2` and opens a PR to `milestone/M19` when done.

### E19.2 Review Checklist

When E19.2 Completion Notice arrives:

- [ ] `governance/templates/steering-note.md` present; YAML schema matches
  `.ai-project/artifacts/steering-notes/2026-06-19__creation-chat__steering-note.md`
- [ ] `governance/templates/progress-digest.md` present with four required sections
  (Phase Status, Open Decisions, Next Actions, Blocking Concerns)
- [ ] `governance/templates/bouncer-work-log.md` present; 2-minute fill test passes
  (reviewer can fill a sample entry in under 2 minutes)
- [ ] `governance/systems/creation-chat-guide.md` present with all four re-instantiation
  steps (before reset, what to include, how to re-open, what the new session receives)
- [ ] `tests/test_ongoing_artifacts.py` present; schema validation tests pass
- [ ] 2026-06-19 reference Steering Note validates against the new schema test
- [ ] `governance/templates/README.md` updated with three new entries
- [ ] All existing tests pass

### Issuing Review Decisions

Use `governance/templates/review-decision.md` for accept or reject decisions.

**Accept:** All DoD items satisfied, checklists above pass, tests green.

**Reject:** State specific failing DoD items; request targeted rework. Maximum 3
rejection cycles per Epic before escalating to Phase Chat.

### Authorizing Merges

After each Accept Review Decision, the agent opens a PR (`epic/P4-M19-E19.x → milestone/M19`).
Authorize the merge using `governance/templates/merge-authorization.md`, then the agent
merges.

---

## MILESTONE CLOSURE

After both epics are merged to `milestone/M19` and all DoD items are verified, produce
the Milestone Closure Declaration and commit it to `milestone/M19`:

```markdown
---
type: milestone-closure-declaration
milestone: M19
status: complete
completion_date: <YYYY-MM-DD>
declared_by: Milestone Chat (P4-M19 — Creation Chat Completion and Bugfix Workflow)
issued_to: Phase Chat (P4 — Team Collaboration and Artifact-Driven Communication)
---

# MILESTONE CLOSURE DECLARATION — M19
...
```

**Closure checklist:**
- [ ] E19.1 merged to `milestone/M19`
- [ ] E19.2 merged to `milestone/M19`
- [ ] Full test suite passes on `milestone/M19`
- [ ] All DoD items from milestone spec satisfied
- [ ] `P4__phase-spec.md` is at v1.3.0

Then open PR: `milestone/M19 → phase/P4` and forward the Closure Declaration to
Phase Chat for review and merge authorization.

---

## PHASE P4 CLOSURE (for Phase Chat awareness)

After Phase Chat merges M19 to `phase/P4`:

1. Phase Chat opens PR: `phase/P4 → master`
2. Phase Chat produces Phase P4 Delivery Notice
3. HQ Chat issues Phase Accept
4. PR merges to `master`
5. Phase P4 is complete

This Milestone Chat session ends when the Closure Declaration is forwarded to Phase Chat.

---

## ESCALATION PATH

Escalate to Phase Chat via `governance/templates/escalation-notice.md` when:

- A planning artifact is missing and execution is blocked
- An Epic is rejected 3 times and the agent cannot resolve the issue
- An out-of-scope finding arises that requires Phase Chat decision
- The DoD requires information only Phase Chat can supply

---

## REFERENCE

- **Milestone Spec:** `P4-M19__milestone-spec.md`
- **E19.1 Spec:** `P4-M19-E19.1__spec__Bugfix_Workflow.md`
- **E19.2 Spec:** `P4-M19-E19.2__spec__Creation_Chat_Ongoing_Artifacts.md`
- **E19.1 Starter:** `P4-M19-E19.1__epic-execution-chat-starter.md`
- **E19.2 Starter:** `P4-M19-E19.2__epic-execution-chat-starter.md`
- **Phase Spec:** `P4__phase-spec.md` (v1.2.0; E19.1 updates to v1.3.0)
- **Governance Templates:** `governance/templates/` (all current templates present
  as of M17–M18: merge-authorization, review-decision, escalation-notice, genesis,
  epic-closure-notice)
- **Reference Steering Note:** `.ai-project/artifacts/steering-notes/2026-06-19__creation-chat__steering-note.md`
- **Next:** Phase Chat merge authorization → `phase/P4 → master` PR → P4 complete
