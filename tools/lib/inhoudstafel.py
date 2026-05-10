"""TOC-strip voor wettekst-PDFs.

Wettekst-PDFs (EU richtlijnen, Belgische wetboeken, KB/MB-compilaties) hebben
typisch een Inhoudstafel/INHOUDSTAFEL aan het begin met dotted-leader-pagina-
referenties. Die TOC dupliceert de body-headings en geeft RAG-ruis: een
retrieval-hit op een TOC-lijn levert geen artikel-content.

Deze module biedt één robuuste TOC-strip die:

  1. Een **expliciete marker** ("Inhoudstafel", "INHOUDSTAFEL") herkent en het
     volledige blok daaronder weghaalt tot de eerste body-regel.
  2. Een **orphan TOC-cluster** detecteert (geen marker, maar wel ≥3 dotted-
     leader-regels in de eerste 60 regels): begint vanaf de eerste TOC-regel.
  3. **Wrap-detection**: TOC-entries kunnen multi-line zijn (eerste regel =
     headertekst, tweede regel = paginanummer met dots). De volgende non-blank
     regel meekijken om "deze heading hoort bij een TOC" te beslissen.
  4. **Body-start-detectie**: stop bij eerste regel die NIET TOC-suffix-achtig
     is en wel een heading is (markdown-`#`, `EERSTE/TWEEDE/... AFDELING`,
     `Artikel N`, `Art. N`) of een lange paragraaf-regel zonder leading-ws.

Wordt gebruikt door:
  * `tools/lib/extractors/pdftotext_compilatie_btw.py` (inline tijdens extract)
  * `tools/lib/cleanup.py:remove_inhoudstafel` (post-extract cleanup-stap voor
    pdftotext_ejustice)

Niet bedoeld om interne TOCs van bijlagen te strippen (die staan ver in de
body en zijn een ander probleem).
"""
from __future__ import annotations

import re

# ─── Patronen ────────────────────────────────────────────────────────────────

_INHOUDSTAFEL_RE = re.compile(r"^[ \t]*(?:Inhoudstafel|INHOUDSTAFEL)\b.*$", re.I)

# Geschreven AFDELING-volgnummers (Belgische compilaties).
_AFDELING_WORDS_RE = re.compile(
    r"^[ \t]+(?:EERSTE|TWEEDE|DERDE|VIERDE|VIJFDE|ZESDE|ZEVENDE|"
    r"ACHTSTE|NEGENDE|TIENDE|ELFDE|TWAALFDE)\s+AFDELING\b"
)

_ART_BIS = (
    r"(?:bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies|"
    r"undecies|duodecies|terdecies|quaterdecies)"
)
_ARTIKEL_PLAIN_RE = re.compile(
    rf"^[ \t]+(?:Art\.|Artikel)\s+\d+(?:{_ART_BIS})?(?:/\d+)?\s*\.?\s*$"
)

# Bare structurele headings (zonder markdown-prefix, zonder TOC-suffix).
# Komen voor in raw ejustice-extracten waar de body "TITEL I" / "Artikel 1"
# als plain text bevat. Verschilt van `_AFDELING_WORDS_RE` (die de Belgische
# compilatie-stijl met leading whitespace dekt).
_BARE_STRUCTURAL_RE = re.compile(
    r"^(?:DEEL|BOEK|TITEL|TITLE|HOOFDSTUK|Hoofdstuk|AFDELING|Afdeling|"
    r"ONDERAFDELING|Onderafdeling)\s+[IVXLCDM\d]",
)
_BARE_ARTIKEL_RE = re.compile(
    rf"^(?:Artikel|Art\.)\s+\d+(?:{_ART_BIS})?(?:/\d+)?\s*\.?\s*$"
)

# TOC-suffix-detectoren: regel ziet er TOC-achtig uit.
_TOC_SUFFIX_PATTERNS = (
    re.compile(r"\(art\.\s+\d+\w*\s*[\-–]\s*art\.\s+\d+\w*\)"),  # (art. 1 - art. 4)
    re.compile(r"\(art\.\s+\d+[^)]{0,40}\)"),                     # (art. N ...)
    re.compile(r"\.{3,}\s*\d+\s*$"),                              # ........ 12
    # Heading + whitespace + paginanummer. Vereist substantiële tekst (≥10
    # niet-witruimte chars) vóór de whitespace zodat we lone-page-number-regels
    # (een digit alleen op een regel met cover-page whitespace) NIET matchen.
    re.compile(r"\S.{10,}\s{3,}\d+\s*$"),
    # EU-OJ-stijl: trailing reeks van "space-dot" (eindeloos `. . . . .`).
    # Vereist ≥3 " ."-sequenties aan het einde; geen paginanummer nodig.
    re.compile(r"(?:\s\.){3,}\s*\.?\s*$"),
    # pdftotext-layout truncates wijde TOC-regels: "TITEL I .........." (4+
    # dots aan einde, paginanummer afgekapt). Body-zinnen eindigen niet op
    # 4+ aaneengesloten dots, dus dit is veilig als TOC-signaal.
    re.compile(r"\.{4,}\s*$"),
)

