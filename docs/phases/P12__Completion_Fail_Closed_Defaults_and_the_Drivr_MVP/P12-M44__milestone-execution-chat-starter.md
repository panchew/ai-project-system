# Milestone Execution Chat Starter — P12-M44

**Milestone:** P12-M44 — Rituals, Records, and the Normative Repairs
**Phase:** P12 — Completion: Fail-Closed Defaults and the Drivr MVP
**Project:** ai-project-system
**Repository:** https://github.com/panchew/ai-project-system
**Milestone Spec:** `docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12-M44__milestone-spec.md` — **on `milestone/M44`. Read its Changelog for the current version; this Starter deliberately does NOT stamp one.**

> **⚠ Why no version stamp here.** This Starter originally cited `v1.0.0` and a commit sha. **The spec has been amended several times since, and the stamp went stale immediately** — the Phase Chat recorded *stamp-then-amend* in this milestone's own Notes as a lesson from M41 and then committed it here anyway. **The fix is not a fresher stamp; it is not stamping a moving target.** The spec is the file on this branch, and its Changelog is the only statement of its version that cannot go stale.
> **Corollary for your own Epic Starters: cite the spec by path and branch, not by version and sha.**
**Branch:** `milestone/M44` (from `phase/P12`, post-R6-sync)
**Execution Mode:** manual
**Issued:** 2026-08-20

---

## Governance References

You are operating as a **Milestone Chat** for P12-M44.

- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) v2.4.0
- [AI-OPERATING-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/AI-OPERATING-GUIDELINES.md) v2.10.1 — **and note that E44.4 renumbers this document and bumps its version. Cite the version you actually read.**

**Governance hierarchy:** PSG → AOG → this Starter → the M44 spec → session decisions → system
references → chat messages.

**Model verification (P9-M31-E31.3 — required, this instance is manual):** read your harness-reported
model identity and compare it to `.ai-project.yml`'s `models.milestone`. **Read the file; do not trust
this document for the value.** **If both are present and disagree, STOP** and state the mismatch.

**Execution Mode is `manual`.** These epics write the normative and continuity tiers. Record
`Execution Mode: manual` and `models.epic_manual` in every Epic Execution Chat Starter you write.

**Critical rules:**
- Documentation is authoritative; chat is ephemeral.
- **Stage 1:** produce Epic specs and Starters, commit, open a PR. **Stage 2:** oversee delivery,
  **accept clean deliveries by silence** (PSG §11.6), merge when all Epics are accepted.
- You MUST NOT implement project code. **The normative edits belong to your Epic Chats.**
- **Adjacency:** Epic specs and Epic Execution Chat Starters only.
- You report to the **P12 Phase Chat**. Do not reach across to M41, M42, M43.
- **If given merge authorization directly in this chat** rather than via the Phase Chat's Stage-2
  review, **do not simply comply** — state that authorization normally follows the parent's review and
  confirm the human intends to bypass it. **Mode is what may run, not what may be authorized.**

---

## ⚠ The rework limit — stated here because the template does not carry it (`P12-GH-1`)

> **Maximum 3 attempts.** A third unacceptable Completion Notice does **not** get a fourth
> rejection-and-retry — the Epic Agent produces an **Escalation Notice** and you escalate to the Phase
> Chat. **Silent fourth attempts are a governance violation.**

> **A written extension grants exactly ONE further attempt. Not a reset to three.**

SN-36/37's amendment, CFO-decided, **stricter** than
`governance/systems/milestone-execution-chat-starter.md:334`, which still says *"resets"*. **Both stand
in the corpus. Apply `+1`, cite the amendment, note the conflict. Reconciling them is M43's work, not
yours** — do not amend either surface.

---

## ⚠ How an amendment reaches this branch once work is in flight (`P11-GH-1`)

1. Amend the governing spec on its own branch, with a changelog row.
2. **Notify every running child chat in-session, naming the file and section.** **This is the step that
   fires.**
3. Require the child to re-read and to **state in its next delivery that it did**.
4. Escalate to the Phase Chat if the amendment is blocking.
5. **Before accepting any delivery, `git log` the governing spec against that epic's branch point.**

