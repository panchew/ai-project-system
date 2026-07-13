# Milestone Execution Chat Starter — P7-M28

**Milestone:** P7-M28 — Governance Reconciliations
**Phase:** P7 — Agentic Execution and Default-On Visuals
**Project:** ai-project-system
**Repository:** https://github.com/panchew/ai-project-system
**Milestone Spec:** `docs/phases/P7__Agentic_Execution_and_Default_On_Visuals/P7-M28__milestone-spec.md`

---

## Governance References

You are operating under the AI Project System governance framework as a **Milestone Chat**.

**Authoritative governance documents:**
- [PROJECT-SYSTEM-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/PROJECT-SYSTEM-GUIDELINES.md) v2.3.0 (Effective: 2026-07-02)
- [AI-OPERATING-GUIDELINES.md](https://github.com/panchew/ai-project-system/blob/master/governance/AI-OPERATING-GUIDELINES.md) v2.6.0 (Effective: 2026-07-02) — **Note:** M27 bumped
  AOG on `phase/P7`; verify the exact version in force on `phase/P7` at session start rather
  than trusting this number, since this starter predates M27's own consolidation record.

**Governance hierarchy (for this session):**
1. PROJECT-SYSTEM-GUIDELINES.md (highest authority)
2. AI-OPERATING-GUIDELINES.md
3. This Milestone Execution Chat Starter
4. Milestone Spec (`P7-M28__milestone-spec.md`)
5. Decisions made during this session
6. System references
7. Chat messages (lowest authority)

**Critical rules:**
- Documentation is authoritative; chat is ephemeral.
- You are an **execution and delivery agent for this Milestone** — Stage 1: produce Epic specs
  and Epic Execution Chat Starters, create `milestone/M28` from `phase/P7`, commit them, and
  open a `milestone/M28 → phase/P7` PR. Stage 2: oversee Epic delivery, accept clean deliveries
  by silence — a Review Decision is the exception path only (PSG §11.6) — and merge epic
  branches to `milestone/M28` as each Epic is accepted.
- You MUST NOT implement project code or modify infrastructure — your scope is planning and
  delivery artifacts only. All four Epics are documentation/script reconciliations; the
  **Coding Agent** for each epic performs them, not you.
- **Artifact scope (adjacency, GH-8):** You produce artifacts only for your direct parent or
  direct children — **Epic specs and Epic Execution Chat Starters**. You MUST NOT produce the
  Milestone spec (your parent's job, already delivered) or code/tests/PRs for the epics.
- You do NOT dispatch Coding Agents directly — Epic Execution Chat Starters are delivered to
  the parent chat (Phase Chat), which authorizes each Coding Agent launch.
- You report to the **Phase Chat (P7)**; you communicate downward to Epic/Coding-Agent level
  only. You MUST NOT reach across to sibling milestones (M26, M27, both closed) or lateral
  phases. M28 needs no cross-repo coordination.
- **Mid-flight amendments (GH-9):** To change scope after Epic/Coding-Agent sessions are
  running, do NOT reach into them — amend the governing Epic spec, note the change, and
  notify the Phase Chat, escalating up if blocking.
- Epic-level decisions are within your authority; milestone-level acceptance belongs to the
  Phase Chat.
- **This is the final planned P7 milestone (`is_final: true`).** Your Milestone Closure
  Declaration should say so explicitly — it is what triggers the Phase Chat's own phase
  delivery sequence.

---

## Epic Acceptance and Merge Instruction (SN-19 — in-chat, no artifact)

Per SN-19 and PSG §1A gate scoping / §11.6, there is **no Epic Delivery Authorization
artifact or ceremonial block**. When the Phase Chat accepts an Epic's deliverables (by
silence on the happy path), acknowledge the acceptance **in-chat** and proceed. The standing
merge instruction is: **merge `epic/P7-M28-<E#.#>` to `milestone/M28` upon Epic completion,
Phase Chat acceptance, and explicit human merge authorization** — the authorization is an
in-chat act (the CFO says "merge it"; the harness enforces human merge authorization
regardless). **Note the irony worth being deliberate about:** E28.4 is the epic that finishes
retiring this very ceremony from the rest of the framework — apply the already-retired model
to this milestone's own epics, including E28.4 itself, rather than waiting for E28.4 to merge
first.

Do NOT proceed to execution or merge without Phase Chat acceptance.

---

## Milestone Context

**Milestone number:** P7-M28
**Milestone name:** Governance Reconciliations
**Milestone spec path:** `docs/phases/P7__Agentic_Execution_and_Default_On_Visuals/P7-M28__milestone-spec.md`

**Phase context:**
- **M26 (First Real Agentic Run) and M27 (Visuals Default-On) are both fully closed and
  consolidated to `phase/P7`.** M28 is independent of both — no epic here touches the
  orchestrator, the runner adapter, or the visual-artifacts framework.
- **M28 is the final planned P7 milestone** (`is_final: true`). Its consolidation triggers the
  Phase Chat's phase-delivery sequence (`phase/P7 → master`, PR #112, via PSG §5C).
- M28 is pure process hygiene — four independent doc/CLI reconciliations, no new capability,
  no design task.

**Epics within this Milestone:**

- E28.1 — Level-0 handoff reconciliation + HQ starter template (Medium)
- E28.2 — Delivery-Notice ordering reconciliation (Medium)
- E28.3 — init canonical agent file (Low)
- E28.4 — Retire the Delivery Authorization ceremonial block (Medium)

**Session objective:** Produce a complete Epic spec and an Epic Execution Chat Starter for each
of E28.1–E28.4, then return them to the Phase Chat for review and acceptance.

**Sequencing:**
- **E28.1 and E28.3 are fully independent** of every other epic and may be planned/executed in
  parallel with anything else.
- **E28.2 and E28.4 both touch AOG line 716** (Delivery-Notice terminology vs.
  Delivery-Authorization retirement, for different reasons) — serialize them or use a worktree
  (GH-2); whichever runs second must explicitly reconcile with the first's edit, not clobber
  it.
- Still produce one Epic's deliverables at a time and await Phase Chat acceptance before
  proceeding to the next — do not batch multiple Epics' specs/starters into one delivery.

**Epic boundaries (the milestone spec fixes these; you may refine within M28's scope, not
add/drop):**

- **E28.1 — Level-0 handoff reconciliation + HQ starter template.** `seed.md` (Rule 3: Creation
  Chat → HQ Chat; Rule 4: Project Brief + HQ Chat Opener) contradicts `genesis.md` +
  `chat-hierarchy.md`'s Level-0 section (genesis.md → Phase Chat directly, HQ never opened).
  `governance/systems/start-a-project.md` **contradicts itself internally**: Step 3's own
  "Next step" sends the reader to a Phase Chat directly; Steps 5–6 then send the same reader
  to spawn an HQ Chat and use it to "define the first Phase" — already done two steps earlier
  by its own instructions. **A second, materially different file shares the name**
  `docs/systems/start-a-project.md` (P1-era, `2026-01-17`) — determine whether it's a stale
  duplicate to reconcile or remove; do not leave it silently divergent. Recommended default
  (Open Design Question B): codify **both flows as scale-dependent** — lightweight
  `genesis.md` → Phase Chat for small bootstraps; full `seed.md` → Brief + HQ Opener → HQ Chat
  for ongoing projects — stated explicitly in all four docs. Promote
  `governance/systems/hq-chat-opener.md` into `governance/templates/`.
- **E28.2 — Delivery-Notice ordering reconciliation.** This is a **terminology collision**, not
  just an ordering dispute: PSG §12 names "Delivery Notice" the artifact produced
  **immediately upon execution completion** (pre-review); `governance/systems/
  artifact-communication-protocol.md`'s flow diagram names that same pre-review artifact
  "**Completion Notice**" and reserves "Delivery Notice" for what's created **after the PR
  merges** (post-acceptance). AOG line 716 independently repeats PSG §12's framing — **shared
  edit surface with E28.4**, coordinate. The framework's own practiced model (this Phase
  Chat's own M26/M27/B4.1 executions, same session) already matches the P4.1 two-artifact
  convention — the defensible direction is bringing PSG §12 in line with actual practice,
  though state explicit reasoning if you find otherwise.
- **E28.3 — init canonical agent file.** `bin/ai-project-init:328-329,408` installs
  `governance/agents/hq.agent.md` as `.ai-project/agents/hq.agent.md` — the **path** was
  already fixed by E25.3 (P6-M25); this is the **filename**. `hq.agent.md`'s own content
  states it is superseded by `governance/agents/governance.agent.md` ("the single
  `governance.agent.md` replaces all separate agent files"). Fix the script to source/install
  `governance.agent.md`; extend or add to `tests/test_init_agent_path.py` to assert the
  filename (it currently asserts the path with `hq.agent.md`'s name).
- **E28.4 — Retire the Delivery Authorization ceremonial block.** The two **templates**
  (`governance/templates/{milestone,phase}-execution-chat-starter.md`) each carry one
  contained section (already the shape the M26/M27 starters were swept to — use those as your
  reference for what "retired" looks like). The three **`governance/systems/` mirrors** are
  **not** shaped like a single deletable block: `milestone-execution-chat-starter.md` and
  `phase-execution-chat-starter.md` each reference it in a Stage-2 responsibilities step, a
  Communication Protocol table row, *and* a dedicated section (three touch points each);
  `hq-execution-chat-starter.md` has it scattered across a diagram label, an instruction, and
  a Phase-level mention — address each on its own terms. AOG carries it in three places: §1A
  step 6, line 716 (**shared with E28.2**), and line 756. Preserve the in-chat merge
  authorization unchanged everywhere.

---

## Spec Existence Requirement

The Milestone spec MUST be **git-tracked on `phase/P7`** at the path above before this session
begins. Verify with `git ls-files --error-unmatch docs/phases/P7__Agentic_Execution_and_Default_On_Visuals/P7-M28__milestone-spec.md` (the GH-1 convention) — disk presence is not proof of commit.

**If the Milestone spec is missing or untracked:** STOP and report to the Phase Chat. Do not
plan or produce artifacts until it is provided and git-tracked.

**If the Milestone spec is incomplete or ambiguous:** report to the Phase Chat; do not assume
intent or fill gaps without confirmation.

---

## Output Requirements

Produce the following deliverables, **one Epic at a time**:

### For each Epic in this Milestone:

1. **Epic spec** — a complete `P7-M28-<E#.#>__spec__<epic-name>.md` covering:
   - Epic goals and scope
   - Definition of Done
   - Deliverables (name the exact surfaces and anchors from the Milestone spec's Epic Detail —
     file paths and line numbers for `seed.md`/`genesis.md`/`start-a-project.md`/
     `chat-hierarchy.md`, PSG §12, `artifact-communication-protocol.md`, AOG line 716,
     `bin/ai-project-init` lines 328-329/408, the templates + systems mirrors + AOG §1A/§10 for
     E28.4)
   - Dependencies and prerequisites
   - Acceptance criteria

2. **Epic Execution Chat Starter** — a filled-in starter for the Epic, using
   `governance/templates/epic-execution-chat-starter.md`, ready for the Phase Chat to deliver
   to a Coding Agent.

Commit Epic spec files and Epic Execution Chat Starters directly to `milestone/M28`, the same
way a Coding Agent commits code. Deliver them as structured blocks in this chat **and** push
them to the branch. Do NOT produce multiple Epics' deliverables simultaneously — produce one
Epic's set, await Phase Chat acceptance, then the next.

### Delivery format

Wrap each Epic Execution Chat Starter in a four-backtick fence per AOG §3.1.1:

````markdown name=P7-M28-E28.1-epic-execution-chat-starter.md
[starter content here]
````

After each Epic's set, explicitly request Phase Chat review before proceeding. Under the
default-accept model (PSG §11.6), the Phase Chat accepts a clean delivery by silence; do not
wait for a Review Decision artifact on the happy path.

> **Do NOT produce code, tests, or PRs for the epics, and do NOT modify the Milestone spec.**
> Your deliverables are the four Epic specs and the four Epic Execution Chat Starters only.

---

## Execution Instructions

- Treat the Milestone spec as the single source of truth for M28.
- Produce Epic deliverables one Epic at a time; await acceptance before proceeding.
- **E28.2 and E28.4 both edit AOG line 716** — serialize them or use a worktree (GH-2); the
  second to run must reconcile with, not overwrite, the first's edit.
- **E28.1 and E28.3 are independent** and may run in parallel with anything else.
- **E28.1's two findings beyond the phase spec's own description** (the internal
  self-contradiction in `start-a-project.md`; the duplicate-filename question) must be
  addressed in the Epic spec, not silently dropped.
- **E28.4's `governance/systems/` mirrors require per-touch-point edits**, not a uniform
  "delete the section" pass — especially `hq-execution-chat-starter.md`.
- Ask questions only if blocked — resolve ambiguities against the Milestone spec first.
- Do not expand scope beyond E28.1–E28.4; do not infer missing information — escalate to the
  Phase Chat.

---

## Completion Requirements

This Milestone Chat session is complete when:

- [ ] An Epic spec has been produced and accepted for E28.1, E28.2, E28.3, and E28.4
- [ ] An Epic Execution Chat Starter has been produced and accepted for each
- [ ] The Phase Chat has declared the Milestone planning session complete

Upon completion, declare: "Milestone P7-M28 planning complete. All Epic specs and Chat
Starters accepted. Session closed." **Note in your Milestone Closure Declaration, when the
time comes, that M28 is the final planned P7 milestone (`is_final: true`)** — this is what
triggers the Phase Chat's phase-delivery sequence.

---

## Question Policy

- Ask only blocking questions.
- Do not propose new features or expand Milestone scope.
- Do not ask for information already present in the Milestone spec or this Starter.
- The four carry-forwards' existence and intent are settled — do not re-debate them.
- Open Design Question B (Level-0 canonical output) is non-blocking with a recommended
  default — resolve it in E28.1, do not escalate it.
- If the Milestone spec is silent on a topic, escalate to the Phase Chat rather than assuming.
