import os, sys
os.chdir('/Users/stivni/Documents/ITAA/certificaid')
sys.path.insert(0, '/Users/stivni/Documents/ITAA/certificaid')
from tools.lib.records_api import save_record

record = {
    "id": "cash-ratio",
    "naam": "Cash ratio (liquiditeit in strenge zin)",
    "node_type": "cluster",
    "schema_version": "1.6",
    "status": "seed",
    "linked_anchors": ["1.3.II.C", "1.3.taak.1"],
    "naam_alternatief": ["Kasratio", "Cash ratio"],
    "_provenance": {
        "extractor_run": "concept-extractie-v4-2026-05-19T-overnight-gap-fix",
        "model": "claude-opus-4-7",
        "anchor_id": "1.3.II.C",
        "linked_anchors": ["1.3.II.C", "1.3.taak.1"],
        "reviewed_by": None,
        "bron_gap": "Geen Belgische trusted bron in de bundle voor de cash-ratio-formule. Standaard financial-analysis-doctrine. Confidence: inferred-common-knowledge."
    },
    "situering": {
        "text": "Cash ratio = (geldbeleggingen + liquide middelen) / schulden op ten hoogste een jaar. Het is de strengste liquiditeitstoets: ze meet hoeveel van de korte schulden onmiddellijk kunnen worden voldaan zonder beroep te doen op vorderingen of voorraden. In voorraadintensieve sectoren is dit de meest waardevolle van de drie liquiditeitsratio's omdat ze de illusie van liquiditeit door grote voorraden uitsluit.",
        "confidence": "inferred-common-knowledge",
        "source": {"type": "vakdoctrine", "short": "Algemene financial-analysis-doctrine"},
        "_provenance": {"inputs": [{"id": "anchor-1.3.II.C", "sha256": None, "version": "rag-v1"}]}
    },
    "definitie": {
        "text": "De cash ratio is de verhouding tussen de meest liquide vlottende activa (geldbeleggingen + liquide middelen) en de schulden op ten hoogste een jaar. Ze toont in welke mate de onderneming haar korte schulden onmiddellijk en zonder operationele tussenstappen zou kunnen voldoen.",
        "confidence": "inferred-common-knowledge",
        "source": {"type": "vakdoctrine", "short": "Algemene financial-analysis-doctrine"},
        "_provenance": {"inputs": [{"id": "anchor-1.3.II.C", "sha256": None, "version": "rag-v1"}]}
    },
    "bouwstenen": [
        {
            "titel": "Enkel cash en cash-equivalenten",
            "wat": "Tel rubriek VIII (geldbeleggingen) + rubriek IX (liquide middelen) op en deel door de schulden op ten hoogste een jaar. Voorraden en handelsvorderingen worden — anders dan bij quick ratio en current ratio — niet meegerekend.",
            "waarom": "Geldbeleggingen en liquide middelen zijn binnen de dag beschikbaar. Vorderingen vergen nog inning; voorraad vergt nog verkoop. Bij acute crisis valt enkel echte cash terug.",
            "grondslag": "Vakdoctrine financial analysis",
            "confidence": "inferred-common-knowledge",
            "source": {"type": "vakdoctrine", "short": "Financial analysis"},
            "_provenance": {"inputs": [{"id": "anchor-1.3.II.C", "sha256": None, "version": "rag-v1"}]},
            "voorbeelden": [
                {
                    "vorm": "eenvoudig",
                    "omschrijving": "Rotex Roeselare NV: geldbeleggingen € 500.000 + liquide middelen € 800.000 = € 1.300.000. Korte schulden € 4.000.000. Cash ratio = € 1.300.000 / € 4.000.000 = 0,325."
                }
            ]
        },
        {
            "titel": "Strengste van de drie",
            "wat": "Current ratio > quick ratio > cash ratio. Hoe lager je in deze hiërarchie zakt, hoe strenger de toets en hoe minder vlottende-activa-categorieën meetellen.",
            "waarom": "Een lage cash ratio is niet meteen alarmerend (bedrijven houden bewust weinig kasreserve), maar samen met andere zwakke signalen (lage solvabiliteit, dalende quick ratio) wordt ze diagnostisch.",
            "grondslag": "Vakdoctrine",
            "confidence": "inferred-common-knowledge",
            "source": {"type": "vakdoctrine", "short": "Financial analysis"},
            "_provenance": {"inputs": [{"id": "anchor-1.3.II.C", "sha256": None, "version": "rag-v1"}]}
        }
    ],
    "berekeningsmethode": [
        {
            "naam": "Berekening cash ratio",
            "ratio": "De onmiddellijk beschikbare middelen tegenover de schulden die binnen het jaar betaald moeten worden. Strenger dan current of quick omdat enkel cash en cash-equivalenten in de teller staan.",
            "source": {"type": "vakdoctrine", "short": "Financial analysis"},
            "confidence": "inferred-common-knowledge",
            "_provenance": {"inputs": [{"id": "anchor-1.3.II.C", "sha256": None, "version": "rag-v1"}]},
            "formules": [
                {
                    "id": "cash-ratio-formule",
                    "naam": "Cash ratio",
                    "wiskunde": "cash ratio = (geldbeleggingen + liquide middelen) / schulden op ten hoogste een jaar",
                    "variabelen": [
                        {"symbool": "geldbeleggingen", "betekenis": "Balansrubriek VIII (geldbeleggingen, kortlopende effecten)", "eenheid": "EUR"},
                        {"symbool": "liquide middelen", "betekenis": "Balansrubriek IX (kas, bank, postcheque)", "eenheid": "EUR"},
                        {"symbool": "schulden op ten hoogste een jaar", "betekenis": "Passiefrubriek IX (financiële, handels, fiscale, sociale en andere schulden ≤ 1 jaar) + overlopende rekeningen passief", "eenheid": "EUR"}
                    ],
                    "invulling_voorbeeld": {
                        "waarden": "Rotex: geldbeleggingen € 500.000; liquide middelen € 800.000; korte schulden € 4.000.000",
                        "berekening": "(€ 500.000 + € 800.000) / € 4.000.000 = € 1.300.000 / € 4.000.000 = 0,325",
                        "eenheid_resultaat": "verhoudingsgetal"
                    }
                }
            ],
            "stappen": [
                {
                    "nr": 1,
                    "titel": "Lees geldbeleggingen en liquide middelen",
                    "wat": "Open de balans, neem de bedragen uit rubriek VIII (geldbeleggingen) en rubriek IX (liquide middelen) op activazijde.",
                    "waarom": "Dit zijn de twee balansrubrieken die binnen de dag in cash beschikbaar zijn.",
                    "input": [{"artefact": "Balans (actief)", "veld": "Rubrieken VIII en IX", "type": "boekhoudkundig-bedrag"}],
                    "output": [{"artefact": "Werkblad", "veld": "Totaal cash + equivalenten", "type": "boekhoudkundig-bedrag"}],
                    "hoe": "1. Voor Rotex: rubriek VIII = € 500.000, rubriek IX = € 800.000.\n2. Som = € 1.300.000.\n",
                    "grondslag": "KB WVV balansschema"
                },
                {
                    "nr": 2,
                    "titel": "Lees schulden op ten hoogste een jaar",
                    "wat": "Neem passiefrubriek IX (financiële, handels, fiscale, sociale, andere schulden ≤ 1 jaar) + overlopende rekeningen passief.",
                    "waarom": "Dit zijn de verplichtingen die binnen 12 maanden moeten worden voldaan.",
                    "input": [{"artefact": "Balans (passief)", "veld": "Rubriek IX + overlopende rekeningen", "type": "boekhoudkundig-bedrag"}],
                    "output": [{"artefact": "Werkblad", "veld": "Totaal korte schulden", "type": "boekhoudkundig-bedrag"}],
                    "hoe": "1. Voor Rotex: rubriek IX totaal = € 3.800.000 + overlopende rekeningen passief = € 200.000.\n2. Som = € 4.000.000.\n",
                    "grondslag": "KB WVV balansschema"
                },
                {
                    "nr": 3,
                    "titel": "Bereken de verhouding",
                    "wat": "Deel cash + equivalenten door de korte schulden.",
                    "waarom": "Geeft de strengste maatstaf: kan de onderneming morgen zonder hulp van vorderingen of voorraden alle korte schulden voldoen?",
                    "input": [{"artefact": "Werkblad", "veld": "Teller en noemer", "type": "boekhoudkundig-bedrag"}],
                    "output": [{"artefact": "Ratio-tabel", "veld": "Cash ratio", "type": "verhoudingsgetal"}],
                    "hoe": "1. € 1.300.000 / € 4.000.000 = 0,325.\n2. Plaats in evolutie + samen met current en quick: trio toont volledig liquiditeitsbeeld.\n",
                    "voorbeeld": {
                        "scenario": "Rotex Roeselare NV — boekjaar 20X1.",
                        "substappen": [
                            {
                                "nr": 1,
                                "titel": "Inputgegevens balans",
                                "type": "balans",
                                "data": "| Rotex Roeselare NV — extractie balans      | Bedrag (€) |\n|--------------------------------------------|-----------:|\n| Geldbeleggingen (VIII)                     |    500.000 |\n| Liquide middelen (IX)                      |    800.000 |\n| **Totaal cash + equivalenten**             | **1.300.000** |\n| Schulden ≤ 1 jaar (incl. overlopende pass) |  4.000.000 |"
                            },
                            {
                                "nr": 2,
                                "titel": "Berekening cash ratio",
                                "type": "berekening",
                                "data": "Cash ratio = € 1.300.000 / € 4.000.000 = **0,325**"
                            }
                        ]
                    },
                    "grondslag": "Vakdoctrine financial analysis"
                }
            ],
            "concreet_voorbeeld": {
                "scenario": "Rotex Roeselare NV: geldbeleggingen € 500.000 + liquide middelen € 800.000 = € 1.300.000; korte schulden € 4.000.000.",
                "berekening": "Cash ratio = € 1.300.000 / € 4.000.000 = 0,325.",
                "resultaat": "Een cash ratio van 0,325 betekent dat Rotex met onmiddellijk beschikbare cash slechts 32,5 % van haar korte schulden zou kunnen voldoen. Voor een productie-onderneming met current ratio 2,0 en quick ratio 1,375 is dit niet alarmerend — voorraden en vorderingen vullen de rest aan. Bij een dienstverlener zonder voorraden zou diezelfde cash ratio te laag zijn."
            }
        }
    ],
    "in_praktijk": [
        {
            "aspect": "Strengste liquiditeitstoets",
            "betekenis": "Bij examenvragen 'welke ratio test de meest acute betaalkracht?' of 'welke ratio sluit voorraden én vorderingen uit?' is het antwoord altijd cash ratio. Ze meet de pure kassituatie zonder operationele tussenschakels.",
            "anker_slug": "1.3.II.C",
            "confidence": "inferred-common-knowledge",
            "source": {"type": "vakdoctrine", "short": "Financial analysis"},
            "_provenance": {"inputs": [{"id": "anchor-1.3.II.C", "sha256": None, "version": "rag-v1"}]}
        },
        {
            "aspect": "Geen vaste norm",
            "betekenis": "Anders dan current ratio (norm rond 1-2) of quick ratio (norm rond 1) heeft cash ratio geen algemeen aanvaarde minimumwaarde. Bedrijven optimaliseren bewust hun kaspositie: te hoge cash = niet productief belegd; te lage cash = liquiditeitsrisico. Interpretatie gebeurt steeds sectorgebonden en samen met de andere twee ratio's.",
            "anker_slug": "1.3.II.C",
            "confidence": "inferred",
            "source": {"type": "vakdoctrine", "short": "Financial analysis"},
            "_provenance": {"inputs": [{"id": "anchor-1.3.II.C", "sha256": None, "version": "rag-v1"}]}
        }
    ],
    "vergelijkingsparen": [
        {
            "vergelijking_met": "quick-ratio",
            "verschil": "Quick ratio neemt naast cash ook handelsvorderingen mee (alles behalve voorraden). Cash ratio sluit ook vorderingen uit en houdt alleen geldbeleggingen + liquide middelen. Cash is strenger.",
            "trigger": "Examenvraag 'liquiditeit in enge of strengste zin?': enge = quick (zonder voorraden); strengste = cash (zonder voorraden én vorderingen).",
            "_provenance": {"inputs": [{"id": "anchor-1.3.II.C", "sha256": None, "version": "rag-v1"}]}
        },
        {
            "vergelijking_met": "current-ratio",
            "verschil": "Current ratio neemt alle vlottende activa (inclusief voorraden + vorderingen). Cash ratio kijkt alleen naar onmiddellijk beschikbare middelen. Het verschil is groot voor voorraadintensieve sectoren.",
            "trigger": "Examenvraag 'liquiditeit in ruime versus strengste zin?': ruim = current; strengst = cash.",
            "_provenance": {"inputs": [{"id": "anchor-1.3.II.C", "sha256": None, "version": "rag-v1"}]}
        }
    ],
    "valkuilen": [
        {
            "text": "Een lage cash ratio is niet automatisch alarmerend. Bedrijven met sterke handelskrediet-positie en betrouwbare klanten houden bewust weinig cash aan om geen renteverlies te lijden. Bekijk altijd samen met quick ratio, rotatie van vorderingen en bankkredietruimte.",
            "confidence": "inferred-common-knowledge",
            "source": {"type": "vakdoctrine", "short": "Financial analysis"},
            "_provenance": {"inputs": [{"id": "anchor-1.3.II.C", "sha256": None, "version": "rag-v1"}]}
        },
        {
            "text": "Geldbeleggingen onder rubriek VIII zijn niet altijd echt liquide. Termijndeposito's op meer dan 3 maanden of niet-beursgenoteerde participaties horen er soms in maar zijn niet onmiddellijk te gelde te maken. Controleer de toelichting bij de geldbeleggingen vóór je ze als cash beschouwt.",
            "confidence": "inferred",
            "source": {"type": "vakdoctrine", "short": "Financial analysis"},
            "_provenance": {"inputs": [{"id": "anchor-1.3.II.C", "sha256": None, "version": "rag-v1"}]}
        }
    ],
    "edges": [
        {
            "type": "onderdeel-van",
            "target": "liquiditeitsratio",
            "redenering": "Cash ratio is de derde hoofdvariant van de liquiditeitsratio-categorie, naast current en quick.",
            "confidence": "inferred"
        },
        {
            "type": "vergelijkt-met",
            "target": "quick-ratio",
            "redenering": "Cash ratio (strengst, zonder voorraden én vorderingen) versus quick ratio (zonder voorraden).",
            "confidence": "inferred"
        },
        {
            "type": "vergelijkt-met",
            "target": "current-ratio",
            "redenering": "Cash ratio (strengst) versus current ratio (ruimst).",
            "confidence": "inferred"
        }
    ]
}

save_record(record)
print("OK cash-ratio saved")
