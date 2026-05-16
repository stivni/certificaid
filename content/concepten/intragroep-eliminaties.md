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

> Bij de opstelling van de geconsolideerde jaarrekening moeten alle wederzijdse opbrengsten, kosten, vorderingen, schulden en in activa begrepen onderlinge winsten of verliezen tussen de in de consolidatie opgenomen vennootschappen worden geëlimineerd, om te vermijden dat dezelfde transacties dubbel verschijnen en dat winsten op interne transacties worden gerealiseerd in de groepscijfers terwijl ze economisch niet zijn gerealiseerd buiten de groep.
>
> _Bron: KB WVV art. 3:134 jo. art. 3:136_


> [!summary] Korte definitie
> Bij de opstelling van de geconsolideerde jaarrekening moeten alle wederzijdse opbrengsten, kosten, vorderingen, schulden en in activa begrepen onderlinge winsten of verliezen tussen de in de consolidatie opgenomen vennootschappen worden geëlimineerd, om te vermijden dat dezelfde transacties dubbel verschijnen en dat winsten op interne transacties worden gerealiseerd in de groepscijfers terwijl ze economisch niet zijn gerealiseerd buiten de groep.

> [!info] Behoort tot: [[integrale-consolidatie]] · [[evenredige-consolidatie]]
## Berekening

### Eliminatie van niet-gerealiseerde winst in voorraad (intra-groepsverkoop)

**Eliminatie van niet-gerealiseerde winst in voorraad (intra-groepsverkoop)** 
```
Te elimineren winst = brutomarge% × restvoorraad op balansdatum bij de kopende groepsvennootschap. Het actief 'Voorraden' in de geconsolideerde balans wordt met dat bedrag verminderd; de geconsolideerde reserves dalen evenredig (KB WVV art. 3:134, 2°). De volledige interne omzet en bijbehorende kostprijs verkochte goederen worden uit de geconsolideerde resultatenrekening geschrapt (KB WVV art. 3:136, 1°).
```

*Het deel van de marge dat op de interne verkoop werd geboekt is voor de groep economisch niet gerealiseerd zolang het goed nog in de groep zit. Het actief moet in de geconsolideerde balans worden teruggebracht tot de oorspronkelijke kostprijs voor de groep, en de interne winst mag niet in de geconsolideerde reserves blijven hangen.*

### . 

**Voorbeeld**: Aurelia Holding NV verkoopt voor 100 goederen aan Brugse Brouwerij BV (100 % integrale consolidatie). M realiseert daarop een brutomarge van 30 % (kostprijs voor Aurelia Holding NV = 70, marge = 30). Op balansdatum heeft D nog 40 % van die goederen in voorraad (oorspronkelijke interne aankoopprijs = 40); de overige 60 (interne prijs) is reeds aan derden buiten de groep doorverkocht.

```
Stap 1–2: interne verkoop 100, brutomarge 30 %, restvoorraad bij Brugse Brouwerij BV op balansdatum = 40 (uitgedrukt in de interne aankoopprijs). Stap 3: niet-gerealiseerde winst = 40 × 30 % = 12. Stap 4 (balans-eliminatie, KB WVV art. 3:134, 2°): 'Voorraden' −12, 'Reserves' −12; D's voorraad wordt zo teruggebracht van 40 naar 28 — de oorspronkelijke kostprijs voor de groep. Stap 5 (P&L-eliminatie, KB WVV art. 3:136, 1°): omzet −100, kostprijs verkochte goederen −100 (de interne omzet en bijbehorende kost vallen samen weg uit de geconsolideerde resultatenrekening). De winst op het reeds aan derden verkochte deel (60 × 30 % = 18) is wel gerealiseerd voor de groep en blijft, na de P&L-eliminatie van de interne verkoop, behouden via de verkoop van Brugse Brouwerij BV aan de externe klant.
```

Resultaat: Geconsolideerde balans: voorraden en reserves elk −12. Geconsolideerde resultatenrekening: omzet en kostprijs verkochte goederen elk −100. Netto-effect op geconsolideerd resultaat: −12 (de niet-gerealiseerde marge op het deel dat nog binnen de groep zit). Op het ogenblik dat D ook die resterende 40 aan een derde verkoopt, valt de eliminatie weg en wordt de 12 alsnog als groepsresultaat erkend.

## In de praktijk

### Verkocht actief vs. verkochte dienst {id="verkocht-actief-vs-verkochte-dienst"}

