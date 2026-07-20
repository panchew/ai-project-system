# Token-Burn Dataset — E30.1 (P9-M30)

Generated 2026-07-17T22:16:01+00:00 by `bin/measure-token-burn` v1.0.0. **Aggregated numbers only** — no conversation content. Machine-readable twin: `token-burn-dataset.json`.

- Paid source: 72 harness session files, 72 with usage data, window 2026-06-12 → 2026-07-17.
- Corpus tokenizer: tiktoken/o200k_base (proxy for the Claude tokenizer; see README error bars).
- Spend kinds: `paid` (Anthropic API via Claude Code) vs `local` (ollama agentic runs) — kept in separate sections, never merged.

## 1. Paid spend — level × task-type matrix

Cell values: `sessions / API calls / output tokens / cache-creation / cache-read` (input tokens are negligible next to cache figures; full components per cell in the JSON). Empty cells carry their gap or structural record — see §6.

| level \ task | planning | execution | review | closure |
|---|---|---|---|---|
| **creation** | GAP → G6 | N/A structural → G3 | GAP → G6 | GAP → G6 |
| **hq** | n=3, calls=177, out=235,181, cc=1,936,250, cr=24,488,182 | N/A structural → G3 | GAP → G5 | GAP → G5 |
| **phase** | n=1, calls=15, out=25,509, cc=79,902, cr=959,048 | N/A structural → G3 | GAP → G4 | GAP → G4 |
| **milestone** | n=2, calls=145, out=130,933, cc=470,465, cr=25,042,834 | N/A structural → G3 | n=1, calls=35, out=57,137, cc=134,344, cr=2,914,804 | GAP → G4 |
| **epic** | N/A structural → G1 | n=38, calls=1896, out=1,535,241, cc=5,624,657, cr=173,186,511 | N/A structural → G1 | GAP → G2 |

### Mixed / unattributed buckets (whole-session totals, split is G7)

| level | bucket | sessions | API calls | output | cache-creation | cache-read |
|---|---|---|---|---|---|---|
| creation | unattributed | 5 | 267 | 438,406 | 3,920,605 | 32,100,014 |
| hq | mixed | 1 | 107 | 100,446 | 1,174,201 | 9,099,456 |
| phase | mixed | 5 | 701 | 878,543 | 6,258,389 | 114,687,143 |
| milestone | mixed | 13 | 1379 | 1,719,969 | 8,950,883 | 244,709,574 |
| milestone | unattributed | 1 | 27 | 53,249 | 336,824 | 1,131,497 |
| epic | mixed | 1 | 226 | 168,210 | 705,398 | 45,790,814 |
| unattributed | mixed | 1 | 326 | 246,395 | 2,823,652 | 31,883,177 |

## 2. Paid spend — by model (frontier mix)

| model | input | cache-creation | cache-read | output |
|---|---|---|---|---|
| claude-fable-5 | 25,439 | 2,713,397 | 51,945,538 | 604,170 |
| claude-opus-4-8 | 318,556 | 16,298,848 | 270,618,587 | 2,812,338 |
| claude-sonnet-4-6 | 993 | 6,159,872 | 68,627,722 | 611,730 |
| claude-sonnet-5 | 20,982 | 7,243,453 | 314,801,207 | 1,560,981 |

## 3. Measured context load (provider-billed)

| level | first-turn context, median | per-call context, median |
|---|---|---|
| creation | 29,749 | 102,515 |
| hq | 23,051 | 101,163 |
| phase | 22,228 | 169,003 |
| milestone | 19,356 | 129,135 |
| epic | 20,966 | 76,135 |

First-turn = input + cache-creation + cache-read of the session's first API call (system prompt + memory + first message). Per-call = session context total / API calls (what each call re-reads, mostly cached).

## 4. Governance-corpus overhead (Direction B, proxy tokenizer — G10)

| file | tokens (o200k proxy) |
|---|---|
| PSG (PROJECT-SYSTEM-GUIDELINES.md) | 10,443 |
| AOG (AI-OPERATING-GUIDELINES.md) | 12,080 |
| yml spec (ai-project-yml-spec.md) | 7,140 |
| generic epic starter (governance/EPIC-EXECUTION-CHAT-STARTER.md) | 859 |
| P9 phase starter | 2,687 |
| P9 phase spec | 5,268 |
| M30 milestone starter | 3,593 |
| M30 milestone spec | 5,230 |
| E30.1 epic starter | 2,997 |
| E30.1 epic spec | 3,816 |

