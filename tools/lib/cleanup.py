"""
Gedeelde cleanup-functies voor wettekst-conversie.

Alle functies zijn puur structureel: ze veranderen nooit de wettelijke tekst,
alleen de opmaak, de taal-selectie en de metadataruis.

Verbatim-garantie: na elke functie is de NL-tekst identiek aan de bron.
"""

import re


# ---------------------------------------------------------------------------
# 1. Tweetaligheid — Frans verwijderen
# ---------------------------------------------------------------------------

def strip_french_columns(text: str, nl_col_x: int, page_width: int = 595) -> str:
    """
    Voor pdftotext -layout output: verwijder de kolom rechts van nl_col_x.
    Gebruikt door de bilingual-converter vóór cleanup.
    (Dit is al ingebakken in convert-wetboek.py bilingual mode —
    hier als utility voor nieuwe conversies.)
    """
    # Niet van toepassing op al-geconverteerde tekst; zie extract_nl_column in convert-wetboek.py
    return text


# Herkenbare Franse patronen in "NL-only" teksten die toch FR-fragmenten bevatten
_FRENCH_MARKERS = [
    # Typische FR juridische zinsstarters
    r"^\s*(?:Art\.|Chapitre|Section|Titre|Livre|Partie)\s+\d+[a-z]?\s*\.\s*[A-Z][a-zé]",
    # Expliciete FR-taalmarkering
    r"<FR>.*?</FR>",
    r"\[FR\].*?\[/FR\]",
    # Lange blokken met typisch FR vocabulaire (minimaal 3 FR woorden op een rij)
    r"\b(au|aux|de|du|des|le|la|les|est|sont|pour|dans|par|sur|une|avec|qui|que|ou|et)\b"
    r".{0,20}"
    r"\b(au|aux|de|du|des|le|la|les|est|sont|pour|dans|par|sur|une|avec|qui|que|ou|et)\b"
    r".{0,20}"
    r"\b(au|aux|de|du|des|le|la|les|est|sont|pour|dans|par|sur|une|avec|qui|que|ou|et)\b",
]


def remove_french_lines(text: str) -> str:
    """
    Verwijder regels die overwegend Frans zijn.
    Conservatief: enkel regels die duidelijk FR zijn (niet NL-tekst met FR leenwoorden).
    """
    nl_words = set("van de het een en in op is zijn worden voor met bij als tot".split())
    fr_words = set("du des les aux une est sont par sur dans pour avec qui que ou".split())

    result_lines = []
    for line in text.split("\n"):
        words = re.findall(r"\b[a-zA-Zéèêàùûîôëïü]+\b", line.lower())
        if not words:
            result_lines.append(line)
            continue
        nl_count = sum(1 for w in words if w in nl_words)
        fr_count = sum(1 for w in words if w in fr_words)
        # Enkel verwijderen als FR duidelijk domineert én geen NL-signal
        if fr_count >= 3 and fr_count > nl_count * 2 and len(words) >= 4:
            continue
        result_lines.append(line)
    return "\n".join(result_lines)


def remove_french_blocks(text: str) -> str:
    """
    Verwijder aaneengesloten blokken van meerdere Franse regels.
    Gebruikt voor ejustice-documenten met alternerende NL/FR paragrafen.
    """
    lines = text.split("\n")
    result = []
    fr_buffer = []
    nl_words = set("van de het een en in op is zijn worden voor met bij als tot aan geen".split())
    fr_words = set("du des les aux une est sont par sur dans pour avec qui que ou ce cette".split())

    def is_french_line(line: str) -> bool:
        words = re.findall(r"\b[a-zA-Zéèêàùûîôëïü]+\b", line.lower())
        if len(words) < 3:
            return False
        nl = sum(1 for w in words if w in nl_words)
        fr = sum(1 for w in words if w in fr_words)
        return fr >= 2 and fr > nl

    for line in lines:
        if is_french_line(line):
            fr_buffer.append(line)
        else:
            # Flush FR buffer enkel als het meer dan 1 regel bevat
            if len(fr_buffer) > 1:
                pass  # verwijder het hele FR-blok
            elif fr_buffer:
                result.extend(fr_buffer)  # twijfelgeval: behoud
            fr_buffer = []
            result.append(line)

    return "\n".join(result)