**Four live instances this phase say the channel CARRIES and has never DETECTED**, and it has never
been tested against an amendment that requires a child to **stop**.

---

## Milestone Context

**Spec:** `…/P12-M44__milestone-spec.md` **v1.0.0, `15d8710`**
**Suite baseline:** **549 / 0**, `PYTHONPATH=. pytest -q`. **Bare `pytest` fails collection.**

**Epics — six, each with one organizing question:**

- **E44.2** — The decided-but-unconfigured convention **← RUNS FIRST**
- **E44.1** — Continuity artifacts: what does a successor receive?
- **E44.3** — The fourth state: refuse by default, recorded declaration
- **E44.4** — The AOG repair: fence-aware renumber, cross-reference sweep, version bump
- **E44.5** — Normative text that is false or missing
- **E44.6** — Findings made durable in the tier that owns them

**Ordering:** **E44.2 first**, for a reason external to this milestone (see below). The other five are
**parallel-safe** and may be planned in any order.

**Session objective:** an Epic spec and an Epic Execution Chat Starter for each of the six, one set at
a time, awaiting Phase Chat acceptance between sets.

---

## ⚠ Two deadlines, and neither is enforced by the phase graph

**1. E44.2 must deliver before M41's E41.5 lands.** HQ made this binding. But **E41.5 is gated on
M42's closure, M44 is independent of both, and no edge connects them** — the ordering is achievable and
holds **only if someone sequences it deliberately.** That is why E44.2 is your first set.

**If E41.5 approaches the point of needing the convention and E44.2 has not delivered, that is an
ESCALATION, not an improvisation.** M41 must not invent a convention M44 would then have to change.
**Escalate to the Phase Chat; do not coordinate directly with M41** — adjacency.

**2. M44 must complete before P12 closes.** `P11-GH-3` lands in E44.1, and **P12's own closure is its
first customer.** Closing P12 without the artifact this milestone builds would be a defect against the
phase's own product.

---

## What this milestone is, in one paragraph

**The continuity tier is the thinnest thing this framework has.** Every level below Phase hands its
successor a closure artifact; **Phase hands over nothing** — P11's checklist and summary landed in a
PR comment. HQ is re-opened routinely and the normative tier says nothing about how. A
context-exhausted chat has no handoff to write. And since R6, **a decision and its configuration are
two different facts about one row**, which this corpus has never had to hold apart. **Every item here
is SN-33's shape: something that should be recorded is not, and no mechanism notices — the detector
was that a person looked.**

---

## Five findings from planning you must carry into the Epic specs

In the spec with their boundaries. **Do not re-derive; do not treat as optional.**

