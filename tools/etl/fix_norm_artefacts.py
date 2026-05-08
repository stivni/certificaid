#!/usr/bin/env python3
"""
Targeted ETL-fixes voor specifieke artefacten in bron-MD's.

Pakt de overgebleven 'rare voorkomens' aan die `inject_norm_headings.py` niet
opvangt (te file-specifiek voor generieke heuristieken). Elke fix-functie is
opt-in en zelfgedocumenteerd: ze kijkt zelf of het patroon van toepassing is
en past de tekst aan.

Lijst van fixes (alfabetisch op functie-naam, niet alle worden op elke norm
toegepast — zie `FIX_PIPELINE_PER_FILE`):

  - merge_scrambled_section_title:  PDF-artefact waarbij elk woord van een
    section-title op een aparte regel staat met blanco-regels ertussen
    (bijv. AWW-richtlijn-BIBF section 3).
  - normalize_heading_levels:       `# **N. X**` (titel-style) → `## N. X`
    en `## ***N.N X***` → `### N.N X` etc. (KMO-controlenorm-pattern).
  - remove_html_entities:           `&rsquo;` → `'`, `&ldquo;` → `"`, etc.
  - remove_inline_page_numbers:     `1/4`, `2/4` als losse regels.
  - remove_recurring_footer:        verwijdert herhaalde paginavoetregels
    (bv. copyright-strings die op elke PDF-pagina staan).
  - replace_ocr_lab:                `lAB` → `IAB`, `lBR` → `IBR` (l↔I).
  - strip_form_feeds:               `\\x0c` form-feed characters.

Gebruik:
  python tools/etl/fix_norm_artefacts.py            # alle fixes op alle bekende files
  python tools/etl/fix_norm_artefacts.py --file ITAA-norm-X.md
  python tools/etl/fix_norm_artefacts.py --dry-run
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parent.parent.parent
NORMEN_DIR = ROOT / "resources" / "bronnen" / "normen"


# ─── Fix-resultaat per call ─────────────────────────────────────────────────

@dataclass
class FixResult:
    name: str
    applied: bool = False
    changes: int = 0
    note: str = ""


@dataclass
class FileResult:
    bestand: str
    fixes: list[FixResult] = field(default_factory=list)
    text_before: str = ""
    text_after: str = ""

    @property
    def changed(self) -> bool:
        return self.text_before != self.text_after


# ─── Helper: split frontmatter ──────────────────────────────────────────────

_FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def split_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter_block_with_delims, body)."""
    m = _FM_RE.match(text)
    if not m:
        return "", text
    return text[: m.end()], text[m.end() :]


# ─── Individuele fix-functies ───────────────────────────────────────────────

def replace_ocr_lab(body: str) -> tuple[str, FixResult]:
    """OCR-fout: kleine-l ipv hoofdletter-I in afkortingen IAB / IBR / IDAC / IFAC."""
    n = 0
    new_body = body
    for wrong, right in (("lAB", "IAB"), ("lBR", "IBR"), ("lDAC", "IDAC"), ("lFAC", "IFAC")):
        # Word-boundary om losse `lAB`-fragmenten in echte woorden te vermijden
        pat = re.compile(rf"\b{wrong}\b")
        new_body, count = pat.subn(right, new_body)
        n += count
    return new_body, FixResult(
        name="replace_ocr_lab",
        applied=n > 0,
        changes=n,
        note=f"{n} OCR-correctie(s) (lAB→IAB enz.)",
    )


def strip_form_feeds(body: str) -> tuple[str, FixResult]:
    """Verwijder `\\x0c` form-feed characters (PDF-paginascheiding)."""
    n = body.count("\x0c")
    return body.replace("\x0c", ""), FixResult(
        name="strip_form_feeds",
        applied=n > 0,
        changes=n,
        note=f"{n} form-feed character(s) verwijderd",
    )


