---
title: "Financiële leasing — v1 (instrument-mockup met sterke vergelijking)"
tags:
  - experiment
  - mockup
status: experimental
mockup: true
---

> **Mockup om het schema 1.7-model te testen op een instrument met
> sterke vergelijk-as** (vs operationele leasing). v5-structuur.
>
> **Confidence-tekens**: ⚖️ uit bron · 🔗 afgeleid · 🧭 vuistregel · ⚠️ te verifiëren

# Financiële leasing

Een **financiële leasing** is een leasingsovereenkomst waarbij de
**economische eigendom** van het actief overgaat naar de leasingnemer
ondanks dat de juridische eigendom bij de leasingmaatschappij blijft.
Boekhoudkundig wordt het actief geactiveerd bij de leasingnemer en
afgeschreven; de leasebetalingen worden gesplitst in **kapitaalaflossing**
en **rentecomponent**.

🔗 Het sleutel-onderscheid met operationele leasing: bij financiële
leasing **draagt de leasingnemer alle risico's en geniet hij alle
voordelen** van het actief — alsof hij het gekocht had — en wordt het
contract boekhoudkundig ook zo behandeld.

*Bron: ⚠️ [[KB-WVV]] (financiële leasing definitie) · [[CBN]]
(praktische verwerking) — exacte artikelen te verifiëren.*

## Wat er economisch echt gebeurt

🔗 Juridisch huurt de leasingnemer een actief; economisch koopt hij het op
afbetaling. De leasingmaatschappij financiert de aankoop en blijft eigenaar
als zekerheid — kan terugeisen bij wanbetaling. Maar het *gebruik*, de
*waarde-evolutie* (waarde-vermindering door slijtage, technologische
veroudering), en het *risico* (schade, verlies) liggen volledig bij de
leasingnemer.

🔗 Daarom volgt de **boekhoudkundige weergave de economische realiteit**
(substance over form): het actief verschijnt bij de leasingnemer als
vaste activum + schuld. Anders zou de balans van een leasingnemer geen
juist beeld geven van zijn werkelijke activa en verplichtingen.

🔗 De **kost-spreiding** verschilt fundamenteel van operationele leasing:
- Operationele lease = huur = volledig in resultaat als kost in jaar van
  betaling (recht-lineaire spreiding van vooruitbetalingen).
- Financiële lease = aankoop op afbetaling = activeren + afschrijven
  (over levensduur) + financiële kost (rente op de schuld) — twee aparte
  kost-stromen.

## Wanneer kies je dit?

### Voor wie

🧭 Ondernemingen die **een investeringsgoed nodig hebben zonder cash uit
te geven aan voorhand**, en die het actief **economisch tot zich willen
trekken** (afschrijven, mogelijk later kopen tegen restwaarde).

### Wanneer wel inzetten

- 🔗 **Cash-conservatie** — geen grote eenmalige uitgave; gespreide
  betalingen over de looptijd.
- 🔗 **Investeringsaftrek** ⚠️ — financiële leasing kwalificeert vaak voor
  investeringsaftrek (te verifiëren) omdat economisch eigenaarschap bij
  de leasingnemer ligt. Bij operationele leasing in principe niet.
- 🧭 **Restwaarde-overname intentie** — als je op vervaldag het actief
  effectief wil overnemen, financiële leasing past beter dan operationele.
- 🔗 **Inflatiebescherming** — vaste leasebetalingen tegen inflatie.

### Wanneer niet

- 🧭 **Korte gebruiksduur** — als je het actief enkel 2-3 jaar gebruikt
  en niet wil overnemen, operationele leasing of huur is goedkoper.
- 🧭 **Technologisch snel verouderend** materieel (IT) — operationele
  lease verplaatst veroudering-risico naar leasingmaatschappij.
