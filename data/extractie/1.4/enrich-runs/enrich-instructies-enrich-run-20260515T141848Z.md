# ENRICH-run enrich-run-20260515T141848Z — Instructies voor Opus-subagent

**Programmaonderdeel**: 1.4
**Run-id**: enrich-run-20260515T141848Z
**Gegenereerd op**: 2026-05-15T14:18:48+00:00
**Records te verwerken**: 7
**Gaps te verwerken**: 8

## Jouw taak

Verrijk de onderstaande concept-records door de gevraagde gaps in te vullen.
Werk conform `prompts/concept-enrich-v1.md` (prompt hieronder als referentie).

**Hard contract** (herhaling van de prompt):
- Behoud álle bestaande velden en array-items.
- Corrigeren mag — verplicht met `corrected_from` + `correction_reason` + bron.
- Verwijderen verboden.
- Alleen gevraagde gaps verwerken.

## Na je run

Na het verwerken van alle records, schrijf een korte samenvatting naar stdout
zoals beschreven in de prompt.

**Markeer GEEN gap-statussen** — dat doet `enrich_records.py --markeer-gaps-na-run`.

---

## Records en gaps


## Record: `consolidatieverschil`

**Gaps te verwerken** (2 stuks):

```json
[
  {
    "record_id": "consolidatieverschil",
    "aspect": "definitie.onvolledig",
    "reden": "Examenvragen 2013-2 vr8 en 2015-1 vr11 vragen 'de vier voornaamste oorzaken van positieve consolidatieverschillen' (8 punten). Het record telt slechts 3 oorzaken-entries onder oorzaken[], en één (verwachte ongunstige resultaatsontwikkeling) betreft bovendien negatief consolidatieverschil — er zijn dus slechts 2 echte positieve oorzaken. Een vierde positieve oorzaak (typisch: niet-geactiveerde immateriële waarde / merken / klantenbestand als afzonderlijke oorzaak naast goodwill voor synergieverwachting) ontbreekt om de examenvraag volledig te kunnen oplossen.",
    "prio": "hoog",
    "geconstateerd_door": "verify-run-20260515T141017Z",
    "geconstateerd_op": "2026-05-15T14:30:00+00:00",
    "status": "open"
  },
  {
    "record_id": "consolidatieverschil",
    "aspect": "vergelijkingsparen.vrije-tekst-niet-gespiegeld",
    "reden": "De definitie en bouwstenen verwijzen expliciet naar 'dochteronderneming' en 'geassocieerde onderneming' als bereik van het consolidatieverschil, maar deze concepten staan niet als vergelijkingsparen.vergelijking_met of in een edge — onderscheid dochter vs. geassocieerde is examen-relevant (vermogensmutatie versus integrale consolidatie raakt de berekening).",
    "prio": "midden",
    "geconstateerd_door": "verify-run-20260515T141017Z",
    "geconstateerd_op": "2026-05-15T14:30:00+00:00",
    "status": "open"
  }
]
```

**Bron-bundle**: `data/extractie/1.4/enrich-runs/bundle-consolidatieverschil-enrich-run-20260515T141848Z.json` — 458 chunks beschikbaar (bronnen: advies, norm, wettekst)

**Bestaand record** (`data/concept_records/consolidatieverschil.json`):

```json
{
  "id": "consolidatieverschil",
  "naam": "Consolidatieverschil",
  "node_type": "fenomeen",
  "schema_version": "1.2",
  "status": "seed",
  "linked_anchors": [
    "1.4.I.D",
    "1.4.I.G",
    "1.4.I.B",
    "1.4.I.E",
    "1.4.taak.1"
  ],
  "_provenance": {
    "extractor_run": "concept-extractie-v3-2026-05-15T13:36Z",
    "model": "claude-opus-4-7",
    "anchor_id": "1.4.I.D",
    "dekt_ook_anchors": [
      "1.4.I.G",
      "1.4.I.B",
      "1.4.I.E",
      "1.4.taak.1"
    ],
    "reviewed_by": null
  },
  "definitie": {
    "text": "Het verschil dat ontstaat bij de eerste consolidatie tussen (a) de aanschaffingswaarde van een deelneming in een dochter- of geassocieerde onderneming en (b) het overeenkomstige deel van het eigen vermogen van die onderneming op verwervingsdatum, na toerekening van het verschil aan onder-/overgewaardeerde activa en passiva. Het overblijvende verschil wordt in de geconsolideerde balans opgenomen onder de post 'Consolidatieverschillen', aan actiefzijde indien positief en aan passiefzijde indien negatief. Positieve consolidatieverschillen worden afgeschreven over de vermoedelijke gebruiksduur.",
    "confidence": "grounded",
    "source": {
      "type": "kb",
      "short": "KB WVV art. 3:130 jo. art. 3:131"
    },
    "references": [
      {
        "type": "kb",
        "short": "KB WVV art. 3:127, a) (compensatie)"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:128 (toerekening aan activa/passiva)"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:129 (datum van waardebepaling)"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:130 (boeking)"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:131 (afschrijving)"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:132 (gedeeltelijke realisatie)"
      },
      {
        "type": "advies",
        "short": "CBN 2022/11 — Vermogensmutatiemethode (consolidatieverschil bij vermogensmutatie)"
      },
      {
        "type": "advies",
        "short": "CBN 2013/3 — Step acquisitions (update)"
      }
    ],
    "_provenance": {
      "inputs": [
        {
          "id": "KB-WVV-2019__art_3_102",
          "sha256": null,
          "version": "rag-v1"
        },
        {
          "id": "KB-WVV-2019__art_3_103",
          "sha256": null,
          "version": "rag-v1"
        },
        {
          "id": "KB-WVV-2019__art_3_104",
          "sha256": null,
          "version": "rag-v1"
        },
        {
          "id": "CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_voorbeeld-1",
          "sha256": null,
          "version": "rag-v1"
        }
      ]
    }
  },
  "bouwstenen": [
    {
      "naam": "Positief consolidatieverschil",
      "text": "Ontstaat wanneer de aanschaffingswaarde van de deelneming het pro-rata aandeel in het eigen vermogen van de dochter (na toerekening aan onder-/overgewaardeerde activa) overstijgt. Boeking aan actiefzijde van de geconsolideerde balans. Wordt afgeschreven volgens een passend plan dat overeenstemt met de vermoedelijke gebruiksduur. Bij afschrijving over meer dan vijf jaar: motivering in toelichting verplicht (KB WVV art. 3:131, § 1).",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:131, § 1"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_103",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "naam": "Negatief consolidatieverschil",
      "text": "Ontstaat wanneer de aanschaffingswaarde van de deelneming lager is dan het pro-rata aandeel in het eigen vermogen (na toerekening). Boeking aan passiefzijde van de geconsolideerde balans. Mag niet zomaar in de resultatenrekening worden opgenomen; uitzondering: indien het negatieve verschil te verklaren valt door een op verwervingsdatum verwachte ongunstige resultaatsontwikkeling, mag het worden opgenomen in resultaat naarmate die ongunstige ontwikkeling zich realiseert (KB WVV art. 3:131, § 2).",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:131, § 2"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_103",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "naam": "Geen compensatie tussen positief en negatief",
      "text": "Positieve en negatieve consolidatieverschillen mogen niet met elkaar worden gecompenseerd, tenzij zij betrekking hebben op dezelfde dochteronderneming — in dat geval is compensatie verplicht (KB WVV art. 3:130).",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:130"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_102",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "naam": "Gedeeltelijke realisatie van de aandelen",
      "text": "Ingeval de aandelen van een in de consolidatie opgenomen dochter geheel of gedeeltelijk buiten de consolidatiekring worden gerealiseerd, wordt het overblijvende consolidatieverschil afgeboekt naar verhouding van de gerealiseerde aandelen (KB WVV art. 3:132).",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:132"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_104",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "oorzaken": [
    {
      "text": "Overpaid goodwill — de moeder betaalt een premie boven het pro-rata aandeel in het netto-actief van de dochter (verwachte synergieën, marktpositie, immateriële waarde).",
      "confidence": "inferred-from-aggregation",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:130 (logica) + CBN-praktijk"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_voorbeeld-1",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "text": "Activa van de dochter zijn boekhoudkundig ondergewaardeerd (bv. terreinen tegen historische kostprijs); de moeder betaalt de werkelijke waarde. Eerste stap (KB WVV art. 3:128): verschil toerekenen aan die onder-/overgewaardeerde bestanddelen vooraleer het residu als consolidatieverschil wordt geboekt.",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:128 + CBN 2022/11 voorbeeld"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_voorbeeld",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "text": "Verwachte ongunstige resultaatsontwikkeling — een aanschaffingswaarde lager dan netto-actief op acquisitiedatum kan voortvloeien uit de verwachting van komende verliezen; dan negatief consolidatieverschil.",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:131, § 2"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_103",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "berekeningsmethode": [
    {
      "naam": "Berekening van het consolidatieverschil bij eerste consolidatie",
      "formule": "Consolidatieverschil = aanschaffingswaarde aandelen − belang% × eigen vermogen dochter op verwervingsdatum (na toerekening van het verschil aan onder-/overgewaardeerde activa en passiva van de dochter)",
      "ratio": "Het verschil reflecteert de kostprijs die de moeder bovenop (of onder) het netto-actief heeft betaald, na correctie voor stille meer-/minderwaarden in de dochter. Het residu vangt de niet aan specifieke activa toewijsbare goodwill (of badwill) op.",
      "stappen": [
        {
          "volgorde": 1,
          "text": "Bepaal de aanschaffingswaarde van de deelneming."
        },
        {
          "volgorde": 2,
          "text": "Bepaal het pro-rata aandeel (belang%) in het eigen vermogen van de dochter op verwervingsdatum (KB WVV art. 3:129)."
        },
        {
          "volgorde": 3,
          "text": "Bereken het bruto-verschil (stap 1 − stap 2)."
        },
        {
          "volgorde": 4,
          "text": "Reken het bruto-verschil zoveel mogelijk toe aan onder-/overgewaardeerde actief- of passiefbestanddelen van de dochter (KB WVV art. 3:128, art. 3:130)."
        },
        {
          "volgorde": 5,
          "text": "Het residu = consolidatieverschil. Positief → actiefzijde; negatief → passiefzijde (KB WVV art. 3:130)."
        }
      ],
      "concreet_voorbeeld": {
        "scenario": "M verwerft 100 % van D voor 1.000. Eigen vermogen D op verwervingsdatum = 700. M identificeert dat de terreinen van D voor 150 ondergewaardeerd zijn t.o.v. werkelijke waarde.",
        "berekening": "Stap 1: aanschaffingswaarde = 1.000. Stap 2: pro-rata EV = 100 % × 700 = 700. Stap 3: bruto-verschil = 1.000 − 700 = 300. Stap 4: 150 wordt toegerekend aan de terreinen (geconsolideerde balans: terreinen +150). Stap 5: residu = 300 − 150 = 150. Geboekt als 'Consolidatieverschillen' (actiefzijde), afgeschreven volgens passend plan.",
        "resultaat": "In de geconsolideerde balans wordt 150 als positief consolidatieverschil geboekt; de terreinen van D worden voor 150 opgewaardeerd. Het positieve consolidatieverschil wordt bv. over 5 jaar afgeschreven (30 per jaar in de geconsolideerde resultatenrekening, afzonderlijke post bij bedrijfs- of financiële kosten — KB WVV art. 3:131)."
      },
      "source": {
        "type": "kb",
        "short": "Synthese KB WVV art. 3:127 — 3:131; CBN 2022/11 voorbeeld"
      },
      "confidence": "inferred-from-aggregation",
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_102",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "KB-WVV-2019__art_3_103",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_voorbeeld",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "in_praktijk": [
    {
      "aspect": "Consolidatieverschil bij vermogensmutatie",
      "betekenis": "Ook bij toepassing van de vermogensmutatiemethode (geassocieerde onderneming) ontstaat een consolidatieverschil: het verschil tussen de boekwaarde van de deelneming en het pro-rata aandeel in het eigen vermogen wordt — na toerekening aan onder-/overgewaardeerde activa — geboekt als positief of negatief consolidatieverschil. Wordt afzonderlijk gevolgd en afgeschreven (CBN 2022/11).",
      "confidence": "grounded",
      "source": {
        "type": "advies",
        "short": "CBN 2022/11"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_voorbeeld",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "aspect": "Afzonderlijke post in de resultatenrekening",
      "betekenis": "De afschrijvingen op positieve consolidatieverschillen worden in de geconsolideerde resultatenrekening geboekt in een afzonderlijke post van de bedrijfskosten of van de financiële kosten — niet vermengd met de gewone afschrijvingen op de bestaande activa (KB WVV art. 3:131, § 1, lid 3).",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:131, § 1"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_103",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "vergelijkingsparen": [
    {
      "vergelijking_met": "integrale-consolidatie",
      "verschil": "Het consolidatieverschil is een gevolg van de techniek van integrale consolidatie (compensatie deelneming-eigen vermogen op verwervingsdatum). Het is niet de techniek zelf maar één bouwsteen ervan.",
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_102",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "vergelijking_met": "vermogensmutatiemethode",
      "verschil": "Bij vermogensmutatie wordt het consolidatieverschil onderscheiden van de balanspost 'Vennootschappen waarop vermogensmutatie is toegepast' en afzonderlijk afgeschreven (CBN 2022/11). Bij integrale consolidatie verschijnt het in de eigen post 'Consolidatieverschillen' op de balans.",
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_voorbeeld",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "vergelijking_met": "eerste-consolidatie",
      "verschil": "De eerste consolidatie is het tijdstip waarop het consolidatieverschil wordt vastgesteld. Wijzigingen in latere consolidaties wijzigen het verschil niet — alleen de afschrijving van een positief verschil en specifieke gebeurtenissen (gedeeltelijke realisatie, wijziging consolidatiekring) raken het.",
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_104",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "valkuilen": [
    {
      "text": "Het verschil tussen aanschaffingswaarde en EV op verwervingsdatum is niet onmiddellijk het consolidatieverschil. Eerst moet het worden toegerekend aan onder-/overgewaardeerde activa en passiva (KB WVV art. 3:128 jo. art. 3:130, lid 1). Pas het residu na deze toerekening wordt als 'Consolidatieverschillen' geboekt.",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:130"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_102",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "text": "Negatief consolidatieverschil mag niet 'gewoon' worden geboekt als winst. KB WVV art. 3:131, § 2 voorziet enkel een opname in resultaat wanneer het verschil te verklaren is door een verwachte ongunstige ontwikkeling van de dochter — en dan slechts naarmate die ontwikkeling zich realiseert.",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:131, § 2"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_103",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "text": "Aanvullende of niet-recurrente afschrijvingen moeten worden toegepast wanneer wijzigingen in de economische omstandigheden het niet langer rechtvaardigen het positieve consolidatieverschil tegen die waarde te behouden (KB WVV art. 3:131, § 1).",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:131, § 1"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_103",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ]
}
```

