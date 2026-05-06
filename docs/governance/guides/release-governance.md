# Release Governance and Promotion Policy

This guide defines when and how governance artifacts are promoted to release branches (including `master`/`main`) while phase execution is ongoing.

## Goals

- Allow safe, early adoption of vetted governance capabilities across projects
- Maintain clear quality bars (gates) prior to promotion
- Keep phase/milestone workstreams independent from release cadence

## Versioning

- Governance Version: MAJOR.MINOR.PATCH
  - MAJOR: Incompatible structural changes across phases (e.g., P2→P3)
  - MINOR: Milestone-level capabilities and guides (e.g., M8)
  - PATCH: Clarifications, doc fixes, non-breaking improvements

Examples:
- v0.8.0 — P2 Milestone 8 adoption architecture released
- v0.8.1 — Docs fixes, no behavior change

## Branching Model

- Ongoing work: `phase/P<n>` and `milestone/M<n>`
- Release branches: `release/v<MAJOR>.<MINOR>` (optional, for long-lived stabilization)
- Stable: `master` (or `main`) reflects the latest approved governance release

Promotion targets:
- From `phase/P<n>` (or `milestone/M<n>`) → `release/vX.Y` (optional) → `master`
- Direct `phase/P<n>` → `master` is allowed if gates pass and risk is low

## Release Gates (Minimum to Promote)

Before promoting to `master`, the following must be true for the scoped change:

1) Documentation
- HQ agent behavior and startup prompt documented and usable
- Onboarding/migration guide for legacy or ungoverned projects
- Governance upgrade workflow with validation and rollback steps

2) Validation
- End-to-end validation executed on at least one supported platform (Linux minimum)
- Test plan, steps, and results documented with known issues and mitigations

3) Hygiene
- Branches consolidated at the milestone level (epics merged into the milestone branch)
- Clear, reproducible instructions to adopt/rollback in projects

4) Authorization
- Delivery Authorization granted for the promotion scope
- Human review completed on the consolidation/release PR

If all four categories are satisfied, promotion to `master` is permitted.

## Release Types

- Preview Release: Meets all gates, but with documented limitations; recommended for new/greenfield projects and opt-in adopters
- Release Candidate (RC): Preview + broader cross-platform validation; limited freeze window
- Stable: RC accepted; promoted to `master`; recommended default

## Minimal Completion Level that Deserves "Release"

The minimal level is the completion of a Milestone whose scope includes:
- Adoption architecture (how to use it)
- Migration path (how to get there from legacy)
- Upgrade workflow (how to evolve safely)
- Validated end-to-end flow on at least one platform

Milestone M8 satisfies these and therefore qualifies for a Preview Release (v0.8.0) to `master`, even while Phase 2 continues.

## Promotion Workflow (Example for M8)

1) Ensure consolidation: `milestone/M8` → `phase/P2`
2) Tag and (optionally) branch for release:
   - Tag: `v0.8.0`
   - Optional branch: `release/v0.8`
3) Create PR to promote governance docs/templates and any tooling to `master`:
   - Base: `master`
   - Head: `phase/P2` (or `release/v0.8` if used)
   - Title: "Release v0.8.0 — Adoption Architecture and Multi-Project Support"
   - Body: Include gate evidence (docs, validation, completion notice) and known issues
4) Human review and Delivery Authorization for release scope
5) Merge PR; announce availability and recommended usage scope (Preview)

## Rollout Guidance

- New projects: Adopt latest `master` (Preview allowed)
- Ongoing projects: Opt-in via governance manifest/version pin; follow migration and upgrade guides
- Backports: If necessary, cherry-pick doc/tooling fixes to `release/vX.Y` branches; retag PATCH versions

## Reversibility

- Each release must include explicit rollback steps in the upgrade workflow
- If needed, revert the `master` promotion commit and document the reversion

## Audit and Communication

- Each promotion includes a Delivery Authorization record and links to validation artifacts
- Execution chats use the standardized "Awaiting Delivery Authorization" templates to communicate status up the chain
