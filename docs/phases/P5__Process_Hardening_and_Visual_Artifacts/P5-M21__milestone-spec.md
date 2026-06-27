---
milestone: M21
name: Adoption Clarity and Platform Agnosticism
phase: P5
status: planned
start_date: 2026-06-27
epics:
  - E21.1
  - E21.2
is_final: false
---

# Milestone M21 — Adoption Clarity and Platform Agnosticism

## Purpose

Remove the friction points that block or mislead a new adopter on first contact. M21 closes
the three adoption-facing gaps from the P5 backlog (GH-4, GH-5, GH-6): governance delivery is
silently tied to a single tool's convention (`.github/agents/`, GitHub Copilot); the
`governance/` vs `.governance/` distinction is never explained before path-sensitive
instructions appear; and `start-a-project.md` never tells the adopter to open a Creation Chat
first. M21 is the second P5 milestone, executed after M20 (Governance Process Hardening) and
before M22 (Visual Artifacts).

This milestone ensures:
- Governance delivery is **platform-agnostic** — Claude Code, Cursor, and Windsurf users reach
  the agent-delivery step without GitHub-specific dead ends (GH-5)
- The **`governance/` vs `.governance/`** distinction is explained up front, before any
  path-sensitive instruction, in every adoption-facing guide (GH-6)
- `start-a-project.md` begins with **"Step 0: Open the Creation Chat"** (paste `seed.md`),
  so a new adopter has a Creation Chat before anything else (GH-4)

---

## Problem Statement

Three adoption defects currently confuse or block new adopters:

1. **Platform lock-in (GH-5).** The governance framework presents `.github/agents/` (a GitHub
   Copilot convention) as the canonical agent-delivery path, and the adoption guides reference
   GitHub Copilot as the assumed tool. This silently excludes Claude Code, Cursor, Windsurf,
   and any tool that does not use that path — they have no documented route to the
   governance agent.

2. **`governance/` vs `.governance/` ambiguity (GH-6).** Two distinct directories exist:
   `governance/` (the framework SOURCE repo, used when dogfooding) and `.governance/` (the
   submodule path inside a consumer project). The adoption and sync guides reference both
   without explaining the split, so an adopter who clones the framework and follows the
   adoption guide hits silent path failures.

3. **Missing Creation Chat opener (GH-4).** `start-a-project.md` explains how to fill in
   `genesis.md` but never tells the user to first paste `governance/templates/seed.md` into a
   Claude session to open the Creation Chat. A new adopter has no Creation Chat and no guidance
   on how to start one.

Each is a low-effort documentation change with high adoption leverage: every new adopter hits
these in the first ten minutes.

---

## Goals

By the end of this milestone, the system must:

1. Define a **platform-agnostic agent-delivery convention** (decoupled from `.github/agents/`),
   add **Claude Code, Cursor, and Windsurf** integration guides alongside the existing Copilot
   guidance, and update the adoption guide and `start-a-project.md` to reference the neutral
   path and link to the tool-specific guides (GH-5).
2. Add a **"Self-referential vs. submodule: how to read this guide"** note to the top of
   `governance/guides/ADOPTION-GUIDE.md`, `governance/guides/GOVERNANCE-SYNC-GUIDE.md`, and
   `governance/systems/start-a-project.md`, before any path-sensitive instruction (GH-6).
3. Add a **"Step 0: Open the Creation Chat"** section to `start-a-project.md` that directs the
   adopter to paste `governance/templates/seed.md` into a Claude session (GH-4).

---

## Non-Goals

This milestone explicitly does **not** aim to:

- Build tooling/automation that auto-installs agents per platform (M21 documents the
  convention and guides; no installer)
- Retro-edit closed P2 phase docs under `docs/phases/P2__.../` that mention `.github/agents/`
  as historical record — scope is the *current* adoption-facing guides only
