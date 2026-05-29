---
title: "Maatstaf van heffing — BTW"
concept_type: "principe"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.4.I
tags:
  - concept
  - schema-2.2
  - type-principe
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/maatstaf-van-heffing-btw.json"
---

_Principe_ · ook: btw-grondslag · base d'imposition TVA

## Definitie

De maatstaf van heffing is het bedrag waarop het btw-tarief wordt toegepast om de verschuldigde btw te berekenen. Algemene regel (art. 26, §1 W.BTW): de maatstaf bestaat uit alles wat de leverancier of dienstverrichter als tegenprestatie ontvangt of moet ontvangen van wie ook — koper, afnemer of derde — inclusief subsidies die rechtstreeks met de prijs zijn verbonden, en met inbegrip van bijkomende kosten zoals commissie, verpakking, vervoer en verzekering. Niét inbegrepen: de btw zelf, prijsverminderingen en kortingen die op het tijdstip van de handeling worden toegestaan, en bedragen die de leverancier in naam en voor rekening van zijn klant heeft voorgeschoten (doorrekening van uitschot).

<small>📖 W.BTW — art. 26 + art. 28 — _wettekst_ · Richtlijn 2006/112/EG — art. 73 + art. 78 + art. 79 — _richtlijn_</small>

## Substantie

