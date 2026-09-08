---
type: hq_ruling
steering_note_ref:
  - .ai-project/artifacts/steering-notes/2026-09-07__creation-chat__steering-note__P13-daily-fleet-operation__draft.md
concern_id: SN-47
hq_opener_ref: .ai-project/artifacts/hq-openers/2026-09-07__hq-chat-opener.md
progress_digest_ref: .ai-project/artifacts/progress-digests/2026-09-07__hq__progress-digest.md
issued_by: HQ Chat (ai-project-system)
issued_to: Layer-8/CFO (mandatory diff reviewer, PSG §11.6.1); the P13 Phase Chat
phase: P13 (this ruling opens it)
date: 2026-09-07
status: active
blocking_resolved: true
---

# HQ Ruling — P13 Opens: Daily Fleet Operation in Drivr, and the Four Things SN-47 Left Open

**Prerequisite verification (P9-M31-E31.3):** harness `claude-opus-5` vs `models.hq:
remote:claude-opus-5` — **match.** `models.hq` is unchanged by this ruling.

**Routing:** SN-47 (Creation Chat, draft) → HQ opener `2026-09-07__hq-chat-opener.md` → this
ruling → P13 phase spec → Phase Execution Chat Starter. SN-47 is **consumed** by this ruling.
Its `status: draft` is preserved as filed; consumption records which of its contents became
binding, and by what authority.

---

## 1. What SN-47 supplied, and what this ruling adds

SN-47 carried **thirteen confirmed CFO requirements** and a larger body of material marked
**[PROPOSED — confirm]**. The confirmed requirements are the CFO's input and are **not
re-litigated here**. This ruling does three things the note could not:

1. It resolves the four decisions SN-47 left open, by direct CFO answer, recorded in §2.
2. It records **four findings from verification** that change the note's own framing (§3).
3. It disposes of the digest's ten carry-forwards explicitly (§5), which SN-47 asked for and
   could not perform.

**Creation Chat authority boundary, restated:** SN-47's appearance in the record conferred no
governance authority on its author, and its marked proposals were not accepted by transmission.
Where this ruling adopts a proposal, it says so and names it as **HQ-adopted**, so a later reader
can tell a CFO decision from an HQ judgement.

---

## 2. The four open decisions, ruled

All four were put to the CFO in this session and answered directly. **These are CFO decisions,
recorded by HQ, not HQ judgements.**

### Decision 1 — `model_verification: blocking` is intentional; the rows are true

`6a52493` (2026-09-07 08:44) flipped `advisory → blocking` **after** the Progress Digest
(`06526c3`, 00:48) had disposed of that flip as *do not arm yet*, on the stated ground that
flipping while the configured rows did not describe what those chats run on *"would halt every
Phase, Milestone and Epic chat, and P13 could not open a Phase Chat at all."*

**Ruled:** the flip is **intentional and correct**. The CFO states the rows are now true — he
will open Phase, Milestone and Epic chats on the configured models. Accordingly:

- **`P12-CF-1` is CLOSED, discharged by CFO decision**, not by its original trigger condition.
  The trigger was *"arm when `models.phase`, `models.milestone` and `models.epic_manual` name
  what those chats actually run on."* The CFO has asserted that state directly. HQ records that
  it did **not** independently verify those three chats' runtime identities — it cannot, from
  here — and that the assertion is the CFO's.
- **The P13 Phase Chat runs on `remote:gpt-5.6-sol`**, not on this harness. The Phase Execution
  Chat Starter is therefore written to be **self-contained and harness-neutral**: it may not
  assume Claude Code tooling, this session's context, or any capability not stated in it.
- **Consistency obligation — and what it turned out to be hiding.** The working tree carried an
  uncommitted `models.creation: gpt-6-astra → gpt-6` edit while the committed record still said
  `gpt-6-astra`. Verifying that inconsistency before quoting Decision 1 as established uncovered
  a larger one: **`master` was red.**

  `tests/test_model_config.py::test_chat_hierarchy_manual_mapping_agrees_with_yml_block[creation]`
  requires `chat-hierarchy.md`'s "The mapping" table and `.ai-project.yml`'s `models:` block to
  agree. `2ed2a48` changed the config side and not the table side. **The suite has been 773
  passed / 1 failed since 2026-09-07 08:44** — against the **774** the Progress Digest reports at
  P12 close-out — and neither direct commit was run against it. See §3 F5.

  **Discharged by this ruling's own PR**, which commits the `creation: gpt-6` value, reconciles
  `chat-hierarchy.md` to it (v1.6.0 → **v1.7.0**, with the change recorded as a lineup change
  rather than a version refresh, superseding SN-41 on the `creation` cell only, `hq` untouched),
  corrects the now-false `.ai-project.yml` provenance comment, and restores **774 passed**.
  Decision 1 may be quoted as established once that PR merges.

