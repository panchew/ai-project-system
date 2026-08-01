---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-07-31T23:55:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-27
    severity: high
    title: P11 spine — Drivr as coordination over rented execution; fleet registry with three states; competing-model review that surfaces findings only
decisions:
  - "P11 is Drivr. The recorded direction of SN-24 becomes the phase spine. HQ may now produce the Phase Execution Chat Starter."
  - "An app is made AI-powered by calling a CLI tool that owns the inference. This is a different skill from using AI tools to write software, and it is the architectural basis of Drivr: Drivr does not implement inference, it invokes tools that do."
  - "Drivr must be able to use ANY CLI tool that empowers the work. The execution layer is a pluggable adapter surface, not a fixed choice of engine. local-agent-runner and OpenCode are today's roster, not the architecture."
  - "SUPERSEDED BY AMENDMENT 1 — see below. Original text: Today's roster, as a starting point and not a constraint: Epics that run locally may choose their tool (local-agent-runner); OpenCode covers the rest, which is what unlocks any model from any provider with API keys and other auth methods."
  - "AMENDMENT 1 — OpenCode covers the local lane too. OpenCode + Ollama + qwen3-coder:30b works as if it were local-agent-runner; verified by the CFO in field practice on the desktop version. The two-lane split is retired; one tool currently covers both local and cloud."
  - "AMENDMENT 1 — local-agent-runner is retained only if it still provides something. If it does, keep it; otherwise the focus is pluggability — any CLI tool leveraging local or cloud, open-source or paid models."
  - "AMENDMENT 1 — The local inference RUNTIME question is CLOSED. llama.cpp is no longer something the CFO wants to spend attention or time on; nothing else will be tried for local inference. Ollama is settled, not provisionally chosen."
  - "AMENDMENT 1 — The local inference MODEL roster stays open. Two questions remain live: (a) whether qwen3-coder:30b can handle the context of a MILESTONE, and (b) whether any other open-source model runs with similar or better results. Keep an eye on newer models."
  - "The fleet has three states. ACTIVE = enrolled in the registry; receives time and attention. BENCHED = not currently receiving attention; may return. ARCHIVED = not planned to ever be touched again, though it can be brought back to life."
  - "The orchestrator schedules agentic runs to avoid overloading the system."
  - "Competing models review PRs — including GitHub Copilot as a PR reviewer — looking closely for performance, security, and scalability. They SURFACE FINDINGS ONLY. They hold no authority and resolve nothing."
  - "The leverage case for P11 is stated as a choice, and the choice is this: the return is learning and adopting a way of working that keeps the CFO competitive in the industry. It is not revenue and not a platform."
references:
  - "SN-24 (2026-07-28) — Drivr direction, headless-first, four-project ecosystem, gates in-app, the human inside the governance graph. This note makes that direction a spine; it does not amend it."
  - "SN-23 (2026-07-20) — Ratified Decision #7 (scheduler only when contention bites) is load-bearing for the scheduling item below."
  - "2026-07-31 Progress Digest — Open Decisions #1-#6, which this note triages."
  - "SN-26 (this session) — Creation Chat re-instantiation ritual; explicitly NOT part of this spine."
---

# Steering Note — Creation Chat to HQ Chat

## Purpose

This note sets **P11's spine**. The 2026-07-31 Progress Digest closed P10 and stated that the
one thing waiting is P11, which is waiting on the Creation Chat, because HQ does not infer a
spine to write a Phase Execution Chat Starter from. This is that spine, together with a triage
of the digest's Open Decisions #1–#6.

The decisions in the front matter are the CFO's, taken in the 2026-07-31 Creation Chat session.
Items this chat proposes rather than received are tagged **[PROPOSED — confirm]** inline and are
not binding until the CFO confirms them.

---

## Concerns for HQ Triage

### SN-27 — P11 spine: coordination over rented execution [HIGH]

**Detail.**

#### The realization that organizes the phase

The CFO's words: *"I think I finally understand how to make an app be AI powered: by calling a
CLI tool that enables the inference. This is different to knowing how to use AI tools to
implement software."*

SN-24 already ruled that Drivr **rents its chat half** from existing harnesses (Claude Code /
OpenCode / Copilot) rather than building an agent client. This session extends the same
principle one layer down: **Drivr rents its execution half too.** It does not implement
inference, does not own a model loop, and does not grow its own engine. It invokes CLI tools
that already do that, and spends its whole budget on the layer nobody sells — coordination over
this project's own governance state.

