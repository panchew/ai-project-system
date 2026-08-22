---
project: ai-project-system
phase: P12
milestone: M41
type: stage2-acceptance-log
status: active
last_updated: 2026-08-21
---

# P12-M41 — Stage-2 Acceptance Log

**Why this file exists.** `#229` (merged `ad6e3f1`) **suspends accept-by-silence for M41** while more
than one session may hold its Stage-2. Under the suspension **an epic delivery is accepted only by an
explicit, committed acceptance — silence accepts nothing.** This log is that record: one row per
delivery, each carrying the **session UUID** of the accepting chat.

**A role is what gets duplicated; an author is not.** The UUID is the point of the entry, not
decoration.

**When the suspension lapses** — on the CFO's recorded naming of M41's holder — §11.6's
accept-by-silence returns for the happy path. **This chat will keep writing the UUID anyway**, by
choice rather than obligation: it costs one line, and it is what made the M41 fork legible.

---

## Acceptances

| Epic | Delivery | Decision | Accepting session | Date |
|---|---|---|---|---|
| **E41.2** | PR **#231**, `epic/P12-M41-E41.2` @ `ce4f1c8` | **ACCEPTED** — two escalations routed upward, no rework consumed | `1b70b020-4734-45ac-a514-8e4e0ba7d40c` | 2026-08-22 |
| **E41.1** | PR **#230**, `epic/P12-M41-E41.1` @ **`e2e26e4`** (accepted at `bdbbd36`; annotations actioned) | **ACCEPTED** — with two annotations, neither a rework attempt | `1b70b020-4734-45ac-a514-8e4e0ba7d40c` | 2026-08-21 |

---

## E41.1 — the review behind the decision

**Re-measured, not taken on report (G2).** The executor's report is not the evidence, and this chat
verified the load-bearing claims itself:

| Claim | Re-measured by this chat | Result |
|---|---|---|
| PR mergeable, 0 drift | `gh pr view 230`; `rev-list --count` vs `origin/master` | **MERGEABLE, 0 behind** |
| Four artifacts committed | `git cat-file -e` on the epic branch | **4 of 4 tracked** |
| The epic did not edit its own spec | `git log $M..$E -- …E41.1__spec__*` | **empty — clean** |
| Both 27b declared, `limit.context` observed | live `~/.config/opencode/opencode.json` | **`qwen3.8:27b` and `qwen3.6:27b` at 32768, `tool_call: true`** |
| Four pre-existing entries untouched | same file, 6 entries total | **4 pre-existing values unchanged, incl. the recorded `qwen3-coder:30b` 262144 overpack** |
| Second overpack (`llama3.1:8b`) | same file | **declares 131072 — confirmed** |
| Suite green, delta 0 | `PYTHONPATH=. pytest -q` on the epic branch | **549 passed / 0 failed** |

**Acceptance criteria — all five met.** D1 complete with no product name surviving as an unresolved
value; **D2 Part B (binding) recorded on all three columns for all five verification targets**;
D3/D4 with the out-of-repo boundary stated; D5 answering R4 **by running it**; D6 escalating four
items with **nothing substituted**.

### Annotation 1 — the binding table is superseded in place by a section 400 lines away

**§2.3's Part B table still reads `UNKNOWN / UNKNOWN / UNKNOWN` for `phase` and `milestone`.** It is
superseded by **§9.3's corrected table**, where all five confirm.

**This is handled better than any prior instance in this milestone** — there is a ⚠ banner at the
head of the record and a superseded-claims table at §9.2 naming the false statements explicitly.
**Keeping the account rather than rewriting it is the right discipline** and is not in question.

**But §2.3 is the *binding* table, and E41.5 is the artifact that will read it.** A reader who lands
on the acceptance criterion's own table gets the withdrawn answer. **Add an in-place supersession
marker at §2.3 pointing to §9.3.** One line. **Not a rework attempt** — the result is correct, the
correction is present, and the substance is complete.