def remove_inline_page_numbers(body: str) -> tuple[str, FixResult]:
    """Verwijder regels die enkel een paginanummer bevatten ('1/4', 'Page N of N')."""
    pat = re.compile(
        r"(?m)^\s*(?:\d+/\d+|Page\s+\d+\s+of\s+\d+)\s*$\n?",
    )
    new_body, n = pat.subn("", body)
    return new_body, FixResult(
        name="remove_inline_page_numbers",
        applied=n > 0,
        changes=n,
        note=f"{n} inline paginanummer-regel(s) verwijderd",
    )


def remove_recurring_footer(body: str, footer_lines: list[str]) -> tuple[str, FixResult]:
    """
    Verwijder een herhaalde voetregel (bv. copyright op elke PDF-pagina).

    `footer_lines` is een lijst van strings — exact-match per regel. Als de
    eerste regel matcht, worden de daaropvolgende regels die ook matchen
    (in volgorde) ook verwijderd, plus omliggende blanco's.

    Verwijdert ALLE voorkomens (geen 'eerste behouden').
    """
    if not footer_lines:
        return body, FixResult(name="remove_recurring_footer", applied=False)

    lines = body.split("\n")
    n_lines = len(lines)
    n_footers = len(footer_lines)
    keep: list[bool] = [True] * n_lines

    i = 0
    matches = 0
    while i < n_lines:
        if i + n_footers <= n_lines and all(
            lines[i + j].strip() == footer_lines[j].strip()
            for j in range(n_footers)
        ):
            for j in range(n_footers):
                keep[i + j] = False
            matches += 1
            i += n_footers
        else:
            i += 1

    if matches == 0:
        return body, FixResult(name="remove_recurring_footer", applied=False)

    new_lines = [ln for ln, k in zip(lines, keep) if k]
    new_body = "\n".join(new_lines)
    # Collapse runs van 4+ blank lines naar 2 (de footer-removal kan grote
    # blokken witruimte achterlaten)
    new_body = re.sub(r"\n{4,}", "\n\n\n", new_body)
    return new_body, FixResult(
        name="remove_recurring_footer",
        applied=True,
        changes=matches,
        note=f"{matches} voorkomens verwijderd",
    )


def merge_scrambled_section_title(body: str, prefix: str, expected_words: list[str]) -> tuple[str, FixResult]:
    """
    Fix sectietitels waar elk woord op een aparte regel staat met blanco's
    ertussen (PDF-artefact, bv. AWW-richtlijn-BIBF '## 3. Algemene...').

    `prefix`: de start van de regel waar de title vermoedelijk afbreekt
              (bv. '## 3. Algemene risicobeoordeling beroepsbeoefenaar')
    `expected_words`: woorden die in de juiste volgorde moeten worden
              opgepikt uit de eerstvolgende blanco-regels
              (bv. ['op', 'te', 'maken', 'door', 'de'])

    Het volledig gemergde resultaat is `prefix + ' ' + ' '.join(expected_words)`.
    Als prefix niet voorkomt, no-op.
    """
    if prefix not in body:
        return body, FixResult(name="merge_scrambled_section_title", applied=False, note="prefix niet gevonden")

    # Regex: prefix + (\n\s*<word>)+ — opnieuw opbouwen tot één regel
    target_pat = re.compile(
        re.escape(prefix)
        + r"(?:\s*\n\s*\n\s*"
        + r"\s*\n\s*\n\s*".join(re.escape(w) for w in expected_words)
        + r")",
        re.MULTILINE,
    )
    new_title = prefix + " " + " ".join(expected_words)
    new_body, n = target_pat.subn(new_title, body)
    return new_body, FixResult(
        name="merge_scrambled_section_title",
        applied=n > 0,
        changes=n,
        note=f"prefix '{prefix[:50]}...' samengevoegd met {len(expected_words)} woorden",
    )


def remove_orphan_lines(body: str, lines_to_remove: list[str]) -> tuple[str, FixResult]:
    """
    Verwijder specifieke regels (exact-match na strip) — bedoeld voor TOC-resten
    die als wees in de body achterblijven. Bijv. BIJLAGE-titel zonder vervolg.

    `lines_to_remove`: lijst van exacte stripped-strings.
    """
    if not lines_to_remove:
        return body, FixResult(name="remove_orphan_lines", applied=False)

    targets = {s.strip() for s in lines_to_remove}
    new_lines: list[str] = []
    n = 0
    for line in body.split("\n"):
        if line.strip() in targets:
            n += 1
            continue
        new_lines.append(line)
    return "\n".join(new_lines), FixResult(
        name="remove_orphan_lines",
        applied=n > 0,
        changes=n,
        note=f"{n} wees-regel(s) verwijderd",
    )


