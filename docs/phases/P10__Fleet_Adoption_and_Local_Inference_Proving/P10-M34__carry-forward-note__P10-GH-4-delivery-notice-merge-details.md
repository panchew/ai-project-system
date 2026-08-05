---
project: ai-project-system
phase: P10
milestone: M34
type: note
status: active
issuer_chat: Milestone Chat (P10-M34)
issued_to: Phase Chat (P10)
last_updated: 2026-07-29
---

# Carry-Forward Note — P10-GH-4: `delivery_notice.merge_details` is a structurally unfillable field

**Recorded, not fixed.** This is a framework *capability* observation, which M34's Non-Goals place
outside its adoption epics ("no framework capability on spec"). It is filed here so the Phase Chat
can carry it to HQ or a later phase, and it will be restated in the M34 Milestone Closure
Declaration.

**Origin:** surfaced during Stage-2 review of E34.3 (2026-07-29), when its delivery notice was
re-opened after merge and still read `merge_commit: <pending>`. The initial suspicion — that E34.3's
notice was stale — was **wrong**, and checking that is what found the real gap.

---

## The finding

`governance/templates/delivery-notice.md` requires a `merge_details` block:

```yaml
merge_details:
  pr_number: <PR_number>
  pr_url: <PR_GitHub_URL>
  merge_commit: <commit_hash>
  merge_timestamp: <ISO-8601 UTC>
  merge_strategy: squash|rebase|merge
  target_branch: <target_branch>
```

Three of those six fields — `merge_commit`, `merge_timestamp`, and (usually) `merge_strategy` —
**cannot be known when the artifact is authored.** The canonical happy path puts Delivery Notice
production at **step 2** and the merge at **step 6**:

| Step | Act |
|---|---|
| 1 | Execution completed |
| **2** | **Epic Delivery Notice produced** ← the fields must be filled here |
| 3–5 | Parent-chat review · acceptance · human merge authorization |
| **6** | **PR merged** ← the fields' values first exist here |

Nothing in the process returns to step 2. The template gives no "complete after merge" instruction
and defines no `<pending>` convention, so every Epic Chat invents a placeholder independently.

## Evidence (repo-wide, measured 2026-07-29 on `milestone/M34`)

- **15** git-tracked delivery notices carry a `merge_commit:` field.
- **1** has a real commit hash. **14 are placeholders.**
- The 14 include **all four M33 epic notices** — a milestone that is *fully closed and consolidated*.
  So this is settled framework practice, not drift, and not any one epic's defect.
- The sole filled case is instructive rather than contradictory:
  `.ai-project/artifacts/delivery-notices/2026-07-13T16_50_00Z__B4.1__delivery_notice.md` records
  `pr_number: none (direct merge, no PR)` and was authored **by HQ Chat after the merge had already
  happened** (`merge_commit: b46d7be`). The field is fillable exactly when the notice is written
  post-merge — which the Epic happy path structurally forbids.

## Why it is worth fixing rather than tolerating

A reader holding only a delivery notice cannot tell whether the epic ever merged, and the artifact
*appears* to answer that question. That is worse than omitting it: a placeholder in a field the
template presents as factual invites a reader to conclude "not merged." The framework's own standard
is that every claim be confirmable from committed evidence; here the record silently under-reports a
fact that git holds.

The cost of tolerating it is currently absorbed by the Milestone Closure Declaration, which restates
merge SHAs — so the information is not lost, it is just not where the template points.

## Candidate directions (for whoever scopes it — not decided here)

1. **Drop the three post-merge fields from the template** and let the Milestone Closure Declaration
   remain the single place merge facts are recorded. Cheapest; removes a field that has never worked.
2. **Split the block** into author-time facts (`pr_number`, `pr_url`, `target_branch`) and an
   explicitly optional post-merge addendum, with a documented `<pending>` convention so the
   placeholder stops being ad-hoc.
3. **Assign completion to the merging party.** Whoever performs the merge (parent chat, post-
   authorization) fills the three fields. Most faithful to the template's apparent intent, and the
   most process weight — it adds a write-back step to a lifecycle that currently ends cleanly at
   merge.

**No recommendation is made from this level.** The choice trades record fidelity against process
weight, which is a framework-design judgment above a Milestone Chat's adjacency.

## Explicitly not done here

- No template edit, no notice edited retroactively, no `<pending>` convention introduced.
- E34.3's notice is **left exactly as delivered** — it matches 14/15 precedent and correcting it
  alone would make the corpus *less* consistent, not more.
- No renumbering or reinterpretation of P10-GH-1 (`framework_version` unschema'd), **P10-GH-2**
  (Creation Chat Seed does not implement the E31.3 verification), or **P10-GH-3** (policy row P1
  contradicts the live config). This is **P10-GH-4**, the next free identifier.

  > **Amendment 2026-08-04 (P11-M36-E36.5) — the parenthetical gloss of P10-GH-2 above restates a
  > false premise.** The original text is left unedited, deliberately. `governance/templates/seed.md`
  > has carried the E31.3 check since **`d7ee7cd` (2026-07-19)**, nine days before the ruling that
  > filed the gap. The real defect was `creation-chat-guide.md`'s re-instantiation ritual, and
  > **E36.3 (merged `d8f4871`) has closed it.** Per **SN-26** (Required action 1) and **HQ Ruling
  > 2026-08-01, Decision 8**.
  >
  > **This amendment corrects the gloss only.** It renumbers nothing, reopens nothing, and leaves
  > this note's P10-GH-4 subject matter entirely untouched.
