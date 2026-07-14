# .ai-project Queue System

This directory acts as the asynchronous, file-driven message bus for the unattended 24/7 autonomous development cluster.

## Execution Sequence

1. **Phase Planning (`02_phase.json`):** HQ mode writes this file to trigger Phase planning (Milestones planning within a Phase).
2. **Milestone Planning (`03_milestone.json`):** Phase mode writes this file to trigger Milestone planning (Epics planning within a Milestone).
3. **Epic Execution (`04_epic.json`):** Milestone mode writes this file to trigger Epic execution.

The orchestrator CLI daemon monitors this directory, locks execution via `.ai-project/locks/execution.lock`, spins up containerized Docker sandboxes, and handles the Dev-QA recursion loop.

## Live Epic Execution Trigger (`04_epic.json`)

In the live flow, `dev_command` is the real-model adapter `./bin/run-dev-agent` (also the
orchestrator's default when the field is omitted), and `validation_command` is the project's
real test/lint gate. Success is decided by the QA `validation_command` exit code — never by
the dev agent's own output.

```json
{
  "epic_id": "P7-M26-E26.3",
  "epic_spec_path": "docs/phases/.../P7-M26-E26.3__spec__....md",
  "sandbox_env": "alpine:latest",
  "dev_command": "./bin/run-dev-agent",
  "validation_command": "python3 -m pytest -q",
  "run_dev_initially": true
}
```

Model routing comes from `.ai-project.yml` `models:` (`epic_dev` / `epic_qa`), exported to the
sandbox as `AI_PROJECT_ACTIVE_MODEL`.

> **Note:** `tests/mocks/mock_{dev,qa}.sh` and `bin/verify-loop.sh` are a **verification-only
> regression harness** for the loop logic (P3-M12-E12.3). They are never part of the live flow
> and must not appear in a live trigger's `dev_command`/`validation_command`.
