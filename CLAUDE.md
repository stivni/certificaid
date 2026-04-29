# Certificaid

Kennisbank voor het ITAA bekwaamheidsexamen (gecertificeerd accountant / gecertificeerd belastingadviseur).

## Doel
Gestructureerde studiematerie die:
- Georganiseerd is rond reële fenomenen en coherente studieonderwerpen — niet rond vakken of wetsartikelen
- Vakoverschrijdend is (één concept kan in meerdere vakken voorkomen)
- Terugkoppelt naar de TDKs uit de officiële ITAA-brochure
- Alleen verifieerbare informatie bevat (bronvermelding verplicht)

## Terminologie

| Term | Betekenis |
|------|-----------|
| **TDKs** | Taken, Doelstellingen en Kenniselementen — de inhoud van een vakfiche |
| **Materie / studiematerie** | De conceptfiches: de inhoudelijke bouwstenen waarnaar de TDKs verwijzen |
| **Concept / fenomeen** | Één coherent studieonderwerp met een eigen fiche in `content/concepten/` |

## Structuur
```
certificaid/
├── CLAUDE.md
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

## Absolute regel: geen hallucinaties in de materie
Dit is de belangrijkste regel van het hele project.

- Elk feit, elke definitie, elk wetsartikel in de **materie-secties** moet traceerbaar zijn naar een concrete bron
- Schrijf NOOIT iets over wetsinhoud zonder een bronverwijzing
- Als je een concept niet met zekerheid kunt onderbouwen vanuit een bron: zeg dat expliciet, vul het veld NIET in, en markeer het als `⚠️ te verifiëren`
- Liever een leeg veld dan een onzeker feit

**Uitzondering — valkuilen en voorbeeldvragen**: hier zijn AI-gegenereerde aannames toegestaan, op voorwaarde dat ze duidelijk gelabeld zijn met 🤖. De student weet dan dat dit een redenering is op basis van het concept, niet een geciteerde examenvraag of gedocumenteerde valkuil. De materie zelf waarop de valkuil of vraag gebaseerd is, blijft wel brongebonden.

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

## Status van vakken en concepten

Vakfiches en conceptfiches gebruiken tags om hun status aan te geven in de Explorer:

| Tags | Betekenis | Zichtbaar in Explorer |
|------|-----------|----------------------|
| `[wip]` | Actief in behandeling — [WIP] in titel | **Ja** |
| `[wip, verborgen]` | Nog niet behandeld — [WIP] in titel | **Nee** |
| *(geen wip-tag)* | Voltooid en geverifieerd | **Ja** |

**Werkwijze**: wanneer we een vak of concept beginnen te behandelen, verwijder de `verborgen`-tag. De `wip`-tag en het [WIP]-prefix in de titel blijven staan tot de gebruiker de inhoud valideert.

## Doelpubliek en schrijfstijl
De conceptfiches zijn studiemateriaal voor mensen die al iets van de boekhoudkundige en fiscale wereld kennen (bv. via opleiding of praktijk), maar geen juristen zijn.

- **Menselijke, heldere taal** — geen legalese, wel precies
- **Niet alles is gekend** — leg ook "bekende" begrippen kort uit, mensen vergeten
- **Afkortingen** — eerste vermelding altijd voluit: "Besloten Vennootschap (BV)"
- **Wikilinks** — elk concept dat elders een fiche heeft, krijgt een `[[link]]` bij elke vermelding; zo mogelijk naar de relevante sectie via `[[fiche#sectie|tekst]]`
- **Vakken in numerieke volgorde** — 1.2 voor 2.3 voor 3.1 enz.
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

**Vertrekpunt**: de TDKs van de vakfiches. Die beschrijven wat een student moet *kunnen doen* en *begrijpen* — de concepten zijn de bouwstenen daarvoor.

**Werkwijze**:
1. Lees de taken en doelstellingen: welk fenomeen of onderwerp moet de student beheersen om deze taak uit te voeren?
2. Lees de kenniselementen: welke begrippen en onderwerpen worden expliciet genoemd?
3. Let ook op **impliciete concepten**: dingen die niet met naam worden vermeld maar wel verondersteld worden
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

| Emoji | Type | Vraag die het beantwoordt | Signaalwoorden |
|-------|------|--------------------------|----------------|
| 📌 | **Begrip** | Wat is X? | definitie, term, afkorting |
| ⚖️ | **Principe** | Hoe werkt X als algemene regel? | beginsel, basisregel |
| 📋 | **Procedure** | Welke stappen volg je? | stappen, termijnen, volgorde |
| 🔢 | **Berekening** | Hoe reken je X uit? | formule, ratio, tarief, grondslag |
| ↔️ | **Vergelijking** | Wat is het verschil tussen X en Y? | vs, verschil, kies je voor |
| 💬 | **Advies** | Wat zeg je tegen de cliënt? | adviseer, begeleid, stel voor |
| ✅ | **Checklist** | Wat controleer je? | controleer of, verifieer, ga na |
| 🔍 | **Diagnose** | Wat zie je en wat betekent dat? | herken, detecteer, alarmsignaal |
| 🔒 | **Verplichting** | Wat moet verplicht gebeuren? | verplicht, moet, meldingsplicht |
| 👤 | **Rol** | Wie doet wat? | taak van, bevoegdheid, verantwoordelijkheid |

Als een sectie niet past binnen deze 10 types, stel dan een nieuw type voor met naam, vraag en signaalwoorden — ter validatie door de gebruiker.

- Een concept bevat **alleen de secties die relevant zijn** — niet elk concept heeft alle types of domeinen nodig.
- Hetzelfde type mag **meerdere keren voorkomen** binnen één concept (bv. twee aparte berekeningen, of twee begrippen die samen horen).

## Conventie conceptfiche

Elk bestand in content/concepten/ volgt dit formaat:

```
---
tags: [4.0]                 # alle vakken waar dit concept leerstof is
niveau: integratie
status: draft               # draft → geverifieerd (alleen gebruiker zet geverifieerd)
bronnen:
  - Wet ITAA art. 37
itaa-lex: XXI, p. 2604
---

# 📌 Naam van het concept

> Relevant voor: [[4.0-deontologie|4.0]]

Zie ook: [[verwant-concept-a]], [[verwant-concept-b]]

## 📌 Begrippen

### 📌 Begrip: Term A
Definitie van Term A. ([[itaa-lex-XXI#art-2|Wet ITAA art. 2]])

### 📌 Begrip: Term B
Definitie van Term B.

## ⚖️ Principe: Naam van het principe
Inhoud. ([[itaa-lex-XVII#art-47|AWW art. 47]])

> [!warning]- ⚠️ Opgelet: [de correcte situatie in één zin]
> [Volledige uitleg van de juiste regel]
>
> ❌ Verkeerde aanname: "[wat studenten vaak foutief denken]"
>
> 📝 *Gebaseerd op voorbeeldexamen 2024* — of — 🤖 *AI-inschatting op basis van conceptuele analyse*

## 🔒 Verplichting: Naam van de verplichting
Inhoud.

## Per vak

### [4.0] Naam van het vak

**Relevante TDKs:**
- Taak "X" → doelstelling "Y" → kenniselement Z.n

> [!example]- ❓ Voorbeeldvraag 1 — 📝 Uit voorbeeldexamen 2024
> [De vraag zoals die in een examen verschijnt]
>
> > [!success]- ✅ Antwoord
> > [Het correcte antwoord]
> >
> > **Verantwoording**: [Waarom dit het juiste antwoord is, met bronverwijzing]

> [!example]- ❓ Voorbeeldvraag 2 — 🤖 AI-gegenereerd
> [Een vraag die op basis van de materie verwacht kan worden]
>
> > [!success]- ✅ Antwoord
> > [Het correcte antwoord]
> >
> > **Verantwoording**: [Uitleg]

## Bronnen en artikelen
- [[itaa-lex-XXI|ITAA-LEX XXI]] — Wet ITAA 2019
- [[itaa-lex-XXI#art-37|Wet ITAA art. 37]]: onafhankelijkheid en deontologische beginselen
```

### Bronvermelding: regels

**Inline bronnen**: elke feitelijke bewering over wetsinhoud krijgt een klikbare verwijzing direct in de tekst via de ITAA-LEX proxy:
- `([[itaa-lex-XXI#art-37|Wet ITAA art. 37]])` — verwijst naar de artikel-sectie in de proxy
- `([[itaa-lex-XVII#art-47|AWW art. 47]])` — idem voor de AWW

**Sectie "Bronnen en artikelen"** onderaan herhaalt de referenties als overzicht met klikbare ITAA-LEX proxy-links.

**Geen links naar lokale PDF's** — altijd via de ITAA-LEX proxy of een publieke online bron.

### ITAA-LEX proxy-bestanden

Elke gebruikte ITAA-LEX sectie heeft een bestand in `content/itaa-lex/` met de naamgeving `itaa-lex-[sectienummer].md`.

Het proxy-bestand is georganiseerd als een **echte index** met artikel-level headings zodat deep-links werken:

```
---
itaa-lex-sectie: XVII
wet: Wet van 18 september 2017 ...
afkorting: AWW
online: https://www.ejustice.just.fgov.be/[...]
---

# ITAA-LEX XVII — AWW (Antiwitwaswet 2017)

[Online raadplegen](https://www.ejustice.just.fgov.be/[...]) · ejustice.just.fgov.be

## Structuur en paginanummers

| Artikel(en) | Onderwerp | Pagina ITAA-LEX |
|-------------|-----------|-----------------|
| Art. 2 | Definitie witwassen | p. 2441 |
| ...    | ...       | ...     |

## Art. 2 — Definitie witwassen {#art-2}
> Pagina ITAA-LEX: p. 2441

Korte inhoud of samenvatting van het artikel.

## Art. 47 — Meldingsplicht {#art-47}
> Pagina ITAA-LEX: p. 2469

...

## Gebruikte concepten
Concepten die naar deze sectie verwijzen: [[antiwitwaswetgeving]]
```

De heading-anchors (`{#art-2}`) maken deep-links mogelijk: `[[itaa-lex-XVII#art-2|AWW art. 2]]`.

Proxy-bestanden worden **on demand** aangemaakt — alleen wanneer een conceptfiche ernaar verwijst.

## Conventie vakfiche — TDKs en materie

### TDK-bullets linken naar materie

Elke TDK-bullet die verwijst naar een te kennen concept krijgt een link naar de relevante **sectie** in de conceptfiche:

```markdown
- Een [[antiwitwaswetgeving#verplichting-meldingsplicht-aan-de-cfi|meldingsplicht]] uitvoeren
```

Een TDK-bullet zonder link naar materie is een signaal dat er materie ontbreekt of dat de link nog niet gelegd is.

### "Relevante materie" — volledigheidseis

De sectie onderaan de vakfiche heet **"Relevante materie"** (vroeger: "Concepten"). Ze bevat alle conceptfiches die samen de volledige examenstof voor dit vak dekken.

**Eis**: een student die enkel de "Relevante materie"-lijst doorloopt zonder één TDK-link te volgen, moet toch alle examenstof gezien hebben. De lijst is dus geen subset — ze is compleet.

### Verificatiestap na het schrijven van een vakfiche

Na het opstellen of bijwerken van een vakfiche, doorloop je expliciet:

1. **Elke TDK-bullet** → heeft die een link naar de juiste sectie in een conceptfiche?
2. **Elke conceptfiche in "Relevante materie"** → dekt die alle TDKs die ernaar linken?
3. **Zijn er TDKs die naar geen enkele materie linken?** → maak de ontbrekende materie aan of voeg de TDK toe als sectie in een bestaande fiche

## Niveauindeling

De frontmatter van elke conceptfiche bevat een `niveau`-veld. Claude kiest het niveau op basis van de TDKs in de vakfiche — niet op basis van aannames.

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
