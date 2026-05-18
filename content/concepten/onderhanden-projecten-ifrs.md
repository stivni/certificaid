---
title: Onderhanden projecten in opdracht van derden — onder IFRS 15
tags:
- concept
- regel
- po-1-5
linked_anchors:
- 1.5.V.E
- 1.5.V.D
- 1.5.V
programmaonderdelen:
- '1.5'
confidence: grounded
node_type: regel
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/onderhanden-projecten-ifrs.json
gegenereerd_op: '2026-05-18'
---
# Onderhanden projecten in opdracht van derden — onder IFRS 15 ⚖️

> [!summary] Korte inhoud
> Sinds de inwerkingtreding van IFRS 15 op 1 januari 2018 is IAS 11 — Construction Contracts ingetrokken. **Onderhanden projecten in opdracht van derden** (bouwprojecten, infrastructuurprojecten, specifiek-gemaakte goederen of diensten) vallen nu onder de algemene regel van IFRS 15.

> [!info] Behoort tot: [[opbrengsten-ifrs]]

Sinds de inwerkingtreding van IFRS 15 op 1 januari 2018 is IAS 11 — Construction Contracts ingetrokken. **Onderhanden projecten in opdracht van derden** (bouwprojecten, infrastructuurprojecten, specifiek-gemaakte goederen of diensten) vallen nu onder de algemene regel van IFRS 15. De kernvraag wordt: voldoet de prestatieverplichting aan de criteria van **opname over een periode** (alinea 35)? Drie criteria, waarvan minstens één moet vervuld zijn: (a) klant ontvangt en consumeert gelijktijdig de voordelen naarmate de entiteit presteert; (b) prestaties creëren of versterken een actief waarover de klant zeggenschap heeft naarmate dat actief wordt gecreëerd of versterkt; (c) prestaties creëren geen actief met een alternatieve gebruiksmogelijkheid voor de entiteit én de entiteit heeft een afdwingbaar recht op betaling voor reeds verrichte prestaties. Bij vervulling over een periode: opbrengstopname via een **outputmethode** (geleverde eenheden, mijlpalen) of **inputmethode** (kosten gemaakt / totaal verwachte kosten; gewerkte uren) — alinea 41 + B14-B19. Voor de vroegere IAS 11-techniek (percentage-of-completion via kosten-input) gaat in essentie de inputmethode.

_Bron: IFRS 15 alinea 35-37 + 41_


## Bouwstenen

### Outputmethode versus inputmethode ⚖️

**Outputmethode** (alinea B15): opbrengstopname op basis van waarde voor de klant van de tot dusver overgedragen goederen/diensten — bv. opgeleverde mijlpalen, geïnstalleerde eenheden, gefactureerde projectresultaten. **Inputmethode** (alinea B18): op basis van entiteits-inputs in verhouding tot totaal verwachte inputs — bv. kosten gemaakt / totale verwachte kosten, gewerkte uren / totaal verwachte uren.

**Waarom?** Outputmethode is theoretisch zuiverder (klantperspectief) maar vereist meetbare outputmijlpalen. Inputmethode is praktischer wanneer prestaties gelijkmatig over de tijd lopen — bv. bouwprojecten met diffuse output.

**Voorbeeld**: Cattoir's productie-eenheid bouwen voor Zelena Bio: prestaties zijn gelijkmatig en complex; outputmijlpalen zijn moeilijk objectief te identificeren. → Inputmethode (kosten gemaakt). Voor een rijwegproject waarbij elke afgewerkte 100 m oplevering = betaling: outputmethode (kilometer opgeleverd) is logischer.

_Grondslag: IFRS 15 alinea B15 + B18_

### Verwacht verlies — onmiddellijk opnemen 🤖

Wanneer de **totale verwachte kosten** van het contract hoger zijn dan de **totale transactieprijs**, ontstaat een verwacht verlies. Onder IFRS 15 wordt het verlies opgenomen via IAS 37 (onerous contracts) of via de gewone IFRS 15-opname, niet apart als 'voorziening'. Het netto-effect: de boekhoudkundige opname van het verlies gebeurt zodra het verlies waarschijnlijk en betrouwbaar schatbaar is — niet pas bij opleveringen.

**Waarom?** Voorzichtigheidsbeginsel: een verwacht verlies in een lopend contract is een actuele economische realiteit. Wachten tot het project klaar is zou de winst van de tussenliggende jaren artificieel hoog houden.

**Voorbeeld**: Cattoir's contract met Zelena Bio: transactieprijs € 4.500.000, totaal verwachte kosten € 4.900.000 (oorspronkelijk € 4.200.000, gestegen door materiaalprijzen). Verwacht verlies € 400.000 → onmiddellijk opgenomen in W&V, niet gewacht tot eindoplevering.

_Grondslag: IAS 37 onerous contracts + IFRS 15_

### Niet-meetbare voortgang — alleen kosten goedmaken ⚖️

Als een entiteit haar voortgang niet redelijkerwijs kan meten (vroege fase contract, te grote onzekerheid), maar zij verwacht wel de gemaakte kosten goed te maken: opbrengstopname **overeenkomstig de gemaakte kosten** totdat voortgang redelijk meetbaar wordt (alinea 45). Dat geeft een nul-marge tijdens de onzekere fase.

