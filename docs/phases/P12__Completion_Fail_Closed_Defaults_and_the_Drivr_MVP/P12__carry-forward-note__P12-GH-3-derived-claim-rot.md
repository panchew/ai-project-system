---
project: ai-project-system
phase: P12
milestone: null
type: note
status: active
issuer_chat: HQ Chat (ai-project-system)
issued_to: unowned — filed, deliberately not placed
last_updated: 2026-08-20
severity: medium
---

# Carry-Forward Note — P12-GH-3: derived-claim rot — nothing re-derives a derived claim when its premise moves, and a citation that still resolves gives no sign

**Origin: the M41 Milestone Chat**, generalizing a defect in the P12 Phase Chat's own artifact (V2).
**Verified and sharpened by the Phase Chat**, which then **declined to place it in M44** and asked HQ
to file it instead. **HQ agrees on both counts** and is filing it here.

**Filed, not placed.** See Placement.

---

## The defect

**A claim derived from a premise is not re-derived when the premise moves.** Every instance was
**correct when written**. None is a mistake. **The composite is wrong anyway**, because each was
computed against a premise a later act changed, and nothing recomputed.

**Four instances, one milestone, four different substrates:**

| Instance | Whose | Substrate | Premise that moved |
|---|---|---|---|
| **F3's file list** | M41 Milestone Chat | An epic-set finding | HQ's annotation narrowed the collision to two keys |
| **A branch behind its parent** | the branch | Git | `master` advanced |
| **Decision 11's negative-only bar** | **HQ** | A ruling's acceptance clause | The detector's definition was never re-derived |
| **E41.1 v1.0.2's *"citation does not yet resolve"*** | M41 Milestone Chat | A spec's own Note | **#221 merged** |

**The fourth is the cleanest specimen the project has.** E41.1 recorded, accurately, that the R6
citation did not resolve on its branch. #221 merged; the premise moved; the claim did not. The chat
found it in its own artifact while pulling the sync, fixed it at v1.0.3, and **kept the account rather
than the outcome** — writing into the spec that nothing detected the staleness, that it was told, and
that the repair was manual.

---

## The mechanism — and this formulation is the M41 Milestone Chat's, quoted because it is better than HQ's

HQ and the Phase Chat both initially read the S1 → V2 → Decision 11 sequence as **three levels
catching each other**, which is flattering and wrong. **The M41 chat's reading is that it is one
defect written three times, each level inheriting the framing rather than the reasoning:**

> *"Flag the known failures" is the obvious way to specify a detector, and it is wrong in the same way
> each time — **a detector is defined by discrimination, not by detection.** Nobody re-derived it
> because **it did not look derived; it looked like a requirement.**"*

**That last clause is the mechanism, and it unifies all four instances.** In each case a
**conclusion** was written in a form that does not read as a conclusion, so nothing ever triggered
re-derivation:

- *"Three divergence guards enforce it"* — **reads as a fact.**
- *"The citation does not resolve"* — **reads as a fact.**
- *"Flag both recorded historical failures"* — **reads as a requirement.**

All three were conclusions from premises that later moved.

**The statement of the defect, adopted verbatim from the M41 Milestone Chat:**

> **The corpus has no convention that marks a claim as derived, so nothing signals when its premise
> moves.**

**EXTENDED 2026-08-21, and this framing is more useful than the one above.** Also the M41 Milestone
Chat's, carried by the Phase Chat rather than left in a message:

> **A correction is itself a derived-claim event, and nothing in the corpus treats it as one.**

**Three instances, three substrates, one mechanism** — F3's file list (the Phase Chat's), E41.1's
`Dependencies→Blockers` line (the M41 chat's), and the sweep that named it (its twin's). **Each party
corrected the thing in front of it, and none asked what else rested on the premise it had just
falsified.**

**This sharpens what a remedy must cover.** Not merely *detect a premise moving* — that frames the
premise as changing on its own. **Every correction IS a premise moving, performed deliberately, by
someone who knows they are doing it.** The moment of highest risk is the moment of highest attention,
which is why the defect survives careful work. **A remedy that watches for drift and does not treat
corrections as first-class drift events will miss the instances this project actually produces.**

---

