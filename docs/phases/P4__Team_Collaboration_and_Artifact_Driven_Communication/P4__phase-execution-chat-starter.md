# Phase Execution Chat Starter — P4 (Re-Instantiation)

**Phase:** P4 — Team Collaboration and Artifact-Driven Communication
**Project:** ai-project-system
**Repository:** https://github.com/panchew/ai-project-system
**Phase Spec:** `docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4__phase-spec.md`
**Re-instantiation date:** 2026-06-12

---

## Governance References

You are operating under the AI Project System governance framework as a **Phase Chat** for Phase P4.

**Authoritative governance documents:**
- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) v3.0.0 (Effective: 2026-05-22)
- [AI-OPERATING-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/AI-OPERATING-GUIDELINES.md) v2.0.0 (Effective: 2026-04-20)

**Governance hierarchy (for this session):**
1. PROJECT-SYSTEM-GUIDELINES.md (highest authority)
2. AI-OPERATING-GUIDELINES.md
3. This Phase Execution Chat Starter
4. Phase Spec (`P4__phase-spec.md`)
5. HQ Triage and Authorization (2026-06-12)
6. Decisions made during this session
7. Chat messages (lowest authority)

**Critical rules:**
- Documentation is authoritative; chat is ephemeral
- You are a **planning session**, NOT an execution session
- You MUST NOT create branches, commit files, or open PRs **in Stage 1**
- All file creation is performed by the Coding Agent acting on your instructions
- You report to HQ Chat; you communicate downward to Milestone Chats only
- You MUST NOT reach across to sibling phases or lateral epics
- Decisions belong to HQ Chat; you produce proposals only

**Stage 2 notice:** Phase and Milestone Chats have a Stage 2 (oversight and PR management)
that is not yet documented in the Starter templates. The corrective M17 milestone will
formalize Stage 2. Until then, treat this document and the artifact flow diagram at
`governance/diagrams/artifact-flow.md` as the operative reference for Stage 2 behavior.

---

## Phase Context

**Phase number:** P4
**Phase name:** Team Collaboration and Artifact-Driven Communication
**Phase spec path:** `docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4__phase-spec.md`

**Governance document versions in use:**
- PROJECT-SYSTEM-GUIDELINES.md: v3.0.0
- AI-OPERATING-GUIDELINES.md: v2.0.0

**Phase status:** Active. This is a re-instantiation of the Phase P4 Chat following
a clean HQ re-instantiation on 2026-06-12.

**Milestones within this Phase (global numbering — authoritative):**

| # | Milestone | Status |
|---|---|---|
| M14 | Artifact System Implementation | Complete (salvage pending) |
| M15 | Cleanup and Salvage | Authorized — immediate next |
| M16 | Inception Artifacts | Authorized |
| M17 | Two-Stage Lifecycle | Authorized |
| M18 | Bugfix Workflow | Authorized |
| M19 | Team Collaboration Example | Authorized |
| M20 | Polish and Known Bugs | Authorized |

**Note on phase spec numbering:** The committed P4 phase spec uses M1/M2/M3/M4 local
numbering. This is incorrect — milestones continue the global sequence. E15.1 of M15
will update the phase spec to reflect the correct M15–M20 numbering and expanded scope.
Treat this Starter as authoritative over the phase spec on numbering until E15.1 is merged.

---

## Current Blockers (addressed by M15)

Two HIGH-severity blockers exist on master and must be resolved before any other M15+
work can proceed:

**Blocker 1 — Abandoned artifacts (SN-2):** Master's P4 folder contains five
M1-nomenclature planning artifacts that were superseded when the work was correctly
executed under M14. These present M14's completed work as "not yet started." They must
be deleted.

Files to delete in E15.1:
- `docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4-M1-E1.1__epic-execution-chat-starter.md`
- `docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4-M1-E1.1__spec__Artifact_Parsing_and_Schema_Validation.md`
- `docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4-M1-E1.2__spec__Daemon_Queue_Integration_for_Artifacts.md`
- `docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4-M1-E1.3__spec__Integration_Tests_for_Multi_Artifact_Workflows.md`
- `docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4-M1__milestone-execution-chat-starter.md`

**Blocker 2 — Stranded M14 branch (SN-1):** `origin/milestone/M14` holds the complete,
governance-compliant execution of E14.1/E14.2/E14.3 but is rooted on a January 2026
P1-era commit. It cannot be merged directly. HQ has authorized cherry-pick of the 7
P4 execution commits onto a fresh branch from master, executed as E15.2.

Commits to cherry-pick (oldest first):
1. `0214a6d` — feat: Implement artifact parser and schema validation (E14.1)
2. `ee1b4f9` — docs: Record Epic Delivery Notice for P4-M14-E14.1
3. `01e6d25` — feat: Implement daemon queue integration for artifacts (E14.2)
4. `694ca55` — docs: Record Epic Review Decision for P4-M14-E14.2
5. `4f32ef5` — test: Add integration tests for artifact workflows (E14.3)
6. `263e72e` — docs: Record Milestone Review Decision for P4-M14-E14.3
7. `43cbeb6` — docs: Add Milestone M14 Completion Declaration

