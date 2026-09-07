---
artifact_type: reference
artifact_version: 1.0
timestamp: 2026-08-21T21:00:00Z
issuer_chat: Epic Execution Chat (P12-M41-E41.1)
project_name: ai-project-system
phase: P12
milestone: M41
epic: E41.1
subject: host OpenCode model declarations
records_host_mutation: true
host: panchew@ (this workstation)
file_recorded: /home/panchew/.config/opencode/opencode.json
applied: 2026-08-21
sha256_before: f5cee248bc8dcb60fa42e03d06f2208039820a007d0ab0eb6bf31d2a9f17158e
sha256_after: 608828e1a3f903d4825500d278fd00f845d6a3c13adbe28920650c35d15087fd
---

# Reference — `opencode.json` after declaring both 27b models (E41.1 / D3+D4)

## ⚠ The out-of-repo boundary — read this before relying on anything below

**The file this artifact records lives OUTSIDE this repository and cannot be version-controlled.**

- The live file is `/home/panchew/.config/opencode/opencode.json`, on **one host**.
- **Nothing in this repository enforces its contents.** There is no test, no hook, no validator and
  no CI step that reads it, asserts it, or restores it. `git ls-files` filtered for `opencode`
  returns only measurement artifacts and spec prose — **no copy of this config has ever been
  tracked** (verified 2026-08-21).
- **A fresh machine will not have this.** A clone of this repository, on a new host, has an
  `opencode.json` that declares neither 27b model — or no `opencode.json` at all. Every local-model
  claim in M41 is a claim about *this* host.
- **This artifact is a RECORD OF a host mutation, not the mutation itself and not a mechanism for
  reproducing it.** If the live file is edited, deleted, or replaced, this artifact will not know
  and will not say so. It is accurate as of the date in its front-matter and **its accuracy decays
  silently.**
- **To reapply on another host**, the JSON in §2 must be merged by hand into that host's file. The
  `limit.context` values below were **observed on this host's hardware** (see §4) and are not
  guaranteed to be what another machine's runtime loads.

**Anyone re-measuring should re-derive the limits rather than copy them.**

---

## 1. What changed, and what deliberately did not

**Two entries added under `provider.ollama.models`. Nothing else touched.**

| | Before | After |
|---|---|---|
| Size | 1,217 bytes | 1,609 bytes |
| sha256 | `f5cee248bc8dcb60fa42e03d06f2208039820a007d0ab0eb6bf31d2a9f17158e` | `608828e1a3f903d4825500d278fd00f845d6a3c13adbe28920650c35d15087fd` |
| mtime | 2026-07-22 23:30:20 | 2026-08-21 14:53:59 |
| Ollama models declared | 4 | 6 |
| Lines added / removed / modified | — | **+16 / 0 / 0** |

### 1.1 The before/after diff

```diff
--- opencode.json (before, mtime 2026-07-22 23:30:20)
+++ opencode.json (after,  mtime 2026-08-21 14:53:59)
@@ -10,6 +10,22 @@
         "baseURL": "http://localhost:11434/v1"
       },
       "models": {
+        "qwen3.8:27b": {
+          "name": "Qwen3.8 27B (local)",
+          "tool_call": true,
+          "limit": {
+            "context": 32768,
+            "output": 8192
+          }
+        },
+        "qwen3.6:27b": {
+          "name": "Qwen3.6 27B (local)",
+          "tool_call": true,
+          "limit": {
+            "context": 32768,
+            "output": 8192
+          }
+        },
         "qwen3-coder:30b": {
           "name": "Qwen3 Coder 30B (local, best quality)",
           "tool_call": true,
```

**The diff is purely additive.** No `-` line exists in it.

### 1.2 The four pre-existing entries are byte-identical — proven three ways

The Epic spec requires this shown by diff. It is shown by diff **and** by two stronger checks,
because a diff proves the lines did not change while these prove the *entries* did not:

1. **Diff:** zero removed lines, zero modified lines (§1.1).
2. **Structural:** each pre-existing entry, parsed and canonically re-serialized with sorted keys,
   compares **equal** before and after — `qwen3-coder:30b`, `qwen2.5-coder:14b`, `qwen2.5-coder:7b`,
   `llama3.1:8b`, all `True`.
