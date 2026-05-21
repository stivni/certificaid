---
title: "Jaarrekening — v1 (POC mockup)"
tags:
  - experiment
  - mockup
  - kader
status: experimental
mockup: true
linked_anchors:
  - "1.1.II.S"
  - "1.1.III.I"
  - "1.4.I.I"
---

> **POC mockup** — test of **één overkoepelende kader-fiche** met de
> cyclus (inventaris → opmaak → AV → neerlegging) als interne sectie
> didactisch beter werkt dan een opsplitsing in twee aparte records
> (artefact `jaarrekening` + procedure `opmaak-cyclus`). Voorstel
> `kind: kader` met de artefact-componenten als leden — zie
> [Iteratie-log](#iteratie-log) voor de afweging artefact vs kader.
>
> Vergelijk met:
> [[jaarrekeninganalyse-v1|jaarrekeninganalyse (kader, lezen)]] ·
> [[obligatielening-v7|obligatielening (instrument)]] ·
> [[oprichtingskosten-v1|oprichtingskosten (balanspost)]].
>
> **Confidence-tekens** (per claim):
> ⚖️ uit wet · KB · CBN · norm (grounded)
> 🔗 redenering uit bronnen (inferred)
> 🧭 beroepswijsheid, geen harde regel (vuistregel)
> ⚠️ bron ontbreekt of nog te verifiëren
> ❌ tegenstrijdig (gecheckt en fout)

# Jaarrekening

De **jaarrekening** is het wettelijk gestructureerde **financiële
eindverslag** dat élke vennootschap, vzw of stichting elk boekjaar
opmaakt: een **geheel** bestaande uit **balans**, **resultatenrekening**
en **toelichting**, opgesteld volgens door de Koning bepaalde
waarderingsregels en in een door de Koning bepaalde vorm.

*Bron: [[WVV#art-3-1]]* ⚖️

## Wat er economisch echt gebeurt

De jaarrekening is **het officiële beeld van de onderneming op één
moment** — typisch 31 december — plus **wat er in dat boekjaar gebeurd
is**. Drie dingen tegelijk:

1. **Foto van het vermogen** (balans) — wat heeft de onderneming
   (activa), wat is ze schuldig (vreemd vermogen), wat blijft over voor
   de eigenaars (eigen vermogen)?
2. **Film van het resultaat** (resultatenrekening) — wat heeft de
   onderneming dit jaar verdiend en uitgegeven?
3. **Bijsluiter** (toelichting) — welke keuzes (afschrijving, waardering,
   spreiding) liggen achter die cijfers, en welke risico's of
   verplichtingen zijn niet in de cijfers zelf zichtbaar?

🔗 Substance over form: de jaarrekening is **geen administratieve
formaliteit** maar het instrument waarmee derden — schuldeisers, fiscus,
aandeelhouders, werknemers, banken, leveranciers — beslissingen nemen
*zonder de boeken te kunnen openen*. Dat verklaart de strakke
voorgeschreven vorm: vergelijkbaarheid tussen ondernemingen en over de
jaren heen is de kern.

🔗 De jaarrekening is ook het **scharnierpunt** tussen de boekhouding
(continu, dagelijks) en het externe rapporteringscircuit (jaarlijks,
publiek). Tussen beide zit de **eindejaars-cyclus**: inventaris,
afsluiting, opmaak, controle, goedkeuring, neerlegging — zie
[De cyclus](#de-cyclus-van-inventaris-tot-neerlegging).

## Voorkennis & leespad

- **Lees eerst** (voorvereisten): [[boekhoudbeginselen]] ·
  [[mar-rekeningenstelsel]] · [[dubbele-boekhouding]] ·
  [[continuiteit-going-concern]]
- **Past binnen kader**: dit *is* een kader-fiche — de overkoepelende
  context voor balansposten, resultatenrekeningposten en
  toelichtingsrubrieken.
- **Naast deze fiche relevant**: [[jaarrekeninganalyse-v1]] (hoe lees je
  een jaarrekening eens ze er staat) · [[oprichtingskosten-v1]]
  (concrete balanspost) · [[obligatielening-v7]] (instrument met
  toelichtingsverplichtingen) · [[uitkering-aan-aandeelhouders-v1]]
  (gebruik van het resultaat)
- **Bij vervolgvragen**: [[geconsolideerde-jaarrekening]] · [[IFRS-vs-BGAAP]]
  · [[NBB-centrale-balansen]] · [[alarmbel-procedure]]

## Wanneer is dit van toepassing?

🧭 *Geen keuze-element op artefact-niveau* — de jaarrekening is
**verplicht** voor élke vennootschap met rechtspersoonlijkheid, elke
vzw, elke ivzw en elke stichting (artikel 3:1 §1 WVV — vennootschappen;
artikel 3:47 §1 WVV — vzw's/ivzw's). De **echte keuzes** zitten op het
niveau van het **schema** (volledig vs verkort vs micro — zie
[Formaten](#formaten-volledig-verkort-micro)) en op het niveau van de
**individuele waarderings- en spreidingskeuzes** (afschrijvingsmethode,
agio/disagio-spreiding, herwaardering, …) die in de **waarderingsregels**
worden vastgelegd.

*Bron: [[WVV#art-3-1]] · [[WVV#art-3-47]]* ⚖️

🧭 Voor **buitenlandse vennootschappen met een Belgisch bijkantoor**
geldt de opmaakplicht ook, behalve wanneer dat bijkantoor geen eigen
opbrengsten heeft door verkoop aan derden (artikel 3:1 §2 WVV).

## Hoe het werkt

*De jaarrekening is een samengesteld artefact: drie verplichte
componenten (balans, resultatenrekening, toelichting) + één facultatieve/
voorwaardelijke (jaarverslag) + één situationele (sociale balans). De
**cyclus** beschrijft hoe het artefact tot stand komt. De
**waarderingsregels** zijn een verplichte bijlage van de toelichting die
de keuzes achter de cijfers documenteert.*

### Artefact-componenten

```
┌─────────────────────────── JAARREKENING ───────────────────────────┐
│  ┌────────────────┐  ┌────────────────────┐  ┌──────────────────┐  │
│  │   BALANS       │  │  RESULTATENREK.    │  │   TOELICHTING    │  │
│  │  (foto t)      │  │  (film t-1 → t)    │  │  (bijsluiter)    │  │
│  │  Activa /      │  │  Opbrengsten /     │  │  + waarderings-  │  │
│  │  Passiva       │  │  Kosten / Winst    │  │    regels        │  │
│  └────────────────┘  └────────────────────┘  └──────────────────┘  │
│                                                                    │
│  ┌──────────────────────┐    ┌─────────────────────────────────┐  │
│  │  SOCIALE BALANS      │    │  JAARVERSLAG (bestuursorgaan)   │  │
│  │  (≥ 20 vte gem.)     │    │  (volledig schema; vrijgesteld  │  │
│  │  facultatieve onder- │    │   voor klein/micro)             │  │
│  │  delen toelichting   │    │                                 │  │
│  └──────────────────────┘    └─────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────┘
```

#### Balans

De **balans** geeft op afsluitingsdatum (de **balansdatum**, meestal
31/12) de **vermogenstoestand** weer: aan actiefzijde wat de
onderneming **bezit of vordert**, aan passiefzijde wat ze **schuldig
is** plus het **eigen vermogen** (het saldo dat aan de eigenaars
toekomt).

🔗 De balans is een **momentopname** — zie ook
[balansdatum-effect in jaarrekeninganalyse-v1](jaarrekeninganalyse-v1.md#3-balansdatum-effect-bewaken).
Eenmalige transacties net vóór of na balansdatum kunnen het beeld
sterk vertekenen.

⚖️ **Vorm**: vastgelegd in Bijlage 3 (volledig schema), Bijlage 4
(verkort) of een specifiek micro-schema bij het KB WVV.
*Bron: [[KB-WVV#art-3-80]] · [[KB-WVV#art-3-83]] · [[KB-WVV#art-3-84]]* ⚖️

#### Resultatenrekening

De **resultatenrekening** toont over het **hele boekjaar** de
**opbrengsten** en **kosten**, en eindigt op de **winst of het verlies
van het boekjaar**. Dat resultaat wordt vervolgens **bestemd**
(reserve · overgedragen resultaat · dividend) bij de algemene
vergadering — zie [Resultaatverwerking](#7-resultaatverwerking).

⚖️ Twee voorstellingsvormen toegelaten in het volledig schema:
*per aard* (kosten gegroepeerd naar hun economische aard — handelsgoederen,
diensten, personeel, afschrijvingen, …) of *per functie* (kosten
gegroepeerd naar bestemming — kostprijs verkopen, marketing, …). In
België wordt **per aard** veruit het meest gebruikt — ⚠️ KB-WVV-artikel
voor functie-schema te verifiëren.

#### Toelichting

De **toelichting** is **geen aanhangsel maar deel van het geheel**
(artikel 3:1 §1 WVV "vormt een geheel"). Ze bevat:

- de **samenvatting van de waarderingsregels** (zie
  [Waarderingsregels-bijlage](#de-waarderingsregels-verplicht-onderdeel))
  ⚖️ [[KB-WVV#art-3-90]] *(artikel te verifiëren)* ⚠️
- **detailstaten** bij balansposten (mutaties vaste activa, schulden
  meer/minder dan een jaar, vorderingen, …)
- **vermeldingen** over niet-in-balans-genomen verplichtingen
  (waarborgen, contractuele engagementen, hangende geschillen)
- **gebeurtenissen na balansdatum** ⚠️ [[KB-WVV#art-3-58]] te
  verifiëren
- gegevens van **bestuurders en commissaris** ⚖️ *(zie CBN-advies
  2020/09)*
- **interne verrichtingen** met aandeelhouders/bestuurders, transacties
  met verbonden partijen
- **sociale balans** indien van toepassing (zie hieronder)

🔗 De toelichting is voor een lezer **het cruciale instrument om
keuzes achter de cijfers te begrijpen**: zonder waarderingsregels zegt
"afschrijvingen 200.000" niet of dat lineair of degressief is, over
welke termijn, op welke basis. Een audit van de jaarrekening zonder de
toelichting te lezen is structureel onmogelijk.

#### Sociale balans

De **sociale balans** is een gestructureerde voorstelling van
personeelsgegevens (aantal werknemers in voltijdse equivalenten,
loonkost, scholing, sociale maatregelen). Ze is **opgenomen in de
toelichting** zodra de entiteit een **jaargemiddelde van ten minste
20 personeelsleden** (in vte) telt.

*Bron: [[KB-WVV#art-3-161]]* ⚖️ *(voor VZW/IVZW/stichting; analoog
artikel voor vennootschappen ⚠️ te verifiëren)*

#### Jaarverslag

Het **jaarverslag** (officieel: verslag van het bestuursorgaan) is een
**narratief document** met onder meer een overzicht van de activiteiten,
de belangrijkste risico's en onzekerheden, en de gebeurtenissen na
balansdatum.

🔗 Het is **niet opgenomen in de jaarrekening zelf**, maar wordt
**samen** ermee neergelegd bij de NBB. Bij de **wettelijke controle**
verschijnt het in een aparte paragraaf van het commissaris-verslag.

⚖️ **Vrijstelling voor kleine en micro-vennootschappen**: ⚠️ exact
WVV-artikel te verifiëren — vermoedelijk artikel 3:5 of 3:6 WVV. De
*memorie van toelichting* bevestigt de vrijstellingen.

### Formaten (volledig · verkort · micro)

🔗 Het **formaat** van de jaarrekening hangt af van de **grootte** van
de vennootschap of vereniging op balansdatum. Drie groottecategorieën,
elk met een eigen schema. De grootte bepaalt:

- de **diepgang** van de schema's (aantal rubrieken, mate van detail)
- het al-of-niet opmaken van **bepaalde toelichtingsrubrieken**
- de **verplichting tot jaarverslag** (volledig schema)
- de **verplichting tot aanstelling van een commissaris** ⚠️

#### Vergelijkingstabel — vennootschappen

| Kenmerk | **Volledig** | **Verkort (klein)** | **Micro** |
|---|---|---|---|
| **Norm-artikel** | [[WVV#art-1-24]] ⚖️ | [[WVV#art-1-24]] ⚖️ | [[WVV#art-1-25]] ⚖️ |
| **Definitie** | Méér dan 1 van de criteria | Niet meer dan 1 criterium | Klein + niet-dochter/moeder + niet meer dan 1 micro-criterium |
| **Werknemers (jaargem., vte)** | — | ≤ 50 | ≤ 10 |
| **Jaaromzet excl. btw** | — | ≤ € 9.000.000 | ≤ € 900.000 *(sinds 2024)* |
| **Balanstotaal** | — | ≤ € 4.500.000 | ≤ € 450.000 *(sinds 2024)* |
| **Schema balans** | Bijlage 3 KB WVV | Bijlage 4 KB WVV | Microschema |
| **Schema resultatenrekening** | Bijlage 3 | Bijlage 3 | Bijlage 4 |
| **Toelichting** | Volledig | Beperkt | Sterk beperkt |
| **Jaarverslag** | Verplicht | Vrijgesteld 🧭 | Vrijgesteld 🧭 |
| **Commissaris** | Doorgaans verplicht ⚠️ | Doorgaans niet ⚠️ | Doorgaans niet ⚠️ |

*Bron drempels: [[WVV#art-1-24]] § 1 · [[WVV#art-1-25]] § 1* ⚖️ —
laatste actualisering van bedragen via wet van 28/03/2024 en wet van
02/12/2024.

🧭 **Vuistregel voor grootteberekening**: bij **moedervennootschappen**
gebeurt de toetsing op **geconsolideerde of geaggregeerde** basis (niet
enkelvoudig) — vandaar dat een kleine *enkelvoudige* X die deel uitmaakt
van een grotere groep tóch als groot kan worden gekwalificeerd. *Bron:
[[CBN-2022-03]]* ⚖️

🧭 **Consistentiebeginsel**: een vennootschap kan pas overschakelen
naar een ander schema na **twee opeenvolgende boekjaren** waarin de
grenzen anders worden beoordeeld — ⚠️ exacte regel te verifiëren in
[[WVV#art-1-24]] § 2 e.v.

#### Vergelijkbare schaal voor vzw's/ivzw's

⚖️ Voor vzw's en ivzw's gelden parallelle criteria in [[WVV#art-1-28]]
(klein) en [[WVV#art-1-29]] (micro), met **andere drempels** (omzet en
balanstotaal aangepast bij KB 2024-05-25). *Bron: [[WVV#art-1-29]]* ⚖️
De schema's zelf staan in **bijlagen 6, 7 en 8** van het KB WVV
(volledig, verkort, micro voor verenigingen). *Bron: [[CBN-2019-12]]* ⚖️

### De cyclus (van inventaris tot neerlegging)

🔗 De **eindejaars-cyclus** is de procedurele rug waarop de jaarrekening
tot stand komt. Acht etappes; de jaarrekening is het tussenresultaat
tussen etappe 4 (opmaak) en etappe 8 (neerlegging).

#### Tijdslijn (boekjaar = kalenderjaar)

```
T = 31/12   T+0…1 m   T+1…3 m   T+3…6 m   T+6 m         T+6 m+30 d   T+7 m
   │           │          │          │          │              │           │
   ▼           ▼          ▼          ▼          ▼              ▼           ▼
Afsluiting → Inventaris → Eindejaars- → Proefbalans → AV-goedkeuring → Neerlegging   ⏰ uiterste
boekjaar    + waardering   boekingen   + opmaak     + resultaat-      bij NBB        datum NBB
                                       jaarrekening verwerking
```

⚖️ **Uiterste data** (vennootschappen, KB-WVV-cyclus):
- AV moet binnen **6 maanden** na afsluitingsdatum plaatsvinden
  ([[WVV#art-3-1]] §1) — voor een boekjaar dat eindigt op 31/12 dus
  uiterlijk **30 juni**.
- Neerlegging bij NBB binnen **30 dagen na goedkeuring** én **uiterlijk
  7 maanden** na afsluitdatum ([[WVV#art-3-10]] ⚠️ exact artikel te
  verifiëren) — voor een boekjaar dat eindigt op 31/12 dus uiterlijk
  **31 juli**. *Bron: [[CBN-2020-08]]* ⚖️

#### 1. Inventaris

⚖️ Het bestuursorgaan is **wettelijk verplicht** om **elk jaar een
inventaris** op te maken volgens de door de Koning bepaalde
waarderingsregels (artikel 3:1 §1 WVV). De inventaris is een
**genummerde lijst** van álle activa- en passivabestanddelen op
afsluitingsdatum, met **waarde** per bestanddeel — typisch in het
**inventarisboek**.

🔗 Waarderingsregels worden door het bestuursorgaan vastgelegd in het
inventarisboek; een **samenvatting** komt in de toelichting. *Bron:
[[CBN-2019-04]] · [[KB-WVV#art-3-1]] e.v.* ⚖️

🧭 In de praktijk omvat de inventaris ook: voorraadinventarisatie
(fysieke telling), bevestiging van vorderingen en schulden,
bankbevestiging, controles op werk-in-uitvoering, debiteuren-aging,
voorzieningen-evaluatie.

#### 2. Eindejaars-boekingen

🔗 Op basis van de inventaris worden de **eindejaars-correcties**
geboekt:
- **Afschrijvingen** vaste activa (incl. oprichtingskosten — zie
  [[oprichtingskosten-v1]])
- **Waardeverminderingen** op voorraden, vorderingen, financiële
  vaste activa
- **Voorzieningen** voor risico's en kosten
- **Toe te rekenen kosten** (rente, huur, vakantiegeld) en **over te
  dragen kosten/opbrengsten**
- **Herwaarderingen** (indien gekozen) — strikte CBN-voorwaarden
- **Belastingen** (vennootschapsbelasting, uitgestelde belastingen)
- **Bestemming reserves uit voorgaande boekjaren** (wettelijke,
  beschikbare, onbeschikbare reserves)

⚖️ Definitie afschrijvingen + waardeverminderingen in [[KB-WVV#art-3-23]].

#### 3. Proefbalans en afsluiting

🔗 Na de eindejaars-boekingen wordt een **proefbalans** opgesteld
(controle: totaal debet = totaal credit, kolom-totalen sluiten). Dat
levert de **netto-eindwaardes** per rekening op die in balans en
resultatenrekening worden ingelezen.

#### 4. Opmaak jaarrekening (door het bestuursorgaan)

⚖️ Het bestuursorgaan **stelt de jaarrekening op** in de bij het KB
WVV bepaalde **vorm en inhoud** (artikel 3:1 §1 WVV). Concreet: balans,
resultatenrekening, toelichting + (indien volledig schema) jaarverslag.

🔗 Bij **duaal bestuur** in een NV is de **raad van toezicht**
exclusief bevoegd voor de **vaststelling** (= opmaak) van de
jaarrekening; de directieraad kan voorbereiden en uitvoeren, maar de
verantwoordelijkheid blijft bij de raad van toezicht. *Bron:
[[CBN-2020-09]]* ⚖️

#### 5. Commissaris-controle (indien aangesteld)

⚖️ Indien een **commissaris** is aangesteld, overhandigt het
bestuursorgaan hem de nodige stukken **minstens één maand** vóór de
geplande AV (45 dagen bij genoteerde vennootschappen). De commissaris
stelt een **omstandig schriftelijk verslag** op. *Bron:
[[WVV#art-3-71]] (MvT) · [[WVV#art-3-75]]* ⚖️

🔗 Wanneer een **ondernemingsraad** is opgericht, is een commissaris
**verplicht** — zie [[WVV#art-3-72]] e.v. ⚠️ exacte verplichting te
verifiëren.

#### 6. AV-goedkeuring

⚖️ Binnen **6 maanden** na afsluitingsdatum legt het bestuursorgaan de
jaarrekening ter **goedkeuring** voor aan de algemene vergadering
(vennootschappen — [[WVV#art-3-1]] §1; vzw's — [[WVV#art-3-47]] §1).

🧭 Bij **niet-tijdige voorlegging** wordt schade die derden lijden
"behoudens tegenbewijs geacht voort te vloeien uit dit verzuim"
([[WVV#art-3-1]] §1 in fine ⚖️) — een **bewijslastomkering** die de
bestuurders motiveert om de termijn strikt na te leven.

🔗 De AV beslist over:
- **Goedkeuring** van de jaarrekening
- **Resultaatverwerking** (zie [stap 7](#7-resultaatverwerking))
- **Kwijting** aan bestuurders (en, indien aanwezig, commissaris)

#### 7. Resultaatverwerking

🔗 Uit het resultaat van het boekjaar (winst of verlies) plus het
**overgedragen resultaat** beslist de AV over:
- Aanleg of dotatie aan **wettelijke reserve** (NV: 5 % van nettowinst
  tot reserve = 10 % van kapitaal; ⚠️ exact artikel WVV te verifiëren —
  voor BV vervalt het bij gebrek aan kapitaal-begrip)
- Dotatie aan **beschikbare reserves** of **onbeschikbare reserves**
- **Dividenden** aan aandeelhouders — **onder voorbehoud** van de
  netto-actief-toets en (BV) de liquiditeitstest. Zie
  [[uitkering-aan-aandeelhouders-v1]].
- **Overgedragen winst/verlies** naar het volgende boekjaar
- (BV/CV) **inhouding van interimdividenden** indien al uitgekeerd

⚖️ **Netto-actief-toets** voor uitkering: geen uitkering indien netto-
actief gedaald is of zou dalen onder gestort kapitaal + onbeschikbare
reserves. Voor de berekening worden de **niet-afgeschreven
oprichtingskosten + uitbreidingskosten + kosten O&O** **afgetrokken**
van het netto-actief — tenzij uitzonderlijk gemotiveerd in de
toelichting. *Bron: [[WVV#art-7-212]]* ⚖️

🔗 Dat artikel verklaart waarom oprichtingskosten **geactiveerd** een
**uitkeringsbeperking** veroorzaken — zie [[oprichtingskosten-v1]],
sectie "Uitkeringsverbod".

#### 8. Neerlegging bij de NBB

⚖️ Binnen **30 dagen na goedkeuring** door de AV legt het
bestuursorgaan de jaarrekening neer bij de **Nationale Bank van
België** (Balanscentrale), én **uiterlijk 7 maanden** na de
afsluitingsdatum van het boekjaar. *Bron: [[WVV#art-3-10]]
([[CBN-2020-01]]) · [[CBN-2020-08]]* ⚖️

🔗 Worden samen neergelegd:
- de **jaarrekening** zelf (balans + resultatenrekening + toelichting)
- het **jaarverslag** (indien verplicht)
- het **verslag van de commissaris** (indien verplicht)
- de **gegevens van bestuurders en commissaris** ([[CBN-2020-09]])
- een **sociale balans** (indien drempel 20 vte bereikt)
- het **resultaatverwerkings-besluit** van de AV

⚖️ **Aanvaarding**: de NBB controleert rekenkundige en logische
consistentie. Tenzij andersluidend bericht binnen 8 werkdagen geldt de
neerlegging als aanvaard. Bij **wezenlijke fouten** moet de vennootschap
**binnen 2 maanden** een verbeterde versie neerleggen. *Bron:
[[WVV#art-3-14]] (MvT)* ⚖️

🧭 **Praktische valkuil**: vergeet het besluit van resultaatverwerking
niet bij de stukken; een onvolledige neerlegging riskeert kost en
boete bij heraanvraag.

#### Voor (i)vzw's en stichtingen — afwijkende route

🔗 **Kleine** vzw's/ivzw's/stichtingen (onder de drempels van artikel
3:47 §2 WVV) leggen niet neer bij de NBB maar bij de **griffie van de
ondernemingsrechtbank** — opname in het verenigings- of
stichtingsdossier. *Bron: [[CBN-2020-07]] · [[CBN-2020-12]]* ⚖️

### De waarderingsregels (verplicht onderdeel)

🔗 De **waarderingsregels** zijn **geen optioneel addendum** maar een
**verplicht onderdeel van de toelichting**. Drie functies:

1. **Documenteren** welke keuzes het bestuursorgaan gemaakt heeft
   binnen de wettelijke speelruimte (afschrijvingsmethode, spreiding
   agio/disagio, voorraadwaardering FIFO/LIFO/gemiddeld, …)
2. **Verantwoorden** dat de jaarrekening een **getrouw beeld** geeft
3. **Consistentie** afdwingen — eenmaal gekozen, blijft de regel
   gelden tot expliciete wijziging die toegelicht moet worden

⚖️ "Het bestuursorgaan bepaalt de door haar toegepaste waarderingsregels
rekening houdend met de eigen kenmerken van het bedrijf. Deze
waarderingsregels worden vastgelegd in het inventarisboek. Een
samenvatting van deze waarderingsregels moet worden opgenomen in de
toelichting." *Bron: [[CBN-2019-04]]* ⚖️

🔗 Praktische inhoud van een waarderingsregels-samenvatting:

| Domein | Te vermelden keuze |
|---|---|
| **Oprichtingskosten** | Activeren of in resultaat? Spreiding? Bij uitgifte leningen: spreiding over looptijd? |
| **Immateriële vaste activa** | Afschrijvingstermijn (max 10 j voor O&O onbepaalde gebruiksduur) |
| **Materiële vaste activa** | Lineair / degressief / proportioneel; jaar van inwerkingstelling pro rata |
| **Herwaarderingen** | Toegepast? Op welke posten? Methode? |
| **Voorraden** | FIFO / LIFO / gewogen gemiddelde / individueel |
| **Vorderingen** | Methode waardeverminderingen (statistisch, individueel) |
| **Schulden in vreemde munt** | Koers per balansdatum + behandeling van koersverschillen |
| **Voorzieningen** | Criteria voor opname; berekeningsmethode |
| **Agio/disagio op leningen** | Lineair vs effective interest; spreiding over looptijd |

🧭 **Valkuil**: een **boilerplate** waarderingsregels-tekst die niet
overeenstemt met wat in de cijfers gebeurt is een veelvoorkomende fout
bij niet-gecontroleerde jaarrekeningen. CBN 112/8 waarschuwt expliciet
voor onvoldoende nauwkeurigheid in de samenvatting.

⚖️ "De waarderingsregels moeten van jaar tot jaar gelijk blijven" —
**consistentiebeginsel**. Wijziging vereist verantwoording in de
toelichting + impact-vermelding. *Bron: [[CBN-2019-04]]* ⚖️

## Rol van de accountant

*De jaarrekening is het meest universele werk-artefact van de
accountant. Drie klant-perspectieven, één extern controle-perspectief.*

### 🏢 Voor de vennootschap (bestuur · ondernemer)

#### 🎯 Adviseur

**Wat doe je**:
- 🧭 **Formaat-keuze begeleiden** — bewaken of de vennootschap onder
  klein/micro blijft of moet doorschakelen; effect op
  rapporteringsverplichtingen, jaarverslag, commissaris.
- 🧭 **Groottecategorie-monitoring** over twee opeenvolgende boekjaren
  (consistentiebeginsel — automatische overschakeling pas na twee jaar).
- 🧭 **Waarderingsregels-keuzes adviseren** in functie van het beeld dat
  de vennootschap wil tonen (winst-spreiding via afschrijvingstempo,
  voorraadwaardering, voorzieningen).
- 🔗 **Resultaatverwerking-strategie** — interactie met dividendpolitiek
  en netto-actief-toets ([[uitkering-aan-aandeelhouders-v1]]).
- 🧭 **Going-concern-discussie** wanneer ratio's of resultaten zwak zijn
  — zie [[jaarrekeninganalyse-v1]] §going-concern.

#### 📋 Boekhouder

**Wat doe je** (zie [De cyclus](#de-cyclus-van-inventaris-tot-neerlegging)
voor de chronologie):

1. **Inventaris opmaken** (per rekening, met onderliggende
   documentatie) en in inventarisboek vastleggen.
2. **Eindejaars-boekingen** verzorgen (afschrijvingen,
   waardeverminderingen, voorzieningen, prorata, herwaardering).
3. **Proefbalans** afsluiten en consistentie controleren met
   sub-administraties (klanten, leveranciers, vaste activa, voorraad).
4. **Jaarrekening opmaken** in het juiste schema (volledig/verkort/micro)
   inclusief toelichting + waarderingsregels.
5. **Sociale balans** opmaken indien drempel bereikt.
6. **Neerleggingsdossier** voorbereiden voor NBB (formaat, bijlagen,
   resultaatverwerking-besluit).
7. **Tijdige neerlegging** binnen 30 dagen na AV en uiterlijk 7 maanden
   na afsluiting. Boete- en herstelkostbeheersing.

##### Uitvoerings-valkuilen voor de boekhouder

- ⚖️ **Niet-tijdige voorlegging aan AV** (later dan 6 maanden) →
  bewijslastomkering bij derdenschade. *Bron: [[WVV#art-3-1]] §1* ⚖️
- ⚖️ **Niet-tijdige neerlegging bij NBB** (later dan 7 maanden) →
  vermoeden van bestuurdersfout bij derden + administratieve boetes
  ⚠️ tarief te verifiëren.
- 🔗 **Waarderingsregels onvolledig of inconsistent met cijfers** —
  zie CBN 112/8.
- 🔗 **Sociale balans vergeten** wanneer drempel 20 vte net overschreden
  wordt.
- 🔗 **Resultaatverwerking ontbreekt** bij neerlegging.
- 🧭 **Onbeschikbare reserves verkeerd geclassificeerd** (wettelijke
  reserve vs herwaarderingsmeerwaarde-reserve vs niet-uitkeerbare door
  oprichtingskosten) → fout bij volgende uitkering-toets.

#### 🔍 Begeleider — relatie met externe partijen

🧭 De accountant is typisch het **eerste aanspreekpunt** bij:
- vragen van de NBB-balanscentrale over rekenkundige inconsistenties
- vragen van de fiscus die de aangifte vennootschapsbelasting koppelt
  aan de neergelegde jaarrekening
- vragen van **banken** (kredietdossier) of **leveranciers**
  (commercieel onderzoek) op basis van NBB-publicatie

### 🔍 Voor de auditor / commissaris (extern perspectief)

⚖️ De **commissaris** (wettelijke controle, ISA-conform) levert het
**verslag van de commissaris** dat samen met de jaarrekening wordt
neergelegd. *Bron: [[WVV#art-3-75]]* ⚖️

#### Controle-aandachtspunten

- ⚖️ **Inventarisaanwezigheid** en match met balansposten (kasaudit,
  voorraadbijwoning, bevestigingen).
- ⚖️ **Waarderingsregels** — consistentie met voorgaande jaren, juiste
  toepassing op de cijfers, volledigheid van samenvatting in toelichting.
- ⚖️ **Toelichting volledig** — niet-in-balans-genomen verplichtingen,
  gebeurtenissen na balansdatum, transacties verbonden partijen,
  bezoldigingen bestuurders.
- ⚖️ **Vorm conform schema** — Bijlage 3/4/microschema correct
  toegepast voor het juiste groottesegment.
- ⚖️ **Going-concern-veronderstelling** — beoordeeld op basis van
  ratio's + cashflow + management-prognose (ISA 570 ⚠️).
- 🔗 **Resultaatverwerking-besluit** consistent met de getoonde cijfers
  en met de wettelijke uitkeringsbeperkingen (artikel 7:212 e.v.).
- 🔗 **Sociale balans** correct opgesteld indien drempel bereikt.

⚖️ Indien het bestuursorgaan in gebreke blijft de stukken tijdig (≥ 1
maand vóór AV) over te maken, stelt de commissaris een **verslag van
niet-bevinding** op. *Bron: [[WVV#art-3-71]] (MvT)* ⚖️

### 💰 Voor de fiscus (indirect — via aangifte vennootschapsbelasting)

🔗 De **goedgekeurde en neergelegde jaarrekening** is de **basis** voor
de fiscale aangifte. De accountant maakt de **fiscale aansluiting**
tussen het boekhoudkundig resultaat en het belastbaar resultaat (DOC,
verworpen uitgaven, aftrekken, …).

🧭 *Niet hier in detail* — zie aangifte vennootschapsbelasting-fiches.
Wel relevant: **wezenlijke fouten** in de neergelegde jaarrekening
kunnen de fiscale grondslag wijzigen en vereisen
**correctie-neerlegging** ([[WVV#art-3-14]]) + eventueel een gewijzigde
aangifte.

## Veelvoorkomende verwarringen

- **Jaarrekening ≠ jaarverslag.** De jaarrekening is het *cijferdeel*
  (balans + resultatenrekening + toelichting). Het jaarverslag is het
  *narratief deel* van het bestuursorgaan. Beide worden samen
  neergelegd maar zijn juridisch aparte documenten — vrijstelling
  jaarverslag voor klein/micro raakt de jaarrekening niet.
- **Jaarrekening ≠ aangifte vennootschapsbelasting.** De jaarrekening
  is een **boekhoudkundig** document; de aangifte is een **fiscaal**
  document. De aangifte vertrekt vanuit de jaarrekening maar wijkt
  ervan af via verworpen uitgaven, DBI, fiscale aftrekken, enz.
- **Sociale balans ≠ sociaal verslag.** De sociale balans is een
  **gestructureerde tabel** in de toelichting (vte, loonkost,
  scholing) — wettelijk verplicht boven 20 vte. Niet te verwarren met
  het bredere sociaal verslag (ESG, duurzaamheidsrapportering).
- **Klein vs micro verschilt op één punt naast de drempels**: een
  micro-vennootschap mag **geen dochter of moeder** zijn ([[WVV#art-1-25]]
  §1 ⚖️). Een klein-vennootschap mag dat wel.
- **Verkort schema ≠ vereenvoudigde boekhouding.** Het verkort schema
  is een *jaarrekeningformaat* voor entiteiten met dubbele boekhouding.
  Een vereenvoudigde boekhouding (kas-uitgaven/inkomsten, alleen voor
  zeer kleine vzw's en eenmanszaken) levert een ander type artefact —
  zie [[KB-WVV#art-3-186]] e.v. ⚠️
- **Goedkeuring AV ≠ neerlegging.** Goedkeuring is een interne
  vennootschapshandeling; neerlegging is de externe publicatie.
  Beide moeten binnen aparte termijnen plaatsvinden (6 m vs 7 m na
  boekjaar).

## Familie & alternatieven

🔗 *Hier geen "alternatieven" — de jaarrekening is het wettelijk
verplichte artefact, niet kiesbaar.* Wel:

### Varianten binnen dezelfde familie

- **Enkelvoudige jaarrekening** ↔ **[[geconsolideerde-jaarrekening]]**
  (voor moedervennootschappen — eigen schema, eigen drempels)
- **BGAAP-jaarrekening** ↔ **IFRS-jaarrekening** ([[IFRS-vs-BGAAP]] —
  IFRS verplicht voor genoteerde geconsolideerde; toegestaan voor
  geconsolideerde van financiële instellingen; ⚠️ exacte regels)
- **Boekjaar = kalenderjaar** ↔ **Boekjaar afwijkend** (verschuift alle
  termijnen pro rata)

### Aanverwante artefacten

- **[[interimstaat]]** of **tussentijdse jaarrekening** — voor
  interimdividend, herstructurering, omzetting; ITAA-norm
  effecten/omzetting van toepassing.
- **[[staat-van-activa-en-passiva]]** — bij omzetting, fusie, splitsing;
  ITAA-norm omzetting-vennootschap.
- **[[liquidatie-jaarrekening]]** — bij vereffening, andere
  waarderingsregels.

## Wat dit record dekt

*Voor een stagiair GA: een check-lijst van competenties (chronologisch,
in volgorde van uitvoeren binnen het jaar-cyclus) + termen
(alfabetisch).*

### Behandelde competenties (chronologisch)

1. **Groottecategorie bepalen** voor de vennootschap of vereniging
   (klein/micro/groot — geconsolideerd of enkelvoudig) — zie
   [Formaten](#formaten-volledig-verkort-micro).
2. **Schema kiezen** (volledig / verkort / micro / vereenvoudigd) —
   zie [Vergelijkingstabel](#vergelijkingstabel--vennootschappen).
3. **Waarderingsregels formuleren** en in inventarisboek vastleggen —
   zie [Waarderingsregels-bijlage](#de-waarderingsregels-verplicht-onderdeel).
4. **Inventaris opmaken** met onderliggende documentatie — zie
   [stap 1](#1-inventaris).
5. **Eindejaars-boekingen** uitvoeren (afschrijvingen,
   waardeverminderingen, voorzieningen, prorata, herwaardering,
   belastingen) — zie [stap 2](#2-eindejaars-boekingen).
6. **Proefbalans** opmaken en consistentie controleren — zie
   [stap 3](#3-proefbalans-en-afsluiting).
7. **Jaarrekening opmaken** in het juiste schema, met toelichting en
   waarderingsregels — zie [stap 4](#4-opmaak-jaarrekening-door-het-bestuursorgaan).
8. **Sociale balans** opmaken indien drempel 20 vte bereikt — zie
   [Sociale balans](#sociale-balans).
9. **Jaarverslag** voorbereiden indien volledig schema (samenwerking
   met bestuursorgaan) — zie [Jaarverslag](#jaarverslag).
10. **Stukken overhandigen aan commissaris** minstens 1 maand vóór AV —
    zie [stap 5](#5-commissaris-controle-indien-aangesteld).
11. **Jaarrekening voorleggen aan AV** binnen 6 maanden — zie
    [stap 6](#6-av-goedkeuring).
12. **Resultaatverwerking** voorbereiden (rekening houdend met
    netto-actief-toets en oprichtingskosten-aftrek) — zie
    [stap 7](#7-resultaatverwerking).
13. **Neerleggingsdossier** samenstellen en binnen 30 dagen na AV
    indienen bij NBB (uiterlijk 7 m na afsluiting) — zie
    [stap 8](#8-neerlegging-bij-de-nbb).
14. **Verbeterneerlegging** verzorgen bij wezenlijke fouten — zie
    [Aanvaarding](#8-neerlegging-bij-de-nbb).
15. **Auditor-controle** als commissaris uitvoeren — zie
    [auditor-rol](#-voor-de-auditor--commissaris-extern-perspectief).

### Behandelde termen (alfabetisch)

afsluitingsdatum · balans · balansdatum · balanscentrale ·
commissaris · consistentiebeginsel · duaal bestuur · eindejaars-
boekingen · enkelvoudige jaarrekening · geconsolideerde jaarrekening ·
getrouw beeld · groottecriteria · inventaris · inventarisboek ·
jaarverslag · klein · macro-/microschema · micro · NBB-neerlegging ·
netto-actief-toets · onbeschikbare reserves · oprichtingskosten-aftrek ·
proefbalans · resultatenrekening · resultaatverwerking · samenvatting
waarderingsregels · sociale balans · toelichting · verbeterneerlegging ·
volledig schema · waarderingsregels · wettelijke reserve

### Behandelde formules (op kader-niveau)

Geen specifieke formules — wel deze structurele identiteiten:

- **Balans-identiteit**: *Totaal Actief = Totaal Passief (= EV + VV)*
- **Resultaat-identiteit**: *Opbrengsten − Kosten = Winst (of Verlies)
  van het boekjaar*
- **Netto-actief-toetswaarde** = *Activa − Voorzieningen − Schulden −
  niet-afgeschreven oprichtings/uitbreidings/O&O-kosten*

### Behandelde regimes (via edges)

- [[uitkering-aan-aandeelhouders-v1]] (netto-actief-toets,
  liquiditeitstest BV) — `gerelateerd`
- [[alarmbel-procedure]] (bij negatief of sterk verminderd netto-actief)
  — `triggert_procedure`
- [[continuiteit-going-concern]] — `gerelateerd`
- [[wettelijke-controle-isa]] — `gecontroleerd_door`
- [[centrale-balansen-nbb]] — `gepubliceerd_via`
- IFRS-regime ([[IFRS-vs-BGAAP]]) voor genoteerde groepen —
  `alternatief_referentiestelsel`

## Bronnen en verwijzingen

**Bronnen (grounded)** ⚖️:

- [[WVV#art-3-1]] § 1 — opmaakplicht jaarrekening + 6-maanden-AV-termijn
- [[WVV#art-3-10]] — neerlegging bij NBB (30 dagen + 7 maanden)
- [[WVV#art-3-14]] (MvT) — aanvaardingscontrole NBB + verbeterneerlegging
- [[WVV#art-3-47]] — analoog voor vzw/ivzw
- [[WVV#art-3-71]] (MvT) — stukken aan commissaris + verslag van
  niet-bevinding
- [[WVV#art-3-75]] — inhoud verslag commissaris
- [[WVV#art-7-212]] — netto-actief-toets bij uitkering + oprichtings-
  kosten-aftrek
- [[WVV#art-1-24]] — groottecriteria vennootschap (klein)
- [[WVV#art-1-25]] — groottecriteria microvennootschap
- [[WVV#art-1-28]] / [[WVV#art-1-29]] — analoge criteria vzw/stichting
- [[KB-WVV#art-3-23]] — definitie afschrijvingen/waardeverminderingen
- [[KB-WVV#art-3-80]] — balans volledig schema (Bijlage 3)
- [[KB-WVV#art-3-83]] — balans verkort schema (Bijlage 4)
- [[KB-WVV#art-3-84]] — microschema balans
- [[KB-WVV#art-3-161]] — sociale balans in toelichting (vzw/ivzw —
  drempel 20 vte)
- [[CBN-2019-04]] — vastlegging waarderingsregels door bestuursorgaan +
  samenvatting in toelichting
- [[CBN-112-8]] — waarderingsregels-nauwkeurigheid
- [[CBN-2019-12]] — groottecriteria vzw/stichting + schema's
- [[CBN-2020-01]] — neerlegging enkelvoudige jaarrekening NBB
- [[CBN-2020-07]] · [[CBN-2020-08]] — uitstel AV en neerlegging (COVID-
  context, maar bevestigt de standaardtermijnen 6 m en 7 m)
- [[CBN-2020-09]] — vermelding bestuurders en commissaris in jaarrekening
- [[CBN-2020-12]] — correctie jaarrekening
- [[CBN-2022-03]] — beoordeling groottecriteria (geconsolideerd of
  geaggregeerd voor moeder)

**Te verifiëren** ⚠️:

- Exact KB-WVV-artikel voor schema "per functie" resultatenrekening
- Exact WVV-artikel voor vrijstelling jaarverslag klein/micro
- Exact KB-WVV-artikel voor samenvatting waarderingsregels in
  toelichting (vermoedelijk art. 3:90 e.v.)
- Exact WVV-artikel voor verplichte aanstelling commissaris bij
  ondernemingsraad
- Exact WVV-artikel voor wettelijke reserve NV (vermoedelijk 7:211 ⚠️)
- ISA 570 (going concern) — auditor-context
- Boete-tarieven niet-tijdige neerlegging NBB
- IFRS-verplichting genoteerde groepen + financiële instellingen
- Pre-2024-grootte-drempels voor historische jaarrekeningen
- Consistentiebeginsel: twee-jaars-regel bij groottewijziging

**Cross-record edges**:

- `heeft_lid` → [[balans-onderdeel]], [[resultatenrekening-onderdeel]],
  [[toelichting-onderdeel]], [[jaarverslag]], [[sociale-balans]],
  [[waarderingsregels-onderdeel]]
- `heeft_balanspost` → [[oprichtingskosten-v1]],
  [[immateriele-vaste-activa]], [[materiele-vaste-activa]],
  [[voorraden]], [[handelsvorderingen]], [[liquide-middelen]],
  [[eigen-vermogen]], [[voorzieningen]], [[schulden-meer-dan-een-jaar]],
  [[schulden-minder-dan-een-jaar]], …
- `valt_onder_kader` ← [[oprichtingskosten-v1]],
  [[obligatielening-v7]], [[uitkering-aan-aandeelhouders-v1]]
- `gerelateerd` → [[jaarrekeninganalyse-v1]] (lezen),
  [[geconsolideerde-jaarrekening]], [[IFRS-vs-BGAAP]],
  [[boekjaar]], [[inventaris]]
- `triggert_procedure` → [[alarmbel-procedure]] (bij negatief
  netto-actief)
- `gecontroleerd_door` → [[wettelijke-controle-isa]]
- `gepubliceerd_via` → [[centrale-balansen-nbb]]
- `verward_met` → [[jaarverslag]] ↔ jaarrekening,
  [[aangifte-vennootschapsbelasting]] ↔ jaarrekening,
  [[sociale-balans]] ↔ [[duurzaamheidsverslag]]
- `kiesbaar_schema` → [[volledig-schema]], [[verkort-schema]],
  [[microschema]]

---

## Iteratie-log

**v1 (huidige)** — eerste POC mockup als **kind: kader** met de
artefact-componenten (balans, resultatenrekening, toelichting,
jaarverslag, sociale balans) en de **cyclus** als **interne secties**.
Test of dit beter werkt dan een opsplitsing **kind: artefact** +
**kind: procedure**.

### 1. Werkt het patroon?

**Wat werkt**:
- **Eén-fiche-aanpak met cyclus binnen** geeft een **integrale leesfijn
  ervaring**: de stagiair die de jaarrekening begrijpt vindt op één
  plek artefact + tijdslijn + waarderingsregels + neerleggingseis +
  resultaatverwerking-link. Geen *jumping* tussen records.
- **Element-vocabulaire** werkt goed voor het vergelijkingsschema
  (vergelijkingstabel-weergave) en de cyclus (tijdslijn-weergave).
- **Rol-sectie** is leesbaar: vennootschap-perspectief krijgt 3 rollen
  (adviseur · boekhouder · begeleider); auditor heeft eigen blok;
  fiscus krijgt een kort kruisverwijzings-blok.
- **Cross-edge naar [[oprichtingskosten-v1]]** via netto-actief-toets
  + waarderingsregels werkt vloeiend — die uitzondering hoeft in beide
  records vermeld te zijn maar zonder duplicatie van detail.

**Wat schuurt**:
- **Lengte**: meer dan 700 regels. Voor één concept-fiche aan de
  bovengrens; de cyclus-sectie alleen al loopt 200+ regels. Render-laag
  zal collapsibility hard moeten gebruiken (default dicht voor
  cyclus-detail-stappen).
- **Component-detail (balans, resultatenrekening, toelichting)** blijft
  oppervlakkig — alleen "wat het is, vorm, KB-artikel". Een **echte**
  balans-fiche zou MAR-rubrieken bespreken, een resultatenrekening-fiche
  zou opbrengstrubrieken vs kostenrubrieken behandelen. Hier dus
  **stub** met `heeft_lid` → eigen records.
- **Sociale balans + jaarverslag** voelen als **bijzaken** in deze
  fiche — terwijl ze juridisch significant zijn. Mogelijk eigen records
  rechtvaardigen.
- **Cyclus stap 5 (commissaris-controle)** botst met de scope van
  [[wettelijke-controle-isa]] — wat hier hoort en wat daar? Voorlopig
  hier alleen de **interactie** beschreven; ISA-detail naar eigen record.

### 2. Voor jaarrekening: één fiche met cyclus binnen, of toch twee?

**Argument voor één fiche** *(huidige keuze)*:
- De cyclus is **niet zinvol los van het artefact** — een leerling die
  alleen "hoe maak je een jaarrekening op" leest mist de **waarom-cijfers
  in dit schema**.
- De **waarderingsregels** zijn zowel artefact-onderdeel (sectie van
  toelichting) als cyclus-onderdeel (output van stap 1-2). Splitsen
  zou dwingen tot duplicatie of cross-link-flikkering.
- **Renderbaarheid** met collapsibility (per ADR-010) lost de
  lengte-bezorgdheid op.

**Argument voor twee fiches** *(verworpen voor POC, herzien indien
render lengte niet aankan)*:
- **Procedure-kind** heeft een eigen taal (actoren, formaliteiten,
  termijnen, deadlines met sancties) die anders is dan artefact-taal
  (vorm, inhoud, structuur). Mengen levert een hybride op.
- **Cross-PO-bereikbaarheid**: cyclus-vragen op het examen
  (PO 1.1 + PO 1.4) kunnen apart van artefact-vragen (PO 1.1) aan bod
  komen. Twee records zou directere link naar examenpatronen mogelijk
  maken.

**Beslissing voor de POC**: **één fiche** met cyclus als sub-sectie.
Mogelijk in productie *artefact-jaarrekening* als kader en *opmaak-
cyclus-jaarrekening* als procedure-lid uitsplitsen, maar dat is
herzienbaar op basis van rendering + examenpatroon-fit.

### 3. Aanbevelingen voor de skeleton-voorstel-prompt of EXTRACT v5

- **Kind `kader` voor wettelijk verplichte rapporteringsartefacten**:
  de definitie van kader in ADR-025 ("cross-cutting denkraam met eigen
  taken") past zonder spanning — *cross-cutting* slaat hier op
  cross-balanspost (elke balanspost komt voor in dit kader).
- **Element-vocabulaire-uitbreiding**: voeg `tijdslijn-illustratie`
  (eigen ASCII of mermaid-render) toe als weergavetype. De cyclus-
  illustratie hierboven is een eerste poging.
- **Vergelijkingstabel-weergave** met emojis voor selectie-context
  (klein/micro/groot) werkt goed in markdown. Stagiair kan visueel
  scannen.
- **"Wanneer is dit van toepassing"** (vs "Wanneer kies je dit") als
  sectie-variant voor **verplichte artefacten zonder keuze-aspect**.
  ADR-025 erkent al de variabiliteit; expliciet in EXTRACT v5-prompt
  als alternatief noemen vermijdt forceerd "speelruimte" waar er geen
  is.
- **Bibliotheek van rol-templates**: vennootschap × adviseur, vennootschap
  × boekhouder, vennootschap × begeleider, vennootschap × fiscaal,
  extern × auditor — herbruikbaar voor andere kader-fiches.
- **Cyclus-pattern voor procedure-vlechtwerk** binnen kader: één
  ASCII-illustratie + recursieve `### Stap N`-secties met confidence-
  emoji per stap. Werkt voor elke wettelijke sequentie (uitkering,
  fusie, kapitaalverhoging).

### 4. Open punten

- **Sub-records voor balans, resultatenrekening, toelichting** —
  wenselijk maar zelf weer kader-achtig (de balans heeft 10+ rubrieken).
  Mogelijk **balans = kader** met balansposten als leden? Dat is de
  vraag die door [[oprichtingskosten-v1]] gevalideerd wordt.
- **Genoteerde vennootschap-IFRS-track** is hier afwezig. Verdient
  een eigen kader-fiche [[IFRS-vs-BGAAP]] of een sub-sectie hier?
- **Tussentijdse jaarrekeningen** (interim, fusie-tussenstand,
  vereffening) — eigen records of variantsectie?
- **NBB-publicatie als data-stream** (XBRL, gestructureerde data) — een
  techniek die de accountant moet kennen maar conceptueel weinig
  toevoegt. Vermoedelijk eigen record [[centrale-balansen-nbb]].
