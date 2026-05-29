---
title: "Aangifte vennootschapsbelasting"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
  - gebeurtenis
ankers:
  - 2.3.III
  - 2.3.IV
  - 2.3.taak.1
  - 2.3.taak.2
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-regeling
  - cat-gebeurtenis
  - status-concept
gegenereerd_uit: "data/concepten/records/aangifte-vennootschapsbelasting.json"
---

_Procedure_ · afk: **Aangifte VenB** · ook: VenB-aangifte · Biztax-aangifte · déclaration ISoc · formulier 275.1

## Definitie

De aangifte vennootschapsbelasting is de jaarlijkse elektronische aangifte (formulier 275.1) die elke binnenlandse vennootschap onderworpen aan de VenB moet indienen bij FOD Financiën binnen ongeveer 7 maanden na afsluiting van het boekjaar. De aangifte vertaalt de boekhoudkundige winst — zoals goedgekeurd door de algemene vergadering in de jaarrekening — via de 8 bewerkingen naar het belastbaar resultaat, waarop het VenB-tarief wordt toegepast. Indiening gebeurt verplicht via het Biztax-platform (TaxOnWeb-zakelijke variant).

<small>📖 WIB92 — art. 305 — _wettekst_ · WIB92 — art. 310 — _wettekst_ · aangifte-VenB-2025-identificatie — Aangifte VenB AJ 2025 — Identificatie + grootte vennootschap — _aangifte_</small>

## Substantie

De aangifte VenB is procedureel complexer dan de PB-aangifte: (a) verplicht elektronisch via Biztax — geen papier-optie (sinds AJ 2015 voor de meeste vennootschappen, volledig vanaf AJ 2018); (b) één formulier (275.1) met 30+ vakken in vaste structuur die de boekhoudkundige + fiscale data integreert; (c) vele verplichte bijlagen — minstens de jaarrekening, eventueel TP-formulieren bij multinationals (vanaf bepaalde omzet/balanstotaal-drempels), DBI-tabel met dochters, CFC-opgave voor gecontroleerde buitenlandse vennootschappen. De aangifte wordt opgesteld door de vennootschap (zaakvoerder/bestuurder verantwoordelijk) — typisch via accountantskantoor met software (Sage BoB, Adsolut, Yuki, ...). Termijn vereist coördinatie met AV-goedkeuring jaarrekening (binnen 6 maanden na boekjaar-einde, art. 3:1 WVV) — zonder goedgekeurde jaarrekening geen aangifte mogelijk.

<small>📖 WIB92 — art. 305 lid 2 — _wettekst_ · aangifte-VenB-2025-bijlagen — Samenvatting bijlagen + diverse bescheiden + verplicht bij te voegen opgaven — _aangifte_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

De aangifte VenB is een dichte interface tussen het Belgisch boekhoudrecht (jaarrekening WVV) en het fiscaal recht (WIB92): ze materialiseert het boekhoud-conformiteit-beginsel (art. 183) door de jaarrekening verplicht als basis te nemen en de fiscale correcties expliciet zichtbaar te maken op het formulier. Vereisten als TP-verklaring en CFC-rapportering integreren internationale anti-belastingontwijking-regels (BEPS-actieplan, ATAD-richtlijn) in de standaard-aangifte. De korte termijn van 7 maanden dwingt de vennootschap haar boekhouding en jaarrekening tijdig af te ronden — een implicit incentive voor governance-kwaliteit.

<small>🔗 WIB92 — art. 183 — _wettekst_ · WIB92 — art. 310 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 305-311 + KB/WIB92 + Wet 25-4-2014 (verplichte elektronische aangifte voor vennootschappen)

Biztax operationeel sinds 2013, verplicht elektronisch sinds AJ 2015. Jaarlijkse uitbreiding met nieuwe rubrieken (CFC sinds AJ 2020, Pijler 2 sinds AJ 2025). Formulier 275.1 wordt jaarlijks bijgewerkt door FOD Financiën conform wetswijzigingen.

