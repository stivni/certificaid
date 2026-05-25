---
tags: ["2.3"]
itaa-lex-sectie: ""
wet: "aangifte-VenB-2025-verworpen-uitgaven"
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
    - id: resources/raw/handcrafted/aangifte-VenB-2025-verworpen-uitgaven.md
      sha256: 67fce21d8fad7ec6ee391ca3a2132eaba9329b23eeced5116e049a05686ca533
      version:
      pages:
  tooling:
    pipeline: manual-import
    pipeline_version: be14c139
    model:
    prompt_version:
  generated_at: '2026-05-21T17:11:18Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-21T17:45:05Z'
    confirmed_by: subagent-qa-batch-aangifte-venb-2025
    rationale: Alle 50 codes (1201-1264) verbatim uit voorbereiding-p5-6 geverifieerd. Wetsartikelen art. 66 § 1, 198/1, 185/2, 53 24° gevonden in toelichting (lijnen 1292-1764). Tabel-pipe-syntax overal correct, sectie-organisatie A-H logisch. Didactische blockquotes zijn correcte interpretatie van toelichting-tekst, geen training-knowledge.
    caveat:
    layer1:
      status: pass
      run_id: 20260521-173837
      run_at: '2026-05-21T17:38:37Z'
      heading_count: 54
      max_section_chars: 10913
      file_size_chars: 42818
      flags: []
    layer2:
      status: trusted
      agent: subagent-qa-batch-aangifte-venb-2025
      run_at: '2026-05-21T17:45:05Z'
      rationale: Alle 50 codes (1201-1264) verbatim uit voorbereiding-p5-6 geverifieerd. Wetsartikelen art. 66 § 1, 198/1, 185/2, 53 24° gevonden in toelichting (lijnen 1292-1764). Tabel-pipe-syntax overal correct, sectie-organisatie A-H logisch. Didactische blockquotes zijn correcte interpretatie van toelichting-tekst, geen training-knowledge.
      concrete_problemen: []
---

# Aangifte VenB aanslagjaar 2025 — codes vak Verworpen uitgaven en overige bestanddelen van het resultaat

> **Bron**: "Aangifte in de vennootschapsbelasting — aanslagjaar 2025" (modelformulier 275.1, blz. 5–6) + "Toelichting bij de aangifte in de vennootschapsbelasting — aanslagjaar 2025" (vak Verworpen uitgaven, blz. 15–25 van de toelichting).
> - Aangifte: <https://financien.belgium.be/sites/default/files/121-aangifte-venb-2025.pdf>
> - Toelichting: <https://financien.belgium.be/sites/default/files/121-aangifte-venb-toelichting-2025.pdf>
>
> Gepubliceerd door FOD Financiën. Geraadpleegd 2026-05-21.
> Codes zijn verbatim overgenomen uit de officiële voorbereiding van de aangifte (blz. 5–6).
>
> **Functie van dit vak**: Verworpen uitgaven (VU) zijn boekhoudkundige kosten die fiscaal niet aftrekbaar zijn. Ze worden bij de belastbare basis gevoegd ("overige bestanddelen van het resultaat"). De eindsom **code 1240** komt naast de mutatie belaste reserves (code 1080 PN) en de uitgekeerde dividenden in de uiteenzetting van de winst terecht.
>
> **Algemene rechtvaardigingsplicht**: bij de aangifte horen drie lijsten:
> 1. een lijst van de bedrijfs-, financiële en uitzonderlijke kosten volgens hun aard, met de eraan verbonden bezoldigingen per categorie;
> 2. een opgave van toegekende of betaalbaar gestelde roerende inkomsten (aard, bedrag, datum, aanslagvoet, roerende voorheffing) — de toekenning verplicht tot aangifte 273/273 A/273 S, ook indien geen RV verschuldigd is (art. 312 WIB 92 jo. art. 85 KB/WIB 92, zie ook regel 1322);
> 3. een opgave van gehuurde onroerende goederen (ligging, aard, eigenaar, huurbedrag 2024).

---

## A. Niet-aftrekbare belastingen, taksen en boeten

### Niet-aftrekbare belastingen — code 1201

| Rubriek | Omschrijving | Code |
|---|---|---|
| 1 | **Niet-aftrekbare belastingen** — vennootschapsbelasting (incl. afzonderlijke aanslagen art. 219, 219bis, 219quater, 219quinquies WIB 92), voorafbetalingen op de VenB, als ontlasting van verkrijgers gedragen roerende voorheffing op door de vennootschap betaalde/toegekende roerende inkomsten, verhogingen/vermeerderingen/kosten/nalatigheidsinteresten op niet-aftrekbare belastingen, het op niet-aftrekbare belastingen betrekking hebbende gedeelte van de "geraamde belastingschulden", werkelijke en fictieve roerende voorheffing en het forfaitaire gedeelte van de buitenlandse belasting (op niet-dividend roerende inkomsten) | **1201** |

> **Geraamd bedrag van belastingschulden — bijzondere regel**: indien dit bedrag op willekeurige wijze is bepaald en in een belangrijke mate de in te kohieren belasting overtreft, moet het gedeelte dat de verschuldigde belasting te boven gaat onder de **belastbare reserves** worden opgenomen. Alleen de werkelijk verschuldigde belasting wordt als niet-aftrekbare uitgave aangemerkt.
>
> **Vermindering met terugbetalingen**: het bedrag van de niet-aftrekbare belastingen wordt verminderd met (i) terugbetalingen tijdens het belastbare tijdperk van belastingen die vroeger niet als beroepskosten zijn aangenomen en (ii) regulariseringen van geraamde belastingschulden die voorheen als VU zijn belast (zie ook het zeventiende streepje, litt. b, van de rubriek "Aanpassingen in meer van de begintoestand van de reserves" — vak Reserves).

### Gewestelijke belastingen, heffingen en retributies — code 1202

| Rubriek | Omschrijving | Code |
|---|---|---|
| 2 | **Gewestelijke belastingen, heffingen en retributies** — andere dan deze bedoeld in art. 3 BW 16.01.1989 (financiering Gemeenschappen en Gewesten) en andere dan deze ingevoerd door de Gewesten op het gebruik van voertuigen of de openbare weg; samen met de verhogingen, vermeerderingen, kosten en nalatigheidsinteresten daarop (art. 198 § 1, 5° WIB 92). Tevens belasting op spelen/weddenschappen en op automatische ontspanningstoestellen (art. 53, 32° WIB 92) | **1202** |

### Geldboeten, verbeurdverklaringen en straffen — code 1203

