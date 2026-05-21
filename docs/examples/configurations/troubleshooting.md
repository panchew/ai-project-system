---
title: Troubleshooting Common Override Issues
type: example
phase: P2
milestone: M9
epic: E9.4
status: active
last_updated: 2026-05-21
---

# Troubleshooting — Common Override Issues

This guide covers the most common issues when configuring `.ai-project.yml` overrides, with symptoms, causes, solutions, and prevention tips.

---

## 1. Override Not Taking Effect

**Symptom:** The HQ agent generates branch names using `epic/` even though `epic_prefix: feature/` is set. Merge instructions use `merge` even though `merge_strategy: squash` is set.

**Cause (a):** `.ai-project.yml` is not being read by the HQ agent. This happens when the file is missing, at the wrong path, or the agent is running with a cached/stale configuration.

**Solution:**
1. Verify `.ai-project.yml` exists at the repository root: `ls .ai-project.yml`
2. Confirm the agent process was restarted after editing the file
3. Run the agent with verbose logging to confirm file loading

**Prevention:**
- Treat `.ai-project.yml` as a configuration file that requires agent restart
- Add a startup log line in the agent that confirms the loaded config path

**Cause (b):** The `overrides` block is absent. If there's no `overrides:` key in `.ai-project.yml`, all governance defaults apply.

**Solution:**
```yaml
# Add the overrides block:
overrides:
  merge_strategy: squash
  epic_prefix: feature/
```

**Prevention:**
- Always include the `overrides` block (even if empty) when you intend to customize
- Use the application example as a reference template

**Cause (c):** The field name is incorrect. For example, `merge-strategy:` (hyphen) instead of `merge_strategy:` (underscore), or `epic_prefix:` misspelled as `epic-prefix:`.

**Solution:**
```yaml
# Correct field names:
overrides:
  branch_strategy: gitflow      # underscore, not hyphen
  merge_strategy: rebase        # underscore, not hyphen
  epic_prefix: feature/         # underscore, not hyphen
```

**Prevention:**
- Copy-paste override field names from `ai-project-yml-spec.md` §3.3
- YAML keys are case-sensitive and underscore-sensitive

---

## 2. Validation Error on Startup

**Symptom:** The HQ agent (or CLI) reports a validation error and refuses to proceed. Error messages like:
```
Invalid merge_strategy: 'Squash'. Must be one of: merge, squash, rebase.
Invalid branch_strategy: 'git-flow'. Must be one of: trunk-based, gitflow.
```

**Cause:** An override field contains a value that is not in its allowed set. Common mistakes include wrong case (`Squash` vs `squash`), wrong delimiter (`git-flow` vs `gitflow`), or a value that doesn't exist.

**Solution:** Correct the value to match exactly one of the allowed values:

| Field | Allowed Values |
|-------|---------------|
| `branch_strategy` | `trunk-based`, `gitflow` |
| `merge_strategy` | `merge`, `squash`, `rebase` |

```yaml
# Correct:
merge_strategy: squash          # lowercase
branch_strategy: gitflow        # no hyphen, all lowercase

# Incorrect:
merge_strategy: Squash          # uppercase
branch_strategy: git-flow       # hyphen instead of underscore
```

**Prevention:**
- Refer to `ai-project-yml-spec.md` §3.3 for exact allowed values
- All values are case-sensitive — always use lowercase
- Use the application or monorepo example as a template

---

## 3. Wrong Branch Prefix in Generated Artifacts

**Symptom:** Generated specs and chat starters reference `epic/E9.4` even though `epic_prefix: feature/` is configured. The prefix appears correct in `.ai-project.yml` but artifacts use the default.

**Cause:** The override was applied after artifacts were already generated. The HQ agent uses the prefix at generation time. If the prefix changes mid-epic, previously generated artifacts retain the old prefix.

**Solution:**
1. Update existing artifacts to use the new prefix (manual or regenerate)
2. Future artifacts will use the correct prefix

**Prevention:**
- Set the `epic_prefix` before generating any Epic artifacts
- If changing the prefix mid-project, audit and update all existing specs and chat starters
- Consider the prefix a project-level constant, not a per-epic setting

---

## 4. Merge Strategy Mismatch

**Symptom:** PR descriptions say "Merge using merge" but the team expects squash merges. Or the merge button in GitHub/GitLab defaults to merge commit even though `merge_strategy: squash` is set.

**Cause (a):** The override is set correctly but the repository's GitHub/GitLab settings use a different default merge method. The override is advisory to the HQ agent for generated documentation; it does not control repository-level merge settings.

**Solution:**
1. Update the repository's merge settings in GitHub/GitLab to match
2. The override ensures documentation consistency, but platform settings control the actual merge

