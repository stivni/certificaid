"""
In-process orchestrator voor de Certificaid bronnen-ETL (ADR-005 §2).

Pipeline per bron:
    extract → cleanup → headings → frontmatter → staging-output

De extract-stap delegeert naar `tools/lib/extractors/<method>.py` op basis van
`extract.method` in `resources/source_config.yaml`. Cleanup en
heading-injection zijn gedeeld (`tools/lib/cleanup.py`, `tools/lib/headings.py`).

Output landt in `data/etl-staging/<source_name>.md` — NIET in
`resources/bronnen/wetteksten/`. Dat blijft de huidige goedgekeurde set; staging
wordt door een latere fase (D) gepromoveerd.

Gebruik:
    python3 tools/etl/convert.py --list
    python3 tools/etl/convert.py --source WIB92
    python3 tools/etl/convert.py --source Wet-ITAA-2019 --diff
    python3 tools/etl/convert.py --all
    python3 tools/etl/convert.py --dry-run --source WIB92

Skipped methods: `handcrafted` (geen conversie nodig) en `derived` (compilatie
afgeleide MDs — fase B2 maakt deze obsolete).
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import textwrap
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIG_PATH = ROOT / "resources" / "source_config.yaml"
STAGING_DIR = ROOT / "data" / "etl-staging"

sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

from tools.lib.cleanup import run_pipeline, DEFAULT_STEPS  # noqa: E402
from tools.lib.headings import process_wettekst  # noqa: E402
from tools.lib.extractors import get_handler  # noqa: E402
from tools.lib.provenance import (  # noqa: E402
    Input,
    make_input,
    make_provenance,
    write_provenance,
    Trust,
    read_provenance,
)


# ─── Config laden ─────────────────────────────────────────────────────────────

def load_config() -> dict:
    with CONFIG_PATH.open() as f:
        return yaml.safe_load(f)["sources"]


def get_source(name: str, config: dict) -> dict:
    if name not in config:
        print(f"Bron '{name}' niet gevonden in source_config.yaml")
        print(f"  Beschikbaar: {', '.join(sorted(config))}")
        sys.exit(1)
    return config[name]


def resolve_method(cfg: dict) -> str:
    """Geef de extract-methode terug; valt terug op legacy `type:`."""
    extract = cfg.get("extract")
    if extract and "method" in extract:
        return extract["method"]
    return cfg.get("type", "")


# ─── Frontmatter ──────────────────────────────────────────────────────────────

_BRON_LABEL_PER_METHOD = {
    "pdftotext_ejustice": "ejustice.just.fgov.be (gecoördineerde versie)",
    "custom_wetboek": "Fisconetplus.be (officieuze gecoördineerde versie)",
    "custom_wib92": "Fisconet (officieuze gecoördineerde versie)",
    "justel_html": "www.ejustice.just.fgov.be (Justel, gecoördineerde versie)",
    "justel_bs_bilingual": "ejustice.just.fgov.be (B.S. originele publicatie — NL-kolom)",
}


def _format_tags(tags) -> str:
    """Render tags-lijst als geldige YAML flow-list met dubbele quotes."""
    if isinstance(tags, list):
        return "[" + ", ".join(f'"{t}"' for t in tags) + "]"
    return str(tags)


def _safe(value: str) -> str:
    """Escape dubbele quotes binnen YAML-strings."""
    if value is None:
        return ""
    return str(value).replace('"', '\\"')


def build_initial_frontmatter(cfg: dict, source_name: str, method: str) -> str:
    """Bouw de YAML-frontmatter + intro-paragraaf (vóór heading-injection).

    Het `chunk:`-blok wordt later bijgevoegd door `process_wettekst` op basis
    van de gedetecteerde structuurhiërarchie.
    """
    tags = cfg.get("tags", [])
    tags_str = _format_tags(tags)
    itaa = _safe(cfg.get("itaa_sectie", ""))
    wet_full = cfg.get("wet", source_name)
    titel = cfg.get("titel") or wet_full
    bijgewerkt = _safe(cfg.get("bijgewerkt", ""))
    bron_rol = cfg.get("bron_rol")
    bron_label = _BRON_LABEL_PER_METHOD.get(method, "onbekend")

    fm_lines = [
        "---",
        f"tags: {tags_str}",
        f'itaa-lex-sectie: "{itaa}"',
        f'wet: "{_safe(wet_full)}"',
    ]
    if bron_rol:
        fm_lines.append(f'bron_rol: "{_safe(bron_rol)}"')
    fm_lines.extend([
        'status: "beschikbaar"',
        f'bijgewerkt: "{bijgewerkt}"',
        f'bron: "{bron_label}"',
        "---",
        "",
        f"# {titel}",
        "",
        f"*Bijgewerkt tot en met {bijgewerkt} — gecoördineerde versie.*",
        "",
        "",
    ])
    return "\n".join(fm_lines)


# ─── Provenance ───────────────────────────────────────────────────────────────

def _resolve_inputs(cfg: dict, source_name: str, method: str) -> list[Input]:
    """Bouw de provenance.inputs-lijst voor deze bron.

    Voor PDF-gebaseerde methods: hash de raw PDF('s).
    Voor `justel_html`: gebruik de URL als id (geen sha).
    """
    inputs: list[Input] = []

    extract_cfg = cfg.get("extract") or {}
    params = extract_cfg.get("params") or {}
    raw = cfg.get("raw")
    raw_files = params.get("raw_files") or []

    if raw_files:
        for rf in raw_files:
            p = ROOT / rf
            if p.exists():
                inputs.append(make_input(p, version=cfg.get("bijgewerkt"), repo_root=ROOT))
    elif raw:
        p = ROOT / raw
        if p.exists():
            inputs.append(make_input(p, version=cfg.get("bijgewerkt"), repo_root=ROOT))

    if method == "justel_html":
        url = params.get("start_url") or cfg.get("source_url")
        if url:
            from tools.lib.provenance import make_url_input
            inputs.append(make_url_input(url, version=cfg.get("bijgewerkt")))

    return inputs


def _attach_provenance(staging_path: Path, cfg: dict, source_name: str,
                       method: str) -> None:
    """Schrijf het provenance-blok (incl. trust=unreviewed) in de staging-MD."""
    inputs = _resolve_inputs(cfg, source_name, method)
    prov = make_provenance(
        inputs=inputs,
        pipeline="tools/etl/convert.py",
        repo_root=ROOT,
    )
    prov.trust = Trust(status="unreviewed", confirmed_by="default")
    write_provenance(staging_path, prov)


# ─── Cleanup-stappenkeuze ─────────────────────────────────────────────────────

def _cleanup_steps_for(cfg: dict, method: str) -> list[str]:
    """Bepaal de cleanup-stappen voor deze bron.

    - pdftotext_ejustice: DEFAULT_STEPS + `cfg.cleanup` (bron-specifiek).
    - custom_wetboek/custom_wib92: extractor heeft al fix_broken_words +
      merge_wrapped_lines + merge_heading_continuations toegepast; we draaien
      enkel de niet-overlappende stappen plus eventuele bron-specifieke.
    - justel_html / justel_bs_bilingual: extractor levert al schone tekst;
      we beperken cleanup tot collapse_blank_lines.
    """
    if method == "pdftotext_ejustice":
        steps = list(DEFAULT_STEPS) + list(cfg.get("cleanup", []))
        return steps
    if method in ("custom_wetboek", "custom_wib92"):
        # Body is al grotendeels schoon; geen toc-removal of artefact-stripping
        # die het reeds geconverteerde markdown zou kunnen breken.
        return ["collapse_blank_lines"] + list(cfg.get("cleanup", []))
    if method in ("justel_html", "justel_bs_bilingual"):
        return ["collapse_blank_lines"]
    return list(DEFAULT_STEPS)


# ─── Diff-helper ──────────────────────────────────────────────────────────────

def _show_diff(left: Path, right: Path) -> None:
    if not left.exists() or not right.exists():
        print(f"  Diff niet mogelijk: ontbrekend bestand ({left.name} of {right.name})")
        return
    result = subprocess.run(
        ["git", "--no-pager", "diff", "--no-index", "--color=never",
         str(left), str(right)],
        cwd=ROOT,
    )
    if result.returncode == 0:
        print("  Geen verschillen.")


# ─── Kern-pipeline ────────────────────────────────────────────────────────────

def convert_one(source_name: str, *, dry_run: bool = False,
                show_diff: bool = False) -> Path | None:
    """Converteer één bron naar `data/etl-staging/<source_name>.md`."""
    config = load_config()
    cfg = get_source(source_name, config)
    method = resolve_method(cfg)
    status = cfg.get("status", "onbekend")

    print(f"\n{'='*60}")
    print(f"Bron: {source_name}  |  methode: {method}  |  status: {status}")

    if method in ("handcrafted", "skip"):
        print(f"  Skip — methode={method} (geen conversie nodig)")
        return None
    if method in ("derived", "split"):
        print(f"  Skip — methode={method} (afgeleide bron; fase B2 herziet dit)")
        return None

    handler = get_handler(method)
    if handler is None:
        print(f"  Geen handler voor extract.method={method!r}")
        return None

    # 1. Extract
    print(f"  → Extractie via lib.extractors.{method}")
    raw_text = handler(cfg, source_name)

    # 2. Cleanup op de body (frontmatter komt erna; preserve_frontmatter=False
    #    omdat we nog geen frontmatter hebben).
    steps = _cleanup_steps_for(cfg, method)
    if steps:
        print(f"  → Cleanup: {steps}")
        raw_text = run_pipeline(raw_text, steps=steps, preserve_frontmatter=False)

    # 3. Bouw frontmatter + intro-paragraaf + body. De intro (`# wet`-H1 en
    #    *Bijgewerkt tot* regel) staat nadrukkelijk NA cleanup, omdat ejustice-
    #    cleanup-stappen (bv. remove_toc_ejustice) de H1 anders zouden strippen.
    text = build_initial_frontmatter(cfg, source_name, method) + raw_text.lstrip("\n")

    # 4. Heading-injection + chunk-blok in frontmatter
    text, info = process_wettekst(text)
    print(
        f"  → Headings: ranks={info['ranks']} reduced={info['reduced_ranks']} "
        f"chunk.level={info['chunk_level']} conversies={info['n_conversies']}"
    )

    # 5. Schrijven naar staging
    staging_path = STAGING_DIR / f"{source_name}.md"
    def _display(p: Path) -> str:
        try:
            return str(p.relative_to(ROOT))
        except ValueError:
            return str(p)

    if not dry_run:
        STAGING_DIR.mkdir(parents=True, exist_ok=True)
        staging_path.write_text(text, encoding="utf-8")
        # Provenance-blok toevoegen
        _attach_provenance(staging_path, cfg, source_name, method)
        print(f"  ✓ Geschreven: {_display(staging_path)}")
    else:
        print(f"  (dry-run) {_display(staging_path)} — {len(text):,} tekens")

    if show_diff:
        original = ROOT / cfg.get("output", "")
        if cfg.get("output") and original.exists() and staging_path.exists():
            print(f"  Diff: {original.relative_to(ROOT)} ↔ staging")
            _show_diff(original, staging_path)

    return staging_path


# ─── CLI ──────────────────────────────────────────────────────────────────────

def cmd_list(config: dict, filter_method: str | None = None,
             filter_status: str | None = None) -> None:
    header = f"{'Naam':<45} {'Methode':<28} {'Status':<12}"
    print(header)
    print("─" * len(header))
    for name, cfg in config.items():
        method = resolve_method(cfg)
        s = cfg.get("status", "?")
        if filter_method and method != filter_method:
            continue
        if filter_status and s != filter_status:
            continue
        print(f"{name:<45} {method:<28} {s}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Certificaid bronnen-ETL — in-process orchestrator (ADR-005 §2)"
    )
    parser.add_argument("--source", help="Naam van de bron uit source_config.yaml")
    parser.add_argument("--all", action="store_true",
                        help="Alle bronnen behalve handcrafted/derived")
    parser.add_argument("--list", action="store_true", help="Toon overzicht")
    parser.add_argument("--diff", action="store_true",
                        help="Toon git-diff tussen huidige resources/bronnen en staging")
    parser.add_argument("--dry-run", action="store_true",
                        help="Pipeline draaien zonder naar staging te schrijven")
    parser.add_argument("--method", help="Filter --list op extract.method")
    parser.add_argument("--status", help="Filter --list op status")
    args = parser.parse_args()

    config = load_config()

    if args.list:
        cmd_list(config, filter_method=args.method, filter_status=args.status)
        return

    if args.source:
        convert_one(args.source, dry_run=args.dry_run, show_diff=args.diff)
        return

    if args.all:
        skipped = 0
        done = 0
        for name, cfg in config.items():
            method = resolve_method(cfg)
            if method in ("handcrafted", "skip", "derived", "split"):
                skipped += 1
                continue
            try:
                convert_one(name, dry_run=args.dry_run, show_diff=False)
                done += 1
            except Exception as e:
                print(f"  ERR: {name}: {e}")
        print(f"\n✓ Klaar: {done} verwerkt, {skipped} overgeslagen.")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
