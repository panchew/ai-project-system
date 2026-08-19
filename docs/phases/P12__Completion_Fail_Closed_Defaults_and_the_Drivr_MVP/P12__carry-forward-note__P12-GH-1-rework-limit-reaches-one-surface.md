---
project: ai-project-system
phase: P12
milestone: null
type: note
status: active
issuer_chat: HQ Chat (ai-project-system)
issued_to: P12 Phase Chat → M43
last_updated: 2026-08-19
severity: medium
---

# Carry-Forward Note — P12-GH-1: the rework limit reaches one starter surface of nine, zero templates, and now has two contradictory extension semantics

**Origin: SN-32 (Creation Chat, 2026-08-18).** Filed here as a gap record in HQ's numbering per that
note's own Required action — **separately from the consolidation that fixes it**, because the
consolidation is scoped into M43 and a deferred fix must not take the defect's record with it.

**Re-measured by HQ on `master` at `19c77ab`, 2026-08-19.** Two of SN-32's figures do not survive
re-measurement. The substantive finding does. Both are recorded below, because a gap record that
inherits an unverified count is the defect this project has now filed twice (`P11-GH-2`).

---

## The defect

**The only mechanism bounding rework loops is not delivered to the chat that must enforce it.**

`governance/systems/milestone-execution-chat-starter.md` states the rule, at lines 330-335:

> **Maximum 3 attempts.** If a third Completion Notice is still not acceptable, do **not** [continue].
> The 3-attempt limit resets only if you explicitly grant an extension in writing (as an artifact or
> a recorded decision). Silent fourth attempts are a governance violation.

**`governance/templates/milestone-execution-chat-starter.md` — the file a Milestone Chat is actually
instantiated from — contains the word "rework" zero times.**

---

## Measurement, as re-run

Nine starter-shaped surfaces, plus the two normative documents:

| Surface | "rework" | states the 3-attempt rule |
|---|---|---|
| `governance/systems/milestone-execution-chat-starter.md` | 8 | **yes** (L330, L334) |
| `governance/systems/hq-execution-chat-starter.md` | **2** | no |
| `governance/systems/epic-execution-chat-starter.md` | 0 | no |
| `governance/systems/phase-execution-chat-starter.md` | 0 | no |
| `governance/systems/system-hq-seed.md` | 0 | no |
| `governance/templates/milestone-execution-chat-starter.md` | **0** | no |
| `governance/templates/epic-execution-chat-starter.md` | 0 | no |
| `governance/templates/phase-execution-chat-starter.md` | 0 | no |
| `governance/templates/seed.md` | 0 | no |
| `PROJECT-SYSTEM-GUIDELINES.md` | 0 | **no — the rule is not in the normative tier at all** |
| `AI-OPERATING-GUIDELINES.md` | 0 | no |

### Two corrections to SN-32, recorded rather than silently absorbed

1. **"The other six starter surfaces — 0 occurrences" is wrong on one file.**
   `governance/systems/hq-execution-chat-starter.md` contains **two** occurrences of "rework" (L125,
   L364). **Neither states or implies the limit** — one is a Review Decision outcome in an artifact
   table, the other is a list of artifact kinds — so SN-32's *substantive* claim (the rule reaches
   exactly one surface) is unaffected. The literal count is not.
2. **The set is nine surfaces, not eight, under HQ's enumeration.** HQ counts four
   `systems/*-execution-chat-starter.md`, three `templates/*-execution-chat-starter.md`, and the two
   seed files that instantiate chats the same way. SN-32's set of eight is not itemized, so the two
   sets cannot be reconciled from the artifacts. **M43 must state the set it consolidates across,
   itemized**, so the next re-measurement is comparable.

**Neither correction changes what must be done.** They are recorded because *"the count was inherited
and not re-run"* is a named error class here, and a gap record is exactly the artifact a future
reader will re-cite.

---

## The second half, which SN-32 predates

**There are now two statements about what a written extension grants, and they disagree.**

| Source | Semantics |
|---|---|
| `governance/systems/milestone-execution-chat-starter.md:334` | The limit **"resets"** — unbounded, repeatable |
| SN-36/37 amendment (2026-08-19, CFO-decided) | **Exactly one further attempt.** *"Not a reset to three."* |

The CFO's decision is **stricter** than the rule it invokes: the recorded act of resolving a blocker
in the escalation chat *is* the written extension the existing rule requires — a human looked and
acted, which is the opposite of silent — but it buys one attempt, not three.

**Two statements about one mechanism is the drift condition this framework exists to prevent.** M43
reconciles them into one; it does not leave both standing with a citation preferring the newer.

---

## Why this is `P9-GH-1`'s shape, three phases later

`P9-GH-1` was *a rule present in one starter surface and absent from the rest, invisible because no
surface is authoritative.* It was closed on 2026-08-17 by sweeping all eight surfaces (E40.5).

**That sweep fixed one rule. It did not fix the fragmentation that produced it.** `P12-GH-1` is the
same structure applied to a different rule, still open, found by measurement rather than by failure.

**The generalization is the real finding and M43 should scope to it:** as long as a behavioural rule
can live in one starter surface and be authoritative there, every such rule is one omission away from
being unenforceable, and no test detects the omission. The E40.5 sweep is a per-rule remedy for a
per-surface problem.

---

## Severity: Medium

**Not High:** the limit has never been observed to fail in practice, because every Milestone Chat to
date has been manual and a human noticed the loop. **Not Low:** that supervision is precisely what
P12 removes. The rule becomes load-bearing exactly when the mode it protects against arrives — and
SN-31 Decision 5 makes **exhausted rework the trigger for the framework's first fail-closed default**,
so an unenforceable limit disarms the counterweight to the phase's organizing finding.

---

## Placement

**M43 — The Acceptance Chain, Made Structural.** Not M42: this is a governance-surface defect, not an
execution-tier one, and it is coupled to Decision 5's flip rather than to the `bin/` scripts.