| Rubriek | Omschrijving | Code |
|---|---|---|
| 3 | **Geldboeten, verbeurdverklaringen en straffen van alle aard** — incl. transactionele en administratieve geldboeten (ook indien niet-strafrechtelijk en zelfs indien berekend op een aftrekbare belasting), verhogingen van sociale bijdragen, fiscale of sociale regularisatieheffingen, en geldsommen art. 216bis Sv. Ook indien de boete is opgelopen door een persoon die van de vennootschap art. 30 WIB 92-bezoldigingen ontvangt (art. 53, 6° WIB 92) | **1203** |

### Jaarlijkse taksen financiële sector — code 1245

| Rubriek | Omschrijving | Code |
|---|---|---|
| 4 | **Jaarlijkse taksen op kredietinstellingen, collectieve beleggingsinstellingen en verzekeringsondernemingen** — 80% van de drie taksen (art. 20111, 20121, 20130 WDRT). **Vanaf 01.01.2024 zijn deze taksen volledig niet-aftrekbaar** (art. 198 § 1, 6°/1, 6°/2, 6°/3 WIB 92) | **1245** |

### Taks inscheping luchtvaartuig — code 1246

| Rubriek | Omschrijving | Code |
|---|---|---|
| 5 | **Taks op de inscheping van een luchtvaartuig** (art. 160 WDRT) en toekenningen aan derden ter vergoeding van die taks (art. 53, 30° en 31° WIB 92). Aftrekbaar als de taks uitdrukkelijk en afzonderlijk aan derden wordt doorgerekend op de factuur (art. 53/1 WIB 92) | **1246** |

---

## B. Personeels- en bedrijfsleidersgerelateerde verworpen uitgaven

### Niet-aftrekbare pensioenen, kapitalen, werkgeversbijdragen en -premies — code 1204

| Rubriek | Omschrijving | Code |
|---|---|---|
| 6 | **Niet-aftrekbare pensioenen, kapitalen, werkgeversbijdragen en -premies** — inzonderheid: werkgeversbijdragen/-premies art. 38 § 1 al. 1 20° WIB 92 (collectieve of individuele toezeggingen art. 38 § 2); werkgeversbijdragen art. 52, 3°, b WIB 92 voor individuele aanvullende pensioentoezeggingen (W 28.04.2003) **boven 2.970 euro/jaar** (geïndexeerd) voor art. 30, 1° WIB 92-verkrijgers; door werkgever rechtstreeks aan personeelsleden uitgekeerde kapitalen tot herstel van bestendige inkomstenderving bij arbeidsongeschiktheid; bijdragen/premies die niet voldoen aan art. 59 en 195 WIB 92; pensioenen/renten/toelagen die niet voldoen aan art. 60 WIB 92 | **1204** |

> **Inlichtingenplicht**: art. 59 § 1 al. 1 5° en art. 60, 3° WIB 92 vereisen dat de inlichtingen gevraagd bij toepassing van het KB 25.04.2007 (uitvoering art. 306 programmawet (I) van 27.12.2006) zijn verstrekt. Ontbreekt dat, dan zijn de bijdragen/premies niet aftrekbaar.

### Niet-aftrekbare autokosten en minderwaarden — code 1205

| Rubriek | Omschrijving | Code |
|---|---|---|
| 7 | **Niet-aftrekbare autokosten en minderwaarden op autovoertuigen** — het niet-aftrekbare gedeelte van autokosten (incl. brandstof) en het niet-aftrekbare gedeelte van verwezenlijkte minderwaarden op autovoertuigen (art. 66 § 1 en art. 198bis WIB 92) | **1205** |

> **Aftrekformule autokosten (art. 66 § 1 WIB 92 + art. 198bis WIB 92)**:
> 1. **60 %** indien CO2-uitstoot ≥ 200 gr/km of indien geen CO2-gegevens beschikbaar bij DIV.
> 2. In alle andere gevallen: **100 % − [120 % − (0,5 % × coëfficiënt × gr CO2/km)]**, met coëfficiënt 1 voor diesel, 0,95 voor andere brandstoffen en 0,90 voor aardgas < 12 fiscale PK. Resultaat **maximaal 50 %**.
>
> **Valse hybrides (art. 36 § 2 tiende lid WIB 92)**: oplaadbare hybride met batterij < 0,5 kWh/100 kg wagengewicht of CO2-uitstoot > 50 gr/km → CO2-gehalte = dat van het overeenstemmend voertuig met dezelfde brandstof (art. 19 KB/WIB 92). Bestaat geen overeenstemmend voertuig, dan wordt de uitstootwaarde × 2,5. De lijst valse hybrides staat op de FOD Financiën-website. **Niet van toepassing** op hybrides aangekocht vóór 01.01.2018.
>
> **Plug-in hybride brandstofkosten — vanaf 01.01.2023**: voor benzine-/dieselkosten van een vanaf 01.01.2023 aangekocht/geleased/gehuurd oplaadbaar hybridevoertuig is het percentage **minstens 50 %**.
>
> **Niet-aftrekbare minderwaarden (art. 66 § 1 vijfde lid WIB 92)**: tarief = 100 − [(som fiscaal aanvaarde afschrijvingen, per BT beperkt tot 100 %) / (som geboekte afschrijvingen voor dezelfde BT)] × 100.

### Autokosten ten belope van een gedeelte van het voordeel van alle aard — code 1206

| Rubriek | Omschrijving | Code |
|---|---|---|
| 8 | **Autokosten ten belope van een gedeelte van het voordeel van alle aard** — voor voertuigen die (al dan niet kosteloos) voor persoonlijk gebruik ter beschikking zijn gesteld: **40 %** van het VAA (vóór bijdrage van de verkrijger) indien brandstofkosten geheel of gedeeltelijk door de vennootschap ten laste worden genomen; **17 %** indien geen brandstofkosten ten laste van de vennootschap (art. 198 § 1, 9° en 9°bis WIB 92) | **1206** |

### Niet-aftrekbare receptiekosten en kosten voor relatiegeschenken — code 1207

| Rubriek | Omschrijving | Code |
|---|---|---|
| 9 | **Niet-aftrekbare receptiekosten en kosten voor relatiegeschenken** — **50 %** van receptiekosten, kosten voor relatiegeschenken en toekenningen aan derden ter vergoeding daarvan (art. 53, 8° en 11° WIB 92). Aftrekbaar bij uitdrukkelijke en afzonderlijke doorrekening op de factuur (art. 53/1 WIB 92) | **1207** |

### Niet-aftrekbare restaurantkosten — code 1208

| Rubriek | Omschrijving | Code |
|---|---|---|
| 10 | **Niet-aftrekbare restaurantkosten** — **31 %** van restaurantkosten en toekenningen aan derden ter vergoeding daarvan (art. 53, 8°bis en 11° WIB 92). Aftrekbaar bij uitdrukkelijke en afzonderlijke doorrekening op de factuur (art. 53/1 WIB 92) | **1208** |

### Kosten voor niet-specifieke beroepskledij — code 1209

