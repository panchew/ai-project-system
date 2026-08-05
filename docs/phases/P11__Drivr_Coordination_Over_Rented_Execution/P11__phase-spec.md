---
phase: P11
name: "Drivr: Coordination over Rented Execution"
status: scoping
start_date: 2026-08-01
planned_end_date: 2026-08-29
version: 1.0.3
---

# Phase P11: Drivr — Coordination over Rented Execution

## Executive Summary

P10 proved the framework works in the wild: six fleet projects at confirmable v7.0.0, two real
Agentic/Local epics, the local runtime settled, the fleet-operator role canonized with a handback
obligation and a ratified execution matrix. The corpus stands at **v7.1.0**, suite **366/0**. What
P10 also proved is that **the operator is still the CFO.** The lane is hand-run. The gate list is
whatever the human remembers. A blocked agentic instance has a normative obligation to hand back and
no mechanism to do it with.

**P11 builds the thing that holds the framework's hands: Drivr.** Per SN-27 (2026-07-31, all
decisions the CFO's) and its Amendment 1 (2026-08-01), the organizing realization is:

> **An app is made AI-powered by calling a CLI tool that owns the inference.**

SN-24 already ruled that Drivr **rents its chat half** from existing harnesses rather than building
an agent client. SN-27 extends the identical principle one layer down: **Drivr rents its execution
half too.** It implements no inference, owns no model loop, and grows no engine. It invokes CLI tools
that already do all three, and spends its entire budget on the one layer nobody sells — **coordination
over this project's own governance state.**

Amendment 1 tested that architecture within two hours of it being decided and it held: OpenCode +
Ollama + `qwen3-coder:30b` covers the local lane as well as `local-agent-runner` does, so the
two-lane roster collapsed to one tool. **The roster changed; the architecture did not.** That is what
a pluggable adapter surface is for, and it is the strongest available evidence that the surface, not
the engine, was the right thing to commit to.

Four milestones, in binding order:

1. **M36 — Record Integrity and Documentation Hygiene.** CFO-decided as the phase's first milestone.
   Four self-contained items with zero Drivr dependency: SN-28's namespace/citation/allocation fixes,
   SN-26's re-instantiation reconciliation, the SN-1 System HQ codification, and P10-GH-2's
   re-diagnosis. The cleanup lands **before any Drivr code exists** *and* lands **governed**.
2. **M37 — Drivr Inception, Fleet Registry, and the Execution Adapter Surface.** The Drivr repository
   does not exist yet. Create it, enroll it, give it a three-state fleet registry over every project
   on the machine, and give it one working CLI adapter (OpenCode) behind a surface built for more.
3. **M38 — Trustworthy Completion Signal (P10-GH-7).** The phase's load-bearing technical risk, and
   the one thing renting an engine does *not* solve. Sequenced **before** anything that dispatches.
4. **M39 — Coordination: Scheduler, Derived Gate Queue, and the Thin Surface.** The payload: a
   scheduler that keeps the serialized lane busy without overloading the machine, a gate queue
   *derived* from governance state, a headless-first surface, and competing-model PR review that
   surfaces findings and holds no authority.

**The leverage case is a choice, and it is on the record** (SN-27 decision 8). The return is *a way
of working that keeps the CFO competitive in the industry.* Not revenue. Not a platform. **The bar
this sets: P11 is justified to the degree the way of working it produces transfers to how the CFO
actually works professionally — not to the degree the machine is impressive.**

---

## Vision

By the end of P11:

- ✅ **The record is trustworthy again.** No duplicate Steering Note ID is citable by number without
  its date; an allocation rule exists and a test enforces it; the Creation Chat re-instantiation
  ritual can actually be executed and carries the E31.3 model check on the path itself; System HQ's
  routing and CFO-originated requests are codified without one gram of new authority.
- ✅ **Drivr exists, is governed, and calls a CLI tool that owns the inference.** A real repository,
  enrolled at v7.1.0 under this framework's own governance, invoking OpenCode through an adapter
  interface that a second engine could be dropped into without re-architecture.
- ✅ **The fleet is a data structure, not a memory.** Every project on the machine is classified
  **active**, **benched**, or **archived**, in a registry Drivr reads — which resolves `ai-stack` and
  `character-factory` as a side effect of the classification pass rather than as a separate decision,
  and catches the projects that appeared since P10's list.
- ✅ **The completion signal can be trusted, or its limits are measured and stated.** A run's outcome
  is judged by something better than an exit code proven wrong in both directions on two independent
  engines, and the `epic_qa` lane has run at least once (**G11 closed**).
- ✅ **The lane runs itself, and the human holds the gate.** A scheduler keeps one reasoning job
  running at a time without a human starting it; the gate queue is **computed from governance state,
  never hand-maintained**; the human approves through the app, and inbound approval is a signed
  one-time link — **never a chat reply**.
- ✅ **A blocked instance can actually hand back.** M35 made handback a normative obligation with no
  detector beneath it. P11 supplies the detector and the surface it arrives on.
- ✅ **Competing models review PRs and change nothing on their own.** GitHub Copilot and at least one
  competing model surface performance, security and scalability findings into the CFO's §11.6.1 diff
  review. They hold no authority, resolve nothing, and no volume of agreement between them converts
  into a decision.

---

## Scope

**Where P11's work lands.** Like P10, this phase's deliverables live substantially **outside this
repository** — most of them in **Drivr**, a repository that does not exist at phase open (verified
`~/soft-dev`, 2026-08-01). This repo holds the **governance record**: the phase spec, milestone and
epic specs, execution-chat starters, delivery and closure artifacts, and the captured evidence. M36
is the exception and is entirely in-repo: it amends this framework's own normative corpus.

### P11.1: Record Integrity and Documentation Hygiene (M36)

**First, by CFO ruling (2026-08-01, recorded in SN-28).** Four self-contained items, no Drivr
dependency. The CFO's instinct was to clean everything before P11 opened at all; the Creation Chat
objected that amending normative documents outside any phase would be ungoverned work in the
repository whose thesis is that work is governed. **The ruling takes both positions: the cleanup lands
before any Drivr code exists, and it lands governed** — with a spec, a DoD, a Stage-2 review and a
closure record. Nothing is delayed except the ungoverned-ness.

**1. Steering Note ID integrity (SN-28 Required actions 1–3).**

The audit found 28 IDs across 23 notes with **two double-claimed**, and the SN-23 collision reaches
into the normative tier: `AI-OPERATING-GUIDELINES.md` and `chat-hierarchy.md` **both cite "SN-23
Decision 2" meaning entirely unrelated decisions**, and the latter declares its one *superseded*. A
reader following the AOG citation lands on the supersession notice and concludes platform agnosticism
was superseded. It was not.

