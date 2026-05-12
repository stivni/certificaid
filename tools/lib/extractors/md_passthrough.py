"""md_passthrough — extractor voor handmatig samengestelde Markdown-bronnen.

Sommige bronnen hebben geen scriptbare raw-input (PDF/HTML) — ze zijn
handmatig samengesteld uit fragmenten of door iemand uitgetypt. Toch willen
we ze door de pipeline laten lopen (ADR-005 §1 "Deterministisch herloadbaar"
geldt ook voor deze bronnen).

Voor dit type wordt de markdown-body in `resources/raw/handcrafted/<naam>.md`
opgeslagen (git-tracked, ANDERS dan andere raw-mappen die gitignored zijn).
De pipeline leest dat raw bestand, de transformer-chain bouwt frontmatter +
chunk-config, en de output landt in `resources/bronnen/<rol>/<naam>.md`.

Voordeel boven `handcrafted`: de output-MD is reproduceerbaar, kan een
trust-cyclus doorlopen, en raakt niet "los van" de pipeline.

Configuratie in source_config.yaml:

    SourceName:
      bron_rol: interpretatief
      raw: resources/raw/handcrafted/SourceName.md
      output: resources/bronnen/normen/SourceName.md
      extract:
        method: md_passthrough
"""
from __future__ import annotations

from pathlib import Path


def extract(cfg: dict, source_name: str) -> str:
    """Lees raw markdown-body en geef hem terug zoals hij is.

    Args:
        cfg: source-config voor deze bron (moet `raw`-veld bevatten).
        source_name: bron-naam (voor foutmeldingen).

    Returns:
        De body als markdown-string. De pipeline voegt frontmatter toe.
    """
    raw = cfg.get("raw")
    if not raw:
        raise ValueError(f"{source_name}: md_passthrough vereist een 'raw'-veld in cfg")

    # Resolve t.o.v. repo-root (twee niveaus boven tools/lib/extractors/)
    root = Path(__file__).resolve().parents[3]
    raw_path = root / raw
    if not raw_path.exists():
        raise FileNotFoundError(
            f"{source_name}: raw-bestand niet gevonden: {raw_path}"
        )

    text = raw_path.read_text(encoding="utf-8")

    # Als de raw zelf YAML-frontmatter bevat, strip die zodat de orchestrator
    # de frontmatter consistent kan genereren via transform-chain.
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end > 0:
            text = text[end + 4:].lstrip("\n")

    return text
