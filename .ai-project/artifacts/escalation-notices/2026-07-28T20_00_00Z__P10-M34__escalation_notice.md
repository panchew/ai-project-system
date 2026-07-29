---
type: escalation-notice
milestone: M34
issued_by: Phase Chat (P10)
issued_to: HQ Chat
date: 2026-07-28
status: open
---

# Escalation Notice: `claude-opus-4-8` unavailable in a manual-chat harness surface — model-routing policy needs a decision

## Trigger

The M34 Milestone Chat (P10-M34, opened per the Milestone Execution Chat Starter I delivered)
refused to open, invoking the P9-M31-E31.3 manual-chat model-verification guardrail
(`governance/systems/chat-hierarchy.md` "Manual Chat Model Verification"): self-reported model ≠
configured expectation for its level. Its refusal is correct behavior per that guardrail — no
override was attempted or appropriate.

Diagnosis confirmed the **configuration is not the defect**: `.ai-project.yml`'s
`models.milestone: remote:claude-opus-4-8` correctly implements policy row P4 of
`.ai-project/artifacts/reference/token-measurement/model-routing-policy.md` (M30/E30.2,
evidence-derived) and the fixed P10 posture (Manual/Paid from Creation through Milestone). The
CFO then attempted the indicated remedy — relaunch the Milestone Chat on the configured model —
and found **`claude-opus-4-8` is no longer available in Claude Code for VS Code**, the harness
surface in use, and had to select `claude-sonnet-5` instead (`/model default` → "Set model to
claude-sonnet-5").

**This is a model-availability fact, not a chat-level slip**, and it is not one of the recorded
revisit triggers in `model-routing-policy.md`'s policy rows P1–P5 (which name things like "within-
session task segmentation landing" or "M31 dual-mode runs at epic level," not "the pinned model
becomes unavailable in a harness surface"). The same `remote:claude-opus-4-8` value maps five
manual-verification keys — `hq`, `phase`, `milestone`, `creation`, `epic_manual`
(`.ai-project.yml`) — so if the unavailability is not surface-specific to this one VS Code
instance, every manually-run chat level is exposed to the same refusal, not just M34.

## What Was Attempted

1. As Phase Chat, verified the `.ai-project.yml` mapping was correct against policy — ruled out a
   config-edit fix.
2. Advised the CFO to relaunch the M34 Milestone Chat on the configured model
   (`claude-opus-4-8`).
3. CFO attempted this in Claude Code for VS Code and found the model not offered; selected
   `claude-sonnet-5` as the available alternative.
4. Did **not** edit `.ai-project.yml`'s `models:` block or `model-routing-policy.md`'s rows —
   changing the paid-frontier default is a policy decision outside Phase Chat's adjacency
   ("produce proposals only" — Phase Execution Chat Starter, Critical Rules) and outside the
   evidence-derived process M30 established for this exact policy.

## Decision Needed

HQ Chat (or, if HQ judges this a policy-authorship question, Creation Chat) needs to decide the
paid-frontier mapping going forward, given `claude-opus-4-8`'s confirmed unavailability in at
least one manual-chat harness surface:

- Adopt `claude-sonnet-5` (what the CFO already had to select) as the updated mapping for the
  five affected keys, or another available model — and whether this is a same-tier substitution
  or requires re-running M30's evidence process (the model-routing-policy.md rows are
  evidence-derived from a specific captured dataset tied to `claude-opus-4-8`'s measured spend
  share; swapping the model without new evidence may itself be worth flagging, not just
  patching).
- Whether the unavailability is scoped to this one harness surface (Claude Code for VS Code) or
  broader — worth a quick confirmation before committing a fleet-wide policy edit.
- Who updates `model-routing-policy.md` + `.ai-project.yml`'s `models:` block once decided (HQ
  directly, or delegated back to a Phase/Milestone Chat as an epic).

**Not asking HQ to re-litigate the fixed P10 posture (Manual/Paid through Milestone,
Agentic/Local at the Epic) — only which model fills the paid-frontier slot.**

## Impact

- **M34 Milestone Chat cannot open** — M34 planning oversight is paused until this resolves.
  M34's three epics (E34.1 mcp fix, E34.2 dormant roadmap, E34.3 `models:` routing edit — note:
  E34.3 targets the *agentic* `epic_dev`/`epic_qa` keys, unrelated to this escalation's
  paid-frontier keys) cannot proceed to Stage 1 delivery.
- **Every other manually-run chat level maps to the same value** (`hq`, `phase`, `creation`,
  `epic_manual`) — if the unavailability is not surface-specific, HQ Chat, Creation Chat, and
  this Phase Chat itself are all exposed to the identical refusal on their next relaunch. This
  Phase Chat session's own self-report at session start was `claude-opus-4-8`
  (`models.phase` match), but that self-report predates the CFO's finding and I have no fresher
  read on it — flagging honestly rather than asserting continued availability I cannot verify.
- No other P10 milestone is directly blocked (M33 is closed; M35 is unscheduled), but the same
  wall will recur the moment any of them opens a manual chat.

## Resolution

(empty — awaiting HQ Chat decision)
