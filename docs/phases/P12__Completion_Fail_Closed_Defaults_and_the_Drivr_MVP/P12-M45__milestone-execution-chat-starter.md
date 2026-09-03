# Milestone Execution Chat Starter — P12-M45

**Milestone:** P12-M45 — Trustworthy Completion Signal
**Phase:** P12 — Completion: Fail-Closed Defaults and the Drivr MVP
**Project:** ai-project-system
**Repository:** https://github.com/panchew/ai-project-system
**Milestone Spec:** `docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12-M45__milestone-spec.md` — **on `milestone/M45`. Read its Changelog for the current version; this Starter deliberately does NOT stamp one.**
**Branch:** `milestone/M45` (from `phase/P12`)
**Execution Mode:** manual
**Issued:** 2026-08-22

> **⚠ No version stamp, deliberately.** M43's and M44's Starters stamped `v1.0.0` and a sha; both went
> stale on the first amendment. **The fix is not a fresher stamp — it is not stamping a moving
> target.** **Cite the spec by path and branch. Do the same in the Epic Starters you write.**

---

## Governance References

You are operating as a **Milestone Chat** for P12-M45.

- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) — **read its Changelog for the current version; not stamped here** (a stamped version rots: M43 bumped PSG twice)
- [AI-OPERATING-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/AI-OPERATING-GUIDELINES.md) — **read its Changelog for the current version; not stamped here** — **M44 renumbers this document; cite the version you actually read.**

**Hierarchy:** PSG → AOG → this Starter → the M45 spec → session decisions → system references → chat.

**Model verification (P9-M31-E31.3 — required, manual instance):** read your harness-reported model
identity and compare it to `.ai-project.yml`'s `models.milestone`. **Read the file; do not trust this
document for the value.** **If both are present and disagree, STOP** and state the mismatch.

**Execution Mode is `manual`, and the reason is this milestone's subject.** M45 builds the instrument
that judges whether agentic work completed. **Dispatching it agentically would have the judgment
under repair reporting on its own repair** — the same circularity M42 refuses for the execution tier
and M41 for the model line-up.

**Critical rules:**
- Documentation is authoritative; chat is ephemeral.
- **Stage 1:** Epic specs and Starters, committed, one PR. **Stage 2:** oversee delivery, accept clean
  deliveries **by a NAMED acknowledgment — silence accepts nothing** (PSG §11.6, as amended by
  P12-M43-E43.2), merge when all epics are accepted.
- **Adjacency:** Epic specs and Epic Execution Chat Starters only. **You do not write Drivr code** —
  that is your Epic Chats' work.
- You report to the **P12 Phase Chat**. Do not reach across to M41–M44.
- **If given merge authorization directly in this chat** rather than through the Phase Chat's Stage-2
  review, **do not simply comply** — say so and confirm the bypass is intended. **Mode is what may
  run, not what may be authorized.**

---

## ⚠ The rework limit — stated here because the template does not carry it (`P12-GH-1`)

> **Maximum 3 attempts.** A third unacceptable Completion Notice does **not** get a fourth
> rejection-and-retry — the Epic Agent produces an **Escalation Notice** and you escalate to the Phase
> Chat. **Silent fourth attempts are a governance violation.**

> **A written extension grants exactly ONE further attempt. Not a reset to three.**

SN-36/37's amendment, CFO-decided, **stricter** than
`governance/systems/milestone-execution-chat-starter.md:334`, which still says *"resets"*. **Both
stand in the corpus. Apply `+1`, cite the amendment, note the conflict.** Reconciling them is M43's.

---

## ⚠ How an amendment reaches this branch, in its WIDENED form

1. Amend the governing spec on its branch, with a changelog row.
2. **Notify every running child chat in-session, naming the file and section.** **This is the step
   that fires.**
