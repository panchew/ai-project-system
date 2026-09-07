---
artifact_type: progress_digest
artifact_version: 1.0
timestamp: 2026-09-07T23:59:00Z
issuer_chat: HQ Chat
target: Creation Chat
project_name: ai-project-system
period_covered: 2026-08-19 to 2026-09-07
supersedes: .ai-project/artifacts/progress-digests/2026-08-17__hq__progress-digest.md
purpose: P13 scoping handoff — P12 is fully closed at v9.0.0; HQ cannot self-scope a phase
---

# Progress Digest — ai-project-system (2026-08-19 to 2026-09-07)

**HQ to the Creation Chat.** P12 is closed. **HQ does not scope a phase** — that is what this hands
over.

---

## Phase Status

| | |
|---|---|
| **Phase** | **P12 FULLY CLOSED** 2026-09-07 at **v9.0.0** |
| `master` | `c707b9a` · delivery merge `2a033fe` · tag `v9.0.0` |
| **Version** | `governance.version` `8.0.0` → **`9.0.0`** |
| **Suite** | **774 passed** · validator **0 errors, 0 warnings** |
| **Scale** | **Seven** milestones (M41–M47), **thirty-two** epics |
| **Total** | **Twelve phases**, all closed |
| **Open PRs** | none |
| **Blocking concerns** | **none** — nothing in the framework waits on this chat except P13 itself |

---

## What P12 actually produced

**It opened on one sentence and closed it at every tier it had been found in:** *when the evidence
that should gate an action is absent, the action proceeds.*

- **Execution tier.** The sandbox's `subprocess.run(command, shell=True)` host path is **removed, not
  guarded** — absence now raises and exits 5. Staging is scoped to an explicit list. The merge
  ladder's `--admin` rung is gone **and its test is inverted**: it once asserted the override beat a
  protected branch; it now asserts the override is unreachable. `ai-project-init` no longer
  manufactures an agent and then validates its own stub.
- **Acceptance chain.** A child cannot hold merge authorization. **Silence accepts nothing** — an
  acceptance names the party that reviewed. Exhausted rework flips the parent to manual; resume
  restores the mode and **not the budget**.
- **Completion signal.** `_decide` reads `Role.INSPECTION`; **`undetermined` is first-class at six
  substrates** and survives end to end without folding into *in progress* or *blocked*.
- **Surface.** Three governance rules made **unrepresentable** rather than validated — a closed
  capability domain, not runtime checking.
- **Then it used what it built.** M47 carried `P1-M1-E1.1` on `panchew-io` end to end agentically
  through Drivr: **111 tool rounds, 21 files changed**, instrument verdict `PASS` against a bar
  committed **before** the run it judged.

**Closed:** `P12-GH-1`, `P12-GH-2`. **`P10-GH-7` re-rated on measured evidence.**

**Outside the milestone machinery**, by CFO decision (SN-40…SN-46): the **baseline model line-up**
landed; the **switching ratchet** broken — **six** surfaces, not the four SN-40 counted; **local
inference PARKED, re-enterable**, north star unchanged and only the sequence changed.

**Three firsts, and they are the phase closing with what it built:** the first closure **reviewed
against a Phase Completion Declaration** (`P11-GH-3`, which the CFO found by symmetry — P12's opening
said it would be its own first customer, and it was); the first acceptance recorded as a **named**
acknowledgment; the first proof that is **a run** rather than an assertion that one could happen.

---

## Open Decisions — for the Creation Chat

### 1. What is P13's spine?

**HQ cannot answer this and does not try.** What HQ can say is what P12 leaves in front of it.

### 2. The sharpest question P12 leaves — read this before choosing a spine

**Agentic dispatch worked. Once.** One project, one epic, one engine — and M47 says so in its own
record rather than claiming more.

**Everything that made it work is unproven at any other scale:** it ran on `panchew-io`, whose
governed `models:` block **had been silently reverted by its own restructure** (M47 Finding 1,
verified live). The engine was one remote provider. The instrument that validated it has judged one
run.

**So the honest statement is that the framework can now do the thing it was built for, and has done
it exactly once.** Whether P13's spine is *scale that*, *harden that*, or something else entirely is
the Creation Chat's call — but a spine chosen without noticing that `n=1` would be choosing on a
weaker basis than the record supports.

### 3. The CFO's productivity direction is live and only half discharged

SN-40…SN-46 (2026-08-27) ruled: *be more productive, work better, not harder.* **Agentic runs working
properly matters more than local inference.** P12 delivered the first half — a run that works.
**The second half — that it works repeatably, on more than one project — is untouched.**

### 4. The ecosystem is now seven projects, and three are unplaced

P11 recorded four. The CFO has since named **`content-creation-pipeline`, `wheelie`, `panchew-io`**.
**The enrollment path is about to be exercised three more times**, and **SN-45's adoption gap is
open**: this framework runs on PRs, branches and merge authorizations — **it assumes a configured
remote by construction, and `bin/ai-project-init` does not establish one.**

### 5. Drivr has no remote, by CFO ruling

**Every Drivr commit exists on one disk. No PR exists for any Drivr change.** Ruled *"local-only for
now."* **Recorded as a decision, not a defect** — but P12's proof run depended on Drivr, and the
publication-model question rides with any spine that leans on it further.

