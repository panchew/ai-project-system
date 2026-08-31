---
type: hq_ruling
concern_id: enforcement declaration timing (CFO); SN-42 milestone shape (CFO preference)
amends_in_part:
  - .ai-project/artifacts/rulings/2026-08-27__ai-project-system-hq__ruling__sn40-46-baseline-lineup-and-the-switching-ratchet.md
issued_by: HQ Chat (ai-project-system), scribing two CFO decisions
issued_to: Layer-8/CFO (mandatory diff reviewer, PSG §11.6.1); the P12 Phase Chat
phase: P12
date: 2026-08-27
status: active
blocking_resolved: true
---

# HQ Ruling — Enforcement Is Declared and DEFERRED TO P12's CLOSE; SN-42 Extends M47 by Preference

**Prerequisite verification (P9-M31-E31.3):** harness `claude-opus-5` vs `models.hq:
remote:claude-opus-5` — **match.** `models.hq` is unchanged, which is the only reason this session is
able to write this ruling; see Decision 1.

**HQ scribes; it does not decide.** Both are the CFO's, taken 2026-08-27.

---

## Decision 1 — Enforcement is DECLARED, and takes effect at P12's closure, not now

**The CFO's decision:** *"Let's enforce only when the Phase is over to avoid halting any chat."*

**`model_verification` stays `advisory` for the remainder of P12 and flips to `blocking` as part of
P12's closure.** SN-37's model-qualification gate and HQ's suspended fidelity condition **resume at the
same moment**, automatically.

### Why the deferral is the substantive part, not a delay

**Enforcing today would halt the Phase Chat and the Milestone Chats mid-execution.** They run as Claude
sessions; the baseline configures `phase: remote:gpt-5.6-sol` and `milestone: remote:deepseek-v4-pro`.
Under `blocking`, each stops at its next prerequisite check. **HQ and Creation are unaffected — both
are `remote:claude-opus-5`** — which is a fact worth stating plainly, because *the one level that
would not have been halted is the level that would have thrown the switch.*

**HQ had raised a second objection and withdrew most of it before the CFO decided.** The
2026-08-27 ruling held that arming a fail-closed check against unmeasured fidelity is worse than not
arming it. **Since then delivery was proven and the single observed failure was a model normalizing a
mangled filesystem path.** A token like `gpt-5.6-sol` is short and unlikely to be normalized. **The
fidelity risk for model names is materially smaller than that ruling implied, and HQ said so rather
than letting an objection stand on inherited weight.** The decision therefore rests on the halt, which
is concrete, rather than on a risk HQ had overstated.

### The deferral has an EVENT trigger and a place that cannot lose it

**This phase has twice recorded a deferral failing because its trigger was a session's continued
existence** — once inside four hours. **P12's closure is an event, not a survival.**

**And it is placed where the phase cannot close around it:** a new **acceptance criterion** in the
phase spec (v1.3.0), so **P12 may not close without disposing of it — flip it, or record why not.**
That uses the backstop the Phase Chat already adopted: *the Phase Completion Declaration is the one
artifact guaranteed to be written while the phase is still open.*

**What the deferral does NOT do:** it does not reopen the ratchet question, weaken the honesty clause,
or make the advisory default permanent. **The ratchet stays broken for the rest of P12** — a lineup
change remains one PR rather than a six-surface edit — **which is the productivity property the CFO
bought and is deliberately not being handed back early.**

---

## Decision 2 — SN-42 extends M47 by preference; a new milestone is a justified escalation

**The CFO's decision:** *"Better if avoid an additional milestone, but let's do it if justified."*

**So the Phase Chat's default is to extend M47.** An eighth milestone remains available and is **an
escalation it must justify — not a free choice, and not forbidden.** **The bar is the work's actual
size, not tidiness.**

**HQ notes the asymmetry, because a preference can quietly become a prohibition:** if remote agentic
dispatch turns out to be milestone-sized and is compressed into M47 to honour a preference, **the
result is M47 carrying two objectives and failing to prove either.** **The CFO's word is "justified,"
not "no" — and the Phase Chat should read it as a bar to clear rather than a door that is closed.**

**Unchanged:** the objective's placement in P12 (HQ ruling, 2026-08-27), and **M47's acceptance
criterion that the proof run be checked by `bin/successful-nothing-instrument`** — which applies to a
remote engine exactly as it did to a local one. *A dispatch lane that cannot tell a finished run from
a silent nothing is the completion-signal problem P12 already owns, and a new engine class does not
exempt it.*

---

## Disposition

**Both decisions recorded with their consequences rather than merely their content.** Phase spec →
**v1.3.0**: one acceptance criterion (the enforcement flip at closure) and one scope note (SN-42
extends M47 by preference).

**`blocking_resolved: true`** — nothing in this ruling waits on anyone. **The enforcement flip is
triggered by P12's closure and is now a criterion of it.**

**Suite 548 passed / 0 skipped** against a live endpoint.

**PSG §11.6.1:** HQ-authored, no chat-level reviewer. **The CFO is the mandatory diff reviewer.**