def collapse_blank_runs(body: str, max_blanks: int = 2) -> tuple[str, FixResult]:
    """
    Reduceer runs van >max_blanks opeenvolgende blanco regels naar max_blanks.

    Behandelt zowel echt lege regels als regels met enkel whitespace
    (PDF-artefact: `\\n   \\n   \\n` ipv `\\n\\n\\n`).
    """
    # Eerst: regels die enkel whitespace bevatten leeg maken (\n[ \t]+\n → \n\n)
    body = re.sub(r"(?<=\n)[ \t]+(?=\n)", "", body)

    # Dan: collapse opeenvolgende blanco regels
    pat = re.compile(rf"\n{{{max_blanks + 2},}}")
    target = "\n" * (max_blanks + 1)
    new_body, n = pat.subn(target, body)
    return new_body, FixResult(
        name="collapse_blank_runs",
        applied=n > 0,
        changes=n,
        note=f"{n} blank-run(s) gecollapsed naar max {max_blanks}",
    )


def remove_html_entities(body: str) -> tuple[str, FixResult]:
    """Vervang HTML-entiteiten door hun Unicode-equivalent."""
    mapping = {
        "&rsquo;": "'",
        "&lsquo;": "'",
        "&rdquo;": '"',
        "&ldquo;": '"',
        "&hellip;": "…",
        "&sect;": "§",
        "&eacute;": "é",
        "&egrave;": "è",
        "&agrave;": "à",
        "&iuml;": "ï",
        "&euml;": "ë",
        "&ouml;": "ö",
        "&uuml;": "ü",
        "&ccedil;": "ç",
        "&amp;": "&",
        "&nbsp;": " ",
    }
    n = 0
    new_body = body
    for ent, repl in mapping.items():
        count = new_body.count(ent)
        if count:
            new_body = new_body.replace(ent, repl)
            n += count
    return new_body, FixResult(
        name="remove_html_entities",
        applied=n > 0,
        changes=n,
        note=f"{n} HTML-entit{'eit' if n == 1 else 'eiten'} vervangen",
    )


def remove_prefix_until(body: str, marker: str) -> tuple[str, FixResult]:
    """Verwijder alles in de body vóór de eerste occurrence van marker (marker zelf behouden)."""
    idx = body.find(marker)
    if idx == -1:
        return body, FixResult(
            name="remove_prefix_until",
            applied=False,
            note=f"marker {marker[:40]!r} niet gevonden",
        )
    removed_chars = idx
    new_body = body[idx:]
    return new_body, FixResult(
        name="remove_prefix_until",
        applied=True,
        changes=1,
        note=f"{removed_chars} chars vóór '{marker[:30]}' verwijderd",
    )


def inject_plain_headings(body: str, heading_texts: list[str]) -> tuple[str, FixResult]:
    """Voeg '## ' toe voor regels die exact overeenkomen met een sectietitel (zonder heading-prefix)."""
    n = 0
    new_body = body
    for text in heading_texts:
        pat = re.compile(rf"(?m)^[ \t]*{re.escape(text)}[ \t]*$")
        replacement = f"## {text}"
        new_body, count = pat.subn(replacement, new_body)
        n += count
    return new_body, FixResult(
        name="inject_plain_headings",
        applied=n > 0,
        changes=n,
        note=f"{n} plain-tekst sectie(s) als ## heading gemarkeerd",
    )


def fix_specific_ocr(body: str, pairs: list[tuple[str, str]]) -> tuple[str, FixResult]:
    """Directe tekst-vervangingen voor file-specifieke OCR-fouten of heading-correcties."""
    n = 0
    new_body = body
    for wrong, right in pairs:
        count = new_body.count(wrong)
        if count:
            new_body = new_body.replace(wrong, right)
            n += count
    return new_body, FixResult(
        name="fix_specific_ocr",
        applied=n > 0,
        changes=n,
        note=f"{n} specifieke tekst-vervanging(en)",
    )


