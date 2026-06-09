---
project: ai-project-system
phase: P2
milestone: M6
type: milestone
status: completed
last_updated: 2026-04-18
---

# Milestone M6 — Governance Separation & `.ai-project.yml`

## Purpose

Separate governance from project documentation, establish the `/governance` folder as the authoritative home for all system rules and agent files, and define the `.ai-project.yml` project configuration contract.

This is the foundational milestone for Phase P2. All subsequent milestones (CLI tool, HQ agent, overrides, adoption) depend on the architecture established here.

## Problem Statement

Currently, governance files (`PROJECT-SYSTEM-GUIDELINES.md`, `AI-OPERATING-GUIDELINES.md`, `templates/`) live in `docs/` alongside project history. This creates two problems:

1. **Mixed concerns** — system rules and project artifacts are in the same folder. Unclear which files are "system infrastructure" vs. "what happened in this project."
2. **No sync mechanism** — external projects must copy governance files manually. Updates don't propagate. Projects diverge.

Milestone M6 establishes the infrastructure that solves both: a clean `/governance` folder in the source repo, and a `.ai-project.yml` file that lets adopting projects declare their governance source and version.

## Goals

By the end of Milestone M6:

- Governance files moved to `/governance` folder in source repository
- `/governance` folder structure defined and documented
- `.ai-project.yml` specification created — format, required fields, optional fields
- Git submodule pattern defined, documented, and tested
- Source repository (`ai-project-system`) restructured to new layout
- Migration guide available for existing P1 projects

## Non-Goals

Milestone M6 explicitly does **not** aim to:

- Implement the CLI initialization tool (M7)
- Create the HQ Chat agent file (M8)
- Build the override resolution system (M9)
- Validate multi-project adoption (M10)
- Create hierarchical documentation structure (M7)

## Planned Epics

### **E6.1 — Define `/governance` Folder Structure**
Design and document the canonical `/governance` folder layout: what goes in it, naming conventions, subdirectories (`agents/`, `templates/`, etc.), and the authority hierarchy within the folder.

### **E6.2 — Move Governance Files to `/governance`**
Execute the migration: move `PROJECT-SYSTEM-GUIDELINES.md`, `AI-OPERATING-GUIDELINES.md`, `docs/templates/`, and related system files to `/governance`. Update all internal references. Increment governance version to v2.0.0.

### **E6.3 — Define `.ai-project.yml` Specification**
Specify the `.ai-project.yml` format: required fields (`governance.source`, `governance.version`), optional override fields, and validation rules. Write the spec document and add a reference `.ai-project.yml` to this repository.

### **E6.4 — Document Git Submodule Setup**
Write the canonical instructions for external projects to reference governance via git submodule: add submodule, pin version, sync updates. Include in the migration guide and governance docs.

### **E6.5 — Migration Guide & Source Repo Validation**
Write the migration guide for existing P1 projects adopting P2 structure. Validate the source repo (`ai-project-system`) fully conforms to the new layout. Confirm all internal links and references are correct.

### **E6.6 — Phase Execution Chat Starter**
Define the role and responsibilities of a Phase Chat. Create the system doc and fillable template for the Phase Execution Chat Starter — the artifact a Phase Chat uses to launch a Milestone Chat.

### **E6.7 — Milestone Execution Chat Starter**
Define the role and responsibilities of a Milestone Chat. Create the system doc and fillable template for the Milestone Execution Chat Starter — the artifact a Milestone Chat uses to produce Epic Execution Chat Starters. Document the full four-level chat hierarchy end-to-end.

## Completion Criteria

Milestone M6 is considered complete when:

- All 7 Epics are completed and accepted
- `/governance` folder exists and contains all governance files
- `docs/` contains only project history artifacts (phases, context, roadmap, admin)
- `.ai-project.yml` specification document exists and is referenced from governance
- `ai-project-system` repository contains a valid `.ai-project.yml`
- Git submodule setup is documented and tested against the source repo
- Migration guide is written and covers P1 → P2 transition
- All internal documentation references are updated
- Phase Execution Chat Starter system doc and template exist in `/governance`
- Milestone Execution Chat Starter system doc and template exist in `/governance`
- Full four-level chat hierarchy (HQ → Phase → Milestone → Epic → Coding Agent) is documented

## Dependencies

- ✅ P1 fully closed (governance baseline stable)
- ✅ P2 phase spec updated with revised milestone plan
