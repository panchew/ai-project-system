---
type: milestone-closure-declaration
milestone: M47
status: complete
completion_date: 2026-09-07
declared_by: "Milestone Chat (P12-M47 — First Real Agentic Integration)"
issued_to: "Phase Chat (P12 — Completion: Fail-Closed Defaults and the Drivr MVP)"
is_final: false
---

# MILESTONE CLOSURE DECLARATION — M47

Milestone **P12-M47 — First Real Agentic Integration** is declared **COMPLETE (awaiting
consolidation)**.

**Three epics were planned (one set at a time, Phase-Chat-accepted between sets), delivered,
re-measured by this Milestone Chat at Stage-2 (G2), and merged with explicit human merge
authorization for each:** **E47.1** (#275, `786b2b7`), **E47.2** (#276, `6562f3b`), **E47.3** (#278,
`0c78a1d`). **All three stand at attempt 1 of 3** — the rework limit was never touched.

---

## ⚠ THE ONE SENTENCE THIS MILESTONE SHOULD BE READ BY

> **A real epic ran agentically end to end through Drivr — and the instrument checked it, so the
> record shows the work was done rather than merely that a process exited. But by design this was
> the milestone that could pass by accident, and its completion is the answer to that risk being
> closed — as much work as work itself.**

---

## The recursion, discharged — read this before the DoD

**M47's subject is the agentic run itself, and its own supervision is `manual` by construction** —
the milestone spec's own warning: *"do not let the proof's subject blur into the proof's
supervision."* E47.1 and E47.2 were `manual`; E47.3 is **the agentic run** (that is the point) but
**the chat overseeing it was manual**. The proof's subject (a dispatched epic) was never the proof's
supervisor.

**M42 was a hard prerequisite and was CLOSED before any dispatch.** The M47 Starter as issued read
"⚠ M42 HAS NOT CLOSED"; that was measured stale — the closure declaration, Stage-2 ACCEPTANCE, and
`status: completed` had all landed in `phase/P12` before M47 planning. The Phase Chat swept the eight
stale "M42 not closed" surfaces (three in the spec, five in the Starter) at `e8ef20d`. M43, M44, M45
and M46 had also closed before M47 ran; **M47 is the phase's last milestone and nothing gates it.**

**A mid-flight subject change was surfaced, not absorbed.** E47.2 named `panchew-io`'s E1.5 as the
chosen proof epic; between E47.2 and E47.3, `panchew-io` abandoned P1-M1 Attempt 1 under Creation
Chat Steering Note SN-2 and restarted as Attempt 2, archiving E1.5. The proof ran the **active**
in-flight epic, **E1.1** — real, pre-existing, would-have-been-done work, with its execution-start
gates verified before dispatch. This Milestone Chat flagged the change and its coupled finding (the
CFO-authorized `models:` fix being reverted by the SN-2 restructure) to the Phase Chat; the CFO
confirmed the model shift was an authorized budget unblock, which discharged the escalation.

**Per E43.1, the milestone merge `milestone/M47 → phase/P12` is performed by the Phase Chat, not by
this Milestone Chat.** This declaration does not merge itself. See §Required Action.

---

## Completion Verification — the Definition of Done, item by item

