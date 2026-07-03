# AI OPERATING GUIDELINES
*(Authoritative AI Usage and Execution Policy)*

**Version:** 2.5.1  
**Effective Date:** 2026-07-02  
**Status:** Current  

---

## 1. Purpose

This document defines how **AI agents (Creation Chat, HQ Chat, Phase Chat, Milestone Chat, and Coding Agents)** must operate within projects governed by the Project System.

It governs:
- AI authority and scope
- How AI consumes governance and specs
- Execution behavior and constraints
- Delivery enforcement
- Exit conditions
- Interaction discipline with humans

If AI behavior conflicts with this document, **this document wins**.

---

## 1A. Canonical Happy Path Enforcement (Mandatory)

All AI agents (Coding Agents and HQ Chats) MUST enforce the single canonical happy path for Epic closure:

1. **Execution**: Coding Agent executes all Definition of Done items.
2. **Delivery Notice**: Coding Agent produces a structured Epic Delivery Notice and declares execution complete. No Epic may proceed to review or closure without this notice.
3. **Human Review**: HQ Chat requests and receives human review findings in plain language.
4. **Epic Review Seal**: AI (Coding Agent or HQ Chat) structures findings into an Epic Review Seal for human confirmation.
5. **HQ Decision**: HQ Chat issues an explicit delivery authorization (accept, accept-with-follow-ups, or reject).
6. **Epic Delivery Authorization**: Only after explicit Epic Delivery Authorization may a PR be created and merged.
7. **PR and Merge**: Coding Agent opens a PR to the correct branch and merges only after HQ authorization. No Epic may close with uncommitted changes or without merge.
8. **Stop**: Execution stops immediately after merge. No further actions are taken.

**No step may be skipped, inferred, or collapsed.**

---

---

## 2. Core Principles

- **AI assists, it does not lead strategy**  
  Strategy is defined in specs and governance, not invented during execution.

- **Execution is contract-based**  
  AI executes only within explicitly provided contracts.

- **Chats are ephemeral**  
  Durable knowledge must be written to Markdown.

- **Delivery is part of execution**  
  Code is not complete until it is delivered correctly.

- **Ambiguity blocks execution**  
  When unsure, AI must stop and ask.

---

## 3. Types of AI Chats

The AI Project System defines five chat types operating in a strict hierarchy:

| Level | Chat Type | Role |
|-------|-----------|------|
| 0 | Creation Chat | Vision — permanent institution, authority-free |
| 1 | HQ Chat | Intent — coordinates phases, owns phase-level decisions |
| 2 | Phase Execution Chat | Milestone planning and delivery — produces, commits, and PRs Milestone specs and starters; oversees Milestone delivery |
| 3 | Milestone Execution Chat | Epic planning and delivery — produces, commits, and PRs Epic specs and starters; oversees Epic delivery |
| 4 | Epic Execution Chat (Coding Agent) | Implementation — writes code, tests, commits, and PRs |

**Terminology rule:** All chat levels from 2 upward are execution agents — they call tools, commit artifacts, and open PRs autonomously. The distinction is *what* they execute: Levels 2 and 3 execute and deliver planning artifacts; Level 4 executes and delivers code. **Implementation** — writing project code — is reserved for Level 4.

---

### 3.1 HQ Chats

HQ chats:
- Coordinate work
- Produce specs, roadmaps, and decisions
- Generate execution contracts (Epic Execution Chat Starters)
- Do NOT perform implementation

HQ chats are **authoritative for intent**, not for code.

#### 3.1.1 Epic Execution Chat Starter Format

When HQ Chat produces an Epic Execution Chat Starter, it MUST:

1. **Present in markdown code block:**
   - Use four backticks (````) to fence the code block
   - Ensures code blocks inside chat starter (triple backticks) are properly escaped
   
2. **Include filename in header:**
   - Format: `name=<epic-id>-epic-execution-chat-starter.md`
   - Example: `name=E5.1-epic-execution-chat-starter.md`
   - Helps users identify and save the file if needed

3. **Use markdown language identifier:**
   - Specify `markdown` as language for proper syntax highlighting
   - Full header format: ````markdown name=<epic-id>-epic-execution-chat-starter.md`

4. **Provide brief instruction:**
   - After code block, include: "Copy the entire chat starter above and paste into your Coding Agent chat to begin execution."
   - Clear call-to-action for user

**Rationale:** Code blocks provide clear visual boundaries, enable one-click copying, and prevent incomplete content selection. This significantly improves user experience when starting Epic execution.

**Example:**

`````markdown name=E5.1-epic-execution-chat-starter.md
## EPIC EXECUTION CHAT STARTER

### MANDATORY CONTEXT PACKET

**Project:** ai-project-system
[... full chat starter content ...]
```
`````

Copy the entire chat starter above and paste into your Coding Agent chat to begin execution.

**Scope:**
- **Applies to:** Epic Execution Chat Starters produced by HQ Chat
- **Does NOT apply to:** Normal HQ responses, Epic specs, Coding Agent outputs, or other governance documents

---

### 3.2 Coding Agent Chats

Coding Agent chats:
- Execute a single Epic
- Operate under an explicit execution contract
- Write code, tests, commits, PRs, and reports
- Must conclude autonomously when work is complete

