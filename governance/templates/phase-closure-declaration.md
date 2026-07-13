---
type: template
status: active
last_updated: 2026-07-02
---

# Phase Closure Declaration Template

<!--
  PHASE CLOSURE DECLARATION TEMPLATE

  Purpose: Provide the canonical format for the phase-closure declaration — the recorded
  output of the PSG §5C phase-closure sequence (Step 9).

  Usage:
  1. Execute PSG §5C Steps 1–8 first (README update, version bump, consolidation merge,
     git tag — the mandatory automatic steps; no Steering Note is required)
  2. Replace all <placeholders> with actual content
  3. Commit as docs/phases/P<id>__<Phase_Name>/P<id>__phase-closure-declaration.md
     to `master` (the record post-dates the closure commit it describes)

  This template formalizes the frontmatter and body shape shared by the hand-made
  P2–P5 declarations. Unlike the milestone closure declaration (issued in chat),
  the phase-closure declaration is a committed repository artifact.
-->

---

## Phase Closure Declaration

Use this format after PSG §5C Steps 1–8 are complete:

```markdown
---
type: phase-closure-declaration
phase: P<id>
name: <Phase Name>
status: closed
merge_commit: <sha>
tag: v<version>
master_head_at_closure: <sha>
closed_date: YYYY-MM-DD
closed_by: <declaring chat — e.g., HQ Chat or Phase Chat (P<id>)>
acceptance_model: <how closure was recorded — e.g., SN-13 default-accept (no Review Decision artifact issued)>
---

# Phase P<id> Closure Declaration

**Phase P<id> — <Phase Name> is closed.**

Merge commit `<sha>` landed on `master`. Tagged `<tag>`.

---

## Delivery Record

| Milestone | Epics | Scope / gaps closed | PR | Merge commit |
|-----------|-------|---------------------|-----|--------------|
| M<id> — <Milestone Name> | E<id>.1–E<id>.n (<count>) | <items> | #<pr> | `<sha>` |
[One row per milestone]

<Total epic count> epics. <Test summary — e.g., "259 passed / 1 skipped by design">.

---

## Process Record

<How closure was recorded under the operating acceptance model, and any notable
process events during the phase — escalations, spec amendments, steering notes —
each with a pointer to its committed artifact.>

---

## What P<id> Delivered to `master`

- <Delivered capability / change 1>
- <Delivered capability / change 2>
[Group by theme; write for a reader discovering the phase from master]

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

---

## Carry-Forward to P<next-id>

| ID | Title | Priority |
|----|-------|----------|
| <id> | <title> | <priority> |
[Omit this section if nothing carries forward]

---

## Sign-Off

Phase P<id> is closed. <One- or two-sentence statement of the system state at <tag>.>
```

---

## Example: Phase P5 Closure Declaration (abridged)

```markdown
---
type: phase-closure-declaration
phase: P5
name: Process Hardening and Visual Artifacts
status: closed
merge_commit: 69c1446
tag: v5.0.0
master_head_at_closure: 69c1446
closed_date: 2026-06-28
closed_by: HQ Chat
acceptance_model: SN-13 default-accept (no Review Decision artifact issued)
---

# Phase P5 Closure Declaration

**Phase P5 — Process Hardening and Visual Artifacts is closed.**

Merge commit `69c1446` landed on master. Tagged `v5.0.0`.

[Delivery Record, Process Record, What P5 Delivered, Carry-Forward, Sign-Off follow —
see docs/phases/P5__Process_Hardening_and_Visual_Artifacts/P5__phase-closure-declaration.md]
```

---

## Notes

- This declaration is **Step 9 of the PSG §5C phase-closure sequence** — producing it
  presumes the README update, version bump, and git tag (Steps 3, 4, 8) are already done
- The declaration is a **committed repository artifact** on `master`, unlike the milestone
  closure declaration, which is issued in HQ chat
- The frontmatter formalizes the shape the hand-made P2–P5 declarations already shared
- `acceptance_model` records **how** closure acceptance was recorded; the acceptance
  model's normative text is PROJECT-SYSTEM-GUIDELINES.md §11.6 "Default-Accept (SN-13)",
  not this template
- Template follows governance style (prescriptive, structured, explicit)
