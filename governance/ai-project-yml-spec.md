# `.ai-project.yml` Specification

**Version:** 2.3.0  
**Status:** Active  
**Effective Date:** 2026-07-13  
**Introduced In:** Epic E6.3 (P2-M6); override specification completed in Epic E9.1 (P2-M9); `visual_artifacts` block added in Epic E22.1 (P5-M22); `epic_dev` default moved to a tool-calling-capable model in Epic E26.2 (P7-M26); `visual_artifacts` flipped to default-on and `visual_required_for_specs` enforcement key added in Epic E27.1 (P7-M27)

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

models:                  # OPTIONAL. Hybrid model routing maps for autonomous clusters.
  hq: <string>           # default: remote:gpt-4o
  phase: <string>        # default: remote:claude-3-5-sonnet
  milestone: <string>    # default: remote:claude-3-5-sonnet
  epic_dev: <string>     # default: local:qwen2.5-coder:14b
  epic_qa: <string>      # default: local:qwen2.5-coder:7b

visual_artifacts:        # OPTIONAL. Default-on visual-artifact generation. Absent ⇒ enabled. Full spec: M22/M27.
  enabled: <bool>        # default: true. false is the explicit opt-out.
  comfyui_url: <string>  # default: http://localhost:8188. Generative endpoint (well-formed URL when present).
  types:                 # OPTIONAL. Subset of: diagrams, infographics, video.
    - diagrams
    - infographics
    - video
  visual_required_for_specs: <bool>  # default: true. Enforcement setting for specs.
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

