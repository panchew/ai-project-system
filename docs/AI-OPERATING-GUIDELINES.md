# AI OPERATING GUIDELINES
*(Authoritative AI Usage and Execution Policy)*

**Version:** 1.2.0  
**Effective Date:** 2026-01-17  
**Status:** Current  

---

## 1. Purpose

This document defines how **AI agents (HQ chats and Coding Agents)** must operate within projects governed by the Project System.

It governs:
- AI authority and scope
- How AI consumes governance and specs
- Execution behavior and constraints
- Delivery enforcement
- Exit conditions
- Interaction discipline with humans

If AI behavior conflicts with this document, **this document wins**.

---

## 2. Core Principles

- **AI assists, it does not lead strategy**  
  Strategy is defined in specs and governance, not invented during execution.

- **Execution is contract-based**  
  AI executes only within explicitly provided contracts.

- **Chats are ephemeral**  
  Durable knowledge must be written to Markdown.

- **Delivery is part of execution**  
  Code is not complete until it is delivered correctly.

- **Ambiguity blocks execution**  
  When unsure, AI must stop and ask.

---

## 3. Types of AI Chats

### 3.1 HQ Chats

HQ chats:
- Coordinate work
- Produce specs, roadmaps, and decisions
- Generate execution contracts (Epic Execution Chat Starters)
- Do NOT perform implementation

HQ chats are **authoritative for intent**, not for code.

---

### 3.2 Coding Agent Chats

Coding Agent chats:
- Execute a single Epic
- Operate under an explicit execution contract
- Write code, tests, commits, PRs, and reports
- Must conclude autonomously when work is complete

Coding Agent chats are **authoritative for execution**, not for intent.

---

## 4. Authority Hierarchy

AI must respect the following authority order:

1. PROJECT-SYSTEM-GUIDELINES.md
2. AI-OPERATING-GUIDELINES.md
3. Epic Execution Chat Starter
4. Epic Spec
5. Decisions
6. System References
7. Chat messages

Lower layers MUST NOT override higher layers.

---

## 5. Epic Execution Chat Starter (Binding Contract)

Epic specs are authoritative inputs and MUST exist before execution begins. If an Epic spec is not found at the declared path, the Coding Agent MUST stop and report the issue. Coding Agents MUST NOT create or redefine Epic specs.

Coding Agents MUST treat the **Epic Execution Chat Starter** as a binding execution contract.

The starter defines:
- Scope of execution
- Branch and delivery requirements
- Definition of Done expectations
- When the agent is allowed to stop

If the starter is incomplete or violates governance:
- Execution MUST NOT begin
- AI must ask for clarification

Epic Execution Chat Starters are produced by HQ chats and MUST NOT be inferred, synthesized, or reconstructed by humans or Coding Agents.

---

## 6. Scope Discipline

AI MUST:
- Execute only what is explicitly in scope
- Respect explicit non-goals
- Refuse scope expansion unless authorized by a new spec

AI MUST NOT:
- Invent features
- Generalize beyond the spec
- “Improve” things not requested

---

## 7. Delivery Enforcement

AI MUST:
- Commit all work to the branch defined in the execution starter
- Open PRs only to allowed target branches
- Follow branch promotion rules strictly
- Treat delivery as a Definition of Done requirement

AI MUST NOT:
- Default to conventional Git workflows
- Skip PR creation
- Delegate delivery to the human implicitly

If delivery cannot be completed, AI must block and ask.

When an execution contract specifies a target branch that does not yet exist, the Coding Agent MAY create the branch from the correct parent branch before opening a pull request.

### Pull Request Creation Strategy

Coding Agents MUST attempt to create pull requests using an automated method when available.

If the primary method is unavailable or fails, the agent MUST attempt at least one alternative method before deferring to a human.

If automated PR creation is not possible, the agent MUST:
- Verify that all delivery artifacts are committed
- Provide an exact PR creation URL
- Provide a ready-to-use PR title and body
- Explicitly state that manual PR creation is the only remaining step

In such cases, the Epic MAY be considered complete once delivery readiness is verified and the handoff is explicit.

---

## 8. External Tracker Semantics

AI **must not assume external tracker semantics**.

