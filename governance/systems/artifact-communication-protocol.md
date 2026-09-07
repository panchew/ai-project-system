---
type: system
status: active
effective_date: 2026-09-02
version: 1.5.0
---

# Artifact Communication Protocol (P4.1)

## Purpose

This document defines the canonical artifact formats and communication rules for structured, predictable handoffs between governance chats in the AI Project System.

**Problem Solved:** Manual mode previously required human copy-paste between chats, creating transcription errors and breaking audit trails. Agentic mode had no standard for parent-child artifact exchange. (Transport itself is now solved better still by committed files passed by reference — AI-OPERATING-GUIDELINES.md §3.1.1; see §Integration with Manual Mode.)

**Solution:** Two canonical artifacts for the standard Epic/Milestone/Phase flow — **Delivery Notice** (produced by the child at execution completion) and **Review Decision** (produced by the parent, exception path only) — with standardized frontmatter (YAML) + markdown body. Every chat produces these when appropriate, and parent chats consume them for decisions. The Bugfix Workflow retains its own, separate two-artifact model (see §3) as a deliberate exception.

**Benefit:** 
- Automation-ready: chats can parse YAML frontmatter programmatically
- Human-readable: markdown body explains context
- Audit trail: every handoff is recorded
- No transcription: artifacts flow directly between chats
- CFO-friendly: Layer-8 sees predictable completion/review/delivery artifacts from all projects

---

## Core Principles

1. **Artifact-First Communication** — Every chat-to-chat handoff uses one of the canonical artifacts
2. **Frontmatter + Body** — YAML frontmatter for machine parsing, markdown body for human context
3. **Reference Integrity** — Every artifact includes parent_id, child_id, epic_id, milestone_id, phase_id as appropriate
4. **One Way Per Direction** — Delivery Notice flows up at execution completion; a Review Decision flows down only on the exception path (a clean delivery is accepted by an acknowledgment naming the party that reviewed and accepted — silence accepts nothing — PSG §11.6 / AOG §14)
5. **Immutability** — Once an artifact is created, it is archived; modifications create a new versioned artifact
6. **Terminal States** — A chat declares completion via its Delivery Notice, the parent accepts a clean delivery by an acknowledgment that names the party that reviewed and accepted (merge + in-chat acknowledgment; silence accepts nothing) and rejects or accepts-with-follow-ups via artifact on the exception path (PSG §11.6); no further artifact is produced in the standard flow after merge

---

## Artifact Types

### 1. Delivery Notice (Epic → Milestone, Milestone → Phase, Phase → HQ)

**Trigger:** Epic/Milestone/Phase declares work finished, submits for parent review.

**Direction:** Upward (child → parent)

**Purpose:** Signal readiness for parent acceptance. The parent accepts a clean delivery by an acknowledgment naming the party that reviewed and accepted (silence accepts nothing); it issues a Review Decision (Reject, or Accept with follow-up Epics) only on the exception path (PSG §11.6 / AOG §14).

#### Structure

```markdown
---
artifact_type: delivery_notice
artifact_version: 1.0
timestamp: <ISO-8601 UTC>
issuer_chat: <chat_type> (<full_reference>)
issuer_role: Epic|Milestone|Phase Agent
status: ready_for_review
epic_id: <P#-M#-E#.#>
milestone_id: <P#-M#>
phase_id: <P#>
project_name: <name>
deliverables:
  - name: <artifact_name>
    path: <repo_path>
    type: spec|implementation|report|pr
    status: ready
  - name: ...
    ...
blockers: []  # or list of {description, severity: critical|warning}
qa_status: passed|failed|blocked  # final QA loop result
pr_details:
  number: <PR number or "pending">
  title: <PR title>
  target_branch: <target branch>
  url: <GitHub URL or "not_created_yet">
---

# Delivery Notice: <P#-M#-E#.#> — <Epic Name>

## Summary
<Brief executive summary of what was delivered (2-3 sentences)>

## Deliverables
<List of what was created/modified, with paths and status>

## Quality Assurance
- Tests: <passed/failed/n/a>
- Code Review: <ready/pending/issues>
- Definition of Done: <✓ all items met / ✗ items pending>

## Blockers or Risks
<Any outstanding issues that may affect acceptance>

## Ready for Parent Review
This Epic is complete and submitted for <Milestone|Phase|HQ> Chat review and acceptance.

**Next Action:** Parent Chat reviews this artifact. Then (PSG §11.6):
- **Clean delivery** → accepted by an acknowledgment naming the party that reviewed and accepted (merge + in-chat acknowledgment; no artifact; silence accepts nothing)
- **Not clean** → exception-path **Review Decision** (Reject → rework, or Accept with follow-up Epics)
```

