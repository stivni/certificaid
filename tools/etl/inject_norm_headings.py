#!/usr/bin/env python3
"""
Post-processing: injecteer ## sectie-headings in ITAA-norm-*.md bestanden.

Werkt op de bestaande bestanden in resources/bronnen/normen/.
Detecteert heading-patronen en converteert ze naar markdown ## headings
zodat de RAG-indexer proper kan chunken.

Bijzondere behandeling:
  - opdrachtbrief: volledige herextractie uit PDF (pdftotext zonder -layout)
    omdat de -layout-mode de TOC had gefragmenteerd naar losse nummers

Patronen (in volgorde van toepassing per regel):
  A. Genummerde secties    "1. Titel"           → ## 1. Titel
     (AWW-reglement, AWW-geconsolideerd, AWW-richtlijn-bibf)
  B. Romijnse cijfer       "   I. Titel"        → ## I. Titel
     (domiciliering, gecentreerd vanuit PDF-layout)
  C. Artikel-formaat       "Artikel 1 - Titel"  → ## Artikel 1 - Titel
     (permanente-vorming, procedurereglement)
  D. Bijlage-formaat       "Bijlage I: Titel"   → ## Bijlage I. Titel
  E. Gecentreerde titels   " {25+} Titel"       → ## Titel
     (effectennorm, samenstellingsopdrachten — alleen na blanco regel)
  F. Tweetalige kolom      "NL-titel    {8+sp} FR" → ## NL-titel
     (intern-kwaliteitsmanagement)

Gebruik:
  python tools/etl/inject_norm_headings.py            # verwerk alle normen
  python tools/etl/inject_norm_headings.py --file ITAA-norm-aww-reglement.md
  python tools/etl/inject_norm_headings.py --dry-run  # toon wijzigingen
  python tools/etl/inject_norm_headings.py --report   # statistieken
"""

from __future__ import annotations

import argparse
import html
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
NORMEN_DIR = ROOT / "resources" / "bronnen" / "normen"
RAW_DIR = ROOT / "resources" / "raw" / "normen"

SKIP_FILES = {"INDEX.md", "README.md", "WETTEKSTEN-INDEX.md"}

# Bestandsnamen die al goede heading-structuur hebben (niet aanraken)
ALREADY_STRUCTURED = {
    "ITAA-norm-fusie-splitsing.md",
    "ITAA-norm-omzetting-vennootschap.md",
    "ITAA-norm-kmo-controlenorm.md",
    "ITAA-norm-algemene-controlenorm.md",
    "ISA-570-herzien.md",
}

# Naam van het raw PDF-bestand per norm (voor herextractie)
RAW_PDF_MAP = {
    "ITAA-norm-opdrachtbrief.md": "nota-opdrachtbrief.pdf",
    "ITAA-norm-aww-procedurereglement.md": "procedurereglement-AWW-art118.pdf",
    "ITAA-norm-gedragslijnen-relaties-IBR.md": "gedragslijnen-relaties-IBR.pdf",
    "ITAA-norm-aww-geconsolideerd.md": "beexcellent-416-aww-geconsolideerd.pdf",
    "ITAA-norm-aww-richtlijn-bibf.md": "beexcellent-4-bibf-aww.pdf",
    "ITAA-norm-effectennorm.md": "beexcellent-2692-effectennorm.pdf",
    "ITAA-norm-intern-kwaliteitsmanagement.md": "beexcellent-2640-kwaliteitsmanagement.pdf",
    "ITAA-norm-samenstellingsopdrachten-isrs4410.md": "beexcellent-2091-isrs4410.pdf",
}

# Bestanden die herextractie uit PDF nodig hebben (pdftotext zonder -layout)
# De originele -layout-extractie produceerde twee-kolom artefacten die headings
# braken en false-positive zinsfragmenten als sectie-titels belandden.
NEEDS_REEXTRACTION = {
    "ITAA-norm-opdrachtbrief.md",
    "ITAA-norm-aww-geconsolideerd.md",
    "ITAA-norm-aww-richtlijn-bibf.md",      # beexcellent PDF: TOC-duplicaten in -layout extractie
    "ITAA-norm-aww-procedurereglement.md",  # procedurereglement: Artikel N-formaat
    "ITAA-norm-effectennorm.md",
    "ITAA-norm-samenstellingsopdrachten-isrs4410.md",
    "ITAA-norm-ontbinding-vereffening.md",
    "ITAA-norm-intern-kwaliteitsmanagement.md",
}

