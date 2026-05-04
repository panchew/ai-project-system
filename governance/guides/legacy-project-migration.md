---
project: ai-project-system
type: migration-guide
version: 1.0.0
status: Active
effective_date: 2026-05-04
---

# Legacy Project Migration Guide

**Version:** 1.0.0  
**Status:** Active  
**Effective Date:** 2026-05-04  
**Introduced In:** Epic E8.2 (P2-M8)

---

## 1. Purpose

This guide enables existing projects to adopt the current P2 governance architecture without manual file copying and with minimal disruption. It supports detection of legacy project states and provides safe onboarding workflows for projects with missing or outdated governance.

**What this guide covers:**
- Detecting current, legacy, and ungoverned project states
- Safe migration workflows for different project types
- Preservation of existing documentation and project context
- Error handling and recovery procedures

This migration preserves existing project content while adding or updating governance artifacts.

---

## 2. Project State Detection

Before migration, identify your project's current governance state:

### Current Governance (P2 Structure)
- Has `.ai-project.yml` at repository root
- Has `governance/` folder as git submodule
- Governance version matches current P2 (v2.0.0 or later)
- No governance files in `docs/` folder

**Action:** No migration needed. Project is already current.

### Legacy Governance (P1 or Pre-P2 Structure)
- Has governance files directly in `docs/` folder
- May have `.governance/` submodule (P1 structure)
- Missing or outdated `.ai-project.yml`
- Governance files mixed with project documentation

**Action:** Follow Legacy Governance Upgrade workflow.

### No Governance
- No `.ai-project.yml` file
- No `governance/` or `.governance/` folder
- No governance-related files in `docs/`

**Action:** Follow Governance Install workflow.

### Partial Governance
- Has `governance/` but missing `.ai-project.yml`
- Has `.ai-project.yml` but missing `governance/` submodule
- Mixed legacy and current elements

**Action:** Follow Project Rescue workflow.

---

## 3. Migration Workflows

### Workflow A: Legacy Governance Upgrade

For projects with existing governance that needs updating to P2 structure.

#### Prerequisites
- [ ] Working tree is clean (`git status` shows nothing)
- [ ] You are on a feature branch (not main/master/milestone branches)
- [ ] Recent backup or remote push exists
- [ ] All active epics are paused or closed

#### Step 1: Backup Current State
```bash
# Create backup branch
git checkout -b backup-pre-migration
git push origin backup-pre-migration

# Return to working branch
git checkout <your-feature-branch>
```

#### Step 2: Update Governance Submodule
```bash
# If .governance/ exists, remove it
if [ -d ".governance" ]; then
  git submodule deinit .governance
  git rm .governance
  rm -rf .git/modules/.governance
fi

# Add governance/ submodule
git submodule add https://github.com/panchew/ai-project-system governance
cd governance
git fetch
git checkout milestone/M8  # or current version
cd ..
git add governance .gitmodules
git commit -m "chore: migrate governance to P2 submodule structure"
```

#### Step 3: Create or Update .ai-project.yml
Create `.ai-project.yml` at repository root:

```yaml
# .ai-project.yml
# AI Project System — Project Configuration Contract
# Spec: governance/governance/ai-project-yml-spec.md

governance:
  source: https://github.com/panchew/ai-project-system
  version: "milestone/M8"
  ref: milestone/M8

project:
  name: <your-project-name>         # slug format, e.g. my-project
  description: "<short description of your project>"
```

Replace `<your-project-name>` and description with your project values.

```bash
git add .ai-project.yml
git commit -m "chore: add .ai-project.yml for P2 governance"
```

#### Step 4: Preserve and Move Documentation
```bash
# Move project docs from docs/ to docs/ (keeping existing structure)
# No destructive moves - preserve all existing content
# Governance files in docs/ will be shadowed by submodule
```

#### Step 5: Validate Migration
```bash
# Verify submodule
git submodule status

# Verify .ai-project.yml exists and is valid
cat .ai-project.yml

# Check that governance/ contains expected files
ls governance/governance/
```

---

### Workflow B: Governance Install

For projects with no existing governance.

#### Prerequisites
- [ ] Working tree is clean
- [ ] You are on a feature branch
- [ ] Project has some documentation or code to govern

#### Step 1: Add Governance Submodule
```bash
git submodule add https://github.com/panchew/ai-project-system governance
cd governance
git fetch
git checkout milestone/M8
cd ..
git add governance .gitmodules
git commit -m "chore: install AI Project System governance"
```

#### Step 2: Create .ai-project.yml
Create `.ai-project.yml` at repository root:

```yaml
governance:
  source: https://github.com/panchew/ai-project-system
  version: "milestone/M8"
  ref: milestone/M8

project:
  name: <your-project-name>
  description: "<project description>"
```

```bash
git add .ai-project.yml
git commit -m "chore: add project configuration for governance"
```

#### Step 3: Initialize Project Structure (Optional)
Consider creating initial project documentation:

```bash
mkdir -p docs/phases
# Copy starter templates from governance/templates/
cp governance/governance/templates/phase-spec.md docs/phases/P1__phase.md
```

---

### Workflow C: Project Rescue

For projects with partial or broken governance.

#### Assessment Phase
First, diagnose what exists:

```bash
# Check for governance files
find . -name "*.md" | grep -i governance

# Check for config files
ls -la | grep -E "\.(yml|yaml)$"

# Check git submodules
git submodule status
```

#### Recovery Steps
Based on what you find:

**Missing .ai-project.yml but has governance/ submodule:**
- Follow Step 3 from Workflow A

**Has .ai-project.yml but missing governance/ submodule:**
- Follow Step 2 from Workflow A

**Has mixed legacy files:**
- Backup docs/ folder
- Follow full Workflow A
- Manually review and migrate any custom governance files

---

## 4. Error Handling and Recovery

### Common Issues

#### Submodule Add Fails
**Error:** `fatal: 'governance' already exists in the index`
**Solution:**
```bash
# Remove existing governance folder
rm -rf governance
git rm -r governance 2>/dev/null || true
git commit -m "chore: remove conflicting governance folder"

# Retry submodule add
git submodule add https://github.com/panchew/ai-project-system governance
```

#### Submodule Checkout Fails
**Error:** `fatal: reference is not a tree: milestone/M8`
**Solution:**
```bash
cd governance
git fetch origin
git branch -r  # Check available branches
git checkout <correct-branch>  # Use available branch/tag
cd ..
```

#### .ai-project.yml Validation Errors
**Error:** Project doesn't start or governance commands fail
**Solution:**
- Verify YAML syntax: `python -c "import yaml; yaml.safe_load(open('.ai-project.yml'))"`
- Check required fields against spec in `governance/governance/ai-project-yml-spec.md`
- Ensure version matches available governance version

### Recovery Procedures

#### Complete Rollback
If migration fails completely:
```bash
# Reset to pre-migration state
git checkout backup-pre-migration
git branch -D <migration-branch>

# Or reset commits
git reset --hard HEAD~<number-of-migration-commits>
git submodule deinit governance
git rm governance
rm -rf .git/modules/governance
```

#### Partial Recovery
If some changes succeeded but others failed:
- Manually fix the broken parts
- Commit fixes separately
- Test governance functionality

---

## 5. Post-Migration Validation

After migration, verify everything works:

### Governance Validation
```bash
# Check submodule health
git submodule status

# Verify governance files are accessible
ls governance/governance/

# Test basic governance commands (if CLI exists)
./governance/bin/ai-project-init --help 2>/dev/null || echo "CLI not available yet"
```

### Project Integrity
```bash
# Ensure no files were accidentally deleted
git status

# Verify existing docs are intact
find docs/ -type f | head -10

# Check that .ai-project.yml is valid
cat .ai-project.yml
```

### Documentation Preservation
- [ ] All existing docs in `docs/` are preserved
- [ ] No destructive folder moves occurred
- [ ] Project history and context maintained
- [ ] Custom governance adaptations noted (if any)

---

## 6. Best Practices

### Before Migration
- Always work on a feature branch
- Create backup branches or tags
- Pause active development
- Review existing documentation for customizations

### During Migration
- Follow steps in order
- Commit after each major step
- Test after each commit
- Don't skip validation steps

### After Migration
- Update team documentation
- Train team on new structure
- Monitor for issues in first few days
- Plan next project phases using new governance

---

## 7. Support and Resources

### Getting Help
- Check this guide's troubleshooting section
- Review governance documentation in `governance/governance/`
- Consult project maintainers

### Related Documentation
- [QUICK-START.md](QUICK-START.md) — Getting started with new projects
- [migration-p1-to-p2.md](migration-p1-to-p2.md) — P1 to P2 migration details
- [ai-project-yml-spec.md](ai-project-yml-spec.md) — Configuration file specification
- [submodule-setup.md](submodule-setup.md) — Git submodule management

---

## 8. Version History

- **v1.0.0 (2026-05-04)**: Initial release for P2-M8-E8.2
  - Support for legacy governance upgrade
  - Governance install for new projects
  - Project rescue workflows
  - Error handling and recovery procedures