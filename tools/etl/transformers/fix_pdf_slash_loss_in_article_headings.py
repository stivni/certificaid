r"""Transformer: fix PDF-render slash-loss in artikel-headings.

Sommige PDFs (notable: WBTW-KB4) renderen `Art. 8/1` als `Artikel 81` —
de forward slash gaat verloren tussen 8 en 1 door font-rendering. Het
gevolg: heading-injectie produceert `## Art. 81` terwijl de body in
amendment-annotaties expliciet refereert naar `artikel 8/1`.

Detectie-heuristiek:
1. Vind heading `## Art. NM` waar M is 1-9.
2. Kijk naar de eerstvolgende 20 regels body. Als die expliciet
   verwijzen naar `artikel N/M` (met slash), is de heading verkeerd.
3. Rewrite heading naar `## Art. N/M`.

Conservatief: alleen wanneer de slash-versie expliciet in de body staat.
Toepassen na inject_headings_wettekst.

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

# Match heading van vorm "## Art. NM" waar N en M cijfers zijn (≤2 digits voor N).
# 'N' = de hoofd-artikelnummer (1-2 digits); 'M' = sub-nummer (1 digit).
# We zijn restrictief: alleen 2- of 3-cijferige artikel-nummers.
_HEADING_RE = re.compile(
    r"^(?P<prefix>#{1,6}\s+Art\.\s+)(?P<num>\d{2,3})\s*$",
    re.M,
)


def fix_pdf_slash_loss_in_article_headings(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Rewrite '## Art. NM' → '## Art. N/M' waar body 'artikel N/M' bevat."""
    matches = list(_HEADING_RE.finditer(body))
    if not matches:
        return body, frontmatter

    new_body = body
    # Verwerk van achteren naar voren (anders schuiven indices).
    for m in reversed(matches):
        num_str = m.group("num")
        # Probeer alle splits: NM → N/M (single-digit M)
        if len(num_str) == 2:
            n, mm = num_str[0], num_str[1]
        elif len(num_str) == 3:
            n, mm = num_str[:2], num_str[2]
        else:
            continue
        # Verifieer dat body refereert naar `artikel N/M` (binnen 30 regels na heading)
        heading_end = m.end()
        # Pak max 2000 chars na de heading
        scope = new_body[heading_end:heading_end + 3000]
        slash_ref = re.compile(rf"\bartikel\s+{re.escape(n)}/{re.escape(mm)}\b", re.I)
        if not slash_ref.search(scope):
            continue
        # Rewrite heading
        replacement = f"{m.group('prefix')}{n}/{mm}"
        new_body = new_body[:m.start()] + replacement + new_body[m.end():]
    return new_body, frontmatter