# Bekende hoofdsectie-titels voor opdrachtbrief (niet-genummerd, kolom 0)
OPDRACHTBRIEF_SECTIONS = {
    "Wettelijke verplichting",
    "Enkele inhoudelijke aspecten van de opdrachtbrief",
    "De ondertekening van de opdrachtbrief",
    "Uitvoering van de opdrachtbrief",
}

# Regels te verwijderen na TOC-cleaning (specifieke voet- en kopteksten)
FOOTER_PATTERNS = [
    re.compile(r'^Page\s+\d+\s+of\s+\d+\s*$'),
    re.compile(r'^\d+/\d+\s*$'),
    re.compile(r'^Herformulering\s+.+\d+/\d+\s*$'),
    re.compile(r'^Herformulering\s+\w+\s+\d{4}\s*$'),
]

# ── helpers ───────────────────────────────────────────────────────────────────

def strip_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter_met_delimiters, body). Body is lstrip'd."""
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end == -1:
        return "", text
    return text[: end + 4], text[end + 4 :].lstrip("\n")


def clean_toc_and_page_noise(body: str) -> str:
    """Verwijder TOC-regels (met ......), losse paginanummers en footers."""
    # Verwijder form feed (paginascheiding vanuit pdftotext-extractie)
    body = body.replace("\x0c", "\n")
    lines = body.split("\n")
    cleaned = []
    for line in lines:
        stripped = line.strip()
        # TOC-regel met puntreeks
        if re.search(r"\.{4,}", line) and re.search(r"\d+\s*$", line):
            continue
        # Losse paginanummers (max 4 chars)
        if re.match(r"^[\t ]*\d+[\t ]*$", line) and len(stripped) <= 4:
            continue
        # Footers (Page N of N, N/N, Herformulering ..., etc.)
        if any(p.match(stripped) for p in FOOTER_PATTERNS):
            continue
        # Inhoudsopgave-header (lege TOC-markering)
        if re.match(r"^(Inhoud|Inhoudstafel|Inhoudsopgave|Inhoudstafel\.?)\s*$", stripped):
            continue
        cleaned.append(line)
    return "\n".join(cleaned)


def extract_pdf_text(pdf_path: Path, layout: bool = False) -> str:
    """Converteer PDF naar tekst via pdftotext."""
    args = ["pdftotext"]
    if layout:
        args.append("-layout")
    args += [str(pdf_path), "-"]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as exc:
        print(f"  ✗ pdftotext mislukt: {exc.stderr}", file=sys.stderr)
        return ""


# ── heading-injectie ──────────────────────────────────────────────────────────

# Patroon A: genummerde sectie zonder inspringing, geen decimale punt
# Bijv. "1. Algemene bepalingen" of "10.   Slotbepalingen"
# NIET: "1.1 Subparagraaf" (decimale punt)
# NIET: "   1. ..." (leading spaces → sub-artikel in preamble)
_PAT_A = re.compile(
    r"^([1-9][0-9]*)\.(\s{1,8})"
    r"([A-ZÉÀÙÔÎ][a-zA-ZéèàùôîïëüäöÉÈÀÙÔÎÏËÜÄÖ\(\)\s,\*'/-]{2,65}?)"
    r"(\s{6,}.*)?$"
)
# Extra guard: rij MAG geen decimale punt direct na de hoofdcijfers hebben
_PAT_A_EXCL = re.compile(r"^[1-9][0-9]*\.[0-9]")

# Patroon B: Romijnse cijfers
# B1: diep ingesprongen (gecentreerd via -layout): "                    I. Voorwoord"
# B2: kolom 0 in lineaire extractie (zonder -layout): "I. Doelstellingen"
# Beide varianten: altijd na een blanco regel of start van body
_PAT_B1 = re.compile(r"^\s{15,}([IVX]{1,6})\.\s+(.{3,80}?)\s*$")
_PAT_B2 = re.compile(r"^([IVX]{1,6})\.\s+(.{3,80}?)\s*$")

# Patroon C: Artikel N - Titel (permanente-vorming, procedurereglement)
_PAT_C = re.compile(r"^\s*(Artikel\s+[0-9]+)\s*[-–]\s*(.{2,80}?)\s*$")