## EXTENDED 2026-08-23 — a fourth family member, and a constraint on any remedy

**Three additions, all from the level below, all verified by HQ before recording.**

### (a) The restatement variant — the amendment ARRIVED and was read anyway

**The E41.2 Epic Chat's Delivery Notice asserted accept-by-silence**, suspended by `ad6e3f1` —
**which is an ancestor of its branch point `575b0fd`, and the ruling file was tracked on its branch
throughout.** Verified by HQ.

**Nothing was stale. Nothing moved.** It read a surface that **restates** the rule instead of the
corpus that **holds** it.

> **The backstop checks whether the SPEC moved. It does not check the rules a STARTER RESTATES, and
> a restatement is a copy with no link back to its source.** *(P12 Phase Chat)*

**And the constraint that makes this bind on M43's own remedy rather than merely evidence it:**

> **The restatement is not optional. `P12-GH-1` is why it exists** — the templates carry the rework
> rule zero times, so every starter restates it. ***The mitigation for one defect is the mechanism of
> another.*** *(P12-M41 Milestone Chat)*

**So E43.3's consolidation is constrained, not merely justified: every restatement it cannot remove
becomes a new dependency of exactly this kind** — and a consolidation that removes most of them
leaves the survivors *looking deliberate*, which is harder to audit than a uniform mess.

### (b) False absence — a zero that was never evidence

**HQ committed this defect while filing this note.** A literal grep for `accepted by silence` in the
E41.2 starter returned **0**; the rule is at line 44 as `accepted **by silence**`, split by markdown
emphasis **and** by a line wrap. **Three mechanisms defeat one sentence.** A second instance the same
week: `**Execution Mode:** manual` scores **0** against `Execution Mode: manual`, and a contract sweep
nearly reported a gap on it.

> ***A false positive announces itself; a false absence looks like a clean result.*** *(P12-M41
> Milestone Chat)*

**This is the corpus's own Hard Constraint firing** — *falsify a pattern before trusting a zero
result* — **against the party quoting it.** Markdown emphasis mid-phrase is a fifth variant beside
`\b` against `__`, `--include='*.py'` skipping `bin/`, and reflow-fragile literal guards. **It is the
nastiest of them, because the rendered text reads perfectly: a human reviewing the file sees the
rule; only the grep does not.**

### (c) The constraint on any remedy, and it outranks the instances

> **"In three consecutive rounds the finder was never the author. Whatever this project builds to
> catch premise-dependents, it should assume the author cannot run it on themselves."** *(P12-M41-E41.1
> Epic Chat)*

**Instance count is now eight across four levels, and every one was caught downstream. None by a
check.** Three are HQ's own: a branch-staleness claim re-used without re-measuring, Decision 11's
negative-only bar, and Decision 17's premise that a qualification run dispatches through the agentic
lane — **falsified by E41.2's runs, which never invoked the orchestrator.**

**A plainer form of the same constraint, from HQ against itself:** *the author is also the reader
least likely to re-read.* **A ninth instance was HQ misreading a gate in a spec HQ wrote** — asserting
`M44 → M45` where the spec says M43 and M44 are independent. **The premise never moved. It was read
wrong.**

**This is a design requirement on M44/M46, not an observation about diligence:** a premise-dependent
detector that the author runs on their own work is answering the wrong question.

---

## Why it is the worst of the three, and the reason is structural

The corpus now has three members of one family. **Two are named; this is the third and it was
unnamed:**

| # | Family member | Status |
|---|---|---|
| 1 | **Downward amendment** — a spec amendment does not reach a branch already executing | `P11-GH-1`, open. Mitigation exists and is a **carrier, not a detector** |
| 2 | **Upward staleness** — a branch, or a reader, drifts behind its parent | Recorded under `P11-GH-1`; **unowned**, no mechanism |
| 3 | **Derived-claim rot** — a claim's premise moves and the claim is not recomputed | **This note. Previously unnamed.** |

**The Phase Chat's statement of why the third is worst is the finding, and HQ quotes it rather than
paraphrasing:**

> **A dangling citation is visible; a resolving citation pointing at rotted content is not.** Every
> mechanism here detects *absence*; none detects staleness in something *present*.

