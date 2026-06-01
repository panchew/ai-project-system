# MILESTONE EXECUTION CHAT STARTER — P4-M17: Bug Fixes & Polish

MANDATORY CONTEXT PACKET

Project: ai-project-system
Phase: P4 — Team Collaboration and Artifact-Driven Communication
Milestone: M17 — Bug Fixes & Polish
Status: Planning Milestone
Governance: PROJECT-SYSTEM-GUIDELINES.md and AI-OPERATING-GUIDELINES.md enforced
Execution Mode: Milestone planning (produces Epic Execution Chat Starters)
Scope Rule: Create 2 Epic Execution Chat Starters for E17.1, E17.2 only.

MILESTONE OVERVIEW

**Goal:** Fix known issues with daemon orchestrator path resolution, update starters to reference artifact system, polish documentation, and prepare for team adoption.

**Deliverables:**
- Daemon orchestrator path resolution fix
- Updated HQ Chat Starter with artifact system references
- Updated Milestone Chat Starter with bugfix handling
- CFO Dashboard view (aggregated progress from multiple projects)
- Polish on all P4 governance documents

**Dependencies:**
- M14 (Artifact System) must be complete
- M15 (Bugfix Workflow) must be complete
- M16 (Team Example & Documentation) must be complete

**Duration:** 2-3 days

EPIC STUBS (2 EPICS)

### E17.1 – Fix Daemon Orchestrator Path Resolution

**Status:** Spec Complete (ready to execute)

**Description:** Fix known issue where v2.0.0 submodules don't have orchestrator binary, blocking fresh project init.

**Key Requirements:**
- Issue: When users clone ai-project-system with v2.0.0 daemon submodule, orchestrator binary is not found
- Investigation: Determine root cause (missing binary, wrong path, permission issue)
- Solution Option 1: Make daemon search in `governance/bin/` as fallback
- Solution Option 2: Update submodule version to v3.0.0+ (includes orchestrator)
- Solution Option 3: Build orchestrator on-demand during setup
- Test: Fresh project init on clean machine must work
- Verify: Daemon can find and execute orchestrator for Epic spawning

**Deliverables:**
- Daemon fix (code change or submodule update)
- Setup documentation update
- Test verification (fresh project init)
- Changelog entry documenting fix

**Spec:** `P4-M17-E17.1__spec__Fix_Daemon_Orchestrator_Path_Resolution.md`

---

### E17.2 – Update Starters & Documentation

**Status:** Spec Complete (ready to execute)

**Description:** Update HQ Chat Starter, Milestone Starter, and all governance documents to reference artifact system, production gate, and team collaboration patterns.

**Key Requirements:**

**HQ Chat Starter Updates:**
- Add section: "Artifact System (P4.1)" — how artifacts flow through HQ Chat
- Add section: "Bugfix Epic Workflow (P4.2)" — handling urgent production issues
- Add section: "Production Deployment Gate" — CFO authorization requirement
- Add section: "Team Roles & Decision Matrix" — link to P4.3 documentation
- Add examples: sample Completion Notices, Review Decisions, Deployment Authorizations
- Reference: example project (M16)

**Milestone Chat Starter Updates:**
- Add section: "Completion Notices" — how to receive and review
- Add section: "Rework Cycle" — handling rejections and retries
- Add section: "Escalation Path" — when to escalate to Phase/HQ
- Add examples: review decision process
- Reference: artifact protocol

**Documentation Polish:**
- Ensure all P4 documents are cross-linked
- Add index: "P4 Governance System Guide" (entry point for all P4 docs)
- Add troubleshooting guide: common issues and resolutions
- Add FAQ: "How do I...?" style guidance
- Update main README to highlight P4 features

**CFO Dashboard (Optional Advanced Feature):**
- Create view aggregating progress from multiple projects
- Show open Epics, Completion Notices awaiting review, SLA status
- Show production deployment requests pending CFO authorization
- Show post-mortem reports for recent bugfixes
- Can be simple (text-based) or advanced (web-based)

