---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-08-11T00:00:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-30
    severity: medium
    title: External assessment (issue #192) routed — independently verified, two claims corrected, four recommendations sorted by level; E38.2 unaffected
decisions:
  - "The CFO commissioned the external assessment and explicitly deferred all three routing questions to the Creation Chat ('I don't know' / 'Not sure' / 'Only if it's worth it'). Everything below is a Creation Chat RECOMMENDATION awaiting HQ action, not a CFO ruling."
references:
  - "https://github.com/panchew/ai-project-system/issues/192 — the assessment itself. Referenced, not transcribed (SN-23 of 2026-07-18: artifacts pass by reference)."
---

# Steering Note — Creation Chat to HQ Chat

## Purpose

Routes an external review (issue #192, filed 2026-08-10 at the CFO's request) into governance, and
records an independent re-measurement of its checkable claims. The issue is **not** reproduced
here — it is a durable record at a stable URL, and copying it would be the artifact echo SN-23
(2026-07-18) retired.

What this note adds is the **delta**: what verification found, and where the four recommendations
belong.

---

## Concerns for HQ Triage

### SN-30 — External assessment verified and routed [MEDIUM]

**Detail.**

#### Independent re-measurement

Per G2 — *the reviewer re-measures; the executor's report is not the evidence* — every checkable
claim was re-run on `milestone/M38`, 2026-08-11.

**Held exactly:** the AOG section-numbering defect; core docs 2,034 lines (1055 + 979); corpus
18,956 lines; verification keywords 1 hit per core document; observability keywords 0 in both.

**The section-numbering defect is worse than the issue states.** AOG contains **two sections both
titled "Error Handling"** — `## 13. Error Handling` (L701) and `## 14. Error Handling` (L861) —
so a cross-reference by *title* is ambiguous before the numbering is even considered. Full order:
`1, 1A, 2–9, 13, 14, 10, 11, 12, 13, 14, 16, 15`. Ten phases without detection.

**Two claims did not hold:**

1. **Test count 27 → actually 26** under `tests/`. The 27th is
   `.venv/lib/python3.14/site-packages/regex/tests/test_regex.py`, a vendored dependency. The row's
   Fact column reads *"in repo"* while its Layer column reads `tests/`; those disagree. **Caught by
   the layer-and-time discipline (P11-GH-2) the issue was itself applying** — worth recording as
   evidence that the discipline works, not only as a count error.
2. **The 91 / 68 normative-statement figures are not reproducible from the stated method.**
   Case-sensitive extraction of the listed keywords gives **52 / 46** matching lines (55 / 50
   occurrences); case-insensitive gives **109 / 79**. The stated figure sits between, consistent
   with case-insensitive extraction plus a manual pass dropping prose uses. That is a defensible
   method and matches the issue's own "single-pass, one reviewer" caveat — but it appears under a
   heading reading **"Verified at review time"** with layer and time, which claims more than a
   judgment call carries.

**The error is conservative.** A denominator nearer 98 than 159 moves the ratios from 13:1 and
119:1 to roughly **21:1 and 193:1** — understating the issue's own thesis rather than inflating it.

**Verdict: the shape is sound and the one concrete defect claim is real.** That is the correct
verdict on an assessment that instructed its reader in advance to treat the shape as the finding.

#### Routing — the four recommendations are three kinds of work

| Rec | Kind | Recommended placement |
|---|---|---|
| **1** — build checks for the four observed defects | Epic work; pre-qualified, mechanical | A milestone with room. The pattern exists here twice already (`test_starter_lint.py`, `test_steering_note_id_uniqueness.py`). |
| **2** — promote G1 and G2 into the core documents | **Constitutional amendment** | **Pull forward.** See below. |
| **3** — add an observability tier | Constitutional amendment | **Not now.** See below. |
| **4–5** — reduce exposition, then measure the reduction | Phase-scale question | A spine conversation, not an M38 one. Not P11 scope on current evidence. |

**Rec 2 is the pull-forward candidate.** G1 and G2 are general rules — neither is epic-specific —
currently **living in an epic spec**, restated with re-explained provenance in E38.6. Every new
epic must rediscover or re-cite them, and the M37 lineage that produced them is carried by
convention rather than by the normative tier. They are, by the issue's assessment, the
highest-value rules in the corpus and the most fragile. That combination is what makes them worth
moving ahead of the rest.

**Rec 3 should wait, and the reason is this project's own scar tissue.** Writing a normative
observability requirement before Drivr emits any telemetry would record a rule whose trigger
nothing produces — the exact defect of **P10-GH-7** (M35 recorded the handback rule with no
detector beneath it; still open, still High). The healthy pattern is already running: **E38.6
requires all four fields per-epic by its own spec.** That is the pilot. Codify after it produces
evidence, as default-accept went from practice to PSG §11.6 (P6-GH-10). Codifying first inverts
the order that worked.

**Required action:** HQ should place Rec 1 and Rec 2, and record Recs 3–5 as deferred with the
reasoning above, so neither is re-inherited as an open question of unknown status.

---

## Decisions Already Made

None by the CFO. The three routing questions were explicitly deferred to this chat; the
recommendations above await HQ.

---

## Carry-Over Open Items

1. **E38.2 is unaffected and should not be delayed.** It is the execution adapter surface plus the
   OpenCode adapter — the binding Stage-A gate that E38.3 onward depend on. Issue #192 concerns
   document structure, rule enforcement and telemetry; there is no overlap. Blocking a gate epic on
   an advisory review would be the costly error available here.
2. **The AOG section-numbering fix is a candidate for hotfix treatment** under the boundary already
   set in SN-28's ruling — *adds or corrects mechanically-checkable structure, changes no normative
   text.* Renumbering sections **does** change cross-references, so it likely fails that test and
   belongs in a milestone. Flagged for HQ to decide, not assumed either way.
3. **The count-error tally gains another entry** (the 27 / 26 discrepancy). Per the M38 correction,
   cite it by artifact and defect — issue #192, test-count row — never by ordinal.

---

## Next Action

HQ Chat should:

1. Record SN-30. **Do not delay E38.2** (Carry-Over 1).
2. Place **Rec 1** (checks) and **Rec 2** (promote G1/G2) into a milestone with room.
3. Record **Recs 3–5 as deferred**, with the P10-GH-7 reasoning attached to Rec 3, so their status
   is explicit rather than unknown.
4. Decide whether the AOG section-numbering fix clears SN-28's hotfix boundary (Carry-Over 2).
