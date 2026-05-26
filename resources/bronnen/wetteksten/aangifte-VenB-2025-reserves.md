---
tags: ["2.3"]
itaa-lex-sectie: ""
wet: "aangifte-VenB-2025-reserves"
bron_rol: "formulier"
status: "beschikbaar"
bijgewerkt: "2025"
bron: "FOD Financiën — modelformulier 275.1 + toelichting"
chunk:
  level: 2
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/handcrafted/aangifte-VenB-2025-reserves.md
      sha256: 581dde181bff61df9ff14645b0616fc27a41fee9dafda93fd8d8f22dbc7d4e9c
      version:
      pages:
  tooling:
    pipeline: manual-import
    pipeline_version: be14c139
    model:
    prompt_version:
  generated_at: '2026-05-21T17:02:25Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-21T17:45:05Z'
    confirmed_by: subagent-qa-batch-aangifte-venb-2025
    rationale: 'Pilot-bron, schrijver: human. Alle codes (1001-1180) verbatim uit voorbereiding-p2-4 geverifieerd. Wetsartikelen art. 184quater, 219quater, 192 § 1, 194quinquies § 1+2, 205/5, 194quater/1 spot-checked tegen toelichting (lijnen 398-2869) en kloppen. Tabel-pipe-syntax volledig, bron-blockquote met PDF-URLs intact, didactische blockquotes (M5) doen geen ongeverifieerde wetsartikelclaims. Geen ETL-artefacten.'
    caveat:
    layer1:
      status: pass
      run_id: 20260521-173837
      run_at: '2026-05-21T17:38:37Z'
      heading_count: 14
      max_section_chars: 7044
      file_size_chars: 23611
      flags: []
    layer2:
      status: trusted
      agent: subagent-qa-batch-aangifte-venb-2025
      run_at: '2026-05-21T17:45:05Z'
      rationale: 'Pilot-bron, schrijver: human. Alle codes (1001-1180) verbatim uit voorbereiding-p2-4 geverifieerd. Wetsartikelen art. 184quater, 219quater, 192 § 1, 194quinquies § 1+2, 205/5, 194quater/1 spot-checked tegen toelichting (lijnen 398-2869) en kloppen. Tabel-pipe-syntax volledig, bron-blockquote met PDF-URLs intact, didactische blockquotes (M5) doen geen ongeverifieerde wetsartikelclaims. Geen ETL-artefacten.'
      concrete_problemen: []
---

# Aangifte VenB aanslagjaar 2025 — codes vak Reserves (Belastbare + Vrijgestelde gereserveerde winst)

> **Bron**: "Aangifte in de vennootschapsbelasting — aanslagjaar 2025" (modelformulier 275.1, blz. 2–4) + "Toelichting bij de aangifte in de vennootschapsbelasting — aanslagjaar 2025" (toelichting bij vak Reserves, blz. 6–15 van de toelichting).
> - Aangifte: <https://financien.belgium.be/sites/default/files/121-aangifte-venb-2025.pdf>
> - Toelichting: <https://financien.belgium.be/sites/default/files/121-aangifte-venb-toelichting-2025.pdf>
>
> Gepubliceerd door FOD Financiën. Geraadpleegd 2026-05-21.
> Codes zijn verbatim overgenomen uit de officiële voorbereiding van de aangifte (blz. 2–4).
>
> **PN** = de code wordt met **+** of **–** ingevuld (positief/negatief). De rubriek bevat een ondertekend bedrag (bv. een negatieve reserve, een overgedragen verlies, een aanpassing in min).
> **Twee kolommen**: voor elke regel vermeldt de aangifte het bedrag *bij het begin* en *op het einde* van het belastbare tijdperk. Sommige aanpassings-rubrieken hebben maar één kolom (zie codes 1051–1073, 1061, 1067, 1070, 1080).

---

## A. Belastbare gereserveerde winst — boekhoudkundige reserves (blz. 2)

