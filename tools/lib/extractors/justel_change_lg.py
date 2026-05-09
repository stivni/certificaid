"""Extractor voor `justel_change_lg` — oudere Justel ``change_lg.pl`` HTML.

De moderne Justel-pagina gebruikt een gestructureerde DOM met
``div#list-title-3`` en wordt afgehandeld door :mod:`justel_html`. Voor oudere
documenten levert ejustice nog steeds een legacy-pagina (URL-pad
``/cgi_loi/change_lg.pl``) waarin de wettekst in één lange ``<BR>``-gescheiden
regel staat met ``<A NAME='LNK000N'>``-ankers voor hoofdstukken en
``<A NAME='Art.N'></A>Artikel <A HREF='#Art.N+1'> N</A>`` voor artikelen.

Deze handler parseert dat formaat naar plain-tekst regels die door
``tools.lib.headings.process_wettekst`` herkend worden:

    HOOFDSTUK I. - Algemene bepalingen.

    Art. 1. Voor de toepassing van dit besluit ...

Cleanup (NBSP→spatie, blank-line-collapse) en frontmatter worden door de
orchestrator gedaan; de extractor levert alleen de markdown-body terug.
"""
from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


# ── HTML → tekst helpers ─────────────────────────────────────────────────────

# Body begint bij ``<h2 id="text"`` (de "Tekst"-sectie).
_BODY_START_RE = re.compile(
    r"<h2[^>]*\bid=['\"]text['\"][^>]*>.*?</h2>",
    re.IGNORECASE | re.DOTALL,
)

# Body eindigt op het volgende ``<div id="list-title-…"`` of de ``<div class="links``
# (Aanhef / Links / footer). Het eerste van die markers knipt de body af.
_BODY_END_PATTERNS = (
    re.compile(r"<div[^>]*\bid=['\"]list-title-sw_prev['\"]", re.IGNORECASE),
    re.compile(r"<div[^>]*\bid=['\"]list-title-sw['\"]", re.IGNORECASE),
    re.compile(r"<div[^>]*\bclass=['\"][^'\"]*\blinks\b", re.IGNORECASE),
    re.compile(r"</main>", re.IGNORECASE),
)

# HOOFDSTUK / TITEL / DEEL / BOEK / AFDELING etc. via een ``LNK``-anker.
# Voorbeeld: <A NAME='LNK0003' HREF='#LNKR0003'>HOOFDSTUK III.</A>
_LNK_ANCHOR_RE = re.compile(
    r"<A\s+NAME=['\"]LNK\d+['\"][^>]*>(?P<label>[^<]+)</A>",
    re.IGNORECASE,
)

# Artikel-heading. Twee varianten:
#   1) Eerste artikel:  <A NAME='Art.1'></A>Artikel <A HREF='#Art.2'> 1</A>.
#   2) Volgende:        <A NAME='Art.5' HREF='#Art.4'>Art.</A> <A HREF='#Art.6'> 5</A>.
# We normaliseren beide naar ``Art. <nr>.``
_ART_FIRST_RE = re.compile(
    r"<A\s+NAME=['\"]Art\.(?P<num1>[^'\"]+)['\"][^>]*></A>\s*Artikel\s*"
    r"<A[^>]*>\s*(?P<num2>[^<]+?)\s*</A>\s*\.?",
    re.IGNORECASE,
)
_ART_NEXT_RE = re.compile(
    r"<A\s+NAME=['\"]Art\.(?P<num1>[^'\"]+)['\"][^>]*>\s*Art\.\s*</A>\s*"
    r"<A[^>]*>\s*(?P<num2>[^<]+?)\s*</A>\s*\.?",
    re.IGNORECASE,
)

# Overgebleven losse ``<A …>tekst</A>`` (bv. interne kruisverwijzingen) →
# vervang door de tekst-content.
_GENERIC_ANCHOR_RE = re.compile(
    r"<A\b[^>]*>(?P<txt>[^<]*)</A>",
    re.IGNORECASE,
)

# Alle resterende HTML-tags (uitgezonderd <BR>, dat hieronder eerst wordt
# omgezet naar newline).
_TAG_RE = re.compile(r"<[^>]+>")


def _extract_body(html_text: str) -> str:
    """Knip de wettekst-body uit de Justel ``change_lg.pl``-pagina.

    Strategie: zoek het begin via ``<h2 id="text">`` en eindig bij het volgende
    div-blok (Aanhef of Links). Geeft de ruwe HTML-fragment-string terug.
    """
    start_match = _BODY_START_RE.search(html_text)
    if not start_match:
        raise ValueError(
            "Geen <h2 id='text'> gevonden — is dit echt een Justel "
            "change_lg.pl-pagina?"
        )
    body_html = html_text[start_match.end():]

    # Knip op het eerste end-pattern.
    end_offsets = [m.start() for p in _BODY_END_PATTERNS
                   for m in [p.search(body_html)] if m]
    if end_offsets:
        body_html = body_html[: min(end_offsets)]

    return body_html


