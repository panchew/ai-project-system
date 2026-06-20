---
type: genesis
project: taskflow
created_by: Creation Chat (facilitated by Morgan Chen, CFO)
date: 2026-06-18
phase_1_name: Core Task Management
status: complete
---

# Genesis — Taskflow

> Walkthrough artifact for Epic P4-M18-E18.1. This is a completed genesis.md for a
> fictitious task-management project ("Taskflow"), produced by filling out
> `governance/templates/genesis.md` from a blank start. All names are illustrative.

## Project Brief

**Goal:** Ship a self-hosted task management app where small teams create, assign, and
track tasks through a simple board, with no per-seat pricing.

**Problem:** Existing task tools are either bloated and expensive or too bare to manage
real team work. Small teams want a focused board they can run themselves and trust with
their data.

**Initial Team:**

| Role | Person | Authority |
|------|--------|-----------|
| CFO | Morgan Chen | Phase scope, production authorization |
| Phase Lead | Alex Rivera | Milestone planning, Epic acceptance |
| Contributor | Jamie Park | Epic implementation |
| Contributor | Sam Torres | Epic implementation |

## HQ Context Packet

- **Project:** taskflow
- **Governance path:** `.governance/` (sourced as a submodule; see start-a-project.md)
- **Phase 1 scope summary:** Deliver core task management — task CRUD, a single shared
  board with status columns, and assignment to team members. No notifications,
  integrations, or multi-board support in Phase 1.
- **Key constraints:** Self-hosted (no third-party SaaS dependency for data); Python
  backend to match team skills; first usable release within one quarter.

## Phase 1 Scope

**Name:** Core Task Management

**Goal:** A team can self-host Taskflow, create and assign tasks, and move them across a
shared board from "To Do" to "Done".

**Milestone stubs:**

- M1: Task data model and CRUD API (create, read, update, delete tasks)
- M2: Shared board with status columns and drag-to-move
- M3: Task assignment to team members and a per-assignee view

## Creation Chat Decisions

- Project name confirmed: taskflow
- Phase 1 scope accepted: yes — core task CRUD, one shared board, and assignment;
  notifications and integrations explicitly deferred to a later phase
- Team roles assigned: Morgan Chen (CFO), Alex Rivera (Phase Lead), Jamie Park and
  Sam Torres (Contributors)

## Next Step

Open a Phase Chat using
[`governance/templates/phase-execution-chat-starter.md`](../../governance/templates/phase-execution-chat-starter.md),
passing this committed `genesis.md` as the mandatory context packet. The Phase Chat
consumes the HQ Context Packet and Phase 1 Scope above to plan milestones M1–M3. No
execution begins until the Phase Chat has produced and authorized Milestone work.
