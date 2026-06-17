# Example Walkthrough

**A full Epic cycle, traced through real artifacts.**

This walkthrough follows the Taskflow example project through one complete Epic cycle — from Phase authorization to Delivery Notice. You will see every artifact, every decision, and every handoff in sequence.

All artifact files referenced here exist in `examples/team-project-example/` and can be opened in your editor to read the full content.

---

## The Taskflow Project

The Taskflow example is a fictional team project that demonstrates the AI Project System in a team setting. The project structure:

- **Phase P1 — Task Management App** (`examples/team-project-example/docs/phases/P1__Task_Management_App/P1__phase-spec.md`)
  - **Milestone M1 — Core Backend** (`M1__milestone-spec.md`) — 3 Epics
  - **Milestone M2 — Frontend** (`M2__milestone-spec.md`) — 3 Epics
  - **Milestone M3 — Polish and Deploy** (`M3__milestone-spec.md`) — includes Bugfix B1.1

**The team:**

| Role | Person | Authority |
|---|---|---|
| CFO | Morgan Chen | Phase authorization, production deployment |
| Phase Lead | Alex Rivera | Milestone planning, Review Decisions |
| Developer 1 | Jamie Park | Implements E1.1, E1.2 |
| Developer 2 | Sam Torres | Implements E1.3, E2.2 |
| Reviewer | Casey Kim | Code review gate |

---

## Part 1: Phase Authorization

### Step 1 — CFO Authorizes Phase P1

Morgan Chen reads the Phase P1 spec at:

```
examples/team-project-example/docs/phases/P1__Task_Management_App/P1__phase-spec.md
```

The spec defines the project goals (a task management web app), three milestones, and the target timeline. Morgan confirms scope, team, and budget are acceptable, then issues a Phase Authorization in HQ Chat:

> "Phase P1 — Task Management App is authorized. Alex Rivera is confirmed as Phase Lead. Budget approved. Target completion: 2026-06-30."

**Decision recorded:** Phase Authorization (in HQ Chat history)

**Who decides:** CFO (Morgan Chen)

---

### Step 2 — Phase Lead Plans Milestone M1

Alex Rivera reviews the Phase P1 spec and creates the Milestone M1 spec at:

```
examples/team-project-example/docs/phases/P1__Task_Management_App/M1__Core_Backend/M1__milestone-spec.md
```

Alex reviews the three Epics planned for M1:
- **E1.3 — Database Schema** → Sam Torres (starts first; unblocks E1.1 and E1.2)
- **E1.1 — User Authentication** → Jamie Park (starts after E1.3 merges)
- **E1.2 — Task CRUD API** → Jamie Park (starts in parallel with E1.1)

Alex issues Epic Delivery Authorizations for all three Epics.

**Who decides:** Phase Lead (Alex Rivera)

---

## Part 2: Epic E1.1 — The Happy Path

This section traces E1.1 (User Authentication) from spec to Delivery Notice.

### Step 3 — Developer Reads Spec and Creates Branch

Jamie Park reads the E1.1 spec:

```
examples/team-project-example/docs/phases/P1__Task_Management_App/M1__Core_Backend/E1.1__spec__user-authentication.md
```

The spec requires: JWT authentication, four endpoints (register, login, refresh, logout), a `require_auth` middleware for use by E1.2, and ≥80% test coverage.

Jamie creates the branch:

```bash
git checkout milestone/M1
git pull origin milestone/M1
git checkout -b epic/E1.1
```

**Who acts:** Contributor (Jamie Park)

---

### Step 4 — Implementation

Jamie implements the four endpoints, the middleware, and the Pydantic schemas. After running tests (18/18 passing, 84% coverage), Jamie opens PR #12 targeting `milestone/M1`.

PR title: `feat: JWT user authentication (E1.1)`

Casey Kim (Reviewer) reviews PR #12. The implementation is correct, coverage exceeds 80%, and the `require_auth` middleware is clean and reusable. Casey approves.

**Who acts:** Contributor (Jamie Park), Reviewer (Casey Kim)

---

### Step 5 — Completion Notice

Jamie produces a Completion Notice and commits it to the `epic/E1.1` branch:

```
examples/team-project-example/.ai-project/artifacts/completion-notices/
2026-06-02T10-00-00Z__P1-M1-E1.1__completion-notice.md
```

Key fields from this artifact:
- `status: ready_for_review`
- `qa_status: passed`
- `blockers: []`
- `pr_details.number: 12`