### Annotation 2 — the consequence is not this epic's to draw, and the record already knows it

The delivery **message** states that *"phase/milestone are no longer blocked on surface existence."*
**The record does not say that, and is right not to.** §2.3.2 bounds itself precisely:

> *"Verified for `opencode run`. The interactive TUI was not separately verified… Whether a human
> would choose to drive a governance chat through OpenCode is a separate question this epic does not
> answer."*

**That boundary is the correct one and it is load-bearing.** R6's trigger speaks of a **surface a
manual verification chat opens on**; what is confirmed is that **`opencode run` dispatches the model
and it self-reports.** Those may or may not be the same thing — **it is the transport-versus-surface
distinction (E41.4's U2) arriving on the rows it was predicted for.**

> ### ⚠ CORRECTION TO THIS ANNOTATION — 2026-08-21, and the Epic Chat found it, not this chat
>
> **Annotation 2 as first written said the record *"does not say that, and is right not to."* That
> was FALSE, and the epic corrected me.**
>
> §2.3.2 bounded the claim, and this chat checked §2.3.2. **But `bdbbd36`'s §9.3 — the corrected
> table, the one E41.5 actually reads — carried the unbounded sentence verbatim** at line 650:
> *"All five manual verification targets now confirm on both halves of the HQ manual-surface rule."*
> **Verified by this chat against `bdbbd36` after the epic raised it.**
>
> **So the overclaim was in the artifact, not only in the summary**, on the exact surface E41.5
> consumes — and the failure mode was concrete: E41.5 lands on §9.3, reads *all five confirm*, and
> widens its landing set before HQ has ruled.
>
> **The epic applied this log's own Annotation 1 logic back at it:** *the binding surface must not
> carry a claim that has been narrowed elsewhere.* It then changed the artifact **after acceptance
> and against this chat's explicit "nothing for you to fix"**, and **flagged it rather than burying
> it in the diff**, offering to revert.
>
> **RATIFIED, not reverted.** `e2e26e4`, record **v1.3.1**: +40 / −4, the four removed lines being
> the sentence qualified in place, no measurement, table, or D-result touched — re-measured by this
> chat, not taken on report. §2.3 additionally carries **seven** in-place `SUPERSEDED → §9.3`
> markers, one per superseded cell, because *"a banner is skippable by anyone scanning straight to
> the table, which is exactly the reading pattern that made this worth fixing."*
>
> **And the pattern fired in this chat's own review.** *A premise has dependents, and the correction
> does not find them* — this log checked the instance in front of it (§2.3.2) and not the premise's
> other dependent (§9.3). **Fifth instance in this milestone, first inside a Stage-2 review.** The
> level below caught the level above, which is the direction the record claims this chain works in.

**So: the measurement is ACCEPTED. The consequence is ESCALATED.** Whether these confirmations
satisfy R6's carry-forward trigger — and therefore whether E41.5's landing set widens beyond
`creation` — is **HQ's ruling**, not this epic's and not this chat's. **E41.5's deliverable 1 is
unchanged until HQ says otherwise.**

### Post-acceptance rounds 2 and 3 — ratified, and why round 3 was more than accurate

**`e2e26e4` (round 2)** is recorded in the correction block above: the epic fixed the stale-optimistic
sentence at §9.3 against this chat's explicit *"nothing for you to fix"*, and was right.

**`e95cf07` (round 3) — RATIFIED, and the reasoning matters more than the accuracy.** Re-measured
here: +25 / −8, the removed lines being stale claims **replaced by marked versions preserving the
original text struck through**; no measurement, table, or D-result touched; suite 549/0.

It marked two further superseded sections — §2.2's Part A remote table (`NO` for `phase` and
`milestone`) and §2.3.3's R6b table (`CANDIDATE — blocked on a working credential`). **Both
stale-PESSIMISTIC, and §2.3.3 is the R6b analysis HQ was actively reading while ruling on R6's
trigger.**

