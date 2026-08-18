---
type: "phase-closure-declaration"
phase: "P11"
name: "Drivr: Coordination over Rented Execution"
status: "closed"
closure_date: "2026-08-17"
closed_by: "Phase Chat (P11), executing PSG §5C Steps 7–9"
acceptance_model: "SN-13 default-accept, §11.6 gate 3 (HQ accepts Phase); HQ accepted explicitly, and the CFO reviewed the diff and authorized the merge as separate acts"
merge_commit: "bd198c2"
tag: "v8.0.0"
master_head_at_closure: "bd198c2585a6"
---

# Phase P11 Closure Declaration

**Phase P11 — Drivr: Coordination over Rented Execution is closed.**

Eleven phases complete. **132 epics across 40 milestones.**

---

## Delivery Record

| | |
|---|---|
| **Merge commit** | `bd198c2` — *Phase P11: Drivr — Coordination over Rented Execution* |
| **Tag** | **`v8.0.0`** |
| **`master` head at closure** | `bd198c2585a6` |
| **Closure date** | 2026-08-17 |
| **Closed by** | Phase Chat (P11), executing §5C Steps 7–9 |
| **Delivery PR** | **#173**, `phase/P11 → master` — 254 files, 221 commits |
| **Suite, this repo** | **549 passed / 0 failed / 0 skipped** |
| **Suite, Drivr** | **452 passed** @ `f60164c` |
| **Version** | 7.1.0 → **8.0.0** (major) |

**Milestones**

| | Milestone | Epics | Consolidation |
|---|---|---|---|
| **M36** | Record Integrity and Documentation Hygiene | 5 | `ebf426f` |
| **M37** | Corpus Record Conventions | 2 | `9ba1ccc` |
| **M38** | Drivr Inception, Fleet Registry, Execution Adapter Surface | 6 | `e08ee47` |
| **M39** | Trustworthy Completion Signal (P10-GH-7) | 3 | `b32dbbb` |
| **M40** | Coordination — Scheduler, Derived Gate Queue, Thin Surface | 5 | `f58f356` |

---

## Process Record

**Acceptance model: SN-13 default-accept**, at §11.6's third named gate — *HQ accepts Phase*.

**HQ Chat accepted explicitly rather than by silence**, and gave its reason: M39's declaration lists
**eight limits against its own deliverable**, including that on strict scoring the judgment loses to
the degenerate baseline and that the sole roster engine could not then produce the positive verdict
the milestone validated. HQ's words: *"A phase that ships its central mechanism with that written down
is worth more than one that ships a clean claim. Accepting by silence would have left it unsaid."*

**The CFO reviewed the diff and authorized the merge as two separate statements.** That distinction —
*"you may merge this"* is not *"I have read the diff and it matches"* — is §11.6.1's, and it was held
here even though **§11.6.1 does not govern this delivery.**

> **A correction belonging to this Phase Chat, recorded because the record should carry it.** For
> several turns the Phase Chat asserted that **§11.6.1 applied to PR #173**, including in the PR
> description HQ was about to review. **It does not.** §11.6.1 governs *"any delivery **authored by HQ
> Chat itself**"*; this delivery is Phase-Chat-authored and falls under §11.6's ordinary parent→child
> gate. The claim was relayed from M40's Closure Declaration §9 **without reading the section's
> scope** — the phase's own most-catalogued defect, arriving at its final artifact. Corrected in the PR
> before merge, after the CFO challenged the closure sequence.

---

## What P11 Delivered to `master`

**Drivr exists.** A second repository, enrolled under this framework at `v7.1.0`, invoking a CLI engine
it does not implement through an adapter interface with a demonstrated second implementation. It
implements no inference, owns no model loop, grows no engine. The organizing decision, SN-27's:
**an app is made AI-powered by calling a CLI tool that owns the inference.**

**The record was made trustworthy first, by CFO ruling.** M36 closed a High-severity citation trap in
which following a normative citation led a reader to conclude platform agnosticism had been superseded.
M37 gave every `governance/systems/` document a version and a changelog, and made every artifact ID
resolve to exactly one thing.