Each field in the `overrides` block customizes a specific governance dimension. Override values take precedence over governance defaults but are overridden by local project conventions (see [Precedence](#precedence)).

For a complete enumeration of all overridable and non-overridable governance dimensions with rationale, constraints, and boundary rules, see the Override Boundaries document:

```
governance/override-boundaries.md
```

| Field | Type | Default | Allowed Values | Constraint | Behavioral Effect |
|-------|------|---------|----------------|------------|-------------------|
| `branch_strategy` | String | `trunk-based` | `trunk-based`, `gitflow` | Must be one of the allowed values | Controls branch naming and promotion strategy. `trunk-based`: standard `epic/*` → `milestone/*` → `phase/*` → `develop` hierarchy. `gitflow`: an additional long-lived `develop` branch is expected between `phase/*` and `main`. |
| `merge_strategy` | String | `merge` | `merge`, `squash`, `rebase` | Must be one of the allowed values | Sets the default PR merge method. `merge`: standard merge commit. `squash`: squash all commits into one. `rebase`: rebase onto target before merge (fast-forward). Individual PRs may override at merge time. |
| `epic_prefix` | String | `epic/` | Any string ending with `/` | Must end with `/`; must not be empty | Customizes the prefix for epic branch names. The HQ agent generates branches as `<prefix>E<id>` (e.g., `feature/E9.1`). Affects all epic branch creation and references in generated artifacts. |

#### Field Details

##### `overrides.branch_strategy`

| Property | Value |
|----------|-------|
| Type | String |
| Required | No |
| Default | `trunk-based` |
| Allowed Values | `trunk-based`, `gitflow` |
| Constraint | Must be one of the allowed values. Case-sensitive. |
| Validation Error | `"Invalid branch_strategy: '<value>'. Must be one of: trunk-based, gitflow."` |

When set to `trunk-based`, the standard branch hierarchy (`epic/*` → `milestone/*` → `phase/*` → `develop`) applies. When set to `gitflow`, the system expects an additional long-lived `develop` branch between `phase/*` and `main`, and promotes milestone branches to `develop` before merging to `main`.

**Valid examples:**
```yaml
branch_strategy: trunk-based
branch_strategy: gitflow
```

**Invalid:**
```yaml
branch_strategy: git-flow    # hyphen instead of underscore
branch_strategy: trunk       # not an allowed value
```

---

##### `overrides.merge_strategy`

| Property | Value |
|----------|-------|
| Type | String |
| Required | No |
| Default | `merge` |
| Allowed Values | `merge`, `squash`, `rebase` |
| Constraint | Must be one of the allowed values. Case-sensitive. |
| Validation Error | `"Invalid merge_strategy: '<value>'. Must be one of: merge, squash, rebase."` |

Sets the default merge method for pull requests across the project. Individual PRs may override at merge time. The HQ agent references this value when generating PR descriptions and merge instructions.

**Valid examples:**
```yaml
merge_strategy: merge
merge_strategy: squash
merge_strategy: rebase
```

**Invalid:**
```yaml
merge_strategy: fast-forward-only  # not an allowed value
merge_strategy: MERGE              # case-sensitive
```

---

##### `overrides.epic_prefix`

| Property | Value |
|----------|-------|
| Type | String |
| Required | No |
| Default | `epic/` |
| Allowed Values | Any non-empty string ending with `/` |
| Constraint | Must end with `/`. Must not be empty. |
| Validation Error | `"Invalid epic_prefix: '<value>'. Must end with '/' and must not be empty."` |

Customizes the prefix used for epic branch names. The HQ agent applies this prefix when generating epic branches, milestone specs, epic specs, and chat starters. All generated branch references use the custom prefix instead of the default `epic/`.

The prefix is used in branch names as `<prefix>E<id>` (e.g., with `feature/` the branch for Epic E9.1 becomes `feature/E9.1`).

**Valid examples:**
```yaml
epic_prefix: feature/
epic_prefix: topic/
epic_prefix: epic/
```

**Invalid:**
```yaml
epic_prefix: feature      # missing trailing /
epic_prefix: ""            # empty string
epic_prefix: /epic         # leading / is allowed but unusual; missing trailing /
```

---

#### Unknown Override Keys

When the `overrides` block is present, only the three recognized keys (`branch_strategy`, `merge_strategy`, `epic_prefix`) are valid. Unknown keys:

- **MUST produce a validation warning** (not an error) during tooling validation
- **MUST be ignored** by the HQ agent during override resolution
- **MUST NOT** affect governance behavior

This forward-compatibility rule allows future versions of the spec to add new override fields without breaking existing configurations.

---

#### Precedence

Override resolution follows a three-level hierarchy:

| Level | Source | Authority | Example |
|-------|--------|-----------|---------|
| 1 (highest) | Local project convention | Documented in `docs/decisions/` | A decision document that explicitly overrides a governance convention for exceptional circumstances |
| 2 (medium) | `.ai-project.yml` overrides | Declared in the `overrides` block | `overrides.epic_prefix: feature/` |
| 3 (lowest) | Governance defaults | Defined in `PROJECT-SYSTEM-GUIDELINES.md` | Default `epic_prefix: epic/` |

**Resolution rule:** When a conflict exists, the highest-level source wins. If no override exists at a given level, the next level down applies.

For full precedence documentation and core non-overridable dimensions, see `PROJECT-SYSTEM-GUIDELINES.md` (Section: Override System).

For the formal enumeration of all overridable and non-overridable dimensions with rationale and boundary rules, see `governance/override-boundaries.md`.

---

### 3.4 Optional Fields — `models` (Hybrid Model Routing)

The `models` block is **optional**. When present, it configures the local/remote hybrid model selection for unattended 24/7 autonomous cluster execution.

| Field | Type | Default | Allowed Formats / Examples | Role |
|-------|------|---------|---------------------------|------|
| `hq` | String | `remote:gpt-4o` | `remote:gpt-4o`, `remote:claude-3-5-sonnet` | Product Owner (High-level vision & Requirements) |
| `phase` | String | `remote:claude-3-5-sonnet` | `remote:claude-3-5-sonnet` | Software Architect (Phase Milestone planning) |
| `milestone` | String | `remote:claude-3-5-sonnet` | `remote:claude-3-5-sonnet` | Software Architect (Milestone Epic planning) |
| `epic_dev` | String | `local:qwen2.5-coder:14b` | `local:qwen2.5-coder:14b`, `local:qwen2.5-coder` | Developer Agent (Code implementation; must be a tool-calling-capable model) |
| `epic_qa` | String | `local:qwen2.5-coder:7b` | `local:qwen2.5-coder:7b`, `local:llama3` | QA Tester Agent (Verification & Test runner) |

#### Format Constraints
Model configuration values must follow one of these formats:
- **Remote Models:** Prefix with `remote:` followed by the provider and model name (e.g., `remote:gpt-4o`, `remote:claude-3-5-sonnet`, `remote:gemini-1.5-pro`).
- **Local Models:** Prefix with `local:` followed by the model identifier (e.g., `local:qwen2.5-coder:14b`, `local:qwen2.5-coder:7b`). These are format examples only, not defaults; role defaults are defined in the table above.

---

### 3.5 Optional Fields — `visual_artifacts` (Visual Artifacts)

The `visual_artifacts` block is **optional** and **default-on**. When the block is **absent**, the
visual-artifacts capability is **enabled** at its documented defaults — `enabled: false` is the
explicit opt-out. This reflects visuals as the CFO's default lens on an increasingly autonomous
system (SN-17); it no longer mirrors the `cfo_review_gate` / `models` opt-in philosophy for the
`enabled` field specifically.

When present, the block declares whether visual artifacts are enabled, where the generative endpoint
(ComfyUI) lives, which artifact types are in scope, and whether visuals are required for specs.

| Field | Type | Default | Allowed Values | Constraint | Behavioral Effect |
|-------|------|---------|----------------|------------|-------------------|
| `enabled` | Boolean | `true` | `true`, `false` | Must be a YAML boolean when present | Master on/off switch. `true` (or block absent) ⇒ capability on; `false` ⇒ capability off (explicit opt-out). |
| `comfyui_url` | String | `http://localhost:8188` | Any well-formed `http`/`https` URL | Must be a well-formed URL (scheme + host) when present | Declares the ComfyUI generative endpoint. Endpoint availability is the CFO's responsibility; this field only declares where it is configured. |
| `types` | List of String | `[diagrams, infographics, video]` | Each entry one of: `diagrams`, `infographics`, `video` | Every entry must be an allowed value when present | Selects which artifact types are in scope. `diagrams`: Mermaid/PlantUML structural; `infographics`: ComfyUI-generated imagery; `video`: ComfyUI video (optional). |
| `visual_required_for_specs` | Boolean | `true` | `true`, `false` | Must be a YAML boolean when present | Enforcement setting: whether specs are required to carry a visual. Governs enforcement only, not which artifact types are automatic (see AOG §16.1/§16.2). |

#### Field Details

##### `visual_artifacts.enabled`

| Property | Value |
|----------|-------|
| Type | Boolean |
| Required | No |
| Default | `true` |
| Allowed Values | `true`, `false` |
| Constraint | Must be a YAML boolean when present. A non-boolean is a validation error. |
| Validation Error | `"Invalid visual_artifacts.enabled: '<value>'. Must be a boolean (true or false)."` |

##### `visual_artifacts.comfyui_url`

| Property | Value |
|----------|-------|
| Type | String |
| Required | No |
| Default | `http://localhost:8188` |
| Allowed Values | Any well-formed `http`/`https` URL |
| Constraint | When present, must be a well-formed URL (a parseable `http`/`https` scheme with a host). |
| Validation Error | `"Invalid visual_artifacts.comfyui_url: '<value>'. Must be a well-formed http(s) URL."` |

##### `visual_artifacts.types`

| Property | Value |
|----------|-------|
| Type | List of String |
| Required | No |
| Default | `[diagrams, infographics, video]` |
| Allowed Values | Each entry one of: `diagrams`, `infographics`, `video` |
| Constraint | When present, every entry must be an allowed value. An entry outside the set is a validation error. |
| Validation Error | `"Invalid visual_artifacts.types entry: '<value>'. Must be one of: diagrams, infographics, video."` |

##### `visual_artifacts.visual_required_for_specs`

| Property | Value |
|----------|-------|
| Type | Boolean |
| Required | No |
| Default | `true` |
| Allowed Values | `true`, `false` |
| Constraint | Must be a YAML boolean when present. A non-boolean is a validation error. |
| Validation Error | `"Invalid visual_artifacts.visual_required_for_specs: '<value>'. Must be a boolean (true or false)."` |

#### Unknown `visual_artifacts` Keys

When the `visual_artifacts` block is present, only the four recognized keys (`enabled`,
`comfyui_url`, `types`, `visual_required_for_specs`) are valid. Unknown keys:

- **MUST produce a validation warning** (not an error) during tooling validation
- **MUST be ignored** during capability resolution
- **MUST NOT** affect governance behavior

This forward-compatibility rule (mirroring the `overrides` and `models` blocks) allows future
versions of the spec to add new `visual_artifacts` fields without breaking existing configurations.

#### Worked Example

```yaml
visual_artifacts:
  enabled: true                          # default-on; false is the explicit opt-out
  comfyui_url: http://localhost:8188
  types:
    - diagrams                           # Mermaid/PlantUML structural
    - infographics                       # ComfyUI-generated imagery
    - video                              # ComfyUI video (optional)
  visual_required_for_specs: true        # enforcement setting; defaulted true
```

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

When the `overrides` block is present, the following additional validation rules apply:

9. The `overrides` block must be valid YAML (covered by rule 2)
10. Each recognized override field must contain an allowed value per its constraint (see Section 3.3):
    - `overrides.branch_strategy` must be one of: `trunk-based`, `gitflow`
    - `overrides.merge_strategy` must be one of: `merge`, `squash`, `rebase`
    - `overrides.epic_prefix` must end with `/` and must not be empty
11. Unknown keys in the `overrides` block MUST produce a validation warning (not an error)
12. Invalid values for known override fields MUST produce a validation error
13. At least one override value is NOT required — the block is fully optional

When the `models` block is present, the following additional validation rules apply:

14. The `models` block must be valid YAML (covered by rule 2)
15. Each recognized model routing field (`hq`, `phase`, `milestone`, `epic_dev`, `epic_qa`) must be a string matching `^(remote|local):[a-zA-Z0-9.:_-]+$`
16. Unknown keys in the `models` block MUST produce a validation warning
17. Invalid values or formats in the `models` block MUST produce a validation error

When the `visual_artifacts` block is present, the following additional validation rules apply:

18. The `visual_artifacts` block must be valid YAML (covered by rule 2)
19. `visual_artifacts.enabled`, when present, must be a boolean (`true`/`false`)
20. Each entry in `visual_artifacts.types`, when present, must be one of: `diagrams`, `infographics`, `video`
21. `visual_artifacts.comfyui_url`, when present, must be a well-formed URL (a parseable `http`/`https` scheme with a host)
22. Unknown keys in the `visual_artifacts` block MUST produce a validation warning (not an error)
23. Invalid values in the `visual_artifacts` block MUST produce a validation error
24. The entire `visual_artifacts` block is optional; an **absent** block is valid and means the capability is **enabled** at its documented defaults (no error, no warning)
25. `visual_artifacts.visual_required_for_specs`, when present, must be a boolean (`true`/`false`)

A `.ai-project.yml` file is **invalid** if any required field is absent, any constraint above is violated, any known override field contains an invalid value, any `visual_artifacts` value violates rules 19–21 or 25, or the file is not valid YAML.

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

## 11. Full Example with Visual Artifacts

```yaml
# .ai-project.yml
governance:
  source: https://github.com/panchew/ai-project-system
  version: "2.1.0"
  ref: v2.1.0

project:
  name: acme-payments
  description: "Payment processing service for ACME Corp"

visual_artifacts:
  enabled: true
  comfyui_url: http://localhost:8188
  types:
    - diagrams
    - infographics
  visual_required_for_specs: true
```

An equivalent project with the `visual_artifacts` block **omitted** has the capability **enabled**
at its documented defaults and remains valid. Setting `enabled: false` is the explicit opt-out.

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 2.3.0 | 2026-07-13 | `visual_artifacts` flipped from opt-in/off-by-default to default-on/opt-out: §3.5 `enabled` default `false` → `true`; added new `visual_required_for_specs` enforcement field (default `true`) with Field Details block and §4 validation rule 25; Worked Example and §11 Full Example updated. (Epic E27.1, P7-M27) |
| 2.2.0 | 2026-07-12 | `epic_dev` default moved from `local:llama3:8b` (verified unusable for tool-calling — empty tool-call responses, local-agent-runner CONTRACT §1.4) to `local:qwen2.5-coder:14b`, consistently in the schema comment (§3.4), the field table default/examples, and the format-constraint examples. `epic_qa` unchanged. (Epic E26.2, P7-M26) |
| 2.1.0 | 2026-06-28 | Added the optional, opt-in `visual_artifacts` block: Section 3.1 schema reference, new Section 3.5 (field definitions for `enabled`, `comfyui_url`, `types`, unknown-key forward-compatibility, worked example), validation rules 18–24 in Section 4, and a full example in Section 11. Absent block ⇒ capability disabled. (Epic E22.1, P5-M22) |
| 2.0.0 | 2026-05-21 | Complete override specification: Section 3.3 expanded from stub to full field definitions with types, defaults, allowed values, constraints, behavioral effects, and precedence hierarchy. Added override validation rules to Section 4. (Epic E9.1, P2-M9) |
| 1.0.0 | 2026-04-20 | Initial specification (Epic E6.3, P2-M6) |
