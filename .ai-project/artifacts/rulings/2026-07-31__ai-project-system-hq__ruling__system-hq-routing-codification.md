---
type: hq_ruling
steering_note_ref: .ai-project/artifacts/steering-notes/2026-07-31__layer-8-cfo__steering-note__system-hq-routing-model.md
concern_id: SN-29 (renumbered from SN-1 on 2026-08-04 by P11-M36-E36.2; see the Amendment note below)
issued_by: HQ Chat (ai-project-system)
issued_to: Creation Chat (P11 scoping), the P11 Phase Chat that receives the placement
phase: P10 (closed) → P11 (unscoped)
date: 2026-07-31
status: active
blocking_resolved: true
---

# HQ Ruling — SN-1 Accepted: System HQ Routing and Origination Are Codified in P11, Minimally

**Steering Note:** Layer-8/CFO to HQ Chat, 2026-07-31, scribed by System HQ — *Routing and
human-originated requests are unrecorded field practice* [MEDIUM]

> **Amendment 2026-08-04 (P11-M36-E36.2) — the concern this ruling answers was renumbered
> `SN-1` → `SN-29`.** The Layer-8/CFO note
> (`.ai-project/artifacts/steering-notes/2026-07-31__layer-8-cfo__steering-note__system-hq-routing-model.md`)
> was filed claiming `SN-1`, an ID already held by the 2026-06-12 Creation Chat note. **HQ Ruling
> 2026-08-01, Decision 3** ruled it misnumbered and ordered the renumber; `SN-29` was allocated by
> the rule now recorded in `governance/systems/creation-chat-guide.md` §"Steering Note ID
> Allocation". **Every `SN-1` below — including this document's title and the Disposition — refers
> to the Layer-8/CFO note and now reads `SN-29`.** The text is left as issued rather than rewritten:
> the citations were correct at their date, and recording the rename here keeps it legible *as* a
> rename. Nothing this ruling decided is changed.

D1–D4 are **CFO decisions already made.** HQ does not re-decide them and this ruling does not
restate them as though they were open. What HQ owes is triage, placement, and the constraints the
codification must satisfy.

---

## Decision 1 — Accepted; placed in P11, early and small

The gap is real: `system-hq.md` (v1.0.2) records only the `system_request` → `system_response`
pair written back into the **requesting** project, and `system-hq-seed.md` Rule 7 sanctions a
Steering Note into a project only in the re-instantiation context. Neither A→B routing nor
CFO-originated requests appear anywhere normative, and both are now standing practice.

**Placement: P11, as a small self-contained documentation amendment — not P10.** P10 closed at
`v7.1.0` on 2026-07-31 (merge `bb727a5`); reopening a closed, tagged phase for a medium-severity
documentation gap would cost more in record integrity than the delay costs in risk.

**HQ does not self-scope a phase.** The Creation Chat sets P11's spine. This ruling registers the
item and its constraints so that whatever spine is chosen, the placement is a slotting decision
rather than a fresh analysis. It is small, independent of Drivr, and has no dependency on any
other carry-forward — it can sit in the first milestone that has room.

---

## Decision 2 — The codification is minimal, and "minimal" is defined here

Per the CFO's own second next-action: **record D1–D3 as practice already in use; do not expand
System HQ authority.** The SN-21/SN-22 pin — System HQ is not a "mighty governing System Chat" —
stands. Concretely, the amendment:

- **Adds** a short *Routing & Origination* section to `governance/systems/system-hq.md` recording
  D1 (route to B via B's own artifact channels; **routing never commands** — B's chain triages
  under its own governance), D2 (CFO-originated requests, scribed), and D3 (operating scope:
  primarily config and setup; planned work only in specific cases and then execution-only against
  artifact authorization).
- **Adds no new authority, no new decision rights, and no new artifact type.**
- **Carries status-vocabulary and changelog hygiene** for that document.

---

## Decision 3 — Reuse `steering_note` for the routed-to-B leg. Ratified, with the reason stated.

The CFO's preference is ratified, and HQ records *why* rather than deferring, because the reason
is the load-bearing part:

**A `steering_note` already encodes exactly the semantics D1 requires — direction, not
authorization.** That is the whole content of "routing never commands." Inventing a
`routing_request` (or similar) would create an artifact whose authority semantics are undefined
on arrival, and the first thing a receiving chain would have to decide is whether it must comply.
That question is precisely what D1 answers *no* to, and the existing type answers it by
construction. A new type is therefore not merely a larger decision — it would be a **worse** one.

Issuer: System HQ. Target: project B's HQ Chat. B's chain triages it like any other steering note.

---

## Decision 4 — The Authority Boundary is verbatim-frozen, and the check is a DoD item

D4 pins `system-hq.md` §Authority Boundary unchanged. HQ makes the verification explicit rather
than trusting it, because a verbatim-identical block reproduced across documents is exactly the
kind of thing that drifts under an adjacent edit:

**The amendment's Definition of Done must include a byte-level agreement check of the Authority
Boundary block across all three documents that carry it** — `governance/systems/system-hq.md`,
`governance/systems/system-hq-seed.md`, and `chat-hierarchy.md`'s out-of-hierarchy System HQ
annex — showing them identical **after** the edit. Not "was not intentionally changed" — shown
identical.

The four boundary properties stand untouched: no review/merge/scope decisions, mandatory
escalation shapes, the outward-facing confirmation rule, and no self-initiated work.

---

## Decision 5 — D2's integrity property, named so the amendment cannot lose it

D2 has a consequence the note states in passing and the amendment must carry deliberately: when
System HQ scribes a CFO-originated request, **the artifact records the true issuer
(Layer-8/CFO), not the scribe.**

If the scribe ever becomes the apparent issuer, the record loses the ability to distinguish
CFO-originated work from project-originated work — and that distinction is what makes the whole
request chain auditable after the fact. **A DoD item: the amendment must state the
issuer-vs-scribe rule explicitly and require the scribing artifact to name both.**

Worth noting that the steering note being ruled on is itself a clean instance of D2's own
vocabulary rule — an instruction landing in a project asking it to work, filed as a
`steering_note`, scribed by System HQ, `issuer_chat` recording Layer-8/CFO. The rule is coherent
in practice before it is coherent on paper, which is the SN-21 pattern the note invokes and the
right order to do it in.

---

## Decision 6 — Carry-overs

Both of the note's open items are accepted as recorded, neither blocking:

1. **A worked example in `system-hq.md`'s informative sections** — desirable once the normative
   text lands; the 2026-07-31 `social-stories-creator` ComfyUI case is the available reference
   instance. Informative, not normative; may follow in the same amendment or after it.
2. **No true A→B routing instance exists yet.** No governed project B was available at decision
   time (the ComfyUI host tree `ai-stack` is unregistered — the same `ai-stack` P10 carried
   forward as an unenrolled project, noted-not-addressed). The routing leg was exercised as
   route-back-to-A. **The first genuine A→B routing instance should be recorded in
   `system-hq.md`'s changelog when it occurs** — codifying a leg that has never run once is a
   known and accepted position here, not an oversight, precisely because D1 was practised in its
   adjacent form the same day.

**On closure, the amendment cites this steering note as its source** — the SN-21 pattern: field
practice → steering note → canon.

---

## Disposition

**SN-1 accepted, triaged closed at HQ, placed in P11.** No P10 reopening. No authority expansion.
No new artifact type. The Creation Chat carries this into P11 scoping as a registered, ready-to-slot
item — see the 2026-07-31 Progress Digest.
