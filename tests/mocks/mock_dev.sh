#!/bin/bash
# mock_dev.sh - Mock Developer Agent Script
# Simulates code modifications by writing state files.

echo "[Mock Dev] Running with model: ${AI_PROJECT_ACTIVE_MODEL:-unknown}"

# Write a state file indicating dev has run and "fixed" the issues.
mkdir -p .ai-project
echo "fixed" > .ai-project/dev_fixed.txt
echo "[Mock Dev] Code successfully fixed and state written to .ai-project/dev_fixed.txt"
exit 0
