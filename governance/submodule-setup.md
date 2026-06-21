# Git Submodule Setup Guide

**Version:** 1.0.0  
**Status:** Active  
**Effective Date:** 2026-04-21  
**Introduced In:** Epic E6.4 (P2-M6)

---

## 1. Purpose

This guide documents the canonical procedure for referencing the AI Project System governance package from an external project using a **git submodule**. It covers:

- Adding governance as a submodule
- Pinning to a specific version
- Updating to a new version
- Team setup for new clones
- How the submodule relates to `.ai-project.yml` fields

The guide is intended to be followed directly and to be automated by the `ai-project init` CLI (M7).

---

## 2. The `.governance/` Convention

Governance submodules are installed at **`.governance/`** — a hidden folder at the repository root.

**Rationale:**
- The leading dot signals a system dependency, not project content. This is the same convention used for `.git/`, `.github/`, `.vscode/` — infrastructure, not artifacts.
- Keeping governance at a dedicated, predictable path allows HQ agents and CLI tools to discover it without configuration.
- Separating governance from project files prevents accidental modification of governance content.

**The canonical submodule path is `.governance/`. No other path is supported.**

---

## 3. How This Relates to `.ai-project.yml`

Your project's `.ai-project.yml` file (see [`governance/ai-project-yml-spec.md`](ai-project-yml-spec.md)) declares two fields that correspond directly to the submodule:

| `.ai-project.yml` field | What it maps to |
|-------------------------|-----------------|
| `governance.source` | The URL passed to `git submodule add` |
| `governance.version` | The semver string of the pinned governance release |
| `governance.ref` | The git ref (tag, branch, or SHA) checked out inside `.governance/` |

**Example `.ai-project.yml` for a project using governance via submodule:**

```yaml
# .ai-project.yml
governance:
  source: https://github.com/panchew/ai-project-system
  version: "4.0.0"
  ref: v4.0.0

project:
  name: my-project
  description: "My project using AI Project System governance"
```

The `governance.source` URL and the `governance.ref` value are the two parameters you supply during setup. Once the submodule is committed, `.ai-project.yml` records them so HQ agents can verify the pinned ref without reading `.gitmodules`.

---

## 4. Self-Referential Pattern (`ai-project-system` itself)

The `ai-project-system` repository is both the governance source and a project governed by itself. It does **not** use a submodule to reference its own governance.

Instead, its `.ai-project.yml` uses a local relative path:

```yaml
governance:
  source: ./governance
  version: "4.0.0"
  ref: master
```

This `./governance` path points directly to the `governance/` folder within the same repository. This is the **self-referential pattern** — valid only for the governance source repository itself.

External projects MUST use the HTTPS URL pattern, not a local path.

---

## 5. Procedure: Initial Setup (New Project)

Run these commands from your project's repository root.

### Step 1 — Add the submodule

```bash
git submodule add https://github.com/panchew/ai-project-system .governance
```

This clones `ai-project-system` into `.governance/` and creates a `.gitmodules` file. The submodule is initially checked out at the remote's default branch HEAD.

**After this step, `.governance/` contains governance files but is not yet pinned.** Proceed to Step 2.

### Step 2 — Pin to a specific version

```bash
cd .governance
git fetch
git checkout v4.0.0   # replace with your target version tag or ref
cd ..
```

Governance releases are tagged with semver prefixed `v` (e.g., `v4.0.0`). Always pin to a tag for reproducibility. If pinning to a branch (e.g., `milestone/M6`) during development, note that the pinned commit will advance as the branch moves — use a SHA or tag for stability in production projects.

### Step 3 — Commit the submodule and create `.ai-project.yml`

```bash
git add .governance .gitmodules
git commit -m "chore: add governance submodule pinned to v4.0.0"
```

Then create `.ai-project.yml` at the repository root:

```yaml
# .ai-project.yml
# AI Project System — Project Configuration Contract
# Spec: .governance/governance/ai-project-yml-spec.md v1.0.0

governance:
  source: https://github.com/panchew/ai-project-system
  version: "4.0.0"
  ref: v4.0.0

project:
  name: my-project
  description: "Short description of my project"
```

Commit it:

```bash
git add .ai-project.yml
git commit -m "chore: add .ai-project.yml pinned to governance v4.0.0"
```

---

## 6. Procedure: Updating to a New Governance Version

Run these commands from your project's repository root.

```bash
cd .governance
git fetch
git checkout v4.1.0   # replace with the target version
cd ..
git add .governance
git commit -m "chore: update governance submodule to v4.1.0"
```

Then update `.ai-project.yml` to reflect the new version:

```yaml
governance:
  source: https://github.com/panchew/ai-project-system
  version: "4.1.0"   # updated
  ref: v4.1.0        # updated
```

```bash
git add .ai-project.yml
git commit -m "chore: update .ai-project.yml to governance v4.1.0"
```

**Keep `.ai-project.yml` and the submodule pinned ref in sync.** A drift between `governance.ref` in `.ai-project.yml` and the actual checked-out commit in `.governance/` will be reported as a governance drift warning by the HQ agent.

