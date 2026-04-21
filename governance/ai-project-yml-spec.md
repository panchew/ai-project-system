# `.ai-project.yml` Specification

**Version:** 1.0.0  
**Status:** Active  
**Effective Date:** 2026-04-20  
**Introduced In:** Epic E6.3 (P2-M6)

---

## 1. Purpose

`.ai-project.yml` is the **project configuration contract** for any project using the AI Project System governance framework. It declares:

- Where the project's governance source lives (URL or local path)
- Which governance version the project is pinned to
- Optional project-specific overrides of governance defaults

This file is the single authoritative source of truth for governance discovery. Every project using the AI Project System MUST have a `.ai-project.yml` at its repository root.

---

## 2. File Location

```
<repository-root>/.ai-project.yml
```

The file MUST be at the repository root. No other location is valid.

---

## 3. Schema

### 3.1 Full Schema Reference

```yaml
# .ai-project.yml
# AI Project System — Project Configuration Contract

governance:
  source: <string>       # REQUIRED. URL or path to governance source repository.
  version: <string>      # REQUIRED. Pinned governance version (semver).
  ref: <string>          # REQUIRED. Git ref (tag, branch, or SHA) on the governance source.

project:
  name: <string>         # REQUIRED. Unique project identifier (slug format).
  description: <string>  # REQUIRED. Short human-readable project description.

overrides:               # OPTIONAL. Project-specific governance overrides. Full spec: M9.
  branch_strategy: <string>   # default: trunk-based
  merge_strategy: <string>    # default: merge
  epic_prefix: <string>       # default: epic/
```

---

### 3.2 Required Fields

#### `governance.source`

| Property    | Value |
|-------------|-------|
| Type        | String |
| Required    | Yes |
| Format      | HTTPS URL or relative filesystem path |
| Constraint  | Must be a valid HTTPS URL or a relative path starting with `./` or `../` |

Declares the canonical governance source. For projects that use the `ai-project-system` as an external reference (e.g., via Git submodule or URL), this is the URL of the upstream governance repository. For projects that embed governance locally, this is the relative path to the governance root.

**Valid examples:**
```yaml
source: https://github.com/panchew/ai-project-system      # external URL
source: ./governance                                        # local relative path (self-referential)
source: ./.governance-submodule                            # submodule at repo root
```

**Invalid:**
```yaml
source: /absolute/path                                     # absolute paths are not allowed
source: git@github.com:panchew/ai-project-system.git      # SSH URLs are not allowed
```

---

#### `governance.version`

| Property    | Value |
|-------------|-------|
| Type        | String |
| Required    | Yes |
| Format      | Semantic version (`MAJOR.MINOR.PATCH`) |
| Constraint  | Must be a valid semver string (e.g., `"2.0.0"`). Quoted to preserve string type. |

Declares the pinned governance version. The HQ agent and CLI use this field to detect governance drift between a project and its governance source.

**Valid examples:**
```yaml
version: "2.0.0"
version: "1.4.2"
```

**Invalid:**
```yaml
version: 2.0.0          # unquoted — YAML may parse as float; must be quoted
version: latest          # non-pinned refs are not allowed in this field
version: "^2.0.0"        # range specifiers are not allowed
```

---

#### `governance.ref`

| Property    | Value |
|-------------|-------|
| Type        | String |
| Required    | Yes |
| Format      | Git tag, branch name, or full SHA |
| Constraint  | Must be a valid Git ref resolvable on the `governance.source` repository |

Declares the exact Git ref on the governance source that corresponds to `governance.version`. The CLI and HQ agent use this ref when fetching or syncing governance files.

**Valid examples:**
```yaml
ref: v2.0.0              # tag (preferred for pinned governance)
ref: milestone/M6        # branch
ref: a1b2c3d4e5f6...     # full SHA (40 characters)
```

---

#### `project.name`

| Property    | Value |
|-------------|-------|
| Type        | String |
| Required    | Yes |
| Format      | Slug (lowercase, hyphens allowed, no spaces) |
| Constraint  | Must match `^[a-z][a-z0-9-]*$`. Must be unique within the organization. |

Human-readable identifier used in logs, CLI output, and governance artifact metadata.

**Valid examples:**
```yaml
name: my-project
name: ai-project-system
name: acme-payments-service
```

---

#### `project.description`

| Property    | Value |
|-------------|-------|
| Type        | String |
| Required    | Yes |
| Format      | Free text, single line |
| Constraint  | Must be non-empty. Keep under 120 characters. Must be quoted if it contains `:` or `#`. |

Short human-readable description of the project. Used in CLI output and governance artifact headers.

**Valid examples:**
```yaml
description: "Payment processing microservice for ACME Corp"
description: "AI Project System governance source repository"
```

