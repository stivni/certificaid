# Patroon-labeling rapport — ITAA Bekwaamheidsexamen

**Tool**: `patroon-labeling-v1`
**Model**: Sonnet (claude-sonnet-4-6)
**Datum**: 2026-05-15 (initieel) · 2026-05-18 (refresh met BIBF-corpus)
**Corpus**: 2013-1 (37), 2013-2 (38), 2014-1 (46), 2015-1 (56), 2024-1 (11), 2003-bibf (28), 2008-bibf (37) → **253 vragen totaal**

---

## Resultaten

### Unieke vraagvormen: 11 (10 ITAA + 1 nieuw via BIBF-refresh)

| ID | Naam | Geschat n |
|---|---|---|
| `vraagvorm-mc-aankruisen` | Multiple Choice — één juist antwoord | 60 |
| `vraagvorm-jf-reeks-stellingen` | Juist/Fout — reeks stellingen | 65 |
| `vraagvorm-jf-met-motivering` | Juist/Fout — met motivering | 19 |
| `vraagvorm-mc-gemengd-meerdere-deelvragen` | MC-blok met meerdere deelvragen | 22 |
| `vraagvorm-open-definitie` | Open — definitie of begripsomschrijving | 38 |
| `vraagvorm-open-procedure-ontwerp` | Open — procedure ontwerpen | 18 |
| `vraagvorm-open-advies-casus` | Open — advies in casus | 29 |
| `vraagvorm-berekening-met-mc` | Berekening — cijfers berekenen | 36 |
| `vraagvorm-invultabel` | Invultabel — matrix of tabel invullen | 11 |
| `vraagvorm-open-berekening-motiveer` | Open — bereken én motiveer | 17 |
| `vraagvorm-open-boeking-journaalpost` *(NIEUW 2026-05-18)* | Open — boekingen (journaalposten) geven | 8 |

**Totaal geschat**: ~323 (meervoudig omdat sommige vragen meerdere vraagvormen combineren in deelvragen)

### Unieke complexiteitspatronen: 16 (15 ITAA + 1 nieuw via BIBF-refresh)

| ID | Naam | Camouflage |
|---|---|---|
| `complex-feiten-geen-camouflage` | Feitenvraag — rechtstreekse kennisreproductie | geen |
| `complex-feiten-red-herring` | Feitenvraag met red-herring | red-herring |
| `complex-feiten-schijngelijkenis` | Feitenvraag met schijngelijkenis | schijngelijkenis |
| `complex-toepassing-abstract` | Regeltoepassing op abstracte casus | geen |
| `complex-toepassing-verborgen-vereiste` | Regeltoepassing met verborgen vereiste | verborgen-vereiste |
| `complex-grensgeval-uitzondering` | Grensgeval-herkenning | verborgen-vereiste |
| `complex-procedure-rol-bevoegdheid` | Procedure, rol en bevoegdheid | geen |
| `complex-casus-multi-concept` | Uitgebreide casus — meerdere concepten | geen |
| `complex-vergelijk-twee-situaties` | Vergelijking twee (bijna-)gelijke situaties | schijngelijkenis |
| `complex-identifeer-de-fout` | Identificeer de fout | verborgen-vereiste |
| `complex-berekening-met-fiscale-keten` | Meerstapsberekening met fiscale keten | geen |
| `complex-stellingen-reeks-uitzondering` | Reeks stellingen — vind de uitzondering | schijngelijkenis |
| `complex-adviseer-en-onderbouw` | Adviseer en onderbouw | verborgen-vereiste |
| `complex-tabel-classificeer` | Classificeer in tabel | geen |
| `complex-grensgeval-red-herring-fiscaal` | Fiscale grensgeval-vraag met misleidende details | red-herring |
| `complex-boekhoudkundige-verwerking-meerstap` *(NIEUW 2026-05-18)* | Boekhoudkundige verwerking — meerstaps journaalposten met fiscale interactie | geen |

---

## Distributie per examen

### Vraagvormen per examen

| Examen | MC-aankruisen | J/F-reeks | J/F-motivering | MC-blok | Open-def | Open-proc | Open-advies | Berekening | Invultabel | Berek+motiv |
|---|---|---|---|---|---|---|---|---|---|---|
| 2013-1 | 10 | 14 | 2 | — | 7 | 2 | 5 | 4 | — | 3 |
| 2013-2 | 9 | 10 | 2 | — | 5 | 1 | 4 | 7 | 2 | 3 |
| 2014-1 | 4 | 20 | 1 | — | 6 | 2 | 8 | 3 | 1 | 5 |
| 2015-1 | 17 | 29 | 2 | — | 1 | 2 | 2 | 2 | 1 | 3 |
| 2024-1 | — | 3 | — | 8 | — | — | — | — | — | — |

