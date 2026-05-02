# HQ Startup Prompt — Canonical

Use this prompt with the "hq" custom agent after initializing a project with the AI Project System CLI.

## Canonical Prompt

```
I'm starting a new project using the AI Project System governance framework. 
Initialize HQ Chat for [project-name] and help me create a Phase 0 project formalization.
```

Replace `[project-name]` with your project name.

## Expected Behavior

- Activates HQ Chat in governance mode
- Reads `.ai-project.yml` for project configuration
- Loads governance rules from the `governance/` submodule
- Begins Phase 0 planning and produces initial formalization notes

## How To Use in VS Code

1. Open your project in VS Code.
2. Open GitHub Copilot Chat.
3. Select the "hq" custom agent.
4. Paste the Canonical Prompt and send.

## References

- Governance: governance/PROJECT-SYSTEM-GUIDELINES.md
- AI Operating: governance/AI-OPERATING-GUIDELINES.md
- CLI Usage: docs/systems/cli-usage-guide.md
