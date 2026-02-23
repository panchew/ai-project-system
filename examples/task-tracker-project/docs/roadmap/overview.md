# Roadmap Overview — Personal Task Tracker CLI

## Project Vision

Build a simple, effective command-line tool for managing personal tasks. The tool should help individuals organize their work, track progress, and stay productive without unnecessary complexity.

## Project Phases

### Phase 0 — Project Initialization

**Goal:** Establish project repository and governance

**Milestones:**
- **M0.1:** Repository Setup & Governance *(Completed)*

**Key Deliverables:**
- Repository structure established
- Governance documents in place
- Development environment configured

**Status:** ✅ Completed

---

### Phase 1 — Core Features

**Goal:** Deliver essential task management functionality

**Milestones:**
- **M1:** Basic Task Management *(In Progress)*
- **M2:** Task Organization & Filtering *(Planned)*
- **M3:** Data Persistence & Export *(Planned)*

**Key Capabilities:**
- Create, read, update, delete tasks
- List and filter tasks
- Mark tasks complete
- Persist data between sessions
- Export task lists

**Status:** 🔄 In Progress

---

### Phase 2 — Advanced Features *(Future)*

**Goal:** Add productivity-enhancing features

**Planned Milestones:**
- **M1:** Recurring Tasks & Templates
- **M2:** Due Dates & Reminders
- **M3:** Tags & Categories

**Status:** 📋 Planned

---

## Current Focus: Phase 1, Milestone 1

### Milestone M1 — Basic Task Management

**Goal:** Enable users to create and manage tasks

**Epics:**

#### Epic 1.1 — Task Creation & Storage *(In Progress)*

**Problem:** Users need to create tasks and have them persisted

**Deliverables:**
- Task data model (JSON schema)
- Task creation command (`task add "description"`)
- In-memory storage implementation
- Basic validation (required fields, length limits)
- Unit tests for task creation

**Acceptance Criteria:**
- User can create task with description
- Task receives unique ID
- Task defaults to "pending" status
- Task is stored in memory
- Invalid input is rejected with clear error

**Status:** 🔄 In Progress

---

#### Epic 1.2 — Task Listing *(Planned)*

**Problem:** Users need to view their tasks

**Deliverables:**
- List command (`task list`)
- Formatted output (table or list view)
- Filter by status (pending, completed)
- Sort options (by date, priority)

**Status:** 📋 Planned

---

#### Epic 1.3 — Task Completion *(Planned)*

**Problem:** Users need to mark tasks as complete

**Deliverables:**
- Complete command (`task complete <id>`)
- Status transition logic
- Completion timestamp
- Validation (task exists, already completed)

**Status:** 📋 Planned

---

## Milestone Progress Tracking

### Phase 1, Milestone 1: Basic Task Management

| Epic | Title | Status | Est. Completion |
|------|-------|--------|----------------|
| E1.1 | Task Creation & Storage | In Progress | Week 1 |
| E1.2 | Task Listing | Planned | Week 2 |
| E1.3 | Task Completion | Planned | Week 2 |

---

## Future Milestones (High-Level)

### Phase 1, Milestone 2: Task Organization & Filtering
- Priority levels
- Search functionality
- Advanced filtering

### Phase 1, Milestone 3: Data Persistence & Export
- File-based storage (JSON)
- Export to CSV/Markdown
- Import existing task lists

### Phase 2, Milestone 1: Recurring Tasks
- Task templates
- Recurring schedules
- Auto-generation

### Phase 2, Milestone 2: Due Dates & Reminders
- Due date tracking
- Overdue highlighting
- Reminder notifications

---

## Dependencies & Constraints

**Technical Stack:**
- Language: Python 3.9+
- Storage: JSON file format
- CLI Framework: argparse (standard library)
- Testing: pytest

**External Dependencies:** None for Phase 1 (standard library only)

**Constraints:**
- Keep CLI simple and fast
- No external service dependencies
- Offline-first design
- Cross-platform (Linux, macOS, Windows)

---

## Risk & Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Scope creep | High | Strict Epic boundaries, clear DoD |
| Data loss | Medium | Implement file backups in M1.3 |
| Performance with large task lists | Low | Defer optimization to Phase 2 |

---

## Success Metrics

**Phase 1 Complete When:**
- Users can create, list, complete, and persist tasks
- All P1 Milestone acceptance criteria met
- Documentation complete
- Basic test coverage (>80%)

**Phase 2 Complete When:**
- Advanced features implemented
- Production-ready quality
- User testing complete

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-01-15 | Initial roadmap created |
| 0.2.0 | 2026-01-20 | Phase 1 milestones detailed |

---

**Note:** This roadmap represents the current plan. Phases and Milestones may be adjusted based on learning and user feedback.
