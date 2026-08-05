---
artifact_type: hq_opener
artifact_version: 1.0
timestamp: 2026-08-01T00:30:00Z
issued_by: Creation Chat
project_name: ai-project-system
repo: https://github.com/panchew/ai-project-system
governance_version: PROJECT-SYSTEM-GUIDELINES.md v2.4.0
operating_version: AI-OPERATING-GUIDELINES.md v2.10.0
framework_version: v7.1.0
active_phase: none — P10 closed 2026-07-31 at v7.1.0; P11 not yet opened
instantiation: p11-scoping
supersedes: .ai-project/artifacts/hq-openers/2026-07-28__hq-chat-opener.md
provenance: >
  Authored by the Creation Chat to instantiate an HQ Chat that opens P11. This is a
  SCOPING instantiation: the 2026-07-31 Progress Digest stated that HQ cannot scope a
  phase and that P11 waits on the Creation Chat for a spine. That spine is now filed
  (SN-27 + Amendment 1). This opener carries it, plus SN-26 and SN-28, into HQ, along
  with two CFO rulings made in the same session: P11's first milestone is documentation
  hygiene, and one duplicate-ID test is authorized as a hotfix. To be filed verbatim by
  the HQ Chat session it instantiates, for the artifact record.
---

# HQ Chat Opener — Project Control Room