**Deliverables:**
- Updated `governance/HQ-EXECUTION-CHAT-STARTER.md`
- Updated `governance/systems/milestone-execution-chat-starter.md`
- New `docs/team-collaboration/P4-governance-system-guide.md` (index)
- New `docs/team-collaboration/troubleshooting-guide.md`
- New `docs/team-collaboration/faq.md`
- Updated main README with P4 highlights
- (Optional) CFO Dashboard prototype

**Spec:** `P4-M17-E17.2__spec__Update_Starters_and_Documentation.md`

**Depends On:** M14, M15, M16 (need to reference completed work)

---

## ACCEPTANCE CRITERIA (MILESTONE LEVEL)

✅ **Daemon orchestrator issue is fixed:**
- Fresh project init works (no missing binary errors)
- Daemon can spawn orchestrator for Epic execution
- Tested on clean checkout

✅ **HQ Chat Starter is updated:**
- References artifact system and P4 features
- Includes decision matrices and escalation paths
- Examples of artifacts are clear
- Team member can use it without confusion

✅ **Milestone Chat Starter is updated:**
- Explains Completion Notice handling
- Shows Review Decision process
- Clear escalation path to Phase/HQ

✅ **Documentation is complete and polished:**
- All P4 docs are cross-linked
- Index document helps navigate the system
- FAQ answers common "how do I...?" questions
- Troubleshooting guide helps with known issues

✅ **Team is ready for adoption:**
- CFO can use example project (M16) to understand workflow
- HQ Chat Starter guides agent implementation
- Documentation is clear enough for onboarding new teams
- Dashboard shows project progress at a glance

---

## KEY DECISIONS

1. **Path resolution fix urgency:** This is marked as HIGH risk in phase spec. Fix early in M17 to unblock all team adoption.

2. **Simple documentation > complex dashboards:** Focus on clarity and completeness of written guides. Dashboard can be added later.

3. **Backwards compatibility:** All updates to Starters must not break existing projects. Additions only, no removals.

4. **Cross-linking:** Every document links to related docs. Team member can navigate easily.

---

## INTEGRATION WITH M14, M15, M16

M17 pulls together all M14-M16 work:
- M14 artifacts are referenced in updated starters
- M15 bugfix handling is documented in HQ Starter
- M16 example project is referenced as onboarding tool
- All documentation is polished and production-ready

---

## SUCCESS CRITERIA (FROM CFO PERSPECTIVE)

- Daemon path issue is fixed (no more "orchestrator not found" errors)
- Updated HQ Starter is clear and actionable
- CFO Dashboard (if included) gives quick overview of project status
- Team member can onboard using documentation in <1 hour
- All P4 features are documented and accessible

---

## DEPENDENCIES & BLOCKERS

- ✅ M14 (Artifact System) must be complete
- ✅ M15 (Bugfix Workflow) must be complete
- ✅ M16 (Team Example) must be complete
- ✅ Daemon orchestrator issue is known (identified in P4 scope)

---

## NEXT STEPS

1. **Accept Milestone M17** — CFO approves bug fixes and polish scope
2. **Execute E17.1** — Fix daemon orchestrator path issue
3. **Execute E17.2** — Update starters and documentation
4. **Full integration test** — Run M14 → M15 → M16 workflow end-to-end
5. **Team adoption** — Begin onboarding first external team using P4 framework

---

## REFERENCE

- **Phase Spec:** `docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4__phase-spec.md`
- **M14 Milestone Starter:** `docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4-M14__milestone-execution-chat-starter.md`
- **M15 Milestone Starter:** `docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4-M15__milestone-execution-chat-starter.md`
- **M16 Milestone Starter:** `docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4-M16__milestone-execution-chat-starter.md`
- **Project System Guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md`
- **AI Operating Guidelines:** `governance/AI-OPERATING-GUIDELINES.md`
