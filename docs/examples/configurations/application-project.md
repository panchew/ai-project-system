---
title: Application Project Configuration Example
type: example
phase: P2
milestone: M9
epic: E9.4
status: active
last_updated: 2026-05-21
---

# Application Project — `.ai-project.yml` Example

## Project Profile

An **application project** ships code to production (web service, CLI tool, mobile app). Application teams typically value clean release histories and may adopt team-specific branch naming conventions.

**Characteristics:**
- Deployed to production environments
- Multiple contributors working on features concurrently
- Release tracking requires clean commit history
- Teams often have established branch naming conventions

## Configuration

```yaml
# .ai-project.yml
# Application project — squash merges, feature prefix
# Spec: governance/ai-project-yml-spec.md

governance:
  source: https://github.com/panchew/ai-project-system
  version: "2.0.0"
  ref: v2.0.0

project:
  name: acme-payments
  description: "Payment processing service for ACME Corp"

overrides:
  merge_strategy: squash
  epic_prefix: feature/
```

## Override Rationale

### `merge_strategy: squash`

| Aspect | Detail |
|--------|--------|
| **Why** | Squash merges collapse all feature branch commits into a single commit on the target branch |
| **Benefit** | Clean, linear release history — each merge corresponds to one logical feature |
| **Trade-off** | Individual commit-level detail is lost; use descriptive PR titles |
| **Use case** | Services deployed to production where changelogs map to features, not individual commits |

### `epic_prefix: feature/`

| Aspect | Detail |
|--------|--------|
| **Why** | Many application teams already use `feature/` as a branch prefix convention |
| **Benefit** | Aligns governance branch naming with existing team workflow |
| **Effect** | Epic branches are created as `feature/E<id>` instead of `epic/E<id>` |
| **Use case** | Teams with established `feature/` naming in their development process |

## Expected Behavior

With these overrides, the HQ agent generates artifacts using custom values:

| Dimension | Override Value | Effect on Artifacts |
|-----------|---------------|-------------------|
| Branch strategy | `trunk-based` (default) | Standard branch hierarchy — no change |
| Merge strategy | `squash` | PR descriptions reference squash merge; merge instructions say "Merge using squash" |
| Epic prefix | `feature/` | Branches named `feature/E<id>` (e.g., `feature/E9.4`); specs and chat starters use `feature/E9.4` |

**Example branch names generated:**
- Epic branch: `feature/E9.4`
- Milestone branch: `milestone/M9`
- Phase branch: `phase/P2`

**Example merge instruction in PR description:**
> "This PR merges `feature/E9.4` into `milestone/M9` using squash."

## Validation

The configuration above passes all validation rules from `ai-project-yml-spec.md` §4:

| # | Rule | Result |
|---|------|--------|
| 1 | File exists and is valid YAML | ✅ Valid YAML — parseable without errors |
| 2 | Required fields present | ✅ `governance.source`, `governance.version`, `governance.ref`, `project.name`, `project.description` all present |
| 3 | `governance.source` is HTTPS URL or relative path | ✅ `https://github.com/panchew/ai-project-system` — valid HTTPS URL |
| 4 | `governance.version` is quoted semver | ✅ `"2.0.0"` — quoted string, valid semver |
| 5 | `governance.ref` is non-empty string | ✅ `v2.0.0` — non-empty |
| 6 | `project.name` matches `^[a-z][a-z0-9-]*$` | ✅ `acme-payments` — lowercase with hyphen |
| 7 | `project.description` is non-empty | ✅ `"Payment processing service for ACME Corp"` — non-empty |
| 8 | Override values valid per field constraints | ✅ `merge_strategy: squash` — valid (one of `merge`, `squash`, `rebase`) |
| 9 | Overrides block is valid YAML | ✅ Part of top-level YAML — no parse errors |
| 10a | `branch_strategy` constraint | ✅ Not set — defaults to `trunk-based` |
| 10b | `merge_strategy` constraint | ✅ `squash` — valid allowed value |
| 10c | `epic_prefix` constraint | ✅ `feature/` — ends with `/`, non-empty |
| 11 | Unknown keys produce warning (not error) | ✅ No unknown keys present |
| 12 | Invalid override values produce error | ✅ All values valid — no errors |

**Validation result: PASS** — All required fields present and correct. Both override values are valid per spec constraints. Unknown keys not present.
