#!/usr/bin/env python3
"""
Heading-statistieken per bron — input voor chunking-beslissing.

Voor elke bron-MD: tel headings per niveau (h1..h6) en bereken sectie-lengte
statistiek (min/max/mean) per niveau. Dit geeft een data-gedreven indicatie
van op welk heading-niveau de chunker moet splitsen voor optimale RAG-chunks.

Heuristiek (richtlijn voor chunk-niveau):
  - Pas headings vanaf niveau 2 (`##`) komen in aanmerking als chunk-grenzen.
  - Het *aanbevolen* niveau is het diepste niveau waarbij:
      * minstens 2 headings voorkomen, EN
      * de gemiddelde sectielengte ≤ TARGET_CHUNK_CHARS (~6K, ADR-006), EN
      * de maximale sectielengte ≤ MAX_CHUNK_CHARS (24K)
  - Als geen niveau aan beide voldoet: het niveau met laagste max_section_chars.
  - Als bron < MIN_FILE_CHARS heeft: geen aanbeveling (te klein om over na te denken).

Dit tool muteert geen bestanden — het schrijft alleen een rapport.
Voor de chunker (rag_index.py) is de aanbeveling adviserend — die kan ook
gewoon altijd op `##` chunken (huidige default).

Gebruik:
    python tools/etl/heading_stats.py --all                    # alle bron-MDs
    python tools/etl/heading_stats.py --bron-rol advies        # alleen adviezen
    python tools/etl/heading_stats.py --file resources/bronnen/adviezen/X.md

Output: stdout (machine-leesbaar JSON via --json) + samenvatting per bron-rol.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from statistics import mean, median

ROOT = Path(__file__).resolve().parent.parent.parent

BRON_DIRS = {
    "wettekst": ROOT / "resources" / "bronnen" / "wetteksten",
    "norm":     ROOT / "resources" / "bronnen" / "normen",
    "advies":   ROOT / "resources" / "bronnen" / "adviezen",
}

SKIP_FILES = {"INDEX.md", "README.md", "WETTEKSTEN-INDEX.md"}

# Drempels (afgestemd op ADR-006)
TARGET_CHUNK_CHARS = 6_000      # ideaal — past binnen embedding-window
MAX_CHUNK_CHARS = 24_000        # bovengrens vóór auto-split
MIN_FILE_CHARS = 2_000          # < dit: geen aanbeveling nodig

_FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
_HEADING_RE = re.compile(r"(?m)^(#{1,6})\s+(.+)$")


# ─── Data types ───────────────────────────────────────────────────────────────

@dataclass
class LevelStats:
    level: int                   # 1..6
    count: int
    min_chars: int = 0
    max_chars: int = 0
    mean_chars: int = 0
    median_chars: int = 0


@dataclass
class BronHeadingReport:
    bestand: str
    file_size_chars: int
    levels: dict[int, LevelStats] = field(default_factory=dict)  # level → stats
    recommended_chunk_level: int | None = None
    recommended_reason: str = ""


# ─── Analysis ─────────────────────────────────────────────────────────────────

def split_frontmatter(text: str) -> tuple[str, str]:
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return "", text
    return text[: m.end()], text[m.end():]


def section_lengths_at_level(body: str, level: int) -> list[int]:
    """Lengtes van secties als de body op heading-niveau `level` wordt gesplitst.

    Bv. level=2 → splits op `## `. level=3 → splits op `### ` (en verder).
    Headings van *dezelfde of dieper* niveau gelden als grens; ondieper
    (= bovenliggend) niveau begrenst niet.
    """
    if level < 1 or level > 6:
        return [len(body)]
    pattern = re.compile(rf"(?m)^#{{{level}}}\s+.*$")
    parts = pattern.split(body)
    return [len(p) for p in parts]


def collect_heading_stats(body: str) -> dict[int, LevelStats]:
    """Voor elk heading-niveau dat in de body voorkomt: stats."""
    counts = {lv: 0 for lv in range(1, 7)}
    for m in _HEADING_RE.finditer(body):
        lv = len(m.group(1))
        counts[lv] += 1

    stats = {}
    for lv, count in counts.items():
        if count == 0:
            continue
        lengths = section_lengths_at_level(body, lv)
        # Skip de "voor-eerste-heading" sectie als die leeg/klein is
        nonempty = [l for l in lengths if l > 0]
        if not nonempty:
            stats[lv] = LevelStats(level=lv, count=count)
            continue
        stats[lv] = LevelStats(
            level=lv,
            count=count,
            min_chars=min(nonempty),
            max_chars=max(nonempty),
            mean_chars=int(mean(nonempty)),
            median_chars=int(median(nonempty)),
        )
    return stats


def recommend_chunk_level(
    file_size: int, stats: dict[int, LevelStats]
) -> tuple[int | None, str]:
    """Stel een chunk-heading-niveau voor.

    Voorkeur: het diepste niveau dat (a) minstens 2 headings heeft,
    (b) max_section <= MAX_CHUNK_CHARS, (c) mean_section <= TARGET_CHUNK_CHARS.
    """
    if file_size < MIN_FILE_CHARS:
        return None, f"bestand klein ({file_size} chars) — geen chunking nodig"

    # Filter alleen levels >= 2 (level 1 = doc-titel, geen chunk-grens)
    candidates = sorted(
        (s for lv, s in stats.items() if lv >= 2 and s.count >= 2),
        key=lambda s: s.level,
        reverse=True,  # diepste eerst
    )
    for s in candidates:
        if s.max_chars <= MAX_CHUNK_CHARS and s.mean_chars <= TARGET_CHUNK_CHARS:
            return s.level, (
                f"{s.count} headings op niveau {s.level}, "
                f"mean={s.mean_chars}, max={s.max_chars}"
            )

    # Fallback: niveau met laagste max_chars (=meest fijnmazig zonder mega-chunk)
    if candidates:
        best = min(candidates, key=lambda s: s.max_chars)
        return best.level, (
            f"fallback: niveau {best.level} heeft laagste max_section "
            f"({best.max_chars} chars), mean={best.mean_chars}"
        )

    # Geen enkel niveau met >= 2 headings
    return None, "geen heading-niveau heeft minstens 2 headings — niet chunkbaar"


def analyze_bron(path: Path) -> BronHeadingReport:
    text = path.read_text(encoding="utf-8")
    _, body = split_frontmatter(text)
    file_size = len(body)
    stats = collect_heading_stats(body)
    rec_level, reason = recommend_chunk_level(file_size, stats)
    # Relative-to-root als het kan, anders absolute (bv. test-bestanden in /tmp)
    try:
        bestand = str(path.relative_to(ROOT))
    except ValueError:
        bestand = str(path)
    return BronHeadingReport(
        bestand=bestand,
        file_size_chars=file_size,
        levels=stats,
        recommended_chunk_level=rec_level,
        recommended_reason=reason,
    )


# ─── Aggregaten over corpus ──────────────────────────────────────────────────

def aggregate_per_bron_rol(reports: list[BronHeadingReport]) -> dict:
    """Tel hoe vaak elk aanbevolen niveau voorkomt + level-distributie."""
    rec_counter: dict[str, int] = {}
    level_distribution: dict[int, int] = {lv: 0 for lv in range(1, 7)}
    no_recommendation = 0

    for r in reports:
        if r.recommended_chunk_level is None:
            no_recommendation += 1
        else:
            key = f"## (level 2)" if r.recommended_chunk_level == 2 else f"### (level {r.recommended_chunk_level})"
            key = f"level-{r.recommended_chunk_level}"
            rec_counter[key] = rec_counter.get(key, 0) + 1
        for lv in r.levels:
            level_distribution[lv] += r.levels[lv].count

    return {
        "n_bronnen": len(reports),
        "recommended_distribution": dict(sorted(rec_counter.items())),
        "no_recommendation": no_recommendation,
        "heading_count_per_level": level_distribution,
    }


# ─── CLI ─────────────────────────────────────────────────────────────────────

def gather_targets(args) -> list[Path]:
    if args.file:
        return [Path(args.file).resolve()]
    if args.bron_rol:
        d = BRON_DIRS[args.bron_rol]
        return sorted(p for p in d.glob("*.md") if p.name not in SKIP_FILES)
    targets: list[Path] = []
    for d in BRON_DIRS.values():
        targets.extend(p for p in d.glob("*.md") if p.name not in SKIP_FILES)
    return sorted(targets)


def main():
    p = argparse.ArgumentParser(description="Heading-statistieken per bron-MD.")
    p.add_argument("--bron-rol", choices=list(BRON_DIRS), help="Beperk tot één bron-rol")
    p.add_argument("--file", help="Specifiek pad")
    p.add_argument("--all", action="store_true", help="Alle bronnen (default als niets anders)")
    p.add_argument("--json", action="store_true", help="Output volledige JSON-rapport (anders samenvatting)")
    p.add_argument("--show-per-bron", action="store_true", help="Toon stats per bron in samenvatting")
    args = p.parse_args()

    if not (args.file or args.bron_rol or args.all):
        args.all = True

    targets = gather_targets(args)
    if not targets:
        print("Geen bestanden gevonden.", file=sys.stderr)
        sys.exit(1)

    reports = [analyze_bron(p) for p in targets]

    if args.json:
        out = {
            "n_bronnen": len(reports),
            "bronnen": [
                {
                    "bestand": r.bestand,
                    "file_size_chars": r.file_size_chars,
                    "levels": {str(lv): asdict(s) for lv, s in r.levels.items()},
                    "recommended_chunk_level": r.recommended_chunk_level,
                    "recommended_reason": r.recommended_reason,
                }
                for r in reports
            ],
            "aggregate": aggregate_per_bron_rol(reports),
        }
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return

    # Tekst-samenvatting
    agg = aggregate_per_bron_rol(reports)
    print(f"Heading-statistieken — {agg['n_bronnen']} bronnen geanalyseerd\n")
    print("Headings per niveau (totaal over alle bronnen):")
    for lv in sorted(agg["heading_count_per_level"]):
        cnt = agg["heading_count_per_level"][lv]
        if cnt:
            print(f"  H{lv}: {cnt}")
    print()
    print("Aanbevolen chunk-niveau (verdeling):")
    for lv, cnt in agg["recommended_distribution"].items():
        print(f"  {lv}: {cnt}")
    if agg["no_recommendation"]:
        print(f"  geen aanbeveling: {agg['no_recommendation']} (te klein of geen structuur)")

    if args.show_per_bron:
        print(f"\n{'─' * 60}\nPer bron:\n")
        for r in reports[:50]:
            level_summary = ", ".join(
                f"H{lv}={s.count}" for lv, s in sorted(r.levels.items())
            ) or "(geen)"
            rec = (
                f"→ chunk op H{r.recommended_chunk_level}"
                if r.recommended_chunk_level else "→ (geen aanbeveling)"
            )
            print(f"  {r.bestand}")
            print(f"     {r.file_size_chars} chars · {level_summary}  {rec}")


if __name__ == "__main__":
    main()
