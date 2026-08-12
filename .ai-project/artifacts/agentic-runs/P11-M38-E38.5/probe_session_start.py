#!/usr/bin/env python3
"""Deterministic marker probe: Milestone Chat session-start corpus.

Constructs the prescribed session-start corpus (147,571 bytes of source
content plus a 55-byte section-boundary residue from the original line-range
extraction; the probe actually tested the 147,626-byte superset), places a
unique marker at position 0, sends it through the Ollama /api/generate
endpoint, and records the raw structured response.

Every source is commit-anchored to PINNED_COMMIT. Re-running this script
with the same commit available rebuilds the identical tested bytes.
"""

import json, os, subprocess, sys, time

REPO = subprocess.run(['git', 'rev-parse', '--show-toplevel'],
                       capture_output=True, text=True).stdout.strip()
PINNED_COMMIT = '7f8b0c126e3701058d6e4d4c8cee22409acea46a'  # milestone/M38 at measurement
BASE_REF = PINNED_COMMIT       # source documents: pinned to the recorded commit
MARKER = 'MARKER_E385_SESSION_START_PROBE_20260812'
OUTDIR = os.path.join(REPO, '.ai-project/artifacts/agentic-runs/P11-M38-E38.5')

os.chdir(REPO)

def git_show(ref, path):
    r = subprocess.run(['git', 'show', f'{ref}:{path}'],
                       capture_output=True, text=True, cwd=REPO)
    if r.returncode != 0:
        raise FileNotFoundError(f'{ref}:{path}')
    return r.stdout

def extract(ref, path, start, end):
    """Extract lines start..end (1-indexed, inclusive) from a git-tracked file."""
    content = git_show(ref, path)
    lines = content.splitlines(keepends=True)
    # lines[start-1:end] extracts from line start to line end (inclusive)
    return ''.join(lines[start-1:end])

# ── Source commit anchor ──────────────────────────────────────────────
# PINNED_COMMIT is the extraction commit; BASE_REF used here as descriptive provenance
# since the script no longer resolves it dynamically.
base_commit = PINNED_COMMIT

# ── Phase spec base path ──────────────────────────────────────────────
PHASE_DIR = 'docs/phases/P11__Drivr_Coordination_Over_Rented_Execution'
PSG_PATH = 'governance/PROJECT-SYSTEM-GUIDELINES.md'
AOG_PATH = 'governance/AI-OPERATING-GUIDELINES.md'
PHASE_SPEC_PATH = f'{PHASE_DIR}/P11__phase-spec.md'

# ══════════════════════════════════════════════════════════════════════
# 1. CORE DOCUMENTS
# ══════════════════════════════════════════════════════════════════════

sections = {}

# 1a. M38 Milestone Execution Chat Starter (full)
sections['starter'] = git_show(BASE_REF, f'{PHASE_DIR}/P11-M38__milestone-execution-chat-starter.md')

# 1b. M38 Milestone Spec (full)
sections['milestone_spec'] = git_show(BASE_REF, f'{PHASE_DIR}/P11-M38__milestone-spec.md')

# 1c. Phase spec §P11.3 (lines 227-309)
sections['p11_3'] = extract(BASE_REF, PHASE_SPEC_PATH, 227, 309)

# 1d. Phase spec §Milestones M38 entry (lines 477-511)
# Line 512 is ### M39: Trustworthy Completion Signal — excluded from the defined scope.
sections['m38_milestones'] = extract(BASE_REF, PHASE_SPEC_PATH, 477, 511)

# 1e. Phase spec §Acceptance Criteria (lines 585-626)
# Lines 627-628 are the closing --- separator and blank — excluded from the defined scope.
sections['acceptance'] = extract(BASE_REF, PHASE_SPEC_PATH, 585, 626)

# ══════════════════════════════════════════════════════════════════════
# 2. PSG SESSION-START SECTIONS
# ══════════════════════════════════════════════════════════════════════

