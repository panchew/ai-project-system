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
is_final: false
---

# Milestone M20 — Governance Process Hardening

## Purpose

Eliminate the three governance process gaps (GH-1, GH-2, GH-3) that surfaced during
P4 execution and that will recur — with increasing cost — as concurrent chat usage
grows. M20 is the highest-priority milestone of Phase P5: it hardens the execution
process itself before any further feature work (M21 adoption clarity, M22 visual
artifacts) is layered on top.

This milestone ensures:
- Prerequisite verification proves an artifact is **git-tracked**, not merely present
  on a working-tree disk (GH-1)
- Concurrently-active chats have a **documented working-tree isolation convention**,
  not tribal knowledge (GH-2)
- Scope direction to in-flight Epics always flows through a **mandatory, auditable
  channel** (GH-3)

---

## Problem Statement

P4 execution surfaced three latent process defects, each captured in the M19 Escalation
Notice and each independently capable of producing silent, hard-to-detect failures:

1. **False-green prerequisites (GH-1).** A prerequisite artifact was declared
   "✅ committed" in a spec but was untracked in git. The Stage 1 check verified file
   existence on disk only. A fresh worktree clone would have lacked the artifact
   entirely, and the dependent chat would have proceeded on a false premise.

2. **Shared working tree (GH-2).** A Milestone Chat and an Epic Chat shared one working
   tree. While the Milestone Chat had an in-flight commit, the Epic Chat checked out a
   new branch — and the Milestone Chat's subsequent commit landed on the wrong branch
   silently.

3. **Unrouted scope direction (GH-3).** Scope direction from the Creation Chat / CFO to
   an in-flight Epic had no documented mandatory channel, allowing scope to change
   without an audit trail or a spec amendment.

Each gap is cheap to close as a documentation/wording change now, and expensive to
absorb repeatedly once multiple chats run in parallel as a matter of course.

---

## Goals

By the end of this milestone, the system must:

1. Mandate `git ls-files --error-unmatch <path>` verification on the expected branch as
   the prerequisite check in both the Milestone and Epic Execution Chat Starter templates,
   with a one-sentence inline rationale and test coverage asserting the wording is present.
2. Document a "Working-Tree Isolation" convention in `chat-hierarchy.md` and reference it
   from AOG §3 (Chat Rules): one `git worktree` per concurrently-active chat.
3. Document a "Scope Direction Protocol" in `chat-hierarchy.md` (the HQ-ratified rule,
   verbatim) and reference it from AOG §3, including the P0-emergency exception.

---

## Non-Goals

This milestone explicitly does **not** aim to:

- Build automation, hooks, or CI checks that *enforce* worktree isolation or scope
  routing at runtime (M20 hardens the documented process; tooling is out of scope)
- Re-litigate or modify the HQ-ratified GH-3 rule wording (it is documented verbatim)
- Touch adoption documentation (M21) or visual artifacts (M22)
- Retro-amend already-closed P4 specs or notices

---

## In Scope

- Wording amendments to `governance/templates/milestone-execution-chat-starter.md` and
  `governance/templates/epic-execution-chat-starter.md` (E20.1)
- New "Working-Tree Isolation" section in `governance/systems/chat-hierarchy.md` (E20.2)
- New "Scope Direction Protocol" section in `governance/systems/chat-hierarchy.md` (E20.3)
- Corresponding rule references in `governance/AI-OPERATING-GUIDELINES.md` §3 (E20.2, E20.3)
- Test coverage asserting the amended template wording (E20.1)

## Out of Scope

- Runtime enforcement tooling
- Changes to PSG (the rules live in AOG + chat-hierarchy.md)
- Any M21 / M22 deliverable

---

## Planned Epics

### Confirmed Epics

- **E20.1 — Prerequisite git-tracking verification** (GH-1) — Replace disk-existence
  prerequisite language with `git ls-files --error-unmatch <path>` verification in both
  starter templates; add inline rationale; add test coverage.
- **E20.2 — Working-tree isolation convention** (GH-2) — Add "Working-Tree Isolation"
  section to `chat-hierarchy.md` and a corresponding rule reference to AOG §3.
- **E20.3 — Scope direction protocol** (GH-3) — Add "Scope Direction Protocol" section
  (HQ-ratified rule verbatim) to `chat-hierarchy.md` and a corresponding rule reference
  to AOG §3.

> Note: This Phase Chat produces the Milestone spec and the three Epic Execution Chat
> Starters directly (per the P5 Phase Execution Chat Starter). The Milestone spec below
> carries the full per-Epic Deliverables / Definition of Done / Acceptance Criteria; the
> Epic Starters reproduce their slice as the binding execution contract. No separate Epic
> spec files are produced at this stage.

### Deferred Epics

- None.

---

## Epic Detail

### E20.1 — Prerequisite git-tracking verification (GH-1)

**Source:** M19 Escalation Notice, Gap 1.

**Deliverables:**

1. **`governance/templates/milestone-execution-chat-starter.md`** — Amend the prerequisite
   verification language (the "Spec Existence Requirement" section, which today tests
   disk presence: *"The Milestone spec MUST exist at the path specified above…"*) so it
   requires the prerequisite/spec to be **git-tracked on the expected branch**, verified
   with `git ls-files --error-unmatch <path>`. Replace any "exists on disk / file is
   present" notion with the git-tracking check.
