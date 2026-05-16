---
title: Intragroep-eliminaties
tags:
- concept
- procedure
- po-1-4
linked_anchors:
- 1.4.I.D
- 1.4.I.G
- 1.4.I.B
- 1.4.taak.1
programmaonderdelen:
- '1.4'
confidence: grounded
node_type: procedure
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/intragroep-eliminaties.json
gegenereerd_op: '2026-05-16'
---
# Intragroep-eliminaties ⚖️

> [!summary] Korte inhoud
> Bij het opstellen van de geconsolideerde jaarrekening moet je alle onderlinge opbrengsten en kosten, vorderingen en schulden, en niet-gerealiseerde winsten of verliezen tussen groepsleden schrappen.

> [!info] Behoort tot: [[integrale-consolidatie]] · [[evenredige-consolidatie]]

Bij het opstellen van de geconsolideerde jaarrekening moet je alle onderlinge opbrengsten en kosten, vorderingen en schulden, en niet-gerealiseerde winsten of verliezen tussen groepsleden schrappen. Anders zou dezelfde transactie dubbel verschijnen, en zou de groep winst boeken op verkopen aan zichzelf — winst die economisch nog niet is gerealiseerd buiten de groep.

_Bron: KB WVV art. 3:134 jo. art. 3:136_


## Berekening

### Eliminatie van niet-gerealiseerde winst in voorraad (intra-groepsverkoop)

**Te elimineren niet-gerealiseerde winst in voorraad** 
```
te elimineren winst = restvoorraad (in interne aankoopprijs) × brutomarge%
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `restvoorraad (in interne aankoopprijs)` | Wat de koper-groepsvennootschap nog op balansdatum in voorraad heeft, uitgedrukt in de prijs die zij intern betaalde | EUR |
| `brutomarge%` | Winstmarge van de verkoper op de interne verkoop = (verkoopprijs − kostprijs) / verkoopprijs | % |

**Voorbeeld-invulling**: restvoorraad bij Brugse = € 200.000; brutomarge Aurelia = 30 %

```
€ 200.000 × 30 % = € 60.000
```

_Resultaat in EUR_
**Pro-rata eliminatie bij evenredige consolidatie** (volgt op: te-elimineren-winst)
```
pro-rata eliminatie = volle eliminatie × belangenpercentage moeder in gemeenschappelijke dochter
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `volle eliminatie` | Resultaat van bovenstaande formule (alsof 100 % wordt geconsolideerd) | EUR |
| `belangenpercentage moeder` | Aandeel van moeder in kapitaal gemeenschappelijke dochter | % |

**Voorbeeld-invulling**: volle eliminatie = € 60.000; belang Cardinal in Filmstudio Florence = 50 %

```
€ 60.000 × 50 % = € 30.000
```

_Resultaat in EUR_
*Het marge-deel op een interne verkoop is voor de groep economisch niet gerealiseerd zolang het goed nog in de groep zit. Het actief moet in de geconsolideerde balans terug naar de oorspronkelijke kostprijs voor de groep, en de interne winst mag niet in de geconsolideerde reserves blijven hangen.*

### 1. Breng de intra-groepsverkoop in kaart

Noteer wie verkocht (verkoper), wie kocht (koper), de totale interne verkoopprijs en de brutomarge% van de verkoper.

**Waarom?** Een correcte berekening start met een correct gedocumenteerde transactie. Foute marge of verkeerd bedrag werkt door in elke volgende stap.

**📥 Input**:
- Boekhouding verkoper → **Verkoopfactuur, kostprijs, marge** _(document)_

**📤 Output**:
- Werkblad eliminatie → **Interne verkoopprijs + marge%** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Open de boekhouding van Aurelia Holding NV (verkoper).
2. Bepaal de totale interne verkoopprijs voor de verkoop aan Brugse Brouwerij BV: € 500.000.
3. Bepaal de kostprijs voor Aurelia: € 350.000.
4. Brutomarge = (€ 500.000 − € 350.000) / € 500.000 = 30 %.


**Grondslag**: KB WVV art. 3:134, 2°

### 2. Bepaal de restvoorraad op balansdatum

