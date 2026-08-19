---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-08-19T23:59:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-39
    severity: low
    title: Pre-reset continuity note — P12 is open and running; what the next Creation Chat session inherits, and the one trap waiting for it
decisions:
  - "This session's substantive output is SN-31 through SN-38, across three notes plus the filed HQ opener. This note adds no new position — it exists so the next session starts from state rather than reconstructing it."
  - "The Creation Chat's next engagement is expected at P12's close, at the CFO's discretion. Nothing in P12 waits on this chat."
references:
  - ".ai-project/artifacts/steering-notes/2026-08-18__creation-chat__steering-note__P12-spine-fail-open.md — SN-31…SN-35"
  - ".ai-project/artifacts/steering-notes/2026-08-19__creation-chat__steering-note__drivr-ux-and-model-qualification.md — SN-36/SN-37"
  - ".ai-project/artifacts/steering-notes/2026-08-19__creation-chat__steering-note__model-lineup.md — SN-38"
  - ".ai-project/artifacts/hq-openers/2026-08-19__hq-chat-opener.md — the opener that instantiated P12's HQ session"
---

# Steering Note — Creation Chat to HQ Chat

## Purpose

**Pre-reset continuity, per `creation-chat-guide.md` Re-instantiation Ritual Steps 1 and 2.** The
CFO is closing this session and expects to return at P12's close.

This session produced three Steering Notes carrying eight concerns, all addressed **to HQ**. None
was addressed to the *next Creation Chat session*, which is what the ritual actually requires. This
note is that, and nothing more — **no new position is taken here.**

---

## SN-39 — What the next session inherits [LOW]

### State at close

| | |
|---|---|
| **Phase** | **P12 OPEN** — *Completion: Fail-Closed Defaults and the Drivr MVP.* Six milestones, M41–M46 |
| **Binding orders** | M41 → M46 (no M46 epic dispatches agentically until M41 closes); M44 → M45 (the surface *is* the completion signal) |
| **Open PR** | **#215**, `governance/hq-p12-opening` — HQ's phase opening, not yet merged |
| **Master** | `afe5d79`, pushed |
| **Suite** | 549 passed / 0 failed |
| **Waiting on this chat** | **nothing** |

### The one thing that will bite on return, stated first because it is easy to miss

**`.ai-project.yml`'s `models.creation` is scheduled to move from `remote:claude-opus-5` to
`fable-5`** (SN-38, CFO ruling). The Seed's *Prerequisite Verification* compares a Creation Chat's
harness-reported model against that key and **halts on mismatch**.

**So if the edit lands during P12, the next Creation Chat session must be opened on fable-5.**
Opening it on opus-5 out of habit will stop the session at its first instruction — correctly, and
confusingly if unexpected.

**Under SN-38 the edit is gated:** `creation` is a manual verification target, and the CFO ruled that
SN-37's qualification gate binds those too, so fable-5 must pass the planted-defect back-test before
the key moves. **Check `models.creation` before opening the next session.** That check costs seconds
and is the difference between a working re-instantiation and a halt nobody expects.

### What the next session should read

The ritual's Step 3 is unchanged: paste the **Seed**, then pass the **most recent Steering Note** and
the **most recent Progress Digest**. At P12's close both will be newer than anything in this session.
**This note is not the one to pass if a later one exists** — the ritual says most recent, and by
then it will not be this.

For history, the three substantive notes of 2026-08-18/19 are listed in this note's `references`.
They are referenced, not summarised — SN-23's rule that artifacts pass by reference.

### Carry-overs that are genuinely the Creation Chat's, not HQ's

Everything else filed this session belongs to HQ or to a milestone. These three do not:

1. **The Drivr UX vision is `State: proposed`.** Its binding
   (https://claude.ai/code/artifact/688a152b-df5d-4882-b48f-26108200b92c) is recorded at SN-36. When
   M45 builds the surface, the **`implemented`** half of AOG §16.6's two-track pair becomes due, and
   the Creation Chat is where the `proposed` half came from. A returning session should expect to
   compare them.
2. **Four topics from the 2026-08-18 dump were never scoped and are not lost, only unplaced:**
   `content-creation-pipeline`, `wheelie`, `panchew-io` (the new projects), and the **harness vision**
   the CFO deferred to its own conversation. The ecosystem was four projects at P11; these would make
   it seven. **That is a Brief-level identity question**, not a phase question, and it is the natural
   subject of a returning Creation Chat.
3. **`github.com/spec-kit` and `gonzalezpazmonica/pm-workspace`** were offered as sources to mine and
   never opened. Low cost, non-urgent, still available.

### Two things a returning session should verify rather than assume

**This session made three errors of the same class, all caught one level down.** They are recorded in
their notes; the pattern is repeated here because it is the most useful thing this session learned
about its own reliability:

- E29.3's precision FAILs read as a verdict on the Generative track, when its own delivery notice
  attributes them to one model's known weakness (**environment axis**).
- `governance-propagation.md` cited as prohibiting work, without checking that its stated constraints
  had expired (**time axis** — became SN-34).
- SN-35 filed claiming HQ had no re-instantiation path, after grepping the normative tier and not the
  artifact corpus, where **eight prior openers** sat (**layer axis** — corrected in SN-38's commit).

All three are `P11-GH-2`. **A returning session should verify claims in the tier they are about, not
the tier that is easiest to search.**

---

## Next Action

**For HQ, and it is live:**

**SN-38 is not on `governance/hq-p12-opening`.** Commits `3eda074` and `afe5d79` landed on master
after the branch was cut; the phase spec has zero occurrences of `SN-38`, `Deepseek` or `epic_qa`.
SN-31…SN-37 all reached it — only the model line-up did not.

**This is `P11-GH-1` firing live, inside the phase that owns fixing it** — a spec amended after its
working branch was cut, for the fifth recorded time. Merge master into the branch and reconcile the
five items SN-38 raises before #215 merges; amending an unmerged spec is cheaper than amending a
merged one. **Record this instance as dated evidence against `P11-GH-1`** — it is the first one
observed in P12 and it was found by the Creation Chat rather than by the mechanism.

**For the next Creation Chat session:** check `models.creation` before opening. Then take direction
from the most recent Steering Note's Next Action, per the ritual — not from this one, unless it is
still the most recent.