#### Examples

**Epic Delivery Notice:**
```markdown
---
artifact_type: delivery_notice
artifact_version: 1.0
timestamp: 2026-05-29T14:32:00Z
issuer_chat: Epic Agent (P1-M1-E1.1)
issuer_role: Epic Agent
status: ready_for_review
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: my-project
deliverables:
  - name: Epic Spec
    path: docs/phases/P1__Phase_Name/M1__Milestone/E1.1__spec__Feature_Name.md
    type: spec
    status: ready
  - name: Implementation
    path: src/features/feature-name.ts
    type: implementation
    status: ready
  - name: Tests
    path: tests/features/feature-name.test.ts
    type: implementation
    status: ready
  - name: Pull Request
    path: pull/428
    type: pr
    status: ready
blockers: []
qa_status: passed
pr_details:
  number: 428
  title: "feat: Implement Feature Name (E1.1)"
  target_branch: milestone/M1
  url: "https://github.com/user/project/pull/428"
---

# Delivery Notice: P1-M1-E1.1 — Feature Name

## Summary
Implemented feature XYZ with full test coverage and documentation. All Definition of Done items satisfied.

## Deliverables
- ✓ Epic spec created
- ✓ Implementation code committed
- ✓ Tests written and passing (14/14 tests)
- ✓ PR #428 opened against milestone/M1
- ✓ Code review checklist completed

## Quality Assurance
- Tests: passed (14/14)
- Code Review: ready (self-reviewed against checklist)
- Definition of Done: ✓ all items met

## Blockers or Risks
None. Ready for acceptance.

## Ready for Parent Review
This Epic is complete and submitted for Milestone Chat review and acceptance.
```

---

### 2. Review Decision (Milestone → Epic, Phase → Milestone, HQ → Phase) — exception path

**Trigger:** Parent reviews a Delivery Notice and finds the delivery **not clean**. This is the exception path (PSG §11.6 / AOG §14): a clean delivery is accepted by an acknowledgment naming the party that reviewed and accepted — the merge plus the in-chat acknowledgment is the acceptance record, silence accepts nothing — and produces no Review Decision.

**Direction:** Downward (parent → child)

**Purpose:** Require rework (Reject), or grant authority to proceed with merge while binding follow-up Epic(s) (Accept with follow-ups).

#### Structure

```markdown
---
artifact_type: review_decision
artifact_version: 1.0
timestamp: <ISO-8601 UTC>
issuer_chat: <chat_type> (<full_reference>)
issuer_role: Milestone|Phase|HQ Agent
decision: accept|reject
epic_id: <P#-M#-E#.#> (or milestone_id for Milestone reviews, phase_id for Phase reviews)
milestone_id: <P#-M#>
phase_id: <P#>
project_name: <name>
delivery_notice_timestamp: <timestamp of the Delivery Notice being reviewed>
feedback: <feedback or rejection reason>
authorization:
  action: merge|rework
  merge_instruction: <if action=merge: detailed merge instructions>
---

# Review Decision: <P#-M#-E#.#> — <Epic Name>

## Decision: ACCEPT | REJECT

## Reviewer Context
- Reviewed by: <chat_type> Agent
- Review Date: <YYYY-MM-DD HH:MM UTC>
- Delivery Notice Date: <YYYY-MM-DD HH:MM UTC>

## Feedback
<Detailed feedback, notes, or rejection reason>

## Authorization
<If ACCEPT:>
The parent performs the merge of this work (PSG §11.6 — a child never holds merge
authorization). The parent's own steps:
1. <step 1>
2. <step 2>
3. ...

<If REJECT:>
This submission has been rejected. Please address the following before resubmitting:
1. <required change 1>
2. <required change 2>
3. ...
```

