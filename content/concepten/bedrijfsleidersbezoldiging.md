---
title: "Bedrijfsleidersbezoldiging"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.2.taak.3
  - 2.3.taak.3
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/bedrijfsleidersbezoldiging.json"
---

# Bedrijfsleidersbezoldiging

_Regime_

📋 Regeling · Anchors: `2.2.taak.3` · `2.3.taak.3` · Wave: `skeleton-cross-cutting-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: bedrijfsleidersloon · zaakvoerdersbezoldiging · rémunération de dirigeant d'entreprise — **Vertalingen**: fr: rémunération de dirigeant d'entreprise

## Definitie

📖 Bezoldigingen van bedrijfsleiders zijn alle beloningen verleend of toegekend aan een natuurlijke persoon die (1) een opdracht als bestuurder, zaakvoerder, vereffenaar of soortgelijke functies uitoefent, of (2) in een vennootschap een leidende functie of een leidende werkzaamheid van dagelijks bestuur, van commerciële, financiële of technische aard uitoefent buiten een arbeidsovereenkomst (art. 32 WIB92). Ze omvatten vaste/veranderlijke tantièmes, zitpenningen, voordelen alle aard, geherkwalificeerde huur (boven 5/3 van het gerevaloriseerd KI) en alle sommen die de vennootschap toekent buiten dividenden of terugbetaling eigen kosten.

<small>📚 WIB92 — art. 32 — _wettekst_</small>

## Substantie

🔗 Bedrijfsleidersbezoldiging is een hoofdstrategisch instrument: de zaakvoerder bouwt zijn vergoeding op uit een mix van vier kanalen die elk een eigen fiscale logica hebben. (1) Maandelijks loon — onderworpen aan progressieve PB (tot 50 %) + bedrijfsvoorheffing + sociale bijdragen zelfstandige; aftrekbaar als kost in vennootschap. (2) Tantième — geboekt na het belastbare tijdperk maar fiscaal in datzelfde tijdperk aftrekbaar via art. 195 WIB; voorheffing inhouden bij toekenning AV. (3) VAA (woning, auto, lening, energie) — forfaitair gewaardeerd, bij loon gevoegd, deels aftrekbaar in vennootschap (autokosten + 17 %/40 % verworpen uitgave). (4) Onrechtstreekse vergoeding — huur (art. 32-3° herkwalificatie), groepsverzekering/IPT (80 %-regel art. 59), dividend (DBI-mogelijkheden, RV 30 % maar VVPR-bis 15 % onder voorwaarden). De optimale mix balanceert PB-progressie, 45.000-EUR-regel voor KMO-tarief VenB en RV-niveau op dividenden.

<small>📚 WIB92 — art. 32, 195, 215 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De fiscale wetgever heeft historisch een ongelijkheid willen voorkomen tussen werknemers en bedrijfsleiders. Daarom worden bedrijfsleiders 'gelijkgesteld' aan loontrekkenden voor PB-grondslag (art. 30-2°), maar zonder de loonbescherming + werkgevers-RSZ van werknemers. De 45.000-EUR-regel (art. 215-4°) komt uit de hervorming 2018: ze beoogt een ware bezoldiging boven sluip-dividenden, anders verliest de KMO haar verlaagd VenB-tarief 20 %.

<small>📚 WIB92 — art. 30-2°, 215-4° — _wettekst_</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 30-2°, 32, 195, 215; vanaf AJ 2019

**✅ Voor**
- 🔗 Bij KMO-zaakvoerder/bestuurder die periodiek vergoeding uit eigen vennootschap ontvangt.
- 🔗 Bij aandeelhouder die op de borderline tussen 'bezoldiging' en 'dividend' kiest (mix-optimalisatie).

**📋 Voorwaarden**
- 📖 Toekenning ten laste van het resultaat van het belastbaar tijdperk — boeking op rekening 618 (Bezoldigingen bestuurders, zaakvoerders, beherende vennoten).

## Bouwstenen

### 💡 Wie is 'bedrijfsleider' fiscaal?  
_`begrip`_

📖 Twee categorieën (art. 32 WIB92): (1) natuurlijke persoon met mandaat (bestuurder, zaakvoerder, vereffenaar of gelijksoortige functie); (2) natuurlijke persoon met leidende functie of leidende werkzaamheid van dagelijks bestuur (commercieel, financieel, technisch) buiten een arbeidsovereenkomst. Cat. 2 mag enkel als hij niet onder een arbeidscontract werkt — zo niet, is hij werknemer (art. 30-1°).

<small>📚 WIB92 — art. 32 — _wettekst_</small>

### ⚙️ 4 bouwblokken bezoldigingsmix  
_`mechanisme`_

**Substantie**: 🔗 De zaakvoerder bouwt zijn vergoeding op uit één of meer van vier kanalen:

<small>📚 WIB92 — art. 32, 195 — _wettekst_</small>

### 📏 45.000-EUR-bezoldigingsregel (KMO-tarief)  
_`drempel`_

📖 Een kleine vennootschap verliest het verlaagd VenB-tarief 20 % (op de eerste schijf van € 100.000 winst — art. 215, lid 2 WIB92) wanneer ze, vanaf het vijfde belastbare tijdperk vanaf oprichting, niet aan ten minste één bedrijfsleider (art. 32) een bezoldiging toekent ten laste van het resultaat die gelijk is aan of hoger is dan: ofwel € 45.000, ofwel — indien lager — het belastbaar inkomen van de vennootschap (art. 215, lid 3, 4°).

<small>📚 WIB92 — art. 215, lid 3, 4° — _wettekst_</small>

### ✴️ Bezoldigingstheorie (aftrekbaarheid kosten woning/auto)  
_`principe`_

🔗 De Cassatie-rechtspraak (sinds arrest 12-06-2015) staat toe dat een vennootschap kosten van een onroerend goed (woning, deels of volledig privé bewoond door de zaakvoerder) als beroepskost aftrekt op grond van art. 49 WIB92, mits de uitgave een (kosteloos) voordeel uitmaakt dat in de bezoldigingspolitiek past — d.w.z. de uitgave is een vergoeding voor de prestaties van de bedrijfsleider en wordt als VAA bij hem belast. Dit is een belangrijke uitzondering op de strikte 'maatschappelijk doel'-test: de causaliteitsband wordt afgeleid uit de bezoldigingspolitiek, niet uit een directe link met inkomstenverwerving.

<small>📚 WIB92 — art. 49, 32 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ↪️ Herkwalificatie huur > 5/3 gerevaloriseerd KI  
_`uitzondering`_

📖 Wanneer een bedrijfsleider een gebouwd onroerend goed verhuurt aan zijn vennootschap, wordt de huur boven 5/3 van het gerevaloriseerd KI fiscaal geherkwalificeerd tot bezoldiging (art. 32, lid 2, 3°). Gevolg: op dat overschot wordt bedrijfsvoorheffing ingehouden + sociale bijdragen verschuldigd, en het bedrag wordt in PB belast als beroepsinkomen i.p.v. onroerend inkomen. De kosten in verband met dat onroerend goed worden niet meer in aftrek gebracht op het overschot-deel.

<small>📚 WIB92 — art. 32, lid 2, 3° — _wettekst_</small>

### 📜 Eigen kosten werkgever — bedrijfsleider (art. 32/1)  
_`regel`_

📖 Bepaalde kosten die de vennootschap voor haar bedrijfsleider draagt (representatie, kantoor thuis, parkeren ...) worden niet als bezoldiging belast als ze 'eigen kosten van de vennootschap' vormen — d.w.z. de werknemer/bedrijfsleider doet die uitgaven in opdracht van of in het belang van de vennootschap. Het is een soort omgekeerde VAA: geen belasting bij bedrijfsleider, wel aftrek bij vennootschap. Strakke voorwaarden (art. 32/1).

<small>📚 WIB92 — art. 32/1 — _wettekst_</small>

## Voorbeelden

### 💡 Zaakvoerder BV — bruto-loon € 60.000 in jaar X 🔗

_Eenpersoons-BV. Geen VAA. Bedrijfsvoorheffing aan de bron. Sociale bijdragen via sociaal verzekeringsfonds._

**Berekening:**

**Boeking:**


<small>📚 WIB92 — art. 32, 270 — _wettekst_ · aangifte-PB-2025-bezoldigingen — vak XVI code 1401 — _aangifte_</small>

### 💡 KMO-tarief test — vennootschap met winst € 80.000 + bezoldiging € 30.000 🔗

_Kleine vennootschap (art. 1:24 WVV), 7e boekjaar, één zaakvoerder die € 30.000 bezoldiging trekt. Belastbare winst vóór VenB-tarief = € 80.000._

**Berekening:**

<small>📚 WIB92 — art. 215, lid 3, 4° — _wettekst_ · aangifte-VenB-2025-tarief-voorafbetalingen — code 1754 — _aangifte_</small>

### 💡 Bezoldigingsmix: maandloon € 36.000 + tantième € 24.000 + VAA-auto € 4.000 🔗

_Zaakvoerder kiest mix om over de 45.000-regel te raken én EUR 60.000 totaal te bereiken. Wagen 165 g CO2, cataloguswaarde € 35.000, leeftijd 0 jaar._



**Boeking:**


<small>📚 WIB92 — art. 32, 195, 198 § 1, 9° — _wettekst_</small>

## Valkuilen

### ⚠️ Tantième fiscaal aftrekbaar in jaar van toekenning, niet in jaar van AV-beslissing

**Verkeerde assumptie**: Een tantième die in maart Y+1 op de AV wordt beslist, is fiscaal aftrekbaar in jaar Y+1.

**Kernpunt**: Een tantième die op de gewone AV wordt toegekend uit het resultaat van boekjaar Y, is via art. 195 WIB fiscaal aftrekbaar in boekjaar Y (mits boeking 14→47 vóór goedkeuring jaarrekening), maar bij de bedrijfsleider belastbaar in kalenderjaar Y+1 (datum van toekenning). Cash-flow + timing-effect.

<small>📚 WIB92 — art. 195 — _wettekst_</small>

### ⚠️ 45.000-EUR-regel — VAA telt mee, maar niet alle componenten

**Verkeerde assumptie**: VAA voor woning of auto telt automatisch mee voor de 45.000-EUR-toets.

**Kernpunt**: De drempel kijkt naar 'bezoldiging ten laste van het resultaat van het belastbaar tijdperk' (art. 215). VAA-loon telt mee voor zover het effectief als kost in de vennootschap is geboekt (bv. autokost is kost; woning-VAA is voor het loon-deel kost via rekening 618). Niet-vergoede voordelen (passieve woning eigendom van bedrijfsleider, dividend) tellen NIET mee. Bedrijfsvoorheffing inhouding telt ook niet (komt al uit de bezoldiging).

<small>📚 WIB92 — art. 215 — _wettekst_</small>

## Speelruimtes

### 🎚️ Bezoldiging vs dividend — twee kanalen

## Accountant-perspectieven

### Stagiair die bezoldigingsmix adviseert

_Per cliënt-zaakvoerder maakt de stagiair een jaarlijkse pro forma optimalisatie: 45.000-toets + IPT-ruimte + RV-niveau._

#### 💰 Fiscaal adviseur

##### 👣 Jaarlijks bezoldigingsadvies (najaar)  
_`stap`_

**Substantie**: 🔗 (1) Schat geprojecteerde winst boekjaar. (2) Test 45.000-EUR-regel: voldoende? Indien niet, simuleer minimumloon. (3) Bereken IPT-ruimte (80 %-regel art. 59) — eventuele extra storting tot fiscale grens. (4) Bereken tantième-mogelijkheid (boeken tijdig vóór jaareinde, AV maart Y+1). (5) Documenteer in bezoldigingsmemo aan cliënt: bedragen + cash-flow per kwartaal + risico's controle.

<small>📚 WIB92 — art. 32, 59, 195, 215 — _wettekst_</small>

#### 📒 Boekhouder

##### 👣 Boekingen bezoldiging + BV + sociale bijdragen  
_`stap`_

**Substantie**: 🔗 (1) Maandelijks: 618 D / 4530 BV C + 416 R/C C. (2) Bedrijfsvoorheffing maandelijks afdragen: 4530 D / 5500 C. (3) Sociale bijdragen: 6230 (sociale bijdragen zelfstandige) D / 4540 C, kwartaalbetaling. (4) Tantième: 14 D / 47 C bij AV; 47 D / 4530 + 5500 C bij betaling. (5) IPT-premie: 6230 D / 5500 C (vennootschap-deel, 100 % aftrekbaar binnen 80 %-regel).

<small>📚 MAR (KB 21.10.2018) — rek. 618, 4530, 6230 — _kb_</small>

## Verder lezen (scope-out)

- → Werknemer-loon en payroll-cascade → [[werknemersbezoldiging]] _(moet-verwijzen)_
- → Tantième-details → [[tantieme]] _(moet-verwijzen)_
- → VAA-componenten (woning · auto · lening · ...) → [[voordelen-alle-aard]] _(moet-verwijzen)_
- → Groepsverzekering / IPT als pensioencomponent → [[groepsverzekering-ipt]] _(moet-verwijzen)_
- → KMO-tarief 20% (verlaagd-tarief) → [[verlaagd-tarief-kleine-vennootschap]] _(moet-verwijzen)_
- ↪ Dividend-uitkering als alternatieve route → ⏳ dividend-uitkering _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[beroepsinkomen-pb]]
### `vereist`
- [[verlaagd-tarief-kleine-vennootschap]]
### `bevat`
- [[tantieme]]
- [[voordelen-alle-aard]]
### `triggert`
- [[bedrijfsvoorheffing]]
### `vergelijkbaar_met`
- ⏳ dividend-uitkering
    - **Gelijkenissen**:
        - beide manieren waarop aandeelhouder-zaakvoerder vergoed wordt uit eigen vennootschap
    - **Verschillen**:
        - bezoldiging = aftrekbaar in venn., progressief in PB, sociale bijdragen; dividend = niet aftrekbaar in venn., RV 30 %/15 % VVPR-bis, geen sociale bijdragen
    - ⚠️ **Verwarringsrisico**: Mix-optimalisatie vergt simulatie per cliënt; geen 'best in alle gevallen'.
- [[werknemersbezoldiging]]
    - **Gelijkenissen**:
        - beide vallen onder art. 30 WIB beroepsinkomen
        - beide met bedrijfsvoorheffing
    - **Verschillen**:
        - werknemer: arbeidsovereenkomst + werkgevers-RSZ + werknemers-RSZ; bedrijfsleider: mandaat zonder arbeidsovereenkomst + zelfstandigen-sociale-bijdragen
    - ⚠️ **Verwarringsrisico**: Cumul bezoldiging werknemer + bedrijfsleider mogelijk indien gescheiden functies, anders herkwalificatie risico.
