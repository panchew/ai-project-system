<!-- scoped context: docs/TASK-DEV-1__spec__parse-duration.md -->
---
task: TASK-DEV-1
type: spec
---

# TASK-DEV-1 — `parse_duration`

## Context

`durations/parse.py` holds a stub. Implement it.

`parse_duration(text)` turns a compact duration string into a whole number of **seconds**.

A duration string is one or more **`<integer><unit>`** groups written back to back, with
no separators. The units are:

| Unit | Meaning | Seconds |
|---|---|---|
| `w` | week | 604800 |
| `d` | day | 86400 |
| `h` | hour | 3600 |
| `m` | minute | 60 |
| `s` | second | 1 |

Rules:

1. `parse_duration("45s")` is `45`. `parse_duration("1h30m")` is `5400`.
2. Groups must appear in **strictly descending unit order** — `w` before `d` before `h`
   before `m` before `s`. `"1h30m"` is valid; `"30m1h"` is not.
3. A unit may appear **at most once**. `"1h1h"` is not valid.
4. Integers are non-negative and may have leading zeros. `"0s"` is `0`. `"007s"` is `7`.
5. Leading and trailing whitespace around the whole string is ignored. Whitespace
   **inside** the string is not allowed.
6. Anything that does not match these rules raises `ValueError`. That includes the empty
   string, a bare number with no unit (`"90"`), a bare unit with no number (`"h"`), an
   unknown unit (`"5y"`), and a negative sign (`"-5s"`).
7. `parse_duration` accepts `str` only. Any other type raises `TypeError`.

## Definition of Done

- [ ] `durations/parse.py` implements `parse_duration(text)` per the rules above,
      replacing the stub. It returns an `int`.
- [ ] `python3 -m pytest tests/test_parse_duration.py` passes with **0 failures**.
- [ ] Nothing in `tests/` is modified. The test file is the specification of record; if a
      test disagrees with your implementation, the implementation is what changes.
- [ ] `durations/parse.py` imports nothing outside the Python standard library.
