"""iesba — extractor voor IESBA Code of Ethics PDF (ADR-005 §2).

De IESBA Code of Ethics is een Engelstalige PDF gegenereerd met Microsoft Word.
Structuur:
  - Lopende headers: "THE CODE", "SECTION NNN", "PART N" als losse regels
  - Paginanummers als standalone regels
  - Part-headings: "PART N – TITEL OVER\nMEERDERE REGELS"
  - Section-headings: "SECTION NNN\nTITEL VAN DE SECTIE"
  - Paragraafnummers: "NNN.N", "NNN.N An", "RNNN.N", "NNN.N An" als standalone regels

Werkwijze:
  1. pdftotext (zonder -layout, i.e. simpele mode) — beste resultaat voor deze PDF
  2. Cleanup-pass:
     a. Strip lopende headers (THE CODE, SECTION NNN, PART N standalone)
     b. Strip standalone paginanummers
     c. Promoveer PART-headings naar # markdown headings
     d. Promoveer SECTION-headings naar ## markdown headings
     e. Bold paragraafnummers (inline in tekst)

Signatuur:
    extract(cfg: dict, source_name: str) -> str

Returns de body zonder frontmatter. De orchestrator voegt frontmatter toe.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

# ─── Regex-constanten ─────────────────────────────────────────────────────────

# Paragraafnummer-formaten in IESBA:
#   100.1      — basis
#   100.2      — basis
#   100.5 A1   — application material (spatie + letter + cijfer)
#   100.5 A2   — application material
#   R100.6     — requirement (R-prefix)
#   R210.4     — requirement
#   900.55     — hogere nummers
# Matcht ook standalone (geen toelichting achteraan op dezelfde regel)
_PARA_NUM_RE = re.compile(
    r"^(R?\d{2,3}\.\d+(?:\s+A\d+)?)$",
    re.MULTILINE,
)

# Glitch uit pdftotext-output: een spatie kruipt tussen majeur- en minor-nr van
# een paragraafnummer. Voorbeeld: '120. 15 A1' moet '120.15 A1' worden vóór
# we ze als heel paragraafnummer kunnen bolden.
_PARA_NUM_GLITCH_RE = re.compile(
    r"^(R?\d{2,3})\.\s+(\d+(?:\s+A\d+)?)$",
    re.MULTILINE,
)

# Lopende headers die als losse regels voorkomen in de PDF
_RUNNING_HEADER_RE = re.compile(
    r"^(?:THE CODE|PART\s+\d+|SECTION\s+\d{3})$",
    re.MULTILINE,
)

# Standalone paginanummers (1-4 cijfers op een lege regel)
_PAGE_NUMBER_RE = re.compile(
    r"^\d{1,4}$",
    re.MULTILINE,
)

# PART-heading: "PART N – REST VAN DE TITEL" (eventueel meerregelig)
# De titel loopt door op de volgende regel als de huidige eindigt zonder punt.
# Voorbeeld:
#   PART 1 – COMPLYING WITH THE CODE, FUNDAMENTAL
#   PRINCIPLES AND CONCEPTUAL FRAMEWORK
_PART_HEADING_RE = re.compile(
    r"^(PART\s+(\d+))\s*[–—-]\s*(.+?)$",
    re.MULTILINE,
)

# SECTION-heading: "SECTION NNN\nTITEL" (twee opeenvolgende regels)
_SECTION_HEADING_RE = re.compile(
    r"^SECTION\s+(\d{3})\n([A-Z][A-Z ,\-–()&/]+)$",
    re.MULTILINE,
)

# Form feed (page separator in pdftotext output)
_FORM_FEED_RE = re.compile(r"\x0c")

# Inter-Part TABLE OF CONTENTS-blok: "TABLE OF CONTENTS\n\nPage\n\n..."
# Gevolgd door Section-vermeldingen met dotted-leaders.
# Strip het hele blok van "TABLE OF CONTENTS" tot en met de volgende lege rule
# vóór de echte Part-heading.
# Aanpak: strip "TABLE OF CONTENTS" + "Page" als standalone regels.
_TOC_LABEL_RE = re.compile(
    r"^(TABLE OF CONTENTS|Page)$",
    re.MULTILINE,
)


# ─── Titel-hulpfuncties ───────────────────────────────────────────────────────

def _title_case_iesba(text: str) -> str:
    """Converteer ALL CAPS IESBA-tekst naar Title Case.

    Behoudt korte voorzetsels/lidwoorden in lowercase (a, and, for, in, of,
    on, the, to, with) tenzij ze het eerste woord zijn.
    """
    lower_words = {"a", "and", "for", "in", "of", "on", "the", "to", "with",
                   "an", "at", "but", "by", "from", "or", "nor"}
    words = text.strip().split()
    result = []
    for i, word in enumerate(words):
        if i == 0 or word.lower() not in lower_words:
            result.append(word.capitalize())
        else:
            result.append(word.lower())
    return " ".join(result)


# ─── Helper-functies ──────────────────────────────────────────────────────────

_TOC_SECTION_LINE_RE = re.compile(
    r"^Section\s+\d{3}\s+\w",
    re.I,
)


def _is_toc_section_line(line: str) -> bool:
    """Detecteer een TOC-vermelding: 'Section NNN Titel...'."""
    return bool(_TOC_SECTION_LINE_RE.match(line.strip()))


# ─── Hoofd-cleanup ────────────────────────────────────────────────────────────

def _cleanup_iesba(raw: str) -> str:
    """Verwerk ruwe pdftotext-output van IESBA PDF naar gestructureerde markdown.

    Stappen:
    1. Normaliseer form feeds naar paragraafscheiding
    2. Promoveer PART-headings (meerregelig, CAPS)
    3. Promoveer SECTION-headings (twee regels)
    4. Strip lopende headers (THE CODE, SECTION NNN standalone, PART N standalone)
    5. Strip standalone paginanummers
    6. Bold paragraafnummers
    7. Normaliseer witruimte
    """
    text = raw

    # Stap 1: form feeds → dubbele newline
    text = _FORM_FEED_RE.sub("\n\n", text)

    # Stap 2: PART-headings promoveren
    # "PART 1 – COMPLYING WITH THE CODE, FUNDAMENTAL\nPRINCIPLES AND CONCEPTUAL FRAMEWORK"
    # → "# Part 1 — Complying with the Code, Fundamental Principles and Conceptual Framework"
    # We doen dit voor de lopende-header-strip zodat we PART N niet dubbel strippen.

    def _replace_part(m: re.Match) -> str:
        part_num = m.group(2)
        title_first = m.group(3).strip()
        return f"# Part {part_num} — {_title_case_iesba(title_first)}"

    text = _PART_HEADING_RE.sub(_replace_part, text)

    # Na PART-replacement: een uppercase-only regel die direct volgt op de
    # # Part-heading is de titel-voortzetting. Absorbeer deze.
    # Voorbeeld: "# Part 1 — ...\nPRINCIPLES AND CONCEPTUAL FRAMEWORK"
    # De eerste substitutie pakt al de tekst op dezelfde regel; de
    # meerregelige voortzetting is een aparte aanpak.
    _PART_CONT_AFTER_HEADING_RE = re.compile(
        r"(# Part \d+ — [^\n]+)\n([A-Z][A-Z ,\-–()&/]+)$",
        re.MULTILINE,
    )

    def _absorb_continuation(m: re.Match) -> str:
        heading = m.group(1)
        continuation = m.group(2).strip()
        return f"{heading} {_title_case_iesba(continuation)}"

    # Loop zodat we meerdere continuatieregels absorberen
    prev = None
    while prev != text:
        prev = text
        text = _PART_CONT_AFTER_HEADING_RE.sub(_absorb_continuation, text)

    # Stap 3: SECTION-headings promoveren
    # "SECTION 100\nCOMPLYING WITH THE CODE"
    # → "## Section 100 — Complying with the Code"
    def _replace_section(m: re.Match) -> str:
        sec_num = m.group(1)
        title = _title_case_iesba(m.group(2).strip())
        return f"## Section {sec_num} — {title}"

    text = _SECTION_HEADING_RE.sub(_replace_section, text)

    # Stap 4: strip lopende headers (standalone regels), TOC-labels en
    # inter-Part TOC-blokken (TABLE OF CONTENTS + Page)
    lines = text.split("\n")
    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        if _RUNNING_HEADER_RE.match(stripped):
            continue  # verwijder losse running header
        if _TOC_LABEL_RE.match(stripped):
            continue  # verwijder TABLE OF CONTENTS / Page labels
        cleaned_lines.append(line)
    text = "\n".join(cleaned_lines)

    # Stap 5: strip standalone paginanummers
    lines = text.split("\n")
    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        if _PAGE_NUMBER_RE.match(stripped):
            continue
        cleaned_lines.append(line)
    text = "\n".join(cleaned_lines)

    # Stap 5b: strip dotted-leader TOC-entries (Section NNN Titel.......... N)
    # en losse "Section NNN Titel" regels in mini-TOC blokken
    # Twee patronen:
    #   "Section 200 Applying...............  40" (met dots)
    #   "Section 210 Conflicts of Interest" (zonder dots, wel paginanummer)
    _DOTTED_LEADER_LINE_RE = re.compile(
        r"^.+?\.{3,}.*$",
        re.MULTILINE,
    )
    text = _DOTTED_LEADER_LINE_RE.sub("", text)

    # Stap 5c: strip # Part-headings die onmiddellijk gevolgd worden door
    # "Section NNN ..." regels (mini-TOC blok, nog niet gepromoveerd via regex)
    # Strategie: vind "# Part N — ..." gevolgd door een niet-lege regel
    # die begint met "Section \d{3}" (TOC-entry zonder dots al gestript)
    # → verwijder de # Part-heading in die context
    def _strip_toc_part_headings(txt: str) -> str:
        """Strip Part-headings die onderdeel zijn van een inter-Part mini-TOC."""
        lines = txt.split("\n")
        result = []
        skip_next_part = False
        for i, line in enumerate(lines):
            # Zoek een # Part-heading die gevolgd wordt door een TOC-achtige regel
            if line.startswith("# Part "):
                # Kijk naar de volgende niet-lege regel
                next_nonempty = next(
                    (l for l in lines[i + 1:i + 5] if l.strip()),
                    "",
                )
                # Als de volgende niet-lege regel een "Section NNN ..." TOC-entry is
                # EN ook eindigt met een paginanummer of wordt gevolgd door meer
                # Section-entries → dit is een mini-TOC Part-heading
                if _is_toc_section_line(next_nonempty):
                    continue  # sla deze TOC-Part-heading over
            result.append(line)
        return "\n".join(result)

    text = _strip_toc_part_headings(text)

    # Stap 5d: dedupliceer opeenvolgende # Part-headings
    # Na dotted-leader stripping kan een mini-TOC Part-entry ongedetecteerd
    # blijven; de echte Part-heading volgt dan direct daarna.
    # Verwijder de eerste van twee identieke # Part N-headings in een klein
    # contextvenster (≤15 regels afstand).
    def _dedup_part_headings(txt: str) -> str:
        lines = txt.split("\n")
        result = []
        last_part_heading: str | None = None
        last_part_idx: int = -1
        for i, line in enumerate(lines):
            if line.startswith("# Part "):
                if last_part_heading == line and i - last_part_idx <= 20:
                    # Dubbele Part-heading gevonden — verwijder de eerder
                    # toegevoegde (die was de TOC-versie)
                    result = [l for l in result if l != last_part_heading or
                              result.index(l) < len(result) - 1]
                    # Eenvoudiger: verwijder de laatste occurrence in result
                    for j in range(len(result) - 1, -1, -1):
                        if result[j] == last_part_heading:
                            del result[j]
                            break
                last_part_heading = line
                last_part_idx = i
            result.append(line)
        return "\n".join(result)

    text = _dedup_part_headings(text)

    # Stap 6: bold paragraafnummers — standalone op eigen regel
    # "100.1\n\nText" → "**100.1**\n\nText"
    # Vervanging: alleen als de regel uitsluitend het paragraafnummer bevat

    # Stap 6a: glitch-fix — '120. 15 A1' → '120.15 A1' (pdftotext-artefact)
    text = _PARA_NUM_GLITCH_RE.sub(r"\1.\2", text)

    def _bold_para(m: re.Match) -> str:
        return f"**{m.group(1)}**"

    text = _PARA_NUM_RE.sub(_bold_para, text)

    # Stap 7: absorbeer vervolgregels voor onvolledige ## Section headings
    # Voorbeeld: "## Section 200 — Applying the Conceptual Framework –\n
    # PROFESSIONAL ACCOUNTANTS IN BUSINESS"
    # Heuristic: ## heading die eindigt op – of — of een ander koppelstuk
    # EN de volgende regel is ALL CAPS (max 80 chars) → absorbeer
    _INCOMPLETE_SECTION_RE = re.compile(
        r"(## Section \d+ — [^\n]+[–—-])\n([A-Z][A-Z ,\-–()&/]{5,79})$",
        re.MULTILINE,
    )

    def _complete_section(m: re.Match) -> str:
        heading = m.group(1).rstrip("–—- ").rstrip()
        continuation = m.group(2).strip()
        return f"{heading} {_title_case_iesba(continuation)}"

    prev = None
    while prev != text:
        prev = text
        text = _INCOMPLETE_SECTION_RE.sub(_complete_section, text)

    # Stap 8: normaliseer opeenvolgende lege regels (max 2)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.strip()

    return text


# ─── Publieke extractor-API ───────────────────────────────────────────────────

def extract(cfg: dict, source_name: str) -> str:
    """Extract IESBA Code of Ethics PDF naar markdown (ADR-005 §2).

    Args:
        cfg: source-config voor deze bron (must have 'raw' field).
        source_name: bron-naam (voor foutmeldingen).

    Returns:
        Gecleande body als markdown-string, zonder frontmatter.
    """
    raw = cfg.get("raw")
    if not raw:
        raise ValueError(f"{source_name}: iesba-extractor vereist een 'raw'-veld in cfg")

    raw_path = Path(raw)
    if not raw_path.is_absolute():
        raw_path = ROOT / raw
    if not raw_path.exists():
        raise FileNotFoundError(
            f"{source_name}: raw PDF niet gevonden: {raw_path}"
        )

    params = (cfg.get("extract") or {}).get("params") or {}
    # Standaard start_page=20: pagina's 1-19 zijn voorblad, TOC en gidstekst.
    # De eigenlijke Code-tekst begint op pagina 20 (PART 1).
    start_page = params.get("start_page", 20)

    # pdftotext zonder -layout: betere tekstvolgorde voor deze enkolomige PDF
    cmd = ["pdftotext"]
    if start_page > 1:
        cmd += ["-f", str(start_page)]
    cmd += [str(raw_path), "-"]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"{source_name}: pdftotext mislukt: {result.stderr}"
        )

    return _cleanup_iesba(result.stdout)
