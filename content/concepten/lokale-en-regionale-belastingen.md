---
title: "Lokale en regionale belastingen"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 2.7.I
  - 2.7.II
  - 2.7.taak.1
  - 2.7.taak.2
  - 2.7.taak.3
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/lokale-en-regionale-belastingen.json"
---

_Kader_

## Definitie

Lokale en regionale belastingen omvat alle belastingen geheven door overheden onder het federale niveau: de drie gewesten (Vlaanderen, Wallonië, Brussel) en de lokale besturen (provincies en gemeenten). Het is een Σ-overzicht dat de fiscale driehoek federaal — gewest — gemeente in kaart brengt en aanduidt waar elke deelbevoegdheid grondslag, tarief en inning bepaalt. De bevoegdheidsverdeling steunt op artikel 170 Grondwet (legaliteit + decentralisering), de Bijzondere Financieringswet van 16 januari 1989 (gewestelijk niveau) en artikelen 41 en 162 Grondwet (gemeentelijk en provinciaal niveau).

<small>📖 Grondwet — art. 170 — _wettekst_ · Grondwet — art. 41 — _wettekst_ · Grondwet — art. 162 — _wettekst_ · BWHI 16-01-1989 — art. 3 — _wettekst_</small>

## Substantie

Voor de accountant betekent dit drie parallelle systemen die naast elkaar bestaan voor één cliënt: een vennootschap die in Vlaanderen gevestigd is en een onroerend goed in Wallonië bezit, betaalt federale VenB, Vlaamse aanvullende gemeentebelasting (via PB-werknemers), Waalse onroerende voorheffing op het Waalse vastgoed, en lokale Vlaamse heffingen (bedrijfsbelasting, milieuheffing) van de gemeente waar de zetel ligt. Voor advies, aangifte en betwisting moet de accountant per belasting opnieuw uitzoeken: welk niveau? welke procedure? welke beroepsweg? Het concept is daarom vooral een navigatie-instrument om bevoegdheid en procedureregime correct te alloceren.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

De Belgische staatsstructuur kent geen unitair fiscaal systeem: opeenvolgende staatshervormingen hebben fiscale bevoegdheden gedecentraliseerd om gewesten en lokale besturen autonoom beleid te laten voeren in materies die hen toegewezen zijn (huisvesting, milieu, mobiliteit, gemeentelijk welzijn). De overlap-risico's worden afgedwongen door (1) het legaliteitsbeginsel — elk niveau heft enkel via een eigen norm (wet, decreet, ordonnantie, reglement); (2) non-bis-in-idem — geen dubbele belasting op hetzelfde feit; (3) wettelijke verbods-lijsten zoals WIB92 art. 464 (gemeenten en provincies mogen geen opcentiemen heffen op PB, VenB, RPB of BNI).

<small>📖 Grondwet — art. 170 — _wettekst_ · WIB92 — art. 464 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: Grondwet art. 41, 162, 170 + BWHI 16-01-1989 + gewest-specifieke codices (VCF, Brusselse Codex Fiscale Procedure, Waals decreet 6-5-1999) + gemeentewetten/-decreten

**✅ Voor**
- 🔗 Telkens een belasting niet duidelijk federaal is: eerst bepalen aan welk niveau ze toebehoort (gewestelijk/provinciaal/gemeentelijk), dan welke procedure-codex geldt, dan welke administratie ze int.

## Sub-concepten

### 📦 Driehoek federaal — gewest — lokaal

#### Definitie

Drie bevoegdheidsniveaus naast elkaar. Federaal: alle 'klassieke' belastingen (PB-basis, VenB, btw, accijnzen, douane) — basis WIB92 + Btw-Wetboek + W.Acc. Gewestelijk: lijst van eigen belastingen (registratie, successie, OV, verkeersbelasting, BIV, eurovignet, spelen en weddenschappen, …) + aanvullende gewestelijke PB via opcentiemen/kortingen — basis BFW. Lokaal: gemeentelijke en provinciale belastingen op alles wat niet federaal of gewestelijk verboden is (bedrijfsbelasting, milieu, parkeer, tweede verblijven, reclameborden, …) + aanvullende gemeentebelasting PB als belangrijkste opbrengstpost — basis GW art. 41/162/170 §4 + gemeentewetten.

