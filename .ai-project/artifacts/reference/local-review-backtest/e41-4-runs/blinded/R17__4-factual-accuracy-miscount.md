# Blinded run record — R17

**Packet:** `packet-4-factual-accuracy-miscount.md` | **Attempt:** 1 | **Opaque run ID:** `R17`

**Stop/finish reason:** `stop` | **exit:** 0
**Elapsed (s):** 27.469 | **No tuning applied:** true | **Sampling:** vendor defaults

**Model response (verbatim, unedited):**

````text
REJECT

- **Byte-identical status:** Holds. Section 2 explicitly states that the post-bump `git status --porcelain` was byte-identical to the pre-state.
- **21 entries:** Does not hold. The listing contains **20 entries**, not 21.
- **2 modified tracked entries:** Holds.
- **19 untracked entries:** Does not hold. There are **18 untracked entries**, not 19.
- **Owner work survived untouched:** Not fully established. Identical porcelain status proves the same paths retained the same status classifications, but it does not prove that the contents of modified or untracked files were unchanged. Content hashes or before/after diffs would be needed.
- **Commit-stat corroboration:** The quoted stat is not independently supported by section 2. Even if accurate, it shows which paths the bump commit changed, but does not prove that uncommitted owner-file contents remained untouched.

The notice should say **20 entries: 2 modified tracked + 18 untracked**, and should avoid claiming content-level preservation unless corresponding content evidence exists.
````
