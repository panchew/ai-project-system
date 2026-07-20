---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-07-20T21:30:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-23
    severity: high
    title: P10 spine — fleet adoption of v7.0.0. Manual/Paid through Milestone, Agentic/Local at the Epic, fixed as posture across all enrolled projects; one serialized local-inference lane operated by System Chat; run-first ordering (validate and measure out of real epic runs, not before); local-inference substrate is the real open risk.
decisions:
  - "P10 is an ADOPTION phase, not a capability-building phase. The governance framework is ready (CFO's judgment, backed by the repo at v7.0.0). No new framework capability is built on spec and no third spin-off is spawned in P10. The goal is to get the CFO's real projects actually running under v7.0.0 so progress happens in every governed project, not just this one."
  - "Operating posture is FIXED, not a per-project menu. The agentic/manual x local/paid matrix resolves into one posture: Manual/Paid from Creation down through Milestone; Agentic/Local at the Epic. This holds for all projects. The other two cells (Agentic/Paid, Manual/Local) are technically possible and hold value, but are off the P10 critical path — revisitable later, not built now."
  - "Blast-radius GOAL is all enrolled projects; the first real step is a two-project proving pair. home_finance and local-agent-runner run first — they are furthest along (canonical governance.agent.md already installed), so a v7.0.0 epic runs there with the least yak-shaving. The rest are sequenced behind them."
  - "The dormant enrolled projects (courtis, fieldledger-assesment, Getawayinsured2023, and the empty side of ai-project-system-mcp) go on the P10 roadmap — not urgent, but rolling under v7.0.0 by end of phase. ai-project-system-mcp currently has the SUPERSEDED hq.agent.md installed (P6-GH-15 sitting live in a real project) and needs the canonical governance.agent.md."
  - "Concurrency rule: enrollment (all projects, eligible to run) and concurrency (one reasoning job at any instant) are different axes and do not conflict. Epic agents run back-to-back through a SINGLE serialized local-inference lane. Near-24/7 means the lane stays busy — the next epic starts when the last finishes — never idle, never two reasoning jobs at once."
  - "System Chat operates the fleet. It runs the serialized lane, decides what runs next, and keeps registered projects current on governance version (e.g. 'make sure all registered projects have the latest governance version'). It is the CFO's day-to-day operator/sidekick. Creation Chat remains the source of governance knowledge; System Chat remains the hands."
  - "System Chat holds NO authority to act fleet-wide on a spoken word. A request to System Chat is a proposal until it carries authority behind it — the same rule that governs the Creation Chat. 'Update every project to v7.0.0' is a fleet-wide write and must not execute on speech alone. This is the seam that must not recreate the very thing the framework exists to prevent, one level down."
  - "System Chat needs a daily re-instantiation seed — an artifact analogous to the Creation Chat's Genesis seed, ideally spawned once a day (restates the SN-22 open item). This is a concrete input for the standing SN-21 System-participant canonization work."
  - "Scheduler: hand-run the lane first. With at most two or three projects able to run an epic this week, a contention problem is not yet possible. The CFO (optionally with System Chat) IS the lane for now. A built scheduler is constructed only when real contention bites — that friction defines P10's later scope rather than a guess up front."
  - "Run-first ordering. Measurement and validation come OUT of real epic runs, not before them. This resolves the 2026-07-20 Progress Digest Decision 2 with a third option HQ did not offer: not 'fix measurement then prove the spine' nor 'accept the hand numbers and move on', but 'run real epics, then measure and validate what actually happened'. The measurement tool cannot prove a claim about work that has not run."
  - "Local-inference substrate is the real open RISK, and the last thing standing between here and go. The framework is ready; the local stack is not yet proven in the wild. The current local-agent-runner is built on Ollama; a reference setup the CFO is drawn to (Qwen3.6 27B, Q8_0, llama.cpp — see reference below) recommends against Ollama and benchmarks on Mac unified memory. The first real v7.0.0 epic on the proving pair is the experiment that settles the runtime question (keep Ollama vs switch the runner to llama.cpp + Qwen3.6). Do not decide the setup in the abstract and then adopt — adopt on the proving pair and let the first epic settle it."
  - "Parked until adoption surfaces them: (a) competing-model code review — near-standard practice, substrate already exists (CFO merge gate, Stage-2 at every parent, multi-model-capable runner); the open design question is the second reviewer's AUTHORITY (advisory vs blocking), and it touches P9-GH-1. (b) P9-GH-1, the merge-authorization hole still open at Milestone->Phase and Phase->HQ. (c) ComfyUI precision investigation. None are P10 spine; they enter scope only as real adoption friction surfaces them."
  - "Sidekick-for-external-projects (adapting this governance to serve workflows already defined by teams that hire the CFO) is an IDENTITY question, not a P10 scope item. It is Project-Brief territory — pivot vs addition — and is deliberately NOT decided here. Noted so P10 does not inherit an unstated pivot."
