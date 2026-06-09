---
project: ai-project-system
phase: P3
milestone: M13
type: milestone
status: planned
last_updated: 2026-05-24
---

# Milestone M13 — Orchestrator CLI Daemon

## Purpose

The purpose of this milestone is to implement the unattended background CLI daemon and automate Git merge workflows. By introducing process daemonization and automated target-branch merging, we eliminate the need for manual orchestration scripts execution, allowing the agentic cluster to poll for new epics, run them in sandboxes, verify success, and auto-merge results back into parent milestone branches autonomously.

This milestone ensures:
- The orchestrator can run as a persistent background daemon (`ai-project-daemon`) on the host.
- The daemon detects newly written trigger files under `.ai-project/queue/` and initiates runs automatically.
- Success outcomes trigger automatic git merges/PR approvals based on the branch hierarchy rules.
- Daemon operations can be managed via a clean, self-documenting CLI interface (start, stop, status, logs).

---

## Problem Statement

Even with sandboxed, self-healing execution loops, the cluster currently relies on manual triggers (e.g. running the orchestrator command manually in a shell). To achieve a true 24/7 autonomous cluster, the orchestration layer must operate continuously in the background as a daemon. Furthermore, when an epic successfully completes validation, manual intervention is still needed to push code and merge branches. Automating branch merges and PR promotion under strict governance guidelines completes the autonomous loop.

---

## Goals

By the end of this milestone, the system must:

1. Provide a reliable, self-documenting background daemon execution model (`--daemon` mode).
2. Build an automated queue-watching and job-scheduler engine that watches `.ai-project/queue/` triggers.
3. Implement safe auto-merge hooks to automatically integrate successful Epic branches into their parent milestone branch.
4. Support clean lifecycle management commands (start, stop, status, logs) with automated CLI testing.

---

## Non-Goals

This milestone explicitly does **not** aim to:

- Provide deep integrations with systemd/init.d startup configs (local user-space background execution only).
- Support automated resolution of complex branch conflicts (any conflict halts execution, writes an escalation report, and alerts a human).
- Build external remote API controllers or network sockets for remote management.

---

## In Scope

- Process daemonization (double-forking / user-space detached process management in Python).
- Lexicographical trigger queue polling and file-watching mechanics.
- Auto-merge git promotion hooks and automation scripts calling the GitHub CLI (`gh`).
- Management command-line parameters (`ai-project-daemon start|stop|status|logs`).
- Daemon logs rotation, standard redirection, and clean PID management.
- Crash recovery and self-healing locks when the daemon gets restarted.

---

## Out of Scope

- Multi-tenant scheduling or parallel docker container executions (single-queue processing).
- Direct socket interface programming for real-time daemon messaging.

---

## Planned Epics

### Confirmed Epics

- [E13.1 — CLI Daemon Process & Control Suite](P3-M13-E13.1__spec__daemon-control-suite.md) — Implement the core python background daemon (`ai-project-daemon`) and its lifecycle commands (start, stop, status, logs).
- [E13.2 — File-Driven Trigger Discovery & Scheduler](P3-M13-E13.2__spec__trigger-discovery-scheduler.md) — Build the queue watching and schedulers that monitor the `.ai-project/queue/` folder and trigger loop runs.
- [E13.3 — Auto-Merge Git Hooks & Conflict Resolver](P3-M13-E13.3__spec__auto-merge-hooks.md) — Create git promotion hooks to automatically merge successful epic branches to milestones and handle exceptions.
- [E13.4 — Daemon Lifecycle Management & Integration Tests](P3-M13-E13.4__spec__daemon-lifecycle-tests.md) — Deliver functional tests validating clean daemon startup, graceful shutdowns, lock handling, and logs capture.

---

## Completion Criteria

Milestone M13 is complete when all Epics under M13 are completed and closed.

---

## Acceptance Criteria

- [ ] CLI daemon successfully launches, double-forks into background, and records its active PID in `.ai-project/locks/daemon.pid`.
- [ ] Queue-watching engine correctly detects triggers placed in `.ai-project/queue/` and initiates sandboxed execution.
- [ ] Successful validation runs automatically trigger git branch promotion and merge into parent branch without human intervention.
- [ ] Standard lifecycle control commands (start, stop, status, logs) are fully functional and clean.
- [ ] Abrupt termination or crashes of the daemon cleanly release files and recover state.
- [ ] Comprehensive test suite verifies daemon operations, logging, and merge scenarios successfully.

---

## Dependencies

**Internal Dependencies:**
- Milestone M12 (Containerized Sandbox & Loop Verification) must be completed and closed.

**External Dependencies:**
- GitHub CLI (`gh`) must be authenticated on the host to run auto-merges on PRs.

---

## Timeline

**Target Start:** 2026-05-24  
**Target Completion:** 2026-05-31  
**Actual Start:** 2026-05-24  
**Actual Completion:** In progress (planned)

---

## Notes

Completing M13 establishes the final automated operational baseline for Phase P3, realizing the 24/7 unattended autonomous development cluster goal.
