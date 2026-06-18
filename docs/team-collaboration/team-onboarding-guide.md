# Team Onboarding Guide

**Welcome to the AI Project System.**

> 📍 Part of the **[P4 Governance System Guide](P4-governance-system-guide.md)** — the entry point to all team-collaboration docs.

This guide helps every new team member understand their role, how the team makes decisions, and how work flows from idea to merged code. Read your role section first, then skim the others for context.

---

## What Is the AI Project System?

The AI Project System is a governance framework for executing software projects with AI assistance. It replaces ad-hoc AI chat sessions with a structured hierarchy: every piece of work is planned in a spec, executed by an agent or developer, reviewed by a parent authority, and delivered through a PR.

**Core idea:** Documentation is authoritative. Chat is ephemeral.

All decisions, approvals, and handoffs are recorded as Markdown artifacts in the repository — not in chat logs. This means any team member can understand project state by reading the repo.

---

## How Work Flows

Work flows top-down through four levels:

```
CFO → HQ Agent → Phase Lead → Milestone Agent → Epic Agent → Contributors
```

Each level produces a spec (what to do) and a Chat Starter (how the next level begins). Work flows upward as Completion Notices, which trigger Review Decisions, which enable merges.

### The Three Canonical Artifacts

Every handoff between levels uses exactly one of three artifact types:

| Artifact | Direction | Purpose |
|---|---|---|
| **Completion Notice** | Child → Parent | "Work is done, please review." |
| **Review Decision** | Parent → Child | "Accepted (merge) or Rejected (rework)." |
| **Delivery Notice** | Child → Archive | "PR merged, chat closed." |

These are stored in `.ai-project/artifacts/` and committed to the repository. See [decision-matrices.md](decision-matrices.md) for who issues which artifact.

---

## Roles

### CFO — Chief Financial Officer (Layer-8)

**You are the single source of strategic authority.**

The CFO is typically the project owner or technical lead. Only one person holds this role.

**Decisions only CFO can make:**
- Authorize new Phases (scope, budget, timeline)
- Authorize all production deployments (no exceptions)
- Override any lower-level decision when justified

**CFO does NOT:**
- Merge PRs directly (delegates to the authorized role)
- Bypass Definition of Done or governance rules

**Time commitment:** 30 minutes to 2 hours per week

**How to participate:** Visit HQ Chat when prompted. Review high-level status reports. Issue Phase Authorizations and Deployment Authorizations as artifacts.

See [cfo-quick-start.md](cfo-quick-start.md) for a 5-minute orientation to your day-to-day.

---

### Phase Lead (Optional — Team Lead Role)

**You own Phase planning and milestone strategy.**

The Phase Lead is typically a senior developer or engineering lead. The role is optional; when absent, HQ Agent fulfills this function.

**Decisions Phase Lead can make:**
- Plan milestones within Phase scope
- Reorder milestones and prioritize Epics
- Escalate blockers to CFO

**Phase Lead does NOT:**
- Redefine Phase scope (CFO must approve)
- Cancel a Phase (CFO only)

**Time commitment:** 2–5 hours per week during active Milestones

See [phase-lead-guide.md](phase-lead-guide.md) for full workflow.

---

### Reviewer

**You are the technical quality gate.**

The Reviewer is typically a peer developer. They review PRs against the Epic spec, tests, and Definition of Done.

**Decisions Reviewer can make:**
- Block a merge if the code does not meet the Definition of Done
- Request rework (maps to Epic rejection)
- Approve the PR for the Milestone Agent to accept

**Reviewer does NOT:**
- Approve the final merge independently (Milestone Agent accepts)
- Change Epic scope

**Time commitment:** 1–3 hours per Epic reviewed

See [reviewer-guide.md](reviewer-guide.md) for the review checklist.

---

### Contributor (Developer)

**You implement Epics.**

Contributors are developers (human or AI agent) assigned to one or more Epics. You receive an Epic spec, create a branch, implement, and open a PR.

**What you control:**
- Implementation decisions within Epic scope
- Ask questions if the spec is ambiguous — escalate to your Milestone Agent

**You do NOT:**
- Modify Epic scope unilaterally
- Merge PRs yourself
- Deploy to production

**Time commitment:** Varies by Epic size (hours to days per Epic)

See [contributor-guide.md](contributor-guide.md) for the full Epic workflow.

---

### HQ Agent

**Autonomous planning agent.**

The HQ Agent operates in HQ Chat mode. It translates CFO decisions into Phase planning artifacts, reviews Phase Completion Notices, and coordinates Milestone Agents. In most team setups, the HQ Agent runs as an AI assistant.

**Authority:** Can approve Phase planning on CFO authorization. Cannot authorize production deployment.

---

### Milestone Agent

