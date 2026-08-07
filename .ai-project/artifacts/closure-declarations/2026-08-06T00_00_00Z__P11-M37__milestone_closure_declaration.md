---
type: milestone-closure-declaration
milestone: M37
status: complete
completion_date: 2026-08-06
declared_by: Milestone Chat (P11-M37 — Corpus Record Conventions)
issued_to: Phase Chat (P11 — Drivr: Coordination over Rented Execution)
is_final_milestone: false
---

# MILESTONE CLOSURE DECLARATION — M37

Milestone **P11-M37 — Corpus Record Conventions** is hereby declared **COMPLETE (awaiting
consolidation)**. Two epics — **E37.1** and **E37.2** — have been executed, **independently verified
by this Milestone Chat**, and merged to `milestone/M37` with explicit human merge authorization for
each (SN-19 / PSG §11.6).

**M37 is NOT P11's final milestone.** On consolidation the Phase Chat proceeds to **M38 planning** —
Drivr inception — per the binding order M36 → M37 → M38 → M39 → M40. `phase/P11` is not merged to
master until all five milestones close.

Full suite green on `milestone/M37` @ `9c93ba2`: **377 passed, 0 failed, 0 skipped, 0 xfailed.**

**What "independently verified" meant here.** Not Delivery Notices trusted on faith — **G2 in its
general form: the reviewer re-measures, and the delivery's claim is not the evidence.** For E37.1 I
extracted the row literals by `grep` pattern rather than by the Notice's line numbers, so the
comparison did not inherit its method; recomputed the §Steering Note ID Allocation freeze hash from
the merge base; and counted changelog rows per document myself. For E37.2 I re-ran all three sweeps
plus a broader level-keyed sweep, diffed `PROJECT-SYSTEM-GUIDELINES.md` in full to confirm a one-line
change, and verified the rework's containment at 4 insertions / 2 deletions. **Two claims did not
survive contact and are recorded below rather than absorbed.**

---

## Completion Verification

| Epic | Merge | PR | Verified |
|---|---|---|---|
| **E37.1** — System-tier versioning convention (P10-GH-8) | `61fe789` | #186 | ✅ accepted by silence (SN-13) |
| **E37.2** — Artifact-ID citation forms (`GH-`, escalation notices) | `a5ee6f8` | #187 | ✅ accepted after one narrow rework (Review Decision, resolved) |

**Both merges human-authorized in-chat** (SN-19 — no ceremonial artifact; harness-enforced regardless).

**Post-merge state on `milestone/M37`, re-measured after the second merge:**

```
governance/systems/ documents:                  17
  carrying version + ## Changelog:              17
bare GH-<n> under governance/:                   0
milestone-key escalation citations:              0
PROJECT-SYSTEM-GUIDELINES.md:605:                P6-GH-10
creation-chat-guide.md:                          version 1.1.0
chat-hierarchy.md:                               version 1.1.0
## Artifact ID Citation Forms:                   present
suite:                                           377 passed / 0 failed
```

---

## Milestone Definition of Done — verified

| # | Item | Status |
|---|---|---|
| 1 | E37.1 and E37.2 each meet their own DoD | ✅ verified per epic |
| 2 | Both epic branches merged to `milestone/M37` | ✅ `61fe789`, `a5ee6f8` |
| 3 | All 17 `governance/systems/` documents carry `version` + `## Changelog`; ten seeded forward-looking, seven shown untouched, no reconstructed history | ✅ 17/17; exactly one changelog row per seeded document |
| 4 | `chat-hierarchy.md`'s seeding row records M36's amendment to it, sourced from the 2026-08-05 erratum and not Decision 5's count | ✅ byte-identical to the G1 literal |
| 5 | No namespace-stripped `GH-<n>` remains under `governance/`; `PSG:605` reads `P6-GH-10` | ✅ sweep returns 0 |
| 6 | The `GH-` phase-prefix rule, the escalation-notice full-filename rule, and the prefix-means-filing-phase statement recorded normatively **in one place**, exceptions named, nothing renumbered | ✅ one section; `PSG:605` cites rather than restates |
| 7 | The escalation-notice sweep is exhaustive, covering the third occurrence at `ai-project-yml-spec.md:6` the ruling does not name | ✅ and **all three are fixed**, not merely covered |
| 8 | **No test, linter or validator was added** — and any recommendation is recorded and escalated, not built | ✅ `tests/` untouched by both epics; guard recommended and escalated |
| 9 | Both deliveries carry a Structural Mermaid diagram (fenced, in-repo, no ComfyUI) | ✅ both |
| 10 | Both Epic Starters declare `Execution Mode: manual` and route to `models.epic_manual` — unless the CFO overrides E37.1, in which case recorded | ✅ both manual/paid; **the override was taken and then reverted — see Findings 1** |
| 11 | **M37's contents were not widened.** No parked carry-forward absorbed; anything proposed was escalated | ✅ two epics at open and at close |
| 12 | Full suite green on `milestone/M37` (377 / 0 baseline, no regressions, no new skips) | ✅ 377 / 0 |
| 13 | Milestone Closure Declaration produced (`is_final: false` — M38 planning follows) | ✅ this document |

