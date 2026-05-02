# Certificaid

Kennisbank voor het ITAA bekwaamheidsexamen voor Gecertificeerd Accountant.

## Context

### Probleemstelling

ITAA levert voor het bekwaamheidsexamen geen cursusmateriaal. Wél een officieel programma met Taken, Doelstellingen en Kenniselementen (TDKs) per vak, een niveaubepaling per vak, en een opgave van wat de student bij het examen bij heeft. Dit project destilleert uit dat programma — aangevuld met wetteksten, normen, voorbeeldexamens en indien nodig AI-redenering — het studiemateriaal dat ontbreekt.

### Doelpubliek

De conceptfiches zijn studiemateriaal voor mensen Stagiairs Gecertificeerd Accountant. Of gelijkgestelden door ervaring.  
Die kennen al iets van de boekhoudkundige en fiscale wereld (bv. via opleiding of praktijk), maar ze zijn geen juristen.

### Info over het examen

Tijdens het bekwaamheidsexamen mag de student gebruiken:
- **ITAA-LEX** — de volledige wettekstenbundel (genummerde secties, paginanummers)
- **Cijferzakboekje** — geactualiseerde/geïndexeerde bedragen, tarieven en drempelwaarden

**Gevolg voor de fiches**: exacte bedragen en tarieven hoeven niet uit het hoofd gekend te zijn — de student kan ze opzoeken. Wat wél getoetst wordt en dus centraal staat in onze fiches:
- Het **concept** begrijpen: wanneer is iets van toepassing, waarom, op wie?
- **Weten waar** je iets terugvindt in ITAA-LEX (sectie + onderwerp)
- **Randgevallen en uitzonderingen** herkennen — die staan minder prominent en worden specifiek bevraagd
- **Conceptuele valkuilen**: niet "verkeerd bedrag", maar "verkeerde redenering" — bv. denken dat een omweg via het postkantoor de contantengrens omzeilt

Valkuilen in de fiches gaan dus over **verkeerde concepten**, niet over verkeerde cijfers.

### Niveaubepalingen

| Niveau | Wat de student kan | Typische examenvraag |
|--------|-------------------|----------------------|
| **weten-en-inzien** | Het concept benoemen en uitleggen: definitie, toepassingsgebied, waarom het bestaat | "Wat is X?" / "Welke stelling over X is juist?" |
| **toepassen** | Het concept correct gebruiken in een concrete situatie: berekening, boeking, procedure uitvoeren | "Bereken X" / "Hoe boek je Y?" / "Welke stappen volg je?" |
| **integratie** | Meerdere concepten combineren om een complexe vraag te beantwoorden: advies geven, diagnose stellen, afwegen | "Adviseer de cliënt" / "Wat zijn de gevolgen van X voor Y en Z?" |

## Aanpak

### Drie lagen studiemateriaal

Het bekwaamheidsexamen toetst bekwaamheid = het vermogen om technieken correct toe te passen in onbekende situaties. Daarvoor zijn drie soorten studiemateriaal nodig:

| Laag | Vraag | Content | Bron van waarheid |
|------|-------|---------|-------------------|
| **Kennis** (materie) | Wat is X? Hoe werkt X? | Één concept per fiche in `content/materie/` | Wetteksten, CBN-adviezen |
| **Competentie** | Hoe pak ik dit type taak aan? | Één techniek per fiche in `content/competenties/` | ITAA-normen, CBN, beroepspraktijk |
| **Synthese** | Hoe combineer ik competenties over domeinen? | Voorbeeldexamenvragen bij programmaonderdelen | Voorbeeldexamens |

Materie = de blokjes. Competenties = de bouwtechnieken. Synthese = oefenen met beide tegelijk.

Een competentie is zelfstandig toetsbaar op het examen en combineert meerdere materie-bouwstenen in een aanbevolen werkwijze. Ze kan via compositie naar andere competenties verwijzen als sub-stap.

**Motiveringsstructuur**: elk antwoord op integratieniveau volgt **conclusie → grondslag → redenering**. Dit is een globale stelregel — niet herhalen in individuele fiches.

### Materie vs. competentie

**Canonieke thuisplaats**: elk stuk inhoud heeft één vaste plek — materie of competentie, nooit beide.

**Onzekere overlap tussen concepten**: behandel apart en documenteer de twijfel (`⚠️ mogelijke overlap met [[andere-fiche]]`). Niet vooraf samenvoegen op basis van een vermoeden — de inhoudelijke controle bij Stap 4 vindt incoherenties vanzelf.

**Zeker hetzelfde concept**: zet in dezelfde fiche. Coherentieproblemen worden opgelost in de verificatiestap, niet door te splitsen.

**Naamgeving competenties**: altijd een werkwoord + object, actiegericht. ✓ `continuiteit-beoordelen`, ✓ `jaarrekening-herwerken` — ✗ `falingspredictie-beoordelen` (substantief + werkwoord).

**Naam verifiëren na schrijven**: de naam is een hypothese bij aanvang. Na het schrijven van de fiche: stel jezelf de vraag *"Dekt de naam het volledige bereik van de competentie, of slechts één fase?"* Zo niet: hernoem vóór commit. Prioriteitsvolgorde: (1) zoek of een gezaghebbende bron (ITAA-norm, wettekst) een naam geeft → gebruik die; (2) anders: draft-naam aanpassen aan de werkelijke scope.

| Hoort in materie | Hoort in competentie |
|---|---|
| Definitie van een begrip | Hoe je een begrip gebruikt in een taakcontext |
| Drempelwaarden en criteria | Wanneer je welk criterium toepast |
| Formule van een ratio | Welke ratio's relevant zijn voor welk analysedoel |
| Wettelijke verplichting | Hoe je de naleving ervan verifieert |
| Benchmark of sectorgemiddelde | Hoe je een uitkomst interpreteert aan de hand van die benchmark |

Een competentie citeert materie kort als context voor een stap, maar de volledige uitleg staat altijd in de materie-fiche. Omgekeerd vermeldt een materie-fiche niet hoe de informatie in een taakcontext gebruikt wordt — dat is de rol van de competentie.

**Concrete ankerpunten bij links** — geldt voor alle fiches (materie én competentie): geef bij een verwijzing naar een andere fiche altijd 1–3 concrete voorbeelden of sleutelwoorden, dan pas de link naar de volledige uitleg.
- ✓ "Groepeer rubrieken per categorie (bv. `29/58` = vlottende activa, `10/15` = EV) — volledige mapping: [[jaarrekeninganalyse#-analytische-indeling-van-de-balans|Analytische indeling balans]]"
- ✗ "Groepeer rubrieken, zie [[jaarrekeninganalyse]]" — te kaal: de student weet niet wat ze gaan vinden

**Gebruik van `→`** — de pijl heeft twee geldige toepassingen; gebruik hem nergens anders:
- Logische flow in tekst: "oorzaak → gevolg", "A → B → C"
- PO-fiche takenbullet: `- → [[competentie|Naam]]` — semantische markering van een competentielink

Gebruik **geen** `→` als vervanging voor een gewone link in lopende tekst: schrijf `[[link|Beschrijving]]` of `Zie [[link|Beschrijving]]`, niet `→ Zie [[link]]`.

### Terminologie

| Term | Betekenis |
|------|-----------|
| **TDKs** | Taken, Doelstellingen en Kenniselementen — de inhoud van een programmaonderdeel-fiche |
| **Materie** | Kennisfiches: één concept per fiche in `content/materie/` — de bouwstenen |
| **Competentie** | Techniekefiches: hoe je meerdere kenniselementen combineert voor een taak — in `content/competenties/` |
| **Concept / fenomeen** | Één coherent studieonderwerp met een eigen fiche in `content/materie/` |

Kenniselement-IDs komen uit de officiële brochure (april 2022):
- 1.1 t.e.m. 1.9 = accountancy
- 2.1 t.e.m. 2.8 = fiscaal
- 3.1, 3.2 = vennootschapsrecht
- 4.0 = deontologie

### Status en tags

Programmaonderdeel-fiches en materie-fiches gebruiken tags om hun status aan te geven in de Explorer:

| Tags | Betekenis | Zichtbaar in Explorer |
|------|-----------|----------------------|
| `[wip]` | Actief in behandeling | **Ja** |
| `[wip, verborgen]` | Nog niet behandeld (onderdelen die nog niet aan bod komen) | **Nee** |
| *(geen wip-tag)* | Voltooid en geverifieerd door de gebruiker | **Ja** |

De `wip`-tag volstaat als indicator — géén [WIP]-prefix in de titel.

**Werkwijze programmaonderdelen**: wanneer we een vak beginnen te behandelen, verwijder de `verborgen`-tag. De `wip`-tag blijft staan tot de gebruiker valideert.

**Werkwijze materie**: nieuwe conceptfiches starten altijd met `wip`-tag. De tag wordt pas verwijderd (en `status` van `draft` naar `geverifieerd` gezet) wanneer de gebruiker de inhoud valideert. Alleen de gebruiker doet dat.

**Nieuwe inzichten doorvoeren — ook op geverifieerde fiches**: als een architectureel of inhoudelijk inzicht vereist dat een geverifieerde fiche aangepast wordt, voer de wijziging volledig door:
1. Zet `status` terug naar `draft` en voeg `wip`-tag toe
2. Voeg een entry toe aan `CHANGELOG.md` met datum, bestandsnaam en reden
3. Pas alle afhankelijke fiches en links aan

**CHANGELOG.md**: het centrale overzicht van alle wijzigingen aan eerder geverifieerde fiches. Formaat: chronologisch, per sessie gegroepeerd. De gebruiker markeert "geverifieerd tot [datum]" na een verificatieronde — zo weet iedereen welke batch al bekeken is.

## Bronnen

### Primaire werkreferentie

Bronnen staan in twee plaatsen:
- **`resources/`**: bronbestanden voor verificatie en opzoekwerk — doorzoekbaar met `grep` of `Read`
- **`content/bronnen/`**: site-versie met Quartz-ankers — gebruik dit pad voor wikilinks

**Semantische indexes** (altijd eerst raadplegen vóór je gaat greppen):

| Index | Inhoud | Gebruik |
|---|---|---|
| `resources/normen/INDEX.md` | ITAA-normen: naam, datum, thema's; ook welke nog achter auth zitten | Welke norm regelt procedure X? |
| `resources/adviezen/INDEX.md` | Alle CBN-adviezen: nummer, datum, thema's per advies | Welk advies is relevant voor onderwerp X? |
| `resources/wetteksten/INDEX.md` | Alle lokale wetteksten met thema's | Welke wet/KB behandelt onderwerp X? |
| `resources/voorbeeldexamens/INDEX.md` | Per examen: POs, vraagtypen, thema's | Welk examen bevraagt PO X / concept Y? |

> **⚠️ Nummerverschuiving oude examens**: de voorbeeldexamens van vóór 2022 gebruiken de _oude_ PO-nummering (zonder PO 2.1 Algemene beginselen). Vertaaltabel: oud 2.1 PB = nieuw 2.2 · oud 2.2 VennB = nieuw 2.3 · oud 2.3 BTW = nieuw 2.4 · oud 2.4 Registratie = nieuw 2.5 · oud 2.6 Europees = nieuw 2.8. Bij het toewijzen van examenthema's: controleer of een vraag gelabeld als oud 2.2 (VennB) of oud 2.3 (BTW) niet eerder thuishoort bij **nieuw 2.1 Algemene beginselen** — dat PO bestond niet in de oude examens maar kan inhoudelijk gedekt zijn door die vragen.

**ITAA-normen doorzoeken** — elk norm-bestand heeft YAML-frontmatter met `naam`, `datum`, `themas` (lijst):
```bash
# Op thema:
grep -rl "  - antiwitwas" content/bronnen/normen/
grep -rl "  - controle" content/bronnen/normen/

# Vrije tekst:
grep -rl "opdrachtbrief" content/bronnen/normen/
```

**CBN-adviezen doorzoeken** — elk advies heeft YAML-frontmatter met `nummer`, `datum`, `themas` (lijst):
```bash
# Op thema (frontmatter — meest precies):
grep -rl "  - leasing" content/bronnen/adviezen/
grep -rl "  - afschrijving" content/bronnen/adviezen/

# Op jaar:
grep -rl "datum: 2021" content/bronnen/adviezen/

# Vrije tekst in body:
grep -rl "operationele leasing" content/bronnen/adviezen/

# Gecombineerd — thema + recent:
grep -l "  - leasing" content/bronnen/adviezen/ | xargs grep -l "datum: 202"
```

**Werkwijze bronopzoeking** (bij elke PO-build):
1. Lees de relevante INDEX.md — identificeer kandidaat-bronnen semantisch
2. Grep op thema via `  - [thema]` in frontmatter, of op vrije tekst in body
3. Lees de volledige gevonden passages voor citaat en verificatie
4. Ga enkel online als de bron niet lokaal beschikbaar is (zie `resources/wetteksten/INDEX.md` voor ontbrekende wetten)

**ITAA-LEX** is geen aparte bron maar een bundeling van wetteksten en normen met paginanummers. Studeer met ITAA-LEX referenties (sectienummer + paginanummer) in de bronfiches zelf — zo oefen je ook de opzoeklogica voor het examen.

**Cijferzakboekje** is een aparte examenbron met geïndexeerde bedragen en tarieven die niet in de wetteksten staan. Vermeld bij exacte bedragen de bron als "Cijferzakboekje [jaar]".

