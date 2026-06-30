---
project: <project-name>           <!-- Replace with your project identifier (must match parent milestone) -->
phase: <P#>                        <!-- Replace with parent phase ID (e.g., P1) -->
milestone: <M#>                    <!-- Replace with parent milestone ID (e.g., M1) -->
epic: <E#.#>                       <!-- Replace with epic ID (e.g., E1.1, E2.3) -->
type: spec                         <!-- Do not modify - identifies this as an epic spec -->
status: <planned|active|completed> <!-- Current status: planned, active, or completed -->
last_updated: <YYYY-MM-DD>        <!-- Date of last modification (ISO 8601 format) -->
---

<!-- 
  EPIC SPEC TEMPLATE
  
  Purpose: Define a single unit of deliverable work within a Milestone.
  
  Usage:
  1. Copy this template
  2. Replace all <placeholders> with actual content
  3. Delete HTML comments (or keep for future reference)
  4. Save as: docs/phases/P<N>__<Phase_Folder>/P<N>-M<N>-E<N>.<N>__spec__<epic-name>.md
  
  Example filename: docs/phases/P1__System_Foundation/P1-M1-E1.1__spec__project-tracker-integration.md
-->

# Epic <E#.#> — <Epic Name>

<!-- 
  Epic title format: "Epic E#.# — <Descriptive Name>"
  Examples:
  - Epic E1.1 — Project Tracker Integration System
  - Epic E2.1 — Human Review, Acceptance & Review Seals
  - Epic E3.2 — Template Scaffolding
-->

## Context

<!-- 
  Provide background and context for this Epic.
  
  Answer:
  - What has happened before this Epic?
  - What state is the system in?
  - Why is this Epic needed now?
  
  Typical length: 2-5 paragraphs
-->

[Provide context for this Epic. What is the current state? What led to this work?]

<!-- Example:
Milestone M1 established the foundational mechanics of the AI Project System and validated that the Phase–Milestone–Epic model works end-to-end.

During real-world usage across multiple projects, a critical gap was identified: projects could not track Epic progress in external systems like GitHub Projects or Linear, creating friction for teams using external project management tools.

This Epic addresses that gap by defining a lightweight integration system.
-->

---

## Problem Statement

<!-- 
  Clearly articulate the problem this Epic solves.
  
  Answer:
  - What is broken, missing, or inefficient?
  - What pain does this cause?
  - What happens if this Epic is not completed?
  
  Be specific and concrete.
-->

[Describe the specific problem this Epic solves.]

<!-- Example:
The current system has no mechanism for:
- Tracking Epic status in external project management tools
- Syncing Epic metadata (phase, milestone, status) with external trackers
- Notifying external systems when Epics are completed

This creates manual overhead and prevents teams from using their preferred project management tools.
-->

---

## Goals

<!-- 
  List the specific goals of this Epic.
  
  Goals should be:
  - Concrete and measurable
  - Outcome-focused (what will be achieved, not how)
  - Achievable within the Epic scope
-->

By the end of this Epic, the system must:

1. [Goal 1: Specific, measurable outcome]
2. [Goal 2: Specific, measurable outcome]
3. [Goal 3: Specific, measurable outcome]
4. [Goal 4: Specific, measurable outcome]

<!-- Example:
By the end of this Epic, the system must:

1. Define a standard integration format for external project trackers
2. Provide documentation for integrating with GitHub Projects
3. Demonstrate end-to-end integration with at least one external tracker
4. Enable Epic metadata to be synced automatically
-->

---

## Non-Goals

<!-- 
  Define what this Epic explicitly does NOT aim to achieve.
  
  This prevents scope creep and sets clear boundaries.
  
  Common non-goals:
  - Automation or tooling (unless explicitly in scope)
  - Features deferred to future Epics
  - Out-of-scope integrations
-->

This Epic explicitly does **not** aim to:

- [Non-goal 1: What is deferred or out of scope]
- [Non-goal 2: What is deferred or out of scope]
- [Non-goal 3: What is deferred or out of scope]

<!-- Example:
This Epic explicitly does **not** aim to:

- Build automated sync tooling (CLI, bots, or APIs)
- Support all project management tools (only GitHub Projects initially)
- Modify existing Epic specs or governance documents
-->

---

## Scope of Work

<!-- 
  Define the work required to complete this Epic.
  
  Break down into major work streams or components.
  
  Use headings (###) to organize work into logical sections.
  Be specific about what will be created, modified, or removed.
-->

### 1. [Work Stream 1 Name]

[Describe the first major component of work.]

**Must include:**
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

### 2. [Work Stream 2 Name]

[Describe the second major component of work.]

**Must include:**
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

### 3. [Work Stream 3 Name]

[Describe the third major component of work.]

**Must include:**
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

<!-- Example:
### 1. Integration Format Definition

Define a standard format for representing Epic metadata in external trackers.

**Must include:**
- Epic ID mapping
- Status field mapping
- Phase and Milestone metadata
- Completion date tracking

### 2. GitHub Projects Integration

Document how to integrate with GitHub Projects.

**Must include:**
- Setup instructions
- Field mapping reference
- Example project configuration
- Troubleshooting guide
-->

---

## Deliverables

<!-- 
  List the concrete artifacts this Epic will produce.
  
  Deliverables should be:
  - Specific files, documents, or code
  - Testable or verifiable
  - Checkboxes for tracking
-->

This Epic must produce:

- [ ] [Deliverable 1: Specific file or artifact]
- [ ] [Deliverable 2: Specific file or artifact]
- [ ] [Deliverable 3: Specific file or artifact]
- [ ] [Deliverable 4: Specific file or artifact]
- [ ] [Delivery Notice]

<!-- Example:
This Epic must produce:

- [ ] Integration format specification document
- [ ] GitHub Projects integration guide
- [ ] Example project configuration
- [ ] Delivery Notice
-->

---

## Definition of Done

<!-- 
  Define the INTERNAL checklist that verifies all work is complete.
  
  Definition of Done answers: "Is the Epic implemented correctly?"
  
  Format: Checkboxes for each DoD item
  
  DoD items are typically:
  - Work completed (code written, docs created)
  - Tests passing
  - Documentation updated
  - No known blockers
  
  DoD is verified by the Coding Agent in the Delivery Notice.
-->

Epic <E#.#> is complete when:

- [ ] [DoD item 1: Work completion check]
- [ ] [DoD item 2: Quality check]
- [ ] [DoD item 3: Documentation check]
- [ ] [DoD item 4: Integration check]
- [ ] [Delivery Notice produced and committed]
- [ ] [Pull request opened to milestone branch]

<!-- Example:
Epic E1.1 is complete when:

- [ ] Integration format specification is documented
- [ ] GitHub Projects integration guide is complete
- [ ] Example configuration is tested and verified
- [ ] All documentation is committed to the repository
- [ ] Delivery Notice produced and committed
- [ ] Pull request opened to milestone/M1 branch
-->

---

## Acceptance Criteria

<!-- 
  Define the EXTERNAL conditions that verify the Epic delivers value.
  
  Acceptance Criteria answer: "Does this Epic solve the problem and meet user needs?"
  
  Format: Checkboxes or bullet points
  
  Acceptance Criteria are typically:
  - User-facing outcomes
  - Business value delivered
  - Functional requirements met
  
  Acceptance Criteria are verified during Human Review (see AI-OPERATING-GUIDELINES.md).
  
  IMPORTANT: Acceptance Criteria are NOT the same as Definition of Done.
  - DoD = internal quality/completeness checks
  - Acceptance Criteria = external value/fitness checks
-->

- [ ] [Acceptance criterion 1: User-facing outcome or capability]
- [ ] [Acceptance criterion 2: User-facing outcome or capability]
- [ ] [Acceptance criterion 3: User-facing outcome or capability]
- [ ] [Acceptance criterion 4: User-facing outcome or capability]

<!-- Example:
- [ ] A user can integrate Epic tracking with GitHub Projects in under 10 minutes
- [ ] Epic status updates are reflected in GitHub Projects within 1 minute
- [ ] Phase and Milestone metadata is visible in GitHub Projects
- [ ] Integration does not require coding (configuration only)
-->

---

## Technical Constraints

<!-- 
  Optional: Define technical limitations, requirements, or standards.
  
  Examples:
  - Technology stack restrictions
  - Format requirements (e.g., Markdown, YAML)
  - Performance constraints
  - Compatibility requirements
-->

**Format:** [Required format, e.g., Markdown, JSON, YAML]  
**Technology:** [Required tech stack or tools]  
**Performance:** [Performance requirements, if any]  
**Compatibility:** [Compatibility requirements, e.g., must work with existing specs]  

<!-- Example:
**Format:** Markdown with YAML front-matter  
**Technology:** No external dependencies; pure documentation  
**Performance:** N/A (documentation only)  
**Compatibility:** Must work with existing Epic spec format  
-->

---

## Dependencies

<!-- 
  Optional: List dependencies on other Epics, external systems, or teams.
  
  Format:
  - Dependency type: Description
  - Include links to dependent Epics if applicable
-->

**Internal Dependencies:**
- [Epic or Milestone ID]: [Description of dependency]

**External Dependencies:**
- [External system or team]: [Description of dependency]

**Blockers:**
- [Any known blockers or risks]

<!-- Example:
**Internal Dependencies:**
- Epic E1.1 must be completed before E1.2 can begin

**External Dependencies:**
- GitHub Projects API must be accessible

**Blockers:**
- None
-->

---

## Timeline

<!-- 
  Optional: Provide estimated effort or target dates.
  
  Note: Timelines are guidance, not hard deadlines. Update as needed.
-->

**Estimated Effort:** [e.g., 2-3 days, 1 week, or "TBD"]  
**Target Completion:** [YYYY-MM-DD or "TBD"]  
**Actual Completion:** [YYYY-MM-DD or "In progress"]

---

## Execution Notes

<!-- 
  Optional: Provide guidance for the Coding Agent executing this Epic.
  
  Common uses:
  - Where to start
  - Implementation order
  - Key decisions already made
  - Links to reference materials
-->

[Provide guidance for execution, if applicable.]

<!-- Example:
Execution order:
1. Define integration format first
2. Create GitHub Projects guide second
3. Test integration with example project
4. Document findings in Delivery Notice
-->

---

## Related Documents

<!-- 
  Optional: Link to related specs, governance docs, or context files.
  
  Examples:
  - Parent milestone spec
  - Related Epics
  - Governance documents
  - External references
-->

- [Parent Milestone Spec](P<#>-M<#>__milestone.md)
- [Related Epic Spec](P<#>-M<#>-E<#>.<#>__spec__<name>.md)
- [PROJECT-SYSTEM-GUIDELINES.md](../../PROJECT-SYSTEM-GUIDELINES.md)
- [AI-OPERATING-GUIDELINES.md](../../AI-OPERATING-GUIDELINES.md)

<!-- Example:
- [Milestone M1 Spec](P1-M1__milestone.md)
- [Epic E1.2 Spec](P1-M1-E1.2__spec__execution-contracts.md)
- [PROJECT-SYSTEM-GUIDELINES.md](../../PROJECT-SYSTEM-GUIDELINES.md)
-->

---

## Visual Bindings

<!-- 
  Optional. Record links to any generated visuals for this Epic, using the binding schema in
  governance/guides/visual-artifacts.md §7 (link + What / Level / State / Description).
  Bind a hosted LINK, never a committed path. A level may carry both a `proposed` binding
  (before build) and an `implemented` binding (after). Omit this section if there are no visuals.
-->

**Visual binding**
- **Link:** <hosted URL of the generated visual>
- **What:** image | infographic | mockup | diagram | clip
- **Level:** Epic
- **State:** proposed | implemented
- **Description:** <short text that survives link rot>

---

## Notes

<!-- 
  Optional: Include any additional context, clarifications, or open questions.
  
  Common uses:
  - Decisions made during planning
  - Risks or concerns
  - Follow-up Epics
  - Known limitations
-->

[Any additional notes, risks, or follow-up items.]

<!-- Example:
This Epic focuses on documentation only. Future Epics may add automation for syncing Epic status automatically.
-->
