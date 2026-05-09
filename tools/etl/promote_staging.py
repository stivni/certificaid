#!/usr/bin/env python3
"""Promotie van staging-MDs naar resources/bronnen/ met trust-status.

Uitvoering van Laag-3-flow uit ADR-005 §5: combineer de drie verdict-bronnen
(Laag 1 deterministisch, Laag 1.5 diff-review, Laag 2 inhoudelijke beoordeling)
en promoot kwalificerende staging-MDs naar `resources/bronnen/<rol-pad>/`,
waarbij `provenance.trust` correct wordt ingevuld.

Verdict-combinatie (ADR-005 §5):

    | Laag 1 | Laag 1.5                | Laag 2                  | Resultaat       |
    |--------|-------------------------|-------------------------|-----------------|
    | pass   | improvement / no_op     | trusted                 | auto-trust      |
    | pass   | structural_change       | trusted                 | review-pending  |
    | pass   | regression              | *                       | blocked         |
    | warn   | *                       | trusted                 | review-pending  |
    | fail   | *                       | *                       | blocked         |
    | *      | *                       | needs-rework / rejected | blocked         |

Wanneer Laag 2 ontbreekt voor een bron (geen content-verdict) wordt content
behandeld als `trusted` indien Laag 1 = pass én Laag 1.5 ∈ {improvement, no_op,
afwezig}. Anders blokkeer.

Gebruik:

    python3 tools/etl/promote_staging.py --run <run-id> \\
        --qa data/qa/<run-id>.json \\
        --diff data/qa/<run-id>-diff-verdicts.json \\
        [--content data/qa/<run-id>-content-verdicts.json] \\
        [--dry-run]

Schrijft samenvatting op stdout en `data/qa/<run-id>-promote-result.json`
met details. Blocked-bronnen blijven in staging; hun reden komt in
`data/qa/<run-id>-blocked.json`.

Idempotentie: tweede run met dezelfde inputs (zelfde verdicts + zelfde
staging) levert identieke trust-velden op (modulo het ene tijdstempel
`agent_verdict_at`, dat hergebruikt wordt uit het verdict-bestand of
deterministisch uit de run-id afgeleid kan worden via --verdict-time).
"""
from __future__ import annotations

import argparse
import io
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import yaml
from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIG_PATH = ROOT / "resources" / "source_config.yaml"
DEFAULT_STAGING_DIR = ROOT / "data" / "etl-staging"
DEFAULT_RESOURCES_DIR = ROOT / "resources" / "bronnen"
DEFAULT_QA_DIR = ROOT / "data" / "qa"

DEFAULT_CONFIRMED_BY = "subagent-sonnet-4-6"

# ─── Frontmatter I/O ─────────────────────────────────────────────────────────

_FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def _yaml_rt() -> YAML:
    y = YAML()
    y.preserve_quotes = True
    y.indent(mapping=2, sequence=4, offset=2)
    y.width = 4096
    return y


def _read_frontmatter(path: Path) -> tuple[Optional[dict], str]:
    text = path.read_text(encoding="utf-8")
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    data = _yaml_rt().load(m.group(1)) or {}
    body = text[m.end():]
    return data, body


def _write_frontmatter(path: Path, data: dict, body: str) -> None:
    buf = io.StringIO()
    _yaml_rt().dump(data, buf)
    path.write_text(f"---\n{buf.getvalue()}---\n{body}", encoding="utf-8")


# ─── Verdict-loading ─────────────────────────────────────────────────────────

def _load_qa_verdicts(path: Path) -> dict[str, dict]:
    """Laag 1: returns {bestandsnaam: verdict-dict}. bestand-key is basename."""
    data = json.loads(path.read_text(encoding="utf-8"))
    result: dict[str, dict] = {}
    bronnen = data.get("bronnen", []) if isinstance(data, dict) else []
    for entry in bronnen:
        bestand = entry.get("bestand")
        if not bestand:
            continue
        key = Path(bestand).name
        result[key] = entry
    return result


def _load_diff_verdicts(path: Path) -> dict[str, dict]:
    """Laag 1.5: returns {bestandsnaam: verdict-dict}."""
    data = json.loads(path.read_text(encoding="utf-8"))
    result: dict[str, dict] = {}
    verdicts = data.get("verdicts", []) if isinstance(data, dict) else data
    for entry in verdicts:
        bestand = entry.get("bestand")
        if not bestand:
            continue
        key = Path(bestand).name
        result[key] = entry
    return result


