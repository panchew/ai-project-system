# Quick Start Guide

**Get started with the AI Project System in 30 minutes.**

This guide walks you through creating your first Phase, Milestone, and Epic—from initialization to closure. By the end, you'll understand the system through practice, not just theory.

> **Two execution modes available:** This guide teaches **manual mode** (copy-paste Chat Starters — no infrastructure needed).  
> The system also supports **agentic mode** (file-driven autonomous cluster with Docker and daemon).  
> See [`README.md`](../../README.md) for the agentic mode overview, or jump directly to the tools:  
> `bin/ai-project-orchestrator`, `bin/ai-project-daemon`, `Dockerfile.sandbox`, `bin/verify-loop.sh`.  
> When using the daemon from a submodule consumer project, pass `--project-root .`:  
> `.governance/bin/ai-project-daemon --project-root . start`.

---

## What is the AI Project System?

The AI Project System is a **documentation-driven governance framework** for executing software projects with AI assistance.

**The Problem It Solves:**
- AI agents lose context across conversations
- Project scope expands without control
- Work quality varies without standards
- Handoffs between humans and AI are chaotic

**The Solution:**
- Structured specs (Phase → Milestone → Epic)
- Authoritative documentation (not chat history)
- Clear execution boundaries (when agent starts/stops)
- Explicit human review and approval

**Key Benefits:**
- Repeatable project execution
- Context preserved in files (not lost in chat)
- Clear accountability (who decides what)
- AI-assisted work with human governance

---

## Who This Is For

This system is designed for:
- Engineers using AI coding assistants (ChatGPT, GitHub Copilot, Cursor, etc.)
- Projects where scope, quality, and delivery matter
- People who want structure without sacrificing AI speed

**Prerequisites:**
- Git (basic familiarity)
- Markdown editing
- AI chat tool access (ChatGPT, Claude, etc.)

**What you'll need:**
- 30 minutes of focused time
- A git repository (new or existing)
- An AI assistant to act as your "Coding Agent"

---

## The 30-Minute Walkthrough

### Overview: What We'll Build

In this walkthrough, you'll:
1. Initialize the AI Project System structure (using `ai-project init`)
2. Start HQ Mode and create a Phase spec
3. Plan and create a Milestone spec
4. Create an Epic spec within that Milestone
5. Execute that Epic with an AI Coding Agent
6. Complete and close your first Epic

**Time estimate:** 25-30 minutes

---

## Step 1: Initialize Repository Structure
**Time: 1 minute**

### 1.1 Run the CLI

Use the `ai-project init` command to scaffold your project in seconds:

```bash
ai-project init my-project
cd my-project
```

This creates:
- **Canonical `docs/` hierarchy** (phases, roadmap, context, decisions, admin)
- **Governance submodule** pinned to the current version
- **`.ai-project.yml`** with correct governance reference
- **Governance Agent file.** The canonical, tool-neutral location is
  `.ai-project/agents/governance.agent.md`. (The CLI also writes a copy to `.github/agents/`, which
  GitHub Copilot auto-detects — see [Tool Integration Guides](integrations/README.md).)

### 1.2 Install the CLI (if needed)

If you don't have the CLI installed, grab it from the [AI Project System repository](https://github.com/panchew/ai-project-system):

```bash
# Clone the system repository
git clone https://github.com/panchew/ai-project-system.git
# Copy the CLI to your PATH
cp ai-project-system/bin/ai-project-init /usr/local/bin/
```

Or use the git submodule approach directly:

```bash
cd your-project
mkdir -p docs/phases docs/roadmap docs/context docs/decisions docs/admin
git submodule add https://github.com/panchew/ai-project-system.git .governance
git submodule update --init --recursive
cat > .ai-project.yml << EOF
governance:
  source: ./.governance
  version: "4.0.0"
  ref: v4.0.0
project:
  name: your-project
  description: "Your project description"
EOF
```

### 1.3 Verify structure