---

## Acceptance Criteria — verified

1. **Every `governance/systems/` document can record its own amendments** — 17 of 17 compliant, ten
   seeded forward-looking, seven untouched, no reconstructed history. ✅
2. **`chat-hierarchy.md`'s changelog tells a reader that M36 amended it** — the fact HQ's own Decision
   5 count would have lost. ✅ **And the document has since used that capability**: E37.2's own
   amendment to it is recorded in a second row, which would have been unrecordable four days ago.
3. **No citation in the normative tier resolves to more than one artifact** — `PSG:605` disambiguated,
   no bare `GH-<n>` remaining, escalation notices cited by full filename. ✅ **3 of 3** after rework.
4. **The `GH-` prefix's meaning is recorded as immutable-by-origin**, forward-allocated ranges ratified
   as exceptions, nothing renumbered. ✅
5. **Both rule sets live in one place and are cited elsewhere, not restated.** ✅
6. **The milestone closed exactly as wide as it opened** — two items, no absorbed carry-forwards, no
   enforcement built. ✅
7. **The full suite is green at milestone delivery** — 377 / 0. ✅

---

## Milestone Summary

M37 was carved out of old-M37 on 2026-08-05 by CFO direction, because *"the milestone with room"* had
become *"the milestone things get put in"* — seven epics, four of them carry-forward hygiene routed
there one ruling at a time. **HQ named that pattern and constrained itself against it; the CFO fixed
it structurally.** The fence was the load-bearing rule of this milestone, and it held: **two epics at
opening, two at closing, nothing absorbed.**

**E37.1** seeded ten `governance/systems/` documents with a `version` field and a `## Changelog`,
forward-looking only. Its difficulty was never the ten near-identical rows — it was the **one row that
had to be different**, sourced from the 2026-08-05 erratum rather than from the ruling that scheduled
the work, because HQ's Decision 5 count omits `chat-hierarchy.md` and a row written from it would have
recorded the directory's most-cited document as unamended by the milestone that amended it. **G1
converted that judgment call into transcription**, and the delivery removed transcription error as a
failure mode entirely by extracting the literals programmatically rather than retyping them.

**E37.2** disambiguated the corpus's sole bare `GH-` identifier — in the framework's highest-authority
document, where the surrounding context actively misleads — and recorded four citation-form rules
**once**, in a new section adjacent to E36.1's. Its difficulty was precision, not volume: two
characters, and four rules whose entire value is that they can be applied by someone who has never
read the ruling.

**Neither epic decided anything.** Every deliverable traces to HQ Ruling 2026-08-04 or 2026-08-05.

---

## Findings

### 1. The posture round-trip — decided, reverted, and better for it

For one day E37.1 ran **agentic / local** by CFO decision. The Milestone Chat, planning its dispatch,
found that **agentic dispatch had not worked since 2026-07-12**: the sandbox cannot reach ollama on
`localhost`, and `local-agent-runner` is absent from the sandbox image. The Phase Chat verified all six
claims; **HQ added the measurement that settled it** — with the endpoint gap fixed the runner is *still*
absent, so the posture depended on **M38/E38.2's adapter surface**, a milestone binding order places
after this one. **HQ Ruling 2026-08-06, Decision 2 reverted to uniform manual/paid.**