# Patroon C2: Standalone "Artikel N" zonder koppeltitel
_PAT_C2 = re.compile(r"^\s*(Artikel\s+[0-9]+)\s*$")

# Patroon D: Bijlagen
# Bijv. "Bijlage I: Variabelen ..."
_PAT_D = re.compile(
    r"^(Bijlage|BIJLAGE)\s+([IVX0-9]+)[:\.\s]\s*(.{3,80}?)\s*$",
    re.IGNORECASE,
)

# Patroon E: Gecentreerde sectietitel in twee-kolom normen (25+ leading spaces)
# Bijv. "                              Toepassingsgebied van deze norm"
# Alleen na blanco regel; max 5 woorden; geen werkwoorden (filter zinsfragmenten)
_PAT_E = re.compile(
    r"^\s{25,}([A-ZÉÀÙÔÎ][a-zA-ZéèàùôîïëüäöÉÈÀÙÔÎÏËÜÄÖ\s,\*'/-]{8,70}?)\s*$"
)
_PAT_E_VERB = re.compile(
    r"\b(is|zijn|was|werd|werden|kan|zal|mag|moet|dient|heeft|hebben|wordt|worden|"
    r"houden|brengt|stelt|maakt|legt|neemt|geeft)\b"
)

# Patroon F: Tweetalige kolom (NL titel gevolgd door 8+ spaties + FR titel)
# Bijv. "Kwaliteitsmanagementsysteem                 Système de gestion ..."
_PAT_F = re.compile(
    r"^([A-ZÉÀÙÔÎ][a-zA-ZéèàùôîïëüäöÉÈÀÙÔÎÏËÜÄÖ\s\(\)'/-]{5,80}?)\s{8,}"
    r"[A-ZÉÀÙÔÎÏLa-zéèàùôîïëüäöA-Zl]"
)

# Patroon G: Sectietitel direct boven VEREISTEN/TOEPASSINGSMODALITEITEN
# (gebruikt lookahead naar volgende niet-lege regel)
_VEREISTEN_MARKER = re.compile(r"\bVEREISTEN\b|\bTOEPASSINGSMODALITEITEN\b")


# ─── TOC-parse + missing-section synthesis (two-column glitch fix) ───────────
#
# Sommige BeExcellent twee-kolom-PDFs (bv. ITAA-norm-aww-geconsolideerd)
# verliezen tijdens NL-kolom-extractie de standalone "N. Titel"-regels voor
# meerdere hoofdsecties. De subsecties "N.x." duiken dan op in de body zonder
# voorafgaande heading. Patroon A vindt dan niets om te promoveren.
#
# De TOC zelf overleeft de extractie wél: regel "N." gevolgd door een
# ALL-CAPS titel + dotted leader + paginanummer (bv.
# "ORGANISATIE EN INTERNE CONTROLE -------- 5"). We parsen die op om een
# canonieke {section_num: TitleCase}-map te bouwen en injecteren synthetisch
# "N. <TitleCase>"-regels vóór de eerste "N.x."-subsectie als er nog geen
# parent-heading was. Inline gegluede koppen ("7. Titel Body...") worden in
# dezelfde pass gesplitst.
#
# Werkt zonder file-specifieke triggers: enige voorwaarde is dat de body
# een TOC-blok bevat met ≥2 ``^N\.$`` standalone-regels.

_TOC_NUM_LINE = re.compile(r"^([1-9][0-9]*)\.\s*$")
# TOC-titel-regel: ALL-CAPS woorden, optioneel met spaties/leestekens,
# afgesloten met dotted-leader (---- of ....) + paginanummer.
_TOC_TITLE_LINE = re.compile(
    r"^([A-ZÉÀÙÔÎÄËÏÖÜ][A-ZÉÀÙÔÎÄËÏÖÜ\s,\(\)/°'’\"-]{4,200}?)\s*[-.]{4,}\s*\d+\s*$"
)


