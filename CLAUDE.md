# Certificaid

Kennisbank voor het ITAA bekwaamheidsexamen (gecertificeerd accountant / gecertificeerd belastingadviseur).

## Doel
Gestructureerde conceptfiches die:
- Georganiseerd zijn rond reële fenomenen en coherente studieonderwerpen — niet rond vakken of wetsartikelen
- Vakoverschrijdend zijn (één concept kan in meerdere vakken voorkomen)
- Terugkoppelen naar de taken, doelstellingen en kenniselementen uit de officiële ITAA-brochure
- Alleen verifieerbare informatie bevatten (bronvermelding verplicht)

## Structuur
```
certificaid/
├── CLAUDE.md
├── quartz.config.ts        # Quartz-configuratie (titel, plugins, baseUrl)
├── quartz.layout.ts        # Quartz-layout (sidebar, zoeken, backlinks)
├── quartz/                 # gitignored — symlink naar node_modules na `npm install`
├── package.json            # devDependency: @jackyzha0/quartz van GitHub
├── .gitignore
├── .github/
│   └── workflows/
│       └── deploy.yml      # Build & deploy naar GitHub Pages bij push op main
├── content/
│   ├── index.md
│   ├── concepten/          # Één .md per concept, zie conventie hieronder
│   ├── vakken/             # Één .md per vak (1.1 t.e.m. 4.0)
│   └── itaa-lex/           # Proxy per ITAA-LEX sectie — alleen secties die effectief gebruikt worden
├── tools/
└── resources/              # Bronmateriaal (bv. ITAA-brochure PDF, ITAA_LEX_index.xlsx)
```

### Publicatie
- Site: https://stivni.github.io/certificaid
- Lokaal testen: `npm install && npm run dev` → http://localhost:8080
- Deploy triggert automatisch bij wijzigingen in `content/`, `quartz.config.ts` of `quartz.layout.ts`

## Absolute regel: geen hallucinaties
Dit is de belangrijkste regel van het hele project.

- Elk feit, elke definitie, elk wetsartikel moet traceerbaar zijn naar een
  concrete bron
- Schrijf NOOIT iets over wetsinhoud zonder een bronverwijzing
- Als je een concept niet met zekerheid kunt onderbouwen vanuit een bron:
  zeg dat expliciet, vul het veld NIET in, en markeer het als `⚠️ te verifiëren`
- Liever een leeg veld dan een onzeker feit

