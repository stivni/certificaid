#!/usr/bin/env python3
"""Gap-fix PO 1.9 — 4 records updaten via records-API."""
import os
import json
os.chdir('/Users/stivni/Documents/ITAA/certificaid')

import sys
sys.path.insert(0, '/Users/stivni/Documents/ITAA/certificaid')

from tools.lib.records_api import save_record

REPO = '/Users/stivni/Documents/ITAA/certificaid'

def load(rec_id):
    p = os.path.join(REPO, 'data/concepten/records', rec_id + '.json')
    with open(p) as f:
        return json.load(f)

# ============================================================
# 1) ohlson-o-score : 3 edges toevoegen
# ============================================================
ohlson = load('ohlson-o-score')
existing_edges = ohlson.get('edges', [])
new_edges = [
    {
        "type": "vereist-kennis-van",
        "target": "werkkapitaal",
        "redenering": "Variabele 3 (NBK/TA) gebruikt netto bedrijfskapitaal — zelfde begrip als variabele 1 in Altman.",
        "confidence": "grounded"
    },
    {
        "type": "vereist-kennis-van",
        "target": "solvabiliteitsratio",
        "redenering": "Variabele 2 (VV/TA — schuldgraad) en indicator 5 (VV>TA — negatief eigen vermogen) zijn solvabiliteits-equivalenten.",
        "confidence": "grounded"
    },
    {
        "type": "vereist-kennis-van",
        "target": "current-ratio",
        "redenering": "Variabele 4 (VK/VlA — vlottende schulden / vlottende activa) is de inverse van de current-ratio.",
        "confidence": "grounded"
    },
    {
        "type": "getriggerd-door",
        "target": "falen-van-de-onderneming",
        "redenering": "Ohlson is een predictiemodel voor faillissement — falen is het te voorspellen fenomeen.",
        "confidence": "inferred"
    }
]
# Behoud de bestaande onderdeel-van; dedupliceer op (type,target)
existing_keys = {(e['type'], e['target']) for e in existing_edges}
for ne in new_edges:
    if (ne['type'], ne['target']) not in existing_keys:
        existing_edges.append(ne)
ohlson['edges'] = existing_edges
ohlson['_provenance']['note'] = "Gap-fix overnight 2026-05-19: edges uitgebreid (werkkapitaal, solvabiliteitsratio, current-ratio, falen) voor uniforme rijkheid met altman-z-score."
ohlson['_provenance']['touched_at'] = "2026-05-19T20:00:00Z"
save_record(ohlson)
print(f"OK ohlson-o-score: {len(ohlson['edges'])} edges")

# ============================================================
# 2) kasstroomoverzicht-drie-segmenten : edges toevoegen
# ============================================================
ksov = load('kasstroomoverzicht-drie-segmenten')
existing_edges = ksov.get('edges', [])
new_edges = [
    {
        "type": "bevat",
        "target": "cashflow-analyse",
        "redenering": "Het operationeel segment (CFO) is in essentie de cashflow-analyse, met BBK-correctie.",
        "confidence": "grounded"
    },
    {
        "type": "bevat",
        "target": "behoefte-aan-bedrijfskapitaal",
        "redenering": "Δ BBK is het verbindingsstuk tussen resultaat en operationele kasstroom — kern van het CFO-segment.",
        "confidence": "grounded"
    },
    {
        "type": "bevat",
        "target": "financiering-met-eigen-vermogen",
        "redenering": "Kapitaalverhogingen en dividenden zijn componenten van het CFF-segment.",
        "confidence": "grounded"
    },
    {
        "type": "bevat",
        "target": "financiering-met-derdenkapitaal",
        "redenering": "Nieuwe leningen en terugbetalingen zijn componenten van het CFF-segment.",
        "confidence": "grounded"
    }
]
existing_keys = {(e['type'], e['target']) for e in existing_edges}
for ne in new_edges:
    if (ne['type'], ne['target']) not in existing_keys:
        existing_edges.append(ne)
ksov['edges'] = existing_edges
ksov['_provenance']['note'] = "Gap-fix overnight 2026-05-19: edges toegevoegd (bevat → 4 gebaseerd-op-concepten) voor RAG-graph-retrieval."
ksov['_provenance']['touched_at'] = "2026-05-19T20:00:00Z"
save_record(ksov)
print(f"OK kasstroomoverzicht-drie-segmenten: {len(ksov['edges'])} edges")

