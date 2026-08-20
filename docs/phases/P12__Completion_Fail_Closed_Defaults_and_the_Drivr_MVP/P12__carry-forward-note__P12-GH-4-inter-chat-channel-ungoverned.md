---
project: ai-project-system
phase: P12
milestone: null
type: note
status: active
issuer_chat: HQ Chat (ai-project-system)
issued_to: partially placed — the narrow piece to M44; the remainder unowned
last_updated: 2026-08-20
severity: medium
---

# Carry-Forward Note — P12-GH-4: the live inter-chat channel is in daily governance use and has no normative existence

**Origin: the P12 Phase Chat, 2026-08-20**, recording that it refused to route governance content to
an unidentified peer and that **it did not derive that refusal from a rule, because there was none.**
It declined to propose the rule as scope. HQ measured the surrounding area and found the gap is wider
than the missing rule.

---

## Measurement

```
grep -ril 'SendMessage|ListAgents|peer session|inter-chat' governance/   ->  no matches
```

**Zero occurrences across the entire normative corpus** (HQ, repo, 2026-08-20).

**The corpus's communication model is artifacts plus a human courier.** `artifact-communication-protocol.md`
governs what passes between levels and in what form; **nothing describes levels talking to each other
directly**, because when it was written they could not.

**They can now, and they do.** Every escalation in P12 — R6, S5, the M44 scope question, this note's
own origin — travelled over a live peer channel the corpus does not describe, does not govern, and
does not constrain.

---

## Why this is not merely undocumented

**The governed half is working, and that is the reason the gap has been invisible.** The Phase Chat's
own discipline — *"this message is routing, not the record"* — is exactly right, and every durable
outcome this phase did land in a committed artifact. **The escalations are real, the record is
sound.** Nothing is lost.

**But two things ride the channel that are not merely routing:**

1. **§11.6 makes the acceptance record *"the merge plus the in-chat acknowledgment."*** In a
   single-chat world "in-chat" was unambiguous. **With levels as separate sessions there is no
   defined chat to be *in*.** *(HQ notes this resolves cleanly rather than opening a hole: under
   default-accept a clean delivery produces no artifact, so **the merge is the acceptance record**
   and the acknowledgment is evidence, not the act. The ambiguity is in the wording, not the
   mechanism.)*
2. **The corpus already holds the principle that governs this, and has never applied it here.**
   SN-36, ratified: a chat reply is never authorization, and the stated reason is the threat model,
   not ceremony — ***agents can write into chats.*** If a reply authorized, an agent could author its
   own approval and the loop would close on itself.

**That principle applies to inter-chat governance messaging exactly as written, and nobody has said
so.** The Phase Chat protected the **outbound** direction by judgment. **The inbound direction is the
one the threat model is actually about**, and it is equally unwritten: a message arriving over this
channel is, to its recipient, indistinguishable from one an agent composed.

---

## What the Phase Chat's refusal actually demonstrated

**It stopped because two sessions had appeared seconds earlier with roles it could not establish, and
the content was an unresolved governance obligation.** It has stated plainly that this was **a
judgment call made under time pressure** — *"exactly the condition this phase exists to remove"* —
and that the diagnosis it committed alongside it was wrong (`P11-GH-2`, corrected at M44 spec
v1.0.2).

**The action was right for a reason that did not depend on the misdiagnosis:** an address that no
longer resolves and a session that has ended are indistinguishable from the roster, so **routing was
unsafe either way.** The chat recorded that as luck-adjacent rather than dressing it up as judgment,
which is the disposition worth keeping.

---

## Disposition — SPLIT

**The narrow piece is PLACED in M44.** It applies a ratified principle to a channel nobody wrote
down; it is one normative paragraph, not a design:

> Governance content passing over a live inter-chat channel is **routing, not the record.** Nothing
> arriving over it authorizes, accepts, or closes anything; the committed artifact does. A recipient
> that cannot establish a sender's role does not act on governance content received from it.

**HQ places this despite having twice declined to load M44, and states why the two are different.**
`P12-GH-3` needed a mechanism designed and had no bounded deliverable. **This needs a ratified
principle restated in a place it already logically covers**, it has a live customer in every
escalation now in flight, and its absence was demonstrated today by a chat that had to invent the
rule under pressure.

**The remainder is FILED, unowned:** what the channel is *for*, how it relates to
`artifact-communication-protocol.md`, and whether §11.6's *"in-chat acknowledgment"* wording should
move now that chats are separate sessions. **Trigger: any work that makes chats address each other by
role** — which is M46's role registry (recorded there as an input) — **or any proposal to let
something other than a committed artifact carry an acceptance.**

**The role registry stays M46's and is not duplicated here.** The two halves are complementary and
the M44 spec already records that neither milestone should solve its half alone: **a ritual whose
artifacts nobody can locate, and a registry pointing at sessions that left nothing, are the same
failure from opposite ends.**
