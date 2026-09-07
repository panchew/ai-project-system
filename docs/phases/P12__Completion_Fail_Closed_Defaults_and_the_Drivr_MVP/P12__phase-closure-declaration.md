---
type: phase-closure-declaration
phase: P12
name: "Completion: Fail-Closed Defaults and the Drivr MVP"
status: CLOSED
closed_date: 2026-09-07
declared_by: HQ Chat (ai-project-system)
supersedes: docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12__phase-completion-declaration.md
---

# Phase P12 Closure Declaration

**Phase P12 — Completion: Fail-Closed Defaults and the Drivr MVP is CLOSED.**

**PSG §5C Step 9.** Written on `master` **after** the merge, the tag and the version bump exist,
because those are what it records. The **Phase Completion Declaration** it supersedes was written at
Step 2 while the phase was still open and is what HQ reviewed at Step 6 — **the two are different
artifacts doing different jobs, which is the arrangement `P11-GH-3` existed to create.**

---

## Delivery Record

| | |
|---|---|
| **Consolidation PR** | **#280**, `phase/P12` → `master` |
| **Merge commit** | `2a033fe` |
| **`master` head at closure** | `2a033fe` |
| **Tag** | **`v9.0.0`** → `2a033fe` |
| **Version** | `governance.version` `8.0.0` → **`9.0.0`** |
| **Suite** | **`774 passed`**, re-run by HQ on `master` after merge |
| **Config validator** | **`0 errors, 0 warnings`** |
| **Milestones** | **Seven** — M41…M47, all closed into `phase/P12` |
| **Epics** | **Thirty-two** |
| **Open PRs** | none |

**Twelve phases complete.**

---

## Process Record — three firsts, and they are the phase closing with what it built

1. **The first phase closure reviewed against a Phase Completion Declaration.** `P11-GH-3` —
   *phase closure has no pre-merge completion artifact, where Epic and Milestone both do* — was
   **found by the CFO** by arguing from symmetry against the corpus. P12's opening said the phase
   would be its own first customer. **It was.** M44/E44.1 landed the template; the declaration at
   Step 2 is what HQ received at Step 6.
2. **The first acceptance recorded as a NAMED acknowledgment**, per M43/E43.2 — *silence accepts
   nothing.* HQ's acceptance names the accepting session. **Under the model this phase replaced, a
   clean phase delivery could have produced no artifact on either side.**
3. **The first phase closure whose proof is a real agentic run.** M47 carried `P1-M1-E1.1` on
   `panchew-io` end to end through Drivr — **111 tool rounds, 21 files changed**, instrument verdict
   `PASS` against a bar committed **before** the run it judges.

**HQ re-measured the organizing evidence at Step 6 rather than accepting the checklist** (G2). All
four fail-open instances verified **in the source**: the sandbox's `shell=True` host path **removed**
rather than guarded; staging scoped to an explicit list; the `--admin` rung gone **with its test
inverted** to assert unreachability; init's placeholder deleted.

---

## What P12 Delivered to `master`

**P12 opened on a confirmed finding: *when the evidence that should gate an action is absent, the
action proceeds.*** It closed that disposition at every tier it had been found in.

- **Execution tier (M42).** `bin/` no longer proceeds on absent gating evidence. Sandbox absence
  aborts, staging is epic-scoped, approval failure aborts, `ai-project-init` never manufactures an
  agent. **`P12-GH-2` closed.**
- **Acceptance chain (M43).** A child cannot hold merge authorization; acceptance is no longer
  indistinguishable from absence; exhausted rework flips the parent to manual; resume restores the
  mode and not the budget. **`P12-GH-1` closed** — the rework limit reached 0 of 25 templates and now
  reaches 7.
- **Records and rituals (M44).** The Phase Completion Declaration; the HQ re-instantiation ritual
  recorded from nine instances; a context-exhaustion handoff type; `governance-propagation.md`'s
  false Constraints struck; the AOG renumbered `1..18` monotonic.
- **Completion signal (M45).** `_decide` reads `Role.INSPECTION`; **`undetermined` is first-class at
  six substrates** and carried end to end without folding. **`P10-GH-7` re-rated on measured
  evidence.**
- **Surface (M46).** Three governance rules made **unrepresentable** rather than validated — a closed
  capability domain, not runtime checking. The model-qualification gate, with its bar committed
  first.
- **Proof (M47).** One real epic, one real project, one engine — and a record that shows the work was
  **done** rather than that a process exited.

**Outside the milestone machinery**, by CFO decision and HQ ruling: the **baseline model line-up**,
the **switching ratchet broken** — it was **six** surfaces, not the four SN-40 counted — and
**local inference PARKED, re-enterable**, north star unchanged, sequence changed.

