# Phase Execution Chat Starter — P12

**Phase:** P12 — Completion: Fail-Closed Defaults and the Drivr MVP
**Project:** ai-project-system
**Repository:** https://github.com/panchew/ai-project-system
**Phase Spec:** `docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12__phase-spec.md`
**Opening Ruling:** `.ai-project/artifacts/rulings/2026-08-19__ai-project-system-hq__ruling__p12-opening-and-sn-30-37-triage.md`
**Execution Mode:** manual
**Issued:** 2026-08-19 · **Amended:** 2026-08-19 (SN-38 restructure — seven milestones)

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
3. `.ai-project/artifacts/steering-notes/2026-08-19__creation-chat__steering-note__model-lineup.md`
   — SN-38: the ruled model line-up, row P4's closure, SN-37's widened gate scope, and the CFO's
   direction that the evidence be collected **first**.
4. The opening ruling above — thirteen decisions **plus an amendment carrying six more (14-19)**,
   including what is **returned to the CFO** and must not be treated as yours. **The amendment
   restructured this phase to seven milestones**; the mapping is in its banner and in the phase
   spec's v1.1.0 changelog.
5. `docs/phases/P12__.../P12__carry-forward-note__P12-GH-1-rework-limit-reaches-one-surface.md`
6. `docs/phases/P12__.../P12__carry-forward-note__P12-GH-2-init-validator-accepts-its-own-placeholder.md`

**Current state:** `master` at `19c77ab`, framework **v8.0.0**, suite **549 passed / 0 failed**
(measured 2026-08-19, `PYTHONPATH=. pytest -q`). No open PRs. Drivr at `~/soft-dev/drivr`.

---

## Milestone Structure and Binding Order

| Milestone | Scope | Order constraint |
|---|---|---|
| **M41** The Model Line-Up and Its Evidence | The ruled line-up measured before it lands; `epic_dev`/`epic_qa` separately; incumbent baseline | **Opens first, closes late** — terminal epic gated on M42 |
| **M42** Fail-Closed Execution Tier | Rows 1-3 and 5 of the finding; `P12-GH-2` | **Gates M47** — SN-31 Decision 2 |
| **M43** The Acceptance Chain, Made Structural | Parent merges; accept-by-silence; rework flip; resume; `P12-GH-1` | Independent |
| **M44** Rituals, Records, Normative Repairs | `P11-GH-3`; HQ ritual; handoff artifact; `governance-propagation.md`; i18n; SN-30 Recs 1-2; AOG renumber | **Must close before P12 closes**; HQ ritual gates M46 |
| **M45** Trustworthy Completion Signal | `P10-GH-7`; M39's judgment; `undetermined` first-class | **Gates M46** |
| **M46** The Drivr MVP Surface | SN-36's binding; SN-37's gate with its bar | Gated on M45 |
| **M47** First Real Agentic Integration | One real epic, one real project, end to end | **Gated on M42** |

**Three binding constraints: `M42 → M47`, `M45 → M46`, and M41's terminal epic gated on M42's
closure.** M43 and M44 are independent of each other and of the M45/M46 pair, and may run in parallel
at your discretion. **A change to any of the three is an escalation to HQ, not a decision.**

**M41's number is allocation order, not closing order.** It opens first because the CFO directed the
evidence be collected early; its terminal epic — the `.ai-project.yml` edit plus the
`model-routing-policy.md` mapping-table and row-P4 update, **which travel as one epic so they cannot
drift apart** — waits for M42, because a model change landing with a lane repair makes the next
failure unattributable.

**`P11-GH-1` is an active risk and you own the mitigation.** Mid-flight spec amendments do not reach
working branches; it fired **four times in P11**, once in reverse. P12 runs three parallel tracks.
**State in each Milestone Execution Chat Starter you write how an amendment reaches a branch already
in flight.** Do not wait for it to fire.

---

## Session Objective

Plan **Milestone M41 — The Model Line-Up and Its Evidence** first, then **M42 — Fail-Closed
Execution Tier**.

**M41 is first by CFO direction, given after the phase opened** — his call to make, and made: the
model evidence is collected early. It is cheap and three of its four inputs already exist. **M42
follows immediately**, and is the milestone with zero dependency on anything else in the phase and
the one that **gates M47, the phase's proof.** M43, M44, M45, M46 and M47 are planned in later
sessions. **You may plan M43 and M44 in parallel with execution once their predecessors' planning is
accepted** — they are independent — but **do not plan ahead of a binding constraint.**