**✅ Voor**
- 📖 Elke binnenlandse vennootschap onderworpen aan de VenB (art. 179 WIB92) — BV, NV, CV, VOF, CommV met rechtspersoonlijkheid + winstoogmerk + Belgische zetel. Ook organismen voor financiering van pensioenen (OFP). Voor buitenlandse vennootschappen met Belgische vaste inrichting: aangifte op formulier 275.2 (BNI/vennootschap).

**🚫 Niet voor**
- 🔗 Vennootschappen die niet aan VenB onderworpen zijn (rechtspersonenbelasting RPB — formulier 276.5; belasting niet-inwoners BNI — formulier 275.2 voor vennootschap zonder Belgische zetel maar wel Belgische vaste inrichting). Ook vennootschappen in vereffening na sluiting: laatste 275.1 op datum sluiting, daarna geen aangifte meer.

**📋 Voorwaarden**
- 📖 Vormvereisten: (1) volledig en correct ingevuld 275.1-formulier in Biztax; (2) goedgekeurde jaarrekening AV als bijlage (verplicht — art. 307 WIB92); (3) extra bijlagen indien van toepassing (zie bouwsteen bijlagen); (4) elektronische ondertekening via eID/itsme door bestuurder/zaakvoerder of gemandateerde (accountant met volmacht).

**▶️ Trigger start**
- 🔗 Afsluiting boekjaar triggert de aangifte-procedure. Workflow: (1) boekhouding afsluiten (eindejaarsverrichtingen, voorraadwaardering); (2) jaarrekening opstellen door bestuursorgaan; (3) verslag door commissaris (zo aanwezig); (4) AV goedkeuring (binnen 6 maanden); (5) neerlegging jaarrekening NBB (binnen 1 maand na AV); (6) aangifte VenB opstellen op basis goedgekeurde jaarrekening; (7) elektronische indiening Biztax binnen 7 maanden na boekjaar-einde.

**⏹ Trigger einde**
- 📖 Indiening van de aangifte (bevestiging Biztax) sluit de aangifte-fase af. De fiscus vestigt vervolgens de aanslag (typisch binnen enkele maanden — uiterlijk 30 juni van het jaar volgend op het AJ, art. 359 WIB92), met eventueel een controle-fase tussen.

**⚠️ Risico**
- 📖 Laattijdige aangifte: ambtshalve aanslag (art. 351) op basis van geschatte winst, belastingverhoging 10-200 % (art. 444). Bovendien: belastingvermeerdering bij onvoldoende voorafbetalingen blijft van toepassing. Niet-indiening: zelfde sancties + onmogelijkheid om vorige verliezen of investeringsaftrek voor dit AJ te claimen (verloren — niet overdraagbaar zonder aangifte).
- 🔗 TP-verklaring vergeten bij multinationals: vanaf bepaalde drempels (omzet > 50 M, balanstotaal > 25 M, personeel > 100) zijn vennootschappen verplicht een TP-Local File (form 275 LF), TP-Master File (form 275 MF) en Country-by-Country Report (CbCR — form 275 CbCR) in te dienen. Niet-naleving: administratieve boetes 1.250-25.000 EUR per ontbrekend document (art. 445/1 WIB92).

## Bouwstenen

### 📜 Biztax-platform

Biztax (biztax.fgov.be) is het verplichte elektronisch platform voor de aangifte vennootschapsbelasting (en BNI/vennootschap). Toegang via eID/itsme van bestuurder/zaakvoerder, of via mandataris-volmacht (boekhoudkantoor). Vennootschap-software (Sage, Adsolut, Yuki, Octopus, ...) kan rechtstreeks via XML-feed in Biztax invoeren ('via een derde partij'-flow). Papier-aangifte is niet meer toegestaan voor vennootschappen sinds AJ 2018, behoudens uitzonderlijke gevallen (overmacht — fiscus geeft expliciete toelating). Biztax bevat ingebouwde controles (cross-validatie cijfers, plausibiliteit), genereert een PDF-bevestiging + uniek depotnummer dat als bewijs van tijdige indiening dient.

<small>📖 WIB92 — art. 305 lid 2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Formulier 275.1 — VenB-aangifte

