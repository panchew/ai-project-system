<!--
  PRESERVED REFERENCE — delivered by the CFO into the Creation Chat on 2026-06-29
  as the verified ComfyUI endpoint contract for P6. Content reproduced faithfully;
  only paste-encoding artifacts (mojibake dashes/arrows/symbols) were normalized.
  This is the CFO's host-side documentation of the generative endpoint. The
  matching API-format workflows are the sibling *.json files in this directory.
  Authoritative location of the live endpoint and models stays on the CFO's side.
-->

# ComfyUI as the Governance Visual-Artifacts Endpoint

This ComfyUI instance is the **CFO-provided generative endpoint** for the AI Project System's
visual-artifact capability (governance P5 / Milestone M22). Governed projects set
`visual_artifacts.enabled: true` with `comfyui_url: http://localhost:8188` and call
`bin/ai-project-visual` (a one-shot *prompt → image/video* helper) against this server.

The framework defines two visual modes:

- **Structural** — Mermaid / PlantUML diagrams written as text by the agent. **No ComfyUI needed.**
  Used for HQ architecture, phase-scope, and milestone component/flow diagrams.
- **Generative** — imagery / video produced here. Used for Creation-Chat concept/vision imagery,
  infographics, Epic-Chat UI mockups, and (optional) video.

This document covers only the **generative** half — the models and workflows installed here.

---

## What's installed for governance visuals

| Model | Path | Role | Source |
|-------|------|------|--------|
| `flux1-schnell-fp8-e4m3fn.safetensors` | `models/unet/` | FLUX.1-schnell UNet (fp8) — best prompt adherence + legible text | `Kijai/flux-fp8` |
| `clip_l.safetensors` | `models/clip/` | FLUX CLIP-L text encoder | `comfyanonymous/flux_text_encoders` |
| `t5xxl_fp8_e4m3fn.safetensors` | `models/clip/` | T5-XXL text encoder (shared: FLUX **and** LTX-Video) | `comfyanonymous/flux_text_encoders` |
| `flux-vae-bf16.safetensors` | `models/vae/` | FLUX autoencoder | `Kijai/flux-fp8` |
| `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` | `models/checkpoints/` | SDXL — fast, versatile concept imagery | `RunDiffusion/Juggernaut-XL-v9` |
| `ltx-video-2b-v0.9.5.safetensors` | `models/checkpoints/` | LTX-Video 2B — text-to-video | `Lightricks/LTX-Video` |

`models/unet` and `models/clip` are mapped in `extra_model_paths.yaml`
(keys `unet:` and `clip:`). **`extra_model_paths.yaml` is read only at container start** — restart
ComfyUI after changing it. New model *files* in already-mapped folders are picked up on a refresh.

---

## Workflows

API-format graphs in `workflows/`. The helper replaces the literal token `%prompt%`
(in the positive prompt node) with `--prompt`. Image dimensions / steps are set **inside** each JSON.

| Workflow | Model | Best for | Output |
|----------|-------|----------|--------|
| `workflows/flux-schnell.json` | FLUX.1-schnell | infographics, concept/vision imagery, mockups **with text** | `.png` |
| `workflows/sdxl.json` | Juggernaut XL | fast, photoreal/illustrative concept imagery | `.png` |
| `workflows/ltxv-video.json` | LTX-Video 2B | short concept video clips | `.webm` |

> SDXL also runs on the helper's **built-in** workflow via `--checkpoint`; `sdxl.json` is a tuned
> variant (negative prompt, 1024², dpmpp_2m/karras, 30 steps).

---

## Configuration (`.ai-project.yml`)

```yaml
visual_artifacts:
  enabled: true
  comfyui_url: http://localhost:8188
  types: [diagrams, infographics, video]
```

The helper reads this from the **current working directory** (`PROJECT_ROOT = cwd`), and refuses a
`--type` not listed in `types`.

---

## Usage

Run from the project root so the helper finds `.ai-project.yml`:

```bash
# Concept / infographic (FLUX — best for anything with text/labels)
.governance/bin/ai-project-visual \
  --prompt "isometric concept image of a layered governance framework, clean, professional" \
  --type infographics --workflow workflows/flux-schnell.json \
  --output .ai-project/visuals/creation/vision.png

# Fast concept imagery (SDXL)
.governance/bin/ai-project-visual \
  --prompt "warm, approachable hero image for a developer tool, soft gradients" \
  --type infographics --workflow workflows/sdxl.json \
  --output .ai-project/visuals/creation/vision-sdxl.png

# Short video clip (LTX-Video)
.governance/bin/ai-project-visual \
  --prompt "slow cinematic pan across a glowing network of connected nodes" \
  --type video --workflow workflows/ltxv-video.json \
  --output .ai-project/visuals/creation/vision.webm
```

Exit codes: `0` ok · `2` disabled · `3` config error · `4` runtime error.

---

## Operations

```bash
# Restart after editing extra_model_paths.yaml (registers unet/ + clip/)
docker compose -f docker-compose.yml restart comfyui     # from this dir
# Env changes (e.g. CLI_ARGS) need a recreate, not a plain restart:
docker compose -f docker-compose.yml up -d comfyui

# Confirm the server sees a model
curl -s localhost:8188/object_info/CheckpointLoaderSimple \
  | python3 -c "import sys,json;print(json.load(sys.stdin)['CheckpointLoaderSimple']['input']['required']['ckpt_name'][0])"

# Endpoint health
curl -s localhost:8188/system_stats
```

**Hardware:** RTX 5060 Ti 16 GB (Blackwell sm_120), image `yanwk/comfyui-boot:cu130-megapak-pt211`
(CUDA 13 / PyTorch 2.11). FLUX fp8 UNet (~11.9 GB) fits VRAM with T5 offloaded to system RAM —
note ollama + llama.cpp also consume RAM on this host.

---

## Status — verified

- [x] Model dirs, `extra_model_paths.yaml` (unet/clip), workflows, `.ai-project.yml` block
- [x] All 6 models downloaded; container recreated; server sees every model
- [x] **SDXL** (`sdxl.json`) → PNG ✅
- [x] **FLUX** (`flux-schnell.json`) → PNG with legible headline text ✅
- [x] **LTX-Video** (`ltxv-video.json`) → valid `.webm` ✅

All three generated through `bin/ai-project-visual` against `http://localhost:8188`. Test outputs:
`.ai-project/visuals/test/{sdxl,flux,ltxv}-test.*`.

### Blackwell (sm_120) attention fix — required for video

LTX-Video (and other attention-bias models) crash under xformers on this GPU:
`No operator found for memory_efficient_attention_forward … capability (12,0) too new`. The fix is in
`docker-compose.yml`: `CLI_ARGS=--use-pytorch-cross-attention` forces PyTorch
native SDPA, which handles attn-bias on sm_120. Keep this set. FLUX/SDXL work with or without it.

### Notes on quality

- FLUX schnell (4 steps) renders **headlines/labels** cleanly but garbles long body text — expected
  for the distilled model. For dense legible text, raise steps or use FLUX-dev.
- LTX-Video defaults: 768×512, 97 frames @ 25 fps. Edit `workflows/ltxv-video.json` to change.