# ============================================================
# 3) kwantitatieve-financiele-diagnose : edges toevoegen
# ============================================================
kfd = load('kwantitatieve-financiele-diagnose')
existing_edges = kfd.get('edges', [])
new_edges = [
    {
        "type": "bevat",
        "target": "altman-z-score",
        "redenering": "Altman is een van de twee gepresenteerde kwantitatieve diagnosemodellen.",
        "confidence": "grounded"
    },
    {
        "type": "bevat",
        "target": "ohlson-o-score",
        "redenering": "Ohlson is het tweede gepresenteerde kwantitatieve diagnosemodel.",
        "confidence": "grounded"
    },
    {
        "type": "getriggerd-door",
        "target": "falen-van-de-onderneming",
        "redenering": "Het synthese-doel van deze modellen is het voorspellen van faillissement.",
        "confidence": "inferred"
    }
]
existing_keys = {(e['type'], e['target']) for e in existing_edges}
for ne in new_edges:
    if (ne['type'], ne['target']) not in existing_keys:
        existing_edges.append(ne)
kfd['edges'] = existing_edges
kfd['_provenance']['note'] = "Gap-fix overnight 2026-05-19: edges toegevoegd (bevat → altman/ohlson, getriggerd-door → falen) voor expliciete graph-relaties."
kfd['_provenance']['touched_at'] = "2026-05-19T20:00:00Z"
save_record(kfd)
print(f"OK kwantitatieve-financiele-diagnose: {len(kfd['edges'])} edges")

# ============================================================
# 4) herstructurering-resultatenrekening : in_praktijk toevoegen
# ============================================================
hrr = load('herstructurering-resultatenrekening')
in_praktijk = hrr.get('in_praktijk', [])
new_items = [
    {
        "aspect": "Examen-relevantie: vier blokken én TW-isolatie",
        "betekenis": "Op het examen wordt getoetst of de stagiair een 'platte' resultatenrekening kan ontleden in (1) bedrijfs-, (2) financieel, (3) uitzonderlijk (oud schema) en (4) belastingblok, én daarbinnen de toegevoegde waarde kan isoleren. Vraag-type: 'herstructureer onderstaande RR' of 'bereken de TW uit volgende gegevens'. Antwoord moet beide niveaus tonen: blok-indeling én TW-detail.",
        "anker_slug": "1.9.III.B",
        "confidence": "inferred",
        "source": {
            "type": "vakdoctrine",
            "short": "Examencontext financiële analyse"
        },
        "_provenance": {
            "inputs": [
                {
                    "id": "anchor-1.9.III.B",
                    "sha256": None,
                    "version": "rag-v1"
                }
            ]
        }
    },
    {
        "aspect": "Verkort/microschema vraagt expliciete vermelding van beperking",
        "betekenis": "Bij analyse van een verkort- of microschema (zoals een kleine BV) moet de stagiair in het antwoord uitdrukkelijk aangeven dat de TW-berekening onvolledig blijft zonder toelichtingsinformatie. De examencorrector beoordeelt het zien van de beperking, niet het magisch invullen van ontbrekende cijfers.",
        "anker_slug": "1.9.III.C",
        "confidence": "inferred",
        "source": {
            "type": "vakdoctrine",
            "short": "KB WVV — verkort/microschema + examen-correctiepraktijk"
        },
        "_provenance": {
            "inputs": [
                {
                    "id": "anchor-1.9.III.C",
                    "sha256": None,
                    "version": "rag-v1"
                }
            ]
        }
    },
    {
        "aspect": "Concretisering Rotex Roeselare NV (volledig schema)",
        "betekenis": "Volledig schema RR: omzet € 30.000.000 + andere bedrijfsopbrengsten € 500.000 − aankopen handelsgoederen € 12.500.000 = TW € 18.000.000. Daaronder: personeelskosten − € 12.000.000, afschrijvingen − € 1.500.000, andere bedrijfskosten ≈ − € 1.500.000 → bedrijfsresultaat ≈ € 3.000.000. Financieel resultaat − € 600.000, belastingen − € 1.500.000 → nettoresultaat ≈ € 900.000 (cijfers zijn illustratief).",
        "anker_slug": "1.9.III.B",
        "confidence": "inferred",
        "source": {
            "type": "vakdoctrine",
            "short": "Voorbeeld-case Rotex Roeselare NV"
        },
        "_provenance": {
            "inputs": [
                {
                    "id": "anchor-1.9.III.B",
                    "sha256": None,
                    "version": "rag-v1"
                }
            ]
        }
    }
]
# Append nieuwe items (dedupliceer op aspect-titel)
existing_aspects = {p.get('aspect') for p in in_praktijk}
for ni in new_items:
    if ni['aspect'] not in existing_aspects:
        in_praktijk.append(ni)
hrr['in_praktijk'] = in_praktijk
hrr['_provenance']['note'] = "Gap-fix overnight 2026-05-19: in_praktijk-blok toegevoegd (3 items) voor uniforme rijkheid met andere methode-records in PO 1.9."
hrr['_provenance']['touched_at'] = "2026-05-19T20:00:00Z"
save_record(hrr)
print(f"OK herstructurering-resultatenrekening: {len(hrr['in_praktijk'])} in_praktijk items")

print("\nAll 4 records updated successfully.")
