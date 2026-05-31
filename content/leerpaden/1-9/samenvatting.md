---
title: "Samenvatting PO 1.9 — Financiële analyse en financieel bedrijfsbeheer"
description: "Spickzettel voor cijfer-/diagnose-vak — werkkapitaal-drieluik + ratio-arsenaal + DSCR-recept + Z-score + alarmprocedure-drempels + diagnose-template. Printbaar op 2-3 A4."
explorer_title: "5. Samenvatting"
tags:
  - samenvatting
  - po-1-9
---

<div class="no-print">

> **Samenvatting — spickzettel voor de week vóór het examen.** PO 1.9 is een cijfer- + diagnose-vak op integratie-niveau — deze samenvatting bundelt de formules (annuïteit, DSCR, Z-score, ratio-identiteiten), de drempels (alarmprocedure, Z-banden, DSCR-vuistregels) en de stappenplannen (DSCR-recept, diagnose-template) die je op het examen moet kunnen. Niet bedoeld om voor het eerst te leren — daar zijn de leerstukken voor. Voor verhaal en routekaart: [[leerpaden/1-9|minicursus PO 1.9]]. Voor actief doorrekenen: [[leerpaden/1-9/oefening|oefening Belmonte-diagnose]].

</div>

## 1. Take-away — wat je écht moet weten

- **NBK = BBK + NT** is de functionele identiteit. NBK krimpt + BBK stijgt → NT collapsert → structurele kasovertrek-afhankelijkheid. Verbeteren via vier knoppen: voorraden ↓ · klantenkrediet ↓ · leverancierskrediet ↑ · permanent vermogen ↑.
- **DSCR = cashflow / totale schuldenlast**. Vuistregel bank ≥ 1,20-1,30. Annuïteit $a = K \cdot i / (1 - (1+i)^{-n})$. Matching-principe: looptijd ≤ economische levensduur. Bij DSCR < 1: niet-haalbaar → 4 alternatieven (langere looptijd · eigen inbreng · bullet · staat-gewaarborgde KMO-lening).
- **Z-score = 1,2·X1 + 1,4·X2 + 3,3·X3 + 0,6·X4 + 1,0·X5**. Banden: safe > 2,99 · grey 1,81-2,99 · distress < 1,81. Trend is informatiever dan absoluut getal. Z-score in grey + dalend = signaal voor anticiperende actie, NU.
- **Alarmprocedure-drempel NV (WVV 7:228)**: netto-actief < 1/2 of < 1/4 geplaatst kapitaal. **BV (WVV 5:153)**: netto-actief negatief of niet meer kunnen voldoen aan 12-maands-opeisbare-schulden. CBN 2021/14 voor berekening netto-actief.
- **Diagnose-rapport ≠ ratio-overzicht**. Vijf bouwstenen: data-discipline → consistentie-correctie → 4 analyse-lagen → SWOT financieel → aanbevelingen per stakeholder/horizon. Executive summary op pagina 1 (max 1 pagina, vaste 5-paragrafen-structuur).

---

## 2. Vier analyse-lagen in één blik

Elke diagnose werkt deze vier lagen in deze volgorde. Eerste drie zijn input; vierde is de risico-toets.

| Laag | Wat meet het | Hoofd-instrument(en) | Hoort bij |
|---|---|---|---|
| **1. Functionele balans** | Structureel financierings-evenwicht | NBK · BBK · NT-drieluik | PO 1.3 (techniek) |
| **2. Ratio-families** | Vier dimensies tegelijk | Liquid · Solvab · Rentab · Activit + interpretatie-laag | PO 1.3 (techniek) |
| **3. Kasstromen + FCF** | Cashgeneratie + investerings-capaciteit | KSO indirect IAS 7 · FCFF/FCFE | PO 1.3 (techniek), PO 1.9 (DSCR-beslissing) |
| **4. Continuïteit + predictie** | Risico op insolventie 1-2 jaar | Going-concern + alarmprocedure + Z-score + ISA 570 | PO 1.9 (kern) |

---

## 3. Formule-arsenaal

### Werkkapitaal-drieluik (functionele balans)

**NBK** top-down én bottom-up moet hetzelfde getal geven (controle-toets). **BBK** = wat de exploitatiecyclus structureel vastpint. **NT** = NBK − BBK = financiële marge. NT < 0 = structurele kasovertrek-afhankelijkheid.

$$
\text{NBK}_{\text{top-down}} = \text{Permanent vermogen} - \text{Vaste activa} \qquad \text{NBK}_{\text{bottom-up}} = \text{Vlottende activa} - \text{Schulden} \leq 1\text{j} \qquad \text{NT} = \text{NBK} - \text{BBK}
$$

