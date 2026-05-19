---
title: Werkkapitaalbehoefte (besoin en fonds de roulement, BFR)
tags:
- concept
- begrip
- po-1-3
linked_anchors:
- 1.3.II.C
- 1.3.taak.1
programmaonderdelen:
- '1.3'
confidence: inferred
node_type: begrip
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/werkkapitaalbehoefte.json
gegenereerd_op: '2026-05-18'
---
# Werkkapitaalbehoefte (besoin en fonds de roulement, BFR) 🤖

Werkkapitaalbehoefte = (voorraden + handelsvorderingen) − handelsschulden. Het meet hoeveel cash de operationele cyclus zelf vraagt om de tijd tussen aankoop, verkoop en betaling te overbruggen. Samen met werkkapitaal (de absolute buffer uit de balans) bepaalt het de netto-kaspositie: werkkapitaal − werkkapitaalbehoefte = nettokas. Wanneer werkkapitaalbehoefte groter is dan werkkapitaal, ontstaat een structureel liquiditeitstekort dat moet worden opgevangen met bankkrediet of leveranciersuitstel.

> [!summary] Korte inhoud
> De werkkapitaalbehoefte is het bedrag aan financiering dat de operationele cyclus van de onderneming nodig heeft: de som van voorraden en handelsvorderingen, verminderd met de handelsschulden.

> [!info] Behoort tot: [[liquiditeitsratio]]

De werkkapitaalbehoefte is het bedrag aan financiering dat de operationele cyclus van de onderneming nodig heeft: de som van voorraden en handelsvorderingen, verminderd met de handelsschulden. Het toont hoeveel cash er vastzit in de cyclus tussen aankoop, productie, verkoop en inning.

_Bron: Algemene financial-analysis-doctrine_


## Bouwstenen

### Drie operationele componenten 🤖

Voorraden + handelsvorderingen − handelsschulden. De eerste twee binden cash (geld dat in voorraad of nog niet geïnd is); de handelsschulden vrijgeven cash (leveranciers financieren de cyclus mee).

**Waarom?** Hoe langer de productie- en inningscyclus, hoe meer middelen er nodig zijn om die te financieren tot het verkochte product effectief wordt betaald.



Rotex Roeselare NV: voorraden € 2.500.000 + handelsvorderingen € 4.000.000 − handelsschulden € 1.800.000 = werkkapitaalbehoefte € 4.700.000.

_Grondslag: Vakdoctrine financial analysis_

### Sectorgebonden 🤖

Een groothandel of producent met lange productiecyclus heeft een hoge werkkapitaalbehoefte; een supermarkt (kort houdbare voorraad, cash-verkoop) of dienstverlener heeft een lage of zelfs negatieve werkkapitaalbehoefte.

**Waarom?** Bedrijven die snel innen (cash bij verkoop) en traag betalen aan leveranciers, laten in feite de leverancier hun cyclus financieren — werkkapitaalbehoefte negatief.



Supermarkt Mertens BV: voorraad € 200.000 + handelsvorderingen € 50.000 − handelsschulden € 600.000 = werkkapitaalbehoefte € −350.000. De leveranciers financieren de cyclus.

_Grondslag: Vakdoctrine_


## Berekening

### Berekening werkkapitaalbehoefte

**Werkkapitaalbehoefte** 
```
werkkapitaalbehoefte = voorraden + handelsvorderingen − handelsschulden
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `voorraden` | Balanspost VI (voorraden en bestellingen in uitvoering) | EUR |
| `handelsvorderingen` | Vorderingen op ten hoogste een jaar uit hoofde van handelstransacties (rubriek VII.A.4 handelsvorderingen) | EUR |
| `handelsschulden` | Schulden op ten hoogste een jaar tegenover leveranciers (rubriek IX.C.1 handelsschulden) | EUR |

**Voorbeeld-invulling**: Rotex: voorraden € 2.500.000; handelsvorderingen € 4.000.000; handelsschulden € 1.800.000

```
€ 2.500.000 + € 4.000.000 − € 1.800.000 = € 4.700.000
```

_Resultaat in EUR_
**Nettokaspositie** (volgt op: werkkapitaalbehoefte-formule)
```
nettokas = werkkapitaal − werkkapitaalbehoefte
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `werkkapitaal` | Vlottende activa − schulden op ten hoogste een jaar (zie record [[werkkapitaal]]) | EUR |
| `werkkapitaalbehoefte` | Resultaat van de eerste formule | EUR |

**Voorbeeld-invulling**: Rotex: werkkapitaal € 4.000.000; werkkapitaalbehoefte € 4.700.000

```
€ 4.000.000 − € 4.700.000 = € −700.000
```

_Resultaat in EUR (negatief = liquiditeitstekort, op te vangen met bankkrediet)_
*De operationele cyclus (van aankoop tot inning) heeft permanent een hoeveelheid cash nodig. Voorraad en vorderingen binden cash; handelsschulden vrijgeven cash.*


## In de praktijk

<h3 id="1.3.II.C">Liquiditeitstekort detecteren</h3>

> [!tip]- Liquiditeitstekort detecteren
> De vergelijking werkkapitaal versus werkkapitaalbehoefte is de standaard-redenering voor liquiditeitsdiagnose. Werkkapitaal < werkkapitaalbehoefte = structureel liquiditeitstekort: de balans-buffer dekt de operationele behoefte niet en de onderneming moet noodzakelijk extern krediet aantrekken (kaskrediet, factoring, leveranciersuitstel). 🤖

<h3 id="1.3.II.C">Decompositie via rotatieratio's</h3>

> [!tip]- Decompositie via rotatieratio's
> Een stijgende werkkapitaalbehoefte komt meestal uit (a) tragere voorraadrotatie (voorraad blijft langer liggen), (b) langere klantkrediet-termijn (vorderingen stijgen sneller dan omzet), of (c) kortere leverancierskrediet-termijn. Combineer altijd met de rotatie-ratio's om te zien welk element verklarend is. 🤖


> [!info]- Niet verwarren met [[werkkapitaal]]
> Werkkapitaal = wat er is (balans-buffer: vlottende activa − korte schulden). Werkkapitaalbehoefte = wat er nodig is (operationele cyclus: voorraden + handelsvorderingen − handelsschulden). Verschil = nettokaspositie.
>
> _Trigger_: Examenvraag 'beschikbaar versus benodigd werkkapitaal': beschikbaar = werkkapitaal; benodigd = werkkapitaalbehoefte.


## Valkuilen

> [!warning]- Niet alle vorderingen en schulden horen in de berekening
> ⚠️ Niet alle vorderingen en schulden horen in de berekening. Werkkapitaalbehoefte bevat alleen de operationele cyclus-componenten: handelsvorderingen en handelsschulden, niet bv. fiscale schulden, dividenduitkeringen of financiële schulden ≤ 1 jaar. 🤖
>
> _Bron: Financial analysis_


> [!warning]- Een negatieve werkkapitaalbehoefte is niet automatisch goed: ze betekent dat de onderneming sterk afhankelijk is van leverancierskrediet
> ⚠️ Een negatieve werkkapitaalbehoefte is niet automatisch goed: ze betekent dat de onderneming sterk afhankelijk is van leverancierskrediet. Bij verstrenging (leveranciers eisen contante betaling) klapt de operationele cyclus in elkaar. 🤖
>
> _Bron: Financial analysis_



## Bronnen

[^1]: `aggregate`
[^2]: `anchor-1.3.II.C`
