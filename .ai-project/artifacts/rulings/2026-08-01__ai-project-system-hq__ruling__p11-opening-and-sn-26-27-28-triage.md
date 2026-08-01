---
type: hq_ruling
steering_note_ref:
  - .ai-project/artifacts/steering-notes/2026-07-31__creation-chat__steering-note__P11-drivr-spine.md
  - .ai-project/artifacts/steering-notes/2026-07-31__creation-chat__steering-note__creation-reinstantiation-ritual.md
  - .ai-project/artifacts/steering-notes/2026-08-01__creation-chat__steering-note__sn-numbering-unenforced.md
concern_id: SN-27 (+ Amendment 1), SN-26, SN-28
hq_opener_ref: .ai-project/artifacts/hq-openers/2026-08-01__hq-chat-opener.md
issued_by: HQ Chat (ai-project-system)
issued_to: Layer-8/CFO (mandatory diff reviewer, PSG §11.6.1); the P11 Phase Chat
phase: P11 (opened by this ruling)
date: 2026-08-01
status: active
blocking_resolved: true
---

# HQ Ruling — P11 Opens on the SN-27 Spine; SN-26 and SN-28 Placed; the Namespace Question Answered

**Steering Notes:** SN-27 + Amendment 1 (P11 spine), SN-26 (Creation Chat re-instantiation ritual),
SN-28 (Steering Note ID allocation unenforced). All three carried by the 2026-08-01 HQ Chat Opener.

**Prerequisite verification (P9-M31-E31.3):** harness-reported model `claude-opus-5` vs
`.ai-project.yml` `models.hq: remote:claude-opus-5` — **match.** No mismatch; proceeding.

The eight binding decisions in SN-27, its four Amendment-1 decisions, the CFO's two 2026-08-01
rulings recorded in SN-28, and the CFO decisions recorded in SN-26 are **not re-decided here.**
What HQ owes is the phase, the milestone shape, the placements, and the constraints — plus the one
question SN-28 addressed to HQ directly.

---

## Decision 1 — P11 is opened on the SN-27 spine, with four milestones

**Phase P11 — Drivr: Coordination over Rented Execution.**
Spec: `docs/phases/P11__Drivr_Coordination_Over_Rented_Execution/P11__phase-spec.md`.
Starter: `docs/phases/P11__Drivr_Coordination_Over_Rented_Execution/P11__phase-execution-chat-starter.md`.

| # | Milestone | Why it sits where it sits |
|---|---|---|
| **M36** | Record Integrity and Documentation Hygiene | CFO-decided as first (Decision 2). Zero dependency on Drivr; lands before any Drivr code exists, and lands governed. |
| **M37** | Drivr Inception, Fleet Registry, and the Execution Adapter Surface | The Drivr repository **does not exist** (`~/soft-dev` verified, 2026-08-01). Nothing downstream can be built until it does, is enrolled, and can invoke one CLI engine. |
| **M38** | Trustworthy Completion Signal (P10-GH-7) | Sequenced **after** M37 because it needs a real adapter to measure, and **before** M39 because M39 dispatches. This is the SN-27 Required action, honoured literally. |
| **M39** | Coordination: Scheduler, Derived Gate Queue, and the Thin Surface | The first thing in the phase that dispatches unattended runs. Gated on M38. |

**M36 → M37 → M38 → M39 is a binding order**, and the binding is not stylistic: M38 exists to make
M39 safe, and M37 exists to give M38 something to measure. M36 is first by CFO ruling.

**HQ did not self-scope this.** The spine is SN-27's; the first milestone's content and position are
the CFO's; the decomposition into four milestones is HQ's own call and is the thing HQ is for.

---

## Decision 2 — M36 is documentation hygiene, first, and its contents are fixed

Per the CFO's 2026-08-01 ruling recorded in SN-28 ("Resolved — before P11, or inside it? Both, split
by kind"), M36 carries four self-contained items:

1. **SN-28 Required actions 1–3** — the namespace answer (now supplied by Decision 3 below, to be
   *applied*, not re-derived), the SN-23 citation fix, and an ID allocation rule.
