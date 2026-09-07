# Blinded run record — R09

**Packet:** `packet-5-test-correctness.md` | **Attempt:** 1 | **Opaque run ID:** `R09`

**Stop/finish reason:** `stop` | **exit:** 0
**Elapsed (s):** 85.393 | **No tuning applied:** true | **Sampling:** vendor defaults

**Model response (verbatim, unedited):**

````text
**Conclusion: the test is defective, not the document. `milestone/M1` on line 111 is correct and must not be changed; fix `tests/test_starter_lint.py` by widening how it derives the set of real milestones.**

---

### 1. What the test asserts, and its decision mechanism

It asserts that every `milestone/M<n>` token appearing in any `**/*epic-execution-chat-starter.md` under `docs/` names a real milestone. Its ground truth is built in `known_milestones()`: it takes the *filenames* of the starter files it just globbed and extracts `M(\d+)` via `^P\d+-M(\d+)-E[\d.]+__epic-execution-chat-starter\.md$`. A reference passes if either:

- its number is in that filename-derived set, or
- `highest < int(num) <= highest + 10`, where `highest` is the max of that same set.

That is the whole mechanism, and both branches inherit the same flaw: **the only evidence a milestone exists is that someone wrote an Epic starter file for it.** In this repo that set is `{9, 10, 14…41}`. M1–M8 and M11–M13 are structurally unrepresentable — they predate or skip the starter naming convention. The lookahead does not rescue them either, since it admits only numbers *above* the frontier (41). A real, below-frontier milestone with no starter file can therefore never pass. That is not a tuning problem; it is the ground-truth source being wrong.

Note also the docstring's own scoping: the defect class is a *stray extra digit* (`M14`→`M144`, `M17`→`M147`), which by construction lands an order of magnitude past the frontier. `M1` is not that class. The implementation is far broader than the contract it documents.

### 2. Is line 111 a mistake?

No, on two independent grounds — either alone is sufficient.

- **M1 is a real milestone of this repository.** `docs/phases/P1__System_Foundation_and_Adoption/` contains `P1-M1__milestone.md`, `P1-M1-E1.1__spec__…`, and `P1-M1__completion__…`. The test simply cannot see it.
- **The reference isn't to this repository at all.** E34.2 is a fleet-adoption epic about bumping `Getawayinsured2023`, `footboard` and `courtis`. Line 111 records a fact about *footboard's* checkout state. The guard has no notion of repo scope, so it reads another project's branch name as a claim about this one. This blind spot is structural for P10: a phase whose subject matter is other repositories' branches will keep tripping a guard that assumes every branch token is local.

The suggested remedy in the failure message — "likely a stray extra digit," implying `M1` → some longer number — would corrupt a true statement about a third-party repo. Following it would be worse than the red suite.

### 3. What to change

**Change `tests/test_starter_lint.py`.** Replace `FILENAME_RE` / `known_milestones()` so the milestone set is derived from *all* governance documents in `docs/phases/*/`, not starter filenames alone — i.e. match the `P\d+-M([\d.]+)` prefix on any file in a phase directory. I verified this yields M1–M45 contiguously, so it fixes the under-approximation at the root without a hand-maintained allowlist (preserving the property the docstring is proud of). Every existing synthetic fixture in the file still passes under that change, since each writes its files into a phase directory; `test_detector_flags_far_future_typo_beyond_lookahead` and both stray-digit regressions keep their teeth, because M99/M144/M147 remain absent from any filename.

Two things I would **not** do:

- **Do not edit the starter.** The repo currently carries the E34.2 workaround — line 111 was reworded to "its own `M1` milestone branch" purely to avoid emitting the literal token, with an inline note pointing at carry-forward note P10-GH-6. That turned the suite green but is the wrong shape of fix: it makes governance prose self-censor to placate a broken lint, and the trap re-arms for the next cross-repo epic. P10-GH-6 says as much explicitly and declines to recommend. I am recommending: option 1 in that note (widen the ground truth), and the workaround should be reverted once the test is fixed so the sentence reads naturally again.
- **Do not simply accept all below-frontier numbers.** That would blunt the guard against a plausible-but-wrong milestone reference. The problem is the *source* of truth, not the strictness.

Two residual items worth recording separately, neither blocking:

- The cross-repo blind spot (reason 2) survives this fix — it passes here only because footboard's M1 coincides with a valid local M1. A reference to a fleet project's `milestone/M50` would still fire falsely. Worth a follow-up, not worth inventing a marker convention today.
- The M34 epic specs and starter state a **366/0/0** baseline that has been false since `973a7f5`. A stale asserted baseline is the more dangerous defect here: it invites an epic to either claim a green suite it never observed or blame a pre-existing red on its own work. E34.2 caught this only because it measured rather than trusted. Those baseline claims should be corrected, and "measure, don't cite" reinforced in the Prerequisite Verification step.
````
