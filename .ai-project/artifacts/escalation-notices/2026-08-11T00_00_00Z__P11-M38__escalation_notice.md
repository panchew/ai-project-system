---
type: escalation-notice
milestone: M38
epic: E38.3
issued_by: Epic Chat (P11-M38-E38.3)
issued_to: Milestone Chat (P11-M38)
date: 2026-08-11
status: open
---

# Escalation Notice: the framework's own enrollment tool produces §4-invalid configs, and §4 has no rule for the fields it writes

## Summary

E38.3 built the first thing that enforces `governance/ai-project-yml-spec.md` §4
(`bin/ai-project-validate`, `P10-GH-5`) and ran it against the real fleet. **Three findings are
outside this Epic's authority to act on and are escalated rather than fixed.** All three were left
exactly as found.

**Nothing in this notice was repaired.** No enrolled project was modified, `bin/ai-project-init` was
not touched, and no agent was re-installed. That is the deliberate posture, not an omission.

---

## Escalation 1 — `bin/ai-project-init` generates configs that §4 calls invalid, and it is the direct cause of the fleet's invalidity

**Measured 2026-08-11, `ai-project-system` @ `epic/P11-M38-E38.3`.**

`create_ai_project_yml()` (`bin/ai-project-init:249-268`) writes exactly five fields:

| §4 requirement | init writes it? | Result |
|---|---|---|
| `governance.source` (rules 3, 4) | yes | ✅ |
| `governance.version` (rules 3, 5) | yes | ✅ |
| **`governance.ref`** (rules 3, **6**) | **no** | ❌ **invalid** |
| `project.name` (rules 3, 7) | yes | ✅ |
| **`project.description`** (rules 3, **8**) | **no** | ❌ **invalid** |
| `project.created_at` | yes | **not in the schema at all** |
| `governance.submodule_path` | yes | **not in the schema at all** |

**And there are two validators in this framework enforcing different contracts.**
`validate_ai_project_yml_content()` (`bin/ai-project-init:107-115`) requires `project`, `governance`,
`name`, `created_at`, `source`, `version`. **It enforces `created_at`, which the schema does not
define, and does not enforce `ref` or `description`, which the schema requires.** The contract that
is written down is not the contract that is enforced.

**This is not a latent defect. It is the direct cause of every §4 failure in the fleet:**

| Project | §4 errors | Traceable to `init`? |
|---|---|---|
| `ai-project-system-mcp` | `project.description` absent | **yes** |
| `courtis` | `project.description` absent | **yes** |
| `home_finance` | `project.description` absent; `project.name` fails rule 7 | **description: yes**; name: no |
| `social-stories-creator` | `governance.ref` absent; `project.description` absent; `governance.version` unquoted; `governance.version` not bare semver | **yes, all four** |

**4 of 13 enrolled configs are §4-invalid, carrying 8 errors between them.** Seven of those eight
are init's.

> **`social-stories-creator`'s two rule-5 errors are also init's**, by a mechanism worth naming:
> init takes a **single** `--governance-version` argument and feeds it to **both** `governance.version`
> and the submodule git ref — two things the schema deliberately separates. A tag name (`v7.0.0`) is
> correct for the ref and wrong for the version, which rule 5 requires to be a quoted bare semver.
> E38.1 hit this and corrected it by hand in Drivr; `social-stories-creator` did not.

**Drivr's outcome, verified against the delivered repository rather than taken from its spec:**
E38.1's spec was amended to v1.1.0 on this finding and required four post-init additions plus one
correction and a §4 self-check. **It delivered them. `bin/ai-project-validate` reports Drivr
§4-VALID — 0 errors, 2 warnings — at Drivr HEAD `31dad51`, 2026-08-11.** The collision resolved the
good way. **The tool that created it is still broken**, and the next project enrolled through it will
be born invalid the same way.

**Not fixed here** — `bin/ai-project-init` is out of scope by the Epic Spec's §Non-Goals. **Also
recorded, not fixed:** init hard-codes the submodule path as `governance` and exposes no flag for it,
which is why the two projects still at `governance/` rather than the fleet's `.governance` convention
are exactly the init-created ones.

> **Correcting a figure this Epic inherited rather than measured.** Drivr's `.ai-project.yml` comment
> (E38.1, 2026-08-10) records init as hard-coding the path *"at :262, :294 and :298"* — **three**
> sites. Measured directly on `bin/ai-project-init` at `epic/P11-M38-E38.3`, 2026-08-11, it is
> **eight**: line **262** (`submodule_path: governance/` in the emitted config) plus **274, 281, 283,
> 286, 289, 294, 298** in `add_governance_submodule()` — the `git submodule add` path argument, two
> `git clone` targets, two `git -C` working directories, the `--force` re-add, and the `.gitmodules`
> section key. The figure is corrected because it changes the size of the fix, not because the
> underlying finding was wrong. **This is a count taken from an artifact instead of from the
> source**, in an Epic whose own subject is that a count is only as good as the pattern behind it.

---

## Escalation 2 — §4 has no rule for unknown keys outside its three optional blocks, and three live fields fall in that gap

**§4's unknown-key rules are 11, 16 and 22, and they cover only `overrides`, `models` and
`visual_artifacts`. There is no rule at all for unknown keys at the top level or inside
`governance:` and `project:`.** A validator meeting `created_at` therefore has **no §4 instruction** —
error, warn and ignore are all equally unsupported by the text.

**The schema-drift class, measured strict-form 2026-08-11 across 13 enrolled projects:**

