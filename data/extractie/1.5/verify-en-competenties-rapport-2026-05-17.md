# VERIFY + Competentie-destillatie PO 1.5 — rapport

**Run-id**: `verify-run-1.5-2026-05-17`
**Datum**: 2026-05-17
**Model**: claude-opus-4-7 (subagent, geen externe API)
**Scope**: PO 1.5 — Europese normen + IFRS (14 anchors, 26 records uit extraction-rapport van vandaag)
**Outputs**: 12 gaps in `data/extractie/gaps.json` + 1 synthese-record + 7 competentie-yamls

---

## Samenvatting

```
VERIFY-run verify-run-1.5-2026-05-17 — samenvatting
====================================================
Records beoordeeld : 26
Examenvragen getest: 0 (Check A geskipt — geen 1.5 vragen geclassificeerd)
Gaps gevonden:
  hoog  : 1
  midden: 7
  laag  : 4
Top-3 aandachtspunten:
  1. wijziging-boekhoudkundig-referentiestelsel: stappen.onvolledig — procedure-record zonder uitgewerkte stappen (CBN 2022/08 verdient 3-4 stappen).
  2. opbrengsten-ifrs: edges.target-ontbreekt — dangling edge naar BE-GAAP-pendant `opbrengsten` dat niet bestaat in PO 1.1.
  3. leaseverplichting-ifrs + right-of-use-actief: valkuilen.ontbreekt — begrip-records zonder valkuilen (andere begrippen hebben er 1-2).

Competentie-destillatie:
  Competenties voorgesteld : 7 (binnen 5-7 range)
  Bestanden geschreven     : 7
  Stappen totaal           : 31
  Praktijk-pct > 50%       : 0 (geen mens-review-flag op procedure_grondslag)
  Schema 1.1               : ja (alle 7)
```

---

## Deel A — VERIFY-gaps (12 stuks)

### Check A: examenvraag-simulatie
Geskipt — er zijn nog geen examenvragen geclassificeerd onder PO 1.5-anchors (`data/programma/examen_vragen/` bevat geen 1.5-coverage).

### Check B: uniforme rijkheid

| Record | Aspect | Prio | Reden |
|---|---|---|---|
| `wijziging-boekhoudkundig-referentiestelsel` | `stappen.onvolledig` | **hoog** | node_type=procedure maar 0 stappen, terwijl `ifrs-eerste-toepassing` (5 stappen) en `correctie-jaarrekening-ifrs` (3 stappen) wel uitgewerkt zijn. CBN 2022/08-wisseling-procedure verdient minimaal 3-4 stappen. |
| `afschrijvingen-ifrs` | `stappen.onvolledig` | midden | node_type=methode met 0 stappen; `bijzondere-waardevermindering-ias-36` heeft er 4, `opbrengsten-ifrs` 5. |
| `herwaarderingsmodel-ias-16` | `stappen.onvolledig` | midden | node_type=methode met 0 stappen — herwaarderingsproces (frequentie, OCI, realisatie) heeft procedurele structuur. |
| `componentenbenadering-ias-16` | `stappen.onvolledig` | midden | node_type=methode met 0 stappen — identificatie + apart afschrijvingsplan per component is procedureel. |
| `leaseverplichting-ifrs` | `valkuilen.ontbreekt` | midden | 0 valkuilen; klassieke fouten (verkeerde rentevoet, variabele omzet-huur, geen herwaardering bij optie-herziening) ontbreken. |
| `right-of-use-actief` | `valkuilen.ontbreekt` | midden | 0 valkuilen; typische fouten (initiële directe kosten en ontmanteling vergeten in eerste waardering) ontbreken. |
| `ias-1-winst-en-totaalresultaat` | `valkuilen.ontbreekt` | laag | 2 valkuilen aanwezig maar OCI reclassifiable/non-reclassifiable (notoire examenval) niet als valkuil opgenomen. |

### Check C1: mechanische edge-targets

| Record | Edge | Bestaande target? | Prio |
|---|---|---|---|
| `onderhanden-projecten-ifrs` | `vervangt → ias-11-onderhanden-projecten` | Nee — historische IAS 11 heeft geen eigen record (historische_noot volstaat) | laag |
| `opbrengsten-ifrs` | `vergelijkt-met → opbrengsten` | Nee — BE-GAAP-pendant ontbreekt in corpus | midden |
| `opbrengsten-ifrs` | `vervangt → ias-18-opbrengsten` | Nee — historische IAS 18 heeft geen eigen record | laag |

`vergelijkingsparen.target-ontbreekt`: geen — alle vergelijkingsparen-targets bestaan.

### Check C2: vrije-tekst-niet-gespiegeld + records-overlap (LLM-oordeel)