Stel vast hoeveel van het verkochte goed op balansdatum nog in voorraad zit bij de koper — uitgedrukt in de interne aankoopprijs (= wat Brugse heeft betaald).

**Waarom?** Alleen het deel dat nog binnen de groep zit, is economisch niet gerealiseerd. Wat al aan derden buiten de groep is doorverkocht, is wel echt winst geworden.

**📥 Input**:
- Voorraadinventaris koper → **Resterende hoeveelheid × interne aankoopprijs** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkblad eliminatie → **Restvoorraad (interne aankoopprijs)** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Tel hoeveel goederen van de interne aankoop nog in de voorraad van Brugse Brouwerij BV liggen.
2. Vermenigvuldig met de interne aankoopprijs per eenheid.
3. Bv. 40 % van wat Brugse intern aankocht zit nog in voorraad → 40 % × € 500.000 = € 200.000 (in interne aankoopprijs).


**Grondslag**: KB WVV art. 3:134, 2°

### 3. Bereken de te elimineren winst

Niet-gerealiseerde winst = restvoorraad (interne aankoopprijs) × brutomarge%.

**Waarom?** Dit is precies het stuk groepswinst dat nog niet door verkoop aan derden is bewezen. Door dit te schrappen, presenteer je de voorraad opnieuw tegen de oorspronkelijke kostprijs voor de groep.

**📥 Input**:
- Werkblad eliminatie → **Restvoorraad + marge%** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkblad eliminatie → **Te elimineren winst** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Neem de restvoorraad uit stap 2: 40.
2. Neem de marge uit stap 1: 30 %.
3. Niet-gerealiseerde winst = 40 × 30 % = 12.


**Grondslag**: KB WVV art. 3:134, 2°

### 4. Schrap de winst uit voorraad en reserves

Boekhoudkundige eliminatie op de balans: 'Voorraden' en 'Geconsolideerde reserves' elk verminderen met de te elimineren winst.

**Waarom?** De voorraad gaat terug naar oorspronkelijke kostprijs voor de groep; het reserves-deel reflecteert dat de winst nog niet is verdiend.

**📥 Input**:
- Werkblad eliminatie → **Te elimineren winst** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geconsolideerde balans → **Voorraden + reserves** _(geëlimineerde-post)_

**🛠️ Hoe**:

1. Open de geconsolideerde balans.
2. Verlaag 'Voorraden' met 12: 40 → 28.
3. Verlaag 'Geconsolideerde reserves' met 12.
4. De voorraad van Brugse staat nu op 28 (= 40 − 12), wat overeenstemt met de oorspronkelijke kostprijs voor de groep (70 % × 40 = 28).


> [!example]- Voorbeeld: Aurelia Holding NV verkocht in boekjaar 20X1 voor € 500.000 goederen aan Brugse Brouwerij BV met 30 % marge
> Aurelia Holding NV verkocht in boekjaar 20X1 voor € 500.000 goederen aan Brugse Brouwerij BV met 30 % marge. Brugse heeft op 31 december 20X1 nog € 200.000 in voorraad (uitgedrukt in interne aankoopprijs); € 300.000 is al aan derden doorverkocht.
>
> 1. **Te elimineren winst** 🧮
>
>    Restvoorraad bij Brugse: **€ 200.000** (interne aankoopprijs)
>    Brutomarge Aurelia: **30 %**
>    Te elimineren winst = € 200.000 × 30 % = **€ 60.000**
>
> 2. **Balans-eliminatie** 📝
>
>    Activa: Voorraden Brugse −€ 60.000 (€ 200.000 → € 140.000)
>    Passiva: Geconsolideerde reserves −€ 60.000
>    Voorraad staat nu op € 140.000 = oorspronkelijke kostprijs voor de groep (70 % × € 200.000).
>
> 3. **P&L-eliminatie (zie stap 5)** 📝
>
>    Omzet Aurelia −€ 500.000
>    Kostprijs verkochte goederen Brugse −€ 500.000
>    (P&L-eliminatie gaat altijd voor de volledige € 500.000, ongeacht restvoorraad — alleen de niet-gerealiseerde winst gaat via reserves.)
>

