# Visual Artifacts — Integration Guide

Visual artifacts let each chat level produce an image, diagram, or video appropriate to its level of
abstraction. The capability is **default-on**: it is active unless a project explicitly opts out
with `visual_artifacts.enabled: false`. This guide covers the capability's config, opting out, the
two production modes, the `bin/ai-project-visual` helper, output formats, and a worked example for
every chat level.

| | |
|---|---|
| **Audience** | Adopters enabling visual generation; tool-capable agents producing visuals |
| **Configuration spec** | [`../ai-project-yml-spec.md`](../ai-project-yml-spec.md) §3.5 |
| **Operating policy** | [`../AI-OPERATING-GUIDELINES.md`](../AI-OPERATING-GUIDELINES.md) §16 |
| **Helper** | [`../../bin/ai-project-visual`](../../bin/ai-project-visual) |

---

## 1. Configuring the capability

The capability is active with no `.ai-project.yml` block at all. To customize it, or to opt out, add
a `visual_artifacts` block to your project's `.ai-project.yml`:

```yaml
visual_artifacts:
  enabled: true                       # default-on; absent or true ⇒ enabled, false ⇒ opt-out
  comfyui_url: http://localhost:8188  # your ComfyUI endpoint (http/https)
  types:                              # subset of the allowed types
    - diagrams
    - infographics
    - video
  visual_required_for_specs: true     # enforcement setting; defaulted true
```

- **`enabled`** (bool) — the master switch. Absent block or `true` means the capability is on;
  explicit `false` opts out and the helper exits with a clear "disabled" message.
- **`comfyui_url`** (URL) — a well-formed `http(s)` endpoint for a reachable ComfyUI instance.
  Standing up that endpoint is the **CFO's** responsibility, not the framework's.
- **`types`** (list) — any subset of `diagrams`, `infographics`, `video`. The helper refuses a
  `--type` that is not listed.
- **`visual_required_for_specs`** (bool) — enforcement setting, defaulted `true`; governs whether
  specs are required to carry a visual. It does not decide which artifact types are automatic.

The full schema, defaults, and validation rules live in
[`ai-project-yml-spec.md`](../ai-project-yml-spec.md) §3.5. The block is read through a single source
— `bin/ai-project-orchestrator`'s `load_yml_config()` / `resolve_visual_artifacts()` — so the helper,
the orchestrator, and the tests never disagree about the effective config.

> **No** project commits generated binaries — the rule is universal and holds whether or not the
> capability is enabled. The governance **source** repository runs with `enabled: true` (since Epic
> E29.2) and still commits no generated output: it ships the guidance, the helper, and the test, and
> references generated artifacts by link like every other adopter.

---

## 2. The two modes

### Structural (Mermaid / PlantUML)

Diagrams expressed as **text**, committed alongside the artifact they illustrate. No endpoint and no
tool capability beyond writing a fenced code block are required. Prefer structural mode for
architecture, scope, component, and flow diagrams — anything whose meaning is its structure.

````markdown
```mermaid
flowchart LR
    Creation[Creation Chat] --> HQ[HQ Chat]
    HQ --> Phase[Phase Chat] --> Milestone[Milestone Chat] --> Epic[Epic Chat]
```
````

PlantUML is equally acceptable where your renderer supports it:

```plantuml
@startuml
[Creation Chat] --> [HQ Chat]
[HQ Chat] --> [Phase Chat]
@enduml
```

Commit structural diagrams **inline** in the governing artifact, or as a sibling `.mmd` / `.puml`
file next to it.

### Generative (ComfyUI)

Imagery or video produced from a natural-language prompt via the configured ComfyUI endpoint, using
the `bin/ai-project-visual` helper. Prefer generative mode for concept/vision imagery, infographics,
and UI mockups — anything where a rendered image communicates better than a diagram.

---

## 3. The `bin/ai-project-visual` helper

A minimal, callable **prompt → artifact** path for any tool-capable agent. One prompt, one artifact:
no queue, no batch, no UI.

