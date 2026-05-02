# AI Project System — CLI Usage Guide

This guide explains how to initialize a new project with the AI Project System CLI and verify readiness for HQ Chat planning.

## Installation

No separate installation is required when using this repository locally. Run the CLI directly:

```bash
./bin/ai-project-init <project-name> [options]
```

To make it globally accessible (optional):

```bash
chmod +x bin/ai-project-init
sudo ln -sf "$(pwd)/bin/ai-project-init" /usr/local/bin/ai-project-init
```

## Usage

```bash
ai-project init <project-name> [options]
```

- `--dir <path>`: Output directory parent (project folder will be created inside).
- `--governance-source <url>`: Governance repo URL (default: https://github.com/panchew/ai-project-system).
- `--governance-version <ref>`: Tag/branch (default: v2.0.0).
- `--skip-git`: Do not initialize a git repository.
- `--skip-submodule`: Skip adding governance as a submodule (offline/testing only).

## What You Get

- Standard docs structure and `.ai-project.yml` with governance metadata
- Governance as a Git submodule at `governance/`
- HQ Chat agent installed at `.github/agents/hq.agent.md` (stubbed if governance agent not present)
- Clean initial git commit

## Quick Start

```bash
./bin/ai-project-init my-project --dir /tmp
cd /tmp/my-project
code .
```

Then open GitHub Copilot Chat, pick the "hq" custom agent, and use the canonical prompt from the HQ Startup Prompt guide.

## End-to-End Verification Checklist

```bash
# Repo scaffold
ls -la

# Verify governance submodule
git submodule status
ls governance/

# Verify agent file
cat .github/agents/hq.agent.md | sed -n '1,40p'

# Validate YAML
cat .ai-project.yml

# Git state
git status
git log --oneline -n 1
```

## Troubleshooting

- Governance submodule fails to add:
  - Ensure network access to GitHub and correct `--governance-version`.
  - CLI falls back to clone+adopt; check `.gitmodules` for `submodule.governance.branch`.
- Agent file missing or empty:
  - Re-run "Install HQ Agent" step manually:
    ```bash
    mkdir -p .github/agents
    if [[ -f governance/agents/hq.agent.md ]]; then
      cp governance/agents/hq.agent.md .github/agents/hq.agent.md
    else
      printf "# HQ Chat Agent\n\nThis agent is under development in Milestone M8.\n" > .github/agents/hq.agent.md
    fi
    ```
- `git status` shows changes after init:
  - The CLI amends the initial commit to include the HQ agent file. If it failed (rare), you may see a second commit; this is acceptable.

## Related Documents

- Governance: governance/PROJECT-SYSTEM-GUIDELINES.md
- AI Operating: governance/AI-OPERATING-GUIDELINES.md
- HQ Startup Prompt: docs/systems/hq-startup-prompt.md
