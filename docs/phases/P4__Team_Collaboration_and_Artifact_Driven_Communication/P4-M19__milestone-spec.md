---
milestone: M19
name: Creation Chat Completion and Bugfix Workflow
phase: P4
status: planned
start_date: 2026-06-20
epics:
  - E19.1
  - E19.2
is_final: true
---

# Milestone M19: Creation Chat Completion and Bugfix Workflow

## Goal

Close Phase P4. M19 delivers the two remaining P4 success criteria in a single
consolidated milestone:

1. **Bugfix Workflow (E19.1)** — the expedited production-issue path with SLA tracking,
   CFO Deployment Authorization, and post-mortem generation. The last undelivered item
   from the P4 success criteria.

2. **Creation Chat Ongoing Artifacts (E19.2)** — the artifact vocabulary that turns
   Creation Chat from a one-shot bootstrap tool into a permanent institution: Steering
   Notes, Progress Digests, Bouncer Work logs, and the re-instantiation ritual.

M19 is the final milestone of Phase P4. When M19 merges to `phase/P4` and `phase/P4`
merges to `master`, Phase P4 is complete.

---

## Scope

### E19.1 — Bugfix Workflow

**Deliverables:**

1. **HQ Chat Bugfix Handler** — section added to `governance/systems/hq-execution-chat-starter.md`
   describing how HQ Chat evaluates an incoming issue (Bugfix Epic vs. defer), creates
   the minimal Bugfix Epic spec in `docs/bugfixes/B#.#__spec__<slug>.md`, and commits
   and issues Epic Delivery Authorization. References `governance/systems/bugfix-epic-workflow.md`
   (existing design doc) as the protocol source.

2. **Deployment Authorization artifact** — new YAML schema and template at
   `governance/templates/deployment-authorization.md`. CFO explicitly authorizes or
   rejects any production deploy via this artifact before code is pushed.

3. **SLA tracking** — 4-hour review window from Completion Notice receipt for Bugfix
   Epics, documented in the bugfix workflow. Escalation on miss: urgent flag to CFO.

4. **Post-mortem template** — `governance/templates/post-mortem.md` for Critical/High
   severity bugfixes. Auto-referenced by the bugfix workflow documentation.

5. **Phase spec update (v1.3.0)** — replace original M19 (Two-Stage Lifecycle) and M20
   (Bugfix Workflow) stubs with the executed M19 consolidated scope; record Two-Stage
   Lifecycle diagram as deferred (M17 delivered partial coverage); mark M19 as final
   P4 milestone; increment version from 1.2.0 → 1.3.0.

**Carry-over items (assigned to E19.1):**
- Update `docs/roadmap/overview.md` P4 status to reflect M14–M18 complete
- Add `pytest` to project dependencies (`requirements-dev.txt` or `pyproject.toml`)

### E19.2 — Creation Chat Ongoing Artifacts

**Design constraint (binding — must appear verbatim in E19.2 spec):**

> Creation Chat is the single visible human interface. All governance (HQ, Phase,
> Milestone, Epic) runs as background agents communicating via artifacts. Design
> decisions at every level must optimize for this: complexity invisible to the user,
> only decisions and outcomes surface. The Progress Digest in particular must be
> high-signal and low-noise — the user should not need to dig into phase or milestone
> artifacts to understand project state.

**Deliverables:**

1. **Steering Note schema + template** — `governance/templates/steering-note.md`.
   Authoritative reference instance already committed:
   `.ai-project/artifacts/steering-notes/2026-06-19__creation-chat__steering-note.md`.
   The template YAML schema must match that instance structure.
   Naming convention: `<ISO-date>__<issuer-chat-slug>__steering-note.md`.

2. **Progress Digest schema + template** — `governance/templates/progress-digest.md`.
   Flows HQ → Creation Chat on a periodic basis. Must be high-signal, low-noise: the
   user reads this instead of digging into phase/milestone artifacts. Required sections:
   Phase Status, Open Decisions, Next Actions (3–5 items max), Blocking Concerns.
   Naming convention: `<ISO-date>__hq__progress-digest.md`.

