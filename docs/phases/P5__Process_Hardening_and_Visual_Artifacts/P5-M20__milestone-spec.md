---
milestone: M20
name: Governance Process Hardening
phase: P5
status: planned
start_date: 2026-06-24
epics:
  - E20.1
  - E20.2
  - E20.3
  - E20.4
  - E20.5
is_final: false
---

# Milestone M20 — Governance Process Hardening

## Purpose

Eliminate the five governance process gaps (GH-1, GH-2, GH-3, GH-8, GH-9) that surfaced
during P4 and P5 execution and that will recur — with increasing cost — as concurrent
chat usage grows. M20 is the highest-priority milestone of Phase P5: it hardens the
execution process itself before any further feature work (M21 adoption clarity, M22 visual
artifacts) is layered on top.

This milestone ensures:
- Prerequisite verification proves an artifact is **git-tracked**, not merely present on a
  working-tree disk (GH-1)
- Concurrently-active chats have a **documented working-tree isolation convention**, not
  tribal knowledge (GH-2)
- Scope direction to in-flight Epics always flows through a **mandatory, auditable
  channel** (GH-3)
- Chats produce artifacts only for **directly adjacent levels** — no grandchild or
  grandparent artifacts that bypass a review gate (GH-8)
- Communication follows a **defined hierarchical protocol** — 1-to-1 upward, spec-file
  downward, mid-flight changes escalate up rather than reach into running sessions (GH-9)

---

## Problem Statement

P4 and P5 execution surfaced five latent process defects, each independently capable of
producing silent, hard-to-detect failures:

1. **False-green prerequisites (GH-1).** A prerequisite artifact was declared
   "✅ committed" in a spec but was untracked in git. The Stage 1 check verified file
   existence on disk only. A fresh worktree clone would have lacked the artifact entirely,
   and the dependent chat would have proceeded on a false premise.

2. **Shared working tree (GH-2).** A Milestone Chat and an Epic Chat shared one working
   tree. While the Milestone Chat had an in-flight commit, the Epic Chat checked out a new
   branch — and the Milestone Chat's subsequent commit landed on the wrong branch silently.

3. **Unrouted scope direction (GH-3).** Scope direction from the Creation Chat / CFO to an
   in-flight Epic had no documented mandatory channel, allowing scope to change without an
   audit trail or a spec amendment.

