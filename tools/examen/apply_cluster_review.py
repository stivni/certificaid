"""Apply cluster-review-verdicts: update cluster-files + stamp cluster-id op interpretaties.

Leest `_clusters/_review.json` en verwerkt elke verdict:

- `false_positive` → cluster verwijderen uit `<po>.json`, leden naar singletons-lijst.
- `echt_duplicaat` / `varianten` → cluster behouden in `<po>.json` met `verdict` + `actie`
  velden; elk lid krijgt `cluster_id` + `cluster_verdict` + `cluster_actie` op zijn
  interpretatie-file (additieve velden, schema 1.2 compatible).

Deterministisch, idempotent, fail-loud.

CLI:
    python3 -m tools.examen.apply_cluster_review
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
CLUSTERS_DIR = REPO_ROOT / "data" / "programma" / "examen_vragen" / "_clusters"
INTERPRETATIES_DIR = REPO_ROOT / "data" / "programma" / "examen_vragen" / "_interpretaties"
REVIEW_PAD = CLUSTERS_DIR / "_review.json"


def _laad_json(pad: Path) -> dict[str, Any]:
    return json.loads(pad.read_text(encoding="utf-8"))


def _schrijf_json(pad: Path, data: dict[str, Any]) -> None:
    pad.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def _verdicts_per_cluster(review: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Map cluster_id → verdict-record."""
    return {r["cluster_id"]: r for r in review["reviews"]}


def _process_po_cluster_file(
    po_pad: Path,
    verdicts: dict[str, dict[str, Any]],
) -> tuple[int, int, list[tuple[str, str]]]:
    """Update één per-PO cluster-file op basis van de verdicts.

    Returns (n_overlevend, n_false_positive, lijst_van_(cluster_id, lid_vraag_id)
    voor overlevende clusters — om interpretaties te stempelen).
    """
    data = _laad_json(po_pad)
    nieuwe_clusters: list[dict[str, Any]] = []
    false_positive_leden: list[dict[str, Any]] = []
    stamp_paren: list[tuple[str, str]] = []
    n_fp = 0

    for cluster in data["clusters"]:
        cid = cluster["cluster_id"]
        verdict = verdicts.get(cid)
        if verdict is None:
            # Geen review — laat staan zonder verdict-veld
            nieuwe_clusters.append(cluster)
            continue
        v = verdict["verdict"]
        cluster["verdict"] = v
        cluster["actie"] = verdict["actie"]
        cluster["motivering"] = verdict["motivering"]
        if v == "false_positive":
            n_fp += 1
            # Members terug naar singletons
            for lid in cluster["voorkomens"]:
                false_positive_leden.append(lid)
        else:
            nieuwe_clusters.append(cluster)
            for lid in cluster["voorkomens"]:
                stamp_paren.append((cid, lid["vraag_id"]))

    if false_positive_leden:
        data["singletons"] = list(data.get("singletons", []) + false_positive_leden)
        # Dedup op vraag_id voor het geval
        seen = set()
        dedup: list[dict[str, Any]] = []
        for s in data["singletons"]:
            if s["vraag_id"] in seen:
                continue
            seen.add(s["vraag_id"])
            dedup.append(s)
        data["singletons"] = dedup

    data["clusters"] = nieuwe_clusters
    data["n_clusters"] = len(nieuwe_clusters)
    data["n_singletons"] = len(data.get("singletons", []))
    data["review_toegepast_op"] = datetime.now(timezone.utc).isoformat(timespec="seconds")

    _schrijf_json(po_pad, data)
    return len(nieuwe_clusters), n_fp, stamp_paren


