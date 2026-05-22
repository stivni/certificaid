"""Deterministische migratie van schema 2.1 v1.4 records naar v1.5.

Wijzigingen v1.4 → v1.5 (zie docs/schema-v15-besluit.md voor volledig besluit):

Top-level:
- naam.andere_talen → naam.vertaling
- metadata.primary_po → DROP (afleidbaar uit ankers[0])
- metadata.linked_anchors → metadata.ankers
- metadata.dekt_tdks → DROP (was redundant)
- metadata.tags → DROP (onbenut)
- metadata.cross_po → DROP (afleidbaar)

Inhoud:
- inhoud.definitie/substantie/rationale → inhoud.kern.{definitie,substantie,rationale}
- tekstblok.text → tekst (veldnaam)
- gebruikscontext.trigger_start/einde/voordeel/risico: singular → array
- gebruikscontext.* (contextitems): "text" → "tekst", drop "relateert_naar" (port naar relaties[] is niet altijd mogelijk — log)
- inhoud.voorbeelden {intro, cases[]} → inhoud.voorbeelden: array (intro-tekst behouden als context op eerste case, of gelogd)
- inhoud.voorbeelden cases: voorbeeld.naam.primair → voorbeeld.titel
- inhoud.rollen_per_perspectief {intro, perspectieven[]} → inhoud.accountant_perspectieven (array)
  (intro-tekst gelogd; in v1.5 zit intro op perspectief-niveau, niet op wrapper)
- inhoud.keuzekader → inhoud.syntheses[0] met type=keuzekader, inhoud={assen, vergelijkingstabel?}

Elementen (recursief):
- element.kern verplicht: definitie/substantie/rationale → element.kern.{...}
- element.beschrijving → element.kern.definitie (als geen definitie bestaat; anders geconcateneerd in rationale; ofwel gelogd)
- element.verwijst_naar → DROP (port naar relaties is niet mechanisch mogelijk; gelogd)
- element.inhoud_type mapping:
    procedure_stap, stap_in_cyclus → stap
    component → subconcept
    berekening → formule
    voorwaarde → regel
    vergelijking → mechanisme
    eigenschap → begrip
    valkuil (als inhoud_type op element) → mechanisme (concept-niveau valkuilen[] is de juiste plek)
    moment_in_tijd, keuze → mechanisme (fallback; niet in gebruik per inventarisatie)
- element.voorbeelden: voorbeeld_inline → voorbeeld (naam.primair → titel)

Weergaven (recursief):
- weergave.type mapping:
    t_rekening → boeking
    voorbeeld → proza
    casus → proza
    diagram → proza
  (per inventarisatie: niet in gebruik; defensieve mapping)

Changelog:
- Voeg entry toe: operatie=migrate-v14-v15, timestamp=now, model=migration-script

Idempotent: tweede run = no-op (rec is al v1.5 → geen wijzigingen).

CLI:
    python3 -m tools.extractie.migrate_records_to_v15 --dry-run
    python3 -m tools.extractie.migrate_records_to_v15 [--limit N]
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
RECORDS_DIR = REPO_ROOT / "data" / "concepten" / "records"
SCHEMA_PATH = REPO_ROOT / "data" / "concepten" / "schema-2.1.schema.json"

# Mappings
INHOUD_TYPE_MAP = {
    "procedure_stap": "stap",
    "stap_in_cyclus": "stap",
    "component": "subconcept",
    "berekening": "formule",
    "voorwaarde": "regel",
    "vergelijking": "mechanisme",
    "eigenschap": "begrip",
    "valkuil": "mechanisme",
    "moment_in_tijd": "mechanisme",
    "keuze": "mechanisme",
}

WEERGAVE_TYPE_MAP = {
    "t_rekening": "boeking",
    "voorbeeld": "proza",
    "casus": "proza",
    "diagram": "proza",
}

KERN_KEYS = ("definitie", "substantie", "rationale")


def _migrate_tekstblok(blok):
    """Rename 'text' → 'tekst' in een tekstblok-achtige dict. Mutates."""
    if not isinstance(blok, dict):
        return blok
    if "text" in blok and "tekst" not in blok:
        blok["tekst"] = blok.pop("text")
    return blok


def _migrate_grondslag(g):
    """Geen field-renames in grondslag, maar wel garanderen dat checked_at een geldige iso-string is.
    De huidige records hebben soms checked_at zoals '2026-05-22' (date-only) — dat is geldig per nieuw schema
    (we hebben format-restrict verwijderd voor compatibiliteit)."""
    return g


def _migrate_contextitem(item, log):
    """gebruikscontext-item: text → tekst. relateert_naar → DROP (gelogd)."""
    if not isinstance(item, dict):
        return item
    if "text" in item and "tekst" not in item:
        item["tekst"] = item.pop("text")
    if "relateert_naar" in item:
        log.append(("contextitem_relateert_naar_dropped", item.get("relateert_naar")))
        item.pop("relateert_naar")
    if "rationale" in item:
        # tekst-schema kent rationale als optioneel veld — behouden
        pass
    return item


def _migrate_element(el, log, depth=0):
    """Migreer één element recursief. Returns nieuwe dict (vervangt in-place)."""
    if not isinstance(el, dict):
        return el

    # Inhoud_type mapping
    if "inhoud_type" in el:
        old = el["inhoud_type"]
        if old in INHOUD_TYPE_MAP:
            el["inhoud_type"] = INHOUD_TYPE_MAP[old]
            log.append(("inhoud_type_remap", el.get("id"), old, el["inhoud_type"]))

    # kern-wrapper aanmaken (skip als al gemigreerd: kern aanwezig)
    if "kern" in el and isinstance(el["kern"], dict):
        # Element al gemigreerd; re-migrate tekstblok-velden binnen kern + recurseer sub-velden
        for k in KERN_KEYS:
            if k in el["kern"]:
                _migrate_tekstblok(el["kern"][k])
        # weergaven type-remap
        if "weergaven" in el and isinstance(el["weergaven"], list):
            for w in el["weergaven"]:
                if isinstance(w, dict) and w.get("type") in WEERGAVE_TYPE_MAP:
                    w["type"] = WEERGAVE_TYPE_MAP[w["type"]]
        if "elementen" in el and isinstance(el["elementen"], list):
            el["elementen"] = [_migrate_element(c, log, depth + 1) for c in el["elementen"]]
        if "voorbeelden" in el and isinstance(el["voorbeelden"], list):
            el["voorbeelden"] = [_migrate_voorbeeld(v, log) for v in el["voorbeelden"]]
        return el

    # kern-wrapper aanmaken
    kern = {}
    for k in KERN_KEYS:
        if k in el and isinstance(el[k], dict):
            kern[k] = _migrate_tekstblok(el.pop(k))

    # element.beschrijving → kern.definitie (als geen definitie bestaat); anders gelogd
    if "beschrijving" in el:
        beschr = el.pop("beschrijving")
        if "definitie" not in kern:
            # Synthetiseer een tekstblok. Grondslag: gebruik element.grondslag als beschikbaar,
            # anders een minimaal verondersteld-blok met ai_model (vermijd schema-faal).
            grondslag = el.get("grondslag")
            if not grondslag:
                # Probeer een sane default — beschrijving was vaak AI-gegenereerd
                grondslag = {
                    "confidence": "verondersteld",
                    "bronnen": [
                        {
                            "type": "ai_model",
                            "naam": "claude-sonnet-4-6",
                            "datum": "2026-05-22",
                        }
                    ],
                }
            kern["definitie"] = {"tekst": beschr, "grondslag": grondslag}
            log.append(("beschrijving_naar_kern_definitie", el.get("id")))
        else:
            log.append(("beschrijving_dropped_definitie_bestond", el.get("id"), beschr[:80]))

    if kern:
        el["kern"] = kern
    else:
        # Geen enkele kern-bron: voeg een minimale placeholder toe zodat element-schema geldig blijft.
        # Dit kan voorkomen bij elementen die alleen 'grondslag' + 'inhoud_type' + 'naam' hadden.
        naam_primair = el.get("naam", {}).get("primair", "(naam onbekend)")
        log.append(("element_zonder_kern_placeholder", el.get("id"), naam_primair))
        el["kern"] = {
            "definitie": {
                "tekst": naam_primair,
                "grondslag": el.get("grondslag")
                or {
                    "confidence": "verondersteld",
                    "bronnen": [
                        {
                            "type": "ai_model",
                            "naam": "claude-sonnet-4-6",
                            "datum": "2026-05-22",
                        }
                    ],
                },
            }
        }

    # verwijst_naar → DROP (geen mechanische port naar relaties[])
    if "verwijst_naar" in el:
        log.append(("element_verwijst_naar_dropped", el.get("id"), el["verwijst_naar"]))
        el.pop("verwijst_naar")

    # weergaven (rename type)
    if "weergaven" in el and isinstance(el["weergaven"], list):
        for w in el["weergaven"]:
            if isinstance(w, dict) and "type" in w and w["type"] in WEERGAVE_TYPE_MAP:
                old = w["type"]
                w["type"] = WEERGAVE_TYPE_MAP[old]
                log.append(("weergave_type_remap", el.get("id"), old, w["type"]))

    # Sub-elementen recursief
    if "elementen" in el and isinstance(el["elementen"], list):
        el["elementen"] = [_migrate_element(c, log, depth + 1) for c in el["elementen"]]

    # voorbeelden op element-niveau: voorbeeld_inline → voorbeeld (naam.primair → titel)
    if "voorbeelden" in el and isinstance(el["voorbeelden"], list):
        el["voorbeelden"] = [_migrate_voorbeeld(v, log) for v in el["voorbeelden"]]

    return el


def _migrate_voorbeeld(v, log):
    """voorbeeld_inline of voorbeeld → unified voorbeeld met 'titel'."""
    if not isinstance(v, dict):
        return v
    # Als al gemigreerd (heeft titel): doe niets
    if "titel" in v:
        # mogelijk al v1.5; nog wel recursief elementen migreren
        if "elementen" in v and isinstance(v["elementen"], list):
            v["elementen"] = [_migrate_element(c, log) for c in v["elementen"]]
        if "weergaven" in v:
            for w in v["weergaven"]:
                if isinstance(w, dict) and w.get("type") in WEERGAVE_TYPE_MAP:
                    w["type"] = WEERGAVE_TYPE_MAP[w["type"]]
        return v
    if "naam" in v and isinstance(v["naam"], dict):
        v["titel"] = v["naam"].get("primair") or "(geen titel)"
        v.pop("naam")
    # elementen recursief
    if "elementen" in v and isinstance(v["elementen"], list):
        v["elementen"] = [_migrate_element(c, log) for c in v["elementen"]]
    # weergaven type-remap
    if "weergaven" in v and isinstance(v["weergaven"], list):
        for w in v["weergaven"]:
            if isinstance(w, dict) and w.get("type") in WEERGAVE_TYPE_MAP:
                w["type"] = WEERGAVE_TYPE_MAP[w["type"]]
    return v


def _migrate_gebruikscontext(gc, log):
    if not isinstance(gc, dict):
        return gc

    array_keys = (
        "voor",
        "niet_voor",
        "voorwaarden",
        "uitsluitingen",
        "indicaties",
        "contra_indicaties",
    )
    singular_to_array_keys = ("trigger_start", "trigger_einde", "voordeel", "risico")

    for k in array_keys:
        if k in gc and isinstance(gc[k], list):
            gc[k] = [_migrate_contextitem(item, log) for item in gc[k]]

    for k in singular_to_array_keys:
        if k in gc:
            val = gc[k]
            if isinstance(val, dict):
                gc[k] = [_migrate_contextitem(val, log)]
                log.append(("gebruikscontext_singular_to_array", k))
            elif isinstance(val, list):
                gc[k] = [_migrate_contextitem(item, log) for item in val]

    return gc


def _migrate_keuzekader_naar_synthese(kk, log):
    """keuzekader → synthese[0] met type=keuzekader."""
    if not isinstance(kk, dict):
        return None
    intro = kk.pop("intro", None)
    inhoud_payload = {}
    if "assen" in kk:
        inhoud_payload["assen"] = kk["assen"]
    if "vergelijkingstabel" in kk:
        inhoud_payload["vergelijkingstabel"] = kk["vergelijkingstabel"]
    syn = {"type": "keuzekader", "inhoud": inhoud_payload}
    if intro:
        syn["intro"] = intro
    log.append(("keuzekader_naar_synthese",))
    return syn


def _migrate_voorbeelden_top(vb, log):
    """inhoud.voorbeelden {intro, cases[]} → list[voorbeeld]."""
    if isinstance(vb, list):
        # al gemigreerd
        return [_migrate_voorbeeld(v, log) for v in vb]
    if isinstance(vb, dict):
        intro = vb.pop("intro", None)
        cases = vb.pop("cases", [])
        result = [_migrate_voorbeeld(c, log) for c in cases]
        if intro:
            # Behoud intro door het te prependen aan context van eerste voorbeeld (lossless heuristiek)
            if result and isinstance(result[0], dict):
                existing_ctx = result[0].get("context", "")
                result[0]["context"] = (intro + ("\n\n" + existing_ctx if existing_ctx else "")).strip()
                log.append(("voorbeelden_intro_naar_context_eerste_case",))
            else:
                log.append(("voorbeelden_intro_dropped", intro[:80]))
        return result
    return vb


def _migrate_rollen_per_perspectief(rpp, log):
    """rollen_per_perspectief {intro, perspectieven[]} → list[perspectief]."""
    if isinstance(rpp, list):
        # al gemigreerd
        return [
            {**p, "rollen": [_migrate_rol_invulling(r, log) for r in p.get("rollen", [])]}
            for p in rpp
        ]
    if isinstance(rpp, dict):
        intro = rpp.pop("intro", None)
        perspectieven = rpp.pop("perspectieven", [])
        result = []
        for p in perspectieven:
            if "rollen" in p and isinstance(p["rollen"], list):
                p["rollen"] = [_migrate_rol_invulling(r, log) for r in p["rollen"]]
            result.append(p)
        if intro and result:
            # Behoud intro als intro op het eerste perspectief
            existing = result[0].get("intro", "")
            result[0]["intro"] = (intro + ("\n\n" + existing if existing else "")).strip()
            log.append(("rollen_intro_naar_eerste_perspectief",))
        elif intro:
            log.append(("rollen_intro_dropped", intro[:80]))
        return result
    return rpp


def _migrate_rol_invulling(rol, log):
    if not isinstance(rol, dict):
        return rol
    if "elementen" in rol and isinstance(rol["elementen"], list):
        rol["elementen"] = [_migrate_element(e, log) for e in rol["elementen"]]
    # Filter rol-enum: bestuurder/curator/forensisch zijn gedropt
    if rol.get("rol") in ("bestuurder", "curator", "forensisch"):
        old = rol["rol"]
        # Mapping: bestuurder → adviseur (rol vd accountant ten opzichte van bestuurder), curator → fiscaal/auditor, forensisch → auditor
        mapping = {"bestuurder": "adviseur", "curator": "auditor", "forensisch": "auditor"}
        rol["rol"] = mapping[old]
        log.append(("rol_enum_remap", old, rol["rol"]))
    return rol


def migrate(rec: dict) -> tuple[dict, list]:
    """Pas v1.4 → v1.5 wijzigingen toe. Retourneert (rec, log_entries)."""
    log: list = []

    # naam.andere_talen → naam.vertaling
    naam = rec.get("naam", {})
    if isinstance(naam, dict) and "andere_talen" in naam and "vertaling" not in naam:
        naam["vertaling"] = naam.pop("andere_talen")
        log.append(("andere_talen_naar_vertaling",))

    # metadata clean-up
    md = rec.get("metadata", {})
    if isinstance(md, dict):
        # linked_anchors → ankers
        if "linked_anchors" in md and "ankers" not in md:
            md["ankers"] = md.pop("linked_anchors")
            log.append(("linked_anchors_naar_ankers",))
        # Drop velden
        for drop_key in ("primary_po", "dekt_tdks", "tags", "cross_po"):
            if drop_key in md:
                md.pop(drop_key)
                log.append((f"metadata_{drop_key}_gedropt",))

    # inhoud: kern-wrapper + andere transformaties
    inh = rec.get("inhoud", {})
    if isinstance(inh, dict):
        # kern-wrapper
        if "kern" not in inh:
            kern = {}
            for k in KERN_KEYS:
                if k in inh and isinstance(inh[k], dict):
                    kern[k] = _migrate_tekstblok(inh.pop(k))
            if kern:
                inh["kern"] = kern
                log.append(("kern_wrapper_aangemaakt", list(kern.keys())))
            else:
                # Geen definitie/substantie/rationale aanwezig — placeholder zodat schema valid is
                naam_primair = rec.get("naam", {}).get("primair", "(naam onbekend)")
                log.append(("concept_zonder_kern_placeholder",))
                inh["kern"] = {
                    "definitie": {
                        "tekst": naam_primair,
                        "grondslag": {
                            "confidence": "verondersteld",
                            "bronnen": [
                                {
                                    "type": "ai_model",
                                    "naam": "claude-sonnet-4-6",
                                    "datum": "2026-05-22",
                                }
                            ],
                        },
                    }
                }
        else:
            # Eventueel al een kern aanwezig — recursief tekst-migratie
            for k in KERN_KEYS:
                if k in inh["kern"]:
                    _migrate_tekstblok(inh["kern"][k])

        # gebruikscontext
        if "gebruikscontext" in inh:
            inh["gebruikscontext"] = _migrate_gebruikscontext(inh["gebruikscontext"], log)

        # elementen recursief
        if "elementen" in inh and isinstance(inh["elementen"], list):
            inh["elementen"] = [_migrate_element(e, log) for e in inh["elementen"]]

        # voorbeelden
        if "voorbeelden" in inh:
            inh["voorbeelden"] = _migrate_voorbeelden_top(inh["voorbeelden"], log)

        # rollen_per_perspectief → accountant_perspectieven
        if "rollen_per_perspectief" in inh and "accountant_perspectieven" not in inh:
            inh["accountant_perspectieven"] = _migrate_rollen_per_perspectief(
                inh.pop("rollen_per_perspectief"), log
            )
            log.append(("rollen_per_perspectief_naar_accountant_perspectieven",))
        elif "accountant_perspectieven" in inh:
            inh["accountant_perspectieven"] = _migrate_rollen_per_perspectief(
                inh["accountant_perspectieven"], log
            )

        # keuzekader → syntheses[0]
        if "keuzekader" in inh:
            syn = _migrate_keuzekader_naar_synthese(inh.pop("keuzekader"), log)
            if syn is not None:
                inh.setdefault("syntheses", []).insert(0, syn)

    # relaties: toelichting kan tekstblok zijn → text→tekst rename
    rel = rec.get("relaties", [])
    if isinstance(rel, list):
        for r in rel:
            if isinstance(r, dict) and "toelichting" in r and isinstance(r["toelichting"], dict):
                _migrate_tekstblok(r["toelichting"])

    return rec, log


def _migration_marker_present(rec: dict) -> bool:
    """Return True als er al een migrate-v14-v15 changelog-entry bestaat (idempotent guard)."""
    cl = rec.get("metadata", {}).get("changelog", [])
    if not isinstance(cl, list):
        return False
    return any(isinstance(e, dict) and e.get("operatie") == "migrate-v14-v15" for e in cl)


def _add_changelog_entry(rec: dict, log: list) -> None:
    cl = rec.setdefault("metadata", {}).setdefault("changelog", [])
    cl.append(
        {
            "operatie": "migrate-v14-v15",
            "timestamp": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "model": "migration-script",
            "wijziging": f"Schema 2.1 v1.4 → v1.5 (mutaties: {len(log)})",
        }
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Migrate records van schema 2.1 v1.4 → v1.5.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0, help="Beperk tot N records (0=alle).")
    parser.add_argument("--quiet", action="store_true", help="Verberg per-record logs.")
    args = parser.parse_args()

    schema = json.loads(SCHEMA_PATH.read_text())
    validator = Draft202012Validator(schema)

    paden = sorted(RECORDS_DIR.glob("*.json"))
    if args.limit > 0:
        paden = paden[: args.limit]

    aantal_gewijzigd = 0
    aantal_already_v15 = 0
    aantal_post_invalide = 0
    info_verlies_records: list[tuple[str, list]] = []
    invalide_records: list[tuple[str, str]] = []

    log_event_counter: dict = {}

    for pad in paden:
        try:
            rec = json.loads(pad.read_text())
        except json.JSONDecodeError as e:
            print(f"  ✗ {pad.name}: JSON-fout: {e}")
            continue

        if _migration_marker_present(rec):
            aantal_already_v15 += 1
            continue

        migrated, log = migrate(rec)

        # Tel event-types
        for ev in log:
            evtype = ev[0] if isinstance(ev, tuple) else str(ev)
            log_event_counter[evtype] = log_event_counter.get(evtype, 0) + 1

        # Identificeer info-verlies
        info_verlies_events = {
            "element_verwijst_naar_dropped",
            "contextitem_relateert_naar_dropped",
            "beschrijving_dropped_definitie_bestond",
            "voorbeelden_intro_dropped",
            "rollen_intro_dropped",
            "element_zonder_kern_placeholder",
            "concept_zonder_kern_placeholder",
        }
        verlies_in_record = [ev for ev in log if ev[0] in info_verlies_events]
        if verlies_in_record:
            info_verlies_records.append((pad.stem, verlies_in_record))

        # Voeg changelog-entry toe
        _add_changelog_entry(migrated, log)

        # Valideer
        errors = list(validator.iter_errors(migrated))
        if errors:
            aantal_post_invalide += 1
            err_msg = errors[0].message[:160]
            err_path = "/".join(str(p) for p in errors[0].absolute_path)
            invalide_records.append((pad.stem, f"@/{err_path}: {err_msg}"))
            if not args.quiet:
                print(f"  ✗ {pad.stem}: {len(errors)} validation errors — @/{err_path}: {err_msg}")

        aantal_gewijzigd += 1
        if not args.dry_run and not errors:
            pad.write_text(json.dumps(migrated, ensure_ascii=False, indent=2) + "\n")

    # Samenvatting
    print()
    print("=" * 72)
    print(f"MIGRATIE-SAMENVATTING ({'DRY-RUN' if args.dry_run else 'WRITE'})")
    print("=" * 72)
    print(f"Records totaal:           {len(paden)}")
    print(f"Reeds v1.5 (geskipt):     {aantal_already_v15}")
    print(f"Gemigreerd:               {aantal_gewijzigd}")
    print(f"Post-migratie invalide:   {aantal_post_invalide}")
    print()
    print("Event-frequentie:")
    for ev, n in sorted(log_event_counter.items(), key=lambda x: -x[1]):
        print(f"  {ev:48s} {n:5d}")
    print()
    if info_verlies_records:
        print(f"Records met info-verlies ({len(info_verlies_records)}):")
        for stem, events in info_verlies_records[:30]:
            event_types = ", ".join(sorted({ev[0] for ev in events}))
            print(f"  • {stem}: {event_types}")
        if len(info_verlies_records) > 30:
            print(f"  ... en {len(info_verlies_records) - 30} meer")
    if invalide_records:
        print()
        print(f"Records die niet valideren ({len(invalide_records)}):")
        for stem, msg in invalide_records[:30]:
            print(f"  ✗ {stem}: {msg}")
        if len(invalide_records) > 30:
            print(f"  ... en {len(invalide_records) - 30} meer")
    print()
    if args.dry_run:
        print("(DRY-RUN — geen disk-writes)")
    return 0 if aantal_post_invalide == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
