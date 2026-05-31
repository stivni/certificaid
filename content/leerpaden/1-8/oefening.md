---
title: "Oefening: Patisserie Beauclair — kostprijs, beslissing, variantie"
description: "Doorgewerkte mini-case in vier stappen: één patisserie met twee producten en een oven-knelpunt. De student berekent kostprijzen via full costing én ABC, kiest de optimale knelpunt-mix, voert een keep-or-drop-analyse uit, en decomposeert een variantie naar prijs en hoeveelheid."
explorer_title: "7. Oefening"
tags:
  - oefening
  - po-1.8
  - cluster-analytische-boekhouding
  - studietijd-75-90min
---

<div class="no-print">

> **Oefening — doe eerst zelf, controleer dan.** Dit is een doorlopende mini-case waar je drie analytische technieken (kostprijs, beslissing, variantie) op één bedrijf toepast. Werk elke stap eerst uit met pen en papier; klap de uitwerking pas open als je vastloopt of klaar bent. De vier stappen bouwen op elkaar — een verkeerde methode-keuze in stap 1 kantelt de beslissing in stap 3. Reken op 75-90 minuten als je het écht doet. Voor verhaal en routekaart: [[leerpaden/1-8|minicursus PO 1.8]].

</div>

## Opgave

Patisserie Beauclair BV is een kleine artisanale patisserie in Brussel met twee producten: een klassieke chocolademousse (potje van 200 ml, hoog volume, simpel proces) en een bruidstaart op maat (job-order, laag volume, complex proces). Het bedrijf werkt met één industriële oven die 3.000 oven-uren per jaar beschikbaar heeft — momenteel volledig benut. Drie patissiers (chef + twee assistenten) staan op vast contract.

Boekjaar 2025 is afgesloten. Het management overweegt een aantal beslissingen voor 2026 en stelt voor het eerst een standaardkost-systeem op voor de mousse. Hieronder vind je alle gegevens die je nodig hebt: volumes en prijzen, variabele kosten, vaste kosten, oven-uren-verbruik, activiteits-data en de resultatenrekening 2025. **Open pas de uitwerking nadat je je eigen antwoord hebt opgeschreven.**

### Volume en verkoopprijs 2025

| Product | Volume | Verkoopprijs/eenheid | Omzet (EUR) |
|---|---:|---:|---:|
| Chocolademousse *(potje van 200 ml)* | 20.000 potjes | 8 | 160.000 |
| Bruidstaart *(op maat)* | 400 stuks | 300 | 120.000 |
| **Totaal omzet** |  |  | **280.000** |

### Variabele kost per eenheid

| Product | Ingrediënten | Variabele OH *(energie + toevoegingen)* | Totaal variabel |
|---|---:|---:|---:|
| Chocolademousse | 2,00 | 1,00 | **3,00** |
| Bruidstaart | 80,00 | 40,00 | **120,00** |

### Vaste kosten 2025 (totaal)

| Kostenpost | Bedrag/jaar (EUR) |
|---|---:|
| Huur en nutsvoorzieningen | 24.000 |
| Lonen 3 patissiers *(chef + 2 assistenten, vast contract)* | 90.000 |
| Verzekering en varia | 6.000 |
| **Totaal vaste kosten** | **120.000** |

### Oven-uren-verbruik

| Product | Oven-uren/eenheid | Volume | Totaal oven-uren/jaar |
|---|---:|---:|---:|
| Chocolademousse | 0,05 | 20.000 | 1.000 |
| Bruidstaart | 5,00 | 400 | 2.000 |
| **Totaal oven-uren** |  |  | **3.000** |

> Capaciteit oven: 3.000 oven-uren/jaar.

### Activiteits-data 2025 (voor wie ABC wil toepassen)

| Activiteit | Vaste kost gerelateerd (EUR) | Cost driver | Volume cost driver |
|---|---:|---|---|
| Bakken/oven *(energie, oven-onderhoud, ovenkost)* | 40.000 | oven-uren | 3.000 (zie boven) |
| Setup/recept-voorbereiding *(opzet per batch, weegwerk, mise-en-place)* | 50.000 | aantal batches | 500 *(mousse: 100 batches van 200 potjes; taart: 400 batches van 1 stuk)* |
| Versiering/afwerking *(decoratie, persoonlijke afwerking — enkel taarten)* | 30.000 | aantal afgewerkte taarten | 400 |
| **Totaal** | **120.000** |  |  |