Coding Agent chats are **authoritative for execution**, not for intent.

---

### 3.3 HQ Planning and Unplanned Progress Branches

During milestone or phase planning, HQ Chats MUST check for and review unplanned progress branches.

#### HQ Planning Behavior

When conducting planning (milestone or phase scope), HQ MUST:

1. **Ask about unplanned branches**: "Are there any unplanned progress branches to review?"
2. **Request branch listing**: Ask human to provide `unplanned/*` branch names
3. **Review each branch**:
   - Ask human to describe the branch intent and key commits
   - Review commits if branch content is accessible
   - Assess alignment with project goals
4. **Identify scope groupings**: If branch contains multi-topic work, identify logical commit groupings by scope. Propose separate Epics for distinct topics, each cherry-picking relevant commits.
5. **Propose integration approach** for each branch:
   - **Create Epic to integrate**: Define Epic with integration strategy
   - **Defer**: Branch stays open for future planning cycle
   - **Discard**: Branch is closed without integration (explicit decision documented)

#### Epic Specification Requirements for Unplanned Branch Integration

When an Epic is created to integrate work from an unplanned branch, the Epic spec MUST include:

1. **Branch reference**: Explicit name of the unplanned branch (e.g., `unplanned/template-refinements`)
2. **Integration strategy**: How the work will be integrated:
   - **Cherry-pick**: List specific commits or commit ranges to cherry-pick
   - **Full merge**: Merge entire branch history
   - **Partial integration**: Describe what subset of work to extract and how
   - **Reimplementation**: Reimplement concepts from scratch with reference to unplanned branch
3. **Branch closure**: Specify whether unplanned branch should be deleted after Epic completion

**For multi-topic unplanned branches:**
- HQ may create multiple Epics to integrate different aspects
- Each Epic cherry-picks commits relevant to its scope
- Epic specs must clearly document which commits are integrated

**Example (in Epic spec):**

```markdown
## Integration Strategy

This Epic integrates work from `unplanned/template-refinements`.

**Approach:** Cherry-pick commits from unplanned branch

**Commits to integrate:**
- `abc1234` — Add epic-review-seal.md template
- `def5678` — Refine delivery-notice.md structure
- `ghi9012` — Add examples to epic-spec.md template

**Branch closure:** Delete `unplanned/template-refinements` after Epic completion.
```

#### Coding Agent Integration Behavior

When executing an Epic that integrates an unplanned branch, Coding Agents MUST:

1. **Read unplanned branch**: Access commits and content from the specified unplanned branch
2. **Follow integration strategy exactly**: Execute the strategy defined in the Epic spec
   - If cherry-pick: Use `git cherry-pick` for specified commits
   - If full merge: Merge branch (though this should be rare given promotion rules)
   - If partial: Extract and implement specified subset
   - If reimplementation: Reference unplanned branch but write new code
3. **Work in Epic branch**: All integration work happens in the Epic branch (e.g., `epic/E4.3`)
4. **Do NOT modify unplanned branch**: Unplanned branch remains unchanged during integration
5. **Report integration**: Document which commits/work were integrated in Epic Delivery Notice
6. **Branch closure**: Delete unplanned branch after Epic closes ONLY if Epic spec specifies deletion

#### Branch Lifecycle

Unplanned branches have an **explicit lifecycle**:

- **Open**: Branch exists with commits; awaits planning review
- **Under Review**: HQ is evaluating during planning
- **Scheduled for Integration**: Epic created to integrate the work
- **Integrated**: Work fully absorbed into governed branch; branch deleted
- **Deferred**: Stays open for future planning cycle
- **Discarded**: Explicitly rejected; branch deleted without integration

**Critical Rule:** Unplanned branches MUST stay open until they are fully integrated OR explicitly discarded. There is no automatic expiration.

---

### 3.4 Milestone Closure

Milestone closure is the process by which HQ Chat declares a milestone complete, prompts for consolidation, and confirms full closure after merge.

**Key distinction:** Milestone closure is parallel to Epic closure but operates at the milestone level (consolidating Epic work into parent branch).

---

#### When Milestone Closure Begins

Milestone closure begins when:
- All planned Epics for the milestone are complete (executed, reviewed, accepted, merged)
- All milestone completion criteria (from milestone spec) are satisfied
- HQ Chat evaluates milestone status

**Trigger:** HQ Chat SHOULD proactively check milestone status when the last planned Epic is closed.

---

#### HQ Chat Milestone Closure Behavior (6 Steps)

When all milestone Epics are complete, HQ Chat MUST execute this process:

**Step 1: Evaluate Completion Criteria**
- Review milestone spec completion criteria section
- Verify each criterion is satisfied
- Document which criteria are met (or not met)
- Do NOT proceed if any criterion unsatisfied

**Step 2: Check Epic Status**
- Verify all planned Epics are executed
- Confirm all Epics reviewed and accepted
- Confirm all Epic branches merged to milestone branch
- List all completed Epics with status

**Step 3: Declare Milestone Complete**
- Issue explicit declaration: "Milestone <id> complete"
- Provide structured verification checklist
- Include milestone summary (brief description of what was delivered)

