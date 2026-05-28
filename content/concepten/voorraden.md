---
title: "Voorraden"
concept_type: "balanspost"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 1.1.II.E
tags:
  - concept
  - schema-2.2
  - type-balanspost
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/voorraden.json"
---

# Voorraden

_Balanspost_

🏢 Entiteit · Anchors: `1.1.II.E` · Wave: `extract-jaarrekening-rest-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: stocks · voorraad

## Definitie

📖 **Voorraden** zijn lichamelijke roerende activa die de onderneming aanhoudt **om te verkopen** (handelsgoederen, afgewerkte producten), **om te verbruiken in het productieproces** (grondstoffen, hulpstoffen) of die zich **in bewerking** bevinden (goederen in bewerking, onderhanden werk). Ze vormen samen met de geldmiddelen en kortlopende vorderingen het **werkkapitaal** van de onderneming en staan op de actief-zijde van de balans onder de **vlottende activa** (MAR-klasse 30-39). Voorraden zijn typisch activiteitsgebonden: een handelsfirma kent vooral klasse 34 (handelsgoederen); een productiebedrijf kent klassen 30-33 + 37 (onderhanden) + 35 (gereed product).

<small>📚 KB 29-04-2019 WVV — bijlage MAR — Klasse 3 — _kb_</small>

## Substantie

📖 De **MAR-klasse 3** kent volgende sub-rubrieken:
- **30** Grondstoffen
- **31** Hulpstoffen
- **32** Goederen in bewerking
- **33** Gereed product
- **34** Handelsgoederen
- **35** Onroerende goederen bestemd voor verkoop
- **36** Vooruitbetalingen op aankopen voor voorraden
- **37** Bestellingen in uitvoering (onderhanden werk — diensten + projecten)

Voorraden worden bij **inkomst** geboekt aan **aanschaffingswaarde** (aankoopprijs + bijkomende kosten zoals vervoer, douane, niet-aftrekbare btw) of aan **vervaardigingsprijs** (aankoopprijs grondstoffen + directe productiekosten + redelijk deel indirecte productiekosten). Op **balansdatum** worden ze gewaardeerd aan de **laagste** van aanschaffings-/vervaardigingsprijs en **marktwaarde** (laagste-waarde-regel — voorzichtigheidsbeginsel). Het verschil leidt tot een **waardevermindering** geboekt via rekening **631 (Waardeverminderingen op voorraden)** met als tegenpost een vermindering van de voorraadrekening.

<small>📚 KB 29-04-2019 WVV — art. 3:35 e.v. — _kb_ · KB 29-04-2019 WVV — bijlage MAR — Klasse 3 + rekening 631 — _kb_</small>

## Rationale

🔗 Voorraden zitten **tussen** geld en realisatie: ze zijn al geïnvesteerde middelen die nog moeten worden omgezet in vorderingen of cash. Een correcte voorraadwaardering is essentieel omdat ze (1) de bedrijfsmarge bepaalt (kostprijs verkochte goederen = beginvoorraad + aankopen − eindvoorraad), (2) de getrouw-beeld-waardering van vlottende activa beïnvloedt, en (3) typisch een belangrijk audit-risico vormt (manipulatie via overschatting → winst opblazen). Het voorzichtigheidsbeginsel verplicht **onmiddellijke afboeking** bij waardedaling (laagste-waarde-regel) maar geen activering van winsten op niet-verkochte voorraad.

<small>📚 KB 29-04-2019 WVV — art. 3:35 — _kb_</small>

## Bouwstenen

### 📜 FIFO — first-in-first-out  
_`regel`_

📖 **FIFO** veronderstelt dat de **oudst aangekochte** voorraad eerst wordt verkocht of verbruikt. Bij stijgende aankoopprijzen: kostprijs verkochte goederen wordt laag gewaardeerd (oude prijzen), eindvoorraad hoog (recente prijzen) → hogere boekhoudkundige winst. Bij dalende prijzen: omgekeerd. FIFO is in België de meest gebruikte methode omdat ze (1) het matching-principe vrij dicht benadert en (2) de eindvoorraad waardeert aan recente, realistische prijzen.

<small>📚 KB 29-04-2019 WVV — art. 3:37 — _kb_</small>

### 📜 LIFO — last-in-first-out  
_`regel`_

📖 **LIFO** veronderstelt dat de **meest recent aangekochte** voorraad eerst wordt verkocht. Bij stijgende prijzen: kostprijs verkochte goederen hoog (recente prijzen), eindvoorraad laag (oude prijzen) → lagere winst. **Belangrijk**: LIFO is **toegelaten** in het Belgische boekhoudrecht (KB 29-04-2019), maar **verboden** onder IFRS (IAS 2) — een belangrijk verschil bij overgang van B-GAAP naar IFRS.

<small>📚 KB 29-04-2019 WVV — art. 3:37 — _kb_</small>

### 📜 Gemiddelde gewogen prijs (GMP)  
_`regel`_

📖 **GMP** berekent de eenheidsprijs als het gewogen gemiddelde van alle aankopen sinds begin van het boekjaar (of voortschrijdend na elke aankoop). Geschikt voor inwisselbare bulk-voorraden (granen, vloeistoffen, metalen). Vlakt prijsschommelingen uit — geen winst- of verliesmanipulatie via voorraadbeweging.

<small>📚 KB 29-04-2019 WVV — art. 3:37 — _kb_</small>

### ⚙️ Waardevermindering op voorraad (laagste-waarde-regel)  
_`mechanisme`_

📖 Wanneer de **marktwaarde** (realisatiewaarde voor verkoopvoorraden, vervangingswaarde voor verbruiksvoorraden) op balansdatum **lager** is dan de boekwaarde, moet een **waardevermindering** worden geboekt (laagste-waarde-regel, art. 3:35 KB).

**Boeking** (waardevermindering = verschil aanschaffingswaarde min marktwaarde):
```
631 Waardeverminderingen op voorraden    D 1.500
   34x Voorraad handelsgoederen          C 1.500
