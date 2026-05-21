"""Pre-fetch context bundle voor concept-extract (full 2-pass architectuur).

Verzamelt alle deterministische context voor één fiche zonder LLM:
  - lees_kandidaat: skeleton-context (anchors, edges, motivatie, verwachte_onderdelen)
  - lees_anchor_bundle: alle TDKs voor primary_po (zonder vector-data)
  - lees_record per top-3 v1_hints: content-inspiratie
  - template_voorbeelden: paden naar relevante schema-2.0 mockups + extracts
  - zoek_bronnen (rerank=false): 4 vooraf-bepaalde queries via daemon /zoek-bronnen
      → 3× kind-specifieke queries uit QUERY_TEMPLATES_PER_KIND
      → 1× algemene catch-all query uit fiche-naam + motivatie[:100]

Full 2-pass (default): bundle-script voert queries ZELF via daemon — results staan
in bundle.hits. Agent skipt initiële retrieval volledig en doet alleen 1-3 eigen
gerichte queries met rerank=true voor ⚖️-gaten.

Legacy fallback (--no-full-2pass): queries staan als pending-markers in bundle.
Agent voert ze zelf uit via MCP in pass-2 (oud gedrag).

Output: JSON-bundle in data/extractie/_bundles/<fiche_id>.json (~150-300 KB).

Vereist: daemon actief op localhost:8765 (voor full-2pass modus).
  Start: launchctl kickstart -k gui/$(id -u)/com.certificaid.embedding-daemon

Usage:
    python3 -m tools.extractie.build_context_bundle <fiche_id>
    python3 -m tools.extractie.build_context_bundle <fiche_id> --max-v1 3 --max-onderdelen-queries 3
    python3 -m tools.extractie.build_context_bundle <fiche_id> --no-full-2pass  # legacy mode
"""

import argparse
import json
import sqlite3
import sys
import urllib.request
import urllib.error
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DB_PATH = REPO / "data" / "extractie" / "candidates.sqlite3"
BUNDLES_DIR = REPO / "data" / "extractie" / "_bundles"
EMBED_DAEMON = "http://localhost:8765"

PROGRAMMA_PATH = REPO / "data" / "programma" / "programma.json"
ANCHORS_PATH = REPO / "data" / "programma" / "anchors.json"
EXPERIMENT_DIR = REPO / "content" / "experiment"
RECORDS_DIR = REPO / "data" / "concepten" / "records"

# Velden die te groot of onleesbaar zijn voor de bundle
_ANCHOR_VECTOR_VELDEN = {"vector", "vectors", "embedding", "embeddings", "vector_sha"}


def _http_post(path: str, payload: dict, timeout: int = 60) -> dict:
    """POST naar embedding/RAG-daemon. Return JSON."""
    url = f"{EMBED_DAEMON}{path}"
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def get_kandidaat(fiche_id: str) -> dict:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    r = conn.execute("SELECT * FROM candidates WHERE fiche_id = ?", (fiche_id,)).fetchone()
    conn.close()
    if not r:
        raise SystemExit(f"Kandidaat '{fiche_id}' niet gevonden in DB.")
    out = dict(r)
    # Parse JSON-velden
    for k in ("linked_anchors", "dekt_tdks", "edges_voorgesteld", "depends_on_fiches",
              "v1_hints", "rol_perspectieven", "voorgesteld_door_pos",
              "rationale_per_po", "aanvullings_log", "verwachte_onderdelen"):
        if k in out and out[k]:
            try: out[k] = json.loads(out[k])
            except: pass
    # Strip embedding blob (te groot voor bundle)
    out.pop("embedding", None)
    return out


