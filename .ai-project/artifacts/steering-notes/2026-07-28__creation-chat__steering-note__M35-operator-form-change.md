---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-07-28T05:00:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-24
    severity: high
    title: M35's FORM is superseded before it starts — the fleet operator becomes a headless daemon (Drivr, P11), not a chat. M35's content survives intact; only its shape changes. Amend M35 before any work begins on it, or P10 will build the thing P11 is designed to make unnecessary.
decisions:
  - "The ecosystem is FOUR projects, not one. (1) AI Project System — governance, FOCUSED ON ITSELF; it does NOT coordinate the others. (2) Local Agent Runner — execution. (3) AI Project System MCP — the protocol seam between them; promoted from dormant loose end to load-bearing infrastructure. (4) Drivr (name tentative) — coordination daemon, gates, and thin surface. A fifth top-level orchestrator project was proposed and then collapsed into Drivr as redundant under the lightness criterion."
  - "Drivr's shape is HEADLESS-FIRST. An orchestrator daemon + MCP over governance state + an in-app gate surface; the chat half is RENTED from existing harnesses (Claude Code / OpenCode / Copilot), not built. The CFO first chose the opposite — 'the app IS the tool', i.e. building an own agent client with streaming, tool-call rendering, diffs and permission prompts — and then reversed it on adding the criterion 'as agentic as we can, so the infrastructure is as light as possible'. The single-window experience is a NICE TO HAVE, not a requirement. The own-client shape remains possible but unbuilt."
  - "The inversion that drove the reversal, recorded so it is not re-litigated: a dashboard is a surface for WATCHING. The more genuinely agentic the machine, the less there is to watch. At the limit the surface is 'a gate needs your key', not an IDE. Maximum autonomy and minimum infrastructure point the same direction; an own agent client points against both."
  - "Drivr is P11 work. SN-23 Ratified Decision #1 (no third spin-off in P10) STANDS UNAMENDED and is not to be reopened. P10 proceeds as scoped in every respect except M35, below. The CFO continues P10 in the meantime."
  - "M35's FORM changes; its CONTENT does not. M35 as specified canonizes System Chat — a CHAT — as the fleet operator with a daily re-instantiation seed. Drivr's daemon replaces that form. What survives untouched: the operator role (runs the serialized lane, keeps registered projects current), the authority boundary, and the operator's standing brief (what the operator needs to know each cycle). What changes: chat-shaped becomes daemon-shaped, and the 'daily re-instantiation seed' becomes the daemon's operating context rather than a chat spawned each morning."
  - "The no-authority-on-speech seam gets STRONGER, not weaker, under the daemon form. A daemon has no speech at all — only gates. SN-23's seam is preserved by construction rather than by discipline."
  - "Standing principle, in the CFO's words: 'I want the system to be agentic/automatic, but I want to have the keys to the gates' and 'I am part of the system.' The human is a node INSIDE the governance graph, not an operator above it. Automation runs the machine; authority stays held."
  - "The gate queue is derived, never hand-maintained: it is whatever governance says is outstanding — authority artifacts that should exist and do not yet. The human holds the gate; the system computes the list."
  - "Gate notifications are IN-APP ONLY for now. System notifications and WhatsApp are explicitly DEFERRED — 'it can wait'. No push-notification work is to be scoped."
  - "If and when push notification is ever built, the split is binding: OUTBOUND ('a gate needs your key') is informational and harmless on any channel. INBOUND approval must NEVER be a chat reply. It travels as a signed one-time link back into the app, so the authorization artifact is still minted in-app. 'Reply YES to merge' would hole the very seam SN-23 exists to defend, and is ruled out in advance."
  - "MCP's status changed. It was named by the CFO as one of two topics (with agentic workflows) that reshaped this direction. Under the headless-first shape it is the mechanism by which any harness becomes Drivr's chat half without an own client being written. M34/E34.1 should therefore treat ai-project-system-mcp as future load-bearing infrastructure, not merely a P6-GH-15 hygiene fix."
references:
  - "Working sketch produced in session (layout, control flow, ecosystem, and gate-channel diagrams). Not an artifact; reproduce into the P11 Project Brief when P11 opens."
  - "SN-23 (2026-07-20) — P10 adoption spine. Ratified Decision #1 (no third spin-off in P10) and #7 (scheduler only when contention bites) are load-bearing for this note and are NOT amended by it."
  - "P10 phase spec §P10.3 / §Milestones M35 — the text this note asks HQ to amend."
---

# Creation Chat Steering Note — M35 Operator Form Change

## Purpose

Direction-setting session held in the Creation Chat on 2026-07-28, CFO present, following
a six-day pause in the framework repo. The pause was not drift: the CFO was reconciling two
topics — **MCP** and **agentic workflows** — against the framework's design, and specifically
against how the industry is building orchestration that automates its own self-building.

