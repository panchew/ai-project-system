---
milestone: M18
name: Inception Artifacts
phase: P4
status: planned
start_date: 2026-06-18
epics:
  - E18.1
---

# Milestone M18: Inception Artifacts

## Goal

Define and implement the Creation Chat / Genesis layer — the canonical entry point for
starting a new project under the AI Project System governance framework. Without this,
there is no defined "how to begin": new adopters must reverse-engineer the system from
existing projects rather than follow a prescribed onboarding path.

This is the foundational shift deferred from the original M16 plan. It makes the system
self-describing for first-time users and agents.

---

## Scope

One Epic:

- **E18.1 — Genesis Template and Creation Chat**

---

## Epic Summary

### E18.1 — Genesis Template and Creation Chat

**What it delivers:**

A `genesis.md` governance template that a new user (or an AI agent acting as Creation
Chat) uses to bootstrap a project from scratch. The template captures the inputs
(project name, goal, initial team) and produces the outputs needed to open a Phase Chat:
an HQ context packet and a Phase 1 scope definition.

`start-a-project.md` is updated to reflect this flow end-to-end. The walkthrough
validates that following the template produces a working project structure with no manual
steps outside what the template prescribes.

**Key requirements:**
- `governance/templates/genesis.md` created with YAML front-matter schema and guidance
- Creation Chat role defined: inputs, decision authority, outputs
- `start-a-project.md` updated to reference the Creation Chat flow
- New-project walkthrough validated (real run, not hypothetical)

**Spec:** `P4-M18-E18.1__spec__Genesis_Template_and_Creation_Chat.md`

---

## Definition of Done

- [ ] `governance/templates/genesis.md` created with YAML front-matter schema,
  required fields, and placeholder guidance text
- [ ] Creation Chat role defined in `governance/systems/` or in the template itself:
  what it receives (project brief), what it produces (HQ context packet, Phase 1 scope)
- [ ] `governance/systems/start-a-project.md` updated end-to-end to reference the
  Creation Chat flow; no manual file-copy steps remain
- [ ] Walkthrough: a real new-project setup is executed using the genesis template and
  the output is verified (HQ context packet present, Phase 1 scope coherent)
- [ ] Tests updated or added to cover genesis front-matter schema validity
- [ ] All existing tests still pass
- [ ] E18.1 Delivery Notice produced and committed
- [ ] Pull request opened: `epic/P4-M18-E18.1` → `milestone/M18`

---

## Acceptance Criteria

1. A new user can follow `start-a-project.md` from blank repo to an open Phase Chat
   session using only the genesis template — no knowledge of internal file paths required
2. `governance/templates/genesis.md` is valid against its own YAML front-matter schema
3. The Creation Chat role definition clearly states what decisions it makes and what
   artifacts it produces
4. The validated walkthrough is committed as evidence (in the Delivery Notice or
   as a separate walkthrough document)
5. All tests pass

---

## Branch Strategy

```
phase/P4  (HEAD: 5f3b10d)
└── milestone/M18          ← this branch
    └── epic/P4-M18-E18.1  ← single epic branch
```

Epic PRs target `milestone/M18`. Milestone PR targets `phase/P4`.

---

## Dependencies

- `governance/systems/start-a-project.md` — update (already rewritten in M15; this
  extends it with the Creation Chat flow)
- `governance/templates/` — add `genesis.md`
- M16 and M17 complete (both merged to `phase/P4`) ✅

---

## Notes

- This milestone has one Epic. No parallel execution is needed.
- The genesis template is the "front door" of the system. Keep it concise:
  it should be readable in under 5 minutes by someone with no prior knowledge.
- The walkthrough validation is mandatory — do not mark E18.1 done without running it.
