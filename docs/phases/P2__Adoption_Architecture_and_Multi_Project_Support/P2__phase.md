---
project: ai-project-system
phase: P2
milestone: null
epic: null
type: phase
status: completed
last_updated: 2026-05-21
---

# Phase P2 — Adoption Architecture & Multi-Project Support

## Purpose

**Enable the AI Project System to be adopted, maintained, and evolved across multiple external projects — with a CLI-backed, agent-driven experience from day one.**

Phase P2 transforms the system from a **single-project governance framework** (dogfooded in `panchew/ai-project-system`) into a **multi-project infrastructure** that supports:
- Governance isolated from project documentation and referenceable via git submodule
- Project-specific configuration and overrides via `.ai-project.yml`
- Canonical project initialization via a `ai-project init` CLI tool
- An HQ Chat agent (VS Code Copilot custom agent) that reads `.ai-project.yml` and instantiates itself as the project's control room
- Hierarchical documentation that scales

**Phase P1 proved the system works.** Phase P2 makes it adoptable and launchable in minutes.

### North Star User Story

> As a developer, I open GitHub Copilot Chat in VS Code and indicate that I want to start a project using the AI Project System governance method. This instantiates the current chat as an HQ Chat for that project — allowing me to start the project from scratch with full governance, hitting the ground running.

The `ai-project init` CLI tool scaffolds the project structure and installs governance agent files so the HQ Chat agent is ready the moment VS Code opens.

---

## Problem Statement

Phase P1 governance was designed for dogfooding within `panchew/ai-project-system`. Real-world adoption revealed critical architectural limitations:

### **Problem 1: Governance and Project Documentation Are Mixed**
- Governance (system rules) and project history (what happened) live in the same folder
- Unclear which files are "system infrastructure" vs. "project artifacts"
- No clean separation between authoritative governance and project-specific documentation

### **Problem 2: No Governance Sync Mechanism**
- External projects must copy governance files
- Governance updates don't propagate to existing projects
- Projects diverge and become incompatible over time
- No way to declare "this project uses governance v1.5.0"

### **Problem 3: No Canonical Project Initialization**
- No standardized way to spin up a new project
- Manual setup is error-prone and tedious
- No CLI tool to scaffold structure and install governance agent files
- High friction for adoption

### **Problem 4: No HQ Chat Agent**
- HQ Chat is a conceptual role, not a concrete VS Code agent
- Developers must manually configure chat behavior and context
- No automatic governance loading from `.ai-project.yml`
- No canonical "start a project" entry point

### **Problem 5: No Override Mechanism**
- One-size-fits-all governance doesn't work
- Projects need flexibility (branching strategy, naming conventions, merge strategy)
- No way to override conventions without forking governance
- Forces projects to abandon governance or ignore rules

### **Problem 6: Flat Documentation Doesn't Scale**
- Current structure: `docs/phases/P1-M1-E1.1__spec.md` (flat folder)
- Deep projects create file explosion in single directory
- Visual structure doesn't match logical hierarchy
- Navigation becomes difficult

**These problems block adoption beyond single-project dogfooding.**

---

## Goals

By the end of Phase P2, the system must:

1. **Separate governance from project documentation**
   - Governance lives in `/governance` folder in source repository
   - Projects reference governance via git submodule or external reference
   - Clear distinction between system rules and project artifacts

2. **Enable governance sync and versioning**
   - Projects declare governance source and version in `.ai-project.yml`
   - Governance updates propagate to adopting projects
   - Governance version pinning prevents breaking changes

3. **Provide canonical project initialization via CLI**
   - `ai-project init` CLI scaffolds project structure and installs governance agent files
   - Hierarchical documentation structure created automatically
   - `.ai-project.yml` written with correct governance reference
   - Project is ready to open HQ Chat immediately after init

4. **Deliver a governance-aware HQ Chat agent**
   - `hq.agent.md` shipped as part of the governance package
   - HQ agent reads `.ai-project.yml` on startup: governance source, version, overrides
   - HQ agent produces: Phase specs, Milestone specs, Epic specs, Chat Starters
   - Selecting the `hq` agent in VS Code Copilot Chat instantiates HQ mode
   - Canonical "start a project" prompt defined
   - HQ agent tool access: read + write doc files only (no terminal, no code execution)

