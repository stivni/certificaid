---
title: Waarderingsneutraal registratiesysteem
tags:
- concept
- cluster
- po-1-8
linked_anchors:
- 1.8.IV.B
- 1.8.IV.C
programmaonderdelen:
- '1.8'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/registratiesysteem-waarderingsneutraal.json
gegenereerd_op: '2026-05-21'
---
# Waarderingsneutraal registratiesysteem 🔗

Een waarderingsneutraal registratiesysteem vermijdt waarderingsconflicten door belangrijke beslissingen (afschrijvingen, waardeverminderingen, voorraadwaardering) centraal te coördineren en consistent toe te passen tussen algemene en analytische boekhouding. CBN 3/3 beschrijft hiervoor vijf principes — toepasbaar zowel voor joint-ventures als binnen een analytische boekhouding-systeem.

> [!info] Behoort tot: [[rekeningenstelsel-analytisch]]



## Bouwstenen

### Vermijden van waarderingsconflicten ⚖️

Afschrijvingen, waardeverminderingen en voorraadwaardering eenduidig vaststellen; analytische boekhouding mag niet conflicteren met algemene boekhouding zonder expliciete reden (bv. opportuniteitskost).

**Waarom?** Anders raken cijfers per kostencentrum of per drager bezoedeld door methodische verschillen.



Yperse Werkplaats BV past 10-jaar lineaire afschrijving toe op productiemachines in algemene boekhouding én in analytische — geen 'productie-uren-afschrijving' alleen in analytische. Mismatch zou kostprijs onstabiel maken.

_Grondslag: CBN 3/3_


## Berekening

### Reconciliatie-procedure algemene boekhouding ↔ analytische boekhouding (klasse 6 ↔ klasse 9)

*Periodieke vergelijking die garandeert dat dezelfde economische werkelijkheid in beide boekhoudingen op dezelfde waarderingsbasis geregistreerd is. Verschillen mogen, maar moeten verklaarbaar zijn vanuit één van de vijf waarderingsneutraal-principes (CBN 3/3).*

### 1. Vergelijk waarderingsregels op kritieke posten

Loop bij elke periodeafsluiting drie posten af: afschrijvingsmethode + tarief, methode voorraadwaardering (FIFO / gewogen gemiddelde / individueel), criteria voor waardeverminderingen.

**🛠️ Hoe**:

Toets dat klasse 6 (algemeen) en klasse 9 (analytisch) dezelfde basis gebruiken. Verschil = anomalie tenzij gemotiveerd in waardenneutraliteits-charter.

**Grondslag**: CBN 3/3 — waarderingsneutraliteit

### 2. Aggregeer klasse 6 totalen per kostengroep

Tel kostsoorten in klasse 6 op per groep (61 diensten, 62 lonen, 63 afschrijvingen, 64 andere) voor de afgesloten periode.

**🛠️ Hoe**:

Uit grootboek; documenteer eventuele eindperiode-correcties (vakantiegeldvoorziening, uitgestelde lasten) zodat de klasse-6-cijfers vergelijkbaar zijn met klasse 9.

**Grondslag**: KB 21.10.2018 — MAR klasse 6

### 3. Aggregeer klasse 9 totalen per kostencentrum + reflectie-rekening

Tel toegerekende kosten op klasse 9 op per kostencentrum + saldo van de reflectierekeningen (90-91).

**🛠️ Hoe**:

Reflectierekening = spiegelboeking van klasse 6 op klasse 9. Totalen moeten matchen tenzij interne verrekeningen of opportuniteitskosten extra zijn opgenomen.

**Grondslag**: [[rekeningenstelsel-analytisch]]

### 4. Verklaar elk verschil

Voor elk verschil tussen klasse-6-totaal en gespiegelde klasse-9-toewijzing: koppel aan één van vijf toegestane oorzaken — (a) interne verrekening tussen centra, (b) opportuniteitskost (alleen analytisch geboekt), (c) standaard-werkelijk-verschil bij gebruik van voorbepaalde kosten, (d) toerekening van niet-kostsoort-uitgaven (privé-uitgaven van bestuurder), (e) timing-verschil door periode-correctie.

**🛠️ Hoe**:

Onverklaarbare verschillen onderzoeken: typisch boekingsfout of vergeten verdeelboeking. Documenteer in verzoeningsdossier per kostencentrum.

**Grondslag**: CBN 3/3

### 5. Boek correctie of leg vast als legitiem verschil

Boekingsfouten corrigeren via tegen-/herboeking. Legitieme verschillen (interne verrekening, opportuniteitskost) vastleggen in periodeafsluitings-memo zodat audit traceerbaarheid behouden blijft.

**🛠️ Hoe**:

Uitsplitsing legitieme verschillen op afzonderlijke verschillen-rekeningen (klasse 98) zodat de samenhang met klasse 6 hersteld kan worden voor jaarrekening-doeleinden.

**Grondslag**: CBN 3/3 + [[verschillenboekhouding]]


## In de praktijk

<h3 id="algemene-versus-analytische-reconciliatie">Algemene-versus-analytische reconciliatie</h3>

> [!tip]- Algemene-versus-analytische reconciliatie
> Periodieke reconciliatie tussen klasse 6 (algemene) en klasse 9 (analytische) is een sleutel-controle. Verschillen mogen, maar moeten verklaarbaar zijn (interne verrekeningen, opportuniteitskost, verschillen tussen werkelijke en standaardkost). 🤖


## Bronnen

[^1]: `CBN-0003-03-advies-inzake-de-boekhoudkundige-verwerking-van-verrichtingen-van-tijdelijk__sec_methode-die-waarderingsneutraal-is-5-principes_part1`
