#!/usr/bin/env bash
# Upload data/rag/main/ als asset op de GitHub Release "embeddings-latest".
# Overschrijft de bestaande asset. Doorloop wanneer je je Streamlit-deploy
# een nieuwe RAG-snapshot wil geven.
set -euo pipefail

cd "$(dirname "$0")/../.."

if ! command -v gh > /dev/null; then
  echo "❌ gh CLI ontbreekt. Install met: brew install gh && gh auth login"
  exit 1
fi

if [[ ! -d data/rag/main ]] || [[ -z "$(ls -A data/rag/main 2>/dev/null)" ]]; then
  echo "❌ data/rag/main/ is leeg of bestaat niet."
  exit 1
fi

TAG="embeddings-latest"
ASSET="rag-main.tar.zst"

echo "→ Tarring data/rag/main/ ..."
tar --zstd -cf "$ASSET" -C data/rag main
SIZE=$(du -h "$ASSET" | cut -f1)
echo "  $ASSET ($SIZE)"

if ! gh release view "$TAG" > /dev/null 2>&1; then
  echo "→ Release $TAG bestaat niet, aanmaken ..."
  gh release create "$TAG" --title "Embeddings (rolling)" --notes "RAG-snapshot. Wordt overschreven bij elke nieuwe upload."
fi

echo "→ Bestaande asset weghalen (indien aanwezig) ..."
gh release delete-asset "$TAG" "$ASSET" --yes 2>/dev/null || true

echo "→ Uploading ..."
gh release upload "$TAG" "$ASSET"

rm -f "$ASSET"
echo "✅ Klaar. Streamlit pickt deze op via setup.sh bij volgende deploy/reboot."
