# Override Boundaries

**Governance Reference:** PROJECT-SYSTEM-GUIDELINES.md §14C  
**First Defined In:** Epic E9.1 (P2-M9)  
**Last Updated:** 2026-05-21  
**Status:** Active

---

## Purpose

This document defines the formal boundaries of the AI Project System override system: which governance dimensions may be customized via `.ai-project.yml` overrides and which are core and immutable. It is the authoritative reference for understanding what can and cannot be changed without a governance amendment.

---

## Overridable Dimensions

The following governance dimensions may be customized via the `overrides` block in `.ai-project.yml`. Each dimension has a defined type, default, allowed values, and behavioral scope.

| Dimension | Override Field | Default | Allowed Values | What It Controls |
|-----------|---------------|---------|----------------|-----------------|
| Branch prefix | `epic_prefix` | `epic/` | Any non-empty string ending with `/` | The prefix used for epic branch names. Affects all generated branch references in artifacts (specs, chat starters). |
| Merge strategy | `merge_strategy` | `merge` | `merge`, `squash`, `rebase` | The default PR merge method referenced in generated merge instructions and PR descriptions. |
| Branch strategy | `branch_strategy` | `trunk-based` | `trunk-based`, `gitflow` | The branch naming and promotion strategy. Controls whether the standard hierarchy applies or an additional `develop` branch is expected. |

### Overridable Dimension Details

#### `epic_prefix`

| Property | Value |
|----------|-------|
| Field | `overrides.epic_prefix` |
| Default | `epic/` |
| Allowed | Any non-empty string ending with `/` |
| Constraint | Must end with `/`; must not be empty |

**What it controls:** The HQ agent uses this prefix when generating epic branch names (`<prefix>E<id>`) and referencing epic branches in generated artifacts (Milestone specs, Epic specs, Chat Starters).

**How it affects system behavior:** All generated branch references in specs, templates, and execution instructions use the custom prefix. The branch hierarchy structure (`epic/*` → `milestone/*` → `phase/*`) remains unchanged — only the prefix is customized.

**Examples:** `feature/E9.2`, `topic/E9.2`, `story/E9.2`

**Validation:** Must end with `/`. Unknown prefixes produce a warning.

**Rationale for overridability:** Organizations have established naming conventions for work items (features, stories, topics). Requiring `epic/` would force teams to adopt an unnatural prefix. The prefix is a cosmetic convention that does not affect governance logic or execution discipline.

---

#### `merge_strategy`

| Property | Value |
|----------|-------|
| Field | `overrides.merge_strategy` |
| Default | `merge` |
| Allowed | `merge`, `squash`, `rebase` |
| Constraint | Must be one of the allowed values |

**What it controls:** The merge method referenced in generated PR descriptions and merge instructions within Chat Starters and Epic specs.

**How it affects system behavior:** The HQ agent references this value when generating PR descriptions (e.g., "Merge using squash"). Individual PRs may override at merge time. The value is advisory for the merge executor, not an enforced rule.

**Examples:** `merge` (standard merge commit), `squash` (squash all commits), `rebase` (rebase onto target, fast-forward)

**Validation:** Must be one of `merge`, `squash`, or `rebase`. Case-sensitive.

**Rationale for overridability:** Team workflows vary. Some teams prefer clean linear histories (squash/rebase), others preserve full commit history (merge). The merge method is an operational convention, not a governance principle.

---

#### `branch_strategy`

| Property | Value |
|----------|-------|
| Field | `overrides.branch_strategy` |
| Default | `trunk-based` |
| Allowed | `trunk-based`, `gitflow` |
| Constraint | Must be one of the allowed values |

**What it controls:** The branch naming and promotion strategy. `trunk-based` uses the standard `epic/*` → `milestone/*` → `phase/*` → `develop` hierarchy. `gitflow` adds an expectation of a long-lived `develop` branch between `phase/*` and `main`.

