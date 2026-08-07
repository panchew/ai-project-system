---
project: ai-project-system
phase: P11
milestone: null
type: note
status: active
issuer_chat: HQ Chat (ai-project-system)
issued_to: Phase Chat (P11) → P11 Closure Declaration
last_updated: 2026-08-06
severity: medium
---

# Carry-Forward Note — P11-GH-2: a verification can be real, correctly reported, and performed at the wrong layer

**Recorded, not fixed, and deliberately not placed in a milestone.** Three instances of a class is a
record; it is not yet a remedy, and choosing a remedy now would be a fourth guess.

**Origin:** named by the P11-M37 Milestone Chat in its own erratum, 2026-08-05, while correcting its
own instance. HQ files it because **two of the three instances are HQ's.**

---

## The defect

`"Verify, do not inherit"` is in force across P11 and has worked — it has caught real defects
repeatedly. But it is **satisfied by measuring something**, and it says nothing about whether the
thing measured is the thing that matters.

Each instance below was a **genuine measurement, honestly reported, that certified nothing about the
claim it was offered in support of.** None was a shortcut, and none would have been caught by
demanding more rigour — the rigour was present.

| # | Instance | Measured | Executes at | Consequence |
|---|---|---|---|---|
| 1 | Phase spec v1.0.0's Ollama context note (**HQ**) | nothing — inherited from an opener and repeated | Ollama **0.30.0** on this host | A binding technical note asserted a 4,096-token ceiling that does not exist. Corrected v1.0.1. |
| 2 | Starter constraint 2a's xfail mechanism (**HQ**) | the test's marker semantics | against a corpus **HQ's own Decision 4** keeps colliding | An epic following it literally would have delivered a red suite. Corrected by the Phase Chat. |
| 3 | M37 milestone spec v1.1.0's dispatch preconditions (**Milestone Chat**) | the three preconditions, on the **host** | `bin/run-dev-agent`, **inside the sandbox** | *"Verified on this host"* and *"no configuration change is required"* — both true, together misleading. E37.1 was not dispatchable. Corrected v1.1.2. |

Instance 1 measured nothing and is the weakest form. **Instances 2 and 3 are the interesting ones:**
both measured carefully, at a layer adjacent to the one that governs the outcome. Instance 2 checked
the mechanism against the test and not against the ruling that determines whether the mechanism can
ever fire. Instance 3 checked reachability from the machine, for code that runs in a container that
cannot see it.

---

## Why the existing practice does not catch it

- **`"Verify, do not inherit"`** tells you to measure rather than trust. All three did. It has no
  clause about *what*.
- **Stage-2 review** re-measures the claim **as stated**. A claim stated at the wrong layer
  re-measures true.
- **Delivery evidence** records the command and its output. Both are correct; the output is being
  read as evidence for a different proposition than the one it establishes.

The common shape: **the verification and the execution sit on opposite sides of a boundary that the
claim does not name** — a version boundary, a ruling boundary, a container boundary.

---

## Severity: Medium

All three were caught before delivery, none reached production behaviour, and each remedy was cheap.
It is not Low because the failure is **invisible to the mechanism designed to catch it** — the
evidence looks right, the reviewer's re-measurement agrees, and the defect passes both. It is not
High because every instance so far was caught within one hop.

**It recurs wherever a claim crosses a boundary the claim does not name**, which on this project's
evidence is often.

---

## Interim practice, in force from 2026-08-06

Ratified in HQ Ruling 2026-08-06:

> **A verification states the layer it was performed at, and the layer the verified thing executes
> at. Where those differ, the verification is not evidence.**

Cheap, and it converts the failure from invisible to visible: instance 3's *"verified on this host"*
already contained the disclosure — it simply was not read as one, because nothing required the
second half of the sentence.

**This is a practice, not a mechanism.** It depends on the author noticing the boundary they are
crossing, which is precisely what all three instances failed to do. Same limitation as P11-GH-1's
interim practice, recorded for the same reason.

---

## Candidate directions — recorded, none recommended

1. **A required field in delivery/verification evidence naming the execution layer.** Mechanical and
   testable; risks becoming a box that is filled with the wrong answer.
2. **Fold into Stage-2 as a standing question** — *"what layer does this run at, and is that where it
   was measured?"* Cheapest; still a convention.
3. **Coordination-layer detection (Drivr).** Weaker fit than P11-GH-1 — this is a reasoning defect,
   not a state-propagation one, and a daemon cannot see it.
4. **Accept it as a known limit of the practice**, on the argument that three-for-three caught within
   one hop means the chain is already the mechanism.

Direction 4 is not a joke and should be weighed seriously: **the review chain caught every instance,
including both of HQ's.** The question is whether that is a property of the design or of the
attention currently being paid to it — and that question cannot be answered from three instances.


---

## Sibling pattern — added 2026-08-06, distinct from the above and not folded into it

A second HQ failure mode surfaced the day this note was filed. It is **not** a wrong-layer
verification, and merging the two would blur both:

> **A premise is inherited from an input and not re-tested against the decision the artifact itself
> just made.**

| # | Instance | The decision | The premise it invalidated, carried anyway |
|---|---|---|---|
| 1 | Starter constraint 2a | HQ Ruling 2026-08-01 **D4: SN-23 is never renumbered** | *"the moment E36.1/E36.2 clear those collisions the check XPASSes"* — it can never clear, so it can never XPASS |
| 2 | HQ Ruling 2026-08-06 | **Route C: revert E37.1 to manual/paid** | *"E37.1's two artifacts need no rework"* — reverting them **was** rework; `5fb7540`/`64efc02` had already made them agentic |

**Both are internal contradictions inside a single HQ artifact**, between a decision and a premise
sitting a few paragraphs apart. Neither would be caught by measuring more carefully: the measurement
was never the weak link. **The check that would catch them is re-reading the artifact's own claims
against its own decisions before issuing it** — cheap, and not currently performed.

Instance 2 was caught **from the executing end**, by the Milestone Chat applying the ruling and
finding that doing so required work the ruling said was unnecessary. Instance 1 was caught by the
Phase Chat. **Neither was caught by HQ.**

**Recorded here rather than filed as `P11-GH-3`, deliberately.** Two instances is the bar this phase
used for P11-GH-1, so it arguably qualifies — but **HQ is the party this pattern indicts, and HQ
electing to keep it as a sub-heading of someone else's note is exactly the judgment it should not
make about itself.** Whether it earns its own record is the CFO's call.