def _load_content_verdicts(path: Optional[Path]) -> dict[str, dict]:
    """Laag 2 (optioneel): returns {bestandsnaam: verdict-dict}."""
    if path is None:
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    result: dict[str, dict] = {}
    verdicts = data.get("verdicts", []) if isinstance(data, dict) else data
    for entry in verdicts:
        bestand = entry.get("bestand")
        if not bestand:
            continue
        key = Path(bestand).name
        result[key] = entry
    return result


# ─── Pad-mapping ─────────────────────────────────────────────────────────────

def _load_source_config(config_path: Path) -> dict:
    if not config_path.exists():
        return {}
    with config_path.open() as f:
        loaded = yaml.safe_load(f) or {}
    return loaded.get("sources", {}) if isinstance(loaded, dict) else {}


def _resolve_destination(
    staging_md: Path,
    source_config: dict,
    bron_rol: Optional[str],
    *,
    resources_root: Path,
    project_root: Path,
) -> Path:
    """Bepaal het doelpad in resources/bronnen/.

    Strategie:
      1. Match op `output:` in source_config (per bron of per split). Het
         pad is relatief tot project_root (zoals het in source_config.yaml
         staat: ``resources/bronnen/<rol>/<naam>.md``). Als de submap
         (wetteksten/normen/adviezen) van het output-pad bekend is, wordt
         die op resources_root toegepast — zo respecteert de mapping ook
         een tmp_path-resources_root in tests.
      2. Fallback op bron_rol → submap (wetteksten/normen/adviezen).
      3. Wetteksten/praktijkgids/formulier/normatief/itaa_lex → wetteksten/.
         Interpretatief → onderscheid normen vs. adviezen via bestandsnaam-
         heuristiek (advies-bestandsnamen beginnen typisch met `advies-` of
         een CBN-nummerpatroon; alle andere interpretatieve bronnen gaan
         naar normen/).
    """
    name = staging_md.name

    def _apply_output(out_str: str) -> Path:
        out_path = Path(out_str)
        if out_path.is_absolute():
            return out_path
        # Probeer out_str te interpreteren als "resources/bronnen/<sub>/<naam>".
        parts = out_path.parts
        if len(parts) >= 3 and parts[0] == "resources" and parts[1] == "bronnen":
            sub = parts[2]
            return resources_root / sub / Path(*parts[3:])
        # Fallback: relatief tot project_root.
        return project_root / out_path

    for cfg in source_config.values():
        out = cfg.get("output") if isinstance(cfg, dict) else None
        if out and Path(out).name == name:
            return _apply_output(out)
        for split in (cfg.get("splits", []) or []) if isinstance(cfg, dict) else []:
            split_out = split.get("output")
            if split_out and Path(split_out).name == name:
                return _apply_output(split_out)

    rol = (bron_rol or "").lower()
    if rol in {"itaa_lex", "normatief", "praktijkgids", "formulier"}:
        return resources_root / "wetteksten" / name
    if rol == "interpretatief":
        # Heuristiek: advies-bestanden hebben vaak `advies-` prefix of nummer-prefix
        lower = name.lower()
        if lower.startswith("advies-") or re.match(r"^\d{2,4}[-_]", lower):
            return resources_root / "adviezen" / name
        return resources_root / "normen" / name
    # Onbekend → veiligste default
    return resources_root / "wetteksten" / name


# ─── Verdict-combinatie ──────────────────────────────────────────────────────

VALID_QA = {"pass", "warn", "fail"}
VALID_DIFF = {"improvement", "regression", "structural_change", "no_op"}
VALID_CONTENT = {"trusted", "needs-rework", "rejected"}


