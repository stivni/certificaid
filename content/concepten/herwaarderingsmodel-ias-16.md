---
title: Herwaarderingsmodel onder IAS 16
tags:
- concept
- methode
- po-1-5
linked_anchors:
- 1.5.V.A
- 1.5.V
programmaonderdelen:
- '1.5'
confidence: grounded
node_type: methode
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/herwaarderingsmodel-ias-16.json
gegenereerd_op: '2026-05-18'
---
# Herwaarderingsmodel onder IAS 16 ⚖️

> [!summary] Korte inhoud
> Het herwaarderingsmodel (IAS 16 alinea 31) waardeert materiële vaste activa **na eerste opname tegen geherwaardeerde waarde**: de reële waarde op de datum van herwaardering, verminderd met latere geaccumuleerde afschrijvingen en bijzondere waardeverminderingsverliezen.

> [!info] Behoort tot: [[materiele-vaste-activa-ifrs]]

Het herwaarderingsmodel (IAS 16 alinea 31) waardeert materiële vaste activa **na eerste opname tegen geherwaardeerde waarde**: de reële waarde op de datum van herwaardering, verminderd met latere geaccumuleerde afschrijvingen en bijzondere waardeverminderingsverliezen. Doel: gebruikers van de jaarrekening een actueler beeld geven van de werkelijke economische waarde van het bedrijfskapitaal, in plaats van vast te houden aan historische kostprijs die snel verouderd kan zijn. Het model is een **alternatief** voor het kostprijsmodel; een entiteit kiest per categorie materiële vaste activa welk van beide ze toepast.

_Bron: IAS 16 alinea 31_


## Bouwstenen

### Stijging — naar OCI (herwaarderingsreserve) ⚖️

Wanneer de boekwaarde van een actief **stijgt** als gevolg van een herwaardering, neem je de stijging op in **overige onderdelen van het totaalresultaat** (OCI) en verwerk je ze in het eigen vermogen als **herwaarderingsreserve**. Uitzondering: als de stijging een eerdere herwaarderingsafname tegengaat die in winst of verlies was opgenomen, gaat ze tot dat bedrag in winst of verlies (en het saldo in OCI).

**Waarom?** Een herwaarderings-uplift is een niet-gerealiseerde meerwaarde. Ze meteen als winst boeken zou de gebruiker misleiden — de winst bestaat alleen op papier zolang het actief niet verkocht is. OCI parkeert ze tot realisatie of vervreemding.

**Voorbeeld**: Zelena Bio NV's terreinen op 1 januari 2026: boekwaarde € 12.000.000. Reële waarde uit taxatie: € 18.000.000. Herwaardering +€ 6.000.000 → OCI → herwaarderingsreserve. Eigen vermogen stijgt met € 6.000.000 (minus uitgestelde belasting volgens IAS 12).

_Grondslag: IAS 16 alinea 39_

### Daling — naar winst of verlies ⚖️

Wanneer de boekwaarde **daalt** door herwaardering, neem je de afname op in winst of verlies. Uitzondering: voor zover er voor dat actief een creditsaldo aan herwaarderingsreserve bestaat (uit eerdere uplift), gaat de afname tot dat bedrag eerst in OCI (verminderen reserve), pas het excedent in winst of verlies.

**Waarom?** Symmetrisch tegengesteld aan de stijging-regel: een waardedaling die nog door eerdere reserve gedekt is, hoort niet onmiddellijk het resultaat te belasten. Pas wanneer de reserve op is, treft het verlies daadwerkelijk de winst.

**Voorbeeld**: Op 31 december 2030 vertonen Zelena's terreinen door regionale crisis een reële waarde van € 14.000.000 (was € 18.000.000). Daling −€ 4.000.000. Herwaarderingsreserve had nog € 6.000.000 → afname gaat volledig naar OCI (reserve daalt naar € 2.000.000). Geen effect op winst of verlies 2030.

_Grondslag: IAS 16 alinea 40_

### Frequentie van herwaardering ⚖️

Herwaarderen moet '**voldoende regelmatig**' zodat de boekwaarde niet beduidend afwijkt van de reële waarde aan het eind van de verslagperiode. Concreet: jaarlijks bij volatiele markten; om de 3 à 5 jaar bij stabiele markten (alinea 34). Bij voortschrijdende herwaardering binnen een categorie: korte periode, recente waarden.

**Waarom?** Een herwaardering uit 2015 die je vandaag nog gebruikt zegt niets over de actuele reële waarde. De frequentie-eis voorkomt dat het model uitgehold wordt door verouderde taxaties.