**Grondslag**: KB WVV art. 3:134, 2°

### 5. Schrap de interne omzet en kostprijs uit de P&L

Op de geconsolideerde resultatenrekening: schrap de volledige interne omzet bij de verkoper én de volledige interne aankoopkost bij de koper — voor exact hetzelfde bedrag, ongeacht of het goed nog in voorraad zit.

**Waarom?** De P&L-eliminatie gaat altijd voor 100 %: de groep mag economisch geen omzet boeken op verkopen aan zichzelf. De marge-correctie via reserves (stap 4) regelt de winst-realisatie.

**📥 Input**:
- Resultatenrekening verkoper + koper → **Interne omzet + interne kostprijs** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geconsolideerde resultatenrekening → **Omzet + kostprijs** _(geëlimineerde-post)_

**🛠️ Hoe**:

1. Identificeer de volledige interne omzet bij de verkoper: € 500.000.
2. Identificeer de bijbehorende kostprijs verkochte goederen bij de koper: € 500.000 (= wat Brugse betaalde aan Aurelia).
3. Schrap beide: omzet −€ 500.000, kostprijs −€ 500.000.
4. Geconsolideerd resultaat van deze transactie blijft technisch netto € 0 in de P&L; de niet-gerealiseerde winst (€ 60.000) is via stap 4 uit de reserves gegaan.


**Grondslag**: KB WVV art. 3:136, 1°

### 6. Bij evenredige consolidatie: alle stappen × belangenpercentage

Voor gemeenschappelijke dochters die evenredig worden geconsolideerd: vermenigvuldig elke eliminatie (winst in voorraad, omzet, kostprijs) met het belangenpercentage van de moeder. Geen 100 %-eliminatie.

**Waarom?** Alleen jouw pro-rata stuk zit in de geconsolideerde jaarrekening; volledige eliminatie zou te veel wegnemen.

**📥 Input**:
- Werkblad eliminatie → **Volle eliminatie-bedragen** _(boekhoudkundig-bedrag)_
- Aandeelhoudersstructuur → **Belangenpercentage moeder in gemeenschappelijke dochter** _(percentage)_

**📤 Output**:
- Geconsolideerde balans + resultatenrekening → **Pro-rata eliminaties** _(geëlimineerde-post)_

**🛠️ Hoe**:

1. Identificeer dat de tegenpartij een gemeenschappelijke dochter is (evenredig geconsolideerd).
2. Neem het belangenpercentage van de moeder: bv. 50 % voor Cardinal in Filmstudio Florence.
3. Pas elke eliminatie aan: vermenigvuldig met 50 %.
4. Voorbeeld: niet-gerealiseerde winst € 60.000 → € 60.000 × 50 % = € 30.000 te elimineren. Interne omzet € 500.000 → € 250.000 te elimineren. Kostprijs € 500.000 → € 250.000 te elimineren.


**Grondslag**: KB WVV art. 3:140, a

**Voorbeeld**: Aurelia Holding NV verkoopt voor € 500.000 goederen aan Brugse Brouwerij BV (100 % integrale consolidatie). Aurelia realiseert daarop een brutomarge van 30 % (kostprijs voor Aurelia = € 350.000, marge = € 150.000). Op balansdatum heeft Brugse nog 40 % van die goederen in voorraad (oorspronkelijke interne aankoopprijs = € 200.000); de overige € 300.000 (interne prijs) is reeds aan derden buiten de groep doorverkocht.

```
Stap 1–2: interne verkoop € 500.000, brutomarge 30 %, restvoorraad bij Brugse op balansdatum = € 200.000 (interne aankoopprijs). Stap 3: niet-gerealiseerde winst = € 200.000 × 30 % = € 60.000. Stap 4 (balans, KB WVV art. 3:134, 2°): 'Voorraden' −€ 60.000, 'Reserves' −€ 60.000; Brugse's voorraad gaat van € 200.000 naar € 140.000 — de oorspronkelijke kostprijs voor de groep. Stap 5 (P&L, KB WVV art. 3:136, 1°): omzet −€ 500.000, kostprijs verkochte goederen −€ 500.000. De winst op het reeds aan derden verkochte deel (€ 300.000 × 30 % = € 90.000) is al gerealiseerd via de externe verkoop bij Brugse.
```

