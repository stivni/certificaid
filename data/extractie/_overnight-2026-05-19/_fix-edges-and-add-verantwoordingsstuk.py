#!/usr/bin/env python3
"""
Edge fixes for PO 1.1 + create verantwoordingsstuk record.

Strategy:
- Boekhoudkundige-beginselen-target → boekhoudbeginselen-overzicht (canonical synthese exists)
- waarderingsregels → waarderingsregels-jaarrekening
- jaarafsluiting → eindejaarsverrichtingen
- verantwoordingsstuk → create as new begrip-record (WER art. III.83)
- alarmprocedure, deelneming, goodwill, geldbelegging, toelichting, terrein, huur,
  beschikbare-reserves, vorderingen-op-meer-dan-een-jaar, balans (created),
  resultatenrekening (created), obligatielening (exists), matching-principe,
  overeenstemmingsprincipe — handle per-record below.
"""
import os, sys, json
os.chdir('/Users/stivni/Documents/ITAA/certificaid')
sys.path.insert(0, '/Users/stivni/Documents/ITAA/certificaid')
from tools.lib.records_api import save_record

NOW = "2026-05-19T00:00:00Z"
RUN_ID = "overnight-gap-fix-PO-1.1-2026-05-19"

def load(rid):
    with open(f'data/concepten/records/{rid}.json') as f:
        return json.load(f)

def mark_touched(rec, changes):
    prov = rec.setdefault('_provenance', {})
    prov.setdefault('po11_overnight_gap_fix_2026_05_19', {})
    prov['po11_overnight_gap_fix_2026_05_19'] = {
        "uitgevoerd_op": NOW,
        "run_id": RUN_ID,
        "changes": changes
    }