- Touch process hardening (M20, done) or visual artifacts (M22)
- Change `genesis.md` / `seed.md` content (M21 only references seed.md from start-a-project.md;
  seed.md's own visual-intent change is M22/E22.2)

---

## In Scope

- A platform-agnostic agent-delivery convention + new tool integration guides under
  `governance/guides/` (E21.1)
- Edits to `governance/guides/ADOPTION-GUIDE.md`, `governance/guides/QUICK-START.md`,
  `governance/guides/GOVERNANCE-SYNC-GUIDE.md`, and `governance/systems/start-a-project.md`
  (E21.1, E21.2)
- Any test/doc-lint coverage needed to keep the suite green

## Out of Scope

- Per-platform installers or automation
- Edits to historical `docs/phases/P2__.../` records
- M20 / M22 deliverables

---

## Planned Epics

### Confirmed Epics

- **E21.1 — Platform agnosticism** (GH-5)
- **E21.2 — Adoption documentation clarity** (GH-6 + GH-4)

> **Artifact scope (GH-8 adjacency — now governance law via E20.4):** Per AOG §3.6, the Phase
> Chat produces only this Milestone spec and the Milestone Execution Chat Starter. **No Epic
> specs or Epic Execution Chat Starters are produced at the Phase level for M21** — the
> Milestone Chat (§3.7) authors all Epic specs and Epic Execution Chat Starters for E21.1 and
> E21.2 as its own deliverables. (This is the corrected flow; contrast M20, where Phase-level
> Epic starters were a retained one-time exception.)

### Deferred Epics

- None.

---

## Epic Detail

### E21.1 — Platform agnosticism (GH-5)

**Source:** P5 phase spec, P5-GH-5.

**Grounding (verified):** Platform-specific assumptions live in the *current* guides —
`governance/guides/ADOPTION-GUIDE.md` and `governance/guides/QUICK-START.md` reference GitHub
Copilot; `.github/agents/` appears as the agent path. (The `.github/agents/` hits under
`docs/phases/P2__.../` are closed historical records — out of scope.) No `.github/agents/`
directory exists in this repo, so decoupling targets the **references/assumptions in the
guides**, not a directory.

**Deliverables:**

1. **Platform-agnostic delivery convention** — define a tool-neutral agent-delivery convention
   (e.g., `.ai-project/agents/` or equivalent) and document it as the canonical path, replacing
   the implicit `.github/agents/` (Copilot) assumption in the adoption-facing guides.
2. **Tool integration guides** — add **Claude Code, Cursor, and Windsurf** integration guides
   under `governance/guides/` (e.g., `governance/guides/integrations/<tool>.md` or equivalent),
   alongside the existing Copilot guidance. Each guide: where the governance agent lives, how
   that tool consumes it, and how to open a governance chat with it.
3. **Adoption-doc updates** — update `governance/guides/ADOPTION-GUIDE.md` and
   `governance/systems/start-a-project.md` (and `QUICK-START.md` where it names Copilot) to
   reference the platform-agnostic path and link to the per-tool guides; keep Copilot as one
   option among equals, not the default.

**Definition of Done:**
- [ ] A tool-neutral agent-delivery convention is defined and documented as canonical
- [ ] Claude Code, Cursor, and Windsurf integration guides exist under `governance/guides/`
- [ ] ADOPTION-GUIDE.md, start-a-project.md (and QUICK-START.md) reference the neutral path and
      link the per-tool guides; no GitHub-specific path is *required* to reach the agent step
- [ ] Full test suite passes

**Acceptance Criteria:**
- [ ] A new adopter using Cursor (not GitHub Copilot) can reach the governance agent-delivery
      step without a platform-specific dead end
- [ ] No adoption-facing guide presents `.github/agents/` as the only/canonical path

---

### E21.2 — Adoption documentation clarity (GH-6 + GH-4)

**Source:** P5 phase spec, P5-GH-6 and P5-GH-4.

**Deliverables:**

1. **`governance/` vs `.governance/` disambiguation (GH-6)** — add a "Self-referential vs.
   submodule: how to read this guide" note to the **top** of (before any path-sensitive
   instruction): `governance/guides/ADOPTION-GUIDE.md`, `governance/guides/GOVERNANCE-SYNC-GUIDE.md`,
   and `governance/systems/start-a-project.md`. The note explains: `governance/` = the framework
   source repo (dogfooding); `.governance/` = the submodule path inside a consumer project.
2. **"Step 0: Open the Creation Chat" (GH-4)** — add a Step 0 section to
   `governance/systems/start-a-project.md` directing the adopter to paste
   `governance/templates/seed.md` into a Claude session to open the Creation Chat, *before*
   filling in `genesis.md`.
