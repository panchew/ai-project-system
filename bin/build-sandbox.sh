#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status
set -euo pipefail

# Define colors
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

log_success() {
    echo -e "${GREEN}[✓] $1${NC}"
}

log_error() {
    echo -e "${RED}[!] $1${NC}" >&2
}

# 1. Build the image
echo "Building the sandbox Docker image..."
if docker build -f Dockerfile.sandbox -t ai-project-sandbox:latest .; then
    log_success "Docker image 'ai-project-sandbox:latest' built successfully."
else
    log_error "Failed to build Docker image."
    exit 1
fi

# 2. Perform functional verification
echo "Starting functional verification..."

# Check whoami
echo "Checking execution user..."
CONTAINER_USER=$(docker run --rm ai-project-sandbox:latest whoami 2>/dev/null || true)
# Trim whitespace
CONTAINER_USER=$(echo "$CONTAINER_USER" | tr -d '[:space:]')
if [ "$CONTAINER_USER" = "sandbox" ]; then
    log_success "Container executes as user 'sandbox'."
else
    log_error "Container executes as user '$CONTAINER_USER', expected 'sandbox'."
    exit 1
fi

# Check python3 and node versions
echo "Checking Python 3 installation..."
if docker run --rm ai-project-sandbox:latest python3 --version >/dev/null 2>&1; then
    PYTHON_VER=$(docker run --rm ai-project-sandbox:latest python3 --version)
    log_success "Python 3 is available: $PYTHON_VER"
else
    log_error "Python 3 is not available in the sandbox."
    exit 1
fi

echo "Checking Node.js installation..."
if docker run --rm ai-project-sandbox:latest node --version >/dev/null 2>&1; then
    NODE_VER=$(docker run --rm ai-project-sandbox:latest node --version)
    log_success "Node.js is available: $NODE_VER"
else
    log_error "Node.js is not available in the sandbox."
    exit 1
fi

# Verify write access to volume-mounted folder
echo "Verifying volume mount write permissions..."
HOST_TEMP_DIR=$(mktemp -d /tmp/sandbox-test.XXXXXX)
# Make the host directory writable by the sandbox user
chmod 777 "$HOST_TEMP_DIR"

# Ensure host directory is cleaned up on exit
trap 'rm -rf "$HOST_TEMP_DIR"' EXIT

if docker run --rm -v "$HOST_TEMP_DIR:/workspace/test-volume" ai-project-sandbox:latest bash -c "echo 'verification-successful' > /workspace/test-volume/verified.txt" 2>/dev/null; then
    if [ -f "$HOST_TEMP_DIR/verified.txt" ] && grep -q "verification-successful" "$HOST_TEMP_DIR/verified.txt"; then
        log_success "Volume mount write permissions verified successfully."
    else
        log_error "Volume mount write succeeded in container but file not found/verified on host."
        exit 1
    fi
else
    log_error "Failed to write to volume-mounted directory from within container."
    exit 1
fi

log_success "All sandbox container verifications passed successfully!"