**Substantie**: Het formulier 275.1 bestaat uit vakken die conceptueel de cascade VenB-berekening volgen: (A) Identificatie + grootte vennootschap (KBO-nummer, naam, adres, rechtsvorm, kleine-vennootschap-toets art. 1:24 WVV: omzet/balanstotaal/personeel); (B) Reserves (mutatie belaste + vrijgestelde reserves — code 1080 PN); (C) Verworpen uitgaven (categorieën autokosten, restaurant, geldboetes, geschenken — codes 1209 e.v.); (D) Uiteenzetting van de winst (Belgisch resterend / verdrag-vrijgesteld / niet-vrijgesteld — opdeling); (E) Aftrekken in vaste volgorde (codes 1432-1445 — zie tabel onder belastbare-grondslag-vennootschapsbelasting); (F) Tarief-toepassing (25 % / 20 % KMO); (G) Bijzondere aanslagen (geheime commissielonen art. 219); (H) Voorheffingen + voorafbetalingen-aanrekening (codes 1820 e.v.). Bijkomende rubrieken voor: gecontroleerde buitenlandse vennootschappen (CFC), groepsbijdrage-overeenkomsten, hybride mismatches.

<small>📖 aangifte-VenB-2025-identificatie — Sleutelcodes vak Identificatie + grootte (1871 verbondenheid, 1872 VTE, ...) — _aangifte_ · aangifte-VenB-2025-uiteenzetting-winst — Tabel aftrekken in volgorde codes 1432-1445 — _aangifte_ · aangifte-VenB-2025-oeso-cfc-groepsbijdrage — Vakken CFC + groepsbijdrage — _aangifte_</small>

### 📜 Termijn: ~7 maanden na boekjaar-einde

Indienings-termijn (art. 310 WIB92): uiterlijk de laatste dag van de zevende maand na het tijdstip waarop het boekjaar werd afgesloten — voor zover deze zevende maand niet eerder verstrijkt dan de laatste dag van september (vroeger boekjaar = niet voor september). Praktijk: vennootschap met boekjaar = kalenderjaar → afsluiting 31 december → AV uiterlijk 30 juni → aangifte uiterlijk 30 september (of einde van de 7de maand). Vennootschap met gebroken boekjaar 1-7 → 30-6: aangifte uiterlijk eind januari volgend jaar. Bij wettelijke uitzonderingen (overmacht, COVID-19 uitstel-regelingen): expliciete verlenging door FOD Financiën via communicatie + KB.

<small>📖 WIB92 — art. 310 — _wettekst_</small>

### 📜 Verplichte bijlagen + opgaven

Bij elke aangifte 275.1 verplicht te voegen: (1) goedgekeurde jaarrekening (boekhoudkundige winst); (2) bij toepassing van DBI-aftrek: tabel dochters met deelnemingspercentage + houdperiode (DBI-opgave); (3) bij investeringsaftrek: investeringsaftrek-tabel met type investering + percentage; (4) bij vrijgestelde reserves: opgave gespreid taxeerbare meerwaarden; (5) bij multinationals (omzet > 50 M of balanstotaal > 25 M of personeel > 100): TP-Local File (275 LF), Master File (275 MF — moederholding), Country-by-Country Report (275 CbCR — vanaf 750 M geconsolideerde omzet); (6) bij gecontroleerde buitenlandse vennootschap (art. 185/2): CFC-opgave; (7) bij groepsbijdrage-overeenkomst: opgave dochter/zustermaatschappij + bedrag. Voor erkende accountants: opgave 'erkend ITAA-mandataris' (kwaliteitslabel).

<small>📖 aangifte-VenB-2025-bijlagen — Samenvatting — Bijlagen en formulieren — _aangifte_ · aangifte-VenB-2025-bijlagen — Diverse bescheiden + verplicht bij te voegen opgaven — _aangifte_ · aangifte-VenB-2025-oeso-cfc-groepsbijdrage — CFC-opgave + groepsbijdrage — _aangifte_</small>

### 👣 Coördinatie AV-goedkeuring jaarrekening

