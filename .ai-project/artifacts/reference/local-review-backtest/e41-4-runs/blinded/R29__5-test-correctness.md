# Blinded run record — R29

**Packet:** `packet-5-test-correctness.md` | **Attempt:** 1 | **Opaque run ID:** `R29`

**Stop/finish reason:** `stop` | **exit:** 0
**Elapsed (s):** 54.855 | **No tuning applied:** true | **Sampling:** vendor defaults

**Model response (verbatim, unedited):**

````text






The flagged reference is **not** a mistake — it is a false positive. The starter should be reworded (drop the literal `milestone/M<n>` token), not "corrected" to a different milestone.

## Reasons

**1. What the test asserts, and its mechanism**

`test_no_branch_name_typos_in_starters` scans every `*epic-execution-chat-starter.md` for the token `milestone/M(\d+)`. It builds the set of "known" milestones *only* from the starter filenames themselves (`P#-M(n)-E#.#__epic-execution-chat-starter.md` via `known_milestones()`). A reference is declared a typo when its number is (a) not in that filename-derived set and (b) not within `PLANNED_MILESTONE_LOOKAHEAD` (10) *above* the highest filename-derived milestone. It is deliberately lenient for sibling/planned milestones, but it has one assumption baked in: **every `milestone/M<n>` token names a branch in this governance repo**.

**2. Why the flagged reference isn't a mistake**

Line 111's `milestone/M1` names **`footboard`'s** branch — a separate git repository with its *own* milestone numbering that starts at M1. This repo's `M1` (P1-M1) exists in the directory listing but has no `*epic-execution-chat-starter.md`, so it is invisible to `known_milestones()`; and `M1` is far below the `M34` frontier, so the lookahead exemption can't save it. Two independent defects (filename-only milestone discovery, and no cross-repo awareness) both fire, but the authored text is correct: footboard's branch genuinely is called `M1` in footboard.

**3. What should change**

Change the **starter** (`docs/phases/P10__.../P10-M34-E34.2__epic-execution-chat-starter.md`, the sentence spanning lines 109–111), rewording `footboard`'s branch so it no longer carries the literal `milestone/M<n>` token — e.g. "its own `M1` milestone branch" — since that token is this repo's numbering convention and collides with the lint. The milestone number itself must **not** be edited; there is no stray digit. The test is a framework-capability limitation (it cannot distinguish this repo's branches from a cross-repo target's), which the governance record already tracks as **P10-GH-6** (see `P10__phase-closure-declaration.md:204` and `P10-M35-E35.5__spec__...`), rather than "fixing" the fragile detector inside an adoption epic.
````
