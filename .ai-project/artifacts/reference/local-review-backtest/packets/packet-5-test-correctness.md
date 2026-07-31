<!-- ===================================================================== -->
<!-- AUDIT HEADER — read by humans, NEVER sent to the model.               -->
<!-- The prompt is EXACTLY the bytes after the PROMPT-BEGIN marker line.   -->
<!-- ===================================================================== -->

# Packet 5 — test-correctness judgment (ground truth: THE TEST IS WRONG, not the document)

**Defect (E35.5 spec, row 5):** `tests/test_starter_lint.py` flagged a **real** milestone reference as
a typo. The guard derives its set of known milestones exclusively from Epic-starter filenames, so every
milestone predating that naming convention (M1–M8 in this repo) is invisible to it; and the flagged
line referred to **another repository's** branch, which the guard has no notion of. Filed as
**P10-GH-6**, recorded not fixed.

**Provenance — verbatim from committed state on `milestone/M35`:**

- Section 1 is the pytest failure text as recorded at the time of the finding.
- Section 2 is `tests/test_starter_lint.py` at `f4c3a30` — unchanged since, and unchanged by the
  finding (the file was deliberately not modified).
- Section 3 is `git show 973a7f5:docs/phases/P10__.../P10-M34-E34.2__epic-execution-chat-starter.md`,
  the flagged revision, lines 104–115.
- Section 4 is a plain `ls` of the repository's phase directories.

**Excised (blinding record) — none of the following appears below:**

- `docs/phases/P10__.../P10-M34__carry-forward-note__P10-GH-6-starter-lint-false-positive.md` — the
  entire finding, both reasons, and four candidate fixes.
- `P10-M34-E34.2__confirmation-evidence.md` Check 3, which states the same finding.
- The reworded (post-workaround) starter text, and the M34 Closure Declaration.
- The gap identifier `P10-GH-6` itself.

<!-- PROMPT-BEGIN -->
You are performing a **Stage-2 review** under the AI Project System governance framework. The test
suite of the governance repository is **red**. Your job is to determine the cause and state what
should be done about it.

---

## 1. The failure

```
FAILED tests/test_starter_lint.py::test_no_branch_name_typos_in_starters

E           Failed: Milestone branch-name typo(s) detected in Epic starters:
E             docs/phases/P10__Fleet_Adoption_and_Local_Inference_Proving/P10-M34-E34.2__epic-execution-chat-starter.md:111 -> milestone/M1 (not a known milestone)
E           Fix the milestone number (likely a stray extra digit).

365 passed, 1 failed, 0 skipped
```

---

## 2. The test that failed, in full

