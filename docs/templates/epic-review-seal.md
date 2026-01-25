# Epic Review Seal Template

**Purpose:** The Epic Review Seal is a structured, copy-pasteable block used to express human (Layer 8) review findings after a Coding Agent has reported execution completion.

**Usage:** This template is optimized for HQ Chat. It captures human judgment without requiring formalized documentation before review is complete. It is NOT an acceptance artifact—it is a decision input.

**When to use:**
1. A Coding Agent has reported "Execution Complete"
2. Human has tested/reviewed the delivered work
3. Human has findings to communicate before acceptance

**Flow:**
1. Copy the template below
2. Fill in your findings naturally
3. Paste into HQ Chat
4. Request explicit acceptance decision

---

## Epic Review Seal Template

```markdown
---
## Epic Review Seal — [Epic ID and Title]

**Reviewer:** [Your Name]  
**Review Date:** [YYYY-MM-DD]  
**Epic:** [Epic ID: Full Epic Title]  

**What I Tested/Reviewed:**
- [Describe what you tested or verified]
- [Any specific scenarios, edge cases, or integration points]

**Findings:**
- [Finding 1: What worked as expected]
- [Finding 2: What worked correctly]
- [Issue 1: What didn't work, unexpected behavior, or design concern (if any)]
- [Issue 2: Additional concerns (if any)]

**Overall Assessment:**
[Brief summary in natural language. Is it correct? Is it fit for purpose? Any blockers?]

**Recommendation:** [Select one]
- Accept as-is
- Accept with follow-up Epic(s)
- Reject (requires new Epic(s))

**HQ Decision Requested:**  
Based on the findings above, should this Epic be:
1. **Accepted as-is** — No further work required
2. **Accepted with follow-up Epic(s)** — Accept this Epic, but create new Epic(s) to address findings
3. **Rejected** — Does not meet requirements; create new Epic(s) to address issues

---
```

---

## Example Usage

```markdown
---
## Epic Review Seal — P1-M2-E2.1 Human Review, Acceptance & Review Seals

**Reviewer:** Alice Doe  
**Review Date:** 2026-01-23  
**Epic:** P1-M2-E2.1: Human Review, Acceptance & Review Seals  

**What I Tested/Reviewed:**
- Verified governance updates in PROJECT-SYSTEM-GUIDELINES.md
- Verified AI-OPERATING-GUIDELINES.md updates
- Confirmed Epic Review Seal template was created
- Reviewed Completion Report structure

**Findings:**
- Governance documentation correctly separates execution from acceptance
- Coding Agent stop rules are clear and unambiguous
- Epic Review Seal template is usable and ergonomic
- Acceptance flow is explicitly documented

**Overall Assessment:**
All deliverables are present and correct. The system now clearly separates execution, review, and acceptance. No issues identified.

**Recommendation:** Accept as-is

**HQ Decision Requested:**  
Based on the findings above, should this Epic be:
1. **Accepted as-is** — No further work required ✓
2. **Accepted with follow-up Epic(s)** — Accept this Epic, but create new Epic(s) to address findings
3. **Rejected** — Does not meet requirements; create new Epic(s) to address issues

---
```

---

## Notes

- The Epic Review Seal is **human-centric**. It's designed to capture natural language findings without forcing premature structure.
- The seal is **NOT a blocker**. It's a lightweight mechanism for communicating findings to HQ Chat.
- HQ Chat makes the final acceptance decision, which is recorded in the Epic Completion Report.
- If the recommendation is "Accept with follow-ups" or "Reject", new Epic(s) must be created to address findings.
