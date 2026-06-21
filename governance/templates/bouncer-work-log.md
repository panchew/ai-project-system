---
artifact_type: bouncer_work_log
timestamp: <ISO-8601 UTC, e.g. 2026-06-20T14:30:00Z>
project: <project-slug>
severity: <data-fix | user-request | system-op | other>
---

<!--
  BOUNCER WORK LOG TEMPLATE — Layer-8 manual intervention record.

  Purpose: a lightweight record of manual work done to operate a live system —
  data fixes, direct user requests, one-off console operations. The gap between
  what the system does and what reality demands. NOT a bugfix (those produce
  commits); this is the loose record that sits below a Steering Note.

  Design target: fill in UNDER 2 MINUTES. Four fields, one sentence each.
  If you are spending longer, you are over-writing it — keep it terse.

  The pattern-detection loop this feeds:
    real-life operation → bouncer work (manual, no commit)
      → logged here (lightweight) → 3+ of the same type → Steering Note → Epic

  Naming convention: <ISO-datetime>__bouncer-work__<slug>.md
    e.g. 2026-06-20T1430__bouncer-work__reset-stuck-invoice.md
  Storage: .ai-project/artifacts/bouncer-work-logs/

  Front-matter: artifact_type (always bouncer_work_log), timestamp (ISO-8601 UTC),
  project (slug), severity (data-fix | user-request | system-op | other).

  Delete these comments, fill the four fields, commit. Done.
-->

# Bouncer Work Log — <one-line slug>

**What happened:** <One sentence: the situation that required manual intervention.>

**What I did:** <One sentence: the manual action you took.>

**Side effects:** <One sentence: anything needing follow-up. Delete this line if none.>

**Pattern flag:** `[ ] This is the 3rd+ occurrence of this type → write Steering Note`
