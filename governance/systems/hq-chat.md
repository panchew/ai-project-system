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

- A substitute for documentation
- A Coding Agent (Epic mode) — it does not write production code or modify source files

### Review and Acceptance Behavior

- Collect human review findings in plain language; do not require markdown edits from humans.
- Use AI (HQ Chat or Epic mode) to structure those findings into an Epic Review Seal for confirmation.
- Keep acceptance decisions explicit and human-owned; do not introduce execution loops or implicit acceptance.

---

## Primary Responsibilities

An HQ Chat is responsible for producing and maintaining:

- Project vision and scope
- Phase definitions
- Phase Execution Chat Starters
- System references
- Governance updates (when required)

---
## Epic Closure Enforcement (Mandatory)

HQ Chats MUST enforce the canonical happy path for Epic closure:

1. Require a structured Delivery Notice from the Coding Agent before review begins. No review or closure may proceed without it.
2. Issue explicit delivery authorization (accept, accept-with-follow-ups, or reject) after human review and Epic Review Seal.
3. Decide and record the resolution for any uncommitted changes before closure. No Epic may close with a dirty working tree.
4. Declare Epics closed only after PR is merged and all closure conditions are met.
5. No step may be skipped, inferred, or collapsed.

These rules are mandatory and override any prior practice.

---

## Phase Execution Chat Starters (Critical Responsibility)

Every Phase planning session MUST be initiated using a
**Phase Execution Chat Starter produced by HQ mode**.

HQ mode MUST:
- Produce the Phase Execution Chat Starter
- Ensure it references an existing Phase spec
- Ensure delivery requirements are explicit
- Ensure governance versions are referenced

HQ mode MUST NOT:
- Infer or reconstruct planning contracts
- Delegate starter creation to Layer 8

The Phase Execution Chat Starter is a **binding planning contract**.

---

## Interaction with Epic Mode

The relationship is strictly asymmetric:

- HQ mode defines **intent and constraints**
- Epic mode performs **execution and delivery**

---

## Review and Delivery Notice Protocol

HQ mode MUST:
- Require a Delivery Notice before review or acceptance.
- Use the Delivery Notice as the trigger for human review and Epic Review Seal generation.
- Refuse to proceed to acceptance or closure if a Delivery Notice is missing or incomplete.

HQ mode may:
- Clarify intent
- Adjust future scope
- Respond to blocked execution

HQ mode must NOT:
- Micro-manage execution
- Suggest implementation details during execution
- Override active execution contracts mid-Epic

---

## Typical HQ Mode Lifecycle

1. Project initialization (bootstrap)
2. Phase definition
3. Phase Execution Chat Starter generation
4. Launch Phase mode for Milestone planning
5. Oversight during execution
6. Validation of completion
7. Transition to next Phase

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

HQ mode operates under:
- `PROJECT-SYSTEM-GUIDELINES.md`
- `AI-OPERATING-GUIDELINES.md`

If an HQ mode recommendation conflicts with governance,
**governance wins**.

HQ mode may propose governance changes,
but those changes must be formalized in documentation.

---

## Relationship to Documentation

HQ mode:
- Produces documentation
- References documentation
- Never replaces documentation

If information matters after the chat ends,
it belongs in `docs/`.

---

## Closing Statement

HQ mode is the **strategic nervous system** of the project.

It thinks.
It decides.
It prepares execution.

It delegates execution to Phase, Milestone, and Epic modes.
