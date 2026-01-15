# AI OPERATING GUIDELINES
*(Authoritative AI Usage Policy)*

---

## 1. Purpose

This document defines **how AI tools are used within a project**.

It governs:
- HQ chats
- Execution chats
- Coding Agents
- Context handling
- The relationship between chats and documentation

If AI behavior conflicts with this document, **this document wins**.

---

## 2. Core Principles

- **Chats are ephemeral**  
  AI chats are execution tools, not memory systems.

- **Markdown is the source of truth**  
  Durable knowledge lives in versioned Markdown files.

- **Context is explicit and externalized**  
  AI effectiveness depends on provided context, not chat history.

---

## 3. Chat Architecture

### 3.1 HQ Chat

Each project has exactly **one HQ chat**.

**Purpose**
- Governance
- Planning
- Roadmaps
- Architectural direction
- System-level decisions

**Rules**
- No code execution
- No implementation details
- Decisions must be recorded in Markdown to be authoritative

---

### 3.2 Execution Chats

Execution chats are used for **doing work**.

**Rules**
- One Epic per chat
- Strictly scoped
- Terminated when the Epic is complete
- Must begin with a Mandatory Context Packet

Execution chats include:
- ChatGPT execution chats
- GitHub Copilot Chat sessions
- Any AI-assisted coding interaction

---

## 4. Mandatory Context Packet

Every execution chat MUST begin with a **Mandatory Context Packet**.

The packet is **derived from document front-matter**, not invented.

### Canonical Format

```md
# Project Context
Project: <project-name>
Repository: <repo-name>

# Current Scope
Phase: P<id> – <name>
Milestone: M<id> – <name>
Epic: E<id> – <name>

# Goal of This Increment
<Clear, testable objective>

# Constraints
- Tech stack:
- Architectural rules:
- Explicit non-goals:

# Authoritative Documents
- Epic Spec: <path>
- Decisions: <path(s)>
```

---

## 5. Coding Agent Rules

Coding Agents MUST:

- Stay strictly within Epic scope
- Make small, incremental, reversible changes
- Avoid speculative refactors
- Ask before introducing new abstractions
- Respect authoritative documents over chat instructions

Coding Agents MUST NOT:

- Expand scope
- Modify unrelated code
- Invent requirements
- Bypass documentation

---

## 6. Enforcement

Authority order:

1. Governance documents
2. Specs and decisions
3. This document
4. Chat instructions
5. AI assumptions

If a conflict exists, **the higher authority wins**.

---

## Closing Statement

AI is treated as a **short-lived cognitive worker**.

Structure enables intelligence.
