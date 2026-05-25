---
project: ai-project-system
phase: P3
milestone: M12
type: milestone
status: planned
last_updated: 2026-05-23
---

# Milestone M12 — Containerized Sandbox & Loop Verification

## Purpose

The purpose of this milestone is to implement the containerized validation sandbox and mature the closed-loop autonomous Dev-QA self-repair engine. It builds upon the file-driven bus established in M11 by encapsulating the execution of coding agents and QA test suites within secure, volume-mounted containers, and enabling deterministic self-repair iterations.

This milestone ensures:
- Agent execution and validation are strictly sandboxed within isolated Docker environments.
- Coding and QA models interact in a closed-loop execution loop to self-repair failures.
- Robust verification testing of the autonomous loop under multi-attempt failures, successes, and escalations.
- Security constraints are enforced regarding filesystem write boundaries and volume mount permissions.

---

## Problem Statement

Allowing autonomous agents to execute code or run test suites directly on the host machine presents severe security risks (malicious code execution, host system compromise) and environmental reproducibility issues (package/runtime dependency drift). Additionally, without an integrated closed-loop self-repair mechanism, if an agent makes a trivial error during code generation, the system immediately stalls, requiring manual human intervention and violating the goal of a 24/7 unattended autonomous development cluster.

---

## Goals

By the end of this milestone, the system must:

1. Provide a canonical, secure `Dockerfile.sandbox` defining the isolated environment for execution and validation.
2. Mature the python orchestrator to implement the full Dev-QA closed-loop self-repair cycle with a strict 3-attempt ceiling.
3. Deliver a robust verification mock harness to simulate and validate all loop scenarios.
4. Establish security boundaries and lock-handling controls to prevent host contamination and handle crashes gracefully.

---

## Non-Goals

This milestone explicitly does **not** aim to:

- Implement the CLI background daemon or state verification commands (deferred to M13).
- Implement automated Git merge hooks or main-branch auto-promotions (deferred to M13).
- Provide a graphical interface or web-based monitoring dashboard for running loops.
- Support container orchestrators beyond standard Docker (e.g., Kubernetes, Nomad).

---

## In Scope

- Docker sandbox packaging and base image configuration.
- Closed-loop self-repair logic integration within `bin/ai-project-orchestrator`.
- Failure logging, traceback capturing, and feedback routing to Dev roles.
- Development of a simulation/mock harness for testing the 3-attempt loop behavior.
- Hardening of folder write boundaries, sandbox volume isolation, and environment cleanup.
- Graceful signals handling (SIGINT, SIGTERM) and lockfile recovery mechanics.

---

## Out of Scope

- Automated git hook verification for developer commits.
- Hybrid model routing to cloud providers not configured in `.ai-project.yml`.
- Multi-container networks or microservice sandboxing in execution.

---

## Planned Epics

### Confirmed Epics

- [E12.1 — Sandbox Container Image](P3-M12-E12.1__spec__sandbox-container-image.md) — Create and package the official `Dockerfile.sandbox` image to run linters, tests, and runtimes isolated from the host.
- [E12.2 — Closed-Loop Execution Recursion Engine](P3-M12-E12.2__spec__closed-loop-recursion-engine.md) — Upgrade the Python Orchestrator to route QA logs back to the Dev model for iterative self-repair attempts.
- [E12.3 — Verification Script & Loop Mock Harness](P3-M12-E12.3__spec__verification-mock-harness.md) — Create a CLI harness simulating success, multi-attempt repair, and escalation states to verify loop stability.
- [E12.4 — Sandbox Security Boundaries & Lock Recovery](P3-M12-E12.4__spec__sandbox-security-boundaries.md) — Implement file write boundary restrictions, container isolation safeguards, and strict lock-file lifecycle handling.

---

## Completion Criteria

Milestone M12 is complete when all Epics under M12 are completed and closed.

---

## Acceptance Criteria

- [ ] Sandbox Docker container successfully boots, runs mock validations, and cleanly exits.
- [ ] Orchestrator executes self-repair loops, routing error outputs back to the developer role successfully.
- [ ] A 3-attempt ceiling is strictly enforced: success on attempt 1, 2, or 3 deletes the queue trigger and commits the code, while failure on attempt 3 produces a structured markdown escalation report under `docs/admin/`.
- [ ] Simulating failures via the Mock Harness verifies loop outcomes without hanging.
- [ ] Sandbox volume permissions restrict write access to authorized workspaces.
- [ ] Interruptions (SIGINT/SIGTERM) or container failures cleanly release the `.ai-project/locks/execution.lock` and execute cleanup.

---

## Dependencies

**Internal Dependencies:**
- Milestone M11 (File-Driven Bus & State Triggers) must be completed and closed (Completed).

**External Dependencies:**
- Docker engine must be installed and running on the host machine for sandbox execution.

---

## Timeline

**Target Start:** 2026-05-23  
**Target Completion:** 2026-05-30  
**Actual Start:** 2026-05-23  
**Actual Completion:** In progress (planned)

---

## Notes

This milestone provides the primary security barrier and self-repair resilience of the unattended cluster, transforming the orchestrator into a fully autonomous, production-grade DevOps engine.
