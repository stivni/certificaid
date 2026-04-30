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
| **TDKs** | Taken, Doelstellingen en Kenniselementen — de inhoud van een programmaonderdeel-fiche |
| **Materie / studiematerie** | De conceptfiches: de inhoudelijke bouwstenen waarnaar de TDKs verwijzen |
| **Concept / fenomeen** | Één coherent studieonderwerp met een eigen fiche in `content/materie/` |

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
│   ├── materie/            # Één .md per concept/fenomeen — getoond als "Materie" in de Explorer
│   ├── programmaonderdelen/ # Één .md per programmaonderdeel — getoond als "Programmaonderdelen" in de Explorer
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

## Status van programmaonderdelen en materie

Programmaonderdeel-fiches en materie-fiches gebruiken tags om hun status aan te geven in de Explorer:

| Tags | Betekenis | Zichtbaar in Explorer |
|------|-----------|----------------------|
| `[wip]` | Actief in behandeling | **Ja** |
| `[wip, verborgen]` | Nog niet behandeld (onderdelen die nog niet aan bod komen) | **Nee** |
| *(geen wip-tag)* | Voltooid en geverifieerd door de gebruiker | **Ja** |

De `wip`-tag volstaat als indicator — géén [WIP]-prefix in de titel.

**Werkwijze programmaonderdelen**: wanneer we een vak beginnen te behandelen, verwijder de `verborgen`-tag. De `wip`-tag blijft staan tot de gebruiker valideert.

**Werkwijze materie**: nieuwe conceptfiches starten altijd met `wip`-tag. De tag wordt pas verwijderd (en `status` van `draft` naar `geverifieerd` gezet) wanneer de gebruiker de inhoud valideert. Alleen de gebruiker doet dat.

## Doelpubliek en schrijfstijl
De conceptfiches zijn studiemateriaal voor mensen die al iets van de boekhoudkundige en fiscale wereld kennen (bv. via opleiding of praktijk), maar geen juristen zijn.

- **Menselijke, heldere taal** — geen legalese, wel precies
- **Niet alles is gekend** — leg ook "bekende" begrippen kort uit, mensen vergeten
- **Afkortingen** — eerste vermelding altijd voluit met een wikilink naar de fiche (en zo mogelijk naar de specifieke sectie) waar het begrip uitgelegd wordt: "Gecertificeerd Belastingadviseur ([[beroep-van-accountant-en-belastingadviseur|GBA]])"; daarna gewoon de afkorting
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

## Structuur binnen een fiche

De volgorde van secties binnen een fiche volgt een vaste logica — van algemeen naar specifiek, van begrip naar toepassing:

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

### Iteratief werkproces

Conceptfiches worden in stappen opgebouwd. Elke stap wordt door de gebruiker geverifieerd voor de volgende begint:

1. **Materie** — begrippen, principes, verplichtingen, procedures — volledig brongebonden
2. **Valkuilen + praktijkvoorbeelden** — mag 🤖 als gelabeld
3. **Voorbeeldvragen** — mag 🤖 als gelabeld
4. **Hyperlinks, ITAA-LEX referenties, backlinks** — alle links controleren en aanvullen

### Template materie-fiche

Elk bestand in `content/materie/` volgt dit formaat:

```
---
tags: ["4.0", wip, materie]  # programmaonderdeel-ID's + wip + materie
niveau: integratie
status: draft                 # draft → geverifieerd (alleen gebruiker zet geverifieerd)
bronnen:
  - Wet ITAA art. 37
itaa-lex: XXI, p. 2604
---

# Naam van het concept

## 📌 Term A
Definitie van Term A. ([[itaa-lex-XXI#art-2|Wet ITAA art. 2]])

## 📌 Term B (AFKORTING)
Definitie. Overkoepelend begrip? → Zie [[conceptfiche#term-a|Term A]], [[conceptfiche#term-c|Term C]]

## ⚖️ Naam van het principe
Inhoud. ([[itaa-lex-XVII#art-47|AWW art. 47]])

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

### Template programmaonderdeel-fiche

Elk bestand in `content/programmaonderdelen/` volgt dit formaat:

```
---
explorer_title: "X.X Korte naam"      # weergave in de Explorer
tags: ["X.X", wip, programmaonderdeel]
---

