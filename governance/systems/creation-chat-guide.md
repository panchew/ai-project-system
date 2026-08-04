# Creation Chat Guide — Ongoing Operation

**Status:** Active
**Applies to:** Creation Chat (Level 0 — see [`chat-hierarchy.md`](chat-hierarchy.md))
**Companion to:** [`start-a-project.md`](start-a-project.md) (the bootstrap half)

---

## Why this guide exists

[`start-a-project.md`](start-a-project.md) covers the **bootstrap half** of the
Creation Chat: producing the committed `genesis.md` that lets a Phase Chat open.
This guide covers the **ongoing half**: how the Creation Chat operates as a
permanent institution across many sessions — handing off state, staying informed,
recording manual work, and resetting without losing continuity.

The governing design constraint:

> Creation Chat is the single visible human interface. All governance (HQ, Phase,
> Milestone, Epic) runs as background agents communicating via artifacts. Complexity
> stays invisible to the user; only decisions and outcomes surface.

Everything below exists to make that continuity survive a chat reset using nothing
but committed artifacts.

---

## Re-instantiation Ritual

*(Amended P11-M36-E36.3, 2026-08-04, recording SN-26 Required actions 2, 3 and 4,
and canonizing SN-26 Carry-Over 1 per HQ Ruling 2026-08-01, Decision 9.
**This section is the single normative statement governing Creation Chat
re-instantiation.** [`../templates/seed.md`](../templates/seed.md) Rule 5 cites it
and does not restate it.)*

A Creation Chat session does not live forever. Context fills, sessions end, chats
get reset. The ritual preserves continuity across a reset using committed artifacts
and no session memory.

### Step 1 — Before reset: produce and commit a Steering Note

Before ending a session or resetting the chat, produce a Steering Note using
[`../templates/steering-note.md`](../templates/steering-note.md) and commit it to:

```
.ai-project/artifacts/steering-notes/<ISO-date>__creation-chat__steering-note.md
```

This is the durable record of where the project stands. If it is not committed,
the reset loses state. Committing is part of the ritual, not an afterthought.

### Step 2 — What to include in the pre-reset Steering Note

Structured state, not a narrative. Capture exactly:

- **Open concerns** — anything unresolved, each with id, severity, and the action
  it requires (front-matter `concerns` + the Concerns section).
- **Binding decisions** — decisions made this session that must not be re-debated
  (front-matter `decisions` + the Decisions Already Made section).
- **Carry-over items** — non-blocking items passed forward.
- **Next action** — exactly what the next session (or HQ) should do first.

If the next session would have to guess at any of these, the note is incomplete.

### Step 3 — How to re-open: paste the Seed, then pass the two current artifacts

Open the new session by **pasting [`../templates/seed.md`](../templates/seed.md)**,
with its `framework_version` front-matter field filled to the governance version the
project is on. Then pass these committed artifacts, and nothing else:

1. The **most recent Steering Note** from
   `.ai-project/artifacts/steering-notes/` (latest by ISO-date in the filename).
2. The **most recent Progress Digest**, if one exists, from
   `.ai-project/artifacts/progress-digests/` (latest by ISO-date).

**One addition is permitted, and only one.** A project that holds a committed
`genesis.md` may pass it as well, for original project identity. A project that has
none **does not render one for this purpose** — see "Why the Seed opens the session"
below. Otherwise: no chat transcript, no memory export, nothing else.

This is SN-26 Carry-Over 1's working practice, **canonized unchanged**.

### Step 4 — The model check runs on this path (P9-M31-E31.3)

Because Step 3 opens with the Seed, a re-instantiated session **runs the E31.3 model
check before it does anything else** — the Seed's own *Prerequisite Verification*
section is the first instruction it receives. Creation Chat is manual-only,
permanently (SN-22); the session compares its harness-reported model identity against
`.ai-project.yml`'s `models.creation`. **If both are present and disagree, the session
stops and waits for human resolution.**