**Identify M47's candidate project early, while M42 is still in flight.** It is the only milestone
whose success depends on a real project having real work available at the right moment, and it is the
one the phase exists to reach. HQ named this as the phase's open risk; surfacing a candidate early is
the mitigation.

---

## M41 — The Model Line-Up and Its Evidence

**Goal:** the CFO's ruled per-level line-up, measured before it lands, with `epic_dev` and `epic_qa`
separated for the first time.

**Branch:** `milestone/M41` from `phase/P12` (which you branch from `master`).

**Execution posture for M41's epics: manual / paid frontier**, on the models declared **today**. The
milestone's own subject is which models to run; running it on the candidates it is measuring would be
circular.

**The line-up, ruled — not yours to re-decide:**

| Key | Current | Target |
|---|---|---|
| `creation` | `remote:claude-opus-5` | **fable-5** |
| `hq` | `remote:claude-opus-5` | **unchanged** |
| `phase` | `remote:claude-opus-5` | **GPT-5.6 Sol** |
| `milestone` | `remote:claude-opus-5` | **Deepseek V4 Flash** — a **policy-row change**, closing row P4 |
| `epic_manual` | `remote:claude-opus-5` | **local:qwen3.8:27b** |
| `epic_dev` / `epic_qa` | `local:qwen3-coder:30b` | **held pending your measurement** |

**Two harnesses, because the checks do not transfer:**

- **Dispatch lanes** (`epic_dev`, `epic_qa`) — detect **successful nothing**: tool rounds > 0, files
  changed > 0, claims resolving against files that exist. **The instrument must be built**; a minimal
  version is M41's, the formalized gate is M46's.
- **Verification targets** (`creation`, `phase`, `milestone`, `epic_manual`) — detect **failed
  judgment**: planted defects, catches versus false alarms. **The instrument already exists** —
  E35.5's back-test, digest-confirmed as *"remains available."* Do not rebuild it.

**What you measure, and the premise correction that shapes it:**

1. **`epic_dev` and `epic_qa` separately.** They hold the same string today and the record treats
   them oppositely — `epic_dev` owns the project's **only mergeable-work evidence** (E33.2 Run B,
   E33.4); `epic_qa` owns its **only recorded fabrication** (E39.3). One string has been hiding that.
2. **The incumbent first.** There is no baseline for `qwen3-coder:30b` on the judgment task, and the
   bar is **relative** — the candidate must be no worse on every objective check and strictly better
   on at least one, over a floor of tool rounds > 0 and files changed > 0.
3. **`qwen3-coder:30b` has NEVER been compared against any 27b.** E33.2 compared the **14b** against
   the 30b. E35.5's `PASS 4/5, one SPLIT, zero false alarms` over ten runs belongs to
   **`qwen3.6:27b`**, chosen deliberately because Stage-2 review is general reasoning and the 30b is
   coder-tuned. **The only milestone-level judgment result this project owns belongs to a 27b.**
4. **`qwen3.6:27b` is present in Ollama but declared nowhere in `opencode.json`** — it is **not
   routable** through the execution adapter without a config addition. **That addition is your work,
   and must not be discovered mid-run.**
5. **`qwen3.8:27b` is present on this host** — 17.7 GB, verified by HQ 2026-08-19. **Re-confirm at
   run time; do not inherit it from this document.** Both 27b entries exceed this box's 16 GB VRAM
   and will partially offload, less than the 30b's 18.6 GB.
6. **The three remote targets — fable-5, GPT-5.6 Sol, Deepseek V4 Flash — are UNVERIFIED.** HQ
   checked local models only. **Confirm each is reachable before you measure it**, and escalate if
   one is not.

**The terminal epic, and its two gates:**

- It carries the **`.ai-project.yml` edit** and the **`model-routing-policy.md` mapping-table and
  row-P4 update** as **one epic**, so the two cannot drift apart.
- **It may not merge until M42 is closed.**
- **Row P4 is recorded as closed by CFO ruling**, with the Change discipline satisfied **by decision,
  stated plainly**. **Do not file it as a same-tier refresh** — the 2026-07-28 precedent covers
  vendor moves within a tier and explicitly left the TIER rows untouched. This is a tier change.
- **Definition of Done includes notifying every level before the edit lands.** Five verification
  targets arm simultaneously; a chat opened on the old model afterwards **halts by design**. That is
  correct behaviour and a poor surprise.

**If a row fails its harness, escalate to HQ for the CFO. Do not land it anyway, and do not drop it.**
The CFO ruled the line-up *and* ruled that the gate binds it; when the two disagree, the result goes
in front of him. **HQ has already decided this** (Decision 15) — you do not need to re-derive it, and
you do not have authority to resolve it yourself.

