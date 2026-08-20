---
type: hq_ruling
concern_id: S5 (held), T3 (endorsed), U1 (ratified), U2 (two-axis rule), M44 inputs 1-2
amends_in_part: .ai-project/artifacts/rulings/2026-08-19__ai-project-system-hq__ruling__p12-opening-and-sn-30-37-triage.md
hq_opener_ref: .ai-project/artifacts/hq-openers/2026-08-19__hq-chat-opener.md
issued_by: HQ Chat (ai-project-system)
issued_to: Layer-8/CFO (S5 is his; mandatory diff reviewer, PSG §11.6.1); the P12 Phase Chat; M41; M44
phase: P12
date: 2026-08-20
status: active
blocking_resolved: false
---

# HQ Ruling — S5 Stays with the CFO; T3 and U1 Endorsed at Their Level; U2's Two Axes Named; Decision 11 Corrected Against Itself

**Prerequisite verification (P9-M31-E31.3):** harness `claude-opus-5` vs `models.hq:
remote:claude-opus-5` — **match.**

**`blocking_resolved: false`** — deliberately. **S5 is unresolved and is the CFO's.** This ruling
disposes of everything around it and leaves the one decision that is not HQ's.

---

## Decision 1 — S5 stays with the CFO. HQ ratifies the interim and records a recommendation, nothing more

**The finding is verified.** `bin/run-qa-agent:333-344` refuses to dispatch when `write_file`,
`edit_file`, `git` or `run_command` appear in the enabled set, with the intent stated in the comment:
*"the adapter refuses to dispatch under a tool set that could mutate the tree, so the guarantee does
not depend on the QA tool set staying read-only after this epic ends."* **`files changed > 0` on
`epic_qa` is unreachable by construction, not merely unlikely.**

**HQ does not rule it.** Binding Constraint 6's floor is enumerated in the CFO's own words in
SN-36/37, and the phase spec lists it among the decisions not to re-examine. **The Phase Chat declined
to touch it for exactly that reason and routed it. HQ stands in the same relation to that decision and
will not adopt a per-lane form by calling it an application detail.**

**Ratified, because these are HQ's to ratify:**

- **The interim handling is correct and continues.** Build the instrument; measure the `epic_dev`
  baseline unaffected; record every raw count for `epic_qa`; **withhold the `epic_qa` pass/fail
  verdict.**
- **E41.3 may not apply an unresolved floor.** The Hard Constraint requires the bar committed before
  the run it judges, and **a bar under escalation is not committed.** HQ confirms that reading.
- **Repairing this by weakening either mechanism is the wrong repair.** Criterion 2 is the class of
  guarantee P12 exists to build; the floor is the class of detector P12 exists to build. **HQ would
  reject a resolution that relaxes either**, and records that so no epic reaches for the cheap fix.

**HQ's recommendation to the CFO, on the record so his decision is cheap:**

**A per-lane floor** — `epic_dev` keeps `rounds > 0` **and** `files changed > 0`; `epic_qa` takes
`rounds > 0` **and** `claims resolve`, with files-changed recorded but not scored.

**The argument, in one line: `files changed > 0` on `epic_qa` is not a strict bar — it is a constant
false.** A check that returns the same answer for every candidate has **zero discriminating power**.
It measures the harness, not the model.

**And it loses nothing against the record.** E39.3's fabrication returned `VERDICT: PASS` with **zero
tool rounds, citing a key the file does not contain** — caught by `rounds > 0` **and** by
`claims resolve`, independently. E33.2's 14b (exit 0, 0 rounds, 0 files) fails the dev-lane form on
both counts. **Every recorded failure still fails.**

**Precedent is the CFO's own.** SN-38 ruled two harnesses *"because the checks do not transfer."*
S5 is that principle one level finer, inside the dispatch-lane category, between a lane that writes
and a lane that is **forbidden** to.

---

## Decision 2 — HQ's own Decision 11 carried the defect the Phase Chat just found in its own criterion. Corrected here

**The P12 opening ruling, Decision 11:** *"the suite must flag both recorded historical failures when
replayed — E33.2's 14b … and E39.3's dispatches."*

**Negative cases only. `return FAIL` satisfies it in full.** That is precisely the defect the Phase
Chat found in its own E41.2 acceptance criterion and repaired at M41 spec v1.2.1 — and HQ's version
governs **M46's formalized gate**, where an always-failing gate would reject every candidate forever
while passing its own acceptance.

**Decision 11 is amended.** The gate's acceptance requirement now reads:

> The suite must **discriminate in both directions**: flag **E33.2's 14b** and **E39.3's `epic_qa`
> dispatch** as failures, **and pass E33.2 Run B and E33.4** as successes. **A detector with no
> negative control is not a detector.**

**Both positive controls are already committed here**, which is why this costs nothing to require.

**A coherence worth naming, because it argues for the shape rather than merely permitting it:**
**E35.5's own back-test already had this property since July.** `rubric.md:111` — packet 3's ground
truth is **ACCEPT**, so a reject-everything model scores 4/5 and fails only that one. **And packet 3
is E33.2 Run B.** The instrument the phase told everyone not to rebuild already knew what two of this
phase's own acceptance criteria did not.

