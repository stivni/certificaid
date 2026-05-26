"""Cluster examenvragen per programmaonderdeel via bge-m3 embeddings.

Doel: duplicaat- en variant-vragen identificeren zodat ze samen beantwoord
kunnen worden, met een frequentie-signaal ("N× bevraagd") als belangsmaat.

Werkwijze:
1. Verzamel alle interpretaties met `programmaonderdeel_ids` bevattend de
   doel-PO.
2. Bouw per vraag een embed-tekst: `vraag_onderwerp + vraagstelling(en)`.
3. POST batch naar embedding-daemon (`POST /embed`, bge-m3, MPS).
4. Bereken cosine-similarity-matrix.
5. Greedy single-link clustering: paren met cosine ≥ threshold worden
   verbonden, transitief gesloten tot clusters.
6. Output: `data/programma/examen_vragen/_clusters/<po>.json` met clusters
   + singletons + per-paar cosine-score voor handmatige review.

CLI:
    python3 -m tools.examen.cluster_vragen --po 1.4
    python3 -m tools.examen.cluster_vragen --po 1.4 --threshold 0.80
    python3 -m tools.examen.cluster_vragen --po-all   # alle PO's
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import urllib.request
import urllib.error

REPO_ROOT = Path(__file__).resolve().parents[2]
INTERPRETATIES_DIR = REPO_ROOT / "data" / "programma" / "examen_vragen" / "_interpretaties"
CLUSTERS_DIR = REPO_ROOT / "data" / "programma" / "examen_vragen" / "_clusters"

DAEMON_URL = "http://localhost:8765"
DEFAULT_THRESHOLD = 0.85

SCHEMA_VERSIE = "1.0"


def _laad_interpretatie(pad: Path) -> dict[str, Any] | None:
    """Lees één interpretatie-file. Returns None bij parse-fout."""
    try:
        return json.loads(pad.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        print(f"WARN: kon {pad} niet lezen: {exc}", file=sys.stderr)
        return None


def _verzamel_vragen_per_po(po_code: str) -> list[dict[str, Any]]:
    """Verzamel alle vragen die binnen de gegeven PO vallen."""
    vragen: list[dict[str, Any]] = []
    for examen_dir in sorted(INTERPRETATIES_DIR.iterdir()):
        if not examen_dir.is_dir():
            continue
        for vraag_pad in sorted(examen_dir.glob("*.json")):
            data = _laad_interpretatie(vraag_pad)
            if data is None:
                continue
            if po_code not in (data.get("programmaonderdeel_ids") or []):
                continue
            vragen.append({
                "examen_id": data.get("examen_id", examen_dir.name),
                "vraag_id": data.get("vraag_id", vraag_pad.stem),
                "vraag_onderwerp": data.get("vraag_onderwerp") or "",
                "themas": data.get("themas") or [],
                "vraagstellingen": [
                    v.get("vraagstelling", "") for v in data.get("vragen", [])
                ],
                "vraag_pad": str(vraag_pad.relative_to(REPO_ROOT)),
            })
    return vragen


def _bouw_embed_tekst(v: dict[str, Any]) -> str:
    """Bouw de tekst die geëmbed wordt voor similarity.

    Combinatie van vraag_onderwerp + alle vraagstellingen geeft een sterke
    semantische vingerafdruk. Themas worden weggelaten — die helpen wel voor
    vraag-onderwerp-detectie maar zijn vaak overlappend en zouden valse
    similarity opleveren tussen verschillende vragen rond hetzelfde thema.
    """
    onderwerp = (v["vraag_onderwerp"] or "").strip()
    vraagstellingen = " ".join(
        (vs or "").strip() for vs in v["vraagstellingen"] if (vs or "").strip()
    )
    if onderwerp and vraagstellingen:
        return f"{onderwerp}. {vraagstellingen}"
    return onderwerp or vraagstellingen or "(geen tekst)"


def _embed_via_daemon(teksten: list[str]) -> list[list[float]]:
    """POST naar /embed; return één embedding per tekst."""
    payload = json.dumps({"texts": teksten}).encode("utf-8")
    req = urllib.request.Request(
        url=f"{DAEMON_URL}/embed",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Embedding-daemon niet bereikbaar op {DAEMON_URL}: {exc}") from exc
    return data["embeddings"]


def _cosine(a: list[float], b: list[float]) -> float:
    """Cosine similarity tussen twee vectoren (zonder numpy)."""
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(y * y for y in b) ** 0.5
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def _cluster_greedy(
    vragen: list[dict[str, Any]],
    embeddings: list[list[float]],
    threshold: float,
) -> tuple[list[list[int]], list[tuple[int, int, float]]]:
    """Single-link clustering: paren met cosine ≥ threshold = zelfde cluster.

    Returns (clusters_van_indices, paren_boven_threshold_met_score).
    """
    n = len(vragen)
    # Union-find datastructuur
    parent = list(range(n))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(i: int, j: int) -> None:
        ri, rj = find(i), find(j)
        if ri != rj:
            parent[ri] = rj

    paren: list[tuple[int, int, float]] = []
    for i in range(n):
        for j in range(i + 1, n):
            score = _cosine(embeddings[i], embeddings[j])
            if score >= threshold:
                paren.append((i, j, score))
                union(i, j)

    # Groepeer indices per root
    clusters_map: dict[int, list[int]] = defaultdict(list)
    for i in range(n):
        clusters_map[find(i)].append(i)

    # Sorteer: grootste clusters eerst
    clusters = sorted(clusters_map.values(), key=lambda c: -len(c))
    paren.sort(key=lambda p: -p[2])
    return clusters, paren


def _voorlopige_label(vragen_in_cluster: list[dict[str, Any]]) -> str:
    """Kies het kortste vraag_onderwerp als voorlopige label."""
    onderwerpen = [v["vraag_onderwerp"] for v in vragen_in_cluster if v["vraag_onderwerp"]]
    if not onderwerpen:
        return "(geen onderwerp)"
    return min(onderwerpen, key=len)


def cluster_po(po_code: str, threshold: float = DEFAULT_THRESHOLD) -> Path:
    """Cluster alle vragen binnen één PO. Schrijf JSON-output."""
    vragen = _verzamel_vragen_per_po(po_code)
    if not vragen:
        raise RuntimeError(f"Geen vragen gevonden voor PO {po_code}")

    teksten = [_bouw_embed_tekst(v) for v in vragen]
    print(f"[cluster] PO {po_code}: {len(vragen)} vragen → embed via daemon ...")
    embeddings = _embed_via_daemon(teksten)
    print(f"[cluster] PO {po_code}: embeddings ontvangen ({len(embeddings[0])}-D).")

    cluster_indices, paren = _cluster_greedy(vragen, embeddings, threshold)
    print(f"[cluster] PO {po_code}: {len(cluster_indices)} clusters, "
          f"{len(paren)} paren ≥ {threshold}.")

    clusters_uit: list[dict[str, Any]] = []
    singletons_uit: list[dict[str, Any]] = []
    cluster_seq = 0
    for groep in cluster_indices:
        if len(groep) == 1:
            v = vragen[groep[0]]
            singletons_uit.append({
                "examen_id": v["examen_id"],
                "vraag_id": v["vraag_id"],
                "vraag_onderwerp": v["vraag_onderwerp"],
                "vraag_pad": v["vraag_pad"],
            })
            continue
        cluster_seq += 1
        groep_vragen = [vragen[i] for i in groep]
        clusters_uit.append({
            "cluster_id": f"{po_code}-c{cluster_seq}",
            "voorlopige_label": _voorlopige_label(groep_vragen),
            "n_voorkomens": len(groep),
            "voorkomens": [
                {
                    "examen_id": v["examen_id"],
                    "vraag_id": v["vraag_id"],
                    "vraag_onderwerp": v["vraag_onderwerp"],
                    "vraag_pad": v["vraag_pad"],
                }
                for v in groep_vragen
            ],
            "interne_scores": [
                {
                    "van": vragen[i]["vraag_id"],
                    "naar": vragen[j]["vraag_id"],
                    "cosine": round(score, 4),
                }
                for (i, j, score) in paren
                if i in groep and j in groep
            ],
        })

    # Toon ook borderline-paren NAAST clusters (paren onder threshold die
    # mogelijk relevant zijn voor manual review)
    borderline_paren = []
    for i in range(len(vragen)):
        for j in range(i + 1, len(vragen)):
            score = _cosine(embeddings[i], embeddings[j])
            if 0.75 <= score < threshold:
                borderline_paren.append({
                    "van": vragen[i]["vraag_id"],
                    "naar": vragen[j]["vraag_id"],
                    "cosine": round(score, 4),
                })
    borderline_paren.sort(key=lambda p: -p["cosine"])

    output = {
        "schema_versie": SCHEMA_VERSIE,
        "po_code": po_code,
        "gegenereerd_op": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "embedding_model": "BAAI/bge-m3",
        "threshold_cosine": threshold,
        "n_vragen": len(vragen),
        "n_clusters": len(clusters_uit),
        "n_singletons": len(singletons_uit),
        "clusters": clusters_uit,
        "borderline_paren": borderline_paren[:20],  # top-20 voor review
        "singletons": singletons_uit,
    }

    CLUSTERS_DIR.mkdir(parents=True, exist_ok=True)
    out_pad = CLUSTERS_DIR / f"{po_code}.json"
    out_pad.write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"[cluster] PO {po_code}: geschreven → {out_pad.relative_to(REPO_ROOT)}")
    return out_pad


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--po", help="Cluster één PO (bv. 1.4).")
    parser.add_argument("--po-all", action="store_true", help="Alle PO's clusteren.")
    parser.add_argument(
        "--threshold",
        type=float,
        default=DEFAULT_THRESHOLD,
        help=f"Cosine-threshold voor cluster-merging (default {DEFAULT_THRESHOLD}).",
    )
    args = parser.parse_args(argv)

    if not args.po and not args.po_all:
        parser.error("Geef --po <code> of --po-all op.")

    if args.po_all:
        # Discover alle PO-codes uit interpretaties
        alle_po: set[str] = set()
        for examen_dir in INTERPRETATIES_DIR.iterdir():
            if not examen_dir.is_dir():
                continue
            for pad in examen_dir.glob("*.json"):
                d = _laad_interpretatie(pad)
                if d:
                    alle_po.update(d.get("programmaonderdeel_ids") or [])
        for po in sorted(alle_po):
            try:
                cluster_po(po, args.threshold)
            except RuntimeError as exc:
                print(f"WARN: skip PO {po}: {exc}", file=sys.stderr)
    else:
        cluster_po(args.po, args.threshold)

    return 0


if __name__ == "__main__":
    sys.exit(main())