2. **SN-26** — reconcile the three disagreeing Creation Chat re-instantiation surfaces; decide
   whether this project renders its own `genesis.md` and whether a Project Brief is expected; ensure
   whatever path is canonized carries the E31.3 check **on the path itself**.
3. **The SN-1 System HQ codification** — already ruled 2026-07-31
   (`.ai-project/artifacts/rulings/2026-07-31__ai-project-system-hq__ruling__system-hq-routing-codification.md`,
   D1–D4 accepted). M36 *executes* it. Its DoD items travel unchanged: the byte-level Authority
   Boundary agreement check across three documents, the issuer-vs-scribe rule, reuse of
   `steering_note` for the routed-to-B leg.
4. **SN-26's re-diagnosis of P10-GH-2** — amend the carry-forward text (Decision 8 below).

**The ordering constraint inside M36 is binding:** the namespace question is answered *before* any
renumbering is specified. Decision 3 answers it, so M36 inherits an answer rather than a question —
but no epic may renumber anything on its own initiative.

**Why the CFO's ordering was right and is recorded so it is not re-litigated:** the CFO wanted
everything cleaned before P11 opened; the Creation Chat objected that amending
`AI-OPERATING-GUIDELINES.md`, `chat-hierarchy.md` and `artifact-communication-protocol.md` outside
any phase would be ungoverned work in the repository whose thesis is that work is governed. The
ruling takes both. HQ adds nothing to it.

---

## Decision 3 — The namespace question, ANSWERED: the directory is the sequence

SN-28 Required action 1 asked HQ directly: *does System HQ, as a distinct entity, maintain its own
Steering Note sequence?*

**No. One sequence per steering-note directory, regardless of issuing entity.**

A note filed into `<project>/.ai-project/artifacts/steering-notes/` takes the next free `SN-<n>` in
that directory, whoever issued it. Sub-IDs keep the existing letter-suffix form (`SN-12a`).

**The reason, which is the load-bearing part.** An identifier's only job is to be unambiguous *in
the space where it is cited*, and the space where these are cited is the directory. Entity
provenance is **already recorded twice** — in `issuer_chat` and in the filename's entity slug
(`2026-07-31__layer-8-cfo__steering-note__…`). Adding a second ID space to the same directory would
put the provenance a third time into the identifier, and would oblige every future citation to
carry a namespace prefix to be readable. That is the same cost as the collision it avoids, paid on
every note forever rather than once.

This is the third application of a rule this repository has now made twice — *governance names the
tier, routing names the model*; *governance names the role, P11 names the thing that runs it*. Here:
**the record names the issuer; the identifier names nothing but position.**

**Consequence:** `2026-07-31__layer-8-cfo__steering-note__system-hq-routing-model.md` is
**misnumbered**. It takes the next free ID at M36 execution time. Its two existing citations — the
2026-07-31 Progress Digest and the 2026-07-31 System HQ codification ruling — are amended with a
footnote recording the old number, so the rename is traceable rather than silent.

---

## Decision 4 — SN-23 is NOT renumbered; citations carry the date. And the rule that makes this consistent with Decision 3

SN-28 Required action 2 proposed date-qualified citations rather than renumbering, tagged
`[PROPOSED — confirm]`. **HQ ratifies it.** This is method for executing a fix the CFO already
directed, not new direction, so it is HQ's to rule on — and it is subject to the CFO's §11.6.1 diff
review like everything else in this ruling.

Renumbering one collision and not the other is only defensible if a rule separates them. The rule:

> **A bookkeeping defect never rewrites a citation in a normative document.** Where a colliding ID
> is cited only in project-internal, non-normative artifacts, renumber. Where it is cited in the
> normative tier, date-qualify the citations and leave the collision visible.