> **Algemene voorwaarde**: indien de aangifte op papier wordt ingediend en niet alle reserves in het vak kunnen worden vermeld, een opgave met *toestand bij begin en einde van elk reservecomponent* bijvoegen, alsook een afschrift van alle reserverekeningen waarop in het belastbare tijdperk is gedebiteerd of gecrediteerd.

### Reserves op de balans

| Rubriek | Omschrijving | Code |
|---|---|---|
| 1 | Belastbare reserves in het kapitaal en belastbare uitgiftepremies (+/-) — **ook** de negatieve reserve aangelegd n.a.v. een (gedeeltelijke) terugbetaling van kapitaal of gestort-kapitaal-gelijkgestelde uitgiftepremies (art. 18, eerste lid, 2° en 2°bis, WIB 92) | **1001 PN** |
| 2 | Belastbaar gedeelte van de herwaarderingsmeerwaarden | **1004** |
| 3a | Wettelijke reserve — boekhoudkundig bedrag, **te verminderen** met het op subrekening geboekte deel art. 184quater/541 WIB 92 (dat in code 1012 hoort) | **1005** |
| 3b | Onbeschikbare reserves — idem, excl. liquidatiereserve-component | **1006** |
| 3c | Beschikbare reserves — idem, excl. liquidatiereserve-component | **1007** |
| 4 | Overgedragen winst (verlies) (+/-) | **1008 PN** |
| 5 | **Liquidatiereserve** — reserve bedoeld in art. 184quater of 541 WIB 92 (opgave 275 A). Op de aanleg in het belastbare tijdperk is bovendien de afzonderlijke aanslag art. 219quater WIB 92 verschuldigd (zie vak Afzonderlijke aanslagen) | **1012** |
| 6 | Belastbare voorzieningen | **1009** |
| 7 | Andere in de balans vermelde reserves — **drie vrij in te vullen lijnen** | **1010** |
| 8 | Andere belastbare reserves (+/-) — **drie vrij in te vullen lijnen** | **1011 PN** |

### Onzichtbare reserves (latente belaste reserves — niet op balans)

Onderwaarderingen van activa en overwaarderingen van passiva die niet zichtbaar in de jaarrekening zijn opgenomen, blijven fiscaal als reserves belastbaar.

| Rubriek | Omschrijving | Code |
|---|---|---|
| 9a | Belastbare waardeverminderingen | **1020** |
| 9b | Overdreven afschrijvingen — opgave per categorie activa vereist (aanschaffingswaarde, percentage, mutaties, recuperaties). **Degressieve afschrijving** mag enkel nog op activa verkregen of tot stand gebracht **vóór 01.01.2020** (art. 196 § 3 WIB 92) | **1021** |
| 9c | Andere onderschattingen van activa (voorraden, bestellingen in uitvoering, portefeuillewaarden, niet-afschrijfbare activa) | **1022** |
| 9d | Overschattingen van passiva (schuldenrekeningen die niet ten belope van het ingeschreven bedrag overeenstemmen met werkelijke schulden) | **1023** |
| 9e | Meerwaarden bij overdracht van activa aan een buitenlandse vaste inrichting (art. 185/1 WIB 92) — detail per overgedragen bestanddeel | **1024** |
| 9f | Vooruitbetaalde kosten (art. 195/1 WIB 92) — kosten betaald/gedragen in het belastbare tijdperk maar betrekking hebbend op een toekomstig tijdperk. Zie Circulaire 2018/C/43 van 10.04.2018 | **1025** |

> **Subtotaal blz. 2**: code **1040 PN** = belastbare reserves vóór aanpassing begintoestand. Wordt op blz. 3 overgedragen.

---

## A. Belastbare gereserveerde winst — aanpassing begintoestand (blz. 3)

De aanpassingen werken op het *begin* van het belastbare tijdperk: ze corrigeren de uitgangspositie zodat de variatie van belaste reserves over het tijdperk juist berekend wordt. Vrijstellingen die definitief worden, "verlaten" de vrijgestelde-reserves-categorie via een +-aanpassing hier.