**Step 4: Prompt for Consolidation**
- Inform human that milestone consolidation is required
- Provide PR guidance:
  - Source branch: `milestone/<id>`
  - Target branch: `<parent-branch>` (identify phase branch or develop/main)
  - PR title suggestion: "Milestone <id>: <Milestone Name>"
  - PR description guidance: Include milestone summary and Epic list
- Do NOT create PR automatically (human owns this step)

**Step 5: After Merge — Declare Fully Closed**
- Once human confirms PR merged, declare "Milestone <id> fully closed"
- Record closure date
- Record merge commit SHA
- Confirm branch hierarchy preserved

**Step 6: Confirm Next Milestone Branch Created**
- Verify next milestone branch created from merged parent
- Branch name: `milestone/<next-id>`
- Confirm branching from correct parent (where previous milestone merged)

---

#### Milestone Closure Declaration Format

When declaring milestone complete (Step 3), HQ Chat MUST use this structured format:

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
- [Criterion 1]: ✅ Satisfied
- [Criterion 2]: ✅ Satisfied
- [Criterion 3]: ✅ Satisfied
[List all criteria from milestone spec]

## Milestone Summary

[2-4 sentence summary of what was delivered in this milestone]

## Required Action: Consolidation

**To fully close this milestone, consolidation is required:**

1. Create Pull Request:
   - Source: `milestone/<id>`
   - Target: `<parent-branch>` [Identify: phase/<id> or develop or main]
   - Title: "Milestone <id>: <Milestone Name>"
   - Description: Include milestone summary and Epic list above

2. Human reviews consolidation PR

3. Merge PR (become milestone closure commit)

4. Report merge commit SHA back to HQ

**Next milestone (`milestone/<next-id>`) MUST branch from `<parent-branch>` after merge.**
```

After merge is confirmed, HQ Chat issues a **Fully Closed Declaration:**

```markdown
# MILESTONE FULLY CLOSED — M<id>

**Milestone:** M<id> — <Milestone Name>
**Status:** CLOSED ✅
**Closure Date:** YYYY-MM-DD
**Closed By:** HQ Chat
**Merge Commit:** <sha>

## Closure Confirmation

✅ PR created: `milestone/<id>` → `<parent-branch>`
✅ PR merged: Consolidation commit `<sha>`
✅ Branch hierarchy preserved: Milestone work now in `<parent-branch>`
✅ Milestone declared fully closed

## Next Steps

- Create `milestone/<next-id>` from `<parent-branch>` branch
- Begin planning for Milestone <next-id>
```

---

#### Completion Criteria Evaluation (Critical)

HQ Chat MUST rigorously evaluate milestone completion criteria before declaring complete.

**Required behavior:**
1. Read milestone spec completion criteria section
2. Evaluate EACH criterion individually
3. Document verification for each criterion (satisfied or not)
4. Only declare complete if ALL criteria satisfied
5. If any criterion unsatisfied, do NOT declare complete — instead, identify missing work

**Example evaluation:**

```markdown
## Completion Criteria Evaluation

From milestone spec (P1-M5__milestone.md):

1. ✅ **All 3 Epics complete:** E5.1, E5.2, E5.3 executed and accepted
2. ✅ **Governance updated:** PROJECT-SYSTEM-GUIDELINES.md and AI-OPERATING-GUIDELINES.md include new sections
3. ✅ **Real usage feedback integrated:** Governance gaps from M4 closure addressed
4. ✅ **System refinement complete:** Templates and guidance improved based on M4 experience

All criteria satisfied. Milestone M5 is complete.
```

**If criteria not satisfied:**

```markdown
## Completion Criteria Evaluation

From milestone spec (P1-M5__milestone.md):

1. ✅ **All 3 Epics complete:** E5.1, E5.2, E5.3 executed and accepted
2. ❌ **Governance updated:** E5.3 not yet complete
3. ⚠️ **Real usage feedback integrated:** Partially complete (E5.3 pending)

