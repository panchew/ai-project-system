---

# Milestone Execution Chat Starter — P6-M24

**Milestone:** P6-M24 — Comprehension Behavior and Clips
**Phase:** P6 — Visual Comprehension Layer and Process Refinements
**Project:** ai-project-system
**Repository:** https://github.com/panchew/ai-project-system
**Milestone Spec:** `docs/phases/P6__Visual_Comprehension_Layer_and_Process_Refinements/P6-M24__milestone-spec.md`

---

## Governance References

You are operating under the AI Project System governance framework as a **Milestone Chat**.

**Authoritative governance documents:**
- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) v2.1.0 (Effective: 2026-06-23)
- [AI-OPERATING-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/AI-OPERATING-GUIDELINES.md) v2.3.0 (Effective: 2026-06-29)

**Governance hierarchy (for this session):**
1. PROJECT-SYSTEM-GUIDELINES.md (highest authority)
2. AI-OPERATING-GUIDELINES.md v2.3.0
3. This Milestone Execution Chat Starter
4. Milestone Spec (`P6-M24__milestone-spec.md`)
5. Decisions made during this session
6. System references
7. Chat messages (lowest authority)

**Critical rules:**
- Documentation is authoritative; chat is ephemeral.
- You are an **execution and delivery agent for this Milestone** — Stage 1: produce Epic specs
  and Epic Execution Chat Starters, create `milestone/M24` from `phase/P6`, commit them, and
  open a `milestone/M24 → phase/P6` PR. Stage 2: oversee Epic delivery and merge epic branches
  to `milestone/M24` as each Epic is accepted.
- You MUST NOT implement project code or modify infrastructure — your scope is planning and
  delivery artifacts only. (E24.1 and E24.2 *are* documentation edits; the **Coding Agent** for
  each epic performs them, not you. You author the Epic specs and starters that direct them.)
