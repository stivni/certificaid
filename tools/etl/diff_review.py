#!/usr/bin/env python3
"""
Laag 1.5 van de bronnen-QA-gate (ADR-005 §5): regressie-diff tussen staging-MD
en HEAD-versie van de bron, beoordeeld door een Claude Code subagent.

Dit script roept de Anthropic API NIET rechtstreeks aan (CLAUDE.md regel 3 —
geen API-calls in build-pipeline). De flow is mens-gemedieerd:

  1. ``--print-prompt`` genereert een markdown-rapport met git-diffs en
     instructies voor een Sonnet-subagent.
  2. De mens kopieert het rapport in een Claude Code Task-aanroep.
  3. De subagent retourneert verdicts (JSON, één blok per bestand).
  4. ``--apply-verdicts <verdict-bestand>`` valideert die verdicts en
     schrijft ze naar `data/qa/<run-id>-diff-verdicts.json` in canonical
     format.

Bronnen zonder HEAD-versie (nieuwe bronnen die nog niet in git zitten)
krijgen automatisch verdict ``no_op`` — geen subagent-call nodig.

Gebruik:

  # Modus 1: prompt-bundle voor subagent genereren
  python tools/etl/diff_review.py --staging-dir data/etl-staging \\
      --out data/qa/<run-id>-diff-prompt.md

  python tools/etl/diff_review.py --bron Wet-ITAA-2019 \\
      --out data/qa/<run-id>-diff-prompt.md

  # Modus 2: subagent-output omzetten naar canonical verdict-bestand
  python tools/etl/diff_review.py --apply-verdicts <verdict-bestand> \\
      --out data/qa/<run-id>-diff-verdicts.json

Idempotentie: een tweede run met dezelfde input (zelfde staging-MDs en
zelfde HEAD-versie) produceert identieke output, modulo ``run_id`` dat
de mens expliciet via ``--run-id`` kan vastpinnen.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIG_PATH = ROOT / "resources" / "source_config.yaml"
DEFAULT_STAGING_DIR = ROOT / "data" / "etl-staging"
DEFAULT_OUTPUT_DIR = ROOT / "data" / "qa"

VALID_VERDICTS = {"improvement", "regression", "structural_change", "no_op"}


# ─── Helpers ─────────────────────────────────────────────────────────────────

def run_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


def load_config() -> dict:
    with CONFIG_PATH.open() as f:
        return yaml.safe_load(f).get("sources", {})


def staging_to_head_path(staging_md: Path, config: dict) -> Optional[Path]:
    """Map een staging-MD-bestand naar zijn HEAD-equivalent in resources/bronnen/.

    Lookup-strategie:
      1. Zoek in source_config.yaml naar een bron waarvan ``output:`` op de
         staging-bestandsnaam eindigt (zonder map-prefix).
      2. Idem voor ``splits[*].output:``.
      3. Fallback: hetzelfde pad onder resources/bronnen/wetteksten/.

    Geeft None terug als geen mapping gevonden — caller behandelt dit als
    "nieuwe bron".
    """
    name = staging_md.name
    for source_name, cfg in config.items():
        out = cfg.get("output")
        if out and Path(out).name == name:
            return ROOT / out
        for split in cfg.get("splits", []) or []:
            split_out = split.get("output")
            if split_out and Path(split_out).name == name:
                return ROOT / split_out
    fallback = ROOT / "resources" / "bronnen" / "wetteksten" / name
    if fallback.exists():
        return fallback
    return None


def git_diff(head_path: Path, staging_path: Path) -> str:
    """Genereer git-diff tussen HEAD-versie en staging-MD.

    Gebruikt ``git diff --no-index`` zodat de staging-MD niet gestaged hoeft te
    zijn. Returnt lege string als bestanden identiek zijn.
    """
    try:
        result = subprocess.run(
            [
                "git", "diff", "--no-index", "--no-color",
                str(head_path), str(staging_path),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        # ``git diff --no-index`` exit-code: 0 = identiek, 1 = verschillen, >1 = error
        if result.returncode > 1:
            raise RuntimeError(f"git diff fout: {result.stderr.strip()}")
        return result.stdout
    except FileNotFoundError as e:
        raise RuntimeError("git niet gevonden in PATH") from e


def iter_staging_files(staging_dir: Path, bron: Optional[str]) -> list[Path]:
    if not staging_dir.exists():
        raise SystemExit(f"Staging-map bestaat niet: {staging_dir}")
    files = sorted(staging_dir.glob("*.md"))
    if bron:
        # Match op exacte stem of bestandsnaam
        files = [f for f in files if f.stem == bron or f.name == bron]
        if not files:
            raise SystemExit(f"Geen staging-MD gevonden voor --bron {bron!r}")
    return files


# ─── Modus 1: prompt-bundle genereren ────────────────────────────────────────

PROMPT_HEADER = """\
# Diff-review batch {run_id}

