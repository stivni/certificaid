#!/usr/bin/env bash
# pre-commit-records-parity.sh — Controleer disk/RAG/content parity voor concept-records.
#
# Blokkerend: bij drift (disk↔RAG én disk↔content) blokkeert de commit.
# Geen override-vlag op hook-niveau.
# Override: git commit --no-verify (expliciete keuze van de gebruiker).
#
# ADR-019 §"Pre-commit hook gedrag — strict" + §"Content-sync"
set -euo pipefail

GEWIJZIGD_RECORDS=0
GEWIJZIGD_CONTENT=0

if git diff --cached --name-only | grep -q "^data/concepten/records/"; then
  GEWIJZIGD_RECORDS=1
fi
if git diff --cached --name-only | grep -q "^content/concepten/"; then
  GEWIJZIGD_CONTENT=1
fi

if [ "$GEWIJZIGD_RECORDS" -eq 1 ] || [ "$GEWIJZIGD_CONTENT" -eq 1 ]; then
  echo "→ records-parity: concept-records of content-fiches gewijzigd — audit starten …"
  if ! python3 -m tools.lib.records_api audit; then
    echo ""
    echo "✗ records-parity MISLUKT — commit geblokkeerd."
    echo "  Drift-types: disk↔RAG (ghosts/missing) en/of disk↔content (content_ontbreekt/content_extra)"
    echo "  Herstel drift via: python3 -m tools.lib.records_api audit --fix"
    echo "  Of herindexeer:    python3 -m tools.lib.records_api reindex-all"
    echo "  Override (nood):   git commit --no-verify"
    exit 1
  fi
  echo "✓ records-parity OK (disk + RAG + content in sync)"
fi
