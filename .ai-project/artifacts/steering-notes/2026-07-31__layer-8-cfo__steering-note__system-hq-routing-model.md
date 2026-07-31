---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-07-31T20:37:49Z
issuer_chat: Layer-8/CFO (scribed by System HQ at CFO instruction)
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-1
    severity: medium
    title: "system-hq.md records only the request→response pair; routing and human-originated requests are unrecorded field practice"
decisions:
  - "D1: When governed project A needs something from governed project B, A files a system_request; System HQ either executes it within the Authority Boundary or routes it to B via B's own artifact channels. Routing never commands — B's chain triages under its own governance."
  - "D2: The CFO (Layer-8) may originate system_requests through System HQ; System HQ scribes them and the artifact records the true issuer (Layer-8/CFO). Artifact type follows direction: a request from a project to System HQ is a system_request; an instruction landing in a project asking it to work is a steering_note."
  - "D3: System HQ's operating scope is primarily config and setup. Planned work may be involved only in specific cases, and even then System HQ's role is execution-only against artifact authorization; scope and acceptance decisions remain with the project's chain or the CFO."
  - "D4: The System HQ Authority Boundary (system-hq.md §Authority Boundary) is unchanged verbatim by all of the above — no review/merge/scope decisions, mandatory escalation shapes, outward-facing confirmation rule, and no self-initiated work all stand."
---

# Steering Note — Layer-8/CFO to HQ Chat (ai-project-system)

## Purpose

This note hands the ai-project-system chain a set of binding CFO decisions
about how System HQ operates, made during a System HQ session on 2026-07-31
that handled `social-stories-creator`'s ComfyUI verification request. The
model below was **practiced in the field that day** (System HQ executed the
verification, then routed remediation decisions back into the project's own
chain via Steering Note — the same practice-then-canonize path SN-21 took for
System HQ itself). The required codification is small: record the routing flow
and human-originated requests in `governance/systems/system-hq.md` (and any
word-for-word reproductions that must agree), leaving the Authority Boundary
untouched.

---

## Concerns for HQ Triage

### SN-1 — Routing and human-originated requests are unrecorded field practice [MEDIUM]

**Detail:** `governance/systems/system-hq.md` (v1.0.2) defines System HQ as
answering a `system_request` with a `system_response` written back into the
**requesting** project, and Rule 7 of `system-hq-seed.md` sanctions "a
Steering Note into the relevant project" only in the re-instantiation context.
Two behaviors the CFO has now decided are part of the desk's normal operation
are not recorded anywhere normative: (a) routing a request onward to a
*different* governed project B when the work belongs to B's chain, and (b) the
CFO originating `system_request`s through System HQ as scribe. Today's field
usage (2026-07-31, social-stories-creator ComfyUI M2) exercised the adjacent
mechanics — execution plus a System HQ-issued Steering Note into the
requesting project — and the model was affirmed by the CFO in session.

**Required action:** Scope and land an amendment to
`governance/systems/system-hq.md` through this repo's own governance process
that records D1–D3 as normal operation (likely: a short "Routing & Origination"
section plus status-vocabulary/changelog hygiene; check `chat-hierarchy.md`'s
out-of-hierarchy annex and `system-hq-seed.md` for reproductions that must
stay in agreement). **The Authority Boundary block must remain verbatim
identical across all three documents — D4 pins it untouched.** If the
amendment wants a named artifact for the routed-to-B leg, prefer reusing
`steering_note` (issuer: System HQ; target: B's HQ Chat) over inventing a new
type; a new type would be a separate, larger decision.

---

## Decisions Already Made

1. **D1 — Routing model.** When governed project A needs something from
   governed project B, A files a `system_request`; System HQ either executes
   it within the Authority Boundary or routes it to B via B's own artifact
   channels. Routing never commands — B's chain triages under its own
   governance.
2. **D2 — Human-originated requests.** The CFO (Layer-8) may originate
   `system_request`s through System HQ; System HQ scribes them and the
   artifact records the true issuer (Layer-8/CFO). Artifact type follows
   direction: project → System HQ is a `system_request`; an instruction
   landing in a project asking it to work is a `steering_note`.
3. **D3 — Operating scope.** Primarily config and setup. Planned work only in
   specific cases, and then execution-only against artifact authorization;
   scope and acceptance decisions remain with the project's chain or the CFO.
4. **D4 — Boundary frozen.** The Authority Boundary
   (`system-hq.md` §Authority Boundary) is unchanged verbatim by D1–D3.

---

## Carry-Over Open Items

1. Whether A→B routing wants a worked example added to `system-hq.md`'s
   informative sections once the normative text lands (today's
   social-stories-creator case is available as the reference instance).
2. No governed project B existed on this machine at decision time for the
   concrete case (the ComfyUI host tree, `ai-stack`, is unregistered) — the
   routing leg was exercised as route-back-to-A instead. First true A→B
   routing instance should be noted in the changelog when it occurs.

---

## Next Action

HQ Chat (ai-project-system) should:
1. Triage this note and place the codification in the appropriate
   phase/milestone (a documentation amendment of `system-hq.md` + agreement
   check of its two reproductions; Authority Boundary verbatim per D4).
2. Keep the amendment minimal — record D1–D3 as practice already in use; do
   not expand System HQ authority (the SN-21/SN-22 "mighty governing System
   Chat" pin stands).
3. On merge/closure, note this note as the source (the SN-21 pattern:
   field practice → Steering Note → canon).