## Instructies voor subagent

Je bent een conservatieve regressie-checker voor de Certificaid bronnen-ETL.
Voor elk diff-blok hieronder, geef precies één verdict-record terug in dit
formaat (één JSON-object per bestand, geen markdown-fences eromheen):

```
{{
  "bestand": "<exact zoals in de header>",
  "diff_verdict": "improvement | regression | structural_change | no_op",
  "rationale": "1-3 zinnen — wat veranderde, is het beter/slechter/equivalent",
  "kritieke_observaties": ["..."]
}}
```

Heuristiek:

- `improvement` — duidelijke verbetering: artefacten verwijderd, headings
  beter gestructureerd, content completer of leesbaarder.
- `no_op` — niets verandert behalve `provenance.generated_at` of andere
  ruis-velden zonder semantische impact.
- `structural_change` — grote herstructurering (heading-niveaus opgeschoven,
  bron-splits anders gegroepeerd, ...). Mens moet er nog naar kijken.
- `regression` — slechter dan HEAD: juridische tekst verdwenen, headings
  weggevallen, nieuwe artefacten geïntroduceerd. Auto-trust geblokkeerd.

Bij twijfel tussen `improvement` en `structural_change`: kies
`structural_change`. Bij twijfel tussen `regression` en `structural_change`:
kies `regression` (conservatief).

Aantal bestanden in deze batch: {n_files}
Waarvan met HEAD-diff: {n_with_diff}
Waarvan nieuwe bron (auto no_op, geen verdict nodig): {n_new}

---