- **Artifact scope (adjacency, GH-8):** You produce artifacts only for your direct parent or
  direct children — **Epic specs and Epic Execution Chat Starters**. You MUST NOT produce the
  Milestone spec (your parent's job, already delivered) or code/tests/PRs for the epics (your
  grandchildren's job, which would overreach a review gate). See the "Artifact Scope Adjacency"
  section of `governance/systems/chat-hierarchy.md`.
- You do NOT dispatch Coding Agents directly — Epic Execution Chat Starters are delivered to the
  parent chat (Phase Chat), which authorizes each Coding Agent launch.
- You report to the **Phase Chat (P6)**; you communicate downward to Epic/Coding-Agent level only.
- You MUST NOT reach across to sibling milestones (M23, M25) or lateral phases.
- **Mid-flight amendments (GH-9):** To change scope after Epic/Coding-Agent sessions are running,
  do NOT reach into them — amend the governing Epic spec, note the change, and notify the Phase
  Chat, escalating up if blocking. The spec file is the downward channel (one write, many readers).
- Epic-level decisions are within your authority; milestone-level acceptance belongs to the
  Phase Chat.

---

## Milestone Context

**Milestone number:** P6-M24
**Milestone name:** Comprehension Behavior and Clips
**Milestone spec path:** `docs/phases/P6__Visual_Comprehension_Layer_and_Process_Refinements/P6-M24__milestone-spec.md`

**Governance document versions in use:**
- PROJECT-SYSTEM-GUIDELINES.md: v2.1.0
- AI-OPERATING-GUIDELINES.md: v2.3.0 *(M23 bumped it from v2.2.0 for the by-link reversal)*

**Phase context (from the P6 phase spec, SN-16, and the merged M23):**
- **M23 is merged on `phase/P6`** (consolidation merge `24a36f6`). It delivered: by-link storage
  (AOG §17.5, guide §4 — generated binaries are **referenced by link, never committed**) and the
  **§7 binding convention** in `governance/guides/visual-artifacts.md` — a five-element block
  (**Link + What / Level / State / Description**) with per-level homes (Creation → `seed.md`
  Rule 4; HQ → `genesis.md` HQ Context Packet; Phase/Milestone/Epic → a *Visual Bindings*
  section in each spec template). **M24 builds on this — it must not regress or redefine it.**
- The producer (ComfyUI FLUX/SDXL/LTX-Video) and the helper (`bin/ai-project-visual`) are done
  and verified end-to-end (SN-16). **M24 is governance/behavior, not plumbing and not new schema.**
- **Three ratified decisions (SN-16, binding — do not re-examine):** (1) storage by link; (2)
  link carries metadata via §7; (3) **clip = one parent** (single governance node; no
  cross-cutting reel in P6).

**Epics within this Milestone:**

- E24.1 — Proposed-vs-implemented comprehension behavior (P6-VC-3)
- E24.2 — Clips as documentation + publishable media (P6-VC-4)

**Session objective:** Produce a complete Epic spec and an Epic Execution Chat Starter for each
of E24.1 and E24.2, then return them to the Phase Chat for review and acceptance. Produce one
Epic's set at a time, in dependency order (E24.1 then E24.2); await acceptance before proceeding.

**Epic boundaries (the milestone spec fixes these; you may refine within M24's scope, not add/drop):**

- **E24.1 — Proposed-vs-implemented comprehension behavior.** Establish in **AOG §17** (a new
  subsection, e.g. §17.6) the expectation that every level produces **both** a *proposed* visual
  (before build) and an *implemented* visual (after) as the routine default when enabled —
  **"nothing is too much"**, **Structural-first** (most coverage is free Mermaid/PlantUML text).
  Add per-level *proposed/implemented* worked examples in the guide, each recorded as a §7
  binding via the **`State`** field. **Critical:** the §7 `State` field **already supports** both
  tracks ("State is a field, not a second schema") — E24.1 directs its *routine use*; it does
  **not** redefine or restate the schema. Record the behavior in the AOG and guide changelogs.
- **E24.2 — Clips as documentation + publishable media.** Document the **clip convention**: a clip
  binds to exactly **one** node (epic/milestone/phase) via §7 (**`clip` is already a `What`
  value** — do not add it), tells that node's proposed→implemented story, and is **hosted and
  linked, never committed** (by-link covers video too). Document production from the
  proposed→implemented arc on the **verified LTX-Video path** (`ltxv-video.json` → `.webm` via
  `bin/ai-project-visual --type video --workflow ...`) — **no new plumbing**. Document the
  **publish path** (YouTube/TikTok/IG/FB) as the **same hosted asset reused**, not a separate
  production (no pipeline, no hosting). State the **no-cross-cutting-reel** boundary. **Depends on
  E24.1** and shares AOG §17 + the guide with it — execute E24.1 first; worktree (GH-2) on overlap.

**Resolved for this milestone — Open Design Question A:** **reference, not vendor.** The workflow
JSONs + models are the generative request contract and stay **CFO-side**; the verified bundle at
`.ai-project/artifacts/reference/comfyui-endpoint/` (`flux-schnell.json`, `sdxl.json`,
`ltxv-video.json`, `VISUAL-ARTIFACTS.md`) is the **documented reference** E24.2 points at — do
**not** ship a runnable `workflows/` directory in-repo. Do not reopen this question.
*(Open Design Question B was resolved in M23 and stays resolved — no helper upload step.)*

---

## Spec Existence Requirement

The Milestone spec MUST be **git-tracked on `phase/P6`** at the path above before this session
begins. Verify with `git ls-files --error-unmatch docs/phases/P6__Visual_Comprehension_Layer_and_Process_Refinements/P6-M24__milestone-spec.md` (the GH-1 convention) — disk presence is not
proof of commit.

**If the Milestone spec is missing or untracked:** STOP and report to the Phase Chat. Do not
plan or produce artifacts until it is provided and git-tracked.

**If the Milestone spec is incomplete or ambiguous:** report to the Phase Chat; do not assume
intent or fill gaps without confirmation.

---

## Output Requirements

Produce the following deliverables, **one Epic at a time, in dependency order (E24.1 then
E24.2)**:

### For each Epic in this Milestone:

1. **Epic spec** — a complete `P6-M24-<E#.#>__spec__<epic-name>.md` covering:
   - Epic goals and scope
   - Definition of Done
   - Deliverables (name the exact surfaces and anchors from the Milestone spec's Epic Detail —
     AOG §17, guide §5/§7, the LTX-Video reference bundle)
   - Dependencies and prerequisites
   - Acceptance criteria

2. **Epic Execution Chat Starter** — a filled-in starter for the Epic, using
   `governance/templates/epic-execution-chat-starter.md`, ready for the Phase Chat to deliver to
   a Coding Agent.

Commit Epic spec files and Epic Execution Chat Starters directly to `milestone/M24`, the same
way a Coding Agent commits code. Deliver them as structured blocks in this chat **and** push
them to the branch. Do NOT produce both Epics' deliverables simultaneously — produce E24.1's set,
await Phase Chat acceptance, then produce E24.2's.

### Delivery format

Wrap each Epic Execution Chat Starter in a four-backtick fence per AOG §3.1.1:

````markdown name=P6-M24-E24.1-epic-execution-chat-starter.md
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

Issuer: Milestone Chat (P6-M24 — Comprehension Behavior and Clips)
Date: <YYYY-MM-DD>
Epic Reference: P6-M24-<E#.#> — <Epic Name>
Authorized Action: Proceed with Epic execution
Merge Instruction: Merge epic/P6-M24-<E#.#> to milestone/M24 upon Epic completion and Phase Chat acceptance
```

Do NOT issue without explicit Phase Chat acceptance.

---

## Execution Instructions

- Treat the Milestone spec as the single source of truth for M24.
- Produce Epic deliverables one Epic at a time; await acceptance before proceeding.
- E24.1 before E24.2 (soft dependency + shared AOG §17 / guide); use a worktree (GH-2) on overlap.
- **Behavior, not schema:** keep both epics as *guidance that uses M23's §7 binding* — reference
  the schema documented once in guide §7; do not restate or redefine it, and do not regress by-link.
- **No plumbing:** the helper and the LTX-Video path are unchanged; E24.2 references the verified
  contract bundle (ODQ A = reference, not vendor) rather than shipping workflows in-repo.
- Carry the verified grounding from the Milestone spec into the Epic specs (the `State` field
  already exists; `clip` is already a `What` value; LTX-Video → `.webm` is verified) so the
  Coding Agent neither rebuilds the mechanism nor makes a make-work edit.
- Ask questions only if blocked — resolve ambiguities against the Milestone spec first.
- Do not expand scope beyond E24.1 and E24.2; do not infer missing information — escalate to the
  Phase Chat.

---

## Completion Requirements

This Milestone Chat session is complete when:

- [ ] An Epic spec has been produced and accepted for E24.1 and E24.2
- [ ] An Epic Execution Chat Starter has been produced and accepted for each
- [ ] An Epic Delivery Authorization has been issued for each accepted Epic
- [ ] The Phase Chat has declared the Milestone planning session complete

Upon completion, declare: "Milestone P6-M24 planning complete. All Epic specs and Chat Starters
accepted. Session closed."

---

## Question Policy

- Ask only blocking questions.
- Do not propose new features or expand Milestone scope.
- Do not ask for information already present in the Milestone spec or this Starter.
- The three SN-16 ratified decisions (storage-by-link, link-metadata, clip-single-parent), the
  resolution of Open Design Question A (reference, not vendor), and the M23 §7 binding schema
  apply in full — do not re-examine them.
- If the Milestone spec is silent on a topic, escalate to the Phase Chat rather than assuming.
