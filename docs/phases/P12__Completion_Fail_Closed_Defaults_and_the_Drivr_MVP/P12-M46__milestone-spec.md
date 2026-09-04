---
milestone: M46
name: "The Drivr MVP Surface"
phase: P12
status: planned
start_date: 2026-09-04
epics:
  - E46.1
  - E46.2
  - E46.3
  - E46.4
  - E46.5
is_final: false
---

# Milestone P12-M46 — The Drivr MVP Surface

## ⚠ THE ONE SENTENCE THIS MILESTONE IS ORGANIZED BY

> **A surface that *validates* a governance rule can be argued with; a surface that cannot
> *represent* the rule's violation has nothing to argue about — and M46's job is to move at least
> three rules from the first category to the second, on a board whose central verdict is now allowed
> to say "I don't know."**

---

## Why this milestone runs now, and not earlier

**M45 gates M46, and the gate was real rather than administrative.** The surface's two central
behaviours — *render what a run is doing* and *take the human to where attention belongs* — **are the
completion signal**. Building the board before M45 would have produced a window confidently
displaying a verdict the pre-E45.2 judgment could not support: every read-only run rendered as
`DID_NOT_COMPLETE`, which is a false red the operator would learn to ignore.

M45 handed over a **written, stable contract** — `docs/m46-completion-signal-contract.md`, on Drivr
`main` at `4872107` — and this milestone **builds against it and does not re-derive it.**

---

## Findings

### V1 — Names carry no role, and the impossibility argument that justified the registry is dead

**The requirement survives; its reasoning does not.** The M46 role-identification input was filed
2026-08-20 on the claim that role identity is *unreachable from inside the fleet by construction*.
On 2026-08-27 the harness moved: `ListAgents` now reports the calling session its own address. **A
session can state who it is.**

**What survives is the real requirement: a name carries no role.** A fleet still cannot determine
*who is HQ* or *who holds M41* from the roster alone. **M46 builds against "names carry no role",
never against "sessions cannot identify themselves"** — the second is false and a deliverable resting
on it would be false with it.

> **Why this finding is placed first.** The dead claim lived in messages for a week and **stopped at
> the artifact boundary** — it was never filed, so nothing had to be unwound. The M41 Milestone Chat
> caught it by **re-measuring at the moment of use**, one turn short of shipping a reply asserting it.
> **`P12-GH-3`'s most uncomfortable instance: not a document, not a branch, but a claim about the
> environment, made inside that environment.** Every epic here inherits the obligation to re-measure
> the harness claim it rests on, at the moment it rests on it.

*Verified by the Phase Chat against the phase spec's amended input, repo, `phase/P12` `cd1b490`,
2026-09-04.*

### V2 — A fork that agrees is invisible, and the record cannot settle it afterwards

Three live forks are on record. **The HQ fork was caught because it CONTRADICTED** — PR #226 declared
S5 unresolved three hours after the ruling merged, and a *reader* noticed two rulings disagreeing.
**The M41 fork AGREED**: same voice, same discipline, correct amendments, and it caught a defect the
incumbent missed. **There was no signal at all.** It surfaced only because the incumbent went to do
work already done and read the log first — **a habit, not a mechanism.**

**The property to design against:** *a fork that contradicts is detectable at merge; a fork that
agrees is invisible, and it silently doubles the write surface for a role.*

**Two consequences that narrow the remedy space, and the second rules out a class:**

**(a) Correctness is not safety.** A fork does not have to be wrong to be a problem, and being right
is not evidence it was safe. **A remedy evaluated against whether forks have produced bad output will
conclude there is no problem.**

**(b) A tie-break computed from the shared state is self-legitimizing.** Any rule of the form *"the
session whose commit most recently touched X holds the role"* makes the role **acquirable by the very
act it governs** — whoever writes last becomes the holder, so a mistaken write retroactively
legitimizes itself. **Exclusivity must be enforced by something outside the state the forks write**,
which is Drivr's side of the boundary, not the corpus's.

