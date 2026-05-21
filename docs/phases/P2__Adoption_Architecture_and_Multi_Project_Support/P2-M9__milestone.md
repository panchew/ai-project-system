---
project: ai-project-system
phase: P2
milestone: M9
type: milestone
status: active
last_updated: 2026-05-21
---

# Milestone M9 — Configuration & Override System

## Purpose

Allow projects to customize governance behavior without forking the governance source. The `.ai-project.yml` override specification enables projects to adapt conventions (branching, naming, merge strategy) to their local needs while keeping governance synchronised from the upstream source.

This milestone ensures:
- Override fields in `.ai-project.yml` are fully specified and validated
- Override precedence rules are documented and unambiguous
- Override boundaries are clearly defined (what can vs. cannot be overridden)
- The HQ agent reads and applies overrides during planning
- Example configurations exist for common project types

---

## Problem Statement

Phase P2 established a clean governance separation (M6), CLI initialization (M7), and an HQ Chat agent (M8). However, governance is currently one-size-fits-all:

- Projects must use the exact same branching conventions (`epic/*`, `milestone/*`, `phase/*`)
- Merge strategy is fixed (no choice between merge, squash, or rebase)
- Epic prefix is hardcoded
- No way to adapt conventions without forking the entire governance source
- The `.ai-project.yml` schema declares an `overrides` block (from E6.3) but it is a stub with no formal specification

Projects that need to deviate even slightly from defaults are forced to either:
- Fork governance (losing sync capability)
- Ignore governance rules (undermining the system)

Without M9, the system cannot accommodate real-world project diversity.

---

## Goals

By the end of Milestone M9:

1. The `.ai-project.yml` override specification is complete — all override fields defined with types, defaults, and constraints
2. Override precedence rules are documented in governance (config < governance < local)
3. Override boundaries are defined — what is overridable vs. what is core and immutable
4. The HQ agent reads `.ai-project.yml` and applies overrides during planning
5. Example configurations exist for at least 3 common project types
6. Override validation rules are documented

---

## Non-Goals

Milestone M9 explicitly does **not** aim to:

- Build CLI support for overrides (`ai-project init` override flags deferred — M7 already delivered without them)
- Implement runtime override enforcement in Coding Agents
- Create a governance diff/merge tool
- Support per-epic or per-milestone overrides (project-level only)
- Build a UI for override configuration

---

## In Scope

- Complete `.ai-project.yml` override specification (types, defaults, constraints)
- Override precedence hierarchy documentation
- Override boundaries specification (core vs. overridable)
- HQ agent override reading and application logic
- Example configurations for common project patterns
- Integration with existing `.ai-project.yml` validation

---

## Out of Scope

- CLI override flags (not needed — `.ai-project.yml` is the canonical source)
- Coding Agent override enforcement (deferred to P3)
- Per-epic or per-milestone overrides
- Governance diff tooling

---

## Planned Epics

### **E9.1 — Define Override Specification & Precedence Rules**
Define the complete set of override fields for `.ai-project.yml`, their types, defaults, constraints, and validation rules. Document the override precedence hierarchy (governance defaults → project overrides → local overrides). Update the `.ai-project.yml` spec document.

### **E9.2 — Document Override Boundaries and System Integration**
Define which governance dimensions are overridable (branch naming, merge strategy, epic prefix) and which are core/immutable (canonical happy path, authority hierarchy, DoD requirements, closure rules). Document how overrides flow through the system — how the HQ agent, templates, and specs should reference overridden values.

### **E9.3 — Implement HQ Agent Override Support**
Update `hq.agent.md` to read `.ai-project.yml` overrides and apply them during planning artifact generation. Ensure override values flow into generated Phase specs, Milestone specs, Epic specs, and Chat Starters. Add override validation logic to the agent startup sequence.

### **E9.4 — Create Example Configurations & Validate**
Create 3+ example `.ai-project.yml` configurations for common project types (library, application, mono-repo workspace). Validate each against the override spec. Test that the HQ agent correctly reads and applies each configuration. Document troubleshooting guidance.

---

## Definition of Done

- [ ] E9.1 Epic spec and Execution Chat Starter complete and accepted
- [ ] E9.2 Epic spec and Execution Chat Starter complete and accepted
- [ ] E9.3 Epic spec and Execution Chat Starter complete and accepted
- [ ] E9.4 Epic spec and Execution Chat Starter complete and accepted
- [ ] All 4 Epics executed and merged to `milestone/M9`
- [ ] `.ai-project.yml` override specification published in governance
- [ ] Override precedence hierarchy documented in PROJECT-SYSTEM-GUIDELINES.md
- [ ] Override boundaries documented
- [ ] HQ agent applies overrides during planning
- [ ] Completion notice and phase delivery authorization produced

---

## Acceptance Criteria

- A project can set `overrides.epic_prefix: "feature/"` and the HQ agent generates branches as `feature/E9.1` instead of `epic/E9.1`
- Override precedence is documented and unambiguous — a human reader can determine which value wins in any conflict
- Core governance (happy path, authority hierarchy, DoD) is explicitly marked as non-overridable
- Example configurations exist for at least 3 project types and are validated
- The `.ai-project.yml` spec passes validation for all known override combinations

---

## Milestone Exit Criteria

Milestone M9 is complete when:

1. All 4 Epics (E9.1–E9.4) are complete and accepted
2. `.ai-project.yml` override specification is complete and published
3. Override precedence rules are documented in governance
4. Override boundaries are defined
5. HQ agent reads and applies overrides during planning
6. Example configurations exist and are validated
7. M9 completion artifacts are produced (completion report, phase delivery authorization)

---

## Dependencies

- ✅ M6 complete — `.ai-project.yml` spec exists with overrides stub
- ✅ M7 complete — CLI init produces valid `.ai-project.yml`
- ✅ M8 complete — HQ agent is operational and can be extended
- ✅ Governance v2.0.0 active

---

## Execution Notes

**Override fields to define (initial set):**
- `overrides.branch_strategy` — default: `trunk-based` (future: `git-flow`)
- `overrides.merge_strategy` — default: `merge` (alternatives: `squash`, `rebase`)
- `overrides.epic_prefix` — default: `epic/`

**Precedence (highest to lowest):**
1. Local project convention (documented in project decisions)
2. `.ai-project.yml` overrides
3. Governance defaults (PROJECT-SYSTEM-GUIDELINES.md)

**Core (non-overridable):**
- Canonical happy path (8 steps)
- Authority hierarchy
- Epic lifecycle (spec → execute → deliver → review → accept → merge)
- Definition of DoD requirements
- Documentation front-matter conventions
- Branch hierarchy (epic → milestone → phase), only prefixes are overridable

**Testing:**
- Create test projects with different override combinations
- Verify HQ agent generates correct branch names and paths
- Validate that spec output references overridden values

**Success Signal:**
- A project lead can change `epic_prefix` to `feature/` in `.ai-project.yml` and the HQ agent immediately generates specs and starters using the custom prefix — without forking governance.
