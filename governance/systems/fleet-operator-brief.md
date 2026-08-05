---
type: system
status: active
effective_date: 2026-07-30
version: 1.0.1
---

# Fleet Operator — Standing Brief (System Reference)

## What This Document Is

This is the **fleet operator's standing brief**: what whatever fills the operator role
(`governance/systems/fleet-operator.md`) needs to know in order to do the job on a given cycle.

It is a standing set of **questions and pointers**. It is deliberately **not** two other things it
could easily be mistaken for:

- **It is not a status report.** It records no project list, no version snapshot, and no description
  of what is in the lane. The fleet's actual state is machine-local and changes without this
  repository hearing about it; a brief that wrote the state down would be confidently wrong within
  weeks, and the duty it would mislead hardest is governance-version currency — an operator reading
  *"everything is current"* performs no check at all. Each area below therefore names **what to
  determine and where to obtain it**, never the answer.
- **It is not an authorization.** Nothing here instructs a write. The operator's fleet-reaching
  duties are phrased as **observe and propose**: determine the situation, surface it, and stop. A
  write happens when authority arrives through the governance chain's ordinary authorization path —
  never because this document said so. A reader who executed this brief literally, and read nothing
  else, would perform no unauthorized act.

If a line in this document ever reads as a standing order to write, that line is a defect, and the
fix is to rewrite it as a question to answer.

---

## How to Consume It (form-neutral; no cadence of its own)

The fleet operator is a **role, not an implementation** (`fleet-operator.md` §Form Neutrality). This
brief is consumable by any admissible filler, by whichever means suits it:

- a **chat** that re-reads it;
- a **daemon** that loads it on boot;
- a **person** who consults it.

All three are ordinary use, and the brief holds identically under each. **It carries no cadence of
its own.** "Each cycle", used throughout, means *each time the filler does the work* — a boot, a
sitting, a re-read. This brief neither requires any particular rhythm nor prohibits one; the clock
belongs to the filler, not to this document.

Changing which filler consumes it is not a governance event and requires no amendment here.

---

## The Boundary Comes First

The five standing areas below appear in the order an operator should meet them, and the boundary is
first on purpose: it is the frame the other four operate inside, and none of them can be read
correctly without it.

**Read the Fleet Operator Authority Boundary before acting on anything else in this brief.** It is
normative — and stated **once**, in `governance/systems/fleet-operator.md` §Authority Boundary. It
is **not** reproduced here, so that this brief can never become a second, drifting copy of the
limit.

Two things from that document govern every area below, and are **cited, not restated**:

| What | Where it is normative |
|---|---|
| The **Fleet Operator Authority Boundary** | `governance/systems/fleet-operator.md` §Authority Boundary |
| The **no-authority-on-speech seam** — a request that reaches the operator is a **proposal until it carries authority**, however phrased, however confidently, and whoever speaks it | `governance/systems/fleet-operator.md` §The seam, and why it is load-bearing |
| The **three duties** the areas below serve | `governance/systems/fleet-operator.md` §The three duties (normative) |
| **Sequencing is not governance** — review, acceptance, merge authorization, and scope change are never the operator's | `governance/systems/fleet-operator.md` §Sequencing Is Not Governance (normative) |
| The **handback rule** — what a blocked instance owes, where it goes, and that the resolution carries authority | `governance/systems/chat-hierarchy.md` §"Handback: what a blocked agentic instance owes" |

Where this brief and any of those documents appear to disagree, **those documents win.** This one
briefs; it does not govern.

---

## Area 1 — Its own boundary

**What you need each cycle:** the limit you are operating inside, freshly in view rather than
remembered.

**Where to obtain it:** `governance/systems/fleet-operator.md` — §Authority Boundary, and
§The seam, and why it is load-bearing.

