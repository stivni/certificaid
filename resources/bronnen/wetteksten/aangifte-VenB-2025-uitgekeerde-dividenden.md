---
tags: ["2.3"]
itaa-lex-sectie: ""
wet: "aangifte-VenB-2025-uitgekeerde-dividenden"
bron_rol: "formulier"
status: "beschikbaar"
bijgewerkt: "2025"
bron: "FOD Financiën — modelformulier 275.1 + toelichting"
chunk:
  level: 2
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/handcrafted/aangifte-VenB-2025-uitgekeerde-dividenden.md
      sha256: 9fd48e0c0465d7da7001e7fa8f22640820742b065090d5fe35e0a3022b113ce7
      version:
      pages:
  tooling:
    pipeline: manual-import
    pipeline_version: be14c139
    model:
    prompt_version:
  generated_at: '2026-05-21T17:17:19Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-21T17:45:05Z'
    confirmed_by: subagent-qa-batch-aangifte-venb-2025
    rationale: Alle 8 codes (1301, 1302, 1303, 1305, 1306, 1320, 1322, 1340) verbatim verified tegen voorbereiding-p6-7. Wetsartikelen (art. 18, 186, 187, 209, 210 § 1, 184quater, 541, 219quater, 206/4 vierde lid, 207 zevende lid) letterlijk in toelichting-regels 1867-2003. Alle ⚖️-claims grounded.
    caveat:
    layer1:
      status: pass
      run_id: 20260521-173837
      run_at: '2026-05-21T17:38:37Z'
      heading_count: 9
      max_section_chars: 12271
      file_size_chars: 17926
      flags: []
    layer2:
      status: trusted
      agent: subagent-qa-batch-aangifte-venb-2025
      run_at: '2026-05-21T17:45:05Z'
      rationale: Alle 8 codes (1301, 1302, 1303, 1305, 1306, 1320, 1322, 1340) verbatim verified tegen voorbereiding-p6-7. Wetsartikelen (art. 18, 186, 187, 209, 210 § 1, 184quater, 541, 219quater, 206/4 vierde lid, 207 zevende lid) letterlijk in toelichting-regels 1867-2003. Alle ⚖️-claims grounded.
      concrete_problemen: []
---

# Aangifte VenB aanslagjaar 2025 — codes vakken Uitgekeerde dividenden + Buitenlandse winst die geniet van een verminderde belasting

> **Bron**: "Aangifte in de vennootschapsbelasting — aanslagjaar 2025" (modelformulier 275.1, blz. 6–7) + "Toelichting bij de aangifte in de vennootschapsbelasting — aanslagjaar 2025" (toelichting bij de vakken Uitgekeerde dividenden en Buitenlandse winst die geniet van een verminderde belasting, blz. 26–27 van de toelichting).
> - Aangifte: <https://financien.belgium.be/sites/default/files/121-aangifte-venb-2025.pdf>
> - Toelichting: <https://financien.belgium.be/sites/default/files/121-aangifte-venb-toelichting-2025.pdf>
>
> Gepubliceerd door FOD Financiën. Geraadpleegd 2026-05-21.
> Codes zijn verbatim overgenomen uit de officiële voorbereiding van de aangifte (blz. 6–7).
>
> Het vak Uitgekeerde dividenden volgt direct op het vak Verworpen uitgaven. Het eindbedrag (code **1320**) stroomt door naar de Uiteenzetting van de winst (zie het canonieke document over dat vak).

---

## C. Uitgekeerde dividenden (blz. 6)

> **Algemene afbakening** ⚖️: bedoeld zijn de uitgekeerde dividenden, met uitzondering van het gedeelte van de dividenden die aan natuurlijke personen worden toegekend door volgens art. 8:4 WVV erkende coöperatieve vennootschappen, voor zover dat gedeelte niet meer bedraagt dan **200 euro per natuurlijke persoon**.

### Componenten van de uitgekeerde dividenden

