# PROJECT SYSTEM GUIDELINES
*(Authoritative Project Structure, Documentation, and Execution Policy)*

**Version:** 2.0.0  
**Effective Date:** 2026-04-20  
**Status:** Current  

---

## 1. Purpose

This document defines the **authoritative project system rules** used across all projects.

It governs:
- Repository structure
- Documentation organization (`docs/` as a system)
- Branch naming, hierarchy, and promotion
- Markdown conventions and front-matter
- Execution eligibility, delivery, and closure
- AI-assisted execution behavior
- Cross-project consistency

If any structure, document, or practice conflicts with this file, **this file wins**.

---

## 1A. Canonical Happy Path for Epic Closure (Mandatory)

All Epics MUST follow the single canonical happy path for closure:

1. **Execution**: Coding Agent executes all Definition of Done items.
2. **Delivery Notice**: Coding Agent produces a structured Epic Delivery Notice and declares execution complete. No Epic may proceed to review or closure without this notice.
3. **Human Review**: HQ Chat requests and receives human review findings in plain language.
4. **Epic Review Seal**: AI (Coding Agent or HQ Chat) structures findings into an Epic Review Seal for human confirmation.
5. **HQ Decision**: HQ Chat issues an explicit delivery authorization (accept, accept-with-follow-ups, or reject).
6. **HQ Delivery Authorization**: Only after explicit HQ authorization may a PR be created and merged.
7. **PR and Merge**: Coding Agent opens a PR to the correct branch and merges only after HQ authorization. No Epic may close with uncommitted changes or without merge.
8. **Stop**: Execution stops immediately after merge. No further actions are taken.

**No step may be skipped, inferred, or collapsed.**

---

---

## 2. Core Principles

- **Consistency over optimization**  
  Predictability is more valuable than local perfection.

- **Markdown is a first-class artifact**  
  Durable knowledge lives in versioned Markdown files.

- **Structure enables scale**  
  Clear structure allows parallel work without coordination overhead.

- **Context must be explicit and derivable**  
  Execution context must be mechanically extractable, not remembered.

- **Done must be explicit**  
  Execution units must define and record their own completion.

- **Delivery follows hierarchy, not convenience**  
  Branch promotion is governed, not inferred.

---

## 3. Canonical Repository Structure

```
/
├─ governance/
│  ├─ README.md
│  ├─ PROJECT-SYSTEM-GUIDELINES.md
│  ├─ AI-OPERATING-GUIDELINES.md
│  ├─ EPIC-EXECUTION-CHAT-STARTER.md
│  ├─ agents/
│  ├─ diagrams/
│  ├─ guides/
│  ├─ systems/
│  └─ templates/
├─ docs/
│  ├─ README.md
│  ├─ roadmap/
│  ├─ phases/
│  ├─ decisions/
│  ├─ context/
│  └─ _legacy/
├─ src/
├─ tests/
└─ README.md
```

Governance files live under `governance/`. All project history and execution artifacts live under `docs/`.

---

## 4. The `docs/` Folder as a System

The `docs/` directory is a **structured, executable knowledge system**, not passive documentation.

Rules:
- Documentation precedes execution
- Specs drive implementation
- Decisions are explicit and immutable
- Context is preserved independently of chats

Chats are ephemeral.  
Markdown is authoritative.

Local enforcement is defined in `docs/README.md`.

---

## 5. Mandatory Document Front-Matter

All **execution-relevant Markdown documents** MUST begin with a YAML front-matter block.

### Required Front-Matter

```
---
project: <project-name>
phase: P<id>
milestone: M<id>
epic: E<id> | null
type: <spec | decision | system | task | completion | reference>
status: <draft | active | completed | deprecated>
last_updated: YYYY-MM-DD
---
```

Front-matter is mandatory for:
- Phase, milestone, and epic specs
- Decisions
- System installation tasks
- Operational system references
- Epic completion reports

Front-matter is not required for:
- Governance documents
- Index files (README)
- Templates

Execution context MUST be derivable from front-matter.

---

## 5B. Milestone Closure

