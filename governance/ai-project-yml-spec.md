# `.ai-project.yml` Specification

**Version:** 2.9.0  
**Status:** Active  
**Effective Date:** 2026-08-11  
**Introduced In:** Epic E6.3 (P2-M6); override specification completed in Epic E9.1 (P2-M9); `visual_artifacts` block added in Epic E22.1 (P5-M22); `epic_dev` default moved to a tool-calling-capable model in Epic E26.2 (P7-M26); `visual_artifacts` flipped to default-on and `visual_required_for_specs` enforcement key added in Epic E27.1 (P7-M27); `types` naming-collision resolved in Epic E29.1 (P8-M29); `models` defaults refreshed to the measurement-grounded mapping in Epic E30.2 (P9-M30); `models.creation` and `models.epic_manual` keys added (manual-chat-only, no agentic dispatch surface) in Epic E31.3 (P9-M31); the five paid-frontier `models` defaults refreshed `claude-opus-4-8` → `claude-opus-5` by HQ Ruling (`.ai-project/artifacts/escalation-notices/2026-07-28T20_00_00Z__P10-M34__escalation_notice.md`); the two agentic epic-lane `models` defaults moved `qwen2.5-coder:14b` → `qwen3-coder:30b` on M33 run evidence in Epic E34.3 (P10-M34); optional top-level `framework_version` given a schema entry and §4 rule 3's field count corrected in Epic E38.3 (P11-M38); the top-level opt-out gate keys `cfo_review_gate` and `rework_exhaustion_flip` blessed with schema entries (§3.7/§3.8) and §4 rules 27/28 in Epic E43.4 (P12-M43)

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

framework_version: <string>  # OPTIONAL. Framework version this project has ADOPTED,
                             # as distinct from governance.version (what it PINS).
                             # Accepts a bare or v-prefixed semver. Full spec: §3.6.

cfo_review_gate: <enabled|disabled>   # OPTIONAL. CFO PR review gate. Absent ⇒ enabled.
                                      # `disabled` is the explicit opt-out. Full spec: §3.7.

rework_exhaustion_flip: <enabled|disabled>  # OPTIONAL. Rework-exhaustion flip to manual.
                                            # Absent ⇒ enabled. `disabled` is the explicit
                                            # opt-out. Full spec: §3.8.

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

models:                  # OPTIONAL. Hybrid model routing maps for autonomous clusters
                         # (hq/phase/milestone/epic_dev/epic_qa) plus manual-chat-only
                         # verification targets (creation/epic_manual, no dispatch surface).
  hq: <string>           # default: remote:claude-opus-5
  phase: <string>        # default: remote:claude-opus-5
  milestone: <string>    # default: remote:claude-opus-5
  epic_dev: <string>     # default: local:qwen3-coder:30b
  epic_qa: <string>      # default: local:qwen3-coder:30b
  creation: <string>     # default: remote:claude-opus-5. Manual-chat-only (E31.3).
  epic_manual: <string>  # default: remote:claude-opus-5. Manual-chat-only (E31.3).

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

The `models` block is **optional**. When present, it configures two related things: the
local/remote hybrid model selection for unattended 24/7 autonomous cluster execution
(`hq`, `phase`, `milestone`, `epic_dev`, `epic_qa`), and, since Epic E31.3 (P9-M31), the
expected-model verification targets for **manually**-run chats at every level
(`creation`, `epic_manual` are manual-only additions; `hq`/`phase`/`milestone` double as
both — they were already the agentic-dispatch keys and are also the manual-verification
targets those three levels check against, since a Phase/Milestone/HQ instance may run
manually or (for Phase/Milestone) agentically).