### Ratio-families (kernformules; vol detail bij PO 1.3)

Vier families × één kernformule. Voor varianten en interpretatie-banden: concept-records [[liquiditeits-ratios]] · [[solvabiliteits-ratios]] · [[rentabiliteits-ratios]] · [[activiteits-ratios]].

$$
\text{Current} = \tfrac{\text{Vlottend}}{\text{KT-schulden}} \quad \text{Solvab} = \tfrac{\text{EV}}{\text{Totaal}} \quad \text{ROE} = \tfrac{\text{Nettores}}{\text{EV}} \quad \text{DSO} = \tfrac{\text{Handelsvord} \times 365}{\text{Omzet incl. btw}}
$$

### Kasstroom (Belgische proxy versus IAS 7)

**Belgische bedrijfscashflow** (CBN 2011/14) = nettoresultaat + niet-kaskosten — proxy, géén werkkapitaal-correctie. **Operationele kasstroom IAS 7 indirect** = proxy ± Δ werkkapitaal. **FCFF** = operationele kasstroom − vervangingsinvesteringen. Voor DSCR-vuistregels: gebruik bedrijfscashflow proxy (snel, conservatief).

$$
\text{Bedrijfscashflow}_{\text{proxy}} = \text{Nettores} + \text{Afschr} + \Delta\text{Voorz} + \Delta\text{WV} \qquad \text{FCFF} = \text{OK}_{\text{IAS 7}} - \text{CapEx vervanging}
$$

### Annuïteit + DSCR (krediet-beoordeling)

**Annuïteit** = jaarlijkse vaste betaling (kapitaal + interest) bij gelijk-annuïteit-krediet. Examen-vuistregels: $1{,}05^{-5} \approx 0{,}78$; $1{,}06^{-5} \approx 0{,}75$; $1{,}06^{-8} \approx 0{,}63$; $1{,}06^{-10} \approx 0{,}56$. **DSCR-vuistregel bank** ≥ 1,20-1,30. **Matching-principe**: looptijd ≤ economische levensduur actief.

$$
a = \frac{K \cdot i}{1 - (1+i)^{-n}} \qquad \text{DSCR} = \frac{\text{Cashflow}}{\text{Bestaande aflossingen} + \text{Annuïteit nieuw}}
$$

### Altman Z-score

Vijf componenten × vaste gewichten. Banden: **safe > 2,99** · **grey 1,81-2,99** (verhoogd risico, monitoren) · **distress < 1,81** (acuut). Trend is informatiever dan absoluut getal. Ohlson O-score is empirisch beter voor private vennootschappen (logit-model met 9 variabelen); kennen op niveau van bestaan en doel.

$$
Z = 1{,}2 \cdot X_1 + 1{,}4 \cdot X_2 + 3{,}3 \cdot X_3 + 0{,}6 \cdot X_4 + 1{,}0 \cdot X_5
$$

---

## 4. Drempels en interpretatie-banden

### Alarmprocedure WVV

| Vennootschapsvorm | Trigger | Wet-ref | Termijn |
|---|---|---|---|
| **NV** (kapitaalhoudend) | Netto-actief < 1/2 of < 1/4 geplaatst kapitaal | WVV 7:228 | AV binnen 2 maanden |
| NV | Netto-actief < 61.500 EUR | WVV 7:229 | Belanghebbende of OM kan ontbinding vorderen |
| **BV** (kapitaalloos) | Netto-actief negatief (of dreigt te worden) | WVV 5:153, 1° | AV binnen 2 maanden |
| BV | Niet meer kunnen voldoen aan opeisbare schulden 12 maanden | WVV 5:153, 2° | Idem |

**Netto-actief** = totaal activa − voorzieningen − schulden − niet-afgeschreven oprichtings/O&O-kosten. Voor de exacte berekenings-methodiek: CBN-advies 2021/14 (twee uitgewerkte voorbeelden).

### Z-score-banden + actie

| Band | Z-waarde | Interpretatie | Actie adviseur |
|---|---|---|---|
| Safe zone | > 2,99 | Stabiel; geen verhoogd risico | Geen ad-hoc actie; jaarlijkse monitoring |
| Grey zone | 1,81 - 2,99 | Verhoogd risico op insolventie 1-2 jaar | Trend-analyse + ISA 570-indicatoren screenen + bestuur informeren |
| Distress zone | < 1,81 | Acuut risico | Continuïteits-plan formaliseren + alarmprocedure-projectie + going-concern-waardering herzien |

