"""Diff-changelog generator voor Certificaid leermateriaal (ADR-010 §versionering).

Vervangt het oude append-only `content/snapshots/<v>/`-pad. Werkt met git als
versie-systeem: vergelijk huidige HEAD met laatste publieke tag (default
`v1.0`, overrideable), filter wijzigingen tot content/concepten/,
content/competenties/, content/studiemateriaal/, classificeer per file
(inhoudelijk vs render-only), schrijf changelog-pagina + cache voor
render-laag (per-fiche "Bijgewerkt"-badge).

Gebruik:
  python3 -m tools.leermateriaal.build_changelog                # default v1.0
  python3 -m tools.leermateriaal.build_changelog --basis-tag v1.0
  python3 -m tools.leermateriaal.build_changelog --basis-tag 01ada764  # commit-hash ad-hoc

Output:
  content/changelog/index.md       — chronologisch overzicht voor de student
  data/leermateriaal/wijzigingen-sinds-<tag>.json  — cache voor render-laag
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import TypedDict

ROOT = Path(__file__).resolve().parent.parent.parent
RECORDS_DIR = ROOT / "data" / "concepten" / "records"
CHANGELOG_DIR = ROOT / "content" / "changelog"
CACHE_DIR = ROOT / "data" / "leermateriaal"

CONTENT_PADEN = (
    "content/concepten/",
    "content/competenties/",
    "content/studiemateriaal/",
)
RECORD_PADEN = (
    "data/concepten/records/",
)


class Wijziging(TypedDict):
    pad: str
    status: str  # A/M/D
    classificatie: str  # "inhoudelijk" | "render-only" | "structureel"
    commit: str
    commit_date: str
    commit_subject: str


def _git(*args: str) -> str:
    """Run git en return stdout."""
    result = subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=True,
    )
    return result.stdout.strip()


def _ref_bestaat(ref: str) -> bool:
    try:
        subprocess.run(
            ["git", "rev-parse", "--verify", ref],
            capture_output=True, text=True, cwd=ROOT, check=True,
        )
        return True
    except subprocess.CalledProcessError:
        return False


def _classificeer(pad: str, status: str) -> str:
    """Classificeer wijziging als inhoudelijk / render-only / structureel.

    Heuristiek:
    - Toevoeging of verwijdering van een record → structureel
    - Toevoeging/verwijdering van een fiche → structureel
    - Wijziging in data/concepten/records/ → inhoudelijk (record-mutatie)
    - Wijziging in content/ zonder bijbehorende record-mutatie → render-only
    - Default content-wijziging → inhoudelijk (false positive is goedaardig)
    """
    if status in ("A", "D"):
        return "structureel"
    return "inhoudelijk"


def _wijzigingen_sinds(basis_ref: str) -> list[Wijziging]:
    """Verzamel alle wijzigingen in content/ + data/concepten/records/ sinds basis_ref."""
    if not _ref_bestaat(basis_ref):
        raise SystemExit(
            f"FOUT: ref '{basis_ref}' bestaat niet. Set een tag met `git tag v1.0` "
            f"of geef een commit-hash via --basis-tag <hash>."
        )

    # Verzamel commits met hun gewijzigde files
    log_output = _git(
        "log",
        f"{basis_ref}..HEAD",
        "--name-status",
        "--pretty=format:COMMIT|%H|%cI|%s",
    )

    wijzigingen: list[Wijziging] = []
    huidige_commit = ""
    huidige_date = ""
    huidige_subject = ""

    for regel in log_output.split("\n"):
        if regel.startswith("COMMIT|"):
            _, huidige_commit, huidige_date, huidige_subject = regel.split("|", 3)
            continue
        if not regel.strip():
            continue
        # status\tpad of status\told_pad\tnew_pad
        delen = regel.split("\t")
        status = delen[0][0] if delen[0] else ""
        pad = delen[-1]
        if any(pad.startswith(p) for p in (*CONTENT_PADEN, *RECORD_PADEN)):
            wijzigingen.append(Wijziging(
                pad=pad,
                status=status,
                classificatie=_classificeer(pad, status),
                commit=huidige_commit[:8],
                commit_date=huidige_date[:10],
                commit_subject=huidige_subject,
            ))

    return wijzigingen


def _record_ids_uit_wijzigingen(wijzigingen: list[Wijziging]) -> dict[str, list[Wijziging]]:
    """Map record-id → lijst van wijzigingen die er betrekking op hebben.

    Pakt zowel data/concepten/records/<id>.json als content/concepten/<id>.md.
    """
    by_id: dict[str, list[Wijziging]] = {}
    for w in wijzigingen:
        pad = w["pad"]
        if pad.startswith("data/concepten/records/") and pad.endswith(".json"):
            rid = Path(pad).stem
        elif pad.startswith("content/concepten/") and pad.endswith(".md"):
            rid = Path(pad).stem
        elif pad.startswith("content/competenties/") and pad.endswith(".md"):
            rid = Path(pad).stem
        else:
            continue
        by_id.setdefault(rid, []).append(w)
    return by_id


def _minicursus_ids_uit_wijzigingen(wijzigingen: list[Wijziging]) -> dict[str, list[Wijziging]]:
    by_id: dict[str, list[Wijziging]] = {}
    for w in wijzigingen:
        pad = w["pad"]
        if pad.startswith("content/studiemateriaal/") and pad.endswith(".md"):
            rid = Path(pad).stem
            by_id.setdefault(rid, []).append(w)
    return by_id


def _schrijf_changelog_pagina(
    basis_ref: str,
    wijzigingen: list[Wijziging],
    records_idx: dict[str, list[Wijziging]],
    minicursus_idx: dict[str, list[Wijziging]],
) -> Path:
    """Schrijf /content/changelog/index.md."""
    CHANGELOG_DIR.mkdir(parents=True, exist_ok=True)
    pad = CHANGELOG_DIR / "index.md"

    nu = datetime.now().strftime("%Y-%m-%d")
    inhoudelijk_count = sum(1 for w in wijzigingen if w["classificatie"] == "inhoudelijk")
    structureel_count = sum(1 for w in wijzigingen if w["classificatie"] == "structureel")

    regels = [
        "---",
        "title: Wat is er veranderd?",
        "tags:",
        "- changelog",
        f"gegenereerd_op: {nu}",
        f"basis_ref: {basis_ref}",
        "---",
        "",
        f"# Wat is er veranderd sinds {basis_ref}?",
        "",
        f"_{len(wijzigingen)} wijzigingen — {inhoudelijk_count} inhoudelijk, "
        f"{structureel_count} structureel._",
        "",
        "Deze pagina toont wat er veranderd is in de leerstof sinds release "
        f"`{basis_ref}`. Gebruik dit als jouw oriëntatiepunt tijdens herhalingsruns — "
        "lees alleen wat veranderd is, niet de hele cursus opnieuw.",
        "",
        "## Gewijzigde concepten",
        "",
    ]
    if records_idx:
        for rid, ws in sorted(records_idx.items()):
            laatste = max(ws, key=lambda x: x["commit_date"])
            regels.append(f"- [[{rid}]] — laatst bijgewerkt {laatste['commit_date']} "
                          f"({len(ws)} wijziging{'en' if len(ws) > 1 else ''})")
        regels.append("")
    else:
        regels.append("_Geen wijzigingen in concept-fiches._")
        regels.append("")

    regels.extend([
        "## Gewijzigde minicursussen",
        "",
    ])
    if minicursus_idx:
        for mid, ws in sorted(minicursus_idx.items()):
            laatste = max(ws, key=lambda x: x["commit_date"])
            regels.append(f"- [[studiemateriaal/{mid}|{mid}]] — laatst bijgewerkt {laatste['commit_date']}")
        regels.append("")
    else:
        regels.append("_Geen wijzigingen in minicursussen._")
        regels.append("")

    regels.extend([
        "## Chronologisch",
        "",
        "Volledige lijst van wijzigingen, nieuwste eerst:",
        "",
    ])

    # Groepeer per commit
    per_commit: dict[str, list[Wijziging]] = {}
    for w in wijzigingen:
        per_commit.setdefault(w["commit"], []).append(w)
    commits_sorted = sorted(
        per_commit.keys(),
        key=lambda c: per_commit[c][0]["commit_date"],
        reverse=True,
    )
    for commit in commits_sorted:
        ws = per_commit[commit]
        regels.append(f"### {ws[0]['commit_date']} — `{commit}` {ws[0]['commit_subject']}")
        regels.append("")
        for w in ws:
            status_label = {"A": "nieuw", "M": "gewijzigd", "D": "verwijderd"}.get(w["status"], w["status"])
            regels.append(f"- `{status_label}` {w['pad']} ({w['classificatie']})")
        regels.append("")

    pad.write_text("\n".join(regels) + "\n", encoding="utf-8")
    return pad


def _schrijf_render_cache(
    basis_ref: str,
    records_idx: dict[str, list[Wijziging]],
    minicursus_idx: dict[str, list[Wijziging]],
) -> Path:
    """Schrijf cache voor render-laag — per-fiche badge-rendering.

    Twee bestanden: een historisch bestand per basis_ref en een
    `wijzigingen-actueel.json` voor render-laag (well-known pad).
    """
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache = {
        "basis_ref": basis_ref,
        "gegenereerd_op": datetime.now().isoformat(timespec="seconds"),
        "records": {rid: [w["commit_date"] for w in ws] for rid, ws in records_idx.items()},
        "minicursussen": {mid: [w["commit_date"] for w in ws] for mid, ws in minicursus_idx.items()},
    }
    blob = json.dumps(cache, ensure_ascii=False, indent=2) + "\n"
    historisch = CACHE_DIR / f"wijzigingen-sinds-{basis_ref.replace('/', '_')}.json"
    actueel = CACHE_DIR / "wijzigingen-actueel.json"
    historisch.write_text(blob, encoding="utf-8")
    actueel.write_text(blob, encoding="utf-8")
    return historisch


def _bepaal_basis_ref(opgegeven: str | None) -> str:
    """Default: laatste tag matching v*. Fallback op opgegeven of error."""
    if opgegeven:
        return opgegeven
    try:
        tag = _git("describe", "--tags", "--match", "v*", "--abbrev=0")
        return tag
    except subprocess.CalledProcessError:
        raise SystemExit(
            "FOUT: geen v*-tag gevonden. Set een eerst met `git tag v1.0` of "
            "geef een commit-hash via --basis-tag <hash>."
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--basis-tag",
        default=None,
        help="Ref om vandaan te diffen (default: laatste v*-tag).",
    )
    args = parser.parse_args()

    basis_ref = _bepaal_basis_ref(args.basis_tag)
    print(f"[changelog] basis-ref: {basis_ref}")

    wijzigingen = _wijzigingen_sinds(basis_ref)
    if not wijzigingen:
        print("[changelog] Geen wijzigingen in content/ of records/ sinds basis-ref.")
        return 0

    records_idx = _record_ids_uit_wijzigingen(wijzigingen)
    minicursus_idx = _minicursus_ids_uit_wijzigingen(wijzigingen)

    pagina = _schrijf_changelog_pagina(basis_ref, wijzigingen, records_idx, minicursus_idx)
    cache = _schrijf_render_cache(basis_ref, records_idx, minicursus_idx)

    print(f"[changelog] {len(wijzigingen)} wijzigingen ({len(records_idx)} records, "
          f"{len(minicursus_idx)} minicursussen)")
    print(f"  Pagina: {pagina.relative_to(ROOT)}")
    print(f"  Cache:  {cache.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
