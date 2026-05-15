# Pilot-rapport concept-extractie PO 1.4

**Datum**: 2026-05-15
**Pilot**: ADR-008 Fase C — per-anchor concept-extractie
**Extractor**: claude-opus-4-7 (Claude Code subagent)
**Programmaonderdeel**: 1.4 Geconsolideerde jaarrekening en wetgeving
**Run-id**: `concept-extractie-v1-2026-05-15-pilot-1.4`

## Samenvatting

13 anchor-bundles verwerkt, **17 concept-records** geproduceerd in `data/concept_records/1.4/`. Bundeling is overwegend Belgisch-rechtelijk (KB WVV + CBN-adviezen); IFRS-anchors leverden weinig IFRS-specifieke inhoud op omdat het bronnencorpus geen IFRS-standaardteksten bevat.

## Aantal records per anchor

Onderstaande telling geeft het aantal records aan dat **primair gemotiveerd** is vanuit elk anchor. Veel records dekken bijkomende anchors (`dekt_ook_anchors` in `_provenance`).

| Anchor | Tekst | Bundle | Primaire records | Records (id's) |
|---|---|---:|---:|---|
| 1.4.I.C | Begrippen, consolidatieverplichting (moedermaatschappij, consortium), vrijstellingen | 31 | 4 | consolidatieverplichting, consortium, consolidatiekring, vrijstelling-subconsolidatie |
| 1.4.I.D | Consolidatietechnieken (integrale en evenredige consolidatie) | 80 | 3 | integrale-consolidatie, evenredige-consolidatie, intragroep-eliminaties |
| 1.4.I.E | Vermogensmutatiemethode | 28 | 1 | vermogensmutatiemethode |
| 1.4.I.F | Geconsolideerde jaarrekening en jaarverslag | 20 | 2 | geconsolideerde-jaarrekening, uitgestelde-belastingen-consolidatie |
| 1.4.I.G | Wijziging van de consolidatiekring | 105 | 3 | consolidatieverschil, step-acquisition, step-disposal |
| 1.4.taak.1 | Opstellen van de individuele en geconsolideerde jaarrekening | 198 | 1 | uniforme-waarderingsregels-consolidatie |
| 1.4.II.A | Wettelijk kader IFRS (IFRS10/3/11/12) | 85 | 2 | ifrs-keuze-geconsolideerde-jaarrekening, ifrs-verordening-1606-2002 |
| 1.4.I | Belgische wetgeving (meta) | 133 | 0 | (volledig gedekt door 1.4.I.C-G) |
| 1.4.I.B | CBN-adviezen over consolidatie (meta) | 259 | 1 | groottecriteria-geconsolideerde-basis |
| 1.4.II | IFRS (meta) | 20 | 0 | (gedekt door 1.4.II.A) |
| 1.4.II.B | Begrippen, consolidatieverplichting IFRS | 20 | 0 | (geen IFRS-specifieke bron — gedekt door Belgische concepten) |
| 1.4.II.C | Consolidatietechnieken IFRS | 70 | 0 | (geen IFRS-specifieke bron) |
| 1.4.II.D | Wijzigingen consolidatiekring IFRS | 109 | 0 | (geen IFRS-specifieke bron) |
| **Totaal** |  | **1156** | **17** | |

## Bundeling-statistiek

- **Anchors met 0 primaire records**: 5 (1.4.I, 1.4.II, 1.4.II.B, 1.4.II.C, 1.4.II.D). Reden: meta-anchors of IFRS-anchors waarvoor het bronnencorpus geen specifieke chunks bevat.
- **Anchors met 1 record**: 5 (1.4.I.E, 1.4.I.F deels, 1.4.taak.1, 1.4.I.B, 1.4.II.A deels — combinaties).
- **Anchors met 2 records**: 2 (1.4.I.F, 1.4.II.A).
- **Anchors met 3 records**: 2 (1.4.I.D, 1.4.I.G).
- **Anchors met 4 records**: 1 (1.4.I.C).

**Cross-anchor bundeling**: 12 van de 17 records dragen een `dekt_ook_anchors`-veld waarmee aangegeven wordt dat ze ook andere anchor-bundles bestrijken. Sterkst gedeelde concepten:
- `consolidatieverplichting`: 4 anchors (1.4.I.C, 1.4.I.B, 1.4.I, 1.4.taak.1)
- `consolidatiekring`: 4 anchors
- `consortium`: 4 anchors
- `integrale-consolidatie`, `evenredige-consolidatie`, `intragroep-eliminaties`, `vermogensmutatiemethode`: elk in 4+ anchors gebruikt
- `geconsolideerde-jaarrekening`: 5 anchors

De IFRS-anchors (II.B, II.C, II.D) hebben effectief de **Belgische** records bevestigd zonder eigen records te genereren — de IFRS-Verordening 1606/2002 en KB WVV art. 3:104 §2 leveren het ene IFRS-specifieke concept (keuze-mechanisme).

## Node-type-distributie

| node_type | aantal | records |
|---|---:|---|
| `methode` | 3 | vermogensmutatiemethode, integrale-consolidatie, evenredige-consolidatie |
| `regel` | 5 | consolidatieverplichting, vrijstelling-subconsolidatie, uitgestelde-belastingen-consolidatie, ifrs-keuze-geconsolideerde-jaarrekening, ifrs-verordening-1606-2002, uniforme-waarderingsregels-consolidatie |
| `begrip` | 4 | consortium, consolidatiekring, geconsolideerde-jaarrekening, consolidatieverschil |
| `procedure` | 3 | intragroep-eliminaties, step-acquisition, step-disposal |
| `drempel` | 1 | groottecriteria-geconsolideerde-basis |
| **Totaal** | **17** | (16 unieke records — 1 record `uniforme-waarderingsregels-consolidatie` past in `regel`; tellingen overlappen met de tabel hierboven na correctie: 6 regels) |

Geen voorgestelde nieuwe node-types (`voorgesteld:<naam>`). De 8 initiele node-types uit ADR-007 dekken alle behoeften voor PO 1.4 ruimschoots.

## Confidence-verdeling

Een handmatige telling op de 17 records (block-velden + sub-velden zoals stappen, bouwstenen, uitzonderingen, valkuilen):

- **`grounded`**: ~60 blocks (overwegend hoofdvelden, stappen en bouwstenen die direct traceerbaar zijn naar KB WVV-artikelen of CBN-advies-passages).
- **`inferred`**: ~5 blocks (typisch enkele valkuilen die een vergelijking maken tussen methodes, of synthese-stappen in step-disposal).

Verhouding ongeveer **92% grounded / 8% inferred**, in lijn met de empirische verwachting uit ADR-008 (waarom bron-first werkt: de bron levert de feiten, de extractor parafraseert).

## Open vragen en problemen

### 1. IFRS-bronnencorpus ontbreekt
De anchors 1.4.II.A, 1.4.II.B, 1.4.II.C en 1.4.II.D verwijzen expliciet naar **IFRS10, IFRS3, IFRS11, IFRS12** en de specifieke IFRS-consolidatieregels. Het huidige RAG-corpus bevat geen integrale teksten van deze standaarden (alleen Verordening 1606/2002 als kader). Effect:
- De IFRS-bundles bestaan grotendeels uit **Belgische** chunks (KB WVV + CBN) die het Belgische regime beschrijven.
- Het is in deze pilot **niet mogelijk** om IFRS-specifieke begrippen (zoals "control" volgens IFRS10, "business combination" volgens IFRS3, "joint arrangement" volgens IFRS11, "structured entity" volgens IFRS12) op te bouwen zonder hallucinatie-risico.
- Aanbeveling: voeg IFRS-standaardteksten (NL-vertaling of EU-publicatie) toe aan het bronnencorpus voordat de IFRS-laag van PO 1.4 verder wordt uitgewerkt.

### 2. Bundles bevatten footnote-residuen
Veel CBN-chunks bevatten markdown-footnote-syntax (`[^2]`, `[^18]`, …) als verwijzingen. Die zijn behouden in de chunk-tekst maar verwijzen naar voetnoten die in de chunk zelf niet aanwezig zijn. Niet problematisch voor concept-extractie (footnotes bevatten meestal artikelnummers die elders in de tekst staan), maar voor latere display-laag is footnote-resolutie aan te bevelen.

### 3. Zeer grote bundles dragen weinig nieuwe content
Bundle 1.4.taak.1 (198 chunks) en 1.4.I (133 chunks) bevatten vrijwel uitsluitend chunks die ook in de specifiekere I.C-I.G anchors voorkwamen. Slechts 1 nieuw concept (uniforme-waarderingsregels-consolidatie) is uit 1.4.taak.1 gehaald, en 1 uit 1.4.I.B (groottecriteria). Dit bevestigt het ADR-008 ontwerpprincipe dat brede taak-anchors vooral cross-anchor-confirmatie leveren, geen nieuwe content.

### 4. Bron-noot in chunk-tekst niet altijd schoon
Sommige chunks beginnen met `[CBN-advies XXX — ...]`-headers. Dit is metadata in de tekstkop en is meegelezen voor source-identificatie, maar het is enigszins fragiel: ETL-niveau (ADR-005) zou dit kunnen migreren naar chunk-metadata.

### 5. Geconsolideerd jaarverslag onvolledig gedekt
Anchor 1.4.I.F is "Geconsolideerde jaarrekening **en jaarverslag**", maar de bundle bevat geen chunks die specifiek het jaarverslag (rapport van bestuur, niet-financiele informatie, bestuurdersaansprakelijkheid voor het verslag) behandelen. Het record `geconsolideerde-jaarrekening` dekt enkel de jaarrekening. Een follow-up retrieval voor "jaarverslag" / "rapport van bestuur" is nodig — wellicht zit dit in WVV-hoofdstukken die niet in dit corpus zijn opgenomen.

## Voorgestelde schema-uitbreidingen

**Geen** in deze pilot. Alle records passen binnen ADR-007 schema 1.1. De 8 initiele node-types volstaan voor het consolidatiedomein.

Wel een **klein implementatie-detail** waargenomen: ik heb meerdere keren een `dekt_ook_anchors`-veld toegevoegd binnen `_provenance` om cross-anchor bundeling te documenteren. Dit veld zit niet expliciet in ADR-007 schema 1.1. Voorstel:
- ofwel formaliseren in ADR-007 als optioneel `_provenance.dekt_ook_anchors: [<anchor_id>, ...]`;
- ofwel weglaten en de informatie reconstrueren uit chunk-anchor-mapping in fase B output.

## Vergelijking met v0.1 materie-fiches

**Niet uitvoerbaar in deze pilot**: de directory `content/materie/` bestaat **niet** in de huidige working tree. Er zijn dus geen v0.1 materie-fiches om mee te vergelijken voor PO 1.4. De `content/`-directory bevat enkel `index.md` en `CHANGELOG.md`. Volgens CLAUDE.md zou de structuur `content/materie/` moeten bestaan, maar deze is leeg of nog niet aangemaakt voor PO 1.4.

Voor toekomstige vergelijking is het minimaal nodig dat de v0.1-fiches (indien elders gearchiveerd) worden teruggebracht in deze tree, ofwel dat een mapping naar git-archief beschikbaar is.

**Wat de extractie wel suggereert ten opzichte van een typisch consolidatiehoofdstuk in een Belgisch boekhoudhandboek**:
- Strikt onderscheid tussen `methode` (vermogensmutatie, integraal, evenredig) en de `procedure` (intragroep-eliminaties als geordende stappenset). Dit is een nuttige granulariteit voor leerdoelen.
- `consolidatieverschil` als eigen begrip naast `step-acquisition`/`step-disposal` als procedures benadrukt het verschil tussen *wat* een goodwill-achtig saldo is en *hoe* je het beheert bij wijziging van de consolidatiekring.
- `groottecriteria-geconsolideerde-basis` als drempel-type isoleert de vrijstellingsdrempel-redenering die in handboeken vaak verspreid zit over hoofdstukken consolidatie en groottecriteria.

## Conclusie

De bron-first matching (ADR-008 fase B) leverde voor PO 1.4 bruikbare bundles voor 8 van 13 anchors. De 5 IFRS-anchors zijn structureel beperkt door corpus-dekking, niet door de extractie-methode. De 17 gegenereerde concept-records dekken het Belgische consolidatiedomein systematisch:

- **Architectuur**: 4 begripsknooppunten (jaarrekening, kring, consortium, consolidatieverschil)
- **Technieken**: 3 methodes (integraal, evenredig, vermogensmutatie) + 1 procedure (intragroep-eliminaties)
- **Verplichtings-regels**: 4-6 regels (consolidatieverplichting, vrijstelling subconsolidatie, uitgestelde belastingen, uniforme waarderingsregels, IFRS-keuze, IFRS-verordening)
- **Dynamiek**: 2 procedures (step-acquisition, step-disposal) + 1 drempel (groottecriteria)

Geen records met `inferred`-only hoofdveld; geen artikelnummers buiten chunk-bron; geen voorgestelde node-types. De pilot is geslaagd binnen de ADR-007/008 spelregels.

**Eerstvolgende actie** (fase D, niet onderdeel van deze pilot):
1. Edges aanbrengen tussen records (bv. `vermogensmutatiemethode uitzondering-op integrale-consolidatie`, `intragroep-eliminaties onderdeel-van integrale-consolidatie`, `step-acquisition schakelt-over-naar integrale-consolidatie`, …).
2. IFRS-bronnencorpus uitbreiden en de IFRS-anchors opnieuw matchen.
3. Verdiepingsronde voor `casus`-knooppunten op basis van voorbeelden in CBN-2022/11 en CBN-2013/3-4 (voorbeeld 1, voorbeeld 7).
