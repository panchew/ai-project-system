---
project: ai-project-system
phase: P11
milestone: null
type: note
status: active
issuer_chat: HQ Chat (ai-project-system)
issued_to: Phase Chat (P11) → P11 Closure Declaration
last_updated: 2026-09-03
severity: medium
---

# Carry-Forward Note — P11-GH-1: a mid-flight spec amendment lands on `master` and reaches no working branch

**Recorded, not fixed.** Closing this properly means changing how the framework's downward channel
works, which is a governance-capability change larger than anything in M36's scope and unrelated to
its subject. It is recorded here so it does not evaporate with the session that found it.

**Origin:** found by HQ on 2026-08-04, immediately after merging its own ruling — and then found
again, one level lower, within the same hour. Twice in two days is what turned it from an
observation into a gap record.

---

## The defect

`PROJECT-SYSTEM-GUIDELINES.md` §13D makes the spec file the sole downward channel:

> **Downward communication is the spec file, not broadcasting.** A parent communicates a directive,
> amendment, or correction by amending its own spec file; children — including those already
> mid-execution — read from that same source. One write, many readers.

**"That same source" is not the same file when branches are involved.** A parent amends the spec on
its own branch — for HQ, that is `master`. Every child cut its branch earlier and carries a **copy**
frozen at branch time. The parent writes once; the children read a different file and see nothing.

There is no mechanism, no obligation, and no check anywhere in the corpus that makes an amendment
propagate to branches already in flight. §13D describes a channel it does not implement.

---

## Both observed instances

| # | Amendment | Landed on | Branch that could not see it | Consequence had it not been caught |
|---|---|---|---|---|
| 1 | Phase spec **v1.0.2**, adding **E37.6** (HQ Ruling 2026-08-04) | `master` | `phase/P11` (at v1.0.1) | The Phase Chat plans **M37 with five epics instead of six**. The ruling silently fails to reach the chat it was addressed to. |
| 2 | The same ruling's **Decision 5** — the Closure Declaration must record M36's unrecordable amendments | `master` | `milestone/M36` | **E36.3 lands the second unrecordable amendment, M36 closes without naming either**, and the interim record the ruling made mandatory does not happen. |

Instance 2 is the sharper one. The M36 milestone spec **predates the ruling**, so the obligation
appears in no document the Milestone Chat reads, and its Closure Declaration DoD item says only
*"Milestone Closure Declaration produced (`is_final: false`)"*. **Nothing downstream was wrong.
Every chat was working correctly from the newest document it could see.**

---

## Instances recorded in P12 — cited by artifact and defect, never by ordinal

The instances above are P11's. **P12 produced further instances of the same gap**, and they are
recorded here — **each by the artifact and defect that identifies it, not by an ordinal**, because
the tally is ruled unusable (P11's closure counts four, this note records two, and the
count-error-tally record is reconciled at a floor rather than as a running integer). None of the
three below re-opens the fix: **this records evidence only** (opening ruling, Decision 12 — `P11-GH-1`
is not scoped as work in P12).

| Instance (artifact + defect) | Direction | Path by which it was caught | Recorded |
|---|---|---|---|
| **P12 phase spec on `governance/hq-p12-opening`** — cut from `master` at `19c77ab`, while SN-38 landed at `3eda074` and was amended at `afe5d79`, **both after the cut**; the phase spec on that branch carried **zero** occurrences of `SN-38`, `Deepseek` or `epic_qa` | downward (parent amends, child already executing) | **out-of-chain** — a **Creation Chat reading `master`**, not the level below and not any mechanism (SN-39) | resolved by merging `master` (`0a19563`) and reconciling before `#215` merged (`8f5fb7c`). **Facts from the P12 phase spec, not re-derived (P11-GH-2).** |
| **M41 milestone spec v1.1.0 citing the F6 ruling (`ff24a48`, on `master` at `f504be2`) in three places, while the file is absent from `milestone/M41`** | **upward** (a child branch drifts behind its parent while its own artifacts cite content the branch does not have) | the Phase Chat, directed by HQ, after HQ noticed — **a carrier, not a detector** | recorded in `P12-M41__milestone-spec.md` v1.1.1 (`2026-08-20`); the direction that makes it distinct is the gap's other half — *downward amendment is mechanised; upward branch staleness is unowned*. |
| **E41.1 spec v1.0.2's *"the R6 citation does not yet resolve on this branch"*** — true when written, because `#221` was unmerged; `#221` merged (`master` `f31ec78`) and the premise moved, and the claim was not re-derived | **derived-claim rot** (a claim's premise moves and the claim is not recomputed — `P12-GH-3`) | the M41 Milestone Chat, told by HQ; the repair was manual | corrected at E41.1 v1.0.3 (`2026-08-20`), which kept the account rather than only the outcome: nothing detected the staleness, HQ told, the repair was manual — **a resolving citation pointing at rotted content gives no sign**. |

