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

**A claim derived from a premise is not re-derived when the premise moves.** Every instance in P12 so
far was **correct when written**:

- **F3** was true when the M41 Milestone Chat wrote it.
- **HQ's annotation to F3** — that the `bin/` collision was two keys, not five — was correct when made.
- **The Phase Chat's two amendments** were each correct when made.

None of them is a mistake. **The composite is wrong anyway**, because each was computed against a
premise that a later act changed, and nothing recomputed.

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

1. **It is phase-scale and wants a spine conversation**, not a milestone. It has **no bounded
   deliverable yet** — "re-derive derived claims" is a discipline, not a task, and the remedy is
   probably mechanical (something that knows a citation's target changed since the citing sentence was
   written), which is a design problem nobody has framed.
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

**Owner: none.** Deliberately. The next spine conversation inherits it.

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
