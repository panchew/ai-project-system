# Tool Integration Guides

The AI Project System governance framework is **tool-neutral**. The Governance Agent is a single
instructions file ([`governance/agents/governance.agent.md`](../../agents/governance.agent.md))
that any AI chat tool can load as context. These guides show how to deliver and open that agent in
each supported tool.

---

## The Neutral Convention

Regardless of tool, the Governance Agent is installed to one canonical, platform-independent path
in your project:

```
.ai-project/agents/governance.agent.md
```

This sits alongside the rest of the `.ai-project/` namespace (`artifacts/`, `logs/`, `queue/`). It
is the **single source of truth** for the agent definition in your project. Each tool then consumes
that file in its own way — see your tool's guide below.

Install it once (from a submodule consumer project):

```bash
mkdir -p .ai-project/agents
cp .governance/governance/agents/governance.agent.md .ai-project/agents/governance.agent.md
```

> **If your project IS the governance source** (e.g., `ai-project-system` itself), governance lives
> at `./governance` locally rather than as a submodule:
> `cp ./governance/agents/governance.agent.md .ai-project/agents/governance.agent.md`

---

## Pick Your Tool

| Tool | Guide | How it consumes the agent |
|------|-------|---------------------------|
| **Claude Code** | [claude-code.md](claude-code.md) | Project-memory import / `@`-mention |
| **Cursor** | [cursor.md](cursor.md) | Project Rule / `@Files` context |
| **Windsurf** | [windsurf.md](windsurf.md) | Workspace rule / `@`-mention in Cascade |
| **GitHub Copilot** | [github-copilot.md](github-copilot.md) | Agent-file auto-detection (`.github/agents/`) |

Each guide answers the same three questions, in the same order:

1. **Where the governance agent lives** — the neutral path (and, for Copilot, the `.github/agents/`
   copy it auto-detects).
2. **How this tool consumes it** — agent-file registration, custom instructions, or copy-paste.
3. **How to open a governance chat** — the concrete action that gets a governance session running.

All four tools are first-class peers. Copilot is one option among equals, not the default.

---

## After You Open the Agent

Whichever tool you use, once the Governance Agent is loaded you proceed identically: send the
canonical startup prompt (or paste a Chat Starter) to activate the mode you need — HQ, Phase,
Milestone, or Epic. See [ADOPTION-GUIDE.md → Step 4](../ADOPTION-GUIDE.md#step-4-send-canonical-startup-prompt).