**Plans Epics, reviews and accepts Epic deliverables.**

The Milestone Agent creates Epic specs and Epic Execution Chat Starters, then reviews Completion Notices from Epic Agents. Issues Review Decisions (accept or reject).

**Authority:** Can accept or reject Epic Completion Notices. Cannot approve Phase-level decisions.

---

### Epic Agent (Coding Agent)

**Executes Epics in a sandbox.**

The Epic Agent receives an Epic Execution Chat Starter, implements the work, opens a PR, and produces a Completion Notice. After receiving a Review Decision (Accept), it merges the PR and issues a Delivery Notice.

**Authority:** Can implement within Epic scope. Cannot merge without explicit authorization.

---

## Authority Matrix at a Glance

| Decision Type | Who Decides | Where Recorded |
|---|---|---|
| Phase scope | CFO | Phase Authorization artifact |
| Phase planning | HQ Agent (on CFO authorization) | Phase Spec |
| Milestone planning | Phase Lead or Milestone Agent | Milestone Spec |
| Epic acceptance | Milestone Agent | Review Decision artifact |
| Code review gate | Reviewer | PR comment or Review Blockers artifact |
| Production deployment | CFO | Deployment Authorization artifact |
| Escalation resolution | Parent role in authority chain | Escalation artifact |

For full detail, see [decision-matrices.md](decision-matrices.md).

---

## Escalation Path

When you are blocked and cannot resolve an issue at your level:

```
Contributor → blocked?
  ↓ escalate to
Epic Agent / Milestone Agent
  ↓ still blocked?
  ↓ escalate to
Phase Lead / HQ Agent
  ↓ still blocked?
  ↓ escalate to
CFO (Layer-8) — final authority
```

**Rules:**
1. Document the blocker as an Escalation artifact (not just a chat message)
2. State the specific decision you need
3. Do not re-escalate once a decision is made — accept it and continue
4. SLA for response: Epic level 4 hours, Milestone 8 hours, Phase 24 hours, CFO 2 business days

---

## Execution Modes

### Manual Mode (Copy-Paste)

The CFO or Phase Lead manually copies Chat Starters into AI chat sessions and copies artifacts between chats. No infrastructure required.

**Best for:** Teams just getting started, weeks 1–4 of adoption.

Steps:
1. Open your AI assistant (Claude, ChatGPT, etc.)
2. Paste the relevant Chat Starter as your first message
3. The agent self-configures to the correct mode
4. When the agent produces a Completion Notice, copy it and paste into the parent chat
5. Parent chat produces a Review Decision — copy it back

### Agentic Mode (Daemon Routing)

The `ai-project-daemon` monitors the `.ai-project/artifacts/` directory and routes artifacts between chat sessions automatically. Completion Notices trigger parent review; Review Decisions trigger child execution.

**Best for:** Teams with 4+ weeks of experience, comfortable with Docker and CLI tooling.

See [example-walkthrough.md](example-walkthrough.md) for a step-by-step demonstration of both modes.

---

## Communication Norms

- **Decisions go in artifacts, not chat messages.** A decision made in chat is not authoritative unless recorded in an artifact file committed to the repo.
- **Escalations use Escalation artifacts.** Vague "help needed" messages are not escalations.
- **No lateral communication between chats.** Epic Chat A cannot communicate with Epic Chat B. Communicate upward to your parent chat only.
- **Async-first.** The system is designed to run without real-time meetings. Leave artifacts for your team; they will process them when available.

---

## Your First Week

| Day | What to Do |
|---|---|
| Day 1 | Read this guide. Read your role-specific guide. |
| Day 2 | Read the Project System Guidelines (§1–3) and your first Epic spec. |
| Day 3 | Open your first Epic Execution Chat. Ask questions if the spec is unclear. |
| Day 4 | Implement. Commit. Open PR. |
| Day 5 | Produce Completion Notice. Await Review Decision. |

**Your first Epic:** Ask your Phase Lead or HQ Agent to assign you a small, well-defined Epic. After you complete it successfully, your authority and trust level will expand.

---

## Cross-References

- [CFO Quick Start](cfo-quick-start.md) — for the strategic decision-maker
- [Contributor Guide](contributor-guide.md) — for developers implementing Epics
- [Reviewer Guide](reviewer-guide.md) — for code reviewers
- [Phase Lead Guide](phase-lead-guide.md) — for planning leads
- [Decision Matrices](decision-matrices.md) — who decides what, at a glance
- [Example Walkthrough](example-walkthrough.md) — real cycle end-to-end
- [FAQ](faq.md) — common questions answered
- [Troubleshooting Guide](troubleshooting-guide.md) — if something goes wrong
- [Governance: Roles & Authorization](../../governance/systems/roles-authorization-team-governance.md) — authoritative role definitions