- **The namespace question is ANSWERED and is applied here, not re-derived** (HQ Ruling 2026-08-01,
  Decision 3): **one sequence per steering-note directory, regardless of issuing entity.** A note
  filed into a project's `steering-notes/` takes the next free `SN-<n>`; sub-IDs keep letter suffixes.
  Provenance is already recorded in `issuer_chat` and the filename slug — the identifier names
  position and nothing else.
- **SN-1 (the Layer-8/CFO note) is renumbered** to the next free ID at execution time. Its two
  citations (the 2026-07-31 Progress Digest, the 2026-07-31 System HQ codification ruling) are
  amended with a footnote recording the old number, so the rename is traceable.
- **SN-23 is NOT renumbered.** Citations carry the date instead — `SN-23 (2026-07-18)` for
  reference-first / platform agnosticism, `SN-23 (2026-07-20)` for the P10 adoption spine — and the
  citing documents are fixed: `AI-OPERATING-GUIDELINES.md`, `artifact-communication-protocol.md`,
  `chat-hierarchy.md`, `fleet-operator.md`, `fleet-operator-brief.md`, and SN-27's own
  "Ratified Decision #7" citation.
- **The rule separating those two treatments is normative and must be recorded:** *a bookkeeping
  defect never rewrites a citation in a normative document.* Cited only in project-internal
  non-normative artifacts → renumber. Cited in the normative tier → date-qualify and leave the
  collision visible rather than laundered.
- **An allocation rule** lands in the Steering Note template and `creation-chat-guide.md`: next ID =
  highest existing ID in the directory + 1, regardless of issuing entity.

**2. Creation Chat re-instantiation (SN-26).** Three surfaces describe how a Creation Chat is
re-opened and they disagree; `creation-chat-guide.md`'s ritual names `genesis.md` as artifact #1 and
**no `genesis.md` exists in this project** — nor a Project Brief. The ritual is unexecutable as
written. M36: decide whether this project renders its own `genesis.md` (and whether a Project Brief is
expected for a framework repo that bootstrapped itself); reconcile the three surfaces to **one
normative statement** with the others citing rather than restating it; and **ensure whatever path is
canonized carries the E31.3 model check on the path itself**, not only in a template that path may
not include. The Seed's existing behaviour — the one surface that caused verification to happen —
must be preserved, not traded away for tidiness.

**3. The SN-1 System HQ codification.** Already ruled 2026-07-31 (D1–D4 accepted); M36 *executes* it.
A short **Routing & Origination** section in `governance/systems/system-hq.md` recording D1 (route to
project B via B's own artifact channels; **routing never commands**), D2 (CFO-originated requests,
scribed), D3 (operating scope: config and setup primarily; planned work only in specific cases and
then execution-only against artifact authorization). **No new authority, no new decision rights, no
new artifact type** — the routed-to-B leg reuses `steering_note`, because that type already encodes
*direction, not authorization*, which is the whole content of "routing never commands."

Two DoD items travel verbatim from that ruling and are **not optional**:
- a **byte-level agreement check** of the Authority Boundary block across `system-hq.md`,
  `system-hq-seed.md`, and `chat-hierarchy.md`'s out-of-hierarchy annex, shown identical **after** the
  edit — not "was not intentionally changed";
- the **issuer-vs-scribe rule** stated explicitly, requiring the scribing artifact to name both (if
  the scribe ever becomes the apparent issuer, the record loses the ability to distinguish
  CFO-originated from project-originated work).

**4. P10-GH-2 re-diagnosis (SN-26 Required action 1).** The carry-forward is filed as *"the Creation
Chat Seed does not implement the E31.3 check."* False: `governance/templates/seed.md` has carried it
since `d7ee7cd` (2026-07-19), nine days before the ruling that filed the gap, and the 2026-07-31
session opened from `seed.md` ran the check. **As filed, it points a future owner at a file that needs
no change and the real defect survives the fix.** Amend the carry-forward text so the re-diagnosis
travels with the item.

**5. The bounded artifact-ID audit (SN-28 Carry-Over 3).** Only steering notes were audited. Rulings,
escalation notices, and the `GH-` gap-record series allocate IDs the same unenforced way, and `GH-` is
cited far more widely. **M36 audits and reports. It does not fix what it finds.** If a second family
shows collisions reaching the normative tier, that is an **escalation to HQ**, not scope the milestone
absorbs.

**M36 amends normative documents, so the `hq-chat.md` Structural-diagram obligation applies to its
deliveries** (Mermaid, fenced, no ComfyUI) — showing which documents were touched, what changed in
each named to the section, what was deliberately frozen, and where authority flowed.

### P11.2: Drivr Inception, Fleet Registry, and the Execution Adapter Surface (M37)

**Drivr does not exist.** M37 creates it, enrolls it under this framework at v7.1.0 using M33/E33.1's
enrolled-project procedure, and gets it to the point where it can invoke one CLI engine and read the
fleet.

**The adapter surface is the architecture; the roster is configuration.** Drivr must be able to use
**any CLI tool that empowers the work** (SN-27 decision 3). The interface is the deliverable. Today's
roster after Amendment A1.1 is **one tool: OpenCode**, covering local *and* cloud — verified by the
CFO in field practice, OpenCode + Ollama + `qwen3-coder:30b` working as `local-agent-runner` does. A
future roster change must be a configuration decision, not a re-architecture; the milestone is
successful only if a second adapter could be added without touching the coordination layer.

> **Technical note, binding on whoever builds the OpenCode adapter — corrected v1.0.1, now measured
> rather than inherited.** The v1.0.0 text carried a warning that Ollama defaults every model to a
> 4,096-token context window. **That is false on this host and was never verified before being
> written into this spec.** Measured 2026-08-01 against **Ollama 0.30.0**:
>
> | Fact | Measured |
> |---|---|
> | `qwen3-coder:30b` loaded context | **32,768** (12.9 GB VRAM of 21.4 GB total; ~8.5 GB in RAM) |
> | `qwen2.5-coder:7b` loaded context | **32,768**, wholly unconfigured |
> | 20,530-token prompt, marker at position 0, **no options set** | marker recovered — no 4k truncation |
> | same prompt, `/v1` + `options.num_ctx=2048` | marker **still** recovered |
>
> Two consequences. **The 4,096 default does not apply here** — Ollama 0.30.0 loads the model's own
> context. And **the `/v1` OpenAI-compatible endpoint silently ignores `options` entirely**: forcing
> `num_ctx=2048` changed nothing, so OpenCode cannot set the loaded context through that transport
> and does not need to. (`local-agent-runner`'s native `/api/chat` *does* honour `options` — a real
> transport difference, but **not** a retention argument for E37.4, since the default is already
> correct.)
>
> **The surviving caution is an 8× overpack, and it is the one to build against.** `opencode.json`
> declares `"context": 262144` for `qwen3-coder:30b` against **32,768** actually loaded. That
> declared limit is what OpenCode uses to decide when to compact a conversation, so a long session
> will pack past what Ollama holds and be truncated silently. **The adapter must derive the declared
> limit from what `/api/ps` reports as loaded, not from the model's trained maximum.** Short tasks
> are unaffected: B3.1's scoped context measured 7,819 bytes (~2,000 tokens).
>
> **Method is recorded so this correction is reproducible and so the next one is cheaper:** plant a
> marker at position 0 of a prompt that exceeds the suspected limit, ask for it back, and read
> `/api/ps` for `context_length`. Do not infer a context ceiling from an agent behaving badly.