| Field | Type | Default | Allowed Formats / Examples | Role |
|-------|------|---------|---------------------------|------|
| `hq` | String | `remote:claude-opus-5` | `remote:claude-opus-5`, `remote:claude-sonnet-5` | Product Owner (High-level vision & Requirements); manual-chat verification target for HQ |
| `phase` | String | `remote:claude-opus-5` | `remote:claude-opus-5` | Software Architect (Phase Milestone planning); manual-chat verification target for Phase |
| `milestone` | String | `remote:claude-opus-5` | `remote:claude-opus-5` | Software Architect (Milestone Epic planning); manual-chat verification target for Milestone |
| `epic_dev` | String | `local:qwen3-coder:30b` | `local:qwen3-coder:30b`, `local:qwen2.5-coder` | Developer Agent (Code implementation; must be a tool-calling-capable model **and large enough to actually use the tools** — see the sizing note below). Agentic dispatch lane only — not a manual-chat verification target. |
| `epic_qa` | String | `local:qwen3-coder:30b` | `local:qwen3-coder:30b`, `local:llama3` | QA Tester Agent (Verification & Test runner). Agentic dispatch lane only — not a manual-chat verification target. |
| `creation` | String | `remote:claude-opus-5` | `remote:claude-opus-5` | Manual-chat verification target for Creation Chat only — Creation never dispatches agentically (SN-22), so this key has no dispatch role. |
| `epic_manual` | String | `remote:claude-opus-5` | `remote:claude-opus-5` | Manual-chat verification target for a human-driven Epic chat — distinct from `epic_dev`/`epic_qa`, which serve the agentic Dev/QA dispatch lanes only. |

> **Defaults provenance (v2.4.0, Epic E30.2 / P9-M30):** these defaults are the
> measurement-grounded mapping derived in the governance source repository from
> its captured token-burn dataset — the prior defaults (`remote:gpt-4o`,
> `remote:claude-3-5-sonnet`, `local:qwen2.5-coder:7b` for `epic_qa`) never
> appeared in a single measured session and were replaced as unevidenced. See
> the source repo's `.ai-project/artifacts/reference/token-measurement/`
> (model-routing-policy.md + audit-report.md) for the derivation. Adopting
> repositories may override any value per their own evidence.

> **`creation`/`epic_manual` provenance (v2.5.0, Epic E31.3 / P9-M31):** these two keys
> exist solely so every manually-startable chat level has a configured verification
> target (`governance/systems/chat-hierarchy.md` "Manual Chat Model Verification") — they
> are consumed from `model-routing-policy.md`'s existing policy rows (P1 for `creation`,
> P5 for `epic_manual`), not new policy judgments. Absent block or absent key is a
> documented permissive default (chat proceeds, states no expectation is configured), not
> a validation error and not a refusal — see chat-hierarchy.md for the reasoning.