| Rubriek | Omschrijving | Code |
|---|---|---|
| a | **Gewone dividenden** — alle dividenden andere dan de hierna onder b) tot d) bedoelde verrichtingen (zie didactische blockquote hieronder voor de inhoud) | **1301** |
| b | **Verkrijging van eigen aandelen** — positief verschil tussen verkrijgingsprijs (of waarde) van de aandelen en het gedeelte van het gerevaloriseerde gestorte kapitaal dat de verkregen aandelen vertegenwoordigen (art. 186 WIB 92) | **1302** |
| c | **Overlijden, uittreding of uitsluiting van een vennoot** — positief verschil tussen de uitkeringen/toekenningen (in geld, in effecten of in enige andere vorm) aan de belanghebbende of zijn rechthebbenden, en zijn aandeel in het gerevaloriseerde gestorte kapitaal (art. 187 WIB 92) | **1303** |
| d (deel 1) | **Gedeelte van de verdeling van maatschappelijk vermogen dat voortkomt van een vermindering van de liquidatiereserve** (art. 184quater WIB 92) **en van een vermindering van de bijzondere liquidatiereserve** (art. 541 WIB 92) | **1305** |
| d (deel 2) | **Verdeling van maatschappelijk vermogen na aftrek** van het gedeelte dat voortkomt van een vermindering van de liquidatiereserve en van een vermindering van de bijzondere liquidatiereserve — positief verschil tussen de uitkeringen en het gerevaloriseerde gestorte kapitaal (art. 209, eerste lid, WIB 92) | **1306** |

### Eindsom vak Uitgekeerde dividenden

| Subtotaal | Omschrijving | Code |
|---|---|---|
| **Uitgekeerde dividenden** | Totaal van de regels **1301 + 1302 + 1303 + 1305 + 1306**. Wordt overgedragen naar de Uiteenzetting van de winst. | **1320** |

### Aanvinkvakje aangifte roerende voorheffing

| Rubriek | Omschrijving | Code |
|---|---|---|
| — | **Verklaring 273 A**: de vennootschap is op de hoogte van haar verplichting om een aangifte in de roerende voorheffing (aangifteformulier 273 A) in te dienen wanneer ten minste één van de rubrieken regels **1301**, **1302**, **1303** of **1306** is ingevuld, **zelfs wanneer geen roerende voorheffing is verschuldigd** | **1322** |

---

## Inhoud per rubriek — wat hoort wáár?

> **a) Gewone dividenden (code 1301)** ⚖️ — vier deelcategorieën:
> 1. Het gedecreteerde bedrag van de dividenden, evenals alle voordelen toegekend aan aandelen en winstbewijzen, hoe ook genaamd, ongeacht uit welken hoofde en op welke wijze die toekenning plaatsvindt.
> 2. Gehele of gedeeltelijke terugbetalingen van kapitaal, **met uitzondering** van de terugbetalingen die volgens art. 18, tweede lid, WIB 92 geacht worden voort te komen uit het gestort kapitaal of uit met gestort kapitaal gelijkgestelde uitgiftepremies en andere bedragen waarop bij uitgifte is ingeschreven, en die zijn verkregen ter uitvoering van een regelmatige beslissing van de vennootschap overeenkomstig het WVV (of, indien de vennootschap niet onder het WVV ressorteert, volgens het recht dat haar beheerst).
> 3. Gehele of gedeeltelijke terugbetalingen van uitgiftepremies en andere bedragen waarop ter gelegenheid van de uitgifte van aandelen of winstbewijzen is ingeschreven, met dezelfde uitzondering als hierboven (art. 184, tweede lid, WIB 92 + art. 18, tweede lid, WIB 92).
> 4. Interesten van voorschotten zoals bedoeld in art. 18, achtste lid, WIB 92, wanneer één van de in art. 18, eerste lid, 4° WIB 92 bedoelde grenzen wordt overschreden en in de mate van die overschrijding.

> **b) Verkrijging van eigen aandelen (code 1302)** ⚖️ — art. 186 WIB 92:
> Wanneer een vennootschap op enige wijze eigen aandelen verkrijgt, moet in beginsel het positieve verschil worden aangegeven tussen de verkrijgingsprijs (of de waarde) van die aandelen en het gedeelte van het gerevaloriseerde gestorte kapitaal dat de verkregen aandelen vertegenwoordigen.
>
> Als de aandelen vóór de ontbinding worden verkregen onder de WVV-voorwaarden (of het toepasselijke rechtspersonenrecht), is die regel slechts van toepassing wanneer:
> 1. op de verkregen aandelen waardeverminderingen worden geboekt — tot het bedrag van de geboekte waardeverminderingen;
> 2. de aandelen worden vervreemd — ten bedrage van het negatieve verschil tussen verkoopprijs en verkrijgingsprijs/waarde;
> 3. de aandelen worden vernietigd of van rechtswege nietig worden;
> 4. en uiterlijk bij de ontbinding van de vennootschap.
>
> In de gevallen 2° tot 4° wordt het dividend in voorkomend geval verminderd met de reeds belaste waardeverminderingen (situatie 1°).
>
> **20%-regel**: in de mate dat de verkrijging tot gevolg heeft dat de vennootschap eigen aandelen in portefeuille houdt die **meer dan 20%** van haar kapitaal vertegenwoordigen, worden de nieuw verworven aandelen geacht te zijn vernietigd (situatie 3°). Bij gelijktijdige verkrijging van aandelen van verschillende overdragers of tegen verschillende aanschaffingswaarden: de vennootschap duidt de aandelen aan; bij gebrek aan aanduiding worden ze proportioneel geacht vernietigd te zijn. Zolang die aandelen in portefeuille blijven, is hun fiscale nettowaarde gelijk aan nul en vormt hun balanswaarde een uitgedrukte niet-verwezenlijkte meerwaarde (art. 44 § 1, 1° en art. 190 WIB 92 — zie code **1103** van vak Reserves B).
>
> Toepassing van die fictieve vernietiging laat art. 192 § 1 WIB 92 onverlet wanneer de vennootschap eigen aandelen die in portefeuille werden gehouden later overdraagt (link naar code **1051** in vak Reserves A).
>
> **Bijlage verplicht**: lijst van het aantal in het belastbare tijdperk verkregen eigen aandelen en van de reeds in bezit zijnde eigen aandelen — met datum, verkrijgingsprijs/-waarde, deel gestort kapitaal, vermelding of de aandelen zijn vernietigd of van rechtswege nietig zijn. Bij vervreemding: aantal, verkoopprijs, eventueel verlies. Bij geboekte waardeverminderingen: bedrag opgeven.

