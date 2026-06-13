---
project: taskflow
phase: P1
milestone: M2
type: milestone
status: planned
last_updated: 2026-06-01
---

# Milestone M2 — Frontend

## Purpose

Build the React frontend that lets users interact with Taskflow through a browser. M2 consumes the M1 API and delivers a polished task management experience.

This milestone ensures:
- Users can log in via a browser-based authentication flow
- Users can view, create, edit, and delete tasks from a dashboard
- Users can search and filter tasks by status, priority, and assignee

---

## Problem Statement

The M1 backend provides a functional API but has no user interface. Without M2, Taskflow is inaccessible to non-technical stakeholders and cannot be demonstrated to end users.

---

## Goals

By the end of this milestone, the system must:

1. Provide a login/registration page that calls the M1 auth API
2. Display a task dashboard showing all tasks with inline editing
3. Support search (by title/description) and filtering (by status, priority, assignee)
4. Achieve Lighthouse performance score ≥ 85 on the dashboard page

---

## Non-Goals

This milestone explicitly does **not** aim to:

- Build a native mobile app
- Implement real-time collaborative editing
- Build admin or reporting dashboards
- Optimize the backend API (that belongs in M3)

---

## In Scope

- React 18 frontend application (TypeScript)
- Login and registration screens
- Task dashboard with CRUD operations
- Search and filter functionality
- Component unit tests (Jest + React Testing Library)

---

## Out of Scope

- End-to-end browser tests (Cypress/Playwright)
- Dark mode or theme switching
- Internationalization (i18n)

---

## Planned Epics

### Confirmed Epics

- [E2.1 — Login UI](E2.1__spec__login-ui.md) — Login and registration pages wired to the M1 auth API
- [E2.2 — Task Dashboard](E2.2__spec__task-dashboard.md) — Full task management dashboard with inline CRUD
- [E2.3 — Search and Filter](E2.3__spec__search-and-filter.md) — Search bar and filter sidebar for the task list

### Deferred Epics

- None

---

## Completion Criteria

Milestone M2 is complete when all Epics under M2 are completed and closed.

Additional criteria:
- All Epic PRs merged to `milestone/M2`
- Lighthouse performance score ≥ 85 confirmed against staging
- Phase Lead (Alex Rivera) issues Milestone Completion Notice

---

## Acceptance Criteria

- [ ] A user can log in and see their task dashboard within 3 seconds on a standard connection
- [ ] A user can create a task with title, description, priority, and due date without a page reload
- [ ] Search returns results within 500ms for a dataset of 500 tasks
- [ ] Filter combinations (status AND priority) work correctly

---

## Dependencies

**Internal Dependencies:**
- M1 must be completed before M2 begins (all auth and task API endpoints required)

**External Dependencies:**
- M1 API is deployed to a staging environment accessible by the frontend build

---

## Timeline

**Target Start:** 2026-06-11
**Target Completion:** 2026-06-20
**Actual Start:** Not started
**Actual Completion:** In progress

---

## Notes

E2.1, E2.2, and E2.3 can execute in parallel after the M1 API is available. E2.1 (Login UI) should be prioritized first so other epics can use authentication in their integration tests.