```
ai-project-visual --prompt "<text>" --type <type> --output <path> [--workflow graph.json]
                  [--checkpoint NAME] [--width N] [--height N] [--seed N] [--timeout S]
```

| Flag | Meaning |
|------|---------|
| `--prompt` (required) | Natural-language prompt for the visual. |
| `--type` (required) | One of the configured `visual_artifacts.types`. |
| `--output` (required) | Local working file to write the artifact to, then host and link — not a committed path (parent dirs are created). |
| `--workflow` | A ComfyUI **API-format** workflow JSON. Required for non-image types (e.g. `video`). The literal token `%prompt%` in the file is replaced with `--prompt`. |
| `--checkpoint` | Checkpoint name for the built-in text-to-image workflow (must exist on the server). |
| `--width` / `--height` / `--seed` | Built-in-workflow image dimensions and sampler seed. |
| `--timeout` | Generation timeout in seconds (default 120). |

Run it from the project root (it reads that project's `.ai-project.yml`):

```bash
# --output is a local working file — host it on your storage backend and link it; do not commit it.
ai-project-visual \
  --prompt "isometric system architecture diagram, clean, labelled services" \
  --type diagrams \
  --output ./architecture.png
```

When no `--workflow` is given, the helper submits a standard text-to-image graph (CheckpointLoader →
CLIP encode → KSampler → VAE decode → SaveImage) with your prompt injected, polls `/history`, and
downloads the result via `/view`. For `video` or any bespoke pipeline, supply your own graph with
`--workflow` and mark the prompt insertion point with `%prompt%`.

### Exit codes

| Code | Meaning |
|------|---------|
| `0` | Success — artifact written to `--output`. |
| `2` | Capability disabled (explicit `enabled: false`). |
| `3` | Configuration error — invalid endpoint, `--type` not in `types`, or missing `--workflow`. |
| `4` | Runtime error — endpoint unreachable, generation failed, or no output produced. |
| `5` | Execution locked — a live agentic epic execution holds `bin/ai-project-orchestrator`'s execution lock; the call is refused to avoid GPU contention with live Ollama inference. See [`gpu-coexistence.md`](gpu-coexistence.md). |

Each failure prints a one-line, actionable message to stderr.

---

## 4. Output formats

| Mode | Typical format(s) | Where it comes from |
|------|-------------------|---------------------|
| Structural | `.mmd`, `.puml`, or inline fenced block | Authored by the agent |
| Generative — image | `.png` (default ComfyUI `SaveImage`) | `/view?type=output` |
| Generative — video | `.webp` / `.mp4` / `.gif` per your workflow | `/view` (gifs/videos output) |

Generated artifacts are **referenced by link, never committed to git.** The helper writes a local
working file; host it on your storage backend — the **adopter owns the storage backend** — and
reference it by link from the governing artifact, so the **link**, not the binary, travels with the
decision record. Where generated binaries live is the adopting team's decision; the framework is
infrastructure-agnostic about storage just as it is about endpoints.

---

## 5. Per-level worked examples

Each chat level produces the visual appropriate to its altitude (the SN-11 abstraction). An agent
produces the visual for **its own** level — it does not reach up or down the cascade. Visual intent
originates at the Creation Chat (elicited via `seed.md` Rule 4) and propagates downward.

Per **AOG §16.6**, when the capability is enabled each level produces **both** a *proposed* visual
(the intent, before build) and an *implemented* visual (what was built, after). Every example below
shows that pair, and each is recorded as a **§7 binding** distinguished by its `State` field —
`proposed` or `implemented`. The binding schema is documented once in §7; these examples *use* it,
they do not restate it. A pair is the **same block in two states** — it differs by `State` (and,
where the medium changes from mockup to screenshot, by `What`). Most pairs are two cheap Structural
diagrams (Mermaid / PlantUML); only Creation and Epic reach for Generative, where a render
communicates better — that Structural-first economy is what keeps "nothing is too much" affordable.

In the generative examples below, `--output` names a **local working file**: host it on your storage
backend and bind it by **link** — it is not committed to git. Structural diagrams live inline (free);
their binding `Link` is a hosted permalink to the committed diagram, never a local path.

### Creation Chat — concept / vision imagery

> *Generative.* Capture the look and feel of the finished product — proposed before build, implemented
> from the shipped UI.

**Proposed** — the intended look and feel, before anything is built:

```bash
ai-project-visual \
  --prompt "warm, approachable mobile budgeting app hero image, soft gradients, friendly" \
  --type infographics \
  --output ./vision.png
```

**Visual binding** (schema in §7)
- **Link:** https://files.example.com/acme/creation/vision-proposed.png
- **What:** image
- **Level:** Creation
- **State:** proposed
- **Description:** Concept render of the budgeting app's intended warm, approachable feel.

**Implemented** — a render captured from the shipped product:

**Visual binding** (schema in §7)
- **Link:** https://files.example.com/acme/creation/vision-implemented.png
- **What:** image
- **Level:** Creation
- **State:** implemented
- **Description:** Hero screenshot of the shipped app — soft gradients delivered as proposed.

### HQ Chat — system architecture

> *Structural.* Two text diagrams — the target architecture, then the one actually built.

**Proposed** — the intended architecture:

```mermaid
flowchart TB
    Client --> API[API Gateway]
    API --> Auth[Auth Service]
    API --> Core[Core Service]
    Core --> DB[(Database)]
```

**Visual binding** (schema in §7)
- **Link:** https://github.com/acme/app/blob/v1/docs/hq-architecture.md#proposed
- **What:** diagram
- **Level:** HQ
- **State:** proposed
- **Description:** Target architecture — a gateway fronting auth + core over one database.

**Implemented** — the architecture as built (a cache was added under load):

```mermaid
flowchart TB
    Client --> API[API Gateway]
    API --> Auth[Auth Service]
    API --> Core[Core Service]
    Core --> Cache[(Cache)]
    Core --> DB[(Database)]
```

**Visual binding** (schema in §7)
- **Link:** https://github.com/acme/app/blob/v1/docs/hq-architecture.md#implemented
- **What:** diagram
- **Level:** HQ
- **State:** implemented
- **Description:** Shipped architecture — a cache was added between core and the database.

### Phase Chat — phase scope diagram

> *Structural.* What was planned in/out of the phase, then what actually landed.

**Proposed** — intended scope:

```mermaid
flowchart LR
    subgraph In Scope
        A[Ingestion] --> B[Normalization]
    end
    subgraph Out of Scope
        C[Reporting]
    end
```

**Visual binding** (schema in §7)
- **Link:** https://github.com/acme/app/blob/v1/docs/phase2-spec.md#scope-proposed
- **What:** diagram
- **Level:** Phase
- **State:** proposed
- **Description:** Phase 2 planned scope — ingestion + normalization in, reporting out.

**Implemented** — scope as delivered (reporting pulled in, validation deferred):

```mermaid
flowchart LR
    subgraph Delivered
        A[Ingestion] --> B[Normalization] --> C[Reporting]
    end
    subgraph Deferred
        D[Validation]
    end
```

**Visual binding** (schema in §7)
- **Link:** https://github.com/acme/app/blob/v1/docs/phase2-spec.md#scope-implemented
- **What:** diagram
- **Level:** Phase
- **State:** implemented
- **Description:** Phase 2 as delivered — reporting landed; validation deferred to phase 3.

### Milestone Chat — component + flow diagrams

> *Structural.* The intended flow, then the flow as built.

**Proposed** — intended request flow:

```mermaid
sequenceDiagram
    User->>UI: submit form
    UI->>API: POST /record
    API->>DB: insert
    DB-->>API: ok
    API-->>UI: 201 Created
```

**Visual binding** (schema in §7)
- **Link:** https://github.com/acme/app/blob/v1/docs/m4-spec.md#flow-proposed
- **What:** diagram
- **Level:** Milestone
- **State:** proposed
- **Description:** Planned record-creation flow — UI to API to DB, 201 on success.

**Implemented** — flow as built (a validation step was added before insert):

```mermaid
sequenceDiagram
    User->>UI: submit form
    UI->>API: POST /record
    API->>API: validate
    API->>DB: insert
    DB-->>API: ok
    API-->>UI: 201 Created
```

**Visual binding** (schema in §7)
- **Link:** https://github.com/acme/app/blob/v1/docs/m4-spec.md#flow-implemented
- **What:** diagram
- **Level:** Milestone
- **State:** implemented
- **Description:** Built flow — a server-side validation step was added before insert.

### Epic Chat — UI mockups, before/after, implementation diagrams

> *Generative.* A mockup of the intended screen, then the screen as shipped.

**Proposed** — a mockup of the intended screen, before build:

```bash
ai-project-visual \
  --prompt "clean settings screen mockup, toggle list, light theme, mobile" \
  --type diagrams \
  --output ./E12.3-settings-mockup.png
```

**Visual binding** (schema in §7)
- **Link:** https://files.example.com/acme/epic/E12.3-settings-proposed.png
- **What:** mockup
- **Level:** Epic
- **State:** proposed
- **Description:** Proposed settings screen — toggle list, light theme, mobile.

**Implemented** — a screenshot of the built screen:

**Visual binding** (schema in §7)
- **Link:** https://files.example.com/acme/epic/E12.3-settings-implemented.png
- **What:** image
- **Level:** Epic
- **State:** implemented
- **Description:** Shipped settings screen — toggle list as proposed; a search field was added.

---

## 6. Testing without a live endpoint

The integration test under [`../../tests/integration/`](../../tests/integration/) exercises the
helper against the configured endpoint. It reads the effective config through the same resolver as
the helper, so a project's suite never disagrees with its config about whether the endpoint test
should run. Two paths keep the suite green without a reachable ComfyUI instance:

- **Projects with the capability off** — the endpoint test **skips when `visual_artifacts.enabled` is
  `false`**. Set `enabled: true` and point `comfyui_url` at a reachable server to make it run.
- **Contributors and CI on a project that has it on** — set
  `AI_PROJECT_SKIP_LIVE_ENDPOINT_TESTS=1` to skip that one test on a machine without a reachable
  endpoint. Unset (the default) still runs it and requires the endpoint.

In *this* repository the capability is enabled (`enabled: true`, since Epic E29.2) and the endpoint
test therefore **runs for real by default** against the live local endpoint — it is not skipped here
unless a contributor opts out via that environment variable.

---

## 7. Binding a visual to an artifact

Under by-link (§4), the only thing that lands in git is a **link** — and a bare link rots: the host
moves, the file is renamed, the URL 404s, and the decision record loses the visual it referenced. A
**binding** is the small, load-bearing record that travels with the decision in the binary's place —
the link plus four metadata fields that outlive it. A binding always records a **link, never a
committed `.ai-project/visuals/...` path** — committing the binary is exactly what §4 reversed.

### The binding schema

A visual binding has five elements:

| Element | Meaning |
|---------|---------|
| **Link** | The hosted URL of the generated visual (**required**; never a committed path). |
| **What** | The visual's kind: `image` / `infographic` / `mockup` / `diagram` / `clip`. |
| **Level** | The governance level it binds to: `Creation` / `HQ` / `Phase` / `Milestone` / `Epic`. |
| **State** | The two-track state: `proposed` (before build) or `implemented` (after). |
| **Description** | Short text that survives link rot — what the visual shows and why. |

Record a binding as a labeled block:

```markdown
**Visual binding**
- **Link:** <hosted URL>
- **What:** image | infographic | mockup | diagram | clip
- **Level:** Creation | HQ | Phase | Milestone | Epic
- **State:** proposed | implemented
- **Description:** <short text that survives link rot>
```

**State is a field, not a second schema.** A level may carry both a `proposed` binding (the visual
intent, before build) and an `implemented` binding (what was actually built) — the same five-element
block, distinguished by **State**. Record as many bindings as a level needs; omit the binding
entirely when a level has no visual.

### Where a binding lives — per-level placement

A binding attaches to the **governing artifact of its level**, so the link sits beside the decision
it illustrates. Each level has a defined home:

| Level | Artifact | Where the binding goes |
|-------|----------|------------------------|
| Creation | [`../templates/seed.md`](../templates/seed.md) | The Project Brief's **_Visual success_** element (Rule 4), where visual intent is already elicited. |
| HQ | [`../templates/genesis.md`](../templates/genesis.md) | The **HQ Context Packet**, beside the system-architecture record. |
| Phase | [`../templates/phase-spec.md`](../templates/phase-spec.md) | The **Visual Bindings** section. |
| Milestone | [`../templates/milestone-spec.md`](../templates/milestone-spec.md) | The **Visual Bindings** section. |
| Epic | [`../templates/epic-spec.md`](../templates/epic-spec.md) | The **Visual Bindings** section. |
| Epic (delivery) | [`../templates/delivery-notice.md`](../templates/delivery-notice.md) | The **Visual Bindings** section. |
| Epic (closure) | [`../templates/epic-closure-notice.md`](../templates/epic-closure-notice.md) | The **Visual Bindings** section. |
| Milestone (closure) | [`../templates/milestone-closure-declaration.md`](../templates/milestone-closure-declaration.md) | The **Visual Bindings** section. |
| Phase (closure) | [`../templates/phase-closure-declaration.md`](../templates/phase-closure-declaration.md) | The **Visual Bindings** section. |

The last four rows are the **delivery/closure** half of the automatic trigger set (§9) —
`delivery-notice.md` and `epic-closure-notice.md` are both Epic-level artifacts and get adjacent
rows rather than sharing one, consistent with one row per artifact file elsewhere in this table.

An agent records the binding for **its own** level only — it does not reach up or down the cascade
(the altitude rule from §5). Visual intent still originates at the Creation Chat (`seed.md` Rule 4)
and propagates downward; this convention formalizes how the resulting link + metadata is recorded at
each level the intent reaches. The schema is documented **once, here** — each template's home
references it rather than restating it.

---

## 8. Clips

A **clip** is a short video that renders **one** governance node's proposed→implemented arc (§5, AOG
§16.6) as motion. It is the most CFO-facing visual — a few seconds that let the CFO follow a node's
story — and it doubles as publishable media. A clip is **single-parent** (AOG §16.7): it binds to
exactly one node via a §7 binding with `What: clip`; it does **not** stitch many nodes into a
cross-cutting reel (that montage is deferred in P6).

