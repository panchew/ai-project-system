#!/bin/bash
# bin/verify-daemon.sh - Comprehensive E2E Lifecycle & Crash Recovery Integration Test Suite
# Epic: E13.4 - Daemon Lifecycle Management & Integration Tests

# Exit on error
set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOCKS_DIR="$PROJECT_ROOT/.ai-project/locks"
LOGS_DIR="$PROJECT_ROOT/.ai-project/logs"
QUEUE_DIR="$PROJECT_ROOT/.ai-project/queue"

LOCK_FILE="$LOCKS_DIR/daemon.pid"
LOG_FILE="$LOGS_DIR/daemon.log"
EXECUTION_LOCK="$LOCKS_DIR/execution.lock"
ORCHESTRATOR_BIN="$PROJECT_ROOT/bin/ai-project-orchestrator"
DAEMON_BIN="$PROJECT_ROOT/bin/ai-project-daemon"

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

# Preserve initial state & permissions
INITIAL_GIT_HASH=$(git rev-parse HEAD)
ORIG_PERM_LOCKS=$(stat -c "%a" "$LOCKS_DIR" 2>/dev/null || echo "775")
ORIG_PERM_LOGS=$(stat -c "%a" "$LOGS_DIR" 2>/dev/null || echo "775")

WAS_RUNNING=false
if [ -f "$LOCK_FILE" ]; then
    orig_pid=$(cat "$LOCK_FILE" 2>/dev/null)
    if [ -n "$orig_pid" ] && ps -p "$orig_pid" > /dev/null 2>&1; then
        log_info "Active daemon detected (PID $orig_pid). Stopping it gracefully for test isolation..."
        # Copy original files for restoration later
        [ -f "$LOG_FILE" ] && cp "$LOG_FILE" "$LOG_FILE.orig"
        [ -f "$EXECUTION_LOCK" ] && cp "$EXECUTION_LOCK" "$EXECUTION_LOCK.orig"
        cp "$LOCK_FILE" "$LOCK_FILE.orig"
        
        # Stop daemon gracefully
        "$DAEMON_BIN" stop >/dev/null 2>&1 || true
        WAS_RUNNING=true
    fi
fi

# If they weren't backed up (meaning WAS_RUNNING is false), move them to .orig just in case they exist as stale files
if [ "$WAS_RUNNING" = "false" ]; then
    [ -f "$LOCK_FILE" ] && mv "$LOCK_FILE" "$LOCK_FILE.orig"
    [ -f "$LOG_FILE" ] && mv "$LOG_FILE" "$LOG_FILE.orig"
    [ -f "$EXECUTION_LOCK" ] && mv "$EXECUTION_LOCK" "$EXECUTION_LOCK.orig"
fi

cleanup_workspace() {
    log_info "Cleaning up workspace state..."
    
    # 1. Kill any leftover daemon processes started during this test run
    if [ -f "$LOCK_FILE" ]; then
        local d_pid=$(cat "$LOCK_FILE" 2>/dev/null)
        if [ -n "$d_pid" ] && ps -p "$d_pid" > /dev/null 2>&1; then
            log_warn "Force killing leftover test daemon process with PID $d_pid"
            kill -9 "$d_pid" >/dev/null 2>&1 || true
        fi
        rm -f "$LOCK_FILE"
    fi

    # Remove temporary test triggers
    rm -f "$QUEUE_DIR/99_test.json"

    # Restore orchestrator backup if it exists
    if [ -f "$ORCHESTRATOR_BIN.bak" ]; then
        log_info "Restoring real orchestrator..."
        mv "$ORCHESTRATOR_BIN.bak" "$ORCHESTRATOR_BIN"
    fi

    # Restore directories from Scenario 7 if they exist
    if [ -d "$LOCKS_DIR.tmp" ]; then
        log_info "Restoring locks directory backup..."
        rm -rf "$LOCKS_DIR"
        mv "$LOCKS_DIR.tmp" "$LOCKS_DIR"
    fi
    if [ -d "$LOGS_DIR.tmp" ]; then
        log_info "Restoring logs directory backup..."
        rm -rf "$LOGS_DIR"
        mv "$LOGS_DIR.tmp" "$LOGS_DIR"
    fi

    # Restore permissions
    [ -d "$LOCKS_DIR" ] && chmod "$ORIG_PERM_LOCKS" "$LOCKS_DIR"
    [ -d "$LOGS_DIR" ] && chmod "$ORIG_PERM_LOGS" "$LOGS_DIR"

    # Restore original state files
    rm -f "$LOCK_FILE" "$LOG_FILE" "$EXECUTION_LOCK"
    [ -f "$LOCK_FILE.orig" ] && mv "$LOCK_FILE.orig" "$LOCK_FILE"
    [ -f "$LOG_FILE.orig" ] && mv "$LOG_FILE.orig" "$LOG_FILE"
    [ -f "$EXECUTION_LOCK.orig" ] && mv "$EXECUTION_LOCK.orig" "$EXECUTION_LOCK"

    # If daemon was running originally, restart it
    if [ "$WAS_RUNNING" = "true" ]; then
        log_info "Restarting original daemon..."
        "$DAEMON_BIN" start >/dev/null 2>&1 || true
    fi

    # Restore Git to initial commit if it changed
    CURRENT_HASH=$(git rev-parse HEAD)
    if [ "$INITIAL_GIT_HASH" != "$CURRENT_HASH" ]; then
        log_warn "Git state modified. Resetting repository to initial hash $INITIAL_GIT_HASH..."
        git reset --soft "$INITIAL_GIT_HASH" >/dev/null 2>&1
        git reset HEAD >/dev/null 2>&1
    fi
}

