---
type: escalation-notice
milestone: M35
issued_by: Milestone Chat (P10-M35)
issued_to: Phase Chat (P10)
date: 2026-07-31
status: open
---

# Escalation Notice: the `Getawayinsured2023` natural experiment does not exist as described — a premise error in the P10 phase spec (v1.3.0) and the M35 milestone spec

## Trigger

E35.5's back-test, verifying its harvest target before using it, found that
`Getawayinsured2023`'s live `.ai-project.yml` routes the Phase and Milestone levels to a
**remote** endpoint, not a local one:

```yaml
models:
  creation: remote:kimi-k3
  hq: remote:kimi-k3
  phase: remote:qwen3.6:27b
  milestone: remote:qwen3.6:27b
  epic_dev: local:qwen3-coder:30b
  epic_qa: local:qwen3-coder:30b
  epic_manual: local:qwen3-coder:30b
```

Two committed governing documents describe it otherwise, and both are the Phase Chat's artifacts:

| Document | What it says |
|---|---|
| **P10 phase spec §P10.3** (v1.3.0, `phase/P10`) | *"`Getawayinsured2023`'s live `.ai-project.yml` (`phase` and `milestone` **already pointed at a local model**) is a **legitimate override, not a policy violation** … and may be harvested as a natural experiment"* |
| **P10-M35 milestone spec** (Epic Detail → E35.5) | *"`Getawayinsured2023`'s own `.ai-project.yml` **already runs exactly this configuration** and is available to harvest as a natural experiment"* |

The configuration it actually runs is a **non-frontier open-weights model at a remote endpoint** —
which is an override on the *model/tier* axis (rows P3/P4 decide *paid frontier*), but says nothing
whatever about **locality**, the axis E35.5 was directed to gather evidence on.

## What Was Attempted

- E35.5 reported the discrepancy in `judgment.md` rather than proceeding as though the premise held,
  and scoped its conclusion accordingly: *"It supports the model choice and says nothing about
  running the Milestone level locally."*
- This Milestone Chat **independently verified** the file at
  `/home/panchew/soft-dev/Getawayinsured2023/.ai-project.yml` (lines 21–28) during Stage-2 review.
  The quoted block above is that read, not a restatement of the Epic's.
- The error is **not correctable within this Milestone Chat's authority**: both documents belong to
  the Phase Chat (artifact-scope adjacency, PSG §1A). A child does not edit its parent's spec.
- The M35 milestone spec's own instruction anticipated exactly this handling — *"if
  `Getawayinsured2023`'s configuration is harvested, its evidence is that project's alone until
  corroborated"* — and the honest answer is that on the locality question there was nothing to
  harvest.

## Decision Needed

1. **Whether to amend the P10 phase spec** (§P10.3, and the same claim wherever it recurs) to state
   `Getawayinsured2023`'s configuration accurately, and at what version. The Phase Chat's call; this
   Milestone Chat has not touched either document.
2. **Whether the M35 milestone spec is amended or annotated**, given M35 is closing — recording the
   correction in the **Milestone Closure Declaration** may be the lighter path, and this Milestone
   Chat can do that under its own authority if the Phase Chat prefers it.
3. **How the P10 Closure Declaration should carry it** — as a corrected premise, so a future reader
   of the row-P4 question does not inherit the belief that a fleet project was already running
   Milestone locally.

## Impact

**E35.5's delivery is unaffected and is accepted.** Its evidence is the back-test itself, which ran
`qwen3.6:27b` locally via Ollama against blinded material; that is real local evidence about the
model's Stage-2 review quality, and it stands on its own.

**What collapses is the corroboration.** The phase spec offered the natural experiment as
*additional* evidence — a project already doing this in production. There is no such project. The
consequence is narrow but real: **the evidence base for opening the Milestone-locality cell is
thinner than the phase spec assumed**, and HQ should know that when it weighs E35.5's PASS on row P4.
E35.5's own judgment already says the PASS is necessary but not sufficient; this makes one of the
reasons concrete rather than formal.

**Nothing is blocked.** M35 can close on schedule. This notice exists so the correction is recorded
where the level that owns those documents can act on it, rather than being absorbed silently by the
chat that happened to find it.

**No project was modified.** `Getawayinsured2023`'s configuration is a legitimate override and was
read only. It is not a defect and is not to be "fixed."

## Resolution

*(open — for the Phase Chat)*

## Notes

- Filed one level up, to the immediate parent, per the routing rule this very milestone recorded
  (`governance/systems/chat-hierarchy.md`, "Handback: what a blocked agentic instance owes" →
  *Routing: exactly one level*). The Phase Chat decides resolve-or-escalate.
- The finding is a small credit to the method rather than a failure of it: E35.5 was told to verify
  its inputs before using them, did, and reported what it found instead of what it was told to
  expect. A back-test that had assumed the premise would have produced a corroboration claim with
  nothing behind it.