---

## Record: `evenredige-consolidatie`

**Gaps te verwerken** (1 stuks):

```json
[
  {
    "record_id": "evenredige-consolidatie",
    "aspect": "vergelijkingsparen.vrije-tekst-niet-gespiegeld",
    "reden": "De definitietekst van evenredige consolidatie verwijst naar 'gezamenlijke controle' en 'gemeenschappelijke dochteronderneming' als triggerend criterium en naar 'minderheidsbelangen' (afwezig bij evenredige methode) maar geen van deze drie staan als vergelijkingsparen.vergelijking_met. De vergelijking met vermogensmutatie/integraal staat wel, het verschil met de actor-concepten niet.",
    "prio": "midden",
    "geconstateerd_door": "verify-run-20260515T141017Z",
    "geconstateerd_op": "2026-05-15T14:30:00+00:00",
    "status": "open"
  }
]
```

**Bron-bundle**: `data/extractie/1.4/enrich-runs/bundle-evenredige-consolidatie-enrich-run-20260515T141848Z.json` — 438 chunks beschikbaar (bronnen: advies, norm, wettekst)

**Bestaand record** (`data/concept_records/evenredige-consolidatie.json`):

```json
{
  "id": "evenredige-consolidatie",
  "naam": "Evenredige consolidatie (proportionele consolidatie)",
  "node_type": "methode",
  "schema_version": "1.2",
  "status": "seed",
  "linked_anchors": [
    "1.4.I.D",
    "1.4.I.B",
    "1.4.II.C",
    "1.4.taak.1"
  ],
  "_provenance": {
    "extractor_run": "concept-extractie-v3-2026-05-15T13:36Z",
    "model": "claude-opus-4-7",
    "anchor_id": "1.4.I.D",
    "dekt_ook_anchors": [
      "1.4.I.B",
      "1.4.II.C",
      "1.4.taak.1"
    ],
    "reviewed_by": null
  },
  "doel": {
    "text": "Een gemeenschappelijke dochteronderneming (een vennootschap waarover een beperkt aantal vennoten gezamenlijke controle uitoefenen via overeenkomst) wordt in de geconsolideerde jaarrekening van elke gezamenlijk controlerende vennoot opgenomen naar rato van haar rechten in het kapitaal (of in de inbreng, voor kapitaalloze vennootschappen). Hiermee wordt enkel het pro-rata deel van de activa, passiva, opbrengsten en kosten meegenomen — zonder afzondering van 'aandeel van derden', want het derden-deel wordt eenvoudigweg niet opgenomen.",
    "confidence": "grounded",
    "source": {
      "type": "kb",
      "short": "KB WVV art. 3:124, 2° jo. art. 3:140"
    },
    "references": [
      {
        "type": "kb",
        "short": "KB WVV art. 3:124, 2°"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:140"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:139"
      }
    ],
    "_provenance": {
      "inputs": [
        {
          "id": "KB-WVV-2019__art_3_111",
          "sha256": null,
          "version": "rag-v1"
        },
        {
          "id": "KB-WVV-2019__art_3_110",
          "sha256": null,
          "version": "rag-v1"
        }
      ]
    }
  },
  "voorwaarden_toepassing": [
    {
      "text": "Er moet gezamenlijke controle bestaan over een gemeenschappelijke dochteronderneming (overeenkomst dat beleidsbeslissingen alleen met gemeenschappelijke instemming kunnen worden genomen).",
      "confidence": "grounded",
      "source": {
        "type": "advies",
        "short": "CBN 2017/02"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_algemeen",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "text": "Het bedrijf van de gemeenschappelijke dochter moet voldoende geïntegreerd zijn in dat van de gezamenlijk controlerende vennootschap. Is het bedrijf niet nauw geïntegreerd, dan kan in plaats van evenredige consolidatie de vermogensmutatiemethode worden toegepast (CBN 2013/3).",
      "confidence": "grounded",
      "source": {
        "type": "advies",
        "short": "CBN 2013/3"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_praktische-uitwerking",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "bouwstenen": [
    {
      "naam": "Pro-rata opname (KB WVV art. 3:140, b)",
      "text": "De actief- en passiefbestanddelen, rechten en verplichtingen, opbrengsten en kosten van de gemeenschappelijke dochter worden opgenomen naar rato van de rechten in het kapitaal (resp. in de inbreng) die door de consoliderende vennootschap en haar in de consolidatie opgenomen dochters worden gehouden.",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:140, b"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_111",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "naam": "Toepassing van de integrale-consolidatie-regels op het pro-rata deel (KB WVV art. 3:140, a)",
      "text": "Op de evenredig geconsolideerde gemeenschappelijke dochter zijn — voor het opgenomen pro-rata deel — de regels van toepassing inzake compensatie van de deelneming (KB WVV art. 3:127, a)), toerekening van het verschil aan onder-/overgewaardeerde activa (KB WVV art. 3:128), bepaling van de waarde op verwervingsdatum (KB WVV art. 3:129), boeking van het consolidatieverschil (KB WVV art. 3:130), afschrijving (KB WVV art. 3:131) en gedeeltelijke realisatie (KB WVV art. 3:132 en art. 3:133). Idem voor de eliminaties (KB WVV art. 3:134, 3:136, 3:138 en art. 3:139) op het pro-rata deel.",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:140, a"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_111",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "naam": "Geen 'aandeel van derden'-post",
      "text": "Anders dan bij integrale consolidatie kent de evenredige consolidatie geen post 'Belangen van derden' of 'Aandeel van derden in het resultaat' — het deel buiten de groep wordt niet opgenomen, zodat er geen derden-correctie nodig is.",
      "confidence": "inferred-from-aggregation",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:140 (de verwijzing naar KB WVV art. 3:137 ontbreekt)"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_111",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "KB-WVV-2019__art_3_108",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "berekeningsmethode": [
    {
      "naam": "Evenredige consolidatie — pro-rata opname",
      "formule": "Geconsolideerde post = (post moeder) + (post gemeenschappelijke dochter × belang%) − intragroep-eliminaties op het pro-rata deel",
      "ratio": "Bij gezamenlijke controle wordt de macht over de dochter gedeeld; de geconsolideerde jaarrekening reflecteert die gedeelde macht door enkel het overeenstemmend deel van activa, passiva, opbrengsten en kosten te tonen. Het deel buiten de groep wordt niet 'gecorrigeerd' via een derden-post (zoals bij integrale consolidatie), maar simpelweg niet opgenomen.",
      "stappen": [
        {
          "volgorde": 1,
          "text": "Bepaal het belangenpercentage (rechten in kapitaal / inbreng) van de consoliderende vennootschap in de gemeenschappelijke dochter."
        },
        {
          "volgorde": 2,
          "text": "Vermenigvuldig elke actief-, passief-, opbrengsten- en kostenpost van de dochter met dit percentage."
        },
        {
          "volgorde": 3,
          "text": "Voeg de pro-rata bedragen samen met de bedragen van de moeder en haar integraal geconsolideerde dochters."
        },
        {
          "volgorde": 4,
          "text": "Pas de compensatie- en eliminatieregels van KB WVV art. 3:127, 3:128, 3:130, 3:134, 3:136 toe op het pro-rata deel (KB WVV art. 3:140, a))."
        }
      ],
      "concreet_voorbeeld": {
        "scenario": "Vennootschap A en vennootschap B oefenen gezamenlijke controle uit over vennootschap X via een aandeelhoudersovereenkomst — elk bezit 50 % van het kapitaal. Balans X: materiële vaste activa 800; voorraden 200; kas 100; eigen vermogen 600; schulden 500. Resultatenrekening X: omzet 1.000; kosten 800; resultaat 200. A koopt voor 60 goederen bij X (intra-groepsverkoop, in voorraad bij A; X realiseerde daarop een winst van 10).",
        "berekening": "Pro-rata deel van A in X = 50 %.\nGeconsolideerde activa van X (vóór eliminatie): 50 % × (800 + 200 + 100) = 50 % × 1.100 = 550. Geconsolideerde schulden van X: 50 % × 500 = 250. Geconsolideerd eigen vermogen van X: 50 % × 600 = 300.\nGeconsolideerde omzet uit X: 50 % × 1.000 = 500. Geconsolideerde kosten uit X: 50 % × 800 = 400. Geconsolideerd resultaat uit X (vóór eliminatie): 50 % × 200 = 100.\nIntra-groepselimatie (KB WVV art. 3:140 jo. art. 3:134, op pro-rata deel): de winst op de intra-groepsverkoop wordt geëlimineerd voor 50 % × 10 = 5 (deel van A in het pro-rata aandeel). Geconsolideerde voorraden A worden met 5 verminderd; geconsolideerd resultaat met 5 verminderd.",
        "resultaat": "In de geconsolideerde balans van A worden 550 activa en 250 schulden uit X opgenomen (na eliminatie 545 activa); 100 resultaat van X wordt voor 50 % meegenomen, verminderd met de intra-groepselimatie van 5 → 95. Er is géén post 'Aandeel van derden in resultaat' bij evenredige consolidatie — de overige 50 % van X verschijnt niet in de geconsolideerde jaarrekening van A (B doet dezelfde oefening voor haar 50 %)."
      },
      "source": {
        "type": "kb",
        "short": "Synthese KB WVV art. 3:140 jo. art. 3:127 — 3:138"
      },
      "confidence": "inferred-from-aggregation",
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_111",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "KB-WVV-2019__art_3_106",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_voorbeeld-2",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "in_praktijk": [
    {
      "aspect": "Wanneer toepassen",
      "betekenis": "Standaard voor gemeenschappelijke dochters bij gezamenlijke controle. Uitzondering: bij gemeenschappelijke dochters die niet nauw geïntegreerd zijn in het bedrijf van de moeder, kan vermogensmutatie worden gebruikt (CBN 2013/3).",
      "herkenningspunt": "Gezamenlijke controle (overeenkomst, vetorecht) → evenredig.",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:124, 2°"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_111",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_praktische-uitwerking",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "vergelijkingsparen": [
    {
      "vergelijking_met": "integrale-consolidatie",
      "verschil": "Integraal = 100 % opname met afzondering van derden-deel. Evenredig = pro-rata opname (% kapitaaldeelname), geen derden-post. Trigger: type controle (exclusief vs. gezamenlijk).",
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_98",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "KB-WVV-2019__art_3_111",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "vergelijking_met": "vermogensmutatiemethode",
      "verschil": "Evenredige consolidatie = activa/passiva regel voor regel pro-rata opgenomen (gedeelde controle). Vermogensmutatie = deelneming als één gesynthetiseerde post (invloed van betekenis, of niet-geïntegreerde gemeenschappelijke dochter). Bij gezamenlijke controle is evenredig de regel, vermogensmutatie de uitzondering.",
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_praktische-uitwerking",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "valkuilen": [
    {
      "text": "Het opgenomen pro-rata deel volgt het belangenpercentage (rechten in kapitaal), niet het controlepercentage. Een 50/50 joint venture wordt aldus voor 50 % opgenomen, ook al heeft elke vennoot via de overeenkomst eigenlijk een gelijke beleidsmacht.",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:140, b"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_111",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "text": "Intra-groepsverkopen tussen de moeder en de gemeenschappelijke dochter worden geëlimineerd op het pro-rata deel — niet voor 100 %. Andere bronnen (oudere W.Venn., IFRS 11) kennen andere regels; in WVV-context geldt de pro-rata eliminatie.",
      "confidence": "inferred-from-aggregation",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:140, a"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_111",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ]
}
```

