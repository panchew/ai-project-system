---
artifact_type: progress_digest
artifact_version: 1.0
timestamp: 2026-08-17T23:59:00Z
issuer_chat: HQ Chat
target: Creation Chat
project_name: ai-project-system
period_covered: 2026-08-01 to 2026-08-17
supersedes: .ai-project/artifacts/progress-digests/2026-07-31__hq__progress-digest.md
purpose: P12 scoping handoff — P11 is fully closed at v8.0.0; HQ cannot self-scope a phase
---

# Progress Digest — ai-project-system (2026-08-01 to 2026-08-17)

**For the Creation Chat, to open P12 scoping.** P11 is fully closed. HQ does not scope a phase — the
Creation Chat sets the spine — so this digest exists to make that session start from the converged
state rather than reconstruct it.

---

## Phase Status

| | |
|---|---|
| **P11** | **FULLY CLOSED** 2026-08-17 |
| Merge | `bd198c2` · Closure declaration `0408e66` · Tag **`v8.0.0`** |
| Suite | **549 passed / 0 failed / 0 skipped** (this repo), **452 passed** (Drivr) — both measured by HQ at Step 6 |
| Milestones | **five** — M36 Record Integrity · M37 Corpus Record Conventions · M38 Drivr Inception · M39 Trustworthy Completion Signal · M40 Coordination |
| Open PRs | none |
| Blocking concerns | **none** |

**Eleven phases complete.** P11 opened four milestones and closed five: a second cleanup milestone was
inserted mid-phase at CFO direction when M38 had accumulated seven epics, four of them carry-forward
hygiene HQ had routed there one ruling at a time.

---

## What P11 actually produced

**Drivr exists** at `~/soft-dev/drivr`, enrolled under this framework, with a scheduler, a derived
gate queue, a headless surface, and signed one-time-link approval. It implements no inference and
invokes a CLI engine it does not own — the spine held.

**The record was repaired before any of it was built.** M36 and M37 closed the Steering Note ID
collisions, canonized an allocation rule with a test behind it, reconciled Creation Chat
re-instantiation to one normative statement, codified System HQ's routing, and gave all 17
`governance/systems/` documents a version and a changelog.

**`P9-GH-1` closed** — open since P9 — and `P10-GH-9`'s substantive half with it, both landing
*before* dispatch wiring, which was `P10-GH-9`'s own trigger.

