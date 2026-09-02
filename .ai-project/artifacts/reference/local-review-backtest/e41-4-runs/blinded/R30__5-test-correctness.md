# Blinded run record — R30

**Packet:** `packet-5-test-correctness.md` | **Attempt:** 2 | **Opaque run ID:** `R30`

**Stop/finish reason:** `stop` | **exit:** 0
**Elapsed (s):** 91.901 | **No tuning applied:** true | **Sampling:** vendor defaults

**Model response (verbatim, unedited):**

````text








**Conclusion:** The test is red because of a false positive in `tests/test_starter_lint.py` — the reference flagged on line 111 is correct and deliberate, not a typo. The defect that should be changed is in the test, not in the starter document.

## Reasons

**1. What the test asserts, and its mechanism.**
`test_no_branch_name_typos_in_starters` scans every `*epic-execution-chat-starter.md`, extracts every `milestone/M<n>` token via `BRANCH_RE = r"milestone/M(\d+)\b"`, and declares a token a typo unless it is either (a) a "known milestone" — derived strictly from starter filenames matching `^P\d+-M(\d+)-E[\d.]+__epic-execution-chat-starter\.md$` — or (b) a "planned" milestone: a number in the narrow window `(highest, highest + 10]`. Here `highest` is M41. `M1` fails both tests: it is *not* a known milestone (no `P1-M1-E*__epic-execution-chat-starter.md` exists — this repo's starter convention only begins at M9, so real milestones M1–M8 are invisible to `known_milestones()`), and `M1` is *below* the frontier, so it can never satisfy the planned-milestone clause (which only admits numbers *above* the highest existing milestone). The guard can therefore only ever accept a below-frontier number if it happens to already be in the starter-derived set.

**2. Is line 111 a mistake?** No. Two independent reasons it is legitimate, both surfaced in `P10-M34__carry-forward-note__P10-GH-6-starter-lint-false-positive.md`:

- The token describes the `footboard` repository's *own* `milestone/M1` branch. P10/E34.2's subject is bumping three *separate* repositories (`Getawayinsured2023`, `footboard`, `courtis`), each with its own governance numbering. A reference to another repository's branch is exactly what this cross-repo adoption epic exists to talk about, and the guard has no notion of a branch name belonging to a different repo.
- M1 is also a *real milestone of this repository* (`P1-M1-E1.1__spec__…` exists), just one that predates the starter-filename convention the detector keys on. So even absent the cross-repo aspect, the ground-truth derivation is incomplete.

The test's failure text ("Fix the milestone number, likely a stray extra digit") points at the wrong remedy: the digit is not stray, and the defect class the guard was built for (stray digits like M14→M144, which land an order of magnitude *past* the frontier) is not present here.

**3. What should be changed, in which file.** The bug lives in `tests/test_starter_lint.py`, not in the document. Two defects in the detector need fixing: (i) `known_milestones()` under-derives ground truth (starter filenames only, blind to M1–M8 and other milestones without a starter file), and (ii) the guard cannot distinguish a foreign repo's branch reference from this repo's `milestone/M<n>`. The durable fixes are: widen the ground truth (derive known milestones from milestone specs/phase directories rather than starter filenames alone), and/or narrow the guard to its actual stated defect class (flag only references implausibly far past the frontier).

Note on current state: my `git log`/`grep` shows the repo has *since* applied a document-level workaround — `P10-M34-E34.2__epic-execution-chat-starter.md` now reads "`footboard` on its own `M1` milestone branch" (with an inline "Wording note … see P10-GH-6"), so `milestone/M1` no longer appears and the suite is currently green. That is a workaround in one file, not a fix: any future cross-repo starter that names a target repo's `milestone/M<n>` below the frontier will fail the same way. The correct permanent change is to the test's detector logic, as recorded (without decision) in the P10-GH-6 carry-forward note.
````
