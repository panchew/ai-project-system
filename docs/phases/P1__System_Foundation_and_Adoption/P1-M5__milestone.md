---
project: ai-project-system
phase: P1
milestone: M5
type: milestone
status: fully_closed
last_updated: 2026-04-18
---

# Milestone M5 — System Refinement from Real Usage

## Purpose

Milestone M5 addresses system improvements and refinements identified through real-world usage and dogfooding of the AI Project System.

This milestone focuses on **closing workflow gaps** and **improving ergonomics** based on practical experience, not theoretical design.

---

## Problem Statement

While Phase P1 has successfully established a stable, adoption-ready system (M1-M4 complete), real-world usage has revealed workflow gaps:

- **Unplanned creative work:** During execution, humans and AI encounter ideas, improvements, and opportunities that don't fit current Epic scope
- **No capture mechanism:** Current system lacks a canonical way to preserve this work without breaking execution discipline
- **Working outside governance:** Users resort to ungoverned work to capture insights, creating drift from the system
- **Lost insights:** Valuable observations and improvements are lost or forgotten between Epics

These gaps don't invalidate the system, but they create friction that can be resolved through targeted refinements.

---

## Goals

By the end of Milestone M5, the system should:

1. Provide a canonical mechanism for capturing unplanned work without breaking execution discipline
2. Enable creativity and exploration while preserving structured execution
3. Create feedback loops from execution → planning
4. Allow users to work within governance even for exploratory work
5. Address any other high-impact refinements identified through dogfooding

---

## Non-Goals

Milestone M5 explicitly does **not** aim to:

- Redesign the Phase-Milestone-Epic model
- Add automation tooling (CLI, web apps, bots)
- Change fundamental governance principles
- Address speculative improvements (only real usage-driven refinements)
- Expand system scope beyond current charter

---

## Planned Epics

### **E5.1 — Unplanned Progress Branch Model**

Formalize the "unplanned progress branches" model for capturing exploratory work:
- Define `unplanned/*` branch naming convention
- Update PROJECT-SYSTEM-GUIDELINES.md with lifecycle and rules
- Update AI-OPERATING-GUIDELINES.md with HQ planning behavior
- Document integration process (Epic spec decides strategy)
- Optionally dogfood with example unplanned branch

**Goal:** Users can capture creative work within governance, no more "working outside the system."

---

### **Future Epics (TBD)**

Additional refinements may be added to M5 as dogfooding continues:
- Epic Delivery Notes formalization (if distinct from unplanned branches)
- Other high-impact ergonomic improvements
- Clarifications or simplifications identified through usage

Epics will be added incrementally based on real needs, not speculatively.

---

## Completion Criteria

Milestone M5 is considered complete when:

- All planned Epics are completed and accepted
- Unplanned progress branch model is formally governed and usable
- Users can work within governance for both structured execution and exploratory work
- No additional high-priority refinements are identified (or all identified refinements are addressed)

---

## Dependencies

- ✅ **M1 complete** (stable governance foundation)
- ✅ **M2 complete** (execution ergonomics baseline)
- ✅ **M3 complete** (governance propagation defined)
- ✅ **M4 complete** (adoption readiness achieved)

M5 builds on stable system foundation from M1-M4.

---

## Notes

This milestone is intentionally **reactive, not proactive**:
- Epics are driven by real usage friction, not theoretical improvements
- New Epics may be added as dogfooding reveals needs
- Completion is based on "no more high-priority gaps" not a fixed Epic count

M5 prioritizes **practical usability refinements** over feature expansion.

---

## Success Metrics

After M5 completion:
- Users report working within governance for all work (including exploratory)
- Unplanned branch model is used successfully across projects
- No major workflow gaps remain unaddressed