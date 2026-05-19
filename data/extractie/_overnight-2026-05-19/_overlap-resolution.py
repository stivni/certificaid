#!/usr/bin/env python3
"""
Overlap resolution for PO 1.1 — link records that describe same fenomeen.
Full merge would require incoming-edge redirect on ~20 records each; defer to a
dedicated merge-pass (orphan-management in rename_record). For now: cross-link.
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
    prov['po11_overnight_gap_fix_2026_05_19'] = {
        "uitgevoerd_op": NOW,
        "run_id": RUN_ID,
        "changes": changes
    }

def add_edge_if_missing(rec, edge):
    edges = rec.setdefault('edges', [])
    key = (edge['type'], edge['target'])
    for e in edges:
        if (e.get('type'), e.get('target')) == key:
            return False
    edges.append(edge)
    return True

# ---- getrouw-beeld ↔ getrouw-beeld-jaarrekening ----
# Beide beschrijven hetzelfde fenomeen (art. III.89 WER + KB WVV art. 3:1).
# Verschil: getrouw-beeld is generieker (PO 1.1, boekhoudbeginsel-perspectief);
# getrouw-beeld-jaarrekening is specifieker (PO 1.2, jaarrekening-perspectief).
# Cross-link via vergelijkt-met met aspect-facet.
rec = load('getrouw-beeld')
add_edge_if_missing(rec, {
    "type": "vergelijkt-met",
    "target": "getrouw-beeld-jaarrekening",
    "aspect": "perspectief",
    "redenering": "Beide records dekken het getrouw-beeld-beginsel (WER art. III.89 / KB WVV art. 3:1). Dit record dekt het beginsel-perspectief (PO 1.1 — boekhoudbeginselen); getrouw-beeld-jaarrekening dekt het jaarrekening-perspectief (PO 1.2 — toelichtingsverplichting bij ontoereikende regels). Kandidaat voor merge in volgende VERIFY-pass."
})
mark_touched(rec, ["cross-link toegevoegd naar getrouw-beeld-jaarrekening (overlap-flag voor toekomstige merge)"])
save_record(rec)
print("OK: getrouw-beeld cross-linked")

rec = load('getrouw-beeld-jaarrekening')
add_edge_if_missing(rec, {
    "type": "vergelijkt-met",
    "target": "getrouw-beeld",
    "aspect": "perspectief",
    "redenering": "Beide records dekken het getrouw-beeld-beginsel. Dit record dekt het jaarrekening-perspectief (PO 1.2 — toelichtingsverplichting); getrouw-beeld dekt het beginsel-perspectief (PO 1.1). Kandidaat voor merge in volgende VERIFY-pass."
})
mark_touched(rec, ["cross-link toegevoegd naar getrouw-beeld (overlap-flag voor toekomstige merge)"])
save_record(rec)
print("OK: getrouw-beeld-jaarrekening cross-linked")

# ---- bewaring-boekhoudstukken ↔ bewaartermijn-boekhouding ----
rec = load('bewaring-boekhoudstukken')
add_edge_if_missing(rec, {
    "type": "vergelijkt-met",
    "target": "bewaartermijn-boekhouding",
    "aspect": "perspectief",
    "redenering": "Beide records dekken hetzelfde fenomeen (WER art. III.86 — 7 jaar bewaartermijn). Dit record vanuit boekhoudplicht-perspectief (PO 1.1); bewaartermijn-boekhouding vanuit jaarrekening-perspectief (PO 1.2). Kandidaat voor merge in volgende VERIFY-pass."
})
mark_touched(rec, ["cross-link toegevoegd naar bewaartermijn-boekhouding (overlap-flag voor toekomstige merge)"])
save_record(rec)
print("OK: bewaring-boekhoudstukken cross-linked")

rec = load('bewaartermijn-boekhouding')
add_edge_if_missing(rec, {
    "type": "vergelijkt-met",
    "target": "bewaring-boekhoudstukken",
    "aspect": "perspectief",
    "redenering": "Beide records dekken hetzelfde fenomeen (WER art. III.86). Kandidaat voor merge in volgende VERIFY-pass."
})
mark_touched(rec, ["cross-link toegevoegd naar bewaring-boekhoudstukken (overlap-flag voor toekomstige merge)"])
save_record(rec)
print("OK: bewaartermijn-boekhouding cross-linked")

# ---- rechten-verplichtingen-buiten-balans / klasse-0-niet-in-balans / niet-in-balans-opgenomen-rechten-verplichtingen ----
# Three records:
#  - rechten-verplichtingen-buiten-balans (cluster, PO 1.1) — overkoepelend
#  - klasse-0-niet-in-balans (begrip, PO 1.3 + 1.2) — boekhoudkundige rekeningenklasse
#  - niet-in-balans-opgenomen-rechten-verplichtingen (regel, PO 1.3 + 1.2) — toelichtingsverplichting
# Aanbeveling: drie records BEHOUDEN als drie perspectieven (geen merge),
# maar bidirectionele cross-links toevoegen. Cluster behoudt overkoepelende rol.
rec = load('rechten-verplichtingen-buiten-balans')
add_edge_if_missing(rec, {
    "type": "vereist-kennis-van",
    "target": "klasse-0-niet-in-balans",
    "redenering": "Boekhoudkundige uitwerking via MAR klasse 0."
})
add_edge_if_missing(rec, {
    "type": "vereist-kennis-van",
    "target": "niet-in-balans-opgenomen-rechten-verplichtingen",
    "redenering": "Toelichtingsverplichting bij de jaarrekening (KB WVV)."
})
mark_touched(rec, ["cross-links toegevoegd naar klasse-0-niet-in-balans en niet-in-balans-opgenomen-rechten-verplichtingen (drie perspectieven van zelfde fenomeen — cluster is overkoepelend)"])
save_record(rec)
print("OK: rechten-verplichtingen-buiten-balans cross-linked naar twee perspectieven")

# klasse-0-niet-in-balans already has edge onderdeel-van → niet-in-balans-opgenomen-rechten-verplichtingen.
# Add edge onderdeel-van → rechten-verplichtingen-buiten-balans (overkoepelend).
rec = load('klasse-0-niet-in-balans')
add_edge_if_missing(rec, {
    "type": "specialisatie-van",
    "target": "rechten-verplichtingen-buiten-balans",
    "redenering": "Klasse 0 is de boekhoudkundige specialisatie van het overkoepelende fenomeen."
})
mark_touched(rec, ["edge specialisatie-van rechten-verplichtingen-buiten-balans toegevoegd (drie-perspectief)"])
save_record(rec)
print("OK: klasse-0-niet-in-balans linked naar overkoepelend cluster")

rec = load('niet-in-balans-opgenomen-rechten-verplichtingen')
add_edge_if_missing(rec, {
    "type": "specialisatie-van",
    "target": "rechten-verplichtingen-buiten-balans",
    "redenering": "Deze regel is de toelichtingsverplichting-specialisatie van het overkoepelende fenomeen."
})
mark_touched(rec, ["edge specialisatie-van rechten-verplichtingen-buiten-balans toegevoegd (drie-perspectief)"])
save_record(rec)
print("OK: niet-in-balans-opgenomen-rechten-verplichtingen linked naar overkoepelend cluster")

# ---- jaarrekening overlap met jaarrekening-schema / samenstelling-statutaire-jaarrekening ----
# Aanbeveling gap: link via 'bevat'/'specialisatie-van' edges in plaats van merge.
# 'bevat' is deprecated; gebruik inverse onderdeel-van op de specialisatie-records.
# Check beide bestaan:
rec = load('jaarrekening-schema')
add_edge_if_missing(rec, {
    "type": "specialisatie-van",
    "target": "jaarrekening",
    "redenering": "Jaarrekening-schema is de schema-keuze-specialisatie (volledig/verkort/micro) binnen het overkoepelende jaarrekening-cluster."
})
mark_touched(rec, ["edge specialisatie-van jaarrekening toegevoegd"])
save_record(rec)
print("OK: jaarrekening-schema linked naar jaarrekening")

rec = load('samenstelling-statutaire-jaarrekening')
add_edge_if_missing(rec, {
    "type": "onderdeel-van",
    "target": "jaarrekening",
    "redenering": "Samenstelling-statutaire-jaarrekening is een procedure-aspect van het jaarrekening-cluster."
})
mark_touched(rec, ["edge onderdeel-van jaarrekening toegevoegd"])
save_record(rec)
print("OK: samenstelling-statutaire-jaarrekening linked naar jaarrekening")

print("\nOverlap-resolution voltooid.")