> De drie activiteit-budgetten samen kloppen exact met de 120.000 EUR vaste kosten. De toewijzing van de vaste kosten naar deze drie pools is een management-keuze gebaseerd op activiteits-analyse (welke vaste kost wordt door welke activiteit gedreven).

### Resultatenrekening Patisserie Beauclair BV — boekjaar 2025 *(vereenvoudigd, tot bedrijfsresultaat)*

|  |  |
|:---|---:|
| **Bedrijfsopbrengsten — omzet** | **280.000** |
| **Bedrijfskosten** | **228.000** |
| Variabele kosten *(ingrediënten + variabele overhead)* | 108.000 |
| Vaste kosten *(huur, lonen, verzekering)* | 120.000 |
| **Bedrijfsresultaat** | **52.000** |

### Aanvullende context voor 2026

Twee aanvullende elementen die het management wil meenemen in 2026:

1. Een **bistro-keten** heeft een eenmalige order van **2.000 extra mousses** aangeboden tegen **5 EUR/stuk** in plaats van 8 — de vraag is of Beauclair die aanvaardt.
2. De inkoopprijzen van melk en chocolade staan onder druk, en in **Q1 2026** zal voor het eerst een **standaardkost-kaart** voor de mousse worden opgesteld met **variantie-analyse**.

---

## Uitwerking

### Stap 1 — Kostprijs vergelijken: full costing vs ABC

Bereken de kostprijs per eenheid voor mousse én taart, eerst via full costing (kies één verdeelsleutel) en daarna via activity-based costing (ABC) met de drie pools uit de opgave. Vergelijk de uitkomsten en formuleer wat ABC bijbrengt dat full costing mist.

<details>
<summary><strong>Oplossing — klik om te tonen</strong></summary>

**Full costing** met oven-uren als verdeelsleutel:

$$\text{Tarief} = \frac{120.000 \text{ vaste kosten}}{3.000 \text{ oven-uren}} = 40 \text{ EUR/oven-uur}$$

Mousse: 3 (var) + 0,05 × 40 = 3 + 2 = **5,00 EUR/potje** — marge 8 − 5 = +3 EUR (37,5 %).
Taart: 120 (var) + 5 × 40 = 120 + 200 = **320 EUR/stuk** — marge 300 − 320 = **−20 EUR (verlies)**.

Op het eerste gezicht maakt de taart dus verlies.

**ABC** — drie pools, elk met eigen tarief:

- Bakken/oven: 40.000 / 3.000 = **13,33 EUR/oven-uur**
- Setup: 50.000 / 500 batches = **100 EUR/batch**
- Versiering: 30.000 / 400 taarten = **75 EUR/taart**

Doorrekenen mousse: 3 (var) + 0,05 × 13,33 (bakken) + 100/200 (setup — één batch dekt 200 potjes) + 0 (geen versiering) = 3 + 0,67 + 0,50 + 0 = **4,17 EUR/potje** → marge 3,83 EUR (48 %).

Doorrekenen taart: 120 (var) + 5 × 13,33 (bakken) + 100/1 (setup — één batch = één taart) + 75 (versiering) = 120 + 66,67 + 100 + 75 = **361,67 EUR/stuk** → "verlies" van −61,67 EUR.

**Vergelijking full costing vs ABC — kostprijs en marge per eenheid (EUR)**

| Methode | Mousse kostprijs | Mousse marge | Taart kostprijs | Taart marge |
|---|---:|---:|---:|---:|
| Full costing *(sleutel: oven-uren, 40 EUR/uur)* | 5,00 | +3,00 *(37,5 %)* | 320,00 | **−20,00 *(verlies)*** |
| ABC *(3 pools)* | **4,17** | **+3,83 *(48 %)*** | **361,67** | **−61,67 *(groter verlies)*** |
| Verschil | −0,83 | +0,83 | +41,67 | −41,67 |

Wat ABC bijbrengt: full costing legt álle overhead via één sleutel (oven-uren) op de producten. Maar setup en versiering zijn niet oven-uren-gedreven — ze zijn batch-gedreven én taart-specifiek. Full costing ondertaxeert daardoor de overhead-impact van de complexe taart en overtaxeert lichtjes de mousse. ABC laat zien dat de taart **groter** verlies maakt dan full doet vermoeden, en dat de mousse iets goedkoper is dan full suggereert.

De methode-keuze kan dus de keep-or-drop-beslissing kantelen — maar vóór je de taart schrapt op basis van deze cijfers, doe eerst stap 3.

