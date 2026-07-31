---
project: ai-project-system
phase: P10
milestone: M35
type: note
status: active
issuer_chat: Milestone Chat (P10-M35)
issued_to: Phase Chat (P10) → P10 Closure Declaration
last_updated: 2026-07-30
---

# Carry-Forward Note — P10-GH-9: agentic parents × default-accept × P9-GH-1

**Recorded, not fixed.** The risk described here **cannot materialize until a dispatcher exists**,
and no dispatcher for Phase or Milestone is built in P10 (HQ Ruling on SN-25, Decision 8 — P11's).
That makes this genuinely deferrable and worth writing down precisely because the day it stops being
deferrable, nobody will remember it was ever noticed.

**Origin:** surfaced during the Milestone Chat's Stage-2 review of E35.4, from the corollary that
Epic added to §"Mode is not authority" and flagged for review.

---

## The E35.4 corollary — ruled, and on firmer ground than the Epic claimed

E35.4 added, beyond its literal spec, a corollary stating that PSG §11.6's accept-by-silence presumes
a manual instance and does not extend to an unattended one. The Epic flagged it honestly as its one
judgment call and offered to have it struck.

**Ruling: it stands.** The Epic under-argued its own case. It presented the corollary as a *deduction*
from HQ Ruling Decision 4 (acceptance requires the human's key; an unattended instance has no key) —
true, but it is also **directly supported by §11.6's own text**:

- §11.6 defines the acceptance record as *"the **merge plus the in-chat acknowledgment** is the
  acceptance record"* — acceptance is bound to a merge, not to silence in isolation.
- §11.6's gate (A) preserves *"human-confirmation requirements (e.g., a human-authorized merge on an
  Epic PR)"* explicitly, and states the two gates **MUST NOT be collapsed**.

So §11.6 never granted acceptance-by-silence decoupled from a human-keyed merge. The corollary
**restates §11.6's structure under a new running mode**; it does not narrow a PSG grant, and a
system-tier document is not constraining a higher tier by saying so. Striking it would have left open
the one silent route E35.4's own acceptance criterion exists to close: *"the matrix allows an agentic
Milestone; §11.6 says silence accepts; therefore an unattended Milestone accepts by doing nothing."*

## The residual worth carrying — two parts

**1. PSG §11.6 does not name the agentic case in its own text.** The qualifier now lives one tier
down, in `governance/systems/chat-hierarchy.md`. That is correct placement for P10 (§11.6 predates
the matrix, and amending PSG was not in M35's scope), but the natural end state is for §11.6 to carry
the qualifier itself, so a reader of the highest-authority document does not have to reach a system
reference to learn how its own model behaves under an Execution Mode that did not exist when it was
written.

**2. The matrix raised the cost of P9-GH-1 without touching it.** This is the substantive half.

**P9-GH-1** is the merge-authorization hole at **Milestone→Phase** and **Phase→HQ**: the guard
routing merge authorization through the parent chat was never extended past the **Epic** templates.
Note that §11.6's own preserved-gate example is *"a human-authorized merge on an **Epic** PR"* — the
level where the guard exists.

Stack the two facts:

| | Before the matrix (SN-23 posture) | After ratification |
|---|---|---|
| Phase / Milestone Execution Mode | Manual only, by posture | **Agentic or manual** |
| Merge guard at Milestone→Phase, Phase→HQ | Absent (P9-GH-1) | Absent (unchanged) |
| Consequence | The absent guard was covered by a human being in the session | The absent guard is the only thing between an unattended parent and a merge at those two gates |

**Nothing about P9-GH-1 changed. What changed is what was compensating for it.** While Phase and
Milestone were manual by fixed posture, a human was present at those gates by construction — the same
structural argument SN-22 supplies for escalation termination. The matrix removes that guarantee as a
*permission* today and as a *practice* whenever a dispatcher lands.

P9-GH-1 was parked under SN-23 as *"enters scope only on adoption friction."* This is not friction
yet, and this note does not un-park it. It records that the item's **severity rose on 2026-07-30**
while its status stayed *parked* — precisely the kind of change that goes unnoticed because neither
document moved.

## Scope and owner

**Owner: unassigned.** Not P10 work — P10 is adoption, not capability, and both halves are
capability-shaped (a PSG amendment; a guard extension).

**Trigger for revisit — concrete, and it belongs to P11:** *before the first Phase or Milestone
agentic dispatch is wired.* A dispatcher that can launch an unattended parent at a gate with no merge
guard should not ship before P9-GH-1 is closed at that gate, or before a compensating gate is
recorded. That is a Drivr prerequisite, not a P10 defect.

## Explicitly not claimed

- This is **not** a defect in E35.4. The delivery is accepted; its corollary is upheld and its
  flagging of it is the reason this note is well-formed.
- This does **not** close, reopen, or re-scope **P9-GH-1** — it re-rates it, and says why.
- This is **not** a claim that any unattended parent has ever accepted or merged anything. No
  dispatcher for those levels exists; the matrix restores a possibility, not a default.