```
your-project/
├── .ai-project.yml             # Project configuration contract
├── .governance/                # Git submodule (pinned version)
│   └── governance/
│       ├── PROJECT-SYSTEM-GUIDELINES.md
│       ├── AI-OPERATING-GUIDELINES.md
│       ├── templates/
│       ├── diagrams/
│       ├── systems/
│       └── guides/
├── docs/
│   ├── phases/                 # Phase → Milestone → Epic artifacts
│   ├── roadmap/
│   ├── context/
│   ├── decisions/
│   └── admin/
├── .ai-project/
│   └── agents/
│       └── governance.agent.md # Governance Agent (canonical, tool-neutral; all modes)
├── .github/
│   └── agents/
│       └── governance.agent.md # GitHub Copilot auto-detection copy (one tool's convention)
└── [your existing project files]
```

✅ **Checkpoint:** Your project is initialized with governance, ready for HQ Chat.

---

## Step 2: Create Your First Phase Spec (HQ Mode)

**Time: 3 minutes**

A **Phase** is a major segment of work with a clear purpose and exit criteria. Use the **Governance Agent in HQ mode** to create it.

### 2.1 Start HQ Mode

1. Open your project in your AI chat tool that supports agent instructions from a markdown file.
2. Ensure the tool has access to the unified Governance Agent at its canonical, tool-neutral path
   `.ai-project/agents/governance.agent.md`. For the exact steps in your tool — Claude Code, Cursor,
   Windsurf, or GitHub Copilot — follow the matching [Tool Integration Guide](integrations/README.md).
3. Select or load the agent per that guide (e.g., select `hq` in Copilot; import or `@`-mention the
   file in Claude Code / Cursor / Windsurf).
4. Send the canonical prompt to activate **HQ mode**:

**For a new project:**
```
I'm starting a new project using the AI Project System governance framework.
Initialize HQ Chat for my-project and help me create a Phase 0 project formalization.
```

**For an existing project (adoption):**
```
I want to adopt the AI Project System governance framework for my existing project at [repository-path].
Initialize HQ Chat for this project, help me assess what's needed for adoption, and create a migration plan.
```

### 2.2 Follow HQ mode guidance

The agent (in HQ mode) will:
1. Read `.ai-project.yml` to discover governance context
2. Present a structured Phase 0 spec
3. Guide you through approving it
4. Save the Phase spec to `docs/phases/`

**If you don't have the Governance Agent available**, you can create the spec manually from the template:

```bash
cp .governance/governance/templates/phase-spec.md docs/phases/P1__phase__my-first-phase.md
```

Then fill in the front-matter and sections per the template instructions.

✅ **Checkpoint:** You've created your first Phase specification.

---

## Step 3: Create Your First Milestone Spec
**Time: 5 minutes**

A **Milestone** is a collection of related Epics that deliver a cohesive increment.

### 3.1 Create a Phase folder

```bash
mkdir -p docs/phases/P1__My_First_Phase
```

### 3.2 Copy the template

```bash
cp .governance/governance/templates/milestone-spec.md docs/phases/P1__My_First_Phase/P1-M1__milestone.md
```

### 3.3 Fill in the front-matter

```yaml
---
project: my-project-name
phase: P1
milestone: M1
type: milestone
status: planned
last_updated: 2026-01-29
---
```

### 3.4 Complete the Milestone spec

**Milestone Title:**
```markdown
# Milestone M1 — My First Milestone

**Phase:** P1 — My First Phase
```

**Purpose:**
```markdown
## Purpose

This Milestone delivers [describe the deliverable increment].

Example:
This Milestone delivers the initial project documentation structure and 
completes the first Epic to validate the workflow.
```

**Problem Statement:**
```markdown
## Problem Statement

Currently:
- [Describe current state]
- [What's missing or broken]

This Milestone:
- [What it provides]
- [How it improves the situation]
```

**Goals:**
```markdown
## Goals

By the end of this Milestone:

1. [Goal 1]
2. [Goal 2]
3. [Goal 3]
```

