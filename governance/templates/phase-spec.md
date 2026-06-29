---
project: <project-name>           <!-- Replace with your project identifier (kebab-case, e.g., 'my-web-app') -->
phase: <P#>                        <!-- Replace with phase ID (e.g., P1, P2, P3) -->
milestone: null                    <!-- Always null for phase specs -->
epic: null                         <!-- Always null for phase specs -->
type: phase                        <!-- Do not modify - identifies this as a phase spec -->
status: <planned|active|completed> <!-- Current status: planned, active, or completed -->
last_updated: <YYYY-MM-DD>        <!-- Date of last modification (ISO 8601 format) -->
---

<!-- 
  PHASE SPEC TEMPLATE
  
  Purpose: Define a major phase of work containing multiple milestones.
  
  Usage:
  1. Copy this template
  2. Replace all <placeholders> with actual content
  3. Delete HTML comments (or keep for future reference)
  4. Save as: docs/phases/P<N>__phase__<phase-name>.md
  
  Example filename: docs/phases/P1__phase__system-foundation.md
-->

# Phase <P#> — <Phase Name>

<!-- 
  Phase title format: "Phase P# — <Descriptive Name>"
  Examples:
  - Phase P1 — System Foundation & Adoption
  - Phase P2 — Advanced Features & Integrations
  - Phase P0 — Project Formalization
-->

## Purpose

<!-- 
  Describe the high-level purpose of this phase.
  
  Answer these questions:
  - What is this phase trying to achieve?
  - Why does this phase exist?
  - What value does it deliver?
  
  Keep it concise (2-4 sentences or a short bulleted list).
-->

[Describe the primary purpose and strategic goals of this phase.]

This phase focuses on:
- [Key focus area 1]
- [Key focus area 2]
- [Key focus area 3]

<!-- Example:
Establish the AI Project System as a stable, adoptable, and self-hosting system.

This phase focuses on:
- Governance stability
- System references
- Templates and execution contracts
- Adoption readiness for new projects
-->

---

## In Scope

<!-- 
  Define what IS included in this phase.
  
  Be specific about:
  - Types of work
  - Deliverables
  - Areas of focus
  
  Use bullet points for clarity.
-->

- [Work type or deliverable 1]
- [Work type or deliverable 2]
- [Work type or deliverable 3]
- [Work type or deliverable 4]

<!-- Example:
- Governance documents and versioning
- System references (e.g. project tracker integration)
- Canonical templates
- Adoption and initialization rules
-->

---

## Out of Scope

<!-- 
  Define what IS NOT included in this phase.
  
  This helps prevent scope creep and sets clear boundaries.
  
  Common out-of-scope items:
  - Features deferred to future phases
  - Automation or tooling
  - Specific integrations
  - UI/UX work
-->

- [Out of scope item 1]
- [Out of scope item 2]
- [Out of scope item 3]
- [Out of scope item 4]

<!-- Example:
- Product features
- Automation or CLI tooling
- Web UI or public homepage
- Provider-specific integrations
-->

---

## Exit Criteria

<!-- 
  Define the conditions required for this phase to be considered complete.
  
  Typically:
  - "Phase P# is complete when all milestones under P# are completed and closed."
  
  You can add additional criteria if needed (e.g., governance review, stakeholder acceptance).
-->

Phase <P#> is complete when all milestones under <P#> are completed and closed.

<!-- 
  Optional: Add additional exit criteria if needed
  
  Examples:
  - Governance review completed
  - All Phase-level acceptance criteria met
  - Stakeholder sign-off received
-->

---

## Milestones

<!-- 
  Optional: List planned milestones within this phase.
  
  Format:
  - [M# — Milestone Name](path/to/milestone-spec.md) — Brief description
  
  This section helps readers understand the phase structure at a glance.
-->

- [M1 — <Milestone Name>](P<#>__<Folder>/P<#>-M1__milestone.md) — [Brief description]
- [M2 — <Milestone Name>](P<#>__<Folder>/P<#>-M2__milestone.md) — [Brief description]
- [M3 — <Milestone Name>](P<#>__<Folder>/P<#>-M3__milestone.md) — [Brief description]

<!-- Example:
- [M1 — Genesis & Integration Baseline](P1__System_Foundation/P1-M1__milestone.md) — Establish minimum baseline for project initialization
- [M2 — Review & Acceptance](P1__System_Foundation/P1-M2__milestone.md) — Formalize human review and acceptance workflows
- [M3 — Governance Propagation](P1__System_Foundation/P1-M3__milestone.md) — Enable governance to propagate across projects
-->

---

## Visual Bindings

<!-- 
  Optional. Record links to any generated visuals for this phase, using the binding schema in
  governance/guides/visual-artifacts.md §7 (link + What / Level / State / Description).
  Bind a hosted LINK, never a committed path. A level may carry both a `proposed` binding
  (before build) and an `implemented` binding (after). Omit this section if there are no visuals.
-->

**Visual binding**
- **Link:** <hosted URL of the generated visual>
- **What:** image | infographic | mockup | diagram | clip
- **Level:** Phase
- **State:** proposed | implemented
- **Description:** <short text that survives link rot>

---

## Notes

<!-- 
  Optional: Include any additional context, constraints, or clarifications.
  
  Common uses:
  - Dependencies on other phases
  - Key assumptions
  - Risk factors
  - Open questions
-->

[Any additional notes, constraints, or context for this phase.]

<!-- Example:
This phase is the foundational phase of the AI Project System and must be completed before any dependent projects can fully adopt the system.
-->