**And it cannot be repaired by reading the record.** Measured 2026-08-21:
`git log --all --format='%an <%ae>' | sort -u` returns **exactly one author** across the entire
repository, because the harness signs as the human. **The corpus cannot tell whether two artifacts in
one role came from one chat or two.**

### V3 — The board's contract already exists, is stable, and is not M46's to re-derive

`docs/m46-completion-signal-contract.md` (Drivr `main` `4872107`) names the layers, the three states,
the board vocabulary, and — explicitly — **what M46 may not do**: render `undetermined` as
`in progress` (fail-open) or as `blocked` (over-claim), fold it into `DONE`/`NOT_DONE` at render time,
or read the exit code, `status`, or the model's prose as a substitute signal.

**A change to that contract is a spec amendment with a changelog row, reviewed by the parent — not a
silent edit.** If M46 finds the contract wrong, that is an escalation, not a local fix.

*Verified by the Phase Chat: file present on Drivr `main` at `4872107`, §4 and §5 read directly,
2026-09-04.*

### V4 — Unrepresentable is a stronger claim than validated, and the phase spec asks for the stronger one

Success criterion 17 names **three** rules the surface must make unrepresentable: **no agentic at
Creation/HQ; no Phase/Milestone dispatch; no mode control implying merge authority.**

**A validated rule is a rule the interface can express and then reject.** It leaves a code path where
the forbidden state exists and something must notice. **An unrepresentable rule has no such path** —
the state cannot be constructed, so no check can be forgotten, disabled, or raced. **This milestone's
deliverable is the absence of a control, and absence is hard to demonstrate**, so each of the three
must be shown by a test that fails if the state becomes constructible.

> **This is the phase's organizing finding inverted for once.** Everywhere else in P12, *absent
> evidence let an action proceed*. Here, **absent capability is the safety property** — and the risk
> is the mirror image: an absence that is merely undocumented today and re-added tomorrow by someone
> who did not know it was load-bearing.

### V5 — The qualification bar must be committed before the suite it grades, and M45 proved the form works

SN-37's gate must **detect *successful nothing*** — a run that returns a confident verdict having
done nothing — **on both recorded historical failures**: the `epic_qa` dispatch that returned
`VERDICT: PASS` with **zero tool rounds** while citing a `framework_version` key the file does not
have (P11-M39-E39.3), and the four-times-overpacked `llama3.1:8b` observation (P12-M41-E41.1).

**E45.1 is the worked precedent and the reason its result is citable:** it committed the bar as the
**first commit on its branch** (`da0c66a`, verified by the Phase Chat), then measured against it.
**A bar written after the measurement grades the measurement it was written from.**

---

## Binding Constraints (settled — NOT for re-debate)

1. **The completion-signal contract is an input, not a subject.** Build against
   `docs/m46-completion-signal-contract.md` as it stands. Disagreement escalates.
2. **`undetermined` is rendered as `undetermined`.** Never as `in progress`, never as `blocked`,
   never folded into a terminal state at render time.
3. **The exit code, `status`, and model prose are refused as load-bearing signals** — measured
   unreliable on this stack (E39.1, P10-GH-7 re-rated by E45.3).
4. **Exclusivity is enforced outside the state the forks write.** No tie-break derived from artifacts
   both forks mutate (V2b). No form resting on implicit `HEAD`.
5. **Three rules unrepresentable, not merely validated** (V4), each with a test that fails if the
   forbidden state becomes constructible.
6. **The qualification bar is committed before the suite runs** (V5), as its own commit, checkable by
   `git log` from the branch point.
7. **Mode is not authority.** No control may imply that switching execution mode grants merge
   authority (SN-25, ratified matrix).
8. **Escalation terminates one level up** (SN-25). The escalate-further control is one-level, not a
   broadcast.