**Safe to measure now:** a qualification run dispatches through the agentic lane and M42 is repairing
that lane, but **Docker is present on this host**, so the unsandboxed fallback will not fire. The
dependency is real and non-blocking.

---

## M42 — Fail-Closed Execution Tier

**Goal:** no path in `bin/` proceeds when the evidence that should gate it is absent. Four defects,
one design question, and two tests that currently assert the defect rather than the guard.

**Branch:** `milestone/M42` from `phase/P12` (which you branch from `master`).

**Execution posture for M42's epics: manual / paid frontier.** These epics modify the execution tier
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
   the epic's message. **The design question M42 owes an answer to:** what "the epic's files" means,
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

**Three obligations M42 carries beyond the fixes:**

- **Run a real end-to-end `ai-project-init`** (not `--skip-submodule`). HQ's `P12-GH-2` diagnosis
  states its own verification boundary: the paths were read, the live victim was taken from the
  record, and **no end-to-end init was run.** M42 runs it. If the inference is wrong, say so — the
  finding shrinks to the validator and the test, which are defects on their own terms.
- **Sweep the fleet for existing placeholder agents** and repair or record each, `social-stories-creator`
  included. Enumerate; do not fix only the one known case.
- **Determine and record the blast radius.** These scripts live in `bin/` at the repo root and are
  therefore **not** inside the `governance/` submodule adopters consume — but `AI-OPERATING-GUIDELINES.md`,
  `chat-hierarchy.md` and three guides instruct adopters to use them. **Name every caller, Drivr
  included.**

---

## Output Requirements

**For M41, produce the same pair first** —
`P12-M41__milestone-spec.md` and `P12-M41__milestone-execution-chat-starter.md` — covering: the ruled
line-up with each row's kind of change; the two harnesses and which already exists; the six
measurement points above; the terminal epic with **both** its gates and its notification DoD item;
and the escalation rule for a row that fails its harness. **Then, for M42, produce in order:**

1. **Milestone spec** —
   `docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12-M42__milestone-spec.md`
   covering: goals and scope; the four defects with their verified file:line; the design question in
   defect 2 named as a decision the milestone owes; the two test inversions; the three obligations
   above; the epic list with deliverables and acceptance criteria; prerequisites and dependencies
   (including that M42 gates M47); Definition of Done; and acceptance criteria.

2. **Milestone Execution Chat Starter** —
   `docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12-M42__milestone-execution-chat-starter.md`,
   using `governance/templates/milestone-execution-chat-starter.md`.

**The starter you write must carry the 3-attempt rework rule explicitly, in its own body.** The
template does not contain it — that is `P12-GH-1`, filed and open, and M43 has not yet fixed it. Do
not rely on the template to deliver a rule it does not have. **State the limit, and state that a
written extension grants exactly one further attempt** (SN-36/37's amendment, which is stricter than
`milestone-execution-chat-starter.md:334`'s *"resets"*). If the two statements still disagree in the
corpus when you write it, **cite the amendment and note the conflict** — reconciling them is M43's
work, not yours.

Deliver the Milestone spec first, then the starter — hand off **reference-first** per AOG §3.1.1:
emit the committed path plus a one-line summary rather than echoing the body. Use the fenced
full-body fallback only for a genuinely repo-less consumer. After both, request HQ review. Under
§11.6 default-accept, HQ accepts a clean delivery by silence.

**On HQ acceptance of M42 planning**, proceed with M42 execution oversight: epic branches merge to
`milestone/M42` upon Epic acceptance.

> **Note on merge authorization, which changes inside this phase.** Today, merge authorization is an
> in-chat act and the merge itself requires explicit human authorization the harness enforces. **M43
> moves the merge to the parent** (SN-31 Decision 4). Until M43 delivers, operate under the current
> rule; when M43 lands, it applies to milestones planned after it. **Do not pre-apply it.**

> **Do NOT produce Epic specs or Epic Execution Chat Starters.** Epic planning belongs to the
> Milestone Chats (adjacency). Your deliverables are Milestone specs and Milestone Execution Chat
> Starters only.

---

## Completion Requirements

This Phase Chat session is complete when HQ Chat has accepted all **seven** milestones' deliverables and
their Milestone Completion Notices, and `phase/P12` has merged to `master` via the PSG §5C closure
sequence — closing P12.

**P12's closure is different from every prior phase's, and this is deliberate.** `P11-GH-3` lands in
M44: a **Phase Completion Declaration at §5C Step 2**, marked `COMPLETE (awaiting consolidation)`,
carrying the verification checklist, milestone table and phase summary that in P11 lived in a PR
comment. **P12's own closure is its first customer.** Use it. If M44 has delivered it, closing P12
without one is a defect against the phase's own product. §5C **Step 9**'s declaration is unmoved and
still records the merge commit, tag and head.

After M42 planning is accepted: "M42 deliverables accepted. Proceeding to M42 execution oversight."

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

**From SN-38, binding and not re-decidable by you:** the line-up itself; that
`milestone → Deepseek V4 Flash` is a **policy-row change** and must not be filed as a same-tier
refresh; that SN-37's gate binds **verification targets as well as** dispatch lanes (the lanes-only
proposal is **superseded**); that `epic_dev` and `epic_qa` are measured **separately** and the
incumbent is measured to set the relative bar's baseline; and that **no model swap lands until M42
closes.**

