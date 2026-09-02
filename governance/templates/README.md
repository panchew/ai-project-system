# AI Project System Templates

**Purpose:** This directory contains complete, copy-paste-ready templates for all AI Project System artifacts.

**Goal:** Enable new projects to scaffold complete documentation structure in under 5 minutes.

---

## Available Templates

### Project Bootstrap Template

| Template | File | When to Use |
|----------|------|-------------|
| **Genesis** | [genesis.md](genesis.md) | Starting a brand-new project — the Creation Chat fills this out to produce the committed `genesis.md` that lets a Phase Chat open (see [`../systems/start-a-project.md`](../systems/start-a-project.md)) |

### Core Specification Templates

| Template | File | When to Use |
|----------|------|-------------|
| **Phase Spec** | [phase-spec.md](phase-spec.md) | Starting a new major phase of work |
| **Milestone Spec** | [milestone-spec.md](milestone-spec.md) | Defining a collection of related Epics within a Phase |
| **Epic Spec** | [epic-spec.md](epic-spec.md) | Defining a single unit of deliverable work |

### Execution & Review Templates

| Template | File | When to Use |
|----------|------|-------------|
| **Epic Execution Chat Starter** | [epic-execution-chat-starter.md](epic-execution-chat-starter.md) | Providing execution context to the Governance Agent (Epic mode) |
| **Epic Review Seal** | [epic-review-seal.md](epic-review-seal.md) | Capturing human review findings before acceptance |

### Artifact Communication Templates (P4)

| Template | File | When to Use |
|----------|------|-------------|
| **Completion Notice (Epic)** | [completion-notice-epic.md](completion-notice-epic.md) | Epic Agent signals work is finished and ready for Milestone review |
| **Review Decision** | [review-decision.md](review-decision.md) | Exception path only — reviewing chat issues Accept-with-follow-ups or Reject on a Completion Notice that isn't clean; a clean delivery is accepted by silence (PROJECT-SYSTEM-GUIDELINES.md §11.6) |
| **Delivery Notice** | [delivery-notice.md](delivery-notice.md) | Epic Agent records the delivery after acceptance |
| **Merge Authorization** | [merge-authorization.md](merge-authorization.md) | The parent's record of the merge it performed of an accepted Epic's branch (PSG §11.6 — a child never holds merge authorization) |
| **Epic Closure Notice** | [epic-closure-notice.md](epic-closure-notice.md) | Coding Agent confirms a merge completed, to the Milestone Chat |
| **Escalation Notice** | [escalation-notice.md](escalation-notice.md) | Any chat escalates a blocking or out-of-scope finding to its parent |

### Creation Chat Ongoing Templates (P4-M19)

| Template | File | When to Use |
|----------|------|-------------|
| **Steering Note** | [steering-note.md](steering-note.md) | A chat (typically Creation Chat) hands off open concerns and binding decisions to its parent (typically HQ) — at session end before a reset, or when a blocking concern arises (see [`../systems/creation-chat-guide.md`](../systems/creation-chat-guide.md)) |
| **Progress Digest** | [progress-digest.md](progress-digest.md) | HQ Chat sends the Creation Chat a self-contained, high-signal summary of project state at the start of a new phase/milestone or on request |
| **Bouncer Work Log** | [bouncer-work-log.md](bouncer-work-log.md) | Recording a Layer-8 manual intervention (data fix, direct user request, one-off console op) in under two minutes; feeds pattern detection toward a Steering Note |

### Bugfix Workflow Templates (P4.2)

| Template | File | When to Use |
|----------|------|-------------|
| **Deployment Authorization** | [deployment-authorization.md](deployment-authorization.md) | CFO authorizes (or rejects) deploying an Epic or Bugfix Epic to production/staging — the production deployment gate's record |
| **Post-Mortem** | [post-mortem.md](post-mortem.md) | Incident analysis after a Critical/High severity Bugfix Epic resolves (required for Critical/High, optional for Medium/Low) |

> Bugfix Epic specs themselves live in `docs/bugfixes/` under the `B#.#` convention — see
> [`docs/bugfixes/README.md`](../../docs/bugfixes/README.md) and the
> [Bugfix Epic Workflow](../systems/bugfix-epic-workflow.md).

---

## Quick Start Workflow

### Starting a New Project

1. **Create Phase Spec**
   - Copy [phase-spec.md](phase-spec.md)
   - Fill in project name, phase ID, and purpose
   - Define scope and exit criteria
   - Save as `docs/phases/P<N>__phase__<phase-name>.md`

