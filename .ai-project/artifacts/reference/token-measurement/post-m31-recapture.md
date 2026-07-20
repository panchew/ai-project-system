---
project: ai-project-system
phase: P9
milestone: M31
type: reference
status: active
last_updated: 2026-07-20
---

# Post-M31 Measurement Recapture — Comparison Note

**What this is:** the honest re-check the M31 Milestone spec's "Post-M31 Measurement
Recapture" section calls for — did E30.3's (pack-reduction) and E30.4's (echo-elimination)
**forward-looking** billed-median claims move billed reality, now that M31's three epics
have run under the post-E30.3/E30.4 templates? `bin/measure-token-burn` was rerun,
unmodified, into a separate output directory so the M30 baseline stays frozen.

**Datasets:**
- Baseline (M30, frozen): [`token-burn-dataset.md`](token-burn-dataset.md) — generated
  2026-07-17T22:16:01Z, 72 session files, window 2026-06-12 → 2026-07-17.
- Recapture (this note's evidence): [`post-m31-recapture/token-burn-dataset.md`](post-m31-recapture/token-burn-dataset.md)
  / [`.json`](post-m31-recapture/token-burn-dataset.json) — generated 2026-07-20T01:15:36Z,
  76 session files, window 2026-06-12 → 2026-07-20.

---

## 1. A structural finding before the numbers: the recapture is not a clean "since window" sample

The task called for measuring "sessions since the M30 measurement window." The mechanism
has no `--since`/date-filter flag (confirmed by reading `bin/measure-token-burn`; not
added here — Hard Constraint 1) — it always scans every `*.jsonl` file currently present
in the harness session directory. Diffing the two runs' session-ID sets shows the
population is **not append-only**:

| | count |
|---|---:|
| Sessions in both runs (stable) | 67 |
| In baseline, gone from the recapture (rotated out of the harness dir) | 5 |
| New in the recapture | 9 |
| **Recapture total** | **76** |

The 5 that disappeared — `3caa6b86` (06-13, epic), `75bf59aa` (06-18, epic), `a8637d59`
(06-13, milestone), `b1d38ce2` (06-17, milestone), `b5881f04` (06-17, epic) — are gone from
`~/.claude/projects/.../*.jsonl` between the two capture times, presumably local retention
that predates this task and is outside its control. This means the recapture's aggregate
totals (§1–§2 of the recapture dataset) are **not** "baseline plus what happened since,"
they are a different, overlapping-but-not-superset sample. Any before/after delta on the
*aggregate* totals conflates real new activity with unexplained sample churn — not
attributable to E30.3/E30.4 or to anything else observed here. This is recorded as a
finding for the mechanism (a `--since` filter and/or session-ID-set stability would fix
it), not fixed in this task per Hard Constraint 1.

Additionally, 4 of the 67 stable sessions (`3331978d`, `c10b3cb0`, `da848017`, `e92a5427`
— all dated 2026-07-17, i.e. live at the moment the M30 baseline was captured) grew in
place between the two runs (more API calls, higher per-call context) because their harness
JSONL files kept being appended to after the baseline snapshot. This is the mechanism's
own documented blind spot ("Self-measurement," README.md) firing exactly as described, not
a new defect.

**Consequence for everything below:** the Direction A medians reported next are measured
correctly by the (unmodified) mechanism, but the *comparison* between the two runs is
confounded by sample churn and in-place growth. Movement — in either direction — cannot be
cleanly attributed to E30.3/E30.4 versus population drift.

---

## 2. E30.3's claim (governance-pack mechanism reduction) — cannot be tested via Direction B; Direction A shows no reduction

**What E30.3 actually claimed:** [`context-scoping.md`](context-scoping.md) §4.2 measured
a reduction of the *instructed load list* (epic 29,336→12,005, milestone 36,614→15,971,
phase 30,478→14,586 proxy tokens), computed by hand-tokenizing the new `governance/
templates/*-execution-chat-starter.md` scoping blocks — **not** by rerunning
`bin/measure-token-burn`. That document's own §7 records the design decision explicitly:
rerunning the mechanism would overwrite the frozen "before" pack definition the comparison
depends on, so the mechanism's Direction B `level_packs` was deliberately left pointing at
the same fixed M30 file set (`P9 phase starter`, `M30 milestone starter/spec`, `E30.1 epic
starter/spec`, PSG, AOG) forever.

**Recapture's Direction B pack numbers, run today:**

| level | M30 baseline pack | recapture pack | Δ |
|---|---:|---:|---:|
| phase | 30,478 | 31,812 | +1,334 (+4.4%) |
| milestone | 36,614 | 38,588 | +1,974 (+5.4%) |
| epic | 29,336 | 29,989 | +653 (+2.2%) |

**Verdict: not applicable, by design — not "unchanged."** These packs went *up*, not down,
because the mechanism (correctly, per its own frozen-baseline design) is still tokenizing
the same M30 starter/spec files, which themselves grew slightly (e.g. AOG's changelog
gained entries; P9 phase spec gained M31 content) — nothing here reflects the scoped load
lists context-scoping.md §3 defines. **The Hard Constraint 1 instruction ("mechanism
unmodified") means this recapture structurally cannot verify E30.3's pack-reduction claim
via Direction B — the reduction lives in a document, not in a rerunnable mechanism cell.**
Re-verifying it would require either a new, separately-committed measurement in the style
of context-scoping.md §4.2 (out of this task's scope — Hard Constraint: "do not edit
`bin/measure-token-burn`") or a future mechanism change that is itself a finding, not a fix
made here.

**Direction A — billed per-call context median, the number context-scoping.md §5 actually
recommended M31 re-check:**

| level | M30 baseline median | recapture median | Δ |
|---|---:|---:|---:|
| phase | 169,003 | 169,003 | 0% (n=6 both; same session set, no shift in the two middle-ranked values) |
| milestone | 129,135 | 143,575 | **+11.2%** (n=17 both; population churn — 2 sessions rotated out, 2 new ones in) |
| epic | 76,135 | 81,017 | **+6.4%** (n=39→42; 3 rotated out, 6 new in) |

**Honest verdict: no reduction observed — milestone and epic per-call medians moved up,
not down; phase held flat.** Per §1, this movement is not cleanly attributable to anything:
the milestone/epic populations are not the same sessions before and after (sample churn),
and the truly M31-scoped subsample is minuscule (see §4). The most defensible statement
this recapture supports is: **the forward-looking billed-median improvement E30.3 predicted
has not shown up yet, and this measurement cannot rule out that it never will, because
the population it would need to show up in — enough M31-scoped sessions to move a
17–42-session median — does not yet exist.**

---

## 3. E30.4's claim (reference-first echo elimination) — mechanism has no signal for it; recorded as a gap, not a proxy

The task asks whether the recapture's session population shows handoffs happening by
reference (short) rather than paste/echo (long). Reading `bin/measure-token-burn`'s
attribution rules (`SIGNAL_PATTERNS`, `classify_task`) confirms: the mechanism detects
**which files a session wrote** (spec/starter/delivery-notice/closure/review-decision
paths), not **how much artifact-body text a session's context contains**. It has no signal
that distinguishes a session that echoed a full starter body from one that pasted a
41-token reference line — both would produce identical `artifact_write_signals`.
[`echo-cost-note.md`](echo-cost-note.md) §3 (gap G14) says the same thing about the
historical dataset for the same reason.

**Honest verdict: cannot be tested by this mechanism — recorded as a gap, not inferred
from a proxy.** Per the task's own instruction ("if they don't [distinguish it], say so as
a gap rather than inventing a proxy"), no substitute metric is offered here. The only
indirect evidence available is the same Direction A medians in §2, which — if E30.4's
elimination were both fully adopted *and* large enough to show up against a 17–42-session
noisy population — would be expected to pull medians down. They did not. That is weak,
confounded evidence at best (see §1), not a measurement of reference-adoption itself.

---

## 4. Sample-size honesty

M31's own true population — sessions on the `milestone/M31` branch, the only sessions that
ran end-to-end under the post-E30.3/E30.4 templates — is **4 sessions total**, all dated
2026-07-19/07-20:

| session | date | level | task | api_calls | notes |
|---|---|---|---|---:|---|
| `4ef54b07` | 2026-07-19 | epic | execution | 62 | complete |
| `a8130717` | 2026-07-19 | epic | execution | 108 | complete |
| `dfee1a5a` | 2026-07-19 | epic | execution | 117 | complete |
| `1cb3da03` | 2026-07-20 | milestone | unattributed | 11 (at capture) | **this recapture task's own session — mid-flight, incomplete at the moment of capture** |

n=4, 3 complete. A percentage computed over a handful of sessions is a fundamentally
different claim than one computed over the baseline's n=72 (or the recapture's diluted
n=76/n=17/n=42 level buckets used in §2 — those buckets are dominated by pre-M31, in some
cases pre-M30-closure, sessions and are not an M31-only measurement). No level-median
comparison restricted to just these 4 sessions is reported here — 3–4 points is not enough
to compute a defensible median against a 17–72-point baseline, and doing so anyway would
violate Hard Constraint 3 ("do not shape the comparison to produce a positive result") in
the other direction — manufacturing false precision.

**Additional attribution limit (named in the task and confirmed here):** E30.3, E30.4, and
all three M31 epics (E31.1–E31.3) landed in the same window. Even where a real, sufficiently
large movement existed, this recapture has no way to attribute it to any one of the four
concurrent changes.

---

## 5. TTL caveat

Every median and pack figure above is a **token count**, not a dollar figure — token counts
are exact regardless of cache-write TTL. The TTL caveat (E30.2's audit-report.md: a 5-minute
vs 1-hour cache-write TTL changes `cache_creation`'s *price* weight from 1.25× to 2× base
input, bounding a dollar-cost estimate at up to +18–18.5% higher than the 1.25×-only
figure) applies only if these token counts are converted to a dollar estimate downstream —
this note does not do that conversion, and the harness session data does not record which
TTL any given `cache_creation_input_tokens` value used (same gap the audit report names).
Anyone pricing the medians above should apply the same ±18% bound E30.2 used.

---

## 6. Summary verdict

| claim | verdict |
|---|---|
| E30.3 — governance-pack reduction (Direction B) | **Not testable by this recapture.** The mechanism's pack cells are intentionally frozen to the pre-reduction file set (context-scoping.md §7 DD1); re-verifying requires a new measurement outside this task's mechanism-unmodified scope. |
| E30.3 — billed per-call context median (Direction A) | **No reduction observed.** Phase flat (169,003→169,003), milestone +11.2% (129,135→143,575), epic +6.4% (76,135→81,017) — moved the wrong direction, though not attributably (population churn, n too small for M31-only). |
| E30.4 — reference-first echo elimination | **Not testable by this recapture.** The mechanism has no signal distinguishing echo from reference; recorded as a gap (consistent with echo-cost-note.md's own G14), not inferred from a proxy. |
| Overall | **"No movement yet, window too short" — the honest, acceptable finding the Milestone spec anticipated.** M31's true measurable population is 4 sessions (3 complete). The mechanism itself needs a `--since`/session-ID-stability fix before a future recapture can produce a clean before/after — recorded as a finding for whoever next touches the mechanism, not fixed here. |

---

## 7. Gap/finding records (continuing the G-series informally; not edits to the frozen dataset's G1–G14)

- **Recapture-finding 1:** `bin/measure-token-burn` has no time-window filter; reruns scan
  the full current harness directory, which is not append-only (sessions are rotated out —
  §1). A future mechanism change (out of this task's scope) would need either a `--since`
  flag or to persist a stable session-ID ledger across runs to support clean longitudinal
  comparison.
- **Recapture-finding 2:** the mechanism's Direction B `level_packs` are, by
  context-scoping.md's own design decision, permanently pinned to the pre-E30.3 file set —
  rerunning `bin/measure-token-burn` will never show the E30.3 reduction, by construction.
  Anyone wanting to re-verify E30.3's pack claim needs a new artifact in the
  context-scoping.md style, not a mechanism rerun.
- **Recapture-finding 3 (= echo-cost-note.md G14, reconfirmed):** the mechanism has no
  echo-vs-reference signal.

---

## Related

- [`token-burn-dataset.md`](token-burn-dataset.md) / [`.json`](token-burn-dataset.json) — M30 baseline, frozen, unchanged by this task.
- [`post-m31-recapture/token-burn-dataset.md`](post-m31-recapture/token-burn-dataset.md) / [`.json`](post-m31-recapture/token-burn-dataset.json) — this recapture's raw output.
- [`context-scoping.md`](context-scoping.md) — E30.3, the pack-reduction claim being checked.
- [`echo-cost-note.md`](echo-cost-note.md) — E30.4, the echo-elimination claim being checked.
- [`audit-report.md`](audit-report.md) §2.1 — source of the TTL/+18% bound.
- [`README.md`](README.md) — mechanism contract, attribution rules, documented blind spots (self-measurement blind spot fired here — §1).
- [P9-M31 Milestone Spec](../../../../docs/phases/P9__Context_Handling_and_Token_Efficiency/P9-M31__milestone-spec.md) — "Post-M31 Measurement Recapture" section, this task's authority.