De aangifte VenB kan pas worden ingediend wanneer de jaarrekening door de AV is goedgekeurd. Volgens art. 3:1 WVV moet de AV binnen 6 maanden na afsluiting boekjaar plaatsvinden. Realistische timing: (1) maand 1-3 na boekjaar = afsluitende boekhouding + jaarrekening opstellen door bestuursorgaan; (2) maand 4 = verslag commissaris (zo aanwezig); (3) maand 4-6 = AV-bijeenroeping + goedkeuring; (4) maand 7 = aangifte VenB. Te krap = risico op laattijdige aangifte; te ruim = aangifte kan al worden ingediend in maand 6 indien AV vroeg goedkeurde. Indien AV laattijdig (bv. door corona-uitstel of geschil): aangifte kan ambtshalve worden vermeden via uitstel-aanvraag bij FOD.

<small>📖 WVV — art. 3:1 — _wettekst_ · WIB92 — art. 310 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ↪️ Formulier 275.2 — BNI/vennootschap

Voor buitenlandse vennootschappen (geen Belgische zetel) met Belgische vaste inrichting of Belgische bron-inkomsten: aangifte via formulier 275.2 (Belasting niet-inwoners — vennootschap, art. 227 2° + 233 WIB92). Conceptueel vergelijkbaar met 275.1 maar beperkter — enkel de Belgische bron-inkomsten worden aangegeven; verrekening met thuisland via DBV.

<small>📖 WIB92 — art. 227 2° — _wettekst_ · WIB92 — art. 233 — _wettekst_</small>

## Voorbeelden

> [!example]- BV met boekjaar = kalenderjaar — workflow AJ 2026
> _BV ConsultingPro, kleine vennootschap. Boekjaar 1-1-2025 → 31-12-2025 (= AJ 2026). Boekhoudkundige winst 120.000 EUR. Verworpen uitgaven 8.000. DBI ontvangen 5.000. Voorafbetalingen totaal 22.000 EUR. Externe accountant (mandataris) verzorgt aangifte._
>
> - 31-12-2025: boekjaar afgesloten
> - Januari-maart 2026: accountant rondt boekhouding af, eindejaarsverrichtingen (voorraad, vorderingen, provisies)
> - April 2026: jaarrekening opgesteld door zaakvoerder; commissaris-verslag (zo aanwezig)
> - Mei 2026: AV bijeengeroepen, jaarrekening goedgekeurd; resultaatbestemming beslist
> - Juni 2026: jaarrekening neerleggen NBB (binnen 30 dagen na AV — art. 3:10 WVV)
> - Juli-augustus 2026: aangifte VenB opstellen in Biztax — accountant met mandataris-volmacht; 275.1 vakken A-H invullen + DBI-tabel als bijlage
> - September 2026 (uiterlijk 30-9): aangifte indienen via Biztax, bevestiging + depotnummer opslaan
> - Najaar 2026: aanslag wordt gevestigd door FOD; aanslagbiljet komt; verrekening voorafbetalingen 22.000 met VenB ~ 23.000 → saldo bij te betalen ~ 1.000 EUR + eventueel belastingvermeerdering
>
> Cijfer-cascade BV ConsultingPro AJ 2026:
>
> - Boekhoudkundige winst: 120.000
> - + Verworpen uitgaven: 8.000 → 128.000
> - Belgisch resterend: 128.000 (geen verdrag-vrijgesteld)
> - − DBI (100 % aftrek mits voorwaarden): 5.000 → 123.000
> - Geen innovatie- of investeringsaftrek dit jaar → 123.000
> - Belastbare grondslag = 123.000 EUR
> - KMO-toets vervuld (kleine vennootschap + minimumbezoldiging) → 20 % op eerste 100K + 25 % op overschot
> - VenB = (100.000 × 20 %) + (23.000 × 25 %) = 20.000 + 5.750 = 25.750 EUR
> - − Voorafbetalingen 22.000 → saldo bij te betalen 3.750 EUR + check vermeerdering.
>
> <small>🔗 WIB92 — art. 310 — _wettekst_ · aangifte-VenB-2025-uiteenzetting-winst — Uiteenzetting + aftrekken — _aangifte_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- NV met gebroken boekjaar 1-7 → 30-6 — andere termijn
> _NV LogisticsPlus, niet-kleine vennootschap. Boekjaar 1-7-2024 → 30-6-2025. Aanslagjaar = AJ 2025 (jaar waarin boekjaar wordt afgesloten)._
>
> Termijn-flow gebroken boekjaar:
>
> ```mermaid
> flowchart LR
>   A[01-07-2024 Start boekjaar] --> B[30-06-2025 Afsluiting]
>   B --> C[Tot 31-12-2025 AV moet plaatsvinden binnen 6m WVV art 3:1]
>   C --> D[Aangifte VenB uiterlijk 31-01-2026 7 maanden na afsluiting WIB92 art 310]
>   D --> E[Aanslag wordt gevestigd door FOD 2026]
> ```
>
> Kernpunten:
> - Boekjaar-afsluiting bepaalt het AJ → 30-6-2025 → AJ 2025
> - AV-termijn = 6 maanden na boekjaar-einde (uiterlijk 31-12-2025)
> - Aangifte-termijn = 7 maanden na boekjaar-einde (uiterlijk 31-1-2026)
> - Anders dan PB: geen 'aangifte juli' — termijn loopt volledig parallel met boekjaar-cyclus
> - 25 %-tarief van toepassing (NV LogisticsPlus is geen kleine vennootschap)
>
> <small>📖 WIB92 — art. 310 — _wettekst_ · KB/WIB92 — art. 200 — _kb_</small>