def _to_title_case_nl(allcaps: str) -> str:
    """Convert ALL-CAPS NL-titel naar zin-hoofdletter (eerste woord cap).

    Behoudt accent-letters en functiewoorden in lowercase (van, de, het,
    en, op, te, in, voor, ...). Geen full title-case omdat NL-conventie
    alleen het eerste woord en eigennamen capitaliseert.
    """
    _LOW = {
        "van", "de", "het", "een", "en", "of", "in", "op", "bij", "aan",
        "voor", "tot", "met", "als", "uit", "over", "om", "naar", "te",
        "per", "via", "na", "rond", "zonder", "dat", "die", "wat",
        "ten", "ter",
    }
    words = allcaps.split()
    out: list[str] = []
    for idx, w in enumerate(words):
        wl = w.lower()
        # Eerste woord altijd cap, rest behoudt lowercase voor functiewoorden
        if idx == 0:
            out.append(wl[:1].upper() + wl[1:])
        elif wl in _LOW:
            out.append(wl)
        else:
            out.append(wl)
    return " ".join(out)


# Fallback voor sectie-titels die de NL-kolom-extractie volledig verliest
# (lange titels die over twee regels wrapten in het PDF-original). Per
# bestandsnaam: ``{section_num: TitleCase}``.
#
# Reden voor hardcoded fallback i.p.v. body-scan: zonder de TOC-regel zien
# we alleen subsectie-titels in de body — die geven semantisch de verkeerde
# scope ("Clientacceptatiebeleid" is een subsectie van "Waakzaamheid ...").
# Een handmatig geverifieerde fallback is robuuster.
_SECTION_TITLE_OVERRIDES: dict[str, dict[int, str]] = {
    "ITAA-norm-aww-geconsolideerd.md": {
        4: "Waakzaamheid ten aanzien van de cliënten en de verrichtingen",
    },
}


def _extract_toc_section_titles(body: str) -> dict[int, str]:
    """Parse de TOC-regio en lever ``{section_num: TitleCase}`` op.

    Detecteert het patroon ``N.\\n<ALLCAPS titel> ------- <pagenr>`` waar de
    titel-regel direct (zonder tussenliggende blanke regels) op de
    nummer-regel volgt. Een blanke regel tussen ``N.`` en de eerstvolgende
    tekst betekent dat de echte titel verloren is in de extractie (twee-
    kolom-glitch); we noteren géén titel voor die sectie en laten een
    eventuele override de gap vullen.

    Stopt zodra niet-TOC regels komen na ≥2 succesvolle TOC-matches.
    Retourneert lege dict als geen TOC herkend wordt.
    """
    lines = body.split("\n")
    titles: dict[int, str] = {}

    i = 0
    n = len(lines)
    while i < n:
        m_num = _TOC_NUM_LINE.match(lines[i])
        if m_num and i + 1 < n:
            section_num = int(m_num.group(1))
            # Titel-regel MOET direct volgen (geen blanke ertussen). Anders
            # is de titel verloren in de twee-kolom-extractie.
            next_line = lines[i + 1].strip()
            if next_line:
                m_title = _TOC_TITLE_LINE.match(next_line)
                if m_title:
                    raw_title = m_title.group(1).strip()
                    titles[section_num] = _to_title_case_nl(raw_title)
                    i += 2
                    continue
        i += 1

    return titles


def _split_inline_section_heading(
    line: str, toc_titles: dict[int, str]
) -> tuple[str, str] | None:
    """Detecteer een inline gegluede sectie-kop ``N. Titel Body...``.

    Retourneert ``(heading_line, body_rest)`` als de regel met een TOC-titel
    begint en daarna nog body-tekst volgt. ``None`` als geen match.

    Algoritme: probeer per N in toc_titles of de regel begint met
    ``"N. " + <TOC-titel>``. Als de regel langer is dan dat prefix én
    er volgt méér content, splits.
    """
    for num, title in toc_titles.items():
        prefix = f"{num}. {title}"
        if line.startswith(prefix):
            rest = line[len(prefix):].lstrip()
            if rest:
                # Inline glue gevonden — splits op heading vs body-rest
                return prefix, rest
    return None


# Subsectie-detectie: "N.x." of "N.x" of "N.x.y" aan begin van regel
_SUBSECTION_RE = re.compile(r"^([1-9][0-9]*)\.[0-9]+(?:\.|\s|$)")

# Standalone parent-heading: "N. Titel" aan begin van regel (zonder decimaalpunt)
_PARENT_HEADING_RE = re.compile(r"^([1-9][0-9]*)\.\s+[A-ZÉÀÙÔÎ]")

