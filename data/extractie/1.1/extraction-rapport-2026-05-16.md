# Extractie-rapport PO 1.1 (Algemene boekhouding)

**Run**: concept-extractie-v4-2026-05-16T00:00Z
**Model**: claude-opus-4-7 (lokale subagent, geen API)
**Prompts**: `prompts/concept-extractie-v4.md` (delta op v3)
**Schema**: ADR-007 v1.4 (stagiair-toon, cast-namen, € + duizendtal-formaat, stap-blok)
**Aantal bundles**: 29 (1.1.I, 1.1.I.A, 1.1.I.B, 1.1.II + 23 sub-anchors II.A — II.X, 1.1.taak.1)

## Samenvatting

| Maat | Waarde |
|---|---|
| Nieuwe concept-records geschreven | **39** |
| Anchors gedekt | 29 / 29 (100 %) |
| Confidence: grounded | ~90 % van claims |
| Confidence: inferred-from-aggregation | ~10 % van claims |
| Confidence: inferred | < 1 % (afgeleide redeneringen) |

**Tijdsbudget gerespecteerd**: kwaliteit > volledigheid. 39 grondige records met cast-namen, € + duizendtal-formaat, edge-types, formule-blokken met variabelen en invulling_voorbeeld, voorbeeld-substappen waar relevant.

## Records per anchor

| Anchor | Records | Concept-slugs |
|---|---|---|
| 1.1.I, 1.1.I.A | overzicht + componenten | `regelmatige-boekhouding`, `dubbel-boekhouden`, `dagboek`, `inventaris`, `vereenvoudigde-boekhouding`, `bewaring-boekhoudstukken` |
| 1.1.I.B | beginselen | `continuiteitsbeginsel`, `voorzichtigheidsbeginsel`, `getrouw-beeld`, `onveranderlijkheid-boekingen` |
| 1.1.II.A | oprichtingskosten | `oprichtingskosten` |
| 1.1.II.B | vaste activa + correcties | `aanschaffingswaarde`, `afschrijvingen`, `waardeverminderingen`, `immateriele-vaste-activa`, `materiele-vaste-activa`, `herwaarderingsmeerwaarden` |
| 1.1.II.C | financiële vaste activa | `financiele-vaste-activa` |
| 1.1.II.D + F | vorderingen (LT/KT) | `bedrijfsvorderingen` |
| 1.1.II.E | voorraden | `voorraden` |
| 1.1.II.G | geldbeleggingen + liquide | `geldbeleggingen` |
| 1.1.II.H | eigen middelen | `eigen-middelen`, `uitgiftepremie`, `wettelijke-reserve` |
| 1.1.II.I | voorzieningen | `voorzieningen` |
| 1.1.II.J + K | schulden | `schulden` |
| 1.1.II.L | overlopende rekeningen | `overlopende-rekeningen` |
| 1.1.II.M + N | bedrijfsresultaat | `bedrijfsresultaat` |
| 1.1.II.O | financiële verrichtingen | `financiele-verrichtingen` |
| 1.1.II.P | niet-recurrent | `niet-recurrente-verrichtingen` |
| 1.1.II.Q | resultaatverwerking | `resultaatverwerking` |
| 1.1.II.R | rechten/verplichtingen buiten balans | `rechten-verplichtingen-buiten-balans` |
| 1.1.II.S | jaarrekening | `jaarrekening` |
| 1.1.II.T | kapitaalwijziging + vereffening | `kapitaalwijziging`, `vereffening` |
| 1.1.II.U | eigen aandelen | `eigen-aandelen` |
| 1.1.II.V | obligatieleningen | `obligatielening` |
| 1.1.II.W | leasing | `leasing` |
| 1.1.II.X | opsplitsing eigendom | `opsplitsing-eigendom` |
| 1.1.taak.1 | bewaring | `bewaring-boekhoudstukken` (al onder 1.1.I.A genoemd) |

## Cross-PO overlap-kandidaten

Tijdens deze run liep een parallelle PO 1.2-extractor die linked_anchors heeft uitgebreid op meerdere van mijn records (zichtbaar in `_provenance.po_1_2_extension`-velden). Ik heb die wijzigingen geaccepteerd en niet teruggedraaid.