### Producing a clip from the arc

A clip is produced on the **verified LTX-Video path — no new plumbing.** The `--type video --workflow`
capability already exists in [`../../bin/ai-project-visual`](../../bin/ai-project-visual), and the
LTX-Video workflow is verified end-to-end (`ltxv-video.json` → valid `.webm`):

```bash
ai-project-visual \
  --prompt "<the node's proposed→implemented story, e.g. the settings screen's before→after>" \
  --type video --workflow <ltxv-video graph> \
  --output ./E12.3-arc.webm
```

The **exact command, the workflow graph, and the verified parameters** (LTX-Video defaults: 768×512,
97 frames @ 25 fps) live in the preserved reference bundle — see
[`../../.ai-project/artifacts/reference/comfyui-endpoint/VISUAL-ARTIFACTS.md`](../../.ai-project/artifacts/reference/comfyui-endpoint/VISUAL-ARTIFACTS.md)
and its `ltxv-video.json`. **Cite the bundle; do not re-transcribe or ship the workflow** — the
framework references the CFO-side contract, it does not vendor it (see *Open Design Question A* below).

### Binding a clip

A clip is bound like any other visual — a **§7 binding** — with `What: clip` and `Level` set to the
one node it narrates. Its **Link** is the hosted URL of the `.webm`, **never a committed path**
(by-link, §4). A clip narrates the whole arc, so it reads most naturally as an `implemented` binding
(it exists once the arc is real); this is a wording choice, not a new `State` value.