Milestone M5 is NOT complete. E5.3 must be completed before milestone closure.
```

---

#### Milestone Closure vs. Epic Closure (Parallel Structure)

Milestone closure mirrors Epic closure:

| Step | Epic Closure | Milestone Closure |
|------|--------------|-------------------|
| **Completion** | All DoD items verified | All Epics complete, criteria satisfied |
| **Declaration** | Coding Agent declares execution complete | HQ declares milestone complete |
| **Consolidation Prompt** | Coding Agent produces Delivery Notice | HQ prompts for PR and consolidation |
| **Human Review** | Human reviews Epic work | Human reviews consolidation PR |
| **Authorization** | HQ authorizes delivery | Human approves merge |
| **Merge** | Epic branch → milestone branch | Milestone branch → parent branch |
| **Closure** | Epic declared closed | Milestone declared fully closed |
| **Next Step** | Next Epic can begin | Next milestone branches from parent |

**Key parallel:** Both require explicit consolidation via PR, human review, and formal closure declaration.

---

#### Authority and Responsibility

- **HQ Chat** owns milestone completion evaluation and closure declaration
- **Human** owns consolidation PR review and approval
- **Coding Agent** does NOT close milestones (out of scope for Coding Agents)

**HQ Chat MUST NOT:**
- Infer milestone complete without evaluating criteria
- Skip consolidation step
- Declare fully closed before merge confirmed
- Create next milestone branch without confirming correct parent

---

#### Edge Cases and Clarifications

**What if milestone has unmerged Epic branches?**
- Milestone is NOT complete
- HQ must ensure all Epic branches merged before declaring complete

**What if phase branch does not exist?**
- Milestone merges to `develop` or `main` (project-specific convention)
- HQ must identify correct target and document decision

**What if next milestone already exists?**
- This indicates process failure (next milestone should not exist until previous milestone fully closed)
- HQ must investigate and correct branch hierarchy

**What if human rejects consolidation PR?**
- Milestone remains "complete but not fully closed"
- Human identifies issues
- HQ creates follow-up Epic(s) to address issues
- Consolidation retried after follow-ups complete

---

### 3.5 Creation Chat (Level 0)

Creation Chat is a **permanent institution** above HQ Chat. It operates outside the phase/milestone lifecycle — it is never closed, never scoped to a phase, and holds no execution authority.

Creation Chat:
- Is initialized once by pasting `governance/templates/seed.md` into a fresh chat session
- Produces **Steering Notes** addressed to HQ Chat (carry binding CFO intent)
- Receives **Progress Digests** from HQ Chat
- Holds no execution authority — it does not plan phases, produce specs, or dispatch agents
- Captures vision and communicates it downward; HQ Chat interprets and acts on it

Creation Chat is **authoritative for vision**, not for plans.

---

### 3.6 Phase Execution Chat (Level 2)

Phase Execution Chat is a **finite autonomous execution and delivery agent scoped to a single Phase**. It is launched by HQ Chat using a Phase Execution Chat Starter.

**Stage 1 — Execution:** Reviews the Phase spec, produces Milestone specs and Milestone Execution Chat Starters, creates a phase branch, commits all planning artifacts, and opens a PR to HQ Chat for review.

**Stage 2 — Delivery:** After HQ Chat accepts the PR, oversees Milestone execution — receives Milestone Completion Notices, issues Milestone Review Decisions, and when all Milestones are accepted, delivers the Phase by executing the canonical phase-closure sequence (PROJECT-SYSTEM-GUIDELINES.md §5C) — the consolidation merge plus the mandatory README-update, version-bump, and git-tag steps.

Phase Execution Chat does NOT:
- Implement project code or modify infrastructure
- Dispatch Coding Agents — that is HQ Chat's authority after each Milestone Execution Chat Starter is accepted
- Make phase-level accept/reject decisions (those belong to HQ Chat)

**Artifact scope (adjacency):** Phase Execution Chat produces artifacts only for its direct parent or direct children — Milestone specs and Milestone Execution Chat Starters. It MUST NOT produce Epic specs or Epic Execution Chat Starters (a grandchild artifact that bypasses the Milestone Chat's review gate), nor any grandparent artifact above its level. See the **"Artifact Scope Adjacency"** section of `governance/systems/chat-hierarchy.md` for the full rule and the adjacency table.

Phase Execution Chat is **authoritative for milestone planning and delivery**, not for implementation or phase decisions.

---

### 3.7 Milestone Execution Chat (Level 3)

Milestone Execution Chat is a **finite autonomous execution and delivery agent scoped to a single Milestone**. It is launched by Phase Execution Chat (or HQ Chat during bootstrap) using a Milestone Execution Chat Starter.

**Stage 1 — Execution:** Reviews the Milestone spec, produces Epic specs and Epic Execution Chat Starters, creates a milestone branch, commits all planning artifacts, and opens a PR to the parent chat for review.

**Stage 2 — Delivery:** After the parent chat accepts the PR, oversees Epic execution — receives Epic Completion Notices (Delivery Notices from Coding Agents), issues Epic Review Decisions, and when all Epics are accepted, delivers the Milestone by merging the milestone branch.

Milestone Execution Chat does NOT:
- Implement project code or modify infrastructure
- Dispatch Coding Agents directly — Epic Execution Chat Starters are delivered to the parent chat, which authorizes each Coding Agent launch
- Make milestone-level accept/reject decisions (those belong to the parent chat)

**Artifact scope (adjacency):** Milestone Execution Chat produces artifacts only for its direct parent or direct children — Epic specs and Epic Execution Chat Starters. It MUST NOT produce Milestone specs (its parent's job) or code, tests, or PRs (its grandchildren's job). See the **"Artifact Scope Adjacency"** section of `governance/systems/chat-hierarchy.md` for the full rule and the adjacency table.

Milestone Execution Chat is **authoritative for epic planning and delivery**, not for implementation or milestone decisions.

---

### 3.8 Working-Tree Isolation

When two or more chats are active simultaneously, each chat MUST operate in its own git
working tree. A chat MUST NOT commit in a working tree that another concurrently-active
chat may switch (check out a different branch in): a branch checkout by one chat silently
re-targets the other chat's next commit, landing it on the wrong branch.

Create a dedicated tree per active chat — `git worktree add ../worktree-<role>-<id> <branch>`
— and work only in your own tree for the lifetime of the chat. This applies whenever two
or more chats run concurrently; a single chat working alone does not need a separate
worktree.

See the **"Working-Tree Isolation"** section of `governance/systems/chat-hierarchy.md` for
the full rule, practical guidance, and a worked `git worktree` example.

---

### 3.9 Scope Direction Protocol

Scope direction from the Creation Chat or CFO to any in-flight Epic MUST flow through the
mandatory channel: Steering Note → HQ Chat → spec amendment → Milestone Chat re-issues the
amended starter. Scope MUST NOT change through any informal path — a chat message or a
hand-edited starter pasted into a running session does not change an Epic's scope. The only
exception is a P0 production emergency, where an unblocking directive may be issued verbally
and MUST be formalized within the same session via a Steering Note and a retroactive spec
amendment. An Epic executes only against its committed, re-issued starter.

See the **"Scope Direction Protocol"** section of `governance/systems/chat-hierarchy.md`
for the HQ-ratified rule verbatim, the P0 exception, and the rationale.

---

### 3.10 Communication Protocol

Information moves through the hierarchy in two directions, each with exactly one sanctioned
channel. **Upward communication is 1-to-1:** every level has exactly one parent; escalations
and completion notices travel up one level, and the receiving level decides whether to absorb
or escalate further. No level skips its parent to reach a grandparent. **Downward
communication is the spec file, not broadcasting:** a parent amends its own spec, and children
— including those mid-execution — read from that same source at any time (one write, many
readers, no separate message per child). The level spec file is therefore **dual-role** — a
planning artifact and a live contract holding the authoritative state of scope, constraints,
and directives including amendments.

**Mid-flight updates escalate UP.** If a directive changes after children are running, the
parent amends the spec and, if the change is blocking, escalates up to its own parent to
decide whether to pause or cancel affected children. A chat MUST NOT reach downward into a
running child session.

See the **"Communication Protocol"** section of `governance/systems/chat-hierarchy.md` for the
four decisions in full and the amendment-issuing guidance, and §3.9 (Scope Direction Protocol)
for the related channel that routes externally-originated scope changes through the same spec
amendment.

---

## 4. Authority Hierarchy

AI must respect the following authority order:

1. PROJECT-SYSTEM-GUIDELINES.md
2. AI-OPERATING-GUIDELINES.md
3. Epic Execution Chat Starter
4. Epic Spec
5. Decisions
6. System References
7. Chat messages

Lower layers MUST NOT override higher layers.

---

## 5. Epic Execution Chat Starter (Binding Contract)

Epic specs are authoritative inputs and MUST exist before execution begins. If an Epic spec is not found at the declared path, the Coding Agent MUST stop and report the issue. Coding Agents MUST NOT create or redefine Epic specs.

Coding Agents MUST treat the **Epic Execution Chat Starter** as a binding execution contract.

The starter defines:
- Scope of execution
- Branch and delivery requirements
- Definition of Done expectations
- When the agent is allowed to stop

If the starter is incomplete or violates governance:
- Execution MUST NOT begin
- AI must ask for clarification

Epic Execution Chat Starters are produced by HQ chats and MUST NOT be inferred, synthesized, or reconstructed by humans or Coding Agents.

---

## 6. Scope Discipline

AI MUST:
- Execute only what is explicitly in scope
- Respect explicit non-goals
- Refuse scope expansion unless authorized by a new spec

AI MUST NOT:
- Invent features
- Generalize beyond the spec
- “Improve” things not requested

---

## 7. Delivery Enforcement

AI MUST:
- Commit all work to the branch defined in the execution starter
- Open PRs only to allowed target branches
- Follow branch promotion rules strictly
- Treat delivery as a Definition of Done requirement

AI MUST NOT:
- Default to conventional Git workflows
- Skip PR creation
- Delegate delivery to the human implicitly

If delivery cannot be completed, AI must block and ask.

When an execution contract specifies a target branch that does not yet exist, the Coding Agent MAY create the branch from the correct parent branch before opening a pull request.

### Pull Request Creation Strategy

Coding Agents MUST attempt to create pull requests using an automated method when available.

If the primary method is unavailable or fails, the agent MUST attempt at least one alternative method before deferring to a human.

If automated PR creation is not possible, the agent MUST:
- Verify that all delivery artifacts are committed
- Provide an exact PR creation URL
- Provide a ready-to-use PR title and body
- Explicitly state that manual PR creation is the only remaining step

In such cases, the Epic MAY be considered complete once delivery readiness is verified and the handoff is explicit.

---

## 8. External Tracker Semantics

AI **must not assume external tracker semantics**.

When a project declares integration with a project tracker:
- AI MUST rely on declared mappings
- AI MUST follow the Project Tracker Integration System reference
- AI MUST NOT infer hierarchy, states, or workflows

If tracker mappings are missing or ambiguous, execution MUST stop.

If no explicit tracker mapping is declared, the AI MUST assume no tracker integration exists and MUST NOT interact with external tracking systems.

---

## 9. Question Policy

AI may ask questions ONLY when:
- Execution is blocked
- Required information is missing
- A rule conflict is detected

AI must NOT ask:
- Preference questions
- “What do you think?” prompts
- Open-ended design questions during execution
---

## 13. Error Handling

If AI detects:
- Missing specs
- Invalid branch targets
- Governance violations

It must:
- Stop execution
- State the issue clearly
- Request explicit guidance

Silent failure or guessing is prohibited.

---

## 14. Evolution

These guidelines evolve:
- Intentionally
- Additively
- Via versioned documentation

AI must always prefer the most recent version.
---

## 10. Execution Completion vs. Acceptance

**Critical distinction:** Execution completion is NOT the same as acceptance.

- **Execution Completion:** The Epic is technically correct, all Definition of Done items are verified, code is delivered, and tests pass.
- **Delivery Notice:** A structured, explicit notice produced by the Coding Agent upon execution completion. This is a mandatory artifact and a prerequisite for human review and Epic Delivery Authorization decision. No Epic may proceed to review or closure without a Delivery Notice.
- **Acceptance:** A human (Layer 8) has reviewed the execution, made a judgment about correctness and fitness, and HQ Chat has made an explicit accept/reject decision.


Canonical flow:

```
Human review (plain language) → AI-generated Epic Review Seal → HQ decision
```
**HQ Chat review behavior:**
- Ask humans for plain-language findings only; do not require markdown editing.
- Generate or request AI-generated Epic Review Seals from human input, then confirm accuracy with the human before deciding.
- Keep acceptance decisions explicit and record them in the Review Decision; do not introduce execution or acceptance loops.

**Coding Agent support during review:**
- When asked, generate Epic Review Seal drafts from human-provided natural language without altering intent.
- Present the draft to the human for confirmation before HQ decision.
- Do not ask humans to format or edit markdown; handle structuring within AI.

**Coding Agent enforcement and stop rules:**
- Coding Agent MUST always produce a Delivery Notice upon execution completion.
- Coding Agent MUST explicitly state when it is awaiting HQ authorization and refuse to proceed without it.
- Coding Agent MUST NOT close an Epic with uncommitted changes.
- Coding Agent MUST stop execution immediately after merge; no further actions are permitted.

Coding Agents MUST:
- Report execution completion accurately
- Stop after reporting
- NOT infer acceptance
- NOT iterate without a new execution contract

HQ Chat (human) MUST:
- Conduct human review after execution completion
- Request or provide findings in natural language (no markdown required)
- Use AI to generate the Epic Review Seal from that input (see below)
- Make an explicit accept/reject decision
- Create follow-up Epics if required

**HQ Chat enforcement and closure rules:**
- HQ Chat MUST require a Delivery Notice before review.
- HQ Chat MUST issue explicit Epic Delivery Authorization before PR/merge.
- HQ Chat MUST decide resolution for any uncommitted changes before closure.
- HQ Chat MUST declare Epics closed only after merge.

This separation prevents ambiguity and ensures human judgment is properly captured.

---

## 11. Human Review and Epic Review Seal

After a Coding Agent reports execution completion, human review is required before acceptance can be finalized.

**Human Review Process:**
1. Human (Layer 8) tests/reviews the delivered work
2. Human shares findings in natural language (chat, notes, or bullets—no structure required)
3. AI (Coding Agent or HQ Chat) structures those findings into an **Epic Review Seal** for human approval; the human is not required to write or edit markdown
4. AI (on behalf of the human) posts the Epic Review Seal into HQ Chat, requesting an explicit decision

The Epic Review Seal is NOT an acceptance artifact. It is a decision input.

The Epic Review Seal captures:
- What was tested or reviewed
- Findings in plain language
- Issues identified (if any)
- An explicit request for HQ decision: **Accept as-is**, **Accept with follow-up Epic(s)**, or **Reject and create new Epic(s)**

Example Epic Review Seal structure (see governance/templates/epic-review-seal.md for canonical form):

```
---
## Epic Review Seal — [Epic ID]

