#!/bin/bash
# mock_dev.sh - Mock Developer Agent Script
# Simulates code modifications by writing state files.
#
# VERIFICATION-ONLY (boundary set in P7-M26-E26.2): used solely by
# bin/verify-loop.sh to regression-test the orchestrator loop logic.
# Never part of the live flow — live triggers use ./bin/run-dev-agent.

echo "[Mock Dev] Running with model: ${AI_PROJECT_ACTIVE_MODEL:-unknown}"

# Write a state file indicating dev has run and "fixed" the issues.
mkdir -p .ai-project
echo "fixed" > .ai-project/dev_fixed.txt
echo "[Mock Dev] Code successfully fixed and state written to .ai-project/dev_fixed.txt"
exit 0