---

## Decision 3 — T3 is ENDORSED, not overruled. The line the Phase Chat drew is adopted as the general test

**T3 is not a change to Binding Constraint 6, and the Phase Chat's reasoning is correct.**

**SN-37's text keeps two terms separate:** *"no worse on **every objective check** … **over an
absolute floor of** tool rounds > 0 and files changed > 0."* **The floor is enumerated. The objective
checks never were.** Supplying them is the discharge of Decision 11's own obligation — *the bar set as
part of the same work rather than deferred to first use* — not an amendment.

**And it touches none of the three things that are the CFO's:** neither of the bar's two conditions,
neither floor value, nor the prohibition on subjective scoring.

**The finding underneath it is verified and is stronger than the ruling it produced.**
`agentic-runs/P10-M33-E33.2/run-record.md:75-82`: Run B took **10 rounds, wasted 3** on a
`pip install -e .` its allow-list denied, terminated `max_iterations_exceeded` — **and "produced
correct, complete, green work", suite 210 passed.** The record calls it *"a false-negative exit code
(mirror image of Run A's false positive)."*

**So this project owns the run that proves its own metric is non-directional.** More rounds is not
better; a model doing that work in four rounds is not worse. With `files changed` structurally zero on
one lane and `claims resolving` directional only as a rate, **"strictly better on at least one" had
almost nothing to attach to** — and the only remaining tie-breaker is the quality judgment the
constraint prohibits. **An epic in that position escalates or reaches for an impression. Naming it
first is what prevents the second.**

**The line, adopted as HQ's general test for this class:**

> **Changing a value the CFO enumerated → escalation.**
> **Supplying a term he left unenumerated, where an artifact already obliges someone to supply it →
> the level that owes it.**

**The placement call is right and HQ would have insisted on it too:** the checks land in **E41.2**,
committed with the task, because *choosing a scoring rule after you know who is being scored* is
exactly what bar-committed-first exists to prevent. E41.3 escalating rather than improvising if E41.2
delivers without one is the correct failure mode.

---

## Decision 4 — U1 is RATIFIED. Scorer-blinding surrounds F2's protected set without touching it

**E35.5's blinding is one-directional** — every control keeps the answer from the model; nothing
blinds the scorer to which model produced an output. **E35.5 had no reason to**, with one candidate
and a scorer that was not it.

**E41.4 breaks that:** `claude-opus-5` is a **subject** — the incumbent whose baseline makes the other
rows decidable, added by M41's own finding F4 — **and is the scorer's own model**, since every chat in
this milestone runs on it. **Unblinded, it grades its own output against four competitors.**

**Ratified as the Phase Chat's call, not escalated, and the reasoning is right:** F2's protected set is
enumerable — packets, rubric, ground truth, model-side blinding, E35.5's ten runs — and scorer-blinding
touches none of it. **F2 said build only the transport to stop someone rewriting a packet, not to
forbid a control the original never needed.** Opaque run IDs, score with identity withheld, commit the
scores, **then** publish the committed mapping. **A blind, not a secret, with commit order as the
control.**

**The self-attribution is the part HQ wants on the record.** Two of the Phase Chat's own decisions
composed into this — the manual/paid-frontier posture written *to prevent* circularity, and F4 which
added `claude-opus-5` as a subject. **Each correct alone; together they made the scorer a subject.**
That is the composition failure this corpus has no detector for, and it was found by the level below.

**The recorded method asymmetry is required and HQ endorses it:** the fifty new runs carry
scorer-blinding, E35.5's ten cited `qwen3.6:27b` runs do not. It contaminates no row decision — a lane
candidate is not a verification target — **and the record should say it rather than let a reader find
it.**

---

## Decision 5 — U2: two axes, ruled separately. The measurement axis is named here

**The Phase Chat's generalization is the durable output and HQ adopts it:** *"is the model
available?"* was **one question doing two jobs**, and the two answers **invert between adjacent rows
in the same milestone.**

| Row | Landing axis (chat surface, R6) | Measurement axis (programmatic transport) |
|---|---|---|
| `phase` → GPT-5.6 Sol | **unknown** | credential present — **measurable** |
| `creation` → fable-5 | **plausible** (in-harness) | no credential — **maybe not measurable** |
| `milestone` → Deepseek V4 Flash | **none** | **none** |
| `epic_manual` → `qwen3.8:27b` | gated (R6/F6) | Ollama — **measurable now** |

**R6 ruled the landing axis. The measurement axis is ruled here:**

> **A row without a transport blocks that row's measurement and nothing else. Measure what can be
> measured, escalate what cannot, and substitute nothing.**

**The substitution clause is the load-bearing half.** A reachable model standing in for an unreachable
one is `P12-GH-2`'s manufactured-substitute pattern one tier up — the defect this phase filed at
severity High. **The Phase Chat made per-row blocking binding at its level before asking; that was
correct and HQ ratifies it rather than re-deciding it.**

**HQ notes the credential check was performed correctly** — provider-name presence only, raw output
discarded, no credential material displayed or recorded. **That discipline should be stated in
E41.1's record**, because a future reader will otherwise not know it was observed.

### For the CFO: `milestone → Deepseek V4 Flash` now carries three independent negatives

**No chat surface. No environment credential. No entry in the `opencode` auth store.**

**It is the highest-risk row in SN-38** — Milestone holds Stage-2 accept authority, which is the
stated reason row P4 read paid frontier, and the move is to a Flash tier on public capability claims.
**And it is currently the one row that can be neither measured nor landed**, which means **the
qualification gate the CFO commissioned specifically to make that row decidable cannot run on it.**

**HQ proposes nothing.** Both axes are CFO-side tooling facts. This is stated so the row's status is
explicit rather than discovered at E41.4.

---

## Decision 6 — M44 Input 1 is PLACED. Input 2 is FILED as `P12-GH-3` and NOT placed

**Input 1 — "decided" and "configured" have never had to be held apart — is placed in M44**, and HQ
places it because **HQ's own R6 ruling created the condition.**

Until R6, this corpus recorded a decision **by making the edit**; they were one act. R6 separated them
possibly for a long time: `phase`, `milestone` and `epic_manual` are now **decided-and-unconfigured**
on a trigger with no expiry. **E41.5 is the first artifact here that must let a reader see both facts
without inferring one from the other, and no convention was designed for it.**

**The failure mode is specific and it is this phase's own shape:** a reader who cannot tell **will
assume the file matches the ruling** — the divergence the guards exist to catch, arriving in the one
place the guards do not reach, **the prose.** It fits M44's organizing principle (records and rituals)
rather than merely fitting M44's calendar.

**Input 2 — derived-claim rot — is filed as `P12-GH-3`, severity High, and deliberately unscoped.**
See `docs/phases/P12__.../P12__carry-forward-note__P12-GH-3-derived-claim-rot.md`.

**Both the Phase Chat and the M41 chat invoked HQ's own warning against their own finding and declined
to push it into M44. That was right, and HQ will not override it by placing it there instead.**
**Filing is not placing.** SN-32's pattern exactly: the record survives whether or not the fix is
scheduled.

**Why it earns High.** A dangling citation is visible; **a resolving citation pointing at rotted
content is not.** Every mechanism this corpus owns — the divergence guards, the starter lint, the ID
uniqueness check, the per-set branch-drift check — **detects absence.** None detects staleness in
something present. And the phase's thesis applies with one word changed: **when the evidence that
should gate a claim has moved, the claim proceeds.**

---

## Decision 7 — The channel finding is adopted in the Milestone Chat's sharper form, and HQ's earlier account of it was too generous

**HQ wrote that the `P11-GH-1` channel "fired correctly."** The Phase Chat narrowed that to *the
channel is a carrier, not a detector.* **The Milestone Chat's form is better and is the one this
ruling adopts:**

> **The channel has not yet been tested against an amendment that requires a child to stop.**

**Both live exercises tested arrival**, and both amendments happened to be **compatible** with what the
child was doing — so re-reading changed nothing material either time. The second exercise's addressee
reports it had **already discovered the amendment by colliding with it**, about ten minutes before the
notification drained.

**Notification-versus-detection is a distinction with no cost until an amendment invalidates work in
flight, and then it is the entire cost.** `P11-GH-1`'s real severity is **unmeasured**, and both data
points are the easy case. **HQ's "fired correctly" overstated it and is corrected here.**

---

## On the tally, in the direction the Phase Chat chose to state it

Four defects caught one level down in M41. **Three were the Phase Chat's own** — an acceptance
criterion satisfied by `return FAIL`; a posture×F4 composition that made the scorer a subject; and a
rotted file list. **One was HQ's**, via R6. The Milestone Chat's own was the only one that changed a
practice rather than a document.

**The Phase Chat put that ratio on the record itself rather than the version where the reviewer
catches everyone else.** HQ records it in the same direction and adds the one it owns: **R6 corrected
an HQ ruling, Decision 2 above corrects another, and Decision 7 corrects an HQ characterization.**
Three HQ errors caught from below in two days.

**P11 concluded that the review chain caught every HQ error, and asked whether that was a property of
the design or of current attention. P12 is now the second phase's worth of evidence, and it still does
not answer the question** — because in every instance the catcher was a chat applying the artifact,
which is the same path P11 described. **`P12-GH-3` is where that observation now lives.**

---

## Disposition

**Open and NOT resolved: S5.** The CFO's. `epic_qa`'s verdict stays withheld; everything else in M41
proceeds.

**Also open with the CFO:** #221's diff review; #220's diff review and merge authorization; the
surface question, which U2 widens into a transport question; and `milestone → Deepseek V4 Flash`'s
three negatives.

**PSG §11.6.1:** HQ-authored, no chat-level reviewer. The CFO is the mandatory diff reviewer.
