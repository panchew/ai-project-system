---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-08-01T01:15:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-28
    severity: high
    title: Steering Note ID allocation is unenforced — SN-23 and SN-1 are each claimed by two different notes, and two normative documents cite "SN-23 Decision 2" meaning different decisions, one of which is superseded
decisions:
  - "Fix, do not leave. The CFO directed that these be corrected."
  - "Correction is P11 milestone work, not pre-P11 work. Recording defects is Creation Chat's standing job and happens now; amending normative documents is epic work and happens inside a governed phase with a spec, a DoD and a Stage-2 review."
references:
  - "SN-26 (2026-07-31) — Creation Chat re-instantiation ritual; same documentation-hygiene bucket."
  - "SN-27 (2026-07-31) + Amendment 1 — P11 spine; unaffected by this note."
  - "2026-07-31 Progress Digest Open Decision #3 — SN-1 System HQ codification, ruled and placed in P11; same bucket."
---

# Steering Note — Creation Chat to HQ Chat

## Purpose

Records a defect in the Steering Note record itself, found while answering an unrelated CFO
question during the 2026-07-31/08-01 Creation Chat session. **Two Steering Note IDs are each
claimed by two different notes**, and in one case the collision reaches into normative documents
that cite the ID by number. The root cause is that ID allocation has no enforcement of any kind.

This note **records**; it does not fix. The CFO directed that it be fixed, and the binding
decision below places that fix inside P11 rather than before it.

---

## Concerns for HQ Triage

### SN-28 — Steering Note ID allocation is unenforced, and two IDs are double-claimed [HIGH]

**Detail.**

#### The audit

Every note in `.ai-project/artifacts/steering-notes/` was read for its front-matter `id:` values.
Result: 28 IDs across 23 notes, **two of them double-claimed**.

| ID | Claimed by | Also claimed by |
|---|---|---|
| **SN-23** | `2026-07-18__creation-chat__steering-note__reference-dont-display.md` | `2026-07-20__creation-chat__steering-note__P10-adoption-spine.md` |
| **SN-1** | `2026-06-12__creation-chat__steering-note.md` (which claims SN-1 … SN-5) | `2026-07-31__layer-8-cfo__steering-note__system-hq-routing-model.md` |

**Verified as NOT a defect, recorded so it is not re-flagged:** `SN-12a` and `SN-12b` in
`2026-06-25__creation-chat__steering-note.md` are correctly suffixed sub-IDs of a single concern,
not a collision. An earlier pass in this session mis-flagged them; the mis-flag was a regex
artifact (`SN-[0-9]*` truncating the letter suffix), not a record defect.

#### Why the SN-23 collision is High, and it is not the duplication

A duplicate ID is untidy. **A duplicate ID cited by number in normative documents, where one of
the two meanings is partly superseded, is a trap.** Both SN-23s are actively cited:

| Document | Citation | Which SN-23 it means |
|---|---|---|
| `governance/AI-OPERATING-GUIDELINES.md` | "**SN-23 Decision 2**, ratified" and "SN-23 (CFO-ratified 2026-07-18)" | reference-first / platform agnosticism (2026-07-18) |
| `governance/systems/artifact-communication-protocol.md` | "**SN-23 Decision 2** — platform agnosticism preserved" | reference-first (2026-07-18) |
| `governance/systems/chat-hierarchy.md` | "**SN-23 Ratified Decision #2** is superseded on the Execution Mode axis only" | P10 adoption spine (2026-07-20) |
| `governance/systems/fleet-operator.md`, `fleet-operator-brief.md` | "SN-23 (operator role …)" | P10 adoption spine (2026-07-20) |

So **`AI-OPERATING-GUIDELINES.md` and `chat-hierarchy.md` both cite "SN-23 Decision 2" meaning
two entirely unrelated decisions**, and `chat-hierarchy.md` declares its one **superseded**. A
reader following the AOG citation can land on the supersession notice and conclude that
**platform agnosticism was superseded**. It was not — a different Decision 2 was, on a different
axis, in a different note.

This is the failure mode the framework repeatedly rules against: **a normative document pinned to
an identifier it does not control.** P10 closed this class twice (*governance names the tier,
routing names the model*; *governance names the role, P11 names the thing that runs it*). This is
the same defect wearing a third costume.

SN-27, filed hours ago, cites "SN-23 Ratified Decision #7" and compounds it.

#### The SN-1 collision is a different defect — an unanswered namespace question

The CFO's observation, which prompted this audit: *"one entity wrote a SN in other entity
(project) and it labeled it 'SN-1' when I was sure SNs sequence was far beyond 1."*

