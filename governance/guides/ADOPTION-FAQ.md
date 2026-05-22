---
project: ai-project-system
phase: P2
milestone: M10
epic: E10.1
type: reference
status: active
last_updated: 2026-05-21
updated_by: E10.3-governance-sync-validation
---

# Adoption Troubleshooting FAQ

Common issues encountered during AI Project System adoption and their resolutions.

**Related guide:** [ADOPTION-GUIDE.md](ADOPTION-GUIDE.md)

---

## Table of Contents

1. [Governance Submodule Issues](#1-governance-submodule-issues)
2. [.ai-project.yml Validation Errors](#2-ai-projectyml-validation-errors)
3. [Governance Agent Not Appearing](#3-governance-agent-not-appearing)
4. [Branch Naming Conflicts](#4-branch-naming-conflicts)
5. [Override Configuration Problems](#5-override-configuration-problems)
6. [Governance Sync/Update Failures](#6-governance-syncupdate-failures)
7. [CLI Init Failures](#7-cli-init-failures)
8. [Existing Project Adoption](#8-existing-project-adoption)
9. [Governance Version Tag Issues](#9-governance-version-tag-issues)
10. [General Governance Questions](#10-general-governance-questions)

---

## 1. Governance Submodule Issues

### Problem: Submodule directory is empty or missing

Running `git submodule status` shows `-` (uninitialized) or the `.governance/` directory is empty.

**Cause:** The submodule was registered but not initialized, or the clone was performed without `--recurse-submodules`.

**Solution:**

1. Initialize the submodule:
   ```bash
   git submodule update --init --recursive
   ```

2. Verify initialization:
   ```bash
   git submodule status
   ```
   Expected: A leading space (initialized) followed by a commit SHA.

3. If still empty, deinit and re-init:
   ```bash
   git submodule deinit .governance
   git submodule update --init --recursive
   ```

**Prevention:** Clone projects with `git clone --recurse-submodules <url>` and run `git submodule update --recursive` after every `git pull` that may include submodule changes.

**See also:** [Submodule Setup Guide](../submodule-setup.md#7-procedure-team-setup-clone-with-submodules)

---

### Problem: Submodule is on the wrong version or detached HEAD

The submodule points to a different ref than the one specified in `.ai-project.yml`.

**Cause:** Governance version was updated in `.ai-project.yml` but the submodule was not updated, or someone checked out a different ref inside `.governance/`.

**Solution:**

1. Check current submodule state:
   ```bash
   cd .governance
   git log --oneline -1
   cd ..
   ```

2. Compare with `.ai-project.yml` `governance.ref`:
   ```bash
   cat .ai-project.yml
   ```

3. Pin to the correct ref:
   ```bash
   cd .governance
   git fetch
   git checkout v2.0.0     # or the ref from .ai-project.yml
   cd ..
   git add .governance
   git commit -m "chore: sync governance submodule to v2.0.0"
   ```

**Prevention:** Keep `.ai-project.yml` and the submodule ref in sync. Use tags (`v2.0.0`) for stability, not branches.

**See also:** [Submodule Setup Guide](../submodule-setup.md#6-procedure-updating-to-a-new-governance-version)

---

## 2. .ai-project.yml Validation Errors

### Problem: CLI or HQ agent reports "invalid .ai-project.yml"

The project config file fails validation.

**Cause:** Missing required fields, incorrect YAML syntax, or constraint violations.

**Solution:**

1. Validate YAML syntax:
   ```bash
   python -c "import yaml; yaml.safe_load(open('.ai-project.yml'))"
   ```
   If this fails, fix YAML syntax errors (missing colons, incorrect indentation).

2. Verify required fields are present:
   ```bash
   cat .ai-project.yml
   ```
   Ensure all five required fields exist:
   - `governance.source`
   - `governance.version`
   - `governance.ref`
   - `project.name`
   - `project.description`

3. Check field constraints:
   - `governance.version` must be a quoted semver string (e.g., `"2.0.0"`, not `2.0.0`)
   - `project.name` must match `^[a-z][a-z0-9-]*$` (lowercase, hyphens only)
   - `governance.source` must be an HTTPS URL or relative path starting with `./` or `../`

4. Restore the correct file from a backup or recreate:
   ```yaml
   governance:
     source: https://github.com/panchew/ai-project-system
     version: "2.0.0"
     ref: v2.0.0
   project:
     name: my-project
     description: "My project description"
   ```

**Prevention:** Use the `ai-project init` CLI to create `.ai-project.yml` — it generates valid configuration automatically. If editing manually, validate with a YAML linter.

**See also:** [`.ai-project.yml` Specification](../ai-project-yml-spec.md#4-validation-rules)

---

## 3. Governance Agent Not Appearing

### Problem: The agent is not available in the AI tool's agent selector

After following the adoption guide, the Governance Agent is not available.

**Cause:** The agent file is missing, has incorrect YAML front-matter, or the tool has not reloaded the agent configuration.

**Solution:**

1. Verify the agent file exists:
   ```bash
   cat .github/agents/governance.agent.md
   ```
   If missing, copy it from governance:
   ```bash
   mkdir -p .github/agents
   cp .governance/governance/agents/governance.agent.md .github/agents/governance.agent.md
   ```

2. Check the front-matter has correct `name` field:
   ```yaml
   ---
   name: hq
   version: 2.0.0
   description: Unified Governance Agent — operates as HQ, Phase, Milestone, or Epic mode based on the Chat Starter delivered
   type: custom-agent
   ---
   ```

3. Restart your AI tool / reload the agent configuration.

4. Verify the agent is selectable in your tool's agent selector (look for **"hq"** or the name you configured).

**Prevention:** Ensure `.github/agents/governance.agent.md` is committed to the repository. Run `git status` to verify it is tracked.

> **Old `hq.agent.md`?** Remove any old `.github/agents/hq.agent.md` — it has been replaced by the unified `governance.agent.md`.

**See also:** [ADOPTION-GUIDE.md Step 3](ADOPTION-GUIDE.md#step-3-configure-hq-agent)

---

## 4. Branch Naming Conflicts

### Problem: Pushing a branch fails with naming errors or confusion about branch hierarchy

Git rejects the push, or branches are created with wrong prefixes.

**Cause:** Branch names do not follow the canonical hierarchy (`epic/*`, `milestone/*`, `phase/*`), or the target branch for a PR is incorrect.

**Solution:**

1. Verify branch naming rules from governance:
   ```bash
   grep "Branch Naming" .governance/governance/PROJECT-SYSTEM-GUIDELINES.md
   ```

2. List existing branches to check hierarchy:
   ```bash
   git branch -a
   ```

3. Create a correctly named branch:
   ```bash
   git checkout master
   git checkout -b milestone/M1        # milestone branch
   git checkout -b epic/E1.1           # epic branch (from milestone)
   ```

4. If you created a misnamed branch, rename it:
   ```bash
   git branch -m old-bad-name epic/E1.1
   ```

**Common naming mistakes and fixes:**

| Mistake | Correction |
|---------|-----------|
| `epic-E1.1` | `epic/E1.1` |
| `EPIC/E1.1` | `epic/E1.1` |
| `branch/epic-E1.1` | `epic/E1.1` |
| PR from `epic/E1.1` to `master` | PR from `epic/E1.1` to `milestone/M1` |

**Prevention:** Always create epic branches from their parent milestone branch: `git checkout -b epic/E1.1 milestone/M1`. Follow the promotion path: `epic/* → milestone/* → phase/* → develop/main`.

**See also:** [PROJECT-SYSTEM-GUIDELINES.md §7-8](../PROJECT-SYSTEM-GUIDELINES.md#7-branch-naming-rules)

---

## 5. Override Configuration Problems

### Problem: Governance overrides in `.ai-project.yml` are not taking effect

The HQ agent is not applying project-specific overrides (branch strategy, merge strategy, epic prefix).

**Cause:** Overrides block is missing, incorrectly formatted, or uses unrecognized keys.

**Solution:**

1. Check the overrides section in `.ai-project.yml`:
   ```bash
   cat .ai-project.yml
   ```

2. Verify the overrides block uses only recognized keys:
   ```yaml
   overrides:
     branch_strategy: trunk-based    # or: gitflow
     merge_strategy: merge           # or: squash, rebase
     epic_prefix: epic/              # or: feature/
   ```

3. Validate YAML syntax:
   ```bash
   python -c "import yaml; d=yaml.safe_load(open('.ai-project.yml')); print(d.get('overrides', {}))"
   ```

4. If overrides are correctly formatted but not applied, verify the Governance Agent version is v2.0.0+:
   ```bash
   head -5 .governance/governance/agents/governance.agent.md
   ```
   Expected: `version: 2.0.0` or later.

**Prevention:** Start with no overrides (defaults apply). Add overrides only when you need to deviate from defaults. Document override changes in a decision record under `docs/decisions/`.

**See also:** [`.ai-project.yml` Specification §3.3](../ai-project-yml-spec.md#33-optional-fields--overrides)

---

## 6. Governance Sync/Update Failures

### Problem: `git submodule update` fails, or governance updates produce merge conflicts

Running `git submodule update` returns errors, or pulling governance changes causes conflicts.

**Cause:** Network issues, submodule URL mismatch, dirty submodule state, tag not found, or conflicting changes.

**Solution:**

1. For submodule update failures:
    ```bash
    # Verify remote URL
    git config --file .gitmodules --list | grep submodule
    
    # Update submodule (force if needed)
   git submodule update --init --recursive --force
   ```

2. For URL mismatch, fix `.gitmodules`:
   ```bash
   git submodule sync
   git submodule update --init --recursive
   ```

3. For merge conflicts in `.gitmodules`:
   ```bash
   # The conflict is typically in the .gitmodules file, not in submodule files
   git checkout --theirs .gitmodules   # accept incoming version
   git add .gitmodules
   git commit -m "chore: resolve governance .gitmodules conflict"
   ```
   **Note:** Modern git (v2.43+) automatically resolves conflicts in the submodule pointer (SHA). Content-level conflicts only occur in `.gitmodules` or other tracked files.

4. For dirty submodule state (unstaged changes inside `.governance/`):
   ```bash
   cd .governance
   git stash
   cd ..
   git submodule update
   ```

5. For submodule checkout failures when a tag does not exist:
   ```bash
   # Error message: pathspec 'vX.X.X' did not match any file(s) known to git
   # List available tags
   cd .governance
   git fetch
   git tag --list 'v*'
   # Checkout the correct existing tag
   git checkout v2.0.0
   cd ..
   ```

6. For rollback to a previous governance version:
   ```bash
   cd .governance
   git fetch
   git checkout v2.0.0            # rollback target
   cd ..
   git add .governance
   git commit -m "chore: rollback governance to v2.0.0"
   # Update .ai-project.yml version and ref to match
   ```

**Prevention:** Treat `.governance/` as read-only. Never make changes inside the submodule directory. Always use `git submodule update` after pulling. Use tags for stability (`v2.0.0`), not branches. Verify the target tag exists before starting a sync.

**See also:** [Governance Sync Guide](GOVERNANCE-SYNC-GUIDE.md), [Submodule Setup Guide §9](../submodule-setup.md#9-edge-cases-and-gotchas)

---

### Problem: `@panchew/ai-project` package not found on npm

`npm install -g @panchew/ai-project` returns a 404 error.

**Cause:** The CLI package has not been published to the npm registry, or the package name is incorrect.

**Solution:**

1. **Use the local script** from the governance source:
   ```bash
   # After adding governance submodule
   ./governance/bin/ai-project-init init my-project
   ```
   
   Or clone the governance source directly:
   ```bash
   git clone https://github.com/panchew/ai-project-system /tmp/ai-project-system
   /tmp/ai-project-system/bin/ai-project-init init my-project
   ```

2. **Set up governance manually** if the script is not available:
   - Add the submodule: `git submodule add https://github.com/panchew/ai-project-system governance`
   - Create `.ai-project.yml` manually with your project name and governance reference
   - Copy the Governance Agent: `cp governance/agents/governance.agent.md .github/agents/governance.agent.md`

**Prevention:** Check the [governance source repository](https://github.com/panchew/ai-project-system) for the latest CLI availability. The local script at `bin/ai-project-init` is always available.

---

## 7. CLI Init Failures

### Problem: `ai-project init` fails with permission errors, missing dependencies, or network errors

The CLI command does not complete successfully.

**Cause:** Missing Node.js, insufficient permissions, network connectivity issues, or npm installation problems.

**Solution:**

1. **CLI not found:**
   ```bash
   # Try npx
   npx @panchew/ai-project init my-project
   
   # Or install globally
   npm install -g @panchew/ai-project
   ```

2. **Permission errors (Unix/Mac):**
   ```bash
   # Fix npm permissions
   npm config get prefix
   # If /usr/local, use:
   sudo npm install -g @panchew/ai-project
   # Better: configure npm for user directory
   npm config set prefix ~/.npm
   echo 'export PATH=$PATH:~/.npm/bin' >> ~/.bashrc
   source ~/.bashrc
   npm install -g @panchew/ai-project
   ```

3. **Node.js not found or outdated:**
   ```bash
   node --version
   # Must be v18+
   # Install or upgrade: https://nodejs.org/
   ```

4. **Network issues (git submodule clone fails):**
   ```bash
   # Test connectivity
   git ls-remote https://github.com/panchew/ai-project-system
   
   # If blocked by proxy:
   git config --global http.proxy http://proxy:port
   git config --global https.proxy http://proxy:port
   ```

5. **Project already exists / not empty:**
   ```bash
   # Initialize in an empty directory
   mkdir new-project && cd new-project && ai-project init .
   
   # Or force init in existing directory
   ai-project init my-project --force
   ```

6. **Node.js version below v18:**
   ```bash
   node --version
   # Must be v18+, you have v16 or lower
   ```
   **Solution:** Use `nvm` to install and manage Node.js versions:
   ```bash
   nvm install 18
   nvm use 18
   ```
   If Node.js upgrade is not possible, skip the CLI and set up governance manually:
   - Add the governance submodule directly: `git submodule add https://github.com/panchew/ai-project-system governance`
   - Create `.ai-project.yml` manually (see Step 2 verification example)
   - Copy the Governance Agent: `cp governance/agents/governance.agent.md .github/agents/governance.agent.md`
   
   Governance itself is language-agnostic — Node.js is only required for the CLI tool.

**Prevention:** Ensure Node.js v18+ and npm are installed before running `ai-project init`. Use `nvm` to manage Node.js versions. Configure npm for user directory to avoid permission issues. Clone the project first, then run `init` inside it.

**See also:** [ADOPTION-GUIDE.md Prerequisites](ADOPTION-GUIDE.md#prerequisites)

---

## 8. Existing Project Adoption

### Problem: I have an existing project with code and history — `ai-project init` requires an empty directory

The adoption guide targets greenfield projects, but you need to add governance to an existing repository.

**Cause:** The `ai-project init` CLI scaffold creates a new project skeleton and refuses to run in a non-empty directory to avoid overwriting existing content.

**Solution:**

1. **Use the Legacy Migration Guide** — it provides a "Governance Install" workflow (Workflow B) specifically for existing projects:
   - [Legacy Migration Guide: Governance Install](legacy-project-migration.md#workflow-b-governance-install)
   
2. **Manual governance install** (summary):
   ```bash
   # Add governance submodule
   git submodule add https://github.com/panchew/ai-project-system governance
   cd governance
   git fetch
   git checkout milestone/M10   # or current stable branch
   cd ..
   
   # Create .ai-project.yml
   cat > .ai-project.yml << EOF
   governance:
     source: https://github.com/panchew/ai-project-system
     version: "2.0.0"
     ref: milestone/M10
   project:
     name: my-project
     description: "My project description"
   EOF
   
    # Install Governance Agent
    mkdir -p .github/agents
    cp governance/agents/governance.agent.md .github/agents/governance.agent.md
    
    # Commit
    git add .ai-project.yml .gitmodules governance .github
    git commit -m "chore: adopt AI Project System governance"
   ```

3. **Use the adoption startup prompt** once governance is installed:
   ```
   I want to adopt the AI Project System governance framework for my existing project at [repository-path].
   Initialize HQ Chat for this project, help me assess what's needed for adoption, and create a migration plan.
   ```

**Prevention:** When starting a new project from scratch, use `ai-project init` before adding any code. For existing projects, always use the migration guide.

**See also:** [Legacy Migration Guide](legacy-project-migration.md#workflow-b-governance-install), [ADOPTION-GUIDE.md Step 1](ADOPTION-GUIDE.md#step-1-initialize-your-project), [ADOPTION-GUIDE.md Step 4](ADOPTION-GUIDE.md#step-4-send-canonical-startup-prompt)

---

## 9. Governance Version Tag Issues

### Problem: `v2.0.0` tag not found when adding governance submodule

The guide says to use `v2.0.0` but `git checkout v2.0.0` fails with `pathspec 'v2.0.0' did not match any file(s) known to git`.

**Cause:** The git tag `v2.0.0` may not have been created yet in the governance source repository. Only the conceptual version number exists in `.ai-project.yml`.

**Solution:**

1. **Check available branches and tags:**
   ```bash
   cd governance
   git branch -r          # List remote branches
   git tag                # List tags
   cd ..
   ```

2. **Use a branch ref instead of a tag:**
   ```bash
   cd governance
   git fetch origin
   git checkout milestone/M10   # or: develop, master
   cd ..
   git add governance
   ```

3. **Update `.ai-project.yml` to match:**
   ```yaml
   governance:
     source: https://github.com/panchew/ai-project-system
     version: "milestone/M10"
     ref: milestone/M10
   ```

**Prevention:** Use tags for stability once they are created (`v2.0.0`, `v2.0.1`, etc.). During active development, branch refs (`milestone/M10`, `develop`) are acceptable but may change.

**See also:** [ADOPTION-GUIDE.md Step 2](ADOPTION-GUIDE.md#step-2-verify-governance-submodule)

---

## 10. General Governance Questions

### Problem: I do not understand the governance architecture, authority hierarchy, or process flow

Confusion about how the system works, who decides what, and how work flows through the system.

**Cause:** The governance model (Phase → Milestone → Epic hierarchy, authority separation, delivery process) is unfamiliar to new adopters.

**Solution:**

Review these key concepts:

**Architecture overview:**

```
HQ Chat (human decision-maker)
  │
  ▼
Phase (major segment of work)
  │
  ▼
Milestone (cohesive increment)
  │
  ▼
Epic (single deliverable)
  │
  ▼
Coding Agent (AI executor)
```

**Authority hierarchy (highest to lowest):**

1. PROJECT-SYSTEM-GUIDELINES.md
2. AI-OPERATING-GUIDELINES.md
3. Epic Execution Chat Starter
4. Epic Spec
5. Decisions
6. System References
7. Chat messages

**Canonical Epic lifecycle:**

```
Spec → Execute → Deliver → Review → Accept/Reject → Merge → Close
```

**Key principles:**

- **Documentation is authoritative, chat is ephemeral** — Knowledge lives in Markdown files, not chat history
- **AI assists, humans decide** — Coding Agents execute; HQ Chat (human) owns accept/reject decisions
- **Done must be explicit** — Every Epic has a Definition of Done checklist
- **Delivery follows hierarchy** — Branch merges must follow `epic/* → milestone/* → phase/* → develop/main`

**Prevention:** Read the governance documents in order:
1. [PROJECT-SYSTEM-GUIDELINES.md](../PROJECT-SYSTEM-GUIDELINES.md) — System structure and rules
2. [AI-OPERATING-GUIDELINES.md](../AI-OPERATING-GUIDELINES.md) — AI execution procedures
3. [ADOPTION-GUIDE.md](ADOPTION-GUIDE.md) — Step-by-step adoption walkthrough

**See also:** [FAQ.md](FAQ.md) — General system FAQ with philosophy and conceptual questions

---

## Still Have Questions?

- **Open an issue:** [GitHub Issues](https://github.com/panchew/ai-project-system/issues)
- **Review governance docs:** `governance/` in this repository
- **Check existing guides:** [guides/README.md](README.md) for the complete directory