9. **Drivr work is not complete until it is on Drivr `main`.** A DoD item measured only on an epic
   branch is **not met** — the M43/M45 defect, which recurred once and will not recur here.

---

## Epics

Five epics. **E46.1 runs first** — the registry is a prerequisite for the auto-open and
go-to-blocker behaviours, not a convenience. **E46.5 sets its bar first** within its own branch.

### E46.1 — The role registry and exclusivity *(FIRST — prerequisite)*

**Organizing question: how does Drivr know which session holds a role, and that exactly one does?**

**Deliverables**

1. **A role registry** mapping a governance role (`hq`, `phase`, `milestone/M<n>`, `epic/<id>`) to the
   session address that holds it, owned by **Drivr**, since Drivr opens the chats. Built against
   *names carry no role* (V1) — a session can state its address; nothing states its role.
2. **An exclusivity mechanism** enforced **outside** the state the forks write (V2b), such that a
   second session claiming a held role is **detected at claim time**, not at merge, and not by a
   reader.
3. **The agreeing-fork case addressed explicitly** — the remedy must work when the second session is
   correct, well-behaved, and produces converging output (V2a).

**Acceptance criteria**

- [ ] A role maps to exactly one session address, and a second claimant is refused or flagged **at
      claim time**
- [ ] The mechanism does not rest on any artifact both forks can write, nor on implicit `HEAD`
- [ ] The agreeing-fork case is demonstrated, not just the contradicting one
- [ ] No claim rests on *"sessions cannot identify themselves"* (V1 — false since 2026-08-27)

### E46.2 — The board, and `undetermined` rendered

**Organizing question: what does the operator see, and can the interface show a verdict the signal
cannot support?**

**Deliverables**

1. **The board**, rendering each project's Phase/Milestone/Epic and each run's state in the
   contract's vocabulary — `queued` / `in progress` / `undetermined` plus the determinate terminals.
2. **A guard that fails if `undetermined` is rendered as anything else**, mirroring on the render side
   the no-fold guard E45.4 built on the consumer side.
3. **The post-fix rate visible** — the board shows the size of the problem, which is the pressure that
   keeps the phase honest (E45.4 D4).

**Acceptance criteria**

- [ ] `Conclusion.UNDETERMINED` renders as `undetermined` and as nothing else
- [ ] A render-side fold fails a test, falsified in both directions
- [ ] No render path reads the exit code, `status`, or model prose (BC3)

### E46.3 — Three governance rules made unrepresentable

**Organizing question: which states can the interface simply not construct?**

**Deliverables**

1. **No agentic at Creation/HQ** — the control does not exist for those levels.
2. **No Phase/Milestone dispatch** — the surface offers no path to dispatch at those levels.
3. **No mode control implying merge authority** — mode is not authority (BC7).
4. **For each: a test that fails if the state becomes constructible** (V4) — absence demonstrated,
   not asserted.

**Acceptance criteria**

- [ ] Three rules named, each unrepresentable rather than validated
- [ ] Each has a test that fails when the forbidden state is made constructible again
- [ ] The distinction between *rejected* and *unrepresentable* is stated in the record

### E46.4 — Approval formed in chat, carried by link; escalate-further as one level

**Organizing question: how does a human authorize, and how far does an escalation travel?**

**Deliverables**

1. **Approval formed in chat and carried by a signed one-time link** — never a chat reply as the
   authorization itself (P11 spine; inbound approval must be a signed one-time link).
2. **Escalate-further as a one-level control** terminating at the immediate parent (SN-25), not a
   broadcast and not a jump to the human.
3. **The go-to-blocker affordance**, which depends on E46.1's registry.

**Acceptance criteria**

- [ ] An approval cannot be given by a chat reply alone
- [ ] Escalation moves exactly one level; the terminus is stated
- [ ] Go-to-blocker resolves through the registry, not a guess

### E46.5 — SN-37's qualification gate, bar committed first

