---
type: escalation-notice
milestone: M19
issued_by: Milestone Chat (P4-M19 — Creation Chat Completion and Bugfix Workflow)
issued_to: Phase Chat (P4 — Team Collaboration and Artifact-Driven Communication)
date: 2026-06-20
status: open
---

# Escalation Notice: Process gaps surfaced during M19 execution (non-blocking, for future-work hardening)

## Trigger

Out-of-scope process findings. Neither blocks M19 — both epics are proceeding — but both
are systemic and will recur (and grow more costly as the system moves from manual mode
toward concurrent/agentic execution). Raising them now so the fixes land in governance
before the next phase rather than being rediscovered. The system-level items are flagged
for Phase Chat to forward to HQ Chat.

## Findings

### Gap 1 — Declared prerequisites are not verified as *committed*

The M19 milestone spec and the E19.2 epic starter both list the reference Steering Note
(`.ai-project/artifacts/steering-notes/2026-06-19__creation-chat__steering-note.md`) as a
satisfied prerequisite (marked "✅ committed"). During execution it was found **untracked
in the working tree** — never committed to `phase/P4` or `milestone/M19`. E19.2's schema
test is required to validate against this exact instance, so a fresh worktree or clone of
`epic/P4-M19-E19.2` would not have had it.

Root cause: the Stage 1 prerequisite check in the milestone/epic starters verifies that
**planning artifacts exist as files**, but does not verify that **declared prerequisite
artifacts are actually tracked in git** on the expected branch. A "✅ committed" claim in a
spec is taken at face value. This is a false-green: the check passes while the prerequisite
is absent from history.

### Gap 2 — Concurrent chats sharing one git working tree cause wrong-branch commits

This Milestone Chat and the live E19.2 Epic Execution operated in the **same git working
tree** (`git worktree list` shows a single tree). While I had an in-flight two-step commit
task, the E19.2 chat created and checked out `epic/P4-M19-E19.2` from `milestone/M19`. My
second commit (the reference Steering Note) therefore landed on `epic/P4-M19-E19.2` instead
of `milestone/M19`, silently, with no error.

It worked out benignly this time (the Steering Note is content E19.2 needs and will carry
back to `milestone/M19` on merge), but the failure mode is general: any two chats sharing a
working tree can switch the branch under each other and commit to the wrong place, or
clobber each other's uncommitted/untracked work. There is currently no convention assigning
working-tree ownership per chat.

### Gap 3 — Creation Chat / CFO scope direction entered an Epic out-of-band

Mid-execution, the CFO (Layer 8, operating Creation Chat) added new scope to E19.2 — a "CFO
PR review gate" — by having Creation Chat produce a *revised Epic Execution Chat Starter*
with a new binding "Constraint 2," which was pasted into the already-running E19.2 Epic chat.
The Epic Agent implemented it faithfully. The directive is legitimate top-level authority,
but the channel bypassed the artifact cascade (Steering Note → HQ → Phase → Milestone spec
amendment) and the Milestone Chat that owns epic starters, and left no audit trail. On first
review the addition was indistinguishable from an Epic Agent self-authorizing scope — exactly
the ambiguity a proper trail prevents. (This is the same class of out-of-band intervention
that the E19.2 Bouncer-Work-Log → Steering-Note loop exists to capture.)

## What Was Attempted

- **Gap 1:** Resolved for M19 in-flight by committing the reference Steering Note so the
  E19.2 branch has it (it will reach `milestone/M19` via the E19.2 merge). This patches the
  instance; it does not fix the verification step that let it through.
- **Gap 2:** Contained by ceasing all working-tree mutations from the Milestone Chat while
  E19.2 runs and switching to read-only review of the epic branch (`git show`/`git diff`)
  instead of checking out the epic branch. This avoids further collisions; it does not
  establish a durable isolation convention.
- **Gap 3:** Formalized after the fact rather than rejecting correct, CFO-wanted work:
  Creation Chat issued Steering Note SN-9 (`2026-06-20__creation-chat__steering-note.md`)
  recording the decision; the Milestone Chat amended the E19.2 spec to v1.1 (Constraint 2 +
  Functional Requirement 5, with a provenance note) adopting it; E19.2 was then accepted
  against v1.1. This restores the audit trail; it does not establish the routing rule.

## Decision Needed

For Phase Chat (and forward the system-level items to HQ Chat):

1. **Strengthen the prerequisite check** in the milestone/epic execution starters: a
   prerequisite marked "committed" must be verified with `git ls-tree`/`git ls-files`
   against the expected branch, not by file existence in the working tree alone. Suggest
   amending the Stage 1 checklist wording accordingly.
2. **Establish a working-tree isolation convention** for concurrently-active chats —
   e.g., one `git worktree` per active chat, or an explicit branch-ownership rule that a
   chat never runs in a tree another chat may switch. Suggest documenting this in
   `governance/systems/chat-hierarchy.md` and/or the operating guidelines.
3. Confirm whether the reference Steering Note should *also* exist independently on
   `milestone/M19` (cherry-picked) rather than only arriving via the E19.2 merge, or
   whether arriving via the merge is acceptable. (Milestone Chat's view: arriving via the
   merge is acceptable; no action needed.)
4. **Ratify the routing rule** (Gap 3): scope direction from Creation Chat / the CFO MUST
   flow as a Steering Note + spec amendment (and, for an in-flight Epic, a Milestone-Chat
   re-issued starter), never as a pasted starter edit. Confirm the after-the-fact
   formalization of the E19.2 CFO PR review gate is the correct remedy, and document the
   rule in the operating guidelines / `chat-hierarchy.md`.

## Impact

Non-blocking for M19. E19.1 is merged and closed; E19.2 is accepted (against spec v1.1) and
authorized to merge. The cost of inaction is future recurrence: silent false-green
prerequisite checks, silent wrong-branch/clobbered-work commits, and out-of-band scope
changes with no audit trail — all of which become more likely and more damaging as more
chats run concurrently and as execution moves toward agentic mode.

## Resolution

(empty — awaiting Phase Chat decision; system-level items to be forwarded to HQ Chat)