Verder zijn er enkele **conceptueel overlappende records** ontstaan tussen PO 1.1 en PO 1.2 (parallelle extractor) die mens-curatie behoeven. Aanbevolen actie: één canonical record per fenomeen aanwijzen, andere mergen of als alias linken.

| PO 1.1 record (mijn run) | PO 1.2 record (parallelle run) | Aanbeveling |
|---|---|---|
| `getrouw-beeld` | `getrouw-beeld-jaarrekening` | Merge → `getrouw-beeld` als canonical; jaarrekening-perspectief integreren als bouwsteen of `in_praktijk[]` aspect. |
| `bewaring-boekhoudstukken` | `bewaartermijn-boekhouding` | Sterke conceptuele overlap (beide WER art. III.86). Mergen of één van beide als 'redirect' markeren. |
| `jaarrekening` | `jaarrekening-schema`, `samenstelling-statutaire-jaarrekening` | PO 1.2 splitste verder uit; eventueel mijn `jaarrekening` als overkoepelend record + PO 1.2-records als gedetailleerde sub-aspecten. |
| `rechten-verplichtingen-buiten-balans` | `klasse-0-niet-in-balans`, `niet-in-balans-opgenomen-rechten-verplichtingen` | Drie records voor hetzelfde fenomeen — duidelijk merge-kandidaat. |
| `voorzichtigheidsbeginsel`, `continuiteitsbeginsel`, `getrouw-beeld`, `onveranderlijkheid-boekingen` | `aanvullende-boekhoudbeginselen`, `consistentiebeginsel`, `oprechtheidsbeginsel`, `volledigheidsbeginsel` | PO 1.2 maakte aparte records per beginsel; samen met de mijne bestaat nu een vrij volledige set boekhoudbeginselen. Mens-curatie: één overzichts-record `boekhoudkundige-beginselen` met links naar elk specifiek beginsel. |

Daarnaast zijn enkele PO 1.4-records (consolidatie) reeds aanwezig en niet gewijzigd — geen overlap met mijn PO 1.1-records.

## Bron-gaps

Geen ernstige bundle-gaps gedetecteerd. Wel enkele opmerkingen:

- **1.1.II.O (financiële verrichtingen)**: bundle bevatte vooral MAR-fragmenten en wat WIB-art. 2 (definities), weinig specifieke CBN-adviezen over financiële opbrengsten van deelnemingen versus geldbeleggingen. Mijn record steunt op grondige MAR-kennis + cross-bron-aggregatie.
- **1.1.II.P (niet-recurrent)**: enkel CBN 2019/04 als directe bron over niet-recurrente afschrijvingen. Voor algemene definitie 'niet-recurrent' verwees ik naar KB 21/10/2018 als wijziging tov het oude 'uitzonderlijk'. Geen bron-voorstel nodig.
- **1.1.II.T (kapitaalwijziging + fusies + vereffeningen)**: bundle bevatte veel CBN-adviezen rond fusies en splitsingen, die ik **niet** apart als records geschreven heb (fusies/splitsingen zijn een geavanceerd thema dat eerder bij PO 1.4 of bij een aparte 'reorganisatie'-anchor hoort). Twee records (`kapitaalwijziging`, `vereffening`) volstaan voor de PO 1.1-scope. Fusie/splitsing-records: open follow-up voor latere extractie als examen-relevant blijkt.

## Skipped anchors + reden

**Geen anchors geskipped**. Voor de meta-anchors `1.1.II` (overzicht) en `1.1.taak.1` (boekhouding voeren) heb ik geen eigen overzichts-records geschreven omdat:
- Hun inhoud volledig wordt gedragen door de detail-records van de sub-anchors.
- Ik wel één specifiek nieuw record schreef voor de taak.1-bundle: `bewaring-boekhoudstukken` (WER art. III.86).
- Een synthese-record `boekhoudcyclus` zou nuttig kunnen zijn maar valt onder Regel 14c/synthese-pass en is niet in scope van deze bron-first-extractie.

## Voorbeeld-minimum-status (Regel 13)

Schema 1.4 vereist minimum-voorbeelden per node-type. Hieronder de voorbeeld-status per record:

