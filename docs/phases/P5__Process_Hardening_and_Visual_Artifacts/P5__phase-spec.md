---
phase: P5
name: Process Hardening and Visual Artifacts
status: active
start_date: 2026-06-21
planned_end_date: 2026-07-31
version: 1.0.0
---

# Phase P5: Process Hardening and Visual Artifacts

## Executive Summary

Phase P5 addresses two distinct but parallel objectives:

1. **Process Hardening** — close the six governance gaps and adoption-clarity issues
   surfaced during P4 execution (P5-GH-1 through GH-6; GH-7 was resolved as an emergency
   patch before scoping opened). These range from false-green prerequisite checks to
   platform lock-in in the governance delivery path.

2. **Visual Artifacts** — establish visual artifact production as a first-class,
   opt-in capability at every chat level (P5-VA-1). Governance framework scope only:
   `.ai-project.yml` spec extension, AI-OPERATING-GUIDELINES.md additions, and `seed.md`
   visual intent elicitation. Full ComfyUI agent implementation is deferred to the
   future agentic app.

---

## Vision

By the end of P5:

- ✅ **False-green prerequisite checks are eliminated** — starters verify artifacts are
  git-tracked, not merely present on disk
- ✅ **Concurrent chats are safe** — working-tree isolation is a documented convention,
  not tribal knowledge
- ✅ **CFO scope direction always leaves an artifact trail** — the routing rule is in the
  operating guidelines and chat hierarchy
- ✅ **Any tool-capable agent can produce visuals** — when enabled, every chat level
  has clear guidance on what visual to produce and how
- ✅ **New adopters reach the right starting point on the first read** — the
  `governance/` vs `.governance/` split, the platform-agnostic delivery path, and the
  Creation Chat session opener are all surfaced before confusion can occur

---

## Scope

### P5.1: Governance Process Hardening (M20)

Close the five governance gaps that will recur and compound with concurrency (three from P4 execution; two from SN-12 2026-06-25).

**P5-GH-1 — Prerequisite git-tracking verification**

The Stage 1 prerequisite checklist in Milestone and Epic Execution Chat Starters accepts
file existence on disk as proof of "committed." An artifact can be untracked in git (as
happened with the SN-9 reference Steering Note during M19) and still pass the check.
The fix is a wording change: "verified with `git ls-files --error-unmatch <path>` on the
expected branch" replaces "file exists."

**P5-GH-2 — Working-tree isolation convention**

Two active chats sharing one working tree can switch the branch under each other and
commit to the wrong place silently. No convention exists assigning tree ownership per chat.
The fix is a documented rule in `governance/systems/chat-hierarchy.md` and
`governance/AI-OPERATING-GUIDELINES.md`: one `git worktree` per concurrently-active chat;
a chat never operates in a tree another concurrent chat may switch.

**P5-GH-3 — Scope routing rule**

CFO / Creation Chat scope direction to an in-flight Epic currently has no documented
mandatory channel. The fix is a formal rule in `chat-hierarchy.md` and AOG: direction
must flow as Steering Note → HQ Chat → spec amendment → Milestone Chat re-issues amended
starter. The P0-emergency exception and its after-the-fact formalization requirement are
also documented.

**P5-GH-8 — Artifact scope adjacency** (SN-12a, 2026-06-25)

Phase Execution Chats have been producing Epic Execution Chat Starters — skipping the
Milestone Chat layer and bypassing its review gate. The rule: each chat level produces
artifacts only for its direct parent or direct children. No grandchild or grandparent
artifacts. The fix is an explicit adjacency rule in the Critical Rules section of Phase
and Milestone Execution Chat Starter templates and in AOG §3.6 and §3.7.

**P5-GH-9 — Hierarchical communication protocol** (SN-12b, 2026-06-25)

The governance model defines upward artifact types (Escalation Notices, Completion
Notices) but does not define how downward communication propagates when a parent needs
to reach multiple concurrent children. The fix: document the spec-as-channel model —
upward is 1-to-1 (one level at a time, no skipping); downward is via spec amendment
(one write, many readers); the spec file is both a planning artifact and a live contract;
mid-flight updates escalate UP, not into running child sessions.

