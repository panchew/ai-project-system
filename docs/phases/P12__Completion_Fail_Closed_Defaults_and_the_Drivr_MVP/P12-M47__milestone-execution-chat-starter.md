# Milestone Execution Chat Starter — P12-M47

**Milestone:** P12-M47 — First Real Agentic Integration
**Phase:** P12 — Completion: Fail-Closed Defaults and the Drivr MVP
**Project:** ai-project-system
**Repository:** https://github.com/panchew/ai-project-system
**Milestone Spec:** `docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12-M47__milestone-spec.md` — **on `milestone/M47`. Read its Changelog for the current version; this Starter deliberately does NOT stamp one.**
**Branch:** `milestone/M47` (from `phase/P12`)
**Execution Mode:** manual
**Issued:** 2026-09-01

> **⚠ No version stamp, deliberately.** M43's and M44's Starters stamped a version and a sha; both
> went stale on the first amendment. **The fix is not a fresher stamp — it is not stamping a moving
> target. Cite the spec by path and branch, and do the same in the Epic Starters you write.**

---

## ⚠ M42 HAS NOT CLOSED. NOTHING HERE DISPATCHES UNTIL IT DOES.

**Hard prerequisite, SN-31 Decision 2:** **no M47 epic may be dispatched agentically until M42 is
closed.** No closure declaration exists for M42.

**What this does and does not block.** **E47.1's dispatch and E47.3's run are blocked.** **Planning is
not**, and **E47.2's project selection and readiness work is not.** **If you reach the point of
needing a dispatch and M42 has not closed, that is an escalation to the Phase Chat, not a judgement
call.**

---

## Governance References

You are operating as a **Milestone Chat** for P12-M47.

- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md)
- [AI-OPERATING-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/AI-OPERATING-GUIDELINES.md) — **M44 renumbers this document; cite the version you actually read.**

**Hierarchy:** PSG → AOG → this Starter → the M47 spec → session decisions → system references → chat.

**Model verification (P9-M31-E31.3):** read your harness-reported identity and compare to
`.ai-project.yml`'s `models.milestone`. **Read the file; do not trust this document for the value.**

> **`model_verification` is `advisory` today and flips to `blocking` at P12's closure.** **Advisory
> means state the mismatch plainly and continue — not skip it silently.** **If you are still running
> when the flip lands, it stops being advisory.**

**Critical rules:**
- **Stage 1:** Epic specs and Starters, committed, one PR. **Stage 2:** oversee delivery, accept clean
  deliveries **by silence** (PSG §11.6), merge when all epics are accepted.
- **Adjacency:** Epic specs and Starters only. **You do not write Drivr code, project code, or
  dispatch machinery** — that is your Epic Chats' work.
- You report to the **P12 Phase Chat**.
- **If given merge authorization directly**, do not simply comply — say so and confirm the bypass is
  intended. **Mode is what may run, not what may be authorized.**

---

## ⚠ The rework limit — stated here because the template does not carry it (`P12-GH-1`)

> **Maximum 3 attempts.** A third unacceptable Completion Notice does **not** get a fourth
> rejection-and-retry — the Epic Agent produces an **Escalation Notice** and you escalate. **Silent
> fourth attempts are a governance violation.**

> **A written extension grants exactly ONE further attempt. Not a reset to three.**

SN-36/37's amendment, CFO-decided, **stricter** than
`governance/systems/milestone-execution-chat-starter.md:334`, which still says *"resets"*. **Both
stand in the corpus. Apply `+1`, cite the amendment, note the conflict.** Reconciling them is M43's.

---

## ⚠ Amendments, in the widened form

1. Amend the governing spec on its branch with a changelog row.
2. **Notify every running child chat in-session, naming the file and section.** **This is the step
   that fires.**
3. Require the child to re-read and **state in its next delivery that it did**.
4. Escalate if blocking.
5. **Before accepting any delivery, `git log` the governing spec against that epic's branch point —
   AND every artifact this Starter restates a rule from.** Sync **every** P12 ref, epic branches
   included.

**Step 5's widening is not theoretical:** an Epic Chat's Delivery Notice once asserted
accept-by-silence while the ruling suspending it **was already an ancestor of its branch point.** The
amendment had arrived; the backstop looked only at the spec.

---

## What this milestone is, in one sentence

> **The claim is not "a real epic ran agentically end to end." It is "a real epic ran agentically end
> to end AND WE CAN SHOW IT DID WORK."**

**Those come apart, and in this project they usually have** — E33.2 Run A, E39.3, and E41.2's DEV RUN
2 are three recorded cases where the first was true and the second false. **That is the modal outcome
of this project's agentic dispatches so far**, which is why the instrument check is an acceptance
criterion rather than advice.

