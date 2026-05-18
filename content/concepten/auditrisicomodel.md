---
title: Auditrisicomodel (controlerisico)
tags:
- concept
- cluster
- po-1-6
- po-1-7
linked_anchors:
- 1.6.II.B
- 1.6.II
- 1.6.III.A
- 1.7.V.E
programmaonderdelen:
- '1.6'
- '1.7'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/auditrisicomodel.json
gegenereerd_op: '2026-05-18'
---
# Auditrisicomodel (controlerisico) 🤖

Het auditrisicomodel structureert de risico-aanpak van de auditor. Het controlerisico — het risico dat de auditor een verkeerd oordeel geeft terwijl de financiële overzichten een materiële afwijking bevatten — wordt opgesplitst in drie componenten: inherent risico, intern beheersingsrisico en ontdekkingsrisico. De auditor stuurt het ontdekkingsrisico (= hoeveel werk hij doet) op basis van zijn inschatting van de eerste twee.

> [!info] Bestaat uit (3): [[inherent-risico]] · [[intern-beheersingsrisico]] · [[ontdekkingsrisico]] · Specialisaties (1): [[auditrisico-1-7-context]]


## Bouwstenen

### Drie componenten ⚖️

Inherent risico (vatbaarheid van een bewering voor afwijking vóór interne beheersing) + intern beheersingsrisico (kans dat de IC een afwijking mist) = risico op een afwijking van materieel belang. Ontdekkingsrisico = de auditor zelf.

**Waarom?** Splits het 'globale' risico in onderdelen die je apart kan inschatten en beïnvloeden.




_Grondslag: ITAA KMO-controlenorm Bijlage 1_

### Wat de auditor kan beïnvloeden 🤖

Enkel het ontdekkingsrisico. Inherent en intern beheersingsrisico zijn EIGENSCHAPPEN van de cliënt — de auditor schat ze in, hij verlaagt ze niet.

**Waarom?** Zo focust het model op de stuurknop van de auditor: omvang, timing en aard van zijn werkzaamheden.



Sofie Janssens kan niet de IT-controles van Rotex verbeteren, maar zij kan beslissen om méér substantive testing te doen op voorraadwaardering wanneer de IC daar zwak is.

_Grondslag: ITAA KMO-controlenorm §96_


## Berekening

### Controlerisico als product van componenten

**Controlerisico (audit risk)** 
```
controlerisico = inherent risico × intern beheersingsrisico × ontdekkingsrisico
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `inherent risico` | Kans op afwijking vóór interne beheersing | % / kans |
| `intern beheersingsrisico` | Kans dat interne beheersing een afwijking mist | % / kans |
| `ontdekkingsrisico` | Kans dat audit-werkzaamheden de afwijking niet ontdekken | % / kans |

**Voorbeeld-invulling**: Bij Rotex Roeselare NV schat Sofie Janssens in: inherent risico = 60 % (complexe groep), intern beheersingsrisico = 30 % (sterke IC), gewenst controlerisico = 5 %.

```
ontdekkingsrisico = 5 % / (60 % × 30 %) = 5 % / 18 % ≈ 28 %
```

_Resultaat in % / kans_
*Het model maakt de relatie expliciet: als inherent of intern beheersingsrisico hoger zijn, moet ontdekkingsrisico lager — wat betekent: meer en gerichtere werkzaamheden door de auditor.*


## Zie ook

- **Wordt voorondersteld in** (2): [[materieel-belang-audit]] · [[risico-inschatting-audit]]
## Bronnen

[^1]: `ITAA-norm-kmo-controlenorm__sec_bijlage-1-definities_part2`
[^2]: `ITAA-norm-kmo-controlenorm__sec_3-2-1-manieren-om-in-te-spelen-op-ingeschatte-risico-s`
