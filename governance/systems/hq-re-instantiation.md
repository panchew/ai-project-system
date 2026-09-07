---
type: system
status: active
effective_date: 2026-09-03
version: 1.0.0
---

# HQ Chat Re-instantiation Ritual

*(Recorded by P12-M44-E44.1 from the nine committed opener instances in
`.ai-project/artifacts/hq-openers/` — the practice was followed nine times before it was
written. It is a **record**, not a design: a discrepancy between the nine and this ritual is
a **finding**, reported in the Notes below, never silently normalized. The Creation Chat's
ritual — `governance/systems/creation-chat-guide.md` "Re-instantiation Ritual" (SN-26,
canonized P11-M36-E36.3) — is the model; this section is the single normative statement
governing **HQ Chat** re-instantiation. `governance/systems/hq-chat.md` and
`governance/templates/hq-chat-opener.md` cite it and do not restate it.)*

An HQ Chat session does not live forever. Context fills, sessions end, a session can even
fork without knowing it (the 2026-08-20 departure specimens). The ritual preserves
continuity across a reset using **committed artifacts and no session memory** — and it must
cover **departure, not only arrival**, because the case that actually occurred is the one
where nobody was there to perform the act.

---

## Step 1 — Before departure: what a departing HQ session leaves behind

Before ending a session, the departing HQ session leaves behind **committed artifacts**,
and nothing that lives only in the chat. The nine openers all describe what an **arriving**
session receives; the departure half is the one that has been missing, and it failed in
real time on 2026-08-20 (a deferral whose trigger was, in effect, a session's continued
existence). Leaving behind means committing:

- A **Progress Digest** recording the session's close-out, open decisions and their
  dispositions, at `.ai-project/artifacts/progress-digests/<ISO-date>__hq__progress-digest.md`.
- Any **decision made this session** as a committed artifact (a Steering Note for creation-side
  input, a ruling for an HQ decision) — a decision that exists only in the chat does not
  survive the session.
- **Unresolved open concerns**, each with its disposition and the action it requires.

If a session departs **without knowing it is departing** — the 2026-08-20 fork, where a VS
Code layout change split one session into two and neither could observe the other — it
cannot write anything. **The ritual therefore cannot be only an act the departing session
performs.** Something must be **reconstructible by the arriving session from committed
state alone** (Step 3 below). A gap in that reconstruction is a defect in this ritual's
Step 1 discipline — and the committed state is the only thing the arriving session can
rely on.

---

## Step 2 — What the close-out must include

Structured state, not a narrative. The close-out records:

- **Open concerns** — anything unresolved, each with an id, severity, and the action it
  requires.
- **Binding decisions** — decisions made this session that must not be re-debated, with
  their committed artifact.
- **Carry-over items** — non-blocking items passed forward.
- **Next action** — exactly what the next session should do first.

If the next session would have to guess at any of these, the close-out is incomplete.

---

## Step 3 — How to re-open: pass the opener, then the current artifacts

Open the new session by **pasting the most recent committed opener** —
`.ai-project/artifacts/hq-openers/<latest by ISO-date in the filename>__hq-chat-opener.md`
(or the opener template, `governance/templates/hq-chat-opener.md`, when no committed opener
exists). Then pass these committed artifacts, and nothing else:

1. The **most recent HQ opener** from `.ai-project/artifacts/hq-openers/` (latest by
   ISO-date in the filename).
2. The **Steering Notes the opener carries as agenda** — cited by the opener, never
   re-attached (an opener carries **unconsumed** Steering Notes as agenda and **ruled** ones
   as constraints; the convention from the 2026-08-01 opener).
3. The **most recent Progress Digest**, if one exists, from
   `.ai-project/artifacts/progress-digests/` (latest by ISO-date).

Otherwise: no chat transcript, no memory export, nothing else.

**Reconstruction from committed state alone.** If no opener, or no close-out, exists — the
departure specimens are exactly the case where they do not — the arriving session
reconstructs the handoff from committed state alone: the `supersedes:` chain of any openers
that do exist, the Steering Notes and Progress Digests stream, and `git log` of the
`.ai-project/artifacts/` trees. **Committed state is the floor, never the hope.**

---

## Step 4 — The model check runs on this path (P9-M31-E31.3)

Because Step 3 opens with the opener, a re-instantiated HQ session **runs the E31.3 model
check before it does anything else** — the opener's own *Prerequisite Verification* section
is the first instruction it receives (present in the 2026-07-28, 2026-08-01 and 2026-08-19
instances). HQ Chat is manual-only, permanently (SN-22); the session compares its
harness-reported model identity against `.ai-project.yml`'s `models.hq`. **If both are
present and disagree, the session stops and waits for human resolution.**

The mapping, the self-report method's known limits, and the absent-block/absent-key
permissive default are defined **once**, in `governance/systems/chat-hierarchy.md` "Manual
Chat Model Verification" — cited here, not restated.

