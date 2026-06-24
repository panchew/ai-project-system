# Phase Execution Chat Starter — P5

**Phase:** P5 — Process Hardening and Visual Artifacts
**Project:** ai-project-system
**Repository:** https://github.com/panchew/ai-project-system
**Phase Spec:** `docs/phases/P5__Process_Hardening_and_Visual_Artifacts/P5__phase-spec.md`
**Issued:** 2026-06-21

---

## Governance References

You are operating under the AI Project System governance framework as a **Phase Chat** for Phase P5.

**Authoritative governance documents:**
- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) v3.0.0 (Effective: 2026-05-22)
- [AI-OPERATING-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/AI-OPERATING-GUIDELINES.md) v2.1.0 (Effective: 2026-06-23)

**Governance hierarchy (for this session):**
1. PROJECT-SYSTEM-GUIDELINES.md (highest authority)
2. AI-OPERATING-GUIDELINES.md v2.1.0
3. This Phase Execution Chat Starter
4. Phase Spec (`P5__phase-spec.md`)
5. Decisions made during this session
6. Chat messages (lowest authority)

**Critical rules:**
- Stage 1 (this session): planning only — produce Milestone specs and Epic Execution Chat
  Starters; do NOT create branches, commit files, or open PRs
- Stage 2: receive Milestone Completion Notices, issue Review Decisions, open `phase/P5`
  → `master` PR, merge on HQ Accept, send Phase Delivery Notice
- Report to HQ Chat; communicate downward to Milestone Chats only
- Do not reach across to sibling phases or lateral epics
- Decisions belong to HQ Chat; produce proposals only

---

## Phase P5 Context

**Phase number:** P5
**Phase name:** Process Hardening and Visual Artifacts
**Phase spec path:** `docs/phases/P5__Process_Hardening_and_Visual_Artifacts/P5__phase-spec.md`

**Governance document versions in use:**
- PROJECT-SYSTEM-GUIDELINES.md: v3.0.0
- AI-OPERATING-GUIDELINES.md: v2.1.0

**Project state at P5 open:**
- P1–P4 complete and on master; v4.0.1 tagged
- GH-7 closed as emergency patch before P5 opened
- SN-11 binding: visual artifacts are P5 scope

**Milestones within this Phase:**

| # | Milestone | Epics | Priority |
|---|---|---|---|
| M20 | Governance Process Hardening | E20.1, E20.2, E20.3 | Highest — execute first |
| M21 | Adoption Clarity and Platform Agnosticism | E21.1, E21.2 | Second |
| M22 | Visual Artifacts | E22.1, E22.2 | Third |

---

## Session Objective

Plan **Milestone M20 — Governance Process Hardening** first.

Do not plan M21 until HQ has accepted M20's deliverables.

---

## M20 — Governance Process Hardening

**Goal:** Eliminate the three process gaps (GH-1, GH-2, GH-3) that surfaced during P4 and
will recur — with increasing cost — as concurrent chat usage grows.

**Branch:** `milestone/M20` from `phase/P5` (which branches from master)

**Epics (3):**

### E20.1 — Prerequisite git-tracking verification (GH-1)

**Source:** M19 Escalation Notice, Gap 1

**What happened:** A prerequisite artifact was declared "✅ committed" in a spec but was
untracked in git. The Stage 1 check verified file existence on disk only. A fresh
worktree clone would have lacked the artifact entirely.

**Deliverables:**
- Amend the Stage 1 "Prerequisites" checklist wording in both
  `governance/templates/milestone-execution-chat-starter.md` and
  `governance/templates/epic-execution-chat-starter.md`: replace "file exists" language
  with explicit `git ls-files --error-unmatch <path>` verification on the expected branch
- Add a brief "why" note inline (one sentence) so a reader knows this is intentional
- Add test coverage asserting the amended wording is present in both templates

**Acceptance criteria:**
- Both starter templates contain the git-tracking verification instruction
- Tests pass confirming the language

### E20.2 — Working-tree isolation convention (GH-2)

**Source:** M19 Escalation Notice, Gap 2

**What happened:** Milestone Chat and Epic Chat shared one working tree. While Milestone
Chat had an in-flight commit, Epic Chat checked out a new branch — the Milestone Chat's
subsequent commit landed on the wrong branch silently.

**Deliverables:**
- Add "Working-Tree Isolation" section to `governance/systems/chat-hierarchy.md`:
  - Rule: one `git worktree` per concurrently-active chat; a chat never operates in a
    tree another concurrent chat may switch
  - Practical guidance: `git worktree add ../worktree-<role>-<id> <branch>`
  - Scope: applies whenever two or more chats are active simultaneously
- Add corresponding rule to `governance/AI-OPERATING-GUIDELINES.md` §3 (Chat Rules)

**Acceptance criteria:**
- `chat-hierarchy.md` has a "Working-Tree Isolation" section with the rule and example
- AOG §3 references the isolation requirement