| Content-pad | Wet | ITAA-LEX sectie |
|-------------|-----|-----------------|
| `content/bronnen/wetteksten/XVII-antiwitwaswet.md` | Antiwitwaswet 2017 (t.e.m. 24/12/2025) | XVII |
| `content/bronnen/wetteksten/XXI-wet-itaa.md` | Wet ITAA 17/03/2019 | XXI |
| `content/bronnen/wetteksten/XV-wvv.md` | WVV 23/03/2019 | XV |
| `content/bronnen/wetteksten/XV-KB-wvv.md` | KB 29/04/2019 uitvoering WVV | XV (KB) |
| `content/bronnen/wetteksten/XIII-wer/` | WER (per Boek) | XIII |
| `content/bronnen/wetteksten/XIII-KB-wer-boekhouding.md` | KB 21/10/2018 boekhoudnormen WER | XIII (KB) |
| `content/bronnen/wetteksten/IVA-vcf.md` | VCF (t.e.m. 31/12/2025) | IV.A |
| `content/bronnen/wetteksten/VII-wetboek-invordering.md` | Wetboek Invordering 2019 | VII |
| `content/bronnen/wetteksten/V-wdrt.md` | Wetboek Diverse Rechten en Taksen | V |
| `content/bronnen/wetteksten/XI-oud-bw.md` | Oud Burgerlijk Wetboek | XI (oud) |
| `content/bronnen/wetteksten/II-KB-wib92.md` | KB/WIB92 27/08/1993 | II (KB) |
| `content/bronnen/wetteksten/EU-richtlijn-2013-34.md` | Richtlijn 2013/34/EU | EU |

**Nog niet lokaal beschikbaar als volledige tekst** (placeholders aanwezig in `content/bronnen/wetteksten/`): WIB92, BTW-Wetboek, BW 2019, VCF-UVB, Ord. Brussel Fiscale Procedure, Decr. Waals. Zie ook `resources/wetteksten/status.md`.

**ITAA-normen lokaal beschikbaar** in `content/bronnen/normen/` (11 bestanden: 9 ITAA-normen + ISA-570 + domiciliëringsnorm). 5 normen nog achter ITAA-authenticatie — zie `resources/normen/INDEX.md` voor overzicht en download-instructies.

**Alle CBN-adviezen lokaal beschikbaar** in `content/bronnen/adviezen/` (466 bestanden, verbatim via HTML-extractie, nummerprefix). Raw PDFs in `resources/adviezen/raw/`. Semantische index: `resources/adviezen/INDEX.md`.

**Werkwijze bij het schrijven van materie:**
1. Lees `resources/wetteksten/INDEX.md` — welke wet is relevant?
2. Lees `resources/adviezen/INDEX.md` — welk CBN-advies behandelt dit onderwerp?
3. Grep in de gevonden bestanden op artikelnummer of sleutelwoord
4. Citeer inline via wikilink naar `content/bronnen/wetteksten/` of `content/bronnen/adviezen/`
5. Ga enkel online als de bron niet lokaal beschikbaar is

### Bronhiërarchie

De bronhiërarchie verschilt per laag.

