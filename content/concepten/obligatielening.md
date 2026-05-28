---
title: "Obligatielening"
concept_type: "instrument"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 3.0.IV.D
tags:
  - concept
  - schema-2.2
  - type-instrument
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/obligatielening.json"
---

# Obligatielening

_Instrument_

📋 Regeling · Anchors: `3.0.IV.D` · Wave: `skeleton-vennootschapsrecht-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: bond issue · bondloan · uitgifte van obligaties — **Vertalingen**: fr: emprunt obligataire · en: bond issue

## Definitie

📖 Een obligatielening is een lening die door een vennootschap wordt aangegaan in de vorm van uitgifte van obligaties: meerdere verhandelbare effecten die elk eenzelfde schuldvordering vertegenwoordigen tegen eenzelfde nominale waarde. Elke obligatie is voor de houder het equivalent van een lening aan de uitgever; in ruil verbindt de uitgever zich tot terugbetaling van het kapitaal (nominale waarde) op een vastgelegde vervaldag en tot periodieke rentebetalingen ('coupons'). Naast de gewone obligatie bestaan varianten: converteerbare obligaties (conversierecht in aandelen), warrant-obligaties (obligatie + losse warrant), achtergestelde obligaties (lagere rang) en eeuwigdurende obligaties (geen vaste vervaldag).

<small>📚 CBN-advies 2019/07 — Inleiding - definitie obligatielening — _cbn_ · WVV — art. 7:54 — _wettekst_ · WVV — art. 5:32 — _wettekst_</small>

## Substantie

🔗 Het sleutelverschil met een banklening is dat een obligatielening wordt opgesplitst in stukken die elk verkocht worden aan een groep beleggers - de uitgevende vennootschap krijgt dus financiering van velen tegelijk, niet van één bank. Daardoor heeft de uitgever meer onderhandelingsruimte over rentevoet en voorwaarden (geen één bank die zijn convenanten oplegt), maar krijgt hij wel de complexiteit van een effecten-procedure: prospectus boven bepaalde drempels (FSMA, EU-prospectusverordening), notarisbetrokkenheid voor de uitgifte, en effectenpublicatie. Voor grote vennootschappen is dit een courante financieringsweg; voor KMO's blijft de banklening dominant. Voor de belegger is een obligatie een vastrentend instrument: lager risicoprofiel dan aandeel, maar wel kredietrisico op de uitgever.

<small>📚 Memorie van toelichting WVV (Parl. St. Kamer 54-3119/001) — Art. 5:32 + 7:54 - effecten-statuut — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De obligatielening combineert twee functies: financiering voor de vennootschap, beleggings-instrument voor de markt. Door de schuld in verhandelbare effecten te 'tokeniseren' kan ze opgedeeld worden over veel houders, en kan ieder van hen op elk moment verkopen op de markt zonder dat de vennootschap zelf moet herfinancieren. Dat verhoogt de liquiditeit voor de beleggers en daardoor wordt de gevraagde rente lager. De juridische bescherming van de obligatiehouder gebeurt typisch via een 'algemene vergadering van obligatiehouders' (analoog aan de aandeelhoudersvergadering) en eventueel via een trustee of bewaarder.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WVV art. 5:32-37 (BV) + 7:54-78 (NV) + EU-Prospectusverordening 2017/1129 + Belgische Prospectuswet 11-07-2018

**✅ Voor**
- 🔗 Financiering van grote bedragen (typisch boven 10-20 miljoen EUR) waar één bank te grote risicoconcentratie zou krijgen, of waar de uitgever onafhankelijkheid wil van een specifieke bankrelatie. Ook strategisch instrument voor groei-vennootschappen die hun investeerdersbasis willen verbreden.

**📋 Voorwaarden**
- 📖 Bevoegd orgaan: voor de NV beslist het bestuursorgaan over de uitgifte van gewone obligaties (art. 7:54 WVV) - de algemene vergadering enkel voor converteerbare obligaties en warrant-obligaties (omdat die de aandeelhoudersstructuur kunnen wijzigen). Voor de BV: bestuursorgaan of algemene vergadering volgens de statuten. Notariele akte vereist voor converteerbare obligaties en warrant-obligaties. Boven de prospectus-drempel (typisch 5 mio EUR over 12 maanden, met uitzonderingen): goedgekeurde prospectus door de FSMA.
- 📖 Nominale waarde minimum 25 EUR (BV); voor de NV is er geen wettelijke minimum-nominale, maar marktpraktijk legt typisch hogere drempels op.

**👍 Voordeel**
- 🔗 Financiering van zeer grote bedragen zonder afhankelijkheid van één bankrelatie. Doorgaans soepelere covenants dan bij een banklening. Aftrekbare rentekosten binnen de grenzen van art. 198/1 WIB92. Bij converteerbare en warrant-obligaties: lagere coupon dan bij gewone obligaties (de equity-kicker compenseert).

**⚠️ Risico**
- 🔗 Hoge transactiekosten bij uitgifte (prospectus, juristen, notariskosten, banking fee) - rendabel pas vanaf bepaalde uitgifte-omvang. Reputatierisico bij niet-betaling van een coupon: het wordt onmiddellijk publiek bekend, en de marktwaarde van de obligaties keldert. Bij genoteerde obligaties: doorlopende informatieverplichtingen onder de transparantiewet.

## Bouwstenen

### ⚙️ Varianten: gewone, converteerbare, warrant, achtergestelde, eeuwigdurende  
_`mechanisme`_

📖 (1) Gewone obligatie - klassiek schuldinstrument, terugbetaling op vervaldag tegen nominale waarde, periodieke coupons. (2) Converteerbare obligatie - geeft houder recht (of plicht) om in aandelen te converteren op vooraf bepaalde modaliteiten; conversie kan aan de obligatiehouder, de vennootschap of automatisch toebehoren. (3) Warrant-obligatie - obligatie + losse warrant die recht geeft op inschrijving op nieuwe aandelen; obligatie en warrant kunnen na uitgifte apart verhandeld worden. (4) Achtergestelde obligatie - klassieke obligatie maar in rang achter andere schuldeisers. (5) Eeuwigdurende obligatie - geen vaste vervaldag, wel rente; aflossing op initiatief van de uitgever (call) of houder (put). Convertibles en warrant-obligaties hebben hybride karakter en raken aan het aandelenkapitaal - daarom is bij hun uitgifte de algemene vergadering bevoegd.

<small>📚 WVV — art. 7:54 + 7:64-65 — _wettekst_ · WVV — art. 5:32 — _wettekst_ · CBN-advies 139/5 — Obligaties met warrant — _cbn_</small>

### 📜 Waardering op uitgiftewaarde + actuariële behandeling van agio/disagio  
_`regel`_

📖 Bij de uitgevende vennootschap worden obligatieleningen geboekt aan hun uitgiftewaarde (art. 3:51 KB WVV). Wanneer het actuariële rendement (berekend bij uitgifte met inachtneming van de terugbetalingswaarde op vervaldag) verschilt van het nominale rendement, wordt het verschil tussen uitgifteprijs en terugbetalingswaarde pro rata temporis over de resterende looptijd in resultaat genomen als bestanddeel van de rentekost. Dat gebeurt in beginsel op geactualiseerde basis (effectieve-rente-methode); de vennootschap kan kiezen voor lineaire spreiding of - bij geringe weerslag - de obligatielening voor haar uitgifteprijs in de balans behouden.

<small>📚 CBN-advies 2019/07 — Obligatielening - waardering en behandeling agio/disagio — _cbn_ · KB WVV — art. 3:51 — _kb_</small>

### 📜 Roerende voorheffing op coupons  
_`regel`_

📖 Op de rentebetalingen aan obligatiehouders is roerende voorheffing verschuldigd. Standaardtarief: 30% (art. 269 WIB92, sinds 2017). Bevrijdend bij particuliere belastingplichtigen voor wie het inkomen tot het privé-vermogen behoort. De uitgever houdt de RV in bij betaling van de coupon, stort ze door aan de fiscus en bezorgt aan de houder een fiscaal attest. Voor gebrachte coupons over een boekjaargrens: pro rata RV-boeking via rekening 491 ('verkregen opbrengsten') of 492 ('toe te rekenen kosten') op de actiefzijde.

<small>📚 WIB92 — art. 269 — _wettekst_ · CBN-advies 2018/14 — Roerende voorheffing - boekingsschema — _cbn_</small>

### 📜 Bevoegdheid: bestuursorgaan vs algemene vergadering  
_`regel`_

📖 Voor de NV beslist het bestuursorgaan over de uitgifte van gewone obligaties (art. 7:54 WVV). Voor converteerbare obligaties en warrant-obligaties is een besluit van de algemene vergadering vereist - ze raken aan de aandeelhoudersstructuur. De AV moet beslissen volgens de regels voor een statutenwijziging (3/4-meerderheid, aanwezigheidsquorum, verslag bestuursorgaan + commissaris). Voor de BV: de statuten bepalen de bevoegde organen; default is de algemene vergadering.

<small>📚 WVV — art. 7:54 — _wettekst_ · WVV — art. 7:64-65 — _wettekst_</small>

### 📜 Prospectusplicht (FSMA / EU-verordening)  
_`regel`_

📖 Voor een publieke aanbieding van obligaties is in beginsel een door de FSMA goedgekeurde prospectus vereist (EU-Prospectusverordening 2017/1129 + Belgische uitvoeringswet 11-07-2018). Drempels en vrijstellingen: aanbiedingen onder 5 miljoen EUR per 12 maanden zijn vrijgesteld (eventueel met informatienota vereist boven 500.000 EUR); aanbiedingen uitsluitend aan gekwalificeerde beleggers of aan minder dan 150 niet-gekwalificeerde beleggers per lidstaat zijn vrijgesteld. Voor niet-publieke uitgiftes (private placement) is geen prospectus nodig, maar wel een schriftelijke informatie aan de beleggers.

<small>📚 EU-Prospectusverordening 2017/1129 — art. 1 + 3 - prospectusplicht en vrijstellingen — _wettekst_ · Wet 11-07-2018 aanbieding beleggingsinstrumenten — art. 10 + 11 — _wettekst_</small>

### ⚙️ Obligatie met warrant - boekhoudkundige splitsing  
_`mechanisme`_

📖 Bij obligaties met warrant moet de aanschafprijs (bij koper) en de uitgifteprijs (bij uitgever) gesplitst worden over twee componenten: het schuldgedeelte (de obligatie) en het optie-gedeelte (de warrant). CBN 139/5 reikt verschillende methoden aan: (1) latere noteringssplitsing (waarde = totaalprijs * koers warrant / (koers obligatie + koers warrant)); (2) actuariële methode op basis van marktrente voor gewone obligaties met vergelijkbare kenmerken - het verschil tussen uitgifteprijs en actuariële waarde van de obligatie geldt als waarde van de warrant. Bij uitoefening van de warrant: betaling van de uitoefenprijs + uitgifte van nieuwe aandelen; de warrant-balanswaarde wordt afgeboekt naar het eigen vermogen (kapitaalverhoging).

<small>📚 CBN-advies 139/5 — Obligaties met warrant - splitsingsmethoden — _cbn_</small>

## Voorbeelden

### 💡 Gewone obligatielening met disagio (uitgifte onder pari) 🔗

_NV Aurelia geeft 1.000 obligaties uit met nominale waarde 1.000 EUR, coupon 3%, looptijd 5 jaar, bullet-aflossing. Uitgifteprijs: 980 EUR per obligatie (disagio van 20 EUR). Totaal uitgegeven: 980.000 EUR; totale terugbetalingswaarde op vervaldag: 1.000.000 EUR._

**Boeking:**


**Berekening:**
- Stap 1 - disagio = 1.000.000 - 980.000 = 20.000 EUR; te spreiden over 5 jaar.
- Stap 2 - lineaire spreiding (toegelaten optie volgens CBN 2019/07): 20.000 / 5 = 4.000 EUR per jaar bijkomende rentekost.
- Stap 3 - jaarlijkse coupon: 1.000 obligaties x 1.000 EUR nominaal x 3% = 30.000 EUR. RV 30%: 9.000 EUR in te houden; 21.000 EUR uitbetaald aan houders.
- Stap 4 - totale jaarlijkse rentekost in de resultatenrekening: 30.000 (coupon) + 4.000 (disagio-spreiding) = 34.000 EUR. Effectief rendement voor de obligatiehouder is daardoor hoger dan de nominale 3%.
- Stap 5 - bij vervaldag: D 170 1.000.000 | C 55 1.000.000 (terugbetaling tegen nominale waarde); 170 was na 5 jaar bijgeschreven tot 1.000.000 via de disagio-toevoegingen.

**Boeking:**


<small>📚 CBN-advies 2019/07 — Behandeling agio/disagio — _cbn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Obligatielening verwarren met aandelenuitgifte

**Verkeerde assumptie**: Een obligatielening verhoogt het eigen vermogen van de vennootschap.

**Kernpunt**: Een gewone obligatielening is vreemd vermogen - schuldverbintenis met terugbetalingsplicht. Het eigen vermogen blijft ongewijzigd. Pas bij conversie van een converteerbare obligatie naar aandelen (of uitoefening van een warrant) wordt een deel omgezet in eigen vermogen. Vergelijk de balansrubriek: obligaties = VIII.A.1 (rekening 170-171); aandelen = I.A (rekening 100/111).

<small>📚 CBN-advies 2019/07 — Definitie obligatielening - schuldinstrument — _cbn_</small>

### ⚠️ Disagio of agio in één keer als rentekost nemen

**Verkeerde assumptie**: Bij uitgifte onder pari (disagio) komt het verschil ineens in de rentekost van het uitgiftejaar.

**Kernpunt**: Het verschil tussen uitgifteprijs en terugbetalingswaarde wordt pro rata temporis gespreid over de looptijd - in beginsel actuarieel (effectieve-rente), bij wijze van uitzondering lineair (CBN 2019/07 optie 1) of niet wanneer de weerslag verwaarloosbaar is (optie 2). In één keer in resultaat nemen vertekent zowel het resultaat van het uitgiftejaar als de rentekost in latere jaren.

<small>📚 CBN-advies 2019/07 — Spreiding disagio/agio — _cbn_</small>

### ⚠️ Roerende voorheffing op bruto-coupon vergeten

**Verkeerde assumptie**: De rentekost in de boekhouding van de uitgever is gelijk aan het bedrag dat effectief naar de houders gaat.

**Kernpunt**: De brutocoupon (rentekost) wordt geboekt op rekening 650; de RV (30%) wordt apart ingehouden en doorgestort aan de fiscus via rekening 453. De uitgever moet zorgen voor tijdige aangifte 273 en doorstortingen. Bij gemiste RV-aangiftes: boete + nalatigheidsinterest, ook indien het gaat om eigen vergissingen van de uitgever (RV is een persoonlijke schuld van de uitkerende vennootschap).

<small>📚 CBN-advies 2018/14 — Roerende voorheffing - boekingstabel — _cbn_</small>

## Accountant-perspectieven

### Uitgevende vennootschap

_De accountant of bedrijfsrevisor die de uitgifte begeleidt en de daaropvolgende boekhoudkundige verwerking opvolgt._

#### 👥 Begeleider

##### 👣 Voorbereiding van een obligatie-uitgifte  
_`stap`_

🔗 Bepaal de modaliteit (gewone / converteerbaar / met warrant / achtergesteld). Stel met juridisch adviseur het uitgiftecontract op. Controleer of bovendrempelse prospectusplicht ontstaat - zo ja, doorloop FSMA-procedure (kostbaar en tijdrovend). Bij converteerbare of warrant-obligaties: bereid het besluit van de algemene vergadering voor met verslag bestuursorgaan + verslag commissaris. Maak een financieringsplan dat de coupon-betalingen en de eindterugbetaling realistisch positioneert tegenover de verwachte kasstromen.

<small>📚 WVV — art. 7:54 + 7:64 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📒 Boekhouder

##### 👣 Verwerking uitgifte, coupons en eindaflossing  
_`stap`_

📖 Bij uitgifte: D 55 (uitgifteprijs ontvangen) | C 170-171 obligatieleningen (uitgifteprijs). Disagio/agio: spreiden via correctie op 170/171 + rentelast op 650. Bij elke coupon: D 650 brutocoupon | C 453 RV + C 55 nettocoupon. Bij eindaflossing: D 170 | C 55. Indien obligatie converteerbaar: bij conversie D 170 | C 100/111 (kapitaal/inbreng) + eventueel C 1100 uitgiftepremie - geen kasbeweging. Bij warrant-obligatie: aparte boekingen voor obligatie en warrant volgens splitsingsmethode CBN 139/5.

<small>📚 CBN-advies 2019/07 — Boekhoudkundige verwerking obligatielening — _cbn_ · CBN-advies 139/5 — Obligaties met warrant — _cbn_ · CBN-advies 2018/14 — Roerende voorheffing — _cbn_</small>

## Verder lezen (scope-out)

- → Eigen vermogen - afbakening vreemd vs eigen → [[eigen-vermogen]] _(moet-verwijzen)_
- → Kapitaalverhoging - alternatief als financieringsbron → [[kapitaalverhoging]] _(moet-verwijzen)_
- → Banklening - primaire vergelijking als bilaterale schuld → [[banklening-investeringskrediet]] _(moet-verwijzen)_
- → Achtergestelde lening - variant in rangorde → [[achtergestelde-lening]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- ⏳ lening
### `vergelijkbaar_met`
- [[banklening-investeringskrediet]]
    - **Gelijkenissen**:
        - Beide zijn vreemd vermogen op meer dan een jaar
        - Beide genereren rentekost aftrekbaar binnen art. 198/1 WIB92
    - **Verschillen**:
        - Obligatielening: effecten-instrument, verhandelbaar, uitgegeven aan veelheid van investeerders, prospectusplicht boven drempels
        - Banklening: bilaterale overeenkomst met één kredietinstelling, geen effecten, geen prospectus
        - Obligatielening: vaste coupon, vaste vervaldag, bullet typisch
        - Banklening: amortizing of annuïtair typisch, individuele waarborgen + covenants
    - ⚠️ **Verwarringsrisico**: Beide eindigen in rubriek VIII.A van het passief, maar op verschillende subrekeningen: 170-171 voor obligaties, 173-174 voor bankleningen.
- [[achtergestelde-lening]]
    - **Gelijkenissen**:
        - Beide zijn vreemd vermogen
        - Beide kunnen achtergesteld zijn (achtergestelde obligaties bestaan)
    - **Verschillen**:
        - Obligatielening is per definitie effecten-instrument; achtergestelde lening is meestal bilaterale schuld
        - Achtergestelde lening = rangorde-keuze; obligatie = vorm van het instrument
    - ⚠️ **Verwarringsrisico**: Achtergestelde obligaties combineren beide concepten - dan geldt het regime van de obligatielening + achterstellingsclausule.
- [[kapitaalverhoging]]
    - **Gelijkenissen**:
        - Beide zijn financieringsbronnen die op de kapitaalmarkt worden opgehaald
        - Beide bouwen op aanbod en vraag van investeerders
    - **Verschillen**:
        - Kapitaalverhoging = eigen vermogen (aandelen, geen terugbetalingsplicht, dividenduitkering afhankelijk van winst en kapitaalbescherming)
        - Obligatielening = vreemd vermogen (terugbetaling verplicht, rente niet afhankelijk van winst, geen stemrecht)
        - Aandeelhouders dragen ondernemingsrisico volledig; obligatiehouders krijgen voorrang bij vereffening
    - ⚠️ **Verwarringsrisico**: Bij een converteerbare obligatie of een warrant-obligatie loopt het onderscheid niet meer scherp - het instrument start als schuld en kan in eigen vermogen omgezet worden. Boekhoudkundige verwerking moet de twee componenten splitsen.
