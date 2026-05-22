---
project: ai-project-system
type: migration-guide
version: 2.0.0
status: Active
effective_date: 2026-05-22
---

# Legacy Project Migration Guide

**Version:** 2.0.0  
**Status:** Active  
**Effective Date:** 2026-05-22

---

## Purpose

This guide gets an existing project — whether started with an early version of this system or plain — onto the current governance in under 10 minutes. The adoption startup prompt handles the rest.

---

## Quick Migration (Recommended)

### Prerequisites

- [ ] Working tree is clean (`git status` shows nothing)
- [ ] You are on a feature branch (not master/main)
- [ ] Recent backup or remote push exists
- [ ] Active work is paused or committed

### Step 1: Add Governance Submodule

```bash
git submodule add https://github.com/panchew/ai-project-system governance
cd governance
git fetch
git checkout master
cd ..
git add governance .gitmodules
git commit -m "chore: add AI Project System governance"
```

### Step 2: Create Project Config

Create `.ai-project.yml` at repository root:

```yaml
governance:
  source: https://github.com/panchew/ai-project-system
  version: "2.0.0"
  ref: master
project:
  name: <your-project-name>
  description: "<short description>"
```

```bash
git add .ai-project.yml
git commit -m "chore: add project configuration"
```

### Step 3: Install the Governance Agent

```bash
mkdir -p .github/agents
cp governance/agents/governance.agent.md .github/agents/governance.agent.md
git add .github/agents/governance.agent.md
git commit -m "chore: install Governance Agent"
```

### Step 4: Start HQ Mode with Adoption Prompt

Open your AI chat tool with the Governance Agent selected and send:

```
I want to adopt the AI Project System governance framework for my existing project at <repo-path>.
Initialize HQ Chat for this project, help me assess what's needed for adoption, and create a migration plan.
```

The agent will inventory your existing docs, assess what's needed, and produce a migration plan.

**That's it.** Steps 1-3 take ~5 minutes. Step 4 is conversational.

---

## Rollback

If anything goes wrong:

```bash
# Reset to pre-migration state
git checkout <your-feature-branch>
git reset --hard HEAD~3   # undo the three migration commits
git submodule deinit governance
git rm governance
rm -rf .git/modules/governance
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `git submodule add` fails — `governance` already exists | `rm -rf governance && git rm -r governance && git commit -m "chore: remove conflicting folder"` then retry |
| Submodule checkout fails — `master` not found | `cd governance && git fetch origin && git branch -r` to see available branches, then check out the correct one |
| `.ai-project.yml` invalid | Validate with `python -c "import yaml; yaml.safe_load(open('.ai-project.yml'))"` and check against `governance/ai-project-yml-spec.md` |
| Agent not appearing | Ensure `.github/agents/governance.agent.md` exists with correct YAML front-matter. Restart your AI tool. See [ADOPTION-FAQ.md](ADOPTION-FAQ.md). |

---

## Reference

- [ADOPTION-GUIDE.md](ADOPTION-GUIDE.md) — Full greenfield adoption walkthrough
- [ADOPTION-FAQ.md](ADOPTION-FAQ.md) — Common issues and solutions
- [governance.agent.md](../agents/governance.agent.md) — Unified Governance Agent definition
- [submodule-setup.md](../submodule-setup.md) — Git submodule management details
- [ai-project-yml-spec.md](../ai-project-yml-spec.md) — Configuration file specification