---

## Record: `exclusieve-controle`

**Gaps te verwerken** (1 stuks):

```json
[
  {
    "record_id": "exclusieve-controle",
    "aspect": "in_praktijk.ontbreekt",
    "reden": "Slechts 1 in_praktijk-entry voor een centraal concept dat de keuze tussen integrale consolidatie en de andere methoden bepaalt. Voorbeeld van 'controle in feite' (bestuurdersbenoeming bij twee opeenvolgende AV's) ontbreekt, evenals het onderscheid > 50 % stemrechten versus de andere onweerlegbare vermoedens.",
    "prio": "midden",
    "geconstateerd_door": "verify-run-20260515T141017Z",
    "geconstateerd_op": "2026-05-15T14:30:00+00:00",
    "status": "open"
  }
]
```

**Bron-bundle**: `data/extractie/1.4/enrich-runs/bundle-exclusieve-controle-enrich-run-20260515T141848Z.json` — 427 chunks beschikbaar (bronnen: advies, norm, wettekst)

**Bestaand record** (`data/concept_records/exclusieve-controle.json`):

```json
{
  "id": "exclusieve-controle",
  "naam": "Exclusieve controle",
  "node_type": "begrip",
  "schema_version": "1.2",
  "status": "seed",
  "linked_anchors": [
    "1.4.I.C",
    "1.4.I.B",
    "1.4.I.D",
    "1.4.taak.1"
  ],
  "_provenance": {
    "extractor_run": "concept-extractie-v3-2026-05-15T13:36Z",
    "model": "claude-opus-4-7",
    "anchor_id": "1.4.I.C",
    "dekt_ook_anchors": [
      "1.4.I.B",
      "1.4.I.D",
      "1.4.taak.1"
    ],
    "reviewed_by": null
  },
  "definitie": {
    "text": "De controle die één vennootschap alleen uitoefent over een andere vennootschap, in tegenstelling tot gezamenlijke controle waarbij meerdere vennoten samen beslissen. Exclusieve controle wordt onweerlegbaar vermoed wanneer een vennootschap rechtstreeks of via dochterondernemingen meer dan de helft van de stemrechten verbonden aan de aandelen van een andere vennootschap bezit, of het recht heeft om de meerderheid van de bestuurders te benoemen of te ontslaan.",
    "confidence": "inferred-from-aggregation",
    "source": {
      "type": "wet",
      "short": "WVV art. 1:14, § 2 jo. art. 1:16"
    },
    "references": [
      {
        "type": "wet",
        "short": "WVV art. 1:14, § 2"
      },
      {
        "type": "wet",
        "short": "WVV art. 1:16"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:124"
      },
      {
        "type": "advies",
        "short": "CBN 2022/03 — Beoordeling groottecriteria"
      }
    ],
    "_provenance": {
      "inputs": [
        {
          "id": "CBN-2022-03-beoordeling-van-de-groottecriteria-overeenkomstig-artikelen-124-en-125-van-het-wetboek-van__sec_consolidatie-moedervennootschap",
          "sha256": null,
          "version": "rag-v1"
        },
        {
          "id": "CBN-2022-11-vermogensmutatiemethode__sec_toepassingsgebied",
          "sha256": null,
          "version": "rag-v1"
        }
      ]
    }
  },
  "in_praktijk": [
    {
      "aspect": "Gevolg voor consolidatiemethode",
      "betekenis": "Exclusieve controle triggert verplichte integrale consolidatie van de dochteronderneming (KB WVV art. 3:124, 1°). Alle actief- en passiefbestanddelen, rechten en verplichtingen, opbrengsten en kosten worden integraal opgenomen; het deel buiten de groep wordt afgezonderd als belangen van derden.",
      "herkenningspunt": "Examenopgave: 'M bezit 80 % van de stemrechten van D' → exclusieve controle in rechte → integrale consolidatie van D in M.",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:124, 1°"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_98",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "voorwaarden": [
    {
      "text": "Bezit (rechtstreeks of via dochters) van meer dan de helft van de stemrechten — onweerlegbaar vermoeden van controle in rechte.",
      "confidence": "inferred-from-aggregation",
      "source": {
        "type": "wet",
        "short": "WVV art. 1:14, § 2, 1°"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_toepassingsgebied",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "text": "Statutaire of contractuele macht om de meerderheid van de bestuurders of zaakvoerders te benoemen of te ontslaan.",
      "confidence": "inferred-from-aggregation",
      "source": {
        "type": "wet",
        "short": "WVV art. 1:14, § 2"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_toepassingsgebied",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "text": "Controle in feite — afgeleid uit het feit dat de vennootschap met haar effectieve stemrechten gedurende de twee laatste algemene vergaderingen de meerderheid van de bestuurders heeft kunnen aanstellen.",
      "confidence": "inferred",
      "source": {
        "type": "wet",
        "short": "WVV art. 1:14, § 2 (controle in feite)"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_77",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "vergelijkingsparen": [
    {
      "vergelijking_met": "gezamenlijke-controle",
      "verschil": "Exclusieve controle = één vennootschap alleen beslist; gezamenlijke controle = vereiste gemeenschappelijke instemming van een beperkt aantal vennoten. Exclusief → integrale consolidatie; gezamenlijk → evenredige consolidatie of vermogensmutatie.",
      "trigger": "Cruciale vraag: bestaat een overeenkomst dat beleidsbeslissingen alleen samen mogen worden genomen? Zo ja: gezamenlijke controle; anders: exclusieve controle of geen controle.",
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_algemeen",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "vergelijking_met": "invloed-van-betekenis",
      "verschil": "Exclusieve controle = beslissende invloed (eenzijdig sturen); invloed van betekenis = significante maar niet beslissende invloed (deelname zonder dominantie). Drempelmatig: > 50 % → controle (in rechte); 20–50 % → vermoeden van invloed van betekenis.",
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_praktische-uitwerking",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "drempelwaarden": [
    {
      "naam": "Onweerlegbaar vermoeden van controle in rechte",
      "waarde": "> 50 %",
      "eenheid": "stemrechten",
      "gevolg": "Onweerlegbaar vermoeden van exclusieve controle → moedervennootschap → integrale consolidatie van de dochter.",
      "source": {
        "type": "wet",
        "short": "WVV art. 1:14, § 2, 1°"
      },
      "confidence": "inferred-from-aggregation",
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_toepassingsgebied",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "valkuilen": [
    {
      "text": "Bij exact 50 % zonder stemovereenkomst is er géén exclusieve controle. Het loutere bezit van precies de helft van de stemrechten is onvoldoende; de wet eist 'meer dan de helft'.",
      "confidence": "grounded",
      "source": {
        "type": "advies",
        "short": "CBN 2017/02 — geval 2"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_geval-2-de-vennootschap-a-en-de-vennootschap-b-hebben-geen-o_2",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ]
}
```

