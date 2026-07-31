---
phase: P10
name: Fleet Adoption and Local-Inference Proving
status: scoping
start_date: 2026-07-20
planned_end_date: 2026-08-10
version: 1.3.1
---

# Phase P10: Fleet Adoption and Local-Inference Proving

## Executive Summary

The framework is done being built. Through P9 every chat level works, visual artifacts are
real, the token cost model is measured, working levels have a manual/agentic switch, and the
system-level participant is canonized — the corpus stands at v7.0.0, suite 363/0. What has
**not** happened is the framework doing its job in the wild: of ten projects in `~/soft-dev`,
eight are enrolled but enrollment is shallow — a scaffold dropped in and mostly never run — and
**no project except the framework itself is confirmably on v7.0.0.** The machinery works; it has
not yet been used.

**P10's spine is fleet adoption of v7.0.0: get the CFO's real projects actually running under
governance, so progress happens in every governed project and not just this one.** Per SN-23
(Creation Chat, 2026-07-20, all decisions CFO-ratified), P10 is an **adoption phase, not a
capability-building phase.** No new framework capability is built on spec; no third spin-off is
spawned. The convergence is deliberately toward doing *less*.

Three commitments define the phase:

1. **The operating posture is fixed, not a per-project menu.** The agentic/manual × local/paid
   matrix resolves into one posture that holds for every project: **Manual/Paid from Creation
   down through Milestone; Agentic/Local at the Epic.** The other two cells (Agentic/Paid,
   Manual/Local) are technically possible and revisitable later, but off the P10 critical path.

2. **Adoption is proven on a pair before it is spread.** `home_finance` and `local-agent-runner`
   are furthest along (canonical `governance.agent.md` already installed), so the first real
   Agentic/Local epic runs there with the least yak-shaving. The dormant enrolled projects are
   sequenced behind them.

3. **Run-first ordering.** Measurement and validation come **out of real epic runs, not before
   them.** The measurement tool cannot prove a claim about work that has not run. This resolves
   the 2026-07-20 Progress Digest's Decision 2 with a third option HQ had not offered: not "fix
   measurement then prove the spine," nor "accept the hand numbers and move on," but "run real
   epics, then measure and validate what actually happened."

The one open **risk** gating all of it is the **local-inference substrate.** The framework is
ready; the local stack is not yet proven in the wild. `local-agent-runner` is built on Ollama; a
reference setup the CFO is drawn to (Qwen3.6 27B, Q8_0, llama.cpp — which recommends against
Ollama) points the other way. **The runtime fork is settled by the first real epic on the
proving pair, not decided in the abstract and then adopted.**

Three milestones:

1. **M33 — Proving Pair: v7.0.0 + First Real Agentic/Local Epic** — bump the pair to v7.0.0, run
   the first real Agentic/Local epic, settle the Ollama-vs-llama.cpp runtime question from that
   run, and produce the trustworthy burn/validation evidence run-first ordering promises (P9-GH-2
   fixed only as far as trusting that run's numbers requires).
2. **M34 — Fleet Roll-forward** — the dormant enrolled projects (courtis, Getawayinsured2023,
   ai-project-system-mcp) roll under v7.0.0 by end of phase, including the ai-project-system-mcp
   superseded-agent fix (P6-GH-15 live in the wild).
3. **M35 — System-Operator Canonization** — the **fleet operator role** (implementation
   form-neutral; expected but not required to be the Drivr daemon, P11): runs the serialized
   local-inference lane and keeps registered projects current on governance version, with
   **no authority to act fleet-wide on a spoken word**, plus its standing brief (what the
   operator needs each cycle — amended from a daily chat-spawn ritual, SN-24 / HQ Ruling
   2026-07-28). Also records that **a blocked autonomous instance must hand back to its
   immediate parent** via escalation notice, that escalation travels exactly one level, that
   Creation Chat's awareness of escalations is visibility-only, and ratifies an **execution
   matrix** restoring agentic mode at Phase/Milestone (mode is not authority — Stage-2
   accept/merge still require the human's key) while directing an evidence-gathering evaluation
   of Milestone × local inference (SN-25 / HQ Ruling 2026-07-30).

---

## Vision

By the end of P10:

- ✅ **The proving pair runs under v7.0.0 for real.** `home_finance` and `local-agent-runner` are
  stamped at `framework_version: v7.0.0` and each has carried at least one real Agentic/Local epic
  end-to-end under the fixed posture — not a scaffold, an actual governed run.
- ✅ **The local runtime question is settled by evidence.** The first real epic's run record
  states the decision — keep Ollama, or switch the runner to llama.cpp + Qwen3.6 — with the
  reasons the run itself produced. The abstract debate is closed by a run, not a memo.
- ✅ **Adoption produced its own measurement and validation.** Run-first ordering delivered:
  there is trustworthy burn/validation evidence from a real epic run, and `measure-token-burn` is
  honest enough against that real data to trust its output (P9-GH-2 closed to the extent M33
  needs).
- ✅ **The fleet is rolling under v7.0.0.** The dormant enrolled projects are on the P10 roadmap
  with a recorded path to v7.0.0 and are moving along it; ai-project-system-mcp no longer carries
  the superseded `hq.agent.md` (P6-GH-15 resolved in the wild).
- ✅ **The fleet operator role is canonized** (form-neutral — chat, daemon, cron job, or a
  person with a terminal; expected but not required to be Drivr, P11). Its role (run the lane,
  keep projects current) is recorded, the **no-authority-on-speech seam** is normative ("update
  every project to v7.0.0" is a fleet-wide write that must not execute on speech alone), and its
  standing brief exists — what the operator needs each cycle, usable regardless of what
  implements the role.
- ✅ **Autonomy can hand back, and the chain terminates at a human.** A blocked autonomous
  instance escalates to its immediate parent, one level at a time, guaranteed to reach a manual
  level (Creation/HQ, permanently manual per SN-22) in a bounded number of hops. Creation Chat's
  awareness of the chain is recorded as visibility only. The execution matrix is ratified —
  Phase and Milestone may run agentically — with mode explicitly not conferring authority:
  Stage-2 acceptance and merge still require the human's key.
- ✅ **The Milestone × local-inference question has real evidence, not an assertion either way.**
  A local model's Stage-2 review has been back-tested against the phase's own known defects
  (M33's decomposition gap, E33.2's false positive, E33.4's false negative, M34's dirty-entry
  miscount, P10-GH-6), measuring review quality rather than throughput or cost.
- ✅ **Progress happened in more than one repo.** The phase's evidence shows governed work
  advancing in the CFO's real projects, which is the entire point.

---

## Scope

**A note on where P10 work lands.** This is the framework's first phase whose deliverables live
substantially in **other repositories.** A version bump and a real epic on `home_finance` change
that repo, not this one. The framework repo (`ai-project-system`) holds the **governance record**:
the phase spec, milestone/epic specs, execution-chat starters, delivery/closure artifacts, and
the captured evidence (run records, burn data, runtime decision). The Milestone and Epic Chats
own the mechanics of driving a governed run in a target repo; HQ scopes the problem, not the
resolution. "Adopt all" is therefore not one action but three per project — **cleanup, version
bump to v7.0.0, then the first real Agentic/Local epic.**

### P10.1: Proving Pair — v7.0.0 + First Real Agentic/Local Epic (M33)

The spine. On `home_finance` and `local-agent-runner` — the two projects with canonical
`governance.agent.md` already installed:

**Version bump to v7.0.0.** Stamp each project at `framework_version: v7.0.0` and bring its
installed governance to the current corpus (the mechanics of a version bump on an enrolled
project are the Milestone/Epic Chat's design decision — a documented, repeatable procedure is the
valuable byproduct).

**Run the first real Agentic/Local epic under the fixed posture.** A genuine unit of that
project's own work, scoped and reviewed Manual/Paid from Creation through Milestone, executed
Agentic/Local at the Epic. Not a synthetic demo — a real epic that advances the project. The
run record is the phase's most important evidence.

**Settle the local runtime question from that run.** The first real epic is the experiment that
resolves the substrate risk: keep Ollama, or switch the runner to llama.cpp + Qwen3.6 27B Q8_0
(the reference setup, which recommends against Ollama and benchmarks on Mac unified memory). The
decision is **recorded with the run's own reasons** — quality, throughput, loadability, review
burden — not decided in the abstract. Adopt on the proving pair and let the first epic settle it.

**Trustworthy measurement, out of the real run (P9-GH-2, folded in per HQ triage).** Run-first
ordering says measurement comes out of real runs. That requires the run's numbers to be
trustworthy, and P9-GH-2 records that `measure-token-burn` cannot verify its own reduction
claims. Scope: capture real burn/validation data from the proving-pair epic and fix/validate
`measure-token-burn` **only as far as trusting that run's numbers requires** — honest against real
data, not perfected in the abstract. The extent is conditional, sized by what the run needs.

### P10.2: Fleet Roll-forward (M34)

Sequenced behind the proving pair. The dormant enrolled projects roll under v7.0.0 by end of
phase — not urgent, but moving:

- **courtis, Getawayinsured2023** — dormant, artifacts dir near-empty. Roadmap each onto v7.0.0:
  cleanup, version bump, and (where the project is ready) a first governed epic. The repeatable
  bump procedure from M33 is the lever. (`fieldledger-assesment`, originally listed here, was
  dropped 2026-07-29 — a screening project, not a real adoption target; direct CFO instruction.
  See Changelog v1.2.0.)
- **ai-project-system-mcp** — carries the **superseded `hq.agent.md`** (P6-GH-15 sitting live in
  a real project); artifacts near-empty. Replace it with the canonical `governance.agent.md` and
  bring it to v7.0.0. This closes P6-GH-15 in the wild.
- **footboard** — some artifact activity (7 files), no canonical agent. Bring under v7.0.0 with a
  canonical agent as the roadmap reaches it.

The blast-radius **goal** is all enrolled projects. M34 does not require every project to have run
an epic by phase close; it requires each to be **rolling** — on the roadmap with a recorded path
to v7.0.0 and demonstrable movement along it.

### P10.3: System-Operator Canonization (M35)

*(Re-scoped in one pass, 2026-07-30, per HQ Ruling on SN-25, Decision 6 — folding in both the
SN-24 operator-form amendment (2026-07-28, form-only) and SN-25's additions (2026-07-30: handback,
one-level escalation, Creation Chat awareness, the execution matrix, the Milestone × local
evidence mandate). M35 had been amended once already (v1.1.0) and had still not opened; rather
than patch a second time, HQ directed a single clean re-scope from current understanding. See the
Amendment History entry and both rulings:
`.ai-project/artifacts/rulings/2026-07-28__ai-project-system-hq__ruling__sn-24-m35-operator-form.md`,
`.ai-project/artifacts/rulings/2026-07-30__ai-project-system-hq__ruling__sn-25-handback-and-execution-matrix.md`.)*

Advances the standing SN-21 System-participant work into the operator role SN-23 describes, and
adds the obligations SN-25 found the operator record under-specified without. Independent of
M33/M34 in dependency; schedulable by the Phase Chat where it fits. **M35 stays in P10** —
recording the rules is governance; only the mechanisms wait for P11 (Decision 8, both rulings).

**The fleet operator runs the fleet.** Record normatively that the fleet operator runs the
serialized local-inference lane, decides what runs next, and keeps registered projects current on
governance version ("make sure all registered projects have the latest governance version").
Creation Chat remains the source of governance knowledge; the operator remains the hands. **The
operator's implementation is form-neutral and lives outside this repo's governance corpus** — a
chat window, a daemon, a cron job, or a person with a terminal are all admissible; the role and
its boundary hold regardless of which one fills it. It is expected, but not required, to be
implemented by the Drivr daemon (P11) — this record does not depend on that.

**The no-authority-on-speech seam (load-bearing).** The fleet operator holds **no authority to
act fleet-wide on a spoken word.** A request to it is a proposal until it carries authority behind
it — the same rule that governs the Creation Chat. "Update every project to v7.0.0" is a
fleet-wide write and must not execute on speech alone. This is the seam that must not recreate,
one level down, the very thing the framework exists to prevent. It is recorded normatively, and
generalizes cleanly across implementations — a daemon has no speech at all, only gates, which
makes the seam stronger, not weaker, under that form.

**Operator's standing brief.** The operator needs a standing brief — what it needs to know each
cycle to run the lane and keep the fleet current, within the authority boundary above — analogous
in content to the Creation Chat's Genesis seed (restates the SN-22 open item that M32/E32.2
began), but **form-neutral**: a document a chat re-reads each day, a daemon loads on boot, or a
human consults, not a daily-spawn ritual tied to any one of those.

**The serialized lane, hand-run first.** Enrollment (all projects eligible to run) and concurrency
(one reasoning job at any instant) are different axes and do not conflict. Epics run back-to-back
through a **single serialized local-inference lane** — near-24/7 means the lane stays busy, never
idle, never two reasoning jobs at once. With at most two or three projects able to run an epic
this week, a contention problem is not yet possible: **the CFO (optionally with the fleet
operator) IS the lane for now.** M35 canonizes the operator role and the hand-run lane; a built
scheduler is constructed only when real contention bites — that friction defines P10's later
scope rather than a guess up front.

**Handback is a role obligation (SN-25 Decision 1).** An autonomous execution instance that
becomes **blocked** — it has encountered something requiring judgment it cannot supply — must be
able to surface that block, with enough context for the receiving level to act, and the resulting
intervention is **authority-bearing**. An autonomy that cannot hand back is not autonomy; it is an
unattended process that fails silently. The handback travels as an **escalation notice** —
already an existing artifact type, exercised by hand twice in M34; no new artifact type, no new
authority model. **The destination is the immediate parent, not "a human"** — an instance has no
way to identify or select a human directly. The human is reached because the chain **terminates
at a manual level by construction**: Creation and HQ are manual-only, permanently (SN-22), so
every escalation that keeps escalating arrives at a human in a bounded number of hops.
Termination is guaranteed by SN-22, not by hope. How that arrival is surfaced to the human (a
chat window opening, a notification, a dashboard) is **coordination and is P11's** — governance's
part ends at "the notice is emitted, reaches the parent, and carries enough context to act on."

**Escalation travels exactly one level (SN-25 Decision 2).** An escalation notice targets the
issuing instance's **immediate parent and nowhere else.** The parent then decides the next step's
direction: **resolve and return** to the child, or **issue its own notice** one level further up.
No instance names a target above its parent; no level is skipped. The child's job is to describe
the blocker fully — nature, what was attempted, what it could not resolve; judgment about the
*problem* stays nearest the problem, judgment about *where it goes* stays with the level holding
authority over it. This is a restoration of the framework's existing design, not a new rule —
instance-judged routing was considered and rejected because it lets a child choose its own judge
(an Epic routing straight to HQ steps around its Milestone's Stage-2 authority, and the parent may
never learn its own epic is blocked). M34's own escalation is the worked example: the Milestone
Chat could not open, its parent Phase Chat diagnosed and issued its own notice to HQ, and HQ
ruled — two hops, no level skipped. **This does not close P9-GH-1** (the merge-authorization hole
at Milestone→Phase and Phase→HQ) — the two are adjacent protection, not the same fix, and a
future reader must not conflate them. **The CFO is not a level in the chain** and may answer at
any point without that being a bypass; the obligation a direct CFO answer creates is *recording*
— the decision must land where the level that would otherwise have ruled can see it (the M34
`fieldledger-assesment` resolution is the worked example of this, too).

**Creation Chat awareness is visibility, never authority (SN-25 Decision 3).** The Creation Chat
is aware of all escalation notices wherever they arise in the chain — a **retrieval** property
over committed artifacts (a re-instantiated Creation Chat reads the directory), never a
subscription, and never a seat. **Seed Rule 3 stands: the Creation Chat holds no governance
authority.** Awareness must never make it a decision point or a resolution path. Awareness has
exactly one legitimate outlet: the Creation Chat may **issue a steering note to HQ** —
direction-setting, not resolution — which is how SN-23, SN-24, and SN-25 themselves arrived.
Naming the outlet explicitly is what keeps awareness from drifting into "the Creation Chat
unblocked it."

**The execution matrix is ratified; mode is not authority (SN-25 Decision 4).** SN-23 Ratified
Decision #2 (Manual/Paid from Creation through Milestone; Agentic/Local at the Epic) is
**superseded on the Execution Mode axis only** — see the Ratified Decisions footnote below. The
locality axis stands, with Milestone under evaluation (next paragraph):

| Level | Execution Mode | Inference locality |
|---|---|---|
| Creation | Manual only (permanent, SN-22) | Remote |
| HQ | Manual only (permanent, SN-22) | Remote |
| Phase | Agentic or manual | Remote |
| Milestone | Agentic or manual | Remote — **local under evaluation** |
| Epic | Agentic or manual | Local or remote (in force, E34.3) |

At Phase and Milestone the change is dispatch, not permission — `governance/systems/chat-hierarchy.md`
(P9-M31-E31.1) already made Execution Mode normative at those levels and recorded that no dispatch
mechanism yet consumes the declaration; SN-23 narrowed it for P10, and this restores the E31.1
baseline. **Mode is not authority.** Restoring agentic mode at Milestone says an instance at that
level *may run unattended* — it does **not** widen what that instance may *authorize*. Milestone
is where Stage-2 accept authority lives, and errors there propagate into merges. **Until ruled
otherwise, authority-bearing acts — Stage-2 acceptance and merge authorization — still require the
human's key, whatever mode the instance is running in.** Mode is what may run; gates are what may
be decided without a key; conflating them would let a mode restoration silently widen authority.
Per-level gates remain a requirement and stay revisitable (SN-24). Technical possibility remains
not sufficient reason — this is a bounded position, not a removal of limits.

**Milestone × local inference — collect evidence, decide on the result (SN-25 Decision 5).** The
cell is **neither opened nor closed** — it opens or closes on evidence, run-first (SN-23 #4). What
must be measured is **review quality, not throughput or cost**: `model-routing-policy.md` row
P4's reason for paid frontier is that Milestone holds Stage-2 accept authority and its errors
propagate into merges, not price. **The sufficiency bar, stated concretely:** a local model's
Stage-2 review is a candidate for the cell if it **back-tests successfully against defects with
already-known ground truth** — at minimum, M33's decomposition gap (E33.4), E33.2 Run A's
false-positive completion, E33.4's false-negative completion, M34's footboard dirty-entry
miscount, and P10-GH-6's starter-lint false positive — catching what was caught and flagging what
was missed, on material it was not told the answer to. A pass is necessary evidence, not by
itself sufficient to move row P4. ~~`Getawayinsured2023`'s live `.ai-project.yml` (`phase` and
`milestone` already pointed at a local model) is a legitimate override... and may be harvested as
a natural experiment~~ — **premise corrected 2026-07-31 (E35.5 Stage-2 finding; escalation notice
`2026-07-31T00_00_00Z__P10-M35__escalation_notice.md`).** `Getawayinsured2023` routes `phase`/
`milestone` to `remote:qwen3.6:27b`, not a local endpoint — it is a legitimate override on the
**model/tier** axis (a non-frontier open-weights model where rows P3/P4 specify paid frontier)
and is **silent on locality**. **No fleet project was running the Milestone level on local
inference; there is no natural experiment to harvest.** This does not weaken E35.5's own
back-test evidence (which ran `qwen3.6:27b` locally against blinded material and stands on its
own), but it removes the corroboration this spec assumed was available — **the evidence base for
opening the Milestone-locality cell is thinner than this section originally stated.** See the
Changelog v1.3.1 entry. The result may still amend row P4 independently of the row's own unfired
revisit trigger — a trigger is a prompt to
revisit, not a precondition for it — and P4 does not wait on P9-GH-3 (still carried forward,
unowned).

**Block detection is the load-bearing risk — P10-GH-7 (SN-25 Decision 7).** You cannot escalate on
a block you cannot detect, and detection is measured broken in both directions: E33.2 Run A
returned exit 0 having done zero work (the validation command would have passed on the unchanged
repo); E33.4 returned exit 2 having produced complete, green work. Corroborated across two
projects: **the exit code is not a completion signal on this stack.** Compounding it, **G11
stands** — zero captured QA-role runs, so the lane that would supply a trustworthy signal has
never been exercised. Any handback mechanism built over this signal yields either constant false
escalations (the human becomes the bottleneck again, worse than before) or silent no-ops that read
as success. Recorded now because recording it costs nothing and building on it costs everything;
owner unassigned, carried forward to the P10 closure declaration alongside P10-GH-1…GH-6.

**Nothing here is built in P10 (SN-25 Decision 8, reaffirming SN-24's).** M35 records the rules;
P11 builds the mechanisms. No block detector, no mode switch, no runner→chat channel, no dispatch
wiring for Phase/Milestone agentic declarations, and no push-notification work (deferred under the
SN-24 ruling) is scoped here. The domain split: executing larger units and being invocable from a
manual chat is **execution** (Local Agent Runner); deciding when to run, detecting the block,
switching mode, and surfacing the intervention is **coordination** (Drivr, P11); the rule that
autonomy must hand back, that escalation travels one level, and that intervention is
authority-bearing, is **governance** (this repo).

---

## Out of Scope

- **New framework capability built on spec.** P10 is adoption, not capability. Nothing is built
  because the spec says so; work enters only as real adoption friction surfaces it (SN-23).
- **A third spin-off project.** Not spawned in P10 (SN-23). The "software factory" spin-off (SN-20
  Carry-Over 2) remains a future Creation Chat item.
- **A built local-inference scheduler.** Hand-run the lane first. Constructed only when real
  contention bites (SN-23). The CFO is the lane for now.
- **Competing-model code review.** Parked. Near-standard practice and the substrate exists (CFO
  merge gate, Stage-2 at every parent, multi-model-capable runner), but the open design question
  is the second reviewer's **authority** (advisory vs blocking) and it touches P9-GH-1. Enters
  scope only on adoption friction (SN-23).
- **P9-GH-1 — the merge-authorization hole** still open at Milestone→Phase and Phase→HQ. Parked;
  enters scope only on adoption friction (SN-23). Not P10 spine.
- **P9-GH-3 — within-session context segmentation.** Carried from P9 unowned; not adoption spine.
  Recorded as deferred, enters scope only if it blocks an adoption run.
- **ComfyUI precision investigation.** Parked; non-blocking CFO-side track, enters scope only on
  adoption friction (SN-23, continuing the P8/P9 posture).
- **P8-GH-2 — machine-local visual-artifact hosting (Low).** Remains deferred on its recorded
  trigger: revisit only if cloud-reachable hosting is ever actually needed. Not scoped.
- **The two unenrolled projects (ai-stack, character-factory).** Noted, not addressed — decide
  later whether they are real projects to govern or leftovers (SN-23). Not P10 work.
- **The "mighty" governing System Chat / fleet-wide write authority.** Pinned vision item. M35
  canonizes the operator role **with the no-authority-on-speech seam intact** — no expansion of
  authority.
- **The handback/escalation mechanisms themselves.** M35 records that a blocked instance must
  hand back and that escalation travels one level; it does not build a block detector, a
  mode-switch trigger, a runner→chat channel, or dispatch wiring for Phase/Milestone agentic
  declarations. These are P11 (SN-25 / HQ Ruling 2026-07-30, Decision 8).
- **P9-GH-1 remains open — the one-level escalation rule does not close it.** Adjacent
  protection against the same authority class, not the same fix (SN-25 ruling Decision 2). Not
  to be silently conflated at any future reading.
- **A decision on Milestone × local inference.** M35 directs and conducts the evidence-gathering
  evaluation; it does not itself decide whether to move `model-routing-policy.md` row P4. That
  is a further HQ call on the evaluation's result (SN-25 ruling Decision 5).
- **Sidekick-for-external-projects (adapting this governance to serve teams that hire the CFO).**
  An **identity question** — Project-Brief territory (pivot vs addition) — deliberately NOT decided
  here. Noted so P10 does not inherit an unstated pivot (SN-23).

---

## Milestones

### M33: Proving Pair — v7.0.0 + First Real Agentic/Local Epic

**Goal:** On `home_finance` and `local-agent-runner`, bump to v7.0.0, run the first real
Agentic/Local epic under the fixed posture, settle the Ollama-vs-llama.cpp runtime question from
that run, and produce trustworthy burn/validation evidence out of the run.

**Indicative Epics** (the Milestone Chat owns final decomposition):
- **E33.1 — Enrolled-project v7.0.0 bump procedure + apply to the pair.** A documented, repeatable
  procedure for bumping an enrolled project to v7.0.0 (governance refresh + `framework_version`
  stamp), applied to both proving-pair projects. The procedure is the reusable lever for M34.
- **E33.2 — First real Agentic/Local epic on the pair + runtime decision.** Scope and run a
  genuine epic of the target project's own work under the fixed posture; capture the run record;
  record the Ollama-vs-llama.cpp+Qwen3.6 decision with the run's own reasons.
- **E33.3 — Trustworthy measurement out of the run (P9-GH-2).** Capture real burn/validation data
  from E33.2's run and fix/validate `measure-token-burn` only as far as trusting that run's
  numbers requires. Conditional in extent, sized by the run.

**Sequencing:** M33 first — it is the spine, and its bump procedure (E33.1) and evidence feed M34
and M35. The runtime decision (E33.2) unblocks the fleet's local substrate choice.

### M34: Fleet Roll-forward

**Goal:** The dormant enrolled projects (courtis, Getawayinsured2023, ai-project-system-mcp) are
rolling under v7.0.0 by end of phase, including the ai-project-system-mcp superseded-agent fix
(P6-GH-15).

**Indicative Epics:**
- **E34.1 — ai-project-system-mcp superseded-agent fix + v7.0.0.** Replace the superseded
  `hq.agent.md` with canonical `governance.agent.md`; bump to v7.0.0. Closes P6-GH-15 in the wild.
- **E34.2 — Dormant-project roadmap + roll-forward.** Sequence courtis, Getawayinsured2023 (and
  footboard as reached) onto v7.0.0 using E33.1's procedure; each rolling with a recorded path
  and demonstrable movement by phase close.

**Sequencing:** Behind M33 — consumes E33.1's bump procedure and E33.2's settled runtime choice.

### M35: System-Operator Canonization

*(Re-scoped in one pass, 2026-07-30, per HQ Ruling on SN-25 Decision 6 — folds in SN-24
(2026-07-28, form-only) and SN-25 (2026-07-30: handback, one-level escalation, Creation Chat
awareness, execution matrix, Milestone × local evidence mandate); see §P10.3 above.)*

**Goal:** Canonize the fleet operator role — runs the serialized lane, keeps projects current,
holds no authority to act on speech alone — with a form-neutral standing brief; record that a
blocked autonomous instance must hand back to its immediate parent and that escalation travels
exactly one level; ratify the execution matrix (mode is not authority); and produce real evidence
on the Milestone × local-inference question.

**Indicative Epics:**
- **E35.1 — Fleet-operator role + no-authority-on-speech seam.** Record normatively that the
  fleet operator (implementation form-neutral) operates the lane and keeps registered projects
  current, and that it holds no authority to act fleet-wide on speech alone (fleet-wide writes are
  proposals until authorized).
- **E35.2 — Operator's standing brief.** Complete the operator's standing brief as a form-neutral
  artifact (extends M32/E32.2's re-instantiation seed): what the operator needs each cycle to run
  the lane and keep the fleet current, within the authority boundary — consumable by a chat, a
  daemon, or a human, not a daily-spawn ritual tied to any one of those.
- **E35.3 — Handback + one-level escalation + Creation Chat awareness.** Record normatively that
  a blocked autonomous instance hands back to its immediate parent via escalation notice
  (authority-bearing intervention, terminates at a manual level by construction, SN-22); that
  escalation targets the immediate parent only, with the parent choosing resolve-or-escalate;
  that this does **not** close P9-GH-1; and that Creation Chat's awareness of all escalations is
  visibility-only, with "issue a steering note to HQ" as its sole legitimate outlet.
- **E35.4 — Execution matrix ratification + mode-is-not-authority.** Record the execution matrix
  normatively (likely in `governance/systems/chat-hierarchy.md`'s Execution Mode section),
  restoring the E31.1 baseline at Phase/Milestone; record explicitly that mode never confers
  Stage-2 accept or merge authority, which still requires the human's key regardless of running
  mode; record the SN-23 Ratified Decision #2 supersession (Execution Mode axis only).
- **E35.5 — Milestone × local-inference evidence-gathering.** Conduct the back-test evaluation
  against the concrete bar (M33's decomposition gap, E33.2 Run A's false positive, E33.4's false
  negative, M34's footboard miscount, P10-GH-6), measuring review quality; produce a recorded
  pass/fail judgment as evidence for a further HQ call on `model-routing-policy.md` row P4 — this
  epic does not itself decide row P4. *(The `Getawayinsured2023` "natural experiment" named in
  earlier drafts of this entry does not exist — corrected 2026-07-31, see §P10.3 above and the
  Changelog v1.3.1 entry; `Getawayinsured2023` runs Phase/Milestone remote, not local.)*

> Also carried forward (recorded, not an epic — nothing is built on it in P10): **P10-GH-7**,
> the two-sided exit-code untrust (E33.2 Run A / E33.4) plus the unexercised QA lane (G11), which
> makes any future handback mechanism's block-detection signal untrustworthy until addressed.

**Sequencing note:** M35 is independent of M33/M34 in dependency and schedulable by the Phase Chat
where it fits; the M33 → M34 ordering is binding. Within M35, E35.1–E35.4 are governance-record
epics with no hard ordering among them; E35.5 is evidence-gathering work and may run in parallel.

---

## Success Criteria

### P10 is Complete When:

1. ✅ **The proving pair runs under v7.0.0 for real** — both `home_finance` and
   `local-agent-runner` are stamped `framework_version: v7.0.0` and each has carried at least one
   real Agentic/Local epic end-to-end under the fixed posture (evidence in the run records)
2. ✅ **The local runtime question is settled by the run** — a recorded decision (keep Ollama vs
   switch to llama.cpp + Qwen3.6) with reasons the first real epic itself produced
3. ✅ **Run-first ordering delivered its evidence** — trustworthy burn/validation data exists from
   a real epic run, and `measure-token-burn` is honest against that real data (P9-GH-2 closed to
   the extent M33 needed)
4. ✅ **A repeatable enrolled-project v7.0.0 bump procedure exists** and has been applied to at
   least the proving pair
5. ✅ **The dormant enrolled projects are rolling under v7.0.0** — each on the roadmap with a
   recorded path and demonstrable movement; ai-project-system-mcp no longer carries the superseded
   `hq.agent.md` (P6-GH-15 resolved in the wild)
6. ✅ **The fleet-operator role is canonized** (form-neutral implementation) — the run-the-lane /
   keep-projects-current role is recorded, the no-authority-on-speech seam is normative, and the
   operator's standing brief exists
7. ✅ **A blocked autonomous instance can hand back, normatively** — the escalation-notice
   handback is recorded as authority-bearing, the one-level-only routing rule is recorded (with
   P9-GH-1 explicitly not closed by it), and Creation Chat's awareness of escalations is recorded
   as visibility-only with its steering-note outlet named
8. ✅ **The execution matrix is ratified and mode is not authority** — Phase/Milestone agentic
   mode is restored per the E31.1 baseline, and it is recorded explicitly that Stage-2 accept and
   merge authorization still require the human's key regardless of running mode
9. ✅ **The Milestone × local-inference question has real evidence** — a back-test evaluation
   against the phase's own known defects (measuring review quality, not throughput or cost) is
   conducted and its pass/fail judgment recorded, with `Getawayinsured2023`'s live configuration
   harvested as a natural experiment where applicable
10. ✅ **The parked items are recorded as explicit defers** — competing-model code review,
    P9-GH-1, P9-GH-3, ComfyUI, P8-GH-2, and P10-GH-7 (block-detection untrust) named with their
    triggers, not silently dropped

---

## Acceptance Criteria

The CFO (Layer 8) will accept P10 complete when:

- [ ] `framework_version: v7.0.0` is stamped and confirmable in both `home_finance` and
  `local-agent-runner`, and each has a committed run record for at least one real Agentic/Local
  epic executed under the fixed posture
- [ ] The runtime decision (Ollama vs llama.cpp + Qwen3.6) is recorded in the proving-pair run
  evidence with the run's own reasons — not an abstract memo
- [ ] Real burn/validation data from the proving-pair run exists in the repo, and a stated,
  evidence-backed judgment that `measure-token-burn`'s numbers for that run can be trusted
  (P9-GH-2)
- [ ] A documented, repeatable enrolled-project v7.0.0 bump procedure exists and shows evidence of
  having been applied to the pair
- [ ] ai-project-system-mcp carries the canonical `governance.agent.md` (superseded `hq.agent.md`
  gone) at v7.0.0; courtis and Getawayinsured2023 each have a recorded roll-forward path with
  demonstrable movement
- [ ] Governance records the fleet-operator role (form-neutral) and the no-authority-on-speech
  seam normatively, and the operator's standing brief is usable
- [ ] Governance records the handback rule (authority-bearing, terminates at a manual level by
  construction), the one-level escalation rule (with P9-GH-1 explicitly not closed by it), and
  Creation Chat awareness as visibility-only with its steering-note outlet named
- [ ] The execution matrix is ratified and recorded, with mode-is-not-authority stated explicitly
  (Stage-2 accept/merge require the human's key regardless of running mode)
- [ ] A Milestone × local-inference back-test evaluation is conducted against the phase's known
  defects, measuring review quality, with a recorded pass/fail judgment
- [ ] The full suite is green at delivery (363 baseline, no regressions, no skips introduced to
  route around changes) — for changes that touch this repo
- [ ] The phase closure declaration restates the parked/deferred items with their triggers
  (competing-model review, P9-GH-1, P9-GH-3, ComfyUI, P8-GH-2, P10-GH-7)

---

## Dependencies

### Internal
- P9's dual-mode switch + agentic paid-vs-local decision logic (M31) and manual-mode guardrail —
  the fixed posture is applied through these, not rebuilt — on master at v7.0.0
- P9's `measure-token-burn` instrumentation (M30/E30.1) — the object of M33/E33.3's trust work
- P9's SN-21 canonization + re-instantiation seed (M32/E32.1–E32.2) — M35 extends the seed into
  the operator's standing brief (form-neutral, SN-24)
- `bin/run-dev-agent` + orchestrator path (P7) — the Agentic/Local Epic execution substrate
- The canonical `governance.agent.md` and `ai-project-init` install path — the bump procedure's
  raw material
- `governance/systems/chat-hierarchy.md`'s "Execution Mode" section (P9-M31-E31.1) — the existing
  normative baseline the execution matrix (E35.4) restores at Phase/Milestone, and the surface
  E35.4 amends to record the matrix and mode-is-not-authority
- `.ai-project/artifacts/escalation-notices/` — the existing artifact type E35.3's handback rule
  reuses; the M34 escalations (`2026-07-28T20_00_00Z…`, `2026-07-29T00_00_00Z…`) are its worked
  examples
- `model-routing-policy.md` row P4 — the evidence-derived decision E35.5's evaluation must engage
  with (may amend independently of the row's own unfired trigger, per the SN-25 ruling)

### External / CFO-side
- **The target project repos** — `home_finance`, `local-agent-runner`, and the dormant four live
  outside this repo; P10's real work lands there. The CFO controls their state and access.
- **Local-inference substrate** — the open risk. Ollama today on `local-agent-runner`; the
  llama.cpp + Qwen3.6 27B Q8_0 reference stack benchmarks on Mac unified memory (~32 tok/s at
  ~42 GB on M5 Max 128 GB). The first real epic settles which one the fleet runs on.
- **GPU / hardware** — the serialized lane and any local-vs-ComfyUI contention (P9.2 context)
  remain CFO-side; the hand-run lane sidesteps a scheduler for now.
- **Premium/frontier quota** — Manual/Paid work from Creation through Milestone spends paid
  tokens; the CFO controls pacing. Agentic/Local at the Epic is the relief valve the whole posture
  is built to provide.

---

## Timeline

**Estimate:** 3 Milestones, ~13 Epics (revised 2026-07-30 from actuals + the M35 re-scope; original
estimate was ~7)
- M33 (Proving Pair — v7.0.0 + first real Agentic/Local epic): **closed**, 4 epics actual (E33.4
  added at closure to fix a decomposition gap)
- M34 (Fleet Roll-forward): **closed**, 3 epics actual (E34.3/E34.1/E34.2)
- M35 (System-Operator Canonization): ~5 epics indicative post-re-scope (E35.1–E35.5); mostly
  governance-record work, E35.5's evidence-gathering is the long pole
- **Total: ~2–3 weeks original estimate held through M33/M34; M35 added scope 2026-07-30 (SN-25)
  after the estimate was set**

The CFO's read (2026-07-20): "this might be the week everything clicks and the machine starts
going." The estimate is deliberately loose — run-first ordering means the first real epic's
duration is discovered, not assumed.

---

## Reference

### Governing Steering Notes
- **SN-23:** `.ai-project/artifacts/steering-notes/2026-07-20__creation-chat__steering-note__P10-adoption-spine.md`
  — P10 spine: fleet adoption of v7.0.0; fixed posture (Manual/Paid through Milestone, Agentic/Local
  at the Epic); proving pair first; dormant-project roadmap; run-first ordering; System-Chat-as-
  operator with the no-authority-on-speech seam and daily seed; local substrate as the open risk;
  parked items (binding; all decisions CFO-ratified)
- **SN-24:** `.ai-project/artifacts/steering-notes/2026-07-28__creation-chat__steering-note__M35-operator-form-change.md`
  — M35's operator form is superseded before it starts (Drivr/P11 daemon direction); HQ Ruling
  (`.ai-project/artifacts/rulings/2026-07-28__ai-project-system-hq__ruling__sn-24-m35-operator-form.md`)
  accepted it and amended one step further — M35 names the operator by **role**, not by any
  implementation (chat or daemon). Form-only; the role, the seam, and the standing brief are
  unchanged from SN-23
- **SN-25:** `.ai-project/artifacts/steering-notes/2026-07-30__creation-chat__steering-note__escalation-handback-and-execution-matrix.md`
  — autonomy must be able to hand back (an autonomous instance that becomes blocked has no way to
  summon a human); plus a CFO precision on the Execution Mode axis and a Milestone × local
  inference evidence-collection mandate. HQ Ruling
  (`.ai-project/artifacts/rulings/2026-07-30__ai-project-system-hq__ruling__sn-25-handback-and-execution-matrix.md`)
  accepted it: handback destination corrected to the immediate parent (not "a human"); one-level
  escalation recorded (does not close P9-GH-1); Creation Chat awareness is visibility-only; the
  execution matrix ratified with mode-is-not-authority attached; the Milestone × local evaluation
  directed with a concrete back-test bar; P10-GH-7 registered; M35 directed to re-scope once
  (this amendment) rather than patch twice

### Key Reference Documents
- `.ai-project/artifacts/hq-openers/2026-07-20__hq-chat-opener.md` — the opener instantiating this
  scoping session (filed verbatim for the artifact record)
- `.ai-project/artifacts/progress-digests/2026-07-20__hq__progress-digest.md` — reported P9
  closed clean at v7.0.0; parked HQ on the single open decision (set the P10 spine) that SN-23
  resolves; its Decision 2 (token measurement) resolved here by run-first ordering
- `docs/phases/P9__Context_Handling_and_Token_Efficiency/P9__phase-closure-declaration.md` —
  carry-forwards P9-GH-1/2/3 (verbatim definitions), P8-GH-2 restated deferred, ComfyUI non-blocking
- Local-model setup reference (share with the fleet operator): https://quesma.com/blog/qwen-36-is-awesome/
  — Qwen3.6 27B dense, Q8_0 + MTP, llama.cpp (recommends against Ollama), 64k context, ~32 tok/s
  at ~42 GB on MacBook M5 Max 128 GB. Author's bar: "a third as much code, but of higher quality"
  — the correct trade for a bounded, reviewed Epic agent
- `governance/systems/chat-hierarchy.md` + the SN-21 system-participant canonization (P9/M32) —
  the base M35 extends into the operator role

### Ratified Decisions (settled — NOT for re-debate; SN-23, all CFO-ratified)
1. **P10 is adoption, not capability.** Get v7.0.0 running for real across the CFO's projects. No
   new framework capability on spec; no third spin-off.
2. **The operating posture is fixed.** Manual/Paid from Creation through Milestone; Agentic/Local
   at the Epic. Holds for all projects; the other two matrix cells are off the critical path.
3. **Proving pair first.** home_finance + local-agent-runner run first (canonical agent already
   installed); the rest sequenced behind them. Blast-radius goal is all enrolled projects.
4. **Run-first ordering.** Measurement and validation come out of real epic runs, not before them.
5. **The runtime fork is settled by a run.** Ollama vs llama.cpp + Qwen3.6 is decided by the first
   real epic on the proving pair — adopt on the pair, not in the abstract.
6. **System Chat operates the fleet, with no authority on speech.** It runs the lane and keeps
   projects current; a fleet-wide write is a proposal until authorized. Daily seed required.
7. **Scheduler only when contention bites.** Hand-run the lane first; the CFO is the lane for now.
8. **Local-inference substrate is the open risk** — the last thing standing between here and go.

> **Note on Decision 6 (SN-24 / HQ Ruling, 2026-07-28):** the text above is preserved verbatim as
> SN-23's original record — not reopened. Its **form** is amended: "System Chat" names an
> implementation this repo's governance does not control; M35 (§P10.3) now records the operator
> by **role**, form-neutral, with the content (runs the lane, keeps projects current, no
> authority on speech, a standing brief) unchanged. See
> `.ai-project/artifacts/rulings/2026-07-28__ai-project-system-hq__ruling__sn-24-m35-operator-form.md`.

> **Note on Decision 2 (SN-25 / HQ Ruling, 2026-07-30):** the text above is preserved verbatim as
> SN-23's original record — not reopened. Decision 2's **Execution Mode axis is superseded**:
> Phase and Milestone may now run agentically or manually (the execution matrix, §P10.3), not
> Manual/Paid-only — restoring the P9-M31-E31.1 baseline that SN-23 had narrowed for P10's start.
> Decision 2's **locality axis stands**, with Milestone × local inference now under a directed
> evidence evaluation (§P10.3, E35.5) rather than settled either way. The supersession is recorded
> explicitly so it is a decision, not drift; **mode restoration does not confer authority** —
> Stage-2 accept and merge still require the human's key regardless of running mode. See
> `.ai-project/artifacts/rulings/2026-07-30__ai-project-system-hq__ruling__sn-25-handback-and-execution-matrix.md`.

### HQ Triage Decisions (this scoping session, 2026-07-20)
| Item | Decision | Where |
|------|----------|-------|
| Milestone shape | **3 milestones** — M33 Proving Pair, M34 Fleet Roll-forward, M35 System-Operator Canonization (CFO-ratified this session) | Milestones |
| P9-GH-2 (measure-token-burn can't verify its own reduction claims) | **Folded into M33** (E33.3) — trustworthy measurement is a proving-pair dependency; fix only as far as trusting the real run's numbers requires (CFO-ratified this session) | M33 (E33.3) |
| P6-GH-15 (superseded hq.agent.md live in ai-project-system-mcp) | **Into M34** — replace with canonical governance.agent.md at v7.0.0; closes it in the wild | M34 (E34.1) |
| P9-GH-1 (merge-auth hole at Milestone→Phase / Phase→HQ) | **Parked** — enters scope only on adoption friction; touches competing-model review's authority question | Out of Scope |
| P9-GH-3 (within-session context segmentation, unowned) | **Deferred** — not adoption spine; enters scope only if it blocks an adoption run | Out of Scope |
| Competing-model code review | **Parked** — substrate exists; open question is second-reviewer authority; enters on friction | Out of Scope |
| ComfyUI precision investigation | **Parked** — non-blocking CFO-side track, enters on friction | Out of Scope |
| P8-GH-2 (machine-local visual-artifact hosting, Low) | **Deferred** on its recorded trigger — not scoped | Out of Scope |
| ai-stack, character-factory (unenrolled) | **Noted, not addressed** — decide later if real projects or leftovers | Out of Scope |
| Sidekick-for-external-projects | **Not P10** — Brief-level identity question (pivot vs addition); noted so P10 inherits no unstated pivot | Out of Scope |

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.3.1 | 2026-07-31 | Premise correction (Phase Chat, resolving M35 escalation `.ai-project/artifacts/escalation-notices/2026-07-31T00_00_00Z__P10-M35__escalation_notice.md`, filed by the M35 Milestone Chat after E35.5 verified its harvest target before using it). §P10.3 and §Milestones→M35 (E35.5) both claimed `Getawayinsured2023` already ran Phase/Milestone on a local model, offering it as a corroborating "natural experiment" for the Milestone-locality question. **False**: it routes `phase`/`milestone` to `remote:qwen3.6:27b`; its override is on the model/tier axis (non-frontier open-weights vs. paid frontier), silent on locality. Corrected in place (struck text preserved, not deleted) rather than reopening the sections wholesale. Does not affect E35.5's own back-test evidence, which is independent of the harvest claim; does narrow the evidence base for any future row-P4 decision, which the Phase Closure Declaration must carry forward accurately. M35 milestone spec corrected in parallel (Milestone Chat's escalation deferred that edit to the Phase Chat). No other change; M33/M34 unaffected. |
| 1.3.0 | 2026-07-30 | M35 re-scoped in one pass (Phase Chat, per HQ Ruling on SN-25, Decision 6), folding in SN-24 (2026-07-28, form-only, already at v1.1.0) and SN-25 (2026-07-30) together rather than patching a second time. **SN-25 additions:** the handback rule (a blocked autonomous instance hands back to its immediate parent via escalation notice, authority-bearing, terminating at a manual level by construction per SN-22); the one-level escalation rule (parent-only targeting; does **not** close P9-GH-1); Creation Chat awareness as visibility-only (outlet: steering note to HQ); the execution matrix ratified, **superseding SN-23 Ratified Decision #2 on the Execution Mode axis only** (Phase/Milestone restored to agentic-or-manual per the E31.1 baseline; locality axis stands, Milestone under evaluation) with **mode-is-not-authority** stated explicitly (Stage-2 accept/merge still require the human's key); the Milestone × local-inference evidence mandate (back-test bar named, review-quality not throughput, `Getawayinsured2023` harvestable as a legitimate natural experiment, may amend row P4 independent of its unfired trigger); **P10-GH-7** registered (two-sided exit-code untrust + unexercised G11 QA lane — the block-detection risk under any future handback mechanism). Touches Executive Summary item 3, Vision, §P10.3 (comprehensive rewrite), Out of Scope, §Milestones→M35 (epics E35.1–E35.5, from E35.1–E35.2), Success Criteria (+3), Acceptance Criteria (+3), Dependencies, Timeline (epic estimate revised from actuals), Reference (SN-25 + ruling added; new Ratified-Decisions footnote on Decision 2, verbatim text not reopened). No change to M33/M34 (both closed) or to any decision this note does not name. |
| 1.2.0 | 2026-07-29 | Mid-flight amendment (Phase Chat, direct CFO instruction, resolving Milestone Chat escalation `.ai-project/artifacts/escalation-notices/2026-07-29T00_00_00Z__P10-M34__escalation_notice.md`): **`fieldledger-assesment` removed** from M34's dormant-project set and from the phase Acceptance Criteria — a screening project, not a real adoption target. Touches Executive Summary item 2, §P10.2, §Milestones→M34 (Goal + E34.2), and Acceptance Criteria. M34's own spec carries the matching amendment (Amendment A1). The escalation's other two items (an incoming `social-stories-creator` project; an inbound "personal platform") are **not** resolved by this entry — left open, not silently absorbed. No change to M33 (closed) or the fixed operating posture. |
| 1.1.0 | 2026-07-28 | Mid-flight amendment (Phase Chat, per SN-24 / HQ Ruling): M35 "System-Operator Canonization" amended form-only — the operator is named by **role**, not by implementation (neither "System Chat" nor "Drivr's daemon"); the daily re-instantiation-seed *ritual* retired in favor of a form-neutral **standing brief** with the same content. Touches Executive Summary item 3, Vision, §P10.3, §Milestones→M35 (E35.1/E35.2 retitled), Success Criteria 6, Acceptance Criteria, Dependencies, Reference (SN-24 added to Governing Steering Notes; Decision 6 footnoted, not rewritten). No change to M33 (closed), M34 (unaffected/independent), the fixed operating posture, or any SN-23 ratified decision's substance. Companion to the same-session paid-frontier model-mapping ruling (escalation-notice `2026-07-28T20_00_00Z__P10-M34__escalation_notice.md`), which this changelog does not otherwise touch (`.ai-project.yml`/policy files, not this spec). |
| 1.0.0 | 2026-07-20 | Initial P10 phase spec. Three milestones (M33 Proving Pair — v7.0.0 + first real Agentic/Local epic + runtime decision + P9-GH-2 folded in; M34 Fleet Roll-forward incl. P6-GH-15 fix; M35 System-Operator Canonization with no-authority-on-speech seam + daily seed), ~7 epics. Scoped by SN-23 (spine: fleet adoption of v7.0.0; fixed posture; proving pair first; run-first ordering; local substrate the open risk). Parked: competing-model review, P9-GH-1, P9-GH-3, ComfyUI, P8-GH-2. Milestone shape and P9-GH-2 disposition CFO-ratified this session. |