def _stamp_interpretatie(
    examen_id: str,
    vraag_id: str,
    cluster_id: str,
    verdict: str,
    actie: str,
) -> bool:
    """Voeg `cluster_id` + `cluster_verdict` + `cluster_actie` toe aan
    interpretatie-file. Idempotent.

    Returns True bij effectieve wijziging.
    """
    pad = INTERPRETATIES_DIR / examen_id / f"{vraag_id}.json"
    if not pad.is_file():
        print(f"WARN: interpretatie ontbreekt: {pad}", file=sys.stderr)
        return False
    data = _laad_json(pad)
    huidige = (
        data.get("cluster_id"),
        data.get("cluster_verdict"),
        data.get("cluster_actie"),
    )
    nieuwe = (cluster_id, verdict, actie)
    if huidige == nieuwe:
        return False
    data["cluster_id"] = cluster_id
    data["cluster_verdict"] = verdict
    data["cluster_actie"] = actie
    _schrijf_json(pad, data)
    return True


def _verwijder_cluster_velden(examen_id: str, vraag_id: str) -> bool:
    """Strip cluster-velden uit interpretatie (voor false-positive-leden)."""
    pad = INTERPRETATIES_DIR / examen_id / f"{vraag_id}.json"
    if not pad.is_file():
        return False
    data = _laad_json(pad)
    if not any(k in data for k in ("cluster_id", "cluster_verdict", "cluster_actie")):
        return False
    for k in ("cluster_id", "cluster_verdict", "cluster_actie"):
        data.pop(k, None)
    _schrijf_json(pad, data)
    return True


def main() -> int:
    if not REVIEW_PAD.is_file():
        print(f"ERROR: review-file ontbreekt: {REVIEW_PAD}", file=sys.stderr)
        return 1
    review = _laad_json(REVIEW_PAD)
    verdicts = _verdicts_per_cluster(review)

    print(f"[apply] Review-verdicts geladen: {len(verdicts)} clusters")

    # Map false-positive cluster-id → leden (om hun interpretatie-velden te strippen)
    fp_leden_per_examen: dict[str, list[str]] = defaultdict(list)
    for r in review["reviews"]:
        if r["verdict"] == "false_positive":
            for vid in r["voorkomens"]:
                # vid = "2015-1-vr28" — eerste segment-pair is examen_id
                # Extract examen_id: "2015-1" of "2003-bibf"
                # Vraag-id eindigt op -vrXX of -vrXXY; alles ervoor is examen
                idx = vid.rfind("-vr")
                if idx == -1:
                    print(f"WARN: kon examen_id niet bepalen uit {vid}", file=sys.stderr)
                    continue
                examen_id = vid[:idx]
                fp_leden_per_examen[examen_id].append(vid)

    # Verwerk alle per-PO cluster-files
    totaal_overlevend = 0
    totaal_fp = 0
    totaal_stamps = 0
    for po_pad in sorted(CLUSTERS_DIR.glob("*.json")):
        if po_pad.name.startswith("_"):
            continue  # _review.json zelf overslaan
        n_overlevend, n_fp, stamp_paren = _process_po_cluster_file(po_pad, verdicts)
        totaal_overlevend += n_overlevend
        totaal_fp += n_fp
        # Stamp interpretaties van overlevende clusters
        for cid, lid_vid in stamp_paren:
            v = verdicts[cid]
            # Examen-id uit lid_vid extraheren
            idx = lid_vid.rfind("-vr")
            if idx == -1:
                continue
            examen_id = lid_vid[:idx]
            if _stamp_interpretatie(examen_id, lid_vid, cid, v["verdict"], v["actie"]):
                totaal_stamps += 1
        print(f"  {po_pad.name}: {n_overlevend} overlevend, {n_fp} false-positive")

    # Strip cluster-velden van false-positive leden
    totaal_strips = 0
    for examen_id, vragen in fp_leden_per_examen.items():
        for vid in vragen:
            if _verwijder_cluster_velden(examen_id, vid):
                totaal_strips += 1

    print()
    print(f"[apply] Overlevende clusters totaal: {totaal_overlevend}")
    print(f"[apply] False-positives gesloten: {totaal_fp}")
    print(f"[apply] Interpretaties gestempeld: {totaal_stamps}")
    print(f"[apply] Interpretaties gestript (false-positive leden): {totaal_strips}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