# Trap handler for clean exit
trap_handler() {
    local exit_status=$?
    if [ $exit_status -ne 0 ]; then
        log_error "Verification script failed or was interrupted with exit code $exit_status!"
        cleanup_workspace
        exit $exit_status
    fi
}
trap trap_handler INT TERM EXIT

# Assertions Helpers
assert_contains() {
    local file="$1"
    local pattern="$2"
    local msg="$3"
    if ! grep -q "$pattern" "$file"; then
        log_error "Assertion failed: $msg (Pattern '$pattern' not found in $file)"
        exit 1
    fi
    log_success "Verified: $msg"
}

assert_exit_code() {
    local cmd="$1"
    local expected="$2"
    local msg="$3"
    set +e
    eval "$cmd" >/dev/null 2>&1
    local actual=$?
    set -e
    if [ $actual -ne $expected ]; then
        log_error "Assertion failed: $msg (Expected exit code $expected, got $actual)"
        exit 1
    fi
    log_success "Verified: $msg"
}

assert_output_contains() {
    local cmd="$1"
    local pattern="$2"
    local msg="$3"
    set +e
    local output=$(eval "$cmd" 2>&1)
    local actual=$?
    set -e
    if ! echo "$output" | grep -q "$pattern"; then
        log_error "Assertion failed: $msg (Pattern '$pattern' not found in output: '$output')"
        exit 1
    fi
    log_success "Verified: $msg"
}

# ==============================================================================
# SCENARIO 1: Standard Start, Status, Logs, and Stop Lifecycle
# ==============================================================================
run_scenario_1() {
    log_info "------------------------------------------------------------"
    log_info "Scenario 1: Standard Lifecycle Operations"
    log_info "------------------------------------------------------------"
    
    # Ensure starting in a clean/stopped state
    rm -f "$LOCK_FILE" "$LOG_FILE"
    
    assert_output_contains "$DAEMON_BIN status" "Daemon is stopped" "Status reports stopped when daemon is inactive"
    
    # Start the daemon
    log_info "Starting daemon..."
    assert_output_contains "$DAEMON_BIN start" "Daemon started" "Daemon starts successfully"
    
    # Verify Lockfile exists and contains a valid active PID
    if [ ! -f "$LOCK_FILE" ]; then
        log_error "Lockfile was not created!"
        exit 1
    fi
    local d_pid=$(cat "$LOCK_FILE" 2>/dev/null)
    if [ -z "$d_pid" ] || ! ps -p "$d_pid" >/dev/null 2>&1; then
        log_error "Lockfile does not contain a valid running PID! Got: '$d_pid'"
        exit 1
    fi
    log_success "Verified: Lockfile exists with active PID $d_pid"
    
    assert_output_contains "$DAEMON_BIN status" "Daemon is running (PID: $d_pid)" "Status reports running with correct PID"
    
    # Wait for daemon to write initial start log
    sleep 1
    
    assert_contains "$LOG_FILE" "Daemon loop started" "Daemon writes loop startup log to daemon.log"
    assert_output_contains "$DAEMON_BIN logs" "Daemon loop started" "Daemon logs command displays background log file content"
    
    # Stop the daemon
    log_info "Stopping daemon..."
    assert_output_contains "$DAEMON_BIN stop" "Daemon stopped" "Daemon stops gracefully"
    
    if [ -f "$LOCK_FILE" ]; then
        log_error "Lockfile was not removed after graceful stop!"
        exit 1
    fi
    log_success "Verified: Lockfile removed on graceful stop"
    
    assert_output_contains "$DAEMON_BIN status" "Daemon is stopped" "Status reports stopped after termination"
}

