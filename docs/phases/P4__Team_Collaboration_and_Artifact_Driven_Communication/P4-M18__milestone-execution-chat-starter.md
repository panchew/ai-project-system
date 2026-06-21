# MILESTONE EXECUTION CHAT STARTER — P4-M18: Inception Artifacts

MANDATORY CONTEXT PACKET

Project: ai-project-system
Phase: P4 — Team Collaboration and Artifact-Driven Communication
Milestone: M18 — Inception Artifacts
Governance: PROJECT-SYSTEM-GUIDELINES.md and AI-OPERATING-GUIDELINES.md enforced
Base branch: `milestone/M18` (branched from `phase/P4` at commit `5f3b10d`)

MILESTONE OVERVIEW

**Goal:** Define and implement the Creation Chat / Genesis layer — the canonical entry
point for starting a new project under the AI Project System governance framework.

**Why this matters:** Every subsequent workflow (Phase Chat, Milestone Chat, Epic
execution) is well-defined, but the step before all of them — bootstrapping a new
project from a brief — is not. This milestone fills that gap.

**Single Epic:**
- E18.1 — Genesis Template and Creation Chat

**Dependencies:** M16 ✅ M17 ✅ (both merged to `phase/P4`)

BRANCH HIERARCHY

```
phase/P4  (HEAD: 5f3b10d)
└── milestone/M18          ← this branch
    └── epic/P4-M18-E18.1  ← one epic branch
```

---

## STAGE 1 — Review Planning Artifacts and Authorize Execution

Before dispatching E18.1, confirm the following are present and correct on
`milestone/M18`:

**Planning artifacts (committed by Phase Chat):**
- [ ] `P4-M18__milestone-spec.md` — milestone goal, DoD, acceptance criteria
- [ ] `P4-M18-E18.1__spec__Genesis_Template_and_Creation_Chat.md` — epic spec
- [ ] `P4-M18-E18.1__epic-execution-chat-starter.md` — this starter's companion

**Verification:**
```bash
git log origin/phase/P4..HEAD --oneline   # confirm planning commit present
ls docs/phases/P4*/P4-M18*               # confirm all three files present
```

If all planning artifacts are present, proceed to Stage 2.

If any are missing: **do not dispatch the Epic** — escalate to Phase Chat.

---

## STAGE 2 — Oversee E18.1 Execution

### Dispatching E18.1

Open a new Epic Execution Chat using:
```
docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4-M18-E18.1__epic-execution-chat-starter.md
```

The agent will work on branch `epic/P4-M18-E18.1` and open a PR to `milestone/M18`
when done.

### Receiving the Completion Notice

When E18.1 completes, the agent produces a Completion Notice committed to
`epic/P4-M18-E18.1`. You will receive it as a PR comment or forwarded artifact.

**Review checklist:**
- [ ] `governance/templates/genesis.md` present with correct YAML schema
- [ ] All required sections present (Project Brief, HQ Context Packet, Phase 1 Scope,
  Creation Chat Decisions, Next Step)
- [ ] Filled example present and believable (completed genesis.md, not a draft)
- [ ] Creation Chat role defined in `governance/systems/chat-hierarchy.md`
- [ ] `start-a-project.md` updated with Creation Chat step; no manual file-copy remains
- [ ] `governance/templates/README.md` updated
- [ ] Genesis schema test present and passing
- [ ] All 189 baseline tests pass (no regression)
- [ ] The filled walkthrough example could be handed to a Phase Chat with no further
  explanation (key acceptance criterion — test this manually)

### Issuing a Review Decision

**Accept:** All DoD items satisfied; walkthrough passes the "cold read" test.

Issue a Review Decision artifact (use `governance/templates/review-decision.md`):
```yaml
type: review-decision
epic: P4-M18-E18.1
decision: accept
```

**Reject:** One or more DoD items not satisfied, or the walkthrough example requires
explanation to use.

Issue a Review Decision with `decision: reject`, list the specific failures, and
request rework. Maximum 3 rejection cycles before escalating to Phase Chat.

### Authorizing the Merge

After issuing an Accept Review Decision, the agent opens a PR:
`epic/P4-M18-E18.1` → `milestone/M18`

You authorize the merge with a Merge Authorization artifact (use
`governance/templates/merge-authorization.md`), then the agent merges.

### After E18.1 Merges

1. Verify `milestone/M18` reflects all E18.1 deliverables
2. Produce the **Milestone Closure Declaration** (see below)
3. Open PR: `milestone/M18` → `phase/P4`
4. Forward Closure Declaration to Phase Chat for review and merge authorization

---

## MILESTONE CLOSURE DECLARATION (template)

When all Epics are merged and all DoD items verified, produce this artifact and commit
it to `milestone/M18`:

```markdown
---
type: milestone-closure-declaration
milestone: M18
status: complete
completion_date: <YYYY-MM-DD>
declared_by: Milestone Chat (P4-M18 — Inception Artifacts)
issued_to: Phase Chat (P4 — Team Collaboration and Artifact-Driven Communication)
---

# MILESTONE CLOSURE DECLARATION — M18

## Completion Verification
✅ E18.1: Genesis Template and Creation Chat — merged to milestone/M18 (PR #__, merge commit <sha>)

## Milestone Definition of Done — all items satisfied:
[copy DoD from milestone spec with verification notes]

## Milestone Acceptance Criteria — all satisfied:
[copy acceptance criteria with verification notes]

## Milestone Summary
[2-3 sentence summary of what was delivered and why it matters]

## Open Items for Phase Chat
[any non-blocking items; "none" if clean]

## Required Action: Consolidation
1. Pull Request: milestone/M18 → phase/P4
2. Phase Chat reviews and authorizes merge
3. Merge PR (milestone closure commit)
4. milestone/M19 MUST branch from phase/P4 after merge
```

---

## ESCALATION PATH

Escalate to Phase Chat (via Escalation Notice using
`governance/templates/escalation-notice.md`) when:

- A planning artifact is missing and execution is blocked
- E18.1 is rejected 3 times and the agent cannot resolve the issue
- A finding arises that is outside Milestone Chat authority
- The DoD requires a decision only Phase Chat can make

---

## REFERENCE

- **Milestone Spec:** `P4-M18__milestone-spec.md`
- **Epic Spec:** `P4-M18-E18.1__spec__Genesis_Template_and_Creation_Chat.md`
- **Epic Starter:** `P4-M18-E18.1__epic-execution-chat-starter.md`
- **Phase Spec:** `P4__phase-spec.md` (v1.2.0)
- **Governance Templates:** `governance/templates/` (merge-authorization, review-decision,
  escalation-notice, epic-closure-notice all present as of M17)
- **Next Milestone:** M19 — Two-Stage Lifecycle (branches from phase/P4 after M18 merges)