_HEADING_RE = re.compile(r"^#{1,6}\s+\S")


def _is_toc_line(ln: str) -> bool:
    """Heuristiek: heeft deze regel een TOC-suffix (dotted-leader, paginanummer)?"""
    if not ln.strip():
        return False
    return any(p.search(ln) for p in _TOC_SUFFIX_PATTERNS)


def _toc_continuation(lines: list[str], idx: int) -> bool:
    """Kijk of de eerstvolgende non-blank regel een TOC-suffix heeft.

    Multi-line TOC-entries: eerste regel = title, tweede (of derde) = paginanummer
    met dotted-leaders. Als één van de volgende 3 non-blank regels TOC-suffix
    heeft, is `idx` een wrap-TOC-entry.
    """
    seen = 0
    for k in range(idx + 1, min(idx + 6, len(lines))):
        if not lines[k].strip():
            continue
        seen += 1
        if _is_toc_line(lines[k]):
            return True
        if seen >= 3:
            return False
    return False


def _is_body_marker(ln: str) -> bool:
    """Regel ziet eruit als body-start (heading, AFDELING, Artikel).

    Dekt:
      * markdown-`#`-headings: `### TITEL I`
      * Belgische compilatie-stijl met leading whitespace:
        `        EERSTE AFDELING`, `      Artikel 1`
      * EU-OJ/ejustice plain text zonder leading-ws:
        `TITEL I`, `Artikel 1`, `HOOFDSTUK 2`
    """
    return bool(
        _HEADING_RE.match(ln)
        or _AFDELING_WORDS_RE.match(ln)
        or _ARTIKEL_PLAIN_RE.match(ln)
        or _BARE_STRUCTURAL_RE.match(ln)
        or _BARE_ARTIKEL_RE.match(ln)
    )


# ─── Hoofdfunctie ────────────────────────────────────────────────────────────

def strip_inhoudstafel(body: str, *, search_window: int = 60) -> str:
    """Verwijder Inhoudstafel-blok aan begin van body.

    Args:
      body: tekst (zonder frontmatter).
      search_window: aantal regels waarbinnen we naar TOC-cluster zoeken
        wanneer geen expliciete "Inhoudstafel"-marker aanwezig is.

    Returns:
      Body zonder TOC-blok. Als geen TOC gevonden: body ongewijzigd.

    Detectie-logica:
      1. Zoek "Inhoudstafel"/"INHOUDSTAFEL"-regel. Indien gevonden: TOC begint
         daar.
      2. Anders: cluster-heuristiek. ≥3 TOC-suffix-regels in de eerste
         `search_window` regels → TOC begint bij de eerste TOC-regel.
      3. Body-start = eerste niet-TOC niet-blank heading of paragraaf-regel.
    """
    lines = body.splitlines()

    # Stap 1: vind TOC-start.
    toc_start = None
    for i, ln in enumerate(lines):
        if _INHOUDSTAFEL_RE.match(ln):
            toc_start = i
            break
    if toc_start is None:
        hits = [i for i, ln in enumerate(lines[:search_window]) if _is_toc_line(ln)]
        if len(hits) < 3:
            return body
        toc_start = hits[0]

    # Stap 2: vind body-start.
    body_start = None
    for j in range(toc_start + 1, len(lines)):
        ln = lines[j]
        if not ln.strip():
            continue
        if _is_toc_line(ln) or _toc_continuation(lines, j):
            continue
        if _is_body_marker(ln):
            body_start = j
            break
        # Lange paragraaf-regel zonder leading whitespace → body.
        if not ln.startswith((" ", "\t")) and len(ln.strip()) >= 40:
            body_start = j
            break

    if body_start is None:
        return body

    return "\n".join(lines[:toc_start] + lines[body_start:])