**Planned Epics:**
```markdown
## Planned Epics

- **E1.1** — [Epic name] ([planned/active/complete])
  - [Brief description]
```

### 3.5 Save and commit

```bash
git add docs/phases/P1__My_First_Phase/P1-M1__milestone.md
git commit -m "Add Milestone M1 spec"
```

✅ **Checkpoint:** You've created your first Milestone specification.

---

## Step 4: Create Your First Epic Spec
**Time: 7 minutes**

An **Epic** is a single unit of deliverable work with clear goals and acceptance criteria.

### 4.1 Copy the template

```bash
cp .governance/governance/templates/epic-spec.md docs/phases/P1__My_First_Phase/P1-M1-E1.1__spec__my-first-epic.md
```

### 4.2 Fill in the front-matter

```yaml
---
project: my-project-name
phase: P1
milestone: M1
epic: E1.1
type: spec
status: planned
last_updated: 2026-01-29
---
```

### 4.3 Complete the Epic spec

**Epic Title:**
```markdown
# Epic E1.1 — My First Epic

**Phase:** P1 — My First Phase  
**Milestone:** M1 — My First Milestone
```

**Context:**
```markdown
## Context

[Provide background on why this Epic exists]

Example:
To validate the AI Project System workflow, we need a simple Epic that 
demonstrates the full lifecycle from spec creation → execution → closure.
```

**Problem Statement:**
```markdown
## Problem Statement

[Describe the specific problem this Epic solves]

Example:
There is no working example of an Epic execution in this project. 
This Epic creates a simple documentation file to validate the workflow.
```

**Goals:**
```markdown
## Goals

By the end of this Epic:

1. [Goal 1 - make it measurable]
2. [Goal 2 - make it verifiable]
3. [Goal 3 - make it achievable]

Example:
1. Create a project README in the repository root
2. Document the project's purpose and structure
3. Verify the Epic execution and closure workflow
```

**Deliverables:**
```markdown
## Deliverables

The following artifacts will be produced:

1. ✅ `README.md` — Project overview and navigation
2. ✅ `P1-M1-E1.1__completion__my-first-epic.md` — Delivery Notice

(Checkboxes help track progress during execution)
```

**Definition of Done:**
```markdown
## Definition of Done

This Epic is complete when:

- [ ] README.md created in repository root
- [ ] README includes project purpose, structure, and getting started
- [ ] Delivery Notice created and committed
- [ ] All changes committed to `epic/E1.1` branch
- [ ] Pull request opened to `milestone/M1` branch
```

**Acceptance Criteria:**
```markdown
## Acceptance Criteria

Success criteria for human review:

- README clearly explains project purpose
- README is well-formatted and professional
- All links work correctly
- Delivery Notice verifies DoD completion
```

**Technical Constraints:**
```markdown
## Technical Constraints

- **Format:** Markdown only
- **Tone:** Professional, concise
- **Length:** README should be scannable (not too long)
```

### 4.4 Save and commit

```bash
git add docs/phases/P1__My_First_Phase/P1-M1-E1.1__spec__my-first-epic.md
git commit -m "Add Epic E1.1 spec"
```

✅ **Checkpoint:** You've created your first Epic specification.

---

## Step 5: Execute Your First Epic
**Time: 5-10 minutes**

Now you'll execute the Epic using an AI Coding Agent.

### 5.1 Create the Epic Execution Chat Starter

```bash
cp .governance/governance/templates/epic-execution-chat-starter.md temp-chat-starter.md
```

Open `temp-chat-starter.md` and fill in:

**Front section:**
```markdown
# Epic Execution Chat Starter — E1.1

**Epic:** E1.1 — My First Epic  
**Phase:** P1 — My First Phase  
**Milestone:** M1 — My First Milestone  
**Repository:** [your-username]/[your-repo]  
**Branch Strategy:** `epic/E1.1` → PR to `milestone/M1`
```

