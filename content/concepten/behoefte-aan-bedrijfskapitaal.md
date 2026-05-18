---
title: Behoefte aan bedrijfskapitaal (BBK)
tags:
- concept
- begrip
- po-1-9
linked_anchors:
- 1.9.IV.D
- 1.9.IV
- 1.9.taak.1
programmaonderdelen:
- '1.9'
confidence: inferred
node_type: begrip
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/behoefte-aan-bedrijfskapitaal.json
gegenereerd_op: '2026-05-18'
---
# Behoefte aan bedrijfskapitaal (BBK) 🤖

> [!summary] Korte inhoud
> De behoefte aan bedrijfskapitaal (BBK) is het bedrag dat de onderneming permanent moet financieren omdat haar exploitatiecyclus geld vastzet in voorraden en handelsvorderingen voordat zij van haar klanten betaling krijgt — vermindert door wat ze zelf op krediet bij leveranciers k….

> [!info] Behoort tot: [[kasstroomoverzicht-drie-segmenten]]

De behoefte aan bedrijfskapitaal (BBK) is het bedrag dat de onderneming permanent moet financieren omdat haar exploitatiecyclus geld vastzet in voorraden en handelsvorderingen voordat zij van haar klanten betaling krijgt — vermindert door wat ze zelf op krediet bij leveranciers koopt.

_Bron: Financiële analyse — Belgische vakliteratuur (Ooghe-Van Wymeersch, Vereeck e.a.)_


## Bouwstenen

### Voorraad + handelsvorderingen − leverancierskrediet 🤖

Som van wat operationeel vastzit (voorraden, handelsvorderingen) min wat van leveranciers nog niet betaald is (handelsschulden). Het positief verschil is geld dat permanent moet voorgefinancierd worden.

**Waarom?** Een groeiende handelsactiviteit vreet vanzelf cash via de exploitatiecyclus — zonder financiering komt het bedrijf in liquiditeitsproblemen ondanks winstgevendheid.

**Voorbeeld**: Rotex Roeselare NV heeft voorraden van € 6.000.000, handelsvorderingen € 8.000.000 en handelsschulden € 4.500.000. BBK = € 6.000.000 + € 8.000.000 − € 4.500.000 = € 9.500.000.

_Grondslag: Vakdoctrine_

### Werkkapitaal moet de BBK dekken 🤖

Het werkkapitaal (permanente middelen − vaste activa) moet de BBK financieren. Werkkapitaal > BBK levert positieve nettokas; werkkapitaal < BBK betekent dat kortlopend bankkrediet de exploitatiecyclus moet dichtdekken.

**Waarom?** Dit verklaart waarom een winstgevend bedrijf toch in liquiditeitsproblemen kan komen: groeiende omzet → groeiende BBK → werkkapitaal niet meer toereikend → kasspanning.

**Voorbeeld**: Rotex Roeselare NV: werkkapitaal = € 8.000.000, BBK = € 9.500.000 → nettokas = − € 1.500.000 (kortlopende bankkrediet nodig).

_Grondslag: Vakdoctrine_


## Berekening

### Behoefte aan bedrijfskapitaal

**BBK (statisch)** 
```
BBK = voorraden + handelsvorderingen − handelsschulden
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `voorraden` | Klasse 3 — voorraden en bestellingen in uitvoering | EUR |
| `handelsvorderingen` | Klasse 40 — vorderingen op ten hoogste 1 jaar | EUR |
| `handelsschulden` | Klasse 44 — handelsschulden | EUR |

**Voorbeeld-invulling**: voorraden = € 6.000.000, vorderingen = € 8.000.000, schulden = € 4.500.000

```
€ 6.000.000 + € 8.000.000 − € 4.500.000 = € 9.500.000
```

_Resultaat in EUR_
**Nettokas (afgeleide)** (volgt op: bbk)
```
nettokas = werkkapitaal − BBK
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `werkkapitaal` | Zie [[werkkapitaal]] — permanent geïnvesteerd in exploitatiecyclus | EUR |

**Voorbeeld-invulling**: werkkapitaal = € 8.000.000, BBK = € 9.500.000

```
€ 8.000.000 − € 9.500.000 = − € 1.500.000
```

_Resultaat in EUR_

> [!info]- Niet verwarren met [[werkkapitaal]]
> Werkkapitaal is de financieringsbron (permanente middelen min vaste activa); BBK is de behoefte (voorraden + vorderingen min handelsschulden). Het verschil tussen beide is de nettokas — positief = ruimte, negatief = kasspanning.
>
> _Trigger_: Bij examenvraag 'continuïteit / liquiditeitsanalyse': controleer of werkkapitaal de BBK dekt. Niet hetzelfde concept verwarren.


## Valkuilen

> [!warning]- Een groeiend BBK is niet noodzakelijk slecht: het kan signaal zijn van een groeiende activiteit
> ⚠️ Een groeiend BBK is niet noodzakelijk slecht: het kan signaal zijn van een groeiende activiteit. Het wordt problematisch wanneer de BBK sneller groeit dan de omzet (verslechtering inning klanten of voorraadrotatie). 🤖
>
> _Bron: Financiële analyse_



## Zie ook

- **Vereist kennis van**: [[werkkapitaal]]

## Bronnen

[^1]: `anchor-1.9.IV.D`