psg_ranges = {
    'preamble': (1, 9),
    's1':       (10, 26),
    's1a':      (27, 47),
    's2':       (48, 69),
    's5':       (117, 150),
    's6':       (364, 378),
    's7':       (379, 394),
    's8':       (395, 422),
    's9':       (498, 505),
    's10':      (506, 513),
    's11':      (514, 532),
    's115':     (533, 579),
    's116':     (580, 628),
    's12':      (629, 648),
    's13c':     (695, 715),
    's15':      (904, 913),
}

for label, (start, end) in psg_ranges.items():
    sections[f'psg_{label}'] = extract(BASE_REF, PSG_PATH, start, end)

# ══════════════════════════════════════════════════════════════════════
# 3. AOG SESSION-START SECTIONS
# ══════════════════════════════════════════════════════════════════════

aog_ranges = {
    'preamble': (1, 9),
    's1':       (10, 25),
    's1a':      (26, 44),
    's2':       (45, 63),
    's37':      (515, 533),
    's39':      (551, 565),
    's310':     (566, 589),
    's4':       (590, 605),
    's5':       (606, 625),
    's6':       (626, 639),
    's7':       (640, 672),
    's9':       (688, 700),
    's10':      (727, 779),
    's12':      (825, 846),
    's13':      (847, 860),
    's14':      (861, 876),
}

for label, (start, end) in aog_ranges.items():
    sections[f'aog_{label}'] = extract(BASE_REF, AOG_PATH, start, end)

# ══════════════════════════════════════════════════════════════════════
# 4. ASSEMBLE CORPUS
# ══════════════════════════════════════════════════════════════════════

# Defined concatenation order
corpus_parts = [
    sections['starter'],
    sections['milestone_spec'],
    sections['p11_3'],
    sections['m38_milestones'],
    sections['acceptance'],
]
for label in sorted(psg_ranges.keys()):
    corpus_parts.append(sections[f'psg_{label}'])
for label in sorted(aog_ranges.keys()):
    corpus_parts.append(sections[f'aog_{label}'])

raw_corpus = '\n\n===SECTION_BOUNDARY===\n\n'.join(corpus_parts)

# ══════════════════════════════════════════════════════════════════════
# 5. BUILD PROMPT WITH MARKER
# ══════════════════════════════════════════════════════════════════════

# Marker at position 0; instruction in the tail so marker loss is
# distinguishable from instruction loss.
tail_instruction = f"""

END_OF_CORPUS_MARKER

Above is a document corpus with a unique marker string at position 0
(the very first line). Your task: output that marker string exactly.
Reply with ONLY the marker text, nothing else. Do not include any
other text, explanation, or formatting."""

prompt = MARKER + '\n\n' + raw_corpus + tail_instruction

prompt_bytes = len(prompt.encode('utf-8'))
prompt_tokens_est = prompt_bytes // 4  # rough est; exact count from API response

# ══════════════════════════════════════════════════════════════════════
# 6. RECORD PROBE DATA
# ══════════════════════════════════════════════════════════════════════

os.makedirs(OUTDIR, exist_ok=True)
run_id = time.strftime('%Y%m%dT%H%M%S')

# Per-section byte count table
section_bytes = {}
for key, content in sections.items():
    section_bytes[key] = len(content.encode('utf-8'))

manifest = {
    'run_id': run_id,
    'probe_type': 'marker_session_start_corpus',
    'source_ref': BASE_REF,
    'source_commit': base_commit,
    'marker': MARKER,
    'corpus': {
        'num_parts': len(corpus_parts),
        'concatenation_separator': '\\n\\n===SECTION_BOUNDARY===\\n\\n',
    },
    'section_byte_counts': section_bytes,
    'corpus_raw_bytes': len(raw_corpus.encode('utf-8')),
    'prompt_bytes': prompt_bytes,
    'prompt_tokens_est': prompt_tokens_est,
    'tail_instruction_present': True,
    'model': 'qwen3-coder:30b',
    'endpoint': 'http://localhost:11434/api/generate',
    'options': {'num_predict': 30},
    'probe_command': 'python3 .ai-project/artifacts/agentic-runs/P11-M38-E38.5/probe_session_start.py',
}

