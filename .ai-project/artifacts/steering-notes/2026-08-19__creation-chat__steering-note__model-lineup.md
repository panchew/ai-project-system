---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-08-19T23:00:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-38
    severity: medium
    title: Target per-level model line-up ruled by the CFO — three same-tier mapping edits, one policy-row change closing row P4, one row still gated by SN-37
decisions:
  - "Target line-up ruled by the CFO 2026-08-19. Creation: fable-5. HQ: opus-5 (unchanged). Phase: GPT-5.6 Sol. Milestone: Deepseek V4 Flash. epic_manual: Qwen3.8:27b."
  - "Milestone -> Deepseek V4 Flash is a POLICY-ROW CHANGE by CFO decision, not a mapping refresh, and it CLOSES model-routing-policy.md row P4 — open and awaiting the CFO's timing since P10. It must be recorded as a ruling, never filed as a same-tier refresh."
  - "Creation -> fable-5 and Phase -> GPT-5.6 Sol are SAME-TIER vendor moves: mapping-table edits under the 2026-07-28 precedent, TIER rows untouched, no new evidence required."
  - "epic_manual -> local:qwen3.8:27b. Every Epic chat, manual and agentic, now runs local — consistent with the standing goal that local execution is control at the finest grain."
  - "RULED by the CFO: SN-37's gate binds MANUAL-CHAT VERIFICATION TARGETS AS WELL AS dispatch lanes. The Creation Chat's narrower lanes-only proposal is superseded. Two harnesses follow, because the checks do not transfer: lanes are qualified by detecting SUCCESSFUL NOTHING; verification targets by detecting FAILED JUDGMENT — planted defects, catches vs false alarms — which is E35.5's back-test and already exists."
  - "Consequence, accepted: four of the five line-up rows now require a qualification run before they land (creation, phase, milestone, epic_manual). Only hq moves freely, because it does not move. The wider scoping is what makes milestone -> Deepseek V4 Flash measurable — E35.5's back-test was built for milestone-level judgment, so the CFO's two rulings compose."
  - "CFO DIRECTION: collect the model evidence FIRST, as an early step of P12, explicitly inserted after the phase opened — his call to make. Placement is HQ's; the measurement is not optional."
  - "The qualification must measure epic_dev and epic_qa SEPARATELY, and must measure the INCUMBENT (qwen3-coder:30b) to establish the relative bar's baseline."
  - "Premise correction, on the record: qwen3-coder:30b has NEVER been compared against any 27b. E33.2 compared 14b vs 30b. E35.5's PASS 4/5 with zero false alarms belongs to qwen3.6:27b, chosen deliberately as a general reasoning model for judgment work. The only milestone-level judgment result this project owns belongs to a 27b."
  - "epic_dev and epic_qa are NOT one question. epic_dev stays qwen3-coder:30b — it owns the only mergeable-work evidence. epic_qa is the row with a live problem: E39.3 records that the same model FABRICATED ITS EVIDENCE on the first real QA run ever captured — VERDICT: PASS, zero tool rounds, citing a key the file does not contain, with the read-only tools genuinely advertised."
  - "NO MODEL SWAP LANDS UNTIL M41 CLOSES. M41 repairs the code the lane runs through; changing the model during the repair makes the next failure unattributable. Same reasoning as the phase's own M41 -> M46 binding order, one level down."
references:
  - ".ai-project/artifacts/steering-notes/2026-08-19__creation-chat__steering-note__drivr-ux-and-model-qualification.md — SN-37, the gate this note scopes."
  - ".ai-project/artifacts/reference/token-measurement/model-routing-policy.md — row P4 and the Change discipline."
---

# Steering Note — Creation Chat to HQ Chat

## Purpose

The CFO ruled the target per-level model line-up on 2026-08-19, explicitly to remove friction later:
*"I don't want to go through friction when I need to setup the models."* This note records it, sorts
it into the three kinds of change it actually contains, and routes the execution.

**No configuration change is made by this note.** The Creation Chat holds no authority to edit
`.ai-project.yml` (Seed Rule 3). The edit belongs to HQ, inside P12, on a deliberate branch.

---

## SN-38 — The line-up, and what each row costs [MEDIUM]

| Key | Current | Target | Kind of change |
|---|---|---|---|
| `creation` | `remote:claude-opus-5` | **fable-5** | Same-tier mapping edit |
| `hq` | `remote:claude-opus-5` | **opus-5** | No change |
| `phase` | `remote:claude-opus-5` | **GPT-5.6 Sol** | Same-tier mapping edit |
| `milestone` | `remote:claude-opus-5` | **Deepseek V4 Flash** | **Policy-row change — closes row P4** |
| `epic_manual` | `remote:claude-opus-5` | **Qwen3.8:27b** (local) | Tier change, manual target |
| `epic_dev` | `local:qwen3-coder:30b` | *unchanged pending SN-37* | Gated |
| `epic_qa` | `local:qwen3-coder:30b` | *unchanged pending SN-37* | Gated |