### Aanpassingen in meer (+) — verhoging van het beginbedrag

| Rubriek | Omschrijving | Code |
|---|---|---|
| 11 | **Meerwaarden op aandelen** — art. 192 § 1 al. 1 WIB 92. Vrijstelling slechts voor zover (i) de eventuele inkomsten van de aandelen voor DBI-aftrek in aanmerking komen (taxatievoorwaarde art. 202–203 WIB 92), en (ii) het belastbare bedrag hoger is dan het totaal van vroeger aanvaarde waardeverminderingen verminderd met meerwaarden belast volgens art. 24, eerste lid, 3° WIB 92. Vrijstelling niet van toepassing op handelsportefeuille van kredietinstellingen | **1051** |
| 12 | **Meerwaarden op aandelen — CFC-regeling** (art. 192 § 4 WIB 92): meerwaarden op aandelen van een buitenlandse vennootschap waarvan de winst eerder als niet-uitgekeerde winst belast werd onder art. 185/2 WIB 92 (CFC). Vrijstelling beperkt tot dat eerder belaste winstbedrag, voor zover nog niet uitgekeerd en nog op het passief aanwezig. Zie Circulaire 2024/C/82 van 13.12.2024 | **1068** |
| 13 | **Terugnemingen** van vroegere in verworpen uitgaven opgenomen waardeverminderingen op aandelen — m.b.t. waardeverminderingen die volgens art. 198 § 1, 7° WIB 92 als verworpen uitgave werden belast | **1052** |
| 14a | Definitieve vrijstelling **tax shelter erkende audiovisuele werken** (art. 194ter WIB 92) | **1053** |
| 14b | Definitieve vrijstelling **tax shelter erkende podiumproducties** (art. 194ter + 194ter/1 WIB 92) | **1059** |
| 14c | Definitieve vrijstelling **tax shelter erkende videospellen** (art. 194ter + 194ter/3 WIB 92) | **1066** |
| 15 | Vrijstelling **gewestelijke premies en kapitaal- en interestsubsidies** — tewerkstellings-/beroepsoverstappremies en economische-expansie-subsidies betekend vanaf 01.01.2006 (art. 193bis § 1 WIB 92), én O&O-subsidies vanaf 01.01.2007 (art. 193ter § 1 WIB 92). Kapitaalsubsidies worden hier slechts vrijgesteld in de mate dat ze belastbaar worden op grond van art. 362 WIB 92 (zie code 1124 letter k) | **1054** |
| 16 | Definitieve vrijstelling **winst uit reorganisatieplan of minnelijk akkoord** dat **vóór 08.01.2024** is gehomologeerd/vastgesteld — art. 48/1 WIB 92 zoals het bestond vóór wijziging door art. 49 W 28.12.2023. Definitief zodra het plan/akkoord volledig is uitgevoerd; bewijs van publicatie in BS + uitvoering bijvoegen (art. 27/1 § 1 KB/WIB 92) | **1055** |
| 17 | Definitieve vrijstelling **innovatie-inkomsten** — art. 194quinquies § 2 WIB 92. Vrijstelling wordt definitief in het belastbare tijdperk waarin het IP-recht (art. 205/1 § 2, 1°, a–d WIB 92) is verleend. Opgave 275 INNO | **1058** |
| 18 | Vrijstelling ten belope van het overgedragen, **niet-aftrekbaar financieringskostensurplus** (EBITDA-regel) — art. 194sexies WIB 92. Beperkt tot het positieve verschil tussen het grensbedrag (art. 198/1 § 3) en het financieringskostensurplus (art. 198/1 § 2). Opgave 275 SE. Circulaire 2023/C/8 van 12.01.2023 | **1064** |
| 19a | **Vergoeding groepsbijdrage** verkregen — art. 194septies 1° + art. 205/5 § 3, vierde lid WIB 92. Vrijstelling van de vergoeding die de toetredende vennootschap ontvangt in ruil voor opname van de groepsbijdrage in haar winst. Circulaire 2020/C/29 van 13.02.2020 | **1062** |
| 19b | **Vergoeding interestaftrek-overeenkomst** verkregen — art. 194septies 2° + art. 198/1 § 4, vijfde lid WIB 92. Vergoeding van een groepsvennootschap in ruil voor overdracht van het grensbedrag financieringskostensurplus. Circulaire 2023/C/8 | **1063** |
| 19c | **Vergoeding voor bijheffing minimumbelasting** (Pijler 2) — art. 194septies 3° WIB 92. Vergoeding van groepsvennootschap voor betaalde bijheffing onder art. 28 en 35 W 19.12.2023 | **1069** |
| 20a | **Verhoogde aftrek afschrijvingen laadstations** voor elektrische wagens — art. 64quater WIB 92. **100%** van afschrijvingen voor investeringen 01.09.2021–31.03.2023; **50%** voor 01.04.2023–31.08.2024. Laadstation moet operationeel én publiek toegankelijk zijn. Circulaire 2021/C/115 | **1065** |
| 20b | **Verhoogde aftrek 80%** voor leveringskosten zelfstandige dagbladhandels (kosten vanaf 01.01.2024) — art. 48 W 12.05.2024. Circulaire 2024/C/69 van 04.11.2024 | **1072** |
| 20c | **Verhoogde aftrek 20%** voor elektronische factureringspakketten (e-invoicing) — art. 64ter, eerste lid, 1° WIB 92. Kosten vanaf 01.01.2024 verbonden aan pakketten voor gestructureerde e-facturatie onder W 06.02.2024 (verplichting e-invoicing) | **1073** |
| 21 | Negatieve correctie **Diamant Stelsel** — voor diamanthandelaars onderworpen aan het forfaitaire stelsel | **1057** |
| 22 | **Andere** in meer — o.a.: opnemingen van gestort kapitaal (uitgez. regelmatige terugbetaling onder WVV); terugbetalingen van vroeger niet-aftrekbare belastingen; gedeelte gerealiseerde meerwaarden op autovoertuigen volgens art. 24 vierde lid; vervreemding van eigen aandelen >20% (art. 188 derde lid); herziening winst art. 185 § 2 b); terugnames waardeverminderingen na overgang van rechtspersonenbelasting (art. 184quinquies); energiecrisis-vergoedingen onder W 30.10.2022 | **1056** |

