# Governance Agent in Claude Code

How to deliver and open the AI Project System Governance Agent in
[Claude Code](https://claude.com/claude-code).

> Prerequisite: you have run `ai-project init` and the governance submodule is present at
> `.governance/`. See [ADOPTION-GUIDE.md](../ADOPTION-GUIDE.md) Steps 1–2.

---

## 1. Where the governance agent lives

The neutral, canonical path in your project:

```
.ai-project/agents/governance.agent.md
```

Install it from the submodule:

```bash
mkdir -p .ai-project/agents
cp .governance/governance/agents/governance.agent.md .ai-project/agents/governance.agent.md
```

(If your project IS the governance source, copy from `./governance/agents/governance.agent.md`.)

## 2. How Claude Code consumes it

Claude Code loads project context from `CLAUDE.md` (project memory) automatically, and it supports
file imports with the `@path` syntax. Make the agent definition part of every session by adding one
import line to your project's `CLAUDE.md`:

```markdown
# Project memory

@.ai-project/agents/governance.agent.md
```

If `CLAUDE.md` does not exist yet, create it at the repository root with the line above. From then
on, every `claude` session in this project loads the full Governance Agent definition as context.

> **Per-session alternative:** if you would rather not edit `CLAUDE.md`, you can pull the agent in
> for a single session by typing `@.ai-project/agents/governance.agent.md` in the Claude Code
> prompt before pasting your Chat Starter.

## 3. How to open a governance chat

1. Start Claude Code in the project root:
   ```bash
   claude
   ```
2. The Governance Agent definition is already in context (via the `CLAUDE.md` import, or your
   `@`-mention).
3. Paste the canonical startup prompt or a Chat Starter to activate the mode you need (HQ, Phase,
   Milestone, or Epic). See
   [ADOPTION-GUIDE.md → Step 4](../ADOPTION-GUIDE.md#step-4-send-canonical-startup-prompt).

The agent self-configures to the correct mode based on the Chat Starter you paste.

---

**Verify:** ask the session "what governance mode are you in?" — it should answer with the mode
implied by your prompt and confirm it loaded the governance files from `.governance/`.
