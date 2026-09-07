<!-- QA context: standard = /home/panchew/soft-dev/ai-project-system/.ai-project/artifacts/measurement-tasks/P12-M41/qa-task/standard/TASK-QA-1__standard__servicecard-spec.md § Validation Rules -->
## STANDARD

## Validation Rules


1. The file is valid YAML and its top level is a mapping.
2. `name` is present and is a lowercase string matching `^[a-z][a-z0-9-]*$`.
3. `owner` is present and is a string containing exactly one `@`.
4. `tier` is present and is one of exactly `gold`, `silver`, `bronze`.
5. `replicas` is present and is an integer greater than or equal to `1`.
6. `port` is present and is an integer in the range `1024`–`65535` inclusive.
7. `healthcheck` is present and is a mapping with both a `path` key and a `timeout_s` key.
8. `healthcheck.path` starts with `/`.
9. `healthcheck.timeout_s` is an integer between `1` and `30` inclusive.
10. `dependencies`, when present, is a list of strings, each matching the same pattern as
    `name` in rule 2.
11. `region` is present and is one of exactly `us-east`, `us-west`, `eu-central`.
12. Every top-level key is one of: `name`, `owner`, `tier`, `replicas`, `port`,
    `healthcheck`, `dependencies`, `region`. Any other top-level key is a violation.

## WORK

Read these files with the read_file tool and assess them against the standard above:

- /home/panchew/soft-dev/ai-project-system/.ai-project/artifacts/measurement-tasks/P12-M41/qa-task/work/servicecard.yml
