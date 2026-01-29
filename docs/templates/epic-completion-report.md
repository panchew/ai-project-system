---
project: <project-name>           <!-- Replace with your project identifier (must match Epic spec) -->
phase: <P#>                        <!-- Replace with parent phase ID (must match Epic spec) -->
milestone: <M#>                    <!-- Replace with parent milestone ID (must match Epic spec) -->
epic: <E#.#>                       <!-- Replace with epic ID (must match Epic spec) -->
type: completion                   <!-- Do not modify - identifies this as a completion report -->
status: completed                  <!-- Always 'completed' for completion reports -->
last_updated: <YYYY-MM-DD>        <!-- Date of completion report creation (ISO 8601 format) -->
---

<!-- 
  EPIC COMPLETION REPORT TEMPLATE
  
  Purpose: Document Epic execution results and verify Definition of Done.
  
  Usage:
  1. Copy this template
  2. Replace all <placeholders> with actual content
  3. Verify all DoD items from Epic spec
  4. Delete HTML comments (or keep for future reference)
  5. Save as: docs/phases/P<N>__<Phase_Folder>/P<N>-M<N>-E<N>.<N>__completion__<epic-name>.md
  
  Example filename: docs/phases/P1__System_Foundation/P1-M1-E1.1__completion__project-tracker-integration.md
  
  IMPORTANT: This report is created by the Coding Agent AFTER execution is complete.
-->

# Epic <E#.#> Completion Report — <Epic Name>

<!-- 
  Title format: "Epic E#.# Completion Report — <Epic Name>"
  Examples:
  - Epic E1.1 Completion Report — Project Tracker Integration System
  - Epic E2.1 Completion Report — Human Review, Acceptance & Review Seals
-->

## Executive Summary

<!-- 
  Provide a brief (2-4 sentence) summary of Epic execution.
  
  Answer:
  - Was the Epic executed successfully?
  - What was delivered?
  - Is the Epic ready for human review?
  
  Keep it concise and factual.
-->

Epic <E#.#> has been **executed and delivered successfully**.

[Provide 1-2 sentences summarizing what was accomplished.]

[State readiness for review, e.g., "All deliverables are complete and ready for human review."]

<!-- Example:
Epic E1.1 has been **executed and delivered successfully**.

This Epic defined a lightweight integration system for external project trackers, documented GitHub Projects integration, and provided example configurations.

All deliverables are complete and ready for human review.
-->

---

## Deliverables

<!-- 
  List all deliverables from the Epic spec and confirm their completion.
  
  Format:
  ### Deliverable #: [Name]
  - **File/Location:** [Path to file or artifact]
  - **Status:** ✅ Complete | ⚠️ Partial | ❌ Not delivered
  - **Description:** [Brief description of what was delivered]
  - **Notes:** [Any relevant notes, deviations, or clarifications]
-->

### Deliverable 1: [Deliverable Name]

**File/Location:** [Path to file or URL]  
**Status:** ✅ Complete  
**Description:** [What was delivered]  
**Notes:** [Any relevant context]

### Deliverable 2: [Deliverable Name]

**File/Location:** [Path to file or URL]  
**Status:** ✅ Complete  
**Description:** [What was delivered]  
**Notes:** [Any relevant context]

### Deliverable 3: [Deliverable Name]

**File/Location:** [Path to file or URL]  
**Status:** ✅ Complete  
**Description:** [What was delivered]  
**Notes:** [Any relevant context]

<!-- Example:
### Deliverable 1: Integration Format Specification

**File/Location:** `/docs/systems/project-tracker-integration.md`  
**Status:** ✅ Complete  
**Description:** Documented standard format for Epic metadata in external trackers  
**Notes:** Includes field mappings, status values, and metadata structure

### Deliverable 2: GitHub Projects Integration Guide

**File/Location:** `/docs/integrations/github-projects.md`  
**Status:** ✅ Complete  
**Description:** Step-by-step guide for integrating with GitHub Projects  
**Notes:** Includes setup instructions, field mappings, and troubleshooting
-->

---

## Definition of Done Verification

<!-- 
  Verify EACH Definition of Done item from the Epic spec.
  
  Format:
  ✅ **[DoD Item]**
  - [Explanation of how this was satisfied]
  - [Evidence: file path, test results, etc.]
  
  Copy DoD items EXACTLY from Epic spec and confirm each one.
-->

Referencing the Epic <E#.#> spec Definition of Done:

✅ **[DoD item 1 from spec]**
- [How this was satisfied]
- [Evidence or reference]

✅ **[DoD item 2 from spec]**
- [How this was satisfied]
- [Evidence or reference]

✅ **[DoD item 3 from spec]**
- [How this was satisfied]
- [Evidence or reference]

✅ **[DoD item 4 from spec]**
- [How this was satisfied]
- [Evidence or reference]

✅ **[DoD item 5 from spec]**
- [How this was satisfied]
- [Evidence or reference]

**All Definition of Done items are satisfied.**

<!-- Example:
Referencing the Epic E1.1 spec Definition of Done:

✅ **Integration format specification is documented**
- Created `/docs/systems/project-tracker-integration.md`
- Document includes field mappings, status values, and metadata structure

✅ **GitHub Projects integration guide is complete**
- Created `/docs/integrations/github-projects.md`
- Guide includes setup, configuration, and troubleshooting