2. **`governance/templates/epic-execution-chat-starter.md`** — Add an equivalent
   prerequisite git-tracking verification instruction (alongside the Epic Spec reference /
   `Commit:` line) requiring `git ls-files --error-unmatch <path>` on the expected branch
   for the spec and any declared prerequisite artifacts.
3. **Inline rationale (both templates)** — one sentence explaining *why* (e.g., "Disk
   presence is not proof of commit: an untracked file passes a file-exists check but is
   absent from a fresh worktree clone, producing a false-green prerequisite.").
4. **Test coverage** — a test (new module `tests/test_template_prerequisite_wording.py`,
   or an addition to `tests/test_starter_lint.py`) asserting the literal string
   `git ls-files --error-unmatch` is present in **both** template files.

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

1. **`governance/systems/chat-hierarchy.md`** — Add a "Working-Tree Isolation" section
   containing:
   - **Rule:** one `git worktree` per concurrently-active chat; a chat never operates in
     a tree that another concurrent chat may switch.
   - **Practical guidance:** `git worktree add ../worktree-<role>-<id> <branch>`, with a
     concrete example (e.g., `git worktree add ../worktree-milestone-M21 milestone/M21`).
   - **Scope:** applies whenever two or more chats are active simultaneously.
2. **`governance/AI-OPERATING-GUIDELINES.md` §3 (Chat Rules)** — Add a corresponding rule
   that states the isolation requirement and cross-references the chat-hierarchy.md
   section.

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

**Deliverables:**

1. **`governance/systems/chat-hierarchy.md`** — Add a "Scope Direction Protocol" section
   containing the rule above **verbatim**, the P0 exception, and a one-paragraph
   explanation of why the channel matters (audit trail, ambiguity prevention).
2. **`governance/AI-OPERATING-GUIDELINES.md` §3 (Chat Rules)** — Add a corresponding rule
   that states the routing requirement and cross-references the chat-hierarchy.md section.

**Definition of Done:**
- [ ] `chat-hierarchy.md` has a "Scope Direction Protocol" section with the ratified rule verbatim, the P0 exception, and the rationale paragraph
- [ ] AOG §3 references the routing requirement and links to the chat-hierarchy.md section
- [ ] Full test suite passes

**Acceptance Criteria:**
- [ ] `chat-hierarchy.md` has a "Scope Direction Protocol" section with the ratified rule
- [ ] AOG §3 references the routing requirement

---

## Branch Strategy

```
master
└── phase/P5
    └── milestone/M20             ← this milestone
        ├── epic/P5-M20-E20.1     ← Prerequisite git-tracking verification
        ├── epic/P5-M20-E20.2     ← Working-tree isolation convention
        └── epic/P5-M20-E20.3     ← Scope direction protocol
```

Epic PRs target `milestone/M20`. Consolidation PR: `milestone/M20 → phase/P5`.
Phase closure PR (after all P5 milestones): `phase/P5 → master`.

---

## Prerequisites

- `phase/P5` branch exists from `master`
- `governance/templates/milestone-execution-chat-starter.md` present and git-tracked
- `governance/templates/epic-execution-chat-starter.md` present and git-tracked
- `governance/systems/chat-hierarchy.md` present and git-tracked
- `governance/AI-OPERATING-GUIDELINES.md` v2.1.0 present and git-tracked
- `tests/test_starter_lint.py` present (test home reference for E20.1)

> Verify each with `git ls-files --error-unmatch <path>` on `phase/P5` before opening the
> dependent Epic — this milestone hardens exactly that check (E20.1), so it is held to it.

---

## Dependencies and Sequencing

**Internal:**
- E20.1 is **independent** (touches templates + tests only) and may run in parallel.
- **E20.2 and E20.3 both edit the same two files** (`chat-hierarchy.md` and
  `AI-OPERATING-GUIDELINES.md` §3). To avoid merge conflicts they should be executed
  **sequentially** — E20.2 first, then E20.3 rebased on the merged result — or, if run
  concurrently, in **separate worktrees** with a rebase before the second PR. (This
  milestone is itself the GH-2 fix; M20 should dogfood it.)

**External:** None.

---

## Definition of Done (Milestone)

- [ ] E20.1, E20.2, E20.3 each meet their Definition of Done above
- [ ] All three epic branches merged to `milestone/M20`
- [ ] Full test suite passes on `milestone/M20`
- [ ] Milestone Closure Declaration produced

---

## Acceptance Criteria (Milestone)

1. Both starter templates mandate `git ls-files --error-unmatch <path>` verification on
   the expected branch, with inline rationale, and a passing test asserts it.
2. `chat-hierarchy.md` contains a "Working-Tree Isolation" section (rule + worked example)
   and AOG §3 references it.
3. `chat-hierarchy.md` contains a "Scope Direction Protocol" section with the HQ-ratified
   rule verbatim, the P0 exception, and rationale; AOG §3 references it.
4. Full test suite passes.

---

## Timeline

**Target Start:** 2026-06-24
**Target Completion:** 2026-06-29 (3–5 days per Phase spec estimate)
**Actual Start:** Not started
**Actual Completion:** In progress

---

## Notes

- M20 is process hardening, not feature work: every deliverable is a documentation or
  wording change plus a single guard test. Keep edits surgical and avoid restructuring
  the host documents.
- The GH-3 rule is **ratified and verbatim** — do not paraphrase, soften, or extend it.
- M20 should be executed under its own convention: use isolated worktrees for any
  concurrent epic work (E20.2 / E20.3).
