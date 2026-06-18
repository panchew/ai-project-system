# CFO Quick Start

**Your job in under 5 minutes.**

> 📍 Part of the **[P4 Governance System Guide](P4-governance-system-guide.md)** — the entry point to all team-collaboration docs.

---

## Your Role

You are the CFO — the single source of strategic authority for this project. One person holds this role; it cannot be delegated away. Everything escalates to you eventually. Two things require your explicit approval that no one else can give:

1. **Authorizing new Phases** (scope, budget, timeline)
2. **Authorizing production deployments** (no deploy happens without you)

Everything else is handled by agents and your team.

---

## Your Job in Bullet Points

- **Authorize Phases.** When HQ Agent presents a Phase for approval, you say yes or no and record it.
- **Authorize production deployments.** You receive a Deployment Authorization Request; you approve or reject it.
- **Review escalations.** When the team is blocked and no one lower can decide, it reaches you.
- **Override decisions when necessary.** You can override any lower-level decision — but document your rationale.
- **Assign team members.** You decide who is Phase Lead, Reviewer, or contributor on a project.

**You do not** merge PRs directly, modify governance rules, or bypass Definition of Done.

---

## Your Typical Week

| Activity | Frequency | Time |
|---|---|---|
| Visit HQ Chat, read status | 2–3x per week | 10 min |
| Issue Phase Authorization | Once per Phase start | 5 min |
| Review Deployment Authorization Request | Once per release | 10 min |
| Respond to escalations | As needed | 5–15 min |
| **Total** | | **30 min – 2 hours/week** |

---

## How to Review a Completion Notice

When a Phase or Milestone finishes, HQ Agent presents you with a **Completion Notice**. Here is how to review it:

1. Open HQ Chat (or read the artifact file at `.ai-project/artifacts/completion-notices/`).
2. Check the `deliverables` list — are all items marked `ready`?
3. Check `qa_status` — must be `passed`.
4. Check `blockers` — should be empty.
5. Decide: accept or reject.

**If accepting:** Instruct HQ Agent to issue a Review Decision (Accept).

**If rejecting:** State the specific items that need rework. HQ Agent issues a Review Decision (Reject) with your feedback.

---

## How to Issue a Review Decision

You do not write the artifact yourself — that is HQ Agent's job. You state your decision in HQ Chat:

> "Phase P1 is accepted. Proceed to production planning."

or

> "Phase P1 is rejected. The performance milestone was not delivered. Rework required."

HQ Agent records this as a Review Decision artifact committed to the repository.

---

## How to Authorize Production Deployment

When a release is ready, you receive a **Deployment Authorization Request** artifact. It tells you:
- What is deploying
- Known risks
- Rollback plan

Your response in HQ Chat:

> "Approved. Deploy P1 to production."

or

> "Rejected. Address the rollback plan gap first."

HQ Agent records your decision and the deployment proceeds (or pauses) accordingly.

**This gate is non-negotiable.** No production deployment occurs without this artifact and your explicit approval.

---

## What You Can Override

You can override any decision at any level — but you must document the reason:

> "Overriding Milestone Agent's rejection of E1.2. The spec gap was mine, not the contributor's. Treating E1.2 as accepted."

Document overrides in HQ Chat so HQ Agent can record them as artifacts.

---

## Escalation: What Reaches You

Issues escalate to you when no lower level can decide. Common triggers:

- A Phase Lead and HQ Agent disagree on scope
- A production incident requires immediate deployment outside the normal cycle
- A security or compliance concern requires strategic decision
- A team conflict cannot be resolved at the Milestone level

When you receive an escalation:
1. Read the Escalation artifact (in `.ai-project/artifacts/` or in HQ Chat)
2. Make a decision
3. State it clearly in HQ Chat
4. HQ Agent records it and cascades the decision downward

**SLA:** Escalations marked URGENT should be addressed within same business day.

---

## Cross-References

- [Team Onboarding Guide](team-onboarding-guide.md) — full team overview
- [Decision Matrices](decision-matrices.md) — who decides what
- [Troubleshooting Guide](troubleshooting-guide.md) — if something goes wrong
- [Governance: Roles & Authorization](../../governance/systems/roles-authorization-team-governance.md) — authoritative definitions
