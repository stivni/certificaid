---
title: Afschrijvingen
tags:
- concept
- cluster
- po-1-1
- po-1-2
linked_anchors:
- 1.1.II.A
- 1.1.II.B
- 1.1.II.W
- 1.2.V.B
- 1.2.V
- 1.2.taak.1
programmaonderdelen:
- '1.1'
- '1.2'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/afschrijvingen.json
gegenereerd_op: '2026-05-18'
---
# Afschrijvingen ⚖️

> [!summary] Korte inhoud
> Bedragen ten laste van de resultatenrekening genomen met betrekking tot **oprichtingskosten** en **immateriële en materiële vaste activa met beperkte gebruiksduur**, om hetzij de aanschaffingswaarde te spreiden over de waarschijnlijke gebruiksduur, hetzij de kost te nemen op het….

> [!info] Specialisatie van: [[voorzichtigheidsbeginsel]]

Bedragen ten laste van de resultatenrekening genomen met betrekking tot **oprichtingskosten** en **immateriële en materiële vaste activa met beperkte gebruiksduur**, om hetzij de aanschaffingswaarde te spreiden over de waarschijnlijke gebruiksduur, hetzij de kost te nemen op het ogenblik waarop ze worden aangegaan (KB WVV art. 3:23). Het afschrijvingsplan wordt vastgesteld door het bestuursorgaan en samengevat in de toelichting. De gecumuleerde afschrijvingen worden in mindering gebracht van de actiefposten waarop ze betrekking hebben.

_Bron: KB WVV art. 3:23_


## Bouwstenen

### Drie elementen om de afschrijving te bepalen ⚖️

Voor elk afschrijfbaar actief bepaal je drie dingen: (1) de **af te schrijven waarde** (aanschaffingswaarde, eventueel min restwaarde), (2) de **geschatte gebruiksduur** in jaren, (3) het **ritme van verbruik** (gelijkmatig, degressief, progressief, pro rata van prestatie-eenheden).

**Waarom?** Deze drie keuzes definiëren samen de jaarlijkse last. Eén keuze veranderen (bv. korte gebruiksduur) heeft direct impact op het resultaat — daarom moet het plan onderbouwd zijn en consistent worden toegepast.



Voor de snij-installatie van € 30.500: af te schrijven waarde € 30.500 (geen restwaarde geschat), gebruiksduur 5 jaar, ritme lineair → € 6.100/jaar.

_Grondslag: KB WVV art. 3:23; CBN 2010/15_

### Vastgesteld door bestuursorgaan + samengevat in toelichting ⚖️

Het afschrijvingsplan wordt formeel vastgesteld door het bestuursorgaan. Een samenvatting van de waarderingsregels (inclusief gehanteerde gebruiksduur per categorie) komt in de toelichting bij de jaarrekening.

**Waarom?** Transparantie tegenover de jaarrekeninggebruiker: hij moet de afschrijvingslast kunnen interpreteren in functie van de gekozen methode. Bovendien dwingt de formele vaststelling tot bewuste keuzes.



Bestuur Naaiatelier Ninove BV beslist in waarderingsregels: 'Installaties en machines: lineair, 5 jaar. Bedrijfsvoertuigen: lineair, 4 jaar. Kantoormeubilair: lineair, 10 jaar.' Toelichting bij jaarrekening: sectie 'Waarderingsregels'.

_Grondslag: KB WVV art. 3:6 + CBN 2010/15_

### Recurrent versus niet-recurrent ⚖️

Recurrente afschrijvingen volgen het opgestelde afschrijvingsplan. **Niet-recurrente afschrijvingen** worden geboekt bovenop het plan wanneer de boekwaarde plots groter is dan de gebruikswaarde door technische ontwaarding of gewijzigde economische omstandigheden.

**Waarom?** Het plan veronderstelt 'normaal gebruik'. Bij abnormale ontwaarding (brand, technologische sprong, brexit-effect) moet sneller afgeschreven worden om geen overgewaardeerd actief op de balans te houden.



Naaiatelier Ninove BV heeft een snij-installatie met boekwaarde € 18.300 (na 2 jaar). Door brand is de installatie maar half functioneel; gebruikswaarde = € 6.500. Niet-recurrente afschrijving = € 18.300 − € 6.500 = € 11.800, geboekt op rekening 6602 'Niet-recurrente afschrijvingen' i.p.v. 6302.

_Grondslag: KB WVV art. 3:23 + CBN 2019/04_

### Terugname van niet-recurrente afschrijving — verplicht ⚖️

