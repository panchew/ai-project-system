---
artifact_type: progress_digest
artifact_version: 1.0
timestamp: <ISO-8601 UTC, e.g. 2026-06-20T09:00:00Z>
issuer_chat: HQ Chat
target: Creation Chat
project_name: <project-slug>
period_covered: <ISO-date range, e.g. 2026-06-14 to 2026-06-20>
---

<!--
  PROGRESS DIGEST TEMPLATE — HQ Chat → Creation Chat.

  Purpose: the primary, self-contained summary of project state the user reads.
  It must be high-signal and low-noise — the user should NOT have to open any
  phase or milestone artifact to understand where the project stands.

  This is the tightest document in the system. If in doubt, CUT a line — never
  add one. Exactly four sections, no more, no fewer. Do not add sections.

  When HQ sends one:
  - At the start of each new phase or milestone.
  - On request from the Creation Chat.

  Naming convention: <ISO-date>__hq__progress-digest.md
    e.g. 2026-06-20__hq__progress-digest.md
  Storage: .ai-project/artifacts/progress-digests/

  Front-matter fields:
  - artifact_type:    always `progress_digest`
  - artifact_version: schema version (currently 1.0)
  - timestamp:        ISO-8601 UTC the digest was issued
  - issuer_chat:      always `HQ Chat`
  - target:           always `Creation Chat`
  - project_name:     project slug (kebab-case)
  - period_covered:   ISO-date range this digest summarizes

  Fill every <placeholder>, delete these comments, then commit.
-->

# Progress Digest — <project-slug> (<period_covered>)

## Phase Status

<!-- One line per milestone. Status icon: ✅ complete / 🔄 in progress / ⏳ planned.
     Add the blocking issue inline only if one exists; otherwise leave it blank. -->

| Milestone | Status | Blocking issue |
|-----------|--------|----------------|
| <M# — name> | 🔄 | <blocking issue, or blank> |
| <M# — name> | ✅ | |
| <M# — name> | ⏳ | |

## Open Decisions

<!-- Decisions the user must make or confirm. Numbered. Each item states the
     question AND the deadline or trigger. Write "None." if there are none. -->

1. <The decision/question the user must resolve.> — <deadline or trigger>
2. <The decision/question the user must resolve.> — <deadline or trigger>

## Next Actions

<!-- 3–5 items maximum. Each: what, who initiates, by when. If you have more than
     five, you are including noise — cut to the five that matter. -->

1. <What> — <who initiates> — <by when>
2. <What> — <who initiates> — <by when>
3. <What> — <who initiates> — <by when>

## Blocking Concerns

<!-- Zero to three items. Write "None." if the project is clean. If more than
     three exist, list the three most severe — the rest belong in a Steering Note. -->

None.
