# Phase Execution Chat Starter — P12

**Phase:** P12 — Completion: Fail-Closed Defaults and the Drivr MVP
**Project:** ai-project-system
**Repository:** https://github.com/panchew/ai-project-system
**Phase Spec:** `docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12__phase-spec.md`
**Opening Ruling:** `.ai-project/artifacts/rulings/2026-08-19__ai-project-system-hq__ruling__p12-opening-and-sn-30-37-triage.md`
**Execution Mode:** manual
**Issued:** 2026-08-19

---

## Governance References

You are operating under the AI Project System governance framework as a **Phase Chat** for Phase P12.

**Authoritative governance documents:**
- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) v2.4.0
- [AI-OPERATING-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/AI-OPERATING-GUIDELINES.md) v2.10.1

**Governance hierarchy (for this session):**
1. PROJECT-SYSTEM-GUIDELINES.md (highest authority)
2. AI-OPERATING-GUIDELINES.md v2.10.1
3. This Phase Execution Chat Starter
4. Phase Spec (`P12__phase-spec.md`)
5. Decisions made during this session
6. System references
7. Chat messages (lowest authority)

**Model verification (P9-M31-E31.3 — required, this instance is manual):** read your own
harness-reported model identity and compare it to `.ai-project.yml`'s `models.phase`
(`remote:claude-opus-5`). **If they disagree, STOP and state the mismatch; wait for human
resolution.** Do not proceed on a mismatch.

**Execution Mode is `manual` and is not a preference.** No dispatch mechanism consumes a Phase-level
agentic declaration — the path is implemented at **Epic only** (SN-31 Carry-Over 1). A Phase Chat
declaring `agentic` would be declaring a mode nothing can execute. **Mode is not authority** in
either direction.

---

## Phase P12 Context

**Eleven phases built a governance framework and, in P11, a coordinator for it. None of them used
it.** Agentic mode has never been integrated in any project — the CFO's own words, recorded in SN-31:
*"just doing some testing and measuring does not count as being using it already."*

**P12's spine, in the CFO's words:** *completing what I think is my vision of the workflow, using the
governance and the MVP of the harness (Drivr).* **A completion phase, not a redesign** — established
by evidence: the CFO described his intended workflow to a chat held deliberately ignorant of this
implementation, and the diff against what is built came back substantially matching.

**The organizing evidence is five verified instances of one disposition** — *when the evidence that
should gate an action is absent, the action proceeds.* They are in the phase spec's Executive
Summary with file and line. **They are what this phase is about, not a defect backlog appended to
it.** Read them before planning anything.

**Read before your first output — these are your inputs and they are not re-derivable from the
spec alone:**

1. `.ai-project/artifacts/steering-notes/2026-08-18__creation-chat__steering-note__P12-spine-fail-open.md`
   — SN-31…SN-35: the spine, the finding, eight binding decisions, ten carry-overs.
2. `.ai-project/artifacts/steering-notes/2026-08-19__creation-chat__steering-note__drivr-ux-and-model-qualification.md`
   — SN-36/SN-37 and the same-day amendment: Drivr's surface, the qualification gate, twelve further
   decisions.
3. The opening ruling above — thirteen decisions, including what is **returned to the CFO** and must
   not be treated as yours.
4. `docs/phases/P12__.../P12__carry-forward-note__P12-GH-1-rework-limit-reaches-one-surface.md`
5. `docs/phases/P12__.../P12__carry-forward-note__P12-GH-2-init-validator-accepts-its-own-placeholder.md`

**Current state:** `master` at `19c77ab`, framework **v8.0.0**, suite **549 passed / 0 failed**
(measured 2026-08-19, `PYTHONPATH=. pytest -q`). No open PRs. Drivr at `~/soft-dev/drivr`.

---

## Milestone Structure and Binding Order

