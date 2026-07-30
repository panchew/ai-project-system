---
project: ai-project-system
phase: P10
milestone: M35
type: note
status: active
issuer_chat: Milestone Chat (P10-M35)
issued_to: Phase Chat (P10) → P10 Closure Declaration
last_updated: 2026-07-30
---

# Carry-Forward Note — P10-GH-8: `governance/systems/` versions and changelogs are inconsistent

**Recorded, not fixed.** Establishing a versioning convention across the system-tier corpus is a
governance-hygiene change of its own, larger than any M35 epic and unrelated to M35's subject. It is
recorded here so it does not evaporate with the session that found it.

**Origin:** surfaced by E35.1's Delivery Notice, which flagged it to this Milestone Chat rather than
resolving it unilaterally — the correct handling, and the reason this note exists.

---

## The finding

`governance/systems/` holds 15 documents. Five carry a `version` field and a `## Changelog` table
(`system-hq.md`, `system-hq-seed.md`, `artifact-communication-protocol.md`, `bugfix-epic-workflow.md`,
`roles-authorization-team-governance.md`). The rest — including
**`governance/systems/chat-hierarchy.md`** — carry neither.

`chat-hierarchy.md` is the sharpest case, because it is the most-amended document in the directory
and the one most often cited as normative:

| Amendment | Epic | What it added |
|---|---|---|
| Execution Mode (manual vs. agentic) | P9-M31-E31.1 | A normative axis the whole framework now cites |
| Manual Chat Model Verification | P9-M31-E31.3 | A refuse-on-mismatch rule with real teeth |
| System HQ out-of-hierarchy annex | P9-M32-E32.1 | An entire cross-project participant |
| Fleet-operator annex note + `§Reference` | P10-M35-E35.1 | A second out-of-hierarchy role |
| Execution matrix (expected) | P10-M35-E35.4 | A ratified table restoring agentic mode at Phase/Milestone |

Every one of those is dated and attributed **only** by an inline italic note in the body
(`*(Added P9-M32-E32.1, 2026-07-20.)*`). There is no single place a reader can look to see what
changed in the document and when, and no version string any other artifact can cite.

## Why it was not fixed in E35.1

E35.1's Definition of Done required system-tier front-matter and a `## Changelog` on every system
document it created or modified. It satisfied that for the document it created (`fleet-operator.md`
v1.0.0) and the one it version-bumped (`system-hq.md` v1.0.2), and **declined** to retrofit a version
and a backdated changelog onto `chat-hierarchy.md`.

**This Milestone Chat upholds that judgment.** Inventing a version number for a document that has
never had one, and reconstructing its changelog after the fact, is a corpus-wide convention decision
arriving under cover of a cross-reference edit — the precise class of unrequested widening E35.1 was
written to avoid. E35.1 instead followed that document's own established precedent (the E32.1 inline
dated note), which is consistent, attributed, and honest about what it is.

## Why it still matters

The gap is real in both directions, which is why it is recorded rather than dismissed:

- **Citability.** `system-hq.md` can be cited as "v1.0.2"; `chat-hierarchy.md` cannot be cited by
  version at all, only by branch and commit — and it is cited by *more* artifacts than any other
  document in the directory, including every Execution Chat Starter this framework produces.
- **Reconstruction cost.** Answering "when did Execution Mode become normative?" today requires
  grepping italic notes in the body. A changelog would answer it in one read.
- **It compounds.** E35.4 is expected to amend the same document again, adding the ratified execution
  matrix. Each amendment makes the retrofit larger and its reconstruction less reliable.

## Scope and owner

**Owner: unassigned.** Not P10 work — P10 is adoption, not capability, and this is corpus hygiene.
Recorded for the P10 Closure Declaration alongside P10-GH-1…GH-7.

**Trigger for revisit:** the next epic that amends a system-tier document and finds itself unable to
state what changed since a prior known-good state. Whoever takes it should decide the convention
**once** for all 15 documents rather than per-document under a passing edit — which is exactly what
E35.1 correctly refused to do.

## Explicitly not claimed

- This is **not** a defect in E35.1. E35.1's delivery is accepted; its judgment on this point is the
  reason the note is well-formed.
- This is **not** a request that E35.4 fix it. E35.4 should follow `chat-hierarchy.md`'s existing
  inline-dated-note precedent, exactly as E35.1 did, and leave the convention question here.