- **SN-1** is cited in two non-normative artifacts (a digest, a ruling). Renumber — cheap, contained.
- **SN-23** is cited in `AI-OPERATING-GUIDELINES.md`, `artifact-communication-protocol.md`,
  `chat-hierarchy.md`, `fleet-operator.md` and `fleet-operator-brief.md`. Renumbering silently
  invalidates every one of them and launders a record whose honesty is the point. Date-qualify:
  `SN-23 (2026-07-18)` for reference-first / platform agnosticism, `SN-23 (2026-07-20)` for the P10
  adoption spine. Fix the citing documents; leave both notes' IDs alone.

SN-27 itself cites *"SN-23 Ratified Decision #7"* meaning the 2026-07-20 note. M36 fixes that
citation too — the phase spec below already carries it date-qualified.

---

## Decision 5 — The duplicate-ID test is authorized as Bugfix **B3.1**. HQ delegates execution; HQ does not perform it

SN-28 Required action 4, CFO-classified as a hotfix. HQ authorizes it and files the spec:
`docs/bugfixes/B3.1__spec__steering-note-id-allocation-unenforced.md`.

**Vehicle: the Bugfix Epic (`governance/systems/bugfix-epic-workflow.md`, `docs/bugfixes/README.md`),
not an unplanned branch.** PSG §8A branches are explicitly *proposals with no authority, integrable
only via a planned Epic* — the opposite of what a hotfix needs. The Bugfix Epic is the repository's
own governed expedited path, precedented here by B4.1, and it requires exactly what the CFO's
carve-out described: a minimal spec, direct HQ authorization, `bugfix/B3.1`, a merge that HQ
approves.

**Severity `medium` → `B3.1`.** The B-scheme's first digit encodes severity, not phase
(`docs/bugfixes/README.md` supersedes the older phase-encoding). The defect this bugfix fixes is
*allocation has no enforcement* — limited impact with a manual workaround. The **High** rating SN-28
carries belongs to the SN-23 citation trap, which this bugfix does not touch and M36 does.

**HQ does not write the test.** `governance/systems/hq-chat.md` is unambiguous — HQ is not a Coding
Agent and does not modify source files — and a ruling that suspended that rule for its own
convenience would be worth less than the test. **The bugfix is delegated to an Epic-mode Coding
Agent**, dispatched by the CFO from the filed spec. HQ authored the spec and the authorization;
those are HQ artifacts. `tests/` is not.

**B3.1 may land before M36 opens.** That is the whole point of the carve-out. It is bounded by the
property the CFO named: it adds a test and changes no normative text. **The moment an item in this
bucket would edit a governance document it leaves the bucket and goes to M36.**

---

## Decision 6 — P10-GH-7 is in scope, owned by M38, and nothing dispatches before it closes

SN-27's Required action is honoured as written, with the sequencing made structural rather than
advisory: **M38 exists for it, and M39 cannot begin until M38 delivers.**

The evidence is two independent engines, which is why this is not a carry-forward:

- **This stack:** E33.2 Run A — exit 0, zero work. E33.4 — exit 2, complete green work. *The exit
  code is not a completion signal here.*
