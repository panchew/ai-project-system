# Epic Execution Chat Starter Template

<!-- 
  EPIC EXECUTION CHAT STARTER TEMPLATE
  
  Purpose: Provide the Governance Agent (Epic mode) with complete context to execute an Epic.
  
  Usage:
  1. Copy this template
  2. Replace all <placeholders> with actual content
  3. Delete HTML comments (or keep for reference)
  4. The entire filled-in content MUST be wrapped in a fenced markdown code block
     when delivered (see AI-OPERATING-GUIDELINES.md §3.1.1):

         ````markdown name=<E#.#>-epic-execution-chat-starter.md
         [filled-in content here]
         ````

     This preserves markdown formatting when the starter is copy-pasted into a
     new Governance Agent session (Epic mode). The four-backtick fence escapes
     any triple-backtick code blocks inside the content.
  5. After the code block, add the canonical copy instruction:
     "Copy the entire chat starter above and paste into the Governance Agent (Epic mode) to begin execution."
  
  This template aligns with AI-OPERATING-GUIDELINES.md and PROJECT-SYSTEM-GUIDELINES.md.
-->

---

# Epic Execution Chat Starter — <E#.#>

**Epic:** <E#.#> — <Epic Name>  
**Phase:** <P#> — <Phase Name>  
**Milestone:** <M#> — <Milestone Name>  
**Repository:** <owner>/<repo-name>  
**Branch Strategy:** `epic/<E#.#>` → PR to `milestone/<M#>`  

---

## Governance References

You are operating under the AI Project System governance framework.

