---
project: ai-project-system
phase: P2
milestone: M6
type: milestone
status: planned
last_updated: 2026-02-23
---

# Milestone M6 — Governance Separation & External Reference Model

## Purpose

Separate governance from project documentation and enable external projects to reference governance via git submodule.

## Problem Statement

Currently, governance files (PROJECT-SYSTEM-GUIDELINES.md, AI-OPERATING-GUIDELINES.md, templates) live in `docs/` alongside project history. External projects must copy these files, and updates don't propagate.

Milestone M6 establishes the infrastructure for governance to be external, versionable, and syncable.

## Goals

By the end of Milestone M6:

- Governance files moved to `/governance` folder in source repository
- `.ai-project.yml` specification created and documented
- Git submodule pattern defined and tested
- Source repository restructured
- Migration guide available for existing projects

## Non-Goals

Milestone M6 explicitly does **not** aim to:

- Implement project initialization automation (M7)
- Create hierarchical documentation structure (M7)
- Build override system (M8)
- Validate multi-project adoption (M9)

## Planned Epics

Epics will be defined incrementally as M6 execution begins.

Expected Epics:
- Create `/governance` folder structure
- Move governance files to `/governance`
- Create `.ai-project.yml` specification
- Document git submodule setup
- Test governance reference in external project

## Completion Criteria

Milestone M6 is considered complete when:

- All planned Epics are completed and accepted
- Governance files live in `/governance` folder
- `.ai-project.yml` specification exists
- Git submodule setup documented and tested
- External project can reference governance via submodule
- Migration guide available

## Notes

Milestone M6 is the first milestone under Phase P2. It establishes foundational architecture that M7-M9 will build upon.

This milestone introduces **breaking changes** to repository structure. Existing projects will need migration.

---

**M6 is planned. Epics will be created as execution begins.**