# X.X Volledige naam van het programmaonderdeel

## Taken en doelstellingen

### Taak: [omschrijving]

- [[materie-fiche#sectie|Doelstelling]]: omschrijving van wat de student moet kunnen
  - Kenniselement X.n: [[materie-fiche#sectie|korte omschrijving]]

## Relevante materie

- [[materie-fiche-a|Naam concept A]]
- [[materie-fiche-b|Naam concept B]]
```

### Sectiehoofdingen: emoji vervangt het typewoord

De emoji aan het begin van een sectieheading **is** het type — het typewoord wordt niet herhaald:
- ✓ `## 📌 Witwassen van geld`
- ✗ `## 📌 Begrip: Witwassen van geld`

### Begrippen: één per sectie, naam vóór afkorting

Elk begrip krijgt een eigen `##`-sectie, zodat het een eigen anker heeft voor deep-links. Meerdere begrippen in één sectie is niet toegestaan.

**Volgorde**: naam volledig uitgeschreven, dan afkorting tussen haakjes:
- ✓ `## 📌 Cel voor Financiële Informatieverwerking (CFI)`
- ✗ `## 📌 CFI`

**Overkoepelende begrippen** die verwijzen naar twee of meer andere begrippen (bv. WG/FT → witwassen + terrorismefinanciering) krijgen een eigen sectie met verwijzingen naar de componentbegrippen.

**Elke afkorting** die in de fiche gebruikt wordt, moet als begrip opgenomen zijn zodat er naar gelinkt kan worden.

**Engelse afkortingen**: wanneer de afkorting Engelstalig is maar de titelnaam Nederlandstalig (bv. AMLCO, UBO), voeg dan een cursieve subtitel toe met de volledige Engelse term — direct onder de heading, vóór de bodytekst:

```markdown
## 📌 Verantwoordelijke persoon (AMLCO)
*Anti-Money Laundering Compliance Officer*

De persoon die toeziet...
```

Nederlandstalige afkortingen die rechtstreeks van de naam afleiden (GA, GBA, ITAA) krijgen geen subtitel.

### Ankers voor sectielinks

Quartz genereert ankers door de heading te slugifyen: emoji worden verwijderd **maar de spatie erna blijft** (en wordt een streepje), spaties worden koppeltekens, alles wordt lowercase, en **geaccentueerde tekens worden behouden**.

Dit betekent dat elke sectie met een emoji-heading een **leading dash** krijgt:
- Heading `## 📌 Witwassen van geld` → anker `#-witwassen-van-geld`
- Heading `## 🔒 Meldingsplicht` → anker `#-meldingsplicht`
- Heading `## 📌 Cel voor Financiële Informatieverwerking (CFI)` → anker `#-cel-voor-financiële-informatieverwerking-cfi`

Let op:
- Link: `[[antiwitwaswetgeving#-witwassen-van-geld|...]]` ✓
- Link: `[[antiwitwaswetgeving#witwassen-van-geld|...]]` ✗ (leading dash ontbreekt)
- Geaccentueerde tekens (ë, é, ij...) worden **niet** omgezet naar ASCII: gebruik `financiële` niet `financiele`

**Uitzondering**: ITAA-LEX proxy-headings (`## Art. X`) hebben geen emoji en dus geen leading dash → anker is gewoon `#art-x`.

### ITAA-LEX proxy: ankers

Proxy-headings zijn kortweg `## Art. X` (zonder beschrijving, zonder `{#art-X}`). Quartz genereert het anker dan als `art-x`. De beschrijving staat in de body van die sectie:

```
## Art. 47
**Meldingsplicht aan de CFI**
> Pagina ITAA-LEX: p. 2469

§1: Melding verplicht...
```

Link: `[[itaa-lex-XVII#art-47|AWW art. 47]]` ✓

### Callout: valkuil

```markdown
> [!warning]- Korte omschrijving van de valkuil
> ❌ *"De verkeerde aanname die studenten vaak maken."*
>
> De correcte uitleg van de regel, met bronverwijzing inline.
>
> 📝 *Uit voorbeeldexamen [jaar]* — of — 🤖 *AI-aanvulling*
```

- De `[!warning]`-callout heeft al een ⚠️-icoon — géén emoji herhalen in de titel
- De titel is een **korte omschrijving** van de valkuil, niet de foutieve bewering zelf
- De foutieve aanname staat als eerste regel in de body, cursief en tussen aanhalingstekens
- Daarna de correcte uitleg
- Helemaal onderaan de bronvermelding (📝 of 🤖)

### Callout: voorbeeldvraag

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

### Callout: in de praktijk

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

### Bronvermelding: regels

**Inline bronnen**: elke feitelijke bewering over wetsinhoud krijgt een klikbare verwijzing direct in de tekst via de ITAA-LEX proxy:
- `([[itaa-lex-XXI#art-37|Wet ITAA art. 37]])` — verwijst naar de artikel-sectie in de proxy
- `([[itaa-lex-XVII#art-47|AWW art. 47]])` — idem voor de AWW

**Links altijd naar artikel-anker**, nooit naar het algemene proxy-document: `[[itaa-lex-XXI#art-37|...]]` en niet `[[itaa-lex-XXI|...]]` wanneer je een specifiek artikel bedoelt.

**Geen aparte "Bronnen en artikelen"-sectie** — bronverwijzingen staan inline in de tekst, direct na de feitelijke bewering. Een aparte sectie onderaan is redundant en niet onderhoudbaar.

**Geen links naar lokale PDF's** — altijd via de ITAA-LEX proxy of een publieke online bron.

### ITAA-LEX proxy-bestanden

Elke gebruikte ITAA-LEX sectie heeft een bestand in `content/itaa-lex/` met de naamgeving `itaa-lex-[sectienummer].md`.

**Regel**: elk artikel waarnaar een materie-fiche linkt, **moet** een eigen `## Art. X` heading hebben in de proxy. Voeg die toe vóór je de link schrijft.

**Heading-formaat**: kortweg `## Art. X` — géén beschrijving in de heading, géén `{#art-X}`. Quartz genereert dan automatisch anker `art-x`. De beschrijving staat als vetgedrukte tekst onder de heading.

Het proxy-bestand ziet er zo uit:

```
---
itaa-lex-sectie: XVII
wet: Wet van 18 september 2017 ...
afkorting: AWW
online: https://www.ejustice.just.fgov.be/[...]
---

# ITAA-LEX XVII — AWW (Antiwitwaswet 2017)

[Online raadplegen](https://www.ejustice.just.fgov.be/[...]) · ejustice.just.fgov.be

## Overzicht artikelen

| Artikel(en) | Onderwerp | Pagina ITAA-LEX |
|-------------|-----------|-----------------|
| [Art. 2](#art-2) | Definitie witwassen | p. 2441 |
| ...    | ...       | ...     |

## Art. 2
**Definitie witwassen van geld**
> Pagina ITAA-LEX: p. 2441

Korte inhoud of samenvatting van het artikel.

## Art. 47
**Meldingsplicht aan de CFI**
> Pagina ITAA-LEX: p. 2469

...

## Gebruikte concepten
Concepten die naar deze sectie verwijzen: [[antiwitwaswetgeving]]
```

Link: `[[itaa-lex-XVII#art-47|AWW art. 47]]` ✓ — anker `art-47` matcht de heading `## Art. 47`.

Proxy-bestanden worden **on demand** aangemaakt — alleen wanneer een conceptfiche ernaar verwijst. Artikels die niet nodig zijn, staan niet in de proxy.

## Taalgebruik: afkortingen en voluit schrijven

Gebruik de **volledige term** waar mogelijk, en de afkorting enkel wanneer die écht courant is (btw, bv, nv) of wanneer de wet zelf uitsluitend de afkorting gebruikt. Twijfelgevallen: schrijf voluit.

- ✓ "witwassen van geld en financiering van terrorisme" (bij eerste vermelding), daarna "WG/FT" enkel als de context het vanzelfsprekend maakt
- ✓ "cliëntenonderzoek" ipv "CDD" in lopende tekst
- ✓ "uiteindelijke begunstigde" ipv "UBO" waar het past
- ✓ "btw", "bv", "nv" → courant genoeg om altijd als afkorting te gebruiken

## Sectie "Relevant voor"

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

## Conventie programmaonderdeel-fiche — kenniselementen en materie

### "TDK" is intern begrip — niet in content

"TDK" (Taken, Doelstellingen en Kenniselementen) is onze interne term voor de structuur van de brochure. In de fiches zelf gebruiken we de echte termen: "Kenniselement", "Taak", "Doelstelling".

### TDKs linken naar materie

Elke TDK die verwijst naar een te kennen concept krijgt een link naar de relevante **sectie** in de materie-fiche. Ankers zijn zonder emoji (Quartz strips ze):

```markdown
- Een [[antiwitwaswetgeving#meldingsplicht-en-het-verbod-op-mededeling-tipping-off|meldingsplicht]] uitvoeren
```

Een bullet zonder link naar materie is een signaal dat er materie ontbreekt of dat de link nog niet gelegd is.

### "Relevante materie" — volledigheidseis

De sectie onderaan de vakfiche heet **"Relevante materie"** (vroeger: "Concepten"). Ze bevat alle conceptfiches die samen de volledige examenstof voor dit vak dekken.

**Eis**: een student die enkel de "Relevante materie"-lijst doorloopt zonder één TDK-link te volgen, moet toch alle examenstof gezien hebben. De lijst is dus geen subset — ze is compleet.

### Verificatiestap na het schrijven van een vakfiche

Na het opstellen of bijwerken van een vakfiche, doorloop je expliciet:

1. **Elke TDK** → heeft die een link naar de juiste sectie in een conceptfiche?
2. **Elke conceptfiche in "Relevante materie"** → dekt die alle TDKs die ernaar linken?
3. **Zijn er TDKs die naar geen enkele materie linken?** → maak de ontbrekende materie aan of voeg het kenniselement toe als sectie in een bestaande fiche

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
3. **Volg het iteratief werkproces**: eerst materie (brongebonden), daarna valkuilen + praktijkvoorbeelden (🤖 mag), daarna voorbeeldvragen (🤖 mag), daarna hyperlinks en referenties.
4. **Begin met de begrippen**: schrijf eerst de basisconcepten en definities uit — dit vormt de fundering voor alle andere secties.
5. **Markeer onzekerheden**: elk veld zonder verifieerbare bron krijgt `⚠️ te verifiëren`.
6. **Zet status op `draft`**: de gebruiker valideert de inhoud voor de status naar `geverifieerd` gaat. Schrijf nooit `status: geverifieerd` zelf.

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

## Workflow: nieuw programmaonderdeel opstarten

Dit is de volgorde wanneer we een nieuw programmaonderdeel beginnen te behandelen:

### Stap 1 — Programmaonderdeel activeren
1. Open `content/programmaonderdelen/X.X-naam.md`
2. Verwijder `verborgen` uit de tags → fiche is zichtbaar in de Explorer

### Stap 2 — Concepten bepalen
1. Lees de taken, doelstellingen en kenniselementen in de brochure (resources/programma.pdf) en/of programmaonderdeel fiche
2. Bepaal welke concepten/fenomenen de materie vormen (zie "Hoe bepalen we welke concepten er zijn?")
3. Controleer op duplicaten met bestaande materie-fiches
4. Leg de lijst voor aan de gebruiker ter validatie

### Stap 3 — Per concept: materie-fiche aanmaken (iteratief)
Voor elk nieuw concept, in deze volgorde (elke stap door gebruiker valideren):

1. **Materie** — begrippen, principes, verplichtingen, procedures — volledig brongebonden
   - Maak indien nodig een nieuwe ITAA-LEX proxy aan of voeg artikelen toe
   - Gebruik het template materie-fiche
   - **Kritische lezing achteraf** (zie hieronder)
2. **Valkuilen + praktijkvoorbeelden** — mag 🤖 als gelabeld; voeg bij elke berekening of procedure minstens één concreet doorgewerkt voorbeeld toe
3. **Voorbeeldvragen** — raadpleeg eerst `resources/voorbeeldexamens/`; gebruik echte vragen (📝) prioritair; vul aan met 🤖
   - **Verplichte eerste stap**: gebruik `pdftotext` om alle PDF's in `resources/voorbeeldexamens/` te doorzoeken op vragen die het concept raken. Grep op sleutelwoorden uit de sectiehoofden.
   - Echte examenvragen worden letterlijk overgenomen (behoudens vertaling naar het Nederlandstalige calloutformaat) en gelabeld als `📝 *Uit voorbeeldexamen [jaar]*`
   - Vul aan met 🤖-vragen voor concepten waarvoor geen examenmateriaal beschikbaar is, of om aspecten te testen die niet in de echte examens voorkomen
4. **Hyperlinks** — semantische doorlezing voor links (zie hieronder)

### Semantische hyperlinkdoorlezing (stap 4)

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

**Geen grepping** — een keyword-zoekopdracht mist passages die conceptueel verwijzen zonder letterlijk de term te gebruiken. De enige betrouwbare methode is lezen.

**Geldt voor beide fichetypes**: materie-fiches én programmaonderdeel-fiches. In programmaonderdeel-fiches linkt elke taak, doelstelling en kenniselement naar de relevante sectie in de materie — niet enkel naar het fiche-niveau.

### Wettekstverificatie na het schrijven van de materie

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

### Kritische lezing na het schrijven van de materie

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

De oplossing is altijd: de informatie meteen in de tekst opnemen, niet doorverwijzen naar een artikel zonder de inhoud te geven. De student heeft ITAA-LEX bij zich maar moet weten **wat** hij moet opzoeken en **waarom** — niet de interpretatie zelf moeten doen.

**Controleer ook de logische structuur van elke paragraaf en de fiche als geheel:**

| Structuurprobleem | Correctie |
|---|---|
| Uitzondering vóór de hoofdregel | Hoofdregel eerst, dan "behalve wanneer..." |
| Gevolg vóór oorzaak | Oorzaak → gevolg: "X leidt tot Y", niet "Y wordt opgelegd wanneer X" |
| Passieve zin verbergt de actor | Herschrijf actief: wie doet wat? |
| Items in een lijst niet parallel | Zorg dat alle items dezelfde grammaticale structuur volgen |
| Informatie staat twee keer | Eén keer, en wikilink naar de sectie waar het uitgelegd is |
| Term gebruikt vóór hij uitgelegd is | Sectievolgorde aanpassen of begrip eerder introduceren |
| Sanctie staat ver van de verplichting | Sanctie direct na de verplichting plaatsen |
| Vergelijking staat vóór de begrippen | Tabel pas na introductie van alle betrokken concepten |
| Twee secties over hetzelfde thema | Samenvoegen tot één sectie |
| Eén sectie over twee ongerelateerde thema's | Opsplitsen in twee secties |

### Stap 4 — Programmaonderdeel-fiche afwerken
1. Vul de kenniselement-bullets in met links naar de juiste secties in de materie-fiches
2. Vul de "Relevante materie"-sectie in met alle bijhorende materie-fiches
3. Doorloop de verificatiestap (zie "Verificatiestap na het schrijven van een programmaonderdeel-fiche")

### Stap 5 — Validatie door de gebruiker
- Gebruiker valideert materie → `status: draft` blijft, `wip`-tag blijft
- Wanneer gebruiker volledig tevreden is: `wip`-tag verwijderen, `status: geverifieerd`

## Quartz: documentatie eerst raadplegen

Bij elke wijziging aan Quartz layout, componenten of styling:
1. Controleer https://quartz.jzhao.xyz/layout voor beschikbare componenten en opties
2. Controleer de broncode in `quartz/components/` voor precieze API
3. Pas daarna pas `quartz.layout.ts` of `quartz/styles/custom.scss` aan

Quartz heeft ingebouwde wrappers zoals `Component.Flex()` die CSS-hacks overbodig maken.