**Waarom?** Geen winst boeken zolang voortgang niet meetbaar is — anders zou de winst kunstmatig geconstrueerd zijn. Maar ook geen verlies tonen als de kosten gedekt zullen worden — daarom: opbrengst = kost.

**Voorbeeld**: Cattoir's eerste 3 maanden van het Zelena-project: design-fase, hoge onzekerheid over totale kosten. Kosten gemaakt € 350.000. Opbrengstopname = € 350.000 (nul-marge). Vanaf maand 4 wordt voortgang meetbaar → reguliere percentage-of-completion methode.

_Grondslag: IFRS 15 alinea 45_


## Berekening

### Percentage-of-completion via inputmethode (kosten)

**Voortgangspercentage** 
```
voortgangspercentage = kosten gemaakt tot dusver / totaal verwachte kosten
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `kosten gemaakt tot dusver` | Cumulatief gemaakte kosten van contractuitvoering | EUR |
| `totaal verwachte kosten` | Som verwachte kosten over hele contractduur (regelmatig herzien) | EUR |

**Voorbeeld-invulling**: Cattoir's contract met Zelena Bio op 31 december 2026: kosten gemaakt € 2.700.000; totaal verwachte kosten € 4.500.000

```
€ 2.700.000 / € 4.500.000 = 60%
```

_Resultaat in %_
**Cumulatieve opbrengstopname** (volgt op: voortgangspercentage)
```
cumulatieve opbrengst = voortgangspercentage × totale transactieprijs
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `voortgangspercentage` | Resultaat vorige formule | % |
| `totale transactieprijs` | Vergoeding waarop entiteit recht heeft | EUR |

**Voorbeeld-invulling**: voortgangspercentage = 60%; totale transactieprijs = € 4.500.000

```
60% × € 4.500.000 = € 2.700.000 cumulatief opgenomen opbrengst
```

_Resultaat in EUR_
**Opbrengst van de periode** (volgt op: opbrengstopname-tot-dusver)
```
opbrengst periode = cumulatieve opbrengst eind − cumulatieve opbrengst begin
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `cumulatieve opbrengst eind` | Cumulatieve opbrengst tot einde van huidige periode | EUR |
| `cumulatieve opbrengst begin` | Cumulatieve opbrengst tot einde van vorige periode | EUR |

**Voorbeeld-invulling**: Cattoir: cumulatieve opbrengst 31 december 2026 = € 2.700.000; cumulatieve opbrengst 31 december 2025 = € 1.080.000 (voortgang 24% × € 4.500.000)

```
€ 2.700.000 − € 1.080.000 = € 1.620.000 opbrengst boekjaar 2026
```

_Resultaat in EUR_

> [!info]- Niet verwarren met [[voorraden-ifrs]]
> Voorraden (IAS 2) zijn activa aangehouden voor verkoop in de NORMALE bedrijfsvoering — generieke producten. Onderhanden projecten in opdracht van derden (nu IFRS 15) zijn klant-specifieke prestaties waar opbrengstopname over een periode gebeurt onder strikte criteria. Een product op voorraad voor algemene verkoop = IAS 2; een gebouw in opdracht van een specifieke klant = IFRS 15-PO over periode.
>
> _Trigger_: Examen: 'Klant-specifiek project' → IFRS 15 over periode (mits criterium b of c vervuld); 'algemene voorraad voor verkoop' → IAS 2.


## Valkuilen

> [!warning]- Niet automatisch elk bouwproject is opname over periode
> ⚠️ Niet automatisch elk bouwproject is opname over periode. Toets de drie criteria van alinea 35. Een speculatief residentieel bouwproject zonder specifieke koper (entiteit bouwt voor eigen rekening en zoekt later koper) voldoet typisch NIET aan de over-periode-criteria → opbrengstopname pas bij verkoop. ⚖️
>
> _Bron: IFRS 15 alinea 35-37_


> [!warning]- De inputmethode 'kosten gemaakt' moet inputs uitsluiten die geen vooruitgang reflecteren
> ⚠️ De inputmethode 'kosten gemaakt' moet inputs uitsluiten die geen vooruitgang reflecteren. Bv. een grote voorraad materialen ingekocht maar nog niet verwerkt mag NIET als gemaakte kost in de teller — dat zou voortgang overschatten (alinea B19). ⚖️
>
> _Bron: IFRS 15 alinea B19_


> [!warning]- Totaal verwachte kosten worden **periodiek herzien**
> ⚠️ Totaal verwachte kosten worden **periodiek herzien**. Een kostenstijging (materiaalprijzen, vertragingen) leidt tot een lager voortgangspercentage — en dus mogelijk een terugneming van eerder geboekte opbrengst in het lopende boekjaar (cumulatieve inhaal). ⚖️
>
> _Bron: IFRS 15 alinea 43_



## Bronnen

[^1]: `IFRS-15-opbrengsten-van-contracten-met-klanten__sec_opname`