| Milestone | Scope | Order constraint |
|---|---|---|
| **M41** Fail-Closed Execution Tier | Rows 1-3 and 5 of the finding; `P12-GH-2` | **Gates M46** — SN-31 Decision 2 |
| **M42** The Acceptance Chain, Made Structural | Parent merges; accept-by-silence; rework flip; resume; `P12-GH-1` | Independent |
| **M43** Rituals, Records, Normative Repairs | `P11-GH-3`; HQ ritual; handoff artifact; `governance-propagation.md`; i18n; SN-30 Recs 1-2; AOG renumber | **Must close before P12 closes**; HQ ritual gates M45 |
| **M44** Trustworthy Completion Signal | `P10-GH-7`; M39's judgment; `undetermined` first-class | **Gates M45** |
| **M45** The Drivr MVP Surface | SN-36's binding; SN-37's gate with its bar | Gated on M44 |
| **M46** First Real Agentic Integration | One real epic, one real project, end to end | **Gated on M41** |

**Two binding orders: `M41 → M46` and `M44 → M45`.** M42 and M43 are independent of each other and
of the M44/M45 pair, and may run in parallel at your discretion. **A change to either binding order
is an escalation to HQ, not a decision.**

**`P11-GH-1` is an active risk and you own the mitigation.** Mid-flight spec amendments do not reach
working branches; it fired **four times in P11**, once in reverse. P12 runs three parallel tracks.
**State in each Milestone Execution Chat Starter you write how an amendment reaches a branch already
in flight.** Do not wait for it to fire.

---

## Session Objective

Plan **Milestone M41 — Fail-Closed Execution Tier** first.

M41 is first because it is the only milestone with zero dependency on anything else in the phase, and
because **it gates M46, which is the phase's proof.** M42, M43, M44, M45 and M46 are planned in later
sessions of this Phase Chat. **You may plan M42 and M43 in parallel with M41's execution once M41's
planning is accepted** — they are independent — but **do not plan ahead of a binding order.**

**Identify M46's candidate project early, while M41 is still in flight.** It is the only milestone
whose success depends on a real project having real work available at the right moment, and it is the
one the phase exists to reach. HQ named this as the phase's open risk; surfacing a candidate early is
the mitigation.

---

## M41 — Fail-Closed Execution Tier

**Goal:** no path in `bin/` proceeds when the evidence that should gate it is absent. Four defects,
one design question, and two tests that currently assert the defect rather than the guard.

**Branch:** `milestone/M41` from `phase/P12` (which you branch from `master`).

**Execution posture for M41's epics: manual / paid frontier.** These epics modify the execution tier
itself — the sandbox path, the staging path, the merge path and the initializer — and **the agentic
lane runs through the first two of them.** Routing them agentically would have the machinery under
repair supervising its own repair. Record `Execution Mode: manual` and `models.epic_manual` in every
Epic Execution Chat Starter the Milestone Chat writes. **This is a scoping judgment about these
epics, not a general ruling about local inference.**

**The four defects, all verified on `master` at `19c77ab`:**

1. **`bin/ai-project-orchestrator:393-397`** — `FileNotFoundError` on the Docker invocation falls
   through to `subprocess.run(command, shell=True, ...)` on the host. **Isolation fails open.** The
   fix is not a louder log: absence of isolation must abort, and any surviving host-execution path
   must be an **explicitly declared, recorded** opt-in that the run record states.
2. **`bin/ai-project-orchestrator:472`** — `git add .` stages the entire tree, then commits it under
   the epic's message. **The design question M41 owes an answer to:** what "the epic's files" means,
   and what happens when the agent touched something it should not have. `git add .` currently
   launders that case into the epic's commit.
3. **`bin/ai-project-git-merge:269, 275-281`** — approval failure prints *"Proceeding to merge"* and
   runs a three-rung ladder ending in **`--admin`** and `--auto`. Approval failure must abort; the
   `--admin` rung goes or is gated behind a recorded human authorization.
4. **`bin/ai-project-init:328, 336-353`** (`P12-GH-2`, **High**) — the governance-agent source path is
   one `governance/` level short of where the submodule puts it; the fallback writes a 230-byte
   placeholder; **the validator then accepts the placeholder.** The second init defect travels with
   it: `submodule_path: governance/` against the fleet's `.governance` convention. **Repairing
   installs without repairing init re-breaks them on the next install.**

**Two tests must be inverted, not deleted:**

- `bin/ai-project-git-merge:447-460` asserts the `--admin` rung succeeds against a branch that
  returned *"Branch protected."*