Milestone closure is the process of consolidating a completed milestone's work into the parent branch and formally declaring the milestone fully closed.

### Milestone Closure vs. Completion

**Two distinct states:**

- **Milestone complete:** All planned Epics for the milestone are executed, reviewed, accepted, and merged to the milestone branch. All milestone completion criteria (from milestone spec) are satisfied.

- **Milestone fully closed:** Milestone complete AND consolidated into parent branch via merged PR. The milestone branch work is now part of the canonical branch hierarchy.

**A milestone can be "complete" without being "fully closed."** Full closure requires consolidation.

---

### 7-Step Milestone Closure Process

Milestone closure follows a structured process parallel to Epic closure:

**Step 1: All Epics Complete**
- All planned Epics for the milestone are executed
- All Epics reviewed and accepted by HQ
- All Epic branches merged to milestone branch
- Milestone branch contains all milestone work

**Step 2: HQ Declares Milestone Complete**
- HQ Chat evaluates milestone completion criteria (from milestone spec)
- Verifies each criterion is satisfied
- Declares "Milestone <id> complete" with verification checklist
- Documents milestone summary

**Step 3: PR Created**
- Create Pull Request: `milestone/<id>` → parent branch
- Parent branch determined by branch hierarchy (see below)
- PR title: "Milestone <id>: <Milestone Name>"
- PR description includes milestone summary and Epic list

**Step 4: Human Reviews Consolidation**
- Human reviews PR to verify all milestone work is present
- Confirms branch hierarchy is correct
- Verifies no conflicts or missing work
- Approves consolidation

**Step 5: Merge Completes**
- PR merged after human approval
- Milestone work now consolidated into parent branch
- Merge commit becomes milestone closure commit

**Step 6: Milestone Declared Fully Closed**
- HQ declares "Milestone <id> fully closed"
- Records closure date and merge commit
- Confirms branch hierarchy preserved

**Step 7: Next Milestone Branch Created**
- Next milestone branch created from merged parent branch
- Ensures next milestone starts from clean baseline
- Branch name: `milestone/<next-id>`

---

### Branch Hierarchy Consolidation

Milestone closure consolidates work up the branch hierarchy:

```
epic/E<id> → milestone/M<id> → phase/P<id> → develop/main
           (Epic closure)    (Milestone      (Phase
                             closure)         closure)
```

**Consolidation rules:**
- **Epic branches** merge to **milestone branches** (Epic closure)
- **Milestone branches** merge to **phase branches** OR **develop/main** (Milestone closure)
- **Phase branches** merge to **develop** or **main** (Phase closure - future work)

**Each level requires explicit PR and human review.** No automatic promotion.

---

### Parent Branch Determination

When closing a milestone, determine the parent branch:

**If phase branch exists:**
- Milestone merges to phase branch: `milestone/M<id>` → `phase/P<id>`
- Next milestone branches from same phase branch

**If no phase branch exists:**
- Milestone merges to `develop` or `main` (project-specific)
- Next milestone branches from same target (`develop` or `main`)

**Rule:** Next milestone MUST branch from the same parent where previous milestone merged.

---

### Example: Milestone M4 Closure

**Context:** Milestone M4 (System Refinement) completed 2026-02-17 with 4 Epics (E4.1-E4.4).

**Closure workflow:**

1. **All Epics complete:** E4.1, E4.2, E4.3, E4.4 executed, accepted, merged to `milestone/M4`
2. **HQ declares M4 complete:** HQ evaluated M4 completion criteria, all satisfied
3. **PR created:** `milestone/M4` → `phase/P1` (Phase 1 branch exists)
4. **Human reviews:** Verified all M4 work present, no conflicts
5. **Merge completes:** PR merged (commit `1784fe0`)
6. **M4 declared fully closed:** Milestone M4 fully closed 2026-02-17
7. **M5 branch created:** `milestone/M5` created from `phase/P1` (merged parent)

**Key insight:** M4 closure exposed the need for explicit milestone closure process (this Epic formalizes that process).

---

### Milestone Closure Authority

