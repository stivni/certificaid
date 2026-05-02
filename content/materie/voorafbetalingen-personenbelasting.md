---
tags: ["2.2", wip, materie]
niveau: toepassen
status: draft
bouwversie: 2
bronnen:
  - WIB92 art. 157-168, 175-178, 218
  - KB/WIB92 art. 64-66
---

# Voorafbetalingen — personenbelasting

Voorafbetalingen zijn **vrijwillige vooruitbetalingen** van de PB die de belastingplichtige doet aan de FOD Financiën gedurende het inkomstenjaar ([[bronnen/wetteksten/II-wib92|WIB92 art. 157-168]]). Voor **werknemers** is dit doorgaans niet nodig — de [[voorheffingen-personenbelasting#-bedrijfsvoorheffing-bv|bedrijfsvoorheffing]] dekt de belasting al. Voor **zelfstandigen, vrije beroepers en bedrijfsleiders** zijn voorafbetalingen feitelijk **verplicht**: zonder voorafbetalingen wordt een **vermeerdering** opgelegd die de belasting verhoogt.

De systematiek komt op het examen elk jaar terug — niet omwille van de berekening (die wordt door Tax-on-web automatisch gedaan) maar omdat de fiscale optimalisatie ervan onderdeel is van het [[fiscaal-advies-personenbelasting-formuleren|fiscaal advies]] aan de cliënt.

---

## 📌 Voorafbetaling (VA)
*Versement anticipé (VA)*

Vrijwillige betaling op een specifieke rekening van de FOD Financiën **gedurende het inkomstenjaar**, met als doel de uiteindelijke belastingschuld geleidelijk te vereffenen ([[bronnen/wetteksten/II-wib92|WIB92 art. 157]]).

**Wie?**
- **Verplicht in feite** (om vermeerdering te vermijden): zelfstandigen, bedrijfsleiders, vrije beroepers
- **Vrijwillig** (om bonificatie te ontvangen): werknemers met groot bijkomend inkomen

**Hoe?**
- Storting op het IBAN van het inningskantoor (rekeningnummer specifiek per regio en aanslagjaar)
- Vermelding van de **gestructureerde mededeling** (uniek per belastingplichtige)
- Te raadplegen via MyMinfin of via het ontvangen voorafbetalingsbericht (per kwartaal verstuurd)

**Vier kwartalen — vervaldagen** (wettelijk):

| Kwartaal | Vervaldag | Waarde-coëfficiënt (aj. 2026, indicatief) |
|---|---|---|
| **VA1** | 10 april | 9,00% |
| **VA2** | 10 juli | 7,50% |
| **VA3** | 10 oktober | 6,00% |
| **VA4** | 20 december | 4,50% |

**Vroegere VA = hogere fiscale waarde** — wie vroeg in het jaar betaalt, krijgt méér "fiscaal krediet" per euro dan wie laat betaalt.

---

## 🔢 Vermeerdering wegens onvoldoende VA

Als de som van **VA × waarde-coëfficiënt** **lager** is dan **vermeerderingscoëfficiënt × belastingschuld**, wordt een **vermeerdering** opgelegd ([[bronnen/wetteksten/II-wib92|WIB92 art. 158]]).

**Vereenvoudigde formule**:

```
Vermeerdering = Belasting × Vermeerderingsbasis%
              − (VA1 × 9% + VA2 × 7,5% + VA3 × 6% + VA4 × 4,5%)
```

Als deze som **negatief** is → geen vermeerdering.

**Vermeerderingsbasis%** (cijferzakboekje aj. 2026, indicatief):
- **6,75%** voor inkomstenjaar 2025
- Gebaseerd op de **referentierente** van de ECB (sterk gestegen sinds 2022)

**Plafond voor de vermeerdering**: 90% van de berekende vermeerdering (dwz: nooit meer dan 90% van de bovenstaande som als sanctie).

> [!info]- In de praktijk
>
> Een zelfstandige met geraamde belasting € 16 000 voor inkomstenjaar 2025.
>
> **Geen voorafbetalingen**:
> - Vermeerdering = € 16 000 × 6,75% = € 1 080
> - Effectieve heffing: € 16 000 + € 1 080 = € 17 080
>
> **Optimale voorafbetaling — VA1 ten belope van 75% van de belasting**:
> - VA1 = € 12 000 × 9% = € 1 080 fiscale waarde → dekt volledig de vermeerderingsbasis (€ 1 080)
> - Vermeerdering = € 1 080 − € 1 080 = € 0
> - Effectieve heffing: € 16 000 + € 0 = € 16 000 — bespaard € 1 080
>
> **Verspreid betalen** (€ 4 000 per kwartaal):
> - Fiscale waarde = € 4 000 × (9% + 7,5% + 6% + 4,5%) = € 4 000 × 27% = € 1 080
> - Ook vermeerdering = € 0 — gelijkwaardig fiscaal effect
>
> Belangrijk: vroeg in het jaar betalen heeft méér impact per euro dan laat — vandaar de aanbeveling VA1 te maximaliseren bij liquiditeitskrap.
>
> 🤖 *AI-aanvulling*

> [!warning]- Geen vermeerdering ≠ geen belasting — VA verminderen enkel de vermeerderingssanctie
> ❌ *"Door € 8 000 voorafbetaling te storten heb ik mijn belasting van € 16 000 al voor de helft betaald — saldo bij aanslag = € 8 000."*
>
> Klopt voor het saldo, maar **niet** voor de **vermeerdering**: VA's wegen mee tegen de **vermeerderingsbasis**, niet tegen de belastingschuld als zodanig. Een VA van € 8 000 in VA1 levert fiscale waarde € 720 op — voldoende om vermeerdering volledig te neutraliseren bij belasting € 16 000 (basis € 1 080) — maar de **belasting blijft € 16 000**. Saldo bij aanslag = € 16 000 − € 8 000 (VA) − € 0 (vermeerdering vermeden) = € 8 000.
>
> 🤖 *AI-aanvulling*

---

## 🔢 Berekening optimale VA — formule

Om vermeerdering volledig te vermijden:

```
∑ (VAᵢ × waarde-coëfficiëntᵢ) ≥ Belasting × vermeerderingsbasis%
```

Voor inkomstenjaar 2025 (6,75% vermeerderingsbasis):

```
∑ (VAᵢ × wᵢ) ≥ 0,0675 × Belasting
```

**Snelle vuistregels**:

| Strategie | Werking |
|---|---|
| **Volledige VA1** | VA1 = 0,75 × Belasting (≈ € 0,075 / 0,09 × Belasting) — geen verdere VA nodig |
| **Spreiden 25% per kwartaal** | VA1 = VA2 = VA3 = VA4 = 0,25 × Belasting (effect 27% gemiddeld → ruim voldoende) |
| **Maximale VA4 alleen** | VA4 = 1,5 × Belasting — vereist veel cash op het einde, aanbevolen alleen als geen andere optie |

---

## 🔢 Bonificatie wegens vroegtijdige betaling

Voor **werknemers** (= geen verplichte VA) kan een vrijwillige VA leiden tot een **bonificatie** — een vermindering van de belasting ([[bronnen/wetteksten/II-wib92|WIB92 art. 175]]).

**Voorwaarden**:
- VA in **VA1, VA2, of VA3** (niet VA4 — geen bonificatie)
- Bonificatietarieven (cijferzakboekje aj. 2026, indicatief):
  - VA1 (april): 4,50%
  - VA2 (juli): 3,00%
  - VA3 (oktober): 1,50%
  - VA4 (december): 0%

**Berekening bonificatie**:

```
Bonificatie = ∑ (VAᵢ × bonificatietariefᵢ)
```

**Gebruikssituaties voor werknemers**:
- **Hoog roerend inkomen** dat niet door BV gedekt is
- **Verkoop van een investeringspand** met meerwaarde
- **Bedrijfsleider die vrijwillig extra VA stort** om hogere effectieve return op zijn liquide middelen te halen (bonificatie tegenover bankrente vergelijken)

> [!info]- In de praktijk
>
> Een werknemer ontvangt in maart 2025 een grote prijs (divers inkomen € 50 000, niet gedekt door BV). Verwachte extra belasting: € 16 500 (33% afzonderlijk).
>
> **Optie A — afwachten**:
> - Geen extra heffing in 2025 omdat geen verplichte VA voor werknemers
> - Bij PB-aanslag aj. 2026: bijbetalen € 16 500
>
> **Optie B — VA1 € 16 500 storten**:
> - Bonificatie = € 16 500 × 4,5% = € 743 vermindering van belasting
> - Effectief belasting € 16 500 − € 743 = € 15 757 in plaats van € 16 500
>
> Vergelijking met cash op de bank @ 3% rente: € 16 500 × 3% × 9/12 ≈ € 371 rente in plaats van € 743 bonificatie → **VA1 is voordeliger** dan banksparen voor lange perioden.
>
> 🤖 *AI-aanvulling*

---

## 🔢 Strategie van VA voor zelfstandigen

Standaardadvies aan een nieuwe zelfstandige cliënt: **schat de jaarbelasting** en spreid VA over de 4 kwartalen.

**Stappen**:

1. **Schat het bruto-inkomen** voor het lopende jaar (op basis van vorig jaar of forecast)
2. **Bereken de geraamde belasting** via Tax-on-web simulator (op fictieve aangifte)
3. **Verdeel de geraamde belasting** over de 4 kwartalen (€ 4 000 per kwartaal bij € 16 000 belasting) of concentreer in VA1 als cash beschikbaar
4. **Stort op vervaldag** met gestructureerde mededeling
5. **Heroverweeg na 6 maanden** — bij gewijzigd inkomen kan VA3 of VA4 worden aangepast

**Voor cliënten met variabel inkomen** (consultancy, projecten): **conservatief** schatten en lichte overstroming aanvaarden — een teruggave is altijd beter dan een vermeerderingssanctie.

---

## ⚖️ Eerste 3 jaar zelfstandige — vrijstelling vermeerdering

Voor de **eerste 3 jaar** als zelfstandige in hoofdberoep wordt de **vermeerdering volledig kwijtgescholden** ([[bronnen/wetteksten/II-wib92|WIB92 art. 165]]) — een wettelijke vrijstelling om startende zelfstandigen liquiditeitsruimte te geven.

**Voorwaarden**:
- Zelfstandige in **hoofdberoep** (niet bijberoep)
- Geen voorafbetalingen vereist gedurende deze periode

**Strategisch advies**: zelfs zonder vermeerderingssanctie blijft VA aanbevolen om een **fiscale opbouw** te krijgen — bij PB-aanslag van € 12 000 zonder VA is een onverwachte cashflow-piek; met spreidingsbetaling is de schok beperkt.

---

## 🔒 Aangifteverplichting en mandataris

In de **PB-aangifte** (vak XI):
- VA's worden vooringevuld via MyMinfin (gebaseerd op werkelijk geboekte stortingen op rekening FOD)
- Mandataris controleert dat alle VA's correct zijn opgenomen
- Bij correcte storting met gestructureerde mededeling: automatische opname
- Bij foutieve mededeling: VA wordt **niet** automatisch toegekend → contact met inningskantoor

**Bewijs van VA**: bankafschrift met datum en gestructureerde mededeling — bewaarplicht 7 jaar.

---

## 🚩 Vergeten VA — fiscale verrassing

De drie meest voorkomende fiscale verrassingen rond VA:

| Probleem | Gevolg | Mitigatie |
|---|---|---|
| **Cliënt vergeet VA1** te storten | Volledige vermeerdering = ~ 6,75% van belasting | Reminder op 1 maart |
| **Verkeerde gestructureerde mededeling** | VA niet automatisch toegekend | Controle in MyMinfin op elk kwartaal |
| **Onderschatting belasting** (VA op basis van vorig jaar, dit jaar fors hoger) | Onvoldoende VA → vermeerdering | Halfjaarlijkse herraming |

> [!warning]- Vermeerdering van 6,75% wordt zelden teruggevorderd door bezwaar
> ❌ *"Ik vergat VA1 te storten omdat ik op vakantie was — bij bezwaar krijg ik die vermeerdering wel kwijt."*
>
> De vermeerdering wegens onvoldoende VA is **automatisch** en **niet ontheffbaar** door bezwaar omwille van persoonlijke omstandigheden ([[bronnen/wetteksten/II-wib92|WIB92 art. 159]]). Enkel zeer beperkte uitzonderingen gelden (overmacht in de strikte zin, onmogelijkheid van betaling). Vakantie, vergetelheid, cashflow-krap zijn geen geldige redenen — beste mitigatie blijft preventie via reminders en standing orders.
>
> 🤖 *AI-aanvulling*

---

## Relevant voor

**[[2.2-personenbelasting|2.2 Personenbelasting]]**

Kenniselementen:
- XV — Voorafbetalingen

### Voorbeeldvragen

> [!question]- Vermeerdering vermijden
>
> Een zelfstandige raamt zijn belasting voor inkomstenjaar 2025 op € 20 000. Hij wil de vermeerdering volledig vermijden door **één enkele** VA in VA1 (april). Hoeveel moet hij storten?
>
> > [!success]- Antwoord
> >
> > **VA1 ≈ € 15 000 (= 75% van € 20 000).**
> >
> > Vermeerderingsbasis = 6,75% × € 20 000 = € 1 350. Om dit volledig te neutraliseren met enkel VA1 (waarde-coëfficiënt 9%): VA1 × 9% ≥ € 1 350 → VA1 ≥ € 15 000. Wie liever spreidt: € 5 000 per kwartaal (totaal € 20 000) levert fiscale waarde 5 000 × (9 + 7,5 + 6 + 4,5)% = € 1 350 op — gelijkwaardig effect met betere cashflow-spreiding.
> >
> > *Zie: [[voorafbetalingen-personenbelasting#-vermeerdering-wegens-onvoldoende-va|Vermeerdering]] en [[voorafbetalingen-personenbelasting#-berekening-optimale-va-formule|Berekening optimale VA]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Bonificatie werknemer
>
> Een werknemer met groot bijkomend roerend inkomen (€ 30 000 dividenden geglobaliseerd) stort € 9 000 in VA1 (april 2025). Welke bonificatie krijgt hij?
>
> > [!success]- Antwoord
> >
> > **Bonificatie = € 9 000 × 4,5% = € 405.**
> >
> > Voor een werknemer (= geen verplichte VA) leveren vrijwillige VA's een **bonificatie** op (= belastingvermindering). VA1 heeft de hoogste bonificatiecoëfficiënt (4,5% voor aj. 2026, indicatief). Bonificatie verschijnt automatisch in de PB-aanslag als negatieve post — verlaagt te betalen of verhoogt teruggave. Vergelijken met banksparen @ 3% over 9 maanden: € 9 000 × 3% × 9/12 = € 203 → bonificatie wint met € 202 voordeel. **VA's zijn fiscaal voordeliger dan parkeren op spaarrekening** voor lange tijdspaden.
> >
> > *Zie: [[voorafbetalingen-personenbelasting#-bonificatie-wegens-vroegtijdige-betaling|Bonificatie]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Eerste jaar zelfstandige
>
> Een persoon start in januari 2025 als zelfstandige in hoofdberoep. Hij maakt geen voorafbetalingen. Bij PB-aanslag aj. 2026 wordt geraamd dat hij € 8 000 belasting verschuldigd is. Vermeerdering?
>
> > [!success]- Antwoord
> >
> > **Geen vermeerdering — vrijstelling eerste 3 jaar zelfstandige in hoofdberoep.**
> >
> > [[bronnen/wetteksten/II-wib92|WIB92 art. 165]] voorziet een **wettelijke vrijstelling** van vermeerdering wegens onvoldoende VA gedurende de **eerste 3 jaar** als zelfstandige in hoofdberoep. De € 8 000 belasting moet volledig betaald worden bij PB-aanslag, maar zonder bijkomende vermeerderingssanctie. Strategisch advies: zelfs zonder sanctie is het aan te raden om VA's te beginnen in jaar 2 of 3 om een fiscale opbouw te creëren — de overgang naar volledig betalen vanaf jaar 4 zonder VA is een grote schok.
> >
> > *Zie: [[voorafbetalingen-personenbelasting#️-eerste-3-jaar-zelfstandige-vrijstelling-vermeerdering|Eerste 3 jaar zelfstandige]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Verkeerde gestructureerde mededeling
>
> Een belastingplichtige stort € 5 000 in VA1 maar gebruikt per ongeluk de gestructureerde mededeling van zijn vrouw. Wordt deze VA aan zijn aanslag toegekend?
>
> > [!success]- Antwoord
> >
> > **Niet automatisch — moet gecorrigeerd worden via inningskantoor.**
> >
> > De gestructureerde mededeling is uniek per belastingplichtige en koppelt de storting aan zijn dossier. Bij gebruik van de mededeling van de partner wordt de VA toegekend aan **diens** dossier — niet aan dat van de stortingsbeoogde. Bij gezamenlijke aanslag is dit zelden problematisch (de VA wordt verrekend in de gemeenschappelijke aanslag), maar bij afzonderlijke aanslag of in geval van scheiding ontstaat een mismatch. **Mitigatie**: contact met inningskantoor om de VA om te boeken (bewijs nodig: bankafschrift + onderschrijven van bestemming). Voorkom door zorgvuldig kopiëren van de juiste gestructureerde mededeling vanuit MyMinfin.
> >
> > *Zie: [[voorafbetalingen-personenbelasting#-aangifteverplichting-en-mandataris|Aangifteverplichting]]*
>
> 🤖 *AI-aanvulling*
