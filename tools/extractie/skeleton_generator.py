"""Skeleton-JSON-generator voor schema 2.2 concept-records.

ADR-035 (schema 2.2): vanuit cluster-spec YAML genereert dit script
N schema-2.2-valide JSON-skeleton-records in data/concepten/records/.

Per record:
- naam (primair + synoniemen + afkorting)
- concept_type (uit cluster-spec)
- metadata.ankers (uit cluster-spec PO-mapping)
- metadata.scope.in[] + scope.out[] (extractie-guidance VOORAF)
- inhoud.kern.definitie (placeholder, agent vult in)
- inhoud.elementen[] (sub-concepten met scope per element)
- inhoud.geldigheid (voor regimes/regelingen)
- inhoud.accountant_perspectieven[] (placeholders per cluster-default)
- relaties[] (cross-cluster hints uit cluster-spec)
- provenance (model: skeleton-generator, wave_id: cluster-naam)

Gebruik:
    python3 -m tools.extractie.skeleton_generator <cluster-spec.yaml>
    python3 -m tools.extractie.skeleton_generator --all  # alle clusters in tools/extractie/cluster-specs/
    python3 -m tools.extractie.skeleton_generator --validate  # check 2.2-conformiteit

Cluster-spec YAML-shape:
    cluster: boekhouding
    discipline: boekhouding
    po_mapping: ["1.1", "1.2"]
    bronnen_pin:
      - WER Boek III
      - KB 29-04-2019
    records:
      - id: jaarrekening
        naam:
          primair: "Jaarrekening"
          synoniemen: [...]
          afkorting: "JR"
        concept_type: kader
        ankers: ["1.1.II.S", "1.2.taak.1"]
        scope_in:
          - "Balansschema (volledig/verkort/micro)"
          - "Resultatenrekening (ROW)"
          - "Toelichting + sociale balans"
        scope_out:
          - "Geconsolideerde jaarrekening — zie geconsolideerde-jaarrekening"
          - "IFRS-rapportering — zie ifrs"
        elementen:
          - id: balansschema
            naam_primair: "Balansschema"
            inhoud_type: subconcept
          - id: openbaarmaking
            naam_primair: "Openbaarmaking jaarrekening"
            inhoud_type: stap
            scope_in: ["NBB-neerlegging 30-dagen + taksen"]
        cross_relaties:
          - target: belgisch-boekhoudrecht
            type: valt-onder
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import logging
import sys
from pathlib import Path

import yaml  # type: ignore

logger = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parents[2]
RECORDS_DIR = ROOT / "data" / "concepten" / "records"
RECORDS_V21_DIR = ROOT / "data" / "concepten" / "records-v21"
SPECS_DIR = ROOT / "tools" / "extractie" / "cluster-specs"
SCHEMA_PATH = ROOT / "data" / "concepten" / "schema-2.2.schema.json"


def _now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _build_naam(spec_naam: dict | str) -> dict:
    """Naam-blok uit spec. Spec kan string of dict zijn."""
    if isinstance(spec_naam, str):
        return {"primair": spec_naam}
    blok = {"primair": spec_naam["primair"]}
    if "afkorting" in spec_naam:
        blok["afkorting"] = spec_naam["afkorting"]
    if "synoniemen" in spec_naam:
        blok["synoniemen"] = list(spec_naam["synoniemen"])
    if "vertaling" in spec_naam:
        blok["vertaling"] = dict(spec_naam["vertaling"])
    return blok


def _build_inhoud(spec: dict, default_definitie: str) -> dict:
    """Bouw inhoud-blok uit spec (kern + subconcepten + bouwstenen + gebruikscontext). Schema 2.2."""
    inhoud = {
        "kern": {
            "definitie": {
                "tekst": spec.get("definitie_placeholder", default_definitie),
                "grondslag": {
                    "confidence": "verondersteld",
                    "bronnen": [{"type": "ai_model", "naam": "skeleton-generator", "datum": _now_iso()[:10]}],
                },
            }
        }
    }
    if "geldigheid" in spec or "gebruikscontext" in spec:
        gc = dict(spec.get("gebruikscontext") or {})
        if "geldigheid" in spec:
            gc["geldigheid"] = dict(spec["geldigheid"])
        inhoud["gebruikscontext"] = gc
    if "subconcepten" in spec:
        inhoud["subconcepten"] = [_build_subconcept(sub) for sub in spec["subconcepten"]]
    if "bouwstenen" in spec:
        inhoud["bouwstenen"] = [_build_bouwsteen(b) for b in spec["bouwstenen"]]
    return inhoud


def _build_subconcept(sub_spec: dict) -> dict:
    """Sub-concept = mini-concept met inhoud-shape (recursief). Schema 2.2: geen perspectieven/scope/metadata."""
    return {
        "id": sub_spec["id"],
        "naam": _build_naam(sub_spec.get("naam_primair") or sub_spec.get("naam") or sub_spec["id"]),
        "concept_type": sub_spec.get("concept_type", "kader"),
        "inhoud": _build_inhoud(sub_spec, f"⏳ Subconcept te beschrijven: {sub_spec['id']}"),
    }


def _build_bouwsteen(b_spec: dict) -> dict:
    """Bouwsteen = platte content-item (begrip/stap/regel/formule/...). Geen subconcept als inhoud_type."""
    bs = {
        "id": b_spec["id"],
        "naam": _build_naam(b_spec.get("naam_primair") or b_spec.get("naam") or b_spec["id"]),
        "inhoud_type": b_spec.get("inhoud_type", "begrip"),
        "kern": {
            "definitie": {
                "tekst": b_spec.get("definitie_placeholder", f"⏳ Bouwsteen te beschrijven: {b_spec['id']}"),
                "grondslag": {
                    "confidence": "verondersteld",
                    "bronnen": [{"type": "ai_model", "naam": "skeleton-generator", "datum": _now_iso()[:10]}],
                },
            }
        },
    }
    if "subconcepten" in b_spec or "bouwstenen" in b_spec or "gebruikscontext" in b_spec or "geldigheid" in b_spec:
        bs["inhoud"] = _build_inhoud(b_spec, "")
        # Verwijder dubbele kern (al in bouwsteen-niveau)
        bs["inhoud"].pop("kern", None)
    return bs


def _build_scope_out(out_spec: list) -> list:
    """scope.out: lijst van objects met topic/richting/ref."""
    result = []
    for item in out_spec:
        if isinstance(item, str):
            # Backwards-compat: parse "topic — zie record-id" als moet-verwijzen
            if " — zie " in item:
                topic, ref = item.split(" — zie ", 1)
                result.append({"topic": topic.strip(), "richting": "moet-verwijzen", "ref": ref.strip()})
            else:
                result.append({"topic": item, "richting": "mag-verwijzen"})
        else:
            result.append(dict(item))
    return result


def _build_relatie(rel_spec: dict) -> dict:
    """Top-level relatie-skeleton. Schema 2.2: grondslag optioneel — agent vult bij beschrijven-operatie."""
    rel = {
        "type": rel_spec.get("type", "vergelijkbaar_met"),
        "target": rel_spec["target"],
    }
    # Extra velden uit spec (gelijkenissen/verschillen/etc voor vergelijkbaar_met)
    for k, v in rel_spec.items():
        if k not in ("type", "target"):
            rel[k] = v
    return rel


def _build_record(rec_spec: dict, cluster_spec: dict) -> dict:
    """Bouw een schema-2.2-skeleton-record uit cluster-spec + record-spec."""
    rid = rec_spec["id"]
    cluster_name = cluster_spec.get("cluster", "onbekend")
    wave_id = f"skeleton-{cluster_name}-{_now_iso()[:10]}"

    record = {
        "id": rid,
        "naam": _build_naam(rec_spec.get("naam") or rid.replace("-", " ").title()),
        "concept_type": rec_spec.get("concept_type", "kader"),
        "metadata": {
            "schema_version": "2.2",
            "status": "skeleton",
            "categorieen": list(rec_spec.get("categorieen") or ["kader"]),
            "ankers": list(rec_spec.get("ankers") or []),
            "provenance": {
                "model": "skeleton-generator",
                "wave_id": wave_id,
                "iteratie": "skeleton-v1",
            },
            "changelog": [
                {
                    "operatie": "skeleton",
                    "timestamp": _now_iso(),
                    "model": "skeleton-generator",
                    "wave_id": wave_id,
                    "wijziging": "Skeleton-record aangemaakt uit cluster-spec",
                }
            ],
        },
        "inhoud": _build_inhoud(rec_spec, f"⏳ Te beschrijven door agent in cluster-extractie van {cluster_name}."),
        "relaties": [],
    }

    # scope op record-niveau (alleen top — niet recursief op sub-concepten)
    if "scope_in" in rec_spec or "scope_out" in rec_spec:
        record["metadata"]["scope"] = {}
        if "scope_in" in rec_spec:
            record["metadata"]["scope"]["in"] = list(rec_spec["scope_in"])
        if "scope_out" in rec_spec:
            record["metadata"]["scope"]["out"] = _build_scope_out(rec_spec["scope_out"])

    # accountant_perspectieven TOP-only (record-niveau) — schema 2.2 refactor
    if "accountant_perspectieven" in rec_spec:
        record["accountant_perspectieven"] = []
        for idx, persp_spec in enumerate(rec_spec["accountant_perspectieven"]):
            positie = persp_spec.get("positie", "eigen-kantoor")
            persp = {
                "id": persp_spec.get("id", f"perspectief-{idx+1}-{positie}"),
                "naam": _build_naam(persp_spec.get("naam") or positie.replace("-", " ").title()),
                "rollen": [],
            }
            if "context" in persp_spec:
                persp["intro"] = persp_spec["context"]
            for rol_spec in persp_spec.get("rollen", []):
                if isinstance(rol_spec, str):
                    persp["rollen"].append({"rol": rol_spec, "elementen": []})
                else:
                    persp["rollen"].append(
                        {
                            "rol": rol_spec["rol"],
                            "elementen": [_build_bouwsteen(e) for e in rol_spec.get("elementen", [])],
                        }
                    )
            record["accountant_perspectieven"].append(persp)

    # relaties (cross-cluster + binnen-cluster hints)
    for rel_spec in rec_spec.get("cross_relaties") or []:
        record["relaties"].append(_build_relatie(rel_spec))
    for rel_spec in rec_spec.get("relaties") or []:
        record["relaties"].append(_build_relatie(rel_spec))

    return record


def generate_cluster(spec_path: Path, output_dir: Path = RECORDS_DIR, dry_run: bool = False) -> dict:
    """Genereer alle skeleton-records uit één cluster-spec YAML.

    Retour: stats-dict {created, skipped, failed}.
    """
    spec = yaml.safe_load(spec_path.read_text())
    cluster_name = spec.get("cluster", spec_path.stem)
    stats = {"created": 0, "skipped": 0, "failed": 0, "cluster": cluster_name}

    output_dir.mkdir(parents=True, exist_ok=True)

    for rec_spec in spec.get("records") or []:
        rid = rec_spec["id"]
        out_path = output_dir / f"{rid}.json"

        if out_path.exists() and not dry_run:
            logger.warning("SKIP: %s bestaat al — niet overschrijven (gebruik --force)", rid)
            stats["skipped"] += 1
            continue

        try:
            record = _build_record(rec_spec, spec)
            if dry_run:
                print(f"DRY-RUN {rid}:")
                print(json.dumps(record, indent=2, ensure_ascii=False)[:500])
                print()
            else:
                out_path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
            stats["created"] += 1
        except Exception as exc:
            logger.error("FAIL %s: %s", rid, exc)
            stats["failed"] += 1

    return stats


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", nargs="?", help="Cluster-spec YAML pad")
    parser.add_argument("--all", action="store_true", help="Alle YAMLs in tools/extractie/cluster-specs/")
    parser.add_argument("--dry-run", action="store_true", help="Toon output, schrijf niet")
    parser.add_argument("--force", action="store_true", help="Overschrijf bestaande records")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    if args.all:
        if not SPECS_DIR.exists():
            print(f"FOUT: {SPECS_DIR} bestaat niet")
            return 1
        spec_files = sorted(SPECS_DIR.glob("*.yaml")) + sorted(SPECS_DIR.glob("*.yml"))
        if not spec_files:
            print(f"FOUT: geen YAMLs in {SPECS_DIR}")
            return 1
    elif args.spec:
        spec_files = [Path(args.spec)]
    else:
        parser.error("geef <spec> of --all")

    totals = {"created": 0, "skipped": 0, "failed": 0}
    for sf in spec_files:
        print(f"\n=== {sf.name} ===")
        stats = generate_cluster(sf, dry_run=args.dry_run)
        print(f"  cluster: {stats['cluster']}: created={stats['created']} skipped={stats['skipped']} failed={stats['failed']}")
        for k in totals:
            totals[k] += stats.get(k, 0)

    print(f"\n=== TOTAAL ===")
    print(f"created={totals['created']} skipped={totals['skipped']} failed={totals['failed']}")
    return 0 if totals["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