def combine_verdicts(
    qa: Optional[str],
    diff: Optional[str],
    content: Optional[str],
    *,
    content_auto: bool = False,
    diff_auto: bool = False,
) -> tuple[str, str]:
    """Returnt (resultaat, reden).

    resultaat ∈ {"auto-trust", "review-pending", "blocked"}.

    Strikte content-verdict-vereiste (mei 2026 — gebruikersfeedback):
      * Ontbrekend content-verdict → blocked. Geen "default trusted"-pad meer.
      * Auto-gesynthetiseerd content-verdict (`content_auto=True`) →
        review-pending. Zo'n verdict is door een script geschreven, niet door
        een agent gelezen; daarom altijd menselijke steekproef.
      * Auto-gesynthetiseerd diff-verdict (`diff_auto=True`) wordt verder
        normaal verwerkt (diff is structurele check, geen content-judgment).

    Volgorde van blokkers (van strikt naar permissief):
      1. content ∈ {needs-rework, rejected}  → blocked
      2. qa == fail                          → blocked
      3. diff == regression                  → blocked
      4. content is None                     → blocked (vereist agent-lezing)
      5. content_auto en content == trusted  → review-pending
      6. qa == warn                          → review-pending
      7. qa == pass + diff ∈ {improvement, no_op, None} → auto-trust
      8. qa == pass + diff == structural_change         → review-pending
    """
    # Eerst content: needs-rework / rejected blokkeren altijd.
    if content in {"needs-rework", "rejected"}:
        return "blocked", f"content-verdict={content}"

    # Laag 1 fail → blocked.
    if qa == "fail":
        return "blocked", "Laag 1 verdict=fail"

    # Laag 1.5 regression → blocked.
    if diff == "regression":
        return "blocked", "Laag 1.5 verdict=regression"

    # Strikt: content-verdict is verplicht. Geen default-trusted-pad meer.
    if content is None:
        return "blocked", "content-verdict ontbreekt (agent-lezing vereist; geen auto-trust)"

    if content != "trusted":
        # safety net (mocht een onbekende waarde sluipen)
        return "blocked", f"content-verdict={content}"

    # Auto-gesynthetiseerd content-verdict: nooit auto-trust.
    if content_auto:
        return "review-pending", "content-verdict is auto-gesynthetiseerd (agent moet alsnog lezen)"

    # Hier is content effectief trusted door een agent.
    if qa == "warn":
        return "review-pending", "Laag 1 verdict=warn"

    if qa == "pass":
        if diff in {"improvement", "no_op", None}:
            return "auto-trust", "Laag 1 pass + Laag 1.5 OK"
        if diff == "structural_change":
            return "review-pending", "Laag 1.5 structural_change"

    # Onverwacht: blokkeer conservatief.
    return "blocked", f"onverwachte combinatie qa={qa!r} diff={diff!r} content={content!r}"


# ─── Promotie ────────────────────────────────────────────────────────────────

def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _set_trust(
    data: dict,
    *,
    qa_version: str,
    confirmed_by: str,
    rationale: str,
    sample_pick: bool,
    timestamp: str,
    qa_entry: Optional[dict] = None,
    diff_entry: Optional[dict] = None,
    content_entry: Optional[dict] = None,
) -> None:
    prov = data.setdefault("provenance", {})
    if not isinstance(prov, dict):
        # Vervang met dict — frontmatter zonder provenance is een gebroken bron,
        # maar we willen niet hard crashen tijdens promotie.
        data["provenance"] = {}
        prov = data["provenance"]
    trust = prov.get("trust")
    if not isinstance(trust, dict):
        trust = {}
        prov["trust"] = trust

    trust["status"] = "trusted"
    trust["qa_version"] = qa_version
    trust["agent_verdict_at"] = timestamp
    # confirmed_at houden we naast agent_verdict_at gelijk (legacy-veld).
    trust["confirmed_at"] = timestamp
    trust["confirmed_by"] = confirmed_by
    trust["rationale"] = rationale
    trust["sample_pick"] = sample_pick
    trust["sample_reviewed_at"] = None
    trust["sample_reviewed_by"] = None

    # Embed de drie laag-detail-blokken (ADR-005 §5). Tot mei 2026 leefden deze
    # in losse `data/qa/*.json`; nu inline in de bron-MD zodat elke bron zijn
    # volledige QA-historie meedraagt en aggregatie via grep mogelijk is.
    if qa_entry:
        flags = []
        for c in qa_entry.get("checks", []):
            st = c.get("status")
            if st in ("warn", "fail"):
                flags.append({"name": c.get("name"), "status": st,
                              "detail": c.get("detail"), "samples": c.get("samples", []) or []})
        trust["layer1"] = {
            "verdict": qa_entry.get("verdict"),
            "heading_count": qa_entry.get("heading_count"),
            "max_section_chars": qa_entry.get("max_section_chars"),
            "file_size_chars": qa_entry.get("file_size_chars"),
            "flags": flags,
            "run_id": qa_entry.get("run_id") or qa_version,
        }
    if diff_entry:
        trust["layer1_5_diff"] = {
            "verdict": diff_entry.get("diff_verdict") or diff_entry.get("verdict"),
            "rationale": diff_entry.get("rationale"),
            "kritieke_observaties": diff_entry.get("kritieke_observaties") or [],
            "auto": bool(diff_entry.get("auto", False)),
            "run_id": qa_version,
        }
    if content_entry:
        trust["layer2_content"] = {
            "verdict": content_entry.get("aanbevolen_status") or content_entry.get("verdict"),
            "rationale": content_entry.get("rationale"),
            "problemen": content_entry.get("concrete_problemen") or content_entry.get("problemen") or [],
            "sterkte": content_entry.get("concrete_sterke_punten") or content_entry.get("sterkte") or [],
            "auto": bool(content_entry.get("auto", False)),
            "run_id": qa_version,
        }