This is what makes the phase buildable at the lightness criterion SN-24 set (*"as agentic as we
can, so the infrastructure is as light as possible"*).

#### Execution is a pluggable adapter surface

**Drivr must be able to use any CLI tool that empowers the work.** The roster below is the
starting point, explicitly not the architecture:

| Lane | Tool | What it unlocks |
|---|---|---|
| Epics run locally | `local-agent-runner` (the Epic may choose the tool) | Local inference on owned hardware; the proven lane from P9/P10 |
| Everything else | OpenCode | Any model from any provider, with API keys and other auth methods |

The prior open question — whether OpenCode should eventually absorb the local lane as well — is
**answered one level up and therefore dissolved.** The commitment is to the adapter surface, not
to either tool. A future roster change is a configuration decision, not a re-architecture.

**Context for how this arrived, recorded so the record is honest:** the CFO raised a concern this
session that `local-agent-runner` might be reinventing the wheel, having realized that OpenCode
covers the same ground — one-shot non-interactive `opencode run` against a local Ollama model,
plus a broader built-in toolset and a headless server mode that `local-agent-runner` does not
have. The concern was well founded on the facts. The resolution is not that either tool was a
mistake, but that **the choice of engine was the wrong thing to have been fixed at all.** P9/P10's
local-inference evidence — the runtime decision, the 14b-vs-30b model-tier finding, the blinded
review back-test — is evidence about *local agentic execution* and survives any change of engine.

#### The fleet registry and its three states

| State | Definition (CFO's) |
|---|---|
| **Active** | Enrolled in the registry. Receives time and attention. |
| **Benched** | Not currently receiving attention. May return. |
| **Archived** | Not planned to ever be touched again — though it can be brought back to life. |

**The orchestrator schedules agentic runs to avoid overloading the system.** This is the concrete
form of SN-23 Ratified Decision #7 (*scheduler only when contention bites*): P10 ran the local
lane by hand and the contention is real and measured — one GPU, 16 GB VRAM shared with ComfyUI,
one heavy consumer at a time, `qwen3-coder:30b` already partially offloading to RAM.

**[PROPOSED — confirm]** State transitions are the CFO's to make; Drivr may *propose* a move
(e.g. surfacing a project with no epic activity for some period) but never executes one on its
own. This follows the standing SN-24 principle — *automation runs the machine; authority stays
held* — but the CFO has not stated it for this specific case, so it is proposed, not recorded.

#### Competing-model PR review — findings only

The CFO wants **competing models looking closely for performance, security, and scalability**,
with **GitHub Copilot added as a PR reviewer**. Their output is **surfacing findings only.**

This matters to place precisely against governance already in force. **PSG §11.6.1** makes the
CFO the mandatory **diff** reviewer on every PR — authorization is not review, and default-accept
is only safe because a parent actually looks. Competing-model review therefore **feeds that
review; it does not substitute for it, dilute it, or create a consensus path that resolves
anything.** No finding from any model carries authority, and no volume of agreement between
models converts into one. This is *mode is not authority* applied to a new participant class.

Recorded consequence: this **un-parks** the competing-model code review item, which P10 parked
unowned. It now has a shape and an explicit authority ceiling.

#### The leverage case, stated as a choice

The 2026-07-31 digest asked that P11's framing state the leverage case as a **choice**, not let
it read as though the infrastructure were the goal — carrying the CFO's own SN-24 caution that
all four projects are infrastructure, none is a platform, and none earns revenue.

The CFO's answer, this session: the return is **learning and adopting a way of working that keeps
them competitive in the industry.** Not revenue. Not a platform.

That is a coherent and sufficient justification, and it is recorded as the deliberate choice it
is. It also sets a real bar for the phase: **P11 is justified to the degree the way of working it
produces is genuinely transferable to how the CFO works professionally** — not to the degree the
machine is impressive.

#### The one thing that does NOT get solved by renting

**P10-GH-7 (High) is inherited, not retired, and this is the single most important technical
constraint on the phase.**

P10 measured the completion signal untrustworthy in **both** directions on its own stack —
E33.2 Run A returned **exit 0 having done zero work**; E33.4 returned **exit 2 having produced
complete, green work** — with **G11** standing at zero captured `epic_qa` runs.

Renting the engine does not escape this. OpenCode carries an **open issue of exactly the same
shape**: `opencode run` exits `0` even when the session errored, because the run command does not
await the event loop that tracks error state (`anomalyco/opencode` issue #14551). Adopting it
**relocates** the untrustworthy-completion-signal problem into a dependency the CFO does not
control and cannot patch as freely as an owned engine.

A scheduler that dispatches unattended runs, and a gate queue derived from what governance says
is outstanding, both **depend on knowing whether a run finished, stalled, or failed confidently
wrong.** Building either over the current signal yields constant false escalations or silent
no-ops that read as success — which is what P10-GH-7 already says in the abstract, now with a
second engine's independent confirmation.

**Required action:** HQ should treat P10-GH-7 as **in scope for P11 and sequenced before**
anything that dispatches or schedules unattended runs, rather than as a carry-forward to triage.
The handback rule M35 recorded has no detector beneath it in either engine.

---

## Decisions Already Made

Binding, from the 2026-07-31 Creation Chat session. Not for HQ to re-debate.

1. **P11 is Drivr.** SN-24's direction becomes the phase spine; HQ may produce the Phase
   Execution Chat Starter.
2. **An app is made AI-powered by calling a CLI tool that owns the inference** — a distinct skill
   from using AI tools to write software, and the architectural basis of Drivr.
3. **Drivr must be able to use any CLI tool that empowers the work.** Execution is a pluggable
   adapter surface; no engine is fixed by the architecture.
4. **Today's roster:** locally-run Epics may choose their tool (`local-agent-runner`); OpenCode
   covers the rest, unlocking any model from any provider with API keys and other auth methods.
5. **Three fleet states:** active (enrolled in the registry; receives time and attention), benched
   (not currently receiving attention; may return), archived (not planned to be touched again;
   revivable).
6. **The orchestrator schedules agentic runs to avoid overloading the system.**
7. **Competing models review PRs, including GitHub Copilot, for performance, security, and
   scalability — surfacing findings only, with no authority.**
8. **The leverage case is a choice:** the return is a way of working that keeps the CFO
   competitive in the industry — not revenue, not a platform.

---

## Carry-Over Open Items

Triage of the 2026-07-31 Progress Digest's remaining Open Decisions, plus items this session
raised.

1. **Digest #2 — block detection.** Resolved by this note: **in scope, sequenced first**, with
   OpenCode's issue #14551 as new corroborating evidence. See the Required action above.
2. **Digest #3 — SN-1 System HQ codification.** Unchanged: accepted, self-contained, no
   dependencies, needs a milestone with room. **[PROPOSED — confirm]** place it alongside SN-26
   (below) in a documentation milestone rather than interleaved with Drivr build work.
3. **Digest #4 — P9-GH-1 / P10-GH-9.** The trigger is *before the first Phase or Milestone agentic
   dispatch is wired*. Nothing in this spine fires it yet, but Drivr's scheduler is the most
   plausible thing that would. **[PROPOSED — confirm]** HQ assigns an owner at the milestone that
   first touches dispatch, rather than at phase open.
4. **Digest #5 — `ai-stack` and `character-factory` unenrolled.** **[PROPOSED — confirm]** these
   resolve themselves as a side effect of the registry: building a three-state registry forces
   every project on the machine to be classified active, benched, or archived. No separate
   decision needed — the classification pass is registry work.
5. **Digest #6 — sidekick-for-external-projects.** Unchanged: a Brief-level identity question,
   not phase scope. Untouched by this note.
6. **SN-26 — Creation Chat re-instantiation ritual.** Medium tightening. Explicitly **not** part
   of this spine, per the binding decision recorded in that note.
7. **[PROPOSED — confirm] A measured comparison of the two engines**, in this project's house
   style (measure it, don't argue it — the row-P4 discipline): run OpenCode's `run` against
   `local-agent-runner`'s own `proof/` fixture task, same model, same host, and compare transcript
   quality and exit-code honesty. Under Decision 3 this is no longer a choose-one exercise — it is
   how the adapter surface learns what each tool's signal is actually worth, which is directly
   what P10-GH-7 needs. Not blocking the spine.
8. **Ollama context-window trap**, noted for whoever builds the OpenCode adapter: Ollama defaults
   every model to a 4,096-token context window regardless of what the model supports, and OpenCode
   needs roughly 16k+ to drive its tool-use loop. A silent truncation here would look like model
   incompetence.

---

## Amendment 1 — 2026-08-01, Creation Chat

Recorded after the note was filed and before HQ consumed it. The CFO's words, same session.
The spine is unchanged; the execution roster and the local-inference questions are.

### A1.1 — OpenCode covers the local lane too; the two-lane split is retired

**OpenCode + Ollama + `qwen3-coder:30b` works as if it were `local-agent-runner`** — verified by
the CFO in field practice, on the desktop version.

This supersedes the roster table above. There is no local-vs-cloud tool split: **one tool
currently covers both.** Binding decision 3 — *any CLI tool that empowers the work*, execution as
a pluggable adapter surface — is **unaffected and is the reason this costs nothing.** The roster
changed; the architecture did not. That is the adapter surface working as designed, on its first
real test, two hours after being decided.

### A1.2 — `local-agent-runner` is retained only if it still provides something

The CFO: *"If `local-agent-runner` provides anything to the project, let's keep it. Otherwise,
let's focus on pluggability."*

This is a **directed assessment with a real possibility of retirement**, not a foregone
conclusion in either direction. It is not a judgment on the work: P9/P10's local-inference
evidence — the runtime decision, the 14b-vs-30b model-tier finding, the blinded review back-test —
was evidence about *local agentic execution* and stands whatever happens to the engine that
produced it.

**[PROPOSED — confirm]** the assessment bar is *"names a capability P11 actually needs that
OpenCode does not provide."* The two candidates worth checking before retiring it, so the
assessment is evidence rather than vibe: its **library entry point** (`run(task, tools, model)`
with custom in-process tool handlers) and its **JSON-schema argument coercion** for models that
mistype tool arguments. OpenCode's `serve` mode may well cover the first. If neither survives
contact with a real P11 need, retirement is the honest outcome.

### A1.3 — The local-inference RUNTIME question is closed

The CFO is **no longer interested in trying anything else for local inference**, and **llama.cpp
is no longer something to spend attention or time on.**

This **closes a parked item rather than deferring it.** P10 carried the llama.cpp + Qwen3.6 Q8_0
trial as parked-on-trigger, pending Mac-class ~42 GB hardware. That trigger is now void: the item
is closed by decision, not waiting on hardware. **HQ should record it as closed** so no future
phase re-inherits it as an open parked item.

**Ollama is settled, not provisionally chosen.** M33 decided to keep it by running it; this makes
that permanent.

### A1.4 — The local-inference MODEL roster stays open

Distinct from A1.3, and the distinction is the point: **the runtime is settled; the models are
not.** Two live questions, in the CFO's framing:

1. **Can `qwen3-coder:30b` handle the context of a MILESTONE?** This is the sharpest open technical
   question in the phase. It sits directly against **row P4**, which HQ ruled unchanged on
   2026-07-31 — Milestone stays paid frontier — with three named gates behind it: measured
   prescription variance (**G-P4-a**), unassisted search and absence-detection over a real branch
   (**G-P4-b**), and tool-using verification before ruling (**G-P4-c**). The CFO is now naming a
   fourth axis, **context capacity at milestone scale**, which E35.5's blinded-packet method did
   not test. Row P4's ruling is not reopened by this note; it is where the answer would land.
2. **Does any other open-source model run with similar or better results?** Standing watch item —
   *keep an eye on newer models.* **[PROPOSED — confirm]** this is a recurring cheap re-test
   against E35.5's existing back-test harness when a candidate appears, not a scheduled
   investigation. The harness already exists and the ground truth is already committed, which is
   what makes watching affordable.

### A1.5 — What this sharpens about P10-GH-7

If OpenCode becomes the sole engine, the untrustworthy completion signal is **no longer split
across two codebases** — it concentrates entirely in OpenCode's open issue #14551 (`run` exits `0`
on session errors). That is *better* for diagnosis and *worse* for control: one well-understood
failure mode, in a dependency the CFO does not own. The Required action above is unchanged and, if
anything, more urgent.

---

## Next Action

HQ Chat should:

1. **Open P11 with Drivr as its spine**, per the eight binding decisions above.
2. **Produce the Phase Execution Chat Starter**, carrying SN-24's obligations forward as that note
   requires — the four-project ecosystem, the headless-first inversion (*a dashboard is a surface
   for watching; the more agentic the machine, the less there is to watch*), and the
   infrastructure-is-not-a-platform caution, now answered by binding decision 8.
3. **Sequence P10-GH-7 before any scheduling or dispatch work.** The spine's scheduler and gate
   queue both rest on a completion signal measured broken in two engines.
4. **Return the seven `[PROPOSED — confirm]` items to the CFO** rather than acting on them — items
   2, 3, 4, 7 in Carry-Over, the state-transition rule and Drivr's propose-only role under the
   registry, and the engine-comparison spike.
5. **Take no action on SN-26** beyond recording it, per that note's own instruction.
6. **Record the llama.cpp trial as CLOSED, not parked** (Amendment A1.3). Its hardware trigger is
   void; leaving it parked would let a future phase re-inherit a decision the CFO has already made.
7. **Carry the milestone-context question into P11 scope** (Amendment A1.4) as a fourth axis
   alongside row P4's G-P4-a/b/c gates. Row P4's ruling is not reopened by this note.
