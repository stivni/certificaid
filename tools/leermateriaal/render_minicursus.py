"""
Render minicursus-skeleton + Opus-glue-instructies voor een programmaonderdeel.

Werkt in twee fasen:
1. Deterministisch skeleton: leest leerpad + records + competenties, bouwt body
   met alle wikilinks en cheatsheet-data (drempelwaarden, formules, vergelijkingsparen).
2. Schrijft subagent-instructies voor Opus om LLM-glue-placeholders in te vullen.

Geen LLM-calls in dit script zelf (CLAUDE.md regel 3).

Gebruik:
  python3 -m tools.leermateriaal.render_minicursus --programmaonderdeel 1.4
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
RECORDS_DIR = ROOT / "data" / "concepten" / "records"
LEERPADEN_DIR = ROOT / "data" / "concepten" / "leerpaden"
GAPS_FILE = ROOT / "data" / "extractie" / "gaps.json"
PROGRAMMA_FILE = ROOT / "data" / "programma" / "programma.json"
OUTPUT_CONTENT_DIR = ROOT / "content" / "studiemateriaal"
EXTRACTIE_DIR = ROOT / "data" / "extractie"
PROMPTS_DIR = ROOT / "prompts"
GLUE_PROMPT = PROMPTS_DIR / "minicursus-glue-v3.md"
EXAMEN_VRAGEN_DIR = ROOT / "data" / "programma" / "examen_vragen"


def _laad_records_voor_programmaonderdeel(programmaonderdeel_id: str) -> list[dict]:
    """Laad alle concept-records voor een programmaonderdeel."""
    prefix = f"{programmaonderdeel_id}."
    records = []
    for bestand in sorted(RECORDS_DIR.glob("*.json")):
        if bestand.name.startswith("_"):
            continue
        try:
            record = json.loads(bestand.read_text(encoding="utf-8"))
            if any(a.startswith(prefix) for a in record.get("linked_anchors", [])):
                records.append(record)
        except (json.JSONDecodeError, OSError):
            pass
    return records


def _laad_competenties_voor_programmaonderdeel(programmaonderdeel_id: str) -> list[dict]:
    """Laad alle competentie-records voor een programmaonderdeel uit records/ (node_type=competentie)."""
    resultaat = []
    for bestand in sorted(RECORDS_DIR.glob("*.json")):
        if bestand.name.startswith("_"):
            continue
        try:
            comp = json.loads(bestand.read_text(encoding="utf-8"))
            if (
                isinstance(comp, dict)
                and comp.get("node_type") == "competentie"
                and programmaonderdeel_id in [str(p) for p in comp.get("programmaonderdelen", [])]
            ):
                resultaat.append(comp)
        except (json.JSONDecodeError, OSError):
            pass
    return resultaat


def _laad_open_gaps_voor_programmaonderdeel(
    programmaonderdeel_id: str, records: list[dict]
) -> list[dict]:
    """Laad open concept-gaps voor records van dit programmaonderdeel."""
    if not GAPS_FILE.exists():
        return []
    try:
        alle_gaps = json.loads(GAPS_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

    record_ids = {r.get("id", "") for r in records}
    return [
        g for g in alle_gaps
        if g.get("status") == "open"
        and g.get("aspect_type", "concept-gap") == "concept-gap"
        and g.get("record_id", "") in record_ids
    ]


def _bouw_cheatsheet_data(records: list[dict]) -> tuple[list, list, list]:
    """Extraheer drempelwaarden, formules en vergelijkingsparen uit alle records.

    Returns:
        (alle_drempelwaarden, alle_formules, alle_vergelijkingsparen)
    """
    alle_drempelwaarden: list[dict] = []
    alle_formules: list[dict] = []
    alle_vergelijkingsparen: list[dict] = []

    for record in records:
        concept_id = record.get("id", "")
        concept_naam = record.get("naam", concept_id)

        for drempel in record.get("drempelwaarden", []):
            alle_drempelwaarden.append({
                "concept_id": concept_id,
                **drempel,
            })

        for methode in record.get("berekeningsmethode", []):
            if methode.get("formule"):
                alle_formules.append({
                    "concept_id": concept_id,
                    "concept_naam": concept_naam,
                    "methode_naam": methode.get("naam", ""),
                    "formule": methode["formule"],
                })

        for paar in record.get("vergelijkingsparen", []):
            alle_vergelijkingsparen.append({
                "concept_id": concept_id,
                **paar,
            })

    return alle_drempelwaarden, alle_formules, alle_vergelijkingsparen


def _slugify_programmaonderdeel(programmaonderdeel_id: str, leerpad: dict) -> str:
    """Genereer een korte slug voor de output-map.

    Neemt het deel van de titel vóór de eerste " en "-conjunctie of de eerste
    komma, en kapt tot maximaal 6 woorden om lange dirnamen te vermijden.
    Bv. "Geconsolideerde jaarrekening en wetgeving betreffende de
    geconsolideerde jaarrekening" → "geconsolideerde-jaarrekening".
    """
    from tools.leermateriaal.lib.wikilinks import slugify
    titel = leerpad.get("titel", programmaonderdeel_id)
    kort = titel
    for splitter in (" en wetgeving", " en ", ", "):
        if splitter in kort:
            kort = kort.split(splitter, 1)[0]
            break
    # Kap tot max 6 woorden voor sanity
    woorden = kort.split()
    if len(woorden) > 6:
        kort = " ".join(woorden[:6])
    # Vervang punt door dash in de PO-code (bv. 1.4 → 1-4) — serve-handler
    # treats dots in path-segments as file-extensions, wat 404 geeft op
    # twee-niveau-dieper folder-URLs (Quartz/serve-handler-bug).
    po_safe = programmaonderdeel_id.replace(".", "-")
    return f"{po_safe}-{slugify(kort)}"


def _programmaonderdeel_intro(programmaonderdeel_id: str) -> str:
    """Haal intro_tekst voor een programmaonderdeel uit programma.json."""
    if not PROGRAMMA_FILE.exists():
        return ""
    try:
        programma = json.loads(PROGRAMMA_FILE.read_text(encoding="utf-8"))
        for po in programma.get("programmaonderdelen", []):
            if str(po.get("code", "")) == programmaonderdeel_id:
                return po.get("intro_tekst", "")
    except (json.JSONDecodeError, KeyError):
        pass
    return ""


def _laad_programmaonderdeel(programmaonderdeel_id: str) -> dict:
    """Haal volledige PO-dict (niveau, taken, kenniselementen) uit programma.json."""
    if not PROGRAMMA_FILE.exists():
        return {}
    try:
        programma = json.loads(PROGRAMMA_FILE.read_text(encoding="utf-8"))
        for po in programma.get("programmaonderdelen", []):
            if str(po.get("code", "")) == programmaonderdeel_id:
                return po
    except (json.JSONDecodeError, KeyError):
        pass
    return {}


def render_skeleton(
    programmaonderdeel_id: str,
    leerpad: dict,
    records: list[dict],
    competenties: list[dict],
    open_gaps: list[dict],
) -> str:
    """Render het deterministisch skeleton van de minicursus.

    Examenvragen worden uitsluitend via data/exam_focus/*.json en
    data/voorbeeldvragen-synthetisch/*.json geladen (ADR-009 §6 mode A).
    De examenfocus-binding-lib doet de filter en sortering; deze functie
    geeft alleen door.

    Args:
        programmaonderdeel_id: bv. '1.4'
        leerpad: leerpad-dict (uit YAML)
        records: alle concept-records voor dit programmaonderdeel
        competenties: alle competenties voor dit programmaonderdeel
        open_gaps: open gaps voor records van dit programmaonderdeel

    Returns:
        Markdown-skeleton met placeholders voor Opus-glue
    """
    from tools.leermateriaal.lib.frontmatter import as_yaml_block, minicursus_frontmatter
    from tools.leermateriaal.lib.jinja_env import get_env

    # Competenties-dict voor snelle lookup
    competenties_dict = {c.get("id", ""): c for c in competenties}

    # Records-dict voor snelle lookup
    concepten_dict = {r.get("id", ""): r for r in records}

    # Frontmatter
    gerelateerde_ids = [r.get("id", "") for r in records]
    frontmatter = minicursus_frontmatter(
        programmaonderdeel_code=programmaonderdeel_id,
        programmaonderdeel_titel=leerpad.get("titel", ""),
        gerelateerde_concept_ids=gerelateerde_ids,
    )
    frontmatter_yaml = as_yaml_block(frontmatter)

    # Cheatsheet-data
    alle_drempelwaarden, alle_formules, alle_vergelijkingsparen = _bouw_cheatsheet_data(records)

    # Programmaonderdeel-data (niveau, taken) voor oriëntatie + taak-binding (ADR-010 §implicatie-5)
    from tools.leermateriaal.lib.taak_binding import (
        alle_po_taak_bindings,
        bouw_taak_dekking,
        niveau_toelichting,
    )
    programmaonderdeel_data = _laad_programmaonderdeel(programmaonderdeel_id)
    po_niveau = programmaonderdeel_data.get("niveau", "")
    po_niveau_toelichting = niveau_toelichting(po_niveau)
    po_taken = programmaonderdeel_data.get("taken", [])

    # Verrijk hoofdstukken met competentie- en synthese-data
    hoofdstukken = leerpad.get("hoofdstukken", [])
    for hoofdstuk in hoofdstukken:
        if hoofdstuk.get("type") == "competentie":
            comp_id = hoofdstuk.get("competentie_id", "")
            hoofdstuk["competentie"] = competenties_dict.get(comp_id, {})
        elif hoofdstuk.get("type") == "synthese":
            syn_id = hoofdstuk.get("synthese_id", "")
            # Synthese-records hoeven niet PO-gefilterd in records_dict te zitten;
            # laad rechtstreeks uit RECORDS_DIR om cross-PO synthese mogelijk te maken
            syn_record = concepten_dict.get(syn_id)
            if syn_record is None:
                syn_pad = RECORDS_DIR / f"{syn_id}.json"
                if syn_pad.exists():
                    try:
                        syn_record = json.loads(syn_pad.read_text(encoding="utf-8"))
                    except json.JSONDecodeError:
                        syn_record = {}
            hoofdstuk["synthese"] = syn_record or {}

    # Gesorteerde records voor concept-index
    gesorteerde_records = sorted(records, key=lambda r: r.get("naam", ""))
    # Gesorteerde competenties voor competentie-index
    gesorteerde_competenties = sorted(competenties, key=lambda c: c.get("titel", ""))

    # Lege glue-placeholders
    glue: dict = {
        "leesgids_titel": "Leesgids",
        "leesgids_tekst": "<!-- TODO: Opus-glue leesgids -->",
        "waarom_po_titel": "Waarom dit programmaonderdeel telt",
        "waarom_po_tekst": "<!-- TODO: Opus-glue waarom_po -->",
        "orientatie": ["<!-- TODO: Opus-glue oriëntatie -->" for _ in hoofdstukken],
        "competentie_intro": ["<!-- TODO: Opus-glue competentie-intro -->" for _ in hoofdstukken],
        "thematisch_intro": ["<!-- TODO: Opus-glue thematisch-intro -->" for _ in hoofdstukken],
        "synthese_intro": ["<!-- TODO: Opus-glue synthese-intro -->" for _ in hoofdstukken],
        "synthese": "<!-- TODO: Opus-glue synthese -->",
        "examenfocus": "<!-- TODO: Opus-glue examenfocus -->",
    }

    # Examenfocus-rubriek (ADR-009 §6 + §7, ADR-010 §implicatie-4)
    from tools.leermateriaal.lib.examenfocus_binding import (
        laad_examenfocus_groepen,
        laad_voorbeeldvragen_synthetisch,
    )
    po_record_ids = {r.get("id") for r in records} | {c.get("id") for c in competenties}
    po_record_ids.discard(None)
    examenfocus_groepen = laad_examenfocus_groepen(po_record_ids)
    voorbeeldvragen_synth = laad_voorbeeldvragen_synthetisch(po_record_ids)

    # Taak-binding per hoofdstuk (ADR-010 §implicatie-5B/5C)
    # Records dict bevat alleen PO-records — voor competentie/synthese-records
    # zit de record-data al in hoofdstuk['competentie'] / hoofdstuk['synthese'],
    # dus die hoeven niet in records_dict.
    taken_per_hoofdstuk = alle_po_taak_bindings(
        leerpad, concepten_dict, programmaonderdeel_data
    )
    # Per hoofdstuk: taak-tekst voor de marker-callout
    taak_codes_naar_tekst = {t.get("code", ""): t.get("tekst", "") for t in po_taken}
    hoofdstuk_taak_markers = []
    for taken_set in taken_per_hoofdstuk:
        markers = [
            {"code": code, "tekst": taak_codes_naar_tekst.get(code, code)}
            for code in sorted(taken_set)
        ]
        hoofdstuk_taak_markers.append(markers)

    # Eind-dashboard: H2-index voor sectie-nummering
    # Vaste H2's voor oriëntatie (1=Wat verwacht, 2=Leesgids, 3=Waarom-PO),
    # dan komen de inhoudelijke hoofdstukken vanaf H2-index 4.
    sectie_offset = 4
    taak_dekking = bouw_taak_dekking(
        leerpad, concepten_dict, programmaonderdeel_data, sectie_offset=sectie_offset
    )

    env = get_env()
    template = env.get_template("minicursus_skeleton.md.j2")

    return template.render(
        frontmatter_yaml=frontmatter_yaml,
        leerpad=leerpad,
        hoofdstukken=hoofdstukken,
        records=records,
        concepten_dict=concepten_dict,
        alle_drempelwaarden=alle_drempelwaarden,
        alle_formules=alle_formules,
        alle_vergelijkingsparen=alle_vergelijkingsparen,
        gesorteerde_records=gesorteerde_records,
        gesorteerde_competenties=gesorteerde_competenties,
        open_gaps=open_gaps,
        glue=glue,
        po_niveau=po_niveau,
        po_niveau_toelichting=po_niveau_toelichting,
        po_taken=po_taken,
        hoofdstuk_taak_markers=hoofdstuk_taak_markers,
        taak_dekking=taak_dekking,
        examenfocus_groepen=examenfocus_groepen,
        voorbeeldvragen_synth=voorbeeldvragen_synth,
    )


def schrijf_subagent_instructies(
    programmaonderdeel_id: str,
    skeleton_pad: Path,
    records: list[dict],
    competenties: list[dict],
    run_id: str,
    werkmap: Path,
) -> Path:
    """Schrijf instructies voor Opus-subagent om LLM-glue in te vullen."""
    werkmap.mkdir(parents=True, exist_ok=True)
    instructies_pad = werkmap / f"minicursus-instructies-{run_id}.md"

    # Records-summaries (naam + definitie + rationale)
    summaries: list[dict] = []
    for record in records:
        hoofdveld = (
            record.get("definitie")
            or record.get("main_rule")
            or record.get("verplichting")
            or record.get("doel")
            or {}
        )
        summaries.append({
            "id": record.get("id", ""),
            "naam": record.get("naam", ""),
            "node_type": record.get("node_type", ""),
            "definitie_snippet": str(hoofdveld.get("text", ""))[:300],
            "rationale_snippet": str(record.get("rationale", {}).get("text", ""))[:200],
        })

    # Competentie-summaries
    comp_summaries: list[dict] = []
    for comp in competenties:
        comp_summaries.append({
            "id": comp.get("id", ""),
            "titel": comp.get("titel", ""),
            "procedure_grondslag": comp.get("procedure_grondslag", {}),
            "gebaseerd_op_concepten": comp.get("gebaseerd_op_concepten", []),
            "eerste_stap": comp.get("stappen", [{}])[0].get("titel", "") if comp.get("stappen") else "",
        })

    glue_prompt_tekst = GLUE_PROMPT.read_text(encoding="utf-8") if GLUE_PROMPT.exists() else (
        f"[WAARSCHUWING: {GLUE_PROMPT.name} niet gevonden — laad handmatig]"
    )

    instructies = f"""# Minicursus-glue-run {run_id} — Instructies voor Opus-subagent

**Programmaonderdeel**: {programmaonderdeel_id}
**Run-id**: {run_id}
**Gegenereerd op**: {datetime.now(timezone.utc).isoformat(timespec="seconds")}

## Jouw taak

Vul de `<!-- TODO: Opus-glue ... -->` placeholders in de skeleton-Markdown in.
Edit de skeleton-Markdown direct (geen JSON-output) volgens de regels in
`prompts/minicursus-glue-v3.md` (parafrase-met-bronlink-contract).

## Input-bestanden

- **Skeleton**: `{skeleton_pad.relative_to(ROOT)}`
- **Records-summaries** ({len(records)} stuks): zie §Records hieronder
- **Competentie-summaries** ({len(competenties)} stuks): zie §Competenties hieronder

## Kern-regels (samenvatting — volledige regels in §Prompt-referentie hieronder)

- Parafrase MAG, mits wikilink bij elke feitelijke claim in dezelfde zin
- Wikilinks toevoegen naar bestaande records (check vooraf dat ze bestaan)
- Geen feit verzinnen zonder record-grondslag, geen non-existent wikilinks
- Werkwoorden volgen het PO-niveau (zie frontmatter / oriëntatie-callout)
- Bij twijfel: korte neutrale tekst, geen uitvinding

## Records-summaries

```json
{json.dumps(summaries, ensure_ascii=False, indent=2)}
```

## Competentie-summaries

```json
{json.dumps(comp_summaries, ensure_ascii=False, indent=2)}
```

---

## Prompt-referentie (minicursus-glue-v3.md)

{glue_prompt_tekst}
"""

    instructies_pad.write_text(instructies, encoding="utf-8")
    return instructies_pad


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--programmaonderdeel",
        required=True,
        help="Programmaonderdeel-code, bv. '1.4'.",
    )
    parser.add_argument(
        "--droog",
        action="store_true",
        help="Droog uitvoeren: render maar schrijf niets weg.",
    )
    parser.add_argument(
        "--forceer",
        action="store_true",
        help="Forceer overschrijven van bestaande minicursus, ook als er geen "
             "Opus-glue TODO-placeholders meer in staan (de glue gaat dan verloren).",
    )
    args = parser.parse_args()

    programmaonderdeel_id: str = args.programmaonderdeel

    # Leerpad laden
    leerpad_bestand = LEERPADEN_DIR / f"{programmaonderdeel_id}.yaml"
    if not leerpad_bestand.exists():
        print(
            f"FOUT: geen leerpad gevonden op {leerpad_bestand.relative_to(ROOT)}. "
            f"Maak eerst een leerpad via tools/leermateriaal/propose_leerpad.py.",
            file=sys.stderr,
        )
        sys.exit(1)

    with open(leerpad_bestand, encoding="utf-8") as f:
        leerpad = yaml.safe_load(f)

    print(f"[minicursus] Leerpad geladen: '{leerpad.get('titel', '?')}'")

    # Records + competenties laden
    records = _laad_records_voor_programmaonderdeel(programmaonderdeel_id)
    print(f"[minicursus] {len(records)} concept-records geladen.")

    competenties = _laad_competenties_voor_programmaonderdeel(programmaonderdeel_id)
    print(f"[minicursus] {len(competenties)} competenties geladen.")

    # Open gaps laden
    open_gaps = _laad_open_gaps_voor_programmaonderdeel(programmaonderdeel_id, records)
    if open_gaps:
        print(f"[minicursus] {len(open_gaps)} open gaps gevonden — worden vermeld in skeleton.")

    # Skeleton renderen (examenvragen via data/exam_focus/*.json — ADR-009 §6 mode A)
    skeleton = render_skeleton(
        programmaonderdeel_id=programmaonderdeel_id,
        leerpad=leerpad,
        records=records,
        competenties=competenties,
        open_gaps=open_gaps,
    )

    # Output-paden
    slug = _slugify_programmaonderdeel(programmaonderdeel_id, leerpad)
    # Plat: minicursus rechtstreeks als bestand onder content/studiemateriaal/,
    # niet binnen een per-PO submap. URL wordt `/studiemateriaal/<slug>`.
    output_map = OUTPUT_CONTENT_DIR
    skeleton_pad = output_map / f"{slug}.md"

    run_id = datetime.now(timezone.utc).strftime("minicursus-run-%Y%m%dT%H%M%SZ")
    werkmap = EXTRACTIE_DIR / programmaonderdeel_id / "minicursus-runs" / run_id

    if not args.droog:
        output_map.mkdir(parents=True, exist_ok=True)
        # Safety: voorkom dat we Opus-glue overschrijven zonder --forceer
        if skeleton_pad.exists() and not args.forceer:
            bestaande = skeleton_pad.read_text(encoding="utf-8")
            todos_in_bestaande = bestaande.count("<!-- TODO: Opus-glue")
            if todos_in_bestaande == 0:
                print(
                    f"FOUT: bestaande {skeleton_pad.relative_to(ROOT)} bevat geen "
                    f"TODO-placeholders meer (Opus-glue is al ingevuld). Opnieuw "
                    f"renderen zou de glue overschrijven. Gebruik --forceer om "
                    f"hier expliciet voor te kiezen.",
                    file=sys.stderr,
                )
                sys.exit(2)
        skeleton_pad.write_text(skeleton, encoding="utf-8")
        print(f"[minicursus] Skeleton geschreven: {skeleton_pad.relative_to(ROOT)}")

        instructies_pad = schrijf_subagent_instructies(
            programmaonderdeel_id=programmaonderdeel_id,
            skeleton_pad=skeleton_pad,
            records=records,
            competenties=competenties,
            run_id=run_id,
            werkmap=werkmap,
        )
        print(f"[minicursus] Subagent-instructies: {instructies_pad.relative_to(ROOT)}")

        print(f"\nVolgende stap:")
        print(f"  Open {instructies_pad.relative_to(ROOT)}")
        print(f"  in een Opus-subagent-sessie voor LLM-glue (minicursus-glue-v3.md).")
        print(f"  Output-skeleton: {skeleton_pad.relative_to(ROOT)}")
    else:
        print("[droog] Skeleton NIET weggeschreven.")
        print("[droog] Subagent-instructies NIET weggeschreven.")


if __name__ == "__main__":
    main()