def strip_toc_dot_lines(body: str) -> tuple[str, FixResult]:
    """
    Verwijder TOC-stippenregels (inhoudsopgave-artefacten).

    Matcht twee patronen:
    - Losse stippelregels: '......................'
    - Titel + stippels:    'Inleiding .......... 6'
    """
    # Match elke regel die eindigt op 4+ punten + optioneel spatie + getal
    pat = re.compile(r"(?m)^[^\n]*\.{4,}\s*\d*\s*$\n?")
    new_body, n = pat.subn("", body)
    return new_body, FixResult(
        name="strip_toc_dot_lines",
        applied=n > 0,
        changes=n,
        note=f"{n} TOC-stippenlijn(en) verwijderd",
    )


def strip_toc_block(body: str, toc_start_re: str, first_section_marker: str) -> tuple[str, FixResult]:
    """
    Verwijder een junk-TOC-blok: het gedeelte tussen toc_start_re en first_section_marker.

    toc_start_re: regex die het begin van het TOC-blok matcht (wordt zelf ook verwijderd)
    first_section_marker: tekst-marker die het einde van het TOC-blok markeert (blijft behouden)
    """
    idx_end = body.find(first_section_marker)
    if idx_end == -1:
        return body, FixResult(name="strip_toc_block", applied=False, note="section_marker niet gevonden")

    m = re.search(toc_start_re, body[:idx_end], re.MULTILINE)
    if not m:
        return body, FixResult(name="strip_toc_block", applied=False, note="toc_start_re niet gevonden vóór marker")

    removed_chars = idx_end - m.start()
    new_body = body[: m.start()] + body[idx_end:]
    return new_body, FixResult(
        name="strip_toc_block",
        applied=True,
        changes=1,
        note=f"TOC-blok van {removed_chars} chars verwijderd (voor '{first_section_marker[:30]}')",
    )


def dedent_indented_headings(body: str) -> tuple[str, FixResult]:
    """
    Verwijder leading whitespace voor markdown-headings.

    Sommige bronnen (bv. KMO-controlenorm) hebben tab-ingesprongen sectie-headings
    (`\\t## ***2.1***`) waardoor noch de QA-checker noch de RAG-chunker ze detecteert.
    Dit normaliseert ze naar kolom-0.
    """
    pat = re.compile(r"(?m)^[ \t]+(#{1,6} )", )
    new_body, n = pat.subn(r"\1", body)
    return new_body, FixResult(
        name="dedent_indented_headings",
        applied=n > 0,
        changes=n,
        note=f"{n} ingesprongen heading(s) ge-dedent",
    )