**What makes P12's primary instance worth the entry rather than a tally mark:** it fired **inside the
phase that owns the gap**, on **HQ's own branch** (`governance/hq-p12-opening`), and was caught by a
chat **outside the parent chain** — a Creation Chat reading `master` — rather than by the
one-level-down review that caught every P11 instance. That is a **detection path unlike every case
on file** (`SN-39`), and it is the part a future remedy has to account for.

**The gap is left open and unscoped.** Recording these instances does not scope `P11-GH-1` as work;
it is the phase's deliberate decision to let three parallel tracks produce more evidence before a
remedy is designed. The gap remains **open and unscoped**, its severity medium.

**Amending a prior phase's carry-forward note from a later phase is established practice**
(`P10-GH-2`, `P11-M36-E36.5`) — the note is a living record, not a closed phase artifact.

---

## Why the existing machinery does not catch it

Each of these looks like it should cover the case, and none does:

- **§13D itself** names the spec file as the channel and stops. It is silent on branches — which is
  the whole gap, in the one section that would be expected to close it.
- **The amendment-history / changelog convention** records *that* a spec changed. It is only ever
  read by someone who already opened the newer copy.
- **Mid-flight amendment guidance** (Phase/Milestone starter templates) tells a parent to *amend the
  spec and notify its own parent* — it governs escalation **upward**, and says nothing about
  reaching the children the amendment is for.
- **Stage-2 review** happens at delivery, far too late: by then the child has already executed
  against the stale contract.
- **`git`** would surface it on merge only if both sides edited the same file. Here the child edited
  nothing, so the merge is clean and silent — **the absence of a conflict is exactly what hides it.**

---

## Severity: Medium, with a note on why not High

Both instances were caught, neither reached delivery, and the corrective action is a routine branch
merge with no conflicts. Nothing was lost.

It is not Low because the failure is **silent, systematic, and worst precisely when it matters
most** — the amendments most likely to be issued mid-flight are the ones a running child most needs.
It is not High because it is trivially detectable once anyone thinks to look, and the fix costs a
merge.

**It will recur on every phase long enough for HQ to rule mid-flight**, which — on this project's
evidence — is most of them.

---

## Interim practice, in force until this is closed

Adopted by HQ on 2026-08-04 and exercised the same day:

1. **When HQ amends a spec or issues a ruling that binds work in flight, HQ says so explicitly and
   names the branches that need it.** The amendment is not "communicated" by existing on `master`.
2. **The sync travels down the hierarchy, not sideways:** `master` → `phase/P#` → `milestone/M#`.
   Merging `master` straight into a milestone branch works but muddles provenance.
3. **The merge commit states what came down and what it binds**, so the receiving chat meets the
   obligation in its own history rather than having to diff two copies of a spec.

Worked example, both instances closed in one pass: `dd9b310` (`master` → `phase/P11`) and `82c69ab`
(`phase/P11` → `milestone/M36`).

**This is a practice, not a mechanism.** It depends entirely on HQ remembering, which is the same
class of failure as the unenforced ID allocation that SN-28 recorded and B3.1 fixed with a test. A
convention that relies on attention is what this project has repeatedly ruled is not enough.

---

## Candidate directions — recorded, none recommended

Deliberately not choosing. Whoever owns this should decide once, with the whole problem in view.

1. **A check that a working branch is not behind its parent on the spec file(s) it is governed by.**
   Mechanical and testable, in the spirit of B3.1. Needs care not to fire on every routine
   divergence.
2. **Make the sync an obligation of the amending level**, recorded in §13D — cheap, but still a
   convention, and it puts the work on the level least able to see which children exist.
3. **Make it an obligation of the receiving level** — re-read the governing spec from the parent
   branch at session start and at each epic boundary. Fits "children read from that same source"
   most literally, and puts the check where the reader is.
4. **Coordination-layer detection (Drivr, P11).** The gate queue is derived from governance state;
   "a child is executing against a superseded spec" is exactly the class of thing a coordination
   daemon should surface. **This is the most natural home and the reason this note is filed in P11
   rather than parked** — but it must not be assumed, since M39's scope is set and does not name it.

**Not scoped into M36.** M36's contents are CFO-fixed at four items, and this is neither a Steering
Note defect nor a re-instantiation defect. Direction 4 makes M39 a plausible home; that is the Phase
Chat's proposal to make and HQ's to rule, not this note's to assume.
