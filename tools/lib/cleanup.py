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


# ---------------------------------------------------------------------------
# Heading-vervolg samenvoegen
# ---------------------------------------------------------------------------

# Structurele markdown-heading: ###, ####, ##### (niet ##, dat is een artikel).
_STRUCTURAL_KEYWORD = (
    r"TITEL|TITRE|HOOFDSTUK|Hoofdstuk|CHAPITRE|Afdeling|Onderafdeling"
    r"|BOEK|Boek|DEEL|Deel|LIVRE|Livre"
)
_STRUCTURAL_HEADING = re.compile(
    rf"^(#{{3,6}})\s+(?:{_STRUCTURAL_KEYWORD})\b", re.IGNORECASE
)
# Verwijdert de markdown-#'s + structureel label (TITEL I., Afdeling Vbis.-, ...)
# zodat alleen de heading-body overblijft.
_STRIP_LABEL = re.compile(
    rf"^#{{3,6}}\s+(?:{_STRUCTURAL_KEYWORD})\s+[\dIVXivx][\w./]*\.?\s*[-–—]?\s*",
    re.IGNORECASE,
)

# De heading is af als ze eindigt op zinsterminator, sluitingshaakje of een
# Justel-sluiter "]<digit>".
_HEADING_COMPLETE_END = re.compile(r"(?:[.!?:)]|\][1-9])\s*$")

# Een vervolgregel mag NIET starten met deze tokens — dan is het een nieuw blok,
# geen heading-staart.
_NEW_BLOCK_START = re.compile(
    rf"^(?:"
    r"#{1,6}\s"                                    # andere markdown-heading
    r"|\*?\*?Art(?:\.|ikel)\s+[\dIVXivx]"          # 'Art. 1' / 'Artikel 1'
    r"|§\s*\d"                                     # § 1
    r"|\(\d+\)\s*<"                                # Justel-ref (1)<DWG …>
    r"|\([a-z]"                                    # Justel-metadata: '(opgeheven bij ...)', '(van toepassing ...)'
    r"|\d+°"                                       # 1° lijstmarker
    r"|[-–—]\s"                                    # markdown lijst-item of korte ref ('- IX / 16 -')
    r"|[-–—]{3,}"                                  # decoratielijn / 'historiek'-marker ('----------', '---- historiek ----')
    rf"|(?:{_STRUCTURAL_KEYWORD})\s+"              # andere ongeformatteerde structurele heading
    r"|(?:Eerste|Tweede|Derde|Vierde|Vijfde|Zesde|Zevende|Achtste|Negende|Tiende)"
    r"\s+(?:afdeling|hoofdstuk|titel|boek|deel)\b"  # 'Eerste afdeling - ...'
    r")",
    re.IGNORECASE,
)

# TOC-detectie: 4 of meer dots op een rij = leader-dots in een inhoudsopgave.
_TOC_LEADER = re.compile(r"\.{4,}")

# Nederlandse functiewoorden — een heading die hierop eindigt is bijna zeker
# afgebroken. Idem voor een vervolgregel die ermee begint.
_FUNCTION_WORDS = frozenset({
    "de", "het", "een", "der", "des", "ten", "ter",
    "van", "voor", "in", "op", "met", "bij", "aan", "tot", "naar", "om",
    "over", "onder", "uit", "tegen", "tussen", "binnen", "buiten", "langs",
    "en", "of", "dan", "maar", "noch", "doch",
    "die", "dat", "deze", "dit",
    "zijn", "haar", "hun", "hen",
    "vier", "vijf", "zes", "zeven",  # 'AAN DE VIER' style
})

# Maximum aantal vervolgregels die we proberen samen te voegen. Hoog genoeg
# om PDF-kolom-wraps van meerdere regels in één pass te vatten (anders blijft
# een staartregel achter en is de stap niet idempotent).
_MAX_HEADING_CONT_LINES = 8
# Maximum lengte voor een 'kort' vervolg dat eindigt op een terminator.
_SHORT_TAIL_LEN = 50
# Boven deze bodylengte gaan we ervan uit dat de heading PDF-kolom-wrap heeft.
_LONG_BODY_THRESHOLD = 60


