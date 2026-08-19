---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-08-19T00:00:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-36
    severity: medium
    title: Drivr's MVP surface captured — resolves the prior note's Next Action 7; its two central behaviours depend on the completion signal (P10-GH-7 and M39), not on any missing widget
  - id: SN-37
    severity: medium
    title: Model-change qualification gate proposed — makes model-routing-policy's Change discipline executable, and answers two items the record shows as never answered; the PASS bar remains undefined
decisions:
  - "Approval reconciled without weakening either rule: the chat is where the judgment is FORMED, the signed one-time link is what CARRIES THE KEY. A chat reply is never authorization. Rests on PSG §11.6.1's ratified distinction — authorization is not review."
  - "The app writes committed artifacts; it does not hold state. One principle covering auto-opened chats, the Manual/Agentic controls, and dashboard-managed configuration."
  - "The two visual spots (planning done / implementation done) are AOG §16.6's proposed→implemented two-track default, rendered Structural, and belong in the MVP because that version costs two fenced code blocks."
  - "Generative (ComfyUI) will be reachable at a fixed ngrok URL fronting a hosted instance. In spec as written — comfyui_url accepts any well-formed http(s) URL and availability is explicitly the CFO's responsibility. No governance change required."
  - "Single-window is re-weighted from 'explicitly not a requirement' (P11) toward central. Not a contradiction of headless-first — a client of a headless daemon is still headless-first — and recorded as a deliberate change rather than drift."
  - "Board status vocabulary for active work is queued / in progress. queued is a property of the serialized inference lane, not of the epic."
  - "In-app diff review is a nice-to-have. §11.6.1 requires the review to happen, not to happen in any particular place; GitHub or an IDE satisfies it."
references:
  - "https://claude.ai/code/artifact/688a152b-df5d-4882-b48f-26108200b92c — The Drivr Window. The visual binding is recorded in SN-36 below."
  - ".ai-project/artifacts/steering-notes/2026-08-18__creation-chat__steering-note__P12-spine-fail-open.md — SN-31…SN-35, master 7af49f7. This note completes its Next Action 7."
---

# Steering Note — Creation Chat to HQ Chat

## Purpose

The 2026-08-18 note set P12's spine and recorded, as its own Next Action 7, that the CFO's **Drivr
UX vision had not been described** — a known gap in the spine's own definition, since Drivr is the
MVP half of it. **This note closes that gap** and carries one new proposal that arrived with it.

The CFO's position at the close of this session: *"I feel certain that we can finally move forward,
I don't see any gaps at the moment."*

---

## Concerns for HQ Triage

### SN-36 — Drivr's MVP surface, and what it actually depends on [MEDIUM]

**Visual binding**
- **Link:** https://claude.ai/code/artifact/688a152b-df5d-4882-b48f-26108200b92c
- **What:** mockup
- **Level:** Creation
- **State:** proposed
- **Description:** The Drivr Window — one window, four regions: a left rail of project tabs, a
  centre chat area with composer, a per-project status dashboard showing each project's current
  Phase/Milestone/Epic, and a Current Activity panel with Manual/Agentic controls and a
  go-to-blocker affordance. Rendered from the CFO's hand sketch of 2026-08-19. Carries the status
  vocabulary, the approval reconciliation, and the structural-vs-generative comparison.

**The surface, as described.** Open the app, pick a project, land where the work is: a project with
no progress opens on its seeded Creation Chat, a project with progress opens wherever attention
belongs. Agentic execution runs to completion or until a blocker escalates — and the escalation
**opens a chat by itself**. Configuration, models and modes are managed from the dashboard, *"with
UI constraints to observe governance rules."* MCP support is expected; external-dependency
integration is later.

**The strongest idea in it, and HQ should treat it as a design principle rather than a feature:**
*UI constraints to observe governance rules.* Today every rule in this framework is enforced by an
agent reading prose and choosing to comply. Making a rule **unrepresentable in the interface** is a
different class of guarantee — no agentic option at Creation or HQ (manual-only, permanently,
SN-22), no Phase or Milestone dispatch (it does not exist — Epic only), no mode control that implies
merge authority ("Mode is not authority"). **A rule that cannot be clicked outranks a rule that is
merely written**, and that is the same insight as SN-31's fail-open finding approached from the
other side.

#### What this UX depends on — the reason it is filed rather than merely recorded

*"The chat must be where the attention should be"* and *"a blocker makes it escalate and open a
chat"* are **one requirement stated twice**: the window must know, without the human, whether work
is finished and whether it is stuck.

That is `P10-GH-7` (block detection untrustworthy in both directions, High, open since M35) plus
M39's completion judgment, which on the sole roster engine projects an empty effect ledger and can
never reach `EFFECTS_VERIFIED`, returns `undetermined` on four cases of six, and on strict scoring
loses to a baseline that always answers *completed*.

**This is good news for scoping, and HQ should read it that way.** The UX and the phase spine want
the same work. It is the strongest evidence yet that SN-31's fail-open findings are **what P12 is**,
rather than a backlog carried inside it.

**A specific consequence worth naming:** the board's active states are `queued` / `in progress`, and
**`undetermined` has no cell in that vocabulary.** M39 returns it on the majority of cases. Rendering
`undetermined` as *in progress* would be the fail-open disposition drawn on a card — the interface
asserting knowledge the system does not have. This needs deciding on purpose.

#### Two structural notes

**Auto-opening a chat *"with the artifacts already applied"* is the re-instantiation ritual executed
by software.** This makes `SN-35` **load-bearing rather than tidy**: to open a chat at any level the
app needs a ritual per level, and HQ does not have one.