### P5.2: Adoption Clarity and Platform Agnosticism (M21)

Close the three adoption-facing gaps that currently confuse or block new adopters.

**P5-GH-4 — Creation Chat session opener missing from start-a-project.md**

`governance/systems/start-a-project.md` describes how to fill in `genesis.md` but does
not tell users to first paste `governance/templates/seed.md` into a Claude session to
open the Creation Chat. A new adopter has no Creation Chat and no guidance on how to
start one. A "Step 0: Open the Creation Chat" section resolves this.

**P5-GH-5 — Platform agnosticism**

The governance framework references `.github/agents/` as the canonical path for agent
delivery (a GitHub Copilot convention). This silently excludes Claude Code, Cursor,
Windsurf, and any other tool that does not use that path. The fix: decouple governance
delivery from `.github/agents/`; add tool-specific integration guides alongside the
existing Copilot guide; update the adoption guide and start-a-project.md.

**P5-GH-6 — governance/ vs .governance/ documentation clarity**

Two distinct directories exist: `governance/` (the framework source repo itself, used
when dogfooding) and `.governance/` (the submodule path in consumer projects). Adoption
guides and sync guides reference both without explaining the split upfront. New adopters
who clone the framework and attempt to follow the adoption guide hit silent failures.
The fix: a prominent note at the top of ADOPTION-GUIDE.md, GOVERNANCE-SYNC-GUIDE.md,
and start-a-project.md that explains the self-referential vs. submodule distinction before
any path-sensitive instructions.

### P5.3: Visual Artifacts (M22)

Establish the visual artifact capability in the governance framework. Scope is the
framework layer only — spec, guidelines, and templates. The full agentic implementation
(agent tool calls to ComfyUI, video pipeline) is deferred to the agentic app.

**P5-VA-1 — Visual artifact production capability**

Binding decisions from SN-11 (2026-06-21):
- Opt-in via `visual_artifacts.enabled` in `.ai-project.yml` (same pattern as
  `cfo_review_gate`)
- Visual abstraction level mirrors chat level (see table below)
- Tool-calling capability is the gate for visual production, not chat level label
- Two visual modes: structural (Mermaid/PlantUML) and generative (ComfyUI API)
- Visual intent originates at Creation Chat and propagates down the artifact cascade
- Video output (ComfyUI video nodes) is in scope
- `seed.md` must elicit "what does success look like visually?" before Project Brief

**Scope clarification (2026-06-21):** Full implementation is in scope for P5. Agents
already have tool-calling capability sufficient to call the ComfyUI API. The ComfyUI
instance availability and readiness is the CFO's responsibility (to be managed via the
ComfyUI project, which will adopt governance separately). P5 delivers a working visual
artifact capability — spec, guidelines, and integration — not just documentation.

| Chat level | Visual type |
|------------|-------------|
| Creation Chat | Concept / vision imagery |
| HQ Chat | System architecture |
| Phase Chat | Phase scope diagram |
| Milestone Chat | Component + flow diagrams |
| Epic Chat | UI mockups, before/after, implementation diagrams |

Proposed `.ai-project.yml` additions:

```yaml
visual_artifacts:
  enabled: false          # opt-in; default false
  comfyui_url: http://localhost:8188
  types:
    - diagrams            # Mermaid/PlantUML structural diagrams
    - infographics        # ComfyUI-generated imagery
    - video               # ComfyUI video generation (optional)
```

---

## Milestones

### M20: Governance Process Hardening (5 Epics)

**Goal:** Eliminate the three P4 execution gaps that recur and worsen with concurrency.

**Epics:**
- **E20.1 — Prerequisite git-tracking verification** (GH-1)
  - Amend Stage 1 prerequisite checklist wording in Milestone and Epic Execution Chat
    Starter templates: file existence → `git ls-files --error-unmatch <path>` on the
    expected branch
  - Add test coverage for the amended checklist language (schema test or doc test)

- **E20.2 — Working-tree isolation convention** (GH-2)
  - Add "Working-Tree Isolation" section to `governance/systems/chat-hierarchy.md`:
    one worktree per concurrently-active chat; no cross-chat branch switching
  - Add corresponding rule to `governance/AI-OPERATING-GUIDELINES.md` §3 (Chat Rules)
  - Add example: `git worktree add ../worktree-milestone-M21 milestone/M21`