### Aanpassingen in min (–) — verlaging van het beginbedrag

| Rubriek | Omschrijving | Code |
|---|---|---|
| 23 | **Groepsbijdrage** (verleende kant) — art. 205/5 + art. 185 § 4 eerste lid WIB 92. Opname van de overgedragen groepsbijdrage in de belastbare grondslag. Circulaire 2020/C/29 | **1067** |
| 24 | **Andere** in min — inzonderheid opnemingen bij overlijden, uittreding of uitsluiting van vennoten van personenvennootschappen die vóór 01.01.1990 hebben plaatsgevonden (zie ook vak Bijzondere aanslagen ≪ vóór 01.01.1990 ≫). Voor verrichtingen vanaf 01.01.1990: rubriek c van vak Uitgekeerde dividenden | **1061** |

### Eindsommen vak A

| Subtotaal | Omschrijving | Code |
|---|---|---|
| Belastbare reserves na aanpassing begintoestand (+/-) | Som van 1040 PN + aanpassingen in meer/min | **1070 PN** |
| **Belastbare gereserveerde winst (+/-)** | Eindbedrag dat doorvloeit naar de uiteenzetting van de winst | **1080 PN** |

---

## B. Vrijgestelde gereserveerde winst (blz. 4)

> **Onaantastbaarheidsvoorwaarde** (algemene voorwaarde voor de vrijstellingen hieronder): de vrijgestelde reserve moet op één of meer afzonderlijke rekeningen van het passief geboekt zijn en blijven, en mag niet tot grondslag dienen voor de berekening van de jaarlijkse dotatie aan de wettelijke reserve of van enige beloning of toekenning. Bij niet-naleving wordt het vroeger vrijgestelde bedrag belastbaar in het tijdperk van niet-naleving. (Uitzondering: art. 45 en 46 § 1 al. 1 2° WIB 92 indien niet uitgedrukt overeenkomstig KB/WVV.)

