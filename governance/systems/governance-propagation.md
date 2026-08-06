---
type: system
status: active
version: 1.0.0
---

# Governance Propagation Model

## Authority Declaration

This repository (`ai-project-system`) is the **authoritative source** for all governance rules, models, and resolutions related to the AI Project System. All governance adopted by other projects must reference this repository explicitly.

## Reference-Based Adoption

Governance does **not** propagate automatically or implicitly. Projects wishing to adopt AI Project System governance must do so by reference, using the provided template (`governance/templates/governance-source.md`).

- Adoption is explicit and intentional
- Projects must declare their governance source in their own repository
- No implicit or automatic inheritance is permitted

## Propagation Model

1. **Authoritative Source:** This repository is the single source of truth for governance.
2. **Adoption by Reference:** Other projects must include a `governance-source.md` file referencing this repository.
3. **Manual Enforcement:** Governance is enforced through manual review and reference, not automation.

## Constraints

- HQ chats and related tools **do not** have live access to GitHub repositories
- No automatic synchronization or polling is possible
- All governance enforcement is by reference and manual review

## Non-Goals

- No CLI or automation tooling
- No automatic or live governance syncing
- No changes to existing governance rules

## Adoption Template

Projects must use the template in `governance/templates/governance-source.md` to declare their governance source.

---

For questions or clarifications, refer to the Epic E3.1 spec or contact the maintainers of this repository.

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-08-05 | **Versioning convention adopted** (HQ Ruling 2026-08-04, P10-GH-8; applied by E37.1, P11-M37). This document previously carried neither a `version` field nor a `## Changelog` section. **This is its first recorded row, and no prior history is reconstructed** — for changes before this date, see `git log -- governance/systems/governance-propagation.md`. |
