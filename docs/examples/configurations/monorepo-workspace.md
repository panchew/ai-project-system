---
title: Monorepo Workspace Configuration Example
type: example
phase: P2
milestone: M9
epic: E9.4
status: active
last_updated: 2026-05-21
---

# Monorepo Workspace — `.ai-project.yml` Example

## Project Profile

A **monorepo workspace** hosts multiple packages, services, or libraries in a single repository. Monorepos require extra coordination for multi-package releases and benefit from linear history across many contributors.

**Characteristics:**
- Multiple independently versioned packages or services
- Many contributors working across different areas
- Coordinated releases across packages
- High value on clean, linear commit history for auditability

## Configuration

```yaml
# .ai-project.yml
# Monorepo workspace — gitflow, rebase, feature prefix
# Spec: governance/ai-project-yml-spec.md

governance:
  source: https://github.com/panchew/ai-project-system
  version: "2.0.0"
  ref: v2.0.0

project:
  name: acme-platform
  description: "ACME Corp platform monorepo — services, libraries, and tooling"

overrides:
  branch_strategy: gitflow
  merge_strategy: rebase
  epic_prefix: feature/
```

## Override Rationale

### `branch_strategy: gitflow`

| Aspect | Detail |
|--------|--------|
| **Why** | Gitflow adds a long-lived `develop` branch that serves as an integration branch between `phase/*` and `main` |
| **Benefit** | Multiple concurrent release streams (e.g., v1 maintenance, v2 development) can coexist |
| **Trade-off** | More branch management overhead; requires discipline to keep `develop` stable |
| **Use case** | Monorepos with coordinated multi-package releases where `develop` is the integration point |

**How gitflow changes the branch hierarchy:**

| Standard (`trunk-based`) | Gitflow |
|--------------------------|---------|
| `epic/*` → `milestone/*` → `phase/*` → `develop` | `epic/*` → `milestone/*` → `phase/*` → `develop` → `main` |
| Milestones merge directly to `develop` | Milestones merge to `develop` first, then promoted to `main` |

### `merge_strategy: rebase`

| Aspect | Detail |
|--------|--------|
| **Why** | Rebase produces a perfectly linear commit history with no merge commits |
| **Benefit** | Essential for monorepos where bisecting and auditing across many packages requires a clean DAG |
| **Trade-off** | Contributors must rebase locally before pushing; conflicts resolved on the contributor's branch |
| **Use case** | Large monorepos with many contributors where linear history simplifies `git bisect` and blame |

### `epic_prefix: feature/`

| Aspect | Detail |
|--------|--------|
| **Why** | `feature/` is a widely recognized monorepo convention that matches existing tooling expectations |
| **Benefit** | Consistency with conventional monorepo branch naming; aligns with CI/CD triggers |
| **Effect** | Epic branches are created as `feature/E<id>` instead of `epic/E<id>` |

## Expected Behavior

With these overrides, the HQ agent generates artifacts as follows:

| Dimension | Override Value | Effect on Artifacts |
|-----------|---------------|-------------------|
| Branch strategy | `gitflow` | Milestone branches promote to `develop` before `main`; chat starters reference the `develop` integration branch |
| Merge strategy | `rebase` | PR descriptions reference rebase merge; merge instructions say "Rebase onto target before merge" |
| Epic prefix | `feature/` | Branches named `feature/E<id>`; specs and chat starters use `feature/E<id>` |

**Example branch names generated:**
- Epic branch: `feature/E9.4`
- Milestone branch: `milestone/M9`
- Phase branch: `phase/P2`
- Integration branch: `develop` (gitflow addition)

**Example merge instruction in PR description:**
> "This PR merges `feature/E9.4` into `milestone/M9` using rebase. Milestone will promote to `develop` before merging to `main`."

## Validation

The configuration above passes all validation rules from `ai-project-yml-spec.md` §4:

| # | Rule | Result |
|---|------|--------|
| 1 | File exists and is valid YAML | ✅ Valid YAML — parseable without errors |
| 2 | Required fields present | ✅ `governance.source`, `governance.version`, `governance.ref`, `project.name`, `project.description` all present |
| 3 | `governance.source` is HTTPS URL or relative path | ✅ `https://github.com/panchew/ai-project-system` — valid HTTPS URL |
| 4 | `governance.version` is quoted semver | ✅ `"2.0.0"` — quoted string, valid semver |
| 5 | `governance.ref` is non-empty string | ✅ `v2.0.0` — non-empty |
| 6 | `project.name` matches `^[a-z][a-z0-9-]*$` | ✅ `acme-platform` — lowercase with hyphen |
| 7 | `project.description` is non-empty | ✅ `"ACME Corp platform monorepo — services, libraries, and tooling"` — non-empty |
| 8 | Override values valid per field constraints | ✅ All three overrides checked individually below |
| 9 | Overrides block is valid YAML | ✅ Part of top-level YAML — no parse errors |
| 10a | `branch_strategy` constraint | ✅ `gitflow` — valid (one of `trunk-based`, `gitflow`) |
| 10b | `merge_strategy` constraint | ✅ `rebase` — valid (one of `merge`, `squash`, `rebase`) |
| 10c | `epic_prefix` constraint | ✅ `feature/` — ends with `/`, non-empty |
| 11 | Unknown keys produce warning (not error) | ✅ No unknown keys present |
| 12 | Invalid override values produce error | ✅ All values valid — no errors |

**Validation result: PASS** — All required fields present and correct. All three override values are valid per spec constraints.