<small>📖 Grondwet — art. 170 — _wettekst_ · BWHI 16-01-1989 — art. 3 — _wettekst_ · WIB92 — art. 464 — _wettekst_</small>

#### ⚙️ Vergelijkingstabel bevoegdheden

Per niveau de drie sleutelvragen: (a) wie heft? (b) welk reglementair instrument? (c) welke beroepsweg?

• Federaal — FOD Financiën heft → wet (WIB92, BtwW, AWGI, WMGI) → bezwaar bij gewestelijke directeur, daarna fiscale rechtbank → hof van beroep.
• Gewest — VLABEL/Brussel Fiscaliteit/SPW Fiscalité heft → decreet of ordonnantie (VCF, Brusselse Codex Fiscale Procedure, Waals decreet) → bezwaar bij gewestelijke fiscaliteitsdienst, daarna fiscale rechtbank.
• Gemeente/Provincie — gemeentebestuur/provinciebestuur heft → belastingreglement (raadsbeslissing) → bezwaar bij College van Burgemeester en Schepenen / Bestendige Deputatie, daarna fiscale rechtbank.

<small>🔗 Grondwet — art. 170 — _wettekst_ · Brusselse Codex Fiscale Procedure — art. 117-124 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Bouwstenen

### ✴️ Legaliteitsbeginsel (art. 170 GW)

Geen belasting zonder wet — elke belasting heeft een normatieve grondslag op het juiste niveau. §1: federaal — wet; §2: gewest — decreet/ordonnantie binnen BFW-grenzen; §3 (geschrapt) — gemeenschappen; §4: provincies en gemeenten — eigen reglement binnen de wet die hun bevoegdheid omkadert. Een belasting zonder geldige norm is nietig.

<small>📖 Grondwet — art. 170 — _wettekst_</small>

### ✴️ Non-bis-in-idem tussen niveaus

Een lager niveau mag niet hetzelfde belastbaar feit belasten dat al door een hoger niveau belast wordt, behoudens bij wet/decreet uitdrukkelijk toegelaten. Concrete uitwerkingen: WIB92 art. 464 verbiedt gemeenten en provincies om opcentiemen op PB, VenB, RPB of BNI te heffen — uitzondering: de aanvullende gemeentebelasting op PB (art. 465 e.v. WIB92) is wel uitdrukkelijk toegelaten. VCF art. 2.3.4.2.2 verbiedt opcentiemen op BIV.

<small>📖 WIB92 — art. 464 — _wettekst_ · VCF — art. 2.3.4.2.2 — _wettekst_</small>

### 📜 Aanvullende gemeentebelasting op de PB als hoofdbron lokale fiscaliteit

Gemeenten heffen procentuele opcentiemen (typisch 6-9 %) op de federaal berekende PB van hun inwoners (WIB92 art. 465-470). Voor de meeste gemeenten is dit de grootste fiscale ontvangst, naast de gemeentelijke opcentiemen op de gewestelijke onroerende voorheffing. Tarief vastgesteld door gemeenteraad in jaarlijks belastingreglement. De FOD Financiën int en stort door.

<small>📖 WIB92 — art. 465 t.e.m. 470 — _wettekst_</small>

## Valkuilen

> [!warning]- Bevoegdheidsallocatie verwarren bij multi-gewestelijk dossier
> **Verkeerde assumptie**: Een Vlaamse cliënt = altijd Vlaamse fiscaliteit voor alles.
>
> **Kernpunt**: Per belasting opnieuw lokaliseren: PB-aanvullend = gemeente van fiscale woonplaats op 1 januari; OV/registratierechten = ligging onroerend goed; verkeersbelasting/BIV = inschrijver-woonplaats; aanvullende gewestelijke PB = gewest van woonplaats op 1 januari. Eén cliënt kan dus in 2 of 3 gewesten tegelijk belastbaar zijn voor verschillende belastingen.
>
> <small>🔗 BWHI 16-01-1989 — art. 5 §2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Bezwaarprocedure verwarren tussen niveaus
> **Verkeerde assumptie**: Stagiair stuurt bezwaar tegen gemeentebelasting naar gewestelijke directeur (federaal-PB-reflex).
>
> **Kernpunt**: Bezwaar tegen gemeentebelasting → College B&S binnen termijn van het belastingreglement (typisch 3 maanden). Bezwaar tegen Vlaamse gewestbelasting → VLABEL. Bezwaar tegen federale belasting → gewestelijke directeur AAFisc. Elk niveau heeft eigen termijn en eigen bestuursorgaan; niet onderling uitwisselbaar.
>
> <small>🔗 Brusselse Codex Fiscale Procedure — art. 117 e.v. — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Advies bij opstart vennootschap — gewestelijke en lokale fiscaliteit

