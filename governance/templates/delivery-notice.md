---
artifact_type: delivery_notice
artifact_version: 1.0
timestamp: <FILL: ISO-8601 UTC, e.g., 2026-05-29T16:00:00Z>
issuer_chat: Epic Agent (<P#-M#-E#.#>)
issuer_role: Epic Agent
status: delivered
epic_id: <P#-M#-E#.#>
milestone_id: <P#-M#>
phase_id: <P#>
project_name: <project-name>
merge_details:
  pr_number: <PR_number>
  pr_url: <PR_GitHub_URL>
  merge_commit: <commit_hash>
  merge_timestamp: <ISO-8601 UTC>
  merge_strategy: squash|rebase|merge
  target_branch: <target_branch>
duration:
  start_date: <YYYY-MM-DD>
  end_date: <YYYY-MM-DD>
  elapsed_days: <number>
final_artifacts:
  - name: <artifact_name>
    path: <repo_path>
    type: spec|implementation|report
  # Add all final artifacts
completion_notice_timestamp: <FILL: timestamp of associated Completion Notice>
review_decision_timestamp: <FILL: timestamp of associated Review Decision>
---

# Delivery Notice: <P#-M#-E#.#> — <Epic Name>

## Summary
<FILL: Brief executive summary - e.g., "Work successfully delivered. PR merged to parent branch. Chat closed.">

## Merge Details
- PR Number: #<number>
- PR URL: <GitHub_URL>
- Merge Commit: <commit_hash>
- Target Branch: <branch>
- Merge Strategy: <squash|rebase|merge>
- Merge Time: <YYYY-MM-DD HH:MM UTC>

## Duration
- Started: <YYYY-MM-DD>
- Completed: <YYYY-MM-DD>
- Total Time: <X days, Y hours>

## Final Artifacts
<FILL: List all deliverables committed to the repository>

Example:
- docs/phases/P#__.../M#__Milestone/E#.#__spec__Feature_Name.md
- src/features/feature-name.ts
- tests/features/feature-name.test.ts

## Chat Closure

This <Epic|Milestone> Chat (<P#-M#-E#.#>) is now closed. All work is delivered and merged to <target_branch>.

**Next Step:** Parent Chat acknowledges delivery and moves forward.