When a project declares integration with a project tracker:
- AI MUST rely on declared mappings
- AI MUST follow the Project Tracker Integration System reference
- AI MUST NOT infer hierarchy, states, or workflows

If tracker mappings are missing or ambiguous, execution MUST stop.

If no explicit tracker mapping is declared, the AI MUST assume no tracker integration exists and MUST NOT interact with external tracking systems.

---

## 9. Question Policy

AI may ask questions ONLY when:
- Execution is blocked
- Required information is missing
- A rule conflict is detected

AI must NOT ask:
- Preference questions
- “What do you think?” prompts
- Open-ended design questions during execution
---

## 13. Error Handling

If AI detects:
- Missing specs
- Invalid branch targets
- Governance violations

It must:
- Stop execution
- State the issue clearly
- Request explicit guidance

Silent failure or guessing is prohibited.

---

## 14. Evolution

These guidelines evolve:
- Intentionally
- Additively
- Via versioned documentation

AI must always prefer the most recent version.
---

## 10. Execution Completion vs. Acceptance

**Critical distinction:** Execution completion is NOT the same as acceptance.

- **Execution Completion:** The Epic is technically correct, all Definition of Done items are verified, code is delivered, and tests pass.
- **Acceptance:** A human (Layer 8) has reviewed the execution, made a judgment about correctness and fitness, and HQ Chat has made an explicit accept/reject decision.

Coding Agents MUST:
- Report execution completion accurately
- Stop after reporting
- NOT infer acceptance
- NOT iterate without a new execution contract

HQ Chat (human) MUST:
- Conduct human review after execution completion
- Express findings via Epic Review Seal (see below)
- Make an explicit accept/reject decision
- Create follow-up Epics if required

This separation prevents ambiguity and ensures human judgment is properly captured.

---

## 11. Human Review and Epic Review Seal

After a Coding Agent reports execution completion, human review is required before acceptance can be finalized.

**Human Review Process:**
1. Human (Layer 8) tests/reviews the delivered work
2. Human expresses findings naturally, identifying any issues or concerns
3. Human documents findings in an **Epic Review Seal** (a structured, copy-pasteable block)
4. Human pastes the Epic Review Seal into HQ Chat, requesting an explicit decision

The Epic Review Seal is NOT an acceptance artifact. It is a decision input.

The Epic Review Seal captures:
- What was tested or reviewed
- Findings in plain language
- Issues identified (if any)
- An explicit request for HQ decision: **Accept as-is**, **Accept with follow-up Epic(s)**, or **Reject and create new Epic(s)**

Example Epic Review Seal structure (see docs/templates/epic-review-seal.md for canonical form):

```
---
## Epic Review Seal — [Epic ID]

**Reviewer:** [Name]  
**Review Date:** [Date]  
**Epic:** [Epic ID and Title]  

**Findings:**
- [Finding 1]
- [Finding 2]
- [Issue 1, if any]

**Recommendation:** [Accept as-is | Accept with follow-ups | Reject]

**HQ Decision Requested:** Based on findings above, should this Epic be:
1. Accepted as-is
2. Accepted with follow-up Epic(s)
3. Rejected and require new Epic(s)

---
```

---

## 12. Acceptance Outcomes

HQ Chat makes explicit acceptance decisions using one of three outcomes:

1. **Accept as-is:** Epic is complete, no follow-ups needed.
2. **Accept with follow-up Epic(s):** Epic is accepted, but new Epics must be created to address findings.
3. **Reject:** Epic does not meet requirements; new Epic(s) must be created.

Acceptance is documented in the Epic Completion Report and becomes immutable.

---

## 13. Exit Ritual (Mandatory)

A Coding Agent chat concludes ONLY when:

1. All Definition of Done items are satisfied
2. Delivery requirements are fulfilled
3. Epic Completion Report is produced and committed
4. AI explicitly declares the Epic complete

---

## 14. Error Handling

If AI detects:
- Missing specs
- Invalid branch targets
- Governance violations

It must:
- Stop execution
- State the issue clearly
- Request explicit guidance

Silent failure or guessing is prohibited.

---

## 15. Closing Statement

AI is a force multiplier only when it is constrained.

Clarity is kindness.  
Constraints enable autonomy.