# Bijlage inline-glue: "BIJLAGE IV: Titel Body..." of "Bijlage IV. Titel Body..."
# We grijpen het Romeins-numerieke gedeelte plus alles t/m de laatste "low-case
# afsluit" en splitten daarna. Heuristiek: titel eindigt op een woord met een
# zin-eindeteken óf op een titel-finale frase ("ter illustratie", "in overweging
# te nemen", ...). Pragmatisch: titel is alles tot de eerste capital-letter-na-
# spatie waar geen functiewoord aan voorafgaat.
_BIJLAGE_INLINE_RE = re.compile(
    r"^(?P<head>(?:Bijlage|BIJLAGE)\s+(?P<num>[IVX]+|[0-9]+)\s*[:\.]\s*"
    r"(?P<title>[A-Za-zÉÀÙÔÎÄËÏÖÜéèàùôîïëüäö\s\(\)/,'’\"-]{3,90}?))"
    r"\s+(?P<body>[A-ZÉÀÙÔÎ][a-z][^\n]*)$"
)


def _split_inline_bijlage_heading(line: str) -> tuple[str, str] | None:
    """Detecteer een inline-gegluede Bijlage-kop ``BIJLAGE IV: Titel Body``.

    Heuristiek: regel begint met ``Bijlage|BIJLAGE <NUM>: <Titel>`` waar
    ``<Titel>`` korte Title-Case-frase is, gevolgd door een nieuwe zin
    (``Capital + lowercase``).

    Retourneert ``(heading_line, body_rest)`` of ``None``.
    """
    m = _BIJLAGE_INLINE_RE.match(line)
    if not m:
        return None
    num = m.group("num")
    title = m.group("title").strip()
    body_rest = m.group("body").strip()
    if not body_rest:
        return None
    # Normaliseer naar "Bijlage <NUM>. <Titel>" (consistent met Pattern D)
    heading = f"Bijlage {num}. {title}"
    return heading, body_rest


def _inject_missing_section_anchors(body: str, toc_titles: dict[int, str]) -> str:
    """Injecteer ``N. <Title>``-regels vóór de eerste ``N.x.``-subsectie
    waarvan de parent-heading ontbreekt. Splits ook inline gegluede koppen
    (zowel ``N. Titel Body`` als ``BIJLAGE IV: Titel Body``).

    Werkt voor de N-N.x-fix alleen als ``toc_titles`` niet-leeg is; de
    Bijlage-inline-split werkt altijd (geen TOC-afhankelijkheid).
    """
    lines = body.split("\n")
    out: list[str] = []
    seen_parent: set[int] = set()

    for line in lines:
        stripped = line.strip()

        # 0. Bijlage inline-glue (werkt onafhankelijk van TOC)
        bijlage_split = _split_inline_bijlage_heading(stripped)
        if bijlage_split is not None:
            heading_line, rest = bijlage_split
            if out and out[-1].strip():
                out.append("")
            out.append(heading_line)
            out.append("")
            out.append(rest)
            continue

        # 1. Inline-glue check: regel begint met "N. <TocTitle> Body..."
        split = _split_inline_section_heading(stripped, toc_titles)
        if split is not None:
            heading_line, rest = split
            # Match het sectie-nummer voor seen_parent
            m = re.match(r"^([1-9][0-9]*)\.", heading_line)
            if m:
                seen_parent.add(int(m.group(1)))
            # Emit heading en body-rest als aparte regels
            if out and out[-1].strip():
                out.append("")
            out.append(heading_line)
            out.append("")
            out.append(rest)
            continue

        # 2. Standalone parent-heading "N. Titel" — markeer als gezien
        m_parent = _PARENT_HEADING_RE.match(stripped)
        if m_parent and not re.match(r"^[1-9][0-9]*\.[0-9]", stripped):
            seen_parent.add(int(m_parent.group(1)))
            out.append(line)
            continue

        # 3. Subsectie "N.x." — check of parent gezien is
        m_sub = _SUBSECTION_RE.match(stripped)
        if m_sub:
            section_num = int(m_sub.group(1))
            if section_num in toc_titles and section_num not in seen_parent:
                # Injecteer synthetic parent-heading
                title = toc_titles[section_num]
                synthetic = f"{section_num}. {title}"
                if out and out[-1].strip():
                    out.append("")
                out.append(synthetic)
                out.append("")
                seen_parent.add(section_num)
            out.append(line)
            continue

        out.append(line)

    return "\n".join(out)


