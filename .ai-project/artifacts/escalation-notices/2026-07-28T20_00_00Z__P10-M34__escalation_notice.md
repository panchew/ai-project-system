---
type: escalation-notice
milestone: M34
issued_by: Phase Chat (P10)
issued_to: HQ Chat
date: 2026-07-28
status: resolved
resolved_by: .ai-project/artifacts/rulings/2026-07-28__ai-project-system-hq__ruling__paid-frontier-model-mapping-refresh.md
resolved_date: 2026-07-28
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

**Resolved 2026-07-28 by HQ Ruling** —
`.ai-project/artifacts/rulings/2026-07-28__ai-project-system-hq__ruling__paid-frontier-model-mapping-refresh.md`.
The HQ Chat hit the identical halt on open (self-report `claude-opus-5` vs configured
`remote:claude-opus-4-8`) and decided nothing until the CFO resolved it in session.

Answering this notice's three questions in order:

1. **The mapping** — the five paid-frontier keys move to `remote:claude-opus-5`, not
   `claude-sonnet-5`. The Opus *line* was never withdrawn; a *version* of it was
   (`/model opus` → `claude-opus-5` in the same VS Code surface). `claude-sonnet-5` was
   rejected as a **tier drop** that would have re-decided the fixed P10 posture under cover of
   a bug fix. **The M30 evidence process was not re-run and did not need to be:** policy rows
   P1–P4 decide a *tier* ("Paid frontier"); `claude-opus-4-8` appears only in the mapping
   table, and the policy's own Change discipline binds **rows**, not mappings.
2. **Scope of the unavailability** — not surface-specific in the way that would matter. The
   pin cannot match any harness selection, since `/model opus` now resolves to `opus-5` and
   `opus-5 ≠ opus-4-8`. There is no harness-side action that clears it; the pin had to move.
   Your honest flag about not being able to re-verify your own session's self-report was the
   right call — it was the same mismatch.
3. **Who updated it** — HQ, directly, as a bounded and recorded exception (Ruling Decision 5).
   Every level that could normally have taken this was refused by the defect itself:
   `epic_manual` was pinned to the unavailable version, and the agentic lane is the
   `qwen2.5-coder:14b` that E33.2 proved emits exit 0 with zero work. Delegation would have
   required overriding the guardrail. Suite green at 366/0 was the acceptance gate.

Also ruled: model unavailability is now a recorded revisit trigger on the **mapping table**,
not on rows P1–P7 — a tier cannot be deprecated, only a version can. Per-level-per-project
model routing is Drivr's domain from P11; the framework builds no routing relocation in the
interim.

**M34 is unblocked** — the Milestone Chat reopens against the corrected `models.milestone` and
proceeds to Stage 1. Its refusal was correct and needs no remediation; the stale literal in
`P10-M34__milestone-execution-chat-starter.md` has been corrected in place. Declining to edit
`.ai-project.yml` and the policy rows yourself was the right adjacency call and is what made a
clean ruling possible.