```python
"""Lint check for milestone branch-name typos in Epic Execution Chat Starters.

Epic P4-M17-E17.2 — Update Starters and Documentation (req 9).

Background
----------
Across M15 and M17 a recurring copy-paste typo appeared in Epic starters: a
milestone branch reference gained an extra digit, e.g. ``milestone/M14`` became
``milestone/M144`` and ``milestone/M17`` became ``milestone/M147``. Followed
literally, such a starter sends a PR to a branch that does not exist.

This check scans every ``*epic-execution-chat-starter.md`` under ``docs/`` and
flags any ``milestone/M<n>`` reference whose number is **not a real milestone**
in this project. The set of real milestones is derived from the starter
filenames themselves (``P#-M#-E#.#__epic-execution-chat-starter.md``), so the
check needs no hand-maintained list.

Why "not a real milestone" rather than "must equal the file's own milestone":
some starters legitimately reference a *sibling* milestone branch — E15.2
cherry-picks from ``origin/milestone/M14`` and E16.1 branches ``milestone/M16``
from ``origin/milestone/M15``. Those are valid cross-references. A typo like
``M144`` is not a real milestone at all, which is exactly what distinguishes a
mistake from a legitimate reference.

Planned milestones are also accepted: a reference just beyond the highest
existing milestone — within ``PLANNED_MILESTONE_LOOKAHEAD`` — is treated as a
legitimately-planned future milestone, not a typo. This lets a starter reference
the next milestone (e.g., the M20 starter's ``milestone/M21`` worktree example)
before its starter file exists. A stray-digit typo lands an order of magnitude
past the frontier (M14 -> M144), well outside the window, so it is still caught.

If this test fails: open the named starter, find the flagged ``milestone/M<n>``
reference, and correct it to the intended milestone (almost always the same
number with the stray digit removed). See the Troubleshooting Guide entry
"An Epic starter references the wrong milestone branch".
"""

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_ROOT = REPO_ROOT / "docs"
STARTER_GLOB = "**/*epic-execution-chat-starter.md"

# milestone/M<number>  (word boundary so M14 and M144 are distinct tokens)
BRANCH_RE = re.compile(r"milestone/M(\d+)\b")
# P<phase>-M<milestone>-E<epic> prefix in a starter filename
FILENAME_RE = re.compile(r"^P\d+-M(\d+)-E[\d.]+__epic-execution-chat-starter\.md$")

# How far past the highest existing milestone a reference may point and still be
# treated as a *planned* milestone rather than a typo. Milestones are planned a
# few at a time (the M20 spec already names M21 and M22), so a reference a short
# distance beyond the frontier is legitimate even before its starter file exists.
# The stray-digit typo this check guards against lands an order of magnitude away
# (M14 -> M144, M17 -> M147) — far outside any real planning horizon — so a small
# window admits genuine near-future milestones while still flagging the typo class.
PLANNED_MILESTONE_LOOKAHEAD = 10


def find_starter_files(docs_root: Path = DOCS_ROOT):
    """All Epic Execution Chat Starter files under ``docs_root``."""
    return sorted(docs_root.glob(STARTER_GLOB))


def known_milestones(files):
    """Set of milestone numbers (as strings) that real starters declare in their names."""
    found = set()
    for f in files:
        m = FILENAME_RE.match(f.name)
        if m:
            found.add(m.group(1))
    return found


def find_branch_typos(docs_root: Path = DOCS_ROOT):
    """Return a list of (file, line_no, milestone_number) for typo'd branch refs.

    A reference is a typo when its milestone number is neither a known milestone
    (derived from starter filenames) nor a plausibly-planned one. A planned
    milestone is a number just beyond the highest existing milestone — within
    ``PLANNED_MILESTONE_LOOKAHEAD`` — which the project may reference before its
    starter file exists (e.g., the M20 starter's ``milestone/M21`` worktree
    example). Stray-digit typos land far past the frontier and are still flagged.
    """
    files = find_starter_files(docs_root)
    valid = known_milestones(files)
    # The highest existing milestone defines the frontier; references a short
    # distance past it are planned milestones, not typos (see constant above).
    highest = max((int(n) for n in valid), default=0)
    violations = []
    for f in files:
        for line_no, line in enumerate(f.read_text().splitlines(), start=1):
            for num in BRANCH_RE.findall(line):
                if num in valid:
                    continue
                # Accept a plausibly-planned milestone: just beyond the frontier
                # and within the lookahead window. Everything else is a typo.
                if highest < int(num) <= highest + PLANNED_MILESTONE_LOOKAHEAD:
                    continue
                violations.append((f, line_no, num))
    return violations


# ---------------------------------------------------------------------------
# Repository guard: the real starters must be clean.
# ---------------------------------------------------------------------------

def test_starter_files_are_discovered():
    """Sanity: the glob actually finds the starters (guards against a path slip)."""
    files = find_starter_files()
    assert files, "No epic-execution-chat-starter.md files found under docs/"


def test_known_milestones_non_empty():
    valid = known_milestones(find_starter_files())
    assert valid, "Could not derive any milestone numbers from starter filenames"


def test_no_branch_name_typos_in_starters():
    """No starter may reference a milestone branch that is not a real milestone."""
    violations = find_branch_typos()
    if violations:
        detail = "\n".join(
            f"  {f.relative_to(REPO_ROOT)}:{ln} -> milestone/M{num} "
            f"(not a known milestone)"
            for f, ln, num in violations
        )
        pytest.fail(
            "Milestone branch-name typo(s) detected in Epic starters:\n"
            + detail
            + "\nFix the milestone number (likely a stray extra digit)."
        )


# ---------------------------------------------------------------------------
# Detector behaviour: synthetic fixtures (so the guard cannot silently rot).
# ---------------------------------------------------------------------------

def _write_starter(root: Path, name: str, body: str) -> Path:
    docs = root / "docs" / "phases" / "PX"
    docs.mkdir(parents=True, exist_ok=True)
    p = docs / name
    p.write_text(body)
    return p


def test_detector_flags_extra_digit_typo(tmp_path):
    """An M17 starter referencing milestone/M147 is flagged."""
    _write_starter(
        tmp_path,
        "P4-M17-E17.9__epic-execution-chat-starter.md",
        "Pull request: `epic/E17.9` -> `milestone/M147`\n",
    )
    violations = find_branch_typos(tmp_path / "docs")
    assert len(violations) == 1
    assert violations[0][2] == "147"


def test_detector_flags_m144_regression(tmp_path):
    """The exact historical typo (M14 -> M144) is caught."""
    # A real milestone (M14) plus a sibling so M14 is "known".
    _write_starter(tmp_path, "P4-M14-E14.1__epic-execution-chat-starter.md",
                   "Target: `milestone/M14`\n")
    bad = _write_starter(tmp_path, "P4-M14-E14.2__epic-execution-chat-starter.md",
                         "Pull request -> `milestone/M144`\n")
    violations = find_branch_typos(tmp_path / "docs")
    assert [(f.name, num) for f, _, num in violations] == [(bad.name, "144")]


def test_detector_allows_legitimate_cross_reference(tmp_path):
    """A starter may reference a sibling milestone branch that really exists."""
    # M14 and M15 both exist (both have starter files); E15.2 references M14.
    _write_starter(tmp_path, "P4-M14-E14.1__epic-execution-chat-starter.md",
                   "Target: `milestone/M14`\n")
    _write_starter(
        tmp_path,
        "P4-M15-E15.2__epic-execution-chat-starter.md",
        "Cherry-pick commits from `origin/milestone/M14` onto `milestone/M15`.\n",
    )
    assert find_branch_typos(tmp_path / "docs") == []


def test_detector_allows_own_milestone(tmp_path):
    _write_starter(tmp_path, "P4-M16-E16.1__epic-execution-chat-starter.md",
                   "PR: `epic/E16.1` -> `milestone/M16`\n")
    assert find_branch_typos(tmp_path / "docs") == []


def test_detector_allows_planned_milestone_within_lookahead(tmp_path):
    """A reference to a not-yet-created but plausibly-planned milestone is allowed.

    The M20 starter's worktree example uses ``milestone/M21`` before any M21
    starter exists. M21 is one past the frontier (M20), well within the planning
    lookahead, so it is accepted — unlike the stray-digit typos above.
    """
    _write_starter(
        tmp_path,
        "P5-M20-E20.2__epic-execution-chat-starter.md",
        "Worked example: `git worktree add ../wt-m21 milestone/M21`\n",
    )
    assert find_branch_typos(tmp_path / "docs") == []


def test_detector_flags_far_future_typo_beyond_lookahead(tmp_path):
    """A number far past the frontier is a typo even though it is 'beyond' it.

    Guards the boundary: being greater than the highest milestone is not enough;
    it must be within the lookahead. M99 against an M20 frontier is a stray-digit
    style typo, not a planned milestone.
    """
    _write_starter(tmp_path, "P5-M20-E20.9__epic-execution-chat-starter.md",
                   "Pull request -> `milestone/M99`\n")
    violations = find_branch_typos(tmp_path / "docs")
    assert [(f.name, num) for f, _, num in violations] == [
        ("P5-M20-E20.9__epic-execution-chat-starter.md", "99")
    ]
```