def _heading_body(line: str) -> str:
    """De body van een structurele heading, zonder ###'en en zonder label."""
    return _STRIP_LABEL.sub("", line.rstrip()).strip()


def _last_word(text: str) -> str:
    words = re.findall(r"[\wÀ-ÿ]+", text)
    return words[-1] if words else ""


def _first_word(text: str) -> str:
    m = re.match(r"\s*([\wÀ-ÿ]+)", text)
    return m.group(1) if m else ""


def _should_merge(heading: str, cont: list[str]) -> bool:
    """Beslis of de heading + vervolgregels samengevoegd moeten worden."""
    head = heading.rstrip()
    if not head or not cont:
        return False
    # Rule 1: heading eindigt op dash → expliciet truncated
    if head[-1] in "-–—":
        return True
    body = _heading_body(heading)
    # Rule 2: heading-body + vervolg samen in HOOFDLETTERS (TITEL I. - DE VERSCHILLENDE / INKOMSTENBELASTINGEN,
    # HOOFDSTUK I / INVOERING VAN DE BELASTING)
    combined = (body + " " + " ".join(cont)).strip()
    if combined and combined == combined.upper() and re.search(r"[A-ZÀ-Þ]", combined):
        return True
    # Rule 3: laatste woord is een functiewoord
    if _last_word(head).lower() in _FUNCTION_WORDS:
        return True
    # Rule 4: vervolgregel start met functiewoord (kleine letter)
    first = cont[0]
    if first and first[0].islower() and _first_word(first).lower() in _FUNCTION_WORDS:
        return True
    # Rule 5: kort éénregelig vervolg dat eindigt op terminator (slot van zin)
    if len(cont) == 1 and len(first) <= _SHORT_TAIL_LEN and first[-1] in ".!?:":
        return True
    # Rule 6: lange heading-body (>= drempel) — typisch teken van PDF-kolom-wrap.
    # Wordt enkel bereikt als de NEW_BLOCK_START-guard al gepasseerd is, dus de
    # vervolgregel is geen artikel, paragraaf, Justel-ref of subsection-heading.
    if len(body) >= _LONG_BODY_THRESHOLD:
        return True
    return False


def merge_heading_continuations(text: str) -> str:
    """
    Voeg structurele heading-vervolgregels samen met de heading.

    PDF-extractie breekt soms structurele headings af over meerdere regels:

        ### TITEL I. - DE VERSCHILLENDE

        INKOMSTENBELASTINGEN

        ## Art. 1

    Wordt na deze stap:

        ### TITEL I. - DE VERSCHILLENDE INKOMSTENBELASTINGEN

        ## Art. 1

    De heading komt enkel in aanmerking als:
      - ze begint met ###/####/##### + een structureel sleutelwoord (TITEL,
        HOOFDSTUK, Afdeling, Onderafdeling, BOEK, DEEL, …)
      - ze NIET eindigt op een terminator (`. : ! ?`), sluithaakje of
        Justel-sluiter (`]N`)
      - ze geen TOC-leader-dots bevat (`....`)

    En enkel als één van de merge-regels vuurt (zie `_should_merge`):
      1. heading eindigt op `-`/`–`/`—`
      2. heading-body + vervolg samen in HOOFDLETTERS
      3. laatste woord van de heading is een functiewoord (de, voor, en, …)
      4. vervolg begint met functiewoord in kleine letter
      5. kort eenregelig vervolg eindigt op terminator
      6. heading-body is lang (>= 60 chars) — typisch PDF-kolom-wrap

    Vervolgregels worden weggegooid als ze starten met een nieuw blok
    (artikel, paragraaf, Justel-ref, andere structurele heading,
    `Eerste afdeling -`, …) of als ze TOC-leader-dots bevatten.

    Idempotent: een al-samengevoegde heading eindigt op terminator en wordt
    in de volgende run overgeslagen.
    """
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = _STRUCTURAL_HEADING.match(line)
        head = line.rstrip()

        if not m or _HEADING_COMPLETE_END.search(head) or _TOC_LEADER.search(head):
            out.append(line)
            i += 1
            continue

        # Mogelijk truncated — zoek vervolgregels
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        if j >= len(lines):
            out.append(line)
            i += 1
            continue

        first = lines[j].strip()
        if _NEW_BLOCK_START.match(first) or _TOC_LEADER.search(first):
            out.append(line)
            i += 1
            continue

        cont: list[str] = []
        k = j
        while k < len(lines) and len(cont) < _MAX_HEADING_CONT_LINES:
            stripped = lines[k].strip()
            if not stripped:
                break
            if _NEW_BLOCK_START.match(stripped) or _TOC_LEADER.search(stripped):
                break
            cont.append(stripped)
            if stripped[-1] in ".!?:":
                k += 1
                break
            k += 1

        if not cont or not _should_merge(line, cont):
            out.append(line)
            i += 1
            continue

        out.append(head + " " + " ".join(cont))
        i = k

    return "\n".join(out)


