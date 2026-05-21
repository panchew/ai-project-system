---
title: Library Project Configuration Example
type: example
phase: P2
milestone: M9
epic: E9.4
status: active
last_updated: 2026-05-21
---

# Library Project — `.ai-project.yml` Example

## Project Profile

A **library project** packages reusable code (utilities, components, SDKs) for consumption by other projects. Libraries follow standard conventions because they are typically built and published by CI/CD pipelines, and their governance needs are minimal.

**Characteristics:**
- Published as a package (npm, PyPI, Maven, etc.)
- Consumed by multiple downstream projects
- Standard branching and merging conventions apply
- Low risk of governance conflicts

## Configuration

```yaml
# .ai-project.yml
# Library project — uses all governance defaults
# Spec: governance/ai-project-yml-spec.md

governance:
  source: https://github.com/panchew/ai-project-system
  version: "2.0.0"
  ref: v2.0.0

project:
  name: acme-utils
  description: "Shared utility library for ACME services"

# No overrides block — all governance defaults apply:
#   branch_strategy: trunk-based
#   merge_strategy: merge
#   epic_prefix: epic/
```

### Alternative Overrides (Commented Out)

If a library team needs custom overrides, uncomment and adjust:

```yaml
# overrides:
#   merge_strategy: squash          # optional: squash for cleaner changelogs
#   epic_prefix: feature/           # optional: match team convention
```

## Override Rationale

Libraries use **no overrides** because:

| Reason | Detail |
|--------|--------|
| Standard conventions | Libraries rarely need custom branch or merge strategies |
| Consumer-driven | Customization happens in the consuming project, not the library |
| Minimal overhead | Defaults (`trunk-based`, `merge`, `epic/`) work well for library workflows |
| CI/CD alignment | Most CI/CD pipelines expect standard branch naming and merge strategies |

## Expected Behavior

With no overrides, the HQ agent applies governance defaults:

| Dimension | Default Value | Effect |
|-----------|---------------|--------|
| Branch strategy | `trunk-based` | Standard `epic/*` → `milestone/*` → `phase/*` → `develop` hierarchy |
| Merge strategy | `merge` | Standard merge commits in PR descriptions |
| Epic prefix | `epic/` | Branches named `epic/E<id>` (e.g., `epic/E9.4`) |

Generated artifacts (specs, chat starters, branch references) use these default values.

## Validation

The configuration above passes all validation rules from `ai-project-yml-spec.md` §4:

| # | Rule | Result |
|---|------|--------|
| 1 | File exists and is valid YAML | ✅ Valid YAML — parseable without errors |
| 2 | Required fields present | ✅ `governance.source`, `governance.version`, `governance.ref`, `project.name`, `project.description` all present |
| 3 | `governance.source` is HTTPS URL or relative path | ✅ `https://github.com/panchew/ai-project-system` — valid HTTPS URL |
| 4 | `governance.version` is quoted semver | ✅ `"2.0.0"` — quoted string, valid semver |
| 5 | `governance.ref` is non-empty string | ✅ `v2.0.0` — non-empty |
| 6 | `project.name` matches `^[a-z][a-z0-9-]*$` | ✅ `acme-utils` — lowercase with hyphen |
| 7 | `project.description` is non-empty | ✅ `"Shared utility library for ACME services"` — non-empty |
| 8 | Override values valid (overrides block absent) | ✅ No overrides block — rule 8 N/A, rules 9–13 not triggered |

**Validation result: PASS** — All required fields present and correct. No overrides block, so all governance defaults apply.