✅ **Example configuration is tested and verified**
- Example project created and tested
- Configuration verified to work with GitHub Projects API

✅ **All documentation is committed to the repository**
- All files committed to `epic/E1.1` branch
- PR opened to `milestone/M1` branch

✅ **Epic Completion Report produced and committed**
- This report serves as the completion artifact

**All Definition of Done items are satisfied.**
-->

---

## Acceptance Criteria Verification

<!-- 
  Verify EACH Acceptance Criterion from the Epic spec.
  
  Format:
  ✅ **[Acceptance criterion from spec]**
  - [How this was verified or tested]
  - [Results or evidence]
  
  Copy Acceptance Criteria EXACTLY from Epic spec and verify each one.
  
  Note: Acceptance Criteria verification is PRELIMINARY. Human review will make final acceptance decision.
-->

Referencing the Epic <E#.#> spec Acceptance Criteria:

✅ **[Acceptance criterion 1 from spec]**
- [How this was tested or verified]
- [Results]

✅ **[Acceptance criterion 2 from spec]**
- [How this was tested or verified]
- [Results]

✅ **[Acceptance criterion 3 from spec]**
- [How this was tested or verified]
- [Results]

✅ **[Acceptance criterion 4 from spec]**
- [How this was tested or verified]
- [Results]

**All Acceptance Criteria are preliminarily satisfied. Final acceptance decision pending human review.**

<!-- Example:
Referencing the Epic E1.1 spec Acceptance Criteria:

✅ **A user can integrate Epic tracking with GitHub Projects in under 10 minutes**
- Tested integration setup following documented guide
- Timed at 8 minutes for complete setup

✅ **Epic status updates are reflected in GitHub Projects within 1 minute**
- Manually tested status sync
- Updates reflected immediately after commit

✅ **Phase and Milestone metadata is visible in GitHub Projects**
- Verified custom fields for phase and milestone
- Metadata correctly populated and visible

✅ **Integration does not require coding (configuration only)**
- No code required; configuration-based only
- Setup uses GitHub UI and YAML configuration

**All Acceptance Criteria are preliminarily satisfied. Final acceptance decision pending human review.**
-->

---

## Key Decisions

<!-- 
  Optional: Document any significant decisions made during execution.
  
  Examples:
  - Technology choices
  - Design decisions
  - Trade-offs made
  - Scope adjustments
-->

[List key decisions made during execution, if any.]

1. **[Decision topic]:** [What was decided and why]
2. **[Decision topic]:** [What was decided and why]
3. **[Decision topic]:** [What was decided and why]

<!-- Example:
1. **Integration format:** Chose YAML front-matter over JSON for consistency with existing Epic specs
2. **GitHub Projects:** Focused on GitHub Projects v2 (new Projects) instead of classic Projects
3. **Automation:** Deferred automated sync to future Epic; this Epic focuses on manual integration
-->

---

## Constraints & Non-Goals

<!-- 
  Confirm that Non-Goals from the Epic spec were respected.
  
  Format:
  ✅ **[Non-goal from spec]**
  - [Confirmation that this was not attempted]
-->

Referencing the Epic <E#.#> spec Non-Goals:

✅ **[Non-goal 1 from spec]**
- [Confirmation this was not done]

✅ **[Non-goal 2 from spec]**
- [Confirmation this was not done]

✅ **[Non-goal 3 from spec]**
- [Confirmation this was not done]

<!-- Example:
Referencing the Epic E1.1 spec Non-Goals:

✅ **Build automated sync tooling (CLI, bots, or APIs)**
- No automation was created; integration is manual

✅ **Support all project management tools**
- Only GitHub Projects was documented

✅ **Modify existing Epic specs or governance documents**
- No changes were made to governance or existing specs
-->

---

## Completion Declaration

<!-- 
  Formal declaration that Epic execution is complete.
  
  This section should:
  - State Epic is complete
  - Reference governance (AI-OPERATING-GUIDELINES.md)
  - State agent is stopping and awaiting human review
-->

This Epic is **complete** per the Definition of Done.

All deliverables have been produced, all DoD items are satisfied, and Acceptance Criteria are preliminarily verified.

Per AI-OPERATING-GUIDELINES.md:
- Execution is complete
- This Completion Report serves as the execution artifact
- Coding Agent is now stopping and awaiting human review

**Next Steps (per canonical happy path):**
1. Human Review — Human tests deliverables and reviews findings
2. Epic Review Seal — Human creates Epic Review Seal with findings
3. HQ Decision — HQ Chat makes acceptance decision (accept/reject/iterate)
4. Delivery Authorization — HQ authorizes PR merge (if accepted)

**Coding Agent execution stopped. Awaiting HQ review and authorization.**

<!-- 
  Do not modify this section. It follows the canonical happy path defined in AI-OPERATING-GUIDELINES.md.
-->

---

## Notes

<!-- 
  Optional: Include any additional context or follow-up items.
  
  Common uses:
  - Known limitations
  - Suggested follow-up Epics
  - Open questions for human review
  - Risks or concerns
-->

[Any additional notes, follow-up items, or context for human review.]

<!-- Example:
**Known Limitations:**
- Integration is manual; automated sync would improve UX (suggest follow-up Epic)

**Suggested Follow-Ups:**
- Epic E1.2: Automated sync tooling for GitHub Projects

**Notes:**
- GitHub Projects API is stable and well-documented; no issues encountered during testing
-->