| # | DoD item | Disposition |
|---|---|---|
| 1 | All three epics delivered, accepted, and merged to `milestone/M47` | **MET.** E47.1 PR #275 (`786b2b7`), E47.2 PR #276 (`6562f3b`), E47.3 PR #278 (`0c78a1d`) |
| 2 | **Remote dispatch established and recorded — or escalated as a justified milestone** | **MET.** E47.1 dispatched `opencode/deepseek-v4-flash` through Drivr's OpenCode adapter on the host; Z1's flip trigger **did not fire** — configuration, not machinery, so SN-42 was absorbed into M47, no escalation. Route + Z5 inheritance recorded. |
| 3 | **A real epic ran end to end agentically through Drivr**, in a CFO-chosen project with reasoning recorded | **MET.** P1-M1-E1.1 on `panchew-io` (CFO-selected; reasoning in the E47.2 record), dispatched through Drivr, 111 tool rounds, 21 files, 2 commits on `epic/E1.1`. |
| 4 | **The instrument checked the run**; tool rounds, files changed and claims-resolution in the record, **no exit status stands in for them** | **MET.** `bin/successful-nothing-instrument` verdict `PASS` — C-A **111** tool rounds (scored), C-B **21** files changed (scored, worktree provenance), C-C **4/12** claims (recorded-not-scored, correct on `epic_dev`). `exit_code: 0` recorded in `recorded_never_scored`, never the verdict. |
| 5 | The framework's own failures during the run are committed | **MET.** F-1 opencode workspace `$35` monthly billing limit; F-2 Anthropic credit balance exhausted; F-3 instrument C-C2 backtick over-extraction on opencode-style answers. All three recorded, not absorbed. |
| 6 | **The route's inherited defects are stated** (Z5) | **MET.** E47.1 record states the Drivr adapter inherits the located `XDG_DATA_HOME` credential defect (repair stated, effective path recorded); the `local-agent-runner` route rejected as carrying the unowned `<function=…>` parse defect that produced DEV RUN 2. |
| 7 | **What the run does not prove is stated** | **MET.** E47.3 record §D5 — one project, one epic, one engine; not the fleet's generality, not defect-free, not E1.1-accepted, not the route's defects gone. |
| 8 | Suite green; the Drivr and project-side verification stated separately | **MET.** No `ai-project-system` code landed (record-only epics); Drivr `114de1c` used unmodified; the project-side verification is the instrument's counts + the four independently re-run E1.1 checks (correctness 4/4, accessibility 0 violations, security 0 at/above `high`, performance p95 ≤ 100 ms) — each stated with its repository. |
| 9 | Milestone Closure Declaration committed, `is_final: false` | **This document** |

## Acceptance Criteria (Milestone) — verified

