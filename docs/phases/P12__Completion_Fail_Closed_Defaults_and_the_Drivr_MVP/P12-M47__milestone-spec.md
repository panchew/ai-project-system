---
milestone: M47
name: "First Real Agentic Integration"
phase: P12
status: planned
start_date: 2026-09-01
epics:
  - E47.1
  - E47.2
  - E47.3
is_final: false
---

# Milestone M47 — First Real Agentic Integration

## Purpose

**Eleven phases built a governance framework and a coordinator for it. None of them used it.** The
CFO's words, recorded in SN-31: *"just doing some testing and measuring does not count as being using
it already."*

**M47 is the phase's proof and the reason the other six exist.** One real epic, in one real project,
carried end to end agentically by Drivr — dispatched, executed, completion-judged, gated, escalated
if it blocks, handed back to its parent, merged by its parent. **Not a measurement run and not a
demo: work that would have been done anyway, done this way instead.**

This milestone ensures:

- **Remote agentic dispatch exists**, or its absence is escalated as a justified milestone rather
  than absorbed silently.
- **A real project is selected on recorded reasoning**, and is actually ready.
- **The run is checked by an instrument rather than by its own report** — and the record says what
  the framework got wrong.

---

## Problem Statement

**The claim M47 must support is not "a real epic ran agentically end to end."** It is:

> **"A real epic ran agentically end to end — AND WE CAN SHOW IT DID WORK."**

**Those come apart, and in this project they usually have.** Three recorded cases where the first was
true and the second false: **E33.2 Run A** (exit 0, 0 tool rounds, nothing produced), **E39.3**
(`VERDICT: PASS`, zero rounds, citing a key the file does not contain), and **E41.2's DEV RUN 2**
(exit 0, 4.2s, stub byte-identical, six tools genuinely advertised).

**That is not a hypothetical risk. It is the modal outcome of this project's agentic dispatches so
far** — and it is why HQ placed the instrument check as an acceptance criterion rather than as
advice.

---

## ⚠ Findings measured at planning time — five

**Measured by the Phase Chat, 2026-08-27 → 2026-09-01, against `origin/phase/P12`, Drivr `f60164c`,
and the fleet on this host.** Verification boundaries stated per `P11-GH-2`.

### Z1 — SN-42 is sized **M47-sized**, on evidence, with a flip trigger

**The CFO's preference is extension over an eighth milestone, and HQ's warning was that a preference
must not decide a size:** *if the work is milestone-sized and gets compressed into M47 to honour a
preference, M47 carries two objectives and proves neither.* **So it was measured.**

| | |
|---|---|
| **This repository cannot dispatch remote** | `bin/run-dev-agent:114` gates the entire path on `local:`; `:109` states a `remote:`-prefixed model *"has no local endpoint to check"*; `discover_runner()` requires the `local-agent-runner` binary |
| **Drivr's adapter is genuinely provider-generic** | `opencode.py:164` partitions `provider/model`; **an unknown provider hits an early `return config`, not an error**; `build_argv` passes the model string straight to `opencode run --model` |
| **The Ollama coupling is an enhancement, not a requirement** | `ollama_endpoint` serves **context-limit observation**, not dispatch |
| **M47's own text** | *"end to end **through Drivr**"* — never through `bin/` |

**So the capability M47 needs may already exist on the path M47 was always specified to use, and the
gap looks like credential and configuration plumbing rather than machinery to build.**

> **NOT ESTABLISHED, and it is what would flip this: no remote dispatch has been run.** A
> provider-generic **code shape** is not a **completed dispatch**, and the `XDG_DATA_HOME` defect is
> live.
>
> **FLIP TRIGGER — a bar, not a hope: if remote dispatch requires new machinery rather than
> configuration, that is the justified escalation and it becomes its own milestone.** E47.1 answers
> it first, before anything depends on the answer.

### Z2 — Transport and dispatch **share a substrate and split at the loop**