def _build_rationale(
    qa_entry: Optional[dict],
    diff_entry: Optional[dict],
    content_entry: Optional[dict],
) -> str:
    parts: list[str] = []
    if qa_entry:
        parts.append(f"L1={qa_entry.get('verdict', '?')}")
    if diff_entry:
        d = diff_entry.get("diff_verdict", "?")
        rat = (diff_entry.get("rationale") or "").strip()
        parts.append(f"L1.5={d}" + (f" ({rat})" if rat else ""))
    if content_entry:
        c = content_entry.get("aanbevolen_status", "?")
        rat = (content_entry.get("rationale") or "").strip()
        parts.append(f"L2={c}" + (f" ({rat})" if rat else ""))
    return "; ".join(parts) if parts else "(geen verdict-rationales)"


def _confirmed_by_from_verdicts(
    diff_entry: Optional[dict],
    content_entry: Optional[dict],
) -> str:
    for entry in (content_entry, diff_entry):
        if not entry:
            continue
        for key in ("confirmed_by", "agent", "subagent"):
            val = entry.get(key)
            if isinstance(val, str) and val.strip():
                return val.strip()
    return DEFAULT_CONFIRMED_BY


# ─── Hoofdflow ───────────────────────────────────────────────────────────────

def promote(
    *,
    run_id: str,
    qa_path: Path,
    diff_path: Path,
    content_path: Optional[Path],
    staging_dir: Path,
    resources_dir: Path,
    qa_dir: Path,
    config_path: Path,
    dry_run: bool = False,
    timestamp: Optional[str] = None,
    project_root: Optional[Path] = None,
) -> dict:
    """Voer de promotie uit en returnt het detail-rapport."""
    qa_verdicts = _load_qa_verdicts(qa_path)
    diff_verdicts = _load_diff_verdicts(diff_path)
    content_verdicts = _load_content_verdicts(content_path)
    source_config = _load_source_config(config_path)

    if not staging_dir.exists():
        raise SystemExit(f"Staging-map bestaat niet: {staging_dir}")

    if project_root is None:
        project_root = ROOT
    timestamp = timestamp or _now_iso()

    auto_trusted: list[str] = []
    review_pending: list[str] = []
    blocked: list[dict] = []

    staging_files = sorted(staging_dir.glob("*.md"))

    for staging_md in staging_files:
        name = staging_md.name
        qa_entry = qa_verdicts.get(name)
        diff_entry = diff_verdicts.get(name)
        content_entry = content_verdicts.get(name)

        qa_v = qa_entry.get("verdict") if qa_entry else None
        diff_v = diff_entry.get("diff_verdict") if diff_entry else None
        content_v = content_entry.get("aanbevolen_status") if content_entry else None
        content_auto = bool(content_entry.get("auto", False)) if content_entry else False
        diff_auto = bool(diff_entry.get("auto", False)) if diff_entry else False

        result, reden = combine_verdicts(
            qa_v, diff_v, content_v,
            content_auto=content_auto, diff_auto=diff_auto,
        )

        if result == "blocked":
            blocked.append({
                "bron": name,
                "reden": reden,
                "qa": qa_v,
                "diff": diff_v,
                "content": content_v,
            })
            continue

        # Lees bron_rol uit staging-frontmatter
        data, body = _read_frontmatter(staging_md)
        if data is None:
            blocked.append({
                "bron": name,
                "reden": "geen frontmatter in staging-MD",
                "qa": qa_v, "diff": diff_v, "content": content_v,
            })
            continue

        bron_rol = data.get("bron_rol") if isinstance(data, dict) else None
        dest_path = _resolve_destination(
            staging_md, source_config, bron_rol,
            resources_root=resources_dir,
            project_root=project_root,
        )

        sample_pick = (result == "review-pending")
        rationale = _build_rationale(qa_entry, diff_entry, content_entry)
        confirmed_by = _confirmed_by_from_verdicts(diff_entry, content_entry)

        _set_trust(
            data,
            qa_version=run_id,
            confirmed_by=confirmed_by,
            rationale=rationale,
            sample_pick=sample_pick,
            timestamp=timestamp,
            qa_entry=qa_entry,
            diff_entry=diff_entry,
            content_entry=content_entry,
        )

        if not dry_run:
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            _write_frontmatter(dest_path, data, body)

        if result == "auto-trust":
            auto_trusted.append(name)
        else:
            review_pending.append(name)

    rapport = {
        "run_id": run_id,
        "auto_trusted": sorted(auto_trusted),
        "review_pending": sorted(review_pending),
        "blocked": sorted(blocked, key=lambda b: b["bron"]),
    }

    if not dry_run:
        qa_dir.mkdir(parents=True, exist_ok=True)
        result_path = qa_dir / f"{run_id}-promote-result.json"
        result_path.write_text(
            json.dumps(rapport, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        if blocked:
            blocked_path = qa_dir / f"{run_id}-blocked.json"
            blocked_path.write_text(
                json.dumps(
                    {"run_id": run_id, "blocked": rapport["blocked"]},
                    indent=2, ensure_ascii=False,
                ) + "\n",
                encoding="utf-8",
            )

    return rapport


def _print_summary(rapport: dict, total: int, dry_run: bool, qa_dir: Path) -> None:
    rid = rapport["run_id"]
    n_auto = len(rapport["auto_trusted"])
    n_review = len(rapport["review_pending"])
    n_blocked = len(rapport["blocked"])
    prefix = "(DRY-RUN) " if dry_run else ""
    print(f"{prefix}Run {rid}: {total} staging-bronnen")
    print(f"  → {n_auto} auto-trusted (gepromoot)")
    print(f"  → {n_review} review-pending (gepromoot, sample_pick=true)")
    if n_blocked:
        if dry_run:
            print(f"  → {n_blocked} blocked (in staging gebleven)")
        else:
            blocked_path = qa_dir / f"{rid}-blocked.json"
            try:
                rel = blocked_path.relative_to(ROOT)
            except ValueError:
                rel = blocked_path
            print(f"  → {n_blocked} blocked (in staging gebleven; zie {rel})")
    else:
        print(f"  → 0 blocked")


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main(argv: Optional[list[str]] = None) -> None:
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--run", required=True, help="run-id (gebruikt als qa_version in trust-blok)")
    p.add_argument("--qa", required=True, type=Path,
                   help="pad naar Laag-1-rapport (qa_bron.py output)")
    p.add_argument("--diff", required=True, type=Path,
                   help="pad naar Laag-1.5-verdicts (diff_review.py canonical)")
    p.add_argument("--content", type=Path, default=None,
                   help="pad naar Laag-2-content-verdicts (optioneel)")
    p.add_argument("--staging-dir", type=Path, default=DEFAULT_STAGING_DIR,
                   help="staging-map (default: data/etl-staging/)")
    p.add_argument("--resources-dir", type=Path, default=DEFAULT_RESOURCES_DIR,
                   help="resources/bronnen-doelmap (default: resources/bronnen/)")
    p.add_argument("--qa-dir", type=Path, default=DEFAULT_QA_DIR,
                   help="map voor verdict-/result-bestanden (default: data/qa/)")
    p.add_argument("--config", type=Path, default=CONFIG_PATH,
                   help="source_config.yaml (default: resources/source_config.yaml)")
    p.add_argument("--dry-run", action="store_true",
                   help="toon planning, schrijf niets")
    p.add_argument("--verdict-time", default=None,
                   help="forceer ISO-tijdstempel voor agent_verdict_at "
                        "(default: nu in UTC); handig voor reproduceerbare tests")

    args = p.parse_args(argv)

    rapport = promote(
        run_id=args.run,
        qa_path=args.qa,
        diff_path=args.diff,
        content_path=args.content,
        staging_dir=args.staging_dir,
        resources_dir=args.resources_dir,
        qa_dir=args.qa_dir,
        config_path=args.config,
        dry_run=args.dry_run,
        timestamp=args.verdict_time,
    )

    total = sum(1 for _ in args.staging_dir.glob("*.md")) if args.staging_dir.exists() else 0
    _print_summary(rapport, total, args.dry_run, args.qa_dir)


if __name__ == "__main__":
    main()
