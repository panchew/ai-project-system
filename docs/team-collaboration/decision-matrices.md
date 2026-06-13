# Decision Matrices

**Reference tables for "who decides?" — answer in under 30 seconds.**

---

## Matrix 1: Decision Authority by Type

| Decision Type | CFO | HQ Agent | Phase Lead | Milestone Agent | Epic Agent | Reviewer | Contributor |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Phase scope** | ✓ decides | — | ✗ proposes only | — | — | — | — |
| **Phase authorization** | ✓ decides | — | — | — | — | — | — |
| **Milestone planning** | — | — | ✓ or delegates | ✓ executes | — | — | — |
| **Epic spec** | — | — | — | ✓ decides | ✓ provides input | — | — |
| **Epic acceptance** | — | — | — | ✓ decides | — | ✓ provides input | — |
| **Epic implementation** | — | — | — | — | ✓ decides | ✓ provides input | ✓ executes |
| **Production deployment** | ✓ decides | — | — | — | — | — | — |
| **Bugfix Epic creation** | — | ✓ decides | — | — | — | — | — |
| **Escalation resolution** | ✓ final authority | ✓ Phase level | ✓ Milestone level | ✓ Epic level | ✓ reports | ✓ reports | ✓ reports |

---

## Matrix 2: Decision Criteria

| Decision Type | Who Decides | Criteria for Approval | Criteria for Rejection |
|---|---|---|---|
| **Phase Scope** | CFO | Goals are clear, team available, budget allocated | Scope unclear, team unavailable, budget not confirmed |
| **Milestone Planning** | Phase Lead / Milestone Agent | Epics derived from Phase spec, dependencies identified | Epics missing, spec gaps unresolved |
| **Epic Acceptance** | Milestone Agent (with Reviewer input) | All DoD items met, PR open, no blockers, Reviewer approved | DoD incomplete, tests failing, scope violation |
| **Production Deployment** | CFO | All Phases merged to staging, rollback plan documented, risk assessed | Risks unmitigated, rollback plan absent, CFO not satisfied |
| **Escalation Decision** | Parent role in authority chain | Blocker is real, lower levels cannot resolve, decision clearly stated | Escalation is premature; lower level should decide |

---

## Matrix 3: Artifact Issuers

| Artifact | Issued By | Consumed By | Authority Required |
|---|---|---|---|
| Phase Spec | HQ Agent or Phase Lead | Phase Lead, Milestone Agents | CFO Phase Authorization |
| Milestone Spec | Milestone Agent | Epic Agents, Contributors | Phase Lead delegation |
| Epic Spec | Milestone Agent | Epic Agent, Contributors | Milestone Agent authority |
| Epic Execution Chat Starter | Milestone Agent | Epic Agent | Milestone Agent issues delivery authorization |
| Completion Notice | Epic Agent / Contributor | Milestone Agent (review) | Any; signals readiness only |
| Review Decision (Accept) | Milestone Agent | Epic Agent (authorizes merge) | Milestone Agent authority |
| Review Decision (Reject) | Milestone Agent | Epic Agent (triggers rework) | Milestone Agent authority |
| Delivery Notice | Epic Agent | Milestone Agent (acknowledgement) | Post-merge; records final state |
| Deployment Authorization | CFO | HQ Agent, Release Agent | CFO only |
| Bugfix Epic Approval | HQ Agent | Developer / Epic Agent | HQ Agent (expedited) |

---

## Matrix 4: Branch Merge Authority

| Target Branch | Who Merges | Authorization Required |
|---|---|---|
| `epic/E#.#` → `milestone/M#` | Epic Agent / Contributor | Review Decision (Accept) from Milestone Agent |
| `milestone/M#` → `phase/P#` | Milestone Agent | Phase approval (Phase Lead or HQ Agent) |
| `phase/P#` → `develop` | Phase Agent / Release Agent | CFO authorization |
| `develop` → `master` | CFO-authorized role | CFO Deployment Authorization |
| `bugfix/B#.#` → `hotfix` | Epic Agent (bugfix) | HQ Agent Review Decision (Accept) |
| `hotfix` → `master` | CFO-authorized role | CFO Deployment Authorization |

**Rule:** No branch merges to a parent branch without explicit authorization from the governing role at that level.

---

## Matrix 5: Escalation Path

| Escalation Source | Escalates To | When | Expected Response Time |
|---|---|---|---|
| Contributor | Epic Agent / Milestone Agent | Spec ambiguous, blocked on dependency | 4 hours |
| Epic Agent | Milestone Agent | Spec conflict, 3 retries exhausted | 4 hours |
| Milestone Agent | Phase Lead / HQ Agent | Scope unclear, Epic dispute unresolved | 8 hours |
| Phase Lead / HQ Agent | CFO | Strategic decision needed, production deployment | 2 business days (URGENT: same day) |

---

## Matrix 6: Execution Mode Comparison

| Aspect | Manual Mode | Agentic Mode |
|---|---|---|
| **Artifact routing** | Human copies artifacts between chats | Daemon routes automatically |
| **Review trigger** | Human pastes Completion Notice into parent chat | Daemon detects file, routes to parent |
| **Infrastructure needed** | None — just AI chat and copy-paste | Docker, daemon, `.ai-project/queue/` |
| **Audit trail** | Artifacts committed manually by team | Artifacts committed by agents |
| **Best for** | Teams new to the system (weeks 1–4) | Mature teams (weeks 9+) |
| **CFO time commitment** | Same — CFO gate unchanged | Same — CFO gate unchanged |
| **Authority model** | Identical | Identical |

---

## Quick-Lookup: "Who approves this?"

| You want to... | Ask... |
|---|---|
| Start a new Phase | CFO |
| Start a new Milestone | Phase Lead or Milestone Agent |
| Merge your Epic PR | Milestone Agent (after Review Decision Accept) |
| Deploy to production | CFO |
| Create a Bugfix Epic | HQ Agent |
| Resolve a spec conflict | Milestone Agent; escalate to Phase Lead if unresolved |
| Override a rejected Epic decision | Phase Lead; escalate to CFO if contested |
| Add a new team member | CFO |

---

## Source

All role authorities in these matrices derive from [Governance: Roles & Authorization](../../governance/systems/roles-authorization-team-governance.md). If any matrix entry conflicts with that document, the governance document takes precedence.