def normalize_heading_levels(body: str) -> tuple[str, FixResult]:
    """
    KMO-controlenorm-patroon: hoofdstukken op H1, subsecties op H2 met
    bold/asterisk-styling. RAG-chunker splitst op H2, dus we willen:

      - Genummerde hoofdstukken `# **N. TITLE**` of bijlagen `# **BIJLAGE...**`
        → `## N. TITLE`  (promoten naar H2-niveau zodat ze chunk-grenzen worden)
      - Subsecties `## ***N.N text***` → `## N.N text`  (BLIJVEN H2, alleen
        bold/asterisk-styling weg — meer chunk-grenzen voor grote hoofdstukken)
      - Subsubsecties `### **N.N.N text**` → `### N.N.N text` (blijven H3,
        styling weg)

    Behoudt de echte H1-titel (zonder cijfer/BIJLAGE-prefix).
    """
    lines = body.split("\n")
    out: list[str] = []
    n_h1_to_h2 = 0
    n_h2_strip = 0
    n_h3_strip = 0

    for line in lines:
        # H1 met genummerde sectie of BIJLAGE → H2 (chunk-grens)
        m = re.match(r"^# \*\*((?:[0-9]+\.\s+|BIJLAGE\s+\d+\s*[:.])\s*.+?)\*\*\s*$", line)
        if m:
            out.append(f"## {m.group(1)}")
            n_h1_to_h2 += 1
            continue

        # H2 met *** styling → H2 zonder styling (extra chunk-grenzen voor grote hoofdstukken)
        m = re.match(r"^## \*\*\*(.+?)\*\*\*\s*$", line)
        if m:
            out.append(f"## {m.group(1)}")
            n_h2_strip += 1
            continue

        # H3 met ** styling → H3 zonder styling
        m = re.match(r"^### \*\*(.+?)\*\*\s*$", line)
        if m:
            out.append(f"### {m.group(1)}")
            n_h3_strip += 1
            continue

        out.append(line)

    n = n_h1_to_h2 + n_h2_strip + n_h3_strip
    parts = []
    if n_h1_to_h2:
        parts.append(f"{n_h1_to_h2} H1→H2")
    if n_h2_strip:
        parts.append(f"{n_h2_strip} H2 styling-strip")
    if n_h3_strip:
        parts.append(f"{n_h3_strip} H3 styling-strip")
    note = ", ".join(parts) if parts else "geen wijzigingen"

    return "\n".join(out), FixResult(
        name="normalize_heading_levels",
        applied=n > 0,
        changes=n,
        note=note,
    )


# ─── Pipeline-config per file ──────────────────────────────────────────────
#
# Per file: lijst van (fix_callable, kwargs)-tuples. De fix-callable heeft
# signatuur (body, **kwargs) -> (new_body, FixResult).

