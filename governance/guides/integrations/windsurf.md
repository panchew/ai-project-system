# Governance Agent in Windsurf

How to deliver and open the AI Project System Governance Agent in
[Windsurf](https://windsurf.com).

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

## 2. How Windsurf consumes it

Windsurf's assistant (Cascade) loads project context two ways; either works.

- **Workspace rule (persistent).** Add a rule that points Cascade at the agent file for every
  conversation in the workspace. Create `.windsurf/rules/governance.md`:

  ```markdown
  ---
  trigger: always_on
  ---

  Operate as the AI Project System Governance Agent defined in
  `.ai-project/agents/governance.agent.md`. Treat that file and the governance documents under
  `.governance/` as authoritative. Read them before acting.
  ```

- **Per-session mention.** Skip the rule and pull the file in directly: in Cascade, `@`-mention
  `.ai-project/agents/governance.agent.md` so its full contents are in context for that
  conversation.

## 3. How to open a governance chat

1. Open Cascade (the Windsurf chat panel).
2. Ensure the agent is in context — the workspace rule applies automatically, or `@`-mention the
   agent file as above.
3. Paste the canonical startup prompt or a Chat Starter to activate the mode you need (HQ, Phase,
   Milestone, or Epic). See
   [ADOPTION-GUIDE.md → Step 4](../ADOPTION-GUIDE.md#step-4-send-canonical-startup-prompt).

The agent self-configures to the correct mode based on the Chat Starter you paste.

---

**Verify:** ask Cascade "what governance mode are you in?" — it should answer with the mode implied
by your prompt and confirm it can read the governance files under `.governance/`.
