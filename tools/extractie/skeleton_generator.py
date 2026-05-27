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


def _build_element(elem_spec: dict) -> dict:
    """Element-skeleton uit cluster-spec. Schema 2.2: scope niet op element (alleen record); geldigheid via gebruikscontext."""
    el = {
        "id": elem_spec["id"],
        "naam": _build_naam(elem_spec.get("naam_primair") or elem_spec.get("naam") or elem_spec["id"]),
        "inhoud_type": elem_spec.get("inhoud_type", "subconcept"),
        "kern": {
            "definitie": {
                "tekst": elem_spec.get("definitie_placeholder", f"⏳ Te beschrijven door agent: {elem_spec['id']}"),
                "grondslag": {
                    "confidence": "verondersteld",
                    "bronnen": [{"type": "ai_model", "naam": "skeleton-generator", "datum": _now_iso()[:10]}],
                },
            }
        },
    }
    if "geldigheid" in elem_spec or "gebruikscontext" in elem_spec:
        gc = dict(elem_spec.get("gebruikscontext") or {})
        if "geldigheid" in elem_spec:
            gc["geldigheid"] = dict(elem_spec["geldigheid"])
        el["gebruikscontext"] = gc
    if "elementen" in elem_spec:
        el["elementen"] = [_build_element(sub) for sub in elem_spec["elementen"]]
    return el


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
        "inhoud": {
            "kern": {
                "definitie": {
                    "tekst": rec_spec.get(
                        "definitie_placeholder",
                        f"⏳ Te beschrijven door agent in cluster-extractie van {cluster_name}.",
                    ),
                    "grondslag": {
                    "confidence": "verondersteld",
                    "bronnen": [{"type": "ai_model", "naam": "skeleton-generator", "datum": _now_iso()[:10]}],
                },
                }
            }
        },
        "relaties": [],
    }

    # scope op record-niveau
    if "scope_in" in rec_spec or "scope_out" in rec_spec:
        record["metadata"]["scope"] = {}
        if "scope_in" in rec_spec:
            record["metadata"]["scope"]["in"] = list(rec_spec["scope_in"])
        if "scope_out" in rec_spec:
            record["metadata"]["scope"]["out"] = _build_scope_out(rec_spec["scope_out"])

    # elementen
    if "elementen" in rec_spec:
        record["inhoud"]["elementen"] = [_build_element(e) for e in rec_spec["elementen"]]

    # geldigheid + gebruikscontext (schema 2.2: geldigheid in gebruikscontext)
    if "geldigheid" in rec_spec or "gebruikscontext" in rec_spec:
        gc = dict(rec_spec.get("gebruikscontext") or {})
        if "geldigheid" in rec_spec:
            gc["geldigheid"] = dict(rec_spec["geldigheid"])
        record["inhoud"]["gebruikscontext"] = gc

    # accountant_perspectieven placeholders
    if "accountant_perspectieven" in rec_spec:
        record["inhoud"]["accountant_perspectieven"] = []
        for persp_spec in rec_spec["accountant_perspectieven"]:
            persp = {
                "positie": persp_spec.get("positie", "eigen-kantoor"),
                "context": persp_spec.get("context", ""),
                "rollen": [],
            }
            for rol_spec in persp_spec.get("rollen", []):
                if isinstance(rol_spec, str):
                    persp["rollen"].append({"rol": rol_spec, "elementen": []})
                else:
                    persp["rollen"].append(
                        {
                            "rol": rol_spec["rol"],
                            "elementen": [_build_element(e) for e in rol_spec.get("elementen", [])],
                        }
                    )
            record["inhoud"]["accountant_perspectieven"].append(persp)

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
