# ADR-030 — Granulariteit-typologie voor concept-records

**Status**: Draft (2026-05-23)
**Vervangt deels**: ADR-007 (conceptmodel — historische 10 `concept_type`-waarden) + ADR-029 §`concept_type`-enum
**Gerelateerd**: ADR-019 (records-API — atomair disk + RAG + content), ADR-005 (bronnen-ETL), ADR-006 (RAG-strategie)

**Voorgeschiedenis-tracker**: [`docs/granulariteit-typologie-draft.md`](../granulariteit-typologie-draft.md) — sparring-iteraties 1 t/m 5 (2026-05-23). Bevat stress-tests op 24 records, casussen (DBI/moeder-dochter, ondernemingsvormen, consolidatiekring), 1+1=1-matrix, en de verwerping van tussenvormen (synthese-records, lichte stub-Entiteiten als eigen records).

---

## Beslissing

Granulariteit van concept-records wordt bepaald door één hoofd-principe + 4 super-categorieën als oriëntatie + 9 werkingsregels (A-I).

**Hoofd-principe**: *1 concept-record = 1 conceptueel coherente eenheid = 1 studiefiche.*

**Toetsvraag bij elk record**: *"Vormt dit één conceptueel geheel zoals een domein-expert (boekhouder, fiscalist, auditor) het zou clusteren — een eenheid die in vakliteratuur, opleiding en praktijk samen wordt behandeld?"* Ja → één concept. Nee → splitsen.

Stagiair-leesbaarheid is een **gevolg** van conceptuele coherentie, geen primair criterium. Wat domein-experts als één samenhangend onderwerp zien, studeert een stagiair ook als één geheel.

---

## 4 super-categorieën (oriëntatie, geen rigide hokjes)

Deze categorieën **vervangen** de 10 `concept_type`-waarden uit ADR-029 (`instrument` · `verrichting` · `procedure` · `balanspost` · `ratio` · `regime` · `methode` · `kader` · `principe` · `actor`).

| Categorie | Heuristiek | Voorbeelden |
|---|---|---|
| **Kader** | Professionele aanpak, discipline of techniek. Tree: rol → sub-domein → techniek. Bevat *eigen* disciplinaire inhoud. | boekhouding · fiscaal/vennootschapsbelasting · audit/COSO · jaarrekening-opmaak · aangifte-vennootschapsbelasting-opmaken · consolidatie-techniek · juridische-vormkeuze-adviseren |
| **Entiteit** | Een ding met identiteit dat in transacties optreedt, ongeacht of de wetgever het ontwierp. | aandeel · leasing · vruchtgebruik · vordering · `ondernemingsvormen` (bundel) · `eigen-vermogen` (bundel) |
| **Gebeurtenis** | Transactie of event tussen Entiteiten — handeling op een moment, met deelnemers en gevolgen. | dividend-uitkering · kapitaalverhoging · fusie · faillissement |
| **Regeling** | Wettelijke regel die *gedrag corrigeert, stuurt, voorkomt of stimuleert*. Normatief van karakter. | dbi-aftrek · notionele-interestaftrek · alarmbel-procedure · liquidatiereserve · huwelijksquotiënt · groottecriterium |

**Belangrijke nuance** (iter. 5): de 4 categorieën zijn **oriëntatie** ("welke rol speelt dit primair?"), geen administratieve hokjes. Een concept-record mag categorieën mengen zolang het conceptueel een geheel vormt. `ondernemingsvormen` (Entiteit-bundel) draagt bv. ook een advies-perspectief met de keuze-matrix — wat in iter. 1-4 een "synthese-Kader-techniek" zou heten.

**Kern-heuristieken**:

| Onderscheid | Heuristiek |
|---|---|
| Kader vs anderen | Organisatorische koepel/aanpak/discipline? Geen "wat IS het ding", maar "binnen welk perspectief werk je?" |
| Entiteit vs Gebeurtenis | Identiteit in de tijd ("aandeel bestaat") → Entiteit. Op een moment met deelnemers/gevolgen ("dividend uitgekeerd") → Gebeurtenis. |
| Entiteit vs Regeling | *Ding* dat in transacties optreedt (zelfs wettelijk gecreëerd: BV, vruchtgebruik) → Entiteit. *Normatieve regel* die gedrag voorschrijft → Regeling. |
| Gebeurtenis vs Regeling | *Iets dat gebeurt* (kapitaalverhoging) → Gebeurtenis. *Regel die op zo'n gebeurtenis inwerkt* (quasi-inbreng-regeling) → Regeling. |