| Rubriek | Omschrijving | Code |
|---|---|---|
| 11 | **Kosten voor niet-specifieke beroepskledij** en toekenningen aan derden ter vergoeding daarvan (art. 53, 7° en 11° WIB 92). Aftrekbaar bij uitdrukkelijke en afzonderlijke doorrekening op de factuur (art. 53/1 WIB 92) | **1209** |

### Sociale voordelen — code 1214

| Rubriek | Omschrijving | Code |
|---|---|---|
| 12 | **Sociale voordelen** als vermeld in art. 38 § 1 al. 1 11° WIB 92, toegekend aan werknemers of bedrijfsleiders (of gewezen werknemers/bedrijfsleiders of hun rechtverkrijgenden) | **1214** |

### Voordelen uit maaltijd-, sport-, cultuur- of ecocheques — code 1215

| Rubriek | Omschrijving | Code |
|---|---|---|
| 13 | **Voordelen uit maaltijd-, sport-, cultuur- of ecocheques** (art. 38 § 1 al. 1 25° WIB 92), met uitzondering van de tot **2 euro per elektronische maaltijdcheque** beperkte werkgeverstussenkomst die voldoet aan art. 38/1 WIB 92 | **1215** |

---

## C. Financierings- en kapitaalgerelateerde verworpen uitgaven

### Overdreven interesten — code 1210

| Rubriek | Omschrijving | Code |
|---|---|---|
| 14 | **Overdreven interesten** van obligaties, leningen, schulden, deposito's en andere effecten ter vertegenwoordiging van leningen, die niet als dividenden moeten worden aangemerkt, in de mate bepaald in **art. 55 WIB 92** | **1210** |

### Interesten met betrekking tot een gedeelte van bepaalde leningen — code 1211

| Rubriek | Omschrijving | Code |
|---|---|---|
| 15 | **Interesten m.b.t. een gedeelte van bepaalde leningen** — onverminderd art. 54 en 55 WIB 92: (a) interesten betaald aan een werkelijke verkrijger die niet aan inkomstenbelasting onderworpen is of aan een aanzienlijk gunstigere aanslagregeling dan het Belgisch gemeen recht (art. 198 § 1, 11° WIB 92); (b) interesten op art. 198/1 § 2 al. 2 eerste streepje WIB 92-leningen waarvan de werkelijke verkrijger tot dezelfde groep behoort (art. 198 § 1, 11°/1 WIB 92). Beide alleen voor zover het totaal van die leningen (uitgez. obligaties openbaar beroep spaarwezen en leningen art. 56 § 2 2° WIB 92) **hoger is dan 5 × (belaste reserves bij begin BT + gestort kapitaal bij einde BT)**. Specifieke regels: art. 198 § 3 al. 3–5 en § 4 WIB 92 | **1211** |

> **Doorkijkregel garanties**: bij leningen gewaarborgd door een derde of waarbij een derde aan de schuldeiser de middelen heeft verschaft en geheel/gedeeltelijk de risico's draagt, wordt **die derde geacht de werkelijke verkrijger** te zijn — indien deze constructie als hoofddoel belastingontwijking heeft.

### Niet-aftrekbaar financieringskostensurplus — code 1262

| Rubriek | Omschrijving | Code |
|---|---|---|
| 16 | **Niet-aftrekbaar financieringskostensurplus** (EBITDA-regel) — onverminderd art. 54 en 55 WIB 92: (a) financieringskostensurplus art. 198/1 § 2 WIB 92 boven het grensbedrag art. 198/1 § 3 WIB 92 (grensbedrag verhoogd/verlaagd via interestaftrek-overeenkomst art. 198/1 § 4 indien deel van een groep); (b) het positieve verschil tussen het via een interestaftrek-overeenkomst overgedragen grensbedrag en het eigen grensbedrag art. 198/1 § 3. **Overeenkomst 275 CDI** bij aangifte voegen om de wijziging van het grensbedrag te rechtvaardigen. Circulaire 2023/C/8 van 12.01.2023 | **1262** |

### Abnormale of goedgunstige voordelen — code 1212

| Rubriek | Omschrijving | Code |
|---|---|---|
| 17 | **Abnormale of goedgunstige voordelen** verleend, onverminderd art. 49 en onder voorbehoud van art. 54 WIB 92, **tenzij** die voordelen in aanmerking komen voor het bepalen van de belastbare inkomsten van de verkrijger (art. 26 WIB 92). **Steeds te vermelden** indien verleend aan: (1) een art. 227 WIB 92-belastingplichtige waarmee een band van wederzijdse afhankelijkheid bestaat; (2) een art. 227-belastingplichtige of buitenlandse inrichting die in zijn land niet aan inkomstenbelasting of aan aanzienlijk gunstigere belastingregeling onderworpen is; (3) een art. 227-belastingplichtige met gemeenschappelijke belangen met 1° of 2° | **1212** |

### Liberaliteiten — code 1216

| Rubriek | Omschrijving | Code |
|---|---|---|
| 18 | **Liberaliteiten** — totaal van alle liberaliteiten **incl. de vrijgestelde bedragen** (rubriek "Vrijgestelde giften" — vak Niet-belastbare bestanddelen). Indien identiteit van verkrijgers/aard van betaalde sommen niet verantwoord is (en geen beroepsinkomsten zijn voor de verkrijgers): tevens in vak Afzonderlijke aanslagen (100 %). **Bijhouden**: een lijst met identiteit van de genieters, aard, bedrag en stortingsdatum; belastbare en vrijstelbare liberaliteiten afzonderlijk groeperen | **1216** |

### Waardeverminderingen en minderwaarden op aandelen — code 1217

| Rubriek | Omschrijving | Code |
|---|---|---|
| 19 | **Waardeverminderingen en minderwaarden op aandelen**, **met uitzondering van**: (a) minderwaarden op aandelen geleden n.a.v. de gehele verdeling van het maatschappelijk vermogen tot ten hoogste het verlies aan gestort kapitaal dat door die aandelen wordt vertegenwoordigd — kapitaalverminderingen ter aanzuivering van geleden verliezen of vorming van een reserve tot dekking van een voorzienbaar verlies blijven hier als gestort kapitaal aangemerkt, in afwijking van art. 184 WIB 92 (art. 198 § 1, 7° en § 2 al. 1 en 4 WIB 92); (b) minderwaarden en waardeverminderingen op aandelen behorend tot de **handelsportefeuille** (art. 35ter § 1 al. 2 a KB 23.09.1992 op de jaarrekening kredietinstellingen) | **1217** |

### Niet-aftrekbare in kosten opgenomen disconto's — code 1243

| Rubriek | Omschrijving | Code |
|---|---|---|
| 20 | **Niet-aftrekbare in kosten opgenomen disconto's** op niet-afschrijfbare immateriële of materiële vaste activa of financiële vaste activa, voor zover de aankoopprijs lager is dan de werkelijke waarde verhoogd met het disconto (art. 198 § 1, 8° WIB 92). Circulaire 2019/C/99 van 30.09.2019 | **1243** |