def inject_headings(
    body: str,
    filename: str = "",
    use_bilingual: bool = False,
) -> str:
    """
    Verwerk body line-by-line en voeg ## headings toe.

    use_bilingual: activeer Patroon F voor tweetalige NL/FR-normen
    """
    # Pre-pass: TOC-parse + synthese van ontbrekende parent-headings +
    # split inline gegluede Bijlage/Sectie-koppen. Lost de "two-column
    # glitch" op waar sectie 2-4/6-10 in body-text verdwenen zijn na
    # NL-kolom-extractie (ITAA-norm-aww-geconsolideerd).
    toc_titles = _extract_toc_section_titles(body)
    # Override-map: vul gaten waar de NL-kolom-extractie de TOC-titel
    # volledig verloor (zie _SECTION_TITLE_OVERRIDES voor rationale).
    overrides = _SECTION_TITLE_OVERRIDES.get(filename, {})
    for num, title in overrides.items():
        toc_titles.setdefault(num, title)
    # Altijd runnen — de Bijlage-inline-split werkt zonder TOC.
    body = _inject_missing_section_anchors(body, toc_titles)

    lines = body.split("\n")
    result: list[str] = []
    prev_blank = True   # begin van body telt als "na blanco"
    n = len(lines)
    skip_lines: set[int] = set()  # indices van regels die verwerkt zijn als heading-continuatie
    in_body = False     # True zodra de eerste niet-Bijlage heading is gevonden

    opdrachtbrief_sections = OPDRACHTBRIEF_SECTIONS if filename == "ITAA-norm-opdrachtbrief.md" else set()

    for i, line in enumerate(lines):
        if i in skip_lines:
            continue
        stripped = line.strip()
        is_blank = stripped == ""

        # Bestaande headings niet aanraken
        if stripped.startswith("#"):
            result.append(line)
            prev_blank = False
            continue

        # Lookahead: volgende niet-lege regel (voor pagina-nummer-check en VEREISTEN-check)
        next_stripped = ""
        for j in range(i + 1, min(i + 4, n)):
            if lines[j].strip():
                next_stripped = lines[j].strip()
                break

        heading: str | None = None

        # ── Patroon A: genummerde sectie, kolom 0 ──
        if (
            not _PAT_A_EXCL.match(line)
            and not line.startswith(" ")
            and not line.startswith("\t")
        ):
            m = _PAT_A.match(line)
            if m:
                title = m.group(3).strip().rstrip("*").strip()
                section_num = int(m.group(1))
                # Artkel-nummers > 20 zijn vrijwel nooit sectie-nummers
                # (AWW-normen hebben max 10 secties; hogere nrs zijn artikel-nummers)
                too_high = section_num > 20
                # Zin-starters die nooit sectie-titels zijn
                sentence_starters = re.match(
                    r"^(Onderhavige\b|Deze norm|Dit artikel|Wanneer\b|"
                    r"De beroepsbeoefenaar|Het kantoor)",
                    title,
                )
                # Lang zin-fragment (lijstitem in preamble)
                long_sentence = (
                    re.match(r"^(Het |Een |De |Er |In |Bij |Als |Van )", title)
                    and len(title) > 55
                )
                if not too_high and not sentence_starters and not long_sentence:
                    # Voeg vervolg-regels toe als titel afbreekt (smal PDF-column)
                    # Bijv. "3. Algemene" + "risicobeoordeling op te" + "maken door de"
                    #      + "beroepsbeoefenaar" → volledige titel
                    if not title.endswith((".", ":", ";", "!", "?")):
                        for j in range(i + 1, min(i + 6, n)):
                            cont = lines[j].strip()
                            if not cont:
                                break
                            if (
                                cont
                                and cont[0].islower()
                                and len(cont.split()) <= 6
                                and not cont[0].isdigit()
                                and not cont.startswith("(")
                            ):
                                title = title + " " + cont
                                skip_lines.add(j)
                            else:
                                break  # stop bij niet-vervolg-lijn
                    heading = f"## {m.group(1)}. {title}"

        # ── Patroon B1: Romijnse cijfers gecentreerd (-layout stijl) ──
        if heading is None:
            m = _PAT_B1.match(line)
            if m and re.match(r"^[IVX]+$", m.group(1)):
                candidate = m.group(2).strip()
                if len(candidate) <= 80 and not candidate.startswith("#"):
                    heading = f"## {m.group(1)}. {candidate}"

        # ── Patroon B2: Romijnse cijfers kolom 0 (no-layout stijl, alleen na blanco) ──
        if heading is None and prev_blank:
            m = _PAT_B2.match(line)
            if m and re.match(r"^[IVX]+$", m.group(1)):
                candidate = m.group(2).strip()
                if len(candidate) <= 80 and not candidate.startswith("#"):
                    heading = f"## {m.group(1)}. {candidate}"

        # ── Patroon C: Artikel N - Titel ──
        if heading is None:
            m = _PAT_C.match(line)
            if m:
                heading = f"## {m.group(1)} - {m.group(2).strip()}"

        # ── Patroon C2: Artikel N (zonder titel, bijv. procedurereglement) ──
        # Strikt patroon (geen leading spaces, alleen nr aan einde) → geen prev_blank nodig
        if heading is None:
            m = _PAT_C2.match(line)
            if m and not line.startswith(" ") and not line.startswith("\t"):
                heading = f"## {m.group(1)}"

        # ── Patroon D: Bijlage
        # Alleen in body (niet in TOC-gebied): in_body wordt True na eerste echte sectie.
        # Sla ook over als volgende niet-lege regel een paginanummer is (extra TOC-check).
        if heading is None and in_body:
            m = _PAT_D.match(line)
            if m and not re.match(r"^\d+/\d+$", next_stripped):
                heading = f"## Bijlage {m.group(2)}. {m.group(3).strip()}"

        # ── Patroon G: sectietitel vóór VEREISTEN/TOEPASSINGSMODALITEITEN ──
        # (typisch voor IBR/IBA-normen in no-layout extractie)
        if heading is None and prev_blank and _VEREISTEN_MARKER.search(next_stripped):
            if (
                stripped
                and not stripped.startswith("#")
                and stripped[0].isupper()
                and not re.search(r"\d", stripped)
                and len(stripped.split()) <= 8
                and not stripped.endswith(".")
                and not stripped.endswith(":")
            ):
                heading = f"## {stripped}"

        # ── Opdrachtbrief: bekende ongenummerde hoofdsecties ──
        if heading is None and opdrachtbrief_sections:
            if stripped in opdrachtbrief_sections:
                heading = f"## {stripped}"

        # ── Patroon E: gecentreerde sectietitel (alleen na blanco) ──
        if heading is None and prev_blank:
            m = _PAT_E.match(line)
            if m:
                candidate = m.group(1).strip()
                words = candidate.split()
                last_word = words[-1].lower().rstrip(".,;:!?") if words else ""
                # Preposities / lidwoorden als laatste woord = onvolledige frase
                _nl_filler = {
                    "door", "van", "de", "het", "een", "en", "of", "in", "op",
                    "bij", "aan", "voor", "tot", "met", "als", "uit", "over",
                    "om", "naar", "te", "per", "via", "na", "rond", "zonder",
                    "dat", "die", "wat", "zijn",
                }
                # Filter: min 2 woorden, max 5 woorden, geen ALL CAPS (document-titel),
                # geen eindpunctuur, geen werkwoorden, geen onvolledige frase (prep)
                if (
                    2 <= len(words) <= 5
                    and not candidate.endswith(".")
                    and not candidate.endswith(":")
                    and not re.search(r"\d", candidate)
                    and not _PAT_E_VERB.search(candidate)
                    and candidate != candidate.upper()   # geen ALL CAPS
                    and last_word not in _nl_filler
                    and not candidate.startswith("Le ")
                    and not candidate.startswith("La ")
                    and not candidate.startswith("Les ")
                    and not candidate.startswith("En ")
                ):
                    heading = f"## {candidate}"

        # ── Patroon F: tweetalige kolom NL + FR (opt-in) ──
        if heading is None and use_bilingual:
            m = _PAT_F.match(line)
            if m:
                candidate = m.group(1).strip()
                # Extra filter: korte NL-titel, geen zin (geen punt/komma aan einde)
                if (
                    2 <= len(candidate.split()) <= 6
                    and not candidate.endswith(".")
                    and not candidate.endswith(":")
                    and not candidate.endswith(",")
                    and not re.search(r"\d", candidate)
                    and not _PAT_E_VERB.search(candidate)
                ):
                    heading = f"## {candidate}"

        # ── Schrijf resultaat ──
        if heading is not None:
            # Zorg voor blanco regel vóór heading
            if result and result[-1].strip():
                result.append("")
            result.append(heading)
            prev_blank = False
            # Activeer in_body zodra eerste niet-Bijlage heading gevonden
            if not in_body and not heading.startswith("## Bijlage"):
                in_body = True
        else:
            result.append(line)
            prev_blank = is_blank

    return "\n".join(result)