---

## Werkingsregels A-I

### Regel A — 1+1=1: combineer als 1-op-1 of coherent

Eén concept-record kan Entiteit + Gebeurtenis + Regeling combineren *zolang ze 1-op-1 of coherent samen optreden*. Splits zodra divergentie. (Volledige matrix in draft §2.)

Voorbeelden:
- **afschrijving** = 1 E (vast actief) + 1 G (jaarlijkse boeking) + 1 R (afschrijvingsregels) → 1 concept.
- **statutaire uittreding** = 1 G + 1 R → 1 concept.
- **leasing** = 1 E + 1 G + meerdere divergente R's (BEGAAP/IFRS/fiscaal/BTW) → hoofdrecord leasing + apart Regeling-record voor kwalificatie waar zinvol.

### Regel B — Regelingen kunnen op alles inwerken

Een Regeling werkt in op een Kader, Entiteit, Gebeurtenis of meerdere tegelijk. Het Regeling-record beschrijft het werkingsmechanisme, met `relaties[]` naar wat het beïnvloedt.

### Regel C — Kader-records: eigen inhoud + lichte verwijzingen naar Regelingen

Een Kader-record bevat eigen disciplinaire inhoud (wat is de techniek, hoe pas je ze toe), maar **geen volledige uitleg** van Regelingen die erin spelen — daar wijst het naar. Vermijdt content-duplicatie.

### Regel D — Aspect-secties per Kader in `inhoud.accountant_perspectieven[]`

Entiteit-, Gebeurtenis- en Kader-records dragen rol-specifieke uitwerking in `inhoud.accountant_perspectieven[]` (schema 2.1 v1.5) — niet in `inhoud.kern.definitie`. Definitie blijft generiek; perspectieven dragen het "hoe doe ik hier mee in mijn vak".

Geldt voor **alle** concept-records ongeacht primaire categorie.

### Regel E — Wat NIET een eigen record is

- Uitzonderingen/drempels/parameters binnen een Regeling → sub-velden van die Regeling.
- Rechtsbasis (wet, KB, richtlijn) → bron-anchor in `resources/bronnen/`.
- Lemma's en begrippen (EBITDA, ROCE) → gedefinieerd in het Kader-record waar ze leven.
- Document-sjablonen (aangifte-formulier) → sub-structuur binnen Kader-record dat de techniek beschrijft.
- Groepsnamen zonder eigen wettelijke inhoud ("aftrekken-en-verminderingen-PB") → géén Kader-record; werkt als filter/categorie.

### Regel F — Lichte Entiteiten zijn sub-secties met anchor, geen eigen records

Een Entiteit die op zichzelf geen volwaardige studiefiche kan dragen (BV, NV, voorraad, klant) wordt **geen eigen record**, maar **sub-sectie met anchor** binnen een bundel-concept of Kader-techniek-record.

**Toetsvraag**: "kan ik over deze Entiteit een zinvolle studiefiche schrijven die op zichzelf staat?" Nee → sub-sectie. Ja → eigen record.

### Regel G — Integratie-leerstof landt altijd in een bestaand bundel-concept

Integratie/afweging/keuze-narratieven leven als perspectief- of kern-sectie in een bestaand record:
- `inhoud.accountant_perspectieven[]` (typisch `advies` voor afwegingen, `fiscaal` voor aftrekvolgordes)
- `inhoud.kern` binnen een Kader-techniek-record (uit PO-taak, Regel §4 hieronder)

**Geen aparte "synthese-records"**. Als geen bundel-concept bestaat waar de integratie in past, betekent dat het bundel-concept zelf nog moet worden aangemaakt — niet als "synthese-record", maar als gewoon bundel.

### Regel H — Diepte per categorie (schrijfregel)