**Voor materie (kennis):**
1. Wetteksten in `content/bronnen/wetteksten/` — gecoördineerde versies (dezelfde tekst als in `resources/wetteksten/`, nu met ITAA-LEX sectienummers als bestandsnaam)
2. Officiële wetteksten op [ejustice.just.fgov.be](http://ejustice.just.fgov.be)
3. [Fisconet.be](http://Fisconet.be) (WIB92, WBTW, ...)
4. CBN-adviezen in `content/bronnen/adviezen/` — volledig lokaal
5. NBB-documentatie op [nbb.be](http://nbb.be)

**Voor competenties (technieken):**
1. ITAA-normen in `content/bronnen/normen/` — 11 normen volledig lokaal; index via `resources/normen/INDEX.md`
2. CBN-adviezen in `content/bronnen/adviezen/` — 466 adviezen volledig lokaal, verbatim; index via `resources/adviezen/INDEX.md`
3. ISA / ISAE / ISRS (IBR-standaarden) — ISA-570 beschikbaar in `content/bronnen/normen/`; overige normen via ibr-ire.be (⚠️ nog niet lokaal ingeladen)
4. Administratieve circulaires FOD Financiën — hoe fiscale regels in de praktijk worden toegepast
5. Erkende handboeken en beroepspraktijk — secundair, niet bindend
6. Geconstrueerde kennis — altijd 🤖 labelen

**Voor beide:**
- De ITAA-brochure (resources/programma.pdf) — voor structuur en leerdoelen
- Cijferzakboekje — voor geïndexeerde bedragen en tarieven
- Online resources — altijd verifiëren met bovenstaande bronnen

**Werkwijze bij het schrijven van een competentie:**
1. Zoek eerst of een ITAA-norm of CBN-advies de procedure al beschrijft — dat is dan de primaire bron, geen constructie
2. Lees `resources/normen/INDEX.md` — grep dan in `content/bronnen/normen/`
3. Lees `resources/adviezen/INDEX.md` — grep dan in `content/bronnen/adviezen/`
4. Ga online (itaa.be, cnc-cbn.be) als de bron niet lokaal beschikbaar is
5. Pas als geen gezaghebbende bron bestaat: construeer de werkwijze op basis van beroepspraktijk en label als 🤖

### Bronvermelding in fiches

**Inline bronnen**: elke feitelijke bewering over wetsinhoud krijgt een klikbare verwijzing direct in de tekst via de wetteksten in `content/bronnen/wetteksten/`:
- `([[wetteksten/XXI-wet-itaa#art-37|Wet ITAA art. 37]])` — springt direct naar Art. 37 in de Wet ITAA
- `([[wetteksten/XVII-antiwitwaswet#art-47|ITAA-LEX XVII · AWW art. 47]])` — springt direct naar Art. 47 in de AWW
- `([[wetteksten/XIII-wer/boek-iii#art-iii-82|WER art. III.82]])` — WER split per Boek

**Links altijd naar artikel-anker**, nooit naar het algemene wettekst-document: `[[wetteksten/XXI-wet-itaa#art-37|...]]` en niet `[[wetteksten/XXI-wet-itaa|...]]` wanneer je een specifiek artikel bedoelt.

**Ankers in wetteksten**: Quartz strips speciale tekens (`:`, `.`, `/`) volledig — ze worden NIET omgezet naar koppeltekens. Spaties worden wél koppeltekens:
- `## Art. 47` → `#art-47`
- `## Art. 1:24` (WVV) → `#art-124` (colon verdwijnt)
- `## Art. 3:23` (KB WVV) → `#art-323`
- `## Art. III.82` (WER) → `#art-iii82` (punt verdwijnt)

**Ankers voor sectielinks in materie-fiches**: Quartz genereert ankers door de heading te slugifyen: emoji worden verwijderd **maar de spatie erna blijft** (en wordt een streepje), spaties worden koppeltekens, alles wordt lowercase, en **geaccentueerde tekens worden behouden**.

Dit betekent dat elke sectie met een emoji-heading een **leading dash** krijgt:
- Heading `## 📌 Witwassen van geld` → anker `#-witwassen-van-geld`
- Heading `## 🔒 Meldingsplicht` → anker `#-meldingsplicht`
- Heading `## 📌 Cel voor Financiële Informatieverwerking (CFI)` → anker `#-cel-voor-financiële-informatieverwerking-cfi`

Let op:
- Link: `[[antiwitwaswetgeving#-witwassen-van-geld|...]]` ✓
- Link: `[[antiwitwaswetgeving#witwassen-van-geld|...]]` ✗ (leading dash ontbreekt)
- Geaccentueerde tekens (ë, é, ij...) worden **niet** omgezet naar ASCII: gebruik `financiële` niet `financiele`

**Uitzondering**: wettekst-headings (`## Art. X`) hebben geen emoji en dus geen leading dash → anker is gewoon `#art-x`.

**Geen aparte "Bronnen en artikelen"-sectie** — bronverwijzingen staan inline in de tekst, direct na de feitelijke bewering. Een aparte sectie onderaan is redundant en niet onderhoudbaar.

**Geen links naar lokale PDF's** — altijd via de wetteksten in `content/bronnen/wetteksten/` of een publieke online bron.

### Bronintegriteit en AI-labeling

Dit is de belangrijkste regel van het hele project.

- Elk feit, elke definitie, elk wetsartikel in **materie-secties** moet traceerbaar zijn naar een concrete bron
- Schrijf NOOIT iets over wetsinhoud zonder een bronverwijzing
- Als je een concept niet met zekerheid kunt onderbouwen vanuit een bron: zeg dat expliciet en markeer het als `⚠️ te verifiëren`
- Liever een leeg veld dan een onzeker feit

**Uitzondering — valkuilen, voorbeeldvragen en competentie-heuristieken**: hier zijn AI-gegenereerde aannames toegestaan, op voorwaarde dat ze duidelijk gelabeld zijn met 🤖. De student weet dan dat dit een redenering is op basis van het concept, niet een geciteerde bron.

### Tegenstrijdige bronnen

De bronhiërarchie zegt welke bron zwaarder weegt. Als twee bronnen elkaar tegenspreken:

- Vermeld **beide standpunten expliciet** — schrijf nooit één versie alsof het de enige waarheid is
- Geef aan welke bron hogere rang heeft volgens de bronhiërarchie
- Markeer het veld als `⚠️ te verifiëren`
- Voorbeeld: "Volgens [bron A] geldt X (rang 1). Volgens [bron B] geldt Y (rang 4). ⚠️ te verifiëren — bron A heeft hogere rang maar bron B is recenter."

### Wettekst lokaal toevoegen

Eenmalig werk dat daarna Read/grep-opzoekwerk vervangt. Zodra een wettekst als `.md` beschikbaar is, gebruik je **nooit meer pdftotext** maar altijd **Read** of **grep** op het `.md`-bestand.

**Wanneer**: als een wettekst ontbreekt in `resources/wetteksten/` of slechts als placeholder bestaat.

**Proces:**
1. Download de gecoördineerde versie als PDF:
   - Belgische wetgeving → [ejustice.just.fgov.be](http://ejustice.just.fgov.be)
   - Fiscale teksten (WIB92, WBTW) → [fisconet.be](http://fisconet.be)
   - Bewaar als `resources/wetteksten/raw/NAAM.pdf`
2. Converteer naar tekst: `pdftotext resources/wetteksten/raw/NAAM.pdf - > /tmp/wet.txt`
3. Structureer als Markdown:
   - Bewaar als `resources/wetteksten/NAAM.md`
   - Heading: `# Korte naam (gecoördineerde versie datum)`
   - Artikel-headings exact: `## Art. X` — geen variaties, zodat ankers voorspelbaar zijn
   - Verwijder paginanummers, kolomkoppen en herhaalde titels
4. Maak een site-versie aan: `content/bronnen/wetteksten/NAAM.md` (dezelfde structuur, zichtbaar op de site)
5. Voeg een rij toe aan de tabel in §Primaire werkreferentie

## Programmaonderdeel-fiches

### Structuur

De programmaonderdeel-fiche is een catalogus. De officiële ITAA-tekst staat ongewijzigd. Taken linken naar competentie-fiches; kenniselementen linken naar materie-fiches. De aggregatielijsten onderaan zijn een navigatiehulp — ze worden gevuld als aggregatie van de inline links.

**Officiële tekst ongewijzigd**: de taak-omschrijving en doelstellingen worden verbatim overgenomen uit de brochure — geen parafrases, geen verkorting. De AI-aanvulling (geïdentificeerde competenties) staat in een aparte `#### Geïdentificeerde competenties` sub-sectie, expliciet gescheiden van de officiële tekst.

**Competenties op taakniveau, niet op doelstellingniveau**: de koppeling taak → competentie is N-N. Eén competentie kan meerdere doelstellingen bedienen, en één doelstelling kan meerdere competenties vereisen. Doelstellingen zijn input voor de redenering, niet de koppellaag. Als een competentie voor meerdere taken relevant is, mag ze in meerdere taken-secties verschijnen — dat is geen duplicatie, dat is de realiteit van een herbruikbare competentie.

**Conventie `→ [[...]]`**: de pijl in de competentielijst is het semantische marker. Als de fiche nog niet bestaat: `→ [[geplande-bestandsnaam|Naam van de competentie]] *(⚠️ aan te maken)*`.

**Kenniselementen zonder materie-link**: laat het item staan als gewone tekst met `*(⚠️ materie aan te maken)*`. Zo is de gap direct zichtbaar bij verificatie.

**"TDK" is intern begrip — niet in content**: "TDK" (Taken, Doelstellingen en Kenniselementen) is onze interne term voor de structuur van de brochure. In de fiches zelf gebruiken we de echte termen: "Kenniselement", "Taak", "Doelstelling".

**TDKs linken naar materie**: elke TDK die verwijst naar een te kennen concept krijgt een link naar de relevante **sectie** in de materie-fiche. Ankers zijn zonder emoji (Quartz strips ze):

```markdown
- Een [[antiwitwaswetgeving#meldingsplicht-en-het-verbod-op-mededeling-tipping-off|meldingsplicht]] uitvoeren
```

Een bullet zonder link naar materie is een signaal dat er materie ontbreekt of dat de link nog niet gelegd is.

### Template

Elk bestand in `content/programmaonderdelen/` volgt dit formaat:

```
---
explorer_title: "X.X Korte naam"      # weergave in de Explorer
tags: ["X.X", wip, programmaonderdeel]
bouwversie: 1
---

# X.X Volledige naam van het programmaonderdeel

## Taken en doelstellingen

### Taak: [omschrijving verbatim uit brochure]

- [doelstelling 1 verbatim uit brochure]
- [doelstelling 2 verbatim uit brochure]

#### Geïdentificeerde competenties

- → [[competentie-fiche-a|Naam competentie A]]
- → [[competentie-fiche-b|Naam competentie B]] *(⚠️ aan te maken)*

## Kenniselementen

**I. Groepsnaam**
- I.A — [[materie-fiche|Naam kenniselement]]: korte omschrijving
- I.B — Naam kenniselement *(⚠️ materie aan te maken)*
- I.C — Naam kenniselement
  1. [[materie-fiche|Subitem A]]
  2. Subitem B *(⚠️ materie aan te maken)*

**II. Groepsnaam**
- II.A — [[materie-fiche|Naam kenniselement]]

## Relevante competenties

- [[competentie-fiche-a|Naam competentie A]]
- [[competentie-fiche-b|Naam competentie B]]

## Relevante materie

- [[materie-fiche-a|Naam concept A]]
- [[materie-fiche-b|Naam concept B]]
```

### Conventies

**"Relevante materie" — volledigheidseis**: de sectie onderaan de vakfiche heet **"Relevante materie"** (vroeger: "Concepten"). Ze bevat alle conceptfiches die samen de volledige examenstof voor dit vak dekken.

**Eis**: een student die enkel de "Relevante materie"-lijst doorloopt zonder één TDK-link te volgen, moet toch alle examenstof gezien hebben. De lijst is dus geen subset — ze is compleet.

**Niet opnemen in een programmaonderdeel-fiche**: een sectie "Aangehaalde wetteksten" of soortgelijk overzicht van bronnen — bronnen worden inline vermeld in de materie-fiches zelf, niet in de vakfiche.

### Verificatiestap

Na het opstellen of bijwerken van een vakfiche, doorloop je expliciet:

1. **Elke TDK** → heeft die een link naar de juiste sectie in een conceptfiche?
2. **Elke conceptfiche in "Relevante materie"** → dekt die alle TDKs die ernaar linken?
3. **Zijn er TDKs die naar geen enkele materie linken?** → maak de ontbrekende materie aan of voeg het kenniselement toe als sectie in een bestaande fiche
4. **Laagcheck** (voor programmaonderdelen op `niveau: integratie`) — signaleer als een laag ontbreekt in de materie-fiches:
   - **Weten**: 📌, ⚖️ of 🔒 → vrijwel altijd aanwezig
   - **Toepassen**: 📋, 🔢, ✅ of 👤 → mist regelmatig
   - **Integreren**: 🔍, ↔️ of 💬 → mist het vaakst
   
   Een integratiefiche zonder Integreren-sectie is een signaal dat de laag mogelijk ontbreekt — niet automatisch een fout (de laag kan ook gedekt zijn via een andere fiche in het programmaonderdeel). Meld dit aan de gebruiker maar blokkeer niet.

## Competentie-fiches

### Granulariteit en compositie

**Granulariteit**: één competentie per zelfstandig toetsbaar examenvaardigheidtype. Als je een examenvraag kunt verzinnen die enkel over deze techniek gaat, verdient ze een eigen fiche.

**Compositie**: een competentie kan naar een andere competentie verwijzen als sub-stap. Nooit herhalen wat al elders staat.

### Staptypes

Elke stap in de aanbevolen werkwijze heeft een type. Het type bepaalt de aard van de redenering en de verwachte uitkomst:

| Icoon | Type | Vraag die het beantwoordt |
|---|---|---|
| 🎯 | **Doel** | Wat wil ik bereiken met deze analyse/taak? |
| 🔍 | **Vaststelling** | Wat is dit? Wie is dit? Welke categorie? |
| 🔀 | **Beslissing** | Welke optie is van toepassing, op basis van welke regel of overweging? |
| 🔢 | **Berekening** | Wat is de waarde? (instructie, niet vraag) |
| 📊 | **Diagnose** | Wat betekenen de geobserveerde signalen in deze context? (past patronen toe) |
| 💬 | **Synthese** | Wat is het totaalplaatje? Welk advies volgt hieruit? |

💬 Synthese en 📊 Diagnose bestaan **uitsluitend** als competentie-staptype — niet als materie-sectiontype.

### Regels

**Volgorde van stappen**: elke stap heeft een expliciete 📥 en 📤 als blockquote vóór de uitleg. Dit maakt de keten zichtbaar, linkbaar en parseerbaar. Inputs die door een vorige stap geproduceerd worden, linken naar die stap. Feiten of externe invoer hebben geen link.

```markdown
> 📥 **Nodig**:
> - [[andere-competentie#stap-x|Output van stap X]]
> - Extern feit (geen link)
>
> 📤 **Uitkomst**:
> - Resultaat A
> - Resultaat B
```

Enkelvoudig: één bullet (ook al is het er maar één — altijd bullet voor consistentie).

**Normale situatie eerst**: de hoofdlijn staat vooraan; uitzonderingen volgen als vetgedrukte `**Uitzondering — [naam]:**` alinea's.

**Geen speciale oordeel-markers**: iedere stap vereist oordeel. Maak niet sommige stappen "speciaal" door een aparte marker — het oordeel zit in de redenering zelf.

**Valkuilen inline**: `[!warning]` callout direct na de stap die ze triggert, zelfde format als materie-fiches.

**Tips**: `[!tip]` callout voor professionele hints die niet uit een bron komen.

**Visueel anker**: een code-blok met een extract uit een jaarrekening, balans, resultatenrekening of ander financieel schema — zodat de student weet *waarnaar* ze kijkt wanneer ze de stap uitvoert. Verplicht bij elke stap die inwerkt op een financieel document (herstructurering, extractie, ratio-berekening). Gebruik altijd een `code`-blok, nooit proza. Voor transformatiestappen (bv. herwerken): toon voor- én na-toestand als twee opeenvolgende blokken.

**Concreet stap-voorbeeld**: `[!info]- Concreet: [situatienaam]` callout — 1-3 zinnen die *deze stap* toepassen op een specifieke situatie, zonder volledig eindgeval te zijn. Verschil met `## Voorbeelden`: dát is het uitgewerkte eindresultaat; dit is een haakje per stap dat de stap minder abstract maakt. Label met 🤖 als geconstrueerd. Verplicht bij stappen die een oordeel of beslissing vereisen zonder visueel anker.

**Stapnamen**: altijd in instructievorm — kort, actief, zonder vraagteken. ✓ "Schema vaststellen", ✓ "Balans herstructureren", ✓ "Ratio berekenen" — ✗ "Welk schema is van toepassing?"

**itaa-lex-secties** in de frontmatter: navigatiehulp voor het examen ("welke secties heb ik bij de hand nodig?"), geen grondslagen.

**Grondslag van de procedure (zichtbaar blok)**: het `> [!info] Grondslag van deze werkwijze`-blok direct na de intro beantwoordt één vraag: *bestaat er een norm, advies of bronwerk dat deze procedure als geheel beschrijft?* Het is geen opsomming van wetsartikels per stap — dat hoort inline bij de stap zelf.

Mogelijke antwoorden:
- "Deze procedure is beschreven in ITAA-norm X / CBN-advies YYYY/NN — de stappen volgen die norm."
- "Er bestaat geen specifieke norm voor deze procedure. De stappen zijn gebaseerd op [beroepspraktijk / NBB-documentatie / ISA X als referentie 🤖]."
- "De wettelijke verplichtingen volgen uit [wet], de analytische stappen zijn gebaseerd op [bron/praktijk 🤖]."

**Bronvermelding per stap**: stappen die uit een concrete bron volgen, vermelden dat inline:
- Stap volgt uit een wettekst: `*(Grondslag: [[wetteksten/...|Art. X]])*`
- Stap volgt uit een CBN-advies: `*(Grondslag: CBN-advies YYYY/NN)*`
- Stap is analytische conventie zonder gezaghebbende bron: `*(Grondslag: 🤖 analytische praktijk)*`

Niet elke stap heeft een expliciete grondslag nodig — voeg hem toe wanneer de bron niet evident is of wanneer het voor de student relevant is te weten of de stap wettelijk verplicht of analytisch conventioneel is.

**Stappen bepalen via bronnen**: zoek eerst of een ITAA-norm of CBN-advies de procedure al beschrijft. Grep in `resources/normen/`; voor CBN-adviezen via `resources/adviezen/INDEX.md` → `content/bronnen/adviezen/`. Ga daarna online (itaa.be, cnc-cbn.be). Pas als geen gezaghebbende bron bestaat: construeer op basis van beroepspraktijk en label als 🤖.

**Elke stap begint met een "waarom"-zin**: de eerste zin na het `📥/📤`-blok beantwoordt *waarom* deze stap noodzakelijk is — niet wat je doet, maar waarom je het doet. Zonder die zin is de stap een procedure-instructie zonder grond; met die zin begrijpt de student de logica en kan ze hem hertoepassen in nieuwe situaties.

- ✓ "Zonder dit doel berekent de student ratio's die irrelevant zijn voor de opdracht."
- ✓ "De wet verbindt dwingende proceduregevolgen aan het bereiken van specifieke drempels — het al dan niet van toepassing zijn is niet-discretionair."
- ✓ "Wie niet herstructureert, berekent ratio's op een juridische indeling die economisch vertekend is."
- ✗ een herhaling van de stapnaam ("In deze stap ga je X doen")
- ✗ een beschrijving van de output ("De uitkomst is Y") — die staat al in het `📤`-blok

**Inhoud in de juiste laag**: als een stap kennis over een begrip of definitie nodig heeft, staat die kennis in de materie-fiche — niet herschreven in de competentie. De stap verwijst ernaar met een concreet ankerpunt (zie §Aanpak > Materie vs. competentie).

Een stap bevat precies: de waarom-zin, de procedure-instructie (hoe), links naar materie, en de concrete elementen die de stap leesbaar maken: visueel anker, `[!info]- Concreet`, `[!warning]`, `[!tip]`. Geen materie herschrijven. Als een opsomming meer dan 3 items bevat (signalen, criteria): staat het al in een materie-fiche? Ja → vervang door link met 1-2 ankerwoorden. Nee → verplaats naar materie-fiche en link daarna.

**Competentie veronderstelt bekende materie**: een stap mag veronderstellen dat de student de gekoppelde materie heeft bestudeerd. De stap hoeft die materie niet te herhalen — maximaal 1-2 zinnen verbinding met de taakcontext zijn toegestaan. De student weet wat een continuïteitsveronderstelling is; de stap legt alleen uit *wanneer en waarom* ze die kennis hier toepast.

**Stap vanuit perspectief van de beroepsbeoefenaar**: elke stap beschrijft wat de beroepsbeoefenaar (GA/GBA/accountant) doet of beoordeelt. Als een stap iets beschrijft wat een ander (bv. het bestuursorgaan) moet doen, schrijf dan: "controleer als beroepsbeoefenaar of het bestuursorgaan X heeft gedaan" — niet "het bestuursorgaan doet X". De beroepsbeoefenaar is steeds de actor.

**Waarom-zin + beginsel**: de waarom-zin mag en moet een wettelijk of boekhoudkundig beginsel vermelden als dat de diepere reden is. Voorbeeld: "Waarom: het [[boekhoudkundige-beginselen#️-continuïteitsbeginsel|continuïteitsbeginsel]] veronderstelt dat de onderneming haar activiteiten voortzet — bij twijfel geldt een verantwoordingsplicht." Het beginsel is de grondslag van de stap, niet de stap zelf.

**Optionele of conditionele stap = aparte stap**: als een actie alleen onder een specifieke conditie wordt uitgevoerd (bv. "indien geen reactie binnen 1 maand"), maak dat dan een aparte genummerde stap met conditionele aanhef: `### 5c. 🔒 [Naam] (indien [conditie])`. Conditionele acties verbergen in een beschrijvende opsomming mist de logica van de procedure.

**"Typische vraagvormen" → "Voorbeeldvragen"**: alle competentie-fiches gebruiken dezelfde terminologie als materie-fiches. De sectie heet "Voorbeeldvragen" en gebruikt het `[!question]-` / `[!success]-` format. "Typische vraagvormen" is verouderd.

**Grondslag-blok: collapsible + AI-indicator**: het grondslag-blok is altijd collapsible (`> [!info]-`) en vermeldt in de titel de verhouding analytische praktijk vs wettelijk genormeerd als percentage: `> [!info]- Grondslag van deze werkwijze (🤖 60% · ⚖️ 40%)`. Gebruik `🤖` voor analytische praktijk en `⚖️` voor wettelijk/normatief genormeerde stappen. Volledig analytisch: `(🤖 100%)`. Zo weet de student direct welke stappen gecodificeerd zijn en welke niet.

**Voorbeelden verplicht**: voeg bij elke competentie minstens één concreet uitgewerkt voorbeeld toe met Situatie / Conclusie / Grondslag / Redenering. Een werkwijze zonder voorbeeld is onvolledig.

**Voorbeeldvragen**: zelfde format als materie-fiches (`[!question]-` genest met `[!success]-`). Raadpleeg eerst `resources/voorbeeldexamens/` voor echte examenvragen.

### Template

```markdown
---
tags: ["X.X", wip, competentie]
niveau: integratie
status: draft
bouwversie: 1
programmaonderdelen: ["X.X"]
itaa-lex-secties:
  - [sectie] ([wet] art. X–Y)
procedure-grondslag: "[ITAA-norm X / CBN-advies YYYY/NN / analytische praktijk 🤖]"
---

# Naam van de competentie

Beschrijf de competentie zo uitgebreid als nodig: wat doe je, waarvoor, in welke situatie, en wat maakt deze competentie anders dan aangrenzende competenties. Eén zin kan volstaan als de scope meteen duidelijk is, maar schrijf gerust twee à drie zinnen als dat helpt om misverstanden te vermijden.

> [!info]- Grondslag van deze werkwijze (🤖 X% · ⚖️ Y%)
> [Beschrijf hier waar de procedure als geheel vandaan komt. Bv.: "Deze procedure volgt ITAA-norm X." of "Er bestaat geen specifieke norm — de stappen zijn gebaseerd op [bron/praktijk 🤖]."]

## Aanbevolen werkwijze

### 1. 🔍 [Stap in instructievorm]

> 📥 **Nodig**:
> - [input of link naar producerende stap]
>
> 📤 **Uitkomst**:
> - [output A]

**Waarom**: [één zin die verklaart waarom de stap noodzakelijk is — beantwoordt "zonder dit weet/kan je X niet"]

[Normale situatie: wat geldt in de meeste gevallen. Maximaal 3 opsommingspunten inline; meer dan 3 → verplaats naar materie-fiche en link.]

**Uitzondering — [naam]**: [wat er anders is en waarom]

```
[Visueel anker: extract uit jaarrekening, balans of schema — bij stappen die inwerken op een financieel document]
[Voor transformatiestappen: toon voor- én na-toestand als twee opeenvolgende blokken]
```

> [!info]- Concreet: [situatienaam]
>
> [1-3 zinnen die deze stap toepassen op een specifieke situatie]
>
> 🤖 *AI-aanvulling*

> [!warning]- [Valkuil: korte naam]
> ❌ *"[Verkeerde aanname die studenten maken]"*
>
> [Correcte redenering]
>
> 🤖 *AI-aanvulling*

> [!tip]- [Tip: korte naam]
> [Praktische hint voor de uitvoering]

### 2. 🔀 [Volgende stap]
...

## Voorbeelden

> [!example]- [Naam van de situatie]
>
> **Situatie**: ...
>
> **Conclusie**: ...
>
> **Grondslag**: ...
>
> **Redenering**: ...
>
> 🤖 *AI-aanvulling*

## Motiveren op het examen

**Een volledig antwoord bevat:**
1. ...
2. ...

**Typische vraagvormen**

> [!question]- [Korte vraagnaam]
>
> [Vraag volledig geformuleerd]
>
> > [!success]- Antwoord
> >
> > **[Verdict]**
> >
> > [Uitleg]
>
> 📝 *Uit voorbeeldexamen [jaar]* — of — 🤖 *AI-aanvulling*
```

## Materie-fiches

### Wat is een concept?

Een concept is de **kleinste coherente eenheid die een student als één geheel moet begrijpen**. De grens ligt daar waar twee stukken kennis onafhankelijk van elkaar bestudeerbaar zijn — dan zijn het twee concepten. Als kennis over het ene zinloos is zonder het andere — dan is het één concept.

**Concepten worden gedefinieerd door het reële fenomeen of studieonderwerp**, niet door de juridische structuur of de vakindeling:
- ✓ "autoleasing" (boekhoudkundig + fiscaal + advies samen)
- ✓ "antiwitwaswetgeving" (scope + verplichtingen samen — niet te splitsen)
- ✓ "deontologische beginselen" (de 7 principes als geheel)
- ✗ niet: "AWW art. 47" of "kenniselement D.6"

**Grootte**: zo groot als nodig. Splitsen alleen als twee ideeën écht onafhankelijk van elkaar voorkomen én bestudeerbaar zijn. Als een concept te groot wordt, kan een specifieker onderdeel een **subconcept** worden dat voortbouwt op het hoofdconcept — het subconcept veronderstelt dan dat de student het hoofdconcept kent.

**Vakoverschrijdend is gewenst**: een concept dat in meerdere vakken voorkomt, krijgt één fiche die alle relevante contexten dekt. De vakken zijn een examen-organisatielaag, geen kennislaag — in de praktijk lopen boekhoudkundige, fiscale en juridische aspecten door elkaar, en dat is ook het niveau waarop het examen toetst.

**Secties volgen topics, niet vakken**: organiseer een fiche per inhoudelijk thema, niet per programmaonderdeel. De interessante stof zit vaak *in de overgang* tussen contexten — een `↔️ Boekhoudkundig vs. fiscaal`-sectie geeft meer inzicht dan twee aparte vak-secties naast elkaar. Per-vak-secties (`### [2.x] Personenbelasting`) zijn enkel gerechtvaardigd als de regels zo fundamenteel verschillen per context dat ze niet zinvol samen te bespreken zijn.

De koppeling concept → vak wordt afgehandeld via de `Relevant voor`-sectie onderaan de fiche en via de PO-fiches — niet via de interne structuur van de materie-fiche.

### Concepten identificeren

**Vertrekpunt**: de TDKs van de vakfiches. Die beschrijven wat een student moet *kunnen doen* en *begrijpen* — de concepten zijn de bouwstenen daarvoor.

**Werkwijze**:
1. Lees de taken en doelstellingen: welk fenomeen of onderwerp moet de student beheersen om deze taak uit te voeren?
2. Lees de kenniselementen: welke begrippen en onderwerpen worden expliciet genoemd?
3. Let ook op **impliciete concepten**: dingen die niet met naam worden vermeld maar wel verondersteld worden
4. Vermijd duplicaten: als hetzelfde fenomeen al als concept bestaat (ook in een ander vak), breid dat concept uit — maak geen tweede fiche

**Geen dubbele concepten**: elk fenomeen of studieonderwerp krijgt precies één fiche. Concepten kunnen op elkaar voortbouwen via wikilinks en subconcept-relaties, maar overlappen niet.

### Niveauindeling van een concept

De frontmatter van elke conceptfiche bevat een `niveau`-veld. Claude kiest het niveau op basis van de TDKs in de vakfiche — niet op basis van aannames.

Een concept kan voor verschillende vakken een verschillend niveau hebben — vermeld dan het hoogste niveau in de frontmatter.

### Domeinen

| Domein | Omschrijving |
|--------|-------------|
| **Boekhoudkundig** | Boeking, waardering, jaarrekening, analytische boekhouding |
| **Fiscaal** | Belastingen, aftrekken, aangiften, procedures |
| **Juridisch** | Wetgeving, rechten, verplichtingen, rechtspraak |

Een concept kan secties uit meerdere domeinen bevatten. Als een sectie niet past binnen deze domeinen, stel dan een nieuw domein voor ter validatie door de gebruiker.

### Sectietypes

Materie-fiches gebruiken 10 sectietypes. 💬 Advies en 🔍 Diagnose bestaan **niet** in materie — die horen uitsluitend in competentie-fiches.

| Emoji | Type | Vraag die het beantwoordt | Signaalwoorden |
|-------|------|--------------------------|----------------|
| 📌 | **Begrip** | Wat is X? | definitie, term, afkorting |
| ⚖️ | **Principe** | Hoe werkt X als algemene regel? | beginsel, basisregel |
| 📋 | **Procedure** | Welke stappen volg je? | stappen, termijnen, volgorde |
| 🔢 | **Berekening** | Hoe reken je X uit? | formule, ratio, tarief, grondslag |
| ↔️ | **Vergelijking** | Wat is het verschil tussen X en Y? | vs, verschil, kies je voor |
| ✅ | **Checklist** | Wat controleer je? | controleer of, verifieer, ga na |
| 🔒 | **Verplichting** | Wat moet verplicht gebeuren? | verplicht, moet, meldingsplicht |
| 👤 | **Rol** | Wie doet wat? | taak van, bevoegdheid, verantwoordelijkheid |
| 🔎 | **Patroon** | Hoe herken je dat iets normaal/gezond is? Welke signalen zijn kenmerkend? | signaal, indicator, kenmerk, typisch bij |
| 🚩 | **Antipatroon** | Hoe herken je dat iets fout gaat of misleidend is? | waarschuwing, valkuil, lijkt op X maar is Y, alarmsignaal |

Een adviespatroon ("bij situatie X adviseer je Y") hoort in 🔎 of 🚩 — niet als aparte sectie.

- Een concept bevat **alleen de secties die relevant zijn** — niet elk concept heeft alle types nodig.
- Hetzelfde type mag **meerdere keren voorkomen** binnen één concept.

### Kennislagen

| Laag | Brochure-niveau | Sectietypes |
|---|---|---|
| **Weten** | weten-en-inzien | 📌 begrip, ⚖️ principe, 🔒 verplichting |
| **Toepassen** | toepassen | 📋 procedure, 🔢 berekening, ✅ checklist, 👤 rol |
| **Integreren** | integratie | 🔎 patroon, 🚩 antipatroon, ↔️ vergelijking |

Een fiche met alleen 📌 en ⚖️ secties is functioneel een weten-fiche, ongeacht de frontmatter. Het `niveau`-veld is een signaal — geen garantie.

### Schrijfstijl

- **Menselijke, heldere taal** — geen legalese, wel precies
- **Niet alles is gekend** — leg ook "bekende" begrippen kort uit, mensen vergeten
- **Afkortingen** — eerste vermelding altijd voluit met een wikilink naar de fiche (en zo mogelijk naar de specifieke sectie) waar het begrip uitgelegd wordt: "Gecertificeerd Belastingadviseur ([[beroep-van-accountant-en-belastingadviseur|GBA]])"; daarna gewoon de afkorting
- **Voluit schrijven**: gebruik de **volledige term** waar mogelijk, en de afkorting enkel wanneer die écht courant is (btw, bv, nv) of wanneer de wet zelf uitsluitend de afkorting gebruikt. Twijfelgevallen: schrijf voluit.
  - ✓ "witwassen van geld en financiering van terrorisme" (bij eerste vermelding), daarna "WG/FT" enkel als de context het vanzelfsprekend maakt
  - ✓ "cliëntenonderzoek" ipv "CDD" in lopende tekst
  - ✓ "uiteindelijke begunstigde" ipv "UBO" waar het past
  - ✓ "btw", "bv", "nv" → courant genoeg om altijd als afkorting te gebruiken
- **Wikilinks** — elk concept dat elders een fiche heeft, krijgt een `[[link]]` bij elke vermelding; zo mogelijk naar de relevante sectie via `[[fiche#sectie|tekst]]`. Dit geldt ook voor impliciete verwijzingen: als een zin verwijst naar een begrip of verplichting die in een andere sectie uitgelegd wordt — ook al staat de naam er niet letterlijk — wordt dat een link. Bv. "de meldingsplicht" → `[[antiwitwaswetgeving#meldingsplicht-en-het-verbod-op-mededeling-tipping-off|meldingsplicht]]`.
- **Programmaonderdelen in numerieke volgorde** — 1.2 voor 2.3 voor 3.1 enz.
- **Exacte bedragen**: vermeld ze ter referentie met bronverwijzing naar ITAA-LEX of cijferzakboekje, maar leg de nadruk op het concept erachter — niet op het getal zelf
- **Praktijkvoorbeelden**: concrete situaties die helpen begrijpen wat de regel betekent. Mag 🤖 zijn als gelabeld — zie het "In de praktijk"-blok hieronder
- **Hoofdregel eerst, uitzondering daarna** — schrijf altijd de algemene regel op, dan pas de uitzonderingen. Nooit omgekeerd: een student die de uitzondering leest vóór de hoofdregel, begrijpt de uitzondering niet.
  - ✓ "Aansprakelijkheidsbeperking is toegestaan — behalve bij bedrieglijk opzet of wettelijk voorbehouden opdrachten."
  - ✗ "In twee gevallen is aansprakelijkheidsbeperking verboden ... voor andere gevallen is ze wél toegestaan."
- **Oorzaak → gevolg, niet omgekeerd** — "Niet betalen van bijdragen leidt tot een terechtwijzing" is helderder dan "Een terechtwijzing wordt opgelegd wanneer bijdragen niet betaald zijn." Gevolg-eerst klinkt juridisch maar vergt een extra denkstap.
- **Actieve zin boven passieve** — "De beroepsbeoefenaar maakt een opdrachtbrief op" is klaarder dan "Een opdrachtbrief wordt opgemaakt." Bij de passieve vorm verdwijnt de actor — en die actor is net wat de student moet onthouden. *(Uitzondering: passief is oké als de actor irrelevant is of de handeling centraal staat.)*
- **Parallelstructuur in opsommingen** — alle items in een lijst volgen dezelfde grammaticale structuur. Niet: "1. een fout begaan hebben, 2. bij bedrieglijk opzet, 3. wanneer het een voorbehouden opdracht betreft." Wél: "1. een fout begaan hebben, 2. bedrieglijk opzet hebben gehad, 3. een wettelijk voorbehouden opdracht uitvoeren." Asymmetrie suggereert ten onrechte dat de items niet op hetzelfde niveau zitten.
- **Niet herhalen — wel verwijzen** — dezelfde informatie staat nooit twee keer in een andere formulering. Als iets al in een andere sectie staat, volstaat een wikilink. Dubbele informatie raakt onvermijdelijk uit sync.
- **Wetsartikelnamen horen in voetnoten, niet midden in een zin** — bronnen worden via voetnoten verantwoord (`[^art-37]`), niet als inline vermelding. Een wetsartikelnaam midden in een zin leidt af van de inhoud en verstoort de leesbaarheid. Twijfelgeval: herformuleer zodat het artikel naar de voetnoot kan.
  - ✓ "De beroepsbeoefenaar handelt in volledige onafhankelijkheid [^art-37]."
  - ✗ "De beroepsbeoefenaar handelt in volledige onafhankelijkheid (Wet ITAA art. 37)."
  - **Uitzonderingen** waar inline wél mag:
    - Het artikel is zélf het onderwerp: "Art. 37 stelt de onafhankelijkheidseis voorop"
    - Tabelcellen met artikelnummers als inhoud (bv. `| Art. 3, 1°–5° |`) — in tabellen is de artikelreferentie het gegeven, geen bronvermelding
- **Geen circulaire definities** — definieer een begrip niet met zichzelf. Gebruik een concrete omschrijving of een ander begrip dat eerder al uitgelegd is.
- **Formule-variabelen: betekenisvolle afkortingen** — gebruik in formules altijd letters of lettercombinaties die de variabele direct benoemen, niet generieke X₁, X₂, X₃. De student moet de formule kunnen lezen zonder de bijhorende tabel. Gebruik domein-gangbare afkortingen: NBK (netto bedrijfskapitaal), TA (totaal activa), EBIT, MVE (marktwaarde eigen vermogen), VV (vreemd vermogen), O (omzet). Bv: `Z = 1,2 × (NBK/TA) + 1,4 × (IW/TA) + 3,3 × (EBIT/TA) + 0,6 × (MVE/VV) + 1,0 × (O/TA)` is leesbaar; `Z = 1,2 × X₁ + ... + 1,0 × X₅` is dat niet.
- **"(zie § X)" → klikbare wikilink** — een verwijzing naar een andere sectie is altijd een wikilink: `[[fiche#anker|sectienaam]]`. De tekst "(zie § X)" of "(zie hierboven)" zonder link is verboden. Kan je een anker bepalen? Dan link. Kan dat niet? Herformuleer de zin zodat de verwijzing overbodig wordt.
- **Geen hyperlinks in titels van collapsible callouts** — links in titels van `[!warning]-`, `[!tip]-`, `[!info]-`, `[!question]-`, `[!success]-`, `[!example]-` callouts worden niet gerenderd in Quartz. Gebruik plain text in de titel. Links mogen wel in de body van de callout.

**Structuur binnen een fiche** — de volgorde van secties volgt een vaste logica, van algemeen naar specifiek, van begrip naar toepassing:

```
1. Begrippen        — van hoog niveau naar detail; elk begrip een eigen sectie
2. Principes/regels — gebruiken alleen begrippen die al uitgelegd zijn
3. Procedures       — stap-voor-stap; sanctie direct bij de bijhorende verplichting
4. Vergelijkingen   — pas nadat alle betrokken begrippen zijn uitgelegd
5. Rollen           — wie doet wat (veronderstelt kennis van begrippen en regels)
```

**Aanvullende structuurregels:**

- **Één thema per sectie, één sectie per thema** — een sectie behandelt exact één idee. Als een sectie twee onverwante dingen bevat: opsplitsen. Als twee secties conceptueel één geheel vormen: samenvoegen. Meldingsplicht en tipping-off horen samen — het zijn twee kanten van dezelfde medaille.
- **Geen voorwaartse verwijzingen** — een begrip dat in sectie B gebruikt wordt, is al uitgelegd in sectie A. Een student die van boven naar beneden leest, mag nooit een term tegenkomen die pas verderop uitgelegd wordt. Als dat toch zo is, staat de sectievolgorde verkeerd.
- **Sancties direct bij de verplichting** — de sanctie voor het niet naleven van een verplichting staat in dezelfde sectie als die verplichting, niet verderop. *(Uitzondering: als meerdere verplichtingen dezelfde sanctie delen, mag die sanctie in een aparte sectie — mits elke verplichting ernaar verwijst.)*
- **Consistente dimensies in tabellen** — elke rij vergelijkt één en dezelfde eigenschap voor alle kolommen. Niet een rij die "wat mag" vergelijkt afwisselen met een rij die "wie het mag" vergelijkt.

**Herstructureren is geen groot werk** — als tijdens het schrijven of nalezen blijkt dat secties verkeerd geordend zijn of moeten worden samengevoegd, wordt dat genoteerd en periodiek in bulk rechtgezet.

**Boekhoudkundige beginselen vermelden waar ze inzicht geven** — een beginsel is geen decoratie maar een verklaring. Vermeld het expliciet wanneer:

| ✓ Vermelden | ✗ Niet vermelden |
|---|---|
| Het beginsel is de **grondslag** voor een procedure — het verklaart *waarom* een stap zo verloopt | De connectie is generiek ("alles moet kloppen") |
| Het beginsel genereert een **detecteerbaar signaal** in de analyse (bv. methodiewijziging → consistentiebeginsel) | Het beginsel is evident uit de context |
| Het beginsel is het **antwoord op een mogelijke "waarom"-vraag** op het examen | |

Concreet: het continuïteitsbeginsel hoort expliciet in fiches over continuïteitsrisico; het consistentiebeginsel hoort in de stap "toelichting lezen op waarderingsregels"; het voorzichtigheidsbeginsel verklaart waarom voorzieningen en waardeverminderingen ratio's vertekenen.

### Hoe een nieuwe conceptfiche starten

1. **Controleer op duplicaten**: bestaat er al een fiche voor dit fenomeen — ook onder een andere naam? Zo ja, breid die uit in plaats van een nieuwe te maken.
2. **Verifieer de bronnen**: heb je voldoende bronmateriaal (ITAA-LEX, wettekst, ITAA-norm) om het concept inhoudelijk uit te diepen zonder aannames? Zo niet, maak eerst een skelet en markeer ontbrekende delen.
3. **Volg de volgorde in §Stap 3A**: materie (brongebonden) → valkuilen + praktijkvoorbeelden (🤖 mag) → voorbeeldvragen (🤖 mag) → hyperlinks.
4. **Begin met de begrippen**: schrijf eerst de basisconcepten en definities uit — dit vormt de fundering voor alle andere secties.
5. **Markeer onzekerheden**: elk veld zonder verifieerbare bron krijgt `⚠️ te verifiëren`.
6. **Zet status op `draft`**: de gebruiker valideert de inhoud voor de status naar `geverifieerd` gaat. Schrijf nooit `status: geverifieerd` zelf.

**Toevoegen kan herstructurering vereisen** — wanneer nieuwe informatie het mentale model verandert, reorganiseer je de fiche zodat de structuur het nieuwe inzicht weerspiegelt. Niet blind aanvullen. Twee specifieke situaties:

- **Informatie verandert de lading van een bestaande sectie**: hernoem de sectie, herschrijf de intro, en pas alle downstream links en ankers aan.
- **Een kenniselement is expliciet benoemd in een TDK**: dat is een signaal dat het zelfstandig bevraagbaar is. Het moet dan als eigen `##`-sectie vindbaar zijn — niet alleen als bijvangst van een bredere sectie. Een nieuwe fiche is niet nodig; een eigen sectie in de bestaande fiche volstaat.

Alle downstream gevolgen (ankers, links in andere fiches, verwijzingen) worden meteen meegenomen — niet uitgesteld.

### Template

Elk bestand in `content/materie/` volgt dit formaat:

```
---
tags: ["4.0", wip, materie]  # programmaonderdeel-ID's + wip + materie
niveau: integratie
status: draft                 # draft → geverifieerd (alleen gebruiker zet geverifieerd)
bouwversie: 1
bronnen:
  - Wet ITAA art. 37
---

# Naam van het concept

## 📌 Term A
Definitie van Term A. ([[wetteksten/XXI-wet-itaa#art-2|ITAA-LEX XXI · Wet ITAA art. 2]])

## 📌 Term B (AFKORTING)
Definitie. Overkoepelend begrip? → Zie [[conceptfiche#term-a|Term A]], [[conceptfiche#term-c|Term C]]

## ⚖️ Naam van het principe
Inhoud. ([[wetteksten/XVII-antiwitwaswet#art-47|ITAA-LEX XVII · AWW art. 47]])

> [!warning]- Korte omschrijving van de valkuil
> ❌ *"De verkeerde aanname die studenten vaak maken."*
>
> De correcte uitleg van de regel.
>
> 📝 *Uit voorbeeldexamen 2024* — of — 🤖 *AI-aanvulling*

> [!info]- In de praktijk
> 🤖 *AI-aanvulling*
>
> Concrete situatie die helpt begrijpen wat de regel betekent.

## 🔒 Naam van de verplichting
Inhoud.

## Relevant voor

**[[X.X-naam|X.X Naam van het programmaonderdeel]]**

Taken:
- *Naam van de taak*
  - Relevante doelstelling

Kenniselementen:
- X.n — [[conceptfiche#sectie-naam|korte omschrijving]]

### Voorbeeldvragen

> [!question]- Korte vraagnaam
>
> De vraag volledig en correct geformuleerd.
>
> Juist of fout?
>
> > [!success]- Antwoord
> >
> > **Fout.**
> >
> > Uitleg van het correcte antwoord.
> >
> > *Zie: [[conceptfiche#sectie-naam|Sectienaam]]*
>
> 📝 *Uit voorbeeldexamen [jaar]* — of — 🤖 *AI-aanvulling*
```

### Conventies

#### Sectiehoofdingen: emoji vervangt het typewoord

De emoji aan het begin van een sectieheading **is** het type — het typewoord wordt niet herhaald:
- ✓ `## 📌 Witwassen van geld`
- ✗ `## 📌 Begrip: Witwassen van geld`

#### Begrippen: één per sectie, naam vóór afkorting

Elk begrip krijgt een eigen `##`-sectie, zodat het een eigen anker heeft voor deep-links. Meerdere begrippen in één sectie is niet toegestaan.

**Volgorde**: naam volledig uitgeschreven, dan afkorting tussen haakjes:
- ✓ `## 📌 Cel voor Financiële Informatieverwerking (CFI)`
- ✗ `## 📌 CFI`

**Synoniemen en anderstalige equivalenten als cursieve subtitel**: wanneer een begrip een courant synoniem heeft (Engels, Frans, Latijn of vaktaal), voeg dat toe als een cursieve subtitel direct onder de heading, vóór de bodytekst:

```markdown
## 📌 Continuïteitsveronderstelling
*Going concern*

De continuïteitsveronderstelling houdt in dat...
```

Dit geldt ook voor afkortingen die niet rechtstreeks van de naam afleiden. De subtitel is altijd cursief, nooit tussen haakjes in de heading zelf.

**Begrip ruimer dan de fiche → eigen fiche**: als een sectie een begrip definieert dat ook in andere fiches wordt gebruikt (buiten de context van dit fenomeen), hoort het begrip in zijn eigen materie-fiche. Detectiestap: wordt dit begrip gelinkt vanuit andere fiches? Heeft het geen eigen fiche? → maak de fiche, link er naartoe, verwijder de definitiesectie uit de huidige fiche. Een fiche die een begrip "leent" omdat het handig is, schendt het principe van de canonieke thuisplaats.

**Fiche-titel = kernfenomeen only**: de titel van een fiche benoemt alleen het centrale fenomeen. Beschrijvende toevoegingen horen er niet in — die zijn altijd onderdelen of gevolgen, niet het fenomeen zelf. Detectiestap: kun je het tweede deel van de titel weghalen zonder het onderwerp te verliezen? Dan hoort het weg.
- ✓ `# Continuiteitsrisico` (alarmbelprocedure is een onderdeel)
- ✗ `# Continuiteitsrisico en alarmbelprocedure`
- ✓ `# Jaarrekening` (neerlegging is een onderdeel)
- ✗ `# Jaarrekening en neerlegging`

**"Kernfenomeen" kan een tweedeling zijn**: de titel benoemt het studieobject — en soms ís het studieobject de vergelijking tussen twee nauw verwante concepten met een gedeeld bovenliggend fenomeen. Als beide concepten samen dat bovenliggende fenomeen vormen, en het onderscheid tussen beide precies is wat getoetst wordt, dan noem je beide in de titel. Voorbeeld: `# Beroepsgeheim en discretieplicht` — het bovenliggende fenomeen is de professionele vertrouwelijkheidsplicht; beroepsgeheim (strafrechtelijk) en discretieplicht (deontologisch) zijn de twee instrumenten. De detectiestap blijft geldig: kun je het tweede deel weghalen zonder het studieobject te verliezen? Bij beroepsgeheim en discretieplicht: nee — dan verlies je precies het onderscheid dat de student moet kennen.

**Overkoepelende begrippen** die verwijzen naar twee of meer andere begrippen (bv. WG/FT → witwassen + terrorismefinanciering) krijgen een eigen sectie met verwijzingen naar de componentbegrippen.

**Elke afkorting** die in de fiche gebruikt wordt, moet als begrip opgenomen zijn zodat er naar gelinkt kan worden.

**Engelse afkortingen**: wanneer de afkorting Engelstalig is maar de titelnaam Nederlandstalig (bv. AMLCO, UBO), voeg dan een cursieve subtitel toe met de volledige Engelse term — direct onder de heading, vóór de bodytekst:

```markdown
## 📌 Verantwoordelijke persoon (AMLCO)
*Anti-Money Laundering Compliance Officer*

De persoon die toeziet...
```

Nederlandstalige afkortingen die rechtstreeks van de naam afleiden (GA, GBA, ITAA) krijgen geen subtitel.

#### Callout: valkuil

```markdown
> [!warning]- Korte omschrijving van de valkuil
> ❌ *"De verkeerde aanname die studenten vaak maken."*
>
> De correcte uitleg van de regel, met bronverwijzing inline.
>
> 📝 *Uit voorbeeldexamen [jaar]* — of — 🤖 *AI-aanvulling*
```

- De `[!warning]`-callout heeft al een ⚠️-icoon — géén emoji herhalen in de titel
- **De titel vermeldt altijd de correcte bewering** — een student die enkel de titel leest weet onmiddellijk wat correct is, zonder de body te hoeven openen. Twee patronen:
  - **Foute overtuiging over een feit**: declaratieve zin met de correcte bewering, eventueel met negatie
    - ✓ "CBN-adviezen zijn niet juridisch bindend"
    - ✓ "Melden vereist geen zekerheid — een vermoeden volstaat"
    - ✗ "CBN-adviezen zijn juridisch bindend" — geeft foute informatie
  - **Foute handeling**: imperatief of "Men moet"-constructie
    - ✓ "Gebruik EV vóór winstverdeling bij ROE"
    - ✓ "Men moet EV vóór winstverdeling gebruiken bij ROE"
    - ✗ "EV vóór winstverdeling gebruiken bij ROE" — infinitief, te ambigu
  - **Test**: kan een student de titel lezen als een correcte instructie of correcte kennis? Ja → OK. Nee → herformuleren.
- De foutieve aanname staat als eerste regel in de body, cursief en tussen aanhalingstekens
- Daarna de correcte uitleg
- Helemaal onderaan de bronvermelding (📝 of 🤖)

#### Callout: voorbeeldvraag

Gebruik `[!question]-` genest met `[!success]-`. **Belangrijk**: voeg een lege regel in na de opening van elke callout — dat is wat Quartz nodig heeft om nesting correct te renderen.

```markdown
> [!question]- Korte vraagnaam
>
> De vraag volledig en correct geformuleerd, zoals in een examen.
>
> Juist of fout? (indien van toepassing, op een aparte regel)
>
> > [!success]- Antwoord
> >
> > **Verdict** (Juist / Fout / Ja / Nee)
> >
> > Uitleg van het correcte antwoord, rustig gespatieerd.
> >
> > *Zie: [[conceptfiche#sectie-naam|Sectienaam]]*
>
> 📝 *Uit voorbeeldexamen [jaar]* — of — 🤖 *AI-aanvulling*
```

- `[!question]-` heeft al een icoon — géén ❓ herhalen in de titel
- **Lege regel** na `> [!question]-` en na `> > [!success]-` — cruciaal voor nesting
- De **titel** is een korte naam voor de vraag (3–6 woorden)
- "Juist of fout?" staat op een **aparte regel** in de vraagbody
- Het **verdict** staat vetgedrukt op de eerste regel van het antwoord
- De **bronvermelding** (📝 of 🤖) staat na de success-callout, nog binnen de question-callout

#### Callout: in de praktijk

```markdown
> [!info]- In de praktijk
>
> Concrete situatie die helpt begrijpen wat de regel betekent.
>
> 🤖 *AI-aanvulling*
```

- De 🤖 staat **onderaan**, na de tekst — net zoals bij `[!warning]`
- Altijd gelabeld 🤖 tenzij de situatie rechtstreeks uit een bron komt
- Verduidelijkt de materie — geen nieuwe feiten introduceren

#### Sectie "Relevant voor"

De sectie die aangeeft voor welk programmaonderdeel het concept relevant is. Structuur:

```markdown
## Relevant voor

**[[X.X-naam|X.X Naam van het programmaonderdeel]]**

Taken:
- *Naam van de taak (cursief)*
  - Relevante doelstelling uit die taak

Kenniselementen:
- X.n — Omschrijving kenniselement
```

- Geen `###` voor het programmaonderdeel — enkel een **bold wikilink**
- Volgorde: eerst Taken met geneste Doelstellingen, dan Kenniselementen
- Taken letterlijk overnemen uit de programmaonderdeel-fiche
- Enkel de voor dit concept relevante Taken en Kenniselementen vermelden

## Bouwversie

Elke fiche bevat `bouwversie: N` in de frontmatter. Dit geeft aan met welke versie van het proces de fiche gebouwd is. Fiches met een lagere versie dan de huidige zijn kandidaat voor heraudit.

**Huidige versie: 2**

| Versie | Datum | Wijzigingen |
|---|---|---|
| 0 | vóór 2026-05-02 | Pre-versioning — gebouwd zonder huidige principes |
| 1 | 2026-05-02 | Eerste versie: waarom-zin verplicht in competentie-stappen; grondslag-blok collapsible met 🤖/⚖️-indicator; synoniemen als cursieve subtitel; fiche-titel = kernfenomeen; formule-variabelen betekenisvol; "(zie § X)" → klikbare link; geen hyperlinks in callout-titels; stap vanuit perspectief beroepsbeoefenaar; optionele stap = aparte stap; naam competentie verifiëren na schrijven; kennislagen (Weten/Toepassen/Integreren); Stap 2A taakdecompositie; laagcheck in verificatiestap |
| 2 | 2026-05-02 | Valkuil-titels: altijd de correcte bewering (declaratief voor feiten, imperatief voor handelingen); visueel anker verplicht bij competentie-stappen die inwerken op financiële documenten; [!info]- Concreet verplicht bij oordeel/beslissingstappen; materie-fiches: topic-secties i.p.v. vak-secties; scope-vernauwing detectiestap in §Kritische lezing; boekhoudkundige-beginselen herscoped naar algemeen niveau |

**Wanneer de versie ophogen**: bij elke wijziging aan CLAUDE.md die bestaande fiches suboptimaal maakt. Infrastructuur, geheugen en Quartz-instellingen tellen niet mee. Voeg een rij toe aan de tabel en verhoog het getal bij "Huidige versie".

**Stale fiches vinden**: `grep -rL "bouwversie" content/materie content/competenties content/programmaonderdelen` (ontbreekt veld) of `grep -r "bouwversie: 0" content/` (verouderd).

---

## Proces

### Werkprincipe

Doorloop alle stappen autonoom. Leg niets voor ter validatie — de gebruiker valideert via Stap 5 door de site te bekijken. Stel alleen een vraag bij echte inhoudelijke twijfel over wetsinhoud of bij een architectuurbeslissing die niet uit de context af te leiden is. Elke `wip`- en `draft`-markering communiceert vanzelf dat inhoud nog niet geverifieerd is.

### Infrastructuur

**Po-builder** (ad-hoc scheduled task in Claude sidebar):
1. Schrijf het PO-nummer naar `/Users/stivni/Documents/ITAA/certificaid/.po-target` (bv. `1.1`)
2. Klik "Run now" op `po-builder` in de sidebar — of spawn direct een background agent

**Voortgangsbestand** — alles over een actieve PO-build staat in `.po-voortgang-[PO].md` in de projectroot (niet in `content/`): voortgang per stap, rol-bevindingen, reconciliatie en beslissingen met redenering. Formaat:

```markdown
# PO [X.X] voortgang

## Stap 3A — [fiche-naam]
### Draft klaar
### Rolreview
**Stagiair**: ...
**QA**: ...
**Examinator**: ...
*(alle zes rollen)*
### Beslissingen
- [bevinding] → **verwerkt**: [redenering]
- [bevinding] → **uitgesteld**: [redenering]
- [bevinding] → **afgewezen**: [redenering]
### Fiche gereviseerd

## Stap 4 — Cross-fiche review
### Rolreview (Coherentie + Examinator)
### Cross-PO integratie
### Beslissingen
```

**Post-build exploratory agent** (persistent via mcp__scheduled-tasks):
- `certificaid-exploratory` — alle zes rollen in één run; leest `EXPLORATORY-coverage.md` om te bepalen welke fiches en rollen het langst niet bekeken zijn; schrijft bevindingen naar `EXPLORATORY.md`; werkt daarna `EXPLORATORY-coverage.md` bij

**`EXPLORATORY-coverage.md`** in de projectroot — coverage-overzicht: welke rol heeft welke fiche wanneer als laatste bekeken. De exploratory agent leest dit vóór elke run en richt zich op de cellen die leeg zijn of de oudste datum hebben.

```markdown
| fiche | stagiair | qa | examinator | bibliothecaris | stage-mentor | coherentie |
|---|---|---|---|---|---|---|
| continuiteitsrisico | 2026-05-01 | 2026-05-01 | — | 2026-05-01 | — | — |
| jaarrekening | — | — | — | — | — | — |
```

**`EXPLORATORY.md`** in de projectroot — post-build exploratory feedback, alle rollen door elkaar. Formaat per bevinding:
```
## [YYYY-MM-DD HH:MM] Exploratieve ronde — [fiches]

[YYYY-MM-DD HH:MM] [rol] [fiche]: [bevinding]
→ obvious fix: [wat verwerkt]
→ ⚠️ WACHT OP GEBRUIKER: [beslissing vereist — reden]
```
Tijdstip via `date '+%Y-%m-%d %H:%M'`. Obvious fixes worden autonoom verwerkt. Bevindingen gemarkeerd met `⚠️ WACHT OP GEBRUIKER` blijven staan tot de gebruiker beslist.

**Geparkeerde fiches**: wanneer een PO herzien wordt van nul, worden bestaande fiches gekopieerd naar `content/_parking-[PO]/` als vergelijkingsbasis.

### Stap 0 — TDKs correct uitlezen uit de brochure

Vóór alles: lees de officiële tekst van het programmaonderdeel uit `resources/programma.pdf` met `pdftotext` en structureer de TDKs correct. Fouten in de TDK-structuur trekken zich door naar alle koppelingen met materie en competenties.

**Hiërarchie in de brochure:**
```
Taak: [hoofdomschrijving]
  a) [subtaak]               ← dit is een SUBtaak, geen doelstelling
  b) [subtaak]
     - [doelstelling]        ← dit is een doelstelling (bullet onder taak of subtaak)
     - [doelstelling]
Kenniselementen:
  I. [hoofdgroep]
     A. [subgroep]
        1. [kenniselement]
```

**Werkwijze:**
1. Gebruik `pdftotext resources/programma.pdf -` en grep op het programmaonderdeelnummer
2. Kopieer de ruwe tekst en onderscheid: Taken → Subtaken (a/b/c) → Doelstellingen (bullets) → Kenniselementen (genummerd)
3. Structureer de fiche met `### Taak:` voor hoofdtaken, en geneste `#### Subtaak:` voor a/b/c-items — NIET als doelstellingen
4. Ga door naar Stap 1 met de gestructureerde TDKs

### Stap 1 — Programmaonderdeel activeren
1. Open `content/programmaonderdelen/X.X-naam.md`
2. Verwijder `verborgen` uit de tags → fiche is zichtbaar in de Explorer

### Stap 2A — Taakdecompositie

Per taak in de programmaonderdeel-fiche: bepaal welke competenties en materie nodig zijn.

**Drie bronnen voor competentie-identificatie:**
- **Taken en doelstellingen**: wat moet de student kunnen *doen*? Elke taak die een aparte aanpak vereist, is een competentie-kandidaat.
- **Voorbeeldexamens**: welke vraagtypen verschijnen in `resources/voorbeeldexamens/`? Elk distinct vraagtype toont direct welke techniek getoetst wordt. Gebruik `pdftotext` om alle examens te doorzoeken.
- **Kenniselementen**: zijn er technieken impliciet verondersteld die de taken niet expliciet noemen?

**Redeneerlogica** — per taak/subtaak:
1. "Wat moet de student kunnen *doen*?" → competentie-kandidaat
2. "Is dit in isolatie uit te voeren in de praktijk?" → ja: eigen fiche; nee: sub-stap in een andere competentie
3. "Bestaat deze competentie al — ook voor een ander vak?" → ja: hergebruiken; nee: nieuwe fiche
4. "Welke materie-bouwstenen heeft deze competentie nodig?" → noteren als vereiste materie (input voor Stap 2B)

Schrijf de geïdentificeerde competentie-links **direct in de vakfiche** bij de bijhorende taak: `- → [[bestandsnaam|Naam]]`. Als de fiche nog niet bestaat: gebruik de geplande bestandsnaam met `*(⚠️ aan te maken)*`.

**Kwaliteitscheck vóór Stap 2B:**
- Zijn **alle** taken én subtaken doorlopen — ook de minder prominente?
- Is elke **doelstelling** (niet alleen elke taak) gelezen als kandidaat-competentie? Een doelstelling levert niet automatisch een aparte competentie op — maar elke doelstelling is een aanwijzing. Als een doelstelling zelfstandig toetsbaar is én een andere aanpak vereist dan de andere doelstellingen onder dezelfde taak, dan is het een eigen competentie.
- Dekt de lijst de vraagtypen die in de voorbeeldexamens voorkomen voor dit vak?
- Zijn er technieken impliciet verondersteld in de kenniselementen die nog geen competentie hebben?
- Zijn de competenties op de juiste granulariteit? Geen te brede ("alles over jaarrekeningen") en geen te smalle ("bereken één specifieke ratio")?
- Is elke competentie gelinkt aan de materie-bouwstenen die ze nodig heeft?
- Zijn er competenties die ook voor een ander vak relevant zijn — en dus gedeeld moeten worden?
- Is elk kenniselement op zijn **hiërarchische positie** bekeken? Een subitem van "ratio's" is zelden een eigen competentie — het is materie die door een bestaande competentie gebruikt wordt.

### Stap 2B — Materie en competenties bepalen
1. Bepaal welke materie-bouwstenen (concepten/fenomenen) nodig zijn — zie §Concepten identificeren
2. Overloop de geïdentificeerde competenties en materies op ontbrekende impliciete concepten
3. Controleer op duplicaten met bestaande materie-fiches en competentie-fiches
4. Schrijf de geïdentificeerde materie-links **direct in de vakfiche** bij de bijhorende kenniselementen. Items zonder fiche: laat staan als `*(⚠️ materie aan te maken)*`

**Bronverificatie per nieuwe competentie** — zoek voor elke nieuw te maken competentie-fiche naar een gezaghebbende bron die de competentie als professionele activiteit beschrijft:

| Zoekstap | Bron | Wat je zoekt |
|---|---|---|
| 1 | `resources/normen/INDEX.md` → bestand | Beschrijft een ITAA-norm deze procedure? |
| 2 | `resources/adviezen/INDEX.md` → bestand | Beschrijft een CBN-advies de aanpak? |
| 3 | `resources/wetteksten/INDEX.md` → bestand | Legt een wettekst de stappen vast? |
| 4 | Online: itaa.be, cnc-cbn.be, nbb.be | Publicaties, omzendbrieven, sectoranalyses |
| 5 | Erkende handboeken | Academische of beroepspublicaties |
| 6 | Geen bron gevonden | Procedure is analytische conventie → label 🤖, vermeld `procedure-grondslag: analytische praktijk` in frontmatter |

Het resultaat van deze zoektocht gaat in een zichtbaar `> [!info] Grondslag van deze werkwijze`-blok direct na de intro van de competentie-fiche. Dit blok is de basis voor de bronvermelding per stap in Stap 3B en is zichtbaar voor de student.

Ga daarna naar Stap 3.

### Stap 3A — Per concept: materie-fiche aanmaken

Voor elk nieuw concept, in deze volgorde — alles in één doorloop, geen tussenpauzes:

1. **Materie** — begrippen, principes, verplichtingen, procedures — volledig brongebonden
   - Gebruik het template materie-fiche
   - **Kritische lezing achteraf** (zie §Kritische lezing)
2. **Valkuilen + praktijkvoorbeelden** — mag 🤖 als gelabeld; voeg bij elke berekening of procedure minstens één concreet doorgewerkt voorbeeld toe
3. **Voorbeeldvragen** — raadpleeg eerst `resources/voorbeeldexamens/`; gebruik echte vragen (📝) prioritair; vul aan met 🤖
   - **Verplichte eerste stap**: lees `resources/voorbeeldexamens/INDEX.md` — welke examens bevatten vragen over dit PO of concept? Lees daarna de relevante PDF's via `pdftotext`.
   - Echte examenvragen worden letterlijk overgenomen en gelabeld als `📝 *Uit voorbeeldexamen [jaar]*`
   - Vul aan met 🤖-vragen voor concepten zonder examenmateriaal
4. **Hyperlinks** — semantische doorlezing voor links (zie §Semantische hyperlinkdoorlezing)
5. **Rolreview** — spawn alle zes rollen parallel op de volledige fiche-draft; verwerk hun bevindingen autonoom; log beslissingen in `.po-voortgang-[PO].md`
   - Elke rol leest de fiche vanuit zijn eigen mindset (zie §Reviewrollen)
   - Conflicterende bevindingen worden autonoom gewikt — redenering wordt gelogd, nooit gewacht
   - Reviseer de fiche op basis van verwerkte beslissingen vóór je doorgaat naar de volgende fiche

**Ontdekking tijdens Stap 3**: als tijdens het schrijven van een fiche een concept of competentie opduikt die nog niet in de vakfiche staat, voeg het dan direct toe aan de vakfiche (als `*(⚠️ aan te maken)*`) en aan de werklijs voor Stap 3. Blokkeer niet — noteer en ga door.

### Stap 3B — Per competentie: competentie-fiche aanmaken

Voor elke nieuwe competentie, in deze volgorde — alles in één doorloop, geen tussenpauzes:

1. **Aanbevolen werkwijze** — stappen met staptypes, normale situatie eerst, uitzonderingen inline — volledig brongebonden voor juridische beslissingen; 🤖 voor analytische heuristieken
   - Gebruik het template competentie-fiche
   - Bepaal de volgorde via "Nodig/Levert op" per stap
2. **Valkuilen** — inline als `[!warning]` bij de relevante stap
3. **Voorbeeldvragen** — zelfde aanpak als materie-fiches; raadpleeg eerst `resources/voorbeeldexamens/`
4. **Links** — elke stap verwijst naar de juiste materie-sectie of andere competentie
5. **Rolreview** — zelfde werkwijze als Stap 3A: spawn alle zes rollen parallel, verwerk autonoom, log in `.po-voortgang-[PO].md`

**Kwaliteitscheck na schrijven** — volgt rechtstreeks uit de §Regels hierboven:
- Heeft elke stap een 📥 én een 📤? Is de uitkomst concreet genoeg?
- Zijn er stappen die output gebruiken van een latere stap? (verkeerde volgorde)
- Is het "Motiveren op het examen"-blok aanwezig en volledig?
- Is er minstens één concreet voorbeeld met Situatie / Conclusie / Grondslag / Redenering?

### Stap 4 — Programmaonderdeel-fiche afwerken
De inline competentie-links (bij taken) en materie-links (bij kenniselementen) zijn al toegevoegd in Stap 2A/2B. Stap 4 finaliseert de aggregatielijsten en controleert volledigheid:

1. Controleer en completeer de `→` competentie-links bij alle taken (placeholders `⚠️ aan te maken` resolveren na Stap 3B)
2. Controleer en completeer de materie-links bij alle kenniselementen (placeholders `⚠️ materie aan te maken` resolveren na Stap 3A)
3. Vul "Relevante competenties" in — als aggregatie van alle `→` links in de taken-sectie, in leeslogische volgorde (basiscompetenties vóór samengestelde)
4. Vul "Relevante materie" in — als aggregatie van alle materie-links in de kenniselementen-sectie, in leeslogische volgorde (begrippen vóór toepassingen, wetgeving vóór analyse)
5. **Volledigheidscheck** (zie ook §Verificatiestap voor de gedetailleerde versie):
   - Is elke taak gekoppeld aan minstens één competentie-fiche?
   - Zijn alle kenniselementen gelinkt — geen bullet zonder link?
   - Kan een student die enkel de aggregatielijsten doorloopt alle examenstof zien?
   - Staan competenties in leeslogische volgorde (basiscompetenties vóór samengestelde)?
6. **Cross-fiche rolreview** — spawn Coherentie-reviewer en Examinator op alle nieuw gemaakte fiches samen:
   - Coherentie-reviewer: spreken de fiches elkaar niet tegen? zijn drempelwaarden en definities consistent?
   - Examinator: zijn er integratievragen mogelijk die meerdere fiches combineren?
   - Cross-PO integratie: hoe integreert dit PO met andere POs die al bestaan? linken de fiches correct naar en vanuit andere programmaonderdeel-fiches?
   - Bevindingen + beslissingen → `.po-voortgang-[PO].md` onder `## Stap 4 — Cross-fiche review`

> Deze check is repetitief genoeg om later als geautomatiseerde routinecontrole (agent) te draaien — bijv. wekelijks over alle vakfiches.

### Stap 5 — Validatie door de gebruiker
- Gebruiker valideert materie → `status: draft` blijft, `wip`-tag blijft
- Wanneer gebruiker volledig tevreden is: `wip`-tag verwijderen, `status: geverifieerd`

### Reviewrollen

Elke fiche wordt beoordeeld vanuit zes brillen. Elke rol vangt een ander type probleem op.

| Rol | Mindset | Vangt op | Detailsectie |
|---|---|---|---|
| **Stagiair** | "Is dit duidelijk en concreet?" | Te abstracte uitleg, ontbrekende voorbeelden | §Student-perspectief review, §Kritische lezing |
| **QA-persoon** | "Klopt dit met de bronnen?" | Feitelijke fouten, ontbrekende bronverwijzingen, tegenstrijdige beweringen | §Wettekstverificatie |
| **Examinator** | "Hoe toets ik dit echt?" | Ontbrekende vraagvarianten, ongeteste integratieniveaus | §Examinator-review |
| **Bibliothecaris** | "Zijn alle links gelegd?" | Ontbrekende wikilinks, polyseme termen zonder kwalificatie | §Semantische hyperlinkdoorlezing |
| **Stage-mentor** | "Wat doet de praktijk anders?" | Norm vs. praktijkkloof, ongeschreven conventies | §Stage-mentor review |
| **Coherentie-reviewer** | "Spreken fiches elkaar niet tegen?" | Cross-fiche inconsistenties, conflicterende drempelwaarden | §Coherentie-review |

**Modus 1 — tijdens de build (synchroon, Stap 3A/3B/4)**
- Alle zes rollen draaien parallel op de fiche-draft
- Bevindingen worden autonoom verwerkt — nooit wachten op de gebruiker
- Conflicterende rol-feedback wordt autonoom gewikt; redenering gelogd in `.po-voortgang-[PO].md`
- De fiche wordt gereviseerd vóór de build verdergaat

**Modus 2 — post-build exploratory (asynchroon)**
- Agents wandelen door bestaande content zonder specifieke opdracht
- Obvious fixes → autonoom verwerkt
- Grotere beslissingen → geflagd als `⚠️ WACHT OP GEBRUIKER` in `EXPLORATORY.md`; de gebruiker beslist wanneer het uitkomt

### Semantische hyperlinkdoorlezing

Lees elke zin van de fiche opnieuw — niet om fouten te zoeken, maar om te vragen: **"heeft deze passage betrekking op iets dat ergens een anker heeft?"**

Dit is een semantische lezing, geen keyword-zoekactie. Een passage kan conceptueel verwijzen naar een ander concept zonder het woord letterlijk te gebruiken. Voorbeelden van wat je zoekt:

| Type passage | Vraag die je stelt |
|---|---|
| Een begrip wordt gebruikt | Heeft dit begrip een eigen `##`-sectie in een fiche? → link naar dat anker |
| Een verplichting wordt beschreven | Heeft die verplichting een eigen sectie? → link |
| Een procedure of sanctie wordt aangehaald | Staat die ergens uitgelegd? → link |
| Een uitzondering verwijst impliciet naar een ander concept | Bv. "het melden schendt het beroepsgeheim niet" → link naar beroepsgeheim |
| Een opsomming bevat termen die elk een eigen sectie hebben | Elk item afzonderlijk linken |
| Callout-tekst (valkuilen, voorbeeldvragen) verwijst naar begrippen | Ook in callouts worden links verwacht |

**Werkwijze:** doorloop de fiche sectie per sectie. Per zin: stel de vraag. Voeg de link toe op de meest precieze plek — bij voorkeur het anker van de sectie, niet het algemene fiche-niveau.

**Elk conceptwoord krijgt een link** — ook in tabellen, ook in de intro, ook in callouts. Geen uitzondering voor "bekende" termen: als iemand het woord niet kent, moet ze kunnen doorklikken.

**Navigeer naar het hoogste semantisch niveau**: link niet naar de naakte definitie van een term als er een relevantere sectie bestaat. "Nettoactief nadert drempel NV" → link naar het patroon of de procedure die dat behandelt, niet naar de definitie van "nettoactief". Vraag: *waarnaar wil een lezer die dit woord niet kent navigeren om het meest te leren?*

**Polyseme termen altijd kwalificeren** — woorden die in meerdere contexten een andere betekenis hebben, worden altijd voorzien van een kwalificatie of een disambiguerende link. Voorbeelden:
- "meldingsplicht" → "meldingsplicht [[continuiteitsrisico#-meldingsplicht-van-de-beroepsbeoefenaar|bij continuïteitsrisico]]" vs. "[[antiwitwaswetgeving#-meldingsplicht|meldingsplicht]] (AWW)"
- "verslag van de commissaris" → altijd vermelden in welk type opdracht
- "bijzondere volmacht" → kwalificeer de context

Wanneer de context de betekenis al ondubbelzinnig maakt (de hele fiche gaat over continuiteitsrisico), volstaat een duidelijke link. Wanneer er risico op verwarring is (bv. meerdere "meldingsplichten" in hetzelfde domein), voeg een expliciete kwalificatie toe aan de tekst zelf.

**Links altijd inline op het conceptwoord** — nooit als losstaande verwijzing achteraan:
- ✓ `... past de [[financiele-ratios#-schema-beperkingen|schema-beperkingen]] toe`
- ✗ `... zie [[financiele-ratios#-schema-beperkingen|Schema-beperkingen]] voor het overzicht`
- ✗ `Formules en betekenis: [[balansaggregaten#-balansaggregaten|Balansaggregaten]]`
- ✗ `Werkwijze: [[jaarrekening-herwerken]]`

Als de formulering geen natuurlijke plek voor de link biedt: herformuleer de zin zodat het conceptwoord erin voorkomt. Alleen als ook dat niet lukt, mag een "zie [[...]]"-verwijzing als last resort.

**Geen grepping** — een keyword-zoekopdracht mist passages die conceptueel verwijzen zonder letterlijk de term te gebruiken. De enige betrouwbare methode is lezen.

**Geldt voor alle fichetypes**: materie-fiches, competentie-fiches én programmaonderdeel-fiches. In competentie-fiches verwijst elke stap naar de juiste materie-sectie of andere competentie. In programmaonderdeel-fiches linkt elke taak naar de bijhorende competentie-fiche.

### Wettekstverificatie

Voordat je tevreden bent met een sectie, stel je je eigen samenvatting actief in vraag door terug te gaan naar de wettekst. Stelregel: **een samenvatting is een interpretatie — de wettekst is de enige zekerheid.**

Vragen die je jezelf stelt bij elke bewering, opsomming of absoluut klinkende uitspraak:

| Wat je hebt geschreven | Vraag die je stelt |
|---|---|
| "Er zijn 4 uitzonderingen" | Zijn het er echt 4? Lees het artikel na en tel |
| "altijd", "nooit", "in alle gevallen" | Bestaat er echt geen enkele uitzondering? |
| "verboden" | Absoluut verboden, of enkel in bepaalde omstandigheden? |
| "verplicht" | Altijd, of enkel bij bepaalde drempels, tijdstippen of situaties? |
| "De beroepsbeoefenaar moet X melden" | Aan wie precies? Binnen welke termijn? |
| "Dit valt onder dezelfde noemer als Y" | Staan ze in hetzelfde artikel? Of in aparte artikelen met een andere grondslag? |
| Een opsomming van 3 items | Is de opsomming exhaustief of enkel een opsomming van voorbeelden? |
| "tenzij de cliënt toestemming geeft" | Geldt die uitzondering onbeperkt, of enkel voor een deel van de informatie? |

Wanneer de verificatie iets nieuws oplevert — een vijfde uitzondering, een nuance die je gemist had, een verschil in grondslag — volgt altijd:

1. **Hertaling**: schrijf de nieuwe informatie in begrijpbare taal. Elk juridisch begrip dat een student zonder juridische achtergrond niet snapt, krijgt een uitleg in gewone woorden. "Over zijn hoedanigheid" → "over jou als beroepsbeoefenaar". "Bestuursrechtelijke procedure" → "overheidsprocedure die jouw statuut raakt".

2. **Praktijkvoorbeeld**: voeg meteen een `[!info]- In de praktijk` blok toe. Een nuance die alleen in abstracte termen beschreven staat, beklijft niet. Een concrete situatie maakt ze onthoudbaar.

### Student-perspectief review

Na het schrijven of aanpassen van een fiche, doorloop ze als een stagiair die de stof voor het eerst ziet: iemand die de theorie begrijpt maar de toepassing nog niet heeft gezien. Stel de volgende vragen bij elke sectie:

| Signaal | Vraag die de stagiair stelt |
|---|---|
| Procedure of begrip zonder concreet geval | "Maar hoe ziet dit er in de praktijk uit?" |
| Vergelijkingstabel zonder voorbeeld van beide situaties | "Kan je een vennootschap noemen waarbij de ene én de andere kant geldt?" |
| Signaallijst zonder cijfercontext | "Hoe zie ik dit in de balans of resultatenrekening?" |
| Berekeningsstap zonder doorgewerkt cijfer | "Kan je dit eens uitrekenen met een echt getal?" |
| Abstracte definitie van een aggregaat of ratio | "Wat betekent dit voor een concrete onderneming?" |

**Minimale aanvullingen per fichecomponent**:
- Elke 📌 begrip of ⚖️ principe met meerdere toestanden: minstens één `[!info]- In de praktijk`-blok
- Elke 📋 procedure of berekening: minstens één cijfer- of situatievoorbeeld
- Balansen, resultatenrekeningen of andere financiële schema's: altijd in een `code`-blok — nooit als proza
- Elke stap in een competentie die over cijfers gaat: minstens één getal in de tekst of het voorbeeld

**Schematische voorstellingen** zijn geen versiering — ze maken een abstracte structuur direct zichtbaar. Gebruik ze wanneer:
- Een balans- of resultatenrekeninglevel beschreven wordt
- Een procedure meerdere stappen heeft met een duidelijke volgorde (tijdslijn of stappendiagram in `code`)
- Een vergelijking twee scenario's naast elkaar zet

Wanneer je de review uitvoert en een lacune vindt: vul die meteen in, label met 🤖 als er geen bronvermelding is, en ga verder. Niet rapporteren en wachten — oplossen.

### Examinator-review

Bekijk de fiche als iemand die vragen opstelt voor het bekwaamheidsexamen. Doel: niet controleren of de inhoud correct is (QA-rol), maar of de fiche écht bekwaamheid toetst en of er blinde vlekken zijn die een overhaaste student zouden misleiden.

| Wat je controleert | Vraag die je stelt |
|---|---|
| Niveau van de voorbeeldvragen | Is er minstens één vraag per niveau (weten / toepassen / integratie)? |
| Conceptbotsing | Is er een vraag waarbij twee concepten of uitzonderingen met elkaar in conflict komen? |
| Overhaaste student | Welke verkeerde aanname zou een bekwame-maar-haastige student maken? Staat die als valkuil in de fiche? |
| Onderscheid gelijkaardige concepten | Is er een vraag die het verschil test tussen dit concept en een naburig concept? |
| Integratie-casus | Is er minstens één scenario-vraag waarbij de student moet redeneren, niet opzoeken? |
| Dekking kenniselementen | Dekt de set voorbeeldvragen alle TDKs die naar deze fiche linken? |

**Werkwijze:**
1. Lees `resources/voorbeeldexamens/INDEX.md` — zijn er echte vragen over dit concept?
2. Neem bestaande vragen als basis en maak varianten die andere aspecten testen
3. Stel minstens één vraag waarbij de student iets moet *uitleggen* of *adviseren*, niet alleen aanvinken
4. Voeg toe als `[!question]-` callout met `📝` of `🤖` label

**Signaal dat de examinator-laag ontbreekt**: alle voorbeeldvragen zijn "juist/fout" of definitievragen zonder toepassing of integratie.

### Stage-mentor review

Bekijk de fiche als een ervaren beroepsbeoefenaar die de stagepraktijk kent. De norm zegt X — maar wat doet iedereen in de praktijk? Wat staat nergens geschreven maar is toch standaard?

| Wat je controleert | Vraag die je stelt |
|---|---|
| Norm vs. praktijk | Beschrijft de fiche enkel wat de norm/wet zegt, of ook hoe het in de praktijk uitpakt? |
| Ongeschreven conventies | Zijn er standaardpraktijken die "iedereen kent" maar die nergens gedocumenteerd staan? |
| Contextafhankelijkheid | Geldt de werkwijze voor alle kantoorgroottes en cliëntprofielen, of enkel voor bepaalde contexten? |
| Praktische valkuilen | Zijn er fouten die beginners systematisch maken — niet uit onwetendheid maar uit gewoonte vanuit een andere context? |

**Werkwijze:**
- Voeg praktijkinput toe als `[!info]- In de praktijk` blok, altijd gelabeld 🤖
- Als norm en praktijk divergeren: vermeld dat expliciet — "De norm vereist X; in de praktijk wordt Y toegepast omdat Z"
- Nooit als bronloze bewering — altijd als gelabelde aanvulling

**Signaal dat de stage-mentor-laag ontbreekt**: de fiche leest als een wettekst-samenvatting zonder enig concreet praktijkgevoel.

### Coherentie-review

Bekijk de fiche niet op zichzelf maar in relatie tot andere fiches. De coherentie-reviewer controleert of fiches die naar elkaar verwijzen ook inhoudelijk consistent zijn — niet alleen qua links (bibliothecaris) of qua bronnen (QA).

| Wat je controleert | Vraag die je stelt |
|---|---|
| Consistentie met gelinkte fiches | Zegt deze fiche over concept X hetzelfde als de fiche die concept X definieert? |
| Conflicterende beweringen | Als fiche A "altijd verplicht" zegt maar fiche B een uitzondering beschrijft voor dezelfde situatie — staat dat conflict ergens vermeld? |
| Drempelwaarden en tarieven | Zijn bedragen en drempels consistent over alle fiches die ernaar verwijzen? |
| Competentie ↔ materie | Baseert de competentie-fiche een stap op materie die in de materie-fiche ook zo beschreven staat? |
| Veronderstelde kennis | Veronderstelt een fiche kennis die in de gelinkte materie-fiche niet of anders beschreven staat? |

**Werkwijze:**
1. Selecteer de gelinkte fiches via de wikilinks in de fiche
2. Lees de overeenkomende secties in beide fiches
3. Bij inconsistentie: vermeld beide versies, geef aan welke bron hogere rang heeft (zie §Tegenstrijdige bronnen), markeer als `⚠️ te verifiëren`
4. Bij verouderde veronderstelling in een competentie-fiche: pas de stap aan zodat ze de huidige materie-fiche weerspiegelt

**Signaal dat coherentie-review nodig is**: meerdere fiches zijn recent aangepast en de downstream fiches zijn nog niet bijgewerkt.

### Kritische lezing

Lees elke zin door vanuit het standpunt van een student die de stof voor het eerst ziet. Stelregel: **als een student bij het lezen een vraag heeft die de tekst niet beantwoordt, is de zin onvolledig.**

Typische signaalzinnen die te vaag zijn:

| Problematische formulering | Vraag die de student stelt |
|---|---|
| "De titels zijn wettelijk beschermd" | Welke titels exact? Allemaal of enkel de beschermde? |
| "Ze mogen de activiteiten van art. X uitoefenen" | Welke activiteiten zijn dat dan? Moet ik zelf in de wet kijken? |
| "Dit is verboden" | Wat precies? Onder welke voorwaarden? Zijn er uitzonderingen? |
| "Er zijn bepaalde voorwaarden" | Welke? Hoeveel? |
| "De bevoegde autoriteit" | Welke autoriteit? |
| "In sommige gevallen" | In welke gevallen precies? |
| "Herstructureer de balans naar een functionele indeling" | Welke rubrieken tel ik bij elkaar op? Wat is de NBB-code? |
| "Groepeer de vlottende activa" | Welke posten vallen daaronder? Is rubriek X erbij of niet? |

De oplossing is altijd: de informatie meteen in de tekst opnemen, niet doorverwijzen naar een artikel zonder de inhoud te geven. De student heeft ITAA-LEX bij zich maar moet weten **wat** hij moet opzoeken en **waarom** — niet de interpretatie zelf moeten doen.

**Controleer ook de structuur** — controleer of de §Schrijfstijlregels gevolgd zijn. Aandachtspunten die makkelijk gemist worden:

| Structuurprobleem | Correctie |
|---|---|
| Gevolg vóór oorzaak | "X leidt tot Y", niet "Y wordt opgelegd wanneer X" |
| Passieve zin verbergt de actor | Herschrijf actief: wie doet wat? |
| Vergelijking staat vóór de begrippen | Tabel pas na introductie van alle betrokken concepten |
| Eén sectie over twee ongerelateerde thema's | Opsplitsen in twee secties |
| Abstract principe wordt geframed als instrument-specifiek | Bij elke fiche die een algemeen principe beschrijft: stel je de vraag "Geldt dit ook buiten de context van dit instrument?" Als ja → scope de intro naar het algemene niveau en verwijs voor de instrumentgebonden toepassing naar de instrumentfiche. Voorbeeld: boekhoudkundige beginselen gelden voor de hele boekhouding, niet alleen voor de jaarrekening. |

### Feedback als verbeterimpuls

Wanneer de gebruiker inhoudelijke feedback geeft — iets was fout, onvolledig, te vaag of ontbrak — stel jezelf onmiddellijk de vraag: **"Hoe had ik dit zelf kunnen detecteren?"**

Als er een antwoord is op die vraag, voeg je een concrete verificatiestap toe in de meest relevante sectie van CLAUDE.md:
- Een denkfout over een begrip → regel in §Kritische lezing
- Een bron die ontbrak of verkeerd geclassificeerd was → regel in §Wettekstverificatie of §Bronintegriteit
- Een structuurprobleem in een fiche → regel in §Kritische lezing structuurtabel
- Een granulariteits- of classificatiefout bij competenties → kwaliteitscheck in §Stap 3B
- Een ontbrekend concept dat tijdens Stap 2A/2B had moeten opduiken → kwaliteitscheck in §Stap 2A of §Stap 2B

Doel: de feedback van vandaag wordt de zelfcheck van morgen. Dit houdt de verificatiestappen actueel en voorkomt dat dezelfde fout zich herhaalt.

## Technisch

### Mappenstructuur
```
certificaid/
├── CLAUDE.md
├── EXPLORATORY.md               # Post-build exploratory bevindingen (alle rollen, met escalatiemarkering)
├── EXPLORATORY-coverage.md      # Coverage-overzicht: welke rol heeft welke fiche wanneer bekeken
├── .po-voortgang-[PO].md        # Per actieve PO-build: voortgang, rolreviews, beslissingen
├── .po-target                   # Actief PO-nummer voor po-builder
├── quartz.config.ts        # Quartz-configuratie (titel, plugins, baseUrl)
├── quartz.layout.ts        # Quartz-layout (sidebar, zoeken, backlinks)
├── quartz/                 # gitignored — copy van node_modules na `npm install`
├── package.json            # devDependency: @jackyzha0/quartz van GitHub
├── .gitignore
├── .github/
│   └── workflows/
│       └── deploy.yml      # Build & deploy naar GitHub Pages bij push op main
├── content/
│   ├── index.md
│   ├── programmaonderdelen/ # Catalogus: per vak welke competenties + materie + synthese-oefeningen
│   ├── competenties/        # Technieken: aanbevolen werkwijze per toetsbaar vaardigheidtype
│   ├── materie/             # Kennis: één concept/fenomeen per fiche
│   └── bronnen/             # Primaire bronnen als doorzoekbare content
│       ├── wetteksten/      # Wetgeving — primaire bron voor materie
│       │   ├── index.md     # Overzicht alle secties met status en links
│       │   ├── XVII-antiwitwaswet.md
│       │   ├── XXI-wet-itaa.md
│       │   ├── XIII-wer/    # WER gesplitst per Boek
│       │   └── ...          # Overige secties (✅ beschikbaar of ⏳ placeholder)
│       ├── normen/          # ITAA-normen als gestructureerde markdown
│       └── adviezen/        # CBN-adviezen (samenvatting; raw PDFs in resources/adviezen/raw/)
├── tools/
└── resources/
    ├── ITAA_Lex_Index.xlsx      # Index van alle ITAA-LEX secties (editie 11 juli 2025)
    ├── programma.pdf            # ITAA-brochure bekwaamheidsexamen (gitignored)
    ├── wetteksten/
    │   ├── *.md                 # Gestructureerde wetteksten — primaire referentie (zie §Lokale wetteksten)
    │   ├── status.md            # Download-status en todo voor ontbrekende wetteksten
    │   └── raw/                 # Gitignored: ruwe PDFs en tussentijdse .txt-bestanden
    ├── normen/
    │   ├── *.md                 # ITAA-normen als gestructureerde markdown
    │   └── raw/                 # Gitignored: bron-PDFs
    └── voorbeeldexamens/        # Gitignored: PDF's van vroegere examens
```

### Publicatie
- Site: https://stivni.github.io/certificaid
- Lokaal testen: `npm install && npm run dev` → http://localhost:8080
- Deploy triggert automatisch bij wijzigingen in `content/`, `quartz.config.ts` of `quartz.layout.ts`

### Quartz

Bij elke wijziging aan Quartz layout, componenten of styling:
1. Controleer https://quartz.jzhao.xyz/layout voor beschikbare componenten en opties
2. Controleer de broncode in `quartz/components/` voor precieze API
3. Pas daarna pas `quartz.layout.ts` of `quartz/styles/custom.scss` aan

Quartz heeft ingebouwde wrappers zoals `Component.Flex()` die CSS-hacks overbodig maken.
