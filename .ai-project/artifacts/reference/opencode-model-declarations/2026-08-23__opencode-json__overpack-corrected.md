---
project: ai-project-system
phase: P12
milestone: M41
type: reference
status: complete
last_updated: 2026-08-23
---

# `opencode.json` — the `qwen3-coder:30b` context overpack, corrected

**⚠ Out-of-repo boundary, restated because it is the whole reason this file exists.** The live file
is `~/.config/opencode/opencode.json` — **host-level, user-level, outside any repository or mount.**
Nothing in this repository enforces its contents and a fresh machine will not have them. **This
artifact is the record of a host mutation, not the mutation.**

## What changed

**One value. One line.**

```diff
33c33
<             "context": 262144,
---
>             "context": 32768,
```

| | |
|---|---|
| Model | `qwen3-coder:30b` |
| Declared before | **262144** — the trained maximum |
| Observed loaded | **32768** |
| Declared after | **32768** |
| Overpack removed | **8×** |

## How the value was derived — observed, never inferred

**E38.2's Constraint 3 applies:** derive the declared limit from what is **observed loaded**, never
from the trained maximum. Executed on the host, 2026-08-23:

1. `/api/ps` before load → `{"models":[]}` — **empty, so nothing was derivable yet.**
2. Loaded the model with an empty prompt — Ollama's own `"done_reason": "load"`, **a runtime
   operation, not inference.**
3. `/api/ps` after load → `qwen3-coder:30b context_length = 32768`.

**The 262144 was never wrong as a fact about the model — it is the trained maximum, and it is what
the always-answering endpoint returns.** It was wrong as a **declaration**, because the declared
limit is what the engine uses to decide when to compact, so a session packs past what the runtime
holds and is truncated silently. **That is the defect E38.2 named and this is the same defect on the
entry E41.1 was forbidden to touch.**

## Provenance

- **Found:** P12-M41-E41.2's execution recorded it as a live inherited condition; **E41.1 recorded it
  and deliberately did not fix it** — its spec forbade altering pre-existing entries, and it
  escalated instead.
- **Authorised:** the CFO, 2026-08-23, in the M41 Milestone Chat, alongside the ruling that collapses
  all three Epic keys to `local:qwen3-coder:30b`. **The fix matters more once this model runs manual
  Epic chats as well as the two dispatch lanes.**
- **Applied by:** the M41 Milestone Chat, session `1b70b020-4734-45ac-a514-8e4e0ba7d40c`.

## The state of all six declarations after this change

| Model | `limit.context` | |
|---|---:|---|
| `qwen3.8:27b` | 32768 | observed, E41.1 |
| `qwen3.6:27b` | 32768 | observed, E41.1 |
| **`qwen3-coder:30b`** | **32768** | **observed, this artifact** |
| `qwen2.5-coder:14b` | 32768 | pre-existing |
| `qwen2.5-coder:7b` | 32768 | pre-existing |
| `llama3.1:8b` | **131072** | ⚠ **pre-existing, and a SECOND overpack — 4×, still unfixed** |

> **⚠ `llama3.1:8b` is still overpacked and was deliberately left alone.** E41.1 found it, declared
> `131072` against `32768` loaded. **It was not part of the CFO's 2026-08-23 authorisation, which
> named `qwen3-coder:30b`.** No model in the ruled line-up uses it, so it is low-value and one
> command away. **Recorded rather than fixed, and it still has no `GH-` ID** — allocation requires
> escalating first.