> **Agentic-lane sizing note (v2.7.0, Epic E34.3 / P10-M34):** `epic_dev`/`epic_qa`
> moved `local:qwen2.5-coder:14b` → `local:qwen3-coder:30b` because the 14b was
> falsified by a real run, not by argument — it returned **exit 0 having changed zero
> files** on a real epic (0 tool rounds, markdown-plan mode), while the same Ollama
> runtime at 30b did mergeable work on that epic and completed a second one. **A
> tool-calling-*capable* model is not automatically a tool-calling-*willing* one at
> small parameter counts**; adopters sizing a local lane should treat "the model
> emitted a plan instead of calling tools" as the failure mode to test for, and should
> never accept a green exit code as proof of work. Trade recorded honestly: at Q4_K_M
> the 30b is 18.6 GB and will **partially offload to system RAM** on a 16 GB-VRAM box
> (measured 12.9 GB VRAM / 21.4 GB total, ~9.4 tok/s vs the 14b's 12.2) — slower, but
> it finishes. Adopting repositories with different hardware may override per their own
> evidence; the governance source repo's derivation is in
> `.ai-project/artifacts/reference/token-measurement/model-routing-policy.md` rows
> P6/P7.

#### Format Constraints
Model configuration values must follow one of these formats:
- **Remote Models:** Prefix with `remote:` followed by the provider and model name (e.g., `remote:claude-opus-5`, `remote:claude-sonnet-5`, `remote:gemini-1.5-pro`).
- **Local Models:** Prefix with `local:` followed by the model identifier (e.g., `local:qwen3-coder:30b`, `local:qwen2.5-coder:7b`). These are format examples only, not defaults; role defaults are defined in the table above.

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
| `types` | List of String | `[diagrams, infographics, video]` | Each entry one of: `diagrams`, `infographics`, `video` | Every entry must be an allowed value when present | Selects which **generative** (ComfyUI) artifact types are in scope — see note below. `diagrams`: ComfyUI-generated diagram-style imagery (txt2img); `infographics`: ComfyUI-generated imagery; `video`: ComfyUI video (optional). |
| `visual_required_for_specs` | Boolean | `true` | `true`, `false` | Must be a YAML boolean when present | Enforcement setting: whether specs are required to carry a visual. Governs enforcement only, not which artifact types are automatic (see AOG §17.1/§17.2). |

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

> **All `types` entries — including `diagrams` — are Generative (ComfyUI) categories.** This
> field has no Structural entry and needs no Structural entry: AOG §17.3's Structural mode
> (Mermaid/PlantUML diagrams written as text by the agent) calls no endpoint, uses no
> `bin/ai-project-visual` invocation, and is available regardless of this block's presence,
> contents, or the `enabled` flag. `types: diagrams` selects ComfyUI-generated diagram-*style*
> imagery (a txt2img call), not Mermaid/PlantUML output. See
> `.ai-project/artifacts/reference/comfyui-endpoint/VISUAL-ARTIFACTS.md` for the full
> Structural/Generative split.

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
    - diagrams                           # ComfyUI-generated diagram-style imagery (txt2img)
    - infographics                       # ComfyUI-generated imagery
    - video                              # ComfyUI video (optional)
  visual_required_for_specs: true        # enforcement setting; defaulted true
  # Structural diagrams (Mermaid/PlantUML, agent-authored text) call no ComfyUI endpoint
  # and need no `types` entry — see AOG §16.3.
```

---

### 3.6 Optional Fields — `framework_version` (Adoption Stamp)

The `framework_version` field is **optional** and lives at the **top level**, not inside `governance:`.

| Property | Value |
|----------|-------|
| Type | String |
| Required | No |
| Default | None — an absent field is valid and carries no implied value |
| Format | Semantic version, bare or `v`-prefixed (`7.1.0`, `v7.1.0`) |
| Constraint | When present, must be a non-empty string matching `^v?\d+\.\d+\.\d+$` |
| Validation Error | `"Invalid framework_version: '<value>'. Must be a non-empty string matching ^v?\d+\.\d+\.\d+$."` |

Declares the framework version this project has **adopted** — the released version whose roll-forward
procedure the project has actually been through.

**It is not a duplicate of `governance.version`, even though it usually agrees with it.** The two
fields answer different questions:

| Field | Question it answers |
|-------|---------------------|
| `governance.version` | Which governance version does this project **pin**? |
| `framework_version` | Which framework version has this project **adopted**? |

A project can pin a version it has not yet adopted (the submodule moves before the roll-forward
completes) or carry an adoption stamp against a pin that has since changed. **When they disagree,
that disagreement is the signal** — it is precisely the drift this field exists to make visible.

> **Measured, and recorded honestly (2026-08-11, Epic E38.3):** across every config on the reference
> machine that carried the field — **7 of 13 enrolled projects** — `framework_version` and
> `governance.version` named the **same version, 7 times out of 7**. The field is therefore
> *currently* redundant in practice. It is defined here anyway because the redundancy is a property
> of a fleet that was stamped and pinned in the same operation, not a property of the field's
> meaning. Tooling **must not** infer one from the other.

**Why optional.** At 2026-08-11, **6 of 13** enrolled projects on the reference machine carried no
stamp at all. Making the field required would have declared six otherwise-valid configs invalid on a
rule that did not exist the day before, which is a fleet-wide reconciliation, not a schema entry.

**Why the `v` prefix is accepted.** Every stamp in existence when this entry was written was
`v`-prefixed (`v7.0.0` ×6, `v7.1.0` ×1), because the value records a released **tag name**. Requiring
a bare semver — the form `governance.version` requires under rule 5 — would have invalidated all
seven. The spec records the convention that exists rather than legislating a new one.

**Valid examples:**
```yaml
framework_version: v7.1.0    # the released tag adopted (fleet convention)
framework_version: 7.1.0     # bare semver, also accepted
```

**Invalid:**
```yaml
framework_version: latest    # non-pinned refs are not allowed
framework_version: v7        # not a full MAJOR.MINOR.PATCH
framework_version: ""        # must be non-empty when present
```

**Self-referential repositories.** The governance source itself (§8) pins `governance.version` to its
own released version, so for that one repository the two fields would record the same fact **by
construction** rather than by coincidence. The governance source is therefore **not expected** to
carry `framework_version`, and its absence there is a documented exemption rather than missing data.

---

### 3.7 Optional Fields — `cfo_review_gate` (CFO PR Review Gate)

The `cfo_review_gate` field is **optional** and lives at the **top level**. When **absent**, the
gate is **enabled** at its default; `disabled` is the explicit opt-out. This is the original
opt-out governance-gate precedent: **on by default, disabled deliberately.**

| Property | Value |
|----------|-------|
| Type | String |
| Required | No |
| Default | `enabled` |
| Allowed Values | `enabled`, `disabled` |
| Constraint | When present, must be one of: `enabled`, `disabled` |
| Validation Error | `"Invalid cfo_review_gate: '<value>'. Must be one of: enabled, disabled."` |

Declares whether the CFO PR review gate is active: `enabled` means merge-ready PRs surface in the
Progress Digest's Open Decisions section for CFO diff review before merge; `disabled` means merges
proceed automatically (agentic auto-merge) with no gate. The behavioural definition is
`governance/systems/creation-chat-guide.md` "CFO PR Review Gate"; this entry is the **schema
blessing** — the key was in live configs and reported as an unblessed top-level key before it was
blessed (Epic E43.4, P12-M43; finding W1 of the M43 milestone spec).

**Valid examples:**
```yaml
cfo_review_gate: enabled     # gate on (the default)
cfo_review_gate: disabled    # explicit opt-out; merges proceed automatically
```

**Invalid:**
```yaml
cfo_review_gate: true        # not the enabled/disabled vocabulary
cfo_review_gate: maybe       # not an allowed value
```

---

### 3.8 Optional Fields — `rework_exhaustion_flip` (Rework-Exhaustion Flip to Manual)

The `rework_exhaustion_flip` field is **optional** and lives at the **top level**. When **absent**,
the flip is **enabled** at its default; `disabled` is the explicit opt-out. It follows the
`cfo_review_gate` pattern (**on by default, disabled deliberately**) and installs the system's
**first fail-closed default**: exhausted rework flips the receiving parent to manual Execution Mode.

| Property | Value |
|----------|-------|
| Type | String |
| Required | No |
| Default | `enabled` |
| Allowed Values | `enabled`, `disabled` |
| Constraint | When present, must be one of: `enabled`, `disabled` |
| Validation Error | `"Invalid rework_exhaustion_flip: '<value>'. Must be one of: enabled, disabled."` |

Declares whether the rework-exhaustion flip is active: `enabled` means that when a parent chat's
rework limit is exhausted — the 3-attempt maximum plus any written `+1`, without an acceptable
delivery (`PROJECT-SYSTEM-GUIDELINES.md` §11.6 "The Rework Limit") — the **receiving parent flips
to manual** Execution Mode, performed and recorded by **Drivr** so the committed starter stays the
source of truth (`governance/systems/chat-hierarchy.md` "The rework-exhaustion flip"). `disabled`
means exhausted rework leaves Execution Mode unchanged.

**Why this key is blessed (W1, M43 milestone spec):** the precedent it copies — `cfo_review_gate` —
was itself an **unblessed** key that `bin/ai-project-validate` warned on. Copying the pattern
verbatim without blessing the result would ship the system's first fail-closed default as a key
nothing validates. E43.4 blesses **both** keys in one change: the new flip key here (§3.8 + §4
rule 28) and the precedent it copies (§3.7 + §4 rule 27), so the whole top-level opt-out surface is
validated rather than half-warned.

**Valid examples:**
```yaml
rework_exhaustion_flip: enabled     # flip on (the default)
rework_exhaustion_flip: disabled    # explicit opt-out; exhausted rework leaves mode unchanged
```

**Invalid:**
```yaml
rework_exhaustion_flip: true        # not the enabled/disabled vocabulary
rework_exhaustion_flip: 1           # not an allowed value
```

---

## 4. Validation Rules

A `.ai-project.yml` file is **valid** when all of the following are true:

1. The file exists at the repository root as `.ai-project.yml`
2. The file is valid YAML (parseable without errors)
3. All five required fields are present: `governance.source`, `governance.version`, `governance.ref`, `project.name`, `project.description`
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
15. Each recognized model routing field (`hq`, `phase`, `milestone`, `epic_dev`, `epic_qa`, `creation`, `epic_manual`) must be a string matching `^(remote|local):[a-zA-Z0-9.:_-]+$`
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

When the top-level `framework_version` field is present, the following additional validation rule applies:

26. `framework_version`, when present, must be a non-empty string matching `^v?\d+\.\d+\.\d+$` (see Section 3.6). The field is **optional**: an absent `framework_version` is valid and is not a warning.

When the top-level `cfo_review_gate` field is present, the following additional validation rule applies:

27. `cfo_review_gate`, when present, must be one of: `enabled`, `disabled` (see Section 3.7). The field is **optional**: an absent `cfo_review_gate` is valid and means the gate is enabled at its default; `disabled` is the explicit opt-out.

When the top-level `rework_exhaustion_flip` field is present, the following additional validation rule applies:

28. `rework_exhaustion_flip`, when present, must be one of: `enabled`, `disabled` (see Section 3.8). The field is **optional**: an absent `rework_exhaustion_flip` is valid and means the flip is enabled at its default; `disabled` is the explicit opt-out.

A `.ai-project.yml` file is **invalid** if any required field is absent, any constraint above is violated, any known override field contains an invalid value, any `visual_artifacts` value violates rules 19–21 or 25, `framework_version` is present and violates rule 26, `cfo_review_gate` is present and violates rule 27, `rework_exhaustion_flip` is present and violates rule 28, or the file is not valid YAML.

> **Unknown keys outside `overrides`, `models` and `visual_artifacts` are not covered by any rule
> above, and that gap is narrower but still open.** Rules 11, 16 and 22 mandate a warning for unknown
> keys inside those three blocks. **There is no rule for unknown keys at the top level or inside
> `governance:` and `project:`** — so error, warn and ignore are all equally unsupported by this
> document. Two such keys exist in live configs today (`created_at`, `submodule_path`), both written
> by `bin/ai-project-init`. **`cfo_review_gate` was a third member until Epic E43.4 (P12-M43)
> blessed it — together with the new `rework_exhaustion_flip` key it now carries §3.7/§3.8 schema
> entries and §4 rules 27/28**, so the opt-out precedent and the system's first fail-closed default
> are no longer in the schema-drift class (finding W1 of the M43 milestone spec). The reference
> implementation (`bin/ai-project-validate`) **warns** and reports remaining unknown keys with **no
> rule number**, so its treatment is never mistaken for enforcement of this section. Closing the gap
> for the remaining two fields — and deciding whether they warrant schema entries of their own — is
> escalated, not settled here.

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
| 2.9.0 | 2026-09-02 | **The top-level opt-out gate keys blessed — `cfo_review_gate` and the new `rework_exhaustion_flip` (E43.4, P12-M43; closes finding W1 of the M43 milestone spec).** **(a) New §3.8 + §4 rule 28** blesses `rework_exhaustion_flip` — the system's **first fail-closed default** — on the `cfo_review_gate` pattern: optional top-level key, **on by default, disabled deliberately**, values `enabled`/`disabled`, absent-key-valid-and-means-enabled. The behaviour it names (exhausted rework — the 3-attempt maximum plus any written `+1`, without an acceptable delivery — flips the **receiving parent** to manual, **performed and recorded by Drivr** so the committed starter stays the source of truth) is normative in PROJECT-SYSTEM-GUIDELINES.md §11.6 "The Rework Limit" and `governance/systems/chat-hierarchy.md`; this entry is the schema blessing. **(b) `cfo_review_gate` blessed in the same change — §3.7 + §4 rule 27.** W1's defect is that the precedent itself was unvalidated (`bin/ai-project-validate` warned on it); blessing the successor while leaving the precedent warned would leave a standing validator warning on this repo's own config, so both keys are blessed together and the whole top-level opt-out surface is validated rather than half-warned. **(c)** §3.1 schema block and the §4 closing gap note updated: `cfo_review_gate` leaves the three-member schema-drift class, leaving `created_at`/`submodule_path` (both `bin/ai-project-init`-written) as the escalated remainder. No existing field, default, or validation rule changed. |
| 2.8.0 | 2026-08-11 | **`framework_version` given a schema entry (`P10-GH-1`), and §4 rule 3's field count corrected.** **(a) New §3.6** defines the optional top-level `framework_version` — the version a project has **adopted**, as against `governance.version`, which is what it **pins** — with a §3.1 schema-block entry and **new §4 rule 26** (non-empty string matching `^v?\d+\.\d+\.\d+$` when present). It is **optional** and the `v` prefix is **accepted**, both deliberately: measured on the reference machine on **2026-08-11** across **13 enrolled projects**, **6 carried no stamp** and **all 7 that did were `v`-prefixed** (`v7.0.0` ×6, `v7.1.0` ×1), so requiring the field, or requiring the bare semver form rule 5 imposes on `governance.version`, would have invalidated six or seven live configs respectively — a fleet-wide reconciliation rather than a schema entry. Recorded honestly in §3.6: in all **7 of 7** configs carrying both, the two fields named the **same version**, so the field is *currently* redundant in practice; it is defined anyway because that is a property of a fleet stamped and pinned in one operation, not of the field's meaning, and tooling **must not** infer either field from the other. **(b) §4 rule 3 read *"All four required fields"* while listing five** — from v1.0.0 (2026-04-20) until this row. §3.1 marks five REQUIRED and §3.2 documents five, so **five is right and the word was wrong**; the count is now **five**. **This correction is standalone, not a consequence of (a):** `framework_version` is optional and therefore never belonged in rule 3's list, so blessing it moved the count from a wrong four to a right five rather than to six. **(c) §4 gains a closing note recording an open gap it does not close:** rules 11, 16 and 22 mandate a warning for unknown keys inside `overrides`, `models` and `visual_artifacts`, and **no rule of this section covers unknown keys at the top level or inside `governance:` / `project:`**. Three such keys are live today — `created_at`, `submodule_path` (both written by `bin/ai-project-init`) and `cfo_review_gate` — and **none of the three is blessed here**; the reference implementation warns and reports them with no rule number, and the gap is escalated. **No existing rule was renumbered, no existing field changed, and no default moved.** New reference implementation: `bin/ai-project-validate` (`P10-GH-5`, first enforcement of this section since it was written), with `tests/test_ai_project_validate.py`. Derivation: `docs/phases/P11__Drivr_Coordination_Over_Rented_Execution/P11-M38-E38.3__delivery-notice.md` (Epic E38.3, P11-M38). |
| 2.7.0 | 2026-07-28 | The two **agentic epic-lane** `models` defaults — `epic_dev` and `epic_qa` — moved `local:qwen2.5-coder:14b` → `local:qwen3-coder:30b`, applying the runtime choice P10-M33 settled by running it (**keep Ollama, raise the model tier**). Unlike 2.6.0 this is a **policy-row change, not a mapping refresh**: `model-routing-policy.md`'s rows **P6/P7 name the model in their own Decision column**, so the file's **Change discipline** is engaged and is satisfied with new cited evidence — E33.2 **Run A** (the 14b: exit 0, 0 tool rounds, 0 files changed on a real epic), **Run B** (same epic, same Ollama runtime, 30b: mergeable work), and **E33.4** (a second real epic, `home_finance`, complete and green). P7 moves on its **existing** gap-grounded interim reasoning with the referent updated — **G11 (zero captured QA-role runs) remains open** and no QA-lane evidence is claimed. Loadability envelope recorded: Q4_K_M/18.6 GB exceeds a 16 GB-VRAM box and partially offloads to RAM (12.9 GB VRAM / 21.4 GB total, ~9.4 tok/s vs 12.2) — slower, but it finishes. Updated §3.1 schema comments, §3.4 field table defaults/examples + new agentic-lane sizing note, and format-constraint examples. The five paid-frontier keys are **untouched** (different surface, different gate). No field, key, or validation rule changed — value/documentation refresh only. Derivation: `docs/phases/P10__Fleet_Adoption_and_Local_Inference_Proving/P10-M33-E33.2__runtime-decision.md` + `.ai-project/artifacts/agentic-runs/P10-M33-E33.2/run-record.md` + `.../P10-M33-E33.4/run-record.md` (Epic E34.3, P10-M34). |
| 2.6.0 | 2026-07-28 | The five paid-frontier `models` defaults — `hq`, `phase`, `milestone`, `creation`, `epic_manual` — refreshed `remote:claude-opus-4-8` → `remote:claude-opus-5` after `claude-opus-4-8` stopped being offered in the harness surface in use, halting every manual governance chat under the P9-M31-E31.3 verification guardrail (`.ai-project/artifacts/escalation-notices/2026-07-28T20_00_00Z__P10-M34__escalation_notice.md`). A **same-tier version refresh**, not a policy change: `model-routing-policy.md`'s rows P1–P4 decide *"Paid frontier"* and `claude-opus-5` is paid frontier, so the M30 evidence process was not re-run — see that file's new **Mapping revisit trigger — model unavailability**. Updated §3.1 schema comments, §3.4 field table defaults/examples, and format-constraint examples. `epic_dev`/`epic_qa` unchanged (agentic lanes, different surface). No field, key, or validation rule changed — value/documentation refresh only. Derivation: `.ai-project/artifacts/rulings/2026-07-28__ai-project-system-hq__ruling__paid-frontier-model-mapping-refresh.md` (HQ Chat, ai-project-system). |
| 2.5.0 | 2026-07-19 | Added two new **manual-chat-only** `models` keys, `creation` and `epic_manual` (default `remote:claude-opus-4-8` for both) — neither has an agentic dispatch surface; both exist solely as verification targets for the manual-mode startup guardrail (Hard Constraint, P9-M31-E31.3). Updated §3.1 schema comments, §3.4 field table + new provenance note, and §4 validation rule 15's recognized-field list. No existing key's default, format, or validation behavior changed. Derivation: governance source repo `governance/systems/chat-hierarchy.md` "Manual Chat Model Verification" (Epic E31.3, P9-M31), consuming `.ai-project/artifacts/reference/token-measurement/model-routing-policy.md` policy rows P1 and P5 without editing them. |
| 2.4.0 | 2026-07-17 | `models` defaults refreshed to the measurement-grounded mapping (Hard Constraint, P9-M30): `hq`/`phase`/`milestone` moved from `remote:gpt-4o` / `remote:claude-3-5-sonnet` (never observed in the 72-session token-burn dataset — falsified defaults) to `remote:claude-opus-4-8` (the measured workhorse at those levels); `epic_qa` moved from the never-measured `local:qwen2.5-coder:7b` to `local:qwen2.5-coder:14b` (the only local model with captured run evidence; gap G11). Updated consistently in the §3.1 schema comments, §3.4 field table defaults/examples + new provenance note, and format-constraint examples. `epic_dev` unchanged. No field, key, or validation rule changed — value/documentation refresh only. Derivation: governance source repo `.ai-project/artifacts/reference/token-measurement/` (Epic E30.2, P9-M30) |
| 2.3.1 | 2026-07-15 | Resolved the `visual_artifacts.types` naming collision with AOG §17.3 (P7-GH-21): §3.5 field table, Field Details (`types`, new clarifying note), and Worked Example no longer describe `diagrams` as "Mermaid/PlantUML structural" — all `types` entries, including `diagrams`, are now documented as Generative (ComfyUI) categories; Structural mode (AOG §17.3) is clarified as needing no `visual_artifacts` config at all. No field, default, or validation rule changed — documentation/reframing only. (Epic E29.1, P8-M29) |
| 2.3.0 | 2026-07-13 | `visual_artifacts` flipped from opt-in/off-by-default to default-on/opt-out: §3.5 `enabled` default `false` → `true`; added new `visual_required_for_specs` enforcement field (default `true`) with Field Details block and §4 validation rule 25; Worked Example and §11 Full Example updated. (Epic E27.1, P7-M27) |
| 2.2.0 | 2026-07-12 | `epic_dev` default moved from `local:llama3:8b` (verified unusable for tool-calling — empty tool-call responses, local-agent-runner CONTRACT §1.4) to `local:qwen2.5-coder:14b`, consistently in the schema comment (§3.4), the field table default/examples, and the format-constraint examples. `epic_qa` unchanged. (Epic E26.2, P7-M26) |
| 2.1.0 | 2026-06-28 | Added the optional, opt-in `visual_artifacts` block: Section 3.1 schema reference, new Section 3.5 (field definitions for `enabled`, `comfyui_url`, `types`, unknown-key forward-compatibility, worked example), validation rules 18–24 in Section 4, and a full example in Section 11. Absent block ⇒ capability disabled. (Epic E22.1, P5-M22) |
| 2.0.0 | 2026-05-21 | Complete override specification: Section 3.3 expanded from stub to full field definitions with types, defaults, allowed values, constraints, behavioral effects, and precedence hierarchy. Added override validation rules to Section 4. (Epic E9.1, P2-M9) |
| 1.0.0 | 2026-04-20 | Initial specification (Epic E6.3, P2-M6) |