- **E20.3 — Scope routing rule** (GH-3)
  - Add "Scope Direction Protocol" to `governance/systems/chat-hierarchy.md`:
    mandatory Steering Note → HQ → spec amendment → re-issued starter channel
  - Add P0-emergency exception and formalization requirement
  - Add corresponding rule to `governance/AI-OPERATING-GUIDELINES.md` §3

- **E20.4 — Artifact scope adjacency** (GH-8)
  - Add explicit adjacency rule to the Critical Rules section of
    `governance/templates/phase-execution-chat-starter.md` and
    `governance/templates/milestone-execution-chat-starter.md`: each chat level produces
    artifacts only for its direct parent or direct children; no grandchild or grandparent
    artifacts
  - Add corresponding rule to AOG §3.6 (Phase Chat) and §3.7 (Milestone Chat)
  - Add the adjacency table to `governance/systems/chat-hierarchy.md`

- **E20.5 — Hierarchical communication protocol** (GH-9)
  - Add "Communication Protocol" section to `governance/systems/chat-hierarchy.md`:
    - Upward: 1-to-1, one level at a time; no level skips its parent
    - Downward: parent amends its own spec file; children read from that spec at any time
    - Spec file dual role: planning artifact and live contract
    - Mid-flight updates: amend the spec; escalate UP if blocking; never reach into running
      child sessions
  - Add corresponding rules to `governance/AI-OPERATING-GUIDELINES.md` §3 and
    `governance/PROJECT-SYSTEM-GUIDELINES.md`
  - Add guidance to Phase and Milestone Execution Chat Starter templates on how to issue
    amendments (amend the spec, note the change, notify parent chat)

### M21: Adoption Clarity and Platform Agnosticism (2 Epics)

**Goal:** Remove the friction points that block or mislead new adopters on first contact.

**Epics:**
- **E21.1 — Platform agnosticism** (GH-5)
  - Decouple governance delivery from `.github/agents/`; define a platform-agnostic
    delivery convention (e.g., `.ai-project/agents/` or equivalent)
  - Add integration guides for Claude Code, Cursor, and Windsurf alongside the existing
    Copilot guide in `governance/guides/`
  - Update ADOPTION-GUIDE.md and start-a-project.md to reference the platform-agnostic
    path and link to tool-specific guides

- **E21.2 — Adoption documentation clarity** (GH-6 + GH-4)
  - Add "Self-referential vs. submodule: how to read this guide" note at the top of
    ADOPTION-GUIDE.md, GOVERNANCE-SYNC-GUIDE.md, and start-a-project.md
  - Add "Step 0: Open the Creation Chat" section to start-a-project.md (paste seed.md)
  - Verify no other path-sensitive adoption instructions suffer the same ambiguity

### M22: Visual Artifacts (2 Epics)

**Goal:** Spec and document the visual artifact capability so any tool-capable agent
can produce visuals when the feature is enabled. Framework layer only.

**Epics:**
- **E22.1 — Configuration and spec** (VA-1 config layer)
  - Add `visual_artifacts` block to `.ai-project.yml` spec (`governance/ai-project-yml-spec.md`)
  - Define fields: `enabled`, `comfyui_url`, `types` (diagrams, infographics, video)
  - Add schema validation and test coverage for the new block
  - Update `.ai-project.yml` in this repo with `enabled: false` default

- **E22.2 — Guidelines, templates, and agent integration** (VA-1 full implementation)
  - Add "Visual Artifact Production" section to `governance/AI-OPERATING-GUIDELINES.md`
    (when enabled: what each chat level produces, how to produce structural vs. generative,
    what files to commit and where)
  - Update `governance/templates/seed.md` Rule 4 to elicit visual intent before Project
    Brief: "What does success look like visually?"
  - Implement ComfyUI API integration callable by any tool-capable agent: a helper
    (`bin/ai-project-visual` or equivalent) that accepts a prompt, type, and output path,
    calls the ComfyUI endpoint from `.ai-project.yml`, and writes the result
  - Add `governance/guides/visual-artifacts.md`: endpoint configuration, structural
    diagram tooling, output formats, and a worked example of each chat level's visual
  - Add integration test against the ComfyUI endpoint (skipped when `enabled: false`)

