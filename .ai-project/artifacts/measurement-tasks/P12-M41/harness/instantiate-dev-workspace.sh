#!/bin/sh
# Instantiate TASK-DEV-1's workspace for one measurement run.
#
# Copies `dev-task/workspace/` ONLY. The reference solution lives in
# `dev-task/ground-truth/` and is never copied, so the answer cannot reach a run.
#
# The destination directory is always named `e412-dev-workspace` because the task's
# tool set scopes allow_paths to `*/e412-dev-workspace/**` -- the runner's
# path_permitted() fnmatchcases an always-absolute resolved path, so an absolute-path
# glob is the only kind that can match, and matching by directory name keeps it
# machine-independent (the same fix P7-M26-E26.3 landed for this repo's own tools.json).
#
# git init + one commit gives C-B its `worktree` provenance: files changed is then a
# measurement of the tree, not a claim by the model.
#
# Usage: instantiate-dev-workspace.sh <parent-dir>

set -eu

if [ $# -ne 1 ]; then
    echo "usage: $0 <parent-dir>" >&2
    exit 3
fi

SRC="$(CDPATH= cd -- "$(dirname -- "$0")/../dev-task/workspace" && pwd)"
DEST="$1/e412-dev-workspace"

if [ -e "$DEST" ]; then
    echo "[instantiate] refusing to overwrite existing $DEST" >&2
    exit 3
fi

mkdir -p "$1"
cp -r "$SRC" "$DEST"
git -C "$DEST" init -q
git -C "$DEST" add -A
git -C "$DEST" -c user.email=e412@example.com -c user.name=E412 commit -q -m "TASK-DEV-1 workspace as instantiated"
echo "$DEST"