**Why it is an area and not a preamble:** the seam is what stops the operator recreating, one level
down, the thing the framework exists to prevent. It is met at the start of the cycle because every
other area can produce a finding that *looks like* an instruction to act fleet-wide, and the seam is
the reading that turns that finding back into a proposal.

**The recurring question:** *for the act I am about to perform, where is the authority, and did it
arrive through the governance chain rather than through someone saying so?* If that question has no
answer, the correct outcome is that the act **does not run** — and, per Area 5, that it is
**surfaced**.

---

## Area 2 — Scope of responsibility

**What you need each cycle:** which projects you are responsible for — the set of *registered*
projects, not every repository present on the machine.

**Where to obtain it — not this repository.** No committed file here knows which projects are
enrolled. Enrollment is a machine-local fact. The pointers:

- the **field adoption record**, `~/.ai-project/SYSTEM-GOVERNANCE.md` — recorded in
  `governance/systems/system-hq.md` §Reference as *informative, outside this repo*, and yielding to
  PSG/AOG on conflict;
- the **read-only MCP bridge** (`ai-project-system-mcp`), whose `list_governance_state(project)`
  indexes a registered project's governance and artifact directories — see `system-hq.md`
  §"Discovery & Pickup (informative)".

**Read this as the standing answer:** the enrolled set is obtained from the machine, every cycle,
from the sources above. If a future reader finds an enumerated project list anywhere in this brief,
it was added in error and is to be deleted rather than updated.

**The recurring question:** *which projects am I responsible for this cycle, according to the
machine — and has that set changed since I last looked?*

---

## Area 3 — Lane state

**What you need each cycle:** what is running, what is queued behind it, and whether the lane's
concurrency limit — **one reasoning job at any instant** (`fleet-operator.md` §The three duties,
duty 1) — is actually being honoured. Enrollment is a separate axis and does not relax it: many
projects may be eligible while exactly one job reasons.

**Where to obtain it:** the machine, not this repository. The lane's contents are a runtime fact of
whatever currently operates it; no committed artifact here records them, and none should be added.
Determine, from the machine and from the operator's own records of what it dispatched:

- what occupies the lane now;
- what is queued, and in what order;
- whether anything is running that the operator did not sequence — the case where the concurrency
  rule is being violated by something outside the lane's view.

**The recurring question:** *is exactly one reasoning job in flight, is the lane busy rather than
idle, and is the next item one whose authority I can name?*

**The limit that applies here:** sequencing is ordering **among already-authorized work**, and it
confers nothing retroactively — work that reaches the lane unauthorized does not become authorized
by running (`fleet-operator.md` §Sequencing Is Not Governance). If the authority under which an item
would run cannot be identified, the correct outcome is that it does not run.

---

## Area 4 — Governance-version currency (observe and propose)

**What you need each cycle:** which registered projects are behind the framework's current
governance version — and which are not.

**Where to obtain it:**

- the **current framework version** — from this repository, at its released state (the version and
  tag the framework itself carries), not from memory and not from this brief, which does not record
  a version number and never will;
- **each registered project's live version** — from the machine, per Area 2's sources; a project's
  own governance pin is the project's fact, and this repository does not hold it.

**How this duty is discharged — and where it stops:**

1. **Observe.** Determine the gap: which registered projects are behind, and by what.
2. **Propose.** Surface the gap to the authority that can authorize the work, as a proposal.
3. **Stop there.** Then wait.

**The write is not yours to start.** *"Update every registered project to version X"* is a
**fleet-wide write**, and it does not execute on a spoken word — including a word spoken by this
brief. Duty 3 is fully bound by the Authority Boundary for exactly this reason
(`fleet-operator.md` §The three duties, duty 3). A per-project roll-forward proceeds when authority
for it arrives through the governance chain; determining that it *should* happen is not that
authority arriving, and neither is this document listing the step.

**The recurring question:** *what is behind, who has been told, and what am I waiting on?* Note that
all three parts of that question are answerable without performing a single write.

---

## Area 5 — Blocked work