---

## Step 5 — What the new session receives

A complete picture of project state with no session memory required:

- The **opener** gives the session's instantiation purpose (its `instantiation:` field — a
  scoping session, a phase-open session, an escalation triage), the current project
  context, governance versions, constraints and immediate next actions.
- The **Steering Notes** it carries as agenda give the unconsumed, binding input from the
  Creation Chat / CFO.
- The **most recent Progress Digest** gives current phase/milestone status and the
  outgoing session's close-out.

The new session opens as if continuing uninterrupted. If it cannot, the gap is a defect in
the departing session's Step 1/Step 2 close-out, or in the committed state — fix the
record, not the ritual.

---

## Where openers live, and the instance record

- **Openers live at `.ai-project/artifacts/hq-openers/`**, named
  `<ISO-date>__hq-chat-opener.md`.
- Nine instances are committed, 2026-06-12 to 2026-08-19. They are **evidence** of the
  ritual; they are read, not edited, by the work that records the ritual.

| Instance | Instantiation | Carries `supersedes:` | Carries Prerequisite Verification |
|----------|---------------|-----------------------|------------------------------------|
| 2026-06-12 | `clean-reinstantiation` | no | no |
| 2026-06-21 | `p5-scoping` | no | no |
| 2026-06-29 | `p6-phase-open` | yes | no |
| 2026-07-14 | `p8-phase-open` | yes | no |
| 2026-07-17 | `p9-scoping-open` | yes | no |
| 2026-07-20 | `p10-scoping-open` | yes | no |
| 2026-07-28 | `m34-escalation-triage` | yes | yes |
| 2026-08-01 | `p11-scoping` | yes | yes |
| 2026-08-19 | `p12-scoping` | yes | yes |

---

## Notes — divergences reported, not normalized

The stable conventions, present in **all nine** instances (measured on `master` 2026-09-03,
before this document existed): `artifact_type: hq_opener`; `artifact_version: 1.0`;
`instantiation:`; `issued_by: Creation Chat`; `project_name: ai-project-system`; `repo`;
`governance_version`; `operating_version`; `framework_version`; `active_phase`; the
`<ISO-date>__hq-chat-opener.md` filename; the `.ai-project/artifacts/hq-openers/` home; and
the provenance note that the opener is authored by the Creation Chat and filed verbatim by
the HQ session it instantiates.

Three divergences are **reported** here, and none is normalized by this ritual:

1. **`supersedes:` chaining is present in 7 of 9.** The first two instances (2026-06-12,
   2026-06-21) predate the chain. The 2026-08-19 correction to SN-35 cited the chain as
   established; the ritual treats the chain as the convention for instances that follow the
   first, and does not retroactively edit the two that lack it.
2. **The E31.3 Prerequisite Verification block is present in 3 of 9** — from 2026-07-28
   (m34-escalation-triage) onward. The first six predate the guardrail's arrival on this
   path. The ritual **requires** the check (Step 4); the six earlier instances are evidence
   of the practice before the check existed, not instances to be rewritten.
3. **The body heading form differs.** Four instances (2026-06-12, 2026-06-21, 2026-06-29,
   2026-07-14) open with "What You Are"; five (2026-07-17 onward) use the template's
   `## Project Context` form. Both are instances of the same practice; the ritual does not
   declare one canonical body layout because the evidence does not support it.

**The departure specimens are recorded because the ritual must survive them.** Specimen 1
(2026-08-20): a deferral resting on a session's continued existence failed within four
hours — the session knew what it held and still lost it. Specimen 2 (2026-08-20): a VS Code
layout change forked the session; it did not know it had departed, and its successor could
not tell that it had. **Neither is a governance failure — the root cause is environmental —
and that is exactly why the ritual cannot assume the departing session knows it is
leaving.** Step 3's reconstruction-from-committed-state rule is what makes the ritual work
when the departing session cannot act.

---

## Reference

- **HQ Chat system reference:** `governance/systems/hq-chat.md`
- **HQ Chat opener template:** `governance/templates/hq-chat-opener.md`
- **Creation Chat ritual (the model):** `governance/systems/creation-chat-guide.md`,
  "Re-instantiation Ritual"
- **Manual Chat Model Verification:** `governance/systems/chat-hierarchy.md`
- **The nine instances (evidence, read not edited):** `.ai-project/artifacts/hq-openers/`

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-09-03 | Initial record. Records the HQ re-instantiation ritual from the nine committed opener instances (`.ai-project/artifacts/hq-openers/`), covering arrival (Step 3) and **departure** (Steps 1–2) with reconstruction-from-committed-state as the floor (the 2026-08-20 departure specimens). Reports the three divergences (7/9 `supersedes:`, 3/9 E31.3 Prerequisite Verification, 4-vs-5 body-heading form) rather than normalizing them. `hq-chat.md` and the opener template cite this document rather than restating it. (P12-M44-E44.1) |