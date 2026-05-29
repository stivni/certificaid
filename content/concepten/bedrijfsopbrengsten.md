---
title: "Bedrijfsopbrengsten"
concept_type: "balanspost"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 1.1.II.M
tags:
  - concept
  - schema-2.2
  - type-balanspost
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/bedrijfsopbrengsten.json"
---

_Balanspost_ · ook: operationele opbrengsten

## Definitie

Bedrijfsopbrengsten zijn opbrengsten uit de gewone bedrijfsuitoefening — geboekt in MAR-klasse 70 t/m 74: 70 omzet (verkopen + dienstprestaties − toegekende kortingen 708) · 71 wijzigingen in voorraad goederen in bewerking, gereed product en bestellingen in uitvoering · 72 geproduceerde vaste activa · 74 andere bedrijfsopbrengsten (subsidies, terugneming voorzieningen, meerwaarde courante realisatie). Samen met bedrijfskosten (klasse 60-65) vormen ze het bedrijfsresultaat. De kern-rubriek is 70 'omzet' — art. 3:90, I.A KB WVV definieert dit als 'het bedrag van de verkoop van goederen en de levering van diensten aan derden in het kader van de gewone bedrijfsuitoefening, na aftrek van kortingen op verkoop, en exclusief btw en andere rechtstreeks op de omzet bezwarende belastingen'.

<small>📖 KB 29.04.2019 (uitvoering WVV) — art. 3:90, I.A — _kb_ · MAR-KB 21.10.2018 — Bijlage 1 klasse 7 — _kb_</small>

## Substantie

Bedrijfsopbrengsten meten 'wat de kernactiviteit oplevert'. De stagiair moet drie zaken vasthouden: (1) omzet ≠ cash-inning — bij factuur boek je 400 (klant, debet) tegenover 700 (omzet, credit); cash beweegt later. (2) Realisatie-moment: opbrengst wordt verantwoord wanneer goed geleverd of dienst gepresteerd, niet bij bestelling of betaling (matching, voorzichtigheid, accrual). (3) Omzet ≠ totale bedrijfsopbrengsten — 70 is enkel kerncommerciële omzet; subsidies (740-743), recuperaties (744-746), terugnemingen waardeverminderingen (749) en geproduceerde-vaste-activa (72) zijn ook bedrijfsopbrengsten maar staan apart. Het groottecriterium 'omzet ≤ 9 mio EUR voor kleine vennootschap' (art. 1:24 WVV) kijkt naar rubriek 70 alleen — niet naar totaal bedrijfsopbrengsten (zie CBN 2022/03 voor afwijkende regeling indien rubriek 74 > 50%).

<small>📖 CBN-advies 2022/03 — Beoordeling groottecriteria — afwijkende regeling — _cbn_ · CBN-advies 100 — Omzet — begrip — _cbn_</small>

## Rationale

Het MAR-onderscheid tussen omzet (70) en andere bedrijfsopbrengsten (74) bestaat omdat omzet de primaire economische maatstaf is: zij meet de schaal van de kernactiviteit, drijft groottecriteria, vennootschapsbelasting-tarieven, en bank-rapportering. Andere bedrijfsopbrengsten zijn vaak niet-recurrent of niet-commercieel (subsidie, recuperatie verzekering, terugneming waardevermindering vorderingen). Voor analyse: omzetgroei jaar-op-jaar = bedrijfsmatige indicator; andere bedrijfsopbrengsten kunnen het bedrijfsresultaat tijdelijk flatteren — vandaar de afwijkende regeling van CBN 2022/03.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 📖 Boeken van uitgaande facturen + dienstprestaties — bij elke verkoop/levering boekt de boekhouder 400 (klant) D / 700 (omzet) C + 451 (te betalen btw) C.
- 📖 Beoordeling groottecriteria voor jaarrekeningvorm (volledig/verkort/microschema) — omzet rubriek 70 als drempel naast balanstotaal en personeelsbestand (art. 1:24 WVV).

## Sub-concepten

### 📦 70 — Omzet

#### Definitie

Omzet (art. 3:90, I.A KB WVV) = bedrag verkoop goederen + levering diensten aan derden in het kader van de gewone bedrijfsuitoefening, na aftrek kortingen op verkoop, exclusief btw en andere rechtstreeks op de omzet bezwarende belastingen (accijnzen, verbruiksbelasting — CBN 2013/11). Sub-rubrieken 700-707 = verkopen en dienstprestaties · 708 = toegekende kortingen, ristorno's en rabatten (debet — verminderen omzet).