### Voorzieningen + waardeverminderingen

| Rubriek | Omschrijving | Code |
|---|---|---|
| 1 | **Waardeverminderingen op handelsvorderingen** (art. 22–27 KB/WIB 92, staat 204.3) + waardeverminderingen op vorderingen op medecontractanten met gehomologeerd reorganisatieplan/minnelijk akkoord (art. XX.38, XX.65, XX.79, XX.83/15, XX.83/30, XX.83/35 WER) | **1101** |
| 2 | **Voorzieningen voor risico's en kosten** (art. 194 WIB 92 + art. 22–27 KB/WIB 92, staat 204.3) — alleen vrijgesteld indien voortvloeiend uit verbintenissen aangegaan tijdens het belastbare tijdperk of voorgaande tijdperken, of uit wettelijke/reglementaire verplichtingen (geen louter boekhoudkundige). Circulaire 2018/C/118 van 26.10.2018 | **1102** |

### Verwezenlijkte + niet-verwezenlijkte meerwaarden

| Rubriek | Omschrijving | Code |
|---|---|---|
| 3 | **Uitgedrukte maar niet-verwezenlijkte meerwaarden** op andere goederen dan voorraden en bestellingen in uitvoering (art. 44 § 1, 1° WIB 92) + vrijgestelde herwaarderingsmeerwaarden art. 184quinquies eerste lid 3° + herschattingsmeerwaarden art. 511 § 2 | **1103** |
| 4a | **Gespreid te belasten meerwaarden op bepaalde effecten** (art. 513 WIB 92) — meerwaarden verwezenlijkt **uiterlijk in een belastbaar tijdperk dat aanvangt vóór 01.01.2020**, mits herbelegging. Belastbaar in 6 gelijke jaarlijkse delen vanaf jaar van realisatie. Opgave 275 K | **1111** |
| 4b | **Gespreid te belasten meerwaarden op materiële en immateriële vaste activa** (art. 47 WIB 92) — bij schadegeval/onteigening/vervreemding ≥ 5 jaar oude activa, mits herbelegging in vormen + termijnen van art. 47. Belastbaar naar verhouding van afschrijvingen op herbeleggingsgoederen. Opgave 276 K | **1112** |
| 4c | **Andere verwezenlijkte meerwaarden** (niet-gespreid) — o.a. monetair gedeelte; vrijgestelde meerwaarden op aandelen art. 45 § 1 al. 1 WIB 92 bij fusie/splitsing/inbreng; meerwaarden bij omvorming gemeenschappelijke beleggingsfondsen art. 45 § 2; vóór 01.01.1990 vastgestelde meerwaarden | **1113** |
| 4d | **Meerwaarden op bedrijfsvoertuigen** (art. 44bis WIB 92) — vrijgesteld mits herbelegging. Opgave 276 N | **1114** |
| 4e | **Meerwaarden op binnenschepen** (art. 44ter WIB 92) — vrijgesteld mits herbelegging in voor commerciële vaart bestemde binnenschepen. Opgave 276 P | **1115** |
| 4f | **Meerwaarden op zeeschepen** (W 02.08.2002 art. 115 § 2 + art. 122) — voor vennootschappen die uitsluitend in scheepvaart-activiteiten zoals omschreven in art. 115 § 2 actief zijn, mits herbelegging. Opgave 275 B | **1116** |

### Specifieke vrijgestelde reserves