## Bronhiërarchie (van meest naar minst gezaghebbend)
1. Officiële wetteksten op [ejustice.just.fgov.be](http://ejustice.just.fgov.be) (geconsolideerde versies)
2. [Fisconet.be](http://Fisconet.be) (WIB92, WBTW, ...)
3. CBN-adviezen op [cnc-cbn.be](http://cnc-cbn.be)
4. ITAA-normen op [itaa.be](http://itaa.be)
5. NBB-documentatie op [nbb.be](http://nbb.be)
6. De ITAA-brochure zelf (resources/programma.pdf) — voor structuur en leerdoelen
7. Online resources, waarvan je dan de juistheid nog moet verifiëren met bovenstaande bronnen

## Examensituatie — wat de student bij heeft

Tijdens het bekwaamheidsexamen mag de student gebruiken:
- **ITAA-LEX** — de volledige wettekstenbundel (genummerde secties, paginanummers)
- **Cijferzakboekje** — geactualiseerde/geïndexeerde bedragen, tarieven en drempelwaarden

**Gevolg voor de fiches**: exacte bedragen en tarieven hoeven niet uit het hoofd gekend te zijn — de student kan ze opzoeken. Wat wél getoetst wordt en dus centraal staat in onze fiches:
- Het **concept** begrijpen: wanneer is iets van toepassing, waarom, op wie?
- **Weten waar** je iets terugvindt in ITAA-LEX (sectie + onderwerp)
- **Randgevallen en uitzonderingen** herkennen — die staan minder prominent en worden specifiek bevraagd
- **Conceptuele valkuilen**: niet "verkeerd bedrag", maar "verkeerde redenering" — bv. denken dat een omweg via het postkantoor de contantengrens omzeilt

Valkuilen in de fiches gaan dus over **verkeerde concepten**, niet over verkeerde cijfers.

## Doelpubliek en schrijfstijl
De conceptfiches zijn studiemateriaal voor mensen die al iets van de boekhoudkundige en fiscale wereld kennen (bv. via opleiding of praktijk), maar geen juristen zijn.

- **Menselijke, heldere taal** — geen legalese, wel precies
- **Niet alles is gekend** — leg ook "bekende" begrippen kort uit, mensen vergeten
- **Afkortingen** — eerste vermelding altijd voluit: "Besloten Vennootschap (BV)"
- **Wikilinks** — elk concept dat elders een fiche heeft, krijgt een `[[link]]` bij elke vermelding
- **Vakken in numerieke volgorde** — 1.2 voor 2.3 voor 3.1 enz.
- **Backlinks** — elke conceptfiche bevat een "Relevant voor" sectie met links naar de vakfiches
- **Leerstof vs. context** — elk concept wordt getoetst aan de taken, doelstellingen en kenniselementen van de vakfiche; wat niet direct geëxamineerd wordt, krijgt het label `context` in de frontmatter, niet `leerstof`
- **Exacte bedragen**: vermeld ze ter referentie met bronverwijzing naar ITAA-LEX of cijferzakboekje, maar leg de nadruk op het concept erachter — niet op het getal zelf

## Wat is een concept?

Een concept is de **kleinste coherente eenheid die een student als één geheel moet begrijpen**. De grens ligt daar waar twee stukken kennis onafhankelijk van elkaar bestudeerbaar zijn — dan zijn het twee concepten. Als kennis over het ene zinloos is zonder het andere — dan is het één concept.

**Concepten worden gedefinieerd door het reële fenomeen of studieonderwerp**, niet door de juridische structuur of de vakindeling:
- ✓ "autoleasing" (boekhoudkundig + fiscaal + advies samen)
- ✓ "antiwitwaswetgeving" (scope + verplichtingen samen — niet te splitsen)
- ✓ "deontologische beginselen" (de 7 principes als geheel)
- ✗ niet: "AWW art. 47" of "kenniselement D.6"

**Grootte**: zo groot als nodig. Splitsen alleen als twee ideeën écht onafhankelijk van elkaar voorkomen én bestudeerbaar zijn. Als een concept te groot wordt, kan een specifieker onderdeel een **subconcept** worden dat voortbouwt op het hoofdconcept — het subconcept veronderstelt dan dat de student het hoofdconcept kent.

**Vakoverschrijdend is gewenst**: een concept dat in 4 vakken voorkomt, heeft 4 vak-secties. De student die personenbelasting instudeert klikt op "autoleasing" en land in de sectie `### [2.x] Personenbelasting` — maar ziet ook dat er een boekhoudkundige en adviessectie bestaat.

## Hoe bepalen we welke concepten er zijn?

**Vertrekpunt**: de taken, doelstellingen en kenniselementen van de vakfiches. Die beschrijven wat een student moet *kunnen doen* en *begrijpen* — de concepten zijn de bouwstenen daarvoor.

**Werkwijze**:
1. Lees de taken en doelstellingen: welk fenomeen of onderwerp moet de student beheersen om deze taak uit te voeren?
2. Lees de kenniselementen: welke begrippen en onderwerpen worden expliciet genoemd?
3. Let ook op **impliciete concepten**: dingen die niet met naam worden vermeld maar wel verondersteld worden (bv. "een risicoanalyse uitvoeren" veronderstelt dat je weet wat een risico is)
4. Vermijd duplicaten: als hetzelfde fenomeen al als concept bestaat (ook in een ander vak), breid dat concept uit — maak geen tweede fiche

**Geen dubbele concepten**: elk fenomeen of studieonderwerp krijgt precies één fiche. Concepten kunnen op elkaar voortbouwen via wikilinks en subconcept-relaties, maar overlappen niet.

## Structuur van een concept

Een concept bestaat uit een geordende lijst van **secties**. Elke sectie heeft een **type** en optioneel een **domein**.

### De domeinen

| Domein | Omschrijving |
|--------|-------------|
| **Boekhoudkundig** | Boeking, waardering, jaarrekening, analytische boekhouding |
| **Fiscaal** | Belastingen, aftrekken, aangiften, procedures |
| **Juridisch** | Wetgeving, rechten, verplichtingen, rechtspraak |

Een concept kan secties uit meerdere domeinen bevatten. Als een sectie niet past binnen deze domeinen, stel dan een nieuw domein voor ter validatie door de gebruiker.

### De sectietypes

| Type | Vraag die het beantwoordt | Signaalwoorden |
|------|--------------------------|----------------|
| **Begrip** | Wat is X? | definitie, term, afkorting |
| **Principe** | Hoe werkt X als algemene regel? | beginsel, basisregel |
| **Procedure** | Welke stappen volg je? | stappen, termijnen, volgorde |
| **Berekening** | Hoe reken je X uit? | formule, ratio, tarief, grondslag |
| **Vergelijking** | Wat is het verschil tussen X en Y? | vs, verschil, kies je voor |
| **Advies** | Wat zeg je tegen de cliënt? | adviseer, begeleid, stel voor |
| **Checklist** | Wat controleer je? | controleer of, verifieer, ga na |
| **Diagnose** | Wat zie je en wat betekent dat? | herken, detecteer, alarmsignaal |
| **Verplichting** | Wat moet verplicht gebeuren? | verplicht, moet, meldingsplicht |
| **Rol** | Wie doet wat? | taak van, bevoegdheid, verantwoordelijkheid |

Als een sectie niet past binnen deze 10 types, stel dan een nieuw type voor met naam, vraag en signaalwoorden — ter validatie door de gebruiker.

- Een concept bevat **alleen de secties die relevant zijn** — niet elk concept heeft alle types of domeinen nodig.
- Hetzelfde type mag **meerdere keren voorkomen** binnen één concept (bv. twee aparte berekeningen, of twee begrippen die samen horen).

## Conventie conceptfiche

Elk bestand in content/concepten/ volgt dit formaat:

```
---
tags: [1.2, 2.3]           # alle vakken waar dit concept leerstof is
niveau: integratie
status: leerstof            # of: context
bronnen:
  - WVV art. 5:142
itaa-lex: XVII, p. ~
---

# Naam van het concept

> Relevant voor: [[1.2-boekhoudrecht-en-jaarrekeningenrecht|1.2]], [[2.3-vennootschapsbelasting|2.3]]

Zie ook: [[verwant-concept-a]], [[verwant-concept-b]]

[Inhoudelijke secties geordend naar sectietypes — zie "Structuur van een concept"]
[Valkuilen en veelgestelde vragen staan als callouts bij de relevante inhoudssectie]

> [!warning]- Veelgemaakte fout: [korte titel]
> Uitleg van de fout en waarom die fout gemaakt wordt.

> [!question]- FAQ: [vraag]
> Antwoord op een typische studievraag over dit onderdeel.

## Per vak

### [1.2] Naam van het vak
Welke secties van dit concept zijn leerstof voor dit vak, en wat is de focus.

> [!example]- Voorbeeldvragen
> 1. [Vraag zoals die in een examen kan verschijnen]
> 2. [Vraag]

### [2.3] Naam van het vak
...

## Bronnen en artikelen
- [Wet X art. Y](https://www.ejustice.just.fgov.be/...) — omschrijving
- ITAA-LEX [sectie], p. [pagina] — omschrijving
```

### Bronvermelding: regels

**Inline bronnen**: elke feitelijke bewering over wetsinhoud krijgt een verwijzing direct in de tekst — bv. `(AWW art. 47)` of `(Wet ITAA art. 50)`.

**Sectie "Bronnen en artikelen"** onderaan bevat de volledige referenties:
- **ITAA-LEX proxy**: link naar de relevante ITAA-LEX sectie-proxy in `content/itaa-lex/` — bv. `[[itaa-lex-XVII|ITAA-LEX XVII, p. 2441]]`. Vanuit die proxy staat een klikbare link naar de online geconsolideerde versie. Dit is de primaire referentie, want ITAA-LEX is het naslagwerk dat tijdens het examen gebruikt mag worden.
- **Directe online link** als aanvulling wanneer nuttig — ejustice.just.fgov.be voor Belgische wetten, fisconet.be voor WIB92 en WBTW.

**Geen links naar lokale PDF's** — altijd via de ITAA-LEX proxy of een publieke online bron.

### ITAA-LEX proxy-bestanden

Elke gebruikte ITAA-LEX sectie krijgt een bestand in `content/itaa-lex/` met de naamgeving `itaa-lex-[sectienummer].md` (bv. `itaa-lex-XVII.md`).

Formaat van een ITAA-LEX proxy:

```
---
itaa-lex-sectie: XVII
wet: Wet van 18 september 2017 tot voorkoming van het witwassen van geld en de financiering van terrorisme
afkorting: AWW
online: https://www.ejustice.just.fgov.be/[...]
---

# ITAA-LEX XVII — AWW (Antiwitwaswet 2017)

[Online raadplegen](https://www.ejustice.just.fgov.be/[...]) · ejustice.just.fgov.be

## Structuur en paginanummers

| Artikel(en) | Onderwerp | Pagina ITAA-LEX |
|-------------|-----------|-----------------|
| Art. 2      | Definitie witwassen | p. 2441 |
| Art. 5      | Onderworpen entiteiten | p. 2443 |
| ...         | ...       | ... |

## Gebruikte concepten

Concepten die naar deze sectie verwijzen: [[antiwitwaswetgeving]]
```

Proxy-bestanden worden **on demand** aangemaakt — alleen wanneer een conceptfiche ernaar verwijst. Niet alle 21 secties hoeven te bestaan.

## Niveauindeling

De frontmatter van elke conceptfiche bevat een `niveau`-veld. Claude kiest het niveau op basis van de taken en doelstellingen in de vakfiche — niet op basis van aannames.

| Niveau | Wat de student kan | Typische examenvraag |
|--------|-------------------|----------------------|
| **weten-en-inzien** | Het concept benoemen en uitleggen: definitie, toepassingsgebied, waarom het bestaat | "Wat is X?" / "Welke stelling over X is juist?" |
| **toepassen** | Het concept correct gebruiken in een concrete situatie: berekening, boeking, procedure uitvoeren | "Bereken X" / "Hoe boek je Y?" / "Welke stappen volg je?" |
| **integratie** | Meerdere concepten combineren om een complexe vraag te beantwoorden: advies geven, diagnose stellen, afwegen | "Adviseer de cliënt" / "Wat zijn de gevolgen van X voor Y en Z?" |

Een concept kan voor verschillende vakken een verschillend niveau hebben — vermeld dan het hoogste niveau in de frontmatter en differentieer in de per-vak-secties.

## Hoe een nieuwe conceptfiche starten

1. **Controleer op duplicaten**: bestaat er al een fiche voor dit fenomeen — ook onder een andere naam? Zo ja, breid die uit in plaats van een nieuwe te maken.
2. **Verifieer de bronnen**: heb je voldoende bronmateriaal (ITAA-LEX, wettekst, ITAA-norm) om het concept inhoudelijk uit te diepen zonder aannames? Zo niet, maak eerst een skelet en markeer ontbrekende delen.
3. **Begin met de begrippen**: schrijf eerst de basisconcepten en definities uit — dit vormt de fundering voor alle andere secties.
4. **Markeer onzekerheden**: elk veld zonder verifieerbare bron krijgt `⚠️ te verifiëren`.
5. **Zet status op `draft`**: de gebruiker valideert de inhoud voor de status naar `geverifieerd` gaat. Schrijf nooit `status: geverifieerd` zelf.

## Tegenstrijdige bronnen

De bronhiërarchie zegt welke bron zwaarder weegt. Als twee bronnen elkaar tegenspreken:

- Vermeld **beide standpunten expliciet** — schrijf nooit één versie alsof het de enige waarheid is
- Geef aan welke bron hogere rang heeft volgens de bronhiërarchie
- Markeer het veld als `⚠️ te verifiëren` en leg het voor aan de gebruiker
- Voorbeeld: "Volgens [bron A] geldt X (rang 1). Volgens [bron B] geldt Y (rang 4). ⚠️ te verifiëren — bron A heeft hogere rang maar bron B is recenter."

## Kenniselement-IDs
Komen uit de officiële brochure (april 2022):
1.1 t.e.m. 1.9 = accountancy
2.1 t.e.m. 2.8 = fiscaal
3.1, 3.2 = vennootschapsrecht
4.0 = deontologie