---

## Success Criteria

### P5 is Complete When:

1. ✅ **No false-green prerequisite checks** — starters mandate git-tracking verification
2. ✅ **Concurrent chat safety documented** — worktree isolation rule in chat-hierarchy.md + AOG
3. ✅ **Scope routing rule documented** — Steering Note channel mandatory in chat-hierarchy.md + AOG
4. ✅ **Artifact scope adjacency enforced** — adjacency rule in starters, AOG §3.6/§3.7, and chat-hierarchy.md
5. ✅ **Hierarchical communication protocol defined** — 1-to-1 upward, spec-as-channel downward, mid-flight amendment protocol in AOG, PSG, and starters
6. ✅ **Visual artifacts fully implemented** — `.ai-project.yml` extension validated;
   AOG directs agents at every level; `seed.md` elicits visual intent; ComfyUI helper
   callable by any tool-capable agent; integration test passes against live endpoint
7. ✅ **Platform-agnostic delivery** — no GitHub-specific paths required in governance delivery
8. ✅ **Adoption clarity** — `governance/` vs `.governance/` explained upfront; Creation Chat
   opener step present in start-a-project.md

---

## Acceptance Criteria

The CFO (Layer 8) will accept P5 complete when:

- [ ] Opening a new Milestone Chat Starter in a fresh worktree shows the git-tracking
  check prominently in Stage 1
- [ ] The working-tree isolation convention is findable from `chat-hierarchy.md` without
  searching elsewhere
- [ ] A new adopter using Cursor (not GitHub Copilot) can reach the governance agent
  delivery step without platform-specific dead ends
- [ ] `start-a-project.md` begins with the Creation Chat session opener step
- [ ] `governance/ai-project-yml-spec.md` documents the `visual_artifacts` block
- [ ] AOG directs an agent to produce a Mermaid diagram when `visual_artifacts.enabled: true`
  and the agent is operating as a Phase Chat
- [ ] `bin/ai-project-visual` (or equivalent) can be called from a tool-capable agent,
  calls the configured ComfyUI endpoint, and writes a visual artifact to the repo

---

## Dependencies

### Internal
- P4 governance framework fully operational (complete)
- GH-7 emergency patch merged (AOG + PSG v2.1.0, complete)
- `governance/templates/seed.md` exists (complete — delivered P4 v4.0.0)

### External
- CFO's local ComfyUI instance (for future agentic app integration — not required for P5 spec work)

---

## Timeline

**Estimate:** 9 Epics across 3 Milestones
- M20 (Governance Hardening): 5–7 days (5 epics)
- M21 (Adoption Clarity): 5–7 days
- M22 (Visual Artifacts): 5–7 days
- **Total: ~3 weeks**

---

## Reference

### Governing Steering Notes
- SN-12: `2026-06-25__creation-chat__steering-note.md` — Artifact scope adjacency (GH-8) and hierarchical communication protocol (GH-9) (binding)
- SN-11: `2026-06-21__creation-chat__steering-note.md` — Visual artifacts (binding)
- SN-10: `2026-06-20__phase-chat__steering-note.md` — genesis.md placement (resolved)
- P4 Escalation Notice: `2026-06-20T15_00_00Z__P4-M19__escalation_notice.md` — GH-1/2/3 source

### Items Excluded from P5
- CFO Dashboard — deferred by design (was excluded from P4 acceptance criteria)
- GH-7 — closed as v4.0.1 emergency patch before P5 opened
- ComfyUI instance readiness — CFO's responsibility (managed via ComfyUI project adopting governance)

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-06-21 | Initial P5 phase spec. Three milestones (M20–M22), 7 Epics. GH+VA scope authorized by HQ. |
| 1.1.0 | 2026-06-25 | M20 expanded from 3 to 5 Epics. Added GH-8 (artifact scope adjacency, E20.4) and GH-9 (hierarchical communication protocol, E20.5) from SN-12 (2026-06-25). Total Epics: 9. |