# ==============================================================================
# SCENARIO 2: Graceful Termination via POSIX signals
# ==============================================================================
run_scenario_2() {
    log_info "------------------------------------------------------------"
    log_info "Scenario 2: Graceful Termination via POSIX signals"
    log_info "------------------------------------------------------------"
    
    rm -f "$LOCK_FILE" "$LOG_FILE"
    
    # Start the daemon
    "$DAEMON_BIN" start >/dev/null 2>&1
    sleep 0.5
    
    local d_pid=$(cat "$LOCK_FILE" 2>/dev/null)
    if [ -z "$d_pid" ] || ! ps -p "$d_pid" >/dev/null 2>&1; then
        log_error "Failed to start daemon for signal test."
        exit 1
    fi
    
    log_info "Sending SIGTERM to daemon PID $d_pid..."
    kill -15 "$d_pid"
    
    # Wait for daemon to gracefully unlink and exit (up to 3 seconds)
    local stopped=false
    for i in {1..30}; do
        if [ ! -f "$LOCK_FILE" ] && ! ps -p "$d_pid" >/dev/null 2>&1; then
            stopped=true
            break
        fi
        sleep 0.1
    done
    
    if [ "$stopped" != "true" ]; then
        log_error "Daemon did not shut down gracefully on SIGTERM within 3 seconds."
        exit 1
    fi
    
    log_success "Verified: Daemon processed SIGTERM, cleaned lockfile, and exited gracefully."
}

# ==============================================================================
# SCENARIO 3: Crash Recovery & Self-Healing of Stale Locks
# ==============================================================================
run_scenario_3() {
    log_info "------------------------------------------------------------"
    log_info "Scenario 3: Crash Recovery & Self-Healing of Stale Locks"
    log_info "------------------------------------------------------------"
    
    rm -f "$LOCK_FILE" "$LOG_FILE"
    
    # Start the daemon
    "$DAEMON_BIN" start >/dev/null 2>&1
    sleep 0.5
    
    local d_pid=$(cat "$LOCK_FILE" 2>/dev/null)
    if [ -z "$d_pid" ] || ! ps -p "$d_pid" >/dev/null 2>&1; then
        log_error "Failed to start daemon for crash recovery test."
        exit 1
    fi
    
    log_info "Simulating daemon crash by sending SIGKILL to PID $d_pid..."
    kill -9 "$d_pid"
    sleep 0.5
    
    if [ ! -f "$LOCK_FILE" ]; then
        log_error "Crash simulation failed: Lockfile was removed when it shouldn't have been."
        exit 1
    fi
    log_success "Verified: Lockfile remains after sudden crash"
    
    assert_output_contains "$DAEMON_BIN status" "Daemon is dead but stale PID lock file exists" "Status reports stale PID lock"
    
    # Start the daemon again and verify recovery
    log_info "Starting daemon with stale lock present..."
    assert_output_contains "$DAEMON_BIN start" "Warning: Stale lockfile found with dead PID" "Start command detects stale lock and issues warning"
    
    local new_pid=$(cat "$LOCK_FILE" 2>/dev/null)
    if [ -z "$new_pid" ] || [ "$new_pid" = "$d_pid" ] || ! ps -p "$new_pid" >/dev/null 2>&1; then
        log_error "Failed to self-heal and start a new daemon process."
        exit 1
    fi
    log_success "Verified: Daemon self-healed, cleared stale lock, and restarted on PID $new_pid"
    
    # Clean up
    "$DAEMON_BIN" stop >/dev/null 2>&1
}

