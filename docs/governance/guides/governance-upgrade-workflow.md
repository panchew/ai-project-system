---
title: Governance Version Upgrade Workflow
status: draft
last_updated: 2026-05-04
applies_to: Project instances using this system
---

# Governance Version Upgrade Workflow

This guide defines a safe, repeatable procedure to upgrade a project to a newer governance version while preserving state and enabling deterministic validation and rollback.

Audience: project maintainers and HQ operators.

Scope: upgrades within the same governance repository (default: `https://github.com/panchew/governance`). Private repos or cross-repo migrations are out of scope for M8.

Note: Upgrades are explicit, operator-initiated actions. No automatic upgrades.

## Prerequisites

- A clean working tree: no uncommitted changes or staged files
- Current branch is the project’s active integration branch
- Network access to the governance repository
- `git` installed; optionally `yq` for YAML edits

Quick checks:

```bash
git status --porcelain=v1  # must print nothing
git submodule status       # governance submodule must be initialized
test -f .ai-project.yml
```

## Read Current Governance Version

The current version is pinned in `.ai-project.yml`:

```yaml
governance:
  source: https://github.com/panchew/governance  # git repo URL
  version: <tag|branch|commit>
  submodule_path: governance
```

Commands to print current version and submodule target:

```bash
# YAML value (portable: grep/sed fallback if yq absent)
if command -v yq >/dev/null 2>&1; then
  cur_ver=$(yq -r '.governance.version' .ai-project.yml)
else
  cur_ver=$(sed -n 's/^\s*version:\s*//p' .ai-project.yml | head -n1)
fi
echo "Current governance.version: $cur_ver"

# Submodule commit currently pinned in the repo
git submodule status governance || true
```

## Discover Available Target Versions

Use tags for stable releases, branches for ongoing tracking, or a commit hash for precise pinning.

```bash
repo_url=$(sed -n 's/^\s*source:\s*//p' .ai-project.yml | head -n1)
[ -z "$repo_url" ] && repo_url=https://github.com/panchew/governance

# List tags (preferred release versions)
git ls-remote --tags "$repo_url" | awk '{print $2}' | sed 's#refs/tags/##' | sort -V | tail -n 30

# List branches (if you intend to track a branch)
git ls-remote --heads "$repo_url" | awk '{print $2}' | sed 's#refs/heads/##' | sort
```

Validation of a chosen target (example variable `target`):

```bash
target=v2.0.0  # or master, or a commit hash

# Verify it exists as tag/branch or is a valid 40-hex commit in the remote
if git ls-remote "$repo_url" "refs/tags/$target" | grep -q .; then echo "Target is a tag"; 
elif git ls-remote "$repo_url" "refs/heads/$target" | grep -q .; then echo "Target is a branch"; 
elif [[ "$target" =~ ^[0-9a-f]{7,40}$ ]] && git ls-remote "$repo_url" | grep -qi "$target"; then echo "Target is a commit"; 
else echo "ERROR: Target version not found in remote" >&2; exit 1; fi
```

## Update `.ai-project.yml` (Safe Procedure)

Always preserve non-governance fields and comments. Prefer `yq` if available; otherwise use in-place edit with a backup and review.

```bash
target=v2.0.0

if command -v yq >/dev/null 2>&1; then
  yq -i 
    '.governance.version = env(target)' 
    .ai-project.yml
else
  cp .ai-project.yml .ai-project.yml.bak
  awk -v tgt="$target" '
    BEGIN{re=0}
    /^\s*governance:/ {re=1}
    re && /^\s*version:/ {$0="  version: " tgt; re=0}
    {print}
  ' .ai-project.yml.bak > .ai-project.yml
fi

git add .ai-project.yml
git commit -m "chore(governance): bump governance.version -> $target"
```

## Refresh `governance/` Submodule to Target Version

Submodules pin an exact commit. To align the submodule to the selected target:

```bash
path=$(sed -n 's/^\s*submodule_path:\s*//p' .ai-project.yml | head -n1)
[ -z "$path" ] && path=governance

git submodule update --init --recursive "$path"
pushd "$path" >/dev/null
  git fetch --tags --prune
  git checkout --detach "$target"  # works for tags, branches, or commits
  # If tracking a branch is desired, replace with: git switch -c upgrade/tmp "$target"
popd >/dev/null

git add "$path"
git commit -m "chore(governance): refresh submodule to $target"
```

