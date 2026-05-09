"""CBN-advies extractor voor de collection-pipeline (ADR-005 §2 + collections-uitbreiding).

Inputs:
    cfg = {
        "bron": "<advies-URL op cbn-cnc.be>",
        "bron_rol": "interpretatief",
        ...                  # andere frontmatter-velden uit de huidige MD
    }
    source_name = bestand-stem (bv. "CBN-2022-15-leasing")

Output:
    string met de markdown-body (geen frontmatter, geen H1-titel — die worden
    door de orchestrator toegevoegd).

Roept ``tools.lib.cbn_advies_html.scrape_advies(url)`` aan en geeft de
``body``-string terug. De orchestrator voegt frontmatter, H1, footnotes en
provenance toe.
"""
from __future__ import annotations

from tools.lib.cbn_advies_html import scrape_advies


def extract(cfg: dict, source_name: str) -> str:
    """Scrape een CBN-advies en geef de markdown-body terug.

    Raised RuntimeError als de URL ontbreekt of de fetch mislukt — de
    orchestrator vangt dit en logt een skip per item.
    """
    url = cfg.get("bron")
    if not url or not str(url).startswith(("http://", "https://")):
        raise RuntimeError(
            f"{source_name}: geen geldige URL in 'bron'-veld (kreeg {url!r})"
        )

    result = scrape_advies(url)
    body = result.get("body", "")
    if not body.strip():
        raise RuntimeError(f"{source_name}: lege body na scrape ({url})")

    # Voeg titel als H1 toe als die niet al in body staat.
    title = (result.get("title") or "").strip()
    if title and not body.lstrip().startswith("# "):
        body = f"# {title}\n\n{body}"

    return body