# ---------------------------------------------------------------------------
# 2. Inhoudsopgave verwijderen
# ---------------------------------------------------------------------------

def remove_toc(text: str) -> str:
    """
    Verwijder de inhoudsopgave bovenaan een wettekst.
    Herkent TOC aan:
    - Regels die eindigen op puntjes + paginanummer: "Hoofdstuk I .............. 12"
    - Regels met "Inhoudstafel" of "Table des matières"
    - Regels van de stijl "Art. 1-5 ...... 3"
    Stopt bij de eerste echte artikeltekst.
    """
    lines = text.split("\n")
    toc_end_idx = 0
    in_toc = False

    toc_markers = re.compile(
        r"(inhoudstafel|inhoudsopgave|table\s+des\s+mati.res|"
        r"\.{4,}\s*\d+\s*$|"          # puntjes + paginanummer
        r"^\s*art\.\s+\d+[-–]\d+\s*\.{2,}|"  # Art. 1-5 ....
        r"^\s*\d+\s*$)",               # alleen een paginanummer
        re.IGNORECASE,
    )

    first_art_marker = re.compile(
        r"^#{1,4}\s+Art\."          # markdown heading
        r"|^\*\*Art\.\s+\d"         # bold art
        r"|^§\s*\d"                 # paragraaf
        r"|^TITEL\s+I\.\s*[-–]"     # structuurkop
        # ejustice inline art. met inhoud — dekt "Art. 47.", "Art. I.20.", "Art. IV.85."
        r"|^\s{0,4}Art\.\s+(?:[IVX]+\.)?[\d][\w./:]*\.\s+\S.{10,}",
        re.IGNORECASE,
    )

    for i, line in enumerate(lines):
        if toc_markers.search(line):
            in_toc = True
            toc_end_idx = i
        elif in_toc and first_art_marker.search(line):
            # Eerste echte artikel gevonden — TOC eindigt hier
            toc_end_idx = i
            break

    if in_toc and toc_end_idx > 0:
        return "\n".join(lines[toc_end_idx:])
    return text


# ---------------------------------------------------------------------------
# 3. Paginanummers en running headers/footers
# ---------------------------------------------------------------------------

_PAGE_NUMBER_RE = re.compile(r"^\s*\d{1,4}\s*$")
_URL_FRAGMENT_RE = re.compile(r"^\s*(net|fisconet|www\.|ejustice|belgisch\s+staatsblad)", re.I)
_DECORATION_RE = re.compile(r"^\s*[—–]{3,}\s*$")  # enkel em/en-dashes, NIET --- (YAML)
_FORM_FEED_RE = re.compile(r"\x0c")
# "Pagina 7 van 76 Copyright Belgisch S taatsblad 17-01-2026" — ejustice PDF running footer
# "S taatsblad" (met spatie) is een OCR-artefact dat ook voorkomt als "Staatsblad"
_STAATSBLAD_FOOTER_RE = re.compile(
    r"^\s*Pagina\s+\d+\s+van\s+\d+\s+Copyright\s+Belgisch\s+S?\s*taatsblad\b",
    re.IGNORECASE,
)


def remove_page_artifacts(text: str) -> str:
    """
    Verwijder paginanummers, URL-fragmenten, decoratieve lijnen en form feeds.
    Gebaseerd op bewezen logica uit convert-wib92.py.
    """
    text = _FORM_FEED_RE.sub("", text)
    lines = []
    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped:
            lines.append("")
            continue
        if _PAGE_NUMBER_RE.match(stripped):
            continue
        if _URL_FRAGMENT_RE.match(stripped):
            continue
        if _DECORATION_RE.match(stripped):
            continue
        if _STAATSBLAD_FOOTER_RE.match(line):
            continue
        lines.append(line)
    return "\n".join(lines)


