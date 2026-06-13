---
project: taskflow
phase: P1
milestone: M1
type: milestone
status: active
last_updated: 2026-06-01
---

# Milestone M1 — Core Backend

## Purpose

Establish the complete backend foundation for Taskflow: user authentication, task data management, and the database schema that all future milestones depend on.

This milestone ensures:
- Authenticated users can register and log in securely
- Tasks can be created, read, updated, and deleted via a REST API
- The PostgreSQL schema is migration-based and extensible

---

## Problem Statement

Without a working backend, the frontend cannot display data, and the deployment pipeline has nothing to ship. M1 is the critical-path dependency for everything else in Phase P1.

---

## Goals

By the end of this milestone, the system must:

1. Provide JWT-based user authentication (register, login, token refresh, logout)
2. Expose a REST API for task CRUD operations with input validation
3. Define and migrate the PostgreSQL schema for users and tasks
4. Achieve 80%+ test coverage on all backend modules

---

## Non-Goals

This milestone explicitly does **not** aim to:

- Build any frontend (deferred to M2)
- Implement real-time updates via WebSockets
- Support file attachments on tasks
- Build admin tooling or dashboards

---

## In Scope

- JWT authentication middleware (register, login, refresh, logout)
- Task CRUD REST API endpoints
- PostgreSQL schema design and Alembic migrations
- Unit and integration tests for auth and task modules

---

## Out of Scope

- Frontend components
- CI/CD pipeline configuration
- Performance benchmarking

---

## Planned Epics

### Confirmed Epics

- [E1.1 — User Authentication](E1.1__spec__user-authentication.md) — JWT auth: register, login, token refresh, logout
- [E1.2 — Task CRUD API](E1.2__spec__task-crud-api.md) — REST endpoints for creating, reading, updating, deleting tasks
- [E1.3 — Database Schema](E1.3__spec__database-schema.md) — PostgreSQL schema and Alembic migration scripts

### Deferred Epics

- None

---

## Completion Criteria

Milestone M1 is complete when all Epics under M1 are completed and closed.

Additional criteria:
- All three Epic PRs merged to `milestone/M1`
- Integration test suite passes end-to-end (auth → task CRUD)
- Phase Lead (Alex Rivera) issues Milestone Completion Notice

---

## Acceptance Criteria

- [ ] POST /auth/register and POST /auth/login return valid JWTs
- [ ] Task endpoints enforce authentication (401 on missing token)
- [ ] All database tables created via migration scripts (no manual DDL)
- [ ] Test coverage ≥ 80% on auth and task modules
- [ ] API documentation (OpenAPI) generated and committed

---

## Dependencies

**Internal Dependencies:**
- None (M1 is the first milestone in P1)

**External Dependencies:**
- PostgreSQL 15+ instance available for integration tests

---

## Timeline

**Target Start:** 2026-06-01
**Target Completion:** 2026-06-10
**Actual Start:** 2026-06-01
**Actual Completion:** In progress

---

## Notes

E1.1 (User Authentication) and E1.2 (Task CRUD API) can execute in parallel once E1.3 (Database Schema) is merged, since they both depend on the schema. The recommended execution order is: E1.3 first, then E1.1 and E1.2 in parallel.
