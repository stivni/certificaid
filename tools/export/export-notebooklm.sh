#!/usr/bin/env bash
# Exporteer alle PO-fiches naar export/[PO]/ voor gebruik in NotebookLM.
# Gebruik: bash tools/export-notebooklm.sh [optioneel: 2.1 2.6 ...]
# Zonder argumenten: alle PO's.

set -e
cd "$(dirname "$0")/.."

PO_DIR="content/programmaonderdelen"
MATERIE_DIR="content/materie"
COMP_DIR="content/competenties"
EXPORT_DIR="export"

if [ $# -gt 0 ]; then
  PO_FILES=()
  for po in "$@"; do
    f=$(find "$PO_DIR" -name "${po}-*.md" 2>/dev/null | head -1)
    [ -n "$f" ] && PO_FILES+=("$f") || echo "⚠️  PO $po niet gevonden"
  done
else
  mapfile -t PO_FILES < <(find "$PO_DIR" -name "*.md" | sort)
fi

for po_file in "${PO_FILES[@]}"; do
  basename=$(basename "$po_file" .md)
  po_num=$(echo "$basename" | grep -oE '^[0-9]+\.[0-9]+')
  [ -z "$po_num" ] && continue

  out_dir="$EXPORT_DIR/$po_num"
  rm -rf "$out_dir"
  mkdir -p "$out_dir"

  cp "$po_file" "$out_dir/"

  while IFS= read -r link; do
    found=$(find "$MATERIE_DIR" "$COMP_DIR" -name "${link}.md" 2>/dev/null | head -1)
    [ -n "$found" ] && cp "$found" "$out_dir/"
  done < <(
    grep -ohE '\[\[([^]|#]+)' "$po_file" \
      | sed 's/\[\[//' \
      | grep -Ev '^(wetteksten|bronnen|normen|adviezen)/|^[0-9]' \
      | sort -u
  )

  count=$(ls "$out_dir" | wc -l | tr -d ' ')
  echo "✅  export/$po_num/ — $count bestanden"
done
