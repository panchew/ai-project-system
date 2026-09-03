---
type: system
status: active
version: 1.1.0
---

# Governance Propagation Model

## Authority Declaration

This repository (`ai-project-system`) is the **authoritative source** for all governance rules, models, and resolutions related to the AI Project System. All governance adopted by other projects must reference this repository explicitly.

## Reference-Based Adoption

Governance does **not** propagate automatically or implicitly. Projects wishing to adopt AI Project System governance must do so by reference, using the provided template (`governance/templates/governance-source.md`).

**Why this survives (Decision 7, 2026-08-19 opening ruling):** not because automatic propagation is
impossible — it is not — but because **adoption must be a project's own recorded decision.** Silent
inheritance would change a project's ruleset without any artifact in that project saying so — the
fail-open disposition applied to governance itself.

- Adoption is explicit and intentional
- Projects must declare their governance source in their own repository
- No implicit or automatic inheritance is permitted

## Language Policy (i18n)

Chat and output proceed in the user's language; documentation remains in the original language;
**English is authoritative**; translation on demand is a **view, never the source** — a
Spanish-speaking adopter therefore interacts in Spanish while the English documentation is
propagated as-is, and any translation is derived from it, never a competing source (SN-31
Carry-Over 10, decided).

## Propagation Model

1. **Authoritative Source:** This repository is the single source of truth for governance.
2. **Adoption by Reference:** Other projects must include a `governance-source.md` file referencing this repository.
3. ~~**Manual Enforcement:** Governance is enforced through manual review and reference, not
   automation.~~ **Struck (Decision 7, "Manual Enforcement… not automation")** — replaced by:
   **Automated checks do not confer acceptance.** Governance enforcement by automation is routine in
   this corpus — `test_starter_lint.py`, `test_steering_note_id_uniqueness.py`, the yml validator —
   but a passing check is **evidence, not acceptance**: a human or a governed parent still accepts.

## Constraints

**Struck (Decision 7, 2026-08-19 opening ruling) — replaced by a dated factual capability statement:**
- ~~HQ chats and related tools **do not** have live access to GitHub repositories~~
- ~~No automatic synchronization or polling is possible~~

**Current capability, as of 2026-09-03:** this repository is operated through `gh` daily — its
chats and tools **do** have live access to GitHub repositories; B2.1 (P11-M37) gave the sandbox
reachability to the host; and **Drivr is a scheduler**. Automatic synchronization and polling are
therefore possible and, where authorized, used.

**Re-check on versioning:** a Constraints section that carries a technical claim is **re-checked
whenever this document is versioned** — the claim verified once and never re-checked is the error
class `P11-GH-2`'s time axis records.

**Struck (Decision 7, "Manual Enforcement… not automation" clause):**
- ~~All governance enforcement is by reference and manual review~~

This was the "Manual Enforcement" claim in Constraint form; the narrower true statement that
replaces it is stated in the Propagation Model above: **automated checks do not confer
acceptance** — a passing check is evidence, and a human or a governed parent still accepts.

## Non-Goals

**Struck (Decision 7, 2026-08-19 opening ruling):**
- ~~No CLI or automation tooling~~

`bin/` exists, is documented in the AOG and three guides, and is instructed to adopters; the
Non-Goal was false when P6 shipped `ai-project-init` and has been false ever since.

**Survives, re-scoped (Decision 7) — a reason is recorded with it:**
- **No automatic or live governance syncing** — this does **not** describe an impossibility; it
  records that **no such mechanism is authorized today**. A future proposal is measured against an
  authorization question it can actually answer, not against a capability claim that is simply
  wrong. (The updater/reconciler is split and deferred — Decision 8 of the same ruling.)

**Unchanged — not governed by Decision 7's table (mapped, not silently dropped):**
- **No changes to existing governance rules** — a scope Non-Goal inherited from the originating epic
  (E3.1), not a technical-capability claim and not an automation-premise prohibition; Decision 7's
  table does not rule it, and this epic does not re-decide what the ruling left unruled.

## Adoption Template

Projects must use the template in `governance/templates/governance-source.md` to declare their governance source.

---

For questions or clarifications, refer to the Epic E3.1 spec or contact the maintainers of this repository.

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.1.0 | 2026-09-03 | **Amended per Decision 7 of the 2026-08-19 opening ruling (E44.5, P12-M44).** Both Constraints struck and replaced by a **dated** factual capability statement (as of 2026-09-03: `gh` daily, sandbox reachability via B2.1, Drivr a scheduler) plus the rule that a Constraints section carrying a technical claim is re-checked whenever the document is versioned. The third Constraint line (*"All governance enforcement is by reference and manual review"*) struck under Decision 7's *"Manual Enforcement… not automation"* clause, replaced by *automated checks do not confer acceptance* (Propagation Model item 3). *"Governance does not propagate automatically or implicitly"* survives on a new reason — adoption must be a project's own recorded decision. Non-Goal *"No CLI or automation tooling"* struck. Non-Goal *"No automatic or live governance syncing"* survives, re-scoped to *not authorized today*. Each survivor carries its own reason; each struck statement is recorded as struck. The i18n policy paragraph (SN-31 Carry-Over 10) added as §Language Policy, one paragraph. |
| 1.0.0 | 2026-08-05 | **Versioning convention adopted** (HQ Ruling 2026-08-04, P10-GH-8; applied by E37.1, P11-M37). This document previously carried neither a `version` field nor a `## Changelog` section. **This is its first recorded row, and no prior history is reconstructed** — for changes before this date, see `git log -- governance/systems/governance-propagation.md`. |