# ---------------------------------------------------------------------------
# Bijlages / Annexen markeren
# ---------------------------------------------------------------------------

# Kale bijlage-regel: 'Bijlage A', 'Bijlage I', 'BIJLAGE I', 'Annex 1',
# 'Bijvoegsel', evt. gevolgd door inline subtitel na '.' of ':'.
# Eist `^…$` zodat inline-references als 'Bijlage A, onder I' niet matchen.
_APPENDIX_BARE = re.compile(
    r"^(Bijlage\s+(?:[A-Z]\d?|[IVX]+)"
    r"|BIJLAGE\s+(?:[A-Z]\d?|[IVX]+)"
    r"|Annex\s+[A-Z0-9]+"
    r"|ANNEX\s+[A-Z0-9]+"
    r"|Bijvoegsel(?:\s+\d+)?)"
    r"(?:\s*[.:]\s*(\S.{0,100}?))?"
    r"\s*$"
)
# Reeds-een-heading: '## Bijlage A', '### BIJLAGE I', enz. Niet hernoemen,
# wel in_appendix=True zetten zodat ## Art.-degradatie verder werkt.
_APPENDIX_HEADING_LINE = re.compile(
    r"^#{1,6}\s+(?:Bijlage|BIJLAGE|Annex|ANNEX|Bijvoegsel)\b"
)
# ## Art. X-heading die binnen de bijlage-sectie naar ### moet (concordantie-
# tabellen en arrest-discussies bevatten anders duplicate artikel-IDs).
_ARTICLE_H2 = re.compile(r"^##\s+(Art\.\s+\S.*?)\s*$")
# Bijlage-titels die concordance-mode aanduiden — alle volgende kale
# 'Bijlage X' lijnen zonder subtitel zijn dan tabel-entries, geen siblings.
_CONCORDANCE_TITLE = re.compile(
    r"\b(concordantie|transponering|correlatie|transpositie)",
    re.IGNORECASE,
)
# Subtitel-regel direct ná een kale Bijlage-regel — moet géén structurele
# subkop zijn (DEEL A, HOOFDSTUK X, lijst-item, paragraaf, art., enz.).
_SUBTITLE_REJECT = re.compile(
    r"^(?:[*#(\-]|\d+°|§|"
    r"Art\.|Artikel\s|"
    r"BIJLAGE|Bijlage|ANNEX|Annex|"
    r"DEEL\s|Deel\s|HOOFDSTUK|Hoofdstuk|TITEL|Titel|"
    r"AFDELING|Afdeling|ONDERAFDELING|Onderafdeling|"
    r"BOEK|Boek|LIVRE|Livre|"
    r"LIJST\b)",
    re.IGNORECASE,
)


def _next_line_subtitle(lines: list[str], start: int) -> tuple[str | None, int]:
    """
    Geef (subtitel, eind_index) terug. Subtitel is de eerstvolgende non-empty
    regel direct ná een kale Bijlage-regel, mits die er als titel uitziet
    (5–100 chars, geen structurele subkop).
    eind_index is de index ná de subtitel-regel (zodat de outer loop verder
    kan); als geen subtitel gevonden wordt, eind_index == start.
    """
    j = start
    while j < len(lines) and not lines[j].strip():
        j += 1
    if j >= len(lines):
        return None, start
    cand = lines[j].strip()
    if not (5 <= len(cand) <= 120):
        return None, start
    if _SUBTITLE_REJECT.match(cand):
        return None, start
    return cand, j + 1


