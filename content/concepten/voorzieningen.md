---
title: "Voorzieningen"
concept_type: "balanspost"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 1.1.II.I
tags:
  - concept
  - schema-2.2
  - type-balanspost
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/voorzieningen.json"
---

# Voorzieningen

_Balanspost_

🏢 Entiteit · Anchors: `1.1.II.I` · Wave: `extract-jaarrekening-rest-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: provisies

## Definitie

📖 Een **voorziening** is een passiefpost (MAR-klasse 16) die op balansdatum een **bestaand risico of toekomstige verplichting** dekt waarvan het **bedrag of de termijn onzeker** is, maar waarvan de uitstroom van middelen voldoende waarschijnlijk is om erkenning te rechtvaardigen. De voorziening is gebaseerd op het **voorzichtigheidsbeginsel** (art. 3:23 KB): de onderneming moet anticiperen op kosten en verliezen die uit het verleden voortvloeien, ook als de exacte uitbetalingsdatum of het exacte bedrag nog niet vaststaat. Voorzieningen verschillen van **schulden** (waar zowel bedrag als termijn vaststaan) en van **uitgestelde belastingen** (een specifiek timing-verschil-fenomeen, ondanks dezelfde klasse 16).

<small>📚 KB 29-04-2019 WVV — art. 3:33 — _kb_ · KB 29-04-2019 WVV — art. 3:23 — _kb_</small>

## Substantie

📖 De **MAR-klasse 16** kent volgende sub-rubrieken:
- **160** Pensioenen en soortgelijke verplichtingen
- **161** Belastingen (geschillen + vermoede aanslagen)
- **162** Grote herstellingen en onderhoud
- **163** Andere risico's en kosten (waarborgen aan klanten, hangende processen, herstructurering)
- **168** Uitgestelde belastingen (zie apart record)

**Boekingsschema**:
- Aanleg: **635/637 Voorzieningen voor risico's en kosten** (kost) D | **160-163** (passief) C
- Aanwending bij voordoen risico: **160-163** D | rechtstreeks tegen werkelijke kost
- Terugneming bij wegvallen: **160-163** D | **6350/6370** C (resulteert in kostenvermindering)

<small>📚 KB 29-04-2019 WVV — bijlage MAR — Klasse 16 (160-163, 168) — _kb_</small>

## Rationale

🔗 Voorzieningen bestaan om het **matching-principe** in evenwicht te brengen met het **voorzichtigheidsbeginsel**: gebeurtenissen uit het verleden (bv. een verkoop met productgarantie, of een proces dat aanhangig is gemaakt) genereren toekomstige kosten waarvan de exacte realisatie onzeker is. Als deze niet werden voorzien, zou het resultaat van het huidige boekjaar te rooskleurig zijn en het resultaat van het toekomstige jaar te zwaar belast. De voorziening 'reserveert' kost in het jaar waarin het risico ontstond, ook al wordt de uitbetaling pas later geconcretiseerd.

<small>📚 KB 29-04-2019 WVV — art. 3:23 — _kb_</small>

## Bouwstenen

### 📜 Erkenningscriteria voorziening  
_`regel`_

📖 Een voorziening wordt erkend als **cumulatief** wordt voldaan:
1. **Bestaande verplichting** — voortspruitend uit een gebeurtenis in het verleden (juridisch of feitelijk, bv. publiek aangekondigde herstructurering);
2. **Waarschijnlijke uitstroom** van middelen om de verplichting af te wikkelen;
3. **Betrouwbare schatting** van het bedrag mogelijk.

Voldoet de situatie aan (1) en (2) maar niet aan (3) → **voorwaardelijke verplichting** in toelichting (klasse 0 of disclosure), geen passiefpost. Voldoet alleen aan (1) → vermelding in toelichting indien materieel.

<small>📚 KB 29-04-2019 WVV — art. 3:33 — _kb_</small>

### ⚙️ Waardering — best estimate + eventuele actualisatie  
_`mechanisme`_

📖 Een voorziening wordt gewaardeerd aan het **beste schattingsbedrag** dat de onderneming op balansdatum verwacht uit te geven om de verplichting af te wikkelen. Voor **langetermijn-voorzieningen** (bv. pensioenverplichtingen op 10-20 jaar) mag de waarde worden **geactualiseerd** met een redelijke disconteringsvoet (typisch overheidsobligatierente van vergelijkbare looptijd). De jaarlijkse **opbouw van de actualisatie** wordt geboekt als financiële kost (klasse 65).

<small>📚 KB 29-04-2019 WVV — art. 3:33 — _kb_</small>

## Voorbeelden

### 💡 Voorziening waarborg op verkochte producten 🔗

_Zelena Bio NV verkoopt jaarlijks 100.000 producten met 2 jaar garantie. Op basis van historische ervaring komt 2 % van de producten terug onder garantie, gemiddelde herstelkost 15 EUR.

**Aanleg op 31-12** (boekjaar 1):
- Verwachte garantieclaims: 100.000 × 2 % × 15 EUR = **30.000 EUR**
- Boeking:
```
637 Voorzieningen voor andere risico's en kosten    D 30.000
   163 Voorzieningen voor andere risico's            C 30.000