**Trend**: De corpus evolueert van gemengde vraagvormen (2013) naar overwegend J/F-stellingen (2015) naar het compacte MC-blok format (2024). 2015 is het pioniersexamen van "volledig MC" met antwoordrooster.

### Complexiteitspatronen per examen (top 3)

| Examen | #1 | #2 | #3 |
|---|---|---|---|
| 2013-1 | feiten-geen-camouflage | casus-multi-concept | procedure-rol-bevoegdheid |
| 2013-2 | feiten-geen-camouflage | stellingen-reeks-uitzondering | vergelijk-twee-situaties |
| 2014-1 | stellingen-reeks-uitzondering | casus-multi-concept | toepassing-verborgen-vereiste |
| 2015-1 | feiten-geen-camouflage | stellingen-reeks-uitzondering | toepassing-verborgen-vereiste |
| 2024-1 | casus-multi-concept | vergelijk-twee-situaties | berekening-fiscale-keten |

---

## 5 opvallende patronen in het corpus

### 1. De recurrente vraag — identieke thema's elk jaar

De volgende vragen komen in vrijwel elk examen voor in bijna identieke formulering:
- **Ratio-analyse** (brutoverkoopmarge, NBK, liquiditeit): 2013-1, 2013-2, 2014-1, 2015-1, 2024-1
- **Begrippen-definitie** (intrinsieke waarde, fractiewaarde, operationele CF): 2013-1 én 2015-1 letterlijk identiek
- **Maximale afwijkingsdatum consolidatie** (3 maanden): 2013-1, 2014-1
- **Consolidatieverschil — definitie + 4 oorzaken**: 2013-2, 2015-1

→ **Implicatie**: deze kernconcepten zijn verankerd in het examenprogramma. Concept-records voor deze thema's zijn hoge prioriteit.

### 2. De "1 stelling onjuist" patroon in PB (PO 2.1)

Bij PO 2.1 (Personenbelasting) verschijnt elk jaar een reeks van 4-8 stellingen waarbij telkens precies 1 stelling fout is per deelthema. Het complexiteitspatroon is `stellingen-reeks-uitzondering`. De student moet het onjuiste element detecteren — niet alle stellingen als geheel beoordelen. Dit vereist:
- Precies kennen van de grenzen (niet de hoofdregel)
- Niet afleiden uit het merendeel (de andere stellingen zijn correct)

→ **Implicatie**: concept-records voor 2.1 moeten de uitzonderingen expliciet vermelden, niet alleen de hoofdregel.

### 3. De verborgen-vereiste in procedurele vragen (IC, 3.2)

Bij IC-vragen (functiescheiding, bevestigingsprocedure) en bijzondere mandaten (omzetting, ontbinding) zit de moeilijkheid niet in het kennen van de regel maar in het signaleren van een vereiste die niet expliciet gevraagd wordt:
- Bevestigingsbrief: student weet dat je verzendt maar niet DAT de accountant zelf de envelop dichtmaakt (niet de klant)
- Omzetting: student kent de procedure maar vergeet dat het werkdossier door de RvB getekend moet zijn

→ **Implicatie**: voor procedurele concepten moeten concept-records de "verborgen-vereiste" stappen expliciet labelen.

### 4. Het MC-blok-format van 2024: grotere dekkingsbreedte, kleinere diepte per deelthema

Het 2024-examen heeft 11 vragen maar elk vraagnummer bundelt 4-5 deelvragen. Dit verklaart de hogere thema-dekking per vraag. De cognitieve eis per deelthema is lager (MC ipv open motivering) maar de breedte is groot. Student moet meer gebieden kennen maar kan minder diepgaand aantonen. Dit is een formatwijziging die impact heeft op de studieaanpak.