> [!example]- Multinational met TP-verplichtingen — Local File + Master File
> _BV BelgiumTech (Belgische dochter van Amerikaanse moeder), omzet 65 M EUR, balanstotaal 80 M, personeel 250. Boekjaar 2024 = AJ 2025. Voert intra-groep transacties uit (royalty's aan Amerikaanse moeder, dienstverlening aan zustermaatschappij in Duitsland)._
>
> | TP-document | Wanneer | Indiening | Boete bij ontbrekend |
>
> | --- | --- | --- | --- |
>
> | 275 LF (Local File) | Drempels overschreden door BelgiumTech zelf (omzet > 50 M of balanstotaal > 25 M of personeel > 100) | Bij aangifte 275.1 als bijlage | 1.250 - 25.000 EUR |
>
> | 275 MF (Master File) | Voor de hoogste Belgische moeder van een groep met geconsolideerde omzet > 50 M (hier: indien BelgiumTech zelf moeder, niet US-moeder) | Binnen 12 maanden na boekjaar-einde | 1.250 - 25.000 EUR |
>
> | 275 CbCR (Country-by-Country Report) | Geconsolideerde groepsomzet > 750 M EUR | Binnen 12 maanden na boekjaar — meestal door US-moeder via US-IRS | 25.000 EUR + per land |
>
> BV BelgiumTech is gehouden tot 275 LF (Local File): documenteert haar intra-groep-transacties — royalty's naar US, services aan DE — met benchmarkstudie ter onderbouwing van arm's-length-prijzen. Bij overschrijding van de drempel zonder Local File: minimumboete 1.250 EUR per ontbrekend document, oplopend tot 25.000 EUR bij herhaling of opzet. Belangrijk voor de accountant: drempels checken op het niveau van de Belgische vennootschap zelf (niet van de groep!) en TP-policy documenteren voorafgaand aan boekjaar-einde.
>
> <small>🔗 WIB92 — art. 321/1-321/7 — _wettekst_ · WIB92 — art. 445/1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- AJ-conventie verwarren bij gebroken boekjaar
> **Verkeerde assumptie**: AJ = kalenderjaar waarin de aangifte wordt ingediend.
>
> **Kernpunt**: AJ = jaar waarin het boekjaar wordt AFGESLOTEN (KB/WIB92 art. 200). Boekjaar 1-7-2024 → 30-6-2025 = AJ 2025 (niet AJ 2026). De aangifte wordt ingediend in 2025-2026 maar betreft AJ 2025. Het AJ-cijfer geeft het jaar van boekjaar-einde aan, niet het jaar van indiening.
>
> <small>📖 KB/WIB92 — art. 200 — _kb_</small>

> [!warning]- Aangifte indienen vóór AV-goedkeuring
> **Verkeerde assumptie**: Wachten op AV is tijdverlies — aangifte kan vroeger ingediend op basis van ontwerp-jaarrekening.
>
> **Kernpunt**: De aangifte VenB is verplicht gebaseerd op de GOEDGEKEURDE jaarrekening (art. 307 WIB92 + boekhoud-conformiteit art. 183). Indiening op basis van ontwerp-jaarrekening die later door AV gewijzigd wordt (bv. resultaatbestemming) creëert discrepantie tussen aangifte en jaarrekening — administratieve fouten. Wel mogelijk: aangifte voorbereiden vóór AV en pas na goedkeuring indienen.
>
> <small>📖 WIB92 — art. 183 — _wettekst_ · WIB92 — art. 307 — _wettekst_</small>

> [!warning]- TP-drempels op groepsniveau interpreteren
> **Verkeerde assumptie**: TP-verklaring is enkel voor multinationals met geconsolideerde omzet > 50 M op groepsniveau.
>
> **Kernpunt**: De drempels voor 275 LF (Local File) gelden op het niveau van de BELGISCHE VENNOOTSCHAP zelf (statutaire cijfers): omzet > 50 M, OF balanstotaal > 25 M, OF personeel > 100 (>= 1 van de 3 drempels). Een kleine Belgische dochter van een grote groep met statutair beperkte cijfers is dus VRIJGESTELD van 275 LF (maar valt mogelijk wel onder Master File via een grotere groepsentiteit). De CbCR-drempel (750 M) is wel groepsgebonden.
>
> <small>📖 WIB92 — art. 321/4 — _wettekst_</small>

> [!warning]- Bijlagen vergeten = aangifte 'volledig'
> **Verkeerde assumptie**: Biztax-bevestiging = aangifte volledig + correct.
>
> **Kernpunt**: Biztax controleert structurele consistentie (cijfers tellen op, codes geldig), maar checkt NIET of alle verplichte bijlagen aanwezig zijn voor de specifieke situatie. Een aangifte zonder DBI-tabel terwijl DBI-aftrek is geclaimd: aangifte is technisch ingediend maar inhoudelijk onvolledig → fiscus zal aanvullende info opvragen, mogelijk DBI-aftrek weigeren. Checklist bijlagen per situatie hanteren.
>
> <small>🔗 aangifte-VenB-2025-bijlagen — Verplicht bij te voegen opgaven — _aangifte_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Eigen kantoor — opstellen + indienen aangifte VenB

_De accountant met mandataris-volmacht die voor cliënt-vennootschappen het 275.1-formulier opstelt in Biztax en indient._

#### 💰 Fiscaal adviseur

##### 👣 Bijlagen-checklist per cliënt

Per cliënt-vennootschap een vaste checklist hanteren: (1) goedgekeurde jaarrekening (PDF AV-notulen); (2) bestemmings-resolutie AV (resultaatbestemming); (3) DBI-tabel met dochters (indien DBI geclaimd); (4) investeringsaftrek-tabel + facturen (indien geclaimd); (5) gespreide meerwaarden-opgave (indien art. 47); (6) TP-LF (indien drempels overschreden); (7) CFC-opgave (indien gecontroleerde buitenlandse dochter); (8) groepsbijdrage-overeenkomst (indien van toepassing). Documenteer in werkpapieren welke bijlagen zijn ingediend + bevestigingsdepotnummer Biztax.

<small>🔗 aangifte-VenB-2025-bijlagen — Verplicht bij te voegen opgaven — _aangifte_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 Cross-check Biztax-output ↔ jaarrekening + boekhouding

Na invullen 275.1 in Biztax (of via XML-feed uit boekhoudsoftware): cross-check de belangrijkste cijfers met de jaarrekening en de boekhouding. (a) Boekhoudkundige winst code 1080 PN = winst-na-belastingen jaarrekening (PB-versie of geconsolideerd). (b) Mutatie reserves = aansluiting met saldo-balansen begin/einde boekjaar. (c) Verworpen uitgaven = optellen van verworpen kost-elementen (autokost, restaurant). (d) DBI-bedrag = som divs ontvangen uit klasse 750x of 751x van betrokken dochters. Discrepanties signaleren EN documenteren — hetzij correctie boekhouding, hetzij correctie aangifte, hetzij doelbewust verschil (bv. fiscale provisie).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🔍 Auditor

##### 📜 Bedrijfsrevisor-perspectief: aansluiting jaarrekening ↔ fiscale aangifte

Voor vennootschappen met commissaris (groot, conform art. 1:24 WVV criterium): de commissaris attesteert de jaarrekening maar NIET de fiscale aangifte. Wel relevant: tijdens audit-werk worden fiscale provisies, latente belastingen en fiscale risico's beoordeeld — ISA 540 (schattingen) + ISA 250 (compliance). De commissaris vraagt expliciet naar de status van fiscale aangiftes (ingediend? tijdig? bezwaar?), om te beoordelen of latente belasting-verplichtingen correct zijn gewaardeerd in de jaarrekening.

<small>🔗 ISA 540 (herzien) — Schattingen + fiscale provisies — _norm_ · ISA 250 (herzien) — Compliance met wet + regelgeving — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Belastbare grondslag VenB (8 bewerkingen — input voor aangifte) → [[belastbare-grondslag-vennootschapsbelasting]] _(moet-verwijzen)_
- → Aanslag-cyclus (generiek proces fiscus vestigt aanslag) → [[aanslag-cyclus]] _(moet-verwijzen)_
- → Algemene fiscale procedure (bezwaar, controle, sancties) → [[fiscale-procedure]] _(moet-verwijzen)_
- ↪ Aangifte personenbelasting (PB-pendant) → [[aangifte-pb]] _(mag-verwijzen)_
- → Vennootschapsbelasting (overkoepelend kader) → [[vennootschapsbelasting]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[vennootschapsbelasting]] — Procedure-record onder Σ-hoofdrecord vennootschapsbelasting.
### `vereist`
- [[belastbare-grondslag-vennootschapsbelasting]] — De aangifte vertaalt de cascade-berekening (8 bewerkingen) van de belastbare grondslag naar de formulier-rubrieken.
- [[jaarrekening]] — Verplichte bijlage; boekhoudkundige winst uit goedgekeurde jaarrekening is startpunt aangifte.
### `triggert`
- [[aanslag-cyclus]] — Ingediende aangifte triggert de aanslag-cyclus van de fiscus (vestiging aanslag binnen termijn art. 359).
### `vergelijkbaar_met`
- [[aangifte-pb]]
    - **Gelijkenissen**:
        - Beide jaarlijkse fiscale aangiften aan FOD Financiën
        - Beide elektronische platforms (Biztax voor VenB, TaxOnWeb voor PB)
        - Beide kennen administratieve sancties bij niet/laattijdige indiening
        - Beide vereisen melding buitenlandse rekeningen + juridische constructies
    - **Verschillen**:
        - VenB-aangifte volgt boekjaar (kan gebroken); PB-aangifte volgt altijd kalenderjaar
        - VenB-aangifte = elektronisch verplicht; PB-aangifte = papier nog mogelijk + VVA-voorstel
        - VenB-termijn = 7 maanden na boekjaar-afsluiting; PB-termijn = juni-juli AJ
        - VenB-aangifte op naam vennootschap (KBO); PB-aangifte op naam natuurlijke persoon (rijksregisternummer)
        - VenB heeft één formulier (275.1) met 30+ vakken; PB heeft formulier met deel 1 + 2 met 16+ vakken
        - VenB vereist jaarrekening + diverse opgaven als bijlage; PB enkel beperkte attesten (pensioensparen, giften)
    - ⚠️ **Verwarringsrisico**: Bij eenpersoons-BV met enige zaakvoerder: stagiair denkt dat één aangifte volstaat — maar er zijn TWEE aangiftes nodig: (1) VenB voor de BV zelf (275.1, einde september AJ), (2) PB voor de zaakvoerder als natuurlijke persoon op zijn bezoldiging + dividend (TaxOnWeb, einde juli AJ). Verschillende termijnen, verschillende platforms, verschillende formulieren.
### `uitgevoerd_door`
- [[gecertificeerd-accountant]] — In praktijk meestal door een erkende accountant met mandataris-volmacht (ITAA-erkend).