| Categorie | Diepte | Voorbeelden |
|---|---|---|
| Entiteit-bundel | Diep — secties per lid (anchors) + perspectieven met afweging | `ondernemingsvormen`, `eigen-vermogen` |
| Entiteit-solo | Middelmatig-diep — aspect-secties per rol | `aandeel`, `leasing` |
| Gebeurtenis | Middelmatig — wat gebeurt, deelnemers, perspectieven | `kapitaalverhoging`, `dividend-uitkering` |
| Regeling | Middelmatig-diep — mechanisme, voorwaarden, uitzonderingen, perspectieven | `dbi-aftrek`, `liquidatiereserve` |
| Kader-rol / Kader-domein | Licht — koepel, navigatie | `boekhouding`, `fiscaal` |
| Kader-techniek (uit PO-taak) | Diep — methodologie + perspectieven + integratie-secties | `consolidatie-techniek`, `aangifte-vennootschapsbelasting-opmaken` |

Élke fiche draagt een substantieel verhaal. Geen schamele stubs.

### Regel I — Bundel-criterium: wanneer wél en wanneer NIET bundelen

Bundel pas als één van twee patronen geldt:

| Patroon | Wanneer | Voorbeelden |
|---|---|---|
| **Keuze-bundel** | Stagiair moet TUSSEN leden kiezen — afweging is de leerstof | `ondernemingsvormen`, `consolidatie-methoden`, `afschrijvings-methoden`, `waarderingsmethoden-voorraad` |
| **Samenhang-bundel** | Leden onlosmakelijk verstrengeld — totaal moet kloppen, je hanteert ze samen | `eigen-vermogen`, `werkkapitaal` |

**NIET bundelen — losse mechanismes** met eigen toepasbaar mechanisme + aparte integratie-laag:
- DBI / NIA / innovatie-aftrek / investeringsaftrek / overgedragen-verliezen → elk eigen Regeling-record. Aftrekvolgorde + korf-systeem + interactie woont in Kader-techniek `aangifte-vennootschapsbelasting-opmaken`.
- PB-faciliteiten (pensioensparen, huwelijksquotiënt, decumul) → idem.

**NIET bundelen — filter-categorieën / overzichten** (anti-pattern): groepsnamen die enkel een fiscaal/boekhoudkundig *kenmerk* uitdrukken zijn geen bundel-concept met `#anchor`-leden. Ze landen als overzichts-sectie in het bovenliggend Kader of als overzichts-Regeling die naar de leden verwijst.
- `verworpen-uitgaven` → géén bundel met `#autokosten` · `#receptie` · `#geschenken`. Wel: overzichts-sectie in Kader `fiscaal/vennootschapsbelasting` die de fenomenen oplijst met hun verworpen-aspect; elk fenomeen is een eigen Regeling-record (zie Regel J).
- `voordelen-alle-aard` → idem.
- `aftrekken-en-verminderingen-PB` → idem (al expliciet onder Regel E).

**NIET bundelen — PO-anchor-cohort** (anti-pattern): wanneer een PO-anchor twee of meer fenomenen samenzet om didactische redenen (tegenhangers, vergelijkbare structuur), is dat een organisatorisch artefact, geen conceptueel geheel.
- `kapitaalverhoging` + `kapitaalvermindering` zitten in PO-anchor 2.3.III.A.iv samen omdat ze tegenhangers zijn → blijven 2 aparte records, elk eigen Gebeurtenis + Regeling-aspect. Niet één bundel met `#verhoging` / `#vermindering`-anchors.
- Toetsvraag: "Vertelt deze samen-clustering één conceptueel verhaal (Keuze of Samenhang), of is het slechts een PO-cohort / didactische tegenhanger?"

**Naamgeving-conventie**:
- **Voorkeur**: intrinsieke naam zonder generieke suffix (`eigen-vermogen`, `werkkapitaal`, `ondernemingsvormen`, `dbi-aftrek`). Domein-termen waar "aftrek"/"vrijstelling"/"regeling" deel zijn van de geijkte naam blijven intact — dat is geen categorie-suffix.
- **Toegelaten alternatief** (consistent als prefix): `balanspost-eigen-vermogen` · `balanspost-werkkapitaal` (mits alle leden van dezelfde categorie hetzelfde prefix dragen).
- **NIET**: suffix als categorie-marker (`eigen-vermogen-componenten`, `balansposten-werkkapitaal`, `reorganisatie-vennootschap-fiscaal`) — dubbel-benoemend, of dimensie-suffix (zie Regel J — dimensies leven als perspectieven binnen één record, niet als naam-achtervoegsel).
- Anchors dragen de specifieke naam: `eigen-vermogen#kapitaal`, `ondernemingsvormen#bv`.

### Regel J — Geïntegreerde Regeling: één fenomeen, alle dimensies in één record

