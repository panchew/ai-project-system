---
project: ai-project-system
phase: P2
milestone: M10
epic: E10.3
type: guide
status: active
last_updated: 2026-05-21
---

# Governance Sync Guide

**Version:** 1.0.0  
**Status:** Active  
**Effective Date:** 2026-05-21  
**Introduced In:** Epic E10.3 (P2-M10)

---

## 1. Overview

This guide documents the procedure for synchronizing governance updates from the source repository to an adopted project. Governance sync is how projects receive updates to the AI Project System governance framework — bug fixes, new policies, improved templates, and version bumps.

### How Governance Versioning Works

Governance releases are versioned using [Semantic Versioning](https://semver.org/) (MAJOR.MINOR.PATCH) with a `v` prefix for git tags:

- **Patch updates** (`v2.0.0` → `v2.0.1`): Bug fixes, documentation corrections, non-breaking template changes
- **Minor updates** (`v2.0.0` → `v2.1.0`): New features, new governance policies, new templates (backward compatible)
- **Major updates** (`v2.0.0` → `v3.0.0`): Breaking changes to governance structure or requirements

Each governance release corresponds to a git tag in the source repository (e.g., `https://github.com/panchew/ai-project-system`). Adopted projects pin to a specific tag and update by checking out a newer tag.

---

## 2. Prerequisites

Before performing a governance sync, ensure:

- Git is installed (v2.20+ recommended; v2.43+ tested)
- The project has a `.governance/` submodule configured (see [Submodule Setup Guide](../submodule-setup.md))
- The project has a `.ai-project.yml` file at its root (see [`.ai-project.yml` Specification](../ai-project-yml-spec.md))
- Access to the governance source repository (HTTPS or local path)
- The target version tag exists in the governance source repository

---

## 3. Normal Update Flow

This is the canonical procedure for updating governance from one version to another. It is documented in [submodule-setup.md §6](../submodule-setup.md#6-procedure-updating-to-a-new-governance-version) and validated in Epic E10.3.

### Step-by-Step

Run these commands from your project's repository root.

#### Step 1 — Fetch and check out the new version

```bash
cd .governance
git fetch
git checkout v2.1.0        # replace with the target version
cd ..
```

The submodule will be in detached HEAD state at the target tag. This is expected.

#### Step 2 — Stage the submodule change

```bash
git add .governance
git commit -m "chore: update governance submodule to v2.1.0"
```

#### Step 3 — Update `.ai-project.yml`

Edit `.ai-project.yml` to reflect the new version:

```yaml
governance:
  source: https://github.com/panchew/ai-project-system
  version: "2.1.0"        # updated
  ref: v2.1.0             # updated
```

Keep `version` and `ref` in sync. `version` is the semver string; `ref` is the git tag.

#### Step 4 — Commit the configuration update

```bash
git add .ai-project.yml
git commit -m "chore: update .ai-project.yml to governance v2.1.0"
```

### What Happens After Sync

- The `.governance/` directory now contains the new governance files
- The HQ agent reads the updated `.ai-project.yml` on next startup
- Governance drift detection (future M9 feature) will use the new version

---

## 4. Verification

After syncing, confirm the update was successful:

```bash
# Check submodule is at the expected tag
git submodule status
# Expected: leading space + SHA + (.governance) (v2.1.0)

# Verify version in .ai-project.yml
grep "version:" .ai-project.yml
# Expected: version: "2.1.0"

# Verify governance files are accessible
ls .governance/governance/PROJECT-SYSTEM-GUIDELINES.md
ls .governance/governance/AI-OPERATING-GUIDELINES.md

# Check that the governance guidelines reflect the new version
head -5 .governance/governance/PROJECT-SYSTEM-GUIDELINES.md
# Expected: Version: 2.1.0

# Validate .ai-project.yml schema
python3 -c "
import yaml
d = yaml.safe_load(open('.ai-project.yml'))
assert 'governance' in d, 'Missing governance block'
assert 'version' in d['governance'], 'Missing version'
print(f'Sync verified: governance {d[\"governance\"][\"version\"]}')
"
```

---

## 5. Edge Cases

### 5.1 Tag Not Found

**Problem:** `git checkout v9.9.9` fails with `pathspec 'v9.9.9' did not match any file(s) known to git`.

**Cause:** The specified tag does not exist in the governance source repository.

**Resolution:**

```bash
# List available tags
cd .governance
git fetch
git tag --list 'v*'
cd ..

# Checkout the correct existing tag
cd .governance
git checkout v2.0.0         # or the latest available tag
cd ..
```

Never create tags locally — tags must come from the upstream source repository.

### 5.2 URL Mismatch

**Problem:** `git submodule update` fails with connection errors.

**Cause:** The URL in `.gitmodules` is incorrect or the remote is unreachable.

**Resolution:**

```bash
# Sync the URL from .gitmodules to .git/config
git submodule sync

# Retry the update
git submodule update --init --recursive
```

If the URL is wrong in `.gitmodules`, edit it directly, then run `git submodule sync`.

### 5.3 Dirty Submodule State

**Problem:** `git checkout` inside `.governance/` fails with "local changes" error, or `git submodule update` fails.

**Cause:** Uncommitted changes exist inside `.governance/`.

**Resolution:**

```bash
cd .governance
git stash
cd ..
git submodule update
```

Always treat `.governance/` as read-only. Never make changes inside it.

### 5.4 Merge Conflict in `.gitmodules`

**Problem:** A `git pull` (or merge) produces a merge conflict in `.gitmodules`.

**Cause:** Two branches modified `.gitmodules` in conflicting ways.

**Resolution:**

```bash
# Accept the incoming (theirs) version
git checkout --theirs .gitmodules
git add .gitmodules
git commit -m "chore: resolve governance submodule conflict"
```

**Note:** With modern git (v2.43+), conflicts in the submodule *pointer* (the SHA recorded for `.governance`) are automatically resolved. The `.gitmodules` file remains the only source of content-level conflicts during governance merges.

---

## 6. Rollback Procedure

Rolling back governance to a previous version follows the same procedure as updating, but targets an older tag.

### Step-by-Step Rollback

```bash
# Step 1 — Checkout the previous version in the submodule
cd .governance
git fetch
git checkout v2.0.0          # the version to roll back to
cd ..

# Step 2 — Stage the submodule change
git add .governance
git commit -m "chore: rollback governance to v2.0.0"

# Step 3 — Update .ai-project.yml
# Edit to match the rollback target
#   version: "2.0.0"
#   ref: v2.0.0
git add .ai-project.yml
git commit -m "chore: update .ai-project.yml to governance v2.0.0"
```

### Rollback Verification

Same as update verification (Section 4), confirming the version matches the rollback target.

### When to Roll Back

- The new governance version introduces breaking changes that affect project workflows
- A governance update was applied prematurely (before the project is ready)
- The update introduced errors in governance file references

---

## 7. Testing Checklist

Use this checklist to validate any governance sync operation:

- [ ] `git submodule status` shows the expected tag
- [ ] `.ai-project.yml` `version` and `ref` match the target governance version
- [ ] `.governance/governance/PROJECT-SYSTEM-GUIDELINES.md` is accessible
- [ ] `.governance/governance/AI-OPERATING-GUIDELINES.md` is accessible
- [ ] `head -5 .governance/governance/PROJECT-SYSTEM-GUIDELINES.md` shows the correct version number
- [ ] YAML validation of `.ai-project.yml` passes
- [ ] No unstaged changes in `.governance/`
- [ ] HQ agent references resolve (if configured)

---

## 8. Related Documents

- [Submodule Setup Guide](../submodule-setup.md) — Initial governance setup and team procedures
- [`.ai-project.yml` Specification](../ai-project-yml-spec.md) — Schema reference and sync documentation
- [ADOPTION-FAQ.md](ADOPTION-FAQ.md) — Troubleshooting for sync and update failures
- [PROJECT-SYSTEM-GUIDELINES.md](../PROJECT-SYSTEM-GUIDELINES.md) — Governance policies
- [Epic E10.3 Test Report](../../docs/phases/P2__Adoption_Architecture_and_Multi_Project_Support/P2-M10-E10.3__test-report__governance-sync.md) — Validated test results