- **HQ Chat** declares milestone complete (evaluates criteria)
- **Human** reviews and approves consolidation PR
- **HQ Chat** declares milestone fully closed (after merge)
- **Coding Agent** does NOT close milestones (authority belongs to HQ and human)

---

### No Uncommitted Work at Closure

At milestone closure (Step 6), the milestone branch MUST have:
- All Epic branches merged
- All commits consolidated
- No uncommitted changes
- Clean working tree

**Uncommitted work blocks closure.** All work must be committed and merged before milestone is declared fully closed.

---

## 6. File Naming Conventions

Epic-level files:

```
P<phase>-M<milestone>-E<epic>__<type>__<slug>.md
```

Rules:
- Filenames must be meaningful in isolation
- Dates use `YYYY-MM-DD`
- No ambiguous names

---

## 7. Branch Naming Rules

Branches represent **intent**, not individuals.

```
phase/P<id>
milestone/M<id>
epic/E<id>
fix/<slug>
spike/<slug>
```

One epic branch corresponds to one epic spec.

---

## 8. Branch Promotion Rules (Mandatory)

Branch merges MUST follow the project hierarchy.

Only Coding Agents (and humans) are permitted to mutate the repository, including creating branches, committing files, and opening pull requests. HQ chats are declarative only and MUST NOT be assumed to have filesystem or CLI access.

Coding Agents MAY create Epic, Milestone, or Phase branches when required to fulfill an explicit execution contract. Branch creation MUST be intentional and traceable to an Epic Execution Chat Starter or a system installation task.

### Promotion Path

```
epic/*      → milestone/*
milestone/* → phase/*
phase/*     → develop
```

### Rules

- Epic branches MUST only open PRs against their parent milestone branch
- Milestone branches MUST only open PRs against their parent phase branch
- Phase branches are promoted to `develop` only once all milestones are integrated
- Direct PRs that skip hierarchy levels are invalid
- If the correct target branch does not exist, execution MUST pause for clarification

These rules override conventional Git workflows.

---

## 8A. Unplanned Progress Branches

**Purpose:** Capture exploratory work, creative insights, and improvements that emerge during execution but fall outside current Epic scope, without breaking execution discipline.

Unplanned Progress Branches provide a Git-native mechanism for preserving ideas and work that need planning integration before acceptance.

### Branch Naming

```
unplanned/<descriptive-slug>
```

Branch names should be descriptive but not restrictive. Single-topic names (e.g., `unplanned/delivery-notice-improvements`) and multi-topic names (e.g., `unplanned/m5-explorations`, `unplanned/governance-clarifications`) are both valid. The slug helps identify the general area of work but does not constrain scope.

Examples:
- `unplanned/template-refinements`
- `unplanned/governance-clarifications`
- `unplanned/example-improvements`
- `unplanned/m5-explorations`

### Authority

Unplanned branches are **proposals**, not accepted work.

- Work in unplanned branches has no authority until explicitly integrated via Epic execution
- Unplanned branches MUST NOT be merged directly to milestone, phase, or develop branches
- Integration MUST occur through a planned Epic with explicit integration strategy

### Lifecycle

1. **Creation**: When insight or improvement emerges during execution, create `unplanned/<topic>` from a stable branch (develop, phase, or milestone)
2. **Work**: Commits are made freely to capture ideas, prototypes, improvements across any topics. Multi-topic drift is allowed and expected. When ready to return to governance, organize commits by scope (via rebase, commit splitting, reordering, or clear commit messages) to facilitate cherry-picking during integration. Freedom during exploration, discipline during integration.
3. **Planning Review**: During HQ planning sessions, unplanned branches are reviewed for potential integration
4. **Integration**: HQ creates an Epic to integrate the work; Epic spec defines integration strategy
5. **Closure**: After successful integration OR explicit rejection, the unplanned branch is deleted

### Rules

