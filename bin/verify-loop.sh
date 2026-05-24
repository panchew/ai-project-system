#!/bin/bash
# bin/verify-loop.sh - Verification Script & Loop Mock Harness for P3-M12-E12.3

# Exit on error
set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
QUEUE_DIR="$PROJECT_ROOT/.ai-project/queue"
LOCKS_DIR="$PROJECT_ROOT/.ai-project/locks"
LOCK_FILE="$LOCKS_DIR/execution.lock"
FEEDBACK_FILE="$PROJECT_ROOT/.ai-project/feedback.json"
DEV_STATE_FILE="$PROJECT_ROOT/.ai-project/dev_fixed.txt"
ADMIN_DIR="$PROJECT_ROOT/docs/admin"
ORCHESTRATOR="$PROJECT_ROOT/bin/ai-project-orchestrator"

# ANSI colors for terminal output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Preserve initial permissions so we can revert them at the end
ORIG_PERM_AI_PROJECT=$(stat -c "%a" "$PROJECT_ROOT/.ai-project")
ORIG_PERM_LOCKS=$(stat -c "%a" "$LOCKS_DIR" 2>/dev/null || echo "775")
ORIG_PERM_QUEUE=$(stat -c "%a" "$QUEUE_DIR" 2>/dev/null || echo "775")
ORIG_PERM_ADMIN=$(stat -c "%a" "$ADMIN_DIR")

# Save initial git commit hash
INITIAL_GIT_HASH=$(git rev-parse HEAD)
log_info "Initial Git Hash: $INITIAL_GIT_HASH"

# Helper to configure world-write permissions for the Docker container
setup_permissions() {
    mkdir -p "$PROJECT_ROOT/.ai-project" "$LOCKS_DIR" "$QUEUE_DIR" "$ADMIN_DIR"
    chmod 777 "$PROJECT_ROOT/.ai-project"
    chmod 777 "$LOCKS_DIR"
    chmod 777 "$QUEUE_DIR"
    chmod 777 "$ADMIN_DIR"
}

# Helper to restore original permissions
restore_permissions() {
    [ -d "$PROJECT_ROOT/.ai-project" ] && chmod "$ORIG_PERM_AI_PROJECT" "$PROJECT_ROOT/.ai-project"
    [ -d "$LOCKS_DIR" ] && chmod "$ORIG_PERM_LOCKS" "$LOCKS_DIR"
    [ -d "$QUEUE_DIR" ] && chmod "$ORIG_PERM_QUEUE" "$QUEUE_DIR"
    [ -d "$ADMIN_DIR" ] && chmod "$ORIG_PERM_ADMIN" "$ADMIN_DIR"
}

cleanup_workspace() {
    log_info "Cleaning up workspace state..."
    # Remove files that are part of the loop execution state
    rm -f "$QUEUE_DIR/04_epic.json"
    rm -f "$QUEUE_DIR/04_epic.json.failed"
    rm -f "$LOCK_FILE"
    rm -f "$FEEDBACK_FILE"
    rm -f "$DEV_STATE_FILE"
    rm -f "$ADMIN_DIR/escalation-report-MOCK-EPIC.md"
    
    # Restore Git to initial commit if it changed
    CURRENT_HASH=$(git rev-parse HEAD)
    if [ "$INITIAL_GIT_HASH" != "$CURRENT_HASH" ]; then
        log_warn "Git state modified. Resetting repository to initial hash $INITIAL_GIT_HASH..."
        git reset --soft "$INITIAL_GIT_HASH" >/dev/null 2>&1
        git reset HEAD >/dev/null 2>&1
    fi
    
    restore_permissions
}

# Register signal and exit trap handler
trap_handler() {
    local exit_status=$?
    if [ $exit_status -ne 0 ]; then
        log_error "Verification script failed or was interrupted with exit code $exit_status!"
        cleanup_workspace
        exit $exit_status
    fi
}
trap trap_handler INT TERM EXIT

# Set permissions for testing
setup_permissions

# Helper to write 04_epic.json trigger file
write_trigger() {
    local val_cmd="$1"
    local dev_cmd="$2"
    local run_dev_init="$3"
    
    mkdir -p "$QUEUE_DIR"
    cat <<EOF > "$QUEUE_DIR/04_epic.json"
{
  "epic_id": "MOCK-EPIC",
  "sandbox_env": "ai-project-sandbox:latest",
  "validation_command": "$val_cmd",
  "dev_command": "$dev_cmd",
  "run_dev_initially": $run_dev_init
}
EOF
}

