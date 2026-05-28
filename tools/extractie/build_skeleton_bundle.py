"""Bundle-builder voor schema-2.2 skeleton-records (ADR-027 pattern).

Pre-fetch alle bronnen-chunks die de agent nodig heeft, zodat agent direct kan schrijven
zonder live MCP-calls. Verwante records (relaties.target) ook meegeleverd voor cross-context.

Output: data/extractie/bundles/<record-id>.json met:
- skeleton: het schema-2.2 skeleton-record
- bronnen_chunks: per scope.in-query → top-K bronnen-hits
- verwante_records: id + naam.primair + kern.definitie van relatie-targets

Gebruik:
    python3 -m tools.extractie.build_skeleton_bundle <record-id>
    python3 -m tools.extractie.build_skeleton_bundle --cluster <cluster-naam>
    python3 -m tools.extractie.build_skeleton_bundle --all
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RECORDS_DIR = ROOT / "data" / "concepten" / "records"
BUNDLES_DIR = ROOT / "data" / "extractie" / "bundles"
DAEMON = "http://localhost:8765"
TOP_K = 5


def _daemon_search(query: str, top_k: int = TOP_K, rerank: bool = False) -> list[dict]:
    """Roep daemon /zoek-bronnen aan. Default rerank=False (snel bi-encoder).
    Agent kan zelf rerank doen via MCP zoek_bronnen voor specifieke claims."""
    payload = json.dumps({"query": query, "top_k": top_k, "rerank": rerank}).encode()
    req = urllib.request.Request(
        f"{DAEMON}/zoek-bronnen",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.load(resp)
            return data.get("results") or data.get("hits") or []
    except (urllib.error.URLError, TimeoutError) as e:
        print(f"  ! daemon-fout voor '{query[:50]}': {e}", file=sys.stderr)
        return []


def _record_summary(rid: str) -> dict | None:
    """Lees record id + naam + kern.definitie (compact voor verwante-records-lijst)."""
    p = RECORDS_DIR / f"{rid}.json"
    if not p.exists():
        return None
    try:
        r = json.load(p.open())
    except Exception:
        return None
    kern_def = ((r.get("inhoud") or {}).get("kern") or {}).get("definitie") or {}
    return {
        "id": r.get("id", rid),
        "naam": (r.get("naam") or {}).get("primair", rid),
        "concept_type": r.get("concept_type", ""),
        "categorieen": (r.get("metadata") or {}).get("categorieen") or [],
        "definitie_snippet": (kern_def.get("tekst") or "")[:300],
    }


def build_bundle(record_id: str) -> dict:
    """Genereer bundle voor 1 skeleton-record."""
    skeleton_path = RECORDS_DIR / f"{record_id}.json"
    if not skeleton_path.exists():
        raise FileNotFoundError(f"{skeleton_path}")
    skeleton = json.load(skeleton_path.open())

    meta = skeleton.get("metadata") or {}
    scope = meta.get("scope") or {}
    scope_in = list(scope.get("in") or [])
    relaties = skeleton.get("relaties") or []

    # Pre-fetch chunks per scope.in-query (+ 1 query met naam.primair voor fallback)
    naam_primair = (skeleton.get("naam") or {}).get("primair", record_id)
    queries = list(dict.fromkeys([naam_primair] + scope_in))  # dedupe, name eerst

    bronnen_chunks: dict[str, list] = {}
    for q in queries[:6]:  # cap op 6 queries per record (budget)
        hits = _daemon_search(q, top_k=TOP_K)
        if hits:
            bronnen_chunks[q] = hits

    # Verwante records via relaties.target (compact summary)
    verwante: list[dict] = []
    for r in relaties:
        target = r.get("target", "").split("#")[0]  # strip element-fragment
        if not target:
            continue
        summary = _record_summary(target)
        if summary:
            verwante.append({**summary, "relatie_type": r.get("type", "")})

    return {
        "record_id": record_id,
        "skeleton_path": str(skeleton_path.relative_to(ROOT)),
        "skeleton": skeleton,
        "bronnen_chunks": bronnen_chunks,
        "verwante_records": verwante,
        "n_queries": len(queries),
        "n_chunks_total": sum(len(v) for v in bronnen_chunks.values()),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("record_id", nargs="?")
    ap.add_argument("--cluster", help="Filter op cluster (wave_id-prefix)")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--out-dir", default=str(BUNDLES_DIR))
    args = ap.parse_args()

    BUNDLES_DIR.mkdir(parents=True, exist_ok=True)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.record_id:
        targets = [args.record_id]
    elif args.all or args.cluster:
        all_records = sorted(RECORDS_DIR.glob("*.json"))
        if args.cluster:
            targets = []
            for p in all_records:
                rec = json.load(p.open())
                wave = ((rec.get("metadata") or {}).get("provenance") or {}).get("wave_id") or ""
                if args.cluster in wave:
                    targets.append(p.stem)
        else:
            targets = [p.stem for p in all_records]
    else:
        ap.error("geef record_id of --cluster of --all")

    ok, fail = 0, 0
    for rid in targets:
        try:
            bundle = build_bundle(rid)
            out_path = out_dir / f"{rid}.json"
            out_path.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n")
            print(f"✓ {rid}: {bundle['n_queries']} queries · {bundle['n_chunks_total']} chunks · {len(bundle['verwante_records'])} verwante records")
            ok += 1
        except Exception as e:
            print(f"✗ {rid}: {e}", file=sys.stderr)
            fail += 1
    print(f"\n{ok} OK · {fail} fail")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
