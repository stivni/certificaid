---
title: Leasing (financieel en operationeel)
tags:
- concept
- cluster
- po-1-1
linked_anchors:
- 1.1.II.W
- 1.1.II.B
programmaonderdelen:
- '1.1'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/leasing.json
gegenereerd_op: '2026-05-18'
---
# Leasing (financieel en operationeel) ⚖️

De Belgische GAAP-classificatie loopt fundamenteel anders dan IFRS — financieel/operationeel hangt af van wedersamenstellings-criterium, niet van risico-overdracht. Voor een stagiair-GA: cruciaal om beide regimes uit elkaar te houden en het juiste te kiezen volgens het toepasselijke kader (B-GAAP voor de meeste KMO's, IFRS bij genoteerd of consoliderende moeder).

> [!summary] Korte inhoud
> Een overeenkomst waarbij een **leasinggever** het gebruik van een goed (auto, machine, gebouw) afstaat aan een **leasingnemer** tegen periodieke vergoeding.

Een overeenkomst waarbij een **leasinggever** het gebruik van een goed (auto, machine, gebouw) afstaat aan een **leasingnemer** tegen periodieke vergoeding. Twee soorten met fundamenteel verschillende boekhoudkundige verwerking: (1) **Financiële leasing** — de leasingvergoedingen dekken de **integrale wedersamenstelling van het kapitaal** dat de gever in het goed investeerde (plus rente). Economisch een aankoop met financiering → activering bij leasingnemer (rubriek 25 MVA in leasing). (2) **Operationele leasing** — vergoedingen dekken NIET de integrale wedersamenstelling. Economisch een huur → kost in resultaat bij leasingnemer.

_Bron: CBN 2015/04 — Leasing + KB WVV art. 3:43 (oud art. 95 KB W.Venn.)_


## Bouwstenen

### Criterium financiële vs operationele leasing ⚖️

Een leasing is **financieel** wanneer de contractueel te storten termijnen (naast rente en kosten) de **integrale wedersamenstelling** dekken van het kapitaal dat de gever in het goed heeft geïnvesteerd. Voor roerende leasings met koopoptie: de optieprijs telt mee als ze maximaal **15 % vertegenwoordigt** van het geïnvesteerde kapitaal. Boven 15 %: operationeel.

**Waarom?** Het criterium volgt de economische werkelijkheid: als de gebruiker uiteindelijk alle waarde van het goed betaalt + zelfs gebruik kan uitkopen tegen een lage prijs, is het de facto een aankoop. Boekhouding moet die economische werkelijkheid weergeven (substance over form).



Transport Tongeren BV vrachtwagen € 85.000, koopoptie € 5.000 (5,9 %) → financieel. Alternatief: koopoptie € 17.500 (20,6 % > 15 %) → operationeel.

_Grondslag: KB WVV art. 3:43 (oud KB art. 95)_

### Financiële leasing — boekhoudkundige verwerking bij leasingnemer ⚖️

(a) Aanvang: actief op rubriek 25 ('MVA in leasing') tegen aanschaffingswaarde (= geïnvesteerd kapitaal) + leasingschuld op rubriek 172 voor zelfde bedrag. (b) Per annuïteit: splitsing kapitaal (vermindering schuld) + rente (financiële kost). (c) Afschrijving van het geleasde actief volgens normale regels voor het soort goed (cfr. eigen MVA). (d) Bij optielichting: overboeking van rubriek 25 naar relevante MVA-rubriek.

**Waarom?** Het actief is economisch dat van de leasingnemer; symmetrische schuld toont financiering. Substance over form.



Transport Tongeren BV jaar 1: jaarlijkse annuïteit € 18.500 (kapitaal € 17.000 + intrest € 1.500). Boeking: Debet 172 Leasingschulden € 17.000 + Debet 650 Intresten € 1.500 / Credit 550 Bank € 18.500. Tegelijk afschrijving vrachtwagen: € 85.000 / 5 jaar = € 17.000 → Debet 6302 / Credit 2529.

_Grondslag: CBN 2015/04_

### Operationele leasing — boekhoudkundige verwerking ⚖️

Goed blijft op de balans van de leasinggever; de leasingnemer boekt de vergoedingen rechtstreeks als **kost** (rubriek 61 'Diensten en diverse goederen'). Geen activum op balans, geen schuld. Soortgelijk aan huur.

**Waarom?** Economisch is operationele leasing dichter bij huur dan bij aankoop; de leasingnemer gebruikt het goed maar 'bezit' het niet. Eenvoudige presentatie volstaat.



Meubelzaak Mertens BV huurt een bestelwagen via operationele leasing aan € 480/maand. Maandelijks: Debet 6105 Huur voertuigen € 480 / Credit 550 Bank € 480. Geen activum, geen schuld op balans.

_Grondslag: CBN 2015/04_

### Toelichting — verplichte vermeldingen ⚖️

In de toelichting bij de jaarrekening: (a) staat MVA in leasing (aanschaffingswaarde, mutaties, afschrijvingen, nettoboekwaarde) per categorie, (b) staat schulden in leasing met uitsplitsing naar resterende looptijd, (c) rechten op aankoop, (d) samenvatting waarderingsregels, (e) algemene beschrijving leasingvoorwaarden.




Transport Tongeren BV toelichting: 'Rubriek III.D Materiële vaste activa in leasing: aanschaffingswaarde € 85.000 (vrachtwagen), cumul. afschr. € 34.000 (na 2 jaar), nettowaarde € 51.000. Leasingschuld 172: oorspr. € 85.000, resterend € 51.000, waarvan € 17.000 binnen jaar en € 34.000 op meer dan jaar.'

_Grondslag: CBN 2015/04_


## In de praktijk

<h3 id="tijdelijke-niet-betaling-covid-context">Tijdelijke niet-betaling (Covid-context)</h3>

> [!tip]- Tijdelijke niet-betaling (Covid-context)
> Bij Covid-kwijtscheldingen: voor operationele leasing geen huur geboekt tijdens opschortingsperiode; voor financiële leasing hangt af van overeenkomst (vaak alleen hoofdsom opgeschort, intrest blijft lopen). ⚖️


> [!info]- Niet verwarren met [[huur-versus-leasing-aspect]]
> Operationele leasing en huur zijn boekhoudkundig vrijwel identiek (kost in RR, geen activum/schuld). Verschil ligt juridisch (huurovereenkomst vs leasecontract) en in mogelijke koopoptie.
>
> _Trigger_: Examen: 'gewone huur kantoor € 1.500/maand' = kostenrekening 61. 'leasing met optie tot aankoop' = onderzoek of optie ≤ 15 % → financieel of operationeel.


## Valkuilen

> [!warning]- De **15 %-regel** voor de koopoptie geldt ALLEEN voor roerende goederen
> ⚠️ De **15 %-regel** voor de koopoptie geldt ALLEEN voor roerende goederen. Voor onroerende goederen (gebouwen) zijn andere criteria van toepassing. Examen: 'leasing van een gebouw met koopoptie 8 %' — niet automatisch financieel; bekijk volledige criteria. ⚖️
>
> _Bron: CBN 2015/04_


> [!warning]- Belgisch boekhoudrecht hanteert een **andere financiële leasing-definitie dan IFRS 16**
> ⚠️ Belgisch boekhoudrecht hanteert een **andere financiële leasing-definitie dan IFRS 16**. Onder IFRS 16 worden bijna alle leasings geactiveerd; in België blijft de splitsing financieel/operationeel volgens KB WVV-criteria gelden. ⚖️
>
> _Bron: CBN 2015/04_



## Zie ook

- **Vereist kennis van**: [[materiele-vaste-activa]]
- **Vereist kennis van**: [[afschrijvingen]]

## Voorbeelden

Transport Tongeren BV neemt een vrachtwagen (werkelijke waarde € 85.000) in financiële leasing voor 5 jaar; jaarlijkse vergoeding € 18.500 (kapitaal € 17.000 + intrest € 1.500) + koopoptie € 5.000 (5,9 % van € 85.000 < 15 %, dus financieel). Boekingen aanvang: Debet 252 MVA in leasing — meubilair/rollend € 85.000 / Credit 172 Leasingschulden € 85.000. Per jaar: Debet 172 € 17.000 + Debet 650 Intresten € 1.500 / Credit 550 Bank € 18.500; en afschrijving Debet 6302 € 17.000 / Credit 2529 € 17.000 (lineair 5 jaar).

## Bronnen

[^1]: `CBN-2015-04-leasing__sec_algemene-principes`
[^2]: `CBN-2021-05-boekhoudrechtelijke-behandeling-van-kwijtschelding-van-huur-ten-gevolge-van-de-covid-19__sec_boekhoudkundige-verwerking-van-de-tijdelijke-niet-betaling-v`
[^3]: `CBN-2015-04-leasing__sec_boekingen-tijdens-de-looptijd-van-het-leasingcontract`
[^4]: `CBN-2015-04-leasing__sec_informatieverschaffing-in-de-toelichting-bij-de-jaarrekening`