That is exactly right, and it explains why the project keeps catching members 1 and 2 while member 3
accumulates silently. **`git cat-file -e` proves a citation resolves. Nothing proves what it resolves
to still supports the sentence citing it.** The P12 corpus is dense with cross-references precisely
because this project values traceability — which means the surface area for this defect grows every
time the record improves.

**It is `P11-GH-2`'s time axis with the sign flipped.** `P11-GH-2` is *a claim verified in one
tier/time/scope and asserted about another.* This is *a claim correctly verified at its own time, and
never re-verified as time moved underneath it.* Same axis, opposite direction: not verified in the
wrong place, but verified in the right place and left there.

---

## Severity: Medium

**Not High:** every instance so far was caught, all within one milestone, and none reached delivery.
**Not Low:** the catches were performed by chats reading carefully, not by any mechanism, and the
detection story is strictly worse than for the two named siblings — **for those, something is missing
and can be looked for; here, everything is present and merely wrong.**

---

## Placement: FILED, NOT PLACED — and HQ states why, because declining is the decision

**HQ declines to scope this in M44, adopting the Phase Chat's reasoning, which is HQ's own reasoning
returned to it:**

1. **A bounded deliverable now EXISTS — and it is the stronger reason to decline, not a reason to
   place it.** The sharpening supplies one: *a convention that marks a claim as derived, so a reader
   or a check can tell what it depends on.* **The M41 chat's own objection to it is decisive, and HQ
   adopts it: a convention with no mechanism to detect an unmarked claim is `P12-GH-1` reproduced** —
   a rule that lives in one place, is authoritative there, and whose omission no test detects. **That
   is the defect M43 exists to fix. Shipping a second instance of it inside M44 would be the phase
   contradicting itself.** Making it *enforceable* is not small.
   - **And it collides with a deferral already on the record.** SN-30 Recs 4 and 5 — reduce
     exposition, then measure the reduction — are deferred pending a spine conversation. **A notation
     convention adds exposition to every claim in the corpus.** That trade belongs in the conversation
     already waiting for it.
2. **Placing it would be HQ doing the thing HQ has twice declined to do.** M44 is the milestone HQ has
   repeatedly warned must not become *"the milestone things get put in."* A phase-scale finding with
   no deliverable is precisely the shape that pattern takes.
3. **P12 will produce more evidence than a remedy designed now would rest on** — the same reasoning
   that keeps `P11-GH-1` open and unscoped (opening ruling, Decision 12). Three parallel tracks and
   five remaining milestones are still to run.

**Trigger:** any work that proposes a mechanism for staleness in the corpus — including any scoping of
`P11-GH-1`'s unowned upward-staleness half. **The three members should be addressed as one family or
not at all**; a remedy for any one of them that does not account for the other two will look complete
and will not be.

**Owner: none.** Deliberately. The next spine conversation inherits it — the same one SN-30 Recs 4-5
are waiting for, which is not a coincidence.

---

## This note was briefly an instance of its own finding

**Recorded because it is the best available evidence, and because deleting the trace would be the
defect again.**

As first written, this note said the finding had **"no bounded deliverable yet."** That was true when
written. The M41 Milestone Chat's sharpening then **supplied one** — and had HQ not been told, the
note would have gone on asserting the absence of a thing that now exists, **in the very artifact
filing the defect of claims outliving their premises.**

**It rotted within the hour, in the note about rotting, and nothing detected it.** HQ was told. The
repair was manual. **That is the fourth instance's mechanism reproduced by the fifth**, and it is why
the trigger below is written to fire on any staleness mechanism rather than on this note's own
subject matter.

---

## A note on how this was found, and it is the part worth keeping

**The chain found it, and each level did something different with it.** The M41 Milestone Chat
generalized it from a defect in its **parent's** artifact. The Phase Chat verified it, judged it out
of scope for the milestone it was about to plan, and **routed it up rather than absorbing it** —
naming, correctly, that absorbing it would have been the error HQ had twice warned against.

**No level in that sequence re-decided above its station, and no level dropped it.** SN-33 records a
Steering Note that reached its target and left no mark; this is the same mechanism working. It is
recorded because P12's organizing finding is that systems proceed when they should stop, and this is
the chain stopping when it should — three times in two days.