Een Regeling clustert **alle dimensies** (fiscaal · BTW · boekhouding · juridisch · loonfiscaliteit · …) van één conceptueel fenomeen in **één record**. NIET splitsen per dimensie — die dimensies leven als `accountant_perspectieven[]` binnen het ene Regeling-record.

**Toetsvraag**: "Als een accountant met dit fenomeen in handen zit, hoeveel verschillende dingen moet hij erover weten?" Als die kennis vanuit één fenomeen vertrekt → één record, N perspectieven.

**Voorbeelden**:

| Fenomeen | Eén record `accountant_perspectieven[]` | NIET zo |
|---|---|---|
| `autokosten` | `boekhouding` (kost-boeking) · `fiscaal` (verworpen-uitgaven CO2-formule) · `btw` (aftrekpercentage, beroepsgebruik) · `loonfiscaliteit` (voordeel alle aard) · `advies` (bedrijfswagen vs cash-for-car) | `verworpen-uitgaven-autokosten` + `btw-autokosten` + `boeking-autokosten` + … |
| `geschenken-en-relatiegeschenken` | `boekhouding` · `fiscaal` (drempels, verworpen-uitgaven) · `btw` (aftrekgrens) | `verworpen-uitgaven-geschenken` + … |
| `bedrijfsrestaurant` / `restaurantkosten` | `boekhouding` · `fiscaal` (69%-regel) · `btw` (uitsluiting) | per dimensie splitsen |
| `dividend-uitkering` | `vennootschap` (uitkeringskader, beschikbare winst) · `aandeelhouder` (RV/PB-perspectief) · `boekhouding` · `juridisch` (uitkeringstest, alarmbel-link) | `dividend-RV` + `dividend-boeking` + `dividend-juridisch` |

**Implicatie voor "filter-categorieën"**: een groepering die enkel een dimensie-kenmerk uitdrukt (verworpen uitgaven, voordelen alle aard, niet-aftrekbare BTW) is geen bundel-concept. Ze leeft als overzichts-sectie in het bovenliggend Kader (`fiscaal/vennootschapsbelasting` → "verworpen uitgaven"-overzicht) en wijst naar de fenomeen-records.

**PO-bewoordingen mogen geen record-grenzen opleggen**. Als een PO `autokosten` enkel onder "verworpen uitgaven" noemt, betekent dat niet dat het record `verworpen-uitgaven-autokosten` heet — het record is gewoon `autokosten` met fiscaal-perspectief dat de verworpen-uitgaven-regel uitlegt.

---

## Schema-aanpassing — anchor-targets in relaties

`relaties[].target` mag een **anchor-suffix** dragen: `{record-id}#{anchor-id}`. Voorbeelden:
- `kapitaalverhoging` → `relaties[].target = "ondernemingsvormen#bv"`
- `alarmbel` → `relaties[].target = "ondernemingsvormen#bv"` en `"ondernemingsvormen#nv"`

Dit lost de fijnmazige link-behoefte op zonder aparte BV/NV-records te vereisen. Schema 2.1 v1.5 + records-API + render-laag krijgen een kleine update om anchor-targets te ondersteunen (deel van pilot-implementatie).

**Embeddings**: voor RAG-precisie mag een bundel-concept *intern gesplitst* worden in chunks per sectie (BV-chunk, NV-chunk, CommV-chunk, afweging-chunk). De record-eenheid (= fiche) blijft het bundel-concept als geheel.

---

## PO-taken → Kader-techniek-records

Bijna alle **taken** uit examenprogramma-onderdelen zijn van de vorm "kan X doen" — die vertalen quasi 1-op-1 naar **Kader-techniek-records** binnen de relevante rol. Een PO-taak-Kader-techniek kan tegelijk **het bundel-concept** zijn dat de bijhorende Entiteiten/Regelingen als secties draagt (Regel D + G).

PO-taken-canoniek in `data/programma/programma.json` (taken/doelstellingen/kenniselementen) + `data/programma/anchors.json` (uitbreiding — bevat vectors, vóór gebruik filteren).

---

## Bronnen-strategie voor Regeling-records

Naast wetteksten zijn twee bron-types **bijzonder waardevol** voor het stofferen van Regeling-records (regimes):