### Huur en huurvoordelen + zakelijk gebruiksrecht — code 1248

| Rubriek | Omschrijving | Code |
|---|---|---|
| 21 | **Huur en toegekende huurvoordelen + vergoedingen/voordelen uit recht van opstal, erfpacht of ander zakelijk gebruiksrecht** wanneer: (a) de aangifte-verplichting art. 307 § 2/2 WIB 92 (**bijlage 270 MLH**) niet is nageleefd, of (b) de huurovereenkomst kosteloos is geregistreerd volgens art. 161, 12° a/b Wb.Reg. (of kosteloos had kunnen worden geregistreerd indien het OG in België lag). Uitzonderingen onder (b): (i) huur uitsluitend voor huisvesting van werknemers/bedrijfsleiders en hun gezin onder wettelijke/contractuele verplichting; (ii) huur door gewestelijke huisvestingsmaatschappij of erkende sociale huisvestingsmaatschappij voor uitsluitend woongebruik | **1248** |

---

## D. Terugnemingen van vroegere vrijstellingen en specifieke regimes

### Terugnemingen van vroegere vrijstellingen — code 1218

| Rubriek | Omschrijving | Code |
|---|---|---|
| 22 | **Terugnemingen van vroegere vrijstellingen** — inzonderheid: (a) vrijstelling aanvullend personeel art. 548 WIB 92 en aanvullend personeel voor wetenschappelijk onderzoek/uitbouw technologisch potentieel art. 524 en 531 WIB 92, geheel of gedeeltelijk terug te nemen; (b) vrijstelling **sociaal passief eenheidsstatuut** art. 67quater WIB 92; (c) eenmalige investeringsaftrek op O&O-investeringen die tot andere doeleinden zijn gebruikt; (d) een zesde per BT (over 5 BT na realisatie) van vroeger op effecten verwezenlijkte niet-monetaire meerwaarden art. 513 WIB 92, beperkt tot de voorheen verleende aftrek; (e) terugbetaalde gewestelijke inkomenscompensatievergoedingen art. 67quinquies WIB 92; (f) groepsbijdrage in mindering gebracht art. 205/5 § 4 WIB 92 die wordt teruggenomen op grond van art. 185 § 4 al. 2 WIB 92 wanneer de buitenlandse activiteit binnen 3 jaar wordt heropgestart (Circulaire 2020/C/29 van 13.02.2020); (g) terugbetaalde COVID-19-vergoedingen art. 6 W 29.05.2020; (h) terugbetaalde energiecrisis-vergoedingen art. 7/1 W 30.10.2022 | **1218** |

### Werknemersparticipatie en winstpremies — code 1233

| Rubriek | Omschrijving | Code |
|---|---|---|
| 23 | **Werknemersparticipatie en winstpremies** — deelnames in het kapitaal of in de winst (incl. winstpremies Hoofdstuk II/1 W 22.05.2001) en deelnames toegekend aan werknemers in een investeringsspaarplan (art. 198 § 1, 12° WIB 92) | **1233** |

### Vergoedingen voor ontbrekende coupon — code 1220

| Rubriek | Omschrijving | Code |
|---|---|---|
| 24 | **Vergoedingen voor ontbrekende coupon** betaald of toegekend in uitvoering van vanaf 01.02.2005 afgesloten zakelijke-zekerheidsovereenkomsten of leningen m.b.t. aandelen, tot een bedrag gelijk aan het verschil tussen het totale brutodividend betaald/toegekend voor de aandelen en het totale brutobedrag als dividend daadwerkelijk verkregen (of waarvoor een vergoeding ontbrekende coupon werd verkregen) (art. 198 § 1, 13° WIB 92) | **1220** |

### Kosten tax shelter — code 1232

| Rubriek | Omschrijving | Code |
|---|---|---|
| 25 | **Kosten tax shelter** — kosten, verliezen, waardeverminderingen, voorzieningen en afschrijvingen in verband met de vrijstelling art. 194ter § 2, 194ter/1 en 194ter/3 WIB 92 | **1232** |

### Gewestelijke premies en kapitaal- en interestsubsidies — code 1222

| Rubriek | Omschrijving | Code |
|---|---|---|
| 26 | **Gewestelijke premies en kapitaal- en interestsubsidies** — (a) deel van de art. 193bis § 1 al. 2 en 193ter § 1 WIB 92-premies en -subsidies dat voorheen definitief werd vrijgesteld en wordt terugbetaald aan het Gewest (art. 198 § 1, 14° WIB 92); (b) bij vrijwillige vervreemding van de art. 193bis § 1 al. 2 en 193ter § 1 vaste activa **gedurende de eerste 3 jaar** van de investering, wordt de voorheen vrijgestelde winst belastbaar in het tijdperk van vervreemding (art. 193bis § 2 en 193ter § 2 WIB 92) | **1222** |

### Vergoedingen interestaftrek-overeenkomst — code 1263

| Rubriek | Omschrijving | Code |
|---|---|---|
| 27 | **Vergoedingen betaald in uitvoering van een interestaftrek-overeenkomst** — art. 198/1 § 4 vijfde lid WIB 92 (art. 198 § 1, 15° WIB 92). Circulaire 2023/C/8 van 12.01.2023 | **1263** |

### Vergoedingen groepsbijdrage-overeenkomst — code 1264

| Rubriek | Omschrijving | Code |
|---|---|---|
| 28 | **Vergoedingen betaald in uitvoering van een groepsbijdrage-overeenkomst** — art. 205/5 § 3 vierde lid en art. 205/5 § 4 vijfde lid WIB 92 (art. 198 § 1, 16° WIB 92). Circulaire 2020/C/29 van 13.02.2020 | **1264** |

### Minimumbelasting MNO/binnenlandse groepen — code 1249

| Rubriek | Omschrijving | Code |
|---|---|---|
| 29 | **Minimumbelasting voor groepen van multinationale ondernemingen en omvangrijke binnenlandse groepen** (Pijler 2) — minimumbelasting art. 2 § 2 W 19.12.2023, daarop in mindering gestorte sommen, alsook verhogingen/vermeerderingen/kosten/nalatigheidsinteresten en voorheffingen (art. 198 § 1, 18° WIB 92) | **1249** |

### Vergoeding voor bijheffing minimumbelasting — code 1250

| Rubriek | Omschrijving | Code |
|---|---|---|
| 30 | **Bedrag betaald als vergoeding voor een bijheffing in het kader van de minimumbelasting** voor MNO-groepen en omvangrijke binnenlandse groepen — vergoeding art. 194septies derde streepje WIB 92 ter compensatie van de belasting art. 28 en 35 W 19.12.2023 die wordt betaald door een binnenlandse vennootschap of Belgische inrichting (art. 198 § 1, 19° WIB 92) | **1250** |

