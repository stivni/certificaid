#!/usr/bin/env python3
"""Create resultatenrekening record (high-prio strategic-pass)."""
import os
os.chdir('/Users/stivni/Documents/ITAA/certificaid')
from tools.lib.records_api import save_record

NOW = "2026-05-19T00:00:00Z"
RUN_ID = "overnight-gap-fix-PO-1.1-2026-05-19"

record = {
    "id": "resultatenrekening",
    "naam": "Resultatenrekening",
    "node_type": "cluster",
    "schema_version": "1.6",
    "status": "seed",
    "linked_anchors": [
        "1.1.II.O",
        "1.1.II.S",
        "1.1.II.Q",
        "1.2.III.B",
        "1.5.I"
    ],
    "_provenance": {
        "extractor_run": f"concept-extractie-v4-{NOW}",
        "model": "claude-opus-4-7",
        "anchor_id": "1.1.II.S",
        "dekt_ook_anchors": ["1.1.II.O", "1.1.II.Q", "1.2.III.B", "1.5.I"],
        "reviewed_by": None,
        "created_door": RUN_ID,
        "created_reden": "Centraal stagiair-concept ontbrak; vier PO 1.1-records linken via onderdeel-van naar resultatenrekening (gap-mining-rapport 2026-05-18)."
    },
    "definitie": {
        "text": "Het **periodieke overzicht** van alle kosten (klasse 6) en opbrengsten (klasse 7) van een boekjaar, geordend volgens rubrieken die het resultaat opbouwen in vier blokken: (1) **bedrijfsresultaat** (operationele activiteit), (2) **financieel resultaat** (kosten en opbrengsten van financieringsverrichtingen), (3) **niet-recurrent resultaat** (uitzonderlijke posten sinds KB 21/10/2018), (4) **belastingen** (vennootschapsbelasting, regularisaties, uitgestelde belastingen). Tussensaldi worden als 'subtotalen' getoond: bedrijfsresultaat → resultaat vóór belastingen → resultaat van het boekjaar. Onderdeel van de jaarrekening (KB WVV bijlagen 2, 3, 4 volgens schema-grootte).",
        "confidence": "grounded",
        "source": {
            "type": "kb",
            "short": "KB WVV art. 3:90 — 3:95 (resultatenrekening); bijlage 2 (volledig schema)"
        },
        "references": [
            {"type": "wet", "short": "WVV art. 3:1 (jaarrekeningplicht)"},
            {"type": "wet", "short": "MAR klasse 6 en 7"}
        ],
        "_provenance": {
            "inputs": [
                {"id": "KB-WVV-2019__art_3_90", "sha256": None, "version": "rag-v1"},
                {"id": "MAR-ondernemingen__art_6_part1", "sha256": None, "version": "rag-v1"}
            ]
        }
    },
    "bouwstenen": [
        {
            "titel": "Vier resultaatblokken naast elkaar",
            "wat": "De resultatenrekening toont in vier opeenvolgende blokken: bedrijfsresultaat (omzet en bedrijfskosten), financieel resultaat (rente-opbrengsten en -kosten, opbrengsten financiële vaste activa, koersverschillen), niet-recurrent resultaat (eenmalige meer-/minderwaarden, reorganisatiekosten), belastingen op het resultaat. Elke blok eindigt met een subtotaal; het laatste cumulatieve subtotaal is het resultaat van het boekjaar.",
            "waarom": "Stagiair en derde-lezer kunnen zo onderscheiden wat **recurrente** bedrijfsprestatie is en wat éénmalig of financiering-gerelateerd. Een onderneming met grote winst uit verkoop van een gebouw (niet-recurrent) is fundamenteel anders dan dezelfde winst uit operationele omzet.",
            "grondslag": "KB WVV art. 3:90; bijlage 2 schema",
            "confidence": "grounded",
            "source": {"type": "kb", "short": "KB WVV bijlage 2"},
            "_provenance": {
                "inputs": [{"id": "KB-WVV-2019__art_3_90", "sha256": None, "version": "rag-v1"}]
            },
            "voorbeelden": [
                {
                    "vorm": "eenvoudig",
                    "omschrijving": "Rotex Roeselare NV 20X1: bedrijfsresultaat € 1.250.000 (omzet € 12M − bedrijfskosten € 10,75M), financieel resultaat − € 180.000 (rentelast > rente-opbrengst), niet-recurrent resultaat + € 320.000 (meerwaarde verkoop oud magazijn), belastingen − € 348.000 → resultaat van het boekjaar € 1.042.000."
                }
            ]
        },
        {
            "titel": "Twee voorstellingsmodellen: aard versus functie",
            "wat": "Het volledige schema kent **twee voorstellingsmodellen** (KB WVV art. 3:91): de **kosten naar aard** (lijst van kostenrubrieken — handelsgoederen, diensten, personeelskosten, afschrijvingen, ...) of de **kosten naar functie** (toegerekend per activiteit — kostprijs verkoop, distributiekosten, administratiekosten, ...). In België is de naar-aard-voorstelling de gangbare default; naar-functie vooral bij multinationale groepen die IFRS-achtige presentatie volgen. Het verkort en het microschema kennen alleen naar-aard.",
            "waarom": "De keuze beïnvloedt wel de leesbaarheid maar niet het eindresultaat (totaal blijft hetzelfde). Naar aard sluit aan bij MAR klasse 6; naar functie vereist een analytische uitsplitsing per departement of activiteit.",
            "grondslag": "KB WVV art. 3:91; bijlage 2",
            "confidence": "grounded",
            "source": {"type": "kb", "short": "KB WVV art. 3:91"},
            "_provenance": {
                "inputs": [{"id": "KB-WVV-2019__art_3_90", "sha256": None, "version": "rag-v1"}]
            },
            "voorbeelden": [
                {
                    "vorm": "eenvoudig",
                    "omschrijving": "Naaiatelier Ninove BV gebruikt naar-aard-voorstelling (gangbaar Belgisch KMO): één lijn 'aankopen handelsgoederen', één lijn 'personeelskosten'. Aurelia Holding NV (consolidatieperspectief, IFRS-georiënteerd) presenteert naar functie: 'kostprijs verkochte goederen', 'distributiekosten', 'administratiekosten'."
                }
            ]
        },
        {
            "titel": "Schema-afhankelijke gedetailleerdheid",
            "wat": "Volledig schema kent ~25 rubrieken op de resultatenrekening; verkort schema groepeert tot ~12 rubrieken (samenvoeging van details); microschema beperkt zich tot ~7 rubrieken (basisstructuur). De groottecategorie van de vennootschap bepaalt welk schema verplicht is.",
            "waarom": "Kleinere ondernemingen krijgen administratieve verlichting; grotere moeten meer detail tonen voor externe gebruikers.",
            "grondslag": "KB WVV bijlagen 2, 3, 4",
            "confidence": "grounded",
            "source": {"type": "kb", "short": "KB WVV bijlagen 2-4"},
            "_provenance": {
                "inputs": [{"id": "KB-WVV-2019__art_3_90", "sha256": None, "version": "rag-v1"}]
            },
            "voorbeelden": [
                {
                    "vorm": "eenvoudig",
                    "omschrijving": "Meubelzaak Mertens BV (klein) toont op de RR één lijn 'Diensten en diverse goederen € 285.000' (rubriek 61). Rotex Roeselare NV (groot) splitst datzelfde bedrag op in onderhoud, huur, energiekosten, advieskosten, ICT-kosten — apart benoemd in de toelichting."
                }
            ]
        },
        {
            "titel": "Klasse 6 (kosten) en klasse 7 (opbrengsten)",
            "wat": "De resultatenrekening is de **synthese van de boekhoudkundige saldi** op rekeningen klasse 6 (kosten) en klasse 7 (opbrengsten). Elke transactie van het boekjaar die kost of opbrengst genereert, kantelt uiteindelijk in één van die rekeningen. Bij jaarafsluiting worden ze afgesloten tegen rekening 14 'Overgedragen resultaat' (zie eindejaarsverrichtingen stap 7).",
            "waarom": "Onderscheid tussen balansrekeningen (klasse 1-5, blijven over boekjaren heen) en resultaatrekeningen (klasse 6-7, leeggemaakt aan einde boekjaar). Zonder dit onderscheid zou je niet kunnen zeggen 'hoeveel was de winst dit jaar?'.",
            "grondslag": "MAR klasse 6 en 7",
            "confidence": "grounded",
            "source": {"type": "kb", "short": "MAR"},
            "_provenance": {
                "inputs": [{"id": "MAR-ondernemingen__art_6_part1", "sha256": None, "version": "rag-v1"}]
            },
            "voorbeelden": [
                {
                    "vorm": "eenvoudig",
                    "omschrijving": "Saldo rekening 60 'Aankopen handelsgoederen' € 850.000 op 31/12 → wordt op de RR getoond bij 'Handelsgoederen, grond- en hulpstoffen'. Saldo rekening 70 'Omzet' € 2.150.000 → top van de RR. Verschil bouwt mee aan bedrijfsresultaat."
                }
            ]
        }
    ],
    "in_praktijk": [
        "De resultatenrekening leest 'van boven naar beneden' als een trechter: omzet → bedrijfsresultaat → resultaat vóór belastingen → resultaat van het boekjaar. Examenscenario's vragen vaak: 'wat blijft over na X?' — werk dan **alleen door de juiste subtotalen heen**.",
        "Het bedrijfsresultaat is de meest betekenisvolle KPI voor operationele prestaties — daarom focusen analisten daarop, niet op het uiteindelijke nettoresultaat dat ook eenmalige en fiscale posten bevat.",
        "Een fiscaal-boekhoudkundig spanningsveld: belastingen op het resultaat worden geboekt vóór de bestemming van het resultaat (rekening 67/77). De resultatenrekening eindigt bij 'resultaat van het boekjaar te bestemmen' — de bestemming (dividend, reserves) is een aparte beweging op de balans, niet op de RR zelf.",
        "Bij vergelijking met vorig boekjaar: KB WVV legt op de vergelijkende cijfers te tonen (consistentiebeginsel). Niet-vergelijkbaarheid (bv. door schema-wijziging) moet expliciet worden gemotiveerd in de toelichting."
    ],
    "valkuilen": [
        {
            "text": "**Niet-recurrent** is niet hetzelfde als het oude '**uitzonderlijk resultaat**'. Sinds KB 21/10/2018 wordt 'uitzonderlijk' (klasse 66/76) onderdrukt en vervangen door **niet-recurrent bedrijfsresultaat** (76A/66A) en **niet-recurrent financieel resultaat** (76B/66B). Stagiairs die nog oude leerboeken hebben raken hier verward.",
            "confidence": "grounded",
            "source": {"type": "kb", "short": "KB 21/10/2018 op de jaarrekening"},
            "_provenance": {
                "inputs": [{"id": "KB-WVV-2019__art_3_90", "sha256": None, "version": "rag-v1"}]
            }
        },
        {
            "text": "Het 'resultaat van het boekjaar' op de resultatenrekening is **te bestemmen** — het is GEEN reserve. Reserves ontstaan pas na bestemming door de algemene vergadering (rekeningen 130-133). Klassieke examenvraag: 'is winst € 250.000 onmiddellijk beschikbaar voor dividend?' Nee — pas na AV-beslissing.",
            "confidence": "grounded",
            "source": {"type": "wet", "short": "WVV art. 5:142 / 7:212"},
            "_provenance": {
                "inputs": [{"id": "KB-WVV-2019__art_3_90", "sha256": None, "version": "rag-v1"}]
            }
        },
        {
            "text": "Resultatenrekening is **periodiek** (boekjaar), balans is **op één moment** (balansdatum). Een rubriek 'voorraad' staat op de balans (eindstand), terwijl 'voorraadwijziging' (delta openings- en eindvoorraad) op de RR staat — die twee samen gelezen tonen waarom het bedrijfsresultaat is wat het is.",
            "confidence": "grounded",
            "source": {"type": "kb", "short": "KB WVV"},
            "_provenance": {
                "inputs": [{"id": "KB-WVV-2019__art_3_90", "sha256": None, "version": "rag-v1"}]
            }
        }
    ],
    "vergelijkingsparen": [
        {
            "vergelijking_met": "balans",
            "verschil": "Balans = **vermogenspositie op één moment** (klasse 1-5, momentopname per balansdatum). Resultatenrekening = **kosten en opbrengsten over een periode** (klasse 6-7, flow over het boekjaar). Het saldo van de RR (winst/verlies) belandt op de balans als component van het eigen vermogen (rekening 14).",
            "trigger": "Examen: 'op welke staat staat post X?' — vraag jezelf: is dit een **toestand** (saldo: voorraad, schuld, kapitaal) of een **beweging** (gedurende boekjaar: omzet, kostprijs)?"
        }
    ],
    "edges": [
        {
            "type": "onderdeel-van",
            "target": "jaarrekening",
            "redenering": "Resultatenrekening is één van de drie verplichte onderdelen van de jaarrekening."
        },
        {
            "type": "vergelijkt-met",
            "target": "balans",
            "redenering": "Periodieke vs momentane voorstelling — frequente examen-verwarring."
        },
        {
            "type": "getriggerd-door",
            "target": "eindejaarsverrichtingen",
            "redenering": "Definitieve resultatenrekening pas na eindejaarsverrichtingen (afschrijvingen, voorzieningen, overlopende rekeningen)."
        }
    ],
    "voorbeelden": [
        {
            "vorm": "scenario",
            "titel": "Resultatenrekening verkort schema — Naaiatelier Ninove BV 20X1",
            "cast": ["Naaiatelier Ninove BV"],
            "omschrijving": "Naaiatelier Ninove BV (klein) maakt resultatenrekening 20X1 op in verkort schema (KB WVV bijlage 3).",
            "stappen": [
                "1. Verzamel saldi klasse 7 (opbrengsten): rekening 70 Omzet € 1.250.000 + rekening 74 Andere bedrijfsopbrengsten € 18.000.",
                "2. Verzamel saldi klasse 6 (kosten): rekening 60 Handelsgoederen € 720.000, rekening 61 Diensten € 145.000, rekening 62 Personeelskosten € 218.000, rekening 630 Afschrijvingen € 22.000.",
                "3. Bereken bedrijfsresultaat: (€ 1.250.000 + € 18.000) − (€ 720.000 + € 145.000 + € 218.000 + € 22.000) = € 163.000.",
                "4. Financieel resultaat: rente-opbrengsten € 1.200 − rente-kosten € 8.500 = − € 7.300.",
                "5. Geen niet-recurrente posten in 20X1.",
                "6. Resultaat vóór belasting € 155.700; vennootschapsbelasting ≈ € 31.140 (KMO-tarief 20 % op eerste schijf, vereenvoudigd).",
                "7. Resultaat van het boekjaar te bestemmen: € 124.560."
            ],
            "illustraties": [
                {
                    "type": "verslag-fragment",
                    "titel": "Resultatenrekening verkort schema 20X1",
                    "verslag_type": "resultatenrekening",
                    "paragraaf_context": "Bijlage 3 KB WVV — verkort schema",
                    "tekst": "| Rubriek | Bedrag |\n|---|---:|\n| 70/74 Bedrijfsopbrengsten | € 1.268.000 |\n| 60/64 Bedrijfskosten | (€ 1.105.000) |\n| **9901 Bedrijfsresultaat** | **€ 163.000** |\n| 75 Financiële opbrengsten | € 1.200 |\n| 65 Financiële kosten | (€ 8.500) |\n| **9903 Resultaat vóór belasting** | **€ 155.700** |\n| 67/77 Belastingen op het resultaat | (€ 31.140) |\n| **9904 Resultaat van het boekjaar** | **€ 124.560** |"
                }
            ]
        }
    ],
    "situering": "Een van de drie verplichte stukken van de jaarrekening — naast balans en toelichting. Voor de stagiair-GA centraal omdat **alle PO 1.1-rubrieken die met kosten of opbrengsten te maken hebben** (bedrijfsresultaat, financiële verrichtingen, niet-recurrent resultaat) hier uiteindelijk landen. Examenvraag-typen: 'in welk subtotaal valt deze transactie?', 'is dit recurrent of niet-recurrent?', 'naar aard of naar functie?'.",
    "naam_alternatief": "income statement / profit and loss / compte de résultats"
}

save_record(record)
print("OK: resultatenrekening opgeslagen")
