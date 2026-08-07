---
type: system
status: active
version: 1.1.0
---

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

**This section governs how IDs are *allocated*. For how they are *cited* — the
`GH-` phase prefix, and artifacts keyed by level rather than by identifier — see
[Artifact ID Citation Forms](#artifact-id-citation-forms) below.**

---

## Artifact ID Citation Forms

*(Added P11-M37-E37.2, 2026-08-06, recording HQ Ruling 2026-08-05, Decisions
1–4.)*

**Companion to [Steering Note ID Allocation](#steering-note-id-allocation)
above.** That section governs how an ID is **allocated**; this one governs how an
ID is **cited**. They are the same concern — *an identifier must resolve to
exactly one artifact* — reached by two different routes, and a reader who needs
one usually needs the other.

### The `GH-` prefix names the phase that FILED the item — permanently

**A gap record's phase prefix names the phase in which it was filed. It never
names the phase expected to address it, and it never changes** — not when the
item is parked, rescheduled to a later phase, re-rated, closed by a different
phase, or closed in the wild by another project.

> **The record names the disposition; the identifier names the origin.**

**The reason, recorded alongside the rule.** An identifier names something
**immutable**; a disposition is not immutable. A prefix that tracked disposition
would have to be rewritten every time the item moved — and each rewrite silently
invalidates every citation pointing at the old ID, including citations in
documents outside this repository. Disposition is already recorded, in the
closure declarations and rulings that move the item. The identifier does not need
to carry it, and must not be made to.

**Allocation restarts per phase.** The prefix carries uniqueness, so a per-phase
counter beginning at 1 is sufficient — `P10-GH-1`, `P11-GH-1`.

**The worked proof: `P10-GH-8`.** Filed in P10; destined for M36, then parked,
then scheduled to M37. **Its ID never moved.** Under a disposition-naming prefix
it would have had to change twice, invalidating every citation each time.

So, for an author filing today: **take the current phase's prefix and the next
free number in that phase's sequence, and expect never to change it.**

### Ratified historical exceptions — recorded, not renumbered

Two ranges predate this rule and do not follow it. **Both are ratified as
permanent exceptions.**

| Range | What it does instead | Status |
|---|---|---|
| `P6-GH-10` … `P6-GH-15` | **Forward-allocated** by P5's closure declaration — the prefix names the phase expected to *address* the item, not the phase that filed it. | ratified exception |
| `P7-GH-16` … `P7-GH-21` | Continues a **global** counter across phases instead of restarting per phase. | ratified exception |

**They are not renumbered, and that is a decision — not unfinished cleanup.**
They have already propagated into the normative tier, so renumbering them would
do exactly the damage the rule above exists to prevent. **Do not "fix" them.**

This is the separating rule from [Steering Note ID
Allocation](#steering-note-id-allocation) applied to a second family: *a
bookkeeping defect never rewrites a citation in a normative document.*

**The SN-15 precedent is noted and not followed.** Two `GH-` IDs *have* been
renumbered before — `P6-GH-1` → `P6-GH-12` and `P6-GH-2` → `P6-GH-13`. The
difference is the one the separating rule turns on: **those renumbers happened
before the IDs had reached the normative tier, and these have.** `P6-GH-1` and
`P6-GH-2` survive in the corpus only as pre-renumber historical references —
strings in old artifacts, not live IDs.

### `GH-` identifiers are cited in full phase-prefixed form

**In any `governance/` document, a `GH-` identifier is written in full
phase-prefixed form — `P6-GH-10`, never as a bare `GH-<n>`.**

*(This section states the prohibited form as the metavariable `GH-<n>` rather
than spelling out a real number. That is deliberate: a rule document that
contained a literal instance of the string it prohibits would be found by every
sweep run against this rule, including its own. **The form is described here, not
exhibited.**)*

**Prose outside the normative tier may abbreviate where an unambiguous antecedent
is adjacent. The normative tier may not.**

The reason follows directly from per-phase allocation: because numbering restarts
each phase, a bare `GH-<n>` names **one item per phase that has reached that
number**. Stripped of its prefix, the number 10 matches both `P5-GH-10` and
`P6-GH-10` — live, unrelated, and indistinguishable to a reader following the
citation.

**Adjacent context is not a substitute for the prefix.** The worked case is the
one that produced this rule: §11.6's History line in
`PROJECT-SYSTEM-GUIDELINES.md` carried the number 10 with no phase prefix, in a
sentence opening with **two P5 anchors** (*"SN-13 (P5)"*, *"since P5"*) against
**one P6 anchor** (*"(P6-M25)"*) — while the identifier meant `P6-GH-10`, on the
`(P6-M25)` / E25.2 anchor. **Neither the identifier
nor its context resolved it**, and a reader weighting salience over adjacency
landed on the wrong item.

This is the direct analogue of the `SN-23` date-qualification rule above, applied
to the family **cited far more widely than `SN-` ever was** — which is what makes
it the more consequential of the two.

### Artifacts keyed by level are cited by full filename

**An escalation notice is cited by its full filename, never by milestone key.**

```
.ai-project/artifacts/escalation-notices/2026-07-28T20_00_00Z__P10-M34__escalation_notice.md
```

— **not** the milestone key alone. The same metavariable discipline applies: the
prohibited form is *"the `P<n>-M<n>` notice"*, described rather than spelled out,
so that a sweep for this defect does not find it here.

The reason: **a milestone can raise more than one notice**, so the milestone key
is doing identifier work it cannot do. Two notices already share `P10-M34`, and
two share `P11-M36`.

**The demonstration is self-contained:** the escalation notice that first
reported this ambiguity —

```
.ai-project/artifacts/escalation-notices/2026-08-04T00_00_00Z__P11-M36__escalation_notice.md
```

— **was itself the second notice raised under its own milestone key**, the first
being the `2026-08-03T00_00_00Z` notice. It instantiated the defect it reported,
and counted itself in the finding rather than exempting itself. **Cited by
filename, as above, both resolve; cited by level key, neither does.**

**Generalized: any artifact family keyed by level rather than by identifier is
cited by full filename.** This covers escalation notices, rulings, closure
declarations and progress digests — families where the filename, not an allocated
ID, is the only thing that resolves to one artifact. **A level key names where an
artifact arose; it does not name which artifact it is.**

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

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.1.0 | 2026-08-06 | **New normative section "Artifact ID Citation Forms"** (E37.2, P11-M37), recording HQ Ruling 2026-08-05, Decisions 1–4, and placed as a sibling immediately after "Steering Note ID Allocation" with mutual cross-references. Four rules, ordered general → specific: **(1)** the `GH-` prefix names the phase that **filed** an item, permanently — *the record names the disposition; the identifier names the origin* — with `P10-GH-8` recorded as the worked proof and per-phase allocation stated; **(2)** `P6-GH-10…15` (forward-allocated) and `P7-GH-16…21` (global counter) ratified as **historical exceptions that are not renumbered**, with the SN-15 precedent noted and not followed; **(3)** `GH-` identifiers cited in `governance/` are written in full phase-prefixed form, never bare; **(4)** escalation notices — and any artifact family keyed by level rather than by identifier — are cited by **full filename**, never by milestone key. One cross-reference line was appended to the end of "Steering Note ID Allocation"; that section's body is otherwise unaltered. **Minor, not patch:** a new normative section is an addition. Companion change outside this document: the bare, namespace-stripped identifier at `PROJECT-SYSTEM-GUIDELINES.md:605` disambiguated to `P6-GH-10`. **Note on form:** the new section states the prohibited citation shapes as metavariables (`GH-<n>`, *"the `P<n>-M<n>` notice"*) rather than spelling them out, so that a sweep for either defect does not match the document that defines it. |
| 1.0.0 | 2026-08-05 | **Versioning convention adopted** (HQ Ruling 2026-08-04, P10-GH-8; applied by E37.1, P11-M37). This document previously carried neither a `version` field nor a `## Changelog` section. **This is its first recorded row, and no prior history is reconstructed** — for changes before this date, see `git log -- governance/systems/creation-chat-guide.md`. **Two earlier amendments are recorded here because they landed while this document could not record them**, per M36's Milestone Closure Declaration §D5 (Amendments 1 and 2 of 3): **(1)** E36.1 (P11-M36, merged `f1a5e75`, 2026-08-03) added the normative section **"Steering Note ID Allocation"** (~74 lines) — the allocation rule, the separating rule *a bookkeeping defect never rewrites a citation in a normative document*, and the statement that `SN-23` is not renumbered, with its two-meaning disambiguation table; **(2)** E36.3 (P11-M36, merged `d8f4871`, 2026-08-04) rewrote the **Re-instantiation Ritual** as the single normative statement governing Creation Chat re-instantiation, canonizing SN-26 Carry-Over 1 unchanged and adding a new **Step 4** placing the P9-M31-E31.3 model check on the canonized path. |
