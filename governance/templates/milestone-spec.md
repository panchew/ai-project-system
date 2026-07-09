---
project: <project-name>           <!-- Replace with your project identifier (must match parent phase) -->
phase: <P#>                        <!-- Replace with parent phase ID (e.g., P1) -->
milestone: <M#>                    <!-- Replace with milestone ID (e.g., M1, M2) -->
type: milestone                    <!-- Do not modify - identifies this as a milestone spec -->
status: <planned|active|completed> <!-- Current status: planned, active, or completed -->
last_updated: <YYYY-MM-DD>        <!-- Date of last modification (ISO 8601 format) -->
---

<!-- 
  MILESTONE SPEC TEMPLATE
  
  Purpose: Define a collection of related Epics within a Phase.
  
  Usage:
  1. Copy this template
  2. Replace all <placeholders> with actual content
  3. Delete HTML comments (or keep for future reference)
  4. Save as: docs/phases/P<N>__<Phase_Folder>/P<N>-M<N>__milestone.md
  
  Example filename: docs/phases/P1__System_Foundation/P1-M1__milestone.md
-->

# Milestone <M#> — <Milestone Name>

<!-- 
  Milestone title format: "Milestone M# — <Descriptive Name>"
  Examples:
  - Milestone M1 — Genesis & Integration Baseline
  - Milestone M2 — Review & Acceptance Mechanisms
  - Milestone M3 — Governance Propagation
-->

## Purpose

<!-- 
  Describe the high-level purpose of this milestone.
  
  Answer these questions:
  - What is this milestone trying to achieve?
  - Why does this milestone exist within its parent phase?
  - What value does it deliver?
  
  Keep it concise (2-4 sentences).
-->

[Describe the primary purpose and goals of this milestone.]

This milestone ensures:
- [Key outcome 1]
- [Key outcome 2]
- [Key outcome 3]

<!-- Example:
Define the minimum complete baseline required to initialize a project using the AI Project System.

This milestone ensures:
- Governance is canonical and versioned
- Execution contracts are explicit
- External integrations are well-defined and optional
-->

---

## Problem Statement

<!-- 
  Optional but recommended: Describe the problem this milestone solves.
  
  Answer:
  - What gap or need exists?
  - What happens if this milestone is not completed?
  - What pain point does this address?
-->

[Describe the problem or gap this milestone addresses.]

<!-- Example:
Without a baseline integration system, projects using the AI Project System cannot track Epic and Milestone status externally, creating friction for teams using external project management tools.
-->

---

## Goals

<!-- 
  List the specific goals of this milestone.
  
  Goals should be:
  - Concrete and measurable
  - Outcome-focused (not activity-focused)
  - Achievable within the milestone scope
-->

By the end of this milestone, the system must:

1. [Goal 1: Specific, measurable outcome]
2. [Goal 2: Specific, measurable outcome]
3. [Goal 3: Specific, measurable outcome]
4. [Goal 4: Specific, measurable outcome]

<!-- Example:
By the end of this milestone, the system must:

1. Provide a canonical governance document that defines the system rules
2. Define an execution contract for Epics
3. Establish a project tracker integration mechanism
4. Demonstrate end-to-end Epic execution and closure
-->

---

## Non-Goals

<!-- 
  Define what this milestone explicitly does NOT aim to achieve.
  
  This prevents scope creep and sets clear boundaries.
  
  Format: Use bullet points or numbered list.
-->

This milestone explicitly does **not** aim to:

- [Non-goal 1: What is deferred or out of scope]
- [Non-goal 2: What is deferred or out of scope]
- [Non-goal 3: What is deferred or out of scope]

<!-- Example:
This milestone explicitly does **not** aim to:

- Build automation or CLI tooling
- Create a web UI for project tracking
- Implement advanced features (deferred to later phases)
-->

---

## In Scope

<!-- 
  Define what IS included in this milestone.
  
  Be specific about:
  - Types of work
  - Deliverables
  - Areas of focus
-->

- [In-scope work type 1]
- [In-scope work type 2]
- [In-scope work type 3]
- [In-scope work type 4]

<!-- Example:
- Initial governance setup
- Project tracker integration system
- Epic execution standards
- Completion and closure semantics
-->

---

## Out of Scope

<!-- 
  Define what IS NOT included in this milestone.
  
  Common out-of-scope items:
  - Features deferred to future milestones
  - Automation or tooling
  - Advanced integrations
-->

