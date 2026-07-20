# Phase Execution Chat Starter — P10

**Phase:** P10 — Fleet Adoption and Local-Inference Proving
**Project:** ai-project-system
**Repository:** https://github.com/panchew/ai-project-system
**Phase Spec:** `docs/phases/P10__Fleet_Adoption_and_Local_Inference_Proving/P10__phase-spec.md`
**Issued:** 2026-07-20

---

## Governance References

You are operating under the AI Project System governance framework as a **Phase Chat** for Phase P10.

**Authoritative governance documents:**
- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) v2.3.0
- [AI-OPERATING-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/AI-OPERATING-GUIDELINES.md) v2.10.0

**Governance hierarchy (for this session):**
1. PROJECT-SYSTEM-GUIDELINES.md (highest authority)
2. AI-OPERATING-GUIDELINES.md v2.10.0
3. This Phase Execution Chat Starter
4. Phase Spec (`P10__phase-spec.md`)
5. Decisions made during this session
6. Chat messages (lowest authority)

**Critical rules:**
- Stage 1 (per milestone): produce the Milestone spec and Milestone Execution Chat Starter,
  use `phase/P10` (create it from master at phase open — it does not yet exist; branch and use
  it), commit all planning artifacts, and open a long-lived `phase/P10 → master` PR for HQ review
  on the first milestone. Not merged until the phase completes.
- Stage 2: receive each Milestone Completion Notice; under the **SN-13 default-accept model**
  (PSG §11.6 / AOG §12), accept a clean delivery by silence — issue a Review Decision only on the
  exception path. Milestone merges land on `phase/P10`; when all milestones are closed, merge
  `phase/P10 → master` on HQ Accept via the **PSG §5C** canonical closure sequence, ending with
  the Phase Closure Declaration (Step 9). There is no separate phase-delivery artifact beyond
  §5C's steps (P8-GH-3: the old "Phase Delivery Notice" phrasing is vestigial — do not
  reintroduce it in any P10 document you produce).
- **Milestone ordering:** M33 → M34 is **binding** (M34's fleet roll-forward consumes M33's
  v7.0.0 bump procedure and its settled local-runtime choice). **M35 is independent** — schedule
  it wherever it fits best, including in parallel.
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

## Phase P10 Context

**Phase number:** P10
**Phase name:** Fleet Adoption and Local-Inference Proving
**Phase spec path:** `docs/phases/P10__Fleet_Adoption_and_Local_Inference_Proving/P10__phase-spec.md`

**Governance document versions in use:**
- PROJECT-SYSTEM-GUIDELINES.md: v2.3.0
- AI-OPERATING-GUIDELINES.md: v2.10.0

**Project state at P10 open:**
- P1–P9 complete and on master; **v7.0.0** tagged. Suite 363 passed / 0 skipped.
- The framework is **done being built** (CFO's judgment, backed by the repo). What has not
  happened is the framework doing its job in the wild: of 10 projects in `~/soft-dev`, 8 are
  enrolled but enrollment is **shallow**, and **no project except the framework is confirmably on
  v7.0.0.** P10's founding fact is this adoption gap; the fix is to run real epics on real
  projects (SN-23).
- The fixed operating posture — **Manual/Paid from Creation through Milestone, Agentic/Local at
  the Epic** — is applied through P9's dual-mode switch (M31) and manual-mode guardrail; P10 does
  not rebuild them, it uses them.
- The **local-inference substrate is the one open risk.** `local-agent-runner` is on Ollama; the
  reference stack (Qwen3.6 27B Q8_0 on llama.cpp, which recommends against Ollama) points the
  other way. The runtime fork is settled by the **first real epic on the proving pair** (M33/E33.2),
  not decided in the abstract.
- **Run-first ordering** is binding: measurement and validation come OUT of real epic runs, not
  before them. `measure-token-burn` (P9/M30) is fixed only as far as trusting a real run's
  numbers requires (P9-GH-2, folded into M33/E33.3).
- SN-23 (Creation Chat, 2026-07-20) scopes this phase and is binding; all eight ratified
  decisions in the phase spec apply. HQ's triage decisions (3-milestone shape; P9-GH-2 → M33;
  P6-GH-15 → M34; P9-GH-1 / P9-GH-3 / competing-model review / ComfyUI / P8-GH-2 parked or
  deferred) are settled.