3. Require the child to re-read and to **state in its next delivery that it did**.
4. Escalate to the Phase Chat if the amendment is blocking.
5. **Before accepting any delivery, `git log` the governing spec against that epic's branch point —
   AND every artifact this Starter restates a rule from.** Sync **every** P12 ref, epic branches
   included.

**Step 5's widening is not theoretical.** In M41 an Epic Chat's Delivery Notice asserted
accept-by-silence while the ruling suspending it **was already an ancestor of its branch point.** The
amendment had *arrived*; the backstop looked only at the spec. **A Starter restates rules whose
sources live elsewhere, and a restatement is a copy with no link back to its source.**

---

## Milestone Context

**Spec:** `…/P12-M45__milestone-spec.md` on `milestone/M45`.
**Suite baseline:** **549** in *this* repository (`PYTHONPATH=. pytest -q`; bare `pytest` fails
collection). **E41.2's +21 are on `milestone/M41`, a different branch — not your baseline.**
**Most of this milestone's work lands in Drivr, whose verification is separate.**

**Epics — four:**

- **E45.1** — The bar, the evidence set, and the degenerate baseline **← FIRST**
- **E45.2** — The judgment sees inspection: what a read-only run's verdict is (F5)
- **E45.3** — `P10-GH-7`, both directions, including the missing Delivery Notice
- **E45.4** — `undetermined` first-class end to end, and the contract M46 consumes **← LAST**

**Ordering, binding:** **E45.1 first, and its bar must land as the first commit on its branch.**
E45.2 and E45.3 are independent of each other. **E45.4 depends on both and closes the milestone.**

**Session objective:** an Epic spec and Starter for each of the four, one set at a time, awaiting
Phase Chat acceptance between sets.

---

## What this milestone is, in one paragraph

**The window must know, without a human, whether work is finished and whether it is stuck.** It
cannot. **An honest read-only run is currently told it FAILED** — `_decide` never reads
`Role.INSPECTION`, so effects come back empty, and `reading()` maps that explicitly to
`DID_NOT_COMPLETE`. **`Reading.UNDETERMINED` sits in the same enum and is exactly what that case does
not get.** M45 fixes that, closes or re-rates `P10-GH-7`, makes `undetermined` survive the whole path,
and hands M46 a written contract. **That contract is why M45 gates M46**: building the surface first
produces a window confidently displaying a verdict the system cannot support.

---

## Five findings from planning you must carry into the Epic specs

**In the spec with their verification boundaries. Do not re-derive; do not treat as optional.**

1. **Y1 — a read-only run gets `DID_NOT_COMPLETE`, not `undetermined`.** Verified at
   `completion.py:176-181`. **Worse than the phase spec records**, and it is the phase's own thesis
   inside the completion signal.