### What every reader of this table needs to know first

**Five of these seven keys are manual-chat verification targets**, not routing. `creation`, `hq`,
`phase`, `milestone` and `epic_manual` each cause a chat at that level to **halt** if it opens on a
model that disagrees with the declared value (P9-M31-E31.3). Only `epic_dev` and `epic_qa` are
dispatch lanes, and the spec says so in terms — *"Agentic dispatch lane only — not a manual-chat
verification target."*

So this change routes nothing. **It arms a set of fail-closed checks.** That is the intended
behaviour and it is protective, but it is immediate: the moment `creation` moves to fable-5, the next
Creation Chat session halts unless it is opened on fable-5. The same applies at every other level.

### Three same-tier mapping edits

`creation → fable-5` and `phase → GPT-5.6 Sol` keep paid frontier at paid frontier and move only the
vendor. **Direct precedent exists:** the 2026-07-28 HQ Ruling moved all five paid-frontier keys from
`claude-opus-4-8` to `claude-opus-5` and was recorded as *"a same-tier version refresh... The
policy's TIER rows (P1–P4) are untouched — only its mapping table."* These are the same shape.
Mapping-table edit, no new evidence obligation. `hq` is unchanged.

### One policy-row change — and it closes an item open since P10

**`milestone → Deepseek V4 Flash` is not a mapping edit, and HQ must not record it as one.**

Milestone is where **Stage-2 accept authority** lives, and that is the stated reason
`model-routing-policy.md` row P4 reads paid frontier — *"the level whose errors propagate into
merges."* A "Flash" tier is a tier change, so the Change discipline applies.

**The Creation Chat raised this; the CFO reaffirmed it. That is the decision, and it is his to
make.** The authority is not in question — what matters is that the record says what happened.

**The useful consequence: this closes row P4.** The 2026-08-17 Progress Digest lists row P4 as *"Not
decided... A further HQ call, on the CFO's timing."* The timing is now. HQ should record this as a
**CFO ruling on row P4**, with the Change discipline satisfied by CFO decision rather than by cited
evidence — and should say so plainly, rather than filing it as a same-tier refresh, which it is not.

### One tier change at the Epic level

`epic_manual → local:qwen3.8:27b`. Combined with the already-local dispatch lanes, **every Epic
chat now runs local, manual and agentic alike.** This is consistent with the CFO's standing goal —
local execution as control at the finest grain — and is recorded as intentional rather than
incidental.

**One interaction HQ should hold while scoping, stated once and not as an objection.** Epic drops to
a local 27b at the same time as Milestone — the level that *reviews* Epic — drops from paid frontier
to a Flash tier. The reviewer and the reviewed move down together. P11's own phase record concludes
that *"the review chain caught every HQ error"* and that each was caught *"one level down, by a chat
applying HQ's output rather than reading it."* That chain is currently the system's main defence, and
this change reduces the capability on both of its sides at once. Not a reason to refuse; a reason for
P12's M46 — the first real agentic integration — to be watched closely rather than assumed.

### The two Epic rows are not one question — the evidence splits them

The CFO asked whether the choice is *"collect evidence then switch"* or *"stay on `qwen3-coder:30b`
since we already have firm ground and measure for progress."* **Neither, because `epic_dev` and
`epic_qa` hold the same string today and the record treats them differently.**

| Task | Model | Result on record |
|---|---|---|
| Code implementation (`epic_dev`) | `qwen3-coder:30b` | **Two real epics, mergeable work** — E33.2 Run B, E33.4 |
| QA / judgment (`epic_qa`) | `qwen3-coder:30b` | **Fabricated its evidence** — E39.3 |
| Review / judgment | `qwen3.6:27b` | **4 catches of 5, one SPLIT, zero false alarms**, ten runs — E35.5 |

**The `epic_qa` row is the load-bearing correction.** E39.3's delivery notice records that the
dispatch ran on *"`.ai-project.yml`'s `models.epic_qa` (`local:qwen3-coder:30b`)"*, that the
read-only tools **were** advertised to the model, and that the run returned `VERDICT: PASS` with
**zero tool rounds**, citing a top-level key the file does not contain. Its verdict, verbatim:

> **"The lane exists and works; the model in it fabricated its evidence."**

**So "firm ground" is true of `epic_dev` and false of `epic_qa`.** The incumbent has the only
mergeable-work evidence in the project *and* the only recorded fabrication, on the first real QA run
ever captured. The distinction has been invisible because one string fills both keys.

#### Recommendation to HQ