# ── per-bestand verwerking ────────────────────────────────────────────────────

def process_file(md_path: Path, dry_run: bool = False) -> dict:
    """
    Verwerk één norm-MD-bestand. Retourneert statistieken.
    """
    filename = md_path.name
    text = md_path.read_text(encoding="utf-8")
    fm, body = strip_frontmatter(text)

    # Herextractie uit PDF indien nodig
    if filename in NEEDS_REEXTRACTION and filename in RAW_PDF_MAP:
        pdf_path = RAW_DIR / RAW_PDF_MAP[filename]
        if pdf_path.exists():
            raw = extract_pdf_text(pdf_path, layout=False)
            if raw:
                body = html.unescape(raw)
            else:
                print(f"  ⚠ herextractie mislukt, gebruik bestaande body")
        else:
            print(f"  ⚠ raw PDF niet gevonden: {pdf_path}")

    # Opkuis
    body = html.unescape(body)
    body = clean_toc_and_page_noise(body)

    # Tweetalig patroon (F) alleen voor intern-kwaliteitsmanagement
    use_bilingual = (filename == "ITAA-norm-intern-kwaliteitsmanagement.md")

    # Tel headings voor
    h2_before = len(re.findall(r"^##\s", body, re.MULTILINE))

    # Injecteer headings
    new_body = inject_headings(body, filename=filename, use_bilingual=use_bilingual)

    # Tel headings na
    h2_after = len(re.findall(r"^##\s", new_body, re.MULTILINE))

    if h2_before == h2_after and filename not in NEEDS_REEXTRACTION:
        return {"file": filename, "h2_before": h2_before, "h2_after": h2_after, "changed": False}

    # Herbouw bestand
    output = fm + "\n\n" + new_body.strip() + "\n"

    if not dry_run:
        md_path.write_text(output, encoding="utf-8")

    return {"file": filename, "h2_before": h2_before, "h2_after": h2_after, "changed": True}