That instinct was right, and the diagnosis is sharper than a miscount. The note
(`2026-07-31__layer-8-cfo__steering-note__system-hq-routing-model.md`) is:

- **issued by** `Layer-8/CFO (scribed by System HQ at CFO instruction)` — a different entity;
- **filed under** `project_name: ai-project-system` — this project's namespace;
- **stored in** this project's `steering-notes/` directory;
- **numbered** `SN-1` — restarting a sequence that had already reached SN-27.

So it was numbered as though System HQ keeps its own sequence, while being filed as though it
belongs to `ai-project-system`'s. **Both cannot be true.** It is already cited as "SN-1" in the
2026-07-31 Progress Digest and in the HQ Ruling that accepted it, so the wrong number is
propagating.

**The question to answer is not "what number should it have."** It is: **does System HQ, as a
distinct entity, maintain its own Steering Note sequence?** If yes, cross-entity notes need a
namespace marker (e.g. `SHQ-1`) and the collision disappears without renumbering. If no, the note
is misnumbered and gets the next free ID. **HQ should answer the namespace question before anyone
renumbers anything** — renumbering first would bake in an answer nobody gave.

#### Root cause: allocation has no enforcement of any kind

There is **no registry, no allocation rule, and no test.** A new ID is chosen by whichever agent
is writing the note, reading prior notes and incrementing. That works exactly as well as the
author's attention, and both collisions are what it looks like when attention lapses — one from a
two-day gap between sessions, one from an entity that reasonably believed it was starting its own
sequence.

`tests/` guards `.ai-project.yml` model-key divergence but nothing guards artifact IDs.

**Required action:** HQ should place the correction in a P11 documentation milestone (see the
binding decision below), covering four things:

1. **Answer the namespace question** for cross-entity Steering Notes — prerequisite to any
   renumbering.
2. **Resolve the SN-23 collision.** **[PROPOSED — confirm]** *do not renumber.* Both notes are
   cited across normative tiers; renumbering silently invalidates every existing citation and
   rewrites a record whose honesty is the point. Instead **mandate that any citation of a
   colliding ID carries its date** — `SN-23 (2026-07-18)` — and fix the four citing documents.
   Cheaper, breaks nothing, and leaves the collision visible rather than laundered.
3. **Add an allocation rule** to the Steering Note template and `creation-chat-guide.md`: the next
   ID is the highest existing ID plus one, across the whole directory, regardless of issuing
   entity; sub-IDs use letter suffixes (`SN-12a`) as already practiced.
4. **Add a test** asserting no duplicate `id:` across `.ai-project/artifacts/steering-notes/`.
   This is the only durable fix; rules 1–3 are documentation and documentation drifts.

---

## Decisions Already Made

1. **Fix, do not leave.** The CFO directed correction.
2. **The correction is P11 milestone work, not pre-P11 work.** Recording a defect is the Creation
   Chat's standing job and happens now, outside any phase, by design. **Amending normative
   documents is epic work** and belongs inside a governed phase — with a spec, a DoD, a Stage-2
   review and a closure record. A "clean everything up before P11 starts" window would be
   ungoverned work in the one repository whose entire thesis is that work is governed, and it
   would produce exactly the artifact this project keeps ruling against: changes to normative
   documents with no reviewable record of why.

---

## Carry-Over Open Items

1. **[PROPOSED — confirm]** This note, SN-26, the SN-1 System HQ codification (already ruled and
   placed in P11), and the SN-26 re-diagnosis of P10-GH-2 form a coherent **documentation-hygiene
   milestone**. Four self-contained items, no dependencies on Drivr, all needing a milestone with
   room rather than analysis. Proposed as P11's first milestone — which satisfies the CFO's
   instinct to clean before building, while keeping the cleanup governed.
2. **[PROPOSED — confirm]** The duplicate-ID test (Required action 4) is the piece worth doing
   even if the rest is deferred, since it is the only item that prevents recurrence rather than
   describing it.
3. Whether other artifact families carry the same unenforced-ID risk — rulings, escalation
   notices, gap records (`P10-GH-*`) — was **not** audited. Only steering notes were checked. The
   `GH-` series in particular is allocated the same way and is cited far more widely.

---

## Next Action

HQ Chat should:

1. Record SN-28.
2. **Take no corrective action before P11 opens**, per binding decision 2.
3. When scoping P11, consider the documentation-hygiene milestone proposed in Carry-Over 1, and
   answer the namespace question in Required action 1 before any renumbering is specified.
4. Note that Carry-Over 3 — whether rulings, escalation notices and `GH-` gap records share this
   defect — is unaudited and may widen the scope of that milestone.