- **OpenCode:** `run` exits 0 on session errors (`anomalyco/opencode` #14551) — the same failure
  mode, in a dependency the CFO does not own.
- **G11 stands at zero captured `epic_qa` runs.** The lane that would supply a trustworthy signal
  has never been exercised. M38 exercises it.

Amendment A1.5 sharpens rather than changes this: if OpenCode becomes the sole engine, the problem
**concentrates** — better for diagnosis, worse for control. M38's deliverable is therefore not "fix
the exit code" but **a completion judgment that does not rest on the exit code alone**, plus the
first captured `epic_qa` runs.

---

## Decision 7 — The llama.cpp trial is recorded CLOSED, not parked

Per Amendment A1.3. Its Mac-class-hardware trigger is **void** — the item is closed by CFO decision,
not waiting on hardware. **The local-inference runtime question is closed; Ollama is settled, not
provisionally chosen.** P10's parked-on-trigger entry does not carry into P11 and no future phase
re-inherits it.

Distinct and deliberately preserved: **the model roster stays open** (A1.4). Two live questions —
whether `qwen3-coder:30b` can hold a *milestone's* context, and whether a newer open-weights model
does better. The first is placed in M37 as a **fourth axis** beside row P4's G-P4-a/b/c gates.
**Row P4's 2026-07-31 ruling is not reopened**; M37 gathers evidence and does not decide it.

---

## Decision 8 — P10-GH-2 is re-diagnosed; the carry-forward text is amended in M36

SN-26's evidence holds and HQ accepts it. P10-GH-2 is recorded as *"the Creation Chat Seed does not
implement the E31.3 model-verification check."* That premise is false: `governance/templates/seed.md`
has carried the Prerequisite Verification section since `d7ee7cd` (2026-07-19), nine days before the
ruling that filed the gap, and the 2026-07-31 Creation Chat session — opened from `seed.md` — ran
the check.

The real gap is that `creation-chat-guide.md`'s re-instantiation ritual hands a session three
artifacts, **none of which carries a model check**, because the only one that would (`genesis.md`)
does not exist in this project. **As filed, P10-GH-2 points a future owner at a file that needs no
change, and the actual defect would survive the fix.** M36 amends the carry-forward text so the
re-diagnosis travels with the item.

---

## Decision 9 — SN-26 is recorded and placed; it did not shape the spine

Per its own binding CFO decision, SN-26 is tightening, not phase scope. It shaped nothing in
Decision 1. It is placed in M36 **alongside** — not merged into — the SN-1 codification, as SN-26
Next Action 3 asks. Its Carry-Over 1 working practice (open Creation Chats with Seed + latest
Steering Note + latest Progress Digest) stays **working practice, not canon**, until M36 canonizes
whatever it canonizes.

---

## Decision 10 — The seven `[PROPOSED — confirm]` items are returned to the CFO, unacted

SN-27 carries seven items authored by the Creation Chat, not the CFO. HQ does not convert a proposal
into spine by placing it. **Returned:**

1. Drivr may *propose* a fleet-state transition but never execute one.
2. The `local-agent-runner` retention bar (*"names a capability P11 needs that OpenCode does not
   provide"*) and its two candidate capabilities.
3. Model-watch as cheap re-tests against E35.5's existing harness rather than scheduled
   investigations.
4. The engine-comparison spike (OpenCode `run` vs `local-agent-runner` on the latter's own `proof/`
   fixture, same model, same host).
5. Placement of SN-1 and SN-26 together in a documentation milestone.
6. P9-GH-1 owner assigned at the dispatch-touching milestone.
7. `ai-stack` / `character-factory` resolved via registry classification.

**Items 5, 6 and 7 are additionally recorded as HQ's own independent decisions** — Decision 2,
Decision 11, and the M37 registry scope respectively. They arrive at the same place the proposals
did, but they arrive on HQ's authority, not by treating an unconfirmed proposal as binding. That
distinction is the whole reason for returning them.

Items 1, 2, 3 and 4 remain **open and unowned**. The phase spec records each as awaiting the CFO and
**names what the affected milestone does if no answer arrives** — no milestone is blocked on a
proposal.

---

## Decision 11 — Carry-forward triage

| Item | Disposition |
|---|---|
| **P10-GH-7** (High) — block detection untrustworthy two-sided + G11 | **In scope. M38 owns it.** Decision 6. |
| **P9-GH-1** (Medium, raised) / **P10-GH-9** (High, trigger-gated) — merge-auth routing; agentic parents × default-accept | **Owner assigned at M39**, the milestone that first wires Phase/Milestone agentic dispatch — which is P10-GH-9's own recorded trigger. Not at phase open: assigning an owner before the trigger fires is bookkeeping, not protection. |
| **P10-GH-5** (Medium) — `ai-project-yml-spec.md` §4 normative but unenforced | **Folded into M37.** The three-state registry reads every enrolled project's `.ai-project.yml`. A registry built over configs that degrade quietly is the same defect class as a scheduler built over an untrustworthy exit code — and 3 of 6 enrolled configs were invalid at P10 close. |
| **P10-GH-1** (Low) — `framework_version` convention-only, not in the yml spec | **Conditional fold-in to M37**, at the Phase Chat's judgment: if the registry reads `framework_version` normatively, schema-bless it in the same pass. If it does not, leave it parked. |
| **P9-GH-3** (Low) — within-session segmentation | Parked, unchanged. Row P4 does not wait on it. |
| **P10-GH-3** (Low) — row P1 vs live `creation` key | Parked, unchanged. |
| **P10-GH-4** (Low) — `delivery_notice.merge_details` unfillable | Parked. Settled practice, four candidate directions recorded, no recommendation. |
| **P10-GH-6** (Low) — starter-lint false positive | Parked. A framework-capability change; enters only on friction. |
| **P10-GH-8** (Low) — `governance/systems/` versions/changelogs inconsistent | Parked. It is a corpus-wide convention change, and M36 is a documentation-hygiene milestone — the Phase Chat MAY propose folding it in, but HQ does not mandate it: M36 already carries four items and the CFO scoped it to those. |
| **P10-GH-10** (Medium) — flaky `test_artifact_router.py` test | Parked, but **named in M38's context**: M38's evidence is suite-shaped, and "full suite green" is weaker evidence while a ~10%-flaky test sits in it. Not scoped; flagged. |
| **P8-GH-2** (Low), **ComfyUI precision investigation** | Restated deferred on their existing triggers, unchanged since P9. |
| **Competing-model code review** | **Un-parked** (SN-27 decision 7 / recorded consequence). It has a shape and an authority ceiling now. **M39 owns it.** |
| **Sidekick-for-external-projects** | Unchanged. A Brief-level identity question, not phase scope. |

---

## Decision 12 — SN-28 Carry-Over 3 is a bounded audit in M36 with a stated decision point

SN-28 audited **only** steering notes. Rulings, escalation notices, and the `GH-` gap-record series
allocate IDs the same unenforced way, and `GH-` is cited far more widely than `SN-`.

**M36 performs the audit and stops there.** The audit is cheap and bounded. What it finds may not be:
if a second family shows collisions reaching the normative tier, **that is an escalation to HQ, not a
scope expansion the milestone absorbs.** M36's DoD includes the audit and a recorded finding; it does
not include fixing whatever the audit turns up.

Stated plainly because SN-28 warned it may widen the milestone: **it may not widen it. It may only
report.**

---

## Note on the review diagram

`governance/systems/hq-chat.md` ("Review Diagram on HQ Rulings") makes a Structural diagram a
**SHOULD** for rulings that **amend a normative document**, and says explicitly that a triage,
placement or disposition needs none — *"one is worse than none if it adds a box that the ruling's
text does not support."*

**This ruling amends no normative document.** It opens a phase, places work, answers a question, and
authorizes a bugfix. Every claim in it is a placement, verifiable by reading the phase spec's
milestone table against this ruling's Decision 1 — a diagram would restate that table, not shorten
the reviewer's path to it. **No diagram, deliberately.** M36's own deliveries — which *do* amend
`AI-OPERATING-GUIDELINES.md`, `chat-hierarchy.md`, `artifact-communication-protocol.md`,
`system-hq.md` and `creation-chat-guide.md` — carry the obligation instead, and the phase spec
records it as a DoD item there.

---

## Disposition

**P11 opened.** SN-27 + Amendment 1 consumed as spine. SN-26 recorded and placed in M36. SN-28
recorded, its namespace question answered, Required actions 1–3 placed in M36 and Required action 4
authorized as B3.1. The llama.cpp trial closed. P10-GH-2 re-diagnosed. Seven proposals returned to
the CFO unacted. Carry-forwards triaged.

**This ruling is an HQ-authored delivery. Per PSG §11.6.1 the CFO is the mandatory diff reviewer and
default-accept does not apply — silence is not acceptance here.** No chat-level reviewer exists for
it.

**Open at HQ, awaiting the CFO:** the four returned proposals that remain unowned (Decision 10, items
1–4). None blocks a milestone; each has a recorded fallback in the phase spec.