The mapping, the self-report method's known limits, and the absent-block/absent-key
permissive default are defined **once**, in [`chat-hierarchy.md`](chat-hierarchy.md)
"Manual Chat Model Verification" — cited here, not restated.

**Why this is a step and not an assumption.** A ritual whose artifacts carry no
verification lets a session open against the wrong model and proceed. That is what
happened on 2026-07-28: a Creation Chat ran `claude-opus-5` against a then-configured
`remote:claude-opus-4-8` and opened anyway. The check existed in the templates and was
absent from the path actually taken (SN-26). **The path now carries it.**

### Step 5 — What the new session receives

A complete picture of project state with no session memory required:

- The **Seed** gives the Creation Chat's identity, its Rules of Engagement, and the
  model check above.
- The latest **Steering Note** gives open concerns, binding decisions, carry-overs,
  and the next action. **Start there** — a re-opened session takes direction from the
  Steering Note's Next Action, not from the Seed's inception prompt.
- The latest **Progress Digest** (if present) gives current phase/milestone status.
- A committed **`genesis.md`**, where a project has one, gives original project
  identity and Phase 1 boundaries — historical context, not current state.

The new session opens as if continuing uninterrupted. If it cannot, the gap is a
defect in the pre-reset Steering Note (Step 2) — fix the note, not the ritual.

### Why the Seed opens the session, and `genesis.md` may not exist

*(The SN-26 decision, recorded so the reasoning survives the rule.)*

`genesis.md` is a **bootstrap** artifact: it scopes project identity, Phase 1
boundaries and team composition, and it is consumed **once**, by the first Phase Chat
([`start-a-project.md`](start-a-project.md) Step 3). Re-instantiation is a
**continuity** problem. The two were conflated, and the cost grows with the project:
a repository well past Phase 1 that re-opens on `genesis.md` is handed **Phase 1 scope
as its picture of the present**. That is a defect for **every** project past its first
phase, not a quirk of any one of them.

The Seed takes artifact #1's place because it **exists for every project** by
construction, carries the Creation Chat's identity and rules, and — decisively —
**causes verification to happen when pasted** (SN-26, Decisions Already Made 2).

**`ai-project-system` renders no `genesis.md` and is not expected to.** It
bootstrapped itself and reached P11 without one; authoring one now would be a
backdated artifact whose Phase-1 content is inert. **No Project Brief is expected
either, for re-instantiation purposes** — [`../templates/seed.md`](../templates/seed.md)
Rule 4's Brief is the *inception* convergence target of the full path, and this
repository's equivalent content lives in committed governance, phase specs, and the
Steering Note / Progress Digest stream.

**Scope limiter, deliberate.** That decides re-instantiation only. Whether a Project
Brief would serve some **other** purpose here is a separate, parked, Brief-level
question (SN-26 Carry-Over 2), and SN-26 says in terms that the two "should not be
entangled." Nothing above rules on it.

---

## When to Write a Steering Note

Write one:

- **At the end of every session**, before a chat reset (the ritual above).
- **When a blocking concern arises mid-session** — do not wait for session end;
  commit a Steering Note so the concern reaches HQ immediately.
- **After 3+ Bouncer Work log entries of the same type** — a detected pattern is
  a concern worth formalizing (see the loop below).

---

## Steering Note ID Allocation

*(Added P11-M36-E36.1, 2026-08-03, recording SN-28 Required actions 1–3 and the
HQ Ruling 2026-08-01, Decisions 3 and 4.)*

### The allocation rule

**The next ID is the highest existing ID in the steering-note directory plus one,
regardless of which chat issues the note.** There is **one sequence per
steering-note directory** — HQ, Creation Chat, and any other issuer draw from the
same run of numbers (HQ Ruling 2026-08-01, Decision 3).

**Sub-IDs keep the existing letter-suffix form** (`SN-12a`, `SN-12b`). A sub-ID is
a **distinct ID, not a collision**, and it does not consume a new number.

**The reason, recorded alongside the rule.** Provenance is **already** recorded —
in the `issuer_chat` front-matter field and in the filename slug. The identifier
therefore **names position and nothing else.** It does not encode who issued the
note, and must not be made to. A rule whose reason is on the record survives an
edit that a bare rule does not.

