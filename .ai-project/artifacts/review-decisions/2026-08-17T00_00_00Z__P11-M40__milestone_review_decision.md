---
type: review-decision
level: milestone
milestone: M40
phase: P11
reviewed_artifact: ".ai-project/artifacts/closure-declarations/2026-08-17T23_30_00Z__P11-M40__milestone_closure_declaration.md"
reviewed_by: "Phase Chat (P11 — Drivr: Coordination over Rented Execution)"
issued_to: "Milestone Chat (P11-M40 — Coordination: Scheduler, Derived Gate Queue, and the Thin Surface)"
date: 2026-08-17
decision: accept
scope: "milestone ACCEPTED; one narrow correction required before consolidation"
---

# Stage-2 Review Decision — P11-M40: ACCEPTED, one narrow correction

**Decision: ACCEPT.** All twelve DoD items and all seven acceptance criteria hold. Every claim I could
verify independently verified, including the milestone's largest — that **M39's limit 5 is falsified by
a real live run.**

**One correction is required before consolidation** (§3). It is one pair of quotes and one count, and it
lands on the artifact phase closure rests on.

*(This decision's own frontmatter quotes every scalar containing a colon — the defect §3 is about.)*

---

## 1. Verified independently — re-run and re-measured

| Claim | Result |
|---|---|
| `ai-project-system` at `5b10cee` | ✅ **549 passed** |
| `drivr` at `f60164c` | ✅ **452 passed** |
| Five merges `724c66a` `e4a1388` `efa1338` `ece1c50` `5b10cee` | ✅ all present |
| **E40.5's binding position honoured in fact** | ✅ `724c66a` **10:17:42** → E40.1 `e4a1388` **12:31:16**, same day |
| **§3.1 — a live run reached `EFFECTS_VERIFIED`** | ✅ run `1786987322-39168925`: `completion: effects-verified`, `expectation: mutating` |
| — its raw stream carries an ordered ledger | ✅ **19 events, 5 × `tool_use`**, plus `step_start`/`step_finish`/`text` |
| — journal across runs | ✅ `no-effects-observed`, **`effects-verified`**, `no-effects-observed` |
| **The guard reaches 8 surfaces** | ✅ 8 governance files named in `tests/test_merge_authorization_routing_guard.py` |
| **The Epic starter is triplicated** | ✅ `governance/EPIC-EXECUTION-CHAT-STARTER.md`, `governance/systems/…`, `governance/templates/…` — **P9's guard reached 1 of 3** |
| **`bin/drivr-gate` has no `approve` verb** | ✅ and its docstring states the omission is deliberate |
| Invalid-YAML frontmatter across the corpus | ✅ **finding confirmed** — see §3 for the count |

**The falsification is the milestone's headline and it holds.** M39 recorded *"a live OpenCode run can
never reach `EFFECTS_VERIFIED`"* as limit 5, and **that limit is now false.** OpenCode's `--format json`
stream does carry ordered `tool_use` events; the ledger is projectable; the verdict was reached through
E39.1's own `covering-verification` rule, unmodified.

**M39 was not wrong to record it, and the declaration says so correctly** — M39 deliberately did not
look, because nothing in M39 needed the answer, and **the question was answerable only at OpenCode's
layer.** E40.1's spec §F2 forbade answering it from Drivr's parser for exactly that reason. **A limit
recorded honestly, then falsified by the epic that needed it, is the process working.**

> **This also supersedes a finding of mine.** M40's milestone spec table — *"`effects-verified`:
> UNREACHABLE"* — was **accurate against the code as it stood** (`from_execution_result` hard-codes
> `effect_ledger=None`) and is now **superseded by the projection E40.1 built.** `P11-GH-2`'s **time
> axis**, on my own spec, and the right outcome: I recorded what was true, the epic changed what was
> true.

---

## 2. What earns the acceptance

**The Hard Constraint was discharged claim by claim, and the re-measurement column is the point.** I
asked that every claim be measured rather than declared. §2 does better: it records **what the Milestone
Chat re-measured itself rather than accepting** — verdicts re-derived from raw `stream.ndjson`, the queue
deleted and recomputed to the same digest, the one-time link exercised live to `409`/`403`×3, **a chat
reply actually posted to the live surface** (`400`, *"expected exactly one `t`, got 0"*), GitHub read
rather than the tree for the authority ceiling, and **the guard falsified by deleting it** — 1 surface →
2 failures, all 8 → 17 failures, restore → 549.

**Falsifying your own guard is the strongest form of the evidence obligation** and it is the answer to
the rotted-guard problem this phase has hit twice.

**Two claims were reported weaker than their headline, self-reported before I asked** — E40.3's
`ACCEPTED_FIELDS` falsification breaks exactly one test because it guards a declaration rather than the
enforcement, and E40.4's ceiling inventory carries one **UNVERIFIED** row because GitHub App
installations cannot be enumerated with a user token. **Recorded as a gap, not assumed clean.** A
milestone closing a phase had every incentive to round both up.

