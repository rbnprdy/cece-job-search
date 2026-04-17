#!/usr/bin/env bash
# backup.sh — Commit and push the current state of the job search tracker to GitHub.
#
# Safe by design:
#   - set -euo pipefail: any failure aborts the script (no silent skips)
#   - Runs from the repo root regardless of the caller's cwd
#   - Refuses to run if the remote isn't the expected backup repo
#   - Never uses --force, --force-with-lease, or any destructive flag
#   - Pushes only the current branch; no wildcard refspecs
#   - Exits cleanly on "nothing to commit" (returns 0, no fake commits)
#
# Usage:
#   ./backup.sh                     # uses auto-generated timestamped commit message
#   ./backup.sh "My message"        # uses the provided commit message

set -euo pipefail

# --- Resolve repo root (directory containing this script) ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# --- Safety: confirm we're in the expected repo ---
EXPECTED_REMOTE="https://github.com/rbnprdy/cece-job-search.git"
ACTUAL_REMOTE="$(git config --get remote.origin.url || echo '')"
if [[ "$ACTUAL_REMOTE" != "$EXPECTED_REMOTE" ]]; then
    echo "ERROR: remote.origin.url is '$ACTUAL_REMOTE', expected '$EXPECTED_REMOTE'" >&2
    echo "Refusing to push — are you sure this is the right repo?" >&2
    exit 1
fi

# --- Safety: confirm we're on main ---
CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"
if [[ "$CURRENT_BRANCH" != "main" ]]; then
    echo "ERROR: expected to be on branch 'main', got '$CURRENT_BRANCH'" >&2
    exit 1
fi

# --- Stage everything (gitignore excludes credentials and temp files) ---
git add -A

# --- Bail cleanly if there are no changes ---
if git diff --cached --quiet; then
    echo "backup.sh: nothing to commit, skipping push."
    exit 0
fi

# --- Commit with the provided message, or a timestamped default ---
if [[ $# -gt 0 ]]; then
    COMMIT_MSG="$1"
else
    COMMIT_MSG="Automated backup $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
fi
git commit -m "$COMMIT_MSG"

# --- Push. Explicitly naming branch on both sides; no force flags anywhere ---
git push origin main

echo "backup.sh: pushed successfully."
