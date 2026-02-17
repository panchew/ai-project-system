# AI Project System Templates

**Purpose:** This directory contains complete, copy-paste-ready templates for all AI Project System artifacts.

**Goal:** Enable new projects to scaffold complete documentation structure in under 5 minutes.

---

## Available Templates

### Core Specification Templates

| Template | File | When to Use |
|----------|------|-------------|
| **Phase Spec** | [phase-spec.md](phase-spec.md) | Starting a new major phase of work |
| **Milestone Spec** | [milestone-spec.md](milestone-spec.md) | Defining a collection of related Epics within a Phase |
| **Epic Spec** | [epic-spec.md](epic-spec.md) | Defining a single unit of deliverable work |

### Execution & Review Templates

| Template | File | When to Use |
|----------|------|-------------|
| **Epic Execution Chat Starter** | [epic-execution-chat-starter.md](epic-execution-chat-starter.md) | Providing execution context to a Coding Agent |
| **Epic Completion Report** | [epic-completion-report.md](epic-completion-report.md) | Documenting Epic execution results and verification |
| **Epic Review Seal** | [epic-review-seal.md](epic-review-seal.md) | Capturing human review findings before acceptance |
| **Epic Completion Notice** | [epic-completion-notice.md](epic-completion-notice.md) | Notifying stakeholders that an Epic has closed |

---

## When to Create Unplanned Progress Branches

If you encounter ideas, improvements, or refinements during execution that fall **outside current Epic scope**, create an **unplanned progress branch**:

```bash
git checkout milestone/M<N>  # or other stable branch
git checkout -b unplanned/<topic-slug>
# Make commits capturing your ideas
```

**Examples:**
- Template improvements discovered while writing specs
- Governance clarifications identified during execution
- Documentation refinements that help future users

Unplanned branches are reviewed during planning and integrated via future Epics. See PROJECT-SYSTEM-GUIDELINES.md section 8A for details.

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
   - Provide to Coding Agent

2. **After Execution Completes**
   - Coding Agent creates Epic Completion Report using [epic-completion-report.md](epic-completion-report.md)
   - Human reviews deliverables and tests results

3. **Human Review**
   - Copy [epic-review-seal.md](epic-review-seal.md)
   - Fill in findings and recommendation
   - Submit to HQ Chat for decision

4. **After Acceptance**
   - Optionally create Epic Completion Notice using [epic-completion-notice.md](epic-completion-notice.md)
   - Announce completion to stakeholders

---

## Front-Matter Field Reference

All specs use YAML front-matter to enable programmatic parsing and validation.

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

### Epic Completion Report Front-Matter

```yaml
---
project: <project-name>           # Unique project identifier (kebab-case)
phase: <P#>                        # Parent phase ID (e.g., P1)
milestone: <M#>                    # Parent milestone ID (e.g., M1)
epic: <E#.#>                       # Epic ID (e.g., E1.1)
type: completion                   # Identifies this as a completion report
status: completed                  # Always 'completed' for completion reports
last_updated: <YYYY-MM-DD>        # Date of last modification
---
```

**Field Descriptions:**
- `project`, `phase`, `milestone`, `epic`: Must match corresponding epic spec
- `type`: Always `completion` for completion reports
- `status`: Always `completed` for completion reports (Epic is finished)
- `last_updated`: ISO 8601 date of completion report creation or last edit

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
- [Phases Directory](../phases/) — Real-world spec examples
