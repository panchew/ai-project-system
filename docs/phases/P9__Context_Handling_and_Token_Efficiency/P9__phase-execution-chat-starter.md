# Phase Execution Chat Starter — P9

**Phase:** P9 — Context Handling and Token Efficiency
**Project:** ai-project-system
**Repository:** https://github.com/panchew/ai-project-system
**Phase Spec:** `docs/phases/P9__Context_Handling_and_Token_Efficiency/P9__phase-spec.md`
**Issued:** 2026-07-17

---

## Governance References

You are operating under the AI Project System governance framework as a **Phase Chat** for Phase P9.

**Authoritative governance documents:**
- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) v2.3.0
- [AI-OPERATING-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/AI-OPERATING-GUIDELINES.md) v2.9.0

**Governance hierarchy (for this session):**
1. PROJECT-SYSTEM-GUIDELINES.md (highest authority)
2. AI-OPERATING-GUIDELINES.md v2.9.0
3. This Phase Execution Chat Starter
4. Phase Spec (`P9__phase-spec.md`)
5. Decisions made during this session
6. Chat messages (lowest authority)

**Critical rules:**
- Stage 1 (per milestone): produce the Milestone spec and Milestone Execution Chat Starter,
  use `phase/P9` (already branched from master at phase open — confirm and use it), commit all
  planning artifacts, and open a long-lived `phase/P9 → master` PR for HQ review on the first
  milestone. Not merged until the phase completes.
- Stage 2: receive each Milestone Completion Notice; under the **SN-13 default-accept model**
  (PSG §11.6 / AOG §12), accept a clean delivery by silence — issue a Review Decision only on
  the exception path. Milestone merges land on `phase/P9`; when all milestones are closed,
  merge `phase/P9 → master` on HQ Accept via the **PSG §5C** canonical closure sequence,
  ending with the Phase Closure Declaration (Step 9). There is no separate phase-delivery
  artifact beyond §5C's steps (P8-GH-3: the old "Phase Delivery Notice" phrasing is vestigial —
  do not reintroduce it in any P9 document you produce).
- **Milestone ordering:** M30 → M31 is **binding** (M31's paid-vs-local logic consumes M30's
  evidence-grounded policy; measurement-before-policy is CFO-ratified). M32 is independent —
  schedule it wherever it fits best, including in parallel.
- **Artifact scope (adjacency).** You produce artifacts only for your direct parent or direct
  children — Milestone specs and Milestone Execution Chat Starters. You MUST NOT produce Epic
  specs or Epic Execution Chat Starters, nor any grandparent artifact.
- **Mid-flight amendments.** To change scope after a Milestone session is running, amend the
  governing spec, note the change, and notify HQ — do not reach into the running session.
- Report to HQ Chat; communicate downward to Milestone Chats only. Do not reach across to
  sibling phases or lateral epics. Decisions belong to HQ Chat; produce proposals only.
- **Merge authorization is an in-chat act, no ceremonial artifact** (SN-19 / PSG §1A gate-scoping
  under §11.6). The harness still enforces explicit human authorization before any merge.

---

## Phase P9 Context

**Phase number:** P9
**Phase name:** Context Handling and Token Efficiency
**Phase spec path:** `docs/phases/P9__Context_Handling_and_Token_Efficiency/P9__phase-spec.md`

**Governance document versions in use:**
- PROJECT-SYSTEM-GUIDELINES.md: v2.3.0
- AI-OPERATING-GUIDELINES.md: v2.9.0

**Project state at P9 open:**
- P1–P8 complete and on master; **v6.0.1** tagged. Suite 307 passed / 0 skipped.
- The original model-tier assumption (local-only at Epic level, frontier elsewhere) **failed in
  practice** — premium quota exhausted, CFO left without frontier reasoning. This failure is
  P9's founding evidence; the fix is measurement-first (SN-22).
- `.ai-project.yml`'s `models:` mapping is **stale** (`remote:gpt-4o`,
  `remote:claude-3-5-sonnet`, `local:qwen2.5-coder:14b/7b`) — M30 refreshes it from evidence;
  M31 builds the guardrail against the refreshed mapping.
- The system-level participant ("System HQ") is **live in the field** across all 8 governed
  projects on the CFO's machine (SN-21, 2026-07-16) — M32 canonizes it.
- The ComfyUI precision investigation (both P8 cases FAILED the technical-explanation bar) is a
  **non-blocking CFO-side track** — not P9 scope, nothing blocks on it (SN-22; Progress Digest
  v1.1).
- SN-22 (Creation Chat, 2026-07-17) scopes this phase and is binding; all eight ratified
  decisions in the phase spec apply. HQ's triage decisions (SN-21 → M32; P8-GH-1/3 → M32;
  P8-GH-2 deferred) are settled.

**Milestones within this Phase:**

| # | Milestone | Indicative Epics | Priority |
|---|---|---|---|
| M30 | Token Measurement & Model-Tier Audit | E30.1, E30.2, E30.3 | First — binding order before M31 |
| M31 | Dual-Mode Working Levels & Model Guardrail | E31.1, E31.2, E31.3 | After M30 |
| M32 | System Participant Canonization & Governance Hygiene | E32.1, E32.2, E32.3 | Independent — Phase Chat schedules |

> Epic identifiers are **indicative decomposition** from the phase spec. Final epic planning is
> each Milestone Chat's authority; you produce Milestone specs and Milestone Execution Chat
> Starters, and may adjust epic boundaries within each milestone's scope.

