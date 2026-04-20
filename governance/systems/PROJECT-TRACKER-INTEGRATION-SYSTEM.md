# PROJECT TRACKER INTEGRATION SYSTEM
*(System Reference – Canonical ↔ External Work Tracking Mapping)*

---

## 1. Purpose

This document defines how projects governed by the **Project System** integrate with
**external project trackers** such as:

- Jira
- Azure DevOps
- GitHub Projects
- Pivotal Tracker
- Trello
- Any provider exposing an API

The goal is to enable **formal, repeatable, and automatable integration** with external
trackers **without compromising the canonical project structure**.

This document is a **system reference**, not governance.

---

## 2. Canonical Project Hierarchy (Authoritative)

Internally, all projects governed by this system use the following **canonical hierarchy**:

```
Phase → Milestone → Epic
```

This hierarchy is:
- Authoritative for specifications
- Used for branching and delivery
- Used by Coding Agents for execution
- Required for completion reports

External tools MUST adapt to this model, not replace it.

---

## 3. External Tracker Hierarchies (Variable)

External trackers use different conceptual models. Examples include:

- Azure DevOps: Product Increment → Feature → User Story
- Jira: Initiative → Epic → Story / Task
- Pivotal Tracker: Release → Epic → Story
- GitHub Projects: Project → Issue → Sub-issue (often flat)
- Trello: Board → List → Card

These hierarchies are **not uniform** and MUST NOT be assumed.

---

## 4. Canonical vs Projected Model

### 4.1 Canonical Model
- Phase, Milestone, Epic
- Stable, versioned, and system-defined
- Used in specs, branches, and documentation

### 4.2 Projected Model
- Tracker-specific representation
- Defined per project
- Used only for synchronization and visibility

The projected model is a **mapping**, not a replacement.

---

## 5. Mapping Strategy (Flexible but Explicit)

Mappings are:
- **Flexible** (to accommodate organizational reality)
- **Explicit** (never inferred)
- **Declared per project**

A canonical level may map to:
- One external level
- A combination of levels
- Or, in limited cases, be omitted

Example mappings:

| Canonical | Azure DevOps | Jira |
|---------|--------------|------|
| Phase | Product Increment | Initiative |
| Milestone | Feature | Epic |
| Epic | User Story | Story |

Mappings MUST be declared before integration.

---

## 6. Project-Level Declaration (Mandatory for Integration)

Projects that integrate with a tracker MUST declare the mapping in:

```
docs/context/project-tracker.md
```

This document MUST include:
- Tracker provider
- API access method (token, app, etc.)
- Canonical ↔ external mapping table
- Sync direction (read-only, write, bidirectional)

If no declaration exists, AI MUST assume **no tracker integration**.

---

## 7. Coding Agent Responsibilities

When a tracker integration is declared, Coding Agents MAY:

- Create or update tracker items corresponding to Epics
- Sync completion state (e.g., Epic completed → external item closed)
- Validate consistency between repo state and tracker state

Coding Agents MUST:

- Never invent mappings
- Never assume tracker semantics
- Never change tracker structure without explicit instruction
- Stop execution if mapping or credentials are missing

---

## 8. Scope of Integration

This system supports, but does not require:

- Epic-level synchronization (minimum viable integration)
- Milestone or Phase rollups (optional)
- Status mirroring (optional)
- Read-only tracking (allowed)

Tracker integration MUST NOT:
- Replace Markdown specs
- Become the source of truth
- Override governance or decisions

---

## 9. Relationship to Governance

- `PROJECT-SYSTEM-GUIDELINES.md` remains authoritative
- This document defines **how integration works**, not whether it is required
- Projects opt in explicitly

---

## 10. Future Automation (Non-Normative)

Future tooling may:
- Generate tracker adapters
- Sync states automatically
- Bootstrap tracker structures from specs
- Provide CLI or web-based setup flows

Such tooling will consume this document as its contract.

---

## Closing Statement

External trackers coordinate people.

The Project System coordinates intent.

Integration translates between the two — it does not blur them.
