# ENRICH-run enrich-run-20260515T144255Z — Instructies voor Opus-subagent

**Programmaonderdeel**: 1.4
**Run-id**: enrich-run-20260515T144255Z
**Gegenereerd op**: 2026-05-15T14:42:55+00:00
**Records te verwerken**: 2
**Gaps te verwerken**: 2

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

**Gaps te verwerken** (1 stuks):

```json
[
  {
    "record_id": "consolidatieverschil",
    "aspect": "oorzaken.dedup",
    "reden": "v3 heeft 5 oorzaken waarvan 2 overlappen (overpaid goodwill ≈ niet-geactiveerde immateriële waarden). Examen vraagt klassiek 4 oorzaken. Consolideer overlappende items, behoud beide perspectieven met corrected_from.",
    "prio": "hoog",
    "geconstateerd_door": "v3-vs-v2-rapport-2026-05-15",
    "geconstateerd_op": "2026-05-15T14:42:33.914454+00:00",
    "status": "open"
  }
]
```

**Bron-bundle**: `data/extractie/1.4/enrich-runs/bundle-consolidatieverschil-enrich-run-20260515T144255Z.json` — 458 chunks beschikbaar (bronnen: advies, norm, wettekst)

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
    "reviewed_by": null,
    "enrich_runs": [
      {
        "run_id": "enrich-run-20260515T141848Z",
        "model": "claude-opus-4-7",
        "gaps_verwerkt": [
          "definitie.onvolledig",
          "vergelijkingsparen.vrije-tekst-niet-gespiegeld"
        ],
        "uitgevoerd_op": "2026-05-15T15:00:00+00:00"
      }
    ]
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
    },
    {
      "text": "Passiefbestanddelen van de dochter zijn boekhoudkundig overgewaardeerd (bv. te hoge voorzieningen, te ruim ingeschatte schulden). KB WVV art. 3:130, eerste lid bepaalt dat het verschil uit de compensatie zoveel mogelijk wordt toegerekend aan 'de actief- en passiefbestanddelen waarvan de waarde hoger of lager is dan hun boekwaarde in de boekhouding van de dochteronderneming'. Een te hoge waardering aan passiefzijde kan zo (mee) verklaren waarom de moeder bereid is een hogere prijs te betalen dan de boekwaarde van het netto-actief — het toegewezen deel verlaagt het residu dat als consolidatieverschil overblijft.",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:130, eerste lid"
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
      "text": "Niet-geactiveerde immateriële waarden in de dochter — synergieverwachtingen, marktpositie, klantenbestand, merken, knowhow en andere economische waarden die naar boekhoudregels niet in de enkelvoudige jaarrekening van de dochter konden worden geactiveerd. Deze waarden zijn niet toewijsbaar aan specifieke actief- of passiefposten (KB WVV art. 3:130, eerste lid) en blijven daarom in het residu zitten: het positieve consolidatieverschil dat aan actiefzijde wordt opgenomen en over de vermoedelijke gebruiksduur wordt afgeschreven (KB WVV art. 3:131, § 1). De Europese Richtlijn 2013/34/EU art. 24, lid 3, c) duidt dit residu uitdrukkelijk als 'goodwill'.",
      "confidence": "inferred-from-aggregation",
      "source": {
        "type": "richtlijn",
        "short": "Richtlijn 2013/34/EU art. 24, lid 3, c); KB WVV art. 3:130 jo. art. 3:131"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "Richtlijn-2013-34-EU__art_24__sub_lid1-lid14",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "KB-WVV-2019__art_3_102",
            "sha256": null,
            "version": "rag-v1"
          },
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
    },
    {
      "vergelijking_met": "dochteronderneming",
      "verschil": "Bij een (integraal geconsolideerde) dochteronderneming wordt het consolidatieverschil vastgesteld door integrale compensatie van de deelneming met het pro-rata aandeel in het eigen vermogen (KB WVV art. 3:127, a) jo. art. 3:130, eerste lid). Het verschil moet vervolgens 'zoveel mogelijk' worden toegerekend aan onder-/overgewaardeerde actief- en passiefbestanddelen van die dochter. Het residu komt in de balanspost 'Consolidatieverschillen' (KB WVV art. 3:130, tweede lid) en wordt afgeschreven volgens de vermoedelijke gebruiksduur (KB WVV art. 3:131, § 1).",
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
          }
        ]
      }
    },
    {
      "vergelijking_met": "geassocieerde-onderneming",
      "verschil": "Bij een geassocieerde onderneming (vermogensmutatie) wordt het consolidatieverschil per transactie bepaald op basis van het verschil tussen de boekwaarde van de deelneming en de overeenstemmende fractie van het eigen vermogen. Beide regimes kennen toerekening aan onderliggende activa/passiva en boeking van het residu als consolidatieverschil — maar CBN 2013/3 stelt expliciet dat bij geassocieerde ondernemingen de toewijzing 'slechts voor zover dit mogelijk is' gebeurt (KB WVV art. 3:142, § 3), wat in de praktijk vaak een grotere niet-toegerekende rest geeft dan bij integrale consolidatie. Bovendien verschijnt het residu bij vermogensmutatie niet als afzonderlijke balanspost maar gevolgd naast de post 'Vennootschappen waarop vermogensmutatie is toegepast' (KB WVV art. 3:141; CBN 2022/11).",
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_praktische-uitwerking",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_eerste-consolidatie",
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

## Record: `intragroep-eliminaties`

**Gaps te verwerken** (1 stuks):

```json
[
  {
    "record_id": "intragroep-eliminaties",
    "aspect": "berekeningsmethode.concreet_voorbeeld",
    "reden": "Stappen aanwezig maar geen gewerkt voorbeeld voor niet-gerealiseerde voorraadwinst. Typische examenvraag (moeder verkoopt 100 aan dochter, marge 30%, nog 40 in voorraad) niet beantwoordbaar zonder cijferuitwerking.",
    "prio": "hoog",
    "geconstateerd_door": "v3-vs-v2-rapport-2026-05-15",
    "geconstateerd_op": "2026-05-15T14:42:33.914454+00:00",
    "status": "open"
  }
]
```

**Bron-bundle**: `data/extractie/1.4/enrich-runs/bundle-intragroep-eliminaties-enrich-run-20260515T144255Z.json` — 440 chunks beschikbaar (bronnen: advies, norm, wettekst)

**Bestaand record** (`data/concept_records/intragroep-eliminaties.json`):

```json
{
  "id": "intragroep-eliminaties",
  "naam": "Intragroep-eliminaties",
  "node_type": "procedure",
  "schema_version": "1.2",
  "status": "seed",
  "linked_anchors": [
    "1.4.I.D",
    "1.4.I.G",
    "1.4.I.B",
    "1.4.taak.1"
  ],
  "_provenance": {
    "extractor_run": "concept-extractie-v3-2026-05-15T13:36Z",
    "model": "claude-opus-4-7",
    "anchor_id": "1.4.I.D",
    "dekt_ook_anchors": [
      "1.4.I.G",
      "1.4.I.B",
      "1.4.taak.1"
    ],
    "reviewed_by": null
  },
  "verplichting": {
    "text": "Bij de opstelling van de geconsolideerde jaarrekening moeten alle wederzijdse opbrengsten, kosten, vorderingen, schulden en in activa begrepen onderlinge winsten of verliezen tussen de in de consolidatie opgenomen vennootschappen worden geëlimineerd, om te vermijden dat dezelfde transacties dubbel verschijnen en dat winsten op interne transacties worden gerealiseerd in de groepscijfers terwijl ze economisch niet zijn gerealiseerd buiten de groep.",
    "confidence": "grounded",
    "source": {
      "type": "kb",
      "short": "KB WVV art. 3:134 jo. art. 3:136"
    },
    "references": [
      {
        "type": "kb",
        "short": "KB WVV art. 3:134 (balans)"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:136 (resultatenrekening)"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:138 (toelichting)"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:139 (materialiteitsuitzondering)"
      },
      {
        "type": "kb",
        "short": "KB WVV art. 3:140, a (evenredige consolidatie — pro-rata eliminatie)"
      }
    ],
    "_provenance": {
      "inputs": [
        {
          "id": "KB-WVV-2019__art_3_106",
          "sha256": null,
          "version": "rag-v1"
        },
        {
          "id": "KB-WVV-2019__art_3_107",
          "sha256": null,
          "version": "rag-v1"
        },
        {
          "id": "KB-WVV-2019__art_3_109",
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
  "stappen": [
    {
      "volgorde": 1,
      "text": "Identificeer onderlinge vorderingen en schulden tussen de consoliderende vennootschap en de in de consolidatie opgenomen dochters (en tussen die dochters onderling). Schrap die zowel aan actiefzijde (vorderingen) als aan passiefzijde (schulden) — de geconsolideerde balans behoudt enkel posities tegenover derden buiten de groep.",
      "actor": "consoliderende vennootschap"
    },
    {
      "volgorde": 2,
      "text": "Identificeer in de waarde van activa in de geconsolideerde balans begrepen onderlinge winsten of verliezen uit intra-groepsverkopen (typisch: voorraad of materiële vaste activa verkocht binnen de groep met een marge). Schrap die winsten of verliezen — het actief moet in de geconsolideerde balans terug naar de oorspronkelijke kostprijs voor de groep.",
      "actor": "consoliderende vennootschap"
    },
    {
      "volgorde": 3,
      "text": "Identificeer onderlinge opbrengsten en kosten uit intra-groepstransacties (interne verkopen, beheersvergoedingen, intresten, huur). Schrap die uit de geconsolideerde resultatenrekening.",
      "actor": "consoliderende vennootschap"
    },
    {
      "volgorde": 4,
      "text": "Voor evenredig geconsolideerde gemeenschappelijke dochters: eliminaties beperken tot het pro-rata deel (KB WVV art. 3:140, a). De moeder elimineert geen 100 % van de intra-groepswinst, maar slechts in functie van haar belangenpercentage.",
      "actor": "consoliderende vennootschap"
    },
    {
      "volgorde": 5,
      "text": "Beoordeel of de eliminaties van te verwaarlozen betekenis zijn (KB WVV art. 3:139). Eliminaties bedoeld in art. 3:134, 3:136, eerste lid, 1° en 2°, en 3:138 mogen achterwege blijven wanneer de bedragen, gelet op het doel van het getrouwe beeld (art. 3:105), van te verwaarlozen betekenis zijn.",
      "actor": "consoliderende vennootschap"
    },
    {
      "volgorde": 6,
      "text": "Pas in de toelichting de inlichtingen aan: de op te nemen inlichtingen over het geheel van de consoliderende vennootschap en haar dochters slaan niet op de wederzijdse rechten en verplichtingen die zijn weggelaten (KB WVV art. 3:138).",
      "actor": "consoliderende vennootschap"
    }
  ],
  "in_praktijk": [
    {
      "aspect": "Verkocht actief vs. verkochte dienst",
      "betekenis": "Bij intra-groepsverkoop van een actief dat bij de koper nog op de balans staat (voorraad, materieel actief), wordt zowel de winst (kostprijs verkochte goederen, opbrengsten) als de boekwaarde-aanpassing geëlimineerd. Bij intra-groepsdiensten (administratie, beheersvergoedingen) volstaat de eliminatie van de opbrengsten en kosten — er is geen impact op activa want de dienst is reeds 'verbruikt'.",
      "herkenningspunt": "Vraag: is het verkochte actief nog binnen de groep aanwezig op balansdatum? Zo ja: elimineer ook de marge in het actief. Zo nee: enkel de P&L-eliminatie.",
      "confidence": "inferred-from-aggregation",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:134, 2° + 3:136"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_106",
            "sha256": null,
            "version": "rag-v1"
          },
          {
            "id": "KB-WVV-2019__art_3_107",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "aspect": "Belastinggevolgen op intragroep-winst",
      "betekenis": "Bij eliminatie van een intra-groepswinst kan er een tijdelijk belastingverschil ontstaan: de winst is fiscaal reeds belast (in de jaarrekening van de verkopende dochter), maar consolideringsgewijs ongerealiseerd. KB WVV art. 3:119 voorziet in een specifieke behandeling van het belastingverschil bij consolidatie.",
      "confidence": "inferred-from-aggregation",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:119"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_94",
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
      "verschil": "Intragroep-eliminaties zijn een verplicht onderdeel van de integrale consolidatie (KB WVV art. 3:134, 3:136). Ze definiëren ze niet — ze realiseren het beginsel dat de groep als één economische entiteit wordt voorgesteld.",
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_106",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "vergelijking_met": "evenredige-consolidatie",
      "verschil": "Bij evenredige consolidatie gelden de eliminaties op het pro-rata deel (KB WVV art. 3:140, a) — niet voor 100 %. De integrale eliminatie zou een verkeerd resultaat geven omdat slechts een deel van de transactie tot de groepsentiteit behoort.",
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
      "vergelijking_met": "vermogensmutatiemethode",
      "verschil": "Bij vermogensmutatie worden de activa/passiva van de geassocieerde niet in de geconsolideerde balans opgenomen — eliminatie op balansniveau is dus niet nodig. Wel wordt het pro-rata aandeel in intra-groepswinsten begrepen in de waarde van een actief uit het 'Aandeel in het resultaat van vennootschappen waarop vermogensmutatie is toegepast' geweerd (CBN 2022/11).",
      "_provenance": {
        "inputs": [
          {
            "id": "CBN-2022-11-vermogensmutatiemethode__sec_intra-groepsverkopen-upstream-downstream-sales",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    }
  ],
  "valkuilen": [
    {
      "text": "Eliminaties kunnen om materialiteitsredenen achterwege blijven (KB WVV art. 3:138 jo. art. 3:139), maar de toets is 'van te verwaarlozen betekenis, gelet op het doel van art. 3:105 (getrouw beeld)'. Materialiteit beoordelen op het niveau van de groep, niet van de individuele post.",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:139"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_110",
            "sha256": null,
            "version": "rag-v1"
          }
        ]
      }
    },
    {
      "text": "Een intra-groepsverkoop tegen kostprijs (zonder marge) levert geen te elimineren winst op de balans op, maar de opbrengsten en kosten moeten nog steeds worden geschrapt uit de resultatenrekening (KB WVV art. 3:136, 1°).",
      "confidence": "grounded",
      "source": {
        "type": "kb",
        "short": "KB WVV art. 3:136, 1°"
      },
      "_provenance": {
        "inputs": [
          {
            "id": "KB-WVV-2019__art_3_107",
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

