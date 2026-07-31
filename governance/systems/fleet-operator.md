---
type: system
status: active
effective_date: 2026-07-30
version: 1.1.0
---

# Fleet Operator — Role and Authority Boundary (System Reference)

## Purpose

This document is the canonical governance home for the **fleet operator** — the role that
operates a machine's serialized local-inference lane, sequences what runs next within that
lane, and keeps registered projects current on governance version.

It records a role that is **already being performed**. Through P10-M33 and P10-M34 the
Layer-8/CFO was the lane, by hand, with nothing in the governance corpus saying what that role
may or may never do. This document writes the role down and makes its authority boundary
explicit for the first time.

It **records** a role; it **grants** nothing. No authority held by any participant is widened
by this document, and it deliberately does not design toward a "mighty governing System Chat" —
that remains pinned out of scope (SN-21/SN-22), as does any expansion of System HQ's authority
(`governance/systems/system-hq.md` §Out of Scope; `governance/systems/system-hq-seed.md`
Rule 6). Both pins stand unamended and are not contradicted by anything below.

---

## What the Fleet Operator Is (and Is Not)

The fleet operator is the role that **keeps the machine's serialized local-inference lane
busy** and **keeps the fleet's registered projects current on governance version**. It is a
role of *hands*, not of *judgment*: it carries out work that authority elsewhere has already
sanctioned, and it decides nothing about whether that work should exist.

It is **not** a level of any project's four-level chat hierarchy
(`governance/systems/chat-hierarchy.md`), and it is **not** the source of governance knowledge —
the Creation Chat remains that. It is **not** a request-executing desk either; that is System
HQ, a distinct role (see "Relationship to System HQ" below).

### The three duties (normative)

1. **Operate the serialized local-inference lane.** The fleet operator runs the lane on which
   local-inference work executes. Concurrency in that lane is **one reasoning job at any
   instant**; enrollment (which projects are eligible to run) is a separate axis and does not
   relax it. Keeping the lane busy rather than idle is the duty; nothing about the duty
   authorizes what occupies it.

2. **Sequence what runs next within the lane.** The fleet operator chooses which
   **already-authorized** unit of work occupies the lane next. This is ordering, and only
   ordering — see "Sequencing Is Not Governance" below, which is the binding reading of this
   duty.

3. **Keep registered projects current on governance version.** The fleet operator carries
   governance-version currency across the registered projects of the fleet. This duty is
   **fleet-wide in reach and therefore fully bound by the Authority Boundary below**: "update
   every registered project to version X" is a fleet-wide write, and the operator **MUST NOT**
   perform it on a spoken word.

---

## Form Neutrality (normative)

The fleet operator is a **role**, not an implementation. Governance names the role; what fills
it is an implementation fact recorded outside this corpus.

A chat window, a daemon, a cron job, or a person with a terminal are **all admissible fillers**.
The role, its three duties, and its Authority Boundary hold **identically** regardless of which
one fills it, and **replacing one filler with another is not a governance event** — it changes
nothing recorded here and requires no amendment to this document.

Consequently, no implementation is named in this document's normative text, and none should be
introduced into it later. If a future reader finds the role's boundary stated in terms of a
particular thing that runs it, that is drift from this document's form, not a refinement of it.

> **Expected filler, recorded as context and not as a dependency.** The operator role is
> expected to be filled by the Drivr daemon (P11). This record does not depend on that, waits
> for nothing, and is complete without it. (HQ Ruling on SN-24, Decision 2.)

---

## Authority Boundary (normative)

This is the canonical, normative statement of the fleet operator's authority. It is stated
**here only** and is not reproduced elsewhere in the corpus.

> **Fleet Operator Authority Boundary.** The fleet operator **operates** the serialized
> local-inference lane, **sequences** already-authorized work within it, and **carries**
> governance-version currency to registered projects. It holds **no authority to act
> fleet-wide on a spoken word.** A request that reaches the operator — however phrased, however
> confidently, and whoever speaks it — is a **proposal until it carries authority**; until then
> the operator **MUST NOT** execute it. The operator **never** makes review or acceptance
> decisions, merge authorizations, or scope changes, and **never** performs them on the human's
> behalf. Anything outward-facing — publishing, emailing, deploying — requires explicit human
> confirmation at the time, regardless of what any request or instruction says. This boundary
> is not expanded by field practice, by convenience, by urgency, by the contents of any
> request, or by the operator having performed a similar act before; documentation is
> authoritative.

