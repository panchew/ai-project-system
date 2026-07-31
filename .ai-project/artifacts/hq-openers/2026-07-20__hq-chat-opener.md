---
artifact_type: hq_opener
artifact_version: 1.0
timestamp: 2026-07-20T22:00:00Z
issued_by: Creation Chat
project_name: ai-project-system
repo: https://github.com/panchew/ai-project-system
governance_version: PROJECT-SYSTEM-GUIDELINES.md v2.3.0
operating_version: AI-OPERATING-GUIDELINES.md v2.10.0
framework_version: v7.0.0
active_phase: none (P9 closed at v7.0.0 — P10 direction set by SN-23, not yet scoped)
instantiation: p10-scoping-open
supersedes: .ai-project/artifacts/hq-openers/2026-07-17__hq-chat-opener.md
provenance: >
  Authored by the Creation Chat to instantiate the HQ Chat for P10 scoping.
  To be filed verbatim by the HQ Chat session it instantiates, for the artifact record.
---

# HQ Chat Opener — Project Control Room

## Project Context
Project: ai-project-system
Repository: https://github.com/panchew/ai-project-system (local: ~/soft-dev/ai-project-system)
Primary Language / Stack (if known): Markdown governance corpus + Python tooling (bin/: daemon, orchestrator, init, version, visual, run-dev-agent, measure-token-burn) + Python test suite (363 passing at v7.0.0)

## Governance
- PROJECT-SYSTEM-GUIDELINES.md version: v2.3.0
- AI-OPERATING-GUIDELINES.md version: v2.10.0

## Current State
Phase: none active — P9 fully closed at v7.0.0 (merge 8044451, tag v7.0.0, master 97ed5a3, suite 363/0); P10 not yet scoped
Milestone: none
Active Epics: none

## Objectives
- Per Steering Note SN-23 (2026-07-20): P10 is fleet ADOPTION of v7.0.0 — get the CFO's real projects actually running under governance, not more framework capability
- Fixed operating posture across all projects: Manual/Paid from Creation through Milestone; Agentic/Local at the Epic. The agentic/manual × local/paid matrix is resolved into a posture, not a per-project menu
- Proving pair first: home_finance + local-agent-runner (the only two with canonical governance.agent.md installed) — version-bump to v7.0.0 and run the first real Agentic/Local epic there
- One serialized local-inference lane operated by System Chat; near-24/7 utilization, never two reasoning jobs at once; hand-run the lane first, build a scheduler only when real contention bites
- Run-first ordering: measurement and validation come OUT of real epic runs, not before them (resolves the 2026-07-20 Progress Digest Decision 2)
- Overarching: progress happens in every governed project, not just this one

## Constraints
- Technical constraints: local-inference substrate is the real open risk gating adoption. The framework is ready; the local stack is not proven in the wild. local-agent-runner is built on Ollama; a reference stack (Qwen3.6 27B Q8_0 on llama.cpp) recommends against Ollama. The runtime fork is settled by the first real epic, not decided in the abstract
- Organizational constraints: solo CFO, one machine; fleet of 10 projects in ~/soft-dev, 8 enrolled but enrollment is shallow — no project except the framework is confirmably on v7.0.0. ai-project-system-mcp carries the SUPERSEDED hq.agent.md (P6-GH-15 live in the wild)
- Explicit non-goals for P10: no new framework capability built on spec; no third spin-off; competing-model code review, P9-GH-1, and ComfyUI are PARKED (enter scope only as adoption friction surfaces them); the external-sidekick idea is a Brief-level identity question and is NOT P10 scope

## Operating Rules
- HQ Chat is declarative only
- Coding Agents execute Epics
- Epic Execution Chat Starters are mandatory
- Documentation is authoritative

## Immediate Next Actions
1. Acknowledge Steering Note SN-23 (P10 adoption spine) — `.ai-project/artifacts/steering-notes/2026-07-20__creation-chat__steering-note__P10-adoption-spine.md`
2. Record the 2026-07-20 Progress Digest's open decisions as resolved by SN-23: P10 spine set (Dec. 1), run-first ordering chosen for token measurement (Dec. 2), P9-GH-1 parked not-in-spine (Dec. 3), ComfyUI parked (Dec. 4)
3. Open the P10 scoping session with SN-23's adoption spine; shape a first milestone around the proving pair (home_finance + local-agent-runner): v7.0.0 bump + first real Agentic/Local epic + settle the Ollama-vs-llama.cpp runtime question from that run
4. Roadmap the dormant enrolled projects (courtis, fieldledger-assesment, Getawayinsured2023, ai-project-system-mcp) to roll under v7.0.0 by end of phase; include the ai-project-system-mcp superseded-agent fix (P6-GH-15)
5. Triage carry-forwards into scope or explicit defer: P9-GH-1 (merge-auth hole at Milestone→Phase / Phase→HQ), P9-GH-2 (measure-token-burn can't verify its own reduction claims), P9-GH-3 (within-session segmentation), P8-GH-2, competing-model code review, ComfyUI
6. Advance the SN-21 System-participant canonization: System Chat as fleet operator (runs the lane, keeps projects current) with NO authority to act fleet-wide on a spoken word, plus its daily re-instantiation seed