5. **Support project-specific overrides**
   - Projects can override conventions (branching, naming, merge strategy) via `.ai-project.yml`
   - Override precedence clearly defined (governance → config → local)
   - Override boundaries documented (what can vs. cannot be overridden)
   - HQ agent reads and applies overrides

6. **Implement hierarchical documentation structure**
   - Phases contain milestones, milestones contain Epics (visual matches logical)
   - `docs/phases/P1/milestones/M1/epics/` folder hierarchy
   - Scales to deep projects without flat file explosion

7. **Validate multi-project adoption**
   - At least 2 projects using Phase P2 architecture
   - Governance sync tested across projects
   - Adoption process documented and validated

---

## Non-Goals

Phase P2 explicitly does **not** aim to:

- **Build Phase/Milestone chat agents** — HQ agent only; Phase and Milestone agents (with full handoff chains and terminal access) deferred to P3
- **Create web UI** — Not needed for core adoption architecture
- **Implement automated validation** — Governance linting, CI/CD deferred to future work
- **Support team collaboration** — Multi-user patterns deferred to future phase
- **Integrate with external tools** — Jira, Linear, Notion sync deferred
- **Build observability/metrics** — Project health dashboards deferred
- **Create public adoption program** — Community case studies deferred
- **Complete closure artifact model** — Phase/Milestone completion report templates and formal PR-merge-as-agent-responsibility deferred to P3

**Focus:** Make the system architecturally sound and launchable for multi-project adoption. The full agent hierarchy (Phase/Milestone/Epic agents with handoffs) is P3.

---

## In Scope

### **Governance Architecture**
- Move governance files to `/governance` folder in source repository
- Define git submodule pattern for external projects
- Create `.ai-project.yml` specification (governance source, version, overrides)
- Update source repository structure

### **CLI Initialization Tool**
- `ai-project init` command scaffolds project structure
- Installs `.github/agents/hq.agent.md` from governance source
- Writes `.ai-project.yml` referencing governance
- Creates hierarchical `docs/phases/milestones/epics/` structure

### **HQ Chat Agent**
- `hq.agent.md` shipped as part of governance package in `/governance/agents/`
- Reads `.ai-project.yml` for governance source, version, active overrides
- Produces Phase specs, Milestone specs, Epic specs, Chat Starters as doc files
- Canonical "start a project" prompt that initializes HQ Chat context
- Tool access: read files + create/write doc files only (no terminal)

