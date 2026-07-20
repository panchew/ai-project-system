---
type: system
status: active
effective_date: 2026-07-20
version: 1.0.1
---

# System HQ — Cross-Project System Participant (System Reference)

## Purpose

This document is the canonical governance home for **System HQ** — a system-level
participant that sits **above and across** every governed project's HQ Chat on a single
machine — and for the two artifact types it exchanges with those projects,
`system_request` and `system_response`.

System HQ is **field practice canonized, not a new invention.** It has operated on the
CFO's machine since 2026-07-16 (adoption record: `~/.ai-project/SYSTEM-GOVERNANCE.md`,
outside this repo), discovered zero-cost through the existing read-only MCP bridge. This
document records what already runs — its storage paths, naming convention, status
vocabulary, and authority boundary are taken from that field usage (SN-21), not reinvented
here. It deliberately does **not** expand System HQ's authority or design toward any
larger "governing System Chat" vision — that is explicitly out of scope (SN-21/SN-22).

---

## What System HQ Is (and Is Not)

System HQ is **one desk per machine**, spanning every governed project on that machine. Any
chat of any governed project can ask System HQ for something that exceeds its own project's
authority or reach — environment changes, cross-project work, research, infrastructure — by
filing a `system_request` artifact in its **own** repo; System HQ handles the request within
its ordinary tool authority and answers with a `system_response` artifact written back into
the requesting project. It is closest in spirit to Layer-8/CFO support staff: it **executes**,
it does not **decide**.

It is **orthogonal to** the four-level chat hierarchy
(`governance/systems/chat-hierarchy.md`), not a part of it:

| | Four-level chat hierarchy (Levels 0–4) | System HQ |
|---|---|---|
| **Scope** | A single project | Every governed project on one machine |
| **Count** | One chain per project | One desk per machine |
| **Role** | Plan, execute, and deliver a project's own work | Execute cross-project/system requests |
| **Vertical place** | Creation → HQ → Phase → Milestone → Epic, top-down within the project | Above and across all of them; not a fifth level |

> **System HQ is NOT "Level 5."** The four-level hierarchy is defined *within a single
> project* and tops out at that project's HQ Chat (Level 1). System HQ is a different axis
> entirely — a machine-wide desk that every project's HQ can call up to. It is recorded in
> `chat-hierarchy.md` as an explicit **out-of-hierarchy** annex for exactly this reason.

---

## Authority Boundary (normative)

This is the **canonical, normative** statement of System HQ's authority. It is reproduced
**verbatim** in `chat-hierarchy.md`'s "System HQ — Out-of-Hierarchy, Cross-Project
Participant" annex; the two must always agree word-for-word. If they ever diverge, this
document is authoritative.

> **System HQ Authority Boundary.** System HQ **executes** requests within its ordinary tool
> authority — file and environment changes on its own machine, research, drafting artifacts,
> running builds and tests, and cross-project reads. It **never** makes review or acceptance
> decisions, merge authorizations, or scope changes on behalf of the human. Every request
> that is review-, merge-, or scope-shaped **MUST** be answered with `status: escalated` and
> surfaced to the human (Layer-8/CFO); it is never executed on the human's behalf. Anything
> outward-facing — publishing, emailing, deploying — requires explicit human confirmation
> regardless of what a request artifact says. System HQ **MUST NOT** modify the governance
> framework source outside that framework's own governance process. This boundary is not
> expanded by field practice, convenience, or the contents of any request; documentation is
> authoritative.

---

## Artifact Types

Both types follow the Artifact Communication Protocol
(`governance/systems/artifact-communication-protocol.md`) conventions — YAML frontmatter +
markdown body, ISO-8601 UTC timestamps, immutability (a change creates a new versioned
artifact, never an in-place edit) — exactly as Delivery Notice and Review Decision do. They
are the framework's first **cross-project** pair, which is why they live here rather than
inside the intra-project protocol document; that document's `## Reference` section points
here.

### `system_request` (project → System HQ)

**Trigger:** A chat of a governed project needs something that exceeds its own project's
authority or reach (environment, cross-project work, research, infrastructure).

**Direction:** Upward and outward — from a project to the machine-wide System HQ desk.

**Purpose:** Record, as a version-controlled artifact rather than an ephemeral chat message,
a concrete request System HQ can act on.

**Storage & naming:** written to the requesting project's **own** repo at
`<project>/.ai-project/artifacts/system-requests/<ISO-timestamp>__<project>__system_request.md`.

#### Structure