references:
  - "Local-model setup reference (share with System Chat): https://quesma.com/blog/qwen-36-is-awesome/ — Qwen3.6 27B dense, Q8_0 + MTP, llama.cpp (author recommends against Ollama), 64k context, ~32 tok/s at ~42 GB on MacBook M5 Max 128 GB unified memory. Author's bar: 'a third as much code, but of higher quality' — the correct trade for a bounded, reviewed Epic agent."
---

# Creation Chat Steering Note — P10 Adoption Spine

## Purpose

Direction-setting session held in the Creation Chat on 2026-07-20, CFO present, in
response to the 2026-07-20 HQ Progress Digest. The digest reported P9 closed clean at
v7.0.0 and parked HQ on a single open decision: the Creation Chat must set the P10 spine.
This note sets it. The CFO's read: "this might be the week everything clicks and the
machine starts going." The convergence below is deliberately toward doing *less* — a
fixed posture and an adoption push, not a fourth capability program.

---

## Concern for HQ Triage

### SN-23 — P10 spine: fleet adoption of v7.0.0 [HIGH]

Severity confirmed by the CFO (2026-07-20); the decisions are the CFO's.

**Detail:** P10 is adoption, not capability. Get v7.0.0 running for real across the
CFO's projects under a fixed operating posture — Manual/Paid through Milestone, Agentic/
Local at the Epic — and let real epic runs produce the measurement, validation, and
steering evidence that the framework has so far only reasoned about. See the `decisions`
list above for the full set.

---

## Fleet state (observed 2026-07-20, `~/soft-dev`)

Enrollment is real but shallow — a scaffold dropped in and mostly never run. "Adopt all"
is therefore not one action but three: cleanup, version bump to v7.0.0, then the first
real Agentic/Local epic.

| Project | Enrolled | Adoption depth |
|---|---|---|
| ai-project-system | — | The framework itself (full machinery: locks, logs, queue, 125 artifacts) |
| home_finance | yes | **Proving pair** — canonical `governance.agent.md` installed |
| local-agent-runner | yes | **Proving pair** — canonical `governance.agent.md` + some artifact activity |
| footboard | yes | Some artifact activity (7 files), no canonical agent |
| ai-project-system-mcp | yes | Has **superseded** `hq.agent.md` (P6-GH-15 live in the wild); artifacts near-empty |
| courtis | yes | Dormant — artifacts dir near-empty |
| fieldledger-assesment | yes | Dormant — artifacts dir near-empty |
| Getawayinsured2023 | yes | Dormant — artifacts dir near-empty |
| ai-stack | no | Not enrolled |
| character-factory | no | Not enrolled |

`framework_version` could not be found stamped in any project except the framework itself:
**no other project is confirmably on v7.0.0 yet.** The unenrolled two (ai-stack,
character-factory) are noted, not addressed — decide later whether they are real projects
to govern or leftovers.

---

## Requested HQ actions

1. Open P10 scoping on the SN-23 spine: adoption of v7.0.0 across the fleet under the fixed posture.
2. First milestone targets the proving pair (home_finance + local-agent-runner): version bump to v7.0.0, run the first real Agentic/Local epic, and settle the local runtime question (Ollama vs llama.cpp + Qwen3.6) from that run.
3. Roadmap the dormant enrolled projects to be rolling under v7.0.0 by end of phase; include the ai-project-system-mcp superseded-agent fix (P6-GH-15).
4. Record the parked items (competing-model code review, P9-GH-1, ComfyUI) as explicit defers that enter scope only on adoption friction — not P10 spine.
5. Note the System-Chat-as-operator model and its daily re-instantiation seed as inputs to the standing SN-21 canonization work; enforce the no-authority-on-speech seam.