# ==============================================================================
# SCENARIO 4: Active PID Conflict Guard
# ==============================================================================
run_scenario_4() {
    log_info "------------------------------------------------------------"
    log_info "Scenario 4: Active PID Conflict Guard"
    log_info "------------------------------------------------------------"
    
    rm -f "$LOCK_FILE"
    
    # Manually write the current script PID ($$) to the LOCK_FILE
    echo "$$" > "$LOCK_FILE"
    
    assert_output_contains "$DAEMON_BIN status" "Daemon is running (PID: $$)" "Status sees active PID manually written to lock"
    
    # Attempt to start daemon, expecting it to refuse
    log_info "Attempting to start daemon while active PID is locked..."
    assert_exit_code "$DAEMON_BIN start" 1 "Daemon fails to start with active PID lock"
    
    # Verify lock file has not been overwritten
    local locked_pid=$(cat "$LOCK_FILE" 2>/dev/null)
    if [ "$locked_pid" != "$$" ]; then
        log_error "Active lockfile was overwritten during conflicting startup attempt!"
        exit 1
    fi
    log_success "Verified: Daemon blocks startup and retains original active lock PID"
    
    rm -f "$LOCK_FILE"
}

# ==============================================================================
# SCENARIO 5: Stale / Inactive Lock Recovery
# ==============================================================================
run_scenario_5() {
    log_info "------------------------------------------------------------"
    log_info "Scenario 5: Stale / Inactive Lock Recovery"
    log_info "------------------------------------------------------------"
    
    rm -f "$LOCK_FILE"
    
    # Find a guaranteed dead PID
    sleep 0.05 &
    local dead_pid=$!
    wait $dead_pid
    
    # Write dead PID to lock file
    echo "$dead_pid" > "$LOCK_FILE"
    
    assert_output_contains "$DAEMON_BIN status" "Daemon is dead but stale PID lock file exists" "Status identifies stale PID lock"
    
    # Start daemon, expecting it to self-heal and start successfully
    log_info "Starting daemon with inactive PID lock..."
    assert_output_contains "$DAEMON_BIN start" "Warning: Stale lockfile found with dead PID" "Daemon recovers stale inactive lock on start"
    
    local new_pid=$(cat "$LOCK_FILE" 2>/dev/null)
    if [ -z "$new_pid" ] || [ "$new_pid" = "$dead_pid" ] || ! ps -p "$new_pid" >/dev/null 2>&1; then
        log_error "Daemon did not self-heal and start on inactive lock."
        exit 1
    fi
    log_success "Verified: Daemon self-heals from manually written inactive lock"
    
    "$DAEMON_BIN" stop >/dev/null 2>&1
}

