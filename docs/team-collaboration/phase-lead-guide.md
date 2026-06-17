# Phase Lead Guide

**For the team member coordinating Milestones and Epics within a Phase.**

The Phase Lead owns Phase execution: you plan milestones, coordinate contributors, issue Epic assignments, and escalate blockers to CFO. This guide covers your workflow, decision authorities, and how you interact with the governance hierarchy.

---

## Your Role

The Phase Lead is an optional role assigned by the CFO. When present, the Phase Lead acts as the tactical execution authority for a Phase: you sit between the strategic CFO and the day-to-day Milestone Agents and contributors.

In teams without a dedicated Phase Lead, the HQ Agent fills this function directly.

**You own:**
- Milestone planning and sequencing within Phase scope
- Epic assignments (which contributor gets which Epic)
- Review Decisions for Epic Completion Notices (or you delegate to the Milestone Agent)
- Escalating blockers to CFO when they exceed your authority

**You do not own:**
- Phase scope (CFO defines this)
- Production deployment authorization (CFO only)
- Phase cancellation (CFO only)

---

## Milestone Planning

### Your Starting Point

You receive:
- **Phase Spec** — defines goals, success criteria, and milestone stubs
- **Phase Delivery Authorization** — CFO's approval to begin Phase execution

Read the Phase Spec fully before planning. Identify:
- Dependencies between milestones (which must complete before another starts?)
- Resource constraints (which contributors are available?)
- Timeline pressure (is there a deadline?)

### Sequencing Milestones

Milestones should be sequenced to:
1. Unblock dependencies early (if M2 depends on M1 output, M1 goes first)
2. Parallelize where possible (M2 and M3 can run concurrently if no shared dependency)
3. Deliver value incrementally (prefer completing a milestone over partial progress on three)

Produce a **Phase Strategy Document** with your sequencing decision and rationale. This is your artifact; commit it to the repository.

### Delegating to Milestone Agents

For each Milestone, you issue a **Milestone Execution Chat Starter** (or have the HQ Agent produce it). This document opens the Milestone planning session.

You assign a Milestone Agent (AI or human) to each Milestone. The Milestone Agent then plans the Epics, produces Epic specs, and assigns Epic Execution Chat Starters.

---

## Epic Acceptance: Review Decisions

When an Epic is complete, the Epic Agent or Contributor produces a **Completion Notice**. Your Milestone Agent receives it first and reviews it. You act as the oversight layer:

- For well-defined, in-scope Epics: let the Milestone Agent issue the Review Decision
- For Epics with disputed scope or quality concerns: review directly and issue the Review Decision yourself
- For Epics requiring CFO visibility (e.g., scope changes, major risk): escalate to CFO before issuing

**How to issue a Review Decision (Accept):**

In your Milestone Chat, state:
> "E1.1 accepted. All deliverables complete, Reviewer approved, no blockers. Authorized to merge."

The Milestone Agent records this as a Review Decision (Accept) artifact and authorizes the contributor to merge.

**How to issue a Review Decision (Reject):**

> "E1.1 rejected. Test coverage is below the spec requirement. Three error paths are untested. Rework required: add tests for timeout, invalid token, and concurrent session cases."

Be specific. The contributor must address every listed item before resubmitting.

---

## Escalation to CFO

You escalate to CFO when:
- A decision affects Phase scope (adding/removing milestones, changing goals)
- A team conflict cannot be resolved at the Milestone level
- A production deployment is needed (always escalates to CFO)
- A timeline change requires CFO buy-in (budget, commitments)
- An escalation from a Milestone Agent reaches you and exceeds your authority

**How to escalate:**
1. Produce an **Escalation artifact** (file in `.ai-project/artifacts/escalations/`)
2. Copy it into HQ Chat with a clear header: "ESCALATION: <title>"
3. State: what the issue is, what you've tried, and what decision you need from CFO
4. Wait for CFO response (SLA: 2 business days, or URGENT for blockers)
5. Record CFO's decision in the artifact and cascade it downward

---

## Working with Milestone Agents

The Milestone Agent is your execution arm for planning. Your relationship:

| You direct | Milestone Agent executes |
|---|---|
| "Plan M1 first, then M2 and M3 in parallel" | Creates Milestone specs and Chat Starters |
| "Assign E1.1 and E1.2 to Jamie" | Issues Epic Delivery Authorizations |
| "E1.3 Completion Notice looks good — accept it" | Issues Review Decision (Accept) artifact |
| "B1.1 needs expedited review (4-hour SLA)" | Triggers expedited Bugfix Epic review |

**What you do not do:** Rewrite Milestone specs or Epic specs unilaterally. If a spec needs changing, work with the Milestone Agent and document the change as an amendment artifact.

---

## Bugfix Epics

When a production issue is discovered during Phase execution:

1. Evaluate with HQ Agent: is this a Bugfix Epic or a planned Epic?
2. If Bugfix: HQ Agent or you create a minimal Bugfix Epic spec (stored in `docs/bugfixes/B#.#__spec__...md`)
3. Issue Epic Delivery Authorization directly to the developer
4. Expedited review SLA: 2–4 hours (not 24 hours)
5. Authorize merge to `bugfix/B#.#` → `hotfix` or `master` (with CFO production gate)

Bugfix Epics bypass Milestone planning ceremony but do not bypass the CFO production deployment gate.

See [Governance: Bugfix Epic Workflow](../../governance/systems/bugfix-epic-workflow.md) for the full protocol.

---

## Reporting Phase Progress to CFO

Keep the CFO informed without overwhelming them. A good cadence:

- **Weekly status message in HQ Chat:** Milestones complete this week, in-flight, blocked
- **Escalation artifact:** Only when CFO decision is actually needed
- **Phase Completion Notice:** When all milestones in the Phase are done

Format for weekly status (optional but recommended):

```
Phase P1 Status — Week of <date>

Completed this week:
- M1 (Core Backend): merged to phase/P1 ✓

In progress:
- M2 (Frontend): E2.1 in review, E2.2 in implementation

Blocked:
- None

Next week:
- M2 final Epic (E2.3) starts Monday
- M3 planning begins Wednesday

Decisions needed from CFO: None this week.
```

---

## Phase Closure

When all milestones are complete:

1. Confirm all Milestone Delivery Notices are committed
2. Produce a **Phase Completion Notice** summarizing all delivered milestones
3. Submit to HQ Chat (or CFO directly) for Phase acceptance
4. Await Phase Review Decision (Accept/Reject from HQ Agent or CFO)
5. On Accept: Phase Lead work is done. Phase merges to `phase/P#` via authorized agent.

---

## Cross-References

- [Team Onboarding Guide](team-onboarding-guide.md) — full system overview
- [CFO Quick Start](cfo-quick-start.md) — what the CFO needs from you
- [Contributor Guide](contributor-guide.md) — what your contributors are expected to do
- [Reviewer Guide](reviewer-guide.md) — how your reviewers participate
- [Decision Matrices](decision-matrices.md) — who decides what
- [Example Walkthrough](example-walkthrough.md) — real Phase Lead actions in context
- [FAQ](faq.md) — common questions
- [Troubleshooting Guide](troubleshooting-guide.md) — if something goes wrong
- [Governance: Roles & Authorization](../../governance/systems/roles-authorization-team-governance.md) — authoritative role definitions
- [Governance: Bugfix Epic Workflow](../../governance/systems/bugfix-epic-workflow.md) — expedited bugfix path