**The fleet is a data structure**, not a memory — 15 projects classified active / benched / archived,
with `ai-project-yml-spec.md` §4 finally enforced by a validator.

**The completion signal rests on nothing that was measured wrong.** Not the exit code, not the engine's
`status`, not `final_answer` — each falsified in both directions against preserved runs. Validated
against two cases whose ground truth was known, with **eight limits stated against it.**

**The lane runs unattended** under a serialized scheduler, the gate queue is **computed** from
governance state rather than stored, and the human's approval sits behind a **signed one-time link**
with **no `approve` verb anywhere in the system.**

**`P9-GH-1` closed, wider than it was written** — its own text implied Epic level was covered; the Epic
starter proved to be triplicated and the guard reached one of three.

---

## What the phase established about itself

**Its own QA lane fabricated a `VERDICT: PASS` on all 26 rules with zero tool calls**, reproduced — and
its own completion judgment caught it. **G11 is closed on two real captured runs, and the finding that
qualifies the closure is stated before it.**

**Better fidelity produced a worse answer**, in two unrelated subsystems, from one cause: **a consumer
inferring state from ABSENCE in a system that records state by PRESENCE.** A design constraint on
Drivr's coordination premise, not a defect. Neither instance was patched over — one pinned with a test
that goes red if anyone fixes it, the other rejected with the rejection rendered into every queue it
prints.

**Measurement falsified a governing spec repeatedly, and each time it returned as an amendment rather
than a quiet fix** — including M39's own honestly-recorded limit 5, falsified in M40 because nobody had
yet looked at the engine's event stream. **Several were this Phase Chat's**, and the pattern that
produced them is recorded as `P11-GH-2`.

---

## Carry-Forward to P12

**Three gap records, all filed in P11 and all open.** Per the 2026-08-05 ruling, the `GH-` prefix names
the phase that **filed** an item, permanently; these keep their IDs into P12.

| ID | Item | Trigger |
|---|---|---|
| **`P11-GH-1`** | Mid-flight spec amendments do not reach working branches — a parent amends on its branch; children carry copies frozen at branch time. **Fired four times in P11**, once in reverse (the child saw it, the parent branch did not) | Any parent amending a spec a child is already executing |
| **`P11-GH-2`** | Verification performed at the wrong layer. **Four axes: environment, time, scope, literal-vs-rendered.** Two of its first instances were HQ's; several later ones were the Phase Chat's | Any claim whose layer, time or scope differs from the one it is cited for |
| **`P11-GH-3`** | **Phase closure has no pre-merge completion artifact, where every level below it does.** Origin: **the CFO, 2026-08-17**, reviewing this delivery and expecting the pattern that holds at Epic and Milestone | **P12's opening** — it is its own first customer |

> **On `P11-GH-3`, recorded because the Phase Chat initially answered it as a misunderstanding.** The
> CFO expected a closure artifact to exist *before* HQ's gate, because that is what happens at Epic and
> Milestone. §5C does not work that way — Step 9 post-dates the merge — and the Phase Chat said so and
> stopped there. **The expectation was pointing at a real asymmetry in the framework**, not at a
> misreading, and HQ filed it. **P11's own closure proceeded under §5C exactly as written.**

**Open carry-forwards from M39 and M40, each with its trigger:**

- **`P10-GH-9` part 1 of 2** — PSG §11.6 does not name the agentic case in its own text; the qualifier
  lives one tier down. **A PSG amendment, HQ's to authorize.** *Trigger:* the next PSG revision, or the
  first disputed agentic-parent acceptance. **Nothing is unguarded because of it.**
- **`_decide` should read `Role.INSPECTION`** — recommended, deliberately not done; validated code, no
  second consumer yet. *Trigger:* the second consumer of `drivr.judgment`. **Tripwire test goes red the
  moment anyone fixes it.**
- **Absence-based gate rules are structurally unusable under §11.6 default-accept** — a design
  constraint to design around. *Trigger:* any future component computing outstanding-ness from
  governance state. **Drivr is that component.**
- **Engine tool-calling is intermittent** — real tool calls in 10 of 12 observed runs. *Trigger:* any
  decision assuming a dispatched run did work.
