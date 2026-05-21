"""
Kwaliteits-audit voor schema 2.0 concept-records.

Scoort elk record op 7 kwaliteit-dimensies (0-10 elk) en geeft een gewogen
totaalscore. Ontworpen als betere proxy voor kwaliteit dan ⚠️-percentage,
dat agents kunnen "gamen" door geen ⚠️ te zetten.

CLI:
    python3 -m tools.extractie.kwaliteits_audit <record-id-of-pad>
    python3 -m tools.extractie.kwaliteits_audit --all
    python3 -m tools.extractie.kwaliteits_audit --wave <wave-id>
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Configuratie
# ---------------------------------------------------------------------------

RECORDS_DIR = Path(__file__).parent.parent.parent / "data" / "concepten" / "records"

# node_types waarvoor cross-PO-breedte relevant kan zijn (niet automatisch verwacht)
# Kader/fiscale-regeling/operatie kunnen multi-PO zijn, maar zijn het niet altijd
POTENTIEEL_MULTI_PO_NODE_TYPES = {"instrument", "operatie", "regime", "fiscale-regeling", "kader"}

# Gewichten per dimensie (optellen tot 1.0)
GEWICHTEN = {
    "bron_specificiteit": 0.20,
    "concrete_elementen": 0.18,
    "cell_fill_matrix": 0.17,
    "slot_sections": 0.15,
    "strategisch_advies": 0.12,
    "cross_po_completeness": 0.08,
    "hallucinatie_vlag": 0.10,
}

# Specifieke bron-pattern: art., par., §, Bijlage + nummer
SPECIFIEKE_BRON_PATTERN = re.compile(
    r"""(
        art\.?\s*\d+(/\d+)?       # art. 205/1  |  art 47
        | par\.?\s*\d+            # par. 13
        | §\s*\d+                 # §3
        | \bBijlage\s+\d+         # Bijlage 1
        | \balinea\s+\d+          # alinea 2
        | \blid\s+\d+             # lid 2
    )""",
    re.VERBOSE | re.IGNORECASE,
)

# Confidence-waarden die als "inhoudsclaim" tellen
CLAIM_CONFIDENCES = {"grounded", "inferred", "te_verifieren", "vuistregel"}


# ---------------------------------------------------------------------------
# Hulpfuncties — recursief doorlopen
# ---------------------------------------------------------------------------

def _iter_dict_values(obj: Any):
    """Yield (path, dict) voor elke dict in de boom, behalve _provenance."""
    if isinstance(obj, dict):
        yield obj
        for k, v in obj.items():
            if k != "_provenance":
                yield from _iter_dict_values(v)
    elif isinstance(obj, list):
        for item in obj:
            yield from _iter_dict_values(item)


def _collect_claims(obj: Any) -> list[dict]:
    """
    Verzamel alle claims: dict-objecten die een 'confidence'-veld bevatten.
    Geeft list van dicts met keys: confidence, source_str.
    """
    claims = []
    for d in _iter_dict_values(obj):
        conf = d.get("confidence")
        if conf and str(conf) in CLAIM_CONFIDENCES:
            source = d.get("source") or d.get("bron") or ""
            if isinstance(source, dict):
                source_str = source.get("short", "") or source.get("full", "") or ""
            elif isinstance(source, str):
                source_str = source
            else:
                source_str = ""
            claims.append({"confidence": str(conf), "source": source_str})
    return claims


def _collect_weergaven(obj: Any) -> list[dict]:
    """Verzamel alle weergaven-items (uit alle niveaus)."""
    weergaven = []
    for d in _iter_dict_values(obj):
        for w in d.get("weergaven", []):
            if isinstance(w, dict):
                weergaven.append(w)
    return weergaven


def _count_text_numbers(obj: Any) -> int:
    """Tel cijfers/datums/percentages in tekstuele content."""
    text = json.dumps(obj, ensure_ascii=False)
    # Match: percentages, geldgetallen, datums, wetsartikel-nummers als cijferreeksen
    matches = re.findall(
        r"""\b\d+([.,]\d+)?\s*%          # percentages
            |\b\d{4}\b                    # jaren/datums
            |€\s*\d+                      # geldgetallen
            |\b\d+/\d+                    # breukachtige art-nrs
        """,
        text,
        re.VERBOSE,
    )
    return len(matches)


def _count_vuistregels(obj: Any) -> tuple[int, int]:
    """
    Geef (vuistregel_count, totaal_claims_count).
    vuistregel = confidence == 'vuistregel' OF element met inhoud_type == 'vuistregel'.
    """
    text = json.dumps(obj, ensure_ascii=False)
    vuistregel_confidence = text.count('"confidence": "vuistregel"') + text.count("'confidence': 'vuistregel'")
    vuistregel_inhoud_type = text.count('"inhoud_type": "vuistregel"') + text.count('"type": "vuistregel"')
    vuistregel_count = max(vuistregel_confidence, vuistregel_inhoud_type)

    all_claims = _collect_claims(obj)
    return vuistregel_count, max(len(all_claims), 1)


def _get_node_type(record: dict) -> str:
    """Haal node_type op; valt terug op 'kind' als node_type afwezig."""
    return record.get("node_type") or record.get("kind") or ""


def _is_cross_po(record: dict) -> bool:
    """
    Bepaal of het record cross-PO is.
    cross_po kan zijn: True, False, 0, 1, None, [], ['2.3', '4.0'], etc.
    """
    val = record.get("cross_po")
    if val is None:
        return False
    if isinstance(val, bool):
        return val
    if isinstance(val, int):
        return bool(val)
    if isinstance(val, list):
        return len(val) > 0
    return bool(val)


def _collect_cells(record: dict) -> list[dict]:
    """
    Verzamel rol×perspectief-cellen uit:
    - rol_van_de_accountant.perspectieven[].rollen[]
    - perspectieven[].rollen[]
    Elk cel bevat: perspectief_id, rol, elementen_count
    """
    cells = []

    # Stijl A: rol_van_de_accountant.perspectieven[].rollen[].elementen[]
    rva = record.get("rol_van_de_accountant", {})
    if isinstance(rva, dict):
        for persp in rva.get("perspectieven", []):
            perspectief_id = persp.get("perspectief_id") or persp.get("actor", "?")
            for rol_obj in persp.get("rollen", []):
                rol = rol_obj.get("rol", "?")
                # elementen of onderdelen
                elementen = rol_obj.get("elementen", rol_obj.get("onderdelen", []))
                cells.append({
                    "perspectief_id": perspectief_id,
                    "rol": rol,
                    "elementen_count": len(elementen) if isinstance(elementen, list) else 0,
                })

    # Stijl B: perspectieven[].rollen[].onderdelen[]  (liquidatiereserve-stijl)
    perspectieven = record.get("perspectieven", [])
    for persp in perspectieven:
        perspectief_id = persp.get("perspectief_id") or persp.get("naam", "?")
        for rol_obj in persp.get("rollen", []):
            rol = rol_obj.get("rol") or rol_obj.get("label", "?")
            onderdelen = rol_obj.get("onderdelen", rol_obj.get("elementen", []))
            cells.append({
                "perspectief_id": perspectief_id,
                "rol": rol,
                "elementen_count": len(onderdelen) if isinstance(onderdelen, list) else 0,
            })

    # Stijl C: rol_van_de_accountant als dict van rol → perspectieven (groepbijdrage-stijl,
    # maar dan per actor-perspectieven met taken-lijst)
    if not cells and isinstance(rva, dict):
        for persp_list in rva.get("perspectieven", []):
            actor = persp_list.get("actor", "?")
            for rol_obj in persp_list.get("rollen", []):
                rol = rol_obj.get("rol", "?")
                taken = rol_obj.get("taken", [])
                cells.append({
                    "perspectief_id": actor,
                    "rol": rol,
                    "elementen_count": len(taken) if isinstance(taken, list) else 0,
                })

    return cells


# ---------------------------------------------------------------------------
# Dimensie-scorings-functies
# ---------------------------------------------------------------------------

def score_bron_specificiteit(record: dict) -> tuple[float, str]:
    """
    Bron-specificiteit: % claims met specifieke bron-referentie (art./par./§/Bijlage + nr).
    10/10 = 90%+ claims hebben specifieke ref.
    Grounded claims zonder bron wegen zwaarder dan inferred.
    """
    claims = _collect_claims(record)
    if not claims:
        return 5.0, "geen claims gevonden (neutraal)"

    grounded_met_bron = 0
    grounded_totaal = 0
    inferred_met_bron = 0
    inferred_totaal = 0

    for c in claims:
        conf = c["confidence"]
        heeft_bron = bool(c["source"] and SPECIFIEKE_BRON_PATTERN.search(c["source"]))
        if conf == "grounded":
            grounded_totaal += 1
            if heeft_bron:
                grounded_met_bron += 1
        elif conf == "inferred":
            inferred_totaal += 1
            if heeft_bron:
                inferred_met_bron += 1

    # Bron-specificiteit weegt vooral grounded claims
    totaal_gewogen = grounded_totaal * 2 + inferred_totaal
    met_bron_gewogen = grounded_met_bron * 2 + inferred_met_bron

    if totaal_gewogen == 0:
        return 5.0, "geen grounded/inferred claims"

    ratio = met_bron_gewogen / totaal_gewogen
    score = min(10.0, ratio * 11.1)  # 90% → 10/10

    detail = (
        f"{grounded_met_bron}/{grounded_totaal} grounded + "
        f"{inferred_met_bron}/{inferred_totaal} inferred met specifieke art-/par-ref"
    )
    return round(score, 1), detail


def score_concrete_elementen(record: dict) -> tuple[float, str]:
    """
    Concrete elementen: ratio non-proza weergaven + aanwezigheid van cijfers/datums.
    10/10 = >50% non-proza weergaven EN veel cijfers.
    """
    weergaven = _collect_weergaven(record)
    totaal = len(weergaven)
    non_proza = sum(
        1 for w in weergaven
        if w.get("type", w.get("inhoud_type", "")) not in ("proza", "tekst", "")
    )

    # Tellen van concrete cijfers in de hele record-tekst
    cijfer_count = _count_text_numbers(record)

    if totaal == 0:
        weergave_score = 0.0
        weergave_detail = "geen weergaven"
    else:
        ratio = non_proza / totaal
        weergave_score = min(10.0, ratio * 20.0)  # 50% → 10/10
        weergave_detail = f"{non_proza}/{totaal} non-proza weergaven"

    # Cijfer-bonus: meer dan 20 concrete cijfers/datums/percentages
    cijfer_score = min(10.0, cijfer_count / 2.0)  # 20+ → 10/10
    cijfer_detail = f"{cijfer_count} concrete cijfers/datums/percentages in tekst"

    # Gemiddelde van weergaven-score en cijfer-score
    score = (weergave_score * 0.6 + cijfer_score * 0.4)
    detail = f"{weergave_detail}; {cijfer_detail}"
    return round(score, 1), detail


def score_cell_fill_matrix(record: dict) -> tuple[float, str]:
    """
    Cell-fill matrix: hoeveel rol×perspectief-cellen zijn gevuld met ≥2 elementen?
    10/10 = ≥3 cellen EN ≥50% cellen hebben ≥2 elementen.
    """
    cells = _collect_cells(record)

    if not cells:
        return 0.0, "geen cellen gevonden (geen perspectieven/rollen)"

    cellen_met_2plus = sum(1 for c in cells if c["elementen_count"] >= 2)
    totaal_cellen = len(cells)

    if totaal_cellen == 0:
        return 0.0, "0 cellen"

    # Score componenten
    heeft_genoeg_cellen = totaal_cellen >= 3  # minimum drempel
    ratio_gevuld = cellen_met_2plus / totaal_cellen

    if not heeft_genoeg_cellen:
        cel_score = totaal_cellen / 3.0 * 5.0  # max 5/10 als <3 cellen
    else:
        cel_score = 5.0 + ratio_gevuld * 5.0  # 5-10 op basis van fill-ratio

    detail = f"{cellen_met_2plus}/{totaal_cellen} cellen met ≥2 elementen"
    return round(cel_score, 1), detail


def score_slot_sections(record: dict) -> tuple[float, str]:
    """
    Slot-sections compleet: veelvoorkomende_verwarringen + familie/alternatieven + bronnen.
    10/10 = alle 3 aanwezig MET inhoud.
    """
    onderdelen = []

    # 1. veelvoorkomende_verwarringen
    vv = record.get("veelvoorkomende_verwarringen")
    if isinstance(vv, list) and len(vv) > 0:
        onderdelen.append(f"verwarringen ({len(vv)} items)")
    elif isinstance(vv, dict) and any(vv.values()):
        onderdelen.append("verwarringen (dict)")
    else:
        onderdelen.append("❌ verwarringen ontbreekt")

    # 2. familie_en_alternatieven / alternatieven_zelfde_doel
    alternatieven = record.get("familie_en_alternatieven") or record.get("alternatieven_zelfde_doel")
    if alternatieven:
        count = len(alternatieven) if isinstance(alternatieven, list) else 1
        onderdelen.append(f"alternatieven ({count})")
    else:
        onderdelen.append("❌ alternatieven ontbreekt")

    # 3. bronnen_en_verwijzingen
    bronnen = record.get("bronnen_en_verwijzingen", {})
    if isinstance(bronnen, dict):
        grounded = bronnen.get("grounded", [])
        te_verif = bronnen.get("te_verifieren", [])
        if grounded or te_verif:
            onderdelen.append(
                f"bronnen ({len(grounded)} grounded, {len(te_verif)} te_verifieren)"
            )
        else:
            onderdelen.append("❌ bronnen leeg")
    elif isinstance(bronnen, list) and bronnen:
        onderdelen.append(f"bronnen ({len(bronnen)} items)")
    else:
        onderdelen.append("❌ bronnen ontbreekt")

    # Score op basis van aanwezige secties
    aanwezig = sum(1 for o in onderdelen if not o.startswith("❌") and "n.v.t." not in o)
    totaal_vereist = sum(1 for o in onderdelen if "n.v.t." not in o)

    if totaal_vereist == 0:
        score = 5.0
    else:
        score = (aanwezig / totaal_vereist) * 10.0

    detail = " | ".join(onderdelen)
    return round(score, 1), detail


def score_strategisch_advies(record: dict) -> tuple[float, str]:
    """
    Strategisch advies: hoofdrisico + hoofdvoordeel aanwezig + vuistregel-ratio 10-25%.
    10/10 = beide aanwezig EN vuistregels 10-25%.
    """
    text = json.dumps(record, ensure_ascii=False)

    # Zoek hoofdrisico/hoofdvoordeel in wanneer_van_toepassing
    wvt = record.get("wanneer_van_toepassing", {})
    heeft_hoofdrisico = bool(
        (isinstance(wvt, dict) and wvt.get("hoofdrisico"))
        or "hoofdrisico" in text
    )
    heeft_hoofdvoordeel = bool(
        (isinstance(wvt, dict) and wvt.get("hoofdvoordeel"))
        or "hoofdvoordeel" in text
    )

    # Vuistregels ratio
    vuistregel_count, totaal_claims = _count_vuistregels(record)
    if totaal_claims > 0:
        vuistregel_ratio = vuistregel_count / totaal_claims
    else:
        vuistregel_ratio = 0.0

    # Score
    aanwezig_score = 0.0
    if heeft_hoofdrisico:
        aanwezig_score += 3.0
    if heeft_hoofdvoordeel:
        aanwezig_score += 3.0

    # Vuistregel-ratio score: 10-25% optimaal
    if vuistregel_ratio == 0:
        vuist_score = 0.0
    elif vuistregel_ratio < 0.10:
        vuist_score = vuistregel_ratio / 0.10 * 2.5  # 0-2.5 bij <10%
    elif vuistregel_ratio <= 0.25:
        vuist_score = 4.0  # optimale range
    else:
        # Te veel vuistregels (overmatig)
        vuist_score = max(0.0, 4.0 - (vuistregel_ratio - 0.25) * 10.0)

    score = min(10.0, aanwezig_score + vuist_score)
    detail = (
        f"hoofdrisico={'ja' if heeft_hoofdrisico else 'nee'}, "
        f"hoofdvoordeel={'ja' if heeft_hoofdvoordeel else 'nee'}, "
        f"vuistregels={vuistregel_count}/{totaal_claims} "
        f"({vuistregel_ratio:.0%})"
    )
    return round(score, 1), detail


def score_cross_po_completeness(record: dict) -> tuple[float, str]:
    """
    Cross-PO completeness: scoort op basis van feitelijke anchor-spreiding.
    - Als cross_po=True: verwacht anchors van ≥2 PO's; ≥3 PO's = 10/10.
    - Als cross_po=False/None EN node_type NIET potentieel-multi-PO: neutraal (5/10).
    - Als cross_po=False/None maar node_type IS potentieel-multi-PO: matig (basis 5/10 max).
    10/10 = cross_po=True EN anchors van ≥3 PO's.
    """
    is_cross = _is_cross_po(record)
    cross_po_raw = record.get("cross_po")
    linked_anchors = record.get("linked_anchors", [])
    node_type = _get_node_type(record)

    # Unieke PO's uit anchors (eerste twee delen: "2.3" uit "2.3.II.B")
    unique_pos = set()
    for anchor in linked_anchors:
        parts = str(anchor).split(".")
        if len(parts) >= 2:
            unique_pos.add(f"{parts[0]}.{parts[1]}")
    po_count = len(unique_pos)

    if is_cross:
        # Record is cross-PO: scoor op basis van anchor-spreiding
        if po_count >= 3:
            score = 10.0
        elif po_count == 2:
            score = 7.0
        else:
            # cross_po=True maar slechts 1 PO in anchors — inconsistent
            score = 3.0
        detail = f"cross_po=True, anchors van {po_count} programmaonderdelen: {sorted(unique_pos)}"
    elif node_type in POTENTIEEL_MULTI_PO_NODE_TYPES:
        # node_type kan multi-PO zijn maar is hier single-PO — geen straf, neutraal
        score = 5.0
        detail = (
            f"node_type={node_type}, cross_po={cross_po_raw!r} (single-programmaonderdeel); "
            f"anchors van {po_count} programmaonderdelen: {sorted(unique_pos)}"
        )
    else:
        # Niet van toepassing (begripscluster, procedure, ratio, etc.)
        score = 5.0
        detail = f"cross-PO niet relevant voor node_type={node_type!r} (neutraal 5.0)"

    return round(score, 1), detail


def score_hallucinatie_vlag(record: dict) -> tuple[float, str]:
    """
    Hallucinatie-vlag: grounded claims ZONDER specifieke bron-citation.
    10/10 = 0 verdachte grounded-zonder-specifieke-bron claims.
    """
    claims = _collect_claims(record)
    grounded_claims = [c for c in claims if c["confidence"] == "grounded"]

    if not grounded_claims:
        return 10.0, "geen grounded claims (geen hallucinatie-risico)"

    verdacht = [
        c for c in grounded_claims
        if not c["source"] or not SPECIFIEKE_BRON_PATTERN.search(c["source"])
    ]
    ratio_verdacht = len(verdacht) / len(grounded_claims)

    # Score: 0 verdacht → 10/10; 100% verdacht → 0/10
    score = max(0.0, 10.0 - ratio_verdacht * 10.0)

    detail = (
        f"{len(verdacht)}/{len(grounded_claims)} grounded claims zonder specifieke art-/par-ref"
    )
    return round(score, 1), detail


# ---------------------------------------------------------------------------
# Hoofd-audit functie
# ---------------------------------------------------------------------------

@dataclass
class AuditResultaat:
    record_id: str
    schema_version: str
    node_type: str
    wave_id: str
    model: str
    scores: dict[str, tuple[float, str]] = field(default_factory=dict)
    totaal: float = 0.0
    gewogen: bool = True
    overgeslagen: bool = False
    reden_overgeslagen: str = ""

    def gewogen_totaal(self) -> float:
        totaal = 0.0
        for dimensie, gewicht in GEWICHTEN.items():
            score, _ = self.scores.get(dimensie, (5.0, ""))
            totaal += score * gewicht
        return round(totaal, 2)

    def print_rapport(self) -> None:
        if self.overgeslagen:
            print(f"[SKIP] {self.record_id}: {self.reden_overgeslagen}")
            return

        dimensie_labels = {
            "bron_specificiteit": "Bron-specificiteit",
            "concrete_elementen": "Concrete elementen",
            "cell_fill_matrix": "Cell-fill matrix",
            "slot_sections": "Slot-sections compleet",
            "strategisch_advies": "Strategisch advies",
            "cross_po_completeness": "Cross-PO completeness",
            "hallucinatie_vlag": "Hallucinatie-vlag",
        }

        print(f"\n=== Kwaliteits-audit: {self.record_id} ===")
        print(f"    schema: {self.schema_version}  |  node_type: {self.node_type}")
        print(f"    model: {self.model}  |  wave: {self.wave_id}")
        print()

        aandachtspunten = []
        for dimensie, (score, detail) in self.scores.items():
            label = dimensie_labels.get(dimensie, dimensie)
            score_bar = _score_bar(score)
            print(f"  {score_bar} {score:4.1f}/10  {label}")
            print(f"          {detail}")
            if score < 5.0:
                aandachtspunten.append(f"- Score {score:.1f}: {label} — {detail}")

        print()
        print(f"  TOTAAL: {self.totaal:.2f}/10 (gewogen gemiddelde)")

        if aandachtspunten:
            print()
            print("  Aandachtspunten:")
            for punt in aandachtspunten:
                print(f"  {punt}")
        print()


def _score_bar(score: float) -> str:
    """Visuele indicator op basis van score."""
    if score >= 8.0:
        return "✓"
    elif score >= 5.0:
        return "~"
    else:
        return "✗"


def audit_record(record_path: Path) -> AuditResultaat:
    """Laad en scoor een enkel record."""
    with open(record_path, encoding="utf-8") as fp:
        try:
            record = json.load(fp)
        except json.JSONDecodeError as exc:
            resultaat = AuditResultaat(
                record_id=record_path.stem,
                schema_version="?",
                node_type="?",
                wave_id="?",
                model="?",
                overgeslagen=True,
                reden_overgeslagen=f"JSON-fout: {exc}",
            )
            return resultaat

    schema_version = record.get("schema_version", "")

    # Skip niet-schema-2.0 records
    if schema_version != "2.0":
        return AuditResultaat(
            record_id=record.get("id", record_path.stem),
            schema_version=schema_version,
            node_type=record.get("node_type", ""),
            wave_id="",
            model="",
            overgeslagen=True,
            reden_overgeslagen=f"schema_version={repr(schema_version)} — geen schema 2.0 record",
        )

    provenance = record.get("_provenance", {})
    wave_id = (
        provenance.get("wave_id")
        or provenance.get("extract_wave_id")
        or provenance.get("wave")
        or "?"
    )
    model = provenance.get("model") or "?"

    # Scoor alle dimensies
    scores = {
        "bron_specificiteit": score_bron_specificiteit(record),
        "concrete_elementen": score_concrete_elementen(record),
        "cell_fill_matrix": score_cell_fill_matrix(record),
        "slot_sections": score_slot_sections(record),
        "strategisch_advies": score_strategisch_advies(record),
        "cross_po_completeness": score_cross_po_completeness(record),
        "hallucinatie_vlag": score_hallucinatie_vlag(record),
    }

    resultaat = AuditResultaat(
        record_id=record.get("id", record_path.stem),
        schema_version=schema_version,
        node_type=_get_node_type(record) or "?",
        wave_id=wave_id,
        model=model,
        scores=scores,
    )
    resultaat.totaal = resultaat.gewogen_totaal()
    return resultaat


def laad_alle_records(wave_filter: str | None = None) -> list[AuditResultaat]:
    """Laad en scoor alle schema 2.0 records, optioneel gefilterd op wave_id."""
    record_files = sorted(RECORDS_DIR.glob("*.json"))
    resultaten = []

    for record_path in record_files:
        resultaat = audit_record(record_path)
        if resultaat.overgeslagen:
            continue
        if wave_filter and resultaat.wave_id != wave_filter:
            continue
        resultaten.append(resultaat)

    return resultaten


def print_overzicht(resultaten: list[AuditResultaat]) -> None:
    """Print een CSV-achtig overzicht van alle records, gesorteerd op totaal-score."""
    if not resultaten:
        print("Geen schema 2.0 records gevonden (of alle gefilterd).")
        return

    gesorteerd = sorted(resultaten, key=lambda r: r.totaal, reverse=True)

    print(
        f"\n{'Record-ID':<40} {'Totaal':>6} "
        f"{'Bron':>5} {'Conc':>5} {'Cell':>5} "
        f"{'Slot':>5} {'Str':>5} {'XPO':>5} {'Hall':>5} "
        f"{'Model':<30} {'Wave':<40}"
    )
    print("-" * 160)

    for r in gesorteerd:
        scores_vals = [
            r.scores.get(d, (0.0, ""))[0]
            for d in [
                "bron_specificiteit", "concrete_elementen", "cell_fill_matrix",
                "slot_sections", "strategisch_advies", "cross_po_completeness",
                "hallucinatie_vlag",
            ]
        ]
        print(
            f"{r.record_id:<40} {r.totaal:>6.2f} "
            + "".join(f"{s:>5.1f}" for s in scores_vals)
            + f"  {r.model:<30} {r.wave_id:<40}"
        )

    print()
    print(f"Totaal: {len(gesorteerd)} records geauditeerd")
    print()

    # Top-5 best
    print("=== Top-5 best ===")
    for r in gesorteerd[:5]:
        print(f"  {r.totaal:.2f}/10  {r.record_id}")

    print()
    print("=== Bottom-5 — aandacht vereist ===")
    for r in gesorteerd[-5:]:
        print(f"  {r.totaal:.2f}/10  {r.record_id}")

    print()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _resolve_record_path(arg: str) -> Path:
    """Resolveert een record-id of bestandspad naar een Path."""
    p = Path(arg)
    if p.exists():
        return p
    # Probeer als record-id in standaard records-dir
    candidate = RECORDS_DIR / f"{arg}.json"
    if candidate.exists():
        return candidate
    # Probeer zonder .json
    candidate2 = RECORDS_DIR / arg
    if candidate2.exists():
        return candidate2
    raise FileNotFoundError(
        f"Record niet gevonden: {arg!r} — geprobeerd {p}, {candidate}, {candidate2}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Kwaliteits-audit voor schema 2.0 concept-records."
    )
    parser.add_argument(
        "record",
        nargs="?",
        help="Record-ID of pad naar een .json-bestand",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Scoor alle schema 2.0 records",
    )
    parser.add_argument(
        "--wave",
        metavar="WAVE_ID",
        help="Filter op extract_wave_id",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Druk per-dimensie rapport af voor elk record",
    )

    args = parser.parse_args()

    if args.all or args.wave:
        resultaten = laad_alle_records(wave_filter=args.wave)
        if args.verbose:
            for r in sorted(resultaten, key=lambda r: r.totaal, reverse=True):
                r.print_rapport()
        else:
            print_overzicht(resultaten)

    elif args.record:
        try:
            record_path = _resolve_record_path(args.record)
        except FileNotFoundError as exc:
            print(f"Fout: {exc}", file=sys.stderr)
            sys.exit(1)
        resultaat = audit_record(record_path)
        resultaat.print_rapport()

    else:
        parser.print_help()
        sys.exit(0)


if __name__ == "__main__":
    main()