#### Examples

Both examples below are **exception-path** artifacts. A clean delivery produces no
Review Decision at all — it is accepted by an acknowledgment naming the party that
reviewed and accepted (silence accepts nothing), with the merge plus the in-chat
acknowledgment as the acceptance record (PSG §11.6).

**Epic Review Decision (Accept with follow-up Epic — exception path):**
```markdown
---
artifact_type: review_decision
artifact_version: 1.0
timestamp: 2026-05-29T15:00:00Z
issuer_chat: Milestone Agent (P1-M1)
issuer_role: Milestone Agent
decision: accept
epic_id: P1-M1-E1.1
milestone_id: P1-M1
phase_id: P1
project_name: my-project
delivery_notice_timestamp: 2026-05-29T14:32:00Z
feedback: "Spec compliance confirmed and tests comprehensive, but the API documentation gap must be closed. Accepted with follow-up Epic E1.3."
authorization:
  action: merge
  merge_instruction: "Merge PR #428 to milestone/M1. After merge, declare Epic complete in Milestone Chat."
---

# Review Decision: P1-M1-E1.1 — Feature Name

## Decision: ACCEPT ✓ (with follow-up Epic)

## Reviewer Context
- Reviewed by: Milestone Agent (P1-M1)
- Review Date: 2026-05-29 15:00 UTC
- Delivery Notice Date: 2026-05-29 14:32 UTC

## Feedback
The implementation is spec-compliant and tests are comprehensive (14/14 passing), but
the API documentation named in the spec was not delivered. The delivery is not clean, so
this exception-path decision records acceptance with follow-up Epic E1.3 (API docs).

## Authorization
The parent (Milestone Agent) performs the merge of this work (PSG §11.6 — a child
never holds merge authorization). The parent's own steps:
1. Ensure PR #428 passes all CI/CD checks
2. Merge PR #428 to milestone/M1 using squash-and-merge strategy
3. Delete the epic/E1.1 branch after merge
4. Declare Epic E1.1 complete in the Milestone Chat
5. Follow-up Epic E1.3 (API documentation) is created for the next planning cycle
```

**Epic Review Decision (Reject — exception path):**
```markdown
---
artifact_type: review_decision
artifact_version: 1.0
timestamp: 2026-05-29T15:30:00Z
issuer_chat: Milestone Agent (P1-M1)
issuer_role: Milestone Agent
decision: reject
epic_id: P1-M1-E1.2
milestone_id: P1-M1
phase_id: P1
project_name: my-project
delivery_notice_timestamp: 2026-05-29T15:15:00Z
feedback: "Test coverage insufficient. Missing tests for error handling. PR CI checks failing."
authorization:
  action: rework
  merge_instruction: null
---

# Review Decision: P1-M1-E1.2 — Another Feature

## Decision: REJECT ✗

## Reviewer Context
- Reviewed by: Milestone Agent (P1-M1)
- Review Date: 2026-05-29 15:30 UTC
- Delivery Notice Date: 2026-05-29 15:15 UTC

## Feedback
This submission is rejected. The following issues must be resolved:

1. **Test Coverage:** Only 60% coverage. Epic spec requires 80% minimum. Add tests for error handling paths.
2. **CI Failures:** 3 linter checks failing. Fix before resubmission.
3. **Documentation:** Missing API documentation in spec. Update before resubmission.

## Authorization
Rework required. Address all items above and resubmit a new Delivery Notice when ready.
```

---

### 3. Post-merge "Delivery Notice" — retired from the standard flow (as of v1.2.0)