# ── hoofdprogramma ────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--file",
        metavar="FILENAME",
        help="Verwerk alleen dit bestand (naam zonder pad)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Toon wat er zou worden gewijzigd zonder te schrijven",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Toon heading-statistieken voor alle bestanden",
    )
    args = parser.parse_args()

    if args.report:
        print("Bestand                                              H2")
        print("-" * 60)
        for f in sorted(NORMEN_DIR.glob("ITAA-norm-*.md")):
            body = strip_frontmatter(f.read_text(encoding="utf-8"))[1]
            count = len(re.findall(r"^##\s", body, re.MULTILINE))
            print(f"  {f.name:<50} {count:>4}")
        return

    if args.file:
        targets = [NORMEN_DIR / args.file]
    else:
        targets = sorted(NORMEN_DIR.glob("ITAA-norm-*.md"))

    print(f"=== inject_norm_headings {'(dry-run) ' if args.dry_run else ''}===")
    stats = []
    for md_path in targets:
        if md_path.name in SKIP_FILES or md_path.name in ALREADY_STRUCTURED:
            continue
        print(f"  {md_path.name} ...", end=" ", flush=True)
        stat = process_file(md_path, dry_run=args.dry_run)
        delta = stat["h2_after"] - stat["h2_before"]
        flag = "✓" if delta > 0 else ("~" if stat["changed"] else "–")
        print(f"{flag}  h2: {stat['h2_before']} → {stat['h2_after']}  (+{delta})")
        stats.append(stat)

    total_added = sum(s["h2_after"] - s["h2_before"] for s in stats)
    changed = sum(1 for s in stats if s["changed"])
    print(f"\nKlaar: {changed}/{len(stats)} bestanden gewijzigd, {total_added} headings toegevoegd.")


if __name__ == "__main__":
    import os
    os.chdir(ROOT)
    main()
