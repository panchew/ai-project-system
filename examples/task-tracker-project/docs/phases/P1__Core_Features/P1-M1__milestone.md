---
project: task-tracker-cli
phase: P1
milestone: M1
type: milestone
status: active
last_updated: 2026-01-20
---

# Milestone M1 — Basic Task Management

## Overview

Milestone M1 delivers the foundational task management capabilities for the Personal Task Tracker CLI. This milestone enables users to create, view, and complete tasks — the core workflow that every task management tool must support.

## Context

**Parent Phase:** P1 — Core Features

**Relationship to Phase Goals:**
This milestone delivers the first iteration of core functionality. Users will be able to perform basic task operations, establishing the foundation for more advanced features in M2 and M3.

**Current State:**
- ✅ Phase 0 completed (repository and governance established)
- ✅ Phase 1 initiated
- 🔄 Milestone M1 active

---

## Goals

By the end of this Milestone:

1. Users can create tasks with descriptions
2. Users can view a list of their tasks
3. Users can mark tasks as complete
4. Tasks are stored in memory (file persistence deferred to M3)
5. Basic validation prevents invalid input
6. Core functionality is tested

---

## Epics

### Epic 1.1 — Task Creation & Storage *(In Progress)*

**Goal:** Enable users to create tasks and store them in memory

**Key Deliverables:**
- Task data model (Python dataclass or class)
- CLI command: `task add "description"`
- In-memory storage implementation
- Input validation (required fields, length limits)
- Unit tests for task creation

**Acceptance Criteria:**
- User can create task with description
- Task receives unique ID (auto-generated)
- Task defaults to "pending" status
- Invalid input rejected with clear error messages

**Status:** 🔄 In Progress

**Spec:** [P1-M1-E1.1__spec__task-creation-and-storage.md](P1-M1-E1.1__spec__task-creation-and-storage.md)

---

### Epic 1.2 — Task Listing *(Planned)*

**Goal:** Enable users to view their tasks

**Key Deliverables:**
- CLI command: `task list`
- Formatted output (readable list view)
- Filter by status (pending, completed)
- Sort by creation date

**Acceptance Criteria:**
- User can list all tasks
- User can filter by status
- Output is readable and well-formatted
- Empty list handled gracefully

**Status:** 📋 Planned

---

### Epic 1.3 — Task Completion *(Planned)*

**Goal:** Enable users to mark tasks as complete

**Key Deliverables:**
- CLI command: `task complete <id>`
- Status transition logic (pending → completed)
- Completion timestamp recording
- Validation (task exists, not already completed)

**Acceptance Criteria:**
- User can mark task complete by ID
- Status transitions correctly
- Completion timestamp recorded
- Invalid ID rejected with clear error
- Already-completed task handled gracefully

**Status:** 📋 Planned

---

## Success Criteria

Milestone M1 is complete when:

- ✅ All three Epics (E1.1, E1.2, E1.3) are completed
- ✅ User can create, list, and complete tasks via CLI
- ✅ Input validation works correctly
- ✅ Test coverage for core functionality exceeds 80%
- ✅ CLI commands are intuitive and consistent
- ✅ Error messages are clear and helpful

---

## Deliverables

### Code
- `task_tracker.models.Task` — Task data model
- `task_tracker.storage.InMemoryStorage` — In-memory task storage
- `task_tracker.cli` — CLI command handlers
- `task_tracker.validators` — Input validation
- Unit tests for all modules

### Documentation
- CLI usage examples (in README.md)
- API documentation (docstrings)

---

## Definition of Done

Milestone M1 is complete when:

- [ ] **All Epics completed**
  - E1.1 (Task Creation & Storage) ✅
  - E1.2 (Task Listing) ✅
  - E1.3 (Task Completion) ✅

- [ ] **Functionality verified**
  - User can create tasks
  - User can list tasks
  - User can complete tasks
  - All commands work as specified

- [ ] **Quality verified**
  - Test coverage > 80%
  - All tests passing
  - No critical bugs

- [ ] **Documentation complete**
  - CLI usage documented
  - Code documented (docstrings)
  - README updated

- [ ] **Review complete**
  - Code review conducted
  - User testing performed
  - Acceptance criteria verified

---

## Technical Constraints

- **Language:** Python 3.9+
- **Storage:** In-memory only (file persistence in M3)
- **CLI Framework:** argparse (standard library)
- **Testing:** pytest
- **Dependencies:** Standard library only for core functionality

---

## Dependencies

**Upstream:**
- Phase 0 complete (repository structure)

**Downstream:**
- Milestone M2 depends on M1 completion
- Milestone M3 depends on M1 completion

---

## Risks & Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| In-memory storage limits usability | Medium | Clearly document limitation, prioritize M3 |
| CLI usability issues | Medium | User testing before finalizing M1 |
| Validation edge cases missed | Low | Comprehensive test coverage |

---

## Progress Tracking

| Epic | Status | Est. Completion | Actual Completion |
|------|--------|----------------|-------------------|
| E1.1 | In Progress | 2026-01-22 | — |
| E1.2 | Planned | 2026-01-25 | — |
| E1.3 | Planned | 2026-01-27 | — |

**Milestone Target:** 2026-01-27

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.2.0 | 2026-01-20 | E1.1 in progress |
| 0.1.0 | 2026-01-17 | Milestone spec created |