**Manual mode:** Jamie copies the Completion Notice and pastes it into the Milestone M1 Chat.

**Agentic mode:** The daemon detects the new file in `.ai-project/artifacts/completion-notices/` and routes it to the Milestone Agent automatically.

**Who acts:** Contributor (Jamie Park)

---

### Step 6 — Review Decision (Accept)

Alex Rivera (Phase Lead, acting as Milestone Agent) reviews the Completion Notice. All DoD items are met, coverage is 84% (above the 80% requirement), and the Reviewer approved. Alex issues a Review Decision:

```
examples/team-project-example/.ai-project/artifacts/review-decisions/
2026-06-02T16-00-00Z__P1-M1-E1.1__review-decision.md
```

Key fields:
- `decision: accept`
- `authorization.action: merge`
- `authorization.merge_instruction: "Merge PR #12 to milestone/M1. Use squash-and-merge strategy. Delete the epic/E1.1 branch after merge."`

**Manual mode:** Alex copies the Review Decision and pastes it back into the Epic E1.1 Chat.

**Agentic mode:** The daemon detects the new Review Decision file and routes it back to the Epic Agent.

**Who decides:** Phase Lead / Milestone Agent (Alex Rivera)

---

### Step 7 — Merge and Delivery Notice

Jamie receives the Review Decision (Accept) and:
1. Confirms PR #12 CI checks are green
2. Merges PR #12 to `milestone/M1` using squash-and-merge
3. Deletes the `epic/E1.1` branch
4. Produces a Delivery Notice and commits it:

```
examples/team-project-example/.ai-project/artifacts/delivery-notices/
2026-06-03T10-00-00Z__P1-M1-E1.1__delivery-notice.md
```

Key fields:
- `status: delivered`
- `merge_details.merge_commit: "a3f7c2d9e1b4680f"`
- `merge_details.target_branch: milestone/M1`
- `duration.elapsed_days: 2`

The Epic E1.1 Chat closes. Alex Rivera acknowledges the Delivery Notice in the Milestone M1 Chat and moves to E1.2.

**Total time for E1.1:** 2 days (start to merge)

---

## Part 3: Epic E1.2 — The Rejection and Rework Path

E1.2 (Task CRUD API) ran in parallel with E1.1. This section shows what happens when a Completion Notice is rejected.

### Step 8 — E1.2 First Submission (Rejected)

Jamie Park completes the E1.2 implementation (five CRUD endpoints for tasks) and submits a Completion Notice:

```
examples/team-project-example/.ai-project/artifacts/completion-notices/
2026-06-05T14-30-00Z__P1-M1-E1.2__completion-notice.md
```

The Completion Notice itself acknowledges that test coverage is 68% — below the 80% minimum in the E1.2 spec. Casey Kim (Reviewer) gave a conditional approval, noting the coverage gap.

---

### Step 9 — Review Decision (Reject)

Alex Rivera reviews the Completion Notice and issues a rejection:

```
examples/team-project-example/.ai-project/artifacts/review-decisions/
2026-06-05T17-00-00Z__P1-M1-E1.2__review-decision.md
```

Key fields:
- `decision: reject`
- `authorization.action: rework`
- `feedback: "Test coverage at 68% is below the required 80%... Missing tests: PUT /tasks/{id} with invalid priority, pagination boundary conditions..."`

The rejection specifies exactly which tests are missing. Jamie does not need to change the implementation — only extend the test suite.

**Manual mode:** Alex copies the Review Decision and pastes it back into the Epic E1.2 Chat.

**Agentic mode:** The daemon detects the rejection and routes it to the Epic Agent.

---

### Step 10 — Rework and Resubmission

Jamie adds the four missing test cases, runs `pytest --cov=src/tasks`, and confirms coverage is now 83%. Jamie produces a new Completion Notice (v1.1):

```
examples/team-project-example/.ai-project/artifacts/completion-notices/
2026-06-07T09-00-00Z__P1-M1-E1.2__completion-notice.md
```

This second Completion Notice shows `qa_status: passed` and coverage at 83%.

---

### Step 11 — Review Decision (Accept, Second Attempt)

Alex Rivera reviews the reworked Completion Notice and issues an acceptance:

```
examples/team-project-example/.ai-project/artifacts/review-decisions/
2026-06-07T14-00-00Z__P1-M1-E1.2__review-decision.md
```

Jamie merges PR #18 and produces the E1.2 Delivery Notice:

```
examples/team-project-example/.ai-project/artifacts/delivery-notices/
2026-06-08T10-00-00Z__P1-M1-E1.2__delivery-notice.md
```

**Total time for E1.2 (including rework):** 4 days

---

## Part 4: Bugfix Epic — The Expedited Path

During Milestone M3, a session token bug is discovered in production. This demonstrates the Bugfix Epic workflow.

The bugfix spec is at:

```
examples/team-project-example/docs/phases/P1__Task_Management_App/M3__Polish_and_Deploy/B1.1__spec__auth-session-bugfix.md
```

**Key differences from a standard Epic:**
- Epic ID prefix is `B` (e.g., `B1.1`), not `E`
- Spec is minimal (problem, impact, fix approach, DoD only)
- HQ Agent approves directly — no Milestone planning ceremony
- Review SLA is 4 hours (not 24 hours)
- Branch strategy: `bugfix/B1.1` → `hotfix` → `master` (not milestone branch)
- Production deployment still requires CFO (Morgan Chen) authorization

For the full Bugfix Epic protocol, see [Governance: Bugfix Epic Workflow](../../governance/systems/bugfix-epic-workflow.md).

---

## Part 5: Execution Mode Comparison

The same Taskflow cycle works in both execution modes. The authority model, artifact formats, and decision chain are identical. Only the artifact routing mechanism changes.

### Manual Mode (Copy-Paste)

```
Jamie (Developer) produces Completion Notice
  ↓
Jamie copies Completion Notice text
  ↓
Alex (Phase Lead) opens Milestone M1 Chat
  ↓
Jamie pastes Completion Notice into Milestone M1 Chat
  ↓
Alex (or Milestone Agent) reviews and produces Review Decision
  ↓
Alex copies Review Decision text
  ↓
Alex pastes Review Decision into Epic E1.1 Chat
  ↓
Jamie reads Review Decision and merges (if Accept)
```

**Steps per Epic cycle (manual):** ~5 copy-paste operations
**Infrastructure needed:** None — just an AI chat and access to the repository

### Agentic Mode (Daemon Routing)

```
Jamie (Developer) produces Completion Notice
  ↓
Jamie commits Completion Notice to .ai-project/artifacts/completion-notices/
  ↓
ai-project-daemon detects new file
  ↓
Daemon routes Completion Notice to Milestone Agent queue
  ↓
Milestone Agent processes and produces Review Decision
  ↓
Daemon detects new Review Decision file
  ↓
Daemon routes Review Decision to Epic Agent
  ↓
Epic Agent reads Review Decision and merges (if Accept)
```

**Steps per Epic cycle (agentic):** 1 commit (daemon handles routing)
**Infrastructure needed:** Docker, `ai-project-daemon` running, `.ai-project/queue/` configured

**Starting the daemon (from your project root):**

```bash
governance/bin/ai-project-daemon --project-root . start
```

---

## Summary: What You Just Saw

| Step | Action | Artifact | Who |
|---|---|---|---|
| 1 | CFO authorizes Phase | Phase Authorization (in HQ Chat) | CFO |
| 2 | Phase Lead plans Milestone | Milestone Spec | Phase Lead |
| 3 | Developer reads spec and branches | — | Contributor |
| 4 | Developer implements and opens PR | Pull Request | Contributor + Reviewer |
| 5 | Developer submits Completion Notice | `...E1.1__completion-notice.md` | Contributor |
| 6 | Phase Lead accepts (Review Decision) | `...E1.1__review-decision.md` | Milestone Agent |
| 7 | Developer merges, issues Delivery Notice | `...E1.1__delivery-notice.md` | Contributor |
| 8–11 | E1.2 rejected and reworked | Multiple artifacts | Milestone Agent, Contributor |

For your first real Epic, follow the same sequence. Use the Taskflow artifacts as formatting references.

---

## Cross-References

- [Contributor Guide](contributor-guide.md) — full Contributor workflow
- [Reviewer Guide](reviewer-guide.md) — code review checklist
- [Phase Lead Guide](phase-lead-guide.md) — Milestone planning workflow
- [Decision Matrices](decision-matrices.md) — who decides what
- [FAQ](faq.md) — common questions
- [Governance: Artifact Communication Protocol](../../governance/systems/artifact-communication-protocol.md) — canonical artifact schemas
- [Governance: Bugfix Epic Workflow](../../governance/systems/bugfix-epic-workflow.md) — expedited bugfix path
- [Taskflow Example Project](../../examples/team-project-example/) — all source files for this walkthrough