### Niet-aftrekbare commissies sportmakelaars — code 1244

| Rubriek | Omschrijving | Code |
|---|---|---|
| 31 | **Niet-aftrekbare commissies en andere vergoedingen aan sportmakelaars** — commissies, makelaarslonen, restorno's, vacatiegelden, erelonen, gratificaties, vergoedingen of voordelen van alle aard **boven 3 % van de totale brutobezoldiging** van de sportbeoefenaar (per jaar, gedurende duur arbeidsovereenkomst), rechtstreeks of onrechtstreeks betaald in het kader van een overeenkomst tot: bijstand van een sportbeoefenaar bij contractonderhandelingen; bijstand van een schuldenaar van de bedrijfsvoorheffing (art. 270, 1° of 3° WIB 92) bij contractonderhandelingen met een sportbeoefenaar; regeling van een uitleenbeurt of definitieve transfer van een sportbeoefenaar (art. 198 § 1, 17° WIB 92) | **1244** |

---

## E. Internationale en anti-misbruik-rubrieken

### Niet-aftrekbare betalingen naar bepaalde Staten — code 1223

| Rubriek | Omschrijving | Code |
|---|---|---|
| 32 | **Niet-aftrekbare betalingen naar bepaalde Staten** — onverminderd art. 219 WIB 92: betalingen rechtstreeks of onrechtstreeks verricht naar in art. 307 § 1/2 al. 1 WIB 92 bedoelde Staten die niet zijn aangegeven, of wel aangegeven maar waarvan de belastingplichtige niet door alle rechtsmiddelen bewijst dat ze in het kader van **werkelijke en oprechte verrichtingen** met **niet-artificiële constructies** zijn verricht (art. 198 § 1, 10° WIB 92). **Aangifte 275 F** vereist zodra het totaal van die betalingen + toename schulden ≥ **100.000 euro** is. Circulaire 2021/C/112 van 20.12.2021 | **1223** |

> **Welke Staten**: Staten die op het tijdstip van de betaling (a) door het Mondiaal Forum inzake transparantie en uitwisseling van inlichtingen aangemerkt worden als niet effectief/substantieel de uitwisselings-standaard toepassend; (b) op de lijst van Staten zonder of met lage belasting voorkomen; of (c) op de EU-lijst van niet-coöperatieve rechtsgebieden staan.
>
> **Diamant Stelsel-uitzondering**: betalingen onder het Diamant Stelsel worden hier **niet** vermeld; ze gaan naar regel **1229** ("Correctie in functie van het minimumbedrag van het netto belastbaar inkomen uit de diamanthandel").

### Niet-aftrekbare betalingen hybridemismatches — code 1236

| Rubriek | Omschrijving | Code |
|---|---|---|
| 33 | **Niet-aftrekbare betalingen gedaan in het kader van bepaalde hybridemismatches** (art. 198 § 1, 10°/1 tot 10°/4 WIB 92). Circulaire 2024/C/66 van 22.10.2024 | **1236** |

### Niet-verantwoorde kosten en verdoken meerwinsten — code 1225

| Rubriek | Omschrijving | Code |
|---|---|---|
| 34 | **Niet-verantwoorde kosten en verdoken meerwinsten** die volgens art. 219 WIB 92 aan de afzonderlijke aanslag worden onderworpen (art. 197 WIB 92) | **1225** |

> **Voorrang andere rubrieken**: niet-verantwoorde kosten die volgens een specifieke wetsbepaling al onder een andere VU-rubriek vallen, worden onder díe rubriek aangegeven, niet onder 1225.

### Terugneming aftrek innovatie-inkomsten (spreiding historische kosten) — code 1230

| Rubriek | Omschrijving | Code |
|---|---|---|
| 35 | **Terugneming van aftrek voor innovatie-inkomsten in geval van spreiding van de historische kosten** — wanneer voor lineaire spreiding van globale uitgaven art. 205/1 § 2, 5° WIB 92 ("historische kosten" m.b.t. een IP-recht) is geopteerd en (i) de spreidingstermijn vervalt in dit BT, **of** (ii) vóór het vervallen wordt de aftrek voor innovatie-inkomsten m.b.t. dat IP-recht niet langer toegepast: de winst wordt verhoogd met het positieve verschil tussen de werkelijk verleende/overgedragen aftrek voor dit BT en hoogstens 6 voorgaande BT, en de aftrek die toegepast zou zijn zonder spreidingsmethode (art. 205/2 § 2 vierde lid WIB 92) | **1230** |

### Terugneming aftrek innovatie-inkomsten (niet-herbelegging) — code 1231

| Rubriek | Omschrijving | Code |
|---|---|---|
| 36 | **Terugneming van aftrek voor innovatie-inkomsten ingevolge niet-herbelegging in kwalificerende uitgaven** — vrijgestelde winst bij vervreemding van een art. 205/1 § 2, 2° vijfde streepje WIB 92-IP-recht wordt **volledig** teruggenomen wanneer de bij vervreemding verkregen vergoedingen **niet binnen 5 jaar** (vanaf eerste dag kalenderjaar van vervreemding, en uiterlijk bij stopzetting beroepswerkzaamheid) zijn besteed aan kwalificerende uitgaven betreffende een of meer andere art. 205/1 § 2, 1° IP-rechten (art. 205/4 § 5 WIB 92) | **1231** |

### Hybridemismatch-inkomsten niet opgenomen in winst — code 1237

| Rubriek | Omschrijving | Code |
|---|---|---|
| 37 | **Inkomsten die verwezenlijkt werden in het kader van een hybridemismatch en niet opgenomen zijn in de winst** — inkomsten verwezenlijkt in het kader van een hybridemismatch en niet opgenomen in de winst van de vennootschap die er gerechtigde voor is (of als zodanig wordt beschouwd onder de wetgeving van een andere Staat), voor zover een buitenlandse onderneming/vestiging die inkomsten van haar belastbare inkomsten mag aftrekken (art. 185 § 2/1 WIB 92). Circulaire 2024/C/66 van 22.10.2024 | **1237** |

### Niet-uitgekeerde winst CFC — code 1238

| Rubriek | Omschrijving | Code |
|---|---|---|
| 38 | **Niet-uitgekeerde winst van een gecontroleerde buitenlandse vennootschap (CFC)** — niet-uitgekeerde winst van een buitenlandse vennootschap of haar buitenlandse inrichting die als CFC wordt aangemerkt, voor zover die winst niet is vrijgesteld volgens art. 185/2 § 4 WIB 92, en werd behaald in een belastbaar tijdperk afgesloten in het BT van de belastingplichtige (art. 185/2 WIB 92). Circulaire 2024/C/82 van 13.12.2024 | **1238** |