**`queued` is a property of the lane, not the epic.** Two epics of one milestone may both be active
while only one holds the single serialized inference lane. The board projects scheduler state onto
work items; the scheduler exists (Drivr, P11).

**Required action:** scope Drivr's surface from this binding rather than from assumption, and treat
the completion-signal work as its prerequisite rather than a parallel track.

---

### SN-37 — A qualification gate for model changes [MEDIUM]

**The CFO's proposal:** a pre-defined set of tests that must pass before a model may be changed or
swapped — his example, trying `Qwen3.8:27b` in place of the current epic-lane model.

**What it converts.** `model-routing-policy.md` already carries a **Change discipline** requiring
new cited evidence for any policy-row change; it is how `qwen2.5-coder:14b → qwen3-coder:30b` was
justified in P10-M34. **It is a prose obligation an agent reads and chooses to honour.** This
proposal makes it a gate that cannot be passed by intention alone — SN-36's UI-constraint principle
applied to model routing.

**What it answers, from the record:**

| Open item | Status before this proposal |
|---|---|
| *"Model-watch as cheap re-tests rather than scheduled investigations"* | The 2026-08-17 digest records it as **never answered.** No watch is scheduled, and it notes **E35.5's harness remains available.** |
| The `local-agent-runner` **retention bar** | Assessment was run (E38.4) and recorded; *"the bar itself was never set"* by the CFO. |
| `model-routing-policy` Change discipline | Stated, cited, unenforced. |

**The suite's first job is already known, because this project has recorded the failure twice.**
E33.2: the 14b *"returned exit 0 having done nothing — 0 tool rounds, 0 files changed."* E39.3: both
dispatches returned `VERDICT: PASS` with **zero tool rounds**, citing a configuration key the file
does not contain. Same shape both times — **the model succeeds at running and fails at doing
anything, confidently.** So the gate's first check is not quality; it is *detecting successful
nothing*: tool rounds greater than zero, files changed greater than zero, claims resolving against
files that exist.

**The open question, and it is the one the CFO has skipped before.** The **bar** — not the tests,
the threshold. "Retention bar never set" is already on the record as an open item; a qualification
suite without a pass threshold reproduces that failure with more machinery around it. E35.5 had a
concrete bar (PASS 4/5, 0 false alarms) and that is precisely why its result was usable.

**Drivr is the natural runner** — run the suite, gate the swap, record the result. No inference of
its own, consistent with its charter.

**Required action:** place this, and require the bar to be set as part of the same work rather than
deferred to first use.

---

## Decisions Already Made

Recorded in the front matter. Two are worth expanding because they resolve prior tensions rather
than adding new positions.

**Approval, reconciled without weakening either rule.** The CFO wants approvals to live in chat, in
manual mode, with a way back to agentic. P11 ruled that inbound approval must be a **signed one-time
link, never a chat reply.** These reconcile through the distinction already ratified in **PSG
§11.6.1**: *authorization is not review.* **The chat is where the judgment is formed; the link is
what carries the key.** A chat reply saying "yes, merge it" is never authorization.
*The reason is the threat model, not ceremony:* **agents can write into chats.** If a reply
authorized, an agent could author its own approval and the loop would close on itself. The signed
link is the one channel a participant in the loop cannot forge.

**Generative reachability is solved without a governance change.** A hosted ComfyUI instance behind
a **fixed `ngrok` URL** satisfies `comfyui_url` as specified — *"Any well-formed `http`/`https`
URL"*, with availability explicitly the CFO's responsibility. **A correction belongs with this:**
E29.3's two precision FAILs have been carried as evidence against the Generative track. The delivery
notice does not say that — it attributes the diagram failure to *"FLUX-schnell's known weakness with
multi-label alphanumeric text"*, a named limitation of one fast model on one box. **The finding is a
model-tier result, not a track verdict, and a hosted instance makes it re-testable.** This is
`P11-GH-2`'s environment axis, found in this chat's own reasoning and corrected by the CFO.

---

## Carry-Over Open Items

1. **Resume has never been specified.** Escalation is one-directional; the flip to manual is
   one-way. The CFO wants *"the possibility to go back to agentic"* after intervening. That
   transition asserts the blocker is resolved — a judgment with an owner — and is exactly the
   transition an impatient system will attempt on its own. Unspecified anywhere in the corpus.

2. **`undetermined` has no board state** (see SN-36).

3. **The qualification bar is unset** (see SN-37).

4. **The ngrok endpoint is stable in address, intermittent in availability.** §16.4 already handles
   this correctly and **fails closed** — where a visual would need generation and the endpoint is
   absent, the agent *"records the intent and defers it rather than fabricating a render."* Recorded
   because it is the one place in the corpus that already does what P12 exists to generalize, and is
   therefore useful to HQ as a worked model rather than an abstraction.

5. **Everything carried forward by the 2026-08-18 note remains open and is not restated here** —
   SN-30's unactioned items, SN-32, SN-34, SN-35, the three untouched digest Open Decisions, and the
   deferred per-level model/mode mapping.

---

## Next Action

1. **Scope Drivr's MVP surface from SN-36's binding**, with the completion-signal work as its
   prerequisite.
2. **Place SN-37**, requiring the PASS bar to be set as part of the work.
3. **Decide what the board renders for `undetermined`** — deliberately, not by default.
4. **Specify the resume transition**, or record explicitly that manual is terminal until ruled
   otherwise.
5. The 2026-08-18 note's seven Next Actions **stand unchanged**; its Next Action 7 is **discharged by
   this note.**
