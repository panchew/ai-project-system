# Taskflow — One Full Epic from Start to Finish

This walkthrough traces Epic E1.1 (User Authentication) through the complete AI Project System lifecycle: from Phase approval to Delivery Notice. It also shows how E1.2 ran in parallel during Milestone M1.

Use this as a step-by-step reference when executing your first Epic on any project.

---

## The Cast

| Role | Person | Authority in this walkthrough |
|------|--------|-------------------------------|
| CFO | Morgan Chen | Authorizes Phase P1 |
| Phase Lead | Alex Rivera | Runs Milestone M1, issues Review Decisions |
| Developer 1 | Jamie Park | Implements E1.1 and E1.2 |
| Developer 2 | Sam Torres | Implements E1.3 (starts first) |
| Reviewer | Casey Kim | Reviews all PRs |

---

## Phase P1 Kickoff

### Step 1 — CFO Authorizes Phase P1

**Who decides:** CFO (Morgan Chen)

Morgan Chen reviews the Phase P1 spec (`docs/phases/P1__Task_Management_App/P1__phase-spec.md`) and confirms the scope, team, and timeline are acceptable.

**Action:** CFO issues Phase Authorization in HQ Chat:

> "Phase P1 — Core Application is authorized. Alex Rivera is confirmed as Phase Lead. Budget approved. Target completion: 2026-06-30."

No artifact file is required for this step (it is recorded in HQ Chat history), but a Phase Authorization artifact may be produced if the team wants a formal record.

---

### Step 2 — Phase Lead Opens Milestone M1

**Who decides:** Phase Lead (Alex Rivera)

Alex Rivera creates the Milestone M1 spec (`M1__milestone-spec.md`) and opens the Milestone M1 Chat. Alex reviews the three planned Epics (E1.1, E1.2, E1.3) and assigns them to developers.

**Epic Assignments:**
- E1.3 (Database Schema) → Sam Torres (Developer 2) — starts immediately, unblocks others
- E1.1 (User Authentication) → Jamie Park (Developer 1) — starts after E1.3 merges
- E1.2 (Task CRUD API) → Jamie Park (Developer 1) — starts in parallel with E1.1

**Decision:** Phase Lead determines execution order: E1.3 first, then E1.1 and E1.2 in parallel.

---

## E1.3 Executes First (Unblocks Everything)

### Step 3 — Developer 2 Creates Branch and Implements E1.3

**Who acts:** Developer 2 (Sam Torres)

Sam Torres creates `epic/E1.3` from `milestone/M1`, reads the spec, and implements the database schema:

```bash
git checkout milestone/M1
git pull
git checkout -b epic/E1.3 milestone/M1
```

Sam writes `src/db/models.py`, creates the Alembic migration, and writes the seed script.

**PR opened:** PR #10 → `milestone/M1`

---

### Step 4 — Reviewer Reviews E1.3 PR

**Who decides:** Reviewer (Casey Kim)

Casey Kim reviews PR #10. The schema is clean, migration applies correctly, seed script is idempotent. Casey approves the PR on GitHub.

---

### Step 5 — Phase Lead Accepts E1.3 and Authorizes Merge

**Who decides:** Phase Lead (Alex Rivera)

Alex reads the E1.3 Completion Notice (produced by Sam), checks the Reviewer approval, and issues a Review Decision (Accept). Sam merges PR #10.

**Milestone M1 is now unblocked.** E1.1 and E1.2 start in parallel.

---

## E1.1 and E1.2 Execute in Parallel

> This is the parallel execution section. Both E1.1 (Jamie Park) and E1.2 (Jamie Park) are worked on simultaneously across different branches. Both PRs are open at the same time.

### Step 6 — Developer 1 Creates E1.1 Branch and Implements Auth

**Who acts:** Developer 1 (Jamie Park)

Jamie creates `epic/E1.1` from `milestone/M1` (which now has the schema merged):

```bash
git checkout milestone/M1
git pull
git checkout -b epic/E1.1 milestone/M1
```

Jamie implements the auth endpoints, middleware, and schemas. Tests written with 84% coverage.