### DSCR-vuistregels

| DSCR-waarde | Interpretatie | Actie |
|---|---|---|
| ≥ 1,30 | Comfortabel | Krediet haalbaar in voorgestelde structuur |
| 1,00 - 1,30 | Krap; binnen vuistregel maar onderhandelen | Eventueel alternatieve structuur (langere looptijd, lagere bedrag) voorstellen |
| < 1,00 | Cashflow dekt zelfs aflossingen niet | Niet-haalbaar; aanbod alternatieven (zie §3) |

### ISA 570 — going-concern-indicatoren (auditor + adviseur)

| Type | Indicator | Tellen mee? |
|---|---|---|
| Financieel | Netto-actief negatief | Ja — sluit aan bij alarmprocedure |
| Financieel | KT-leningen voor LT-financiering (mismatch) | Ja |
| Financieel | Ratio's lopen uit (negatieve trend) | Ja |
| Financieel | Terugkerende exploitatieverliezen | Ja — sterkste indicator |
| Financieel | Achterstand betaling RSZ, BTW, leveranciers | Ja — early signal |
| Financieel | Vergrendelde dividenden, ongunstige ratios | Ja |
| Niet-financieel | Management-vertrek zonder vervanging | Ja |
| Niet-financieel | Verlies sleutel-klant of -leverancier | Ja |
| Niet-financieel | Vergunnings-problemen | Ja |
| Niet-financieel | Arbeidsconflict | Ja |
| Niet-financieel | Technologische veroudering | Ja |

≥ 3 indicatoren oplichten = adviseur moet continuïteits-paragraaf in diagnose opnemen. Commissaris moet ISA 570-procedure formeel doorlopen.

---

## 5. Stappenplannen — wat je doet op het examen

### DSCR-toets — 4 stappen

| Stap | Wat doe je? | Formule / check |
|---|---|---|
| 1 | Annuïteit nieuw krediet berekenen | $a = K \cdot i / (1 - (1+i)^{-n})$ |
| 2 | Totale jaarlijkse schuldenlast | Bestaande aflossingen + nieuwe annuïteit |
| 3 | Beschikbare cashflow bepalen | Bedrijfscashflow proxy = nettores + afschr + Δ voorz + Δ wv (CBN 2011/14) |
| 4 | DSCR berekenen + advies | DSCR = cashflow / debt service; ≥ 1,20 → haalbaar; < 1 → alternatieven aanbieden |

**Alternatieven bij niet-haalbaar**: (1) langere looptijd; (2) eigen inbreng; (3) bullet- of ballonkrediet; (4) staat-gewaarborgde KMO-lening (Gigarant, Sowalfin, finance.brussels); (5) eerst werkkapitaal herstellen om cashflow op te krikken.

### Alarmprocedure-toets — 3 stappen

| Stap | Wat doe je? | Resultaat |
|---|---|---|
| 1 | Netto-actief berekenen (CBN 2021/14) | Totaal activa − voorzieningen − schulden − niet-afgeschreven oprichtings/O&O-kosten |
| 2 | Vergelijken met drempel | NV: helft of kwart kapitaal. BV: nul of liquiditeitstest-fail 12m. |
| 3 | Triggert? | Ja → AV bijeenroepen binnen 2 maanden; bestuursorgaan stelt maatregelen voor. Nee → projectie toekomst (jaarverslag-vermelding indien risico) |

### Diagnose-rapport schrijven — 5 stappen

| Stap | Wat doe je? | Output |
|---|---|---|
| 1 | Data verzamelen + bron-discipline | NBB Balanscentrale + Bel-first + interne data + sector |
| 2 | Consistentie corrigeren | Eenmalige posten + stelselwijzigingen + sector-context |
| 3 | Vier analyse-lagen toepassen | Functionele balans · ratio's · kasstroom · continuïteit |
| 4 | Synthese in financiële SWOT | Sterktes/zwaktes/kansen/bedreigingen in 2×2-matrix |
| 5 | Aanbevelingen per stakeholder × horizon | Tabel: bestuur / bank / aandeelhouders × Q1 / 12m / 24m |

**Executive summary** op pagina 1 (max 1 pagina): diagnose-zin + sterktes + zwaktes/risico's + Top-3 aanbevelingen + vervolg. Vaste structuur — bestuur leest dit + de aanbevelingen-sectie.

### Werkkapitaal-knoppen — wat verhoogt wat?