def remove_inline_metadata(text: str) -> str:
    """
    Verwijder metadataruis die in de artikeltekst terechtgekomen is:
    - Publicatiedatums alléén op een regel
    - Staatsblad-referenties
    - Gewijzigd bij / Opgeheven bij / Ingevoegd bij referenties die losstaan
    """
    patterns = [
        # Staatsblad-referentie als losse regel
        re.compile(r"^\s*B\.?\s*S\.?\s*\d{1,2}[-./]\d{1,2}[-./]\d{2,4}\s*$", re.I),
        # Gewijzigd/ingevoegd/opgeheven referenties zonder juridische inhoud
        re.compile(r"^\s*<(Gewijzigd|Ingevoegd|Opgeheven|Vervangen|Aangevuld)\s+bij\s+[A-Z]", re.I),
        # Datum-only regels (bv. "01-01-2020")
        re.compile(r"^\s*\d{1,2}[-./]\d{1,2}[-./]\d{4}\s*$"),
    ]
    lines = []
    for line in text.split("\n"):
        if any(p.match(line) for p in patterns):
            continue
        lines.append(line)
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 4. Woordafbreking en witruimte
# ---------------------------------------------------------------------------

_HYPHEN_SOFT = re.compile(r"(\w)-\n\s*([a-z])")  # vervolg in kleine letter → soft hyphen, weghalen
_HYPHEN_HARD = re.compile(r"(\w)-\n\s*([A-Z])")  # vervolg in hoofdletter → echt koppelteken, behouden


def fix_broken_words(text: str) -> str:
    """
    Herstel afgebroken woorden aan het einde van regels.
    Onderscheidt soft hyphens (PDF-regelafbreking) van echte koppeltekens
    in samengestelde eigennamen (Lid-Staten, Noord-Ierland).

    'vennoot-\\n   schapsbelasting' → 'vennootschapsbelasting'  (soft, kleine letter)
    'Lid-\\n   Staten'              → 'Lid-Staten'              (echt, hoofdletter)
    """
    text = _HYPHEN_SOFT.sub(r"\1\2", text)
    text = _HYPHEN_HARD.sub(r"\1-\2", text)
    return text


# Markers waarmee een regel altijd los blijft staan in merge_wrapped_lines.
# Dit zijn structurele begin-tokens van een nieuwe paragraaf, lijst-item, heading, …
_NEW_LINE_STARTS = re.compile(
    r"^(?:"
    r"#{1,6}\s"                  # markdown heading
    r"|§\s*\d"                   # § N
    r"|\d+°"                     # 1°
    r"|\d+/\d+°"                 # 1/1°
    r"|\d+\.(?:\s|$)"            # 1. (of 'i.' alleen op regel)
    r"|[a-z]\)(?:\s|$)"          # a) of a) alleen op regel
    r"|[IVXLCivxlc]+\)(?:\s|$)"  # I) of i) — Romeins (hoofd- of kleine letter)
    r"|\(\d+\)(?:\s|$)"          # (1) voetnoot
    r"|HOOFDSTUK\b|TITEL\b|BOEK\b|Hoofdstuk\b|Boek\b"
    r"|Afdeling\b|Onderafdeling\b|Onderafd\.|Eerste\s"
    r"|Art\.\s|Artikel\s"
    r"|\*"                       # markdown italic / lijst-bullet
    r"|_{3,}|-{3,}"              # separator
    r")"
)
_SENTENCE_END = re.compile(r"[.;!?]\s*$")
_WRAP_THRESHOLD = 70  # PDF-kolombreedte ligt rond 80–95; korte regels zijn doorgaans labels