> **CFC-kwalificatie (art. 185/2 § 3 WIB 92)** vereist participatie- én taxatievoorwaarde. **Participatievoorwaarde**: de belastingplichtige bezit zelf minstens 1 aandeel in de buitenlandse vennootschap. Voor de berekening van de deelnemingsverhouding wordt **de volledige deelneming** van een in art. 185/2 § 3 vijfde lid WIB 92 bedoelde geassocieerde entiteit in de laag belaste vennootschap in aanmerking genomen.
>
> Voorbeeld uit de toelichting: vennootschap A (BE) heeft 10 % in B (laag belast) en 40 % in C; C heeft 42 % in B. A en C zijn geassocieerde entiteiten. Voor de participatievoorwaarde van A wordt de volledige 42 %-deelneming van C in B meegenomen → A voldoet aan de participatievoorwaarde voor de CFC-kwalificatie van B.

---

## F. Positieve correcties Diamant Stelsel

> Het Diamant Stelsel (art. 67–70 W 10.08.2015) is een forfaitair stelsel voor geregistreerde diamanthandelaars. De vier positieve correcties hieronder worden in het vak VU vermeld; de bijbehorende technische omschrijving staat in het toelichting-deel "Correcties en beperking van bepaalde aftrekken in toepassing van het Diamant Stelsel" (buiten de hier behandelde regels 1099–1866). Voor regel 1229 specifiek geldt: het is het verschil dat opduikt wanneer het netto belastbaar inkomen uit de diamanthandel minder bedraagt dan 0,55 % van de omzet uit de diamanthandel.

| Rubriek | Omschrijving | Code |
|---|---|---|
| 39 | Positief verschil tussen de **forfaitair vastgestelde brutowinst en de boekhoudkundig vastgestelde brutowinst** | **1226** |
| 40 | **Niet-aftrekbare waardeverminderingen op voorraden en niet-aftrekbare kosten** in het Diamant Stelsel | **1227** |
| 41 | Positief verschil tussen de **referentiebezoldiging voor een bedrijfsleider en de hoogste bedrijfsleidersbezoldiging** | **1228** |
| 42 | **Correctie in functie van het minimumbedrag van het netto belastbaar inkomen uit de diamanthandel** (correctie zodra het netto belastbaar inkomen uit de diamanthandel minder bedraagt dan 0,55 % van de omzet uit die handel — ook opvangrubriek voor betalingen naar bepaalde Staten gedaan in het kader van het Diamant Stelsel) | **1229** |

---

## G. Belastingkrediet-rubrieken (kosten boekhoudkundig aftrekbaar, fiscaal verworpen omdat belastingkrediet wordt verleend)

### Verhoging fietskilometervergoeding CAO 164 — code 1251

| Rubriek | Omschrijving | Code |
|---|---|---|
| 43 | **Uitgaven m.b.t. de verhoging van de fietskilometervergoeding in toepassing van CAO nr. 164** voor woon-werkverplaatsingen in de periode **01.05.2023 t.e.m. 31.12.2024** waarvoor de vennootschap de verrekening van een belastingkrediet vraagt (art. 30, 31 en 35 W 28.12.2023). Circulaire 2024/C/46 van 01.07.2024 | **1251** |

### Facultatieve verhoging fietskilometervergoeding — code 1252

| Rubriek | Omschrijving | Code |
|---|---|---|
| 44 | **Uitgaven m.b.t. de facultatieve verhoging van de fietskilometervergoeding voor woon-werkverplaatsingen** in de periode **01.01.2024 t.e.m. 31.12.2026** waarvoor de verrekening van een belastingkrediet wordt gevraagd (art. 17, 18 en 22 W 22.12.2023). Circulaire 2024/C/56 van 05.09.2024 | **1252** |

### Verdeelkostprijzen kranten en tijdschriften — code 1253

| Rubriek | Omschrijving | Code |
|---|---|---|
| 45 | **Verdeelkostprijzen voor de levering van kranten en tijdschriften** gedaan of gedragen vanaf **01.07.2024 t.e.m. 31.12.2026**, werkelijk ten laste van de vennootschap-uitgeefster en waarvoor de verrekening van een belastingkrediet wordt gevraagd (art. 50 en 55 W 12.05.2024). Circulaire 2024/C/69 van 04.11.2024 | **1253** |

### Tussenkomst treinabonnement — code 1254

| Rubriek | Omschrijving | Code |
|---|---|---|
| 46 | **Tussenkomst van de werkgever in een treinabonnement** ten belope van het verleende belastingkrediet, betaald of toegekend in de periode **01.01.2024 t.e.m. 31.12.2027** door een werkgever bedoeld in art. 57 § 1 al. 2 W 12.05.2024 (art. 57 W 12.05.2024) | **1254** |

---

## H. Restcategorie en eindsom

### Andere verworpen uitgaven en overige bestanddelen van het resultaat — code 1239

| Rubriek | Omschrijving | Code |
|---|---|---|
| 47 | **Andere verworpen uitgaven en overige bestanddelen** — inzonderheid: (a) belastbare restorno's in coöperatieve verbruiksverenigingen (art. 189 WIB 92); (b) kosten voor jacht, visvangst, yachten of pleziervaartuigen en lusthuizen, **behalve** indien aangetoond dat ze noodzakelijk zijn uit hoofde van de eigen aard van de beroepswerkzaamheid of in de belastbare bezoldigingen van personeelsleden/bedrijfsleiders begrepen zijn (art. 53, 9° en 11° WIB 92; aftrekbaar bij uitdrukkelijke en afzonderlijke factuurdoorrekening volgens art. 53/1 WIB 92); (c) alle kosten **op onredelijke wijze** de beroepsbehoeften overtreffend (art. 53, 10° en 11° WIB 92); (d) interest, art. 90 al. 1 11° WIB 92-vergoedingen, retributies voor concessie van octrooien/fabricageprocédés/dergelijke rechten of bezoldigingen voor prestaties bedoeld in **art. 54 WIB 92**; (e) jaarlijkse taks op winstdeelnemingen op levensverzekeringscontracten (art. 198 § 1, 4° WIB 92); (f) jaarlijkse taks op effectenrekeningen art. 201/4 WDRT (art. 198 § 1, 6° WIB 92); (g) financiële voordelen of voordelen van alle aard art. 53, 24° WIB 92; (h) compenserende toeslag art. 33bis § 4 W 24.12.1999 die via art. 275/11 WIB 92 wordt afgetrokken van de BV (arbeidsovereenkomsten vanaf 01.07.2018, art. 53, 26° WIB 92); (i) financiële bijdrage art. 5bis § 9 Verord. (EU) nr. 833/2014 (Rusland-sancties) (art. 53, 34° WIB 92) | **1239** |

### Eindsom — code 1240

