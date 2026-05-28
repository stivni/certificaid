---
title: "Eindejaarspremie"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.2.taak.3
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/eindejaarspremie.json"
---

# Eindejaarspremie

_Regime_

📋 Regeling · Anchors: `2.2.taak.3` · Wave: `skeleton-cross-cutting-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: 13e maand · eindejaarsuitkering

## Definitie

🔗 De eindejaarspremie is een jaarlijkse bijkomende bezoldiging, doorgaans betaald in december, waarvan de toekenning, de berekeningsbasis en het bedrag worden bepaald door de sectorale CAO van het bevoegde paritair comité (of bij ontstentenis door de individuele/bedrijfs-CAO). Anders dan de dertiende maand (= typisch één maandloon) kan een eindejaarspremie ook een vast forfaitair bedrag, een percentage van het jaarloon, of een combinatie zijn. Fiscaal en sociaal kwalificeert ze als gewone bezoldiging — volledig RSZ-onderworpen en aan bedrijfsvoorheffing volgens de afzonderlijke schaal voor 'exceptionele vergoedingen' (KB/WIB92 Bijlage III).

<small>📚 WIB92 — art. 31 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

🔗 De eindejaarspremie is in de praktijk vaak synoniem voor 'dertiende maand', maar het verschilt vooral in de berekeningsbasis: een eindejaarspremie kan een vast bedrag (bv. 500 EUR voor alle werknemers van een sector) zijn, of een percentage (bv. 8,33 % van het jaarloon — dat komt neer op één maandloon), of een combinatie (vast deel + variabel). Sectoraal levert dit verschillende uitkomsten op — vooral bij lage lonen waar een vast forfait relatief gunstiger is dan een percentage. Voor de werkgever blijft de boekhoudkundige behandeling identiek aan de dertiende maand: maandelijkse 1/12-provisioning en afrekening in december.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De eindejaarspremie ontstond uit CAO-onderhandelingen als instrument om koopkracht te verhogen zonder de wettelijke loonnorm te overschrijden. Sectoraal differentiëren onderhandelaars tussen 'dertiende maand' (afhankelijk van het loonniveau — gunstig voor hogere lonen) en 'forfaitaire eindejaarspremie' (gelijk voor alle werknemers — gunstig voor lagere lonen). De terminologie reflecteert de berekeningslogica, niet de juridische aard — fiscaal en sociaal zijn beide identiek behandeld.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: Sectorale CAO's; WIB92 art. 31; KB/WIB92 Bijlage III voor BV

Geen federale wettelijke verplichting; uitsluitend CAO-gestuurd.

**✅ Voor**
- 🔗 Werknemers in een paritair comité waarvan de CAO een eindejaarspremie voorziet. Sommige PC's leggen een vast forfait op (bv. 'Sociaal Fonds van de sector betaalt 500 EUR netto'), andere een percentage van het bruto-jaarloon.

**📋 Voorwaarden**
- 🔗 Sectoraal CAO-bepaald: minimum-anciënniteit, pro-rata-regels bij in-/uitdiensttreding, gelijkgestelde dagen voor schorsing. Sommige sectoren betalen via een Sociaal Fonds (= geen RSZ-werkgever-bijdrage op de werkgevers-zijde, omdat het Fonds de betaling doet).

## Bouwstenen

### ⚙️ Berekeningsvarianten eindejaarspremie  
_`mechanisme`_

🔗 Drie typische varianten in sectorale CAO's: (1) één maandloon van december (= equivalent dertiende maand); (2) percentage van het bruto-jaarloon (bv. 8,33 % ≈ 1/12); (3) vast forfait (bv. 500 EUR voor iedereen). Combinaties bestaan: vast deel + variabel. Pro-rata bij minder dan 12 maanden anciënniteit binnen het refertejaar volgens CAO-formule.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 BV — afzonderlijke schaal exceptionele vergoedingen  
_`regel`_

🔗 BV op de eindejaarspremie wordt berekend via KB/WIB92 Bijlage III — schaal van afzonderlijke aanslag voor exceptionele vergoedingen. Tarief hangt af van het bruto-jaarloon van de werknemer en levert typisch een hoger inhoudingspercentage dan op een gewoon maandloon. Definitieve afrekening in de personenbelasting van het volgende jaar.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Uitbetaling via Sociaal Fonds (sectoraal)  
_`mechanisme`_

🔗 In sommige sectoren (bv. bouwsector, horecasector, transportsector) wordt de eindejaarspremie niet door de werkgever zelf uitbetaald, maar door een sectoraal Sociaal Fonds. Werkgever betaalt een bijdrage aan het Fonds (klasse 64 of 62) en het Fonds betaalt vervolgens de premie aan de werknemer. Voor de werknemer: aparte loonfiche 281.10 of 281.18 (afhankelijk van fonds-statuut).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Forfaitaire eindejaarspremie € 500 (CAO vast bedrag) 🔗

_Sectorale CAO van Sven's PC voorziet een vaste eindejaarspremie van 500 EUR bruto voor alle werknemers met minstens 6 maanden anciënniteit. Sven heeft 8 maanden anciënniteit op refertedatum._

**Berekening:**
- Stap 1 — bruto premie: 500,00 EUR (sectoraal vast)
- Stap 2 — RSZ-werknemer 13,07 %: 500 × 13,07 % = 65,35 EUR
- Stap 3 — belastbaar: 500 − 65,35 = 434,65 EUR
- Stap 4 — BV afzonderlijke schaal (indicatief 23 % voor referte-jaarloon ≈ 42.000 EUR): 434,65 × 23 % ≈ 100 EUR — exacte schaal in Cijferzakboekje
- Stap 5 — netto: ≈ 335 EUR
- Stap 6 — werkgevers-RSZ 25 %: 125 EUR — totale loonkost 625 EUR

→ **Resultaat**: Werkgever betaalt 625 EUR loonkost; werknemer ontvangt ≈ 335 EUR netto. Op een vaste premie blijft door RSZ + BV ongeveer 2/3 over.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Eindejaarspremie als brutoloon-belasting-vrij beschouwen

**Verkeerde assumptie**: De eindejaarspremie wordt gegeven 'als cadeau' en is fiscaal voordelig of vrijgesteld.

**Kernpunt**: Geen enkele bijzondere vrijstelling — de eindejaarspremie is een gewone bezoldiging in de zin van art. 31 WIB92. Volledig RSZ-onderworpen + afzonderlijke BV-schaal (vaak hoger inhoudingspercentage dan gewoon maandloon). Werkelijk fiscaal-voordelige alternatieven: maaltijdcheques, ecocheques, warrants — geen eindejaarspremie.

<small>📚 WIB92 — art. 31 — _wettekst_</small>

### ⚠️ Eindejaarspremie vergelijken met dertiende maand zonder CAO te lezen

**Verkeerde assumptie**: De twee termen zijn altijd inwisselbaar — een eindejaarspremie is altijd één maandloon.

**Kernpunt**: Termen zijn niet juridisch gedefinieerd; de sectorale CAO bepaalt de exacte berekening. Eerst CAO-tekst lezen: sommige CAO's hebben 'eindejaarspremie' als forfait én 'dertiende maand' als maandloon — dat zijn dan twee verschillende toelagen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Uitbetaling via Sociaal Fonds = geen RSZ-werkgever-kost

**Verkeerde assumptie**: Als het Sociaal Fonds de premie betaalt, kost het de werkgever niets extra.

**Kernpunt**: De werkgever betaalt al een sectorale bijdrage aan het Fonds (typisch een percentage van de bruto-loonmassa). Die bijdrage dekt onder andere de eindejaarspremies. Boekhoudkundig zit de kost dus al in klasse 64 (sectorale bijdragen) of een sub-rekening 621 — niet zichtbaar als 'eindejaarspremie' op het grootboek.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Werkgever-cliënt

_De accountant die de loonprovisies en de december-loonafrekening verzorgt._

#### 📒 Boekhouder

##### 👣 Maandelijkse provisie + december-afrekening  
_`stap`_

🔗 Identieke aanpak als bij dertiende maand: maandelijks 1/12 op 620 + 621, credit 456/459 provisie. Bij sectorale uitbetaling via Sociaal Fonds: de werkgeversbijdrage aan het Fonds op 6203 of 621-sub, geen aparte loonboeking voor de werknemer. Wel de fiche 281.10 van de werkgever bevat het CAO-bedrag.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 CAO-impact op loonbudget  
_`vuistregel`_

🔗 Bij budgettering voor een nieuw boekjaar: ALTIJD de sectorale CAO checken voor de eindejaarspremie-formule. Een CAO-wijziging (bv. indexering vast forfait of percentage-verhoging) kan een significante invloed hebben op de jaarlijkse loonkost. Adviseur waarschuwt cliënt voor CAO-vernieuwingen in zijn PC.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Loon-en-payroll K-techniek (cascade-context) → [[loon-en-payroll]] _(moet-verwijzen)_
- ↪ Werknemers-vergoedingen Σ (alternatieven) → [[werknemers-vergoedingen]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[loon-en-payroll]]
### `vergelijkbaar_met`
- [[dertiende-maand]]
    - **Gelijkenissen**:
        - Beide jaarlijkse bijkomende bezoldigingen, uitbetaling december
        - Beide volledig RSZ-onderworpen + afzonderlijke BV-schaal
        - Beide CAO-gestuurd (geen federaal-wettelijke verplichting)
    - **Verschillen**:
        - Dertiende maand: bedrag = één maandloon (volledig of pro-rata)
        - Eindejaarspremie: kan vast forfait, percentage, of combinatie zijn — sectorale CAO bepaalt
        - Sommige sectoren hebben beide naast elkaar (= 13e maand + premie)
    - ⚠️ **Verwarringsrisico**: De termen worden in praktijk vaak door elkaar gebruikt; eerst sectorale CAO checken voor exacte berekening.
