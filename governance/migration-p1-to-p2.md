---
project: ai-project-system
type: migration-guide
version: 1.0.0
status: Active
effective_date: 2026-04-21
---

# P1 → P2 Migration Guide

**Version:** 1.0.0  
**Status:** Active  
**Effective Date:** 2026-04-21  
**Introduced In:** Epic E6.5 (P2-M6)

---

## 1. Purpose

This guide walks an existing project using the P1 governance structure (flat `docs/` folder with governance files embedded) through adopting the P2 structure:

- Governance is in a `.governance/` git submodule referencing `ai-project-system`
- A `.ai-project.yml` at the repo root declares governance source and version
- `docs/` contains only project history — phases, context, decisions, roadmap
- No governance files remain locally in `docs/`

This migration is a breaking change to folder layout. Follow all steps in order.

---

## 2. Pre-Migration Checklist

Complete these before starting:

- [ ] All P1 epics are closed and accepted
- [ ] All P1 milestones are closed and declared complete
- [ ] Working tree is clean (`git status` shows nothing to commit)
- [ ] You are on a feature branch (not `main`, `master`, or `milestone/*`)
- [ ] You have a recent backup or the repository is pushed to a remote

Once all items above are checked, proceed to Section 3.

---

## 3. Step-by-Step Migration

### Step 1 — Add the `.governance/` submodule

Add `ai-project-system` as a git submodule at `.governance/` and pin it to v2.0.0:

```bash
git submodule add https://github.com/panchew/ai-project-system .governance
cd .governance
git fetch
git checkout v2.0.0
cd ..
git add .governance .gitmodules
git commit -m "chore: add governance submodule pinned to v2.0.0"
```

For the full submodule procedure — including team clone setup and version update instructions — see [`submodule-setup.md`](submodule-setup.md).

---

### Step 2 — Create `.ai-project.yml` at repo root

Create a `.ai-project.yml` file at the root of your repository:

```yaml
# .ai-project.yml
# AI Project System — Project Configuration Contract
# Spec: .governance/governance/ai-project-yml-spec.md v1.0.0

governance:
  source: https://github.com/panchew/ai-project-system
  version: "2.0.0"
  ref: v2.0.0

project:
  name: <your-project-name>         # slug format, e.g. my-project
  description: "<short description of your project>"
```

Replace `<your-project-name>` and the description with your actual project values.

For the full `.ai-project.yml` field reference and validation rules, see [`.governance/governance/ai-project-yml-spec.md`](.governance/governance/ai-project-yml-spec.md).

Commit the file:

```bash
git add .ai-project.yml
git commit -m "chore: add .ai-project.yml pinned to governance v2.0.0"
```

---

### Step 3 — Update `README.md` to reflect new structure

Your project `README.md` should reflect that:

- Governance lives in `.governance/` (the submodule)
- Project artifacts (specs, completions, context) live in `docs/`

Update any references to `docs/PROJECT-SYSTEM-GUIDELINES.md`, `docs/AI-OPERATING-GUIDELINES.md`, `docs/templates/`, `docs/systems/`, or similar to point to `.governance/governance/` instead.

Example change:

```diff
-See [docs/PROJECT-SYSTEM-GUIDELINES.md](docs/PROJECT-SYSTEM-GUIDELINES.md) for project rules.
+See [.governance/governance/PROJECT-SYSTEM-GUIDELINES.md](.governance/governance/PROJECT-SYSTEM-GUIDELINES.md) for project rules.
```

Commit when done:

```bash
git add README.md
git commit -m "docs: update README to reflect P2 structure"
```

---

### Step 4 — Remove local copies of governance files from `docs/`

Governance files now come from the submodule. Remove any local copies that were part of P1 structure:

```bash
# Remove governance docs
git rm docs/PROJECT-SYSTEM-GUIDELINES.md 2>/dev/null || true
git rm docs/AI-OPERATING-GUIDELINES.md 2>/dev/null || true
git rm docs/EPIC-EXECUTION-CHAT-STARTER.md 2>/dev/null || true
git rm docs/FAQ.md 2>/dev/null || true
git rm docs/QUICK-START.md 2>/dev/null || true
git rm docs/governance-source.md 2>/dev/null || true

# Remove governance subdirectories from docs/
git rm -r docs/templates/ 2>/dev/null || true
git rm -r docs/systems/ 2>/dev/null || true
git rm -r docs/diagrams/ 2>/dev/null || true

# Commit
git commit -m "chore: remove local governance files (now via submodule)"
```

After this step, `docs/` should contain only:

```
docs/
├── README.md
├── roadmap/
├── phases/
├── decisions/
├── context/
└── _legacy/         (if applicable)
```

No governance files should remain in `docs/`.

---

### Step 5 — Update internal references to old governance paths

Scan for any remaining links pointing to the old `docs/` governance paths and update them to the new `.governance/governance/` paths:

```bash
# Find files with old paths
grep -r "docs/PROJECT-SYSTEM-GUIDELINES\|docs/AI-OPERATING-GUIDELINES\|docs/templates/\|docs/systems/\|docs/diagrams/\|docs/FAQ\|docs/QUICK-START" --include="*.md" -l
```

For each file found, update the references:

| Old path | New path |
|---|---|
| `docs/PROJECT-SYSTEM-GUIDELINES.md` | `.governance/governance/PROJECT-SYSTEM-GUIDELINES.md` |
| `docs/AI-OPERATING-GUIDELINES.md` | `.governance/governance/AI-OPERATING-GUIDELINES.md` |
| `docs/EPIC-EXECUTION-CHAT-STARTER.md` | `.governance/governance/EPIC-EXECUTION-CHAT-STARTER.md` |
| `docs/FAQ.md` | `.governance/governance/guides/FAQ.md` |
| `docs/QUICK-START.md` | `.governance/governance/guides/QUICK-START.md` |
| `docs/templates/epic-spec.md` | `.governance/governance/templates/epic-spec.md` |
| `docs/systems/hq-chat.md` | `.governance/governance/systems/hq-chat.md` |

> **Note:** References in historical P1 phase artifacts (`docs/phases/P1__*/`) reference the paths as they existed at the time. Do **not** update these — they are historical records and should remain accurate to the state of the project when they were written.

Commit reference updates:

```bash
git add -u
git commit -m "fix: update governance path references to .governance/governance/"
```

---

### Step 6 — Commit and push

Push the migration branch and open a PR for review:

```bash
git push origin <your-branch-name>
```

Open a PR targeting your project's milestone or main integration branch. The PR description should note that this is a P1 → P2 governance migration.

---

## 4. Post-Migration Validation Checklist

After completing all 6 steps, verify:

- [ ] `.ai-project.yml` exists at repo root and is valid per the spec
- [ ] `.governance/` submodule is initialized and checked out at `v2.0.0` (`git submodule status` shows the correct SHA)
- [ ] `.governance/` is pinned to a version tag (not a floating branch)
- [ ] No governance files remain in `docs/` — only project history artifacts
- [ ] Internal links in active documentation resolve correctly
- [ ] `git status` is clean after all migration commits
- [ ] `grep -r "docs/PROJECT-SYSTEM-GUIDELINES\|docs/AI-OPERATING-GUIDELINES\|docs/templates/\|docs/systems/\|docs/diagrams/" --include="*.md"` returns no active (non-historical) results

If all items pass, the migration is complete.

---

## 5. Reference Documents

| Document | Location |
|---|---|
| Submodule setup procedure | [`submodule-setup.md`](submodule-setup.md) |
| `.ai-project.yml` specification | [`ai-project-yml-spec.md`](ai-project-yml-spec.md) |
| Governance folder structure | [`diagrams/repository-structure.md`](diagrams/repository-structure.md) |
| Quick Start guide | [`guides/QUICK-START.md`](guides/QUICK-START.md) |