**The decision was not wrong; its premise was false.** The gap was three weeks old, recorded in
P7-M26-E26.3 on 2026-07-12 and **worked around per-epic rather than filed.** The controlled local/paid
comparison relocates to **M38/E38.6**, where it is native; the endpoint gap is authorized as Bugfix
**B2.1** (High). **The experiment produced a more valuable finding than the comparison would have, and
produced it without executing anything.**

**G1 and G2 survived the revert, deliberately.** They were written to bound a local model, and both
bound a paid-frontier run unchanged — **because neither risk was ever tier-specific.**

### 2. Count errors: two more, both from paid frontier chats, both caught by re-measurement

**Finding 5 of E37.1's delivery: this Milestone Chat's own spec miscounted.** §The adjacent tidy-ups
stated *"four documents use `last_updated`, nine use `effective_date`"*; measured **3 / 11 / 3**, and
the stated pair summed to 13 — **omitting the three documents with no front matter**, the very three
that spec's own §Verified at planning time had discovered by measuring. **The count was authored in the
same session as the table containing the right data, without recounting from it.** Corrected at spec
v1.2.1 with the original struck, not overwritten.

**The `GH-` live-ID count moved three times in two days** — 38 (ruling), 39 (milestone spec), 40 (E37.2
spec and delivery) — each correct at its date, as `P11-GH-1` and then `P11-GH-2` were filed. **A naive
sweep returns 42** by counting two pre-renumber historical strings.

> **Running tally: seven instances in this phase of a record stating a count that omits its own
> contribution; five of them authored by paid frontier chats, including HQ's own Decision 5.** This is
> the argument *for* G1, not against it. **Every one was caught by re-measurement rather than review.**

### 3. The metavariable trap — a design constraint no guard author could otherwise learn

E37.2's first draft of the citation rules **instantiated the defects they prohibit**: spelling out the
forbidden forms literally put 4 bare identifiers and 1 milestone-key citation into `governance/`. Its
own post-edit sweep caught it, and it rewrote the rules to *describe* the prohibited forms rather than
exhibit them.

**Then it fired a second time, during the rework** — in an **ordinary changelog row**, not a rule
statement. Caught again by the epic's own sweep.

> **This is the finding with the longest reach.** The constraint as first recorded was *"allowlist the
> rule document, or mandate the metavariable form in rule statements."* **The second occurrence proves
> that insufficient.** Generalized: **any document that records having fixed a citation defect is
> liable to restate the defect while doing so.** A guard written without knowing this **fails on its
> first run against a correct corpus.**

### 4. Line numbers as a floor — demonstrated twice, within hours

E37.2's spec told its executor to *locate by heading text, not by line number*. **That spec's own line
numbers went stale within hours of being written**, when E37.1's six-line front-matter block shifted
`creation-chat-guide.md` (§Steering Note ID Allocation 161 → 167, insertion point 235 → 241). Corrected
at spec v1.0.1. **Then the same shift invalidated `chat-hierarchy.md:271` → `:272`** in both the ruling
and the spec — reported by E37.2, correctly not "fixed", since both were right at their dates.

### 5. P10-GH-10 fired during Stage-2 review

`tests/test_artifact_router.py::test_daemon_extensions_error_branches` failed on the reviewer's **first**
full-suite run of E37.2 (1 failed / 376 passed), passed in isolation, and passed in runs 2 and 3.
**Zero files under `tests/`, `src/` or `bin/` in either epic's diff.** Behaving exactly as measured
(~30% in full-suite runs). **Recorded with both outcomes**, per the standing instruction. Untouched:
not fixed, skipped, or marked.

### 6. A contradiction in this chat's own Epic spec, surfaced because the Epic escalated

E37.2's spec authorized fixing *"any escalation-notice-by-milestone-key citation the sweep finds under
`governance/`"* while its do-not-touch list named *"all ten of E37.1's other seeded documents"* — and
`chat-hierarchy.md` is both. **The Epic applied *specific prohibition beats general authorization*,
left the citation, and escalated rather than choosing.** That was correct on the text as written, and
it is precisely the outcome a self-contradicting spec should produce.

Resolved at spec v1.1.0 in favour of the fix: the clause protects **E37.1's work product**, not the
documents wholesale. **Recorded as a Review Decision** (exception path, PSG §11.6) rather than settled
in chat — the rework was narrow, specified, and verified. **A contradiction was removed; no subject was
added.**

