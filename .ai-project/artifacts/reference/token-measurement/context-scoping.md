---
project: ai-project-system
phase: P9
milestone: M30
epic: E30.3
type: reference
status: active
last_updated: 2026-07-18
---

# Per-Level Context-Scoping Standard — E30.3 (P9-M30)

**What this is:** the committed answer to "what should a chat at level X load, and
why" for every chat level, derived from the roles the governance documents define
and from measured pack composition — plus the before/after evidence for the pack
reduction E30.3 implemented, and the bounded-scope finding for the context share
no document can control.

**Evidence base:** the E30.1 dataset ([`token-burn-dataset.md`](token-burn-dataset.md)
§§3–4) and the E30.2 audit report ([`audit-report.md`](audit-report.md) §4 findings
7–9, §2.1–2.2), both committed on `milestone/M30`, plus this epic's own composition
measurements (§2 below), produced with the same tokenizer as the mechanism's
Direction B (tiktoken `o200k_base`). **All corpus numbers in this document are
proxy tokens with ±10–15% error bars (G10) — suitable for proportions and
ordering, never billed counts.** Billed medians quoted from dataset §3 are exact
provider-billed numbers.

**Normative status:** the per-level load lists in §3 are normative for the starter
*templates* (`governance/templates/`), which carry self-contained copies so
adopting repos do not depend on this artifact's path. This document is the
evidence record and tie-breaker. PSG and AOG remain fully authoritative: scoping
changes what a chat *loads at session start*, never what the documents *say* — a
chat that hits a situation covered by a section it did not load MUST load that
section before acting (the conditional-load rule, §3.1).

---

## 1. The problem, sized by the measurements

Every governed chat is (implicitly) instructed to load the full governance pack —
starter + required specs + full PSG + full AOG. Measured (dataset §4, confirmed by
re-tokenization on 2026-07-18):

| level | pack (proxy tokens) | PSG+AOG share of pack | billed per-call median (dataset §3) |
|---|---:|---:|---:|
| phase | 30,478 | 22,523 (74%) | 169,003 |
| milestone | 36,614 | 22,523 (62%) | 129,135 |
| epic | 29,336 | 22,523 (77%) | 76,135 |

The packs were assembled by accretion, never scoped against each level's role.
Cache re-reads — what per-call context is mostly made of — are the largest
weighted cost component of the measured window (48.5%, ≈$302 of ≈$623; report
§2.1), and the parent-chat levels with the largest packs are also the costliest
per call. The governance pack is a minority of per-call context (~20–40% upper
bound; report finding 7) — but it is the slice this repo's documents control.

---

## 2. Measured composition (the cut list's evidence)

Method: §7. Tokenizer: tiktoken `o200k_base` (the mechanism's Direction B proxy;
G10 error bars apply to every number in this section).

### 2.1 PSG per-section (total 10,443)

| section | tokens | | section | tokens |
|---|---:|---|---|---:|
| (preamble) + §1 Purpose | 145 | | §11 Definition of Done | 112 |
| §1A Canonical Happy Path | 384 | | §11.5 Human Review vs Completion | 664 |
| §2 Core Principles | 123 | | §11.6 Default-Accept (SN-13) | 484 |
| §3 Canonical Repo Structure | 193 | | §12 Delivery Notice | 225 |
| §4 The docs/ Folder | 82 | | §13A Phase Starter (format) | 304 |
| §5 Front-Matter | 169 | | §13B Milestone Starter (format) | 320 |
| §5B Milestone Closure | 1,116 | | §13C Epic Starter (format) | 107 |
| §5C Phase Closure | 1,094 | | §13D Hierarchical Communication | 370 |
| §6 File Naming | 66 | | §14 Tracker Integration | 112 |
| §7 Branch Naming | 56 | | §14A `.ai-project.yml` | 236 |
| §8 Branch Promotion | 213 | | §14B Git Submodule Setup | 129 |
| §8A Unplanned Progress Branches | 921 | | §14C Override System | 1,463 |
| §9 Doc ↔ Branch Alignment | 41 | | §15 Canonical Epic Spec Template | 36 |
| §10 Decision Management | 34 | | §16–§17, Closing | 123 |
| | | | **Changelog** | **738** |