- MUST be created from a stable branch (develop, phase/*, or milestone/*)
- MUST contain meaningful work (not a dumping ground for random unrelated commits)
- MAY contain multi-topic exploratory work
- Organization by scope happens before integration, not during exploration
- MUST NOT merge directly to any governed branch
- MUST be reviewed by HQ during planning
- MUST be integrated via Epic execution only
- MUST stay open until fully integrated or explicitly discarded (no automatic expiration)

### Distinction from Epic Branches

| Aspect | Epic Branch | Unplanned Branch |
|--------|-------------|------------------|
| **Authority** | Authoritative (spec-driven) | Proposal (needs planning) |
| **Scope** | Defined in Epic spec | Exploratory, emergent |
| **Entry** | Epic spec MUST exist first | Created when insight emerges |
| **Integration** | Promoted via branch hierarchy | Integrated via Epic execution |
| **Lifecycle** | Created → Execute → PR → Merge → Delete | Created → Review → Epic plans integration → Delete |

### Example Workflow

1. **During Epic E3.5 execution**, a developer notices template improvements that would help users
2. **Insight is out of scope** for E3.5 (correctly — scope discipline is preserved)
3. **Developer creates** `unplanned/template-refinements` from `milestone/M3`
4. **Developer commits** improvements to unplanned branch (5 commits)
   - (Branch may accumulate commits across multiple topics — this is expected)
5. **During M4 planning**, HQ asks: "Are there any unplanned branches to review?"
6. **Human reports** `unplanned/template-refinements` exists with template improvements
7. **HQ reviews** commits and proposes integration
   - (If branch contains multi-topic work, HQ may create multiple Epics, each cherry-picking relevant commits)
8. **HQ creates Epic E4.3**: "Integrate Template Refinements"
9. **Epic spec defines strategy**: Cherry-pick commits 2, 3, 5 from `unplanned/template-refinements`
10. **Coding Agent executes E4.3**: Reads unplanned branch, cherry-picks specified commits to `epic/E4.3`
11. **After E4.3 closes**: `unplanned/template-refinements` is deleted (work fully integrated)

---

## 9. Documentation ↔ Branch Alignment

- Every active epic branch MUST have a corresponding epic spec
- Specs without branches are not in execution
- Execution work without a spec is invalid

---

## 10. Decision Management

- Decisions live under `docs/decisions/`
- Decisions are immutable once accepted
- Changes require a new decision document

---

## 11. Definition of Done (Mandatory)

Every **Epic spec MUST include a Definition of Done**.

The Definition of Done:
- Defines the exit condition for execution chats
- Authorizes Coding Agents to conclude work autonomously
- Prevents ambiguous or open-ended execution

Execution chats MUST:
- Validate all Definition of Done items
- Open a PR against the **correct milestone branch**
- Produce an Epic Completion Report
- Declare completion explicitly and stop

Delivery readiness includes verified commits and an explicit pull request handoff when automated PR creation is unavailable.

---

## 11.5. Human Review, Acceptance vs. Execution Completion

**Critical lifecycle distinction:** An Epic can be **execution-complete** while still requiring **human acceptance**.

### Definitions

- **Execution Completion:** All Definition of Done items are verified, code is delivered, tests pass, and the Coding Agent reports completion. This is technical correctness and delivery completeness.

- **Delivery Notice:** A structured, explicit notice produced by the Coding Agent upon execution completion. This is a mandatory artifact and a prerequisite for human review and HQ authorization. No Epic may proceed to review or closure without a Delivery Notice.

- **Human Review:** After execution completion, a human (Layer 8) conducts an independent review—testing functionality, evaluating correctness against intent, identifying design issues, or uncovering unexpected behavior.

- **Acceptance:** An explicit decision made by HQ Chat (human) regarding whether to accept, accept-with-follow-ups, or reject the completed Epic based on human review findings.

### Flow

```
Coding Agent Executes
  ↓
Coding Agent Reports: "Execution Complete"
  ↓
Human Reviews (Layer 8) in natural language
  ↓
AI Structures review into Epic Review Seal (human approval, no markdown authoring required)
  ↓
HQ Chat Makes Decision: Accept | Accept-with-Followups | Reject
  ↓
Acceptance Recorded in Completion Report
```

### Key Rules

1. **Coding Agents MUST stop after reporting execution completion.** They do NOT infer acceptance.
2. **Coding Agents MUST produce a Delivery Notice before review.** No Epic may proceed to review or closure without a Delivery Notice.
2. **Humans OWN review.** Human judgment is a first-class input, not a rubber stamp.
3. **HQ Chat OWNS acceptance decisions.** Acceptance is recorded explicitly and becomes immutable.
4. **HQ Chat MUST issue explicit delivery authorization before PR/merge.** Coding Agents must await this authorization and refuse to proceed without it.
4. **Follow-up work requires new Epics.** If human review identifies issues, new Epic(s) must be created; iteration without a new contract is prohibited.
5. **Acceptance decisions are recorded in the Epic Completion Report.** The report captures human findings, the decision, and any follow-up actions.
6. **Structured review artifacts are AI-generated.** Humans provide plain-language findings; Coding Agents or HQ Chat produce the Epic Review Seal from that input. Humans may approve or correct AI-structured text but are not required to author or edit markdown.

7. **No Epic may close with uncommitted changes.** The working tree must be clean before merge and closure.
8. **Execution stops immediately after merge.** No further actions are taken by the Coding Agent.

---

---

## 12. Epic Completion Reports (Mandatory)

Every Epic MUST conclude with an **Epic Completion Report**.

---
## 12A. Delivery Notice (Mandatory)

Every Epic MUST include a structured Delivery Notice as a prerequisite for review and closure. The Delivery Notice:
- Is produced by the Coding Agent immediately upon execution completion
- Is required before human review or HQ authorization
- Must be explicit, structured, and committed to the repository
- Is referenced in the Epic Completion Report

See `governance/templates/epic-completion-notice.md` for the canonical Delivery Notice template.

---

The Epic Completion Report:
- Is created once, at Epic completion
- Is stored alongside the Epic spec under `docs/phases/`
- Records what was delivered, verified, and deferred
- Serves as the durable closure artifact for the Epic
- **Includes the acceptance decision and human review findings** (if applicable)

Completion Reports are append-only and MUST NOT modify the original Epic spec.

---

## 13. Epic Execution Chat Starter (Mandatory)

Every Epic execution chat MUST begin with a **complete Epic Execution Chat Starter**.

The starter is a binding execution contract and MUST include:
- Mandatory Context Packet
- Explicit scope and non-goals
- Governance enforcement statement
- Definition of Done reminder
- Delivery Requirements (branch + PR target)

Execution chats that omit delivery requirements are invalid.

A canonical template is provided under:

```
governance/templates/epic-execution-chat-starter.md
```

---

## 14. Project Tracker Integration (Optional, Declarative)

Projects **may declare integrations with external project trackers** (e.g. Jira, Azure DevOps, GitHub Projects, Pivotal Tracker) via **system references**.

Such integrations:
- Are optional
- Must be explicitly declared
- Must not replace the canonical project structure

Details are defined in the Project Tracker Integration System reference.

Tracker integrations MUST be declared via a system reference under `governance/systems/` and MUST NOT be inferred from external tools or naming conventions.

---

## 15. Canonical Epic Spec Template

All Epic specs MUST follow the canonical structure defined in:

```
governance/templates/epic-spec.md
```

---

## 16. System Installation Tasks

Governance changes that affect structure or conventions require a **System Installation Task**.

Such tasks are:
- One-time
- Explicitly scoped
- Execution-only
- Delegated to a Coding Agent

---

## 17. Adoption & Evolution

- Adopted at project creation
- Enforced forward-only
- Evolution is intentional, additive, and versioned

---

## Closing Statement

This project system exists to:
- Reduce friction
- Preserve clarity
- Enable parallel work
- Support AI-native workflows

Structure is not bureaucracy.  
Structure is leverage.

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 2.0.0 | 2026-04-20 | Governance files migrated from `docs/` to `/governance/` (E6.2). Updated canonical repository structure, template paths, and system reference paths. |
| 1.5.0 | 2026-02-18 | Previous version — governance lived in `docs/`. |
