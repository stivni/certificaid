#!/usr/bin/env bash
# Worktree-status + cleanup helper.
#
# Lijst alle worktrees met categorisering:
#   MERGED   — HEAD reachable from main; geen lost werk (veilig te prunen mits 0 uncommitted)
#   AHEAD=N  — HEAD heeft N commits NIET in main; potentieel werk dat moet gemerged worden
#   BROKEN   — worktree-dir bestaat maar .git pointer is kapot; veilig te wissen
#
# Plus uncommitted-count per worktree.
#
# Gebruik:
#   tools/worktree_status.sh                # lijst alleen
#   tools/worktree_status.sh --prune-safe   # prune MERGED + uncommitted=0 + BROKEN
#   tools/worktree_status.sh --warn-age N   # exit code 1 als er agent-worktrees zijn ≥ N dagen oud (voor hooks)
#
# Geen --force, geen interactie. Voor de risicovolle worktrees (AHEAD of MERGED+uncommitted):
# gewoon zelf bekijken en beslissen.

set -uo pipefail

cd "$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "not in a git repo"; exit 1; }

MODE="${1:-list}"

prune_one() {
  local wt="$1"
  git worktree unlock "$wt" 2>/dev/null
  if [ -e "$wt/.git" ]; then
    git worktree remove --force "$wt" 2>&1 | head -1
  else
    rm -rf "$wt" && echo "removed broken $wt"
  fi
}

count_old=0
list_lines=()

for wt in .claude/worktrees/agent-*/; do
  [ -d "$wt" ] || continue
  base=$(basename "$wt")
  if [ ! -e "$wt/.git" ]; then
    list_lines+=("$base | BROKEN")
    if [ "$MODE" = "--prune-safe" ]; then prune_one "$wt"; fi
    continue
  fi
  head=$(git -C "$wt" rev-parse HEAD 2>/dev/null)
  dirty=$(git -C "$wt" status --porcelain 2>/dev/null | wc -l | tr -d ' ')
  if git merge-base --is-ancestor "$head" main 2>/dev/null; then
    cat="MERGED"
  else
    ahead=$(git rev-list --count main.."$head" 2>/dev/null || echo "?")
    cat="AHEAD=$ahead"
  fi
  # Age in days (mtime of the worktree dir)
  age=$(( ( $(date +%s) - $(stat -f %m "$wt" 2>/dev/null || stat -c %Y "$wt") ) / 86400 ))
  list_lines+=("$base | head=${head:0:8} | uncommitted=$dirty | $cat | age=${age}d")

  if [ "$MODE" = "--prune-safe" ] && [ "$cat" = "MERGED" ] && [ "$dirty" = "0" ]; then
    prune_one "$wt"
  fi

  if [[ "$MODE" == "--warn-age" ]] && [ "$age" -ge "${2:-7}" ]; then
    count_old=$(( count_old + 1 ))
  fi
done

if [ "$MODE" = "--warn-age" ]; then
  if [ "$count_old" -gt 0 ]; then
    echo "WARN: $count_old worktree(s) ≥ ${2:-7} dagen oud — run: tools/worktree_status.sh"
    exit 1
  fi
  exit 0
fi

if [ ${#list_lines[@]} -eq 0 ]; then
  echo "Geen agent-worktrees gevonden."
else
  printf '%s\n' "${list_lines[@]}"
fi

git worktree prune