**PR opened:** PR #12 → `milestone/M1`
**Date:** 2026-06-01 (started), 2026-06-02 (PR opened)

> **Simultaneously:** Jamie also has `epic/E1.2` open with the Task CRUD API in progress.

---

### Step 7 — Reviewer Reviews E1.1 PR

**Who decides:** Reviewer (Casey Kim)

Casey Kim reviews PR #12. The auth implementation is correct, tests are comprehensive, middleware is clean and reusable. Casey approves on GitHub with no change requests.

---

### Step 8 — Developer 1 Produces E1.1 Completion Notice

**Who acts:** Developer 1 (Jamie Park)

With all Definition of Done items met and the Reviewer approval in hand, Jamie produces the Completion Notice and commits it to `epic/E1.1`:

**File created:**
```
examples/team-project-example/.ai-project/artifacts/completion-notices/
  2026-06-02T10-00-00Z__P1-M1-E1.1__completion-notice.md
```

**Key fields in the Completion Notice:**
- `status: ready_for_review`
- `qa_status: passed` (18/18 tests, 84% coverage)
- `pr_details.number: 12`

---

### Step 9 — Phase Lead Reviews E1.1 Completion Notice

**Who decides:** Phase Lead (Alex Rivera)

Alex reads the Completion Notice and verifies:
- ✓ All deliverables listed
- ✓ Reviewer approval noted
- ✓ Coverage 84% > 80% required
- ✓ PR #12 is open and CI is green

Alex issues a Review Decision (Accept):

**File created:**
```
examples/team-project-example/.ai-project/artifacts/review-decisions/
  2026-06-02T16-00-00Z__P1-M1-E1.1__review-decision.md
```

**Key fields:**
- `decision: accept`
- `authorization.action: merge`
- `authorization.merge_instruction: "Merge PR #12 to milestone/M1. Squash-and-merge."`

**Decision point:** Accept/reject is made by Phase Lead (Alex Rivera), not by the Developer or Reviewer.

---

### Step 10 — Developer 1 Merges E1.1 and Produces Delivery Notice

**Who acts:** Developer 1 (Jamie Park), authorized by Review Decision

With the Accept decision in hand, Jamie:
1. Confirms PR #12 CI is green
2. Merges PR #12 to `milestone/M1` using squash-and-merge
3. Deletes the `epic/E1.1` branch
4. Produces the Delivery Notice:

**File created:**
```
examples/team-project-example/.ai-project/artifacts/delivery-notices/
  2026-06-03T10-00-00Z__P1-M1-E1.1__delivery-notice.md
```

**Key fields:**
- `status: delivered`
- `merge_details.merge_commit: a3f7c2d9e1b4680f`
- `merge_details.target_branch: milestone/M1`

**Epic E1.1 is now closed.**

---

## E1.2 — A Rejection and Rework Cycle

> While E1.1 was being reviewed and merged, E1.2 continued in parallel. E1.2 illustrates what happens when a Completion Notice is rejected.

### Step 11 — Developer 1 Submits E1.2 Completion Notice (v1.0)

**Who acts:** Developer 1 (Jamie Park)

Jamie submits the first Completion Notice for E1.2 on 2026-06-05:

```
.ai-project/artifacts/completion-notices/
  2026-06-05T14-30-00Z__P1-M1-E1.2__completion-notice.md
```

Jamie notes in the notice that test coverage is 68% — below the required 80%.

---

### Step 12 — Phase Lead Rejects E1.2 (Coverage Below Threshold)

**Who decides:** Phase Lead (Alex Rivera)

Alex reviews the Completion Notice. The spec requires 80% coverage; 68% does not meet the bar. Alex issues a Review Decision (Reject):

```
.ai-project/artifacts/review-decisions/
  2026-06-05T17-00-00Z__P1-M1-E1.2__review-decision.md
```

**Key fields:**
- `decision: reject`
- `feedback: "Test coverage at 68% is below the required 80%..."`
- `authorization.action: rework`

**Decision point:** Reject decision is made by Phase Lead (Alex Rivera). The Developer does not choose whether to accept or reject their own work.

---