The rule is mechanically checked by `tests/test_steering_note_id_uniqueness.py`
(bugfix B3.1). An author can rely on it being **enforced, not merely stated** —
but the guard catches a collision after the fact; it does not choose your ID for
you. Apply the rule when you file.

### When allocation has already failed: the separating rule

A collision that already exists is a **bookkeeping defect**. Remediating it is
governed by one rule:

> **A bookkeeping defect never rewrites a citation in a normative document.**

That resolves into two cases:

- **Cited only in project-internal, non-normative artifacts** (steering notes,
  rulings, digests, closure declarations, reference packets) → **renumber.**
  Nothing load-bearing points at the ID, and the record is cheaper to correct
  than to annotate.
- **Cited in the normative tier** (`governance/`) → **date-qualify the
  citations** — `SN-23 (2026-07-18)` — and **leave the collision visible rather
  than laundered.** The normative tier's citations are load-bearing: a renumber
  silently invalidates every document that points at the old ID, including
  documents outside this repository.

**No chat renumbers on its own initiative.** Renumbering is a ruled act, not a
tidy-up an author performs while passing through.

### The worked case: `SN-1` is renumbered, `SN-23` is not

This asymmetry is a **principle applied**, not an inconsistency:

- **`SN-1`** is cited only in project-internal artifacts, so the separating rule
  sends it to *renumber*.
- **`SN-23`** is cited across the normative tier, so the separating rule sends it
  to *date-qualify*.

**Both 2026-07-18 and 2026-07-20 keep `id: SN-23` permanently, by decision** (HQ
Ruling 2026-08-01, Decision 4). This is a **ratified, deliberate outcome — not
unfinished cleanup.** Do not "fix" it: renumbering either note would invalidate
every citation that was corrected to disambiguate them.

The two meanings, for anyone following a citation:

| Citation | Note | Subject |
|---|---|---|
| `SN-23 (2026-07-18)` | `…__reference-dont-display.md` | reference-first artifact handoff / platform agnosticism |
| `SN-23 (2026-07-20)` | `…__P10-adoption-spine.md` | the P10 adoption spine |

Against B3.1's guard, the surviving `SN-23` collision is a **ratified, allowlisted
exception**, not an outstanding defect.

---

## When to Expect a Progress Digest

The Creation Chat receives a Progress Digest (HQ → Creation Chat) using
[`../templates/progress-digest.md`](../templates/progress-digest.md):

- **At the start of each new phase or milestone** — HQ sends one unprompted.
- **On request** — the Creation Chat can ask HQ Chat for a fresh digest at any time.

The Progress Digest is the primary self-contained summary of project state. The
user should never need to open a phase or milestone artifact to understand where
the project stands — if they do, the digest has failed its purpose.

---

## Escalation Awareness — Visibility Only

*(Added P10-M35-E35.3, 2026-07-30, recording the HQ Ruling on SN-25, Decision 3.)*