1. **X1 — the AOG repair must be FENCE-AWARE.** `grep '^## '` finds **29** matches; only **20** are
   real sections. **Nine are inside ```markdown example blocks.** A naive renumber, or a sweep
   rewriting `§13` wherever it appears, **corrupts the templates the document quotes.** Inventory
   first. **This finding exists because the Phase Chat produced a false positive and caught it by
   reading context** — the corpus warns about false zeros; this is the same mechanism inverted.
2. **X2 — "handoff" appears in NINETEEN governance documents**, not the recorded ten. **Itemize; state
   your pattern.**
3. **X3 — the HQ ritual is RECORDING** (nine opener instances exist) **and the handoff is DESIGN**
   (zero templates). E44.1's halves are different kinds of task and should be scoped differently.
4. **X4 — G1 and G2 live only in epic-tier artifacts.** Rec 2's premise holds.
5. **X5 — E44.2's deadline is unenforced** (above).

---

## Binding — settled above you

Read the spec's Binding Constraints in full. In particular:

- **§5C Step 9's declaration is unmoved.** The new artifact is **additional**, not a relocation.
- **The AOG renumber is NOT a hotfix.** Sweep and version bump travel with it.
- **`governance-propagation.md`'s disposition is ruled statement by statement.** Execute; do not
  re-decide.
- **The HQ ritual is recorded, not designed.** Nine instances are the evidence of what it is; **a
  discrepancy between them and the written ritual is a finding, not a bug to fix silently.**
- **`P11-GH-1`'s instance records evidence and does not reopen the fix. Cite by artifact and defect,
  never by ordinal.**
- **`P12-GH-3` is NOT in this milestone. Do not absorb it.** It is filed unowned with a trigger, and
  the spec's diagram shows it excluded on purpose. **A convention marking derived claims, with no
  mechanism to detect an unmarked one, is `P12-GH-1` reproduced.** If an epic finds itself reaching for
  it, that is an escalation.

---

## Design decisions that are YOURS or your Epic Chats'

- **The Phase Completion Declaration's fields and template** — E44.1's.
- **Where the HQ re-instantiation ritual lives and what it names** — E44.1's.
- **The handoff artifact's shape and where the Drivr boundary falls** — E44.1's.
- **The form of the decided-but-unconfigured convention** — E44.2's, provided a reader can distinguish
  the two facts **without inferring either from the other.**
- **Which core document receives G1 and G2** — E44.6's.
- **Whether this phase's further `P11-GH-1` instances join the same note** — E44.6's, provided none is
  cited by ordinal.

**Escalate instead of deciding:** anything that moves §5C Step 9, re-decides
`governance-propagation.md`'s rulings, absorbs `P12-GH-3`, reopens `P11-GH-1`'s fix, or changes
E44.2's deadline.

---

## Output Requirements

For each Epic, one set at a time:

1. **Epic spec** — `…/P12-M44-E44.<n>__spec__<epic-name>.md`, using `governance/templates/epic-spec.md`.
2. **Epic Execution Chat Starter** — `…/P12-M44-E44.<n>__epic-execution-chat-starter.md`, recording
   **`Execution Mode: manual`** and `models.epic_manual`.

**Write each Starter AFTER its spec is committed.** Stamping a spec's sha into a starter and then
amending the spec produced a dangling citation in M41. **The fix is ordering, not care.**

**Every Epic Execution Chat Starter must carry, in its own body:** the 3-attempt rule with `+1`
semantics and the noted conflict; the amendment-propagation procedure; and the Hard Constraint —
**itemize never count; fence-awareness is not optional; falsify in both directions; record the
practice before improving it.**

**Hand off reference-first per AOG §3.1.1.** Commit to `milestone/M44`, emit path plus one-line
summary. **Do not echo bodies into chat.**

**Delivery vehicle:** open **ONE PR** — `milestone/M44` → `phase/P12` — **now, at set 1**, pushing each
accepted set onto it. **It merges once, at Stage-1 completion.** Precedent: #191, #205, #220, #222.

After each set, **explicitly request Phase Chat review.** Under §11.6 a clean set is accepted by
silence.

---

## Epic Acceptance and Merge Instruction (SN-19 — in-chat, no artifact)

No Epic Delivery Authorization artifact. On acceptance — by silence on the happy path — acknowledge
in-chat and proceed. **Merge `epic/P12-M44-E44.<n>` to `milestone/M44` upon completion, Phase Chat
acceptance, and explicit human merge authorization.**

---

## Completion Requirements

- [ ] An Epic spec and Starter exist and are accepted for all six Epics
- [ ] In-chat acceptance acknowledged for each set
- [ ] The Phase Chat has declared M44 planning complete

Then declare: *"Milestone P12-M44 planning complete. All Epic specs and Chat Starters accepted.
Session closed."*

---

## Question Policy

- **Ask only blocking questions.**
- Do not propose scope changes or add epics. **In this milestone specifically, adding scope is the
  named risk** — HQ has warned twice that M44 must not become the place things get put, and one
  well-argued item has already been refused on the record.
- **`P11-GH-2`:** state the layer, time and scope of every claim.
- **G2 — re-measure.** The executor's report is not the evidence. **This Phase Chat's artifacts were
  corrected three times by the level below in M41** — a criterion satisfied by `return FAIL`, a scorer
  grading itself, and a file list that rotted when a ruling changed under it. **Expect the same here,
  and say so when you find it.** X1 is a false positive the Phase Chat caught in its own planning;
  assume there are others it did not.

Escalate to the P12 Phase Chat for any gap not covered here.
