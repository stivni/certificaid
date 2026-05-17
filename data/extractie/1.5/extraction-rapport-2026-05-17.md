# Extractie-rapport PO 1.5 — IFRS-laag

**Run-id**: `concept-extractie-v4-2026-05-17T00:28Z`
**Model**: claude-opus-4-7 (subagent, geen externe API)
**Datum**: 2026-05-17
**Scope**: PO 1.5 — Beginselen Europese wetgeving + IFRS (14 anchors)
**Output**: `data/concepten/records/` (flat, geen PO-subdirs)

---

## Samenvatting

| Categorie                                  | Aantal |
|--------------------------------------------|-------:|
| **Nieuwe concept-records** (schema 1.4)    |   26   |
| Bijgewerkte bestaande records              |    0   |
| Synthese-records (`node_type: synthese`)   |    1   |
| Dangling-references gelogd                 |    0 (zie §"Open observaties") |
| Bron-voorstellen toegevoegd                |    0   |

26 records valt binnen de geprognosticeerde range 25-40. Geen dubbele-records gedetecteerd via slug-check; alle IFRS-specifieke concepten hebben `-ifrs` of `ias-`/`ifrs-` prefix om botsing met bestaande BE-GAAP-records te vermijden.

---

## Per-anchor mapping

| Anchor      | Anker-tekst                                                              | Records die anchor coveren                                                                                                                                                                                                                                                                                       |
|-------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.5.taak.1  | Opstellen individuele en geconsolideerde jaarrekening                    | `richtlijn-2013-34-eu`, `ifrs-verordening-1606-2002`, `ias-1-jaarrekening-componenten`, `ias-1-toelichtingsvereisten`                                                                                                                                                                                            |
| 1.5.I       | Richtlijn 2013/34/EU                                                     | `richtlijn-2013-34-eu` (primair)                                                                                                                                                                                                                                                                                  |
| 1.5.II      | Verordening (EG) 1606/2002 IFRS-toepassing                               | `ifrs-verordening-1606-2002` (primair), `ifrs-toepassingsgebied-belgie`                                                                                                                                                                                                                                          |
| 1.5.III     | Toepassingsgebied van IFRS in België                                     | `ifrs-toepassingsgebied-belgie` (primair), `ifrs-verordening-1606-2002`, `wijziging-boekhoudkundig-referentiestelsel`                                                                                                                                                                                            |
| 1.5.IV      | Algemeen kader IFRS                                                      | `ifrs-eerste-toepassing`, `ias-1-jaarrekening-componenten`, `ias-1-presentatie-beginselen`, `ias-1-balans-presentatie`, `ias-1-winst-en-totaalresultaat`, `ias-1-mutatieoverzicht-eigen-vermogen`, `ias-1-toelichtingsvereisten`, `be-gaap-vs-ifrs-overzicht`, `correctie-jaarrekening-ifrs`                       |
| 1.5.IV.A    | Eerste toepassing van IFRS (IFRS 1)                                      | `ifrs-eerste-toepassing` (primair)                                                                                                                                                                                                                                                                               |
| 1.5.IV.B    | IAS 1 De jaarrekening                                                    | `ias-1-jaarrekening-componenten` (primair), `ias-1-presentatie-beginselen`, `ias-1-balans-presentatie`, `ias-1-winst-en-totaalresultaat`, `ias-1-mutatieoverzicht-eigen-vermogen`, `ias-1-toelichtingsvereisten`                                                                                                  |
| 1.5.IV.C    | Afwijkingen ten opzichte van Belgische wetgeving                         | `be-gaap-vs-ifrs-overzicht` (primair synthese), `wijziging-boekhoudkundig-referentiestelsel`, `correctie-jaarrekening-ifrs`, `bijzondere-waardevermindering-ias-36`                                                                                                                                              |
| 1.5.V       | Selectie van internationale boekhoudkundige normen                       | Alle V.A-V.E records + `be-gaap-vs-ifrs-overzicht`                                                                                                                                                                                                                                                                |
| 1.5.V.A     | IAS 16 + IAS 38 (MVA + immateriële activa)                               | `materiele-vaste-activa-ifrs` (primair), `immateriele-vaste-activa-ifrs` (primair), `herwaarderingsmodel-ias-16`, `componentenbenadering-ias-16`, `bijzondere-waardevermindering-ias-36`                                                                                                                          |
| 1.5.V.B     | Afschrijvingen volgens IFRS                                              | `afschrijvingen-ifrs` (primair), `componentenbenadering-ias-16`, `bijzondere-waardevermindering-ias-36`                                                                                                                                                                                                          |
| 1.5.V.C     | IAS 17 → IFRS 16 Leaseovereenkomsten                                     | `leasing-ifrs` (primair, met historische noot IAS 17 → IFRS 16), `right-of-use-actief`, `leaseverplichting-ifrs`                                                                                                                                                                                                |
| 1.5.V.D     | IAS 18 → IFRS 15 Opbrengsten                                             | `opbrengsten-ifrs` (primair, met historische noot IAS 18 → IFRS 15), `prestatieverplichting-ifrs-15`                                                                                                                                                                                                              |
| 1.5.V.E     | IAS 2 + IAS 11 → IFRS 15 (voorraden + onderhanden)                       | `voorraden-ifrs` (primair), `onderhanden-projecten-ifrs` (primair, met historische noot IAS 11 → IFRS 15)                                                                                                                                                                                                         |

