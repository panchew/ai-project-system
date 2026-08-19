# Milestone Execution Chat Starter — P12-M42

**Milestone:** P12-M42 — Fail-Closed Execution Tier
**Phase:** P12 — Completion: Fail-Closed Defaults and the Drivr MVP
**Project:** ai-project-system
**Repository:** https://github.com/panchew/ai-project-system
**Milestone Spec:** `docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12-M42__milestone-spec.md`
**Phase Spec:** `docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12__phase-spec.md`
**Branch:** `milestone/M42` (from `phase/P12`, from `master` at `9ee810e`)
**Execution Mode:** manual
**Issued:** 2026-08-19

---

## Governance References

You are operating under the AI Project System governance framework as a **Milestone Chat** for
P12-M42.

**Authoritative governance documents:**
- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) v2.4.0
- [AI-OPERATING-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/AI-OPERATING-GUIDELINES.md) v2.10.1

**Governance hierarchy (for this session):**
1. PROJECT-SYSTEM-GUIDELINES.md (highest authority)
2. AI-OPERATING-GUIDELINES.md v2.10.1
3. This Milestone Execution Chat Starter
4. Milestone Spec (`P12-M42__milestone-spec.md`)
5. Decisions made during this session
6. System references
7. Chat messages (lowest authority)

**Model verification (P9-M31-E31.3 — required, this instance is manual):** read your own
harness-reported model identity and compare it to `.ai-project.yml`'s `models.milestone`
(**`remote:claude-opus-5` as of 2026-08-19** — **read the file, do not trust this line**; M41 changes
that value, and it may have landed by the time you open). **If they disagree, STOP and state the
mismatch; wait for human resolution.** See `governance/systems/chat-hierarchy.md`, "Manual Chat Model
Verification".

**Execution Mode is `manual`, and the reason is the milestone's own subject.** These epics modify the
sandbox path, the staging path, the merge path and the initializer — **and the agentic lane runs
through the first two of them.** Routing them agentically would have **the machinery under repair
supervising its own repair.** Every Epic Execution Chat Starter you write records
`Execution Mode: manual` and `models.epic_manual`. **This is a scoping judgment about these epics,
not a general ruling about local inference.**