Bij intra-groepsverkoop van een actief dat bij de koper nog op de balans staat (voorraad, materieel actief), wordt zowel de winst (kostprijs verkochte goederen, opbrengsten) als de boekwaarde-aanpassing geëlimineerd. Bij intra-groepsdiensten (administratie, beheersvergoedingen) volstaat de eliminatie van de opbrengsten en kosten — er is geen impact op activa want de dienst is reeds 'verbruikt'. 🤖

**Herkenningspunt**: Vraag: is het verkochte actief nog binnen de groep aanwezig op balansdatum? Zo ja: elimineer ook de marge in het actief. Zo nee: enkel de P&L-eliminatie.

### Belastinggevolgen op intragroep-winst {id="belastinggevolgen-op-intragroep-winst"}

Bij eliminatie van een intra-groepswinst kan er een tijdelijk belastingverschil ontstaan: de winst is fiscaal reeds belast (in de jaarrekening van de verkopende dochter), maar consolideringsgewijs ongerealiseerd. KB WVV art. 3:119 voorziet in een specifieke behandeling van het belastingverschil bij consolidatie. 🤖


## Stappen

### 1. Identificeer onderlinge vorderingen en schulden tussen de consoliderende…

Identificeer onderlinge vorderingen en schulden tussen de moedervennootschap en de dochters in de consolidatiekring (en tussen die dochters onderling). Schrap die zowel aan actiefzijde (vorderingen) als aan passiefzijde (schulden) — de geconsolideerde balans behoudt enkel posities tegenover derden buiten de groep.

### 2. Identificeer in de waarde van activa in de…

Identificeer in de waarde van activa in de geconsolideerde balans begrepen onderlinge winsten of verliezen uit intra-groepsverkopen (typisch: voorraad of materiële vaste activa verkocht binnen de groep met een marge). Schrap die winsten of verliezen — het actief moet in de geconsolideerde balans terug naar de oorspronkelijke kostprijs voor de groep.

### 3. Identificeer onderlinge opbrengsten en kosten uit intra-groepstransacties (interne…

Identificeer onderlinge opbrengsten en kosten uit intra-groepstransacties (interne verkopen, beheersvergoedingen, intresten, huur). Schrap die uit de geconsolideerde resultatenrekening.

### 4. Voor evenredig geconsolideerde gemeenschappelijke dochters: eliminaties beperken tot…

Voor evenredig geconsolideerde gemeenschappelijke dochters: eliminaties beperken tot het pro-rata deel (KB WVV art. 3:140, a). De moeder elimineert geen 100 % van de intra-groepswinst, maar slechts in functie van haar belangenpercentage.

### 5. Beoordeel of de eliminaties van te verwaarlozen betekenis…

Beoordeel of de eliminaties van te verwaarlozen betekenis zijn (KB WVV art. 3:139). Eliminaties bedoeld in art. 3:134, 3:136, eerste lid, 1° en 2°, en 3:138 mogen achterwege blijven wanneer de bedragen, gelet op het doel van het getrouwe beeld (art. 3:105), van te verwaarlozen betekenis zijn.

### 6. Pas in de toelichting de inlichtingen aan: de…

Pas in de toelichting de inlichtingen aan: de op te nemen inlichtingen over het geheel van de moedervennootschap en haar dochters slaan niet op de wederzijdse rechten en verplichtingen die zijn weggelaten

**Grondslag**: KB WVV art. 3:138


## Valkuilen

- ⚠️ Eliminaties kunnen om materialiteitsredenen achterwege blijven (KB WVV art. 3:138 jo. art. 3:139), maar de toets is 'van te verwaarlozen betekenis, gelet op het doel van art. 3:105 (getrouw beeld)'. Materialiteit beoordelen op het niveau van de groep, niet van de individuele post. ⚖️
- ⚠️ Een intra-groepsverkoop tegen kostprijs (zonder marge) levert geen te elimineren winst op de balans op, maar de opbrengsten en kosten moeten nog steeds worden geschrapt uit de resultatenrekening (KB WVV art. 3:136, 1°). ⚖️

## Bronnen

[^1]: `KB-WVV-2019__art_3_106`
[^2]: `KB-WVV-2019__art_3_107`
[^3]: `KB-WVV-2019__art_3_109`
[^4]: `KB-WVV-2019__art_3_110`
[^5]: `CBN-2022-11-vermogensmutatiemethode__sec_intra-groepsverkopen-upstream-downstream-sales`
[^6]: `KB-WVV-2019__art_3_94`
[^7]: `KB-WVV-2019__art_3_111`