def merge_wrapped_lines(text: str) -> str:
    """
    Voeg PDF-soft-wraps binnen één paragraaf samen tot één regel.

    pdftotext -layout breekt af op de PDF-kolombreedte. Een vervolgregel wordt
    aan de vorige geplakt wanneer:
      - de vorige regel lang was (>= drempel) én niet eindigt op zinsterminator
        (. ; ? !), of
      - de huidige regel begint met een kleine letter (sterk continuatie-signaal).
    Regels die met een structureel marker beginnen (§, 1°, ##, HOOFDSTUK, …)
    blijven altijd losstaan.

    Werkt zowel op gestripte als op ingesprongen regels.
    """
    out = []
    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped or not out or not out[-1].strip():
            out.append(line)
            continue
        if _NEW_LINE_STARTS.match(stripped):
            out.append(line)
            continue
        prev_stripped = out[-1].strip()
        likely_wrap = (
            len(prev_stripped) >= _WRAP_THRESHOLD
            and not _SENTENCE_END.search(prev_stripped)
        )
        starts_lower = stripped[0].islower()
        if likely_wrap or starts_lower:
            out[-1] = out[-1].rstrip() + " " + stripped
        else:
            out.append(line)
    return "\n".join(out)


def normalize_whitespace(text: str) -> str:
    """
    Normaliseer meerdere spaties tot één (artefact van kolom-extractie).
    Behoudt maximaal 4 spaties inspring.
    """
    lines = []
    for line in text.split("\n"):
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        normalized = re.sub(r"  +", " ", stripped)
        lines.append(" " * min(indent, 4) + normalized)
    return "\n".join(lines)


def collapse_blank_lines(text: str, max_blank: int = 2) -> str:
    """Maximaal max_blank opeenvolgende lege regels."""
    result = re.sub(r"\n{%d,}" % (max_blank + 1), "\n" * max_blank, text)
    return result


# ---------------------------------------------------------------------------
# 5. Standaard markdown-structuur
# ---------------------------------------------------------------------------

def ensure_article_headings(text: str) -> str:
    """
    Zorg dat artikel-markeringen als ## headings geformatteerd zijn.

    Ondersteunt vier formats:
    1. Standalone Art.: `Art. 47` → `## Art. 47`
    2. Standalone Artikel: `Artikel 47` (EU/WABB gecentreerd) → `## Art. 47`
    3. ejustice inline: `  Art. 47. § 1. tekst...` → `## Art. 47\n\n§ 1. tekst...`
    4. MIGB inline: `Art. 47. tekst...` (geen inspringing) → `## Art. 47\n\ntekst...`
    """
    lines = text.split("\n")
    result = []

    # Nummer-patroon voor ensure_article_headings: dekt "47", "6:18", "I.20/1", "IV.85"
    _num = r"(?:[IVXivx]+\.)?[\d][\w./:bis]*"

    # Patroon 1 & 2: standalone — enkel artikelnummer op de regel (ook "Artikel X")
    standalone = re.compile(
        rf"^\s*(Art(?:ikel|\.)\s+{_num})\s*$", re.IGNORECASE
    )
    # Patroon 3: ejustice inline met inspringing (ook WER: "  Art. IV.85. tekst")
    # \s* i.p.v. \s+ na de punt — dekt "Art. 4.Voor" (geen spatie na punt)
    inline_indented = re.compile(
        rf"^\s{{1,4}}(Art\.)\s+({_num})\.\s*(.*\S)", re.IGNORECASE
    )
    # Patroon 4: inline zonder inspringing — MIGB/WVV-stijl
    inline_noindent = re.compile(
        rf"^(Art\.)\s+({_num})\.\s*(\S.*)", re.IGNORECASE
    )
    # Patroon 5: EU-richtlijn "Artikel X" inline met tekst
    artikel_inline = re.compile(
        r"^\s{0,8}(Artikel)\s+(\d[\w./:bis]*)\s*$", re.IGNORECASE
    )

    for line in lines:
        m_standalone = standalone.match(line)
        m_indented   = inline_indented.match(line)
        m_noindent   = inline_noindent.match(line)
        m_artikel    = artikel_inline.match(line)

        if m_standalone:
            # Normaliseer "Artikel X" → "Art. X"
            label = m_standalone.group(1).strip()
            label = re.sub(r"^[Aa]rtikel\s+", "Art. ", label)
            result.append(f"## {label}")
        elif m_artikel:
            result.append(f"## Art. {m_artikel.group(2)}")
        elif m_indented:
            art_num = m_indented.group(2).rstrip(".")
            body = m_indented.group(3).strip()
            result.append(f"## Art. {art_num}")
            result.append("")
            result.append(body)
        elif m_noindent:
            art_num = m_noindent.group(2).rstrip(".")
            body = m_noindent.group(3).strip()
            result.append(f"## Art. {art_num}")
            result.append("")
            result.append(body)
        else:
            result.append(line)

    return "\n".join(result)


