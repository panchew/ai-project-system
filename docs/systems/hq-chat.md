---
project: ai-project-system
phase: P1
milestone: M1
epic: null
type: system
status: active
last_updated: 2026-01-17
---

# HQ Chat (Headquarters / Control Room)

## Purpose

An **HQ Chat** (Headquarters Chat) is the **control room** for a project governed by the AI Project System.

It is responsible for:
- Defining intent
- Establishing structure
- Producing authoritative artifacts that enable execution

HQ Chats **do not execute work**.  
They define *what* should be done and *how execution is governed*.

---

## What an HQ Chat Is

An HQ Chat is a **planning, governance, and coordination surface**, typically hosted in:
- ChatGPT
- Other LLM-based chat interfaces
- Web or mobile applications

HQ Chats:
- Are long-lived
- Accumulate strategic context
- Produce durable Markdown artifacts
- Coordinate multiple Epics and Coding Agent chats

---

## What an HQ Chat Is NOT

An HQ Chat is **not**:

- A Coding Agent
- A place where code is written
- A place where branches are created
- A place where files are modified
- A substitute for documentation

HQ Chats are **declarative only**.  
They do not have filesystem or CLI access and must not be assumed to.

---

## Primary Responsibilities

An HQ Chat is responsible for producing and maintaining:

- Project vision and scope
- Phase definitions
- Milestone definitions
- Epic specifications
- System references
- Governance updates (when required)
- **Epic Execution Chat Starters**

HQ Chats ensure that **execution is possible without improvisation**.

---

## Epic Execution Chat Starters (Critical Responsibility)

Every Epic executed by a Coding Agent MUST be initiated using an
**Epic Execution Chat Starter produced by an HQ Chat**.

HQ Chats MUST:
- Produce the Epic Execution Chat Starter
- Ensure it references an existing Epic spec
- Ensure delivery requirements are explicit
- Ensure governance versions are referenced

HQ Chats MUST NOT:
- Infer or reconstruct execution contracts
- Delegate starter creation to Layer 8
- Allow Coding Agents to infer execution rules

The Epic Execution Chat Starter is a **binding execution contract**.

---

## Interaction with Coding Agents

The relationship is strictly asymmetric:

- HQ Chats define **intent and constraints**
- Coding Agents perform **execution and delivery**

HQ Chats may:
- Clarify intent
- Adjust future scope
- Respond to blocked execution

HQ Chats must NOT:
- Micro-manage execution
- Suggest implementation details during execution
- Override active execution contracts mid-Epic

---

## Typical HQ Chat Lifecycle

1. Project initialization
2. Phase definition
3. Milestone definition
4. Epic specification
5. Epic Execution Chat Starter generation
6. Oversight during execution
7. Validation of completion
8. Transition to next Epic or Milestone

HQ Chats persist across all of these steps.

---

## Standard HQ Chat Opener (Recommended)

When starting an HQ Chat for a new project, the following context should be established:

- Project name
- Repository (if applicable)
- Governance versions in use
- Current Phase (or Phase 0)
- Intended Milestone(s)
- Known constraints

This ensures continuity and prevents context drift.

---

## Relationship to Governance

HQ Chats operate under:
- `PROJECT-SYSTEM-GUIDELINES.md`
- `AI-OPERATING-GUIDELINES.md`

If an HQ Chat recommendation conflicts with governance,
**governance wins**.

HQ Chats may propose governance changes,
but those changes must be formalized in documentation.

---

## Relationship to Documentation

HQ Chats:
- Produce documentation
- Reference documentation
- Never replace documentation

If information matters after the chat ends,
it belongs in `docs/`.

---

## Closing Statement

HQ Chats are the **strategic nervous system** of the project.

They think.
They decide.
They prepare execution.

They do not execute.
