---
title: Balans (jaarrekening-component)
tags:
- concept
- cluster
- po-1-1
- po-1-2
- po-1-5
linked_anchors:
- 1.1.II.S
- 1.1.II.J
- 1.1.II.K
- 1.1.II.L
- 1.1.II.M
- 1.1.II.N
- 1.2.III.B
- 1.5.I
programmaonderdelen:
- '1.1'
- '1.2'
- '1.5'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/balans.json
gegenereerd_op: '2026-05-18'
---
# Balans (jaarrekening-component) ⚖️

Een van de drie verplichte stukken van de jaarrekening (naast resultatenrekening en toelichting). Voor de stagiair-GA centraal omdat **alle PO 1.1-rubrieken over vaste activa, vlottende activa, eigen vermogen, voorzieningen en schulden** hier op verschijnen. Vrijwel elke examenvraag over post-classificatie, schema-keuze of alarmprocedure begint met 'lees deze balans af'.

> [!summary] Korte inhoud
> Het **vermogensoverzicht op één specifieke datum** (balansdatum, typisch 31/12) van een onderneming.

> [!info] Behoort tot: [[jaarrekening]]

Het **vermogensoverzicht op één specifieke datum** (balansdatum, typisch 31/12) van een onderneming. Twee kolommen: **activa** (bezittingen + vorderingen, geordend naar liquiditeit — hoe gemakkelijker te gelde te maken hoe lager) en **passiva** (eigen vermogen + schulden, geordend naar opeisbaarheid — hoe sneller opeisbaar hoe lager). Het fundamentele evenwicht: **activa-totaal = passiva-totaal**. Geboekt op klasse 1 t.e.m. 5 van het MAR. Verplicht onderdeel van de jaarrekening (KB WVV bijlagen 2, 3 of 4 afhankelijk van groottecategorie).

_Bron: KB WVV art. 3:65 — 3:89 (balans); bijlage 2 (volledig schema)_


## Bouwstenen

### Activa: vaste activa boven, vlottende activa onder ⚖️

Activa-zijde geordend van **moeilijkst** naar **gemakkelijkst** liquide. Vaste activa (klasse 2): oprichtingskosten, immateriële vaste activa, materiële vaste activa, financiële vaste activa. Vlottende activa (klasse 3-5): voorraden en bestellingen in uitvoering, vorderingen op ten hoogste één jaar, geldbeleggingen, liquide middelen, overlopende rekeningen actief.

**Waarom?** Lezer ziet meteen de structuur van het ondernemingskapitaal: kapitaalintensief (veel MVA) versus handelsondernemend (veel voorraad/vorderingen). De ordening volgt het gebruik in de bedrijfsvoering — vaste activa zijn de langetermijn-instrumenten, vlottende activa zijn de operationele kringloop.



Rotex Roeselare NV (industriële productie): MVA € 8.500.000 (machines, gebouwen) domineert; vlottende activa € 4.200.000 (voorraad + klantenvorderingen). Naaiatelier Ninove BV (kleinschalig): MVA € 380.000, vlottende activa € 720.000 (voorraad + bank) — handelsverhouding eerder dan kapitaalintensief.

_Grondslag: KB WVV bijlage 2; MAR klasse 2-5_

### Passiva: eigen vermogen boven, schulden onder ⚖️

Passiva-zijde geordend van **niet-opeisbaar** naar **sneller opeisbaar**. Eigen vermogen (klasse 1, rubrieken 10-15): inbreng (kapitaal/uitgiftepremies), reserves, overgedragen resultaat, herwaarderingsmeerwaarden, kapitaalsubsidies. Voorzieningen voor risico's en kosten + uitgestelde belastingen (rubriek 16-17). Schulden (klasse 17-49): schulden op meer dan één jaar, schulden op ten hoogste één jaar, overlopende rekeningen passief.

**Waarom?** Een lezer ziet de **financierings­bronnen** in volgorde van risico voor de onderneming: eigen vermogen kan niet worden opgeëist (geen claim), schulden moeten op vervaldag worden afgelost. Solvabiliteit lees je af uit de verhouding EV / totaal passiva.



Rotex Roeselare NV: EV € 5.800.000 (kapitaal + reserves + overgedragen) — schulden LT € 4.500.000 — schulden KT € 2.400.000 → solvabiliteit ≈ 45 %. Een KMO met EV € 95.000 op schulden € 480.000 (solvabiliteit ≈ 17 %) zit in alarmprocedure-risico (WVV art. 7:228 als negatief netto-actief ontstaat).

