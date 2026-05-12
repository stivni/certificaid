#!/usr/bin/env bash
# Installeer versioneerde git-hooks uit scripts/git-hooks/ in .git/hooks/.
# Idempotent: bestaande hooks worden vervangen.
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
SRC="$REPO_ROOT/scripts/git-hooks"
DEST="$REPO_ROOT/.git/hooks"

for hook in "$SRC"/*; do
    name="$(basename "$hook")"
    cp "$hook" "$DEST/$name"
    chmod +x "$DEST/$name"
    echo "✓ installed: $name"
done
