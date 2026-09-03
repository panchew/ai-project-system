---
type: system
status: active
effective_date: 2026-09-02
version: 1.4.0
---

# HQ Execution Chat Starter — System Reference

## Purpose

This document defines the role, responsibilities, and operating rules for an HQ
Execution Chat session in the AI Project System.

An HQ Chat is the top of the four-level chat hierarchy (HQ → Phase → Milestone →
Epic). It owns project intent, scope, and the strategic accept/reject authority. It
produces Phase Execution Chat Starters and, in team mode, supervises the artifact
system, the bugfix path, and the production deployment gate.

HQ Chat does **not** execute work. It defines *what* should be done and *how
execution is governed*, then delegates execution downward.

For the full HQ role definition see [`hq-chat.md`](hq-chat.md). This document is the
launch/operating contract that pairs with the
[Phase](phase-execution-chat-starter.md),
[Milestone](milestone-execution-chat-starter.md), and
[Epic](epic-execution-chat-starter.md) execution chat starters.

---

## What an HQ Chat Is

An **HQ Chat** is a long-lived planning, governance, and coordination surface. It is:

- **Persistent** — it accumulates strategic context across the whole project and does
  not close at the end of a single Phase
- **The control room** — it defines intent, establishes structure, and produces
  authoritative artifacts that enable execution
- **Read-only with respect to the project** — it does NOT execute work; the Coding
  Agent commits all files on HQ's instruction