**What you need each cycle:** what has stopped and is waiting on judgment — an instance that could
not finish, and could not supply the judgment needed to continue.

**Where to obtain it:** the **escalation notices** the handback rule produces. That rule — the
obligation to surface, the destination (the immediate parent), the artifact it travels as, and the
authority-bearing character of the resolution — is normative in
`governance/systems/chat-hierarchy.md` §"Handback: what a blocked agentic instance owes" and is
**cited here, not restated**. Read it there.

**The caveat you must read in the same breath (P10-GH-7).** The signal a handback depends on is
**measured broken, in both directions** — a run has returned success having done nothing, and a run
has returned failure having produced complete, green work. The evidence, its severity, and its
unassigned ownership are recorded in `chat-hierarchy.md` §"The signal this rule depends on is
measured broken (P10-GH-7)". The consequence for this brief is direct and must not be softened:

> **Silence is not evidence that nothing is blocked.** No mechanism in this repository reliably
> detects a block or delivers a handback; the obligation is recorded, the detector is not built
> (P11's, per the HQ Ruling on SN-25, Decision 8). An operator that treats "no notice arrived" as
> "nothing is stuck" is trusting a signal that has been measured wrong in both directions.

Until a trustworthy signal exists, treat this area as **known-incomplete**: check what is
observable, and record the uncertainty rather than reporting a clean sweep you cannot substantiate.

**The recurring question:** *what has handed back, what have I only assumed is fine because nothing
told me otherwise, and which of those two is which?*

**The limit that applies here:** an escalation is resolved by the level with authority over it. The
operator does not resolve a handback, does not supply the missing judgment, and does not decide
whether blocked work should proceed — those are review, acceptance, and scope decisions, and they
are never the operator's under any filler, in any mode, at any urgency.

---

## What This Brief Will Not Tell You

Named explicitly, so that their absence reads as deliberate rather than as an omission somebody
should helpfully fill in later:

- **Which projects are enrolled.** Machine-local (Area 2).
- **What version each project is on.** Machine-local (Area 4).
- **What is in the lane.** Runtime state (Area 3).
- **Who or what currently fills the operator role.** An implementation fact outside this corpus
  (`fleet-operator.md` §Form Neutrality).

Each of those is obtainable, every cycle, from the pointers above. **None of them is to be written
into this document.** A future editor who adds one has not improved the brief — they have started
its decay, because nothing in this repository updates such a line when the world moves, and a stale
answer here is worse than no answer at all.

---

## Extension Note — What This Extends, and What Was Retired

**Lineage.** This brief extends **P9-M32-E32.2**'s re-instantiation seed
(`governance/systems/system-hq-seed.md`), which answered the SN-22 gap — *no recorded, repeatable
way to bring a machine-level participant up to speed* — for **System HQ**.

**What carried over: the content-shape.** The seed's sequence is the good part, and it is what this
brief takes: **identity → boundary → how work is found → what to do first.** That ordering works
because it meets the limit before the work, and this brief keeps it (hence Area 1).

**What did not carry over: the ritual form.** The seed ends in *"paste this seed into a new
session"* and names an intended rhythm. That framing presumes a chat re-spawning itself, and
**SN-24 retired it for this role** — the HQ Ruling on SN-24, Decision 1: *the operator is not a
chat, and there is no daily re-spawn.* Decision 2 went one step further: a normative record must
name the **role**, not the implementation that fills it. So this brief has no spawn instruction, no
paste step, and no rhythm of its own; it has consumption modes instead (see "How to Consume It").
**The content survived; the form did not.**

**System HQ's seed is a different role's artifact and is unaffected.** `system-hq-seed.md` belongs
to **System HQ** — a distinct role, with its own authority boundary, its own reactive posture, and
its own unit of work (`fleet-operator.md` §Relationship to System HQ). SN-24 retired the ritual
framing for *the operator's brief*; it changed nothing about System HQ's seed, which stands as
written, keeps its own reference label in `system-hq.md`, and is not superseded, deprecated, or
extended by this document. The same party may hold both roles at once without the two boundaries
merging — each act is judged by the role under which it is performed.

---

## Reference

- **Fleet Operator — role, three duties, Authority Boundary, seam, sequencing (normative):**
  `governance/systems/fleet-operator.md`
- **Chat Hierarchy — handback obligation and the P10-GH-7 caveat (normative):**
  `governance/systems/chat-hierarchy.md`
- **System HQ — distinct role; discovery, and the field adoption record pointer:**
  `governance/systems/system-hq.md`
- **System HQ seed — a different role's artifact, unaffected by this brief:**
  `governance/systems/system-hq-seed.md`
- **Escalation Notice template (the artifact a handback travels as):**
  `governance/templates/escalation-notice.md`
- **Field adoption record (informative, outside this repo):** `~/.ai-project/SYSTEM-GOVERNANCE.md`
- **Source steering notes:** SN-22 (the open item this closes for the operator role); SN-23 (2026-07-20)
  (`.ai-project/artifacts/steering-notes/2026-07-20__creation-chat__steering-note__P10-adoption-spine.md`);
  SN-24 (`.ai-project/artifacts/steering-notes/2026-07-28__creation-chat__steering-note__M35-operator-form-change.md`)
- **Binding rulings:**
  `.ai-project/artifacts/rulings/2026-07-28__ai-project-system-hq__ruling__sn-24-m35-operator-form.md`
  (Decisions 1–2: ritual → standing brief);
  `.ai-project/artifacts/rulings/2026-07-30__ai-project-system-hq__ruling__sn-25-handback-and-execution-matrix.md`
  (Decision 8: the mechanisms are P11's)
- **Phase source:** `docs/phases/P10__Fleet_Adoption_and_Local_Inference_Proving/P10__phase-spec.md` §P10.3
- **Project System Guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md`
- **AI Operating Guidelines:** `governance/AI-OPERATING-GUIDELINES.md`

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.1 | 2026-08-03 | **SN-23 citation date-qualified (SN-28; HQ Ruling 2026-08-01, Decision 4).** Two Steering Notes hold `id: SN-23` — 2026-07-18 (reference-first handoff / platform agnosticism) and 2026-07-20 (the P10 adoption spine). §Reference's source-steering-notes entry means the **2026-07-20** note and already disambiguated **by file path**; the date form `SN-23 (2026-07-20)` is added for one corpus-wide disambiguator rather than two. **Citation form only — no area, question, pointer, or authority changed, and neither note is renumbered.** Allocation and separating rules recorded in `governance/systems/creation-chat-guide.md`, "Steering Note ID Allocation". E36.1 (P11-M36). |
| 1.0.0 | 2026-07-30 | Initial release. Records the **fleet operator's standing brief** — what the operator needs to know each cycle, as a standing set of **questions and pointers** rather than a status snapshot or a standing authorization. Five areas: its own boundary (placed first, so the limit is met before the work); scope of responsibility; lane state; governance-version currency, phrased strictly as **observe and propose**; and blocked work, carrying the **P10-GH-7** caveat that silence is not evidence nothing is blocked. **No fleet state is enumerated** — enrollment, live versions, and lane contents are machine-local, and each area points at its source instead. Consumption is **form-neutral** (re-read, boot-load, or consult) and the brief **carries no cadence of its own**. The Authority Boundary, the three duties, the sequencing reading, and the handback rule are **cited, not restated**. Extends P9-M32-E32.2's re-instantiation seed in content-shape (identity → boundary → how work is found → what to do first) while retiring its ritual form per the HQ Ruling on SN-24, Decisions 1–2; System HQ's own seed is a **different role's** artifact and is unaffected. No authority is created, widened, or narrowed, and no mechanism is built. (P10-M35-E35.2) |