De maatstaf is geen 'verkoopprijs' zonder meer — het is de breedst-mogelijke economische waarde van wat de leverancier krijgt. Vandaar dat ook ruil in natura, kwijtschelding van schulden, en subsidies die de prijs verlagen voor de eindverbruiker (vb. milieusubsidie op zonnepanelen) tot de maatstaf behoren. Voor de accountant zijn drie typische valstrikken: (1) commerciële kortingen verminderen de maatstaf maar enkel als ze op factuurdatum toegestaan worden — latere kwantumkortingen vereisen een creditnota; (2) doorrekening in naam-en-voor-rekening blijft btw-vrij maar vereist strikt papierwerk (voorschotnota's, originele bewijsstukken); (3) bij ruil moet de marktwaarde van het ontvangen goed of de ontvangen dienst worden gebruikt als maatstaf — niet de boekwaarde.

<small>🔗 W.BTW — art. 26 + art. 28 + art. 32 + art. 33 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

De ruime definitie van 'tegenprestatie' verzekert dat de btw daadwerkelijk drukt op de volledige economische waarde die wordt overgedragen — zonder dat partijen door slimme prijssplitsing (lage hoofdprijs + hoge 'vervoerkosten' bv.) het effectieve tarief kunnen drukken. De uitsluiting van btw zelf vermijdt dubbele heffing. De uitsluiting van kortingen volgt het werkelijk-betaalde-prijs-beginsel. De gelijkstellingen (art. 33) voor onttrekkingen en gratis afgiften zorgen voor neutraliteit: zonder maatstaf zou een onttrekking belastingvrij zijn ondanks de gelijkstelling met levering.

<small>🔗 Richtlijn 2006/112/EG — art. 73 + art. 79 — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Sub-concepten

### 📦 Wat ZIT in de maatstaf — art. 26 + 28 W.BTW

#### Definitie

Inbegrepen in de maatstaf: (1) de bedongen prijs (cash, op rekening of in natura — marktwaarde); (2) subsidies rechtstreeks verbonden met de prijs (= per geleverd stuk of per dienstverrichting); (3) belastingen, rechten en heffingen (douanerechten, accijnzen, ecotaks, BIV) — behalve de btw zelf; (4) bijkomende kosten die de leverancier aan de afnemer aanrekent: commissie, verpakking, vervoer, verzekering, montagekosten.

<small>📖 W.BTW — art. 26 + art. 28 — _wettekst_ · Richtlijn 2006/112/EG — art. 78 — _richtlijn_</small>

### 📦 Wat zit er NIET in de maatstaf — art. 28 W.BTW

#### Definitie

Uitgesloten van de maatstaf: (1) de btw zelf; (2) prijsverminderingen en kortingen toegestaan op het tijdstip van de handeling (cash discount, kwantumkorting, getrouwheidskorting bij factuur); (3) verpakkingsmateriaal en kosten die de leverancier in naam-en-voor-rekening van de klant voorschiet (= 'sommes payées au nom et pour compte') — strikt bewijsbaar; (4) interesten voor uitgestelde betaling indien apart aangerekend.

<small>📖 W.BTW — art. 28 — _wettekst_ · Richtlijn 2006/112/EG — art. 79 — _richtlijn_</small>

#### 📜 Doorrekening in naam-en-voor-rekening

**Substantie**: Voorbeeld: een accountantskantoor schiet 50 EUR neerleggingskosten van de jaarrekening voor bij de NBB. Dat bedrag mag uit de btw-maatstaf gehouden worden mits het origineel bewijsstuk op naam van de cliënt staat en het exact wordt doorgerekend (geen marge). Zonder strikt bewijs: belastbaar.

<small>🔗 W.BTW — art. 28, 5° — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Specifieke maatstaven — gelijkstellingen + invoer + IC-verwerving

#### Substantie

Voor handelingen zonder marktprijs of zonder normale tegenprestatie gelden afgeleide maatstaven.

<small>📖 W.BTW — art. 32 + art. 33 + art. 34 — _wettekst_</small>

#### 🧭 Maatstaf per bijzonder geval

**Substantie**: Vijf bijzondere maatstaven.

<small>📖 W.BTW — art. 32-34 — _wettekst_</small>

## Voorbeelden

> [!example]- Bouw maatstaf van heffing op — vier praktijkvoorbeelden
> _Telkens: bepaal de maatstaf en het te factureren btw-bedrag (21 %)._
>
> | Casus | Maatstaf | Btw 21 % | Toelichting |
>
> | --- | --- | --- | --- |
>
> | Verkoop machine 10 000 EUR + vervoerkosten 500 EUR (door leverancier georganiseerd) | 10 500 EUR | 2 205 EUR | Vervoerkosten = bijkomende kost art. 28 |
>
> | Verkoop 10 000 EUR met 2 % cash discount bij betaling binnen 8 dagen | 9 800 EUR (= 10 000 - 200) | 2 058 EUR | Korting op factuur → buiten maatstaf art. 28, 2° |
>
> | Aannemer factureert 8 000 EUR + 200 EUR doorgerekend brandstof op eigen naam + 50 EUR NBB-neerleggingskosten in naam-en-voor-rekening cliënt | 8 200 EUR (50 EUR uit maatstaf) | 1 722 EUR | NBB-doorrekening = naam-en-voor-rekening art. 28, 5° — brandstof = bijkomende kost |
>
> | Ruil: garage levert auto 25 000 EUR, klant geeft oude auto in inbouw (markt 8 000 EUR) + 17 000 EUR cash | 25 000 EUR | 5 250 EUR | Maatstaf = normale waarde geleverd goed (art. 32) = volle prijs |
>
> <small>🔗 W.BTW — art. 26 + art. 28 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Bijkomende kosten ZITTEN in de maatstaf
> **Verkeerde assumptie**: Vervoerkosten of verpakkingskosten worden apart gefactureerd, dus apart belast (of niet belast).
>
> **Kernpunt**: Art. 28, 1° W.BTW: bijkomende kosten (vervoer, verpakking, commissie, verzekering) die de leverancier aan de afnemer aanrekent in het kader van dezelfde levering zijn ALTIJD onderdeel van de maatstaf — tegen hetzelfde tarief als het hoofdgoed. Een verpakkingskost op een 6 %-levering wordt dus belast aan 6 %, niet aan 21 %. Vermelding op factuur als 'extra' wijzigt daar niets aan.
>
> <small>📖 W.BTW — art. 28, 1° — _wettekst_</small>

> [!warning]- Korting moet op factuur staan
> **Verkeerde assumptie**: Wanneer je achteraf een kwantumkorting toekent, mag je gewoon minder btw afdragen.
>
> **Kernpunt**: Alleen kortingen die op het tijdstip van de handeling worden toegestaan (= op de oorspronkelijke factuur staan) verminderen direct de maatstaf. Latere kortingen (achteraf-bonus, jaarlijkse retro) vereisen een creditnota (KB nr. 1 art. 11) die de maatstaf en de btw retro-actief aanpast. Zonder creditnota = onverminderde btw verschuldigd op de oorspronkelijke maatstaf.
>
> <small>📖 W.BTW — art. 28, 2° + art. 77 — _wettekst_ · K.B. nr. 1 van 29-12-1992 — art. 11 — _kb_</small>

> [!warning]- Subsidie ≠ altijd buiten maatstaf
> **Verkeerde assumptie**: Overheidssubsidies zijn buiten btw-scope.
>
> **Kernpunt**: Subsidies zijn buiten btw-maatstaf wanneer ze niet rechtstreeks aan de prijs gekoppeld zijn (algemene werkingssubsidie). Maar wanneer ze gekoppeld zijn aan een welbepaald aantal geleverde goederen of diensten — zoals een prijsverlaging per zonnepaneel die de overheid betaalt — dan zijn ze WEL maatstaf (art. 26, §1). De toets: krijgt de leverancier de subsidie 'in plaats van' een deel van de prijs die de eindverbruiker anders zou betalen?
>
> <small>🔗 W.BTW — art. 26, §1 — _wettekst_ · HvJ-EU Office des Produits Wallons (C-184/00) — 22-11-2001 — _rechtspraak_</small>

## Verder lezen (scope-out)

- → Tarief toepassen op maatstaf → [[btw-tarieven]] _(moet-verwijzen)_
- ↪ Douanewaarde bij invoer → [[douanewaarde]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[btw]]
### `vereist`
- [[btw-levering-goederen]]
- [[btw-dienstverlening]]
