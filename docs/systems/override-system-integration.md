---
project: ai-project-system
phase: P2
milestone: M9
epic: E9.2
type: system
status: active
last_updated: 2026-05-21
---

# Override System Integration

**Epic:** E9.2 — Document Override Boundaries and System Integration  
**Governance Reference:** `governance/PROJECT-SYSTEM-GUIDELINES.md` §14C  
**Boundaries Reference:** `governance/override-boundaries.md`

---

## Purpose

This document describes how override values declared in `.ai-project.yml` propagate through the AI Project System — from configuration entry to artifact output. It is the reference for understanding the override flow, resolution points, and template integration.

---

## Override Flow

The override flow traces a value from its declaration in `.ai-project.yml` through the HQ agent to its appearance in generated artifacts.

```
┌─────────────────────────────────────────────────────────────┐
│  1. DECLARATION                                             │
│  .ai-project.yml (overrides block)                          │
│  e.g., overrides.epic_prefix: feature/                      │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  2. READ ON STARTUP                                         │
│  HQ agent reads .ai-project.yml on startup                  │
│  → Parses overrides block                                   │
│  → Validates values against governance rules                 │
│  → Produces warning for unknown keys                        │
│  → Produces error for invalid field values                  │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  3. CACHE IN SESSION CONTEXT                                │
│  HQ agent caches resolved override values:                  │
│  session.overrides = {                                      │
│    epic_prefix: "feature/",                                 │
│    merge_strategy: "squash",                                │
│    branch_strategy: "gitflow"                               │
│  }                                                          │
│  Resolution follows precedence hierarchy:                   │
│  local decision > .ai-project.yml > governance default      │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  4. APPLY DURING ARTIFACT GENERATION                        │
│  HQ agent consults cached overrides when generating:        │
│  → Phase specs                                              │
│  → Milestone specs                                          │
│  → Epic specs                                               │
│  → Chat Starters                                            │
│  → Execution instructions                                   │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  5. RESOLVED VALUES IN ARTIFACTS                            │
│  Generated artifacts contain resolved values:               │
│  - Branch names use custom prefix                           │
│  - Merge instructions reference custom strategy             │
│  - Branch strategy referenced in execution instructions     │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  6. CODING AGENT RECEIVES                                   │
│  Coding Agent reads Chat Starter with resolved values        │
│  → Uses custom branch prefix for branch creation            │
│  → Follows merge strategy in PR instructions                │
│  → Follows branch strategy for promotion                    │
└─────────────────────────────────────────────────────────────┘
```

---

## Override Resolution Points

The HQ agent consults override values at specific points during artifact generation:

### Phase Spec Generation
| Override Field | Where Used | Behavioral Effect |
|---------------|------------|-------------------|
| `epic_prefix` | Branch naming references in phase planning | Generated branch names in phase specs use custom prefix |
| `merge_strategy` | Merge strategy references in phase planning | Generated merge instructions reference custom strategy |
| `branch_strategy` | Branch hierarchy description | Phase spec describes the active branch strategy |

### Milestone Spec Generation
| Override Field | Where Used | Behavioral Effect |
|---------------|------------|-------------------|
| `epic_prefix` | Epic branch references within milestone | Milestone spec references epic branches with custom prefix |
| `merge_strategy` | PR merge instructions | Milestone PR instructions reference custom merge method |
| `branch_strategy` | Branch promotion flow | Milestone spec describes correct promotion path |

### Epic Spec Generation
| Override Field | Where Used | Behavioral Effect |
|---------------|------------|-------------------|
| `epic_prefix` | Epic branch name | Epic branch named `<prefix>E<id>` (e.g., `feature/E9.2`) |
| `merge_strategy` | PR merge instructions in spec | Epic spec references custom merge method |
| `branch_strategy` | Branch target validation | Epic spec references correct target branch conventions |

### Chat Starter Generation
| Override Field | Where Used | Behavioral Effect |
|---------------|------------|-------------------|
| `epic_prefix` | Branch creation instruction | Chat Starter instructs agent to use `<prefix>E<id>` |
| `merge_strategy` | Merge instruction | Chat Starter references custom merge method |
| `branch_strategy` | Execution instructions | Chat Starter references correct branch strategy |

---

## Artifact Mapping

Each override field maps to specific templates and artifact types:

| Override Field | Affected Templates | Affected Artifacts |
|---------------|-------------------|-------------------|
| `epic_prefix` | `governance/templates/epic-spec.md`, `governance/templates/epic-execution-chat-starter.md`, `governance/templates/milestone-spec.md` | Epic specs, Epic Chat Starters, Milestone specs, Phase specs |
| `merge_strategy` | `governance/templates/epic-spec.md`, `governance/templates/epic-execution-chat-starter.md`, `governance/templates/milestone-spec.md` | PR descriptions, merge instructions in chat starters, epic specs |
| `branch_strategy` | `governance/templates/epic-execution-chat-starter.md`, `governance/templates/milestone-spec.md`, `governance/templates/phase-spec.md` | Chat starters (execution instructions), milestone specs, phase specs |

---

## Template Integration

When generating artifacts from templates, the HQ agent should:

1. **Identify override placeholders:** Template fields that accept override values should be clearly marked. Convention: `<%= overrides.field_name %>` in template comments, resolved to the cached value during generation.

2. **Apply defaults:** If an override field is not set, the governance default applies. Defaults are defined in `governance/ai-project-yml-spec.md` §3.3.

3. **Resolve at generation time:** Overrides are resolved when the artifact is generated, not when it is read. This ensures artifacts contain concrete values, not deferred references.

Example template integration for epic branch naming:

```
Template placeholder:  `Branch: <%= overrides.epic_prefix %>E<id>`
With override:         `Branch: feature/E9.2`
Without override:      `Branch: epic/E9.2`
```

---

## Precedence Hierarchy (Reference)

Override resolution follows a three-level hierarchy. The HQ agent checks each level in order and uses the first value found:

| Level | Source | Authority |
|-------|--------|-----------|
| 1 (highest) | Local project convention | `docs/decisions/` |
| 2 (medium) | `.ai-project.yml` overrides | `overrides` block |
| 3 (lowest) | Governance defaults | `PROJECT-SYSTEM-GUIDELINES.md` |

For full precedence documentation, see `governance/PROJECT-SYSTEM-GUIDELINES.md` §14C.

---

## Cross-References

- **Override boundaries:** `governance/override-boundaries.md`
- **Override field definitions:** `governance/ai-project-yml-spec.md` §3.3
- **Override validation rules:** `governance/ai-project-yml-spec.md` §4
- **Precedence hierarchy:** `governance/PROJECT-SYSTEM-GUIDELINES.md` §14C
- **HQ agent implementation:** `governance/agents/hq.agent.md` (Override Integration)
- **Project configuration schema:** `governance/ai-project-yml-spec.md`
