---
project: ai-project-system
phase: P2
milestone: M7
type: milestone
status: completed
last_updated: 2026-05-02
---

# Milestone M7 — CLI Initialization Tool

## Purpose

Enable one-command project initialization with governance and agent files ready to use. The `ai-project init` CLI command scaffolds new projects with the correct folder structure, installs governance via git submodule, writes `.ai-project.yml`, and pre-installs HQ Chat agent files so developers can immediately begin planning with full governance context.

This milestone ensures:
- New projects can be initialized in minutes without manual copying
- Hierarchical documentation structure is correct from the start
- Governance reference is automatic and versioned
- HQ Chat agent is ready to use from day one

---

## Problem Statement

Phase P1 proved the AI Project System governance model works. However, onboarding new projects is manual and error-prone:
- Developers must manually copy governance files
- Folder structure can be misunderstood
- `.ai-project.yml` must be written by hand
- No canonical way to install agent files into a new project

Without a CLI tool, adoption friction remains high. Developers can't "just run a command and start."

---

## Goals

By the end of Milestone M7:

1. The `ai-project init` CLI command exists and is usable
2. Running `ai-project init my-project` scaffolds a complete P2-conformant project
3. The generated project has governance pinned via git submodule at the current version
4. `.ai-project.yml` is written correctly with governance reference
5. HQ Chat agent files are installed and ready
6. End-to-end initialization is tested on a new project
7. Developers can start planning immediately after running the CLI

---

## Non-Goals

Milestone M7 explicitly does **not** aim to:

- Build a full Node.js package with npm registry publication (that's M11+)
- Create override system support in the CLI (M9 delivers that)
- Integrate with external project trackers (M10)
- Build a GUI or web interface for initialization
- Implement automated governance sync (future phase)

---

## Planned Epics

### **E7.1 — Design CLI Architecture & Hierarchical Docs Structure**
Design the `ai-project init` command structure, command-line arguments, and folder hierarchy it should create. Define how the CLI determines project name, location, governance source, and other parameters. Document the expected output folder structure and validate it against PROJECT-SYSTEM-GUIDELINES.md conventions.

### **E7.2 — Implement `ai-project init` Command (Scaffolding)**
Implement the core CLI logic (as shell script or Node.js). The CLI must:
- Accept project name and optional governance source/version parameters
- Create the hierarchical `docs/` structure (phases/, context/, roadmap/, decisions/, admin/)
- Initialize a git repository
- Validate folder structure against conventions

### **E7.3 — Integrate Governance Submodule & `.ai-project.yml` Creation**
Extend the CLI to:
- Add governance as a git submodule at the specified version
- Create `.ai-project.yml` at repo root with correct governance reference
- Validate `.ai-project.yml` against the spec
- Test submodule initialization on a new project

### **E7.4 — Ship HQ Chat Agent Files & End-to-End Validation**
Extend the CLI to:
- Copy or symlink `hq.agent.md` from governance source to `.github/agents/` in the project
- Ensure agent file paths are correct and readable
- Perform end-to-end test: run CLI on a clean directory, verify all outputs, confirm HQ Chat agent is usable
- Document canonical "start a project" prompt for developers

---

## Definition of Done

- [x] E7.1 Epic spec and Execution Chat Starter complete and accepted
- [x] E7.2 Epic spec and Execution Chat Starter complete and accepted
- [x] E7.3 Epic spec and Execution Chat Starter complete and accepted
- [x] E7.4 Epic spec and Execution Chat Starter complete and accepted
- [x] All 4 Epics have been executed and merged to `milestone/M7`
- [x] CLI command is deployed to the repository (at least in `/bin/` or similar)
- [x] End-to-end test passed: `ai-project init test-project` produces a usable P2 project
- [x] Completion notice and phase delivery authorization produced

---

## Acceptance Criteria

- Running `ai-project init my-project` produces a directory tree with all required P2 folders
- The generated project contains a valid `.ai-project.yml` referencing the current governance version
- Governance is installed as a git submodule pinned to the specified version
- HQ Chat agent files are installed and accessible in `.github/agents/`
- A developer can open VS Code in the generated project and use the HQ Chat agent immediately
- The CLI is documented and includes a `--help` option
- The CLI has been tested on at least one new project from scratch

---

## Milestone Exit Criteria

Milestone M7 is complete when:

1. ✅ All 4 Epics (E7.1–E7.4) are complete and accepted
2. ✅ `ai-project init` CLI command is implemented and deployed
3. ✅ End-to-end test confirms: new project scaffold → HQ Chat agent ready → planning can begin
4. ✅ CLI is documented (help text, usage examples, troubleshooting)
5. ✅ Governance version is pinned and correctly referenced in generated projects
6. ✅ M7 completion artifacts are produced (completion report, phase delivery authorization)

> Milestone M7 is complete and production-ready for governance-driven planning with the HQ agent as of 2026-05-02.

---

## Dependencies

- ✅ M6 complete — governance externalized, `.ai-project.yml` spec defined, submodule pattern documented
- ✅ Governance v2.0.0 available at `panchew/ai-project-system` with tag `v2.0.0`
- ✅ `hq.agent.md` exists in `/governance/agents/` (stub file ok for E7 planning; full implementation in M8)

---

## Execution Notes

**CLI Implementation Approach:**
- Can be shell script (bash/sh) or Node.js
- Recommendation: shell script for minimal dependencies; Node.js if scripting becomes complex
- Must run on macOS, Linux, and Windows (WSL ok; native Windows support ideal)

**Governance Source Default:**
- Default: `https://github.com/panchew/ai-project-system`
- Default version: current latest tag (e.g., `v2.0.0`)
- Developers can override via `--governance-source` and `--governance-version` flags

**Testing:**
- Create a clean directory and run the CLI
- Verify all output files exist
- Verify `.ai-project.yml` is valid YAML and matches the spec
- Verify git submodule is initialized correctly
- Open the generated project in VS Code and confirm HQ Chat agent can be activated

**Success Signal:**
- After running the CLI and `cd`ing to the generated project, a developer can immediately select the HQ Chat agent and start planning without any manual setup
