# Epic Review Seal Template

<!-- 
  EPIC REVIEW SEAL TEMPLATE
  
  Purpose: Capture human review findings after Coding Agent execution completion.
  
  Created in: Epic E2.1 (Human Review, Acceptance & Review Seals)
  Aligned with: AI-OPERATING-GUIDELINES.md v1.2.0, Section 11
  
  This template enables Layer 8 (human) review to be expressed in natural language
  before HQ Chat makes an explicit acceptance decision.
-->

**Purpose:** The Epic Review Seal is a structured, copy-pasteable block used to express human (Layer 8) review findings after a Coding Agent has reported execution completion. Under default-accept (PROJECT-SYSTEM-GUIDELINES.md §11.6 / AI-OPERATING-GUIDELINES.md §12), the Seal is produced on the **exception path** — a clean delivery is accepted by silence and produces no Seal.

**Usage:** This template is optimized for HQ Chat. It captures human judgment without requiring formalized documentation before review is complete. It is NOT an acceptance artifact—it is a decision input.

<!-- 
  KEY CONCEPT: The Epic Review Seal is a decision INPUT, not a decision RECORD.
  
  - The seal captures findings and recommendations
  - HQ Chat makes the final acceptance decision
  - The decision is recorded in the Review Decision
  
  See AI-OPERATING-GUIDELINES.md Section 11 for full context.
-->

**When to use:**
1. A Coding Agent has reported "Execution Complete"
2. Human has tested/reviewed the delivered work
3. Human has findings to communicate before acceptance

**Flow:**
1. Copy the template below
2. Fill in your findings naturally
3. Paste into HQ Chat
4. Request explicit acceptance decision

<!-- 
  This flow separates:
  - Execution (Coding Agent responsibility)
  - Review (Human responsibility)
  - Acceptance (HQ Chat governance decision)
  
  This prevents iteration loops and ensures explicit human judgment.
-->

---

## Epic Review Seal Template

<!-- 
  INSTRUCTIONS:
  1. Copy the markdown block below (between the ``` markers)
  2. Fill in all [bracketed] placeholders with your actual findings
  3. Delete this comment block before pasting
  4. Paste into HQ Chat to request acceptance decision
-->

```markdown
---
## Epic Review Seal — [Epic ID and Title]

<!-- Example: Epic Review Seal — P1-M2-E2.1 Human Review, Acceptance & Review Seals -->

**Reviewer:** [Your Name]  
**Review Date:** [YYYY-MM-DD]  
**Epic:** [Epic ID: Full Epic Title]  

<!-- 
  Example:
  **Reviewer:** Alice Doe
  **Review Date:** 2026-01-23
  **Epic:** P1-M2-E2.1: Human Review, Acceptance & Review Seals
-->

**What I Tested/Reviewed:**
<!-- List the deliverables you tested, scenarios you verified, and edge cases you explored -->
- [Describe what you tested or verified]
- [Any specific scenarios, edge cases, or integration points]

<!-- 
  Example:
  - Verified governance updates in PROJECT-SYSTEM-GUIDELINES.md
  - Verified AI-OPERATING-GUIDELINES.md updates
  - Confirmed Epic Review Seal template was created
  - Reviewed Delivery Notice structure
-->

**Findings:**
<!-- Separate positive findings from issues. Be specific and factual. -->
- [Finding 1: What worked as expected]
- [Finding 2: What worked correctly]
- [Issue 1: What didn't work, unexpected behavior, or design concern (if any)]
- [Issue 2: Additional concerns (if any)]

<!-- 
  Example:
  - Governance documentation correctly separates execution from acceptance
  - Coding Agent stop rules are clear and unambiguous
  - Epic Review Seal template is usable and ergonomic
  - Acceptance flow is explicitly documented
-->

**Overall Assessment:**
<!-- Provide a brief summary: Is it correct? Fit for purpose? Any blockers? -->
[Brief summary in natural language. Is it correct? Is it fit for purpose? Any blockers?]

<!-- 
  Example:
  All deliverables are present and correct. The system now clearly separates execution, 
  review, and acceptance. No issues identified.
-->

**Recommendation:** [Select one]
<!-- Choose ONE of the following options -->
- Accept as-is
- Accept with follow-up Epic(s)
- Reject (requires new Epic(s))

**HQ Decision Requested:**  
Based on the findings above, should this Epic be:
1. **Accepted as-is** — No further work required
2. **Accepted with follow-up Epic(s)** — Accept this Epic, but create new Epic(s) to address findings
3. **Rejected** — Does not meet requirements; create new Epic(s) to address issues

<!-- Mark your decision with a ✓ or check mark next to the chosen option -->

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
- Reviewed Delivery Notice structure

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
- HQ Chat makes the final acceptance decision, which is recorded in the Review Decision.
- If the recommendation is "Accept with follow-ups" or "Reject", new Epic(s) must be created to address findings.

---

## Related Documentation

<- Status: planned, ready for 
  Links to governance documents and related templates that provide context for the Epic Review Seal.
-->

- [AI-OPERATING-GUIDELINES.md Section 11](../AI-OPERATING-GUIDELINES.md) — Human Review and Epic Review Seal process
- [PROJECT-SYSTEM-GUIDELINES.md Section 11.5](../PROJECT-SYSTEM-GUIDELINES.md) — Execution vs Acceptance
- [Review Decision Template](review-decision.md) — Where acceptance decisions are recorded
- [Epic E2.1 Spec](../phases/P1__System_Foundation_and_Adoption/P1-M2-E2.1__spec__human-review-and-acceptance.md) — Original Epic that created this template