**Visual binding** (schema in §7)
- **Link:** https://files.example.com/acme/epic/E12.3-arc.webm
- **What:** clip
- **Level:** Epic
- **State:** implemented
- **Description:** 4-second clip of E12.3's settings-screen arc — the proposed mockup dissolving into the shipped screen.

### Publishing a clip

Publishing to YouTube / TikTok / Instagram / Facebook is **the same hosted asset reused** — not a
second render and not a separate production. The clip is already hosted (that is what by-link
requires), and the hosted link is what gets published. The framework **documents this path; it does
not build a publisher, a pipeline, or host the asset** — where a clip is hosted and how it reaches a
social channel is the adopter's decision (infrastructure-agnostic, consistent with §4 / AOG §16.5).

### Open Design Question A — resolved: reference, not vendor

The workflow JSONs and the models behind them are the CFO's generative-request contract and **stay
CFO-side.** The framework's documented reference is the **preserved bundle** at
`.ai-project/artifacts/reference/comfyui-endpoint/` (`ltxv-video.json`, `VISUAL-ARTIFACTS.md`, and the
sibling image workflows); this guide **references** that bundle rather than shipping a runnable
`workflows/` directory in-repo. Production points at the verified contract — it does not re-home or
re-implement it.

---

## 9. Automatic vs. on-demand production (the trigger set)

