---
title: Schulden (LT en KT)
tags:
- concept
- cluster
- po-1-1
linked_anchors:
- 1.1.II.J
- 1.1.II.K
programmaonderdelen:
- '1.1'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/schulden.json
gegenereerd_op: '2026-05-21'
---
# Schulden (LT en KT) ⚖️

De passief-zijde van de financiering — vergt scherp onderscheid op resterende looptijd (LT/KT) en aard (handels/financieel/overige). Voor een stagiair-GA: de overboeking van LT naar KT op het deel dat binnen twaalf maanden vervalt (rekening 42) is een vaste eindjaarsverrichting, en de waardering aan terugbetalingswaarde zonder actualisering is een Belgisch-GAAP-eigenheid t.o.v. IFRS.

> [!summary] Korte inhoud
> **Verplichtingen** van de onderneming tot betaling van een vastgesteld bedrag aan een derde, gewaardeerd tegen nominale **terugbetalingswaarde**.

> [!info] Bestaat uit (1): [[obligatielening]]

**Verplichtingen** van de onderneming tot betaling van een vastgesteld bedrag aan een derde, gewaardeerd tegen nominale **terugbetalingswaarde**. Onderscheid op de balans naar resterende looptijd op balansdatum: **schulden op meer dan één jaar** (rubriek VIII, MAR klasse 17 — financiële schulden, handelsschulden LT, ontvangen vooruitbetalingen LT) en **schulden op ten hoogste één jaar** (rubriek IX, MAR klasse 42 — schulden op meer dan één jaar die binnen het jaar vervallen, 43 — financiële schulden KT, 44 — leveranciers, 45 — schulden uit belastingen/lonen/sociale lasten, 48 — andere).

_Bron: MAR klasse 1 + 4; KB WVV art. 3:48_



## Bouwstenen

### Splitsing op meer / hoogstens één jaar ⚖️

Voor elke meerjarige schuld wordt op balansdatum het gedeelte dat binnen 12 maanden vervalt overgeboekt naar rekening 42 'Schulden op meer dan één jaar die binnen het jaar vervallen'. Het langere-termijn-deel blijft op rekening 17.

**Waarom?** Voor de gebruiker is liquiditeit cruciaal. Korte-termijn-druk moet uit de balans aflezbaar zijn, niet verstopt in een lange-termijn-rubriek.



Uitgeverij Ukkel NV hypothecaire lening 10 jaar, jaarlijkse aflossing € 85.000. Op 31/12/20X1: nog 8 jaar te lopen, totaal € 765.000 schuld. Splitsing: € 85.000 op rekening 42 (vervalt in 20X2), € 680.000 op rekening 173 (langer dan jaar).

_Grondslag: KB WVV art. 3:48 + MAR_

### Categorieën schulden in MAR ⚖️

(17) Financiële schulden LT: 170 obligatieleningen, 173 kredietinstellingen, 174 leasingschulden. (42) idem maar binnen jaar vervallend. (43) Financiële schulden KT: bankvoorschotten. (44) Leveranciers + ontvangen vooruitbetalingen op bestellingen. (45) Belastingen, bezoldigingen, sociale lasten. (48) Diverse schulden.

**Waarom?** Per categorie krijgt de balanslezer meteen inzicht in de aard van de verplichtingen: handelsverplichtingen vs fiscale vs financiële.



Naaiatelier Ninove BV op 31/12: leveranciersschulden € 145.000 (440), BTW te betalen € 18.500 (4514), bedrijfsvoorheffing € 4.200 (453), bezoldigingen € 32.000 (455), RSZ-bijdragen € 18.700 (454). Subtotaal rubriek IX = € 218.400.

_Grondslag: MAR klasse 1 + 4_

### Waardering aan terugbetalingswaarde ⚖️

Schulden worden gewaardeerd aan het bedrag dat bij vervaldag betaald moet worden (nominale waarde). Geen actualisering op basis van rente. Verschil tussen aanvankelijk ontvangen bedrag en terugbetalingswaarde (bv. bij obligaties uitgegeven beneden pari): verschil wordt geactiveerd of als financiële kost geboekt over de looptijd.

