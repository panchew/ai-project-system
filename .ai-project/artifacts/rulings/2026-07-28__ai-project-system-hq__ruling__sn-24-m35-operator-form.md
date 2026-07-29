---
type: hq_ruling
steering_note_ref: .ai-project/artifacts/steering-notes/2026-07-28__creation-chat__steering-note__M35-operator-form-change.md
concern_id: SN-24
opener_ref: .ai-project/artifacts/hq-openers/2026-07-28__hq-chat-opener.md
issued_by: HQ Chat (ai-project-system)
issued_to: Phase Chat (P10)
phase: P10
milestone: M35
date: 2026-07-28
status: active
blocking_resolved: true
---

# HQ Ruling — SN-24 Accepted: M35's Operator Becomes Form-Neutral; the Phase Chat Amends

**Steering Note:** SN-24 (Creation Chat, 2026-07-28, CFO present) — *M35's form is superseded
before it starts* [HIGH]
**Companion ruling this session:**
`2026-07-28__ai-project-system-hq__ruling__paid-frontier-model-mapping-refresh.md`

---

## Decision 1 — SN-24 is accepted in full. The amendment is form-only.

M35's **content** survives: the operator role, the no-authority-on-speech seam, and the
operator's standing brief. M35's **form** retires: the operator is not a chat, and there is no
daily re-instantiation ritual.

M35 also **stays in P10**. SN-24 is right that an operator role and an authority boundary are
governance, and governance is this repo's job. Nothing about the daemon's arrival in P11 makes
the normative record less necessary — it makes it a prerequisite.

---

## Decision 2 — Amend to the *role*, not to the daemon

**This is the ruling's substance, and it is not what SN-24 asked for.** SN-24 frames the change
as chat-shaped → daemon-shaped. HQ amends it one step further: M35 must name the operator by
**role**, naming **neither** a chat nor a daemon as its implementation.