Wanneer de eerder geboekte niet-recurrente afschrijving niet langer verantwoord is (omdat de gebruikswaarde herstelt), MOET de overdaad worden teruggenomen — voor het surplus boven de gewone afschrijving die uit het plan zou volgen.

**Waarom?** Voorzichtigheid mag geen verborgen reserve worden. Als de oorzaak van de extra afschrijving verdwijnt, moet ook het effect verdwijnen.



Brand-versterkte niet-recurrente afschrijving van € 11.800 in jaar 2; in jaar 3 wordt de installatie volledig hersteld en de gebruikswaarde is terug € 22.000. Terugname tot het bedrag dat volgens het gewone plan op die datum aanvaardbaar is.

_Grondslag: KB WVV art. 3:23 + CBN 2019/04_


## Berekening

### Lineaire afschrijving

**Lineaire jaarlijkse afschrijving** 
```
jaarlijkse afschrijving = (aanschaffingswaarde − restwaarde) / gebruiksduur in jaren
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `aanschaffingswaarde` | Zie [[aanschaffingswaarde]] | EUR |
| `restwaarde` | Geschatte waarde aan einde van gebruiksduur | EUR |
| `gebruiksduur` | Geschatte economische levensduur | jaar |

**Voorbeeld-invulling**: aanschaffingswaarde = € 30.500; restwaarde = € 0; gebruiksduur = 5 jaar

```
(€ 30.500 − € 0) / 5 = € 6.100 per jaar
```

_Resultaat in EUR_
*Het meest gangbare ritme: even grote tranches over alle jaren van de gebruiksduur. Geschikt wanneer het actief gelijkmatig wordt gebruikt.*

### 1. Bepaal de af te schrijven waarde

Aanschaffingswaarde minus eventueel geschatte restwaarde. Vaak wordt restwaarde 0 verondersteld.

**🛠️ Hoe**:

1. Neem aanschaffingswaarde uit de boekhouding (rekening eindigend op 0).
2. Trek restwaarde af (indien geschat).
3. = af te schrijven waarde.


**Grondslag**: CBN 2010/15

### 2. Bereken jaarlijkse tranche

Af te schrijven waarde / gebruiksduur in jaren.

**🛠️ Hoe**:

1. Deel af te schrijven waarde door gebruiksduur.
2. = jaarlijkse afschrijving.
3. Pro rata in jaar van aankoop (alleen voor het deel van het jaar).


> [!example]- Voorbeeld: Naaiatelier Ninove BV koopt op 1 juli 20X1 een snij-installatie voor € 30.500, gebruiksduur 5 jaar, restwaarde 0
> Naaiatelier Ninove BV koopt op 1 juli 20X1 een snij-installatie voor € 30.500, gebruiksduur 5 jaar, restwaarde 0.
>
> 1. **Berekening per jaar** 🧮
>
>    Af te schrijven waarde: € 30.500
>    Gebruiksduur: 5 jaar
>    Jaarlijkse tranche: € 30.500 / 5 = **€ 6.100**
>
> 2. **Pro rata jaar van aankoop (6 maanden in 20X1)** 🧮
>
>    Afschrijving 20X1: € 6.100 × 6/12 = **€ 3.050**
>    Afschrijving 20X2 — 20X5: € 6.100 elk jaar
>    Afschrijving 20X6: € 6.100 × 6/12 = € 3.050 (laatste half jaar)
>    Totaal: € 3.050 + € 6.100 × 4 + € 3.050 = € 30.500 ✓
>
> 3. **Boeking eind 20X1** 📝
>
>    Debet 6302 Afschrijvingen MVA € 3.050 / Credit 2309 Afschrijvingen op installaties € 3.050
>    Netto-boekwaarde 31/12/20X1 = € 30.500 − € 3.050 = € 27.450
>

**Grondslag**: CBN 2010/15

### Degressieve afschrijving (versneld)

**Degressieve afschrijving (fiscaal)** 
```
jaarlijkse afschrijving = nettoboekwaarde × (2 × lineair %)  — tot lineair lager
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `nettoboekwaarde` | Aanschaffingswaarde min cumul. afschrijvingen op begin van het jaar | EUR |
| `lineair %` | 1 / gebruiksduur in jaren | % |

**Voorbeeld-invulling**: aanschaffingswaarde € 30.500; gebruiksduur 5 jaar (lineair % = 20 %, degressief % = 40 %)

```
Jaar 1: € 30.500 × 40 % = € 12.200 (vs lineair € 6.100). Jaar 2: (€ 30.500 − € 12.200) × 40 % = € 7.320.
```