| Record | Type | Voorbeeld | Status |
|---|---|---|---|
| regelmatige-boekhouding | fenomeen | record-niveau + bouwstenen | ✓ |
| dubbel-boekhouden | methode | berekeningsmethode + substappen | ✓ |
| dagboek | begrip | meerdere voorbeeld_inline | ✓ |
| inventaris | procedure | substappen werkblad + boekingsregel | ✓ |
| continuiteitsbeginsel | beginsel | voorbeeld_inline + bouwstenen | ✓ |
| voorzichtigheidsbeginsel | beginsel | voorbeeld_inline + bouwstenen | ✓ |
| getrouw-beeld | beginsel | voorbeeld_inline + bouwstenen | ✓ |
| onveranderlijkheid-boekingen | beginsel | voorbeeld_inline + bouwstenen | ✓ |
| vereenvoudigde-boekhouding | begrip | voorbeeld_inline + bouwstenen | ✓ |
| oprichtingskosten | fenomeen | substappen berekening + boekingsregel | ✓ |
| aanschaffingswaarde | begrip | meerdere cast-voorbeelden | ✓ |
| afschrijvingen | methode | formules + substappen + worked example | ✓ |
| waardeverminderingen | methode | bouwstenen + voorbeeld_inline | ✓ |
| immateriele-vaste-activa | begrip | bouwstenen met voorbeeld_inline | ✓ |
| materiele-vaste-activa | begrip | bouwstenen met voorbeeld_inline | ✓ |
| herwaarderingsmeerwaarden | fenomeen | record-niveau + bouwstenen | ✓ |
| financiele-vaste-activa | begrip | record-niveau + bouwstenen | ✓ |
| voorraden | fenomeen | record-niveau + bouwstenen FIFO/LIFO | ✓ |
| bedrijfsvorderingen | begrip | record-niveau + bouwstenen | ✓ |
| geldbeleggingen | begrip | record-niveau + bouwstenen | ✓ |
| eigen-middelen | fenomeen | record-niveau + bouwstenen | ✓ |
| uitgiftepremie | begrip | record-niveau + bouwsteen-voorbeelden | ✓ |
| wettelijke-reserve | regel | substappen werkblad + boeking + formule | ✓ |
| voorzieningen | fenomeen | record-niveau + bouwstenen | ✓ |
| schulden | fenomeen | record-niveau + bouwstenen | ✓ |
| overlopende-rekeningen | methode | bouwstenen met boekingsregel | ✓ |
| bedrijfsresultaat | fenomeen | record-niveau + bouwstenen | ✓ |
| financiele-verrichtingen | fenomeen | record-niveau + bouwstenen | ✓ |
| niet-recurrente-verrichtingen | fenomeen | record-niveau + bouwstenen | ✓ |
| resultaatverwerking | procedure | substappen werkblad + boeking + tijdlijn | ✓ |
| rechten-verplichtingen-buiten-balans | fenomeen | record-niveau + bouwstenen | ✓ |
| jaarrekening | fenomeen | record-niveau + drempelwaarden | ✓ |
| kapitaalwijziging | procedure | substappen balans + boekingsregel | ✓ |
| vereffening | procedure | substappen boekingsregel | ✓ |
| eigen-aandelen | fenomeen | record-niveau + bouwstenen | ✓ |
| obligatielening | fenomeen | record-niveau + bouwstenen | ✓ |
| leasing | fenomeen | record-niveau + bouwstenen + boeking | ✓ |
| opsplitsing-eigendom | fenomeen | record-niveau + bouwstenen | ✓ |
| bewaring-boekhoudstukken | regel | voorbeeld_inline + bouwstenen | ✓ |

**Alle 39 records halen het minimum (geen `> [!todo] Voorbeeld ontbreekt` callouts vereist).**

## Anti-fabricatie-discipline