---

## Record: `geconsolideerd-jaarverslag`

**Gaps te verwerken** (1 stuks):

```json
[
  {
    "record_id": "geconsolideerd-jaarverslag",
    "aspect": "in_praktijk.ontbreekt",
    "reden": "Record heeft slechts 1 in_praktijk-entry, 1 valkuil en 1 vergelijkingspaar terwijl het concept centraal staat in art. 3:32/3:35 WVV (inhoudsvereisten, risico's, niet-financiële verklaring, beschrijving deelnemingen). Te dun voor een coherente minicursus-paragraaf naast geconsolideerde-jaarrekening.",
    "prio": "midden",
    "geconstateerd_door": "verify-run-20260515T141017Z",
    "geconstateerd_op": "2026-05-15T14:30:00+00:00",
    "status": "open"
  }
]
```

**Bron-bundle**: `data/extractie/1.4/enrich-runs/bundle-geconsolideerd-jaarverslag-enrich-run-20260515T141848Z.json` — 240 chunks beschikbaar (bronnen: advies, norm, wettekst)

**Bestaand record** (`data/concept_records/geconsolideerd-jaarverslag.json`):

```json
{
  "id": "geconsolideerd-jaarverslag",
  "naam": "Geconsolideerd jaarverslag",
  "node_type": "begrip",
  "schema_version": "1.2",
  "status": "seed",
  "linked_anchors": [
    "1.4.I.F",
    "1.4.I.C",
    "1.4.II.C",
    "1.4.taak.1"
  ],
  "_provenance": {
    "extractor_run": "concept-extractie-v3-2026-05-15T13:36Z",
    "model": "claude-opus-4-7",
    "anchor_id": "1.4.I.F",
    "dekt_ook_anchors": [
      "1.4.I.C",
      "1.4.II.C",
      "1.4.taak.1"
    ],
    "reviewed_by": null
  },
  "definitie": {
    "text": "Het door het bestuursorgaan opgestelde toelichtende verslag dat samen met de geconsolideerde jaarrekening wordt opgemaakt, gecontroleerd en bekendgemaakt door elke consolidatieplichtige moedervennootschap (of, voor een consortium, gezamenlijk door de leden). Beschrijft de evolutie van de zaken, het resultaat en de positie van de geconsolideerde groep; verwijst naar belangrijke gebeurtenissen na balansdatum, voornaamste risico's en onzekerheden, vooruitzichten, en alle informatie die door de wet of door de regels van behoorlijke ondernemingscommunicatie vereist is.",
    "confidence": "inferred-from-aggregation",
    "source": {
      "type": "wet",
      "short": "WVV art. 3:32 (jaarverslag); art. 3:35 (gecondenseerd voor consolidatie)"
    },
    "references": [
      {
        "type": "wet",
        "short": "WVV art. 3:32 (algemeen jaarverslag)"
      },
      {
        "type": "advies",
        "short": "CBN 2022/11 — Toepassingsgebied (vermelding plicht jaarverslag)"
      },
      {
        "type": "advies",
        "short": "CBN 2022/09 — Consolidatieverplichting bij consortium"
      },
      {
        "type": "richtlijn",
        "short": "Richtlijn 2013/34/EU art. 29"
      }
    ],
    "_provenance": {
      "inputs": [
        {
          "id": "CBN-2022-11-vermogensmutatiemethode__sec_toepassingsgebied",
          "sha256": null,
          "version": "rag-v1"
        },
        {
          "id": "CBN-2022-09-consolidatie-bij-de-horizontale-groep-consortium-0__sec_consolidatieverplichting-consoliderende-vennootschap",
          "sha256": null,
          "version": "rag-v1"
        }
      ]
    }
  },
  "in_praktijk": [
    {
      "aspect": "Samen met de jaarrekening",
      "betekenis": "De moedervennootschap die consolidatieplichtig is, moet niet alleen een geconsolideerde jaarrekening opmaken, maar ook een jaarverslag daarover, dat moet worden gecontroleerd en bekendgemaakt (CBN 2022/11). Bij een consortium gebeurt dit gezamenlijk door de leden (CBN 2022/09).",
      "confidence": "grounded",
      "source": {
        "type": "advies",
        "short": "CBN 2022/11; CBN 2022/09"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_toepassingsgebied",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "CBN-2022-09-consolidatie-bij-de-horizontale-groep-consortium-0__sec_consolidatieverplichting-consoliderende-vennootschap",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "vergelijkingsparen": [
    {
      "vergelijking_met": "geconsolideerde-jaarrekening",
      "verschil": "De jaarrekening is het cijfermatige product (balans, resultatenrekening, toelichting). Het jaarverslag is het narratieve, toelichtende stuk. Beide moeten samen worden opgesteld, gecontroleerd en bekendgemaakt — maar verschillen in vorm en inhoud.",
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_toepassingsgebied",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "valkuilen": [
    {
      "text": "De vrijstelling van de verplichting om een geconsolideerde jaarrekening op te stellen (groep van beperkte omvang of subconsolidatie) omvat ook de vrijstelling van het geconsolideerd jaarverslag. Beide vallen samen.",
      "confidence": "inferred-from-aggregation",
      "source": {
        "type": "advies",
        "short": "CBN 2022/11"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_toepassingsgebied",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ]
}
```

---

## Record: `geconsolideerde-jaarrekening`

**Gaps te verwerken** (1 stuks):

```json
[
  {
    "record_id": "geconsolideerde-jaarrekening",
    "aspect": "drempelwaarden.ontbreekt",
    "reden": "Examenvragen 2013-1 vr7 en 2014-1 vr7 vragen expliciet de maximale afwijking qua afsluitingsdatum (KB WVV art. 3:109 tweede lid: 3 maanden). De bouwsteen 'Afsluitingsdatum' vermeldt enkel 'mits motivering in de toelichting' zonder de kwantitatieve drempel — vraag is daarmee onbeantwoordbaar uit het record.",
    "prio": "hoog",
    "geconstateerd_door": "verify-run-20260515T141017Z",
    "geconstateerd_op": "2026-05-15T14:30:00+00:00",
    "status": "open"
  }
]
```

**Bron-bundle**: `data/extractie/1.4/enrich-runs/bundle-geconsolideerde-jaarrekening-enrich-run-20260515T141848Z.json` — 275 chunks beschikbaar (bronnen: advies, norm, wettekst)

**Bestaand record** (`data/concept_records/geconsolideerde-jaarrekening.json`):

