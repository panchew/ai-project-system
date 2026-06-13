---
project: ai-project-system
phase: P4
milestone: M15
type: milestone
status: active
last_updated: 2026-06-13
---

# Milestone M15 — Cleanup and Salvage

## Purpose

Make master honest, canonical, and coherent before any Phase P4 feature work begins.
M15 removes stale artifacts, corrects governance documentation, and recovers the complete
M14 implementation from a stranded branch.

This milestone ensures:
- No M1-nomenclature planning artifacts misrepresent M14's completed work as "not yet started"
- Obsolete completion templates are removed; the canonical template is identified
- `start-a-project.md` reflects the current `ai-project init` + governance-as-submodule flow
- The P4 phase spec uses correct global milestone numbering (M15–M20)
- M14's full implementation (artifact parsing, daemon integration, integration tests) is on master

---

## Problem Statement

Master currently suffers two HIGH-severity blockers:

**SN-2 (Abandoned artifacts):** Five M1-nomenclature planning artifacts in the P4 folder
present M14's completed work as "not yet started." Any reader of master's P4 folder gets a
false picture of project state. Two additional obsolete completion templates in
`governance/templates/` (Jan 2026 / P2-era) are superseded by the canonical
`completion-notice-epic.md` but still exist, creating confusion about which to use.
`start-a-project.md` describes a manual file-copy flow that was superseded by
`ai-project init` + governance-as-submodule. The P4 phase spec uses M1/M2/M3/M4
local numbering instead of global M15–M20.

**SN-1 (Stranded M14 branch):** `origin/milestone/M14` holds the complete,
governance-compliant execution of E14.1, E14.2, and E14.3, but is rooted on a
January 2026 P1-era commit and cannot be merged directly to master. The P4 feature
work — artifact parsing, daemon integration, integration tests — is effectively absent
from master until salvaged.

Until both blockers are resolved, master is misleading about project state and the
test suite covering the P4 implementation does not exist on master.

---

## Goals

By the end of this milestone, master must:

1. Contain zero M1-nomenclature artifacts in the P4 folder
2. Have two obsolete governance templates removed from `governance/templates/`
3. Have `governance/systems/start-a-project.md` accurately describe the current project
   initialization flow (including Genesis/Creation Chat)
4. Have `P4__phase-spec.md` use the correct global M15–M20 milestone numbering and
   expanded scope
5. Have M14's implementation commits (E14.1, E14.2, E14.3) present and passing

---

## Non-Goals

This milestone explicitly does **not** aim to:

- Build any new P4 features (deferred to M16+)
- Implement Inception Artifacts (M16)
- Implement Two-Stage Lifecycle changes (M17)
- Design or implement the Bugfix Workflow (M18)
- Create the Team Collaboration Example (M19)
- Polish or known-bug work (M20)

---

## In Scope

- Deletion of 5 stale M1-nomenclature planning artifacts from the P4 folder
- Deletion of 2 obsolete completion templates (`epic-completion-notice.md`,
  `epic-completion-report.md`) from `governance/templates/`
- Recommendation on renaming `governance/templates/completion-notice-epic.md`
  to `completion-notice.md`
- Rewrite of `governance/systems/start-a-project.md`
- Update of `P4__phase-spec.md` to reflect global M15–M20 milestone numbering
  and expanded scope
- Cherry-pick of 7 M14 commits onto a new branch from `milestone/M15`, with conflict resolution
- Test suite pass verification after salvage

---

## Out of Scope

- Any new feature implementation
- Changes to `lib/` beyond what the cherry-picked M14 commits introduce
- New governance templates or policy documents
- Documentation beyond the specific files listed in E15.1 scope

---

## Planned Epics

### Confirmed Epics

- **E15.1 — Master Cleanup** (`P4-M15-E15.1__epic-execution-chat-starter.md`) —
  Delete 5 stale M1-nomenclature artifacts and 2 obsolete templates, rewrite
  `start-a-project.md`, update P4 phase spec to global M15–M20 numbering, and
  deliver a rename recommendation for `completion-notice-epic.md`. Docs/governance
  only; no code changes.

