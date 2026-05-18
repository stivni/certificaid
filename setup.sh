#!/usr/bin/env bash
# Streamlit Cloud startup: download de RAG-snapshot uit de "embeddings-latest"
# GitHub Release en pak uit naar data/rag/main/.
# Idempotent: skipt download als chroma.sqlite3 al bestaat.
set -euo pipefail

cd "$(dirname "$0")"

REPO="stivni/certificaid"
TAG="embeddings-latest"
ASSET="rag-main.tar.zst"
TARGET="data/rag/main"

if [[ -f "$TARGET/chroma.sqlite3" ]]; then
  echo "✓ RAG-index al aanwezig, skip download."
  exit 0
fi

echo "→ Downloading $ASSET van $REPO release $TAG ..."
mkdir -p "$TARGET"
curl -sSL "https://github.com/$REPO/releases/download/$TAG/$ASSET" -o "/tmp/$ASSET"

echo "→ Uitpakken naar $TARGET ..."
tar --zstd -xf "/tmp/$ASSET" -C data/rag
rm -f "/tmp/$ASSET"

echo "✅ RAG-index klaar."
