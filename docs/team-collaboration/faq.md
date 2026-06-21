# FAQ

**Frequently asked questions about team collaboration in the AI Project System.**

---

## Role & Authority

**Q1: We have two senior developers. Can both be CFO?**

No. The CFO role is held by exactly one person. Only one human can be the final production deployment authority and Phase authorization authority. If two people share strategic decisions, designate one as CFO and the other as Phase Lead. The Phase Lead can make tactical decisions within Phase scope, but all production deployments and Phase scope changes require CFO approval.

---

**Q2: Can the CFO also act as a Contributor?**

Technically yes, but it creates a self-authorization conflict: a contributor cannot approve their own work. If the CFO writes code on an Epic, a different person must act as Reviewer and the Milestone Agent must be an agent (not the CFO) to issue the Review Decision. This setup works for very small teams (2 people) but becomes awkward at scale.

---

**Q3: Who issues Review Decisions if we don't have a dedicated Milestone Agent?**

In manual mode, the Phase Lead issues Review Decisions directly. The Phase Lead reads the Completion Notice, evaluates the checklist, and issues the Review Decision artifact in the Milestone Chat. "Milestone Agent" is a role, not a specific person — the Phase Lead can fill it.

---

**Q4: A contributor says the spec is wrong. Who decides what the spec means?**

The contributor escalates to the Milestone Agent (or Phase Lead in manual mode). The Milestone Agent interprets the spec or amends it. If the amendment changes Epic scope significantly, it must be documented as a spec amendment artifact. The contributor does not interpret scope unilaterally.

---

## Workflow & Process

**Q5: How do I start my first Epic?**

1. Your Phase Lead or Milestone Agent sends you an Epic Execution Chat Starter and Epic Delivery Authorization.
2. Read the Epic spec fully before starting.
3. Create your branch: `git checkout -b epic/E#.#` from the milestone branch.
4. Implement per the spec. Open a PR.
5. Produce a Completion Notice, commit it to your branch.
6. In manual mode: paste it into your Milestone Chat. In agentic mode: the daemon routes it.
7. Await the Review Decision.

See [Contributor Guide](contributor-guide.md) for the complete step-by-step.

---

**Q6: My Epic was rejected. How many times can I resubmit?**

Up to 3 attempts. After 3 failed Completion Notices, the Epic Agent must produce an Escalation Notice (template: `governance/templates/escalation-notice.md`) to the Milestone Agent explaining why the work cannot be completed. The Milestone Agent then decides: escalate to Phase Lead, adjust the spec, or reassign the Epic.

The 3-attempt limit resets if the Milestone Agent explicitly grants an extension in writing.

---

**Q7: Can I work on two Epics at once?**

Yes, if your Phase Lead authorizes parallel execution. Common in practice: E1.1 and E1.2 often run in parallel when they have no code dependency. However:
- Each Epic has its own branch (`epic/E1.1`, `epic/E1.2`)
- Each Epic has its own Completion Notice
- Each Epic's Review Decision is independent
- Do not mix changes from different Epics on the same branch

---

**Q8: Do I need to update the spec if I deviate during implementation?**

No — the spec is immutable once issued. If you deviate from the spec (for a good reason), document the deviation in your Completion Notice under a "Deviations" section and explain your rationale. The Milestone Agent may accept the deviation or reject and ask you to comply with the original spec. Do not silently deviate and hope it passes review.

---

**Q9: Who handles code conflicts when two Epics touch the same file?**

The Phase Lead or Milestone Agent coordinates sequencing to minimize conflicts. If conflicts occur at merge time:
1. The Contributor resolves the merge conflict on their branch
2. The Contributor notifies the Reviewer that a conflict was resolved
3. The Reviewer checks that the conflict resolution is correct
4. The Completion Notice notes the conflict resolution

Do not resolve merge conflicts silently — document them in the Completion Notice.

---

## Artifacts & Governance

**Q10: Is a chat message a valid decision?**

No. Decisions recorded only in chat messages are not authoritative. The system rule is: **documentation is authoritative, chat is ephemeral.** Every decision — acceptance, rejection, escalation resolution, production authorization — must be recorded as an artifact file committed to the repository. A Review Decision in chat that is never committed to a file did not happen officially.

---

**Q11: How do I find out the current Phase status?**

Read the artifacts in `.ai-project/artifacts/`. Look for:
- `delivery-notices/` — what has been merged
- `completion-notices/` — what is pending review
- `review-decisions/` — what has been accepted or rejected

In agentic mode, the daemon maintains a queue status in `.ai-project/queue/`. In manual mode, your Phase Lead maintains status in the Milestone Chat.

---

**Q12: Can we skip the Completion Notice and merge directly?**

No. The Completion Notice → Review Decision sequence is required by governance. Merging without a Review Decision (Accept) violates the authorization protocol and may result in the work being reverted. The Completion Notice is what triggers the parent review. Without it, no review happens.

---

## Bugfix Epics

**Q13: There's a production bug. How do we handle it urgently?**

Use the Bugfix Epic workflow:
1. Report to HQ Chat: severity, affected component, scope estimate
2. HQ Agent evaluates and creates a minimal Bugfix Epic spec (`docs/bugfixes/B#.#__spec__...md`)
3. HQ Agent issues a Bugfix Epic Approval directly to you
4. You implement on a `bugfix/B#.#` branch
5. HQ Agent reviews your Completion Notice within 4 hours (SLA)
6. On Accept: merge to hotfix branch
7. Production deploy requires CFO authorization regardless of urgency

See [Governance: Bugfix Epic Workflow](../../governance/systems/bugfix-epic-workflow.md) and the [Troubleshooting Guide](troubleshooting-guide.md) for escalation steps.