# ==============================================================================
# SCENARIO 1: Immediate Success (Passes on attempt 1, commits and deletes trigger)
# ==============================================================================
run_scenario_1() {
    log_info "------------------------------------------------------------"
    log_info "Running Scenario 1: Immediate Success"
    log_info "------------------------------------------------------------"
    
    # Clean up state
    cleanup_workspace
    setup_permissions
    
    # Setup trigger where QA validation always succeeds on attempt 1
    write_trigger "./tests/mocks/mock_qa.sh always_success" "./tests/mocks/mock_dev.sh" "false"
    
    # Record commit hash before run
    local pre_run_hash=$(git rev-parse HEAD)
    
    # Execute orchestrator (expecting success, exit code 0)
    log_info "Executing orchestrator..."
    set +e
    python3 "$ORCHESTRATOR"
    local exit_code=$?
    set -e
    
    log_info "Orchestrator finished with exit code: $exit_code"
    
    # Assertions
    if [ $exit_code -ne 0 ]; then
        log_error "Scenario 1 failed: orchestrator exited with code $exit_code, expected 0"
        exit 1
    fi
    
    if [ -f "$QUEUE_DIR/04_epic.json" ]; then
        log_error "Scenario 1 failed: trigger file was not deleted"
        exit 1
    fi
    
    if [ -f "$FEEDBACK_FILE" ]; then
        log_error "Scenario 1 failed: feedback.json should not exist"
        exit 1
    fi
    
    if [ -f "$ADMIN_DIR/escalation-report-MOCK-EPIC.md" ]; then
        log_error "Scenario 1 failed: escalation report should not exist"
        exit 1
    fi
    
    local post_run_hash=$(git rev-parse HEAD)
    if [ "$pre_run_hash" = "$post_run_hash" ]; then
        log_error "Scenario 1 failed: no git commit was made"
        exit 1
    fi
    
    log_success "Scenario 1: Immediate Success verified successfully!"
}

# ==============================================================================
# SCENARIO 2: Successful Self-Repair (Fails on 1, Dev fixes, passes on 2)
# ==============================================================================
run_scenario_2() {
    log_info "------------------------------------------------------------"
    log_info "Running Scenario 2: Successful Self-Repair"
    log_info "------------------------------------------------------------"
    
    # Clean up state
    cleanup_workspace
    setup_permissions
    
    # Setup trigger where QA check depends on the dev state file
    write_trigger "./tests/mocks/mock_qa.sh" "./tests/mocks/mock_dev.sh" "false"
    
    # Record commit hash before run
    local pre_run_hash=$(git rev-parse HEAD)
    
    # Execute orchestrator (expecting success after repair, exit code 0)
    log_info "Executing orchestrator..."
    set +e
    python3 "$ORCHESTRATOR"
    local exit_code=$?
    set -e
    
    log_info "Orchestrator finished with exit code: $exit_code"
    
    # Assertions
    if [ $exit_code -ne 0 ]; then
        log_error "Scenario 2 failed: orchestrator exited with code $exit_code, expected 0"
        exit 1
    fi
    
    if [ -f "$QUEUE_DIR/04_epic.json" ]; then
        log_error "Scenario 2 failed: trigger file was not deleted"
        exit 1
    fi
    
    if [ -f "$FEEDBACK_FILE" ]; then
        log_error "Scenario 2 failed: feedback.json was not deleted upon success"
        exit 1
    fi
    
    if [ ! -f "$DEV_STATE_FILE" ]; then
        log_error "Scenario 2 failed: dev state file dev_fixed.txt was not created"
        exit 1
    fi
    
    local post_run_hash=$(git rev-parse HEAD)
    if [ "$pre_run_hash" = "$post_run_hash" ]; then
        log_error "Scenario 2 failed: no git commit was made"
        exit 1
    fi
    
    log_success "Scenario 2: Successful Self-Repair verified successfully!"
}