**Reviewer:** [Name]  
**Review Date:** [Date]  
**Epic:** [Epic ID and Title]  

**Findings:**
- [Finding 1]
- [Finding 2]
- [Issue 1, if any]

**Recommendation:** [Accept as-is | Accept with follow-ups | Reject]

**HQ Decision Requested:** Based on findings above, should this Epic be:
1. Accepted as-is
2. Accepted with follow-up Epic(s)
3. Rejected and require new Epic(s)

---
```

---

## 12. Acceptance Outcomes

HQ Chat makes explicit acceptance decisions using one of three outcomes:

1. **Accept as-is:** Epic is complete, no follow-ups needed.
2. **Accept with follow-up Epic(s):** Epic is accepted, but new Epics must be created to address findings.
3. **Reject:** Epic does not meet requirements; new Epic(s) must be created.

Acceptance is documented in the Review Decision and becomes immutable.

---

## 13. Exit Ritual (Mandatory)

A Coding Agent chat concludes ONLY when:

1. All Definition of Done items are satisfied
2. Delivery requirements are fulfilled
3. A structured Delivery Notice has been produced and committed
4. AI explicitly declares the Epic complete
5. HQ authorization for PR/merge has been received and executed
7. The working tree is clean (no uncommitted changes)
8. Execution stops immediately after merge

---

## 14. Error Handling

If AI detects:
- Missing specs
- Invalid branch targets
- Governance violations

It must:
- Stop execution
- State the issue clearly
- Request explicit guidance

Silent failure or guessing is prohibited.

---

## 16. Visual Artifact Production

Visual artifacts are an **opt-in** capability. Every chat level may produce a visual appropriate to
its altitude — but only when the capability is enabled and the producing agent can call tools. This
section governs *use*; the configuration schema is defined in `governance/ai-project-yml-spec.md` §3.5.

### 16.1 Opt-in gating

The capability is active only when `.ai-project.yml` carries `visual_artifacts.enabled: true`. An
**absent block or `enabled: false` means the capability is off** — agents MUST NOT attempt
generative visual production, and the integration test that exercises it MUST skip (not fail). The
block's keys are `enabled` (bool), `comfyui_url` (URL), and `types` (a subset of `diagrams`,
`infographics`, `video`), read through the single config source in `bin/ai-project-orchestrator`
(`load_yml_config` / `resolve_visual_artifacts`).

### 16.2 Per-level abstraction

Each chat level produces visuals at its own level of abstraction. An agent produces the visual for
**its** level — it does not reach up or down the cascade:

| Chat level | Visual type |
|------------|-------------|
| Creation Chat | Concept / vision imagery |
| HQ Chat | System architecture |
| Phase Chat | Phase scope diagram |
| Milestone Chat | Component + flow diagrams |
| Epic Chat | UI mockups, before/after, implementation diagrams |

Visual intent originates at the **Creation Chat** — elicited at inception via `seed.md` Rule 4 ("What
does success look like visually?") — and propagates down the artifact cascade: each level translates
the level above's vision into the visual appropriate to its own scope. Each level produces that
abstraction in **both** tracks — a proposed and an implemented visual (§16.6) — at its own altitude.

### 16.3 Two modes

- **Structural** — diagrams expressed as text (Mermaid / PlantUML), committed alongside the artifact
  they illustrate. Structural visuals need no endpoint and no capability beyond writing a fenced code
  block; prefer them for architecture, scope, component, and flow diagrams.
- **Generative** — imagery or video produced from a natural-language prompt via the configured
  ComfyUI endpoint, using the `bin/ai-project-visual` helper. Use generative mode for concept/vision
  imagery, infographics, and UI mockups where a rendered image communicates better than a diagram.

Prefer Structural for most coverage: it is what makes the proposed→implemented two-track default
(§16.6) affordable, since most pairs are two text diagrams at no cost.

### 16.4 Tool-capability gating

The gate is **capability, not the chat-level label.** An agent produces a generative visual only if
it can call tools (run `bin/ai-project-visual` and reach the endpoint). A chat operating in a
tool-less surface produces **structural** visuals only and MUST NOT claim to have generated imagery
it cannot produce. When a level's visual requires generation and the agent lacks tool capability, it
records the visual intent in its artifact and defers generation to a tool-capable agent rather than
fabricating a result.

### 16.5 What to commit, and where

- **Structural** diagrams live inline in the governing artifact (spec, brief, guide) or as a sibling
  `.mmd` / `.puml` file next to it.
- **Generated** artifacts are **referenced by link, never committed to git.** The helper writes a
  local working file; the agent hosts it on the **adopter's storage backend** and references it by
  link from the governing artifact, so the **link** — not the binary — travels with the decision
  record. Where generated binaries live is the adopting team's decision: the framework is
  infrastructure-agnostic about storage just as it is about endpoints and agents.
- **No** project commits generated binaries — the governance **source** repo's
  `visual_artifacts.enabled: false` is one instance of that universal rule. The source repo ships the
  guidance, the helper, and the test — not generated output.

### 16.6 Proposed vs. implemented

When the capability is enabled, every level produces **both** a *proposed* visual (the intent, before
the work is built) and an *implemented* visual (what was actually built, after) — not one or the
other. The proposed visual records what the level set out to make; the implemented visual records what
it delivered, so the gap between intent and result stays visible at every altitude. **Producing both
is the routine default, not an exception.**

**Nothing is too much.** Be generous: err toward producing the pair rather than skipping it. The bar
is *coverage* — a proposed→implemented pair at each enabled level — not restraint.

**Structural-first is what makes that affordable.** Most coverage is free: a proposed and an
implemented Mermaid/PlantUML diagram are two text blocks with no endpoint and no cost (§16.3). Lean on
Structural for most pairs and reserve Generative (ComfyUI) for the levels where a rendered image
genuinely communicates better — a Creation concept, an Epic mockup. Because the cheap path carries
most of the load, "nothing is too much" stays cheap.

The two tracks are recorded through the **`State` field of the §7 binding** (`proposed` /
`implemented`) defined in `governance/guides/visual-artifacts.md` §7 — a level may carry one binding
of each `State`. This subsection sets the *expectation*; §7 defines *how* a track is recorded. Do not
restate that schema here.

The gates still bind: the two-track default applies **only when enabled** (§16.1), and a tool-less
surface produces **Structural** visuals only (§16.4) — where a proposed visual would need generation,
the agent records the intent and defers it per §16.4 rather than fabricating a render.

See `governance/guides/visual-artifacts.md` for endpoint configuration, structural-diagram tooling,
output formats, and a worked example per chat level.

### 16.7 Clips

A **clip** is a short video that renders **one** governance node's proposed→implemented story (§16.6)
as motion — the most CFO-facing visual, and the one that doubles as publishable media. Its policy is
single-parent binding:

- **Single-parent.** A clip binds to exactly **one** node — one epic, one milestone, or one phase —
  via the §7 binding with `What: clip` and `Level` set to that node. It narrates **that node's** two
  tracks (§16.6); it does not reach up or down the cascade (the altitude rule, §16.2).
- **Hosted and linked, never committed.** A clip is a generated `.webm`, so by-link (§16.5 / §7) binds
  it exactly as it binds an image: the helper writes a local working file, the agent hosts it, and the
  **link** — not the binary — travels with the decision record. Do not commit the `.webm`.
- **No cross-cutting reel.** A clip is single-parent by rule. A project-spanning editorial montage that
  stitches many nodes into one reel is **deferred in P6** (SN-16, binding decision 3) — do not build
  one; bind one node's arc.

For how a clip is **produced** from the arc (on the verified LTX-Video path) and **published** (the
same hosted asset reused, not a second production), see `governance/guides/visual-artifacts.md` §8.
**Reference §7 for the binding schema — `clip` is an existing `What` value; do not restate the schema
here.**

---

## 15. Closing Statement

AI is a force multiplier only when it is constrained.

Clarity is kindness.  
Constraints enable autonomy.

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 2.5.1 | 2026-07-02 | Reconciled the §3.6 Stage 2 phase-delivery clause to the canonical phase-closure sequence (PSG §5C, new in PSG v2.2.0): the Phase Chat delivers the Phase by executing §5C — the consolidation merge **plus** the mandatory README-update, version-bump, and git-tag steps — not by merging the phase branch alone. No acceptance / Review-Decision language changed (that surface is E25.2). E25.1 (P6-M25). |
| 2.5.0 | 2026-07-02 | Added §16.7 "Clips": a clip is a short video rendering **one** governance node's proposed→implemented story (§16.6) as motion. Establishes the clip convention at policy altitude — **single-parent** (binds to exactly one epic / milestone / phase via the §7 binding with `What: clip`, narrating that node's two tracks, not spanning the cascade), **hosted and linked, never committed** (by-link, §16.5 / §7, holds for `.webm` as for images), and the **no-cross-cutting-reel boundary** (a project-spanning montage is deferred in P6). Points to `governance/guides/visual-artifacts.md` §8 for production (on the verified LTX-Video path) and publish (same hosted asset reused). The §7 schema is **referenced, not restated**; `clip` is an existing `What` value (not re-added). Per SN-16 (ratified 2026-06-29), binding decision 3; E24.2 (P6-M24). |
| 2.4.0 | 2026-06-29 | Added §16.6 "Proposed vs. implemented": establishes the **two-track expectation as the routine default** — when `visual_artifacts.enabled: true`, every level produces **both** a *proposed* (intent, before build) and an *implemented* (after) visual, with the **"nothing is too much"** coverage bar and a **Structural-first** preference (most pairs are two free text diagrams; reserve Generative for where a render communicates better). The two tracks are recorded via the §7 binding's `State` field (referenced, **not** restated); the §16.1 opt-in and §16.4 tool-capability gates still bind (a tool-less surface produces Structural only and defers generative intent). Added a one-line tie-in to §16.2 and §16.3. Per SN-15/SN-16 (ratified 2026-06-29); E24.1 (P6-M24). |
| 2.3.0 | 2026-06-29 | **Reversal of v5.0.0 shipped guidance.** Rewrote §16.5 to the **by-link** storage model: generated visual artifacts are **never committed to git** — the helper writes a local working file, which the agent hosts on the adopter's storage backend and references by link from the governing artifact (the link, not the binary, travels with the decision record). Generalized the source-repo bullet so that *no* project commits generated binaries — `enabled: false` is one instance of that universal rule. Structural-diagram (Mermaid/PlantUML) guidance unchanged. Per SN-16 (ratified 2026-06-29); E23.1 (P6-M23). |
| 2.2.0 | 2026-06-28 | Added §16 "Visual Artifact Production": per-level abstraction table (SN-11), structural vs. generative modes, tool-capability gating, and commit guidance — opt-in on `visual_artifacts.enabled` (ai-project-yml-spec.md §3.5). Part of E22.2 (P5-M22), which completes VA-1 with `seed.md` Rule 4 visual-intent elicitation, the `bin/ai-project-visual` helper, `governance/guides/visual-artifacts.md`, and a skip-on-disabled integration test. |
| 2.1.0 | 2026-06-23 | Added §3.5–3.7 definitions for Creation Chat, Phase Chat, and Milestone Chat. Added chat hierarchy table to §3 intro. Updated Purpose to name all five chat types. Fixes P5-GH-7: Phase/Milestone chat roles introduced in P4 were absent from this document, causing HQ Chat to use Epic-level rules when producing Phase/Milestone starters. |
| 2.0.0 | 2026-04-20 | Governance files migrated from `docs/` to `/governance/` (E6.2). Updated template path references. |
| 1.4.1 | 2026-02-22 | Previous version — governance lived in `docs/`. |