### Decision 2 — Drivr gets a private remote

`/home/panchew/soft-dev/drivr` has **no remote at all** (verified: `git remote -v` empty at
`114de1c`). The digest carried this as *"Drivr has no remote,"* owner Phase/HQ, trigger
*publication-model decision*, and recorded it as a **decision, not a defect**. SN-47 filed it as
Open Decision 5, to be resolved *"during phase opening."*

**HQ rated it higher than SN-47 did, and the CFO agreed.** This framework's acceptance chain —
Stage-2 review, merge authorization, and `cfo_review_gate: enabled` — is **constructed on pull
requests**. P13 places five of its eight milestones' implementation inside Drivr. Running those
epics in a repository with no remote does not make the acceptance chain lenient; it makes it
**inoperable**, and would have produced five milestones of work that no gate could refuse.

**Ruled:** Drivr receives a **private git remote** before any milestone that changes Drivr code
opens. This preserves the substance of the prior local-only ruling — the work is not published —
while restoring PRs, Stage-2 review, merge authorization and the CFO diff gate. It also answers
SN-47 Open Decision 5's recovery half, which local-only left unsolved: **every Drivr commit
currently exists on one disk.**

**This supersedes the local-only disposition on the publication axis only.** Drivr remains
unpublished. Nothing here makes it public, and nothing here reopens the local-inference
direction, which stays parked (§5).

### Decision 3 — Eight milestones; repeatability is proven early, not last

**Ruled:** SN-47's seven candidate milestones are adopted as the starting frame with **two
contract-level amendments**. Decomposition below the contract remains the Phase Chat's.

**Amendment A — operational proof precedes surface work.** SN-47's M48 readiness is **static**:
validator runs, config parses, catalog membership. The note concedes the point itself —
*"static alignment is not operational readiness"* — and then sequences the first proof of
repeatability into **M54**, the final milestone.

The digest's sharpest finding is that **agentic dispatch has worked exactly once**: one project,
one epic, one engine, on `panchew-io`, *whose governed `models:` block had been silently reverted
by its own restructure.* Every carry-forward defect class — the silent reversion, SN-45's
enrollment gap, provider-route resolution, the credential-directory mismatch — is **invisible to
a static check and appears only in a real run.**

Readiness in P13 therefore means **a real headless Epic dispatch on `footboard` and
`home_finance` through the already-proven P12 path**, taking `n` from 1 to 3, before any UI
milestone opens. No new surface is built for it. If the path does not generalize, P13 learns that
in its first milestone rather than its last.

**Amendment B — split SN-47's M51.** As drafted it bundled three distinct risks: in-app
conversational execution, extension of dispatch from Epic through Milestone to Phase, and the
eligibility lever. The first is a **surface** change; the second is a **capability-domain**
change that reopens something P12 deliberately closed (Decision 4). A single milestone spanning
both yields a failure nobody can attribute. They are separated into M51 and M52.

Net: **eight milestones, M48–M55.**

### Decision 4 — Phase/Milestone dispatch becomes representable; authority does not

**SN-47 understated this, and the understatement mattered.** The note describes requirement 9 as
*"implementing the allowance already present in governance."* Governance does permit the mode:
`chat-hierarchy.md`'s ratified execution matrix restores Phase/Milestone agentic as a
*possibility*, and its "Mode is not authority" section records that no dispatcher yet consumes
the declaration.

But [`drivr/capabilities/model.py:20-21`](../../../../drivr/drivr/capabilities/model.py) does not
merely fail to implement it. It makes Phase/Milestone dispatch **unrepresentable by
construction** — *"`dispatch` is not constructible at `phase` or `milestone`. It is constructible
at `epic` only."* And SN-36 names that rule as **one of three exemplars** of the CFO's own design
principle, *"a rule that cannot be clicked outranks a rule that is merely written,"* beside
SN-22's manual-only Creation/HQ and "Mode is not authority."

So requirement 9 does not wire an unwired allowance. **It removes one of the three exemplars from
a closed capability domain that P12 closed on purpose**, and requirement 10's lever replaces a
structural impossibility with a toggle — a genuine downgrade in guarantee class.

**Ruled**, with the CFO's decision:

- **Dispatch becomes representable at Phase and Milestone**, gated by the eligibility lever.
- **The lever defaults to OFF** at Phase and Milestone. Enabling eligibility alone must not
  start or resume work.
- **Lever scope: per-project, with a fleet-wide default.**
- **Merge and acceptance authority stay unrepresentable by construction**, as does Creation/HQ
  manual-only (SN-22). The other two exemplars are untouched. "Mode is not authority" is
  unamended and binding: an instance running unattended holds exactly the authority its level
  always held.
- **M52 must re-derive and re-state what remains closed** after the domain is reopened. A
  capability domain that is reopened without restating its remaining closures is how the closure
  is lost by drift rather than by decision.

---

## 3. Findings from verification that amend SN-47's framing

Recorded because a later reader should not have to re-derive them.

| # | Finding | Consequence |
|---|---|---|
| F1 | The `model_verification` flip post-dates the digest that disposed against it (`6a52493` 08:44 vs `06526c3` 00:48, same day). | Not drift — a CFO decision. Ruled in Decision 1; `P12-CF-1` closed as discharged, with the record-consistency obligation attached. |
| F2 | Drivr has **no remote at all**, verified, not merely no PRs. | Elevated from SN-47's "resolve during phase opening" to a **phase entry condition**. Decision 2. |
| F3 | Phase/Milestone dispatch is **unrepresentable by construction** and is a named SN-36 exemplar — not unimplemented. | SN-47's "allowance already present" framing is corrected. Decision 4. |
| F4 | All three fleet projects hold **uncommitted** `.ai-project.yml` model additions on non-default branches (`milestone/M1`, `chore/framework-v7.0.0-bump`, `epic/E1.1`). | This is the precise state that produced the `panchew-io` silent reversion. **Phase entry condition 2**: commit them on purpose before anything else touches those repositories. |
| **F5** | **`master` has been red since `2ed2a48` (2026-09-07 08:44).** The `creation` divergence guard failed: 773 passed / 1 failed, against the digest's **774** at P12 close-out. Both direct config commits landed without the suite. | **Repaired in this ruling's PR** (Decision 1). Three things are worth recording beyond the repair. **(a) The guard worked and nothing else did** — not the commit, not the digest written seven hours earlier, not the opener, not SN-47's configuration section, which read the same file and reported it as the CFO's edit to preserve. **(b) It was found by running the suite, not by reading**, which is the same lesson as F3 arriving by a different route. **(c) It bears directly on `P12-GH-3`:** the digest's *"774 passing"* was true when written and became false four hours later, and every artifact since has carried it forward as current. That is derived-claim rot with a dated instance — **the eleventh**, and again caught downstream. |

---

## 4. Decisions HQ made where the CFO was not asked

Recorded separately and marked, so they can be corrected cheaply. **These are HQ judgements, not
CFO decisions.**

1. **Governance auto-update: readiness is required for P13 completion; the complete updater is
   not.** SN-47 left the priority open and proposed this weight itself. HQ adopts it. Readiness
   threads through M48, M52, M53 and M55 as SN-47 proposed. If the updater ships, M55
   demonstrates authorized apply and recovery; if it does not, M55 records the supported manual
   update path. **UI readiness alone may not be reported as auto-update completion.**
2. **Adoption bar: two reviewed work items per pilot project, and five working days of daily
   use after integration.** SN-47's proposed threshold, HQ-adopted. The fleet roster
   (`panchew-io`, `footboard`, `home_finance`) is the CFO's and is settled.
3. **`home_finance`'s schema errors are resolved explicitly in M48, and may not be resolved by
   silent rename.** Its `project.name` carries an underscore against a hyphenated-slug rule, and
   `project.description` is absent. M48 chooses — with evidence — between renaming the project
   with a recorded supersession and filing a schema finding against the rule. No rename is
   authorized by this ruling.
4. **The non-deterministic suite gets an owner.** Carried unowned by the digest with the
   observation that *"suite green" is the gate every closure reports against* — including P12's,
   and including P13's. A gate that passes, fails, and passes on identical commits is a
   fail-open in the acceptance chain, the same class P12 spent a phase closing. Assigned to M48.

---

## 5. Carry-forward dispositions

The digest carried ten items and asked for explicit dispositions. **None is silently absorbed
into the UI work**, per SN-47's own instruction.