# Save construction manifest
with open(f'{OUTDIR}/{run_id}__construction-manifest.json', 'w') as f:
    json.dump(manifest, f, indent=2)

print(f'Run ID: {run_id}')
print(f'Source commit (milestone/M38): {base_commit}')
print(f'Total sections: {len(section_bytes)}')
print(f'Corpus raw bytes: {manifest["corpus_raw_bytes"]}')
print(f'Prompt bytes: {prompt_bytes}')
print(f'Estimated tokens (4 byte/tok): {prompt_tokens_est}')
print(f'Marker at position 0: {MARKER}')
print()

# ══════════════════════════════════════════════════════════════════════
# 7. READ /api/ps BEFORE LOAD
# ══════════════════════════════════════════════════════════════════════

import urllib.request

def ollama_get(path):
    r = urllib.request.urlopen(f'http://localhost:11434{path}', timeout=10)
    return json.loads(r.read())

ps_before = ollama_get('/api/ps')
with open(f'{OUTDIR}/{run_id}__ps-before.json', 'w') as f:
    json.dump(ps_before, f, indent=2)
print(f'/api/ps before load: {len(ps_before.get("models", []))} loaded')

# ══════════════════════════════════════════════════════════════════════
# 8. SEND PROBE
# ══════════════════════════════════════════════════════════════════════

payload = json.dumps({
    'model': 'qwen3-coder:30b',
    'prompt': prompt,
    'stream': False,
    'options': {'num_predict': 30}
}).encode('utf-8')

req = urllib.request.Request(
    'http://localhost:11434/api/generate',
    data=payload,
    headers={'Content-Type': 'application/json'},
    method='POST'
)

print(f'Sending probe ({len(payload)} bytes payload)...')
start = time.time()
try:
    with urllib.request.urlopen(req, timeout=600) as resp:
        probe_response = json.loads(resp.read())
    elapsed = time.time() - start
    print(f'Probe completed in {elapsed:.1f}s')
except Exception as e:
    probe_response = {'error': str(e)}
    elapsed = time.time() - start
    print(f'Probe FAILED in {elapsed:.1f}s: {e}')

with open(f'{OUTDIR}/{run_id}__probe-response.json', 'w') as f:
    json.dump(probe_response, f, indent=2)

# ══════════════════════════════════════════════════════════════════════
# 9. READ /api/ps AFTER LOAD
# ══════════════════════════════════════════════════════════════════════

ps_after = ollama_get('/api/ps')
with open(f'{OUTDIR}/{run_id}__ps-after.json', 'w') as f:
    json.dump(ps_after, f, indent=2)

loaded_context = None
if ps_after.get('models'):
    loaded_context = ps_after['models'][0].get('context_length')
print(f'/api/ps after load: context_length={loaded_context}')

# ══════════════════════════════════════════════════════════════════════
# 10. SUMMARY
# ══════════════════════════════════════════════════════════════════════

print()
print('=== PROBE RESULT ===')
if 'error' in probe_response:
    print(f'  ERROR: {probe_response["error"]}')
else:
    print(f'  done_reason: {probe_response.get("done_reason")}')
    print(f'  prompt_eval_count: {probe_response.get("prompt_eval_count")}')
    resp_text = probe_response.get('response', '').strip()
    print(f'  response: "{resp_text}"')
    print(f'  marker_correct: {resp_text == MARKER}')
    if resp_text == MARKER:
        print('  → MARKER RETAINED — no truncation at position 0')
    elif resp_text:
        print(f'  → MARKER LOST — model returned different content')
    else:
        print('  → No response')
    print(f'  eval_count: {probe_response.get("eval_count")}')
    print(f'  loaded_context (from /api/ps): {loaded_context}')