---

**Q14: What is the difference between Bugfix Epic (B#.#) and a regular Epic (E#.#)?**

| | Regular Epic | Bugfix Epic |
|---|---|---|
| ID format | `E#.#` | `B#.#` |
| Planning path | Phase → Milestone → Epic | Direct to HQ Chat |
| Spec length | Full | Minimal (problem, fix, DoD) |
| Review SLA | 24 hours | 4 hours |
| Branch | `epic/E#.#` → `milestone/M#` | `bugfix/B#.#` → hotfix |
| Production gate | CFO (standard cycle) | CFO (required, expedited) |

---

## Agentic vs Manual Mode

**Q15: We're just starting. Should we use agentic mode?**

No. Start with manual mode (copy-paste). Manual mode requires no infrastructure and lets you learn the artifact formats and decision flow by doing. Once you have completed 3–5 Epics in manual mode and everyone understands the artifact cycle, then consider agentic mode.

The governance model is identical in both modes. Switching from manual to agentic later does not require any governance changes — only infrastructure setup.

See [Example Walkthrough](example-walkthrough.md) for a side-by-side comparison of both modes in action.

---

## P4: Completion, Review & Production

**Q16: How do I know when my work is complete?**

Work is complete only when every item in the Epic's **Definition of Done** is satisfied — deliverables built, tests passing, PR opened against the correct branch — *and* the parent chat has issued a Review Decision (Accept). Self-declaring "done" is not enough; completion is confirmed by the accepting Review Decision, not by your own judgment. See the [Contributor Guide](contributor-guide.md).

---

**Q17: How do I read a Completion Notice?**

A Completion Notice has YAML front-matter (`epic_id`, `pr_details`, `qa_status`) and a body. Read the front-matter first to confirm the Epic, the PR, and that QA passed; then read the body for deliverables, the Definition-of-Done checklist, and any noted deviations or risks. If `qa_status` is not `passed` or the DoD has gaps, that is your signal to Reject. The schema is defined in [Artifact Communication Protocol](../../governance/systems/artifact-communication-protocol.md).

---

**Q18: What is a Review Decision?**

A Review Decision is the artifact a reviewing chat (Milestone, Phase, or HQ) issues in response to a Completion Notice. It records one binding outcome — **Accept** (authorize merge) or **Reject** (require rework) — with feedback explaining why. Like every decision in the system, it is committed to the repository; a verdict given only in chat is not authoritative. Template: `governance/templates/review-decision.md`.

---

**Q19: When do I escalate, and to whom?**

Escalate **upward** (Epic → Milestone → Phase → HQ; never to a sibling) when you cannot resolve something within your authority: a blocking dependency, an out-of-scope finding, a missing or contradictory spec, or 3 exhausted rework attempts. Produce an **Escalation Notice** (template: `governance/templates/escalation-notice.md`) stating the blocker, what you tried, the decision you need, and the impact. Don't proceed on the blocked path until the parent responds.

---

**Q20: How do I authorize a production deployment?**

Only the **CFO** can authorize production deployment, and only by issuing a committed **Deployment Authorization** artifact — naming the build/commit, confirming verification (tests green, review accepted, Delivery Notice present), and stating a rollback plan. This gate applies to every path, including urgent bugfixes; urgency never waives it. See [CFO Quick Start](cfo-quick-start.md).

---

**Q21: What happens if a review SLA is missed?**

Regular Epics carry a 24-hour review SLA; Bugfix Epics carry 4 hours. If it's missed, first re-confirm the Completion Notice actually reached the reviewer (in manual mode, that it was pasted into the parent chat, not just committed). If there's still no response, escalate to the next level up (Milestone → Phase → HQ/CFO) and quantify the impact. A missed SLA is an escalation trigger, not a license to self-approve and merge. See the [Troubleshooting Guide](troubleshooting-guide.md).

---

**Q22: Can I skip the Definition of Done if I'm in a hurry?**

No. The Definition of Done is the contract between the spec and the merge — there is no fast path that skips it, and no role (not even the CFO) "waives" it for convenience. If a DoD item is genuinely wrong or impossible, that is a spec problem: escalate to amend the spec, don't silently drop the item. Bugfix Epics have a *smaller* DoD, not *no* DoD.

---

**Q23: How do I onboard a new team to the system?**

Start everyone with the [P4 Governance System Guide](P4-governance-system-guide.md), then have each person read their role guide ([CFO](cfo-quick-start.md), [Phase Lead](phase-lead-guide.md), [Contributor](contributor-guide.md), [Reviewer](reviewer-guide.md)). Run your first 3–5 Epics in **manual mode** using the [Taskflow example](../../examples/team-project-example/README.md) and [Example Walkthrough](example-walkthrough.md) as a reference, then consider agentic mode. The governance is identical in both modes, so switching later changes infrastructure, not process.

---

## Cross-References

- [P4 Governance System Guide](P4-governance-system-guide.md) — start here / entry point
- [Team Onboarding Guide](team-onboarding-guide.md) — full system overview
- [Contributor Guide](contributor-guide.md) — Epic workflow for developers
- [Reviewer Guide](reviewer-guide.md) — code review process
- [Phase Lead Guide](phase-lead-guide.md) — planning and coordination
- [CFO Quick Start](cfo-quick-start.md) — strategic authority overview
- [Decision Matrices](decision-matrices.md) — who decides what
- [Example Walkthrough](example-walkthrough.md) — real cycle from start to finish
- [Troubleshooting Guide](troubleshooting-guide.md) — when things go wrong
