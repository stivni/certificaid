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
  python tools/etl/qa_bron.py --all                       # alle bronnen
  python tools/etl/qa_bron.py --bron-rol norm
  python tools/etl/qa_bron.py --collection cbn-adviezen
  python tools/etl/qa_bron.py --file resources/bronnen/normen/X.md
  python tools/etl/qa_bron.py --all --report-only        # alleen samenvatting

Output: `data/qa/<run-id>.json` + samenvatting op stdout.
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

COLLECTION_TO_DIR = {
    "wetteksten":   BRON_DIRS["wettekst"],
    "itaa-normen":  BRON_DIRS["norm"],
    "cbn-adviezen": BRON_DIRS["advies"],
}

SKIP_FILES = {"INDEX.md", "README.md", "WETTEKSTEN-INDEX.md"}

# Drempels (afgestemd op ADR-006 RAG-bovengrens van 24K per chunk)
HEADING_THRESHOLD_CHARS = 5000     # bestand >5K chars zonder ## → warn
MAX_SECTION_CHARS = 24_000          # langste sectie tussen ## > 24K → fail (mega-chunk)
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


def _split_frontmatter(text: str) -> tuple[Optional[str], str]:
    """Returns (frontmatter_yaml, body_text). Frontmatter is None als afwezig."""
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    return m.group(1), text[m.end():]


def _section_lengths(body: str) -> list[int]:
    """Splits body op `##` headings en returnt lengtes per sectie (in chars)."""
    parts = re.split(r"(?m)^##\s+.*$", body)
    return [len(p) for p in parts]


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
    """Returns (CheckResult, heading_count). file_size in chars (excl. frontmatter)."""
    heading_count = len(re.findall(r"(?m)^##\s+", body))
    if file_size >= HEADING_THRESHOLD_CHARS and heading_count == 0:
        return (
            CheckResult(
                name="heading_structure",
                status="warn",
                detail=f"bestand van {file_size} chars heeft 0 ##-headings → degraded chunking",
            ),
            heading_count,
        )
    return CheckResult(name="heading_structure", status="pass", detail=f"{heading_count} ## headings"), heading_count


def check_max_section(body: str, heading_count: int) -> tuple[CheckResult, int]:
    """Beoordeel maximale sectiegrootte tussen ## headings.

    - FAIL: max_section > 24K én géén ## headings (één megachunk, geen structuur)
    - WARN: max_section > 24K mét ## headings (chunker zal auto-splitsen op 8K-grenzen,
            maar minder semantische chunks dan ideaal)
    - PASS: max_section ≤ 24K
    """
    lengths = _section_lengths(body)
    max_len = max(lengths) if lengths else 0
    if max_len > MAX_SECTION_CHARS:
        if heading_count == 0:
            return (
                CheckResult(
                    name="max_section_size",
                    status="fail",
                    detail=f"langste sectie: {max_len} chars (>{MAX_SECTION_CHARS}) zonder enige ## structuur",
                ),
                max_len,
            )
        return (
            CheckResult(
                name="max_section_size",
                status="warn",
                detail=f"langste sectie: {max_len} chars (>{MAX_SECTION_CHARS}); "
                       f"chunker splitst auto op alinea-grenzen via split_long_chunk",
            ),
            max_len,
        )
    return CheckResult(name="max_section_size", status="pass", detail=f"langste sectie: {max_len} chars"), max_len


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
    samples = _samples_from_pattern(_RE_COLUMN_BLEED, body)
    if samples:
        return CheckResult(
            name="no_column_bleed",
            status="warn",
            detail=f"{len(samples)} kolom-bleed-patroon/-en gevonden (twee-kolom PDF-extractie?)",
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

def qa_one_bron(path: Path) -> BronReport:
    path = path.resolve()
    text = path.read_text(encoding="utf-8")
    frontmatter, body = _split_frontmatter(text)
    bron_rol = _bron_rol_from_path(path)

    checks: list[CheckResult] = []
    checks.append(check_frontmatter(bron_rol, frontmatter, body))
    checks.append(check_provenance(path))

    heading_check, heading_count = check_heading_structure(body, len(body))
    checks.append(heading_check)

    section_check, max_section = check_max_section(body, heading_count)
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

    return BronReport(
        bestand=str(path.relative_to(ROOT)),
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


def run_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--all", action="store_true", help="verwerk alle bronnen")
    p.add_argument("--bron-rol", choices=sorted(BRON_DIRS), help="beperk tot één bron-rol")
    p.add_argument("--collection", choices=sorted(COLLECTION_TO_DIR), help="beperk tot één collection")
    p.add_argument("--file", type=Path, help="één specifiek bestand")
    p.add_argument("--report-only", action="store_true", help="alleen samenvatting; geen JSON-rapport schrijven")
    p.add_argument("--output-dir", type=Path, default=ROOT / "data" / "qa",
                   help="map voor JSON-rapport (default: data/qa/)")
    args = p.parse_args()

    if not (args.all or args.bron_rol or args.collection or args.file):
        p.error("Specificeer --all, --bron-rol, --collection of --file")

    targets = iter_targets(args.file, args.bron_rol, args.collection)
    if not targets:
        print("Geen bestanden gevonden.")
        return

    print(f"=== qa_bron — {len(targets)} bron(nen) ===")
    reports: list[BronReport] = []
    counters = {"pass": 0, "warn": 0, "fail": 0}
    for path in targets:
        report = qa_one_bron(path)
        reports.append(report)
        counters[report.verdict] += 1

    # Stdout-samenvatting
    print(f"\nVerdict-overzicht: pass={counters['pass']}  warn={counters['warn']}  fail={counters['fail']}")
    print()
    print("Bestanden met problemen (warn/fail):")
    for r in reports:
        if r.verdict == "pass":
            continue
        problems = [c for c in r.checks if c.status != "pass"]
        flags = ",".join(f"{c.status[0].upper()}:{c.name}" for c in problems)
        print(f"  [{r.verdict.upper():4s}] {r.bestand}  ({flags})")

    # JSON-rapport
    if not args.report_only:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        rid = run_id()
        out_path = args.output_dir / f"qa-{rid}.json"
        rapport = {
            "run_id": rid,
            "scope": {
                "all": args.all,
                "bron_rol": args.bron_rol,
                "collection": args.collection,
                "file": str(args.file) if args.file else None,
            },
            "totals": counters,
            "bronnen": [asdict(r) for r in reports],
        }
        out_path.write_text(json.dumps(rapport, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nRapport: {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
