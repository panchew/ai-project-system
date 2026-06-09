# MILESTONE EXECUTION CHAT STARTER — P4-M16: Team Collaboration Example Project

MANDATORY CONTEXT PACKET

Project: ai-project-system
Phase: P4 — Team Collaboration and Artifact-Driven Communication
Milestone: M16 — Team Collaboration Example & Documentation
Status: Planning Milestone
Governance: PROJECT-SYSTEM-GUIDELINES.md and AI-OPERATING-GUIDELINES.md enforced
Execution Mode: Milestone planning (produces Epic Execution Chat Starters)
Scope Rule: Create 2 Epic Execution Chat Starters for E16.1, E16.2 only.

MILESTONE OVERVIEW

**Goal:** Create a real-world 3-person team collaboration example project and document governance roles, decision matrices, and onboarding procedures.

**Deliverables:**
- Example project with 3 concurrent Epics demonstrating team workflow
- Team Onboarding Guide (roles, authority matrix, escalation paths)
- CFO Quick Start guide (weekly decision patterns)
- Contributor Guide (how to execute an Epic)
- Role-based decision matrices with examples
- Walkthrough of one full Epic from planning to delivery

**Dependencies:**
- M14 (Artifact System) must be complete
- M15 (Bugfix Workflow) must be complete
- P4.3 Design (Roles & Authorization) is complete

**Duration:** 3-5 days

EPIC STUBS (2 EPICS)

### E16.1 – Example Project Setup & Walkthrough

**Status:** Spec Complete (ready to execute)

**Description:** Create a real-world 3-person team example project and document the full workflow.

**Key Requirements:**
- Create example project directory: `examples/team-project-example/`
- Project structure: Phase P1 with 3 Milestones (M14, M15, M16)
- Each Milestone has 2-3 Epics (6-9 Epics total)
- Assign team roles:
  - CFO (Layer-8) — strategic oversight
  - Phase Lead — milestone coordination
  - 2 Contributors — implementation
  - 1 Reviewer — code review
- Create actual artifact examples (Completion Notices, Review Decisions, Delivery Notices)
- Document the full flow: Planning → E14.1 Execution → Completion Notice → M14 Review → Review Decision → Merge → Delivery Notice
- Show decision points and who decides
- Example should be runnable (test/verify all artifacts)

**Deliverables:**
- `examples/team-project-example/` directory structure
- Phase P1 spec, Milestone M14-M16 specs, Epic E14.1-E3.3 specs
- Real artifact examples (stored in `.ai-project/artifacts/`)
- Walkthrough document: "One Full Epic from Start to Finish"
- README with team roles explained
- Role assignment table with decision authorities

**Spec:** `P4-M16-E16.1__spec__Example_Project_Setup_and_Walkthrough.md`

---

### E16.2 – Team Collaboration Documentation

**Status:** Spec Complete (ready to execute)

**Description:** Create comprehensive guides for each role to enable team adoption with minimal confusion.

**Key Requirements:**
- **Team Onboarding Guide:**
  - What are the roles? (CFO, Phase Lead, Contributor, Reviewer, etc.)
  - Authority matrix: who decides what?
  - Escalation flowchart: when and where to escalate
  - Communication norms (chat-first, artifact-driven)
  - Time commitment per role

- **CFO Quick Start:**
  - Your job: strategic oversight and production deployment gates
  - Typical week: 1-3 decisions per project
  - How to review Completion Notices
  - How to issue Review Decisions
  - How to authorize production deployment
  - Time commitment: 30 min - 2 hours/week

- **Contributor Guide:**
  - Your job: implement Epics according to spec
  - Epic workflow: receive Epic Spec → implement → create Completion Notice → await Review Decision → merge
  - Definition of Done: tests, documentation, code review
  - What to ask if blocked (escalation path)
  - Example PR workflow

- **Reviewer Guide:**
  - Your job: code review and Definition of Done validation
  - Checklist for reviews: tests, docs, spec compliance
  - How to provide feedback
  - How to block merge if needed
  - Integration with Review Decision

- **Phase Lead Guide:**
  - Your job: milestone coordination and escalation
  - How to plan milestones
  - How to prioritize Epics
  - When to escalate to CFO
  - Delegation and team communication

