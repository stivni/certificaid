---
title: ABC-methode (Activity Based Costing)
tags:
- concept
- cluster
- po-1-8
linked_anchors:
- 1.8.III.F
programmaonderdelen:
- '1.8'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/abc-methode.json
gegenereerd_op: '2026-05-18'
---
# ABC-methode (Activity Based Costing) 🤖

> [!summary] Korte inhoud
> Activity Based Costing (ABC) verfijnt de kostentoewijzing door indirecte kosten niet via één algemene sleutel maar via meerdere activiteiten en cost drivers naar producten te verdelen.

> [!info] Behoort tot: [[costing-methodes-vergelijking]] · Specialisatie van: [[volledige-kostencalculatie]]

Activity Based Costing (ABC) verfijnt de kostentoewijzing door indirecte kosten niet via één algemene sleutel maar via meerdere activiteiten en cost drivers naar producten te verdelen. ABC herkent dat verschillende indirecte kosten verschillende oorzaken hebben (set-up versus productie-uren versus orderafhandeling) en wijst elke kost toe op basis van zijn eigen drijver. Resultaat: nauwkeuriger kostprijs, vooral voor producten met sterk verschillende complexiteit of seriegrootte.

_Bron: Cooper-Kaplan ABC-methode (management accounting) — bron-gap_


## Bouwstenen

### Stap 1: identificeer activiteiten 🤖

Splits het bedrijfsproces op in activiteiten (set-up, kwaliteitscontrole, inkooporder, klantadvies, verzending). Een activiteit is een herhaalbare handeling met meetbare kost.

**Waarom?** Eén overhead-pool is te grof; activiteiten geven granulariteit.



Yperse Werkplaats BV identificeert in Confectie 5 activiteiten: (1) machine omstellen, (2) kwaliteitscontrole tapijt, (3) verpakken, (4) klant-callcenter, (5) verzending.


### Stap 2: koppel kosten aan activiteiten 🤖

Verdeel de indirecte kosten over de activiteiten op basis van resource drivers (tijd, vloeroppervlakte, lonen). Elke activiteit krijgt een totale kost (cost pool).

**Waarom?** Bepaalt hoeveel elke activiteit kost om uit te voeren.



Yperse Werkplaats BV: omstellen-activiteit kost € 180.000/jaar (loon 2 omstellers + machine-leegloop). Kwaliteitscontrole € 96.000/jaar (loon 2 kwaliteitscontroleurs).


### Stap 3: bepaal cost driver per activiteit 🤖

Voor elke activiteit kies een drijver die de inzet veroorzaakt: aantal set-ups, aantal kwaliteitscontroles, aantal verzonden orders.

**Waarom?** Causaal verband tussen activiteit en kostendrager wordt zichtbaar.



Yperse Werkplaats BV — cost drivers: omstellen → aantal omstellingen (jaar: 1.200); kwaliteitscontrole → aantal gecontroleerde tapijten (jaar: 20.000); verzending → aantal orders (jaar: 800).


### Stap 4: bereken activity-rate 🤖

Cost pool per activiteit / totaal cost-driver-eenheden = kost per cost-driver-eenheid.

**Waarom?** Tarief om de activiteitenkost over kostendragers te verdelen.



Yperse: omstellen-rate = € 180.000 / 1.200 = € 150 per omstelling. Kwaliteitscontrole-rate = € 96.000 / 20.000 = € 4,80 per tapijt. Verzending-rate = € 60.000 / 800 = € 75 per order.


### Stap 5: wijs toe aan kostendragers 🤖

Voor elke kostendrager: tel het verbruik per activiteit op (aantal omstellingen, controles, orders). Vermenigvuldig met activity-rate.

**Waarom?** Geeft per kostendrager een toegerekende overhead die zijn werkelijk verbruik weerspiegelt.



Yperse: order grootwarenhuis (5.000 tapijten, 1 omstelling, 1 verzending) → overhead = € 150 (omstellen) + 5.000 × € 4,80 (controle) + € 75 (verzending) = € 24.225 → € 4,85/tapijt overhead. Order boetiek-keten (200 tapijten, 1 omstelling, 1 verzending) → € 150 + 200×4,80 + 75 = € 1.185 → € 5,93/tapijt. Kleine order draagt méér per stuk — wat klassieke sleutel verbergt.



## In de praktijk

<h3 id="wanneer-abc-nuttig-is">Wanneer ABC nuttig is</h3>

> [!tip]- Wanneer ABC nuttig is
> ABC loont vooral bij (1) hoog aandeel indirecte kosten (> 30 % van totale kosten), (2) diverse productmix met verschillende seriegroottes, (3) producten of klanten met sterk verschillende complexiteit. Bij een homogene productlijn met dominante directe kosten levert ABC weinig extra inzicht maar wel extra administratielast. 🤖

<h3 id="verfijning-geen-vervanging">Verfijning, geen vervanging</h3>

> [!tip]- Verfijning, geen vervanging
> ABC vervangt full costing niet conceptueel — het verfijnt de tweede stap (overhead-verdeling). De grootste meerwaarde zit in 'rare events' (omstellingen, complexe orders) die in traditionele sleutels onder de radar vallen. 🤖


> [!info]- Niet verwarren met [[volledige-kostencalculatie]]
> Traditionele full costing: 1-2 verdeelsleutels per kostencentrum (typisch arbeidsuren of machine-uren). ABC: meerdere activiteiten per centrum, elk met eigen cost driver. ABC geeft accuratere kostprijs, vooral voor laag-volume-/hoog-complexiteit-producten die in klassieke aanpak ondergerapporteerd raken.
>
> _Trigger_: Bij examen-vraag op kostprijs van klein order met veel omsteltijd: klassieke sleutel onderschat de overhead; ABC herstelt.


## Valkuilen

> [!warning]- ABC is duur in opzet en onderhoud
> ⚠️ ABC is duur in opzet en onderhoud. Per activiteit moeten metingen worden bijgehouden — vaak 50-100 activiteiten in middelgrote ondernemingen. Voor KMO's vaak overgedimensioneerd; eenvoudiger systeem met 5-10 cost drivers volstaat (Time-Driven ABC). 🤖


> [!warning]- ABC is geen wettelijke voorraadwaarderingsmethode in België — voor de jaarrekening blijft de wettelijke vervaardigingsprijs (CBN 132/7) geld…
> ⚠️ ABC is geen wettelijke voorraadwaarderingsmethode in België — voor de jaarrekening blijft de wettelijke vervaardigingsprijs (CBN 132/7) gelden. ABC dient als interne informatie, niet voor voorraadwaardering in de balans (behalve indien resultaten dicht bij full costing liggen). 🤖



## Zie ook

- **Vereist kennis van**: [[verdeelsleutel]]