| Field | In configs | Occurrences in the yml-spec (before this Epic) | Written by `init`? | Disposition |
|---|---|---|---|---|
| `framework_version` | **7 of 13** | **0** | no | **BLESSED** — §3.6 + rule 26, optional (`P10-GH-1`, decided by the Phase Chat) |
| `created_at` | **5 of 13** | **0** | **yes** | **NOT blessed. Escalated.** |
| `submodule_path` | **5 of 13** | **0** | **yes** | **NOT blessed. Escalated.** |
| `cfo_review_gate` | **2 of 13** | **1 — a prose aside in §3.5, never a schema entry** | no | **NOT blessed. Escalated.** |

**What E38.3 did:** `bin/ai-project-validate` **warns** on unknown keys wherever §4 is silent, and
reports those findings with **no rule number** so the treatment can never be mistaken for §4
enforcement. The reasoning: warning is the only treatment this document evidences anywhere — all
three of its unknown-key rules choose it, both times for the same stated purpose (forward
compatibility, §3.3 and §3.5) — and warning keeps the drift **visible** without declaring configs
invalid on a rule the spec never wrote.

**What E38.3 deliberately did not do:** write that treatment into §4. **Filling a normative silence
by fiat is a larger change than this Epic was authorized to make**, and the Epic Spec is explicit
that widening the fold-in beyond `framework_version` is not the Epic's to take. §4 now carries a note
**recording** the gap and pointing at the reference implementation's behaviour, marked as escalated
rather than settled.

**Two rulings are wanted:**

1. **Does §4 gain a general unknown-key rule**, and is it warn (consistent with 11/16/22) or error?
2. **Do `created_at`, `submodule_path` and `cfo_review_gate` warrant schema entries of their own?**
   E38.3's recommendation, offered as a recommendation: **`created_at` and `submodule_path` should be
   decided together with Escalation 1**, because `init` writes both and the right fix may be to stop
   writing them rather than to bless them. **`cfo_review_gate` is a different case** — it is a real,
   documented capability with a prose description already in §3.5 and two live users, and it reads as
   a straightforward schema entry that was simply never made.

---

## Escalation 3 — a measurement in this Epic's own spec was taken at the wrong layer

**Not a defect in the fleet. A defect in how the fleet was measured, filed because `P11-GH-2` is the
carry-forward it belongs to and because it happened inside the Epic whose own subject is that a count
is only as good as the pattern behind it.**

The E38.3 spec's Finding 6 (v1.2.0, 2026-08-11) recorded the installed `governance.agent.md` as
**"canonical ×10, stub ×1, absent ×2."** Re-measured exhaustively — every `governance.agent.md` at
any depth in every project, rather than the single `.ai-project/agents/` path — **it does not hold:**

- **`fieldledger-assesment` is not absent.** It carries a **14,352 B** copy at
  `.governance/governance/agents/` — the pre-v7.0.0 canonical, consistent with its submodule being
  pinned at **v5.1.0**. It is **stale, not missing**, and the "not expected" flag attached to its
  absence was attached to something that is not the case.
- **There is a fourth state: STALE.** 14,352 B is an older canonical — neither the 230 B stub nor
  absent. A three-value axis cannot represent it.
- **`footboard` holds two states at once** — 14,711 B at its two live paths and a stale 14,352 B
  leftover at `.github/agents/`. A single per-project value cannot represent it.
- **`social-stories-creator`'s stub is only its INSTALLED copy.** The canonical 14,711 B file is
  present and correct inside its own submodule at `governance/governance/agents/`. So the
  characterisation that it "survived only because it was never rolled forward" does not fit either:
  **its submodule is pinned at v7.0.0, the same commit `8044451` as six other projects.** It *was*
  rolled forward. **The install was not.**
- **Only `character-factory` has no `governance.agent.md` anywhere at any depth**, consistent with
  never having been enrolled.

**Cause:** the measurement looked at one install path; the fleet uses more than one. That is
`P11-GH-2`'s named failure — verification performed at the wrong layer — and it is the fourth
distinct axis that carry-forward has now collected, after repository, method and time.

**Nothing was repaired.** No agent re-installed, no submodule moved, no stale copy deleted. The
registry's `installed_agent` field carries four states (`canonical` / `stale` / `stub` / `absent`)
plus `native` and `not_applicable`, and records the two-copy cases in a note.

---

## A fourth item, reported but not escalated for a ruling

**The two governing documents render the CFO's three state definitions differently**, and both claim
the text is verbatim. The Epic Spec's §Scope-1 table reads *"Not planned to ever be touched again —
though it can be brought back to life"*; the Epic Execution Chat Starter's inline parenthetical reads
*"though it can be brought back"*, and omits *"Enrolled in the registry."* from `Active`. **The
starter outranks the spec** in the governance hierarchy.

The registry reproduces the **spec's table form**, on the reading that the starter's parenthetical is
a compression of it, and **records the discrepancy in the file itself** rather than picking one
silently. Raised here because this milestone's lineage spent two milestones on citation integrity;
**it needs a correction to one document, not a ruling.**

---

## What the Milestone Chat is asked for

| # | Item | Ask |
|---|---|---|
| 1 | `bin/ai-project-init` produces §4-invalid configs; two validators, different contracts | **Route it.** A bugfix epic is the obvious shape; the blast radius is every future enrollment. |
| 2 | §4's unknown-key gap; three unblessed drift fields | **A ruling**, or an explicit park. E38.3's recommendation is in Escalation 2 and is a recommendation only. |
| 3 | Finding 6's measurement layer | **Note it against `P11-GH-2`.** Nothing to fix; the corrected measurement is in the registry. |
| 4 | The two renderings of the CFO's state definitions | **A correction to one document.** No ruling needed. |

**None of the four blocks E38.3's delivery.**
