# P4 Governance System Guide

**The entry point to Team Collaboration & Artifact-Driven Communication.**

Welcome. If you are new to running the AI Project System as a team — or you are a CFO,
Phase Lead, or new team member onboarding — start here. This page explains what P4 adds,
the few concepts you need, and where to go next.

---

## What is P4?

Phases P1–P3 made the AI Project System work for a solo developer: structured specs, a
Phase → Milestone → Epic hierarchy, and an autonomous execution cluster. **P4 makes it
work for a team.**

It adds three things:

1. **Artifact-Driven Communication (P4.1)** — work and decisions move between people and
   chats as committed Markdown files, not chat messages.
2. **Bugfix Epic Workflow (P4.2)** — an expedited path for unplanned production issues,
   with a 4-hour review SLA and a hard production-deployment gate.
3. **Roles & Authorization (P4.3)** — explicit team roles (CFO, Phase Lead, Contributor,
   Reviewer, and the chat agents) with a decision matrix that records who decides what.

The guiding rule across all of P4: **documentation is authoritative; chat is ephemeral.**
A decision that lives only in a chat message did not officially happen.

---

## Key concepts

**Artifacts.** Structured files (YAML front-matter + body) committed to the repo. The
core review cycle uses three:

- **Completion Notice** — an Epic says "I'm done; please review." (Epic → Milestone)
- **Review Decision** — the reviewer says **Accept** (merge) or **Reject** (rework).
- **Delivery Notice** — after merge, the Epic records the merge and closes its chat.

Supporting artifacts have canonical templates too: **Merge Authorization**, **Epic
Closure Notice**, and **Escalation Notice**.

**Roles.** Authority is bounded by role. The **CFO** is the single human strategic
authority and the only one who authorizes production deployment. The **Phase Lead** plans
and accepts within a Phase. **Contributors** build Epics; **Reviewers** review them.

**The rework cycle.** A rejected Epic gets up to **3 attempts**. If the third still
fails, the team escalates to the Phase Chat with an Escalation Notice rather than
retrying indefinitely.

**The production gate.** No code reaches production without an explicit CFO Deployment
Authorization — on every path, including urgent bugfixes. Urgency never waives the gate.

---

## Quick links

### Start by role
- [Team Onboarding Guide](team-onboarding-guide.md) — system overview, all roles, your first week
- [CFO Quick Start](cfo-quick-start.md) — strategic authority and the production gate
- [Phase Lead Guide](phase-lead-guide.md) — milestone planning, Epic acceptance, escalation
- [Contributor Guide](contributor-guide.md) — the full Epic workflow for developers
- [Reviewer Guide](reviewer-guide.md) — review checklist and how to block

### Reference
- [Decision Matrices](decision-matrices.md) — who decides what, in table form
- [FAQ](faq.md) — answered "How do I…?" questions
- [Troubleshooting Guide](troubleshooting-guide.md) — problem → cause → solution
- [Example Walkthrough](example-walkthrough.md) — a real Epic cycle, start to finish

### Learn by example
- [Taskflow Team Project Example](../../examples/team-project-example/README.md) — a
  complete team project with real artifacts, a rejected-then-reworked Epic, and a bugfix.

### Governance (authoritative)
- [Artifact Communication Protocol](../../governance/systems/artifact-communication-protocol.md) — every artifact schema
- [Bugfix Epic Workflow](../../governance/systems/bugfix-epic-workflow.md) — the expedited path
- [Roles, Authorization & Team Governance](../../governance/systems/roles-authorization-team-governance.md) — authoritative role definitions
- [HQ](../../governance/systems/hq-execution-chat-starter.md) ·
  [Milestone](../../governance/systems/milestone-execution-chat-starter.md) chat starters

If anything in these team guides ever conflicts with the governance documents,
**governance takes precedence.**

---

## Where to go next

| You are… | Read first | Then |
|----------|-----------|------|
| A new team member | [Team Onboarding Guide](team-onboarding-guide.md) | [Example Walkthrough](example-walkthrough.md) |
| A CFO / Project Owner | [CFO Quick Start](cfo-quick-start.md) | [Decision Matrices](decision-matrices.md) |
| A Phase Lead | [Phase Lead Guide](phase-lead-guide.md) | [Troubleshooting Guide](troubleshooting-guide.md) |
| A developer | [Contributor Guide](contributor-guide.md) | [FAQ](faq.md) |
| Stuck right now | [Troubleshooting Guide](troubleshooting-guide.md) | [FAQ](faq.md) |

Start manual (copy-paste artifacts between chats) until the cycle feels natural, then
graduate to agentic mode. The governance is identical in both.
</content>