```json
{
  "id": "geconsolideerde-jaarrekening",
  "naam": "Geconsolideerde jaarrekening",
  "node_type": "begrip",
  "schema_version": "1.2",
  "status": "seed",
  "linked_anchors": [
    "1.4.I.F",
    "1.4.I.C",
    "1.4.II",
    "1.4.II.A",
    "1.4.II.C",
    "1.4.taak.1"
  ],
  "_provenance": {
    "extractor_run": "concept-extractie-v3-2026-05-15T13:36Z",
    "model": "claude-opus-4-7",
    "anchor_id": "1.4.I.F",
    "dekt_ook_anchors": [
      "1.4.I.C",
      "1.4.II",
      "1.4.II.A",
      "1.4.II.C",
      "1.4.taak.1"
    ],
    "reviewed_by": null
  },
  "definitie": {
    "text": "De jaarrekening die het vermogen, de financiële positie en het resultaat van het geconsolideerde geheel (consoliderende vennootschap + dochterondernemingen in de consolidatiekring) opneemt alsof het om één enkele vennootschap ging. Bestaat uit balans, resultatenrekening en toelichting; deze stukken vormen één geheel. Wordt opgesteld op dezelfde datum als de jaarrekening van de consoliderende vennootschap (KB WVV art. 3:109) en in euro uitgedrukt (KB WVV art. 3:103 jo. WVV art. 3:30, § 2). Geconsolideerde balans en resultatenrekening moeten voortvloeien uit een samenhangend en controleerbaar boekhoudsysteem dat de continuïteit van het ene op het andere jaar verzekert.",
    "confidence": "grounded",
    "source": {
      "type": "kb",
      "short": "KB WVV art. 3:103 jo. art. 3:107 jo. art. 3:123"
    },
    "references": [
      {
        "type": "kb",
        "short": "KB WVV art. 3:103 (samenstelling)"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:104 (toepasselijke standaard — BEGAAP of IFRS)"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:105 (getrouw beeld)"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:107 (vormvereisten + belangen van derden afzonderlijk)"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:108 (boekhoudkundige continuïteit)"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:109 (afsluitingsdatum)"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:123 (één economische entiteit)"
      },
      {
        "type": "richtlijn",
        "short": "Richtlijn 2013/34/EU art. 21"
      },
      {
        "type": "wet",
        "short": "WIB92 art. 321/1, 13° (fiscaal-technische definitie)"
      }
    ],
    "_provenance": {
      "inputs": [
        {
          "id": "KB-WVV-2019__art_3_81",
          "sha256": null,
          "version": "rag-v1"
        },
        {
          "id": "KB-WVV-2019__art_3_82",
          "sha256": null,
          "version": "rag-v1"
        },
        {
          "id": "KB-WVV-2019__art_3_83",
          "sha256": null,
          "version": "rag-v1"
        },
        {
          "id": "KB-WVV-2019__art_3_84",
          "sha256": null,
          "version": "rag-v1"
        },
        {
          "id": "KB-WVV-2019__art_3_97",
          "sha256": null,
          "version": "rag-v1"
        },
        {
          "id": "WIB92__art_321/1__sub_13deg",
          "sha256": null,
          "version": "rag-v1"
        }
      ]
    }
  },
  "bouwstenen": [
    {
      "naam": "Beginsel van één economische entiteit (KB WVV art. 3:123)",
      "text": "In de geconsolideerde jaarrekening worden het vermogen, de financiële positie en het resultaat van het geconsolideerde geheel opgenomen 'alsof het om één enkele vennootschap ging'. Deze fictie verklaart de eliminatie van intra-groeptransacties en de afzondering van belangen van derden.",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:123"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_97",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "naam": "Vormvereisten (KB WVV art. 3:107)",
      "text": "De geconsolideerde jaarrekening moet duidelijk worden opgesteld en stelselmatig weergeven, op afsluitingsdatum, de aard en het bedrag van de bezittingen/rechten, schulden/verplichtingen en eigen middelen van het geconsolideerde geheel, alsook voor het boekjaar de aard en het bedrag van de opbrengsten en kosten. Belangen van derden worden afzonderlijk vermeld in balans en resultatenrekening. Compensatie tussen tegoeden en schulden, tussen rechten en verplichtingen, en tussen opbrengsten en kosten is verboden behoudens uitzonderingen in dit hoofdstuk.",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:107"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_83",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "naam": "Keuze tussen Belgisch boekhoudrecht en IFRS (KB WVV art. 3:104)",
      "text": "Standaard: opstellen overeenkomstig de bepalingen van titel 2 van het KB WVV (Belgisch consolidatierecht). § 2: het bestuursorgaan kan beslissen om de geconsolideerde jaarrekening op te stellen met toepassing van het geheel van de internationale boekhoudnormen (IFRS zoals aangenomen door de EU op grond van Verordening 1606/2002). Deze beslissing is onherroepbaar; de toelichting vermeldt dat de onderneming over de nodige middelen beschikt en dat zij alle door de Europese Commissie aangenomen IFRS toepast.",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:104"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_82",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "naam": "Afsluitingsdatum (KB WVV art. 3:109)",
      "text": "De geconsolideerde jaarrekening wordt op dezelfde datum afgesloten als de jaarrekening van de consoliderende vennootschap. Andere datum is mogelijk om rekening te houden met de balansdatum van de meeste of belangrijkste in de consolidatie opgenomen ondernemingen — mits motivering in de toelichting (KB WVV art. 3:111).",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:109 jo. art. 3:111"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_85",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "KB-WVV-2019__art_3_87",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "naam": "Volledigheid (KB WVV art. 3:110)",
      "text": "Onverminderd specifieke eliminatie-/derden-bepalingen bevat de geconsolideerde jaarrekening alle actief- en passiefbestanddelen en alle rechten en verplichtingen van de consoliderende vennootschap en van de in de consolidatie opgenomen dochters op de afsluitingsdatum, alsmede alle opbrengsten en kosten.",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:110"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_86",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "in_praktijk": [
    {
      "aspect": "Toewijzing van het resultaat van de moeder",
      "betekenis": "Behalve wanneer KB WVV art. 3:109, tweede lid wordt toegepast, wordt de geconsolideerde balans opgesteld na toewijzing — d.w.z. na bestemming van het niet-geconsolideerde resultaat van de consoliderende vennootschap (KB WVV art. 3:114).",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:114"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_90",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "aspect": "Wijzigingen in de consolidatiekring (KB WVV art. 3:102 jo. art. 3:152)",
      "betekenis": "Indien de samenstelling van het geconsolideerde geheel in de loop van het boekjaar een aanmerkelijke wijziging heeft ondergaan, moet de toelichting inlichtingen bevatten die een zinvolle vergelijking met vorige jaren mogelijk maken. Bij elke post wordt het bedrag van het overeenkomstige post van het vorige boekjaar vermeld (KB WVV art. 3:152).",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:102 jo. art. 3:152"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_80",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "KB-WVV-2019__art_3_122",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "vergelijkingsparen": [
    {
      "vergelijking_met": "geconsolideerd-jaarverslag",
      "verschil": "De geconsolideerde jaarrekening is een gestandaardiseerd cijfermatig stuk (balans, resultatenrekening, toelichting). Het geconsolideerd jaarverslag is een vrij toelichtend stuk dat de evolutie en de toekomstverwachtingen van de groep beschrijft. Beide moeten samen worden opgesteld, gecontroleerd en bekendgemaakt.",
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_toepassingsgebied",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "vergelijking_met": "consolidatieverplichting",
      "verschil": "Consolidatieverplichting is de juridische plicht; de geconsolideerde jaarrekening is het uitvoerend product van die plicht.",
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_82",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "valkuilen": [
    {
      "text": "De keuze voor IFRS (KB WVV art. 3:104, § 2) is onherroepbaar — een onderneming die eenmaal voor IFRS-consolidatie heeft gekozen, kan niet meer terugschakelen naar Belgisch boekhoudrecht.",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:104, § 2"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_82",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "text": "Een vennootschap die niet wettelijk consolidatieplichtig is maar vrijwillig of op grond van bijzondere bepalingen een geconsolideerde jaarrekening publiceert, moet die opstellen volgens hetzelfde wettelijke kader (KB WVV art. 3:112).",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:112"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_88",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "text": "De fiscale definitie in WIB92 art. 321/1, 13° verwijst naar 'multinationale groepen' (Pillar Two context). Verwar deze fiscaaltechnische definitie niet met het algemeen boekhoudrechtelijk begrip van de geconsolideerde jaarrekening (KB WVV).",
      "confidence": "grounded",
      "source": {
        "type": "wet",
        "short": "WIB92 art. 321/1, 13°"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "WIB92__art_321/1__sub_13deg",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ]
}
```

---

## Record: `groep-van-beperkte-omvang`

**Gaps te verwerken** (1 stuks):

```json
[
  {
    "record_id": "groep-van-beperkte-omvang",
    "aspect": "records.overlappend-fenomeen",
    "reden": "Het record 'groep-van-beperkte-omvang' (begrip) en het record 'groottecriteria-consolidatie' (drempel) delen dezelfde primaire bron (WVV art. 1:26, § 1) en beschrijven beide de vrijstellingsdrempels en de twee berekeningsmethoden (geconsolideerde versus geaggregeerde basis +20 %). De definitiekern en de in_praktijk-content overlappen meer dan 60 %.",
    "prio": "midden",
    "geconstateerd_door": "verify-run-20260515T141017Z",
    "geconstateerd_op": "2026-05-15T14:30:00+00:00",
    "status": "open"
  }
]
```

**Bron-bundle**: `data/extractie/1.4/enrich-runs/bundle-groep-van-beperkte-omvang-enrich-run-20260515T141848Z.json` — 267 chunks beschikbaar (bronnen: advies, wettekst)

**Bestaand record** (`data/concept_records/groep-van-beperkte-omvang.json`):

