---
artifact_type: protocol_correction
artifact_version: 2.0
timestamp: 2026-08-14T20:30:00Z
issuer_chat: Epic Agent (P11-M38-E38.6)
issuer_role: Epic Agent
status: pre-registered
epic_id: P11-M38-E38.6
milestone_id: P11-M38
phase_id: P11
project_name: ai-project-system
governs: Review Decision 2026-08-14T20:22:53Z (REJECT, action: rework) — re-review 01
supersedes: protocol-correction-addendum.md v1.0 (2026-08-14T19:30:00Z — see erratum)
---

# Protocol-Correction Addendum v2 — E38.6 re-review 01 resubmission

**This addendum is committed BEFORE paid run 3.** It is the pre-registered authorization
for one paid replacement run, per Review Decision `2026-08-14T20:22:53Z` (Finding 1). Git
history proves it precedes run 3. The **original rubric and prompt are frozen** — neither is
edited.

## 1. Paid run 2 is a protocol-invalid trial

**Paid run 2 is identified as a protocol-invalid trial — not a scored arm and not a
candidate result.** It violated the frozen conditions on **two** grounds (Finding 1):

1. **Session-type mismatch:** it was a `claude-code fresh subagent context
   (operator-dispatched)` — programmatically dispatched — not the frozen *manual* session
   at `models.epic_manual`.
2. **Unenforced access boundary:** repository isolation was **instructed, not sandboxed**;
   the host process retained tool access capable of reading beyond the packet.

Its output may remain as useful evidence of an interesting result, but it is a second
protocol-invalid paid trial and is **not** the paid CATCH in the controlled pair. It is
preserved at `runs/paid/paid-arm-run-2-output.md` and `paid-arm-run-2-meta.json`.

## 2. Authorization for exactly one paid run 3

**Exactly one replacement paid run is authorized, solely because paid run 2 violated frozen
conditions.** Its frozen conditions:

- **genuinely fresh, human-operated manual chat** at `models.epic_manual`
  (`remote:claude-opus-5`);
- **no inherited conversation** — a brand-new session;
- **no local-repository connector, no shell, no filesystem/search tool** — no way to read
  anything except the prompt;
- **no context other than the exact sealed packet** (the 42,875-byte input, MD5
  `450dcfb78800f13ff39cabf4bcf1907f`, committed at `runs/paid/sealed-input-run-3.txt`);
- **no evaluator follow-up, no clarification, no re-prompting**;
- the **original rubric unchanged**.

## 3. The sealed input, committed before run 3

The exact sealed packet input is committed as a durable evidence file
(`runs/paid/sealed-input-run-3.txt`) **before run 3**, with its byte count (42,875) and MD5
(`450dcfb78800f13ff39cabf4bcf1907f`) recorded. It is byte-for-byte identical to the input
the reviewer independently recovered for run 2. Committing it makes the prompt boundary and
the absence of the answer verifiable after temporary files disappear.

The prompt is exactly the bytes after the `<!-- PROMPT-BEGIN -->` marker; the audit header
that states the answer is **not** included in the sealed input.

## 4. No best-of-N, no prompt tuning, no suppression

All three paid attempts stay in the record. Run 3 is not selected *as better* than an
invalid trial — it is the only valid paid arm, and runs 1 and 2 are retained as
protocol-failure records. No prompt is tuned, no packet is edited, no output is selected by
quality.

## 5. Execution

The operator pastes the exact sealed input into one fresh manual session and makes no
follow-up intervention. The exact output/transcript, model identity evidence, start/end
timestamps, and elapsed wall-clock time are captured and committed.

If the required manual, packet-only conditions cannot be provided, this Epic escalates
instead of substituting another execution mode (per the review's instruction).

## 6. Ordering

This addendum and the sealed input are committed **before** run 3. Local run 2 is **not**
rerun. The comparison is recomputed using local run 2 and paid run 3.
