---

# Milestone Execution Chat Starter — P6-M23

**Milestone:** P6-M23 — By-Link Storage Model and Binding Convention
**Phase:** P6 — Visual Comprehension Layer and Process Refinements
**Project:** ai-project-system
**Repository:** https://github.com/panchew/ai-project-system
**Milestone Spec:** `docs/phases/P6__Visual_Comprehension_Layer_and_Process_Refinements/P6-M23__milestone-spec.md`

---

## Governance References

You are operating under the AI Project System governance framework as a **Milestone Chat**.

**Authoritative governance documents:**
- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) v2.1.0 (Effective: 2026-06-23)
- [AI-OPERATING-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/AI-OPERATING-GUIDELINES.md) v2.2.0 (Effective: 2026-06-28)

**Governance hierarchy (for this session):**
1. PROJECT-SYSTEM-GUIDELINES.md (highest authority)
2. AI-OPERATING-GUIDELINES.md v2.2.0
3. This Milestone Execution Chat Starter
4. Milestone Spec (`P6-M23__milestone-spec.md`)
5. Decisions made during this session
6. System references
7. Chat messages (lowest authority)

**Critical rules:**
- Documentation is authoritative; chat is ephemeral.
- You are an **execution and delivery agent for this Milestone** — Stage 1: produce Epic specs
  and Epic Execution Chat Starters, create `milestone/M23` from `phase/P6`, commit them, and
  open a `milestone/M23 → phase/P6` PR. Stage 2: oversee Epic delivery and merge epic branches
  to `milestone/M23` as each Epic is accepted.
- You MUST NOT implement project code or modify infrastructure — your scope is planning and
  delivery artifacts only. (E23.1 and E23.2 *are* documentation edits; the **Coding Agent** for
  each epic performs them, not you. You author the Epic specs and starters that direct them.)
