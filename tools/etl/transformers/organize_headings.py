"""
Transformer: organize_headings (ADR-005 §4) — placeholder/noop.

De huidige `tools/lib/headings.py::process_wettekst` combineert heading-injectie
en heading-organisatie in één stap. Een aparte `organize_headings`-transformer
wordt pas zinvol wanneer we inject_headings_wettekst opsplitsen in:
  1. inject_headings_wettekst — structuurlabels → markdown-niveaus
  2. organize_headings       — hiërarchie normaliseren, max 6 niveaus, parent-child

TODO (vervolgrefactor, Fase 2 ADR-005):
  - Extraheer de conditional-flattening logica uit headings.py als aparte stap.
  - Maak organize_headings een echte implementatie.
  - Verwijder dan de flattening uit inject_headings_wettekst.

Signature: (body: str, frontmatter: dict) -> tuple[str, dict]
"""
from __future__ import annotations


def organize_headings(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Noop-placeholder — heading-organisatie zit momenteel in inject_headings_wettekst."""
    return body, frontmatter
