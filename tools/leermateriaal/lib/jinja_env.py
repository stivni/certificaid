"""
Jinja2 Environment setup voor leermateriaal-templates (ADR-010).

Laadt templates vanuit tools/leermateriaal/templates/ met strict undefined-mode
zodat ontbrekende variabelen vroeg falen. Registreert confidence_label, slugify,
regex_replace, regex_search en truncate_cell als Jinja2-filters.
"""

from __future__ import annotations

import re
from pathlib import Path

from jinja2 import ChainableUndefined, Environment, FileSystemLoader

from tools.leermateriaal.lib.confidence import label as confidence_label_fn
from tools.leermateriaal.lib.wikilinks import slugify as slugify_fn

_TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"

_env: Environment | None = None


def _regex_replace(waarde: str, patroon: str, vervanging: str = "") -> str:
    """Vervang regex-matches in een string."""
    return re.sub(patroon, vervanging, str(waarde))


def _regex_search(waarde: str, patroon: str) -> str:
    """Geef eerste regex-match terug, of lege string als geen match."""
    treffer = re.search(patroon, str(waarde))
    return treffer.group(0) if treffer else ""


def _truncate_cel(waarde: str, lengte: int = 120, suffix: str = "…") -> str:
    """Kap een string af op `lengte` tekens voor gebruik in tabelcellen."""
    tekst = str(waarde)
    if len(tekst) <= lengte:
        return tekst
    return tekst[:lengte].rstrip() + suffix


# Afkortingen waarbij de punt GEEN zinsbeëindiging is.
# Belgisch-juridische context: "art.", "§", "lid", "jo.", "nl.", maar ook
# bv./vs./nr./e.g./i.e. en hoofdletters-afkortingen van wetboeken.
_AFKORTING_VOOR_PUNT = {
    "art", "bv", "nl", "vs", "nr", "ca", "blz", "p", "pp",
    "jo", "j", "i.e", "e.g", "etc", "incl", "excl",
    "wvv", "kb", "cbn", "btw", "av", "rv", "rr", "ev", "lid",
}


def _is_afkorting(woord: str) -> bool:
    """Check of een woord (zonder trailing dot) een bekende niet-zin-eindigende afkorting is."""
    return woord.lower().lstrip("(") in _AFKORTING_VOOR_PUNT


def _eerste_zin(waarde: str, max_lengte: int = 120) -> str:
    """Extraheer eerste zin uit een tekst — duizendtal- en afkorting-veilig.

    Splits op zinsbeëindiging (`. ` met spatie, gevolgd door hoofdletter of einde)
    zodat bedragen als `€ 1.600.000` en wetsverwijzingen `WVV art. 1:26` niet
    midden in het bedrag/wetsartikel worden gecapt.

    Args:
        waarde: input-string
        max_lengte: harde lengte-cap (default 120)

    Returns:
        Eerste zin (zonder afsluitende punt) of de hele string als korter dan max_lengte.
    """
    tekst = str(waarde).strip()
    if not tekst:
        return ""

    # Zoek kandidaat-zin-eindes: `. ` of `! ` of `? ` of einde-string
    # Loop tot we een echte zin-einde vinden (geen afkorting ervoor)
    pos = 0
    while pos < len(tekst):
        treffer = re.search(r"[.!?](\s|$)", tekst[pos:])
        if not treffer:
            kandidaat = tekst
            break
        eind = pos + treffer.start()
        # Welk woord staat vóór de punt?
        woord_match = re.search(r"(\S+)$", tekst[:eind])
        woord = woord_match.group(1) if woord_match else ""
        # Echte zin-einde als woord geen afkorting is EN volgende karakter
        # is einde-string, hoofdletter, of leeg
        rest = tekst[eind + 1:].lstrip()
        volgende_is_hoofdletter = bool(rest) and rest[0].isupper()
        if not _is_afkorting(woord) and (not rest or volgende_is_hoofdletter):
            kandidaat = tekst[:eind].rstrip(" \t")
            break
        # Niet echt einde — kijk verder voorbij deze punt
        pos = eind + 1
    else:
        kandidaat = tekst

    if len(kandidaat) > max_lengte:
        kandidaat = kandidaat[:max_lengte].rstrip() + "…"
    return kandidaat


def get_env() -> Environment:
    """Haal de geconfigureerde Jinja2 Environment op (singleton).

    Filters beschikbaar in templates:
    - ``confidence_label``: confidence-string → emoji ('grounded' → '⚖️', anders '🤖')
    - ``slugify``: tekst → URL-slug
    - ``regex_replace``: regex-substitutie
    - ``regex_search``: geeft eerste match terug
    - ``truncate_cel``: kap af op N tekens (default 120) voor tabelcellen
    - ``eerste_zin``: extraheer eerste zin (duizendtal-veilig, max-lengte 120)

    Returns:
        geconfigureerde Jinja2 Environment
    """
    global _env
    if _env is None:
        _env = Environment(
            loader=FileSystemLoader(str(_TEMPLATES_DIR)),
            undefined=ChainableUndefined,
            keep_trailing_newline=True,
            trim_blocks=True,
            lstrip_blocks=True,
        )
        _env.filters["confidence_label"] = confidence_label_fn
        _env.filters["slugify"] = slugify_fn
        _env.filters["regex_replace"] = _regex_replace
        _env.filters["regex_search"] = _regex_search
        _env.filters["truncate_cel"] = _truncate_cel
        _env.filters["eerste_zin"] = _eerste_zin
    return _env