The capability is on by default (§1, AOG §16.1) — this section states what "on" actually produces,
and when.

**Structural-first at zero infrastructure.** With no `comfyui_url` configured, only Structural
visuals (§2) are produced; Generative activates only once an endpoint is present and the agent has
tool capability (AOG §16.4). This is the same mode split and gate documented in §2 above — this
section adds no new machinery, only states which path fires by default.

**The automatic trigger set.** Two artifact families get a visual automatically, with no request
required:
- **Specs** — Phase spec, Milestone spec, Epic spec.
- **Delivery/closure declarations** — Delivery Notice, Epic Closure Notice, Milestone Closure
  Declaration, Phase Closure Declaration.

Every other artifact type — steering note, progress digest, merge authorization, escalation notice,
run record, and anything else not named above — is **on-demand only**: an adopter or agent asks for
it explicitly, in the proper chat, pointing at the artifact file. Do not infer automatic production
for an artifact type outside this list.

All eight automatic-trigger artifact types have a defined binding home in the §7 placement table —
the four delivery/closure rows close a gap the original five spec-only rows left open.

This is the adopter-facing restatement of AOG §16.8; the normative rule lives there.

---

## Related documents

| Document | Purpose |
|----------|---------|
| [`../ai-project-yml-spec.md`](../ai-project-yml-spec.md) §3.5 | The `visual_artifacts` config block (schema + validation) |
| [`../AI-OPERATING-GUIDELINES.md`](../AI-OPERATING-GUIDELINES.md) §16 | Operating policy: per-level abstraction, modes, gating, by-link storage guidance |
| [`../templates/seed.md`](../templates/seed.md) | Rule 4 — visual-intent elicitation at inception |
| [`../../bin/ai-project-visual`](../../bin/ai-project-visual) | The ComfyUI helper |
| [`gpu-coexistence.md`](gpu-coexistence.md) | Ollama + ComfyUI GPU/VRAM coexistence design; the execution-lock guardrail (exit code `5`) |

