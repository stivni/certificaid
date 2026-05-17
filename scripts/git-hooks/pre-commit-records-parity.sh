#!/usr/bin/env bash
# pre-commit-records-parity.sh — Controleer disk/RAG parity voor concept-records.
#
# Blokkerend: bij drift blokkeert de commit. Geen override-vlag op hook-niveau.
# Override: git commit --no-verify (expliciete keuze van de gebruiker).
#
# ADR-019 §"Pre-commit hook gedrag — strict"
set -euo pipefail

if git diff --cached --name-only | grep -q "^data/concepten/records/"; then
  echo "→ records-parity: concept-records gewijzigd — audit starten …"
  if ! python3 -m tools.lib.records_api audit; then
    echo ""
    echo "✗ records-parity MISLUKT — commit geblokkeerd."
    echo "  Herstel drift via: python3 -m tools.lib.records_api audit --fix"
    echo "  Of herindexeer:    python3 -m tools.lib.records_api reindex-all"
    echo "  Override (nood):   git commit --no-verify"
    exit 1
  fi
  echo "✓ records-parity OK"
fi