4. **Artifact scope non-adjacency (GH-8).** Phase Execution Chats have been producing Epic
   Execution Chat Starters — skipping the Milestone Chat layer entirely. This collapses the
   hierarchy, removes a review gate, and gives a chat authority over artifacts that belong
   to a non-adjacent level. (Source: SN-12, 2026-06-25. A live instance occurred in this
   very milestone's Stage-1 delivery — see Notes.)

5. **Undefined hierarchical communication (GH-9).** The model defines upward artifacts
   (Escalation/Completion Notices) but not how directives propagate downward, especially
   when one parent must reach several concurrent children. Without a rule, parents are
   tempted to reach into running child sessions. (Source: SN-12, 2026-06-25.)

Each gap is cheap to close as a documentation/wording change now, and expensive to absorb
repeatedly once multiple chats run in parallel as a matter of course.

---

## Goals

By the end of this milestone, the system must:

1. Mandate `git ls-files --error-unmatch <path>` verification on the expected branch as the
   prerequisite check in both the Milestone and Epic Execution Chat Starter templates, with
   a one-sentence inline rationale and test coverage asserting the wording is present.
2. Document a "Working-Tree Isolation" convention in `chat-hierarchy.md` and reference it
   from AOG §3 (Chat Rules): one `git worktree` per concurrently-active chat.
3. Document a "Scope Direction Protocol" in `chat-hierarchy.md` (the HQ-ratified rule,
   verbatim) and reference it from AOG §3, including the P0-emergency exception.
4. Document an **artifact scope adjacency rule** in the Phase and Milestone Execution Chat
   Starter templates' Critical Rules, in AOG §3.6 and §3.7, and as a table in
   `chat-hierarchy.md`: each chat produces artifacts only for its direct parent or children.
5. Document a **hierarchical communication protocol** in `chat-hierarchy.md`, AOG §3, and
   PSG: 1-to-1 upward, spec-file downward, dual-role spec file, mid-flight escalate-up;
   plus amendment guidance in the Phase and Milestone starter templates.

---

## Non-Goals

This milestone explicitly does **not** aim to:

- Build automation, hooks, or CI checks that *enforce* worktree isolation, scope routing,
  adjacency, or the communication protocol at runtime (M20 hardens the documented process;
  tooling is out of scope)
- Re-litigate or modify the HQ-ratified GH-3 rule wording, or the binding SN-12 decisions
  behind GH-8/GH-9 (all documented as ratified)
- Touch adoption documentation (M21) or visual artifacts (M22)
- Retro-amend already-closed P4 specs or notices

---

## In Scope

- Wording amendments to `governance/templates/milestone-execution-chat-starter.md`,
  `governance/templates/epic-execution-chat-starter.md`, and
  `governance/templates/phase-execution-chat-starter.md` (E20.1, E20.4, E20.5)
- New sections in `governance/systems/chat-hierarchy.md`: Working-Tree Isolation (E20.2),
  Scope Direction Protocol (E20.3), artifact adjacency table (E20.4), Communication
  Protocol (E20.5)
- Corresponding rule references in `governance/AI-OPERATING-GUIDELINES.md` §3 / §3.6 / §3.7
  (E20.2–E20.5) and `governance/PROJECT-SYSTEM-GUIDELINES.md` (E20.5)
- Test coverage asserting the amended template wording (E20.1)

## Out of Scope

- Runtime enforcement tooling
- Any M21 / M22 deliverable

---

## Planned Epics

### Confirmed Epics

- **E20.1 — Prerequisite git-tracking verification** (GH-1)
- **E20.2 — Working-tree isolation convention** (GH-2)
- **E20.3 — Scope direction protocol** (GH-3)
- **E20.4 — Artifact scope adjacency** (GH-8)
- **E20.5 — Hierarchical communication protocol** (GH-9)

> **Note on artifact production (and a GH-8 caveat):** Per AOG §3.6 the Phase Chat produces
> the Milestone spec and the **Milestone** Execution Chat Starter; the **Milestone** Chat
> (§3.7) produces Epic specs and **Epic** Execution Chat Starters. During Stage-1 delivery
> the Phase Chat produced Epic Execution Chat Starters for E20.1–E20.3 — itself an instance
> of the GH-8 gap. By HQ decision (2026-06-25, Option B) those three are **retained as
> Phase-provided drafts** for the Milestone Chat to reconcile and re-issue. Consistent with
> GH-8, **no Epic starters were produced for E20.4 or E20.5** — the Milestone Chat produces
> those (and all Epic _specs_) as its own deliverables.

### Deferred Epics

- None.

---

## Epic Detail

### E20.1 — Prerequisite git-tracking verification (GH-1)

**Source:** M19 Escalation Notice, Gap 1.

**Deliverables:**

1. **`governance/templates/milestone-execution-chat-starter.md`** — Amend the prerequisite
   verification language (the "Spec Existence Requirement" section, which today tests disk
   presence) so it requires the prerequisite/spec to be **git-tracked on the expected
   branch**, verified with `git ls-files --error-unmatch <path>`.
2. **`governance/templates/epic-execution-chat-starter.md`** — Add an equivalent
   prerequisite git-tracking verification instruction (alongside the Epic Spec reference /
   `Commit:` line) requiring `git ls-files --error-unmatch <path>` on the expected branch.
3. **Inline rationale (both templates)** — one sentence explaining *why* (disk presence is
   not proof of commit; an untracked file passes a file-exists check but is absent from a
   fresh worktree clone, producing a false-green prerequisite).
4. **Test coverage** — a test (`tests/test_template_prerequisite_wording.py`, or an addition
   to `tests/test_starter_lint.py`) asserting the literal string `git ls-files
   --error-unmatch` is present in **both** template files.

**Definition of Done:**
- [ ] Both starter templates contain the `git ls-files --error-unmatch <path>` verification instruction
- [ ] A one-sentence inline rationale is present in both templates
- [ ] Test asserting the wording in both templates is committed and passing
- [ ] Full test suite passes

**Acceptance Criteria:**
- [ ] Opening either template, the prerequisite check reads as a git-tracking verification on the expected branch, not a disk-existence check
- [ ] `pytest` confirms the language is present in both templates

---

### E20.2 — Working-tree isolation convention (GH-2)

**Source:** M19 Escalation Notice, Gap 2.

**Deliverables:**

1. **`governance/systems/chat-hierarchy.md`** — Add a "Working-Tree Isolation" section:
   - **Rule:** one `git worktree` per concurrently-active chat; a chat never operates in a
     tree another concurrent chat may switch.
   - **Practical guidance:** `git worktree add ../worktree-<role>-<id> <branch>`, with a
     worked example (e.g., `git worktree add ../worktree-milestone-M21 milestone/M21`).
   - **Scope:** applies whenever two or more chats are active simultaneously.
2. **`governance/AI-OPERATING-GUIDELINES.md` §3 (Chat Rules)** — Add a corresponding rule
   stating the isolation requirement and cross-referencing the chat-hierarchy.md section.

**Definition of Done:**
- [ ] `chat-hierarchy.md` has a "Working-Tree Isolation" section with the rule, guidance, and worked example
- [ ] AOG §3 references the isolation requirement and links to the chat-hierarchy.md section
- [ ] Full test suite passes

**Acceptance Criteria:**
- [ ] The working-tree isolation convention is findable directly from `chat-hierarchy.md` without searching elsewhere
- [ ] AOG §3 references the isolation requirement

---

### E20.3 — Scope direction protocol (GH-3)

**Source:** M19 Escalation Notice, Gap 3; ratified by HQ (2026-06-20).

**The binding rule (HQ-ratified — must appear verbatim):**

> Scope direction from the Creation Chat or CFO (Layer 8) to any in-flight Epic must
> flow as Steering Note → HQ Chat → spec amendment → Milestone Chat re-issues amended
> starter. The only exception is a P0 production emergency, where an unblocking directive
> may be issued verbally and formalized within the same session via a Steering Note and
> retroactive spec amendment.

**Worked example (this milestone):** the Phase Chat Stage-1 authority conflict (Starter vs
AOG §3.6) was routed upward via Escalation Notice → HQ Ruling
(`P5-M20__escalation-notice__phase-chat-commit-authority.md` →
`P5-M20__hq-ruling__phase-chat-commit-authority.md`) instead of being silently self-resolved
— a live demonstration of the escalate-up-don't-self-resolve principle this protocol codifies.

**Deliverables:**

1. **`governance/systems/chat-hierarchy.md`** — Add a "Scope Direction Protocol" section
   containing the rule above **verbatim**, the P0 exception, and a one-paragraph
   explanation of why the channel matters (audit trail, ambiguity prevention).
2. **`governance/AI-OPERATING-GUIDELINES.md` §3 (Chat Rules)** — Add a corresponding rule
   stating the routing requirement and cross-referencing the chat-hierarchy.md section.

**Definition of Done:**
- [ ] `chat-hierarchy.md` has a "Scope Direction Protocol" section with the ratified rule verbatim, the P0 exception, and the rationale paragraph
- [ ] AOG §3 references the routing requirement and links to the chat-hierarchy.md section
- [ ] Full test suite passes

**Acceptance Criteria:**
- [ ] `chat-hierarchy.md` has a "Scope Direction Protocol" section with the ratified rule
- [ ] AOG §3 references the routing requirement

---

### E20.4 — Artifact scope adjacency (GH-8)

**Source:** SN-12 (2026-06-25), Concern SN-12a — binding decision.

**The binding rule:** Each chat level produces artifacts only for its **direct parent** or
**direct children**. No grandchild artifacts (e.g., a Phase Chat must not produce Epic
Execution Chat Starters) and no grandparent artifacts. A violation either bypasses a review
gate (grandchild production) or overreaches a parent's authority (grandparent production).

**Deliverables:**

1. **`governance/templates/phase-execution-chat-starter.md`** and
   **`governance/templates/milestone-execution-chat-starter.md`** — Add the adjacency rule
   to the **Critical Rules** section of each: a chat produces artifacts only for its direct
   parent or direct children; no grandchild/grandparent artifacts.
2. **`governance/AI-OPERATING-GUIDELINES.md`** — Add the corresponding rule to **§3.6**
   (Phase Chat) and **§3.7** (Milestone Chat).
3. **`governance/systems/chat-hierarchy.md`** — Add the adjacency table (Chat → may produce
   / must NOT produce) from SN-12a.

**Definition of Done:**
- [ ] Both the Phase and Milestone Execution Chat Starter templates state the adjacency rule in Critical Rules
- [ ] AOG §3.6 and §3.7 each state the adjacency rule
- [ ] `chat-hierarchy.md` contains the adjacency table
- [ ] Full test suite passes

**Acceptance Criteria:**
- [ ] The adjacency rule is present in both starter templates' Critical Rules
- [ ] AOG §3.6 and §3.7 reference the adjacency requirement
- [ ] `chat-hierarchy.md` has the adjacency table

---

### E20.5 — Hierarchical communication protocol (GH-9)

**Source:** SN-12 (2026-06-25), Concern SN-12b — binding decisions.

**The binding decisions:** Upward communication is 1-to-1, one level at a time (no level
skips its parent). Downward communication is solved by the spec file, not broadcasting — a
parent amends its own spec; children (including those mid-execution) read from it at any
time. The level spec file is dual-role: planning artifact *and* live contract. Mid-flight
updates amend the spec and escalate **up** if blocking; a parent never reaches into running
child sessions it does not control.

**Deliverables:**

1. **`governance/systems/chat-hierarchy.md`** — Add a "Communication Protocol" section
   covering: upward 1-to-1; downward via spec-file amendment; spec-file dual role;
   mid-flight escalate-up / never reach into running sessions.
2. **`governance/AI-OPERATING-GUIDELINES.md` §3** and **`governance/PROJECT-SYSTEM-GUIDELINES.md`**
   — Add the corresponding rules.
3. **`governance/templates/phase-execution-chat-starter.md`** and
   **`governance/templates/milestone-execution-chat-starter.md`** — Add guidance on how to
   issue amendments: amend the spec, note the change, notify the parent chat.

**Definition of Done:**
- [ ] `chat-hierarchy.md` has a "Communication Protocol" section with all four decisions
- [ ] AOG §3 and PSG each state the upward-1to1 / spec-as-channel / mid-flight-escalate-up rules
- [ ] Both starter templates include amendment-issuing guidance
- [ ] Full test suite passes

**Acceptance Criteria:**
- [ ] `chat-hierarchy.md` documents the upward, downward, dual-role, and mid-flight rules
- [ ] AOG §3 and PSG reference the communication protocol
- [ ] Both starter templates explain how to issue a spec amendment

---

## Branch Strategy

```
master
└── phase/P5
    └── milestone/M20             ← this milestone
        ├── epic/P5-M20-E20.1     ← Prerequisite git-tracking verification (GH-1)
        ├── epic/P5-M20-E20.2     ← Working-tree isolation convention (GH-2)
        ├── epic/P5-M20-E20.3     ← Scope direction protocol (GH-3)
        ├── epic/P5-M20-E20.4     ← Artifact scope adjacency (GH-8)
        └── epic/P5-M20-E20.5     ← Hierarchical communication protocol (GH-9)
```

Epic PRs target `milestone/M20`. Consolidation PR: `milestone/M20 → phase/P5`.
Phase closure PR (after all P5 milestones): `phase/P5 → master`.

---

## Prerequisites

- `phase/P5` branch exists from `master` (synced to the v1.1.0 phase spec — 5-epic M20)
- `governance/templates/milestone-execution-chat-starter.md` present and git-tracked
- `governance/templates/epic-execution-chat-starter.md` present and git-tracked
- `governance/templates/phase-execution-chat-starter.md` present and git-tracked
- `governance/systems/chat-hierarchy.md` present and git-tracked
- `governance/AI-OPERATING-GUIDELINES.md` v2.1.0 and `governance/PROJECT-SYSTEM-GUIDELINES.md`
  v3.0.0 present and git-tracked
- `tests/test_starter_lint.py` present (test home reference for E20.1)

> Verify each with `git ls-files --error-unmatch <path>` on `phase/P5` before opening the
> dependent Epic — this milestone hardens exactly that check (E20.1), so it is held to it.

---

## Dependencies and Sequencing

**Internal — shared-file contention is significant; serialize edits to shared files:**

| File | Epics that edit it |
|------|--------------------|
| `governance/systems/chat-hierarchy.md` | E20.2, E20.3, E20.4, E20.5 |
| `governance/AI-OPERATING-GUIDELINES.md` §3 / §3.6 / §3.7 | E20.2, E20.3, E20.4, E20.5 |
| `governance/templates/milestone-execution-chat-starter.md` | E20.1, E20.4, E20.5 |
| `governance/templates/phase-execution-chat-starter.md` | E20.4, E20.5 |
| `governance/templates/epic-execution-chat-starter.md` | E20.1 |

- Recommended execution order: **E20.1 → E20.2 → E20.3 → E20.4 → E20.5**, each rebased on
  the prior merge. Because four of five epics edit `chat-hierarchy.md` and AOG §3, parallel
  execution **requires** per-epic worktrees (the GH-2 fix this milestone delivers) and a
  rebase before each subsequent PR. Prefer sequential.
- E20.1 is the most independent (templates + tests) and can lead.

**External:** None.

---

## Definition of Done (Milestone)

- [ ] E20.1, E20.2, E20.3, E20.4, E20.5 each meet their Definition of Done above
- [ ] All five epic branches merged to `milestone/M20`
- [ ] Full test suite passes on `milestone/M20`
- [ ] Milestone Closure Declaration produced

---

## Acceptance Criteria (Milestone)

1. Both starter templates mandate `git ls-files --error-unmatch <path>` verification, with
   inline rationale, and a passing test asserts it (GH-1).
2. `chat-hierarchy.md` has a "Working-Tree Isolation" section and AOG §3 references it (GH-2).
3. `chat-hierarchy.md` has a "Scope Direction Protocol" section with the HQ-ratified rule
   verbatim, P0 exception, and rationale; AOG §3 references it (GH-3).
4. The adjacency rule is in both starter templates' Critical Rules, in AOG §3.6 and §3.7,
   and as a table in `chat-hierarchy.md` (GH-8).
5. The hierarchical communication protocol is in `chat-hierarchy.md`, AOG §3, and PSG, with
   amendment guidance in both starter templates (GH-9).
6. Full test suite passes.

---

## Timeline

**Target Start:** 2026-06-24
**Target Completion:** 2026-07-01 (5–7 days per Phase spec estimate for 5 epics)
**Actual Start:** Not started
**Actual Completion:** In progress

---

## Notes

- M20 is process hardening, not feature work: every deliverable is a documentation or
  wording change plus (for E20.1) a single guard test. Keep edits surgical and avoid
  restructuring the host documents.
- The GH-3 rule is **ratified and verbatim**; the GH-8/GH-9 decisions come from **SN-12**
  (2026-06-25) and are binding — do not paraphrase, soften, or extend them.
- **Self-referential worked examples (M20 dogfoods its own fixes):** GH-3's escalate-up
  principle was demonstrated by this milestone's own Stage-1 authority-conflict escalation;
  GH-8's adjacency rule was demonstrated by this milestone's own Stage-1 delivery producing
  Epic starters one level too high (retained per HQ Option B, to be re-issued by the
  Milestone Chat). Both are cited above as live examples.
- M20 should be executed under its own conventions: isolated worktrees for any concurrent
  epic work (E20.2), and serialized edits to the shared governance documents.
