---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-07-31T23:30:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-26
    severity: medium
    title: Creation Chat re-instantiation is described by three disagreeing surfaces and is unexecutable as written; P10-GH-2 is misdiagnosed
decisions:
  - This item is tightening, not phase scope. It must not be allowed to shape or consume P11's spine, which is being set separately and must be substantially more than process polish.
---

# Steering Note — Creation Chat to HQ Chat

> **Amendment 2026-08-04 (P11-M36-E36.2) — `SN-1` in this note was renumbered to `SN-29`.**
> Both references below to *"the SN-1 System HQ codification"* (Next Action items) mean the
> Layer-8/CFO Steering Note
> (`.ai-project/artifacts/steering-notes/2026-07-31__layer-8-cfo__steering-note__system-hq-routing-model.md`),
> renumbered per **HQ Ruling 2026-08-01, Decision 3**. **This note's own concern IDs are
> unaffected.** The text is left as issued — it was correct at its date.

## Purpose

This note closes the opening segment of the 2026-07-31 Creation Chat session — the session
convened to scope P11 in response to the 2026-07-31 Progress Digest. It hands off one
process defect found while opening that session, so that it is recorded and triaged
without being carried into P11 scoping as though it were phase-shaped work. P11 scoping
itself continues in-session and is **not** the subject of this note.

---

## Concerns for HQ Triage

### SN-26 — Creation Chat re-instantiation is described by three disagreeing surfaces, and P10-GH-2 misdiagnoses the resulting gap [MEDIUM]

**Detail:**

This session was opened by pasting the contents of `governance/templates/seed.md` with
`framework_version` filled to `7.1.0`. That is what the template instructs — line 4 is
`framework_version: <FILL: e.g., 3.0.0>` — and it produced the correct behaviour: the
E31.3 prerequisite check ran, compared the harness self-report (`claude-opus-5`) against
`.ai-project.yml`'s `models.creation` (`remote:claude-opus-5`), matched, and proceeded.
Nothing in this concern is a criticism of how the session was opened.

The defect is that **three surfaces describe how a Creation Chat is re-opened, and they
do not agree**:

| Surface | What it says to pass |
|---|---|
| `governance/templates/seed.md`, Rule 5 — Re-instantiation | "this Genesis artifact plus the current Project Brief" |
| `governance/systems/creation-chat-guide.md`, Re-instantiation Ritual, Step 3 | "exactly three artifacts and nothing else": `genesis.md`, latest Steering Note, latest Progress Digest |
| What is actually available in this repository | Neither a rendered `genesis.md` nor a Project Brief exists |

Verified for this repository at `master` (`e6315bf`):

- **No `genesis.md` exists** at the project root or under `governance/`. Only the blank
  template `governance/templates/genesis.md` exists.
- **No Project Brief exists.** The only `*brief*` files are
  `governance/systems/fleet-operator-brief.md` and
  `docs/phases/P10__.../P10-M35-E35.2__spec__operator-standing-brief.md`, neither of which
  is a Creation Chat Project Brief.
- Steering Notes and Progress Digests, by contrast, **do** exist and are current.

So `creation-chat-guide.md`'s ritual cannot be executed here as written: its artifact #1
does not exist. The Seed's Rule 5 cannot be executed either, for the same reason.

**This re-diagnoses P10-GH-2, and arguably inverts it.** P10-GH-2 is recorded — in the
2026-07-28 HQ Ruling on the paid-frontier mapping refresh, Decision 6, and in the P10
Phase Closure Declaration — as *"the Creation Chat Seed does not implement the E31.3
model-verification check … the Creation Chat Seed never picked it up."* That premise does
not hold against the repository:

- `governance/templates/seed.md:22` has carried the **Prerequisite Verification** section
  since commit `d7ee7cd` (P9-M31-E31.3, 2026-07-19) — nine days **before** the ruling that
  filed the gap.
- `governance/templates/genesis.md` carries it as well, from the same commit. `d7ee7cd`'s
  own message states it wired the check into "all five manual-chat template surfaces (the
  three Execution Chat Starters, `hq-chat-opener.md`, `genesis.md`/`seed.md`)."
- This session is direct evidence: opened from `seed.md`, the check ran.