| Subtotaal | Omschrijving | Code |
|---|---|---|
| **Verworpen uitgaven en overige bestanddelen van het resultaat** | Eindbedrag van alle codes 1201–1239 hierboven. Dit bedrag wordt overgebracht naar de uiteenzetting van de winst | **1240** |

---

## Didactische opmerkingen

> **Hoe leest het vak VU samen met de andere vakken?**
> 1. Vak Reserves levert code **1080 PN** = mutatie belaste reserves (vertrekpunt fiscale winstbepaling).
> 2. Vak VU levert code **1240** = boekhoudkundige kosten die fiscaal niet aftrekbaar zijn, opgeteld bij de fiscale basis.
> 3. Vak Uitgekeerde dividenden levert code **1320**.
> 4. **Som 1080 PN + 1140 (vrijgesteld) + 1240 + 1320 = fiscale resultaat vóór aftrekken** (DBI, innovatie-aftrek, vorige verliezen, e.d.) — uitgewerkt in vak Uiteenzetting van de winst.
>
> Zonder eindsom 1240 zou de fiscale basis enkel uit netto-boekhoudkundige winst + reservebewegingen bestaan — niet-aftrekbare kosten zouden ten onrechte de belastbare grondslag verminderen.

> **Niet-aftrekbare belastingen (1201) — drievoudige scope**:
> 1. **Eigen vennootschapsbelasting** + afzonderlijke aanslagen (art. 219, 219bis, 219quater, 219quinquies WIB 92).
> 2. **Voorafbetalingen** op de VenB en verhogingen/nalatigheidsinteresten op niet-aftrekbare belastingen.
> 3. **Roerende voorheffing** (werkelijk + fictief) en het forfaitaire gedeelte van de buitenlandse belasting op niet-dividend roerende inkomsten — voor zover door de vennootschap als ontlasting van de verkrijger gedragen.
> Tegenpost: terugbetalingen van vroeger-niet-aftrekbare belastingen worden afgetrokken (komen langs een andere weg ook in de begintoestand-aanpassingen van de reserves — zie code 1056 zeventiende streepje litt. b).

> **Autokosten: het samenspel 1205 ↔ 1206**:
> - Code **1205** = het niet-aftrekbare gedeelte van **alle** autokosten en minderwaarden, volgens de CO2-formule (art. 66 § 1 + art. 198bis WIB 92).
> - Code **1206** = de extra, autonome forfaitaire bijtelling bij persoonlijk gebruik: **40 %** van het VAA (brandstofkosten ten laste van vennootschap) of **17 %** (anders) — bovenop wat al onder 1205 is verworpen.
> Voor valse hybrides geldt sinds 01.01.2023 een minimum-niet-aftrekbaarheid van 50 % op benzine-/dieselkosten.

> **Receptie 50 % (1207) vs. restaurant 31 % (1208) vs. kledij 100 % (1209)**:
> - Receptiekosten en relatiegeschenken: 50 % niet-aftrekbaar (art. 53, 8° WIB 92).
> - Restaurantkosten: 31 % niet-aftrekbaar (art. 53, 8°bis WIB 92).
> - Niet-specifieke beroepskledij: integraal niet-aftrekbaar (art. 53, 7° WIB 92).
> Voor alle drie gelden de doorrekenings-uitzonderingen van art. 53/1 WIB 92: aftrekbaar zodra uitdrukkelijk en afzonderlijk op de factuur aan derden doorgerekend.

> **Anti-misbruik trio voor interesten**:
> 1. **Code 1210 — overdreven interesten** (art. 55 WIB 92): rentevoet boven marktrente.
> 2. **Code 1211 — interesten m.b.t. een gedeelte van bepaalde leningen** (art. 198 § 1, 11° en 11°/1 WIB 92): bedrag-test 5 × (belaste reserves + gestort kapitaal) bij leningen naar verkrijgers in gunstigere belastingregimes of intra-groep.
> 3. **Code 1262 — financieringskostensurplus** (EBITDA-regel, art. 198/1 WIB 92): boekhoudkundig netto financieringskostensurplus boven het grensbedrag (30 % EBITDA of 3 mio €).
> Doorkijkregel onder 1211: als een derde een lening waarborgt of de schuldeiser financiert en de risico's draagt, en deze constructie heeft belastingontwijking als hoofddoel, wordt de derde geacht de werkelijke verkrijger te zijn.

> **Drie tax-shelter-codes in dit vak**:
> - **Code 1232** = kosten m.b.t. de tax shelter-vrijstelling (art. 194ter § 2, 194ter/1, 194ter/3 WIB 92). Boekhoudkundig kost; fiscaal verworpen omdat de overeenkomstige vrijstelling al via vak Reserves loopt (codes 1122 / 1125 / 1130 voorlopig; 1053 / 1059 / 1066 definitief).
> Dit is conceptueel het spiegelbeeld van de tax-shelter-reserve: aan de inkomstenkant vrijgesteld, aan de kostenkant verworpen.

> **Hybride mismatches — symmetrie 1236 ↔ 1237**:
> - **Code 1236** = niet-aftrekbare *betalingen* gedaan in het kader van een hybridemismatch (art. 198 § 1, 10°/1 tot 10°/4 WIB 92).
> - **Code 1237** = *inkomsten* die in het kader van een hybridemismatch verwezenlijkt werden en *niet* in de winst van de vennootschap zijn opgenomen, terwijl een buitenlandse onderneming/vestiging ze wel aftrekt (art. 185 § 2/1 WIB 92).
> Beide codes vloeien voort uit ATAD II / Anti-Tax-Avoidance Directive. Circulaire 2024/C/66 van 22.10.2024 behandelt beide.

> **Innovatie-aftrek-terugnemingen 1230 vs. 1231**:
> - **Code 1230** = terugneming wanneer de **spreidingstermijn voor historische kosten** vervalt of de aftrek voortijdig wordt stopgezet — winst wordt verhoogd met het positieve verschil tussen werkelijk verleende aftrek (huidig BT + tot 6 voorgaande BT) en de aftrek die zonder spreidingsmethode zou zijn toegepast (art. 205/2 § 2 vierde lid WIB 92).
> - **Code 1231** = terugneming wanneer bij **vervreemding van een IP-recht** de vergoedingen niet binnen **5 jaar** worden besteed aan kwalificerende uitgaven voor andere IP-rechten (art. 205/4 § 5 WIB 92). Hier wordt de voorheen vrijgestelde winst **volledig** teruggenomen.

