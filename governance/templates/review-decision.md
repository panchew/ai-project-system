---
artifact_type: review_decision
artifact_version: 1.0
timestamp: <FILL: ISO-8601 UTC, e.g., 2026-05-29T15:00:00Z>
issuer_chat: Milestone Agent (<P#-M#>)
issuer_role: Milestone Agent
decision: accept|reject
epic_id: <P#-M#-E#.#>
milestone_id: <P#-M#>
phase_id: <P#>
project_name: <project-name>
completion_notice_timestamp: <FILL: timestamp of the Completion Notice being reviewed>
feedback: <FILL: see body section below>
authorization:
  action: merge|rework
  merge_instruction: <FILL: if action=merge, detailed merge steps; if action=rework, leave null or describe rework>
---

# Review Decision: <P#-M#-E#.#> — <Epic Name>

## Decision: ACCEPT ✓ | REJECT ✗

<FILL: Choose one above>

## Reviewer Context
- Reviewed by: <Milestone|Phase|HQ> Agent (<reference>)
- Review Date: <YYYY-MM-DD HH:MM UTC>
- Completion Notice Date: <YYYY-MM-DD HH:MM UTC>

## Feedback

<FILL: Detailed feedback, notes, or rejection reason. See examples below.>

### Example (ACCEPT)
> Excellent work. Spec compliance confirmed, tests comprehensive, PR ready for merge. No issues found.

### Example (REJECT)
> This submission requires rework. The following issues must be resolved:
> 1. **Test Coverage:** Only 60% coverage. Epic spec requires 80% minimum. Add tests for error handling.
> 2. **CI Failures:** 3 linter checks failing. Fix all before resubmission.
> 3. **Documentation:** API documentation missing. Update before resubmission.

## Authorization

<FILL: Choose one section below based on decision>

### If ACCEPT:
The parent performs the merge of this work (PSG §11.6 — a child never holds merge authorization). The parent's own steps:
1. <FILL: Step 1 - e.g., "Verify all CI/CD checks pass on PR #NNN">
2. <FILL: Step 2 - e.g., "Merge PR #NNN to milestone/M# using squash-and-merge">
3. <FILL: Step 3 - e.g., "Delete the epic/E#.# branch after the merge">
4. <FILL: Step 4 - e.g., "Confirm the Epic produced its Delivery Notice; declare Epic E#.# complete in Milestone Chat">
5. <FILL: Step 5 - e.g., "Move to next Epic">

### If REJECT:
Rework required. Address all issues above and resubmit:
1. Make the required changes listed in Feedback above
2. Ensure all CI/CD checks pass locally and in PR
3. Create a new Completion Notice (v1.1) once ready
4. Resubmit for review
