#!/usr/bin/env python3
"""
Laag 1 van de bronnen-QA-gate (ADR-005 §5): deterministische checks per bron-MD.

Genereert een machine-leesbaar rapport met pass/warn/fail per bron en concrete
vindplaatsen van problemen. Subagent-Laag-2 (`qa_subagent_prompt.md`) gebruikt
dit rapport als invoer voor inhoudelijke beoordeling; Laag-3 (`mark_trusted.py`)
zet de uiteindelijke trust-status.

Gecontroleerde criteria (zie ADR-005 §5 — Laag 1):

  Frontmatter & provenance:
    - frontmatter aanwezig + verplichte velden voor bron-rol
    - provenance-blok valide (inputs, tooling, generated_at)

  Structuur (RAG-bruikbaarheid):
    - aantal `##`-headings
    - heading-drempel: minstens 1 `##` voor bestand >5K chars
    - langste sectie tussen `##` < 24K chars (RAG-bovengrens, ADR-006)
    - chunk-config valid (bij --staging): chunk.level int 2-6, chunk.type string,
      chunk.sub_strategy null of string

  Extractie-artefacten:
    - geen `\\x0c` form feed (PDF-paginascheiding niet opgekuist)
    - geen `....\\d+$` TOC-residu in body
    - geen `Page N of N` of `N/N` paginavoetregels
    - geen runs van >5 lege regels
    - geen kolom-bleed: `[A-Z][a-z]+\\s{20,}[A-Z]` patronen
    - OCR-flags: `lAB`, `lBR`, vermoedelijke l/I-verwarring

Verdict per bron: `pass | warn | fail`
  - fail   = blokker voor RAG-indexering (b.v. provenance ontbreekt, mega-chunk)
  - warn   = bruikbaar maar suboptimaal (b.v. kolom-bleed, korte runs)
  - pass   = alle checks groen

Gebruik:
  python tools/etl/qa_bron.py --all                       # alle bronnen (resources/)
  python tools/etl/qa_bron.py --bron-rol norm
  python tools/etl/qa_bron.py --collection cbn-adviezen
  python tools/etl/qa_bron.py --file resources/bronnen/normen/X.md
  python tools/etl/qa_bron.py --all --report-only         # alleen samenvatting
  python tools/etl/qa_bron.py --staging                   # alle staging-MDs
  python tools/etl/qa_bron.py --staging --bron WIB92      # één staging-MD

Output: `data/etl/qa/<run-id>.json` + samenvatting op stdout.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from tools.lib.provenance import read_provenance  # noqa: E402

BRON_DIRS = {
    "wettekst": ROOT / "resources" / "bronnen" / "wetteksten",
    "norm":     ROOT / "resources" / "bronnen" / "normen",
    "advies":   ROOT / "resources" / "bronnen" / "adviezen",
}

STAGING_DIR = ROOT / "data" / "etl-staging"

COLLECTION_TO_DIR = {
    "wetteksten":   BRON_DIRS["wettekst"],
    "itaa-normen":  BRON_DIRS["norm"],
    "cbn-adviezen": BRON_DIRS["advies"],
}

SKIP_FILES = {"INDEX.md", "README.md", "WETTEKSTEN-INDEX.md"}

# Drempels (afgestemd op ADR-006 RAG-bovengrens van 24K per chunk)
# Een bestand zonder headings is één chunk. Dat is pas een probleem als het
# bestand groter is dan de absolute RAG-bovengrens (24K); dan overschrijdt
# de auto-split zijn semantische basis. Bestanden < 24K zonder headings zijn
# acceptabel als één groot-maar-behapbaar chunk.
HEADING_THRESHOLD_CHARS = 24_000   # bestand >24K chars zonder heading → warn
MAX_SECTION_CHARS = 24_000          # langste sectie > 24K → warn/fail
MAX_BLANK_RUN = 5                   # >5 lege regels op rij → warn
MAX_SAMPLES_PER_CHECK = 3           # max voorbeelden per problematische check

# Verplichte frontmatter-velden per bron-rol
REQUIRED_FRONTMATTER = {
    "wettekst": {"tags", "bron", "provenance"},
    "norm":     {"tags", "naam", "type", "bron", "provenance"},
    "advies":   {"nummer", "datum", "themas", "bron", "provenance"},
}

# Patroondefinities — hergebruik van inject_norm_headings.py-regex waar mogelijk
_RE_FORM_FEED = re.compile(r"\x0c")
_RE_TOC_DOTS = re.compile(r"\.{4,}\s*\d+\s*$", re.MULTILINE)
_RE_PAGE_FOOTER = re.compile(r"^(Page\s+\d+\s+of\s+\d+|\d+/\d+|Herformulering\s+\w+\s+\d{4}.*\d+/\d+)\s*$", re.MULTILINE)
_RE_COLUMN_BLEED = re.compile(r"[A-Za-zéèàùôîïëüäöÉÈÀÙÔÎÏËÜÄÖ][a-zéèàùôîïëüäö]{2,}\s{20,}[A-ZÉÈÀÙÔÎÏ][a-zéèàùôîïëüäö]")
_RE_OCR_LAB = re.compile(r"\blAB\b|\blBR\b|\blDAC\b|\blFAC\b")  # I/l-verwarring op bekende afkortingen
_FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


# ─── Result types ────────────────────────────────────────────────────────────

@dataclass
class CheckResult:
    """Eén check op één bron."""
    name: str
    status: str               # "pass" | "warn" | "fail"
    detail: Optional[str] = None
    samples: list[str] = field(default_factory=list)


@dataclass
class BronReport:
    """Volledige QA-uitkomst voor één bron-MD."""
    bestand: str              # relatieve pad
    bron_rol: str
    file_size_chars: int
    heading_count: int
    max_section_chars: int
    verdict: str              # "pass" | "warn" | "fail"
    checks: list[CheckResult]


# ─── Helpers ─────────────────────────────────────────────────────────────────

def _bron_rol_from_path(path: Path) -> str:
    """Leid bron-rol af uit map-structuur (zelfde mapping als rag_index.py)."""
    parent = path.parent.name
    return {
        "wetteksten": "wettekst",
        "normen":     "norm",
        "adviezen":   "advies",
    }.get(parent, "unknown")


def _bron_rol_from_staging(frontmatter: Optional[str]) -> str:
    """Leid bron-rol af uit staging-frontmatter.

    Staging-MDs dragen meestal `bron_rol: itaa_lex` (wetteksten). Voor de QA-checks
    mappen we dat naar `wettekst`. Andere expliciete waarden worden 1:1 doorgegeven.
    Fallback: `wettekst` (staging-folder bevat momenteel alleen wetteksten).
    """
    if frontmatter is None:
        return "wettekst"
    m = re.search(r"(?m)^bron_rol\s*:\s*['\"]?([A-Za-z_]+)['\"]?\s*$", frontmatter)
    if not m:
        return "wettekst"
    raw = m.group(1)
    return {
        "itaa_lex":  "wettekst",
        "wetteksten": "wettekst",
        "wettekst":  "wettekst",
        "norm":      "norm",
        "normen":    "norm",
        "advies":    "advies",
        "adviezen":  "advies",
    }.get(raw, raw)


def _split_frontmatter(text: str) -> tuple[Optional[str], str]:
    """Returns (frontmatter_yaml, body_text). Frontmatter is None als afwezig."""
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    return m.group(1), text[m.end():]


def _best_chunk_level_and_max(body: str) -> tuple[int, int]:
    """Zoek het diepste heading-niveau (H2–H6) waarvoor de langste sectie ≤ MAX_SECTION_CHARS.

    Logica (van diepste naar ondiepste):
      1. Probeer elk niveau met ≥ 2 headings, van H6 → H2.
      2. Zodra een niveau de langste sectie ≤ MAX_SECTION_CHARS geeft → return dat.
      3. Geen enkel niveau haalt de grens: return het niveau met de kleinste max
         (meest fijnmazige beschikbare splitsing — fallback voor warn-rapportage).
      4. Geen headings aanwezig: return (2, len(body)) — body is één mega-sectie.

    Returnt: (gekozen_niveau, max_sectie_lengte_op_dat_niveau)
    """
    best_fallback: tuple[int, int] = (2, len(body))
    for level in range(6, 1, -1):
        pattern = re.compile(rf"(?m)^#{{{level}}}\s+.*$")
        if len(pattern.findall(body)) < 2:
            continue
        parts = pattern.split(body)
        nonempty = [len(p) for p in parts if p.strip()]
        max_len = max(nonempty) if nonempty else 0
        if max_len <= MAX_SECTION_CHARS:
            return level, max_len          # ✓ dit niveau past
        if max_len < best_fallback[1]:
            best_fallback = (level, max_len)
    return best_fallback


def _samples_from_pattern(pattern: re.Pattern, text: str, body_offset: int = 0) -> list[str]:
    """Verzamel max MAX_SAMPLES_PER_CHECK voorbeelden van een regex-match (regel + voorbeeld)."""
    samples = []
    lines = text.split("\n")
    for line_idx, line in enumerate(lines, start=1):
        if pattern.search(line):
            samples.append(f"regel {line_idx + body_offset}: {line.strip()[:120]}")
            if len(samples) >= MAX_SAMPLES_PER_CHECK:
                break
    return samples


def _detect_long_blank_runs(body: str) -> tuple[int, list[str]]:
    """Tel langste run van opeenvolgende lege regels en geef voorbeelden."""
    longest = 0
    samples = []
    current = 0
    current_start = 0
    lines = body.split("\n")
    for idx, line in enumerate(lines, start=1):
        if line.strip() == "":
            if current == 0:
                current_start = idx
            current += 1
            longest = max(longest, current)
        else:
            if current > MAX_BLANK_RUN and len(samples) < MAX_SAMPLES_PER_CHECK:
                samples.append(f"regels {current_start}-{current_start + current - 1}: {current} lege regels")
            current = 0
    if current > MAX_BLANK_RUN and len(samples) < MAX_SAMPLES_PER_CHECK:
        samples.append(f"regels {current_start}-{current_start + current - 1}: {current} lege regels")
    return longest, samples


# ─── Checks ──────────────────────────────────────────────────────────────────

def check_frontmatter(bron_rol: str, frontmatter: Optional[str], body: str) -> CheckResult:
    if frontmatter is None:
        return CheckResult(
            name="frontmatter_present",
            status="fail",
            detail="Geen YAML-frontmatter aanwezig (`---\\n...\\n---`)",
        )
    required = REQUIRED_FRONTMATTER.get(bron_rol, set())
    if not required:
        return CheckResult(name="frontmatter_complete", status="pass", detail=f"bron-rol {bron_rol!r} zonder verplichte velden")

    # Eenvoudige check: zoek `<key>:` aan het begin van een regel binnen frontmatter
    present = {
        key for key in required
        if re.search(rf"(?m)^{re.escape(key)}\s*:", frontmatter)
    }
    missing = required - present
    if missing:
        return CheckResult(
            name="frontmatter_complete",
            status="fail",
            detail=f"ontbrekende velden: {sorted(missing)}",
        )
    return CheckResult(name="frontmatter_complete", status="pass")


def _parse_chunk_config(frontmatter: str) -> Optional[dict]:
    """Parse minimale `chunk:`-blok uit frontmatter zonder PyYAML-dependency.

    Verwacht structuur:
      chunk:
        level: <int>
        type: "<string>"
        sub_strategy: <null|string>

    Returnt dict met keys {level, type, sub_strategy} of None bij ontbreken.
    Onbekende of niet-parsebare waarden worden als raw string teruggegeven; de
    validator beoordeelt of ze geldig zijn.
    """
    m = re.search(r"(?m)^chunk\s*:\s*$", frontmatter)
    if not m:
        return None
    # Vang de geïndenteerde regels die volgen (begin met whitespace).
    tail = frontmatter[m.end():]
    block_lines = []
    for line in tail.split("\n"):
        if line.startswith((" ", "\t")):
            block_lines.append(line)
        elif line.strip() == "":
            block_lines.append(line)
        else:
            break
    cfg: dict = {}
    for line in block_lines:
        kv = re.match(r"^\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*:\s*(.*)$", line)
        if not kv:
            continue
        key, raw = kv.group(1), kv.group(2).strip()
        # Strip inline comments en quotes
        if raw.startswith('"') and raw.endswith('"') and len(raw) >= 2:
            value: object = raw[1:-1]
        elif raw.startswith("'") and raw.endswith("'") and len(raw) >= 2:
            value = raw[1:-1]
        elif raw == "" or raw.lower() in {"null", "~"}:
            value = None
        else:
            try:
                value = int(raw)
            except ValueError:
                value = raw
        cfg[key] = value
    return cfg


def check_chunk_config(frontmatter: Optional[str]) -> CheckResult:
    """Valideer `chunk:`-frontmatter (alleen actief in staging-mode)."""
    if frontmatter is None:
        return CheckResult(
            name="chunk_config_valid",
            status="fail",
            detail="chunk-config ontbreekt of incompleet (geen frontmatter)",
        )
    cfg = _parse_chunk_config(frontmatter)
    if cfg is None:
        return CheckResult(
            name="chunk_config_valid",
            status="fail",
            detail="chunk-config ontbreekt of incompleet (geen `chunk:`-blok)",
        )
    problems: list[str] = []
    level = cfg.get("level")
    if not isinstance(level, int) or not (2 <= level <= 6):
        problems.append(f"level moet int 2-6 zijn (kreeg: {level!r})")
    ctype = cfg.get("type")
    if not isinstance(ctype, str) or not ctype:
        problems.append(f"type moet niet-lege string zijn (kreeg: {ctype!r})")
    if "sub_strategy" not in cfg:
        problems.append("sub_strategy ontbreekt (mag null of string zijn)")
    else:
        sub = cfg["sub_strategy"]
        if sub is not None and not isinstance(sub, str):
            problems.append(f"sub_strategy moet null of string zijn (kreeg: {sub!r})")
    if problems:
        return CheckResult(
            name="chunk_config_valid",
            status="fail",
            detail="chunk-config ontbreekt of incompleet",
            samples=problems[:MAX_SAMPLES_PER_CHECK],
        )
    return CheckResult(
        name="chunk_config_valid",
        status="pass",
        detail=f"level={level}, type={ctype!r}, sub_strategy={cfg.get('sub_strategy')!r}",
    )


def check_provenance(path: Path) -> CheckResult:
    prov = read_provenance(path)
    if prov is None:
        return CheckResult(
            name="provenance_valid",
            status="fail",
            detail="provenance-blok ontbreekt (run add_provenance.py)",
        )
    if not prov.inputs:
        return CheckResult(
            name="provenance_valid",
            status="warn",
            detail="provenance.inputs is leeg",
        )
    if not prov.tooling.pipeline:
        return CheckResult(
            name="provenance_valid",
            status="warn",
            detail="provenance.tooling.pipeline ontbreekt",
        )
    return CheckResult(name="provenance_valid", status="pass")


def check_heading_structure(body: str, file_size: int) -> tuple[CheckResult, int]:
    """Returns (CheckResult, heading_count). file_size in chars (excl. frontmatter).

    Telt headings van niveau >= 2 (`##`, `###`, `####`, ...). Een bestand
    geldt als gestructureerd zodra er minstens één heading van eender welk
    diepteniveau is — chunkerstrategie kiest het juiste niveau separaat
    (zie `tools/etl/heading_stats.py`).
    """
    # Tel alle headings vanaf niveau 2 (## en dieper). H1 = doc-titel, niet
    # een sectiebegrenzer voor chunking.
    heading_count = len(re.findall(r"(?m)^#{2,6}\s+", body))
    if file_size >= HEADING_THRESHOLD_CHARS and heading_count == 0:
        return (
            CheckResult(
                name="heading_structure",
                status="warn",
                detail=f"bestand van {file_size} chars heeft 0 headings (## of dieper) → degraded chunking",
            ),
            heading_count,
        )
    return (
        CheckResult(
            name="heading_structure",
            status="pass",
            detail=f"{heading_count} headings (## of dieper)",
        ),
        heading_count,
    )


_SUB_BOUNDARY_QA_RE = re.compile(r"(?m)^\s*(?:\d+°|§\s*\d+)")


def check_max_section(
    body: str,
    heading_count: int,
    forced_level: Optional[int] = None,
    sub_strategy: Optional[str] = None,
) -> tuple[CheckResult, int]:
    """Beoordeel maximale sectiegrootte op het meest geschikte chunk-niveau.

    Gebruikt `_best_chunk_level_and_max()` om het diepste heading-niveau te vinden
    waarop de langste sectie ≤ 24K blijft. Zo vermijden we valse positieven voor
    adviezen die op ## groot zijn maar op ### / #### / ##### prima gesplitst kunnen
    worden.

    Wanneer `forced_level` is gegeven (uit chunk-config frontmatter), wordt de
    langste sectie op precies dat heading-niveau gemeten — geen auto-keuze. Dit is
    de staging-modus waar ETL de chunk-strategie expliciet vastlegt.

    Wanneer `sub_strategy == "per_definitieblok"` (ADR-006 §4.2): sub-grenzen
    (`1°`, `§ N`) worden meegenomen als virtuele extra grenzen na de
    heading-split. De RAG-chunker doet dat ook — qa_bron moet dezelfde lens
    gebruiken om geen valse FAILs te rapporteren.

    - FAIL: geen enkel niveau haalt ≤ 24K EN geen headings (één megachunk)
    - WARN: geen enkel niveau haalt ≤ 24K mét headings (structuur aanwezig maar te grof)
    - PASS: er is een niveau waarop de langste sectie ≤ 24K
    """
    def _max_with_sub_split(text: str) -> int:
        """Pas sub-boundary split toe en retourneer langste segment."""
        boundaries = [m.start() for m in _SUB_BOUNDARY_QA_RE.finditer(text)]
        if len(boundaries) < 3:
            return len(text)
        boundaries.append(len(text))
        last = 0
        # intro
        intro_len = boundaries[0] - last
        max_seg = intro_len
        for i in range(len(boundaries) - 1):
            seg_len = boundaries[i + 1] - boundaries[i]
            if seg_len > max_seg:
                max_seg = seg_len
        return max_seg

    if forced_level is not None and 2 <= forced_level <= 6:
        pattern = re.compile(rf"(?m)^#{{{forced_level}}}\s+.*$")
        parts = pattern.split(body)
        nonempty = [p for p in parts if p.strip()]
        if sub_strategy == "per_definitieblok" and nonempty:
            max_len_forced = max(_max_with_sub_split(p) for p in nonempty)
        else:
            max_len_forced = max((len(p) for p in nonempty), default=len(body))
        level, max_len = forced_level, max_len_forced
    else:
        level, max_len = _best_chunk_level_and_max(body)
        if sub_strategy == "per_definitieblok":
            # Pas sub-split ook toe op auto-detected level: meet niveau-X
            # secties opnieuw met sub-grens-splits.
            pattern = re.compile(rf"(?m)^#{{{level}}}\s+.*$")
            parts = [p for p in pattern.split(body) if p.strip()]
            if parts:
                max_len = max(_max_with_sub_split(p) for p in parts)
    hdr = "#" * level
    if max_len > MAX_SECTION_CHARS:
        if heading_count == 0:
            return (
                CheckResult(
                    name="max_section_size",
                    status="fail",
                    detail=f"langste sectie: {max_len} chars (>{MAX_SECTION_CHARS}) — geen heading-structuur aanwezig",
                ),
                max_len,
            )
        return (
            CheckResult(
                name="max_section_size",
                status="warn",
                detail=f"langste sectie op {hdr}-niveau: {max_len} chars (>{MAX_SECTION_CHARS}); "
                       f"chunker splitst auto op alinea-grenzen via split_long_chunk",
            ),
            max_len,
        )
    return (
        CheckResult(
            name="max_section_size",
            status="pass",
            detail=f"langste sectie op {hdr}-niveau: {max_len} chars",
        ),
        max_len,
    )


def check_no_form_feed(body: str) -> CheckResult:
    if _RE_FORM_FEED.search(body):
        count = len(_RE_FORM_FEED.findall(body))
        return CheckResult(
            name="no_form_feed",
            status="fail",
            detail=f"{count} \\x0c form-feed character(s) — PDF-paginascheiding niet opgekuist",
        )
    return CheckResult(name="no_form_feed", status="pass")


def check_no_toc_dots(body: str) -> CheckResult:
    matches = _RE_TOC_DOTS.findall(body)
    if matches:
        return CheckResult(
            name="no_toc_dots",
            status="warn",
            detail=f"{len(matches)} TOC-stippen-regel(s) gevonden",
            samples=[m[:80] for m in matches[:MAX_SAMPLES_PER_CHECK]],
        )
    return CheckResult(name="no_toc_dots", status="pass")


def check_no_page_footer(body: str) -> CheckResult:
    matches = _RE_PAGE_FOOTER.findall(body)
    if matches:
        return CheckResult(
            name="no_page_footer",
            status="warn",
            detail=f"{len(matches)} paginavoetregel(s) gevonden",
            samples=[m[:80] for m in matches[:MAX_SAMPLES_PER_CHECK]],
        )
    return CheckResult(name="no_page_footer", status="pass")


def check_no_long_blank_runs(body: str) -> CheckResult:
    longest, samples = _detect_long_blank_runs(body)
    if longest > MAX_BLANK_RUN:
        return CheckResult(
            name="no_long_blank_runs",
            status="warn",
            detail=f"langste run: {longest} lege regels (>{MAX_BLANK_RUN})",
            samples=samples,
        )
    return CheckResult(name="no_long_blank_runs", status="pass")


def check_no_column_bleed(body: str) -> CheckResult:
    # Skip regels die deel zijn van een tabel-context:
    # 1. Markdown-tabelrijen (regels die beginnen met `|`).
    # 2. Plain-text tabulair blok: een regel met een spatie-run van ≥10 die
    #    in een blok zit met ≥1 andere "tabulaire" regel binnen ±2 regels.
    #    Dit vangt 2-koloms TOC-headers ("Bijwerking ... Te vervangen pagina's")
    #    en pseudo-tabellen zonder pipes op, zonder echte krantenkolom-bleed
    #    (NL/FR door elkaar in lopende tekst) te missen.
    lines = body.split("\n")
    wide_gap = re.compile(r"\S\s{10,}\S")
    multi_gap = re.compile(r"\S\s{4,}\S.*?\S\s{4,}\S")
    # TOC-kop "Bijwerking ... Te vervangen pagina's" / "Vervangen pagina's"
    # uit WBTW-KB-bijwerkingsoverzichten — geen kolom-bleed.
    toc_bijwerking = re.compile(
        r"^\s*Bijwerking\b.*\b(Te\s+)?[Vv]ervangen\s+pagina"
    )

    def is_table_pipe(line: str) -> bool:
        return line.lstrip().startswith("|")

    def is_strong_tabular(line: str) -> bool:
        # Regel met spatie-run ≥10 = duidelijk twee-koloms layout.
        return bool(wide_gap.search(line))

    def is_weak_tabular(line: str) -> bool:
        # Regel met ≥2 spatie-runs van ≥4 spaties = tabulaire datarij
        # (bv. "Bijw. 01 / 01.01.2012     30.12.2011      Volledige uitgave").
        return bool(multi_gap.search(line))

    # Een regel is "in tabel-context" als:
    #   - het een markdown-pipe-regel is, OF
    #   - hijzelf "strong tabular" is (spatie-run ≥10) EN minstens één buur
    #     (±3 regels) ook tabulair is (pipe, strong of weak).
    # Weak-tabular alleen telt als buur, niet als trigger — voorkomt dat
    # gewone genummerde lijst-items (één enkele inspring + dubbele spatie)
    # als tabel doorgaan.
    in_table_context = [False] * len(lines)
    for i, line in enumerate(lines):
        if is_table_pipe(line) or toc_bijwerking.match(line):
            in_table_context[i] = True
            continue
        if not is_strong_tabular(line):
            continue
        for j in range(max(0, i - 3), min(len(lines), i + 4)):
            if j == i:
                continue
            neighbour = lines[j]
            if (
                is_table_pipe(neighbour)
                or is_strong_tabular(neighbour)
                or is_weak_tabular(neighbour)
            ):
                in_table_context[i] = True
                break

    filtered_body = "\n".join(
        line for i, line in enumerate(lines) if not in_table_context[i]
    )
    samples = _samples_from_pattern(_RE_COLUMN_BLEED, filtered_body)
    if samples:
        return CheckResult(
            name="no_column_bleed",
            status="warn",
            detail=f"{len(samples)} kolom-bleed-patroon/-en gevonden buiten tabellen (twee-kolom PDF-extractie?)",
            samples=samples,
        )
    return CheckResult(name="no_column_bleed", status="pass")


def check_no_ocr_flags(body: str) -> CheckResult:
    samples = _samples_from_pattern(_RE_OCR_LAB, body)
    if samples:
        return CheckResult(
            name="no_ocr_flags",
            status="warn",
            detail=f"{len(samples)} OCR-letterverwarring(en) gevonden (l/I)",
            samples=samples,
        )
    return CheckResult(name="no_ocr_flags", status="pass")


# ─── Pipeline ────────────────────────────────────────────────────────────────

def qa_one_bron(path: Path, staging: bool = False) -> BronReport:
    path = path.resolve()
    text = path.read_text(encoding="utf-8")
    frontmatter, body = _split_frontmatter(text)
    if staging:
        bron_rol = _bron_rol_from_staging(frontmatter)
    else:
        bron_rol = _bron_rol_from_path(path)

    checks: list[CheckResult] = []
    checks.append(check_frontmatter(bron_rol, frontmatter, body))
    checks.append(check_provenance(path))

    forced_level: Optional[int] = None
    sub_strategy: Optional[str] = None
    if staging:
        chunk_check = check_chunk_config(frontmatter)
        checks.append(chunk_check)
        cfg = _parse_chunk_config(frontmatter or "")
        if cfg and isinstance(cfg.get("level"), int):
            forced_level = cfg["level"]
        if cfg:
            sub = cfg.get("sub_strategy")
            if isinstance(sub, str) and sub:
                sub_strategy = sub

    heading_check, heading_count = check_heading_structure(body, len(body))
    checks.append(heading_check)

    section_check, max_section = check_max_section(
        body, heading_count, forced_level, sub_strategy=sub_strategy,
    )
    checks.append(section_check)

    checks.append(check_no_form_feed(body))
    checks.append(check_no_toc_dots(body))
    checks.append(check_no_page_footer(body))
    checks.append(check_no_long_blank_runs(body))
    checks.append(check_no_column_bleed(body))
    checks.append(check_no_ocr_flags(body))

    # Verdict-aggregatie: één fail → fail; één warn → warn; anders pass
    statuses = {c.status for c in checks}
    if "fail" in statuses:
        verdict = "fail"
    elif "warn" in statuses:
        verdict = "warn"
    else:
        verdict = "pass"

    try:
        bestand_rel = str(path.relative_to(ROOT))
    except ValueError:
        bestand_rel = str(path)
    return BronReport(
        bestand=bestand_rel,
        bron_rol=bron_rol,
        file_size_chars=len(body),
        heading_count=heading_count,
        max_section_chars=max_section,
        verdict=verdict,
        checks=checks,
    )


def iter_targets(file: Optional[Path], bron_rol: Optional[str], collection: Optional[str]) -> list[Path]:
    if file:
        return [file]
    if collection:
        if collection not in COLLECTION_TO_DIR:
            raise SystemExit(f"Onbekende collection: {collection!r}")
        dirs = [COLLECTION_TO_DIR[collection]]
    elif bron_rol:
        if bron_rol not in BRON_DIRS:
            raise SystemExit(f"Onbekende bron-rol: {bron_rol!r}")
        dirs = [BRON_DIRS[bron_rol]]
    else:
        dirs = list(BRON_DIRS.values())

    files: list[Path] = []
    for d in dirs:
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md")):
            if f.name in SKIP_FILES:
                continue
            files.append(f)
    return files


def iter_staging_targets(bron: Optional[str]) -> list[Path]:
    """Verzamel staging-MD's uit `data/etl/staging/`.

    Met `--bron NAAM` wordt op stem (filename zonder .md) gefilterd, hoofdletter-
    ongevoelig. Geen match → SystemExit.
    """
    if not STAGING_DIR.exists():
        raise SystemExit(f"Staging-map ontbreekt: {STAGING_DIR}")
    all_files = sorted(f for f in STAGING_DIR.glob("*.md") if f.name not in SKIP_FILES)
    if bron is None:
        return all_files
    needle = bron.lower()
    matches = [f for f in all_files if f.stem.lower() == needle]
    if not matches:
        # fallback: substring-match voor flexibiliteit
        matches = [f for f in all_files if needle in f.stem.lower()]
    if not matches:
        raise SystemExit(f"Geen staging-bestand gevonden voor --bron {bron!r}")
    return matches


def run_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


def _write_layer1_to_frontmatter(report: BronReport, run_id_str: str) -> bool:
    """Schrijf layer1-block naar provenance.trust.layer1 van de bron-MD.

    Returns True als de file gewijzigd werd. Idempotent (no-op als identiek).
    """
    import io
    from ruamel.yaml import YAML

    path = ROOT / report.bestand if not Path(report.bestand).is_absolute() else Path(report.bestand)
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return False

    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.indent(mapping=2, sequence=4, offset=2)
    yaml.width = 4096
    fm = yaml.load(m.group(1)) or {}
    body = text[m.end():]

    flags = []
    for c in report.checks:
        if c.status in ("warn", "fail"):
            flags.append({"name": c.name, "status": c.status,
                          "detail": c.detail, "samples": c.samples or []})

    # Nieuw schema (ADR-004 2026-05-11): layer1.status (niet .verdict), + run_at.
    # qa_bron.py raakt trust.status en trust.confirmed_by NIET aan — Laag 1
    # bevestigt nooit trust zelfstandig (zie ADR-005 §5, trust-derivation-regel).
    from datetime import datetime, timezone as _tz
    layer1 = {
        "status": report.verdict,   # pass | warn | fail
        "run_id": run_id_str,
        "run_at": datetime.now(_tz.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "heading_count": report.heading_count,
        "max_section_chars": report.max_section_chars,
        "file_size_chars": report.file_size_chars,
        "flags": flags,
    }

    prov = fm.setdefault("provenance", {})
    if not isinstance(prov, dict):
        return False
    trust = prov.get("trust")
    if not isinstance(trust, dict):
        trust = {}
        prov["trust"] = trust
    # Idempotentie: vergelijk zonder run_at (die verandert altijd).
    existing_l1 = trust.get("layer1") or {}
    existing_comparable = {k: v for k, v in existing_l1.items() if k != "run_at"}
    new_comparable = {k: v for k, v in layer1.items() if k != "run_at"}
    if existing_comparable == new_comparable:
        return False  # idempotent (zelfde resultaat, andere timestamp)
    trust["layer1"] = layer1

    buf = io.StringIO()
    yaml.dump(fm, buf)
    path.write_text(f"---\n{buf.getvalue()}---\n{body}", encoding="utf-8")
    return True


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--all", action="store_true", help="verwerk alle bronnen")
    p.add_argument("--bron-rol", choices=sorted(BRON_DIRS), help="beperk tot één bron-rol")
    p.add_argument("--collection", choices=sorted(COLLECTION_TO_DIR), help="beperk tot één collection")
    p.add_argument("--file", type=Path, help="één specifiek bestand")
    p.add_argument("--staging", action="store_true",
                   help="draai op data/etl/staging/ ipv resources/bronnen/")
    p.add_argument("--bron", type=str,
                   help="(met --staging) beperk tot één staging-bestand op filename-stem")
    p.add_argument("--report-only", action="store_true", help="alleen samenvatting; geen JSON-rapport schrijven")
    p.add_argument("--no-frontmatter", action="store_true",
                   help="schrijf layer1 NIET naar bron-frontmatter (default: wel schrijven)")
    p.add_argument("--no-json", action="store_true",
                   help="schrijf NIET naar data/etl/qa/qa-<rid>.json (frontmatter blijft primaire opslag)")
    p.add_argument("--output-dir", type=Path, default=ROOT / "data" / "qa",
                   help="map voor JSON-rapport (default: data/etl/qa/)")
    args = p.parse_args()

    if args.staging:
        if args.all or args.bron_rol or args.collection or args.file:
            p.error("--staging is niet combineerbaar met --all/--bron-rol/--collection/--file")
        targets = iter_staging_targets(args.bron)
    else:
        if args.bron:
            p.error("--bron werkt enkel met --staging")
        if not (args.all or args.bron_rol or args.collection or args.file):
            p.error("Specificeer --all, --bron-rol, --collection, --file of --staging")
        targets = iter_targets(args.file, args.bron_rol, args.collection)

    if not targets:
        print("Geen bestanden gevonden.")
        return

    mode_label = "staging" if args.staging else "resources"
    print(f"=== qa_bron [{mode_label}] — {len(targets)} bron(nen) ===")
    reports: list[BronReport] = []
    counters = {"pass": 0, "warn": 0, "fail": 0}
    rid = run_id()
    n_frontmatter_written = 0
    for path in targets:
        report = qa_one_bron(path, staging=args.staging)
        reports.append(report)
        counters[report.verdict] += 1
        if not args.no_frontmatter:
            try:
                if _write_layer1_to_frontmatter(report, rid):
                    n_frontmatter_written += 1
            except Exception as exc:
                print(f"  ! frontmatter-write faalde voor {report.bestand}: {exc}", file=sys.stderr)

    # Stdout-samenvatting
    print(f"\nVerdict-overzicht: pass={counters['pass']}  warn={counters['warn']}  fail={counters['fail']}")
    if not args.no_frontmatter:
        print(f"Layer1 in frontmatter geschreven: {n_frontmatter_written}/{len(targets)}")
    print()
    print("Bestanden met problemen (warn/fail):")
    for r in reports:
        if r.verdict == "pass":
            continue
        problems = [c for c in r.checks if c.status != "pass"]
        flags = ",".join(f"{c.status[0].upper()}:{c.name}" for c in problems)
        print(f"  [{r.verdict.upper():4s}] {r.bestand}  ({flags})")

    # JSON-rapport (legacy; frontmatter is nu de primaire opslag)
    if not args.report_only and not args.no_json:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        out_path = args.output_dir / f"qa-{rid}.json"
        rapport = {
            "run_id": rid,
            "scope": {
                "all": args.all,
                "bron_rol": args.bron_rol,
                "collection": args.collection,
                "file": str(args.file) if args.file else None,
                "staging": args.staging,
                "bron": args.bron,
            },
            "totals": counters,
            "bronnen": [asdict(r) for r in reports],
        }
        out_path.write_text(json.dumps(rapport, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nRapport: {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
