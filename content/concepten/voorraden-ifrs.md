---
title: Voorraden onder IFRS (IAS 2)
tags:
- concept
- regel
- po-1-5
linked_anchors:
- 1.5.V.E
- 1.5.V
programmaonderdelen:
- '1.5'
confidence: grounded
node_type: regel
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/voorraden-ifrs.json
gegenereerd_op: '2026-05-18'
---
# Voorraden onder IFRS (IAS 2) ⚖️

> [!summary] Korte inhoud
> IAS 2 — Voorraden regelt de boekhoudkundige verwerking van voorraden onder IFRS. **Voorraden** (alinea 6) zijn activa: (a) aangehouden voor verkoop in het kader van de normale bedrijfsvoering; (b) in het productieproces voor dergelijke verkoop; OF (c) grond-/hulpstoffen die tijde….

IAS 2 — Voorraden regelt de boekhoudkundige verwerking van voorraden onder IFRS. **Voorraden** (alinea 6) zijn activa: (a) aangehouden voor verkoop in het kader van de normale bedrijfsvoering; (b) in het productieproces voor dergelijke verkoop; OF (c) grond-/hulpstoffen die tijdens het productieproces of de dienstverlening worden verbruikt. **Waarderingsregel**: voorraden worden gewaardeerd tegen de **laagste waarde** van **kostprijs** en **opbrengstwaarde** (net realisable value, NRV) — alinea 9. De **kostprijs** bestaat uit inkoopkosten + conversiekosten + andere kosten om voorraden op huidige locatie en in huidige staat te brengen (alinea 10). De **opbrengstwaarde** is de geschatte verkoopprijs in de normale bedrijfsvoering minus geschatte kosten van voltooiing en minus geschatte kosten om de verkoop te realiseren (alinea 6). Voor toerekening van kosten aan voorraadbestanddelen: **specifieke identificatie** voor niet-onderling-uitwisselbare voorraden of specifieke projecten (alinea 23); **FIFO** (eerst in, eerst uit) of **gewogen gemiddelde kostprijs** voor alle andere (alinea 25). **LIFO is verboden** onder IFRS — een belangrijk verschil met Belgisch GAAP.

_Bron: IAS 2 alinea's 6, 9, 10, 25_


## Bouwstenen

### Kostprijscomponenten ⚖️

Drie hoofdcomponenten (alinea 10): (a) **inkoopkosten** — aankoopprijs + invoerrechten + niet-terugvorderbare belastingen + transport- en afhandelingskosten, minus handelskortingen; (b) **conversiekosten** — directe arbeidskosten + systematische toerekening van vaste en variabele indirecte productiekosten; (c) **andere kosten** indien nodig om voorraad op locatie en in staat te brengen.

**Waarom?** Voorraad moet een correcte volledige kostprijs dragen — niet alleen de inkoopprijs maar ook de transport, eventuele bewerking, indirecte productie. Anders zou de marge bij verkoop kunstmatig hoog of laag worden.


_Grondslag: IAS 2 alinea 10-15_

### Verboden kosten — geen onderdeel kostprijs ⚖️

Niét in de kostprijs van voorraden opnemen (alinea 16): (a) abnormale hoeveelheden verspilling van grondstof, arbeid of productiekosten; (b) opslagkosten, tenzij noodzakelijk in productieproces vóór later stadium; (c) administratieve overheadkosten zonder bijdrage aan locatie/staat van voorraad; (d) verkoopkosten. Deze kosten direct als last in W&V.

**Waarom?** Abnormale verspilling weerspiegelt geen normale kostprijs en zou voorraad opblazen. Verkoopkosten ontstaan pas bij realisatie en horen bij periode-resultaat, niet bij voorraad-waarde.


_Grondslag: IAS 2 alinea 16_

### Toerekeningsformules — geen LIFO ⚖️

Voor onderling uitwisselbare voorraden: **FIFO** (first in, first out) of **gewogen gemiddelde kostprijs**. Voor dezelfde aard en gebruik moet één formule consequent worden gebruikt (alinea 25). **LIFO (last in, first out) is expliciet verboden** sinds 2003 — een belangrijk verschil met Belgisch GAAP en sommige andere stelsels (US-GAAP).

**Waarom?** LIFO geeft in inflatiegevoelige sectoren een lagere voorraad-boekwaarde en hogere kostprijs van omzet — wat winstmanipulatie kan toelaten en de balans onrealistisch laag toont. IASB-conclusie: ongewenst.


_Grondslag: IAS 2 alinea 25_

### Opbrengstwaarde-test — laagste-van ⚖️

Op elke balansdatum: vergelijk de boekwaarde (kostprijs) met de **opbrengstwaarde** (NRV) — geschatte verkoopprijs minus geschatte kosten van voltooiing en realisatie. Indien NRV lager: afschrijven van voorraad tot NRV, verlies in W&V (alinea 9 + 28). In een volgende periode mag de afschrijving worden teruggenomen tot maximum de oorspronkelijke kostprijs (alinea 33).

