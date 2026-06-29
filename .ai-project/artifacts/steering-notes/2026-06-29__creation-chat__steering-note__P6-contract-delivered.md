---
artifact_type: steering_note
artifact_version: 1.0
timestamp: 2026-06-29T00:00:00Z
issuer_chat: Creation Chat
target: HQ Chat
project_name: ai-project-system
concerns:
  - id: SN-16
    severity: high
    title: ComfyUI contract delivered + verified — P6 scope sharpens; producer plumbing already exists, real work is storage-model reversal + binding + comprehension behavior
decisions:
  - "The SN-15 gating dependency is RESOLVED. The CFO delivered three verified API-format workflows (flux-schnell, sdxl, ltxv-video) plus the endpoint contract doc, preserved at .ai-project/artifacts/reference/comfyui-endpoint/."
  - "Request contract confirmed and already implemented: bin/ai-project-visual substitutes the literal token %prompt% in the positive CLIPTextEncode node, POSTs the graph to comfyui_url, polls /history, downloads via /view, and writes to --output. Verified end-to-end by the CFO for PNG (SDXL, FLUX) and WEBM (LTX-Video)."
  - "Storage stays by-link per SN-15. This REVERSES shipped P5 guidance (governance/guides/visual-artifacts.md §4 and AOG §16), which instructs committing the generated binary into .ai-project/visuals/ alongside the artifact. Reconciling the framework to the by-link model is an explicit P6 deliverable."
  - "RATIFIED 2026-06-29 by CFO — storage reversal confirmed: generated visual material is NOT stored in the version-controlled project; it is referenced by link. Rationale: version control is the wrong home for generated binary material."
  - "RATIFIED 2026-06-29 by CFO — the link binding carries context metadata (what the visual is, which level it binds to, proposed-vs-implemented, a short description). Load-bearing under the by-link model."
  - "RATIFIED 2026-06-29 by CFO — a clip binds to exactly one parent node (one epic, milestone, or phase) and tells that node's proposed->implemented story, using the same binding convention as any other visual. Clips do not float as cross-cutting editorial in P6; a project-spanning montage is a separate, later capability if ever wanted."
---

# Creation Chat Steering Note — P6 Contract Delivered, Scope Sharpened

## Purpose

This note follows SN-15. The CFO has delivered the ComfyUI workflow(s) into the
Creation Chat, clearing the gating dependency SN-15 flagged. The delivery also
revealed that the consumer plumbing already exists and is verified — which
narrows and sharpens P6. This note hands HQ the resolved dependency, the
confirmed contract, and the revised scope so the P6 phase spec reflects reality
rather than the original "build the consumer" assumption.

---

## Concerns for HQ Triage

### SN-16 — Contract delivered; P6 scope sharpens [HIGH]

**Detail:**

The CFO's delivery (preserved at `.ai-project/artifacts/reference/comfyui-endpoint/`:
`flux-schnell.json`, `sdxl.json`, `ltxv-video.json`, `VISUAL-ARTIFACTS.md`) shows
the *producer* (ComfyUI: FLUX-schnell, SDXL/Juggernaut-XL, LTX-Video 2B) and the
*consumer helper* (`bin/ai-project-visual`, shipped in P5 M22) are both complete
and verified working end-to-end. The original P6-GH-13 framing — "wire the API
call into the agent execution layer" — is therefore largely already done.

What is **not** done is everything between the working helper and the CFO's stated
goal (a continuous visual comprehension layer). P6's real scope is:

1. **Storage-model reversal.** Shipped P5 guidance says commit the binary into
   `.ai-project/visuals/<level>/<id>.<ext>` so it "travels with the decision
   record" (`visual-artifacts.md` §4; AOG §16; reflected in the §4 Output-formats
   table and per-level examples). SN-15 reverses this to **by-link, no binaries in
   git, adopter owns the storage backend**. P6 must update the guide, AOG §16, the
   helper's output guidance, and the integration-test expectations to the by-link
   model. This is the single biggest governance change in P6.