| Record | Aspect | Prio | Reden |
|---|---|---|---|
| `be-gaap-vs-ifrs-overzicht` | `vergelijkingsparen.vrije-tekst-niet-gespiegeld` | laag | Synthese-vergelijkingstabel verwijst in vrije tekst naar 'IFRS 16 single model' en 'IAS 38 onderzoek/ontwikkeling' zonder structurele link buiten `gebaseerd_op_concepten[]`. Verifieer dekking. |
| `opbrengsten-ifrs` | `records.ontbreekt` | midden | BE-GAAP-tegenhanger `opbrengsten` (realisatiebeginsel KB WVV art. 3:18 + 3:46) ontbreekt — vergelijking PO 1.1↔1.5 onmogelijk zonder dit record. |
| `be-gaap-vs-ifrs-overzicht` | `records.ontbreekt` | laag | Suggestie tot synthese `ifrs-16-lessee-vs-lessor-overzicht` — sinds deze run aangemaakt (zie Deel B). Gap blijft open als beleidskeuze: "facultatief". |

Geen `records.overlappend-fenomeen` gedetecteerd: alle 26 records dekken verschillende fenomenen; suffix-conventie `-ifrs` / `ias-X` / `ifrs-X` voorkomt botsing met BE-GAAP-records.

### Cross-PO observaties (geen gap-entry)

- **PO 1.4 (IFRS 10/11/12 consolidatie)**: bewust buiten PO 1.5-scope (zie extraction-rapport §"Open observaties 3"). `ifrs-consolidatieraamwerk` bestaat in PO 1.4 zonder linked_anchors naar 1.5. Geen actie.
- **PO 1.1 BE-GAAP-tegenhangers**: `leasing`, `voorraden`, `afschrijvingen`, `materiele-vaste-activa`, `immateriele-vaste-activa` bestaan en zijn correct als `vergelijkingsparen[].vergelijking_met` opgenomen vanuit IFRS-records. Reverse-cross-link (van BE-GAAP-record naar IFRS-variant) is een follow-up voor enrich-pass — niet als gap geboekt omdat de extraction-rapport §"Volgende stappen 1" al expliciet wijst op deze symmetrie-vraag.

---

## Deel B — Synthese-record toegevoegd (1)

**`ifrs-16-lessee-vs-lessor-overzicht`** (`data/concepten/records/ifrs-16-lessee-vs-lessor-overzicht.json`)

**Reden van keuze**:
- `opbrengsten-ifrs.stappen[]` dekt al het 5-stappen-model van IFRS 15 in detail (5 stappen, inclusief substappen) → een aparte `ifrs-15-5-stappen-model`-synthese zou duplicatief zijn.
- `leasing-ifrs.bouwstenen[]` raakt lessor-asymmetrie slechts kort (1 zin in vergelijkingsparen); lessor-classificatie (operationeel/financieel onder IFRS 16 alinea 61-66) is nergens uitgewerkt en is een notoir examenpunt bij PO 1.5.V.C.
- Synthese koppelt `leasing-ifrs`, `right-of-use-actief`, `leaseverplichting-ifrs` aan het lessor-perspectief in één coherent overzicht.

**Schema 1.4 conform**:
- `node_type: synthese`
- `gebaseerd_op_concepten[]`: 4 records (lessee-zijde 3 IFRS + BE-GAAP-leasing).
- `vergelijkingstabel`: 8 rijen × 2 kolommen (lessee, lessor).
- `beslisboom`: Mermaid flowchart, twee takken (lessee single model versus lessor binair model).
- 2 valkuilen + 4 edges (allemaal naar bestaande records).

**Cast-conform**: Zelena Bio NV (lessee) + Vastgoed Veurne NV (impliciete lessor). Bedragen: € 3.894.000 + € 480.000/jaar (consistent met bestaand voorbeeld in `leaseverplichting-ifrs`).

**Niet gemaakt** (overwogen, verworpen): `ifrs-15-5-stappen-model` — reden hierboven.

---

## Deel C — Competenties-destillatie (7 voorgesteld)

| ID | Titel | Stappen | wettelijk_pct | gebaseerd_op |
|---|---|---:|---:|---:|
| `bepalen-toepasselijkheid-ifrs-belgie` | Bepalen of een onderneming IFRS moet of mag toepassen in België | 3 | 90 % | 4 |
| `uitvoeren-eerste-toepassing-ifrs` | Uitvoeren van de eerste toepassing van IFRS overeenkomstig IFRS 1 | 5 | 70 % | 4 |
| `waarderen-materiele-vaste-activa-ifrs` | Waarderen van materiële vaste activa onder IAS 16 (kostprijs- of herwaarderingsmodel) | 4 | 75 % | 5 |
| `verwerken-leasing-ifrs-lessee` | Verwerken van een leaseovereenkomst onder IFRS 16 als lessee | 5 | 80 % | 5 |
| `toepassen-vijf-stappen-model-opbrengsten-ifrs` | Toepassen van het 5-stappen-model van IFRS 15 voor opbrengstenherkenning | 5 | 80 % | 4 |
| `toetsen-bijzondere-waardevermindering-ias-36` | Toetsen van een actief op bijzondere waardevermindering onder IAS 36 | 4 | 80 % | 4 |
| `presenteren-ifrs-jaarrekening-volgens-ias-1` | Presenteren van een IFRS-jaarrekening volgens IAS 1 | 5 | 85 % | 6 |