**Authoritative governance documents:**
- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/<owner>/<repo>/blob/<branch>/governance/PROJECT-SYSTEM-GUIDELINES.md) v<version> (Effective: <YYYY-MM-DD>)
- [AI-OPERATING-GUIDELINES.md](https://github.com/<owner>/<repo>/blob/<branch>/governance/AI-OPERATING-GUIDELINES.md) v<version> (Effective: <YYYY-MM-DD>)

<!-- 
  Replace <owner>, <repo>, <branch>, and <version> with actual values.
  
  Example:
  - [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) v2.0.0 (Effective: 2026-04-20)
-->

**Governance hierarchy:**
1. PROJECT-SYSTEM-GUIDELINES.md (highest authority)
2. AI-OPERATING-GUIDELINES.md
3. This Epic Execution Chat Starter
4. Epic Spec
5. Decisions made during execution
6. System references
7. Chat messages (lowest authority)

**Critical rules:**
- Documentation is authoritative, chat is ephemeral
- You must follow the canonical happy path for Epic closure
- You must produce an Epic Completion Report upon execution completion
- You must stop after PR creation and await HQ authorization for merge
- Accept/reject decisions are made by HQ Chat (human), not by you

---

## Epic Specification

**Full spec:** [<P#>-<M#>-<E#.#>__spec__<epic-name>.md](https://github.com/<owner>/<repo>/blob/<branch>/docs/phases/<P#>__<Phase_Folder>/<P#>-<M#>-<E#.#>__spec__<epic-name>.md)

**Commit:** `<commit-hash>`

<!-- 
  Replace:
  - <P#>-<M#>-<E#.#>__spec__<epic-name>.md with actual filename
  - <commit-hash> with the commit hash where the spec was finalized
  
  Example:
  **Full spec:** [P1-M4-E4.1__spec__templates-and-scaffolding.md](https://github.com/panchew/ai-project-system/blob/master/docs/phases/P1__System_Foundation_and_Adoption/P1-M4-E4.1__spec__templates-and-scaffolding.md)
  **Commit:** `480a09a`
-->

### Summary

[Provide a 1-2 sentence summary of the Epic.]

<!-- Example:
Create complete, ready-to-use templates for all AI Project System artifacts to enable new projects to scaffold documentation in under 5 minutes.
-->

### Problem Statement

[Summarize the problem this Epic solves.]

<!-- Example:
New projects must reverse-engineer spec structure from existing files, creating 20-30 minute setup overhead and increased error rates. This Epic provides copy-paste-ready templates with inline guidance.
-->

### Goals

[List 3-5 key goals from the Epic spec.]

1. [Goal 1]
2. [Goal 2]
3. [Goal 3]
4. [Goal 4]

<!-- Example:
1. Provide templates for all major spec types (Phase, Milestone, Epic, Completion Report, Chat Starter)
2. Include inline guidance and examples within templates
3. Ensure templates align with current governance (v1.3.0)
4. Make front-matter self-documenting
5. Enable scaffolding in under 5 minutes
-->

---

## Deliverables

You must produce:

1. [✅/❌] **[Deliverable 1]** (`<file-path>`)
2. [✅/❌] **[Deliverable 2]** (`<file-path>`)
3. [✅/❌] **[Deliverable 3]** (`<file-path>`)
4. [✅/❌] **[Deliverable 4]** (`<file-path>`)
5. [✅/❌] **Epic Completion Report** (`<file-path>`)

<!-- 
  List all deliverables from Epic spec.
  
  Use checkboxes to track progress during execution.
  
  Example:
  1. ✅ **Phase spec template** (`governance/templates/phase-spec.md`)
  2. ✅ **Milestone spec template** (`governance/templates/milestone-spec.md`)
  3. ✅ **Epic spec template** (`governance/templates/epic-spec.md`)
  4. ✅ **Epic Completion Report** (`docs/phases/P1__System_Foundation_and_Adoption/P1-M4-E4.1__completion__templates-and-scaffolding.md`)
-->

---

## Definition of Done

- [ ] [DoD item 1 from Epic spec]
- [ ] [DoD item 2 from Epic spec]
- [ ] [DoD item 3 from Epic spec]
- [ ] [DoD item 4 from Epic spec]
- [ ] [DoD item 5 from Epic spec]
- [ ] Epic Completion Report produced and committed
- [ ] All changes committed to `epic/<E#.#>` branch
- [ ] Pull request opened to `milestone/<M#>` branch

<!-- 
  Copy Definition of Done items EXACTLY from Epic spec.
  
  Use this checklist to track execution progress.
-->

---

## Acceptance Criteria

- [ ] [Acceptance criterion 1 from Epic spec]
- [ ] [Acceptance criterion 2 from Epic spec]
- [ ] [Acceptance criterion 3 from Epic spec]
- [ ] [Acceptance criterion 4 from Epic spec]

<!-- 
  Copy Acceptance Criteria items EXACTLY from Epic spec.
  
  These will be verified during human review (not by Coding Agent).
-->

---

## Technical Constraints

<!-- 
  Summarize key technical constraints from Epic spec.
  
  Examples:
  - **Format:** Markdown with YAML front-matter
  - **Technology:** No external dependencies
  - **Performance:** Must complete in under 5 seconds
  - **Compatibility:** Must work with existing specs
-->

- **Format:** [Required format]
- **Technology:** [Tech stack or tools]
- **Performance:** [Performance requirements]
- **Compatibility:** [Compatibility requirements]

<!-- Example:
- **Format:** Markdown with YAML front-matter
- **Comments:** Use HTML comment syntax `<!-- comment -->` for inline guidance
- **Examples:** Must be placeholder/generic, not real project data
- **Governance:** Must not contradict or modify governance documents
- **Location:** All templates in `governance/templates/`
-->

---

## Execution Contract

### Your Responsibilities (Coding Agent)

1. **Create branch** `epic/<E#.#>` from current `<base-branch>`
2. **Implement all deliverables** per Epic spec
3. **Verify governance alignment** (templates must reflect current governance)
4. **Create Epic Completion Report** verifying all DoD items
5. **Commit all changes** to `epic/<E#.#>` branch
6. **Open pull request** to `milestone/<M#>` branch
7. **Produce Epic Delivery Notice** upon completion
8. **Stop and await HQ authorization** (do not merge)

<!-- 
  Customize based on Epic requirements.
  
  Common responsibilities:
  - Create feature branch
  - Implement deliverables
  - Write tests (if applicable)
  - Update documentation
  - Create Completion Report
  - Open PR
  - Stop and await review
-->

### What You Must NOT Do

- ❌ Do NOT merge the PR (HQ authorizes merge)
- ❌ Do NOT infer acceptance (HQ decides accept/reject)
- ❌ Do NOT modify governance documents (unless explicitly in scope)
- ❌ Do NOT create automation/tooling (unless explicitly in scope)
- ❌ Do NOT include project-specific content (use generic examples)
- ❌ Do NOT iterate without explicit HQ instruction

<!-- 
  Customize based on Epic scope and constraints.
-->

---

## Reference Materials

### Existing Specs to Reference

<!-- 
  List existing files that provide structural reference.
  
  Examples:
  - Existing specs to copy structure from
  - Templates to enhance
  - Governance documents to align with
-->

For structural reference, examine:
- `<path-to-reference-file-1>`
- `<path-to-reference-file-2>`
- `<path-to-reference-file-3>`

<!-- Example:
For structural reference, examine:
- `docs/phases/P1__System_Foundation_and_Adoption/P1-M1__milestone.md`
- `docs/phases/P1__System_Foundation_and_Adoption/P1-M2-E2.1__spec__human-review-and-acceptance.md`
- `docs/phases/P1__System_Foundation_and_Adoption/P1-M2-E2.1__completion__human-review-and-acceptance.md`
-->

### Front-Matter Fields Reference

<!-- 
  Provide front-matter schema for relevant spec types.
  
  Include examples showing required fields and format.
-->

**Phase spec:**
```yaml
---
project: <project-name>
phase: <P#>
milestone: null
epic: null
type: phase
status: <planned|active|completed>
last_updated: <YYYY-MM-DD>
---
```

**Milestone spec:**
```yaml
---
project: <project-name>
phase: <P#>
milestone: <M#>
type: milestone
status: <planned|active|completed>
last_updated: <YYYY-MM-DD>
---
```

**Epic spec:**
```yaml
---
project: <project-name>
phase: <P#>
milestone: <M#>
epic: <E#.#>
type: spec
status: <planned|active|completed>
last_updated: <YYYY-MM-DD>
---
```

<!-- 
  Include any additional reference materials needed for execution.
-->

---

## Canonical Happy Path (Reminder)

1. ✅ Execution completed (all deliverables created)
2. ✅ Epic Delivery Notice produced (you create this)
3. ⏸️ Human Review performed (human does this)
4. ⏸️ Epic Review Seal produced (human or HQ creates this)
5. ⏸️ HQ decision recorded (HQ decides: accept/reject/iterate)
6. ⏸️ HQ delivery authorization issued (HQ authorizes merge)
7. ⏸️ PR merged (you perform merge after authorization)
8. ⏸️ Execution stops (you stop immediately after merge)

**You are responsible for steps 1-2 only. Then you STOP and await HQ instruction.**

---

## Epic Delivery Notice Template

When you complete execution, produce this artifact:

**File:** `docs/phases/<P#>__<Phase_Folder>/<P#>-<M#>-<E#.#>__delivery-notice.md`

```markdown
---
type: delivery-notice
epic: <E#.#>
status: delivered
delivery_date: <YYYY-MM-DD>
---

# Epic Delivery Notice — <E#.#>

**Epic:** <E#.#> — <Epic Name>  
**Status:** Execution Complete, Delivered to HQ for Review  
**Delivery Date:** <YYYY-MM-DD>

## Execution Summary

[Brief summary of what was completed]

## Deliverables Completed

- [ ] [Deliverable 1]
- [ ] [Deliverable 2]
- [ ] [Deliverable 3]
- [ ] [Epic Completion Report]

## Definition of Done Status

[List each DoD item and confirm completion]

## Branch and PR Information

- **Branch:** `epic/<E#.#>`
- **PR:** [Link to PR]
- **Target:** `milestone/<M#>`
- **Commits:** [Number] commits
- **Files Changed:** [Number] files

## Notes

[Any deviations, challenges, or follow-up items]

## Awaiting HQ Review

This Epic is delivered and awaiting:
1. Human Review
2. Epic Review Seal
3. HQ acceptance decision
4. HQ merge authorization

---

**Coding Agent stopped per AI-OPERATING-GUIDELINES.md canonical happy path.**
```

---

## Exit Conditions

**You MUST stop execution when:**
- ✅ All deliverables are completed and committed
- ✅ Epic Completion Report is created
- ✅ Pull request is opened to `milestone/<M#>`
- ✅ Epic Delivery Notice is produced

**Then report to human:**
"Epic <E#.#> execution complete. Epic Delivery Notice produced. Awaiting HQ review and authorization."

---

## Begin Execution

You may now begin executing Epic <E#.#>.

Start by:
1. Creating branch `epic/<E#.#>` from `<base-branch>`
2. Reviewing Epic spec and reference materials
3. Implementing deliverables per Definition of Done
4. Following the execution checklist

**Good luck, Coding Agent!**