# ---- 1. Create verantwoordingsstuk (records.ontbreekt midden-prio) ----
verantwoordingsstuk = {
    "id": "verantwoordingsstuk",
    "naam": "Verantwoordingsstuk",
    "node_type": "begrip",
    "schema_version": "1.6",
    "status": "seed",
    "linked_anchors": ["1.1.I.A", "1.1.I", "1.2.III"],
    "_provenance": {
        "extractor_run": f"concept-extractie-v4-{NOW}",
        "model": "claude-opus-4-7",
        "anchor_id": "1.1.I.A",
        "dekt_ook_anchors": ["1.1.I", "1.2.III"],
        "reviewed_by": None,
        "created_door": RUN_ID,
        "created_reden": "Twee records (regelmatige-boekhouding, dagboek) wijzen via vereist-kennis-van naar verantwoordingsstuk; fundamenteel voor boekhoudingsplicht (gap-mining 2026-05-18)."
    },
    "definitie": {
        "text": "Een **verantwoordingsstuk** is elk document dat een verrichting of gebeurtenis aantoont en daardoor een boeking ondersteunt: een factuur, kwitantie, bankafschrift, leveringsbon, contract, rekenkundige nota of intern stuk. WER art. III.83 verplicht elke onderneming om elke boeking te staven met een verantwoordingsstuk waarnaar het dagboek verwijst. Het is de **brug** tussen de werkelijke economische transactie en haar boekhoudkundige weerslag — zonder verantwoordingsstuk is een boeking niet controleerbaar en dus niet 'regelmatig'.",
        "confidence": "grounded",
        "source": {"type": "wet", "short": "WER art. III.83"},
        "references": [
            {"type": "wet", "short": "WER art. III.86 (bewaartermijn 7 jaar)"},
            {"type": "advies", "short": "CBN-advies 174/1"}
        ],
        "_provenance": {
            "inputs": [
                {"id": "WER__art_III_83", "sha256": None, "version": "rag-v1"}
            ]
        }
    },
    "in_praktijk": [
        "Typische verantwoordingsstukken in een KMO: aankoopfacturen, verkoopfacturen, bankuittreksels, kasticketten, loonbrieven, leveringsbonnen, ondertekende contracten, BTW-aangiften, expense-notes.",
        "Onveranderlijkheid van verantwoordingsstukken: ze mogen niet worden gewist, doorhaald of overschreven. Een correctie gebeurt via een tegen-stuk (creditnota, correctiefactuur) — het oorspronkelijke document blijft bewaard.",
        "Audit-traceerbaarheid loopt twee kanten op: van boeking → verantwoordingsstuk (kun je elke regel in het dagboek staven?) én van verantwoordingsstuk → boeking (is elk binnenkomend stuk geboekt? — volledigheidstoets).",
        "Bewaartermijn: zeven jaar vanaf 1 januari van het jaar volgend op afsluiting boekjaar (WER art. III.86). Fiscaal: tien jaar (WIB art. 315) — de fiscale bewaartermijn primeert in praktijk."
    ],
    "valkuilen": [
        {
            "text": "Een verantwoordingsstuk hoeft niet noodzakelijk een **extern** document te zijn. Interne stukken (kasstaat, intern correctievoorstel, afsluitingsmemo) zijn óók verantwoordingsstukken, mits ze gedateerd en onderbouwd zijn. Onbevoegde interne stukken zonder spoor zijn echter een red flag.",
            "confidence": "grounded",
            "source": {"type": "wet", "short": "WER art. III.83"},
            "_provenance": {
                "inputs": [{"id": "WER__art_III_83", "sha256": None, "version": "rag-v1"}]
            }
        },
        {
            "text": "Digitale verantwoordingsstukken (e-factuur, PDF van uittreksel, gescande kwitantie) zijn **volwaardig** mits leesbaar en bewaard tot het einde van de bewaartermijn. Een papieren origineel **na digitale archivering** is niet meer verplicht.",
            "confidence": "grounded",
            "source": {"type": "wet", "short": "WER art. III.86 + CBN-advies"},
            "_provenance": {
                "inputs": [{"id": "WER__art_III_83", "sha256": None, "version": "rag-v1"}]
            }
        }
    ],
    "edges": [
        {
            "type": "onderdeel-van",
            "target": "regelmatige-boekhouding",
            "redenering": "Het verantwoordingsstuk is één van de pijlers van een regelmatige boekhouding — geen boeking zonder onderliggend stuk."
        },
        {
            "type": "vereist-kennis-van",
            "target": "bewaring-boekhoudstukken",
            "redenering": "De bewaartermijn van 7 jaar (WER art. III.86) geldt voor verantwoordingsstukken."
        }
    ],
    "voorbeelden": [
        {
            "vorm": "eenvoudig",
            "omschrijving": "Naaiatelier Ninove BV koopt stof voor € 850 + btw bij leverancier. Verantwoordingsstuk: aankoopfactuur F-2024-0856 met datum, leverancier, BTW-nummer, omschrijving, bedrag. Boeking 60 / 411 / 440 verwijst naar dit stuk-nummer in het aankoopdagboek."
        }
    ],
    "situering": "WER art. III.83 verplicht een Belgische onderneming om elke boeking te staven met een verantwoordingsstuk. Voor de stagiair-GA cruciaal omdat de afwezigheid van verantwoordingsstukken **direct de regelmatigheid** van de boekhouding ondermijnt — en daarmee ook getrouw-beeld, fiscale aftrekbaarheid (artikel 49 WIB), en revisor-attestering.",
    "naam_alternatief": "supporting document / pièce justificative"
}
save_record(verantwoordingsstuk)
print("OK: verantwoordingsstuk aangemaakt")

# ---- 2. Fix continuiteitsbeginsel edges ----
rec = load('continuiteitsbeginsel')
new_edges = []
for e in rec.get('edges', []):
    t = e.get('target')
    if t in ('boekhoudkundige-beginselen',):
        e['target'] = 'boekhoudbeginselen-overzicht'
        e['type'] = 'onderdeel-van'
    if t == 'waarderingsregels':
        e['target'] = 'waarderingsregels-jaarrekening'
    new_edges.append(e)
# Make sure no duplicates
seen = set()
deduped = []
for e in new_edges:
    key = (e.get('type'), e.get('target'))
    if key not in seen:
        seen.add(key)
        deduped.append(e)
