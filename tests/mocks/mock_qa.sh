#!/bin/bash
# mock_qa.sh - Mock QA Validation Script
# Simulates tests passing or failing.
#
# VERIFICATION-ONLY (boundary set in P7-M26-E26.2): used solely by
# bin/verify-loop.sh to regression-test the orchestrator loop logic.
# Never part of the live flow — live triggers use a real validation_command.

SCENARIO="${1:-$MOCK_QA_SCENARIO}"

echo "[Mock QA] Running with model: ${AI_PROJECT_ACTIVE_MODEL:-unknown}"
echo "[Mock QA] Scenario: ${SCENARIO:-default}"

if [ "$SCENARIO" = "always_fail" ]; then
    echo "[Mock QA] Simulated failure (always_fail)."
    exit 1
elif [ "$SCENARIO" = "always_success" ]; then
    echo "[Mock QA] Simulated success (always_success)."
    exit 0
else
    # Default scenario: checks for .ai-project/dev_fixed.txt
    if [ -f ".ai-project/dev_fixed.txt" ]; then
        echo "[Mock QA] Found .ai-project/dev_fixed.txt. Validation PASSED!"
        exit 0
    else
        echo "[Mock QA] .ai-project/dev_fixed.txt not found. Validation FAILED!"
        exit 1
    fi
fi
