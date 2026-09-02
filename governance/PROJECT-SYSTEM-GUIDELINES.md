# PROJECT SYSTEM GUIDELINES
*(Authoritative Project Structure, Documentation, and Execution Policy)*

**Version:** 2.7.0  
**Effective Date:** 2026-09-02  
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
7. **PR and Merge**: Coding Agent opens a PR to the correct branch; the parent performs the merge after authorization (§11.6 — a child never holds merge authorization). No Epic may close with uncommitted changes or without merge.
8. **Stop**: Execution stops immediately after merge. No further actions are taken.

**No step may be skipped, inferred, or collapsed.**

**Gate scoping (§11.6 Default-Accept):** Steps 3–6 are the **Layer-8 human-review gate** and are preserved — default-accept does not remove them. The **acceptance-artifact** question within them is governed by §11.6: for a **clean** Epic (meets Definition of Done, acceptance criteria, and spec), the review acknowledgment, HQ decision, and delivery authorization are **in-chat acts** — no Review Decision artifact is produced, the **Epic Review Seal is issued only on the exception path** (reject / accept-with-follow-ups), and the review acknowledgment **names the party that reviewed and accepted** (role + session identity) — silence accepts nothing (§11.6). Explicit authorization before merge (Step 6) still applies; it is an in-chat act, not an artifact.

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
- **Phase branches** merge to **`master`** (or the project's mainline) — Phase closure, per the canonical sequence in **§5C**

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

## 5C. Phase Closure

Phase closure is the process of consolidating a completed phase's work into `master` and formally delivering the phase — **README update, version bump, and git tag included** — as one canonical, mandatory sequence. The delivery steps are automatic parts of closure itself: **no out-of-band Steering Note is required to close a phase.**

### Phase Closure vs. Completion

**Two distinct states:**

- **Phase complete:** All planned Milestones for the phase are executed, accepted, and fully closed (§5B) into the phase branch. All phase completion criteria (from the phase spec) are satisfied.

- **Phase fully closed (delivered):** Phase complete AND consolidated into `master` via merged PR AND the mandatory delivery steps executed — README updated, version bumped, closure commit tagged — AND the phase-closure declaration recorded.

**A phase can be "complete" without being "fully closed."** Full closure requires consolidation **and** the delivery steps.

---

### 9-Step Phase Closure Process

Phase closure follows a structured process parallel to Epic closure (§1A) and Milestone closure (§5B), one level up:

**Step 1: All Milestones Fully Closed**
- All planned Milestones for the phase are executed, accepted, and consolidated into `phase/P<id>` per §5B
- Phase branch contains all phase work
- Working tree clean — **uncommitted work blocks closure** (as at §5B)

**Step 2: Phase Declared Complete**
- Phase completion criteria (from the phase spec) are evaluated and each verified satisfied
- "Phase P<id> complete" declared with a verification checklist and phase summary

**Step 3: README Update (Mandatory, Automatic)**
- Top-level `README.md` is updated **on the phase branch** to the delivered state: status banners, test counts, version references, capability summary
- Stale claims MUST be retired here — this step exists so `master` never advertises a previous phase's numbers

**Step 4: Version Bump (Mandatory, Automatic)**
- The project version is bumped **on the phase branch** per the project's versioning scheme (phase closure is typically a major bump — e.g., P5 closed as `v5.0.0`)
- Every place the version is recorded (README, config, manifest) agrees

**Step 5: Consolidation PR Created**
- Create Pull Request: `phase/P<id>` → `master` (or the project's mainline — `main`/`develop` per project configuration)
- PR title: "Phase P<id>: <Phase Name>"
- PR description includes the phase summary and Milestone list
- The PR carries the README and version updates from Steps 3–4 — delivery travels through the governed promotion path, not as direct commits to `master`

**Step 6: Delivery Reviewed**
- Closure is recorded under the operating acceptance model, **SN-13 default-accept**: a clean delivery (all completion criteria met) is accepted by an acknowledgment that names the party that reviewed and accepted — silence accepts nothing; a **Review Decision** artifact is the exception path only
- *(Stated by reference only — the acceptance model's normative text is §11.6 "Default-Accept (SN-13)", not this section)*

**Step 7: Merge Completes**
- PR merged; the merge commit becomes the **phase closure commit** on `master`

**Step 8: Git Tag (Mandatory, Automatic)**
- The closure commit is tagged with the version from Step 4 (e.g., `v6.0.0`) and the tag is pushed
- The tag is the durable, discoverable marker of the phase delivery on `master`

**Step 9: Phase-Closure Declaration Recorded**
- `docs/phases/P<id>__<Phase_Name>/P<id>__phase-closure-declaration.md` committed to `master` (the record post-dates the closure commit it describes), using `governance/templates/phase-closure-declaration.md`
- Records merge commit, tag, `master` head at closure, closure date, closed-by, and acceptance model
- "Phase P<id> fully closed" declared — the phase is **delivered**
- The next phase branch (`phase/P<next-id>`), if any, is created from `master` after the merge

**No step may be skipped, inferred, or collapsed.** Steps 3, 4, and 8 (README update, version bump, git tag) are mandatory automatic steps of the sequence itself — **no out-of-band Steering Note is required to trigger them.**

---

### Phase Closure Authority

- **Phase Chat** prepares the delivery (Steps 3–5) and executes consolidation, tagging, and the declaration (Steps 7–9)
- **HQ Chat** is the acceptance authority (Step 6) under the operating acceptance model
- **Coding Agents** do NOT close phases (authority parallels §5B: closure belongs to the levels above the work)

---

### Applicability

This sequence governs phase closures from P6 forward. Earlier phases (P2–P5) closed by out-of-band Steering Note before this section existed; their hand-made declarations stand as history and are not re-closed.

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
- Produce a Delivery Notice
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
AI Structures review into Epic Review Seal — exception path only (human approval, no markdown authoring required)
  ↓
HQ Chat Makes Decision: Accept | Accept-with-Followups | Reject
  ↓
Acceptance Recorded per §11.6 Default-Accept:
  clean → accepted by acknowledgment naming the party that reviewed
          (merge + in-chat acknowledgment; no artifact; silence accepts nothing)
  not clean → Review Decision records the exception
```

### Key Rules

1. **Coding Agents MUST stop after reporting execution completion.** They do NOT infer acceptance.
2. **Coding Agents MUST produce a Delivery Notice before review.** No Epic may proceed to review or closure without a Delivery Notice.
3. **Humans OWN review.** Human judgment is a first-class input, not a rubber stamp.
4. **HQ Chat OWNS acceptance decisions.** A clean delivery is accepted by an acknowledgment that names the party that reviewed and accepted per §11.6 — the merge plus the in-chat acknowledgment is the acceptance record, and silence accepts nothing; a Review Decision, when issued on the exception path, is immutable.
5. **HQ Chat MUST issue explicit delivery authorization before PR/merge.** Coding Agents must await this authorization and refuse to merge without it — the parent performs the merge (§11.6). The authorization is an in-chat act; it produces no artifact on the happy path.
6. **Follow-up work requires new Epics.** If human review identifies issues, new Epic(s) must be created; iteration without a new contract is prohibited.
7. **Exception-path decisions are recorded in the Review Decision** (and Epic Review Seal): human findings, the reject / accept-with-follow-ups decision, and any follow-up actions. A clean delivery produces no Review Decision — see §11.6.
8. **Structured review artifacts are AI-generated.** Humans provide plain-language findings; Coding Agents or HQ Chat produce the Epic Review Seal from that input. Humans may approve or correct AI-structured text but are not required to author or edit markdown.
9. **No Epic may close with uncommitted changes.** The working tree must be clean before merge and closure.
10. **Execution stops immediately after the merge.** No further actions are taken by the Coding Agent; the merge itself is performed by the parent (§11.6).

---

## 11.6. Default-Accept (SN-13)

The **normative acceptance model** at every **parent-chat → child gate**: Phase Chat accepts a clean Milestone; Milestone Chat accepts a clean Epic; HQ Chat accepts a clean Phase.

### The Model

- **Happy path (default-accept):** a parent chat accepts a **clean** child delivery — one meeting its Definition of Done, acceptance criteria, and spec. No Review Decision artifact is produced; the **parent's merge plus an in-chat acknowledgment that names the party that reviewed and accepted is the acceptance record**. The acknowledgment is a **positive signal an identified party emitted** — it carries the **role and session identity** of the party that reviewed the delivery and accepted it, so *reviewed and clean* is distinguishable from *nobody looked* **from the record alone**, and a duplicated role leaves two signals rather than two indistinguishable silences. **Silence accepts nothing**: an absent acknowledgment is nobody's acceptance, never a role's. A clean delivery still produces **no new artifact** — the signal rides the acknowledgment that already exists (E43.2, P12-M43).
- **Exception path:** a **Review Decision** (and, at Epic level, the **Epic Review Seal**) is issued **only when a delivery is not clean** — to reject it or to accept it with follow-up Epic(s). A Review Decision, once issued, is immutable.
- **The parent performs the merge.** At the Phase→Milestone and Milestone→Epic gates, the merge of a child's branch is performed by the **parent** that accepted the delivery — a child never holds merge authorization. A Merge Authorization is the **parent's own record of an act it performed**, never an instruction issued to a child (E43.1, P12-M43). The bypass class `P9-GH-1` / `P10-GH-9` record is structurally unavailable, not merely discouraged.

### What Default-Accept Governs

Exactly two questions:

1. Whether the parent chat must produce an **acceptance artifact** for a clean child delivery — no. The acknowledgment — an in-chat act that names the party that reviewed and accepted — is the acceptance, and it is not an artifact.
2. Whether a **Review Decision** is mandatory on the happy path — no; the Review Decision is the exception path only.

### What Is Preserved — Two Gates, Not One

Default-accept does **not** remove the human from the loop. Two distinct gates exist and MUST NOT be collapsed:

- **(A) Layer-8 human review — preserved.** The human's independent review (§11.5 "Human Review"; "Humans OWN review") remains available and authoritative wherever the framework mandates it, and human-confirmation requirements (e.g., a human-authorized merge on an Epic PR) stand. Human judgment is a first-class input, not a rubber stamp.
- **(B) Parent-chat → child acceptance artifact — default-accept.** No acceptance artifact is produced for a clean delivery; the acknowledgment, naming the party that reviewed and accepted, carries the acceptance. **Silence accepts nothing** — acceptance is an emission by an identified party; a Review Decision is issued only on the exception path.

Default-accept removes the *mandatory Review Decision artifact on the happy path*, not the *human's review*, and not the *identity of the reviewer* — the acknowledgment names who reviewed.

### What the Signal Does Not Claim

The acknowledgment distinguishes **review-happened** from **nobody-looked**. It does **not** make the review **good**: an acceptance by a named party is evidence that the party reviewed the delivery; it is not a verdict on the quality of that review. *"A review happened"* is not *"the review was correct"* — the boundary is stated, not implied, so the acceptance model cannot be read to install the confidence-without-grounding E39.3 recorded (E43.2, P12-M43).

### Where the Acknowledgment Is Recorded

The acknowledgment names the party that reviewed and accepted (role + session identity) and is recorded **with the parent's merge** of the child's branch — the parent records its own act (E43.1). The committed record alone therefore carries the attribution: a reader can tell, from the record, that a review happened — not merely that a merge did. No separate object is produced on the happy path.

> **History:** SN-13 (P5) established this model; it has governed every delivery since P5. The Review Decision and Epic Review Seal artifacts themselves are unchanged — default-accept changes *when* they are issued, not *what* they are. Codified by E25.2 (P6-M25); closes **`P6-GH-10`** — *"formally codify SN-13 default-accept into AOG, PSG and the Execution Chat Starter templates"*, filed in P5's closure declaration and forward-allocated to P6. **The resolution rests on the `(P6-M25)` / E25.2 anchor, not on this sentence's two P5 anchors**, which point at the unrelated `P5-GH-10`. Cited in full form per `governance/systems/creation-chat-guide.md` §Artifact ID Citation Forms.

### The Rework Limit

The rework limit is the **single mechanism that bounds rework loops**, and it is stated once, here. At every parent-chat → child gate, a parent chat may reject a child's delivery a **maximum of 3 attempts**. If a third Completion Notice is still not acceptable, the parent does **not** issue a fourth rejection-and-retry; the child produces an **Escalation Notice** and the parent escalates to its own parent (at the Milestone→Epic gate, the Phase Chat). **Silent fourth attempts are a governance violation.**

**A written extension grants exactly ONE further attempt — not a reset to three.** A written
extension is an explicit grant recorded as an artifact or a recorded decision (for example, the
CFO's recorded act of resolving a blocker in the escalation chat, SN-36/37). It adds one attempt to
the budget; it does not restore the budget. **Rework is exhausted** when the 3-attempt maximum plus
any written `+1` has been spent without an acceptable delivery — the state the rework-exhaustion
flip (E43.4, P12-M43) triggers on.

> **History:** previously the rule lived only in `governance/systems/milestone-execution-chat-starter.md` (with a contradictory extension semantics — "resets") and in **no** normative document. E43.3 (P12-M43) consolidated the two statements into this one normative statement and routed every starter-shaped surface to it by carry or cite. Closes **`P12-GH-1`**.

### The Rework-Exhaustion Flip

**Exhausted rework flips the receiving parent to manual.** When a parent chat's rework limit is
exhausted — the 3-attempt maximum plus any written `+1`, spent without an acceptable delivery (the
definition above) — the **receiving parent flips to manual Execution Mode**. This is the system's
**first fail-closed default**, and the counterweight to the phase's organising finding: agentic
Execution Mode is defined by *no human being present*, and a rework loop is exactly where a human
needs to be. The flip puts a human in the loop for the escalation rather than leaving an unattended
parent to keep reworking.

**Opt-out, on by default.** The flip is governed by the `rework_exhaustion_flip` key in
`.ai-project.yml` (`governance/ai-project-yml-spec.md` §3.8): **`enabled` by default**, `disabled`
only deliberately. A project that disables it has explicitly declined the fail-closed default;
the flip itself is never made mandatory (SN-31 Decision 5).

**Drivr performs the flip and records it.** The flip is performed and recorded by **Drivr** — not
by mutating the receiving parent's committed Execution Chat Starter. The committed starter remains
the source of truth for the instance's declared Execution Mode (`chat-hierarchy.md`, "Declaration
mechanism"); a runtime flip that rewrote the committed file would break that invariant. The flip is
**discoverable from the record** Drivr writes, never from a rewritten committed file — the
difference between a fail-closed default and a race condition (E43.4, P12-M43). The way back —
**resume** — restores the declared mode and never promotes manual → agentic, and returns the mode,
never the budget (`chat-hierarchy.md`, "Resume").

### 11.6.1 HQ-Authored Deliveries — No Parent, Therefore No Default-Accept

Default-accept is defined above at the **parent-chat → child gate**, and it names three: Phase accepts Milestone, Milestone accepts Epic, HQ accepts Phase. **HQ's own output has no row in that list, because HQ has no parent chat.**

This section closes that gap. It governs any delivery **authored by HQ Chat itself** — rulings, progress digests, errata, and any governance edit HQ applies directly under a recorded exception.

**Default-accept MUST NOT be applied to an HQ-authored delivery. Silence is never acceptance here.**

The reason is structural, not a matter of caution. Default-accept is safe *because a parent chat reviews* — silence stands in for a review that actually happened at the level above. Above HQ there is no such level: the **Creation Chat holds no governance authority** (Seed Rule 3) and therefore cannot be the reviewer, and no other chat sits higher. Applying default-accept to HQ output would mean silence standing in for a review that never occurred and could not occur.

**The designated reviewer for HQ-authored deliveries is Layer-8 (the CFO), and the review is a diff review.**

- **Authorization is not review.** "You may merge this" is authorization; "I have read the change and it matches the expectation" is review. §11.6's two-gate framing already distinguishes them — gate (A) Layer-8 human review, gate (B) the acceptance artifact. For this one class, **gate (A) is mandatory rather than merely available**, and gate (B) does not apply at all.
- **An HQ-authored PR merges only after the CFO has reviewed the diff and said so.** `cfo_review_gate` (`.ai-project.yml`; see `governance/systems/creation-chat-guide.md` "CFO PR Review Gate") remains the mechanism; this section makes the gate non-optional for this class regardless of that toggle's setting.
- **HQ MUST NOT merge its own delivery on authorization alone**, and MUST state plainly in any such PR that HQ authored it and no chat-level reviewer exists for it.

**Relationship to P9-GH-1 / P10-GH-9 — stated so this is not misread as closing them.** Those record the same authority class seen from the *child* side: a child chat taking merge authorization directly and bypassing its parent's Stage-2 review, with the Milestone and Phase starter templates still unpatched. This section addresses the *top* of the chain, where the problem is not a bypassed parent but the absence of one. **It closes neither.** The two are complementary halves of the same concern and both remain open.

> **History:** Established by CFO direction, 2026-07-31 — *"I am that reviewer for you… this is the spot where it's worth I am the bottleneck."* Prompted by two HQ-authored PRs (#165, #166) merged on direct authorization with no independent reviewer, a fact recorded in both merge bodies at the time rather than normalized silently.

---

## 12. Delivery Notice (Mandatory)

Every Epic MUST conclude with a structured **Delivery Notice**, produced by the Coding Agent upon execution completion. It is a prerequisite for review and closure — no Epic may proceed to review or closure without one.

The Delivery Notice:
- Is produced by the Coding Agent immediately upon execution completion
- Is required before human review or HQ authorization
- Must be explicit, structured, and committed to the repository
- Is created once, at Epic completion, and stored alongside the Epic spec under `docs/phases/`
- Records what was delivered, verified, and deferred
- Serves as the durable closure artifact for the Epic

Delivery Notices are append-only and MUST NOT modify the original Epic spec.

On the **exception path**, the acceptance decision and human review findings are recorded separately in the **Review Decision** (and **Epic Review Seal**), not in the Delivery Notice; a clean delivery is accepted by an acknowledgment that names the party that reviewed and accepted and produces no Review Decision — see §11.5 and §11.6.

See `governance/templates/delivery-notice.md` for the canonical template.

---

## 13A. Phase Execution Chat Starter (Mandatory)

Every Phase execution session MUST begin with a **complete Phase Execution Chat Starter**.

The Phase Execution Chat Starter is a binding execution contract that defines:
- Phase goals and scope
- Complete list of Milestones to be planned
- Governance versions in use
- Phase Execution Chat responsibilities and constraints
- Session lifecycle and completion criteria

A Phase Execution Chat (autonomous execution and delivery agent scoped to a single Phase) is launched by HQ Chat using this artifact. In Stage 1 it produces Milestone specs and Milestone Execution Chat Starters, commits them to a phase branch, and opens a PR. In Stage 2 it oversees Milestone delivery — accepting clean Milestone deliveries by an acknowledgment that names the party that reviewed and accepted (§11.6 — silence accepts nothing) and issuing a Review Decision only on the exception path (§11.6) — and merges the phase branch when all Milestones are accepted.

**Phase Execution Chat role:** Execution and delivery agent for this Phase. It commits and PRs its deliverables and oversees delivery through to merge — it does not merely converse. See AI-OPERATING-GUIDELINES.md §3.6 for full role definition.

For full role and responsibility definitions, see:

- **Agent definition:** `governance/agents/governance.agent.md` (Phase mode)
- **Fillable template:** `governance/templates/phase-execution-chat-starter.md`
- **Hierarchy reference:** `governance/systems/chat-hierarchy.md` (Level 2)

---

## 13B. Milestone Execution Chat Starter (Mandatory)

Every Milestone execution session MUST begin with a **complete Milestone Execution Chat Starter**.

The Milestone Execution Chat Starter is a binding execution contract that defines:
- Milestone goals and scope
- Complete list of Epics to be planned
- Governance versions in use
- Milestone Execution Chat responsibilities and constraints
- Session lifecycle and completion criteria

A Milestone Execution Chat (autonomous execution and delivery agent scoped to a single Milestone) is launched by Phase Execution Chat (or HQ Chat during bootstrap) using this artifact. In Stage 1 it produces Epic specs and Epic Execution Chat Starters, commits them to a milestone branch, and opens a PR. In Stage 2 it oversees Epic delivery — accepting clean Epic deliveries by an acknowledgment that names the party that reviewed and accepted (§11.6 — silence accepts nothing) and issuing a Review Decision only on the exception path (§11.6), and performing the merge of each accepted Epic's branch as the parent — and the **Phase Execution Chat performs the merge of the milestone branch** when all Epics are accepted (§11.6 — the parent performs the merge of a child's branch).

**Milestone Execution Chat role:** Execution and delivery agent for this Milestone. It commits and PRs its deliverables and oversees delivery through to merge — it does not merely converse. See AI-OPERATING-GUIDELINES.md §3.7 for full role definition.

For full role and responsibility definitions, see:

- **Agent definition:** `governance/agents/governance.agent.md` (Milestone mode)
- **Fillable template:** `governance/templates/milestone-execution-chat-starter.md`
- **Hierarchy reference:** `governance/systems/chat-hierarchy.md` (Level 3)

---

## 13C. Epic Execution Chat Starter (Mandatory)

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

## 13D. Hierarchical Communication Protocol (Mandatory)

Information moves through the chat hierarchy in two directions, each with exactly one
sanctioned channel.

- **Upward communication is 1-to-1.** Every level has exactly one parent. Escalations and
  completion notices travel up one level — Epic → Milestone → Phase → HQ — and the receiving
  level decides whether to absorb the issue or escalate it further. No level skips its parent
  to reach a grandparent.
- **Downward communication is the spec file, not broadcasting.** A parent communicates a
  directive, amendment, or correction by amending its own spec file; children — including
  those already mid-execution — read from that same source at any time. One write, many
  readers; no separate message per child.
- **The level spec file is dual-role:** a planning artifact (what was planned) and a live
  contract (the authoritative state of scope, constraints, and directives, including
  amendments).
- **Mid-flight updates escalate UP.** If a directive changes after child sessions are running,
  the parent amends the spec and, if the change is blocking, escalates up to its own parent to
  decide whether to pause or cancel affected children. Reaching downward into a running child
  session is prohibited.

This is the SN-12b binding decision (Creation Chat Steering Note, 2026-06-25). For the full
protocol and worked guidance see the **"Communication Protocol"** section of
`governance/systems/chat-hierarchy.md` and AI-OPERATING-GUIDELINES.md §3.10. The Phase and
Milestone Execution Chat Starter templates carry the amendment-issuing guidance for their
levels.

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

## 14A. `.ai-project.yml` — Required Project Configuration Artifact

Every project using the AI Project System MUST have a `.ai-project.yml` file at its repository root. This file is the **project configuration contract**: it declares the governance source, the pinned governance version, and optional project-specific overrides.

`.ai-project.yml` is required before any HQ agent session or `ai-project init` scaffolding. It is the foundation for governance discovery (M8), CLI scaffolding (M7), and the override system (M9).

### Required fields

- `governance.source` — URL or relative path to the governance source repository
- `governance.version` — Pinned governance version (semver string, quoted)
- `governance.ref` — Git ref (tag, branch, or SHA) on the governance source
- `project.name` — Project slug identifier
- `project.description` — Short project description

### Canonical specification

Full field definitions, validation rules, HQ agent usage, and CLI scaffolding behavior are documented in:

```
governance/ai-project-yml-spec.md
```

---

## 14B. Git Submodule Setup — External Project Reference Procedure

External projects reference this governance package via git submodule. The canonical procedure for adding, pinning, updating, and cloning governance via submodule is documented in:

```
governance/submodule-setup.md
```

Key conventions:
- The submodule MUST be installed at `.governance/` (hidden folder)
- `governance.source` in `.ai-project.yml` corresponds to the submodule remote URL
- `governance.ref` in `.ai-project.yml` corresponds to the checked-out ref inside `.governance/`

---

## 14C. Override System

The override system allows projects to customize select governance conventions without forking the governance source. Overrides are declared in the `.ai-project.yml` `overrides` block and affect how the HQ agent generates branches, artifacts, and planning documents.

Override resolution follows a strict precedence hierarchy. Core governance dimensions are immutable and cannot be overridden.

### Override Precedence Hierarchy

Override values are resolved using a three-level hierarchy. When a value is requested, the system checks each level in order and uses the first value found:

| Level | Source | Authority | When It Applies |
|-------|--------|-----------|-----------------|
| 1 (highest) | Local project convention | Documented in `docs/decisions/` | Rare — used only for exceptional circumstances requiring deviation beyond `.ai-project.yml` overrides. Must be explicitly documented in a decision record. |
| 2 (medium) | `.ai-project.yml` overrides | Declared in `overrides` block | Standard customization mechanism. Takes effect when the HQ agent reads the file at startup. |
| 3 (lowest) | Governance defaults | Defined in this document (`PROJECT-SYSTEM-GUIDELINES.md`) | Baseline. Applies when no override is present at Level 1 or Level 2. |

**Resolution rule:** When a conflict exists, the highest-level source wins. If no override exists at a given level, the next level down applies.

#### Precedence Resolution Example

| Scenario | Local Decision | `.ai-project.yml` Override | Governance Default | Result |
|----------|---------------|---------------------------|-------------------|--------|
| No overrides set | None | None | `epic_prefix: epic/` | `epic/` (Level 3) |
| Only `.ai-project.yml` override | None | `epic_prefix: feature/` | `epic_prefix: epic/` | `feature/` (Level 2) |
| Full override stack | `epic_prefix: custom/` | `epic_prefix: feature/` | `epic_prefix: epic/` | `custom/` (Level 1) |
| Partial stack (Level 1 silent) | `branch_strategy: gitflow` (in decision) | `merge_strategy: squash` | `branch_strategy: trunk-based`, `merge_strategy: merge` | `branch_strategy: gitflow`, `merge_strategy: squash` |

### Overridable Fields

The following governance dimensions may be customized via `.ai-project.yml` overrides:

- **Branch naming strategy** (`overrides.branch_strategy`): Choose between `trunk-based` and `gitflow` conventions
- **Merge strategy** (`overrides.merge_strategy`): Choose default PR merge method (`merge`, `squash`, or `rebase`)
- **Epic branch prefix** (`overrides.epic_prefix`): Customize the prefix for epic branch names (e.g., `feature/`, `topic/`)

Full field definitions, constraints, and allowed values are documented in:
```
governance/ai-project-yml-spec.md
```
See Section 3.3 — Optional Fields (`overrides`).

### Core (Non-Overridable) Governance Dimensions

The following governance dimensions are **immutable** and **cannot be altered** by any override mechanism. Attempting to override these dimensions (via `.ai-project.yml`, local decisions, or any other mechanism) is invalid.

| Dimension | Why It Is Non-Overridable | Consequence of Allowing Overrides |
|-----------|--------------------------|-----------------------------------|
| **Canonical happy path** (8 steps: execution → delivery notice → human review → epic review seal → HQ decision → HQ authorization → PR & merge → stop) | The happy path is the foundational execution contract. Every Epic must follow it. Skipping or reordering steps breaks the governance model. | Epics would skip review or merge without authorization, breaking the audit trail and authority hierarchy. |
| **Authority hierarchy** (HQ Chat → Phase Chat → Milestone Chat → Coding Agent) | Establishes clear decision boundaries. Restructuring would create ambiguity about who decides what. | Unclear ownership of decisions, conflicting instructions, loss of accountability. |
| **Epic lifecycle** (spec → execute → deliver → review → accept → merge) | The lifecycle guarantees that every Epic has a spec before execution, delivery before review, and acceptance before merge. | Epics could be executed without specs, merged without review, or accepted without explicit authorization. |
| **Definition of DoD requirements** | DoD is the minimum bar for completion. Reducing DoD scope undermines quality. | Epics could declare completion without meeting all requirements. |
| **Documentation front-matter conventions** | Front-matter is how the system mechanically derives execution context. Changing the format would break tooling. | Tooling (HQ agent, CLI) could not parse artifacts; context would not be derivable. |
| **Branch hierarchy** (`epic/*` → `milestone/*` → `phase/*`) | The hierarchy enforces promotion discipline. Branches must follow this structure to maintain traceability. | Branches could merge in any order, skipping hierarchy levels, breaking the audit trail. (Note: **prefixes** are overridable via `epic_prefix` — the structural hierarchy itself is not.) |

### Adding Overrides to a Project

To add overrides to an existing project:

1. Create or edit `.ai-project.yml` at the repository root
2. Add an `overrides` block with the desired fields
3. Validate the file against the rules in `governance/ai-project-yml-spec.md` Section 4
4. Commit and push the change
5. The HQ agent reads and applies overrides on next startup

**Example `.ai-project.yml` with overrides:**

```yaml
governance:
  source: https://github.com/panchew/ai-project-system
  version: "3.0.0"
  ref: v3.0.0

project:
  name: acme-payments
  description: "Payment processing service for ACME Corp"

overrides:
  branch_strategy: gitflow
  merge_strategy: squash
  epic_prefix: feature/
```

### Validation

Override values are validated when the HQ agent reads `.ai-project.yml`:

- Unknown override keys produce a warning and are ignored
- Invalid values for known keys produce an error and prevent agent startup
- The `overrides` block must be valid YAML
- No override values are required — the block is fully optional

See `governance/ai-project-yml-spec.md` Section 4 for the complete validation rule set.

### Override Boundaries

The formal Override Boundaries document enumerates all overridable and non-overridable governance dimensions with detailed rationale, constraints, and examples. It is the authoritative reference for understanding which governance dimensions may be customized.

```
governance/override-boundaries.md
```

The Override Boundaries document is a companion to this section. It provides per-dimension detail that is summarized here.

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

## 18. Unattended Cluster Execution Rules (Optional, Agentic)

Projects may declare autonomous execution loops by enabling `"unattended_cluster": true` under `.ai-project.yml`.

### 18A. File-Driven Communication
All agent-to-agent communication inside the cluster MUST proceed via JSON/YAML files under `.ai-project/queue/`. No agent may initiate direct memory-sharing or network communication outside the repository bounds.

### 18B. The Recursion Limit
The local orchestrator loop is strictly bounded to three (3) compilation/test execution attempts per Epic. If validation fails on the third attempt, the loop MUST freeze the branch, produce a structured markdown escalation report under `docs/admin/`, and suspend execution until a Human Director unblocks it.

### 18C. Strict Sandbox Isolation
All code implementation (Epic execution) and validation (QA runs) MUST execute within ephemeral, volume-mounted containers (such as Docker) to prevent host filesystem contamination, security vulnerabilities, or package installation drift.

### 18D. Hybrid Model Routing (Token Optimization)
To optimize the intelligence-to-token-spend ratio during unattended operations:
- **Strategic Roles (HQ, Phase, Milestone Mode):** Planning, requirement modeling, and architecture mapping MUST use premium, remote models (e.g. `remote:gpt-4o`, `remote:claude-3-5-sonnet`) to ensure rigorous compliance with constraints and structural preservation.
- **Implementation & Assurance Roles (Developer, QA Tester Mode):** High-frequency tasks like code implementation, file editing, test execution, and linter debugging SHOULD use local or low-cost models (e.g. `local:llama3`, `local:qwen2.5-coder`) to manage operational expenses while keeping code execution secure.

All model assignments MUST be explicitly declared in the `.ai-project.yml` configuration under the `models` block.

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
|---------|------|--------|
| 2.7.0 | 2026-09-02 | **The rework-exhaustion flip, stated normatively (E43.4, P12-M43).** Added §11.6 "The Rework-Exhaustion Flip", the one normative statement of the system's **first fail-closed default**: **exhausted rework** (the 3-attempt maximum plus any written `+1`, spent without an acceptable delivery — the definition in "The Rework Limit" above) **flips the receiving parent to manual Execution Mode**. **Opt-out, on by default** — governed by the new `rework_exhaustion_flip` key in `.ai-project.yml` (`ai-project-yml-spec.md` §3.8), `enabled` by default, `disabled` only deliberately. **Drivr performs the flip and records it** — the committed Execution Chat Starter is not mutated, so the committed-starter invariant survives and the flip is discoverable from the record; **resume** restores the declared mode, never promotes manual → agentic, and returns the mode, not the budget (both stated at `chat-hierarchy.md`). The trigger definition and the `+1` semantics are unchanged (E43.3). No gate, authority, or §11.6.1 rule changed. |
| 2.6.0 | 2026-09-02 | **The rework limit, as one normative statement (E43.3, P12-M43; closes `P12-GH-1`).** Added §11.6 "The Rework Limit": at every parent-chat → child gate a parent may reject a child's delivery a **maximum of three (3) attempts**; on a third still-unacceptable Completion Notice the parent issues no fourth rejection-and-retry, the child produces an **Escalation Notice**, and the parent escalates. **A written extension grants exactly ONE further attempt, not a reset to three** (SN-36/37, CFO-decided, stricter than the earlier "resets" wording — the surviving semantics). Defines **rework exhaustion** (3 attempts + any written +1, without an acceptable delivery) as the state E43.4's flip triggers on. The rule was previously in exactly one starter surface (`systems/milestone-execution-chat-starter.md`), absent from every template and the normative tier, and carried two contradictory extension semantics; it is now stated once here, and every starter-shaped surface reaches it by carry or cite. |
| 2.5.0 | 2026-09-02 | **Acceptance distinguishable from absence (E43.2, P12-M43).** The acceptance record now carries a **positive, attributable signal**: the happy-path acknowledgment **names the party that reviewed and accepted** (role + session identity) — an emission by an identified party, never an absence attributed to a role — so *reviewed and clean* is distinguishable from *nobody looked* **from the record alone**, and a duplicated role leaves two signals rather than two indistinguishable silences. **Silence accepts nothing.** Default-accept is tweaked, not retired: a clean delivery still produces **no new artifact** — the signal rides the acknowledgment that already exists, recorded with the parent's merge (E43.1). Added §11.6 subsections "What the Signal Does Not Claim" (review-happened ≠ review-correct; E39.3's overclaim refused) and "Where the Acknowledgment Is Recorded". Amended the always-restate surfaces that said "accepted by silence": §1A gate-scoping, §5C Step 6, §11.5 flow + Key Rule 4, §12, §13A, §13B, and §11.6 "What Default-Accept Governs" + gate (B). §11.6.1 (HQ-authored deliveries) is deliberately unchanged. |
| 2.4.1 | 2026-09-02 | **The parent performs the merge (E43.1, P12-M43).** Added the one normative statement to §11.6 "The Model": at the Phase→Milestone and Milestone→Epic gates the **parent** performs the merge of a child's branch, so **a child never holds merge authorization** and a Merge Authorization is the parent's own record of an act it performed, not an instruction to a child. The bypass class `P9-GH-1`/`P10-GH-9` record is structurally unavailable, not merely discouraged. Amended the happy-path acceptance record to *"the parent's merge plus the in-chat acknowledgment"*. Corrected every statement that instructed a child to merge its own branch: §1A step 7, §11.5 Key Rules 5 and 10, §13B (the Phase Execution Chat now performs the merge of the milestone branch; the Milestone Chat performs epic-branch merges as the parent). §11.6.1 (HQ-authored deliveries, CFO diff review) is deliberately unchanged. |
| 2.4.0 | 2026-07-31 | Added **§11.6.1 "HQ-Authored Deliveries — No Parent, Therefore No Default-Accept."** §11.6 defines default-accept at the parent-chat → child gate and names three (Phase↔Milestone, Milestone↔Epic, HQ↔Phase); **HQ's own output had no row, because HQ has no parent chat.** Default-accept is safe *because a parent reviews* — silence stands in for a review that happened one level up. Above HQ no such level exists: the Creation Chat holds no governance authority (Seed Rule 3) and cannot be the reviewer. So default-accept MUST NOT apply to HQ-authored deliveries (rulings, digests, errata, direct governance edits), silence is never acceptance there, **Layer-8/the CFO is the designated reviewer, and the review is a diff review** — authorization ("you may merge") is explicitly distinguished from review ("I read it and it matches"). §11.6's gate (A) becomes mandatory for this one class; gate (B) does not apply. HQ MUST NOT merge its own delivery on authorization alone and MUST state in the PR that no chat-level reviewer exists for it. Explicitly does **not** close P9-GH-1 or P10-GH-9, which record the same authority class from the child side (bypassed parent) rather than the top (absent parent). No existing rule changed; §11.6's model for the three parent→child gates is untouched. Established by CFO direction 2026-07-31 after PRs #165/#166 merged with no independent reviewer. |
| 2.3.0 | 2026-07-02 | Added §11.6 "Default-Accept (SN-13)": the normative acceptance model at every parent-chat → child gate — **happy path** = a clean delivery (Definition of Done + acceptance criteria + spec) is accepted **by silence**, no Review Decision artifact, the merge + in-chat acknowledgment is the acceptance record; **exception path** = a Review Decision (and Epic-level Epic Review Seal) is issued only when a delivery is not clean. Two-gate framing made explicit: **Layer-8 human review preserved** (§11.5 "Human Review" and "Humans OWN review" stand); only the acceptance-artifact question changes. Reconciled the always-review surfaces: §11.5 flow last step + Key Rules (duplicate rule numbering also fixed — rules now 1–10), §12 exception-path sentence, §13A/§13B "issues … Review Decisions" clauses, §1A gate-scoping note (human-review steps preserved verbatim); wired §5C Step 6's by-reference pointer to §11.6. Codifies SN-13 (P5); fixes P6-GH-10; E25.2 (P6-M25). |
| 2.2.0 | 2026-07-02 | Added §5C "Phase Closure": canonical, mandatory phase-closure sequence mirroring §1A/§5B — an ordered 9-step process with **README update, version bump, and git tag as mandatory automatic steps** (no out-of-band Steering Note required to close a phase); "phase complete vs. fully closed (delivered)" distinction; consolidation target `phase/P<id>` → `master`; phase-closure declaration as the recorded output, formalized as `governance/templates/phase-closure-declaration.md`. Reconciled the §5B consolidation-rules line that called phase closure "future work" to point at §5C. Closure acceptance stated by reference to SN-13 default-accept only (normative codification is E25.2). Applies P6 forward. Fixes P6-GH-12; E25.1 (P6-M25). |
| 2.1.0 | 2026-06-23 | Renamed §13A "Phase Planning Chat Starter" and §13B "Milestone Planning Chat Starter" (removed "Execution" misnomer). Added Phase/Milestone Chat role summaries to §13A/13B with references to AI-OPERATING-GUIDELINES.md §3.6–3.7. Removed duplicate §13A section. Fixes P5-GH-7: "Execution" terminology was being copied into Phase/Milestone starters, causing generated starters to carry Epic-level rules. |
| 3.0.0 | 2026-05-22 | Phase P3: Agentic Execution Model Maturity. Added Section 18 defining rules for 24/7 unattended development clusters, Docker sandboxing, and file-driven Dev-QA recursion queues. |
| 2.0.0 | 2026-04-20 | Governance files migrated from `docs/` to `/governance/` (E6.2). Updated canonical repository structure, template paths, and system reference paths. |
| 1.5.0 | 2026-02-18 | Previous version — governance lived in `docs/`. |