---

## 3. The flagged document

`docs/phases/P10__Fleet_Adoption_and_Local_Inference_Proving/P10-M34-E34.2__epic-execution-chat-starter.md`,
lines 104–115. Line 111 is the one the test flags.

```markdown

### Your Responsibilities (Coding Agent)

1. **Create branch** `epic/P10-M34-E34.2` from `milestone/M34` (in **this** repo).
2. **Run Prerequisite Verification**; record every result including all three pre-states.
3. **Decide and document the branch base** for each target (spec Judgment call 1). Two projects sit
   on non-default branches mid-governance-work — `Getawayinsured2023` on `phase/P1`, `footboard` on
   `milestone/M1`. Recommendation is to branch from the default branch so the bump is independently
   publishable. **State your choice and reasoning per project.**
4. **`Getawayinsured2023` — stamp only.** Its submodule is already at v7.0.0 and its agent sha is
   already canonical. **Re-run the FM3 agent-freshness check and record that it passed** (it is the
   only fleet project where FM3 does not bite — that is worth recording, not skipping). Add
```

Context for reading that passage: this epic's subject matter is bumping **three other repositories**
to a new framework version. `Getawayinsured2023`, `footboard` and `courtis` are separate git
repositories, each with its own branches and its own governance numbering.

---

## 4. Repository state

