r"""Transformer: fix pdftotext line-wrap-glue bugs (word-concat + ligaturen).

Twee categorieën van bugs die pdftotext oplevert:

1. **Ligaturen niet ontbonden**: pdftotext laat soms `ﬁ` (U+FB01) of `ﬂ`
   (U+FB02) staan i.p.v. ze om te zetten naar `fi`/`fl`. Voorbeelden:
   `geïdentiﬁceerd` → `geïdentificeerd`, `BTW-identiﬁcatienummer` →
   `BTW-identificatienummer`.

2. **Hyphen+newline collapsed naar concat**: pdftotext laat soms een
   afgebroken woord (woord eindigt met `-` aan einde regel, volgt woord
   op volgende regel) samenvoegen tot één string zonder hyphen of spatie.
   Voorbeelden:
     - `BTWidentificatienummer` (was `BTW-` + `identificatienummer`)
     - `BTWdoeleinden` (was `BTW-` + `doeleinden`)
     - `douaneentrepot` (was `douane-` + `entrepot`)
     - `inartikel` (was `in` + `artikel`)

Hier passen we een whitelist toe van veelvoorkomende concat-bugs uit het
Belgische wetteksten-corpus (WBTW-KB31, KB48, KB55, etc.). Conservatief —
alleen exacte string-matches, geen generieke heuristiek.

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

# Ligatuur-replacements (Unicode private-use → ASCII equivalents).
_LIGATURE_MAP = {
    "ﬀ": "ff",
    "ﬁ": "fi",
    "ﬂ": "fl",
    "ﬃ": "ffi",
    "ﬄ": "ffl",
    "ﬅ": "st",  # archaic, but pdftotext kan dit produceren
    "ﬆ": "st",
}

# Whitelist concat-fixes voor BTW-/douane-context. Geordend per voorkomen
# in WBTW-corpus (alleen toegepast als exacte match — geen generieke regel).
# Patroon-paar: (re.compile, replacement).
_CONCAT_FIXES: list[tuple[re.Pattern[str], str]] = [
    # BTW-prefix concats
    (re.compile(r"\bBTWidentificatienummer\b"), "BTW-identificatienummer"),
    (re.compile(r"\bBTWidentiﬁcatienummer\b"), "BTW-identificatienummer"),
    (re.compile(r"\bBTWdoeleinden\b"), "BTW-doeleinden"),
    (re.compile(r"\bBTWkantoor\b"), "BTW-kantoor"),
    (re.compile(r"\bBTWeenheid\b"), "BTW-eenheid"),
    (re.compile(r"\bBTWaangifte\b"), "BTW-aangifte"),
    (re.compile(r"\bBTWplichtige\b"), "BTW-plichtige"),
    # Lowercase btw-prefix concats (komt voor in KB7)
    (re.compile(r"\bbtwidentificatienummer\b"), "btw-identificatienummer"),
    (re.compile(r"\bbtwdoeleinden\b"), "btw-doeleinden"),
    (re.compile(r"\bbtwkantoor\b"), "btw-kantoor"),
    (re.compile(r"\bbtwtarief\b"), "btw-tarief"),
    (re.compile(r"\bbtweenheid\b"), "btw-eenheid"),
    (re.compile(r"\bBTWeenheid\b"), "BTW-eenheid"),
    (re.compile(r"\bbtwaangifte\b"), "btw-aangifte"),
    (re.compile(r"\bbtwaangiften\b"), "btw-aangiften"),
    (re.compile(r"\bbtwopgave\b"), "btw-opgave"),
    (re.compile(r"\bBTWopgave\b"), "BTW-opgave"),
    (re.compile(r"\bBTWkantoor\b"), "BTW-kantoor"),
    (re.compile(r"\bbtwentrepot\b"), "btw-entrepot"),
    (re.compile(r"\bbtwkasticket\b"), "btw-kasticket"),
    (re.compile(r"\bbtwkastickets\b"), "btw-kastickets"),
    # het + Wetboek/Wet (komt voor in KB48)
    (re.compile(r"\bhetWetboek\b"), "het Wetboek"),
    (re.compile(r"\bhetWetboek\.", flags=0), "het Wetboek."),
    (re.compile(r"\bvanhet\b"), "van het"),
    (re.compile(r"\binhet\b"), "in het"),
    # douane-prefix concats
    (re.compile(r"\bdouaneentrepot\b"), "douane-entrepot"),
    (re.compile(r"\bdouaneagent\b"), "douane-agent"),
    (re.compile(r"\bdouaneadministratie\b"), "douane-administratie"),
    # in + artikel/paragraaf (algemene 'in'+word concats die in KB31 voorkomen)
    (re.compile(r"\binartikel\b"), "in artikel"),
    (re.compile(r"\binparagraaf\b"), "in paragraaf"),
    # § + N (ruimte ontbreekt) — komt voor in KB55 ("§ 1en § 2")
    (re.compile(r"§ (\d+)en\b"), r"§ \1 en"),
]


def fix_pdftotext_glue_bugs(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Normaliseer ligaturen + whitelist-concat-fixes."""
    new_body = body
    # 1) Ligaturen
    for char, repl in _LIGATURE_MAP.items():
        if char in new_body:
            new_body = new_body.replace(char, repl)
    # 2) Whitelist concat-fixes
    for pat, repl in _CONCAT_FIXES:
        new_body = pat.sub(repl, new_body)
    return new_body, frontmatter