1. **`epic_dev` stays `qwen3-coder:30b`.** It owns the only mergeable-work evidence. Nothing in the
   public claims about newer models justifies disturbing the one row that is working.
2. **`epic_qa` is the row with a live problem.** For it the qualification run is **confirmation, not
   discovery** — the evidenced alternative (`qwen3.6:27b`) is already installed, and the incumbent
   has a recorded failure at exactly this task.
3. **No swap lands until M41 closes.** M41 repairs the code the lane runs through. A model change
   and a lane repair landing together makes the next failure unattributable — the same reasoning as
   the phase's own M41 → M46 binding order, one level down.
4. **`qwen3.8:27b` enters as a candidate, not a conclusion** — verify presence on the host first,
   then let it compete against `qwen3.6:27b`, which already holds the judgment result.

#### What tempers the urgency, and should be said so nobody over-corrects

**E39.1's binding decision is that no model-generated judgment may be load-bearing.** Today the QA
model's verdict corroborates; it does not authorize. A weak `epic_qa` model cannot by itself break
anything. **The row matters because M44 exists to make that judgment trustworthy** — the choice is
about which model M44 builds on, not about a live wound. That is a reason to measure carefully
rather than to hurry.

#### Correcting the premise this note was nearly built on

**No comparison between `qwen3-coder:30b` and any 27b has ever been run.** The CFO asked directly
whether the 30b had beaten `qwen3.6:27b`; it has not, and the record says so:

- **E33.2 (P10-M33) compared `qwen2.5-coder:14b` against `qwen3-coder:30b`.** Run A returned
  *"exit 0 / 'completed' while delivering nothing"*; Run B produced mergeable work. **No 27b was in
  that run.** This is the entire evidentiary basis for the current `epic_dev`/`epic_qa` value.
- **E35.5's back-test — 4 catches of 5, one SPLIT, zero false alarms, judgment PASS — was run on
  `qwen3.6:27b`.** E38.5 records this as a load-bearing finding: the 27b *"was chosen deliberately:
  it is a general reasoning model, which is what Stage-2 review is — `qwen3-coder:30b` is
  coder-tuned"*, and the 30b was only *"an optional comparator, if running it is cheap."*

**So the only milestone-level judgment result this project owns belongs to a 27b, not to the model
currently configured.** That materially favours the CFO's direction and is recorded here because an
earlier draft of this note understated it as a VRAM-fit speculation.

**Three caveats, so this is not over-read in the other direction.** `qwen3.6:27b` is present in
Ollama but **declared nowhere in `opencode.json`** (verified 2026-08-08), so it is not routable
through the execution adapter without a config addition. **E35.5's own delivery notice records six
arguments against over-reading its PASS**, and E38.5 instructs readers not to lean on it. And
**`qwen3.8:27b`'s availability on this host is unverified** — no check has been run.

Capacity context, unchanged: `qwen3-coder:30b` (Q4_K_M, 18.6 GB) **exceeds this host's 16 GB VRAM and
partially offloads to RAM** (12.9 GB VRAM / 21.4 GB total, ~9.4 tok/s end-to-end).

#### A finding the current configuration masks

E35.5 chose a general reasoning model over a coder-tuned one **because the job was judgment, not
code.** `epic_dev` and `epic_qa` are separate keys for exactly that reason — and they currently hold
**the same value**, which hides the distinction. A coder-tuned model for implementation paired with a
general reasoning model for verification may be the correct answer, and **nothing in the record has
tested that pairing.** The qualification gate should measure the two keys separately rather than
qualifying "the Epic model" as one thing.

#### Why hype cannot substitute for the gate

The CFO's stated reason for pushing `qwen3.8:27b` is public claims of frontier-level capability, and
similar claims for Deepseek V4 Flash. **This chat cannot verify either claim and does not attempt
to.** More usefully: **capability is not the axis that has failed here.** The 14b emitted a
well-formed JSON *plan* and changed nothing. E39.3's dispatches returned `VERDICT: PASS` with **zero
tool rounds**, citing a configuration key the file does not contain. Both would read as competent on
any capability benchmark; both failed at **agentic discipline** — actually calling tools, actually
touching files — which is orthogonal to reasoning quality.

That is why SN-37's first check is *detect successful nothing*, and why a hype-driven swap without
the gate collects the one kind of evidence that does not answer the question.

### SN-37's scope — RULED: the gate binds verification targets too

The Creation Chat proposed the narrower scoping — gate binds dispatch lanes only, on the grounds
that its checks (tool rounds > 0, files changed > 0, claims resolving) are meaningless for a chat a
human drives. **The CFO ruled the wider scope: the gate binds manual-chat verification targets as
well.** Recorded as decided; the proposal is superseded.