**Status:** This document previously described a *second*, post-merge artifact — also named
"Delivery Notice," created by the child chat after the PR is merged to the parent branch, to
record final merge state and close the chat. Direct verification of practice (the canonical
`governance/templates/epic-execution-chat-starter.md` template, and all seven recent P7 Epics
this session — E26.1, E26.2, E26.3, E27.1, E27.2, E27.3, E28.1) shows this second artifact is
**not produced** anywhere in the standard Epic/Milestone/Phase flow: every one of those Epics
produced exactly one notice, at execution completion, pre-review — the artifact renamed
"Delivery Notice" in §1 above (matching PSG §12, AOG §1.1 step 2, AOG §12). Reusing the same
name for two different lifecycle points was itself the terminology collision this version
resolves (see the Epic E28.2 spec's grounding). This section, its schema, and its worked
examples are therefore retired from the standard flow: the chat simply closes on merge, with no
further artifact produced.

**Exception:** the **Bugfix Workflow** (`governance/systems/bugfix-epic-workflow.md`)
intentionally retains a two-artifact model — its own Completion Notice (pre-review) and
Delivery Notice (post-merge) — as part of its deliberately heavier process (4-hour SLA review,
CFO-signed Deployment Authorization, mandatory Post-Mortem). That document remains authoritative
for its own artifacts; it is not restated here.

---

## Communication Flow Diagram

```
Epic Execution Chat
    ↓
    [Complete]
    ↓ ARTIFACT: Delivery Notice
    ↓
Milestone Chat
    ↓
    [Review]  (PSG §11.6)
    ↓ clean     → accepted by acknowledgment naming the party that reviewed
    ↓             (no artifact; in-chat acknowledgment + merge; silence accepts nothing)
    ↓ not clean → ARTIFACT: Review Decision (Reject ← rework required,
    ↓             or Accept with follow-up Epics)
    ↓
Epic Execution Chat (if Reject: rework and resubmit)
    ↓
    [Rework] → Delivery Notice (v1.1) → re-review (clean → accepted by acknowledgment naming the party that reviewed)
    ↓
Epic Execution Chat
    ↓
    [Merge PR] → Epic Chat closed (no further artifact in the standard flow — §3)
    ↓
Milestone Chat
    ↓
    [Acknowledge] → Next Epic or Milestone Complete
    ↓ ARTIFACT: Delivery Notice (Milestone)
    ↓
Phase Chat
    ↓
    [Review] → Repeat flow at Milestone level
```

---

## Rules

### Creation Rules

1. **Delivery Notice** is created by the child chat when work is finished (all Definition of Done items met, PR open/merged).
2. **Review Decision** is created by the parent chat only on the exception path — when its review of the Delivery Notice finds the delivery not clean (PSG §11.6). A clean delivery is accepted by an acknowledgment naming the party that reviewed and accepted (silence accepts nothing); review happens within 24 hours or escalates, but produces no artifact.
3. The post-merge "Delivery Notice" (previously created by the child chat after PR merge) is retired for the standard flow as of v1.2.0 — see §3. The Bugfix Workflow continues to create its own two-artifact pair; not restated here.

### Formatting Rules

1. All artifacts MUST have valid YAML frontmatter (no syntax errors).
2. Frontmatter MUST include: `artifact_type`, `artifact_version`, `timestamp`, `issuer_chat`, `decision/status`.
3. Reference IDs MUST match the naming convention: `P#-M#-E#.#` (for Epics), `P#-M#` (for Milestones), `P#` (for Phases).
4. Timestamps MUST be ISO-8601 UTC format.
5. Markdown body MUST be human-readable; no machine-only formats allowed.

### Workflow Rules

1. A Delivery Notice MUST precede a Review Decision.
2. Parent acceptance MUST precede the merge. On the happy path a clean delivery is accepted by an acknowledgment naming the party that reviewed and accepted — no Review Decision exists (PSG §11.6 / AOG §14; silence accepts nothing); on the exception path the Review Decision (Accept with follow-ups) MUST precede the merge.
3. If a Review Decision rejects, the child chat creates a new Delivery Notice (v1.1) after rework.
4. Artifacts are immutable once created; modifications create new versions (v1.1, v1.2, etc.).

### Storage & Archival Rules

1. **Delivery Notices** (the pre-review, execution-completion artifact — renamed from "Completion Notice," see §1) are stored in `.ai-project/artifacts/completion-notices/` (one file per Epic/Milestone).
2. **Review Decisions** are stored in `.ai-project/artifacts/review-decisions/` (one file per decision).
3. The post-merge "Delivery Notice" storage convention (`.ai-project/artifacts/delivery-notices/`) is retired for the standard flow (see §3) and remains in use only by the Bugfix Workflow's own two-artifact model.
4. File naming: `<timestamp>__<epic_id_or_milestone_id>__<artifact_type>.md`
5. Artifacts are committed to the repository for audit trail.

---

## Integration with Manual Mode

In manual mode (no daemon), chats produce these artifacts as committed, git-tracked
files and hand them to parent chats **by reference** per AI-OPERATING-GUIDELINES.md
§3.1.1 (the canonical artifact-handoff rule): IDE-attach + one line of intent, or
the canonical reference line (artifact type + id — repo-relative path — status).
The parent chat reads the referenced file selectively (frontmatter + Summary +
DoD/QA suffices under PSG §11.6); a clean delivery is accepted by an acknowledgment that
names the party that reviewed and accepted, with an
in-chat acknowledgment (silence accepts nothing), and on the exception path the Review Decision is handed
back the same way — by reference.

*Fallback — no repo access?* For genuinely repo-less setups only, copy-paste
transport remains documented in AI-OPERATING-GUIDELINES.md §3.1.1's fallback
format (SN-23 (2026-07-18) Decision 2 — platform agnosticism preserved).

**CFO Benefit:** Layer-8 can visit any HQ Chat and see the latest Delivery Notices and Review Decisions in a structured format, making progress tracking across multiple projects trivial.

---

## Integration with Agentic Mode

In agentic mode (daemon running), these artifacts flow through the queue system:

1. Epic Chat completes → writes Delivery Notice to `.ai-project/artifacts/completion-notices/`
2. Daemon detects Delivery Notice → routes to parent (Milestone Chat or HQ Chat)
3. Parent Chat reads and reviews → clean: accepts by an acknowledgment naming the party that reviewed and accepted, and acknowledges to the child (no artifact — PSG §11.6; silence accepts nothing); not clean: writes exception-path Review Decision to `.ai-project/artifacts/review-decisions/`
4. Daemon detects an exception-path Review Decision → routes back to child (Epic Chat or Milestone Chat)
5. Child Chat proceeds on acceptance (the attributed acknowledgment, or Accept-with-follow-ups) → merges; no further artifact is produced in the standard flow (§3). On Reject it reworks and resubmits a new Delivery Notice (v1.1).

---

## Reference

- **System HQ (cross-project participant — `system_request`/`system_response` schemas):** `governance/systems/system-hq.md` — the machine-wide System HQ desk and its two artifact types live there, not in this document, because they are the framework's first **cross-project** pair (this document's types are all intra-project). See that document for their schemas, storage/naming conventions, status vocabulary, and System HQ's normative authority boundary.
- **Chat Hierarchy:** `governance/systems/chat-hierarchy.md`
- **Epic Execution Chat Starter:** `governance/EPIC-EXECUTION-CHAT-STARTER.md`
- **Milestone Execution Chat Starter:** `governance/systems/milestone-execution-chat-starter.md`
- **Phase Execution Chat Starter:** `governance/systems/phase-execution-chat-starter.md`
- **Project System Guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md`
- **AI Operating Guidelines:** `governance/AI-OPERATING-GUIDELINES.md`

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.5.0 | 2026-09-02 | **Acceptance distinguishable from absence (E43.2, P12-M43).** Every "accepted by silence" statement reconciled to the amended PSG §11.6: a clean delivery is accepted by an **in-chat acknowledgment that names the party that reviewed and accepted** (role + session identity); **silence accepts nothing**. Amended: Core Principles 4 and 6, the Delivery Notice purpose, the Completion Notice next-action flow, the Review Decision trigger and examples, the communication flow diagram, the Creation/Workflow rules, and the Manual/Agentic Mode integration steps. No artifact type, schema, or storage rule changed — the signal rides the acknowledgment, not a new object. Backed by `tests/test_acceptance_distinguishable_from_absence.py`. |
| 1.4.1 | 2026-08-03 | **SN-23 citations date-qualified (SN-28; HQ Ruling 2026-08-01, Decision 4).** Two Steering Notes hold `id: SN-23` — 2026-07-18 (reference-first handoff / platform agnosticism) and 2026-07-20 (the P10 adoption spine). Both SN-23 citations in this document (§Integration with Manual Mode's repo-less fallback pointer, and the v1.3.0 changelog entry) mean the **2026-07-18** note and now carry the date form `SN-23 (2026-07-18)`. **Citation disambiguation only — no schema, storage rule, flow, or acceptance-model change, and neither note is renumbered.** Allocation and separating rules recorded in `governance/systems/creation-chat-guide.md`, "Steering Note ID Allocation". E36.1 (P11-M36). |
| 1.4.0 | 2026-07-20 | Added a `## Reference` pointer to the new companion document `governance/systems/system-hq.md`, which canonizes the framework's first **cross-project** artifact pair (`system_request`/`system_response`) and the System HQ participant. Design Decision 1B (SN-21): the cross-project pair lives in a companion document rather than this document's intra-project `## Artifact Types` section, whose Core Principles and Communication Flow Diagram assume a single-project chain. No existing schema, example, flow diagram, or storage rule changed. (P9-M32-E32.1) |
| 1.0.0 | 2026-05-29 | Initial release. Defines Completion Notice, Review Decision, Delivery Notice schemas and integration with manual & agentic modes. |
| 1.1.0 | 2026-07-03 | Reconciled to default-accept (SN-13, PSG §11.6 / AOG §14): Review Decision reframed as the exception-path artifact; a clean delivery is accepted by silence. Ordering rule "Review Decision (Accept) MUST precede a Delivery Notice" scoped to the exception path. ACCEPT worked example reframed as accept-with-follow-ups; REJECT example and all schemas unchanged. (P6-M25-E25.4) |
| 1.3.0 | 2026-07-18 | **Reference-first manual-mode handoff (SN-23 (2026-07-18)).** §Integration with Manual Mode rewritten: artifacts are committed, git-tracked files handed to parent chats **by reference** (IDE-attach + one-line intent, or the canonical reference line) per the generalized AI-OPERATING-GUIDELINES.md §3.1.1 — cited, not restated; copy-paste transport retained as the documented **repo-less fallback** (SN-23 (2026-07-18) Decision 2). §Purpose "Problem Solved" annotated: transport is now solved by committed files + reference, not paste. Schemas, storage rules, agentic-mode flow, and the §11.6 acceptance model unchanged. Per SN-23 (2026-07-18), CFO-ratified; E30.4 (P9-M30). |
| 1.2.0 | 2026-07-13 | Delivery-Notice terminology collision reconciled against PSG §12 / AOG §1.1 step 2 / AOG §12 (all three already agreed): the pre-review, execution-completion artifact (formerly "Completion Notice," §1) is renamed **Delivery Notice**. The separate post-merge "Delivery Notice" (formerly §3) is retired from the standard Epic/Milestone/Phase flow — direct verification found it unproduced across all seven recent P7 Epics (E26.1-3, E27.1-3, E28.1) and the canonical `epic-execution-chat-starter.md` template, which has fully converged on the single-artifact model. The Bugfix Workflow's continued, intentional two-artifact model (`bugfix-epic-workflow.md`) is explicitly carved out as an exception, not restated here. No PSG or AOG edit was needed — both already matched this direction. (P7-M28-E28.2; reverses the M28 Milestone spec's stated recommended default, with reasoning grounded in direct evidence — see the Epic spec) |