> **Amendment 2026-08-04 (P11-M36-E36.2) — `SN-1` in this opener was renumbered to `SN-29`.**
> The five references below to *"the SN-1 System HQ codification"* (Open item #3, the P11-scoping
> note, the triage table row #3, and the two `[PROPOSED]` placement items) mean the Layer-8/CFO
> Steering Note
> (`.ai-project/artifacts/steering-notes/2026-07-31__layer-8-cfo__steering-note__system-hq-routing-model.md`),
> which was filed claiming an ID already held by the 2026-06-12 Creation Chat note. **HQ Ruling
> 2026-08-01, Decision 3** ruled it misnumbered; E36.2 executed the renumber to `SN-29` on
> 2026-08-04. The separate reference to *"SN-23 and SN-1 are each claimed by two different notes"*
> describes the collision as it stood and is left alone — it remains true of that date. The text is
> not rewritten; the rename is recorded here so it stays legible *as* a rename.

## ⚠ Prerequisite Verification — READ BEFORE ANYTHING ELSE

Per the HQ Chat Opener template and `governance/systems/chat-hierarchy.md` "Manual Chat Model
Verification" (P9-M31-E31.3): read your own harness-reported model identity and compare it to
`.ai-project.yml`'s `models.hq`. If both are present and disagree, **STOP — state the mismatch
plainly and wait for human resolution.**

- `.ai-project.yml` `models.hq` = `remote:claude-opus-5`
- **No mismatch is expected.** The 2026-07-28 HQ Ruling refreshed all five paid-frontier keys
  from `claude-opus-4-8` to `claude-opus-5`, and the Creation Chat session that authored this
  opener verified cleanly against `models.creation` on the same value.

If a mismatch nonetheless appears, it is not pre-diagnosed and is not this chat's agenda. Halt
per the rule.

---

## Project Context

| Field | Value |
|---|---|
| **Project** | `ai-project-system` — the governance framework's own repository |
| **Repo** | https://github.com/panchew/ai-project-system |
| **Governance** | PSG v2.4.0 / AOG v2.10.0 |
| **Framework** | v7.1.0 (tag). `master` has since advanced with Creation Chat artifacts only — steering notes and this opener. No code or governance-document changes since the tag. |
| **Phase status** | P10 closed 2026-07-31 (merge `bb727a5`, tag `v7.1.0`, closure `4598d4d`). **No phase open.** |
| **Suite** | 366 passed / 0 failed / 0 skipped at P10 closure |
| **Open PRs** | None |
| **Blocking concerns** | None. Nothing in the framework waits on HQ except P11 itself. |

**Ecosystem — four projects** (SN-24, not amended): (1) AI Project System — governance, focused
on itself, does *not* coordinate the others; (2) Local Agent Runner — execution; (3) AI Project
System MCP — the protocol seam, load-bearing; (4) Drivr — coordination daemon, gates, thin
surface. Item (2)'s continued existence is under directed assessment — see SN-27 Amendment A1.2.

---

## Why This Chat Exists

**To open P11.** The 2026-07-31 Progress Digest's closing line: *"The one thing waiting is P11
itself, and it is waiting on the Creation Chat."* It is no longer waiting.

Per `hq-chat.md`, HQ produces the **Phase Execution Chat Starter** — a binding planning contract —
and does not infer a spine to write it from. The spine is supplied below.

---

## Agenda — in order

### 1. Consume SN-27 and its Amendment 1 — the P11 spine [PRIMARY]

`.ai-project/artifacts/steering-notes/2026-07-31__creation-chat__steering-note__P11-drivr-spine.md`

**Read the note including Amendment 1 before acting on any part of it.** One binding decision in
the front matter is marked `SUPERSEDED BY AMENDMENT 1`; the amendment was filed 2026-08-01, before
this opener, precisely so that no superseded roster is read as binding.

Eight binding CFO decisions set the spine. The organizing one: **an app is made AI-powered by
calling a CLI tool that owns the inference.** SN-24 already ruled Drivr rents its *chat* half from
existing harnesses; SN-27 extends the same principle to its *execution* half. Drivr implements no
inference and owns no model loop. It coordinates.

Amendment 1 then changes the roster without touching the spine — OpenCode covers the local lane
too, verified in field practice — which is the adapter-surface decision proving itself within
hours of being made.

**HQ's task:** open P11 with this spine and produce the Phase Execution Chat Starter.

### 2. P11's FIRST milestone is documentation hygiene — CFO-decided [BINDING]

**Ruled by the CFO, 2026-08-01, in the Creation Chat session that authored this opener.** Not a
proposal for HQ to weigh. Four self-contained items, no dependencies on Drivr, before any Drivr
work begins:

1. **SN-28 Required actions 1–3** — answer the cross-entity namespace question, resolve the SN-23
   citation ambiguity, add an ID allocation rule.
2. **SN-26** — reconcile the three disagreeing Creation Chat re-instantiation surfaces; decide
   whether this project renders its own `genesis.md`.
3. **The SN-1 System HQ codification** — already ruled, already placed in P11 (see the triage
   table below for its path and content).
4. **SN-26's re-diagnosis of P10-GH-2** — amend the carry-forward text so a future owner is
   pointed at the ritual rather than at `seed.md`.

**Answer SN-28's namespace question before any renumbering is specified in the milestone spec.**
Renumbering first would bake in an answer nobody gave.

**Why this ordering, recorded so it is not re-litigated:** the CFO's instinct was to clean
everything before P11 opened at all. The Creation Chat objected that amending normative documents
outside any phase would mean no spec, no DoD, no Stage-2 review and no closure record — ungoverned
work in the repository whose thesis is that work is governed. The ruling takes both: the cleanup
lands **before any Drivr code exists** *and* lands **governed**.

### 3. One hotfix is authorized to land before P11 opens [BINDING]

**The duplicate-ID test** — SN-28 Required action 4, asserting no duplicate `id:` across
`.ai-project/artifacts/steering-notes/`. CFO-classified as a **hotfix**: small, mechanical,
self-contained, adds a test and changes no normative text. It is the only SN-28 item that prevents
recurrence rather than describing it.

**The carve-out is bounded by that property, not by diff size.** The moment an item in this bucket
would edit a governance document, it leaves the bucket and goes to the milestone above.

**HQ authorizes and executes or delegates it.** The Creation Chat does not — it produces artifacts
and holds no authority.

### 4. Sequence P10-GH-7 before any dispatch or scheduling work [HIGH]

The spine's scheduler and derived gate queue both depend on knowing whether a run finished,
stalled, or failed confidently wrong. That signal is **measured broken in two independent
engines**: P10's own runs (exit 0 with zero work; exit 2 with complete green work) and OpenCode's
open issue #14551 (`run` exits 0 on session errors). **G11** stands at zero captured `epic_qa`
runs.

SN-27 asks that this be treated as in-scope and sequenced first, rather than triaged as a
carry-forward. Amendment A1.5 sharpens it: if OpenCode becomes the sole engine, the problem
concentrates in a dependency the CFO does not own.

### 5. Record the llama.cpp trial as CLOSED, not parked [SN-27 A1.3]

The CFO has dropped it by decision. Its Mac-class-hardware trigger is void. Left parked, a future
phase re-inherits a decision already made. **The local-inference runtime question is closed;
Ollama is settled, not provisionally chosen.** The *model* roster stays open — see A1.4.

### 6. Carry the milestone-context question into P11 scope [SN-27 A1.4]

*Can `qwen3-coder:30b` handle the context of a milestone?* This is a **fourth axis** beside row
P4's existing gates (G-P4-a prescription variance, G-P4-b unassisted search, G-P4-c tool-using
verification) — capacity at scale, which E35.5's blinded-packet method did not test.