> **CFC-regeling (1238) — wanneer is een buitenlandse vennootschap een CFC?**
> Twee voorwaarden moeten cumulatief vervuld zijn (art. 185/2 § 3 WIB 92):
> 1. **Participatievoorwaarde**: de Belgische belastingplichtige bezit zelf minstens 1 aandeel. Voor de berekening van het deelnemingspercentage wordt de **volledige** deelneming van geassocieerde entiteiten meegenomen (niet alleen het pro-rata-deel).
> 2. **Taxatievoorwaarde**: de buitenlandse winst wordt aan een lager tarief belast dan een Belgische referentie.
> Voldoet de buitenlandse vennootschap aan beide, dan wordt haar niet-uitgekeerde winst toegerekend aan de Belgische aandeelhouder via code 1238. Vrijstelling mogelijk onder art. 185/2 § 4 WIB 92 (m.n. substance-test).

> **Belastingkrediet-rubrieken 1251–1254 — fiscale logica**:
> Deze codes voegen aan de belastbare basis kosten toe die boekhoudkundig wél geboekt zijn, maar waarvoor een **belastingkrediet** wordt verleend in de afrekeningsfase. De krediet-rubrieken zelf staan in het vak Verrekenbare voorheffingen en overige verrekenbare bestanddelen. Logica: de fiscale gunst gebeurt via krediet-mechanisme, niet via kostenaftrek — dus wordt de kostenaftrek geneutraliseerd door verwerping. **Cesuur 01.05.2023** (CAO 164, code 1251) versus **01.01.2024** (facultatieve verhoging, code 1252) is belangrijk voor de overgangsperiode tot eind 2024.

> **Niet-verantwoorde kosten (1225) ↔ afzonderlijke aanslag 100 %**: code 1225 voegt het bedrag toe aan de belastbare grondslag (art. 197 WIB 92), maar daarbovenop draagt de vennootschap de **afzonderlijke aanslag art. 219 WIB 92** (zie vak Afzonderlijke aanslagen). Toepasselijk voor niet-verantwoorde kosten, verdoken meerwinsten, voordelen van alle aard en inkomsten uit auteursrechten/naburige rechten waarvan de identiteit van de verkrijger niet binnen de termijn aan de fiscus is meegedeeld. Voorrang-regel: als de niet-aftrekbaarheid uit een andere specifieke bepaling voortvloeit (bv. liberaliteiten in 1216), wordt onder die andere rubriek aangegeven, niet onder 1225.

> **Liberaliteiten (1216) — totaal vermelden, dan corrigeren**:
> De rubriek vereist het totaal van **alle** liberaliteiten — ook de vrijgestelde — omdat de vrijstelling later in het traject volgt via de rubriek "Vrijgestelde giften" (vak Niet-belastbare bestanddelen). De vennootschap moet een lijst bijhouden met identiteit van de genieters, aard, bedrag en stortingsdatum, en de belastbare en vrijstelbare liberaliteiten afzonderlijk groeperen. Indien identiteit van verkrijger niet verantwoord is en het geen beroepsinkomsten zijn voor de verkrijger, valt het bedrag bovendien onder de afzonderlijke aanslag van 100 %.

---

## Samenvatting — Sleutelcodes vak Verworpen uitgaven

| Concept | Subsectie | Primaire code | Omschrijving |
|---|---|---|---|
| **Eindsom verworpen uitgaven** | H | **1240** | Totaalbedrag dat naar uiteenzetting van de winst gaat |
| Niet-aftrekbare belastingen (VenB, RV, ed.) | A | **1201** | Incl. afzonderlijke aanslagen art. 219–219quinquies |
| Geldboeten en straffen | A | **1203** | Art. 53, 6° — ook administratieve boeten |
| Niet-aftrekbare autokosten | B | **1205** | CO2-formule art. 66 § 1 + art. 198bis |
| VAA-autokosten 40 %/17 % | B | **1206** | Bovenop 1205 bij persoonlijk gebruik |
| Receptiekosten 50 % | B | **1207** | Art. 53, 8° |
| Restaurantkosten 31 % | B | **1208** | Art. 53, 8°bis |
| Niet-specifieke beroepskledij | B | **1209** | 100 % verworpen, art. 53, 7° |
| Overdreven interesten | C | **1210** | Art. 55 WIB 92 |
| Interesten 5 × (reserves + kapitaal)-grens | C | **1211** | Art. 198 § 1, 11° en 11°/1 |
| Niet-aftrekbaar financieringskostensurplus | C | **1262** | EBITDA-regel art. 198/1 |
| Abnormale of goedgunstige voordelen | C | **1212** | Art. 26 WIB 92 |
| Liberaliteiten (totaal, ook vrijgesteld) | C | **1216** | Lijst met identiteit verkrijgers vereist |
| Waardeverm. en minderwaarden op aandelen | C | **1217** | Art. 198 § 1, 7° — uitz. handelsportefeuille |
| Terugneming vroegere vrijstellingen | D | **1218** | Sociaal passief, O&O-personeel, groepsbijdrage e.d. |
| Werknemersparticipatie en winstpremies | D | **1233** | Art. 198 § 1, 12° |
| Kosten tax shelter | D | **1232** | Spiegelbeeld vrijstelling 1122/1125/1130 |
| Vergoedingen interestaftrek-overeenkomst | D | **1263** | Spiegelbeeld code 1063 (vak Reserves) |
| Vergoedingen groepsbijdrage-overeenkomst | D | **1264** | Spiegelbeeld code 1062 (vak Reserves) |
| Minimumbelasting Pijler 2 | D | **1249** | W 19.12.2023 |
| Betaling voor bijheffing Pijler 2 | D | **1250** | Spiegelbeeld code 1069 (vak Reserves) |
| Betalingen naar belastingparadijzen | E | **1223** | Aangifte 275 F vanaf 100.000 € |
| Hybridemismatch-betalingen | E | **1236** | ATAD II |
| Niet-verantwoorde kosten / verdoken meerwinsten | E | **1225** | Triggert afzonderlijke aanslag art. 219 |
| Terugneming innovatie-aftrek (spreiding) | E | **1230** | Art. 205/2 § 2 vierde lid |
| Terugneming innovatie-aftrek (niet-herbelegd) | E | **1231** | 5-jaar-herbeleggingstermijn art. 205/4 § 5 |
| Hybridemismatch-inkomsten niet in winst | E | **1237** | Art. 185 § 2/1 |
| Niet-uitgekeerde winst CFC | E | **1238** | Art. 185/2 — Circulaire 2024/C/82 |
| Diamant Stelsel correcties | F | **1226–1229** | Forfaitair stelsel diamanthandelaars (art. 67–70 W 10.08.2015) |
| Belastingkrediet fietskilometervergoeding | G | **1251 / 1252** | CAO 164 + facultatieve verhoging |
| Belastingkrediet kranten/tijdschriften | G | **1253** | Vanaf 01.07.2024 |
| Belastingkrediet treinabonnement | G | **1254** | Tussenkomst werkgever |
| Andere VU (restcategorie) | H | **1239** | Jacht, lusthuizen, onredelijke kosten, effectentaks, Rusland-bijdrage, ed. |