Raised by the M41 Milestone Chat as *"E41.4's U2 and SN-42 may be one piece of work."* **Refined
rather than adopted:**

| | E41.4's transport (done) | M47's dispatch |
|---|---|---|
| Reach a remote provider, authenticate, send, receive | needed | needed |
| **Agentic loop — tool calls, execution, iteration** | **not needed** | **the whole point** |

**The decisive fact is E41.4's own T1:** E35.5's back-test is **single-turn and tool-free**
(`judgment.md` caution 4) — *"no follow-up, no repo access, no ability to check a claim against a
file."* **It sends a packet and scores text. It never needs a tool call.**

**So M41 already established the shared substrate** — credentials, provider config, reachability, on
three remote engines. **M47 INHERITS it and must not rebuild it.** What remains genuinely new is the
**loop**.

### Z3 — The candidate-project list in the phase spec is **stale**, and the live candidate has a blocker

The phase spec names *"the proving pair (`home_finance`, `local-agent-runner`) and Drivr itself"*.
**Re-surveyed on this host:**

| Project | State |
|---|---|
| `home_finance` | v7.0.0, stalled on `epic/E1.1`, **last commit 2026-07-20** |
| `local-agent-runner` | v7.0.0, **last commit 2026-07-20**, dirty tree — **and it owns the unowned parse defect** |
| **`panchew-io`** | **v7.1.0, clean, active 2026-08-23, on `milestone/M1` with FIVE planned epics — spec and starter committed for each** |

**`panchew-io` is the only fleet project with real, current, in-flight epic work** — which is exactly
the condition HQ warned M47 might not find: *"the only milestone whose success depends on a real
project having real work available at the right moment."*

> **⚠ AND IT CANNOT DISPATCH TODAY.** `panchew-io/.ai-project.yml` has **only `governance:` and
> `project:`** — **zero occurrences of `models`.** Agentic dispatch needs `models.epic_dev` /
> `models.epic_qa`. **Verified rather than inferred from a silent grep.**

**Cheap to fix, and it is exactly the kind of gap that otherwise surfaces at dispatch time — which
for M47 means inside the phase's own proof run.** **Project selection remains the CFO's**; this is a
survey with evidence, not a choice.

### Z4 — The acceptance instrument **exists and is tested. Nothing is to be built**

`bin/successful-nothing-instrument` and `tests/test_successful_nothing_instrument.py`, delivered by
E41.2, **+20 tests, suite at 569.** It was **validated in both directions** — three recorded failures
flagged, **two negative controls passed** — and then **caught a live successful-nothing on the
incumbent that it was not built against.**

**A replay set can be fitted to its own cases. A live catch cannot.** That is why HQ made it M47's
criterion rather than a suggestion.

### Z5 — The routing choice decides **which defects M47 inherits**, not only whether it can dispatch

**This is the finding that most changes E47.1's shape**, and it does not appear in the phase spec.

- **Route via `bin/run-dev-agent` → `local-agent-runner`:** inherits **the unowned `<function=…>`
  parse defect** at `local_agent_runner/tool_calls.py:171`, in a **third repository**, reachable by
  neither M42 nor M47. **That defect produced DEV RUN 2 — one of the three cases M47's criterion
  exists to catch.**
- **Route via Drivr's OpenCode adapter:** **does not inherit it** — different engine, different
  parser. **Inherits instead the `XDG_DATA_HOME` credential defect**, which is known, located, and
  has a stated repair.

> **So E47.1 is not only "can we dispatch remotely." It is "by which path, and what does that path
> already carry."** A route that dispatches successfully while inheriting a defect that manufactures
> false successes **would produce exactly the run M47's criterion is designed to reject.**

---

## Binding Constraints (settled — NOT for re-debate)

