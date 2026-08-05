---
type: system
status: active
effective_date: 2026-07-20
version: 1.0.3
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

**Routing adds no status.** The five values above were reviewed against §Routing &
Origination below and needed no additions. A request that System HQ routes onward to another
governed project closes with `done` — the routing *is* the execution System HQ performed —
and its `system_response` names the routing artifact, so the trail stays followable from the
requesting project's own repo. `escalated` is likewise unchanged by routing: a review-,
merge-, or scope-shaped request is escalated to the human, **never** routed onward as though
some other project's chain could make that decision instead.

---

## Routing & Origination (normative)

This section **records practice already in use.** It adds **no authority, no decision rights,
and no new artifact type.** Every rule below describes something the desk already does; none
of it enlarges what the desk may do.

Source: the Layer-8/CFO Steering Note of 2026-07-31 (**`SN-29`**), decisions D1–D3, placed
here by HQ Ruling 2026-07-31. **The Authority Boundary above is unchanged by all of it** —
that is D4, and this amendment verified it byte-for-byte across all three documents that
reproduce it (see this version's Changelog row). The §Out of Scope pin against growth toward
a "mighty governing System Chat" (SN-21/SN-22) stands unamended.

### Routing a request onward to another governed project (D1)

The `system_request` → `system_response` pair above covers the ordinary case: project A asks,
System HQ executes, the answer is written back into A. **Some work belongs to a different
governed project B's chain.** When it does:

- A files a `system_request` in its **own** repo, as always.
- System HQ **either** executes it within the Authority Boundary, **or routes it to B via B's
  own artifact channels** — never by acting inside B on A's behalf.
- **Routing never commands.** B's chain receives *direction* and **triages it under its own
  governance**, exactly as it would any other input. Whether B acts, when, and in what scope
  are B's decisions — or the CFO's. They are not System HQ's, and not A's.

**The routed-to-B leg reuses `steering_note`; no new artifact type exists.** The reason is
load-bearing rather than incidental, and is recorded here so that it survives a later edit
that a bare rule would not:

> A `steering_note` **already encodes exactly the semantics D1 requires — direction, not
> authorization.** That is the entire content of "routing never commands." Inventing a
> `routing_request` would create an artifact whose authority semantics are **undefined on
> arrival**, so the first thing a receiving chain would have to decide is whether it must
> comply. **That question is precisely what D1 answers *no* to, and the existing type answers
> it by construction.** A new type would not merely be a larger decision — it would be a
> **worse** one.

Issuer: System HQ. Target: project B's HQ Chat. The note is filed under B's own
`steering-notes/` conventions, in B's repo.

### Requests the CFO originates (D2)

The CFO (Layer-8) may originate `system_request`s through System HQ, which **scribes** them.
Origination is the CFO's; scribing is System HQ's. **This grants the desk no ability to
initiate work of its own** — "no self-initiated work" is an Authority Boundary property and
is unchanged.

**Artifact type follows direction, not authorship:**

| Direction | Type |
|---|---|
| A project → System HQ, asking for something beyond that project's own reach | `system_request` |
| An instruction landing **in** a project, asking it to work | `steering_note` |

#### The issuer-vs-scribe rule

When System HQ writes down a request it did not originate, **the artifact records the true
issuer — Layer-8/CFO — and not the scribe. The scribing artifact MUST name both**: who issued
it, and who wrote it down.

**The reason:** if the scribe ever becomes the apparent issuer, the record loses the ability
to distinguish CFO-originated work from project-originated work — and that distinction is
what makes the request chain auditable after the fact. A reader who cannot tell which of the
two they are looking at cannot reconstruct who asked for the work.

`SN-29` is itself a clean instance of the rule it establishes: an instruction landing in a
project asking it to work, filed as a `steering_note`, with
`issuer_chat: Layer-8/CFO (scribed by System HQ at CFO instruction)` — **both parties named
in one field.** The rule was coherent in practice before it was coherent on paper, which is
the SN-21 pattern.

### Operating scope (D3)

System HQ's operating scope is **primarily config and setup.** Planned work may be involved
only in specific cases, and even then System HQ's role is **execution-only against artifact
authorization**. **Scope and acceptance decisions remain with the project's chain or the
CFO** — which is the Authority Boundary restated in the routing context, not an exception
carved into it.

### Worked example (informative)

The 2026-07-31 `social-stories-creator` case, as recorded in `SN-29`: the project filed a
ComfyUI verification request; System HQ **executed** the verification within its ordinary
tool authority, then put the resulting **remediation decisions back into the project's own
chain as a Steering Note** rather than deciding them itself. Execution was System HQ's; the
decisions were not.

**That instance is the adjacent form — route-back-to-A, not A→B** — because no governed
project B was available for it: the ComfyUI host tree `ai-stack` is unregistered. It is
offered as an illustration of the *shape* (execute what is executable; return every decision
to a chain that owns it), not as an A→B instance.

> **No true A→B routing instance has occurred yet.** Codifying a leg that has never run once
> is **a known and accepted position here, not an oversight** — D1 was practised in its
> adjacent form the same day it was decided. **The first genuine A→B routing instance should
> be recorded in this document's Changelog when it occurs.**

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
- **Fleet operator (a distinct role, not an expansion of this one):**
  `governance/systems/fleet-operator.md` — the role that operates the serialized
  local-inference lane, sequences already-authorized work within it, and keeps registered
  projects current on governance version. Recorded separately because it is **not** part of
  System HQ's authority: that document expands nothing here, and the same party may hold both
  roles without merging their boundaries.
- **Artifact Communication Protocol:** `governance/systems/artifact-communication-protocol.md`
- **Daily re-instantiation seed:** `governance/systems/system-hq-seed.md`
- **Field adoption record (informative, outside this repo):** `~/.ai-project/SYSTEM-GOVERNANCE.md`
- **Source steering note (canonization):** SN-21
  (`.ai-project/artifacts/steering-notes/2026-07-16__creation-chat__steering-note__system-hq-adoption.md`)
- **Source steering note (§Routing & Origination):** `SN-29`
  (`.ai-project/artifacts/steering-notes/2026-07-31__layer-8-cfo__steering-note__system-hq-routing-model.md`,
  D1–D4), accepted by
  `.ai-project/artifacts/rulings/2026-07-31__ai-project-system-hq__ruling__system-hq-routing-codification.md`
  (Decisions 1–6). The concern was renumbered `SN-1` → `SN-29` on 2026-08-04 (P11-M36-E36.2);
  citations of it as `SN-1` in artifacts dated on or before 2026-08-01 are correct for their date.
- **Project System Guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md`
- **AI Operating Guidelines:** `governance/AI-OPERATING-GUIDELINES.md`

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-07-20 | Initial release. Canonizes System HQ (field-adopted 2026-07-16, SN-21): the `system_request`/`system_response` schemas, storage/naming conventions, and status vocabulary (matching field usage, not reinvented); the normative Authority Boundary (execute-never-decide; `status: escalated` mandatory for review/merge/scope); and System HQ's out-of-hierarchy, cross-project, one-desk-per-machine nature. (P9-M32-E32.1) |
| 1.0.1 | 2026-07-20 | Reference section gains a back-pointer to the daily re-instantiation seed (`system-hq-seed.md`, P9-M32-E32.2), closing the one-way-only cross-reference E32.2 correctly declined to edit unilaterally. Phase-closure hygiene, not a schema or authority change. |
| 1.0.2 | 2026-07-30 | Reference section gains a back-pointer to `governance/systems/fleet-operator.md` (P10-M35-E35.1), which records the fleet-operator role as a **distinct** role. Cross-reference hygiene only: the Authority Boundary block is untouched (and therefore still word-for-word identical to its reproductions in `chat-hierarchy.md` and `system-hq-seed.md`), the §Out of Scope pin against expansion toward a "mighty governing System Chat" stands unamended, and no System HQ authority is added, removed, or reinterpreted. |
| 1.0.3 | 2026-08-04 | Adds §Routing & Origination (normative), recording `SN-29` D1–D3 as **practice already in use**: routing a request onward to another governed project B via B's own artifact channels, where **routing never commands** and B's chain triages under its own governance (D1); CFO-originated requests that System HQ **scribes**, with the **issuer-vs-scribe rule** requiring the artifact to **name both** the true issuer (Layer-8/CFO) and the scribe, because losing that distinction is what would make the request chain unauditable (D2); and the operating scope — primarily config and setup, planned work only in specific cases and then execution-only against artifact authorization (D3). **The routed-to-B leg reuses `steering_note`; no new artifact type is created**, because that type already encodes *direction, not authorization* — the whole content of "routing never commands" — and the reason is recorded in the section itself rather than left to this row. Status vocabulary reviewed against the new section and **unchanged**: routing closes with the existing `done`, and `escalated` still governs every review-, merge-, or scope-shaped request. **No authority, no decision rights, and no artifact type are added, removed, or reinterpreted.** Per D4 the Authority Boundary block is untouched and was **shown** — not assumed — byte-identical across all **three** documents that carry it (this one, `system-hq-seed.md`, and `chat-hierarchy.md`'s annex): `sha256` prefix `baecaad4dbc2146c`, 11 lines each, measured before and after the edit with the command and both outputs committed at `docs/phases/P11__Drivr_Coordination_Over_Rented_Execution/P11-M36-E36.4__authority-boundary-byte-check.md`. The §Out of Scope pin against expansion toward a "mighty governing System Chat" (SN-21/SN-22) stands unamended. **No true A→B routing instance has occurred yet — an accepted position, not an oversight; the first genuine one should be recorded in this Changelog when it occurs.** (P11-M36-E36.4) |