**The ruling requires two harnesses, because the checks genuinely do not transfer.**

| Kind | Keys | What qualifies it | Status |
|---|---|---|---|
| **Agentic dispatch lane** | `epic_dev`, `epic_qa` | Detect *successful nothing* — tool rounds > 0, files changed > 0, claims resolving against files that exist | To be built |
| **Manual verification target** | `creation`, `hq`, `phase`, `milestone`, `epic_manual` | Detect *failed judgment* — planted defects, catches versus false alarms, on the review work the level actually performs | **Already exists — E35.5's back-test** |

A manual chat has no unattended run, so "did it call tools" measures nothing there. **"Did it catch
the planted defect" is the right question, and the instrument is built**: E35.5's back-test scored
`qwen3.6:27b` at 4 catches of 5, one SPLIT, zero false alarms across ten runs, and the 2026-08-17
Progress Digest confirms the harness *"remains available."*

**The ruling's strongest consequence, and the reason it is better than the proposal it replaced.**
`milestone → Deepseek V4 Flash` is the highest-risk row in this note: Milestone holds **Stage-2
accept authority**, which is the stated reason `model-routing-policy.md` row P4 reads paid frontier,
and the move is toward a Flash tier on public capability claims. **E35.5's back-test was built to
measure milestone-level judgment.** The wider scoping therefore supplies exactly the evidence the
row P4 decision otherwise lacked — which the narrower scoping would have excluded. **The CFO's two
rulings compose: the second makes the first measurable.**

**The honest cost, recorded rather than glossed.** Four of the five line-up rows now require a
qualification run before they land — `creation`, `phase`, `milestone`, `epic_manual`. Only `hq`
moves freely, because it does not move. This is more up-front work than lanes-only scoping, and it
converts friction discovered at setup into friction scheduled in advance. That is the trade the CFO
chose, stated so nobody reopens it as an oversight.

**One distinction for HQ, so the two mechanisms are not conflated.** The **model check**
(P9-M31-E31.3) verifies that the *running* model matches the *declared* one. The **qualification
gate** (SN-37) verifies that the declared model is *fit*. Both fail closed; they answer different
questions, and a pass on either is not a pass on the other.

---

## CFO direction — evidence before the Epic-row swap, inserted into an open phase

**The CFO directs that the model evidence be collected first, as an early step of P12, and is
explicit that inserting it after the phase has opened is his call to make.** Recorded as direction,
not as a proposal.

**It is cheap, and three of its four inputs already exist.** E35.5's back-test harness is built and
the digest confirms it *"remains available"*; `qwen3.6:27b` is already installed; the relative bar
agreed in SN-36/37's amendment gives a defined pass condition without inventing a number. What is
missing is only the run.

**What it should measure, given the findings above:**
1. **`epic_dev` and `epic_qa` separately**, not "the Epic model" as one thing.
2. **The incumbent first** — `qwen3-coder:30b` — since the bar is relative and there is currently no
   baseline for it on the judgment task.
3. **`qwen3.6:27b` as a real candidate, not a footnote.** It holds the only judgment result on
   record.
4. **`qwen3.8:27b` if and only if it is available on this host** — verify before scoping around it.

**One sequencing fact for HQ, stated so it is not discovered mid-run:** a qualification run
dispatches through the agentic lane, and **M41 is repairing the code that lane runs through.**
Docker is present on this host, so the unsandboxed fallback (`bin/ai-project-orchestrator:397`) will
not fire and the measurement is safe to take. The dependency is real but not blocking; it should be
recorded rather than assumed away.

**Placement is HQ's call.** The gate currently lives in M45. Pulling the *measurement* forward while
leaving the *gate's construction* in M45 is one option; another is a small bugfix-shaped spike ahead
of M41. This note does not choose.

---

## Next Action

0. **Run the model evidence first**, per the CFO direction above — placement HQ's call, scope as
   listed.

1. **HQ executes the `.ai-project.yml` edit** inside P12, on a deliberate branch — five keys change,
   two do not. `.ai-project.yml` is untouched by PR #215, so there is no conflict with the
   phase-opening PR.
2. **Record `milestone → Deepseek V4 Flash` as a CFO ruling on `model-routing-policy.md` row P4**,
   satisfying the Change discipline by decision rather than by evidence, and **update the policy's
   mapping table and row P4 together.** Do not file it as a same-tier refresh.
3. **Confirm or reject the SN-37 scoping** above before the gate is built, since it determines what
   the gate is for.
4. **Verify `qwen3.8:27b` is available on this host** before the gate's first run, and measure the
   incumbent as the relative bar requires.
5. **Warn every level before the edit lands.** Five verification targets arm simultaneously; a chat
   opened on the old model after the edit halts by design. That is correct behaviour and a poor
   surprise.