```json
{
  "id": "groep-van-beperkte-omvang",
  "naam": "Groep van beperkte omvang",
  "node_type": "begrip",
  "schema_version": "1.2",
  "status": "seed",
  "linked_anchors": [
    "1.4.I.C",
    "1.4.I.B",
    "1.4.II.B"
  ],
  "_provenance": {
    "extractor_run": "concept-extractie-v3-2026-05-15T13:36Z",
    "model": "claude-opus-4-7",
    "anchor_id": "1.4.I.C",
    "dekt_ook_anchors": [
      "1.4.I.B",
      "1.4.II.B"
    ],
    "reviewed_by": null
  },
  "definitie": {
    "text": "Een groep die op geconsolideerde of geaggregeerde basis niet meer dan één van de criteria van WVV art. 1:26, § 1 overschrijdt (jaaromzet, balanstotaal, jaargemiddelde aantal werknemers). Een vennootschap die deel uitmaakt van een groep van beperkte omvang is in beginsel vrijgesteld van de verplichting om een geconsolideerde jaarrekening en een jaarverslag over de geconsolideerde jaarrekening op te stellen.",
    "confidence": "grounded",
    "source": {
      "type": "wet",
      "short": "WVV art. 1:26, § 1"
    },
    "references": [
      {
        "type": "wet",
        "short": "WVV art. 1:24 (kleine vennootschap)"
      },
      {
        "type": "wet",
        "short": "WVV art. 1:26 (groep van beperkte omvang)"
      },
      {
        "type": "advies",
        "short": "CBN 2022/03 — Beoordeling groottecriteria"
      },
      {
        "type": "advies",
        "short": "CBN 2022/11 — Vermogensmutatiemethode"
      }
    ],
    "_provenance": {
      "inputs": [
        {
          "id": "CBN-2022-11-vermogensmutatiemethode__sec_toepassingsgebied",
          "sha256": null,
          "version": "rag-v1"
        },
        {
          "id": "CBN-2022-09-consolidatie-bij-de-horizontale-groep-consortium-0__sec_beoordeling-groottecriteria-ingeval-van-een-consortium",
          "sha256": null,
          "version": "rag-v1"
        }
      ]
    }
  },
  "in_praktijk": [
    {
      "aspect": "Twee berekeningsmethoden",
      "betekenis": "Methode 1: geconsolideerde basis (KB WVV-consolidatieregels toepassen) — vereist een effectieve consolidatie-oefening. Methode 2: geaggregeerde basis (alle bedragen van verbonden vennootschappen optellen, met drempels +20 %) — vereenvoudigde methode (WVV art. 1:24, § 6). Het personeelsaantal wordt steeds als jaargemiddelde per vennootschap berekend.",
      "confidence": "grounded",
      "source": {
        "type": "advies",
        "short": "CBN 2022/03"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-03-beoordeling-van-de-groottecriteria-overeenkomstig-artikelen-124-en-125-van-het-wetboek-van__sec_vereenvoudigde-methode-berekening-van-het-balanstotaal-en-de",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "CBN-2022-03-beoordeling-van-de-groottecriteria-overeenkomstig-artikelen-124-en-125-van-het-wetboek-van__sec_berekeningsmethoden",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "aspect": "Consortium-context",
      "betekenis": "Bij een consortium wordt de groottebepaling op het niveau van de leden samen uitgevoerd. De centrale leider die geen vennootschap is (bv. natuurlijke persoon, private stichting) wordt niet meegeteld.",
      "confidence": "grounded",
      "source": {
        "type": "advies",
        "short": "CBN 2022/09"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-09-consolidatie-bij-de-horizontale-groep-consortium-0__sec_beoordeling-groottecriteria-ingeval-van-een-consortium",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "vergelijkingsparen": [
    {
      "vergelijking_met": "groottecriteria-consolidatie",
      "verschil": "De 'groep van beperkte omvang' is de kwalificatie (het juridisch statuut van vrijstelling); 'groottecriteria-consolidatie' verwijst naar de toets-set (omzet, balanstotaal, personeel) waaraan die kwalificatie wordt afgemeten.",
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_toepassingsgebied",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "vergelijking_met": "consolidatieverplichting",
      "verschil": "De consolidatieverplichting is de regel; de kwalificatie als 'groep van beperkte omvang' triggert de uitzondering (vrijstelling). De vrijstelling betreft zowel de jaarrekening als het jaarverslag.",
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_toepassingsgebied",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "valkuilen": [
    {
      "text": "Vrijstelling op grond van beperkte omvang werkt enkel als 'maximaal één criterium overschreden' — niet 'minder dan twee'. Het criterium-aantal moet strikt worden geteld, en alle drie de criteria moeten worden beoordeeld (omzet, balanstotaal, personeel).",
      "confidence": "grounded",
      "source": {
        "type": "wet",
        "short": "WVV art. 1:26, § 1 (toepassing analoog aan art. 1:24)"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2017-15-transacties-onder-gemeenschappelijke-leiding-common-control-transactions-update__sec_verband-met-de-berekening-van-de-groottecriteria-bij-transac",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "text": "De vrijstelling vervalt niet zomaar wanneer de drempels eenmalig worden overschreden — er gelden specifieke regels over duurzaamheid van overschrijdingen (zie CBN 2024/07 voor de actualisering van drempels en de impact-overgangsregels). Bij twijfel: raadpleeg het Cijferzakboekje voor de actuele drempels.",
      "confidence": "inferred",
      "source": {
        "type": "advies",
        "short": "CBN 2024/07"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2024-07-gevolgen-verhoging-groottecriteria-voor-vennootschappen__sec_voorbeeld-5-beoordeling-op-geconsolideerde-of-geaggregeerde-_part2",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ]
}
```

---

## Record: `vermogensmutatiemethode`

**Gaps te verwerken** (1 stuks):

```json
[
  {
    "record_id": "vermogensmutatiemethode",
    "aspect": "vergelijkingsparen.vrije-tekst-niet-gespiegeld",
    "reden": "De definitie noemt 'invloed van betekenis' als toepassingscriterium en 'consolidatieverschil' wordt expliciet uitgewerkt (CBN 2022/11), maar 'invloed-van-betekenis' en 'consolidatieverschil' staan niet als vergelijkingsparen op vermogensmutatiemethode — terwijl ze in de bestaande vergelijkingsparen van die andere records wél naar vermogensmutatie wijzen (asymmetrisch).",
    "prio": "midden",
    "geconstateerd_door": "verify-run-20260515T141017Z",
    "geconstateerd_op": "2026-05-15T14:30:00+00:00",
    "status": "open"
  }
]
```

**Bron-bundle**: `data/extractie/1.4/enrich-runs/bundle-vermogensmutatiemethode-enrich-run-20260515T141848Z.json` — 278 chunks beschikbaar (bronnen: advies, norm, wettekst)

**Bestaand record** (`data/concept_records/vermogensmutatiemethode.json`):

