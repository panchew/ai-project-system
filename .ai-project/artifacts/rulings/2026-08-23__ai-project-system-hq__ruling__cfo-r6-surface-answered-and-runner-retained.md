---
type: hq_ruling
concern_id: R6 carry-forward trigger (CFO answer); local-agent-runner retention (CFO decision)
amends_in_part:
  - .ai-project/artifacts/rulings/2026-08-20__ai-project-system-hq__ruling__r6-manual-verification-surface-rule.md
  - .ai-project/artifacts/rulings/2026-08-23__ai-project-system-hq__ruling__batched-p12-dispositions.md
issued_by: HQ Chat (ai-project-system), scribing two CFO decisions
issued_to: Layer-8/CFO (mandatory diff reviewer, PSG §11.6.1); the P12 Phase Chat; M41; M46; M47
phase: P12
date: 2026-08-23
status: active
blocking_resolved: false
---

# HQ Ruling — The CFO Answers R6's Surface Question and Retains `local-agent-runner`. Neither Lands Anything, and One Gap Has No Owner

**Prerequisite verification (P9-M31-E31.3):** harness `claude-opus-5` vs `models.hq:
remote:claude-opus-5` — **match.**

**HQ scribes here; it does not decide.** Both decisions below are the CFO's, taken 2026-08-23.
**Recorded because a decision that lives only in a chat is one roster turnover from gone** — SN-33's
finding, demonstrated three times in this phase.

---

## Decision 1 — The R6 surface question is ANSWERED: yes, and in a more general form than was asked

**The CFO's answer, in substance:** *he will drive a Phase Chat and a Milestone Chat inside **any
harness that provides the required model(s)**. OpenCode qualifies.*

**HQ notes the general form is broader and better than the question**, and records it as the operative
statement rather than the instance:

> **The surface criterion is not "is it OpenCode." It is "does the harness provide the required
> model."** A future harness meeting that condition needs no new adjudication.

**That retires the per-surface question this phase kept re-opening.** F6 adjudicated one row; R6
replaced it with one rule over three rows; **this replaces "which surface" with a property a surface
either has or does not.**

### It applies to all three rows, and HQ states the reading so it can be narrowed if wrong

**R6 constructed the carry-forward as *one trigger covering three rows* — `phase`, `milestone`, and
`epic_manual` — owner the CFO, no expiry.** The CFO's phrasing named a Phase Chat and a Milestone
Chat; **his general criterion names the harness, not the level.**

**HQ applies it to all three.** The trigger was never per-row; splitting it now would recreate the
per-row adjudication R6 abolished. **If he meant Phase and Milestone only, `epic_manual` stays a
carry-forward on his word and this reading is withdrawn.**

### ⚠ It does NOT land anything, and reading it as a landing would be the error

**The trigger's factual halves stand where the batched ruling left them:**

| Half | Status |
|---|---|
| Runs the model | **Met** |
| Self-report — mechanism | **Met**, verified in the binary |
| Self-report — delivery to a session | **Met**, verified by probe |
| Self-report — **fidelity** | **UNMEASURED**, with a demonstrated failure against it |

**The batched ruling made fidelity binding on the landing regardless of this answer**, and it is not
softened by a yes:

> **The landing requires the check exercised on the interactive path with the actual target models.
> Arming a fail-closed check against a property that has only ever been observed to fail is worse than
> not arming it.**

**So: the surface precondition is satisfied; the measurement is not.** **E41.5's landing set stays
`creation`** until **E41.4's D7** resolves whether the observed normalization is model-side or
injector-side. **Nothing about this answer accelerates E41.5.**

---

## Decision 2 — `local-agent-runner` is RETAINED. The bar is answered by being made moot

**The CFO's answer, in substance:** *the runner is involved in qualifying `epic_dev` and `epic_qa`, and
he is for proceeding.*

**HQ records what that settles, precisely, because it settles less than it appears to:**

**SETTLED — the disjunction from the batched ruling's Decision 7 collapses.** That decision put two
branches to him: *either it is kept and the parse is repaired there, or it is retired and the lane is
rebuilt on something else.* **He has taken the first. `local-agent-runner` is retained; the lane is not
rebuilt on something else.**

**Also settled by consequence:** the retention **bar** — open since P11, assessed in E38.4, never set —
**is moot rather than met.** A bar exists to decide retention. **Retention is decided, so no bar needs
setting**, and HQ records it as **closed by decision, not by evidence** — the same honest form used for
row P4, and for the same reason: **say which route was taken rather than manufacture a citation.**

---

## Decision 3 — What Decision 2 does NOT settle, and it has no owner

**Retaining the runner does not repair the parse.**

**The chain from the batched ruling is unchanged by retention:** `DEV RUN 2`'s successful-nothing came
from the parser reading `<function=…>` as prose → that is the `FAIL 0/20` mode in the bimodal baseline
→ the CFO's bar says *raise N until stable, else hold* → the stable baseline must come from the
**repaired** lane → **M42 does not repair the parse, and cannot: it is in `local-agent-runner`, a third
repository.**

> **So `epic_dev` and `epic_qa` remain unqualifiable until the parse is repaired or ruled irrelevant —
> and after Decision 2, the repair has a home but still has no owner, no milestone, and no phase.**

**Three things HQ is NOT doing, and says so rather than leaving them ambiguous:**

1. **Not scoping the repair into P12.** The phase already carries seven milestones. **A repair in a
   third repository is not a bounded addition to any of them**, and placing it on HQ's own initiative
   is the pattern HQ has refused three times this phase.
2. **Not asserting the parse causes the bimodality.** *Where* is measured. **Whether is plausible and
   unmeasured.** E41.3 dispatches through the repaired lane regardless and may settle it for free.
3. **Not treating "unqualifiable" as failure.** SN-38 already makes **hold** the default for both rows.
   **Holding is a legitimate outcome; holding for an unnamed reason is not** — which is the whole
   reason this is written down.

**The open question, stated once and left with the CFO:**

> **Where does the `local-agent-runner` parse repair happen — a P12 milestone, a bugfix, its own
> repository's work, or P13?** *Trigger: E41.3's first attempt at a stable baseline through the
> repaired lane. It will either stabilise, which retires the question, or it will not, which forces it.*

---

## Disposition

**Two CFO decisions scribed. Neither lands a row.**

**R6's carry-forward can lapse for all three rows on the surface criterion — and does not, because
fidelity is unmeasured.** **`local-agent-runner` is retained and its bar is closed as moot.** **The
parse repair has a home and no owner.**

**`blocking_resolved: false`** — Decision 3's question is open and is the CFO's.

**PSG §11.6.1:** HQ-authored, no chat-level reviewer. **The CFO is the mandatory diff reviewer.**
