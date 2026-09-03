---
type: template
status: active
last_updated: 2026-09-03
---

# Phase Completion Declaration Template

<!--
  PHASE COMPLETION DECLARATION TEMPLATE

  Purpose: Provide the canonical format for the phase-completion declaration — the
  recorded output of the PSG §5C phase-closure sequence (Step 2).

  Relationship to the Phase-Closure Declaration (PSG §5C Step 9):
  - The Phase Completion Declaration is ADDITIONAL, not a relocation. §5C Step 9 and
    `governance/templates/phase-closure-declaration.md` are unchanged.
  - It is written at Step 2, WHILE the phase is still open — the one artifact guaranteed
    to be written before the phase's parent gate. Step 9's declaration is written after
    consolidation, and records the merge commit, tag and master head — none of which exist
    at Step 2.

  Usage:
  1. Execute PSG §5C Steps 1–2 first (all planned Milestones fully closed; completion
     criteria evaluated).
  2. Replace all <placeholders> with actual content.
  3. Commit as docs/phases/P<id>__<Phase_Name>/P<id>__phase-completion-declaration.md on
     the phase branch (`phase/P<id>`), while the phase is still open.
  4. §5C Step 6 reviews it; Step 9's Phase-Closure Declaration later records the delivered
     state on `master`.
-->

---

## Phase Completion Declaration

Use this format at PSG §5C Step 2, after all planned Milestones are fully closed into the
phase branch:

```markdown
---
type: phase-completion-declaration
phase: P<id>
name: <Phase Name>
status: COMPLETE (awaiting consolidation)
declared_date: YYYY-MM-DD
declared_by: Phase Chat (P<id>)
acceptance_model: <how completion is to be recorded at §5C Step 6 — e.g., SN-13 default-accept (a clean delivery is accepted by an acknowledgment naming the party that reviewed and accepted); silence accepts nothing>
---

# Phase P<id> Completion Declaration

**Phase P<id> — <Phase Name> is COMPLETE (awaiting consolidation).**

All planned Milestones are fully closed into `phase/P<id>`. The phase remains **open**:
this declaration is written at §5C Step 2 and does not close it. Step 9's Phase-Closure
Declaration, on `master`, records the delivered state after consolidation.

---

## Verification Checklist

Each phase completion criterion (from the phase spec) with its verification status:

| # | Completion criterion (phase spec) | Status |
|---|-----------------------------------|--------|
| 1 | <criterion 1> | Satisfied |
| 2 | <criterion 2> | Satisfied |
| 3 | <criterion 3> | Deferred — <where and why; the backstop terminus for deferred phase-spec corrections> |
[One row per criterion; a deferred item must state its owner and trigger]

---

## Milestone Table

| Milestone | Epics | PR | Merge commit (into `phase/P<id>`) |
|-----------|-------|----|------------------------------------|
| M<id> — <Milestone Name> | E<id>.1–E<id>.n | #<pr> | `<sha>` |
[One row per milestone, in consolidation order]

---

## Phase Summary

<2–4 sentence summary of what this phase delivered — the capability and records a
successor at the next level receives.>

---

## Visual Bindings

<Optional. Record links to any generated visuals for this phase, using the binding schema in
governance/guides/visual-artifacts.md §7 (link + What / Level / State / Description). Bind a
hosted LINK, never a committed path. Omit this section if there are no visuals.>

**Visual binding**
- **Link:** <hosted URL of the generated visual>
- **What:** image | infographic | mockup | diagram | clip
- **Level:** Phase
- **State:** proposed | implemented
- **Description:** <short text that survives link rot>
```

---

## Notes

- This declaration is **Step 2 of the PSG §5C phase-closure sequence** — it is written
  **while the phase is still open**, before the README update, version bump and git tag
  (Steps 3, 4, 8), and before Step 9's Phase-Closure Declaration.
- It is **additional, not a relocation**: §5C Step 9 and
  `governance/templates/phase-closure-declaration.md` are **unchanged**. The two
  declarations are distinct artifacts — Step 2's records completion of the planned work
  with its verification checklist and milestone table; Step 9's records the delivered
  state on `master` (merge commit, tag, head).
- It carries the **verification checklist, milestone table and phase summary** that
  previously had no home — in P11 they landed in a PR comment.
- Because it is the one artifact guaranteed to be written while the phase is still open,
  it is the **backstop terminus for any deferred phase-spec correction** (P12's own
  closure is its first customer).
- `acceptance_model` records **how** completion acceptance is recorded; the acceptance
  model's normative text is PROJECT-SYSTEM-GUIDELINES.md §11.6 "Default-Accept (SN-13)",
  not this template.
- Template follows governance style (prescriptive, structured, explicit).