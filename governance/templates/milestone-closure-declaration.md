---
type: template
status: active
last_updated: 2026-02-18
---

# Milestone Closure Declaration Template

<!-- 
  MILESTONE CLOSURE DECLARATION TEMPLATE
  
  Purpose: Provide structured format for HQ Chat to declare milestone complete and prompt for consolidation.
  
  Usage:
  1. HQ Chat uses this format when all milestone Epics are complete
  2. Replace all <placeholders> with actual content
  3. Issue declaration in HQ chat (converted to Markdown)
  4. After merge, issue "Fully Closed Declaration" (see below)
  
  Two-stage process:
  - Stage 1: Milestone Complete (awaiting consolidation) — use "Completion Declaration"
  - Stage 2: Milestone Fully Closed (after merge) — use "Fully Closed Declaration"
-->

---

## Stage 1: Milestone Completion Declaration

Use this format when all Epics complete and milestone criteria satisfied:

```markdown
# MILESTONE CLOSURE DECLARATION — M<id>

**Milestone:** M<id> — <Milestone Name>
**Status:** COMPLETE (awaiting consolidation) ✅
**Completion Date:** YYYY-MM-DD
**Declared By:** HQ Chat

## Completion Verification

✅ **All Epics complete:**
- E<id>: <Epic Name> — merged to milestone/<id>
- E<id>: <Epic Name> — merged to milestone/<id>
- E<id>: <Epic Name> — merged to milestone/<id>
[List all Epics]

✅ **All Epics accepted:** Human review approved for all Epics

✅ **Milestone criteria satisfied:**
- [Criterion 1 from milestone spec]: ✅ Satisfied
- [Criterion 2 from milestone spec]: ✅ Satisfied
- [Criterion 3 from milestone spec]: ✅ Satisfied
[List all criteria from milestone spec and verification status]

## Milestone Summary

[2-4 sentence summary of what was delivered in this milestone]

Examples:
- "This milestone delivered 3 Epics focused on system refinement based on M4 real usage."
- "Key deliverables include governance updates, template improvements, and milestone closure process formalization."

## Required Action: Consolidation

**To fully close this milestone, consolidation is required:**

1. **Create Pull Request:**
   - Source: `milestone/<id>`
   - Target: `<parent-branch>` [Identify: phase/<id> OR develop OR main]
   - Title: "Milestone <id>: <Milestone Name>"
   - Description: Include milestone summary and Epic list above

2. **Human reviews consolidation PR:**
   - Verify all milestone work present
   - Confirm no conflicts
   - Check branch hierarchy correct

3. **Merge PR** (becomes milestone closure commit)

4. **Report merge commit SHA back to HQ**

**Next milestone (`milestone/<next-id>`) MUST branch from `<parent-branch>` after merge.**
```

---

## Stage 2: Fully Closed Declaration

Use this format after PR merged and closure confirmed:

```markdown
# MILESTONE FULLY CLOSED — M<id>

**Milestone:** M<id> — <Milestone Name>
**Status:** CLOSED ✅
**Closure Date:** YYYY-MM-DD
**Closed By:** HQ Chat
**Merge Commit:** <sha>

## Closure Confirmation

✅ **PR created:** `milestone/<id>` → `<parent-branch>`
✅ **PR merged:** Consolidation commit `<sha>`
✅ **Branch hierarchy preserved:** Milestone work now in `<parent-branch>`
✅ **Milestone declared fully closed:** All work consolidated

## Next Steps

- Create `milestone/<next-id>` from `<parent-branch>` branch
- Begin planning for Milestone <next-id>
- (Optional) Archive or delete `milestone/<id>` branch per project policy
```

---

## Example: Milestone M4 Closure Declaration

### Stage 1: Completion (2026-02-17)

```markdown
# MILESTONE CLOSURE DECLARATION — M4

**Milestone:** M4 — System Refinement from Real Usage
**Status:** COMPLETE (awaiting consolidation) ✅
**Completion Date:** 2026-02-17
**Declared By:** HQ Chat

## Completion Verification

✅ **All Epics complete:**
- E4.1: Validation and Constraint System — merged to milestone/M4
- E4.2: Unplanned Progress Branch System — merged to milestone/M4
- E4.3: HQ Planning Behavior for Unplanned Branches — merged to milestone/M4
- E4.4: Epic Delivery Notice Template — merged to milestone/M4

✅ **All Epics accepted:** Human review approved for all 4 Epics

✅ **Milestone criteria satisfied:**
- System gaps from M3 identified and addressed: ✅ Satisfied
- Real usage feedback integrated: ✅ Satisfied
- Governance refined based on experience: ✅ Satisfied

## Milestone Summary

Milestone M4 delivered 4 Epics focused on refining the Project System based on real usage feedback from Milestones M1-M3. Key improvements include validation/constraint systems, unplanned progress branch handling, HQ planning behavior formalization, and Epic delivery notice template creation.

## Required Action: Consolidation

**To fully close this milestone, consolidation is required:**

1. **Create Pull Request:**
   - Source: `milestone/M4`
   - Target: `phase/P1` (Phase 1 branch exists)
   - Title: "Milestone M4: System Refinement from Real Usage"
   - Description: Include milestone summary and Epic list above

2. **Human reviews consolidation PR**

3. **Merge PR** (becomes milestone closure commit)

4. **Report merge commit SHA back to HQ**

**Next milestone (`milestone/M5`) MUST branch from `phase/P1` after merge.**
```

### Stage 2: Fully Closed (after merge)

```markdown
# MILESTONE FULLY CLOSED — M4

**Milestone:** M4 — System Refinement from Real Usage
**Status:** CLOSED ✅
**Closure Date:** 2026-02-17
**Closed By:** HQ Chat
**Merge Commit:** 1784fe0

## Closure Confirmation

✅ **PR created:** `milestone/M4` → `phase/P1`
✅ **PR merged:** Consolidation commit `1784fe0`
✅ **Branch hierarchy preserved:** Milestone M4 work now in `phase/P1`
✅ **Milestone declared fully closed:** All work consolidated

## Next Steps

- Create `milestone/M5` from `phase/P1` branch
- Begin planning for Milestone M5: System Refinement Continuation
```

---

## Notes

- This template is used by **HQ Chat only** (not Coding Agents)
- Milestone closure is a two-stage process (complete → fully closed)
- Consolidation PR is created by human (not automatic)
- Next milestone MUST branch from parent branch where previous milestone merged
- Template follows governance style (prescriptive, structured, explicit)
