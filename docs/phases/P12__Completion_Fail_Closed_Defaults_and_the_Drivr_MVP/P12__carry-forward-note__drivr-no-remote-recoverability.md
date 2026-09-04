---
project: ai-project-system
phase: P12
milestone: M45
type: note
status: open
issuer_chat: M45 Milestone Chat (ai-project-system)
issued_to: P12 Phase Chat
last_updated: 2026-09-03
severity: high
---

# Carry-Forward Note — Drivr has no git remote; P12-M45's Drivr changes are recoverable only from this disk

**Origin: the M45 Milestone Chat's Stage-2 review of E45.2 (PR #264), 2026-09-03.** Raised by the
E45.2 Epic Agent in its Delivery Notice, confirmed by the Milestone Chat by re-measure, and accepted
by the Phase Chat as **accept-now-and-record**: E45.2 is accepted and merged on its verified merits,
and this note records the recoverability gap separately so the merge does not carry it silently.

---

## The gap

**The Drivr repository (`~/soft-dev/drivr`) has no configured remote.** `git remote -v` is empty; its
only submodule (`.governance`) points *into* `ai-project-system` (`branch = v7.1.0`). Every change in
M45's E45.2, E45.3 and E45.4 lands in Drivr — outside `ai-project-system` and outside its suite — but
there is nowhere Drivr pushes to.

Consequence, measured at E45.2: the E45.2 code change (`17aef91` on Drivr's `epic/P12-M45-E45.2`,
branched from `f15e239`) exists **only on this disk**. The Delivery Notice in `ai-project-system`
(which *is* pushed and merged) records the ref, but no other machine can fetch that commit. If this
disk is lost, the milestone's actual work is unrecoverable while its record survives pointing at a
commit that no longer exists.

This is the set-1 lesson in a new shape: *"nothing of the record lives only on one disk — which is
worse."* The milestone branch itself was fixed (fast-forwarded and pushed); Drivr's side has no such
remedy, because there is no origin to push to.

---

## What is known

- **Drivr is a real git repo**, with `main` at `f15e239` and the E45.2 work on `epic/P12-M45-E45.2`
  at `17aef91`, committed and verified (suite 470 passed, measured on this host).
- **Drivr is deliberately outside `ai-project-system`** — the M45 milestone spec's External
  prerequisite names it as the landing site for E45.2–E45.4, and its verification is separate.
- **No Drivr remote, no Drivr origin, no `.gitmodules` entry in `ai-project-system`** pointing at
  Drivr. Drivr is not a submodule of `ai-project-system`; only its own `.governance` submodule points
  back the other way.
- **The `ai-project-system` record is intact** — every M45 Delivery Notice cites the Drivr ref, so the
  provenance is recorded; what is missing is a second copy of the Drivr commits themselves.

## Open question (owned by the P12 Phase Chat, not the Milestone Chat)

Is Drivr meant to be published? Three live possibilities, none decided here:

1. **Drivr gets its own remote** (its own GitHub repo), and `origin` is configured so each epic's
   Drivr branch is pushed and the milestone's work is recoverable off this disk.
2. **Drivr is intentionally local-only** — a coordination daemon with no published remote — in which
   case the `ai-project-system` Delivery Notice is the durable record and the disk is the only copy,
   accepted as a stated risk.
3. **Drivr is vendored into `ai-project-system`** (submodule or subtree) so its P12-M45 changes travel
   the governed path.

The Phase Chat resolves this; the Milestone Chat does not decide Drivr's publication model. Until it
is resolved, **every M45 epic (E45.2 done; E45.3, E45.4 ahead) lands in a repo whose commit exists
only on this disk**, and each Delivery Notice should keep flagging it as E45.2's did.

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-09-03 | Initial note, from E45.2's Stage-2 review (PR #264). Records that Drivr has no remote, that the E45.2 change (`17aef91`) is recoverable only from this disk, and that the Phase Chat owns the publication-model decision. E45.2 was accepted and merged on verified merits; this note is the separate record the accept-now-and-record decision requires. |
