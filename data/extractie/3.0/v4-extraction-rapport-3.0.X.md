# EXTRACT v4 — Rapport PO 3.0.X (Insolventiewetgeving)

**Run-id**: `concept-extractie-v4-2026-05-20`
**Anchor**: 3.0.X "Insolventiewetgeving (boek XX van het Wetboek Economisch recht)"
**Wave**: Wave 1 vervolg na pilot 3.0.II/3.0.I/3.0.IV/3.0.IX
**Model**: claude-opus-4-7
**Schema**: 1.6

---

## Aantal records

| Categorie | Aantal |
|---|---|
| Nieuw aangemaakt | 17 |
| Bijgewerkt | 0 |
| Hernoemd | 0 |
| Verwijderd | 0 |

**Audit na save**: `disk: 543 records, RAG: 543, content: 504 fiches — OK, in sync.**

Records gemaakt:

| Id | node_type | Korte beschrijving |
|---|---|---|
| `insolventieprocedures-belgie` | cluster | Kapstok over Boek XX WER (preventief / reorganisatie / faillissement) |
| `faillissement` | cluster | Faillissementsprocedure (voorwaarden, organen, verloop, sluiting, kwijtschelding) |
| `gerechtelijke-reorganisatie` | cluster | Reorganisatieprocedure (vier varianten + besloten) |
| `vroegtijdige-waarschuwing-insolventie` | cluster | Knipperlichten + Kamer voor ondernemingen in moeilijkheden |
| `besloten-voorbereiding-faillissement` | cluster | Pre-pack-mechanisme (XX.97/1 e.v., sinds 2023) |
| `voorwaarden-faillietverklaring` | regel | Duurzame staking van betaling + geschokt krediet (cumulatief) |
| `opschorting-betaling-gerechtelijke-reorganisatie` | regel | Moratorium tijdens reorganisatie (XX.50) |
| `meldingsplicht-accountant-continuiteit` | regel | XX.23 § 3 — meldingsplicht beoefenaars + uitzondering op beroepsgeheim |
| `verdachte-periode-faillissement` | regel | XX.111 (onweerlegbaar) en XX.112 (bij kennis) niet-tegenwerpbaarheid |
| `curator-faillissement` | autoriteit | Gerechtsmandataris die boedel beheert en vereffent |
| `rechter-commissaris-insolventie` | autoriteit | Toeziende rechter binnen insolventierechtbank |
| `schuldvergelijking-tijdens-opschorting` | begrip | Compensatie enkel bij verknochtheid (XX.55) |
| `buitengerechtelijk-minnelijk-akkoord` | begrip | Lichtste preventieve uitweg (XX.64) |
| `gerechtelijke-reorganisatie-varianten-vergelijking` | synthese | Vergelijkingstabel 6 varianten |
| `insolventietriage-beslisboom` | synthese | 5-stappen-beslisboom voor accountant |
| `kwijtschelding-natuurlijke-persoon-gefailleerde` | regel | Fresh start voor natuurlijke persoon (XX.171) |
| `boekhoudkundige-verwerking-insolventie-akkoord` | regel | CBN-2021/07 — boeking kwijtschelding als uitzonderlijke opbrengst |

## Mix vs. verwachting

| Type | Verwacht | Geleverd |
|---|---|---|
| cluster | 3-5 | 5 |
| regel | 4-6 | 6 |
| begrip + autoriteit | 3-4 | 4 (2 autoriteit + 2 begrip) |
| synthese | 2-3 | 2 |

Doel-spreiding gehaald (17 records, midden-bovenkant van het bereik van 12-18).

## Edges-overzicht

| Edge-type | Aantal voorkomens | Voornaamste targets |
|---|---|---|
| `onderdeel-van` | 14 | `insolventieprocedures-belgie` (4×), `faillissement` (5×), `gerechtelijke-reorganisatie` (3×) |
| `vergelijkt-met` | 9 | `faillissement`↔`gerechtelijke-reorganisatie`, `curator`↔`rechter-commissaris`, `gerechtelijke-ontbinding`, `ontbinding-vennootschap`, `vereffening` |
| `vereist-kennis-van` | 8 | `continuiteitsbeginsel` (3×), `opschorting-betaling-gerechtelijke-reorganisatie`, `kamer-ondernemingen-in-moeilijkheden`, `meldingsplicht-accountant-continuiteit`, `schuldvergelijking-tijdens-opschorting` |
| `getriggerd-door` | 2 | `voorwaarden-faillietverklaring`, `faillissement` |
| `uitzondering-op` | 1 | `beroepsgeheim` (pending target) |
| `verwijst-naar` | 6 | Cross-links naar `kamer-ondernemingen-in-moeilijkheden`, syntheses ↔ clusters |

Cross-PO bridges naar PO 1.x: `continuiteitsbeginsel` (PO 1.1), `kamer-ondernemingen-in-moeilijkheden` (PO 1.3.I.D), impliciet naar `continuiteitsveronderstelling-audit` (PO 1.x audit).

Cross-PO bridges binnen 3.0: `gerechtelijke-ontbinding`, `ontbinding-vennootschap`, `vereffening` — duidelijk afgebakend van insolventie via `vergelijkt-met`-edges met aspect.

## Gaps.json-toevoegingen

**9 nieuwe entries** in `data/extractie/gaps.json` (van 958 → 967).

| Aspect | Aantal | Prio-mix |
|---|---|---|
| `records.ontbreekt` | 5 | 1× hoog (geen), 3× midden, 1× laag |
| `bron-gap` | 2 | 1× midden, 1× laag |
| `context-edge-ontbreekt` | 1 | midden |
| `dangling-reference` | 1 | laag |

Belangrijkste gaps:
- **3.0.VII-bridge**: aansprakelijkheidsregimes specifiek voor insolventie (kennelijk grove fout — kwijtscheldingscontext, voortzetting verlieslatende activiteit, wrongful trading) bewust uit scope; cross-link verwacht bij wave 3.0.VII.
- **Sub-anchor 3.0.X.A-F**: top-level kapstokken aangelegd, sub-anchor-detail (rangorde, samenloop, voorrechten, EU-grensoverschrijdende insolventie) hoort in wave 2.
- **Boekhoud-CBN-detail**: CBN-2021/07 alleen via inleidings-chunk beschikbaar; volledig advies hercheck-kandidaat voor RAG-bundle-uitbreiding.
- **Edge-update bestaand record**: `kamer-ondernemingen-in-moeilijkheden` heeft `onderdeel-van: vroegtijdige-waarschuwing-insolventie`-edge nodig (+ anchor 3.0.X toevoegen) bij next-touch.

## Migraties

Geen migraties gedaan in deze wave — alle records zijn nieuw aangemaakt. Geen `voorbeeld_inline`-→-`voorbeelden`-migraties, geen schema-1.4-→-1.5-type-hernoemingen, geen `doel`-→-`situering`-conversies (bestaande records niet aangeraakt).

## Claims `inferred-from-aggregation`

Records met substantiële cross-bron- of cross-chunk-synthese (gemarkeerd in de respectievelijke velden):

- `insolventieprocedures-belgie` — situering en in_praktijk-blok (synthese over Boek XX-structuur + CBN-2021/07-inleiding)
- `faillissement` — situering, valkuilen, in_praktijk (synthese over verschillende artikelen XX.98-171)
- `gerechtelijke-reorganisatie` — situering (synthese over XX.83/22 + CBN)
- `vroegtijdige-waarschuwing-insolventie` — situering, in_praktijk (synthese over XX.21+XX.23+XX.29/1)
- `besloten-voorbereiding-faillissement` — situering (afleiding uit XX.97/1)
- `voorwaarden-faillietverklaring` — voorwaarden (combinatie XX.99/XX.100), situering
- `verdachte-periode-faillissement` — situering, voorwaarden (combinatie XX.111-XX.112)
- `meldingsplicht-accountant-continuiteit` — in_praktijk (synthese deontologie + WER)
- `curator-faillissement` — rol (synthese verschillende XX-artikelen)
- `gerechtelijke-reorganisatie-varianten-vergelijking` — geheel synthese (drie kerninzichten inferred-from-aggregation)
- `insolventietriage-beslisboom` — geheel synthese, ook kerninzicht-2 `inferred`
- `boekhoudkundige-verwerking-insolventie-akkoord` — situering, voorwaarde-3 (continuïteits-impact gekruist met CBN-2018/18)

Alle claims hebben minstens één `_provenance.inputs[]` met chunk-id.

## Open observaties (narratieve patronen)

1. **WER Boek XX-structuur is sterk normatief-procedureel**, met weinig declaratieve definities. Veel relevante begrippen (verknochtheid, geschokt krediet, duurzame staking van betaling) zijn doctrinair-rechtspraak-gevormd en niet direct in chunks aanwezig — dat dwong tot inferred-from-aggregation-confidence. Bron-bundle-uitbreiding met doctrine-bronnen (handboek insolventierecht) zou hierin verbeteren.

2. **Boek XX is volop in evolutie** — twee grote hervormingen (W 2017-08-11 oprichting, W 2023-06-07 omzetting EU-Restructuring-richtlijn) hebben sinds 2018 al verschillende delen ingrijpend gewijzigd (besloten reorganisatie, besloten voorbereiding faillissement, cross-class cram-down). Records moeten op middellange termijn opnieuw worden gecheckt op recente W 2024-05-15 wijzigingen.

3. **Regime-cluster-heuristiek werkte hier minder** dan in WVV-procedures: insolventie kent geen BV/NV/CV-regime-variantie, wel **procedure-variantie** (4 GRP-varianten). De synthese `gerechtelijke-reorganisatie-varianten-vergelijking` vervult de rol die in WVV door regime-clusters wordt vervuld.

4. **Brugfunctie naar PO 1.1 / 1.3 / 1.x**: insolventie raakt direct continuïteitsbeginsel (PO 1.1), kamer-ondernemingen-in-moeilijkheden (PO 1.3.I.D), continuiteitsveronderstelling-audit (PO 1.x audit), beroepsgeheim/meldingsplicht (PO 1.10 deontologie). Bij latere passes over PO 1.x is wederzijdse edge-consistentie vereist (zie context-edge-ontbreekt-gap).

5. **Cijferzakboekje-onafhankelijkheid**: alle records zijn vrij van tarief- of bedrag-afhankelijkheid. Stagiair moet de procedurele logica begrijpen — alle relevante drempels (15 dagen opschorting, 30 dagen aangiftetermijn, etc.) zijn niet-cijferzakboekje-data en horen wel in records.

## Zelf-evaluatie

| Criterium | Score | Toelichting |
|---|---|---|
| Stagiair-niveau Nederlands | ✓ | Vermijden van wetgeeftaal; valkuilen in stagiair-perspectief |
| Cast-conventie | ✓ | Meubelzaak Mertens, Verffabriek Veurne, Naaiatelier Ninove, Transport Tongeren, Solaris Sint-Truiden, Brugse Brouwerij, Energiehuis Evergem — allen uit `casts/globaal.yaml` |
| Bedragen €-formaat | ✓ | € 1.500.000-stijl met punt als duizendsep |
| Geen bron-genaamde records | ✓ | Geen `wer-boek-xx`, geen `insolventiewet-2017`; alle records benoemen het fenomeen |
| Confidence-labels | ✓ | grounded waar chunk-id direct dekt; inferred-from-aggregation bij synthese ≥ 2 bronnen/chunks; inferred met ratio bij echte redenering |
| Provenance op elk inhoudelijk veld | ✓ | Elke definitie, situering, voorwaarde, bouwsteen heeft `_provenance.inputs` |
| Edge-canoniciteit | ✓ | Enkel de 7 canonieke types; geen `bevat`, geen `contrasteert-met`, geen `vervangt` |
| Near-duplicate-check | ✓ | Bestaand `kamer-ondernemingen-in-moeilijkheden` niet gedupliceerd, wel cross-gelinkt |
| Concretiserings-velden | ✓ | In_praktijk + voorbeelden + 1 illustratie (boeking kwijtschelding) |
| Audit groen | ✓ | 543 records disk = RAG; OK |
| Worktree-cwd workaround | ✓ | `os.chdir('/Users/stivni/Documents/ITAA/certificaid')` in elk batch-script |
| Gaps.json absoluut pad | ✓ | Verplicht protocol gevolgd — geen relatief pad |

Sterkste punten:
- 5 clusters bouwen een **coherente kapstok-laag** over alles van vroegtijdige waarschuwing tot kwijtschelding.
- De synthese `gerechtelijke-reorganisatie-varianten-vergelijking` met 6-rijige vergelijkingstabel maakt de complexe GRP-variant-keuze direct hanteerbaar.
- De synthese `insolventietriage-beslisboom` brengt de accountant-specifieke kijk — geen pure juridische beschrijving maar een diagnostisch-procedureel hulpmiddel.

Aandachtspunten:
- `boekhoudkundige-verwerking-insolventie-akkoord` leunt op één CBN-inleidings-chunk + algemene boekhoudkennis. Sterkere bron-grounding wenselijk (full CBN-2021/07 in RAG).
- `verdachte-periode-faillissement` baseert zich op chunks XX.111-XX.112 maar de term 'verdachte periode' en de bevoegdheid van de rechtbank om de datum staking van betaling te bepalen, komen impliciet uit doctrine.
- `kwijtschelding-natuurlijke-persoon-gefailleerde` heeft de niet-kwijtscheldbare-schulden-uitzondering als `inferred` — exacte WER-grondslag bevestigen bij next-touch.

## Volgende stappen

**Wave 2 voor 3.0.X** (sub-anchor-detail):
- 3.0.X.A — Vroege detectie-instrumenten (extra: voortzettingsverklaring na gewichtig verlies, knipperlicht-doctrine)
- 3.0.X.C — GRP-procedurele detail (categorie-indeling schuldeisers, dubbele meerderheid, cross-class cram-down, herstructureringsdeskundige rol)
- 3.0.X.D — Faillissementsdetail (voorrechten en rangorde, samenloop, terugvordering, gevolgen voor echtgenoten)
- 3.0.X.F — Schuldvergelijking + samenloop diepgang

**Andere onmiddellijke werk-items**:
- Bestaand record `kamer-ondernemingen-in-moeilijkheden` updaten: edge `onderdeel-van: vroegtijdige-waarschuwing-insolventie` + `linked_anchors` aanvullen met `3.0.X`.
- Cross-PO sync naar PO 1.x (continuiteitsbeginsel, continuiteitsveronderstelling-audit): wederzijdse edges. Volgt bij volgende PO 1.x-pass.
- Wave voor 3.0.VII bestuurdersaansprakelijkheid: vermelden kennelijk-grove-fout, voortzetting verlieslatende activiteit als insolventie-specifieke aansprakelijkheidsgronden.
