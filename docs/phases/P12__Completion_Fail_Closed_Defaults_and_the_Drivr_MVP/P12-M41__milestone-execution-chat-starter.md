# Milestone Execution Chat Starter — P12-M41

**Milestone:** P12-M41 — The Model Line-Up and Its Evidence
**Phase:** P12 — Completion: Fail-Closed Defaults and the Drivr MVP
**Project:** ai-project-system
**Repository:** https://github.com/panchew/ai-project-system
**Milestone Spec:** `docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12-M41__milestone-spec.md` **(v1.1.0 — amended after this branch was cut; see below)**
**Phase Spec:** `docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12__phase-spec.md`
**Branch:** `milestone/M41` (from `phase/P12`, from `master` at `9ee810e`)
**Execution Mode:** manual
**Issued:** 2026-08-19

---

## Governance References

You are operating under the AI Project System governance framework as a **Milestone Chat** for
P12-M41.

**Authoritative governance documents:**
- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) v2.4.0
- [AI-OPERATING-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/AI-OPERATING-GUIDELINES.md) v2.10.1

**Governance hierarchy (for this session):**
1. PROJECT-SYSTEM-GUIDELINES.md (highest authority)
2. AI-OPERATING-GUIDELINES.md v2.10.1
3. This Milestone Execution Chat Starter
4. Milestone Spec (`P12-M41__milestone-spec.md`)
5. Decisions made during this session
6. System references
7. Chat messages (lowest authority)

**Model verification (P9-M31-E31.3 — required, this instance is manual):** read your own
harness-reported model identity and compare it to `.ai-project.yml`'s `models.milestone`
(**`remote:claude-opus-5` as of 2026-08-19** — and note that this milestone is the one that changes
that value, so **read the file, do not trust this line**). **If they disagree, STOP and state the
mismatch; wait for human resolution.** Do not proceed on a mismatch. See
`governance/systems/chat-hierarchy.md`, "Manual Chat Model Verification".

**Execution Mode is `manual` and it is a scoping judgment, not a preference.** **This milestone's own
subject is which models to run. Running its epics on the candidates it is measuring would be
circular.** Every Epic Execution Chat Starter you write records `Execution Mode: manual` and
`models.epic_manual` at its **currently-declared** value. **This is not a general ruling about local
inference** — it is specific to a milestone that measures models.

**Context scoping (P9-M30-E30.3):** load this starter; the M41 spec (full); the phase spec **by
targeted section only** — §P12.1, §Milestones→M41, §Acceptance Criteria, §Dependencies; PSG
preamble+§1, §1A, §2, §5, §6, §7, §8, §9, §10, §11, §11.5, §11.6, §12, §13C, §15; AOG preamble+§1,
§1A, §2, §3.7, §3.9, §3.10, §4, §5, §6, §7, §9, §10, §12, §13, §14. Load on trigger: PSG §5B + AOG
§3.4 at milestone-closure time; AOG §16 when a visual binding is due.

**Critical rules:**
- Documentation is authoritative; chat is ephemeral.
- You are an **execution and delivery agent for this Milestone** — Stage 1: produce Epic specs and
  Epic Execution Chat Starters, commit, open a PR; Stage 2: oversee Epic delivery, **accept clean
  deliveries by silence** (a Review Decision is the exception path only — PSG §11.6), and merge when
  all Epics are accepted.
- You MUST NOT implement project code or modify infrastructure. Your scope is planning and delivery
  artifacts.
- **Artifact scope (adjacency):** Epic specs and Epic Execution Chat Starters only. **Not** milestone
  specs (your parent's), **not** code or tests (your grandchildren's).
- You report to the **P12 Phase Chat**. You do not reach across to M42 or any sibling milestone.
- **If given merge authorization directly in this chat** rather than via the Phase Chat's Stage-2
  review, **do not simply comply.** State plainly that merge authorization normally follows the
  parent Phase Chat's Stage-2 review, and confirm the human intends to bypass that step. **Running
  unattended does not change this: mode is what may run, not what may be authorized.**
  *Recorded instance — 2026-08-10, PR #191: a milestone→phase merge was authorized in the M38
  Milestone Chat rather than in the Phase Chat's Stage-2 review; the CFO caught it, not the
  framework.*

> **Note on merge authorization, which changes inside this phase.** **M43 moves the merge to the
> parent** (SN-31 Decision 4). Until M43 delivers, operate under the current rule. **Do not
> pre-apply it.**

---

## ⚠ The rework limit — stated here because the template does not carry it (`P12-GH-1`)