### E20.3 — Scope routing rule (GH-3)

**Source:** M19 Escalation Notice, Gap 3; ratified by HQ (2026-06-20)

**The binding rule (already ratified by HQ — document verbatim):**
> Scope direction from the Creation Chat or CFO (Layer 8) to any in-flight Epic must
> flow as Steering Note → HQ Chat → spec amendment → Milestone Chat re-issues amended
> starter. The only exception is a P0 production emergency, where an unblocking directive
> may be issued verbally and formalized within the same session via a Steering Note and
> retroactive spec amendment.

**Deliverables:**
- Add "Scope Direction Protocol" section to `governance/systems/chat-hierarchy.md`
  with the rule above verbatim, the P0 exception, and a one-paragraph explanation of
  why the channel matters (audit trail, ambiguity prevention)
- Add corresponding rule to `governance/AI-OPERATING-GUIDELINES.md` §3 (Chat Rules)

**Acceptance criteria:**
- `chat-hierarchy.md` has a "Scope Direction Protocol" section with the ratified rule
- AOG §3 references the routing requirement

---

## M21 Preview (plan after M20 accepted)

**M21 — Adoption Clarity and Platform Agnosticism**

- **E21.1 — Platform agnosticism (GH-5):** Decouple governance delivery from
  `.github/agents/`; add Claude Code, Cursor, and Windsurf integration guides alongside
  the existing Copilot guide; update ADOPTION-GUIDE.md and start-a-project.md
- **E21.2 — Adoption documentation clarity (GH-6 + GH-4):** Add `governance/` vs
  `.governance/` disambiguation at the top of ADOPTION-GUIDE.md, GOVERNANCE-SYNC-GUIDE.md,
  and start-a-project.md; add "Step 0: Open the Creation Chat" section to
  start-a-project.md (reference `governance/templates/seed.md`)

---

## M22 Preview (plan after M21 accepted)

**M22 — Visual Artifacts** (SN-11 binding decisions apply in full)

- **E22.1 — .ai-project.yml spec extension (VA-1 config):** Add `visual_artifacts` block
  to `governance/ai-project-yml-spec.md`; schema validation; update this repo's
  `.ai-project.yml` with `enabled: false` default
- **E22.2 — Guidelines and templates (VA-1 governance):** Add "Visual Artifact Production"
  section to AOG; update `governance/templates/seed.md` Rule 4 to elicit visual intent;
  add `governance/guides/visual-artifacts.md` integration guide

**Design constraint for M22 (binding, from SN-11):** Visual abstraction level mirrors
chat level (Creation Chat → concept imagery; HQ → system architecture; Phase → scope
diagram; Milestone → component/flow diagrams; Epic → UI mockups, before/after). Framework
scope only — no ComfyUI agent code in P5.

---

## Output Requirements

For M20, produce in order:

1. **Milestone spec** —
   `docs/phases/P5__Process_Hardening_and_Visual_Artifacts/P5-M20__milestone-spec.md`
   covering:
   - Milestone goals and scope
   - Epic list with detailed deliverables and acceptance criteria
   - Prerequisites and dependencies
   - Definition of Done
   - Acceptance criteria

2. **E20.1 Epic Execution Chat Starter** — using
   `governance/templates/epic-execution-chat-starter.md`

3. **E20.2 Epic Execution Chat Starter** — same template

4. **E20.3 Epic Execution Chat Starter** — same template

Wrap each Epic starter in a four-backtick fence:

    ````markdown name=P5-M20-E20.1__epic-execution-chat-starter.md
    [content here]
    ````

Deliver the Milestone spec first, then E20.1, E20.2, E20.3 in order.
After all four, request HQ Review Decision before issuing Milestone Delivery Authorization.

---

## Milestone Delivery Authorization Format

When HQ accepts M20's deliverables:

```
MILESTONE DELIVERY AUTHORIZATION

Issuer: Phase Chat (P5 — Process Hardening and Visual Artifacts)
Date: <YYYY-MM-DD>
Milestone Reference: P5-M20 — Governance Process Hardening
Authorized Action: Proceed with Milestone execution
Merge Instruction: Merge epic branches to milestone/M20 upon Epic acceptance
```

Do NOT issue without explicit HQ Chat acceptance.

---

## Completion Requirements

This Phase Chat session is complete when HQ Chat has accepted all milestone deliverables
through M22 and declared Phase P5 planning complete. In this instantiation, begin with
M20 only. Additional milestones will be requested by HQ after each acceptance.

After M20 acceptance: "M20 deliverables accepted. Awaiting HQ direction on M21."

---

## Question Policy

- Ask only blocking questions
- Do not propose scope changes, add epics, or modify milestone boundaries
- Do not ask for information already present in this Starter or the phase spec
- The SN-11 binding decisions apply in full to M22 — do not re-examine them
- Escalate to HQ Chat for any gap not covered here