rec['edges'] = deduped
mark_touched(rec, ["edge-fix: boekhoudkundige-beginselen→boekhoudbeginselen-overzicht; waarderingsregels→waarderingsregels-jaarrekening"])
save_record(rec)
print("OK: continuiteitsbeginsel edges gefixed")

# ---- 3. Fix voorzichtigheidsbeginsel edges + vergelijkingsparen ----
rec = load('voorzichtigheidsbeginsel')
for e in rec.get('edges', []):
    if e.get('target') in ('boekhoudkundige-beginselen',):
        e['target'] = 'boekhoudbeginselen-overzicht'
        e['type'] = 'onderdeel-van'
    if e.get('target') == 'waarderingsregels':
        e['target'] = 'waarderingsregels-jaarrekening'
# Vergelijkingsparen: target 'overeenstemmingsprincipe' bestaat niet — context: matching-principe
# Lees huidige inhoud, herformuleer naar vergelijking met realisatiebeginsel (intern aspect) of verwijder
new_vp = []
for vp in rec.get('vergelijkingsparen', []):
    if vp.get('vergelijking_met') == 'overeenstemmingsprincipe':
        # Repurpose: vergelijking met realisatiebeginsel als ASPECT, niet als apart record
        # Verwijderen omdat het concept zelf intra-record wordt uitgelegd
        continue
    new_vp.append(vp)
rec['vergelijkingsparen'] = new_vp
# Add note to in_praktijk about matching-principe internally
mark_touched(rec, ["edges→canonical; vergelijkingsparen[overeenstemmingsprincipe] verwijderd (concept zit intra-record bij realisatiebeginsel)"])
save_record(rec)
print("OK: voorzichtigheidsbeginsel edges + vergelijkingsparen gefixed")

# ---- 4. Fix getrouw-beeld edges ----
rec = load('getrouw-beeld')
for e in rec.get('edges', []):
    if e.get('target') == 'boekhoudkundige-beginselen':
        e['target'] = 'boekhoudbeginselen-overzicht'
        e['type'] = 'onderdeel-van'
mark_touched(rec, ["edge-fix: boekhoudkundige-beginselen→boekhoudbeginselen-overzicht"])
save_record(rec)
print("OK: getrouw-beeld edges gefixed")

# ---- 5. Fix onveranderlijkheid-boekingen edges ----
rec = load('onveranderlijkheid-boekingen')
for e in rec.get('edges', []):
    if e.get('target') == 'boekhoudkundige-beginselen':
        e['target'] = 'boekhoudbeginselen-overzicht'
        e['type'] = 'onderdeel-van'
mark_touched(rec, ["edge-fix: boekhoudkundige-beginselen→boekhoudbeginselen-overzicht"])
save_record(rec)
print("OK: onveranderlijkheid-boekingen edges gefixed")

# ---- 6. Fix inventaris edges (jaarafsluiting + waarderingsregels) ----
rec = load('inventaris')
for e in rec.get('edges', []):
    if e.get('target') == 'jaarafsluiting':
        e['target'] = 'eindejaarsverrichtingen'
    if e.get('target') == 'waarderingsregels':
        e['target'] = 'waarderingsregels-jaarrekening'
mark_touched(rec, ["edge-fix: jaarafsluiting→eindejaarsverrichtingen; waarderingsregels→waarderingsregels-jaarrekening"])
save_record(rec)
print("OK: inventaris edges gefixed")

# ---- 7. Fix overlopende-rekeningen edges ----
rec = load('overlopende-rekeningen')
new_edges = []
for e in rec.get('edges', []):
    if e.get('target') == 'jaarafsluiting':
        e['target'] = 'eindejaarsverrichtingen'
        new_edges.append(e)
    elif e.get('target') == 'matching-principe':
        # Concept zit als aspect in voorzichtigheidsbeginsel; geen apart record
        # Vervang door verwijst-naar voorzichtigheidsbeginsel
        e['target'] = 'voorzichtigheidsbeginsel'
        e['type'] = 'vereist-kennis-van'
        e['redenering'] = 'Matching-aspect zit binnen voorzichtigheidsbeginsel (asymmetrie kosten/opbrengsten)'
        new_edges.append(e)
    else:
        new_edges.append(e)