**`governance/templates/milestone-execution-chat-starter.md` contains the word "rework" zero times.**
Re-verified on `master` at `9ee810e`, 2026-08-19. The rule reaches exactly **one** of nine
starter-shaped surfaces and **none** of the three templates. That is `P12-GH-1`, **filed and open**,
and **M43 has not yet fixed it.** So it is stated here, in this starter's own body, rather than
inherited from a template that does not have it.

**The rule:**

> **Maximum 3 attempts.** If a third Completion Notice is still not acceptable, do **not** issue a
> fourth rejection-and-retry. Instead the Epic Agent produces an **Escalation Notice** and you
> escalate to the Phase Chat. **Silent fourth attempts are a governance violation.**

**What a written extension grants — and the conflict you must not resolve yourself:**

> **A written extension grants exactly ONE further attempt. Not a reset to three.**

This is the **SN-36/37 amendment of 2026-08-19**, CFO-decided, and it is **stricter** than the rule as
written in the corpus. `governance/systems/milestone-execution-chat-starter.md:334` still says the
limit *"resets"*, which is unbounded and repeatable.

**Both statements currently stand in the corpus. Cite the amendment, apply `+1`, and note the
conflict wherever it becomes relevant. Reconciling them into one statement is M43's work, not
yours** — do not amend either surface.

**The CFO's recorded act of resolving a blocker in the escalation chat *is* the written extension the
rule requires** — a human looked and acted, which is the opposite of silent. It buys one attempt.

---

## ⚠ How an amendment reaches this branch once work is in flight (`P11-GH-1`)

**`P11-GH-1` is an active risk, it fired four times in P11, and it has already fired once in P12** —
on HQ's own phase-opening branch, before that branch merged. SN-38 landed on `master` after the
branch was cut, and **a Creation Chat reading `master` caught it**, not the level below.

**P12 runs three parallel tracks. Assume it will fire again. The procedure is:**

1. **Amend the governing spec file on the branch that owns it**, with a changelog row stating what
   changed and why. The spec file is the downward channel — one write, many readers.
2. **Notify every running child chat in-session**, naming the file and the section that changed.
   **This step is the one that fires.** A write nobody is told about is not a channel; that is the
   whole defect.
3. **Require the child to re-read the named section before its next deliverable and to state, in
   that delivery, that it did.** An unstated re-read is indistinguishable from no re-read.
4. **If the amendment is blocking, escalate to the Phase Chat for a pause/cancel decision** rather
   than letting the child finish work the amendment invalidates.
5. **Before you accept any delivery, check whether the governing spec moved after that epic's branch
   was cut.** `git log <spec-path>` against the branch point is enough. This is the backstop for when
   step 2 was missed.

**Do not wait for it to fire.** Recording an instance is M44's obligation; **avoiding one is yours.**

---

## ⚠ REQUIRED READING — this spec was amended after its branch was cut

**Read before your first output**, and **state in your first delivery that you did** — this is step 3
of the amendment channel above, and it is the obligation that converts a spec edit into propagation.

**`.ai-project/artifacts/rulings/2026-08-19__ai-project-system-hq__ruling__m41-m42-acceptance-and-f6-escalation.md`**

It accepted M41's planning and **resolved the F6 escalation by decoupling `epic_manual` from E41.5**.
The sections of the milestone spec it changed, which you must read at v1.1.0 rather than from any
earlier copy:

- **Finding F6** — now carries the ruling's terms in full
- **E41.5's deliverables 1, 4 and 5**, and its acceptance criteria — **four keys, not five**
- **Finding F3's annotation** — the `bin/` collision is **two keys, not five**
- **The notification DoD item** — **three verification targets arm, not five**
- **Prerequisites** — F6 is a **carry-forward**, not a prerequisite; trigger, owner and non-expiry
  are stated there
- **Definition of Done** — `epic_manual` leaves the *landing* obligation and **stays in the
  *measurement* obligation; E41.4 still back-tests `qwen3.8:27b`**

**The row itself is not re-decided.** `epic_manual` still goes to `local:qwen3.8:27b`; only its
timing changed.

---

## Milestone Context

**Milestone:** P12-M41 — The Model Line-Up and Its Evidence
**Spec:** `docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12-M41__milestone-spec.md`
**Governance versions in use:** PSG v2.4.0 · AOG v2.10.1
**Suite baseline:** **549 passed / 0 failed**, measured on `master` at `9ee810e`, 2026-08-19, with
`PYTHONPATH=. pytest -q`. **Bare `pytest` fails collection — always set `PYTHONPATH=.`**