---

### 3.3 Optional Fields — `overrides`

The `overrides` block is **optional**. When absent, all governance defaults apply.

> **Note:** Full override specification is deferred to M9. The fields below are stubbed to establish the schema contract. Values other than the listed options are not yet defined.

| Field | Type | Default | Allowed Values (M6) | Description |
|-------|------|---------|---------------------|-------------|
| `branch_strategy` | String | `trunk-based` | `trunk-based`, `gitflow` | Branch naming and promotion strategy |
| `merge_strategy` | String | `merge` | `merge`, `squash`, `rebase` | Default PR merge method |
| `epic_prefix` | String | `epic/` | Any string ending in `/` | Prefix for epic branch names |

When `overrides` is present, only listed keys are recognized. Unknown override keys MUST be ignored by tooling in M6/M7/M8; validation of unknown keys is reserved for M9.

---

## 4. Validation Rules

A `.ai-project.yml` file is **valid** when all of the following are true:

1. The file exists at the repository root as `.ai-project.yml`
2. The file is valid YAML (parseable without errors)
3. All four required fields are present: `governance.source`, `governance.version`, `governance.ref`, `project.name`, `project.description`
4. `governance.source` is an HTTPS URL or a relative path starting with `./` or `../`
5. `governance.version` is a quoted semver string matching `\d+\.\d+\.\d+`
6. `governance.ref` is a non-empty string
7. `project.name` matches `^[a-z][a-z0-9-]*$`
8. `project.description` is a non-empty string

A `.ai-project.yml` file is **invalid** if any required field is absent, any constraint above is violated, or the file is not valid YAML.

---

## 5. How the HQ Agent Uses This File

The HQ agent reads `.ai-project.yml` on startup to self-configure. Specifically:

- **`governance.source` + `governance.ref`**: Used to locate and fetch governance documents (guidelines, templates, systems). The agent resolves the governance source and checks out the specified ref.
- **`governance.version`**: Used to detect governance drift. The agent compares this value against the version declared in `PROJECT-SYSTEM-GUIDELINES.md` at the resolved ref. If they differ, the agent warns the user.
- **`project.name` + `project.description`**: Used in agent output headers and log entries.
- **`overrides`**: Consulted when the agent applies governance rules (e.g., determining branch naming conventions). Overrides take precedence over defaults.

The HQ agent MUST NOT proceed with execution if `.ai-project.yml` is absent or invalid.

---

## 6. How `ai-project init` Uses This File

When a user runs `ai-project init`, the CLI:

1. Prompts for `project.name`, `project.description`, `governance.source`, `governance.version`, and `governance.ref`
2. Scaffolds `.ai-project.yml` at the repository root using the provided values
3. Validates the resulting file against the rules in Section 4
4. Reports success or validation errors

`ai-project init` MUST NOT overwrite an existing `.ai-project.yml` without explicit `--force` confirmation.

---

## 7. Governance Version Sync

When the governance source releases a new version:

1. The project maintainer updates `governance.version` and `governance.ref` in `.ai-project.yml`
2. The HQ agent (or CLI, in M9) fetches the new governance files from `governance.source` at the new `governance.ref`
3. Updated governance files are committed to the project repository
4. The change is recorded in a decision document under `docs/decisions/`

**Manual sync (M6/M7):** In M6 and M7, governance sync is a manual process. The project maintainer is responsible for detecting new versions and updating `.ai-project.yml` accordingly.

**Automated sync (future):** Automated sync tooling is deferred to a future milestone.

---

## 8. Self-Referential Usage (Governance Source Repositories)

For repositories that ARE the governance source (i.e., `ai-project-system` itself), the `governance.source` field uses a local relative path pointing to the governance folder within the same repository:

```yaml
governance:
  source: ./governance
  version: "2.0.0"
  ref: v2.0.0
```

This is the canonical self-referential pattern. It confirms that the repository uses its own governance, which the HQ agent handles as a special case (no external fetch required; governance is always at `./governance`).

---

## 9. Minimal Valid Example

```yaml
# .ai-project.yml
governance:
  source: https://github.com/panchew/ai-project-system
  version: "2.0.0"
  ref: v2.0.0

project:
  name: my-project
  description: "My project using the AI Project System"
```

---

## 10. Full Example with Overrides

```yaml
# .ai-project.yml
governance:
  source: https://github.com/panchew/ai-project-system
  version: "2.0.0"
  ref: v2.0.0

project:
  name: acme-payments
  description: "Payment processing service for ACME Corp"

overrides:
  branch_strategy: gitflow
  merge_strategy: squash
  epic_prefix: feature/
```

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-04-20 | Initial specification (Epic E6.3, P2-M6) |