- 🔗 **Voorkeur voor off-balance financiering** ⚠️ — onder oude BGAAP
  gaf operationele leasing minder balanscijfers, maar dit is onder IFRS-16
  niet meer waar. Te verifiëren voor BE-BGAAP huidige praktijk.

### Hoofdrisico voor de klant

🔗 **Onderbenutting van het actief** — vaste maandelijkse last loopt
ongeacht of het actief productief is. Bij economische tegenslag → kostpost
die niet wegvalt.

🔗 **Restwaarde-misrekening** — als de overeengekomen restwaarde te hoog
ligt vergeleken met de werkelijke marktwaarde op vervaldag, blijf je vast
zitten aan een onaantrekkelijke koopoptie.

### Hoofdvoordeel voor de klant

🔗 **Economische eigendom zonder volledige aankoop-cashout** + mogelijke
**investeringsaftrek** + **afschrijfbaarheid** voor fiscale optimalisatie.

## Hoe het werkt

*Boekhoudkundige uitwerking onder [🏢 Vennootschap-leasingnemer](#-vennootschap-leasingnemer)
en [🏢 Leasingmaatschappij](#-leasingmaatschappij).*

### Kwalificatie als financiële leasing

⚖️ Een leaseovereenkomst kwalificeert als **financieel** (in plaats van
operationeel) wanneer ze ofwel **één van de volgende criteria** vervult,
ofwel de "substance over form"-test slaagt:

⚠️ *Exact criteria-overzicht te verifiëren in KB WVV — typisch:*
1. **Risico's en voordelen** van het actief liggen substantieel bij de
   leasingnemer.
2. **Aankoopoptie** tegen een prijs die significant lager is dan de
   verwachte marktwaarde op vervaldag (typisch < 15 % van aankoopwaarde).
3. **Contractduur** beslaat het grootste deel van de economische
   levensduur van het actief (typisch > 75 %).
4. **Contante waarde van de leasebetalingen** > 90 % van de
   marktwaarde van het actief bij aanvang.
5. **Specifiek actief** dat zonder grote aanpassing niet door anderen
   bruikbaar is.

🔗 Eén criterium vervuld kan voldoende zijn voor kwalificatie als
financiële leasing — maar het is de **economische substantie** die
uiteindelijk telt.

### Splitsing van de leasebetaling

⚖️ Elke leasebetaling wordt gesplitst in:
1. **Kapitaalaflossing** — vermindering van de leasingschuld.
2. **Rentecomponent** — financiële kost op het uitstaand saldo.

🔗 De verhouding tussen beide verschuift over de looptijd: in beginjaren
overweegt de rentecomponent (groot uitstaand saldo); op het einde
domineert de kapitaalaflossing.

#### Formule

De berekening verloopt typisch via een **actuariële tabel** waarin elke
maandelijkse of jaarlijkse betaling wordt opgesplitst op basis van de
**impliciete leaserente** (interne rentevoet die maakt dat de contante
waarde van alle betalingen + restwaarde-optie gelijk is aan de marktwaarde
bij aanvang).

⚠️ Concrete formule + voorbeeld te verifiëren.

> Boekhoudkundige uitwerking: zie
> [🏢 Vennootschap-leasingnemer → Boekingen jaarlijks](#boekingen--jaarlijks).

### Afschrijving van het geactiveerde actief

⚖️ Het geactiveerde actief wordt afgeschreven volgens de **gewone regels
voor het type actief** (niet over de leaseduur indien deze korter is dan
de levensduur, tenzij de leasingnemer het actief op vervaldag niet
overneemt).

⚠️ Detail-regels te verifiëren.

### Restwaarde en koopoptie

⚖️ Op vervaldag heeft de leasingnemer typisch een **koopoptie** tegen
een **vooraf vastgelegde restwaarde**.

🔗 Drie scenario's:
1. **Optie lichten** — actief overnemen tegen restwaarde; de schuld is
   afgelost, het actief blijft op de balans.
2. **Optie niet lichten** — actief teruggeven aan leasingmaatschappij;
   uitboeken van actief + schuld.
3. **Vervroegde aankoop** — vaak met premie, contractueel geregeld.

### Speelruimte

- 🔗 **Looptijd** vs economische levensduur — bepalen kwalificatie en
  afschrijfduur.
- 🔗 **Restwaarde** — onderhandeling tussen leasingnemer en
  leasingmaatschappij; hogere restwaarde → lagere maandelijkse last, maar
  groter risico op overwaardering.
- 🔗 **Vooruitbetaling** — eerste betaling is vaak hoger om de impliciete
  rente te verlagen.

### Valkuilen

- 📋 *Boekhouder* — ⚠️ **financiële vs operationele leasing verkeerd
  kwalificeren** → activa- en schuld-positie verkeerd; resultaat over
  hele looptijd vertekend.
- 📋 *Boekhouder* — 🔗 **leasebetaling niet correct splitsen** in
  kapitaal vs rente → schuld evolueert verkeerd.
- 🎯 *Adviseur* — 🧭 **restwaarde te hoog onderhandelen** → klant zit
  vast op vervaldag aan onaantrekkelijke optie.
- 📋 *Boekhouder* — ⚠️ **investeringsaftrek niet aanvragen** bij
  kwalificerende financiële lease — voordeel verlies.

---

## Perspectieven per actor

### 🏢 Vennootschap-leasingnemer

**Rekeningen-overzicht**: ⚠️ **25** Vaste activa in leasing (subrubriek
per soort actief) · **172** Schulden uit financieringshuur (langlopend) ·
**42** Schulden uit financieringshuur (korter dan 1 jaar) · **6500**
Rentekosten leasing · **6302** Afschrijvingen geactiveerde leasingactiva.

> ⚠️ MAR-rekeningen voor leasing te verifiëren — boven schema is plausibel
> maar exact MAR-nummers moeten geverifieerd.

#### Boekingen — bij aanvang

⚠️ *Onder voorbehoud; te verifiëren.*

> **Voorbeeld**: NV ABC leaset een machine met marktwaarde € 100.000.
> Looptijd 5 jaar, jaarlijkse leasebetaling € 23.000 (totaal € 115.000),
> impliciete leaserente ≈ 5 %, restwaarde € 5.000 (koopoptie).

**Bij aanvang van het leasecontract**:

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 25 | Vaste activa in leasing — machine | 100.000 | — |
| 172 | Schuld uit financieringshuur (>1j) | — | 100.000 |

⚠️ ⚠️ Splitsing schuld langlopend (172) vs kort lopend (42) op
balansdatum — te verifiëren wanneer en hoe.

#### Boekingen — jaarlijks

⚠️ *Voorbeeld onder voorbehoud — split kapitaal/rente vereenvoudigd.*

**Jaar 1 — leasebetaling € 23.000 (waarvan ~€ 5.000 rente, ~€ 18.000 kapitaal)**:

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 6500 | Rentekosten leasing | 5.000 | — |
| 172 | Schuld financieringshuur | 18.000 | — |
| 550 | Zichtrekening | — | 23.000 |

**Jaarlijkse afschrijving (lineair over 5 jaar)**:

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 6302 | Afschrijving geleased actief | 20.000 | — |
| 250x | Geleased actief — afschrijving | — | 20.000 |

#### Boeking — op vervaldag (koopoptie gelicht)

⚠️ Te verifiëren — typisch:
- restwaarde betalen
- actief verschuift van rekening 25 (geleasede activa) naar 23 (eigen
  vaste activa)
- afschrijving loopt verder volgens normale regels

#### Boeking — op vervaldag (koopoptie niet gelicht)

⚠️ Actief en restschuld uitboeken; eventuele meer- of minderwaarde op
overdracht.

#### Fiscaal

- ⚠️ **Afschrijvingen** zijn aftrekbare beroepskosten — looptijd volgens
  fiscale regels (kortste tussen leaseduur en levensduur).
- ⚠️ **Rentecomponent** is aftrekbaar als financieringskost ([[WIB92#art-49]]).
- ⚠️ **Investeringsaftrek** mogelijk bij kwalificatie — voorwaarden en
  tarief in [Cijferzakboekje §X] / [[WIB92]].
- ⚠️ **BTW** — pro rata aftrekbaar op leasecomponent, regels te verifiëren.

Edge → [[investeringsaftrek]] ⚠️ · [[aftrekbaarheid-financieringskosten]]

#### Toelichting jaarrekening

⚠️ Te verifiëren — typisch:
- aard van geleasede activa
- looptijden + restwaardes
- splitsing schuld kort/lang termijn

#### Formaliteiten

⚠️ Geen bijzondere formaliteiten buiten contract — te verifiëren of
publicatieplicht of statutaire vermelding nodig is.

### 🏢 Leasingmaatschappij

**Bij aanvang**: boekt **financiële vordering** (i.p.v. actief), gespreid
over looptijd; ontvangt leasebetalingen die ze splitst in rente-opbrengst
+ kapitaalterugbetaling.

⚠️ Verdere uitwerking buiten scope van dit record — leasingmaatschappij is
typisch geen eindklant maar tegenpartij.

### 🏢💰 Vergelijking met operationele leasing — andere zijde

Operationele leasing heeft **geen activering** bij de huurder. De
maandelijkse huur is volledig kostpost in jaar van betaling, geen schuld
op balans.

⚠️ Detail van operationele lease te zien in [[operationele-leasing]]
(nog te creëren).

## Vergelijking financiële vs operationele leasing

| Aspect | Financiële leasing | Operationele leasing |
|---|---|---|
| Economisch eigenaarschap | Bij leasingnemer | Bij leasinggever |
| Boekhouding actief | Geactiveerd (25) | Niet geactiveerd |
| Boekhouding schuld | Op balans (172/42) | Niet op balans |
| Kost spreiding | Afschrijving + rente | Huurkost lineair |
| Restwaarde-optie | Typisch met aantrekkelijke koopoptie | Geen koopoptie of marktconform |
| Investeringsaftrek | ⚠️ Mogelijk | ⚠️ Niet |
| Risico actief | Bij leasingnemer | Bij leasinggever |
| Geschikt voor | Lange-termijn-gebruik, intentie tot overname | Korte termijn, geen overname |

🔗 Onder oude BGAAP gaf operationele lease een "off-balance"-voordeel —
geen schuldzichtbaarheid. Onder IFRS-16 verdwenen die voordelen voor
geconsolideerde rapportering. ⚠️ Voor BE-BGAAP statutaire jaarrekening
te verifiëren.

## Veelvoorkomende verwarringen

- **Renting ≠ operationele leasing.** Renting is meestal een
  korterlopende huur met service-inbegrip, vooral voor wagens.
- **Sale-and-lease-back** — verkoop met onmiddellijke terugleasing.
  Boekhoudkundig en fiscaal eigen regels (winstuitstel, etc.) — eigen
  record waard.
- **Erfpacht en opstal** zijn juridisch andere constructies maar kunnen
  economisch lijken op leasing — te verifiëren.

## Alternatieven (zelfde doel: actief gebruiken zonder aankoop)

- [[operationele-leasing]] — huur zonder economisch eigenaarschap
- [[huur]] — gewone huur (vaak korter, met service)
- [[renting]] — operationele lease + service (typisch wagens)
- [[bankfinanciering-investering]] — lenen om te kopen
- [[obligatielening]] — lange-termijn schuldfinanciering

→ Vergelijkingsmatrix: [[vergelijking-investeringsfinanciering]]

## Wat dit record dekt

### Behandelde competenties (chronologisch)

1. **Klant adviseren** over keuze financiële vs operationele leasing vs
   aankoop met financiering.
2. **Leasecontract kwalificeren** als financieel of operationeel ⚠️.
3. **Aanvang boekhoudkundig verwerken** (activeren + schuld) ⚠️.
4. **Jaarlijkse routine** — leasebetaling splitsen, afschrijven, rente
   boeken ⚠️.
5. **Toelichting jaarrekening** opstellen ⚠️.
6. **Restwaarde-optie behandelen** op vervaldag (lichten of teruggeven) ⚠️.
7. **Investeringsaftrek aanvragen** indien van toepassing ⚠️.
8. **BTW-pro rata** correct verwerken ⚠️.

### Behandelde termen (alfabetisch)

economische eigendom · financieringshuur · impliciete leaserente ·
koopoptie · leasebetaling · leasingmaatschappij · leasingnemer ·
operationele leasing · rentecomponent · restwaarde · sale-and-lease-back ·
substance over form

### Behandelde formules

- **Splitsing leasebetaling** = kapitaalaflossing + rentecomponent
  (via actuariële tabel obv impliciete rente). ⚠️ Detail-formule te
  verifiëren.

### Behandelde regimes (via edges)

[investeringsaftrek](#fiscaal) ⚠️ ·
[aftrekbaarheid-financieringskosten](#fiscaal) ⚠️

## Bronnen en verwijzingen

**Bronnen (grounded)** ⚖️:
- ⚠️ [[KB-WVV]] — definitie financiële leasing en kwalificatie-criteria
- ⚠️ [[CBN]] — advies leasing (nummer te verifiëren)
- ⚠️ [[WIB92]] — investeringsaftrek + aftrekbaarheid rente

**Te verifiëren** ⚠️ (veel — dit record is dunner gegrond):
- Exacte kwalificatie-criteria onder BE-BGAAP
- MAR-rekeningnummers (25 / 172 / 42 / 6302)
- Splitsing leasebetaling: methode, voorbeeld
- Afschrijfduur regels
- Investeringsaftrek-voorwaarden en tarief
- BTW-regime
- Sale-and-lease-back-specifieke regels

**Cross-record edges**:
- `gerelateerd` → [[operationele-leasing]], [[huur]], [[renting]],
  [[bankfinanciering-investering]], [[sale-and-lease-back]]
- `valt_onder_regime` → [[investeringsaftrek]] ⚠️,
  [[aftrekbaarheid-financieringskosten]]
- `verward_met` → [[operationele-leasing]], [[renting]], [[huur]]

---

## Iteratie-log

**v1 (huidige)** — eerste mockup van een **instrument met sterke
vergelijking-as**. Test van het v5-patroon waarbij de hoofdspanning niet
zit in *wat is het* maar in *waarom dit i.p.v. alternatief X*.

**Wat opvalt vs obligatielening**:
- **Vergelijkingsmatrix** krijgt eigen sectie (Financiële vs
  operationele) — niet uit te stellen tot het einde. Misschien zou ze
  zelfs *vóór* Hoe het werkt moeten staan, omdat de kwalificatie het
  centrale onderwerp is.
- **Kwalificatie als kind-vraag** — financiële vs operationele is geen
  bijzaak maar de hoofd-vraag. Misschien verdient kwalificatie een eigen
  rubriek bij dit type instrument.
- **Veel ⚠️**: minder bronvast dan obligatielening; MAR-rekeningen +
  KB WVV-criteria + investeringsaftrek-regels te verifiëren.

**Open punten**:
- Moet **vergelijking** met alternatief (operationele lease) een
  *eigen rubriek* worden voor instrumenten met sterke alternatieven? Of
  is de bestaande "Alternatieven (zelfde doel)"-sectie voldoende?
- Bij twee zo-nauw-verbonden concepten (financiële + operationele lease)
  — is een **gedeeld synthese-record** met de matrix beter dan
  vergelijking-secties in beide records?