**§4 is the most valuable thing in this declaration and it is not a deliverable.** *Better fidelity
produced a worse answer*, found twice, in unrelated subsystems, from one cause: **a consumer inferring
state from ABSENCE in a system that records state by PRESENCE.** A perfectly projected ledger on a
read-only run still reads `NO_EFFECTS_OBSERVED`; an absence-based gate rule reads the **happy path as
the backlog**, because §11.6 accepts a clean delivery **by silence and produces no artifact**. **Both get
worse as recognition improves.**

That is a design constraint on Drivr's entire coordination premise, correctly identified as such rather
than as a defect — and **neither was patched over**: one compensated at the consumer and **pinned with a
test that goes red if anyone fixes it**, the other **rejected and the rejection rendered into every
queue it prints.** Making a compensation retirable rather than permanent is the right instinct.

**And `P9-GH-1` closed wider than it was written.** Its own text — *"past the Epic templates"* — implied
Epic level was covered. **It was not: the Epic starter is triplicated and the guard reached one of
three**, and `governance/EPIC-EXECUTION-CHAT-STARTER.md`, which `README.md:15` designates canonical,
**carried an unguarded instruction to merge.** An item open since P9 turned out to be larger than its
own description.

---

## 3. The correction — the declaration's own frontmatter does not parse

Carry-forward 5 reports **55 artifacts** with unparseable frontmatter, **five** of them closure
declarations. **Re-measured: 56 and six.**

The difference is **this declaration.** Line 6:

```
declared_by: Milestone Chat (P11-M40 — Coordination: Scheduler, Derived Gate Queue, and the Thin Surface)
```

`Coordination: Scheduler` is an unquoted scalar containing `": "` — `yaml.safe_load` fails with
*"mapping values are not allowed here."* **So M40's Closure Declaration is not machine-readable, and it
is the artifact phase closure rests on.**

**This is the count-omission class one final time** — *a record stating a count that omits its own
contribution* — landing in the artifact that reports the defect, about the defect it reports. The phase
has now tracked this class from M36 through M40; **this is its closing instance and it is the tidiest of
them.**

### Required — two edits, no re-run

- [ ] **Quote the `declared_by` scalar** (and any sibling containing `": "`) so the frontmatter parses.
      Verify with `yaml.safe_load`, not by eye.
- [ ] **Correct carry-forward 5's count to 56 / six, including this declaration**, and say that it
      included itself — the omission is the finding's own subject.

**Nothing else.** No epic reopens, no re-measurement, no suite re-run. **On landing, the milestone is
accepted and consolidation proceeds.**

*I note the same class of trap caught me during this review:* my first search for the guard used a
literal phrase, returned **zero across all eight surfaces**, and read as a missing guard. Carry-forward
8 predicted exactly that — *"literal-string guards are reflow-fragile as a class… once nearly filing a
defect against a guard that was present and correct."* **It happened to me on the claim that warns about
it.** Its proposed method obligation — *state the layer a pattern matches at, and falsify the pattern
before trusting a zero result* — **is accepted and carried to phase closure.**

---

## 4. The two items handed to me for §5C Step 6 — both accepted, both mine

**1. PR #173's description is stale and I wrote it.** It lists two M36 planning documents while the PR
changes **187 files** (Copilot Finding A2, verified). **That description is the first thing a §11.6.1
reviewer reads.** I will rewrite it before requesting the CFO's diff review — a phase-closure PR whose
description describes one milestone's planning is an obstacle to the review it exists to enable.

**2. E40.5's handback obligation, accepted without qualification.** My own starter carries no
Phase-level routing guard — it predates E40.5, and **a template amendment reaches no already-running
chat** (`P11-GH-1`). For a **`phase/* → master`** delivery:

> **PSG §11.6.1 applies, and an HQ authorization does not stand in for the CFO's diff review.**
> *"You may merge this"* is not *"I have read the diff and it matches."*

**Recorded as binding on me at Step 6.** I will not treat an authorization as a review, and I will say
which I have received.

---

## 5. Disposition

**Milestone P11-M40 — Coordination is ACCEPTED**, subject to §3's two edits.

The lane runs unattended across five captured dispatches nobody started. The gate queue is derived and
reproduces to the same digest. A signed one-time link was minted, used, and refused on reuse, with a
chat reply posted and rejected. Two competing models produced 23 findings and **resolved nothing**.
`P9-GH-1` closed wider than written, before dispatch was wired. **Nothing became an engine, and no
`approve` verb exists anywhere.**

**And the milestone falsified four things it was handed, including one of mine and one of M39's, each
returning as an amendment rather than a quiet fix.**

**On the corrected declaration, `is_final: true` triggers PSG §5C.** The Phase Chat proceeds to phase
closure: README, version bump, **PR #173 with a rewritten description**, the **CFO's §11.6.1 diff
review**, merge, tag, and the Phase-Closure Declaration restating §7 and §8 with **llama.cpp recorded
CLOSED, not parked.**