> **c) Overlijden, uittreding of uitsluiting van een vennoot (code 1303)** ⚖️ — art. 187 WIB 92:
> Wanneer het maatschappelijk vermogen **gedeeltelijk** wordt verdeeld ten gevolge van overlijden, uittreding of uitsluiting van een vennoot, moet het positieve verschil worden aangegeven tussen de uitkeringen of toekenningen (in geld, in effecten of in enige andere vorm) aan de belanghebbende of zijn rechthebbenden, en zijn aandeel in het gerevaloriseerde gestorte kapitaal.

> **d) Verdeling van maatschappelijk vermogen (codes 1305 + 1306)** ⚖️ — art. 209, eerste lid, WIB 92:
> Wanneer het maatschappelijk vermogen wordt verdeeld ten gevolge van **ontbinding of om enige andere reden**, moet het positieve verschil worden aangegeven tussen de uitkeringen in geld, in effecten of in enige andere vorm, en het gerevaloriseerde gestorte kapitaal.
>
> In de in art. 210 § 1 WIB 92 bedoelde gevallen wordt de werkelijke waarde van het maatschappelijk vermogen gelijkgesteld met een bij verdeling van het maatschappelijk vermogen uitgekeerde som.
>
> **Splitsing 1305 / 1306**:
> - Code **1305** ontvangt het gedeelte van de verdeling dat **voortkomt van een vermindering van de liquidatiereserve** (art. 184quater WIB 92) **én van de bijzondere liquidatiereserve** (art. 541 WIB 92). Op die component is de roerende voorheffing al via de afzonderlijke aanslag van 10% (art. 219quater WIB 92) afgewikkeld, zodat de toelichting deze component apart isoleert.
> - Code **1306** ontvangt het resterend bedrag: de verdeling **na aftrek** van dat liquidatiereserve-gedeelte.

> **Totaal van de uitgekeerde dividenden (code 1320)** ⚖️ — het totale bedrag van de hierboven bedoelde uitgekeerde dividenden (regels 1301 tot 1303, 1305 en 1306).

> **Algemene opmerking — vóór 01.01.1990** ⚖️: voor de in c) en d) vermelde verrichtingen die **vóór 01.01.1990** hebben plaatsgevonden, wordt verwezen naar de regels **1511** en **1512** van het vak "Bijzondere aanslagen met betrekking tot verrichtingen die vóór 01.01.1990 hebben plaatsgevonden".

---

## Didactische opmerkingen