### **Configuration & Overrides**
- `.ai-project.yml` format and specification
- Override precedence rules
- Override boundaries (what's overridable vs. core)
- Override validation

### **Adoption Validation**
- Migrate `ai-project-system` to Phase P2 architecture
- Adopt Phase P2 architecture in at least one external project
- Test governance sync and updates
- Document adoption process

### **Documentation Updates**
- PROJECT-SYSTEM-GUIDELINES.md v2.0.0 (breaking changes)
- AI-OPERATING-GUIDELINES.md updates for HQ agent behavior and overrides
- Migration guide (Phase P1 → Phase P2 structure)
- Adoption guide for new projects

---

## Out of Scope

### **Deferred to P3 — Execution Model Maturity**
- ~~Separate agent files per level~~ (resolved: replaced by unified `governance.agent.md` with 4 modes)
- Full handoff chain (HQ → Phase → Milestone → Epic modes)
- Phase/Milestone completion report templates
- PR merge formalized as agent responsibility at Phase and Milestone level
- Parent-gating rules (phase chat only opens after HQ produces starter)

### **Deferred to Future Phases**
- Automated validation (governance health checks, lint rules)
- Team collaboration (multi-user, concurrent Epics)
- External integrations (project trackers, CI/CD)
- Observability (metrics, dashboards)
- Community infrastructure (public case studies, forums)

### **Explicitly Not Included**
- Non-git version control systems (SVN, Mercurial)
- Non-GitHub hosting (GitLab, Bitbucket) — may work but not validated
- Windows-specific tooling — Unix/Mac focus
- Monorepo support — single-repo projects only

---

## Execution Bootstrap Note

> **Phase P2 is self-referential.** The Phase Execution Chat Starter and Milestone Execution Chat Starter are deliverables of this Phase (M6 — E6.6 and E6.7). They cannot be used to launch Phase P2 itself because they don't exist yet.

**Governance exception for Phase P2:** Milestone M6 is executed under the prior-art model — HQ Chat produces Epic Execution Chat Starters directly, bypassing the Phase Chat and Milestone Chat layers. This is not a workaround; it is the correct and only coherent behavior when the tools being built are not yet available.

**Starting with M7:** The full four-level hierarchy (HQ → Phase Chat → Milestone Chat → Coding Agent) is available and MUST be used for all milestones from M7 onward.

This bootstrap exception is a documented precedent: any Phase that delivers new chat-layer infrastructure is permitted to execute under the previous layer's model for the milestone(s) that create that infrastructure.

---

## Planned Milestones

### **M6 — Governance Separation & `.ai-project.yml`**
**Purpose:** Separate governance from project documentation and define the project configuration contract.

**Key deliverables:**
- Governance files moved to `/governance` folder
- `.ai-project.yml` specification (governance source, version, overrides)
- Git submodule setup instructions
- Migration guide (P1 → P2 structure)
- Source repository restructured

**Exit criteria:** External project can reference governance via git submodule; `.ai-project.yml` spec is complete

---

### **M7 — CLI Initialization Tool**
**Purpose:** Enable one-command project initialization with governance and agent files ready.

**Key deliverables:**
- `ai-project init` CLI command (shell script or Node.js)
- Scaffolds hierarchical `docs/` structure
- Installs `.github/agents/hq.agent.md` from governance source
- Writes `.ai-project.yml` referencing governance
- Tested end-to-end on a new project

**Exit criteria:** `ai-project init my-project` produces a repo where HQ Chat agent is immediately usable

---

### **M8 — HQ Chat Agent**
**Purpose:** Deliver the governance-aware HQ Chat agent that fulfills the north star user story.

**Key deliverables:**
- `hq.agent.md` in `/governance/agents/`
- Agent reads `.ai-project.yml` on startup (governance source, version, overrides)
- Agent produces Phase specs, Milestone specs, Epic specs, Chat Starters as doc files
- Canonical "start a project" prompt documented
- Tool access scoped: read + write doc files only (no terminal)
- Shipped to projects via `ai-project init`

**Exit criteria:** Developer opens VS Code, selects `hq` agent, sends canonical prompt, and HQ Chat is live with correct governance context

---

### **M9 — Configuration & Override System**
**Purpose:** Allow projects to customize governance behavior without forking it.

**Key deliverables:**
- Complete `.ai-project.yml` override specification
- Override precedence rules documented in governance
- Override boundaries defined (what's overridable vs. core)
- HQ agent reads and applies overrides
- Example configurations for common project types

**Exit criteria:** Project can override branching/naming conventions; HQ agent respects overrides during planning

---

### **M10 — Adoption Validation & Documentation**
**Purpose:** Validate multi-project governance works in practice; document the full adoption path.

**Key deliverables:**
- At least 2 projects using Phase P2 architecture
- Adoption guide (step-by-step from zero to HQ Chat live)
- Troubleshooting FAQ
- Governance sync validation across projects
- Phase P2 completion report

**Exit criteria:** External project successfully adopts P2 architecture, runs `ai-project init`, opens HQ Chat, and syncs governance updates

---

## Exit Criteria

Phase P2 is complete when:

1. **Governance is externalized**
   - ✅ Governance lives in `/governance` folder in source repository
   - ✅ Projects reference governance via git submodule
   - ✅ `.ai-project.yml` specification exists and is documented

2. **CLI initialization works**
   - ✅ `ai-project init` scaffolds project structure and installs agent files
   - ✅ Hierarchical documentation structure created automatically
   - ✅ `.ai-project.yml` written with correct governance reference

3. **HQ Chat agent is operational**
   - ✅ `hq.agent.md` shipped in governance package
   - ✅ HQ agent reads `.ai-project.yml` and applies governance context
   - ✅ Canonical "start a project" prompt produces Phase spec
   - ✅ North star user story achievable end-to-end

4. **Overrides work**
   - ✅ Projects can override conventions via `.ai-project.yml`
   - ✅ HQ agent respects overrides during planning
   - ✅ Override boundaries are documented

5. **Multi-project adoption validated**
   - ✅ At least 2 projects use Phase P2 architecture
   - ✅ Governance sync tested across projects
   - ✅ Adoption process documented

6. **Governance updated**
   - ✅ PROJECT-SYSTEM-GUIDELINES.md v2.0.0 published
   - ✅ AI-OPERATING-GUIDELINES.md updated for HQ agent behavior and overrides
   - ✅ Migration guide available

7. **All milestones complete**
   - ✅ M6 — Governance Separation & `.ai-project.yml`
   - ✅ M7 — CLI Initialization Tool
   - ✅ M8 — HQ Chat Agent
   - ✅ M9 — Configuration & Override System
   - ✅ M10 — Adoption Validation & Documentation

---

## Success Metrics

**Phase P2 will be considered successful if:**

- External projects can adopt governance in **< 30 minutes** (from chat starter)
- Governance updates propagate to existing projects **without manual copying**
- Projects can override conventions **without forking governance**
- At least **2 real projects** (not examples) use Phase P2 architecture
- Adoption friction is **measurably lower** than Phase P1 dogfooding

---

## Risks & Mitigations

### **Risk 1: Git Submodules Are Confusing**
**Likelihood:** High  
**Impact:** Medium (adoption friction)

**Mitigation:**
- Provide clear setup instructions
- Include troubleshooting guide
- Consider reference-only fallback if submodules prove too difficult
- Test with non-git-expert users

---

### **Risk 2: Hierarchical Structure Breaks Existing Projects**
**Likelihood:** Medium  
**Impact:** High (breaking change)

**Mitigation:**
- Provide migration scripts/guides
- Version governance as v2.0.0 (signal breaking change)
- Support both flat and hierarchical during transition
- Test migration with `ai-project-system` itself first

---

### **Risk 3: Override System Is Too Complex**
**Likelihood:** Medium  
**Impact:** Medium (adoption confusion)

**Mitigation:**
- Start with minimal override set (branching, naming only)
- Expand overrides based on real needs, not speculation
- Document override boundaries clearly
- Provide override validation

---

### **Risk 4: Coding Agents Can't Read External Governance**
**Likelihood:** Low  
**Impact:** High (blocks adoption)

**Mitigation:**
- Test governance reference with multiple AI tools
- Validate network access patterns
- Fallback to git submodule if reference-only fails
- Document requirements clearly

---

## Dependencies

**External dependencies:**
- Git submodule functionality (standard git feature)
- Network access for governance reference (if used)
- YAML parsing (standard, widely supported)

**Internal dependencies:**
- Phase P1 complete ✅
- Phase P1 governance stable (v1.5.0 / v1.4.1) ✅
- Source repository (`panchew/ai-project-system`) in production ✅

**No blockers identified.**

---

## Timeline Estimate

**Phase P2 is expected to take 4-6 weeks:**

- M6: 1-2 weeks (governance separation, git submodule setup)
- M7: 1-2 weeks (project init, hierarchical structure)
- M8: 1 week (override system)
- M9: 1 week (adoption validation, documentation)

**Total:** 4-6 weeks depending on complexity and real-world testing needs.

**No deadline.** Phase P2 proceeds at pace driven by real usage needs.

---

## Notes

### **Why Phase P2 Is Critical**

Phase P1 proved the system works **for a single project**. Phase P2 makes it work **for many projects**.

Without Phase P2:
- Every project forks governance → divergence and incompatibility
- Governance updates don't propagate → projects become stale
- Setup is manual and error-prone → adoption friction too high
- No flexibility → projects abandon governance when it doesn't fit

**Phase P2 is the difference between "proof of concept" and "production-ready infrastructure."**

---

### **Breaking Changes Expected**

Phase P2 will introduce **breaking changes** to repository structure:
- Governance moves to `/governance` folder
- Documentation structure becomes hierarchical
- `.ai-project.yml` required for projects

**Governance version will increment to v2.0.0** to signal breaking changes.

Existing Phase P1 projects (including `ai-project-system` itself) will need migration.

---

### **Adoption Is Validation**

Phase P2 success depends on **real adoption**. At least 2 projects must use the architecture:
1. `panchew/ai-project-system` (dogfooding)
2. User's external project (real-world validation)

If additional external projects adopt during Phase P2, even better.

---

## Related Documents

- [Phase P1 Specification](../P1__System_Foundation_and_Adoption/P1__phase.md) — Foundation phase (complete)
- [PROJECT-SYSTEM-GUIDELINES.md](../../PROJECT-SYSTEM-GUIDELINES.md) v1.5.0 — Current governance
- [AI-OPERATING-GUIDELINES.md](../../AI-OPERATING-GUIDELINES.md) v1.4.1 — Current governance

---

## Approval

**Phase P2 spec approved by HQ:** 2026-02-23

**Status:** Active (execution authorized)  
**Created:** 2026-02-23  
**Last Updated:** 2026-02-23