| directory | tokens | files |
|---|---|---|
| governance/ total (*.md recursive) | 157,287 | 69 |
| governance/templates | 34,030 | 25 |
| governance/systems | 33,470 | 13 |

Per-level load packs (starter + required specs + PSG + AOG):

| level | pack tokens (o200k proxy) |
|---|---|
| phase | 30,478 |
| milestone | 36,614 |
| epic | 29,336 |

## 5. Local (ollama) spend — Direction C-lite

| run | model | output tokens | prompt tokens | context.md (proxy) | duration ms |
|---|---|---|---|---|---|
| P7-M26-E26.3-PROVE | qwen2.5-coder:14b | 404 | GAP → G9 | 671 | 20595 |

## 6. Gap records (Hard Constraint)

- **G1** (structural; epic × planning; epic × review): Epic planning and epic review are performed inside the parent chats (Milestone/Phase), never in a standalone epic-level session — no such session type exists to measure. Their spend is contained in the milestone/phase planning, review, and mixed cells.
- **G2** (gap; epic × closure): Epic closure (Delivery Notice authoring) happens inside the epic execution session. The mechanism attributes whole sessions and does not segment spend within a session, so the closure share is bundled into epic x execution and not separately measurable.
- **G3** (structural; milestone × execution; phase × execution; hq × execution; creation × execution): Only Epic chats execute; Milestone/Phase/HQ/Creation delegate execution downward. These cells are structurally empty, not measurement holes.
- **G4** (gap; milestone × closure; phase × review; phase × closure): Milestone/phase review and closure activity is embedded in long mixed-purpose sessions (see the mixed bucket) and cannot be separated per-message by this mechanism. Whole-session totals for those sessions are reported in the mixed bucket; the per-task split is a gap.
- **G5** (gap; hq × review; hq × closure): HQ work (scoping, digests, coordination, acceptance) does not map one-to-one onto the four task types; sessions with pure planning signals are measured, the remainder are mixed or signal-free. HQ level totals are measured; these per-task cells are gaps.
- **G6** (gap; creation × planning; creation × review; creation × closure): Creation Chat sessions (seed-booted) produce artifacts in-conversation and write no governance files to the repo, so the task-type signals cannot see their work. Creation level totals are measured (see per-session rows); the per-task split is a gap.
- **G7** (gap; cross-cutting): Mixed-purpose sessions (level attributed, several task types in one session) are reported as their own bucket with full totals; their internal per-task split is a recorded gap, not estimated.
- **G8** (gap; cross-cutting): Coverage is limited to this machine's harness directory. Sessions on other surfaces or machines (e.g. any claude.ai web chats for Creation/HQ) and any deleted local sessions are invisible to the mechanism and unmeasured.
- **G9** (gap; cross-cutting): Local (ollama) prompt/input tokens: the runner transcript records per-turn output eval_count only; prompt_eval_count is not persisted and run-metadata.json carries no token counts (unchanged by this epic). Local output tokens are measured; local input tokens are a gap (context.md size is proxy-tokenized as the context figure).
- **G10** (limitation; cross-cutting): Direction B corpus numbers use tiktoken o200k_base as a proxy for the Claude tokenizer (billed counts). Treat them with an error bar of roughly +/-10-15% typical for English markdown; they are suitable for proportions and ordering, not exact billing. Paid-side first-turn and per-call context medians ARE provider-billed numbers, but include the harness system prompt and memory, not governance corpus alone.

## 7. Per-session aggregates (paid)

Attribution rules are documented in README.md. `level_rule`/`task_rule` state which rule fired; `branch-fallback` and signal-based rules are lower-confidence than `first-message`.