3. **Raw substring:** each pre-existing entry's exact source text block from the *before* file is
   located **verbatim** inside the *after* file — all four `True`.

`$schema`, `model`, `small_model` and `provider.ollama.options` also compare equal.

**The insertion point was chosen to make this cheap to verify:** the two new entries were inserted
**immediately after `"models": {`**, ahead of every existing entry, so no existing byte moves
relative to its own block and no existing line is even adjacent to an edit.

---

## 2. The resulting file, verbatim

This is the complete content of `/home/panchew/.config/opencode/opencode.json` as of
**2026-08-21**, sha256 `608828e1a3f903d4825500d278fd00f845d6a3c13adbe28920650c35d15087fd`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-sonnet-5",
  "small_model": "anthropic/claude-haiku-4-5",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": {
        "baseURL": "http://localhost:11434/v1"
      },
      "models": {
        "qwen3.8:27b": {
          "name": "Qwen3.8 27B (local)",
          "tool_call": true,
          "limit": {
            "context": 32768,
            "output": 8192
          }
        },
        "qwen3.6:27b": {
          "name": "Qwen3.6 27B (local)",
          "tool_call": true,
          "limit": {
            "context": 32768,
            "output": 8192
          }
        },
        "qwen3-coder:30b": {
          "name": "Qwen3 Coder 30B (local, best quality)",
          "tool_call": true,
          "limit": {
            "context": 262144,
            "output": 8192
          }
        },
        "qwen2.5-coder:14b": {
          "name": "Qwen2.5 Coder 14B (local, faster)",
          "tool_call": true,
          "limit": {
            "context": 32768,
            "output": 8192
          }
        },
        "qwen2.5-coder:7b": {
          "name": "Qwen2.5 Coder 7B (local, fastest)",
          "tool_call": true,
          "limit": {
            "context": 32768,
            "output": 8192
          }
        },
        "llama3.1:8b": {
          "name": "Llama 3.1 8B (local, general chat)",
          "tool_call": true,
          "limit": {
            "context": 131072,
            "output": 8192
          }
        }
      }
    }
  }
}
```

**Two values in the text above are known-wrong and are reproduced faithfully rather than corrected:**
`qwen3-coder:30b`'s `262144` and `llama3.1:8b`'s `131072`. See §5.

---

## 3. Why each field of the new entries has the value it has

| Field | Value | Basis |
|---|---|---|
| `tool_call` | `true` | Required by the Epic spec, and matched to all four existing entries |
| `limit.context` | `32768` | **Observed loaded** on this host, 2026-08-21 (§4). **Not a trained maximum** |
| `limit.output` | `8192` | **A choice, not a measurement.** All four existing entries read `8192`; matching them keeps the file internally consistent. **No output limit was observed and none is claimed** |
| `name` | `"Qwen3.8 27B (local)"` / `"Qwen3.6 27B (local)"` | Deliberately plain. The existing entries editorialize (*"best quality"*, *"faster"*); **E41.1 measures no model's quality**, and a display name asserting one would prejudge exactly what E41.2 and E41.3 exist to measure |

---

## 4. How `limit.context` was derived — load, then observe

**Method:** `drivr.execution.context_limits.observe_loaded_context`, from **Drivr at HEAD
`f60164c`**, imported read-only. Drivr was **not modified**.

**Why Drivr's function rather than a direct read** (Epic design decision 2): the adapter rewrites
this entry's `limit.context` on every dispatch from its own observation. Deriving the declared value
by a second, independently-written path risks declaring a number the adapter then disagrees with.
Reuse makes agreement structural rather than coincidental.

**The sequence, and it matters that step 1 came first:**

1. `GET /api/ps` → **`{"models":[]}`** — nothing loaded, so **no limit was derivable at that point.**
2. Each model was **loaded** (an empty-prompt request; Ollama's own `done_reason` for it is
   `"load"` — runtime control, not inference).
3. `GET /api/ps` re-read, and the value it reported for the loaded model was used.

| Model | `context_length` observed | `source` | `size_vram` at observation |
|---|---:|---|---:|
| `qwen3.8:27b` | **32,768** | `observed-after-load` | 10,764,083,526 |
| `qwen3.6:27b` | **32,768** | `observed-after-load` | 11,924,521,613 |

Raw `/api/ps` entry for `qwen3.8:27b`, as returned:

```json
{"name": "qwen3.8:27b", "model": "qwen3.8:27b",
 "digest": "22130167c4c20e20c7b71454612966ca8e8171e9b3cc8ab6ce8aa6cbfec79643",
 "context_length": 32768, "size_vram": 10764083526,
 "expires_at": "2026-08-21T20:58:03.339419716Z"}