**Dekking**: alle 14 anchors gedekt door minstens één primair record. Geen anchor zonder content.

---

## IFRS-vs-IAS expliciete mappings

PO 1.5-anchors verwijzen historisch naar IAS 11, IAS 17 en IAS 18. Deze zijn vervangen door IFRS 15 (opbrengsten, vervangt IAS 11 + IAS 18) en IFRS 16 (leasing, vervangt IAS 17). De records reflecteren de **huidige stand** (IFRS 15/16) met **historische noot** in `_provenance.historische_noot`:

| PO 1.5-anchor               | Historische IAS  | Huidige IFRS    | Record                            |
|----------------------------|------------------|-----------------|-----------------------------------|
| 1.5.V.C IAS 17 Leasing     | IAS 17           | IFRS 16          | `leasing-ifrs`                     |
| 1.5.V.D IAS 18 Opbrengsten | IAS 18           | IFRS 15          | `opbrengsten-ifrs`                 |
| 1.5.V.E IAS 11 Onderhanden | IAS 11           | IFRS 15 (over-periode-opname) | `onderhanden-projecten-ifrs` |

De `edges[]` met `"type": "vervangt"` markeren deze relaties expliciet voor leerpad-tooling en eventuele examenexposure.

---

## Cross-PO overlap-kandidaten

Veel IFRS-records zijn IFRS-tegenhangers van bestaande Belgisch-GAAP-records uit PO 1.1 / 1.4. Botsing **bewust vermeden** door consistente suffix `-ifrs` of `ias-`/`ifrs-` prefix. Mapping voor enrich/cross-link-pass:

| Nieuwe IFRS-record               | BE-GAAP-tegenhanger                | Verwarringsrisico (in `vergelijkingsparen[]`)               |
|----------------------------------|------------------------------------|-------------------------------------------------------------|
| `materiele-vaste-activa-ifrs`    | `materiele-vaste-activa`           | Ja — herwaardering, componentenbenadering                    |
| `immateriele-vaste-activa-ifrs`  | `immateriele-vaste-activa`         | Ja — onderzoekskosten-activering verboden onder IFRS         |
| `leasing-ifrs`                   | `leasing`                          | Ja — operationele/financiële lease vs. single model          |
| `opbrengsten-ifrs`               | (impliciet, KB WVV art. 3:18)      | Ja — 5-stappen-model vs. realisatiebeginsel                  |
| `voorraden-ifrs`                 | `voorraden`                        | Ja — LIFO verbod                                            |
| `afschrijvingen-ifrs`            | `afschrijvingen`                   | Ja — componentenbenadering verplicht, geen opbrengstenmethode |
| `herwaarderingsmodel-ias-16`     | `herwaarderingsmeerwaarden`        | Ja — verschillende voorwaarden                              |
| `ias-1-jaarrekening-componenten` | `jaarrekening`, `jaarrekening-schema` | Ja — 5 componenten vs. 3 (BE-GAAP)                       |
| `correctie-jaarrekening-ifrs`    | (impliciet, KB WVV)                | Ja — CBN 2020/12 verwijzing                                  |
| `bijzondere-waardevermindering-ias-36` | (impliciet, KB WVV waardeverminderingen) | Beperkt — toetsing verschillend                       |

