---
title: "Oprichtingskosten — v1 (POC mockup balanspost)"
tags:
  - experiment
  - mockup
  - balanspost
status: experimental
mockup: true
linked_anchors:
  - "1.1.II.J"
  - "1.1.II.S"
---

> **POC mockup** — test of **`balanspost`** als nieuw kind (sub-
> vocabulaire van `begripscluster`) didactisch werkt voor een rubriek
> die juridisch én boekhoudkundig één plaats op de balans inneemt
> (MAR 20) maar conceptueel **vier componenten** + **één belangrijke
> uitzondering** + **één uitkeringsverbod-gevolg** bundelt.
>
> De **uitzondering obligatie-uitgiftekosten** (mag over heelfile-
> looptijd worden gespreid i.p.v. max 5 jaar) staat hier expliciet als
> element met `is_uitzondering_op`-edge — in toekomstige
> [[obligatielening-v7|obligatielening]]-fiche komt dit terug als
> verwijzing.
>
> Vergelijk met:
> [[obligatielening-v7|obligatielening (instrument)]] ·
> [[solvabiliteitsratio-v2|solvabiliteit (ratio)]] ·
> [[jaarrekening-v1|jaarrekening (kader)]] ·
> [[vvprbis-v1|VVPRbis (fiscale regeling)]].
>
> **Confidence-tekens** (per claim):
> ⚖️ uit wet · KB · CBN · norm (grounded)
> 🔗 redenering uit bronnen (inferred)
> 🧭 beroepswijsheid, geen harde regel (vuistregel)
> ⚠️ bron ontbreekt of nog te verifiëren
> ❌ tegenstrijdig (gecheckt en fout)

# Oprichtingskosten

**Oprichtingskosten** zijn **bepaalde aanloop-, uitgifte- of
herstructureringskosten** die de vennootschap maakt en die — in plaats
van direct als kost van het jaar door de resultatenrekening te lopen —
**geactiveerd** mogen worden op de balans (MAR-rubriek 20) om
**gespreid in de tijd** te worden afgeschreven.