---

## Carry-Forward to P13

**Owners and triggers, per the Completion Declaration. Restating is not reopening.**

| ID | Item | Owner | Trigger |
|---|---|---|---|
| **`P12-CF-1`** | **`model_verification` flip, `advisory → blocking`.** Disposed by *record why not* (CFO). **Flipping while the configured rows do not describe what those chats run on would halt every Phase, Milestone and Epic chat — P13 could not open a Phase Chat at all.** | HQ | **Arm when `models.phase`, `models.milestone` and `models.epic_manual` name what those chats actually run on.** |
| `P12-GH-3` | Derived-claim rot — **a correction is itself a derived-claim event** | unowned | Filed with its trigger; M44 confirmed **not absorbed** |
| `P12-GH-4` | The inter-chat channel is ungoverned | partially landed | Narrow half in M44/E44.3; remainder open |
| `P12-GH-5` | Declared context exceeds loaded | unowned | Filed with its trigger |
| — | **Drivr has no remote** — every Drivr commit exists on one disk | Phase/HQ | CFO ruled *"Drivr code local-only for now"*; revisit on a publication-model decision |
| — | **Delivery Notice location split** — corpus bi-located, template and practice disagree, no test catches it | unowned | Observed since P11-M40; M44 reproduced **both sides in one milestone** |
| — | **Duplicate `Error Handling` CONTENT in the AOG** — the title collision is resolved, the content is not | unowned | M44/E44.4 was in scope for titles only |
| — | **Closed-phase sweep scope** — does *corpus-wide* include the closed record? | unowned | Wants a ruling **before** a future sweep asks |
| — | **The suite is non-deterministic where `visual_artifacts.enabled: true`** — pass / fail / pass on identical commits; 38 s vs 176–213 s | unowned | **Never formally filed until P12's closure.** *"Suite green" is the gate every closure reports against* |
| — | **`panchew-io` reverted a CFO-authorized `models:` block through its own restructure** | fleet | M47 Finding 1, verified live. Any project whose governed config can be silently reverted by its own restructure |

**Restated, not reopened:** **llama.cpp and any non-Ollama local runtime is CLOSED by CFO decision,
not parked** — its trigger is void and no phase re-inherits it. **Local inference is PARKED**, with
re-entry conditional on agentic runs working properly (SN-42/SN-43). Row P4, `P12-GH-5` and the
`local-agent-runner` parse-repair question **park with it.** `local-agent-runner`'s **retention
stands** — parking did not reopen it.

---

## Two annotations from HQ's Step-6 acceptance, carried here

1. **`4 of 12` claims resolved on the proof run.** It passes the ruled per-lane floor legitimately —
   C-C is the `epic_qa` lane's term and is correctly recorded `scored: false` — and **nothing in this
   closure is contingent on it.** But *"the work was done"* and *"the claims about the work resolve"*
   are different properties, and this run separates them by a factor of three. **Worth a successor's
   attention when the `epic_qa` lane is next exercised.**
2. **The Phase Chat corrected HQ on `model_verification`, and was right.** HQ's ordering fix said
   *flip last, by HQ*. The better answer is that **flipping at all is wrong while the rows do not
   describe reality.** Recorded because the correction came from the level below, which is this
   phase's most repeated finding about itself.

---

## The finding this phase leaves about its own conduct

**`P12-GH-3` closes at ten dated instances across four levels. Every one was caught downstream, none
by a check. Four were HQ's own** — including one where **HQ misread a gate in a spec HQ wrote**, and
one where **HQ committed the defect while filing the note that names it.**

> **Whatever this project builds to catch premise-dependents, it should assume the author cannot run
> it on themselves.**

**P11 asked whether the review chain catching every HQ error is a property of the design or of
current attention. P12 does not answer it either** — but it leaves ten dated instances and a stated
design requirement, which is more than P11 left.

---

## Sign-Off

**Phase P12 is CLOSED at `v9.0.0`.**

**Accepted at §5C Step 6 by HQ Chat (`ai-project-system`), session
`62efeb41-f77c-488e-b4e6-6ae9aa976dd4`** — a named acknowledgment per E43.2, on
[#280](https://github.com/panchew/ai-project-system/pull/280#issuecomment-5566112832).

**Merge and tag authorized by the CFO (Layer 8)** on diff review, per **PSG §11.6.1** — HQ has no
parent chat, so the CFO is the mandatory diff reviewer and **authorization is not review.** Both were
given: he reviewed, and HQ accepted.
