---
project: ai-project-system
phase: P2
milestone: M10
epic: E10.2
type: adoption-record
status: completed
last_updated: 2026-05-21
---

# Adoption Record — ai-project-system

## 1. Project Identification

| Field | Value |
|-------|-------|
| **Project name** | ai-project-system |
| **Repository URL** | https://github.com/panchew/ai-project-system |
| **Adoption date** | 2026-05-21 |
| **Adopter name/role** | Coding Agent / Epic Executor |
| **Governance version** | v2.0.0 |

## 2. Prerequisites Status

| Prerequisite | Status | Notes |
|---|---|---|
| Git (v2.30+) | ✅ | v2.43.0 |
| GitHub account | ✅ | panchew/ai-project-system accessible |
| VS Code (1.85+) | ✅ | v1.120.0 |
| GitHub Copilot extension | ⚠️ | Installed but agent file not deployed to `.github/agents/` |
| Node.js (v18+) | ❌ | v16.14.0 — below minimum v18+ required by guide |
| `ai-project` CLI installed | ❌ | Not globally installed; `npx @panchew/ai-project` fallback available |

## 3. Step Completion Log

| # | Step | Start Time | End Time | Duration | Outcome | Deviations? |
|---|---|---|---|---|---|---|
| 1 | Prerequisites Verification | 10:00 | 10:03 | 3 min | ⚠️ | Node.js v16 (below v18); CLI not installed |
| 2 | Step 1: `ai-project init` | 10:03 | 10:05 | 2 min | ⚠️ | Skipped — source repo would create recursive self-reference; must use `source: ./governance` manually |
| 3 | Step 2: Verify Governance | 10:05 | 10:08 | 3 min | ⚠️ | No submodule; governance at `./governance` locally; guide assumes submodule pattern |
| 4 | Step 3: Configure HQ Agent | 10:08 | 10:10 | 2 min | ⚠️ | Agent file exists at `governance/agents/hq.agent.md` but not at `.github/agents/hq.agent.md`; must be copied |
| 5 | Step 4: Canonical Startup Prompt | 10:10 | 10:12 | 2 min | ⚠️ | Cannot send prompt from Coding Agent context; human with HQ agent needed |
| 6 | Step 5: Create Phase 0 Spec | 10:12 | 10:13 | 1 min | ✅ | Phase 0 already exists (`P0__phase__project-formalization.md`) |
| 7 | Step 6: Plan First Milestone | 10:13 | 10:15 | 2 min | ✅ | Milestones exist (M0.1, M1, etc. across phases) |

**Total time to completion:** 15 minutes (simulated — for a fresh project, estimated 25–30 min)

## 4. Friction Points

| # | Category | Description | Step Occurred | Root Cause | Workaround | Recommended Fix |
|---|---|---|---|---|---|---|
| 1 | Environment | Node.js v16 installed; guide requires v18+ | Prerequisites | Environment has older Node.js LTS | Use `nvm` to switch to Node.js v18+; or proceed with v16 for non-CLI steps | Add Node.js version troubleshooting to FAQ; recommend `nvm` as installation method |
| 2 | Tooling | `ai-project` CLI not installed globally | Step 1 | Package not installed | Use `npx @panchew/ai-project` as fallback | Add `npx` fallback to the guide's main instructions, not just troubleshooting |
| 3 | Governance | Source repo references `./governance` locally, not via submodule | Step 2 | The adoption guide assumes submodule pattern, but the governance source repo uses local path | Manually verify files exist at `./governance/` | Add a note that source/governance repos use a different pattern (local reference) than adopting projects |
| 4 | Tooling | `.github/agents/hq.agent.md` does not exist in project | Step 3 | Agent file is in governance repo but not deployed to `.github/agents/` | `mkdir -p .github/agents && cp governance/agents/hq.agent.md .github/agents/hq.agent.md` | Add explicit "deploy agent file" step to the guide; note the source repo needs manual deployment |
| 5 | Documentation | Guide Step 4 assumes human interaction with HQ Chat; no guidance for CI/automated contexts | Step 4 | Guide written for human adopter; Coding Agent executing the guide cannot send startup prompt | Simulate or document the expected HQ response | Add note about automation context: Coding Agents should document expected HQ behavior, not execute prompts |
| 6 | Documentation | No milestone file at expected path `P2-M10__milestone.md` | Reference | Milestone spec was never created as standalone file; M10 criteria documented in phase spec | Reference M10 criteria from `P2__phase.md` instead | Ensure all milestones have standalone milestone spec files |
| 7 | Process | Source repo `ai-project init` would create recursive governance reference | Step 1 | Governance source repo IS the governance; init would reference itself | Skip `ai-project init` for the source repository | Add explicit guidance: "For the governance source repository, do not run `ai-project init` — governance is built in" |

## 5. Guide Deviations

| Step | Expected (per guide) | Actual | Reason | Impact |
|---|---|---|---|---|
| Step 1 | `ai-project init my-project` scaffolds new project | Skipped — source repo cannot init itself | Source repository contains governance; init would create circular reference | Neutral — source repo is a special case |
| Step 2 | Verify `.governance/` submodule | Verified `governance/` local directory instead | Source repo uses `source: ./governance`, not submodule | Neutral — both patterns are valid per governance spec |
| Step 3 | Verify `.github/agents/hq.agent.md` exists | File found at `governance/agents/hq.agent.md` instead | Source repo stores agents in governance package, not deployed to project | Negative — agent must be manually deployed to `.github/agents/` |
| Step 5 | Create Phase 0 spec via HQ Chat | Phase 0 already exists | Project is mature; Phase 0 was created during earlier phases | Neutral — adoption verified that Phase 0 exists and is correct |
| Step 6 | Plan first milestone | Milestones already exist across multiple phases | Project is fully adopted with existing execution history | Neutral — expected for the governance source repo |

## 6. Improvement Suggestions

| # | Area | Suggestion | Priority |
|---|---|---|---|
| 1 | ADOPTION-GUIDE.md — Prerequisites | Add `npx @panchew/ai-project` as primary option alongside global install | High |
| 2 | ADOPTION-GUIDE.md — Prerequisites | Add Node.js version management recommendation (`nvm`) | Medium |
| 3 | ADOPTION-GUIDE.md — Step 1 | Add special case note for governance source repository | Medium |
| 4 | ADOPTION-GUIDE.md — Step 3 | Add explicit "deploy agent file from governance" step | High |
| 5 | ADOPTION-GUIDE.md — Step 2 | Clarify that source repos use `source: ./governance` not submodule | Medium |
| 6 | ADOPTION-FAQ.md | Add FAQ entry: "Node.js version below v18" | Medium |
| 7 | ADOPTION-FAQ.md | Add FAQ entry: "Governance source repository adoption" | Low |
| 8 | ADOPTION-GUIDE.md | Add "automation context" note for Coding Agent-led adoption | Low |

## 7. Final Status

**Status:** Partial

**Reason:** The governance source repository (`ai-project-system`) is a special case that deviates from the standard adoption path in several ways. Core governance structure is verified and correct, but the project lacks a deployed HQ agent file at `.github/agents/hq.agent.md`, has older Node.js (v16), and the `ai-project init` step is inapplicable. Key friction points identified will improve the guide for external projects.

**Time to completion:** 15 minutes (simulated; target: 25–30 minutes)

---

*Adoption record created using [ADOPTION-RECORD-TEMPLATE.md](../guides/ADOPTION-RECORD-TEMPLATE.md).*
*Governance version: v2.0.0*