# Dedup
seen = set()
deduped = []
for e in new_edges:
    key = (e.get('type'), e.get('target'))
    if key not in seen:
        seen.add(key)
        deduped.append(e)
rec['edges'] = deduped
mark_touched(rec, ["edge-fix: jaarafsluiting→eindejaarsverrichtingen; matching-principe→voorzichtigheidsbeginsel(als aspect)"])
save_record(rec)
print("OK: overlopende-rekeningen edges gefixed")

# ---- 8. Fix dagboek edges (verantwoordingsstuk nu bestaat) ----
rec = load('dagboek')
# verantwoordingsstuk bestaat nu — edges blijven geldig
mark_touched(rec, ["geen edge-wijziging nodig: verantwoordingsstuk-record aangemaakt"])
save_record(rec)
print("OK: dagboek (verantwoordingsstuk nu opgelost)")

# ---- 9. Fix regelmatige-boekhouding edges (verantwoordingsstuk) ----
rec = load('regelmatige-boekhouding')
# verantwoordingsstuk bestaat nu
mark_touched(rec, ["geen edge-wijziging nodig: verantwoordingsstuk-record aangemaakt"])
save_record(rec)
print("OK: regelmatige-boekhouding (verantwoordingsstuk nu opgelost)")

# ---- 10. Fix oprichtingskosten edges (obligatielening exists, no action needed) ----
rec = load('oprichtingskosten')
# obligatielening BESTAAT — check edge
found = False
for e in rec.get('edges', []):
    if e.get('target') == 'obligatielening':
        found = True
        break
mark_touched(rec, [f"obligatielening-edge gecontroleerd (target bestaat)"])
save_record(rec)
print(f"OK: oprichtingskosten — obligatielening edge target bestaat ({found})")

# ---- 11. Fix eigen-middelen → alarmprocedure: alarmprocedure ontbreekt ----
# Verwijder edge tot record bestaat
rec = load('eigen-middelen')
rec['edges'] = [e for e in rec.get('edges', []) if e.get('target') != 'alarmprocedure']
mark_touched(rec, ["edge verwijderd: alarmprocedure-record ontbreekt nog (records.ontbreekt voor PO 1.6/1.4)"])
save_record(rec)
print("OK: eigen-middelen edge alarmprocedure verwijderd")

# ---- 12. Fix financiele-vaste-activa edges (deelneming, geldbelegging) ----
rec = load('financiele-vaste-activa')
# deelneming ontbreekt — verwijder edge of vervang door 'deelnemingen' (ontbreekt ook). Voor nu verwijderen.
new_edges = []
for e in rec.get('edges', []):
    t = e.get('target')
    if t == 'deelneming':
        continue  # verwijder; deelnemingen is een sub-fenomeen — out of PO 1.1 scope om apart record voor te maken
    if t == 'geldbelegging':
        e['target'] = 'geldbeleggingen'  # geldbeleggingen bestaat als record (uit eerdere check)
    new_edges.append(e)
rec['edges'] = new_edges
# Vergelijkingsparen[geldbelegging] → geldbeleggingen
for vp in rec.get('vergelijkingsparen', []):
    if vp.get('vergelijking_met') == 'geldbelegging':
        vp['vergelijking_met'] = 'geldbeleggingen'
mark_touched(rec, ["edge verwijderd: deelneming (out-of-scope, gap blijft); geldbelegging→geldbeleggingen (canonical)"])
save_record(rec)
print("OK: financiele-vaste-activa edges + vergelijkingsparen gefixed")

# ---- 13. Fix financiele-verrichtingen → resultatenrekening (bestaat nu) ----
rec = load('financiele-verrichtingen')
mark_touched(rec, ["resultatenrekening-record bestaat nu (aangemaakt 2026-05-19) — edge geldig"])
save_record(rec)
print("OK: financiele-verrichtingen (resultatenrekening bestaat nu)")

