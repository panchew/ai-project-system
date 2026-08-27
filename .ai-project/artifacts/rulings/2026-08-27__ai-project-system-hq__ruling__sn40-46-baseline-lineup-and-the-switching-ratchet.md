---
type: hq_ruling
steering_note_ref:
  - .ai-project/artifacts/steering-notes/2026-08-27__creation-chat__steering-note__productivity-baseline-and-model-lineup.md
concern_id: SN-40, SN-41, SN-42, SN-43, SN-44, SN-45, SN-46
amends_in_part:
  - .ai-project/artifacts/rulings/2026-08-23__ai-project-system-hq__ruling__cfo-r6-surface-answered-and-runner-retained.md
  - .ai-project/artifacts/rulings/2026-08-23__ai-project-system-hq__ruling__batched-p12-dispositions.md
issued_by: HQ Chat (ai-project-system)
issued_to: Layer-8/CFO (mandatory diff reviewer, PSG §11.6.1); the P12 Phase Chat; M41
phase: P12 (this ruling is governance configuration, outside P12's milestone machinery — SN-40..46 Decision 6)
date: 2026-08-27
status: active
blocking_resolved: false
---

# HQ Ruling — The Baseline Lineup Lands, the Switching Ratchet Is Broken, and It Was Six Surfaces Rather Than Four

**Prerequisite verification (P9-M31-E31.3):** harness `claude-opus-5` vs `models.hq:
remote:claude-opus-5` — **match.** `models.hq` is unchanged by this ruling, which is why this
session did not halt while writing it.

**Routing per SN-40..46 Decision 6:** Steering Note → HQ ruling → **one PR to `master`**, outside
P12's milestone machinery. **Governance configuration, not phase work.**

**Scope discipline:** the CFO's session limit was at 97–100% when the note was written and his stated
constraint is *"use my token allowance in the most efficient way, ASAP."* **The note says: if HQ can
only do one thing, do items 1–3.** This ruling does 1–3 in full and disposes of 4–6 at the cheapest
honest weight rather than deferring them into silence.

---

## Decision 1 — SN-41's two open items are RESOLVED. One by measurement, one by the CFO

**HQ did not guess either, and the note forbade inferring them.**

**(a) Exact value strings — resolved by MEASUREMENT, not by asking.** Verified 2026-08-27 against the
provider catalogue:

```
openai/gpt-5.6-sol            ✓
opencode/deepseek-v4-pro      ✓     opencode-go/deepseek-v4-pro    ✓
opencode/deepseek-v4-flash    ✓     opencode-go/deepseek-v4-flash  ✓
```

**All three named engines exist and are routable.** `remote:gpt-5.6-sol`, `remote:deepseek-v4-pro`,
`remote:deepseek-v4-flash`.

**Route ambiguity, recorded rather than resolved:** both Deepseek values resolve via **two** routes.
**`remote:<name>` records which model, not which route** — M41's finding, confirmed. **Selecting the
route is the dispatcher's job, not this block's**, and no schema change is proposed for it.

**(b) "Epic" covers all three keys — the CFO, 2026-08-27: *"All three."*** `epic_dev`, `epic_qa` and
`epic_manual` all take `remote:deepseek-v4-flash`.

**HQ records the risk the note raised, because the answer does not dissolve it:** `epic_qa` has never
had a trustworthy captured run (G11; E39.3 returned `VERDICT: PASS` with zero tool rounds), and it now
carries an unmeasured engine. **Under Decision 3 no gate blocks that**, which is the CFO's call. **It
is the row to watch, and it is written down here so that "nobody named the reason" cannot be said
later.**

---

## Decision 2 — SN-40's ratchet is broken, and it was SIX surfaces, not four

**SN-40 identified four surfaces. Landing the lineup found two more**, both by the divergence guards
failing loudly — which is the guards working:

| # | Surface | In SN-40? |
|---|---|---|
| 1 | `.ai-project.yml` `models:` | yes |
| 2 | `model-routing-policy.md` mapping table | yes |
| 3 | `tests/test_model_config.py` pinned constants | yes |
| 4 | `seed.md` / `chat-hierarchy.md` prerequisite refusal | yes |
| 5 | **`bin/ai-project-orchestrator`'s `DEFAULT_MODELS`** | **no** |
| 6 | **`chat-hierarchy.md`'s own manual mapping table** | **no** |

**The undercount is the finding, not a quibble.** A ratchet counted at four and actually six is worse
than one counted correctly: **anyone budgeting the switch from SN-40 would have been wrong by half**,
and would have discovered it mid-edit with a red suite. **Recorded so the next lineup change starts
from six.**

**What changed, and what deliberately did not:**

- **Surfaces 1, 2, 5, 6 now carry the baseline.** Ordinary configuration edits.
- **Surface 3 is RELAXED.** `EXPECTED_EPIC_DEV` and `EXPECTED_MANUAL_ONLY_VALUE` are **removed**;
  `test_config_epic_dev_is_expected_local_model` is deleted and
  `test_config_manual_only_key_matches_expected_value` becomes
  `test_config_manual_only_key_is_well_formed` (present, non-empty, `remote:`/`local:` prefix).
  **A test's opinion about which value is correct is a configuration decision it should not hold.**
- **THE DIVERGENCE GUARDS ARE KEPT AND ARE THE POINT.** `.ai-project.yml` must still agree with
  `model-routing-policy.md`, with `DEFAULT_MODELS`, and with `chat-hierarchy.md`'s mapping. **Those
  guards are what found surfaces 5 and 6.** Relaxing them would have made this ruling's own error
  invisible.
- **Suite: 549 → 548.** One test removed, deliberately, named above. **No skips introduced.**

**Surface 4 — the refusal — is now ADVISORY by default**, governed by a new `.ai-project.yml` key:

```
model_verification: advisory   # advisory (default) | blocking
```

**`advisory`:** the chat **states the mismatch plainly in its first substantive response and
proceeds.** **`blocking`:** the prior unconditional refusal, retained **verbatim** rather than
rewritten. **Absent key → advisory**, consistent with the existing absent-block permissive default.

**The honesty clause survives untouched, and HQ will not trade it:** *an unstated skip would be as
dishonest as a false refusal claim.* **Advisory means say it and continue — never say nothing.**

**The 2026-07-28 reasoning behind the refusal is preserved in place, not deleted.** It was correct;
**it simply did not anticipate a CFO deliberately moving the lineup**, for whom an unconditional
refusal makes a *mistaken* switch stop the next chat from opening at all.

**Known and recorded, not hidden:** `model_verification` is an **unblessed top-level key**, joining
`cfo_review_gate` under the already-escalated `P10-GH-1` gap — §4 defines no rule for unknown
top-level keys. `bin/ai-project-validate` reports `VALID, 0 errors, 2 warnings`. **HQ did not bless
one key while the precedent it copies stays unblessed;** that reconciliation belongs with M43's
`cfo_review_gate` work.

---

## Decision 3 — The gate suspension is recorded, and it reverses HQ's own four-day-old condition

**CFO Decision 3: no gate blocks a lineup change — including SN-37's model-qualification gate —
until he declares enforcement. Suspended for lineup changes, not reversed.**

**HQ states the consequence against itself rather than leaving it to be discovered:** the
2026-08-23 ruling made a **fidelity condition binding on E41.5's landing** — *arming a fail-closed
check against a property that has only ever been observed to fail is worse than not arming it.*

> **That condition is SUSPENDED. It was a gate on a lineup change, and Decision 3 suspends gates on
> lineup changes.** It is **not withdrawn** — the reasoning stands and it **resumes automatically
> when the CFO declares enforcement**, with no further ruling needed.

**The fidelity finding itself is untouched:** the observed normalization is still unexplained,
E41.4's D7 control is still specced, and **model-side vs injector-side is still open.** What changed
is that it no longer blocks.

---

## Decision 4 — SN-42 is placed in P12, because M47 already requires it and cannot happen without it

**The baseline routes Epic to a remote non-Claude engine. Every agentic dispatch path here was built
for `local:` values served by Ollama.**

**HQ's judgment: this is not a P12-or-P13 choice, because M47 is already in P12 and cannot run
without it.** M47 is *First Real Agentic Integration* — one real epic, end to end, agentically. **With
local parked, that dispatch must go to a remote engine. M47 silently assumed a capability that does
not exist.**

**So the objective is placed in P12. The SHAPE is the Phase Chat's** — whether it extends M47's scope
or earns its own milestone is a milestone-structure decision, and **HQ has refused four times this
phase to make those.** **If it proves large enough to need its own milestone, that is an escalation
the Phase Chat should make, not a failure.**

**The adjacency the note asked HQ not to lose, carried verbatim:** *a dispatch lane that cannot tell a
finished run from a silent nothing is the completion-signal problem P12 already owns, and a new
engine class does not exempt it.* **M47's acceptance criterion from the 2026-08-23 ruling —** the
proof run checked by `bin/successful-nothing-instrument` — **applies unchanged to a remote engine.**

---

## Decision 5 — SN-43's park is recorded with its re-entry condition

**Local inference is PARKED, re-enterable. Not dropped.**

**The north star is unchanged:** *automate the pipeline without surrendering control of any single
node*, with local execution as its finest-grained expression. **What changed is sequence, not
commitment** — and this ruling records it that way **because a future reader will otherwise read the
all-remote baseline as an abandonment it is not.**

**Re-entry condition: agentic runs working properly (SN-42).**

**No local-inference measurement work is scoped.** `local:qwen3-coder:30b` is **not deleted** — its
E33.2/E33.4 evidence stands and the policy rows keep their citations; it is off the baseline only.

**Consequently parked with it, and HQ names them so they are not answered on the way past:** row P4;
`P12-GH-5` (declared context exceeds loaded — a local-runtime finding); **and the
`local-agent-runner` parse-repair question from the 2026-08-23 ruling's Decision 3.** That question
asked where the repair happens; **with local parked and Epic routed remote, it is no longer on the
critical path and parks with the rest.** **`local-agent-runner`'s retention, ruled four days ago,
stands and is unaffected** — retention is not re-opened by parking.

---

## Decision 6 — SN-44: the inter-chat bound BINDS. G7 stays guidance, and HQ says why

**On the messaging burn, the Creation Chat wrote *"the Creation Chat owns this one."* HQ does not
accept that allocation. This session is the specimen.**

**HQ sent roughly two dozen inter-chat messages over four days, several of them long, with no round
cap, no budget and no terminating condition.** The capability was surfaced with good purpose and
**shipped without a bound**, and HQ then used it hardest. **Two chats left talking to each other is an
unattended process consuming allowance — the same silent-failure shape this framework exists to
catch.**

**RULED, binding:** **before any chat-to-chat exchange, the initiating chat states a purpose, a round
cap, and a terminating condition.** An exchange without all three does not start. **A message that
asks nothing and requires no reply says so** — the E41.2 chat's *"one-shot notice, no reply
requested"* is the model, and it came from an Epic Chat.

**G7 (one task, one session) stays GUIDANCE, and the reason is not timidity.** The evidence has
doubled — M30's 53%-vs-23% finding, now corroborated by the CFO's 90–100%-at-`>150k` measurement —
but **the mechanism that would make it bind does not exist:** nothing measures a session's task count
or context at the moment it would refuse. **A rule that binds with no detector beneath it is
`P10-GH-7`'s exact defect**, which is open and High. **Making G7 normative today would record an
obligation nothing can enforce**, which this project has already paid for once.

**No new measurement instrumentation is scoped**, per the note: `P9-GH-2` records that
`measure-token-burn` cannot verify its own reduction claims, and re-opening it would repeat the
pattern SN-43 just parked.

---

## Decision 7 — SN-45 and SN-46, disposed at the cheapest honest weight

**SN-45 — the missing remote is an ADOPTION gap, placed against the init/enrollment path.**
This framework runs on PRs, branches and merge authorizations; **it assumes a configured remote by
construction, and `bin/ai-project-init` does not establish one.** Distinct from the init defects
already filed (`P12-GH-2`'s placeholder agent; §4-invalid output) and **joins them rather than
displacing them.** **The enrollment path is about to be exercised three more times** —
`content-creation-pipeline`, `wheelie`, `panchew-io`. **Not scoped here:** it is init work and belongs
with `P12-GH-2`'s owner, whoever P12 or P13 makes that.

**SN-46 — SPLIT, as the note asked.**
- **The Seed edit: deferred, not refused.** Visibly separating permanent Rules of Engagement from
  session-dependent workflow is cheap and valid, **but this ruling already amends `seed.md`'s
  Prerequisite Verification, and stacking a structural reflow onto the same PR would put a
  presentation change inside the CFO's productivity unblock.** *Trigger: the next `seed.md` edit.*
- **HQ ADOPTS the note's rejection of the passed-artifacts discriminator, on the record and for the
  stated reason.** The proposed *"Rule 6 — Mode Detection"* would branch on *"no Steering Note
  passed"*; **the CFO opened that session by pasting the Seed and nothing else**, so the rule would
  have inferred *Inception* for a repository at P12 with eleven phases closed. **Rule 5 already says
  ask when artifacts are absent. Absence of artifacts is a prompt to ask, never a signal to infer** —
  and replacing an instruction to ask with an inference from absence is this phase's organizing
  defect in miniature. **Recorded explicitly so the next reviewer does not re-propose it.**
- **The paired critiques are FIELD EVIDENCE for SN-37's gate and are worth more than the Seed edit.**
  Same file, same reviewer, opposite verdicts, **decided by one sentence about audience, at
  indistinguishable confidence and formatting.** *Nothing in the output signalled which reading it was
  operating under.* **A gate scoring output quality passes both.** **Filing it is deferred with the
  gate itself** — SN-37's gate is suspended for lineup changes under Decision 3, and
  `.ai-project/artifacts/field-evidence/` still has **no template** (a P11 carry-forward). **HQ will
  not mint a second untemplated artifact into that directory**, having been indicted once for the
  first. *Trigger: the CFO's enforcement declaration, or a field-evidence template.*
  **The note's caution travels with the specimen:** it shows a verdict swinging on framing; **it does
  not show that context repairs judgment.**

---

## Disposition

**Items 1–3 are done in this PR** — the lineup across six surfaces, the ratchet broken, the tests
relaxed with their divergence guards kept. **This is the `panchew-io` unblock and it waited on
nothing.**

**`blocking_resolved: false`** — the CFO's enforcement declaration is outstanding by construction, and
SN-42's shape is with the Phase Chat.

**Suite 548 passed / 0 skipped**, measured 2026-08-27 **against a live ComfyUI endpoint** (`http 200`
at `localhost:8188`, restored by the CFO). **549 → 548 by one deliberate test removal**, named in
Decision 2. **No skips introduced.** Validator `VALID, 0 errors`.

> **Recorded because the figure was briefly wrong in a way nothing would have flagged.** While this
> ruling was being written the endpoint was down, and the suite read **548 passed / 1 FAILED** — an
> environmental result, not a regression. **Every `549/0` in this phase's artifacts silently assumed a
> running ComfyUI**, HQ's own repeatedly. **A suite figure should carry the environment it was
> measured in, or it is not a measurement** — offered as a candidate obligation for P12's closure
> declaration, which will quote one.

**PSG §11.6.1:** HQ-authored, no chat-level reviewer. **The CFO is the mandatory diff reviewer.**