**Row P4's 2026-07-31 ruling is not reopened by this.** It is where an answer would eventually
land.

### 7. Record SN-26 — no action [MEDIUM]

`.ai-project/artifacts/steering-notes/2026-07-31__creation-chat__steering-note__creation-reinstantiation-ritual.md`

Creation Chat re-instantiation is described by three disagreeing surfaces and is unexecutable as
written; **P10-GH-2 is misdiagnosed** and its carry-forward text should be amended so a future
owner is pointed at the ritual rather than at `seed.md`, which has carried the check since
`d7ee7cd`. Binding CFO decision in that note: **this is tightening, not phase scope, and must not
shape P11's spine.** Record it; place it later, in a milestone with room, alongside the SN-1
System HQ codification.

### 8. Steering Notes carried by this opener — the complete set

**Three: SN-26, SN-27 (with Amendment 1), and SN-28.** Those are the Steering Notes HQ has not yet
consumed.

**SN-28** — `.ai-project/artifacts/steering-notes/2026-08-01__creation-chat__steering-note__sn-numbering-unenforced.md`
— records that Steering Note ID allocation is unenforced: **SN-23 and SN-1 are each claimed by two
different notes**, and `AI-OPERATING-GUIDELINES.md` and `chat-hierarchy.md` both cite *"SN-23
Decision 2"* meaning different decisions, one of which the latter declares superseded. Binding CFO
decision in that note: **fix it, but inside P11, not before it.**

A caution for this chat's own reading: **citations of "SN-23" in the corpus are ambiguous.** Where
a document cites SN-23, check the date before relying on it — 2026-07-18 is reference-first /
platform agnosticism; 2026-07-20 is the P10 adoption spine. This opener's Constraints section
cites the 2026-07-20 note.

Every other Steering Note in `.ai-project/artifacts/steering-notes/` has already been ruled on and
is **deliberately not re-attached** — SN-23 (consumed by P10 opening, running and closing), SN-24
(ruled `2026-07-28__...__sn-24-m35-operator-form.md`), SN-25 (ruled
`2026-07-30__...__sn-25-handback-and-execution-matrix.md`), and SN-1 (ruled
`2026-07-31__...__system-hq-routing-codification.md`).

**The convention, stated so it holds for future openers:** an opener carries **unconsumed**
Steering Notes as *agenda*, and **ruled** ones as *constraints* — cited by their ruling, never
re-attached as notes. Re-attaching a ruled note invites HQ to re-decide what is already decided.
This is why SN-24 appears in this opener's **Constraints** section rather than its agenda, and why
SN-25 appears there only as *mode is not authority*.

### 9. Triage of the digest's remaining Open Decisions

| Digest item | Disposition per SN-27 |
|---|---|
| #1 What is P11's spine? | **Answered.** Agenda 1. |
| #2 Block detection | **In scope, sequenced first.** Agenda 2. |
| #3 SN-1 System HQ codification | **Already ruled and placed in P11** — `.ai-project/artifacts/rulings/2026-07-31__ai-project-system-hq__ruling__system-hq-routing-codification.md` (D1–D4 accepted). P11 must *execute* it: a self-contained amendment to `system-hq.md`, Authority Boundary verbatim-frozen across three documents as a DoD item, reusing `steering_note` for the routed-to-B leg rather than inventing a type. No dependencies. `[PROPOSED]` place beside SN-26 in a documentation milestone. |
| #4 P9-GH-1 / P10-GH-9 owner | Trigger is the first Phase/Milestone agentic dispatch. `[PROPOSED]` assign at the milestone that first touches dispatch, not at phase open. |
| #5 `ai-stack`, `character-factory` | `[PROPOSED]` resolves as a side effect of the three-state registry — classification is registry work, not a separate decision. |
| #6 Sidekick-for-external-projects | Unchanged. Brief-level identity question, not phase scope. |

