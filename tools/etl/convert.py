"""
Unified conversie-pipeline voor Certificaid-bronnen.

Gebruik:
  python tools/etl/convert.py --list                          # overzicht alle bronnen
  python tools/etl/convert.py --source WIB92                 # converteer één bron
  python tools/etl/convert.py --source Antiwitwaswet-2017 --reindex
  python tools/etl/convert.py --type ejustice_nl              # alle bronnen van dit type
  python tools/etl/convert.py --type toc_only                 # alle bronnen die conversie nodig hebben
  python tools/etl/convert.py --cleanup-only --source WIB92  # alleen cleanup, geen herconversie
  python tools/etl/convert.py --diff --source WIB92          # toon diff na cleanup
"""

import argparse
import subprocess
import sys
import textwrap
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIG_PATH = ROOT / "resources" / "source_config.yaml"

sys.path.insert(0, str(ROOT / "tools"))
from lib.cleanup import run_pipeline, ALL_STEPS


# ---------------------------------------------------------------------------
# Config laden
# ---------------------------------------------------------------------------

def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)["sources"]


def get_source(name: str, config: dict) -> dict:
    if name not in config:
        print(f"❌ Bron '{name}' niet gevonden in source_config.yaml")
        print(f"   Beschikbaar: {', '.join(config)}")
        sys.exit(1)
    return config[name]


# ---------------------------------------------------------------------------
# PDF → tekst extractie
# ---------------------------------------------------------------------------

def pdftotext_nl(pdf_path: str, start_page: int = 1, end_page: int | None = None) -> str:
    """Extraheer NL-tekst uit een NL-only PDF met pdftotext -layout."""
    cmd = ["pdftotext", "-layout"]
    if start_page > 1:
        cmd += ["-f", str(start_page)]
    if end_page:
        cmd += ["-l", str(end_page)]
    cmd += [pdf_path, "-"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"pdftotext mislukt: {result.stderr}")
    return result.stdout


def pdftotext_bilingual(pdf_path: str, nl_col_x: int, start_page: int = 1,
                         end_page: int | None = None) -> str:
    """Extraheer enkel de NL-kolom uit een tweetalige PDF."""
    # Detect paginabreedte (standaard 595pt voor A4)
    col_w = 595 - nl_col_x - 10
    page_h = 842

    cmd = ["pdftotext", "-layout",
           "-x", str(nl_col_x), "-y", "0",
           "-W", str(col_w), "-H", str(page_h)]
    if start_page > 1:
        cmd += ["-f", str(start_page)]
    if end_page:
        cmd += ["-l", str(end_page)]
    cmd += [pdf_path, "-"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"pdftotext bilingual mislukt: {result.stderr}")
    return result.stdout


# ---------------------------------------------------------------------------
# Frontmatter genereren
# ---------------------------------------------------------------------------

def make_frontmatter(cfg: dict, source_name: str) -> str:
    tags = cfg.get("tags", [])
    tags_str = str(tags).replace("'", '"')
    itaa = cfg.get("itaa_sectie", "")
    wet = cfg.get("wet", source_name)
    bijgewerkt = cfg.get("bijgewerkt", "")
    return textwrap.dedent(f"""\
        ---
        tags: {tags_str}
        itaa-lex-sectie: "{itaa}"
        wet: "{wet}"
        status: "beschikbaar"
        bijgewerkt: "{bijgewerkt}"
        bron: "ejustice.just.fgov.be (gecoördineerde versie)"
        ---

        # {wet}

        *Bijgewerkt tot en met {bijgewerkt} — gecoördineerde versie.*

    """)


# ---------------------------------------------------------------------------
# Conversiemethoden
# ---------------------------------------------------------------------------

def convert_wib92(cfg: dict, source_name: str, dry_run: bool = False) -> str:
    """Delegeer naar het bestaande convert-wib92.py script."""
    script = ROOT / "tools" / "etl" / "convert-wib92.py"
    if not script.exists():
        raise FileNotFoundError(f"convert-wib92.py niet gevonden")
    print(f"  → Delegeer naar {script.name}")
    if not dry_run:
        result = subprocess.run(["python3", str(script)], capture_output=True, text=True, cwd=ROOT)
        if result.returncode != 0:
            print(f"  ⚠️  Waarschuwing: {result.stderr[:200]}")
    return cfg["output"]


def convert_wetboek(cfg: dict, source_name: str, dry_run: bool = False) -> str:
    """Delegeer naar convert-wetboek.py — die leest de YAML-entry zelf."""
    script = ROOT / "tools" / "etl" / "convert-wetboek.py"
    print(f"  → Delegeer naar {script.name} {source_name}")
    if not dry_run:
        result = subprocess.run(
            ["python3", str(script), source_name],
            capture_output=True, text=True, cwd=ROOT
        )
        if result.returncode != 0:
            print(f"  ⚠️  Waarschuwing: {result.stderr[:200]}")
    return cfg["output"]