- `tests/test_init_agent_path.py` invokes the script with `--skip-submodule`, so the branch that would
  fail is unreachable under its own test. It correctly guards `P6-GH-11`; it cannot see this defect.

**After inversion the suite must fail if the admin override is reachable unrecorded, or if a
placeholder agent is installable at all.**

**Three obligations M41 carries beyond the fixes:**

- **Run a real end-to-end `ai-project-init`** (not `--skip-submodule`). HQ's `P12-GH-2` diagnosis
  states its own verification boundary: the paths were read, the live victim was taken from the
  record, and **no end-to-end init was run.** M41 runs it. If the inference is wrong, say so — the
  finding shrinks to the validator and the test, which are defects on their own terms.
- **Sweep the fleet for existing placeholder agents** and repair or record each, `social-stories-creator`
  included. Enumerate; do not fix only the one known case.
- **Determine and record the blast radius.** These scripts live in `bin/` at the repo root and are
  therefore **not** inside the `governance/` submodule adopters consume — but `AI-OPERATING-GUIDELINES.md`,
  `chat-hierarchy.md` and three guides instruct adopters to use them. **Name every caller, Drivr
  included.**

---

## Output Requirements

For M41, produce in order:

1. **Milestone spec** —
   `docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12-M41__milestone-spec.md`
   covering: goals and scope; the four defects with their verified file:line; the design question in
   defect 2 named as a decision the milestone owes; the two test inversions; the three obligations
   above; the epic list with deliverables and acceptance criteria; prerequisites and dependencies
   (including that M41 gates M46); Definition of Done; and acceptance criteria.

2. **Milestone Execution Chat Starter** —
   `docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12-M41__milestone-execution-chat-starter.md`,
   using `governance/templates/milestone-execution-chat-starter.md`.