### 6. Two items P11 left that P12 did not answer either

**The `P11-GH-2` sibling pattern** — whether it earns its own record. **Left to the CFO deliberately:
HQ is the party it indicts.** And **the artifact-type inventory**: `rulings` still has **no
template**, and P12 issued eleven of them into an untemplated class.

---

## Carry-Forwards to P13

**Ten items with owners and triggers. Five were never formally filed before P12's closure.**

| ID | Item | Owner | Trigger |
|---|---|---|---|
| **`P12-CF-1`** | **`model_verification` flip, `advisory → blocking`** — disposed by *record why not*. **Flipping while the configured rows do not describe what those chats run on would halt every Phase, Milestone and Epic chat, and P13 could not open a Phase Chat at all.** | HQ | Arm when `models.phase`, `models.milestone` and `models.epic_manual` name what those chats actually run on |
| `P12-GH-3` | **Derived-claim rot** — a correction is itself a derived-claim event | unowned | Filed with its trigger; M44 confirmed **not absorbed** |
| `P12-GH-4` | The inter-chat channel is ungoverned | partially landed | Narrow half in M44/E44.3; remainder open |
| `P12-GH-5` | Declared context exceeds loaded | unowned | Filed with its trigger |
| — | **Drivr has no remote** | Phase/HQ | Publication-model decision |
| — | **Delivery Notice location split** — corpus bi-located; template and practice disagree; **no test catches it** | unowned | M44 reproduced **both sides in one milestone** |
| — | **Duplicate `Error Handling` CONTENT in the AOG** — the title collision is fixed, the content is not | unowned | E44.4 was scoped to titles |
| — | **Closed-phase sweep scope** — does *corpus-wide* include the closed record? | unowned | Wants a ruling **before** a sweep asks |
| — | **The suite is non-deterministic where `visual_artifacts.enabled: true`** — pass / fail / pass on identical commits | unowned | ***"Suite green" is the gate every closure reports against***, including P12's |
| — | **`panchew-io` silently reverted a CFO-authorized `models:` block through its own restructure** | fleet | Any project whose governed config can be reverted by its own restructure |

**Restated, not reopened:** **llama.cpp and any non-Ollama local runtime is CLOSED by CFO decision**,
not parked — no phase re-inherits it. **Local inference is PARKED**, re-entry conditional on agentic
runs working properly. **Row P4, `P12-GH-5` and the `local-agent-runner` parse-repair question park
with it.** `local-agent-runner`'s **retention stands** — parking did not reopen it.

---

## What the phase says about how it worked

**Recorded because it bears on how P13 should be run, not as commentary.**

**`P12-GH-3` closed at ten dated instances across four levels. Every one was caught DOWNSTREAM. None
by a check. Four were HQ's own** — including one where **HQ misread a gate in a spec HQ wrote**, and
one where **HQ committed the defect while filing the note that names it.**

> **Whatever this project builds to catch premise-dependents, it should assume the author cannot run
> it on themselves.**

**P11 asked whether the review chain catching every HQ error is a property of the design or of
current attention. P12 does not answer it either** — but it leaves **ten dated instances and a stated
design requirement**, which is more than P11 left, and it is the strongest candidate this project has
for a rule that would have caught things nothing else did.

**A second observation, and it is a durable one about mechanism.** P12 ran through **four complete
peer-roster turnovers in a single day**; HQ's own session name changed twice; messages sent to
identified chats landed nowhere within the hour. **Every artifact survived; no message was reliable.**
One incorrect constraint circulated in chat for a week and **stopped at the artifact boundary** —
it never reached a spec, so nothing had to be unwound. **The batching discipline was adopted for
token economy and turned out to be a quarantine.**

**Concretely for P13:** the inter-chat channel is now **bounded by ruling** — purpose, round cap,
terminating condition, or the exchange does not start. **HQ was the specimen that produced that rule**,
having sent roughly two dozen unbounded messages before it existed.

---

## Blocking Concerns

**None.** Nothing in the framework waits on the Creation Chat except P13 itself.

---

## Next Actions

1. **Read this digest and set P13's spine** — or decide the next move is not a phase at all.
2. **Weigh Open Decision 2 before choosing.** Agentic dispatch works, at `n=1`, on a project whose
   governed config had silently reverted. That is a real result and a narrow one.
3. **Decide whether the three unplaced projects and SN-45's adoption gap belong in the spine**, given
   the enrollment path is about to run three more times.
4. **Answer or retire Open Decision 6's two items** — the `P11-GH-2` sibling pattern and the
   artifact-type inventory. Both have now survived two phases, and **both implicate HQ**, which is
   why HQ has placed neither.
5. **File a Steering Note to HQ carrying the spine.** HQ opens the phase from it and produces the
   Phase Execution Chat Starter.

---

## Closing Note

P12 set out to make the framework stop when its evidence is missing, and then to use it in anger for
the first time. **It did both.** The gates fail closed by construction rather than by compliance, the
completion signal can admit ignorance, the surface cannot express the violations it used to validate,
and a real epic ran end to end with a record that shows work was **done** rather than that a process
exited.

**What it did not settle is whether any of that holds at n greater than one.** That is an honest place
to close a phase and a real place to start one.