_Bij oprichting van een vennootschap of vestigingskeuze adviseert de accountant over de fiscale impact per niveau._

#### 🧭 Adviseur

##### 👣 Vestigingsplaats-impact in kaart brengen

Bij keuze vennootschapszetel of inwoner-domicilie: inventariseer per niveau (gewest + gemeente) de relevante belastingen. Vergelijk effectieve tarieven aanvullende gemeentebelasting PB, OV-opcentiemen (gemeente + provincie), bedrijfsbelasting van de gemeente. Schenkings- en successierechten verschillen per gewest. Voor accountant-advies: cijfers concreet maken met ramingen op basis van jaarlijkse cijferzakboekjes of belastingreglementen.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 🧭 Cliënt waarschuwen voor samenloop tussen niveaus

Bij elk fenomeen dat door meerdere bestuursniveaus geraakt kan worden, doorloopt de accountant een 5-stappen-samenloop-analyse: (1) Inventariseer welke niveaus het fenomeen raken — vastgoed wordt typisch geraakt door federale roerende voorheffing op huurinkomsten in bepaalde regimes, gewestelijke onroerende voorheffing, gemeentelijke + provinciale opcentiemen op OV, eventueel gemeentelijke sui-generis-belastingen (tweede verblijven, leegstand). (2) Toets per niveau-paar of non-bis-in-idem geldt of dat samenloop wettelijk uitdrukkelijk toegelaten is — WIB92 art. 464 verbiedt opcentiemen op PB/VenB/RPB/BNI, maar art. 465 e.v. laat aanvullende gemeentebelasting PB net wel toe. (3) Bereken de totale effectieve fiscale druk cumulatief over de niveaus heen. (4) Identificeer compensatie-mechanismen: bij dubbele belasting op zelfde grondslag soms aftrek of voorheffing-systeem (bv. OV deels verrekenbaar in PB voor eigen woning historisch). (5) Vermijd verrassingen via vooraf-inschatting + waar mogelijk ruling-aanvraag bij Vlabel/Brussel Fiscaliteit/SPW Fiscalité. Communiceer cumulatieve impact aan cliënt vóór beslissing (vestigingsplaats, aankoop tweede verblijf, herstructurering vastgoedportfolio).

<small>🔗 WIB92 — art. 464-470 — _wettekst_ · Grondwet — art. 170 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-29)</small>

### Vertegenwoordiging bij gewestelijke en lokale fiscus

_De accountant vertegenwoordigt de cliënt bij controle, bezwaar of bemiddeling op gewestelijk of lokaal niveau._

#### 👥 Begeleider

##### 🧭 Bezwaar correct routeren per niveau

Eerste vraag bij elk fiscaal dispuut: welk niveau? Aanslagbiljet vermeldt heffingsoverheid + bezwaarinstantie + bezwaartermijn. Termijnen zijn dwingend en niveau-specifiek (federaal PB = 6 maanden vanaf verzending; Vlaamse gewestbelasting = 3 maanden; gemeentebelasting = doorgaans 3 maanden vanaf 3e werkdag na verzending). Verkeerd geadresseerd bezwaar = vaak verlies van termijn.

<small>🔗 WIB92 — art. 366-371 — _wettekst_ · VCF — art. 3.5.2.0.1 e.v. — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Federale fiscale procedure → [[fiscale-procedure]] _(moet-verwijzen)_
- → Gewestelijke fiscale procedure detail → [[gewestelijke-fiscale-procedure]] _(moet-verwijzen)_
- ↪ Oprichting-vennootschap (advies-cross) → [[oprichting-vennootschap]] _(mag-verwijzen)_
- → Registratie + successie (apart gewestelijk cluster) → [[registratie-en-successierechten]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[fiscaal-recht]]
### `bevat`
- [[gewestelijke-fiscale-autonomie]]
- [[lokale-fiscale-autonomie]]