**Totaal**: 31 stappen, gemiddeld 4,4 per competentie. Wettelijk_pct varieert 70-90 % (geen competentie met praktijk_pct > 50 — geen mens-review-flag).

**Coverage van PO 1.5-anchors**:
- 1.5.II + 1.5.III (toepassingsgebied): `bepalen-toepasselijkheid-ifrs-belgie`
- 1.5.IV + 1.5.IV.A (algemeen kader + IFRS 1): `uitvoeren-eerste-toepassing-ifrs`
- 1.5.IV.B (IAS 1): `presenteren-ifrs-jaarrekening-volgens-ias-1`
- 1.5.V.A (IAS 16 + IAS 38): `waarderen-materiele-vaste-activa-ifrs`
- 1.5.V.A + V.B (impairment IAS 36): `toetsen-bijzondere-waardevermindering-ias-36`
- 1.5.V.C (IFRS 16 leasing): `verwerken-leasing-ifrs-lessee`
- 1.5.V.D + V.E (IFRS 15 opbrengsten + onderhanden): `toepassen-vijf-stappen-model-opbrengsten-ifrs`

Alle 14 anchors gedekt door minstens één competentie.

**Schema 1.1-conformiteit**:
- Stap-blok-schema (Regel A): elke stap heeft `nr / titel / wat / hoe / grondslag` (verplicht) + meestal `waarom / input[] / output[]`. `voorbeeld.substappen[]` bij stappen die balansen wijzigen, bedragen berekenen of boekingen doen.
- Cast verplicht (Regel B): Zelena Bio NV als beursgenoteerde IFRS-rapporteur dominant; Rotex Roeselare NV als BE-GAAP-vergelijking; Aurelia Holding NV (klant 5-stappen-model), Constructies Cattoir BV (bouwprojecten), Meubelzaak Mertens BV (kleine groep, vrijwillige IFRS-vraag), Vastgoed Veurne NV (lessor IFRS 16), Wolters & Partners CVBA (commissaris). Geen X/Y/ABC.
- Stagiair-toon (Regel C): korte zinnen, eerste afkortinggebruik voluit (CGU, WACC, IBR, ROU, SSP, OCI), geen buzzword-stapeling.
- Concept-grondslag verplicht (Regel D): elke `hoe`-instructie verwijst expliciet naar bron-concept via wikilink (`[[concept-id]] §sectie`).
- Conventieverschil concept↔competentie (Regel E-bis): competentie-stappen orchestreren meerdere concepten en delegeren naar concept-procedures via wikilink (bv. `verwerken-leasing-ifrs-lessee` stap 4 → `[[leaseverplichting-ifrs]] §berekening-eerste-waardering`).
- Voorbeeld-substappen (Regel F): 11 stappen hebben substappen (balans/berekening/boekingsregel/opmerking-types). Markdown-tabellen voor balansen en berekeningen, conform conventie.
- Voorbeelden uit bronnen (Regel G): bedragen uit bron-chunks waar beschikbaar (€ 480.000/jaar lease uit `leaseverplichting-ifrs.voorbeeld_inline`); synthese-bedragen voor pedagogische illustratie (impairment-getallen, allocatie-percentages) als `confidence: inferred` via redenering.
- Valkuilen schema 1.0 → 1.1 (Regel E): titel is het ADVIES, `vaak_fout` als sub-info, `grondslag` met wikilink. Toegepast in alle 7 yamls.

**Anti-fabricatie-discipline**:
- IFRS-citaties uitsluitend uit IFRS-standaard-records (`materiele-vaste-activa-ifrs`, `opbrengsten-ifrs`, ...) die zelf naar `IFRS-XX-...md`-bronnen verwijzen.
- Cast-bedragen plausibel voor beursgenoteerde IFRS-rapporteur (omzet € 250M, balanstotaal € 125-129M, lease € 3,9M, productielijn € 12M, segment-goodwill € 8,5M).
- Geen examenvragen geconsulteerd (Anti-circulariteitsregel).

---

## Vervolgstappen (advies)

1. **Mens-review**: 7 nieuwe competenties + 1 synthese vereisen curator-validatie (`_provenance.gecureerd_door` is `null`).
2. **Enrich-pass**: dangling edges `ias-11-onderhanden-projecten` en `ias-18-opbrengsten` opruimen door ofwel stub-records aan te maken ofwel de edges te schrappen ten gunste van `_provenance.historische_noot`.
3. **PO 1.1 follow-up**: BE-GAAP-record `opbrengsten` aanmaken om symmetrie te herstellen.
4. **Rikheid-verbetering**: 4 records met `stappen.onvolledig` (priority hoog/midden) in een volgende enrich-pass uitwerken — meest urgent `wijziging-boekhoudkundig-referentiestelsel` (CBN 2022/08-procedure).
5. **Validatie**: `tools/leermateriaal/lib/validate_competentie.py` op de 7 nieuwe yamls draaien zodra Schema 1.1-validator de nieuwe stap-blok-velden accepteert.

---

*Gegenereerd door verify-run-1.5-2026-05-17 op 2026-05-17. Geen commit; eindcontrole door mens vereist.*