> **Let op.** Naïeve reflex: "mooi, ABC bevestigt dat taart verlies maakt — schrappen!" Maar wacht — full én ABC zijn beide allocatie-methodes voor *vaste kosten die toch doorlopen*. Voor de stop-beslissing telt iets anders: de **vermijdbare** vaste kosten. Daarover gaat stap 3. Een ABC-verlies is op zichzelf géén stop-signaal.

</details>

### Stap 2 — Contributiemarge en knelpunt-mix

Bereken de contributiemarge per eenheid voor mousse en taart, en daarna de contributiemarge per oven-uur. De oven is volledig benut, maar het management onderzoekt twee scenario's: (a) 100 extra oven-uren beschikbaar via een onderhouds-optimalisatie — welk product krijgt voorrang? (b) de bistro-keten biedt 2.000 extra mousses tegen 5 EUR/stuk — aanvaarden?

<details>
<summary><strong>Oplossing — klik om te tonen</strong></summary>

CM per eenheid: mousse = 8 − 3 = 5 EUR/potje (62,5 %); taart = 300 − 120 = 180 EUR/stuk (60 %). Op het eerste gezicht lijkt de taart 36× rendabeler — maar dat is een misleidende vergelijking als de capaciteit knelt.

**CM per knelpunt-uur** is de juiste maatstaf:

$$\text{Mousse: } \frac{5}{0{,}05} = 100 \text{ EUR/oven-uur} \quad\text{vs}\quad \text{Taart: } \frac{180}{5} = 36 \text{ EUR/oven-uur}$$

De mousse genereert bijna 3× meer CM per knelpunt-uur dan de taart.

**Contributiemarge — per eenheid vs per knelpunt-uur (EUR)**

| Maatstaf | Mousse | Taart | Wie wint? |
|---|---:|---:|---|
| CM/eenheid | 5,00 | 180,00 | Taart *(misleidend)* |
| Oven-uren/eenheid | 0,05 | 5,00 |  |
| **CM/oven-uur** | **100,00** | **36,00** | **Mousse** |
| 100 extra uren → extra CM | +10.000 | +3.600 | Mousse +6.400 |

**Scenario (a) — 100 extra oven-uren**: bij mousse 100 × 100 = +10.000 EUR extra CM; bij taart 100 × 36 = +3.600 EUR. Verschil = **6.400 EUR/jaar**. Bij knelpunt-druk wint de mousse, niet de taart — ondanks de hogere CM per eenheid.

**Scenario (b) — special order 2.000 mousses à 5 EUR**. Incrementele opbrengst: 2.000 × 5 = 10.000 EUR. Incrementele variabele kost: 2.000 × 3 = 6.000 EUR. Brutowinst zonder capaciteits-effect: +4.000 EUR.

Maar: er zijn 2.000 × 0,05 = 100 extra oven-uren nodig — die zijn er niet, want de capaciteit is volledig benut. Om die 100 uren vrij te maken, moet er iets minder van iets anders gebeuren. Optie: 100 oven-uren minder taart = 20 taarten minder = 20 × 180 = 3.600 EUR CM verloren.

Netto-effect: +4.000 − 3.600 = **+400 EUR**. De order is dus *net* aanvaardbaar, maar de marge is veel dunner dan de bruto-vergelijking suggereert. Alternatief: extra capaciteit via overuren bij de patissiers — dan moet de extra loonkost onder 4.000 EUR blijven, en dat is bij 30 EUR/uur + overuren-toeslag eng krap.

> **Let op.** Stagiair-reflex bij een special order: "order > variabele kost = aanvaarden". Klopt enkel bij vrije capaciteit. Bij volle capaciteit telt de **opportunity cost** van wat je MOET LATEN om plek te maken. Vergeet je dat, dan ziet de order eruit als +4.000 EUR — terwijl ze in werkelijkheid slechts +400 EUR (of zelfs verlies) oplevert.

</details>

### Stap 3 — Keep-or-drop: stoppen met de taart?

Het management overweegt de taart-lijn te schrappen op basis van de cijfers uit stap 1 ("verlies onder beide methoden"). Werk de echte beslissingsanalyse uit: wat verliest Beauclair aan contributiemarge, en welke vaste kosten verdwijnen écht als de taart-lijn stopt? Maak vervolgens een afgewogen aanbeveling. Vergeet niet wat er met de vrijgekomen oven-uren kan gebeuren.

