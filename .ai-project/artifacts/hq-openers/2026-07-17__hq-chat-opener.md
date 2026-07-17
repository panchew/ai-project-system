---
artifact_type: hq_opener
artifact_version: 1.0
timestamp: 2026-07-17T22:30:00Z
issued_by: Creation Chat
project_name: ai-project-system
repo: https://github.com/panchew/ai-project-system
governance_version: PROJECT-SYSTEM-GUIDELINES.md v2.3.0
operating_version: AI-OPERATING-GUIDELINES.md v2.9.0
framework_version: v6.0.1
active_phase: none (P8 closed at v6.0.1 — P9 direction set by SN-22, not yet scoped)
instantiation: p9-scoping-open
supersedes: .ai-project/artifacts/hq-openers/2026-07-14__hq-chat-opener.md
provenance: >
  Filed by the HQ Chat session it instantiated (2026-07-17), verbatim as received,
  for the artifact record. Content authored by the Creation Chat.
---

# HQ Chat Opener — Project Control Room

## Project Context
Project: ai-project-system
Repository: https://github.com/panchew/ai-project-system (local: ~/soft-dev/ai-project-system)
Primary Language / Stack (if known): Markdown governance corpus + Python tooling (bin/: daemon, orchestrator, init, version, visual, run-dev-agent) + Python test suite (307 passing at v6.0.1)

## Governance
- PROJECT-SYSTEM-GUIDELINES.md version: v2.3.0
- AI-OPERATING-GUIDELINES.md version: v2.9.0

## Current State
Phase: none active — P8 fully closed at v6.0.1 (merge c45b8a9, tag v6.0.1); P9 not yet scoped
Milestone: none
Active Epics: none

## Objectives
- Per Steering Note SN-22 (2026-07-17): context handling / token efficiency is the P9 spine — make token use as smart and effective as possible
- Measurement-first model-tier audit (frontier/paid vs local), so policies are realistic
- Dual manual/agentic mode for Phase, Milestone, and Epic Chats; Creation Chat and HQ Chat remain manual at all times
- Manual-mode startup guardrail: verify model-per-level against .ai-project.yml; refuse to proceed on mismatch
- Overarching: get the CFO's system up and running so every governed project makes progress

## Constraints
- Technical constraints: premium/frontier token quota is limited — the Epics-only-local assumption already failed in practice; agentic mode must itself decide paid vs local
- Organizational constraints: solo CFO across 8 governed projects on one machine
- Explicit non-goals: ComfyUI visual-artifact work is relevant but NOT a blocker and NOT the P9 spine; 'mighty' governing System Chat is pinned vision, not scope (SN-21 executor System HQ stands as written)

## Operating Rules
- HQ Chat is declarative only
- Coding Agents execute Epics
- Epic Execution Chat Starters are mandatory
- Documentation is authoritative

## Immediate Next Actions
1. Acknowledge Steering Notes SN-21 (System HQ adoption) and SN-22 (P9 direction) — both committed at 71f0ea5
2. Record the Progress Digest revision: ComfyUI demoted from likely-P9-spine to non-blocking track
3. Open the P9 scoping session with SN-22's spine and three workstreams as candidate scope
4. Triage carry-forwards P8-GH-1/2/3 and SN-21 canonization (incl. the daily System Chat re-instantiation seed) into P9 or standalone epics