### 2.2 AOG per-section (total 12,080)

| section | tokens | | section | tokens |
|---|---:|---|---|---:|
| (preamble) + §1 Purpose | 139 | | §7 Delivery Enforcement | 241 |
| §1A Happy Path Enforcement | 258 | | §8 External Tracker Semantics | 98 |
| §2 Core Principles | 106 | | §9 Question Policy | 59 |
| §3 intro + §3.1 HQ Chats | 663 | | §10 Completion vs Acceptance | 571 |
| §3.2 Coding Agent Chats | 67 | | §11 Human Review / Review Seal | 345 |
| §3.3 HQ Planning / Unplanned | 871 | | §12 Acceptance Outcomes | 423 |
| §3.4 Milestone Closure | 1,769 | | §13 Exit Ritual | 92 |
| §3.5 Creation Chat | 158 | | §14 Error Handling | 50 |
| §3.6 Phase Execution Chat | 379 | | early dup §13/§14 rows | 85 |
| §3.7 Milestone Execution Chat | 357 | | §16 Visual Artifact Production | 2,259 |
| §3.8 Working-Tree Isolation | 190 | | §15 Closing Statement | 29 |
| §3.9 Scope Direction Protocol | 181 | | **Changelog** | **2,106** |
| §3.10 Communication Protocol | 296 | | | |

### 2.3 What the composition says

1. **Role-irrelevant and dormant content dominates.** The two changelogs alone are
   2,844 tokens (9.7% of PSG+AOG) loaded at every level for zero operating value.
   AOG §3 carries every chat type's rules to every chat: an Epic chat's own
   subsections (§3.2 + §3.8 + §3.10) are 553 of §3's 4,931. AOG §16 (2,259) binds
   only when visual artifacts are due. PSG §5B/§5C (2,210) bind only at closure
   moments; §14C (1,463) only when overrides are declared; §8A (921) only when
   unplanned work arises.
2. **Starter↔spec duplication is real but smaller than hypothesized.** The Epic
   spec named dedup "the likely biggest single win"; measurement says otherwise.
   Verbatim line-level duplication is ~9% of each M30 epic starter (E30.1: 273,
   E30.2: 297, E30.3: 323 tokens) — starters paraphrase rather than copy. The
   *structural* duplication is larger: the epic starter template mandates copying
   Deliverables, DoD, and Acceptance Criteria "EXACTLY from Epic spec" and embeds
   a per-epic Delivery Notice template although
   `governance/templates/delivery-notice.md` (642) exists. Sections whose
   authoritative content is the spec or a committed template, measured on the M30
   starters (Deliverables + DoD + Acceptance Criteria + Technical Constraints +
   embedded DN template): E30.1 = 905, E30.2 = 1,105, E30.3 = 1,120 tokens —
   ~30–33% of each starter.
3. **Parent-spec over-loading:** the milestone pack carries the full phase spec
   (5,268), of which a Milestone Chat's operating need is its own milestone's
   entry plus the phase acceptance criteria (§Milestones 632 + §Acceptance
   Criteria 280 = 912 upper bound; the chat's own entry is a fraction of
   §Milestones).
4. **Milestone/phase starters carry no measurable spec duplication** (verbatim
   dup = 0%): no dedup lever exists there — honesty over magnitude; the lever at
   those levels is PSG/AOG section scoping and parent-spec targeting only.

---

## 3. The per-level scoping standard

### 3.1 Rules

- **Core** = load at session start. **Conditional** = load *when the named
  trigger occurs*, before acting on that situation — skipping a conditional
  section that has triggered is a governance violation, not a token saving.
  **Don't-load** = not needed for the level's role; the full documents remain
  authoritative and available.