→ **Implicatie**: voor 2024-voorbereiding is breedte (veel thema's correct kunnen identificeren) even belangrijk als diepte.

### 5. De fiscale-keten-vragen als differentiator

Vragen met een meerstaps fiscale berekening (VennB-grondslag, meerwaarden bij fusie, stopzettingsmeerwaarden) scoren hoog bij goede studenten en laag bij gemiddelde studenten. Ze vereisen:
1. Correct categoriseren van de situatie
2. Juiste formule kennen
3. Keten correct doorrekenen (fout in stap 1 kaskadeert)

De M-D fusievraag uit 2024 (Netto actief 100, fiscale waarde participatie 20, verliezen 30, innovatie-aftrek 40) is een typisch voorbeeld: student moet de meerwaarde berekenen (80) en dan de fiscale behandeling kennen.

→ **Implicatie**: concept-records voor fiscale berekeningen moeten stappenplannen bevatten, niet alleen regels.

---

## Suggesties voor schema-uitbreiding concept-records

Op basis van de geobserveerde examenpatronen blijkt het examen structureel de volgende kennislagen te verwachten — die nog niet als veld in het concept-schema zitten:

### 1. `drempelwaarden` — expliciete lijst van kritieke getallen

Examenvragen draaien regelmatig om drempels (nettoactief alarmbelprocedure, BTW-vrijstellingsdrempel, contantengrens, n-dagenkrediet). Een concept-record voor bv. `alarmbelprocedure` zou een veld `drempelwaarden: [{bedrag: "helft gestort kapitaal", context: "netto-actief < 50% gestort kapitaal"}]` nodig hebben.

### 2. `tijdlijn` — kritieke termijnen en datums

Procedures hebben wettelijke termijnen die exact gevraagd worden:
- AV bijeenroepen binnen 2 maanden na vaststelling (alarmbelprocedure)
- Antwoord vraag om inlichtingen: 1 maand (30 dagen)
- Consolidatie-afwijking: max. 3 maanden

Veld `tijdlijn: [{stap: "vaststelling negatief netto-actief", termijn: "2 maanden", actor: "bestuursorgaan", actie: "bijeenroeping AV"}]` zou dit structureren.

### 3. `verborgen_vereiste` — vereisten die niet in de vraag staan maar wel nodig zijn

Een veld `verborgen_vereiste: ["accountant verstuurt bevestigingsbrief zelf, niet via klant"]` per concept zou direct het examenpatroon spiegelen en de studierichting aanduiden.

### 4. `vergelijkingsparen` — concepten die verward worden

Elk concept dat in een schijngelijkenis-vraag verschijnt, zou een veld `vergelijkingsparen: ["liquiditeit_enge_zin vs. liquiditeit_ruime_zin: verschil = voorraden"]` kunnen hebben. Dit maakt patroon-matching in retrieval mogelijk.

### 5. `pos_gewicht` — welke POs bevragen dit concept het meest

Een veld dat aangeeft hoe zwaar een concept in het examen weegt (PO + geschat puntengewicht per examen), zodat retrieval kan prioriteren op examens-relevantie.

---

## Bestanden aangemaakt

| Bestand | Inhoud |
|---|---|
| `data/exam_patterns/vraagvormen.json` | 10 geconsolideerde vraagvormen |
| `data/exam_patterns/complexiteitspatronen.json` | 15 geconsolideerde complexiteitspatronen |
| `data/examen_vragen/2013-1-labels.json` | 37 vraag-labels |
| `data/examen_vragen/2013-2-labels.json` | 38 vraag-labels |
| `data/examen_vragen/2014-1-labels.json` | 46 vraag-labels |
| `data/examen_vragen/2015-1-labels.json` | 56 vraag-labels |
| `data/examen_vragen/2024-1-labels.json` | 11 vraag-labels |
| `data/exam_patterns/_labeling-rapport.md` | Dit rapport |

**Totaal gelabeld**: 188 vragen (initieel) · 253 vragen (na BIBF-refresh 2026-05-18)

---

## Refresh-log

### 2026-05-18 — BIBF-corpus toegevoegd (2003-bibf + 2008-bibf)

**Aanleiding**: TODO.md §3.4b — examenpatroon-bibliotheken dekten 5/7 voorbeeldexamens. De twee BIBF-examens (2003 en 2008) waren nog niet doorgelabeld.

**Werkwijze**: Sonnet-agent (subagent in Claude Code, geen API-call) heeft de 28 + 37 = 65 BIBF-vragen één voor één gelezen en gelabeld op vraagvorm + complexiteitspatroon, gebruikmakend van het bestaande schema (15 complexiteitspatronen + 10 vraagvormen). Vorige labelscript `tools/examen/extract_exam_patterns.py` is verwijderd (stale path + schond CLAUDE.md regel 3); refresh gebeurt sindsdien als eenmalige subagent-pass per refresh-event.

**Wijzigingen**:

- **Provenance**: `corpus` uitgebreid met `2003-bibf.json` + `2008-bibf.json`, `n_vragen_corpus` 188 → 253, `versie` 20260515.1 → 20260518.1, `model` `sonnet` → `sonnet-4-6`.
- **Nieuwe vraagvorm**: `vraagvorm-open-boeking-journaalpost` (8 voorkomens). Gebruikt voor vragen die expliciet journaalposten/afsluitingsboekingen vragen — typisch BIBF Vak A (Algemene boekhouding) maar het format komt ook in PO 1.x naar voor (boekhoudkundige verwerking als examen-output).
- **Nieuw complexiteitspatroon**: `complex-boekhoudkundige-verwerking-meerstap` (9 BIBF-voorbeelden). Boekhoudkundige verwerking waarbij de boekingsregel interageert met fiscaal-/waarderingsregels (kapitaalsubsidie + uitgestelde belasting, voorraadwijzigingen, oprichtingskosten + afschrijvingsritme). Analogon van `complex-berekening-met-fiscale-keten` maar op boekhoudkundig niveau.
- **`geschat_n_voorkomens` aangepast** voor: mc-aankruisen 55→60, jf-reeks 62→65, jf-met-motivering 18→19, open-definitie 20→38, open-procedure 12→18, open-advies-casus 15→29, berekening-met-mc 28→36, invultabel 10→11, open-berekening-motiveer 16→17.
- **65 BIBF-vraag-IDs** toegevoegd aan `voorbeelden_uit_corpus` / `voorbeelden` van de relevante patronen. Buiten-programma vragen (2003-vrI1, 2003-vrJ1, 2003-vrJ2, 2008-vrJ1 — vermeld in `_programmaonderdeel_classificatie.json` zonder PO-mapping) zijn **wel** mee gelabeld op vraagvorm/complexiteit (style is representatief); de PO-filter komt later in de consumer.

**Opvallende observaties BIBF vs ITAA**:

1. **Boekingsvragen zijn een eigen BIBF-genre**: BIBF Vak A (Algemene boekhouding) heeft consequent 2-6 vragen die expliciet journaalposten vragen. ITAA-examens (2013-2024) hebben dit format **niet** als zodanig — boekhoudkundige kennis komt daar via tabel-classificeer of MC-aankruisen. Implicatie: PO 1.5 (boekhoudkundig kader) zou journaalpost-vraag als examenformat kunnen herintroduceren, of niet — maar concept-records voor 1.x kunnen niet enkel op MC mikken.
2. **Lange casus-vragen met deontologische sub-vraagjes**: BIBF Vak K bevat veel meer narratieve casussen met meerdere deelvragen (typisch K-vragen 2008: K1-K5 zijn allemaal lange verhalen met 2-4 deelvragen elk). ITAA-examens hebben deze laag minder uitgesproken — daar zit deontologie vaak in J/F-stellingen. Het BIBF-format heeft hier hogere cognitieve eis (synthese-niveau).
3. **Geen MC-blok-format in BIBF**: Het `vraagvorm-mc-gemengd-meerdere-deelvragen` format (uit 2024-1) ontbreekt in beide BIBF-examens — die hebben aparte vraagnummers per topic. Trend richting compactere MC-blokken is een ITAA-evolutie.
4. **BIBF telt meer "feiten-geen-camouflage" vragen**: 13 van 65 BIBF-vragen zijn rechtstreekse kennisreproductie zonder camouflage, vs. ~5/188 in de ITAA-corpus per examen. BIBF-examens leunen meer op kennis-reproductie, ITAA op kennis-toepassing en analyse.
5. **Boekhoudkundige meerstapsverwerking is een eigen complexiteitsklasse**: Het patroon "boek de afsluitingsboekingen voor verrichtingen die zowel boekhoudkundig als fiscaal/waardrings-effect hebben" (kapitaalsubsidies + uitgestelde belastingen, voorraadwijziging + waardevermindering) is in de huidige ITAA-corpus niet aanwezig maar dekt 9 BIBF-vragen — verdient een eigen patroon (toegevoegd).

**Aangepaste bestanden**:

- `data/programma/exam_patterns/complexiteitspatronen.json`
- `data/programma/exam_patterns/vraagvormen.json`
- `data/programma/exam_patterns/_labeling-rapport.md` (dit bestand)

**Niet aangepast** (out of scope refresh): per-examen-labelfiles `data/programma/examen_vragen/{examen-id}-labels.json` voor de BIBF-examens — die zijn er nog niet, en zullen later in een eigen pass per vraag opgebouwd worden zodra de consumer ze nodig heeft.