**`local-agent-runner`'s retention is a directed assessment with a real possibility of retirement**
(A1.2), and it is **not** a judgment on the work: P9/P10's local-inference evidence — the runtime
decision, the 14b-vs-30b model-tier finding, the blinded review back-test — was evidence about *local
agentic execution* and stands whatever happens to the engine that produced it. The assessment **bar**
is a returned proposal (see Open Items); if the CFO does not set one, M37 records the two candidate
capabilities worth checking — its **library entry point** (`run(task, tools, model)` with in-process
tool handlers) and its **JSON-schema argument coercion** for models that mistype tool arguments —
tests whether OpenCode's `serve` mode covers them, and reports **without retiring anything**.

**The fleet registry has three states** (SN-27 decision 5):

| State | Definition (the CFO's) |
|---|---|
| **Active** | Enrolled in the registry. Receives time and attention. |
| **Benched** | Not currently receiving attention. May return. |
| **Archived** | Not planned to ever be touched again — though it can be brought back to life. |

**Building it forces a classification pass over every project on the machine**, which is how
`ai-stack` and `character-factory` resolve — as registry work, not as a separate decision. The pass
must cover the projects that appeared **after** P10's list was written: `personal-management-system`,
`social-stories-creator`, and `voicebox` are present in `~/soft-dev` and are named in no prior phase
artifact. P10's own six (`home_finance`, `local-agent-runner`, `ai-project-system-mcp`, `courtis`,
`Getawayinsured2023`, `footboard`) plus `fieldledger-assesment` (dropped from P10 by direct CFO
instruction as a screening project) are classified too — dropping from a phase's scope is not a
registry state.

**P10-GH-5 is folded in here** (HQ Ruling 2026-08-01, Decision 11): `ai-project-yml-spec.md` §4's
validation rules are normative and unenforced, no validator exists in `bin/`, and **3 of 6 enrolled
configs were invalid by P10 close**. A registry built over configs that degrade quietly is the same
defect class as a scheduler built over an untrustworthy exit code. **P10-GH-1** (`framework_version`
is convention-only, not in the yml spec) is a **conditional** fold-in at the Phase Chat's judgment:
schema-bless it in the same pass *if* the registry reads it normatively; otherwise leave it parked.

**The milestone-context question is evidence-gathering here** (A1.4): *can `qwen3-coder:30b` handle
the context of a **milestone**?* This is a **fourth axis** beside `model-routing-policy.md` row P4's
existing gates — G-P4-a (measured prescription variance), G-P4-b (unassisted search and
absence-detection over a real branch), G-P4-c (tool-using verification before ruling) — testing
**capacity at scale**, which E35.5's blinded-packet method did not test. **Row P4's 2026-07-31 ruling
is not reopened, and M37 does not decide it.** M37 produces the measurement; a further HQ call decides
the row.

### P11.3: Trustworthy Completion Signal (M38)

**The one thing renting does not solve, and the phase's load-bearing technical constraint.**

P10 measured completion untrustworthy in **both** directions on its own stack: **E33.2 Run A returned
exit 0 having done zero work**; **E33.4 returned exit 2 having produced complete, green work.**
Corroborated across two projects — *the exit code is not a completion signal on this stack.*
Compounding it, **G11 stands at zero captured `epic_qa` runs**: the lane that would supply a
trustworthy signal has never been exercised.