- **Artifact scope (adjacency, GH-8):** You produce artifacts only for your direct parent or
  direct children — **Epic specs and Epic Execution Chat Starters**. You MUST NOT produce the
  Milestone spec (your parent's job, already delivered) or code/tests/PRs for the epics (your
  grandchildren's job, which would overreach a review gate). See the "Artifact Scope Adjacency"
  section of `governance/systems/chat-hierarchy.md`.
- You do NOT dispatch Coding Agents directly — Epic Execution Chat Starters are delivered to the
  parent chat (Phase Chat), which authorizes each Coding Agent launch.
- You report to the **Phase Chat (P6)**; you communicate downward to Epic/Coding-Agent level only.
- You MUST NOT reach across to sibling milestones (M24, M25) or lateral phases.
- **Mid-flight amendments (GH-9):** To change scope after Epic/Coding-Agent sessions are running,
  do NOT reach into them — amend the governing Epic spec, note the change, and notify the Phase
  Chat, escalating up if blocking. The spec file is the downward channel (one write, many readers).
- Epic-level decisions are within your authority; milestone-level acceptance belongs to the
  Phase Chat.

---

## Milestone Context

**Milestone number:** P6-M23
**Milestone name:** By-Link Storage Model and Binding Convention
**Milestone spec path:** `docs/phases/P6__Visual_Comprehension_Layer_and_Process_Refinements/P6-M23__milestone-spec.md`

**Governance document versions in use:**
- PROJECT-SYSTEM-GUIDELINES.md: v2.1.0
- AI-OPERATING-GUIDELINES.md: v2.2.0

**Phase context (from the P6 phase spec and SN-16):**
- P5 (v5.0.0) shipped the visual-artifacts **framework**, inert (`enabled: false`). The
  producer (three ComfyUI workflows) and the helper (`bin/ai-project-visual`) are **done and
  verified end-to-end** (SN-16). **M23 is governance/documentation, not plumbing.**
- **Three ratified decisions (SN-16, binding — do not re-examine):** (1) storage by link; (2)
  link carries metadata (what / level / proposed-vs-implemented / short description); (3) clip =
  one parent. Decision 3 is M24's concern, carried here for continuity only.

**Epics within this Milestone:**

- E23.1 — By-link storage reconciliation (P6-VC-1)
- E23.2 — Link + metadata binding convention (P6-VC-2)

**Session objective:** Produce a complete Epic spec and an Epic Execution Chat Starter for each
of E23.1 and E23.2, then return them to the Phase Chat for review and acceptance. Produce one
Epic's set at a time; await acceptance before proceeding to the next.

**Epic boundaries (the milestone spec fixes these; you may refine within M23's scope, not add/drop):**

- **E23.1 — By-link storage reconciliation.** Reverse v5.0.0 commit-the-binary guidance to
  by-link across **four named surfaces** and record the reversal in two changelogs:
  1. `governance/guides/visual-artifacts.md` — §4 "Output formats" prose, the §1 source-repo
     note, **and** the §5 worked-example `--output` paths (all imply commit today).
  2. `governance/AI-OPERATING-GUIDELINES.md` §16.5 "What to commit, and where" (the "Generated
     artifacts … and committed" bullet + the source-repo bullet). AOG is at v2.2.0.
  3. `bin/ai-project-visual` **output guidance only** — docstring usage example + `--output`
     help text frame `--output` as a local working file to host and link, not commit. **No
     behaviour change, no upload step** (Open Design Question B is resolved — see below).
  4. The integration-test surface — `tests/integration/test_visual_artifacts_helper.py`
     **already writes to a `tmp_path` and asserts bytes > 0; it does NOT assert a committed
     binary.** Verify this and **record that it is already by-link-consistent** rather than make
     a make-work edit; reconcile only a residual example path if one implies commit.
  5. Record the change as an explicit **reversal of v5.0.0 shipped guidance** in the AOG
     changelog **and** a guide changelog. *(The guide has no changelog section today — adding
     one, or an equivalent dated reversal note, is part of the work.)*
- **E23.2 — Link + metadata binding convention.** Define the binding schema (a **link** + four
  load-bearing metadata fields: *what / which level / proposed-vs-implemented / short
  description*), the **per-level placement convention** (which artifact a binding attaches to
  and how the link gets there, for Creation / HQ / Phase / Milestone / Epic), and update
  `governance/guides/visual-artifacts.md` plus the relevant per-level templates. **Depends on
  E23.1** (binds a *link*, never a committed path) and shares `visual-artifacts.md` with it —
  execute E23.1 first; use a worktree (GH-2) if overlap arises.

**Resolved for this milestone — Open Design Question B:** the helper stays a minimal one-shot
`prompt → local file` tool; **no upload/link-emitting step is added.** Hosting the local file
and recording its link is the **agent's responsibility**, via the E23.2 binding convention.
E23.1's helper-output guidance reflects this. Do not reopen this question.

---

## Spec Existence Requirement

The Milestone spec MUST be **git-tracked on `phase/P6`** at the path above before this session
begins. Verify with `git ls-files --error-unmatch docs/phases/P6__Visual_Comprehension_Layer_and_Process_Refinements/P6-M23__milestone-spec.md` (the GH-1 convention) — disk presence is not
proof of commit.

**If the Milestone spec is missing or untracked:** STOP and report to the Phase Chat. Do not
plan or produce artifacts until it is provided and git-tracked.

**If the Milestone spec is incomplete or ambiguous:** report to the Phase Chat; do not assume
intent or fill gaps without confirmation.

---

## Output Requirements

Produce the following deliverables, **one Epic at a time, in dependency order (E23.1 then
E23.2)**:

### For each Epic in this Milestone:

1. **Epic spec** — a complete `P6-M23-<E#.#>__spec__<epic-name>.md` covering:
   - Epic goals and scope
   - Definition of Done
   - Deliverables (name the exact surfaces and anchors from the Milestone spec's Epic Detail)
   - Dependencies and prerequisites
   - Acceptance criteria

2. **Epic Execution Chat Starter** — a filled-in starter for the Epic, using
   `governance/templates/epic-execution-chat-starter.md`, ready for the Phase Chat to deliver to
   a Coding Agent.

Commit Epic spec files and Epic Execution Chat Starters directly to `milestone/M23`, the same
way a Coding Agent commits code. Deliver them as structured blocks in this chat **and** push
them to the branch. Do NOT produce both Epics' deliverables simultaneously — produce E23.1's set,
await Phase Chat acceptance, then produce E23.2's.

### Delivery format

Wrap each Epic Execution Chat Starter in a four-backtick fence per AOG §3.1.1:

````markdown name=P6-M23-E23.1-epic-execution-chat-starter.md
[starter content here]
````

After each Epic's set, explicitly request Phase Chat review before proceeding. Under SN-13
default-accept, the Phase Chat accepts a clean delivery by silence; do not wait for a Review
Decision artifact on the happy path.

> **Do NOT produce code, tests, or PRs for the epics, and do NOT modify the Milestone spec.**
> Your deliverables are the two Epic specs and the two Epic Execution Chat Starters only.

---

## Epic Delivery Authorization

When the Phase Chat accepts an Epic's deliverables, issue:

```
EPIC DELIVERY AUTHORIZATION

Issuer: Milestone Chat (P6-M23 — By-Link Storage Model and Binding Convention)
Date: <YYYY-MM-DD>
Epic Reference: P6-M23-<E#.#> — <Epic Name>
Authorized Action: Proceed with Epic execution
Merge Instruction: Merge epic/P6-M23-<E#.#> to milestone/M23 upon Epic completion and Phase Chat acceptance
```

Do NOT issue without explicit Phase Chat acceptance.

---

## Execution Instructions

- Treat the Milestone spec as the single source of truth for M23.
- Produce Epic deliverables one Epic at a time; await acceptance before proceeding.
- E23.1 before E23.2 (soft dependency + shared `visual-artifacts.md`); use a worktree (GH-2) on overlap.
- Carry the verified grounding from the Milestone spec into the Epic specs so the Coding Agent
  neither misses a surface nor makes a make-work edit (especially the integration-test surface,
  which is already by-link-consistent, and the guide's missing changelog).
- Keep the reversal explicit: each surface must end up with **no** instruction to commit a
  generated binary, and the changelogs must record it **as a reversal of v5.0.0**.
- Do not touch structural-diagram guidance (Mermaid/PlantUML stay in git).
- Ask questions only if blocked — resolve ambiguities against the Milestone spec first.
- Do not expand scope beyond E23.1 and E23.2; do not infer missing information — escalate to the
  Phase Chat.

---

## Completion Requirements

This Milestone Chat session is complete when:

- [ ] An Epic spec has been produced and accepted for E23.1 and E23.2
- [ ] An Epic Execution Chat Starter has been produced and accepted for each
- [ ] An Epic Delivery Authorization has been issued for each accepted Epic
- [ ] The Phase Chat has declared the Milestone planning session complete

Upon completion, declare: "Milestone P6-M23 planning complete. All Epic specs and Chat Starters
accepted. Session closed."

---

## Question Policy

- Ask only blocking questions.
- Do not propose new features or expand Milestone scope.
- Do not ask for information already present in the Milestone spec or this Starter.
- The three SN-16 ratified decisions (storage-by-link, link-metadata, clip-single-parent) and
  the resolution of Open Design Question B apply in full — do not re-examine them.
- If the Milestone spec is silent on a topic, escalate to the Phase Chat rather than assuming.