Resultaat: Geconsolideerde balans: voorraden en reserves elk −€ 60.000. Geconsolideerde resultatenrekening: omzet en kostprijs verkochte goederen elk −€ 500.000. Netto-effect op geconsolideerd resultaat: −€ 60.000 (de niet-gerealiseerde marge op het deel dat nog binnen de groep zit). Op het ogenblik dat Brugse ook die resterende € 200.000 aan een derde verkoopt, valt de eliminatie weg en wordt de € 60.000 alsnog als groepsresultaat erkend.

## In de praktijk

<h3 id="verkocht-actief-vs-verkochte-dienst">Verkocht actief vs. verkochte dienst</h3>

> [!tip]- Verkocht actief vs. verkochte dienst
> Bij intra-groepsverkoop van een actief dat bij de koper nog op de balans staat (voorraad, materieel actief), schrap je zowel de winst (kostprijs, opbrengsten) als de boekwaarde-aanpassing. Bij intra-groepsdiensten (administratie, beheersvergoedingen) volstaat het wederzijds schrappen van opbrengsten en kosten — er is geen impact op activa want de dienst is al verbruikt. 🤖

> [!tip]- Herkennen op het examen
> Vraag: zit het verkochte actief op balansdatum nog binnen de groep? Ja → ook marge-eliminatie in actief. Nee → enkel P&L-eliminatie.

<h3 id="belastinggevolgen-op-intragroep-winst">Belastinggevolgen op intragroep-winst</h3>

> [!tip]- Belastinggevolgen op intragroep-winst
> Bij eliminatie van een intra-groepswinst kan een tijdelijk belastingverschil ontstaan: de winst is fiscaal al belast (bij de verkopende dochter), maar bij consolidatie ongerealiseerd. KB WVV art. 3:119 regelt de behandeling van dat belastingverschil bij consolidatie. 🤖


## Stappen

### 1. Schrap onderlinge vorderingen en schulden

Identificeer alle vorderingen en schulden tussen moeder en dochters in de consolidatiekring (en tussen dochters onderling). Schrap die wederzijds: vordering bij de ene weg én schuld bij de andere weg.

**Waarom?** Een groep kan niet aan zichzelf geld lenen. Als onderlinge vorderingen en schulden zouden blijven staan, blaast dat de geconsolideerde balans op met posten die enkel binnen de groep bestaan.

**📥 Input**:
- Boekhouding moeder + alle dochters in consolidatiekring → **Vorderingen + schulden tussen groepsleden** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geconsolideerde balans → **Onderlinge vorderingen en schulden** _(geëlimineerde-post)_

**🛠️ Hoe**:

1. Maak per groepslid een lijst van vorderingen op andere groepsleden (debiteur intercompany).
2. Maak per groepslid een lijst van schulden aan andere groepsleden (crediteur intercompany).
3. Voor elk bedrag: schrap zowel de vordering bij de ene als de schuld bij de andere — moet voor exact hetzelfde bedrag zijn.
4. Bv. Aurelia heeft een vordering van € 250.000 op Brugse, Brugse heeft een schuld van € 250.000 aan Aurelia → beide gaan weg uit de geconsolideerde balans.
5. Mismatchen? Onderzoek (timing-verschil, valutaverschil, dispuut) en corrigeer eerst de individuele boekhouding.


**Grondslag**: KB WVV art. 3:134, 1°

### 2. Schrap interne winst die nog in activa zit

Spoor onderlinge winsten op die nog in activa van de geconsolideerde balans zitten — typisch in voorraden of vaste activa die met marge intern zijn verkocht. Schrap die marge uit de activawaarde én uit de reserves; het actief gaat terug naar de oorspronkelijke kostprijs voor de groep.

**Waarom?** Een groep kan economisch geen winst maken op verkopen aan zichzelf — die winst is pas reëel als het goed aan iemand buiten de groep verkocht raakt. Niet-gerealiseerde winst eruithalen is essentieel om geen schijnwinst in de groepsreserves te laten staan.