2. **Create Milestone Spec(s)**
   - Copy [milestone-spec.md](milestone-spec.md) for each milestone
   - Fill in milestone ID, purpose, and planned Epics
   - Define completion criteria
   - Save as `docs/phases/P<N>__System_<Folder>/P<N>-M<N>__milestone.md`

3. **Create Epic Spec(s)**
   - Copy [epic-spec.md](epic-spec.md) for each Epic
   - Fill in Epic ID, problem statement, goals, deliverables, DoD
   - Define acceptance criteria
   - Save as `docs/phases/P<N>__System_<Folder>/P<N>-M<N>-E<N>.<N>__spec__<epic-name>.md`

### Executing an Epic

1. **Create Epic Execution Chat Starter**
   - Copy [epic-execution-chat-starter.md](epic-execution-chat-starter.md)
   - Fill in Epic context and references
   - Provide to Governance Agent (Epic mode)

2. **After Execution Completes**
   - Epic mode produces a Completion Notice using [completion-notice-epic.md](completion-notice-epic.md)
   - Human reviews deliverables and test results

3. **Human Review**
   - Copy [epic-review-seal.md](epic-review-seal.md)
   - Fill in findings and recommendation
   - Submit to HQ Chat for decision; the reviewing chat issues a [review-decision.md](review-decision.md)

4. **After Acceptance**
   - Produce a Delivery Notice using [delivery-notice.md](delivery-notice.md) once the PR is merged
   - Announce completion to stakeholders

---

## Front-Matter Field Reference

All specs use YAML front-matter to enable programmatic parsing and validation.

### Genesis Front-Matter

```yaml
---
type: genesis                      # Identifies this as a genesis artifact
project: <project-slug>            # Project name (kebab-case)
created_by: <role or person>       # Creation Chat role or person
date: <YYYY-MM-DD>                 # ISO date the genesis was completed
phase_1_name: <Phase 1 name>      # Short human name of Phase 1
status: <draft|complete>           # draft while filling in; complete when ready to hand off
---
```

**Field Descriptions:**
- `type`: Always `genesis` for genesis artifacts
- `project`: Project identifier (kebab-case, e.g., `taskflow`)
- `created_by`: The role or person acting as Creation Chat
- `date`: ISO 8601 date the genesis was completed
- `phase_1_name`: Short name of Phase 1 (e.g., `Core Task Management`)
- `status`: `draft` while in progress, `complete` once committed and ready for the Phase Chat

### Phase Spec Front-Matter

```yaml
---
project: <project-name>           # Unique project identifier (kebab-case)
phase: <P#>                        # Phase ID (e.g., P1, P2)
milestone: null                    # Always null for phase specs
epic: null                         # Always null for phase specs
type: phase                        # Identifies this as a phase spec
status: <planned|active|completed> # Current phase status
last_updated: <YYYY-MM-DD>        # Date of last modification
---
```

**Field Descriptions:**
- `project`: Unique identifier for your project (use kebab-case, e.g., `my-web-app`)
- `phase`: Phase number (format: `P` + integer, e.g., `P1`, `P2`)
- `type`: Always `phase` for phase specs
- `status`: Lifecycle state — `planned` (not started), `active` (in progress), `completed` (finished)
- `last_updated`: ISO 8601 date of last edit (format: `YYYY-MM-DD`)

### Milestone Spec Front-Matter

```yaml
---
project: <project-name>           # Unique project identifier (kebab-case)
phase: <P#>                        # Parent phase ID (e.g., P1)
milestone: <M#>                    # Milestone ID (e.g., M1, M2)
type: milestone                    # Identifies this as a milestone spec
status: <planned|active|completed> # Current milestone status
last_updated: <YYYY-MM-DD>        # Date of last modification
---
```

**Field Descriptions:**
- `project`: Must match parent phase project identifier
- `phase`: Parent phase ID (e.g., `P1`)
- `milestone`: Milestone number (format: `M` + integer, e.g., `M1`, `M2`)
- `type`: Always `milestone` for milestone specs
- `status`: Lifecycle state — `planned`, `active`, or `completed`
- `last_updated`: ISO 8601 date of last edit

### Epic Spec Front-Matter

```yaml
---
project: <project-name>           # Unique project identifier (kebab-case)
phase: <P#>                        # Parent phase ID (e.g., P1)
milestone: <M#>                    # Parent milestone ID (e.g., M1)
epic: <E#.#>                       # Epic ID (e.g., E1.1, E2.3)
type: spec                         # Identifies this as an epic spec
status: <planned|active|completed> # Current epic status
last_updated: <YYYY-MM-DD>        # Date of last modification
---
```