**Two bugfixes**: `B3.1` (Steering Note ID uniqueness guard) and `B2.1` (the sandbox could not reach
the host's Ollama — a gap documented **2026-07-12** and worked around per-epic for three weeks).

---

## Open Decisions — for the Creation Chat

### 1. What is P12's spine?

**HQ does not infer one.** This is the decision that gates everything else, and the one this digest
exists to enable.

### 2. The sharpest technical question P11 leaves open — read this before choosing a spine

**M39 validated a completion judgment, and the engine on today's roster cannot produce its positive
verdict.** M39's closure declaration states it plainly among eight self-reported limits:

> *Every case comes from one runner (`local-agent-runner`); none from OpenCode. Engine generality is
> untested — not weakly supported, untested. Worse for M40: a live OpenCode run projects
> `effect_ledger=None`, so it can never reach `EFFECTS_VERIFIED`.*

Amendment A1.1 made **OpenCode the sole roster engine**. A1.2 put `local-agent-runner` under directed
retirement assessment. **So the coordination layer P11 built is validated against the engine the phase
was moving away from, and blind on the one it moved to.**

Also from the same corpus: `undetermined` on four of six cases, and *"on strict scoring it loses to
the degenerate baseline"* (a mechanism that always answers *completed* scores 5/6). It beats the
degenerate baseline on contradictions — 0 versus 1 — and on nothing else.

**This is not a defect report.** It is honest self-assessment that M39 and M40 both volunteered, and
it is the most decision-relevant thing in the phase. Whether P12 closes that gap, lives with it, or
goes somewhere else entirely is the Creation Chat's call.

### 3. Four proposals returned to the CFO in P11 — status

| Proposal | Where it landed |
|---|---|
| Drivr may *propose* fleet-state transitions, never execute | **Resolved by fallback** — M38 built transitions as an append-only recorded human action; `transitions: []`, no timer, no hook |
| The `local-agent-runner` retention bar | **Assessment run** (E38.4) and recorded. The **bar itself was never set** by the CFO |
| Model-watch as cheap re-tests rather than scheduled investigations | **Never answered.** No watch is scheduled; E35.5's harness remains available |
| The engine-comparison spike | **Done twice** — B3.1's field evidence, then E38.6's controlled comparison |

### 4. Whether the `P11-GH-2` sibling pattern earns its own record

*A premise inherited from an input and not re-tested against the decision the artifact itself just
made.* Two instances, **both HQ's**, recorded as a sub-heading on `P11-GH-2` rather than filed.
**Left to the CFO deliberately** — HQ is the party it indicts and should not be the one deciding it
stays minor.

### 5. The artifact-type inventory the CFO has pending

Comparing artifact families **in use** against those **templated**: `rulings` has **no template**
despite being the most consequential class HQ produces, and `field-evidence` **was minted by HQ in
P11 without a template or a ruling authorizing a new type**. Both implicate HQ.

### 6. `model-routing-policy.md` row P4

**Not decided.** M38 produced the fourth-axis milestone-context evidence; the 2026-07-31 ruling is not
reopened. A further HQ call, on the CFO's timing.

---

## Carry-Forwards to P12

**Three gap records, all filed in P11, all open.** Per the 2026-08-05 ruling the `GH-` prefix names
**the phase that filed it**, permanently — these keep their `P11-` prefix in P12 and forever.

| ID | Substance | Trigger |
|---|---|---|
| **`P11-GH-1`** | Mid-flight spec amendments do not reach working branches. **Fired four times in P11**, once in reverse | Any parent amending a spec a child is already executing |
| **`P11-GH-2`** | Verification performed at the wrong layer — four axes: environment, time, scope, literal-vs-rendered | Any claim whose layer, time or scope differs from the one it is cited for |
| **`P11-GH-3`** | Phase closure has no pre-merge completion artifact, where Epic and Milestone both do. **Found by the CFO** reviewing P11's own delivery | **P12's opening — it is its own first customer** |

The phase closure declaration carries the fuller M39/M40 list with each item's trigger, including
**55 artifacts whose frontmatter is not valid YAML** (five of them closure declarations), intermittent
engine tool-calling, and the unusable-`\b`-against-`__` corpus finding.

**Restated, not reopened:** llama.cpp and any non-Ollama local runtime is **CLOSED by CFO decision**,
not parked — its hardware trigger is void and no phase re-inherits it. Push/WhatsApp deferred.
Single-window explicitly not a requirement. Sidekick-for-external-projects remains a **Brief-level
identity question** and no phase should inherit it as an unstated pivot.

---

## What the phase says about how it worked

Recorded because it bears on how P12 should be run, not as commentary.

**The review chain caught every HQ error, and there were several.** A ruling whose xfail mechanism
could never fire; an amendment count corrected downward after HQ applied only the half that lowered
it; a rule generalized from one run that the phase's own known case falsified; a technical note
inherited from an opener and never checked against the running version. **Each was caught one level
down, by a chat applying HQ's output rather than reading it.** `P11-GH-2` and its sibling exist
because of that pattern, and the open question in both is whether the chain catching them is a
property of the design or of current attention.

**One convention was written in P5 and observed for the first time in P11** — one git worktree per
concurrent chat, ignored for seven weeks including by HQ, now in force with three trees. Its
mechanism candidate is recorded against a future scheduler: *a dispatcher that decides when a run
happens is the natural owner of which worktree it gets.*

---

## Blocking Concerns

**None.** Nothing in the framework waits on the Creation Chat except P12 itself.

---

## Next Actions

1. **Read this digest and set P12's spine**, or decide that the next move is not a phase at all.
2. **Answer or retire** the four items in Open Decision 3 — two are genuinely unanswered.
3. **Rule on Open Decision 4** — whether the sibling pattern is filed.
4. **File a Steering Note to HQ** carrying the spine. HQ opens the phase from it and produces the
   Phase Execution Chat Starter.
5. **P12's opening should carry `P11-GH-3`** — a Phase Completion Declaration at §5C Step 2, so the
   next phase gate has an artifact to review rather than a PR comment.

---

## Closing Note

P11 set out to build the thing that holds the framework's hands, and it did: the lane runs, the gate
queue is derived, the human holds the key through a signed link that cannot be a chat reply.

**What it did not settle is whether the machine can tell when its own work is finished.** M39 built
the judgment, validated it on the engine the phase was retiring, and wrote down that the engine it
kept cannot produce the verdict. That is an honest place to stop a phase and a real place to start
one.

**The one thing waiting is P12, and it is waiting on the Creation Chat.**