Phase directories present in `docs/phases/` of this repository:

```
$ ls docs/phases/
P0-M0.1-E0.1.1__completion__retired.md
P0-M0.1-E0.1.1__epic__formalize-system-repository.md
P0-M0.1__milestone__repository-bootstrap.md
P0__phase__project-formalization.md
P10__Fleet_Adoption_and_Local_Inference_Proving
P1__System_Foundation_and_Adoption
P1__phase.md
P2__Adoption_Architecture_and_Multi_Project_Support
P3__Agentic_Execution_Model_Maturity
P4__Team_Collaboration_and_Artifact_Driven_Communication
P5__Process_Hardening_and_Visual_Artifacts
P6__Visual_Comprehension_Layer_and_Process_Refinements
P7__Agentic_Execution_and_Default_On_Visuals
P8__Visual_Artifacts_Activation
P9__Context_Handling_and_Token_Efficiency

$ ls docs/phases/P1__System_Foundation_and_Adoption/
P1-M1-E1.1__completion__project-tracker-integration-system.md
P1-M1-E1.1__spec__project-tracker-integration-system.md
P1-M1__completion__genesis-and-integration-baseline.md
P1-M1__milestone.md
P1-M2-E2.1__completion__human-review-and-acceptance.md
P1-M2-E2.1__spec__human-review-and-acceptance.md
P1-M2-E2.2__completion__human-language-review-capture-and-structured-artifact-generation.md
P1-M2-E2.2__spec__human-language-review-capture-and-structured-artifact-generation.md
P1-M2-E2.3__completion__happy-path-enforcement-and-end-to-end-closure-validation.md
P1-M2-E2.3__spec__happy-path-enforcement-and-end-to-end-closure-validation.md
P1-M2__milestone.md
P1-M3-E3.1__completion-notice.md
P1-M3-E3.1__completion__governance-propagation-and-authority-declaration.md
P1-M3-E3.1__spec__governance-propagation-and-authority-declaration.md
P1-M3__milestone.md
P1-M4-E4.1__completion__templates-and-scaffolding.md
P1-M4-E4.1__delivery-notice.md
P1-M4-E4.1__spec__templates-and-scaffolding.md
P1-M5-E5.1__completion__unplanned-progress-branch-model.md
P1-M5-E5.1__spec__unplanned-progress-branch-model.md
P1-M5__milestone.md
(further P1-M4 / P1-M5 entries omitted for length; no other file types present)
```

---

## 5. Your task

State your conclusion on its own line, then give your reasons.

Address, in your reasons:

1. What exactly the test is asserting, and by what mechanism it decides a reference is a typo.
2. Whether the flagged reference on line 111 is in fact a mistake.
3. What should be changed, and why — be specific about which file you would change.