def mark_appendices(text: str) -> str:
    """
    Markeer 'Bijlage X' / 'BIJLAGE X' / 'Annex Y' / 'Bijvoegsel' op een eigen
    regel als '## Bijlage X — <subtitel>' headings, en degrade ## artikel-
    headings binnen de bijlage-sectie naar ### om duplicate artikel-IDs te
    voorkomen (concordantietabellen, arrest-discussies).

    Patronen die als heading gedetecteerd worden:
      - 'Bijlage A' / 'Bijlage I' (kaal label)
      - 'Bijlage A. <subtitel>' / 'Bijlage A: <subtitel>'  (inline subtitel)
      - 'BIJLAGE I' (EU-stijl, hoofdletters)
      - 'Annex 1' / 'ANNEX I' / 'Bijvoegsel'
    Inline-references blijven onaangeroerd: 'Bijlage A, onder I' matcht niet
    omdat na het label geen `.` of `:` of einde-regel staat.

    Subtitel-detectie:
      - inline (zelfde regel, na `.` of `:`)
      - of de eerstvolgende non-empty regel, mits 5–120 chars en niet
        beginnend met een structurele marker (DEEL/HOOFDSTUK/TITEL/...,
        Art., §, lijst-item, ...).

    Idempotent: regels die al een markdown-heading zijn ('## Bijlage A')
    worden niet hernoemd. De flag `in_appendix` wordt wél gezet zodat
    downstream artikel-degradatie blijft werken bij herhaalde runs.
    """
    lines = text.split("\n")
    out: list[str] = []
    in_appendix = False
    in_concordance = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if _APPENDIX_HEADING_LINE.match(line):
            in_appendix = True
            in_concordance = bool(_CONCORDANCE_TITLE.search(line))
            out.append(line)
            i += 1
            continue
        m = _APPENDIX_BARE.match(line)
        if m:
            label = m.group(1).strip()
            subtitle = m.group(2).strip().rstrip(":") if m.group(2) else None
            next_i = i + 1
            if not subtitle:
                cand, next_i = _next_line_subtitle(lines, i + 1)
                if cand:
                    subtitle = cand.rstrip(":").strip()
            # In een concordantietabel staan kale bijlage-references zonder
            # subtitel (bv. 'Bijlage II' tussen '— ... —'). Onderscheid op
            # basis van in_concordance: gezet wanneer een eerdere bijlage-
            # heading een concordance-keyword bevat ('Concordantietabel',
            # 'Transponeringstabel', ...) of wanneer ## Art.-degradaties zijn
            # waargenomen.
            if in_appendix and in_concordance and not subtitle:
                out.append(line)
                i += 1
                continue
            new_heading = f"## {label}" + (f" — {subtitle}" if subtitle else "")
            out.append(new_heading)
            in_appendix = True
            in_concordance = bool(_CONCORDANCE_TITLE.search(new_heading))
            i = next_i
            continue
        if in_appendix and in_concordance:
            # In concordance-mode: degrade dupliccate ## Art.-headings naar ###
            # om duplicate artikel-IDs in de chunk-index te voorkomen. Buiten
            # concordance-mode laten we ## Art.-headings in bijlages staan
            # (bv. WBTW Bijlage B 'Opmerkingen en arresten' — elke arrest-
            # discussie wordt een eigen chunk, geen duplicaat met de hoofdwet).
            ma = _ARTICLE_H2.match(line)
            if ma:
                out.append(f"### {ma.group(1)}")
                i += 1
                continue
        out.append(line)
        i += 1
    return "\n".join(out)


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
    "merge_heading_continuations",  # afgebroken structurele headings (TITEL/HOOFDSTUK/...) herstellen
    "mark_appendices",         # 'Bijlage A' / 'BIJLAGE I' → '## Bijlage A — <subtitel>'
]

OPTIONAL_STEPS = {
    "remove_french_lines": remove_french_lines,
    "remove_french_blocks": remove_french_blocks,
    "remove_inline_metadata": remove_inline_metadata,
    "ensure_article_headings": ensure_article_headings,
    "remove_toc_ejustice": remove_toc_ejustice,
    "merge_heading_continuations": merge_heading_continuations,
    "mark_appendices": mark_appendices,
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