**The starter you write must carry the 3-attempt rework rule explicitly, in its own body.** The
template does not contain it — that is `P12-GH-1`, filed and open, and M42 has not yet fixed it. Do
not rely on the template to deliver a rule it does not have. **State the limit, and state that a
written extension grants exactly one further attempt** (SN-36/37's amendment, which is stricter than
`milestone-execution-chat-starter.md:334`'s *"resets"*). If the two statements still disagree in the
corpus when you write it, **cite the amendment and note the conflict** — reconciling them is M42's
work, not yours.

Deliver the Milestone spec first, then the starter — hand off **reference-first** per AOG §3.1.1:
emit the committed path plus a one-line summary rather than echoing the body. Use the fenced
full-body fallback only for a genuinely repo-less consumer. After both, request HQ review. Under
§11.6 default-accept, HQ accepts a clean delivery by silence.

**On HQ acceptance of M41 planning**, proceed with M41 execution oversight: epic branches merge to
`milestone/M41` upon Epic acceptance.

> **Note on merge authorization, which changes inside this phase.** Today, merge authorization is an
> in-chat act and the merge itself requires explicit human authorization the harness enforces. **M42
> moves the merge to the parent** (SN-31 Decision 4). Until M42 delivers, operate under the current
> rule; when M42 lands, it applies to milestones planned after it. **Do not pre-apply it.**

> **Do NOT produce Epic specs or Epic Execution Chat Starters.** Epic planning belongs to the
> Milestone Chats (adjacency). Your deliverables are Milestone specs and Milestone Execution Chat
> Starters only.

---

## Completion Requirements

This Phase Chat session is complete when HQ Chat has accepted all six milestones' deliverables and
their Milestone Completion Notices, and `phase/P12` has merged to `master` via the PSG §5C closure
sequence — closing P12.

**P12's closure is different from every prior phase's, and this is deliberate.** `P11-GH-3` lands in
M43: a **Phase Completion Declaration at §5C Step 2**, marked `COMPLETE (awaiting consolidation)`,
carrying the verification checklist, milestone table and phase summary that in P11 lived in a PR
comment. **P12's own closure is its first customer.** Use it. If M43 has delivered it, closing P12
without one is a defect against the phase's own product. §5C **Step 9**'s declaration is unmoved and
still records the merge commit, tag and head.

After M41 planning is accepted: "M41 deliverables accepted. Proceeding to M41 execution oversight."

---

## Question Policy

- Ask only blocking questions.
- Do not propose scope changes, add milestones, or modify milestone boundaries. **The two binding
  orders are binding** — a change to either is an escalation, not a decision.

**The binding decisions in the phase spec apply in full — do not re-examine them.** Twenty-three
across SN-31 and SN-36/37, plus thirteen HQ decisions in the opening ruling. In particular: the
parent performs the merge; accept-by-silence is tweaked, not retired; exhausted rework flips the
parent to manual as an opt-out default that Drivr performs and records; **resume restores, never
promotes, and returns the mode not the budget**; a written extension grants **+1**, not a reset;
`undetermined` is a **first-class board state**; the qualification bar is **relative and objective**
over a floor of tool rounds > 0 and files changed > 0; **the chat forms the judgment, the signed link
carries the key** — a chat reply is never authorization; the app writes committed artifacts and does
not hold state; `queued` is a property of **the lane**, not the epic; escalate-further advances
**one** level.

**CLOSED — must not be reopened, re-parked, or re-inherited:**
- **llama.cpp and any non-Ollama local runtime.** Closed by CFO decision; its hardware trigger is
  **void**; no phase re-inherits it.
- **Push / WhatsApp notification** — deferred.
- **Sidekick-for-external-projects** — a **Brief-level identity question**, not a phase pivot.
- **Phase and Milestone agentic dispatch** — it does not exist. P12 confines agentic to Epic and
  makes the *interface* refuse to imply otherwise.
- **Governance auto-update** — **split** by the opening ruling; **neither half is in P12.** Half A's
  first possible customer is P13. The `ai-project-init` fix is in M41 **on its own merits as a
  fail-open defect**, and is not a reconciler component.
- **SN-30 Recs 3, 4 and 5** — deferred with recorded reasoning and triggers.
- **`model-routing-policy.md` row P4** and the per-level model/mode mapping — the CFO's, on his
  timing. **No configuration change is authorized by this phase.**

**Design decisions that are yours or your children's — pick a direction, document the reasoning, and
proceed; do not escalate these:**
- What "the epic's files" means for scoped staging, and what happens to out-of-scope modifications
  (M41).
- Whether the sandbox opt-in is a flag, a config key, or a per-run declaration (M41).
- What replaces silence as the sole carrier of acceptance, given that a clean delivery must still
  cost no artifact (M42).
- The shape of the single normative statement governing the rework limit, and which surface holds it
  (M42).
- The Phase Completion Declaration's fields and template (M43).
- Where the HQ re-instantiation ritual lives and what it names (M43).
- What the completion judgment is built from, given M40's **F5** — *the ordered-ledger projection
  fixes only half the problem; a perfect ledger on a read-only run still returns
  `NO_EFFECTS_OBSERVED` because `_decide` never reads `Role.INSPECTION`* (M44).
- The board's rendering of `undetermined`, given that it must be its own state (M45).

**Seven items are returned to the CFO and are unowned. Do not treat any as binding, and do not
absorb them:** the escalation terminus; governance auto-update's partial-apply and
immutable-artifact sub-questions; the `local-agent-runner` retention bar; model-watch cadence;
whether the `P11-GH-2` sibling pattern earns its own record; the artifact-type inventory; row P4 and
the per-level mapping. **Each is listed in the phase spec's "Open Items — Returned to the CFO."** If
a milestone reaches one with no answer, escalate rather than deciding it.

**Method obligations that apply to you, inherited from P11 and cheap to honour:**
- **G2 — the reviewer re-measures.** The executor's report is not the evidence. HQ re-measured SN-32
  on the way in and found two figures that did not survive; you should expect the same of HQ's.
- **`P11-GH-2` — state the layer, time and scope a claim was verified at**, and do not assert about
  one tier from a measurement taken in another.
- **This corpus defeats naive pattern-matching.** `\b` is unusable against the `__` filename
  convention; literal-string guards are reflow-fragile; `--include='*.py'` skips every `bin/` entry
  point — which matters directly in M41, where all four defects are in `bin/`. **Falsify a pattern
  before trusting a zero result.**
- **An absence is only evidence when the thing that would have created it actually ran.**

Escalate to HQ Chat for any gap not covered here.

---

Copy the entire chat starter above and paste into your Phase Chat to begin planning.
