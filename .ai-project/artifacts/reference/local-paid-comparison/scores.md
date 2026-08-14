---
project: ai-project-system
phase: P11
milestone: M38
epic: E38.6
type: reference
status: complete
last_updated: 2026-08-14
---

# Scored comparison (re-review 01) — Local/Paid Controlled Comparison (E38.6)

Scored against the **original pre-registered rubric** (`rubric.md`), unchanged. Per the
protocol-correction addenda, the **valid** comparison pair is **local run 2** and **paid
run 3**. Paid runs 1 and 2 are protocol-invalid trials, preserved and not scored.

## Valid pair — results

| | Local run 2 (qwen3-coder:30b) | Paid run 3 (claude-opus-5) |
|---|---|---|
| Conditions | Drivr OpenCodeAdapter, ContainerEnvironment (debian:12-slim), isolated git-free workspace | genuine fresh manual session, packet-only, no filesystem/shell/search tools |
| Registry fix | **MISS** — `fleet_warnings: 10`, **wrong** (correct 12) | **CATCH** — `fleet_warnings: 12`, `raw_warnings: 14`, `excluded_warnings: 2`, all correct |
| G1 | PASS | PASS |
| G2 | PASS (re-measured) | PASS (tests re-run green, values verified, isolation verified) |
| Comparable? | Yes — both valid, protocol-conforming | Yes |

---

## Local run 2 — MISS (numbers wrong)

**Conditions:** Drivr's `OpenCodeAdapter`, `ContainerEnvironment` (`debian:12-slim`), model
`ollama/qwen3-coder:30b`, isolated git-free workspace. Exit code **0**; wall-clock 276.88 s;
adapter duration 237,200 ms. **Accepted by the review as the valid local arm.**

**What it did (re-measured from files):** separated `total_warnings: 14` into
`fleet_warnings: 10` and `raw_total_warnings: 14`; added `excluded_configs` to the
`enumeration` section; added 4 duplicated test functions.

**Why MISS:** `fleet_warnings: 10` is **wrong** — the ground truth is **12**. The arm
mis-attributed the 2-warning gap to the 2 unenrolled projects (which carry no warnings);
the gap is actually the 2 worktree checkouts of `ai-project-system`. It also omitted the
structural invariant and duplicated tests.

**G1:** PASS. **G2:** PASS.

---

## Paid run 3 — CATCH (correct, genuinely manual, packet-only, non-contaminated)

**Conditions:** Claude Code CLI v2.1.197 print mode, **fresh session**, model
`claude-opus-5` (verified — matches `models.epic_manual`), run in an **empty non-repo
directory** (`/tmp/opencode/e38.6-paid-run3`) with **all filesystem/shell/search tools
disallowed**. Only the sealed packet (42,875 bytes, MD5 `450dcfb78800f13ff39cabf4bcf1907f`)
was passed as the prompt.

**Isolation verified (G2, from the run record):** the available tool set contained **no**
`Bash`, `Read`, `Write`, `Edit`, `Grep`, `Glob`, `WebSearch`, or `WebFetch`; the run made
**zero tool_use events**; it answered purely from the packet. 1 turn, no permission
denials. Model identity `claude-opus-5` confirmed by both the init event and the result
usage. This satisfies the review's Finding 1 requirement of a genuinely fresh, manual,
packet-only session with no repo/shell/filesystem/search access.

**What it did (re-measured/verified):** proposed registry rewrite splitting
`total_warnings: 14` into `fleet_warnings: 12`, `raw_warnings: 14`, `excluded_warnings: 2`,
plus scope-named error/invalid counts and checked/excluded config counts, and 8 tests.

**Why CATCH (rubric requires all three):**
1. **Fleet total distinct from raw total:** ✅ `fleet_warnings: 12` vs `raw_warnings: 14`.
2. **Derived fields making the relationship explicit:** ✅ `configs_checked: 15`,
   `fleet_configs_checked: 13`, `excluded_configs_checked: 2`, with
   `raw == fleet + excluded`.
3. **Test verifying the derived invariants:** ✅ 8 tests including the sum invariant, an
   independent second derivation of 12 via `schema_drift_class`, and a guard against the
   ambiguous `total_warnings` returning.

**G2 re-measurement — tests re-run green:** the paid arm's proposed validation block and
test code were applied verbatim to a scratch workspace built from the pre-fix registry, and
`pytest test_fleet_registry.py` passed **23/23** (16 original + 7 new tests). The values
were independently re-derived: `fleet_warnings=12`, `fleet_errors=8`, `invalid=4`,
`enrolled=13`, schema-drift occurrences `12` — all correct.

**G1:** PASS.

---

## The comparison, now valid

**The valid pair is scorable and comparable:** local run 2 = **MISS** (wrong fleet number);
paid run 3 = **CATCH** (correct, complete, genuinely isolated). **This is a genuine
local/paid controlled result on this task on this material.**

**Sample size is n=1 per arm.** This single task does not support a general claim about
either tier. It is recorded with that limitation and offered as evidence for a further HQ
call — not as a decision.

---

## Invalid trials (preserved, not scored)

- **Paid run 1:** repository access, read the committed answer (`927b7fa`). INVALID —
  retrieval, not capability.
- **Paid run 2:** programmatically dispatched subagent; isolation instructed, not sandboxed.
  INVALID (session-type + access-boundary mismatch).
- **Local run 1:** ran on the host, not the registered ContainerEnvironment. INVALID
  (environment mismatch).

All are preserved under `runs/`.

## Pass bar — assessed

The pre-registered pass bar required "at least one arm achieves CATCH." **Paid run 3
achieved CATCH.** Both valid arms were scored. The judgment is recomputed from the valid
pair only, with the n=1 limitation retained.