**Waarom?** Het voorzichtigheidsbeginsel: voorraden mogen niet boven hun waarschijnlijke realisatiewaarde worden gewaardeerd. Maar overdreven afschrijvingen mogen ook niet permanent blijven — terugneming bij herstel van NRV.


_Grondslag: IAS 2 alinea 9 + 28-33_

### Opname als last bij verkoop ⚖️

Wanneer voorraden verkocht worden, neem je de boekwaarde op als last (kostprijs van omzet) in **dezelfde** periode waarin de daarmee verband houdende opbrengst wordt opgenomen. Matching-beginsel: opbrengst en bijhorende kostprijs gaan samen.

**Waarom?** Een correcte marge per periode vereist dat opbrengsten en hun directe kostprijs samen worden geboekt. Decouplen zou de werkelijke winstgevendheid vervalsen.


_Grondslag: IAS 2 alinea 34_


## Berekening

### Gewogen gemiddelde kostprijs — illustratie

**Gewogen gemiddelde kostprijs per eenheid** 
```
gewogen gemiddelde = (totale kostprijs begin + totale aankoopkosten periode) / (aantal eenheden begin + aantal eenheden gekocht)
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `totale kostprijs begin` | Boekwaarde voorraad bij aanvang periode | EUR |
| `totale aankoopkosten periode` | Som van alle aankopen tijdens periode | EUR |
| `aantal eenheden` | Aantal voorraad-eenheden | kg/stuks |

**Voorbeeld-invulling**: Zelena Bio ingrediënt X — beginvoorraad 30.000 kg × € 12,00 = € 360.000; aankoop januari 20.000 kg × € 13,00 = € 260.000; aankoop juni 25.000 kg × € 12,50 = € 312.500

```
(€ 360.000 + € 260.000 + € 312.500) / (30.000 + 20.000 + 25.000) = € 932.500 / 75.000 = € 12,43 per kg
```

_Resultaat in EUR/kg_

> [!info]- Niet verwarren met [[voorraden]]
> Belgisch GAAP (KB WVV) staat **drie methoden** toe voor toerekening: FIFO, LIFO, gewogen gemiddelde. IFRS (IAS 2) staat alleen FIFO of gewogen gemiddelde toe — **LIFO verboden**. Bij eerste IFRS-toepassing moeten LIFO-gebruikers herrekenen.
>
> _Trigger_: Examen: 'Onderneming gebruikt LIFO voor voorraadwaardering' — onder IFRS NIET toegelaten; onder BE-GAAP wel.


## Valkuilen

> [!warning]- Bij grondstoffen geldt: NIET afschrijven tot NRV als het verwachte gereed product (waarin de grondstof verwerkt wordt) tegen of boven kostpr…
> ⚠️ Bij grondstoffen geldt: NIET afschrijven tot NRV als het verwachte gereed product (waarin de grondstof verwerkt wordt) tegen of boven kostprijs verkocht zal worden (alinea 32). De vervangingskostprijs is dan een proxy voor NRV alleen als ook het gereed product onder kostprijs zou worden verkocht. ⚖️
>
> _Bron: IAS 2 alinea 32_


> [!warning]- Bij abnormaal lage productie blijft de toerekening van vaste indirecte productiekosten op het 'normale capaciteit'-niveau (alinea 13)
> ⚠️ Bij abnormaal lage productie blijft de toerekening van vaste indirecte productiekosten op het 'normale capaciteit'-niveau (alinea 13). De niet-toegerekende overhead wordt direct als last opgenomen, NIET in de voorraadkostprijs verwerkt. ⚖️
>
> _Bron: IAS 2 alinea 13_


> [!warning]- Onderhanden projecten in opdracht van derden (oude IAS 11) vallen sinds 2018 onder **IFRS 15** — niet meer onder IAS 2 of een aparte standaa…
> ⚠️ Onderhanden projecten in opdracht van derden (oude IAS 11) vallen sinds 2018 onder **IFRS 15** — niet meer onder IAS 2 of een aparte standaard. Opbrengsten over periode opgenomen volgens IFRS 15 alinea 35-37. ⚖️
>
> _Bron: IFRS 15 (vervanging IAS 11)_



## Zie ook

- **Vereist kennis van**: [[onderhanden-projecten-ifrs]]

## Bronnen

[^1]: `IAS-2-voorraden__sec_waardering-van-voorraden`
[^2]: `IAS-2-voorraden__sec_definities`
[^3]: `IAS-2-voorraden__sec_opname-als-last`
[^4]: `IFRS-15-opbrengsten-van-contracten-met-klanten__sec_opname`
