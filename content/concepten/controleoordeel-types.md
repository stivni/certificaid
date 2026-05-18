---
title: Types van controleoordeel
tags:
- concept
- cluster
- po-1-6
linked_anchors:
- 1.6.IV
- 1.6.IV.B
- 1.6.IV.C
programmaonderdelen:
- '1.6'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/controleoordeel-types.json
gegenereerd_op: '2026-05-18'
---
# Types van controleoordeel 🤖

Op het einde van een audit formuleert de beroepsbeoefenaar een controleoordeel. Vier types: (1) goedkeurend oordeel zonder voorbehoud, (2) oordeel met voorbehoud, (3) afkeurend oordeel, (4) onthouding van oordeel. De keuze hangt af van (a) of afwijkingen materieel zijn én of zij diepgaande invloed hebben, en (b) of voldoende en geschikte assurance-informatie kon worden verkregen.

> [!info] Bestaat uit (1): [[aangepast-oordeel]]


## Bouwstenen

### Goedkeurend oordeel zonder voorbehoud ⚖️

De jaarrekening geeft in alle van materieel belang zijnde opzichten een getrouw beeld. Geen materiële afwijkingen, voldoende assurance-informatie.

**Waarom?** De default-uitkomst als de audit niets materieels heeft gedetecteerd.



Bij Rotex Roeselare NV vindt Sofie Janssens geen materiële afwijkingen → goedkeurend oordeel zonder voorbehoud.

_Grondslag: ITAA KMO-controlenorm §117_

### Oordeel met voorbehoud (qualified) ⚖️

(a) Er zijn materiële afwijkingen vastgesteld die echter geen diepgaande invloed hebben, OF (b) er kon geen voldoende assurance-informatie worden verkregen, maar de mogelijke effecten zijn niet diepgaand.

**Waarom?** Tussenoordeel: er zijn problemen, maar niet zo erg dat de hele jaarrekening onbruikbaar wordt.



Sofie Janssens stelt vast dat één deelneming van Rotex met € 250.000 te hoog gewaardeerd is — materieel maar geïsoleerd. Oordeel met voorbehoud: 'naar ons oordeel, behoudens de overwaardering van de deelneming X, geeft de jaarrekening een getrouw beeld'.

_Grondslag: ITAA KMO-controlenorm §119_

### Afkeurend oordeel (adverse) ⚖️

Materiële afwijkingen MET diepgaande invloed: de jaarrekening geeft GEEN getrouw beeld.

**Waarom?** Wanneer de afwijking zo erg is dat één paragraaf voorbehoud niet volstaat — een afzonderlijke afwijking benoemen zou misleiden.



Sofie Janssens stelt vast dat Naaiatelier Ninove BV haar voorraden globaal en systematisch met € 1.200.000 heeft overgewaardeerd, wat de hele balans en het resultaat omslaat. Afkeurend oordeel.

_Grondslag: ITAA KMO-controlenorm §120_

### Onthouding van oordeel (disclaimer) ⚖️

Onmogelijk om voldoende en geschikte assurance-informatie te verkrijgen, EN de mogelijke effecten kunnen diepgaand zijn. De auditor kan geen oordeel formuleren.

**Waarom?** Bv. de cliënt weigert toegang tot kerndocumenten, of een scope-beperking maakt audit onmogelijk.



Meubelzaak Mertens BV weigert de openingsbalans en de aankoopfacturen voor de eerste jaarhelft beschikbaar te stellen. Sofie Janssens kan de voorraadwaardering niet auditeren → onthouding van oordeel.

_Grondslag: ITAA KMO-controlenorm §118_


> [!info]- Niet verwarren met [[afkeurend-oordeel-vs-oordeel-met-voorbehoud]]
> Beide gaan over een AFWIJKING in de jaarrekening die voldoende-en-geschikte assurance-informatie heeft opgeleverd. Oordeel met voorbehoud = de afwijking is materieel maar GEÏSOLEERD (één post, één rubriek): de rest van de jaarrekening blijft gebruikbaar. Afkeurend oordeel = de afwijking is materieel ÉN DIEPGAAND: de hele jaarrekening is misleidend, één paragraaf voorbehoud zou de gebruiker bedriegen.
>
> _Trigger_: Examenvraag: ‘systematische overwaardering van voorraden die balans en resultaat omslaat’ → afkeurend. ‘één deelneming € 250.000 te hoog gewaardeerd’ → oordeel met voorbehoud.

> [!info]- Niet verwarren met [[oordeelonthouding-vs-oordeel-met-voorbehoud]]
> Beide kunnen het gevolg zijn van SCOPE-BEPERKING (geen voldoende-en-geschikte assurance-informatie). Oordeel met voorbehoud = de niet-detecteerbare effecten zijn materieel maar geïsoleerd. Oordeelonthouding = de niet-detecteerbare effecten kunnen materieel én diepgaand zijn (één pijler van de jaarrekening niet auditeerbaar). De auditor kan dan geen oordeel formuleren.
>
> _Trigger_: Examenvraag: ‘klant weigert openingsbalans + alle aankoopfacturen H1’ → oordeelonthouding. ‘inventarisatie van één magazijn niet bijwoonbaar, alternatieve procedures slagen niet’ → oordeel met voorbehoud.


## Zie ook

- **Vereist kennis van**: [[materieel-belang-audit]]
- **Wordt voorondersteld in** (2): [[controleverslag-elementen]] · [[opstellen-controleverslag-en-formuleren-oordeel]]
## Bronnen

[^1]: `ITAA-norm-kmo-controlenorm__sec_3-3-1-basis-voor-het-oordeel`
[^2]: `ITAA-norm-kmo-controlenorm__sec_3-3-2-1-financi-le-overzichten-bevatten-afwijkingen-van-mate`
[^3]: `ITAA-norm-kmo-controlenorm__sec_3-3-2-aangepast-oordeel`
[^4]: `ISA-705-herzien__sec_vereisten_2_part2`