# ==============================================================================
# SCENARIO 6: Log capturing & continuous queue-polling orchestrator invocation
# ==============================================================================
run_scenario_6() {
    log_info "------------------------------------------------------------"
    log_info "Scenario 6: Log Capturing & Queue-Polling Redirection"
    log_info "------------------------------------------------------------"
    
    rm -f "$LOCK_FILE" "$LOG_FILE"
    rm -f "$QUEUE_DIR/99_test.json"
    mkdir -p "$QUEUE_DIR"
    
    # 1. Back up real orchestrator
    log_info "Backing up real orchestrator..."
    mv "$ORCHESTRATOR_BIN" "$ORCHESTRATOR_BIN.bak"
    
    # 2. Write mock orchestrator
    log_info "Installing mock orchestrator..."
    cat <<'EOF' > "$ORCHESTRATOR_BIN"
#!/usr/bin/env python3
import sys
print(f"Mock orchestrator invoked with args: {sys.argv[1:]}")
print("Line 2 from mock orchestrator")
sys.exit(0)
EOF
    chmod +x "$ORCHESTRATOR_BIN"
    
    # 3. Start the daemon
    "$DAEMON_BIN" start >/dev/null 2>&1
    sleep 0.5
    
    # 4. Write dummy trigger file
    log_info "Writing temporary trigger 99_test.json..."
    echo '{"test_daemon_polling": true}' > "$QUEUE_DIR/99_test.json"
    
    # 5. Wait for daemon loop to poll (poll interval is 2s)
    log_info "Waiting for daemon to poll queue (approx 3 seconds)..."
    sleep 3
    
    # 6. Stop the daemon immediately so we don't pollute logs further
    "$DAEMON_BIN" stop >/dev/null 2>&1
    
    # 7. Check logs for discovery, execution, and completion markers
    assert_contains "$LOG_FILE" "Discovered trigger: 99_test.json. Invoking orchestrator..." "Log contains queue discovery message"
    assert_contains "$LOG_FILE" "\[ORCHESTRATOR\] Mock orchestrator invoked with args: \['99_test.json'\]" "Log contains orchestrator output redirect with prefix"
    assert_contains "$LOG_FILE" "\[ORCHESTRATOR\] Line 2 from mock orchestrator" "Log contains full multiline orchestrator stream"
    assert_contains "$LOG_FILE" "Orchestrator successfully completed trigger: 99_test.json" "Log contains trigger completion message"
    
    # 8. Restore real orchestrator
    log_info "Restoring real orchestrator..."
    mv "$ORCHESTRATOR_BIN.bak" "$ORCHESTRATOR_BIN"
    rm -f "$QUEUE_DIR/99_test.json"
}

# ==============================================================================
# SCENARIO 7: Missing & Unwritable Directories Handling
# ==============================================================================
run_scenario_7() {
    log_info "------------------------------------------------------------"
    log_info "Scenario 7: Missing & Unwritable Directories Handling"
    log_info "------------------------------------------------------------"
    
    rm -f "$LOCK_FILE" "$LOG_FILE"
    
    # 1. Missing directory creation check
    log_info "Testing missing locks/logs directories automatic creation..."
    mv "$LOCKS_DIR" "$LOCKS_DIR.tmp"
    mv "$LOGS_DIR" "$LOGS_DIR.tmp"
    
    # Try to start daemon - it should recreate both directories and start
    assert_output_contains "$DAEMON_BIN start" "Daemon started" "Daemon successfully starts even if locks/logs directories are missing"
    
    if [ ! -d "$LOCKS_DIR" ]; then
        log_error "LOCKS_DIR was not automatically recreated!"
        exit 1
    fi
    if [ ! -d "$LOGS_DIR" ]; then
        log_error "LOGS_DIR was not automatically recreated!"
        exit 1
    fi
    log_success "Verified: locks/logs directories were automatically recreated with standard permissions."
    
    # Stop daemon
    "$DAEMON_BIN" stop >/dev/null 2>&1
    
    # Restore original directories
    rm -rf "$LOCKS_DIR" "$LOGS_DIR"
    mv "$LOCKS_DIR.tmp" "$LOCKS_DIR"
    mv "$LOGS_DIR.tmp" "$LOGS_DIR"
    
    # 2. Unwritable directory failure check
    log_info "Testing unwritable locks directory failure handling..."
    local orig_perm=$(stat -c "%a" "$LOCKS_DIR")
    chmod 500 "$LOCKS_DIR"
    
    assert_exit_code "$DAEMON_BIN start" 1 "Daemon startup fails cleanly when locks directory is unwritable"
    
    chmod "$orig_perm" "$LOCKS_DIR"
}

# ==============================================================================
# Main Verification Execution Flow
# ==============================================================================
log_info "================================================================"
log_info "  STARTING DAEMON LIFECYCLE & INTEGRATION TESTS (EPIC E13.4)"
log_info "================================================================"

run_scenario_1
run_scenario_2
run_scenario_3
run_scenario_4
run_scenario_5
run_scenario_6
run_scenario_7

# Run cleanup successfully before standard exit
cleanup_workspace

# Disable trap handler to prevent double execution on script termination
trap - INT TERM EXIT

echo -e "\n${GREEN}======================================================================${NC}"
echo -e "${GREEN}  ALL DAEMON LIFECYCLE & INTEGRATION TEST SCENARIOS PASSED!         ${NC}"
echo -e "${GREEN}======================================================================${NC}"
log_success "E2E Integration Verification script complete."
exit 0