| Rubriek | Omschrijving | Code |
|---|---|---|
| 5 | **Investeringsreserve** (art. 194quater WIB 92) — KMO-instrument, niet als winst aangemerkt | **1121** |
| 6 | **Wederopbouwreserve** (art. 194quater/1 WIB 92) — aangelegd bij einde van een belastbaar tijdperk verbonden aan aj. 2022, 2023 of 2024; COVID-19-maatregel ter herstel van eigen vermogen, vrijgesteld mits behoud werkgelegenheid. Opgave 275 RR. Circulaire 2022/C/6 van 18.01.2022 | **1129** |
| 7a | **Tax shelter — erkende audiovisuele werken** (art. 194ter §§ 2–4 WIB 92) — voorlopig vrijgestelde winst bij ondertekening raamovereenkomst | **1122** |
| 7b | **Tax shelter — erkende podiumproducties** (art. 194ter §§ 2–4 + 194ter/1 WIB 92) | **1125** |
| 7c | **Tax shelter — erkende videospellen** (art. 194ter §§ 2–4 + 194ter/3 WIB 92) | **1130** |
| 8 | **Reserve voor innovatie-inkomsten** (art. 194quinquies § 1 WIB 92) — voorlopig vrijgestelde winst m.b.t. nog-niet-verleende IP-rechten (art. 205/1 § 2, 1°, a–d WIB 92). Opgave 275 INNO | **1126** |
| 9 | **Vrijgestelde winst inschakelingsbedrijf** (art. 193quater WIB 92) — winst gehouden in vermogen van erkend inschakelingsbedrijf. Circulaire 2018/C/89 van 17.07.2018 | **1127** |
| 10a | **Winst uit reorganisatieplan / minnelijk akkoord** gehomologeerd/vastgesteld **vóór 08.01.2024** (art. 48/1 WIB 92, oude regeling). Voorwaarde: vonnis gepubliceerd in BS in het belastbare tijdperk. Vrijstelling behouden via art. 27/1 § 2 KB/WIB 92 zolang plan loopt; documenten bij aangifte voegen (art. 27/1 § 3 KB/WIB 92) | **1123** |
| 10b | **Winst uit reorganisatieplan / minnelijk akkoord** gehomologeerd/vastgesteld **vanaf 08.01.2024** (art. 48/1 WIB 92, nieuwe regeling). **Verschil met oude regeling**: de tijdelijk vrijgestelde winst wordt opgenomen in de belastbare grondslag van het **3de t/m 6de** belastbare tijdperk volgend op de volledige tenuitvoerlegging/intrekking, ten belope van **één vierde** per tijdperk. Bij herleving van een kwijtgescholden schuld: integraal restant belastbaar in dat tijdperk | **1131** |
| 11 | **Andere vrijgestelde bestanddelen** — o.a. (a) reconversievennootschap art. 58 W 31.07.1984; (b) innovatievennootschap art. 69 § 1 1° W 31.07.1984; (c) inschakelingsbedrijf art. 67 W 26.03.1999 (oude regeling, vóór art. 193quater); (d) sociaal passief (historisch); (e) investeringsreserve aj. 1982 (art. 511 § 1); (f) fiscaal toegelaten afschrijvingen boven aanschaffingswaarde; (g–j) 20%-gedeelten verhoogde aftrek voor gemeenschappelijk vervoer / beveiliging KMO / fietsen / 0g-CO2-voertuigen (art. 190bis + 194octies WIB 92); (k) kapitaalsubsidies art. 362 + vrijgestelde subsidies art. 184quinquies; (l) vrijgestelde bestanddelen art. 184ter § 1; (m) technische voorzieningen verzekeringsondernemingen art. 731–734 KB/WIB 92 | **1124** |

### Eindsommen vak B

| Subtotaal | Omschrijving | Code |
|---|---|---|
| **Vrijgestelde gereserveerde winst** | Eindbedrag van alle vrijgestelde reservecomponenten | **1140** |
| In het kapitaal en de uitgiftepremies geïncorporeerd gedeelte van de vrijgestelde reserves | Het deel van 1140 dat naar kapitaal/uitgiftepremies is overgeboekt | **1180** |

---

## Didactische opmerkingen

