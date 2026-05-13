r"""Transformer: strip opgeheven KB-versie als 'Bijlage' appendix.

Fisconet-compilatie voegt soms de OPGEHEVEN oudere versie van een KB
als 'Bijlage' toe aan het nieuwere KB. Voorbeeld in WBTW-KB50:

  ### Art. 17
  De minister bevoegd voor Financiën...

  Bijlage
  Btw-opgave van de intracommunautaire handelingen

  Koninklijk besluit nr. 50 van 9 december 2009 ...
  Dit koninklijk besluit werd vervangen met ingang van 01.01.2020
  door het Koninklijk besluit nr. 50, van 11 december 2019 ...

  ### Art. 1
  De belastingplichtigen ...
  ...

De 'Bijlage' is geen echte bijlage maar een herhaling van de hele
opgeheven wet. Voor een RAG-index is alleen de CURRENT versie relevant.

Detectie-heuristiek:
1. Vind regel `^Bijlage$` (met of zonder ##) gevolgd door subtitle.
2. Binnen 20 regels: vind een 'Koninklijk besluit nr. X van [datum]'
   intro + 'werd vervangen' of '(Officieuze coördinatie)' marker.
3. Strip vanaf 'Bijlage' tot einde body.

Conservatief: vereist EXPLICIETE 'werd vervangen' sentinel zodat we
echte bijlagen (zoals tabel-bijlagen) niet strippen.

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

_BIJLAGE_HEADER_RE = re.compile(
    r"^(?:#{1,6}\s+)?Bijlage\s*$",
    re.M,
)

_VERVANGEN_SENTINEL_RE = re.compile(
    r"\bDit\s+(?:koninklijk\s+besluit|MB|ministerieel\s+besluit)\s+werd\s+vervangen\b",
    re.I,
)


def strip_opgeheven_kb_appendix(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Strip opgeheven KB-versie ingebed als 'Bijlage'-sectie tot einde body."""
    matches = list(_BIJLAGE_HEADER_RE.finditer(body))
    if not matches:
        return body, frontmatter
    for m in matches:
        # Bekijk de 2000 chars na 'Bijlage' voor de 'werd vervangen' sentinel.
        scope = body[m.end():m.end() + 2500]
        if _VERVANGEN_SENTINEL_RE.search(scope):
            # Strip van Bijlage-header tot einde body.
            new_body = body[:m.start()].rstrip() + "\n"
            return new_body, frontmatter
    return body, frontmatter