---

## Constraints Binding on P11

1. **SN-24 is not amended** — headless-first; the chat half is rented; gates in-app only; push
   and WhatsApp deferred; inbound approval must never be a chat reply (signed one-time link, so
   the authorization artifact is still minted in-app); the human is a node *inside* the governance
   graph, not an operator above it.
2. **Gate queue is derived, never hand-maintained** — it is whatever governance says is
   outstanding. The human holds the gate; the system computes the list.
3. **PSG §11.6.1 is in force** — the CFO is the mandatory *diff* reviewer for HQ-authored
   deliveries, because HQ has no parent chat and default-accept is only safe because a parent
   reviews. Competing-model PR review **feeds this and never substitutes for it** (SN-27 decision
   7: surfacing findings only, no authority, no consensus path).
4. **Mode is not authority** — an instance running unattended holds exactly the authority its
   level always held.
5. **The leverage case is a choice, and it is on the record** — the return is a way of working
   that keeps the CFO competitive in the industry. Not revenue, not a platform. **The bar this
   sets:** P11 is justified to the degree the way of working it produces transfers to how the CFO
   actually works professionally — not to the degree the machine is impressive.
6. **HQ Rulings amending normative documents SHOULD carry a Structural diagram** (Mermaid, fenced,
   no ComfyUI) — `hq-chat.md`, "Review Diagram on HQ Rulings."

---

## Items Returned to the CFO — Do Not Act On

SN-27 carries seven `[PROPOSED — confirm]` items authored by the Creation Chat, not the CFO. They
are **proposals, not decisions**, and HQ should return them rather than treat them as spine:

1. Drivr may *propose* a fleet-state transition but never execute one.
2. The `local-agent-runner` retention bar (*"names a capability P11 needs that OpenCode does not
   provide"*), and its two candidate capabilities.
3. Model-watch as cheap re-tests against E35.5's existing harness rather than scheduled
   investigations.
4. The engine-comparison spike (OpenCode `run` vs `local-agent-runner` on the latter's own
   `proof/` fixture, same model, same host — comparing transcript quality and exit-code honesty).
5. Placement of SN-1 and SN-26 together in a documentation milestone.
6. P9-GH-1 owner assigned at the dispatch-touching milestone.
7. `ai-stack` / `character-factory` resolved via registry classification.

---

## Next Actions for HQ

1. Verify model per the prerequisite block above.
2. Read SN-27 **including Amendment 1**, then SN-26 and SN-28.
3. **Open P11** with the SN-27 spine.
4. **Produce the Phase Execution Chat Starter**, carrying SN-24's opener obligations forward —
   the four-project ecosystem, the headless-first inversion (*a dashboard is a surface for
   watching; the more agentic the machine, the less there is to watch*), and the
   infrastructure-is-not-a-platform caution, now answered by SN-27 decision 8.
5. **Scope P11's first milestone as documentation hygiene** (Agenda 2) — CFO-decided, not open.
   Answer SN-28's namespace question before specifying any renumbering.
6. **Authorize the duplicate-ID test hotfix** (Agenda 3), or delegate it. It may land before P11
   opens.
7. Sequence P10-GH-7 ahead of dispatch/scheduling work (Agenda 4).
8. Record the llama.cpp closure and SN-26's re-diagnosis of P10-GH-2.
9. File this opener verbatim in the artifact record.

---

## Technical Note for Whoever Builds the OpenCode Adapter

Ollama defaults **every** model to a 4,096-token context window regardless of what the model
supports; OpenCode needs roughly 16k+ to drive its tool-use loop. Silent truncation here presents
as model incompetence. Relevant to Agenda 4 — a milestone-context test that hits this without
knowing it would produce a false negative about the model.