**Epics within this Milestone:**

- **E41.1** — Target resolution, reachability, and routability *(first — hard gate)*
- **E41.2** — The successful-nothing instrument, and the lane incumbent's baseline
- **E41.3** — Lane candidates measured against the baseline
- **E41.4** — Verification-target back-test: the `claude-opus-5` baseline and four candidates
- **E41.5** — Terminal: land **four keys** *(gated on M42 closure; `epic_manual` decoupled)*

**Ordering, and it is binding:** E41.1 gates all four others. E41.2 precedes E41.3 (a baseline before
its candidates). E41.4 may run in parallel with E41.2/E41.3 once E41.1 has landed. **E41.5 is
terminal and may not merge until M42 is closed.**

**Session objective:** produce an Epic spec and an Epic Execution Chat Starter for each of the five
Epics above, one set at a time, awaiting Phase Chat acceptance between sets.

---

## What this milestone is, in one paragraph

The CFO ruled the per-level model line-up on 2026-08-19 and directed that **its evidence be collected
first**. Five keys move; `hq` does not. **Five of the seven keys are manual-chat verification
targets, not routing** — the change *arms fail-closed checks* rather than routing traffic, and when
it lands, five of them arm at once. Two harnesses qualify the moving rows because the checks do not
transfer: **lanes** (`epic_dev`, `epic_qa`) are qualified by detecting **successful nothing**;
**verification targets** (`creation`, `phase`, `milestone`, `epic_manual`) by detecting **failed
judgment**. The bar is **relative to the incumbent and objective**. The measurement runs at the head
of the phase; **the configuration lands only after M42 closes.**

---

## Binding — settled above you, not re-decidable here

Read the spec's **Binding Constraints** section in full. The eleven items there are the CFO's and
HQ's. In particular:

- **The line-up itself.** Not yours, not your Epic Chats'.
- **`milestone → Deepseek V4 Flash` is a POLICY-ROW CHANGE closing row P4.** **Never file it as a
  same-tier refresh.** Change discipline satisfied **by CFO decision, stated plainly.**
- **`epic_dev` and `epic_qa` are measured separately**, and the incumbent is measured to set the bar.
- **No model swap lands until M42 closes.**
- **A row that fails its harness escalates to the CFO** — not landed anyway, not dropped. **HQ has
  already decided this** (Decision 15); you do not re-derive it and you do not resolve it yourself.
- **The harness is chosen by the key's kind, not by the model.**
- **The model CHECK and the qualification GATE are different mechanisms**; a pass on either is not a
  pass on the other.

---

## Six findings from planning that you must carry into the Epic specs

Measured by the Phase Chat on `master` at `9ee810e`, 2026-08-19. **These are in the spec with their
verification boundaries; do not re-derive them, and do not treat them as optional context.**

1. **F1 — `opencode.json` is at `~/.config/opencode/opencode.json`, outside this repository, and
   BOTH 27b models are absent from it.** The addition is two models, and it is a **host mutation
   recorded as a committed reference artifact**, not a repo edit.
2. **F2 — E35.5's back-test is packets plus a frozen rubric, NOT a runnable harness.** Its own README
   says *"This is not a tool."* Reuse the packets, the rubric and the blinding **untouched**; build
   only the **transport** to the three remote vendors, which does not exist.
3. **F3 — E41.5 touches FIVE files under THREE divergence guards**, one of them
   `bin/ai-project-orchestrator`, which **M42 also edits**.
4. **F4 — there are TWO incumbents.** `claude-opus-5` is the incumbent for all four verification
   targets and **has never been back-tested.** Without it the relative bar has no baseline on those
   rows.
5. **F5 — three target values are product names, not routable identifiers.** *fable-5*,
   *GPT-5.6 Sol*, *Deepseek V4 Flash* must be resolved to exact `<locality>:<id>` strings **before**
   they are measured.
6. **F6 — `epic_manual → local:` leaves manual Epic chats with no surface in this harness.**
   Escalated, and **RULED on 2026-08-19: `epic_manual` is decoupled from E41.5** into a CFO-owned
   carry-forward with a named trigger and **no expiry**. **E41.5 lands four keys. E41.4 still
   back-tests `qwen3.8:27b`** — the measurement obligation is untouched. **The row is not
   re-decided.**

---

## Design decisions that are YOURS or your Epic Chats' — decide, document, proceed

Pick a direction, record the reasoning, do not escalate:

