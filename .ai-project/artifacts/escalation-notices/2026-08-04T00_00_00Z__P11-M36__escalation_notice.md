---
type: escalation-notice
milestone: M36
epic: E36.5
issued_by: Epic Chat (P11-M36-E36.5)
issued_to: Milestone Chat (P11-M36) — one level up per SN-25; for routing to HQ, which owns the remediation decision
date: 2026-08-04
status: open
---

# Escalation Notice: two artifact families carry citation ambiguity that reaches the normative tier

**Source:** the bounded artifact-ID audit required by SN-28 Carry-Over 3 and HQ Ruling 2026-08-01,
**Decision 12**. Full evidence and reproducible method:
[`docs/phases/P11__Drivr_Coordination_Over_Rented_Execution/P11-M36-E36.5__artifact-id-audit.md`](../../../docs/phases/P11__Drivr_Coordination_Over_Rented_Execution/P11-M36-E36.5__artifact-id-audit.md).

> **This notice reports. E36.5 fixed nothing and renumbered nothing.** It is issued because the
> Epic's disposition table makes a normative-tier finding an escalation, not a judgment call — and
> because in both cases below **the fix was cheaper than this notice.** That asymmetry is the exact
> pressure the Hard Boundary exists to resist.

---

## Read this first — the finding is NOT an ID collision

**Stated plainly so severity is not overread.** The audit found **no ID collision in any of the
three families**:

- `rulings/` and `escalation-notices/` **allocate no self-allocated ID at all**, so SN-28's defect
  *as such* cannot exist in them.
- The **`GH-` series is collision-free** — 38 live IDs across six phases, each bound to exactly one
  subject. **Its namespace held.**

What did fire is a **different failure with the same reader-level consequence**: a **shorthand used
to cite an artifact resolves to more than one artifact**, and the ambiguous shorthand appears in
`governance/`. A reader resolving the citation *by its identifier* reaches two candidates.

**This is the SN-23 shape** — which HQ rated High and E36.1 was run to fix — arriving through
citation practice rather than through allocation.

---

## Finding 1 — bare `GH-10` in PROJECT-SYSTEM-GUIDELINES.md

**Location:** `governance/PROJECT-SYSTEM-GUIDELINES.md:605`

> *"Codified by E25.2 (P6-M25); **closes GH-10**."*

`GH-10` is **namespace-stripped**, and it is ambiguous between two live, unrelated items:

| ID | Subject |
|---|---|
| `P5-GH-10` | Delivery Notice receipt protocol |
| `P6-GH-10` | Formally codify the SN-13 default-accept model |

Context resolves it to `P6-GH-10`. **The identifier does not.**

**Why this one matters most:**

- It is in **PSG — the framework's highest-authority document**, higher than any document an SN-23
  citation was found in.
- It is the **only** truly namespace-stripped `GH-<n>` anywhere under `governance/`. All nine other
  normative `GH-` citations carry their phase prefix. It is an outlier, not a convention.
- The `GH-` series is **cited far more widely than `SN-` ever was** — which is precisely what made
  SN-23 a High-severity trap rather than untidiness.

**Root cause — the phase prefix changed meaning mid-corpus.** P5's closure declaration
**forward-allocates P6-prefixed IDs** (`P6-GH-10`, `P6-GH-11` are filed *in P5's record*), so the
prefix there means *"the phase that will address it."* P10's closure declaration carries
`P10-`-prefixed IDs into P11 unchanged, so the prefix there means *"the phase that filed it."* That
inversion is why `P5-GH-10` and `P6-GH-10` are different subjects sharing an ordinal.

Allocation is also non-uniform: P5/P8/P9/P10 restart at 1 per phase; `P6-GH-10…15` and
`P7-GH-16…21` continue a **global** counter.

---

## Finding 2 — "P10-M34 Escalation Notice" resolves to two notices

**Two escalation notices share the milestone key `P10-M34`**, with unrelated subjects:

| File | Subject |
|---|---|
| `2026-07-28T20_00_00Z__P10-M34__escalation_notice.md` | `claude-opus-4-8` unavailable in a manual-chat harness surface |
| `2026-07-29T00_00_00Z__P10-M34__escalation_notice.md` | the M34 fleet set changed — `fieldledger-assesment` out |

The milestone-key shorthand **"P10-M34 Escalation Notice"** appears in **two normative documents**:

- `governance/systems/chat-hierarchy.md:271`
- `governance/ai-project-yml-spec.md:660` (v2.6.0 changelog)

Both mean the **2026-07-28** notice, and both are resolvable **by subject matter only**. The
shorthand also appears in `model-routing-policy.md:92` and `2026-07-28__hq-chat-opener.md:16`.

**This family has no ID and no date in its citation form** — the milestone key is doing identifier
work it cannot do, because a milestone can raise more than one escalation.

> **This notice is itself the second `P11-M36` escalation notice** (after
> `2026-08-03T00_00_00Z__P11-M36__escalation_notice.md`, P10-GH-8's). **It instantiates the very
> ambiguity it reports**, and it is counted in the finding rather than exempted from it. Cite these
> two by **full filename**, never as *"the P11-M36 escalation notice."*

---

## Not escalated — recorded here so the boundary is legible

**`rulings/` carries the same ambiguity but does NOT reach the normative tier.** Two dates hold two
rulings each (2026-07-28, 2026-07-31), and the date-only shorthand is in live use ~14 times across
`docs/` and `.ai-project/artifacts/` — including inside another ruling. **Every one of the 20+
`governance/` citations resolves**, by subject or by an accompanying full path. Per the disposition
table: **project-internal → report and leave.** Not escalated, not renumbered.

---

## What E36.5 deliberately did not do

- **Did not edit PSG:605.** The remediation is two characters (`GH-10` → `P6-GH-10`) and is almost
  certainly correct. It amends a **normative** document — which this Epic is constrained not to
  touch — and the decision is HQ's. **Named explicitly because the cheapness of the fix is the
  hazard, not an argument for making it.**
- **Renumbered nothing**, in any family.
- **Built no mechanism** — no test, validator, linter, or registry. M36 builds none; B3.1's
  steering-note guard was E36.2's bounded exception and is complete.
- **Did not widen M36.** HQ Ruling 2026-08-01, Decision 12: *"it may not widen it. It may only
  report."*

## What is being asked

**A remediation decision, not action inside M36.** For HQ, via the Phase Chat:

1. Whether bare `GH-10` in PSG:605 is disambiguated to `P6-GH-10` — and if so, in which phase.
2. Whether a citation-form rule for `GH-` IDs (always phase-prefixed in normative documents) is
   worth recording, as the SN-23 date-qualification rule was for `SN-`.
3. Whether escalation notices should be cited by **full filename** rather than milestone key.
4. Whether the `GH-` prefix's meaning — *"phase that filed it"* vs *"phase that will address it"* —
   should be stated once, given it silently inverted between P5 and P10.

**Nothing here blocks M36's closure.** E36.5's deliverables are complete; this is a finding handed
upward, which is the outcome the Epic was scoped to produce.

## Precedent

**A `GH-` ID has been renumbered before.** SN-15 (2026-06-28) reconciled `P6-GH-1` → `P6-GH-12` and
`P6-GH-2` → `P6-GH-13`, and recorded the mapping. Those two IDs survive **only** as records of their
own renumber, which is why the live `GH-` count is **38**, not the 40 the corpus records.