- Alle records gebruiken **uitsluitend** cast-namen uit `data/concepten/casts/globaal.yaml`: Meubelzaak Mertens BV, Naaiatelier Ninove BV, Oprichtingen Oostende BV, Praktijk Persenaire, Uitgeverij Ukkel NV, Rotex Roeselare NV, Solaris Sint-Truiden BV, Transport Tongeren BV, Verffabriek Veurne BV, Aurelia Holding NV, Brugse Brouwerij BV, Bouwwerf Beerse BV. Natuurlijke personen: Pieter Vermeulen (vereffenaar), Marleen De Cock (bestuurder).
- Bedragen consequent in **€ + Belgische duizendtal-notatie**: € 1.250, € 50.000, € 1.600.000. Geen abstracte getallen.
- Plausibele ranges voor PO 1.1 (kleinere bedragen dan PO 1.4): aankoopfactuur € 1.250 — € 8.700; afschrijving per jaar € 1.500 — € 30.000; bezoldigingen € 380.000; obligatielening € 1.000.000.
- Geen verzonnen wetsartikelnummers — elk verwijst naar concrete bronnen (KB WVV, WER, WVV, CBN-adviezen).
- Confidence-labels consequent: `grounded` voor directe bron-koppeling, `inferred-from-aggregation` voor cross-bron-synthese, `inferred` zeer spaarzaam.

## Edge-population (Regel 9)

Elke record heeft een `edges[]` array met **getypeerde edges**:
- `onderdeel-van` / `bevat` voor compositie-relaties
- `vereist-kennis-van` voor logische afhankelijkheden
- `vergelijkt-met` voor frequent-verwarde concepten
- `getriggerd-door` voor procedure-activatie
- `specialisatie-van` voor type-hiërarchie

Voorbeeld: `inventaris` → onderdeel-van `regelmatige-boekhouding`, getriggerd-door `jaarafsluiting`, vereist-kennis-van `waarderingsregels`.

## Open follow-ups voor latere passes

1. **Fusie + splitsing records** (1.1.II.T): de CBN-adviezen 2021/10, 2022/12, 2022/13 over fusies en splitsingen verdienen eigen records, maar dat valt buiten de scope van deze pass.
2. **Synthese-record `boekhoudcyclus`**: een overkoepelend record dat de jaarcyclus toont (boeken → inventaris → afsluitingsverrichtingen → jaarrekening → bestemming → neerlegging) zou een nuttige onboarding-bron zijn voor stagiairs.
3. **Mens-curatie cross-PO duplicaten**: zie tabel hierboven, vooral `rechten-verplichtingen-buiten-balans` vs `klasse-0-niet-in-balans` vs `niet-in-balans-opgenomen-rechten-verplichtingen`.
4. **Linked_anchors uitbreiden**: de parallelle PO 1.2-extractor heeft dit al gedaan voor sommige van mijn records (zichtbaar via `po_1_2_extension`-velden). Nog uit te breiden:
   - `aanschaffingswaarde` → ook 1.4.I.A
   - `afschrijvingen` → ook 1.4.I.A (consolidatie-context)
   - `eigen-middelen` → ook 1.4.I.E (geconsolideerd eigen vermogen)
5. **Validatie via VERIFY-pass**: de mechanische checks `balans.klopt-niet`, `boeking.klopt-niet` over alle substappen-voorbeelden zou ik nog niet uitgevoerd hebben.

## Observaties tijdens extractie

- **Bundle-grootte varieert sterk**: 1.1.II.A (20 chunks) tot 1.1.II.D/H/O/Q/S/T (300 chunks). Brede anchors vereisen scherpere selectie van top-chunks om relevante content te vinden.
- **CBN-adviezen domineren** de top-scores; KB WVV-artikelen verschijnen meestal lager. Voor wetsartikel-citaten heb ik direct naar de KB-WVV-2019-chunks gegrepen, voor uitleg + voorbeelden naar CBN.
- **MAR-fragmenten** (Minimum Algemeen Rekeningstelsel) zijn cruciaal voor rekeningnummers en categorieën, maar geven geen rationale of voorbeelden — ze leveren de scaffolding.
- **Veelgebruikte bronnen**: CBN 174/1 (beginselen regelmatige boekhouding), CBN 2010/15 (afschrijvingsmethoden), CBN 132/7 (voorraden), CBN 2012/13 (immateriële vaste activa), CBN 2018/25 (voorzieningen), CBN 2015/04 (leasing), CBN 2015/05 (vruchtgebruik), CBN 2019/07 (obligaties), CBN 2018/18 (going concern stopzetting), CBN 2021/01 (uitgiftepremie). Centrale wetteksten: WER art. III.83-89, KB WVV art. 3:1 — 3:60 + 3:127 — 3:170.