| Maatregel | Effect op NBK | Effect op BBK | Effect op NT |
|---|---|---|---|
| Voorraden afbouwen | — | ↓ | ↑ |
| DSO inkorten (factoring, debiteurenbeheer) | — | ↓ | ↑ |
| DPO verlengen (binnen relatie-grens) | — | ↓ | ↑ |
| Kapitaal-inbreng aandeelhouders | ↑ | — | ↑ |
| LT-lening (vrij voor exploitatie) | ↑ | — | ↑ |
| LT-lening voor vaste-activa-aankoop | — | — | — |
| Winst reserveren (geen dividend) | ↑ | — | ↑ |
| Desinvestering / sale-and-leaseback (LT) | ↑ | — | ↑ |

---

## 6. Klassieke valkuilen (examen-radar)

| Valkuil | Misvatting | Wat klopt wel |
|---|---|---|
| LT-lening voor vaste-activa boeken als 'NBK-verhoging' | Examen-vraag 2013-2 lijkt te suggereren dat elke LT-lening NBK verhoogt | NBK stijgt alleen als extra LT-financiering NIET in vaste activa landt. 100 k lening + 100 k machine = NBK-neutraal. |
| Bedrijfscashflow gelijkstellen aan operationele kasstroom IAS 7 | BIBF-/Belgische analyse-traditie corrigeert NIET voor werkkapitaal-mutaties | **Bedrijfscashflow proxy** (CBN 2011/14) = nettores + niet-kaskosten. **OK IAS 7** = proxy ± Δ werkkapitaal. Verschil kan groot zijn bij groeiend WK. |
| Cashflow gelijkstellen aan 'beschikbaar voor aflossingen' | Cashflow moet ook financieren: interesten bestaande schulden + belastingen + vervangingsinvesteringen + WK-groei + dividenden | Vuistregel: schuldenlast ≤ 70-80 % van cashflow. Onder DSCR 1,00 = structurele insolventie-aankondiging. |
| Netto-actief gelijkstellen aan eigen vermogen | Bij vennootschappen met niet-afgeschreven oprichtingskosten of O&O-kosten verschilt het | CBN 2021/14 berekening: totaal activa − voorzieningen − schulden − (oprichtings + O&O niet-afgeschreven) |
| Wachten op alarmprocedure-trigger om in te grijpen | Wettelijke trigger is een laat signaal — boedel is dan al ingekleurd | Z-score grey zone + ISA 570-indicatoren oplichten = signaal voor anticiperende actie, NU |
| Voorraadafbouw als 'gratis' BBK-reductie | Te agressief = stockbreuken + omzet-verlies | Beheer in samenhang: financieringskost vs commerciële kost = afweging per knop |
| Diagnose-rapport zonder aanbevelingen-per-verantwoordelijke | 'Verbeter de liquiditeit' is geen aanbeveling — dat is een wens | Concrete actie + verantwoordelijke + horizon — anders dwingt het rapport geen actie af |

---

<div class="no-print">

## 7. Verdieping

Werkt iets niet scherp? Klik door naar het leerstuk dat het uitwerkt of het concept dat het definieert:

### Leerstukken

- [[werkkapitaalbeheer-en-financieringskeuzes]] — drie families BBK-reductie + vier NBK-verhoging + matching-principe + dividend-capaciteit
- [[kredietbeoordeling-en-kasstroomprognose]] — DSCR-recept + annuïteit-formule + vier alternatieven + kasstroomprognose-bouwstenen
- [[continuiteit-en-faillissementspredictie]] — going-concern-beginsel + alarmprocedure-drempels + Z-score + ISA 570 + drie rol-perspectieven
- [[financiele-diagnose-stellen]] — vijf bouwstenen + financiële SWOT + executive-summary-template + drie rol-perspectieven

### Concept-fiches

**Techniek-laag (gedeeld met PO 1.3)** — [[functionele-balans]] · [[jaarrekeninganalyse]] · [[kasstroom-analyse]] · [[free-cash-flow]]

**Ratio-families** — [[liquiditeits-ratios]] · [[solvabiliteits-ratios]] · [[rentabiliteits-ratios]] · [[activiteits-ratios]] · [[ratio-interpretatie]]

**Continuïteit + faillissement** — [[continuiteit]] · [[faillissementspredictie-modellen]] · [[faillissement]] · [[kapitaalbescherming]]

**Diagnose-eindproduct** — [[financiele-diagnose]] · [[financiele-analyse-software]]

</div>

---

*Samenvatting PO 1.9. Status: voorgesteld. Scope-snijlijn met PO 1.3 (techniek versus integratie): zie [leerpad-skelet-1-9](../../leerpad-skelet-1-9).*