```

**The digest is recorded, not only the name**, so *"the model we measured"* and *"the model we
declared"* are the same claim: a tag is mutable, a digest is not.

- `qwen3.8:27b` → `22130167c4c20e20c7b71454612966ca8e8171e9b3cc8ab6ce8aa6cbfec79643`
- `qwen3.6:27b` → `a50eda8ed977ab48a12431878896b27ffd5cef552c17af3317d9623b939a7f1e`

**The absent-limit fallback was not needed.** Both models were observable, so both entries carry a
real `context`. Had either not been, that entry would have shipped **with no `limit.context` at
all** — an absent declaration is honest; an inherited maximum is the bug.

---

## 5. ⚠ Two known-wrong values in this file, neither of them this epic's to fix

Completing the declared-vs-observed comparison across **all six** entries:

| Model | DECLARED here | OBSERVED loaded | Ratio |
|---|---:|---:|---:|
| `qwen3.8:27b` | 32,768 | 32,768 | 1× |
| `qwen3.6:27b` | 32,768 | 32,768 | 1× |
| **`qwen3-coder:30b`** | **262,144** | 32,768 | **8× — overpack** |
| `qwen2.5-coder:14b` | 32,768 | 32,768 | 1× |
| `qwen2.5-coder:7b` | 32,768 | 32,768 | 1× |
| **`llama3.1:8b`** | **131,072** | 32,768 | **4× — overpack** |

**`qwen3-coder:30b`'s 8× overpack is the recorded one** (P11-M38-E38.2, Finding 2) and it survives
re-measurement here. **It is deliberately left in place**: the incumbent's declared context is an
input to E41.2's baseline, and changing it mid-milestone would measure the incumbent on a different
configuration than the one its historical evidence came from.

**`llama3.1:8b`'s 4× overpack is NOT recorded anywhere in this corpus.** It was found by completing
the inventory. It is **untouched** — the Epic spec forbids altering the four pre-existing entries —
and it is **escalated** rather than fixed silently.

**Why the declared value matters at all:** the engine uses it to decide when to compact a
conversation. A declaration larger than what the runtime actually loads means long sessions pack
past the real window and are **truncated silently.**

---

## 6. Verification commands, for a future reader

```bash
sha256sum ~/.config/opencode/opencode.json     # expect 608828e1…87fd, as of 2026-08-21
opencode models | grep '^ollama/'              # expect 6 entries, incl. both 27b
curl -s http://localhost:11434/api/ps          # empty until something is loaded
```

**A mismatch means the live file moved after this artifact was written.** That is expected
eventually and is precisely the out-of-repo boundary in §0 — **this artifact will not have noticed.**

---

## Related

- `docs/phases/P12__Completion_Fail_Closed_Defaults_and_the_Drivr_MVP/P12-M41-E41.1__record__target-resolution-reachability-and-routability.md` — the D1/D2/D5 measurement record, including the dispatches that prove both new entries are routable
- `docs/phases/P11__Drivr_Coordination_Over_Rented_Execution/P11-M38-E38.2__spec__execution-adapter-surface-and-opencode-adapter.md` — the `/api/ps`-versus-trained-maximum finding and Constraint 3
- Drivr `f60164c`: `drivr/execution/context_limits.py`, `drivr/execution/opencode.py` — read-only