- [Out-of-scope item 1]
- [Out-of-scope item 2]
- [Out-of-scope item 3]

<!-- Example:
- Automation
- UI or visualization
- Advanced tooling
-->

---

## Planned Epics

<!-- 
  List the Epics planned for this milestone.
  
  Format:
  - [E#.# — Epic Name](path/to/epic-spec.md) — Brief description
  
  Note: Epics can be added or deferred during execution. This is the initial plan.
-->

### Confirmed Epics

- [E<#>.<#> — <Epic Name>](P<#>-M<#>-E<#>.<#>__spec__<epic-name>.md) — [Brief description]
- [E<#>.<#> — <Epic Name>](P<#>-M<#>-E<#>.<#>__spec__<epic-name>.md) — [Brief description]

<!-- Example:
### Confirmed Epics

- [E1.1 — Project Tracker Integration System](P1-M1-E1.1__spec__project-tracker-integration-system.md) — Define integration with external trackers
- [E1.2 — Execution Contracts](P1-M1-E1.2__spec__execution-contracts.md) — Formalize Epic execution rules
-->

### Deferred Epics

<!-- 
  Optional: List Epics that were planned but deferred to a later milestone.
-->

- [E<#>.<#> — <Epic Name>] — Deferred to [Milestone M<#>] — [Reason]

<!-- Example:
- [E1.3 — Advanced Automation] — Deferred to M2 — Out of scope for baseline
-->

---

## Completion Criteria

<!-- 
  Define the conditions required for this milestone to be considered complete.
  
  Typically:
  - "Milestone M# is complete when all Epics under M# are completed and closed."
  
  You can add additional criteria if needed.
-->

Milestone <M#> is complete when all Epics under <M#> are completed and closed.

<!-- 
  Optional: Add additional completion criteria
  
  Examples:
  - All milestone-level acceptance criteria met
  - Integration tests passing
  - Documentation updated
  - Stakeholder review completed
-->

---

## Acceptance Criteria

<!-- 
  Optional: Define measurable conditions that verify milestone success.
  
  Format: Checkboxes or bullet points
  
  Acceptance criteria answer: "How do we know this milestone achieved its goals?"
-->

- [ ] [Acceptance criterion 1: Measurable, testable condition]
- [ ] [Acceptance criterion 2: Measurable, testable condition]
- [ ] [Acceptance criterion 3: Measurable, testable condition]

<!-- Example:
- [ ] A new project can initialize using the AI Project System in under 10 minutes
- [ ] Project tracker integration is documented and tested
- [ ] At least one Epic has been executed end-to-end successfully
-->

---

## Dependencies

<!-- 
  Optional: List dependencies on other milestones, phases, or external systems.
  
  Format:
  - Dependency type: Description
-->

**Internal Dependencies:**
- [Milestone or Phase ID]: [Description of dependency]

**External Dependencies:**
- [External system or team]: [Description of dependency]

<!-- Example:
**Internal Dependencies:**
- Phase P0 must be completed before M1 can begin

**External Dependencies:**
- None
-->

---

## Timeline

<!-- 
  Optional: Provide estimated or target dates.
  
  Note: Timelines are guidance, not hard deadlines. Update as needed.
-->

**Target Start:** [YYYY-MM-DD or "TBD"]  
**Target Completion:** [YYYY-MM-DD or "TBD"]  
**Actual Start:** [YYYY-MM-DD or "Not started"]  
**Actual Completion:** [YYYY-MM-DD or "In progress"]

---

## Visual Bindings

<!-- 
  Optional. Record links to any generated visuals for this milestone, using the binding schema in
  governance/guides/visual-artifacts.md §7 (link + What / Level / State / Description).
  Bind a hosted LINK, never a committed path. A level may carry both a `proposed` binding
  (before build) and an `implemented` binding (after). Omit this section if there are no visuals.
-->

**Visual binding**
- **Link:** <hosted URL of the generated visual>
- **What:** image | infographic | mockup | diagram | clip
- **Level:** Milestone
- **State:** proposed | implemented
- **Description:** <short text that survives link rot>

---

## Notes

<!-- 
  Optional: Include any additional context, constraints, or clarifications.
  
  Common uses:
  - Key decisions made during planning
  - Risk factors
  - Open questions
  - Links to related documentation
-->

[Any additional notes, constraints, or context for this milestone.]

<!-- Example:
This milestone establishes the baseline for all future work. Completing it is a prerequisite for any project adopting the AI Project System.
-->
