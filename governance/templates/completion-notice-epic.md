---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: <FILL: ISO-8601 UTC, e.g., 2026-05-29T14:32:00Z>
issuer_chat: Epic Agent (<P#-M#-E#.#>)
issuer_role: Epic Agent
status: ready_for_review
epic_id: <P#-M#-E#.#>
milestone_id: <P#-M#>
phase_id: <P#>
project_name: <project-name>
deliverables:
  - name: <deliverable_name>
    path: <repo_path_to_deliverable>
    type: spec|implementation|report|pr
    status: ready
  # Add more deliverables as needed
blockers: []
  # Format: [{description: "...", severity: "critical|warning"}, ...]
  # Leave empty [] if no blockers
qa_status: passed|failed|blocked
pr_details:
  number: <PR_number_or_pending>
  title: <PR_title>
  target_branch: <target_branch>
  url: <PR_URL_or_not_created_yet>
---

# Completion Notice: <P#-M#-E#.#> — <Epic Name>

## Summary
<FILL: 2-3 sentence executive summary of what was delivered>

## Deliverables
<FILL: List of what was created/modified with file paths and status>

Example:
- ✓ Epic spec: `docs/phases/.../E#.#__spec__....md`
- ✓ Implementation: `src/.../<files>`
- ✓ Tests: `tests/.../<test files>` (X/X passing)
- ✓ PR #NNN: `https://github.com/.../pull/NNN` (against target_branch)

## Quality Assurance

- Tests: <passed/failed/n/a with count if passed>
- Code Review: <ready/pending/issues>
- Definition of Done: <✓ all items met / ✗ list items pending>
- <Additional QA details if relevant>

## Blockers or Risks

<FILL: Any outstanding issues that may affect acceptance, or "None.">

Example:
- No blockers. All Definition of Done items satisfied.

OR

- Blocker 1: <description> (CRITICAL)
- Blocker 2: <description> (WARNING)
- <etc>

## Ready for Parent Review

This Epic is complete and submitted for <Milestone|Phase|HQ> Chat review and acceptance.

**Next Action:** Under default-accept (PROJECT-SYSTEM-GUIDELINES.md §11.6 /
AI-OPERATING-GUIDELINES.md §12), a clean delivery — Definition of Done, acceptance
criteria, and spec all met — is **accepted by silence**: parent acceptance authorizes
the merge, and no Review Decision is issued. A **Review Decision** is issued only on the
**exception path**, when Parent Chat reviews this artifact and finds it is not clean:
- **Review Decision (Reject)** → requires rework
- **Review Decision (Accept with follow-up Epic(s))** → accepted, but new Epic(s) must
  address findings