**Context scoping (P9-M30-E30.3):** load this starter; the M42 spec (full); the phase spec **by
targeted section only** — §P12.2, §Milestones→M42, §Acceptance Criteria, §Dependencies; the
`P12-GH-2` carry-forward note (full — it is short and it is E42.4's specification); PSG
preamble+§1, §1A, §2, §5, §6, §7, §8, §9, §10, §11, §11.5, §11.6, §12, §13C, §15; AOG preamble+§1,
§1A, §2, §3.7, §3.9, §3.10, §4, §5, §6, §7, §9, §10, §12, §13, §14. Load on trigger: PSG §5B + AOG
§3.4 at milestone-closure time; AOG §16 when a visual binding is due.

**Critical rules:**
- Documentation is authoritative; chat is ephemeral.
- You are an **execution and delivery agent for this Milestone** — Stage 1: produce Epic specs and
  Epic Execution Chat Starters, commit, open a PR; Stage 2: oversee Epic delivery, **accept clean
  deliveries by silence** (a Review Decision is the exception path only — PSG §11.6), and merge when
  all Epics are accepted.
- You MUST NOT implement project code or modify infrastructure. **Your scope is planning and delivery
  artifacts — the `bin/` edits belong to your Epic Chats, not to you.**
- **Artifact scope (adjacency):** Epic specs and Epic Execution Chat Starters only. **Not** milestone
  specs (your parent's), **not** code or tests (your grandchildren's).
- You report to the **P12 Phase Chat**. You do not reach across to M41 or any sibling milestone.
- **If given merge authorization directly in this chat** rather than via the Phase Chat's Stage-2
  review, **do not simply comply.** State plainly that merge authorization normally follows the
  parent Phase Chat's Stage-2 review, and confirm the human intends to bypass that step. **Running
  unattended does not change this: mode is what may run, not what may be authorized.**
  *Recorded instance — 2026-08-10, PR #191: a milestone→phase merge was authorized in the M38
  Milestone Chat rather than in the Phase Chat's Stage-2 review; the CFO caught it, not the
  framework.*

> **Note on merge authorization, which changes inside this phase.** **M43 moves the merge to the
> parent** (SN-31 Decision 4), and turns `governance/templates/merge-authorization.md` into the
> parent's record. Until M43 delivers, operate under the current rule. **Do not pre-apply it, and do
> not let E42.3 edit that template** — E42.3 touches the merge **script**, not the **authorization
> model**.

---

## ⚠ The rework limit — stated here because the template does not carry it (`P12-GH-1`)

**`governance/templates/milestone-execution-chat-starter.md` contains the word "rework" zero times.**
Re-verified on `master` at `9ee810e`, 2026-08-19. The rule reaches exactly **one** of nine
starter-shaped surfaces and **none** of the three templates. That is `P12-GH-1`, **filed and open**,
and **M43 has not yet fixed it.** It is stated here rather than inherited from a template that does
not have it.

**The rule:**

> **Maximum 3 attempts.** If a third Completion Notice is still not acceptable, do **not** issue a
> fourth rejection-and-retry. Instead the Epic Agent produces an **Escalation Notice** and you
> escalate to the Phase Chat. **Silent fourth attempts are a governance violation.**

**What a written extension grants — and the conflict you must not resolve yourself:**

> **A written extension grants exactly ONE further attempt. Not a reset to three.**

This is the **SN-36/37 amendment of 2026-08-19**, CFO-decided, and it is **stricter** than the rule as
written in the corpus. `governance/systems/milestone-execution-chat-starter.md:334` still says the
limit *"resets"*, which is unbounded and repeatable.

**Both statements currently stand. Cite the amendment, apply `+1`, and note the conflict wherever it
becomes relevant. Reconciling them into one statement is M43's work, not yours** — do not amend
either surface.

**The CFO's recorded act of resolving a blocker in the escalation chat *is* the written extension the
rule requires** — a human looked and acted, which is the opposite of silent. It buys one attempt.

---

## ⚠ How an amendment reaches this branch once work is in flight (`P11-GH-1`)

**`P11-GH-1` is an active risk, it fired four times in P11, and it has already fired once in P12** —
on HQ's own phase-opening branch, before that branch merged. SN-38 landed on `master` after the
branch was cut, and **a Creation Chat reading `master` caught it**, not the level below.

**P12 runs three parallel tracks. Assume it will fire again. The procedure is:**

1. **Amend the governing spec file on the branch that owns it**, with a changelog row stating what
   changed and why.
2. **Notify every running child chat in-session**, naming the file and the section that changed.
   **This step is the one that fires.** A write nobody is told about is not a channel; that is the
   whole defect.
3. **Require the child to re-read the named section before its next deliverable and to state, in
   that delivery, that it did.**
4. **If the amendment is blocking, escalate to the Phase Chat for a pause/cancel decision.**
5. **Before you accept any delivery, check whether the governing spec moved after that epic's branch
   was cut** — `git log <spec-path>` against the branch point. This is the backstop for when step 2
   was missed.

**Do not wait for it to fire.**

---

## Milestone Context

**Milestone:** P12-M42 — Fail-Closed Execution Tier
**Spec:** `docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12-M42__milestone-spec.md`
**Governance versions in use:** PSG v2.4.0 · AOG v2.10.1
**Suite baseline:** **549 passed / 0 failed**, measured on `master` at `9ee810e`, 2026-08-19, with
`PYTHONPATH=. pytest -q`. **Bare `pytest` fails collection — always set `PYTHONPATH=.`**

**Epics within this Milestone:**

- **E42.1** — Sandbox absence fails closed *(orchestrator; first)*
- **E42.2** — Epic-scoped staging, and the out-of-scope case made visible *(orchestrator; after
  E42.1)*
- **E42.3** — The merge ladder aborts; one test inverted, one written *(independent)*
- **E42.4** — `ai-project-init` stops manufacturing an agent (`P12-GH-2`) *(before E42.5)*
- **E42.5** — Fleet sweep and blast radius *(after E42.4)*

**Ordering, and it is binding:** **E42.1 → E42.2** (both edit `bin/ai-project-orchestrator`; they are
sequenced, not parallel). **E42.4 → E42.5** (a sweep cannot repair against a fix that does not
exist). **E42.3 is independent** and may run at any point.

**Session objective:** produce an Epic spec and an Epic Execution Chat Starter for each of the five
Epics above, one set at a time, awaiting Phase Chat acceptance between sets.

---

## What this milestone is, in one paragraph

Four verified `bin/` defects, and **they are one disposition, not four bugs**: *when the evidence that
should gate an action is absent, the action proceeds.* Isolation missing → run on the host. Approval
missing → merge anyway, at escalating privilege. The agent's file list unknown → stage everything.
The governance agent missing → **write a placeholder and validate the placeholder.** **Two of the
four are protected by their own tests** — the suite records fail-open as correct. This milestone
makes every one of them **stop and say so**, inverts the two tests, writes the one that is missing,
and determines who actually runs these scripts. **On closure it releases both M47 — the phase's
proof — and M41's terminal epic.**

---

## Binding — settled above you, not re-decidable here

Read the spec's **Binding Constraints** in full. In particular:

- **M42 gates M47.** No M47 epic may be dispatched agentically until this milestone closes. **A
  change to that order is an escalation, not a decision.**
- **M41's terminal epic is gated on this milestone's closure** too.
- **The tests are inverted, not deleted.**
- **`ai-project-init` is repaired on its own merits as a fail-open defect** — **not** as a
  governance-auto-update reconciler component. That work is split and **neither half is in P12.**
- **The fleet sweep enumerates.** Fixing only `social-stories-creator` is not the obligation.
- **A surviving permissive path must be declared AND recorded.**

---

## Three findings from planning that you must carry into the Epic specs

Measured by the Phase Chat by reading, on `master` at `9ee810e`, 2026-08-19. **They are in the spec
with their verification boundaries. Do not re-derive them; do not treat them as optional context.**

1. **G1 — `bin/ai-project-orchestrator` already defines the convention its Docker path violates.**
   `LOCAL_UNAVAILABLE_EXIT = 5` at `:36`, documented at `:31-35` as *"refuse loudly rather than retry
   or **silently fall back**"* — **a sentence that describes the defect** — and already applied at
   `:539-565` with a complete worked shape (state the reason, generate an escalation report, archive
   the trigger file, exit 5). **E42.1 applies the file's own convention. It does not invent one.**
2. **G2 — inverting the merge test is NOT sufficient.** `test_promote_branch_fallback_merge`'s mock
   has **`gh pr review --approve` returning 0**; it exercises the *ladder*, not the *approval
   bypass*. **The `:269` warning-and-continue path has no test at all.** **E42.3 owes a NEW test as
   well as an inverted one.**
3. **G3 — the blast radius is larger than the scoping states.** Not *"three guides"* — **six**
   (`ADOPTION-FAQ`, `ADOPTION-GUIDE`, `FAQ`, `gpu-coexistence`, `QUICK-START`, `visual-artifacts`),
   plus AOG, `chat-hierarchy.md`, `ai-project-yml-spec.md`, an adoption record, `README.md`, **seven
   other `bin/` scripts** and **seven test files** — and **Drivr, which is outside this repository
   and appears in no grep run here.** **That measurement is a NAME SWEEP; E42.5 owes the CALL
   GRAPH**, and owes an answer to *are these paths live?*

---

## Design decisions that are YOURS or your Epic Chats' — decide, document, proceed

The phase starter assigns these to this level explicitly. **Pick a direction, record the reasoning,
do not escalate:**

- **What "the epic's files" means for scoped staging, and what happens to out-of-scope
  modifications** — **E42.2's**, and the spec bounds the option space without answering it. **One
  thing is not open: the out-of-scope case must remain visible in the record.** `git add .` is
  rejected because it makes that case *indistinguishable* from a clean run, not because it is broad.
- **Whether the sandbox opt-in is a flag, a config key, or a per-run declaration** — **E42.1's.**
  Whichever shape: **the run record states the opt-in was taken.**
- **What the strengthened init validator asserts** — provenance, a marker, a checksum. E36.3's
  `sha256` freeze is available precedent and is **not** mandated.
- **How the `--auto` rung is disposed of** alongside `--admin` — kept or dropped, deliberately.

**Escalate instead of deciding:** anything that would change the M42→M47 order, the M42→E41.5 gate,
the invert-don't-delete rule, or the scope of the three obligations; and any finding that the
`P12-GH-2` diagnosis is **wrong** — that is a report to make loudly, not a scope to quietly shrink.

---

## Output Requirements

For each Epic, in order, **one set at a time**:

1. **Epic spec** — `docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12-M42-E42.<n>__spec__<epic-name>.md`,
   using `governance/templates/epic-spec.md`, covering: goals and scope; **the defect's verified
   file:line**; deliverables; the per-epic acceptance criteria from the milestone spec, expanded;
   dependencies and prerequisites (**including the ordering constraints and that M42 gates M47**);
   Definition of Done.
2. **Epic Execution Chat Starter** — `…/P12-M42-E42.<n>__epic-execution-chat-starter.md`, using
   `governance/templates/epic-execution-chat-starter.md`, recording **`Execution Mode: manual`** and
   `models.epic_manual`.

**Every Epic Execution Chat Starter you write must carry, in its own body:** the 3-attempt rework
rule with the **+1** extension semantics and the noted corpus conflict; the amendment-propagation
procedure above; and the Hard Constraint from the milestone spec — in particular **prove every guard
by falsifying it** (delete the guard, watch the test fail; the method B2.1 used) and **`--include='*.py'`
skips every `bin/` entry point, where all four defects live.**

**Hand off reference-first per AOG §3.1.1** — commit to `milestone/M42`, then emit the committed path
plus a one-line summary. **Do not echo artifact bodies into chat.** Use the fenced full-body fallback
only for a genuinely repo-less consumer.

After each set, **explicitly request Phase Chat review** before proceeding. Under PSG §11.6
default-accept, the Phase Chat accepts a clean set by silence.

---

## Epic Acceptance and Merge Instruction (SN-19 — in-chat, no artifact)

There is **no Epic Delivery Authorization artifact**. When the Phase Chat accepts an Epic's
deliverables — by silence on the happy path — acknowledge in-chat and proceed. The standing merge
instruction: **merge `epic/P12-M42-E42.<n>` to `milestone/M42` upon Epic completion, Phase Chat
acceptance, and explicit human merge authorization** (an in-chat act; the harness enforces it
regardless).

**An irony worth naming once, because your Epic Chats will meet it:** E42.3 removes or gates the
`--admin` override in the very script this project's tooling uses to promote branches. **Do not let
an epic route around its own fix.** If a merge in this milestone cannot be completed without the rung
being repaired, that is a finding to report, not a reason to defer the repair.

---

## Completion Requirements

This Milestone Chat session is complete when:

- [ ] An Epic spec and an Epic Execution Chat Starter exist and are accepted for all five Epics
- [ ] In-chat acceptance is acknowledged for each accepted set (SN-19 — no artifact)
- [ ] The Phase Chat has declared M42 planning complete

Upon completion, declare: *"Milestone P12-M42 planning complete. All Epic specs and Chat Starters
accepted. Session closed."*

Then proceed to Stage 2 — execution oversight — under the same rules.

---

## Question Policy

- **Ask only blocking questions.**
- Do not propose scope changes, add epics, or modify the ordering constraints. **M42 → M47 and
  M42 → E41.5 are binding** — a change to either is an escalation to the Phase Chat, not a decision.
- Do not ask for information already in the milestone spec or the `P12-GH-2` carry-forward note.
- **`P11-GH-2` applies to you:** state the layer, time and scope at which any claim was verified, and
  **honour the read-versus-run distinction** — that distinction is the whole reason Obligation 1
  exists.
- **G2 applies to you:** the executor's report is not the evidence. **Re-measure.** This Phase Chat
  re-measured HQ's figures and found three things that changed the work; expect the same of this
  spec's.
- **An absence is only evidence when the thing that would have created it actually ran.**

Escalate to the P12 Phase Chat for any gap not covered here.