def _normalise_anchors(body_html: str) -> str:
    """Vervang structurele ankers door plain-text equivalenten."""

    # Stap 1: HOOFDSTUK / TITEL / ... — labels staan letterlijk in de anchor-body.
    def _lnk_repl(match: re.Match[str]) -> str:
        label = match.group("label").strip()
        # Forceer linebreak ervoor + erna zodat het label op een eigen regel komt.
        return f"\n\n{label}"

    body_html = _LNK_ANCHOR_RE.sub(_lnk_repl, body_html)

    # Stap 2: artikelen — beide varianten naar ``Art. <nr>.``
    def _art_repl(match: re.Match[str]) -> str:
        num = match.group("num2").strip()
        return f"\n\nArt. {num}."

    body_html = _ART_FIRST_RE.sub(_art_repl, body_html)
    body_html = _ART_NEXT_RE.sub(_art_repl, body_html)

    # Stap 3: overige <A>-tags vervangen door hun tekst-content.
    body_html = _GENERIC_ANCHOR_RE.sub(lambda m: m.group("txt"), body_html)
    return body_html


def _html_to_text(body_html: str) -> str:
    """Converteer het anker-genormaliseerde fragment naar plain text."""
    # <BR> → newline (alle hoofdletter-varianten).
    txt = re.sub(r"<\s*BR\s*/?\s*>", "\n", body_html, flags=re.IGNORECASE)
    # Resterende tags strippen.
    txt = _TAG_RE.sub("", txt)
    # HTML-entities decoderen (bv. ``&nbsp;`` → ``\xa0`` → cleanup zet dat om
    # naar gewone spatie via de standaardpipeline).
    txt = html.unescape(txt)
    return txt


def _tidy_lines(text: str) -> str:
    """Trim trailing whitespace, collapse meerdere blanke regels naar één,
    en vervang non-breaking spaces door gewone spaties.

    De gedeelde cleanup-pipeline (``collapse_blank_lines``) doet de
    blank-line-collapse nogmaals; we draaien het hier om een nette
    extractor-output te leveren waarin debugging eenvoudig is. NBSP-vervanging
    moet in de extractor gebeuren omdat de cleanup-stappen voor ``justel_*``
    methods beperkt zijn tot ``collapse_blank_lines``.
    """
    # NBSP (U+00A0) → gewone spatie. Justel change_lg.pl gebruikt &nbsp;&nbsp;
    # als inspring; wij willen platte ASCII-spaties.
    text = text.replace("\xa0", " ")
    # Meerdere spaties op één regel → één spatie (behoudt geen indent want de
    # heading-injection en chunk-detectie werken op regelinhoud, niet op indent).
    text = re.sub(r"[ \t]{2,}", " ", text)
    lines = [line.rstrip() for line in text.splitlines()]
    # Collapse runs van ≥2 lege regels naar exact één lege regel.
    out: list[str] = []
    blank_run = 0
    for line in lines:
        if line.strip() == "":
            blank_run += 1
            if blank_run <= 1:
                out.append("")
        else:
            blank_run = 0
            out.append(line)
    # Strip leading/trailing blanks.
    while out and out[0] == "":
        out.pop(0)
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n"


# ── Public extract() ─────────────────────────────────────────────────────────

def extract(cfg: dict, source_name: str) -> str:
    """Parse oudere Justel change_lg.pl HTML-pagina naar markdown-body.

    Verwacht ``cfg['raw']`` te wijzen naar het lokaal opgeslagen HTML-bestand.
    Returnt een plain-text body (geen frontmatter); ``HOOFDSTUK X.`` en
    ``Art. N.`` staan op aparte regels zodat ``process_wettekst`` ze als
    structuurlabels en chunk-grenzen oppikt.
    """
    raw_rel = cfg.get("raw")
    if not raw_rel:
        raise ValueError(
            f"`raw` ontbreekt voor {source_name}: lokaal HTML-bestand vereist."
        )
    raw_path = ROOT / raw_rel
    if not raw_path.exists():
        raise FileNotFoundError(f"HTML-bestand niet gevonden: {raw_path}")

    # Justel change_lg.pl stuurt ISO-8859-1 (zie meta charset in de bron).
    html_text = raw_path.read_text(encoding="iso-8859-1")

    body_html = _extract_body(html_text)
    body_html = _normalise_anchors(body_html)
    text = _html_to_text(body_html)
    text = _tidy_lines(text)
    return text