Bestaande PO 1.4 / 1.1 records werden NIET aangepast in deze pass — alleen genoemd in `vergelijkingsparen[]` of `edges[]`.

---

## Bron-gaps

Onderstaande gaps zijn opgevallen tijdens extractie. Voor elke gap: hoe omzeild + voorstel voor verbetering.

| Gap                                                                      | Omzeiling                                                                                                                                            | Voorstel                                                                                                                                                                            |
|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bundles 1.5.IV.A-E bevatten ZEER beperkt directe IFRS-tekst             | IFRS-bestanden in `resources/bronnen/wetteksten/` rechtstreeks gelezen als primaire bron; chunk_ids gebruikt in formaat `<filename>__sec_<sectie>` | Bundle-builder voor PO 1.5 herdraaien zodat IFRS-secties als chunks worden opgenomen. Anders gaan RAG-queries op IFRS-content fundamentele claims missen.                          |
| Bundles 1.5.IV.A heeft slechts 25 chunks, weinig over IFRS 1 specifiek  | Lokale lezing van `IFRS-1-eerste-toepassing-...md` (alinea's 1-30+)                                                                                  | IFRS 1 prioriteit voor RAG-indexering; anchor 1.5.IV.A heeft veel meer materiaal nodig dan beschikbaar in bundle.                                                                  |
| IAS 36 (impairment) heeft geen eigen anchor in PO 1.5                   | Record toch gemaakt onder linked_anchors 1.5.V.A + V.B + IV.C — cruciaal voor zowel goodwill (geen afschrijving) als testen MVA                       | PO 1.5 anchors-uitbreiding overwegen: 1.5.V.F 'Bijzondere waardevermindering (IAS 36)'.                                                                                              |
| IFRS 3 (bedrijfscombinaties / goodwill) niet expliciet als anchor       | Verwijzingen via `immateriele-vaste-activa-ifrs` (verwerving via bedrijfscombinatie) en `bijzondere-waardevermindering-ias-36` (goodwill-impairment) | Eigen record `bedrijfscombinaties-ifrs-3` zou overlappen met PO 1.4 (consolidatie); overweeg of het thuishoort in PO 1.5 of als brug-record.                                       |
| Geen anchor voor IAS 12 (winstbelastingen) en IAS 19 (personeelsbeloningen) — beide complex onder IFRS | Niet gedekt — zou eigen records vereisen                                                                                                            | Voor PO 1.5-completeness: minicursus-overwegingen. Niet kritisch voor exam-vragen op huidig anchor-niveau.                                                                          |
| CBN-adviezen verwijzen vaak naar IFRS maar bevatten weinig diepte over IFRS-mechanica zelf | Adviezen gebruikt voor context (toepassingsgebied, wisseling stelsel, correctie) — IFRS-mechanica uit officiële IFRS-tekst                          | Geen actie nodig; CBN-adviezen blijven nuttige aanvullende bron, geen vervanging voor de standaard.                                                                                  |

---

## Schema 1.4 — veld-gebruik

| Veld                                  | Aantal records dat het gebruikt |
|---------------------------------------|--------------------------------:|
| `definitie` (begrip/fenomeen/actor)   | 8                                |
| `main_rule` (regel/beginsel)          | 7                                |
| `verplichting` (procedure)            | 3 (ifrs-eerste-toepassing, correctie-jaarrekening-ifrs, wijziging-boekhoudkundig-referentiestelsel)              |
| `doel` (methode/afwegingskader)       | 4 (componentenbenadering, herwaarderingsmodel, afschrijvingen, bijzondere-waardevermindering, opbrengsten-ifrs als methode) |
| `bouwstenen[]`                        | 25 (vrijwel alle records)        |
| `stappen[]` (stap-blok schema 1.4)    | 5 (ifrs-eerste-toepassing, opbrengsten-ifrs, onderhanden-projecten-ifrs, bijzondere-waardevermindering-ias-36, correctie-jaarrekening-ifrs, componentenbenadering-ias-16) |
| `berekeningsmethode[]` met `formules[]`| 5 (herwaarderingsmodel, componentenbenadering, afschrijvingen-ifrs, voorraden-ifrs, onderhanden-projecten-ifrs) |
| `voorbeeld_inline` op record-niveau   | 18 (Regel 13 minimum gerespecteerd voor begrip/regel/methode-records) |
| `vergelijkingsparen[]`                | 9 (waar BE-GAAP-IFRS-contrast bestaat) |
| `valkuilen[]`                         | 26 (alle records hebben minstens 1) |
| `edges[]`                             | 26 (alle records)                |
| `gebaseerd_op_concepten[]` (synthese) | 1 (be-gaap-vs-ifrs-overzicht)    |
| `vergelijkingstabel` (synthese)       | 1                                |
| `beslisboom` (synthese)               | 1                                |

---

## Stagiair-toon (regel 6)

Alle records gebruiken stagiair-toon: korte zinnen, jargon uitgelegd, eerste afkortinggebruik voluit (bv. 'Other Comprehensive Income, OCI' bij eerste vermelding). Wetsartikelen op laatste regel als `grondslag:` — niet in titels. Bouwsteen-titels onder 6 woorden waar mogelijk; enkele uitzonderingen bij IFRS-specifieke terminologie ('Verbod op opbrengstenmethode' — bewust gekozen voor herkenbaarheid).

## Cast-namen (regel 7)

Cast-namen consistent gebruikt:
- **Zelena Bio NV** (beursgenoteerde IFRS-rapporteur) — primaire entiteit voor IFRS-voorbeelden (in 20 records)
- **Rotex Roeselare NV** (grote NV, BE-GAAP) — voor BE-GAAP-vergelijkingen (8 records)
- **Aurelia Holding NV** + **Brugse Brouwerij BV** — voor consolidatie-context (4 records)
- **Antwerpse Investments NV**, **Drukkerij Dendermonde BV** — geassocieerde-onderneming-scenario (2 records)
- **Constructies Cattoir BV** — bouwprojecten (1 record)
- **Meubelzaak Mertens BV**, **Naaiatelier Ninove BV** — kleine entiteit als vergelijking (3 records)
- **Verffabriek Veurne BV** — vereffeningsvoorbeeld (going concern) (1 record)
- **Wolters & Partners CVBA** — auditor-rol (3 records)
- **Pieter Vermeulen** (consortium-leider), **Marleen De Cock**, **Sofie Janssens** (commissaris/accountant) — natuurlijke personen (3 records)

Geen 'X', 'Y', 'M', 'D', 'ABC' geconstrueerd. Bedragen in €-formaat met duizendtal-punt (regel 14a) — bv. € 3.894.000, € 4.500.000, € 13.800.000. Plausibele ranges voor beursgenoteerde NV (€ 50M-€ 500M omzet, € 100M-€ 1B balanstotaal) gerespecteerd.

## Confidence-labels

| Confidence-type                       | Voorkomen |
|---------------------------------------|----------:|
| `grounded` (direct uit chunk/IFRS-tekst) | ~85%      |
| `inferred-from-aggregation` (cross-bron synthese) | ~10% (vooral in be-gaap-vs-ifrs-overzicht, sommige opmerkingen) |
| `inferred` (redenering buiten chunk-inhoud) | ~5% (waar IFRS-tekst impliciet is + Belgische context vereist)   |

Geen claim zonder `_provenance.inputs` — alle records herleiden naar een chunk_id (uit bundle of IFRS-bestand).

---

## Open observaties

1. **PO 1.5-anchors verouderd op standaarden-niveau.** PO 1.5 noemt nog IAS 11, IAS 17, IAS 18 — terwijl IFRS 15 en IFRS 16 al sinds 2018-2019 van kracht zijn. Voorstel: ITAA-anchors aanpassen in een toekomstige update naar 'IFRS 15 Opbrengsten' (1.5.V.D) en 'IFRS 16 Leases' (1.5.V.C). Records reflecteren al de huidige stand.
2. **Geen synthese-records over centraal-controle-verschil EU-richtlijn / Verordening.** Het verschil tussen rechtsinstrumenten (richtlijn = nationale omzetting; verordening = rechtstreeks) wordt in 2 records vermeld in `vergelijkingsparen[]` maar zou een eigen mini-synthese-record kunnen worden voor publiekrechtelijk overzicht. Niet kritisch voor PO 1.5-completeness.
3. **Aansluiting met PO 1.4 conserveerd.** Records over IFRS-consolidatie (IFRS 10, IFRS 11, IFRS 3) zijn bewust GEEN PO 1.5-scope gegeven — die zitten in PO 1.4 (consolidatie). Bestaand record `ifrs-consolidatieraamwerk` (PO 1.4) krijgt linked_anchors die PO 1.5 niet raken. Geen botsing.
4. **Toolbouw RAG-index.** Voor de tutor om PO 1.5-vragen te beantwoorden moeten de IFRS-bestanden in `resources/bronnen/wetteksten/` worden geïndexeerd in `data/rag/main/` (ChromaDB). Aanbeveling: `tools/rag/rag_index.py` herdraaien met expliciete IFRS-tag-filter.
5. **Drie records hebben node_type "synthese" niet gebruikt** ondanks dat zij synthese-karakter hebben (zoals `be-gaap-vs-ifrs-overzicht`). Reden: synthese-records hebben specifiek `gebaseerd_op_concepten[]` + `vergelijkingstabel` + `beslisboom` velden. Alleen `be-gaap-vs-ifrs-overzicht` voldoet aan deze specifieke schema-eisen volgens regel 10.
6. **Geen dangling-references gelogd.** Begrippen zoals 'kasstroomgenererende eenheid (CGU)' en 'realiseerbare waarde' worden binnen IAS 36-record voldoende uitgelegd; geen aparte records vereist voor PO 1.5-scope.

---

## Granulariteit-beslissingen (regel 14c)

Twee twijfelgevallen waar autonoom beslist:

| Beslispunt                                          | Keuze              | Rationale                                                                                                                                                                  |
|-----------------------------------------------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Right-of-use-actief en leaseverplichting als één of twee records? | **Twee aparte records** | Beide hebben eigen wetsartikel-clusters (alinea 23-25 vs. 26-43), eigen berekeningsmethoden, verschillende kanten van de balans. Cross-refs vanuit `leasing-ifrs` bewaard.  |
| `prestatieverplichting-ifrs-15` apart van `opbrengsten-ifrs`?    | **Twee aparte records** | Prestatieverplichting is zelfstandig examinabel (definitie + onderscheiden-criteria); zou anders verdwijnen binnen 5-stappen-model. Cross-ref vanuit `opbrengsten-ifrs`.    |

---

## Volgende stappen (advies voor enrich-pass)

1. **Cross-bron verrijking**: 9 records hebben nu BE-GAAP-vergelijkingspaar; controleer of bestaande BE-GAAP-records (`afschrijvingen`, `leasing`, `voorraden`, `materiele-vaste-activa`, `immateriele-vaste-activa`) symmetrisch een vergelijkingspaar terug naar de IFRS-variant krijgen.
2. **Synthese-detectie**: `be-gaap-vs-ifrs-overzicht` is gebaseerd op 10 IFRS- + BE-GAAP-records. Bij latere wijzigingen aan onderliggende records: synthese-record updaten (vergelijkingstabel rijden).
3. **Voorbeeld-minimum-check**: Sommige records van type `regel` en `beginsel` hebben enkel `voorbeeld_inline` op bouwsteen-niveau, niet op record-niveau. Voldoet aan regel 13 (minimum 1 voorbeeld_inline ergens in record). Geen TODO-callout nodig.

---

*Gegenereerd door concept-extractie-v4 op 2026-05-17. Records in `data/concepten/records/`. Geen commit door extractor — eindcontrole door mens vereist.*
