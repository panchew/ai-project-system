# Governance Agent in GitHub Copilot

How to deliver and open the AI Project System Governance Agent in
[GitHub Copilot](https://github.com/features/copilot) (VS Code).

> Prerequisite: you have run `ai-project init` and the governance submodule is present at
> `.governance/`. See [ADOPTION-GUIDE.md](../ADOPTION-GUIDE.md) Steps 1–2.

---

## 1. Where the governance agent lives

The neutral, canonical path in your project is the same as for every other tool:

```
.ai-project/agents/governance.agent.md
```

**Copilot additionally auto-detects agent files in `.github/agents/`.** So for Copilot you keep a
second copy at that tool-specific path:

```
.github/agents/governance.agent.md
```

Install both — the neutral source of truth, then the Copilot auto-detection copy:

```bash
# Neutral canonical path
mkdir -p .ai-project/agents
cp .governance/governance/agents/governance.agent.md .ai-project/agents/governance.agent.md

# Copilot auto-detection path
mkdir -p .github/agents
cp .ai-project/agents/governance.agent.md .github/agents/governance.agent.md
# Remove any old separate agent file if present
rm -f .github/agents/hq.agent.md
```

(If your project IS the governance source, copy from `./governance/agents/governance.agent.md`.)

> The `ai-project init` CLI writes the neutral `.ai-project/agents/governance.agent.md` copy for
> you; the Copilot auto-detection copy above is a manual step you (or your tooling) maintain
> separately.

## 2. How GitHub Copilot consumes it

VS Code + GitHub Copilot detects `.github/agents/*.agent.md` automatically — no further
registration is needed. The single Governance Agent file (front-matter `name: hq`) handles all four
modes (HQ, Phase, Milestone, Epic).

## 3. How to open a governance chat

1. Open your project in VS Code with GitHub Copilot enabled.
2. Open the agent selector: `Ctrl+Shift+P` → **"GitHub Copilot: Select Agent"** → choose **"hq"**.
3. Paste the canonical startup prompt or a Chat Starter to activate the mode you need. See
   [ADOPTION-GUIDE.md → Step 4](../ADOPTION-GUIDE.md#step-4-send-canonical-startup-prompt).

The agent self-configures to the correct mode based on the Chat Starter you paste.

---

## Troubleshooting

- **Agent not appearing in the selector:** ensure `.github/agents/governance.agent.md` exists with
  valid YAML front-matter and is committed (`git status` should show it tracked). Re-copy it with
  the install commands above. See also
  [ADOPTION-FAQ → Governance Agent Not Appearing](../ADOPTION-FAQ.md#3-governance-agent-not-appearing).
- **Old `hq.agent.md` still present:** remove it — `rm -f .github/agents/hq.agent.md`. It has been
  replaced by the unified `governance.agent.md`.
- **Agent has no governance context:** confirm the submodule is initialized
  (`git submodule update --init --recursive`) so `.governance/` is populated.

**Verify:** with the "hq" agent selected, send the startup prompt — it should confirm it loaded the
governance files from `.governance/` and propose next steps.