**Field Descriptions:**
- `project`: Must match parent milestone and phase project identifier
- `phase`: Parent phase ID (e.g., `P1`)
- `milestone`: Parent milestone ID (e.g., `M1`)
- `epic`: Epic number (format: `E` + milestone-scoped integer + `.` + epic sequence, e.g., `E1.1`, `E2.3`)
- `type`: Always `spec` for epic specs
- `status`: Lifecycle state — `planned`, `active`, or `completed`
- `last_updated`: ISO 8601 date of last edit

### Delivery Notice Front-Matter

```yaml
---
project: <project-name>           # Unique project identifier (kebab-case)
phase: <P#>                        # Parent phase ID (e.g., P1)
milestone: <M#>                    # Parent milestone ID (e.g., M1)
epic: <E#.#>                       # Epic ID (e.g., E1.1)
type: completion                   # Identifies this as a Delivery Notice / completion artifact
status: completed                  # Always 'completed' for delivered Epics
last_updated: <YYYY-MM-DD>        # Date of last modification
---
```

**Field Descriptions:**
- `project`, `phase`, `milestone`, `epic`: Must match corresponding epic spec
- `type`: Always `completion` for the Delivery Notice / completion artifact
- `status`: Always `completed` (the Epic is finished)
- `last_updated`: ISO 8601 date of the Delivery Notice's creation or last edit

> The artifact-protocol Completion Notice / Review Decision / Delivery Notice schemas
> (P4) are defined in [`../systems/artifact-communication-protocol.md`](../systems/artifact-communication-protocol.md).

---

## Usage Guidelines

### Inline Comments

Templates include HTML comment blocks `<!-- comment -->` to provide inline guidance. These comments:
- Explain what each section should contain
- Provide examples of good content
- Highlight common pitfalls
- Reference governance requirements

**You should delete comments** when filling in templates, or leave them for future reference.

### Example Content

Templates include placeholder content wrapped in `<angle brackets>` or marked as `[example]`. This content:
- Demonstrates proper format and tone
- Shows expected level of detail
- Illustrates best practices

**Replace all example content** with your actual project content.

### Governance Alignment

All templates align with:
- [PROJECT-SYSTEM-GUIDELINES.md](../PROJECT-SYSTEM-GUIDELINES.md) v1.3.0
- [AI-OPERATING-GUIDELINES.md](../AI-OPERATING-GUIDELINES.md) v1.2.0

If templates conflict with governance, **governance takes precedence**. Report any conflicts as issues.

### File Naming Conventions

Use these naming patterns for consistency:

**Phase specs:**
```
docs/phases/P<N>__phase__<phase-name-kebab-case>.md
```
Example: `docs/phases/P1__phase__system-foundation.md`

**Milestone specs:**
```
docs/phases/P<N>__<Phase_Folder_Name>/P<N>-M<N>__milestone.md
```
Example: `docs/phases/P1__System_Foundation/P1-M1__milestone.md`

**Epic specs:**
```
docs/phases/P<N>__<Phase_Folder_Name>/P<N>-M<N>-E<N>.<N>__spec__<epic-name-kebab-case>.md
```
Example: `docs/phases/P1__System_Foundation/P1-M1-E1.1__spec__project-tracker-integration.md`

**Epic completion reports:**
```
docs/phases/P<N>__<Phase_Folder_Name>/P<N>-M<N>-E<N>.<N>__completion__<epic-name-kebab-case>.md
```
Example: `docs/phases/P1__System_Foundation/P1-M1-E1.1__completion__project-tracker-integration.md`

---

## Template Maintenance

Templates are versioned implicitly through governance document versions.

**Current template version:** Aligned with PROJECT-SYSTEM-GUIDELINES.md v1.3.0

When governance is updated:
- Review templates for alignment
- Update templates as needed
- Document changes in governance changelog

---

## Questions or Issues?

If you encounter:
- Missing fields or sections
- Ambiguous guidance
- Conflicts with governance
- Unclear examples

Create an issue or Epic to address template improvements.

---

## Related Documentation

- [PROJECT-SYSTEM-GUIDELINES.md](../PROJECT-SYSTEM-GUIDELINES.md) — System governance and rules
- [AI-OPERATING-GUIDELINES.md](../AI-OPERATING-GUIDELINES.md) — Agent behavior and execution contracts
- [EPIC-EXECUTION-CHAT-STARTER.md](../EPIC-EXECUTION-CHAT-STARTER.md) — Example chat starter structure
- [Phases Directory](../../docs/phases/) — Real-world spec examples