**This is the framework's first phase whose deliverables land substantially in OTHER repos.** A
v7.0.0 bump and a real epic on `home_finance` change *that* repo, not this one. The framework repo
holds the **governance record** — phase/milestone/epic specs, execution-chat starters, delivery/
closure artifacts, and the captured **evidence** (run records, burn data, the runtime decision).
The Milestone/Epic Chats own the mechanics of driving a governed run in a target repo. The
`phase/P10` branch here accumulates the governance record and evidence; the target repos receive
the actual bumps and code. Reflect this in every Milestone spec you write.

**Milestones within this Phase:**

| # | Milestone | Indicative Epics | Priority |
|---|---|---|---|
| M33 | Proving Pair — v7.0.0 + First Real Agentic/Local Epic | E33.1, E33.2, E33.3 | First — binding order before M34 |
| M34 | Fleet Roll-forward | E34.1, E34.2 | After M33 |
| M35 | System-Operator Canonization | E35.1, E35.2 | Independent — Phase Chat schedules |

> Epic identifiers are **indicative decomposition** from the phase spec. Final epic planning is
> each Milestone Chat's authority; you produce Milestone specs and Milestone Execution Chat
> Starters, and may adjust epic boundaries within each milestone's scope.

---

## Session Objective

Plan **Milestone M33 — Proving Pair: v7.0.0 + First Real Agentic/Local Epic** first. M34 and M35
are planned in later sessions of this Phase Chat: M34 only after M33's bump procedure and settled
runtime choice exist (binding order); M35 whenever you judge best (it is independent and may run in
parallel with either).

---

## M33 — Proving Pair: v7.0.0 + First Real Agentic/Local Epic

**Goal:** On `home_finance` and `local-agent-runner` (the two projects with canonical
`governance.agent.md` already installed), bump each to v7.0.0, run the first real Agentic/Local
epic under the fixed posture, settle the Ollama-vs-llama.cpp runtime question from that run, and
produce trustworthy burn/validation evidence out of the run.

**Branch:** `milestone/M33` from `phase/P10` (which branches from master)

**Indicative Epics (3):**
- **E33.1 — Enrolled-project v7.0.0 bump procedure + apply to the pair.** A documented,
  **repeatable** procedure for bumping an enrolled project to v7.0.0 (governance refresh +
  `framework_version` stamp), applied to both proving-pair projects. The procedure is the reusable
  lever M34 consumes — treat it as a first-class deliverable, not a byproduct. How a bump is
  performed (re-run `ai-project-init`, targeted governance-file sync, or other) is a **design
  decision for the Milestone/Epic Chat.**
- **E33.2 — First real Agentic/Local epic on the pair + runtime decision.** Scope and run a
  **genuine** epic of the target project's own work under the fixed posture (Manual/Paid up to the
  Epic, Agentic/Local at the Epic). Capture the run record. Record the Ollama-vs-llama.cpp+Qwen3.6
  decision **with the run's own reasons** (quality, throughput, loadability, review burden) — not
  an abstract memo. A synthetic demo does not satisfy this; it must be real work that advances the
  project.
- **E33.3 — Trustworthy measurement out of the run (P9-GH-2).** Capture real burn/validation data
  from E33.2's run and fix/validate `measure-token-burn` **only as far as trusting that run's
  numbers requires.** Conditional in extent, sized by the run — do not perfect the tool in the
  abstract, and do not skip the honesty check.

**Hard constraint (binding, embed in the milestone spec):** the runtime decision (E33.2) and the
measurement judgment (E33.3) MUST be derived from a **real epic run** on the pair — run-first
ordering is CFO-ratified, not a preference. If a real run cannot be completed for a project,
record the blocker explicitly and escalate; do not substitute an abstract decision or hand-waved
numbers.