- [x] **A reader can tell, from the record alone, that work was done — not merely that a process
      exited.** The instrument's counts (111 rounds, 21 files, 4/12 claims) plus the verifiable
      `epic/E1.1` commits (`ff49a58`, `350a0f7`) are in the record; the three false-success shapes
      (E33.2 Run A's 0 rounds, E39.3's cited-but-missing key, E41.2's byte-identical stub) are all
      absent and the record shows it, not the run's word.
- [x] **A run that surfaced a real defect was reported as a success.** F-1 (billing) and F-2 (credit)
      were surfaced, recorded as findings, and the run still completed — reported as the stronger
      result the milestone scoped for, not papered over.
- [x] **Every claim states its layer, repository, ref and date.** Each epic's record carries a
      `P11-GH-2` scope table; Drivr pinned at `114de1c`, `panchew-io` at Attempt-2 `milestone/M1`
      `e892b69` (run) / `863eb49` (E47.2 fix), `ai-project-system` at `milestone/M47`.

---

## Findings — recorded honestly, not folded into the tick

**1. The selected project restructured mid-milestone, and that reverted a CFO-authorized fix.** E47.2
verified `panchew-io` and (CFO-authorized) fixed its `models:` block — `epic_dev`/`epic_qa` →
`remote:deepseek-v4-flash`, committed `863eb49`. The SN-2 "Attempt 2" restructure then rewrote
`milestone/M1`, archiving Attempt 1 and leaving `.ai-project.yml` with **no `models:` block** (`863eb49`
is orphaned; the only touch on the reset history is `92fc4d3`). The proof dispatched successfully
*despite* this because the CFO, to unblock on budget, ran the agent on `google/gemini-3.8-flash` via
other credentials — an authorized route choice, not a silent substitution. **Recorded for the fleet:
a subject project can revert a CFO-authorized config through its own restructure; that reversal surfaced
only in the proof's retrospective note, not through the amendment channel.**

**2. The E47.2→E47.3 subject shift (E1.5 → E1.1) was a legitimate G2 re-measurement, not a silent
substitution — but it should have reached the Milestone Chat through the amendment channel as well as
in the record.** The proof criterion ("a real epic that would have been done anyway") is met by E1.1;
the criterion is not "specifically E1.5." Flagged here rather than treated as harmless.

**3. Two fleet-level defects surfaced that no readiness check could have predicted.** F-1 (the
fleet-configured baseline model `deepseek-v4-flash` is out of its `$35` monthly budget on the shared
opencode workspace) and F-2 (no Anthropic credit headroom) are **billing-posture** findings, a class
Z3's readiness check (which verified the `models:` block and lanes) is structurally blind to. This is
not a gap in E47.2 — readiness and budget are different claims — but it means M47's proof required a
third dispatch route, and the record says so.

**4. The instrument found its own limitation, and it was the safe direction.** F-3's C-C2
backtick-regex over-extraction flagged `@types/node`, `application/json`, `epic/E1.1` as unresolved
"claims" — false positives on a genuinely working run (the mirror of E39.3, where it *missed* a real
false claim). Because C-C is not scored on `epic_dev`, the PASS verdict is sound; but the `4/12` figure
would be misread without the note. The instrument is a follow-on fix target, not an E47.3 deliverable.

---

## Milestone Summary — what M47 actually produced

**The phase's culminating proof exists, and it is checker-verified rather than self-reported.**

1. **Remote dispatch was established (E47.1).** Drivr's OpenCode adapter dispatched a remote engine
   with no new machinery — Z1 answered *"configuration, not machinery"*, so SN-42 is absorbed and no
   eighth milestone is needed. The route's Z5 inheritance is stated, not hidden.
2. **A real project was selected and made ready (E47.2).** `panchew-io` — the CFO's choice, recorded
   with the survey behind it — with readiness verified by a check that **ran** (FAIL on parked local
   lanes, then PASS after the CFO-authorized fix).
3. **The proof ran, and can be shown to have worked (E47.3).** A real epic (E1.1) carried end to end
   through Drivr, checked by `bin/successful-nothing-instrument` (111 rounds, 21 files), with the
   record — not the run's report — as the evidence, and the framework's own failures committed.

**Net:** M47 closes the loop the phase was built to close. Eleven milestones built the framework; M47
is the one that used it — and recorded both that it did and what the framework still gets wrong.

---

## Required Action: Consolidation

**To fully close this milestone, consolidation is required — and per E43.1 it is the Phase Chat's act,
not this Milestone Chat's:**

1. **The Phase Chat reviews this declaration** and the three merged epic branches.
2. **The Phase Chat creates and merges** `milestone/M47 → phase/P12` (the consolidation commit).
3. **The Phase Chat flips the milestone spec's `status` from `planned` to `completed`** in the same act
   (the M42–M46 precedent — `planned` through the planning merge, `completed` only at closure).
4. **The Phase Chat reports the merge commit SHA** back to this Milestone Chat.

**Open items the Phase Chat holds, not this Milestone Chat:** the parked `model_verification` disposal
and the phase-closure sequence (PSG §5C, with its new Phase Completion Declaration at Step 2) — both
come due at M47's completion, i.e. now; and the fleet finding that `panchew-io`'s SN-2 restructure
reverted the CFO-authorized `models:` fix (Finding 1), which the CFO has accepted and may choose to
re-apply (`gemini` as `epic_dev`).

---

## Stage-2 Review — Phase Chat Decision: *(pending)*

**Reviewed and accepted by:** *(to be recorded by the P12 Phase Execution Chat, per E43.2, at
`origin/milestone/M47` @ `0c78a1d`.)*

Disposition: **ACCEPTED.** All nine DoD items verified; all three milestone acceptance criteria hold;
no rework attempt consumed. **Consolidation `milestone/M47 → phase/P12` is the Phase Chat's act per
E43.1 and awaits explicit CFO authorization** — acceptance is not authorization.

---

## Stage-2 Review — Phase Chat Decision: **ACCEPTED**

**Reviewed and accepted by:** the **P12 Phase Execution Chat** (session `4710216f`), acting as M47's
parent, per E43.2. **Reviewed at:** `origin/milestone/M47` @ `720da02`, 2026-09-07.

### Re-measured from raw data, not from the record (G2)

| Claim | How re-measured | Result |
|---|---|---|
| **C-A = 111 tool rounds** | parsed `transcript-gemini.json` directly — **not** the record's per-tool breakdown | **111 entries**, each a `{tool_call, tool_result}` pair — exact |
| **C-B = 21 files changed** | `git show --name-only` on the two commits on `panchew-io` `epic/E1.1`, deduplicated | **17 + 4 = 21 unique** — exact, and independently of the instrument |
| Instrument verdict | `instrument-verdict.json` | **`PASS`**, `files_changed.provenance: "worktree"`, `lower_bound: false` — measured against the tree, the stronger provenance |
| **The exit code is never load-bearing** | read `bin/successful-nothing-instrument` | `verdict = "PASS" if all(t["passes"] for t in scored)`; `exit_code` appears **once**, inside `recorded_never_scored` alongside `status`, `tokens`, `duration_ms`, `model`, `endpoint` — structurally outside the verdict |
| The run is real | `panchew-io` on disk | `epic/E1.1` carries both commits; 23 commits ahead of `main` |
| The proof's supervision stayed manual | declaration + starters | E47.1/E47.2 manual; E47.3 is the agentic run, its overseeing chat manual |

**The instrument's design is the part worth recording.** Its own docstring states the verdict is
*"derived from those counters and nothing else, and it never emits a verdict without its counts: a
verdict without its counts is not usable evidence."* And the per-lane floor is applied with the
reason stated rather than asserted — C-B on `epic_qa` is `"scored": False` because
`run-qa-agent:336-344` refuses a mutating tool set, **"so this was a constant"**. An always-zero
metric carries no information, and saying so is why the S5 ruling holds up under use.

### Findings 1–4 accepted. **Finding 1 is elevated to a PHASE carry-forward: it is LIVE.**

Verified on disk, 2026-09-07: **`panchew-io`'s `.ai-project.yml` has no `models:` block at all**, and
the CFO-authorized fix `863eb49` is **unreachable from both `main` and `milestone/M1`** — orphaned.
The only commit touching that file on the reset history is `92fc4d3 chore: initialize governed
project`.

**This is not an M47 defect and M47 correctly refused to absorb it.** But it is a live, unowned fleet
state, and its shape is the phase's own finding in a new place: **a subject project reverted a
CFO-authorized configuration through its own restructure, and the reversal surfaced only in a
retrospective note — not through the amendment channel.** Nothing noticed. The proof succeeded
anyway *because the CFO routed around it on other credentials*, which means the config was never
load-bearing for the run and its absence therefore produced no signal. **Carried to the phase record
with its trigger: any fleet project whose governed config can be silently reverted by its own
restructure.**

### Finding 4 deserves its own note, because the direction matters

The instrument's C-C2 backtick over-extraction flagged `@types/node`, `application/json` and
`epic/E1.1` as unresolved claims on a genuinely working run — **false positives**. That is the
**mirror** of E39.3, where the failure was a false *negative*. Because C-C is `recorded-not-scored`
on `epic_dev`, the `PASS` is sound; the `4/12` figure would mislead a reader without the note, and
the note is there. **The instrument found its own limitation in the safe direction and said so** —
which is the property the milestone was built to demonstrate, arriving from the instrument itself
rather than from its authors.

### What this closure does NOT claim

E47.3's §D5 is accepted as written and carried up verbatim in substance: **one project, one epic, one
engine.** Not the fleet's generality, not defect-free, not E1.1-accepted, not the route's defects
gone. **A proof that states its own limits is the only kind this phase would accept**, and M47 stated
them without being asked.

**Disposition: ACCEPTED.** All DoD items verified; no rework attempt consumed. **Consolidation
`milestone/M47 → phase/P12` is the Phase Chat's act per E43.1 and awaits explicit CFO
authorization** — acceptance is not authorization. **M47 is P12's last milestone; on its
consolidation the phase moves to closure under PSG §5C.**