**Renting the engine relocates this problem rather than escaping it.** OpenCode carries an open issue
of exactly the same shape — `opencode run` exits `0` even when the session errored, because the run
command does not await the event loop tracking error state (`anomalyco/opencode` #14551). Amendment
A1.5 sharpens the consequence: if OpenCode becomes the sole engine, the failure mode **concentrates
in a dependency the CFO does not own** — better for diagnosis, worse for control.

**So M38's deliverable is not "fix the exit code."** It is **a completion judgment that does not rest
on the exit code alone**, plus the first captured `epic_qa` runs. What a trustworthy judgment is built
from is the Milestone Chat's design decision — transcript inspection, repository/artifact state
delta, governance-state verification, a QA-role second pass, or a combination. What is **binding** is
that the judgment must be **measured against the known cases**: E33.2 Run A must read as *did not
complete*, and E33.4 must read as *completed*.

**M39 cannot begin until M38 delivers.** A scheduler dispatching unattended runs, and a gate queue
derived from what governance says is outstanding, both depend on knowing whether a run finished,
stalled, or failed confidently wrong. Building either over the current signal yields **constant false
escalations** (the human becomes the bottleneck again, worse than before) or **silent no-ops that read
as success**. M35's handback rule has had no detector beneath it in either engine since the day it was
recorded; M38 is where that stops being true.

**Named, not scoped: P10-GH-10.** A ~10%-flaky `tests/test_artifact_router.py::test_daemon_extensions_error_branches`
weakens "full suite green" as evidence, and M38's evidence is suite-shaped. Flagged for the Phase
Chat's awareness; not this milestone's job.

### P11.4: Coordination — Scheduler, Derived Gate Queue, and the Thin Surface (M39)

The payload, gated on M38.

**The scheduler.** *The orchestrator schedules agentic runs to avoid overloading the system* (SN-27
decision 6). This is the concrete form of **SN-23 (2026-07-20) Ratified Decision #7** — *scheduler
only when contention bites* — and **contention now bites, measured**: one GPU, 16 GB VRAM shared with
ComfyUI, one heavy consumer at a time, `qwen3-coder:30b` already partially offloading to RAM. P10 ran
the lane by hand and the friction is real. The lane stays **serialized**: enrollment (which projects
may run) and concurrency (one reasoning job at any instant) are different axes and do not conflict.

**The derived gate queue.** **It is whatever governance says is outstanding — computed, never
hand-maintained.** The human holds the gate; the system computes the list. A hand-maintained queue is
a second source of truth for governance state and would drift from the artifacts within a week.

**The thin surface, headless-first.** SN-24 is **not amended** and its inversion holds: *a dashboard
is a surface for watching; the more agentic the machine, the less there is to watch.* Gates are
**in-app only**. Push and WhatsApp are **deferred**. **Inbound approval must never be a chat reply** —
it is a **signed one-time link**, so the authorization artifact is still minted in-app. Single-window
is a nice-to-have, not a requirement. The human is a node **inside** the governance graph, not an
operator above it.

**Competing-model PR review — findings only** (SN-27 decision 7). GitHub Copilot as a PR reviewer plus
at least one competing model, looking closely for **performance, security, and scalability**. This
**un-parks** the item P10 carried unowned, and it now has an explicit authority ceiling:

> **PSG §11.6.1 makes the CFO the mandatory diff reviewer.** Competing-model review **feeds that
> review. It does not substitute for it, dilute it, or create a consensus path that resolves
> anything.** No finding from any model carries authority, and no volume of agreement between models
> converts into one. This is *mode is not authority* applied to a new participant class.

**P9-GH-1 / P10-GH-9 get an owner here.** M39 is the milestone that first wires Phase/Milestone
agentic dispatch — which is P10-GH-9's own recorded trigger. P9-GH-1's merge-authorization-routing
guard is patched at Epic level only; the Milestone and Phase starter templates remain unpatched. While
Phase and Milestone ran manual by fixed posture, a human sat at those gates **by construction**; the
ratified execution matrix removed that compensation without touching the guard. **Wiring dispatch
without addressing it is the exact combination P10-GH-9 was filed to prevent.**

---

## Out of Scope

- **Building an inference engine, a model loop, or an agent client.** Drivr rents both halves. This is
  the spine, stated as an exclusion so it cannot erode by increment.
- **Any local-inference runtime other than Ollama.** **Closed by CFO decision** (A1.3), not parked and
  not deferred. The llama.cpp + Qwen3.6 Q8_0 trial's Mac-class-hardware trigger is **void**; the item
  does not carry forward and no future phase re-inherits it. **Ollama is settled, not provisionally
  chosen.**
- **Deciding `model-routing-policy.md` row P4.** M37 gathers milestone-context evidence as a fourth
  axis beside G-P4-a/b/c. **The 2026-07-31 ruling is not reopened**, and the decision is a further HQ
  call on the evidence.
- **Push notifications and WhatsApp.** Deferred under SN-24, unchanged.
- **Approval by chat reply.** Prohibited, not deferred. Signed one-time link only.
- **Drivr executing fleet-state transitions.** A returned proposal (Drivr proposes, the CFO
  transitions) and therefore **not** assumed. Until the CFO rules, M37 builds the registry with
  transitions as a **recorded human action**; nothing automatic.
- **Any expansion of System HQ authority.** M36's codification records D1–D3 as practice already in
  use. The SN-21/SN-22 pin — System HQ is not a "mighty governing System Chat" — stands.
- **Competing-model review holding any authority.** Findings only. No consensus path, no blocking
  vote, no substitution for §11.6.1.
- **Fixing whatever M36's artifact-ID audit finds** beyond steering notes. The audit reports;
  remediation is a further decision.
- **P10-GH-8** (`governance/systems/` versions/changelogs inconsistent). A corpus-wide convention
  change. The Phase Chat MAY propose folding it into M36; HQ does not mandate it — M36's contents were
  set by the CFO and already number four.
- **P9-GH-3, P10-GH-3, P10-GH-4, P10-GH-6, P10-GH-10, P8-GH-2, ComfyUI precision investigation.**
  Parked on their existing triggers, restated so none is silently dropped.
- **Sidekick-for-external-projects.** A Brief-level identity question (pivot vs addition), not phase
  scope. Noted so P11 inherits no unstated pivot.
- **A single-window unified surface.** Nice-to-have under SN-24, explicitly not a requirement.

---

## Milestones

### M36: Record Integrity and Documentation Hygiene

**Goal:** Land the four self-contained documentation items — governed — before any Drivr code exists.

**Indicative Epics** (the Milestone Chat owns final decomposition):
- **E36.1 — Steering Note ID allocation rule + SN-23 date-qualified citations.** Apply the answered
  namespace rule; record the *bookkeeping-never-rewrites-normative-citations* rule; date-qualify the
  SN-23 citations across the five citing documents plus SN-27's; add the allocation rule to the
  Steering Note template and `creation-chat-guide.md`.
- **E36.2 — Renumber the misnumbered Layer-8/CFO note.** Take the next free ID; footnote both existing
  citations with the old number so the rename is traceable.
- **E36.3 — Creation Chat re-instantiation reconciliation (SN-26).** Decide the `genesis.md` /
  Project Brief question; reconcile three surfaces to one normative statement; put the E31.3 check on
  the canonized path itself.
- **E36.4 — System HQ Routing & Origination codification (SN-1).** Per the 2026-07-31 ruling, D1–D4,
  including the byte-level Authority Boundary check across three documents and the issuer-vs-scribe
  rule as DoD items.
- **E36.5 — P10-GH-2 re-diagnosis + bounded artifact-ID audit.** Amend the carry-forward text; audit
  rulings, escalation notices and the `GH-` series for the same unenforced-ID defect; **report,
  escalate if it reaches the normative tier, fix nothing beyond steering notes.**

**Ordering constraint (binding):** the namespace rule (E36.1) is applied before any renumbering
(E36.2). No epic renumbers anything on its own initiative.

**Diagram obligation:** M36's deliveries amend normative documents, so each carries a **Structural**
Mermaid diagram per `hq-chat.md` "Review Diagram on HQ Rulings" — documents touched, what changed named
to the section, what was frozen, where authority flowed. Fenced, in-repo, no ComfyUI.

### M37: Drivr Inception, Fleet Registry, and the Execution Adapter Surface

**Goal:** Drivr exists as a governed repository, holds a three-state registry over every project on
the machine, and invokes one CLI engine through an interface a second engine could be dropped into.

**Indicative Epics:**
- **E37.1 — Drivr repository inception + enrollment at v7.1.0**, using M33/E33.1's enrolled-project
  procedure (11 recorded failure modes — use them).
- **E37.2 — The execution adapter surface + OpenCode adapter.** The interface is the deliverable;
  OpenCode is its first implementation. **Derive the declared context limit from what `/api/ps`
  reports as loaded**, not from the model's trained maximum — see the measured technical note in
  §P11.2 (`opencode.json` declares 262,144 against 32,768 actually loaded).
- **E37.3 — Three-state fleet registry + full classification pass.** Every project in `~/soft-dev`
  classified active/benched/archived, including the three P10 never listed. Fold in **P10-GH-5**
  (a validator for `ai-project-yml-spec.md` §4). **P10-GH-1** conditionally, per the Phase Chat.
- **E37.4 — `local-agent-runner` retention assessment.** Against the CFO's bar if one arrives;
  otherwise test the two candidate capabilities against OpenCode's `serve` mode and **report without
  retiring**.
- **E37.5 — Milestone-context evidence for `qwen3-coder:30b`.** Fourth axis beside G-P4-a/b/c.
  Evidence only; does not decide row P4.

- **E37.6 — System-tier versioning convention (P10-GH-8).** *(Added v1.0.2 per HQ Ruling
  2026-08-04, resolving the M36 escalation.)* Give every document in `governance/systems/` a
  `version` field and a `## Changelog`: seed the **ten** currently-unversioned documents at a
  starting version with a first row recording that the convention was adopted, pointing at git for
  prior history; leave the **seven** that already comply untouched. **No backdated reconstruction —
  permanently out of scope, not deferred.** Mechanical by construction. Independent of E37.1–E37.5;
  the Phase Chat sequences it anywhere in M37.

- **E37.7 — Artifact-ID citation forms (`GH-`, escalation notices).** *(Added v1.0.3 per HQ Ruling
  2026-08-05, resolving E36.5's audit escalation.)* Disambiguate the bare `GH-10` at
  `PROJECT-SYSTEM-GUIDELINES.md:605` to `P6-GH-10` — the sole namespace-stripped `GH-<n>` in the
  normative corpus; record that `GH-` citations in `governance/` carry the phase prefix; record that
  escalation notices are cited by **full filename**, never by milestone key; and record that the
  `GH-` prefix names the **phase that filed it**, permanently, with `P6-GH-10…15` / `P7-GH-16…21` as
  **ratified historical exceptions that are not renumbered**. Independent of E37.1–E37.6.

**Sequencing:** E37.1 first — everything else needs the repository. E37.2 and E37.3 may run in
parallel. This is the phase's largest milestone; **the Phase Chat may split it**, preserving E37.1's
position and the M37 → M38 boundary.

### M38: Trustworthy Completion Signal (P10-GH-7)

**Goal:** A run's completion can be judged by something better than an exit code proven wrong in both
directions on two independent engines, and the `epic_qa` lane has run for real.

**Indicative Epics:**
- **E38.1 — Completion judgment that does not rest on the exit code.** Design and build it; the
  mechanism is the Milestone/Epic Chat's decision.
- **E38.2 — Validate against the known cases.** **Binding:** E33.2 Run A must read *did not complete*;
  E33.4 must read *completed*. A design that cannot be shown against both is not delivered.
- **E38.3 — Exercise the `epic_qa` lane and close G11.** Capture the first real QA-role runs.

**Sequencing:** After M37 (needs a real adapter to measure). **Before M39, bindingly** — nothing in
this phase dispatches or schedules an unattended run until M38 delivers.

### M39: Coordination — Scheduler, Derived Gate Queue, and the Thin Surface

**Goal:** The lane runs without a human starting it, the gate queue is computed from governance state,
the human approves in-app through a signed one-time link, and competing models surface findings that
change nothing on their own.

**Indicative Epics:**
- **E39.1 — Serialized-lane scheduler.** One reasoning job at any instant; enrollment and concurrency
  kept as separate axes.
- **E39.2 — Derived gate queue.** Computed from governance state. Never hand-maintained.
- **E39.3 — Headless-first thin surface + signed one-time-link approval.** Gates in-app only; no chat
  reply ever authorizes.
- **E39.4 — Competing-model PR review (Copilot + at least one competitor).** Findings only, feeding
  §11.6.1; authority ceiling recorded in the epic spec, not assumed.
- **E39.5 — P9-GH-1 / P10-GH-9.** Owner assigned here. Address the merge-authorization-routing guard
  before Phase/Milestone agentic dispatch is wired, or record explicitly why the wiring is safe
  without it.

**Sequencing:** Last. Gated on M38. E39.5 lands **before or with** whatever first wires dispatch.

---

## Success Criteria

### P11 is Complete When:

1. ✅ **No Steering Note ID is citable ambiguously.** SN-23's citations carry dates across all citing
   documents; the misnumbered Layer-8/CFO note is renumbered with traceable footnotes; an allocation
   rule exists in the template and `creation-chat-guide.md`; **B3.1's test enforces uniqueness.**
2. ✅ **Creation Chat re-instantiation is executable as written** and carries the E31.3 model check on
   the path itself, with the `genesis.md` / Project Brief question decided either way.
3. ✅ **System HQ's routing and origination are codified with zero new authority** — the Authority
   Boundary shown byte-identical across three documents *after* the edit, the issuer-vs-scribe rule
   explicit, `steering_note` reused for the routed-to-B leg.
4. ✅ **P10-GH-2's carry-forward text points at the ritual, not at `seed.md`**, and the wider
   artifact-ID audit is recorded with its finding.
5. ✅ **Drivr exists, is enrolled at v7.1.0, and invokes a CLI tool that owns the inference** through
   an adapter interface a second engine could be added to without touching coordination.
6. ✅ **Every project on the machine is classified** active / benched / archived in a registry Drivr
   reads — `ai-stack`, `character-factory`, and the three projects P10 never listed included.
7. ✅ **`local-agent-runner`'s retention is decided on evidence** — kept for a named capability
   OpenCode does not provide, or retired — with the assessment recorded either way.
8. ✅ **The completion signal is trustworthy, or its limits are measured and stated** — validated
   against E33.2 Run A (must read *incomplete*) and E33.4 (must read *complete*) — and **G11 is
   closed** by real captured `epic_qa` runs.
9. ✅ **The lane runs unattended, serialized, without a human starting it**, and the gate queue is
   **derived** from governance state.
10. ✅ **Approval is in-app via a signed one-time link.** No chat reply authorizes anything, anywhere.
11. ✅ **Competing models review PRs and hold no authority** — findings feed the CFO's §11.6.1 diff
    review and resolve nothing.
12. ✅ **P9-GH-1 / P10-GH-9 are addressed or explicitly ruled safe** before Phase/Milestone agentic
    dispatch is wired.
13. ✅ **The parked items are recorded as explicit defers with their triggers** — P9-GH-3, P10-GH-1
    (if not folded), P10-GH-3, P10-GH-4, P10-GH-6, P10-GH-8, P10-GH-10, P8-GH-2, ComfyUI, the
    sidekick identity question — and **llama.cpp is recorded CLOSED, not parked.**

---

## Acceptance Criteria

The CFO (Layer 8) will accept P11 complete when:

- [ ] `AI-OPERATING-GUIDELINES.md`, `artifact-communication-protocol.md`, `chat-hierarchy.md`,
      `fleet-operator.md` and `fleet-operator-brief.md` cite SN-23 with dates, and no reader can reach
      "platform agnosticism was superseded" by following a citation
- [ ] The Layer-8/CFO note carries a non-colliding ID, and both prior citations footnote the change
- [ ] A steering-note ID allocation rule exists in the template and `creation-chat-guide.md`, and
      `tests/` fails on a duplicate `id:` (B3.1, may have landed earlier)
- [ ] One normative statement governs Creation Chat re-instantiation; the other surfaces cite it; the
      canonized path itself carries the E31.3 check; the `genesis.md` / Project Brief question is
      decided and recorded
- [ ] `system-hq.md` carries a Routing & Origination section recording D1–D3 with no new authority,
      no new decision rights and no new artifact type; the Authority Boundary is **shown** identical
      across all three documents post-edit; the issuer-vs-scribe rule is explicit
- [ ] The P10-GH-2 carry-forward text is amended to the re-diagnosed premise; the artifact-ID audit
      beyond steering notes is recorded with its finding (and escalated if it reaches the normative
      tier)
- [ ] A Drivr repository exists, is enrolled at `framework_version: v7.1.0`, and drives at least one
      real governed run end-to-end by invoking a CLI engine it does not implement
- [ ] A second adapter could be added without changing the coordination layer — demonstrated by the
      interface, not asserted
- [ ] Every project in `~/soft-dev` carries a registry classification; a validator enforces
      `ai-project-yml-spec.md` §4 (P10-GH-5)
- [ ] The `local-agent-runner` assessment is recorded with its outcome and reasons
- [ ] The completion judgment is validated against both known cases with the results recorded, and at
      least one real `epic_qa` run is captured (G11)
- [ ] The scheduler runs the serialized lane unattended; the gate queue is demonstrably computed from
      governance artifacts, not stored by hand
- [ ] Inbound approval is a signed one-time link; no path exists by which a chat reply authorizes
- [ ] At least two competing models (including GitHub Copilot) review PRs, with their findings-only
      ceiling recorded in the epics that configure them
- [ ] P9-GH-1 / P10-GH-9 are addressed, or a recorded HQ ruling states why dispatch is safe without
      addressing them
- [ ] Milestone-context evidence for `qwen3-coder:30b` exists as a fourth axis beside G-P4-a/b/c,
      **without** row P4 having been decided by it
- [ ] The full suite is green at delivery (**366 baseline**, no regressions, no skips introduced to
      route around changes) — for changes that touch this repo
- [ ] The phase closure declaration restates the parked/deferred items with their triggers and records
      llama.cpp as **closed**, not parked

---

## Dependencies

### Internal
- **v7.1.0 corpus on master** — PSG v2.4.0 / AOG v2.10.0, suite 366/0
- **PSG §11.6.1** — the CFO as mandatory diff reviewer for HQ-authored deliveries; the ceiling
  competing-model review feeds and never substitutes for
- **`governance/systems/chat-hierarchy.md`** — the ratified execution matrix, *mode is not authority*,
  and the handback / one-level escalation rules M38 supplies a detector for
- **`governance/systems/fleet-operator.md` + `fleet-operator-brief.md`** — the role P11's daemon is
  expected (not required) to implement, with its no-authority-on-speech Authority Boundary
- **M33/E33.1's enrolled-project procedure** (11 recorded failure modes) — E37.1's lever
- **`.ai-project/artifacts/escalation-notices/`** — the existing artifact type handback travels as
- **`model-routing-policy.md` row P4** and its G-P4-a/b/c gates — what M37's evidence sits beside
- **E35.5's back-test harness and committed ground truth** — what makes model-watch affordable
- **`governance/systems/bugfix-epic-workflow.md` + `docs/bugfixes/`** — B3.1's vehicle

### External / CFO-side
- **The Drivr repository** — does not exist at phase open; its creation is E37.1
- **OpenCode** — the execution engine. Its open issue #14551 (`run` exits 0 on session errors) is a
  **dependency the CFO does not own and cannot patch freely**; M38 is designed on that assumption
- **Ollama** — settled runtime (A1.3), measured at **0.30.0**, loading `qwen3-coder:30b` at a
  **32,768** context. The live trap is not a small default but the **8× gap between what
  `opencode.json` declares (262,144) and what is actually loaded** — see §P11.2
- **GPU / hardware** — one GPU, 16 GB VRAM shared with ComfyUI, `qwen3-coder:30b` partially offloading
  to RAM. This is the contention the scheduler exists for
- **GitHub Copilot** — PR-reviewer configuration is CFO-side
- **Premium/frontier quota** — Creation and HQ remain manual and paid, permanently (SN-22)

---

## Timeline

**Estimate:** 4 Milestones, ~18 Epics.

- M36 (Record Integrity and Documentation Hygiene): ~5 epics, in-repo documentation work, fast
- M37 (Drivr Inception / Registry / Adapter Surface): ~5 epics, the largest; a new repository from zero
- M38 (Trustworthy Completion Signal): ~3 epics; the long pole is validation against the known cases
- M39 (Coordination): ~5 epics, gated on M38

**~4 weeks**, deliberately loose. The estimate carries one honest risk: **M38's difficulty is unknown**
because nobody has yet built a completion judgment on this stack, and its failure mode is discovering
that the trustworthy signal is expensive. If that happens, M38 escalates rather than M39 starting
early — **the ordering is binding, not a preference.**

---

## Reference

### Governing Steering Notes
- **SN-27 + Amendment 1:**
  `.ai-project/artifacts/steering-notes/2026-07-31__creation-chat__steering-note__P11-drivr-spine.md`
  — the spine. Eight binding CFO decisions plus four amendment decisions. **Read including Amendment
  1**: one front-matter decision is marked `SUPERSEDED BY AMENDMENT 1` and the superseded roster must
  not be read as binding.
- **SN-26:**
  `.ai-project/artifacts/steering-notes/2026-07-31__creation-chat__steering-note__creation-reinstantiation-ritual.md`
  — re-instantiation ritual unexecutable; P10-GH-2 misdiagnosed. **Binding CFO decision: tightening,
  not phase scope — it must not shape the spine.** Placed in M36.
- **SN-28:**
  `.ai-project/artifacts/steering-notes/2026-08-01__creation-chat__steering-note__sn-numbering-unenforced.md`
  — ID allocation unenforced; SN-23 and SN-1 double-claimed. **Binding CFO rulings: normative
  amendments to P11's first milestone; the duplicate-ID test as a hotfix.**
- **SN-24** (ruled, not re-attached):
  `.ai-project/artifacts/rulings/2026-07-28__ai-project-system-hq__ruling__sn-24-m35-operator-form.md`
  — headless-first, the rented chat half, four-project ecosystem, gates in-app, the human inside the
  graph. **Not amended by anything in P11.**

> **Convention** (stated in the 2026-08-01 opener, recorded here so it holds): an opener carries
> **unconsumed** Steering Notes as *agenda* and **ruled** ones as *constraints* — cited by their
> ruling, never re-attached as notes. Re-attaching a ruled note invites re-deciding what is decided.

> **Citation caution:** *"SN-23" is ambiguous in this corpus.* **2026-07-18** = reference-first /
> platform agnosticism; **2026-07-20** = the P10 adoption spine. Every SN-23 citation in this spec
> carries its date. M36 fixes the rest of the corpus.

### Governing Rulings
- `.ai-project/artifacts/rulings/2026-08-01__ai-project-system-hq__ruling__p11-opening-and-sn-26-27-28-triage.md`
  — opens this phase; answers the namespace question; places SN-26/SN-28; authorizes B3.1; triages
  every carry-forward
- `.ai-project/artifacts/rulings/2026-07-31__ai-project-system-hq__ruling__system-hq-routing-codification.md`
  — SN-1 accepted, D1–D4, executed by M36/E36.4
- `.ai-project/artifacts/rulings/2026-07-31__ai-project-system-hq__ruling__milestone-locality-row-p4.md`
  — row P4 stands; **not reopened** by M37's evidence
- `.ai-project/artifacts/rulings/2026-07-30__ai-project-system-hq__ruling__sn-25-handback-and-execution-matrix.md`
  — handback, one-level escalation, the ratified matrix, *mode is not authority*

### Key Reference Documents
- `.ai-project/artifacts/hq-openers/2026-08-01__hq-chat-opener.md` — the opener instantiating this
  scoping session, filed verbatim for the artifact record
- `docs/phases/P10__Fleet_Adoption_and_Local_Inference_Proving/P10__phase-closure-declaration.md` —
  carry-forward definitions (P9-GH-1/3, P10-GH-1…GH-10) verbatim
- `docs/bugfixes/B3.1__spec__steering-note-id-allocation-unenforced.md` — authorized, may land before
  M36 opens
- `anomalyco/opencode` issue **#14551** — `run` exits 0 on session errors; M38's external constraint

### Binding Decisions (settled — NOT for re-debate)

**From SN-27, the CFO's:**
1. **P11 is Drivr.**
2. **An app is made AI-powered by calling a CLI tool that owns the inference** — the architectural
   basis of Drivr.
3. **Drivr must be able to use any CLI tool that empowers the work.** Execution is a pluggable adapter
   surface; no engine is fixed by the architecture.
4. ~~Two-lane roster~~ — **superseded by A1.1: OpenCode covers local and cloud; one tool currently
   covers both.** Decision 3 is unaffected and is *why* this cost nothing.
5. **Three fleet states** — active, benched, archived.
6. **The orchestrator schedules agentic runs to avoid overloading the system.**
7. **Competing models review PRs, including GitHub Copilot — surfacing findings only, no authority.**
8. **The leverage case is a choice:** a way of working that keeps the CFO competitive in the industry.
   Not revenue, not a platform.

**From Amendment 1:**
- **A1.1** — OpenCode covers the local lane; the two-lane split is retired.
- **A1.2** — `local-agent-runner` is retained only if it still provides something. Directed
  assessment, real possibility of retirement, **not** a judgment on the work.
- **A1.3** — **The local-inference RUNTIME question is CLOSED.** Ollama settled; llama.cpp dropped by
  decision, trigger void.
- **A1.4** — **The MODEL roster stays open.** Milestone-context capacity is a fourth axis; row P4 not
  reopened.
- **A1.5** — A sole engine concentrates the completion-signal problem in a dependency the CFO does not
  own. M38 is more urgent, not less.

**From SN-24, carried unamended:** headless-first; the chat half is rented; gates in-app only; push
and WhatsApp deferred; **inbound approval is never a chat reply**; the human is a node *inside* the
governance graph, not an operator above it.

**Standing:** **Mode is not authority.** An instance running unattended holds exactly the authority its
level always held. **PSG §11.6.1** — the CFO is the mandatory diff reviewer for HQ-authored deliveries.

### HQ Triage Decisions (2026-08-01 ruling)

| Item | Decision | Where |
|---|---|---|
| Milestone shape | **4 milestones**, M36 → M37 → M38 → M39, binding order | Milestones |
| M36 first, contents fixed | **CFO ruling**, not HQ's call to revisit | P11.1 |
| Namespace question (SN-28 RA1) | **Answered by HQ:** one sequence per directory, regardless of issuer | P11.1 |
| SN-23 collision (SN-28 RA2) | **HQ ratifies date-qualification, no renumbering.** Rule: a bookkeeping defect never rewrites a normative citation | P11.1 |
| Duplicate-ID test (SN-28 RA4) | **Authorized as B3.1**, medium severity, Bugfix Epic vehicle; **HQ delegates execution, does not perform it** | `docs/bugfixes/` |
| P10-GH-7 | **In scope, M38 owns it, M39 gated on it** | P11.3 |
| P10-GH-5 | **Folded into M37** — the registry reads every enrolled config | P11.2 |
| P10-GH-1 | **Conditional fold-in to M37**, Phase Chat's judgment | P11.2 |
| P9-GH-1 / P10-GH-9 | **Owner assigned at M39**, the milestone that wires dispatch (P10-GH-9's own trigger) | P11.4 |
| Competing-model review | **Un-parked**, M39 owns it, findings-only ceiling explicit | P11.4 |
| llama.cpp trial | **CLOSED by decision**, not parked; trigger void | Out of Scope |
| SN-26 | **Recorded, placed in M36**, shaped nothing in the spine | P11.1 |
| SN-28 Carry-Over 3 (unaudited families) | **Bounded audit in M36. Reports; does not fix.** Escalates if it reaches the normative tier | P11.1 |
| P10-GH-8 | ~~Not mandated; Phase Chat may propose folding into M36~~ → **SCHEDULED as M37/E37.6** (HQ Ruling 2026-08-04). Its revisit trigger fired inside M36. Convention decided once for all 17 documents, forward-looking only; **not** a B-series bugfix; M36 stays at four items | P11.2 |
| P9-GH-3, P10-GH-3/4/6/10, P8-GH-2, ComfyUI | **Parked** on existing triggers, restated | Out of Scope |
| Seven SN-27 `[PROPOSED]` items | **Returned to the CFO unacted.** Items 5/6/7 independently re-decided on HQ's own authority | Open Items |

### Open Items — Returned to the CFO

Four Creation-Chat proposals remain unowned. **None blocks a milestone**; each has a fallback the
affected milestone executes if no answer arrives:

| Proposal | Fallback if unanswered |
|---|---|
| Drivr may *propose* a fleet-state transition, never execute one | M37 builds transitions as a **recorded human action**. Nothing automatic. |
| The `local-agent-runner` retention bar (*"names a capability P11 needs that OpenCode does not provide"*) | E37.4 tests the two named candidate capabilities and **reports without retiring**. |
| Model-watch as cheap re-tests against E35.5's harness rather than scheduled investigations | No watch is scheduled. The harness stays available; nothing is committed to. |
| The engine-comparison spike (OpenCode `run` vs `local-agent-runner` on `proof/`, same model, same host) | Not run. M38 validates the completion signal against the known cases regardless of engine count. |

Proposals 5, 6 and 7 from SN-27 (SN-1/SN-26 placement, P9-GH-1 owner timing, registry-resolves-the-
unenrolled) are **also** returned, and are **independently decided by HQ** above — same destination,
different authority. That distinction is deliberate.

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.3 | 2026-08-05 | **E37.7 added, HQ Ruling 2026-08-05**, resolving E36.5's bounded artifact-ID audit (SN-28 Carry-Over 3), escalated Epic → Milestone → Phase → HQ. The audit found **no ID collision** — the `GH-` namespace held at 38 live IDs across six phases — but a **citation-form** failure with SN-23's reader-level consequence: a shorthand resolving to more than one artifact, in the normative tier. Four answers, all placed in **E37.7**: disambiguate the bare `GH-10` at `PSG:605` (the only namespace-stripped `GH-<n>` in the corpus, in the highest-authority document); `GH-` citations carry the phase prefix in `governance/`; escalation notices are cited by **full filename** (two already share the `P10-M34` key, and the reporting notice was itself the second `P11-M36`); and the `GH-` prefix names the **phase that filed it**, permanently — *the record names the disposition, the identifier names the origin* — with the forward-allocated `P6-GH-10…15` / `P7-GH-16…21` **ratified as historical exceptions, not renumbered**. `rulings/` date-shorthand ambiguity affirmed report-and-leave (every `governance/` citation resolves). **Not a B-series bugfix** — it edits governance documents, the same boundary held on 2026-08-01 and 2026-08-04. **M36 not reopened.** HQ additionally constrains itself: **nothing further is placed in M37 without reconsidering the milestone's shape**, and the Phase Chat's permission to split M37 is upgraded from permitted to **recommended**. Touches §Milestones→M37 (+E37.7). No milestone ordering, decision, or scope boundary otherwise changes. |
| 1.0.2 | 2026-08-04 | **P10-GH-8 scheduled, HQ Ruling 2026-08-04**, resolving the P11-M36 escalation (M36 Milestone Chat → Phase Chat → HQ). P10-GH-8's own revisit trigger fired inside M36: E36.1 added a 76-line normative section to `creation-chat-guide.md`, a document with no `version` and no `## Changelog`, and could not record it. Verified independently: **17** documents in `governance/systems/`, **7** compliant, **10** not — the set has not shrunk in five weeks. **The convention is decided once here** for all 17: `version` + `## Changelog`, unversioned documents seeded with a first row pointing at git for prior history, **no backdated reconstruction (permanently out of scope)**. **Vehicle declined:** not a B-series bugfix — it would edit ten governance documents, and the SN-28 Decision 5 carve-out is bounded at *"the moment an item would edit a governance document it leaves the bucket"*; nothing here is urgent and the escalation states twice that nothing is blocked. **Placement: M37 as standalone epic E37.6**, joining P10-GH-5 and conditional P10-GH-1 — M37 is already this phase's home for P10-GH hygiene. **M36 stays at four items** (Option A declined by the Phase Chat under its own authority, affirmed). Interim: M36's Closure Declaration MUST record its two unrecordable amendments explicitly. Touches §Milestones→M37 (+E37.6), §HQ Triage Decisions (P10-GH-8 row). No milestone ordering, decision, or scope boundary otherwise changes. |
| 1.0.1 | 2026-08-01 | **Factual correction, HQ, before any Phase Chat read the spec.** v1.0.0's binding technical note to the OpenCode adapter stated that Ollama defaults every model to a 4,096-token context. **It is false on this host.** The claim was inherited from the 2026-08-01 HQ Chat Opener and passed into this spec unverified — an HQ error, recorded rather than quietly overwritten. Measured against Ollama **0.30.0**: `qwen3-coder:30b` and `qwen2.5-coder:7b` both load at **32,768**, a 20,530-token prompt recovers a marker planted at position 0 with no options set, and the `/v1` endpoint **silently ignores `options`** (forcing `num_ctx=2048` changed nothing). The note is replaced with the measurements, the reproduction method, and the **real** caution: `opencode.json` declares 262,144 against 32,768 loaded — an **8× overpack** that bites long sessions, so the adapter must derive its declared limit from `/api/ps`. Touches §P11.2 (technical note; `local-agent-runner` transport difference recorded as **not** an E37.4 retention argument), §Milestones→M37 (E37.2), §Dependencies (Ollama). **No milestone, ordering, decision, or scope boundary is changed** — M38 still gates M39 and P10-GH-7 stands untouched, its E33.2/E33.4 evidence unaffected (those runs did not truncate). |
| 1.0.0 | 2026-08-01 | Initial P11 phase spec. Four milestones (M36 Record Integrity and Documentation Hygiene — CFO-decided first; M37 Drivr Inception, Fleet Registry and Execution Adapter Surface; M38 Trustworthy Completion Signal; M39 Coordination — Scheduler, Derived Gate Queue and Thin Surface), ~18 epics, binding order M36 → M37 → M38 → M39. Scoped by SN-27 + Amendment 1 (spine: Drivr rents both halves — an app is made AI-powered by calling a CLI tool that owns the inference; execution is a pluggable adapter surface; three fleet states; scheduler; competing-model review findings-only; the leverage case as a choice). SN-26 and SN-28 placed in M36 per CFO ruling; the namespace question answered by HQ (one sequence per directory); SN-23 date-qualified rather than renumbered. P10-GH-7 in scope and gating M39; P10-GH-5 folded into M37; P9-GH-1/P10-GH-9 owned at M39; competing-model review un-parked. llama.cpp recorded **closed**, not parked. Four SN-27 proposals returned to the CFO with recorded fallbacks. |
