# AI OPERATING GUIDELINES
*(Authoritative AI Usage Policy)*

---

## 1. Execution Authority

Coding Agents MUST treat the Epic Execution Chat Starter as a **binding execution contract**.

Governance and specs are authoritative references, but the execution chat starter defines:
- What is being executed
- What branch is used
- Where delivery occurs
- When the agent is allowed to stop

---

## 2. Delivery Enforcement

Coding Agents MUST:

- Commit all work to the epic branch specified in the chat starter
- Open a pull request against the explicitly stated target branch
- Refuse to complete execution if delivery requirements are missing or violated
- Default to **pausing for clarification**, not guessing

---

## 3. Exit Ritual

An Epic execution chat concludes only when:

1. Definition of Done is satisfied
2. Delivery requirements are fulfilled
3. Epic Completion Report is produced and committed
4. Agent explicitly declares the Epic complete

---

## Closing Statement

If delivery is ambiguous, execution must stop.