*Bron: [[KB-WVV#art-3-36]] · [[KB-WVV#art-3-37]] · [[CBN-2010-15]]* ⚖️

## Wat er economisch echt gebeurt

**Eenmalige opstart-, uitgifte- of herstructureringskosten zijn vaak
hoog ten opzichte van het resultaat van het jaar waarin ze worden
betaald.** Wie ze in dat ene jaar volledig ten laste neemt, krijgt
**een kunstmatig verlies** dat geen verband houdt met de **economische
realiteit**: die kosten dienen immers de **toekomst** van de
onderneming (oprichting, kapitaalverhoging, leningenuitgifte,
herstructurering met "gunstige en duurzame invloed op de rentabiliteit").

🔗 **Activeren** is de oplossing: de kost wordt op de balans gezet
(actief), zodat de resultatenrekening alleen het **stuk van dit jaar**
draagt (afschrijving), en de rest pas in latere jaren.

🔗 **Maar** — en hier zit de hele kunst — die activering creëert een
**boekhoudkundig waardevol bestanddeel** dat economisch **geen
verkoopwaarde** heeft. De wetgever heeft daarom twee tegenmaatregelen
ingebouwd:

1. **Snelle afschrijving** verplicht — minstens 20 %/jaar (max 5 jaar)
   voor de meeste oprichtingskosten ⚖️.
2. **Uitkeringsverbod** — zolang oprichtingskosten niet volledig
   afgeschreven zijn mag de netto-actief-toets ze niet meerekenen
   (artikel 7:212 WVV). Zie [Uitkeringsverbod](#uitkeringsverbod-tot-volledige-afschrijving).

Dat tweede gevolg is **vaak miskend** door bestuurders die het volle
"papieren" eigen vermogen willen uitkeren — daar moet de accountant
proactief op wijzen.

## Voorkennis & leespad

- **Lees eerst** (voorvereisten): [[matching-beginsel]] · [[balans]] ·
  [[mar-rekeningenstelsel]] · [[afschrijvingen]]
- **Past binnen kader**: [[jaarrekening-v1]] (de oprichtingskosten zijn
  één balanspost binnen het jaarrekening-artefact)
- **Naast deze fiche relevant**: [[obligatielening-v7]] (uitgiftekosten
  van obligaties = bijzonder regime) · [[kapitaalverhoging]]
  (kosten bij kapitaalverhoging activeerbaar) · [[fusie-splitsing]]
  (herstructureringskosten) · [[uitkering-aan-aandeelhouders-v1]]
  (netto-actief-toets met oprichtingskosten-aftrek)
- **Bij vervolgvragen**: [[onderzoek-en-ontwikkeling]] (analoog regime,
  ander artikel) · [[goodwill]] · [[immateriele-vaste-activa]]

## Wanneer kies je dit?

### Voor wie

🧭 **Élke vennootschap** die oprichtings-, kapitaalverhogings-,
uitgifte-, of (welomschreven) herstructureringskosten maakt staat voor
de keuze "**direct ten laste** of **activeren en spreiden**".

🧭 In de praktijk wordt vooral geactiveerd:
- bij **opstart** (notariskosten, kosten van inschrijving KBO, eerste
  drukwerk, oprichtingsadvies)
- bij **kapitaalverhoging** door inbreng (notaris + publicatie)
- bij **uitgifte van leningen** (notaris + emissieprospectus +
  bankcommissies — zie aparte uitzondering hieronder)
- bij **welomschreven herstructurering** (fusie, splitsing,
  reorganisatie met expliciete CBN-verantwoording)

### Wanneer wel activeren

- 🔗 **Bedrag is materieel** t.o.v. het resultaat van het jaar —
  anders is administratieve last (afschrijvings-tabel, toelichting,
  uitkeringsbeperking) zwaarder dan de voordelen.
- 🔗 **Het resultaat van het jaar zou anders verlies tonen** dat de
  realiteit niet weerspiegelt (bv. oprichtingsjaar van een jonge
  vennootschap).
- 🔗 **Bestuur wil een dividenduitkering kunnen blokkeren** zolang
  oprichtingskosten lopen — het uitkeringsverbod werkt dan als
  **buffer-mechanisme** (vermijdt te vroege uitkering uit
  papier-vermogen).
- 🧭 **Bij uitgifte van een obligatielening** met looptijd > 5 jaar
  is activeren + spreiden over de looptijd **standaard-praktijk**
  (zie [Uitzondering](#uitzondering-obligatie-uitgiftekosten-spreiding-over-de-looptijd)).

### Wanneer niet activeren

- 🧭 **Bedrag is onbeduidend** — boek direct in resultatenrekening
  (rekening 61-diensten en diverse goederen of 64-andere bedrijfskosten,
  afhankelijk van aard).
- 🔗 **Geen "gunstige en duurzame invloed op de rentabiliteit"** te
  motiveren (vereist voor herstructureringskosten — zie
  [[CBN-2011-24]]).
- 🧭 **Bestuur zoekt maximale uitkeerbaarheid** in de komende jaren —
  activering blokkeert dat (uitkeringsverbod).
- 🧭 **Internationale rapportering of IFRS-conformiteit gewenst** —
  IFRS staat activering van oprichtingskosten **niet toe**; ⚠️ IAS 38
  / IFRS-conversie te verifiëren.

### Hoofdrisico voor de klant

**Uitkeringsverbod miskennen.** De vennootschap met geactiveerde
oprichtingskosten ziet op haar balans **eigen vermogen X**, maar de
**uitkeerbare ruimte** is X **min** het niet-afgeschreven saldo
oprichtingskosten. Een dividend dat de toets niet doorstaat is een
**verboden uitkering** met **terugvorderbaarheid** en
**bestuurdersaansprakelijkheid** als gevolg.

*Bron: [[WVV#art-7-212]] · [[CBN-2021-02]]* ⚖️

### Hoofdvoordeel voor de klant

**Realistische resultaatpresentatie** in het opstartjaar, en **spreiding
van de fiscale aftrek** van de kost over het toekomstig nut dat ze
genereert (matching-beginsel). Tegelijk een **structurele rem op te
vroege dividenduitkering** — een buffer die bestuurders soms
onderschatten als gunst.

## Hoe het werkt

*Conceptuele uitleg per onderdeel. Concrete boekingen + balans-snapshots
staan onder [Rol van de accountant > Boekhouder](#-boekhouder).*

### De vier componenten — MAR-rubriek 20

⚖️ De wet definieert oprichtingskosten als kosten "verbonden met de
oprichting, de verdere ontwikkeling of de herstructurering van de
vennootschap, in het bijzonder de kosten van oprichting of
kapitaalverhoging, de kosten bij uitgifte van leningen, en de
herstructureringskosten." *Bron: [[CBN-2010-15]] · [[KB-WVV#art-3-36]]
e.v.* ⚖️

Vier sub-rubrieken in het MAR (rekeningen-stelsel):

| MAR-rekening | Naam | Wanneer gebruikt |
|---|---|---|
| **200** | Kosten van oprichting en kapitaalverhoging | Notariskosten oprichting, kosten kapitaalverhoging, inschrijving KBO, registratierechten op inbreng (indien van toepassing) |
| **201** | Kosten bij uitgifte van leningen | Notaris + publicatie + bankcommissies + prospectus-kosten bij obligatielening of grote banklening |
| **202** | Overige oprichtingskosten | Andere aanloopkosten met "duurzaam karakter" (bv. eerste website, eerste drukwerk) — restcategorie |
| **204** | Herstructureringskosten | Welomschreven kosten van structurele wijziging met **gunstige en duurzame invloed op de rentabiliteit** (fusie, splitsing, reorganisatie) — strikte voorwaarden CBN 2011/24 |

*Bron MAR: [[MAR#klasse-2]]* ⚖️

🔗 **Sub-rekeningen-conventie** (uit MAR): elke rekening eindigt op
**0** voor de aanschaffingswaarde, op **9** voor de afschrijvingen
(bv. 200 / 2009; 201 / 2019).

### Keuze: kost-in-jaar of activeren

⚖️ **Wettelijke uitgangspositie**: "Oprichtingskosten worden slechts
op het actief geboekt voor zover ze niet ten laste worden genomen
gedurende het boekjaar waarin ze werden besteid." *Bron:
[[KB-WVV#art-3-36]]* ⚖️

🔗 Dus: activeren is **een keuze**, geen verplichting. De default is
direct ten laste; activeren is de uitzondering die je expliciet maakt.

#### Vergelijkingstabel: kost in jaar vs activeren

| Aspect | **Direct in resultaat** | **Activeren + afschrijven** |
|---|---|---|
| **Boeking** | 61/64 → 550 (cash) | 20x → 550 (cash) + jaarlijks 6300 → 20x9 |
| **Resultaat jaar 1** | Volle kost ineens | 1/N van de kost |
| **Resultaat jaar 2-N** | Geen verdere impact | 1/N afschrijving per jaar |
| **Balans** | Geen impact | Activum (afnemend) — kunstmatig EV-bedrag |
| **Uitkeerbaar EV** | Niet beïnvloed | **Geblokkeerd t.b.v. niet-afgeschreven saldo** ([[WVV#art-7-212]]) |
| **Fiscale aftrek** | Vol in jaar 1 | Gespreid over afschrijvingstermijn |
| **Toelichting** | Geen specifieke vereiste | Waarderingsregels + afschrijvingsplan |
| **Onder IFRS toegestaan** | Ja | **Nee** (IAS 38 ⚠️) |

🧭 **Wanneer welk**:

- **Direct in resultaat**: bij **lage bedragen** (vuistregel < 1-2 %
  van resultaat), **stabiele vennootschap** met groot resultaat, of
  bij **IFRS-conforme rapportering**.
- **Activeren**: bij **hoge bedragen**, **opstart- of post-
  herstructureringsjaren**, of bij **leningenuitgifte met lange
  looptijd**.

### Afschrijvingsplan (max 5 jaar — algemene regel)

⚖️ "Voor de oprichtingskosten worden passende afschrijvingen geboekt,
per jaarlijkse tranches van **ten minste twintig percent** van de
werkelijk uitgegeven bedragen." *Bron: [[KB-WVV#art-3-37]] ·
[[CBN-2010-15]]* ⚖️

🔗 Concreet: **maximaal 5 boekjaren**, minstens **20 %/jaar** lineair —
met als ondergrens de werkelijk uitgegeven bedragen.

🔗 Afschrijving begint in het boekjaar van **werkelijke uitgave** (niet
het jaar waarin de kost werd besteed maar nog niet betaald). Eerste
jaar mag **pro rata temporis** worden afgeschreven — ⚠️ exacte CBN-
positie te verifiëren.

🔗 **Snellere afschrijving** mag (bv. 100 % in jaar 1) — de wet geeft
een **minimum**, geen maximum. Versneld afschrijven is fiscaal vaak
voordelig.

#### Voorbeeld

> **NV Beta** maakt bij oprichting € 25.000 notariskosten (rekening
> 200). Activeert + lineair over 5 jaar afschrijven:

| Jaar | Afschrijving | Cumulatief | Restwaarde |
|---:|---:|---:|---:|
| 1 | 5.000 | 5.000 | 20.000 |
| 2 | 5.000 | 10.000 | 15.000 |
| 3 | 5.000 | 15.000 | 10.000 |
| 4 | 5.000 | 20.000 | 5.000 |
| 5 | 5.000 | 25.000 | 0 |

🧭 Gedurende jaren 1-5 is **€ 25.000 → afnemend naar 0** geblokkeerd
voor uitkering via netto-actief-toets.

### Uitzondering: obligatie-uitgiftekosten — spreiding over de looptijd

⚖️ "De afschrijving van de kosten bij uitgifte van leningen mag echter
gespreid worden over de **looptijd** van de leningen." *Bron:
[[KB-WVV#art-3-37]] (tweede zin) · [[CBN-2010-15]]* ⚖️

🔗 **Wat dit betekent**: de algemene 5-jaar-regel wordt **opzij gezet**
voor kosten op rekening **201 (kosten bij uitgifte van leningen)**.
Wanneer een obligatie- of lange-termijnlening **looptijd > 5 jaar**
heeft, mag de spreiding **dezelfde looptijd** volgen — typisch 7, 8
of 10 jaar.

#### Wat er economisch echt gebeurt — uitzondering

🔗 Het **matching-beginsel** vereist dat de financieringskost in
hetzelfde tempo loopt als het **gebruik van de financiering**. Een
obligatielening met looptijd 8 jaar levert 8 jaar lang financiering;
de eenmalige uitgiftekost hoort daar dus 8 jaar lang aan toegeschreven
te worden, niet 5 jaar gepropt en daarna "gratis" financiering.

#### Voorbeeld

> **NV ABC** geeft een obligatielening van € 1.000.000 uit met
> looptijd 8 jaar. Uitgiftekosten: € 12.000 (notaris + publicatie +
> bankcommissie). Op rekening 201.

Twee toegestane afschrijvingsplannen:

| Plan | Termijn | Jaarlijkse afschrijving |
|---|---|---:|
| **A — algemene regel** | 5 jaar | € 2.400 |
| **B — uitzondering, lening-looptijd** | 8 jaar | € 1.500 |

🔗 Plan B sluit aan bij de coupon- en kapitaal-stroom van de obligatie
en geeft de **werkelijke financieringskost per jaar**. Plan A laat
jaren 6-8 zonder uitgifte-last (mooier resultaat in die jaren, maar
beeld vertekenend).

⚖️ **Verplichting in toelichting**: "Wanneer de spreiding over de
looptijd wordt gekozen, moet dit **expliciet vermeld** worden in de
waarderingsregels en de toelichting." *Bron: [[KB-WVV#art-3-37]]
([[CBN-2010-15]])* ⚖️

🔗 **Cross-record-link**: in de [[obligatielening-v7|obligatielening-
fiche]] verwijst de sectie "Uitgiftekosten" terug naar deze uitzondering
— **dit is dezelfde regel uit twee perspectieven** (instrument vs
balanspost). Edge: `is_uitzondering_op` van obligatielening-
uitgiftekosten → algemene 5-jaar-regel oprichtingskosten.

### Uitkeringsverbod tot volledige afschrijving

⚖️ Artikel 7:212 WVV (NV) — en analoog 5:142 WVV (BV) en 6:115 WVV (CV)
— bepaalt voor de **netto-actief-toets** bij elke uitkering:

> "Onder netto-actief moet worden verstaan het totaalbedrag van de
> activa, verminderd met de voorzieningen, de schulden en, **behoudens
> in uitzonderlijke gevallen te vermelden en te motiveren in de
> toelichting bij de jaarrekening, de nog niet afgeschreven bedragen
> van de oprichtings- en uitbreidingskosten en de kosten voor
> onderzoek en ontwikkeling**."

🔗 **Concreet gevolg**: een vennootschap met € 100.000 eigen vermogen
**en** € 25.000 niet-afgeschreven oprichtingskosten heeft een
**uitkeerbaar netto-actief van € 75.000** (vóór toetsing aan gestort
kapitaal en onbeschikbare reserves). Een dividend boven dat bedrag is
**verboden**.

🧭 **Vuistregel voor de adviseur**: zodra je een vennootschap met
geactiveerde oprichtingskosten ziet **uitkering plannen**, herbereken
de toets met de **aftrek**. Veel klanten en zelfs sommige bestuurders
denken in termen van "EV op balans" en vergeten deze correctie.

🔗 **Uitzonderlijke gevallen** waarin de aftrek niet hoeft: te
**motiveren in de toelichting**. CBN heeft hier weinig specifieke
guidance over — de wettekst is bewust strikt, de uitzondering moet
op zichzelf staand verdedigbaar zijn. ⚠️ CBN-precisering te verifiëren.

### Vermelding in toelichting

⚖️ De **waarderingsregels** in de toelichting moeten **specifiek
vermelden**:

1. **Of oprichtingskosten geactiveerd worden** (of in resultaat
   geboekt)
2. **Afschrijvingsmethode + termijn** (lineair / versneld; 5 jaar /
   looptijd lening)
3. **Voor herstructureringskosten**: motivering dat de
   "gunstige en duurzame invloed op de rentabiliteit"-voorwaarde
   vervuld is ([[CBN-2011-24]])
4. **Voor obligatie-uitgiftekosten**: keuze voor lening-looptijd-
   spreiding **expliciet vermelden** ([[KB-WVV#art-3-37]])

*Bron: [[KB-WVV#art-3-36]] (motivering herstructurering in toelichting) ·
[[CBN-2019-04]] (samenvatting waarderingsregels in toelichting)* ⚖️

🔗 Verder vermeldt de **detailstaat oprichtingskosten** in de
toelichting (volledig schema):
- aanschaffingswaarde + mutaties (toevoegingen, overdrachten,
  buitengebruikstellingen)
- gecumuleerde afschrijvingen + mutaties
- netto-boekwaarde per einde boekjaar
- afschrijvingstermijn + methode

⚠️ Bijlage-rubriek-nummer in Bijlage 3 KB WVV te verifiëren.

## Rol van de accountant

*De accountant treedt op vanuit twee perspectieven bij oprichtingskosten:
de vennootschap (advies + boekhouding + toelichting) en — bij grotere
vennootschappen — de auditor/commissaris.*

### 🏢 Voor de vennootschap (bestuur · ondernemer)

#### 🎯 Adviseur

**Wat doe je**:

- 🧭 **Keuze adviseren** kost-in-jaar vs activeren, op basis van:
  bedrag-materialiteit, resultaat-evolutie, uitkeringsplannen, IFRS-
  ambities. Zie [Vergelijkingstabel](#vergelijkingstabel-kost-in-jaar-vs-activeren).
- 🧭 **Afschrijvingstermijn aansturen** — bij uitgiftekosten lening
  bewust kiezen voor lening-looptijd vs 5 jaar.
- 🔗 **Vooraf waarschuwen** voor het uitkeringsverbod-effect bij
  dividendplanning. *"Mevrouw, u heeft € 30.000 dividend voor ogen,
  maar uw oprichtingskosten zijn nog voor € 18.000 niet afgeschreven —
  uitkeerbaar netto-actief is dus eerder € 50.000, niet € 68.000."*
- 🧭 **Herstructureringskosten** strikt beoordelen — niet alles wat
  "reorganisatie" lijkt voldoet aan de CBN-voorwaarden. Bij twijfel:
  ten laste nemen, niet activeren.
- 🔗 Bij **fusie of overname**: oprichtingskosten van de overgenomen
  vennootschap **niet** automatisch meenemen — ⚠️ specifiek CBN-advies
  te raadplegen rond fusie-restwaardes.

#### 📋 Boekhouder

##### Bij oprichting / kapitaalverhoging (T₀ — algemene regel)

**Voorbeeld**: NV Beta — notariskosten oprichting € 25.000, betaling
per overschrijving. Bestuur kiest activeren + lineair over 5 jaar.

*Boeking bij betaling*

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 200 | Kosten van oprichting en kapitaalverhoging | 25.000 | — |
| 550 | Zichtrekening | — | 25.000 |

*Balans-snapshot direct na boeking*

**Actief**

| Code | Naam | Bedrag |
|---:|---|---:|
| 20 | Oprichtingskosten (200) | +25.000 |
| 55 | Liquide middelen | −25.000 |

**Passief**: geen wijziging.

##### Jaarlijkse afschrijving (T₁ tot T₅ — algemene regel)

*Boeking 31/12 (lineair € 5.000/jaar)*

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 6300 | Afschrijvingen op oprichtingskosten | 5.000 | — |
| 2009 | Geboekte afschrijvingen op oprichtingskosten | — | 5.000 |

🔗 Sub-rekening **2009** (eindigend op 9) registreert de
**gecumuleerde afschrijvingen**; de oorspronkelijke kost blijft staan
op 200. De netto-boekwaarde op de balans = 200 − 2009.

##### Bij uitgiftekosten obligatielening (T₀ — uitzondering)

**Voorbeeld**: NV ABC geeft obligatielening 8 jaar uit, uitgiftekosten
€ 12.000. Bestuur kiest spreiding over 8 jaar (looptijd lening).

*Boeking bij betaling*

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 201 | Kosten bij uitgifte van leningen | 12.000 | — |
| 550 | Zichtrekening | — | 12.000 |

*Jaarlijkse afschrijving (T₁ tot T₈, € 1.500/jaar)*

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 6300 | Afschrijvingen op oprichtingskosten | 1.500 | — |
| 2019 | Geboekte afschrijvingen op kosten uitgifte leningen | — | 1.500 |

🔗 **Verplichting toelichting** in jaar 1 (en verder bij wijziging): de
keuze voor 8-jarige spreiding moet expliciet vermeld worden in de
waarderingsregels-samenvatting. Een formulering: *"De kosten bij
uitgifte van leningen (rekening 201) worden conform artikel 3:37 KB
WVV gespreid over de looptijd van de betrokken obligatielening (8
jaar)."*

##### Bij herstructureringskosten (T₀)

🔗 Activering vereist een **expliciete verantwoording in de
toelichting**: de kosten dragen "een gunstige en duurzame invloed op
de rentabiliteit". Het bestuursorgaan **verklaart** dit in een
**toelichtings-paragraaf** bij de waarderingsregels.

*Bron: [[KB-WVV#art-3-36]] (tweede zin) · [[CBN-2011-24]]* ⚖️

##### Uitvoerings-valkuilen voor de boekhouder

- ⚖️ **Geen afschrijvingsplan in inventarisboek** → wettelijke
  verplichting waarderingsregels-vastlegging niet nageleefd.
  *[[CBN-2019-04]]* ⚖️
- ⚖️ **Afschrijving < 20 %/jaar** (zonder uitzonderings-grondslag) →
  inbreuk op [[KB-WVV#art-3-37]]. De wet stelt **minstens** 20 %.
- ⚖️ **Geen vermelding in toelichting van obligatie-uitgiftekosten-
  spreidingskeuze** wanneer de 5-jaar-regel wordt verlaten → niet-
  conform [[KB-WVV#art-3-37]].
- 🔗 **Activering van herstructureringskosten** zonder de "duurzame
  rentabiliteits-invloed"-motivering in toelichting → niet-conform
  [[CBN-2011-24]].
- 🧭 **Vergeten te herklasseren** wanneer iemand oprichtingskosten
  *zou* willen verkopen of in inbreng geven — ze zijn boekhoudkundig
  een actief maar economisch niet overdraagbaar; de overname-counterparty
  zal ze afwaarderen.
- 🔗 **Sub-rekening 2009/2019 niet gebruikt** (alles direct in 200
  netto geboekt) → conflict met MAR-conventie en met detailstaat-
  vereiste in toelichting.

#### 💰 Fiscaal

🔗 **Aftrekbaarheid afschrijving oprichtingskosten** — gewone
beroepskost van het boekjaar waarin afgeschreven wordt. *Bron:
[[WIB92#art-49]]* ⚖️

🔗 Wanneer de boekhoudkundige afschrijving **versneld** gebeurt (bv.
volledig in jaar 1), volgt de fiscale aftrek mee — onder voorbehoud
van de **minimumdrempel** van 20 %/jaar (boekhoudkundig) die in
dezelfde periode (fiscaal) wordt aanvaard. ⚠️ specifiek
fiscaal-administratieve commentaar te verifiëren.

🔗 Geen **specifiek fiscaal regime** voor oprichtingskosten — wel
indirect effect op:
- **Notionele intrestaftrek** (NIA — voor zover nog van toepassing):
  niet-afgeschreven oprichtingskosten zitten in het **gecorrigeerd
  eigen vermogen** ⚠️ te verifiëren.
- **DBI-aftrek**-context: oprichtingskosten beïnvloeden EV-verhoudingen
  in beperkte mate.

### 🔍 Voor de auditor / commissaris (extern perspectief)

#### Controle-aandachtspunten

- ⚖️ **Activering-voorwaarden vervuld** — vooral voor
  herstructureringskosten: motivering in toelichting aanwezig en
  inhoudelijk redelijk. *[[CBN-2011-24]]* ⚖️
- ⚖️ **Afschrijvingsplan** consistent met waarderingsregels, en
  termijn binnen wettelijke grenzen.
- ⚖️ **Spreidingskeuze obligatie-uitgiftekosten** vermeld in
  toelichting wanneer afgeweken wordt van 5-jaar-regel.
- ⚖️ **Detailstaat oprichtingskosten** in toelichting volledig
  (aanschaffingswaarde, mutaties, gecumuleerde afschrijvingen, netto).
- ⚖️ **Netto-actief-toets** bij uitkeringen correct toegepast met
  aftrek niet-afgeschreven oprichtingskosten. *Bron:
  [[WVV#art-7-212]]* ⚖️
- 🔗 **Eventuele uitzonderlijke niet-aftrek** in toelichting
  gemotiveerd op verdedigbare grond.
- 🧭 **Window dressing-signaal**: activering van twijfelachtige
  kosten net vóór een verlies-jaar of net vóór dividend-toets
  is een **fraude-risico-indicator**.

## Veelvoorkomende verwarringen

- **Oprichtingskosten ≠ inbreng of kapitaal.** Oprichtingskosten zijn
  **kosten** (uitgaven aan derden — notaris, drukker, bank); inbreng
  is **kapitaal** dat de aandeelhouder vol stort (rekening 100).
  Ze worden vaak in dezelfde zin genoemd ("kosten van oprichting") maar
  zijn boekhoudkundig en juridisch totaal verschillend.
- **Oprichtingskosten ≠ immateriële vaste activa.** Beide staan op
  klasse 2 maar in **verschillende rubrieken** (20 vs 21). Immateriële
  vaste activa (concessies, licenties, goodwill, O&O) hebben een
  **verkoopwaarde** of economische gebruiksduur; oprichtingskosten
  zijn een **administratieve constructie** zonder economische waarde
  los van de vennootschap.
- **Onderzoek en ontwikkeling ≠ oprichtingskosten.** O&O staat op
  rekening **210** (immateriële vaste activa) en heeft een eigen
  regime (max 5 of 10 jaar afschrijving — [[CBN-2016-16]]).
  O&O is **economisch overdraagbaar**; oprichtingskosten niet.
  Wel: beide vallen onder dezelfde **netto-actief-toets-aftrek**
  ([[WVV#art-7-212]]).
- **Uitbreidingskosten** is geen aparte MAR-rubriek maar wordt
  in artikel 7:212 WVV vermeld naast oprichtingskosten — historisch
  begrip dat in de praktijk samenvalt met "oprichtingskosten +
  kapitaalverhoging".
- **5-jaar = wettelijk maximum?** ❌ Nee, **5-jaar is een minimum
  afschrijvingstempo** (20 %/jaar). Volledig in jaar 1 afschrijven
  mag. De **5-jaar-uitzondering** voor obligatie-uitgiftekosten
  betekent: spreiden mag *langer* dan 5 jaar.
- **"Vrijstelling" van uitkeringsverbod bij volledige afschrijving?**
  Strikt gezien: zodra de afschrijving op 0 staat, valt de balanspost
  weg en is er niets meer om af te trekken. De "vrijstelling" is dus
  automatisch — niet een aparte beslissing.
- **Activeren = winst boeken?** ❌ Nee, activeren is alleen het
  **verschuiven** van de kost van de resultatenrekening naar de balans.
  Het creëert geen winst, alleen een **andere timing** van het
  resultaat-effect.

## Familie & alternatieven

### Binnen de familie balansposten

Oprichtingskosten is **één balanspost** binnen het
[[jaarrekening-v1|jaarrekening-kader]]. Verwante balansposten:

- [[immateriele-vaste-activa]] (rubriek 21) — andere klasse 2-posten
  met eigen regime
- [[onderzoek-en-ontwikkeling]] (rekening 210) — vergelijkbare
  netto-actief-toets-aftrek; eigen afschrijvings-regels
- [[goodwill]] (rekening 212) — bij overname; eigen waarderingsregels
- [[materiele-vaste-activa]] (klasse 2 — rubriek 22-27) — normale
  afschrijvings-route

### Alternatieven (zelfde economische functie)

Voor **omgaan met grote eenmalige opstart-of-uitgifte-kosten** zijn er
geen echte alternatieven binnen BGAAP:

- **Direct ten laste in resultaat** (default) — eenvoudiger, geen
  uitkeringsbeperking, maar resultaat van jaar 1 vertekend
- **Activeren + afschrijven** (deze fiche) — matching-beginsel-conform
  maar uitkeringsbeperking
- **IFRS-route**: activering oprichtingskosten **niet toegestaan**
  (IAS 38 ⚠️) — als de groep IFRS-conform wil rapporteren is direct in
  resultaat de enige optie.

## Wat dit record dekt

*Een check-lijst voor de stagiair. Competenties chronologisch (volgorde
van uitvoeren bij elke aanloopuitgave); termen alfabetisch.*

### Behandelde competenties (chronologisch)

1. **Kost-natuur identificeren** — valt deze uitgave onder
   oprichtingskosten (rekening 20x) of onder iets anders (61, 64, 21
   …)? Zie [Vier componenten](#de-vier-componenten--mar-rubriek-20).
2. **Keuze adviseren** kost-in-jaar vs activeren op basis van
   materialiteit, resultaat, uitkeringsplannen, IFRS-ambities. Zie
   [Wanneer kies je dit](#wanneer-kies-je-dit).
3. **Sub-rekening kiezen** (200 / 201 / 202 / 204) — zie
   [MAR-tabel](#de-vier-componenten--mar-rubriek-20).
4. **Afschrijvingstermijn vastleggen** — algemeen max 5 jaar (min
   20 %/jaar); uitzondering uitgiftekosten lening = lening-looptijd.
   Zie [Afschrijvingsplan](#afschrijvingsplan-max-5-jaar--algemene-regel)
   en [Uitzondering](#uitzondering-obligatie-uitgiftekosten-spreiding-over-de-looptijd).
5. **Boeking bij betaling** uitvoeren (20x debet, 550 credit) — zie
   [Boekhouder](#-boekhouder).
6. **Waarderingsregel** formuleren en in inventarisboek + toelichting
   opnemen — zie [Vermelding in toelichting](#vermelding-in-toelichting).
7. **Voor herstructureringskosten**: motivering "duurzame
   rentabiliteits-invloed" in toelichting opstellen.
8. **Jaarlijkse afschrijvingsboeking** uitvoeren (6300 debet, 20x9
   credit).
9. **Detailstaat oprichtingskosten** in toelichting bijhouden (mutaties,
   gecumuleerde afschrijvingen, netto-boekwaarde).
10. **Netto-actief-toets** correct toepassen bij elke uitkering:
    aftrek niet-afgeschreven oprichtingskosten + uitbreidingskosten + O&O.
    Zie [Uitkeringsverbod](#uitkeringsverbod-tot-volledige-afschrijving).
11. **Klant adviseren** over uitkeringscapaciteit met expliciete vermelding
    van de aftrek.
12. **Auditor-controle**: activering-voorwaarden, plan, toelichting,
    netto-actief-toets. Zie [auditor-rol](#-voor-de-auditor--commissaris-extern-perspectief).

### Behandelde termen (alfabetisch)

afschrijvingsplan · activeren · detailstaat oprichtingskosten ·
gecorrigeerd eigen vermogen · gecumuleerde afschrijvingen ·
herstructureringskosten · inventarisboek · kapitaalverhoging-kosten ·
kost-in-jaar · matching-beginsel · MAR-rubriek 20 · netto-actief-toets ·
niet-afgeschreven saldo · notariskosten oprichting · obligatie-
uitgiftekosten · oprichtingskosten · uitbreidingskosten ·
uitgiftekosten leningen · uitkeerbaar eigen vermogen · uitkeringsverbod ·
waarderingsregels · 5-jaar-regel

### Behandelde formules

- **Jaarlijkse afschrijving (algemeen)** = *aanschaffingswaarde × 20 %*
  (lineair, min 20 %/jaar)
- **Jaarlijkse afschrijving (uitgiftekosten lening, optie 2)** =
  *aanschaffingswaarde / looptijd van de lening (in jaren)*
- **Uitkeerbaar netto-actief** = *Totaal Activa − Voorzieningen −
  Schulden − niet-afgeschreven oprichtingskosten − niet-afgeschreven
  uitbreidingskosten − niet-afgeschreven O&O*
- **Beschikbare uitkeringsruimte** = *Uitkeerbaar netto-actief −
  gestort/opgevraagd kapitaal − onbeschikbare reserves*

### Behandelde regimes (via edges)

- [Uitkeringsverbod via netto-actief-toets](#uitkeringsverbod-tot-volledige-afschrijving)
  ([[WVV#art-7-212]]) ⚖️
- [Uitzondering obligatie-uitgiftekosten](#uitzondering-obligatie-uitgiftekosten-spreiding-over-de-looptijd)
  ([[KB-WVV#art-3-37]]) ⚖️
- [Aftrekbaarheid in vennootschapsbelasting](#-fiscaal) ([[WIB92#art-49]]) ⚖️
- Toelichtings-vereisten ([[KB-WVV#art-3-36]] · [[CBN-2019-04]] ·
  [[CBN-2011-24]]) ⚖️

## Bronnen en verwijzingen

**Bronnen (grounded)** ⚖️:

- [[KB-WVV#art-3-36]] — voorwaarden activering oprichtingskosten +
  motivering herstructureringskosten in toelichting
- [[KB-WVV#art-3-37]] — afschrijving min 20 %/jaar + uitzondering
  uitgiftekosten leningen (lening-looptijd)
- [[KB-WVV#art-3-23]] — definitie afschrijvingen / waardeverminderingen
- [[WVV#art-7-212]] — netto-actief-toets NV met aftrek niet-
  afgeschreven oprichtings/uitbreidings/O&O-kosten
- [[WVV#art-5-142]] — analoog voor BV ⚠️ exact artikel te bevestigen
- [[WVV#art-6-115]] — analoog voor CV ⚠️
- [[CBN-2010-15]] — afschrijvingsmethoden, sectie oprichtingskosten
- [[CBN-2011-24]] — herstructureringskosten, voorwaarden activering
- [[CBN-2019-04]] — vastlegging waarderingsregels door bestuursorgaan
- [[CBN-2021-02]] — winstverdeling NV (netto-actief-toets,
  sancties bij verboden uitkering)
- [[MAR#klasse-2]] — rekeningenstelsel rubriek 20-204
- [[WIB92#art-49]] — aftrekbaarheid beroepskosten

**Te verifiëren** ⚠️:

- IFRS / IAS 38-positie over oprichtingskosten (niet-activeerbaar)
- Exact CBN-advies bij fusie/overname over oprichtingskosten van
  overgenomen vennootschap
- Pro-rata-temporis-regel in jaar 1 van afschrijving
- "Uitzonderlijke gevallen" voor niet-aftrek in netto-actief-toets —
  bestaande CBN-precedenten
- Notionele intrestaftrek-context (nog van toepassing? gecorrigeerd
  eigen vermogen-berekening)
- Bijlage-rubriek-nummer detailstaat oprichtingskosten in Bijlage 3 KB
  WVV
- Fiscaal-administratieve commentaar over versnelde afschrijving
  oprichtingskosten (max in jaar 1)
- BV-versie [[WVV#art-5-142]] en CV-versie [[WVV#art-6-115]] van het
  uitkeringsverbod precies te citeren

**Cross-record edges**:

- `is_balanspost_van` → [[jaarrekening-v1]] (kader) — deze fiche is een
  concrete invulling van de jaarrekening-balanspost-rubriek
- `is_uitzondering_op` → ❶ obligatie-uitgiftekosten (sub-rekening 201)
  zijn een uitzondering op de algemene 5-jaar-regel van rekening 200.
  ❷ Symmetrisch: in [[obligatielening-v7]] zit deze uitzondering al
  beschreven; deze fiche linkt naar het oprichtingskosten-perspectief.
- `triggert_regime` → [[WVV#art-7-212]] netto-actief-toets-aftrek —
  uitkeringsverbod tot volledige afschrijving
- `gerelateerd` → [[obligatielening-v7]] (uitgiftekosten leningen),
  [[kapitaalverhoging]] (rekening 200),
  [[fusie-splitsing]] (herstructureringskosten — rekening 204),
  [[onderzoek-en-ontwikkeling]] (analoog uitkerings-aftrek-regime,
  ander activum)
- `verward_met` → [[immateriele-vaste-activa]] (klasse 2 maar ander
  regime), [[goodwill]] (rekening 212), [[inbreng-kapitaal]] (rekening
  100), [[onderzoek-en-ontwikkeling]] (rekening 210)
- `valt_onder_kader` → [[jaarrekening-v1]] (artefact-context)
- `gerelateerd_aan_uitkering` → [[uitkering-aan-aandeelhouders-v1]]
  (vermindert uitkeerbaar netto-actief)

---

## Iteratie-log

**v1 (huidige)** — eerste POC mockup van een **`balanspost`-kind**:
een concept dat juridisch één plaats op de balans inneemt (MAR-rubriek
20) maar conceptueel **vier sub-componenten** + **één belangrijke
uitzondering** + **één uitkeringsverbod-gevolg** bundelt.

### 1. Werkt het patroon?

**Wat werkt**:
- **Vergelijkingstabel kost-in-jaar vs activeren** als
  beslissings-hulpmiddel werkt sterk — het is precies wat een stagiair
  nodig heeft om de klant te adviseren.
- **Sub-rekening-tabel (200/201/202/204)** met "wanneer gebruikt"
  voorkomt verwarring.
- **Uitzondering met eigen sectie + cross-link naar
  [[obligatielening-v7]]** maakt de regelgeving in twee richtingen
  vindbaar (vanuit instrument én vanuit balanspost).
- **Uitkeringsverbod met expliciet voorbeeld** ("€ 100k EV − € 25k
  niet-afgeschreven = € 75k uitkeerbaar") landt directer dan de
  abstracte wettekst.
- **Boekhouder-sectie met variant uitgiftekosten** geeft de stagiair
  twee complete uitvoerings-scenario's op één plaats.

**Wat schuurt**:
- **Lengte ~750 regels** — vergelijkbaar met obligatielening-v7. Lijkt
  veel voor "één balanspost", maar de balanspost draagt vier
  componenten + uitzondering + uitkeringsregime + waarderingsregels +
  fiscale impact. Het concept is dichter dan het lijkt.
- **Herhaling met [[jaarrekening-v1|jaarrekening-kader]]** rond
  netto-actief-toets — moet één van beide de toets primair definiëren,
  en de andere verwijzen? Voorlopig staat de **regel** primair hier;
  in jaarrekening-v1 is alleen het **gebruik** (resultaatverwerking-
  stap) beschreven met link naar hier. Acceptabel.
- **Herstructureringskosten** krijgen weinig diepgang — verdienen ze
  eigen record (`kind: balanspost` of `kind: operatie`)? Voorlopig
  hier als sub-rubriek met cross-link naar CBN 2011/24.
- **MAR sub-rekening 2009/2019** (gecumuleerde afschrijvingen) krijgen
  uitleg maar het concept "tegen-rekening" wordt nergens diep
  uitgewerkt — verwijst impliciet naar [[mar-rekeningenstelsel]]
  voorvereiste.

### 2. `balanspost` als kind, of past `begripscluster` ook?

#### Argumenten voor **`balanspost` als nieuw kind**

- **Specifieke didactische logica**: een balanspost-fiche heeft een
  vast skelet — MAR-rekening identificatie + componenten + boeking +
  afschrijving + waardering + toelichting + interactie netto-actief-
  toets. Dat skelet is **anders dan een instrument** (geen "wanneer
  koop je dit") en anders dan een **kader** (geen gemeenschappelijke
  discipline over leden).
- **Examenfit**: het examen test letterlijk balansposten ("welke
  rubriek, welke afschrijving, welke vermelding in toelichting") — een
  kind-naam die deze categorie expliciet erkent maakt examenpatroon-
  matching gemakkelijker.
- **Catalogus-bouw**: ITAA-LEX + Cijferzakboekje + jaarrekening hebben
  een **identificeerbare set balansposten** (rubriek 20, 21, 22, 24, 28,
  29, 30, 40, 41, 50, 55, 10, 11, 12, 13, 16, 17, 42, 43, 44, 45-49…).
  Een eigen kind maakt **systematische dekking** mogelijk en zichtbaar
  via render-laag.
- **Render-kansen**: balanspost-fiches kunnen samen een **interactieve
  balans-rondleiding** voeden (klik op rubriek → fiche).

#### Argumenten voor **`begripscluster` (bestaande kind) ook OK**

- **`begripscluster` is bewust open**: ADR-025 beschrijft het als
  "verzameling samenhangende begrippen zonder operationeel karakter" —
  past op zich.
- **Risico van kind-inflatie**: elke type rapporteringsrubriek apart?
  (resultatenrekeningpost, toelichtingsrubriek, sociale-balans-veld
  …). Dat is een hellend vlak.
- **`balanspost` is renderable als facet/tag**, niet noodzakelijk als
  apart kind — `kind: begripscluster` + `tag: balanspost` zou dezelfde
  filter-mogelijkheid geven zonder taxonomie-uitbreiding.

#### Aanbeveling

🧭 **Voorzichtig voor `balanspost` als kind kiezen** — maar **alleen
indien** we systematisch werk gaan maken van balanspost-dekking (PO 1.1
omvat juist die taak). Anders: `begripscluster` met facet/tag
`balanspost`.

De **didactische winst** van een eigen kind zit vooral in:
- het **vaste skelet** dat de extractor sneller correct vult
- de **renderbaarheid** als balans-rondleiding
- de **examenpatroon-fit**

Als dit POC-paar (jaarrekening + oprichtingskosten) opschaalt naar
10-15 balanspost-fiches in Fase 2, is de kind-promotie verantwoord.
Bij minder: hou het bij `begripscluster` met facet.

**Resultatenrekeningpost** en **toelichtingsrubriek** zouden bij
balanspost-promotie analoge kinds verdienen — dat is een principiële
keuze die voor Fase 2 aan de design-tafel moet.

### 3. Aanbevelingen voor de skeleton-voorstel-prompt of EXTRACT v5

- **Skelet-template "balanspost"** toevoegen in EXTRACT v5-prompt:
  ```
  - Definitie + MAR-rubriek identificatie
  - Componenten / sub-rekeningen
  - Keuze: ten laste / activeren (vergelijkingstabel)
  - Afschrijvingsplan (incl. uitzonderingen)
  - Vermelding in waarderingsregels + toelichting
  - Interactie met netto-actief-toets / uitkering
  - Fiscale aftrekbaarheid
  ```
  Een agent die "oprichtingskosten" of "obligaties als belegging" als
  balanspost herkent, krijgt dit skelet als initial draft.
- **Edge `is_uitzondering_op` met dubbel-doorlinkage**: prompt moet
  expliciet zeggen dat een uitzondering in **beide** records vermeld
  hoort te zijn (vanuit instrument-perspectief én vanuit balanspost-
  perspectief). Dit is een **redundancy by design**, geen DRY-schending.
- **`heeft_uitzondering`-edge als symmetrische tegenhanger** van
  `is_uitzondering_op` overwegen — zou render-laag automatische
  cross-links opleveren.
- **Vergelijkingstabel-weergave** met emoji-indicatoren voor
  voor/nadeel kolom blijkt sterk — toevoegen aan element-weergavetypes
  als variant van `vergelijkingstabel`.
- **Sub-rekening-tabel** als gestandaardiseerd element bij elke
  balanspost-fiche — uniforme presentatie geeft renderbaarheid voor
  een filtering "alle MAR-200-uitgaven".
- **Cross-check op uitkeringsverbod-relevantie**: VERIFY v3 zou kunnen
  vlaggen wanneer een fiche over een netto-actief-toets-aftrekbare
  post (oprichtingskosten, O&O, uitbreidingskosten) geen verwijzing
  bevat naar [[WVV#art-7-212]]. Eenvoudige string-match op MAR-rubriek
  20 of rekening 210/200/201/202/204.

### 4. Open punten

- **Onderzoek en ontwikkeling** (rekening 210, immateriële vaste
  activa) is **vergelijkbaar** in regime — eigen fiche of variant
  hier? Mijn voorkeur: **eigen fiche**, met cross-edge.
- **Uitbreidingskosten** als concept: niet expliciet in MAR maar wel
  in artikel 7:212 WVV — verdient korte vermelding in fiche of cross-
  link?
- **IFRS-positie**: alleen vermeld als ⚠️ — verdient eigen sub-record
  of cross-link naar [[IFRS-vs-BGAAP]] indien dat bestaat.
- **Sub-rekening-conventie (200/2009)** — wordt impliciet uitgelegd
  maar verdient mogelijk eigen voorvereiste-fiche
  [[mar-rekeningenstelsel-conventies]].
- **Fusie-context** voor oprichtingskosten van overgenomen
  vennootschap: hier kort vermeld als TBD, verdient CBN-onderzoek
  vóór finalisering.
- **Aansprakelijkheids-implicatie** voor accountant die dividend
  adviseert zonder oprichtings-aftrek mee te tellen — zou in een
  beroepsethiek-fiche kunnen, of als korte vermelding hier.
