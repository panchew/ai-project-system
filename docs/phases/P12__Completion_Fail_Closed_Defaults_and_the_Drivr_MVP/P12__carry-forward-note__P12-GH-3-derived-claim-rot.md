---
project: ai-project-system
phase: P12
milestone: null
type: note
status: active
issuer_chat: HQ Chat (ai-project-system)
issued_to: unowned — filed, deliberately not scoped
last_updated: 2026-08-20
severity: high
---

# Carry-Forward Note — P12-GH-3: a citation that resolves, to content that has since become false. Nothing in this project re-derives a derived claim when its premise moves

**Found by the M41 Milestone Chat, generalized by the P12 Phase Chat, 2026-08-20**, from a defect in
the Phase Chat's own artifact. **Filed by HQ; explicitly NOT scoped.** Both chats declined to place it
themselves and named the reason — M44 must not become the place things get put. **Filing it is not
placing it.** This is SN-32's pattern: the record exists whether or not the fix is ever scheduled.

---

## The defect

**M41's finding F3 was true when written.** HQ's annotation to it was correct when made. Two
subsequent amendments were each correct at the moment they were made. **The defect is in none of them
individually.**

**`R6` changed the landing set, and three carried arguments silently became false.** Nothing detected
it. Nothing was designed to.

**Every citation involved still resolves.** The files exist, the sections exist, the anchors are
valid. **What moved is the content the citation was reasoning about.**

---

## Why it is the worst of a family of three

| Family member | Shape | Status |
|---|---|---|
| **Downward amendment** | A parent amends a spec a child is already executing | **`P11-GH-1`.** Mechanised as a **carrier** — see below |
| **Upward staleness** | A branch, or a **reader**, falls behind its parent | **Unowned.** Recorded in M41 v1.1.1. HQ demonstrated it against itself on 2026-08-20 |
| **Derived-claim rot** | A citation **resolves**, to content that has since become **false** | **This note. Previously unnamed.** |

**The third is the worst, and the reason is structural: a dangling citation is visible; a resolving
citation pointing at rotted content is not.**

**Every detection mechanism this project owns detects *absence*.** The divergence guards in
`tests/test_model_config.py` fail when a value is missing or disagrees. `test_starter_lint.py` flags a
branch reference that names no real milestone. `test_steering_note_id_uniqueness.py` catches a
duplicate ID. The branch-drift check the Phase Chat now runs per set detects commits not present.

**None of them detects staleness in something present.** A rotted claim passes every check this
corpus has, because nothing is missing.

---

## Why it belongs to this phase's thesis rather than beside it

P12's organizing finding is *when the evidence that should gate an action is absent, the action
proceeds.* **This is the same disposition with one word changed:**

> **When the evidence that should gate a claim has moved, the claim proceeds.**

It is not an analogy. It is the same failure at the level of the record rather than the level of
execution — and P12 has produced **four instances in a single milestone**, three of them in artifacts
authored by the reviewing level itself.

---

## Severity: High

**Not because any instance has cost anything yet.** Every one so far was caught one level down, by a
chat applying an artifact rather than reading it — the same detection path P11 recorded and the same
one whose durability P11 explicitly questioned.

**High because that detection path is a property of current attention, not of the system**, and
because the phase's own mitigations do not reach it. `P11-GH-1`'s channel carries an amendment to a
child; it does not tell anyone which *arguments* the amendment invalidated. The Phase Chat's per-set
branch-drift check detects absent commits; a rotted claim involves no absent commit.

---

## Explicitly not scoped, and the reason is on the record

**HQ has spent this phase warning that M44 must not become "the milestone things get put in"** — the
pattern HQ named in the 2026-08-05 ruling and the CFO then had to resolve structurally by inserting
M37 into P11. **Both the Phase Chat and the M41 chat invoked that warning against their own finding
and declined to push it.** That is the correct instinct and HQ will not override it by filing the
finding into a milestone instead.

**What a remedy would have to do, recorded so a future scoping starts from something:** detect that a
claim's premise has moved, in content that is present and resolves. Every existing mechanism here is
an absence detector, so this is not an extension of one — it is a different kind of check, and nobody
has proposed its shape.

*Trigger: any scoping conversation about verification mechanisms; or a fifth instance.*