- **E15.2 — M14 Branch Salvage** (`P4-M15-E15.2__epic-execution-chat-starter.md`) —
  Create `epic/E15.2` from `milestone/M15`, cherry-pick 7 commits from
  `origin/milestone/M14` in oldest-first order, resolve 3 known conflict files per
  specified strategy, verify tests pass, and open PR to `milestone/M15`.

**Parallelism:** E15.1 and E15.2 have zero file overlap (E15.1 is docs/governance;
E15.2 is code/test/P4-M14 docs) and may proceed concurrently.

---

## Definition of Done

- [ ] 5 M1-nomenclature artifacts deleted from master:
  - `docs/phases/P4.../P4-M1-E1.1__epic-execution-chat-starter.md`
  - `docs/phases/P4.../P4-M1-E1.1__spec__Artifact_Parsing_and_Schema_Validation.md`
  - `docs/phases/P4.../P4-M1-E1.2__spec__Daemon_Queue_Integration_for_Artifacts.md`
  - `docs/phases/P4.../P4-M1-E1.3__spec__Integration_Tests_for_Multi_Artifact_Workflows.md`
  - `docs/phases/P4.../P4-M1__milestone-execution-chat-starter.md`
- [ ] `governance/templates/epic-completion-notice.md` deleted
- [ ] `governance/templates/epic-completion-report.md` deleted
- [ ] `governance/systems/start-a-project.md` rewritten; references `ai-project init`,
      governance-as-submodule flow, and Creation Chat / Genesis layer; contains no
      references to manual file-copy into `docs/`
- [ ] `P4__phase-spec.md` milestone table updated to M15/M16/M17/M18/M19/M20 with
      expanded scope
- [ ] Rename recommendation for `completion-notice-epic.md` recorded in E15.1
      Delivery Notice
- [ ] `origin/milestone/M14`'s 7 execution commits present on `epic/E15.2` via
      cherry-pick, in order
- [ ] Conflicts in P4 phase spec, P4 HQ starter, and roadmap resolved per specified
      strategy
- [ ] `tests/` pass on `epic/E15.2` branch with 0 failures
- [ ] No M1-era artifacts remain on master after both epic branches are merged

---

## Acceptance Criteria

- [ ] `git ls-files 'docs/phases/P4*'` returns no filenames containing `M1-E1` or `M1__`
- [ ] `git ls-files governance/templates/` returns neither `epic-completion-notice.md`
      nor `epic-completion-report.md`
- [ ] `governance/systems/start-a-project.md` contains no references to manual
      file-copy into `docs/`
- [ ] `P4__phase-spec.md` milestone section lists M15, M16, M17, M18, M19, M20
      (not M1, M2, M3, M4)
- [ ] Test suite passes with 0 failures on master after E15.2 is merged
- [ ] PR `epic/E15.2 → milestone/M15` has no outstanding conflicts at PR creation
- [ ] E15.1 Delivery Notice contains a clear recommendation (rename or keep) for
      `completion-notice-epic.md`

---

## Dependencies

**Internal Dependencies:**
- HQ authorization received 2026-06-12 for M15 and both epics
- `origin/milestone/M14` must remain accessible until E15.2 completes

**External Dependencies:**
- None

---

## Branch Strategy

```
master
  └── phase/P4
        └── milestone/M15  ← this spec lives here
              ├── epic/E15.1
              └── epic/E15.2
```

- `epic/E15.1` and `epic/E15.2` are created from `milestone/M15`
- Epic PRs target `milestone/M15`
- After both epics merged: PR `milestone/M15 → phase/P4`

---

## Timeline

**Target Start:** 2026-06-13
**Target Completion:** 2026-06-20
**Actual Start:** 2026-06-13
**Actual Completion:** In progress

---

## Notes

- This spec supersedes M1/M2/M3/M4 local numbering in the committed P4 phase spec.
  Until E15.1 is merged, treat this spec and the Phase Execution Chat Starter
  (re-instantiation 2026-06-12) as authoritative over `P4__phase-spec.md` on
  milestone numbering.
- E15.1 and E15.2 may be reviewed and merged to `milestone/M15` independently.
