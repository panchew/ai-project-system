# Example Project: Personal Task Tracker CLI

## Overview

This is a **complete example project** demonstrating the AI Project System lifecycle from initial planning through Epic completion.

**Problem Domain:** Personal Task Tracker CLI  
**Status:** Example/Educational (not production code)  
**Purpose:** Demonstrate proper Phase → Milestone → Epic structure and artifacts

## What This Example Demonstrates

This example shows:

- ✅ **Complete Phase → Milestone → Epic hierarchy**
- ✅ **Phase 0 (Project Initialization)** artifacts
- ✅ **Phase 1 (Core Features)** with Milestone 1 and Epic 1.1
- ✅ **All major artifact types:**
  - Epic Specification
  - Completion Report
  - Delivery Notice
  - Review Seal
  - Chat Starter
- ✅ **Realistic problem statement and solution design**
- ✅ **Proper repository structure and file naming**
- ✅ **Roadmap showing planned work**

## What This Example Does NOT Demonstrate

- ❌ Multiple Milestones (scope limited to M1 for simplicity)
- ❌ Multiple Epics per Milestone (focused on E1.1 walkthrough)
- ❌ Actual working code implementation (focus is on process, not code)
- ❌ Complex project with many dependencies
- ❌ Real-world production considerations

## How to Use This Example

### For New Users

**Goal: Understand the full Epic lifecycle in ~30 minutes**

1. **Read the roadmap** ([docs/roadmap/overview.md](docs/roadmap/overview.md))
   - See how work is organized into Phases and Milestones

2. **Review Phase structure** ([docs/phases/P1__Core_Features/](docs/phases/P1__Core_Features/))
   - Start with [P1__phase.md](docs/phases/P1__Core_Features/P1__phase.md)
   - Then [P1-M1__milestone.md](docs/phases/P1__Core_Features/P1-M1__milestone.md)

3. **Walk through Epic 1.1 complete lifecycle:**
   - **Start:** [P1-M1-E1.1__spec__task-creation-and-storage.md](docs/phases/P1__Core_Features/P1-M1-E1.1__spec__task-creation-and-storage.md)
   - **Execute:** [P1-M1-E1.1__chat-starter__task-creation-and-storage.md](docs/phases/P1__Core_Features/P1-M1-E1.1__chat-starter__task-creation-and-storage.md)
   - **Complete:** [P1-M1-E1.1__completion__task-creation-and-storage.md](docs/phases/P1__Core_Features/P1-M1-E1.1__completion__task-creation-and-storage.md)
   - **Deliver:** [P1-M1-E1.1__delivery-notice__task-creation-and-storage.md](docs/phases/P1__Core_Features/P1-M1-E1.1__delivery-notice__task-creation-and-storage.md)
   - **Review:** [P1-M1-E1.1__review-seal__task-creation-and-storage.md](docs/phases/P1__Core_Features/P1-M1-E1.1__review-seal__task-creation-and-storage.md)

4. **Understand Phase 0** ([docs/phases/P0__Project_Initialization/](docs/phases/P0__Project_Initialization/))
   - See how projects are initially set up
   - Review governance establishment

### For Starting Your Own Project

**Goal: Copy structure and adapt to your needs**

1. **Use this structure as a template** for your own project repository
2. **Adapt the roadmap** to your problem domain
3. **Follow the same artifact patterns** for your Epics
4. **Reference templates** in [../../governance/templates/](../../governance/templates/)
5. **Follow governance** from [../../governance/PROJECT-SYSTEM-GUIDELINES.md](../../governance/PROJECT-SYSTEM-GUIDELINES.md)

## Project Context: Personal Task Tracker CLI

**Fictional Project Summary:**

> A simple command-line tool for managing personal tasks. Users can create tasks, list them, mark them complete, and organize them by priority. This is a realistic but simple problem that everyone can understand.

**Why This Problem Domain?**

