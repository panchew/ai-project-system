---
name: hq
version: 2.0.0
description: (superseded) Use governance.agent.md — unified agent with HQ/Phase/Milestone/Epic modes
type: custom-agent
scope: governance-execution
---

> **This agent has been superseded by `governance/agents/governance.agent.md`.**
>
> The single `governance.agent.md` replaces all separate agent files (HQ, Phase, Milestone, Epic)
> with one unified agent that self-configures its mode from the Chat Starter you deliver.
>
> To use the new agent:
>
> 1. Copy `governance/agents/governance.agent.md` to `.github/agents/governance.agent.md`
> 2. (Optional) Remove the old `hq.agent.md` from `.github/agents/`
> 3. Select the `hq` agent in your AI tool (the `name:` field is unchanged)
> 4. Paste a Phase, Milestone, or Epic Execution Chat Starter to activate the corresponding mode
>
> **Backward compatibility:** The `name: hq` front-matter is preserved so existing
> tool configurations continue to work after copying the new file.