<small>📖 KB 29.04.2019 — art. 3:90, I.A — _kb_ · CBN-advies 2013/11 — Begrip omzet — doorrekening belastingen — _cbn_</small>

> [!example]- Verkoop handelsgoederen 5.000 EUR + 21% btw aan klant
> _Zelena Bio NV verkoopt aan klant Aurelia Holding NV._
>
> **📒 Boeking uitgaande factuur**
>
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | 400 — Handelsdebiteuren | 6.050 |  |
> | 700 — Verkopen |  | 5.000 |
> | 451 — Te betalen btw |  | 1.050 |
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- Korting 10% achteraf via creditnota — 500 EUR
> _Aurelia krijgt 10% korting op de factuur (500 EUR)._
>
> **📒 Boeking creditnota — korting**
>
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | 708 — Toegekende kortingen op verkoop (-) | 500 |  |
> | 451 — Te betalen btw | 105 |  |
> | 400 — Handelsdebiteuren |  | 605 |
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 71 — Wijzigingen in voorraad goederen in bewerking, gereed product en bestellingen in uitvoering

#### Definitie

Klasse 71 boekt het verschil tussen eindvoorraad en beginvoorraad voor goederen in bewerking (32), gereed product (33) en bestellingen in uitvoering (37). Sub-rubrieken: 712 wijziging voorraad goederen in bewerking · 713 gereed product · 717 bestellingen in uitvoering. Bij toename voorraad: 71 credit (= bedrijfsopbrengst — verbruik nog niet gerealiseerd); bij afname: 71 debet (kost). Doel: matching tussen productiekost (klasse 60-62) en opbrengst (klasse 70).

<small>📖 MAR-KB — Bijlage 1 — klasse 71 — _kb_</small>

### 📦 72 — Geproduceerde vaste activa

#### Definitie

Wanneer de onderneming zelf vaste activa produceert (intern ontwikkelde software, eigen bouw gebouw), worden de productiekosten in klasse 6 geboekt en gecompenseerd via 72 (credit) — gelijktijdig met activering in klasse 21/22 (debet). Resultatenrekening blijft neutraal; geactiveerd actief verschijnt op balans.

<small>📖 MAR-KB — Bijlage 1 — klasse 72 — _kb_</small>

### 📦 74 — Andere bedrijfsopbrengsten

#### Definitie

Niet-omzet bedrijfsopbrengsten: 740 exploitatiesubsidies en compensatiebedragen + 741 meerwaarden op realisatie courante vaste activa + 742 meerwaarden op realisatie handelsvorderingen + 743/748 diverse + 749 als bedrijfsopbrengst op te nemen terugneming waardeverminderingen. Belangrijk: subsidies tellen niet mee voor omzet-groottecriterium (zie rubriek 70 / art. 1:24 WVV).

<small>📖 MAR-KB — Bijlage 1 — klasse 74 — _kb_ · CBN-advies 2022/03 — Afwijkende regeling — rubriek 74 — _cbn_</small>

### 📦 Realisatie-moment — wanneer omzet boeken?

#### Definitie

Be-GAAP (KB WVV): omzet wordt verantwoord wanneer goed geleverd / dienst gepresteerd en factuur uitgereikt (of uitreikbaar). Voor langlopende projecten (bouw, advies, software-implementatie): 'percentage of completion' (voortgangsmethode — rubriek 717 bestellingen in uitvoering) of 'completed contract' (afgewerkte opdracht). IFRS 15: 5-stappen-model — (1) identificeer contract met klant; (2) identificeer prestatieverplichtingen; (3) bepaal transactieprijs; (4) wijs prijs toe aan prestatieverplichtingen; (5) verantwoord omzet bij voldoening prestatieverplichting (point-in-time of over-time).

<small>📖 Verordening (EU) 2023/1803 — IFRS 15 — Opbrengsten van contracten met klanten — _wettekst_</small>

## Valkuilen

> [!warning]- Omzet ≈ totale bedrijfsopbrengsten verwarren
> **Verkeerde assumptie**: Voor het groottecriterium telt het totaal van klasse 70-74.
>
> **Kernpunt**: Art. 1:24 WVV en art. 1:25 WVV gebruiken 'omzet' in de strikte zin — rubriek 70 alleen (verkopen + dienstprestaties). Subsidies, recuperaties en meerwaarden uit klasse 74 tellen niet. Uitzondering: CBN 2022/03 afwijkende regeling bij vennootschappen waar opbrengsten uit gewoon bedrijf voor > 50% niet onder omzet-definitie vallen (bv. holdings).
>
> <small>📖 CBN-advies 2022/03 — Afwijkende regeling — _cbn_ · WVV — art. 1:24-1:25 — _wettekst_</small>