3. **Bouncer Work log** — `governance/templates/bouncer-work-log.md`. Lightweight
   record of Layer-8 manual interventions (data fixes, direct user requests, one-off
   console operations). Design target: under 2 minutes to fill. Must support the
   pattern-detection flow:
   ```
   real-life operation
     → bouncer work (manual, no commit)
       → logged in Bouncer Work log (lightweight)
         → pattern (3+ occurrences) → Steering Note → formal Epic
   ```

4. **Re-instantiation ritual** — documented procedure, placed in
   `governance/systems/creation-chat-guide.md`. Specifies: what to distill before reset
   (a Steering Note), where to put it, how to re-open, what the next session receives.

---

## Branch Strategy

```
phase/P4  (HEAD: 16aa8f7)
└── milestone/M19          ← this branch
    ├── epic/P4-M19-E19.1  ← Bugfix Workflow (dispatched first)
    └── epic/P4-M19-E19.2  ← Creation Chat Ongoing Artifacts (may run in parallel)
```

Epic PRs target `milestone/M19`. Consolidation PR: `milestone/M19 → phase/P4`.
Phase closure PR: `phase/P4 → master`.

---

## Prerequisites

- M18 merged to `phase/P4` ✅ (commit `16aa8f7`)
- `governance/templates/genesis.md` present ✅
- `governance/systems/chat-hierarchy.md` has Creation Chat (Level 0) ✅
- Reference Steering Note committed ✅
  (`.ai-project/artifacts/steering-notes/2026-06-19__creation-chat__steering-note.md`)

---

## Definition of Done

**E19.1 complete:**
- [ ] `docs/bugfixes/README.md` created with B#.# naming convention
- [ ] HQ Execution Chat Starter updated with Bugfix handling section
- [ ] `governance/templates/deployment-authorization.md` committed with YAML schema
  and filled example
- [ ] `governance/templates/post-mortem.md` committed and referenced in bugfix workflow
- [ ] SLA tracking (4-hour window, escalation path) documented in bugfix workflow
- [ ] `docs/roadmap/overview.md` updated: P4 milestones M14–M18 marked complete
- [ ] `pytest` added to project dependencies
- [ ] `P4__phase-spec.md` updated to v1.3.0 (M19 consolidated, M20 removed,
  Two-Stage Lifecycle deferred note, M19 marked final)
- [ ] All existing tests pass

**E19.2 complete:**
- [ ] `governance/templates/steering-note.md` committed; YAML schema matches reference
  instance; filled example embedded
- [ ] `governance/templates/progress-digest.md` committed; high-signal/low-noise
  verified by cold-read test
- [ ] `governance/templates/bouncer-work-log.md` committed; 2-minute fill test passes
- [ ] `governance/systems/creation-chat-guide.md` created with re-instantiation ritual
- [ ] YAML schema validation tests for all three new templates
- [ ] All tests pass

**Milestone complete:**
- [ ] Both epics merged to `milestone/M19`
- [ ] Full test suite passes
- [ ] Milestone Closure Declaration produced

---

## Acceptance Criteria

1. A production issue → Bugfix Epic spec (`docs/bugfixes/B#.#__spec__...md`) flow can
   be described end-to-end from the HQ Chat Starter alone
2. `governance/templates/deployment-authorization.md` exists with correct YAML schema
3. Post-mortem template exists and is referenced in the bugfix workflow documentation
4. A Creation Chat session can be reset and resumed using only committed artifacts
   (genesis.md + most recent Steering Note + most recent Progress Digest)
5. Steering Note, Progress Digest, and Bouncer Work log can each be filled from their
   template alone, without consulting any other governance document
6. Bouncer Work log template passes the 2-minute fill test
7. All tests pass

---

## Phase P4 Closure

After M19 merges to `phase/P4`:

1. Phase Chat opens PR: `phase/P4 → master`
2. Phase Chat produces Phase P4 Delivery Notice
3. HQ Chat issues Phase Accept
4. PR merges to `master`
5. Phase P4 is complete
