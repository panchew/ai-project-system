---
type: escalation-notice
milestone: M17
issued_by: Milestone Chat (P4-M17 — Bug Fixes & Polish)
issued_to: Phase Chat (P4)
date: 2026-06-17
status: open
blocking_execution: true
blocking_closure: false
---

# Escalation Notice — M17 Epic Starters Reference Missing Specs and Carry a Wrong Branch Name

**Issued by:** Milestone Chat (P4-M17 — Bug Fixes & Polish)
**Issued to:** Phase Chat (P4 — Team Collaboration and Artifact-Driven Communication)
**Date:** 2026-06-17
**Blocking M17 execution:** Yes — Epics E17.1 and E17.2 cannot be dispatched as written.
**Blocking M17 closure:** No (milestone has not opened; this is a pre-execution finding)

---

## What Was Found

On opening the M17 Milestone Execution Chat (Bug Fixes & Polish), the two Epic Execution
Chat Starters required for this milestone already exist in the repository:

```
docs/phases/P4__Team_Collaboration_and_Artifact_Driven_Communication/
  P4-M17-E17.1__epic-execution-chat-starter.md
  P4-M17-E17.2__epic-execution-chat-starter.md
```

Both were committed ahead of schedule during Milestone M14 (PR #66, commit `9f69b4e`) as
auto-generated drafts, not as products of an M17 planning pass. A review against the
established starter format and against the files actually present on disk reveals two
defects that prevent either Epic from being dispatched.

---

## Audit Findings

**Critical — Referenced Epic specs do not exist**

Both starters name an Epic spec as the single source of truth and instruct the executing
agent to "Treat the Epic spec as the single source of truth" and "Implement only what is
explicitly defined in the spec." Neither named spec file is present in the repository:

- `P4-M17-E17.1__spec__Fix_Daemon_Orchestrator_Path_Resolution.md` — **missing**
- `P4-M17-E17.2__spec__Update_Starters_and_Documentation.md` — **missing**

Confirmed by directory listing: no `P4-M17*spec*` files exist. The M17 Milestone Starter
nonetheless lists both Epics as **"Status: Spec Complete (ready to execute)"** — this
status is inaccurate. With no spec to bound the work, neither Epic has a source of truth,
and an executing agent has nothing authoritative to implement against. This mirrors the
M15 finding where the E15.3 starter referenced a spec that did not exist.

**High — Wrong target branch name (`M147` instead of `M17`)**

Both starters set the Epic PR target to a branch named `milestone/M147` — a typo for
`milestone/M17`. Four occurrences:

| File | Line | Text |
|------|------|------|
| `P4-M17-E17.1__epic-execution-chat-starter.md` | 17 | ``Pull request: `epic/P4-M17-E17.1` → `milestone/M147` `` |
| `P4-M17-E17.1__epic-execution-chat-starter.md` | 42 | ``PR opened against correct milestone branch (`milestone/M147`)`` |
| `P4-M17-E17.2__epic-execution-chat-starter.md` | 17 | ``Pull request: `epic/P4-M17-E17.2` → `milestone/M147` `` |
| `P4-M17-E17.2__epic-execution-chat-starter.md` | 50 | ``PR opened against correct milestone branch (`milestone/M147`)`` |

An agent following these instructions literally would open PRs against, or attempt to
create, a branch named `milestone/M147`, which corresponds to no milestone in this phase.
This is the same class of defect found in M15 (`milestone/M145` for `milestone/M15`).

**Context — Branch does not yet exist**

The repository is currently on `milestone/M16`. No `milestone/M17` branch exists yet, so
the corrected target (`milestone/M17`) must also be created from `milestone/M16` before
either Epic can open a PR.

---

## What Is Outside Milestone Chat Authority

1. **Authoring the missing Epic specs.** The M17 starters were committed under Phase-level
   planning (PR #66). Whether Milestone Chat may now author `P4-M17-E17.1__spec` and
   `P4-M17-E17.2__spec`, or whether Phase Chat wishes to author/approve them, is a
   Phase-level decision.
2. **Authorizing correction of the committed starters.** The `M147` typo and the
   "Spec Complete" status sit in files already merged to the mainline P4 history.
   Editing merged planning artifacts requires Phase Chat authorization.
3. **Re-asserting "ready to execute."** The Milestone Starter's claim that both Epics are
   spec-complete cannot stand until specs exist; only Phase Chat can re-baseline that
   status.

---

## Decisions Requested from Phase Chat

1. **Who authors the two missing Epic specs?** Options:
   - Milestone Chat drafts both specs (E17.1, E17.2) against the M17 milestone scope, for
     Phase Chat approval before execution.
   - Phase Chat authors/supplies them.
2. **Authorize correcting the `M147` → `M17` typo** in both starters (4 occurrences), and
   correcting the inaccurate "Spec Complete" status to reflect reality.
3. **Confirm branch setup:** create `milestone/M17` from `milestone/M16` as the corrected
   PR target before E17.1/E17.2 dispatch.

---

## M17 Impact

M17 cannot enter execution until the two specs exist and the starters point at a valid
target branch. The two defects are low-effort to remediate (draft two specs; fix four
lines; create one branch) but require Phase Chat authorization because they touch
already-merged planning artifacts. No code or feature work is blocked beyond this — the
underlying daemon path-resolution bug (E17.1) and documentation updates (E17.2) remain
well understood; only their governing specs are absent.

---

## Note on Artifact Type

This reuses the one-off **Escalation Notice** form first produced in M15
(`P4-M15__escalation-notice__E15.3-artifact.md`). As noted there, no canonical template
for upward (Milestone → Phase) escalation yet exists in `governance/templates/`. The
recurrence of (a) starters referencing non-existent specs and (b) `M14x`-style branch-name
typos across two separate milestones (M15: `M145`; M17: `M147`) suggests both a template
gap and a need for a planning-time lint check on auto-generated starters. Recommend Phase
Chat consider folding both into the M17 polish scope or a follow-on milestone.
