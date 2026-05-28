---
title: "Volstortingsplicht"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 3.0.IV.A
  - 3.0.I.C
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/volstortingsplicht.json"
---

# Volstortingsplicht

_Regime_

📋 Regeling · Anchors: `3.0.IV.A` · `3.0.I.C` · Wave: `skeleton-vennootschapsrecht-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: volstortingsverplichting · paying-up obligation — **Vertalingen**: fr: obligation de libération

## Definitie

📖 De volstortingsplicht is de verbintenis van iedere aandeelhouder om de inbreng die hij bij inschrijving op aandelen aan de vennootschap heeft beloofd, ook effectief te storten in geld of te leveren in natura. De plicht ontstaat bij oprichting en bij elke latere uitgifte van aandelen (kapitaalverhoging). Het niet-opgevraagde gedeelte blijft een vordering van de vennootschap op de aandeelhouder en wordt op de balans zichtbaar (rekening 101 'Niet opgevraagd kapitaal' bij de NV, of een vergelijkbare subrekening van 111 bij de kapitaalloze BV).

<small>📚 WVV — art. 1:9 §1 — _wettekst_ · WVV — art. 7:11 — _wettekst_ · CBN-advies 2020/01 — Rekeningenstelsel - rekening 101 / 111 — _cbn_</small>

## Substantie

🔗 Inschrijving op een aandeel is een belofte. Volstorting is de uitvoering van die belofte. Tussen die twee momenten kan tijd zitten - en het WVV laat de partijen veel speelruimte om dat te regelen. De vennootschap kan daardoor 'kapitaal op afroep' organiseren: aandeelhouders verbinden zich, het bestuursorgaan haalt het geld op wanneer het nodig is. De wet beschermt twee belangen tegelijk: dat van de vennootschap (zekerheid dat ze ooit haar geld krijgt) en dat van de schuldeisers (dat er een opvraagbaar bedrag in reserve zit als de vennootschap in problemen geraakt). Een niet-volgestort aandeel is dus tegelijk een eigen-vermogenspost en een schuldvordering.

<small>📚 WVV — art. 1:9 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De volstortingsplicht is de input-zijde van het kapitaalbeschermingsregime. Beperkte aansprakelijkheid van aandeelhouders heeft als tegenwicht dat het beloofde vermogen ook werkelijk in de vennootschap komt - anders zou de schuldeisersbuffer fictief blijven. Bij de NV blijft een minimumkapitaal van 61.500 EUR formeel vereist en moet dat bij oprichting volledig volgestort zijn (samen met minstens een vierde van elk aandeel). Bij de BV werd het minimumkapitaal afgeschaft (WVV 2019), maar de plicht blijft bestaan: iedere vennoot is verschuldigd 'wat hij heeft beloofd in te brengen' (art. 1:9 WVV) - vrijheid voor de partijen, maar wel afdwingbaar.

<small>📚 WVV — art. 1:9 §1 — _wettekst_ · WVV — art. 7:11 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2019-05-01** · basis: WVV (Wet 23-03-2019) - art. 1:9 algemeen, art. 5:8 BV, art. 7:11 NV, art. 7:66 hoofdelijkheid bij overdracht

Bij het WVV (2019) werd het kapitaalbegrip voor de BV afgeschaft. De inbrengplicht zelf bleef bestaan, maar zonder minimumbedrag en met statutaire vrijheid voor de timing van volstorting. Bij de NV bleef de oude logica met minimumkapitaal en 25%-regel bij inschrijving.

**✅ Voor**
- 📖 Elke initiële inschrijving op aandelen bij oprichting en elke nieuwe uitgifte van aandelen bij kapitaalverhoging - in geld of in natura, in elke vennootschapsvorm met aandelen (BV, NV, CV).

**📋 Voorwaarden**
- 📖 Bij de NV: minimum 25% per aandeel volgestort bij inschrijving (art. 7:11 WVV), en het minimumkapitaal van 61.500 EUR moet bij oprichting volledig volgestort zijn. Bij de BV: behoudens andersluidende statutaire bepalingen wordt de inbreng onmiddellijk volledig volgestort - statuten kunnen anders bepalen (gespreide volstorting, oproepschema). Inbreng in natura: integrale volstorting binnen 5 jaar (in beginsel onmiddellijk).

**▶️ Trigger start**
- 📖 (1) Oprichting van de vennootschap - aandeelhouders schrijven in op aandelen; (2) Kapitaalverhoging - bestaande of nieuwe aandeelhouders schrijven in op nieuwe aandelen; (3) Overdracht van een niet-volgestort aandeel - overdrager en overnemer worden hoofdelijk gehouden.

**⏹ Trigger einde**
- 🔗 Volledige volstorting van het beloofde bedrag - de schuldvordering van de vennootschap wordt geboekt-tegen-cash en de niet-opgevraagd-rubriek verdwijnt van de balans.

**⚠️ Risico**
- 📖 Bij wanbetaling van de opvraging: van rechtswege en zonder ingebrekestelling interest op het verschuldigde bedrag (art. 1:9 §2 WVV). Daarnaast kan het bestuursorgaan - of het stemrecht schorsen voor de niet-volgestorte aandelen, - of na een rappel-procedure overgaan tot gedwongen verkoop van de aandelen aan derden of inkoop door de vennootschap.
- 📖 Wie een niet-volgestort aandeel overdraagt blijft hoofdelijk gehouden tot volstorting samen met de overnemer (en alle latere overnemers). Een statutaire of contractuele uitsluiting van die hoofdelijkheid heeft geen werking tegenover de vennootschap of derden. Wel kan de overdrager intern regres uitoefenen op de overnemer.

## Bouwstenen

### 📏 25%-volstorting per aandeel (NV)  
_`drempel`_

📖 Bij de oprichting of bij elke kapitaalverhoging van een NV moet elk aandeel ten minste voor een vierde (25%) volgestort zijn op het moment van inschrijving. Het minimumkapitaal van 61.500 EUR moet bovendien volledig volgestort zijn. Het resterende saldo blijft een vordering van de vennootschap op de aandeelhouder, boekhoudkundig zichtbaar als negatieve post 'Niet opgevraagd kapitaal' (rekening 101) onder het geplaatst kapitaal.

<small>📚 WVV — art. 7:11 — _wettekst_ · CBN-advies 2020/01 — Rekeningenstelsel post 101 — _cbn_</small>

### 📜 BV - statutaire vrijheid voor volstortingstiming  
_`regel`_

📖 Bij de BV (kapitaalloos sinds WVV 2019) is er geen minimumbedrag en geen 25%-regel. De statuten bepalen de timing: onmiddellijke volledige volstorting, gespreide volstorting, oproepschema, ... Behoudens andersluidende statutaire bepalingen geldt onmiddellijke volledige volstorting als default. Het niet-opgevraagde gedeelte wordt geboekt op een subrekening van 111 (onbeschikbare inbreng buiten kapitaal).

<small>📚 WVV — art. 5:8 — _wettekst_ · CBN-advies 2019/14 — Inbreng in een vanaf 1 mei 2019 opgerichte BV — _cbn_</small>

### 📜 Wettelijke interest bij niet-tijdige volstorting  
_`regel`_

📖 De schuldenaar van een inbreng in geld is van rechtswege en zonder ingebrekestelling de interest op die som verschuldigd, te rekenen vanaf de dag waarop ze opeisbaar was. Geen formele aanmaning vereist - automatisch. De interestvoet is in beginsel de wettelijke interest, tenzij de statuten of het oproepschema een hogere afdoende rente bedingen.

<small>📚 WVV — art. 1:9 §2 1° — _wettekst_</small>

### 📜 Hoofdelijkheid bij overdracht van niet-volgestort aandeel  
_`regel`_

📖 Wie een niet-volgestort aandeel overdraagt blijft hoofdelijk gehouden samen met de overnemer (en alle latere overnemers) tegenover de vennootschap en tegenover derden. Een statutair of contractueel beding dat de hoofdelijkheid uitsluit, heeft geen werking. De vennootschap kan elke schuldenaar voor het geheel aanspreken. De overdrager die heeft betaald kan regres uitoefenen op de overnemer en latere overnemers.

<small>📚 WVV — art. 7:66 — _wettekst_</small>

### ⚙️ Opvraging door het bestuursorgaan  
_`mechanisme`_

🔗 Het niet-opgevraagde gedeelte is een latent vermogen: de vennootschap heeft het al op de balans staan als (negatieve) eigen-vermogenspost, maar moet het nog effectief opvragen om er over te beschikken. De beslissing tot opvraging behoort tot de bevoegdheid van het bestuursorgaan (statuten kunnen specificeren). De oproep gebeurt typisch bij aangetekende brief met een betalingstermijn. Bij niet-betaling: ingebrekestelling, daarna sancties (interest, schorsing stemrecht, gedwongen verkoop).

<small>📚 WVV — art. 1:9 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Balansweergave rekening 101 (NV) en 111 (BV)  
_`begrip`_

📖 Bij de NV staat het geplaatst kapitaal in rekening 100 (positief) en het niet-opgevraagde gedeelte in rekening 101 'Niet opgevraagd kapitaal (-)' (negatief). Het nettobedrag van de eigen-vermogensrubriek I.A. = 100 - 101 = effectief gestort kapitaal. Bij de BV werden de oude 100/101-saldi bij omvorming overgeboekt naar 1119 'Andere onbeschikbare inbreng buiten kapitaal', met een afzonderlijke subrekening voor het niet-opgevraagde gedeelte.

<small>📚 CBN-advies 2020/01 — 11 Inbreng buiten kapitaal + Kapitaalloze vennootschappen — _cbn_ · CBN-advies 2019/14 — Omvorming kapitaal - boekingsschema — _cbn_</small>

## Voorbeelden

### 💡 NV-oprichting met gespreide volstorting 🔗

_Vier oprichters richten NV Aurelia op met een geplaatst kapitaal van 100.000 EUR (verdeeld over 1.000 aandelen van 100 EUR nominale waarde). Ze besluiten 30% per aandeel bij inschrijving te volstorten._

**Berekening:**
- Stap 1 - controle minimumvolstorting per aandeel: 30% > 25% (art. 7:11) -> OK.
- Stap 2 - controle minimumkapitaal: minimum 61.500 EUR moet volledig volgestort zijn. Volgestort = 30% x 100.000 = 30.000 EUR. Dit is < 61.500 EUR -> probleem. De oprichters moeten meer storten om aan het minimumkapitaal te voldoen.
- Stap 3 - oplossing: stort 61.500 EUR (volledig minimumkapitaal) + 25% van de resterende 38.500 EUR = 61.500 + 9.625 = 71.125 EUR. Dat overschrijdt de 30%-regel ruim.
- Stap 4 - of: verlaag het geplaatst kapitaal naar bv. 61.500 EUR (volledig volgestort) en breng het verschil als uitgiftepremie.
- Stap 5 - balansweergave (eenvoudige variant met 61.500 EUR volstort + 38.500 EUR niet-opgevraagd):

→ **Resultaat**: Rekening 100 = 100.000 (credit, geplaatst kapitaal); rekening 101 = 38.500 (debet, niet opgevraagd kapitaal). Netto in eigen vermogen: 61.500 EUR effectief gestort.

**Boeking:**


<small>📚 WVV — art. 7:11 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Hoofdelijke gehoudenheid bij overdracht 📖

_Aandeelhouder A van NV Aurelia houdt 100 aandelen aan waarvan 70% niet-volgestort. Hij verkoopt deze aandelen aan B. Twee jaar later vraagt het bestuursorgaan het saldo op: 100 aandelen x 100 EUR x 70% = 7.000 EUR._

**Weergave** `stappenlijst`:

```json
{
  "stappen": [
    "Stap 1 - vennootschap richt opvraging aan B (overnemer). B betaalt niet.",
    "Stap 2 - vennootschap mag ook A (overdrager) aanspreken: A en B zijn hoofdelijk gehouden, ondanks elk hiermee strijdig beding.",
    "Stap 3 - A betaalt 7.000 EUR aan de vennootschap.",
    "Stap 4 - A heeft regres op B voor het volledige bedrag (en op latere overnemers indien meerdere doorverkopen waren gebeurd).",
    "Stap 5 - eventueel bedingen tussen A en B over wie uiteindelijk de last draagt, hebben enkel intern werking; tegenover de vennootschap blijven beiden hoofdelijk gehouden."
  ]
}
```

<small>📚 WVV — art. 7:66 — _wettekst_</small>

## Valkuilen

### ⚠️ Geplaatst = volgestort verwarren

**Verkeerde assumptie**: Het 'kapitaal' van de vennootschap op de balans is wat de aandeelhouders al hebben ingebracht.

**Kernpunt**: Het geplaatste kapitaal (rekening 100) is het beloofde bedrag bij inschrijving. Wat al effectief is binnengekomen, is geplaatst minus niet-opgevraagd (rekening 101). De netto-actief-test gebruikt het 'gestorte of, indien hoger, opgevraagde kapitaal' - niet het geplaatste. Wie deze nuance mist, overschat het uitkeerbare bedrag en de schuldeisersbuffer.

<small>📚 CBN-advies 2021/02 — Vaststelling referentiebedrag - 'gestort of opgevraagd kapitaal' — _cbn_</small>

### ⚠️ Denken dat de BV geen volstortingsplicht meer heeft

**Verkeerde assumptie**: Bij de BV is er geen kapitaal meer, dus ook geen volstortingsplicht.

**Kernpunt**: Het kapitaalbegrip is afgeschaft, niet de inbrengplicht. Art. 1:9 WVV is heel duidelijk: iedere vennoot is aan de vennootschap verschuldigd wat hij heeft beloofd in te brengen. De BV heeft enkel meer vrijheid om de timing statutair te regelen. Default is onmiddellijke volledige volstorting (CBN 2019/14).

<small>📚 WVV — art. 1:9 — _wettekst_ · CBN-advies 2019/14 — Inbreng in een vanaf 1 mei 2019 opgerichte BV — _cbn_</small>

### ⚠️ Aandelen verkopen denkende daarmee de volstortingsplicht door te schuiven

**Verkeerde assumptie**: Eens ik mijn niet-volgestorte aandelen overdraag, ben ik van de plicht af.

**Kernpunt**: Art. 7:66 WVV maakt overdrager en overnemer hoofdelijk gehouden, ongeacht enig andersluidend beding. De vennootschap kan de overdrager nog jaren later aanspreken. Wie dit risico wil afdekken: de aandelen eerst zelf volstorten of in de overdrachtsovereenkomst een afdoende waarborg laten stellen door de overnemer.

<small>📚 WVV — art. 7:66 — _wettekst_</small>

## Accountant-perspectieven

### Eigen kantoor (oprichter of cliënt-vennootschap)

_De accountant die meekijkt bij oprichting, kapitaalverhoging of overdracht van aandelen._

#### 👥 Begeleider

##### 👣 Controle bij oprichting - 25%-regel en minimumkapitaal NV  
_`stap`_

🔗 Bij elke NV-oprichting: check dat per aandeel minstens 25% is volgestort en dat het minimumkapitaal van 61.500 EUR volledig is volgestort. Bij een BV-oprichting: lees de statuten - default is onmiddellijke volledige volstorting; bij gespreide volstorting controle van het oproepschema. Het financieel plan moet aantonen dat de inbreng voldoende is voor de geplande activiteit (een onbestaande of ondergedimensioneerde inbreng creëert oprichtersaansprakelijkheid - art. 5:16 BV / 7:18 NV).

<small>📚 WVV — art. 7:11 — _wettekst_ · WVV — art. 5:8 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📒 Boekhouder

##### 👣 Boeken van een opvraging en latere volstorting  
_`stap`_

🔗 Bij oprichting: D 55 (bank, voor gestort bedrag) + D 101 (niet-opgevraagd, voor saldo) | C 100 (geplaatst kapitaal). Bij latere opvraging: D 416 (te innen opbrengsten, of vergelijkbare debiteurenrekening) | C 101 (niet-opgevraagd kapitaal - de balanspost verschuift naar een opvorderbare vordering). Bij effectieve ontvangst: D 55 (bank) | C 416. Bij de BV: zelfde principes, maar met rekening 1119/111 in plaats van 100/101.

<small>📚 CBN-advies 2020/01 — Rekeningenstelsel - migratie 100/101 -> 111 — _cbn_ · CBN-advies 2019/14 — Omvorming kapitaal - boekingsschema — _cbn_</small>

## Verder lezen (scope-out)

- → Aandeel als onderliggend instrument → [[aandeel]] _(moet-verwijzen)_
- → Kapitaalverhoging als trigger voor nieuwe volstortingsplicht → [[kapitaalverhoging]] _(moet-verwijzen)_
- → Oprichting van de vennootschap als initieel trigger-moment → [[oprichting-vennootschap]] _(moet-verwijzen)_
- ↪ Kapitaalbescherming als output-zijde (uitkeringstesten) → [[kapitaalbescherming]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- ⏳ vennootschapsrecht
### `vereist`
- [[aandeel]] — Volstortingsplicht koppelt zich altijd aan een onderliggend aandeel - geen aandeel, geen volstorting.
### `triggert`
- [[oprichting-vennootschap]]
- [[kapitaalverhoging]] — Elke nieuwe uitgifte van aandelen creëert nieuwe volstortingsverbintenissen.
### `vergelijkbaar_met`
- [[kapitaalbescherming]]
    - **Gelijkenissen**:
        - Beide regimes beschermen schuldeisers door eigen vermogen in de vennootschap te houden
        - Beide werken via een dwingende juridische verplichting met aansprakelijkheidsgevolgen
    - **Verschillen**:
        - Volstortingsplicht werkt aan de inbreng-zijde (input): de aandeelhouder moet beloofd vermogen storten
        - Kapitaalbescherming werkt aan de uitkerings-zijde (output): vermogen mag niet terugvloeien zonder testen
        - Volstortingsplicht is een persoonlijke verbintenis van de aandeelhouder; kapitaalbescherming is een verplichting voor het bestuursorgaan
    - ⚠️ **Verwarringsrisico**: Beide horen in dezelfde 'kapitaalbeschermings'-familie. Houd ze didactisch gescheiden: input (volstorting) vs output (uitkeringstesten).