> **Onderscheid dividend / inkoop / overlijden-uittreding / liquidatie-vereffening** — vier soorten "winstuitstroom" uit een vennootschap, vier WIB-92-artikelen, vier codes:
>
> | Verrichting | Wat gebeurt er? | Wettelijke basis | Code |
> |---|---|---|---|
> | **Gewoon dividend** | De algemene vergadering kent een uitkering toe aan aandelen/winstbewijzen; geen wijziging van het aandelenbestand. Omvat ook bepaalde terugbetalingen van kapitaal/uitgiftepremies en bepaalde interesten van vennoten-voorschotten | art. 18 WIB 92 | **1301** |
> | **Inkoop eigen aandelen** | De vennootschap verwerft haar eigen aandelen (in plaats van die uit te keren aan een derde of in te kopen voor pensioenuitkeringen). Fiscaal dividend = verkrijgingsprijs − overeenstemmend gerevaloriseerd gestort kapitaal | art. 186 WIB 92 | **1302** |
> | **Overlijden / uittreding / uitsluiting vennoot** | **Gedeeltelijke** verdeling van het maatschappelijk vermogen ten gunste van één vennoot (of zijn rechthebbenden); de vennootschap zelf blijft bestaan. Dividend = uitkering − aandeel in gerevaloriseerd gestort kapitaal | art. 187 WIB 92 | **1303** |
> | **Liquidatie / vereffening / "om enige andere reden"** | **Volledige** (of equivalente) verdeling van het maatschappelijk vermogen — bij ontbinding van de vennootschap of bij art. 210 § 1-operaties (gelijkgestelde verrichtingen). Dividend = uitkering − gerevaloriseerd gestort kapitaal | art. 209 (+ 210 § 1) WIB 92 | **1305 / 1306** |
>
> Het hartstuk in elk geval is hetzelfde: vergelijk de **uitkering** (in geld, effecten of enige andere vorm) met het **gerevaloriseerde gestorte kapitaal** dat ermee correspondeert. Het positieve verschil is een fiscaal dividend.

> **"Gehele of gedeeltelijke verdeling van maatschappelijk vermogen" — wat is dat?** ⚖️
> - **Gedeeltelijke** verdeling: een deel van het maatschappelijk vermogen verlaat de vennootschap omdat één of meer vennoten vertrekken (overlijden, uittreding, uitsluiting). De vennootschap zelf gaat verder. → code **1303** (art. 187).
> - **Gehele** verdeling: het volledige maatschappelijk vermogen wordt verdeeld onder de aandeelhouders bij **ontbinding** van de vennootschap of "om enige andere reden". De vennootschap houdt op te bestaan. → code **1305 + 1306** (art. 209 + 210).
> - In art. 210 § 1 WIB 92 worden bepaalde verrichtingen (bv. omzetting in een vennootschap die niet onderworpen is aan VenB, zetelverplaatsing met verlies van VenB-onderworpenheid) **gelijkgesteld** met een verdeling: de werkelijke waarde van het maatschappelijk vermogen wordt dan als uitkering beschouwd, ook al volgt geen feitelijke betaling.
>
> Het verschil dividend (1301) ↔ verdeling van maatschappelijk vermogen (1305/1306) zit dus in de aard van de verrichting: **periodieke winstuitkering aan blijvende aandeelhouders** versus **uitstroom bij vertrek van vennoten of bij beëindiging van de vennootschap**.

> **Splitsing 1305 ↔ 1306 — werkingsmechanisme bij liquidatie**:
> Bij vereffening van een vennootschap die in vorige tijdperken een liquidatiereserve heeft aangelegd (vak Reserves A, code 1012) of een bijzondere liquidatiereserve (art. 541 WIB 92, overgangsregime aj. 2013–2014), splitst de verdeling in twee componenten:
> 1. **Code 1305** = het deel van de verdeling dat voortkomt uit de vermindering van die liquidatiereserves. Op dat deel is bij aanleg al de **afzonderlijke aanslag van 10%** (art. 219quater WIB 92) geheven, zodat het bij uitkering aan aandeelhouder-natuurlijke-personen aan **0%** roerende voorheffing onderworpen is (volle korf benut). De vrijstelling van RV staat los van deze code; **1305** dient om die liquidatiereserve-component apart te kunnen identificeren.
> 2. **Code 1306** = de **rest** van de verdeling — d.w.z. het positieve verschil tussen de uitkering en het gerevaloriseerde gestorte kapitaal, **min** het 1305-bedrag. Op die rest is normale RV verschuldigd (tenzij vrijgesteld).
> Som **1305 + 1306** = totale verdeling van maatschappelijk vermogen die als fiscaal dividend kwalificeert volgens art. 209 WIB 92.

> **Verklaring 1322 — aangifte roerende voorheffing (formulier 273 A)** ⚖️:
> Wanneer ten minste één van de codes **1301, 1302, 1303 of 1306** is ingevuld, moet de vennootschap een aangifte in de roerende voorheffing (formulier **273 A**) indienen, **zelfs wanneer geen RV verschuldigd is** (bv. omdat de aandeelhouder onder een vrijstelling valt, of omdat het de liquidatiereserve-component is). Code **1322** is een aanvinkvakje waarmee de vennootschap die verplichting bevestigt. Merk op: **code 1305 staat niet in de lijst** — die component activeert de 273 A-verplichting niet, omdat de fiscale afwikkeling al gebeurde via de afzonderlijke aanslag 10%.