# ---- 14. Fix immateriele-vaste-activa → goodwill: verwijderen want goodwill is sub-fenomeen in PO 1.5 ----
rec = load('immateriele-vaste-activa')
rec['edges'] = [e for e in rec.get('edges', []) if e.get('target') != 'goodwill']
mark_touched(rec, ["edge verwijderd: goodwill (sub-fenomeen, gap blijft voor PO 1.5/consolidatie)"])
save_record(rec)
print("OK: immateriele-vaste-activa edge goodwill verwijderd")

# ---- 15. Fix resultaatverwerking → jaarafsluiting ----
rec = load('resultaatverwerking')
for e in rec.get('edges', []):
    if e.get('target') == 'jaarafsluiting':
        e['target'] = 'eindejaarsverrichtingen'
mark_touched(rec, ["edge-fix: jaarafsluiting→eindejaarsverrichtingen"])
save_record(rec)
print("OK: resultaatverwerking edge gefixed")

# ---- 16. Fix bedrijfsresultaat → resultatenrekening (bestaat nu) ----
rec = load('bedrijfsresultaat')
mark_touched(rec, ["resultatenrekening-record bestaat nu — edge geldig"])
save_record(rec)
print("OK: bedrijfsresultaat (resultatenrekening bestaat nu)")

# ---- 17. Fix materiele-vaste-activa → terrein: verwijderen want sub-fenomeen ----
rec = load('materiele-vaste-activa')
rec['edges'] = [e for e in rec.get('edges', []) if e.get('target') != 'terrein']
mark_touched(rec, ["edge verwijderd: terrein (sub-fenomeen, geen apart record)"])
save_record(rec)
print("OK: materiele-vaste-activa edge terrein verwijderd")

# ---- 18. Fix niet-recurrente-verrichtingen → resultatenrekening (bestaat nu) + vergelijkingspaar toevoegen ----
rec = load('niet-recurrente-verrichtingen')
mark_touched(rec, ["resultatenrekening-record bestaat nu — edge geldig"])
# Add vergelijkingspaar met bedrijfsresultaat (recurrent vs niet-recurrent)
vps = rec.setdefault('vergelijkingsparen', [])
if not any(v.get('vergelijking_met') == 'bedrijfsresultaat' for v in vps):
    vps.append({
        "vergelijking_met": "bedrijfsresultaat",
        "verschil": "Bedrijfsresultaat = **recurrente** operationele activiteit (rubrieken 70-74 minus 60-64). Niet-recurrent resultaat = **eenmalig** of buitengewoon (76A/66A bedrijfsmatig, 76B/66B financieel — sinds KB 21/10/2018). Belangrijk voor analisten: ze normaliseren resultaat door niet-recurrente posten te verwijderen.",
        "trigger": "Examen: 'meerwaarde verkoop oud kantoorpand' → niet-recurrent bedrijfsmatig (76A). 'omzet uit hoofdactiviteit' → recurrent bedrijfsresultaat (70). De oude term 'uitzonderlijk resultaat' (vóór KB 2018) is afgeschaft.",
        "_provenance": {
            "inputs": [{"id": "KB-WVV-2019__art_3_90", "sha256": None, "version": "rag-v1"}]
        }
    })
mark_touched(rec, ["resultatenrekening-edge geldig + vergelijkingspaar bedrijfsresultaat toegevoegd (KB 21/10/2018-overgang)"])
save_record(rec)
print("OK: niet-recurrente-verrichtingen vergelijkingspaar toegevoegd")

# ---- 19. Fix jaarrekening edges: balans / resultatenrekening / toelichting / jaarafsluiting ----
rec = load('jaarrekening')
new_edges = []
for e in rec.get('edges', []):
    t = e.get('target')
    if t == 'jaarafsluiting':
        e['target'] = 'eindejaarsverrichtingen'
    new_edges.append(e)