- **Decision Matrices:**
  - Phase Scope: who decides? (CFO)
  - Milestone Planning: who decides? (Phase Lead or HQ Agent)
  - Epic Acceptance: who decides? (Milestone Agent)
  - Production Deployment: who decides? (CFO)
  - Escalation: when and how?

- **Example Run-Through:**
  - Step-by-step walkthrough of example E16.1 project
  - Show all artifacts flowing between chats
  - Demonstrate manual mode (copy-paste)
  - Demonstrate agentic mode (daemon routing)

**Deliverables:**
- `docs/team-collaboration/team-onboarding-guide.md`
- `docs/team-collaboration/cfo-quick-start.md`
- `docs/team-collaboration/contributor-guide.md`
- `docs/team-collaboration/reviewer-guide.md`
- `docs/team-collaboration/phase-lead-guide.md`
- `docs/team-collaboration/decision-matrices.md`
- `docs/team-collaboration/example-walkthrough.md`
- All guides cross-linked and referenced in main README

**Spec:** `P4-M16-E16.2__spec__Team_Collaboration_Documentation.md`

**Depends On:** E16.1 (example project is needed for documentation examples)

---

## ACCEPTANCE CRITERIA (MILESTONE LEVEL)

✅ **Example project is realistic:**
- 3-person team (CFO, Phase Lead, Contributors)
- Real project structure (Phase → Milestones → Epics)
- All artifacts present (Completion Notices, Review Decisions, Delivery Notices)
- Demonstrates parallel Epic execution
- Workflows are realistic (not overly simplified)

✅ **Documentation is comprehensive:**
- New team member can read guides and understand their role
- Authority matrix is clear (no ambiguity about who decides what)
- Escalation path is documented
- Time commitment is realistic

✅ **Guides are CFO-friendly:**
- CFO Quick Start: <5 min read, explains what you need to do
- Decision matrices: <30 sec lookup for any decision
- Example workflow: shows one full Epic cycle

✅ **All artifacts flow correctly:**
- Example project can be executed in manual mode
- Daemon can route all artifacts in agentic mode
- Both modes produce same results

---

## KEY DECISIONS

1. **3-person team:** Small enough to be realistic, large enough to show team workflow.

2. **Real vs. minimal specs:** Example uses full specs (not minimal bugfix specs). This shows normal planning workflow.

3. **Both manual & agentic modes:** Documentation shows copy-paste (manual) and daemon routing (agentic). Teams can choose.

4. **Time commitment is clear:** Each role guide specifies expected time commitment (CFO: 1-2 hours/week, Contributors: varies, etc.)

5. **Escalation is emphasized:** Clear flowchart showing when to escalate and to whom.

---

## INTEGRATION WITH M14 & M15

M16 uses artifacts from M14 and M15:
- All Completion Notices, Review Decisions, Delivery Notices use M14 formats
- Example shows how Bugfix Epics (M15) integrate into normal workflow
- Example demonstrates both normal and expedited paths

---

## SUCCESS CRITERIA (FROM CFO PERSPECTIVE)

- CFO reads "CFO Quick Start" (5 minutes)
- CFO understands what decisions they need to make
- CFO can run example project and see full workflow
- CFO feels confident delegating roles to team members
- CFO knows when to escalate and when to decide

---

## DEPENDENCIES & BLOCKERS

- ✅ M14 (Artifact System) must be complete
- ✅ M15 (Bugfix Workflow) must be complete
- ✅ P4.3 Design (Roles & Authorization) is complete
- ✅ Example project structure can be created in examples/

---

## NEXT STEPS

1. **Accept Milestone M16** — CFO approves scope
2. **Execute E16.1** — Create example project with real artifacts
3. **Execute E16.2** — Write team collaboration guides
4. **Integrate example with daemon** — test agentic routing
5. **Begin M17** — bug fixes and final polish
6. **Prepare for team adoption** — example project becomes template for new teams

---

## REFERENCE

- **Phase Spec:** `docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4__phase-spec.md`
- **Roles & Authorization Design:** `governance/systems/roles-authorization-team-governance.md`
- **Artifact Protocol (M14):** `governance/systems/artifact-communication-protocol.md`
- **Bugfix Workflow (M15):** `governance/systems/bugfix-epic-workflow.md`
- **M14 Milestone Starter:** `docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4-M14__milestone-execution-chat-starter.md`
- **M15 Milestone Starter:** `docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/P4-M15__milestone-execution-chat-starter.md`
