---
artifact_type: hq_opener
artifact_version: 1.0
timestamp: 2026-07-28T23:30:00Z
issued_by: Creation Chat
project_name: ai-project-system
repo: https://github.com/panchew/ai-project-system
governance_version: PROJECT-SYSTEM-GUIDELINES.md v2.3.0
operating_version: AI-OPERATING-GUIDELINES.md v2.10.0
framework_version: v7.0.0
active_phase: P10 — Fleet Adoption and Local-Inference Proving (open)
instantiation: m34-escalation-triage
supersedes: .ai-project/artifacts/hq-openers/2026-07-20__hq-chat-opener.md
provenance: >
  Authored by the Creation Chat to instantiate an HQ Chat for a single purpose: triage the
  2026-07-28 P10-M34 Escalation Notice (model-routing unavailability). Not a scoping
  instantiation. To be filed verbatim by the HQ Chat session it instantiates, for the
  artifact record.
---

# HQ Chat Opener — Project Control Room

## ⚠ Prerequisite Verification — READ BEFORE ANYTHING ELSE

Per the HQ Chat Opener template and `governance/systems/chat-hierarchy.md` "Manual Chat
Model Verification" (P9-M31-E31.3): read your own harness-reported model identity and
compare it to `.ai-project.yml`'s `models.hq`. If both are present and disagree, **STOP —
state the mismatch plainly and wait for human resolution.**

**Expect a mismatch. It is pre-diagnosed, and resolving it is why this chat exists.**

- `.ai-project.yml` `models.hq` = `remote:claude-opus-4-8`
- `claude-opus-4-8` is **no longer offered** in Claude Code for VS Code (CFO finding,
  2026-07-28, recorded in the Escalation Notice)

So the guardrail will fire on open. **This is correct behavior, not a defect, and it is not
to be overridden.** Follow the rule exactly: stop, declare the mismatch, and wait. The
difference from an ordinary halt is that the human resolution the guardrail waits for **is
this chat's agenda**, and the CFO is present to give it. Do not proceed to any other HQ work
— scoping, Phase authorization, digest review — until the CFO has resolved the mapping.

## Project Context
Project: ai-project-system
Repository: https://github.com/panchew/ai-project-system (local: ~/soft-dev/ai-project-system)
Primary Language / Stack: Markdown governance corpus + Python tooling (`bin/`: daemon, orchestrator, init, version, visual, run-dev-agent, measure-token-burn) + Python test suite — **366 passing, 0 failures, 0 skips** (independently re-verified 2026-07-28)

## Governance
- PROJECT-SYSTEM-GUIDELINES.md version: v2.3.0
- AI-OPERATING-GUIDELINES.md version: v2.10.0
- framework_version: v7.0.0

## Current State
Phase: **P10 — Fleet Adoption and Local-Inference Proving (open)**. Long-lived PR #149 (`phase/P10`), not for merge until phase close.
Milestone: **M33 CLOSED** — four epics (E33.1–E33.4) delivered and verified; consolidated to `phase/P10` via PR #154 (merged 2026-07-28). **M34 BLOCKED at Stage 1** — milestone spec + execution chat starter delivered (`96ae2fb`), but the M34 Milestone Chat **cannot open** (see below). **M35 unscheduled**, and its form is under amendment per SN-24.
Active Epics: none. M34's three epics (E34.1 mcp fix, E34.2 dormant-project roadmap, E34.3 `models:` routing edit for the *agentic* `epic_dev`/`epic_qa` keys) cannot reach Stage 1 delivery while M34 is blocked.

## Why This Chat Exists

**Escalation Notice — `.ai-project/artifacts/escalation-notices/2026-07-28T20_00_00Z__P10-M34__escalation_notice.md`** (issued by the P10 Phase Chat, status: open).

The M34 Milestone Chat refused to open, correctly invoking the E31.3 manual-chat
model-verification guardrail. Diagnosis confirmed **the configuration is not the defect** —
`models.milestone: remote:claude-opus-4-8` correctly implements policy row P4 of
`.ai-project/artifacts/reference/token-measurement/model-routing-policy.md` and the fixed
P10 posture. The defect is that the pinned model is no longer available in the harness
surface in use.

**The same value maps five manual-verification keys** — `hq`, `phase`, `milestone`,
`creation`, `epic_manual` — so this is not an M34 problem. It is every manually-run chat
level, including this one.

## Evidence Gathered by the Creation Chat (2026-07-28)

The Escalation Notice frames the decision as "adopt `claude-sonnet-5` (what the CFO already
had to select) or another available model," and asks whether swapping invalidates M30's
evidence-derived policy rows. **Evidence collected after the notice was written narrows that
question substantially:**

