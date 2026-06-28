# Governance Agent in Cursor

How to deliver and open the AI Project System Governance Agent in
[Cursor](https://cursor.com).

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

## 2. How Cursor consumes it

Cursor loads project context two ways; either works.

- **Project Rule (persistent).** Add a rule that pulls in the agent file for every chat in the
  workspace. Create `.cursor/rules/governance.mdc`:

  ```markdown
  ---
  description: AI Project System Governance Agent
  alwaysApply: true
  ---

  Operate as the AI Project System Governance Agent. The full agent definition is in
  @.ai-project/agents/governance.agent.md — follow it and the governance documents in
  `.governance/` as authoritative.
  ```

  The `@`-reference attaches the agent file as context whenever the rule applies.

- **Per-session attachment.** Skip the rule and attach the file directly in Chat: type `@Files` and
  select `.ai-project/agents/governance.agent.md` so its full contents are in context for that
  conversation.

## 3. How to open a governance chat

1. Open Cursor Chat (the chat/composer panel).
2. Ensure the agent is in context — the Project Rule applies automatically, or attach the file with
   `@Files` as above.
3. Paste the canonical startup prompt or a Chat Starter to activate the mode you need (HQ, Phase,
   Milestone, or Epic). See
   [ADOPTION-GUIDE.md → Step 4](../ADOPTION-GUIDE.md#step-4-send-canonical-startup-prompt).

The agent self-configures to the correct mode based on the Chat Starter you paste.

---

**Verify:** ask the chat "what governance mode are you in?" — it should answer with the mode implied
by your prompt and confirm it can read the governance files under `.governance/`.
