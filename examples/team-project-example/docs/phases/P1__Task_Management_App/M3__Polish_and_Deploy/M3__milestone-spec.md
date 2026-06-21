---
project: taskflow
phase: P1
milestone: M3
type: milestone
status: planned
last_updated: 2026-06-01
---

# Milestone M3 — Polish and Deploy

## Purpose

Harden, optimize, and ship Taskflow to production. M3 takes the working application from M1 and M2 and makes it production-grade with automated testing, deployment pipelines, and performance targets met.

This milestone ensures:
- The application meets the agreed performance SLAs (API < 200ms p95, Lighthouse ≥ 90)
- A CI/CD pipeline runs on every pull request and deploys automatically to staging
- The application is deployed to production with CFO authorization

---

## Problem Statement

An application that works locally but has no CI/CD, no performance validation, and no deployment path cannot be shipped. M3 closes the gap between "working in development" and "running reliably in production."

---

## Goals

By the end of this milestone, the system must:

1. Achieve API p95 response time ≤ 200ms for task list endpoints
2. Achieve frontend Lighthouse performance score ≥ 90
3. Provide a GitHub Actions CI/CD pipeline (lint, test, build, deploy to staging)
4. Deploy Taskflow to production with documented rollback procedure

---

## Non-Goals

This milestone explicitly does **not** aim to:

- Add new product features (those belong to Phase P2)
- Build a monitoring dashboard (covered by infrastructure team separately)
- Implement database read replicas or sharding

---

## In Scope

- API performance profiling and optimization
- Frontend bundle size reduction and lazy-loading
- GitHub Actions CI/CD workflow files
- Production deployment procedure and rollback runbook

---

## Out of Scope

- New product features
- Database scaling (read replicas, sharding)
- External monitoring setup (Datadog, PagerDuty)

---

## Planned Epics

### Confirmed Epics

- [E3.1 — Performance Optimization](E3.1__spec__performance-optimization.md) — API and frontend performance tuning to meet SLAs
- [E3.2 — CI/CD Pipeline](E3.2__spec__ci-cd-pipeline.md) — GitHub Actions workflow for automated testing and deployment
- [B1.1 — Auth Session Bugfix](B1.1__spec__auth-session-bugfix.md) — Expedited fix for JWT token expiry bug discovered in staging

### Deferred Epics

- None

---

## Completion Criteria

Milestone M3 is complete when all Epics under M3 are completed and closed.

Additional criteria:
- All Epic PRs merged to `milestone/M3`
- Staging deployment passes smoke tests
- CFO (Morgan Chen) issues Production Deployment Authorization

---

## Acceptance Criteria

- [ ] CI pipeline runs on every PR and blocks merge if tests fail
- [ ] API task list endpoint returns in ≤ 200ms (p95, 50 concurrent users)
- [ ] Frontend Lighthouse score ≥ 90 in production configuration
- [ ] Production deployment procedure is documented and tested

---

## Dependencies

**Internal Dependencies:**
- M2 must be completed before M3 performance optimization begins

**External Dependencies:**
- Production environment (cloud hosting) provisioned by the infrastructure team

---

## Timeline

**Target Start:** 2026-06-21
**Target Completion:** 2026-06-30
**Actual Start:** Not started
**Actual Completion:** Not started

---

## Notes

B1.1 (Auth Session Bugfix) was created via the expedited bugfix workflow after a critical JWT token expiry issue was discovered in staging during M2 testing. It uses the expedited SLA path (HQ review within 4 hours) rather than the standard planning path.