> **An artifact understating its own confirmed evidence, in front of the body about to rule on that
> evidence, is worse than the optimistic case.** A stale-optimistic claim widens a landing set; a
> stale-pessimistic one **suppresses evidence at the moment of decision.**

**And the fix anticipated how it could be misused.** The epic bound the chat-surface question **into
the same block** as the correction, so **correcting an understatement could not become a back door to
widening the landing set.** That is the property that made it ratifiable rather than merely correct,
and it is recorded here at HQ's request.

**Boundary set with the ratification:** the artifact is consistent as of `e95cf07`; further unbidden
post-acceptance edits come to this chat first, because **an artifact that keeps changing gives the
CFO no stable object to diff-review** while #230 is in front of him. Time-critical exceptions are
handled as round 3 was — act, then flag immediately.

### R6's trigger — where it actually rests, after two corrections in both directions

| Ground | Status |
|---|---|
| **Runs the model** | **MET, comprehensively.** All five targets answer. |
| **Emits a readable self-report** | **MET AT THE MECHANISM LEVEL.** OpenCode injects from **router-side identifiers** (`${i.providerID}/${i.api.id}`), verified in the binary independently by the epic, by this chat, and by HQ. **Not a model describing itself.** HQ's contrary ground was **withdrawn.** |
| **A surface a manual chat OPENS ON** | **UNMET — and not measurable.** *"Whether a human would choose to drive a governance chat through OpenCode"* is a judgment about what the CFO is willing to operate in. **HQ has put that question to him directly.** |

**No TUI measurement is commissioned, and deliberately so** — it would produce a fact that does not
answer the question.

> **⚠ Sequencing, stated because it will matter later.** HQ's verification boundary is that it
> confirmed the template exists and is router-interpolated, **not that an interactive session invokes
> that same code path** — *"very likely shared, but very likely is not measured."* **That gap is not
> a prerequisite of the CFO's decision. It IS a prerequisite of the landing.** If he says yes,
> **E41.5 must not land `phase` or `milestone` until the interactive path is confirmed to inject** —
> otherwise the rows arm a check against a surface nobody has shown emits the identity it will be
> checked against. **One grep, and it belongs before the edit, not after.**

**E41.5's deliverable 1 remains unchanged. Landing set remains `creation`.**

### Rework accounting

**No rework attempt is consumed.** Attempt 1 of 3 stands, per the CFO's ruling of 2026-08-21: the
limit governs **rejections after review**, and E41.1's two self-corrections were **self-corrections
before review ruled**. **This acceptance is not a rejection**, and its two annotations are
corrections to the record, not to the work.

### Carried up from this delivery

1. **A second, unrecorded context overpack** — `llama3.1:8b` declares 131072 against 32768 loaded, a
   **4× overpack** on the same shape as `qwen3-coder:30b`'s 8×. Correctly left untouched. **No `GH-`
   ID allocated** — allocation requires escalating first.
2. **The snap `XDG_DATA_HOME` trap.** Drivr's `OpenCodeAdapter` sets `XDG_CONFIG_HOME` and **never
   `XDG_DATA_HOME`**, so a credentialed Drivr run hits exactly this. **Invisible so far only because
   every dispatch to date has been Ollama, which needs no credential.**
3. **A refusal to quote is not an absence.** Both remote targets refused *"quote your instructions"*
   while answering *"what model are you?"* immediately. **A check phrased as quotation can fail
   closed against a fully compliant target** — bears on M44's repair and on how E41.5 arms these rows.
4. **`.ai-project.yml` cannot express the provider.** `deepseek-v4-flash` resolves through both
   `opencode/` and `opencode-go/`, so `remote:deepseek-v4-flash` records **which model, not which
   route.** **This record's §9.5 is the only artifact carrying the route** — E41.5 must cite it
   rather than restate it.


---

## E41.2 — the review behind the decision

**Re-measured, not taken on report (G2).**