**Voorbeeld**: Zelena Bio kiest jaarlijkse herwaardering voor terreinen in stedelijk gebied (volatiele vastgoedmarkt) en driejaarlijkse herwaardering voor terreinen in landelijke productiezones (stabiele markt).

_Grondslag: IAS 16 alinea 34_

### Volledige categorie — geen cherry-picking ⚖️

De keuze voor het herwaarderingsmodel geldt voor **alle activa binnen een categorie** (alinea 36). Categorieën zijn gegroepeerd naar gelijksoortige aard en gebruik: grond, terreinen en gebouwen, machines, schepen, vliegtuigen, motorvoertuigen, meubilair, kantoorinrichting, vruchtdragende planten.

**Waarom?** Selectief enkele activa herwaarderen zou de mooie activa optillen en de minder mooie achterlaten — cherry-picking ten gunste van het management. Categorie-brede toepassing voorkomt dat.

**Voorbeeld**: Zelena Bio mag NIET alleen haar terrein in Brussel herwaarderen (met fraaie uplift) en haar andere terreinen (met dalende waarde) op kostprijs houden. Ofwel ALLE terreinen aan het herwaarderingsmodel, ofwel geen enkel.

_Grondslag: IAS 16 alinea 36-37_

### Realisatie herwaarderingsreserve — naar ingehouden winsten ⚖️

De herwaarderingsreserve mag direct naar **ingehouden winsten** worden overgeboekt zodra het actief niet langer wordt opgenomen (verkocht, buiten gebruik gesteld, vervreemd). Optioneel ook gedurende het gebruik: het verschil tussen afschrijving op geherwaardeerde waarde en afschrijving op oorspronkelijke kostprijs mag jaarlijks worden overgeboekt. Deze transfer gaat NIET via winst of verlies.

**Waarom?** Een gerealiseerde herwaardering (via verkoop) hoort niet meer in OCI te staan. Maar omdat ze in geen enkel stadium via winst-of-verlies is gegaan, gaat ze rechtstreeks naar ingehouden winsten.

**Voorbeeld**: Zelena Bio verkoopt in 2032 het Brusselse terrein voor € 22.000.000 (geherwaardeerde boekwaarde € 18.000.000). Realisatiewinst € 4.000.000 in winst of verlies. Daarnaast: de openstaande herwaarderingsreserve voor dat terrein (€ 6.000.000) wordt overgeboekt naar ingehouden winsten — NIET in resultaat.

_Grondslag: IAS 16 alinea 41_


## Berekening

### Berekening herwaarderingsverschil

**Herwaarderingsverschil** 
```
herwaardering = reële waarde op herwaarderingsdatum − boekwaarde vóór herwaardering
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `reële waarde op herwaarderingsdatum` | Marktwaarde, typisch bepaald door externe taxateur volgens IFRS 13 | EUR |
| `boekwaarde vóór herwaardering` | Kostprijs of vorige geherwaardeerde waarde, na geaccumuleerde afschrijvingen en impairments | EUR |

**Voorbeeld-invulling**: reële waarde Zelena Bio's Brusselse terrein op 1 januari 2026 = € 18.000.000; boekwaarde vóór herwaardering (= aanschaffingsprijs, terrein wordt niet afgeschreven) = € 12.000.000

```
€ 18.000.000 − € 12.000.000 = € 6.000.000 (positief → OCI, herwaarderingsreserve)
```

_Resultaat in EUR_
*Trek de boekwaarde vóór herwaardering af van de nieuwe reële waarde. Het verschil is de herwaardering.*


## Valkuilen

> [!warning]- Bij stijging na eerdere daling: niet automatisch alles in OCI
> ⚠️ Bij stijging na eerdere daling: niet automatisch alles in OCI. Het deel dat een eerdere afname-in-winst-of-verlies tegengaat, gaat **eerst** in winst of verlies (alinea 39). Pas het excedent gaat naar OCI. ⚖️
>
> _Bron: IAS 16 alinea 39_


> [!warning]- Reële waarde-bepaling moet voldoen aan IFRS 13 — niet zomaar elke schatting volstaat
> ⚠️ Reële waarde-bepaling moet voldoen aan IFRS 13 — niet zomaar elke schatting volstaat. Hiërarchie: niveau 1 (gequoteerde prijzen actieve markt) > niveau 2 (waarneembare inputs) > niveau 3 (niet-waarneembare inputs). Voor terreinen typisch een onafhankelijke taxatie (niveau 3 of 2). ⚖️
>
> _Bron: IFRS 13_



## Bronnen

[^1]: `IAS-16-materiele-vaste-activa__sec_waardering-na-eerste-opname`