def pdftotext_simple(pdf_path: str, start_page: int = 1,
                      end_page: int | None = None) -> str:
    """pdftotext zonder -layout: lineaire tekst, beter voor meerkolomsdocs."""
    cmd = ["pdftotext"]
    if start_page > 1:
        cmd += ["-f", str(start_page)]
    if end_page:
        cmd += ["-l", str(end_page)]
    cmd += [pdf_path, "-"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"pdftotext mislukt: {result.stderr}")
    return result.stdout


def convert_ejustice(cfg: dict, source_name: str, bilingual: bool = False,
                     dry_run: bool = False) -> str:
    """Converteer een ejustice PDF naar gestructureerde NL markdown."""
    raw = cfg.get("raw")
    if not raw:
        raise ValueError(f"raw-pad ontbreekt voor {source_name}")
    raw_path = ROOT / raw
    if not raw_path.exists():
        raise FileNotFoundError(f"Raw PDF niet gevonden: {raw_path}")

    output_path = ROOT / cfg["output"]
    start_page = cfg.get("start_page", 1)
    end_page = cfg.get("end_page")
    # EU-publicatieblad docs: gebruik simple mode voor betere kolomverwerking
    simple_mode = cfg.get("simple_mode", False)

    print(f"  → Extraheer tekst uit {raw_path.name}")
    if simple_mode:
        text = pdftotext_simple(str(raw_path), start_page, end_page)
    elif bilingual:
        nl_col_x = cfg.get("nl_col_x", 0)
        text = pdftotext_bilingual(str(raw_path), nl_col_x, start_page, end_page)
    else:
        text = pdftotext_nl(str(raw_path), start_page, end_page)

    # Cleanup-pipeline
    cleanup_steps = cfg.get("cleanup", [])
    print(f"  → Cleanup: standaard + {cleanup_steps}")
    text = run_pipeline(text, steps=None)          # standaard stappen
    text = run_pipeline(text, steps=cleanup_steps)  # bron-specifieke extra stappen

    # Frontmatter + artikel-headings
    text = make_frontmatter(cfg, source_name) + text

    if not dry_run:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(text)
        print(f"  ✓ Geschreven: {output_path.relative_to(ROOT)}")

    return str(output_path)


def cleanup_in_place(cfg: dict, source_name: str, dry_run: bool = False,
                     show_diff: bool = False) -> str:
    """Pas cleanup toe op een bestaand markdown-bestand (geen herconversie)."""
    output_path = ROOT / cfg["output"]
    if not output_path.exists():
        raise FileNotFoundError(f"Bestand niet gevonden: {output_path}")

    original = output_path.read_text()
    cleanup_steps = cfg.get("cleanup", [])
    # Standaard cleanup — zonder remove_toc (die verwijdert YAML frontmatter)
    safe_steps = ["remove_page_artifacts", "fix_broken_words",
                  "normalize_whitespace", "collapse_blank_lines",
                  "merge_wrapped_lines", "merge_heading_continuations"]
    cleaned = run_pipeline(original, steps=safe_steps + cleanup_steps)

    if show_diff:
        _show_diff(original, cleaned, output_path.name)

    if not dry_run and cleaned != original:
        output_path.write_text(cleaned)
        lines_before = original.count("\n")
        lines_after = cleaned.count("\n")
        print(f"  ✓ Opgeschoond: {output_path.name} ({lines_before}L → {lines_after}L)")
    elif cleaned == original:
        print(f"  ✓ Geen wijzigingen: {output_path.name}")

    return str(output_path)


def _show_diff(original: str, cleaned: str, name: str):
    import difflib
    diff = list(difflib.unified_diff(
        original.splitlines(keepends=True),
        cleaned.splitlines(keepends=True),
        fromfile=f"voor/{name}",
        tofile=f"na/{name}",
        n=3,
    ))
    if diff:
        print(f"\n{'─'*60}")
        print(f"DIFF: {name}")
        print(''.join(diff[:100]))  # max 100 diff-regels
        if len(diff) > 100:
            print(f"  ... ({len(diff) - 100} regels meer)")
    else:
        print(f"  Geen diff voor {name}")


# ---------------------------------------------------------------------------
# Re-index
# ---------------------------------------------------------------------------

def reindex(source_name: str, cfg: dict):
    """Voeg de geconverteerde bron toe aan de ChromaDB index."""
    script = ROOT / "tools" / "rag" / "rag_index.py"
    collection = _collection_for(cfg)
    print(f"  → Re-index in collection '{collection}'")
    result = subprocess.run(
        ["python3", str(script), "--collection", collection, "--source-file", cfg["output"]],
        capture_output=True, text=True, cwd=ROOT
    )
    if result.returncode != 0:
        print(f"  ⚠️  Re-index waarschuwing: {result.stderr[:200]}")
    else:
        print(f"  ✓ Re-indexed")