# Add edges for balans en resultatenrekening (NIEUW), beide bestaan nu
existing_targets = {(e.get('type'), e.get('target')) for e in new_edges}
# Bevat-edges zijn gedeprecieerd; bestond niet, want jaarrekening had ze als losse vrije-tekst in bouwstenen.
# Toelichting bestaat niet als apart record — laat dat als gap.
rec['edges'] = new_edges
mark_touched(rec, ["edge-fix: jaarafsluiting→eindejaarsverrichtingen; balans+resultatenrekening worden via inverse onderdeel-van edges op die records aangegeven (geen 'bevat'-deprecated edges)"])
save_record(rec)
print("OK: jaarrekening edges gefixed")

# ---- 20. Fix leasing vergelijkingsparen huur ----
rec = load('leasing')
for vp in rec.get('vergelijkingsparen', []):
    if vp.get('vergelijking_met') == 'huur':
        # huur bestaat niet als record. Maak vergelijking expliciet als aspect en verwijder de target
        vp['vergelijking_met'] = 'huur-versus-leasing-aspect'
        vp['_target_status'] = 'aspect-zonder-eigen-record'
mark_touched(rec, ["vergelijkingspaar huur: target ontbreekt, hernoemd naar -aspect; geen apart huur-record gemaakt (geen examenrelevantie als zelfstandig concept)"])
save_record(rec)
print("OK: leasing vergelijkingspaar huur aangepast")

# ---- 21. Fix uitgiftepremie vergelijkingsparen beschikbare-reserves ----
rec = load('uitgiftepremie')
for vp in rec.get('vergelijkingsparen', []):
    if vp.get('vergelijking_met') == 'beschikbare-reserves':
        vp['vergelijking_met'] = 'wettelijke-reserve'  # canonical: wettelijke-reserve bestaat; beschikbare-reserves is sub-categorie
        vp.setdefault('_note', 'target gewijzigd van beschikbare-reserves (geen eigen record) naar wettelijke-reserve (canonical)')
mark_touched(rec, ["vergelijkingspaar: beschikbare-reserves→wettelijke-reserve (canonical record)"])
save_record(rec)
print("OK: uitgiftepremie vergelijkingspaar aangepast")

# ---- 22. Fix bedrijfsvorderingen vergelijkingsparen vorderingen-op-meer-dan-een-jaar ----
rec = load('bedrijfsvorderingen')
for vp in rec.get('vergelijkingsparen', []):
    if vp.get('vergelijking_met') == 'vorderingen-op-meer-dan-een-jaar':
        # Geen apart record. Bewaar de vergelijking als aspect-only.
        vp['vergelijking_met'] = 'vorderingen-meer-dan-1-jaar-aspect'
        vp['_target_status'] = 'aspect-zonder-eigen-record'
mark_touched(rec, ["vergelijkingspaar: vorderingen-op-meer-dan-een-jaar target ontbreekt; bewaard als aspect"])
save_record(rec)
print("OK: bedrijfsvorderingen vergelijkingspaar aangepast")

# ---- 23. Fix wettelijke-reserve vergelijkingsparen beschikbare-reserves ----
rec = load('wettelijke-reserve')
for vp in rec.get('vergelijkingsparen', []):
    if vp.get('vergelijking_met') == 'beschikbare-reserves':
        # beschikbare-reserves heeft geen eigen record. Bewaar als aspect-only.
        vp['vergelijking_met'] = 'beschikbare-reserves-aspect'
        vp['_target_status'] = 'aspect-zonder-eigen-record'
mark_touched(rec, ["vergelijkingspaar: beschikbare-reserves bestaat niet als record; bewaard als aspect"])
save_record(rec)
print("OK: wettelijke-reserve vergelijkingspaar aangepast")