| ID / item | Disposition |
|---|---|
| **`P12-CF-1`** — `model_verification` flip | **CLOSED**, discharged by CFO decision (Decision 1). Record-consistency obligation is phase entry condition 3. |
| **Drivr has no remote** | **CLOSED** by CFO decision (Decision 2). Private remote; phase entry condition 1. |
| **`panchew-io` silent `models:` reversion** | **Owned by M53.** Model selection that takes effect must make this class impossible, not merely unrepeated. **M48 verifies it has not recurred** during the entry-condition commits. |
| **Non-deterministic suite where `visual_artifacts.enabled: true`** | **Owned by M48** (§4 item 4). It gates every acceptance in this phase. |
| **`P10-GH-7`** — block detection untrustworthy both ways | **Owned by M51.** Activity and intervention handling must preserve the distinction between missing evidence and a confirmed blocker. `undetermined` keeps its own visible state and may not render as *in progress*. |
| **`P12-GH-4`** — ungoverned inter-chat channel (remainder) | **Owned by M51**, narrowly: the conversational handoff. **Chat text may not become an authorization channel.** The bounded-exchange ruling (purpose, round cap, terminating condition) stands. |
| **SN-45 enrollment gap** — the framework assumes a configured remote; `bin/ai-project-init` establishes none | **Owned by M48**, verified again at M55. Directly implicated by Decision 2, which is the same defect met from the other side. |
| **`P12-GH-3`** — derived-claim rot | **Carried, unowned. Explicitly not absorbed.** P13 does not scope it. Its trigger stands. Noted: this ruling committed one instance of the class and caught it (Decision 1's consistency obligation), which is the tenth-plus dated instance and again caught downstream rather than by a check. |
| **`P12-GH-5`** — declared context exceeds loaded | **Stays parked** with local inference. M54's measurement examines the current workflow and **does not reopen it**. |
| **Delivery Notice location split** (corpus bi-located, no test catches it) | **Carried, unowned.** Not absorbed. Wants a filing, not a UI milestone. |
| **Duplicate `Error Handling` content in the AOG** | **Carried, unowned.** E44.4 was scoped to titles; the content repair is unscheduled. |
| **Closed-phase sweep scope** | **Carried.** Wants a ruling *before* a sweep asks. P13 triggers no sweep, so it is not ruled here. |
| **`P11-GH-2` sibling pattern; `rulings` untemplated** | **Carried, still unplaced.** Both have now survived three phases, and **both implicate HQ, which is why HQ has again not placed them.** Recorded: this ruling is issued into the untemplated class, making at least twelve. This is a CFO placement, not an HQ one. |

**Restated, not reopened:** llama.cpp and any non-Ollama local runtime is **CLOSED** by CFO
decision. **Local inference is PARKED**, re-entry conditional on agentic runs working properly —
which is precisely what M48 measures, so P13 may generate the re-entry evidence without
re-entering. Row P4 parks with it. `local-agent-runner`'s retention stands.

**Out of scope, restated:** git-history investigation or rewriting. The requested repository work
protects **future** commits. No exposure has been established by any pass to date.

---

## 6. What the Phase Chat receives

1. This ruling.
2. `docs/phases/P13__Daily_Fleet_Operation_in_Drivr/P13__phase-spec.md`.
3. `docs/phases/P13__Daily_Fleet_Operation_in_Drivr/P13__phase-execution-chat-starter.md`.

The Phase Chat verifies the current baseline, confirms the entry conditions are met, and
finalizes milestone decomposition **within this ruling's contract**. It may not reopen §2's four
CFO decisions. It may propose corrections to §4's four HQ judgements, which are marked precisely
so that it can.

---

## 7. One observation, recorded because it bears on how P13 is run

P12 closed on the statement that its `P12-GH-3` instances were **all caught downstream, none by
a check, and four were HQ's own** — with the design requirement that *"whatever this project
builds to catch premise-dependents, it should assume the author cannot run it on themselves."*

**This ruling is a fresh specimen.** SN-47 asserted that extending dispatch to Milestone and
Phase implements an allowance already present. That premise was false in the way that matters,
and it was not caught by the Creation Chat that wrote it, nor by the opener that carried it. It
was caught by reading `drivr/capabilities/model.py`. **The check that worked was going to the
source; the check that failed was every reading of the prose.**

P13 builds a surface whose entire value is telling the CFO what is true about work he is not
watching. It should assume the same thing about itself.

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-09-07 | Initial ruling. Opens P13. Consumes SN-47. Records four CFO decisions (§2), four verification findings that amend SN-47's framing (§3), four marked HQ judgements (§4), and explicit dispositions for all thirteen carried items (§5). |
