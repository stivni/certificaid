---
title: Verschillenboekhouding
tags:
- concept
- methode
- po-1-8
linked_anchors:
- 1.8.VI
- 1.8.VI.D
- 1.8.III.C
programmaonderdelen:
- '1.8'
confidence: inferred
node_type: methode
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/verschillenboekhouding.json
gegenereerd_op: '2026-05-17'
---
# Verschillenboekhouding 🤖

> [!summary] Korte inhoud
> Verschillenboekhouding (variance accounting) registreert systematisch het verschil tussen werkelijke kost en budget- of standaardkost, en splitst dat verschil in oorzaakcomponenten (prijsverschil, hoeveelheidverschil, mix-verschil, efficiëntieverschil).

> [!info] Behoort tot: [[budgetbeheer]]

Verschillenboekhouding (variance accounting) registreert systematisch het verschil tussen werkelijke kost en budget- of standaardkost, en splitst dat verschil in oorzaakcomponenten (prijsverschil, hoeveelheidverschil, mix-verschil, efficiëntieverschil). Doel: snel lokaliseren waar afwijkingen vandaan komen om gericht bij te sturen.

_Bron: Management accounting — bron-gap_


## Bouwstenen

### Prijsverschil vs. hoeveelheidverschil 🤖

Voor materiaal en arbeid splitsen we het totaal verschil in: prijsverschil = werkelijke hoeveelheid × (werkelijke prijs − standaardprijs); hoeveelheidverschil = (werkelijke hoeveelheid − standaardhoeveelheid) × standaardprijs.

**Waarom?** Prijsverschil wijst op aankoop-/markt-oorzaak; hoeveelheidverschil op productie-efficiëntie.

**Voorbeeld**: Yperse Werkplaats BV partij 100 tapijten: standaard 1,2 kg wol × € 5,00 = € 6 per tapijt. Werkelijk: 1,3 kg × € 5,20. Per tapijt: prijsverschil = 1,3 × (5,20 − 5,00) = € 0,26 (ongunstig). Hoeveelheidverschil = (1,3 − 1,2) × € 5,00 = € 0,50 (ongunstig). Voor 100 tapijten: € 26 prijs + € 50 hoeveelheid = € 76 ongunstig totaal.


### Boeking van verschillen 🤖

Verschillen worden op aparte rekeningen geboekt (klasse 9, bv. 980 materiaal-prijsverschil, 981 arbeid-tariefverschil, 985 hoeveelheidverschil). Aan jaareinde wordt het saldo ofwel naar de resultatenrekening overgeboekt ofwel aan de voorraad/COGS toegerekend.

**Waarom?** Aparte rekeningen maken cumulatieve trend zichtbaar en faciliteren maand-afsluiting.

**Voorbeeld**: Yperse boeking maart 20X2: 9300 Confectie € 92.000 / 612 'Werkelijke kost Confectie' € 79.167 + 9810 Verschil Confectie € 12.833.


### Significantiegrens 🤖

Niet elk verschil hoeft onderzocht. Praktijk: drempel van bv. 5 % of € 5.000; alleen daarboven gericht onderzoek (Management by Exception).

**Waarom?** Vermijdt dat controlling-team verzandt in micro-afwijkingen.

**Voorbeeld**: Yperse hanteert: verschil > 10 % en > € 2.500 = onderzoek. Confectie € 12.833 op € 79.167 = 16,2 % → onderzoek. Spinnerij € 850 verschil op budget € 120.000 = 0,7 % → geen onderzoek.



## Berekening

### Prijs- en hoeveelheidverschil

**Prijsverschil** 
```
prijsverschil = werkelijke hoeveelheid × (werkelijke prijs − standaardprijs)
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `werkelijke hoeveelheid` | Werkelijk verbruik | kg of uur |
| `werkelijke prijs` | Werkelijke prijs/tarief per eenheid | EUR/kg of EUR/uur |
| `standaardprijs` | Vooraf vastgelegde standaardprijs | EUR/kg of EUR/uur |

**Voorbeeld-invulling**: Yperse partij 100 tapijten: werkelijk 130 kg wol, werkelijke prijs € 5,20/kg, standaardprijs € 5,00/kg

```
130 × (5,20 − 5,00) = 130 × 0,20 = € 26 (ongunstig)
```

_Resultaat in EUR_
**Hoeveelheidverschil** (volgt op: prijsverschil)
```
hoeveelheidverschil = (werkelijke hoeveelheid − standaardhoeveelheid) × standaardprijs
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `werkelijke hoeveelheid` | Werkelijk verbruik | kg of uur |
| `standaardhoeveelheid` | Standaardverbruik voor werkelijke productie | kg of uur |
| `standaardprijs` | Standaardprijs per eenheid | EUR/kg of EUR/uur |

**Voorbeeld-invulling**: Yperse: werkelijk 130 kg, standaard 100 tapijten × 1,2 kg = 120 kg, standaardprijs € 5,00

```
(130 − 120) × 5,00 = 10 × 5,00 = € 50 (ongunstig)
```

_Resultaat in EUR_
*Splits het totaal verschil in 'wat is duurder geworden?' (prijsverschil) en 'wat hebben we meer/minder gebruikt?' (hoeveelheidverschil).*

**Voorbeeld**: Yperse Werkplaats BV produceert in mei 20X2 een partij van 100 tapijten. Standaard: 1,2 kg wol/tapijt aan € 5,00/kg. Werkelijk: 130 kg wol verbruikt aan € 5,20/kg.

```
Prijsverschil = 130 × (5,20 − 5,00) = € 26 ongunstig. Hoeveelheidverschil = (130 − 120) × 5,00 = € 50 ongunstig. Totaal materiaal-verschil = € 76 ongunstig.
```

Resultaat: € 76 ongunstig totaal, waarvan € 26 te wijten aan duurdere aankoop (verantwoordelijkheid inkoop) en € 50 aan inefficiënt gebruik (verantwoordelijkheid productie).

## Valkuilen

> [!warning]- Standaardhoeveelheid moet altijd berekend worden voor de werkelijke productie, niet voor de geplande
> ⚠️ Standaardhoeveelheid moet altijd berekend worden voor de werkelijke productie, niet voor de geplande. Voorbeeld: gepland 80 tapijten, werkelijk 100 → standaardhoeveelheid is 100 × 1,2 kg = 120 kg, niet 80 × 1,2 = 96 kg. Anders mix je volume-verschil met efficiëntie-verschil. 🤖


> [!warning]- Een ongunstig prijsverschil bij materiaal kan een gunstig hoeveelheidverschil veroorzaken (betere kwaliteit, minder verlies)
> ⚠️ Een ongunstig prijsverschil bij materiaal kan een gunstig hoeveelheidverschil veroorzaken (betere kwaliteit, minder verlies). Beide componenten samen interpreteren — niet apart oordelen. 🤖



## Zie ook

- **Vereist kennis van**: [[voorbepaalde-kosten]]