### Step 13 — Developer 1 Reworks E1.2 and Resubmits

**Who acts:** Developer 1 (Jamie Park)

Jamie adds 9 new test cases (covering the specific gaps called out in the rejection) and discovers a bug in the archived-task count during test authoring. Coverage reaches 83%.

Jamie submits Completion Notice v1.1:

```
.ai-project/artifacts/completion-notices/
  2026-06-07T09-00-00Z__P1-M1-E1.2__completion-notice.md  (artifact_version: 1.1)
```

---

### Step 14 — Phase Lead Accepts E1.2 (Second Review)

**Who decides:** Phase Lead (Alex Rivera)

Alex reviews the v1.1 Completion Notice. All issues resolved. Coverage 83%. Alex issues Accept:

```
.ai-project/artifacts/review-decisions/
  2026-06-07T14-00-00Z__P1-M1-E1.2__review-decision.md
```

Jamie merges PR #17 and produces the Delivery Notice:

```
.ai-project/artifacts/delivery-notices/
  2026-06-08T10-00-00Z__P1-M1-E1.2__delivery-notice.md
```

**Epic E1.2 is now closed.**

---

## Timeline: Parallel Execution in Milestone M1

```
Date        E1.3 (Sam Torres)    E1.1 (Jamie Park)    E1.2 (Jamie Park)
──────────  ───────────────────  ───────────────────  ───────────────────
2026-06-01  [Implements] ──────  [Starts] ────────── [Starts] ──────────
2026-06-02  [PR #10] ─────────  [PR #12, CN v1.0] ─ [in progress] ─────
2026-06-02  [Accepted/Merged] ─  [Accepted] ─────── [in progress] ─────
2026-06-03  [E1.3 DONE] ──────  [Merged, DN] ──────  [in progress] ─────
2026-06-05  ──────────────────  [E1.1 DONE] ────────  [CN v1.0, Rejected]
2026-06-07  ──────────────────  ──────────────────── [CN v1.1, Accepted]
2026-06-08  ──────────────────  ──────────────────── [Merged, DN, DONE]
```

E1.1 and E1.2 ran concurrently from 2026-06-01 through 2026-06-03 (when E1.1 merged). E1.2 continued alone from 2026-06-03 to 2026-06-08.

---

## B1.1 — A Bugfix Epic (Expedited Path)

### Step 15 — Bug Discovered in Staging

**Who reports:** Reviewer (Casey Kim)

During M2 testing (after M1 merged to staging), Casey Kim notices that users with multiple browser tabs open intermittently get logged out. Root cause: JWT refresh race condition in `POST /auth/refresh`.

Casey reports to Phase Lead (Alex Rivera) in HQ Chat:

> "🔴 Potential Bugfix — Auth Session Expires on Concurrent Requests. Severity: Critical. Reproduced consistently. Scope: 1-day fix (SELECT FOR UPDATE)."

---

### Step 16 — HQ Approves Bugfix Epic B1.1

**Who decides:** HQ Agent (on behalf of CFO Morgan Chen)

The HQ Agent evaluates: issue is unplanned, time-sensitive (blocks M2 staging tests), root cause is known, fix is localized. Qualifies for Bugfix Epic workflow.

HQ Agent approves the Bugfix Epic:
> "✓ Bugfix Epic Approved. Epic ID: B1.1. Severity: Critical. Developer: Jamie Park. SLA: Review within 4 hours of Completion Notice."

The minimal Bugfix Epic spec is committed:
```
docs/phases/P1__Task_Management_App/M3__Polish_and_Deploy/
  B1.1__spec__auth-session-bugfix.md
```

---

### Step 17 — Developer 1 Implements B1.1 on Expedited Path

**Who acts:** Developer 1 (Jamie Park)

Key difference from standard Epics: B1.1 uses `bugfix/B1.1` branch (not `epic/B1.1`), merges to `hotfix` or `master` (not milestone), and the parent review comes from HQ Chat (not Milestone Chat), with a 4-hour SLA instead of 24 hours.

Jamie applies the `SELECT FOR UPDATE` fix and adds a concurrent refresh test. PR opened. Completion Notice produced. HQ Agent reviews and accepts within 2 hours.