> **Verband met andere vakken van de aangifte**:
> - Het eindbedrag **1320** (uitgekeerde dividenden) is één van de drie hoofdcomponenten van het fiscale resultaat: **1080 PN** (belastbare gereserveerde winst) + **1240** (verworpen uitgaven) + **1320** (uitgekeerde dividenden) = **1410 PN** (resultaat van het belastbare tijdperk), via de Uiteenzetting van de winst.
> - Een verkrijging van eigen aandelen >20% kan via art. 188 WIB 92 doorwerken in vak Reserves A (zie code **1056** "Andere in meer" — vervreemding van eigen aandelen).
> - Code **1305** is het keerpunt van de liquidatiereserve-cyclus: aanleg via code **1012** (vak Reserves A) → jaarlijkse afzonderlijke aanslag 10% via art. 219quater → uitkering bij vereffening via code **1305** zonder bijkomende RV.

---

## D. Buitenlandse winst die geniet van een verminderde belasting (blz. 6)

> **Context** ⚖️: wanneer de vennootschap beschikt over één of meer **inrichtingen in het buitenland**, moet het totale bedrag van haar resterend resultaat volgens **oorsprong** worden onderverdeeld. Vooraleer die onderverdeling wordt gedaan, worden de verliezen van het belastbare tijdperk die in een land worden geleden, volgens bepaalde regels en in een bepaalde volgorde aangerekend op het totale bedrag van de winst uit andere landen (zie de rubriek "Verdeling van het resterend resultaat volgens oorsprong" van het vak Uiteenzetting van de winst).

### Onherroepelijk verzoek tot niet-aanrekening van verliezen

| Rubriek | Omschrijving | Code |
|---|---|---|
| — | **De vennootschap verzoekt op onherroepelijke wijze om de niet-aanrekening van verliezen op buitenlandse winst waarvan de belasting bij toepassing van een verdrag wordt verminderd** (art. 206/4, vierde lid en art. 207, zevende lid, WIB 92). Aanvinken in de elektronische aangifte; in een papieren aangifte op die regel **"JA"** vermelden. | **1340** |

> **Werking van het verzoek (code 1340)** ⚖️:
> In het geval in de categorie "niet bij verdrag vrijgestelde winst" winst is begrepen waarvan de belasting bij toepassing van internationale verdragen **wordt verminderd** (en dus niet integraal vrijgesteld), kan de belastingplichtige verzoeken dat de verliezen (van het belastbare tijdperk of compenseerbare vorige verliezen) **enkel worden aangerekend op de overige niet bij verdrag vrijgestelde winst**, zonder te worden aangerekend op de winst waarvan de belasting bij toepassing van een internationaal verdrag wordt verminderd.
>
> Dit verzoek is **onherroepelijk** — eens gemaakt, kan het niet meer worden teruggetrokken. Het vakje wordt alleen aangevinkt wanneer de vennootschap dat verzoek effectief doet voor het lopende belastbare tijdperk.
>
> **Wettelijke basis**: art. 206/4, vierde lid en art. 207, zevende lid, WIB 92.

---

## Samenvatting — Sleutelcodes vakken Uitgekeerde dividenden + Buitenlandse winst

| Concept | Vak | Primaire code | Omschrijving |
|---|---|---|---|
| **Eindsom uitgekeerde dividenden** | C | **1320** | Som 1301 + 1302 + 1303 + 1305 + 1306 — stroomt door naar Uiteenzetting van de winst |
| Gewone dividenden | C | **1301** | Gedecreteerd dividend + gelijkgestelde terugbetalingen + voorschot-interesten (art. 18 WIB 92) |
| Verkrijging van eigen aandelen | C | **1302** | Inkoop eigen aandelen — art. 186 WIB 92, met 20%-regel |
| Overlijden, uittreding of uitsluiting vennoot | C | **1303** | Gedeeltelijke verdeling vermogen — art. 187 WIB 92 |
| Verdeling vermogen — liquidatiereserve-deel | C | **1305** | Component uit vermindering liquidatiereserve (art. 184quater) + bijzondere liquidatiereserve (art. 541) |
| Verdeling vermogen — restant | C | **1306** | Verdeling na aftrek 1305-component — art. 209 + 210 § 1 WIB 92 |
| Verklaring 273 A | C | **1322** | Aanvinkvakje — verplichting aangifte RV bij 1301/1302/1303/1306 ingevuld |
| Verzoek niet-aanrekening verliezen op verminderd-belaste buitenlandse winst | D | **1340** | Onherroepelijk verzoek — art. 206/4 vierde lid + art. 207 zevende lid WIB 92 |
