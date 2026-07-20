---
project: ai-project-system
phase: P9
milestone: M31
type: task-starter
status: planned
last_updated: 2026-07-19
---

# Post-M31 Measurement Recapture — Task Starter

**Task:** re-run `bin/measure-token-burn` and honestly check E30.3/E30.4's forward-looking
billed-median claims against real post-M30 usage.
**Phase:** P9 — Context Handling and Token Efficiency
**Milestone:** M31 — Dual-Mode Working Levels & Model Guardrail (milestone-level deliverable,
**not a fourth epic** — the Milestone spec's Planned Epics section names only E31.1–E31.3;
this is the "Post-M31 Measurement Recapture" section's own deliverable, dispatched at the
epic/agent tier on the Milestone Chat's instruction, per the Milestone Execution Chat
Starter's own scope rule)
**Repository:** panchew/ai-project-system
**Branch Strategy:** `epic/P9-M31-recapture` → PR to `milestone/M31`

> **Provenance:** Authored by the Milestone Chat (P9-M31) on 2026-07-19, after all three
> M31 epics merged (E31.1 `31eff27`/PR #140, E31.2 `ec85826`/PR #141, E31.3 `d985538`/PR
> #142, plus the template hardening fix `8dbffe0`). Last milestone-level deliverable before
> the M31 Milestone Closure Declaration.

---

## Why this exists

M30's E30.3 and E30.4 both measured **mechanism-tokenized, forward-looking** reductions —
never claimed as achieved billed savings. E30.3: governance-pack token counts (mechanism
Direction B) fell epic 29,336→12,005 (−59%), milestone 36,614→15,971 (−56%), phase
30,478→14,586 (−52%) after the context-scoping standard landed. E30.4: per-handoff echo
counts fell from ~2,691–3,627 tokens to ~41–50 (reference line) for starters, ~1,401–1,975
to ~44–47 for notices. Both explicitly deferred the real question — "does this actually
show up in billed session context?" — to a later re-run, because at measurement time no
real sessions had yet run under the new scoping standard or the new reference-first rule.

**M31's own three epics are exactly that population.** Every M31 session (this Milestone
Chat's own work, and each Epic Chat's execution) ran under the post-E30.3/E30.4 templates —
scoped context loads, reference-first handoffs, no full-body starter echo. M30's original
measurement found billed per-call context medians of **phase 169K, milestone 129K, epic
76K** (`.ai-project/artifacts/reference/token-measurement/token-burn-dataset.md` §2). The
recapture's job: measure the same thing again over the sessions since that window, and
report — honestly, in either direction — whether those medians moved.

---

## Hard constraints (carried from the Milestone spec — binding)

1. **The mechanism is unmodified.** Do not edit `bin/measure-token-burn`. Any change you
   believe it needs is a finding to record, not a fix to make in this task.
2. **The M30 dataset is frozen evidence — do not overwrite it.** Running the tool with its
   default `--out` (`.ai-project/artifacts/reference/token-measurement/`) would silently
   overwrite `token-burn-dataset.json`/`.md` in place. **Use a distinct `--out` directory**
   for the recapture run (recommended:
   `.ai-project/artifacts/reference/token-measurement/post-m31-recapture/`) so both
   datasets — M30's baseline and M31's recapture — are separately committed and diffable.
3. **This is evidence collection, not a pass/fail gate.** "No movement yet, window too
   short" is an acceptable, honest finding. Do not shape the comparison to produce a
   positive result.
4. **State the TTL caveat** the Milestone spec names: a +18% bound on measured medians if
   the sessions in the recapture window include 1-hour-TTL prompt-cache writes (the same
   caveat E30.2's price weighting documented).
5. **Privacy contract unchanged**: aggregated numbers and attribution labels only, exactly
   as the tool already enforces — no raw transcript content in anything you commit.
6. Full test suite passes (363 baseline, no new skips) — this task is unlikely to touch
   test-covered code (it runs an existing script and commits its output), but verify.

---

## What to do

1. **Create branch** `epic/P9-M31-recapture` from `milestone/M31`.
2. **Run the mechanism**, unmodified, over sessions since the M30 measurement window
   (2026-07-17 → now): `bin/measure-token-burn --out
   .ai-project/artifacts/reference/token-measurement/post-m31-recapture/`. If `tiktoken`
   is unavailable in this environment, `--no-corpus` is acceptable — record that Direction
   B (corpus tokenization) was skipped and why, rather than silently omitting it.
3. **Compare, honestly, against both forward-looking claims**:
   - **E30.3's claim** (governance-pack mechanism reduction) — does the recapture's
     Direction B corpus/pack sizing reflect the reduced packs? Does the recapture's
     Direction A billed per-call context median (phase/milestone/epic) show a lower value
     than M30's baseline (169K/129K/76K)? State the number, the sample size, and whether
     the movement (if any) is plausibly attributable to E30.3 given the window's other
     changes (E30.4, E31.1–E31.3 also landed in this window — attribution across three
     concurrent changes is a genuine limit, not to be papered over).
   - **E30.4's claim** (reference-first echo elimination) — does the recapture's session
     population show handoffs happening by reference (short) rather than paste/echo
     (long)? The mechanism's existing attribution rules may or may not distinguish this
     directly — if they don't, say so as a gap rather than inventing a proxy.
   - **Sample size honesty**: M31's own session count is small (three epics, one milestone
     chat, over ~1 day). State the recapture's n plainly next to any percentage — a
     percentage over a handful of sessions is a different claim than one over 72 (M30's
     baseline n).
4. **Note the TTL caveat** explicitly wherever a dollar or median figure is stated.
5. **Commit the recapture** at:
   - `.ai-project/artifacts/reference/token-measurement/post-m31-recapture/` — the raw
     `token-burn-dataset.{json,md}` this run produces (same shape as M30's, separate
     directory).
   - `.ai-project/artifacts/reference/token-measurement/post-m31-recapture.md` — a short
     comparison note (Milestone Chat's decided location, per the Milestone spec: "beside
     the M30 dataset"): cites the M30 baseline figures, the recapture figures, the honest
     verdict per claim (moved / not moved / can't isolate), the TTL caveat, and the sample-
     size caveat. Cross-link both datasets.
6. **Run the full test suite**; commit; open a PR to `milestone/M31`.
7. **Stop.** Do not merge — the Milestone Chat reviews and merges, same as every Epic PR
   in this milestone. Report completion by reference (path + one-line summary), not by
   pasting the comparison note's body into chat.

---

## What you must NOT do

- ❌ Edit `bin/measure-token-burn`
- ❌ Overwrite `token-burn-dataset.json`/`.md` (M30's frozen evidence) — use the separate
  `--out` directory
- ❌ Claim billed savings as achieved where the recapture only shows directional or
  inconclusive movement
- ❌ Merge the PR / infer acceptance
- ❌ Expand scope into anything else on the M31 handoff list (that's all epic-scoped and
  already delivered) or into M32 territory

---

## Reference Materials

- `bin/measure-token-burn` (the mechanism — read its own docstring for direction A/B/C and
  the `--sessions-dir`/`--out`/`--no-corpus` flags; unmodified)
- `.ai-project/artifacts/reference/token-measurement/token-burn-dataset.md` §2 (M30's
  baseline billed per-call medians: phase 169K, milestone 129K, epic 76K) — the frozen
  comparison target
- `.ai-project/artifacts/reference/token-measurement/context-scoping.md` (E30.3 — what
  changed, mechanism-tokenized pack sizes)
- `.ai-project/artifacts/reference/token-measurement/echo-cost-note.md` (E30.4 — what
  changed, per-handoff echo elimination)
- `.ai-project/artifacts/reference/token-measurement/README.md` (mechanism contract,
  privacy rules, gap-record conventions)
- [P9-M31 Milestone Spec](P9-M31__milestone-spec.md) — "Post-M31 Measurement Recapture"
  section (this task's authority)
- [Milestone Closure Declaration] — not yet written; this recapture's output is its
  evidence annex once committed

---

## Exit Conditions

Stop when the recapture datasets and comparison note are committed, the PR is open to
`milestone/M31`, and the suite is green. Report: "Recapture task complete. Comparison note
at `.ai-project/artifacts/reference/token-measurement/post-m31-recapture.md` — <one-line
verdict>. Awaiting Milestone Chat review and human merge authorization."
