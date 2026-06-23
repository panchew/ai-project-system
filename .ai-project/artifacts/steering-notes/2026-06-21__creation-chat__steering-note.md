---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-06-21T00:00:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-11
    severity: medium
    title: Visual artifacts as a first-class deliverable at every chat level
decisions:
  - Visual artifact production is opt-in via a new visual_artifacts.enabled toggle in .ai-project.yml (same pattern as cfo_review_gate).
  - The abstraction level of visuals mirrors the chat level — Creation Chat produces concept/vision imagery; HQ produces system architecture; Phase produces scope diagrams; Milestone produces component and flow diagrams; Epic produces implementation detail, UI mockups, and before/after comparisons.
  - Any chat that can call tools can produce visuals. Tool-calling capability is the gate, not chat level per se.
  - ComfyUI (CFO has a running local instance) is the target tool for image and video generation. Mermaid/PlantUML serve structural/technical diagrams. Both are valid visual outputs.
  - Visual intent must be captured at Creation Chat inception. seed.md requires a "What does success look like visually?" elicitation before producing the Project Brief.
  - This feature is valid for the governance framework standalone (via operating guidelines directing agents to produce visuals as part of DoD) and for the future agentic app (as a first-class product feature).
  - Videos and short clips are in scope — technically feasible via ComfyUI video nodes.
---

# Creation Chat Steering Note — Visual Artifacts Vision

## Purpose

CFO articulated a clear product vision during the 2026-06-21 Creation Chat session.
The vision is concrete enough to propagate into the governance framework as a new
capability direction. This note captures the binding decisions for HQ to act on.

---

## Concerns for HQ Triage

### SN-11 — Visual artifacts as a first-class deliverable at every chat level

**Severity:** Medium (no existing workflow is blocked; this is additive scope)

**Vision summary:**

The CFO wants every chat level to produce visual artifacts appropriate to its authority
level — before, during, and after execution. The principle: the abstraction level of the
visual matches the abstraction level of the chat.

| Chat level | Visual type | Examples |
|------------|-------------|---------|
| Creation Chat | Concept / vision imagery | Product feel, style reference, what success looks like |
| HQ Chat | System architecture | Full product map, component overview |
| Phase Chat | Phase scope diagram | What moves, what boundaries exist, what this phase touches |
| Milestone Chat | Component + flow diagrams | Data flow, sequence diagrams, what gets built this milestone |
| Epic Chat | Implementation detail | UI mockups, before/after, code structure, ER diagrams |

**Key design decisions (binding):**

1. **Opt-in switch** — `visual_artifacts.enabled: true|false` in `.ai-project.yml`.
   When disabled, agents skip the visual step entirely. When enabled, operating
   guidelines instruct each chat level to produce a visual as part of its closing
   artifact set. Pattern is identical to `cfo_review_gate`.

2. **Tool-calling is the gate** — Any chat that can call tools can produce visuals.
   Milestone Chat can create PRs; therefore it can call ComfyUI; therefore it can
   produce milestone-level visuals. This is not Epic-only.

3. **Two visual modes:**
   - *Structural*: Mermaid / PlantUML / draw.io — code-generated, deterministic,
     lives in markdown. Used for architecture, flow, sequence, ER diagrams.
   - *Generative*: ComfyUI API call — AI-generated imagery and video. Used for
     concept art, UI mockups, end-result visualization, short demo clips.

4. **ComfyUI integration** — CFO has a running local ComfyUI instance.
   `.ai-project.yml` carries the endpoint: `visual_artifacts.comfyui_url`.
   Agents call the API when producing generative visuals.

5. **Visual intent travels the cascade** — The visual vision originates at Creation
   Chat (seed.md elicitation) and flows downward through the Project Brief →
   Phase spec → Milestone spec → Epic spec, becoming progressively more concrete.
   `seed.md` must be updated to elicit "what does success look like visually?"
   before producing the Project Brief.

6. **Video is in scope** — ComfyUI video nodes (AnimateDiff et al.) make short
   clips feasible. The governance framework should not artificially exclude video
   output. The `visual_artifacts.types` list controls what is produced.

**Proposed `.ai-project.yml` additions:**

```yaml
visual_artifacts:
  enabled: true          # or: false (default)
  comfyui_url: http://localhost:8188
  types:
    - diagrams            # Mermaid/PlantUML structural diagrams
    - infographics        # ComfyUI-generated imagery
    - video               # ComfyUI video generation (optional)
```

**Required action from HQ:**

1. Register this as a P5 candidate (P5-VA-1) — Visual Artifacts subsystem.
2. Determine whether this belongs in the governance framework (AI-OPERATING-GUIDELINES.md
   additions + .ai-project.yml spec extension) or is deferred to the agentic app.
   CFO position: valid for both; governance framework gets the spec and switch;
   agentic app gets the full implementation.
3. Update `seed.md` to include visual intent elicitation in the Project Brief
   convergence target (Rule 4).

---

## Decisions Already Made

- `visual_artifacts.enabled` follows the same opt-in pattern as `cfo_review_gate`.
- Tool-calling capability (not chat level label) is the gate for visual production.
- ComfyUI is the target generative tool; CFO's local instance is the integration target.
- Visual intent originates at Creation Chat and propagates down the artifact cascade.
- Video output is in scope.

---

## Carry-Over Open Items

None beyond SN-11.

---

## Next Action

HQ Chat registers P5-VA-1 and determines governance-framework vs agentic-app split.
No execution work starts until P5 phase spec is open.