---

### Step 18 — CFO Authorizes Production Deployment (M3 Only)

**Who decides:** CFO (Morgan Chen)

After all M3 Epics (E3.1, E3.2, B1.1) are merged, Phase Lead Alex Rivera issues the Phase Completion Notice. CFO Morgan Chen reviews and issues Production Deployment Authorization — the only person with this authority.

No deployment proceeds without this authorization.

---

## Summary: Key Decision Points

| Step | Decision | Who Decides | Authority |
|------|----------|------------|-----------|
| Phase P1 start | Authorize Phase | CFO (Morgan Chen) | Highest authority |
| Epic assignment | Who works on what | Phase Lead (Alex Rivera) | Milestone planning |
| E1.3 Review | Accept Completion Notice | Phase Lead (Alex Rivera) | Epic acceptance |
| E1.1 Review | Accept Completion Notice | Phase Lead (Alex Rivera) | Epic acceptance |
| E1.2 First Review | Reject Completion Notice | Phase Lead (Alex Rivera) | Epic acceptance |
| E1.2 Second Review | Accept Completion Notice | Phase Lead (Alex Rivera) | Epic acceptance |
| B1.1 creation | Approve Bugfix Epic | HQ Agent | Bugfix authorization |
| Production Deploy | Authorize deployment | CFO (Morgan Chen) | Deployment gate |

**Key principle:** Developers implement. Reviewers gate quality. Phase Lead accepts or rejects. CFO gates production.

---

## Artifacts Produced (with File Paths)

### Completion Notices
- [`2026-06-02T10-00-00Z__P1-M1-E1.1__completion-notice.md`](.ai-project/artifacts/completion-notices/2026-06-02T10-00-00Z__P1-M1-E1.1__completion-notice.md) — E1.1, accepted
- [`2026-06-05T14-30-00Z__P1-M1-E1.2__completion-notice.md`](.ai-project/artifacts/completion-notices/2026-06-05T14-30-00Z__P1-M1-E1.2__completion-notice.md) — E1.2 v1.0, rejected
- [`2026-06-07T09-00-00Z__P1-M1-E1.2__completion-notice.md`](.ai-project/artifacts/completion-notices/2026-06-07T09-00-00Z__P1-M1-E1.2__completion-notice.md) — E1.2 v1.1, accepted
- [`2026-06-10T09-00-00Z__P1-M2-E2.1__completion-notice.md`](.ai-project/artifacts/completion-notices/2026-06-10T09-00-00Z__P1-M2-E2.1__completion-notice.md) — E2.1, accepted

### Review Decisions
- [`2026-06-02T16-00-00Z__P1-M1-E1.1__review-decision.md`](.ai-project/artifacts/review-decisions/2026-06-02T16-00-00Z__P1-M1-E1.1__review-decision.md) — **ACCEPT**
- [`2026-06-05T17-00-00Z__P1-M1-E1.2__review-decision.md`](.ai-project/artifacts/review-decisions/2026-06-05T17-00-00Z__P1-M1-E1.2__review-decision.md) — **REJECT**
- [`2026-06-07T14-00-00Z__P1-M1-E1.2__review-decision.md`](.ai-project/artifacts/review-decisions/2026-06-07T14-00-00Z__P1-M1-E1.2__review-decision.md) — **ACCEPT** (after rework)

### Delivery Notices
- [`2026-06-03T10-00-00Z__P1-M1-E1.1__delivery-notice.md`](.ai-project/artifacts/delivery-notices/2026-06-03T10-00-00Z__P1-M1-E1.1__delivery-notice.md)
- [`2026-06-08T10-00-00Z__P1-M1-E1.2__delivery-notice.md`](.ai-project/artifacts/delivery-notices/2026-06-08T10-00-00Z__P1-M1-E1.2__delivery-notice.md)
- [`2026-06-10T11-00-00Z__P1-M2-E2.1__delivery-notice.md`](.ai-project/artifacts/delivery-notices/2026-06-10T11-00-00Z__P1-M2-E2.1__delivery-notice.md)
