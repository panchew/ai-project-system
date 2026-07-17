---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-07-16T15:30:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-21
    severity: medium
    title: System HQ adoption in the field — formalize the system_request / system_response artifact pair and the system-level participant role
decisions:
  - "The CFO's machine adopted the framework as a system-level participant ('System HQ') on 2026-07-16 — a desk above every project's HQ, operated by the ambient AI agent at the home directory. Adoption record: ~/.ai-project/SYSTEM-GOVERNANCE.md (outside this repo). This is field usage, already live; the framework should decide whether to canonize it, not whether it may exist."
  - "Two new artifact types are in field use: system_request (project → system, written to the project's own .ai-project/artifacts/system-requests/) and system_response (system → project, .ai-project/artifacts/system-responses/). Both follow the Artifact Communication Protocol's frontmatter+body and immutability rules."
  - "Discovery rides the existing read-only MCP bridge (ai-project-system-mcp): list_governance_state indexes artifact directories by name, so the new types were picked up with zero code changes. The bridge registry was expanded from 1 to all 8 governed projects on this machine."
  - "This note proposes, it does not scope. P8 is already scoped to visual-artifacts activation (SN-20, 2026-07-14) and this does not join it. Canonization is a candidate for P9 or a standalone reconciliation epic, at HQ's triage."
---

# Creation Chat Steering Note — System HQ Adoption in the Field

> **Provenance:** Drafted by the system-level agent operating under
> `~/.ai-project/SYSTEM-GOVERNANCE.md`, at the CFO's direction, to route this
> proposal through the framework's own governance process rather than editing
> framework docs directly. The CFO has authorized filing this note; the
> decisions below describe what already exists in the field, and the concern is
> a proposal for HQ triage, not a directive.

## Purpose

On 2026-07-16 the CFO's machine adopted the framework as a **system-level
participant** — "System HQ," a desk above every project's HQ Chat. Any governed
project can now request things that exceed its own authority or reach
(environment changes, cross-project work, research, infrastructure) by filing a
`system_request` artifact in its own repo; the ambient system agent handles the
request within its tool authority and answers with a `system_response` artifact.

This pattern extends the Artifact Communication Protocol upward past the
project boundary. It works today with zero framework changes — which is exactly
why it should be surfaced here: the framework has a working extension point it
never named, and field usage is now ahead of the written framework.

---

## Concerns for HQ Triage

### SN-21 — Formalize the system-level participant and its artifact pair [MEDIUM]

**Detail:** The following exists in the field, undocumented by the framework:

1. **A participant level above HQ that is not the Creation Chat.** The chat
   hierarchy (`governance/systems/chat-hierarchy.md`) tops out at Level 0
   (Creation Chat) *within a project*. System HQ is orthogonal: one desk per
   *machine*, spanning all governed projects on it, executing requests rather
   than steering vision. It is closest in spirit to Layer-8/CFO support staff:
   it may execute within tool authority but may not make review decisions,
   merge authorizations, or scope changes — those escalate to the human.

2. **Two artifact types**, following the protocol's existing rules
   (frontmatter + body, ISO-8601 UTC timestamps, immutability, versioned
   follow-ups):
   - `system_request` — written by any chat of a governed project to its own
     `.ai-project/artifacts/system-requests/`; carries `status: pending |
     in_progress | done | declined | escalated` and a Definition of Done.
   - `system_response` — written back by the system agent to
     `.ai-project/artifacts/system-responses/`; references the request's
     timestamp; serves as the authoritative closure record.

3. **A discovery mechanism** — the `ai-project-system-mcp` read-only bridge.
   Because `list_governance_state` indexes artifact directories by name, the
   new types surfaced without any code change. Pickup is on-demand (the CFO
   asks the system agent to sweep for `status: pending`); no daemon required.

**Required action:** HQ triages whether and how to canonize:
1. Add the `system_request` / `system_response` schemas to the Artifact
   Communication Protocol (or a companion system-participant document), with
   the storage and naming conventions above.
2. Decide where the system-level participant sits in `chat-hierarchy.md` —
   a new level, an annex, or explicitly out-of-hierarchy with a pointer.
3. Record the authority boundary: system agents execute, humans decide;
   `status: escalated` is the mandatory answer for review/merge/scope requests.
4. Timing is HQ's call — candidate for P9 scoping or a standalone epic. Not P8.

---

## Decisions Already Made

Field facts, not for HQ to re-debate (they describe the CFO's machine, outside
this repo's jurisdiction):

1. **System HQ is live** on the CFO's machine as of 2026-07-16, recorded at
   `~/.ai-project/SYSTEM-GOVERNANCE.md`, framework version v6.0.0. That record
   explicitly yields to PSG/AOG on conflict.
2. **The MCP bridge registry** (`ai-project-system-mcp/registry.yml`) now
   registers all 8 governed projects on the machine, up from 1.
3. **Every registered project** has `system-requests/` and `system-responses/`
   artifact directories scaffolded.

---

## Carry-Over Open Items

Non-blocking, for later triage:

1. **Write path.** The MCP bridge is deliberately read-only (Phase P1 scope);
   `system_response` artifacts are currently written by direct file access,
   which only works because the system agent lives on the same machine. If
   System HQ ever operates remotely, the bridge needs a scoped write tool —
   that is ai-project-system-mcp's roadmap territory, not this repo's.
2. **Volume.** Pickup is on-demand today. If request volume grows, a scheduled
   sweep (cron/daemon) becomes worth defining — including SLA expectations,
   which the Bugfix Workflow already has precedent for.

---

## Next Action

HQ Chat should:

1. Acknowledge SN-21 and record it in the triage queue — no P8 impact.
2. When scoping P9 (or a standalone epic), decide canonize-vs-observe: adopt
   the schemas into the protocol now, or let the field pattern accumulate more
   usage first and revisit.
3. Keep the SN-20 P8 spine untouched.