def remove_toc_ejustice(text: str) -> str:
    """
    Verwijder de ejustice inhoudsopgave.

    TOC-entries: 'Art. X-Y' of 'Art. X:Y-Z' (bereiken, geen punt na nummer + inhoud)
    Echte artikels: 'Art. X.' of 'Art. X:Y.' gevolgd door substantiële tekst (>20 chars)
    """
    lines = text.split("\n")

    # Nummer-patroon: dekt "47", "6:18", "I.20/1", "IV.85", "III.82"
    _art_num = r"(?:[IVX]+\.)?[\d][\w./:]*"

    # Echte artikel: Art. + nummer + punt + substantiële tekst (>15 chars)
    first_real_art = re.compile(
        rf"^\s{{0,4}}Art\.\s+{_art_num}\.\s{{1,3}}\S.{{15,}}"
    )
    # TOC-range: meerdere artikels op één lijn (komma of koppelstreep)
    art_range = re.compile(
        rf"^\s*Art\.\s+{_art_num}(?:[-–,/]\s*(?:[IVX]+\.)?[\d])"
    )

    start_idx = 0
    for i, line in enumerate(lines):
        if first_real_art.match(line):
            # Ga iets terug voor eventuele structurele heading
            start_idx = i
            for j in range(i - 1, max(i - 8, 0), -1):
                stripped = lines[j].strip()
                if stripped and not art_range.match(lines[j]) and len(stripped) > 5:
                    start_idx = j
                    break
            break

    return "\n".join(lines[start_idx:])


# ---------------------------------------------------------------------------
# 6. Gecombineerde cleanup-pipeline
# ---------------------------------------------------------------------------

DEFAULT_STEPS = [
    "remove_page_artifacts",   # eerst ruis weg — anders triggert remove_toc op paginanummers
    "remove_toc",
    "fix_broken_words",
    "normalize_whitespace",
    "collapse_blank_lines",
    "merge_wrapped_lines",     # PDF-soft-wraps samenvoegen tot één paragraaf-regel
]

OPTIONAL_STEPS = {
    "remove_french_lines": remove_french_lines,
    "remove_french_blocks": remove_french_blocks,
    "remove_inline_metadata": remove_inline_metadata,
    "ensure_article_headings": ensure_article_headings,
    "remove_toc_ejustice": remove_toc_ejustice,
}

ALL_STEPS = {
    "remove_toc": remove_toc,
    "remove_page_artifacts": remove_page_artifacts,
    "fix_broken_words": fix_broken_words,
    "normalize_whitespace": normalize_whitespace,
    "collapse_blank_lines": collapse_blank_lines,
    "merge_wrapped_lines": merge_wrapped_lines,
    **OPTIONAL_STEPS,
}


def split_frontmatter(text: str) -> tuple[str, str]:
    """Splits tekst in (frontmatter_block, body). Frontmatter = YAML tussen --- delimiters."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm = text[:end + 4]  # inclusief sluitende ---
            body = text[end + 4:]
            return fm, body
    return "", text


def run_pipeline(text: str, steps: list[str] | None = None,
                 preserve_frontmatter: bool = True) -> str:
    """
    Voer cleanup-stappen uit in volgorde.
    steps=None → DEFAULT_STEPS
    preserve_frontmatter=True → frontmatter wordt niet aangeraakt door cleanup.
    """
    if steps is None:
        steps = DEFAULT_STEPS

    if preserve_frontmatter:
        fm, body = split_frontmatter(text)
    else:
        fm, body = "", text

    for step in steps:
        fn = ALL_STEPS.get(step)
        if fn is None:
            raise ValueError(f"Onbekende cleanup-stap: {step!r}. Beschikbaar: {list(ALL_STEPS)}")
        body = fn(body)

    return fm + body