The likelier explanation for the observed 2026-07-28 failure — a Creation Chat that ran
`claude-opus-5` against a then-configured `remote:claude-opus-4-8` and **opened anyway** —
is not a missing section in the Seed. It is that a session re-opened by
`creation-chat-guide.md`'s ritual receives three artifacts, **none of which carries a
model check**, because the only one that would (`genesis.md`) does not exist in this
project. The check is present in the templates and absent from the path actually taken.

This matters beyond bookkeeping: as filed, P10-GH-2 points a future owner at a file that
needs no change, and the real gap — an unexecutable ritual with no verification step on
its own path — would survive the fix.

**Concrete cost observed this session:** the model check ran, because the Seed was pasted.
But no Steering Note and no Progress Digest were passed in. The 2026-07-31 Progress Digest
was read only because it happened to be open in the operator's editor — luck, not ritual.
The most recent Steering Note
(`.ai-project/artifacts/steering-notes/2026-07-31__layer-8-cfo__steering-note__system-hq-routing-model.md`)
was not handed to the session at all, despite being live input to the P11 scoping this
session exists to do.

**Required action:** HQ should triage SN-26 as a documentation-reconciliation item and,
specifically:

1. **Re-diagnose P10-GH-2** against the evidence above, rather than closing it as filed.
   Its recorded premise ("the Seed never picked it up") is contradicted by `d7ee7cd` and
   by this session. Amend the carry-forward text so a future owner is pointed at the
   ritual, not at `seed.md`.
2. **Decide whether `ai-project-system` renders its own `genesis.md`** (and whether a
   Project Brief is expected for a project that reached P11 without one), or whether the
   ritual should stop naming artifacts this project does not produce. Either answer is
   fine; the current state — a normative ritual naming a non-existent file — is not.
3. **Reconcile the three surfaces to one normative statement**, with the others citing it
   rather than restating it. This is the same defect class P10 closed twice by ruling
   (*governance names the tier, routing names the model*; *governance names the role, P11
   names the thing that runs it*): a normative document pinned to something it does not
   control, here duplicated into three copies free to drift.
4. **Ensure whatever re-instantiation path is canonized carries the E31.3 check on the
   path itself**, not only in a template that path may not include.

---

## Decisions Already Made

1. **This item is tightening, not phase scope.** It is Medium-severity process hygiene and
   must not shape, seed, or consume P11's spine. P11 is required to be substantially more
   than process polish; a re-instantiation-ritual fix is a documentation amendment that
   slots into a milestone with room, in the same class as the SN-1 System HQ codification
   noted in the 2026-07-31 Progress Digest's Open Decisions #3.
2. **How this session was opened was correct and is not at fault.** Pasting `seed.md` and
   filling `framework_version` is the template's own instruction. The Seed was the only
   surface that caused any verification to happen this session, and any reconciliation
   should preserve that property rather than trade it away for tidiness.

---

## Carry-Over Open Items

1. Until the ritual is reconciled, Creation Chat sessions should be opened with the Seed
   **plus** the latest Steering Note **plus** the latest Progress Digest — the union of the
   two documented rituals, minus the artifacts that do not exist. Recorded here as working
   practice, not as a normative amendment; only HQ can make it one.
2. Whether the absence of a Project Brief for `ai-project-system` is itself a gap, or the
   correct state for a framework repository that bootstrapped itself, is unresolved and
   non-blocking. It touches the parked Brief-level "sidekick-for-external-projects"
   identity question (2026-07-31 Progress Digest, Open Decisions #6) and should not be
   entangled with it.

---

## Next Action

HQ Chat should:

1. Record SN-26 for triage. **Do not act on it before P11's spine is set** — it is input to
   a later milestone, not to P11 scoping.
2. Amend the P10-GH-2 carry-forward text per Required action #1 above, so the
   re-diagnosis travels with the item rather than living only in this note.
3. When P11 scope is being filled out, place the ritual reconciliation (Required actions
   #2–#4) in a milestone with room, alongside — not merged into — the SN-1 System HQ
   codification. Both are self-contained documentation amendments with no dependencies.
4. Take no action on the working practice in Carry-Over #1 unless it is to canonize it.