def _strip_vector_velden(anchor: dict) -> dict:
    """Verwijder vector-data uit een anchor-dict (1024-dim floats zijn onleesbaar en onnodig in bundle)."""
    stripped = {}
    for key, value in anchor.items():
        # Bekende vector-veldnamen
        if key in _ANCHOR_VECTOR_VELDEN:
            continue
        # Veld-keys die eindigen op _vec of _vector
        if key.endswith("_vec") or key.endswith("_vector"):
            continue
        # Anonieme grote float-lijsten (heuristiek: list >= 128 floats)
        if isinstance(value, list) and len(value) >= 128 and all(isinstance(v, float) for v in value[:4]):
            continue
        stripped[key] = value
    return stripped


def get_anchor_bundle(po_id: str) -> list:
    """Lees anchors uit anchors.json filtered op PO-prefix, zonder vector-data."""
    if not ANCHORS_PATH.exists():
        return []
    data = json.loads(ANCHORS_PATH.read_text())
    anchors = data.get("anchors", [])
    gefilterd = [a for a in anchors if str(a.get("po", "")) == po_id or str(a.get("anchor_id", "")).startswith(f"{po_id}.")]
    return [_strip_vector_velden(a) for a in gefilterd]


def get_v1_records(v1_hints: list, max_n: int) -> list:
    """Lees v1.x-records van filesystem voor content-inspiratie."""
    records_dir = REPO / "data" / "concepten" / "records"
    out = []
    for rec_id in v1_hints[:max_n]:
        p = records_dir / f"{rec_id}.json"
        if p.exists():
            try:
                out.append(json.loads(p.read_text()))
            except Exception as e:
                out.append({"id": rec_id, "_load_error": str(e)})
        else:
            out.append({"id": rec_id, "_status": "niet gevonden (mogelijk gearchiveerd)"})
    return out