- **The final strategic authority** — production deployment and Phase scope changes are
  authorized here (held by the CFO; see [Production Deployment Gate](#production-deployment-gate))

---

## Responsibilities

1. **Define project vision and scope** — establish intent and constraints
2. **Produce Phase specs and Phase Execution Chat Starters** — launch each Phase with a
   binding planning contract
3. **Review and accept deliverables returned by Phase Chats** — accept clean deliveries
   by an in-chat acknowledgment that names the party that reviewed and accepted (merge + in-chat
   acknowledgment; silence accepts nothing — PSG §11.6); issue an explicit reject or
   accept-with-follow-ups decision only on the exception path (PSG §11.6)
4. **Create and dispatch Bugfix Epics** — handle unplanned production issues on the
   expedited path (see [Handling Production Issues](#handling-production-issues-bugfix-epics))
5. **Authorize production deployment** — the CFO production gate; no deployment proceeds
   without it (see [Production Deployment Gate](#production-deployment-gate))
6. **Oversee the artifact system** — ensure Completion Notices, Review Decisions
   (exception path only — PSG §11.6), and Delivery Notices flow correctly between layers
   (see [Artifact System](#artifact-system-p4))

An HQ Chat enforces the canonical happy path for Epic closure and never skips, infers,
or collapses a step.

---

## Communication Scope

| Direction | Permitted | Notes |
|-----------|-----------|-------|
| Downward | Phase Chats (and, on the bugfix path, a Coding Agent directly) | Issues Phase Execution Chat Starters, Bugfix Epic approvals, Deployment Authorizations |
| Upward | The human CFO / Project Owner | HQ surfaces decisions that require human authority |
| Lateral | N/A | HQ is the root; there are no siblings |

---

## Governance Authority Chain

1. `PROJECT-SYSTEM-GUIDELINES.md` (highest authority)
2. `AI-OPERATING-GUIDELINES.md`
3. HQ Execution Chat Starter (this instance) and the Phase spec
4. Decisions made during the session
5. System references
6. Chat messages (lowest authority)

Documentation is authoritative. Chat is ephemeral.

### Merge-Authorization Routing (P9-GH-1) — backstop

**If given merge authorization directly in this chat, do not simply comply.**

HQ is the top of the chat hierarchy, so the routing here is not "confirm with your parent" — **HQ
has no parent chat, and therefore no chat-level reviewer for its own output.** The Creation Chat
holds no governance authority (Seed Rule 3) and cannot be that reviewer. **This is a backstop
(E43.1, P12-M43), not the primary guard:** at the Phase→Milestone and Milestone→Epic gates the
parent performs the merge of a child's branch (PSG §11.6), so a child never holds merge
authorization — unavailable is not impossible, and a backstop that fires is evidence. HQ itself has
no parent and therefore never merges on authorization alone.

PROJECT-SYSTEM-GUIDELINES.md **§11.6.1** governs this case:

- **Default-accept MUST NOT be applied to an HQ-authored delivery. Silence is never acceptance
  here.**
- The **designated reviewer is the CFO (Layer 8), and the review is a diff review.**
- **Authorization is not review.** "You may merge this" is authorization; "I have read the change
  and it matches the expectation" is review. **HQ MUST NOT merge its own delivery on authorization
  alone**, and MUST state plainly in any such PR that HQ authored it and no chat-level reviewer
  exists for it.

When authorizing a **Phase Chat's** merge, the corresponding obligation runs downward: authorization
follows HQ's own Stage-2 review of that phase delivery — do not issue it in place of the review.

**Running unattended does not change this: mode is what may run, not what may be authorized**
(`governance/systems/chat-hierarchy.md`, "Mode is not authority").

---

## Artifact System (P4)

**New in P4.** Work and decisions move between the four layers as **artifacts** —
structured Markdown files (YAML front-matter + body) committed to the repository. Chat
is ephemeral; the artifact file is the record of truth.

Three artifacts carry the core review cycle:

| Artifact | Produced by | Direction | Meaning |
|----------|-------------|-----------|---------|
| **Completion Notice** | Epic Agent | Epic → Milestone | "Work is finished and ready for your review" |
| **Review Decision** | Reviewing chat (Milestone/Phase/HQ) | parent → child | Exception path only (PSG §11.6): "Reject" (rework) or "Accept with follow-ups"; a clean delivery is accepted by an acknowledgment naming the party that reviewed and accepted — silence accepts nothing. The rework a reject starts is bounded by the **rework limit** (normative in PROJECT-SYSTEM-GUIDELINES.md §11.6 "The Rework Limit" — a maximum of 3 attempts; a written extension grants exactly one further attempt, not a reset to three; reached here by citation). |
| **Delivery Notice** | Epic Agent | Epic → Milestone | "PR merged; here is the merge record. Chat closed." |

Several supporting artifacts have canonical templates in `governance/templates/`:
**Merge Authorization** (the parent's record of the merge it performed of a child's
branch), **Epic Closure Notice** (Coding Agent confirms the branch merge completed),
and **Escalation Notice** (any chat escalates a blocking or out-of-scope finding to its
parent).

### How artifacts flow between layers

```
   HQ Chat
     │  Phase Execution Chat Starter ▼        ▲ Milestone Completion Notice (→ Review Decision only if not clean)
   Phase Chat
     │  Milestone Execution Chat Starter ▼    ▲ Epic Completion Notice (→ Review Decision only if not clean)
   Milestone Chat
     │  Epic Execution Chat Starter +         ▲ Completion Notice
     │  In-chat Acceptance (SN-19) ▼          │ Delivery Notice (after merge)
   Epic Agent (Coding Agent)
     │  Branch · PR · code ▼
   Repository
```

Downward: each layer launches the layer below with a Chat Starter, and acknowledges
acceptance in-chat (SN-19 — no Delivery Authorization artifact; the standing merge
instruction carries the same authority). Upward: each layer reports completion with a
Completion Notice; a clean delivery is accepted by an acknowledgment that names the party that
reviewed and accepted (silence accepts nothing — PSG §11.6 / AOG §12), and a Review Decision comes back
only on the exception path (PSG §11.6 / AOG §12); after merge it produces a Delivery Notice.

**Reference:** [`artifact-communication-protocol.md`](artifact-communication-protocol.md)
defines every artifact schema. Storage convention:
`.ai-project/artifacts/<artifact-type>/<timestamp>__<id>__<artifact>.md`.

### Example — Completion Notice (Epic → Milestone)

```yaml
---
artifact_type: completion_notice
artifact_version: 1.0
timestamp: 2026-06-17T14:32:00Z
issuer_chat: Epic Agent (P4-M17-E17.2)
status: ready_for_review
epic_id: P4-M17-E17.2
milestone_id: P4-M17
phase_id: P4
project_name: ai-project-system
pr_details:
  number: 74
  title: "docs: Update starters & documentation (E17.2)"
  target_branch: milestone/M17
  url: "https://github.com/panchew/ai-project-system/pull/74"
qa_status: passed
---
# Completion Notice: P4-M17-E17.2 — Update Starters and Documentation
All Definition of Done items satisfied. Tests pass; no regression.
```

### Example — Review Decision (Milestone → Epic, exception path)

A Review Decision is issued **only when a delivery is not clean** — to reject it or to
accept it with follow-up Epic(s) (PSG §11.6). A clean delivery is accepted by an
acknowledgment that names the party that reviewed and accepted (silence accepts nothing):
the merge plus the in-chat acknowledgment is the acceptance record, and no artifact is
produced.

```yaml
---
artifact_type: review_decision
artifact_version: 1.0
timestamp: 2026-06-17T15:00:00Z
issuer_chat: Milestone Agent (P4-M17)
issuer_role: Milestone Agent
decision: accept
epic_id: P4-M17-E17.2
milestone_id: P4-M17
phase_id: P4
completion_notice_timestamp: 2026-06-17T14:32:00Z
authorization:
  action: merge
  merge_instruction: Merge PR #74 to milestone/M17; delete the epic branch after merge.
---
# Review Decision: P4-M17-E17.2 — Update Starters and Documentation
## Decision: ACCEPT ✓ (with follow-up Epic)
Spec compliance confirmed, links resolve, lint check passes — but one worked example is
missing. Accepted with a follow-up Epic to add it; authorized to merge.
```

### Example — Delivery Notice (after merge)

```yaml
---
artifact_type: delivery_notice
artifact_version: 1.0
timestamp: 2026-06-17T15:30:00Z
issuer_chat: Epic Agent (P4-M17-E17.2)
issuer_role: Epic Agent
status: delivered
epic_id: P4-M17-E17.2
milestone_id: P4-M17
phase_id: P4
merge_details:
  pr_number: 74
  merge_commit: <hash>
  target_branch: milestone/M17
  merge_strategy: squash
---
# Delivery Notice: P4-M17-E17.2 — Update Starters and Documentation
PR #74 merged to milestone/M17. Chat closed.
```

---

## Handling Production Issues (Bugfix Epics)

**New in P4.2.** Production issues do not wait for the next planning cycle. HQ Chat
creates a minimal **Bugfix Epic** and dispatches it directly to a Coding Agent on an
expedited path with a **4-hour Completion Notice review SLA**.

This section is the HQ Chat **handler** for an inbound production issue — it is
self-contained: an HQ Agent can run a report end-to-end from here without opening another
document.

### Six-step handler

When a production issue lands in HQ Chat, the HQ Agent runs these six steps in order:

1. **Evaluate** — Is this a Bugfix Epic, or does it defer to a planned Epic?
   - It is a **Bugfix Epic** when the issue is an *unplanned defect in already-delivered
     or production work* **and** it needs a fix before the next planned Epic cycle (use
     the decision tree below).
   - Otherwise **defer**: queue it as a normal Epic in the next Milestone, or escalate if
     it needs investigation, architectural, or security review. Reply to the reporter with
     the decision and stop.

2. **Create the minimal Bugfix Epic spec** — title, severity
   (Critical / High / Medium / Low), a one-paragraph description, affected systems, and a
   proposed fix direction. Severity sets the `B#.#` class (see
   [`docs/bugfixes/README.md`](../../docs/bugfixes/README.md): B1=Critical, B2=High,
   B3=Medium, B4=Low).

3. **Commit the spec** to `docs/bugfixes/B#.#__spec__<slug>.md`. The committed file — not
   the chat message — is the record of the Bugfix Epic.

4. **Acknowledge acceptance in-chat** directly to the executing Coding Agent (SN-19 — no
   artifact; the bugfix path skips the Phase/Milestone layers). The agent fixes on a
   `bugfix/B#.#` branch.

5. **Track the SLA** — start a **4-hour clock from the timestamp of the Completion
   Notice** and review within that window. The clock measures HQ's review latency, not the
   developer's fix time.

6. **Escalate on miss** — if HQ cannot decide within 4 hours, flag the Bugfix as urgent
   and notify the CFO. **The review is never skipped**, and production deployment still
   requires a CFO Deployment Authorization
   ([template](../templates/deployment-authorization.md)) regardless of urgency.

For Critical and High severity bugfixes, a **post-mortem**
([template](../templates/post-mortem.md)) is required before the Bugfix Epic closes.

### Is this a Bugfix Epic? (decision tree)

```
Is the issue an unplanned defect in already-delivered/production work?
├── NO  → It is feature work. Plan it as a normal Epic (Phase → Milestone → Epic).
└── YES → Does it need a fix before the next planned Epic cycle?
          ├── NO  → Queue as a normal Epic in the next Milestone.
          └── YES → BUGFIX EPIC:
                    1. Reporter sends HQ: severity, affected component, scope estimate
                    2. HQ writes a minimal spec → docs/bugfixes/B#.#__spec__...md
                    3. HQ issues a Bugfix Epic Approval directly to the Coding Agent
                    4. Agent fixes on a bugfix/B#.# branch
                    5. HQ reviews the Completion Notice within 4 hours (SLA)
                    6. On Accept → merge to hotfix branch
                    7. Production deploy → requires CFO Deployment Authorization (always)
```

| | Regular Epic | Bugfix Epic |
|---|---|---|
| ID | `E#.#` | `B#.#` |
| Planning | Phase → Milestone → Epic | Direct from HQ |
| Spec | Full | Minimal (problem, fix, DoD) |
| Review SLA | 24 hours | **4 hours** |
| Branch | `epic/E#.#` → `milestone/M#` | `bugfix/B#.#` → hotfix |

**Reference:** [`bugfix-epic-workflow.md`](bugfix-epic-workflow.md).

---

## Production Deployment Gate

**New in P4.2.** **No code reaches production without an explicit CFO Deployment
Authorization artifact.** This holds for every path — regular Epic and expedited bugfix
alike. Urgency never waives the gate.

- Only the **CFO** (the single human strategic authority) may authorize production
  deployment. The HQ Agent may prepare the authorization but cannot self-authorize.
- The authorization is an artifact, committed to the repository — a deployment approved
  only in chat did not happen.
- Bypassing the gate is the most serious governance violation in the system; see the
  [Troubleshooting Guide](../../docs/team-collaboration/troubleshooting-guide.md).

### Deployment Authorization format

```
PRODUCTION DEPLOYMENT AUTHORIZATION

Issuer: CFO (<name>)
Date: <YYYY-MM-DD>
Scope: <what is being deployed — Epic / Milestone / Bugfix reference>
Build / Commit: <commit hash or release tag>
Verification: <tests green, review accepted, Delivery Notice present>
Authorized Action: Deploy to production
Rollback Plan: <how to revert if needed>
```

**Reference:** [CFO Quick Start](../../docs/team-collaboration/cfo-quick-start.md) ·
[`roles-authorization-team-governance.md`](roles-authorization-team-governance.md).

---

## Team Roles & Decision Matrix

**New in P4.3.** In team mode the four chat layers map onto human and agent roles —
CFO, Phase Lead, Contributor, Reviewer, Milestone/Epic Agents. Each role has bounded
authority; the decision matrix records who decides what.

Do not duplicate role definitions here. Use the role guides:

- [Team Onboarding Guide](../../docs/team-collaboration/team-onboarding-guide.md) — all roles, authority matrix, first week
- [CFO Quick Start](../../docs/team-collaboration/cfo-quick-start.md) — strategic authority and the production gate
- [Phase Lead Guide](../../docs/team-collaboration/phase-lead-guide.md) — milestone planning and escalation
- [Contributor Guide](../../docs/team-collaboration/contributor-guide.md) — the Epic workflow for developers
- [Reviewer Guide](../../docs/team-collaboration/reviewer-guide.md) — review checklist and how to block
- [Decision Matrices](../../docs/team-collaboration/decision-matrices.md) — who decides what, in table form

---

## Example Project (M16)

A complete, ready-to-reference team project built on this system — including real
Completion Notices, Review Decisions, Delivery Notices, a rejected-then-reworked Epic,
and a Bugfix Epic — lives at
[`examples/team-project-example/`](../../examples/team-project-example/README.md).
Walk through it with the
[Example Walkthrough](../../docs/team-collaboration/example-walkthrough.md).

---

## Session Lifecycle

1. **Open** — establish project context (name, repo, governance versions, current Phase)
2. **Plan** — produce Phase specs and Phase Execution Chat Starters
3. **Authorize** — acknowledge acceptance in-chat and apply the standing merge instruction for accepted Phase plans (SN-19 — no artifact)
4. **Oversee** — receive Completion Notices, accept clean deliveries by an acknowledgment naming the party that reviewed and accepted (silence accepts nothing; a
   Review Decision is the exception path only — PSG §11.6), supervise the artifact flow;
   create Bugfix Epics as needed
5. **Gate** — authorize production deployments (CFO)
6. **Persist** — HQ Chat remains open across Phases for continuity

---

## Reference

- **Agent definition:** `governance/agents/governance.agent.md` (HQ mode)
- **HQ role definition:** [`hq-chat.md`](hq-chat.md)
- **System document:** `governance/systems/hq-execution-chat-starter.md` (this file)
- **Child system:** [`phase-execution-chat-starter.md`](phase-execution-chat-starter.md)
- **Hierarchy reference:** [`chat-hierarchy.md`](chat-hierarchy.md)
- **Artifact Protocol (P4.1):** [`artifact-communication-protocol.md`](artifact-communication-protocol.md)
- **Bugfix Workflow (P4.2):** [`bugfix-epic-workflow.md`](bugfix-epic-workflow.md)
- **Roles & Authorization (P4.3):** [`roles-authorization-team-governance.md`](roles-authorization-team-governance.md)
- **P4 entry point:** [P4 Governance System Guide](../../docs/team-collaboration/P4-governance-system-guide.md)
- **Governing guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md` §13, §18

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.4.0 | 2026-09-02 | **Rework limit reached by citation (E43.3, P12-M43; closes `P12-GH-1`).** The Review Decision row's "Reject (rework)" meaning now names the **rework limit** and points to the one normative statement (PROJECT-SYSTEM-GUIDELINES.md §11.6 "The Rework Limit" — a maximum of 3 attempts; a written extension grants exactly one further attempt, not a reset to three). This surface cites the statement; it does not restate it. Same strictness — no guard weakened. Backed by `tests/test_rework_limit_single_statement.py`. |
| 1.3.0 | 2026-09-02 | **Acceptance distinguishable from absence (E43.2, P12-M43).** Every "accept by silence" statement reconciled to the amended PSG §11.6: HQ Chat accepts a clean Phase delivery by an **in-chat acknowledgment that names the party that reviewed and accepted** (role + session identity); **silence accepts nothing**. Amended: the Review-and-accept responsibility, the supporting-artifacts table's Review Decision row, the artifact-flow note, the Review Decision worked example, and the Oversee step of the session lifecycle. HQ-authored deliveries remain governed by §11.6.1 (CFO diff review; not touched). Same strictness — no guard weakened. Backed by `tests/test_acceptance_distinguishable_from_absence.py`. |
| 1.2.0 | 2026-09-02 | **Merge-authorization guard relabelled as a backstop (E43.1, P12-M43).** The guard's pushback strings survive, relabelled: at the Phase→Milestone and Milestone→Epic gates the parent performs the merge of a child's branch (PSG §11.6), so a child never holds merge authorization — the guard is now a labelled backstop, not the primary guard (unavailable is not impossible; a backstop that fires is evidence); HQ itself has no parent and therefore never merges on authorization alone. Guard clauses (refusal, mode-is-not-authority, §11.6.1) are unchanged — same strictness. Also corrected the supporting-artifact list's Merge Authorization description to the parent's record of the merge it performed. Backed by `tests/test_merge_authorization_parent_performs.py`; the existing `tests/test_merge_authorization_routing_guard.py` still passes. |
| 1.1.0 | 2026-08-17 | **Merge-authorization routing guard added** (E40.5, P11-M40; closes `P9-GH-1`). New §**Merge-Authorization Routing (P9-GH-1)** under §Governance Authority Chain. HQ has **no parent chat**, so the routing is not "confirm upward": PSG **§11.6.1** applies — default-accept MUST NOT be applied to HQ-authored deliveries, the **CFO is the designated diff reviewer**, and HQ MUST NOT merge its own delivery on authorization alone. The guard was previously present in **one** starter surface only (`governance/templates/epic-execution-chat-starter.md`, lines 70-75 as measured 2026-08-16); a sweep on 2026-08-17 established **eight** starter-shaped surfaces, and it now reaches all eight, level-aware per level. Backed by `tests/test_merge_authorization_routing_guard.py`, falsified 2026-08-17. |
| 1.0.0 | 2026-08-05 | **Versioning convention adopted** (HQ Ruling 2026-08-04, P10-GH-8; applied by E37.1, P11-M37). This document previously carried neither a `version` field nor a `## Changelog` section. **This is its first recorded row, and no prior history is reconstructed** — for changes before this date, see `git log -- governance/systems/hq-execution-chat-starter.md`. |