# ==============================================================================
# SCENARIO 3: Max Retries Exhausted (Fails 3 times, archives trigger, escalates)
# ==============================================================================
run_scenario_3() {
    log_info "------------------------------------------------------------"
    log_info "Running Scenario 3: Max Retries Exhausted (Escalation)"
    log_info "------------------------------------------------------------"
    
    # Clean up state
    cleanup_workspace
    setup_permissions
    
    # Setup trigger where QA validation always fails
    write_trigger "./tests/mocks/mock_qa.sh always_fail" "./tests/mocks/mock_dev.sh" "false"
    
    # Record commit hash before run
    local pre_run_hash=$(git rev-parse HEAD)
    
    # Execute orchestrator (expecting escalation failure, exit code 1)
    log_info "Executing orchestrator..."
    set +e
    python3 "$ORCHESTRATOR"
    local exit_code=$?
    set -e
    
    log_info "Orchestrator finished with exit code: $exit_code"
    
    # Assertions
    if [ $exit_code -ne 1 ]; then
        log_error "Scenario 3 failed: orchestrator exited with code $exit_code, expected 1"
        exit 1
    fi
    
    if [ -f "$QUEUE_DIR/04_epic.json" ]; then
        log_error "Scenario 3 failed: trigger file was not archived (still exists as 04_epic.json)"
        exit 1
    fi
    
    if [ ! -f "$QUEUE_DIR/04_epic.json.failed" ]; then
        log_error "Scenario 3 failed: archived trigger file 04_epic.json.failed does not exist"
        exit 1
    fi
    
    if [ ! -f "$FEEDBACK_FILE" ]; then
        log_error "Scenario 3 failed: feedback.json was not written"
        exit 1
    fi
    
    # Check feedback schema and attempt
    local feedback_attempt=$(python3 -c "import json; print(json.load(open('$FEEDBACK_FILE'))['attempt'])")
    if [ "$feedback_attempt" != "3" ]; then
        log_error "Scenario 3 failed: feedback.json attempt is $feedback_attempt, expected 3"
        exit 1
    fi
    
    if [ ! -f "$ADMIN_DIR/escalation-report-MOCK-EPIC.md" ]; then
        log_error "Scenario 3 failed: escalation report docs/admin/escalation-report-MOCK-EPIC.md was not generated"
        exit 1
    fi
    
    local post_run_hash=$(git rev-parse HEAD)
    if [ "$pre_run_hash" != "$post_run_hash" ]; then
        log_error "Scenario 3 failed: git commit was made on failure, should not commit"
        exit 1
    fi
    
    log_success "Scenario 3: Max Retries Exhausted verified successfully!"
}

# ==============================================================================
# SCENARIO 4: Lockfile Guard (Orchestrator refuses to run if lock already exists)
# ==============================================================================
run_scenario_4() {
    log_info "------------------------------------------------------------"
    log_info "Running Scenario 4: Lockfile Guard"
    log_info "------------------------------------------------------------"
    
    # Clean up state
    cleanup_workspace
    setup_permissions
    
    # Create the lockfile manually before running orchestrator
    mkdir -p "$LOCKS_DIR"
    touch "$LOCK_FILE"
    
    # Write trigger
    write_trigger "./tests/mocks/mock_qa.sh always_success" "./tests/mocks/mock_dev.sh" "false"
    
    # Record commit hash before run
    local pre_run_hash=$(git rev-parse HEAD)
    
    # Execute orchestrator (expecting failure to start, exit code 1)
    log_info "Executing orchestrator with existing lock..."
    set +e
    python3 "$ORCHESTRATOR"
    local exit_code=$?
    set -e
    
    log_info "Orchestrator finished with exit code: $exit_code"
    
    # Assertions
    if [ $exit_code -ne 1 ]; then
        log_error "Scenario 4 failed: orchestrator exited with code $exit_code, expected 1"
        exit 1
    fi
    
    if [ ! -f "$QUEUE_DIR/04_epic.json" ]; then
        log_error "Scenario 4 failed: trigger file was modified or deleted"
        exit 1
    fi
    
    if [ -f "$FEEDBACK_FILE" ]; then
        log_error "Scenario 4 failed: feedback.json should not exist"
        exit 1
    fi
    
    if [ -f "$ADMIN_DIR/escalation-report-MOCK-EPIC.md" ]; then
        log_error "Scenario 4 failed: escalation report should not exist"
        exit 1
    fi
    
    local post_run_hash=$(git rev-parse HEAD)
    if [ "$pre_run_hash" != "$post_run_hash" ]; then
        log_error "Scenario 4 failed: a git commit was incorrectly made"
        exit 1
    fi
    
    # Remove lockfile manually so workspace is clean
    rm -f "$LOCK_FILE"
    
    log_success "Scenario 4: Lockfile Guard verified successfully!"
}

# Run all scenarios
run_scenario_1
run_scenario_2
run_scenario_3
run_scenario_4

# Cleanup the workspace at the very end
cleanup_workspace

# Disable trap handler to prevent double execution on script termination
trap - INT TERM EXIT

# Output huge success block
echo -e "\n${GREEN}======================================================================${NC}"
echo -e "${GREEN}  ALL CLOSED-LOOP VERIFICATION SCENARIOS PASSED SUCCESSFULLY!       ${NC}"
echo -e "${GREEN}======================================================================${NC}"
log_success "Closed-loop execution engine recursion verification complete."
exit 0