**Governance References:**
Point to your governance documents (they're in `docs/`).

**Epic Specification:**
Link to your Epic spec:
```markdown
**Full spec:** `docs/phases/P1__My_First_Phase/P1-M1-E1.1__spec__my-first-epic.md`
```

**Deliverables:**
```markdown
## Deliverables

You must produce:

1. ✅ `README.md` — Project overview
2. ✅ `P1-M1-E1.1__completion__my-first-epic.md` — Delivery Notice
```

**Branch Creation:**
```markdown
## Branch Creation Instructions

1. Ensure you're on `master` or `main`:
   ```bash
   git checkout master
   git pull origin master
   ```

2. Create `milestone/M1` branch:
   ```bash
   git checkout -b milestone/M1
   ```

3. Create `epic/E1.1` branch FROM `milestone/M1`:
   ```bash
   git checkout -b epic/E1.1
   ```
```

**Definition of Done:**
Copy from your Epic spec.

**Execution Contract:**
```markdown
### Your Responsibilities (Coding Agent)

1. Create branch `epic/E1.1` from `milestone/M1`
2. Create the deliverables listed above
3. Verify Definition of Done
4. Create Delivery Notice
5. Commit all changes to `epic/E1.1` branch
6. Open pull request to `milestone/M1` branch
7. Produce Epic Delivery Notice (as chat message)
8. Stop and await HQ authorization

### What You Must NOT Do

- ❌ Do NOT merge the PR (HQ authorizes merge)
- ❌ Do NOT infer acceptance (HQ decides)
- ❌ Do NOT continue without instruction
```

### 5.2 Launch Epic Mode

Open your AI chat tool (ChatGPT, Claude, etc.) with the Governance Agent selected and paste the entire Chat Starter you just created.

**The AI will:**
1. Create the `milestone/M1` and `epic/E1.1` branches
2. Create the README
3. Create the Delivery Notice
4. Commit changes
5. Open a PR
6. Produce an Epic Delivery Notice
7. Stop and wait for you

### 5.3 Monitor execution

The AI will show you:
- Git commands being run
- Files being created
- Commits being made
- PR being opened

**Let it work autonomously.** It has clear instructions.

✅ **Checkpoint:** Your AI agent has executed the Epic and is awaiting your review.

---

## Step 6: Complete and Close Your Epic
**Time: 5 minutes**

Now you perform the human review and close the Epic.

### 6.1 Review the deliverables

The AI has produced:
- README.md (in repository root)
- Delivery Notice (in `docs/phases/P1__My_First_Phase/`)
- A pull request from `epic/E1.1` → `milestone/M1`

**Review checklist:**
- [ ] Does the README meet the goals stated in the Epic spec?
- [ ] Is the Delivery Notice complete?
- [ ] Are all Definition of Done items checked off?
- [ ] Does the work meet acceptance criteria?

### 6.2 Create an Epic Review Seal (optional but recommended)

```bash
cp .governance/governance/templates/epic-review-seal.md docs/phases/P1__My_First_Phase/P1-M1-E1.1__review-seal__my-first-epic.md
```

Fill it in with your review findings:
- What you reviewed
- What worked well
- Any issues found
- Your recommendation (Accept / Reject / Request Changes)

Commit it to the `epic/E1.1` branch:
```bash
git add docs/phases/P1__My_First_Phase/P1-M1-E1.1__review-seal__my-first-epic.md
git commit -m "Add Epic Review Seal for E1.1"
git push origin epic/E1.1
```

### 6.3 Make your decision

In the AI chat, provide your decision:

**If you accept:**
```
I have reviewed Epic E1.1 and accept the work. 
Authorization granted: merge PR #[number] from epic/E1.1 to milestone/M1.
```

**If you reject:**
```
I have reviewed Epic E1.1 and reject the work due to: [reason].
Do not merge. [Provide instructions for next steps]
```

**If you request changes:**
```
I have reviewed Epic E1.1 and request the following changes:
1. [Change 1]
2. [Change 2]

Please make these updates and re-deliver.
```

### 6.4 Authorize the merge

If you accepted the work, explicitly tell the AI:

```
Authorization granted: merge epic/E1.1 to milestone/M1.
```

The AI will merge the PR.

### 6.5 Celebrate! 🎉

You've completed your first Epic using the AI Project System!

**What you accomplished:**
- Created a Phase spec
- Created a Milestone spec
- Created an Epic spec
- Executed an Epic with AI assistance
- Reviewed and accepted the work
- Closed an Epic through the proper workflow

✅ **Checkpoint:** You've completed the full Epic lifecycle.

---

## What's Next?

### Learn More

Now that you've completed your first Epic, explore:

1. **Follow the Adoption Guide**
   - [ADOPTION-GUIDE.md](ADOPTION-GUIDE.md) — Step-by-step from zero to HQ Chat live
   - [ADOPTION-FAQ.md](ADOPTION-FAQ.md) — Troubleshooting common issues

2. **Understand Governance**
   - Read [PROJECT-SYSTEM-GUIDELINES.md](PROJECT-SYSTEM-GUIDELINES.md) for system structure
   - Read [AI-OPERATING-GUIDELINES.md](AI-OPERATING-GUIDELINES.md) for execution procedures

3. **Visual Learning**
   - Review [Epic Lifecycle Flow](diagrams/epic-lifecycle-flow.md) diagram
   - Review [Authority Hierarchy](diagrams/authority-hierarchy.md) diagram
   - Review [Repository Structure](diagrams/repository-structure.md) diagram

4. **See Examples**
   - Browse [Phase P1](phases/P1__System_Foundation_and_Adoption/) for real Epic specs and completions
   - Browse [Phase P2](phases/P2__Adoption_Architecture_and_Multi_Project_Support/) for multi-project adoption artifacts
   - Study how this system was built using itself

5. **System References**
   - [How to Start a Project](systems/start-a-project.md)
   - [HQ Chat Guide](systems/hq-chat.md)
   - [Governance Propagation](systems/governance-propagation.md)
   - [Override Boundaries](../override-boundaries.md) — Customizing conventions

### Plan Your Next Epic

Ready to create your next Epic?

1. **Identify a problem or opportunity** in your project
2. **Use HQ Chat** to create an Epic spec and Epic Execution Chat Starter
3. **Launch your Coding Agent** with the Chat Starter
4. **Review and close** following the canonical happy path

### Common Next Steps

**If you're starting a new project:**
- Run `ai-project init` to scaffold (see [Adoption Guide](ADOPTION-GUIDE.md))
- Use HQ Chat to create Phase 0 project formalization
- Define milestones and Epics with HQ Chat guidance

**If you're integrating into an existing project:**
- Follow the [Legacy Project Migration Guide](legacy-project-migration.md)
- Create a transition Phase for "Governance Adoption"
- Prioritize Epics that document existing structure first

**If you're experimenting:**
- Create small, low-risk Epics
- Practice the full workflow
- Refine your Epic specs based on what works

---

## Quick Reference

### Common Commands

**Initialize a new project:**
```bash
ai-project init my-project
```

**Create branches:**
```bash
git checkout master && git pull
git checkout -b milestone/M1
git checkout -b epic/E1.1
```

**Check status:**
```bash
git status
git branch
```

**Commit changes:**
```bash
git add .
git commit -m "Your commit message"
git push origin epic/E1.1
```

**Merge Epic → Milestone:**
```bash
git checkout milestone/M1
git merge epic/E1.1
git push origin milestone/M1
```

**Update governance reference:**
```bash
cd .governance && git fetch && git checkout v4.0.0 && cd ..
```

### File Locations

| What | Where |
|------|-------|
| Project configuration | `.ai-project.yml` (repository root) |
| Governance rules | `.governance/governance/PROJECT-SYSTEM-GUIDELINES.md`, `.governance/governance/AI-OPERATING-GUIDELINES.md` |
| Templates | `.governance/governance/templates/` |
| Governance Agent (canonical, tool-neutral) | `.ai-project/agents/governance.agent.md` |
| Governance Agent (GitHub Copilot auto-detection copy) | `.github/agents/governance.agent.md` |
| Phase Specs | `docs/phases/P<N>__phase__*.md` |
| Milestone Specs | `docs/phases/P<N>__*/P<N>-M<N>__milestone.md` |
| Epic Specs | `docs/phases/P<N>__*/P<N>-M<N>-E<N>.<N>__spec__*.md` |
| Completions | `docs/phases/P<N>__*/P<N>-M<N>-E<N>.<N>__completion__*.md` |
| Adoption records | `.governance/governance/adoption-records/` |
| Diagrams | `.governance/governance/diagrams/` |

### Key Concepts Glossary

| Term | Definition |
|------|------------|
| **Phase** | Major segment of work (e.g., "Foundation", "Feature Development") |
| **Milestone** | Collection of related Epics delivering cohesive increment |
| **Epic** | Single unit of deliverable work (atomic, complete, reviewable) |
| **HQ** | Human Quartermaster (you, the human decision-maker) |
| **Coding Agent** | AI assistant executing work per specs |
| **Definition of Done** | Checklist of completion criteria for an Epic |
| **Acceptance Criteria** | Success criteria for human review |
| **Epic Delivery Notice** | Chat message from agent documenting completion |
| **Epic Review Seal** | Document capturing human review findings |
| **Canonical Happy Path** | Standard Epic lifecycle: Plan → Execute → Deliver → Review → Accept → Merge → Close |

### Branch Naming (Defaults)

```
master                  (production)
  └── phase/P1         (long-lived)
      └── milestone/M1 (long-lived)
          └── epic/E1.1 (short-lived)
```

Prefixes (`epic/`, `milestone/`, `phase/`) are configurable via `.ai-project.yml` overrides. See [Override Boundaries](../override-boundaries.md).

### File Naming

```
Phase:      P1__phase__project-foundation.md
Milestone:  P1-M1__milestone.md
Epic Spec:  P1-M1-E1.1__spec__create-readme.md
Completion: P1-M1-E1.1__completion__create-readme.md
```

---

## Troubleshooting

### "My AI agent merged the PR without authorization"

**Fix:** Remind the agent:
```
Per AI-OPERATING-GUIDELINES.md, you must not merge without explicit HQ authorization.
Please wait for my accept/reject decision and merge authorization.
```

### "My AI agent is asking too many questions"

**Fix:** Your Epic spec or Chat Starter may be ambiguous. Provide more detail in:
- Definition of Done (clear checklist)
- Deliverables (explicit list)
- Technical Constraints (clear boundaries)

### "I don't know what to put in my Epic spec"

**Fix:** Start simple:
- **Problem:** "We don't have X" or "Y is broken"
- **Goal:** "Create X" or "Fix Y"
- **Deliverable:** "A file/feature/fix that does Z"
- **DoD:** "File exists, tests pass, documentation updated"

### "This feels like too much documentation"

**Reminder:** 
- Documentation is authoritative, chat is ephemeral
- AI agents lose context without documentation
- Specs take 10 minutes, save hours of re-explanation
- You're trading upfront clarity for execution efficiency

---

## Get Help

- **Full Governance:** [PROJECT-SYSTEM-GUIDELINES.md](PROJECT-SYSTEM-GUIDELINES.md)
- **Execution Procedures:** [AI-OPERATING-GUIDELINES.md](AI-OPERATING-GUIDELINES.md)
- **Adoption Guide:** [ADOPTION-GUIDE.md](ADOPTION-GUIDE.md)
- **Adoption FAQ:** [ADOPTION-FAQ.md](ADOPTION-FAQ.md)
- **Visual Guides:** [governance/diagrams/](../diagrams/)
- **Examples:** [Phase P1](phases/P1__System_Foundation_and_Adoption/) | [Phase P2](phases/P2__Adoption_Architecture_and_Multi_Project_Support/)

**Still stuck?** File an issue in the [AI Project System repository](https://github.com/panchew/ai-project-system).

---

**You're ready to go. Happy building!** 🚀
