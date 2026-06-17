# Reviewer Guide

**For team members performing code review on Epic pull requests.**

The Reviewer is the technical quality gate for Epic deliverables. Your approval signals that the implementation is correct, spec-compliant, and safe to accept. This guide covers your checklist, your authority, and how to interact with the Review Decision process.

---

## Your Role

As a Reviewer, you are assigned to one or more Epics to review their PRs before the Milestone Agent issues a Review Decision. You have the authority to block a merge if you find issues.

**You own:**
- Technical assessment of implementation correctness
- Verification of spec compliance
- Gate on Definition of Done completeness
- Communicating clear, actionable feedback

**You do not own:**
- Epic scope (that is Milestone Agent territory)
- Final merge authorization (Milestone Agent issues the Review Decision)
- Deployment authorization (CFO only)

---

## When You Are Engaged

Your review is triggered when the Epic Agent or Contributor opens a PR and produces a Completion Notice. Your Phase Lead or Milestone Agent assigns the PR to you.

**Manual mode:** Your Phase Lead messages you directly or assigns you via GitHub.

**Agentic mode:** The daemon routes the Completion Notice to your Milestone Agent, who notifies you via Milestone Chat.

---

## Review Checklist

Work through this checklist in order. Do not approve until all items pass.

### 1. Spec Compliance

- [ ] The PR title references the Epic ID
- [ ] Every deliverable listed in the Epic spec `Deliverables` section is present
- [ ] No deliverables are present that were not in the spec (scope creep)
- [ ] The implementation matches the spec goals — not just the letter but the intent

### 2. Code Correctness

- [ ] Logic is correct — trace through the main execution path manually if needed
- [ ] Edge cases from the spec's Acceptance Criteria are handled
- [ ] No obvious security issues (injection, unvalidated inputs, exposed secrets)
- [ ] No dead code committed (unless it is explicitly marked as intentional)

### 3. Tests

- [ ] Tests exist for all new functionality
- [ ] Tests cover error/failure paths, not just the happy path
- [ ] All tests pass (check CI status on the PR)
- [ ] Test quality is adequate — a test that always passes regardless of logic is not a test

### 4. Definition of Done

- [ ] Contributor's Completion Notice lists DoD items as met
- [ ] You independently verify each DoD item (do not accept the Completion Notice at face value)
- [ ] If the spec lists a minimum test coverage threshold, verify it is met

### 5. Documentation (if applicable)

- [ ] Any new public APIs, flags, or behaviors are documented
- [ ] No broken cross-links in any new Markdown files
- [ ] File paths referenced in documentation actually exist in the repo

### 6. No Regressions

- [ ] Existing tests still pass
- [ ] No functionality that was previously working is broken

---

## How to Provide Feedback

### Approving

If all checklist items pass, approve the PR in GitHub and notify your Milestone Agent or Phase Lead:

> "E1.1 PR #42 approved. Code review complete. No issues. Ready for Milestone acceptance."

In manual mode, pass this message to the Milestone Chat so the Milestone Agent can issue a Review Decision (Accept).

### Requesting Changes

If you find issues, request changes on the PR in GitHub. Be specific:

**Good feedback:**
> "Line 47 in `auth.ts`: the token expiry check uses `<` instead of `<=`. This allows tokens at the exact expiry timestamp to be accepted. Should be `<=` for the check to match the spec's 'valid until expiry' requirement."

**Not useful:**
> "This doesn't look right to me."

Each piece of feedback should state:
- **What** is wrong
- **Where** it is (file + line number when possible)
- **Why** it is wrong (reference the spec, security rule, or correctness issue)
- **What** the fix should be

### Blocking a Merge

If you find a critical issue that must block the merge, flag it as a Review Blocker:

> "BLOCKER: The PR does not implement the rate limiting described in section 3 of the Epic spec. This is a security requirement. Merge must be blocked until implemented."

Communicate this to your Milestone Agent. The Milestone Agent will issue a Review Decision (Reject) based on your blocker. The contributor must rework and resubmit.

---

## How Rejections Work

You do not issue the Review Decision artifact yourself — that is the Milestone Agent's job. Your role is to provide the technical assessment that informs the decision.

**Flow:**

```
Contributor submits Completion Notice
  ↓
Milestone Agent notifies Reviewer
  ↓
Reviewer assesses PR (this is your work)
  ↓ [Issues found]
Reviewer communicates issues to Milestone Agent
  ↓
Milestone Agent issues Review Decision (Reject)
  ↓
Contributor reworks
  ↓ [No issues]
Reviewer approves
  ↓
Milestone Agent issues Review Decision (Accept)
  ↓
Contributor merges
```

---

## Scope Boundaries

It is tempting to review things outside the Epic scope — "while I'm here, this other file also has a problem." Do not do this.

- Review only what is in the Epic spec
- If you notice issues outside scope, note them separately and report them to the Phase Lead as potential future Epics
- Adding new requirements during review is scope creep and delays delivery

The Reviewer role is a quality gate, not a design authority. If you think the spec itself is wrong, escalate that concern to the Phase Lead separately from your code review.

---

## Escalating Review Blockers

If you find a blocker that you believe requires a decision beyond the Milestone Agent's authority (e.g., a security issue requiring architectural change, or a compliance concern), escalate:

1. Document the concern clearly in the PR review
2. Notify the Milestone Agent and Phase Lead
3. The Phase Lead or HQ Agent evaluates severity
4. If Phase-level decision required, Phase Lead escalates to CFO

Do not hold up a review indefinitely without escalating. If you cannot resolve a concern within your authority, escalate immediately.

---

## SLA

Review completion is expected within **24 hours** of being assigned. If you cannot complete review within 24 hours, notify your Phase Lead immediately so they can reassign or extend the timeline.

---

## Cross-References

- [Team Onboarding Guide](team-onboarding-guide.md) — full system overview
- [Contributor Guide](contributor-guide.md) — what the contributor is expected to deliver
- [Decision Matrices](decision-matrices.md) — who decides what
- [FAQ](faq.md) — common questions
- [Troubleshooting Guide](troubleshooting-guide.md) — if something goes wrong
- [Governance: Roles & Authorization](../../governance/systems/roles-authorization-team-governance.md) — authoritative role definitions