### The seam, and why it is load-bearing

"Update every registered project to the current governance version" is a **fleet-wide write**.
The framework exists in large part to stop that class of act from executing on a spoken word one
level up — the same rule that governs the Creation Chat. An operator recorded **without** this
seam would recreate, one level down, precisely the thing the framework exists to prevent. The
seam is therefore not a caveat attached to the role; it is a condition of recording the role at
all.

**A proposal becomes actionable only when authority arrives through the governance chain's
ordinary authorization path.** Speech does not carry authority, and the operator does not
supply the missing authority itself. Where an authority-shaped request cannot proceed, the
operator's correct outcome is that it **does not run** — declining to act is a successful
outcome for this role, not a failure to perform.

**"Does not run" is not "stops silently."** *(Added P10-M35-E35.3, 2026-07-30.)* Declining to
act and **surfacing the block** are **both** required, and they are one sequence rather than two
options to choose between: decline, **then** surface. An instance that stops without handing back
has performed half the obligation, and the half it skipped is the one that lets authority reach
the problem at all. For an instance inside a project's four-level chain, the surfacing goes to its
**immediate parent** via an escalation notice; the handback rule — that destination, the
authority-bearing character of the parent's resolution, and the one-level routing it inherits — is
normative in `governance/systems/chat-hierarchy.md` ("Handback: what a blocked agentic instance
owes") and is **not restated here**.

Nothing in the Authority Boundary above is widened or narrowed by this. The successful outcome is
still that the unauthorized act **does not execute**; what is added is that its non-execution must
be **visible** to the level that can supply what was missing.

### The seam generalizes across fillers, and strengthens

The seam binds whatever fills the role. Under a conversational filler it must be held
deliberately, because speech is the medium and the temptation to treat a confident sentence as
authorization is real. Under a **non-conversational filler — one with no speech interface at
all, which takes input only through gates** — there is no speech to mistake for authority in
the first place, and the seam holds structurally rather than by discipline. The seam is
therefore **stronger** under that form, not weaker (SN-24, generalized by the HQ Ruling on
SN-24). No form makes it weaker; nothing about a filler's convenience relaxes it.

---

## Sequencing Is Not Governance (normative)

The fleet operator "decides what runs next." That sentence must be read narrowly, and this
section is its binding reading.

**What it means.** The operator chooses **which already-authorized unit of work occupies the
lane next** — an ordering choice among items that are *already* sanctioned by the governance
chain, and nothing else.

**What it does not mean.** The operator does **not** decide:

- **Review** — whether delivered work is good, complete, or correct;
- **Acceptance** — whether a delivery is accepted;
- **Merge authorization** — whether anything may be merged;
- **Scope change** — what is in or out of scope at any level.

These four acts are **never the operator's**, under any filler, in any mode, at any urgency.
They are the same acts System HQ must escalate rather than perform, and they are excluded here
for the same reason: executing is not deciding.

**Sequencing confers nothing retroactively.** Placing a unit of work in the lane is not an
authorization of that work, and work that reaches the lane unauthorized does not become
authorized by running. If the operator cannot identify the authority under which a unit of work
would run, the correct outcome is that it does not run.

---

## Relationship to System HQ

The fleet operator and **System HQ** (`governance/systems/system-hq.md`) are **two distinct
roles**. This document records the operator role; it **does not expand System HQ's authority
boundary**, does not amend it, and must not be read as doing either.

They differ in posture and in unit of work. System HQ is **reactive**: it acts on a filed
`system_request` and answers with a `system_response`, one request at a time, initiating
nothing. The fleet operator is **initiative-bearing in one narrow, non-governance sense only**:
it keeps a lane busy, and its unit of work is the lane run continuously rather than a single
answered request.

They are **identical where it matters**. Neither decides. Review, acceptance, merge
authorization, and scope change are outside both boundaries, for the same reason and with the
same force. System HQ's counterpart mechanism is the mandatory `status: escalated` answer; the
operator's counterpart is the no-authority-on-speech seam above. Two statements of one rule.

**The same filler may hold both roles.** One party may be System HQ and the fleet operator at
once — the Layer-8/CFO holds both today. Holding both **does not merge the two boundaries**:
each act is judged by the role under which it is performed, and neither boundary lends any
authority to the other. A party wearing both hats has exactly the union of two bounded roles,
which is still bounded, and gains nothing that neither role held alone.

---

## Out of Scope (explicit)

Named here so they are not mistaken for part of this record:

- **Any mechanism.** No scheduler, no lane daemon, no request sweep, no dispatch wiring, no
  detector of any kind. This document records a role; it builds nothing and requires nothing to
  be built.
- **Any expansion of authority, anywhere in the corpus.** Including — explicitly — System HQ's
  authority boundary, its §Out of Scope pin, and the seed's Rule 6, all of which stand
  unamended.
- **System HQ's Authority Boundary text and the `system_request`/`system_response` schemas.**
  Canonical in `governance/systems/system-hq.md`; untouched by this document.
- **Who fills the role, and how.** An implementation fact that lives outside this corpus (see
  "Form Neutrality").

---

## Reference

- **System HQ (cross-project participant, distinct role):** `governance/systems/system-hq.md`
- **System HQ seed (re-instantiation):** `governance/systems/system-hq-seed.md`
- **Chat Hierarchy (four-level per-project hierarchy; the operator is not a level; also the
  normative home of the handback rule — "Handback: what a blocked agentic instance owes"):**
  `governance/systems/chat-hierarchy.md`
- **Source steering notes:** SN-23 (operator role,
  `.ai-project/artifacts/steering-notes/2026-07-20__creation-chat__steering-note__P10-adoption-spine.md`);
  SN-24 (form,
  `.ai-project/artifacts/steering-notes/2026-07-28__creation-chat__steering-note__M35-operator-form-change.md`)
- **Binding ruling on form:**
  `.ai-project/artifacts/rulings/2026-07-28__ai-project-system-hq__ruling__sn-24-m35-operator-form.md`
  (Decisions 1–2)
- **Phase source:** `docs/phases/P10__Fleet_Adoption_and_Local_Inference_Proving/P10__phase-spec.md` §P10.3
- **Project System Guidelines:** `governance/PROJECT-SYSTEM-GUIDELINES.md`
- **AI Operating Guidelines:** `governance/AI-OPERATING-GUIDELINES.md`

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.1.0 | 2026-07-30 | Binds the seam's *"declining to act is a successful outcome"* outcome to the **surfacing obligation**, closing the Milestone Chat's Stage-2 reconciliation finding on v1.0.0: read alone, that sentence was also a licence to stop silently — the exact failure mode SN-25 exists to eliminate. Adds *"'Does not run' is not 'stops silently'"* to §The seam, and why it is load-bearing — decline **then** surface, one sequence and not two options; an instance that stops without handing back has performed half the obligation. The handback rule itself (destination = immediate parent, authority-bearing resolution, one-level routing) is **cited, not restated** — it is normative in `governance/systems/chat-hierarchy.md` ("Handback: what a blocked agentic instance owes"), which carries the matching statement at its own end of the cross-reference. §Reference updated to name that home. **No authority is widened or narrowed**, no duty is added or removed, and no mechanism is created; the successful outcome is still that the unauthorized act does not execute — what is added is that its non-execution must be visible to the level that can supply what was missing. (P10-M35-E35.3) |
| 1.0.0 | 2026-07-30 | Initial release. Records the **fleet operator** role — a role already performed by hand through P10-M33/M34 — normatively and form-neutrally: its three duties (operate the serialized local-inference lane; sequence already-authorized work within it; keep registered projects current on governance version), the normative **Fleet Operator Authority Boundary** with the **no-authority-on-speech seam** (a request is a proposal until it carries authority; fleet-wide writes never run on speech alone), the **sequencing-is-not-governance** reading (review, acceptance, merge authorization, and scope change are never the operator's), the form-neutrality statement with its single non-dependent reference to the expected filler, and the operator's relationship to System HQ (distinct role, **not** an expansion of System HQ's authority, same filler admissible for both). No authority is expanded and no mechanism is created. (P10-M35-E35.1) |