> **Hoe leest het vak Reserves samen met de uiteenzetting van de winst?**
> 1. Vak A (Belastbare gereserveerde winst) levert code **1080 PN** = mutatie belaste reserves. Die mutatie is het *vertrekpunt* van de fiscale winstbepaling: ze meet de aangroei van belaste reserves over het tijdperk (boekhoudkundig + onzichtbare reserves), gecorrigeerd voor begintoestand-aanpassingen.
> 2. Vak B (Vrijgestelde gereserveerde winst) levert code **1140**. Hier bouwt de vennootschap reserves op die *fiscaal vrij* blijven zolang de onaantastbaarheidsvoorwaarde wordt nageleefd.
> 3. Vak C "Verworpen uitgaven" (blz. 5–6) telt erbij wat de vennootschap als kost geboekt heeft maar niet fiscaal aftrekbaar is.
> 4. De som van die drie componenten = belastbare basis, vóór dividenden en aftrekken.

> **Liquidatiereserve (code 1012) — werkingsmechanisme**:
> 1. Aanleg uit boekhoudkundige winst na belasting (art. 184quater WIB 92).
> 2. Bij aanleg: jaarlijkse **afzonderlijke aanslag 10%** (art. 219quater WIB 92) — staat in vak Afzonderlijke aanslagen.
> 3. Bij uitkering aan natuurlijke personen binnen 5 jaar: bijkomende roerende voorheffing (RV) bovenop de 10%.
> 4. Bij uitkering na 5 jaar: lagere bijkomende RV.
> 5. Bij vereffening: vrij van bijkomende RV (volle korf benut).
> Bij KMO's vaak gebruikt als alternatief voor onmiddellijke uitkering tegen 30% RV.

> **Onderscheid tax shelter — voorlopige (vak B) vs. definitieve (vak A)**:
> - Code **1122 / 1125 / 1130** = *voorlopige* vrijstelling bij ondertekening raamovereenkomst (de reserve verschijnt op de balans als vrijgesteld).
> - Code **1053 / 1059 / 1066** = *definitieve* vrijstelling zodra het audiovisueel werk / podiumproductie / videospel erkend en gerealiseerd is. De reserve verschuift uit "voorlopig" naar "definitief" via een +-aanpassing van de begintoestand op blz. 3.
> Als de productie niet binnen de termijn aan de voorwaarden voldoet, wordt de voorlopige vrijstelling teruggenomen via verworpen uitgaven.

> **Innovatie-aftrek (codes 1058 + 1126)**:
> - Code **1126** (vak B) = *voorlopige* reserve voor innovatie-inkomsten, op grond van art. 194quinquies § 1 WIB 92.
> - Code **1058** (vak A, aanpassing in meer) = *definitieve* vrijstelling zodra het IP-recht (octrooi, kwekersrecht, weesgeneesmiddel, software) volgens art. 205/1 § 2, 1°, a–d WIB 92 is verleend.
> - De aftrek zelf (85% van het netto-innovatie-inkomen) gebeurt elders in de aangifte (vak Uiteenzetting van de winst).
> Opgave 275 INNO is verplicht in beide gevallen.

> **Reorganisatieplan / minnelijk akkoord — cesuur 08.01.2024 (codes 1123 vs. 1131)**:
> - Vóór 08.01.2024 gehomologeerd: **art. 48/1 WIB 92 oude regeling** — winst uit waardeverminderingen op passief blijft vrijgesteld zolang plan loopt, definitief bij volledige uitvoering (code 1055 voor de overgang).
> - Vanaf 08.01.2024: **art. 48/1 nieuwe regeling** — winst is *tijdelijk* vrijgesteld; wordt verplicht **teruggenomen in de belastbare grondslag van het 3de t/m 6de tijdperk** na volledige uitvoering, in vier gelijke schijven van één vierde. Bij herleving van een kwijtgescholden schuld: integraal restant belastbaar.
> Achtergrond: deze fiscale faciliteit ondersteunt ondernemingen in reorganisatie onder Boek XX WER (art. XX.38 vaststelling minnelijk akkoord; art. XX.79 homologatie reorganisatieplan; XX.83/15, XX.83/30, XX.83/35 voor besloten reorganisatieprocedures).