1. **M42 is a hard prerequisite — SATISFIED.** No M47 epic may be dispatched agentically until M42
   closes (SN-31 Decision 2). **M42 CLOSED 2026-09-02** — Closure Declaration accepted by the Phase Chat, consolidated to `phase/P12` by PR #248 (merge `90335ca`), `status: completed`. All four defects re-measured gone at acceptance (host `shell=True` fallback, unscoped `git add .`, the `--admin` rung, the placeholder-agent stub); suite `582` at closure.
   **The prerequisite is discharged; dispatch is no longer blocked on it.**
2. **The proof run is checked by `bin/successful-nothing-instrument`** — HQ acceptance criterion. The
   record carries **tool rounds, files changed and claims-resolution**, not an exit status.
3. **The claim is *"and we can show it did work."*** Not *"it ran."*
4. **Project selection is the CFO's**, recorded with reasoning.
5. **SN-42 extends M47 by default; a new milestone is a justified escalation** — the bar is the
   work's size, not tidiness. **Z1's flip trigger is the test.**
6. **The run record is the deliverable, including what the framework got wrong.** **A clean run that
   surfaced nothing is a weaker result than one that surfaced a real defect**, and this milestone is
   scoped to say so in advance.

---

## Hard Constraint (binding — carries to every Epic)

**M47 is the one milestone that can pass by accident.**

- **Never accept the lane's own report of itself.** Exit codes are measured-unreliable **in both
  directions** on this stack — E33.2 Run A exited 0 having done nothing; E33.4 exited 2 having done
  complete, green work.
- **Zero credentials is `UNDETERMINED`, never *unreachable*** — and record the effective credential
  path per dispatch. A confined `XDG_DATA_HOME` reports **every** remote target unreachable at once.
- **Inherit the substrate; do not rebuild it.** M41 established transport on three remote engines.
- **State the repository.** This milestone spans this repo, Drivr, the selected project, and possibly
  `local-agent-runner`. **"Suite green" covers one of them.**
- **A run that surfaces a real defect is a SUCCESS.** The deliverable is the record, not a green tick.

---

## Planned Epics

Three. **E47.1 is a hard gate on the proof and answers the escalation question first.** E47.2 runs in
parallel. **E47.3 needs both and is the proof itself.**