1. **The Opus tier has not gone away — the pinned *version* was superseded.** Confirmed
   in-session by the CFO in Claude Code for VS Code, the same surface the Escalation Notice
   reports the model missing from:
   - `/model default` → `claude-sonnet-5`
   - `/model opus` → **`claude-opus-5`** — available and selectable
2. **Therefore the candidate substitution is `claude-opus-4-8` → `claude-opus-5`** — a
   same-tier successor version — **not** `→ claude-sonnet-5`, which would be a **tier drop**.
   M30's policy rows are derived for *paid frontier*; `claude-opus-5` is paid frontier.
   Whether a same-tier version refresh requires re-running M30's evidence process is HQ's
   call, but it is a materially smaller question than a tier change.
3. **This Creation Chat is running `claude-opus-5` against `models.creation:
   remote:claude-opus-4-8` — and opened anyway.** The verification ritual lives in
   `chat-hierarchy.md` and the execution chat starters; **the Creation Chat Seed does not
   implement it**, even though E31.3's own mapping table lists `creation` as one of the five
   manual-verification keys. That gap is why any manual governance chat is currently able to
   run at all. It should be recorded and closed on its merits, not left as an accidental
   escape hatch.
4. **`/model opus` resolving to `claude-opus-5` also means the mismatch will persist after
   the CFO switches models** — `opus-5 ≠ opus-4-8`. The pin must change for any manual chat
   to open cleanly. There is no harness-side action that clears this.
5. **`model-routing-policy.md`'s evidence-derived decisions are TIERS, not models.** Rows
   P1–P5 decide *"Paid frontier, manual"* (P1 creation, P2 hq), *"Paid frontier"* (P3 phase,
   P4 milestone), *"Paid frontier today; designated local-offload experiment"* (P5 epic).
   **M30 never derived `claude-opus-4-8`.** That string appears only in the policy's
   *"Mapping to `.ai-project.yml`"* table — the *implementation* of the tier decision, not
   the decision itself. **This largely answers the Escalation Notice's hardest question:**
   `claude-opus-4-8` → `claude-opus-5` is a same-tier mapping refresh that does not disturb
   the evidence-derived rows. It is not a policy change and does not require re-running
   M30's evidence process. HQ should still *state* that judgment explicitly (Action 3).
6. **A policy↔config contradiction found while verifying the above, unrelated to the
   blockage.** Policy row **P1 states "No `models:` key exists or is needed"** for the
   creation level — yet E31.3 added `creation: remote:claude-opus-4-8` to `.ai-project.yml`
   anyway. `tests/test_model_config.py` does not catch it: `creation` and `epic_manual` are
   deliberately outside its five-key `MODEL_KEYS` guard. Recorded for triage, not urgent.

## Domain Boundary — CFO Direction (2026-07-28)

**CFO's stated position, in this Creation Chat session:** *setting the model per level per
project is in the domain of Drivr now.* Before Drivr exists, the CFO's proposed interim was
to *set the model in the artifacts (the openers)* rather than in `.ai-project.yml`.

This is consistent with SN-24's four-project split — **AI Project System is governance and
does not coordinate; Drivr coordinates.** "Which model runs which level in which project" is
routing, and routing is coordination. Evidence item 5 above supports the split from the
framework's own side: the governance policy already decides **tiers**; only the mapping
table names a model. **Governance owns the tier; routing owns which model fills it.**

**Creation Chat analysis of the interim mechanism (offered for HQ's decision, not ratified
by the CFO):** moving the model value *out of `.ai-project.yml` and into the openers* costs
more than it appears, because the E31.3 guardrail reads `.ai-project.yml`, not the opener.
Relocating the source of truth means normative edits to `chat-hierarchy.md`, changes to the
opener and chat-starter templates, and updates to `tests/test_model_config.py` — framework
capability work that **Drivr would then make redundant.** That is the same trap SN-24 just
avoided with M35, one week later. Deleting the keys instead is worse: `chat-hierarchy.md`'s
documented **permissive default** means every manual chat would then open with "no
expectation is configured," degrading the guardrail to a disclaimer rather than relocating
it. There is also a structural asymmetry worth preserving — `epic_dev`/`epic_qa` must stay
machine-readable because the orchestrator reads them at dispatch; only manual levels could
ever live in prose artifacts. **The carrier follows the reader:** manual chats are
instantiated by a human from an artifact, agentic dispatch by a machine from config. Drivr
eventually reads both, which is why both collapse into it later.

**The cheaper interim this analysis suggests** — HQ to accept, modify, or reject:

1. **Bump the pin** `claude-opus-4-8` → `claude-opus-5` in `.ai-project.yml` and the policy's
   mapping table. Unblocks M34 immediately, keeps the guardrail intact, and per evidence
   item 5 needs no new M30 evidence.
