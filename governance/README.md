# AI Project System — Governance

This folder contains all governance files for the AI Project System.

**Governance files are portable.** External projects may reference this folder as a git submodule to adopt the AI Project System governance without copying files manually.

---

## What Is In This Folder

| Item | Purpose |
|---|---|
| `PROJECT-SYSTEM-GUIDELINES.md` | Authoritative project structure and execution rules |
| `AI-OPERATING-GUIDELINES.md` | Authoritative AI agent behavior rules |
| `EPIC-EXECUTION-CHAT-STARTER.md` | Canonical Epic Execution Chat Starter format reference |
| `agents/` | AI agent definition files (VS Code Copilot custom agents) |
| `diagrams/` | Visual documentation of the governance system |
| `guides/` | Onboarding and FAQ for human adopters |
| `systems/` | Operational system reference documents |
| `templates/` | Fillable templates for all governance artifact types |

---

## Authority Hierarchy

When documents conflict, higher levels win:

1. `PROJECT-SYSTEM-GUIDELINES.md` — highest authority
2. `AI-OPERATING-GUIDELINES.md`
3. `EPIC-EXECUTION-CHAT-STARTER.md`
4. `systems/` — operational guidance
5. `templates/`, `guides/`, `diagrams/` — no authority (structure and information only)

---

## How to Adopt This Governance (Git Submodule)

To reference this governance folder from an external project:

```sh
# Add as a submodule
git submodule add https://github.com/panchew/ai-project-system.git governance

# Pin to a specific governance version
cd governance && git checkout v2.0.0
```

Then create a `governance-source.md` at your project root declaring the adoption (use `governance/templates/governance-source.md` as the template).

See `guides/QUICK-START.md` for the full onboarding walkthrough.

---

## Governance Version

This governance folder is versioned at `v2.0.0` as of Milestone M6 (the migration that created this folder).
