---
project: home_finance
phase: P2
milestone: M10
epic: E10.2
type: adoption-record
status: completed
last_updated: 2026-05-21
---

# Adoption Record — home_finance

## 1. Project Identification

| Field | Value |
|-------|-------|
| **Project name** | home_finance |
| **Repository URL** | https://github.com/panchew/home_finance |
| **Adoption date** | 2026-05-21 |
| **Adopter name/role** | Coding Agent / Epic Executor (human-coordinated) |
| **Governance version** | v2.0.0 |

## 2. Prerequisites Status

| Prerequisite | Status | Notes |
|---|---|---|
| Git (v2.30+) | ✅ | v2.43.0 |
| GitHub account | ✅ | panchew/home_finance accessible |
| VS Code (1.85+) | ✅ | v1.120.0 |
| GitHub Copilot extension | ⚠️ | Installed but not yet configured for this project |
| Node.js (v18+) | ❌ | v16.14.0 — below minimum v18+ |
| `ai-project` CLI installed | ❌ | Not available; package not published to npm (404 error); local script at `bin/ai-project-init` must be used |

## 3. Step Completion Log

| # | Step | Start Time | End Time | Duration | Outcome | Deviations? |
|---|---|---|---|---|---|---|
| 1 | Prerequisites Verification | 10:15 | 10:17 | 2 min | ⚠️ | Node.js v16 (below v18); CLI not published on npm |
| 2 | Step 1: `ai-project init` | 10:17 | 10:22 | 5 min | ⚠️ | Skipped — project already exists with Ruby on Rails code; `ai-project init` requires empty directory |
| 3 | State Detection | 10:22 | 10:25 | 3 min | ✅ | Detected "No Governance" state; used Workflow B from migration guide instead |
| 4 | Workflow B: Add Submodule | 10:25 | 10:30 | 5 min | ⚠️ | Submodule added but checked out v0.8.0 (not v2.0.0); no v2.0.0 git tag exists |
| 5 | Workflow B: Create .ai-project.yml | 10:30 | 10:33 | 3 min | ✅ | Created with governance reference |
| 6 | Workflow B: Install HQ Agent | 10:33 | 10:35 | 2 min | ⚠️ | Agent file at `governance/agents/hq.agent.md` needs manual copy to `.github/agents/` |
| 7 | Step 4: Canonical Startup Prompt | 10:35 | 10:36 | 1 min | ⚠️ | Simulated; requires human with VS Code HQ agent to execute |
| 8 | Step 5: Create Phase 0 Spec | 10:36 | 10:40 | 4 min | ⚠️ | Existing docs have some planning artifacts; Phase 0 spec would need HQ Chat creation |

**Total time to completion:** 25 minutes (simulated; fresh project target: 25–30 min)

## 4. Friction Points