- **CBN-adviezen** (Commissie voor Boekhoudkundige Normen) — voor boekhoudkundige regimes/methoden: praktisch, gestructureerd, expliciet over toepassingsgebied en uitzonderingen. Vandaag in `resources/bronnen/adviezen/` (zie [`resources/bronnen/INDEX.md`](../../resources/bronnen/INDEX.md)).
- **Fiscale praktijkgidsen** — voor fiscale regimes (PB, VenB, BTW): integreren wettekst + administratieve commentaar + voorbeelden. Locatie: `resources/bronnen/wetteksten/` (deels aanwezig, uit te breiden).

Beide bron-types zijn primaire input voor de operatie `claims_checken` op Regeling-records (ADR-029). Bij twijfel over een regime-mechanisme: eerst CBN-advies of praktijkgids raadplegen, dan pas wettekst.

Concrete consequentie voor de pilot K-fiscaal/VenB: per Regeling-record (DBI, NIA, innovatie-aftrek, …) checken of een CBN-advies of praktijkgids als grondslag-bron kan dienen.

---

## Migratie-aanpak — top-down tree-afleiding per domein

**Niet** doen: bottom-up reclassificatie van 396 records onder 4 categorieën. **Wel** doen:

1. **Pilot per domein** — startend met K-fiscaal/VenB (PO 2.3 — 21 anchors in `data/programma/anchors.json`).
2. **Top-down**: vanuit PO-taken + ITAA-programma de logische tree schetsen (bundel-concepten + Kader-technieken + Regelingen + Entiteit-records).
3. **Mapping**: huidige VenB-records *afkruisen* tegen de tree — wat blijft / wat smelt in bundel / wat wordt sub-sectie / wat wordt aparte Regeling.
4. **Validatie per cluster** met user.
5. **Implementatie** via records-API (ADR-019 — atomair disk + RAG + content). Schema-aanpassing `#anchor`-relaties als eerste kleine PR.

Verwacht resultaat pilot: ~80 huidige VenB-records → ~25-35 records. Extrapolatie totale corpus: 396 → **~165-195 records** (reductie 50-60%).

---

## Wat dit ADR niet oplost

- **Grenzen blijven grijs in ~10% van de gevallen** (hybride events zoals `oprichting-vennootschap`, kwalificatie-perspectieven bij leasing). Regel A (1+1=1) en relaties[] dempen, elimineren niet.
- **Reductie ≠ halvering naar 100**. Realistisch eindbereik 165-195. Sterkere reductie zou conceptuele coherentie aantasten.
- **Naamgeving-consistentie over 396 bestaande records** is geen one-shot rename. Per pilot-domein wordt het meegenomen.
- **Render-laag-aanpassingen** voor `#anchor`-relaties en bundel-fiches komen apart aan bod (zie [`docs/render-laag.md`](../render-laag.md) en TODO Fase 7).

---

## Volgende stappen

1. **Pilot K-fiscaal/VenB** — top-down tree afleiden uit PO 2.3 (zie [granulariteit-typologie-draft §10](../granulariteit-typologie-draft.md) + filtered anchors-kopie op `/tmp/anchors-no-vectors.json`).
2. **Schema-aanpassing** — `relaties[].target` met `#anchor`-suffix in `data/concepten/schema-2.1.schema.json` + records-API + render-laag.
3. **Migratie pilot-domein** — voorgestelde tree-mapping uitvoeren via records-API, met user-validatie per cluster.
4. **Tweede pilot-domein** ter validatie (voorstel: K-boekhouding/jaarrekening-opmaak — testbed voor bundel-concepten zoals `eigen-vermogen`, `werkkapitaal`).
5. Indien tweede pilot bevestigt → uitrol over alle PO's. Indien niet → terug naar design-modus voor verfijning ADR-030.

---

## Verband met andere ADRs

- **ADR-007** (conceptmodel) — granulariteit-deel wordt door dit ADR herzien; de drie-lagen-redenering en ITAA-LEX-proxies blijven gelden.
- **ADR-019** (records-API) — implementatievehikel; anchor-targets vereisen kleine API-uitbreiding (`validate_relation_target` accepteert `#anchor`-suffix).
- **ADR-029** (schema 2.1 + operaties-model) — `concept_type`-enum wordt vervangen. Operaties (`beschrijven`, `claims_checken`, etc.) blijven onveranderd toepasbaar op de nieuwe categorieën.
- **ADR-005** (bronnen-ETL) — CBN-adviezen en praktijkgidsen blijven onder bestaande pipeline; geen nieuwe bron-types.
