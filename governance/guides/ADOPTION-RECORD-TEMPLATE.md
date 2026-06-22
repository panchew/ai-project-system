---
project: <PROJECT_NAME>
phase: P2
milestone: M10
epic: E10.2
type: adoption-record
status: draft
last_updated: <YYYY-MM-DD>
---

# Adoption Record — <Project Name>

<!--
  Instructions: Replace ALL placeholders (angle-bracketed) with actual values.
  Delete or keep sections as appropriate. Inline HTML comments like this one
  serve as guidance and should be removed once the field is filled.
-->

## 1. Project Identification

| Field | Value |
|-------|-------|
| **Project name** | <Project Name> |
| **Repository URL** | <https://github.com/owner/repo> |
| **Adoption date** | <YYYY-MM-DD> |
| **Adopter name/role** | <Name> / <Role> |
| **Governance version** | <FILL: e.g., 4.0.0> |

## 2. Prerequisites Status

<!--
  Check each prerequisite before starting. Document any pre-existing
  setup (e.g., already had Node.js, had VS Code extensions, etc.).
-->

| Prerequisite | Status | Notes |
|---|---|---|
| Git (v2.30+) | ✅ / ❌ / ⚠️ | <version or issue> |
| Repository host (GitHub, GitLab, etc.) | ✅ / ❌ / ⚠️ | <account status> |
| AI chat tool with agent support | ✅ / ❌ / ⚠️ | <tool name> |
| Node.js (v18+) | ✅ / ❌ / ⚠️ | <version> |
| `ai-project` CLI installed | ✅ / ❌ / ⚠️ | <version or fallback> |

## 3. Step Completion Log

<!--
  Follow the adoption guide (ADOPTION-GUIDE.md) step by step.
  Record start/end times, outcome, and any deviations.
  Use a new row for each step.
-->

| # | Step | Start Time | End Time | Duration | Outcome | Deviations? |
|---|---|---|---|---|---|---|
| 1 | Prerequisites Verification | --:-- | --:-- | -- min | ✅ / ❌ / ⚠️ | <describe> |
| 2 | Step 1: `ai-project init` | --:-- | --:-- | -- min | ✅ / ❌ / ⚠️ | <describe> |
| 3 | Step 2: Verify Governance Submodule | --:-- | --:-- | -- min | ✅ / ❌ / ⚠️ | <describe> |
| 4 | Step 3: Deploy Governance Agent | --:-- | --:-- | -- min | ✅ / ❌ / ⚠️ | <describe> |
| 5 | Step 4: Send Canonical Startup Prompt | --:-- | --:-- | -- min | ✅ / ❌ / ⚠️ | <describe> |
| 6 | Step 5: Create Phase 0 Spec | --:-- | --:-- | -- min | ✅ / ❌ / ⚠️ | <describe> |
| 7 | Step 6: Plan First Milestone | --:-- | --:-- | -- min | ✅ / ❌ / ⚠️ | <describe> |

**Total time to completion:** -- minutes

## 4. Friction Points

<!--
  List every issue encountered during onboarding.
  One row per friction point. Categories:
  - Documentation: Missing steps, unclear instructions, gaps in guide
  - Tooling: CLI failures, dependency issues, version mismatches
  - Environment: OS-specific issues, editor configuration, network access
  - Governance: Submodule issues, schema confusion, override problems
  - Process: Branching confusion, planning flow issues
-->

| # | Category | Description | Step Occurred | Root Cause | Workaround | Recommended Fix |
|---|---|---|---|---|---|---|
| 1 | <Category> | <What happened> | <Step #> | <Why it happened> | <How it was resolved> | <What to change in guide> |
| 2 | <Category> | <What happened> | <Step #> | <Why it happened> | <How it was resolved> | <What to change in guide> |

## 5. Guide Deviations

<!--
  Document any steps where the actual onboarding differed from the guide.
  Include both intentional deviations (e.g., skipping a step) and
  circumstantial ones (e.g., different OS, missing tool).
-->

| Step | Expected (per guide) | Actual | Reason | Impact |
|---|---|---|---|---|
| <# / Name> | <Guide says...> | <What we did> | <Why> | <Positive/Neutral/Negative> |

## 6. Improvement Suggestions

<!--
  Specific, actionable recommendations for improving ADOPTION-GUIDE.md
  and ADOPTION-FAQ.md based on this adoption experience.
-->

| # | Area | Suggestion | Priority |
|---|---|---|---|
| 1 | <Guide section / FAQ entry> | <What to change> | High / Medium / Low |
| 2 | <Guide section / FAQ entry> | <What to change> | High / Medium / Low |

## 7. Final Status

<!--
  Mark the overall outcome:
  - Success: All steps completed, HQ Chat is live
  - Partial: Some steps incomplete or workaround needed
  - Failed: Could not complete adoption
-->

**Status:** <Success / Partial / Failed>

**Reason:** <Brief explanation of outcome>

**Time to completion:** -- minutes (target: 25–30 minutes)

---

*Adoption record created using [ADOPTION-RECORD-TEMPLATE.md](ADOPTION-RECORD-TEMPLATE.md).*
*Governance version: <FILL: e.g., 4.0.0>*