> [!warning]- Btw incl. boeken op 70
> **Verkeerde assumptie**: De totale factuurwaarde inclusief btw belandt op 700.
>
> **Kernpunt**: Omzet 70 is exclusief btw. Btw (21%, 12%, 6%, 0%) gaat naar 451 'te betalen btw'. Verkoopprijs bruto 605 EUR = 500 omzet (700) + 105 btw (451). Examen-valkuil: bij vrijgestelde activiteit (medisch, onderwijs, financieel) is er geen btw maar nog steeds 70 voor verkoopprijs.
>
> <small>📖 KB 29.04.2019 — art. 3:90 I.A — exclusief btw — _kb_</small>

> [!warning]- Realisatie versus inning verwarren
> **Verkeerde assumptie**: Omzet wordt geboekt wanneer de klant betaalt.
>
> **Kernpunt**: Omzet wordt verantwoord bij levering/prestatie (accrual-principe), niet bij betaling. Een verkoop in december 20X4 met betaling in maart 20X5 is omzet van 20X4. Cash-basis is alleen toegelaten voor vereenvoudigde boekhouding (eenmanszaken ≤ omzet-drempel). Dit verklaart waarom omzet > cash-inning bij groeiende ondernemingen.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Onderneming zelf — operationele boekhouding

#### 📒 Boekhouder

##### 👣 Onderscheid omzet (70) vs andere bedrijfsopbrengsten (74)

Per binnenkomende opbrengst: (1) is dit een verkoop van goederen of dienst aan derden in het kader van de gewone bedrijfsuitoefening → 70. (2) Is dit een subsidie van overheid → 740. (3) Is dit een terugneming van een eerdere waardevermindering → 749. (4) Is dit een meerwaarde op verkoop courante vaste activa → 741. Onderscheid is belangrijk voor groottecriteria-toets en voor management-rapportage.

<small>🔗 MAR-KB — Bijlage 1 — klasse 70-74 — _kb_</small>

#### 🔍 Auditor

##### 👣 Omzet-cutoff rond balansdatum

Belangrijkste audit-risico bij omzet: 'pulled-forward' omzet = verzendingsdatum manipuleren om vóór balansdatum te zijn. Procedures: (1) toets laatste 10-20 verkoopfacturen vóór balansdatum tegen verzendbon/leverbon; (2) toets eerste 10-20 facturen na balansdatum; (3) reconciliëer omzet-saldo met btw-aangifte Q4; (4) toets pro rata van langlopende projecten (rubriek 717). ISA 240: presumptie van risico op fraude in omzeterkenning.

<small>📖 ISA 240 — paragraaf 26 — _norm_</small>

#### 💰 Fiscaal adviseur

##### 👣 Omzet naar aangifte VenB / PB

VenB: omzet wordt opgenomen in vak 'Belastbare opbrengsten' van aangifte 275.1. Tarief 25% (of verlaagd 20% op eerste 100.000 EUR voor kleine vennootschappen — art. 215 WIB92). PB (eenmanszaak): bruto-omzet naar vak XVII rubriek 'baten' of 'winst'. Controleer aansluiting met btw-aangifte rooster 00-03 + 44 + 45 + 46 (uitgaande handelingen).

<small>🔗 WIB92 — art. 215 (verlaagd tarief KMO) — _wettekst_</small>

## Verder lezen (scope-out)

- → Bedrijfskosten (klasse 60-65) → [[bedrijfskosten]] _(moet-verwijzen)_
- → IFRS 15 — opbrengstverantwoording → [[opbrengstverantwoording]] _(moet-verwijzen)_
- → Niet-recurrente verrichtingen (uitzonderlijke opbrengsten) → [[niet-recurrente-verrichtingen]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- ⏳ resultatenrekening — Bedrijfsopbrengsten = creditzijde bedrijfsresultaat-deel.
### `vergelijkbaar_met`
- [[bedrijfskosten]]
    - **Gelijkenissen**:
        - Beide vormen het bedrijfsresultaat
    - **Verschillen**:
        - Klasse 70-74 (credit) versus klasse 60-65 (debet)
### `vereist`
- ⏳ rekeningstelsel-mar
### `alternatief_referentiestelsel`
- [[opbrengstverantwoording]] — IFRS 15-aanpak vs Be-GAAP — verschillende erkennings-momenten bij langlopende contracten.