_Grondslag: KB WVV bijlage 2; MAR klasse 1, 16-17_

### Activa-totaal = passiva-totaal (boekhoudkundig evenwicht) ⚖️

De fundamentele balans-vergelijking: activa = passiva. Boekhoudkundig gegarandeerd door dubbel-boekhouden (elke transactie heeft debet- én credit-impact). Een afwijking duidt op een boekhoudfout — niet op een economische ongelijkheid.

**Waarom?** Dit evenwicht is een **controle-instrument**: bij elke proefbalans (eindejaarsverrichtingen stap 7) moet debet = credit. Onbalans wijst op een telout, een vergeten boeking of een geboekte ongelijkmatige journaalpost.



Naaiatelier Ninove BV 31/12 (verkort schema): activa-totaal € 1.100.000 (MVA € 380.000 + voorraad € 195.000 + klanten € 280.000 + bank € 245.000) = passiva-totaal € 1.100.000 (EV € 380.000 + schulden LT € 95.000 + schulden KT € 625.000). Onbalans van € 1 = boekfout, opsporen vóór neerlegging.

_Grondslag: KB WVV art. 3:1; dubbel-boekhoudsysteem_

### Drie schemas: volledig, verkort, micro ⚖️

Net als de resultatenrekening kent de balans drie detailniveaus. Volledig schema (bijlage 2 KB WVV, ~25 balansrubrieken aan elke kant); verkort schema (bijlage 3, ~12 rubrieken — samenvoegingen); microschema (bijlage 4, ~8 rubrieken — minimale uitsplitsing).

**Waarom?** Administratieve proportionaliteit naar grootte. Stagiair moet rubrieken in elk schema kunnen lokaliseren — examenvragen specifiëren typisch welk schema gebruikt wordt.



Volledig schema toont 'III. Materiële vaste activa' met sub-rubrieken A. Terreinen en gebouwen / B. Installaties, machines en uitrusting / C. Meubilair en rollend materieel / D. Leasing en soortgelijke rechten / E. Overige MVA / F. Activa in aanbouw. Verkort schema groepeert tot één lijn 'III. Materiële vaste activa'.

_Grondslag: KB WVV bijlagen 2, 3, 4_

### Vergelijkende cijfers verplicht ⚖️

Op de balans staan voor elke rubriek **twee bedragen** naast elkaar: huidig boekjaar (N) en vorig boekjaar (N-1). Deze 'comparatives' vereisen identieke rubrieken en waarderingsmethoden tussen jaren (consistentiebeginsel). Bij methode-wijziging: vermelding in toelichting + (vaak) restatement van vorig jaar.

**Waarom?** Lezer ziet evolutie van vermogenspositie — sterke daling van EV, sterke stijging van schulden, voorraad-explosie zijn allemaal signalen die je pas ziet bij vergelijking.



Brugse Brouwerij BV balans 20X1: voorraad € 285.000 (20X1) versus € 165.000 (20X0). Stijging € 120.000 wekt vragen op — voorraadopbouw door zwakke verkoop, of strategische opslag voor seizoenspiek? Toelichting moet dat duiden.

_Grondslag: KB WVV art. 3:8 (consistentiebeginsel); bijlagen 2-4_


## In de praktijk

- De balans is een **momentopname** — niet representatief voor het hele boekjaar. Bij sterk seizoensgebonden ondernemingen (ijsfabrikant, kerstdecoratie) kan de eindbalans op 31/12 ongewoon laag voorraadcijfer of hoog kassaldo tonen. De analist relativeert met seizoenscorrectie.
- Onder de balans staat een **buiten-balans-vermelding** in de toelichting: rechten en verplichtingen klasse 0 (borgstellingen, leaseverplichtingen niet-geactiveerd, hangende geschillen). Een 'mooie' balans kan een grote off-balance-exposure verbergen.
- Een **alarmprocedure** (WVV art. 5:153 voor BV / 7:228 voor NV) ontstaat wanneer het netto-actief (EV) onder kritieke drempels zakt: minder dan helft van het kapitaal of negatief. Bestuursorgaan moet dan AV bijeenroepen.
- De balans **beginstand jaar N** moet gelijk zijn aan de balans **eindstand jaar N-1** (continuiteitsbeginsel KB WVV art. 3:5). Onverklaard verschil = boekhoudfout of onverklaarde correctie.

