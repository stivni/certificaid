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

> Bij het opstellen van de geconsolideerde jaarrekening moet je alle onderlinge opbrengsten en kosten, vorderingen en schulden, en niet-gerealiseerde winsten of verliezen tussen groepsleden schrappen. Anders zou dezelfde transactie dubbel verschijnen, en zou de groep winst boeken op verkopen aan zichzelf — winst die economisch nog niet is gerealiseerd buiten de groep.
>
> _Bron: KB WVV art. 3:134 jo. art. 3:136_


> [!summary] Korte definitie
> Bij het opstellen van de geconsolideerde jaarrekening moet je alle onderlinge opbrengsten en kosten, vorderingen en schulden, en niet-gerealiseerde winsten of verliezen tussen groepsleden schrappen.

> [!info] Behoort tot: [[integrale-consolidatie]] · [[evenredige-consolidatie]]
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

**Voorbeeld-invulling**: restvoorraad bij Brugse = 40; brutomarge Aurelia = 30 %

```
40 × 30 % = 12
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

**Voorbeeld-invulling**: volle eliminatie = 12; belang Cardinal in Filmstudio Florence = 50 %

```
12 × 50 % = 6
```

_Resultaat in EUR_
*Het marge-deel op een interne verkoop is voor de groep economisch niet gerealiseerd zolang het goed nog in de groep zit. Het actief moet in de geconsolideerde balans terug naar de oorspronkelijke kostprijs voor de groep, en de interne winst mag niet in de geconsolideerde reserves blijven hangen.*

### . 

**Voorbeeld**: Aurelia Holding NV verkoopt voor 100 goederen aan Brugse Brouwerij BV (100 % integrale consolidatie). Aurelia realiseert daarop een brutomarge van 30 % (kostprijs voor Aurelia = 70, marge = 30). Op balansdatum heeft Brugse nog 40 % van die goederen in voorraad (oorspronkelijke interne aankoopprijs = 40); de overige 60 (interne prijs) is reeds aan derden buiten de groep doorverkocht.

```
Stap 1–2: interne verkoop 100, brutomarge 30 %, restvoorraad bij Brugse op balansdatum = 40 (interne aankoopprijs). Stap 3: niet-gerealiseerde winst = 40 × 30 % = 12. Stap 4 (balans, KB WVV art. 3:134, 2°): 'Voorraden' −12, 'Reserves' −12; Brugse's voorraad gaat van 40 naar 28 — de oorspronkelijke kostprijs voor de groep. Stap 5 (P&L, KB WVV art. 3:136, 1°): omzet −100, kostprijs verkochte goederen −100. De winst op het reeds aan derden verkochte deel (60 × 30 % = 18) is al gerealiseerd via de externe verkoop bij Brugse.
```

Resultaat: Geconsolideerde balans: voorraden en reserves elk −12. Geconsolideerde resultatenrekening: omzet en kostprijs verkochte goederen elk −100. Netto-effect op geconsolideerd resultaat: −12 (de niet-gerealiseerde marge op het deel dat nog binnen de groep zit). Op het ogenblik dat Brugse ook die resterende 40 aan een derde verkoopt, valt de eliminatie weg en wordt de 12 alsnog als groepsresultaat erkend.

## In de praktijk

### Verkocht actief vs. verkochte dienst {id="verkocht-actief-vs-verkochte-dienst"}

Bij intra-groepsverkoop van een actief dat bij de koper nog op de balans staat (voorraad, materieel actief), schrap je zowel de winst (kostprijs, opbrengsten) als de boekwaarde-aanpassing. Bij intra-groepsdiensten (administratie, beheersvergoedingen) volstaat het wederzijds schrappen van opbrengsten en kosten — er is geen impact op activa want de dienst is al verbruikt. 🤖

**Herkenningspunt**: Vraag: zit het verkochte actief op balansdatum nog binnen de groep? Ja → ook marge-eliminatie in actief. Nee → enkel P&L-eliminatie.

### Belastinggevolgen op intragroep-winst {id="belastinggevolgen-op-intragroep-winst"}

Bij eliminatie van een intra-groepswinst kan een tijdelijk belastingverschil ontstaan: de winst is fiscaal al belast (bij de verkopende dochter), maar bij consolidatie ongerealiseerd. KB WVV art. 3:119 regelt de behandeling van dat belastingverschil bij consolidatie. 🤖


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
4. Bv. Aurelia heeft een vordering van 50 op Brugse, Brugse heeft een schuld van 50 aan Aurelia → beide gaan weg uit de geconsolideerde balans.
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

1. Maak een lijst van intra-groepsverkopen met marge (typisch goederen of vaste activa).
2. Bepaal voor elk: hoeveel zit op balansdatum nog binnen de groep (in voorraad of op de balans van de koper)?
3. Bereken de niet-gerealiseerde winst: restvoorraad × brutomarge%.
4. Schrap dat bedrag uit de geconsolideerde voorraadwaarde (of vaste activa) én uit de geconsolideerde reserves.
5. Bv. Aurelia verkoopt aan Brugse voor 100 met 30 % marge; Brugse heeft nog 40 in voorraad → 40 × 30 % = 12 te schrappen.


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
4. Bv. Filmstudio verkoopt aan Cardinal voor 100 met 30 % marge, 40 nog in voorraad → te schrappen winst = 40 × 30 % × 50 % = 6 (niet 12).


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

- ⚠️ Eliminaties kunnen om materialiteitsredenen achterwege blijven (KB WVV art. 3:138 jo. art. 3:139), maar de toets is 'van te verwaarlozen betekenis, gelet op het doel van art. 3:105 (getrouw beeld)'. Beoordeel altijd op groepsniveau, niet op de individuele post — twee individueel kleine eliminaties die samen significant zijn moet je niet beide overslaan. ⚖️
- ⚠️ Een intra-groepsverkoop tegen kostprijs (zonder marge) levert geen te elimineren winst op de balans op — er valt niets uit reserves te halen. Maar opbrengsten en kosten moet je nog steeds uit de geconsolideerde resultatenrekening schrappen (KB WVV art. 3:136, 1°). ⚖️

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