**How it affects system behavior:** The HQ agent references the branch strategy when generating Chat Starters and execution instructions. In `gitflow` mode, milestone branches promote to `develop` before merging to `main`.

**Examples:** `trunk-based`, `gitflow`

**Validation:** Must be one of `trunk-based` or `gitflow`. Case-sensitive.

**Rationale for overridability:** Gitflow is a well-established alternative branching model. Teams that already use Gitflow should not be forced to adopt trunk-based development. The structural hierarchy (epic → milestone → phase) is preserved in both strategies.

---

## Core (Non-Overridable) Dimensions

The following governance dimensions are **immutable** and cannot be altered by any override mechanism. Attempting to override these dimensions (via `.ai-project.yml`, local decisions, or any other mechanism) is invalid.

| Dimension | What It Controls | Why Non-Overridable | Consequence of Allowing Override |
|-----------|-----------------|---------------------|----------------------------------|
| Canonical happy path (8 steps) | The required closure sequence: execution → delivery notice → human review → epic review seal → HQ decision → HQ authorization → PR & merge → stop | Foundational execution contract. Every Epic must follow it. | Epics would skip review or merge without authorization, breaking audit trail and authority hierarchy. |
| Authority hierarchy | Decision ownership: HQ Chat → Milestone Chat → Coding Agent | Establishes clear decision boundaries. | Unclear ownership of decisions, conflicting instructions, loss of accountability. |
| Epic lifecycle stages | Required sequence: spec → execute → deliver → review → accept → merge | Guarantees every Epic has a spec before execution, delivery before review, acceptance before merge. | Epics executed without specs, merged without review, or accepted without authorization. |
| Definition of DoD requirements | Minimum bar for completion | DoD is the quality floor. Reducing scope undermines quality. | Epics declare completion without meeting all requirements. |
| Documentation front-matter conventions | YAML front-matter for execution-context derivation | System requires mechanical extraction of context. Changing format breaks tooling. | Tooling (HQ agent, CLI) cannot parse artifacts; context not derivable. |
| Branch hierarchy structure | `epic/*` → `milestone/*` → `phase/*` | Enforces promotion discipline. Traceability depends on structure. | Branches merge in any order, skipping levels, breaking audit trail. (Prefixes are overridable; structure is not.) |

---

## Boundary Rules

1. **Project-wide scope:** Overrides apply project-wide, not per-epic or per-milestone. All Epics within a project use the same override values.
2. **Lifecycle immutability:** Overrides cannot alter the number or order of governance lifecycle steps (happy path, Epic lifecycle).
3. **DoD integrity:** Overrides cannot relax Definition of DoD requirements.
4. **Advisory to agents:** Overrides are advisory to governance agents. Agents must still validate generated artifacts against governance rules and may produce warnings if overrides create inconsistencies.
5. **Unknown keys:** Unknown override keys produce a warning, not a hard error. This supports forward compatibility.

---

## How to Propose a New Override

To add a new overridable dimension to the governance system:

1. **Determine fit:** The proposed dimension must be a cosmetic or operational convention, not a governance principle. Core dimensions (above) are never eligible.
2. **Create a decision record:** Document the proposal in `docs/decisions/` with rationale, expected behavior, and validation rules.
3. **Update this document:** Add the new dimension to the overridable dimensions table.
4. **Update field specs:** Add the new field to `governance/ai-project-yml-spec.md` §3.3 and validation rules in §4.
5. **Update PROJECT-SYSTEM-GUIDELINES.md:** Add the new field to §14C.
6. **Implement in HQ agent:** Add override reading and application logic (E9.3 pattern).
7. **Commit and version:** The change constitutes a governance evolution and must be versioned.

---

## Cross-References

- **Override system specification:** `governance/PROJECT-SYSTEM-GUIDELINES.md` §14C
- **Override field definitions:** `governance/ai-project-yml-spec.md` §3.3
- **Override validation rules:** `governance/ai-project-yml-spec.md` §4
- **Override system integration:** `docs/systems/override-system-integration.md`
