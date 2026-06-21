# Team Collaboration Guides

**Documentation for adopting the AI Project System as a team.**

New to P4? Start with the **[P4 Governance System Guide](P4-governance-system-guide.md)** —
the entry point that explains what P4 adds and links to everything here. Then pick your
role below and read your guide first.

---

## Start by Role

| Your Role | Start Here | Time to Read |
|---|---|---|
| **CFO / Project Owner** | [CFO Quick Start](cfo-quick-start.md) | 5 min |
| **Phase Lead / Team Lead** | [Phase Lead Guide](phase-lead-guide.md) | 15 min |
| **Developer / Contributor** | [Contributor Guide](contributor-guide.md) | 15 min |
| **Code Reviewer** | [Reviewer Guide](reviewer-guide.md) | 10 min |
| **New to the whole system** | [Team Onboarding Guide](team-onboarding-guide.md) | 20 min |

---

## All Guides

### Start Here

- [P4 Governance System Guide](P4-governance-system-guide.md) — Entry point: what P4 is, key concepts, and links to every guide

### Role Guides

- [Team Onboarding Guide](team-onboarding-guide.md) — System overview, all roles, authority matrix, your first week
- [CFO Quick Start](cfo-quick-start.md) — Your job, typical week, how to review and authorize
- [Contributor Guide](contributor-guide.md) — Full Epic workflow from spec to merged PR
- [Reviewer Guide](reviewer-guide.md) — Review checklist, how to block, how to approve
- [Phase Lead Guide](phase-lead-guide.md) — Milestone planning, Epic acceptance, escalation to CFO

### Reference

- [Decision Matrices](decision-matrices.md) — Who decides what, in table format
- [FAQ](faq.md) — 23 answered "How do I...?" questions
- [Troubleshooting Guide](troubleshooting-guide.md) — Common problems with problem → cause → solution structure

### Tutorial

- [Example Walkthrough](example-walkthrough.md) — Real Epic cycle using the Taskflow example project (E16.1 artifacts)

---

## Quick Answers

**Who approves a merge?** Milestone Agent, after Review Decision (Accept). See [Decision Matrices](decision-matrices.md).

**Who authorizes production?** CFO. Always. No exceptions. See [CFO Quick Start](cfo-quick-start.md).

**What do I do when my Epic is rejected?** See [Contributor Guide — Step 7](contributor-guide.md) and [FAQ Q6](faq.md).

**How does artifact routing work?** See [Example Walkthrough — Part 5](example-walkthrough.md).

**Something went wrong.** See [Troubleshooting Guide](troubleshooting-guide.md).

---

## Governance References

These guides derive all role authorities from the governance documents. If anything here conflicts with governance, governance takes precedence:

- [Roles, Authorization & Team Governance](../../governance/systems/roles-authorization-team-governance.md) — authoritative role definitions
- [Artifact Communication Protocol](../../governance/systems/artifact-communication-protocol.md) — Completion Notice, Review Decision, Delivery Notice schemas
- [Bugfix Epic Workflow](../../governance/systems/bugfix-epic-workflow.md) — expedited bugfix path
- [Chat Hierarchy](../../governance/systems/chat-hierarchy.md) — four-level authority chain