- **E47.1** — Remote agentic dispatch: establish it, or escalate *(first; answers Z1's trigger)*
- **E47.2** — Project selection and readiness *(parallel with E47.1)*
- **E47.3** — The proof run and its record *(needs both)*

**Execution posture: E47.1 and E47.2 are `manual`.** E47.3 is **the agentic run itself** — that is the
point of the milestone — **but the chat overseeing it is manual.** Record `Execution Mode` explicitly
in every Epic Starter and do not let the proof's subject blur into the proof's supervision.

---

## Epic Detail

### E47.1 — Remote agentic dispatch: establish it, or escalate *(first)*

**Organizing question: can an epic be dispatched to a remote engine today, by which path, and what
does that path carry?**

**Deliverables**

1. **A completed remote dispatch, or a recorded escalation.** **One run is the whole answer to Z1's
   trigger.** If it needs configuration → M47 absorbs SN-42 as the CFO prefers. **If it needs new
   machinery → escalate; that is the justified new milestone and it is not a failure.**
2. **The route chosen, with Z5's inheritance stated** — which defects the chosen path already carries,
   and why that trade was taken. **Not merely which path works.**
3. **The substrate inherited from M41, not rebuilt** (Z2) — credentials, provider config,
   reachability on the configured engines.
4. **The effective credential path recorded**, and **zero credentials treated as `UNDETERMINED`**.
5. **Whether the loop works, separately from whether the transport works.** They are different
   claims and only the second is inherited.

**Acceptance criteria**

- [ ] A remote dispatch either completed and is recorded with its route, or was escalated with the
      machinery-versus-configuration judgment stated
- [ ] Z5's inheritance is explicit — what the chosen route already carries
- [ ] No transport work was rebuilt that M41 had established
- [ ] Credential visibility is recorded per dispatch; empty is `UNDETERMINED`

---

### E47.2 — Project selection and readiness *(parallel)*

**Organizing question: which real project, and is it actually ready?**

**Deliverables**

1. **The selection, recorded with reasoning** — the CFO's decision, with the survey behind it.
   **Z3's evidence is the input, not the answer:** the phase spec's candidate list is stale;
   `panchew-io` is the only fleet project with current in-flight epic work.
2. **A readiness check that is run, not assumed.** **`panchew-io` has no `models:` block** — dispatch
   is impossible there today. **Whatever project is chosen, verify it can be dispatched to before it
   is committed to.**
3. **The chosen epic identified** — real work, already planned, that **would have been done anyway.**
   Not a task invented to be dispatched.
4. **The project's framework version and governance state recorded**, so the run's context is
   reconstructible later.

**Acceptance criteria**

- [ ] The project is chosen by the CFO with reasoning recorded
- [ ] Its readiness is **verified by running a check**, not asserted — including a `models:` block
- [ ] The epic is real, pre-existing work, and is named
- [ ] Anything blocking readiness is fixed or escalated before E47.3 starts

---

### E47.3 — The proof run and its record *(needs both)*

**Organizing question: did it run, and can we show it did work?**

**Deliverables**

1. **The run, end to end through Drivr** — dispatched, executed, completion-judged, gated, escalated
   if it blocked, handed back, merged by its parent.
2. **The instrument's verdict**, per HQ's acceptance criterion — **tool rounds, files changed,
   claims-resolution.** **Not an exit status.**
3. **The run record**, including **what the framework got wrong.** **Scoped in advance to say that a
   run surfacing a real defect is the stronger result.**
4. **The completion judgment's verdict recorded as given** — including `undetermined`. **M45 makes
   that signal trustworthy; if M45 has not closed, record what the signal said and that it is not yet
   trustworthy, rather than substituting a human judgment silently.**
5. **A statement of what the run does NOT prove.** One project, one epic, one engine. **The claim
   should be exactly as large as the evidence.**

**Acceptance criteria**

- [ ] A real epic ran end to end agentically through Drivr, in a named project
- [ ] **The instrument checked it and its counts are in the record**
- [ ] The framework's own failures during the run are committed
- [ ] The completion signal's verdict is recorded as given, with its trustworthiness stated
- [ ] The limits of the claim are stated

---

## Prerequisites and Dependencies

**Internal**

- **M42's closure — hard, and MET (2026-09-02).** **M42 CLOSED 2026-09-02** — Closure Declaration accepted by the Phase Chat, consolidated to `phase/P12` by PR #248 (merge `90335ca`), `status: completed`. All four defects re-measured gone at acceptance (host `shell=True` fallback, unscoped `git add .`, the `--admin` rung, the placeholder-agent stub); suite `582` at closure.
- **M41 — closed 2026-09-01**, supplying the instrument (Z4) and the transport substrate (Z2).
- **M45** — makes the completion signal trustworthy. **Not a gate on M47**, but E47.3 records the
  signal's trustworthiness rather than assuming it.

**External**

- **Drivr** — the dispatch path. **Outside this repository and its suite.**
- **The selected project** — outside this repository; readiness is E47.2's to verify.
- **`local-agent-runner`** — only if E47.1 routes through it, in which case Z5's parse defect is
  inherited.
- **CFO decisions:** project selection; and **SN-42's escalation if Z1's trigger fires.**

---

## Definition of Done (Milestone)

- [ ] All three epics delivered, accepted, and merged to `milestone/M47`
- [ ] **Remote dispatch established and recorded — or escalated as a justified milestone**
- [ ] **A real epic ran end to end agentically through Drivr**, in a project chosen by the CFO with
      reasoning recorded
- [ ] **The instrument checked the run**; tool rounds, files changed and claims-resolution are in the
      record, and **no exit status stands in for them**
- [ ] The framework's own failures during the run are committed
- [ ] **The route's inherited defects are stated** (Z5)
- [ ] **What the run does not prove is stated**
- [ ] Suite green; the Drivr and project-side verification stated separately
- [ ] Milestone Closure Declaration committed

---

## Acceptance Criteria (Milestone)

- [ ] **A reader can tell, from the record alone, that work was done — not merely that a process
      exited.** That is the entire difference this milestone exists to establish
- [ ] **A run that surfaced a real defect was reported as a success**, if that is what happened
- [ ] Every claim states its layer, repository, ref and date

---

## Timeline

**Target Start:** M42 closed 2026-09-02; M43–M46 have since closed, so M47 is unblocked · **Target Completion:** it is the phase's last substantive
milestone
**Actual Start:** Not started · **Actual Completion:** In progress

---

## Notes

- **This is the milestone that can pass by accident**, and every other milestone in P12 exists to make
  that harder. M42 stops the execution tier proceeding on absent evidence; M45 makes the completion
  signal honest; M46 renders `undetermined` rather than hiding it; **M41 built the instrument that
  checks this run.** **A green M47 that none of them touched would prove nothing.**

- **On `P11-GH-1`.** Amendments reach a running child by amending this spec on `milestone/M47` with a
  changelog row; **notifying the running chat in-session, naming the section**; requiring it to
  re-read and state that it did; escalating if blocking; and **before accepting any delivery, `git
  log` this spec against the epic's branch point AND every artifact its Starter restates a rule
  from** — the widened form, after the backstop was falsified by a ruling that had *arrived* and was
  not applied.

- **Authoring order:** write each Starter after its spec is committed, and **cite the spec by path and
  branch, never by version and sha.**

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.1.0 | 2026-09-04 | **Records M42's closure across every surface that asserted the opposite** — Binding Constraint 1, the Prerequisites entry, and the Timeline each stated *"M42 has not closed"* or *"NOT MET"*, which stopped being true on **2026-09-02** (PR #248, merge `90335ca`, `status: completed`). **Raised by the M47 Milestone Chat as a blocking question rather than edited silently** — the correct call: a governing spec is amended through the parent, not by the child that reads it. **Three surfaces, not one** — the same `P12-GH-1` shape this phase has now swept four times, which is why the fix was a search for the claim rather than a patch to the line that was quoted. M43, M44, M45 and M46 have also closed since; M47 is the phase's last milestone and is unblocked. |
| 1.0.0 | 2026-09-01 | Initial M47 spec, written after M41's closure was accepted and consolidated. **Five planning-time findings.** **Z1: SN-42 sized M47-SIZED on evidence, with a flip trigger** — this repository cannot dispatch remote (`run-dev-agent:114` gates on `local:`), **Drivr's adapter is provider-generic** (`opencode.py:164`, unknown provider hits an early `return config`), and M47's text always said *through Drivr*; **but no remote dispatch has been run, and if it needs new machinery rather than configuration that is the justified escalation.** **Z2: transport and dispatch share a substrate and split at the loop** — E35.5's back-test is single-turn and tool-free, so **M41 already established the transport and M47 inherits it.** **Z3: the phase spec's candidate list is stale** — `home_finance` and `local-agent-runner` last moved 2026-07-20; **`panchew-io` is the only fleet project with current in-flight epic work (five planned epics), and it has NO `models:` block, so it cannot dispatch today.** **Z4: the acceptance instrument exists and is tested** — nothing to build. **Z5: the routing choice decides which defects M47 inherits** — `local-agent-runner` carries the unowned parse defect that produced DEV RUN 2, one of the three cases the criterion exists to catch; Drivr's adapter carries the located `XDG_DATA_HOME` defect instead. Three epics; **E47.1 answers the escalation question before anything depends on it.** |