FIX_PIPELINE_PER_FILE: dict[str, list[tuple[Callable, dict]]] = {

    "ITAA-norm-gedragslijnen-relaties-IBR.md": [
        (replace_ocr_lab, {}),
        (fix_specific_ocr, {
            "pairs": [
                ("BEROEPSRELATlES", "BEROEPSRELATIES"),
                ("fmanciële", "financiële"),
                ("fmancieel", "financieel"),
                ("WIe ", "wie "),   # leading-space context om false positives te vermijden
            ],
        }),
        (strip_form_feeds, {}),
        (remove_inline_page_numbers, {}),
        (inject_plain_headings, {
            "heading_texts": [
                "Definities",
                "Eerste principe - Aanvaarding van een controleopdracht",
                "Tweede principe - Aanvaarding van een raadgevende opdracht",
                "Derde principe - Meningsverschil",
                "Vierde principe - Contacten met de voorganger",
                "Vijfde principe - Onbetaalde erelonen",
                "Zesde principe - Overdracht van het dossier",
            ],
        }),
        (collapse_blank_runs, {"max_blanks": 2}),
    ],

    "ITAA-norm-permanente-vorming.md": [
        (remove_recurring_footer, {
            "footer_lines": [
                "© ITAA – Norm permanente vorming van het Instituut van de Belastingadviseurs en de Accountants,",
                "goedgekeurd door de Raad van 1 december 2020.",
            ],
        }),
    ],

    "ITAA-norm-kmo-controlenorm.md": [
        (remove_html_entities, {}),
        (dedent_indented_headings, {}),
        (normalize_heading_levels, {}),
    ],

    # Pas geëxtraheerd via extract_norm_twocolumn.py: TOC-stippels resterend
    "ITAA-norm-ontbinding-vereffening.md": [
        (strip_toc_dot_lines, {}),
        (collapse_blank_runs, {"max_blanks": 2}),
    ],

    "ITAA-norm-effectennorm.md": [
        (strip_toc_dot_lines, {}),
        (collapse_blank_runs, {"max_blanks": 2}),
    ],

    "ITAA-norm-samenstellingsopdrachten-isrs4410.md": [
        (strip_toc_dot_lines, {}),
        (collapse_blank_runs, {"max_blanks": 2}),
    ],

    # Pas geëxtraheerd via extract_norm_twocolumn.py (bilingual → NL-only):
    # FR-fragmenten verwijderen + heading corrigeren + extra headings toevoegen.
    "ITAA-norm-intern-kwaliteitsmanagement.md": [
        # Correctie heading: "OP\n\nCABINET" → "OP KANTOORNIVEAU"
        (fix_specific_ocr, {
            "pairs": [
                (
                    "## ALGEMENE VEREISTEN VAN INTERN KWALITEITSMANAGEMENT OP\n\nCABINET ",
                    "## ALGEMENE VEREISTEN VAN INTERN KWALITEITSMANAGEMENT OP KANTOORNIVEAU",
                ),
            ],
        }),
        # Verwijder achtergebleven FR-regels
        (remove_orphan_lines, {
            "lines_to_remove": [
                "Acceptation de missions",
                "Documentation",
            ],
        }),
        (inject_plain_headings, {
            "heading_texts": [
                "Inleiding",
                "Definities",
                "Kwaliteitsmanagementsysteem",
                "Eindverantwoordelijke(n) voor het kwaliteitsmanagementsysteem",
                "Vereisten",
                "Governance en leiderschap",
                "Relevante ethische voorschriften",
                "Aanvaarding van opdrachten",
                "Inwerkingtreding",
            ],
        }),
        (collapse_blank_runs, {"max_blanks": 2}),
    ],

    "ITAA-norm-aww-richtlijn-bibf.md": [
        # Heading is al gemergd maar woordvolgorde verkeerd (beroepsbeoefenaar te vroeg):
        (fix_specific_ocr, {
            "pairs": [
                (
                    "## 3. Algemene risicobeoordeling beroepsbeoefenaar op te maken door de",
                    "## 3. Algemene risicobeoordeling op te maken door de beroepsbeoefenaar",
                ),
            ],
        }),
        # TOC-blok (losse nummers + kapotte titels) vóór eerste sectie verwijderen
        (strip_toc_block, {
            "toc_start_re": r"^\n\n1\.\n",
            "first_section_marker": "## 1. Algemene bepalingen",
        }),
        (collapse_blank_runs, {"max_blanks": 2}),
    ],

    "ITAA-norm-opdrachtbrief.md": [
        # Verwijder het OPDRACHTBRIEF-titelpagina-blok + nummers-only TOC
        (remove_prefix_until, {"marker": "Alhoewel de verplichting"}),
        (collapse_blank_runs, {"max_blanks": 2}),
    ],

    "ITAA-norm-aww-geconsolideerd.md": [
        # Typefout in §10: "gesolideerde" → "geconsolideerde"
        (fix_specific_ocr, {
            "pairs": [
                ("gesolideerde tekst is overgenomen", "geconsolideerde tekst is overgenomen"),
            ],
        }),
        # Bijlage III §3° geografische risicofactoren: c) en d) fout genummerd als a) en b)
        (fix_specific_ocr, {
            "pairs": [
                (
                    "a) landen waarvoor sancties, embargo's of soortgelijke maatregelen gelden die\n"
                    "bijvoorbeeld door de Europese Unie of de Verenigde Naties zijn uitgevaardigd;\n"
                    "b) landen die financiering of ondersteuning verschaffen voor terroristische activiteiten, of\n"
                    "op het grondgebied waarvan als terroristisch aangemerkte organisaties actief zijn.",
                    "c) landen waarvoor sancties, embargo's of soortgelijke maatregelen gelden die\n"
                    "bijvoorbeeld door de Europese Unie of de Verenigde Naties zijn uitgevaardigd;\n"
                    "d) landen die financiering of ondersteuning verschaffen voor terroristische activiteiten, of\n"
                    "op het grondgebied waarvan als terroristisch aangemerkte organisaties actief zijn.",
                ),
            ],
        }),
    ],

    "ITAA-norm-domiciliering.md": [
        # Verwijder logo-blok + titelpagina vóór echte inhoud
        (remove_prefix_until, {"marker": "## I. Voorwoord"}),
        # Verwijder herhaald copyright-blok (verschijnt na elke PDF-sectie)
        (remove_recurring_footer, {
            "footer_lines": [
                "© ITAA – Norm betreffende de verenigbaarheid van de activiteit van domiciliëring van entiteiten,",
                "goedgekeurd door de raad van 2 juli 2024.",
            ],
        }),
        # Verwijder losse voetnotenregels en `---` dividers die na copyright staan
        (remove_orphan_lines, {
            "lines_to_remove": [
                "---",
                "    Conform de wet van 29 maart 2018 tot registratie van dienstenverleners aan vennootschappen.",
                "    Conform artikel III.16 Wetboek van Economisch Recht.",
                # Multi-line footnote 2 (werd in PDF als body-tekst bewaard)
                "Hieronder wordt verstaan het deelnemen aan de effectieve transactie van de aan- of verkoop van de aandelen en niet de",
                "juridische bijstand in het kader hiervan. 3 Artikel 2,12° van de wet van 17 maart 2019 betreffende de beroepen van accountant",
                "en belastingadviseur. 4 Artikel 2,3° van de wet van 17 maart 2019 betreffende de beroepen van accountant en belastingadviseur.",
            ],
        }),
        (collapse_blank_runs, {"max_blanks": 2}),
    ],

    "ITAA-norm-aww-reglement.md": [
        (remove_orphan_lines, {
            "lines_to_remove": [
                "BIJLAGE I: Variabelen ten minste in overweging te nemen in de integrale",
            ],
        }),
        (collapse_blank_runs, {"max_blanks": 2}),
    ],

    "ITAA-norm-omzetting-vennootschap.md": [
        (collapse_blank_runs, {"max_blanks": 2}),
    ],

    "ITAA-norm-permanente-vorming.md": [
        (remove_recurring_footer, {
            "footer_lines": [
                "© ITAA – Norm permanente vorming van het Instituut van de Belastingadviseurs en de Accountants,",
                "goedgekeurd door de Raad van 1 december 2020.",
            ],
        }),
        (collapse_blank_runs, {"max_blanks": 2}),
    ],
}


