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
from tools.lib.extractors import get_handler, COMPILATIE_METHODS, METHOD_HANDLERS  # noqa: E402
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


def load_collections() -> dict:
    """Lees de `collections:`-sectie uit source_config.yaml.

    Geeft een lege dict terug als de sectie ontbreekt.
    """
    with CONFIG_PATH.open() as f:
        data = yaml.safe_load(f) or {}
    return data.get("collections") or {}


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


def _get_sub_strategy(cfg: dict) -> str | None:
    """Lees `extract.params.sub_strategy` (ADR-006 §4.2) of None.

    Wordt doorgegeven aan `process_wettekst` zodat het chunk-blok in de
    staging-frontmatter correct geschreven wordt.
    """
    extract = cfg.get("extract") or {}
    params = extract.get("params") or {}
    val = params.get("sub_strategy")
    return val if isinstance(val, str) and val else None


# ─── Frontmatter ──────────────────────────────────────────────────────────────

_BRON_LABEL_PER_METHOD = {
    "pdftotext_ejustice": "ejustice.just.fgov.be (gecoördineerde versie)",
    "custom_wetboek": "Fisconetplus.be (officieuze gecoördineerde versie)",
    "custom_wib92": "Fisconet (officieuze gecoördineerde versie)",
    "justel_html": "www.ejustice.just.fgov.be (Justel, gecoördineerde versie)",
    "justel_change_lg": "www.ejustice.just.fgov.be (Justel change_lg.pl, legacy HTML — gecoördineerde versie)",
    "justel_bs_bilingual": "ejustice.just.fgov.be (B.S. originele publicatie — NL-kolom)",
    "pdftotext_compilatie_btw": "Afgesplitst uit Fisconet-compilatie (pdftotext_compilatie_btw)",
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


def build_initial_frontmatter(cfg: dict, source_name: str, method: str,
                              overrides: dict | None = None) -> str:
    """Bouw de YAML-frontmatter + intro-paragraaf (vóór heading-injection).

    Het `chunk:`-blok wordt later bijgevoegd door `process_wettekst` op basis
    van de gedetecteerde structuurhiërarchie.

    `overrides` laat een caller (bv. de compilatie-loop in convert_one) toe
    om split-specifieke velden zoals ``wet``, ``tags`` en ``bijgewerkt`` te
    forceren bovenop wat in cfg staat. Veld-namen volgen de cfg-keys.
    """
    overrides = overrides or {}

    def _pick(key, default=None):
        if key in overrides:
            return overrides[key]
        return cfg.get(key, default)

    tags = _pick("tags", [])
    tags_str = _format_tags(tags)
    itaa = _safe(_pick("itaa_sectie", ""))
    wet_full = _pick("wet", source_name)
    titel = _pick("titel") or wet_full
    bijgewerkt = _safe(_pick("bijgewerkt", ""))
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
    if method == "pymupdf_wetboek":
        # Extractor levert al schone output (headings + noise-filter + col-detect).
        # Alleen blank-line collapse + eventuele bron-specifieke stappen.
        return ["collapse_blank_lines"] + list(cfg.get("cleanup", []))
    if method in ("custom_wetboek", "custom_wib92"):
        # Body is al grotendeels schoon; geen toc-removal of artefact-stripping
        # die het reeds geconverteerde markdown zou kunnen breken.
        return ["collapse_blank_lines"] + list(cfg.get("cleanup", []))
    if method in ("justel_html", "justel_change_lg", "justel_bs_bilingual"):
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

    def _display(p: Path) -> str:
        try:
            return str(p.relative_to(ROOT))
        except ValueError:
            return str(p)

    # 1. Extract
    print(f"  → Extractie via lib.extractors.{method}")
    extracted = handler(cfg, source_name)

    # ─── 1-op-N pad: compilatie-handler retourneert dict ──────────────────
    if method in COMPILATIE_METHODS or isinstance(extracted, dict):
        if not isinstance(extracted, dict):
            raise TypeError(
                f"Handler {method!r} verwacht dict, kreeg {type(extracted).__name__}"
            )
        splits_meta = {s["output"]: s for s in (cfg.get("splits") or [])}
        print(f"  → Compilatie-mode: {len(extracted)} splits")
        last_path: Path | None = None
        for output_rel, body in extracted.items():
            split_meta = splits_meta.get(output_rel, {})
            basename = Path(output_rel).stem
            staging_path = STAGING_DIR / f"{basename}.md"

            if not body.strip():
                print(f"    ⚠️  {basename}: lege body — split overgeslagen")
                continue

            # Frontmatter-overrides per split (wet, tags, ...).
            overrides: dict = {}
            for k in ("wet", "tags", "itaa_sectie", "bijgewerkt", "titel"):
                if k in split_meta:
                    overrides[k] = split_meta[k]
                elif "extra_metadata" in split_meta and k in split_meta["extra_metadata"]:
                    overrides[k] = split_meta["extra_metadata"][k]

            text = build_initial_frontmatter(
                cfg, source_name, method, overrides=overrides,
            ) + body.lstrip("\n")
            # ADR-006 §4.2: split-niveau sub_strategy override (bv. WBTW-KB22
            # binnen WBTW-KBs) of bron-niveau extract.params.sub_strategy
            split_sub = (split_meta or {}).get("sub_strategy")
            sub_strategy = split_sub or _get_sub_strategy(cfg)
            text, info = process_wettekst(text, sub_strategy=sub_strategy)

            if not dry_run:
                STAGING_DIR.mkdir(parents=True, exist_ok=True)
                staging_path.write_text(text, encoding="utf-8")
                _attach_provenance(staging_path, cfg, source_name, method)
                print(
                    f"    ✓ {basename}  ranks={info['ranks']} "
                    f"reduced={info['reduced_ranks']} "
                    f"chunk.level={info['chunk_level']}"
                )
            else:
                print(f"    (dry-run) {basename} — {len(text):,} tekens")
            last_path = staging_path

        return last_path

    # ─── 1-op-1 pad: handler retourneert string ───────────────────────────
    raw_text = extracted

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
    sub_strategy = _get_sub_strategy(cfg)
    text, info = process_wettekst(text, sub_strategy=sub_strategy)
    print(
        f"  → Headings: ranks={info['ranks']} reduced={info['reduced_ranks']} "
        f"chunk.level={info['chunk_level']} conversies={info['n_conversies']}"
    )

    # 5. Schrijven naar staging
    staging_path = STAGING_DIR / f"{source_name}.md"

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


# ─── Collection-pipeline (CBN-adviezen, ITAA-normen) ─────────────────────────

# Mapping van collection-naam naar de extract-method-key in METHOD_HANDLERS.
_COLLECTION_METHOD = {
    "cbn-adviezen": "cbn_advies",
    "itaa-normen": "extract_norm",
}

# Per-collection cleanup en chunk-config. Beide collections chunken op H2.
# De CBN-scraper levert al schone markdown — alleen collapse_blank_lines.
# Norm-extractie levert ook schone markdown (na fix_norm_artefacts) — idem.
_COLLECTION_CLEANUP = {
    "cbn-adviezen": ["collapse_blank_lines"],
    "itaa-normen": ["collapse_blank_lines"],
}

_COLLECTION_CHUNK = {
    "cbn-adviezen": {"level": 2, "type": "##", "sub_strategy": None},
    "itaa-normen": {"level": 2, "type": "##", "sub_strategy": None},
}


def _read_frontmatter_md(md_path: Path) -> tuple[dict, str]:
    """Lees frontmatter (als plain dict) + body uit een bestaande MD.

    Geeft ``({}, full_text)`` terug als geen frontmatter aanwezig is.
    """
    from ruamel.yaml import YAML
    text = md_path.read_text(encoding="utf-8")
    import re
    m = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", text, re.DOTALL)
    if not m:
        return {}, text
    yaml_loader = YAML()
    yaml_loader.preserve_quotes = True
    data = yaml_loader.load(m.group(1)) or {}
    # Convert ruamel CommentedMap → plain dict
    from tools.lib.provenance import _to_plain  # noqa: PLC0415
    return _to_plain(data), text[m.end():]


def _build_collection_frontmatter(
    existing_fm: dict,
    *,
    chunk_cfg: dict,
    bron_rol: str | None,
    titel: str | None,
) -> str:
    """Bouw nieuwe frontmatter voor een collection-item.

    Behoudt alle bestaande frontmatter-velden (bron, datum, themas, …),
    voegt of overschrijft `chunk:` en `bron_rol`. De `provenance:` sleutel
    wordt verwijderd zodat de orchestrator hem nadien opnieuw kan toevoegen
    via `_attach_provenance` (anders dubbele blokken).
    """
    import io
    from ruamel.yaml import YAML
    yaml_dumper = YAML()
    yaml_dumper.preserve_quotes = True
    yaml_dumper.indent(mapping=2, sequence=4, offset=2)
    yaml_dumper.width = 4096

    # Werk op een kopie zodat we niet de origineel wijzigen.
    fm = dict(existing_fm)

    # Verwijder provenance — wordt door _attach_provenance opnieuw geschreven.
    fm.pop("provenance", None)

    # bron_rol toevoegen indien nog niet aanwezig (collection-default).
    if bron_rol and "bron_rol" not in fm:
        fm["bron_rol"] = bron_rol

    # Chunk-config — overschrijven, dit wordt door de pipeline bepaald.
    fm["chunk"] = dict(chunk_cfg)

    buf = io.StringIO()
    yaml_dumper.dump(fm, buf)
    return f"---\n{buf.getvalue()}---\n"


def _resolve_collection_inputs(item_cfg: dict, item_inputs_spec: list[dict]) -> list[Input]:
    """Bouw provenance.inputs voor één collection-item op basis van item_inputs-spec."""
    from tools.lib.provenance import make_url_input
    inputs: list[Input] = []
    for spec in item_inputs_spec or []:
        field = spec.get("field")
        kind = spec.get("kind")
        value = item_cfg.get(field)
        if not value:
            continue
        if kind == "local":
            p = Path(value)
            if not p.is_absolute():
                p = ROOT / value
            if p.exists():
                inputs.append(make_input(p, repo_root=ROOT))
        elif kind == "url":
            inputs.append(make_url_input(str(value)))
    return inputs


def _attach_collection_provenance(
    staging_path: Path, item_cfg: dict, item_inputs_spec: list[dict],
) -> None:
    """Schrijf provenance-blok voor een collection-item."""
    inputs = _resolve_collection_inputs(item_cfg, item_inputs_spec)
    prov = make_provenance(
        inputs=inputs,
        pipeline="tools/etl/convert.py",
        repo_root=ROOT,
    )
    prov.trust = Trust(status="unreviewed", confirmed_by="default")
    write_provenance(staging_path, prov)


def convert_collection_item(
    md_path: Path, collection_name: str, collection_cfg: dict,
    *, dry_run: bool = False,
) -> Path | None:
    """Verwerk één item uit een collection.

    Leest de bestaande MD-frontmatter, dispatcht naar de juiste extractor,
    cleant de body, bouwt een nieuwe frontmatter en schrijft naar
    `data/etl-staging/<source_name>.md`. Skipt (returnt None) bij een
    item-failure i.p.v. te falen — de orchestrator-loop blijft draaien.
    """
    source_name = md_path.stem
    method_key = _COLLECTION_METHOD.get(collection_name)
    if method_key is None:
        print(f"  ⚠️  Onbekende collection: {collection_name}")
        return None

    # 1. Lees bestaande frontmatter (= item-cfg)
    try:
        existing_fm, _existing_body = _read_frontmatter_md(md_path)
    except Exception as e:  # noqa: BLE001
        print(f"  ⚠️  {source_name}: kon frontmatter niet lezen ({e}) — skip")
        return None

    # INDEX.md en andere niet-item bestanden: skip
    if not existing_fm:
        print(f"  · {source_name}: geen frontmatter — skip")
        return None

    # 2. Extract via handler
    handler = METHOD_HANDLERS.get(method_key)
    if handler is None:
        print(f"  ⚠️  Geen handler voor method={method_key!r}")
        return None

    try:
        body = handler(existing_fm, source_name)
    except NotImplementedError as e:
        print(f"  · {source_name}: {e}")
        return None
    except FileNotFoundError as e:
        print(f"  · {source_name}: {e}")
        return None
    except Exception as e:  # noqa: BLE001
        print(f"  ⚠️  {source_name}: extractie mislukt ({type(e).__name__}: {e}) — skip")
        return None

    if not isinstance(body, str) or not body.strip():
        print(f"  ⚠️  {source_name}: lege body — skip")
        return None

    # 3. Cleanup
    cleanup_steps = _COLLECTION_CLEANUP.get(collection_name, [])
    if cleanup_steps:
        body = run_pipeline(body, steps=cleanup_steps, preserve_frontmatter=False)

    # 4. Bouw nieuwe frontmatter (KEEP bestaande velden, ADD chunk + bron_rol)
    chunk_cfg = _COLLECTION_CHUNK.get(collection_name, {"level": 2, "type": "##"})
    new_fm = _build_collection_frontmatter(
        existing_fm,
        chunk_cfg=chunk_cfg,
        bron_rol=collection_cfg.get("bron_rol"),
        titel=None,
    )

    text = new_fm + body.lstrip("\n")
    if not text.endswith("\n"):
        text += "\n"

    # 5. Schrijf naar staging
    staging_path = STAGING_DIR / f"{source_name}.md"
    if dry_run:
        print(f"  (dry-run) {source_name} — {len(text):,} tekens")
        return staging_path

    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    staging_path.write_text(text, encoding="utf-8")

    # 6. Provenance toevoegen
    item_inputs_spec = collection_cfg.get("item_inputs") or []
    try:
        _attach_collection_provenance(staging_path, existing_fm, item_inputs_spec)
    except Exception as e:  # noqa: BLE001
        print(f"  ⚠️  {source_name}: provenance-blok niet toegevoegd ({e})")

    print(f"  ✓ {source_name}")
    return staging_path


def convert_collection(
    name: str,
    *,
    dry_run: bool = False,
    limit: int | None = None,
) -> int:
    """Verwerk alle items uit een collection.

    Returnt het aantal succesvol geschreven items. `limit` beperkt de batch
    voor smoketests.
    """
    collections = load_collections()
    if name not in collections:
        print(f"Collection '{name}' niet gevonden in source_config.yaml")
        print(f"  Beschikbaar: {', '.join(sorted(collections))}")
        return 0

    cfg = collections[name]
    output_dir = ROOT / cfg["output_dir"]
    if not output_dir.exists():
        print(f"Output-dir bestaat niet: {output_dir}")
        return 0

    md_paths = sorted(output_dir.glob("*.md"))
    # Skip INDEX.md
    md_paths = [p for p in md_paths if p.name != "INDEX.md"]

    if limit is not None:
        md_paths = md_paths[:limit]

    print(f"\n{'='*60}")
    print(f"Collection: {name}  |  items: {len(md_paths)}  |  staging: data/etl-staging/")
    print("=" * 60)

    done = 0
    for md_path in md_paths:
        out = convert_collection_item(md_path, name, cfg, dry_run=dry_run)
        if out is not None:
            done += 1

    print(f"\n✓ Klaar: {done}/{len(md_paths)} items verwerkt.")
    return done


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
    parser.add_argument("--collection",
                        help="Naam van een collection (bv. cbn-adviezen, itaa-normen)")
    parser.add_argument("--limit", type=int, default=None,
                        help="Beperk --collection tot de eerste N items (smoketest)")
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

    if args.collection:
        convert_collection(
            args.collection, dry_run=args.dry_run, limit=args.limit,
        )
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