> **Groepsbijdrage (codes 1062 ↔ 1067)** — *fiscale consolidatie light* sinds aj. 2020:
> - Code **1067** (in min): vennootschap die de **groepsbijdrage verleent** ziet haar belastbare reserves verlagen — de overgedragen winst wordt bij haar belastbaar via art. 185 § 4 al. 1.
> - Code **1062** (in meer): vennootschap die de **vergoeding** in ruil voor de groepsbijdrage ontvangt, ziet die vergoeding vrijgesteld (art. 194septies 1° WIB 92).
> Voorwaarden: enkel tussen direct verbonden binnenlandse vennootschappen of Belgische inrichtingen, na 5 jaar aaneensluitende verbinding, formele groepsbijdrageovereenkomst (art. 205/5 WIB 92). Circulaire 2020/C/29 van 13.02.2020.

> **Onzichtbare reserves vs. boekhoudkundige reserves**:
> - **Boekhoudkundige reserves** (codes 1001–1011) staan op de balans (wettelijke / beschikbare / overgedragen winst / etc.).
> - **Onzichtbare reserves** (codes 1020–1025) zijn fiscaal als reserves erkend maar **niet zichtbaar** in de jaarrekening. Voorbeelden:
>   - Een overdreven afschrijving (1021): boekhoudkundig afgeschreven kost > fiscaal toegelaten kost → het verschil is een verborgen reserve.
>   - Een overschatting van een passief (1023): een schuld die op de balans staat tegen meer dan haar werkelijke waarde verbergt een reserve.
>   - Vooruitbetaalde kosten (1025): kosten die boekhoudkundig in dit tijdperk vallen maar fiscaal pas in een latere periode aftrekbaar zijn (art. 195/1 WIB 92, Circulaire 2018/C/43).
> Examen-onderscheid: een **stille reserve** in de financiële verslaggeving (latente meerwaarde op vastgoed) is iets anders dan een **onzichtbare reserve** in fiscale zin (verborgen onderwaardering activa / overwaardering passiva).

---

## Samenvatting — Sleutelcodes vak Reserves

| Concept | Subsectie | Primaire code | Omschrijving |
|---|---|---|---|
| Eindsom belastbare gereserveerde winst | A | **1080 PN** | Variatie belaste reserves over het tijdperk (na aanpassingen) |
| Wettelijke reserve op balans | A | **1005** | Boekhoudkundige reserve excl. liquidatiereserve-component |
| Liquidatiereserve aangelegd | A | **1012** | Reserve art. 184quater/541 — jaarlijkse 10% in afzonderlijke aanslag |
| Onzichtbare reserves — overdreven afschrijvingen | A | **1021** | Latente belaste reserve (degressief enkel pre-01.01.2020) |
| Meerwaarden op aandelen vrijgesteld | A | **1051** | Art. 192 § 1 — taxatievoorwaarde art. 202–203 |
| Groepsbijdrage verkregen (vergoeding) | A | **1062** | Art. 194septies 1° |
| Groepsbijdrage verleend | A | **1067** | Art. 205/5 — opname in belastbare grondslag |
| Innovatie-aftrek definitief | A | **1058** | Art. 194quinquies § 2 — opgave 275 INNO |
| Eindsom vrijgestelde gereserveerde winst | B | **1140** | Eindbedrag vrijgestelde reservecomponenten |
| Investeringsreserve KMO | B | **1121** | Art. 194quater |
| Wederopbouwreserve COVID-19 | B | **1129** | Art. 194quater/1 — opgave 275 RR |
| Tax shelter voorlopig — audiovisueel | B | **1122** | Wordt definitief via code 1053 |
| Reserve voor innovatie-inkomsten voorlopig | B | **1126** | Wordt definitief via code 1058 |
| Reorganisatieplan vóór 08.01.2024 | B | **1123** | Oude regeling — definitief bij uitvoering |
| Reorganisatieplan vanaf 08.01.2024 | B | **1131** | Nieuwe regeling — terugname in vier vierden |