**Prevention:**
- Configure both `.ai-project.yml` and repository platform settings to use the same strategy
- Document the expected merge strategy in the project's contributing guide

**Cause (b):** A local project decision document (`docs/decisions/`) overrides the `.ai-project.yml` setting per the precedence hierarchy.

**Solution:**
1. Check `docs/decisions/` for any decision documents that specify a merge strategy
2. Either update the decision document to match, or accept the higher-precedence decision

**Prevention:**
- Understand the precedence hierarchy: local decisions > `.ai-project.yml` overrides > governance defaults
- Search `docs/decisions/` before adding a new override

---

## 5. Precedence Confusion

**Symptom:** An override appears to have no effect, but `branch_strategy: gitflow` is correctly set in `.ai-project.yml`. Another team member says the project uses trunk-based development.

**Cause:** A local project decision document (`docs/decisions/`) has set `branch_strategy: trunk-based` at a higher precedence level than `.ai-project.yml`. Per the precedence hierarchy (Section 3.3 of the spec):

| Level | Source | Authority |
|-------|--------|-----------|
| 1 (highest) | Local project convention (`docs/decisions/`) | Highest |
| 2 | `.ai-project.yml` overrides | Medium |
| 3 (lowest) | Governance defaults | Lowest |

**Solution:**
1. Search for decision documents: `grep -r "branch_strategy" docs/decisions/`
2. If a decision document exists, either update it or remove it if no longer needed
3. If no decision document exists, check if `.ai-project.yml` was edited after agent startup

**Prevention:**
- Always check `docs/decisions/` for overrides before modifying `.ai-project.yml`
- Document any override-related decisions clearly in `docs/decisions/`
- Understand that `.ai-project.yml` overrides are level 2, not level 1

---

## 6. YAML Formatting Issues

**Symptom:** The agent reports a YAML parse error on startup. Error messages like:
```
YAML parse error: mapping values are not allowed here
YAML parse error: did not find expected key
```

**Cause:** Common YAML formatting mistakes:

| Mistake | Incorrect | Correct |
|---------|-----------|---------|
| Missing space after colon | `source:./governance` | `source: ./governance` |
| Wrong indentation | `  source: ./governance\n  version: "2.0.0"\n    ref: v2.0.0` | Consistent 2-space indentation |
| Unquoted colon in description | `description: "My project: great"` (correct) vs `description: My project: great` (invalid) | Quote descriptions containing `:` |
| Tab instead of spaces | Uses tab character | Use spaces (2 per indent level) |
| Trailing whitespace | `merge_strategy: squash ` | `merge_strategy: squash` |
| Missing `governance:` or `project:` key | `source: ...` at top level | Nested under `governance:` |

**Solution:**
1. Validate the file with `python3 -c "import yaml; yaml.safe_load(open('.ai-project.yml'))"`
2. Check indentation — YAML requires consistent spacing (2 spaces per level)
3. Ensure all colons have a space after them (except in quoted strings)
4. Quote any values that contain `:` or `#` characters

**Prevention:**
- Use a YAML linter in your editor
- Copy-paste from validated examples rather than typing YAML from scratch
- Always quote `project.description` and `governance.version` values
- Use 2-space indentation consistently (never tabs)

---

## 7. Unknown Override Keys Producing Warnings

**Symptom:** Validation passes but a warning is logged:
```
Warning: Unknown override key 'custom_field' in .ai-project.yml overrides block. This key will be ignored.
```

**Cause:** The `overrides` block contains a key that is not one of the three recognized fields (`branch_strategy`, `merge_strategy`, `epic_prefix`). Per spec §3.3, unknown keys produce a warning but not an error.

**Solution:**
1. Check if the key is a typo of a recognized field (e.g., `branch-strategy` instead of `branch_strategy`)
2. If intentional (future override), the warning is harmless — the key is ignored
3. If unintentional, remove the unknown key

**Prevention:**
- Only use the three recognized override keys
- Refer to `ai-project-yml-spec.md` §3.3 for the complete list
- Use the provided examples as templates

---

## 8. Version Not Quoted

**Symptom:** The `governance.version` field is parsed as a float by YAML, changing `2.0.0` to `2.0` and breaking semver validation.

**Cause:** YAML parses unquoted `2.0.0` as a floating-point number, truncating it to `2.0`. The spec requires a quoted string.

**Solution:**
```yaml
# Incorrect:
version: 2.0.0    # YAML parses as float 2.0

# Correct:
version: "2.0.0"  # YAML parses as string "2.0.0"
```

**Prevention:**
- Always quote `governance.version` values
- Always quote `project.description` values
- When in doubt, quote string values