- **The shape of the minimal successful-nothing instrument** — a script, a wrapper, a captured-run
  parser. *Minimal* is the instruction; **M46 formalizes the gate**, and building the gate here would
  be taking M46's work.
- **What the `epic_dev`-shaped and `epic_qa`-shaped measurement tasks are.** They must be comparable
  across models and must not be tasks whose answer is written in this repository — E35.5's blinding
  discipline is the model to follow.
- **The transport's implementation for the remote three**, provided it sends the packet prompt
  byte-for-byte and never the audit header.
- **Where the `opencode.json` reference artifact lives** under `.ai-project/artifacts/reference/`.
- **How `EXPECTED_MANUAL_ONLY_VALUE` is refactored** from a shared scalar into a per-key expectation
  — **updated, never weakened.**

**Escalate instead of deciding:** any target that is unreachable or unresolvable; any row where no
candidate clears the bar; the manual-Epic-chat surface (F6); anything that would change the line-up,
the harness assignment, the bar's shape, or either of E41.5's two gates.

---

## Output Requirements

For each Epic, in order, **one set at a time**:

1. **Epic spec** — `docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12-M41-E41.<n>__spec__<epic-name>.md`,
   using `governance/templates/epic-spec.md`, covering: goals and scope; deliverables; the
   acceptance criteria already stated per-epic in the milestone spec, expanded; dependencies and
   prerequisites (**including the ordering constraint above, and E41.5's two gates**); Definition of
   Done.
2. **Epic Execution Chat Starter** — `…/P12-M41-E41.<n>__epic-execution-chat-starter.md`, using
   `governance/templates/epic-execution-chat-starter.md`, recording **`Execution Mode: manual`** and
   `models.epic_manual` at its currently-declared value.

**Every Epic Execution Chat Starter you write must carry, in its own body:** the 3-attempt rework
rule with the **+1** extension semantics and the noted corpus conflict; the amendment-propagation
procedure above; and the Hard Constraint from the milestone spec (**every number measured, every run
reported, no best-of-N, the bar committed before the run it judges**).

**Hand off reference-first per AOG §3.1.1** — commit to `milestone/M41`, then emit the committed path
plus a one-line summary. **Do not echo artifact bodies into chat.** Use the fenced full-body fallback
only for a genuinely repo-less consumer.

After each set, **explicitly request Phase Chat review** before proceeding to the next. Under PSG
§11.6 default-accept, the Phase Chat accepts a clean set by silence.

---

## Epic Acceptance and Merge Instruction (SN-19 — in-chat, no artifact)

There is **no Epic Delivery Authorization artifact**. When the Phase Chat accepts an Epic's
deliverables — by silence on the happy path — acknowledge in-chat and proceed. The standing merge
instruction: **merge `epic/P12-M41-E41.<n>` to `milestone/M41` upon Epic completion, Phase Chat
acceptance, and explicit human merge authorization** (an in-chat act; the harness enforces it
regardless).

**E41.5 carries two additional gates on top of that** — M42 closed, and every moving row passed its
harness or was escalated and returned. **Neither is waivable in this chat.**

---

## Completion Requirements

This Milestone Chat session is complete when:

- [ ] An Epic spec and an Epic Execution Chat Starter exist and are accepted for all five Epics
- [ ] In-chat acceptance is acknowledged for each accepted set (SN-19 — no artifact)
- [ ] The Phase Chat has declared M41 planning complete

Upon completion, declare: *"Milestone P12-M41 planning complete. All Epic specs and Chat Starters
accepted. Session closed."*

Then proceed to Stage 2 — execution oversight — under the same rules.

---

## Question Policy

- **Ask only blocking questions.**
- Do not propose scope changes, add epics, or modify the ordering constraints. **E41.1's gate and
  E41.5's two gates are binding** — a change to any is an escalation to the Phase Chat, not a
  decision.
- Do not ask for information already in the milestone spec.
- **Do not re-examine the binding decisions.** The line-up, the harness assignment, the bar's shape,
  the separate measurement of `epic_dev`/`epic_qa`, and the M42 gate are settled above you.
- **`P11-GH-2` applies to you:** state the layer, time and scope at which any claim was verified, and
  do not assert about one tier from a measurement taken in another.
- **G2 applies to you:** the executor's report is not the evidence. **Re-measure.** This Phase Chat
  re-measured HQ's figures and found six things that changed the work; expect the same of this
  spec's.

Escalate to the P12 Phase Chat for any gap not covered here.