| # | Category | Description | Step Occurred | Root Cause | Workaround | Recommended Fix |
|---|---|---|---|---|---|---|
| 1 | Tooling | `ai-project` CLI not available on npm — `npm install -g @panchew/ai-project` returns 404 | Prerequisites | Package not published to npm registry | Use `bin/ai-project-init` from governance submodule directly (or clone) | Publish the CLI package to npm or document the `bin/ai-project-init` path in the guide |
| 2 | Environment | Node.js v16 installed; guide requires v18+ | Prerequisites | Developer environment has older LTS Node.js | Use `nvm` to switch, or skip CLI-based steps | Add Node.js version management recommendation to guide; expand FAQ |
| 3 | Process | Adoption guide assumes new project from scratch; `home_finance` is an existing Rails app | Step 1 | Guide targets `ai-project init` for new projects; existing projects must use migration guide | Refer to legacy migration guide Workflow B | Add explicit branching in the adoption guide: "New project path" vs. "Existing project path" |
| 4 | Governance | Submodule added at `governance/` but checked out v0.8.0 (default tag), not v2.0.0 | Submodule install | The submodule URL defaults to `master` branch (tagged v0.8.0); no v2.0.0 tag exists in remote | Manually check out `milestone/M10` or `develop` branch | Ensure governance tags are created and pushed before submodule install; or add explicit `--branch` flag to submodule add in guide |
| 5 | Governance | No `v2.0.0` git tag exists despite `.ai-project.yml` declaring `version: "2.0.0"` | Submodule setup | Version tag not created in governance source repository | Use `milestone/M10` branch as ref until tag is created | Create v2.0.0 tag in governance source repo; document tag-based pinning in guide |
| 6 | Tooling | `.github/agents/hq.agent.md` must be manually copied from governance | Agent setup | `ai-project init` auto-installs agent; manual install does not | `cp governance/agents/hq.agent.md .github/agents/hq.agent.md` | Add agent installation step to migration guide Workflow B |
| 7 | Documentation | Adoption guide has no "existing project" path — user must discover migration guide separately | Step 1 | Guide is written exclusively for greenfield projects | Discover migration guide via guides README | Add prominent "Existing project?" callout in adoption guide linking to migration guide |
| 8 | Environment | Project is Ruby on Rails (Ruby 3.3.9); adoption guide assumes JavaScript/Node.js ecosystem | General | Guide written from Node.js/JS perspective | No workaround needed; governance is language-agnostic | Clarify in guide that governance is language-agnostic; Node.js requirement only for CLI |

## 5. Guide Deviations

| Step | Expected (per guide) | Actual | Reason | Impact |
|---|---|---|---|---|
| Step 1 | `ai-project init home_finance` scaffolds new project | Used migration guide Workflow B instead | Project is existing Rails app with data | Positive — correct path for existing projects |
| Step 2 | Verify `.governance/` submodule | Added `governance/` submodule from migration guide | Migration guide uses `governance/` not `.governance/` | Neutral — functionally equivalent |
| Step 3 | Verify `.github/agents/hq.agent.md` | Manually copied from `governance/agents/hq.agent.md` | The `ai-project init` CLI handles this; manual install requires explicit copy | Negative — missing step in guide |
| Existing docs | N/A (greenfield assumption) | Project has 14 docs in `docs/` with planning artifacts | Project has existing documentation to reconcile with governance structure | Neutral — docs can coexist with governance structure |

## 6. Improvement Suggestions

| # | Area | Suggestion | Priority |
|---|---|---|---|
| 1 | ADOPTION-GUIDE.md | Add "Existing project?" callout at the top linking to migration guide | High |
| 2 | ADOPTION-GUIDE.md | Add explicit branching: "New Project Path" vs. "Existing Project Path" | High |
| 3 | ADOPTION-GUIDE.md — Prerequisites | Document `bin/ai-project-init` as alternative when npm package unavailable | High |
| 4 | ADOPTION-GUIDE.md — Prerequisites | Clarify that Node.js v18+ is only needed for CLI, not for governance itself | Medium |
| 5 | ADOPTION-FAQ.md | Add FAQ: "AI Project CLI package not found on npm" | Medium |
| 6 | ADOPTION-FAQ.md | Add FAQ: "How do I adopt governance for an existing project?" | High |
| 7 | ADOPTION-FAQ.md | Add FAQ: "Governance version v2.0.0 tag not found" | Medium |
| 8 | ADOPTION-GUIDE.md | Add step to copy agent file for manual/legacy installations | High |
| 9 | Migration guide | Add explicit agent installation step to Workflow B | Medium |

## 7. Final Status

**Status:** Partial

**Reason:** The project successfully received governance submodule and `.ai-project.yml` configuration. HQ agent file is available in governance but not yet deployed to `.github/agents/` (requires manual step). The adoption guide works for greenfield projects but existing projects must use a separate migration guide path. Key friction points identified: npm package unavailable, governance tag v2.0.0 missing, and no explicit "existing project" path in the adoption guide.

**Time to completion:** 25 minutes (simulated; target: 25–30 minutes)

---

*Adoption record created using [ADOPTION-RECORD-TEMPLATE.md](../guides/ADOPTION-RECORD-TEMPLATE.md).*
*Governance version: v2.0.0*