The session converged on a shape for what comes *after* P10, and that convergence is P11
material. It would normally wait. **One consequence cannot wait**, because it lands inside
P10's own remaining scope: **M35 is now specified in a form that is superseded before it has
started.** This note exists for that single reason. Everything else here is context supplied
so HQ can judge the amendment, not scope to act on.

---

## Concern for HQ Triage

### SN-24 — M35's form is superseded before it starts [HIGH]

Severity confirmed by the CFO (2026-07-28); the decisions are the CFO's.

**Detail.** M35 — *System-Operator Canonization* — is scoped and unstarted. It canonizes
**System Chat**, a chat-shaped participant, as the fleet operator: it runs the serialized
local-inference lane, keeps registered projects current, holds no authority to act
fleet-wide on speech alone, and is spawned each morning from a daily re-instantiation seed.

This session settled that the fleet operator is a **headless daemon** (Drivr, P11), not a
chat. The daemon runs whether or not anyone is looking — which is precisely what the
near-24/7 serialized lane requires and what a chat, alive only while a window is open,
structurally cannot deliver.

**Why this cannot simply wait for P11.** If M35 executes as specified, P10 will build a
chat-shaped operator and a daily-spawn seed that Drivr is designed to make unnecessary —
in the phase whose founding principle is *nothing is built because the spec says so*
(SN-23 #1). The waste is avoidable only if the amendment lands **before M35 starts**.

**What is NOT being asked.** No new capability. No Drivr work in P10. No change to M33
(closed), M34 (unstarted, unaffected in scope), or to the fixed operating posture. SN-23
Ratified Decision #1 stands unamended.

---

## The amendment, stated precisely

| M35 element | Status | Becomes |
|---|---|---|
| Operator **role** — runs the lane, keeps projects current | **Survives unchanged** | — |
| **No-authority-on-speech** seam | **Survives, strengthened** | A daemon has no speech; only gates |
| Operator's **standing brief** — what the operator needs to know each cycle | **Survives** | Daemon operating context, not a chat spawned each morning |
| Operator **form** — System Chat, a chat participant | **Superseded** | Headless daemon (Drivr, P11) |
| **Daily re-instantiation seed** — spawnable once a day | **Superseded as a ritual** | Continuous daemon context |

The normative content M35 was to record is still worth recording, and recording it in P10
is still correct — an operator role and an authority boundary are governance, and governance
is this repo's job. Only the assumption that the operator is a *chat* is retired.

---

## Supporting context — the ecosystem this comes from

The CFO's top-level goal, stated this session: **become a competitive platform builder who
leverages AI tools**, with several platforms running and generating revenue. Efficiency at
the top level is the constraint everything else is judged against.

Against that goal the framework was examined for whether it should be rebuilt agentic-first
or reconciled. The answer was **neither**: the framework stays pure governance, and a
separate governed project carries the agentic coordination. That resolves the identity
question P10 explicitly parked ("pivot vs addition") as **addition** — the framework's
identity does not change.

The four projects and their layers:

| Layer | Project | Job |
|---|---|---|
| Surface + coordination | **Drivr** *(tentative name)* | Daemon, gates, thin surface — P11 |
| Governance | **AI Project System** | The rules — focused on itself, does not coordinate |
| Execution | **Local Agent Runner** | Does the work |
| Seam | **AI Project System MCP** | How the others talk — cuts across, not a layer |

**A caution the CFO asked to be carried on the record rather than left implicit:** all four
of these are *infrastructure*. None of them is a platform, and none earns revenue. The
leverage case for building them is the CFO's to make and is not in question here — but it
is recorded so that the P11 Project Brief states it as a choice rather than letting it read
as though the infrastructure were the goal.

---

## Requested HQ actions

1. **Amend the P10 phase spec's M35 (§P10.3 and §Milestones) to the form change above, before any M35 work begins.** Content preserved, form retired. This is the only action this note requires.
2. **Do not pull Drivr into P10.** SN-23 #1 stands. Record Drivr as P11 direction so it is not lost and not started.
3. **Note MCP's promotion when M34/E34.1 runs** — `ai-project-system-mcp` is future load-bearing infrastructure, not only a P6-GH-15 hygiene fix. No scope change to E34.1 is requested; only that it not be treated as a throwaway.
4. **Record the deferred push-notification decision and the signed-one-time-link rule** so neither is re-derived later — in particular that inbound approval may never travel as a chat reply.
5. **Carry the four-project ecosystem and the headless-first rationale into the P11 opener** when P10 closes, so the P11 Creation Chat starts from the converged shape rather than re-running this session.