| session | date | level (rule) | task (rule) | calls | input | cache-cr | cache-rd | output | first-turn ctx |
|---|---|---|---|---|---|---|---|---|---|
| 4735e1dc | 2026-06-12 | unattributed (none) | mixed (signals:planning+closure) | 326 | 2,797 | 2,823,652 | 31,883,177 | 246,395 | 14,758 |
| 3caa6b86 | 2026-06-13 | epic (first-message) | execution (role) | 69 | 75 | 182,723 | 5,270,861 | 40,883 | 22,784 |
| 512af82f | 2026-06-13 | hq (first-message) | mixed (signals:planning+review+closure) | 107 | 139 | 1,174,201 | 9,099,456 | 100,446 | 20,088 |
| a8637d59 | 2026-06-13 | milestone (first-message) | mixed (signals:planning+review+closure) | 57 | 80 | 532,693 | 4,962,872 | 60,577 | 21,030 |
| b91de094 | 2026-06-13 | phase (first-message) | mixed (signals:planning+closure+delivery_handling) | 204 | 248 | 1,526,278 | 18,958,978 | 193,765 | 21,817 |
| b1444f31 | 2026-06-15 | milestone (branch-fallback) | unattributed (no-signals) | 27 | 4,826 | 336,824 | 1,131,497 | 53,249 | 13,805 |
| b1d38ce2 | 2026-06-17 | milestone (first-message) | mixed (signals:planning+review+closure) | 133 | 10,733 | 385,812 | 16,233,994 | 118,829 | 16,823 |
| b5881f04 | 2026-06-17 | epic (first-message) | execution (role) | 72 | 6,211 | 151,195 | 5,324,314 | 56,125 | 18,156 |
| 75bf59aa | 2026-06-18 | epic (first-message) | execution (role) | 102 | 19,667 | 510,626 | 15,376,234 | 114,333 | 19,936 |
| a252bba7 | 2026-06-18 | milestone (first-message) | mixed (signals:review+closure) | 31 | 8,454 | 76,897 | 1,330,350 | 23,685 | 19,176 |
| dd3bfe59 | 2026-06-18 | epic (first-message) | execution (role) | 34 | 13,628 | 157,316 | 2,081,957 | 28,952 | 16,325 |
| 3e555593 | 2026-06-20 | epic (first-message) | execution (role) | 56 | 9,176 | 93,065 | 3,710,430 | 37,594 | 18,991 |
| 985fefe2 | 2026-06-20 | milestone (first-message) | mixed (signals:planning+review+closure) | 74 | 9,141 | 236,809 | 7,552,471 | 101,426 | 18,826 |
| c6e9a2bc | 2026-06-20 | epic (first-message) | execution (role) | 70 | 17,509 | 361,929 | 5,776,480 | 49,796 | 18,116 |
| 63949cc0 | 2026-06-24 | phase (first-message) | mixed (signals:planning+review+delivery_handling) | 119 | 30,152 | 1,735,027 | 28,650,644 | 282,358 | 19,822 |
| 2c93c36a | 2026-06-25 | epic (first-message) | execution (role) | 24 | 4,571 | 86,489 | 1,084,416 | 21,189 | 19,908 |
| ad7d43f6 | 2026-06-25 | milestone (first-message) | mixed (signals:planning+review+closure) | 108 | 9,061 | 1,088,259 | 19,598,867 | 198,374 | 19,356 |
| 2aa61a92 | 2026-06-26 | epic (first-message) | execution (role) | 23 | 4,599 | 74,964 | 1,115,191 | 25,974 | 15,846 |
| 25bdc917 | 2026-06-27 | epic (first-message) | execution (role) | 33 | 4,124 | 116,643 | 2,880,700 | 31,185 | 14,863 |
| 588dab4d | 2026-06-27 | epic (first-message) | execution (role) | 24 | 4,648 | 42,445 | 933,518 | 12,984 | 15,567 |
| 5b365f77 | 2026-06-27 | epic (first-message) | execution (role) | 34 | 4,663 | 104,518 | 1,786,314 | 19,572 | 15,689 |
| 808814a3 | 2026-06-27 | milestone (first-message) | mixed (signals:planning+review+closure) | 58 | 7,288 | 382,712 | 5,926,070 | 99,736 | 15,682 |
| d986496c | 2026-06-27 | epic (first-message) | execution (role) | 46 | 6,309 | 97,127 | 3,163,387 | 34,025 | 15,691 |
| 560100ae | 2026-06-28 | epic (first-message) | execution (role) | 46 | 6,524 | 185,109 | 4,127,490 | 46,575 | 15,985 |
| 7f0a6440 | 2026-06-28 | milestone (first-message) | mixed (signals:planning+closure) | 61 | 9,493 | 661,173 | 7,206,604 | 97,641 | 15,799 |
| 95d1571e | 2026-06-28 | epic (first-message) | execution (role) | 47 | 6,631 | 126,168 | 3,770,540 | 56,341 | 16,022 |
| c5c8deda | 2026-06-28 | epic (first-message) | execution (role) | 38 | 5,445 | 94,656 | 2,305,371 | 34,086 | 15,791 |
| 4140d3f0 | 2026-06-29 | epic (first-message) | execution (role) | 30 | 6,096 | 84,178 | 1,639,685 | 26,732 | 16,141 |
| afa3c75b | 2026-06-29 | phase (first-message) | mixed (signals:planning+closure) | 108 | 23,024 | 1,401,248 | 17,697,384 | 170,312 | 15,241 |
| b0294145 | 2026-06-29 | hq (first-message) | planning (signals) | 113 | 5,414 | 1,619,586 | 18,980,876 | 155,474 | 20,778 |
| c23d583e | 2026-06-29 | creation (first-message) | unattributed (no-signals) | 115 | 11,294 | 2,761,241 | 18,799,989 | 280,959 | 17,571 |
| ceaba5dd | 2026-06-29 | milestone (first-message) | mixed (signals:planning+closure) | 74 | 15,092 | 563,007 | 10,046,473 | 123,692 | 16,123 |
| e17e800e | 2026-06-29 | epic (first-message) | execution (role) | 39 | 5,134 | 146,097 | 2,843,769 | 33,487 | 20,915 |
| 417cf960 | 2026-06-30 | epic (first-message) | execution (role) | 33 | 5,228 | 160,635 | 2,026,164 | 41,653 | 20,966 |
| 67c9a58b | 2026-06-30 | milestone (first-message) | mixed (signals:planning+closure) | 76 | 14,646 | 543,550 | 10,124,398 | 114,652 | 20,058 |
| 56e005e7 | 2026-07-02 | epic (first-message) | execution (role) | 30 | 4,771 | 118,138 | 1,733,116 | 26,061 | 19,008 |
| 578cb649 | 2026-07-03 | milestone (branch-fallback) | review (first-message) | 35 | 5,513 | 134,344 | 2,914,804 | 57,137 | 20,522 |
| a26452cd | 2026-07-03 | epic (first-message) | execution (role) | 57 | 9,145 | 204,664 | 6,355,776 | 61,514 | 20,847 |
| f3cd130d | 2026-07-03 | epic (first-message) | execution (role) | 31 | 5,139 | 92,499 | 1,959,892 | 34,654 | 20,410 |
| f5fedd22 | 2026-07-03 | milestone (first-message) | mixed (signals:planning+closure) | 184 | 27,619 | 2,231,141 | 51,878,179 | 321,879 | 19,000 |
| cd0b37fa | 2026-07-07 | epic (first-message) | execution (role) | 49 | 98 | 134,298 | 3,404,005 | 26,672 | 32,585 |
| da4b2438 | 2026-07-07 | epic (first-message) | execution (role) | 56 | 112 | 132,012 | 3,928,281 | 24,686 | 31,805 |
| 324cc892 | 2026-07-08 | epic (first-message) | execution (role) | 48 | 96 | 103,575 | 3,556,718 | 28,432 | 32,004 |
| 9bafa61f | 2026-07-11 | creation (first-message) | unattributed (no-signals) | 66 | 5,489 | 567,993 | 6,505,181 | 57,800 | 34,824 |
| 185e0694 | 2026-07-12 | phase (first-message) | mixed (signals:planning+review+closure+delivery_handling) | 170 | 336 | 1,038,487 | 33,842,968 | 159,157 | 22,639 |
| 5eee1fb0 | 2026-07-12 | milestone (first-message) | mixed (signals:planning+closure) | 169 | 337 | 765,621 | 34,058,954 | 156,418 | 22,869 |
| 88bb556b | 2026-07-12 | epic (first-message) | execution (role) | 26 | 51 | 75,203 | 1,572,161 | 30,544 | 22,882 |
| 2cc0bad4 | 2026-07-13 | epic (first-message) | execution (role) | 50 | 100 | 145,880 | 5,917,633 | 43,178 | 34,667 |
| 6ce000fc | 2026-07-13 | epic (first-message) | execution (role) | 36 | 72 | 104,163 | 3,317,665 | 39,747 | 34,232 |
| 79de3147 | 2026-07-13 | epic (first-message) | execution (role) | 54 | 108 | 101,129 | 4,281,156 | 27,851 | 34,404 |
| 7dd5c0b3 | 2026-07-13 | milestone (first-message) | mixed (signals:planning+closure+delivery_handling) | 214 | 428 | 860,633 | 54,019,683 | 173,616 | 34,181 |
| 7e0e95fe | 2026-07-13 | epic (first-message) | execution (role) | 151 | 302 | 509,959 | 28,533,207 | 143,575 | 34,003 |
| 8c9d55d2 | 2026-07-13 | epic (first-message) | execution (role) | 40 | 80 | 100,593 | 3,842,536 | 29,820 | 34,214 |
| aaa16d82 | 2026-07-13 | epic (branch-fallback) | mixed (signals:planning+closure+delivery_handling) | 226 | 11,364 | 705,398 | 45,790,814 | 168,210 | 40,366 |
| c2cb4082 | 2026-07-13 | epic (first-message) | execution (role) | 97 | 194 | 149,382 | 9,618,270 | 54,944 | 34,233 |
| ddff3f41 | 2026-07-13 | milestone (first-message) | planning (signals) | 128 | 256 | 396,143 | 24,031,219 | 105,392 | 34,382 |
| f71d128a | 2026-07-13 | epic (first-message) | execution (role) | 40 | 74 | 128,469 | 2,077,456 | 21,969 | 22,912 |
| 1ca83dbb | 2026-07-14 | epic (first-message) | execution (role) | 41 | 82 | 92,217 | 2,836,491 | 22,024 | 34,247 |
| 5ace29f0 | 2026-07-14 | creation (first-message) | unattributed (no-signals) | 61 | 122 | 530,354 | 5,722,970 | 78,897 | 35,387 |
| a7bbcbc5 | 2026-07-14 | epic (first-message) | execution (role) | 57 | 114 | 100,789 | 4,509,243 | 28,458 | 34,470 |
| 46ee7e03 | 2026-07-15 | hq (first-message) | planning (signals) | 39 | 78 | 228,159 | 3,917,889 | 38,664 | 38,221 |
| d32f9742 | 2026-07-15 | phase (first-message) | mixed (signals:planning+closure) | 100 | 910 | 557,349 | 15,537,169 | 72,951 | 33,913 |
| 1d84328e | 2026-07-16 | epic (first-message) | execution (role) | 54 | 108 | 97,879 | 4,429,819 | 34,729 | 34,360 |
| 78839715 | 2026-07-16 | epic (first-message) | execution (role) | 97 | 194 | 292,492 | 11,916,430 | 73,655 | 34,394 |
| b63cfdd7 | 2026-07-16 | epic (first-message) | execution (role) | 36 | 72 | 63,618 | 2,344,633 | 19,557 | 34,351 |
| b68eb249 | 2026-07-16 | milestone (first-message) | mixed (signals:planning+closure) | 140 | 280 | 622,576 | 21,770,659 | 129,444 | 34,386 |
| 3331978d | 2026-07-17 | milestone (first-message) | planning (signals) | 17 | 33 | 74,322 | 1,011,615 | 25,541 | 24,602 |
| 6b9a1b4e | 2026-07-17 | creation (first-message) | unattributed (no-signals) | 24 | 45 | 43,874 | 1,059,289 | 19,902 | 29,749 |
| c10b3cb0 | 2026-07-17 | phase (first-message) | planning (signals) | 15 | 28 | 79,902 | 959,048 | 25,509 | 24,554 |
| ce8fab50 | 2026-07-17 | creation (first-message) | unattributed (no-signals) | 1 | 2 | 17,143 | 12,585 | 848 | 29,730 |
| da848017 | 2026-07-17 | hq (first-message) | planning (signals) | 25 | 47 | 88,505 | 1,589,417 | 41,043 | 25,324 |
| e92a5427 | 2026-07-17 | epic (first-message) | execution (role) | 26 | 51 | 101,815 | 1,835,202 | 51,685 | 24,632 |