```json
{
  "id": "vermogensmutatiemethode",
  "naam": "Vermogensmutatiemethode (equity method)",
  "node_type": "methode",
  "schema_version": "1.2",
  "status": "seed",
  "linked_anchors": [
    "1.4.I.E",
    "1.4.I.D",
    "1.4.I.G",
    "1.4.II.C",
    "1.4.taak.1"
  ],
  "_provenance": {
    "extractor_run": "concept-extractie-v3-2026-05-15T13:36Z",
    "model": "claude-opus-4-7",
    "anchor_id": "1.4.I.E",
    "dekt_ook_anchors": [
      "1.4.I.D",
      "1.4.I.G",
      "1.4.II.C",
      "1.4.taak.1"
    ],
    "reviewed_by": null
  },
  "doel": {
    "text": "Een deelneming wordt in de geconsolideerde jaarrekening niet activum-per-activum opgenomen, maar als één gesynthetiseerde balanspost — initieel gewaardeerd aan het pro-rata aandeel in het eigen vermogen van de betrokken onderneming op verwervingsdatum, en vervolgens jaarlijks aangepast voor het pro-rata aandeel in de wijzigingen in dat eigen vermogen (resultaat en directe mutaties). De methode wordt toegepast op (a) geassocieerde ondernemingen (invloed van betekenis, geen controle), (b) gemeenschappelijke dochterondernemingen waarvan het bedrijf niet nauw geïntegreerd is in dat van de moeder, en (c) dochterondernemingen buiten de consolidatie gelaten op grond van KB WVV art. 3:98 of 3:99.",
    "confidence": "grounded",
    "source": {
      "type": "kb",
      "short": "KB WVV art. 3:142 jo. art. 3:141 — 3:145"
    },
    "references": [
      {
        "type": "kb",
        "short": "KB WVV art. 3:100 (uitgesloten dochters)"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:141 (balansvoorstelling)"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:142, § 1 — 2 (eerste consolidatie)"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:143 (latere consolidaties)"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:145 (aandeel in resultaat)"
      },
      {
        "type": "advies",
        "short": "CBN 2022/11 — Vermogensmutatiemethode"
      },
      {
        "type": "advies",
        "short": "CBN 2014/3 — Mutaties binnen eigen vermogen geassocieerde"
      }
    ],
    "_provenance": {
      "inputs": [
        {
          "id": "CBN-2022-11-vermogensmutatiemethode__sec_toepassingsgebied",
          "sha256": null,
          "version": "rag-v1"
        },
        {
          "id": "CBN-2022-11-vermogensmutatiemethode__sec_eerste-consolidatie",
          "sha256": null,
          "version": "rag-v1"
        },
        {
          "id": "KB-WVV-2019__art_3_113",
          "sha256": null,
          "version": "rag-v1"
        },
        {
          "id": "KB-WVV-2019__art_3_115",
          "sha256": null,
          "version": "rag-v1"
        }
      ]
    }
  },
  "voorwaarden_toepassing": [
    {
      "text": "Geassocieerde onderneming: deelneming met invloed van betekenis maar zonder controle (WVV art. 1:22; weerlegbaar vermoeden vanaf 20 % stemrechten).",
      "confidence": "grounded",
      "source": {
        "type": "wet",
        "short": "WVV art. 1:22"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_inleiding",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "text": "Gemeenschappelijke dochteronderneming waarvan het bedrijf niet nauw geïntegreerd is in dat van de moeder.",
      "confidence": "grounded",
      "source": {
        "type": "advies",
        "short": "CBN 2013/3"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_praktische-uitwerking",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "text": "Dochteronderneming waarover de consoliderende vennootschap controle in feite bezit maar waarvan opname zou indruisen tegen het getrouwe beeld (KB WVV art. 3:98); of dochters waarvan de going-concern-veronderstelling niet meer kan worden gehandhaafd (KB WVV art. 3:99).",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:100"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_78",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "KB-WVV-2019__art_3_77",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "bouwstenen": [
    {
      "naam": "Eerste consolidatie — herwaardering naar pro-rata aandeel in eigen vermogen",
      "text": "De historische aanschaffingswaarde van de deelneming wordt vervangen door het bedrag dat overeenkomt met het deel van het eigen vermogen van de betrokken vennootschap (inclusief het resultaat over het boekjaar) dat deze deelneming vertegenwoordigt. Een eventueel verschil wordt eerst toegerekend aan onder-/overgewaardeerde activa van de betrokken vennootschap; het overblijvende deel verschijnt als 'Consolidatieverschillen' (positief of negatief) en wordt jaarlijks afgeschreven.",
      "confidence": "grounded",
      "source": {
        "type": "advies",
        "short": "CBN 2022/11 — Eerste consolidatie"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_eerste-consolidatie",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_voorbeeld",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "naam": "Latere consolidaties — pro-rata aandeel in resultaat en directe mutaties",
      "text": "De waarde van de deelneming wordt jaar na jaar verhoogd of verminderd met het pro-rata aandeel in (a) het resultaat van het boekjaar van de betrokken vennootschap, met uitsluiting van het deel dat bij bestemming als dividend wordt toegekend (dat dividend wordt apart geboekt); (b) directe mutaties binnen het eigen vermogen (herwaarderingsmeerwaarde, verkrijging kapitaalsubsidie, overboeking gerealiseerde meerwaarde, omrekeningsverschillen).",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:143"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_113",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_latere-consolidaties",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "CBN-2014-03-de-boekhoudkundige-verwerking-van-mutaties-binnen-het-eigen-vermogen-van-een-geassocieerde__sec_inleiding",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "naam": "Presentatie op de balans (KB WVV art. 3:141)",
      "text": "Deelnemingen waarop vermogensmutatie is toegepast worden in de geconsolideerde balans opgenomen onder een afzonderlijke post van de financiële vaste activa, genoemd 'Vennootschappen waarop vermogensmutatie is toegepast'.",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:141"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_112",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "naam": "Presentatie op de resultatenrekening (KB WVV art. 3:145)",
      "text": "Het aandeel in het resultaat van de betrokken vennootschap wordt onder een afzonderlijke post 'Aandeel in het resultaat van de vennootschappen waarop vermogensmutatie is toegepast' in de geconsolideerde resultatenrekening opgenomen.",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:145"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_115",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "berekeningsmethode": [
    {
      "naam": "Eerste consolidatie — herwaardering en consolidatieverschil",
      "formule": "Boekwaarde deelneming (eerste consolidatie) = pro-rata aandeel × eigen vermogen op verwervingsdatum + consolidatieverschil (positief of negatief)",
      "ratio": "Bij verwerving betaalt de moeder vaak een prijs verschillend van het pro-rata aandeel in het netto-actief van de geassocieerde. Het verschil wordt eerst toegewezen aan onder-/overgewaardeerde activa van de dochter en daarna geboekt als 'Consolidatieverschil'.",
      "stappen": [
        {
          "volgorde": 1,
          "text": "Bepaal de aanschaffingswaarde van de deelneming."
        },
        {
          "volgorde": 2,
          "text": "Bepaal het pro-rata aandeel in het eigen vermogen van de betrokken vennootschap op acquisitiedatum."
        },
        {
          "volgorde": 3,
          "text": "Bereken het verschil (aanschaffingswaarde − pro-rata EV)."
        },
        {
          "volgorde": 4,
          "text": "Wijs het verschil zoveel mogelijk toe aan onder-/overgewaardeerde activa of passiva van de dochter."
        },
        {
          "volgorde": 5,
          "text": "Het overblijvende verschil wordt geboekt als positief of negatief consolidatieverschil; positief consolidatieverschil wordt afgeschreven over de vermoedelijke gebruiksduur (KB WVV art. 3:131)."
        }
      ],
      "concreet_voorbeeld": {
        "scenario": "Onderneming ABC verwerft in 20X1 een belang van 20 % in onderneming DEF. Aanschaffingswaarde 200. Netto-activa DEF op acquisitiedatum: 600.",
        "berekening": "Pro-rata aandeel in EV op acquisitiedatum = 20 % × 600 = 120.\nVerschil = 200 − 120 = 80 (positief).\nGeen onder-/overwaarderingen aangewezen → het volledige verschil van 80 wordt geboekt als positief consolidatieverschil.\nBoeking: 'Vennootschappen waarop vermogensmutatie is toegepast' (balans) +120; 'Positieve consolidatieverschillen' (balans) +80; tegenpost: 'Deelnemingen' −200.",
        "resultaat": "Eerste consolidatie: deelneming wordt voorgesteld als 'Vennootschappen waarop vermogensmutatie is toegepast' voor 120 + 'Positief consolidatieverschil' 80 — som 200 (idem als aanschaffingswaarde). Positief consolidatieverschil wordt afgeschreven over bv. 5 jaar = 16/jaar in de geconsolideerde resultatenrekening (financiële kosten of bedrijfskosten, afzonderlijke post)."
      },
      "source": {
        "type": "advies",
        "short": "CBN 2013/3 — voorbeeld 1; KB WVV art. 3:131, 3:142"
      },
      "confidence": "grounded",
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_voorbeeld-1",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_voorbeeld",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "naam": "Latere consolidatie — pro-rata aandeel in winst of verlies",
      "formule": "Δ boekwaarde deelneming = belang% × Δ eigen vermogen betrokken vennootschap (resultaat van het boekjaar, excl. dividenduitkering, plus directe EV-mutaties)",
      "ratio": "Het pro-rata aandeel in winst of verlies vertaalt zich rechtstreeks in de waarde van de deelneming op de geconsolideerde balans, met als spiegelpost een afzonderlijke resultatenpost 'Aandeel in het resultaat van vennootschappen waarop vermogensmutatie is toegepast'.",
      "stappen": [
        {
          "volgorde": 1,
          "text": "Identificeer het resultaat van de betrokken vennootschap voor het boekjaar."
        },
        {
          "volgorde": 2,
          "text": "Bereken het pro-rata aandeel: belang% × resultaat."
        },
        {
          "volgorde": 3,
          "text": "Verhoog (winst) of verlaag (verlies) de balanspost 'Vennootschappen waarop vermogensmutatie is toegepast' met dit aandeel."
        },
        {
          "volgorde": 4,
          "text": "Boek de tegenpost in de geconsolideerde resultatenrekening als 'Aandeel in het resultaat van vennootschappen waarop vermogensmutatie is toegepast' (KB WVV art. 3:145)."
        },
        {
          "volgorde": 5,
          "text": "Indien dividend wordt uitgekeerd: het dividend wordt apart geboekt als opbrengst, maar het deel van het resultaat dat als dividend wordt toegekend, wordt niet (opnieuw) bij de boekwaarde van de deelneming geteld."
        }
      ],
      "concreet_voorbeeld": {
        "scenario": "Geassocieerde vennootschap Y; belang van moedervennootschap M = 20 %. Hypothese 1: Y maakt in 20X2 een winst van 1.500. Hypothese 2: Y maakt in 20X2 een verlies van 1.500. Hypothese 3: Y maakt in 20X2 een verlies van 15.000 (boekwaarde van de deelneming bij eerste consolidatie was 2.600).",
        "berekening": "Hypothese 1: 20 % × 1.500 = +300 — verhoging boekwaarde deelneming + opname als 'Aandeel in de winst van vennootschappen waarop vermogensmutatie is toegepast'.\nHypothese 2: 20 % × (−1.500) = −300 — verlaging boekwaarde + 'Aandeel in het verlies …' van 300.\nHypothese 3: 20 % × (−15.000) = −3.000 — maar de boekwaarde bedraagt slechts 2.600 en kan niet onder 0 zakken. Verlies wordt slechts ten belope van 2.600 opgenomen; resterende 400 wordt niet doorgeboekt zolang geen aanvullende verplichting (CBN 2022/11).",
        "resultaat": "Hypothese 1: deelneming op balans stijgt met 300 tot bv. 2.900; resultaat verbetert met 300. Hypothese 2: deelneming daalt met 300; verlies in geconsolideerde resultatenrekening 300. Hypothese 3: deelneming wordt afgeboekt tot nul; aandeel in het verlies bedraagt 2.600 (niet 3.000)."
      },
      "source": {
        "type": "advies",
        "short": "CBN 2022/11 — Herberekening (hypotheses 1-3); KB WVV art. 3:143, 3:145"
      },
      "confidence": "grounded",
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_herberekening-van-het-bedrag-van-de-deelneming-waarop-de-ver",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_herberekening-van-het-bedrag-van-de-deelneming-waarop-de-ver_2",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_herberekening-van-het-bedrag-van-de-deelneming-waarop-de-ver_3",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "in_praktijk": [
    {
      "aspect": "Eliminatie van intra-groepswinsten",
      "betekenis": "De resultaten van verrichtingen tussen de consoliderende vennootschap (of haar dochters) en de vennootschap waarop vermogensmutatie wordt toegepast, die in de waardering van een actief zijn begrepen, worden uit het 'Aandeel in het resultaat van vennootschappen waarop vermogensmutatie is toegepast' geweerd voor het pro-rata aandeel. Geldt voor zowel upstream als downstream sales.",
      "confidence": "grounded",
      "source": {
        "type": "advies",
        "short": "CBN 2022/11 — Intra-groepsverkopen"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_intra-groepsverkopen-upstream-downstream-sales",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "aspect": "Geen vrijstelling van subconsolidatie",
      "betekenis": "Het opnemen van een vennootschap via de vermogensmutatiemethode (in plaats van integraal/evenredig) geeft de groep geen vrijstelling van haar consolidatieplicht. De moedervennootschap blijft consolidatieplichtig zolang ze een dochter heeft.",
      "confidence": "grounded",
      "source": {
        "type": "advies",
        "short": "CBN 2022/11 — Toepassing"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_toepassing-van-de-vermogensmutatiemethode",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "aspect": "Verkoop van de deelneming",
      "betekenis": "Bij verkoop wordt het verschil tussen de verkoopprijs en de boekwaarde (op vermogensmutatiebasis, inclusief mutaties tot verkoopdatum) als meer- of minderwaarde in de geconsolideerde resultatenrekening geboekt; het overblijvende positieve consolidatieverschil moet ook worden afgeboekt.",
      "confidence": "grounded",
      "source": {
        "type": "advies",
        "short": "CBN 2022/11 — Voorbeeld 2 verkoop deelneming"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_voorbeeld-2-verkoop-van-de-deelnemingen-waarop-vermogensmuta",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "vergelijkingsparen": [
    {
      "vergelijking_met": "integrale-consolidatie",
      "verschil": "Vermogensmutatie behoudt de deelneming als één balanspost; integrale consolidatie neemt de activa/passiva regel voor regel op. Integraal → controle; vermogensmutatie → invloed van betekenis (of uitgesloten dochters).",
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_praktische-uitwerking",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "vergelijking_met": "evenredige-consolidatie",
      "verschil": "Evenredig = activa/passiva pro-rata opgenomen. Vermogensmutatie = één balanspost, geherwaardeerd naar pro-rata EV. Evenredig is de regel voor gemeenschappelijke dochters; vermogensmutatie kan voor niet-geïntegreerde gemeenschappelijke dochters of voor geassocieerden.",
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_praktische-uitwerking",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "vergelijking_met": "geassocieerde-onderneming",
      "verschil": "De vermogensmutatiemethode is de boekhoudkundige techniek; de geassocieerde onderneming is een typisch toepassingsobject. Niet alle vermogensmutatie-deelnemingen zijn echter geassocieerden — ook uitgesloten dochters (KB WVV art. 3:100) en bepaalde gemeenschappelijke dochters worden zo verwerkt.",
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_78",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "valkuilen": [
    {
      "text": "Het pro-rata aandeel in een verlies kan de boekwaarde van de deelneming nooit onder nul brengen. Verdere verliezen worden niet langer doorgeboekt zolang geen aanvullende verplichting bestaat (CBN 2022/11, hypothese 3).",
      "confidence": "grounded",
      "source": {
        "type": "advies",
        "short": "CBN 2022/11"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_herberekening-van-het-bedrag-van-de-deelneming-waarop-de-ver_3",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "text": "Een dividend dat de geassocieerde uitkeert vermindert het eigen vermogen van de geassocieerde — maar wordt in de jaarrekening van de moeder geboekt als financiële opbrengst (zonder voor een tweede maal als 'aandeel in resultaat' te worden geteld). De vermogensmutatie corrigeert hiervoor: het resultaat-aandeel wordt berekend exclusief het deel dat als dividend wordt toegekend.",
      "confidence": "grounded",
      "source": {
        "type": "advies",
        "short": "CBN 2022/11 — Latere consolidaties"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_latere-consolidaties",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "text": "Wijzigingen in het eigen vermogen van de geassocieerde buiten het resultaat om (herwaarderingsmeerwaarde, kapitaalsubsidie, omrekeningsverschillen) moeten ook in de vermogensmutatie worden meegenomen — niet alleen het resultaat. Dit was vroeger een onderbelicht punt; CBN 2014/3 verduidelijkte het en CBN 2022/11 codificeerde de werkwijze.",
      "confidence": "grounded",
      "source": {
        "type": "advies",
        "short": "CBN 2014/3 + 2022/11"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2014-03-de-boekhoudkundige-verwerking-van-mutaties-binnen-het-eigen-vermogen-van-een-geassocieerde__sec_inleiding",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_directe-mutaties-binnen-het-eigen-vermogen-van-de-geassociee",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ]
}
```

