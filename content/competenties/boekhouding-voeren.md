---
tags: ["1.1", wip, competentie]
niveau: integratie
status: draft
bouwversie: 2
programmaonderdelen: ["1.1"]
itaa-lex-secties:
  - XIII (WER Boek III art. III.82–III.95)
  - XIII (KB WER van 21 oktober 2018 art. 1–11)
procedure-grondslag: "Wettelijk genormeerd door WER art. III.84 en KB 21/10/2018; analytische praktijk voor anomaliedetectie"
---

# Boekhouding voeren

De operationele cyclus van het boekhouden uitvoeren: van de keuze van het boekhoudregime en de opening van het rekeningstelsel, over het chronologisch registreren van verrichtingen in dagboeken, tot de periodieke centralisering naar het grootboek en de correctie van anomalieën. Dit is het dagelijkse vakmanschap dat de boekhouding klaar maakt voor de jaarafsluiting.

> [!info]- Grondslag van deze werkwijze (⚖️ 70% · 🤖 30%)
> De kern van deze procedure is wettelijk vastgelegd:
> - **Dagboek, centraal boek en MAR**: verplichting en werking volgen uit [[bronnen/wetteksten/XIII-wer/boek-iii#art-iii84|WER art. III.84]] en [[bronnen/wetteksten/XIII-KB-wer-boekhouding#art-4|KB WER 2018 art. 4–5]].
> - **Verantwoordingsstukken**: [[bronnen/wetteksten/XIII-wer/boek-iii#art-iii86|WER art. III.86]].
> - **Rekeningstelsel**: minimumindeling vastgelegd via [[bronnen/wetteksten/XIII-KB-wer-boekhouding#art-9|KB WER 2018 art. 9–11]].
> - **Bewaarplicht**: [[bronnen/wetteksten/XIII-wer/boek-iii#art-iii88|WER art. III.88]] en [[bronnen/wetteksten/XIII-KB-wer-boekhouding#art-8|KB WER 2018 art. 8]].
>
> De stappen voor anomaliedetectie (bankafstemming, klanten/leveranciersafstemming, btw-aansluiting) zijn gebaseerd op beroepspraktijk 🤖 — ze vloeien logisch voort uit de wettelijke verplichting van een getrouwe boekhouding maar zijn niet als afzonderlijke procedure voorgeschreven.

## Aanbevolen werkwijze

### 1. 🔍 Boekhoudregime vaststellen

> 📥 **Nodig**:
> - Rechtsvorm en omzetcijfer van de onderneming (laatste afgesloten boekjaar, excl. btw)
>
> 📤 **Uitkomst**:
> - Toepasselijk regime: dubbele boekhouding of vereenvoudigde boekhouding
> - Toepasselijk rekeningenstelsel (MAR voor ondernemingen, MAR vzw voor verenigingen)

**Waarom**: het regime bepaalt welke registers verplicht zijn, of een MAR-conform rekeningenstelsel nodig is en hoe frequent gecentraliseerd moet worden. Een verkeerd regime leidt tot een onwettige boekhouding.

Het basisregime is de **[[dubbele-boekhouding|dubbele boekhouding]]**: dagboek, centraal boek en MAR-conform rekeningenstelsel ([[bronnen/wetteksten/XIII-wer/boek-iii#art-iii84|WER art. III.84]]).

**Uitzondering — vereenvoudigde boekhouding**: bepaalde kleine ondernemingen mogen de [[boekhoudplicht-wer#-vereenvoudigde-boekhouding|vereenvoudigde boekhouding]] voeren met drie dagboeken, zonder centraal boek of MAR ([[bronnen/wetteksten/XIII-wer/boek-iii#art-iii85|WER art. III.85]]):
- Voorwaarde: omzet excl. btw ≤ **€ 500.000** (of € 620.000 voor brandstofhandelaren)
- Wie mag: natuurlijke personen-ondernemingen, vof en gewone commanditaire vennootschappen
- Vennootschappen (bv, nv, …) vallen hier nooit onder — zij zijn altijd verplicht de dubbele boekhouding te voeren

```
Regime bepalen:
  Rechtsvorm = vennootschap (bv, nv, cv …)?  → dubbele boekhouding — altijd
  Rechtsvorm = eenmanszaak / vof / Comm.V?
    Omzet ≤ € 500.000 (excl. btw)?           → vereenvoudigde boekhouding — keuze
    Omzet > € 500.000?                        → dubbele boekhouding — verplicht
```

> [!info]- Concreet: regime van een startende architect-eenmanszaak
>
> Een architect start zijn eenmanszaak in januari. Zijn verwachte omzet voor het eerste jaar is € 80.000 excl. btw. Hij mag starten met de vereenvoudigde boekhouding zolang de verwachte omzet te goeder trouw de drempel niet overschrijdt ([[bronnen/wetteksten/XIII-KB-wer-boekhouding#art-4|KB WER 2018 art. 3]]). Richt hij een bv op, dan is hij per definitie verplicht de dubbele boekhouding te voeren — ongeacht de omzet.
>
> 🤖 *AI-aanvulling*

> [!warning]- Vennootschappen mogen nooit kiezen voor de vereenvoudigde boekhouding
> ❌ *"Een kleine bv met een lage omzet mag de vereenvoudigde boekhouding voeren."*
>
> De vereenvoudigde boekhouding is uitsluitend toegestaan voor natuurlijke personen (eenmanszaken), vof's en gewone commanditaire vennootschappen — nooit voor kapitaalvennootschappen zoals bv, nv of cv. De omzetdrempel is een extra beperking voor wie in principe in aanmerking komt, niet een opening voor iedereen onder die drempel.
>
> 🤖 *AI-aanvulling*

---

### 2. 🔍 Rekeningstelsel openen

> 📥 **Nodig**:
> - Toepasselijk regime (uit stap 1)
> - Sluitingsbalans van het vorige boekjaar (voor continuerende ondernemingen)
>
> 📤 **Uitkomst**:
> - Operationeel rekeningstelsel conform het MAR, met beginbalans correct overgenomen

**Waarom**: zonder een correct geopend rekeningstelsel zijn boekingen vanaf dag één structureel fout — een verkeerde beginstand of een rekeningindeling die het MAR niet volgt, tast de betrouwbaarheid van de volledige boekhouding aan.

**Openingsbalans overnemen** — het [[boekhoudkundige-beginselen|principe van onaantastbaarheid van de openingsbalans]] vereist dat de beginstand van elk boekjaar exact de eindstand van het vorige boekjaar weerspiegelt. Elke balansrekening (klassen 1–5 van het [[dubbele-boekhouding#-minimum-algemeen-rekeningstelsel-mar|MAR]]) wordt overgenomen met haar slotstand als beginstand:

```
Openingsboeking (begin boekjaar):
─────────────────────────────────────────────────────────────────
Rekening      Omschrijving                   Debet     Credit
55000         Bank                           15.000
40000         Handelsvorderingen             28.000
22000         Materiële vaste activa        120.000
17000         Schulden op LT                            80.000
44000         Leveranciersschulden                      12.000
10000         Kapitaal                                  71.000
─────────────────────────────────────────────────────────────────
Totaal D = Totaal C                         163.000   163.000
```

**Resultatenrekeningen (klassen 6 en 7) beginnen altijd op nul** — ze worden volledig verrekend bij de afsluiting van het vorige boekjaar via MAR 14 (overgedragen resultaat).

**MAR aanpassen aan de onderneming** — de minimumindeling is een vloer, geen plafond. De omschrijving van rekeningen mag worden aangepast aan de aard van het bedrijf. Niet-dienstige rekeningen hoeven niet opgenomen te worden. Subrekeningen mogen worden toegevoegd door het rekeningnummer verder uit te splitsen (bv. rekening 40000 → 40010 binnenlandse klanten / 40020 buitenlandse klanten) ([[bronnen/wetteksten/XIII-KB-wer-boekhouding#art-9|KB WER 2018 art. 10–11]]).

> [!warning]- Resultatenrekeningen mogen nooit een beginstand hebben
> ❌ *"Ik neem de omzet van het vorige jaar ook over als beginstand van rekening 700."*
>
> Resultatenrekeningen (klasse 6 en 7) meten een stroom over één boekjaar. Ze worden bij afsluiting gesaldeerd en verrekend via het eigen vermogen (MAR 14). Een niet-nul beginstand op een kosten- of opbrengstenrekening wijst altijd op een fout in de afsluiting van het vorige boekjaar.
>
> 🤖 *AI-aanvulling*

---

### 3. 📋 Verrichtingen registreren in het dagboek

> 📥 **Nodig**:
> - Verantwoordingsstukken (facturen, bankafschriften, loonfiches, …)
> - Operationeel rekeningstelsel (uit stap 2)
>
> 📤 **Uitkomst**:
> - Alle verrichtingen chronologisch en dubbel geboekt in de hulpdagboeken, met verwijzing naar het verantwoordingsstuk

**Waarom**: de dagboekregistratie is de enige bron van waarheid voor de boekhouding. Elke verrichting die niet tijdig, volledig of getrouw wordt ingeschreven, leidt tot een onbetrouwbare boekhouding en mogelijke fiscale sancties.

Elke boeking moet steunen op een **gedagtekend verantwoordingsstuk** waarnaar de boeking verwijst ([[bronnen/wetteksten/XIII-wer/boek-iii#art-iii86|WER art. III.86]]). De verrichtingen worden ingeschreven **zonder uitstel, getrouw, volledig en naar tijdsorde** ([[bronnen/wetteksten/XIII-wer/boek-iii#art-iii84|WER art. III.84]]).

**Hulpdagboeken** — de meeste ondernemingen splitsen het dagboek op per verrichtingstype ([[bronnen/wetteksten/XIII-wer/boek-iii#art-iii84|WER art. III.84]]; [[bronnen/wetteksten/XIII-KB-wer-boekhouding#art-4|KB WER 2018 art. 5]]):

| Hulpdagboek | Inhoud | Verantwoordingsstuk |
|---|---|---|
| Aankoopdagboek | Inkomende facturen leveranciers | Inkomende factuur + leveranciersbon |
| Verkoopdagboek | Uitgaande facturen klanten | Uitgaande factuur (duplicaat) |
| Financieel dagboek | Bank- en kasverrichtingen | Bankrekeninguittreksel, kassabon |
| Dagboek diverse verrichtingen | Lonen, afschrijvingen, eindejaarboekingen, … | Salarisfiches, berekeningen |

**Btw-coderingen** — elke factuur met btw-implicaties vereist de juiste btw-code in het dagboek. Dit bepaalt rechtstreeks de btw-aangifte. Btw-rekeningen (MAR 411 voor aftrekbare btw; MAR 451 voor te betalen btw) worden bij elke boeking correct meegeboekt.

```
Voorbeeld: inkomende factuur leverancier € 2.000 + 21% btw
────────────────────────────────────────────────────────────
Dagboek: Aankoopdagboek                        D          C
44000  Leveranciers (schuld)                           2.420
60000  Aankopen handelsgoederen              2.000
41100  Terugvorderbare btw (21%)               420
────────────────────────────────────────────────────────────
Verwijzing: factuur ABC-2024/0123 dd. 15/01/2024
```

```
Voorbeeld: uitgaande factuur klant € 5.000 + 21% btw
────────────────────────────────────────────────────────────
Dagboek: Verkoopdagboek                        D          C
40000  Klanten (vordering)                   6.050
70000  Omzet                                            5.000
45100  Te betalen btw (21%)                             1.050
────────────────────────────────────────────────────────────
Verwijzing: factuur XYZ-2024/0045 dd. 20/01/2024
```

> [!warning]- Boek elke verrichting op het juiste tijdstip — niet op datum van betaling
> ❌ *"De factuur van december 2024 boek ik pas in januari 2025 wanneer ze betaald wordt."*
>
> Verrichtingen worden geboekt op datum van de prestatie of levering, niet op datum van betaling. Een factuur van december 2024 hoort in de boekhouding van 2024 — ook al wordt ze pas in 2025 betaald. Dit vloeit voort uit het [[boekhoudkundige-beginselen|toerekeningsbeginsel]] (matching principle). Laattijdig boeken verstoort de periodeverdeling van kosten en opbrengsten.
>
> 🤖 *AI-aanvulling*

---

### 4. 📋 Centraliseren naar het grootboek

> 📥 **Nodig**:
> - Ingevulde hulpdagboeken (uit stap 3)
>
> 📤 **Uitkomst**:
> - Samenvattende centralisatieboekingen in het centraal boek, per hoofdrekening; saldo per rekening up-to-date

**Waarom**: het grootboek is het thematische register — het geeft per rekening het volledige overzicht van mutaties en het actuele saldo. Zonder periodieke centralisering is het onmogelijk om balansen of proefbalansen op te stellen of te controleren of de totalen kloppen.

De totalen van de hulpdagboeken worden minstens **maandelijks** samengevat in een centralisatieboeking in het centraal boek ([[bronnen/wetteksten/XIII-wer/boek-iii#art-iii84|WER art. III.84]]). De boeking omvat hetzij het totaal van alle hulpdagboeken uitgesplitst per hoofdrekening, hetzij het totaal per hulpdagboek afzonderlijk ([[bronnen/wetteksten/XIII-wer/boek-iii#art-iii84|WER art. III.84]]).

**Uitzondering**: ondernemingen die de vereenvoudigde boekhouding voeren en toch voor de dubbele kiezen, mogen **driemaandelijks** centraliseren ([[bronnen/wetteksten/XIII-wer/boek-iii#art-iii84|WER art. III.84]]).

```
Centralisatieboeking januari (voorbeeld — Aankoopdagboek)
────────────────────────────────────────────────────────────────────────
Rekening   Omschrijving                                    D          C
60000      Aankopen handelsgoederen (totaal jan)       18.500
41100      Terugvorderbare btw (21%, totaal jan)        3.885
44000      Leveranciers (totaal jan)                            22.385
────────────────────────────────────────────────────────────────────────
Centralisatieboeking januari — aankoopdagboek
```

In **geautomatiseerde systemen** (boekhoudpakketten) is de centralisering doorgaans automatisch bij elke boeking — de proefbalans is altijd actueel. De logica van centralisering blijft dezelfde, maar het mechanisme is onzichtbaar. Zie ook: [[dubbele-boekhouding#-computerverwerking|Computerverwerking]].

**Uitzondering — hulpdagboeken als centraal boek**: als de hulpdagboeken zelf aan de formele vereisten van art. 4 KB WER voldoen (materiële continuïteit, regelmatigheid, onveranderlijkheid), hoeven de gezamenlijke mutaties niet afzonderlijk overgeschreven te worden in een centraal boek ([[bronnen/wetteksten/XIII-KB-wer-boekhouding#art-4|KB WER 2018 art. 5]]). In de praktijk is dit het geval bij de meeste informaticasystemen.

---

### 5. ✅ Anomalieën opsporen en corrigeren

> 📥 **Nodig**:
> - Proefbalans (saldo per rekening, uit stap 4)
> - Bankafschriften, klantenafschriften, leveranciersafschriften, btw-aangifte
>
> 📤 **Uitkomst**:
> - Geïdentificeerde discrepanties tussen boekhouding en externe bronnen
> - Correctieboekingen zodat de boekhouding de werkelijkheid weerspiegelt

**Waarom**: de [[dubbele-boekhouding#-controle-door-de-balans|proefbalans]] controleert alleen het rekenkundig evenwicht — ze vangt geen inhoudelijke fouten op. Inhoudelijke correctheid vereist afstemming met externe bronnen. Een boekhouding die intern klopt maar afwijkt van bankuittreksels of btw-aangiften, is onbetrouwbaar en misleidend.

**Drie afstemmingstypes** (de volgorde is analytisch, niet wettelijk voorgeschreven 🤖):

**5a. Bankafstemming** — vergelijk het saldo van MAR 55 (bankrekening) met het bankrekeninguittreksel:
- Niet-aangekomen betalingen (boekhouding heeft ze, bank nog niet)
- Bankkost of rente die nog niet geboekt is
- Foutief geboekt bedrag

```
Bankafstemming (voorbeeld)
──────────────────────────────────────────────────────
Saldo MAR 55 (boekhouding)          + 12.450
Niet-aangekomen betaling klant      −  2.000   (in boekhouding wel, bank nog niet)
Bankkosten nog te boeken            −     35   (bank verrekende, wij niet)
Gecorrigeerd boekhoudkundig saldo   + 10.415

Saldo bankrekeninguittreksel        + 10.415   ✓ OK
──────────────────────────────────────────────────────
```

**5b. Klanten- en leveranciersafstemming** — vergelijk de openstaande posten in MAR 40 (klanten) en MAR 44 (leveranciers) met de klantenrekeningen en leveranciersafschriften:
- Niet-geboekte factuur (leverancier stuurde een creditnota die nog niet verwerkt is)
- Foutief betaald of geboekt bedrag
- Dubbel geboekte factuur

**5c. Btw-aansluiting** — controleer of de btw-omzet in de boekhouding overeenkomt met de btw-aangifte. Elk kwartaal (of maand) wordt het totaal van MAR 70 (omzet), MAR 451 (te betalen btw) en MAR 411 (aftrekbare btw) vergeleken met de ingediende btw-aangifte. Afwijkingen wijzen op een onvolledige of foutief geboekte periode.

**Correctieboeking** — een foutieve boeking wordt niet doorgestreept of verwijderd maar gecorrigeerd via een tegenboeking. Het oorspronkelijke blijft leesbaar ([[bronnen/wetteksten/XIII-wer/boek-iii#art-iii88|WER art. III.88]]). In een boekhoudpakket: gebruik een stornorekening of maak een tegengestelde boeking met expliciete omschrijving.

```
Foutieve boeking (factuur verkeerd op 61 ipv 60 geboekt, € 500):
    Correctie:
    D: 60000 Aankopen                   500
    C: 61000 Diensten en div. goederen  500
    Omschrijving: correctie factuur X — verkeerde rekening
```

> [!info]- Concreet: btw-aansluiting identificeert vergeten boeking
>
> Een boekhouder stelt bij de kwartaalafsluiting vast dat de btw-aangifte een omzet van € 42.000 vermeldt, maar MAR 70 slechts € 39.500 toont. Verschil: € 2.500. Bij controle blijkt een factuur van eind maart te zijn ingeboekt in april (na de aangifte). De boeking wordt gecorrigeerd met de juiste periode en de aangifte moet worden herzien.
>
> 🤖 *AI-aanvulling*

> [!warning]- Een correcte proefbalans is geen bewijs van een foutloze boekhouding
> ❌ *"De proefbalans klopt, dus de boekhouding is correct."*
>
> De [[dubbele-boekhouding#-controle-door-de-balans|proefbalans]] toont alleen dat totaal debet = totaal credit. Ze vangt niet op: boekingen op de verkeerde rekening, weggelaten boekingen, foutieve bedragen waarbij D en C even groot blijven, of boekingen in de verkeerde periode. Afstemming met externe bronnen (bankuittreksel, klanten, btw-aangifte) is de enige manier om inhoudelijke juistheid te controleren.
>
> 🤖 *AI-aanvulling*

---

### 6. 📋 Periodiek afsluiten en archiveren

> 📥 **Nodig**:
> - Boekhouding na anomaliedetectie en -correctie (stap 5)
>
> 📤 **Uitkomst**:
> - Maandafsluiting vastgesteld (boekingen gelockt, proefbalans bewaard)
> - Jaarafsluiting: centraal boek gesloten, inventaris opgesteld, jaarrekening klaar voor neerlegging
> - Verantwoordingsstukken gearchiveerd conform de bewaarplicht

**Waarom**: periodiek afsluiten zorgt dat de boekhouding niet meer gewijzigd wordt nadat ze is gecontroleerd — zo blijft de historische reeks betrouwbaar en vergelijkbaar. Archiveren is wettelijk verplicht en beschermt de onderneming bij fiscale controles.

**Maandafsluiting** (🤖 beroepspraktijk — niet wettelijk voorgeschreven): na anomaliecontrole wordt de periode afgesloten in het boekhoudpakket. Boekingen voor die periode worden geblokkeerd. Een tussentijdse proefbalans en balans worden bewaard als referentiedocument.

**Jaarafsluiting** — verwijs naar de competentie [[boekjaar-afsluiten|Boekjaar afsluiten]] voor de volledige procedure (inventaris, eindejaarboekingen, opmaken jaarrekening, neerlegging). De boekhoudcyclus eindigt formeel bij de goedkeuring en neerlegging van de jaarrekening.

**Bewaarplicht** — boeken bewaren **7 jaar** te rekenen van 1 januari van het jaar dat volgt op de afsluiting ([[bronnen/wetteksten/XIII-wer/boek-iii#art-iii88|WER art. III.88]]; [[bronnen/wetteksten/XIII-KB-wer-boekhouding#art-8|KB WER 2018 art. 8]]):
- **Kernboeken** (dagboek, centraal boek, inventarisboek): **origineel** bewaren
- **Overige boeken**: origineel of afschrift
- **Verantwoordingsstukken** die tot bewijs tegenover derden kunnen dienen (facturen, bankafschriften): **7 jaar**
- **Interne stukken** die niet strekken tot bewijs jegens derden: **3 jaar**

De bewaarmethode (papier of digitaal) moet de onveranderlijkheid en toegankelijkheid gedurende de volledige bewaringstermijn garanderen ([[bronnen/wetteksten/XIII-KB-wer-boekhouding#art-8|KB WER 2018 art. 8]]).

> [!tip]- Digitale bewaring: zorg voor een onveranderlijk formaat
> Een bestand dat gewoon op een harde schijf staat, voldoet mogelijk niet aan de eis van onveranderlijkheid. Gebruik bij digitale bewaring een formaat en opslagmethode waarbij latere wijziging aantoonbaar is (bv. digitale handtekening, PDF/A, gecertificeerd archiveringsplatform). Een boekhoudpakket met locked periods biedt deze garantie doorgaans intern voor de boekingen zelf, maar niet voor geëxporteerde bestanden.

---

## Voorbeelden

> [!example]- Maandcyclus januari: van facturen naar proefbalans
>
> **Situatie**: een handelsvennootschap (bv) sluit haar boekhoudperiode januari af. Ze heeft: 5 inkomende facturen (totaal € 8.000 + 21% btw), 3 uitgaande facturen (totaal € 12.000 + 21% btw), 2 bankafschriften.
>
> **Conclusie**: na registratie, centralisering en bankafstemming toont de proefbalans een sluitend evenwicht. De btw-positie is: terugvorderbare btw (MAR 411) € 1.680 versus te betalen btw (MAR 451) € 2.520 → netto btw-schuld € 840 voor de aangifte.
>
> **Grondslag**: [[bronnen/wetteksten/XIII-wer/boek-iii#art-iii84|WER art. III.84]]; [[bronnen/wetteksten/XIII-wer/boek-iii#art-iii86|WER art. III.86]]
>
> **Redenering**:
>
> ```
> Stap 1 — Regime: bv → dubbele boekhouding verplicht
>
> Stap 3 — Registratie (selectie):
> Aankoopdagboek (5 facturen totaal):
>   D: 60000 Aankopen             8.000
>   D: 41100 Terugvorderbare btw  1.680
>   C: 44000 Leveranciers                9.680
>
> Verkoopdagboek (3 facturen totaal):
>   D: 40000 Klanten             14.520
>   C: 70000 Omzet                      12.000
>   C: 45100 Te betalen btw              2.520
>
> Stap 4 — Centralisering (einde maand):
>   Centralisatieboeking aankoopdagboek → centraal boek
>   Centralisatieboeking verkoopdagboek → centraal boek
>
> Stap 5 — Bankafstemming:
>   MAR 55 saldo boekhouding  = 28.400
>   Bankrekeninguittreksel    = 28.400  ✓ OK
>
> Btw-positie:
>   Te betalen btw (451)    2.520
>   − Terugvorderbare btw (411)  1.680
>   = Netto btw-schuld        840  → opnemen in kwartaalaangifte
> ```
>
> 🤖 *AI-aanvulling*

> [!example]- Correctieboeking na foutief geboekte huurkost
>
> **Situatie**: een boekhouder heeft in februari de huurkost van € 1.500 per vergissing geboekt op rekening 61000 (diensten en diverse goederen) in plaats van 61100 (huur). Bij de anomaliedetectie in stap 5 valt dit op via de analyse van de proefbalans — 61000 staat te hoog vergeleken met de verwachte kosten.
>
> **Conclusie**: een correctieboeking rechtzet de verkeerde rekening. De proefbalans blijft in evenwicht, de inhoudelijke juistheid wordt hersteld.
>
> **Grondslag**: [[bronnen/wetteksten/XIII-wer/boek-iii#art-iii88|WER art. III.88]] (correcties: oorspronkelijke boeking blijft leesbaar)
>
> **Redenering**:
> ```
> Foutieve boeking (reeds ingevoerd):
>   D: 61000 Diensten en div. goederen    1.500
>   C: 44000 Leveranciers                          1.500
>
> Correctieboeking:
>   D: 61100 Huur                         1.500
>   C: 61000 Diensten en div. goederen             1.500
>   Omschrijving: correctie huurkost februari — verkeerde rekening
>
> Resultaat na correctie:
>   61000: saldo 0 (annulering)
>   61100: saldo 1.500 (juiste rekening)
> ```
>
> 🤖 *AI-aanvulling*

---

## Motiveren op het examen

**Een volledig antwoord bevat:**
1. Vermelding van het toepasselijke regime (dubbele of vereenvoudigde boekhouding) met grondslag
2. Beschrijving van de betrokken stap met verwijzing naar WER of KB WER
3. Bij een correctie: de correctieboeking inclusief omschrijving (niet enkel "een tegenboeking")
4. Bij een afstemmingsvraag: het principe dat de proefbalans niet alles vangt + welke externe bron gebruikt wordt

**Voorbeeldvragen**

> [!question]- Verplichte hulpdagboeken voor een handelsvennootschap
>
> Een boekhouder werkt voor een bv die handelsactiviteiten uitoefent. Welke hulpdagboeken zijn gangbaar in de dubbele boekhouding? Geef vier voorbeelden en omschrijf hun inhoud.
>
> > [!success]- Antwoord
> >
> > **Vier gangbare hulpdagboeken:**
> >
> > 1. **Aankoopdagboek** — alle inkomende facturen van leveranciers (aankopen van goederen, diensten, …)
> > 2. **Verkoopdagboek** — alle uitgaande facturen aan klanten
> > 3. **Financieel dagboek** — bank- en kasverrichtingen (bankafschriften, kasbetalingen en -ontvangsten)
> > 4. **Dagboek diverse verrichtingen** — alle overige boekingen: lonen, afschrijvingen, eindejaarboekingen, correcties
> >
> > De hulpdagboeken zijn een toegelaten opsplitsing van het verplichte dagboek ([[bronnen/wetteksten/XIII-wer/boek-iii#art-iii84|WER art. III.84]]). Als ze aan de formele vereisten voldoen, hoeven hun totalen niet apart overgeschreven te worden in het centraal boek ([[bronnen/wetteksten/XIII-KB-wer-boekhouding#art-4|KB WER 2018 art. 5]]).
> >
> > *Zie: [[dubbele-boekhouding#-hulpdagboeken|Hulpdagboeken]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Bewaarplicht: welke termijn voor facturen?
>
> Een accountant sluit het boekjaar 2024 af op 31 december 2024. Hoe lang moeten de inkoopfacturen van dat boekjaar bewaard worden? Motiveer.
>
> > [!success]- Antwoord
> >
> > **Tot en met 31 december 2031 (7 jaar).**
> >
> > Verantwoordingsstukken die tot bewijs tegenover derden kunnen dienen (inkoopfacturen vallen hier altijd onder) moeten **7 jaar** bewaard worden ([[bronnen/wetteksten/XIII-wer/boek-iii#art-iii86|WER art. III.86]]). De termijn loopt vanaf **1 januari van het jaar dat volgt op de afsluiting**: hier 1 januari 2025, dus tot 31 december 2031.
> >
> > *Zie: [[boekhoudplicht-wer#-bewaarplicht-boeken-7-jaar|Bewaarplicht 7 jaar]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Proefbalans: beperking
>
> Na het invoeren van de boekingen van een kwartaal controleert een boekhouder of de proefbalans klopt. Totaal debet = totaal credit. Hij besluit dat de boekhouding correct is.
>
> Is deze redenering juist? Motiveer.
>
> > [!success]- Antwoord
> >
> > **Nee, de redenering is onjuist.**
> >
> > De [[dubbele-boekhouding#-controle-door-de-balans|proefbalans]] bewijst enkel dat het rekenkundig evenwicht (totaal D = totaal C) intact is. Ze vangt de volgende fouten **niet** op:
> > - Boeking op verkeerde rekening (bv. huurkost op rekening diensten)
> > - Weggelaten boeking (beiden D én C ontbreken — evenwicht blijft)
> > - Verkeerde periode (december-factuur in januari geboekt)
> > - Foutief bedrag waarbij D en C even groot blijven (bv. € 1.200 ipv € 1.020 op beide rekeningen)
> >
> > Inhoudelijke correctheid vereist afstemming met externe bronnen (bankuittreksel, klanten/leveranciers, btw-aangifte).
>
> 🤖 *AI-aanvulling*

> [!question]- Centralisering: wanneer?
>
> Een bv voert de dubbele boekhouding met hulpdagboeken. Hoe vaak moet ze de gezamenlijke mutaties uit de hulpdagboeken samenvatten in het centraal boek?
>
> A. Dagelijks
> B. Minstens maandelijks
> C. Minstens driemaandelijks
> D. Enkel bij de jaarafsluiting
>
> > [!success]- Antwoord
> >
> > **B — Minstens maandelijks.**
> >
> > Voor ondernemingen die de dubbele boekhouding voeren, moeten de gezamenlijke mutaties in de hulpdagboeken minstens maandelijks worden samengevat in een centralisatieboeking in het centraal boek ([[bronnen/wetteksten/XIII-wer/boek-iii#art-iii84|WER art. III.84]]). De driemaandelijkse termijn is een uitzondering voor ondernemingen die recht hebben op de vereenvoudigde boekhouding maar toch voor de dubbele kiezen.
> >
> > *Zie: [[dubbele-boekhouding#-centralisering-van-boekingen|Centralisering van boekingen]]*
>
> 🤖 *AI-aanvulling*

---

## Relevant voor

**[[1.1-algemene-boekhouding|1.1 Algemene boekhouding]]**

Taken:
- *De boekhouding voeren*
  - Rekeningen openen
  - Opstellen van de journalen met inachtneming van de fiscale en analytische gevolgen
  - Centraliseren van de rekeningen
  - Opsporen en corrigeren van anomalieën

Kenniselementen:
- I.A.2 — [[dubbele-boekhouding|Boekhoudkundige basisstructuren]]
- I.A.3 — [[dubbele-boekhouding#-betrouwbaarheid-vergelijkbaarheid-kwaliteit|Problematiek van boekhoudkundige informatie]]
- I.B — [[boekhoudplicht-wer|Boekhoudwetgeving (WER)]]