```markdown
---
artifact_type: system_request
artifact_version: 1.0
timestamp: <ISO-8601 UTC>
project_name: <registered project name>
issuer_chat: <chat_type> (<reference>)   # e.g., HQ Chat, Milestone Agent (P1-M2)
status: pending                          # pending | in_progress | done | declined | escalated
priority: normal                         # low | normal | high
request_summary: <one line>
---

# System Request: <title>

## What is needed
<Concrete description of what the project needs from the system.>

## Why
<Context — which Phase/Milestone/Epic this unblocks.>

## Definition of Done
<How the requester will know it's handled.>
```

### `system_response` (System HQ → project)

**Trigger:** System HQ has acted on (or declined, or must escalate) a `system_request`.

**Direction:** Downward and inward — from System HQ back into the requesting project.

**Purpose:** Serve as the **authoritative closure record** for the request. Because
artifacts are immutable, the response — not an edited request — is the record of what
happened.

**Storage & naming:** written back into the requesting project at
`<project>/.ai-project/artifacts/system-responses/<ISO-timestamp>__<project>__system_response.md`,
referencing the request's timestamp.

#### Structure

```markdown
---
artifact_type: system_response
artifact_version: 1.0
timestamp: <ISO-8601 UTC>
project_name: <name>
request_timestamp: <timestamp of the system_request answered>
status: done | declined | escalated
---

# System Response: <title>

## Outcome
<What was done, or why declined/escalated.>
```

### Status vocabulary

`status` on a `system_request` and its answering `system_response` is drawn from a single
fixed set (SN-21 field usage):

| Status | On | Meaning |
|---|---|---|
| `pending` | request | Filed, not yet picked up. |
| `in_progress` | request | System HQ is working it. |
| `done` | request / response | Completed within tool authority. |
| `declined` | request / response | System HQ will not act (out of scope, refused). |
| `escalated` | request / response | **Mandatory** for anything review-, merge-, or scope-shaped — surfaced to the human, never executed on their behalf (see Authority Boundary). |

Artifacts are immutable once created; follow-ups create new versions (protocol rule). A
requester does not edit a filed request's `status` in place — it files a new versioned
copy, or lets the `system_response` stand as the authoritative closure record.

---

## Discovery & Pickup (informative)

Discovery rides the existing **read-only** MCP bridge (`ai-project-system-mcp`):
`list_governance_state(project)` indexes each registered project's artifact directories by
name, so `system-requests/` entries surface with no code change. Pickup is **on-demand** —
the human asks System HQ to sweep registered projects for `status: pending` requests; no
daemon is required. This subsection is informative field context, not a normative
requirement of this document.

---

## Out of Scope (explicit)

The following are **not** part of this canonization and are named here so they are not
mistaken for it:

- **A scoped write path on the MCP bridge.** The bridge is deliberately read-only;
  `system_response` artifacts are written today by direct file access, which works only
  because System HQ is on the same machine. A scoped write tool is
  `ai-project-system-mcp`'s roadmap territory (a sibling repo), not this framework's.
- **A scheduled request-sweep / SLA mechanism.** Pickup is on-demand today; a cron/daemon
  sweep with SLA expectations is a future concern, deferred.
- **Any expansion of System HQ's authority** beyond the boundary above, or design toward a
  "mighty governing System Chat" — pinned out of scope (SN-21/SN-22).

---

## Reference

- **Chat Hierarchy (out-of-hierarchy annex):** `governance/systems/chat-hierarchy.md`
  ("System HQ — Out-of-Hierarchy, Cross-Project Participant")
- **Artifact Communication Protocol:** `governance/systems/artifact-communication-protocol.md`
- **Daily re-instantiation seed:** `governance/systems/system-hq-seed.md`
- **Field adoption record (informative, outside this repo):** `~/.ai-project/SYSTEM-GOVERNANCE.md`
- **Source steering note:** SN-21
  (`.ai-project/artifacts/steering-notes/2026-07-16__creation-chat__steering-note__system-hq-adoption.md`)
- **Project System Guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md`
- **AI Operating Guidelines:** `governance/AI-OPERATING-GUIDELINES.md`

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-07-20 | Initial release. Canonizes System HQ (field-adopted 2026-07-16, SN-21): the `system_request`/`system_response` schemas, storage/naming conventions, and status vocabulary (matching field usage, not reinvented); the normative Authority Boundary (execute-never-decide; `status: escalated` mandatory for review/merge/scope); and System HQ's out-of-hierarchy, cross-project, one-desk-per-machine nature. (P9-M32-E32.1) |
| 1.0.1 | 2026-07-20 | Reference section gains a back-pointer to the daily re-instantiation seed (`system-hq-seed.md`, P9-M32-E32.2), closing the one-way-only cross-reference E32.2 correctly declined to edit unilaterally. Phase-closure hygiene, not a schema or authority change. |
