<!-- QA context: standard = governance/ai-project-yml-spec.md § 4. Validation Rules -->
## STANDARD

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

A `.ai-project.yml` file is **invalid** if any required field is absent, any constraint above is violated, any known override field contains an invalid value, any `visual_artifacts` value violates rules 19–21 or 25, `framework_version` is present and violates rule 26, or the file is not valid YAML.

> **Unknown keys outside `overrides`, `models` and `visual_artifacts` are not covered by any rule
> above, and that gap is open.** Rules 11, 16 and 22 mandate a warning for unknown keys inside those
> three blocks. **There is no rule for unknown keys at the top level or inside `governance:` and
> `project:`** — so error, warn and ignore are all equally unsupported by this document. Three such
> keys exist in live configs today (`created_at`, `submodule_path`, `cfo_review_gate`); the first two
> are written by `bin/ai-project-init`. The reference implementation
> (`bin/ai-project-validate`) **warns** and reports those findings with **no rule number**, so its
> treatment is never mistaken for enforcement of this section. Closing the gap — and deciding whether
> those three fields warrant schema entries of their own — is escalated, not settled here.

---

## WORK

Read these files with the read_file tool and assess them against the standard above:

- .ai-project.yml