---

## Changelog

| Date | Change |
|------|--------|
| 2026-07-13 | **Execution-lock guardrail exit code (`5`) added.** `bin/ai-project-visual` now refuses a generative call while a live agentic epic execution holds `bin/ai-project-orchestrator`'s execution lock (GPU contention with live Ollama inference) — new exit code `5` added to the §3 exit-code table, and a new "Related documents" row for [`gpu-coexistence.md`](gpu-coexistence.md), the new guide documenting the confirmed Ollama+ComfyUI contention and the guardrail design. No other section changed. Per SN-18; E27.3 (P7-M27). |
| 2026-07-13 | **Trigger-set behavior (§9) added.** New §9 "Automatic vs. on-demand production (the trigger set)": adopter-facing restatement of AOG §16.8 — structural-first at zero infrastructure (cross-referencing §2/AOG §16.4, no new machinery), and the automatic trigger set (Phase/Milestone/Epic specs + the four delivery/closure declarations automatic; everything else on-demand). Extended the §7 placement table with four new rows (`delivery-notice.md`, `epic-closure-notice.md`, `milestone-closure-declaration.md`, `phase-closure-declaration.md`), closing the gap where the delivery/closure half of the trigger set had no defined binding home; the existing five spec rows are unchanged. Appended as §9, following the §8 precedent — §1-§8 not renumbered. Per SN-17 (ratified SN-18); E27.2 (P7-M27). |
| 2026-07-02 | **Clips (§8) added.** New §8 "Clips": a clip is a short video rendering **one** node's proposed→implemented arc (§5 / AOG §16.6) as motion — single-parent (AOG §16.7), the most CFO-facing visual, doubling as publishable media. Documents **production on the verified LTX-Video path** (`ltxv-video.json` → `.webm` via `--type video --workflow`), **citing** the preserved reference bundle (`.ai-project/artifacts/reference/comfyui-endpoint/`) for the exact command and verified parameters (768×512, 97 frames @ 25 fps) rather than re-transcribing or shipping the workflow (**no new plumbing**); a **worked §7 clip binding** (`What: clip`, hosted `.webm` link, `implemented`); the **publish path as reuse** of the same hosted asset (YouTube / TikTok / IG / FB — no publisher or pipeline built); and records **Open Design Question A — reference, not vendor** (the workflow JSONs stay CFO-side; no runnable `workflows/` directory shipped). The §7 schema and by-link (§4) are referenced, **not** restated or changed; `clip` is an existing `What` value. Implements AOG §16.7. Per SN-16 (ratified 2026-06-29), binding decision 3; E24.2 (P6-M24). |
| 2026-06-29 | **Proposed/implemented per-level examples (two-track behavior).** Extended §5 so every level (Creation / HQ / Phase / Milestone / Epic) shows a **proposed** and an **implemented** worked example, each recorded as a **§7 binding** distinguished by its `State` field — the same block in two states, not a second schema. Most pairs are two cheap Structural diagrams; Creation and Epic show a Generative pair where a render communicates better (Structural-first economy). The §7 binding schema and by-link (§4) are referenced, **not** restated or changed. Implements the AOG §16.6 two-track default. Per SN-15/SN-16 (ratified 2026-06-29); E24.1 (P6-M24). |
| 2026-06-29 | **Reversal of v5.0.0 shipped guidance.** Reversed the commit-the-binary storage model to **by-link**: generated artifacts are referenced by link and **never committed to git** — the helper writes a local working file, which the agent hosts on the adopter's storage backend (the adopter owns the storage backend) and links from the governing artifact. Updated §1 (source-repo note generalized — no project commits generated binaries), §3 and §5 (`--output` examples now name local working files), §4 prose, and the §16 related-documents row. Structural-diagram (Mermaid/PlantUML) guidance unchanged. Per SN-16 (ratified 2026-06-29); E23.1 (P6-M23). |
| 2026-06-29 | **Binding convention added (by-link survivability).** Added §7 "Binding a visual to an artifact": a five-element **binding schema** (link + What / Level / State / Description) that records a hosted **link, never a committed path**, and a **per-level placement convention** (Creation → `seed.md` Rule 4 *Visual success*; HQ → `genesis.md` HQ Context Packet; Phase / Milestone / Epic → a "Visual Bindings" section in each spec template). `State` is a single field carrying the proposed/implemented two-track, so a level can hold one of each. Per-level templates updated with a defined binding placement. By-link reversal (§4) and structural-diagram guidance unchanged. Per SN-16 (ratified 2026-06-29), binding decision 2; E23.2 (P6-M23). |