Optional: to persist a branch-tracking behavior for the submodule (not recommended for releases), set the tracked branch in `.gitmodules`:

```bash
branch_to_track=master
git submodule set-branch --branch "$branch_to_track" "$path"
git add .gitmodules
git commit -m "chore(governance): set submodule branch -> $branch_to_track"
```

## Validate the Upgrade

Perform deterministic checks to ensure the governance content is present and readable.

```bash
test -d "$path" && test -f "$path/PROJECT-SYSTEM-GUIDELINES.md"
test -f "$path/AI-OPERATING-GUIDELINES.md"

# Confirm YAML and submodule pointer committed
grep -E '^\s*version:\s*' .ai-project.yml
git submodule status "$path"

# Optional integrity spot checks
git -C "$path" rev-parse --short HEAD
git -C "$path" log --oneline -n 1
```

Project usability smoke check (non-destructive):

```bash
# Example: verify a key system doc is readable
sed -n '1,40p' "$path/PROJECT-SYSTEM-GUIDELINES.md" | sed -n '1,10p'
```

## Rollback and Recovery

If validation fails or the project shows regressions, revert to the previous version.

```bash
# 1) Revert YAML change
git checkout -- .ai-project.yml

# 2) Reset submodule back to the previously recorded commit
git submodule update --init --recursive --checkout "$path"

# 3) If you created commits during upgrade, revert them cleanly
#    (use commit hashes from git log)
git log --oneline -n 5
git revert <commit_that_updated_submodule> <commit_that_updated_yaml>

# 4) Validate again
git submodule status "$path"
grep -E '^\s*version:\s*' .ai-project.yml
```

If conflicts arise during revert, pause and escalate for manual resolution. Do not force-push without review.

## Error Handling and Common Issues

- Missing target version: ensure the tag/branch exists in the remote; check `repo_url` and network access
- Dirty working tree: stash or commit changes before attempting an upgrade
- Submodule detached HEAD warnings: expected when pinning to a specific commit or tag
- Permission or 2FA errors: configure git credentials; private governance repos are out of scope in M8
- Diverged submodule commit: run `git submodule update --recursive --checkout` to sync to the recorded commit

Operator-facing message patterns:

- "Target version not found" → Verify spelling, list tags/branches with `git ls-remote`, or choose a released tag
- "Working tree not clean" → Run `git status`, `git stash -u`, then retry
- "Submodule not initialized" → Run `git submodule update --init --recursive governance`

## End-to-End Example (Happy Path)

```bash
target=v2.0.0
repo_url=https://github.com/panchew/governance
path=governance

git status --porcelain=v1 | wc -l | grep -q '^0$' || { echo "Working tree must be clean"; exit 1; }

git ls-remote --tags "$repo_url" | grep -q "refs/tags/$target$" || { echo "Tag $target not found"; exit 1; }

yq -i '.governance.version = env(target)' .ai-project.yml || {
  cp .ai-project.yml .ai-project.yml.bak && 
  sed -n '1,200p' .ai-project.yml.bak >/dev/null && 
  awk -v tgt="$target" 'BEGIN{re=0} /^\s*governance:/{re=1} re&&/^\s*version:/{ $0="  version: " tgt; re=0 } {print}' .ai-project.yml.bak > .ai-project.yml
}

git add .ai-project.yml && git commit -m "chore(governance): bump governance.version -> $target"

git submodule update --init --recursive "$path"
git -C "$path" fetch --tags --prune
git -C "$path" checkout --detach "$target"

git add "$path" && git commit -m "chore(governance): refresh submodule to $target"

test -f "$path/PROJECT-SYSTEM-GUIDELINES.md" && test -f "$path/AI-OPERATING-GUIDELINES.md"
git submodule status "$path"
```

## Notes and Policy

- Documentation is authoritative; chat is ephemeral
- Stop after PR creation and await HQ authorization for merge
- No automatic upgrades or auto-resolution of merge conflicts
- Keep commits small and descriptive for easier review and rollback