**CLOSED — must not be reopened, re-parked, or re-inherited:**
- **llama.cpp and any non-Ollama local runtime.** Closed by CFO decision; its hardware trigger is
  **void**; no phase re-inherits it.
- **Push / WhatsApp notification** — deferred.
- **Sidekick-for-external-projects** — a **Brief-level identity question**, not a phase pivot.
- **Phase and Milestone agentic dispatch** — it does not exist. P12 confines agentic to Epic and
  makes the *interface* refuse to imply otherwise.
- **Governance auto-update** — **split** by the opening ruling; **neither half is in P12.** Half A's
  first possible customer is P13. The `ai-project-init` fix is in M42 **on its own merits as a
  fail-open defect**, and is not a reconciler component.
- **SN-30 Recs 3, 4 and 5** — deferred with recorded reasoning and triggers.
- **`model-routing-policy.md` row P4** — **CLOSED 2026-08-19 by CFO ruling** (SN-38). Not reopened,
  not re-argued; **recorded and executed** by M41's terminal epic as a **policy-row change**.
- **The per-level MODE mapping** — still a plan awaiting measurement, still the CFO's. **The per-level
  MODEL mapping is ruled and is M41's work.** The configuration change this phase authorizes is
  **exactly the seven keys in SN-38's table and nothing else.**

**Design decisions that are yours or your children's — pick a direction, document the reasoning, and
proceed; do not escalate these:**
- What "the epic's files" means for scoped staging, and what happens to out-of-scope modifications
  (M42).
- Whether the sandbox opt-in is a flag, a config key, or a per-run declaration (M42).
- What replaces silence as the sole carrier of acceptance, given that a clean delivery must still
  cost no artifact (M43).
- The shape of the single normative statement governing the rework limit, and which surface holds it
  (M43).
- The Phase Completion Declaration's fields and template (M44).
- Where the HQ re-instantiation ritual lives and what it names (M44).
- What the completion judgment is built from, given M40's **F5** — *the ordered-ledger projection
  fixes only half the problem; a perfect ledger on a read-only run still returns
  `NO_EFFECTS_OBSERVED` because `_decide` never reads `Role.INSPECTION`* (M45).
- The board's rendering of `undetermined`, given that it must be its own state (M46).

**Seven items are returned to the CFO and are unowned. Do not treat any as binding, and do not
absorb them:** the escalation terminus; governance auto-update's partial-apply and
immutable-artifact sub-questions; the `local-agent-runner` retention bar; model-watch cadence;
whether the `P11-GH-2` sibling pattern earns its own record; the artifact-type inventory; and the
per-level **mode** mapping. **Row P4 is no longer among them — the CFO closed it on 2026-08-19,
four hours after HQ returned it to him.** **Each is listed in the phase spec's "Open Items — Returned to the CFO."** If
a milestone reaches one with no answer, escalate rather than deciding it.

**Method obligations that apply to you, inherited from P11 and cheap to honour:**
- **G2 — the reviewer re-measures.** The executor's report is not the evidence. HQ re-measured SN-32
  on the way in and found two figures that did not survive; you should expect the same of HQ's.
- **`P11-GH-2` — state the layer, time and scope a claim was verified at**, and do not assert about
  one tier from a measurement taken in another.
- **This corpus defeats naive pattern-matching.** `\b` is unusable against the `__` filename
  convention; literal-string guards are reflow-fragile; `--include='*.py'` skips every `bin/` entry
  point — which matters directly in M42, where all four defects are in `bin/`. **Falsify a pattern
  before trusting a zero result.**
- **An absence is only evidence when the thing that would have created it actually ran.**

Escalate to HQ Chat for any gap not covered here.

---

Copy the entire chat starter above and paste into your Phase Chat to begin planning.