**Organizing question: what would make a model swap safe, stated before any model is graded?**

**Deliverables**

1. **The bar, as the first commit on the branch** (V5, BC6) — the pass conditions for a model swap,
   written before the suite runs.
2. **The qualification suite**, which a model must pass before it may be swapped in.
3. **Detection of *successful nothing* on both recorded historical failures** — the zero-tool-round
   `VERDICT: PASS` citing a non-existent key, and the `llama3.1:8b` overpack.

**Acceptance criteria**

- [ ] The bar is the first commit on the branch, shown by `git log` from the branch point
- [ ] Both historical failures are detected by the suite, each named and cited
- [ ] A model that has not passed cannot be swapped in — enforced, not documented

---

## Definition of Done

- [ ] All five epics delivered, accepted, and merged to `milestone/M46`
- [ ] **A role maps to one session, and a second claimant is caught at claim time** (E46.1)
- [ ] **`undetermined` is rendered as itself**, with a render-side no-fold guard (E46.2)
- [ ] **Three governance rules are unrepresentable**, each with a constructibility test (E46.3)
- [ ] **Approval is carried by signed one-time link; escalation is one level** (E46.4)
- [ ] **The qualification bar was committed before the suite**, and both historical failures are
      detected (E46.5)
- [ ] **Every Drivr deliverable is on Drivr `main`**, not only on an epic branch (BC9)
- [ ] Every claim states the layer, repository, ref and date (`P11-GH-2`)
- [ ] No deliverable states a coverage count where a list belongs
- [ ] Suites green, each named with its repository and invocation; the `ai-project-system` count
      stated as **environment-dependent** (`766+1 skipped` / `767` / `766+1 failed` are the same suite)
- [ ] Milestone Closure Declaration committed, `is_final: false`

## Acceptance Criteria (Milestone)

- [ ] **The surface cannot express a governance violation** for the three named rules — a reader can
      say why the state is unconstructible, not merely rejected
- [ ] **The board tells the truth about not knowing** — `undetermined` is visible, distinct, and never
      rendered as a neighbour
- [ ] **A role has one holder, and the mechanism works against an agreeing fork**
- [ ] **The qualification bar was set before it graded anything**, and detects successful nothing on
      both recorded cases
- [ ] **Nothing this milestone declares complete lives only on an epic branch**

## Dependencies

- **M45 (gate, satisfied)** — `docs/m46-completion-signal-contract.md`, Drivr `main` `4872107`
- **SN-36** — the visual binding (the Drivr Window mockup)
- **SN-37** — the model-qualification gate
- **SN-25** — one-level escalation; the terminus of the escalate-further control
- **P11 spine** — inbound approval is a signed one-time link, never a chat reply

## Execution Notes

- **Execution Mode: `manual`.** The surface governs agentic dispatch; building it agentically would
  have the mechanism under repair reporting on its own repair — the circularity M41, M42 and M45 all
  refuse.
- **Two repositories.** Most deliverables land in **Drivr**; `ai-project-system`'s suite does not
  cover them. State the repository of every deliverable, and **finish on `main`** (BC9).
- **Re-measure the harness claim you rest on, at the moment you rest on it** (V1).

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-09-04 | Initial M46 spec, from the P12 phase spec's P12.6 and success criteria 17/18, the M46 role-identification and currency inputs (amended four times, three of them from live forks), and M45's handover contract. Five epics; **E46.1 first** as a prerequisite. Records **V1** (the impossibility argument is dead, the requirement survives), **V2** (a fork that agrees is invisible; exclusivity must live outside the state the forks write; the corpus cannot settle it because the harness signs every commit as one author), **V3** (the contract is an input, not a subject), **V4** (unrepresentable is a stronger claim than validated, and absence needs a constructibility test), **V5** (the bar precedes the suite, per E45.1's worked precedent). **BC9 binds the M43/M45 defect**: a Drivr DoD item measured only on an epic branch is not met. |
