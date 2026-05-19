#!/usr/bin/env bash
# Exporteer per programmaonderdeel een NotebookLM-bundel.
# Bundel = minicursus + gerefereerde concept-fiches + competentie-fiches.
# Gebruik: bash tools/export/export-notebooklm.sh [1.1 1.2 ...]
# Zonder argumenten: alle PO's onder content/studiemateriaal/.

set -e
cd "$(dirname "$0")/../.."

STUDIE_DIR="content/studiemateriaal"
CONCEPTEN_DIR="content/concepten"
COMP_DIR="content/competenties"
EXPORT_DIR="export"

if [ $# -gt 0 ]; then
  PO_NUMS=("$@")
else
  PO_NUMS=()
  while IFS= read -r f; do
    bn=$(basename "$f" .md)
    pn=$(echo "$bn" | grep -oE '^[0-9]+-[0-9]+' | tr '-' '.')
    [ -n "$pn" ] && PO_NUMS+=("$pn")
  done < <(find "$STUDIE_DIR" -maxdepth 1 -name "[0-9]*-*.md" | sort)
fi

for po in "${PO_NUMS[@]}"; do
  slug=$(echo "$po" | tr '.' '-')
  minicursus=$(find "$STUDIE_DIR" -maxdepth 1 -name "${slug}-*.md" 2>/dev/null | head -1)
  if [ -z "$minicursus" ]; then
    echo "⚠️  PO $po: minicursus niet gevonden in $STUDIE_DIR/"
    continue
  fi

  out_dir="$EXPORT_DIR/$po"
  rm -rf "$out_dir"
  mkdir -p "$out_dir"

  cp "$minicursus" "$out_dir/"

  # Verzamel wikilinks uit minicursus, sla cast-namen en wettekst-paden over
  while IFS= read -r link; do
    case "$link" in
      [A-Z]*) continue ;;
    esac
    found=$(find "$CONCEPTEN_DIR" "$COMP_DIR" -maxdepth 1 -name "${link}.md" 2>/dev/null | head -1)
    [ -n "$found" ] && cp "$found" "$out_dir/"
  done < <(
    grep -ohE '\[\[([^]|#]+)' "$minicursus" \
      | sed 's/\[\[//' \
      | grep -Ev '^(wetteksten|bronnen|normen|adviezen)/|^[0-9]' \
      | sort -u
  )

  count=$(ls "$out_dir" | wc -l | tr -d ' ')
  echo "✅  export/$po/ — $count bestanden"
done