<details>
<summary><strong>Oplossing — klik om te tonen</strong></summary>

**Wat verloren gaat**: de totale CM op taart. 400 taarten × 180 EUR CM/stuk = **72.000 EUR/jaar** valt weg.

**Wat aan vaste kosten echt verdwijnt?** Dit is de kritische vraag. Loop de drie ABC-pools af:

- **Versiering 30.000 EUR** — volledig taart-specifiek (mousse heeft géén versiering). 100 % vermijdbaar.
- **Setup 50.000 EUR** — taart genereert 400 van de 500 batches, dus 400/500 × 50.000 = 40.000 EUR is taart-toewijsbaar. Maar een groot deel van die setup-kost zit vast in de lonen van personeel met vast contract. Stel: één assistent (jaarsalaris ~30.000 EUR) kan effectief afgebouwd worden; van die 40.000 toegerekend aan taart is dus pakweg 20.000 EUR écht vermijdbaar, de andere 20.000 blijft als idle-tijd van personeel dat in dienst blijft.
- **Bakken-pool 40.000 EUR** — energie + oven-onderhoud. Die dalen wel naar rato van werkelijk verbruik, maar als de mousse-productie wordt opgeschaald om de vrijgekomen capaciteit te benutten, kantelt dit weer. Eerste-orde-analyse: neem 0 vermijdbaar uit deze pool.

Totaal vermijdbare vaste kost = 30.000 + 20.000 = **50.000 EUR**.

Netto-effect van stoppen met taart: −72.000 CM + 50.000 vermeden vaste kost = **−22.000 EUR/jaar slechter af**. De vermeende "verliesgevende" taart-lijn draagt netto positief bij aan het resultaat.

Plus: de vrijgekomen 2.000 oven-uren kunnen deels naar extra mousse-productie. Bij beperkte marktvraag (stel: 800 extra mousses verkoopbaar): extra CM = 800 × 5 = 4.000 EUR. Eindbeoordeling: −22.000 + 4.000 = **−18.000 EUR**. Conclusie: **niet schrappen**.

**Keep-or-drop-analyse taart-lijn (EUR/jaar)**

| Element | Bedrag | Toelichting |
|---|---:|---|
| CM die wegvalt | −72.000 | 400 stuks × 180 EUR |
| Vermeden versiering | +30.000 | 100 % taart-specifiek |
| Vermeden setup *(één assistent uit)* | +20.000 | 40.000 toegerekend; 20.000 effectief afbouwbaar |
| Niet-vermijdbare setup *(personeel blijft)* | 0 | 20.000 wordt idle-tijd |
| Vermeden bakken-pool | 0 | Mousse-uitbreiding compenseert |
| **Subtotaal — netto-effect stoppen** | **−22.000** | Slechter af |
| Extra CM op vrijgekomen mousse-capaciteit *(800 stuks)* | +4.000 | Mits afzetbaar |
| **Eindbeoordeling** | **−18.000** | **Niet schrappen** |

De full-cost-verlies op de taart is een rapportering-artefact, niet een werkelijke onderprestatie. Stap 1 wees op een "verliesgevend product"; stap 3 corrigeert die conclusie volledig.

> **Let op.** Een verliesgevend product (op full costing) schrappen verhoogt de winst NIET als zijn CM hoger ligt dan de vermijdbare vaste kosten die je elimineert. De vaste kosten die NIET wegvallen, worden anders nog steeds gedragen — alleen dan door de overblijvende producten, die zo "het verlies erven". Voor stop-beslissingen tellen ALLEEN vermijdbare kosten, niet de full-costing-allocatie.

</details>

### Stap 4 — Standaardkost en Q1 2026-variantie

Beauclair stelt voor 2026 voor het eerst een standaardkost-kaart op voor de chocolademousse. De standaard-variabele kost komt uit op 3,00 EUR/potje (zelfde als 2025-werkelijk — geen verwachte stijging in de standaard). Q1 2026: gebudgetteerd 5.000 mousses (= 25 % van het jaar). Werkelijk: 5.000 mousses geproduceerd, maar de kost-inputs wijken af.

Bereken de totale variantie en decomposeer per kostencategorie naar prijs- en hoeveelheidsvariantie. Identificeer per variantie welke functie (inkoop, productie, HR) verantwoordelijk is en formuleer een aanbeveling.

**Q1 2026 werkelijk (input voor de student)**:

| Categorie | Werkelijk verbruik | Werkelijke prijs | Werkelijke kost (EUR) |
|---|---:|---:|---:|
| Melk | 1.100 kg | 5,20 EUR/kg | 5.720 |
| Chocolade | 240 kg | 22 EUR/kg | 5.280 |
| Arbeid | 110 uren | 30,50 EUR/uur | 3.355 |
| Variabele OH |  |  | 2.100 |
| **Totaal werkelijk** |  |  | **16.455** |

<details>
<summary><strong>Oplossing — klik om te tonen</strong></summary>

**Standaardkost-kaart mousse (per potje)**:

| Component | Norm hoeveelheid | Norm prijs | Standaardkost |
|---|---:|---:|---:|
| Melk | 200 g | 5 EUR/kg | 1,00 |
| Chocolade | 50 g | 20 EUR/kg | 1,00 |
| Arbeid | 0,02 u | 30 EUR/u | 0,60 |
| Variabele OH | 0,05 oven-uur | 8 EUR/u | 0,40 |
| **Totaal** |  |  | **3,00** |

**Q1 budget**: 5.000 potjes × 3,00 = **15.000 EUR**.

**Totale variantie**: 16.455 − 15.000 = **+1.455 EUR ongunstig**.

**Decompositie per categorie** — standaard voor 5.000 potjes:

- **Melk**: standaard 5.000 × 0,2 kg = 1.000 kg @ 5. Prijsvariantie = (5,20 − 5,00) × 1.100 = **+220 ongunstig**. Hoeveelheidsvariantie = (1.100 − 1.000) × 5 = **+500 ongunstig**. Totaal melk = **+720**.
- **Chocolade**: standaard 5.000 × 0,05 kg = 250 kg @ 20. Prijsvariantie = (22 − 20) × 240 = **+480 ongunstig**. Hoeveelheidsvariantie = (240 − 250) × 20 = **−200 gunstig** (10 kg minder verbruikt — recept-aanpassing? betere portionering?). Totaal chocolade = **+280**.
- **Arbeid**: standaard 5.000 × 0,02 u = 100 u @ 30. Loonvariantie (prijs) = (30,50 − 30) × 110 = **+55 ongunstig**. Efficiëntievariantie (hoeveelheid) = (110 − 100) × 30 = **+300 ongunstig** (10 extra uren — nieuwe medewerker in opleiding?). Totaal arbeid = **+355**.
- **Variabele OH**: +100 EUR ongunstig (kleine post — niet verder gedecomposeerd).

**Sluittoets**: 720 + 280 + 355 + 100 = **1.455 EUR ✓** — gelijk aan totale variantie.

**Variantie Q1 2026 — decompositie naar prijs- en hoeveelheidsvariantie (EUR)**

| Categorie | Prijsvariantie | Hoeveelheidsvariantie | Totaal | Oorzaak / verantwoordelijke |
|---|---:|---:|---:|---|
| Melk | +220 ongunstig | +500 ongunstig | **+720** | Markt + verspilling — inkoop + productie |
| Chocolade | +480 ongunstig | −200 gunstig | **+280** | Markt — inkoop *(productie compenseert lichtjes)* |
| Arbeid | +55 ongunstig *(loon)* | +300 ongunstig *(efficiëntie)* | **+355** | CAO + opleiding nieuwe assistent |
| Variabele OH | — | — | **+100** | Klein — niet decomposeerd |
| **Totaal** |  |  | **+1.455 *(ongunstig)*** | 9,7 % van budget — materieel |

**Oorzaak-toewijzing en aanbeveling**:

- **Inkoop** draagt de prijsvarianties melk en chocolade (markt-stijgingen). Aanbeveling: heronderhandelen met leveranciers of forwards-contract afsluiten voor de volgende kwartalen.
- **Productie** draagt de melk-hoeveelheidvariantie (verspilling — proces-audit op portionering, mise-en-place, verlies bij overschenken) en de arbeid-efficiëntievariantie (opleiding nieuwe assistent intensiveren).
- **HR/loon**: de kleine loonvariantie (+55) is acceptabel binnen normale CAO-bewegingen.

**Materialiteit**: 1.455 / 15.000 = **9,7 %** — ruim boven de 5 %-vuistregel. Materiële variantie → pro-rata-correctie volgens IAS 2: het gedeelte dat toewijsbaar is aan nog niet verkochte voorraad gaat naar voorraadwaarde, het verkochte deel direct naar resultaat.