---

## 7. Procedure: Team Setup (Clone with Submodules)

### New clone

```bash
git clone --recurse-submodules https://github.com/your-org/your-project
```

This clones the project and immediately populates `.governance/` at the pinned commit.

### Existing clone (submodule not yet initialized)

If you cloned without `--recurse-submodules`, `.governance/` will be an empty directory. Initialize it with:

```bash
git submodule update --init --recursive
```

This is the most common scenario for team members who cloned before the submodule was added.

### After pulling updates that change the pinned commit

When a teammate commits a governance version update, running `git pull` will advance the parent repository's recorded submodule commit. Git will not automatically update the submodule directory. Run:

```bash
git submodule update --recursive
```

This is safe and idempotent. Consider adding it to your project's `Makefile` or setup script.

---

## 8. Referencing Governance Files

Once `.governance/` is populated, all governance files are available at their full paths from your project root:

| Resource | Path |
|----------|------|
| Project System Guidelines | `.governance/governance/PROJECT-SYSTEM-GUIDELINES.md` |
| AI Operating Guidelines | `.governance/governance/AI-OPERATING-GUIDELINES.md` |
| `.ai-project.yml` spec | `.governance/governance/ai-project-yml-spec.md` |
| Submodule setup guide (this file) | `.governance/governance/submodule-setup.md` |
| Governance Agent definition | `.governance/governance/agents/governance.agent.md` |
| Epic spec template | `.governance/governance/templates/epic-spec.md` |
| All governance templates | `.governance/governance/templates/` |

### Agent deployment

The Governance Agent file lives in `.governance/governance/agents/governance.agent.md`. Copy it to `.github/agents/` for your AI tool to detect it:

```bash
mkdir -p .github/agents
cp .governance/governance/agents/governance.agent.md .github/agents/governance.agent.md
```

> **Note:** The single `governance.agent.md` replaces the previous separate `hq.agent.md`, `phase.agent.md`, and `milestone.agent.md` files. Remove any old `hq.agent.md` from `.github/agents/` if present.

Commit the agent:

```bash
git add .github/agents/governance.agent.md
git rm --ignore-unmatch .github/agents/hq.agent.md  # remove old version if present
git commit -m "chore: activate Governance Agent"
```

---

## 9. Edge Cases and Gotchas

### Submodule is in detached HEAD state after clone

When a team member runs `git submodule update --init`, the submodule is placed in **detached HEAD** state at the pinned commit. This is expected and correct. The submodule is not "on a branch" — it is pinned to a specific commit.

To work inside `.governance/` (e.g., to browse refs), you can run `git checkout milestone/M6` inside the submodule directory, but do not commit from there — submodule content is read-only from the perspective of the parent project.

### `git pull` does not update the submodule directory

Running `git pull` in the parent project updates `.gitmodules` and the recorded submodule commit, but does not update the files in `.governance/`. Always follow `git pull` with `git submodule update --recursive` when submodule changes may be included.

### Submodule shows as modified after `git checkout`

If you manually switch refs inside `.governance/`, the parent project will show `.governance` as a modified file. This is because the parent project tracks the submodule at a specific commit SHA. To restore the pinned state: `git submodule update`.

### No tags exist during pre-release development

If the target governance version has not yet been tagged (e.g., governance is still in development on `milestone/M6`), pin to the branch name or a specific SHA:

```bash
git checkout milestone/M6   # pin to branch (advances as branch moves)
# or
git checkout 23d4fc2        # pin to specific SHA (stable)
```

Update `.ai-project.yml` `governance.ref` to match. When a stable tag is released, update both.

### SSH vs HTTPS

Use HTTPS URLs (`https://github.com/panchew/ai-project-system`) for the submodule, not SSH (`git@github.com:...`). HTTPS works in CI environments and unauthenticated contexts without key configuration. SSH is not supported by the HQ agent or `ai-project init` CLI.

---

## 10. Quick Reference

```bash
# --- Initial setup ---
git submodule add https://github.com/panchew/ai-project-system .governance
cd .governance && git fetch && git checkout v4.0.0 && cd ..
git add .governance .gitmodules
git commit -m "chore: add governance submodule pinned to v4.0.0"

# --- Update to new version ---
cd .governance && git fetch && git checkout v4.1.0 && cd ..
git add .governance
git commit -m "chore: update governance submodule to v4.1.0"

# --- New team member: clone ---
git clone --recurse-submodules https://github.com/your-org/your-project

# --- Existing clone: initialize ---
git submodule update --init --recursive

# --- After git pull (if submodule commit changed) ---
git submodule update --recursive
```

---

## Related Documents

- [`.ai-project.yml` Specification](ai-project-yml-spec.md) — Full schema for the project configuration file
- [PROJECT-SYSTEM-GUIDELINES.md](PROJECT-SYSTEM-GUIDELINES.md) — Canonical governance rules
- [AI-OPERATING-GUIDELINES.md](AI-OPERATING-GUIDELINES.md) — Agent operating guidelines