# ─── Hoofdpipeline ──────────────────────────────────────────────────────────

def process_file(md_path: Path, *, dry_run: bool = False) -> FileResult:
    name = md_path.name
    pipeline = FIX_PIPELINE_PER_FILE.get(name, [])
    text_before = md_path.read_text(encoding="utf-8")

    result = FileResult(bestand=str(md_path.relative_to(ROOT)), text_before=text_before)
    if not pipeline:
        result.text_after = text_before
        return result

    fm, body = split_frontmatter(text_before)
    new_body = body

    for fn, kwargs in pipeline:
        new_body, fr = fn(new_body, **kwargs)
        result.fixes.append(fr)

    new_text = fm + new_body
    result.text_after = new_text

    if not dry_run and result.changed:
        md_path.write_text(new_text, encoding="utf-8")

    return result


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--file", help="één specifieke filename in resources/bronnen/normen/")
    p.add_argument("--dry-run", action="store_true", help="toon zonder schrijven")
    args = p.parse_args()

    if args.file:
        targets = [NORMEN_DIR / args.file]
    else:
        targets = [NORMEN_DIR / name for name in sorted(FIX_PIPELINE_PER_FILE.keys())]

    print(f"=== fix_norm_artefacts {'(dry-run) ' if args.dry_run else ''}===")
    n_changed = 0
    for path in targets:
        if not path.exists():
            print(f"  ✗ {path.name}: niet gevonden")
            continue
        result = process_file(path, dry_run=args.dry_run)
        if not result.fixes:
            print(f"  ⊝ {path.name}: geen pipeline geconfigureerd")
            continue
        applied_fixes = [f for f in result.fixes if f.applied]
        if not applied_fixes:
            print(f"  – {path.name}: pipeline geen wijzigingen")
            continue
        flag = "✓" if result.changed else "~"
        print(f"  {flag} {path.name}")
        for f in applied_fixes:
            print(f"      {f.name}: {f.note}")
        if result.changed:
            n_changed += 1

    print(f"\nKlaar: {n_changed}/{len(targets)} bestanden gewijzigd.")
    if args.dry_run:
        print("Dry-run: niets geschreven. Verwijder --dry-run om wijzigingen toe te passen.")


if __name__ == "__main__":
    main()