- Load by section heading (targeted reads — the harness supports offset/section
  reads and search); do not re-read whole documents to reach one section.
- Chats load their **own spec in full**. Parent/sibling specs are loaded by
  targeted section only (the level's row says which).
- Starters reference their spec's sections instead of restating them
  (load-one-reference-the-other); the spec is the single authoritative copy.
- Never load at any level: PSG/AOG **changelogs** (history, not rules), other
  levels' starter-format sections, other levels' role subsections of AOG §3.

### 3.2 Epic Execution Chat (Coding Agent)

Role: execute one epic spec end-to-end, deliver, stop (AOG §3.2; PSG §1A).

| load | content | proxy tokens |
|---|---|---:|
| Core | own starter (reduced form, §4) + own epic spec (full) | starter ≈2.7K + spec |
| Core | PSG: preamble+§1, §1A, §2, §5, §6, §7, §8, §9, §11, §11.5, §11.6, §12 | 2,682 |
| Core | AOG: preamble+§1, §1A, §2, §3.2, §3.8, §3.10, §4, §5, §6, §7, §9, §10, §12, §13 Exit Ritual, §14 Error Handling | 2,780 |
| Conditional | PSG §3 (creating new docs/ areas); §8A (unplanned work arises); §10 (recording decisions); §13D (escalation beyond the DN path); §14A (task touches `.ai-project.yml`); §14C (overrides declared); §18 (agentic cluster mode). AOG §3.9 (scope direction changes mid-flight); §8 (tracker declared); §11 (exception-path review invoked); §16 (epic has visual-artifact deliverables) | 0 unless triggered |
| Don't-load | PSG §4, §5B, §5C, §13A–§13C, §14, §14B, §15–§17, changelog; AOG §3.1, §3.3–§3.7, §15, changelog | — |

Why: an epic chat executes and stops. It closes nothing (milestone/phase closure
are parent acts), produces no starters, and reads no sibling specs. §11.5/§11.6
are core because the stop-and-await-acceptance contract is the role's most
violated edge; §12 because the DN is its closing deliverable.

### 3.3 Milestone Execution Chat

Role: Stage 1 plan epics (specs + starters), Stage 2 oversee delivery, accept by
silence, merge on human authorization (AOG §3.7; PSG §11.6).

| load | content | proxy tokens |
|---|---|---:|
| Core | own starter + own milestone spec (full) | starter + 5,230 |
| Core | phase spec: own milestone's entry in §Milestones + §Acceptance Criteria only | ≤912 |
| Core | PSG: preamble+§1, §1A, §2, §5, §6, §7, §8, §9, §10, §11, §11.5, §11.6, §12, §13C (it writes epic starters), §15 | 2,859 |
| Core | AOG: preamble+§1, §1A, §2, §3.7, §3.9, §3.10, §4, §5 (binding contract of the starters it writes), §6, §7, §9, §10, §12, §13 Exit Ritual, §14 Error Handling | 3,061 |
| Conditional | PSG §5B + AOG §3.4 (at milestone-closure time); PSG §3, §8A, §13D, §14A, §14C, §18; AOG §3.2 (dispatch questions about the child role), §8, §11, §16 (milestone has visual bindings due) | 0 unless triggered |
| Don't-load | rest of phase spec; PSG §4, §5C, §13A, §13B, §14, §14B, §16–§17, changelog; AOG §3.1, §3.3, §3.5, §3.6, §3.8, §15, changelog | — |

Why: the costliest level of the measured window (37% of spend, report §2.2). It
needs the epic-facing format contracts (PSG §13C, §15; AOG §5) because its
deliverables are epic specs and starters; it does not need its own starter-format
section (§13B — already consumed by its parent) or the full phase spec, and the
closure machinery (2,885 tokens across PSG §5B + AOG §3.4) is needed exactly
once, at the end.

### 3.4 Phase Execution Chat

Role: Stage 1 plan milestones, Stage 2 oversee milestone delivery, merge on
human authorization (AOG §3.6).

| load | content | proxy tokens |
|---|---|---:|
| Core | own starter + own phase spec (full) | starter + 5,268 |
| Core | PSG: preamble+§1, §1A, §2, §5, §6, §7, §8, §9, §10, §11, §11.5, §11.6, §12, §13B (it writes milestone starters), §13D | 3,406 |
| Core | AOG: preamble+§1, §1A, §2, §3.6, §3.9, §3.10, §4, §6, §7, §9, §10, §12, §13 Exit Ritual, §14 Error Handling | 2,931 |
| Conditional | PSG §5B + AOG §3.4/§3.7 (during a milestone's closure); PSG §5C (at phase-closure time); PSG §3, §8A, §14A, §14C, §18; AOG §8, §11, §16 | 0 unless triggered |
| Don't-load | milestone/epic specs except by targeted section during review; PSG §4, §13A, §13C, §14, §14B, §15–§17, changelog; AOG §3.1–§3.3, §3.5, §3.8, §15, changelog | — |

Why: same shape as milestone one level up; costliest per-call median (169,003).
§13D is core (it is the hierarchy's main relay). AOG §5 is not core — the epic
starter contract is its grandchild's surface (adjacency).

### 3.5 HQ Chat and Creation Chat (for the record)

Both are **manual at all times** (SN-22) and neither has a mechanism-defined
pack: dataset §4 defines packs only for phase/milestone/epic, and HQ/Creation
sessions boot from an opener/seed rather than starter+spec. Their rows are
therefore qualitative, and the absence of a measured pack is recorded as **G13**
(§6). Guidance from role definitions: HQ (AOG §3.1, §3.3) loads PSG §1A, §2,
§8/§8A, §11.5/§11.6, §12, §13A–§13D and AOG §3.1/§3.3/§3.9/§3.10 plus the
artifact it is currently routing — not the full corpus, and never the
changelogs. Creation (AOG §3.5) loads its seed and the product-vision context it
is working from; governance beyond PSG §2 and the artifact formats it emits is
below its altitude. No reduction is *claimed* for these levels.

---

## 4. Implemented reduction and before/after evidence

### 4.1 What was changed (the surfaces)

1. **`governance/templates/epic-execution-chat-starter.md`** — the Deliverables /
   Definition of Done / Acceptance Criteria / Technical Constraints placeholder
   sections (content the template previously ordered copied "EXACTLY" from the
   spec) are replaced by a single **Spec References** section
   (load-one-reference-the-other); the embedded Delivery Notice template and
   front-matter schema blocks are replaced by references to
   `governance/templates/delivery-notice.md` and the spec templates; a **Context
   Scoping** block carries the §3.2 load list.
2. **`governance/templates/milestone-execution-chat-starter.md`** — a **Context
   Scoping** block carries the §3.3 load list, including the
   phase-spec-by-targeted-section rule.
3. **`governance/templates/phase-execution-chat-starter.md`** — a **Context
   Scoping** block carries the §3.4 load list.

M30's already-delivered starters are left as delivered (they are consumed
artifacts; the standard governs future chats). PSG/AOG normative content is
untouched — every reduction here changes what is *loaded*, not what is *ruled*.

### 4.2 Before/after pack measurements (Direction B, o200k proxy, G10 ±10–15%)

"Before" = the mechanism's committed pack definitions (dataset §4, reproduced by
rerun 2026-07-18). "After" = the §3 load lists applied to the same corpus, with
component arithmetic shown. The epic row uses E30.1's starter/spec as the
measured instance (the mechanism's own pack definition).

| level | before | after | Δ | components of "after" |
|---|---:|---:|---:|---|
| epic | 29,336 | **12,005** | **−59%** | starter 2,727 (= 2,997 − 905 spec-redundant/DN-embed sections + 264 Spec References + 117 DN pointer + 254 scoping block) + spec 3,816 + PSG core 2,682 + AOG core 2,780 |
| milestone | 36,614 | **15,971** | **−56%** | starter 3,909 (= 3,593 + 316 scoping block) + milestone spec 5,230 + phase-spec targeted 912 + PSG core 2,859 + AOG core 3,061 |
| phase | 30,478 | **14,586** | **−52%** | starter 2,981 (= 2,687 + 294 scoping block) + phase spec 5,268 + PSG core 3,406 + AOG core 2,931 |

Every component above is a measured tokenization of committed text (per-section
tables in §2; method in §7); the reference/scoping block figures are the measured
sizes of the blocks this delivery added to the templates. The template files
themselves measure: epic 3,183 → 2,710 (−473, net of the dedup cuts and the
added blocks); milestone 2,320 → 2,636 (+316); phase 2,130 → 2,424 (+294) — the
milestone/phase template files *grow* by their scoping blocks while the packs
their instructions assemble shrink by ~20.6K/15.9K; the reduction lives in the
instructed load, not the template file size.

### 4.3 What these numbers are — and are not (claims vs evidence)

- These are **pack-level proxy measurements** of what a compliant future chat is
  instructed to load. They are reproducible by rerunning the method in §7.
- They are **not billed numbers and not achieved savings.** Billed per-call
  medians (dataset §3) can only move in future captured sessions, and the
  realized effect depends on chats actually performing targeted section reads
  and on conditional sections' trigger frequency. **Billed-median improvement is
  a forward-looking expectation, to be verified by a future capture with E30.1's
  mechanism** — that verification is recommended to M31 (§5).
- Conditional loads are counted at 0 in §4.2 by definition of "session-start
  load"; a session that triggers conditionals loads more, correctly. The
  before-numbers equally exclude on-demand reads, so the comparison is
  like-for-like at session start.

---

## 5. Bounded-scope finding — what reduction cannot address

**Finding: the majority of per-call context lies beyond document control, and the
dominant cost lever M30 found is behavioral, not documentary.**

1. **Share beyond documents.** The full governance pack was at most ~20–40% of
   billed per-call re-read (report finding 7: 29–37K proxy packs against 76–169K
   billed medians, upper bound assuming the whole pack persists in context). The
   remainder — conversation history, tool results, harness system prompt and
   memory (~15–20K billed on first turn, dataset §3) — is produced by session
   *behavior*, not by governance files. After this epic's reduction the
   instructed pack is 12.0–16.0K proxy tokens, i.e. an upper-bound ~9–15% of
   current per-call medians: **even perfect pack scoping leaves ≥60–80% of
   per-call context untouched.** (Proxy-over-billed ratios; G10 bars apply.)
2. **The dominant sink is session length and mixing (G7).** Parent-chat mixed
   sessions are 53% of window spend (milestone 37% + phase 16.1%; medians
   $11.71–$20.84 per session vs $2.92 for a bounded epic execution — report
   §2.2). Cost grows with per-call context × call count; long mixed sessions
   maximize both. No document edit shortens a session.
3. **Recommendations** (findings handed upward — not implemented work):
   - **To M31 (session hygiene, with the binding-order guardrail work):** adopt a
     one-task-one-session discipline at parent levels — open a fresh session per
     task type (planning / review / closure) instead of one long mixed session;
     E30.2 §2.2's medians say this is the largest addressable component of
     spend. Codify it as guidance in M31's dual-mode/guardrail deliverables
     (candidate home: the session-conduct surfaces M31 already owns per the
     phase spec — G7/§2.2 is the evidence).
   - **To M31 (verification):** after M31's parent sessions run under the new
     scoping + E30.4's reference-don't-display, rerun `bin/measure-token-burn`
     and compare per-call medians against dataset §3 — the forward-looking
     verification this epic cannot perform on itself (§4.3).
   - **To the Phase Chat:** within-session task segmentation in
     `bin/measure-token-burn` remains recorded future *measurement* work (report
     §8) — precision, not reduction; unowned as of E30.3. E30.4 (already
     specced) owns the complementary lever this finding cannot reach by scoping:
     governance-mandated echo of artifact bodies into session history.

---

## 6. Gap records (continuing the G-series)

- **G13 (gap; hq/creation packs):** No mechanism-defined or measured load pack
  exists for the HQ and Creation levels (dataset §4 defines packs for
  phase/milestone/epic only; HQ/Creation boot from opener/seed, are manual by
  design per SN-22, and write no starter+spec pair to measure). §3.5's guidance
  is role-derived and qualitative; no reduction is claimed for those levels.
  Revisit only if those levels ever gain mechanism-measurable packs.

Carried unchanged: G1–G10 (dataset §6), G11–G12 (report §6). G10 governs every
proxy number in this document.

---

## 7. Reproduction method (Design Decision 3 record)

**Decision: separate committed before/after evidence (this document), citing the
mechanism — `bin/measure-token-burn` unchanged.** Reasons: (a) regenerating the
dataset files would rerun Direction A over a session window that has moved since
2026-07-17, mutating the paid-session sections that the E30.2 audit report cites
as its sole frozen evidence base; (b) the mechanism's pack definitions are
E30.1's measured record of the *pre-reduction* state — exactly the "before" this
document cites; embedding the post-reduction scoping into the mechanism would
overwrite the baseline it is being compared against. The mechanism README's
future-work notes are unaffected.

To reproduce every §2/§4 number:

```bash
python3 -m venv /tmp/tokenv && /tmp/tokenv/bin/pip install tiktoken
```

```python
# /tmp/tokenv/bin/python — run from the repo root
import re, tiktoken
enc = tiktoken.get_encoding("o200k_base")
tok = lambda s: len(enc.encode(s, disallowed_special=()))

def sections(path, pat=r"^## "):        # fence-aware top-level split
    out, cur, buf, fence = [], "(pre)", [], None
    for ln in open(path, encoding="utf-8", errors="replace").read().split("\n"):
        m = re.match(r"^(`{3,}|~{3,})", ln)
        if m:
            f = m.group(1)
            if fence is None: fence = f
            elif len(f) >= len(fence) and f[0] == fence[0]: fence = None
            buf.append(ln); continue
        if fence is None and re.match(pat, ln):
            out.append((cur, tok("\n".join(buf)))); cur, buf = ln.strip(), [ln]
        else: buf.append(ln)
    out.append((cur, tok("\n".join(buf))))
    return out
# file totals: tok(open(p).read()) — matches dataset §4 (PSG 10,443; AOG 12,080)
# per-section tables (§2.1/§2.2): sections("governance/PROJECT-SYSTEM-GUIDELINES.md")
#   (AOG §3 subsections: extract §3's line span, split with pat=r"^### ")
# verbatim duplication (§2.3): normalize lines (collapse whitespace, lowercase),
#   keep lines >25 chars, sum tok(line) of starter lines present in its spec
# pack sums (§4.2): sum the named components from the tables above
```

The "before" pack numbers are additionally reproducible with the mechanism
itself: `bin/measure-token-burn` (Direction B `level_packs`) — its committed
definitions are the pre-reduction packs.

---

## 8. Design-decision record

- **DD1 (home):** this file, beside the dataset/report — the E30.1→E30.3
  evidence chain stays in one directory, per the Epic spec's recommendation. The
  templates carry self-contained load lists so `governance/` remains portable to
  adopting repos (which do not receive `.ai-project/artifacts/`); this document
  is cross-linked from the directory README.
- **DD2 (lever per level):** PSG/AOG **section scoping** everywhere (the
  measured dominant component: 62–77% of every pack; §2.3.1). **Template dedup**
  at the epic level only, where the duplication is measured (§2.3.2); milestone/
  phase starters measured 0% verbatim duplication, so no dedup lever is claimed
  there. **Parent-spec targeting** at the milestone level (912 vs 5,268
  measured; §2.3.3). The spec's dedup-first hypothesis is corrected by
  measurement — recorded openly in §2.3.2.
- **DD3 (presentation):** separate committed table, mechanism cited, dataset
  files untouched — rationale in §7.