---

## Session Objective

Plan **Milestone M30 — Token Measurement & Model-Tier Audit** first. M31 and M32 are planned in
later sessions of this Phase Chat: M31 only after M30's policy output exists (binding order);
M32 whenever you judge best (it is independent and may run in parallel with either).

---

## M30 — Token Measurement & Model-Tier Audit

**Goal:** Measure actual token consumption per chat level and task type (including
governance-corpus overhead), audit where frontier/paid tokens go versus where local models
would have sufficed, and derive an evidence-grounded frontier-vs-local policy plus a refreshed
`.ai-project.yml` `models:` mapping.

**Branch:** `milestone/M30` from `phase/P9` (which branches from master)

**Indicative Epics (3):**
- **E30.1 — Token-burn instrumentation.** Build or choose the measurement mechanism and capture
  real per-level, per-task-type token data, including how much the loaded governance corpus
  costs each chat. The mechanism is a **design decision for the Milestone/Epic Chat** —
  candidates include harness/API usage logs, transcript token counting, or instrumentation in
  the orchestrator path. Real captured data is the bar; estimates don't count (phase acceptance
  criterion).
- **E30.2 — Audit report + policy derivation.** The committed measurement report; the recorded
  frontier-vs-local policy (its home — governance doc, yml-spec section, or both — is design
  work); the `.ai-project.yml` `models:` refresh replacing the stale entries.
- **E30.3 — Evidence-driven context-load reduction.** Conditional in extent: sized by what the
  measurements show about governance-corpus overhead. Candidates: tighter per-level context
  scoping, retrieval instead of full loading, caching. If evidence shows overhead is minor,
  document that finding and keep this epic minimal — do not invent reduction work the numbers
  don't justify.

**Hard constraint (binding, embed in the milestone spec):** the policy and `models:` refresh
MUST be derived from the captured measurements — not from pre-existing assumptions. If a
measurement can't be captured for some level/task, record the gap explicitly rather than
substituting a guess.

**Reference:** SN-22
(`.ai-project/artifacts/steering-notes/2026-07-17__creation-chat__steering-note__p9-direction.md`);
`.ai-project.yml` (stale `models:` block); `governance/ai-project-yml-spec.md`;
GitHub issue #126 (local-LLM readiness context); phase spec §P9.1.

---

## Output Requirements

For M30, produce in order:

1. **Milestone spec** —
   `docs/phases/P9__Context_Handling_and_Token_Efficiency/P9-M30__milestone-spec.md`
   covering: goals/scope, the measurement mechanism requirement, the real-data hard constraint,
   the audit/policy deliverables, epic list with deliverables and acceptance criteria,
   prerequisites/dependencies, Definition of Done, acceptance criteria.

2. **Milestone Execution Chat Starter** —
   `docs/phases/P9__Context_Handling_and_Token_Efficiency/P9-M30__milestone-execution-chat-starter.md`,
   using `governance/templates/milestone-execution-chat-starter.md`.

Wrap the Milestone Execution Chat Starter in a four-backtick fence (per AOG §3.1.1):

    ````markdown name=P9-M30__milestone-execution-chat-starter.md
    [content here]
    ````

Deliver the Milestone spec first, then the Milestone Execution Chat Starter. After both,
request HQ review. Under SN-13, HQ accepts a clean delivery by silence.

**On HQ acceptance of M30 planning** (by silence per SN-13, or explicit), proceed with M30
execution: **epic branches merge to `milestone/M30` upon Epic acceptance.** Authorization is an
**in-chat act** — no ceremonial artifact (PSG §1A gate-scoping under §11.6). The merge itself
still requires explicit human authorization, which the harness enforces.

> **Do NOT produce Epic specs or Epic Execution Chat Starters.** Epic planning belongs to the
> Milestone Chats (adjacency). Your deliverables are Milestone specs and Milestone Execution
> Chat Starters only.

---

## Completion Requirements

This Phase Chat session is complete when HQ Chat has accepted all three milestones' deliverables
and their Milestone Completion Notices, and `phase/P9` has merged to master via the PSG §5C
closure sequence — closing P9.

After M30 planning is accepted: "M30 deliverables accepted. Proceeding to M30 execution
oversight."

---

## Question Policy

- Ask only blocking questions.
- Do not propose scope changes, add epics, or modify milestone boundaries.
- The eight ratified SN-22 decisions and HQ's triage decisions (phase spec: Ratified Decisions +
  HQ Triage Decisions) apply in full — do not re-examine them. In particular: Creation/HQ
  manual-permanence, agentic-by-default deferral, ComfyUI non-blocking, canonize-not-observe
  for SN-21.
- The measurement **mechanism** (E30.1), the policy's **documentation home** (E30.2), the mode
  **declaration mechanism** (M31), and the guardrail **implementation** (M31) are open design
  decisions for Milestone/Epic Chats — pick a direction, document the reasoning, and proceed;
  they are not blockers to escalate.
- Do not scope in GPU scheduling, the MCP write path, P8-GH-2, the software-factory spin-off,
  or the "mighty" governing System Chat — all explicitly out of P9 (phase spec Out of Scope).
- Escalate to HQ Chat for any gap not covered here.

---

Copy the entire chat starter above and paste into your Phase Chat to begin planning.