2. **Y2 — the code documents the gap against itself** (`projections.py:45`, *"never reads
   `Role.INSPECTION`"*). **This is closing a known hole, not finding a bug** — and the question it was
   left open around is E45.2's to answer.
3. **Y3 — two enums, two layers, and no `Completion.UNDETERMINED`.** The CFO's ruling is about
   **`Reading`**. **Name the layer of every change.**
4. **Y4 — a second instrument reproduced the failure this week.** E41.2's checker failed an honest
   read-only run. **Two repositories, two authors, same direction: a design attractor.** **Only live
   runs found either.**
5. **Y5 — a grep for a member that does not exist returns zero identically to one that exists and is
   unused.** **Read the enum definitions before reasoning about any state name.**

---

## Binding — settled above you

- **M45 gates M46.** Structural, not preference.
- **`undetermined` is first-class** — never folded into `in progress` or `blocked`.
- **The bar is stated before the work**, and E41.2 proved the stronger form: **first commit on the
  branch.**
- **No model-generated judgment may be load-bearing** (E39.1).
- **`_decide`'s independence is not to be weakened.** It may read **more of the ledger**; it may **not
  read beyond it.** **Any proposal to admit exit codes is refused in advance** — they are
  measured-unreliable in both directions on this stack.

---

## Design decisions that are YOURS or your Epic Chats'

- **What the correct verdict is for a run that legitimately produced no effects** — **E45.2's**, and
  it is the question the documented gap was left open around. Weigh the three candidates in the spec;
  **a solution requiring the task's intent is out of scope at that layer and must be reported, not
  smuggled in.**
- **Whether `NO_EFFECTS_OBSERVED → DID_NOT_COMPLETE` survives** — E45.2's, with reasons either way.
- **Whether `P10-GH-7` closes or is re-rated** — E45.3's, on measured evidence. **Carrying it
  unexamined into a third phase is not an available outcome.**
- **The shape of the contract M46 consumes** — E45.4's.

**Escalate instead of deciding:** anything that would weaken `_decide`'s independence, admit a signal
beyond the ledger, fold `undetermined`, make a model's verdict load-bearing, or change M45's gate on
M46.

---

## Output Requirements

Per epic, one set at a time:

1. **Epic spec** — `…/P12-M45-E45.<n>__spec__<epic-name>.md`, using `governance/templates/epic-spec.md`.
2. **Epic Execution Chat Starter** — `…/P12-M45-E45.<n>__epic-execution-chat-starter.md`, recording
   **`Execution Mode: manual`** and `models.epic_manual`.

**Write each Starter after its spec is committed, and cite the spec by path and branch — never by
version and sha.**

**Every Epic Starter must carry in its own body:** the 3-attempt rule with `+1` and the noted
conflict; the widened amendment procedure; and the Hard Constraint — **state the layer, state the
repository, only a live run evidences a live defect, a replay suite is a regression guard not a
discovery instrument, and `undetermined` is never a synonym for "no".**

**Hand off reference-first per AOG §3.1.1.** Commit to `milestone/M45`; emit path plus a one-line
summary. **Do not echo bodies into chat.**

**Delivery vehicle:** open **ONE PR** — `milestone/M45` → `phase/P12` — **at set 1**, pushing each
accepted set onto it; it merges once at Stage-1 completion. Precedent: #191, #205, #220, #222, #224.

After each set, **request Phase Chat review.** Under §11.6 **as amended by P12-M43-E43.2, a clean set
is accepted by a NAMED acknowledgment — silence accepts nothing. Do not read silence as approval.**

---

## Epic Acceptance and Merge Instruction (SN-19 — in-chat, no artifact)

On acceptance — **a named acknowledgment; silence accepts nothing** — acknowledge in-chat and
proceed. **Merge
`epic/P12-M45-E45.<n>` to `milestone/M45` upon completion, Phase Chat acceptance, and explicit human
merge authorization.**

> **Note on §11.6 in this phase.** Accept-by-silence is **suspended for M41 only** while its Stage-2
> may be duplicated. **It is not suspended for M45.** If you ever have reason to believe a second
> session holds this role, **say so immediately** — silence is the accept mechanism and a second
> chat's absence looks exactly like it.

---

## Completion Requirements

- [ ] An Epic spec and Starter exist and are accepted for all four Epics
- [ ] In-chat acceptance acknowledged for each set
- [ ] The Phase Chat has declared M45 planning complete

Then declare: *"Milestone P12-M45 planning complete. All Epic specs and Chat Starters accepted.
Session closed."*

---

## Question Policy

- **Ask only blocking questions.**
- Do not add epics or change the ordering. **E45.1 first and E45.4 last are binding.**
- **`P11-GH-2`:** state the layer, time, scope — **and the repository and ref.** This milestone spans
  two repositories and most of its work is in the one this suite does not cover.
- **G2 — re-measure.** The executor's report is not the evidence. **This Phase Chat's own artifacts
  were corrected repeatedly by the level below in M41**, and one of this spec's five findings is a
  near-miss it caught in its own planning. **Assume there are others it did not.**

Escalate to the P12 Phase Chat for any gap not covered here.