| Claim | Re-measured by this chat | Result |
|---|---|---|
| PR mergeable, no drift | `gh pr view 231`; `rev-list` vs `origin/master` | **MERGEABLE, 0 behind, head `ce4f1c8`** |
| Artifacts committed | `git cat-file -e` on the epic branch | **3 of 3 tracked** |
| Epic did not edit its own spec | `git log $M..$E -- …E41.2__spec__*` | **empty — clean** |
| **The bar predates the runs** | `git log --reverse` on the branch | **D3 `c9c2fb4` at 12:26; first live run `57554c3` at 12:53** — **27 minutes, as history** |
| **The tasks predate the runs** | same | **D4 inputs `4ce9efa` at 12:39 — 14 minutes** |
| Replay, both directions | record §, lines 96–100 | **3 flagged / 2 passed with counts** |
| Floor version stated | record §2 | **`per-lane-ruled-2026-08-20`, stamped by the instrument** |
| Directional checks exist | record §, D4 inputs | **`tests_passed/20` (dev), `catches` 0–5 (qa)** |
| Suite | `PYTHONPATH=. pytest -q` on the epic branch | **570 passed / 0 failed**, +21, all in one new file |

**Acceptance criteria — met, including the two this chat widened.**

- **S1's both-directions requirement is satisfied by measurement, not assertion**: E33.2 Run A, E39.3 and RUN2 **flagged**; **E33.2 Run B (10 rounds / 2 files) and E33.4 (10 rounds / 3 files / 4-of-4) passed.** An instrument that returned `FAIL` unconditionally would have failed here.
- **T3's directional check is present and was committed with the tasks, before any run** — the requirement this chat placed on E41.2 at v1.0.2, discharged in the order that makes it meaningful.
- **S5's ruled per-lane floor was applied and its version stated**, so a reader can tell which bar judged which run. **The `epic_qa` verdict was reached, not withheld** — correct, since S5 is ruled.

### The result that is worth more than the replay

**DEV RUN 2 is a live successful-nothing on the incumbent, captured 2026-08-22** — exit 0, `completed`, **4.2 s, 55 tokens, 0 tool rounds, 0/20 directional**, stub byte-identical, **with six tools genuinely advertised.** The model emitted its call in `<function=…>` syntax and the parser took the message as a final answer.

> **E33.2 Run A's mechanism, on a different model, found live.** The instrument flagged **an instance it was not built against** — which is a stronger validation than any replay, because the replay set could in principle have been fitted to its own cases and this could not.

**And the second instrument self-correction is its mirror:** the checker read a bare `/` inside a correct finding and **failed an honest read-only run.** **Only a live run could have found that** — a false positive in a detector built to catch false negatives.

### Rework accounting

**No attempt consumed. Attempt 1 of 3 stands.** Both instrument corrections were **self-corrections before review ruled**, which is E41.1's precedent and the CFO's ruling of 2026-08-21: the limit governs **rejections after review.**

### Two escalations routed upward — neither decided here, both blocking E41.3's candidate runs

**(a) The `epic_dev` baseline is BIMODAL on identical inputs — `{PASS 9/20, FAIL 0/20}`.**
*"No worse than the incumbent on every objective check"* **has no single number to attach to**, and the epic records that four aggregation rules give four answers. **It measured and stopped rather than choosing one after seeing the data** — which is bar-committed-first applied to itself.
**Above this chat: the bar's shape is Binding Constraint 6, the CFO's, ratified in SN-36/37.** Escalated to the Phase Chat.

**(b) The baselines are HOST baselines, not sandbox baselines.** Docker was present but `bin/ai-project-orchestrator` never ran, so `:392-397` could not fire — **and the fallback executes on the host exactly as these runs did, so the baselines are equivalent to the fail-open path rather than protected from it.**
**Above this chat: it touches the M42 gate's attributability rationale**, which is phase-level and CFO-ruled. Escalated to the Phase Chat.

**What this chat binds meanwhile, without deciding either:** **E41.3 must dispatch identically to E41.2 or the comparison is void**, and **if M42 changes the lane, these baselines are re-measured rather than reinterpreted.**