```

**Aanwending in boekjaar 2** wanneer claims binnenkomen (bv. herstel kost 25.000 EUR):
```
163 Voorzieningen voor andere risico's              D 25.000
   614/611                                          C 25.000 (tegen werkelijke kost)
```
Als er na het garantieperiode nog 5.000 EUR voorziening overblijft → **terugneming**:
```
163                                                 D 5.000
   6370 Terugnemingen voorzieningen                C 5.000
```_

<small>📚 KB 29-04-2019 WVV — art. 3:33 — _kb_</small>

### 💡 Voorziening grote herstelling — cyclisch onderhoud 🔗

_Een industriële onderneming heeft een productielijn die elke 5 jaar een groot onderhoud nodig heeft (kost ca. 200.000 EUR). Tussenliggende jaren: kleine onderhoudsbeurten.

**Spreiding via voorziening**: elk jaar wordt 40.000 EUR geboekt als voorziening (162) om de toekomstige grote onderhoudsuitgave te spreiden over de 5 jaren waarin de slijtage opbouwt. Dit voldoet aan het matching-principe — onderhoudskost evenredig met gebruiksperiode._

<small>📚 KB 29-04-2019 WVV — art. 3:33 — _kb_</small>

## Valkuilen

### ⚠️ Voorziening verwarren met reserve

**Verkeerde assumptie**: Een voorziening en een reserve zijn allebei buffers tegen toekomstige tegenvallers.

**Kernpunt**: Geen. Een **voorziening** (klasse 16, **passief**) dekt een **specifiek bestaand risico of verplichting** uit het verleden — komt **ten laste van het resultaat** (klasse 63). Een **reserve** (klasse 13, **eigen vermogen**) is een **bestemming van behaalde winst** — geen kostenpost, geen specifiek risico, maar interne winstreservering voor toekomstige groei of dividend-uitsmering.

<small>📚 KB 29-04-2019 WVV — Klasse 13 vs Klasse 16 — _kb_</small>

### ⚠️ Voorziening boeken zonder bestaande gebeurtenis

**Verkeerde assumptie**: Je kunt anticipatief een voorziening boeken voor mogelijke toekomstige tegenvallers — bv. een algemene 'crisis-voorziening' van 100.000 EUR.

**Kernpunt**: Een voorziening vereist een **gebeurtenis in het verleden** die de verplichting creëert. Algemene 'voor-de-zekerheid'-voorzieningen zonder concreet aanwijsbare oorzaak zijn **niet toegelaten** — dat zou winst manipuleren ('cookie jar reserving'). Voor toekomstige tegenvallers die geen passend voorzieningsfeit hebben: gebruik een **reserve** uit winstbestemming.

<small>📚 KB 29-04-2019 WVV — art. 3:33 — _kb_</small>

## Verder lezen (scope-out)

- → Uitgestelde belastingen (zelfde klasse 16 ander fenomeen) → [[uitgestelde-belastingen]] _(moet-verwijzen)_
- ↪ IFRS-IAS 37 (provisions) → [[ifrs]] _(mag-verwijzen)_
- ↪ Schulden op korte termijn → [[schulden-op-korte-termijn]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[boekhouding]]
### `vereist`
- [[boekhoudbeginselen]]
### `vergelijkbaar_met`
- [[schulden-op-korte-termijn]]
    - **Gelijkenissen**:
        - Beide passief-rubrieken die toekomstige uitstroom van middelen erkennen
    - **Verschillen**:
        - Schuld: bedrag + termijn vaststaan; voorziening: minstens één van beide onzeker
        - Schuld: feitelijk al geconsumeerd (factuur, loon, lening); voorziening: risico nog te realiseren
    - ⚠️ **Verwarringsrisico**: Stagiairs boeken een vaststaande factuur als voorziening of een onzeker risico als schuld.
- [[uitgestelde-belastingen]]
    - **Gelijkenissen**:
        - Beide gebruiken MAR-klasse 16
    - **Verschillen**:
        - Voorziening (160-163): risico/kost-driven; uitgestelde belasting (168): timing-verschil-driven tussen fiscaal en boekhoudkundig resultaat
        - Voorziening raakt klasse 63 (operating); uitgestelde belasting raakt klasse 67 (belastingen)
    - ⚠️ **Verwarringsrisico**: Beide klasse 16 — studenten denken dat het hetzelfde fenomeen is.
