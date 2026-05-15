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
schema_version: '1.2'
gegenereerd_uit: data/concepten/records/intragroep-eliminaties.json
gegenereerd_op: '2026-05-15'
---
# Intragroep-eliminaties ⚖️

> Bij de opstelling van de geconsolideerde jaarrekening moeten alle wederzijdse opbrengsten, kosten, vorderingen, schulden en in activa begrepen onderlinge winsten of verliezen tussen de in de consolidatie opgenomen vennootschappen worden geëlimineerd, om te vermijden dat dezelfde transacties dubbel verschijnen en dat winsten op interne transacties worden gerealiseerd in de groepscijfers terwijl ze economisch niet zijn gerealiseerd buiten de groep.
>
> _Bron: KB WVV art. 3:134 jo. art. 3:136_


## Berekening

### Eliminatie van niet-gerealiseerde winst in voorraad (intra-groepsverkoop)

**Formule**: `Te elimineren winst = brutomarge% × restvoorraad op balansdatum bij de kopende groepsvennootschap. Het actief 'Voorraden' in de geconsolideerde balans wordt met dat bedrag verminderd; de geconsolideerde reserves dalen evenredig (KB WVV art. 3:134, 2°). De volledige interne omzet en bijbehorende kostprijs verkochte goederen worden uit de geconsolideerde resultatenrekening geschrapt (KB WVV art. 3:136, 1°).`

*Het deel van de marge dat op de interne verkoop werd geboekt is voor de groep economisch niet gerealiseerd zolang het goed nog in de groep zit. Het actief moet in de geconsolideerde balans worden teruggebracht tot de oorspronkelijke kostprijs voor de groep, en de interne winst mag niet in de geconsolideerde reserves blijven hangen.*

**Stappen**:

1. Identificeer de intra-groepsverkoop: verkoper, koper, totale interne verkoopprijs, brutomarge van de verkoper.
2. Bepaal hoeveel van het verkochte goed op balansdatum nog in voorraad zit bij de koper (of nog niet aan derden buiten de groep is doorverkocht).
3. Bereken de niet-gerealiseerde winst: restvoorraad × brutomarge%.
4. Schrap die niet-gerealiseerde winst uit de waarde van 'Voorraden' in de geconsolideerde balans (KB WVV art. 3:134, 2°) en uit de geconsolideerde reserves.
5. Schrap de volledige interne omzet en bijbehorende kostprijs verkochte goederen uit de geconsolideerde resultatenrekening (KB WVV art. 3:136, 1°) — los van of het goed nog in voorraad zit.
6. Voor evenredig geconsolideerde gemeenschappelijke dochters: beperk de eliminatie van de niet-gerealiseerde winst en van de interne omzet/kostprijs tot het pro-rata belang (KB WVV art. 3:140, a).
**Voorbeeld**: Moeder M verkoopt voor 100 goederen aan dochter D (100 % integrale consolidatie). M realiseert daarop een brutomarge van 30 % (kostprijs voor M = 70, marge = 30). Op balansdatum heeft D nog 40 % van die goederen in voorraad (oorspronkelijke interne aankoopprijs = 40); de overige 60 (interne prijs) is reeds aan derden buiten de groep doorverkocht.

```
Stap 1–2: interne verkoop 100, brutomarge 30 %, restvoorraad bij D op balansdatum = 40 (uitgedrukt in de interne aankoopprijs). Stap 3: niet-gerealiseerde winst = 40 × 30 % = 12. Stap 4 (balans-eliminatie, KB WVV art. 3:134, 2°): 'Voorraden' −12, 'Reserves' −12; D's voorraad wordt zo teruggebracht van 40 naar 28 — de oorspronkelijke kostprijs voor de groep. Stap 5 (P&L-eliminatie, KB WVV art. 3:136, 1°): omzet −100, kostprijs verkochte goederen −100 (de interne omzet en bijbehorende kost vallen samen weg uit de geconsolideerde resultatenrekening). De winst op het reeds aan derden verkochte deel (60 × 30 % = 18) is wel gerealiseerd voor de groep en blijft, na de P&L-eliminatie van de interne verkoop, behouden via de verkoop van D aan de externe klant.
```

Resultaat: Geconsolideerde balans: voorraden en reserves elk −12. Geconsolideerde resultatenrekening: omzet en kostprijs verkochte goederen elk −100. Netto-effect op geconsolideerd resultaat: −12 (de niet-gerealiseerde marge op het deel dat nog binnen de groep zit). Op het ogenblik dat D ook die resterende 40 aan een derde verkoopt, valt de eliminatie weg en wordt de 12 alsnog als groepsresultaat erkend.

## In de praktijk

### Verkocht actief vs. verkochte dienst {id="verkocht-actief-vs-verkochte-dienst"}

Bij intra-groepsverkoop van een actief dat bij de koper nog op de balans staat (voorraad, materieel actief), wordt zowel de winst (kostprijs verkochte goederen, opbrengsten) als de boekwaarde-aanpassing geëlimineerd. Bij intra-groepsdiensten (administratie, beheersvergoedingen) volstaat de eliminatie van de opbrengsten en kosten — er is geen impact op activa want de dienst is reeds 'verbruikt'. 🤖

**Herkenningspunt**: Vraag: is het verkochte actief nog binnen de groep aanwezig op balansdatum? Zo ja: elimineer ook de marge in het actief. Zo nee: enkel de P&L-eliminatie.

### Belastinggevolgen op intragroep-winst {id="belastinggevolgen-op-intragroep-winst"}

Bij eliminatie van een intra-groepswinst kan er een tijdelijk belastingverschil ontstaan: de winst is fiscaal reeds belast (in de jaarrekening van de verkopende dochter), maar consolideringsgewijs ongerealiseerd. KB WVV art. 3:119 voorziet in een specifieke behandeling van het belastingverschil bij consolidatie. 🤖


## Vergelijkingsparen

| Verwarrend met | Verschil | Trigger |
|---|---|---|
| [[integrale-consolidatie]] | Intragroep-eliminaties zijn een verplicht onderdeel van de integrale consolidatie (KB WVV art. 3:134, 3:136). Ze definiëren ze niet — ze realiseren het beginsel dat de groep als één economische entiteit wordt voorgesteld. | — |
| [[evenredige-consolidatie]] | Bij evenredige consolidatie gelden de eliminaties op het pro-rata deel (KB WVV art. 3:140, a) — niet voor 100 %. De integrale eliminatie zou een verkeerd resultaat geven omdat slechts een deel van de transactie tot de groepsentiteit behoort. | — |
| [[vermogensmutatiemethode]] | Bij vermogensmutatie worden de activa/passiva van de geassocieerde niet in de geconsolideerde balans opgenomen — eliminatie op balansniveau is dus niet nodig. Wel wordt het pro-rata aandeel in intra-groepswinsten begrepen in de waarde van een actief uit het 'Aandeel in het resultaat van vennootschappen waarop vermogensmutatie is toegepast' geweerd (CBN 2022/11). | — |

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