2. **Carry the resolved model in the opener as documentation, not as source of truth** — the
   CFO's instinct without the expensive part. Free, and it builds the habit Drivr formalizes.
3. **Record that per-level-per-project model routing is Drivr's domain (P11)** so nobody
   builds routing relocation into the framework in the meantime.

## Objectives (this instantiation)

- Resolve the paid-frontier model mapping for the five manual-verification keys so that
  manual governance chats can open again
- Unblock M34 so P10 can resume
- Rule on the domain boundary: per-level-per-project model routing belongs to Drivr (P11),
  and decide the interim that holds until Drivr exists — without building, in P10, routing
  machinery that P11 replaces
- Record the Creation Chat Seed verification gap and the P1 policy↔config contradiction as
  tracked items
- **Not** to re-litigate the fixed P10 posture (Manual/Paid from Creation through Milestone;
  Agentic/Local at the Epic) — only which model fills the paid-frontier slot

## Constraints

- **The mapping change is a policy decision.** The Phase Chat correctly declined to edit
  `.ai-project.yml`'s `models:` block or `model-routing-policy.md`'s rows — outside its
  adjacency ("produce proposals only") and outside the evidence-derived process M30
  established for this exact policy.
- **`model-routing-policy.md`'s rows are evidence-derived** from a captured dataset tied to
  `claude-opus-4-8`'s measured spend share. Whether a same-tier successor inherits that
  evidence is a judgment HQ must state explicitly rather than assume.
- **E34.3 is a different surface.** M34's E34.3 targets the *agentic* `epic_dev`/`epic_qa`
  keys (still `local:qwen2.5-coder:14b`, proven in E33.2 to emit exit 0 with zero work).
  Unrelated to this escalation's paid-frontier keys — do not conflate them.
- **SN-24 is filed and awaiting HQ action** (`239170a`) — M35's *form* is superseded before
  it starts (chat-shaped operator → headless daemon, Drivr/P11). Content survives. Not
  urgent this session, but it is the other open item addressed to HQ.
- Solo CFO, one machine. The CFO is present for this session.

## Operating Rules
- HQ Chat is declarative only
- HQ Chat is manual-only, permanently (SN-22) — never takes an Execution Mode declaration, never runs agentically
- Coding Agents execute Epics
- Epic Execution Chat Starters are mandatory
- Documentation is authoritative

## Immediate Next Actions

1. **Run the prerequisite verification. Declare the mismatch. Wait for the CFO's resolution.**
   Do not skip and do not override.
2. **Decide the paid-frontier mapping** for `hq`, `phase`, `milestone`, `creation`,
   `epic_manual` — given that `claude-opus-5` is confirmed available and `claude-sonnet-5`
   would be a tier drop. The Domain Boundary section recommends the minimal pin bump.
3. **State explicitly whether a same-tier version refresh inherits M30's evidence** or
   requires re-running it. Evidence item 5 argues it does (the rows decide tiers, not
   models). Either answer is acceptable; leaving it unstated is not.
4. **Rule on the Domain Boundary** — that per-level-per-project model routing belongs to
   Drivr (P11), and that the framework does **not** build routing relocation in the interim.
   Accept, modify, or reject the three-step interim proposed there.
5. **Decide who applies the change** — HQ directly, or delegated to a Phase/Milestone Chat as
   an epic — and whether `model-routing-policy.md` gains a new revisit trigger for *model
   unavailability*, which its rows P1–P5 do not currently name.
6. **Record the Creation Chat Seed verification gap** (evidence item 3) as a GH carry-forward.
7. **Record the P1 policy↔config contradiction** (evidence item 6) as a GH carry-forward.
8. **Unblock M34** once the mapping is settled: the Milestone Chat reopens on the corrected
   configured model and proceeds to Stage 1 delivery of E34.1/E34.2/E34.3.
9. **Acknowledge SN-24** and schedule the M35 form amendment before any M35 work begins.

## Root Cause, Stated Plainly

Pinning `models:` to an **exact model version** means every model deprecation halts every
manual governance chat until a policy decision is made. This escalation is that failure
mode's first real-world occurrence, and it will recur at every subsequent deprecation for as
long as the pin is a version.

The structural answer is already implicit in the framework's own documents: **the policy
decides tiers (evidence item 5); only the mapping names a version.** A tier does not get
deprecated. Whether to close that gap by pinning to tier with a resolved-model indirection —
and where that indirection lives — is the **Domain Boundary** question above, and the CFO
has placed it in Drivr's domain. HQ's job this session is to decide the interim, not to
build the end state.

Recorded here so the root cause is triaged deliberately rather than inherited as a recurring
surprise.