def _collection_for(cfg: dict) -> str:
    tags = cfg.get("tags", [])
    if any(t in tags for t in ["II", "VI.A", "VI.B", "VI.C", "IV.A", "VII", "VIII", "IX", "XV", "XIII", "XXI"]):
        return "wetteksten"
    return "wetteksten"


# ---------------------------------------------------------------------------
# Dispatcher
# ---------------------------------------------------------------------------

def process_source(name: str, cfg: dict, cleanup_only: bool = False,
                   dry_run: bool = False, show_diff: bool = False,
                   do_reindex: bool = False):
    source_type = cfg.get("type", "skip")
    status = cfg.get("status", "onbekend")

    print(f"\n{'='*60}")
    print(f"Bron: {name}  |  type: {source_type}  |  status: {status}")

    if source_type == "skip":
        print(f"  → Overgeslagen (type=skip)")
        if cleanup_only and cfg.get("output"):
            cleanup_in_place(cfg, name, dry_run, show_diff)
        return

    if source_type == "split":
        derived_from = cfg.get("derived_from", "?")
        print(f"  → Afgeleid uit '{derived_from}' (type=split). Re-genereer via "
              f"de bijbehorende splits-tool, niet via convert.py.")
        return

    try:
        if cleanup_only:
            cleanup_in_place(cfg, name, dry_run, show_diff)
        elif source_type == "wib92":
            convert_wib92(cfg, name, dry_run)
        elif source_type == "wetboek":
            convert_wetboek(cfg, name, dry_run)
        elif source_type == "ejustice_nl":
            convert_ejustice(cfg, name, bilingual=False, dry_run=dry_run)
        elif source_type == "ejustice_bilingual":
            convert_ejustice(cfg, name, bilingual=True, dry_run=dry_run)
        elif source_type == "raw_md":
            cleanup_in_place(cfg, name, dry_run, show_diff)
        else:
            print(f"  ⚠️  Onbekend type: {source_type}")
            return

        if do_reindex and not dry_run:
            reindex(name, cfg)

    except FileNotFoundError as e:
        print(f"  ❌ Bestand niet gevonden: {e}")
    except Exception as e:
        print(f"  ❌ Fout: {e}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def cmd_list(config: dict, filter_type: str | None = None,
             filter_status: str | None = None):
    """Toon overzicht van alle bronnen."""
    header = f"{'Naam':<45} {'Type':<22} {'Status':<12}"
    print(header)
    print("─" * len(header))
    for name, cfg in config.items():
        t = cfg.get("type", "?")
        s = cfg.get("status", "?")
        if filter_type and t != filter_type:
            continue
        if filter_status and s != filter_status:
            continue
        icon = "✅" if s == "volledig" else ("⚠️ " if s == "toc_only" else "❓")
        print(f"{name:<45} {t:<22} {icon} {s}")

    toc = sum(1 for c in config.values() if c.get("status") == "toc_only")
    volledig = sum(1 for c in config.values() if c.get("status") == "volledig")
    print(f"\n  Totaal: {len(config)} bronnen — {volledig} volledig, {toc} toc_only")


def main():
    parser = argparse.ArgumentParser(description="Certificaid bronnen conversie-pipeline")
    parser.add_argument("--source", help="Naam van de bron (uit source_config.yaml)")
    parser.add_argument("--type", help="Verwerk alle bronnen van dit type")
    parser.add_argument("--status", help="Filter op status (volledig|toc_only)")
    parser.add_argument("--list", action="store_true", help="Toon overzicht")
    parser.add_argument("--cleanup-only", action="store_true",
                        help="Alleen cleanup toepassen, niet herconverteren")
    parser.add_argument("--diff", action="store_true", help="Toon diff na cleanup")
    parser.add_argument("--dry-run", action="store_true",
                        help="Simuleer — schrijf niets naar schijf")
    parser.add_argument("--reindex", action="store_true",
                        help="Re-index in ChromaDB na conversie")
    args = parser.parse_args()

    config = load_config()

    if args.list:
        cmd_list(config, filter_type=args.type, filter_status=args.status)
        return

    # Selecteer bronnen
    if args.source:
        sources = {args.source: get_source(args.source, config)}
    elif args.type:
        # "toc_only" als type-alias voor status-filter
        if args.type == "toc_only":
            sources = {n: c for n, c in config.items() if c.get("status") == "toc_only"}
        else:
            sources = {n: c for n, c in config.items() if c.get("type") == args.type}
        if not sources:
            print(f"Geen bronnen gevonden voor type='{args.type}'")
            return
    else:
        parser.print_help()
        return

    for name, cfg in sources.items():
        process_source(
            name, cfg,
            cleanup_only=args.cleanup_only,
            dry_run=args.dry_run,
            show_diff=args.diff,
            do_reindex=args.reindex,
        )

    print(f"\n✓ Klaar ({len(sources)} bron(nen) verwerkt).")


if __name__ == "__main__":
    main()