- ✅ Universally understandable (everyone has tasks to manage)
- ✅ Simple enough for a pedagogical example
- ✅ Complex enough to require proper planning (not trivial "hello world")
- ✅ Naturally demonstrates Phase → Milestone → Epic decomposition

**Project Scope (Fictional):**

- **Phase 0:** Project Initialization (repository setup, governance)
- **Phase 1:** Core Features (task CRUD, basic filtering)
- **Phase 2:** (Not shown) Advanced Features (recurring tasks, reminders)

## Key Learning Points

### 1. Epic Specifications Are Detailed

Look at [P1-M1-E1.1__spec](docs/phases/P1__Core_Features/P1-M1-E1.1__spec__task-creation-and-storage.md):
- Clear Problem Statement
- Specific Goals and Non-Goals
- Detailed Definition of Done
- Concrete Acceptance Criteria

### 2. Completion Reports Verify All DoD Items

Look at [P1-M1-E1.1__completion](docs/phases/P1__Core_Features/P1-M1-E1.1__completion__task-creation-and-storage.md):
- Every DoD item checked
- Evidence provided for each verification
- Clear statement of completion

### 3. Delivery Notices Formalize Handoff

Look at [P1-M1-E1.1__delivery-notice](docs/phases/P1__Core_Features/P1-M1-E1.1__delivery-notice__task-creation-and-storage.md):
- Structured summary of deliverables
- Explicit completion declaration
- Stops and awaits HQ authorization

### 4. Review Seals Confirm Human Acceptance

Look at [P1-M1-E1.1__review-seal](docs/phases/P1__Core_Features/P1-M1-E1.1__review-seal__task-creation-and-storage.md):
- Human reviewer identified
- Acceptance criteria verified
- Decision recorded

### 5. Chat Starters Provide Execution Context

Look at [P1-M1-E1.1__chat-starter](docs/phases/P1__Core_Features/P1-M1-E1.1__chat-starter__task-creation-and-storage.md):
- Comprehensive context packet for AI
- Spec reference and governance versions
- Execution mode and constraints

## Repository Structure

```
examples/task-tracker-project/
├── README.md (this file)
├── docs/
│   ├── phases/
│   │   ├── P0__Project_Initialization/
│   │   │   ├── P0__phase.md
│   │   │   └── P0-M0-E0.1__spec__repository-setup-and-governance.md
│   │   └── P1__Core_Features/
│   │       ├── P1__phase.md
│   │       ├── P1-M1__milestone.md
│   │       ├── P1-M1-E1.1__spec__task-creation-and-storage.md
│   │       ├── P1-M1-E1.1__completion__task-creation-and-storage.md
│   │       ├── P1-M1-E1.1__delivery-notice__task-creation-and-storage.md
│   │       ├── P1-M1-E1.1__review-seal__task-creation-and-storage.md
│   │       └── P1-M1-E1.1__chat-starter__task-creation-and-storage.md
│   └── roadmap/
│       └── overview.md
└── src/ (placeholder - optional, not the focus)
```

## Next Steps

After reviewing this example:

1. **Read the [Quick Start Guide](../../governance/guides/QUICK-START.md)** for step-by-step instructions
2. **Review the [templates](../../governance/templates/)** to see blank starting points
3. **Start your own project** using this structure as a reference
4. **Follow governance** from [PROJECT-SYSTEM-GUIDELINES.md](../../governance/PROJECT-SYSTEM-GUIDELINES.md)

## References

- [AI Project System Governance](../../governance/PROJECT-SYSTEM-GUIDELINES.md)
- [AI Operating Guidelines](../../governance/AI-OPERATING-GUIDELINES.md)
- [Quick Start Guide](../../governance/guides/QUICK-START.md)
- [Templates](../../governance/templates/)

---

**Note:** This is an educational example. The "Personal Task Tracker CLI" is not a real project. All artifacts demonstrate proper structure and process, not production code.
