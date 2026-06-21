---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-06-20T20:00:00Z
issuer_chat: Phase Chat (P4)
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-10
    severity: low
    title: Creation Chat role definition placed at unreviewed path during Phase P4 closure merge
decisions:
  - The M18 genesis.md project-setup template is the authoritative content at governance/templates/genesis.md; 226/226 tests pass confirming this.
  - The CFO's Creation Chat role definition (from the 'claude takes over' master commit) is preserved at governance/systems/creation-chat-role.md pending HQ placement decision.
---

# Phase Chat Steering Note — Phase P4 Closure

## Purpose

During Phase P4 closure, a merge conflict arose between two different files both living
at `governance/templates/genesis.md`. The resolution preserved both files but placed the
CFO's version at a path the CFO did not choose. HQ Chat should confirm or redirect the
placement before the CFO next opens a Creation Chat session.

---

## Concerns for HQ Triage

### SN-10 — Creation Chat role definition at unreviewed path

**Severity:** Low (no test failures; no blocked workflows; cosmetic until CFO opens next session)

**What happened:**

The CFO's "claude takes over" commit (master, `1914abd`) added
`governance/templates/genesis.md` with a rich **Creation Chat role definition** — the
"You are the Creation Chat" operating manual with five Rules of Engagement, re-instantiation
notes, and ongoing-oversight guidance.

M18-E18.1 (phase/P4) also added `governance/templates/genesis.md` with a **project setup
template** — a fill-in-the-blank form (`type: genesis`, `status: draft`, Project Brief /
HQ Context Packet / Phase 1 Scope sections) validated by `tests/test_genesis_template.py`.

During the `phase/P4 → master` merge, both files collided (add/add conflict). Phase Chat
initially kept the CFO's version; this broke 5 genesis template tests. Phase Chat then
restored the M18 template to `governance/templates/genesis.md` (tests pass) and saved the
CFO's Creation Chat role definition to:

```
governance/systems/creation-chat-role.md
```

This path was Phase Chat's choice, not the CFO's.

**Required action from HQ:**

Confirm one of the following:

1. `governance/systems/creation-chat-role.md` is the correct permanent home — no further action.
2. The CFO's version should replace `governance/templates/genesis.md` — update the test suite
   to validate the new schema and retire the M18 template, or rename the M18 template.
3. The CFO's version should live elsewhere — HQ Chat to rename it and commit.

**What the file contains (for reference):**
`governance/systems/creation-chat-role.md` — YAML front-matter `artifact_type: genesis`,
`artifact_version: 1.0`; five Rules of Engagement; "What to Do Right Now" section; "After
Governance Is Enabled" section. It reads as a Creation Chat session opener / role definition.

---

## Decisions Already Made

- `governance/templates/genesis.md` = M18 project-setup template; 226/226 tests pass; do not change without updating `tests/test_genesis_template.py`.
- `governance/systems/creation-chat-role.md` = CFO's Creation Chat role definition, preserved verbatim from `1914abd`.
- `v4.0.0` tagged at `cd044ab` (the corrected master HEAD after the fix).

---

## Carry-Over Open Items

None beyond SN-10.

---

## Next Action

HQ Chat confirms the placement of `governance/systems/creation-chat-role.md` (or redirects).
No execution work is required — this is a placement decision only.