```
Indien de waarde later herstelt, mag de waardevermindering worden **teruggenomen** via rekening **6310** (terugneming).

<small>📚 KB 29-04-2019 WVV — art. 3:35-39 — _kb_</small>

### ⚙️ Onderhanden werk (klasse 37) — pro-rata  
_`mechanisme`_

📖 **Klasse 37 — Bestellingen in uitvoering** dekt projecten die op balansdatum **niet zijn afgerond**: bouwwerven, software-ontwikkeling, ingenieursopdrachten, langlopende dienstenprojecten. Het Belgische boekhoudrecht laat **twee methodes** toe:

1. **Completed-contract** (oudere methode): winst pas erkennen bij oplevering — voorzichtig maar niet matching-conform;
2. **Percentage-of-completion / pro-rata** (CBN-aanbevolen): winst evenredig met voortgangspercentage erkennen — matcht opbrengsten en kosten.

De pro-rata-methode boekt het onderhanden werk aan **vervaardigingsprijs + redelijke winstopslag op de afgewerkte fractie**. Vereist betrouwbare voortgangsmeting.

<small>📚 KB 29-04-2019 WVV — art. 3:38 — _kb_</small>

## Voorbeelden

### 💡 Handelsfirma — eindvoorraad-waardering FIFO 🔗

_Zelena Bio handelt in biologische voedingsproducten. Op 31-12 zijn er 1.000 eenheden in voorraad. De laatste aankopen waren:
- 1 oktober: 400 stuks aan 12 EUR
- 15 november: 400 stuks aan 13 EUR
- 5 december: 200 stuks aan 14 EUR

De marktwaarde op balansdatum is 13 EUR/stuk.

**FIFO-waardering**: de 1.000 stuks zijn (chronologisch achterstevoren) de meest recente: 200 × 14 + 400 × 13 + 400 × 12 = 2.800 + 5.200 + 4.800 = **12.800 EUR**.
**Marktwaarde**: 1.000 × 13 = 13.000 EUR.

**Laagste-waarde-regel**: voorraad blijft aan 12.800 EUR (lager dan markt). Geen waardevermindering nodig.

Indien marktwaarde 11 EUR/stuk was geweest (11.000 EUR < 12.800 EUR), waardevermindering 1.800 EUR via rekening 631._

<small>📚 KB 29-04-2019 WVV — art. 3:35-37 — _kb_</small>

## Valkuilen

### ⚠️ LIFO denken te mogen gebruiken onder IFRS

**Verkeerde assumptie**: LIFO is internationaal toegestaan — geen probleem bij overstap naar IFRS.

**Kernpunt**: **IAS 2 verbiedt LIFO**. Een Belgische vennootschap die LIFO gebruikt en overstapt op IFRS moet **omschakelen** naar FIFO of gewogen gemiddelde, met retrospectieve aanpassing van de openingsbalans (IFRS 1).

<small>📚 IAS 2 — IAS 2 par. 25 — _richtlijn_</small>

### ⚠️ Voorraad-waardering manipuleren via methodewissel

**Verkeerde assumptie**: Je kunt jaarlijks tussen FIFO en LIFO wisselen om de winst te optimaliseren.

**Kernpunt**: Het **bestendigheidsbeginsel** (art. 3:8 KB) verplicht **stelselmatige** toepassing van waarderingsregels. Wijziging is alleen mogelijk bij belangrijke veranderingen in activiteit of omstandigheden, **met verantwoording in de toelichting** en aanduiding van het impact-cijfer op het resultaat.

<small>📚 KB 29-04-2019 WVV — art. 3:8 — _kb_</small>

## Speelruimtes

### 🎚️ Voorraadwaarderingsmethode kiezen

## Verder lezen (scope-out)

- → Eindejaarsverrichtingen (waardering + correcties) → [[eindejaarsverrichtingen]] _(moet-verwijzen)_
- → Jaarrekening (presentatie balans) → [[jaarrekening]] _(moet-verwijzen)_
- ↪ IFRS-perspectief → [[ifrs]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[boekhouding]]
### `triggert`
- [[eindejaarsverrichtingen]]
### `vergelijkbaar_met`
- [[ifrs]]
    - **Gelijkenissen**:
        - Beide herkennen voorraden bij overgang risico/eigendom
        - Beide kennen laagste-waarde-regel (cost or net realisable value)
    - **Verschillen**:
        - B-GAAP staat LIFO toe; IFRS (IAS 2) niet
        - IAS 2 vereist NRV-toets (net realisable value); B-GAAP gebruikt 'marktwaarde'
    - ⚠️ **Verwarringsrisico**: Stagiairs vergeten dat LIFO een belangrijke B-GAAP-only-methode is bij IFRS-conversie.