The defect in M35 as written is not that "System Chat" is the wrong implementation. It is that
M35 **names an implementation at all** in a normative governance record. Substituting "Drivr's
daemon" for "System Chat" reproduces the defect with a fresher value and buys one amendment
cycle — and it would force a *second* amendment the moment Drivr's shape moves, which SN-24
itself notes is still tentative ("name tentative", "the own-client shape remains possible but
unbuilt").

This is the same lesson this session's other ruling extracted from the model-routing escalation,
and the two should be read together: **governance names the tier; routing names the model that
fills it. Governance names the operator role; P11 names the thing that runs it.** A version can
be deprecated and an implementation can be redesigned; a tier and a role cannot. Both rulings
close the same class of defect — a normative document pinned to a value that something outside
its control is free to change.

Applied to M35: the milestone records **what the fleet operator is, what it may do, and what it
may never do without authority.** Whether that operator is a chat window, a daemon, a cron job,
or a person with a terminal is an implementation fact that lives in P11's project, not in this
repo's governance corpus. The seam holds regardless — which is precisely SN-24's own argument
that the seam gets *stronger* under the daemon form, generalized: a role-level seam binds
whatever fills the role.

**Practical consequence for the Phase Chat:** where M35 currently says "System Chat", write
"the fleet operator" (or equivalent role language). Reference the daemon **once**, as
non-normative context — *"expected to be implemented by the Drivr daemon (P11); this record does
not depend on that"* — so the direction is not lost and the record does not depend on it.

---

## Decision 3 — The Phase Chat performs the amendment; HQ does not

The phase spec is the Phase Chat's artifact. HQ rules; the Phase Chat amends. Deliberately
unlike this session's other ruling, where HQ applied a change directly — **there, every level
that could act was refused by the defect itself, and the exception was recorded as such. Here
there is no deadlock:** `models.phase` now reads `remote:claude-opus-5`, the Phase Chat opens
cleanly, and normal adjacency applies. One ruling does not license the next.

**Scope of the amendment** — form-only, in `P10__phase-spec.md`:

| Location | Change |
|---|---|
| §P10.3 *System-Operator Canonization (M35)* (~L150–179) | "System Chat operates the fleet" → the operator role. Retire the **Daily re-instantiation seed** paragraph as a *ritual*; keep its content as the operator's **standing brief** (what the operator needs each cycle), form-neutral. Keep the seam paragraph and the hand-run-lane paragraph — both survive unchanged. |
| §Milestones → **M35** (~L251–266) | Goal restated to the role. **E35.1** survives essentially as-is (it is already role-and-seam work). **E35.2** changes from "daily-spawn seed" to the **operator's standing brief** — a form-neutral artifact consumable by a daemon, a chat, or a human, not an artifact spawned each morning. |
| Phase-goal list item 3 (~L61) | Same role language |
| Pinned-vision item (~L205), SN-21 seed lineage (~L327), estimate (~L353), interfaces (~L385), decisions table (~L405) | Consequential wording only |
| Amendment History / Changelog | New row citing SN-24 and this ruling; bump the spec's version |

**Timing is binding: the amendment lands *before* any M35 planning work opens, not during it.**
That is SN-24's whole reason for existing — the waste is avoidable only if the amendment
precedes the work. M35 is independent of M33/M34, so this blocks nothing in M34.

**Not in scope of the amendment:** no new capability, no Drivr work, no change to M33 (closed)
or M34 (unaffected), no change to the fixed operating posture, and no reopening of SN-23.

---

## Decision 4 — Drivr is P11. SN-23 Ratified Decision #1 stands unamended.

Restated from this session's companion ruling, which reached the same boundary from the routing
side. Drivr is recorded as P11 direction so it is not lost, and **not started**. No third
spin-off in P10. The framework's identity does not change: the "pivot vs addition" question P10
parked resolves as **addition**.

---

## Decision 5 — MCP's promotion is noted for M34/E34.1; no scope change

`ai-project-system-mcp` is future load-bearing infrastructure — the seam by which any harness
becomes the coordination layer's chat half without an own client being written — not merely a
P6-GH-15 hygiene fix.

**E34.1's scope is unchanged.** What changes is the standard of care: no throwaway choices in a
component something is going to be built on. E34.1's existing intent to replace the raw-SHA
governance pin with the `v7.0.0` tag is exactly the right instinct and should be read as
load-bearing rather than tidying. The Phase Chat carries this to the M34 Milestone Chat as
context, not as a new requirement.

---

## Decision 6 — The notification split is recorded now, binding in advance

Recorded here so it is not re-derived under time pressure by whoever eventually builds it:

- **Gate notifications are in-app only.** System notifications and WhatsApp are **deferred** —
  no push-notification work is to be scoped, in P10 or P11.
- **If push is ever built, the split is binding.** **Outbound** ("a gate needs your key") is
  informational and harmless on any channel. **Inbound approval may NEVER be a chat reply.** It
  travels as a signed one-time link back into the app, so the authorization artifact is still
  minted in-app.

"Reply YES to merge" would hole the exact seam SN-23 and Decision 2 exist to defend, at the
exact moment the human is least likely to be looking closely. Ruled out in advance rather than
argued about later.

Related and equally durable: **the gate queue is derived, never hand-maintained** — it is
whatever governance says is outstanding, i.e. authority artifacts that should exist and do not
yet. The human holds the gate; the system computes the list.

---

## Decision 7 — What the P11 opener must carry

At P10 close, the P11 opener carries forward, so the P11 Creation Chat starts from the converged
shape rather than re-running the 2026-07-28 session:

1. The **four-project ecosystem** and each project's job — including that AI Project System is
   governance **focused on itself** and does not coordinate the others.
2. The **headless-first** shape and the inversion that produced it: *a dashboard is a surface for
   watching; the more genuinely agentic the machine, the less there is to watch.* Recorded so it
   is not re-litigated — the CFO chose "the app IS the tool" and then reversed it on adding the
   lightness criterion. The own-client shape remains possible but unbuilt; the single-window
   experience is a nice-to-have, not a requirement.
3. **The CFO's own caution, carried verbatim in substance:** all four projects are
   *infrastructure*. None is a platform and none earns revenue. The leverage case for building
   them is the CFO's to make and is not in question — but the P11 Project Brief must state it as
   a **choice**, not let it read as though the infrastructure were the goal. HQ endorses carrying
   this: it is the one line in SN-24 most likely to be quietly dropped, and the most valuable to
   keep.
4. The standing principle: *"I want the system to be agentic/automatic, but I want to have the
   keys to the gates"* — the human is a node **inside** the governance graph, not an operator
   above it. Automation runs the machine; authority stays held.

---

## Disposition

**SN-24 — accepted, amended in scope by Decision 2, triaged closed at HQ.** All five requested
HQ actions are answered: #1 ruled and delegated (Decisions 1–3), #2 ruled (Decision 4), #3 noted
(Decision 5), #4 recorded (Decision 6), #5 scheduled (Decision 7).

The Phase Chat is unblocked and owes one thing: the form-only phase-spec amendment, before M35
planning opens. M34 proceeds in parallel and is not gated on it.