2. **Binding + metadata convention.** Define how a visual's *link* plus context
   metadata (what it is, which level, proposed-vs-implemented, a short description)
   attaches to the correct governance artifact at the correct level. This is the
   SN-15 `[PROPOSED — confirm]` metadata item, now load-bearing because the link is
   the only thing in git.

3. **Comprehension behavior ("nothing is too much").** Make proposed-vs-implemented
   visuals routinely happen at every level. Note the framework already has the
   two-mode split (P5 `visual-artifacts.md` §2): **Structural** (Mermaid/PlantUML,
   text, free, no endpoint) carries most architecture/scope/component/flow
   diagrams; **Generative** (ComfyUI) is for concept/vision imagery, infographics,
   mockups, and clips. The generous-coverage bar is cheap for Structural and should
   be the default for "follow the proposed solution and the actual implementation."

4. **Clips as documentation + publishable media.** The LTX-Video path
   (`ltxv-video.json` → `.webm`) is verified. P6 defines how a clip is produced from
   the proposed→implemented arc (SN-15 `[PROPOSED]` single-parent binding) and the
   publish path to YouTube/TikTok/IG/FB — the same asset, reused.

**Required action:** HQ opens the P6 phase spec treating producer + helper as DONE,
and scopes P6 around items 1–4 above plus the process carry-forwards
(GH-10/GH-11/GH-12). The by-link reconciliation (item 1) should be called out as an
explicit deliverable because it changes freshly shipped v5.0.0 guidance.

---

## Decisions Already Made

1. **SN-15 gating dependency resolved** — workflows delivered and preserved in-repo.
2. **Contract confirmed** — `%prompt%` token substitution; helper handles POST →
   poll → download → write; verified for PNG and WEBM.
3. **Storage reversal RATIFIED by CFO (2026-06-29)** — generated visuals are not
   committed to the version-controlled project; they are referenced by link
   (rationale: version control is the wrong home for generated binary material).
   P6 owns reconciling the contradicting shipped P5 guidance to match.
4. **Link metadata RATIFIED by CFO (2026-06-29)** — the link binding carries context
   metadata (what it is, level, proposed-vs-implemented, short description). This
   is load-bearing under by-link, since the link is the only thing in git.
5. **Clip single-parent binding RATIFIED by CFO (2026-06-29)** — every clip belongs
   to exactly one governance node (one epic, milestone, or phase) and tells that
   node's proposed→implemented story, using the same binding convention as any
   other visual. Clips do not float as cross-cutting editorial in P6; a
   project-spanning montage is a separate, later capability if ever wanted.

---

## Carry-Over Open Items

1. **Vendor vs. reference the workflow JSONs.** Decide whether the framework ships
   the workflow JSONs in-repo (e.g., a `workflows/` dir the helper points at) or
   references them on the CFO's ComfyUI host. P6 design choice.
2. **Does the helper need a link-emitting step?** Now sharper since by-link is
   ratified: decide whether `bin/ai-project-visual` gains an upload/return-link
   capability, or whether hosting + linking is the agent's responsibility outside
   the helper. Affects whether the helper changes in P6.
3. **Registry consolidation (carried from SN-15)** — fold GH-10/11/12/13 into the
   single roadmap candidate table.

> The two `[PROPOSED — confirm]` items carried from SN-15 (link metadata; clip
> single-parent binding) were **RATIFIED by the CFO on 2026-06-29** and moved to
> Decisions Already Made (items 4 and 5).

---

## Next Action

HQ Chat should:

1. Open the P6 phase spec from SN-15's spine, revised by SN-16: producer + helper
   are DONE; the phase is storage-model reversal, binding/metadata convention,
   comprehension behavior, and clips — plus process carry-forwards GH-10/11/12.
2. Make the **by-link storage reconciliation** an explicit, named P6 deliverable
   (touches `visual-artifacts.md` §4, AOG §16, helper output guidance, integration
   test). Flag it as a reversal of v5.0.0 shipped guidance.
3. Use `.ai-project/artifacts/reference/comfyui-endpoint/` as the request contract;
   resolve the vendor-vs-reference question for the workflow JSONs.
4. Bring the two `[PROPOSED — confirm]` items to the CFO for ratification when
   authoring the phase spec.
