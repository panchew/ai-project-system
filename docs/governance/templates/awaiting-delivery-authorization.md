# Execution Chat — Awaiting Delivery Authorization Templates

Purpose: Provide a canonical, copy-pasteable markdown block that an Execution Chat (Epic or Milestone) can post in its parent chat to signal that execution is complete and it is awaiting Delivery Authorization.

Usage: Replace bracketed placeholders with concrete values. Post the entire code block into the parent chat.

---

## Epic Execution Chat → Milestone Chat

```markdown
Execution Status: COMPLETE ✅ — Awaiting Delivery Authorization

Scope: Epic Execution Chat → Parent Milestone Chat

Epic: <Epic ID and title>
Milestone: <Milestone ID and title>

Branches:
- Source (head): <epic/branch or milestone aggregate if applicable>
- Target (base): milestone/<Milestone ID>

Summary:
- All epic tasks complete and merged into the milestone aggregation branch
- Criteria met: <brief list>

Artifacts:
- Epic Completion Report: <relative path to completion report>
- Test/Validation: <links to plans/reports>

Action Requested from Parent:
1) Issue Delivery Authorization for this epic consolidation into milestone
2) On authorization, proceed with consolidation PR: <head> → milestone/<Milestone ID>

Notes:
- No regressions observed / Known issues documented: <link>
- Completion Date: <YYYY-MM-DD>
```

---

## Milestone Execution Chat → Phase Chat

```markdown
Execution Status: COMPLETE ✅ — Awaiting Delivery Authorization

Scope: Milestone Execution Chat → Parent Phase Chat

Milestone: <Milestone ID and title>
Phase: <Phase ID and title>

Branches:
- Source (head): milestone/<Milestone ID>
- Target (base): phase/<Phase ID>

Summary:
- All epics (list) complete and merged into milestone/<Milestone ID>
- Milestone criteria satisfied: <brief list>

Artifacts:
- Milestone Completion Notice: <relative path>
- Epic Completion Reports: <list of relative paths>
- Validation/Testing: <links to plans/reports>

Action Requested from Parent:
1) Issue Delivery Authorization for milestone consolidation into phase/<Phase ID>
2) On authorization, proceed with consolidation PR: milestone/<Milestone ID> → phase/<Phase ID>

Notes:
- Branch hygiene complete (epic branches cleaned)
- Completion Date: <YYYY-MM-DD>
```

---

## Tips

- Keep "Summary" to 3–5 bullets. Link to the completion notice/report for details.
- Ensure all referenced links are repository-relative paths so they remain stable.
- If a Delivery Authorization doc is already created, include its path under Artifacts.