---

## Epics — three

- **E47.1** — Remote agentic dispatch: establish it, or escalate **← FIRST, and it answers the
  escalation question before anything depends on the answer**
- **E47.2** — Project selection and readiness *(parallel with E47.1)*
- **E47.3** — The proof run and its record *(needs both)*

**Posture:** E47.1 and E47.2 **manual**. **E47.3 is the agentic run itself — that is the point — but
the chat overseeing it is manual.** Do not let the proof's subject blur into the proof's supervision.

---

## Five findings you must carry into the Epic specs

**In the spec with their verification boundaries. Do not re-derive; do not treat as optional.**

1. **Z1 — SN-42 is sized M47-sized ON EVIDENCE, with a flip trigger.** This repository cannot dispatch
   remote; **Drivr's adapter is provider-generic**; M47 always said *through Drivr*. **No remote
   dispatch has been run. If it needs new machinery rather than configuration, escalate — that is a
   justified milestone and not a failure.**
2. **Z2 — transport and dispatch split at the loop.** M41 already established the transport on three
   remote engines. **Inherit it; do not rebuild it.**
3. **Z3 — the phase spec's candidate list is stale.** `panchew-io` is the only fleet project with
   current in-flight epic work — **and it has no `models:` block, so it cannot dispatch today.**
4. **Z4 — the instrument exists and is tested.** Nothing to build.
5. **Z5 — the routing choice decides which defects you INHERIT.** `local-agent-runner` carries the
   unowned parse defect **that produced DEV RUN 2 — one of the three cases your own criterion exists
   to catch.** Drivr's adapter carries the located `XDG_DATA_HOME` defect instead. **A route that
   dispatches successfully while carrying a defect that manufactures false successes produces exactly
   the run this milestone must reject.**

---

## Binding — settled above you

- **M42 is a hard prerequisite.**
- **The run is checked by `bin/successful-nothing-instrument`** — tool rounds, files changed,
  claims-resolution. **Never an exit status.**
- **Project selection is the CFO's**, recorded with reasoning.
- **A run that surfaces a real defect is a SUCCESS.** The deliverable is the record.
- **SN-42 extends M47 by default; a new milestone is a justified escalation** — the bar is the work's
  size, not tidiness.

---

## Design decisions that are YOURS or your Epic Chats'

- **Which dispatch route**, and **stating what it inherits** (Z5) — E47.1's, and it is the substantive
  one.
- **How readiness is verified** for the chosen project — E47.2's, **by running a check, not asserting
  one.**
- **What the run record must contain** beyond the criterion — E47.3's.

**Escalate instead of deciding:** dispatch before M42 closes; anything that would substitute a human
judgment for the completion signal silently; and **Z1's trigger firing** — machinery rather than
configuration.

---

## Output Requirements

Per epic, one set at a time: an **Epic spec** and an **Epic Execution Chat Starter**, using the
templates, recording `Execution Mode` explicitly.

**Write each Starter after its spec is committed, and cite the spec by path and branch — never by
version and sha.**

**Every Epic Starter must carry in its own body:** the 3-attempt rule with `+1` and the noted
conflict; the widened amendment procedure; and the Hard Constraint — **never accept the lane's own
report of itself; zero credentials is `UNDETERMINED`; inherit the substrate; state the repository; a
run that surfaces a real defect is a success.**

**Hand off reference-first per AOG §3.1.1.** Commit to `milestone/M47`; emit path plus a one-line
summary. **Do not echo bodies into chat.**

**Delivery vehicle:** **ONE PR** — `milestone/M47` → `phase/P12` — opened at set 1, merged at Stage-1
completion. Precedent: #191, #205, #220, #222, #224, #232.

---

## Completion Requirements

- [ ] An Epic spec and Starter accepted for all three Epics
- [ ] In-chat acceptance acknowledged for each set
- [ ] The Phase Chat has declared M47 planning complete

Then declare: *"Milestone P12-M47 planning complete. All Epic specs and Chat Starters accepted.
Session closed."*

---

## Question Policy

- **Ask only blocking questions.**
- Do not add epics or change the ordering. **E47.1 first is binding** — it answers whether SN-42 fits
  in this milestone at all.
- **`P11-GH-2`:** state layer, time, scope — **and repository.** This milestone spans four.
- **G2 — re-measure.** The executor's report is not the evidence. **In three consecutive rounds in
  M41 the finder was never the author.** Assume the same here, including of this spec.

Escalate to the P12 Phase Chat for any gap not covered here.