> **Let op.** De som van prijs- én hoeveelheidsvarianties per categorie moet exact gelijk zijn aan de totale variantie. Klopt het niet (720 + 280 + 355 + 100 = 1.455 ✓), dan zit er een reken-fout in een sub-variantie. Doe deze sluit-toets altijd — examen én praktijk.

</details>

---

## Reflectie

Je hebt nu één keer zelf het volledige analytische-pad doorlopen: kostprijs vergelijken via full costing én ABC, contributiemarge per knelpunt-uur in plaats van per eenheid, keep-or-drop op basis van vermijdbare kosten (niet full-cost-allocatie), en variantie-decompositie naar prijs en hoeveelheid met sluit-toets.

De drie analyses zijn niet afzonderlijk — ze vormen samen de management-toolkit van de analytische boekhouding. Een verkeerde methode-keuze in stap 1 leidt tot een verkeerde beslissing in stap 3: dat is de hele les. Standaardkost levert pas sturing op wanneer de variantie decomposeerbaar is naar prijs én hoeveelheid (stap 4) — anders weet je dat het misloopt, maar niet waar je moet bijsturen.

Het examen zal hier geen volledige case reproduceren — wél fragmenten ("bereken CM per knelpunt-uur", "noem twee redenen waarom ABC en full costing tot verschillende kostprijzen leiden", "decomposeer deze variantie naar prijs en hoeveelheid", "welke kosten tellen bij een keep-or-drop?"). Die fragmenten landen scherp als je deze hele case één keer hebt afgewerkt.

**Doelstellingen die deze oefening dekt** (uit het examenprogramma PO 1.8):

- Kostenberekeningen voor alle soorten ondernemingen
- Gedetailleerde analyse van gemiddelde en marginale kosten
- Kostprijsberekening organiseren en boekhoudkundig verwerken
- Verschillen berekenen en analyseren (variantie)
- Rendabele en onrendabele bedrijfstakken identificeren
- Managementsbeslissingen aanbevelen

**Valkuilen die je geoefend hebt**:

- Cross-subsidie via verkeerde verdeelsleutel (full costing ondertaxeert complexe lijn)
- CM/eenheid vs CM/knelpunt-uur verwarren bij capaciteits-druk
- Special order bij volle capaciteit zonder opportunity cost berekenen
- Full-cost-verlies gelijkstellen aan stop-beslissing
- Variantie-decompositie zonder sluit-toets

---

<div class="no-print">

## Wanneer dit zit, ga dan naar

- [[kostprijsmethoden-kiezen]] — voor de techniek nog eens compact gezien: full costing, variable costing, ABC met beslisboom
- [[break-even-en-marginale-beslissing]] — voor break-even, marginale kosten en de mechaniek van special-order-beslissingen
- [[budget-en-variantieanalyse]] — voor de volledige budgetcyclus, variantie-decompositie en pro-rata-correctie volgens IAS 2
- [[wat-is-analytische-boekhouding]] — voor de fundering: relatie met algemene boekhouding, geïntegreerd vs nevengeschikt stelsel
- [[leerpaden/1-8/samenvatting|Samenvatting PO 1.8]] — voor compacte herhaling vlak voor het examen

</div>

---

## Wettelijk fundament

- **Voorraadwaardering — productie-overhead inclusief vaste OH**: IAS 2 § 12-13. *Vaste productie-overhead op basis van normale capaciteit; idle capacity gaat direct naar resultaat, niet naar voorraad.*
- **Materiële variantie — pro-rata-correctie tussen voorraad en KSO**: IAS 2 § 13. *Wanneer werkelijke kost significant afwijkt van standaard, herverdeling pro rata; vuistregel 5 % materialiteit.*
- **Analytische sfeer + voorraadwaardering — B-GAAP**: CBN-advies 132/7. *Verhouding van de analytische boekhouding tot de algemene boekhouding; toegelaten waarderingsregels voor voorraad.*
- **Break-even, keep-or-drop, special order, standaardkost**: interne management-technieken — geen specifieke wets- of CBN-verwijzing. *Praktijknormen volgen Belgische en internationale handboeken management accounting.*

---

*Oefening PO 1.8. Status: tweede oefening volgens schema in `data/oefeningen/SCHEMA.md` (na Nordica voor PO 1.4). Doel: actieve oefencase als 5e leerlaag — integratie van leerstuk 2 (kostprijsmethoden) + 3 (break-even/marginaal) + 4 (budget/variantie) op één samenhangende mini-case.*
