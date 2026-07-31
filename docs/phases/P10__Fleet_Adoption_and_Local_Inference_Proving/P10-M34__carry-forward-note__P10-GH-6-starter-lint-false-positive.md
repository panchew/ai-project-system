---
project: ai-project-system
phase: P10
milestone: M34
type: note
status: active
issuer_chat: Epic Execution Chat (P10-M34-E34.2)
issued_to: Milestone Chat (P10-M34) → Phase Chat (P10)
last_updated: 2026-07-29
---

# Carry-Forward Note — P10-GH-6: the Epic-starter lint flags real milestones as typos

**Recorded, not fixed.** Changing `tests/test_starter_lint.py` is a framework *capability* change, and
the bump procedure's Failure Mode 4 already establishes that framework-repo changes are **out of scope
for adoption epics**. E34.2 worked around it in its own document and filed this instead.

**Origin:** found during E34.2's Prerequisite Verification. The Epic spec and starter both state the
suite baseline is **366 / 0 / 0**. It was actually **365 passed / 1 failed / 0 skipped** on
`milestone/M34` before any E34.2 work — and the failing test was triggered by E34.2's *own* starter,
committed in `973a7f5`.

---

## The finding

```
E           Failed: Milestone branch-name typo(s) detected in Epic starters:
E             docs/phases/P10__.../P10-M34-E34.2__epic-execution-chat-starter.md:111 -> milestone/M1 (not a known milestone)
E           Fix the milestone number (likely a stray extra digit).
```

The flagged reference is **not a typo**, and `milestone/M1` is **not a fake milestone**. Two
independent reasons the guard is wrong here:

1. **M1 is a real milestone of this repo.** `docs/phases/P1__.../P1-M1-E1.1__spec__project-tracker-integration-system.md`
   and its completion record both exist. But `known_milestones()` derives the set of real milestones
   **exclusively from Epic-starter filenames** matching
   `^P\d+-M(\d+)-E[\d.]+__epic-execution-chat-starter\.md$`. This repo has no M1 *starter* file, so
   **every milestone that predates the starter naming convention is invisible to the guard.** The
   lowest milestone it can see is M9; M1–M8 are all unrepresentable.
2. **The reference was to another repository's branch.** Line 111 described `footboard` sitting on its
   own `milestone/M1` branch — a target-repo fact, which is exactly the subject matter of a
   cross-repo adoption epic. The guard has no notion of a branch name belonging to a different repo.

The guard's own docstring scopes it to a specific defect class: a **stray extra digit** (`M14` →
`M144`, `M17` → `M147`), which always lands an order of magnitude past the milestone frontier. A
reference to a small, real, *below-frontier* number is not that class, and the acceptance logic
(`highest < int(num) <= highest + 10`) only ever admits numbers **above** the frontier — so a
below-frontier unknown can never pass.

## Why it matters beyond one line of Markdown

- **It misreports the baseline.** M34's epic specs state a 366/0/0 baseline that has been false since
  `973a7f5`. Any epic that trusts a stated baseline instead of measuring it will either report a green
  suite it never saw, or attribute a pre-existing red to its own work. E34.2 measured, which is the
  only reason it was caught.
- **It penalizes cross-repo epics specifically.** P10 is a *fleet adoption* phase: its epics exist to
  talk about other repositories' branches. A guard that treats another repo's branch name as a typo in
  this repo will keep firing for as long as the phase's subject matter is the fleet.
- **The fix is not obviously "loosen it".** Simply accepting all below-frontier numbers would blunt the
  guard for genuine mistakes. The interesting question is whether the ground truth should come from
  something better than starter filenames — `docs/phases/*/` directory contents, milestone specs, or
  an explicit registry — which is a design call above this level.

## Candidate directions (not decided here)

1. **Widen the ground truth.** Derive known milestones from milestone specs or phase directories, not
   starter filenames alone. Fixes reason 1 and needs no new convention; does nothing for reason 2.
2. **Teach the guard about cross-repo references** — e.g. skip a match when the line also names a
   known fleet project, or honor an explicit inline marker. Fixes reason 2; adds a convention.
3. **Narrow the guard to its stated defect class.** Flag only references implausibly far past the
   frontier (which is all the docstring ever claimed to catch). Simplest, and it keeps the teeth for
   stray-digit typos; accepts that a wrong-but-plausible milestone number goes uncaught.
4. **Leave it and document the workaround.** Cheapest, but the trap re-arms for the next cross-repo
   epic, and the false baseline in the specs stays wrong.

**No recommendation from this level** — this is a framework capability judgment, and option 1 vs 3 is a
question about what the guard is *for*, which belongs to whoever owns the test.

## What E34.2 did instead

Reworded its own starter so the sentence no longer emits the literal `milestone/M<n>` token —
`footboard`'s branch is now described as "its own `M1` milestone branch", with an inline note pointing
here. **The branch in `footboard` is unchanged; only the phrasing in this repo is.** No test, no spec,
and no other starter was touched. Suite afterwards: **366 passed, 0 failed, 0 skipped.**

This is a workaround in one document, not a fix — the next Epic starter that needs to name a target
repo's milestone branch will hit the same wall.

## Explicitly not done here

- `tests/test_starter_lint.py` **not modified** — no loosened regex, no new allowlist, no changed
  lookahead.
- The stale 366/0/0 baseline claims in the E34.2 spec/starter and the M34 milestone spec are **not**
  rewritten; the true measured baseline is recorded in
  `P10-M34-E34.2__confirmation-evidence.md` instead.
- No other starter was audited for the same latent trigger. Any starter referencing `milestone/M1`
  through `milestone/M8` would fail the same way; **only E34.2's was in the failing set**, so no
  sweep was performed.
- No renumbering of P10-GH-1 (`framework_version` unschema'd), P10-GH-2 (Creation Seed lacks E31.3
  verification), P10-GH-3 (policy row P1 vs live config), P10-GH-4 (`delivery_notice.merge_details`
  unfillable), or P10-GH-5 (yml validation rules unenforced). This is **P10-GH-6**.