---


---

## Prompt-referentie (concept-enrich-v1.md)

# Prompt: Concept-record verrijking — Blok 3 ENRICH (v1)

**Doel**: Verrijk concept-records op basis van open gaps uit `data/extractie/gaps.json`. Schrijft terug naar `data/concept_records/<id>.json`. Strikt append-only contract.

**Model**: claude-opus-4-7 (subagent — ADR-008 §2, §13.3; geen externe API).

**Rol**: Je bent een schrijvende agent (writer), geen beoordelende agent. Je werkt op één record tegelijk. Je werkt alleen gaps weg die in de meegeleverde gap-entries staan. Je beoordeelt geen andere records.

---

## HARD CONTRACT — VERPLICHT

Deze regels zijn niet onderhandelbaar. Bij twijfel: kies de meest conservatieve interpretatie.

### 1 — Behoud alles

Behoud álle bestaande velden, veld-waarden en array-items in het record tenzij je een correctie uitvoert met motivering (zie regel 2). Toevoegen is altijd toegestaan. Weglaten is verboden zonder motivering.

### 2 — Corrigeren mag, maar met bewijs

Als een bestaand veld inhoudelijk onjuist is (aantoonbaar op basis van de bron-bundle), mag je corrigeren. Verplicht:
- Voeg `corrected_from` toe met de **volledige oude waarde** (kopie van het oorspronkelijke veld).
- Voeg `correction_reason` toe met een zin die de fout en de bron beschrijft.
- Voeg `correction_source` toe: de chunk-id of bron die de correctie onderbouwt.

Voorbeeld:
```json
"main_rule": {
  "text": "<nieuwe, correcte tekst>",
  "corrected_from": "<letterlijk de oude tekst>",
  "correction_reason": "WVV art. 1:22 §2 stelt 20 % i.p.v. 25 % als grens voor het vermoeden.",
  "correction_source": "WVV-2019__art_1_22",
  "confidence": "grounded",
  "source": { "type": "wet", "short": "WVV art. 1:22 §2" },
  "_provenance": { "inputs": [{"id": "WVV-2019__art_1_22", "sha256": null, "version": "rag-v1"}] }
}
```

### 3 — Verwijderen verboden

Je verwijdert geen velden en geen array-items. Zelfs als je een item inhoudelijk zwak vindt — behoud. Bij twijfel: behoud.

### 4 — Alleen gevraagde gaps

Je voegt uitsluitend inhoud toe die gevraagd wordt door de meegeleverde gap-entries voor dit record. Je voegt geen velden toe die niet gevraagd zijn, ook al zou je ze nuttig vinden. De beoordeling van wat nodig is, is al gedaan door de VERIFY-agent.

---

## Context

Je krijgt per record:

1. **`record`**: het volledige bestaande record (JSON, schema 1.2), geladen uit `data/concept_records/<id>.json`.
2. **`gap_entries`**: de gefilterde entries uit `data/extractie/gaps.json` voor dit record, met `status: "open"`.
3. **`bron_bundle`**: de bron-chunks die beschikbaar zijn voor de anchors in `linked_anchors[]` van dit record, geladen via `export_bundle.py`.

---

## Werkwijze per record

### Stap 1 — Lees het record en de gaps

Lees het bestaande record volledig. Noteer alle bestaande velden en hun inhoud. Lees de gap-entries: wat ontbreekt precies, wat is het aspect, wat is de reden?

### Stap 2 — Haal relevante chunks op

Scan de `bron_bundle` op chunks die de gap-aspecten direct adresseren. Gebruik alleen chunks die het gevraagde aspect direct behandelen (thematische relevantie — zie v3-prompt Anti-hallucinatie-regel 2).

### Stap 3 — Verwerk elke gap

Voor elke gap-entry:

| Aspect | Wat je toevoegt |
|---|---|
| `berekeningsmethode.concreet_voorbeeld` | Voeg `concreet_voorbeeld`-block toe aan de bestaande `berekeningsmethode[].naam` die het betreft. Als de methode-naam niet exact matcht: voeg toe aan de meest relevante methode. |
| `berekeningsmethode.formule` | Voeg `formule`-veld toe aan de juiste methode. Als er geen `berekeningsmethode[]` is: maak het veld aan met naam + formule + stappen (minimaal 2). |
| `definitie.onvolledig` | Breid `definitie.text` uit — voeg `corrected_from` toe met de oude tekst als je de tekst significant wijzigt. |
| `drempelwaarden.ontbreekt` | Voeg `drempelwaarden[]`-array toe (of items aan bestaande array) met naam, waarde, eenheid, gevolg, source, confidence, provenance. |
| `in_praktijk.ontbreekt` | Voeg `in_praktijk[]`-array toe (of items aan bestaande array) met aspect, betekenis, optioneel herkenningspunt. |
| `vergelijkingsparen.ontbreekt` | Voeg `vergelijkingsparen[]`-items toe voor de gevonden vergelijkingen. |
| `vergelijkingsparen.vrije-tekst-niet-gespiegeld` | Voeg structurele link toe als `vergelijkingsparen[]`-item (voor het concept dat in vrije tekst werd vermeld). |
| `valkuilen.ontbreekt` | Voeg `valkuilen[]`-items toe voor impliciete vereisten, red-herrings, veelgemaakte fouten. |
| `uitzonderingen.ontbreekt` | Voeg `uitzonderingen[]`-items toe met wetsbron. |
| `stappen.onvolledig` | Voeg stappen toe of breid bestaande stappen uit. Behoud volgorde-nummering. |
| `records.ontbreekt` | Log in output-rapport: dit is een taak voor EXTRACT (fase C), niet voor ENRICH. Maak geen nieuw record aan. |

### Stap 4 — Schrijf het bijgewerkte record

Schrijf het volledige bijgewerkte record terug naar `data/concept_records/<id>.json`. Behoud de volledige structuur en opmaak van het origineel zoveel mogelijk.

Update het top-level `_provenance`-block:
```json
"_provenance": {
  "extractor_run": "<originele waarde>",
  "model": "<originele waarde>",
  "anchor_id": "<originele waarde>",
  "dekt_ook_anchors": ["<originele waarde>"],
  "reviewed_by": null,
  "enrich_runs": [
    {
      "run_id": "enrich-run-<id>",
      "model": "claude-opus-4-7",
      "gaps_verwerkt": ["<aspect-1>", "<aspect-2>"],
      "uitgevoerd_op": "<ISO-8601-UTC>"
    }
  ]
}
```

Als `enrich_runs` al bestaat: voeg het nieuwe object toe aan de array (behoud eerder objects).

---

## Anti-hallucinatie-regels

1. Geen nieuwe claims zonder `_provenance.inputs` met thematisch relevante chunk-id's.
2. Geen wetsartikelnummers die niet letterlijk in de bundle staan.
3. `confidence: "grounded"` alleen als de claim direct traceerbaar is naar één chunk.
4. `confidence: "inferred-from-aggregation"` als je over 2+ chunks van 2+ bronnen synthetiseert.
5. Alle chunk-id's in `_provenance.inputs` moeten het concept direct behandelen.

---

## Afsluitend rapport

Na verwerking van alle records, schrijf een beknopt rapport naar stdout:

```
ENRICH-run <id> — samenvatting
================================
Records verwerkt : <n>
Gaps verwerkt    : <n> (<n> hoog / <n> midden / <n> laag)
Correcties aangebracht: <n> (verplicht corrected_from aanwezig)
Records-ontbreekt gaps overgeslagen (taak voor EXTRACT): <n>

Per record:
  <record_id>: <gaps-aspecten verwerkt, kommagescheiden>
  ...
```

---

## Beperkingen

- **Geen nieuwe records aanmaken.** Alleen bestaande records aanvullen.
- **Geen niet-gevraagde velden toevoegen.**
- **Geen gaps-status updaten.** `enrich_records.py` markeert gaps als `enriched-pending-verify` na de subagent-run.
- **Werk in het Nederlands.**