**Reference:** SN-23
(`.ai-project/artifacts/steering-notes/2026-07-20__creation-chat__steering-note__P10-adoption-spine.md`);
phase spec §P10.1; the fleet-state table (phase spec Scope); P9's `bin/run-dev-agent` +
orchestrator path and dual-mode/guardrail (M31); `measure-token-burn` (P9/M30/E30.1); the
local-model setup reference (https://quesma.com/blog/qwen-36-is-awesome/); the target repos
`home_finance` and `local-agent-runner` under `~/soft-dev`.

---

## Output Requirements

For M33, produce in order:

1. **Milestone spec** —
   `docs/phases/P10__Fleet_Adoption_and_Local_Inference_Proving/P10-M33__milestone-spec.md`
   covering: goals/scope, the proving pair and fixed posture, the repeatable-bump-procedure
   requirement, the real-run hard constraint, the runtime-decision and measurement-trust
   deliverables, the cross-repo record/evidence split, epic list with deliverables and acceptance
   criteria, prerequisites/dependencies, Definition of Done, acceptance criteria.

2. **Milestone Execution Chat Starter** —
   `docs/phases/P10__Fleet_Adoption_and_Local_Inference_Proving/P10-M33__milestone-execution-chat-starter.md`,
   using `governance/templates/milestone-execution-chat-starter.md`.

Deliver the Milestone spec first, then the Milestone Execution Chat Starter — hand off the starter
**reference-first** per AOG §3.1.1 (E30.4, live since v7.0.0): emit its committed path plus a
one-line summary rather than echoing the full body; paste the fenced block only as the documented
fallback for a repo-less consumer. After both, request HQ review. Under SN-13, HQ accepts a clean
delivery by silence.

**On HQ acceptance of M33 planning** (by silence per SN-13, or explicit), proceed with M33
execution: **epic branches merge to `milestone/M33` upon Epic acceptance.** Authorization is an
**in-chat act** — no ceremonial artifact (PSG §1A gate-scoping under §11.6). The merge itself
still requires explicit human authorization, which the harness enforces.

> **Do NOT produce Epic specs or Epic Execution Chat Starters.** Epic planning belongs to the
> Milestone Chats (adjacency). Your deliverables are Milestone specs and Milestone Execution Chat
> Starters only.

---

## Completion Requirements

This Phase Chat session is complete when HQ Chat has accepted all three milestones' deliverables
and their Milestone Completion Notices, and `phase/P10` has merged to master via the PSG §5C
closure sequence — closing P10.

After M33 planning is accepted: "M33 deliverables accepted. Proceeding to M33 execution oversight."

---

## Question Policy

- Ask only blocking questions.
- Do not propose scope changes, add milestones, or modify milestone boundaries.
- The eight ratified SN-23 decisions and HQ's triage decisions (phase spec: Ratified Decisions +
  HQ Triage Decisions) apply in full — do not re-examine them. In particular: adoption-not-
  capability, the fixed operating posture, proving-pair-first, run-first ordering, the runtime
  fork settled by a run, and the System-Chat no-authority-on-speech seam.
- The bump **mechanism** (E33.1), the **choice of the pair's first real epic** and the runtime
  **decision criteria** (E33.2), and the extent of the measurement-trust work (E33.3) are open
  design decisions for Milestone/Epic Chats — pick a direction, document the reasoning, and
  proceed; they are not blockers to escalate.
- Do not scope in a built local-inference scheduler, competing-model code review, P9-GH-1,
  P9-GH-3, ComfyUI, P8-GH-2, the unenrolled projects (ai-stack, character-factory), the external-
  sidekick identity question, or any new framework capability on spec — all explicitly out of P10
  (phase spec Out of Scope). They enter only as real adoption friction surfaces them, via HQ.
- Escalate to HQ Chat for any gap not covered here.

---

Copy the entire chat starter above and paste into your Phase Chat to begin planning.