"""


def build_prompt_bundle(
    staging_files: list[Path],
    config: dict,
    rid: str,
) -> tuple[str, list[dict]]:
    """Bouw het markdown-prompt-rapport én de lijst auto-verdicts (no_op voor
    nieuwe bronnen).

    Returnt (prompt_markdown, auto_verdicts).
    """
    auto_verdicts: list[dict] = []
    diff_blocks: list[str] = []
    n_with_diff = 0

    for staging_path in staging_files:
        rel_staging = staging_path.relative_to(ROOT)
        head_path = staging_to_head_path(staging_path, config)

        if head_path is None or not head_path.exists():
            auto_verdicts.append({
                "bestand": str(rel_staging),
                "diff_verdict": "no_op",
                "rationale": "Nieuwe bron zonder HEAD-versie; auto no_op.",
                "kritieke_observaties": [],
                "auto": True,
            })
            continue

        diff_text = git_diff(head_path, staging_path)
        if not diff_text.strip():
            auto_verdicts.append({
                "bestand": str(rel_staging),
                "diff_verdict": "no_op",
                "rationale": "Staging-MD identiek aan HEAD; auto no_op.",
                "kritieke_observaties": [],
                "auto": True,
            })
            continue

        n_with_diff += 1
        block = (
            f"## Bestand: {rel_staging}\n\n"
            f"HEAD: `{head_path.relative_to(ROOT)}`\n\n"
            f"```diff\n{diff_text.rstrip()}\n```\n"
        )
        diff_blocks.append(block)

    n_new = sum(1 for v in auto_verdicts if "Nieuwe bron" in v["rationale"])
    header = PROMPT_HEADER.format(
        run_id=rid,
        n_files=len(staging_files),
        n_with_diff=n_with_diff,
        n_new=n_new,
    )
    body = "\n".join(diff_blocks) if diff_blocks else (
        "_Geen diff-blokken: alle bronnen zijn nieuw of identiek aan HEAD._\n"
    )
    return header + body, auto_verdicts


# ─── Modus 2: verdicts valideren en wegschrijven ─────────────────────────────

def parse_verdicts(text: str) -> list[dict]:
    """Parse subagent-output: één JSON-object per bron, willekeurige whitespace
    of markdown-fences ertussen. Accepteert ook één JSON-array."""
    text = text.strip()
    # Probeer eerst als JSON-array
    try:
        loaded = json.loads(text)
        if isinstance(loaded, list):
            return loaded
        if isinstance(loaded, dict):
            return [loaded]
    except json.JSONDecodeError:
        pass

    # Fallback: zoek alle JSON-objecten op het top-niveau via decoder
    decoder = json.JSONDecoder()
    out: list[dict] = []
    i = 0
    while i < len(text):
        # Sla witruimte en markdown-fences over
        while i < len(text) and text[i] in " \t\r\n":
            i += 1
        if i < len(text) and text[i] == "`":
            # Sla ```...``` of ``` over
            end = text.find("\n", i)
            if end == -1:
                break
            i = end + 1
            continue
        if i >= len(text):
            break
        if text[i] != "{":
            i += 1
            continue
        try:
            obj, end = decoder.raw_decode(text, i)
        except json.JSONDecodeError:
            i += 1
            continue
        if isinstance(obj, dict):
            out.append(obj)
        i = end
    return out


def validate_verdicts(verdicts: list[dict]) -> list[str]:
    """Returnt lijst foutmeldingen; lege lijst = OK."""
    errors: list[str] = []
    seen_bestanden: set[str] = set()
    for idx, v in enumerate(verdicts):
        prefix = f"verdict[{idx}]"
        if not isinstance(v, dict):
            errors.append(f"{prefix}: geen object")
            continue
        bestand = v.get("bestand")
        if not bestand or not isinstance(bestand, str):
            errors.append(f"{prefix}: ontbrekend of ongeldig 'bestand'")
        elif bestand in seen_bestanden:
            errors.append(f"{prefix}: duplicate 'bestand' {bestand!r}")
        else:
            seen_bestanden.add(bestand)

        verdict = v.get("diff_verdict")
        if verdict not in VALID_VERDICTS:
            errors.append(
                f"{prefix} ({bestand!r}): diff_verdict {verdict!r} niet in "
                f"{sorted(VALID_VERDICTS)}"
            )
        if "rationale" in v and not isinstance(v["rationale"], str):
            errors.append(f"{prefix} ({bestand!r}): rationale moet string zijn")
        if "kritieke_observaties" in v:
            obs = v["kritieke_observaties"]
            if not isinstance(obs, list) or not all(isinstance(o, str) for o in obs):
                errors.append(
                    f"{prefix} ({bestand!r}): kritieke_observaties moet list[str] zijn"
                )
    return errors


def canonical_verdicts(verdicts: list[dict], rid: str) -> dict:
    """Sorteer verdicts op bestand voor determinisme; wrap in run-envelop."""
    sorted_verdicts = sorted(
        verdicts,
        key=lambda v: v.get("bestand", ""),
    )
    cleaned = []
    for v in sorted_verdicts:
        cleaned.append({
            "bestand": v.get("bestand", ""),
            "diff_verdict": v.get("diff_verdict"),
            "rationale": v.get("rationale", ""),
            "kritieke_observaties": list(v.get("kritieke_observaties", [])),
            "auto": bool(v.get("auto", False)),
        })
    return {
        "run_id": rid,
        "verdicts": cleaned,
        "totals": _verdict_totals(cleaned),
    }


def _verdict_totals(verdicts: list[dict]) -> dict[str, int]:
    counters = {v: 0 for v in VALID_VERDICTS}
    for v in verdicts:
        verdict = v.get("diff_verdict")
        if verdict in counters:
            counters[verdict] += 1
    return counters


# ─── CLI ─────────────────────────────────────────────────────────────────────

def cmd_print_prompt(args: argparse.Namespace) -> None:
    config = load_config()
    staging_files = iter_staging_files(args.staging_dir, args.bron)
    rid = args.run_id or run_id()

    prompt, auto_verdicts = build_prompt_bundle(staging_files, config, rid)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(prompt, encoding="utf-8")
        print(f"Prompt-bundle: {args.out.relative_to(ROOT) if args.out.is_relative_to(ROOT) else args.out}")
    else:
        sys.stdout.write(prompt)

    # Schrijf auto-verdicts naar zij-bestand zodat apply-verdicts ze later kan mergen
    if auto_verdicts and args.out:
        auto_path = args.out.with_suffix(".auto-verdicts.json")
        canonical = canonical_verdicts(auto_verdicts, rid)
        auto_path.write_text(
            json.dumps(canonical, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        print(f"Auto-verdicts (no_op): {auto_path.relative_to(ROOT) if auto_path.is_relative_to(ROOT) else auto_path}")

    print(
        f"\nrun_id: {rid}\n"
        f"  bestanden:           {len(staging_files)}\n"
        f"  met HEAD-diff:       {len(staging_files) - len(auto_verdicts)}\n"
        f"  auto no_op:          {len(auto_verdicts)}"
    )


def cmd_apply_verdicts(args: argparse.Namespace) -> None:
    text = args.apply_verdicts.read_text(encoding="utf-8")
    verdicts = parse_verdicts(text)

    # Optioneel mergen met auto-verdicts (no_op voor nieuwe bronnen)
    if args.merge_auto:
        auto_text = args.merge_auto.read_text(encoding="utf-8")
        auto_data = json.loads(auto_text)
        auto_list = auto_data.get("verdicts", auto_data) if isinstance(auto_data, dict) else auto_data
        # Filter overlap: subagent-verdict wint van auto
        seen = {v.get("bestand") for v in verdicts}
        for av in auto_list:
            if av.get("bestand") not in seen:
                verdicts.append(av)

    errors = validate_verdicts(verdicts)
    if errors:
        for e in errors:
            print(f"  FOUT: {e}", file=sys.stderr)
        sys.exit(2)

    rid = args.run_id or run_id()
    canonical = canonical_verdicts(verdicts, rid)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(canonical, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Verdict-bestand: {args.out.relative_to(ROOT) if args.out.is_relative_to(ROOT) else args.out}")
    print(f"  totalen: {canonical['totals']}")


def main(argv: Optional[list[str]] = None) -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--staging-dir", type=Path, default=DEFAULT_STAGING_DIR,
                   help="map met staging-MDs (default: data/etl-staging/)")
    p.add_argument("--bron", help="enkel deze bron (stem of bestandsnaam)")
    p.add_argument("--out", type=Path,
                   help="output-bestand (modus 1: .md prompt-bundle; modus 2: .json verdicts)")
    p.add_argument("--run-id", help="forceer specifiek run-id (anders: UTC-timestamp)")

    mode = p.add_mutually_exclusive_group()
    mode.add_argument("--print-prompt", action="store_true",
                      help="modus 1 (default): genereer prompt-bundle voor subagent")
    mode.add_argument("--apply-verdicts", type=Path,
                      help="modus 2: lees subagent-output en schrijf canonical verdict-JSON")

    p.add_argument("--merge-auto", type=Path,
                   help="bij --apply-verdicts: merge auto-verdicts uit dit bestand "
                        "(typisch <out>.auto-verdicts.json uit modus 1)")

    args = p.parse_args(argv)

    # Default modus = print-prompt
    if not args.apply_verdicts:
        if not args.out:
            # Schrijf naar stdout als geen --out gegeven
            pass
        cmd_print_prompt(args)
    else:
        if not args.out:
            p.error("--apply-verdicts vereist --out <bestand>.json")
        cmd_apply_verdicts(args)


if __name__ == "__main__":
    main()