### 7. The wrong-branch hazard, three times in one milestone

The shared worktree was found on the wrong branch **three times** during M37 — twice for this Milestone
Chat (once on `phase/P11`, once on `master`) and once for the Phase Chat, which committed a spec
amendment to the child branch as a result and had to correct the record (spec v1.1.1). **Every Epic
Starter in this milestone carried a branch check as its first prerequisite, and no epic tripped on it.**
**Writing a precaution into a document does not execute it** — the chats that skipped the check were the
ones that wrote it.

---

## Carry-forwards

**Recorded, unowned, and NOT absorbed by this milestone.**

| # | Item | Disposition |
|---|---|---|
| 1 | **Enforcement guard for the versioning + citation conventions** — recommended by both epics, judged valuable, **not built** | **Escalated.** Needs its own scoped item in a milestone whose scope permits enforcement. **Must carry Finding 3's design constraint** or it fails on first run |
| 2 | **Front-matter date-key drift** — 3 `last_updated` / 11 `effective_date` / 3 no date key | Reported and left. Not M37's subject |
| 3 | **`epic-execution-chat-starter.md` declares `type: template`** while sitting in `governance/systems/` — sole `type` outlier of 17 | Reported and left. **Blocks any guard that asserts on `type`** until decided |
| 4 | **Bare identifiers outside `governance/`** — 156 occurrences under `.ai-project/`, 489 under `docs/`, across 184 files | **Out of scope by rule.** The rule as ruled binds the normative tier. Recorded so the number is not mistaken for a defect |
| 5 | **`rulings/` date-only ambiguity** | **Report-and-leave, affirmed** (Decision 6). Not actioned, not escalated |

**Not absorbed, as required:** `P10-GH-4`, `P10-GH-6`, `P10-GH-10`, `P10-GH-5`, `P10-GH-1`, `P9-GH-1`,
`P9-GH-3`, `P10-GH-3`, `P10-GH-7`, `P10-GH-9`, `P8-GH-2`, ComfyUI precision, the sidekick identity
question. **None was proposed for folding in; none was folded in.**

---

## Required Action: Consolidation

The Phase Chat consolidates `milestone/M37` → `phase/P11` and proceeds to **M38 planning** — Drivr
inception, fleet registry, execution adapter surface.

**Three things M38 inherits directly from this milestone:**

1. **The local/paid controlled comparison at `E38.6`**, relocated by HQ Ruling 2026-08-06 rather than
   dropped. **This declaration is the record that the CFO's decision was rescheduled, not abandoned.**
2. **Bugfix `B2.1`** — the sandbox endpoint gap, authorized and delegated, with a post-mortem scoped to
   the real finding: *a gap documented in E26.3 was worked around per-epic for three weeks rather than
   filed.*
3. **The standing split permission**, which the restructure transferred from old-M37 to M38, where it
   inherited five Drivr epics.

---

## Notes

- **M37 executed two rulings and made none.** Every deliverable traces to HQ Ruling 2026-08-04 or
  2026-08-05. The only genuine design choices — E37.1's starting-version scheme and D2–D4, E37.2's
  placement and ordering of the four rules, and the landing order — were made at this level, recorded
  in the specs, and applied without re-litigation.
- **Both epics are judged partly on what they declined**, and both declined the same thing: a guard
  their own measurement loop already was, minus being committed. **E37.2 also declined the adjacent
  two-character fixes it noticed while editing the highest-authority document in the framework** — the
  discipline E36.5 established when it refused the `PSG:605` fix and HQ explicitly declined to undercut.
- **The milestone's subject applied to itself, repeatedly.** A milestone about making the record able to
  state what changed produced: a spec that miscounted its own inventory, a count that moved three times
  in two days, line numbers that went stale within hours of being written, and rule text that twice
  instantiated the defect it prohibits. **Every one was caught by measurement rather than by reading**,
  which is the practice both guardrails encode.
- **PSG §11.6.1 remains in force.** Silence accepts *children's* clean deliveries, never HQ's own
  output. The Structural diagram obligation fired for both epics and is what keeps the CFO's mandatory
  diff review affordable across E37.1's ten-document diff.
- **Default-accept governed E37.1; the exception path governed E37.2.** One Review Decision was issued
  in this milestone, for a defect this Milestone Chat had authored, and it is resolved.