> [!info]- Niet verwarren met [[resultatenrekening]]
> Balans = **toestand op één moment** (vermogensoverzicht 31/12). Resultatenrekening = **flow over een periode** (kosten en opbrengsten van 1/1 tot 31/12). Het saldo van de RR (winst/verlies) komt op de balans terecht als component van eigen vermogen (rekening 14 'Overgedragen resultaat').
>
> _Trigger_: Examen: 'op welke staat staat post X?' Toestand (saldo) → balans. Beweging (gedurende periode) → RR.

> [!info]- Niet verwarren met [[analytische-balans]]
> Statutaire balans volgt KB WVV-schema (juridisch/fiscaal/extern). Analytische balans is een geherorderde versie voor financiële analyse (werkkapitaal, behoefte aan bedrijfskapitaal, nettokas). Zelfde cijfers, andere rangschikking met andere onderverdelingen.
>
> _Trigger_: Examen: 'bereken behoefte aan bedrijfskapitaal' — eerst statutaire balans naar analytische balans omzetten.


## Valkuilen

> [!warning]- **Solvabiliteit en liquiditeit lees je uit de balans, niet uit de RR**
> ⚠️ **Solvabiliteit en liquiditeit lees je uit de balans, niet uit de RR**. Een onderneming kan winstgevend zijn (RR positief) maar illiquide of insolvent (balans toont schulden > activa, of vlottende activa << vlottende schulden). Klassieke examenvraag: 'de NV maakte € 200.000 winst maar staat aan rand faillissement — hoe?'. ⚖️
>
> _Bron: KB WVV_


> [!warning]- **Eigen vermogen ≠ kapitaal**
> ⚠️ **Eigen vermogen ≠ kapitaal**. Het kapitaal (rubriek 10) is slechts één component van het eigen vermogen (klasse 1). Reserves, overgedragen resultaat, herwaarderingsmeerwaarden en kapitaalsubsidies maken óók deel uit van het eigen vermogen. Alarmprocedure-test kijkt naar **totaal eigen vermogen** (rubriek 10-15), niet naar kapitaal alleen. ⚖️
>
> _Bron: WVV art. 1:8 + KB WVV_


> [!warning]- **Boekwaarde ≠ marktwaarde**
> ⚠️ **Boekwaarde ≠ marktwaarde**. Een gebouw met boekwaarde € 850.000 kan een marktwaarde van € 1.500.000 hebben. Voorzichtigheidsbeginsel verbiedt opboeking. Pas bij verkoop wordt de meerwaarde gerealiseerd. Analyse-rapporten met liquidatie- of going-concern-waardering vragen daarom een herwaardering bovenop wat de balans toont. ⚖️
>
> _Bron: KB WVV art. 3:6 (voorzichtigheidsbeginsel)_



## Zie ook

- **Getriggerd door**: [[eindejaarsverrichtingen]]

## Voorbeelden

### Statutaire balans verkort schema — Naaiatelier Ninove BV 31/12/20X1

_Personages: Naaiatelier Ninove BV_

Naaiatelier Ninove BV (klein) heeft op 31/12/20X1 een vereenvoudigde balans verkort schema.

1. Inventariseer activa: MVA netto € 380.000, voorraden € 195.000, handelsvorderingen € 280.000, bank € 245.000.
2. Inventariseer passiva: kapitaal € 18.500, reserves € 95.000, overgedragen resultaat € 142.500 (= EV € 256.000); voorzieningen € 25.000; schulden LT € 95.000; schulden KT (handel + sociaal + fiscaal) € 624.000.
3. Tel: activa € 1.100.000 = passiva € 1.000.000. Onbalans € 100.000 → fout opsporen.
4. Na correctie (herclassering van voorraad € 100.000 die dubbel was geboekt): activa € 1.000.000 = passiva € 1.000.000.
#### Balans verkort schema 31/12/20X1 (gecorrigeerd)
| Activa | Bedrag | Passiva | Bedrag |
|---|---:|---|---:|
| I. Oprichtingskosten | 0 | I. Eigen vermogen | 256000 |
| II. Immateriële vaste activa | 12000 | II. Voorzieningen | 25000 |
| III. Materiële vaste activa | 368000 | III. Schulden op meer dan 1 jaar | 95000 |
| IV. Voorraden | 95000 | IV. Schulden op ten hoogste 1 jaar | 624000 |
| V. Vorderingen ten hoogste 1 jaar | 280000 |  |  |
| VI. Geldbeleggingen + liquide middelen | 245000 |  |  |



## Bronnen

[^1]: `KB-WVV-2019__art_3_66`
[^2]: `MAR-ondernemingen__art_1_part1`