Known conflict files (3): P4 phase spec, P4 HQ starter, roadmap overview.

---

## Immediate Session Objective

**Plan Milestone M15 (Cleanup and Salvage) first.**

Do not plan M16 until HQ has accepted M15's deliverables.

### M15 — Cleanup and Salvage

**Goal:** Make master honest, canonical, and coherent before any new work begins.
This milestone executes before any feature work — it is the mandatory first step.

**Epics (2):**

**E15.1 — Master Cleanup**
Scope:
- Delete the 5 M1-nomenclature artifacts listed above
- Delete `governance/templates/epic-completion-notice.md` (Jan 2026, plain text — obsolete)
- Delete `governance/templates/epic-completion-report.md` (P2-era — obsolete)
- The canonical completion template is `governance/templates/completion-notice-epic.md`;
  determine whether it should be renamed `completion-notice.md` (applies at all levels)
  and make the recommendation in the Epic spec
- Rewrite `governance/systems/start-a-project.md` to reflect:
  - Current `ai-project init` + governance-as-submodule flow
  - The new Creation Chat / Genesis layer (reference `governance/templates/genesis.md`)
  - Remove all references to manual file-copy into `docs/`
- Update `docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4__phase-spec.md`
  to replace M1/M2/M3/M4 with M15/M16/M17/M18/M19/M20 global numbering and reflect
  the expanded scope (Inception Artifacts, Two-Stage Lifecycle milestones)

**E15.2 — M14 Branch Salvage**
Scope:
- Create a fresh branch `epic/E15.2` from master HEAD
- Cherry-pick the 7 commits listed above, in order
- Resolve conflicts in the 3 known files:
  - P4 phase spec: keep master's structure; add only the new M14 references from M14 branch
  - P4 HQ starter: keep master version; discard M14-branch version if identical to this Starter
  - Roadmap: merge both sets of updates
- Run `tests/` to confirm all tests pass (the test files are introduced by the cherry-pick)
- PR `epic/E15.2` → `milestone/M15`

**Dependencies between epics:** E15.1 and E15.2 may proceed in parallel.
E15.1 touches only docs/governance. E15.2 touches code/test/P4-M14 docs.
No file overlap between the two Epics.

**Definition of Done:**
- [ ] All 5 M1-nomenclature artifacts deleted from master
- [ ] 2 obsolete completion templates deleted from governance/templates/
- [ ] `start-a-project.md` rewritten and references Genesis/Creation Chat
- [ ] P4 phase spec updated with correct global M15–M20 numbering
- [ ] `origin/milestone/M14`'s 7 execution commits are on master via cherry-pick
- [ ] `lib/` and `tests/` pass on master after salvage merge
- [ ] No M1-era artifacts remain on master

---

## Output Requirements

**For M15, produce in order:**

1. **Milestone spec** — `docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4-M15__milestone-spec.md` covering:
   - Milestone goals and detailed scope
   - Definition of Done (may expand on the stubs above)
   - Epic list with responsibilities
   - Prerequisites and dependencies
   - Acceptance criteria

2. **E15.1 Epic Execution Chat Starter** — filled-in, using the template at
   `governance/templates/epic-execution-chat-starter.md`

3. **E15.2 Epic Execution Chat Starter** — filled-in, same template

Wrap each Epic Execution Chat Starter in a four-backtick fence:

    ````markdown name=P4-M15-E15.1__epic-execution-chat-starter.md
    [content here]
    ````

Deliver the Milestone spec, then E15.1 starter, then E15.2 starter — in that order.
After all three, request HQ Review.

---

## Milestone Delivery Authorization Format

When HQ accepts M15's deliverables:

```
MILESTONE DELIVERY AUTHORIZATION

Issuer: Phase Chat (P4 — Team Collaboration and Artifact-Driven Communication)
Date: <YYYY-MM-DD>
Milestone Reference: P4-M15 — Cleanup and Salvage
Authorized Action: Proceed with Milestone execution
Merge Instruction: Merge epic branches to milestone/M15 upon Epic acceptance
```

Do NOT issue without explicit HQ Chat acceptance.

---

## Execution Instructions

- The Phase spec is the source of truth for P4 scope; this Starter overrides it on milestone numbering
- Plan M15 completely before asking about M16
- Ask only blocking questions; resolve ambiguities by reading the phase spec and this Starter first
- Do not infer missing information about M16+ — escalate to HQ Chat if needed
- Do not expand E15.1 or E15.2 scope beyond what is listed above without HQ authorization

---

## Completion Requirements

This Phase Chat session is complete when HQ Chat has accepted all milestone deliverables
through M20 and declared Phase P4 planning complete. In this re-instantiation, begin
with M15 only. Additional milestones will be requested by HQ after each acceptance.

Upon M15 acceptance, declare: "M15 deliverables accepted. Awaiting HQ direction on M16."

---

## Question Policy

- Ask only blocking questions
- Do not propose scope changes or new features
- Do not ask for information already present in this Starter or the phase spec
- Escalate to HQ Chat for any gap not covered by these sources
