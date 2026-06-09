# .ai-project Queue System

This directory acts as the asynchronous, file-driven message bus for the unattended 24/7 autonomous development cluster.

## Execution Sequence

1. **Phase Planning (`02_phase.json`):** HQ mode writes this file to trigger Phase planning (Milestones planning within a Phase).
2. **Milestone Planning (`03_milestone.json`):** Phase mode writes this file to trigger Milestone planning (Epics planning within a Milestone).
3. **Epic Execution (`04_epic.json`):** Milestone mode writes this file to trigger Epic execution.

The orchestrator CLI daemon monitors this directory, locks execution via `.ai-project/locks/execution.lock`, spins up containerized Docker sandboxes, and handles the Dev-QA recursion loop.
