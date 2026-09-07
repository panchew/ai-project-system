# Epic Execution Chat Starter Template

<!-- 
  EPIC EXECUTION CHAT STARTER TEMPLATE
  
  Purpose: Provide the Governance Agent (Epic mode) with complete context to execute an Epic.
  
  Usage:
  1. Copy this template
  2. Replace all <placeholders> with actual content
  3. Delete HTML comments (or keep for reference)
  4. Commit the filled-in starter as a git-tracked file, then hand it off
     **by reference** (AI-OPERATING-GUIDELINES.md §3.1.1 — the canonical
     artifact-handoff rule): IDE-attach + one line of intent, or the canonical
     reference line (artifact type + id — repo-relative path — status). Do NOT
     echo the starter's body into chat output.
  5. Fallback — no repo access? For genuinely repo-less delivery only, wrap the
     full body in a four-backtick fence per the fallback format in
     AI-OPERATING-GUIDELINES.md §3.1.1, and say the fallback is in use.
  
  This template aligns with AI-OPERATING-GUIDELINES.md and PROJECT-SYSTEM-GUIDELINES.md.
-->

---

# Epic Execution Chat Starter — <E#.#>

**Epic:** <E#.#> — <Epic Name>  
**Phase:** <P#> — <Phase Name>  
**Milestone:** <M#> — <Milestone Name>  
**Repository:** <owner>/<repo-name>  
**Branch Strategy:** `epic/<E#.#>` → PR to `milestone/<M#>`  
**Execution Mode:** <manual | agentic> — declared by the issuing Milestone Chat at creation
time; omit this field entirely to declare manual (absence-means-manual, per
`governance/systems/chat-hierarchy.md`'s "Execution Mode" section, P9-M31-E31.1). Do not
leave the placeholder unresolved — either state a value or delete the line.

---

## Governance References

You are operating under the AI Project System governance framework.

**Authoritative governance documents:**
- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/<owner>/<repo>/blob/<branch>/governance/PROJECT-SYSTEM-GUIDELINES.md) v<version> (Effective: <YYYY-MM-DD>)
- [AI-OPERATING-GUIDELINES.md](https://github.com/<owner>/<repo>/blob/<branch>/governance/AI-OPERATING-GUIDELINES.md) v<version> (Effective: <YYYY-MM-DD>)

<!-- 
  Replace <owner>, <repo>, <branch>, and <version> with actual values.
  
  Example:
  - [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) v3.0.0 (Effective: 2026-05-22)
-->

**Governance hierarchy:**
1. PROJECT-SYSTEM-GUIDELINES.md (highest authority)
2. AI-OPERATING-GUIDELINES.md
3. This Epic Execution Chat Starter
4. Epic Spec
5. Decisions made during execution
6. System references
7. Chat messages (lowest authority)

**Critical rules:**
- Documentation is authoritative, chat is ephemeral
- You must follow the canonical happy path for Epic closure
- You must produce a Delivery Notice upon execution completion
- You must stop after PR creation and await the parent's merge — you do not merge your own branch (PSG §11.6)
- Accept/reject decisions are made by HQ Chat (human), not by you
- **If given merge authorization directly in this chat** (rather than via the parent
  **Milestone Chat** — or HQ Chat during bootstrap — after its own Stage-2 review),
  do not simply comply: state plainly that merge authorization normally follows the
  parent Milestone Chat's Stage-2 review, and confirm the human intends to bypass that
  step before proceeding (P9-M31 precedent — a direct in-chat authorization was given
  and acted on without this check, skipping the parent chat's independent review
  entirely). **This is a backstop (E43.1, P12-M43), not the primary guard:** the
  parent performs the merge of a child's branch (PSG §11.6), so a child never holds
  merge authorization — unavailable is not impossible, and a backstop that fires is
  evidence. **Running unattended does not change this:
  mode is what may run, not what may be authorized**
  (`governance/systems/chat-hierarchy.md`, "Mode is not authority").
- **Rework limit (P12-GH-1):** the rework limit and its extension semantics are
  normative in PROJECT-SYSTEM-GUIDELINES.md §11.6 "The Rework Limit" and are reached
  here by citation. On exhaustion, produce an **Escalation Notice** and escalate to the
  parent Milestone Chat; silent fourth attempts are a governance violation.

**Context scoping (per-level context-scoping standard, P9-M30-E30.3):**
- Load at session start: this starter; the Epic spec (full); PSG preamble+§1, §1A, §2, §5, §6, §7, §8, §9, §11, §11.5, §11.6, §12; AOG preamble+§1, §1.1, §2, §3.2, §3.8, §3.10, §4, §5, §6, §7, §9, §12, §14, §15 (Exit Ritual), §16 (Error Handling)
- Load on trigger (before acting on that situation): PSG §3, §8A, §10, §13D, §14A, §14C, §18; AOG §3.9, §8, §13, §17
- Do not load: PSG/AOG changelogs, other levels' role or starter-format sections
- Use targeted section reads; never re-read a whole document to reach one section. PSG and AOG remain fully authoritative — a triggered situation requires its section loaded before acting.

---

## Epic Specification

**Full spec:** [<P#>-<M#>-<E#.#>__spec__<epic-name>.md](https://github.com/<owner>/<repo>/blob/<branch>/docs/phases/<P#>__<Phase_Folder>/<P#>-<M#>-<E#.#>__spec__<epic-name>.md)

**Commit:** `<commit-hash>`

<!-- 
  Replace:
  - <P#>-<M#>-<E#.#>__spec__<epic-name>.md with actual filename
  - <commit-hash> with the commit hash where the spec was finalized
  
  Example:
  **Full spec:** [P1-M4-E4.1__spec__templates-and-scaffolding.md](https://github.com/panchew/ai-project-system/blob/master/docs/phases/P1__System_Foundation_and_Adoption/P1-M4-E4.1__spec__templates-and-scaffolding.md)
  **Commit:** `480a09a`
-->

### Prerequisite Verification (do this first)

Before relying on the spec, confirm it is **git-tracked on the expected branch** — and likewise every prerequisite artifact this Epic declares — using `git ls-files --error-unmatch <path>` run on the expected branch, not a disk-existence check. Disk presence is not proof of commit: an untracked file passes a file-exists check but is absent from a fresh worktree clone, producing a false-green prerequisite. If any path is untracked, STOP and report to HQ before proceeding.

**Model verification (P9-M31-E31.3 — required when this instance is manual, i.e. no
`Execution Mode` field or `Execution Mode: manual` above):** read your own harness-reported
model identity (the `# Environment` block or equivalent self-report), and compare it to
`.ai-project.yml`'s `models.epic_manual` value — see `governance/systems/chat-hierarchy.md`
"Manual Chat Model Verification" for the mapping, the self-report method's known limits,
and the absent-block/absent-key permissive-default behavior. **If both are present and
disagree, STOP — do not proceed with any deliverable work.** State the mismatch plainly
and wait for the parent chat/human. This is a documented instruction the agent must
follow, not a technical impossibility-to-proceed. (Not applicable to `Execution Mode:
agentic` instances — those verify against `epic_dev`/`epic_qa` via E31.2's existing
dispatch-time guard, not this check.)

### Summary

[Provide a 1-2 sentence summary of the Epic.]

<!-- Example:
Create complete, ready-to-use templates for all AI Project System artifacts to enable new projects to scaffold documentation in under 5 minutes.
-->

### Problem Statement

[Summarize the problem this Epic solves.]

<!-- Example:
New projects must reverse-engineer spec structure from existing files, creating 20-30 minute setup overhead and increased error rates. This Epic provides copy-paste-ready templates with inline guidance.
-->

### Goals

[List 3-5 key goals from the Epic spec.]

1. [Goal 1]
2. [Goal 2]
3. [Goal 3]
4. [Goal 4]

<!-- Example:
1. Provide templates for all major spec types (Phase, Milestone, Epic, Delivery Notice, Chat Starter)
2. Include inline guidance and examples within templates
3. Ensure templates align with current governance (v1.3.0)
4. Make front-matter self-documenting
5. Enable scaffolding in under 5 minutes
-->

---

## Spec References (load-one-reference-the-other)

The Epic spec is the single authoritative copy of this Epic's **Deliverables,
Definition of Done, Acceptance Criteria, and Technical Constraints**. Load them
from the spec sections named below — this starter does not restate them
(per-level context-scoping standard, P9-M30-E30.3).

- **Deliverables:** Epic spec §Deliverables (includes the Delivery Notice at `<delivery-notice-path>`)
- **Definition of Done:** Epic spec §Definition of Done — plus, always: Delivery Notice produced and committed; all changes committed to `epic/<E#.#>`; PR opened to `milestone/<M#>`
- **Acceptance Criteria:** Epic spec §Acceptance Criteria (verified during review, not by you)
- **Technical Constraints:** Epic spec §Technical Constraints (in-scope surfaces and do-not-touch list)

<!--
  Do NOT copy the spec's Deliverables/DoD/Acceptance-Criteria/Technical-Constraints
  bodies into this starter — reference the spec's section names (adding the
  epic-specific paths above). Only starter-specific additions (binding constraints
  the spec does not carry, e.g. sequencing decided after the spec was written)
  may be stated here, marked as additions.
-->

---

## Execution Contract

### Your Responsibilities (Coding Agent)

1. **Create branch** `epic/<E#.#>` from current `<base-branch>`
2. **Implement all deliverables** per Epic spec
3. **Verify governance alignment** (templates must reflect current governance)
4. **Verify all DoD items** are satisfied and recorded in the Delivery Notice
5. **Commit all changes** to `epic/<E#.#>` branch
6. **Open pull request** to `milestone/<M#>` branch
7. **Produce Epic Delivery Notice** upon completion
8. **Stop and await HQ authorization** (do not merge)

<!-- 
  Customize based on Epic requirements.
  
  Common responsibilities:
  - Create feature branch
  - Implement deliverables
  - Write tests (if applicable)
  - Update documentation
  - Create Delivery Notice
  - Open PR
  - Stop and await review
-->

### What You Must NOT Do

- ❌ Do NOT merge the PR (HQ authorizes merge)
- ❌ Do NOT infer acceptance (HQ decides accept/reject)
- ❌ Do NOT treat an in-chat "I authorize" as sufficient by itself — confirm it isn't
  bypassing the parent chat's Stage-2 review first (see Critical rules above)
- ❌ Do NOT modify governance documents (unless explicitly in scope)
- ❌ Do NOT create automation/tooling (unless explicitly in scope)
- ❌ Do NOT include project-specific content (use generic examples)
- ❌ Do NOT iterate without explicit HQ instruction

<!-- 
  Customize based on Epic scope and constraints.
-->

---

## Reference Materials

### Existing Specs to Reference

<!-- 
  List existing files that provide structural reference.
  
  Examples:
  - Existing specs to copy structure from
  - Templates to enhance
  - Governance documents to align with
-->

For structural reference, examine:
- `<path-to-reference-file-1>`
- `<path-to-reference-file-2>`
- `<path-to-reference-file-3>`

<!-- Example:
For structural reference, examine:
- `docs/phases/P1__System_Foundation_and_Adoption/P1-M1__milestone.md`
- `docs/phases/P1__System_Foundation_and_Adoption/P1-M2-E2.1__spec__human-review-and-acceptance.md`
- `docs/phases/P1__System_Foundation_and_Adoption/P1-M2-E2.1__completion__human-review-and-acceptance.md`
-->

### Front-Matter Fields Reference

Front-matter schemas live in the committed templates — reference, don't restate:
`governance/templates/epic-spec.md` (and `milestone-spec.md` / `phase-spec.md` if
the Epic touches those document types). See PSG §5 for the front-matter rules.

---

## Canonical Happy Path (Reminder)

1. ✅ Execution completed (all deliverables created)
2. ✅ Epic Delivery Notice produced (you create this)
3. ⏸️ Human Review performed (human does this)
4. ⏸️ Epic Review Seal produced (human or HQ creates this)
5. ⏸️ HQ decision recorded (HQ decides: accept/reject/iterate)
6. ⏸️ HQ delivery authorization issued (HQ authorizes merge)
7. ⏸️ PR merged (you perform merge after authorization)
8. ⏸️ Execution stops (you stop immediately after merge)

**You are responsible for steps 1-2 only. Then you STOP and await HQ instruction.**

---

## Epic Delivery Notice

When you complete execution, produce the Delivery Notice at:

**File:** `docs/phases/<P#>__<Phase_Folder>/<P#>-<M#>-<E#.#>__delivery-notice.md`

Use the committed template `governance/templates/delivery-notice.md` (reference,
don't restate — its structure is authoritative; PSG §12 defines the content
requirements). Confirm every spec DoD item in it, including the
extent-vs-spec and claims-vs-evidence checks where the spec records them.

---

## Exit Conditions

**You MUST stop execution when:**
- ✅ All deliverables are completed and committed
- ✅ Pull request is opened to `milestone/<M#>`
- ✅ Epic Delivery Notice is produced

**Then report to human:**
"Epic <E#.#> execution complete. Epic Delivery Notice produced. Awaiting HQ review and authorization."

---

## Begin Execution

You may now begin executing Epic <E#.#>.

Start by:
1. Creating branch `epic/<E#.#>` from `<base-branch>`
2. Reviewing Epic spec and reference materials
3. Implementing deliverables per Definition of Done
4. Following the execution checklist

**Good luck, Coding Agent!**