_Resultaat in EUR_
*Hogere afschrijvingen in de eerste jaren, lager in latere jaren. Toegelaten voor materiële en immateriële vaste activa wanneer dit het werkelijke verbruiksritme weerspiegelt; ook fiscaal versneld plan is toegelaten (KB WVV art. 3:25).*

### 1. Kies methode (fiscaal degressief vs economisch degressief)

Fiscaal versneld: dubbele lineaire jaartranche tot lineair lager wordt. Economisch degressief: lijn volgens werkelijk verbruik.

**🛠️ Hoe**:

1. Fiscaal: bv. dubbele lineaire tranche = 2 × (1/n) op nettoboekwaarde tot lineair lager.
2. Economisch: indien aantoonbaar (bv. ICT-apparatuur verliest snel waarde).

**Grondslag**: KB WVV art. 3:25


## In de praktijk

<h3 id="onderzoek-en-ontwikkeling-goodwill-5-jaar-motivering">Onderzoek en ontwikkeling, goodwill: > 5 jaar = motivering</h3>

> [!tip]- Onderzoek en ontwikkeling, goodwill: > 5 jaar = motivering
> Het KB WVV legt geen minimumafschrijvingsduur op voor immateriële vaste activa, MAAR afschrijving van **kosten van onderzoek en ontwikkeling** of **goodwill** over MEER dan 5 jaar moet worden verantwoord in de toelichting. ⚖️

> [!tip]- Herkennen op het examen
> Examen: 'goodwill afschrijven over 10 jaar' — kan, mits motivering in toelichting.

<h3 id="buiten-gebruik-gestelde-activa-rekening-26">Buiten gebruik gestelde activa (rekening 26)</h3>

> [!tip]- Buiten gebruik gestelde activa (rekening 26)
> Activa die niet meer duurzaam tot de activiteit bijdragen, worden overgebracht naar rekening 26 'Overige materiële vaste activa'. Recurrente afschrijvingen stoppen; in plaats daarvan: niet-recurrente afschrijving of waardevermindering tot realisatiewaarde. ⚖️


> [!info]- Niet verwarren met [[waardeverminderingen]]
> Afschrijvingen: planmatige correctie voor activa met BEPERKTE gebruiksduur (KB WVV art. 3:23, lid 1). Waardeverminderingen: correctie voor activa met onbeperkte gebruiksduur OF voor vlottende activa, om rekening te houden met al-dan-niet-definitieve ontwaardingen (lid 2). Verschillende rekeningen, ander logica.
>
> _Trigger_: Examen: 'gebouw' (gebruiksduur beperkt) → afschrijving. 'Terrein' (onbeperkt) → waardevermindering. 'Voorraad' (vlottend actief) → waardevermindering.


## Valkuilen

> [!warning]- Afschrijving spreidt de KOST in de RR, NIET de waarde van het actief
> ⚠️ Afschrijving spreidt de KOST in de RR, NIET de waarde van het actief. De boekwaarde op de balans is een afgeleide. Stoppen met afschrijven 'omdat het actief eigenlijk niet zoveel waard meer is' is een fout — dat hoort via niet-recurrente afschrijving of waardevermindering. 🤖
>
> _Bron: KB WVV art. 3:23_



## Zie ook

- **Vereist kennis van**: [[aanschaffingswaarde]]

## Voorbeelden

Naaiatelier Ninove BV koopt een snij-installatie voor € 30.500 met geschatte gebruiksduur van 5 jaar. Lineaire afschrijving = € 30.500 / 5 = € 6.100 per jaar. Eind jaar 1: Debet 6302 Afschrijvingen materiële vaste activa € 6.100 / Credit 2309 Afschrijvingen op installaties € 6.100. Op de balans staat de netto-boekwaarde aan eind jaar 1 op € 30.500 − € 6.100 = € 24.400.

## Bronnen

[^1]: `KB-WVV-2019__art_3_18`
[^2]: `CBN-2010-15-afschrijvingsmethoden__sec_algemeen`
[^3]: `CBN-2010-15-afschrijvingsmethoden__sec_immateri-le-en-materi-le-vaste-activa-met-beperkte-gebruiksd`
[^4]: `CBN-2019-04-gevolgen-op-gebied-van-financiele-rapportering-als-gevolg-van-de-bre__sec_afwaardering-van-vlottende-en-vaste-activa`
[^5]: `CBN-2010-15-afschrijvingsmethoden__sec_af-te-schrijven-waarde`
[^6]: `CBN-2021-09-rekening-26-overige-materiele-vaste-activa__sec_waarderingsregels-waardeverminderingen-en-afschrijvingen`