**Waarom?** Eenvoud en voorzichtigheid: de werkelijke betalingsverplichting is wat telt. Voor de gebruiker is dit het meest relevant cijfer.



Uitgeverij Ukkel NV geeft obligaties uit voor nominaal € 1.000.000 maar ontvangt slechts € 950.000 (uitgifte beneden pari, € 50.000 disagio). Schuldwaarde op balans = nominale € 1.000.000; disagio € 50.000 wordt geactiveerd onder oprichtingskosten 201 en afgeschreven over looptijd.

_Grondslag: KB WVV art. 3:48_

### Niet-uitgesproken intresten op LT-schulden ⚖️

Voor schulden op meer dan één jaar zonder rente of met abnormaal lage rente kan een **correctie op de werkelijke schuldwaarde** worden geboekt. Het verschil wordt verspreid in de tijd als financiële kost (KB WVV art. 3:48).

**Waarom?** Een renteloze lening is in feite een korting; de echte economische waarde van de schuld is lager dan de nominale. Deze regel voorkomt verstoring.



Solaris Sint-Truiden BV ontvangt een renteloze lening van € 200.000 voor 5 jaar van een verbonden onderneming. Marktrente 4 % → contante waarde € 200.000 / (1,04)^5 = € 164.386. Verschil € 35.614 wordt over 5 jaar als intrestlast geboekt.

_Grondslag: KB WVV art. 3:48_


## In de praktijk

<h3 id="cut-off-rond-balansdatum-schulden-die-nog-niet-zijn-gefactureerd">Cut-off rond balansdatum: schulden die nog niet zijn gefactureerd</h3>

> [!tip]- Cut-off rond balansdatum: schulden die nog niet zijn gefactureerd
> Op balansdatum kunnen goederen of diensten al ontvangen zijn waar de factuur nog niet is binnengekomen. Deze 'te ontvangen facturen' worden geboekt op rekening 444 'Te ontvangen facturen' (subcategorie leveranciersschulden). ⚖️

> [!tip]- Herkennen op het examen
> Examen: 'in december levering ontvangen voor € 25.000, factuur komt in januari' → boeking december op 444 (schuld) + 600 (kost), niet wachten op factuur.


## Valkuilen

> [!warning]- De splitsing LT/KT gebeurt elk jaar opnieuw — op basis van RESTERENDE looptijd op balansdatum, niet oorspronkelijke
> ⚠️ De splitsing LT/KT gebeurt elk jaar opnieuw — op basis van RESTERENDE looptijd op balansdatum, niet oorspronkelijke. Een 10-jarige lening met nog 8 maanden te lopen staat volledig in rubriek IX. ⚖️
>
> _Bron: KB WVV art. 3:48_


> [!warning]- Voorzieningen (rubriek 16) ZIJN GEEN schulden
> ⚠️ Voorzieningen (rubriek 16) ZIJN GEEN schulden. Schulden zijn vaststaande verplichtingen; voorzieningen zijn onzekere risico's/kosten. Onder bepaalde voorwaarden migreert een voorziening naar een schuld (zodra zeker en gefactureerd). ⚖️
>
> _Bron: KB WVV art. 3:11 vs 3:48_



## Zie ook

- **Vereist kennis van**: [[overlopende-rekeningen]]

## Voorbeelden

Uitgeverij Ukkel NV heeft op 31/12: hypothecaire lening 10 jaar — beginsaldo € 850.000, eindsaldo € 765.000 waarvan € 85.000 binnen het jaar vervalt. Boekhoudkundige presentatie: € 680.000 op rubriek VIII 'Schulden op meer dan één jaar' (rekening 173) en € 85.000 op rubriek IX 'Schulden op ten hoogste één jaar' (rekening 42). Daarnaast leveranciersschulden € 145.000 (44), BTW-schuld € 18.500 (4514), bezoldigingen € 32.000 (455).

## Bronnen

[^1]: `MAR-ondernemingen__art_1`
[^2]: `MAR-ondernemingen__art_4`