**📥 Input**:
- Lijst intra-groepsverkopen met marge → **Interne verkoopprijs + marge** _(boekhoudkundig-bedrag)_
- Voorraden + vaste activa per groepslid → **Restvoorraad of nog-niet-gerealiseerd actief** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geconsolideerde balans → **Voorraden + reserves verminderd** _(geëlimineerde-post)_

**🛠️ Hoe**:

1. Maak een lijst van intragroep-verkopen met marge (typisch goederen of vaste activa).
2. Bepaal voor elk: hoeveel zit op balansdatum nog binnen de groep (in voorraad of op de balans van de koper)?
3. Bereken de niet-gerealiseerde winst: restvoorraad × brutomarge%.
4. Schrap dat bedrag uit de geconsolideerde voorraadwaarde (of vaste activa) én uit de geconsolideerde reserves.
5. Bv. Aurelia verkoopt aan Brugse voor € 500.000 met 30 % marge; Brugse heeft nog € 200.000 in voorraad → € 200.000 × 30 % = € 60.000 te schrappen.


**Grondslag**: KB WVV art. 3:134, 2°

### 3. Schrap onderlinge opbrengsten en kosten

Schrap alle onderlinge opbrengsten en kosten uit de geconsolideerde resultatenrekening: interne verkopen en aankopen, beheersvergoedingen, intresten op intragroep-leningen, huur tussen groepsleden. Voor exact gelijke bedragen aan beide kanten.

**Waarom?** Een groep mag economisch geen omzet boeken op verkopen aan zichzelf. Door wederzijds te schrappen blijft het geconsolideerd resultaat alleen gevuld met transacties tegenover derden buiten de groep.

**📥 Input**:
- Resultatenrekening moeder + dochters → **Onderlinge omzet, aankopen, vergoedingen** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geconsolideerde resultatenrekening → **Onderlinge opbrengsten en kosten** _(geëlimineerde-post)_

**🛠️ Hoe**:

1. Maak een lijst van alle intragroep-transacties in opbrengsten en kosten van het boekjaar.
2. Voor elke transactie: schrap zowel de opbrengst bij de verkoper als de kost bij de koper. Voor exact hetzelfde bedrag.
3. Voorbeeld: Aurelia factureert 24 beheersvergoeding aan Brugse → schrap 24 omzet bij Aurelia én 24 kost bij Brugse.
4. Idem voor intresten op intragroep-leningen, interne huur, royalty's, etc.


**Grondslag**: KB WVV art. 3:136, 1°

### 4. Voor gemeenschappelijke dochters: elimineer pro-rata

Voor evenredig geconsolideerde gemeenschappelijke dochters: alle eliminaties van stappen 1–3 doen op het pro-rata deel, niet voor 100 %.

**Waarom?** Bij evenredige consolidatie zit slechts jouw aandeel van de gemeenschappelijke dochter in de geconsolideerde jaarrekening. Volledige eliminatie zou de groepscijfers verkeerd corrigeren — je elimineert alleen wat je opgenomen hebt.

**📥 Input**:
- Lijst transacties met gemeenschappelijke dochter → **Bedragen** _(boekhoudkundig-bedrag)_
- Werkblad evenredige consolidatie → **Pro-rata-percentage** _(percentage)_

**📤 Output**:
- Geconsolideerde balans + resultatenrekening → **Pro-rata geëlimineerde posten** _(geëlimineerde-post)_

**🛠️ Hoe**:

1. Identificeer transacties tussen Cardinal Group NV (moedergroep) en haar gemeenschappelijke dochter Filmstudio Florence BV (50 %).
2. Bereken de pro-rata-eliminatie: bedrag × belangenpercentage Cardinal = bedrag × 50 %.
3. Schrap dat pro-rata bedrag uit balans en/of resultatenrekening.
4. Bv. Filmstudio verkoopt aan Cardinal voor € 500.000 met 30 % marge, € 200.000 nog in voorraad → te schrappen winst = € 200.000 × 30 % × 50 % = € 30.000 (niet € 60.000).


**Grondslag**: KB WVV art. 3:140, a

### 5. Toets materialiteit: van te verwaarlozen betekenis?

