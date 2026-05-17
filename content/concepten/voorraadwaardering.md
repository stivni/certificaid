---
title: Voorraadwaardering (kostprijsmethoden)
tags:
- concept
- regel
- po-1-8
linked_anchors:
- 1.8.II.B
- 1.8.III.A
programmaonderdelen:
- '1.8'
confidence: grounded
node_type: regel
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/voorraadwaardering.json
gegenereerd_op: '2026-05-17'
---
# Voorraadwaardering (kostprijsmethoden) ⚖️

> [!summary] Korte inhoud
> Voorraden worden gewaardeerd aan aanschaffingswaarde (gekochte goederen) of vervaardigingsprijs (zelf vervaardigde producten), eventueel verminderd tot lagere marktwaarde (laagstewaarderegel).

Voorraden worden gewaardeerd aan aanschaffingswaarde (gekochte goederen) of vervaardigingsprijs (zelf vervaardigde producten), eventueel verminderd tot lagere marktwaarde (laagstewaarderegel). Voor identieke goederen waarvan de prijs schommelt, wordt één van de wettelijk toegestane berekeningsmethoden consistent toegepast: individueel, gewogen gemiddelde of FIFO.

_Bron: CBN-advies 132/7 — Boeking en waardering van voorraden_


## Bouwstenen

### Drie toegestane berekeningsmethoden ⚖️

(1) Individuele waardering: per stuk traceerbaar (geschikt voor unieke goederen, machines). (2) Gewogen gemiddelde: gemiddelde aankoopprijs bij elke nieuwe instroom. (3) FIFO: eerst aangekochte goederen eerst verbruikt. LIFO is in België niet meer toegestaan voor de jaarrekening (KB 21.10.2018).

**Waarom?** Bepaalt welke aankoopprijs aan de uitgaande hoeveelheid wordt toegerekend bij prijsschommelingen.

**Voorbeeld**: Yperse Werkplaats BV koopt wol in 3 partijen: 500 kg × € 4,71 + 800 kg × € 5,10 + 700 kg × € 5,30. Verbruik 1.500 kg. Gewogen gemiddelde: (500×4,71 + 800×5,10 + 700×5,30) / 2.000 = € 5,06/kg → verbruik € 7.590. FIFO: 500×4,71 + 800×5,10 + 200×5,30 = € 7.495.

_Grondslag: KB 21.10.2018 art. 18 · CBN 132/7_

### Laagstewaarderegel ⚖️

Op balansdatum: vergelijk aanschaffingswaarde met marktwaarde. De laagste van beide wordt opgenomen. Waardevermindering tot werkelijke waarde bij blijvende marktdaling.

**Waarom?** Voorzichtigheidsbeginsel; vermijdt opgeblazen voorraadwaarde.

**Voorbeeld**: Yperse Werkplaats BV heeft wol in voorraad aan € 5,06/kg gemiddeld. Marktprijs op balansdatum: € 4,30/kg. Waardevermindering naar marktwaarde verplicht → afboeking van het verschil als waardevermindering.

_Grondslag: CBN 132/7 §Marktwaarde_


## Valkuilen

> [!warning]- Methodewissel (bv. van gewogen gemiddelde naar FIFO) vereist motivering in de toelichting; vergelijkbaarheid met vorige jaarrekening moet wo…
> ⚠️ Methodewissel (bv. van gewogen gemiddelde naar FIFO) vereist motivering in de toelichting; vergelijkbaarheid met vorige jaarrekening moet worden uitgelegd. 🤖


> [!warning]- FIFO geeft in een inflatie-omgeving een hogere voorraadwaarde (recente, hogere prijzen blijven in voorraad) en daardoor hogere winst dan gew…
> ⚠️ FIFO geeft in een inflatie-omgeving een hogere voorraadwaarde (recente, hogere prijzen blijven in voorraad) en daardoor hogere winst dan gewogen gemiddelde. Bij deflatie omgekeerd. Examen-valkuil: studenten denken dat FIFO altijd 'objectiever' is. 🤖



## Zie ook

- **Vereist kennis van**: [[materiaalkosten]]
- **Vereist kennis van**: [[vervaardigingsprijs]]

## Bronnen

[^1]: `CBN-0132-07-boeking-en-waardering-van-voorraden__sec_waardering-van-voorraden-grond-en-hulpstoffen-goederen-in-bewerking`
[^2]: `CBN-0132-07-boeking-en-waardering-van-voorraden__sec_marktwaarde`