def _parse_frontmatter_kind(text: str) -> str | None:
    """Haal `kind` of `node_type` uit YAML-frontmatter van een markdown-bestand."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    frontmatter = text[3:end]
    for line in frontmatter.splitlines():
        for key in ("kind:", "node_type:"):
            if line.strip().startswith(key):
                return line.split(":", 1)[1].strip().strip('"').strip("'")
    return None


def get_template_voorbeelden(fiche_id: str, kandidaat_kind: str) -> dict:
    """Verzamel paden naar relevante schema-2.0 mockups en recente extracts.

    Geeft alleen paden terug — geen content. Agent kan ze zelf lezen via Read-tool.
    """
    mockup_paden: list[str] = []
    if EXPERIMENT_DIR.exists():
        voor_kind: list[Path] = []
        overige: list[Path] = []
        for md in sorted(EXPERIMENT_DIR.glob("*.md")):
            try:
                kind = _parse_frontmatter_kind(md.read_text())
            except Exception:
                kind = None
            if kind == kandidaat_kind:
                voor_kind.append(md)
            else:
                overige.append(md)
        # Max 2: eerst zelfde kind, dan aanvullen met overige (nieuwste eerst op naam)
        kandidaten = (voor_kind + overige)[:2]
        mockup_paden = [str(p) for p in kandidaten]

    extract_paden: list[str] = []
    if RECORDS_DIR.exists():
        treffers: list[tuple[float, str]] = []
        for p in RECORDS_DIR.glob("*.json"):
            if p.stem == fiche_id:
                continue  # kandidaat zelf overslaan
            if p.stem.endswith("-debug"):
                continue  # debug-records overslaan
            try:
                data = json.loads(p.read_text())
            except Exception:
                continue
            if data.get("schema_version") == "2.0" and data.get("node_type") == kandidaat_kind:
                treffers.append((p.stat().st_mtime, str(p)))
        treffers.sort(reverse=True)
        extract_paden = [pad for _, pad in treffers[:2]]

    return {
        "mockups_uit_experiment": mockup_paden,
        "recente_extracts_van_zelfde_kind": extract_paden,
    }


# ---------------------------------------------------------------------------
# Kind-specifieke query-templates (2-pass architectuur)
# ---------------------------------------------------------------------------

QUERY_TEMPLATES_PER_KIND: dict[str, list[str]] = {
    "ratio": [
        "{naam} formule berekening componenten",
        "{naam} drempels interpretatie bandbreedte sector",
        "{naam} going-concern audit ISA 570",
    ],
    "fiscale-regeling": [
        "{naam} voorwaarden toepassing",
        "{naam} berekening aftrek tarief WIB92",
        "{naam} uitsluitingen anti-misbruik",
    ],
    "kader": [
        "{naam} definitie scope toepassingsgebied",
        "{naam} rechtsbronnen wettelijk kader",
        "{naam} actoren rollen verantwoordelijkheden",
    ],
    "operatie": [
        "{naam} wettelijke voorwaarden WVV",
        "{naam} procedure stappen bestuursorgaan AV",
        "{naam} boekhoudkundige verwerking MAR",
    ],
    "procedure": [
        "{naam} wettelijke stappen sequentie",
        "{naam} actoren betrokken termijnen",
        "{naam} sanctie niet-naleving",
    ],
    "familie": [
        "{naam} leden onderscheid",
        "{naam} vergelijking kenmerken",
        "{naam} kwalificatie criteria",
    ],
    "begripscluster": [
        "{naam} definitie hoofdcomponenten",
        "{naam} typologie indeling",
        "{naam} juridisch kader bronnen",
    ],
    "instrument": [
        "{naam} kenmerken structuur",
        "{naam} fiscaal regime RV PB venn",
        "{naam} boekhoudkundige verwerking uitgifte verkoop",
    ],
    "balanspost": [
        "{naam} MAR-rubriek componenten",
        "{naam} waarderingsregels CBN",
        "{naam} toelichting jaarrekening fiscaal aspect",
    ],
    "regime": [
        "{naam} voorwaarden toepassing scope",
        "{naam} berekening tarief percentage",
        "{naam} uitsluitingen overgangsregeling",
    ],
}

# Fallback voor onbekende kinds: gebruik naam + motivatie
_FALLBACK_TEMPLATES = [
    "{naam} definitie begrip",
    "{naam} toepassingsgebied voorwaarden",
    "{naam} procedure uitwerking",
]


def _zoek_bronnen_daemon(query: str, top_k: int = 5, rerank: bool = False) -> list:
    """Echte HTTP-call naar daemon /zoek-bronnen endpoint.

    Retourneert lijst van hit-dicts of een fout-dict als daemon niet bereikbaar is.
    """
    try:
        resp = _http_post("/zoek-bronnen", {
            "query": query,
            "top_k": top_k,
            "rerank": rerank,
        }, timeout=30)
        return resp.get("results", [])
    except Exception as exc:
        # Daemon niet bereikbaar — val terug op pending-marker (backwards-compat)
        return [{
            "_pending": f"daemon niet bereikbaar: {exc}",
            "query": query,
            "top_k": top_k,
            "rerank_aanbevolen": rerank,
        }]


def build_queries(kandidaat: dict, max_onderdelen_queries: int) -> list:
    """Genereer kind-specifieke + 1 algemene query.

    Volgorde:
      1-3: kind-specifieke queries uit QUERY_TEMPLATES_PER_KIND (3 per kind)
      4:   algemene catch-all query uit fiche_id + motivatie[:100]

    Als max_onderdelen_queries opgegeven is (legacy), wordt het aantal kind-queries
    ook daarmee begrensd (voor wie de oude aanpak wil).
    """
    naam = kandidaat.get("fiche_id", "").replace("-", " ")
    kind = kandidaat.get("kind", "")
    motivatie_short = (kandidaat.get("motivatie") or "")[:100]

    templates = QUERY_TEMPLATES_PER_KIND.get(kind, _FALLBACK_TEMPLATES)

    out = []
    # Kind-specifieke queries (max 3, begrensd door max_onderdelen_queries)
    max_kind = min(len(templates), max_onderdelen_queries)
    for tmpl in templates[:max_kind]:
        out.append({
            "category": f"kind:{kind}",
            "query": tmpl.format(naam=naam),
        })

    # Algemene catch-all query
    catch_all = f"{naam} {motivatie_short}".strip()
    out.append({
        "category": "algemeen",
        "query": catch_all,
    })

    return out


def _daemon_beschikbaar() -> bool:
    """Controleer snel of de embedding-daemon bereikbaar is."""
    try:
        url = f"{EMBED_DAEMON}/health"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("status") == "ok"
    except Exception:
        return False


def build_bundle(
    fiche_id: str,
    max_v1: int = 3,
    max_onderdelen_queries: int = 3,
    top_k_bronnen: int = 5,
    full_2pass: bool = True,
) -> dict:
    """Hoofdfunctie: bouw complete context-bundle.

    full_2pass=True (default): queries worden uitgevoerd via daemon /zoek-bronnen,
    results staan in bundle — agent skipt initiële retrieval volledig.
    full_2pass=False: backwards-compat — queries staan als strings in bundle,
    agent voert ze zelf uit via MCP in pass-2.
    """
    t0 = time.time()
    kandidaat = get_kandidaat(fiche_id)
    primary_po = kandidaat.get("primary_po", "")
    kandidaat_kind = kandidaat.get("kind", "")

    anchor_bundle = get_anchor_bundle(primary_po)
    v1_records = get_v1_records(kandidaat.get("v1_hints") or [], max_v1)
    template_voorbeelden = get_template_voorbeelden(fiche_id, kandidaat_kind)
    queries = build_queries(kandidaat, max_onderdelen_queries)

    # Bepaal of we de daemon kunnen aanroepen
    if full_2pass and not _daemon_beschikbaar():
        print(
            "⚠ Daemon niet bereikbaar op localhost:8765. "
            "Fallback naar legacy pending-markers (full_2pass=False).",
            file=sys.stderr,
        )
        full_2pass = False

    bronnen_results = []
    n_daemon_calls = 0
    n_hits_totaal = 0

    for q in queries:
        if full_2pass:
            hits = _zoek_bronnen_daemon(q["query"], top_k=top_k_bronnen, rerank=False)
            n_daemon_calls += 1
            n_hits_totaal += sum(1 for h in hits if "_pending" not in h)
        else:
            # Legacy: pending-marker (agent voert query zelf uit)
            hits = [{
                "_pending": "agent voert deze query uit via mcp__certificaid-rag__zoek_bronnen",
                "query": q["query"],
                "top_k": top_k_bronnen,
                "rerank_aanbevolen": False,
            }]

        bronnen_results.append({
            "category": q["category"],
            "query": q["query"],
            "hits": hits,
        })

    # Agent-instructies zijn afhankelijk van full_2pass-modus
    if full_2pass:
        agent_instructies = {
            "summary": (
                "FULL 2-PASS: deze bundle bevat alle deterministische context inclusief "
                "bronnen-resultaten (hits staan al in bronnen_resultaten[].hits). "
                "Doe GEEN initiële retrieval-calls — start direct met schrijven."
            ),
            "bronnen_resultaten_status": "prefetched_via_daemon",
            "skip_queries": (
                "De vooraf-bepaalde queries zijn al uitgevoerd. "
                "Doe GEEN mcp__certificaid-rag__zoek_bronnen voor de queries in bronnen_resultaten[].query. "
                "Doe wel 1-3 eigen gerichte queries met rerank=true voor ⚖️-claims waar bundle gaps heeft."
            ),
            "cap_total_zoek_bronnen": 3,
            "cap_rerank_true": 3,
            "skip": [
                "lees_kandidaat (al hier)",
                "lees_anchor_bundle (al hier)",
                "lees_record op v1_hints (al hier)",
                "exploratory bash (paden staan in deze bundle)",
                "zoek_bronnen voor de 4 vooraf-bepaalde queries (al uitgevoerd — zie bronnen_resultaten[].hits)",
            ],
        }
    else:
        agent_instructies = {
            "summary": (
                "LEGACY 1-PASS: bronnen_resultaten bevat pending-markers. "
                "Voer de N vooraf-bepaalde queries uit via mcp__certificaid-rag__zoek_bronnen(rerank=false)."
            ),
            "bronnen_resultaten_status": "pending_agent_must_execute",
            "uit_te_voeren_queries": (
                "Voer de queries in bronnen_resultaten[].query uit met "
                "mcp__certificaid-rag__zoek_bronnen, telkens rerank=false. "
                "Daarna max 1-2 eigen gerichte queries met rerank=true voor ⚖️-gaten."
            ),
            "cap_total_zoek_bronnen": 7,
            "cap_rerank_true": 2,
            "skip": [
                "lees_kandidaat (al hier)",
                "lees_anchor_bundle (al hier)",
                "lees_record op v1_hints (al hier)",
                "exploratory bash (paden staan in deze bundle)",
            ],
        }

    bundle = {
        "fiche_id": fiche_id,
        "built_at_iso": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "build_duration_sec": round(time.time() - t0, 2),
        "full_2pass": full_2pass,
        "params": {
            "max_v1": max_v1,
            "max_onderdelen_queries": max_onderdelen_queries,
            "top_k_bronnen": top_k_bronnen,
        },
        "kandidaat": kandidaat,
        "anchor_bundle": anchor_bundle,
        "v1_inspiratie": v1_records,
        "template_voorbeelden": template_voorbeelden,
        "bronnen_resultaten": bronnen_results,
        "agent_instructies": agent_instructies,
    }
    return bundle


def main():
    ap = argparse.ArgumentParser(description="Build context bundle voor 2-pass extract.")
    ap.add_argument("fiche_id")
    ap.add_argument("--max-v1", type=int, default=3)
    ap.add_argument("--max-onderdelen-queries", type=int, default=3,
                    help="Max aantal kind-specifieke queries (default 3; gebruikt QUERY_TEMPLATES_PER_KIND)")
    ap.add_argument("--top-k-bronnen", type=int, default=5)
    ap.add_argument("--no-full-2pass", action="store_true",
                    help="Gebruik legacy pending-markers i.p.v. echte daemon-calls (backwards-compat)")
    ap.add_argument("--out", help="Output-pad (default: data/extractie/_bundles/<fiche_id>.json)")
    args = ap.parse_args()

    BUNDLES_DIR.mkdir(parents=True, exist_ok=True)
    out_path = Path(args.out) if args.out else (BUNDLES_DIR / f"{args.fiche_id}.json")

    full_2pass = not args.no_full_2pass
    bundle = build_bundle(
        args.fiche_id,
        args.max_v1,
        args.max_onderdelen_queries,
        args.top_k_bronnen,
        full_2pass=full_2pass,
    )
    out_path.write_text(json.dumps(bundle, ensure_ascii=False, indent=2))

    # Stats naar stderr
    size_kb = out_path.stat().st_size / 1024
    n_bron_hits = sum(
        sum(1 for h in b.get("hits", []) if "_pending" not in h)
        for b in bundle["bronnen_resultaten"]
    )
    n_pending = sum(
        sum(1 for h in b.get("hits", []) if "_pending" in h)
        for b in bundle["bronnen_resultaten"]
    )
    modus = "full-2pass" if bundle.get("full_2pass") else "legacy-pending"
    print(f"✓ Bundle geschreven: {out_path}", file=sys.stderr)
    print(f"  modus: {modus} · size: {size_kb:.1f} KB · build-tijd: {bundle['build_duration_sec']}s", file=sys.stderr)
    print(f"  kandidaat: {bundle['kandidaat']['kind']}, primary_po={bundle['kandidaat']['primary_po']}", file=sys.stderr)
    print(f"  anchors: {len(bundle['anchor_bundle'])} · v1: {len(bundle['v1_inspiratie'])} · bron-queries: {len(bundle['bronnen_resultaten'])} ({n_bron_hits} hits, {n_pending} pending)", file=sys.stderr)


if __name__ == "__main__":
    main()
