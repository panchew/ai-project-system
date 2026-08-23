---
project: ai-project-system
phase: P12
milestone: null
type: note
status: active
issuer_chat: HQ Chat (ai-project-system)
issued_to: unowned — filed, deliberately not placed
last_updated: 2026-08-23
severity: medium
---

# Carry-Forward Note — P12-GH-5: a model's declared context window exceeds what is actually loaded, silently, and the corpus records one instance while a second went unrecorded for a year

**Found by the E41.1 Epic Chat, verified by the P12-M41 Milestone Chat, escalated rather than
self-allocated.** HQ allocates the ID here; **the epic escalating instead of minting one was the rule
working and is recorded as such.**

---

## The defect

**`llama3.1:8b` declares a context window of `131072` against `32768` actually loaded — a factor of
four.** The M41 Milestone Chat verified the declared value independently rather than relaying it.

**This is the same shape as `qwen3-coder:30b`'s recorded 8× discrepancy**, which *is* in the corpus.
**The `llama3.1:8b` instance is recorded nowhere**, and nothing detected it — it surfaced only
because an epic happened to enumerate declared windows while doing something else.

**Left untouched, correctly:** the epic's spec forbids altering pre-existing entries, so it reported
rather than repaired.

---

## Why it is filed rather than fixed

**One instance in the corpus is an anecdote. Two, in different model families, with nothing that
found either, is a class.**

**The failure mode is a planning error, not a crash.** A chat or a dispatch that trusts the declared
window sizes its context to a budget four times larger than exists. **The overflow is silent** — the
model does not report that it truncated, and the caller has no signal distinguishing *"the model
considered everything and answered badly"* from *"the model never saw the second half."*

**That is this phase's disposition at the inference layer:** the evidence that would gate the
decision — how much context actually loaded — is absent, and the action proceeds.

---

## Severity: Medium

**Not High:** no decision on record has been traced to it, and both instances were caught by
inspection rather than by damage.

**Not Low:** it is a **silent** discrepancy in a value that callers use to size their inputs, it has
occurred in two unrelated model families, and **nothing in this project measures it.** The one
recorded instance was recorded by hand; the second went a year unnoticed.

---

## Explicitly not placed

**No milestone owns it and HQ is not assigning one.** M41 measures models but its scope is the
line-up, not runtime characteristics; M46 builds the qualification gate but declared-vs-loaded is not
a candidate-discrimination check.

**A cheap first step exists and is nobody's:** `/api/show` reports the declared value and `/api/ps`
reports the loaded one, so a comparison is two calls. **That is a measurement, not a fix**, and it
would establish whether this is two anecdotes or a property of the runtime.

*Trigger: any work that sizes a context budget from a declared window; or a third instance.*
