# Contributor Guide

**For developers implementing Epics in the AI Project System.**

This guide covers the full Epic lifecycle from the moment you receive an Epic assignment to the moment your PR is merged. Read this top to bottom before starting your first Epic.

---

## Your Role

As a Contributor, your job is to implement Epics according to their specifications. You work within a well-defined boundary: the Epic spec tells you what to build; you build it; you deliver a PR and a Completion Notice; a parent agent or Phase Lead reviews and decides.

**You own:**
- Implementation decisions within Epic scope
- Tests for your implementation
- Your PR description and code quality
- Asking questions when the spec is ambiguous (do this early)

**You do not own:**
- Epic scope (defined by Milestone Agent)
- Merge authority (held by Milestone Agent after Review Decision)
- Production deployment (CFO only)

---

## Epic Workflow: Step by Step

### Step 1 — Receive Your Epic Assignment

Your Milestone Agent or Phase Lead assigns you an Epic. You will receive:

- An **Epic Execution Chat Starter** — the document that opens your execution session
- An **Epic Delivery Authorization** — explicit authorization to begin work

Both are required before you start. If you have only one, ask your Phase Lead for the other.

**Verify you have:**
- [ ] Epic Execution Chat Starter with your Epic ID (e.g., `P1-M1-E1.1`)
- [ ] Epic Delivery Authorization
- [ ] Access to the Epic spec file (e.g., `docs/phases/P1__Phase_Name/M1__Milestone/E1.1__spec__Feature_Name.md`)

---

### Step 2 — Read the Spec Fully Before Starting

This is the most important step. The spec defines your Definition of Done. Implementing without reading it fully leads to rejection.

Read and understand:
- **Goals** — what problem this Epic solves
- **Deliverables** — the specific files or outputs expected
- **Definition of Done** — the checklist you must complete before submitting
- **Acceptance Criteria** — what the Milestone Agent will check

**If anything is ambiguous:** Ask immediately. Write your question in your execution chat or as an Escalation message to your Milestone Agent. Do not guess at scope.

---

### Step 3 — Create Your Branch

Create your branch from the Milestone branch:

```bash
git checkout milestone/M1
git pull origin milestone/M1
git checkout -b epic/E1.1
```

The branch name format is always `epic/E#.#` (e.g., `epic/E1.1`). Never branch from `master` or `phase/P#` directly.

---

### Step 4 — Implement

Implement the Epic according to the spec. Practical rules:

- **Commit early and often.** Small commits are easier to review.
- **Stay in scope.** If you discover a related problem outside the Epic spec, do not fix it — create a note and escalate. Scope creep causes rejections.
- **Write tests as you go.** Tests written after the fact are always thinner. If the spec requires a minimum coverage threshold, check it before submitting.
- **Self-review before submitting.** Walk through the Definition of Done checklist item by item.

---

### Step 5 — Open Your Pull Request

When implementation is complete:

```bash
git push origin epic/E1.1
```

Open a PR targeting the milestone branch (`milestone/M1`, not `master`).

**PR title format:** `feat: <Epic title> (E1.1)` or `fix:`, `docs:` as appropriate.

**PR description should include:**
- Summary of what was implemented
- How to test it
- Any deviations from the spec (and your rationale)
- Reference to the Epic spec file

---

### Step 6 — Produce a Completion Notice

After your PR is open, produce a **Completion Notice** — a structured artifact signaling that your work is ready for parent review.

The Completion Notice is a Markdown file with YAML frontmatter. Store it at:

```
.ai-project/artifacts/completion-notices/
<timestamp>__<epic_id>__completion-notice.md
```

Minimum required fields:

```markdown
---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: <ISO-8601 UTC>
issuer_chat: Epic Agent (<epic_id>)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: <name>
deliverables:
  - name: Implementation
    path: src/...
    type: implementation
    status: ready
  - name: Tests
    path: tests/...
    type: implementation
    status: ready
  - name: Pull Request
    path: pull/<number>
    type: pr
    status: ready
blockers: []
qa_status: passed
pr_details:
  number: <PR number>
  title: <PR title>
  target_branch: milestone/M1
  url: <PR URL>
---

# Completion Notice: P1-M1-E1.1 — <Epic Title>

## Summary
<2-3 sentences: what was built and delivered>

## Deliverables
- ✓ Implementation committed
- ✓ Tests written and passing
- ✓ PR #<N> opened against milestone/M1

## Quality Assurance
- Tests: passed
- Definition of Done: ✓ all items met

## Blockers or Risks
None.

## Ready for Parent Review
Submitted for Milestone Chat review and acceptance.
```

Commit the Completion Notice to your epic branch before presenting it to the parent chat.

**In manual mode:** Copy the Completion Notice and paste it into your Milestone Chat.

**In agentic mode:** The daemon routes it automatically after you commit.

---

### Step 7 — Await Review Decision

Your Milestone Agent (or Phase Lead in manual mode) reviews your Completion Notice and issues a **Review Decision**.

**If ACCEPT:** You are authorized to merge. Proceed to Step 8.

**If REJECT:** Read the rejection reasons carefully. Address every item listed. Produce a new Completion Notice (increment the version: `v1.1`) after rework and resubmit. You have up to 3 attempts before the Milestone Agent escalates.

---

### Step 8 — Merge and Produce Delivery Notice

After receiving a Review Decision (Accept):

1. Confirm the PR passes all CI checks
2. Merge the PR to the milestone branch
3. Delete your epic branch (optional but recommended)
4. Produce a **Delivery Notice** (similar format to Completion Notice, but with merge details added)
5. Commit the Delivery Notice and close your execution chat

**You do not push directly to `master`, `phase/P#`, or any branch other than the milestone branch specified in your authorization.**

---

## Definition of Done Checklist (Generic)

Before submitting any Completion Notice, verify:

- [ ] All spec deliverables created
- [ ] All acceptance criteria met (verify each one, not just "probably")
- [ ] Tests written and passing
- [ ] No regressions in existing tests
- [ ] PR opened against the correct milestone branch
- [ ] PR description is complete
- [ ] Completion Notice artifact committed to epic branch
- [ ] No broken links in any documentation produced

If any item is unchecked, do not submit — complete it first.

---

## Escalation Path

If you are blocked and cannot proceed:

1. Document the blocker clearly: what you tried, what is preventing progress
2. Write an Escalation message in your execution chat (or an Escalation artifact if formal)
3. Escalate to your Milestone Agent or Phase Lead
4. Wait for response (SLA: 4 hours for Epic-level escalations)
5. Accept the decision and continue — do not re-escalate once decided

**When to escalate:**
- The spec is ambiguous and you cannot safely interpret it
- A dependency (another Epic) has not landed and you are blocked
- You have failed the Dev-QA loop 3 times and cannot resolve the failure
- You discover the spec contains a fundamental conflict or error

---

## PR Workflow Summary

```
Create branch (epic/E#.#)
  ↓
Implement + tests
  ↓
Open PR (→ milestone/M#)
  ↓
Produce Completion Notice
  ↓
Await Review Decision
  ↓ [Accept]
Merge PR → Produce Delivery Notice
  ↓ [Reject]
Rework → New Completion Notice → Resubmit
```

---

## Cross-References

- [Team Onboarding Guide](team-onboarding-guide.md) — full system overview
- [Reviewer Guide](reviewer-guide.md) — what your reviewer is checking
- [Decision Matrices](decision-matrices.md) — who decides what
- [Example Walkthrough](example-walkthrough.md) — real Epic cycle end-to-end
- [FAQ](faq.md) — common questions
- [Troubleshooting Guide](troubleshooting-guide.md) — if something goes wrong
- [Governance: Artifact Communication Protocol](../../governance/systems/artifact-communication-protocol.md) — Completion Notice and Delivery Notice schemas