3. **Ambiguity sweep** — verify no other path-sensitive adoption instruction in the current
   guides suffers the same `governance/` vs `.governance/` ambiguity; fix any found.

**Definition of Done:**
- [ ] The disambiguation note is at the top of all three named docs, ahead of path-sensitive content
- [ ] `start-a-project.md` begins with a "Step 0: Open the Creation Chat" section referencing `seed.md`
- [ ] The ambiguity sweep is complete and any further instances are fixed
- [ ] Full test suite passes

**Acceptance Criteria:**
- [ ] `start-a-project.md` opens with the Creation Chat opener step (paste `seed.md`)
- [ ] The `governance/` vs `.governance/` split is explained up front in ADOPTION-GUIDE.md,
      GOVERNANCE-SYNC-GUIDE.md, and start-a-project.md

---

## Branch Strategy

```
master
└── phase/P5            (M20 already consolidated here)
    └── milestone/M21        ← this milestone (branch from phase/P5)
        ├── epic/P5-M21-E21.1   ← Platform agnosticism (GH-5)
        └── epic/P5-M21-E21.2   ← Adoption documentation clarity (GH-6 + GH-4)
```

Epic PRs target `milestone/M21`. Consolidation PR: `milestone/M21 → phase/P5`.
Phase closure PR (after M22): `phase/P5 → master` (long-lived PR #82).

---

## Prerequisites

- `phase/P5` carries the merged M20 governance hardening (adjacency, worktree isolation,
  scope routing, git-tracking prerequisite, communication protocol now apply)
- These adoption docs are present and git-tracked on `phase/P5` (verify with
  `git ls-files --error-unmatch <path>` — the GH-1 convention M20 delivered):
  - `governance/guides/ADOPTION-GUIDE.md`
  - `governance/guides/GOVERNANCE-SYNC-GUIDE.md`
  - `governance/guides/QUICK-START.md`
  - `governance/systems/start-a-project.md`
  - `governance/templates/seed.md`

---

## Dependencies and Sequencing

**Internal — shared-file contention:**

| File | Epics that edit it |
|------|--------------------|
| `governance/guides/ADOPTION-GUIDE.md` | E21.1, E21.2 |
| `governance/systems/start-a-project.md` | E21.1, E21.2 |
| `governance/guides/QUICK-START.md` | E21.1 |
| `governance/guides/GOVERNANCE-SYNC-GUIDE.md` | E21.2 |

- E21.1 and E21.2 both edit ADOPTION-GUIDE.md and start-a-project.md → **serialize**
  (recommended order **E21.1 → E21.2**, E21.2 rebased on the merged E21.1) or use per-epic
  worktrees with a rebase before the second PR, per the GH-2 convention M20 delivered.

**External:** None. (Per-tool agent verification on real Cursor/Windsurf installs is an
adoption-testing concern, not a framework deliverable.)

---

## Definition of Done (Milestone)

- [ ] E21.1 and E21.2 each meet their Definition of Done above
- [ ] Both epic branches merged to `milestone/M21`
- [ ] Full test suite passes on `milestone/M21`
- [ ] Milestone Closure Declaration produced

---

## Acceptance Criteria (Milestone)

1. A new adopter on a non-Copilot tool (Cursor/Windsurf/Claude Code) can reach the governance
   agent-delivery step with no GitHub-specific dead end; per-tool guides exist (GH-5).
2. The `governance/` vs `.governance/` distinction is explained up front in ADOPTION-GUIDE.md,
   GOVERNANCE-SYNC-GUIDE.md, and start-a-project.md (GH-6).
3. `start-a-project.md` opens with "Step 0: Open the Creation Chat" referencing `seed.md` (GH-4).
4. Full test suite passes.

---

## Timeline

**Target Start:** 2026-06-27
**Target Completion:** 2026-07-04 (5–7 days per Phase spec estimate)
**Actual Start:** Not started
**Actual Completion:** In progress

---

## Notes

- M21 is documentation-clarity work: low-effort, high adoption leverage. Keep edits additive
  and avoid restructuring guides beyond what each gap requires.
- The platform-agnostic *path name* (`.ai-project/agents/` or other) is an Epic-level design
  decision for E21.1; the milestone fixes the requirement (tool-neutral, documented, linked),
  not the exact string.
- Scope is the **current** adoption-facing guides; do not retro-edit closed P2 phase records.
