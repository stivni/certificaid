"""Update werkkapitaal and liquiditeitsratio to add mirrored vergelijkingsparen + edges
toward the newly created werkkapitaalbehoefte and cash-ratio records.

Reads on disk (records-API uses RAG-canonical reads but disk-read is fine for a re-save
since we re-emit the full record via save_record).
"""
import os, sys, json
os.chdir('/Users/stivni/Documents/ITAA/certificaid')
sys.path.insert(0, '/Users/stivni/Documents/ITAA/certificaid')
from tools.lib.records_api import save_record
from pathlib import Path

ROOT = Path('/Users/stivni/Documents/ITAA/certificaid')


def update_werkkapitaal():
    p = ROOT / 'data/concepten/records/werkkapitaal.json'
    rec = json.loads(p.read_text())

    # Add vergelijkingspaar with werkkapitaalbehoefte if not present
    paren = rec.setdefault('vergelijkingsparen', [])
    if not any(vp.get('vergelijking_met') == 'werkkapitaalbehoefte' for vp in paren):
        paren.append({
            "vergelijking_met": "werkkapitaalbehoefte",
            "verschil": "Werkkapitaal = wat er is uit de balans (vlottende activa − schulden op ten hoogste een jaar). Werkkapitaalbehoefte = wat de operationele cyclus nodig heeft (voorraden + handelsvorderingen − handelsschulden). Het verschil tussen beide = nettokaspositie. Negatieve nettokas = structureel liquiditeitstekort.",
            "trigger": "Examenvraag 'beschikbaar versus benodigd werkkapitaal' of 'wanneer is er liquiditeitstekort?': vergelijk werkkapitaal (beschikbaar uit balans) met werkkapitaalbehoefte (benodigd voor cyclus).",
            "_provenance": {
                "inputs": [{"id": "anchor-1.3.II.C", "sha256": None, "version": "rag-v1"}]
            }
        })

    # Add edge to werkkapitaalbehoefte if not present
    edges = rec.setdefault('edges', [])
    if not any(e.get('target') == 'werkkapitaalbehoefte' for e in edges):
        edges.append({
            "type": "vergelijkt-met",
            "target": "werkkapitaalbehoefte",
            "redenering": "Werkkapitaal (beschikbaar uit balans) versus werkkapitaalbehoefte (benodigd voor operationele cyclus). Het verschil bepaalt de nettokas.",
            "confidence": "inferred"
        })

    # Bump provenance
    rec.setdefault('_provenance', {})
    rec['_provenance']['last_touch'] = 'concept-extractie-v4-2026-05-19T-overnight-gap-fix'

    save_record(rec)
    print("OK werkkapitaal updated")


def update_liquiditeitsratio():
    p = ROOT / 'data/concepten/records/liquiditeitsratio.json'
    rec = json.loads(p.read_text())

    paren = rec.setdefault('vergelijkingsparen', [])
    if not any(vp.get('vergelijking_met') == 'cash-ratio' for vp in paren):
        paren.append({
            "vergelijking_met": "cash-ratio",
            "verschil": "Liquiditeitsratio is de overkoepelende categorie waar cash ratio onder valt als strengste hoofdvariant. Cash ratio neemt alleen de onmiddellijk beschikbare middelen (geldbeleggingen + liquide middelen); de bredere current en quick ratios nemen ook voorraden of vorderingen mee.",
            "trigger": "Examenvraag 'strengste liquiditeitstoets?' of 'welke ratio sluit voorraden én vorderingen uit?': altijd cash ratio.",
            "_provenance": {
                "inputs": [{"id": "anchor-1.3.II.C", "sha256": None, "version": "rag-v1"}]
            }
        })

    edges = rec.setdefault('edges', [])
    if not any(e.get('target') == 'cash-ratio' for e in edges):
        edges.append({
            "type": "verwijst-naar",
            "target": "cash-ratio",
            "redenering": "Cash ratio is de derde hoofdvariant binnen de liquiditeitsratio-categorie, naast current en quick.",
            "confidence": "inferred"
        })

    rec.setdefault('_provenance', {})
    rec['_provenance']['last_touch'] = 'concept-extractie-v4-2026-05-19T-overnight-gap-fix'

    save_record(rec)
    print("OK liquiditeitsratio updated")


update_werkkapitaal()
update_liquiditeitsratio()