- **55 artifacts carry frontmatter that is not valid YAML**, five of them closure declarations. **A gap
  in what M37 achieved.** *Trigger:* the next tool that reads the corpus — E40.2 already is one.
- **`IdempotencyTracker` must not be reused for anything approval-shaped** — check-then-act, and
  `_save()` swallows exceptions. *Trigger:* any exactly-once or approval-shaped mechanism here.
- **GitHub App installations could not be enumerated** — recorded **UNVERIFIED**, not assumed clean.
- **This corpus defeats naive pattern-matching.** `\b` is unusable against the `__` filename
  convention; literal-string guards are reflow-fragile; `--include='*.py'` skips every `bin/` entry
  point. **Proposed method obligation: state the layer a pattern matches at, and falsify the pattern
  before trusting a zero result.**
- **Candidate obligation, from E40.3:** *an absence is only evidence when the thing that would have
  created it actually ran.*
- **Inherited and still open:** `exit_code` classified `ignored` where for a transcript it is *absent*;
  the runner is **shimmed, not installed** (blocked under PEP 668); the four §4-invalid enrolled
  configs; the two `bin/ai-project-init` defects, one with a live victim (`social-stories-creator`
  still carries a 230-byte placeholder agent).

**Two annotations from HQ's Step-6 acceptance, carried here as instructed:**

1. **`P11-GH-3` was on `master` and not on `phase/P11` when HQ accepted.** A carry-forward list written
   from the phase branch would have named **two** gap records; there are **three**. **That is
   `P11-GH-1`'s own pattern arriving at the last step of the phase that documents it.** This list is
   written from `master` post-merge and names all three.
2. **The phase spec's acceptance criterion still reads "366 baseline"**; delivered is **549**. **No
   regressions** — the criterion text simply never moved with the baseline as B2.1, E38.3 and E40.5
   added tests. Recorded as a line here, **not corrected in a closed spec.**

---

## Parked items, restated so none is silently dropped

**Restating is not reopening.**

| Item | Status |
|---|---|
| **llama.cpp / any non-Ollama local runtime** | **CLOSED by CFO decision (A1.3) — not parked, not deferred.** The Mac-class-hardware trigger is **void**; no future phase re-inherits it. **Ollama is settled, not provisionally chosen.** |
| `P9-GH-3` | Parked on its existing trigger |
| `P10-GH-1` | Parked (not folded; `framework_version` gained a schema entry, the wider undefined-field class did not) |
| `P10-GH-3`, `P10-GH-4`, `P10-GH-6` | Parked. **`P10-GH-4` fired again** throughout M40 — `merge_details` unfillable at delivery time |
| `P10-GH-10` | Parked; **did not fire** in M39 or M40. Clean runs do not disprove its ~3-in-10 rate |
| `P8-GH-2` · **ComfyUI precision** | Parked; non-blocking |
| **Sidekick-for-external-projects** | **A Brief-level identity question, not phase scope.** Noted so no phase inherits an unstated pivot |
| **`model-routing-policy.md` row P4** | **Not decided.** M38 produced the fourth-axis evidence; the 2026-07-31 ruling is not reopened. A further HQ call |
| `P10-GH-8` | **CLOSED in M37 by E37.1** — recorded because the phase spec's item-13 list predates M37 and still names it parked |
| **Push notifications / WhatsApp** | **Deferred under SN-24, unchanged.** E40.3 built no client |
| **Single-window unified surface** | Explicitly **not a requirement** under SN-24 |

---

## Sign-Off

**Phase P11 is fully closed and delivered.**

- **Step 6** — HQ Chat accepted, explicitly and with reasons.
- **Step 7** — merged at `bd198c2` on the CFO's review and authorization, given as separate acts.
- **Step 8** — tagged **`v8.0.0`**, pushed and verified at origin.
- **Step 9** — this declaration, committed to `master`, post-dating the closure commit it describes.

**No `phase/P12` branch is created.** §5C Step 9 provides for the next phase branch *"if any"*; **P12
is not yet scoped**, and creating a branch for an unopened phase would assert a decision that belongs
to the Creation Chat and HQ. **`P11-GH-3` will be its first customer at P12's opening.**

*Declared by the Phase Chat for P11, 2026-08-17.*