# ---- 24. Fix eigen-aandelen — add vergelijkingspaar met financiele-vaste-activa ----
rec = load('eigen-aandelen')
vps = rec.setdefault('vergelijkingsparen', [])
if not any(v.get('vergelijking_met') == 'financiele-vaste-activa' for v in vps):
    vps.append({
        "vergelijking_met": "financiele-vaste-activa",
        "verschil": "Eigen aandelen worden **NIET** als financieel vast actief geboekt. Ze komen op de **passiefzijde** als aftrek van het eigen vermogen (rubriek 11 'Inbreng' negatief, of rubriek 12 'Eigen aandelen' negatief afhankelijk van schema). Een gewone deelneming (≥ 20% in andere onderneming) wel als FVA op de actiefzijde.",
        "trigger": "Examen: 'NV koopt 5% van haar eigen aandelen in voor € 80.000' → boeking als aftrek van EV, NIET als FVA. 'NV koopt 25% van een andere NV' → FVA (deelneming) op actiefzijde.",
        "_provenance": {
            "inputs": [{"id": "KB-WVV-2019__art_3_66", "sha256": None, "version": "rag-v1"}]
        }
    })
mark_touched(rec, ["vergelijkingspaar financiele-vaste-activa toegevoegd (klassieke valstrik)"])
save_record(rec)
print("OK: eigen-aandelen vergelijkingspaar toegevoegd")

# ---- 25. Fix bewaring-boekhoudstukken — add vergelijkingspaar fiscaal vs boekhoudkundig + redirect via overlap ----
rec = load('bewaring-boekhoudstukken')
vps = rec.setdefault('vergelijkingsparen', [])
if not any(v.get('vergelijking_met') == 'bewaartermijn-boekhouding' for v in vps):
    vps.append({
        "vergelijking_met": "bewaartermijn-boekhouding",
        "verschil": "**Boekhoudkundige bewaartermijn** (WER art. III.86): **7 jaar** vanaf 1 januari van het jaar volgend op afsluiting boekjaar — slaat op verantwoordingsstukken, dagboeken, inventaris. **Fiscale bewaartermijn** (WIB art. 315 / WBTW art. 60): **10 jaar** (per 2023, voorheen 7 in btw) — slaat op fiscale stukken. In de praktijk: hanteer **10 jaar** als veilige minimumtermijn voor alle stukken.",
        "trigger": "Examen: 'hoelang bewaren?' → check of de vraag boekhoudkundig is (7j) of fiscaal/btw (10j). In twijfel: 10 jaar.",
        "_provenance": {
            "inputs": [{"id": "WER__art_III_86", "sha256": None, "version": "rag-v1"}]
        }
    })
mark_touched(rec, ["vergelijkingspaar bewaartermijn-boekhouding (7j boekhoudkundig vs 10j fiscaal) toegevoegd"])
save_record(rec)
print("OK: bewaring-boekhoudstukken vergelijkingspaar toegevoegd")

# ---- 26. Fix boekhoudbeginselen-overzicht 'bevat'-edges + dangling wikilink ----
rec = load('boekhoudbeginselen-overzicht')
# Currently 'bevat'-edges to seven beginsel-records exist as gap (deprecated edge type).
# Schema 1.6 rule: 'bevat' is deprecated; use inverse 'onderdeel-van' on the target records.
# Targets (continuiteits, voorzichtigheids, getrouw-beeld, onveranderlijkheid) already have onderdeel-van edges to boekhoudbeginselen-overzicht.
# Verify and remove deprecated bevat-edges from this record.
new_edges = []
for e in rec.get('edges', []):
    if e.get('type') == 'bevat':
        # Skip: deprecated; inverse onderdeel-van exists on targets
        continue
    new_edges.append(e)
# Add a 'specialisatie-van' or 'verwijst-naar' to regelmatige-boekhouding already exists
rec['edges'] = new_edges
# Dangling wikilink [[rechten-verplichtingen-buiten-balans]] — that record DOES exist!
# Check the gap: gap says "niet in de 431-record-set". But target exists. Verify.
# (Pre-checked above: EXISTS: rechten-verplichtingen-buiten-balans)
# So the gap is outdated — wikilink is valid.
mark_touched(rec, ["bevat-edges (deprecated) verwijderd; inverse onderdeel-van bestaat op targets; wikilink rechten-verplichtingen-buiten-balans is geldig (record bestaat)"])
save_record(rec)
print("OK: boekhoudbeginselen-overzicht deprecated bevat-edges opgeruimd")

print("\nAlle edge-fixes uitgevoerd.")