Beoordeel of een eliminatie van te verwaarlozen betekenis is. Eliminaties uit art. 3:134, art. 3:136 (eerste lid 1° en 2°) en art. 3:138 mogen achterwege blijven als de bedragen, gelet op het getrouwe beeld van art. 3:105, te verwaarlozen zijn.

**Waarom?** Volledige uitvoering van elke eliminatie kan onevenredig veel administratief werk geven voor bedragen die het groepsbeeld nauwelijks beïnvloeden. De wet laat ruimte om dat selectief over te slaan.

**📥 Input**:
- Materialiteitsdrempel voor groep → **Drempelwaarde** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkpapier eliminaties → **Beslissing per eliminatie: wel/niet doen** _(conclusie)_

**🛠️ Hoe**:

1. Bepaal een materialiteitsdrempel voor de geconsolideerde jaarrekening (typisch een percentage van balanstotaal of resultaat).
2. Voor elke eliminatie: vergelijk het bedrag met de drempel.
3. Bedragen onder de drempel: motiveer in werkpapieren waarom je ze niet elimineert; oordeel altijd op groepsniveau, niet per individueel groepslid.
4. Voorzichtigheid: niet-eliminatie mag niet stelselmatig zijn op posten die samen materieel worden.


**Grondslag**: KB WVV art. 3:139

### 6. Pas de toelichting aan: geen melding van weggelaten posten

In de toelichting bij de geconsolideerde jaarrekening: zorg dat informatie over de groep alleen rechten en verplichtingen tegenover derden buiten de groep dekt — niet de geschrapte wederzijdse posten.

**Waarom?** De toelichting moet aansluiten bij wat economisch overgebleven is na consolidatie. Vermelden van wederzijds gewiste rechten/verplichtingen zou de lezer in verwarring brengen.

**📥 Input**:
- Toelichting bij geconsolideerde jaarrekening → **Diverse rubrieken** _(document)_

**📤 Output**:
- Toelichting → **Bijgewerkte rubrieken** _(document)_

**🛠️ Hoe**:

1. Loop de toelichtingsrubrieken na (zekerheden, niet in balans opgenomen rechten/verplichtingen, transacties met verbonden partijen — maar niet binnen consolidatiekring).
2. Filter uit elk overzicht de posten die enkel binnen de geconsolideerde groep bestaan.
3. Behoud de posten tegenover andere groepen, derden, en geassocieerde ondernemingen.


**Grondslag**: KB WVV art. 3:138


## Valkuilen

> [!warning]- Eliminaties kunnen om materialiteitsredenen achterwege blijven (KB WVV art. 3:1…
> ⚠️ Eliminaties kunnen om materialiteitsredenen achterwege blijven (KB WVV art. 3:138 jo. art. 3:139), maar de toets is 'van te verwaarlozen betekenis, gelet op het doel van art. 3:105 (getrouw beeld)'. Beoordeel altijd op groepsniveau, niet op de individuele post — twee individueel kleine eliminaties die samen significant zijn moet je niet beide overslaan. ⚖️
>
> _Bron: KB WVV art. 3:139_


> [!warning]- Een intra-groepsverkoop tegen kostprijs (zonder marge) levert geen te eliminere…
> ⚠️ Een intra-groepsverkoop tegen kostprijs (zonder marge) levert geen te elimineren winst op de balans op — er valt niets uit reserves te halen. Maar opbrengsten en kosten moet je nog steeds uit de geconsolideerde resultatenrekening schrappen (KB WVV art. 3:136, 1°). ⚖️
>
> _Bron: KB WVV art. 3:136, 1°_



## Zie ook

- **Getriggerd door**: [[integrale-consolidatie]]

## Bronnen

[^1]: `KB-WVV-2019__art_3_106`
[^2]: `KB-WVV-2019__art_3_107`
[^3]: `KB-WVV-2019__art_3_109`
[^4]: `KB-WVV-2019__art_3_110`
[^5]: `CBN-2022-11-vermogensmutatiemethode__sec_intra-groepsverkopen-upstream-downstream-sales`
[^6]: `KB-WVV-2019__art_3_94`
[^7]: `KB-WVV-2019__art_3_111`