The Creation Chat is **aware of every escalation notice, wherever in the fleet it
arises** — including a handback from an instance running unattended
([`chat-hierarchy.md`](chat-hierarchy.md), "Handback: what a blocked agentic
instance owes").

**What that awareness is.** A **retrieval** property over committed artifacts.
Escalation notices are committed to the repository
(`.ai-project/artifacts/escalation-notices/`), and a re-instantiated Creation Chat
reads that directory like any other artifact it consumes. That is the whole
mechanism.

**What it is not.** It is **not a subscription** — nothing is pushed, nothing
notifies, no channel is opened, and none is to be built for it. It is **not a
seat** — awareness of an escalation gives the Creation Chat no place in the chain
that resolves it. Escalations travel one level at a time to the **immediate
parent**, and the Creation Chat is never that parent for a blocked instance below
it.

**Seed Rule 3 stands — restated here exactly as written, not amended**
([`../templates/seed.md`](../templates/seed.md), "Rule 3 — No Authority"):

> This chat holds no governance authority. Nothing said here is binding.
>
> Decisions formed here are proposals until the human carries them into the HQ Chat
> via an artifact. The human is the only one who can promote a thought into a
> decision.

Seeing an escalation changes nothing about that rule. The Creation Chat may not
resolve a block, unblock an instance, direct a level, or decide anything — in this
matter or any other.

**The one legitimate outlet: a Steering Note to HQ.** What the Creation Chat may do
with what it sees is **issue a Steering Note**
([`../templates/steering-note.md`](../templates/steering-note.md)) —
direction-setting, not resolution. That is the same channel described in "When to
Write a Steering Note" above, and it is how SN-23 (2026-07-20), SN-24 and SN-25
themselves arrived. Naming the outlet explicitly is what keeps awareness from drifting into
*"the Creation Chat unblocked it"* — a right with no outlet decays into an
improvised one.

**Awareness must never become a resolution path.** A Creation Chat session that
finds itself answering a blocked instance, rather than writing a note to HQ, has
produced the failure this section exists to prevent — not an efficient shortcut
around it.

---

## CFO PR Review Gate

Layer 8 (the CFO / human operator) must be able to see PR changes before a merge
happens. This is a **configurable gate** — ON by default, disableable per project
when the CFO trusts the process to merge automatically. The gate is additive: it
does not replace or rename the existing merge-authorization artifacts, it adds a
human review step ahead of them.

### Configuration

The toggle is a project-level setting in `.ai-project.yml`:

```yaml
cfo_review_gate: enabled   # or: disabled
```

- **`enabled`** (default) — every merge-ready PR must be surfaced for CFO diff
  review before it merges.
- **`disabled`** — merges proceed automatically (agentic auto-merge); behavior is
  unchanged from a system with no gate.

A project that omits the key is treated as `enabled` (gate ON by default).

### Behavior when the gate is ON

```
PR becomes merge-ready
  → surfaced in the Progress Digest "Open Decisions" section
    (PR number, source → target branch, one-line change summary)
      → CFO reviews the diff
        → CFO approves
          → merge proceeds (existing merge-authorization flow)
```

The Progress Digest is the single visible surface, so the merge-ready PR appears
there — showing **what will merge**, not merely that something is ready. This keeps
the gate consistent with the single-visible-interface constraint: the CFO never has
to leave the Creation Chat surface to know a merge is pending.

### Behavior when the gate is OFF

The current automated merge behavior is unchanged. Merge-ready PRs do **not** appear
in the Progress Digest's Open Decisions section, and merges complete without a human
review step.

---

## Bouncer Work Log → Steering Note Loop

Bouncer work is Layer-8 manual intervention triggered by operating a live system:
data fixes, direct user requests, one-off console operations — the gap between what
the system does and what reality demands. It is distinct from the Bugfix Workflow,
which targets code defects and produces commits.

Each intervention gets a lightweight Bouncer Work log entry
([`../templates/bouncer-work-log.md`](../templates/bouncer-work-log.md)) — under two
minutes to fill. The flow:

```
real-life operation
  → bouncer work happens (manual intervention, no commit)
    → logged in Bouncer Work log (lightweight record)
      → pattern detected (3+ of the same type?)
        → Steering Note to HQ
          → formal Epic (automate the fix, close the gap)
```

**What counts as a pattern:** the **same severity** and the **same type** of
intervention occurring **3 or more times**. When the third matching entry lands,
set the Pattern flag on that Bouncer Work log entry and write a Steering Note to HQ
proposing formalization. The Steering Note is how a repeated manual workaround
becomes a funded Epic that removes the manual work.

---

## Related Documentation

- [`start-a-project.md`](start-a-project.md) — bootstrap half (producing genesis.md)
- [`chat-hierarchy.md`](chat-hierarchy.md) — Creation Chat as Level 0
- [`../templates/steering-note.md`](../templates/steering-note.md)
- [`../templates/progress-digest.md`](../templates/progress-digest.md)
- [`../templates/bouncer-work-log.md`](../templates/bouncer-work-log.md)
