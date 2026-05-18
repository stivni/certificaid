---
title: Oprichtingskosten
tags:
- concept
- cluster
- po-1-1
- po-1-2
linked_anchors:
- 1.1.II.A
- 1.1.II.B
- 1.2.V.B
programmaonderdelen:
- '1.1'
- '1.2'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/oprichtingskosten.json
gegenereerd_op: '2026-05-18'
---
# Oprichtingskosten ⚖️

> [!summary] Korte inhoud
> Kosten verbonden met de **oprichting, verdere ontwikkeling of herstructurering** van een vennootschap, in het bijzonder: (a) kosten van oprichting of kapitaalverhoging (notariskosten, registratierechten, advies), (b) kosten bij uitgifte van leningen (bankkosten, noteringskosten,….

Kosten verbonden met de **oprichting, verdere ontwikkeling of herstructurering** van een vennootschap, in het bijzonder: (a) kosten van oprichting of kapitaalverhoging (notariskosten, registratierechten, advies), (b) kosten bij uitgifte van leningen (bankkosten, noteringskosten, publicatiekosten bij obligatieleningen), (c) herstructureringskosten met duurzame impact op rentabiliteit. De onderneming kan **kiezen** ze als kost te boeken in het jaar zelf, OF ze te activeren onder rubriek 20 'Oprichtingskosten' aan de actiefzijde van de balans en af te schrijven over **minstens 5 jaar** (jaarlijkse tranche ≥ 20 %; KB WVV art. 3:36 + 3:37).

_Bron: KB WVV art. 3:36 jo. art. 3:37_


## Bouwstenen

### Keuze: kost of activeren ⚖️

Twee mogelijkheden: (1) de oprichtingskost meteen ten laste nemen in het boekjaar zelf (klasse 6 of 61), of (2) activeren op klasse 20 en spreiden in de tijd via afschrijving. De keuze maakt de onderneming bij de boeking.

**Waarom?** Activeren spreidt de kost over meerdere jaren waarin de onderneming de baten geniet (matching). Meteen ten laste nemen is conservatiever en transparanter. Beide zijn toegelaten.


_Grondslag: KB WVV art. 3:36_

### Minimaal 20 % afschrijving per jaar ⚖️

Geactiveerde oprichtingskosten worden afgeschreven per jaarlijkse tranches van **minstens 20 %** van de werkelijk uitgegeven bedragen. In de praktijk: lineair over 5 jaar of korter, niet over langer dan 5 jaar.

**Waarom?** Oprichtingskosten hebben geen tastbare onderliggende waarde die jaren mee gaat. De wetgever forceert een snelle afbouw om geen 'spookactivum' lang op de balans te houden.


_Grondslag: KB WVV art. 3:37_

### Uitzondering: kosten uitgifte van leningen ⚖️

Kosten bij de uitgifte van een lening (obligatielening, bankkosten, noteringskosten) mogen worden afgeschreven **over de volledige looptijd van de lening** — ook als die langer is dan 5 jaar.

**Waarom?** Uitgiftekosten hebben een direct verband met de lening waarvan de looptijd vastligt; matching met de rentelast over de hele looptijd is logischer dan een geforceerde 5-jaars-afschrijving.


_Grondslag: KB WVV art. 3:37, tweede zin_

### Herstructureringskosten — strikte voorwaarden ⚖️

Herstructureringskosten mogen alleen worden geactiveerd als: (1) het gaat om welbepaalde kosten verbonden met een ingrijpende wijziging in structuur of organisatie, EN (2) ze ertoe strekken een **gunstige en duurzame invloed** te hebben op de rentabiliteit. Motivering in de toelichting is verplicht.

**Waarom?** Zonder strikte voorwaarden zou elke kost als 'herstructurering' kunnen worden afgevoerd naar de balans — wat het resultaat artificieel zou opkrikken. De wetgever beperkt dit tot duidelijk-duurzame ingrepen.


_Grondslag: KB WVV art. 3:36, tweede zin; CBN 2011/24_

### Aftrek van bedrijfs- of financiële kosten — zichtbaarheid ⚖️

Wanneer herstructureringskosten met het karakter van bedrijfskosten/financiële kosten worden geactiveerd, gebeurt dat door ze 'op zichtbare wijze in mindering te brengen' van het totaal van die kosten in de resultatenrekening.

**Waarom?** De gebruiker mag niet misleid worden door een artificieel verlaagde kostenlijn; het effect moet expliciet zichtbaar zijn naast de bruto-kosten.


_Grondslag: KB WVV art. 3:36, derde zin_


## Berekening

### Afschrijvingsschema oprichtingskosten

**Jaarlijkse afschrijving op klassieke oprichtingskosten** 
```
jaarlijkse afschrijving = werkelijk uitgegeven bedrag × afschrijvingspercentage (≥ 20 %)
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `werkelijk uitgegeven bedrag` | Som van de geactiveerde oprichtingskosten | EUR |
| `afschrijvingspercentage` | Gekozen percentage, minstens 20 % per jaar | % |

**Voorbeeld-invulling**: Oprichtingen Oostende BV: € 5.600 × 20 %

```
€ 5.600 × 20 % = € 1.120 per jaar gedurende 5 jaar
```

_Resultaat in EUR_
**Afschrijving op kosten bij uitgifte van leningen** 
```
jaarlijkse afschrijving = uitgiftekosten / looptijd lening (in jaren)
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `uitgiftekosten` | Bankkosten, noteringskosten, publicatiekosten bij uitgifte lening/obligatie | EUR |
| `looptijd lening` | Volledige looptijd van de onderliggende lening | jaar |

**Voorbeeld-invulling**: Uitgiftekosten = € 12.000; looptijd = 8 jaar

```
€ 12.000 / 8 = € 1.500 per jaar
```

_Resultaat in EUR_
*Standaard 20 % per jaar over 5 jaar; voor uitgiftekosten van leningen mag spreiding over de looptijd.*

### 1. Bepaal het te activeren bedrag

Som alle kosten die voldoen aan de definitie van oprichtingskosten (oprichting, kapitaalverhoging, uitgifte leningen, herstructurering met duurzame impact).

**Waarom?** Niet alle 'eerste kosten' van een vennootschap zijn activeerbaar — alleen welbepaalde categorieën met substantiële economische impact.

**🛠️ Hoe**:

1. Verzamel facturen: notariskosten, advies, registratierechten, bankkosten lening, publicatiekosten.
2. Sluit uit: routine-bedrijfskosten (lonen eerste maanden, kantoorkosten), die zijn klasse 6.
3. Som = activeerbaar bedrag.


**Grondslag**: KB WVV art. 3:36

### 2. Stel het afschrijvingsplan op

Bepaal afschrijvingsduur (minstens 20 %/jaar = max 5 jaar voor normale oprichtingskosten; tot looptijd voor uitgiftekosten leningen).

**Waarom?** Een formeel plan is nodig voor consistentie tussen jaren en als voorwerp van controle.

**📥 Input**:
- Boekhouding 20X1 → **Geactiveerd bedrag** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Afschrijvingsplan oprichtingskosten → **Jaarlijkse tranche** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Klassieke oprichtingskosten: lineair 20 % over 5 jaar.
2. Bij snellere afbouw mogelijk: 25 %, 33 %, of zelfs 100 % in jaar 1.
3. Uitgiftekosten leningen: looptijd van de lening (bv. 10 jaar → 10 %/jaar).


> [!example]- Voorbeeld: Oprichtingen Oostende BV activeert € 5.600 oprichtingskosten + € 12.000 uitgiftekosten van een 8-jarige bedrijfslening
> Oprichtingen Oostende BV activeert € 5.600 oprichtingskosten + € 12.000 uitgiftekosten van een 8-jarige bedrijfslening.
>
> 1. **Afschrijvingsplan** 🧮
>
>    | Rubriek                          | Te activeren | Termijn | Jaarlijks |
>    |----------------------------------|-------------:|---------|----------:|
>    | 200 Kosten oprichting/kap        |    € 5.600   | 5 jaar  | € 1.120   |
>    | 201 Kosten uitgifte lening       |   € 12.000   | 8 jaar  | € 1.500   |
>    | **Totaal jaarlijkse afschrijving** | **€ 17.600** |        | **€ 2.620** |
>
> 2. **Boeking eind jaar 1** 📝
>
>    Debet 6300 Afschrijvingen oprichtingskosten € 2.620
>      Credit 2009 Afschrijvingen op kosten oprichting/kap € 1.120
>      Credit 2019 Afschrijvingen op kosten uitgifte leningen € 1.500
>    (Som debet = som credit ✓)
>

**Grondslag**: KB WVV art. 3:37

**Voorbeeld**: Oprichtingen Oostende BV maakt bij oprichting € 5.600 aan notaris- en advieskosten en geeft tegelijk een 8-jarige obligatielening uit met uitgiftekosten € 12.000.

```
Klassieke oprichtingskosten € 5.600: max 5 jaar afschrijving → € 1.120/jaar. Uitgiftekosten lening € 12.000: spreiding over 8 jaar (looptijd) → € 1.500/jaar. Totale jaarlijkse afschrijving = € 2.620.
```

Resultaat: Op de balans staat in jaar 1 onder rubriek 20: aanschaffingswaarde € 17.600 minus afschrijving € 2.620 = nettowaarde € 14.980. In de resultatenrekening rekening 6300 'Afschrijvingen oprichtingskosten' = € 2.620.

## In de praktijk

<h3 id="rubrieken-in-mar-klasse-20">Rubrieken in MAR (klasse 20)</h3>

> [!tip]- Rubrieken in MAR (klasse 20)
> Rekening 200 'Kosten van oprichting en kapitaalverhoging', 201 'Kosten bij uitgifte van leningen', 202 'Overige oprichtingskosten', 204 'Herstructureringskosten'. Bijhorende afschrijvingsrekeningen 2009, 2019, 2029, 2049 (eindigend op 9 = afschrijvingen/waardeverminderingen). ⚖️

> [!tip]- Herkennen op het examen
> Examen: kostentype bepaalt subrekening — notariskosten oprichting → 200; uitgiftekosten obligatielening → 201; herstructureringskosten → 204.


> [!info]- Niet verwarren met [[immateriele-vaste-activa]]
> Oprichtingskosten (rubriek 20) = kosten verbonden met het bestaan/de structuur van de vennootschap; afschrijving min. 20 %/jaar. Immateriële vaste activa (rubriek 21) = identificeerbare niet-monetaire activa zonder fysieke substantie (concessies, octrooien, goodwill); afschrijving over geschatte gebruiksduur, niet beperkt tot 5 jaar.
>
> _Trigger_: Examen: 'patentaankoop voor € 80.000' → immaterieel vast actief (rubr. 21), NIET oprichtingskosten.


## Valkuilen

> [!warning]- Niet alle 'eerste kosten' van een vennootschap zijn oprichtingskosten
> ⚠️ Niet alle 'eerste kosten' van een vennootschap zijn oprichtingskosten. Lopende werkingskosten (lonen, huur, ICT) blijven gewone bedrijfskosten — ook in jaar 1. Activering geldt alleen voor specifiek welomschreven categorieën uit KB WVV art. 3:36. ⚖️
>
> _Bron: KB WVV art. 3:36_


> [!warning]- Herstructureringskosten activeren = motivering verplicht in toelichting
> ⚠️ Herstructureringskosten activeren = motivering verplicht in toelichting. Zonder onderbouwde duurzame rentabiliteitsimpact: meteen kost boeken, geen activering. ⚖️
>
> _Bron: CBN 2011/24_



## Zie ook

- **Getriggerd door**: [[obligatielening]]

## Bronnen

[^1]: `KB-WVV-2019__art_3_30`
[^2]: `KB-WVV-2019__art_3_31`
[^3]: `CBN-2010-15-afschrijvingsmethoden__sec_oprichtingskosten`
[^4]: `CBN-2019-07-boekhoudkundige-verwerking-van-de-uitgifte-van-een-obligatielening__sec_kosten-bij-uitgifte-van-leningen`
[^5]: `CBN-2011-24-herstructureringskosten-verwerking-in-de-jaarrekening__volledig`
[^6]: `MAR-ondernemingen__art_2`
